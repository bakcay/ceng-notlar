"""verify.py — cikti dogrulama kontrolleri (Task 9).

Kontroller gercek arsivi tarar; testler modul sabitlerini gecici bir
dizine yonlendirerek her kontrolu izole olarak surer.
"""
import json
import os
import shutil
import sys
import tempfile
import unicodedata
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import report
import verify
from extract import MOJIBAKE_THRESHOLD

FOOT = "---\n*Kaynak: `%s`*"


class TestStripFieldCodes(unittest.TestCase):
    def test_hyperlink_removed_but_following_prose_kept(self):
        t = 'HYPERLINK "http://x" \\l "a3" BİRDEN ÇOK ALANA GÖRE'
        self.assertEqual(verify.strip_field_codes(t).split(),
                         ["BİRDEN", "ÇOK", "ALANA", "GÖRE"])

    def test_embed_removed(self):
        self.assertEqual(
            verify.strip_field_codes("EMBED Equation.3  1.797").split(),
            ["1.797"])

    def test_real_words_containing_keywords_untouched(self):
        for t in ("CREATE SEQUENCE pers_id", "SERVER_PROTOCOL", "'STOCK FORM'"):
            self.assertEqual(verify.strip_field_codes(t), t)

    def test_baseline_shrinks_so_comparison_is_apples_to_apples(self):
        raw = 'PAGEREF _Toc1 \\h 3 gerçek metin'
        self.assertLess(len(verify.strip_field_codes(raw).split()),
                        len(raw.split()))


class TestSourceOf(unittest.TestCase):
    def test_reads_footnote_path(self):
        p = verify.source_of("# B\n\ngovde\n\n" + FOOT % "A/B.doc")
        self.assertEqual(p, os.path.join(verify.ROOT, "A/B.doc"))

    def test_no_footnote_returns_none(self):
        self.assertIsNone(verify.source_of("# B\n\nyonlendirme govdesi\n"))


