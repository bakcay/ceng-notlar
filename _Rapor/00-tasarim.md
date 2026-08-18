# Arşiv Markdown Dönüşümü — Tasarım

**Tarih:** 2026-08-13
**Kaynak:** `~/Downloads/Bilgisayar Bilgileri/` — 691 dosya, 187 MB, 250 konu klasörü
**Hedef:** `~/Downloads/Bilgisayar Bilgileri/MD/`

---

## 1. Amaç

1998–2004 arası Türkçe bilgisayar ders notları / e-kitap arşivini, içeriğine dokunmadan
okunabilir ve gezilebilir bir Markdown koleksiyonuna çevirmek.

Metin **birebir korunur**. Yapılan iş yalnızca biçim dönüşümü, isim düzeltmesi ve
kategorilendirmedir. Özetleme, yeniden yazım, güncelleme yoktur.

## 2. Kaynak envanteri

| Tip | Adet | İşlem |
|---|---|---|
| `.doc` (Word 97, CP1254) | 247 | `textutil` → HTML → Markdown |
| `.htm` / `.html` | 188 | Windows-1254 → UTF-8 → Markdown. Örnek klasörlerindekiler hariç, bkz. §8 |
| `.php .asp .pl .inc .cgi .js .java .x .lib` | 154 | Dönüştürülmez, `ornekler/` altında orijinal kalır |
| `.gif` | 34 | `gorseller/` altına kopyalanır |
| `.pdf` | 16 | Metne çevrilir + orijinal PDF yanına konur |
| `.txt` / `.rtf` | 13 | Doğrudan Markdown |
| `.lit` | 10 | `_Arsiv/` (İngiliz edebiyatı, arşive ait değil) |
| `.chm .rar .mdb .swf .dump .get` | 14 | `_Arsiv/` altına kopyalanır |

Toplam metin hacmi: `.doc` dosyalarında **1.288.962 kelime** (~4.500 sayfa), artı `.htm` ve PDF.

## 3. Tespit edilen problemler

**P1 — Dosya adları mojibake, klasör adları temiz.**
Dosya adlarında DOS/CP857 → UTF-8 bozulması var (`ü→³`, `Ö→Í`, `ö→÷`, `ç→_`, `ı→i`).
Örnek: `ekitap-Anonim-Ag_Y³klemesi_I_in_Daha_Fazla_Planlama.doc`.
Klasör adları ise doğru UTF-8 Türkçe: `AĞ YÜKLEMESİ İÇİN DAHA FAZLA PLANLAMA`.
→ **Karar:** Başlık kaynağı klasör adıdır. Mojibake çözülmeye çalışılmaz.

**P2 — İsimsiz dosyalar.**
~15 dosya `Odevsitesi_com_32467.doc` / `O-d-e-v-s-i-t-e-s-i-com-19135.doc` biçiminde.
→ P1 ile aynı çözüm: klasör adı kullanılır.

**P3 — Doküman içi başlıklar güvenilmez.**
`textutil -convert html` çıktısındaki `<title>` 247 dosyanın 201'inde dolu, ancak Word
şablonundan devralınan yanlış başlıklar var (`VERİ TABANI ÜZERİNE` → `HTML Nedir`,
`EXCELL 2000 FULL KİTAP` → `Word2000`).
→ **Karar:** `<title>` başlık olarak kullanılmaz. `Author` ve `CreationTime` metadata'sı
kaynak dipnotunda kullanılır.

**P4 — İki katmanlı tekrar.**
- Birebir aynı dosya: 22 grup, 1.8 MB. (`HTML NOTLARI/html notları/html notları/` kendi içine kopyalanmış.)
- Aynı metin, farklı binary: md5 tutmuyor ama boşluksuz metin hash'i aynı.
  Doğrulanmış çiftler: `CIFT ANAHTARLI BILGI GUVENLIGI` = `ÇİFT ANAHTARLI BİLGİ GÜVENLİĞİ` (820 kelime),
  `DNS - DOMAIN MAIN SYSTEM` = `DNS,DOMAIN NAME SYSTEM ( DOMAIN ISIM SISTEMI)` (2166 kelime).

**P5 — Konu örtüşmeleri (tekrar değil).**
E-ticaret 5 farklı metin (5.088 / 7.059 / 12.367 kelime…), Visual Basic 12, XML 4, Pascal 4, Virüsler 2.
İçerikleri farklı → birleştirilmez.

**P6 — `TIP` klasörü arşive ait değil.**
10 `.lit` İngiliz klasiği (Dracula, King Lear, Tom Sawyer…) + `LÜTFEN OKUYUN.txt`.

**P7 — 12 dosya 300 kelimenin altında.**
Önsöz / içindekiler / kalıntı sayfalar (`acadaralik.doc` 42 kelime, `KAYNAKÇA.doc` 33 kelime).

## 4. Dokunulmazlık kuralı

Kaynak arşivin 250 klasörünün hiçbiri **silinmez, taşınmaz, yeniden adlandırılmaz**.
Tüm çıktı `MD/` altına yazılır. Geri alma yöntemi: `MD/` klasörünü silmek.

