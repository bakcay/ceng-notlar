# Konsolide Düzeltme Turu — Rapor

Durum: **TAMAMLANDI**. 7 bulgunun tamamı düzeltildi, tam derleme yeniden
çalıştırıldı, arşiv bütünlüğü korundu.

| | |
|---|---|
| Commit | `3463c1e`, `c306d9d`, `48cfca3`, `60f838e`, `f6a4cf8` |
| Test | 129 → **156**, tamamı geçiyor |
| Arşiv | 692 dosya / 270 dizin — öncesi ve sonrası **aynı** |
| Çıktı | 308 `.md` (değişmedi) |

Derleme satırı:

```
belge:303 yonlendirme:3 dizin:2 ornek:316 gorsel:34 arsiv:24
hata:0 kisa:33 cakisma:0 kurtarma:2 bos:0
```

---

## F1 — Sayfa düzeni tabloları (html2md.py)

### Kural

> Bir tablonun **ızgara yapısı yoksa** (dolu satır < 3 **VEYA** dolu sütun < 2)
> **ve** en büyük hücresi **>= 800 karakter** ise, sayfa düzeni sarmalayıcısı
> sayılır ve sarması açılır.

Izgara boyutu **dolu** satır/sütunlarla ölçülür, ham hücre sayısıyla değil.

### Kanıt ve marj

123 belgedeki **1307 tablo** ölçüldü.

**Marj 1 — koruma tarafı (asıl güvence).** `>=3` dolu satır ve `>=2` dolu sütunlu
299 tablo koşulsuz korunur, hücre boyutundan bağımsız. Doğrulanmış gerçek veri
tablolarının tamamı buraya düşer:

| Belge | Boyut | En büyük hücre |
|---|---|---|
| `İKİ BOTUTLU DİZİ.doc` | 19x3 (10 tablo) | 486 ch |
| `VERİ TABANI SORULAMALARI.doc` | 16x2 | 2039 ch |
| `CMOS NEDİR - TTL NEDİR.doc` | 13x2 | 1293 ch |
| `RAID.doc` | 7x2 | 2166 ch |
| `ASP.NET.doc` | 28x2 | 711 ch |

Kanıtta ızgara yapısına sahip **tek bir** sayfa düzeni tablosu yok; bilinen tüm
sarmalayıcılar ya tek sütunlu ya da en fazla 2 satırlı.

**Marj 2 — eşik tarafı.** Izgarasız 1008 tablonun en büyük hücresi (karakter):
`<800 → 971`, `800-1000 → 4`, `>1000 → 41`. Kesim seyrek bir bölgede
(bandın %0,4'ü, üstündeki bölgenin %4,1'ine karşı). 800-1000 bandındaki 4
tablonun dördü de elle incelendi: hepsi tek hücreli kod/düzyazı kutusu.

Son durumda **korunan en büyük hücre 799 ch**, **açılan en küçük hücre 846 ch** —
eşik tam boşluğa düşüyor.

Eşik **karakter** cinsindendir, kelime değil: kelime saymak yoğun kod bloklarını
olduğundan küçük gösteriyordu (`FDİSK NEDİR.doc`: 846 ch ama yalnızca 107 kelime).

### Yan düzeltmeler (F1 kapsamında zorunlu çıktı)

* **Hücre içi paragraf yapısı.** Hücreler artık tek düz dize değil, blok
  listesi olarak toplanıyor. Sarma açılınca paragraf sınırları ve font tabanlı
  başlık çıkarımı korunuyor — `CPU.md` artık `## CPU (Central Processing Unit)`
  başlığını geri kazanıyor (boş başlık hücresi düşüyor).
* **İç içe tablolar.** İç `<td>`, dış hücrenin biriktirdiği blokları
  sıfırlayıp siliyordu; `PHP_Offline/index.htm`'de 38 kelimelik bir paragraf
  sessizce kayboluyordu. Artık derinlik izleniyor, iç tablolar dış hücreye
  düzleştiriliyor.

### 183 sütun bulmacası — çözüldü

`PHP-2-11.md` / `PHP-2-3.md` **nested-layout artefaktı değil**. 183 borunun
**180'i kaçışlanmış `\|`** — PHP kaynak kodundaki `||` (mantıksal veya)
operatörleri. Gerçek sütun sayısı **3**. Tablo yine de sayfa düzeni
sarmalayıcısıydı ve şimdi açılıyor.

### Sonuç

**>800 karakterlik tablo satırı içeren dosya: 33 → 5** (satır: 22 → 9).

