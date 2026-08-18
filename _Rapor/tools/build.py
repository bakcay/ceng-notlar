#!/usr/bin/env python3
"""Arşivi tarar, dönüştürür ve MD/ altına yazar.

Kaynak SALT-OKUNUR açılır. Yalnızca MD/ altına yazılır — bu kural
_guard_dest() ile her tek yazma işleminde makine tarafından denetlenir.

Kullanım:
    python3 build.py                          # tam dönüşüm
    python3 build.py --only Donanim,Guvenlik  # sadece bu kategoriler
    python3 build.py --dry-run                # hiçbir şey yazmaz, planı basar
"""
import argparse
import json
import os
import re
import shutil
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from categories import categorize
from classify import role, is_bundle_folder
from dedup import file_hash, text_hash, find_duplicates
from extract import (ExtractError, FALLBACK_LOG, GarbageError, RECOVERED,
                     REPAIRED, doc_metadata, extract_html, extract_pdf_text,
                     extract_text, read_htm, recover_doc_text)
from html2md import html_to_markdown, text_to_markdown
from translit import safe_name, slug_from_folder, title_from_folder

ROOT = "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri"
OUT = os.path.join(ROOT, "MD")
# MD/_Rapor tasarim dokumanini, plani, arac dizinini ve onun git deposunu
# barindirir. Build'in urettigi tek sey oradaki stats.json/dups.json'dur;
# dizinin kendisi ASLA temizlik kapsamina girmez (bkz. _protected).
RAPOR = os.path.join(OUT, "_Rapor")

SHORT_DOC_WORDS = 300
SAFE_PATH_RE = re.compile(r"^[A-Za-z0-9._/-]+$")

# Normal donusum bu kadar kelimeden az uretirse "bos cikti" sayilir ve
# kurtarma denenir; kurtarma ancak bu kadar kelime bulursa kabul edilir.
MIN_BODY_WORDS = 3
MIN_SALVAGE_WORDS = 20
_HTML_COMMENT_RE = re.compile(r"<!--(.*?)-->", re.S)
_TAGLIKE_RE = re.compile(r"<[^>]+>")


# --- Guvenlik: yalnizca MD/ altina yazilir -------------------------------

def _guard_dest(path):
    """Hedefin MD/ altinda oldugunu ve ASCII-guvenli oldugunu dogrular.

    Arsivin dokunulmazligi tek bir yerde, makine tarafindan uygulanir:
    kopyalama/yazma/mkdir yapan HER cagri once buradan gecer. Bir hata
    kaynak agacina yazmaya calisirsa surec durur, sessizce devam etmez.
    """
    real_out = os.path.realpath(OUT)
    real = os.path.realpath(path)
    if real != real_out and not real.startswith(real_out + os.sep):
        raise RuntimeError("MD/ disina yazma girisimi: %s" % path)
    rel = os.path.relpath(path, OUT)
    if rel != "." and not SAFE_PATH_RE.match(rel.replace(os.sep, "/")):
        raise RuntimeError("cikti yolu ASCII-guvenli degil: %s" % rel)
    return path


def _protected(path):
    """Yol MD/_Rapor altinda mi? Oradaki hicbir sey silinmez.

    Sembolik baglantiyla kacis olmasin diye realpath uzerinden bakilir.
    """
    real = os.path.realpath(path)
    rap = os.path.realpath(RAPOR)
    return real == rap or real.startswith(rap + os.sep)


def _guard_delete(path):
    """Silinecek yolun MD/ altinda ve _Rapor DISINDA oldugunu dogrular.

    _guard_dest'ten ayri tutuldu: yazarken hedefin ASCII-guvenli olmasini
    sart kosuyoruz, ama SILERKEN tam tersi gerekir -- bayat kalinti zaten
    ASCII disi bir adla durabilir ve temizlenebilmelidir. Yaprağın kendisi
    icin realpath KULLANILMAZ (disari isaret eden bir sembolik baglanti
    silinirken hedefi degil baglantiyi sileriz); kapsam denetimi ust
    dizinin realpath'i uzerinden yapilir, boylece sembolik bir dizinle
    MD/ disina cikmak mumkun degildir.
    """
    real_out = os.path.realpath(OUT)
    parent = os.path.realpath(os.path.dirname(path))
    if parent != real_out and not parent.startswith(real_out + os.sep):
        raise RuntimeError("MD/ disinda silme girisimi: %s" % path)
    if os.path.realpath(path) == real_out:
        raise RuntimeError("MD/ kokunu silme girisimi: %s" % path)
    if _protected(path):
        raise RuntimeError("_Rapor korumalidir, silinemez: %s" % path)
    return path


