import codecs, sys, os, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import extract
from extract import (
    extract_html, extract_text, read_htm, extract_pdf_text, doc_metadata, ExtractError,
    repair_mojibake, looks_like_garbage, recover_doc_text, GarbageError,
)

ROOT = "/Users/bunyaminakcay/Downloads/Bilgisayar Bilgileri"


def p(rel):
    return os.path.join(ROOT, rel)


class TestExtractHtml(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(ROOT):
            self.skipTest("arsiv bulunamadi")

    def test_doc_produces_html_with_turkish(self):
        html = extract_html(p("CPU/CPU.doc"))
        self.assertIn("<html", html.lower())
        self.assertIn("İşlemci", html)

    def test_doc_has_no_mojibake(self):
        html = extract_html(p("MY SQL/MY SQL.doc"))
        for bad in ["Ã¼", "Ä±", "ï¿½", "³lemesi"]:
            self.assertNotIn(bad, html)

    def test_missing_file_raises(self):
        with self.assertRaises(ExtractError):
            extract_html(p("YOK/YOK.doc"))


class TestReadHtm(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(ROOT):
            self.skipTest("arsiv bulunamadi")

    def test_windows1254_htm_decoded(self):
        html = read_htm(p("OPEN GL/openGL_TR.htm"))
        self.assertNotIn("�", html)
        self.assertIn("<html", html.lower())


class TestPdf(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(ROOT):
            self.skipTest("arsiv bulunamadi")

    def test_pdf_text_extracted(self):
        txt = extract_pdf_text(p("A+ KURS NOTLARI/a+_pdf.pdf"))
        self.assertGreater(len(txt.split()), 3000)
        self.assertIn("Bilgisayar", txt)


class TestMetadata(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(ROOT):
            self.skipTest("arsiv bulunamadi")

    def test_author_and_year(self):
        html = extract_html(p("PC SORUNLARINA KOLAY ÇÖZÜMLER/PC SORUNLARINA KOLAY ÇÖZÜMLER.doc"))
        md = doc_metadata(html)
        self.assertEqual(md["author"], "Fatih Yılmaz")
        self.assertEqual(md["year"], "2004")

    def test_missing_metadata_is_none_not_crash(self):
        md = doc_metadata("<html><head></head><body>x</body></html>")
        self.assertIsNone(md["author"])
        self.assertIsNone(md["year"])


class TestReadHtmFallbackLog(unittest.TestCase):
    """read_htm() bir dosyayı beklenenden farklı bir kodlamayla çözdüğünde
    (ya da hiçbiri çalışmayıp son çareye düştüğünde) FALLBACK_LOG'a kayıt
    bırakmalı. Kaynak arşiv salt-okunur olduğu için fixture'lar burada
    tempfile ile üretilir, arşive fixture eklenmez.
    """

    def setUp(self):
        # Suite'in geri kalanı (ör. gercek arsivdeki OPEN GL/openGL_TR.htm)
        # FALLBACK_LOG'a kayit birakmis olabilir; bu testler kendi
        # ekledikleri kayitlari izole gorsun diye onceki durumu saklayip
        # listeyi temizliyoruz, sonda geri yukluyoruz.
        self._saved_log = list(extract.FALLBACK_LOG)
        extract.FALLBACK_LOG.clear()
        self._tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmpdir.cleanup)

    def tearDown(self):
        extract.FALLBACK_LOG.clear()
        extract.FALLBACK_LOG.extend(self._saved_log)

    def _write(self, name, raw_bytes):
        path = os.path.join(self._tmpdir.name, name)
        with open(path, "wb") as fh:
            fh.write(raw_bytes)
        return path

    def test_clean_declared_charset_leaves_log_untouched(self):
        raw = ('<html><head><meta charset="utf-8"></head>'
               '<body>Merhaba Dünya İşlemci</body></html>').encode("utf-8")
        path = self._write("clean.htm", raw)
        html = read_htm(path)
        self.assertIn("İşlemci", html)
        self.assertEqual(extract.FALLBACK_LOG, [])

    def test_fallback_from_declared_charset_records_one_entry(self):
        # Gercek arsiv vakasinin (PASCAL/...bornova_ege_edu_tr.htm) küçültülmüş
        # hali: charset=windows-1254 bildiriliyor ama 0x81 baytı windows-1254'te
        # tanımsız (UnicodeDecodeError) -> utf-8 de reddeder -> iso-8859-9'a
        # (toplam/total bir kodlama, hiçbir bayt icin patlamaz) düşer.
        raw = (b'<html><head><meta http-equiv="Content-Type" '
               b'content="text/html; charset=windows-1254"></head>'
               b'<body>Merhaba \x81 Dunya</body></html>')
        path = self._write("fallback.htm", raw)
        html = read_htm(path)
        self.assertIn("<html", html.lower())
        self.assertEqual(len(extract.FALLBACK_LOG), 1)
        rec = extract.FALLBACK_LOG[0]
        self.assertEqual(rec["path"], path)
        self.assertEqual(rec["declared"], "windows-1254")
        self.assertEqual(rec["used"], "iso-8859-9")
        self.assertFalse(rec["lossy"])

    def test_last_ditch_replace_branch_is_flagged_lossy(self):
        # HTM_ENCODINGS varsayılanında iso-8859-9 ve latin-1 "total" kodlamalar
        # olduğundan (hiçbir bayt dizisi için asla patlamazlar) son çare dalı
        # normal şartlarda hiç tetiklenmez -- bkz. fix raporundaki bulgu.
        # Bu dalı gerçek read_htm() kodunu çalıştırarak test edebilmek için
        # `encodings` parametresiyle total-kodlamaları (iso-8859-9, latin-1)
        # içermeyen kısıtlı bir aday listesi veriyoruz; 0x81 baytı bu üç
        # adayın (utf-8, windows-1254, cp1252) hepsinde tanımsızdır.
        raw = b'<html><body>Merhaba \x81 Dunya</body></html>'
        path = self._write("lossy.htm", raw)
        html = read_htm(path, encodings=["utf-8", "windows-1254", "cp1252"])
        self.assertIn("�", html)
        self.assertEqual(len(extract.FALLBACK_LOG), 1)
        rec = extract.FALLBACK_LOG[0]
        self.assertEqual(rec["path"], path)
        self.assertIsNone(rec["declared"])
        self.assertEqual(rec["used"], "windows-1254(replace)")
        self.assertTrue(rec["lossy"])


class TestRepairMojibakePureFunction(unittest.TestCase):
    """repair_mojibake() I/O yapmaz; tüm testler saf string'lerle çalışır."""

    def test_each_of_six_pairs_repaired_individually(self):
        for bad, good in extract.MOJIBAKE_MAP.items():
            repaired, n = repair_mojibake(bad)
            self.assertEqual(repaired, good, "beklenen: %r -> %r" % (bad, good))
            self.assertEqual(n, 1)

    def test_all_six_together_in_one_string(self):
        # Ý->İ  þ->ş  ý->ı  Þ->Ş  ð->ğ  Ð->Ğ
        text = "ÝþýÞðÐ"
        repaired, n = repair_mojibake(text)
        self.assertEqual(repaired, "İşıŞğĞ")
        self.assertEqual(n, 6)

    def test_realistic_damaged_words(self):
        text = "ÝÇÝNDEKÝLER bilgisayar aðý ÞARTLI ÇALIÞMA"
        repaired, n = repair_mojibake(text)
        self.assertEqual(repaired, "İÇİNDEKİLER bilgisayar ağı ŞARTLI ÇALIŞMA")
        self.assertEqual(n, 7)  # ÝÇÝNDEKÝLER: 3xÝ, aðý: ð+ý, ÞARTLI: Þ, ÇALIÞMA: Þ

    def test_unaffected_turkish_text_untouched(self):
        text = "Türkçe metin: çğıöşü ÇĞİÖŞÜ, hiçbir mojibake karakteri yok."
        repaired, n = repair_mojibake(text)
        self.assertEqual(repaired, text)
        self.assertEqual(n, 0)

    def test_empty_string(self):
        repaired, n = repair_mojibake("")
        self.assertEqual(repaired, "")
        self.assertEqual(n, 0)

    def test_curly_apostrophe_survives_repair(self):
        # Görev talimatı: text.encode('latin-1').decode('cp1254') yaklaşımı
        # U+2019 (kıvrık apostrof) üzerinde patlar ya da errors='replace'
        # ile sessizce bozulur. 6 karakterlik harita bundan etkilenmemeli.
        text = "TCP/IP’ nin Tarihçesi: baþý’ nda ÝÇÝNDEKÝLER"
        repaired, n = repair_mojibake(text)
        self.assertIn("’", repaired)
        self.assertEqual(repaired.count("’"), 2)
        self.assertEqual(repaired, "TCP/IP’ nin Tarihçesi: başı’ nda İÇİNDEKİLER")
        self.assertEqual(n, 5)  # baþý: þ+ý, ÝÇÝNDEKÝLER: 3xÝ


class TestMojibakeThresholdWiring(unittest.TestCase):
    """Eşik mantığı (_repair_if_damaged) read_htm() üzerinden, tempfile
    fixture'larla test edilir -- arşive dokunulmaz.
    """

    def setUp(self):
        self._saved = list(extract.REPAIRED)
        extract.REPAIRED.clear()
        self._tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmpdir.cleanup)

    def tearDown(self):
        extract.REPAIRED.clear()
        extract.REPAIRED.extend(self._saved)

    def _write_htm(self, name, body_text):
        raw = ('<html><head><meta charset="utf-8"></head><body>'
               + body_text + '</body></html>').encode("utf-8")
        path = os.path.join(self._tmpdir.name, name)
        with open(path, "wb") as fh:
            fh.write(raw)
        return path

    def test_exactly_at_threshold_not_repaired(self):
        # MOJIBAKE_THRESHOLD "n > threshold" ile karşılaştırılır (>=20 değil),
        # yani tam eşik değerinde onarım YAPILMAZ.
        body = "ý" * extract.MOJIBAKE_THRESHOLD
        path = self._write_htm("at_threshold.htm", body)
        text = read_htm(path)
        self.assertIn("ý", text)
        self.assertEqual(extract.REPAIRED, [])

    def test_one_above_threshold_is_repaired(self):
        body = "ý" * (extract.MOJIBAKE_THRESHOLD + 1)
        path = self._write_htm("above_threshold.htm", body)
        text = read_htm(path)
        self.assertNotIn("ý", text)
        self.assertIn("ı", text)
        self.assertEqual(len(extract.REPAIRED), 1)
        self.assertEqual(extract.REPAIRED[0], (path, extract.MOJIBAKE_THRESHOLD + 1))

    # -- F4: ayni yol icin IKI cagri TEK kayit uretmeli -------------
    def test_repaired_logged_once_per_path(self):
        body = "ý" * (extract.MOJIBAKE_THRESHOLD + 1)
        path = self._write_htm("iki_kez.htm", body)
        read_htm(path)
        read_htm(path)
        self.assertEqual(len(extract.REPAIRED), 1)
        self.assertEqual(extract.REPAIRED[0][0], path)

    def test_isolated_single_marker_not_repaired(self):
        # Gerçek arşiv vakasının (C NOTLARI/CNotlari.doc, 3 marker) küçültülmüş
        # hali: izole bir yazım hatası, sistemik CP1254 bozulması değil.
        path = self._write_htm("typo.htm", "listenin baţý gösterir")
        text = read_htm(path)
        self.assertIn("ý", text)
        self.assertEqual(extract.REPAIRED, [])


class TestLooksLikeGarbagePureFunction(unittest.TestCase):
    """looks_like_garbage() de saf; sentetik string sınır testleri I/O gerektirmez."""

    def test_empty_text_is_not_garbage(self):
        self.assertFalse(looks_like_garbage(""))

    def test_plausible_turkish_prose_is_not_garbage(self):
        prose = ("Bu bilgisayar için kullanıcı dosyası hazırlanırken menü "
                  "seçenekleri dikkatle incelenmelidir. ") * 50
        self.assertFalse(looks_like_garbage(prose))

    def test_dense_control_and_symbol_noise_is_garbage(self):
        # OLE/ikili sızıntısını taklit eden yoğun kontrol/sembol karakterleri.
        noise = "\x01\x02\x03﻿⭐■" * 200
        self.assertTrue(looks_like_garbage(noise))

    def test_toc_style_dots_and_numbers_are_not_garbage(self):
        # Görev talimatındaki tuzak: içindekiler sayfası nokta dizileri +
        # sayfa numaraları -- hepsi "makul düzyazı" kümesinin İÇİNDE.
        toc = "BÖLÜM I TEMEL BİLGİLER...........................5\n" * 30
        self.assertFalse(looks_like_garbage(toc))


class TestGarbageDetectionRealArchive(unittest.TestCase):
    """4 bilinen bozuk .doc dosyası ve 3 yanlış-pozitif adayı gerçek arşivden.

    Büyük dosyalar (10-35 MB) yerine en küçük bilinen bozuk dosya (AĞ
    KURULUMU, ~10.7 MB) kullanılıyor; testin süresi makul kalsın diye.
    """

    def setUp(self):
        if not os.path.isdir(ROOT):
            self.skipTest("arsiv bulunamadi")

    def test_known_bad_file_raises_garbage_error(self):
        path = p("AĞ KURULUMU/AĞ KURULUMU.doc")
        with self.assertRaises(GarbageError):
            extract_text(path)

    def test_known_bad_file_raises_garbage_error_in_html_mode_too(self):
        path = p("AĞ KURULUMU/AĞ KURULUMU.doc")
        with self.assertRaises(GarbageError):
            extract_html(path)

    def test_garbage_error_is_catchable_as_extract_error(self):
        path = p("AĞ KURULUMU/AĞ KURULUMU.doc")
        with self.assertRaises(ExtractError):
            extract_text(path)

    def test_toc_heavy_turbo_pascal_not_flagged(self):
        path = p("TURBO PASCAL ' a GİRİŞ 2/TURBO PASCAL ' a GİRİŞ 2.doc")
        text = extract_text(path)
        self.assertGreater(len(text), 0)

    def test_toc_heavy_visual_basic_icindekiler_not_flagged(self):
        path = p("HERKES İÇİN VISUAL BASIC/ICINDEKILER.DOC")
        text = extract_text(path)
        self.assertGreater(len(text), 0)

    def test_short_toc_remnant_acadaralik_not_flagged(self):
        path = p("AUTOCAD DERS NOTLARI/acadaralik.doc")
        text = extract_text(path)
        self.assertGreater(len(text), 0)


class TestRecoverDocText(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(ROOT):
            self.skipTest("arsiv bulunamadi")
        self._saved = list(extract.RECOVERED)
        extract.RECOVERED.clear()

    def tearDown(self):
        extract.RECOVERED.clear()
        extract.RECOVERED.extend(self._saved)

    def test_recovers_real_turkish_words_from_ag_kurulumu(self):
        path = p("AĞ KURULUMU/AĞ KURULUMU.doc")
        text = recover_doc_text(path)
        self.assertIn("bilgisayar", text.lower())
        self.assertIn("Ağ ile ilgili ayarları yapabilmek için", text)
        self.assertGreater(len(text.split()), 1000)

    def test_records_word_count_in_recovered_list(self):
        path = p("AĞ KURULUMU/AĞ KURULUMU.doc")
        text = recover_doc_text(path)
        self.assertEqual(len(extract.RECOVERED), 1)
        rec_path, rec_words = extract.RECOVERED[0]
        self.assertEqual(rec_path, path)
        self.assertEqual(rec_words, len(text.split()))

    def test_missing_file_raises_extract_error(self):
        with self.assertRaises(ExtractError):
            recover_doc_text(p("YOK/YOK.doc"))

    # -- F4: ayni yol icin IKI cagri TEK kayit uretmeli -------------
    #    Boru hatti ayni belge icin extract_html VE extract_text
    #    cagirir; kayit cagri basina eklenirse rapor her hasarli
    #    dosyayi iki kez listeler ve tum toplamlari ikiye katlar.
    def test_recovered_logged_once_per_path(self):
        path = p("AĞ KURULUMU/AĞ KURULUMU.doc")
        recover_doc_text(path)
        recover_doc_text(path)
        self.assertEqual(len(extract.RECOVERED), 1)
        self.assertEqual(extract.RECOVERED[0][0], path)

    # -- F3: tipografik noktalama kosulari BOLMEMELI ----------------
    #    Bu karakterler alfabede olmadigi icin gercek duzyazi ikiye
    #    boluniyor ve <20 karakterlik parcalar atiliyordu.
    def test_typographic_punctuation_does_not_split_runs(self):
        path = p("AĞ KURULUMU/AĞ KURULUMU.doc")
        text = recover_doc_text(path)
        # Once tamamen kayipti (F3 raporu)
        self.assertIn("katmanlaşma", text)
        self.assertIn("catenet", text)
        # Kesme isaretli ekler artik kelimeye bagli kurtariliyor
        self.assertIn("TCP/IP’nin", text)


class TestRecoverEmptyIsError(unittest.TestCase):
    """F5: bos kurtarma sessiz basari degil, hata olmali."""

    def setUp(self):
        self._saved = list(extract.RECOVERED)
        extract.RECOVERED.clear()
        self._tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmpdir.cleanup)

    def tearDown(self):
        extract.RECOVERED.clear()
        extract.RECOVERED.extend(self._saved)

    def test_empty_recovery_raises_and_is_not_logged(self):
        path = os.path.join(self._tmpdir.name, "bos.doc")
        # UTF-16LE olarak cozuldugunde okunabilir hicbir kosu vermeyen icerik
        with open(path, "wb") as fh:
            fh.write(b"\x00\x01" * 4000)
        with self.assertRaises(ExtractError):
            recover_doc_text(path)
        self.assertEqual(extract.RECOVERED, [])


class TestPlainTextInputEncoding(unittest.TestCase):
    """F7: BOM'suz .txt icin textutil'in tahmini yanlisti (Mac OS Turkish).

    Arsivdeki 11 .txt'ten UTF-8 olmayan 10'unun tamami bozuk cikiyordu.
    """

    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmpdir.cleanup)

    def _write(self, name, raw):
        path = os.path.join(self._tmpdir.name, name)
        with open(path, "wb") as fh:
            fh.write(raw)
        return path

    def test_cp1254_txt_detected_as_windows_1254(self):
        path = self._write("tr.txt", "Bu bir örnek satır".encode("cp1254"))
        self.assertEqual(extract.plain_text_input_encoding(path),
                         "WINDOWS-1254")

    def test_utf8_txt_detected_as_utf8(self):
        path = self._write("utf.txt", "Bu bir örnek satır".encode("utf-8"))
        self.assertEqual(extract.plain_text_input_encoding(path), "UTF-8")

    def test_bom_left_to_textutil(self):
        path = self._write("bom.txt", codecs.BOM_UTF8 + "Merhaba".encode("utf-8"))
        self.assertIsNone(extract.plain_text_input_encoding(path))

    def test_non_plain_text_extension_untouched(self):
        path = self._write("x.doc", b"\xc7\xdd\xde")
        self.assertIsNone(extract.plain_text_input_encoding(path))

    def test_cp1254_txt_extracts_correct_turkish(self):
        path = self._write("tr2.txt",
                           "Görme Engellilere göre uyarlanmış".encode("cp1254"))
        text = extract_text(path)
        self.assertIn("Görme Engellilere göre uyarlanmış", text)
        # Mac OS Turkish yanlis cozumunun imzalari
        self.assertNotIn("ˆ", text)
        self.assertNotIn("˝", text)


class TestGarbageErrorHierarchy(unittest.TestCase):
    def test_garbage_error_is_extract_error_subclass(self):
        self.assertTrue(issubclass(GarbageError, ExtractError))

    def test_garbage_error_instance_is_extract_error_instance(self):
        self.assertIsInstance(GarbageError("x"), ExtractError)


if __name__ == "__main__":
    unittest.main()
