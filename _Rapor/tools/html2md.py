"""HTML -> Markdown. Word/textutil artıklarını temizler.

Bu modül biçim bilir, dosya sistemi bilmez. Girdi bir HTML dizesi,
çıktı bir Markdown dizesidir.

Başlık tespiti iki yoldan olur:
  1) Gerçek <h1>-<h6> etiketleri
  2) textutil'in ürettiği CSS sınıflarındaki font boyutu: gövde metninin
     en sık görülen (baskın) font boyutundan belirgin büyük ve kısa olan
     paragraflar başlık sayılır.
"""
import html as html_mod
import re
from html.parser import HTMLParser

# İçeriği TÜMÜYLE atılacak BÖLGELER. Bunlar gerçek kapanış etiketine
# sahip, içi metin dolu olabilen bölgelerdir; bir yığında (stack) izlenir.
SKIP_REGION_TAGS = {"style", "script", "head", "title", "xml"}

# İçeriği OLMAYAN (void) etiketler. `<meta>`/`<link>` kapanış etiketi
# almaz; eskiden bunlar da bölge sayacını artırıyor ama hiç azaltmıyordu,
# yani gövdede geçen tek bir `<meta>` belgenin geri kalanını sessizce
# yutabilirdi. Metin taşımadıkları için artık düpedüz yok sayılırlar.
VOID_DROP_TAGS = {"meta", "link"}

# Geriye dönük uyumluluk: dışarıdan atılan etiket kümesini soranlar için.
DROP_TAGS = SKIP_REGION_TAGS | VOID_DROP_TAGS

# YAPISAL EMNİYET SÜBABI. Aşağıdaki blok düzeyi etiketlerden biri
# görüldüğünde belgenin GÖVDESİ başlamış demektir; o an hâlâ açık duran
# "yumuşak" atlama bölgeleri (head/title/xml) kapatılmamış sayılır ve
# yığından atılır. Arşivdeki 188 .htm dosyasının taraması: <head> ve
# <xml> adalarının içinde bu etiketlerin HİÇBİRİ geçmiyor (yalnızca
# title/meta/link/base/style/script ve ad alanlı Word etiketleri), yani
# kural asla yanlış tetiklenemez. style/script ise HTMLParser'da CDATA
# kipindedir: kapanmamış bir <style> içinde etiket olayı hiç doğmaz, bu
# yüzden onlar yığında bırakılır (tarayıcı davranışıyla aynı).
STRUCTURE_TAGS = {"body", "p", "div", "table", "tr", "td", "th",
                  "li", "ul", "ol", "br",
                  "h1", "h2", "h3", "h4", "h5", "h6"}
SOFT_SKIP_TAGS = {"head", "title", "xml"}

# --- Word alan kodu (field code) temizliği -----------------------------
#
# KRİTİK GEÇMİŞ HATA (düzeltildi): önceki sürümde bu grup, eşleştiği
# noktadan flush edilen metnin SONUNA kadar (`[^\n]*`, newline'lar zaten
# tek boşluğa indirgendiği için fiilen `.*`) siliyordu. Aynı paragrafta
# alan kodundan SONRA gerçek metin geldiğinde (ör. "HYPERLINK
# \"http://x\" \\l \"a3\" BİRDEN ÇOK ALANA GÖRE...") o gerçek metin de
# yok oluyordu. Tam arşiv taramasında 103 belgede alan kodu eşleşiyor,
# 87'si gerçek düzyazı kaybediyor, 24 belge %90 kelime-koruma eşiğinin
# altına düşüyordu (bazıları %0'a -- ör. bir sözlük belgesi 5139 -> 2
# kelime). Kök neden: her desen "yönerge + tırnaklı argüman + switch'ler"
# yerine "yönergeden sonra her şey" ile eşleşiyordu.
#
# Şimdi her desen SINIRLI: yönerge + (opsiyonel) argüman + (opsiyonel,
# sıfır veya daha fazla) switch. Bir switch ya `\*` + çıplak biçim
# anahtar kelimesi (MERGEFORMAT, ARABIC gibi -- Word bunları hep böyle
# çiftler), ya da `\harf` + opsiyonel TIRNAKLI değer. Çıplak (tırnaksız)
# bir kelimeyi switch değeri olarak YUTMUYORUZ: \h, \z, \u gibi bayrak
# switch'ler gerçek Word çıktısında hiçbir değer almadan kullanılır;
# bunlardan sonra gelen ilk çıplak kelime GERÇEK içeriğin başlangıcıdır
# (ör. "TOC \o \"1-3\" \h \z \u Başlık metni" -> "Başlık metni" asıl
# içeriktir, switch değeri değil -- ilk denemede bunu da yanlışlıkla
# yutuyordu, ikinci denemede düzeltildi).
#
# ÖNEMLİ: Bu desenler backslash'i KAÇIŞLANMAMIŞ (tek `\`) haliyle
# eşleştirmek üzere yazıldı. `_Collector._finalize()` bu deseni HAM
# (henüz `_escape` uygulanmamış) metne uygular; `_escape` çift ters
# eğik çizgi ürettiği için (`\` -> `\\`) sırayı tersine çevirmek bu
# desenleri sessizce devre dışı bırakır (bkz. TOC \o dalının önceki
# sürümde neden hiç eşleşmediği).
_Q = r'"[^"]*"'              # tırnaklı argüman/switch değeri
_TOK = r'[^\s"\\]+'          # tırnaksız, backslash içermeyen çıplak "kelime"
_ARG = r'(?:\s+(?:%s|%s))?' % (_Q, _TOK)
_SWITCHES = r'(?:\s+\\\*(?:\s+[A-Za-z]+)?|\s+\\[A-Za-z]+(?:\s+%s)?)*' % (_Q,)

