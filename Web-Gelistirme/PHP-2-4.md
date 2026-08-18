# PHP 2

[](http://www.e-dersane.com)

[](javascript:history.go(-1))

[](PHP-2-13.md)

**
Apache, PHP ve mySQL\`in son versiyonlarını bilgisayarınıza indirdikten sonra kurulumu şu şekilde yapabilirsiniz : **

1- tar zxvf apache\_1\_3\_9.tar.gz
2- tar zxvf mysql-3.22.27-pc-linux-i686.tar.gz
3- tar zxvf php-4\_0b3\_tar.gz

Daha sonra işimiz kolaylaşsın diye sembolik linkler yaratalım .

4- ln -s mysql-3.22.27-pc-linux-i686 mysql
5- ln -s apache\_1.3.9 apache
6- ln -s php-4\_0b3 php4

mySQL, Apache ve PHP den bağımsız kurulduğu için öncelikle onu kuralım.
7- cd mysql
8- scripts/mysql\_install\_db
9- bin/safe\_mysqld &

..ve mySQL deamon\` ini başlatalım. Bilgisayarın her açılışında kendiliğinden başlaması için sistem açılış dosyasına (Slackware için /etc/rc.d/rc.local dosyasina) bir ekleme yapalım.

10- /etc/rc.d/local.rc (local.rc dosyası açılış sırasında okunan dosyalardan biridir. Fakat değişik linux dağıtımlarında bu dosyanın ismi ve bulunduğu yer farklı olabilir) dosyasının sonuna ;
/bin/bash -c "cd /usr/local/mysql ; ./bin/safe\_mysqld &
satırını ekleyin.

Şimdi de sıra Apache ve PHP ikilisini kurmaya geldi.

11- cd ../apache
12- ./configure
13- cd ../php
14- ./configure --with-mysql=../mysql --with-apache=../apache
--enable-track-vars 15- make
16- make install
17- cd ./apache
18- ./configure --prefix=/net --activate-module=src/modules/php4/libphp4.a

Bu adımda zaten kullanmakta olduğunuz bir httpd varsa yukarıdaki "--prefix=/net" yerine apache\` nin kurulu olduğu dizinin ismini yazın. Örneğin kendi bilgisayarım için "--prefix=/var/lib/apache" yazmalıydım.

19- make
20- make install

Bu aşamada eski ayarlarını korumak isteyenler make install komutunu kullanmak yerine apache/src\` nin altındaki httpd binary\` sini çalışmakta olan apache binary\` si ile değiştirmeliler. Örneğin kendi bilgisayarım için
cp /var/lib/apache/bin/httpd /var/lib/apache/bin/httpd.yedek
cp src/httpd /var/lib/apache/bin
yazmam gerekliydi. Yukarıda önce eski httpd deamon\` nin bir yedeğini aldık. Ardından yeni httpd\`yi eskisinin üzerine kopyaladık. Fakat burada dikkat edilmesi gerekli bir konu var. Apache, bir çok linux sürümünde bilgisayar açıldığında başlayan bir daemon olarak çalışır. Bu nedenle apache üzerinde yapacağınız değişikliklerden önce, httpd\` yi durdurmanız gereklidir. Bunu da (çalışmakta olan) apache/bin dizininin içinde "./apachectl stop" komutuyla yapabilirsiniz.
Eger 16. maddeyi anlayamadım derseniz kısaca "make install" komutu işinizi görür. Bu komutla beraber /net adinda bir klasör yaratılacak ve içine gerekli dosyalar kopyalanacaktır.

Sıra geldi içine PHP\`yi gömdüğümüz yeni httpd deamon\` ini çalıştırmaya...

Öncelikle eski httpd daemon\`unu
21- /net/bin/apachectl restart
komutu ile durdurup yeni httpd\`yi başlatalım.
22- /etc/rc.d/rc.http
dosyasının içinde muhtemelen
"/var/lib/apache/sbin/apache start" gibi bir ifade vardır. Onu şu şekilde değiştirin ;

#/var/lib/apache/sbin/apache start
/net/bin/apachectl start

Bu sayede bir terslik olursa ilk satırın başındaki diyezi ikinci satıra koyup eski ayarlarınızı kullanmanız mümkün olur.

23- Apache\`nin PHP sayfalarını anlayabilmesi için /net/conf/httpd.conf dosyasındaki (Klasör isminin net ile başlamasının sebebi 18. adımda --prefix=/net komutu kullanmamız yani klasör olarak net ismini seçmemiz)

#AddType application/x-httpd-php3 .php3
#AddType application/x-httpd-php3-source .phps

satırlarını su satırlarla değiştirin ;

AddType application/x-httpd-php .php .php3
AddType application/x-httpd-php-source .phps

Eğer bu satırlar yoksa httpd.conf\` un içinde herhangi bir yere ekleyebilirsiniz. Bu adım da bittikten sonra PHP, mySQL ve Apache kullanıma hazır hale geliyor.

**İlk Örnek **
Eğer su ana kadar herşeyi yukarıda anlatıldığı gibi yaptıysanız muhtemelen asağıdaki uygulamamız da çalışacaktır.
PHP ile hazırlanmış web sayfalarının uzantısının .php şeklinde olması gerekli. Bunu gözönünde bulundurarak bundan sonraki tüm örneklerimizi /net/htdocs/ dizini altına (htdocs dizini, apache\` nin httpd.conf dosyasında bir değişiklik yapılmazsa web sayfalarını tuttuğu dizindir) kaydedeceğiz.
Asağıdaki örneği o2.php adıyla kaydedelim.

**Örnek 2 (o2.php)**

<?php
echo "<center>Merhaba Dünya</center>";
?>
Tahmin edersiniz ki ekran çıktısı;

Merhaba DünyaSeklinde olacaktır. Nereden göreceğim bu çıktıyı derseniz http://localhost/o2.php adresini tarayıcınıza yazıp görebilirsiniz. Burada <center></center> komutu gereği yazı ortalanmıştır. Echo komutu ise tırnak işaretinin içindeki metni ekrana basar. Eğer sayfanın HTML koduna bakarsanız, sadece;
<center>Merhaba Dünya</center>
yazısını görürsünüz. Daha önce de bahsettiğimiz gibi kullanıcı hiçbir şekilde PHP ile ilgili bir komut görmemektedir.

Ekrana "**Merhaba Dünya**" da yazdırdığımıza göre geriye pek birşey kalmadı demektir. ;)

[](javascript:history.go(-1))

[](PHP-2-13.md)

[ ](javascript:window.external.AddFavorite('http://www.e-dersane.com','E-DERSANE.com - Internetle Yasamayi Ogretir!'))

Copyright © 2001- **[www](http://www.e-dersane.com)**[.**E-Dersane.com**](http://www.e-dersane.com)** - Offline Dersler**. All Rights Reserved.
**[](http://www.e-dersane.com)****[](http://www.php.org.tr)****PhP Offline Dersleri **bolumunde yayinlanan bütün metin ve makaleler GPL lisansli olup ayrintili bilgi için [GNU.org](http://www.gnu.org) adresine bakiniz.

---
*Kaynak: `PHP 2/ekitap-Anonim-PHP_Offline/ders11.htm`*
*Görseller: `PHP-2/gorseller/` (1 dosya)*
