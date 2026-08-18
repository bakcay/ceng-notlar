"""Konu klasörü adından kategori belirler.

Sıra önemlidir: RULES listesinde önce gelen kural kazanır. Güvenlik ve
veritabanı kuralları, ağ/programlama kurallarından ÖNCE gelir çünkü
"TCP IP ve FIREWAL" veya "SQL PROGRAMLAMA" gibi başlıklar iki kategoriye
birden anahtar kelime taşır (spec §6, sınırda kalan konular).
"""
import unicodedata

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
        "ANAHTARLI BILGI",
    ]),
    ("Yapay-Zeka", ["YAPAY ZEKA", "YAPAY SINIR", "UZMAN SISTEM", "PROLOG"]),
    ("Veritabani", [
        "VERI TABANI", "VERITABANI", "SQL", "ACCESS", "ORACLE", "DBASE",
        "VTYS", "INFORMIX", "MDB",
    ]),
    ("Elektronik", [
        "AC DC", "CONVENTER", "FILTRE", "FIR ", "PIC ", "PLC", "MEKATRONIK",
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
        "INTERNET SITESI", "OPEN GL", "SUNUCUSU",
    ]),
    ("Isletim-Sistemleri", [
        " DOS ", "WINDOW", "LINUX", "UNIX", "MINIX", "ISLETIM SISTEM",
        "DENETIM MASASI", "KULLANICI PROFIL", "DISK VE DOSYA KOMUT",
        "APPEND", "FDISK",
    ]),
    ("Ag-ve-Iletisim", [
        "AG ", " AG", "NETWORK", "OSI", "TCP", "IP ADRES", "DNS",
        "ETHERNET", "WAN", "ISDN", "DSL", "ROUTER", "KABLOSUZ",
        "MODEM", "ANSI", "ASCII", "INTERNET", "INTRANET", "EXTRANET",
        "CEVIRMELI", "ILETISIM",
    ]),
    ("Donanim", [
        "ANAKART", "CPU", "ISLEMCI", "BELLEK", "SES KART", "CEVRE BIRIM",
        "BIOS", "RAID", "VERSATILE DISC", "DONANIM", " ISA ", "PC SORUN",
        "MOUSE", "SCANNER", "MIKROISLEMCI",
    ]),
    ("Programlama", [
        "ALGORITMA", "PASCAL", "DELPHI", "VISUAL BASIC", "VISUAL BASIC",
        "ASSEMBLER", "PROGRAMLAMA", "PROGRAM", "VERI YAPILARI", "JAVA",
        "CPP", "C DERS", "C NOTLARI", "CSHARP", "C KODLAMA", "BASIC",
        "DIZI", "LIST BOX", "TOOLBOX", "DONGU", "YAZILIM", "FONKSIYON",
        "KODLAMA", "QUICKBASIC", "MOBIL UYGULAMA", "HEDEF PROGRAM",
        "TEMEL KAVRAMLAR VE C ", "PROGRAMMING IN PASCAL",
    ]),
    ("Bilisim-ve-E-Ticaret", [
        "TICARET", "BILISIM DUNYA", "TEKNOKENT", "INTERTECH", "ISO 9001",
        "BILL GATES", "MIS", "INFORMATION", "EGITIM",
    ]),
]

