#!/usr/bin/env python3
"""Çıktı doğrulaması. build.py + report.py'den SONRA çalışır.

Spec §12'nin beş kontrolü + altıncı bir kontrol (boş çıktı):

1. Kelime sayısı korunumu   2. Türkçe karakter bütünlüğü
3. Dosya adı geçerliliği    4. Kayıp yok
5. Link bütünlüğü           6. Boş / neredeyse boş çıktı yok

Her kontrol {check, ok, detail, notes} döndürür. `notes`, KALDI saymayan
ama insanın görmesi gereken bulgular içindir (ölçüm artefaktı, kaynağı
gerçekten kısa olan dosyalar gibi) — bir bulguyu sessizce muaf tutmak
yerine ayrı bir başlık altında GÖSTERMEK için.

CLI çıkış kodu: hepsi geçerse 0, biri kalırsa 1.
"""
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import is_bundle_folder, role
from extract import (ExtractError, GarbageError, extract_pdf_text,
                     extract_text, recover_doc_text)
from html2md import EMBED_RE, FIELD_CODE_RE
from report import body_words, load_stats, need, read_md

ROOT = "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri"
OUT = os.path.join(ROOT, "MD")
RAPOR = os.path.join(OUT, "_Rapor")

# --- Mojibake imzalari ---------------------------------------------------
#
# Iki AYRI hasar turu var ve ikisi de aranmali:
#
# A) UTF-8 baytlarinin Latin-1/CP1252 olarak cozulmesi -- "ü" -> "Ã¼".
#    Cok baytli dizilerdir, Turkce metinde asla gecmezler.
# B) CP1254 baytlarinin Latin-1 olarak cozulmesi -- "İ" -> "Ý". Arsivde
#    ALTI kaynak dosyada tam olarak bu hasar vardi (bkz. extract.py
#    MOJIBAKE_MAP); onarildilar ve bir daha geri gelmemeli. Bu imza tek
#    karakterlidir: Turkcede kullanilmayan Izlandaca/Eski Ingilizce
#    harfler. Brief yalnizca (A)'yi ariyordu, yani onarilan hasarin geri
#    gelmesini fark edemezdi.
# (A) icin TEK karakterli imza KULLANILMAZ: "\u00c3" ve "\u00c4" cok baytli
# dizinin ilk baytidir ama ayni zamanda gecerli Portekizce/Almanca
# harflerdir. Yalnizca iki karakterlik tam diziler aranir.
UTF8_MOJIBAKE = [
    "\u00c3\u00bc",  # \u00fc
    "\u00c3\u00b6",  # \u00f6
    "\u00c3\u00a7",  # \u00e7
    "\u00c3\u009c",  # \u00dc
    "\u00c3\u0096",  # \u00d6
    "\u00c3\u0087",  # \u00c7
    "\u00c4\u00b1",  # \u0131
    "\u00c4\u00b0",  # \u0130
    "\u00c4\u009e",  # \u011e
    "\u00c4\u009f",  # \u011f
    "\u00c5\u009e",  # \u015e
    "\u00c5\u009f",  # \u015f
    "\u00ef\u00bf\u00bd",  # U+FFFD'nin mojibake hali
    "\ufffd",          # kayip karakter
]
CP1254_MOJIBAKE = ["Ý", "þ", "ý", "Þ", "ð", "Ð"]

VALID_PATH = re.compile(r"^[A-Za-z0-9._/-]+$")

WORD_RETENTION = 0.90
MIN_SOURCE_WORDS = 50      # bunun altindaki kaynaklarda oran gurultudur
MIN_BODY_WORDS = 20        # kontrol 6: bunun altindaki govde donusum hatasidir
MAX_DETAIL = 20


def _nfc(s):
    return unicodedata.normalize("NFC", s)


def _rel(p, base=None):
    return _nfc(os.path.relpath(p, OUT if base is None else base))


