"""Kaynak dosyadan UTF-8 HTML veya düz metin çıkarır.

Bu modül format bilir, içerik bilmez. Tüm kaynak erişimi salt-okunurdur.
Zincir: .doc/.rtf/.txt -> textutil | .htm -> iconv | .pdf -> swift+PDFKit
"""
import codecs
import os
import re
import subprocess
import unicodedata

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_SWIFT = os.path.join(TOOLS_DIR, "pdftext.swift")

# Denenecek kodlamalar, sırayla. Arşivdeki .htm'ler ağırlıkla Windows-1254.
HTM_ENCODINGS = ["utf-8", "windows-1254", "iso-8859-9", "cp1252", "latin-1"]

# read_htm() bir dosyayı bildirilen (veya ilk aday) kodlama dışında bir
# kodlamayla çözdüğünde buraya bir kayıt eklenir. Her kayıt:
#   {"path": str, "declared": str|None, "used": str, "lossy": bool}
# "lossy": True yalnızca son çare `windows-1254` + errors="replace" dalı
# çalıştığında set edilir; bu durumda çıktıda U+FFFD (replacement char)
# bulunabilir. Çağıranlar bu listeyi arşiv taraması sonunda inceleyip
# hangi dosyaların sessizce farklı kodlamayla okunduğunu görebilir.
FALLBACK_LOG = []


class ExtractError(Exception):
    pass


class GarbageError(ExtractError):
    """textutil basarili cikti (exit 0) ama sonuc kullanilamaz.

    4 buyuk (10-34 MB) .doc dosyasi -- gercek OLE Composite Document,
    icine gomulu resimlerle -- textutil'i yeniyor: exit code 0 doner ama
    govde ham OLE baytlaridir, anlamli Turkce kelime icermez. Cagiran taraf
    bu hatayi yakalayip recover_doc_text() ile devam edebilir (bkz. Task 3b).
    """
    pass


# --- CP1254 mojibake onarimi -------------------------------------------
#
# 2004'te kaydedilmis 6 kaynak dosya yanlis kod sayfasiyla islenmis: dosya
# CP1254 baytlari icerirken Latin-1 olarak cozülmus (textutil -encoding
# UTF-8 bunu telafi edemiyor, kaynaktaki bozulma zaten metne isleniyor).
# Etkilenen 6 karakterin Latin-1 <-> CP1254 karsiligi birebir bu tablo:
#   Ý(0xDD)->İ  þ(0xFE)->ş  ý(0xFD)->ı  Þ(0xDE)->Ş  ð(0xF0)->ğ  Ð(0xD0)->Ğ
# text.encode('latin-1').decode('cp1254') ayni sonucu verir GIBI gorunur
# ama U+2019 (kivrik apostrof) gibi Latin-1 disi karakterlerde patlar ya da
# errors='replace' ile sessizce bozulur -- bu yuzden kesin bir 6 karakterlik
# haritayla, saf karakter degisimiyle yapiliyor.
MOJIBAKE_MAP = {
    "Ý": "İ",
    "þ": "ş",
    "ý": "ı",
    "Þ": "Ş",
    "ð": "ğ",
    "Ð": "Ğ",
}
_MOJIBAKE_TABLE = str.maketrans(MOJIBAKE_MAP)

# Tam arsiv taramasi (249 .doc/.rtf + 188 .htm, bkz. Task 3b raporu):
# marker sayisi dagilimi net bir bosluk gosteriyor -- 6 dosya 173-7547
# marker (dokumanin her paragrafi bozuk), 3 dosya tam olarak 3 marker
# (C kaynak kodu yorumlarinda tek bir "ý" yazim hatasi, sistemik degil),
# geri kalan 240 dosya 0. Esik >20, bu 6 dosyayi 240+3'ten kesin ayirir
# (en dusuk gercek hasar 173, en yuksek yanlis-pozitif adayi 3 -- 57 kat
# marj). read_htm tarafinda 188 dosyanin tamami 0 marker verdi; hasar
# yalnizca bu 6 .doc dosyasinda.
MOJIBAKE_THRESHOLD = 20

