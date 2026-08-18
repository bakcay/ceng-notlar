# PHP 2

[](http://www.e-dersane.com)

[](javascript:history.go(-1))

[](PHP-2-13.md)

[](PHP-2-4.md)

**
MySQL Kurulumu ve SQL\`e Giris for Win. 95-98-2000 **

**Bu bölümde, PHP ile en çok kullanılan SQL sunucusu MySQL'ın Windows altında kullanımı hakkında bilgi vereceğim. Aynı zamanda SQL diline de bir giriş yapmış olacağız.**

**Kurulum**

MySQL'ı www.mysql.com <http://www.mysql.com> adresinden indirin. (benim kullandığım versiyon 3.22.34-shareware)

ZIP dosyasını açın ve SETUP.EXE yi çalıştırın.

Program yüklendikten sonra MS-DOS ekranına geçin.

cd\\mysql\\bin yazıp ENTER'a basın.

ren mysqld-shareware.exe mysqld.exe yazıp ENTER'a basın.

c:\\mysql\\bin\\mysqld --standalone yazıp ENTER'a basın.

Eğer işletim sisteminiz NT ise, 6.maddeyi atlayın, ***c:\\mysql\\bin\\mysqld --install ***yazıp ENTER'a basın.

Eğer Win95/98 kullanıcısıysanız, 6.maddedeki komutu bilgisayarınızı her yeniden kapatıp açtığınızda tekrar yazıp çalıştırmanız gerekir, ***Başlat | Çalıştır (Start | Run) ***ekranından aynı komutu verip çalıştırabilirsiniz.

exit yazıp ENTER'a basın ve DOS ekranını kapatın.

NT kullanıyorsanız MySQL'i başlatmak için;
***Başlat | Ayarlar | Denetim Masası | Hizmetler*** seçeneklerine tıklayın ve
(Start Menu | Settings | Control Panel | Services)
***MySql*** i seçip ***Başlat*** (Startup) tuşuna basın.

Artık MySQL sistemimizde kurulu. MS-DOS ekranına geçip bir deneme yapalım. DOS ekranında ***cd\\mysql\\bin ***yazın. Bu klasör MySQL'in bütün çalıştırılabilir dosyalarının bulunduğu yer.

C:\\mysql\\bin> **mysqladmin version** Bu komutu verdiğinizde karşınıza MySQL ile ilgili bilgiler gelecektir. Bu, programı doğru bir şekilde yüklediğinizi ve programın kullanıma hazır olduğunu gösterir. Eğer*** "cannot connect to localhost"*** gibi bir hata mesajı alıyorsanız, ***"--standalone"*** ekini koyup koymadığınızı kontrol edip tekrar ***"mysqld"*** yi çalıştırın.

**SQL'e Giriş**

C:/mysql/bin> **mysql** Yukardaki komutu vererek MySQL'i çalıştırıyoruz. Artık karşımızda ***"mysql>"*** şeklinde MySQL komut satırı var. İlk veritabanımızı yaratalım :

mysql> **create database deneme;** Sondaki ***"noktali virgül"***e dikkat edin. Bu işaret MySQL'e işlemi gerçekleştirmesini söyler. Eğer koymazsanız, MySQL komutu yazmaya bir sonraki satırdan devam etmek istediğinizi düşünür ve size devam edebilmeniz için yeni bir satır açar. Bu uzun sorgulamalar için faydalı bir özelliktir.

mysql> **use deneme;*"use"*** komutu ile üstünde çalışmak istediğimiz veritabanını seçiyoruz.

Burada durup biraz veritabanı mantığından ve ne zaman veritabanı kullanmanız gerektiğinden bahsetmek istiyorum. Diyelim ki, bir okuldaki öğrencilerin ders notlarını takip etmemiz isteniyor. Dört tane dersimiz var, Matematik, Türkçe, Beden ve Müzik. Her öğrencinin bu derslerden aldığı bir not var. Ekstra bir bilgi olarak da, öğrencinin sınıfını da takip etmek istiyoruz. Bu alanları aşağıdaki gibi gruplandırabiliriz :

IsimSinifMatematikTürkçeBedenMüzikAhmet10-A3343Mehmet10-A2344Ayse10-A4435"Isim","Sinif","Matematik","Türkçe","Beden" ve "Müzik", ***alan (field)*** olarak adlandırılır. Her alan, aynı kümenin farklı elemanlarını (veya aynı elemanlarını) içerir.

Bu gördüğünüz tabloyu veritabanımızda yaratalım :

mysql>** create table notlar (isim char(20), sinif char(5), mat int, turkce int, beden int, muzik int);**Yarattıgınız veritabanındaki alanları,

mysql> **show fields from notlar;**komutu ile görebilirsiniz. Elde ettiğimiz sonucu görelim :

+--------+----------+------+-----+---------+-------+ | Field | Type | Null | Key | Default | Extra | +--------+----------+------+-----+---------+-------+ | isim | char(20) | YES | | NULL | | | sinif | char(5) | YES | | NULL | | | mat | int(11) | YES | | NULL | | | turkce | int(11) | YES | | NULL | | | beden | int(11) | YES | | NULL | | | muzik | int(11) | YES | | NULL | | +--------+----------+------+-----+---------+-------+Tabloyu yaratırken şu işlemleri doğru yaptığınızdan emin olun :

Alan adları bir çift parantez içine alınmış olmalı.

Her alan adı diğerinden virgül ile ayrılmalı.

Son alandan sonra virgül kullanılmamalı.

Bütün SQL komutlarının sonuna noktalı virgül ";" konmalı.

mysql> **INSERT INTO notlar (isim,sinif,mat,turkce,beden,muzik) VALUES ('Ahmet','10-A',3,3,4,3);*"Char"*** ile tanımladığınız alan adlarına değer verirken tek tırnak arasında yazmak zorundasınız. Diğer alanları ***"integer"*** yani sayısal değer olarak tanımladığımız için böyle bir zorunluluğumuz yok. Şimdi yeni eklediğimiz kaydı listeleyelim :

mysql> **SELECT \* FROM notlar;**

+-------+-------+------+--------+-------+-------+ | isim | sinif | mat | turkce | beden | muzik | +-------+-------+------+--------+-------+-------+ | Ahmet | 10-A | 3 | 3 | 4 | 3 | +-------+-------+------+--------+-------+-------+

**Tabloya Alan Eklemek**

Tabloya istediğimiz zaman yeni bir alan ekleyebilir ya da mevcut alanlar üzerinde değişiklikler yapabiliriz :

mysql> **ALTER table notlar ADD COLUMN resim int;** *Bir'den fazla alan eklemek için:* mysql> **ALTER table notlar ADD COLUMN fizik int, ADD COLUMN dogumtarihi date;**Sonucu kontrol edelim :

mysql> **SELECT \* FROM notlar;**

+-------+-------+------+--------+-------+-------+-------+-------+-------------+ | isim | sinif | mat | turkce | beden | muzik | resim | fizik | dogumtarihi | +-------+-------+------+--------+-------+-------+-------+-------+-------------+ | Ahmet | 10-A | 3 | 3 | 4 | 3 | NULL | NULL | NULL | +-------+-------+------+--------+-------+-------+-------+-------+-------------+ 1 row in set (0.00 sec)

**Çoklu-Satır Kullanarak Komut Girişi**

MySQL komut satırı arabirimi komutu tek bir satır halinde yazmanıza ya da satırlara bölmenize olanak sağlar. İki yazım biçimi arasında bir fark yoktur. Ancak kodunuzu satırlara bölmeniz, yazdıklarınızın daha anlaşılabilir olmasını sağlar.

Çoklu-Satır modunda, MySQL yorumlayıcısı her satırın başına "->" ekler. Bu siz noktalı virgül ";" ile SQL komutunu sonlandırana kadar devam eder. Noktalı virgül yazılıp ENTER'a basıldıktan sonra komut çalıştırılır.

Asagidaki örnekleri inceleyelim :

Tek Satir Örnegimysql> **create table test (alan01 integer,alan02 char(30));Çoklu-Satir Örnegi**mysql> **create table test** -> **(alan01** -> **integer,** -> **alan02** -> char(30));

Dogru KullanimYanlis Kullanimmysql> **create table test** -> **(alan01** -> **integer,** -> **alan02** -> **char(30));**mysql> **create table test** -> **(alan01 inte** -> **ger,** -> **alan02** -> **char(30));**Kayıt eklerken veya güncellerken, bir alana girilecek bilgiyi satırlara bölmeyin. Hata mesajı almazsınız ancak veritabanının yapısına zarar verirsiniz :

Standart IslemBozuk Kayda Neden Olan Islemmysql> **insert into test (alan02)** -> **values** -> ('merhaba ben mysql ogreniyorum');mysql> **insert into test (alan02)** -> **values** -> **('merhaba ben** -> **mysql ogreniyorum');Sonuçlar**mysql> **select \* from test;** +---------+-------------------------------+ | alan01 | alan02 | +---------+-------------------------------+ | NULL | merhaba ben mysql ogreniyorum | | NULL | merhaba ben mysql ogreniyorum | +---------+---------------------+

**Tabloya Değişik Tipte Kayıtlar Ekleyelim**

mysql> **INSERT INTO notlar (isim,sinif,mat,turkce,beden,muzik,resim,fizik,dogumtarihi) -> VALUES ('Asli','10-C',2,2,4,4,5,1,'1980-01-31');**Sonucu görelim:

mysql> SELECT \* FROM notlar;

+-------+-------+------+--------+-------+-------+-------+-------+-------------+ | isim | sinif | mat | turkce | beden | muzik | resim | fizik | dogumtarihi | +-------+-------+------+--------+-------+-------+-------+-------+-------------+ | Ahmet | 10-A | 3 | 3 | 4 | 3 | NULL | NULL | NULL | | Asli | 10-C | 2 | 2 | 4 | 4 | 5 | 1 | 1980-01-31 | +-------+-------+------+--------+-------+-------+-------+-------+-------------+Standart Tarih formatı ***"yyyy-gg-aa"*** dır.

Standart Zaman formatı "***hh:mm:ss"*** dir. (saat:dakika:saniye).

Yukardaki örnekte olduğu gibi Tarih ve Zaman bilgileri kaydedilirken tırnak içine alınmalıdır.

Tarih ***"yyyyggaa"***, Zaman ***"hhmmss"** *formatında yazılabilir. Böyle yazıldıklarında tırnak işareti kullanmaya gerek yoktur.

MySQL'in ***"buffer (tampon)"*** özelliği vardır. Yukarı ok tuşuna basarak önceki komutları tekrar yazdırıp zamandan tasarruf edebilirsiniz.

**Mevcut Kayıtları Güncelleme**

Tek bir alani güncellememysql> **update notlar set fizik=1 where isim='Ahmet';Bir'den çok alani güncelleme**mysql> **update notlar set fizik=3, mat=4 where isim='Asli';** Ve aldığımız sonuç şöyle olacak :

mysql> **SELECT \* FROM notlar;**

+-------+-------+------+--------+-------+-------+-------+-------+-------------+ | isim | sinif | mat | turkce | beden | muzik | resim | fizik | dogumtarihi | +-------+-------+------+--------+-------+-------+-------+-------+-------------+ | Ahmet | 10-A | 3 | 3 | 4 | 3 | NULL | 1 | NULL | | Asli | 10-C | 4 | 2 | 4 | 4 | 5 | 3 | 1980-01-31 | +-------+-------+------+--------+-------+-------+-------+-------+-------------+

**Tablodan Kayıt Silme**

Tablodan bir veya daha fazla kayıt silmek için ***"delete"*** komutunu kullanacağız. Aşağıdaki örneğe bakalım :

mysql> **DELETE FROM notlar WHERE isim='Ahmet'; ***Query OK, 1 row affected (0.01 sec) mysql> ***SELECT \* FROM notlar;**

+-------+-------+------+--------+-------+-------+-------+-------+-------------+ | isim | sinif | mat | turkce | beden | muzik | resim | fizik | dogumtarihi | +-------+-------+------+--------+-------+-------+-------+-------+-------------+ | Asli | 10-C | 4 | 2 | 4 | 4 | 5 | 3 | 1980-01-31 | +-------+-------+------+--------+-------+-------+-------+-------+-------------+***"Delete"*** komutunu kullanırken dikkatli olmalısınız. Yukardaki örnekte WHERE komutunu eklemiş olmasaydık, tablodaki bütün kayıtları sil demiş olacaktık :

mysql> **DELETE FROM notlar; ***Query OK, 2 row affected (0.01 sec)***Çikmak için**

mysql> **quit ***Bye*

**MySQL ve PHP**

SQL dilini kullanarak, bir MySQL veritabanı üzerinde yapabileceğimiz temel işlemleri öğrendik. Tabii ki MySQL ile amacımıza uygun çok daha karmaşık sorgulamalar yapabilir, farklı tablolardan aldığımız bilgileri birleştirip istediğimiz kriterlere uygun biçimde kullanıcılara sunabiliriz. Burada anlattığım komutlara hakim olmanız, PHP ile yarattığınız veritabanı uygulamalarında size sürat kazandıracaktır.

MySQL'in PHP kodu içinde kullanımını ***mysql\_db\_query*** fonksiyonunu inceleyerek öğrenebilirsiniz, ben ufak bir örnek verecegim :

<?php /\* Once veritabanina baglaniyoruz \*/ **$link** = **mysql\_connect**("*localhost*"); /\* SQL komutunu yaziyoruz \*/ **$strSQL** = "*SELECT \* FROM notlar*"; /\* Sorgulamayi yapiyoruz \*/ **$result** = **mysql\_db\_query**("deneme",**$strSQL**,**$link**); /\* Sonuclari ekrana yaziyoruz \*/ **while** (**$row** = **mysql\_fetch\_array**(**$result**)) { echo "*Isim: *" . **$row**\['*isim*'\] . "*<br>"*; echo "*Matematik*: " . **$row**\['*mat*'\] . "*<br>*"; echo "*Türkçe: *" . **$row**\['*turkce*'\] . "*<br>"*; echo "*<br>*"; } ?>***mysql\_fetch\_array*** komutu, sorgulama sonunda oluşan listeden sıradaki ilk kaydı alır ve bunları istenen ***array***'e atar (burada ***$row***). Listedeki bütün kayıtları gösterebilmek için de bu işlemi döngü (***while***) içine sokuyoruz. Bütün kayıtlar okunduğunda döngü de sona erecektir.

**Son Söz**

PHP ve MySQL dinamik web sayfalarI tasarımında her geçen gün daha fazla tanınıyor, kullanılıyor. Her ikisinin de ücretsiz olması (MySQL'in Windows sürümünün shareware olması dışında), kullanımlarının kolay ve performanslarının diğer alternatiflerinden aşagı kalmıyor olması da popülerliklerinin devam etmemesi için hiçbir neden olmadığını gösteriyor. Bugün birçok web alanı veren firma PHP + MySQL desteğini de beraberinde sunuyor. Aynı zamanda bu iki hizmeti reklam karsılığı ücretsiz veren siteler de giderek çoğalmakta. Kısaca, PHP ve MySQL ögrenmekle, her geçen gün büyüyen ve açık-kod felsefesini baslangıç noktası olarak belirlemiş kocaman bir ailenin üyesi olmuş olacaksınız ;o)

**Faydalanılan Kaynaklar**

Analysis And Solutions.Com <http://www.analysisandsolutions.com/code/mybasic.htm>
Wrox's Professional PHP Programming <http://www.wrox.com>

[](javascript:history.go(-1))

[](PHP-2-13.md)

[](PHP-2-4.md)

[ ](javascript:window.external.AddFavorite('http://www.e-dersane.com','E-DERSANE.com - Internetle Yasamayi Ogretir!'))

Copyright © 2001- **[www](http://www.e-dersane.com)**[.**E-Dersane.com**](http://www.e-dersane.com)** - Offline Dersler**. All Rights Reserved.
**[](http://www.e-dersane.com)****[](http://www.php.org.tr)****PhP Offline Dersleri **bolumunde yayinlanan bütün metin ve makaleler GPL lisansli olup ayrintili bilgi için [GNU.org](http://www.gnu.org) adresine bakiniz.

---
*Kaynak: `PHP 2/ekitap-Anonim-PHP_Offline/ders10.htm`*
*Görseller: `PHP-2/gorseller/` (1 dosya)*
