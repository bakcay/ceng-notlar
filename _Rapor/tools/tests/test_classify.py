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
