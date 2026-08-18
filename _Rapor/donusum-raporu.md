# Dönüşüm Raporu

Bu rapor, kaynak arşivdeki her dosyaya ne olduğunu anlatır.
**Kaynak arşive hiç dokunulmadı**: hiçbir dosya silinmedi, taşınmadı veya değiştirilmedi. Aşağıdaki her şey `MD/` klasörünün içinde, kaynağın kopyası üzerinde yapıldı.

## Özet

| Ölçüt | Adet |
| --- | --- |
| Markdown'a çevrilen belge | 303 |
| Tekrar yönlendirme dosyası | 3 |
| Sadece ek dosya içeren konu için giriş sayfası | 2 |
| Kopyalanan kod örneği | 316 |
| Kopyalanan görsel | 34 |
| Çevrilemediği için arşivlenen dosya | 24 |
| Dönüştürülemeyen dosya (hata) | 0 |

## Dönüştürülemeyen dosyalar

Yok. Arşivdeki her belge okunabildi.

## Son çare kurtarma ile okunan belgeler

Bu belgeler normal yolla çevrildiğinde **bomboş** çıkıyordu — metinleri Word'ün gömülü nesnelerinin ya da HTML yorumlarının içinde saklıydı. Ham dosya taranarak metin kurtarıldı. İçerik birebir korundu, ancak biçimlendirme (başlık, tablo) kurtarılamadı.

- `FLASH DERSLERİ/ekitap-Anonim-Flash_Ders_111/DERS111.html` — 1755 kelime kurtarıldı
- `INTERTECH/INTERTECH.doc` — 9855 kelime kurtarıldı

## Bozuk Türkçe harflerin onarımı

Aşağıdaki **8 dosya kaynakta bozuktu**: 2004'te yanlış kod sayfasıyla kaydedildikleri için Türkçe harfler İzlandaca harflere dönüşmüştü (`İ`→`Ý`, `ş`→`þ`, `ı`→`ý`, `Ş`→`Þ`, `ğ`→`ð`, `Ğ`→`Ð`). Çıktıda bu altı harf birebir geri çevrildi; başka hiçbir karaktere dokunulmadı.

Sayılar, dosyada kaç harfin düzeltildiğini gösterir. Bu bozulmanın belge geneline yayılmış gerçek bir hasar mı yoksa tek tük yazım hatası mı olduğu ölçülerek ayrıldı: bu dosyalarda en az 173, onarılmayanlarda en fazla 3 işaret vardı.

- `EXCELL DERSLERİ/EXCEL DERSLERİ.doc` — 7547 harf onarıldı
- `PHOTOSHOP/photoshop.pdf` — 3431 harf onarıldı
- `NETWORK ( AĞ ) KAVRAMLARI/NETWORK ( AĞ ) KAVRAMLARI.doc` — 2227 harf onarıldı
- `PHOTOSHOP ARA YÜZLERİ/ekitap-Anonim-Photoshop_Aray³z.pdf` — 724 harf onarıldı
- `Çevirmeli Ağ Komut Dosyası Yazma Desteği/Çevirmeli Ağ Komut Dosyası Yazma Desteği.doc` — 692 harf onarıldı
- `DELPHI'DE ŞARTLI ÇALIŞMA VE BLOK KONTROL İŞLEMLERİ/DELPHI'DE ŞARTLI ÇALIŞMA VE BLOK KONTROL İŞLEMLERİ.doc` — 561 harf onarıldı
- `BİRDEN ÇOK DOMAİN İLE ÇALIŞMA/BIRDEN COK DOMAIN ILE CALISMA.doc` — 430 harf onarıldı
- `ICON AUTHOR YAZARLIK YAZILIMINDA HAZIRLANMASI/ICON AUTHOR YAZARLIK YAZILIMINDA HAZIRLANMASI.doc` — 173 harf onarıldı

## Word'ün açamadığı büyük belgeler