# repair_mojibake() gercekten uygulandiginda (bkz. _repair_if_damaged)
# buraya (path, n_replaced) eklenir; Task 8 raporu bunu listeler.
REPAIRED = []


def _log_once(log, path, value):
    """(path, value) kaydini ayni yol icin YALNIZCA BIR KEZ ekler.

    F4: bu listeler "dosya basina bir kayit" olarak okunuyor ama eskiden
    her CAGRI basina ekleniyordu. Boru hatti ayni belge icin hem
    extract_html hem extract_text cagirir (ayrica read_htm ve kurtarma
    yollari da vardir); sonucta rapor 6 hasarli dosyayi iki kez listeliyor
    ve butun marker toplamlarini ikiye katliyordu.

    Uyelik listenin KENDISINDEN okunur (ayri bir "gorulen" kumesi
    tutulmaz): testler ve cagiranlar bu listeleri .clear() ile
    sifirliyor; ayri bir kume tutulsaydi clear() sonrasi kayit sessizce
    bastirilirdi. Listeler dosya sayisi kadar kisa (<=6) oldugundan
    dogrusal tarama pratikte bedelsizdir.
    """
    for p, _ in log:
        if p == path:
            return False
    log.append((path, value))
    return True


def repair_mojibake(text):
    """CP1254-as-Latin1 mojibake'ini 6 karakterlik sabit haritayla onarir.

    Salt fonksiyon, I/O yok. Donus: (onarilmis_metin, degistirilen_sayisi).
    Hasar yoksa (n==0) metin degismeden doner (referans esitligi korunur).
    """
    n = sum(text.count(c) for c in MOJIBAKE_MAP)
    if n == 0:
        return text, 0
    return text.translate(_MOJIBAKE_TABLE), n


def _repair_if_damaged(text, path):
    """repair_mojibake'i cagirir; yalnizca esik asilirsa sonucu kullanir.

    Esigin altinda kalan (1-19) marker'lar izole yazim hatasi/typo olarak
    degerlendirilir (bkz. MOJIBAKE_THRESHOLD yorumu) ve dokunulmadan birakilir
    -- boylece "hasar gercekken onar" kurali (spec) tek bir yerde uygulanir.
    """
    repaired, n = repair_mojibake(text)
    if n > MOJIBAKE_THRESHOLD:
        _log_once(REPAIRED, path, n)
        return repaired
    return text


# --- .doc kurtarma: textutil'in yenildigi buyuk OLE dosyalari -----------
#
# 4 buyuk (10-34 MB) .doc dosyasi gercek OLE Composite Document'tir (icine
# gomulu resimlerle); textutil exit 0 donuyor ama govde ham OLE baytlaridir.
# Gercek metin dosyada UTF-16LE olarak duruyor (Word'un ic temsili); ham
# baytlari utf-16-le ile cozmek okunakli Turkce duzyaziyi OLE ikili
# gurultusuyle serpistirilmis halde verir. looks_like_garbage() bu 4
# dosyayi textutil ciktisinda tespit eder; recover_doc_text() ham dosyadan
# dogrudan (textutil'i atlayarak) kurtarma yapar.

# "Gecerli duzyazi" alfabesi: Turkce+ASCII harfler, rakam, bosluk, sik
# noktalama. looks_like_garbage() bu kumenin DISINDA kalan karakterlerin
# oranini olcer; recover_doc_text() ayni kumeyi kullanarak UTF-16LE
# cozumundeki "makul metin" koşularini ikili gurultudan ayirir.
_PLAUSIBLE_PROSE_CHARS = (
    r"A-Za-zÇĞİIıÖŞÜçğıöşü0-9\s.,;:!?()'\"\-/%_*+=<>\[\]{}@#&"
)
_GARBAGE_INVALID_RE = re.compile("[^" + _PLAUSIBLE_PROSE_CHARS + "]")