def md_paths(out_dir=None):
    """Build'in urettigi butun .md dosyalari.

    `_Rapor` TAMAMEN atlanir: tasarim dokumani, plan, arac dizini ve
    raporlarin kendisi build ciktisi DEGILDIR. Uzerlerinde icerik
    kontrolu calistirmak yanlis alarm uretir -- ornegin donusum raporu
    onarilan mojibake karakterlerini ("Ý", "þ") ornek olarak yaziyor;
    mojibake kontrolu bunlari gercek hasar sanardi.
    """
    out_dir = OUT if out_dir is None else out_dir
    for dp, dn, fn in os.walk(out_dir, topdown=True):
        dn[:] = [d for d in dn
                 if os.path.realpath(os.path.join(dp, d)) != os.path.realpath(RAPOR)]
        for f in sorted(fn):
            if f.endswith(".md"):
                yield os.path.join(dp, f)


SRC_RE = re.compile(r"Kaynak: `([^`]+)`")


def source_of(text):
    """.md dipnotundaki kaynak yolunu mutlak yola cevirir; yoksa None."""
    m = SRC_RE.search(text)
    if not m:
        return None
    return os.path.join(ROOT, m.group(1))


def strip_field_codes(text):
    """Word alan kodlarini duz metinden siler.

    Bu, kelime sayisi karsilastirmasinin DOGRU olmasi icin sart.
    `textutil -convert txt` HYPERLINK / PAGEREF / INCLUDEPICTURE /
    MERGEFORMAT / EMBED gibi alan kodlarini metnin icine dokuyor;
    html2md bunlari (dogru olarak) siliyor. Temizlenmemis bir temel
    kullanmak, alan koduyla dolu belgelerde %90 esiginin altinda SAHTE
    bir kayip gosterir -- olcumde 8 dosya boyle raporlaniyordu ve
    hicbirinde tek kelime gercek duzyazi eksik degildi. Temeli de
    ciktiyla ayni sekilde temizlemek, karsilastirmayi elma-elma yapar.
    """
    return EMBED_RE.sub("", FIELD_CODE_RE.sub("", text))


def baseline_text(src):
    """Kaynagin duz metni -> (metin, kurtarildi_mi).

    GarbageError: dort buyuk OLE .doc dosyasinda textutil hata VERMEDEN
    okunaksiz ikili dokuyor. O ciktiyla kelime karsilastirmasi anlamsizdir
    (temelin kendisi copluk); build.py bu dosyalarda UTF-16LE kurtarmasi
    yaptigi icin temel de ayni kurtarmadan alinir ve dosya raporda AYRI
    bir baslikta gosterilir.
    """
    if src.lower().endswith(".pdf"):
        return extract_pdf_text(src), False
    try:
        return extract_text(src), False
    except GarbageError:
        return recover_doc_text(src), True


def _exempt_paths(stats):
    """Govdesi tasarim geregi bir-iki cumle olan cikti dosyalari.

    Yonlendirme dosyalari ("asil kopya sudur") ve yalnizca ek dosya iceren
    konular icin yazilan giris sayfalari. build.py bunlarin yollarini
    stats.json'a yaziyor; metne bakip tahmin etmek yerine kaydi okuyoruz.
    """
    return {_nfc(p) for p in
            need(stats, "yonlendirme_yollari") + need(stats, "dizin_yollari")}


# --- 1) Kelime sayisi korunumu ------------------------------------------

def check_word_counts(stats=None):
    stats = load_stats() if stats is None else stats
    exempt = _exempt_paths(stats)
    bad, recovered, missing = [], [], []
    for md in md_paths():
        if _nfc(md) in exempt:
            continue
        text = read_md(md)
        src = source_of(text)
        if src is None:
            continue
        # UC dizin dosya gibi adlandirilmis ('ACCESS VERI TABANI.doc/',
        # 'quickbasickursu.pdf/'), ayrica sadece-ek konularin dipnotu bir
        # KLASORU gosterir. isfile testi sart.
        if not os.path.isfile(src):
            if not os.path.isdir(src):
                missing.append((_rel(md), _rel(src, ROOT)))
            continue
        try:
            plain, was_recovered = baseline_text(src)
        except ExtractError as ex:
            missing.append((_rel(md), "cikarilamadi: %s" % ex))
            continue
        src_w = len(strip_field_codes(plain).split())
        md_w = body_words(text)
        if src_w <= MIN_SOURCE_WORDS:
            continue
        row = (_rel(md), "%d < %d x %.2f" % (md_w, src_w, WORD_RETENTION))
        if md_w < src_w * WORD_RETENTION:
            (recovered if was_recovered else bad).append(row)

    notes = []
    if recovered:
        notes.append(("textutil'in ayristiramadigi, UTF-16LE ile kurtarilan "
                      ".doc dosyalari — temel de kurtarilmis metinden "
                      "alindi", recovered))
    if missing:
        notes.append(("kaynagi okunamayan .md", missing))
    return {"check": "Kelime sayisi korunumu", "ok": not bad and not missing,
            "detail": bad, "notes": notes}


