# Arşiv Markdown Dönüşümü — Uygulama Planı

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `~/Downloads/Bilgisayar Bilgileri/` altındaki 691 dosyalık Türkçe bilgisayar arşivini, kaynağa hiç dokunmadan, `MD/` altında kategorilere ayrılmış temiz Markdown koleksiyonuna dönüştürmek.

**Architecture:** Saf macOS yerli araç zinciri üzerine kurulu bir Python 3 boru hattı. Kaynak dosya → `textutil`/`iconv`/`swift+PDFKit` ile UTF-8 HTML veya düz metin → HTML temizleme → Markdown. Kategorilendirme anahtar-kelime kuralları + açık istisna tablosuyla yapılır. Her modül tek sorumluluğa sahiptir ve `unittest` ile bağımsız test edilir. Ana orkestratör (`build.py`) modülleri sırayla çağırır, sonuçları `MD/` altına yazar ve `verify.py` çıktıyı doğrular.

**Tech Stack:** Python 3.9 (macOS sistem Python'u, `/usr/bin/python3`), stdlib `unittest` / `html.parser` / `hashlib` / `subprocess`; `textutil`, `iconv`, `swift` + PDFKit — hepsi macOS ile gelir. **Hiçbir `pip install` yok.**

## Global Constraints

- **Kaynak dokunulmazdır.** `MD/` dışındaki hiçbir dosya/klasör silinmez, taşınmaz, yeniden adlandırılmaz, içeriği değiştirilmez. Tüm kaynak erişimi salt-okunur.
- **Metin birebir korunur.** Özetleme, yeniden yazım, güncelleme, düzeltme yok. Sadece biçim dönüşümü.
- **Kurulum yok.** Yalnızca `/usr/bin/python3` stdlib + macOS yerleşik CLI araçları (`textutil`, `iconv`, `swift`, `file`). `pip`, `brew`, `pandoc` kullanılmaz.
- **Çıktı yolları yalnızca `[A-Za-z0-9._/-]` içerir.** Türkçe karakter, boşluk, noktalama dosya adında olmaz.
- **`.md` içeriği UTF-8 ve tam Türkçedir.** ASCII kısıtı sadece dosya adlarına uygulanır, metne değil.
- **Proje kökü:** `/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri`
- **Araç dizini:** `MD/_Rapor/tools/` (bu dizin kendi içinde git deposudur; arşivin tamamı git deposu değildir)
- **Kategori klasörleri numarasızdır:** `Ag-ve-Iletisim`, `Donanim`, … (spec §6)
- Spec: `MD/_Rapor/00-tasarim.md` — bu plan onun uygulamasıdır.

---

## Dosya Yapısı

```
MD/_Rapor/tools/
  translit.py      Türkçe → ASCII-güvenli dosya adı. Tek sorumluluk: isim üretimi.
  categories.py    Klasör adı → kategori. Kural tablosu + açık istisnalar.
  extract.py       Kaynak dosya → (html|text). textutil/iconv/swift sarmalayıcıları.
  html2md.py       Temizlenmiş HTML → Markdown. Word artıklarını atar, başlık çıkarır.
  classify.py      Dosya → rol (belge | ornek | gorsel | arsiv). Hangi dosya nereye gider.
  dedup.py         md5 + normalize-metin hash'i ile tekrar tespiti.
  build.py         Orkestratör. Tarar, dönüştürür, MD/ altına yazar.
  report.py        INDEX.md, donusum-raporu.md, tekrarlar.md, _Arsiv/README.md üretir.
  verify.py        Spec §12'deki 5 doğrulama kontrolü.
  pdftext.swift    PDFKit ile PDF metin çıkarma (extract.py tarafından çağrılır).
  tests/
    test_translit.py  test_categories.py  test_html2md.py
    test_dedup.py     test_classify.py    test_extract.py
```

Sorumluluk sınırı: `extract.py` **format bilir, içerik bilmez**; `html2md.py` **biçim bilir, dosya sistemi bilmez**; `build.py` **dosya sistemi bilir, biçim bilmez**. Her modül tek başına test edilebilir.

---

### Task 1: Proje iskeleti ve Türkçe → ASCII isim üretimi

**Files:**
- Create: `MD/_Rapor/tools/translit.py`
- Test: `MD/_Rapor/tools/tests/test_translit.py`

**Interfaces:**
- Consumes: —
- Produces:
  - `to_ascii(text: str) -> str` — Türkçe harfleri ASCII karşılığına çevirir, başka değişiklik yapmaz
  - `slugify(text: str) -> str` — konu başlığından dosya adı üretir, yalnızca `[A-Za-z0-9-]`
  - `safe_name(name: str) -> str` — mevcut bir dosya adını **olabildiğince koruyarak** güvenli hale getirir; uzantıyı bozmaz. Kod örnekleri ve arşiv dosyaları için (birbirlerine adla referans verirler)
  - `title_from_folder(text: str) -> str` — H1 başlığı üretir, **Türkçe karakterler korunur**
  - `ACRONYMS: set[str]` — büyük harf kalması gereken kısaltmalar

- [ ] **Step 1: Dizinleri ve git deposunu oluştur**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri"
mkdir -p MD/_Rapor/tools/tests
cd MD/_Rapor/tools
git init
printf '__pycache__/\n*.pyc\n' > .gitignore
```

- [ ] **Step 2: Başarısız testi yaz**

`MD/_Rapor/tools/tests/test_translit.py`:

```python
import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from translit import to_ascii, slugify, safe_name, title_from_folder


class TestToAscii(unittest.TestCase):
    def test_lowercase_turkish(self):
        self.assertEqual(to_ascii("çğıöşü"), "cgiosu")

    def test_uppercase_turkish(self):
        self.assertEqual(to_ascii("ÇĞİÖŞÜ"), "CGIOSU")

    def test_dotless_i_and_dotted_I(self):
        self.assertEqual(to_ascii("İŞLETİM ıslak"), "ISLETIM islak")

    def test_leaves_ascii_untouched(self):
        self.assertEqual(to_ascii("Hello World 123"), "Hello World 123")


class TestSlugify(unittest.TestCase):
    def test_basic_uppercase_folder(self):
        self.assertEqual(slugify("AĞ KURULUMU"), "Ag-Kurulumu")

    def test_acronym_preserved(self):
        self.assertEqual(slugify("DNS - DOMAIN MAIN SYSTEM"), "DNS-Domain-Main-System")

    def test_multiple_acronyms(self):
        self.assertEqual(slugify("ANSI - ASCII - OSI"), "ANSI-ASCII-OSI")

    def test_cpp_becomes_cpp_not_c(self):
        self.assertEqual(slugify("C++ DERS NOTLARI"), "Cpp-Ders-Notlari")

    def test_csharp(self):
        self.assertEqual(slugify("C# NOTLARI"), "CSharp-Notlari")

    def test_a_plus(self):
        self.assertEqual(slugify("A+ KURS NOTLARI"), "A-Plus-Kurs-Notlari")

    def test_plain_c_does_not_collide_with_cpp(self):
        self.assertNotEqual(slugify("C DERS NOTLARI"), slugify("C++ DERS NOTLARI"))

    def test_punctuation_stripped(self):
        self.assertEqual(
            slugify("DNS,DOMAIN NAME SYSTEM ( DOMAIN ISIM SISTEMI)"),
            "DNS-Domain-Name-System-Domain-Isim-Sistemi",
        )

    def test_apostrophe_removed_without_splitting(self):
        self.assertEqual(slugify("XML 'i KAVRAMAK"), "XML-i-Kavramak")

    def test_curly_apostrophe(self):
        self.assertEqual(slugify("Excell’de Matematik"), "Excellde-Matematik")

    def test_output_charset(self):
        import re
        for name in ["AĞ YÜKLEMESİ İÇİN DAHA FAZLA PLANLAMA",
                     "A'  dan  Z ' ye  BİLGİSAYAR TERİMLERİ",
                     "VISUAL BASIC 5.0’IN GETİRDİĞİ YENİLİKLER"]:
            self.assertRegex(slugify(name), r"^[A-Za-z0-9-]+$")

    def test_no_leading_trailing_or_double_dash(self):
        s = slugify("  ---  MOUSE , SCANNER  ---  ")
        self.assertEqual(s, "Mouse-Scanner")


class TestSafeName(unittest.TestCase):
    """safe_name mevcut dosya adlarini KORUR, yeniden uretmez.
    Kod ornekleri birbirine adla referans verdigi icin agresif slug yasak."""

    def test_extension_preserved(self):
        self.assertEqual(safe_name("mesajlar02.php"), "mesajlar02.php")

    def test_already_clean_name_untouched(self):
        self.assertEqual(safe_name("CGI-LIB.PL"), "CGI-LIB.PL")
        self.assertEqual(safe_name("form_analiz.pl"), "form_analiz.pl")

    def test_underscores_kept(self):
        self.assertEqual(safe_name("dosya_yaz01_server.php"), "dosya_yaz01_server.php")

    def test_turkish_chars_converted(self):
        self.assertEqual(safe_name("Html Kitabı.chm"), "Html-Kitabi.chm")

    def test_accented_latin_stripped(self):
        self.assertEqual(safe_name("ekitap-Hakki_Ícal-Kitapcik_CGI_Perl_ekler.rar"),
                         "ekitap-Hakki_Ical-Kitapcik_CGI_Perl_ekler.rar")

    def test_spaces_become_dashes(self):
        self.assertEqual(safe_name("William Shakespeare - King Lear.lit"),
                         "William-Shakespeare-King-Lear.lit")

    def test_undecomposable_symbol_becomes_dash(self):
        self.assertEqual(safe_name("ekitap-Anonim-Photoshop_Aray³z.pdf"),
                         "ekitap-Anonim-Photoshop_Aray-z.pdf")

    def test_no_extension(self):
        self.assertEqual(safe_name("LICENSE"), "LICENSE")

    def test_output_charset(self):
        import re
        for n in ["Html Kitabı.chm", "ekitap-Hakki_Ícal-Kitapcik_Javascript_÷rnekler.rar",
                  "Robert Louis Stevenson - The Strange Case of Dr Jekyll and M.lit"]:
            self.assertRegex(safe_name(n), r"^[A-Za-z0-9._-]+$")


class TestTitleFromFolder(unittest.TestCase):
    def test_keeps_turkish_characters(self):
        self.assertEqual(title_from_folder("AĞ KURULUMU"), "Ağ Kurulumu")

    def test_keeps_acronyms_upper(self):
        self.assertEqual(title_from_folder("DNS - DOMAIN MAIN SYSTEM"),
                         "DNS - Domain Main System")

    def test_collapses_whitespace(self):
        self.assertEqual(title_from_folder("MOUSE ,   SCANNER"), "Mouse, Scanner")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Testi çalıştır, başarısız olduğunu doğrula**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest discover tests -v
```
Expected: FAIL — `ModuleNotFoundError: No module named 'translit'`

- [ ] **Step 4: `translit.py`'i yaz**

```python
"""Türkçe metinden ASCII-güvenli dosya adı ve okunabilir başlık üretir.

Dosya adları yalnızca [A-Za-z0-9-] içerir (spec §5).
Başlıklar Türkçe karakterleri korur — ASCII kısıtı sadece dosya adlarına aittir.
"""
import re
import unicodedata

TR_MAP = str.maketrans({
    "ç": "c", "Ç": "C", "ğ": "g", "Ğ": "G", "ı": "i", "İ": "I",
    "ö": "o", "Ö": "O", "ş": "s", "Ş": "S", "ü": "u", "Ü": "U",
    "â": "a", "Â": "A", "î": "i", "Î": "I", "û": "u", "Û": "U",
})

# Büyük harf kalması gereken kısaltmalar. Arşivin konu başlıklarından çıkarıldı.
ACRONYMS = {
    "3D", "AC", "DC", "ANSI", "API", "ASCII", "ASP", "BIOS", "CGI", "CMOS", "CPU",
    "CSS", "DBASE", "DC", "DNS", "DOS", "DSL", "DVD", "FDISK", "FIR", "FTP", "GL",
    "HTM", "HTML", "HTTP", "IP", "ISA", "ISDN", "ISO", "JET", "LAN", "MDB", "MIDI",
    "MIS", "MS", "MSDOS", "NT", "ODTU", "OSI", "PC", "PHP", "PIC", "PLC", "POST",
    "RAID", "RAM", "ROM", "SQL", "TCP", "TTL", "UNIX", "USB", "VB", "VTYS", "WAN",
    "XML", "II", "III", "IV",
}

# Slug üretiminden ÖNCE uygulanır: bilgi kaybını ve çakışmayı önler.
PRE_SUBS = [
    ("C++", "Cpp"), ("c++", "Cpp"),
    ("C#", "CSharp"), ("c#", "CSharp"),
    ("+", " Plus "),
    ("#", " Sharp "),
    ("&", " ve "),
]

# Kesme işaretleri kelimeyi bölmeden atılır: "XML 'i" -> "XML i", "Excell’de" -> "Excellde"
APOSTROPHES = "'\u2018\u2019\u02bc\u00b4`"


def to_ascii(text):
    """Türkçe harfleri ASCII karşılığına çevirir. Başka hiçbir şeyi değiştirmez."""
    return text.translate(TR_MAP)


def _words(text, ascii_out):
    for old, new in PRE_SUBS:
        text = text.replace(old, new)
    text = "".join("" if ch in APOSTROPHES else ch for ch in text)
    if ascii_out:
        text = to_ascii(text)
        text = re.sub(r"[^A-Za-z0-9]+", " ", text)
    else:
        text = re.sub(r"[^0-9A-Za-z\u00c0-\u024f]+", " ", text)
    return [w for w in text.split() if w]


def _cap(word):
    """Kısaltmaysa büyük bırak, değilse Baş Harfi Büyük yap."""
    if to_ascii(word).upper() in ACRONYMS:
        return to_ascii(word).upper() if word.isupper() or word.isalpha() else word
    if word.isdigit():
        return word
    return word[0].upper() + word[1:].lower()


def slugify(text):
    """'AĞ KURULUMU' -> 'Ag-Kurulumu'. Çıktı yalnızca [A-Za-z0-9-]."""
    parts = [_cap(w) for w in _words(text, ascii_out=True)]
    slug = "-".join(parts)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug


def safe_name(name):
    """Var olan bir dosya adını olabildiğince koruyarak güvenli hale getirir.

    slugify'dan farkı: bu fonksiyon ad ÜRETMEZ, mevcut adı ONARIR. Kod
    örnekleri birbirine dosya adıyla referans verdiği için (include/require,
    <img src>) agresif yeniden adlandırma yasaktır. Yalnızca geçersiz
    karakterler dönüştürülür; alt çizgi, nokta, büyük/küçük harf korunur.

    'Html Kitabı.chm' -> 'Html-Kitabi.chm'
    'mesajlar02.php'  -> 'mesajlar02.php'   (değişmez)
    """
    base, dot, ext = name.rpartition(".")
    if not dot:
        base, ext = name, ""
    base = to_ascii(base)
    # Türkçe olmayan aksanlı Latin harfleri (Í, ó, â…) taban harfe indir.
    base = "".join(c for c in unicodedata.normalize("NFKD", base)
                   if not unicodedata.combining(c))
    base = re.sub(r"[^A-Za-z0-9._-]+", "-", base)
    base = re.sub(r"-{2,}", "-", base).strip("-") or "dosya"
    ext = re.sub(r"[^A-Za-z0-9]+", "", to_ascii(ext))
    return base + ("." + ext if ext else "")


def title_from_folder(text):
    """H1 başlığı üretir. Türkçe karakterler korunur, noktalama sadeleştirilir."""
    src = text
    for old, new in PRE_SUBS[:4]:  # C++/C# yalnızca; '+' ve '&' başlıkta korunur
        src = src.replace(old, new)
    src = re.sub(r"\s*,\s*", ", ", src)
    src = re.sub(r"\s*-\s*", " - ", src)
    src = re.sub(r"\s+", " ", src).strip()
    out = []
    for w in src.split(" "):
        core = re.sub(r"[^0-9A-Za-z\u00c0-\u024f]", "", w)
        if not core:
            out.append(w)
            continue
        capped = _cap(core)
        out.append(w.replace(core, capped, 1))
    return " ".join(out)
```

- [ ] **Step 5: Testi çalıştır, geçtiğini doğrula**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest discover tests -v
```
Expected: PASS — tüm testler yeşil. Kırmızı kalan varsa `_cap` / `_words` düzeltilir, test **değiştirilmez**.

- [ ] **Step 6: Gerçek klasör adlarında dumanı gör**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri" && python3 -c "
import sys; sys.path.insert(0,'MD/_Rapor/tools')
from translit import slugify, title_from_folder
import os
names=sorted(d for d in os.listdir('.') if os.path.isdir(d) and d!='MD')
for n in names[:25]: print(f'{n[:42]:42} -> {slugify(n)}')
print('...toplam', len(names))
"
```
Expected: 25 satır düzgün ASCII slug. Bozuk çıkan olursa Step 2'ye test eklenip Step 4 düzeltilir.

- [ ] **Step 7: Commit**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && git add -A && git commit -m "feat: Turkce -> ASCII dosya adi ve baslik uretimi"
```

---

### Task 2: Kategori eşlemesi

**Files:**
- Create: `MD/_Rapor/tools/categories.py`
- Test: `MD/_Rapor/tools/tests/test_categories.py`

**Interfaces:**
- Consumes: `translit.to_ascii`
- Produces:
  - `CATEGORIES: list[str]` — 13 konu kategorisi, spec §6 sırasıyla
  - `categorize(folder_name: str) -> str` — kategori klasör adı döner, eşleşme yoksa `"Sozluk-ve-Referans"`
  - `OVERRIDES: dict[str, str]` — kural tablosunun yanıldığı klasörler için açık atama

- [ ] **Step 1: Başarısız testi yaz**

`MD/_Rapor/tools/tests/test_categories.py`:

```python
import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from categories import categorize, CATEGORIES, OVERRIDES


class TestCategorize(unittest.TestCase):
    def test_known_assignments(self):
        cases = {
            "ANAKARTLAR": "Donanim",
            "CPU": "Donanim",
            "BELLEK TÜRLERİ": "Donanim",
            "BIOS VE BIOS GÜNCELLEME İŞLEMLERİ": "Donanim",
            "AĞ KURULUMU": "Ag-ve-Iletisim",
            "OSİ REFERANS MODELİ": "Ag-ve-Iletisim",
            "TCP  IP ve FİREWAL": "Guvenlik",
            "DOS KOMUTLARI": "Isletim-Sistemleri",
            "LINUX VE AVANTAJLARI": "Isletim-Sistemleri",
            "C++ DERS NOTLARI": "Programlama",
            "ALGORİTMA": "Programlama",
            "HERKES İÇİN VISUAL BASIC": "Programlama",
            "PHP DERSLERİ": "Web-Gelistirme",
            "XML ' e GİRİŞ": "Web-Gelistirme",
            "FLASH NEDİR": "Web-Gelistirme",
            "MY SQL": "Veritabani",
            "ACCESS KURS NOTLARI": "Veritabani",
            "EXCEL 'e GİRİŞ": "Ofis-Yazilimlari",
            "PHOTOSHOP": "Grafik-ve-Tasarim",
            "AUTOCAD DERSLERİ": "Grafik-ve-Tasarim",
            "VİRÜSLER": "Guvenlik",
            "BİLİŞİM SUÇLARI": "Guvenlik",
            "PLC SİSTEMLERİNİN İNCELENMESİ": "Elektronik",
            "MEKATRONİK NEDİR": "Elektronik",
            "E-TİCARET NEDIR": "Bilisim-ve-E-Ticaret",
            "ISO 9001": "Bilisim-ve-E-Ticaret",
            "YAPAY SİNİR AĞLARI": "Yapay-Zeka",
            "A'  dan  Z ' ye  BİLGİSAYAR TERİMLERİ": "Sozluk-ve-Referans",
            "BİLGİSAYAR İNGİLİZCESİ": "Sozluk-ve-Referans",
        }
        for folder, expected in cases.items():
            self.assertEqual(categorize(folder), expected, msg=folder)

    def test_security_beats_network(self):
        # "TCP IP ve FIREWAL" hem ag hem guvenlik kelimesi tasir; guvenlik kazanmali
        self.assertEqual(categorize("TCP  IP ve FİREWAL"), "Guvenlik")
        self.assertEqual(categorize("LİNUX GÜVENLİK AÇIKLARI"), "Guvenlik")

    def test_database_beats_web(self):
        # "MY SQL" ve "SQL PROGRAMLAMA" veritabani, programlama degil
        self.assertEqual(categorize("SQL PROGRAMLAMA"), "Veritabani")

    def test_every_category_is_a_valid_folder_name(self):
        import re
        for c in CATEGORIES:
            self.assertRegex(c, r"^[A-Za-z0-9-]+$")

    def test_unknown_falls_back(self):
        self.assertEqual(categorize("ZZZ BİLİNMEYEN KONU"), "Sozluk-ve-Referans")

    def test_overrides_win_over_rules(self):
        for folder, cat in OVERRIDES.items():
            self.assertEqual(categorize(folder), cat, msg=folder)


class TestRealArchiveCoverage(unittest.TestCase):
    """Arsivdeki 250 klasorun tamami bir kategoriye dusmeli ve
    'Sozluk-ve-Referans' cop kutusuna donusmemeli."""

    ROOT = "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri"

    def test_fallback_bucket_stays_small(self):
        if not os.path.isdir(self.ROOT):
            self.skipTest("arsiv bulunamadi")
        folders = [d for d in os.listdir(self.ROOT)
                   if os.path.isdir(os.path.join(self.ROOT, d)) and d != "MD"]
        fallback = [f for f in folders if categorize(f) == "Sozluk-ve-Referans"]
        self.assertLessEqual(len(fallback), 15,
                             msg="Fallback'e dusenler: " + ", ".join(sorted(fallback)))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Testi çalıştır, başarısız olduğunu doğrula**

Run: `cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest tests.test_categories -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'categories'`

- [ ] **Step 3: `categories.py`'i yaz**

```python
"""Konu klasörü adından kategori belirler.

Sıra önemlidir: RULES listesinde önce gelen kural kazanır. Güvenlik ve
veritabanı kuralları, ağ/programlama kurallarından ÖNCE gelir çünkü
"TCP IP ve FIREWAL" veya "SQL PROGRAMLAMA" gibi başlıklar iki kategoriye
birden anahtar kelime taşır (spec §6, sınırda kalan konular).
"""
from translit import to_ascii

CATEGORIES = [
    "Ag-ve-Iletisim",
    "Bilisim-ve-E-Ticaret",
    "Donanim",
    "Elektronik",
    "Grafik-ve-Tasarim",
    "Guvenlik",
    "Isletim-Sistemleri",
    "Ofis-Yazilimlari",
    "Programlama",
    "Sozluk-ve-Referans",
    "Veritabani",
    "Web-Gelistirme",
    "Yapay-Zeka",
]

FALLBACK = "Sozluk-ve-Referans"

# (kategori, anahtar kelimeler) — normalize edilmis (ASCII, buyuk harf) ada karsi aranir.
RULES = [
    ("Guvenlik", [
        "VIRUS", "GUVENLIK", "GUVENLIGI", "HACKER", "SUCLARI", "FIREWAL",
        "SPAM", "BUFFER OVERFLOW", "SIFRE", "KRIPTO", "YEDEKLEME",
    ]),
    ("Yapay-Zeka", ["YAPAY ZEKA", "YAPAY SINIR", "UZMAN SISTEM", "PROLOG"]),
    ("Veritabani", [
        "VERI TABANI", "VERITABANI", "SQL", "ACCESS", "ORACLE", "DBASE",
        "VTYS", "INFORMIX", "MDB",
    ]),
    ("Elektronik", [
        "AC-DC", "CONVENTER", "FILTRE", "FIR ", "PIC ", "PLC", "MEKATRONIK",
        "MIKROKONTROLOR", "SAYISAL ELEKTRONIK", "OTOMASYON", "KAYAN YAZI",
        "TWO PORT", "POISSON", "DEVRESI", "CMOS", "TTL",
    ]),
    ("Grafik-ve-Tasarim", [
        "3D", "AUTOCAD", "PHOTOSHOP", "COREL", "ICON AUTHOR", "MIDI",
        "PHOTOPAINT", "STUDIO MAX",
    ]),
    ("Ofis-Yazilimlari", [
        "EXCEL", "EXCELL", "WORD", "MICROSOFT PROJECT", "OFIS PROGRAM",
        "ARAC CUBUK", "UYGULAMA YAZILIM",
    ]),
    ("Web-Gelistirme", [
        "HTML", "HTM ", "CSS", "ASP", "PHP", "PERL", "CGI", "JAVA SCRIPT",
        "JAVASCRIPT", "XML", "FRONTPAGE", "FRONT PAGE", "FLASH", "WEB",
        "INTERNET SITESI", "OPEN GL", "ICERIK KODLARI", "SUNUCUSU",
    ]),
    ("Isletim-Sistemleri", [
        "DOS", "WINDOW", "LINUX", "UNIX", "MINIX", "ISLETIM SISTEM",
        "DENETIM MASASI", "KULLANICI PROFIL", "DISK VE DOSYA KOMUT",
        "APPEND", "FDISK",
    ]),
    ("Ag-ve-Iletisim", [
        "AG ", " AG", "NETWORK", "OSI", "TCP", "IP ADRES", "DNS", "DOMAIN",
        "ETHERNET", "LAN", "WAN", "ISDN", "DSL", "ROUTER", "KABLOSUZ",
        "MODEM", "ANSI", "ASCII", "INTERNET", "INTRANET", "EXTRANET",
        "CEVIRMELI", "ILETISIM",
    ]),
    ("Donanim", [
        "ANAKART", "CPU", "ISLEMCI", "BELLEK", "SES KART", "CEVRE BIRIM",
        "BIOS", "RAID", "VERSATILE DISC", "DONANIM", "ISA", "PC SORUN",
        "A PLUS KURS", "MOUSE", "SCANNER", "MIKROISLEMCI",
    ]),
    ("Programlama", [
        "ALGORITMA", "PASCAL", "DELPHI", "VISUAL BASIC", "VISUAL BASIC",
        "ASSEMBLER", "PROGRAMLAMA", "PROGRAM", "VERI YAPILARI", "JAVA",
        "CPP", "C DERS", "C NOTLARI", "CSHARP", "C KODLAMA", "BASIC",
        "DIZI", "LIST BOX", "TOOLBOX", "DONGU", "YAZILIM", "FONKSIYON",
        "KODLAMA", "QUICKBASIC", "MOBIL UYGULAMA",
    ]),
    ("Bilisim-ve-E-Ticaret", [
        "TICARET", "BILISIM DUNYA", "TEKNOKENT", "INTERTECH", "ISO 9001",
        "BILL GATES", "MIS", "INFORMATION", "EGITIM",
    ]),
]

# Kural tablosunun yanildigi klasorler. Klasor adi birebir yazilir.
OVERRIDES = {
    "TCP  IP ve FİREWAL": "Guvenlik",
    "SQL PROGRAMLAMA": "Veritabani",
    "PROLOG İLE UZMAN SİSTEM HAZIRLAMA": "Yapay-Zeka",
    "OPEN GL": "Programlama",
    "MOBİL UYGULAMALARI": "Programlama",
    "ANSI - ASCII - OSI": "Ag-ve-Iletisim",
    "CMOS NEDİR  -  TTL NEDİR": "Elektronik",
    "FDISK NEDIR": "Isletim-Sistemleri",
    "A+ KURS NOTLARI": "Donanim",
    "KİM KORKAR BİLGİSAYARDAN": "Sozluk-ve-Referans",
    "KİM KORKAR UNİX TEN": "Isletim-Sistemleri",
    "BİLGİSAYAR İNGİLİZCESİ": "Sozluk-ve-Referans",
    "GENERAL INFORMATİON ABOUT INFORMATION and MIS": "Bilisim-ve-E-Ticaret",
    "WEB - TABANLI ÖĞRETİM": "Bilisim-ve-E-Ticaret",
    "UZAKTAN EĞİTİM TERİMLER SÖZLÜĞÜ": "Sozluk-ve-Referans",
    "ELEKTRONİK TİCARET TERİMLER SÖZLÜĞÜ": "Bilisim-ve-E-Ticaret",
    "3D MİNİ SÖZLÜK": "Sozluk-ve-Referans",
    "YEDEKLEME NEDİR": "Guvenlik",
    "PROBLEM COZME VE ALGORITMA": "Programlama",
    "TIP": "_Arsiv",
}


def _norm(name):
    return " " + to_ascii(name).upper().replace("+", " PLUS ") + " "


def categorize(folder_name):
    if folder_name in OVERRIDES:
        return OVERRIDES[folder_name]
    hay = _norm(folder_name)
    for category, keywords in RULES:
        for kw in keywords:
            if kw in hay:
                return category
    return FALLBACK
```

- [ ] **Step 4: Testi çalıştır**

Run: `cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest tests.test_categories -v`
Expected: PASS. `test_fallback_bucket_stays_small` kırmızıysa, hata mesajındaki klasör adları `OVERRIDES`'a veya `RULES`'a eklenir.

- [ ] **Step 5: 250 klasörün tam dağılımını insan gözüyle gözden geçir**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri" && python3 -c "
import sys, os, collections; sys.path.insert(0,'MD/_Rapor/tools')
from categories import categorize
folders=sorted(d for d in os.listdir('.') if os.path.isdir(d) and d!='MD')
g=collections.defaultdict(list)
for f in folders: g[categorize(f)].append(f)
for cat in sorted(g):
    print(f'\n### {cat}  ({len(g[cat])})')
    for f in g[cat]: print('   ', f)
print('\nTOPLAM', len(folders))
" | tee MD/_Rapor/kategori-dagilimi.txt
```
Expected: 250 klasör 14 gruba dağılmış. **Bu çıktı kullanıcıya gösterilir ve onaylanır.** Yanlış yerleşenler `OVERRIDES`'a eklenip Step 4–5 tekrarlanır.

- [ ] **Step 6: Commit**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && git add -A && git commit -m "feat: klasor -> kategori eslemesi"
```

---

### Task 3: Metin çıkarma katmanı

**Files:**
- Create: `MD/_Rapor/tools/extract.py`, `MD/_Rapor/tools/pdftext.swift`
- Test: `MD/_Rapor/tools/tests/test_extract.py`

**Interfaces:**
- Consumes: —
- Produces:
  - `extract_html(path: str) -> str` — `.doc/.rtf/.txt` → UTF-8 HTML (textutil)
  - `read_htm(path: str) -> str` — `.htm/.html` → UTF-8 HTML (kodlama tespiti + iconv)
  - `extract_pdf_text(path: str) -> str` — `.pdf` → düz metin (swift + PDFKit)
  - `doc_metadata(html: str) -> dict` — `{"author": str|None, "year": str|None, "title": str|None}`
  - `ExtractError(Exception)` — çıkarma başarısız olduğunda

- [ ] **Step 1: Başarısız testi yaz**

`MD/_Rapor/tools/tests/test_extract.py`:

```python
import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from extract import extract_html, read_htm, extract_pdf_text, doc_metadata, ExtractError

ROOT = "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri"


def p(rel):
    return os.path.join(ROOT, rel)


class TestExtractHtml(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(ROOT):
            self.skipTest("arsiv bulunamadi")

    def test_doc_produces_html_with_turkish(self):
        html = extract_html(p("CPU/CPU.doc"))
        self.assertIn("<html", html.lower())
        self.assertIn("İşlemci", html)

    def test_doc_has_no_mojibake(self):
        html = extract_html(p("MY SQL/MY SQL.doc"))
        for bad in ["Ã¼", "Ä±", "ï¿½", "\u00b3lemesi"]:
            self.assertNotIn(bad, html)

    def test_missing_file_raises(self):
        with self.assertRaises(ExtractError):
            extract_html(p("YOK/YOK.doc"))


class TestReadHtm(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(ROOT):
            self.skipTest("arsiv bulunamadi")

    def test_windows1254_htm_decoded(self):
        html = read_htm(p("OPEN GL/openGL_TR.htm"))
        self.assertNotIn("\ufffd", html)
        self.assertIn("<html", html.lower())


class TestPdf(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(ROOT):
            self.skipTest("arsiv bulunamadi")

    def test_pdf_text_extracted(self):
        txt = extract_pdf_text(p("A+ KURS NOTLARI/a+_pdf.pdf"))
        self.assertGreater(len(txt.split()), 3000)
        self.assertIn("Bilgisayar", txt)


class TestMetadata(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(ROOT):
            self.skipTest("arsiv bulunamadi")

    def test_author_and_year(self):
        html = extract_html(p("PC SORUNLARINA KOLAY ÇÖZÜMLER/PC SORUNLARINA KOLAY ÇÖZÜMLER.doc"))
        md = doc_metadata(html)
        self.assertEqual(md["author"], "Fatih Yılmaz")
        self.assertEqual(md["year"], "2004")

    def test_missing_metadata_is_none_not_crash(self):
        md = doc_metadata("<html><head></head><body>x</body></html>")
        self.assertIsNone(md["author"])
        self.assertIsNone(md["year"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Testi çalıştır, başarısız olduğunu doğrula**

Run: `cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest tests.test_extract -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'extract'`

- [ ] **Step 3: `pdftext.swift`'i yaz**

```swift
import Foundation
import PDFKit

let args = CommandLine.arguments
guard args.count > 1, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("PDF acilamadi\n".data(using: .utf8)!)
    exit(1)
}
var out = ""
for i in 0..<doc.pageCount {
    if let page = doc.page(at: i), let s = page.string { out += s + "\n" }
}
FileHandle.standardOutput.write(out.data(using: .utf8)!)
```

- [ ] **Step 4: `extract.py`'i yaz**

```python
"""Kaynak dosyadan UTF-8 HTML veya düz metin çıkarır.

Bu modül format bilir, içerik bilmez. Tüm kaynak erişimi salt-okunurdur.
Zincir: .doc/.rtf/.txt -> textutil | .htm -> iconv | .pdf -> swift+PDFKit
"""
import os
import re
import subprocess

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_SWIFT = os.path.join(TOOLS_DIR, "pdftext.swift")

# Denenecek kodlamalar, sırayla. Arşivdeki .htm'ler ağırlıkla Windows-1254.
HTM_ENCODINGS = ["utf-8", "windows-1254", "iso-8859-9", "cp1252", "latin-1"]


class ExtractError(Exception):
    pass


def _run(cmd, timeout=120):
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise ExtractError("zaman asimi: %s" % cmd[0])
    if r.returncode != 0:
        raise ExtractError("%s basarisiz (%d): %s"
                           % (cmd[0], r.returncode, r.stderr.decode("utf8", "replace")[:200]))
    return r.stdout.decode("utf-8", "replace")


def extract_html(path):
    """.doc / .rtf / .txt -> UTF-8 HTML."""
    if not os.path.isfile(path):
        raise ExtractError("dosya yok: %s" % path)
    return _run(["textutil", "-convert", "html", "-encoding", "UTF-8", "-stdout", path])


def extract_text(path):
    """.doc / .rtf / .txt -> düz metin. Kelime sayısı doğrulaması için."""
    if not os.path.isfile(path):
        raise ExtractError("dosya yok: %s" % path)
    return _run(["textutil", "-convert", "txt", "-encoding", "UTF-8", "-stdout", path])


def read_htm(path):
    """.htm / .html -> UTF-8 HTML. Kodlamayı meta etiketinden veya deneyerek bulur."""
    if not os.path.isfile(path):
        raise ExtractError("dosya yok: %s" % path)
    raw = open(path, "rb").read()
    m = re.search(rb'charset\s*=\s*["\']?\s*([A-Za-z0-9_-]+)', raw[:4000], re.I)
    order = list(HTM_ENCODINGS)
    if m:
        declared = m.group(1).decode("ascii", "ignore").lower()
        if declared in order:
            order.remove(declared)
        order.insert(0, declared)
    for enc in order:
        try:
            return raw.decode(enc)
        except (UnicodeDecodeError, LookupError):
            continue
    return raw.decode("windows-1254", "replace")


def extract_pdf_text(path):
    """.pdf -> düz metin (PDFKit)."""
    if not os.path.isfile(path):
        raise ExtractError("dosya yok: %s" % path)
    return _run(["swift", PDF_SWIFT, path], timeout=300)


_META_RE = {
    "author": re.compile(r'<meta\s+name="Author"\s+content="([^"]*)"', re.I),
    "title": re.compile(r"<title>(.*?)</title>", re.I | re.S),
    "created": re.compile(r'<meta\s+name="CreationTime"\s+content="(\d{4})', re.I),
}


def doc_metadata(html):
    """textutil HTML başlığından yazar / yıl / doküman başlığı okur.

    Yazar adındaki alt çizgiler boşluğa çevrilir ('Fatih_Yılmaz' -> 'Fatih Yılmaz').
    Doküman başlığı Word şablonundan devralınmış olabilir; başlık olarak
    GÜVENİLMEZ (spec §3/P3), yalnızca bilgi amaçlı döner.
    """
    out = {"author": None, "title": None, "year": None}
    m = _META_RE["author"].search(html)
    if m and m.group(1).strip():
        out["author"] = m.group(1).replace("_", " ").strip()
    m = _META_RE["title"].search(html)
    if m and m.group(1).strip():
        out["title"] = re.sub(r"\s+", " ", m.group(1)).strip()
    m = _META_RE["created"].search(html)
    if m:
        out["year"] = m.group(1)
    return out
```

- [ ] **Step 5: Testi çalıştır**

Run: `cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest tests.test_extract -v`
Expected: PASS (6 test). Swift ilk çağrıda derleme yaptığı için PDF testi ~10 sn sürebilir.

- [ ] **Step 6: Tüm kaynak dosyalarda çıkarma dumanı**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri" && python3 -c "
import sys,os; sys.path.insert(0,'MD/_Rapor/tools')
from extract import extract_html, read_htm, ExtractError
ok=fail=0; errs=[]
for dp,dn,fn in os.walk('.'):
    if dp.startswith('./MD'): continue
    for f in fn:
        pth=os.path.join(dp,f); ext=f.lower().rsplit('.',1)[-1]
        try:
            if ext in ('doc','rtf','txt'): extract_html(pth); ok+=1
            elif ext in ('htm','html'): read_htm(pth); ok+=1
        except ExtractError as e: fail+=1; errs.append((pth,str(e)[:60]))
print('OK',ok,'FAIL',fail)
for e in errs[:20]: print(' ',e)
"
```
Expected: `FAIL 0`. Hata çıkarsa `extract.py`'de ilgili dal düzeltilir.

- [ ] **Step 7: Commit**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && git add -A && git commit -m "feat: doc/htm/pdf metin cikarma katmani"
```

---

### Task 4: HTML → Markdown dönüştürücü

**Files:**
- Create: `MD/_Rapor/tools/html2md.py`
- Test: `MD/_Rapor/tools/tests/test_html2md.py`

**Interfaces:**
- Consumes: —
- Produces:
  - `html_to_markdown(html: str) -> str` — temiz Markdown gövdesi (H1 ve dipnot hariç)
  - `text_to_markdown(text: str) -> str` — PDF/düz metin için; paragrafları toparlar

- [ ] **Step 1: Başarısız testi yaz**

`MD/_Rapor/tools/tests/test_html2md.py`:

```python
import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from html2md import html_to_markdown, text_to_markdown


class TestHtmlToMarkdown(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(html_to_markdown("<html><body><p>Merhaba dünya.</p></body></html>"),
                         "Merhaba dünya.")

    def test_style_and_script_dropped(self):
        html = "<html><head><style>p{color:red}</style></head><body><script>x=1</script><p>Metin</p></body></html>"
        out = html_to_markdown(html)
        self.assertNotIn("color:red", out)
        self.assertNotIn("x=1", out)
        self.assertEqual(out, "Metin")

    def test_word_namespace_tags_dropped(self):
        html = "<html><body><p><o:p></o:p>Gövde</p></body></html>"
        self.assertEqual(html_to_markdown(html), "Gövde")

    def test_bold_and_italic(self):
        self.assertEqual(html_to_markdown("<p><b>kalın</b> ve <i>eğik</i></p>"),
                         "**kalın** ve *eğik*")

    def test_heading_tags(self):
        self.assertEqual(html_to_markdown("<h1>Ana</h1><h2>Alt</h2>"), "# Ana\n\n## Alt")

    def test_large_font_paragraph_becomes_heading(self):
        html = ('<html><head><style>p.p1 {font: 16.0px Arial}'
                'p.p2 {font: 12.0px Times}</style><body>'
                '<p class="p1">SABİT DİSKLER</p><p class="p2">Gövde metni burada.</p>'
                '</body></html>')
        out = html_to_markdown(html)
        self.assertIn("## SABİT DİSKLER", out)
        self.assertIn("Gövde metni burada.", out)

    def test_unordered_list(self):
        self.assertEqual(html_to_markdown("<ul><li>bir</li><li>iki</li></ul>"),
                         "- bir\n- iki")

    def test_ordered_list(self):
        self.assertEqual(html_to_markdown("<ol><li>bir</li><li>iki</li></ol>"),
                         "1. bir\n2. iki")

    def test_table(self):
        html = "<table><tr><td>A</td><td>B</td></tr><tr><td>1</td><td>2</td></tr></table>"
        out = html_to_markdown(html)
        self.assertIn("| A | B |", out)
        self.assertIn("| --- | --- |", out)
        self.assertIn("| 1 | 2 |", out)

    def test_link(self):
        self.assertEqual(html_to_markdown('<p><a href="http://x.com">X</a></p>'),
                         "[X](http://x.com)")

    def test_word_field_codes_removed(self):
        html = '<p>INCLUDEPICTURE "http://a/b.jpg" \\* MERGEFORMATINET </p><p>Gerçek metin</p>'
        out = html_to_markdown(html)
        self.assertNotIn("INCLUDEPICTURE", out)
        self.assertNotIn("MERGEFORMATINET", out)
        self.assertIn("Gerçek metin", out)

    def test_entities_decoded(self):
        self.assertEqual(html_to_markdown("<p>a &amp; b &gt; c &nbsp;d</p>"), "a & b > c d")

    def test_blank_paragraphs_collapsed(self):
        html = "<p>A</p><p></p><p>&nbsp;</p><p></p><p>B</p>"
        self.assertEqual(html_to_markdown(html), "A\n\nB")

    def test_markdown_special_chars_escaped_in_text(self):
        self.assertEqual(html_to_markdown("<p>C:\\dizin *yıldız* _alt_</p>"),
                         r"C:\\dizin \*yıldız\* \_alt\_")

    def test_no_crlf_in_output(self):
        self.assertNotIn("\r", html_to_markdown("<p>bir</p>\r\n<p>iki</p>"))


class TestTextToMarkdown(unittest.TestCase):
    def test_paragraphs_separated_by_blank_line(self):
        self.assertEqual(text_to_markdown("Birinci satır.\n\nİkinci satır."),
                         "Birinci satır.\n\nİkinci satır.")

    def test_bullet_lines_become_list(self):
        self.assertEqual(text_to_markdown("• Bir\n• İki"), "- Bir\n- İki")

    def test_collapses_three_or_more_blank_lines(self):
        self.assertEqual(text_to_markdown("A\n\n\n\n\nB"), "A\n\nB")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Testi çalıştır, başarısız olduğunu doğrula**

Run: `cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest tests.test_html2md -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'html2md'`

- [ ] **Step 3: `html2md.py`'i yaz**

```python
"""HTML -> Markdown. Word/textutil artıklarını temizler.

Bu modül biçim bilir, dosya sistemi bilmez. Girdi bir HTML dizesi,
çıktı bir Markdown dizesidir.

Başlık tespiti iki yoldan olur:
  1) Gerçek <h1>-<h6> etiketleri
  2) textutil'in ürettiği CSS sınıflarındaki font boyutu: gövde metninin
     medyan font boyutundan belirgin büyük ve kısa olan paragraflar başlık sayılır.
"""
import html as html_mod
import re
from html.parser import HTMLParser

DROP_TAGS = {"style", "script", "head", "title", "meta", "link", "xml"}
FIELD_CODE_RE = re.compile(
    r"(INCLUDEPICTURE|MERGEFORMATINET|HYPERLINK\s+\"|PAGEREF|TOC\s+\\o|SEQ\s+)[^\n]*"
)
HEADING_MIN_RATIO = 1.15   # gövde fontunun bu katından büyükse başlık adayı
HEADING_MAX_WORDS = 14     # başlık adayı en fazla bu kadar kelime olabilir


def _font_sizes(css):
    """CSS'ten {sinif_adi: punto} tablosu çıkarır."""
    out = {}
    for m in re.finditer(r"p\.(\w+)\s*\{([^}]*)\}", css):
        cls, body = m.group(1), m.group(2)
        fm = re.search(r"font:\s*([\d.]+)px", body)
        if fm:
            out[cls] = float(fm.group(1))
    return out


def _median(vals):
    if not vals:
        return 0.0
    s = sorted(vals)
    return s[len(s) // 2]


def _escape(text):
    return re.sub(r"([\\*_`\[\]])", r"\\\1", text)


class _Collector(HTMLParser):
    """HTML'i blok listesine indirger: ('p'|'h2'|'li'|'oli'|'tr', metin)."""

    def __init__(self, sizes):
        super().__init__(convert_charrefs=True)
        self.sizes = sizes
        self.blocks = []
        self.buf = []
        self.skip = 0
        self.kind = "p"
        self.cur_size = None
        self.in_table = False
        self.row = []
        self.href = None

    # -- yardimcilar --
    def _flush(self):
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf = []
        if not text:
            self.kind = "p"
            self.cur_size = None
            return
        text = FIELD_CODE_RE.sub("", text).strip()
        if not text:
            self.kind = "p"
            self.cur_size = None
            return
        self.blocks.append((self.kind, text, self.cur_size))
        self.kind = "p"
        self.cur_size = None

    # -- HTMLParser arayuzu --
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in DROP_TAGS or ":" in tag:
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "br":
            self.buf.append(" ")
        elif tag in ("p", "div"):
            self._flush()
            cls = a.get("class", "")
            self.cur_size = self.sizes.get(cls)
        elif re.fullmatch(r"h[1-6]", tag):
            self._flush()
            self.kind = "h" + tag[1]
        elif tag == "li":
            self._flush()
            self.kind = "oli" if self._in_ol else "li"
        elif tag == "ol":
            self._in_ol = True
        elif tag == "ul":
            self._in_ol = False
        elif tag == "table":
            self.in_table = True
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self._flush()
            self.buf = []
        elif tag in ("b", "strong"):
            self.buf.append("**")
        elif tag in ("i", "em"):
            self.buf.append("*")
        elif tag == "a" and a.get("href"):
            self.href = a["href"]
            self.buf.append("[")

    def handle_endtag(self, tag):
        if tag in DROP_TAGS or ":" in tag:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in ("b", "strong"):
            self.buf.append("**")
        elif tag in ("i", "em"):
            self.buf.append("*")
        elif tag == "a" and self.href:
            self.buf.append("](%s)" % self.href)
            self.href = None
        elif tag in ("td", "th"):
            cell = re.sub(r"\s+", " ", "".join(self.buf)).strip()
            self.row.append(cell)
            self.buf = []
        elif tag == "tr":
            if any(self.row):
                self.blocks.append(("tr", self.row, None))
            self.row = []
        elif tag == "table":
            self.in_table = False
            self.blocks.append(("tend", "", None))
        elif tag in ("p", "div", "li") or re.fullmatch(r"h[1-6]", tag):
            self._flush()
        elif tag == "ol":
            self._in_ol = False

    def handle_data(self, data):
        if self.skip:
            return
        self.buf.append(_escape(data) if not self.in_table else data)

    _in_ol = False


def html_to_markdown(source):
    css = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", source, re.S | re.I))
    sizes = _font_sizes(css)

    c = _Collector(sizes)
    c.feed(source)
    c._flush()

    body_sizes = [s for k, t, s in c.blocks if k == "p" and s and len(str(t).split()) > 20]
    base = _median(body_sizes) or _median([s for _, _, s in c.blocks if s]) or 12.0

    out = []
    ol_n = 0
    table_rows = []
    for kind, text, size in c.blocks:
        if kind == "tr":
            table_rows.append(text)
            continue
        if kind == "tend":
            if table_rows:
                width = max(len(r) for r in table_rows)
                for i, r in enumerate(table_rows):
                    r = list(r) + [""] * (width - len(r))
                    out.append("| " + " | ".join(x.replace("|", "\\|") for x in r) + " |")
                    if i == 0:
                        out.append("| " + " | ".join(["---"] * width) + " |")
                table_rows = []
            continue

        if kind != "oli":
            ol_n = 0

        if kind.startswith("h") and len(kind) == 2 and kind[1].isdigit():
            level = min(int(kind[1]) + 1, 6)   # kaynak h1 -> ## (dosyanın h1'i başlıktır)
            out.append("#" * level + " " + text)
        elif kind == "li":
            out.append("- " + text)
        elif kind == "oli":
            ol_n += 1
            out.append("%d. " % ol_n + text)
        else:
            is_heading = (
                size is not None
                and size >= base * HEADING_MIN_RATIO
                and len(text.split()) <= HEADING_MAX_WORDS
                and not text.endswith((".", ":", ";", ","))
            )
            out.append(("## " + text) if is_heading else text)

    md = "\n\n".join(x for x in out if x.strip())
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = md.replace("\r", "")
    md = re.sub(r"[ \t]+\n", "\n", md)
    return md.strip()


BULLET_RE = re.compile(r"^\s*[•·▪◦\-\*]\s+")


def text_to_markdown(text):
    """PDF / düz metin -> Markdown. Madde işaretlerini listeye çevirir."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = html_mod.unescape(text)
    lines = [ln.rstrip() for ln in text.split("\n")]
    out = []
    for ln in lines:
        if BULLET_RE.match(ln):
            out.append("- " + BULLET_RE.sub("", ln).strip())
        else:
            out.append(ln.strip())
    md = "\n".join(out)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()
```

- [ ] **Step 4: Testi çalıştır**

Run: `cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest tests.test_html2md -v`
Expected: PASS (17 test).

- [ ] **Step 5: Gerçek belgede göz kontrolü**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri" && python3 -c "
import sys; sys.path.insert(0,'MD/_Rapor/tools')
from extract import extract_html
from html2md import html_to_markdown
md = html_to_markdown(extract_html('PC SORUNLARINA KOLAY ÇÖZÜMLER/PC SORUNLARINA KOLAY ÇÖZÜMLER.doc'))
print(md[:1800])
print('\n--- KELIME:', len(md.split()))
"
```
Expected: Başlıkların `##` ile işaretlendiği, Türkçe karakterleri sağlam, okunabilir Markdown.

- [ ] **Step 6: Commit**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && git add -A && git commit -m "feat: HTML -> Markdown donusturucu"
```

---

### Task 5: Tekrar tespiti

**Files:**
- Create: `MD/_Rapor/tools/dedup.py`
- Test: `MD/_Rapor/tools/tests/test_dedup.py`

**Interfaces:**
- Consumes: `extract.extract_text`, `extract.ExtractError`
- Produces:
  - `file_hash(path: str) -> str` — dosyanın SHA-256'sı
  - `text_hash(text: str) -> str` — boşluksuz, küçük harfe indirilmiş metnin SHA-256'sı
  - `find_duplicates(entries: list[dict]) -> dict` — `{"binary": [...], "text": [...]}`, her grup kelime sayısına göre sıralı (asıl = ilk)

- [ ] **Step 1: Başarısız testi yaz**

`MD/_Rapor/tools/tests/test_dedup.py`:

```python
import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from dedup import file_hash, text_hash, find_duplicates


class TestTextHash(unittest.TestCase):
    def test_whitespace_insensitive(self):
        self.assertEqual(text_hash("a b\nc"), text_hash("  a\t b   c  "))

    def test_case_insensitive(self):
        self.assertEqual(text_hash("Merhaba"), text_hash("MERHABA"))

    def test_different_text_differs(self):
        self.assertNotEqual(text_hash("bir"), text_hash("iki"))

    def test_turkish_preserved_not_asciified(self):
        self.assertNotEqual(text_hash("şık"), text_hash("sik"))


class TestFindDuplicates(unittest.TestCase):
    def test_binary_duplicates_grouped(self):
        entries = [
            {"path": "a", "fhash": "X", "thash": "T1", "words": 10},
            {"path": "b", "fhash": "X", "thash": "T1", "words": 10},
            {"path": "c", "fhash": "Y", "thash": "T2", "words": 5},
        ]
        r = find_duplicates(entries)
        self.assertEqual(len(r["binary"]), 1)
        self.assertEqual(sorted(r["binary"][0]), ["a", "b"])

    def test_text_duplicates_exclude_binary_duplicates(self):
        entries = [
            {"path": "a", "fhash": "X", "thash": "T", "words": 10},
            {"path": "b", "fhash": "X", "thash": "T", "words": 10},
        ]
        r = find_duplicates(entries)
        self.assertEqual(r["text"], [])

    def test_text_duplicate_canonical_is_longest(self):
        entries = [
            {"path": "kisa", "fhash": "X", "thash": "T", "words": 100},
            {"path": "uzun", "fhash": "Y", "thash": "T", "words": 900},
        ]
        r = find_duplicates(entries)
        self.assertEqual(r["text"][0][0], "uzun")

    def test_no_duplicates_returns_empty(self):
        entries = [{"path": "a", "fhash": "X", "thash": "T1", "words": 1}]
        r = find_duplicates(entries)
        self.assertEqual(r["binary"], [])
        self.assertEqual(r["text"], [])


class TestFileHash(unittest.TestCase):
    def test_same_bytes_same_hash(self):
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False) as f1, \
             tempfile.NamedTemporaryFile(delete=False) as f2:
            f1.write(b"ayni"); f2.write(b"ayni")
            n1, n2 = f1.name, f2.name
        self.assertEqual(file_hash(n1), file_hash(n2))
        os.unlink(n1); os.unlink(n2)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Testi çalıştır, başarısız olduğunu doğrula**

Run: `cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest tests.test_dedup -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'dedup'`

- [ ] **Step 3: `dedup.py`'i yaz**

```python
"""Tekrar tespiti: birebir aynı dosya (bayt) ve aynı metin (farklı bayt).

Spec §9: birebir aynılarda tek kopya kalır; metin aynılarında kelime sayısı
fazla olan asıl seçilir, diğeri yönlendirme dosyasına dönüşür.
"""
import hashlib
import re

_WS = re.compile(r"\s+")


def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def text_hash(text):
    """Boşluk ve büyük/küçük harf farkını yok sayar. Türkçe karakter KORUNUR."""
    norm = _WS.sub("", text).lower()
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def _group(entries, key):
    buckets = {}
    for e in entries:
        buckets.setdefault(e[key], []).append(e)
    return [v for v in buckets.values() if len(v) > 1]


def find_duplicates(entries):
    """entries: [{'path','fhash','thash','words'}, ...]

    Döner: {'binary': [[path,...]], 'text': [[path,...]]}
    Her grupta ilk eleman asıl (kelime sayısı en fazla, eşitse yol alfabetik).
    'text' grupları, tamamı zaten 'binary' grubu olanları içermez.
    """
    def order(g):
        return sorted(g, key=lambda e: (-e["words"], e["path"]))

    binary = [[e["path"] for e in order(g)] for g in _group(entries, "fhash")]

    text = []
    for g in _group(entries, "thash"):
        if len({e["fhash"] for e in g}) == 1:
            continue  # zaten birebir aynı, binary listesinde
        text.append([e["path"] for e in order(g)])

    binary.sort(key=lambda g: g[0])
    text.sort(key=lambda g: g[0])
    return {"binary": binary, "text": text}
```

- [ ] **Step 4: Testi çalıştır**

Run: `cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest tests.test_dedup -v`
Expected: PASS (10 test).

- [ ] **Step 5: Gerçek arşivde bilinen çiftleri doğrula**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri" && python3 -c "
import sys; sys.path.insert(0,'MD/_Rapor/tools')
from extract import extract_text
from dedup import text_hash
pairs=[('CIFT ANAHTARLI BILGI GUVENLIGI/CIFT ANAHTARLI BILGI GUVENLIGI.doc',
        'ÇİFT ANAHTARLI BİLGİ GÜVENLİĞİ/ÇİFT ANAHTARLI BİLGİ GÜVENLİĞİ.doc')]
import glob,os
for a,b in pairs:
    ha=text_hash(extract_text(a)); hb=text_hash(extract_text(b))
    print('AYNI' if ha==hb else 'FARKLI', os.path.dirname(a), '<->', os.path.dirname(b))
"
```
Expected: `AYNI`. (İkinci dosya adı arşivde farklıysa `ls` ile doğrulanır.)

- [ ] **Step 6: Commit**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && git add -A && git commit -m "feat: ikili ve metin tabanli tekrar tespiti"
```

---

### Task 6: Dosya rolü sınıflandırma

**Files:**
- Create: `MD/_Rapor/tools/classify.py`
- Test: `MD/_Rapor/tools/tests/test_classify.py`

**Interfaces:**
- Consumes: —
- Produces:
  - `role(path: str, rel_inside_topic: str) -> str` — `"belge" | "ornek" | "gorsel" | "arsiv" | "atla"`
  - `BUNDLE_FOLDERS: set[str]` — kitap + kod paketi olan 5 konu klasörü (spec §8)

- [ ] **Step 1: Başarısız testi yaz**

`MD/_Rapor/tools/tests/test_classify.py`:

```python
import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from classify import role, BUNDLE_FOLDERS


class TestRole(unittest.TestCase):
    def test_doc_is_belge(self):
        self.assertEqual(role("CPU/CPU.doc", "CPU.doc"), "belge")

    def test_pdf_is_belge(self):
        self.assertEqual(role("A/x.pdf", "x.pdf"), "belge")

    def test_txt_and_rtf_are_belge(self):
        self.assertEqual(role("A/x.txt", "x.txt"), "belge")
        self.assertEqual(role("A/x.rtf", "x.rtf"), "belge")

    def test_top_level_htm_is_belge(self):
        self.assertEqual(role("OPEN GL/openGL_TR.htm", "openGL_TR.htm"), "belge")

    def test_htm_inside_examples_is_ornek(self):
        # Ornek klasoru icindeki .htm kod sayilir (spec §8)
        self.assertEqual(
            role("CGI-PERL KULLANIMI/form.htm", "form.htm", bundle=True), "ornek")

    def test_code_is_ornek(self):
        for ext in ["php", "asp", "pl", "js", "java", "inc", "cgi", "x", "lib", "dump", "get"]:
            self.assertEqual(role("A/x." + ext, "x." + ext), "ornek", msg=ext)

    def test_gif_is_gorsel(self):
        self.assertEqual(role("A/logo.gif", "logo.gif"), "gorsel")

    def test_archive_formats(self):
        for ext in ["chm", "rar", "mdb", "lit", "swf"]:
            self.assertEqual(role("A/x." + ext, "x." + ext), "arsiv", msg=ext)

    def test_ds_store_skipped(self):
        self.assertEqual(role("A/.DS_Store", ".DS_Store"), "atla")

    def test_unknown_extension_goes_to_arsiv(self):
        self.assertEqual(role("A/x.zzz", "x.zzz"), "arsiv")

    def test_bundle_folders_are_the_five_from_spec(self):
        self.assertEqual(BUNDLE_FOLDERS, {
            "PHP - DEVAM",
            "JAVA SCRİPT - DEVAMI",
            "WEB DERSLERİ - HTML",
            "ASP BOOK ÖRNEKLER",
            "CGI-PERL KULLANIMI",
        })


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Testi çalıştır, başarısız olduğunu doğrula**

Run: `cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest tests.test_classify -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'classify'`

- [ ] **Step 3: `classify.py`'i yaz**

```python
"""Her kaynak dosyanın çıktıdaki rolünü belirler.

belge  -> Markdown'a çevrilir
ornek  -> ornekler/ altına orijinal haliyle kopyalanır
gorsel -> gorseller/ altına kopyalanır
arsiv  -> _Arsiv/ altına kopyalanır
atla   -> hiç kopyalanmaz (.DS_Store gibi sistem dosyaları)
"""
import os

BELGE_EXT = {"doc", "rtf", "txt", "pdf", "htm", "html"}
ORNEK_EXT = {"php", "asp", "pl", "js", "java", "inc", "cgi", "x", "lib",
             "dump", "get", "sql", "css", "bat", "c", "cpp", "pas", "vbs"}
GORSEL_EXT = {"gif", "jpg", "jpeg", "png", "bmp"}
ARSIV_EXT = {"chm", "rar", "zip", "mdb", "lit", "swf", "exe", "dll"}
ATLA = {".DS_Store", "Thumbs.db", "desktop.ini"}

# Kitap + calisan kod paketi olan konu klasorleri (spec §8).
BUNDLE_FOLDERS = {
    "PHP - DEVAM",
    "JAVA SCRİPT - DEVAMI",
    "WEB DERSLERİ - HTML",
    "ASP BOOK ÖRNEKLER",
    "CGI-PERL KULLANIMI",
}


def role(path, rel_inside_topic, bundle=False):
    name = os.path.basename(rel_inside_topic)
    if name in ATLA or name.startswith("._"):
        return "atla"
    ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""

    if ext in GORSEL_EXT:
        return "gorsel"
    if ext in ARSIV_EXT:
        return "arsiv"
    if ext in ORNEK_EXT:
        return "ornek"
    if ext in BELGE_EXT:
        # Paket klasörlerinde .htm/.html çalışan örnek sayılır, belge değil.
        if bundle and ext in ("htm", "html"):
            return "ornek"
        return "belge"
    return "arsiv"
```

- [ ] **Step 4: Testi çalıştır**

Run: `cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 -m unittest tests.test_classify -v`
Expected: PASS (11 test).

- [ ] **Step 5: Arşivde rol dağılımını çıkar**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri" && python3 -c "
import sys,os,collections; sys.path.insert(0,'MD/_Rapor/tools')
from classify import role, BUNDLE_FOLDERS
c=collections.Counter()
for dp,dn,fn in os.walk('.'):
    if dp.startswith('./MD'): continue
    parts=dp.split(os.sep)
    topic=parts[1] if len(parts)>1 else ''
    for f in fn:
        c[role(os.path.join(dp,f), f, bundle=topic in BUNDLE_FOLDERS)]+=1
print(dict(c), 'TOPLAM', sum(c.values()))
"
```
Expected: `belge` ~330, `ornek` ~200, `gorsel` 34, `arsiv` ~21, `atla` ~1. Toplam kaynak dosya sayısına eşit olmalı.

- [ ] **Step 6: Commit**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && git add -A && git commit -m "feat: dosya rolu siniflandirma"
```

---

### Task 7: Ana orkestratör

**Files:**
- Create: `MD/_Rapor/tools/build.py`

**Interfaces:**
- Consumes: `translit.slugify`, `translit.title_from_folder`, `categories.categorize`,
  `extract.*`, `html2md.*`, `classify.role`, `classify.BUNDLE_FOLDERS`, `dedup.*`
- Produces:
  - `scan(root: str) -> list[dict]` — kaynak envanteri: `{path, topic, rel, role, category, slug, title}`
  - `build(root: str, only: list[str]|None = None) -> dict` — dönüşümü çalıştırır, istatistik döner
  - CLI: `python3 build.py [--only Kategori1,Kategori2] [--dry-run]`

- [ ] **Step 1: `build.py`'i yaz**

```python
#!/usr/bin/env python3
"""Arşivi tarar, dönüştürür ve MD/ altına yazar.

Kaynak SALT-OKUNUR açılır. Yalnızca MD/ altına yazılır.

Kullanım:
    python3 build.py                          # tam dönüşüm
    python3 build.py --only Donanim,Guvenlik  # sadece bu kategoriler
    python3 build.py --dry-run                # hiçbir şey yazmaz, planı basar
"""
import argparse
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from categories import categorize
from classify import role, BUNDLE_FOLDERS
from dedup import file_hash, text_hash, find_duplicates
from extract import (ExtractError, doc_metadata, extract_html, extract_pdf_text,
                     extract_text, read_htm)
from html2md import html_to_markdown, text_to_markdown
from translit import safe_name, slugify, title_from_folder

ROOT = "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri"
OUT = os.path.join(ROOT, "MD")


def asset_rel(rel):
    """Ek dosyanın çıktıdaki göreli yolunu üretir.

    Konu klasörünün ilk alt dizini bir 'sarmalayıcı'dır — e-kitap paketlerinde
    'ekitap-Hakki_Ícal-Kitap_ik_PHP_÷rnekler/' gibi mojibake bir kabuk. Bu kabuk
    atılır, altındaki yapı OLDUĞU GİBİ korunur; böylece 'res/logo.gif' ve
    'konular/11.htm' gibi iç referanslar çalışmaya devam eder.
    Kalan bileşenler safe_name'den geçirilir (216 ek dosyanın yalnızca 3'ü
    bu adımda değişir).
    """
    parts = rel.split(os.sep)
    if len(parts) > 1:
        parts = parts[1:]
    return "/".join(safe_name(p) for p in parts)


def scan(root):
    """Kaynak envanterini çıkarır. MD/ atlanır."""
    entries = []
    for topic in sorted(os.listdir(root)):
        tdir = os.path.join(root, topic)
        if topic == "MD" or not os.path.isdir(tdir):
            continue
        bundle = topic in BUNDLE_FOLDERS
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
                    "category": category, "slug": slugify(topic),
                    "title": title_from_folder(topic),
                })
    return entries


def _pick_primary(entries):
    """Her konu klasörü için ana belgeyi seçer: en çok kelimeli 'belge'."""
    by_topic = {}
    for e in entries:
        by_topic.setdefault(e["topic"], []).append(e)
    return by_topic


def _to_markdown(e):
    """Bir 'belge' girdisini (markdown_govde, metadata, kelime_sayisi) üçlüsüne çevirir."""
    ext = e["rel"].rsplit(".", 1)[-1].lower()
    if ext == "pdf":
        txt = extract_pdf_text(e["path"])
        return text_to_markdown(txt), {"author": None, "year": None}, len(txt.split())
    if ext in ("htm", "html"):
        raw = read_htm(e["path"])
        return html_to_markdown(raw), doc_metadata(raw), None
    raw = extract_html(e["path"])
    body = html_to_markdown(raw)
    plain = extract_text(e["path"])
    return body, doc_metadata(raw), len(plain.split())


def _footer(e, meta, extras):
    src = os.path.relpath(e["path"], ROOT)
    bits = ["Kaynak: `%s`" % src]
    if meta.get("author"):
        bits.append(meta["author"])
    if meta.get("year"):
        bits.append(meta["year"])
    lines = ["---", "*" + " — ".join(bits) + "*"]
    for label, rel, n in extras:
        lines.append("*%s: `%s` (%d dosya)*" % (label, rel, n))
    return "\n".join(lines)


def build(root=ROOT, only=None, dry_run=False):
    entries = scan(root)
    if only:
        entries = [e for e in entries if e["category"] in only]

    stats = {"belge": 0, "ornek": 0, "gorsel": 0, "arsiv": 0, "yonlendirme": 0,
             "hata": [], "kisa": [], "yeniden_adlandirilan": [], "yazilan": []}

    # 1) Tekrar analizi — yalnızca 'belge' rolündekiler üzerinde
    docs = [e for e in entries if e["role"] == "belge"]
    hashed = []
    for e in docs:
        try:
            plain = (extract_pdf_text(e["path"])
                     if e["rel"].lower().endswith(".pdf") else extract_text(e["path"]))
        except ExtractError as ex:
            stats["hata"].append((e["path"], str(ex)))
            continue
        hashed.append({"path": e["path"], "fhash": file_hash(e["path"]),
                       "thash": text_hash(plain), "words": len(plain.split())})
    dups = find_duplicates(hashed)
    demoted = {p for g in dups["binary"] for p in g[1:]}
    redirect = {}
    for g in dups["text"]:
        for p in g[1:]:
            redirect[p] = g[0]

    if dry_run:
        print(json.dumps({"toplam": len(entries), "belge": len(docs),
                          "ikili_tekrar": len(dups["binary"]),
                          "metin_tekrar": len(dups["text"])},
                         ensure_ascii=False, indent=2))
        return stats

    # 2) Yazma
    by_topic = _pick_primary(entries)
    used_names = {}
    for topic, group in sorted(by_topic.items()):
        cat = group[0]["category"]
        slug = group[0]["slug"]
        cat_dir = os.path.join(OUT, cat)
        os.makedirs(cat_dir, exist_ok=True)

        belgeler = [e for e in group if e["role"] == "belge" and e["path"] not in demoted]
        ornekler = [e for e in group if e["role"] == "ornek"]
        gorseller = [e for e in group if e["role"] == "gorsel"]
        arsivler = [e for e in group if e["role"] == "arsiv"]

        # Ek klasörleri
        assets = os.path.join(cat_dir, slug)
        extras = []
        def _copy(items, subdir, counter, label):
            if not items:
                return
            for e in items:
                out_rel = asset_rel(e["rel"])
                dest = os.path.join(assets, subdir, out_rel)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy2(e["path"], dest)
                if os.path.basename(out_rel) != os.path.basename(e["rel"]):
                    stats["yeniden_adlandirilan"].append((e["rel"], out_rel))
                stats[counter] += 1
            extras.append((label, "%s/%s/" % (slug, subdir), len(items)))

        _copy(ornekler, "ornekler", "ornek", "Örnekler")
        _copy(gorseller, "gorseller", "gorsel", "Görseller")

        for e in arsivler:
            d = os.path.join(OUT, "_Arsiv", cat if cat != "_Arsiv" else "Diger")
            os.makedirs(d, exist_ok=True)
            name = safe_name(os.path.basename(e["rel"]))
            if name != os.path.basename(e["rel"]):
                stats["yeniden_adlandirilan"].append((e["rel"], name))
            shutil.copy2(e["path"], os.path.join(d, name))
            stats["arsiv"] += 1

        # Belgeler
        for i, e in enumerate(sorted(belgeler, key=lambda x: x["rel"])):
            name = slug if len(belgeler) == 1 else "%s-%d" % (slug, i + 1)
            n = used_names.get((cat, name), 0)
            used_names[(cat, name)] = n + 1
            if n:
                name = "%s-%d" % (name, n + 1)
            dest = os.path.join(cat_dir, name + ".md")

            if e["path"] in redirect:
                target = redirect[e["path"]]
                body = ("Bu içerik arşivde birden fazla kez yer alıyor. "
                        "Asıl kopya: `%s`" % os.path.relpath(target, ROOT))
                md = "# %s\n\n%s\n" % (e["title"], body)
                open(dest, "w", encoding="utf-8").write(md)
                stats["yonlendirme"] += 1
                stats["yazilan"].append(dest)
                continue

            try:
                body, meta, words = _to_markdown(e)
            except ExtractError as ex:
                stats["hata"].append((e["path"], str(ex)))
                continue

            md = "# %s\n\n%s\n\n%s\n" % (e["title"], body, _footer(e, meta, extras))
            open(dest, "w", encoding="utf-8").write(md)
            stats["belge"] += 1
            stats["yazilan"].append(dest)
            if words is not None and words < 300:
                stats["kisa"].append((dest, words))

            # PDF ise orijinali yanına kopyala (spec §10)
            if e["rel"].lower().endswith(".pdf"):
                shutil.copy2(e["path"], os.path.join(cat_dir, name + ".pdf"))

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
        print("belge:%d yonlendirme:%d ornek:%d gorsel:%d arsiv:%d hata:%d kisa:%d"
              % (s["belge"], s["yonlendirme"], s["ornek"], s["gorsel"], s["arsiv"],
                 len(s["hata"]), len(s["kisa"])))
        json.dump({k: v for k, v in s.items() if k != "dups"},
                  open(os.path.join(OUT, "_Rapor", "stats.json"), "w"),
                  ensure_ascii=False, indent=2)
        json.dump(s["dups"], open(os.path.join(OUT, "_Rapor", "dups.json"), "w"),
                  ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Kuru çalıştırma — hiçbir şey yazılmadığını doğrula**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 build.py --dry-run
```
Expected: JSON çıktısı (`toplam`, `belge`, `ikili_tekrar`, `metin_tekrar`). `MD/` altında `_Rapor/` dışında yeni klasör oluşmamalı:
```bash
ls "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD"
```
Expected: sadece `_Rapor`.

- [ ] **Step 3: Kaynağın değişmediğini doğrula**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri" && find . -path ./MD -prune -o -type f -print | wc -l
```
Expected: 691 (başlangıçtaki dosya sayısı). Değiştiyse `build.py`'de yazma yolu hatalıdır — **derhal durdurulur**.

- [ ] **Step 4: Tek kategoriyle pilot çalıştırma**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 build.py --only Donanim && ls -la "../../Donanim" && head -40 "../../Donanim/CPU.md"
```
Expected: `Donanim/` altında ~19 `.md`. `CPU.md` H1 başlık + gövde + kaynak dipnotu içermeli, Türkçe karakterler sağlam.

- [ ] **Step 5: Commit**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && git add -A && git commit -m "feat: ana donusum orkestratoru"
```

---

### Task 8: INDEX ve raporlar

**Files:**
- Create: `MD/_Rapor/tools/report.py`

**Interfaces:**
- Consumes: `MD/_Rapor/stats.json`, `MD/_Rapor/dups.json` (Task 7 çıktısı)
- Produces:
  - `write_index(out_dir: str) -> str` — `MD/INDEX.md`
  - `write_conversion_report(out_dir: str) -> str` — `MD/_Rapor/donusum-raporu.md`
  - `write_dup_report(out_dir: str) -> str` — `MD/_Rapor/tekrarlar.md`
  - `write_archive_readme(out_dir: str) -> str` — `MD/_Arsiv/README.md`

- [ ] **Step 1: `report.py`'i yaz**

```python
#!/usr/bin/env python3
"""MD/ altındaki çıktıdan INDEX ve raporları üretir. build.py'den SONRA çalışır."""
import json
import os
import re
import sys

ROOT = "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri"
OUT = os.path.join(ROOT, "MD")
RAPOR = os.path.join(OUT, "_Rapor")


def _md_files(cat_dir):
    return sorted(f for f in os.listdir(cat_dir) if f.endswith(".md"))


def _first_h1(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
    return os.path.basename(path)[:-3]


def _word_count(path):
    with open(path, encoding="utf-8") as f:
        return len(f.read().split())


def write_index(out_dir=OUT):
    cats = sorted(d for d in os.listdir(out_dir)
                  if os.path.isdir(os.path.join(out_dir, d)) and not d.startswith("_"))
    lines = ["# Bilgisayar Bilgileri Arşivi", "",
             "1998–2004 arası Türkçe bilgisayar ders notları ve e-kitapları.",
             "Kaynak arşivden Markdown'a çevrilmiştir; metinler birebir korunmuştur.", ""]
    total = 0
    for c in cats:
        files = _md_files(os.path.join(out_dir, c))
        total += len(files)
        lines.append("## %s (%d)" % (c.replace("-", " "), len(files)))
        lines.append("")
        for f in files:
            p = os.path.join(out_dir, c, f)
            lines.append("- [%s](%s/%s) — %d kelime" % (_first_h1(p), c, f, _word_count(p)))
        lines.append("")
    lines.insert(4, "**Toplam %d konu, %d kategori.**" % (total, len(cats)))
    lines.insert(5, "")
    if os.path.isdir(os.path.join(out_dir, "_Arsiv")):
        lines += ["## Arşiv", "",
                  "Markdown'a çevrilemeyen formatlar: [_Arsiv/](_Arsiv/README.md)", ""]
    path = os.path.join(out_dir, "INDEX.md")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return path


def write_conversion_report(out_dir=OUT):
    s = json.load(open(os.path.join(RAPOR, "stats.json"), encoding="utf-8"))
    lines = ["# Dönüşüm Raporu", "",
             "| Ölçüt | Adet |", "| --- | --- |",
             "| Markdown'a çevrilen belge | %d |" % s["belge"],
             "| Tekrar yönlendirme dosyası | %d |" % s["yonlendirme"],
             "| Kopyalanan kod örneği | %d |" % s["ornek"],
             "| Kopyalanan görsel | %d |" % s["gorsel"],
             "| Arşive alınan dosya | %d |" % s["arsiv"],
             "| Hata | %d |" % len(s["hata"]), ""]
    if s["hata"]:
        lines += ["## Hatalar", ""]
        for p, e in s["hata"]:
            lines.append("- `%s` — %s" % (os.path.relpath(p, ROOT), e))
        lines.append("")
    if s["kisa"]:
        lines += ["## 300 kelimenin altındaki dosyalar", "",
                  "Bunlar önsöz / içindekiler / kalıntı sayfalardır (spec §3/P7). "
                  "Silinmemiştir, bilgi amaçlı listelenir.", ""]
        for p, w in sorted(s["kisa"], key=lambda x: x[1]):
            lines.append("- `%s` — %d kelime" % (os.path.relpath(p, out_dir), w))
        lines.append("")
    if s.get("yeniden_adlandirilan"):
        lines += ["## Yeniden adlandırılan ek dosyalar", "",
                  "Dosya adı geçersiz karakter içerdiği için değiştirildi (spec §5).", ""]
        for old, new in sorted(s["yeniden_adlandirilan"]):
            lines.append("- `%s` → `%s`" % (old, new))
        lines.append("")
    path = os.path.join(RAPOR, "donusum-raporu.md")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return path


def write_dup_report(out_dir=OUT):
    d = json.load(open(os.path.join(RAPOR, "dups.json"), encoding="utf-8"))
    lines = ["# Tekrar Raporu", "",
             "İki tür tekrar tespit edildi (spec §9).", "",
             "## Birebir aynı dosyalar (%d grup)" % len(d["binary"]), "",
             "Her gruptan yalnızca ilk sıradaki dönüştürüldü.", ""]
    for g in d["binary"]:
        lines.append("- **%s**" % os.path.relpath(g[0], ROOT))
        for x in g[1:]:
            lines.append("  - atlandı: `%s`" % os.path.relpath(x, ROOT))
    lines += ["", "## Aynı metin, farklı dosya (%d grup)" % len(d["text"]), "",
              "Kelime sayısı fazla olan asıl seçildi; diğerleri yönlendirme dosyası oldu.", ""]
    for g in d["text"]:
        lines.append("- **%s**" % os.path.relpath(g[0], ROOT))
        for x in g[1:]:
            lines.append("  - yönlendirildi: `%s`" % os.path.relpath(x, ROOT))
    path = os.path.join(RAPOR, "tekrarlar.md")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return path


AÇIKLAMA = {
    "chm": "Windows derlenmiş HTML yardım dosyası. macOS'ta açmak için bir CHM okuyucu gerekir.",
    "rar": "RAR arşivi. `unar` veya The Unarchiver ile açılır.",
    "mdb": "Microsoft Access veritabanı. Access veya LibreOffice Base ile açılır.",
    "lit": "Microsoft Reader e-kitabı. Artık desteklenmeyen bir format.",
    "swf": "Macromedia Flash animasyonu. Flash Player kaldırıldığı için Ruffle gerekir.",
}


def write_archive_readme(out_dir=OUT):
    adir = os.path.join(out_dir, "_Arsiv")
    if not os.path.isdir(adir):
        return None
    lines = ["# Arşiv", "",
             "Markdown'a çevrilemeyen formatlar. Kaynaktan kopyalanmıştır, taşınmamıştır.", ""]
    for dp, dn, fn in sorted(os.walk(adir)):
        files = sorted(f for f in fn if f != "README.md")
        if not files:
            continue
        rel = os.path.relpath(dp, adir)
        lines.append("## %s" % (rel if rel != "." else "Kök"))
        lines.append("")
        for f in files:
            ext = f.rsplit(".", 1)[-1].lower()
            size = os.path.getsize(os.path.join(dp, f)) / 1024
            lines.append("- `%s` — %.0f KB. %s" % (f, size, AÇIKLAMA.get(ext, "")))
        lines.append("")
    path = os.path.join(adir, "README.md")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return path


if __name__ == "__main__":
    for fn in (write_index, write_conversion_report, write_dup_report, write_archive_readme):
        p = fn()
        if p:
            print("yazildi:", os.path.relpath(p, ROOT))
```

- [ ] **Step 2: Pilot çıktı üzerinde çalıştır**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 report.py && head -30 ../../INDEX.md
```
Expected: `INDEX.md`, `donusum-raporu.md`, `tekrarlar.md` yazıldı. INDEX'te `Donanim` kategorisi ve konuları listelenmiş.

- [ ] **Step 3: Commit**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && git add -A && git commit -m "feat: INDEX ve rapor uretimi"
```

---

### Task 9: Doğrulama

**Files:**
- Create: `MD/_Rapor/tools/verify.py`

**Interfaces:**
- Consumes: `MD/` çıktısı, kaynak arşiv, `MD/_Rapor/stats.json`
- Produces:
  - `verify(root: str) -> list[dict]` — `[{check, ok, detail}]`, spec §12'deki 5 kontrol
  - CLI çıkış kodu: hepsi geçerse 0, biri kalırsa 1

- [ ] **Step 1: `verify.py`'i yaz**

```python
#!/usr/bin/env python3
"""Spec §12 doğrulamaları. build.py + report.py'den SONRA çalışır.

1. Kelime sayısı korunumu   2. Türkçe karakter bütünlüğü
3. Dosya adı geçerliliği    4. Kayıp yok      5. Link bütünlüğü
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import role, BUNDLE_FOLDERS
from extract import ExtractError, extract_pdf_text, extract_text

ROOT = "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri"
OUT = os.path.join(ROOT, "MD")

MOJIBAKE = ["Ã¼", "Ã§", "Ä±", "Å\u009f", "ï¿½", "\ufffd", "Ä\u009e", "Å\u009e"]
VALID_PATH = re.compile(r"^[A-Za-z0-9._/-]+$")


def _md_paths():
    for dp, dn, fn in os.walk(OUT):
        if os.path.basename(dp) == "tools":
            dn[:] = []
            continue
        for f in fn:
            if f.endswith(".md"):
                yield os.path.join(dp, f)


def check_word_counts():
    """Her .md, kaynağının en az %90'ı kadar kelime içermeli."""
    stats = json.load(open(os.path.join(OUT, "_Rapor", "stats.json"), encoding="utf-8"))
    bad = []
    for md in _md_paths():
        text = open(md, encoding="utf-8").read()
        m = re.search(r"Kaynak: `([^`]+)`", text)
        if not m:
            continue
        src = os.path.join(ROOT, m.group(1))
        if not os.path.isfile(src):
            bad.append((md, "kaynak bulunamadi"))
            continue
        try:
            plain = (extract_pdf_text(src) if src.lower().endswith(".pdf")
                     else extract_text(src))
        except ExtractError:
            continue
        src_w, md_w = len(plain.split()), len(text.split())
        if src_w > 50 and md_w < src_w * 0.90:
            bad.append((os.path.relpath(md, OUT), "%d < %d*0.9" % (md_w, src_w)))
    return {"check": "Kelime sayisi korunumu", "ok": not bad, "detail": bad[:20]}


def check_no_mojibake():
    bad = []
    for md in _md_paths():
        text = open(md, encoding="utf-8").read()
        hits = [b for b in MOJIBAKE if b in text]
        if hits:
            bad.append((os.path.relpath(md, OUT), hits))
    return {"check": "Turkce karakter butunlugu", "ok": not bad, "detail": bad[:20]}


def check_path_charset():
    bad = []
    for dp, dn, fn in os.walk(OUT):
        if os.path.basename(dp) == "tools":
            dn[:] = []
            continue
        for name in list(dn) + fn:
            rel = os.path.relpath(os.path.join(dp, name), OUT)
            if not VALID_PATH.match(rel):
                bad.append(rel)
    return {"check": "Dosya adi gecerliligi", "ok": not bad, "detail": bad[:20]}


def check_no_loss():
    """Kaynaktaki her dosyanın çıktıda bir karşılığı olmalı."""
    stats = json.load(open(os.path.join(OUT, "_Rapor", "stats.json"), encoding="utf-8"))
    dups = json.load(open(os.path.join(OUT, "_Rapor", "dups.json"), encoding="utf-8"))
    accounted = (stats["belge"] + stats["yonlendirme"] + stats["ornek"]
                 + stats["gorsel"] + stats["arsiv"])
    skipped = sum(len(g) - 1 for g in dups["binary"])
    errors = len(stats["hata"])

    src_total = 0
    for topic in os.listdir(ROOT):
        tdir = os.path.join(ROOT, topic)
        if topic == "MD" or not os.path.isdir(tdir):
            continue
        bundle = topic in BUNDLE_FOLDERS
        for dp, dn, fn in os.walk(tdir):
            for f in fn:
                if role(os.path.join(dp, f), f, bundle=bundle) != "atla":
                    src_total += 1

    diff = src_total - (accounted + skipped + errors)
    return {"check": "Kayip yok", "ok": diff == 0,
            "detail": "kaynak=%d islenen=%d atlanan_tekrar=%d hata=%d fark=%d"
                      % (src_total, accounted, skipped, errors, diff)}


LINK_RE = re.compile(r"\]\((?!https?://)([^)]+)\)")


def check_links():
    bad = []
    for md in _md_paths():
        base = os.path.dirname(md)
        for target in LINK_RE.findall(open(md, encoding="utf-8").read()):
            target = target.split("#")[0]
            if not target:
                continue
            if not os.path.exists(os.path.join(base, target)):
                bad.append((os.path.relpath(md, OUT), target))
    return {"check": "Link butunlugu", "ok": not bad, "detail": bad[:20]}


def verify(root=ROOT):
    return [check_word_counts(), check_no_mojibake(), check_path_charset(),
            check_no_loss(), check_links()]


if __name__ == "__main__":
    results = verify()
    failed = 0
    for r in results:
        mark = "GECTI" if r["ok"] else "KALDI"
        print("[%s] %s" % (mark, r["check"]))
        if not r["ok"]:
            failed += 1
            print("      ", r["detail"])
    sys.exit(1 if failed else 0)
```

- [ ] **Step 2: Pilot çıktı üzerinde çalıştır**

Run:
```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 verify.py; echo "cikis: $?"
```
Expected: Beş kontrolün her biri raporlanır. Pilot aşamada `Kayip yok` kontrolü doğal olarak KALDI verir (sadece bir kategori dönüştürüldü) — tam çalıştırmadan sonra geçmelidir. Diğer dördü GEÇTİ olmalı.

- [ ] **Step 3: Commit**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && git add -A && git commit -m "feat: cikti dogrulama kontrolleri"
```

---

### Task 10: Pilot onayı ve tam dönüşüm

**Files:**
- Modify: yok — yalnızca çalıştırma ve gözden geçirme

**Interfaces:**
- Consumes: Task 1–9'un tamamı
- Produces: `MD/` altında tam çıktı

- [ ] **Step 1: Pilot çıktıyı temizle ve üç kategoriyle yeniden üret**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD" && \
  find . -mindepth 1 -maxdepth 1 ! -name '_Rapor' -exec rm -rf {} + && \
  cd _Rapor/tools && python3 build.py --only Donanim,Web-Gelistirme,Sozluk-ve-Referans && python3 report.py
```
Expected: Üç kategori üretildi. `Web-Gelistirme` paket klasörlerini (`PHP-Kitapcigi/ornekler/`) içermeli.

- [ ] **Step 2: Örnekleri gözden geçir ve kullanıcıya göster**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD" && \
  ls Donanim Web-Gelistirme Sozluk-ve-Referans && \
  echo "=== CPU ===" && head -35 Donanim/CPU.md && \
  echo "=== PHP ===" && head -35 Web-Gelistirme/PHP-Kitapcigi.md && \
  echo "=== ORNEKLER ===" && ls Web-Gelistirme/PHP-Kitapcigi/ornekler | head
```
Expected: Başlıklar `##` ile ayrılmış, Türkçe sağlam, dipnotlar doğru, örnek kodlar yerinde.
**Bu noktada kullanıcı onayı alınır.** Onay gelmeden Step 4'e geçilmez.

- [ ] **Step 3: Kaynağın hâlâ el değmemiş olduğunu doğrula**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri" && \
  find . -path ./MD -prune -o -type f -print | wc -l && \
  find . -path ./MD -prune -o -type d -print | wc -l
```
Expected: 691 dosya, 271 dizin — başlangıçtaki değerlerle birebir aynı.

- [ ] **Step 4: Tam dönüşümü çalıştır**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD" && \
  find . -mindepth 1 -maxdepth 1 ! -name '_Rapor' -exec rm -rf {} + && \
  cd _Rapor/tools && time python3 build.py && python3 report.py
```
Expected: `belge:~250 ornek:~200 gorsel:34 arsiv:~21 hata:0`. Süre ~5–15 dakika (PDF'ler için Swift çağrıları yavaş).

- [ ] **Step 5: Tam doğrulama**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && python3 verify.py; echo "cikis: $?"
```
Expected: `cikis: 0` — beş kontrolün beşi de GEÇTİ. Kalan varsa detayına göre ilgili modül düzeltilip Step 4–5 tekrarlanır.

- [ ] **Step 6: Sonucu özetle**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD" && \
  du -sh . && ls && wc -l INDEX.md && \
  for d in */; do printf "%-24s %s\n" "$d" "$(ls "$d" 2>/dev/null | grep -c '\.md$')"; done
```
Expected: Kategori başına dosya sayıları spec §6'daki tahminlerle uyumlu.

- [ ] **Step 7: Commit**

```bash
cd "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri/MD/_Rapor/tools" && git add -A && git commit -m "chore: tam donusum calistirildi ve dogrulandi"
```

---

## Öz Denetim

**Spec kapsamı:**

| Spec bölümü | Karşılayan task |
|---|---|
| §2 Kaynak envanteri | Task 3 (çıkarma), Task 6 (roller) |
| §3/P1 Mojibake dosya adları | Task 1 — başlık klasör adından |
| §3/P2 İsimsiz dosyalar | Task 1 — aynı çözüm |
| §3/P3 Güvenilmez `<title>` | Task 3 `doc_metadata` — başlık olarak kullanılmaz, dipnota gider |
| §3/P4 İki katmanlı tekrar | Task 5 (`dedup.py`), Task 7 (uygulama) |
| §3/P5 Konu örtüşmeleri | Birleştirme yok — Task 7 her belgeyi ayrı yazar |
| §3/P6 `TIP` klasörü | Task 2 `OVERRIDES["TIP"] = "_Arsiv"` |
| §3/P7 Kısa dosyalar | Task 7 `stats["kisa"]`, Task 8 raporu |
| §4 Dokunulmazlık | Task 7 Step 3, Task 10 Step 3 — dosya sayısı kontrolü |
| §5 İsimlendirme | Task 1 |
| §6 Kategoriler | Task 2 |
| §7 Dosya biçimi | Task 4 (`html2md`), Task 7 (`_footer`) |
| §8 Ekleri olan konular | Task 6 `BUNDLE_FOLDERS`, Task 7 `ornekler/` + `gorseller/` |
| §9 Tekrar politikası | Task 5 + Task 7 `redirect` / `demoted` |
| §10 Dönüştürülemeyenler | Task 6 `arsiv` rolü, Task 7 `_Arsiv/`, Task 8 README |
| §11 Raporlar | Task 8 |
| §12 Doğrulama (5 kontrol) | Task 9 |
| §13 Kapsam dışı | Hiçbir taskta özetleme/yeniden yazım adımı yok |

**Yer tutucu taraması:** Plan içinde TBD/TODO yok; her kod adımı çalıştırılabilir kod içeriyor, her test adımı gerçek assert'ler taşıyor.

**Tip tutarlılığı:**
- `slugify` / `title_from_folder` (Task 1) → `build.scan` (Task 7) ✅
- `categorize` (Task 2) → `build.scan` ✅
- `extract_html` / `extract_text` / `extract_pdf_text` / `read_htm` / `doc_metadata` (Task 3) → `build._to_markdown`, `verify.check_word_counts` ✅
- `html_to_markdown` / `text_to_markdown` (Task 4) → `build._to_markdown` ✅
- `file_hash` / `text_hash` / `find_duplicates` (Task 5) → `build.build` ✅
- `role` / `BUNDLE_FOLDERS` (Task 6) → `build.scan`, `verify.check_no_loss` ✅
- `stats.json` / `dups.json` (Task 7) → `report.py` (Task 8), `verify.py` (Task 9) ✅