# Tam arsiv taramasi (249 .doc/.rtf, hem txt hem html modu, bkz. Task 3b
# raporu): 4 bilinen bozuk dosyanin "gecersiz karakter orani" txt modunda
# 0.754-0.968, html modunda 0.546-0.933 araliginda. Geri kalan 245 dosyanin
# EN KOTUSU (İCİNDEKİLER.doc gibi noktali/numarali icindekiler sayfalari
# dahil) txt modunda 0.100, html modunda 0.037 -- yani "en kirli" gercek
# dosya bile bozuk dosyalarin en temizinden ~5 kat uzakta. Esik 0.3, iki
# ucun ortasinda, her iki yonde de genis marj birakir (iyiye +0.20,
# kotuye +0.25).
GARBAGE_INVALID_FRACTION_THRESHOLD = 0.3


def looks_like_garbage(text):
    """textutil'in basarisiz (ama exit-0) bir donusumunu tespit eder.

    Naif "alfabetik karakter orani" testi (yalniz harf sayar) icindekiler
    sayfalarinda (nokta dizileri, sayfa numaralari) yanlis pozitif verir --
    bkz. yukaridaki esik yorumu. Bunun yerine "makul duzyazi alfabesi"
    (harf+rakam+bosluk+noktalama) DISINDA kalan karakter oranini olcer;
    icindekiler sayfalarindaki nokta/rakam bu kumenin ICINDE oldugu icin
    yanlis pozitif vermez.
    """
    if not text:
        return False
    # findall yerine sub: buyuk (10-35 MB) dosyalarda tek C-seviyeli
    # gecis, milyonlarca tek-karakterlik esleseme nesnesi biriktirmiyor.
    valid_len = len(_GARBAGE_INVALID_RE.sub("", text))
    invalid = len(text) - valid_len
    return (invalid / len(text)) > GARBAGE_INVALID_FRACTION_THRESHOLD


# --- Kurtarma alfabesi (F3) ---------------------------------------------
#
# KRITIK HATA (duzeltildi): kurtarma, `looks_like_garbage` ile AYNI
# karakter kumesini kullaniyordu. O kume tipografik noktalama icermez
# (’ ‘ “ ” – — …), dolayisiyla gercek Turkce duzyazi tam da bu
# karakterlerde IKIYE BOLUNUYOR, olusan <20 karakterlik parcalar da
# atiliyordu. Bu BICIM kaybi degil, ICERIK kaybidir: yalnizca
# `AĞ KURULUMU.doc`ta 386 atilan kosu >=6 harfli ve >=%50 alfabetikti;
# `katmanlaşma` ve `catenet` kelimeleri kurtarilan metinde HIC yoktu.
#
# Olcum (4 bozuk .doc + INTERTECH, ham UTF-16LE cozumu uzerinde): kosulari
# bolen tipografik karakterler ve sayilari -- ’ 579, ” 247, “ 243, © 68,
# ‘ 20, … 18, — 4, ÷ 2, – 2. Baglam incelemesi hepsinin gercek metinde
# oldugunu gosterdi ("TCP/IP’nin", "“firewall”", "Netware’in").
#
# `looks_like_garbage`in alfabesi BILEREK degistirilmedi: 0.3 esigi ve
# onun 5 kat marji o kume uzerinde olculmustu; genisletmek olculmemis bir
# esikle calismak olurdu. Iki islevin ihtiyaci da zaten farklidir --
# biri "bu cikti cop mu" diye bakar, digeri "bu kosu duzyazi mi".
_RECOVER_TYPOGRAPHIC = "’‘“”–—…•·°±×÷§¶©®™"
_RECOVER_RUN_RE = re.compile(
    "[" + _PLAUSIBLE_PROSE_CHARS + re.escape(_RECOVER_TYPOGRAPHIC) + "]+")

