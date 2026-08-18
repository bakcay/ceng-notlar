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