macOS'un metin dönüştürücüsü (`textutil`) aşağıdaki **5 dosyayı ayrıştıramadı**: hata vermeden çalıştı ama ürettiği metin okunaksız ikili döküntüydü. Bunlar içine resim gömülmüş, 10–34 MB'lık gerçek Word belgeleri. Metin, ham dosyanın içinden (Word'ün kendi UTF-16 gösteriminden) doğrudan kurtarıldı.

**Bu dosyalarda biçim kaybı vardır**: yazı düz metne indi, başlıklar ve tablolar korunamadı. Metnin kendisi birebir aktarıldı. Orijinal dosyalar kaynak arşivde el değmemiş durumda.

- `AĞ KURULUMU/AĞ KURULUMU.doc` — 15589 kelime kurtarıldı
- `INTERTECH/INTERTECH.doc` — 9855 kelime kurtarıldı
- `ICON AUTHOR/ICON AUTHOR 2.doc` — 6794 kelime kurtarıldı
- `KULLANICI PROFİLLERİ İLE BİREYSEL AYARLAR YAPMAK/KULLANICI PROFİLLERİ İLE BİREYSEL AYARLAR YAPMAK.doc` — 4685 kelime kurtarıldı
- `VISUAL BASIC MENÜLERİ/VISUAL BASİC MENÜLERİ.doc` — 2872 kelime kurtarıldı

## Kodlaması yanlış bildirilen web sayfaları

Bir `.htm` dosyası hangi kod sayfasıyla yazıldığını kendi içinde bildirir. Aşağıdaki **2 sayfada bu bildirim yanlıştı** ya da hiç yoktu; sayfa, doğru sonucu veren ilk kodlamayla okundu.

Bu liste yalnızca Markdown'a **çevrilen** web sayfalarını kapsar. E-kitap paketlerinin içindeki çalışan `.htm` örnekleri hiç çözümlenmedi; onlar bayt bayt kopyalandığı için kodlama sorunundan etkilenmezler.

Hiçbirinde karakter kaybı olmadı — hepsi tam çözüldü.

| Dosya | Bildirilen | Kullanılan |
| --- | --- | --- |
| `FLASH DERSLERİ/ekitap-Anonim-Flash_Ders_111/DERS111.html` | — | windows-1254 |
| `PASCAL/Pascal Hakkynda Döküman 2 - bornova_ege_edu_tr.htm` | windows-1254 | iso-8859-9 |

## 300 kelimenin altındaki belgeler (33)

Bunlar önsöz, içindekiler veya tek sayfalık kalıntı belgelerdir — kaynakta da bu kadar kısadırlar. Hiçbiri silinmedi, bilgi amaçlı listeleniyor.

- `Web-Gelistirme/CGI-Perl-Kullanimi-5.md` — 4 kelime
- `Ag-ve-Iletisim/IP-Adresleri-Ve-Alt-Aglar-2.md` — 19 kelime
- `Programlama/Java-Programlama-Dili-2.md` — 22 kelime
- `_Arsiv/Tip.md` — 22 kelime
- `Programlama/Java-Programlama-Dili-3.md` — 23 kelime
- `Programlama/Java-Programlama-Dili-11.md` — 25 kelime
- `Programlama/Java-Programlama-Dili-4.md` — 28 kelime
- `Web-Gelistirme/Perl-Ve-CGI-1.md` — 33 kelime
- `Grafik-ve-Tasarim/Autocad-Ders-Notlari-3.md` — 42 kelime
- `Web-Gelistirme/PHP-Devam-2.md` — 50 kelime
- `Programlama/Java-Programlama-Dili-13.md` — 58 kelime
- `Web-Gelistirme/CGI-Perl-Kullanimi-2.md` — 65 kelime
- `Programlama/Java-Programlama-Dili-7.md` — 66 kelime
- `Programlama/Java-Programlama-Dili-5.md` — 68 kelime
- `Grafik-ve-Tasarim/Autocad-Ders-Notlari-1.md` — 71 kelime
- `Programlama/Java-Programlama-Dili-1.md` — 76 kelime
- `Web-Gelistirme/CGI-Perl-Kullanimi-3.md` — 81 kelime
- `Programlama/Java-Programlama-Dili-6.md` — 81 kelime
- `Web-Gelistirme/Perl-Ve-CGI-2.md` — 91 kelime
- `Web-Gelistirme/PHP-2-1.md` — 94 kelime
- `Donanim/Donanim.md` — 128 kelime
- `Web-Gelistirme/PHP-2-13.md` — 139 kelime
- `Programlama/Mobil-Uygulamalari-1.md` — 151 kelime
- `Ofis-Yazilimlari/Arac-Cubuklari.md` — 158 kelime
- `Programlama/Java-Programlama-Dili-9.md` — 172 kelime
- `Elektronik/PIC-1-Ve-PIC-2-2.md` — 174 kelime
- `Web-Gelistirme/Perl-Ve-CGI-4.md` — 189 kelime
- `Programlama/Java-Programlama-Dili-8.md` — 260 kelime
- `Programlama/Hedef-Programlama-1.md` — 262 kelime
- `Programlama/Visual-Basic-5-0in-Getirdigi-Yenilikler.md` — 271 kelime
- `Web-Gelistirme/Flash-Dersleri-Mask-Teknigi.md` — 275 kelime
- `Programlama/Java-Programlama-Dili-10.md` — 288 kelime
- `Grafik-ve-Tasarim/Icon-Author-Yazarlik-Yaziliminda-Hazirlanmasi.md` — 293 kelime

## Adı değiştirilen ek dosyalar (17)

Dosya adında Türkçe harf, boşluk veya noktalama olduğu için çıktıda ASCII bir adla yazıldılar. İçerikleri aynıdır.

- `Aesop - Fables.lit` → `Aesop-Fables.lit`
- `Bram Stoker - Dracula.lit` → `Bram-Stoker-Dracula.lit`
- `Edgar Alan Poe - The Gold Bug.lit` → `Edgar-Alan-Poe-The-Gold-Bug.lit`
- `Francis Bacon - New Atlantis.lit` → `Francis-Bacon-New-Atlantis.lit`
- `HG Wells - The Island of Doctor Moreau.lit` → `HG-Wells-The-Island-of-Doctor-Moreau.lit`
- `Html Kitabı.chm` → `Html-Kitabi.chm`
- `Lewis Carroll - Alices Adventures in Wonderland.lit` → `Lewis-Carroll-Alices-Adventures-in-Wonderland.lit`
- `Mark Twain - Tom Sawyer.lit` → `Mark-Twain-Tom-Sawyer.lit`
- `Microsoft SQL JET Basvurusu.chm` → `Microsoft-SQL-JET-Basvurusu.chm`
- `Robert Louis Stevenson - The Strange Case of Dr Jekyll and M.lit` → `Robert-Louis-Stevenson-The-Strange-Case-of-Dr-Jekyll-and-M.lit`
- `Washington Irving - The Legend of Sleepy Hollow.lit` → `Washington-Irving-The-Legend-of-Sleepy-Hollow.lit`
- `William Shakespeare - King Lear.lit` → `William-Shakespeare-King-Lear.lit`
- `ekitap-Anonim-XML/xml_dosyalar/FILELIST.XML` → `FILELIST-2.XML`
- `ekitap-Hakki_Ícal-Kitap_ik_PHP_÷rnekler/PHP Hosting Companies Search the Directory.htm` → `PHP-Hosting-Companies-Search-the-Directory.htm`
- `ekitap-Hakki_Ícal-Kitapcik_CGI_Perl_ekler.rar` → `ekitap-Hakki_Ical-Kitapcik_CGI_Perl_ekler.rar`
- `ekitap-Hakki_Ícal-Kitapcik_Javascript_÷rnekler.rar` → `ekitap-Hakki_Ical-Kitapcik_Javascript_-rnekler.rar`
- `html notları/html notları/html2000.chm` → `html2000-2.chm`

## Nasıl doğrulandı

`verify.py` her dönüşümden sonra altı kontrol çalıştırır: kelime sayısı korunumu, Türkçe karakter bütünlüğü, dosya adı geçerliliği, kayıp dosya olmaması, bağlantı bütünlüğü ve boş çıktı olmaması.