## 5. İsimlendirme

Türkçe kelimeler, ASCII karakterler. Sabit dönüşüm tablosu:

```
ç→c  Ç→C    ğ→g  Ğ→G    ı→i  I→I
İ→I  ö→o    Ö→O  ş→s    Ş→S  ü→u  Ü→U
```

Ek kurallar:
- Kelimeler `Title-Case`, aralar tire: `Ag-Yuklemesi-Icin-Daha-Fazla-Planlama.md`
- Noktalama (`,` `'` `(` `)` `.`) atılır, ardışık tireler teke iner
- Sonuç yalnızca `[A-Za-z0-9-]` içerir

Örnekler:

| Kaynak | Çıktı |
|---|---|
| `İŞLETİM SİSTEMLERİ/Odevsitesi_com_32195.doc` | `Isletim-Sistemleri/Isletim-Sistemleri.md` |
| `AĞ YÜKLEMESİ İÇİN.../ekitap-Anonim-Ag_Y³klemesi....doc` | `Ag-ve-Iletisim/Ag-Yuklemesi-Icin-Daha-Fazla-Planlama.md` |
| `PHP - DEVAM/ekitap-Hakki_Ícal-Kitap_ik_PHP.doc` | `Web-Gelistirme/PHP-Kitapcigi.md` |
| `DNS,DOMAIN NAME SYSTEM ( DOMAIN ISIM SISTEMI)/...` | `Ag-ve-Iletisim/DNS-Domain-Name-System.md` |

## 6. Kategoriler

Numarasız, alfabetik. 13 konu kategorisi + 2 servis klasörü.

| Klasör | Yaklaşık | Kapsam |
|---|---|---|
| `Ag-ve-Iletisim` | 24 | TCP/IP, OSI, DNS, LAN/WAN, ISDN, DSL, Ethernet, router, kablosuz |
| `Bilisim-ve-E-Ticaret` | 13 | E-ticaret, bilişim dünyası, ISO 9001, MIS, mobil, ODTÜ Teknokent |
| `Donanim` | 19 | Anakart, CPU, bellek, ses kartı, çevre birimleri, BIOS, RAID, DVD, A+ |
| `Elektronik` | 11 | AC-DC, FIR filtre, PIC, PLC, mikrokontrolör, mekatronik, sayısal elektronik |
| `Grafik-ve-Tasarim` | 12 | 3D Max, AutoCAD, Photoshop, Corel, Icon Author, MIDI |
| `Guvenlik` | 10 | Virüs, kriptografi, hacker tarihi, bilişim suçları, firewall, yedekleme |
| `Isletim-Sistemleri` | 16 | DOS, Windows 2000/NT, Linux, UNIX, Minix, disk/dosya komutları |
| `Ofis-Yazilimlari` | 8 | Excel, Word, MS Project, Office genel |
| `Programlama` | 40 | C/C++/C#, Java, Pascal, Delphi, Visual Basic, Assembler, algoritma, veri yapıları |
| `Sozluk-ve-Referans` | 10 | Terim sözlükleri, bilgisayar İngilizcesi, genel giriş metinleri |
| `Veritabani` | 18 | Access, SQL, MySQL, Oracle, dBase, VTYS kavramları |
| `Web-Gelistirme` | 42 | HTML, CSS, ASP/ASP.NET, PHP, Perl/CGI, JavaScript, XML, FrontPage, Flash |
| `Yapay-Zeka` | 2 | Yapay zeka, yapay sinir ağları |
| `_Arsiv` | 25 | Dönüştürülemeyen formatlar |
| `_Rapor` | — | Bu tasarım + dönüşüm raporu + tekrar raporu |

Sınırda kalan konular tek bir kategoriye atanır, ikinci kategoride `INDEX.md` üzerinden
çapraz referans verilir.

## 7. Dosya biçimi

```markdown
# Sabit Diskler

...metin birebir, Word artıkları temizlenmiş, başlıklar/listeler/tablolar
Markdown karşılığına çevrilmiş...

---
*Kaynak: `PC SORUNLARINA KOLAY ÇÖZÜMLER/PC SORUNLARINA KOLAY ÇÖZÜMLER.doc` — Fatih Yılmaz, 2004*
```

- H1 = klasör adından türetilmiş başlık (Türkçe karakterlerle, okunabilir haliyle)
- Gövde = birebir metin
- En altta tek satır kaynak dipnotu (orijinal yol + varsa `Author` + yıl)
- YAML frontmatter **yok** (kullanıcı tercihi: sadece format)

**Dönüşüm zinciri:** `.doc/.rtf` → `textutil -convert html -encoding UTF-8` → HTML temizleme
→ Markdown. Düz metin (`-convert txt`) yerine HTML üzerinden gidilmesinin sebebi: CSS font
boyutlarından başlık hiyerarşisi, `<table>`, `<ul>`/`<ol>` yapıları kurtarılabiliyor.

`.htm` kaynaklar: `iconv -f WINDOWS-1254 -t UTF-8` → aynı temizleme → Markdown.