# Uretilen her dosyanin yolu buraya yazilir. Temizlik (bkz. _sweep) tam
# olarak bu kumeye dayanir: kumede olmayan her sey onceki calismadan kalan
# bayat ciktidir.
MANIFEST = set()

# report.py'nin build agaci ICINE yazdigi dosyalar. Yollari sabittir (bir
# yeniden adlandirmayla bayatlayamazlar) ve build tek basina calistirildiginda
# silinmeleri gereksiz veri kaybi olurdu; bu yuzden temizlikten muaftirlar.
REPORT_OUTPUTS = ("INDEX.md", os.path.join("_Arsiv", "README.md"))


def _mkdir(path):
    _guard_dest(path)
    os.makedirs(path, exist_ok=True)


def _write_text(path, text):
    _guard_dest(path)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    MANIFEST.add(path)


def _copy_file(src, dest):
    _guard_dest(dest)
    shutil.copy2(src, dest)
    MANIFEST.add(dest)


def _sweep(roots, keep):
    """`roots` altinda `keep` kumesinde olmayan dosyalari siler.

    build.py cikti dizinine yazarken onceki calismayi TEMIZLEMIYORDU: bir
    dosya yeniden adlandirildiginda eski ad diskte kaliyor, INDEX'e giriyor
    ve gercekte olmayan bir belge varmis gibi gorunuyordu (uc dosyada bilfiil
    yasandi, elle silindi). Artik her calisma tam olarak niyet ettigi dosya
    kumesini birakir.

    Karsilastirma _Names.key ile (NFC + casefold) yapilir: macOS dosya
    adlarini NFD dondurur ve dosya sistemi buyuk/kucuk harf duyarsizdir --
    duz `in` testi yeni yazilan dosyalari "bayat" sanip silerdi.
    """
    keep_keys = {_Names.key(p) for p in keep}
    doomed, seen_dirs = [], []
    for root in roots:
        if not os.path.isdir(root) or _protected(root):
            continue
        for dp, dn, fn in os.walk(root, topdown=True):
            dn[:] = [d for d in dn if not _protected(os.path.join(dp, d))]
            seen_dirs.append(dp)
            for f in fn:
                p = os.path.join(dp, f)
                if _Names.key(p) not in keep_keys:
                    doomed.append(p)

    removed = []
    for p in doomed:
        _guard_delete(p)
        os.remove(p)
        removed.append(os.path.relpath(p, OUT))
    # Icerigi kalmayan dizinler de bayattir (ornegin yeniden adlandirilmis
    # bir konu klasoru). En derinden yuzeye dogru budanir.
    for dp in sorted(seen_dirs, key=lambda d: d.count(os.sep), reverse=True):
        if os.path.realpath(dp) == os.path.realpath(OUT) or _protected(dp):
            continue
        if os.path.isdir(dp) and not os.listdir(dp):
            _guard_delete(dp)
            os.rmdir(dp)
            removed.append(os.path.relpath(dp, OUT) + "/")

    # Son kosul: taranan alanda artik SADECE niyet edilen dosyalar var.
    # Bu, "build tam olarak urettigi kadarini birakir" iddiasini her
    # calismada makineye dogrulatir; iddia yorumda kalmaz.
    leftover = []
    for root in roots:
        if not os.path.isdir(root) or _protected(root):
            continue
        for dp, dn, fn in os.walk(root, topdown=True):
            dn[:] = [d for d in dn if not _protected(os.path.join(dp, d))]
            leftover += [os.path.relpath(os.path.join(dp, f), OUT)
                         for f in fn
                         if _Names.key(os.path.join(dp, f)) not in keep_keys]
    if leftover:
        raise RuntimeError("temizlik sonrasi beklenmeyen dosya kaldi: %s"
                           % leftover[:5])
    return sorted(removed)