# MIN RUN AYARI (F3, kanitla): 20 KORUNDU -- dusurmek icerik degil
# GURULTU getiriyor. 5 dosyada olculdu; 20'nin altina inildiginde giren
# kosular Windows kayit defteri anahtarlari (CurrentControlSet,
# CurrentVersion, Software, Microsoft), OLE yapi adlari (WordDocument,
# ObjInfo, Ole10Native, SummaryInformation) ve alan kodu kalintisi
# (EMBED PBrush, MERGEFORMATINET) oluyor. Ornegin INTERTECH.doc 20->15
# ile +1374 "kelime" kazaniyor ama bunlarin tamami tekrar eden OLE
# meta verisi. Alfabe duzeltildikten SONRA 20 esiginde atilan kosularin
# tamami zaten alan kodu kalintisidir -- yani gercek kayip sifirdir.
_RECOVER_MIN_RUN = 20
_RECOVER_MIN_LETTER_FRACTION = 0.5

# recover_doc_text() basariyla calistiginda buraya (path, kelime_sayisi)
# eklenir; Task 8 raporu bunu listeler.
RECOVERED = []


def recover_doc_text(path):
    """Textutil'in yenildigi .doc dosyasini ham UTF-16LE taramasiyla kurtarir.

    Dosyayi textutil'e hic sokmadan doğrudan bayt duzeyinde okur, tumunu
    utf-16-le (errors='ignore') ile cozer -- bu, gercek metni OLE ikili
    yapisinin gurultusuyla serpistirilmis halde verir. "Makul duzyazi"
    koşularini (bkz. _PLAUSIBLE_PROSE_CHARS) tutup gurultu koşularini atarak
    okunakli Turkce metin uretir. Basliklar/tablolar gibi bicim bilgisi
    kurtarilamaz; yalnizca duz metin.
    """
    if not os.path.isfile(path):
        raise ExtractError("dosya yok: %s" % path)
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-16-le", "ignore")
    kept = []
    for m in _RECOVER_RUN_RE.finditer(text):
        run = m.group(0)
        if len(run) < _RECOVER_MIN_RUN:
            continue
        letters = sum(1 for c in run if c.isalpha())
        if letters < _RECOVER_MIN_LETTER_FRACTION * len(run):
            continue
        kept.append(run)
    joined = "\n\n".join(kept)
    # \s icindeki tum bosluk turlerini (satirsonu haric -- \xa0 dahil, Word
    # sik sik girinti icin NBSP kullanir) teke indir.
    joined = re.sub(r"[^\S\n\r]+", " ", joined)
    joined = re.sub(r"\r\n?|\n", "\n", joined)
    joined = re.sub(r"\n{3,}", "\n\n", joined)
    result = joined.strip()
    # F5: bos kurtarma BASARI DEGIL, HATADIR. Eskiden UTF-16LE taramasi
    # hicbir sey bulamadiginda "" donuyor ve yine de (path, 0) kaydi
    # ekleniyordu -- rapor bunu basarili bir kurtarma olarak listeliyor,
    # cagiran taraf da bos govdeyi fark etmeden yaziyordu. Artik
    # ExtractError yukselir; cagiranlar bunu zaten yakalayip
    # stats['hata']'ya kaydediyor.
    if not result:
        raise ExtractError("kurtarma bos sonuc verdi (UTF-16LE taramasi "
                           "okunabilir metin bulamadi): %s" % path)
    # F4: dosya basina TEK kayit (bkz. _log_once).
    _log_once(RECOVERED, path, len(result.split()))
    return result


def _run(cmd, timeout=120):
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise ExtractError("zaman asimi: %s" % cmd[0])
    if r.returncode != 0:
        raise ExtractError("%s basarisiz (%d): %s"
                           % (cmd[0], r.returncode, r.stderr.decode("utf8", "replace")[:200]))
    return r.stdout.decode("utf-8", "replace")


