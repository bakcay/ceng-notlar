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

# PRE_SUBS zaten doğru karma büyük/küçük harfle üretir (CSharp); _cap'in
# varsayılan "ilk harf büyük, gerisi küçük" kuralı bunu bozar (Csharp olur).
SPECIAL_CASE = {"CSHARP": "CSharp"}

# Python'un yerleşik str.lower() metodu yalnızca "İ" (LATIN CAPITAL LETTER I
# WITH DOT ABOVE) için hatalıdır: "İ".lower() -> "i̇" (bileşik, i +
# COMBINING DOT ABOVE) üretir, düz "i" değil. Diğer harfler (I, ı, i, Ç,
# Ğ, Ö, Ş, Ü ve küçükleri) str.lower()/upper() ile zaten doğru davranır.
TR_LOWER_MAP = str.maketrans({"İ": "i"})


def _tr_lower(s):
    return s.translate(TR_LOWER_MAP).lower()

# Kesme işaretleri kelimeyi bölmeden atılır: "XML 'i" -> "XML i", "Excell’de" -> "Excellde"
APOSTROPHES = "'‘’ʼ´`"


def to_ascii(text):
    """Türkçe harfleri ASCII karşılığına çevirir. Başka hiçbir şeyi değiştirmez.

    Önce NFC'ye normalize eder: macOS dosya sistemi Türkçe harfleri NFD
    (ayrışık, ör. "İ" -> "I" + COMBINING DOT ABOVE) döndürür ve TR_MAP
    yalnızca önceden birleşik (precomposed) karakterleri tanır.
    """
    return unicodedata.normalize("NFC", text).translate(TR_MAP)


def _words(text, ascii_out):
    for old, new in PRE_SUBS:
        text = text.replace(old, new)
    text = "".join("" if ch in APOSTROPHES else ch for ch in text)
    if ascii_out:
        text = to_ascii(text)
        text = re.sub(r"[^A-Za-z0-9]+", " ", text)
    else:
        text = re.sub(r"[^0-9A-Za-zÀ-ɏ]+", " ", text)
    return [w for w in text.split() if w]


def _cap(word):
    """Kısaltmaysa büyük bırak, değilse Baş Harfi Büyük yap."""
    if len(word) == 1:
        # Tek harfli kalıntılar (ör. "XML 'i" -> "i") kesme işaretiyle
        # ayrılmış ek parçalarıdır; orijinal harf durumu korunur.
        return word
    upper = to_ascii(word).upper()
    if upper in SPECIAL_CASE:
        return SPECIAL_CASE[upper]
    if upper in ACRONYMS:
        return upper
    if word.isdigit():
        return word
    return word[0].upper() + _tr_lower(word[1:])


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
    # NFD (yalnızca kanonik ayrışma) kullanılır; NFKD kullanılırsa üst simge
    # rakamlar gibi uyumluluk-eşdeğerleri (³ -> 3) sessizce rakama döner —
    # bunlar burada "ayrıştırılamaz" sembol sayılıp tireye çevrilmelidir.
    base = "".join(c for c in unicodedata.normalize("NFD", base)
                   if not unicodedata.combining(c))
    base = re.sub(r"[^A-Za-z0-9._-]+", "-", base)
    base = re.sub(r"-{2,}", "-", base).strip("-") or "dosya"
    ext = re.sub(r"[^A-Za-z0-9]+", "", to_ascii(ext))
    return base + ("." + ext if ext else "")


# Başlıktan atılacak dosya uzantıları. Arşivde üç konu KLASÖRÜNÜN adı bir
# dosya uzantısıyla bitiyor (ACCESS VERİ TABANI.doc/, BİLGİSAYAR
# AĞLARINDA TEMEL KAVRAMLAR.doc/, quickbasickursu.pdf/) -- bunlar dizin,
# dosya değil; uzantı başlıkta görünmemeli.
#
# Uzantı "sondaki 1-5 harflik nokta eki" gibi GENEL bir kuralla atılamaz:
# arşivde `ASP.NET` adlı bir konu klasörü var ve "NET" tam da o kalıba
# uyuyor. Bu yüzden yalnızca AÇIK BİR LİSTEDEKİ gerçek dosya uzantıları
# atılır. (Noktası ortada olan adlar -- `Asp'ye giris.Asp nedir`,
# `VISUAL BASIC 5.0’IN GETİRDİĞİ YENİLİKLER` -- zaten sonda eşleşmediği
# için etkilenmez.)
TITLE_STRIP_EXTS = {
    "doc", "docx", "rtf", "txt", "pdf", "htm", "html",
    "xls", "xlsx", "ppt", "pptx", "chm", "zip", "rar",
}
_TRAILING_EXT_RE = re.compile(r"\.([A-Za-z0-9]{1,5})$")


def _strip_title_ext(text):
    m = _TRAILING_EXT_RE.search(text)
    if m and m.group(1).lower() in TITLE_STRIP_EXTS:
        return text[:m.start()].rstrip()
    return text


def slug_from_folder(text):
    """Bir konu KLASÖRÜ adından dosya adı kökü üretir.

    `slugify`den tek farkı, `title_from_folder` ile aynı uzantı atma
    kuralını uygulamasıdır: arşivdeki üç konu klasörünün adı bir dosya
    uzantısıyla bitiyor ve bu uzantı ne başlıkta ne de dosya adında
    görünmeli. Uzantı yalnızca H1'den atıldığı sürece çıktı adları
    `Quickbasickursu-Pdf.md`, `Access-Veri-Tabani-Doc.md`,
    `Bilgisayar-Aglarinda-Temel-Kavramlar-Doc.md` gibi kalıyordu.

    `slugify` GENEL amaçlıdır (gerçek dosya adları da ondan geçebilir);
    uzantı atma yalnızca "bu ad bir KLASÖRÜN adı" bilindiğinde doğrudur,
    bu yüzden ayrı bir fonksiyondur.
    """
    return slugify(_strip_title_ext(unicodedata.normalize("NFC", text)))


def title_from_folder(text):
    """H1 başlığı üretir. Türkçe karakterler korunur, noktalama sadeleştirilir."""
    # NFC'ye normalize et: macOS dosya sistemi NFD (ayrışık) döner, ve
    # _cap içindeki word.replace(core, capped, 1) yalnızca önceden
    # birleşik (precomposed) karakterlerde doğru alt dize eşleşmesi bulur.
    src = unicodedata.normalize("NFC", text)
    # Uzantı, sözcük büyük/küçük harf düzeltmesinden ÖNCE atılır. Aksi
    # halde "TABANI.doc" tek bir sözcük sayılıyor, `core` ondan
    # "TABANIdoc" üretiyor ve `w.replace(core, capped, 1)` noktalı asıl
    # sözcükte bu alt dizeyi bulamadığı için sözcük HİÇ düzeltilmeden
    # kalıyordu -- "# Access Veri TABANI.doc" çıktısının nedeni buydu.
    src = _strip_title_ext(src)
    for old, new in PRE_SUBS[:4]:  # C++/C# yalnızca; '+' ve '&' başlıkta korunur
        src = src.replace(old, new)
    src = re.sub(r"\s*,\s*", ", ", src)
    src = re.sub(r"\s*-\s*", " - ", src)
    src = re.sub(r"\s+", " ", src).strip()
    out = []
    for w in src.split(" "):
        core = re.sub(r"[^0-9A-Za-zÀ-ɏ]", "", w)
        if not core:
            out.append(w)
            continue
        capped = _cap(core)
        out.append(w.replace(core, capped, 1))
    return " ".join(out)