# KRİTİK GEÇMİŞ HATA (düzeltildi): anahtar kelimelerin (TOC, SEQ,
# MERGEFORMAT...) hiçbir kelime-sınırı çapası (word-boundary anchor)
# yoktu -- eski greedy regex bunu `HYPERLINK\s+"`, `TOC\s+\\o`,
# `SEQ\s+` gibi zorunlu son-bağlam gereksinimleriyle örtük olarak
# sağlıyordu; sınırlı (bounded) yeniden yazımda bu gereksinimler
# düşünmeden kaldırılmıştı. Sonuç: "SEQ" gerçek "SEQUENCE" kelimesinin
# İÇİNDE, "TOC" "PROTOCOL"un İÇİNDE, "STOCK"un İÇİNDE eşleşiyordu --
# "CREATE SEQUENCE pers_id" -> "CREATE UENCE pers\_id",
# "SERVER_PROTOCOL" -> "SERVER_PROOL", "'STOCK FORM'" -> "'SK FORM'"
# gibi 18 belgede 55 yerde sessiz metin bozulmasına yol açtı (arşiv
# taraması ile doğrulandı). `\b` tek başına yetmez: "_SEQUENCES" gibi
# alt çizgiden sonra gelen durumları yakalar (alt çizgi \w olduğundan
# sınır oluşmaz) ama "CREATE SEQUENCE" gibi gerçek bir kelime sınırından
# BAŞLAYIP ortasında biten eşleşmeleri yakalamaz -- bu yüzden eşleşmenin
# SONUNDA da `(?!\w)` (bir sonraki karakter kelime karakteri olmasın)
# şartı gerekir; ikisi birlikte, yalnızca gerçekten tam bir "kelime"
# olarak duran alan kodu anahtar kelimelerini eşleştirir.
# EK DÜZELTME (F2 -- alan kodu bir ÖNCEKİ kelimeye YAPIŞIK geldiğinde):
# Word alan kodlarını çok sık boşluksuz olarak önceki kelimeye yapıştırır --
# gerçek örnek: "...gösterilecektirHYPERLINK \l \"tthFtNtAAB\"1."
# "HYPERLINK"in solundaki karakter "r" (bir kelime karakteri) olduğundan
# `\b` eşleşmez ve alan kodunun TAMAMI Markdown'a sızardı (arşiv taraması:
# 2 belgede 36 sızıntı -- MİKROKONTROLÖR VE ÇALIŞMA ESASLARI.doc'ta 28,
# C DERS NOTLARI.doc'ta 8).
#
# Sol çapayı TAMAMEN kaldırmak (yalnızca `(?!\w)` bırakmak) YANLIŞTIR --
# ölçümle doğrulandı: "SEEK STR(WSUBE_KODU)+DTOC(WTARIH)" ifadesindeki
# dBASE/FoxPro fonksiyonu DTOC, "TOC" dalıyla eşleşip "+D(WTARIH)"ye
# bozuluyordu (VERİ TABANI VE BAZI KAVRAMLARI.doc + .htm). Sondaki
# `(?!\w)` bunu yakalayamaz, çünkü bozulma eşleşmenin SOLUNDA.
# Sol tarafı karakter sınıfıyla ayırmak da işe yaramaz: gerçek sızıntılar
# hem küçük harften (gösterilecektir), hem BÜYÜK harften (PRIVATE, AB,
# DPTR), hem rakamdan (addr11, data16) sonra geliyor.
#
# AYIRT EDİCİ ÖLÇÜT SÖZ DİZİMİDİR: gerçek bir yapışık alan kodunun
# ARDINDAN daima gerçek alan kodu söz dizimi gelir (boşluk + `\switch`
# ya da boşluk + tırnaklı argüman). "DTOC(" ise doğrudan paranteze
# bağlanır -- ne switch'i ne tırnaklı argümanı vardır. Bu yüzden desen
# iki dallıdır:
#   A) `\b` ile çapalanmış, söz dizimi ZORUNLU DEĞİL (temiz durumlar)
#   B) çapasız, ama ardından alan kodu söz dizimi ZORUNLU (yapışık durumlar)
# Her iki dal da sonda `(?!\w)` ile korunur (bkz. yukarısı: SEQUENCE,
# PROTOCOL, STOCK regresyonları).
#
# Dört varyantın tamamı tam arşiv üzerinde ölçüldü:
#   çapa yok            -> 0 sızıntı, kelime-içi bozulma VAR (SEQUENCE...)
#   `\b` + `(?!\w)`     -> 36 sızıntı, 0 bozulma        (önceki sürüm)
#   yalnızca `(?!\w)`   -> 0 sızıntı, 1 bozulma (DTOC)  (reviewer önerisi)
#   A|B + `(?!\w)`      -> 0 sızıntı, 0 bozulma         (bu sürüm)
# `(?!\w)` artık ANAHTAR KELİMENİN hemen ardına konur, eşleşmenin sonuna
# değil. Nedeni iki katlı:
#   1) Doğruluk: korunmak istenen bozulmaların hepsi "anahtar kelime daha
#      uzun bir tanımlayıcının ÖN EKİ" biçimindedir (SEQ|UENCE, TOC|K,
#      PRO|TOC|L). Kontrol edilmesi gereken yer tam olarak burasıdır.
#   2) Eşleşmenin sonuna konursa geri izleme (backtracking) alan kodunu
#      YARIM bırakır: "HYPERLINK \l \"tthFtNtAAB\"1." dizisinde son
#      `(?!\w)` sondaki "1" yüzünden başarısız olur, motor `_SWITCHES`i
#      kısaltarak geri iz sürer ve `"tthFtNtAAB"` metne SIZAR.
# `_ARG`/`_SWITCHES` kendi içinde açgözlü (`[^\s"\\]+`, `[A-Za-z]+`)
# olduğundan eşleşme zaten bir kelimenin ortasında BİTEMEZ; bu yüzden
# sondaki çapa gereksizdir.
_CODES = (
    r"(?:INCLUDEPICTURE|HYPERLINK|PAGEREF|SEQ)(?!\w)" + _ARG + _SWITCHES +
    # NUMCHARS'ın önbelleğe alınmış sonucu (sayı) da kalıntıdır
    r"|NUMCHARS(?!\w)" + _SWITCHES + r"(?:\s+\d+)?" +
    r"|TOC(?!\w)" + _SWITCHES +
    r"|(?:MERGEFORMATINET|MERGEFORMAT)(?!\w)"
)
# Yapışık dal: anahtar kelimeden hemen sonra gerçek alan kodu söz dizimi
# (boşluk + ters eğik çizgili switch, ya da boşluk + tırnaklı argüman)
# ŞART koşulur. MERGEFORMAT* burada yok: o bir switch değeridir, kendi
# başına argüman/switch almaz, dolayısıyla yapışık biçimde ayırt edilemez.
_GLUED = (
    r"(?:INCLUDEPICTURE|HYPERLINK|PAGEREF|SEQ|NUMCHARS|TOC)"
    r'(?=\s+(?:\\[A-Za-z*]|"))' + _ARG + _SWITCHES
)
FIELD_CODE_RE = re.compile(r"\b(?:" + _CODES + r")|" + _GLUED)
# EMBED alan kodları (gerçek belgelerde çok sık: silinmiş/gömülü OLE
# nesnelerinin -- resim, grafik, formül -- yerini tutan kalıntı metin,
# örn. "EMBED Word.Picture.8", "EMBED Equation.3") YUKARIDAKİ gibi
# "satır sonuna kadar" silinemez: EMBED Equation.3 çoğunlukla aynı
# paragrafta gerçek formül/ değer metniyle birlikte görülüyor
# (ör. "... EMBED Equation.3  1.79769313486232 x 10^308" -- sayı asıl
# içeriktir). Bu yüzden yalnızca alan kodunun kendisi (anahtar kelime +
# nesne türü + varsa \switch) sınırlı biçimde eşleştirilip silinir.
# Aynı ham-metin/kaçışlanmamış-backslash gerekçesi burada da geçerlidir.
EMBED_RE = re.compile(r"EMBED\s+[\w.]+(?:\s+\\\w+)?")
# Gövde metninde ATX başlık sözdizimiyle çakışan bir satır başı (1-6 '#'
# + boşluk/satır sonu) -- gerçek arşiv belgelerinde görüldü: Excel'in
# "#####" sütun-taşması hata kodu bir paragrafın en başında geçebiliyor.
# Kaçmazsak render sırasında istenmeden gerçek bir Markdown başlığına
# dönüşür.
LEADING_HASH_RE = re.compile(r"^#{1,6}(?=\s|$)")
HEADING_MIN_RATIO = 1.15   # gövde fontunun bu katından büyükse başlık adayı
HEADING_MAX_WORDS = 14     # başlık adayı en fazla bu kadar kelime olabilir
# İçindekiler (TOC) satırları "Başlık ..................... 12" biçiminde,
# genelde başlıkla aynı/yakın fontta ve noktalar boşluksuz sıralandığı
# için kelime sayısı sınırının altında kalıyor -- gerçek bir belgede
# (TURBO PASCAL'a GİRİŞ 2.doc) 16 TOC satırı bu yüzden yanlışlıkla
# başlık sayıldı. Ayırt edici imza: uzun bir nokta dizisi + sonda sayfa
# numarası. Yalnızca "3+ nokta" ile sınırlamak yanlıştı: gerçek bir
# başlık "SABİT DİSKLER..." gibi üç noktayla (ellipsis) bitebiliyor --
# bu, PC SORUNLARINA KOLAY ÇÖZÜMLER.doc'ta gözlenen gerçek bir
# regresyondu. Bu yüzden hem "4+ nokta" hem "sonda rakam" birlikte
# aranır.
TOC_DOT_LEADER_RE = re.compile(r"\.{4,}")