# --- 2) Turkce karakter butunlugu ---------------------------------------

def check_no_mojibake():
    """Ciktida bozuk karakter kalintisi olmamali.

    Bulgular IKI kademeye ayrilir, cunku ikisi farkli seyler soyler:

    * SISTEMIK hasar (>= extract.MOJIBAKE_THRESHOLD isaret): belgenin her
      paragrafi bozuk demektir. Onarim kuralinin devreye girmesi
      gerekirdi; girmediyse bu bir DONUSUM HATASIDIR -> KALDI.
    * IZOLE isaretler (esigin altinda): kaynak metnin icinde tek tuk duran
      bozuk karakterler -- kod ornegindeki "Adýnýzý", tek bir "BELLEÐİNİN"
      gibi. Bunlari onarmak "metin birebir korunur" kuralini cignerdi ve
      tehlikelidir: bir bilgisayar arsivinde bir kod sayfasi tablosu
      "ý", "þ", "ð" karakterlerini VERI olarak yazabilir. Bu yuzden
      onarilmazlar -- ama gizlenmezler de: not olarak tam sayimla
      raporlanirlar.

    Esik extract.py'den okunur; iki modulde ayri sabit tutmak, birinde
    degistirilip otekinde unutuldugunda kontrolu sessizce yanlislastirirdi.
    """
    from extract import MOJIBAKE_THRESHOLD
    bad, isolated = [], []
    for md in md_paths():
        text = read_md(md)
        hits = {b: text.count(b) for b in UTF8_MOJIBAKE + CP1254_MOJIBAKE
                if b in text}
        if not hits:
            continue
        row = (_rel(md), "%d isaret: %s"
               % (sum(hits.values()),
                  ", ".join("%s=%d" % kv for kv in sorted(hits.items()))))
        (bad if sum(hits.values()) > MOJIBAKE_THRESHOLD
         else isolated).append(row)
    notes = []
    if isolated:
        notes.append(("kaynakta izole kalmis bozuk karakterler — birebir "
                      "korundu, onarilmadi (esik: %d)" % MOJIBAKE_THRESHOLD,
                      isolated))
    return {"check": "Turkce karakter butunlugu", "ok": not bad,
            "detail": bad, "notes": notes}


# --- 3) Dosya adi gecerliligi -------------------------------------------

def check_path_charset():
    """Butun cikti yollari [A-Za-z0-9._/-] olmali.

    `_Arsiv` alt cizgiyle basliyor; alt cizgi karakter kumesinde oldugu
    icin bu gecerlidir ve ozel bir muafiyet gerekmez.
    """
    bad = []
    for dp, dn, fn in os.walk(OUT, topdown=True):
        dn[:] = [d for d in dn
                 if os.path.realpath(os.path.join(dp, d)) != os.path.realpath(RAPOR)]
        for name in sorted(dn) + sorted(fn):
            rel = _rel(os.path.join(dp, name))
            if not VALID_PATH.match(rel.replace(os.sep, "/")):
                bad.append(rel)
    return {"check": "Dosya adi gecerliligi", "ok": not bad,
            "detail": bad, "notes": []}


# --- 4) Kayip yok --------------------------------------------------------

