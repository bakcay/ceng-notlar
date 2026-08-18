# PHP 2

[](http://www.e-dersane.com)

[](javascript:history.go(-1))

[](index.htm)

[](ders5.htm)

****
Apache Web Sunucusu Kurulumu****

* Apache*, dünyadaki sunucu piyasasının %60'ına hakim olan en popüler Web Sunucusu'dur. Hem *Windows*, hem *UNIX* sistemler altında çalışabilmektedir. Ben Apache'i Windows altında nasıl hızlı bir şekilde kurup işler hale getirebileceğinizi anlatacağım. Apache'in en son sürümünü <http://www.apache.org> adresinden temin edebilirsiniz, benim kurulumunu açıkladığım sürüm *1.3.12* dir.

Apache size tek dosya halinde ve sıkıştırılmış olarak gelecektir. Kurulum herhangi bir Windows programından daha zor değil, Apache sitesinden çektiğiniz dosyanın üstüne çift tıklayın ve kurulumu başlatın. Karşınıza lisansla ilgili bilgiler ve Apache'in Windows sürümünün halen beta aşamasında olduğu ve UNIX'teki kardeşine oranla güvenlik açıklarının daha fazla olduğu hakkında uyarılar çıkacaktır. Amacımız yazdığımız programları bilgisayarımızda test etmek oldugu için bu uyarılar bizi ilgilendirmiyor. Bu ekranları geçtikten sonra Apache'i hangi klasöre kaydetmek istediğiniz sorulacak. Burada *'Browse'* a tıklayarak bu klasörü *'C:\\Apache'* olarak değiştirin. Bu işlem ileride size kolaylık sağlayacak. Sonraki ekranda *'Typical'* seçenegini seçin. Apache dosyaları kopyalanacak ve kurulum tamamlanacak. Dünyanin en güçlü sunucusu artık emrinize amade ;o)

Bundan sonra yapacağımız işlemlerin çoğu* MS-DOS ekranında geçecek, DOS komutlarını bilmeyenler için adım adım komutları yazacağım, gözünüz korkmasın kısa sürede bu komutlara hakim olursunuz. Rahat takip edebilmeniz için her adımın başına bir numara koyacağım.*

* Baslat | Programlar | MS-DOS komut istemi* ile DOS ekranına çıkın. DOS ekranından tekrar Windows'a dönmek için 'exit' komutunu kullanacaksınız. DOS ekranını Windows altında bir pencere olarak görmek isterseniz, 'ALT+ENTER' tuşlarına basın. Yazılar biraz küçülecek ama yeniyseniz olaya daha rahat hakim olursunuz. DOS ekranina çıktıktan sonra:

1. cd\\apache\\htdocs
2. ren *index.html.en index.html*
3. cd\\apache\\conf
4. edit *httpd.conf*

Apache'in konfigürasyon dosyasıyla karşı karşıyasınız. Yukarıdan aşağıya gerekli bütün satırları inceleyeceğiz ve kendi gereksinimlerimize göre değistireceğiz. '#' ile başlayan satırlar açıklama satırlarıdır. Sol taraf var olan ayarı, sağ taraf sizin yapmanız gereken değişikliği gösteriyor. Baştaki '#'i kaldırmayı unutmayın yoksa değişikliğiniz işleme konmaz.

Var Olan AyarYapılması Gereken Değişiklik #ServerName *new.host.name*ServerName *localhost* DirectoryIndex *index.html*DirectoryIndex *index.html index.php3 index.php* Sonraki değişiklik *Alias* eklemek olacak. *Alias*, harddiskinizdeki herhangi bir klasörü sunucunuza tanıtmanızı sağlar. Önceden tanımlanmış bir *Alias* var, biz de kendimizinkini tanımlayalım. Siz daha sonra istediğiniz kadar *Alias* tanımlayabilirsiniz. Aşağıdaki satırı var olan *Alias* satırının altına ekleyin :

Alias */php/ "C:/apache/php"*

Bir kademe aşağıda *ScriptAlias* var. Önceden var olan *ScriptAlias* satırının altına aşağıdaki satırı ekleyin:

ScriptAlias */php3/ "C:/php3/"*

Yapmamız gereken iki değişiklik daha var. Aşagıya inerek *AddType* bölümünü bulun ve aşagıdaki satırı yenisiyle değiştirin. Bu değişiklik, sunucunun .php .php3 ve .phtml soyadlı dosyaları tanıması ve PHP ile işlemesi için :

Var Olan AyarYapılması Gereken Değişiklik AddType *application/x-httpd-php3 .phtml*AddType *application/x-httpd-php3** .php3 .php .phtml* Daha aşağıda *Action* bölümü var. Buraya eklenecek satır:

Action *application/x-httpd-php3 "/php3/php.exe"*

Bu dosya ile işimiz şimdilik bitti. Dosyayı kaydedip editörden çıkın. Bu adımları atlayıp benim hazırladığım konfigürasyon dosyasını da indirebilirsiniz. ZIP dosyasını çektikten sonra içindeki dosyayı *"C:\\apache\\conf"* klasörünün içine kopyalamanız yeterli. İndirmek için *tyklayyn. <docs/phpkurwinapache/apconf.zip>*

Şimdi Apache'in çalışıp çalışmadığını kontrol edelim.

5. cd\\apache
6. apache *--standalone*

Bu iki komutu uyguladıktan sonra,

*Apache/1.3.12 (Win32) Running...*

mesajını almanız gerekiyor. Şimdi Windows'a geri dönün. Tarayıcınızı çalıştırın. Adres satırına *http://localhost* yazın. Eger her şeyi doğru yaptıysanız, Apache'in karşılama mesajı ile karşilaşacaksınız. Hata aldıysanız, başa dönüp *ServerName* ve *DirectoryIndex*'i kontrol edin ve tekrar deneyin.

Apache'i kapatmak için eski DOS ekranına dokunmadan yeni bir tane açmanız gerekiyor. Windows'tan yeni bir DOS ekranı açın.

7. cd\\apache
8. apache -k shutdown

İlk çalıştırdığınız ekrandaki Apache'in durmuş olduğunu göreceksiniz. Eger durmamışsa CTRL+BREAK tuşlarına basarak çalışmasını durdurabilirsiniz. Bu yöntemi zorda kalmadıkça kullanmayın.

Apache için, DOS ekranına çıkmadan *Basla/Yeniden Basla/Dur* komutlarını vermenizi sağlayan küçük bir program var. ZIP dosyasını kendinize çekin, içindeki *apmgr.exe* dosyasını *c:\\apache* klasörüne kopyalayın ve her bilgisayarı açışınızda çalıştırın. Program sistem çubuğuna yerleşiyor ve kullanım kolaylığı sağlıyor. Bu programı indirmek için tıklayın <docs/phpkurwinapache/apmgr.zip>.

Apache ile ilgili ayarlarımız bitti. Size verdiğim konfigürasyon dosyası işinizi kolaylaştıracak ama ben yine de bu işlemleri tek tek uygulayıp havaya girmenizi tavsiye ederim ;o) *Apache Manager* programını ise mutlaka indirin ve kullanın.

