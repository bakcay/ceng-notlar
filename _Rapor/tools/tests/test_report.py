"""report.py — INDEX ve rapor uretimi (Task 8)."""
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import report
from report import body_words, need, read_md, split_md


FOOTER = "---\n*Kaynak: `A/B.doc`*"


class TestSplitMd(unittest.TestCase):
    def test_h1_and_footer_excluded_from_body(self):
        t = "# Baslik\n\nbir iki uc\n\n" + FOOTER + "\n"
        title, lines = split_md(t)
        self.assertEqual(title, "Baslik")
        self.assertEqual(" ".join(lines).split(), ["bir", "iki", "uc"])
        self.assertEqual(body_words(t), 3)

    def test_multiple_footer_lines_excluded(self):
        t = ("# B\n\nbir iki\n\n---\n*Kaynak: `x`*\n"
             "*Örnekler: `y/ornekler/` (3 dosya)*\n")
        self.assertEqual(body_words(t), 2)

    def test_file_without_footer_keeps_whole_body(self):
        t = "# B\n\nbir iki uc dort\n"
        self.assertEqual(body_words(t), 4)

    def test_body_ending_in_horizontal_rule_is_not_eaten(self):
        """Govdenin son satiri '---' ise dipnot yokmus gibi davranilmali.

        Yatay cizgi govdede kalir (kelime olarak sayilir); onemli olan
        ondan ONCEKI gercek metnin kirpilmamasi.
        """
        _, lines = split_md("# B\n\nbir iki\n\n---\n")
        self.assertIn("bir iki", lines)

    def test_bold_line_before_footer_survives(self):
        t = "# B\n\n**onemli nokta**\n\n" + FOOTER + "\n"
        self.assertEqual(body_words(t), 2)

    def test_missing_h1_returns_empty_title(self):
        title, _ = split_md("duz metin\n")
        self.assertEqual(title, "")

    def test_empty_file(self):
        self.assertEqual(body_words(""), 0)


class TestNeed(unittest.TestCase):
    def test_missing_key_raises_with_available_keys(self):
        with self.assertRaises(KeyError) as cm:
            need({"belge": 1}, "mojibake_onarilan")
        self.assertIn("mojibake_onarilan", str(cm.exception))
        self.assertIn("belge", str(cm.exception))

    def test_present_key_returned_even_when_falsy(self):
        self.assertEqual(need({"hata": []}, "hata"), [])


def _stats(**over):
    s = {"belge": 2, "yonlendirme": 0, "dizin": 0, "ornek": 0, "gorsel": 0,
         "arsiv": 0, "hata": [], "kisa": [], "yeniden_adlandirilan": [],
         "cakisma": [], "kurtarma": [], "bos": [], "silinen": [],
         "mojibake_onarilan": [], "utf16_kurtarilan": [], "kodlama_yedegi": []}
    s.update(over)
    return s