# --- Sayfa düzeni (layout) tablosu tespiti ------------------------------
#
# 1990'lar Word belgeleri gövde metnini sayfa kenar boşluğunu ayarlamak
# için TEK HÜCRELİ bir tabloya sarar. Bunlar sadakatle Markdown tablosuna
# çevrilince koca bir makale tek bir `| ... |` satırına dönüşüp
# okunamaz hale geliyordu (308 çıktının 33'ünde 800 karakteri aşan tablo
# satırı, 19'unda 3000'i aşan; en kötüsü 41.112 karakter tek satır).
#
# KURAL (tam arşiv taraması: 123 belgede 1307 tablo ölçüldü):
#   Bir tablo, IZGARA YAPISI YOKSA (satır < 3 VEYA sütun < 2) ve
#   en büyük hücresi >= 800 karakterse "sayfa düzeni tablosu" sayılır
#   ve SARMASI AÇILIR (hücre içerikleri sıradan blok içeriği olarak akar).
#
# MARJ 1 -- koruma tarafı (asıl güvence): >=3 satır VE >=2 sütunlu 299
# tablonun tamamı KOŞULSUZ korunur, hücre boyutundan bağımsız olarak.
# Doğrulanmış gerçek veri tabloları buraya düşer: İKİ BOTUTLU DİZİ.doc
# (19x3), VERİ TABANI SORULAMALARI (16x2), CMOS NEDİR - TTL NEDİR (13x2),
# RAID.doc (7x2), ASP.NET.doc (28x2). Kanıtta ızgara yapısına sahip
# (>=3x2) TEK BİR sayfa düzeni tablosu yok -- bilinen tüm sarmalayıcılar
# ya tek sütunlu ya da en fazla 2 satırlı (CPU.doc 2x2, A'dan Z'ye 2x1,
# PHOTOSHOP 2x1, PHP_Offline ders*.htm 2x3, SES KARTLARI 1x1).
#
# MARJ 2 -- eşik tarafı: ızgarasız 1008 tablonun en büyük hücresi
# karakter olarak şöyle dağılıyor: <800 -> 971, 800-1000 -> 4,
# >1000 -> 41. Yani kesim noktası seyrek bir bölgede duruyor (bandın
# %0,4'ü, üstündeki bölgenin %4,1'ine karşı). 800-1000 bandındaki 4
# tablonun dördü de elle incelendi: hepsi tek hücreli kod/düzyazı
# kutusu, yani sarmalayıcı -- eşiği burada tutmak temkinli taraftır.
# 800 sınırı ayrıca kusurun ölçüldüğü birimle (">800 karakterlik tablo
# satırı") birebir aynıdır. Eşik KARAKTER cinsindendir, kelime değil:
# kelime saymak yoğun kod bloklarını olduğundan küçük gösteriyordu
# (FDİSK NEDİR.doc: 846 karakter ama yalnızca 107 kelime).
LAYOUT_MIN_GRID_ROWS = 3
LAYOUT_MIN_GRID_COLS = 2
LAYOUT_CELL_CHARS = 800


def _cell_text(cell):
    """Hücrenin blok listesini tek satırlık düz metne indirger.

    Sarması açılmayan (gerçek) tablolarda hücre eskiden olduğu gibi tek
    bir dize olarak render edilir; bloklar arası ayraç boşluktur -- bu,
    blok etiketlerinin hücre içinde boşluğa indirgendiği önceki
    davranışın birebir aynısıdır.
    """
    # Gerçek bir Markdown tablo satırı TEK satırdır: hücre metnindeki
    # <br> kaynaklı satır sonları burada boşluğa indirgenir (aksi halde
    # `| a\nb |` tabloyu kırar). Sayfa düzeni tabloları bu yoldan
    # geçmez -- onların blokları akışa olduğu gibi dökülür, satır
    # sonları orada korunur.
    return _one_line(" ".join(t for _, t, _ in cell if t))


def is_layout_table(rows):
    """Tablonun sayfa düzeni sarmalayıcısı olup olmadığını söyler.

    `rows`: satır listesi; her satır hücre listesi, her hücre
    (kind, text, size) blok listesi.

    Izgara boyutu DOLU satır/sütunlarla ölçülür, ham hücre sayısıyla
    değil. Word'ün sarmalayıcı tabloları sıklıkla bölünmüş/colspan'li
    boş hücreler taşır: PHP_Offline/ders*.htm'de tablo ham haliyle
    4x3 görünüyor ama 2. ve 3. sütunlar BAŞTAN SONA boş; tek dolu
    sütunda 4771 karakterlik ders metni duruyor. Ham sayımla bu
    "ızgara yapısı var" sayılıp korunuyordu. Gerçek veri tablolarında
    tüm hücreler dolu olduğundan iki sayım orada aynı sonucu verir.
    """
    if not rows:
        return False
    n_rows = sum(1 for r in rows if any(_cell_text(c) for c in r))
    width = max(len(r) for r in rows)
    n_cols = sum(1 for j in range(width)
                 if any(j < len(r) and _cell_text(r[j]) for r in rows))
    if n_rows >= LAYOUT_MIN_GRID_ROWS and n_cols >= LAYOUT_MIN_GRID_COLS:
        return False
    biggest = max((len(_cell_text(c)) for r in rows for c in r), default=0)
    return biggest >= LAYOUT_CELL_CHARS


def _unwrap_layout_tables(blocks):
    """Blok akışındaki sayfa düzeni tablolarının sarmasını açar.

    Gerçek tablolar ('tr'/'tend' çifti olarak) DEĞİŞMEDEN yeniden
    yayımlanır -- yalnızca hücreler düz metne indirgenir, böylece aşağıdaki
    render döngüsü hiç değişmeden çalışır. Sayfa düzeni tablolarının
    hücre blokları ise doğrudan akışa serpiştirilir; böylece paragraf/
    başlık yapısı ve (font boyutuna dayalı) başlık çıkarımı bu içerik
    için de normal şekilde işler.
    """
    out = []
    rows = []
    for kind, text, size in blocks:
        if kind == "tr":
            rows.append(text)
            continue
        if kind == "tend":
            if rows:
                if is_layout_table(rows):
                    for row in rows:
                        for cell in row:
                            out.extend(cell)
                else:
                    for row in rows:
                        out.append(("tr", [_cell_text(c) for c in row], None))
                    out.append(("tend", "", None))
            rows = []
            continue
        out.append((kind, text, size))
    return out