# Kural tablosunun yanildigi klasorler. Klasor adi birebir yazilir (NFC).
# "_Arsiv" 13 kategorinin disindadir: arsiv konusu OLMAYAN (bilgisayar
# notlariyla ilgisiz) klasorler icin kullanilir; bu klasorler Sozluk-ve-
# Referans cop kutusune de dusmemelidir, cunku orada gercek "bilinmeyen
# konu" klasorleriyle karisirlar.
OVERRIDES = {
    "OPEN GL": "Programlama",
    "A+ KURS NOTLARI": "Donanim",
    "WEB - TABANLI ÖĞRETİM": "Bilisim-ve-E-Ticaret",
    "UZAKTAN EĞİTİM TERİMLER SÖZLÜĞÜ": "Sozluk-ve-Referans",
    "3D MİNİ SÖZLÜK": "Sozluk-ve-Referans",
    "TIP": "_Arsiv",
    # Icerigi (Server Manager, User Manager, NT Explorer, "domain'ler
    # arasi guven iliskisi") Windows NT alan (domain) yonetimi anlatiyor;
    # klasor adindaki "DOMAIN" kelimesi tek basina RULES'u yaniltip
    # Web-Gelistirme'ye dusurur. Bkz. dosya icerigi (textutil ile okundu).
    "BİRDEN ÇOK DOMAİN İLE ÇALIŞMA": "Isletim-Sistemleri",
    # Klasor adi "icerik kodlari" web icerigini cagristirir ama ictindeki
    # 5 .doc dosyasi Visual Basic kod ornekleridir (Command1_Click,
    # TextBox, PictureBox, sürükle-bırak...). Bkz. dosya icerigi.
    "BAZI İÇERİK KODLARI": "Programlama",
    # Klasor adi genel/belirsiz ("bir text dosyasi olusturmak") ama
    # icerigi ASP/Scripting.FileSystemObject nasil-yapilir dersidir
    # ("Set dosya_nesnesi = CreateObject(...)"). Bkz. dosya icerigi
    # (textutil ile okundu). Adinda hicbir Web-Gelistirme anahtar
    # kelimesi gecmedigi icin RULES bunu asla yakalayamaz; guvenli bir
    # RULES anahtar kelimesi yok (baska hicbir klasor adinda "TEXT
    # DOSYASI" ASP/web anlamina gelmez), bu yuzden override sarttir.
    "BİR TEXT DOSYASI OLUŞTURMAK": "Web-Gelistirme",
}

# OVERRIDES anahtarlari Python kaynak kodunda NFC olarak yazilir; ancak
# macOS dosya sistemi klasor adlarini NFD (ayrisik) dondurur (ornegin
# "İ" -> "I" + COMBINING DOT ABOVE). Naif "folder_name in OVERRIDES"
# karsilastirmasi bu yuzden gercek arsiv girdisinde HER ZAMAN basarisiz
# olur. Anahtarlari da NFC'ye normalize ederek arama yapariz.
_OVERRIDES_NORM = {
    unicodedata.normalize("NFC", k): v for k, v in OVERRIDES.items()
}


def _norm(name):
    s = to_ascii(name).upper()
    # "C++" / "C#" once ozel isaretlerle degil, RULES'daki "CPP" / "CSHARP"
    # anahtar kelimeleriyle dogrudan eslesecek sekilde donusturulur. Genel
    # '+' -> bosluk donusumu tek basina yeterli degildir: "C++ DERS
    # NOTLARI" -> "C   DERS NOTLARI" -> sikistirilince "C DERS NOTLARI"
    # olur ve bu calisir, ama "C++ VERİ TİPLERİ" gibi "DERS"siz basliklarda
    # hicbir kelimeyle eslesmez ve sessizce Sozluk-ve-Referans'a duser.
    s = s.replace("C++", "CPP").replace("C#", "CSHARP")
    # Kalan '+' ve '-' karakterleri kelime ayraci gibi davranir (ör. "A+
    # KURS", "MS-DOS", "AC-DC"): bosluga cevrilip fazla bosluklar
    # sikistirilir. Boylece " DOS " gibi sinir-korumali anahtar kelimeler
    # "MS-DOS" icinde de "DOSYA" icinde OLMADIGI gibi dogru calisir.
    s = s.replace("+", " ").replace("-", " ")
    s = " ".join(s.split())
    return " " + s + " "


def categorize(folder_name):
    key = unicodedata.normalize("NFC", folder_name)
    if key in _OVERRIDES_NORM:
        return _OVERRIDES_NORM[key]
    hay = _norm(folder_name)
    for category, keywords in RULES:
        for kw in keywords:
            if kw in hay:
                return category
    return FALLBACK