# --- Ad cakismasi yonetimi ----------------------------------------------
#
# Iki farkli konu klasoru ayni slug'a inebilir: 'CIFT ANAHTARLI BILGI
# GUVENLIGI' ve 'ÇİFT ANAHTARLI BİLGİ GÜVENLİĞİ' ikisi de Guvenlik/
# altinda 'Cift-Anahtarli-Bilgi-Guvenligi' uretir. Ayrica ayni kategoride
# ayni adli iki arsiv dosyasi vardir (Web-Gelistirme/html2000.chm x2,
# FILELIST.XML x2). Brief'teki referans kod bu durumlarda ikinci dosyayi
# SESSIZCE ilkinin uzerine yazar. Butun hedef yollar tek bir kayit
# defterinden dagitilir; macOS dosya sistemi varsayilan olarak
# buyuk/kucuk harf duyarsiz oldugu icin anahtar casefold'lanir.

class _Names(object):
    def __init__(self):
        self.taken = {}

    @staticmethod
    def key(path):
        return unicodedata.normalize("NFC", path).casefold()

    def is_free(self, path):
        return self.key(path) not in self.taken

    def take(self, path):
        k = self.key(path)
        if k in self.taken:
            raise RuntimeError("hedef yol cakismasi: %s" % path)
        self.taken[k] = path
        return path

    def alloc(self, dirpath, base, ext=""):
        """dirpath icinde 'base+ext' serbest degilse '-2', '-3' ... ekler."""
        cand, i = base, 1
        while not self.is_free(os.path.join(dirpath, cand + ext)):
            i += 1
            cand = "%s-%d" % (base, i)
        return self.take(os.path.join(dirpath, cand + ext)), cand

    def alloc_stem(self, dirpath, slug):
        """Bir konu klasoru icin 'govde' ad ayirir.

        Govde hem ek klasoru adi (dirpath/govde/) hem de .md/.pdf dosya
        adlarinin koku olarak kullanilir; ucu de ayni anda serbest
        olmalidir ki tek konunun ciktilari birbirinden ayrilmasin.
        """
        cand, i = slug, 1
        while not all(self.is_free(os.path.join(dirpath, cand + e))
                      for e in ("", ".md", ".pdf")):
            i += 1
            cand = "%s-%d" % (slug, i)
        self.take(os.path.join(dirpath, cand))
        return cand


def asset_rel(rel):
    """Ek dosyanın çıktıdaki göreli yolunu üretir.

    Konu klasörünün ilk alt dizini bir 'sarmalayıcı'dır — e-kitap paketlerinde
    'ekitap-Hakki_Ícal-Kitap_ik_PHP_÷rnekler/' gibi mojibake bir kabuk. Bu kabuk
    atılır, altındaki yapı OLDUĞU GİBİ korunur; böylece 'res/logo.gif' ve
    'konular/11.htm' gibi iç referanslar çalışmaya devam eder.
    Kalan bileşenler safe_name'den geçirilir (350 ek dosyanın yalnızca 3'ü
    bu adımda değişir).

    Kabuğun atılması ancak konu içindeki TÜM ek dosyaları aynı ilk bileşeni
    paylaşıyorsa güvenlidir; aksi halde iki farklı ağaç düzleşip çakışır.
    Ölçüm: 249 konunun hiçbirinde ek dosyalar birden fazla ilk-seviye dizine
    yayılmıyor (çakışma sayısı 0). Yine de çağıran taraf her hedefi
    kayıt defterinden geçirir, yani sessiz üzerine-yazma yapısal olarak
    imkânsızdır.
    """
    parts = rel.split(os.sep)
    if len(parts) > 1:
        parts = parts[1:]
    return "/".join(safe_name(p) for p in parts)


def scan(root=ROOT):
    """Kaynak envanterini çıkarır. MD/ atlanır."""
    entries = []
    for topic in sorted(os.listdir(root)):
        tdir = os.path.join(root, topic)
        # MD/ cikti dizinidir; nokta ile baslayan dizinler arac artigidir
        # (.claude gibi), arsivin konusu degildir (Task 2 incelemesi).
        if topic == "MD" or topic.startswith(".") or not os.path.isdir(tdir):
            continue
        # NOT: 'topic in BUNDLE_FOLDERS' KULLANILMAZ. macOS dosya adlarini
        # NFD dondurur, kume literalleri NFC'dir; naif uyelik testi 5 paket
        # klasorunun 3'unde sessizce basarisiz olup 134 dosyayi yanlis
        # siniflandirir. is_bundle_folder() once NFC'ye normalize eder.
        bundle = is_bundle_folder(topic)
        category = categorize(topic)
        for dp, dn, fn in os.walk(tdir):
            for f in sorted(fn):
                path = os.path.join(dp, f)
                rel = os.path.relpath(path, tdir)
                r = role(path, rel, bundle=bundle)
                if r == "atla":
                    continue
                entries.append({
                    "path": path, "topic": topic, "rel": rel, "role": r,
                    "category": category, "slug": slug_from_folder(topic),
                    "title": title_from_folder(topic),
                })
    return entries