class ReportBase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.out = os.path.join(self.tmp, "MD")
        self.rapor = os.path.join(self.out, "_Rapor")
        os.makedirs(self.rapor)
        self._orig = (report.ROOT, report.OUT, report.RAPOR)
        report.ROOT, report.OUT, report.RAPOR = self.tmp, self.out, self.rapor

    def tearDown(self):
        report.ROOT, report.OUT, report.RAPOR = self._orig
        shutil.rmtree(self.tmp, ignore_errors=True)

    def doc(self, rel, title, body):
        p = os.path.join(self.out, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("# %s\n\n%s\n\n%s\n" % (title, body, FOOTER))
        return p

    def write_stats(self, **over):
        with open(os.path.join(self.rapor, "stats.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(_stats(**over), fh)

    def write_dups(self, binary=(), text=()):
        with open(os.path.join(self.rapor, "dups.json"), "w",
                  encoding="utf-8") as fh:
            json.dump({"binary": list(binary), "text": list(text)}, fh)


class TestWriteIndex(ReportBase):
    def test_lists_categories_and_titles_and_body_word_counts(self):
        self.doc("Donanim/Anakart.md", "Anakartlar", "bir iki uc")
        self.doc("Guvenlik/Virus.md", "Virüsler", "dort bes")
        idx = report.write_index(self.out)
        t = read_md(idx)
        self.assertIn("## Donanim (1)", t)
        self.assertIn("[Anakartlar](Donanim/Anakart.md) — 3 kelime", t)
        self.assertIn("[Virüsler](Guvenlik/Virus.md) — 2 kelime", t)
        self.assertIn("**Toplam 2 belge, 2 kategori.**", t)

    def test_arsiv_root_documents_are_listed_not_orphaned(self):
        """_Arsiv bir kategori adi olarak da kullaniliyor (ornek: TIP)."""
        self.doc("Donanim/A.md", "A", "bir")
        self.doc("_Arsiv/Tip.md", "Tip", "iki uc")
        idx = report.write_index(self.out)
        t = read_md(idx)
        self.assertIn("[Tip](_Arsiv/Tip.md)", t)
        self.assertIn("**Toplam 2 belge", t)

    def test_arsiv_readme_is_not_listed_as_a_document(self):
        self.doc("Donanim/A.md", "A", "bir")
        os.makedirs(os.path.join(self.out, "_Arsiv"))
        with open(os.path.join(self.out, "_Arsiv", "README.md"), "w") as fh:
            fh.write("# Arsiv\n")
        t = read_md(report.write_index(self.out))
        self.assertNotIn("_Arsiv/README.md) —", t)
        self.assertIn("[_Arsiv/](_Arsiv/README.md)", t)

    def test_empty_category_directory_is_skipped(self):
        self.doc("Donanim/A.md", "A", "bir")
        os.makedirs(os.path.join(self.out, "Bos"))
        t = read_md(report.write_index(self.out))
        self.assertNotIn("## Bos", t)


class TestConversionReport(ReportBase):
    def test_missing_stats_key_fails_loudly(self):
        s = _stats()
        del s["mojibake_onarilan"]
        with open(os.path.join(self.rapor, "stats.json"), "w") as fh:
            json.dump(s, fh)
        with self.assertRaises(KeyError):
            report.write_conversion_report(self.out, self.rapor)

    def test_mojibake_repairs_are_surfaced(self):
        self.write_stats(mojibake_onarilan=[
            [os.path.join(self.tmp, "A/EXCEL.doc"), 7547]])
        t = read_md(report.write_conversion_report(self.out, self.rapor))
        self.assertIn("**1 dosya kaynakta bozuktu**", t)
        self.assertIn("A/EXCEL.doc", t)
        self.assertIn("7547 harf onarıldı", t)

    def test_utf16_recovery_is_surfaced_with_format_loss_warning(self):
        self.write_stats(utf16_kurtarilan=[
            [os.path.join(self.tmp, "A/AG.doc"), 15589]])
        t = read_md(report.write_conversion_report(self.out, self.rapor))
        self.assertIn("A/AG.doc", t)
        self.assertIn("15589 kelime kurtarıldı", t)
        self.assertIn("biçim kaybı vardır", t)

    def test_encoding_fallback_table_and_lossy_warning(self):
        self.write_stats(kodlama_yedegi=[
            {"path": os.path.join(self.tmp, "A/a.htm"),
             "declared": "windows-1254", "used": "iso-8859-9", "lossy": False},
            {"path": os.path.join(self.tmp, "A/b.htm"), "declared": None,
             "used": "windows-1254(replace)", "lossy": True}])
        t = read_md(report.write_conversion_report(self.out, self.rapor))
        self.assertIn("| `A/a.htm` | windows-1254 | iso-8859-9 |", t)
        self.assertIn("bozuk karakter kalmış", t)
        self.assertIn("**1 sayfada hiçbir kodlama tam çözmedi**", t)

    def test_no_lossy_pages_says_so_explicitly(self):
        self.write_stats(kodlama_yedegi=[
            {"path": os.path.join(self.tmp, "A/a.htm"), "declared": None,
             "used": "iso-8859-9", "lossy": False}])
        t = read_md(report.write_conversion_report(self.out, self.rapor))
        self.assertIn("Hiçbirinde karakter kaybı olmadı", t)

    def test_empty_lists_produce_reassuring_text_not_missing_sections(self):
        self.write_stats()
        t = read_md(report.write_conversion_report(self.out, self.rapor))
        self.assertIn("Yok. Arşivdeki her belge okunabildi.", t)
        self.assertIn("Onarım gerektiren dosya çıkmadı.", t)

    def test_swept_stale_files_are_reported(self):
        self.write_stats(silinen=["Donanim/Eski-Ad.md"])
        t = read_md(report.write_conversion_report(self.out, self.rapor))
        self.assertIn("Donanim/Eski-Ad.md", t)


class TestDupReport(ReportBase):
    def test_both_kinds_reported(self):
        a = os.path.join(self.tmp, "A/x.doc")
        b = os.path.join(self.tmp, "B/x.doc")
        self.write_dups(binary=[[a, b]], text=[[a, b]])
        t = read_md(report.write_dup_report(self.out, self.rapor))
        self.assertIn("Birebir aynı dosyalar (1 grup)", t)
        self.assertIn("Aynı metin, farklı dosya (1 grup)", t)
        self.assertIn("aynısı, çevrilmedi: `B/x.doc`", t)
        self.assertIn("yönlendirildi: `B/x.doc`", t)

    def test_no_duplicates(self):
        self.write_dups()
        t = read_md(report.write_dup_report(self.out, self.rapor))
        self.assertIn("Birebir aynı dosyalar (0 grup)", t)


class TestArchiveReadme(ReportBase):
    def _arsiv(self, rel, body=b"x" * 2048):
        p = os.path.join(self.out, "_Arsiv", rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(body)
        return p

    def test_formats_are_explained_in_plain_turkish(self):
        self._arsiv("Web-Gelistirme/html2000.chm")
        t = read_md(report.write_archive_readme(self.out))
        self.assertIn("`html2000.chm` — 2 KB.", t)
        self.assertIn("CHM okuyucu", t)

    def test_markdown_documents_listed_separately_not_as_binaries(self):
        self.doc("_Arsiv/Tip.md", "Tip", "bir iki")
        self._arsiv("Diger/Dracula.lit")
        t = read_md(report.write_archive_readme(self.out))
        self.assertIn("[Tip](Tip.md)", t)
        self.assertNotIn("`Tip.md` —", t)

    def test_readme_itself_not_listed(self):
        self._arsiv("Diger/a.lit")
        report.write_archive_readme(self.out)
        t = read_md(report.write_archive_readme(self.out))
        self.assertNotIn("`README.md`", t)

    def test_returns_none_without_arsiv_dir(self):
        self.assertIsNone(report.write_archive_readme(self.out))

    def test_unknown_extension_still_listed(self):
        self._arsiv("Diger/veri.xyz")
        t = read_md(report.write_archive_readme(self.out))
        self.assertIn("`veri.xyz`", t)


if __name__ == "__main__":
    unittest.main()