| Dosya | Satır | Değerlendirme |
|---|---|---|
| `Veritabani/Veri-Tabani-Sorulamalari.md` | 3 | **Gerçek** 16x2 veri tablosu (SQL örnek/sonuç çiftleri) |
| `Donanim/RAID.md` | 2 | **Gerçek** 7x2 veri tablosu (RAID seviyeleri) |
| `Veritabani/SQL-Sorgulama-Dili.md` | 2 | **Gerçek** çok sütunlu anahtar kelime listesi (4 sütun x 380-445 ch; 2 sütun x 758/688 ch). Hiçbir hücre 800'ü aşmıyor — satır uzunluğu gerçekten çok sütunlu olmasından geliyor. |
| `Elektronik/CMOS-Nedir-TTL-Nedir.md` | 1 | **Gerçek** 13x2 karşılaştırma tablosu |
| `Ag-ve-Iletisim/Network-Temelleri.md` | 1 | **Sarmalayıcı** — tek hücre, 799 ch. Eşiğin 1 karakter altında. Tek kalan yanlış-negatif. |

---

## F2 — Yapışık alan kodu sızıntısı (html2md.py)

Reviewer'ın önerisi (**yalnızca `(?!\w)` bırakmak**) **hatalıydı** ve ölçümle
çürütüldü: `SEEK STR(WSUBE_KODU)+DTOC(WTARIH)` ifadesindeki dBASE/FoxPro
fonksiyonu `DTOC`, `TOC` dalıyla eşleşip **`+D(WTARIH)`** oluyordu
(`VERİ TABANI VE BAZI KAVRAMLARI.doc` + `.htm`). Sondaki `(?!\w)` bunu
yakalayamaz çünkü bozulma eşleşmenin **solunda**. Reviewer yalnızca adı geçen
5 regresyonu (`SEQUENCE`, `PROTOCOL`, `STOCK`, `USER_SEQUENCES`,
`DROP_SEQUENCE`) kontrol etmiş — hepsinde bozulma sağ tarafta.

Sol tarafı karakter sınıfıyla ayırmak da işe yaramaz: gerçek sızıntılar hem
küçük harften (`gösterilecektir`), hem BÜYÜK harften (`PRIVATE`, `AB`, `DPTR`),
hem rakamdan (`addr11`, `data16`) sonra geliyor.

**Ayırt edici ölçüt söz dizimidir.** Desen iki dallı:

* **A)** `\b` ile çapalanmış, söz dizimi zorunlu değil (temiz durumlar)
* **B)** çapasız, ama ardından **gerçek alan kodu söz dizimi** (boşluk +
  `\switch` ya da boşluk + tırnaklı argüman) **şart** (yapışık durumlar)

Ayrıca `(?!\w)` **anahtar kelimenin hemen ardına** taşındı, eşleşmenin sonuna
değil: sonda olduğunda geri izleme alan kodunu yarım bırakıp tırnaklı argümanı
sızdırıyordu (`HYPERLINK \l "tthFtNtAAB"1.` → `"tthFtNtAAB"1.` kalıyordu).

| Varyant | Sızıntı | Kelime-içi bozulma |
|---|---|---|
| çapa yok | 0 | VAR |
| `\b` + `(?!\w)` (gönderilen) | 36 | 0 |
| yalnızca `(?!\w)` (reviewer) | 0 | **1 (DTOC)** |
| **A\|B, `(?!\w)` kelimeden sonra** | **0** | **0** |

### Ek kapsam: kurtarma yolu

F2 hedefi olan 2 belge **0 sızıntıya** indi. Ancak tam taramada `text_to_markdown`
yolunda **16 sızıntı daha** bulundu (`AĞ KURULUMU` 9, `INTERTECH` 4,
`ICON AUTHOR` 3) — UTF-16LE kurtarmasından gelen ham Word metni alan kodu
taşıyor ve temizlik yalnızca HTML yolundaydı. Temizlik bu yola da eklendi;
PDF etkisi ölçüldü: 15 PDF kaynaklı çıktıda bu desenler **hiç eşleşmiyor**.

**Sonuç: arşiv genelinde 0 sızıntı, 0 kelime-içi bozulma.**
Korunması gerekenler yerinde: `SEQUENCE` x17, `SERVER_PROTOCOL` x4,
`STOCK` x5, `DTOC` x2.

---

## F3 — Kurtarmada içerik kaybı (extract.py)

`recover_doc_text`, `looks_like_garbage` ile aynı alfabeyi kullanıyordu; o küme
tipografik noktalama içermez. Kurtarmaya **kendi geniş alfabesi** verildi.
`looks_like_garbage`'ın kümesi **bilerek değiştirilmedi** — 0.3 eşiği ve 5 kat
marjı o küme üzerinde ölçülmüştü.

