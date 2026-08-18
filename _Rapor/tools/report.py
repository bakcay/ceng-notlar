#!/usr/bin/env python3
"""MD/ altındaki çıktıdan INDEX ve raporları üretir. build.py'den SONRA çalışır.

Üretilenler:
    MD/INDEX.md                  — kategori/konu dizini
    MD/_Rapor/donusum-raporu.md  — arşive ne olduğunun anlatımı
    MD/_Rapor/tekrarlar.md       — tekrar eden belgeler
    MD/_Arsiv/README.md          — çevrilemeyen formatların açıklaması

Raporlar arşivin sahibine yazılmıştır, programcıya değil: her sayı bir
cümleyle ne anlama geldiği söylenerek verilir.
"""
import json
import os
import re
import sys
import unicodedata

ROOT = "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri"
OUT = os.path.join(ROOT, "MD")
RAPOR = os.path.join(OUT, "_Rapor")
ARSIV_DIRNAME = "_Arsiv"


# --- Ortak yardimcilar ---------------------------------------------------

def _nfc(s):
    """macOS dosya adlarini NFD dondurur; karsilastirma/gosterim NFC olsun."""
    return unicodedata.normalize("NFC", s)


# NOT: asagidaki varsayilanlar None; ROOT/OUT/RAPOR cagri aninda okunur.
# Varsayilan degeri dogrudan `base=ROOT` yazmak sabiti TANIM aninda
# baglar ve modul sabitini degistiren her cagirani (testler, farkli bir
# arsiv koku) sessizce yanlis yola bakar hale getirir.

def _rel(path, base=None):
    return _nfc(os.path.relpath(path, ROOT if base is None else base))


def load_stats(rapor_dir=None):
    d = RAPOR if rapor_dir is None else rapor_dir
    with open(os.path.join(d, "stats.json"), encoding="utf-8") as fh:
        return json.load(fh)


def load_dups(rapor_dir=None):
    d = RAPOR if rapor_dir is None else rapor_dir
    with open(os.path.join(d, "dups.json"), encoding="utf-8") as fh:
        return json.load(fh)


def need(stats, key):
    """stats.json'dan bir anahtari ZORUNLU olarak okur.

    build.py stats.json'a zaman icinde anahtar ekliyor. `stats.get(key)`
    ile okumak, bir anahtar yeniden adlandirildiginda ilgili rapor
    bolumunu SESSIZCE bostan gosterirdi -- rapor "hic mojibake onarimi
    olmadi" der, gercekte alti dosya onarilmistir. Eksik anahtar bir veri
    hatasidir ve gurultuyle durmalidir.
    """
    if key not in stats:
        raise KeyError(
            "stats.json'da '%s' anahtari yok. build.py yeniden calistirilmali "
            "(mevcut anahtarlar: %s)" % (key, ", ".join(sorted(stats))))
    return stats[key]


# --- .md govdesi ---------------------------------------------------------

_FOOT_RE = re.compile(r"^\*.*\*$")


def split_md(text):
    """Bir .md dosyasini (baslik, govde_satirlari) olarak ayirir.

    Govde = H1 basligi ve sondaki kaynak dipnotu HARIC kalan metin.
    Kelime sayimlari bunun uzerinden yapilir; aksi halde her belgeye
    dipnotun 4-10 kelimesi eklenir ve "bos cikti" tespiti (Task 9,
    kontrol 6) tam da yakalamasi gereken dosyalari kacirir.
    """
    lines = text.splitlines()
    title = ""
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        lines = lines[1:]
    # Sondaki dipnot blogu: '---' + yalnizca *...* satirlari (ve bosluklar).
    i = len(lines)
    while i > 0 and (not lines[i - 1].strip() or _FOOT_RE.match(lines[i - 1].strip())):
        i -= 1
    if i > 0 and lines[i - 1].strip() == "---" and i < len(lines):
        lines = lines[:i - 1]
    return title, lines


def body_words(text):
    """.md govdesindeki kelime sayisi (H1 ve dipnot haric)."""
    return len(" ".join(split_md(text)[1]).split())


