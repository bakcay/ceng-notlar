"""Her kaynak dosyanın çıktıdaki rolünü belirler.

belge  -> Markdown'a çevrilir
ornek  -> ornekler/ altına orijinal haliyle kopyalanır
gorsel -> gorseller/ altına kopyalanır
arsiv  -> _Arsiv/ altına kopyalanır
atla   -> hiç kopyalanmaz (.DS_Store gibi sistem dosyaları)
"""
import os
import unicodedata

BELGE_EXT = {"doc", "rtf", "txt", "pdf", "htm", "html"}
ORNEK_EXT = {"php", "asp", "pl", "js", "java", "inc", "cgi", "x", "lib",
             "dump", "get", "sql", "css", "bat", "c", "cpp", "pas", "vbs"}
GORSEL_EXT = {"gif", "jpg", "jpeg", "png", "bmp"}
ARSIV_EXT = {"chm", "rar", "zip", "mdb", "lit", "swf", "exe", "dll"}
ATLA = {".DS_Store", "Thumbs.db", "desktop.ini"}

# Kitap + calisan kod paketi olan konu klasorleri (spec §8).
# NOT: bu literaller NFC (Python kaynak dosyasi normal formu). macOS
# APFS/HFS+ os.walk/os.listdir klasor adlarini NFD (ayrisik) dondurur;
# Turkce harfli 3 klasor (JAVA SCRİPT - DEVAMI, WEB DERSLERİ - HTML,
# ASP BOOK ÖRNEKLER) bu yuzden gercek arsivden okunan adla dogrudan '=='
# ya da 'in BUNDLE_FOLDERS' karsilastirmasinda ESLESMEZ (trap #1, bkz.
# gorev notlari). Gercek bir klasor adiyla uyelik kontrolu icin
# is_bundle_folder() kullanilmali; BUNDLE_FOLDERS'in kendisi -- test
# tarafindan tam esitlik ile dogrulandigi icin -- NFC literal olarak
# birakildi.
BUNDLE_FOLDERS = {
    "PHP - DEVAM",
    "JAVA SCRİPT - DEVAMI",
    "WEB DERSLERİ - HTML",
    "ASP BOOK ÖRNEKLER",
    "CGI-PERL KULLANIMI",
}


def is_bundle_folder(name):
    """`name` (gercek dosya sisteminden, NFD olabilir) BUNDLE_FOLDERS'ta mi?

    Karsilastirmadan once NFC'ye normalize eder; boylece macOS'un NFD
    donen klasor adlari BUNDLE_FOLDERS'taki NFC literallerle dogru
    eslesir. `role()`'a `bundle=` degerini hesaplarken bunu kullanin.
    """
    return unicodedata.normalize("NFC", name) in BUNDLE_FOLDERS


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
