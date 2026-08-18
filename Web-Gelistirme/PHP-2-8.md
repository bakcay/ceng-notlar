# PHP 2

[](http://www.e-dersane.com)

[](javascript:history.go(-1))

[](PHP-2-13.md)

[](PHP-2-9.md)

**
Personel Web Server Kurulumu ve Php Kurulumu For Win. 95-98**

Herkese merhaba, daha önceki yazımızda *Apache Web Sunucusu*'nu nasıl kuracağımızı ve *PHP*'yi nasıl çalışır hale getirebileceğimizi incelemiştik, bu sefer de Microsoft'un *Internet Information Server*'ının (IIS) kırpılmış hali olan *PWS*'yi inceleyeceğiz. Eger script dilleriyle daha önceden ilgilendiyseniz büyük ihtimalle PWS ile ilgili bir deneyiminiz olmuştur, ben ilk önce PWS'nin kurulumunu anlatacağım, zaten bende kurulu diyorsanız bu bölümü atlayıp direk PHP'nin ayarlanmasına geçebilirsiniz.

PWS'yi Microsoft'un sitesinden indirebilirsiniz. Programı indirdikten sonra *Kur*'u çalıştırın. Sizden *Kisa/Özel/Normal* arasında bir seçim yapmanızı isteyecek. *Normal*'i seçip devam edin. Hangi dizine kopyalamak istediğinizi belirledikten sonra dosyalar kopyalanacak ve bilgisayarınız yeniden başlatılacak.

PWS kurulumunda sıkça karşılaşılan bir problem *Transaction Server*'in kopyalanmasında oluşan hatadır. Registry'nin çok şişik olduğu sistemlerde bu hata meydana geliyor. PHP için bu hizmete ihtiyacımız yok, bu hatayı es geçebilirsiniz. İlla onaracağım derseniz, Microsoft'un sitesinden gerekli bilgiye ulaşabilirsiniz.

Bilgisayar yeniden başladıktan sonra sistem çubuğunda PWS'nin ikonun yer aldığını göreceksiniz. Bu ikonun üzerine sağ tıklayıp sunucuyla ilgili yönetim işlemlerini yapabilirsiniz. Buradan *Hizmeti Başlat* seçeneğini seçin. Tarayıcınızı çalıştırın ve adres satırına *localhost *yazn. PWS'nin tanıtım ekrannı gördüyseniz bu işi becerdiniz demektir. Eğer hata mesajı alıyorsanız yukardaki adımları tekrar inceleyin, sonuç alamazsanız PWS'yi kaldırıp tekrar kurun.

Windows 95/98 Registry Ayarları

PHP'yi PWS ile beraber kullanabilmek için registry'de değişiklikler yapmamız gerekli. Bu ayarları yaparken dikkatli olmalısınız, yanlış bir işlem bilgisayarınızdaki programlara zarar vermenize neden olabilir. Ben yapmanız gerekenleri adım adım anlatacağım. Yapacağım bütün değişiklikleri PHP'yi *C:\\PHP3* klasörüne yüklemiş olduğunuzu kabul ederek anlatacağım, eğer siz farklı bir klasör kullanıyorsanız değişiklikleri buna göre yapmaya dikkat edin.

Başlat | Çalıştır | regedit

Buradan *HKEY\_LOCAL\_MACHINE*'in içine girin ve aşağıdaki yolu bulun :

System | Current Control Set | Services | W3Svc | Parameters | Script Map

Düzen | Yeni | Dize Değeri (String Value) seçin.

Buraya *.php3 yazın. *

Bu değerin üstüne sağ tuş ile tıklayıp *Değiştir*'i seçin.

Değer verisi yazan yere *C:\\PHP3\\php.exe %s %s *satırını ekleyin.

En başa *HKEY\_CLASSES\_ROOT* bölümüne dönün.

Düzen | Yeni | Tuş seçtikten sonra buraya *.php3* yazın.

Önceki sefer yaptığınız gibi *Değiştir*'i seçip değer verisi olarak *phpfile* yazın.

Düzen | Yeni | Tuş seçtikten sonra buraya *phpfile* yazın.

Değer verisi yerine *PHP3 Script* yaın. z

*phpfile*'in üstüne sağ tıklayın, Düzen | Yeni | Tuş seçin ve adın *Shell* koyun.

*Shell*'in üstüne sağ tıklayın, Düzen | Yeni | Tuş seçtikten sonra buraya *Open* yazın.

Open'in üstüne sağ tıklayın, Düzen | Yeni | Tuş seçtikten sonra buraya *Command* yazın.

Varsayılan değer yerine *C:\\PHP3\\php.exe -q %1* yazın. ('l' sayı değil harf)

Registry kullanıma hazır. Son olarak PHP klasöründe yer alan *php3.ini-dist* dosyasını düzenleyeceğiz. Bu dosya PHP dosyalarını nereye kopyaladıysanız orada yer almakta (PHP dosyalarını kopyalamak için ekstra bir işlem yapmanıza gerek yok, sadece ZIP dosyasını bilgisayarınıza kopyalayıp açmanız yeterli). *Notepad*'i çalıştırın ve *php3.ini-dist* dosyasını açın. Burada *extension\_dir* satırını bulun ve karşısına *C:\\PHP3* (ya da dosyalarınız hangi klasördeyse orası) yazın. Daha sonra *Windows Extensions* bölümünü bulun. Burada PHP ile beraber kullanabileceğimiz programların kütüphane dosyaları yer almakta. Bunların içinden *extension=php3\_mysql.dll* satırının başındaki ';' işaretini kaldırarak *MySQL* kütüphanesini aktif hale getirin. Son olarak dosyayı *C:\\Windows\\php3.ini* (dosyanın adının değişmesine dikkat edin) olarak kaydedin ve notepad'den çıkın.

Artık PWS ile ilk PHP programımızı test edebiliriz. Önce PWS'de kendimize bir çalışma klasörü yaratalım. Sistem çubuğundaki PWS ikonuna tıklayıp *Özellikler*'i seçin. Karşımıza PWS'nin Ana ekranı çıkacak. Yine bu ekrandan PWS'yi başlatıp durdurabilirsiniz. Sol taraftaki menüden *Gelişmiş*'i seçin. *Home*'un üstüne gelin ve sağ taraftan *Ekle*'yi seçin. Burada *Diğer Ad* (Alias) ile klasörünüze bir takma ad belirleyin. Biz baslangıç olarak *php* diyelim. Alttaki seçeneklerden *Okuma *ve* Yürütme*'nin seçili olduğundan emin olun.

Notepad'i tekrar çalıştırıp ilk PHP kodumuzu yazalım :

**Örnek Kod 1.1**

<?
echo phpinfo();
?>

Bu kodu biraz önce yarattığımız klasöre test.php3 olarak kaydedelim. Şimdi PWS'nin çalışır halde olduğundan emin olun, tarayıcınızı çalıştırın ve localhost/php/test.php3 yazın. Karşınıza PHP ile ilgili bilgiler çıktıysa başardınız demektir...

[](javascript:history.go(-1))

[](PHP-2-13.md)

[](PHP-2-9.md)

[ ](javascript:window.external.AddFavorite('http://www.e-dersane.com','E-DERSANE.com - Internetle Yasamayi Ogretir!'))

Copyright © 2001- **[www](http://www.e-dersane.com)**[.**E-Dersane.com**](http://www.e-dersane.com)** - Offline Dersler**. All Rights Reserved.
**[](http://www.e-dersane.com)****[](http://www.php.org.tr)****PhP Offline Dersleri **bolumunde yayinlanan bütün metin ve makaleler GPL lisansli olup ayrintili bilgi için [GNU.org](http://www.gnu.org) adresine bakiniz.

---
*Kaynak: `PHP 2/ekitap-Anonim-PHP_Offline/ders5.htm`*
*Görseller: `PHP-2/gorseller/` (1 dosya)*
