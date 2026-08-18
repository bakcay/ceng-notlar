# BIOS Sesli Hata Uyarılarının Ve POST Mesajlarının Anlamı Ve Çözümü

## **BIOS Sesli Hata Uyarılarının ve POST Mesajlarının Anlamı ve Çözümü******

Normal bir boot işlemi esnasında sizin düğmeye basmanızla birlikte önce bilgisayarın bütün bileşenlerine güç verilir, ekran kartınız hemen kendi reklamını yapar ve POST ekranına gelirsiniz. Burada, anakartınız “Aabi bakalım bana neler takılıymış” havalarında bütün bileşenleri ufak bir teste tabi tutar. Size bu sırada ekranda işlemcinizin hızı, ram miktarınız gibi bazı bilgiler verilir. İşletim sisteminin yüklenmeye başlamasından hemen önce ekrana (eğer ben yeterince hızlıyım diyorsanız Pause tuşuna basarak istediğiniz kadar seyredebileceğiniz) bir tablo gelir. Bu tabloda kabaca POST işleminin sonuçlarını görürsünüz diyebiliriz. Peki ya normal bir boot gerçekleşmezse?

Bilgisayarın başlamasını engelleyecek herhangi bir hatada ya sesli ya da POST hata mesajları alırsınız. İyimser olmanın bir alemi yok. Sesli hata mesajları genellikle ölümcül, POST mesajları ise genellikle uyarı niteliğindedir. Genellikle diyorum çünkü, ekran kartı arızasını işaret eden bir sesli hat mesajı sadece ekran kartınızın yerinden oynamasıyla da ortaya çıkabilir.

|  | **Hata** | **Anlamı** |
| --- | --- | --- |
| 1 | Sürekli Ses | Güç kaynağı arızası |
| 2 | Birçok kısa bip | Anakart arızası |
| 3 | 1 uzun | Bellek tazelenmesinde hata |
| 4 | 1 uzun 1 kısa | Anakart veya BIOS çipi arızası |
| 5 | 1 uzun 2 kısa | Ekran kartı arızası (Genellikle eski kartlardaki DIP switch kaynaklıdır) |
| 6 | 1 uzun 3 kısa | Ekran kartı arızası |
| 7 | 2 uzun 1 kısa | Ekran kartı arızası (RAMDAC kaynaklı (?) ) |
| 8 | 2 kısa | Bellek parity (eşlik) hatası |
| 9 | 3 kısa | Belleğin ilk 64k’lık bölümünde hata |
| 10 | 4 kısa | Timer hatası |
| 11 | 5 kısa | İşlemci hatası |
| 12 | 6 kısa | Klavye işlemcisi hatası |
| 13 | 7 kısa | İşlemci hatası |
| 14 | 8 kısa | Ekran kartı belleğinde okuma/yazma hatası |
| 15 | 9 kısa | BIOS ROM hatası |
| 16 | 10 kısa | CMOS okuma/yazma hatası |
| 17 | 11 kısa | Tampon Bellek Hatası |

1. hata için, güç kaynağınızın bağlantılarını kontrol edip bir deneme daha yapın. Eğer sorun devam ediyorsa, üç vakte kadar size yeni bir güç kaynağı gelecek demektir.

2, 4, 10, 12, 15 e 16 numaralı hatalar için, tüm kartları işlemciyi ve RAM’leri söküp tekrar takın. Öncelikle mümkün olduğunca az bileşenle bilgisayarı başlatmaya çalışın. 4, 15 ve 16 numaralı hatalarda BIOS çipinin yerine düzgünce oturduğundan emin olmak için üstüne hafifçe bastırın. Değişen bir şey yoksa 4, 15 ve 16 numaralı hatayla karşı karşıyaysanız yeni bir BIOS çipi edinin, yok eğer değilseniz zaten yeni bir anakartınız olacağınız için BIOS çipiniz otomatik olarak değişmiş olacaktır.

