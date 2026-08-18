"""build._sweep: bayat cikti temizligi (B1).

Testler gercek MD/ agacina DOKUNMAZ. build modulunun OUT/RAPOR sabitleri
gecici bir dizine yonlendirilir; boylece silme davranisi izole olarak
olculebilir.
"""
import os
import shutil
import sys
import tempfile
import unicodedata
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import build


class SweepBase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.out = os.path.join(self.tmp, "MD")
        self.rapor = os.path.join(self.out, "_Rapor")
        os.makedirs(self.rapor)
        self._orig = (build.OUT, build.RAPOR)
        build.OUT, build.RAPOR = self.out, self.rapor

    def tearDown(self):
        build.OUT, build.RAPOR = self._orig
        shutil.rmtree(self.tmp, ignore_errors=True)

    def touch(self, rel, body="x"):
        p = os.path.join(self.out, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)
        return p


class TestSweepRemovesStale(SweepBase):
    def test_file_not_in_manifest_is_removed(self):
        keep = self.touch("Donanim/Yeni-Ad.md")
        stale = self.touch("Donanim/Eski-Ad.md")
        removed = build._sweep([self.out], {keep})
        self.assertTrue(os.path.exists(keep))
        self.assertFalse(os.path.exists(stale))
        self.assertIn("Donanim/Eski-Ad.md", removed)

    def test_emptied_directory_is_pruned(self):
        keep = self.touch("Donanim/A.md")
        self.touch("Donanim/eski-konu/ornekler/a.php")
        build._sweep([self.out], {keep})
        self.assertFalse(os.path.exists(os.path.join(self.out, "Donanim",
                                                     "eski-konu")))
        self.assertTrue(os.path.isdir(os.path.join(self.out, "Donanim")))

    def test_out_root_itself_survives_even_if_empty(self):
        build._sweep([self.out], set())
        self.assertTrue(os.path.isdir(self.out))

    def test_non_ascii_stale_name_can_be_removed(self):
        """Bayat kalinti ASCII disi bir adla durabilir; silinebilmeli."""
        keep = self.touch("Donanim/A.md")
        stale = self.touch("Donanim/ESKİ ÇIKTI.md")
        build._sweep([self.out], {keep})
        self.assertFalse(os.path.exists(stale))


class TestSweepProtectsRapor(SweepBase):
    def test_rapor_contents_are_never_touched(self):
        design = os.path.join(self.rapor, "00-tasarim.md")
        with open(design, "w", encoding="utf-8") as fh:
            fh.write("tasarim")
        toolsdir = os.path.join(self.rapor, "tools", ".git")
        os.makedirs(toolsdir)
        with open(os.path.join(toolsdir, "HEAD"), "w") as fh:
            fh.write("ref: refs/heads/main")
        build._sweep([self.out], set())
        self.assertTrue(os.path.isfile(design))
        self.assertTrue(os.path.isfile(os.path.join(toolsdir, "HEAD")))
        self.assertTrue(os.path.isdir(self.rapor))

    def test_guard_delete_refuses_rapor(self):
        with self.assertRaises(RuntimeError):
            build._guard_delete(os.path.join(self.rapor, "stats.json"))

    def test_guard_delete_refuses_outside_md(self):
        with self.assertRaises(RuntimeError):
            build._guard_delete(os.path.join(self.tmp, "kaynak.doc"))

    def test_guard_delete_refuses_md_root(self):
        with self.assertRaises(RuntimeError):
            build._guard_delete(self.out)

    def test_guard_delete_refuses_symlinked_escape(self):
        """Sembolik bir dizinle MD/ disina cikilamaz."""
        outside = os.path.join(self.tmp, "kaynak")
        os.makedirs(outside)
        with open(os.path.join(outside, "a.doc"), "w") as fh:
            fh.write("x")
        os.symlink(outside, os.path.join(self.out, "link"))
        with self.assertRaises(RuntimeError):
            build._guard_delete(os.path.join(self.out, "link", "a.doc"))


class TestSweepScope(SweepBase):
    def test_only_build_does_not_touch_other_categories(self):
        keep = self.touch("Donanim/A.md")
        self.touch("Donanim/bayat.md")
        other = self.touch("Guvenlik/B.md")
        build._sweep([os.path.join(self.out, "Donanim")], {keep})
        self.assertTrue(os.path.exists(other))
        self.assertFalse(os.path.exists(os.path.join(self.out, "Donanim",
                                                     "bayat.md")))

    def test_missing_root_is_ignored(self):
        build._sweep([os.path.join(self.out, "Yok")], set())


class TestSweepNormalisation(SweepBase):
    def test_nfd_on_disk_matches_nfc_manifest_entry(self):
        """macOS dosya adlarini NFD dondurur; manifest NFC olabilir.

        Duz `in` testi bu dosyayi bayat sanip SILERDI.
        """
        nfd = unicodedata.normalize("NFD", "Donanim/ISLETİM.md")
        p = self.touch(nfd)
        nfc = unicodedata.normalize("NFC", p)
        build._sweep([self.out], {nfc})
        self.assertTrue(os.path.exists(p))

    def test_case_insensitive_match_is_kept(self):
        p = self.touch("Donanim/Ornek.md")
        build._sweep([self.out], {os.path.join(self.out, "Donanim",
                                               "ornek.md")})
        self.assertTrue(os.path.exists(p))


class TestManifestRecording(SweepBase):
    def test_write_text_and_copy_file_register_in_manifest(self):
        build.MANIFEST.clear()
        dest = os.path.join(self.out, "Donanim", "A.md")
        os.makedirs(os.path.dirname(dest))
        build._write_text(dest, "# A\n")
        src = os.path.join(self.tmp, "src.gif")
        with open(src, "wb") as fh:
            fh.write(b"GIF89a")
        copied = os.path.join(self.out, "Donanim", "a", "gorseller", "a.gif")
        os.makedirs(os.path.dirname(copied))
        build._copy_file(src, copied)
        self.assertIn(dest, build.MANIFEST)
        self.assertIn(copied, build.MANIFEST)
        build.MANIFEST.clear()


class TestSweepPostcondition(SweepBase):
    def test_report_outputs_are_exempt(self):
        keep = self.touch("Donanim/A.md")
        idx = self.touch("INDEX.md")
        readme = self.touch("_Arsiv/README.md")
        exempt = {os.path.join(self.out, r) for r in build.REPORT_OUTPUTS}
        build._sweep([self.out], {keep} | exempt)
        self.assertTrue(os.path.exists(idx))
        self.assertTrue(os.path.exists(readme))




class TestUniqueByPath(unittest.TestCase):
    """FALLBACK_LOG cozumleme basina kayit tutar; rapor dosya basina okur."""

    def test_same_path_recorded_twice_collapses(self):
        recs = [{"path": "a.htm", "used": "iso-8859-9"},
                {"path": "a.htm", "used": "iso-8859-9"},
                {"path": "b.htm", "used": "cp1252"}]
        self.assertEqual([r["path"] for r in build._unique_by_path(recs)],
                         ["a.htm", "b.htm"])

    def test_empty(self):
        self.assertEqual(build._unique_by_path([]), [])


if __name__ == "__main__":
    unittest.main()