def _group_by_topic(entries):
    by_topic = {}
    for e in entries:
        by_topic.setdefault(e["topic"], []).append(e)
    return by_topic


# --- Cikarim onbellegi ---------------------------------------------------
#
# Referans kod her 'belge' icin extract_text'i IKI kez (tekrar analizi +
# yazma) ve ayrica extract_html'i bir kez cagirir; PDF'lerde swift
# suzgecini iki kez calistirir. Ayni dosyayi iki kez cikarmak yalnizca
# yavas degil, RECOVERED/REPAIRED gibi modul duzeyi kayit listelerini de
# sisirir. Her dosya her kipte en fazla bir kez cikarilir.

_TEXT_CACHE = {}


def _ext_of(e):
    return e["rel"].rsplit(".", 1)[-1].lower() if "." in e["rel"] else ""


def plain_text(e):
    """Belgenin düz metnini döndürür: (metin, kurtarildi_mi).

    ExtractError yükseltebilir. GarbageError (textutil'in yenildiği 4 büyük
    OLE .doc dosyası) burada yakalanır ve recover_doc_text ile karşılanır;
    böylece bu dosyalar da tekrar analizine ve kelime sayımına girer.
    """
    path = e["path"]
    if path in _TEXT_CACHE:
        return _TEXT_CACHE[path]
    if _ext_of(e) == "pdf":
        out = (extract_pdf_text(path), False)
    else:
        try:
            out = (extract_text(path), False)
        except GarbageError:
            out = (recover_doc_text(path), True)
    _TEXT_CACHE[path] = out
    return out


def _to_markdown(e):
    """Bir 'belge' girdisini (markdown_govde, metadata, kelime_sayisi) yapar."""
    ext = _ext_of(e)
    txt, recovered = plain_text(e)
    words = len(txt.split())
    if ext == "pdf":
        return text_to_markdown(txt), {"author": None, "year": None}, words
    if ext in ("htm", "html"):
        raw = read_htm(e["path"])
        return html_to_markdown(raw), doc_metadata(raw), words
    # 4 buyuk .doc dosyasini textutil ayristiramiyor ve ham OLE baytlari
    # dokuyor. extract.py bunu GarbageError ile bildirir; UTF-16LE kurtarma
    # duz metin dondurur, bicimlendirme (baslik/tablo) kurtarilamaz
    # (Task 3b). plain_text() bunu zaten tespit ettigi icin extract_html'i
    # (10-34 MB dosyada ikinci pahali textutil gecisi) hic denemeyiz.
    if recovered:
        return text_to_markdown(txt), {"author": None, "year": None}, words
    raw = extract_html(e["path"])
    return html_to_markdown(raw), doc_metadata(raw), words