def _looks_like_toc_line(text):
    if not TOC_DOT_LEADER_RE.search(text):
        return False
    tail = text.rstrip("* ").rstrip()
    return bool(tail) and tail[-1].isdigit()


def _font_sizes(css):
    """CSS'ten {sinif_adi: punto} tablosu çıkarır."""
    out = {}
    for m in re.finditer(r"p\.(\w+)\s*\{([^}]*)\}", css):
        cls, body = m.group(1), m.group(2)
        fm = re.search(r"font:\s*([\d.]+)px", body)
        if fm:
            out[cls] = float(fm.group(1))
    return out


def _dominant_size(vals):
    """En sık görülen font boyutunu döndürür (gövde metni budur).

    Referans koddaki `_median` -- sıralanmış listenin ortanca *indeksini*
    (çift sayıda elemanda üst-ortanca) alıyordu. Az sayıda paragraflı
    belgelerde (ör. yalnızca 1 gövde + 1 başlık paragrafı) bu, başlığın
    kendi font boyutunu taban alarak başlığı gövdeyle eşit/küçük gösteriyor
    ve başlık hiç tespit edilemiyordu. Gerçek belgelerde gövde paragrafı
    sayıca her zaman başlıklardan çok olduğundan, en sık tekrar eden boyut
    (mod) gövdeyi çok daha güvenilir temsil eder. Eşitlik durumunda (ör.
    testteki gibi 1 gövde + 1 başlık) küçük olan taraf seçilir, çünkü
    gövde metni pratikte başlıktan büyük olmaz.
    """
    if not vals:
        return 0.0
    counts = {}
    for v in vals:
        counts[v] = counts.get(v, 0) + 1
    best = max(counts.values())
    return min(v for v, n in counts.items() if n == best)


def _escape(text):
    return re.sub(r"([\\*_`\[\]])", r"\\\1", text)


# --- Yapısal işaretçiler (sentinel) -------------------------------------
#
# KRİTİK GEÇMİŞ HATA (düzeltildi): `_escape` her ters eğik çizgiyi ikiye
# katlar (`\` -> `\\`). Eskiden `handle_data` her veri parçasını ANINDA
# kaçışlıyordu; FIELD_CODE_RE/EMBED_RE ise `_flush`'ta -- yani kaçıştan
# SONRA -- çalışıyordu. Sonuç: Word'ün switch'lerindeki tek `\` zaten
# `\\`'ye dönüşmüş oluyordu ve `TOC\s+\\o` gibi tek-backslash bekleyen
# desenler asla eşleşmiyordu (`TOC \o` sessizce arşive sızıyordu);
# `EMBED_RE`'nin `\switch` eki de aynı nedenle hiç ateşlenmiyordu
# (INTERTECH.doc'ta "\\s" kalıntısının 164 kez tekrarlanması bununla
# doğrulandı).
#
# Çözüm: alan kodu temizliğini HAM (kaçışlanmamış) metin üzerinde, kendi
# ekleyeceğimiz Markdown söz dizimini (`**`, `*`, `[...](...)`) escape
# ETMEDEN ÖNCE yapmak. Ama `_escape`'i erkene almak tek başına yetmez:
# birleştirilmiş `buf` içinde hem gerçek kullanıcı metni hem de bizim
# eklediğimiz yapısal işaretler (kalın/eğik/link parantezleri) yan yana
# duruyor -- ikisini ayırt etmeden `_escape` çalıştırılırsa KENDİ
# Markdown söz dizimimiz de kaçışlanıp bozulur. Bu yüzden yapısal
# işaretler, gerçek belgelerde asla geçmeyecek Özel Kullanım Alanı
# (Private Use Area) Unicode karakterleriyle YER TUTUCU olarak tutulur;
# bunlar `_escape`'in karakter sınıfında olmadığından ondan etkilenmez.
# Sıra: ham metni birleştir -> alan kodu temizle -> escape et (yer
# tutucular dokunulmadan geçer) -> yer tutucuları gerçek Markdown söz
# dizimine çevir.
_BOLD = ""
_ITALIC = ""
_LINK_OPEN = ""
_LINK_CLOSE = ""
# <br> de aynı nedenle yer tutucu ile taşınır: `_finalize`'in ilk adımı
# tüm boşlukları tek boşluğa indirger, bu yüzden gerçek satır sonu
# karakteri oraya kadar hayatta kalamaz.
_BR = ""

# --- <br> -> paragraf sınırı --------------------------------------------
#
# 1990'lar Word belgelerinin bir bölümü paragrafı <p> ile DEĞİL, arka
# arkaya iki <br> ile ayırır. Eski sürüm her <br>'yi boşluğa çeviriyor,
# bu yüzden belgenin tamamı tek paragrafa dönüşüyordu (CPU.doc: 8.122
# karakterlik tek paragraf).
#
# ÖLÇÜM (tüm arşiv, 350 .doc/.htm dosyasında 50.883 <br> dizisi):
#   tek <br>      -> 47.759
#   iki <br>      ->  2.812
#   üç+ <br>      ->    312
# Dev-paragraf kusuru gösteren belgelerin imzası tam olarak ikili <br>:
# CPU.doc 21 ikili / 2 tekil, A'dan Z'ye 286 / 11, ISA HAKKINDA HERŞEY
# 395 / 6, ASSEMBLER 147 / 737, Kodlar3 62 / 716.
#
# KURAL: 2+ ardışık <br> = PARAGRAF SINIRI, tek <br> = SATIR SONU.
# Gerekçe HTML'in kendi anlamıdır (boş bir satır bırakmak için iki <br>
# gerekir) ve yukarıdaki dağılım bunu doğrular.
#
# Tek <br> neden boşluk değil de gerçek satır sonu: örneklendiğinde tek
# <br>'lerin yazarın kasten koyduğu satır yapısı olduğu görülüyor --
# ASSEMBLER.doc'ta ASCII kutu şeması, Kodlar3.doc'ta Visual Basic kod
# listesi (`Dim cevap(1 To 14)<br>Dim secenek(...)<br>`). Boşluğa
# indirgemek bu yapıyı yok ediyordu.
_BR_PARA_RE = re.compile(r"(?:%s[ \t]*){2,}" % _BR)