Koşuları bölen tipografik karakterler (5 dosya toplamı):
`’ 579, ” 247, “ 243, © 68, ‘ 20, … 18, — 4, ÷ 2, – 2`. Bağlam incelemesi
hepsinin gerçek metinde olduğunu gösterdi (`TCP/IP’nin`, `“firewall”`,
`Netware’in`).

### Kelime sayısı: önce / sonra

| Dosya | Önce | Sonra | Fark |
|---|---:|---:|---:|
| `AĞ KURULUMU.doc` | 15628 | 15589 | -39 |
| `ICON AUTHOR 2.doc` | 6673 | 6794 | +121 |
| `KULLANICI PROFİLLERİ ...doc` | 4760 | 4685 | -75 |
| `VISUAL BASİC MENÜLERİ.doc` | 2878 | 2872 | -6 |
| `INTERTECH.doc` | 9871 | 9855 | -16 |

**Düşüşler kayıp değil, yeniden belirteçlemedir**: `TCP/IP` + `nin` (2 belirteç)
→ `TCP/IP’nin` (1 belirteç). Belirteç düzeyinde doğrulandı — kaybolan her
belirtecin karşılığı birleşmiş biçimde mevcut.

`katmanlaşma` → **var**. `catenet` → **var**. (İkisi de önce tamamen yoktu.)

### min-run ayarı: 20 KORUNDU (kanıtla)

20'nin altına inince giren koşular içerik değil **gürültü**: kayıt defteri
anahtarları (`CurrentControlSet`, `CurrentVersion`, `Software`), OLE yapı
adları (`WordDocument`, `ObjInfo`, `Ole10Native`, `SummaryInformation`), alan
kodu kalıntısı (`EMBED PBrush`, `MERGEFORMATINET`). `INTERTECH` 20→15 ile
+1374 "kelime" kazanıyor ama tamamı tekrar eden OLE meta verisi. Alfabe
düzeltildikten sonra 20 eşiğinde atılan koşuların tamamı zaten alan kodu
kalıntısıdır.

---

## F4 — Çift kayıt (extract.py)

`_log_once()` ile yol başına tek kayıt. Üyelik **listenin kendisinden** okunur;
ayrı bir "görülen" kümesi tutulmaz, çünkü testler ve çağıranlar listeleri
`.clear()` ile sıfırlıyor.

**Doğrulama (tam derleme sonrası):**

* `REPAIRED`: **6 kayıt, 6 benzersiz yol** — tekrar yok
* `RECOVERED`: **5 kayıt, 5 benzersiz yol** — tekrar yok

---

## F5 — Sessiz boş kurtarma (extract.py)

UTF-16LE taraması boş dönerse artık `ExtractError` yükselir. `build.py::_salvage`
bunu yakalayıp `None` döner (= kurtarılamadı), çağıran taraf dosyayı `bos`
olarak raporlar. Çökme yolu yok.

---

## F6 — H1'de dosya uzantısı (translit.py)

Uzantı, sözcük büyük/küçük harf düzeltmesinden **önce** atılır. Kök neden:
`TABANI.doc` tek sözcük sayılınca `core` ondan `TABANIdoc` üretiyor,
`w.replace(core, capped, 1)` noktalı asıl sözcükte bu alt diziyi bulamıyor ve
sözcük **hiç düzeltilmeden** kalıyordu.

Uzantı genel bir "sondaki 1-5 harflik nokta eki" kuralıyla atılamaz: arşivde
**`ASP.NET`** adlı bir konu klasörü var. Bu yüzden açık uzantı listesi kullanılır.

| Girdi | Önce | Sonra |
|---|---|---|
| `ACCESS VERİ TABANI.doc` | `Access Veri TABANI.doc` | **`Access Veri Tabani`** |
| `BİLGİSAYAR AĞLARINDA TEMEL KAVRAMLAR.doc` | `... Temel KAVRAMLAR.doc` | **`Bilgisayar Ağlarinda Temel Kavramlar`** |
| `quickbasickursu.pdf` | `quickbasickursu.pdf` | **`Quickbasickursu`** |
| `ASP.NET` | `ASP.NET` | `ASP.NET` (değişmedi) |
| `Asp'ye giris.Asp nedir` | — | `Asp'ye giris.Asp Nedir` (değişmedi) |

Uzantıyla biten H1 sayısı: **0**.

---

## F7 — Kodlama bozulması — GERÇEK BOŞLUK, DÜZELTİLDİ

**Teşhis.** `textutil` man sayfası: *"by default encoding will be detected from
BOM"*. BOM'suz `.txt`'te tahmin sistem varsayılanına düşüyor ve bu arşivde
**Mac OS Turkish** oluyor. Bayt düzeyinde doğrulandı:

| Bayt | textutil verdiği | Doğrusu (CP1254) | `mac_turkish` |
|---|---|---|---|
| `0xC7` | `«` | `Ç` | `«` ✓ |
| `0xDD` | `ı` | `İ` | `ı` ✓ |
| `0xDE` | `Ş` | `Ş` | `Ş` ✓ |
| `0xF6` | `ˆ` | `ö` | `ˆ` ✓ |
| `0xFD` | `˝` | `ı` | `˝` ✓ |

Tamamı `mac_turkish` tablosuyla birebir örtüşüyor.

**Kapsam rapordakinden geniş.** Bildirilen 2 çıktı yalnızca en görünür
olanlardı: 11 `.txt` dosyasından UTF-8 olmayan **10'unun tamamı** bozuk
çıkıyordu (yalnızca `webmail.txt` geçerli UTF-8).

**Çözüm** çıkarım katmanında: `.txt` için giriş kodlaması `-inputencoding` ile
açıkça bildirilir (BOM varsa textutil'e bırakılır; yoksa katı UTF-8, o da
olmuyorsa `WINDOWS-1254`). Yalnızca `.txt` için — `.doc/.rtf` kodlamayı kendi
yapısında taşır, `.htm` zaten textutil'e uğramaz.

Sonuç: 11 `.txt` kaynaklı çıktının tamamında Mac-Turkish imzası **yok**;
arşiv genelinde U+FFFD sayısı **0**.

```
TIP E-BOOK LARI AÇABİLMENİZ İÇİN LİT PROGRAMININ KURULU OLMASI GEREKİR.
Bu bir örnek satır
```

---

## Doğrulama özeti

| Kontrol | Sonuç |
|---|---|
| Arşiv bütünlüğü (önce/sonra) | 692 dosya / 270 dizin — **değişmedi** |
| Çıktı `.md` | 308 |
| >800 ch tablo satırı olan dosya | 33 → **5** (4'ü gerçek veri tablosu, 1'i eşiğin 1 ch altında) |
| Alan kodu sızıntısı | **0** |
| Kelime-içi bozulma | **0** |
| `REPAIRED` | 6 kayıt / 6 benzersiz yol |
| `RECOVERED` | 5 kayıt / 5 benzersiz yol |
| U+FFFD | 0 |
| Test | **156 / 156** |

**Görünür kelime kaybı denetimi** (293 belge, eski↔yeni html2md): gerçek
düzyazı kaybı **yok**; kaybolan tek şeyler alan kodu kalıntıları (tırnaklı
URL/çapa argümanları), görüntülenen metin korunuyor.

---

## Endişeler / takip

1. **`<br>` paragraflaması.** `CPU.doc` gövdesi kaynakta tek `<p>` içinde 44
   `<br>` ile yazılmış; `<br>` boşluğa indirgeniyor. Tablo satırı sorunu
   çözüldü ve başlık geri geldi, ama makale hâlâ tek uzun paragraf. Arşiv
   geneline dokunan bir değişiklik olduğu için bu turun kapsamına alınmadı.

2. **Dosya adlarında uzantı kalıntısı.** F6 yalnızca H1'i kapsıyordu (brief'te
   böyle tanımlı). `slugify` değişmediği için şu üç dosya adı hâlâ uzantı
   taşıyor: `Bilgisayar-Aglarinda-Temel-Kavramlar-Doc.md`,
   `Quickbasickursu-Pdf.md`, `Access-Veri-Tabani-Doc.md`. Tutarlılık için
   istenirse ayrı bir tur.

3. **F7 dışı kodlama artıkları** (ayrı, önceden var olan sorunlar):
   * `HTML-Notlari-2.md` (`css-2.pdf`) — LaTeX üretimi PDF; PDFKit birleşen
     aksanları ayrı çıkarıyor (`Giri¸s` = ş, `¨onemli` = ö). PDF çıkarım
     katmanı sorunu, `.txt` kodlama tespiti değil.
   * `Pascal-1.md` (`... bornova_ege_edu_tr.htm`) — kaynak `.htm` uzantılı ama
     gövdesi ikili/sıkıştırılmış veri; `read_htm` son çare dalına düşüyor.
   * `Photoshop.md` — `« Geri` gerçek bir kılavuz tırnak (orijinaldeki "Geri"
     düğmesi), bozulma değil.

4. **`Network-Temelleri.md:628`** — 799 karakterlik tek hücreli sarmalayıcı,
   eşiğin 1 karakter altında. Eşiği düşürmek 500-800 bandındaki 37 tabloyu da
   etkileyeceği için kanıt seyrekleşene kadar dokunulmadı.