def _salvage(e):
    """Normal dönüşüm boş gövde ürettiğinde son çare metin kurtarma.

    Tam arşiv taramasında 308 çıktının 2'si boş gövdeyle sonuçlandı ve
    ikisi de gerçek içerik kaybıydı:

    * `INTERTECH/INTERTECH.doc` (6 MB) — gövdenin tamamı gömülü alt
      dokümandır; textutil yalnızca `EMBED Word.Document.8 \\s` alan
      kodlarını çıkarır, html2md bunları (doğru olarak) siler ve geriye
      hiçbir şey kalmaz. looks_like_garbage bu dosyayı yakalamaz, çünkü
      alan kodları düz ASCII'dir — yani GarbageError yolu devreye
      girmez. Ham OLE taraması 9.871 kelime gerçek Türkçe metin bulur.
    * `FLASH DERSLERİ/.../DERS111.html` — Flash dışa aktarım artefaktı;
      1.755 kelimelik ders metni HTML YORUMU içindedir, yorum dışında
      1 kelime vardır. Yorumları içerik saymak genel bir kural olarak
      YANLIŞ olurdu; bu yüzden html2md'ye dokunulmaz, kural yalnızca
      "aksi halde dosya bomboş kalacak" durumunda uygulanır.

    Dönüş: (markdown_govde, kelime_sayisi) veya kurtarma da yetersizse
    None. Her tetiklenme stats['kurtarma'] altında raporlanır.
    """
    ext = _ext_of(e)
    # Son care kurtarma BASARISIZ olabilir (ozellikle recover_doc_text artik
    # bos sonucta ExtractError yukseltiyor -- bkz. extract.py F5). Bu bir
    # cokme sebebi degil, "kurtarilamadi" demektir: None donulur, cagiran
    # taraf dosyayi 'bos' olarak raporlar.
    try:
        if ext in ("htm", "html"):
            raw = read_htm(e["path"])
            txt = "\n\n".join(m.group(1) for m in _HTML_COMMENT_RE.finditer(raw))
            txt = _TAGLIKE_RE.sub(" ", txt)
        elif ext in ("doc", "rtf"):
            txt, recovered = plain_text(e)
            if not recovered:
                txt = recover_doc_text(e["path"])
        else:
            return None
    except ExtractError:
        return None
    words = len(txt.split())
    if words < MIN_SALVAGE_WORDS:
        return None
    return text_to_markdown(txt), words


def _footer(src_path, meta, extras):
    src = unicodedata.normalize("NFC", os.path.relpath(src_path, ROOT))
    bits = ["Kaynak: `%s`" % src]
    if meta.get("author"):
        bits.append(meta["author"])
    if meta.get("year"):
        bits.append(meta["year"])
    lines = ["---", "*" + " — ".join(bits) + "*"]
    for label, rel, n in extras:
        lines.append("*%s: `%s` (%d dosya)*" % (label, rel, n))
    return "\n".join(lines)


def _unique_by_path(records):
    """Kayit listesini 'path' alanina gore tekillestirir (ilk kayit kazanir).

    FALLBACK_LOG, REPAIRED/RECOVERED'in aksine her COZUMLEME icin bir kayit
    tutar (sozlesmesi budur). Boru hattinda ayni .htm iki kez okunabiliyor
    (normal donusum + _salvage); rapor "dosya basina" okundugu icin ayni
    dosya iki kez listeleniyordu. Cozumleme deterministik oldugundan ayni
    dosyanin iki kaydi zaten ozdestir.
    """
    seen, out = set(), []
    for rec in records:
        if rec["path"] in seen:
            continue
        seen.add(rec["path"])
        out.append(rec)
    return out