3, 8 ve 9 numaralı hatalarla baş etmek için öncelikle RAM’lerinizin yerlerine düzgün oturduklarından ve yuvalarla aralarında herhangi bir yabancı maddenin bulunmadığından emin olun. Eğer birden fazla bellek modülü kullanıyorsanız değişik kombinasyonlar deneyin. Hata hala devam ediyorsa belleklerinizi tek tek deneyerek sorunun hangisi/hangilerinde olduğunu bulabilirsiniz.

5, 6 ve 7 numaralı mesajı alıyorsanız, ekran kartınızın yerine iyice oturduğundan ve monitör bağlantısının düzgünce bir şekilde yapıldığından emin olun. Problem sürüyorsa başka bir ekran kartı ile bilgisayarı başlatmayı deneyin. Sonuç alırsanız sizi tebrik ederiz çok yakın bir zamanda yepyeni bir ekran kartınız olacak. Ekran kartlarıyla ilgili alacağınız sesli hata mesajlarının neredeyse tamamı 6 numara olacaktır. Bu nedenle şimdiden “diii di dit dit” sesine alışmanızda fayda var.

11, 13 ve 17 numaralı hatalar için işlemcinizin düzgün bir şekilde takıldığından emin olun. Mümkünse başka bir işlemciyle denemelerde bulunun, sonuç alamazsanız özellikle 17 numaralı hata için anakartınızdan şüphelenin.

**POST Mesajları**

**BIOS ROM checksum error - System halted: **BIOS çipindeki bir hatayı gösterir. Çipte fiziksel hata veya BIOS yazılımında bozukluk olabilir. Sisteminizi yeni bir BIOS ile update edin, sorun devam ediyorsa yeni bir BIOS çipi edinmeniz gerekecek.

**CMOS battery failed: **BIOS piliniz bitmiş veya bitmek üzere. Pilin türünü belirleyip en yakın saatçiden yenisini alabilirsiniz.

**CMOS checksum error - Defaults loaded: **Herhangi bir nedenden dolayı BIOS ayarlarınızda bozukluk oluşmuş (muhtemelen bitmek üzere olan BIOS pili yüzünden). Varsayılan ayarlar yüklenerek sisteminizin zarar görmesi engellenmiş.

**Floppy disk(s) fail: **Sisteminize takılı bulunan disket sürücü(ler) ile BIOS’taki disket sürücü ayarları birbirini tutmuyor. Disket sürücünüzün bağlantılarını kontrol edin, BIOS’taki ayarlar yanlışsa düzeltin. Sorun devam ediyorsa disket sürücünüzde muhtemel bir fiziksel arıza var demektir.

**Keyboard error or no keyboard present: **Belki de en çok karşılaşılan POST mesajı. Bu mesaj genellikle “Press F1 to continue” diye devam eder. Siz de olmayan klavyenin F1 tuşuna basarak hatadan kurtulabilir veya yeni bir klavye takarak işleme devam edebilirsiniz.

**Memory test fail: **POST mesajlarının belki de en can sıkıcısı. BIOS’taki bellek ayarlarınızda olabilecek bir problemden kaynaklanabildiği gibi, bellek modüllerinizdeki kısmi (kısmi=belli bir bölümündeki) arıza nedeniyle de ortaya çıkailir. Ayarlarınızdan eminseniz, başka bir bellek ile sisteminizi tekrar açmayı deneyin.

**Hard Disk(s) Fail: **Sisteminizde mevcut disk(ler)le BIOS’ta belirilmiş disk ayarları birbirini tutmuyor demektir. BIOS’tan disk ayarlarını otomatiğe getirin, master/slave ayarlarını kontrol edin. Sorun devam ediyorsa disk sürücünüzde fiziksel bir bozukluk kuvetle muhtemeldir.

Bunlar POST hatalarının sadece belli başlı olanları. Sistem-spesifik olarak hata mesajları ile karşılaşabileceğinizi tekrar hatırlatmamda bir sakınca yok.

## Seçil Bursa 2001215011 13.10.2003

## PAGE

## PAGE 1

---
*Kaynak: `BIOS Sesli Hata Uyarılarının ve POST Mesajlarının Anlamı ve Çözümü/BIOS Sesli Hata Uyarılarının ve POST Mesajlarının Anlamı ve Çözümü.doc` — secill — 2004*