**HTML temizleme kuralları:**
- `<style>`, `<script>`, `<o:p>`, `<v:*>`, Word `xmlns:*` namespace'leri atılır
- `class="MsoNormal"` vb. tüm sınıf/stil öznitelikleri atılır
- Font boyutu ≥ 14px ve/veya `<b>` ile sarılı tek satırlık paragraflar → `##` başlık
- `<table>` → Markdown tablo (hücre içi satır sonu `<br>` olarak korunur)
- Ardışık boş paragraflar teke iner, satır sonu `\n` (CRLF değil)
- `INCLUDEPICTURE`, `MERGEFORMATINET`, alan kodu kalıntıları temizlenir

## 8. Ekleri olan konular

Kitap + çalışan kod paketi olan 5 klasör: `PHP - DEVAM` (101 dosya),
`JAVA SCRİPT - DEVAMI` (81), `WEB DERSLERİ - HTML` (75), `ASP BOOK ÖRNEKLER` (53),
`CGI-PERL KULLANIMI` (37).

```
Web-Gelistirme/
  PHP-Kitapcigi.md
  PHP-Kitapcigi/
    ornekler/      ← .php .asp .pl .js .inc .x .lib .dump, orijinal adlarıyla
    gorseller/     ← .gif
```

Kod dosyaları Markdown'a gömülmez. `.md` dipnotuna
`Örnekler: PHP-Kitapcigi/ornekler/ (68 dosya)` satırı eklenir.

Örnek klasörlerindeki `.htm` dosyaları (form örnekleri vb.) da kod sayılır, `ornekler/`
altında kalır — Markdown'a çevrilmez.

## 9. Tekrar politikası

| Durum | İşlem |
|---|---|
| Birebir aynı dosya (md5) | Tek kopya. Diğerleri `_Rapor/tekrarlar.md`'de listelenir. |
| Aynı metin, farklı binary | Kelime sayısı fazla olan asıl. Diğeri tek satırlık yönlendirme `.md`'si: `Bu içerik [X](../yol/X.md) ile aynıdır.` |
| Aynı konu, farklı metin | Dokunulmaz. Hepsi ayrı dosya. `INDEX.md`'de yan yana listelenir. |

Metin karşılaştırması: `textutil -convert txt` çıktısından tüm boşluklar atılıp SHA-256.

## 10. Dönüştürülemeyen formatlar

```
_Arsiv/
  Ingiliz-Edebiyati-Lit/     ← 10 .lit + LÜTFEN OKUYUN.txt (TIP klasörü)
  Chm/                       ← 4 .chm (HTML Kitabı, SQL JET, html2000, VB Tips)
  Rar/                       ← 4 .rar (örnek arşivleri)
  Mdb/                       ← 2 .mdb (ASP Book veritabanları)
  Diger/                     ← .swf
  README.md                  ← her dosyanın ne olduğu, nereden geldiği, nasıl açılacağı
```

Kopyalanır, taşınmaz. PDF'ler bu klasöre girmez — metne çevrilir (§2), orijinal PDF ilgili
kategori klasöründe `.md`'nin yanında durur.

## 11. Üretilecek raporlar

- `MD/INDEX.md` — 13 kategori, altında alfabetik konu listesi, her satırda kelime sayısı ve link
- `MD/_Rapor/donusum-raporu.md` — dönüşen/atlanan dosya sayıları, hata alanlar, 300 kelime altı dosyalar (P7)
- `MD/_Rapor/tekrarlar.md` — md5 tekrarları ve metin tekrarları, hangi dosya asıl seçildi
- `MD/_Arsiv/README.md` — arşiv içeriği açıklaması

## 12. Doğrulama

Dönüşüm tamamlandığında kontrol edilecekler:

1. **Kelime sayısı korunumu** — her `.md`'nin kelime sayısı, kaynağın `textutil -convert txt`
   kelime sayısının %90'ından az olmamalı. Altında kalanlar rapora düşer.
2. **Türkçe karakter bütünlüğü** — hiçbir `.md` içinde `³ Í ÷ Ã¼ Ä± ï¿½` gibi mojibake kalıntısı olmamalı.
3. **Dosya adı geçerliliği** — tüm yollar yalnızca `[A-Za-z0-9._/-]` içermeli.
4. **Kayıp yok** — kaynaktaki her dosya ya bir `.md`'ye, ya `ornekler/`e, ya `gorseller/`e,
   ya `_Arsiv/`e karşılık gelmeli. Karşılığı olmayan dosya rapora düşer.
5. **Link bütünlüğü** — `INDEX.md` ve yönlendirme dosyalarındaki tüm göreli linkler var olan
   dosyaya işaret etmeli.

## 13. Kapsam dışı

- Metin özetleme, güncelleme, yeniden yazım
- Konu örtüşmelerinin birleştirilmesi
- Mojibake dosya adlarının ters mühendislikle çözülmesi
- Kaynak arşivde herhangi bir değişiklik
- `.chm` / `.rar` / `.mdb` / `.lit` içeriğinin açılması