def count_sources(root=None):
    """Kaynak arsivde ciktida karsiligi olmasi gereken dosya sayisi.

    build.scan()'in tarama kurallarini BAGIMSIZ olarak tekrar uygular
    (MD/ ve nokta ile baslayan dizinler haric, rolu 'atla' olanlar haric).
    NOT: paket klasoru uyeligi `topic in BUNDLE_FOLDERS` ile SORULMAZ --
    macOS klasor adlarini NFD dondurur, kume literalleri NFC'dir ve bu
    naif test bes paket klasorunun ucunde sessizce basarisiz olup 134
    dosyayi yanlis rolle sayardi.
    """
    root = ROOT if root is None else root
    total = 0
    for topic in sorted(os.listdir(root)):
        tdir = os.path.join(root, topic)
        if topic == "MD" or topic.startswith(".") or not os.path.isdir(tdir):
            continue
        bundle = is_bundle_folder(topic)
        for dp, dn, fn in os.walk(tdir):
            for f in fn:
                rel = os.path.relpath(os.path.join(dp, f), tdir)
                if role(os.path.join(dp, f), rel, bundle=bundle) != "atla":
                    total += 1
    return total


def check_no_loss(stats=None):
    stats = load_stats() if stats is None else stats
    with open(os.path.join(RAPOR, "dups.json"), encoding="utf-8") as fh:
        dups = json.load(fh)
    accounted = (need(stats, "belge") + need(stats, "yonlendirme")
                 + need(stats, "ornek") + need(stats, "gorsel")
                 + need(stats, "arsiv"))
    skipped = sum(len(g) - 1 for g in dups["binary"])
    errors = len(need(stats, "hata"))
    collisions = len(need(stats, "cakisma"))
    src_total = count_sources()
    diff = src_total - (accounted + skipped + errors + collisions)
    return {"check": "Kayip yok", "ok": diff == 0,
            "detail": [] if diff == 0 else [
                "kaynak=%d islenen=%d atlanan_tekrar=%d hata=%d cakisma=%d "
                "fark=%d" % (src_total, accounted, skipped, errors,
                             collisions, diff)],
            "notes": [("sayim", ["kaynak=%d islenen=%d atlanan_tekrar=%d "
                                 "hata=%d cakisma=%d"
                                 % (src_total, accounted, skipped, errors,
                                    collisions)])]}


# --- 5) Link butunlugu ---------------------------------------------------

LINK_RE = re.compile(r"\]\((?!https?://|mailto:|ftp://)([^)]+)\)")
# Dipnottaki ek klasoru referanslari: *Örnekler: `X/ornekler/` (12 dosya)*
ASSET_RE = re.compile(r"^\*(?:Örnekler|Görseller): `([^`]+)` \((\d+) dosya\)\*$",
                      re.M)


def check_links(stats=None):
    """Bagalantilarin hedefi var olmali.

    Spec §12.5 bu kontrolu ACIKCA "INDEX.md ve yonlendirme dosyalarindaki"
    linklerle sinirlar ve bunun iyi bir nedeni var: BIZIM urettigimiz her
    baglanti calismak ZORUNDADIR, ama donusturulen bir belgenin ICINDEKI
    baglantilar 1999'da yazarin yazdigi metindir. "capplet1.htm",
    "java.exe" gibi hedefler arsivde hicbir zaman bulunmuyordu; bunlari
    duzeltmek metni degistirmek olurdu, silmek ise icerik kaybi.

    Bu yuzden iki kademe:
      * URETILEN baglantilar (INDEX.md, _Arsiv/README.md, yonlendirme ve
        giris sayfalari) ve her belgenin dipnotundaki ek klasoru
        referanslari -> kirikse KALDI.
      * Kaynaktan devralinan baglantilar -> not olarak sayilir.
    """
    stats = load_stats() if stats is None else stats
    generated = _exempt_paths(stats) | {
        _nfc(os.path.join(OUT, "INDEX.md")),
        _nfc(os.path.join(OUT, "_Arsiv", "README.md")),
    }
    bad, inherited = [], []
    for md in md_paths():
        base = os.path.dirname(md)
        text = read_md(md)
        is_generated = _nfc(md) in generated
        for target in LINK_RE.findall(text):
            target = target.split("#")[0].strip()
            if not target:
                continue
            if os.path.exists(os.path.join(base, target)):
                continue
            (bad if is_generated else inherited).append((_rel(md), target))
        # Dipnot ek klasoru referanslari HER dosyada bizim uretimimizdir.
        for rel, n in ASSET_RE.findall(text):
            d = os.path.join(base, rel)
            if not os.path.isdir(d):
                bad.append((_rel(md), "ek klasoru yok: %s" % rel))
            elif sum(len(f) for _, _, f in os.walk(d)) != int(n):
                bad.append((_rel(md), "ek klasorundeki dosya sayisi tutmuyor: "
                                      "%s (%s yaziyor)" % (rel, n)))
    notes = []
    if inherited:
        notes.append(("kaynak belgelerin kendi icindeki, arsivde karsiligi "
                      "olmayan baglantilar — birebir korundu", inherited))
    return {"check": "Link butunlugu", "ok": not bad, "detail": bad,
            "notes": notes}