# --- Duz metin (.txt) giris kodlamasi (F7) ------------------------------
#
# textutil'in man sayfasi: "-inputencoding ... by default encoding will be
# detected from BOM". BOM'suz bir .txt'te tahmin sistem varsayilanina
# dusuyor ve arsivdeki dosyalar icin bu MAC OS TURKISH oluyor -- oysa
# dosyalar WINDOWS-1254. Bayt duzeyinde dogrulandi: 0xC7 -> '«' (dogrusu
# 'Ç'), 0xDD -> 'ı' ('İ'), 0xF6 -> 'ˆ' ('ö'), 0xFD -> '˝' ('ı');
# bunlarin tamami mac_turkish tablosuyla birebir ortusuyor.
#
# Bildirilen iki cikti (_Arsiv/Tip.md, Web-Gelistirme/CGI-Perl-Kullanimi-5.md)
# yalnizca en gorunur olanlardi: arsivdeki 11 .txt dosyasindan UTF-8
# olmayan 10'unun TAMAMI bozuk cikiyordu (yalnizca webmail.txt gecerli
# UTF-8). Bu bir kodlama TESPIT bosluğu, yani cikarim katmaninda
# duzeltilebilir bir hata.
#
# Cozum: .txt icin giris kodlamasi tahmine birakilmaz, textutil'e ACIKCA
# bildirilir. Merdiven read_htm ile ayni felsefede: BOM varsa textutil
# zaten dogru cozer; yoksa once katı UTF-8 denenir, olmuyorsa arsivin
# baskin kod sayfasi WINDOWS-1254 kullanilir.
#
# Yalnizca .txt icin uygulanir: .doc/.rtf ikili/zengin bicimlerdir,
# kodlama bilgisi dosyanin kendi yapisindadir; .htm zaten textutil'e hic
# ugramaz (read_htm saf Python ile isler).
_PLAIN_TEXT_EXTS = (".txt",)
_BOMS = (codecs.BOM_UTF8, codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)


def plain_text_input_encoding(path):
    """.txt icin textutil'e verilecek IANA kodlama adi (yoksa None)."""
    if not path.lower().endswith(_PLAIN_TEXT_EXTS):
        return None
    with open(path, "rb") as fh:
        raw = fh.read()
    if any(raw.startswith(b) for b in _BOMS):
        return None          # BOM var: textutil'in kendi tespiti dogrudur
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError:
        return "WINDOWS-1254"
    return "UTF-8"


def _textutil(path, mode):
    cmd = ["textutil", "-convert", mode, "-encoding", "UTF-8"]
    enc = plain_text_input_encoding(path)
    if enc:
        cmd += ["-inputencoding", enc]
    return _run(cmd + ["-stdout", path])


def extract_html(path):
    """.doc / .rtf / .txt -> UTF-8 HTML.

    Sonuc CP1254 mojibake'e karsi onarilir (bkz. repair_mojibake). textutil
    exit 0 donup de govde kullanilamaz OLE/ikili sizinti ise (bkz.
    looks_like_garbage) GarbageError firlatilir -- cagiran taraf bunu
    yakalayip recover_doc_text() ile devam edebilir.
    """
    if not os.path.isfile(path):
        raise ExtractError("dosya yok: %s" % path)
    html = _textutil(path, "html")
    if looks_like_garbage(html):
        raise GarbageError("textutil HTML ciktisi kullanilamaz (OLE/ikili sizinti): %s" % path)
    return _repair_if_damaged(html, path)


def extract_text(path):
    """.doc / .rtf / .txt -> düz metin. Kelime sayısı doğrulaması için.

    Sonuc CP1254 mojibake'e karsi onarilir (bkz. repair_mojibake). textutil
    exit 0 donup de govde kullanilamaz OLE/ikili sizinti ise (bkz.
    looks_like_garbage) GarbageError firlatilir -- cagiran taraf bunu
    yakalayip recover_doc_text() ile devam edebilir.
    """
    if not os.path.isfile(path):
        raise ExtractError("dosya yok: %s" % path)
    text = _textutil(path, "txt")
    if looks_like_garbage(text):
        raise GarbageError("textutil TXT ciktisi kullanilamaz (OLE/ikili sizinti): %s" % path)
    return _repair_if_damaged(text, path)


