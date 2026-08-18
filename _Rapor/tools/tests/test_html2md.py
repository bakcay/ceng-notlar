import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from html2md import html_to_markdown, text_to_markdown


class TestHtmlToMarkdown(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(html_to_markdown("<html><body><p>Merhaba dünya.</p></body></html>"),
                         "Merhaba dünya.")

    def test_style_and_script_dropped(self):
        html = "<html><head><style>p{color:red}</style></head><body><script>x=1</script><p>Metin</p></body></html>"
        out = html_to_markdown(html)
        self.assertNotIn("color:red", out)
        self.assertNotIn("x=1", out)
        self.assertEqual(out, "Metin")

    def test_word_namespace_tags_dropped(self):
        html = "<html><body><p><o:p></o:p>Gövde</p></body></html>"
        self.assertEqual(html_to_markdown(html), "Gövde")

    def test_bold_and_italic(self):
        self.assertEqual(html_to_markdown("<p><b>kalın</b> ve <i>eğik</i></p>"),
                         "**kalın** ve *eğik*")

    def test_heading_tags(self):
        self.assertEqual(html_to_markdown("<h1>Ana</h1><h2>Alt</h2>"), "# Ana\n\n## Alt")

    def test_large_font_paragraph_becomes_heading(self):
        html = ('<html><head><style>p.p1 {font: 16.0px Arial}'
                'p.p2 {font: 12.0px Times}</style><body>'
                '<p class="p1">SABİT DİSKLER</p><p class="p2">Gövde metni burada.</p>'
                '</body></html>')
        out = html_to_markdown(html)
        self.assertIn("## SABİT DİSKLER", out)
        self.assertIn("Gövde metni burada.", out)

    def test_unordered_list(self):
        self.assertEqual(html_to_markdown("<ul><li>bir</li><li>iki</li></ul>"),
                         "- bir\n- iki")

    def test_ordered_list(self):
        self.assertEqual(html_to_markdown("<ol><li>bir</li><li>iki</li></ol>"),
                         "1. bir\n2. iki")

    def test_table(self):
        html = "<table><tr><td>A</td><td>B</td></tr><tr><td>1</td><td>2</td></tr></table>"
        out = html_to_markdown(html)
        self.assertIn("| A | B |", out)
        self.assertIn("| --- | --- |", out)
        self.assertIn("| 1 | 2 |", out)

    def test_link(self):
        self.assertEqual(html_to_markdown('<p><a href="http://x.com">X</a></p>'),
                         "[X](http://x.com)")

    def test_word_field_codes_removed(self):
        html = '<p>INCLUDEPICTURE "http://a/b.jpg" \\* MERGEFORMATINET </p><p>Gerçek metin</p>'
        out = html_to_markdown(html)
        self.assertNotIn("INCLUDEPICTURE", out)
        self.assertNotIn("MERGEFORMATINET", out)
        self.assertIn("Gerçek metin", out)

    def test_entities_decoded(self):
        self.assertEqual(html_to_markdown("<p>a &amp; b &gt; c &nbsp;d</p>"), "a & b > c d")

    def test_blank_paragraphs_collapsed(self):
        html = "<p>A</p><p></p><p>&nbsp;</p><p></p><p>B</p>"
        self.assertEqual(html_to_markdown(html), "A\n\nB")

    def test_markdown_special_chars_escaped_in_text(self):
        self.assertEqual(html_to_markdown("<p>C:\\dizin *yıldız* _alt_</p>"),
                         r"C:\\dizin \*yıldız\* \_alt\_")

    def test_no_crlf_in_output(self):
        self.assertNotIn("\r", html_to_markdown("<p>bir</p>\r\n<p>iki</p>"))


class TestTextToMarkdown(unittest.TestCase):
    def test_paragraphs_separated_by_blank_line(self):
        self.assertEqual(text_to_markdown("Birinci satır.\n\nİkinci satır."),
                         "Birinci satır.\n\nİkinci satır.")

    def test_bullet_lines_become_list(self):
        self.assertEqual(text_to_markdown("• Bir\n• İki"), "- Bir\n- İki")

    def test_collapses_three_or_more_blank_lines(self):
        self.assertEqual(text_to_markdown("A\n\n\n\n\nB"), "A\n\nB")


class TestBugDrivenBehaviors(unittest.TestCase):
    """Task 4 review (C1/C2/I1/I4) tarafından istenen ek testler.

    Brief'in yukarıdaki 18 testi DEĞİŞTİRİLMEDİ (byte-birebir aynı).
    Bu sınıf, Step 5'in gerçek belge taramasında bulunup düzeltilen ama
    hiçbir teste yansımamış yedi davranışı ve iki kritik regresyonu
    (C1, C2) korur -- review'ın belirttiği gibi, `in_cell` düzeltmesi
    testsizdi ve reverte edildiğinde `test_table` bile hâlâ geçiyordu.
    """

    # -- in_cell: textutil'in <td><p>...</p></td> sarmalaması --------
    def test_table_cell_content_wrapped_in_p_survives(self):
        html = ("<table><tr><td><p>A</p></td><td><p>B</p></td></tr>"
                "<tr><td><p>1</p></td><td><p>2</p></td></tr></table>")
        out = html_to_markdown(html)
        self.assertIn("| A | B |", out)
        self.assertIn("| --- | --- |", out)
        self.assertIn("| 1 | 2 |", out)

    def test_table_cell_multiple_paragraphs_join_with_space(self):
        html = "<table><tr><td><p>Birinci</p><p>ikinci</p></td></tr></table>"
        out = html_to_markdown(html)
        self.assertIn("Birinci ikinci", out)

    # -- EMBED_RE: sınırlı eşleşme, sonraki gerçek içeriği yemez ------
    def test_embed_field_code_bounded_does_not_eat_following_content(self):
        html = "<p>k sayı tipidir. EMBED Equation.3  1.79769313486232 x 10 sonu</p>"
        out = html_to_markdown(html)
        self.assertNotIn("EMBED", out)
        self.assertIn("k sayı tipidir.", out)
        self.assertIn("1.79769313486232", out)
        self.assertIn("sonu", out)

    # -- LEADING_HASH_RE: gövde metninde ATX çakışması ----------------
    def test_leading_hash_run_in_body_text_escaped(self):
        html = "<p>##### Bulunan sonuç hücresi taşıyor</p>"
        out = html_to_markdown(html)
        self.assertTrue(out.startswith("\\#####"))
        self.assertIn("Bulunan sonuç hücresi taşıyor", out)

    # -- _looks_like_toc_line: TOC nokta önderi başlık sayılmamalı,
    #    ama üç noktayla (ellipsis) biten GERÇEK başlık etkilenmemeli --
    def test_toc_dot_leader_line_not_marked_heading(self):
        html = ('<html><head><style>p.p1 {font: 16.0px Arial}'
                'p.p2 {font: 12.0px Times}</style><body>'
                '<p class="p1">EDİTÖR ..................................................8</p>'
                '<p class="p2">Gövde metni burada, en az yirmi bir kelime olacak şekilde '
                'uzatılmış olan bu cümle gövde font tabanını doğru şekilde tespit etmek '
                'için kullanılıyor ve yeterince uzundur.</p>'
                '</body></html>')
        out = html_to_markdown(html)
        self.assertNotIn("## EDİTÖR", out)

    def test_heading_ending_in_ellipsis_still_marked_heading(self):
        # Gerçek belgede ("PC SORUNLARINA KOLAY ÇÖZÜMLER.doc") bu başlık
        # <b> ile sarmalı; kalın olmasaydı zaten ayrı bir muhafız
        # (metnin "." ile bitmemesi şartı) devreye girerdi -- bu test
        # özellikle TOC_DOT_LEADER_RE'nin "3+ nokta" yerine "4+ nokta VE
        # sonda rakam" araması gerektiğini, gerçek belge biçimine sadık
        # kalarak izole eder.
        html = ('<html><head><style>p.p1 {font: 16.0px Arial}'
                'p.p2 {font: 12.0px Times}</style><body>'
                '<p class="p1"><b>SABİT DİSKLER...</b></p>'
                '<p class="p2">Gövde metni burada, en az yirmi bir kelime olacak şekilde '
                'uzatılmış olan bu cümle gövde font tabanını doğru şekilde tespit etmek '
                'için kullanılıyor ve yeterince uzundur.</p>'
                '</body></html>')
        out = html_to_markdown(html)
        self.assertIn("## **SABİT DİSKLER...**", out)

    # -- visible: yalnızca biçimlendirmeden oluşan paragraf elenir ----
    def test_empty_bold_run_paragraph_is_dropped(self):
        html = "<p>A</p><p><b></b></p><p>B</p>"
        self.assertEqual(html_to_markdown(html), "A\n\nB")

    # -- _list_stack: iç liste kapandıktan sonra dış listenin türü ----
    def test_nested_list_outer_type_preserved_after_inner_closes(self):
        # Bilinen sınırlama (task-4-report.md'de düzeltildi): iç içe
        # liste DÜZLEŞTİRİLİR -- girinti yoktur, dış sayaç kesintisiz
        # devam eder. Bu test yalnızca _list_stack'in çözdüğü şeyi
        # korur: iç <ol> kapandıktan SONRA gelen dış <li> hâlâ "oli"
        # (numaralı) mi tanınıyor? Düz bir boolean bayrakla bu "- c"
        # (unordered) üretirdi.
        html = "<ol><li>a<ol><li>x</li><li>y</li></ol></li><li>c</li></ol>"
        self.assertEqual(html_to_markdown(html), "1. a\n2. x\n3. y\n4. c")

    # -- <body> skip reset: kapatılmamış </head> gövdeyi yutmamalı ----
    def test_missing_head_close_before_body_does_not_swallow_content(self):
        html = "<html><head><style>p{color:red}</style><body><p>Gövde metni</p></body></html>"
        self.assertEqual(html_to_markdown(html), "Gövde metni")

    # -- KRİTİK regresyon: DENGESİZ etiket belgenin geri kalanını
    #    SESSİZCE YUTMAMALI ---------------------------------------------
    #    Gerçek dosya: OPEN GL/openGL_TR.htm -- 517 <o:p> açılışına karşı
    #    516 kapanış; tek fazla açılış, belgenin %63'ünü (1478 kelime)
    #    hiçbir hata vermeden siliyordu.
    def test_unbalanced_namespaced_open_tag_does_not_swallow_rest(self):
        html = ("<html><body><p>Ilk paragraf.<O:P></span></p>"
                "<p>Ikinci paragraf.</p><p>Son paragraf.</p></body></html>")
        out = html_to_markdown(html)
        self.assertIn("Ilk paragraf.", out)
        self.assertIn("Ikinci paragraf.", out)
        self.assertIn("Son paragraf.", out)

    def test_many_unbalanced_namespaced_opens_do_not_swallow_rest(self):
        # Tek bir dengesizlik değil, birikenler de toparlanmalı.
        html = ("<html><body>" + "".join("<p>P%d<o:p></p>" % i for i in range(20))
                + "<p>Kuyruk cumlesi.</p></body></html>")
        out = html_to_markdown(html)
        self.assertIn("Kuyruk cumlesi.", out)
        self.assertIn("P19", out)

    def test_unbalanced_namespaced_close_tag_is_harmless(self):
        html = "<html><body><p>Once</p></o:p><p>Sonra</p></body></html>"
        out = html_to_markdown(html)
        self.assertIn("Once", out)
        self.assertIn("Sonra", out)

    def test_namespaced_tag_wrapping_text_keeps_the_text(self):
        # Ad alanlı etiket artık BÖLGE değil; içindeki metin korunur.
        html = "<html><body><p><o:p>Gorunur metin</o:p> devam</p></body></html>"
        out = html_to_markdown(html)
        self.assertIn("Gorunur metin", out)
        self.assertIn("devam", out)

    # -- Ad alanlı boş paragraf işaretçisi metne HİÇBİR ŞEY sızdırmamalı
    def test_empty_o_p_marker_injects_no_stray_text(self):
        for marker in ("<o:p></o:p>", "<o:p> </o:p>", "<o:p>&nbsp;</o:p>",
                       "<O:P></O:P>", "<o:p/>"):
            with self.subTest(marker=marker):
                html = "<html><body><p>Bir iki%s</p></body></html>" % marker
                self.assertEqual(html_to_markdown(html), "Bir iki")
                html = "<html><body><p>%sBir iki</p></body></html>" % marker
                self.assertEqual(html_to_markdown(html), "Bir iki")

    def test_o_p_only_paragraph_produces_no_block(self):
        html = "<html><body><p><o:p>&nbsp;</o:p></p><p>Metin</p></body></html>"
        self.assertEqual(html_to_markdown(html), "Metin")

    # -- Atılması GEREKEN bölgeler atılmaya devam etmeli ---------------
    def test_style_and_script_regions_still_dropped_in_body(self):
        html = ("<html><body><style>p{color:red}</style>"
                "<script>var gizli=1;</script><p>Metin</p></body></html>")
        out = html_to_markdown(html)
        self.assertNotIn("color:red", out)
        self.assertNotIn("gizli", out)
        self.assertEqual(out, "Metin")

    def test_word_xml_metadata_island_still_dropped(self):
        # o:Author vb. artık kendi başına bölge açmıyor; <head>/<xml>
        # bölgeleri onları atmayı SÜRDÜRMELİ.
        html = ("<html><head><xml><o:DocumentProperties>"
                "<o:Author>Gizli Yazar</o:Author>"
                "<o:Words>1234</o:Words></o:DocumentProperties></xml>"
                "<title>Gizli Baslik</title></head>"
                "<body><p>Gorunur</p></body></html>")
        out = html_to_markdown(html)
        self.assertNotIn("Gizli Yazar", out)
        self.assertNotIn("Gizli Baslik", out)
        self.assertNotIn("1234", out)
        self.assertEqual(out, "Gorunur")

    # -- Yapısal emniyet sübabı ve ad eşleşmeli kapanış ----------------
    def test_unclosed_title_in_head_does_not_swallow_body(self):
        html = "<html><head><title>Baslik</head><body><p>Govde</p></body></html>"
        self.assertEqual(html_to_markdown(html), "Govde")

    def test_extra_head_close_does_not_underflow_and_drop_later_style(self):
        html = ("<html><head><title>T</title></head></head>"
                "<body><p>Bir</p><style>p{color:red}</style>"
                "<p>Iki</p></body></html>")
        out = html_to_markdown(html)
        self.assertNotIn("color:red", out)
        self.assertIn("Bir", out)
        self.assertIn("Iki", out)

    def test_stray_meta_in_body_does_not_swallow_rest(self):
        html = ("<html><body><p>Once</p><meta name=\"x\" content=\"y\">"
                "<p>Sonra</p></body></html>")
        out = html_to_markdown(html)
        self.assertIn("Once", out)
        self.assertIn("Sonra", out)
        self.assertNotIn("content", out)

    def test_unclosed_head_without_body_tag_still_yields_content(self):
        # <body> etiketi hiç yok; emniyet sübabı <p> ile devreye girmeli.
        html = "<html><head><title>T</title><p>Govde metni</p></html>"
        self.assertEqual(html_to_markdown(html), "Govde metni")

    # -- C1 (KRİTİK) regresyon: alan kodu artık paragrafın/hücrenin
    #    SONUNA kadar değil, yalnızca kendisini siler ------------------
    def test_field_code_mid_paragraph_does_not_delete_trailing_prose(self):
        html = ('<p>Metin basta. INCLUDEPICTURE "a.gif" \\* MERGEFORMATINET '
                'Metin sonda kayboluyor mu?</p>')
        out = html_to_markdown(html)
        self.assertNotIn("INCLUDEPICTURE", out)
        self.assertNotIn("MERGEFORMATINET", out)
        self.assertIn("Metin basta.", out)
        self.assertIn("Metin sonda kayboluyor mu?", out)

    def test_field_code_mid_table_cell_does_not_delete_trailing_prose(self):
        html = ('<table><tr><td><p>Basta HYPERLINK "http://x" \\l "a3" '
                'Sonda metin</p></td><td><p>B</p></td></tr></table>')
        out = html_to_markdown(html)
        self.assertNotIn("HYPERLINK", out)
        self.assertIn("Basta", out)
        self.assertIn("Sonda metin", out)
        self.assertIn("B", out)

    # -- N1 (ÖNEMLİ) regresyon: FIELD_CODE_RE'nin kelime-sınırı çapası
    #    olmalı -- yoksa SEQ/TOC/MERGEFORMAT gibi anahtar kelimeler
    #    SEQUENCE, PROTOCOL, STOCK gibi gerçek kelimelerin İÇİNDE
    #    eşleşip metni bozar (arşiv taramasında 18 belgede 55 yerde
    #    doğrulandı: "CREATE SEQUENCE" -> "CREATE UENCE",
    #    "SERVER_PROTOCOL" -> "SERVER_PROOL", "'STOCK FORM'" ->
    #    "'SK FORM'"). Bu, kelime sayısını neredeyse hiç değiştirmediği
    #    için retention ölçümüne görünmez -- yalnızca doğrudan bir
    #    içerik testi yakalayabilir.
    def test_field_code_keywords_do_not_match_inside_real_words(self):
        html = ("<p>CREATE SEQUENCE pers_id ve SERVER_PROTOCOL ile "
                "MENU 'STOCK FORM' ve USER_SEQUENCES ve DROP_SEQUENCE</p>")
        out = html_to_markdown(html)
        self.assertIn("SEQUENCE", out)
        self.assertIn("PROTOCOL", out)
        self.assertIn("STOCK", out)
        self.assertIn("USER", out)
        self.assertIn("DROP", out)
        self.assertNotIn(" UENCE", out)
        self.assertNotIn("PROOL", out)
        self.assertNotIn("SK FORM", out)

    # -- C2 (KRİTİK) regresyon: alan kodu temizliği escape'ten SONRA
    #    değil ÖNCE çalışmalı; aksi halde tek '\' zaten '\\' olmuş
    #    olur ve tek-backslash bekleyen desenler asla eşleşmez --------
    def test_toc_field_code_removed_not_dead_code(self):
        html = '<p>TOC \\o "1-3" \\h \\z \\u Baslik metni</p>'
        out = html_to_markdown(html)
        self.assertNotIn("TOC", out)
        self.assertIn("Baslik metni", out)

    def test_embed_switch_removed_no_escaped_residue(self):
        html = "<p>EMBED Excel.Chart.8 \\s gercek metin</p>"
        out = html_to_markdown(html)
        self.assertNotIn("EMBED", out)
        self.assertNotIn("\\s", out)
        self.assertIn("gercek metin", out)

    # -- Sentinel mekanizması: yapısal işaretçiler asla sızmamalı,
    #    alan kodu temizliği kendi Markdown söz dizimimizi bozmamalı --
    def test_sentinel_chars_never_leak_and_field_code_does_not_break_formatting(self):
        html = ('<p><b>kalin</b> INCLUDEPICTURE "x.gif" \\* MERGEFORMATINET '
                '<i>egik</i> <a href="http://x.com">link</a></p>')
        out = html_to_markdown(html)
        for ch in ("", "", "", ""):
            self.assertNotIn(ch, out)
        self.assertNotIn("INCLUDEPICTURE", out)
        self.assertIn("**kalin**", out)
        self.assertIn("*egik*", out)
        self.assertIn("[link](http://x.com)", out)

    # -- F2 regresyon: alan kodu bir ÖNCEKİ kelimeye YAPIŞIK geldiğinde
    #    (Word bunu çok sık üretir) de temizlenmeli. Baştaki `\b` çapası
    #    bu durumda eşleşmiyor ve alan kodunun tamamı Markdown'a
    #    sızıyordu (arşivde 2 belgede 36 sızıntı) -------------------
    def test_glued_field_code_after_word_is_removed(self):
        html = ('<p>Sonuc gösterilecektirHYPERLINK \\l "tthFtNtAAB"1. '
                'Devam eden metin.</p>')
        out = html_to_markdown(html)
        self.assertNotIn("HYPERLINK", out)
        self.assertNotIn("tthFtNtAAB", out)
        # Yapıştığı gerçek kelime BOZULMADAN kalmalı
        self.assertIn("gösterilecektir", out)
        self.assertIn("Devam eden metin.", out)

    def test_glued_field_code_after_uppercase_or_digit_is_removed(self):
        html = ('<p>PRIVATEHYPERLINK \\l "x" ve addr11HYPERLINK \\l "y" son</p>')
        out = html_to_markdown(html)
        self.assertNotIn("HYPERLINK", out)
        self.assertIn("PRIVATE", out)
        self.assertIn("addr11", out)
        self.assertIn("son", out)

    # Sol çapayı TAMAMEN kaldırmak yeni bir bozulma yaratıyordu: dBASE
    # fonksiyonu DTOC, "TOC" dalıyla eşleşip "D(" oluyordu. Yapışık dal
    # artık ardından gerçek alan kodu söz dizimi (switch/tırnaklı
    # argüman) ŞART koştuğu için bu ifade dokunulmadan kalır.
    def test_field_code_keyword_as_identifier_suffix_survives(self):
        out = html_to_markdown("<p>SEEK STR(WSUBE_KODU)+DTOC(WTARIH)</p>")
        self.assertIn("DTOC(WTARIH)", out.replace("\\", ""))

    # -- F1: sayfa düzeni (layout) tablosu tespiti ------------------
    #    1990'lar Word belgeleri gövdeyi tek hücreli bir tabloya sarar;
    #    bu sadakatle çevrilince makale tek bir okunamaz '| ... |'
    #    satırına dönüşüyordu.
    def test_single_cell_layout_table_unwrapped_to_prose(self):
        body = "Bu bir makale cümlesidir. " * 60          # ~1500 karakter
        html = "<table><tr><td><p>%s</p></td></tr></table>" % body
        out = html_to_markdown(html)
        self.assertNotIn("|", out)
        self.assertIn("Bu bir makale cümlesidir.", out)

    def test_layout_table_preserves_paragraph_and_heading_structure(self):
        """Sarma açılınca hücre içi paragraf/başlık yapısı korunmalı."""
        gov = "Gövde cümlesi burada duruyor ve yeterince uzundur. " * 30
        html = ('<html><head><style>p.p1 {font: 24.0px Arial}'
                'p.p2 {font: 10.0px Times}</style><body>'
                '<table><tr><td><p class="p1">CPU NEDİR</p>'
                '<p class="p2">%s</p><p class="p2">İkinci paragraf.</p>'
                '</td></tr></table></body></html>' % gov)
        out = html_to_markdown(html)
        self.assertNotIn("|", out)
        self.assertIn("## CPU NEDİR", out)
        # iki ayrı paragraf olarak çıkmalı, tek blok halinde değil
        self.assertIn("\n\nİkinci paragraf.", out)

    def test_layout_table_drops_empty_leading_cell(self):
        body = "Uzun makale metni devam ediyor burada. " * 40
        html = ("<table><tr><td><p></p></td></tr>"
                "<tr><td><p>%s</p></td></tr></table>" % body)
        out = html_to_markdown(html)
        self.assertNotIn("|", out)
        self.assertTrue(out.startswith("Uzun makale metni"))

    def test_small_genuine_data_table_still_rendered_as_table(self):
        html = ("<table>"
                "<tr><td><p>Ad</p></td><td><p>Değer</p></td></tr>"
                "<tr><td><p>RAM</p></td><td><p>512 MB</p></td></tr>"
                "<tr><td><p>CPU</p></td><td><p>800 MHz</p></td></tr>"
                "</table>")
        out = html_to_markdown(html)
        self.assertIn("| Ad | Değer |", out)
        self.assertIn("| --- | --- |", out)
        self.assertIn("| RAM | 512 MB |", out)
        self.assertIn("| CPU | 800 MHz |", out)

    def test_grid_table_with_long_cells_survives_as_table(self):
        """>=3 satır ve >=2 sütunlu tablo, hücreleri uzun olsa da korunur.

        Gerçek örnek: CMOS NEDİR - TTL NEDİR.doc (13x2, en büyük hücre
        1293 karakter) ve RAID.doc (7x2, 2166 karakter) -- ikisi de
        doğrulanmış gerçek veri tablosudur.
        """
        uzun = "Bu hücre uzun bir açıklama içeriyor ve devam ediyor. " * 25
        rows = "".join("<tr><td><p>Terim%d</p></td><td><p>%s</p></td></tr>"
                       % (i, uzun) for i in range(4))
        out = html_to_markdown("<table>%s</table>" % rows)
        self.assertIn("| Terim0 |", out)
        self.assertIn("| --- | --- |", out)
        self.assertIn("| Terim3 |", out)

    def test_nested_table_content_not_lost(self):
        """İç içe tablo, dıştaki hücrenin bloklarını silmemeli.

        Gerçek örnek: PHP_Offline/index.htm -- iç <td> dış hücrenin
        biriktirdiği blokları sıfırlayınca 38 kelimelik bir paragraf
        sessizce kayboluyordu.
        """
        html = ("<table><tr><td><p>Dis hucre metni</p>"
                "<table><tr><td><p>Ic hucre metni</p></td></tr></table>"
                "<p>Dis hucre devami</p></td></tr></table>")
        out = html_to_markdown(html)
        self.assertIn("Dis hucre metni", out)
        self.assertIn("Ic hucre metni", out)
        self.assertIn("Dis hucre devami", out)

    # -- I1: text_to_markdown da HTML yoluyla aynı kaçışlamayı yapmalı -
    def test_text_to_markdown_escapes_leading_hash_shell_prompt(self):
        out = text_to_markdown("# rm /var/adm/messages\nGerçek metin")
        self.assertTrue(out.startswith("\\# rm /var/adm/messages"))
        self.assertIn("Gerçek metin", out)

    def test_text_to_markdown_escapes_underscore_mid_word(self):
        out = text_to_markdown("n_max degeri onemlidir")
        self.assertIn("n\\_max", out)

    def test_text_to_markdown_word_count_unchanged_by_escaping(self):
        raw = "# rm /var/adm/messages\nn_max *onemli* [deger]"
        out = text_to_markdown(raw)
        self.assertEqual(len(out.split()), len(raw.split()))

    def test_text_to_markdown_bullet_conversion_still_works_with_escaping(self):
        self.assertEqual(text_to_markdown("• n_max"), "- n\\_max")

    # Kurtarilan .doc metni (recover_doc_text -> text_to_markdown) ham
    # Word icerigidir ve alan kodu tasir; temizlik yalnizca HTML yolunda
    # oldugu icin 3 belgede 16 alan kodu ciktiya siziyordu.
    def test_text_to_markdown_strips_field_codes(self):
        out = text_to_markdown('Once metin EMBED Word.Picture.6 sonra metin')
        self.assertNotIn("EMBED", out)
        self.assertIn("Once metin", out)
        self.assertIn("sonra metin", out)

    def test_text_to_markdown_strips_hyperlink_field_code(self):
        out = text_to_markdown('ECLIPSE HYPERLINK "http://eclipse.org" adresi')
        self.assertNotIn("HYPERLINK", out)
        self.assertNotIn("eclipse.org", out)
        self.assertIn("ECLIPSE", out)
        self.assertIn("adresi", out)

    def test_text_to_markdown_keeps_real_words_with_field_code_prefixes(self):
        out = text_to_markdown("CREATE SEQUENCE ve SERVER_PROTOCOL")
        self.assertIn("SEQUENCE", out)
        self.assertIn("PROTOCOL", out)

    def test_text_to_markdown_line_structure_preserved(self):
        """Desenlerdeki \\s+ satir sonlarini yutmamali.

        Testin AMACI degismedi: alan kodu desenleri satir sinirlarini
        yutup metni birbirine karistirmamali. Bekleneni degistiren sey,
        artik satirlarin paragraf kurallariyla toplanmasi -- cumle sonu
        noktalamasiyla biten ve ardindan buyuk harf gelen satir paragrafi
        bitirir; bitirmeyen satir bir SONRAKIYLE BOSLUKLA birlesir. Iki
        durum da ayri ayri dogrulanir.
        """
        out = text_to_markdown("EMBED Word.Picture.6\nIkinci satir.\nUcuncu satir.")
        self.assertEqual(out, "Ikinci satir.\n\nUcuncu satir.")
        # Cumle ortasinda kesilen satir bir sonrakiyle birleserek devam
        # eder; icerik yine kaybolmaz, sadece ayrac bosluk olur.
        out = text_to_markdown("EMBED Word.Picture.6\nIkinci satir\nUcuncu satir")
        self.assertEqual(out, "Ikinci satir Ucuncu satir")


class TestTextReflow(unittest.TestCase):
    """PDF satir akisinin paragrafa cevrilmesi (html2md.py 'reflow' bolumu).

    Her testin dayandigi olcum, ilgili modul yorumunda kayitli.
    """

    def test_wrapped_lines_join_into_one_paragraph(self):
        """Cumle ortasinda biten satir bir sonrakine baglanir."""
        src = ("Dunyada hic bir isletim sistemi, UNIX kadar uzun ve surekli\n"
               "gelismede gundemde kalmayi basaramamistir.")
        self.assertEqual(
            text_to_markdown(src),
            "Dunyada hic bir isletim sistemi, UNIX kadar uzun ve surekli "
            "gelismede gundemde kalmayi basaramamistir.")

    def test_short_sentence_end_before_capital_breaks_paragraph(self):
        src = ("Bu satir belgenin sarma genisligine kadar uzanan uzun bir\n"
               "govde satiridir ve burada biter.\n"
               "Yeni paragraf buradan baslar ve o da bir sure devam eder\n"
               "ve boylece iki paragraf olusur.")
        out = text_to_markdown(src)
        self.assertEqual(len(out.split("\n\n")), 2)
        self.assertTrue(out.split("\n\n")[1].startswith("Yeni paragraf"))

    def test_lowercase_next_line_does_not_break_after_abbreviation(self):
        """Turkce'de yeni paragraf kucuk harfle baslamaz -> 'vb.' bolmez."""
        src = ("Klavye, fare, tarayici, mikrofon, barkod okuyucu vb.\n"
               "aygitlar bilgisayara veri girisi icin kullanilir.")
        self.assertNotIn("\n", text_to_markdown(src))

    def test_turkish_capital_starts_new_paragraph(self):
        """Naif [A-Z] testi I S G U O C harflerinde yanilirdi."""
        for ch in "İŞĞÜÖÇ":
            src = "Kisa bir cumle burada biter.\n%sikinci paragraf baslar." % ch
            self.assertIn("\n\n", text_to_markdown(src))

    def test_shell_prompt_line_is_not_reflowed_into_prose(self):
        src = ("Su komutu verin\n"
               "# rm /var/adm/messages\n"
               "Ardindan sistemi yeniden baslatin")
        out = text_to_markdown(src)
        self.assertIn("\\# rm /var/adm/messages", out.split("\n\n"))

    def test_ls_permission_line_is_not_reflowed_into_prose(self):
        src = ("Dizin listesi soyle gorunur\n"
               "drwxr--r-- 1 ayfer 512 Feb 12 13:35 yeni\n"
               "Sahiplik degismistir")
        self.assertIn("drwxr--r-- 1 ayfer 512 Feb 12 13:35 yeni",
                      text_to_markdown(src).split("\n\n"))

    def test_running_footer_is_kept_out_of_prose(self):
        """Sayfa altbilgisi (rakami degisen, 3+ tekrar) paragrafa girmez."""
        src = "\n".join([
            "Kim Korkar UNIXten - PUSULA YAYINCILIK 6",
            "Bu paylasimlar donanima yapilan yatirimi bir miktar",
            "Kim Korkar UNIXten - PUSULA YAYINCILIK 7",
            "azaltacagi icin bir kazanc unsurudur ve boyle devam eder",
            "Kim Korkar UNIXten - PUSULA YAYINCILIK 8",
            "Yan bellek paylasimi da ayri bir kazanctir",
        ])
        out = text_to_markdown(src)
        for blok in out.split("\n\n"):
            if "PUSULA" in blok:
                self.assertEqual(blok, blok.strip())
                self.assertNotIn("paylasimlar", blok)
                self.assertNotIn("azaltacagi", blok)

    def test_toc_dot_leader_lines_stay_separate(self):
        src = "\n".join([
            "PRINT" + "." * 40 + " 29",
            "STR$" + "." * 40 + " 30",
            "VAL" + "." * 40 + " 30",
        ])
        self.assertEqual(len(text_to_markdown(src).split("\n\n")), 3)

    def test_bullet_list_survives_reflow(self):
        src = ("Sirayla su islemler yapilir.\n"
               "• Devrenin baglandigi port adresi ogrenilir\n"
               "• Bir dongu acilir\n"
               "• Belirlenen porta ilk veri gonderilir.")
        out = text_to_markdown(src)
        self.assertIn("- Devrenin baglandigi port adresi ogrenilir\n"
                      "- Bir dongu acilir\n"
                      "- Belirlenen porta ilk veri gonderilir.", out)

    def test_bullet_continuation_line_joins_its_own_item(self):
        """Sarilan madde satiri bir SONRAKI maddeye degil kendi maddesine."""
        src = ("• Devre her ne kadar hizli olsa da herhangi bir atlamaya karsi\n"
               "bu deger portta tutulur.\n"
               "• Ilk veri tekrar porta gonderilir")
        out = text_to_markdown(src)
        self.assertIn("- Devre her ne kadar hizli olsa da herhangi bir "
                      "atlamaya karsi bu deger portta tutulur.", out)
        self.assertIn("- Ilk veri tekrar porta gonderilir", out)

    def test_hyphenated_line_end_keeps_both_tokens(self):
        """Tireli satir sonu YAPISTIRILMAZ -- kelime sayisi korunur.

        Arsivde 62 tireli satir sonu var ama buyuk bolumu gercek birlesik
        kelime tiresidir (X-Windows, MS-DOS, input-output, read-write);
        yapistirma hem onlari bozar hem de iki belirteci bire indirip
        %100 kelime-koruma guvencesini kirardi.
        """
        for src in ("CSS ile HTML sayfalarina cok buyuk kolaylik ge-\n"
                    "tirmistir ve boylece isler kolaylasti.",
                    "grafik ekran kullanimini saglayan X-\n"
                    "Windows ortaya cikti ve yayildi."):
            out = text_to_markdown(src)
            self.assertEqual(len(out.split()), len(src.split()))
            self.assertNotIn("\n", out)

    def test_word_count_preserved_over_mixed_content(self):
        src = "\n".join([
            "Bir giris cumlesi burada biter.",
            "# ls -l /home/ayfer",
            "drwxr--r-- 1 root 512 Feb 12 13:34 yeni",
            "• madde bir",
            "• madde iki",
            "Devam eden bir govde satiri daha uzun sekilde yazilir ve",
            "bir sonraki satirda tamamlanir.",
        ])
        self.assertEqual(len(text_to_markdown(src).split()), len(src.split()))

    def test_horizontal_rule_line_is_escaped_not_swallowed(self):
        out = text_to_markdown("Once metin.\n----------------------------\nSonra metin.")
        self.assertEqual(
            out, "Once metin.\n\n\\----------------------------\n\nSonra metin.")


class TestBrParagraphs(unittest.TestCase):
    """Cift <br> paragraf sinirini geri getirir (CPU.doc kusuru)."""

    def test_double_br_becomes_paragraph_break(self):
        out = html_to_markdown("<p>Birinci paragraf.<br>\n<br>\nIkinci paragraf.</p>")
        self.assertEqual(out, "Birinci paragraf.\n\nIkinci paragraf.")

    def test_single_br_becomes_line_break_not_space(self):
        out = html_to_markdown("<p>Dim cevap(1 To 14)<br>\nDim soru_no</p>")
        self.assertEqual(out, "Dim cevap(1 To 14)\nDim soru\\_no")

    def test_three_or_more_br_collapse_to_one_paragraph_break(self):
        out = html_to_markdown("<p>A.<br><br><br><br>B.</p>")
        self.assertEqual(out, "A.\n\nB.")

    def test_br_inside_list_item_stays_on_one_line(self):
        out = html_to_markdown("<ul><li>bir<br><br>iki</li><li>uc</li></ul>")
        self.assertEqual(out, "- bir iki\n- uc")

    def test_br_inside_heading_stays_on_one_line(self):
        out = html_to_markdown("<h2>Bir<br><br>Iki</h2>")
        self.assertEqual(out, "## Bir Iki")

    def test_br_inside_real_table_cell_stays_on_one_line(self):
        html = ("<table><tr><td>A<br><br>B</td><td>C</td></tr>"
                "<tr><td>1</td><td>2</td></tr>"
                "<tr><td>3</td><td>4</td></tr></table>")
        out = html_to_markdown(html)
        self.assertIn("| A B | C |", out)

    def test_rule_line_from_br_is_escaped(self):
        out = html_to_markdown("<p>Basla.<br><br>--------------------<br><br>Bitti.</p>")
        self.assertIn("\\--------------------", out)


if __name__ == "__main__":
    unittest.main()