def build(root=ROOT, only=None, dry_run=False):
    entries = scan(root)
    if only:
        entries = [e for e in entries if e["category"] in only]

    MANIFEST.clear()
    stats = {"belge": 0, "ornek": 0, "gorsel": 0, "arsiv": 0, "yonlendirme": 0,
             "dizin": 0, "hata": [], "kisa": [], "yeniden_adlandirilan": [],
             "cakisma": [], "kurtarma": [], "bos": [], "yazilan": [],
             # Task 9 bu iki listeyi "kelime sayisi korunumu" ve "bos cikti"
             # kontrollerinden muaf tutmak icin kullanir: yonlendirme ve dizin
             # dosyalarinin govdesi tasarim geregi bir-iki cumledir.
             "yonlendirme_yollari": [], "dizin_yollari": [], "silinen": []}

    # 1) Tekrar analizi — yalnızca 'belge' rolündekiler üzerinde
    docs = [e for e in entries if e["role"] == "belge"]
    hashed = []
    for e in docs:
        try:
            txt, _ = plain_text(e)
        except ExtractError as ex:
            stats["hata"].append((e["path"], str(ex)))
            continue
        hashed.append({"path": e["path"], "fhash": file_hash(e["path"]),
                       "thash": text_hash(txt), "words": len(txt.split())})
    dups = find_duplicates(hashed)
    demoted = {p for g in dups["binary"] for p in g[1:]}
    redirect = {}
    for g in dups["text"]:
        for p in g[1:]:
            redirect[p] = g[0]

    if dry_run:
        print(json.dumps({"toplam": len(entries), "belge": len(docs),
                          "ikili_tekrar": len(dups["binary"]),
                          "metin_tekrar": len(dups["text"]),
                          "cikarim_hatasi": len(stats["hata"])},
                         ensure_ascii=False, indent=2))
        stats["dups"] = dups
        return stats

    # 2) Yazma
    names = _Names()
    touched_dirs = set()          # --only ile temizligin kapsami
    by_topic = _group_by_topic(entries)
    for topic, group in sorted(by_topic.items()):
        cat = group[0]["category"]
        cat_dir = os.path.join(OUT, cat)
        _mkdir(cat_dir)
        touched_dirs.add(cat_dir)
        stem = names.alloc_stem(cat_dir, group[0]["slug"])

        belgeler = [e for e in group
                    if e["role"] == "belge" and e["path"] not in demoted]
        ornekler = [e for e in group if e["role"] == "ornek"]
        gorseller = [e for e in group if e["role"] == "gorsel"]
        arsivler = [e for e in group if e["role"] == "arsiv"]

        # Ek klasörleri
        assets = os.path.join(cat_dir, stem)
        extras = []

        def _copy(items, subdir, counter, label):
            if not items:
                return
            n = 0
            for e in items:
                out_rel = asset_rel(e["rel"])
                dest = os.path.join(assets, subdir, out_rel)
                # Ek dosyalar birbirine dosya adiyla referans verir
                # (include/require, <img src>); yeniden adlandirma
                # baglantiyi kirar. Bu yuzden cakisma cozulmez, RAPORLANIR
                # -- olcumde 0 tane var, olursa gorunur olmali.
                if not names.is_free(dest):
                    stats["cakisma"].append((e["path"], dest))
                    continue
                names.take(dest)
                _mkdir(os.path.dirname(dest))
                _copy_file(e["path"], dest)
                if os.path.basename(out_rel) != os.path.basename(e["rel"]):
                    stats["yeniden_adlandirilan"].append((e["rel"], out_rel))
                stats[counter] += 1
                n += 1
            if n:
                extras.append((label, "%s/%s/" % (stem, subdir), n))

        _copy(ornekler, "ornekler", "ornek", "Örnekler")
        _copy(gorseller, "gorseller", "gorsel", "Görseller")

        for e in arsivler:
            d = os.path.join(OUT, "_Arsiv", cat if cat != "_Arsiv" else "Diger")
            _mkdir(d)
            touched_dirs.add(d)
            orig = os.path.basename(e["rel"])
            name = safe_name(orig)
            base, dot, ext = name.rpartition(".")
            if not dot:
                base, ext = name, ""
            dest, _ = names.alloc(d, base, ("." + ext) if ext else "")
            if os.path.basename(dest) != orig:
                stats["yeniden_adlandirilan"].append(
                    (e["rel"], os.path.basename(dest)))
            _copy_file(e["path"], dest)
            stats["arsiv"] += 1

        # Konu klasorunde hic 'belge' yok ama ek dosya var: ekler bir
        # .md'den referans edilmezse cikti agacinda erisilemez kalir.
        # Kucuk bir giris sayfasi yazilir.
        if not belgeler and extras:
            dest, _ = names.alloc(cat_dir, stem, ".md")
            body = ("Bu konu klasöründe Markdown'a çevrilebilecek bir belge "
                    "yok; yalnızca aşağıdaki ek dosyalar bulunuyor.")
            _write_text(dest, "# %s\n\n%s\n\n%s\n"
                        % (group[0]["title"], body,
                           _footer(os.path.join(root, topic),
                                   {"author": None, "year": None}, extras)))
            stats["dizin"] += 1
            stats["yazilan"].append(dest)
            stats["dizin_yollari"].append(dest)
            continue

        # Belgeler
        for i, e in enumerate(sorted(belgeler, key=lambda x: x["rel"])):
            base = stem if len(belgeler) == 1 else "%s-%d" % (stem, i + 1)
            dest, name = names.alloc(cat_dir, base, ".md")

            if e["path"] in redirect:
                target = unicodedata.normalize(
                    "NFC", os.path.relpath(redirect[e["path"]], ROOT))
                body = ("Bu içerik arşivde birden fazla kez yer alıyor. "
                        "Asıl kopya: `%s`" % target)
                _write_text(dest, "# %s\n\n%s\n" % (e["title"], body))
                stats["yonlendirme"] += 1
                stats["yazilan"].append(dest)
                stats["yonlendirme_yollari"].append(dest)
                continue

            try:
                body, meta, words = _to_markdown(e)
            except ExtractError as ex:
                stats["hata"].append((e["path"], str(ex)))
                continue

            # Bos govde = sessiz icerik kaybi. Once kurtarma denenir;
            # kurtarma da yetersizse dosya yine yazilir ama 'bos' olarak
            # raporlanir -- gorunmez kalmaz.
            if len(body.split()) < MIN_BODY_WORDS:
                salv = _salvage(e)
                if salv is None:
                    stats["bos"].append(e["path"])
                else:
                    body, words = salv
                    stats["kurtarma"].append((e["path"], words))

            _write_text(dest, "# %s\n\n%s\n\n%s\n"
                        % (e["title"], body, _footer(e["path"], meta, extras)))
            stats["belge"] += 1
            stats["yazilan"].append(dest)
            if words is not None and words < SHORT_DOC_WORDS:
                stats["kisa"].append((dest, words))

            # PDF ise orijinali yanına kopyala (spec §10)
            if _ext_of(e) == "pdf":
                pdf_dest, _ = names.alloc(cat_dir, name, ".pdf")
                _copy_file(e["path"], pdf_dest)

    # 3) Sessiz uzerine-yazma olmadi mi? Yazilan her .md'nin hedef yolu
    #    benzersiz olmali (macOS buyuk/kucuk harf duyarsiz -> casefold).
    keys = [_Names.key(p) for p in stats["yazilan"]]
    if len(keys) != len(set(keys)):
        raise RuntimeError("cakisan .md hedefi: %d yazma, %d benzersiz yol"
                           % (len(keys), len(set(keys))))

    # 4) Bayat cikti temizligi. Tam calismada butun MD/ (elbette _Rapor
    #    haric) taranir; --only ile YALNIZCA bu calismada dokunulan kategori
    #    ve _Arsiv dizinleri taranir -- aksi halde kismi bir build butun
    #    diger kategorileri silerdi.
    roots = [OUT] if not only else sorted(touched_dirs)
    keep = set(MANIFEST) | {os.path.join(OUT, r) for r in REPORT_OUTPUTS}
    stats["silinen"] = _sweep(roots, keep)

    # 5) Cikarim katmaninin kayit defterleri. Bunlar modul duzeyindedir ve
    #    yalnizca bu calisma boyunca dolar; rapor (Task 8) bunlari
    #    stats.json'dan okur, extract.py'i tekrar calistirmaz.
    stats["mojibake_onarilan"] = [[p, n] for p, n in REPAIRED]
    stats["utf16_kurtarilan"] = [[p, n] for p, n in RECOVERED]
    # FALLBACK_LOG, REPAIRED/RECOVERED'in aksine her COZUMLEME icin bir
    # kayit tutar (sozlesmesi budur). Boru hattinda ayni .htm iki kez
    # okunabiliyor (normal donusum + _salvage), bu da raporda ayni dosyayi
    # iki kez gosteriyordu. Rapor "dosya basina" okunacagi icin burada
    # yola gore tekillestirilir; cozumleme deterministik oldugu icin ayni
    # dosyanin iki kaydi zaten ozdestir.
    stats["kodlama_yedegi"] = _unique_by_path(FALLBACK_LOG)
    stats["dups"] = dups
    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    only = a.only.split(",") if a.only else None
    s = build(only=only, dry_run=a.dry_run)
    if not a.dry_run:
        print("belge:%d yonlendirme:%d dizin:%d ornek:%d gorsel:%d arsiv:%d "
              "hata:%d kisa:%d cakisma:%d kurtarma:%d bos:%d silinen:%d"
              % (s["belge"], s["yonlendirme"], s["dizin"], s["ornek"],
                 s["gorsel"], s["arsiv"], len(s["hata"]), len(s["kisa"]),
                 len(s["cakisma"]), len(s["kurtarma"]), len(s["bos"]),
                 len(s["silinen"])))
        for p in s["silinen"]:
            print("  bayat cikti silindi:", p)
        rap = RAPOR
        _mkdir(rap)
        with open(_guard_dest(os.path.join(rap, "stats.json")), "w",
                  encoding="utf-8") as fh:
            json.dump({k: v for k, v in s.items() if k != "dups"}, fh,
                      ensure_ascii=False, indent=2)
        with open(_guard_dest(os.path.join(rap, "dups.json")), "w",
                  encoding="utf-8") as fh:
            json.dump(s["dups"], fh, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