**II. Adım - PHP 3.0.16 Kurulumu**

PHP'nın en son sürümü 4.0, şu anda *release-candidate-1* aşamasında. Mayıs ayı içerisinde 4.0 versiyonu tam olarak oturmuş olacak, benim 3.0.16'yi anlatmamın sebebi, halen büyük bir çoğunluğun 3.0 kullanıyor olması, ve 4.0 ile kurulum olarak hemen hemen aynı olması. Aradaki farklılıklara yazının sonunda değineceğim.

PHP'yi <http://www.php.net> adresinden indirdiniz. ZIP dosyasını açın ve içindeki dosyaları *C:\\php3\\* klasörüne kopyalayın. Şimdiye kadar direk klasör isimleri verdim, siz bunları değiştirebilirsiniz, ama klasör isimlerini değiştirmek çoğunlukla size extra iş çıkarmaktan başka bir işe yaramaz. Dosyaları kopyaladıktan sonra tekrar DOS ekranına geçin:

1. cd\\php3
2. edit *php3.ini-dist*

Bu dosya, PHP ayarlarının saklandığı dosya. *Dynamic Extensions* bölümünü bulun:

Var Olan AyarYapılması Gereken Değişiklik; extension=php3\_mysql.dllextension=php3\_mysql.dll Bunu yapmaktaki amacımız MySQL ile ilgili komutları kullanabilmek. Daha sonra *mail function* satırını bulun. SMTP'nin karşısındaki değeri *127.0.0.1* olarak değiştirin. Bir değer yoksa ekleyin. Düzeltmeler bu kadar. Editörden çıkın.