# --- 6) Bos / neredeyse bos cikti yok -----------------------------------

def check_not_empty(stats=None):
    """Hicbir .md govdesi MIN_BODY_WORDS (20) kelimenin altinda olmamali.

    Brief'te olmayan altinci kontrol. Bos bir .md, dosya var oldugu ve
    basligi dogru oldugu icin butun diger kontrollerden GECER: kelime
    korunumu kaynagi okunamayan dosyalari atlar, link ve ad kontrolleri
    icerige bakmaz. Sessiz icerik kaybinin gecebilecegi tek delik budur.

    Yanlis alarm olmasin diye iki grup ayrilir:
      * yonlendirme / giris sayfalari — govdesi tasarim geregi tek cumle,
        stats.json'daki yollardan taninir (muaf).
      * kaynagi zaten cok kisa olan belgeler — build.py kaynak kelime
        sayisini stats['kisa'] altina yaziyor. Kaynak MIN_SOURCE_WORDS'un
        (50) altindaysa orada kaybedilecek bir makale YOKTUR: baglanti
        listesi, tek satirlik bir readme, bir betigin cikti dosyasi.
        MUAF DEGIL, ayri bir baslikta tam sayimla gosterilir.
        (Esik olarak MIN_SOURCE_WORDS kullaniliyor -- kontrol 1'in
        "olculemeyecek kadar kucuk kaynak" siniriyla ayni sabit; ikinci
        bir sihirli sayi uydurmamak icin.)
    """
    stats = load_stats() if stats is None else stats
    exempt = _exempt_paths(stats)
    short_src = {_nfc(p): w for p, w in need(stats, "kisa")}
    bad, genuinely_short = [], []
    for md in md_paths():
        if _nfc(md) in exempt:
            continue
        n = body_words(read_md(md))
        if n >= MIN_BODY_WORDS:
            continue
        src_w = short_src.get(_nfc(md))
        row = (_rel(md), "govde %d kelime%s"
               % (n, "" if src_w is None else ", kaynak %d kelime" % src_w))
        if src_w is not None and src_w < MIN_SOURCE_WORDS:
            genuinely_short.append(row)
        else:
            bad.append(row)
    notes = []
    if genuinely_short:
        notes.append(("kaynagi da bu kadar kisa olan belgeler (donusum "
                      "hatasi degil)", genuinely_short))
    return {"check": "Bos cikti yok", "ok": not bad, "detail": bad,
            "notes": notes}


def verify(root=ROOT):
    stats = load_stats()
    return [check_word_counts(stats), check_no_mojibake(), check_path_charset(),
            check_no_loss(stats), check_links(stats),
            check_not_empty(stats)]


def _print_rows(rows, indent="      "):
    for r in rows[:MAX_DETAIL]:
        print(indent + (r if isinstance(r, str) else " | ".join(map(str, r))))
    if len(rows) > MAX_DETAIL:
        print("%s... ve %d tane daha" % (indent, len(rows) - MAX_DETAIL))


def main():
    failed = 0
    for r in verify():
        print("[%s] %s (%d bulgu)"
              % ("GECTI" if r["ok"] else "KALDI", r["check"], len(r["detail"])))
        if not r["ok"]:
            failed += 1
            _print_rows(r["detail"])
        for label, rows in r["notes"]:
            print("   not: %s (%d)" % (label, len(rows)))
            _print_rows(rows, indent="      ")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