def read_htm(path, encodings=None):
    """.htm / .html -> UTF-8 HTML. Kodlamayı meta etiketinden veya deneyerek bulur.

    Bildirilen (declared) kodlama başarısız olursa sıradaki adaylar denenir;
    hiçbiri "strict" çözülemezse son çare olarak windows-1254 + errors="replace"
    kullanılır (bu, çıktıya U+FFFD sızdırabilir). Beklenenden (bildirilen ya
    da ilk aday) farklı bir kodlama kullanıldığında -- son çare dahil --
    modül düzeyindeki FALLBACK_LOG'a bir kayıt eklenir; böylece "sessiz"
    bir yedek kodlama seçimi görünür kalır. Dönüş sözleşmesi değişmedi:
    hâlâ `str` döner.

    `encodings`: test/ileri-seviye kullanım için aday listesini geçici
    olarak değiştirir; verilmezse modül düzeyindeki HTM_ENCODINGS kullanılır.
    """
    if not os.path.isfile(path):
        raise ExtractError("dosya yok: %s" % path)
    with open(path, "rb") as fh:
        raw = fh.read()
    order = list(encodings) if encodings is not None else list(HTM_ENCODINGS)
    m = re.search(rb'charset\s*=\s*["\']?\s*([A-Za-z0-9_-]+)', raw[:4000], re.I)
    declared = None
    if m:
        declared = m.group(1).decode("ascii", "ignore").lower()
        if declared in order:
            order.remove(declared)
        order.insert(0, declared)
    expected = order[0] if order else None
    for enc in order:
        try:
            text = raw.decode(enc)
        except (UnicodeDecodeError, LookupError):
            continue
        if enc != expected:
            FALLBACK_LOG.append({
                "path": path,
                "declared": declared,
                "used": enc,
                "lossy": False,
            })
        return _repair_if_damaged(text, path)
    FALLBACK_LOG.append({
        "path": path,
        "declared": declared,
        "used": "windows-1254(replace)",
        "lossy": True,
    })
    return _repair_if_damaged(raw.decode("windows-1254", "replace"), path)


def extract_pdf_text(path):
    """.pdf -> düz metin (PDFKit).

    Sonuc, diger cikarim yollari gibi CP1254 mojibake'ine karsi onarilir.
    ONCEDEN ONARILMIYORDU ve bu gercek bir kayipti: PDF gomulu metni de
    2001-2004'te ayni yanlis kod sayfasiyla yazilmis olabiliyor. verify.py
    kontrol 2 bu bosluğu olcerek buldu -- iki PDF ciktisi 4.155 bozuk
    karakter tasiyordu (PHOTOSHOP/photoshop.pdf'te 3.431, ornegin "ayarlarý"
    = "ayarları"; ayrica "DOÐRU" = "DOĞRU" gibi tek tuk ornekler).
    Ayni esik (MOJIBAKE_THRESHOLD) burada da gecerlidir: esigin altindaki
    izole isaretler kaynak metnin parcasi sayilir ve DOKUNULMAZ.
    """
    if not os.path.isfile(path):
        raise ExtractError("dosya yok: %s" % path)
    return _repair_if_damaged(_run(["swift", PDF_SWIFT, path], timeout=300),
                              path)


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

    macOS/textutil bazen NFD (ayrışık) Unicode üretir; çağıranlara kararlı
    bir biçim vermek için sonuçlar NFC'ye normalize edilir.
    """
    out = {"author": None, "title": None, "year": None}
    m = _META_RE["author"].search(html)
    if m and m.group(1).strip():
        out["author"] = unicodedata.normalize("NFC", m.group(1).replace("_", " ").strip())
    m = _META_RE["title"].search(html)
    if m and m.group(1).strip():
        out["title"] = unicodedata.normalize("NFC", re.sub(r"\s+", " ", m.group(1)).strip())
    m = _META_RE["created"].search(html)
    if m:
        out["year"] = m.group(1)
    return out