def read_md(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _md_files(d):
    return sorted(f for f in os.listdir(d)
                  if f.endswith(".md") and f != "README.md"
                  and os.path.isfile(os.path.join(d, f)))


def _title_of(path, text):
    t = split_md(text)[0]
    return t or os.path.basename(path)[:-3]


# --- INDEX ---------------------------------------------------------------

INDEX_INTRO = [
    "1998–2004 arası Türkçe bilgisayar ders notları ve e-kitapları.",
    "Kaynak arşivden Markdown'a çevrilmiştir; metinler birebir korunmuştur —",
    "hiçbir cümle özetlenmemiş, düzeltilmemiş veya güncellenmemiştir.",
]


def write_index(out_dir=None):
    out_dir = OUT if out_dir is None else out_dir
    cats = sorted(d for d in os.listdir(out_dir)
                  if os.path.isdir(os.path.join(out_dir, d))
                  and not d.startswith("_"))
    lines = ["# Bilgisayar Bilgileri Arşivi", ""] + INDEX_INTRO + [""]
    total = 0
    body = []
    for c in cats:
        files = _md_files(os.path.join(out_dir, c))
        if not files:
            continue
        total += len(files)
        body.append("## %s (%d)" % (c.replace("-", " "), len(files)))
        body.append("")
        for f in files:
            p = os.path.join(out_dir, c, f)
            body.append("- [%s](%s/%s) — %d kelime"
                        % (_title_of(p, read_md(p)), c, f, body_words(read_md(p))))
        body.append("")

    adir = os.path.join(out_dir, ARSIV_DIRNAME)
    arsiv_md = _md_files(adir) if os.path.isdir(adir) else []
    if arsiv_md:
        # _Arsiv bir kategori adi olarak da kullaniliyor (arsivin konusu
        # OLMAYAN klasorler, ornegin TIP). Oraya dusen belgeler gercek
        # birer .md'dir; INDEX'in disinda birakilirlarsa cikti agacinda
        # hicbir yerden erisilemez olurlar.
        total += len(arsiv_md)
        body.append("## Arşiv dışı konular (%d)" % len(arsiv_md))
        body.append("")
        body.append("Bilgisayar konusu olmayan klasörlerden çıkan belgeler.")
        body.append("")
        for f in arsiv_md:
            p = os.path.join(adir, f)
            body.append("- [%s](%s/%s) — %d kelime"
                        % (_title_of(p, read_md(p)), ARSIV_DIRNAME, f,
                           body_words(read_md(p))))
        body.append("")

    lines.append("**Toplam %d belge, %d kategori.**" % (total, len(cats)))
    lines.append("")
    lines += body
    if os.path.isdir(adir):
        lines += ["## Çevrilemeyen dosyalar", "",
                  "CHM, RAR, MDB, LIT, SWF gibi Markdown'a çevrilemeyen "
                  "formatlar kopyalanarak saklandı:",
                  "[_Arsiv/](%s/README.md)" % ARSIV_DIRNAME, ""]
    lines += ["## Raporlar", "",
              "- [Dönüşüm raporu](_Rapor/donusum-raporu.md) — "
              "arşive ne olduğunun ayrıntılı anlatımı",
              "- [Tekrar raporu](_Rapor/tekrarlar.md) — "
              "arşivde birden fazla kez bulunan belgeler", ""]
    path = os.path.join(out_dir, "INDEX.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    return path


# --- Donusum raporu ------------------------------------------------------

def _table(rows):
    out = ["| Ölçüt | Adet |", "| --- | --- |"]
    out += ["| %s | %d |" % r for r in rows]
    out.append("")
    return out


def write_conversion_report(out_dir=None, rapor_dir=None):
    out_dir = OUT if out_dir is None else out_dir
    rapor_dir = RAPOR if rapor_dir is None else rapor_dir
    s = load_stats(rapor_dir)
    L = ["# Dönüşüm Raporu", "",
         "Bu rapor, kaynak arşivdeki her dosyaya ne olduğunu anlatır.",
         "**Kaynak arşive hiç dokunulmadı**: hiçbir dosya silinmedi, taşınmadı "
         "veya değiştirilmedi. Aşağıdaki her şey `MD/` klasörünün içinde, "
         "kaynağın kopyası üzerinde yapıldı.", ""]

    L += ["## Özet", ""]
    L += _table([
        ("Markdown'a çevrilen belge", need(s, "belge")),
        ("Tekrar yönlendirme dosyası", need(s, "yonlendirme")),
        ("Sadece ek dosya içeren konu için giriş sayfası", need(s, "dizin")),
        ("Kopyalanan kod örneği", need(s, "ornek")),
        ("Kopyalanan görsel", need(s, "gorsel")),
        ("Çevrilemediği için arşivlenen dosya", need(s, "arsiv")),
        ("Dönüştürülemeyen dosya (hata)", len(need(s, "hata"))),
    ])

    hata = need(s, "hata")
    if hata:
        L += ["## Dönüştürülemeyen dosyalar", "",
              "Bu dosyalar okunamadı. Kaynakta oldukları gibi duruyorlar.", ""]
        L += ["- `%s` — %s" % (_rel(p), e) for p, e in hata]
        L.append("")
    else:
        L += ["## Dönüştürülemeyen dosyalar", "",
              "Yok. Arşivdeki her belge okunabildi.", ""]

    bos = need(s, "bos")
    if bos:
        L += ["## Boş kalan çıktılar", "",
              "Bu belgelerden hiç metin çıkarılamadı ve kurtarma da sonuç "
              "vermedi. Kaynak dosya yerinde duruyor; içeriğine ulaşmak için "
              "orijinal programla açılması gerekir.", ""]
        L += ["- `%s`" % _rel(p) for p in bos]
        L.append("")

    kurtarma = need(s, "kurtarma")
    if kurtarma:
        L += ["## Son çare kurtarma ile okunan belgeler", "",
              "Bu belgeler normal yolla çevrildiğinde **bomboş** çıkıyordu — "
              "metinleri Word'ün gömülü nesnelerinin ya da HTML yorumlarının "
              "içinde saklıydı. Ham dosya taranarak metin kurtarıldı. "
              "İçerik birebir korundu, ancak biçimlendirme (başlık, tablo) "
              "kurtarılamadı.", ""]
        L += ["- `%s` — %d kelime kurtarıldı" % (_rel(p), n)
              for p, n in sorted(kurtarma)]
        L.append("")

    L += _mojibake_section(s)
    L += _utf16_section(s)
    L += _encoding_section(s)

    kisa = need(s, "kisa")
    if kisa:
        L += ["## 300 kelimenin altındaki belgeler (%d)" % len(kisa), "",
              "Bunlar önsöz, içindekiler veya tek sayfalık kalıntı "
              "belgelerdir — kaynakta da bu kadar kısadırlar. Hiçbiri "
              "silinmedi, bilgi amaçlı listeleniyor.", ""]
        L += ["- `%s` — %d kelime" % (_rel(p, out_dir), w)
              for p, w in sorted(kisa, key=lambda x: x[1])]
        L.append("")

    yeni = need(s, "yeniden_adlandirilan")
    if yeni:
        L += ["## Adı değiştirilen ek dosyalar (%d)" % len(yeni), "",
              "Dosya adında Türkçe harf, boşluk veya noktalama olduğu için "
              "çıktıda ASCII bir adla yazıldılar. İçerikleri aynıdır.", ""]
        L += ["- `%s` → `%s`" % (_nfc(o), _nfc(n)) for o, n in sorted(yeni)]
        L.append("")

    cak = need(s, "cakisma")
    if cak:
        L += ["## Ad çakışması yüzünden kopyalanamayan ek dosyalar", "",
              "Aynı hedef ada iki farklı kaynak dosya düştü. Yeniden "
              "adlandırma, ek dosyalar arasındaki bağlantıları kıracağı için "
              "yapılmadı; durum raporlanıyor.", ""]
        L += ["- `%s` (hedef: `%s`)" % (_rel(p), _rel(d, out_dir))
              for p, d in cak]
        L.append("")

    silinen = need(s, "silinen")
    if silinen:
        L += ["## Önceki dönüşümden kalan ve silinen dosyalar (%d)"
              % len(silinen), "",
              "Bunlar `MD/` içinde kalmış eski çıktılardır (örneğin bir dosya "
              "yeniden adlandırıldığında geride kalan eski ad). Kaynak arşivle "
              "ilgileri yoktur.", ""]
        L += ["- `%s`" % p for p in silinen]
        L.append("")

    L += ["## Nasıl doğrulandı", "",
          "`verify.py` her dönüşümden sonra altı kontrol çalıştırır: kelime "
          "sayısı korunumu, Türkçe karakter bütünlüğü, dosya adı geçerliliği, "
          "kayıp dosya olmaması, bağlantı bütünlüğü ve boş çıktı olmaması.", ""]

    path = os.path.join(rapor_dir, "donusum-raporu.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    return path


def _mojibake_section(s):
    rows = need(s, "mojibake_onarilan")
    L = ["## Bozuk Türkçe harflerin onarımı", ""]
    if not rows:
        L += ["Onarım gerektiren dosya çıkmadı.", ""]
        return L
    L += ["Aşağıdaki **%d dosya kaynakta bozuktu**: 2004'te yanlış kod "
          "sayfasıyla kaydedildikleri için Türkçe harfler İzlandaca harflere "
          "dönüşmüştü (`İ`→`Ý`, `ş`→`þ`, `ı`→`ý`, `Ş`→`Þ`, `ğ`→`ð`, "
          "`Ğ`→`Ð`). Çıktıda bu altı harf birebir geri çevrildi; başka hiçbir "
          "karaktere dokunulmadı." % len(rows), "",
          "Sayılar, dosyada kaç harfin düzeltildiğini gösterir. Bu bozulmanın "
          "belge geneline yayılmış gerçek bir hasar mı yoksa tek tük yazım "
          "hatası mı olduğu ölçülerek ayrıldı: bu dosyalarda en az 173, "
          "onarılmayanlarda en fazla 3 işaret vardı.", ""]
    L += ["- `%s` — %d harf onarıldı" % (_rel(p), n)
          for p, n in sorted(rows, key=lambda x: -x[1])]
    L.append("")
    return L


def _utf16_section(s):
    rows = need(s, "utf16_kurtarilan")
    L = ["## Word'ün açamadığı büyük belgeler", ""]
    if not rows:
        L += ["Bu yola başvurulması gereken dosya çıkmadı.", ""]
        return L
    L += ["macOS'un metin dönüştürücüsü (`textutil`) aşağıdaki **%d dosyayı "
          "ayrıştıramadı**: hata vermeden çalıştı ama ürettiği metin okunaksız "
          "ikili döküntüydü. Bunlar içine resim gömülmüş, 10–34 MB'lık gerçek "
          "Word belgeleri. Metin, ham dosyanın içinden (Word'ün kendi UTF-16 "
          "gösteriminden) doğrudan kurtarıldı." % len(rows), "",
          "**Bu dosyalarda biçim kaybı vardır**: yazı düz metne indi, "
          "başlıklar ve tablolar korunamadı. Metnin kendisi birebir aktarıldı. "
          "Orijinal dosyalar kaynak arşivde el değmemiş durumda.", ""]
    L += ["- `%s` — %d kelime kurtarıldı" % (_rel(p), n)
          for p, n in sorted(rows, key=lambda x: -x[1])]
    L.append("")
    return L


def _encoding_section(s):
    rows = need(s, "kodlama_yedegi")
    L = ["## Kodlaması yanlış bildirilen web sayfaları", ""]
    if not rows:
        L += ["Her sayfa kendi bildirdiği kodlamayla okunabildi.", ""]
        return L
    lossy = [r for r in rows if r.get("lossy")]
    L += ["Bir `.htm` dosyası hangi kod sayfasıyla yazıldığını kendi içinde "
          "bildirir. Aşağıdaki **%d sayfada bu bildirim yanlıştı** ya da hiç "
          "yoktu; sayfa, doğru sonucu veren ilk kodlamayla okundu." % len(rows),
          "",
          "Bu liste yalnızca Markdown'a **çevrilen** web sayfalarını kapsar. "
          "E-kitap paketlerinin içindeki çalışan `.htm` örnekleri hiç "
          "çözümlenmedi; onlar bayt bayt kopyalandığı için kodlama sorunundan "
          "etkilenmezler.", ""]
    if lossy:
        L += ["**%d sayfada hiçbir kodlama tam çözmedi**; son çare olarak "
              "windows-1254 ile okundular ve metinde bozuk karakter kalmış "
              "olabilir:" % len(lossy), ""]
        L += ["- `%s`" % _rel(r["path"]) for r in lossy]
        L.append("")
    else:
        L += ["Hiçbirinde karakter kaybı olmadı — hepsi tam çözüldü.", ""]
    L += ["| Dosya | Bildirilen | Kullanılan |", "| --- | --- | --- |"]
    L += ["| `%s` | %s | %s |" % (_rel(r["path"]), r.get("declared") or "—",
                                  r["used"]) for r in rows]
    L.append("")
    return L


# --- Tekrar raporu -------------------------------------------------------

def write_dup_report(out_dir=None, rapor_dir=None):
    rapor_dir = RAPOR if rapor_dir is None else rapor_dir
    d = load_dups(rapor_dir)
    binary, text = d["binary"], d["text"]
    L = ["# Tekrar Raporu", "",
         "Arşivde aynı belge birden fazla yerde duruyor. İki tür tekrar var; "
         "hiçbir kaynak dosya silinmedi, sadece çıktıda tekrar üretilmedi.", "",
         "## Birebir aynı dosyalar (%d grup)" % len(binary), ""]
    if binary:
        L += ["Baytı baytına aynı dosyalar. Her gruptan yalnızca ilki "
              "çevrildi; diğerleri çıktıya hiç girmedi.", ""]
        for g in binary:
            L.append("- **%s**" % _rel(g[0]))
            L += ["  - aynısı, çevrilmedi: `%s`" % _rel(x) for x in g[1:]]
        L.append("")
    else:
        L += ["Yok.", ""]

    L += ["## Aynı metin, farklı dosya (%d grup)" % len(text), ""]
    if text:
        L += ["Dosyaları farklı ama metinleri aynı. Kelime sayısı en fazla "
              "olan asıl kabul edildi; diğerleri için çıktıda asıla işaret "
              "eden kısa bir yönlendirme sayfası yazıldı.", ""]
        for g in text:
            L.append("- **%s**" % _rel(g[0]))
            L += ["  - yönlendirildi: `%s`" % _rel(x) for x in g[1:]]
        L.append("")
    else:
        L += ["Yok.", ""]

    path = os.path.join(rapor_dir, "tekrarlar.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    return path


# --- Arsiv README --------------------------------------------------------

ACIKLAMA = {
    "chm": "Windows derlenmiş HTML yardım dosyası. macOS'ta açmak için bir "
           "CHM okuyucu gerekir.",
    "rar": "RAR arşivi. `unar` veya The Unarchiver ile açılır.",
    "zip": "ZIP arşivi. Finder'da çift tıklayarak açılır.",
    "mdb": "Microsoft Access veritabanı. Access veya LibreOffice Base ile açılır.",
    "lit": "Microsoft Reader e-kitabı. Artık desteklenmeyen bir format.",
    "swf": "Macromedia Flash animasyonu. Flash Player kaldırıldığı için "
           "Ruffle gerekir.",
    "exe": "Windows programı. macOS'ta çalışmaz.",
    "dll": "Windows kitaplık dosyası. Tek başına kullanılmaz.",
    "xml": "Yardımcı XML verisi. Herhangi bir metin düzenleyiciyle açılır.",
}


def write_archive_readme(out_dir=None):
    out_dir = OUT if out_dir is None else out_dir
    adir = os.path.join(out_dir, ARSIV_DIRNAME)
    if not os.path.isdir(adir):
        return None
    L = ["# Arşiv", "",
         "Markdown'a çevrilemeyen dosya biçimleri. Hepsi kaynak arşivden "
         "**kopyalanmıştır**; orijinalleri yerinde duruyor.", ""]

    root_md = _md_files(adir)
    if root_md:
        L += ["## Bu klasördeki belgeler", "",
              "Bilgisayar konusu olmayan klasörlerden çıkan, çevrilebilmiş "
              "belgeler:", ""]
        L += ["- [%s](%s)" % (_title_of(os.path.join(adir, f),
                                        read_md(os.path.join(adir, f))), f)
              for f in root_md]
        L.append("")

    for dp, dn, fn in sorted(os.walk(adir)):
        dn.sort()
        files = sorted(f for f in fn
                       if not f.endswith(".md")
                       and os.path.isfile(os.path.join(dp, f)))
        if not files:
            continue
        rel = os.path.relpath(dp, adir)
        L += ["## %s" % (rel.replace("-", " ") if rel != "." else "Kök"), ""]
        for f in files:
            ext = f.rsplit(".", 1)[-1].lower() if "." in f else ""
            size = os.path.getsize(os.path.join(dp, f)) / 1024
            L.append("- `%s` — %.0f KB. %s" % (f, size, ACIKLAMA.get(ext, "")))
        L.append("")

    path = os.path.join(adir, "README.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    return path


def main():
    for fn in (write_index, write_conversion_report, write_dup_report,
               write_archive_readme):
        p = fn()
        if p:
            print("yazildi:", _rel(p))
    return 0


if __name__ == "__main__":
    sys.exit(main())