class VerifyBase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.out = os.path.join(self.tmp, "MD")
        self.rapor = os.path.join(self.out, "_Rapor")
        os.makedirs(self.rapor)
        self._v = (verify.ROOT, verify.OUT, verify.RAPOR)
        self._r = (report.ROOT, report.OUT, report.RAPOR)
        verify.ROOT, verify.OUT, verify.RAPOR = self.tmp, self.out, self.rapor
        report.ROOT, report.OUT, report.RAPOR = self.tmp, self.out, self.rapor

    def tearDown(self):
        verify.ROOT, verify.OUT, verify.RAPOR = self._v
        report.ROOT, report.OUT, report.RAPOR = self._r
        shutil.rmtree(self.tmp, ignore_errors=True)

    def md(self, rel, body, src=None):
        p = os.path.join(self.out, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        foot = ("\n\n" + FOOT % src) if src else ""
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("# Baslik\n\n%s%s\n" % (body, foot))
        return p

    def stats(self, **over):
        s = {"belge": 0, "yonlendirme": 0, "dizin": 0, "ornek": 0, "gorsel": 0,
             "arsiv": 0, "hata": [], "kisa": [], "cakisma": [],
             "yonlendirme_yollari": [], "dizin_yollari": []}
        s.update(over)
        return s


class TestMdPaths(VerifyBase):
    def test_rapor_is_skipped_entirely(self):
        keep = self.md("Donanim/A.md", "govde")
        with open(os.path.join(self.rapor, "00-tasarim.md"), "w") as fh:
            fh.write("# tasarim\n")
        os.makedirs(os.path.join(self.rapor, "tools"))
        with open(os.path.join(self.rapor, "tools", "not.md"), "w") as fh:
            fh.write("# not\n")
        self.assertEqual(list(verify.md_paths()), [keep])


class TestMojibake(VerifyBase):
    def test_systemic_cp1254_damage_fails(self):
        self.md("Donanim/A.md", "ayarlarý " * (MOJIBAKE_THRESHOLD + 5))
        r = verify.check_no_mojibake()
        self.assertFalse(r["ok"])
        self.assertIn("Donanim/A.md", r["detail"][0][0])

    def test_utf8_mojibake_sequence_fails(self):
        self.md("Donanim/A.md", "Ã¼ " * (MOJIBAKE_THRESHOLD + 5))
        self.assertFalse(verify.check_no_mojibake()["ok"])

    def test_isolated_markers_reported_as_note_not_failure(self):
        self.md("Donanim/A.md", "listenin baþý gösterir")
        r = verify.check_no_mojibake()
        self.assertTrue(r["ok"])
        self.assertEqual(len(r["notes"]), 1)
        self.assertIn("Donanim/A.md", r["notes"][0][1][0][0])

    def test_clean_turkish_passes_with_no_notes(self):
        self.md("Donanim/A.md", "Türkçe şığöüç İĞŞÖÇÜ metin")
        r = verify.check_no_mojibake()
        self.assertTrue(r["ok"])
        self.assertEqual(r["notes"], [])

    def test_bare_A_tilde_or_A_umlaut_is_not_flagged(self):
        """Tek karakterli imza kullanilsaydi Almanca/Portekizce yanardi."""
        self.md("Donanim/A.md", "São Paulo Ärger Ä Ã")
        self.assertTrue(verify.check_no_mojibake()["ok"])


class TestPathCharset(VerifyBase):
    def test_underscore_prefixed_arsiv_is_valid(self):
        self.md("_Arsiv/Tip.md", "govde")
        self.assertTrue(verify.check_path_charset()["ok"])

    def test_turkish_or_space_in_path_fails(self):
        self.md("Donanim/Bir Şey.md", "govde")
        r = verify.check_path_charset()
        self.assertFalse(r["ok"])

    def test_rapor_contents_not_checked(self):
        os.makedirs(os.path.join(self.rapor, "tools", "__pycache__"))
        with open(os.path.join(self.rapor, "kategori dağılımı.txt"), "w") as fh:
            fh.write("x")
        self.assertTrue(verify.check_path_charset()["ok"])


class TestLinks(VerifyBase):
    def test_broken_link_in_generated_index_fails(self):
        with open(os.path.join(self.out, "INDEX.md"), "w",
                  encoding="utf-8") as fh:
            fh.write("# I\n\n- [A](Donanim/Yok.md)\n")
        r = verify.check_links(self.stats())
        self.assertFalse(r["ok"])

    def test_broken_link_inherited_from_source_is_a_note(self):
        self.md("Donanim/A.md", "[Applet](capplet1.htm)", src="A/B.htm")
        r = verify.check_links(self.stats())
        self.assertTrue(r["ok"])
        self.assertEqual(r["notes"][0][1], [("Donanim/A.md", "capplet1.htm")])

    def test_broken_link_in_redirect_file_fails(self):
        p = self.md("Donanim/A.md", "[asil](Yok.md)")
        r = verify.check_links(self.stats(yonlendirme_yollari=[p]))
        self.assertFalse(r["ok"])

    def test_external_and_anchor_links_ignored(self):
        self.md("Donanim/A.md", "[x](http://a) [y](https://b) [z](mailto:a@b)",
                src="A/B.htm")
        r = verify.check_links(self.stats())
        self.assertTrue(r["ok"])
        self.assertEqual(r["notes"], [])

    def test_missing_asset_folder_fails_even_in_a_converted_document(self):
        p = os.path.join(self.out, "Donanim", "A.md")
        os.makedirs(os.path.dirname(p))
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("# B\n\ngovde\n\n---\n*Kaynak: `A/B.doc`*\n"
                     "*Örnekler: `A/ornekler/` (2 dosya)*\n")
        r = verify.check_links(self.stats())
        self.assertFalse(r["ok"])
        self.assertIn("ek klasoru yok", r["detail"][0][1])

    def test_asset_folder_file_count_must_match(self):
        d = os.path.join(self.out, "Donanim", "A", "ornekler")
        os.makedirs(d)
        with open(os.path.join(d, "a.php"), "w") as fh:
            fh.write("x")
        p = os.path.join(self.out, "Donanim", "A.md")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("# B\n\ngovde\n\n---\n*Kaynak: `A/B.doc`*\n"
                     "*Örnekler: `A/ornekler/` (2 dosya)*\n")
        r = verify.check_links(self.stats())
        self.assertFalse(r["ok"])
        self.assertIn("tutmuyor", r["detail"][0][1])


class TestNotEmpty(VerifyBase):
    def test_near_empty_body_with_large_source_fails(self):
        p = self.md("Donanim/A.md", "cok kisa govde", src="A/B.doc")
        r = verify.check_not_empty(self.stats(kisa=[[p, 5000]]))
        self.assertFalse(r["ok"])

    def test_near_empty_body_with_no_stats_entry_fails(self):
        self.md("Donanim/A.md", "bes kelimelik kisacik govde", src="A/B.doc")
        self.assertFalse(verify.check_not_empty(self.stats())["ok"])

    def test_short_source_is_a_note_not_a_failure(self):
        p = self.md("Donanim/A.md", "tek satir", src="A/B.txt")
        r = verify.check_not_empty(self.stats(kisa=[[p, 4]]))
        self.assertTrue(r["ok"])
        self.assertIn("Donanim/A.md", r["notes"][0][1][0][0])

    def test_redirect_page_is_exempt(self):
        p = self.md("Donanim/A.md", "Asil kopya sudur")
        self.assertTrue(verify.check_not_empty(
            self.stats(yonlendirme_yollari=[p]))["ok"])

    def test_dizin_page_is_exempt(self):
        p = self.md("Donanim/A.md", "Sadece ek dosya var")
        self.assertTrue(verify.check_not_empty(
            self.stats(dizin_yollari=[p]))["ok"])

    def test_long_body_passes(self):
        self.md("Donanim/A.md", "kelime " * 100, src="A/B.doc")
        r = verify.check_not_empty(self.stats())
        self.assertTrue(r["ok"])
        self.assertEqual(r["notes"], [])

    def test_footnote_words_do_not_rescue_an_empty_body(self):
        """Dipnot 8 kelime; tum dosyayi saymak bos govdeyi gizlerdi."""
        self.md("Donanim/A.md", "bos", src="COK/UZUN/BIR/KAYNAK/YOLU.doc")
        self.assertFalse(verify.check_not_empty(self.stats())["ok"])


class TestNoLoss(VerifyBase):
    def _dups(self, binary=(), text=()):
        with open(os.path.join(self.rapor, "dups.json"), "w") as fh:
            json.dump({"binary": list(binary), "text": list(text)}, fh)

    def _src(self, rel):
        p = os.path.join(self.tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as fh:
            fh.write("x")

    def test_balanced_accounting_passes(self):
        self._src("KONU/a.doc")
        self._src("KONU/b.gif")
        self._dups()
        r = verify.check_no_loss(self.stats(belge=1, gorsel=1))
        self.assertTrue(r["ok"])

    def test_unaccounted_source_fails(self):
        self._src("KONU/a.doc")
        self._src("KONU/b.doc")
        self._dups()
        self.assertFalse(verify.check_no_loss(self.stats(belge=1))["ok"])

    def test_ds_store_is_not_counted(self):
        self._src("KONU/a.doc")
        self._src("KONU/.DS_Store")
        self._dups()
        self.assertTrue(verify.check_no_loss(self.stats(belge=1))["ok"])

    def test_dot_directories_are_skipped(self):
        self._src("KONU/a.doc")
        self._src(".claude/settings.json")
        self._dups()
        self.assertTrue(verify.check_no_loss(self.stats(belge=1))["ok"])

    def test_binary_duplicates_count_as_accounted(self):
        self._src("KONU/a.doc")
        self._src("KONU/b.doc")
        self._dups(binary=[["a", "b"]])
        self.assertTrue(verify.check_no_loss(self.stats(belge=1))["ok"])


class TestCountSourcesNFD(VerifyBase):
    def test_nfd_bundle_folder_name_is_recognised(self):
        """macOS klasor adlarini NFD dondurur; naif `in` testi kacirirdi.

        Paket klasorundeki .htm 'ornek' sayilir, 'belge' degil -- ama iki
        rol de 'atla' olmadigi icin sayim ayni cikar. Burada dogrulanan
        sey: NFD adli bir klasor cokme/atlama yasatmiyor ve dosyalari
        sayiliyor.
        """
        nfd = unicodedata.normalize("NFD", "WEB DERSLERİ - HTML")
        d = os.path.join(self.tmp, nfd)
        os.makedirs(d)
        with open(os.path.join(d, "a.htm"), "w") as fh:
            fh.write("x")
        self.assertEqual(verify.count_sources(), 1)

    def test_directory_named_like_a_file_is_walked_not_counted(self):
        d = os.path.join(self.tmp, "quickbasickursu.pdf")
        os.makedirs(d)
        with open(os.path.join(d, "quickbasickursu.pdf"), "w") as fh:
            fh.write("x")
        self.assertEqual(verify.count_sources(), 1)


class TestWordCounts(VerifyBase):
    """Gercek cikarim zinciri kullanilir (.txt -> textutil)."""

    def _src(self, rel, words):
        p = os.path.join(self.tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(" ".join("kelime%d" % i for i in range(words)))
        return rel

    def test_faithful_conversion_passes(self):
        rel = self._src("KONU/a.txt", 200)
        self.md("Donanim/A.md", " ".join("kelime%d" % i for i in range(200)),
                src=rel)
        self.assertTrue(verify.check_word_counts(self.stats())["ok"])

    def test_real_shortfall_fails(self):
        rel = self._src("KONU/a.txt", 200)
        self.md("Donanim/A.md", " ".join("kelime%d" % i for i in range(50)),
                src=rel)
        r = verify.check_word_counts(self.stats())
        self.assertFalse(r["ok"])
        self.assertIn("Donanim/A.md", r["detail"][0][0])

    def test_tiny_source_is_below_the_measurement_gate(self):
        rel = self._src("KONU/a.txt", 20)
        self.md("Donanim/A.md", "tek kelime", src=rel)
        self.assertTrue(verify.check_word_counts(self.stats())["ok"])

    def test_source_that_is_a_directory_is_skipped(self):
        """Uc kaynak dizin dosya gibi adlandirilmis; ayrica sadece-ek
        konularin dipnotu bir KLASORU gosterir."""
        os.makedirs(os.path.join(self.tmp, "quickbasickursu.pdf"))
        self.md("Donanim/A.md", "govde", src="quickbasickursu.pdf")
        self.assertTrue(verify.check_word_counts(self.stats())["ok"])

    def test_missing_source_fails_loudly(self):
        self.md("Donanim/A.md", "govde", src="YOK/yok.doc")
        r = verify.check_word_counts(self.stats())
        self.assertFalse(r["ok"])
        self.assertTrue(any("kaynagi okunamayan" in lbl
                            for lbl, _ in r["notes"]))

    def test_redirect_page_is_exempt(self):
        p = self.md("Donanim/A.md", "Asil kopya sudur")
        self.assertTrue(verify.check_word_counts(
            self.stats(yonlendirme_yollari=[p]))["ok"])

    def test_field_codes_do_not_create_a_phantom_shortfall(self):
        rel = "KONU/a.txt"
        pth = os.path.join(self.tmp, rel)
        os.makedirs(os.path.dirname(pth), exist_ok=True)
        prose = " ".join("kelime%d" % i for i in range(100))
        fields = " ".join('HYPERLINK "http://x%d" \\l "a%d"' % (i, i)
                          for i in range(40))
        with open(pth, "w", encoding="utf-8") as fh:
            fh.write(prose + " " + fields)
        self.md("Donanim/A.md", prose, src=rel)
        self.assertTrue(verify.check_word_counts(self.stats())["ok"])


if __name__ == "__main__":
    unittest.main()
