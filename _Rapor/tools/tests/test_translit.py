import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from translit import (to_ascii, slugify, safe_name, slug_from_folder,
                      title_from_folder)


class TestToAscii(unittest.TestCase):
    def test_lowercase_turkish(self):
        self.assertEqual(to_ascii("çğıöşü"), "cgiosu")

    def test_uppercase_turkish(self):
        self.assertEqual(to_ascii("ÇĞİÖŞÜ"), "CGIOSU")

    def test_dotless_i_and_dotted_I(self):
        self.assertEqual(to_ascii("İŞLETİM ıslak"), "ISLETIM islak")

    def test_leaves_ascii_untouched(self):
        self.assertEqual(to_ascii("Hello World 123"), "Hello World 123")

    def test_nfd_decomposed_input(self):
        # macOS dosya sistemi Turkce karakterleri NFD (ayrisik) bicimde
        # dondurur: "I" + COMBINING DOT ABOVE gibi. Gercek arsiv klasor
        # adlarinda bu bicim gorulur; to_ascii bunu da dogru cevirmelidir.
        import unicodedata
        decomposed = unicodedata.normalize("NFD", "İSTANBUL ÖĞRENCİ")
        self.assertEqual(to_ascii(decomposed), "ISTANBUL OGRENCI")


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

    def test_nfd_decomposed_folder_name(self):
        # Gercek arsiv klasor adlari macOS'ta NFD ayrisik Unicode olarak
        # gelir (os.listdir cikisi). slugify bunu da dogru islemelidir.
        import unicodedata
        decomposed = unicodedata.normalize("NFD", "3D MİNİ SÖZLÜK")
        self.assertEqual(slugify(decomposed), "3D-Mini-Sozluk")


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

    def test_nfd_decomposed_input_titlecased(self):
        # Gercek klasor adlari NFD gelir; buyuk harfli Turkce karakter
        # iceren kelimeler de dogru sekilde kucultulup baslik yapilmali.
        import unicodedata
        decomposed = unicodedata.normalize("NFD", "AĞ TEKNOLOJİSİ")
        self.assertEqual(title_from_folder(decomposed), "Ağ Teknolojisi")

    # -- F6: adı dosya uzantısıyla biten konu KLASÖRLERİ -------------
    #    Arşivde üçü var; H1'de uzantı görünmemeli. Uzantı sözcük
    #    düzeltmesinden önce atılmazsa "TABANI.doc" hiç düzeltilmeden
    #    kalıyordu ("# Access Veri TABANI.doc").
    def test_strips_trailing_doc_extension_and_titlecases(self):
        self.assertEqual(title_from_folder("ACCESS VERİ TABANI.doc"),
                         "Access Veri Tabani")

    def test_strips_trailing_extension_second_real_case(self):
        self.assertEqual(
            title_from_folder("BİLGİSAYAR AĞLARINDA TEMEL KAVRAMLAR.doc"),
            "Bilgisayar Ağlarinda Temel Kavramlar")

    def test_strips_trailing_pdf_extension(self):
        self.assertEqual(title_from_folder("quickbasickursu.pdf"),
                         "Quickbasickursu")

    # ASP.NET gerçek bir konu klasörüdür ve "NET" sondaki kısa nokta
    # ekine benzer -- genel bir kural bunu yanlışlıkla keserdi.
    def test_does_not_strip_non_extension_suffix(self):
        self.assertEqual(title_from_folder("ASP.NET"), "ASP.NET")

    def test_does_not_strip_dot_in_middle(self):
        self.assertEqual(title_from_folder("Asp'ye giris.Asp nedir"),
                         "Asp'ye giris.Asp Nedir")


class TestSlugFromFolder(unittest.TestCase):
    """Konu klasörü adındaki dosya uzantısı DOSYA ADINDAN da atılmalı.

    Uzantı yalnızca H1'den atıldığı sürece çıktı adları
    `Quickbasickursu-Pdf.md` gibi kalıyordu (üç konu klasörü).
    """

    def test_strips_trailing_doc_extension(self):
        self.assertEqual(slug_from_folder("ACCESS VERİ TABANI.doc"),
                         "Access-Veri-Tabani")
        self.assertEqual(
            slug_from_folder("BİLGİSAYAR AĞLARINDA TEMEL KAVRAMLAR.doc"),
            "Bilgisayar-Aglarinda-Temel-Kavramlar")

    def test_strips_trailing_pdf_extension(self):
        self.assertEqual(slug_from_folder("quickbasickursu.pdf"),
                         "Quickbasickursu")

    def test_does_not_strip_non_extension_suffix(self):
        self.assertEqual(slug_from_folder("ASP.NET"), slugify("ASP.NET"))

    def test_matches_slugify_when_no_extension(self):
        for name in ("AĞ KURULUMU", "C++ DERS NOTLARI", "ASP.NET",
                     "Asp'ye giris.Asp nedir"):
            self.assertEqual(slug_from_folder(name), slugify(name))

    def test_slugify_itself_unchanged(self):
        """slugify GENEL amaçlıdır; gerçek dosya adlarında uzantı kalmalı."""
        self.assertEqual(slugify("quickbasickursu.pdf"), "Quickbasickursu-Pdf")


if __name__ == "__main__":
    unittest.main()