3. copy *php3.ini-dist c:\\windows\\php3.ini*

Dosyanın hazır halini tıklayarak <phpcnf.zip> indirebilirsiniz. ZIP dosyasının içindeki dosyayı *C:\\Windows* klasörüne kopyalamanız yeterli.

Apache ve PHP birlikte çalışmaya hazır. Son olarak kendimize bir çalışma klasörü yaratalım. Bu klasörü daha önce *Alias* ile Apache konfigürasyon dosyamıza eklemiştik. Ayni yöntemle başka çalışma dizinleri de ekleyebilirsiniz.

4. cd\\apache
5. md *php*

Artık küçük bir kod yazıp sistemimizi deneyebiliriz. Windows'a geri dönün. Notepad'i çalıştırın. Asağıdaki kodu yazıp *c:\\apache\\php\\test.php* olarak kaydedin.

Örnek 1- test.php

<?
echo phpinfo();
?>

Apache sunucunuzu başlatın. Tarayıcınıza *[http://localhost/php/test.php](http://localhost/php/test.php) * n gerekli dosyaları ku llanıma hazır bir biçimde hazırladım. Yukarıdaki linklerden indirip direk kullanmaya başlayabilirsiniz.

** ****PHP 3.0 - 4.0 Kurulum Farkları**

** **Eğer PHP 4.0'i kurmak istiyorsanız dikkat etmeniz gereken bazı noktalar var. Öncelikle dosyaları *c:\\php\\* klasörüne kopyalamanızı tavsiye ederim. Bu klasördeki *php.ini-dist* dosyasını bu sefer *php.ini* olarak adlandırıp *C:\\Windows* klasörüne kopyalamanız gerekli. Apache'in konfigürasyon dosyası *httpd.conf* içinde, *AddType* ve *Action* tanımlamalarını yaparken *application/x-httpd-php* kullanmanız gerekiyor. *ScriptAlias* satirini yine */php/ "C:/php/"* olarak değiştirmeniz gerekli. *Action* satırında yine klasöre uygun olarak *"/php/php.exe" *yazmalısınız.

Apache ve PHP'nin kurulumu hakkında bilmeniz gerekenler bu kadar. İleride Apache'nin daha geniş konfigürasyonu ve diğer özellikleri hakkında daha ayrıntılı yazılar olacak. Hepinize iyi çalışmalar..

[](javascript:history.go(-1))

[](index.htm)

[](ders5.htm)

[ ](javascript:window.external.AddFavorite('http://www.e-dersane.com','E-DERSANE.com - Internetle Yasamayi Ogretir!'))

Copyright © 2001- **[www](http://www.e-dersane.com)**[.**E-Dersane.com**](http://www.e-dersane.com)** - Offline Dersler**. All Rights Reserved.
**[](http://www.e-dersane.com)****[](http://www.php.org.tr)****PhP Offline Dersleri **bolumunde yayinlanan bütün metin ve makaleler GPL lisansli olup ayrintili bilgi için [GNU.org](http://www.gnu.org) adresine bakiniz.

---
*Kaynak: `PHP 2/ekitap-Anonim-PHP_Offline/ders4.htm`*
*Görseller: `PHP-2/gorseller/` (1 dosya)*