def _br_to_breaks(text):
    """<br> yer tutucularını paragraf/satır sınırına çevirir."""
    if _BR not in text:
        return text
    text = _BR_PARA_RE.sub("\n\n", text)
    text = text.replace(_BR, "\n")
    text = re.sub(r"[ \t]*\n[ \t]*", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Blok başına gelen yalnız `-`/`=` satırı Markdown'da yatay çizgiye
    # ya da setext başlık altçizgisine dönüşüp METNİ YOK EDER (ASSEMBLER
    # ve Kodlar3'te gerçek ayraç satırları var). Kaçırılır.
    out = []
    for ln in text.split("\n"):
        if RULE_LINE_RE.match(ln):
            ln = "\\" + ln.lstrip()
        out.append(ln)
    return "\n".join(out).strip()


def _one_line(text):
    return re.sub(r"\s+", " ", text).strip()


class _Collector(HTMLParser):
    """HTML'i blok listesine indirger: ('p'|'h2'|'li'|'oli'|'tr', metin)."""

    def __init__(self, sizes):
        super().__init__(convert_charrefs=True)
        self.sizes = sizes
        self.blocks = []
        self.buf = []
        # Atlama durumu bir SAYAÇ değil, açık bölge ADLARINDAN oluşan bir
        # YIĞINDIR. Sayaç sürümü, fazladan bir AÇILIŞ etiketini asla
        # toparlayamıyordu: `max(0, skip - 1)` yalnızca fazladan KAPANIŞA
        # karşı koruyordu. Yığında kapanış etiketi ADIYLA eşleşir; eşleşme
        # yoksa yok sayılır (taşma olmaz), eşleşme varsa üstünde kalan
        # kapanmamış bölgeler de birlikte çözülür.
        self._skip_stack = []
        self.kind = "p"
        self.cur_size = None
        self.in_table = False
        self.in_cell = False
        self.row = []
        # İÇ İÇE TABLO derinliği. Word/e-kitap HTML'inde iç içe tablolar
        # yaygındır (sayfa düzeni tablosunun içinde ikinci bir tablo).
        # Derinlik izlenmezse iç <td>, dış hücrenin biriktirdiği blokları
        # sıfırlayıp SESSİZCE SİLER -- PHP_Offline/index.htm'de tam bir
        # paragrafın (38 kelime) kaybolmasıyla ölçüldü. İç içe tablolar
        # dıştaki hücrenin içine DÜZLEŞTİRİLİR: içerik korunur, yalnızca
        # iç ızgara yapısı sadeleşir.
        self.table_depth = 0
        # Hücre içindeki bloklar ayrı toplanır: bir hücre artık tek bir
        # düz dize değil, (kind, text, size) üçlülerinden oluşan bir blok
        # LİSTESİDİR. Gerçek tablolarda bu liste `_cell_text` ile yine tek
        # dizeye indirgenir (davranış aynı); sayfa düzeni tablolarında ise
        # bloklar olduğu gibi akışa dökülür, böylece paragraf sınırları ve
        # başlık çıkarımı korunur.
        self.cell_blocks = []
        self.href = None
        self._hrefs = []
        # Liste iç içe geçebilir (Word HTML'inde yaygın). Tek bir düz
        # boolean bayrak, iç liste kapanınca dış listenin türünü
        # unutuyordu -- bu yüzden bir yığın (stack) kullanılır: her
        # <ol>/<ul> açılışında türü push edilir, kapanışta pop edilir.
        self._list_stack = []

    @property
    def _in_ol(self):
        return bool(self._list_stack) and self._list_stack[-1]

    @property
    def skip(self):
        return len(self._skip_stack)

    def _unwind_soft_skips(self):
        """Gövde başladıysa kapanmamış head/title/xml bölgelerini çöz."""
        while self._skip_stack and self._skip_stack[-1] in SOFT_SKIP_TAGS:
            self._skip_stack.pop()

    # -- yardimcilar --
    def _finalize(self, buf):
        """Ham `buf` listesini bitmiş Markdown metnine çevirir.

        Sıra önemli (yukarıdaki sentinel açıklamasına bakın): birleştir
        -> boşluk sadeleştir -> alan kodu temizle (HAM metin üzerinde,
        tek `\\` hâlâ tek `\\`) -> escape et -> yapısal sentinel'leri
        gerçek Markdown söz dizimine çevir. Hem `_flush` (paragraf/başlık/
        liste öğesi) hem `</td>`/`</th>` (tablo hücresi) bu tek, doğru
        sıralı yoldan geçer -- iki ayrı kopya kod, iki ayrı hata kaynağı
        anlamına gelirdi.
        """
        text = re.sub(r"\s+", " ", "".join(buf)).strip()
        if not text:
            return ""
        text = FIELD_CODE_RE.sub("", text)
        text = EMBED_RE.sub("", text)
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            return ""
        text = _escape(text)
        text = text.replace(_BOLD, "**").replace(_ITALIC, "*")
        text = text.replace(_LINK_OPEN, "[")
        while _LINK_CLOSE in text and self._hrefs:
            href = self._hrefs.pop(0)
            text = text.replace(_LINK_CLOSE, "](%s)" % href, 1)
        if _LINK_CLOSE in text:
            text = text.replace(_LINK_CLOSE, "")
        return _br_to_breaks(text)

    def _flush(self):
        text = self._finalize(self.buf)
        self.buf = []
        if not text:
            self.kind = "p"
            self.cur_size = None
            return
        # Yalnızca biçimlendirme işaretlerinden oluşan paragraflar (ör.
        # Word'de boş bir bold/italic run -> "**") görünürde hiçbir şey
        # içermez; bunlar elenmezse "## ****" gibi anlamsız sahte
        # başlıklara dönüşür (gerçek belgelerde görüldü). Kullanıcının
        # kendi metnindeki kaçışlı yıldızlar (\*) bu süzgeçten etkilenmez.
        visible = re.sub(r"(?<!\\)\*+", "", text).strip()
        if not visible:
            self.kind = "p"
            self.cur_size = None
            return
        is_heading_tag = (
            self.kind.startswith("h") and len(self.kind) == 2 and self.kind[1].isdigit()
        )
        # Başlık ve liste öğesi TEK satır olmak zorundadır: `## `/`- `
        # öneki yalnızca ilk satıra uygulanır, blok içindeki bir satır
        # sonu başlığı/listeyi keser. Bu bloklarda <br> eski davranışa
        # (boşluk) döner.
        if is_heading_tag or self.kind in ("li", "oli"):
            text = _one_line(text)
        if not is_heading_tag:
            text = LEADING_HASH_RE.sub(lambda m: "\\" + m.group(0), text)
        # Hücre içindeysek blok üst düzey akışa DEĞİL, hücrenin kendi
        # listesine gider. Eskiden hücre içi blok etiketleri yalnızca bir
        # boşluğa indirgeniyordu (aksi halde metin üst düzeye kaçıyordu);
        # artık doğru hedefe yönlendirildiği için o özel duruma gerek yok.
        target = self.cell_blocks if self.in_cell else self.blocks
        target.append((self.kind, text, self.cur_size))
        self.kind = "p"
        self.cur_size = None

    # -- HTMLParser arayuzu --
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if ":" in tag:
            # AD ALANLI ETİKET (o:p, v:shape, w:...): etiket olarak YOK
            # SAYILIR, atlama bölgesi AÇMAZ.
            #
            # KRİTİK GEÇMİŞ HATA (düzeltildi): bunlar bölge açıyordu ve
            # `<o:p>` Word'ün boş-paragraf işaretçisi olarak on binlerce
            # kez geçtiği için tek bir kapanmamış açılış (openGL_TR.htm
            # 607. satır: 517 açılışa karşı 516 kapanış) sayacı kalıcı
            # olarak sıfırın üstünde bırakıyor, belgenin geri kalan
            # %63'ü (1478 kelime) SESSİZCE siliniyordu.
            #
            # Yok saymak içerik kaybettirmez: arşivdeki 188 .htm dosyası
            # tarandı; head/xml/style dışında yalnızca o:p (4438),
            # v:shape (8) ve v:shapetype (2) geçiyor ve HİÇBİRİ metin
            # taşımıyor. Gerçekten atılması gereken ad alanlı Word
            # üstverisi (o:DocumentProperties, w:WordDocument, o:Author…)
            # zaten <head>/<xml> adalarının içinde durur ve o bölgeler
            # atılmaya devam eder. `<o:p> </o:p>` yalnızca boşluk taşır,
            # o da `_finalize`de sadeleşir -- metne hiçbir şey sızmaz.
            return
        if tag in VOID_DROP_TAGS:
            return
        if tag in SKIP_REGION_TAGS:
            self._skip_stack.append(tag)
            return
        if self._skip_stack and tag in STRUCTURE_TAGS:
            # Bazı gerçek belgelerde (ve testte) <head> hiç kapatılmadan
            # <body>/<p> başlar. HTMLParser bunu kendiliğinden düzeltmez;
            # düzeltilmezse bölge hiç kapanmaz ve tüm gövde sessizce
            # yutulur. Blok düzeyi bir etiket görüldüğünde kapanmamış
            # yumuşak bölgeler zorla çözülür (iyi biçimli belgede no-op).
            self._unwind_soft_skips()
        if self.skip:
            return
        if tag == "br":
            self.buf.append(_BR)
        elif tag in ("p", "div", "li") or re.fullmatch(r"h[1-6]", tag):
            # textutil bir hücrenin içeriğini HER ZAMAN <p class="tdN"> ile
            # sarmalar. `_flush` artık hücre içindeyken bloğu hücrenin kendi
            # listesine yazdığı için (bkz. `target`), hücre içi ve dışı aynı
            # yoldan geçebilir. Eskiden hücre içindeki blok etiketleri
            # boşluğa indirgeniyordu; bu, hücredeki TÜM paragraf sınırlarını
            # yok ediyordu -- sayfa düzeni tablosunun sarması açıldığında
            # makalenin tek bir dev paragrafa dönüşmesinin nedeni buydu.
            self._flush()
            if tag in ("p", "div"):
                cls = a.get("class", "")
                self.cur_size = self.sizes.get(cls)
            elif tag == "li":
                self.kind = "oli" if self._in_ol else "li"
            else:
                self.kind = "h" + tag[1]
        elif tag == "ol":
            self._list_stack.append(True)
        elif tag == "ul":
            self._list_stack.append(False)
        elif tag == "table":
            self.table_depth += 1
            self.in_table = True
        elif tag == "tr":
            if self.table_depth <= 1:
                self.row = []
        elif tag in ("td", "th"):
            self._flush()
            self.buf = []
            # Yalnızca EN DIŞ hücre yeni bir blok listesi başlatır; iç içe
            # hücreler dıştakine eklemeye devam eder (düzleştirme).
            if self.table_depth <= 1:
                self.in_cell = True
                self.cell_blocks = []
        elif tag in ("b", "strong"):
            self.buf.append(_BOLD)
        elif tag in ("i", "em"):
            self.buf.append(_ITALIC)
        elif tag == "a" and a.get("href"):
            self.href = a["href"]
            self._hrefs.append(self.href)
            self.buf.append(_LINK_OPEN)

    def handle_endtag(self, tag):
        if ":" in tag or tag in VOID_DROP_TAGS:
            return
        if tag in SKIP_REGION_TAGS:
            # ADLA eşleşen en yakın bölge kapatılır; üstünde kalan
            # kapanmamış bölgeler de birlikte çözülür (ör. </head>,
            # kapanmamış bir <title>'ı da toplar). Yığında yoksa
            # (fazladan kapanış) yok sayılır: taşma olmaz.
            if tag in self._skip_stack:
                while self._skip_stack:
                    if self._skip_stack.pop() == tag:
                        break
            return
        if self.skip:
            return
        if tag in ("b", "strong"):
            self.buf.append(_BOLD)
        elif tag in ("i", "em"):
            self.buf.append(_ITALIC)
        elif tag == "a" and self.href:
            self.buf.append(_LINK_CLOSE)
            self.href = None
        elif tag in ("td", "th"):
            # Kalan tampon da hücrenin blok listesine akıtılır; `_flush`
            # (dolayısıyla `_finalize`) tek ve doğru sıralı temizlik
            # noktası olmayı sürdürür.
            self._flush()
            if self.table_depth <= 1:
                self.row.append(self.cell_blocks)
                self.cell_blocks = []
                self.in_cell = False
            self.buf = []
        elif tag == "tr":
            # Hücreler artık blok LİSTESİ; `any` boş olmayan hücre arar.
            if self.table_depth <= 1:
                if any(self.row):
                    self.blocks.append(("tr", self.row, None))
                self.row = []
        elif tag == "table":
            self.table_depth = max(0, self.table_depth - 1)
            if self.table_depth == 0:
                self.in_table = False
                self.blocks.append(("tend", "", None))
        elif tag in ("p", "div", "li") or re.fullmatch(r"h[1-6]", tag):
            if not self.in_cell:
                self._flush()
        elif tag in ("ol", "ul"):
            if self._list_stack:
                self._list_stack.pop()

    def handle_data(self, data):
        if self.skip:
            return
        # HAM (kaçışlanmamış) veri saklanır -- kaçışlama `_finalize`'de,
        # alan kodu temizliğinden SONRA yapılır (yukarıdaki sentinel
        # açıklamasına bakın).
        self.buf.append(data)


def html_to_markdown(source):
    css = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", source, re.S | re.I))
    sizes = _font_sizes(css)

    c = _Collector(sizes)
    c.feed(source)
    c._flush()

    # Sayfa düzeni tablolarının sarması, taban font boyutu hesaplanmadan
    # ÖNCE açılır: gövdesinin tamamı bir sarmalayıcı tablonun içinde olan
    # belgelerde üst düzeyde hiç 'p' bloğu bulunmuyor, dolayısıyla taban
    # boyut yanlış kalibre olup başlık çıkarımı çalışmıyordu.
    blocks = _unwrap_layout_tables(c.blocks)

    body_sizes = [s for k, t, s in blocks if k == "p" and s and len(str(t).split()) > 20]
    base = _dominant_size(body_sizes) or _dominant_size([s for _, _, s in blocks if s]) or 12.0

    # `out` bir liste "chunk" listesidir: her chunk kendi içinde tek '\n'
    # ile birleştirilmiş bağımsız bir blok (bir paragraf/başlık satırı,
    # ardışık liste öğeleri, ya da bütün bir tablo). Chunk'lar birbirinden
    # boş satırla ayrılır; ama bir liste/tablonun KENDİ satırları arasında
    # boş satır OLMAMALI -- aksi halde çıktı geçerli bir Markdown listesi/
    # tablosu olarak render edilmez (referans kod bunu ihlal ediyordu).
    out = []
    ol_n = 0
    list_buf = []
    list_kind = None
    table_rows = []

    def flush_list():
        nonlocal list_buf, list_kind, ol_n
        if list_buf:
            out.append("\n".join(list_buf))
        list_buf = []
        list_kind = None
        ol_n = 0

    for kind, text, size in blocks:
        if kind == "tr":
            flush_list()
            table_rows.append(text)
            continue
        if kind == "tend":
            flush_list()
            if table_rows:
                width = max(len(r) for r in table_rows)
                lines = []
                for i, r in enumerate(table_rows):
                    r = list(r) + [""] * (width - len(r))
                    lines.append("| " + " | ".join(x.replace("|", "\\|") for x in r) + " |")
                    if i == 0:
                        lines.append("| " + " | ".join(["---"] * width) + " |")
                out.append("\n".join(lines))
                table_rows = []
            continue

        if kind == "li":
            list_buf.append("- " + text)
            list_kind = "li"
            continue
        if kind == "oli":
            if list_kind != "oli":
                ol_n = 0
            ol_n += 1
            list_buf.append("%d. " % ol_n + text)
            list_kind = "oli"
            continue

        flush_list()

        if kind.startswith("h") and len(kind) == 2 and kind[1].isdigit():
            out.append("#" * int(kind[1]) + " " + text)
        else:
            is_heading = (
                size is not None
                and size >= base * HEADING_MIN_RATIO
                and len(text.split()) <= HEADING_MAX_WORDS
                and not text.endswith((".", ":", ";", ","))
                and not _looks_like_toc_line(text)
                # Çok satırlı blok başlık olamaz (bkz. `_one_line`).
                and "\n" not in text
            )
            out.append(("## " + text) if is_heading else text)

    flush_list()

    md = "\n\n".join(x for x in out if x.strip())
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = md.replace("\r", "")
    md = re.sub(r"[ \t]+\n", "\n", md)
    return md.strip()


BULLET_RE = re.compile(r"^\s*[•·▪◦\-\*]\s+")

# --- PDF satır akışını paragrafa çevirme (reflow) -----------------------
#
# PDFKit metni SATIR SATIR verir. Eski sürüm satırları tek `\n` ile
# birleştiriyordu; Markdown tek satır sonunu boşluk sayar, bu yüzden
# belgenin TAMAMI tek bir paragrafa dönüşüyordu (ölçüm: 16 PDF'in 6'sı
# tek paragraf, en kötüsü 127.804 karakter -- Kim Korkar UNIX'ten 3).
#
# KURALLAR 16 PDF'in HAM PDFKit ÇIKTISI ÖLÇÜLEREK seçildi:
#
# ÖLÇÜM 1 -- "boş satır / girinti sinyali" YOKTUR. 16 dosyanın 16'sında
# boş satır sayısı 1 (dosya sonundaki), baştan boşluklu satır sayısı 1.
# Yani paragraf sınırı için boşluk/girinti kullanılamaz; karar tamamen
# satırın kendi metnine dayanmalıdır.
#
# ÖLÇÜM 2 -- satırlar sabit bir sarma genişliğinde kırılır ama genişlik
# belgeden belgeye değişir (p90 satır uzunluğu: 74-112). Bu yüzden eşik
# sabit değil, BELGE BAŞINA ölçülür (`_wrap_width`).
#
# KURAL (birleştir): iki komşu satır arasında paragraf sınırı VARDIR
# ancak ve ancak
#   (a) satır cümle-sonu noktalamasıyla bitiyorsa (`.!?:…`, sondaki
#       kapatan tırnak/parantez atıldıktan sonra),
#   (b) satır belgenin sarma genişliğinden KISAysa (uzun satır sarılmış
#       satırdır, paragrafı bitirmez), VE
#   (c) sonraki satır küçük harfle BAŞLAMIYORSA.
# (c) Türkçe için kritiktir: "vb.", "Dr.", "1." gibi kısaltma/numara
# noktaları satır sonuna denk geldiğinde yanlış bölme yapılmasını
# engeller -- Türkçe'de yeni paragraf küçük harfle başlamaz. `islower()`
# Unicode'a duyarlıdır, bu yüzden İ Ş Ğ Ü Ö Ç de doğru sayılır (naif
# `[A-Z]` testi bu altı harfte yanılırdı).
#
# ÖLÇÜM 3 -- BİRLEŞTİRİLMEMESİ gereken satırlar (kanıtla):
#   * kabuk komutu / kök istemi: `# rm /var/adm/messages`, `# chown ...`
#     (UNIX kitabının 5 parçasında 26+ satır), `ls -l` çıktısındaki
#     izin dizeleri (`drwxr--r-- 1 root 512 Feb 12 13:34 yeni`);
#   * sayfa üstbilgi/altbilgisi: rakamları `#`e indirgendiğinde belgede
#     3+ kez geçen satırlar -- "Kim Korkar UNIX'ten? - Can Uğur Ayfer -
#     PUSULA YAYINCILIK 52" (5 dosyada 40-53 kez), "©2003 Mesut Akcan
#     Sayfa - 10 -" (50 kez), "Photoshop Effects - 6 - aeyStudio.com"
#     (12 kez), çıplak sayfa numaraları. Bunlar paragrafın ORTASINDA
#     geçer; birleştirilirse cümlenin içine karışırlar;
#   * içindekiler satırları (`_looks_like_toc_line`): quickbasickursu
#     PDF'inde 8.534 karakterlik tek bir nokta-dizisi bloğu bundan
#     doğuyordu;
#   * madde imli satırlar (mevcut liste dönüşümü korunur).
#
# TİRELİ SATIR SONU: arşivde VAR (16 PDF'te 62 satır; css-2.pdf'te 36).
# Ama satırlar BİRLEŞTİRİLMEZ, yalnızca aralarına boşluk konur. Gerekçe
# ölçümle: 62 vakanın büyük bölümü gerçek birleşik-kelime tiresidir
# (`X-Windows`, `MS-DOS`, `input-output`, `read-write`, `Ctrl-D`,
# `x-large`, `kullanici-adi`, `dosya-dizin`), yani "tireyi at ve iki
# parçayı yapıştır" kuralı bunları BOZAR. Üstelik yapıştırma iki
# belirteci (token) bire indireceği için %100 kelime-koruma güvencesini
# de kırardı. Bu yüzden tire ve boşluk KORUNUR (render edilen sonuç
# eski davranışla birebir aynıdır, orada da satır sonu boşluğa dönüyordu).
SENTENCE_END_RE = re.compile(r"[.!?:…]$")
# Cümle sonu noktalamasından SONRA gelebilen kapatıcılar: "(... vb.)"
TRAILING_CLOSERS = " \t\"')]}»›’”*"
# Kabuk istemi: satır başında #/$/%/> + boşluk + içerik.
PROMPT_LINE_RE = re.compile(r"^[#$%>]\s+\S")
# `ls -l` izin dizesi: drwxr-xr-x, -rw-r--r-- ...
PERM_LINE_RE = re.compile(r"^[-dlbcps][-rwxsStT]{9}[\s@+]")
DIGIT_RUN_RE = re.compile(r"\d+")
# Sarma genişliği tahmini için yüzdelik. p90: satırların %90'ından uzun
# olan bir satır "sarılmış" sayılır ve paragrafı bitiremez.
REFLOW_WIDTH_PCT = 0.90
REFLOW_MIN_WIDTH = 40
# Üstbilgi/altbilgi sayılmak için gereken en az tekrar (rakamlar
# normalize edildikten sonra).
RUNNING_HEAD_MIN = 3
# Blok başında yalnız `-`/`=` işaretlerinden oluşan satır Markdown'da
# yatay çizgiye ya da setext başlık altçizgisine dönüşüp METNİ YOK EDER.
# `_escape` `*` ve `_`yi zaten kaçırır, `-`/`=` kaçmaz.
RULE_LINE_RE = re.compile(r"^\s*(?:-{3,}[-\s]*|={3,}[=\s]*)$")


def _wrap_width(lines):
    """Belgenin gövde sarma genişliğini tahmin eder (p90 satır uzunluğu)."""
    lens = sorted(len(s) for s in lines if s)
    if not lens:
        return REFLOW_MIN_WIDTH
    idx = min(len(lens) - 1, int(len(lens) * REFLOW_WIDTH_PCT))
    return max(REFLOW_MIN_WIDTH, lens[idx])


def _running_head_keys(lines):
    """Rakamları normalize edildiğinde 3+ kez tekrarlanan satırların kümesi."""
    counts = {}
    for s in lines:
        if not s:
            continue
        k = DIGIT_RUN_RE.sub("#", s)
        counts[k] = counts.get(k, 0) + 1
    return {k for k, n in counts.items() if n >= RUNNING_HEAD_MIN}


def _is_verbatim_line(s):
    """Düzyazıya karıştırılmaması gereken komut/çıktı satırı mı?"""
    return bool(PROMPT_LINE_RE.match(s) or PERM_LINE_RE.match(s))


def _ends_sentence(s):
    return bool(SENTENCE_END_RE.search(s.rstrip(TRAILING_CLOSERS)))


def _starts_new_paragraph(s):
    """Satır yeni bir paragraf başlatabilir mi? (küçük harfle başlamıyorsa)"""
    return not s or not s[0].islower()


def _reflow_lines(lines):
    """Satır listesini bloklara ayırır: [(kind, [satır, ...]), ...].

    kind: 'li' (madde imli) veya 'p'. Bir bloğun satırları tek bir
    paragrafa (boşlukla) birleştirilecek demektir.
    """
    width = _wrap_width(lines)
    heads = _running_head_keys(lines)

    def standalone(s):
        return (_is_verbatim_line(s) or _looks_like_toc_line(s)
                or RULE_LINE_RE.match(s)
                or DIGIT_RUN_RE.sub("#", s) in heads)

    blocks = []
    cur = []
    cur_kind = "p"

    def flush():
        if cur:
            blocks.append((cur_kind, list(cur)))
            del cur[:]

    n = len(lines)
    for i, s in enumerate(lines):
        if not s:
            flush()
            continue
        bullet = bool(BULLET_RE.match(s))
        alone = standalone(s)
        if bullet or alone:
            flush()
        if not cur:
            cur_kind = "li" if bullet else "p"
        cur.append(s)
        if alone:
            flush()
            continue
        nxt = lines[i + 1] if i + 1 < n else ""
        if not nxt or BULLET_RE.match(nxt) or standalone(nxt):
            flush()
            continue
        if _ends_sentence(s) and len(s) <= width and _starts_new_paragraph(nxt):
            flush()
    flush()
    return blocks


def text_to_markdown(text):
    """PDF / düz metin -> Markdown. Satırları paragraflara toplar.

    Satır -> paragraf kuralları ve dayandıkları ölçümler için yukarıdaki
    "PDF satır akışını paragrafa çevirme" bölümüne bakın. Birleştirme
    KELİME SAYISINI DEĞİŞTİRMEZ: satır arasına yalnızca boşluk konur,
    hiçbir belirteç (token) silinmez, eklenmez ya da yapıştırılmaz --
    16 PDF'in tamamında %100 kelime-koruma ölçümü bu yüzden korunur.

    PDF/düz metinde HTML yok, ama içerik yine de Markdown olarak
    yorumlanacak: kaçışlanmazsa gerçek metin yanlışlıkla biçimlendirme
    sözdizimi sayılır. Gözlenen gerçek örnek: "KİM KORKAR UNİX TEN" PDF
    setindeki kök kabuk komutları (`# rm /var/adm/messages`, `# chown`,
    `# mkdir`, `# tail -50`) satır başındaki `#` yüzünden gerçek H1
    başlığına dönüşüyordu (5/16 gerçek PDF'te doğrulandı); aynı şekilde
    `n_max` gibi alt çizgili bir tanımlayıcı kaçışsız bırakılırsa eğik
    yazı (italik) olarak render edilip alt çizgiler kayboluyordu. HTML
    yolunda aynı sorunu `_escape` + `LEADING_HASH_RE` ile çözdük; aynı
    ikisi burada da uygulanır. Kelime sayısını (split() ile) etkilemez
    -- yalnızca karakterlerin önüne `\` eklenir, boşluk eklenmez/
    silinmez -- bu yüzden PDF %100 kelime-koruma ölçümünü bozmaz.
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = html_mod.unescape(text)
    lines = []
    for ln in text.split("\n"):
        # Alan kodu temizligi bu yolda da gerekli: UTF-16LE kurtarmasindan
        # (recover_doc_text) gelen .doc metni ham Word icerigidir ve alan
        # kodlarini tasir. Yalnizca html_to_markdown temizlik yaptigi icin
        # kurtarilan 3 belgede 16 alan kodu ciktiya siziyordu
        # (AĞ KURULUMU 9, INTERTECH 4, ICON AUTHOR 3 -- ornegin
        # 'EMBED Word.Picture.6' ve 'HYPERLINK "http://eclipse.org"').
        # PDF yolunda etkisi olcusuyle sifirdir: 15 PDF kaynakli ciktida
        # bu desenler hic eslesmiyor.
        #
        # SIRA: HTML yolundaki ile ayni -- temizlik HAM metinde, `_escape`
        # ters egik cizgileri ikiye katlamadan ONCE yapilir; tersi olsaydi
        # tek `\` zaten `\\` olacagi icin switch bekleyen dallar hic
        # eslesmezdi. Satir satir uygulanir ki desenlerdeki `\s+` satir
        # sonlarini yutup satir yapisini bozmasin.
        lines.append(EMBED_RE.sub("", FIELD_CODE_RE.sub("", ln)).strip())

    out = []
    for kind, block in _reflow_lines(lines):
        parts = []
        for j, s in enumerate(block):
            if j == 0 and kind == "li":
                s = BULLET_RE.sub("", s).strip()
            body = _escape(s)
            if j == 0:
                # Markdown yapısı YALNIZCA blok başında yorumlanır; kaçış
                # da orada gerekir (satır ortasındaki `#` zararsızdır).
                body = LEADING_HASH_RE.sub(lambda m: "\\" + m.group(0), body)
                if RULE_LINE_RE.match(body):
                    body = "\\" + body.lstrip()
            if body:
                parts.append(body)
        txt = " ".join(parts)
        if not txt:
            continue
        out.append((kind, ("- " + txt) if kind == "li" else txt))

    md = []
    prev = None
    for kind, txt in out:
        if md:
            # Ardışık madde satırları TEK satır sonuyla ayrılır; araya boş
            # satır girerse liste kopar (mevcut liste testi bunu korur).
            md.append("\n" if (kind == "li" and prev == "li") else "\n\n")
        md.append(txt)
        prev = kind
    md = "".join(md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()
