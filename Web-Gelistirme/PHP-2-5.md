# PHP 2

[](http://www.e-dersane.com)

[](javascript:history.go(-1))

[](PHP-2-13.md)

[](PHP-2-6.md)

**
PHP ile Internet Programciligina Giris**

Bu yazida PHP ile isinma turlari atmaya baslayacagiz ve ufak, internet programciliginin mantigini anlamaya yönelik kodlar yazip çalistiracagiz. Örnekleri yazmak için herhangi bir text editörünü (notepad gibi) kullanabilirsiniz. Bir Türk tarafindan yazilmis olan *PHPEd <http://www.soysal.com>* size daha rahat bir programlama ortami sunuyor. Ayrica bu adresten PHP ile ilgili Türkçe dökümanlara da ulasabilirsiniz. Allaire'in HomeSite'i da PHP kodlarini taniyip renklendirerek anlamada ve kullanimda kolaylik sagliyor, onu da <http://www.allaire.com> adresinden edinebilirsiniz.

PHP'nin sagladigi en büyük kolayliklardan biri HTML kodunun içine gömülebilir olmasidir. PHP kodu, kullanicinin tarayicisina gitmeden önce sunucu tarafindan islenir ve geriye %100 HTML kodu gönderilir. Asagidaki örnege bakarsak ;

<HTML> <?php **echo** ("*PHP ile yaratilmis yazi*"); ?> </HTML>Normal .html uzantili dosyalar, web sunucusu tarafindan islenmeden direk tarayiciya gönderilir. Sunucu HTML kodundan kaçmaya yarayan "<?" veya "<?php" gibi bir tag ile karsilastiginda ise PHP moduna girer ve bu bilgiler sunucu tarafinda islenir. HTML'den kaçmak ve PHP moduna geçmek için;

<? echo ("Bu SGML kullanimina örnektir."); ?>

<?php echo ("Bu XML ile ilgili özellikleri de kullanmanizi saglar."); ?>

<SCRIPT LANGUAGE='php'> echo ("Bu kullanimi tavsiye etmem."); </SCRIPT>

<% echo ("PHP 3.0.4 ile beraber ASP tipi kaçisi da kullanabilirsiniz."); %>

Yukardaki örnek kodu test.php3 (veya .php) olarak kaydedin ve tarayicinizda deneyin. Daha sonra tarayicinizi kullanarak sayfanin kaynagini inceleyin.

**PHP ve Client-Side (Kullanici-Tarafli) Kod**

PHP'yi client-side kodunu dinamik biçimde yaratmak için kullanabiliriz. Bu isi yaziyi yazdigimiz yöntemin aynisini kullanarak yapacagiz :

<HTML> <?php **echo** ("*<SCRIPT LANGUAGE='JavaScript'> alert ('Dikkat!'); </SCRIPT>*"); ?> </HTML>Sunucu echo komutunu çalistirdiginda, tarayiciya:
<SCRIPT LANGUAGE='JavaScript'> alert ('Dikkat!'); </SCRIPT>
satirini gönderecektir. Tarayici da bu kodu yorumlayip alert kutusunu ekrana çikartacaktir.

**PHP Degiskenleri**

Bütün programlama dillerinde oldugu gibi PHP de verileri saklamak için degiskenleri kullanir. PHP'de bütün degisken isimleri '$' ile baslar. Java veya Visual Basic'in tersine degiskenleri declare etme zorunlulugu yoktur. Bir degiskeni ona bir deger atayarak yaratabilirsiniz :

**$username** = "*Serdar*"; **echo** **$username**;

**Kullaniciyla iletisim**

Degiskenler kullanicinin girdigi bilgileri formdan alip islemek amaciyla da kullanilir. Eger bir sayfa "name" degeri "username" olan bir "textbox" içeriyorsa, buraya girilen deger otomatik olarak "$username" degiskenine atanir :

<HTML> <FORM> Lütfen kullanici adinizi yazin:<BR> <INPUT TYPE=TEXT NAME=username><BR><BR> <INPUT TYPE=SUBMIT VALUE="Gönder"> </FORM> <BR><BR> Kullanici adiniz: <?php **echo** (**$username**); ?> </HTML>Bu kodu yazip "Gönder" tusuna bastiginizda yazmis oldugunuz ismi göreceksiniz. Tarayicinizin URL bölümüne dikkat ederseniz, "dosyaadi.php3?username=yazdiginiz\_isim" oldugunu göreceksiniz. Bu formdaki bilgilerin URL kullanilarak bir sayfadan diger sayfaya tasinmasinda kullanilan yöntemlerden biridir.

**Veri Toplamak ve Web Sunucusundan Istekte Bulunmak**

Web programlarinda ilk adim genellikle kullanicindan birtakim bilgiler toplamaktir. Bu islem HTML formlari araciligiyla saglanir. Kullanici bilgilerini girer ve "Submit" tusuna basar. Tarayici verilen bilgileri düzenler ve web sunucusuna gönderir. Web sunucusunun gönderilen bilgileri anlamasi için, tarayicinin bilgileri Web sunucusunun anlayabilecegi hale getirmesi ve "HTTP Request" yani istekte bulunmasi gerekir.

Her "request" hangi metodla çalisacagini belirlemek zorundadir. Bunu <FORM METHOD="POST"> örnegindeki gibi yapabilirsiniz. En çok kullanilan üç metod HEAD,GET ve POST'tur.

HEAD dokümanin kendisini degil dokümanla ilgili bilgi almak için kullanilir.

GET ve POST web programlarini çalistirmak için kullanacaginiz metodlardir. Her ikisi de ayni görevi görür fakat çalisma biçimleri farklidir.

**GET Metodu**

GET ile bir "request" yapildiginda, bütün form verileri tek bir "string" haline getirilir ve key=value (degisken-ismi=degisken-degeri) biçimine sokulur :

http://www.sj.k12.tr/php/userform.php?username=yazdiginiz\_isim <http://www.sj.k12.tr/php/userform.php?username=Serdar>

Bu satir "php" klasörü içindeki "userform.php" scriptini çalistirir ve bu scripte "username" degiskenini ve bu degiskenin degeri olarak yazdiginiz ismi geçirir.

**ElemanAçiklamasi**

http://www.sj.k12.tr"request"i isleyecek olan sunucu/php/userform.phpSunucudaki dosyanin adi ve yeri?Dosyanin yerini verilerden ayirirkey=valueDegisken isimleri ve degerleri&key=value çiftlerini ayirmak için kullanilir+Bosluk karakterinin yerine geçerGET bütün web request'lerinde default olarak kullanilir. Kullanici bir sayfa istediginde, tarayici GET komutunu kullanir. GET ile çagrilan bir sayfa, eger tarayicinin hafizasinda mevcutsa tarayici sayfanin eski halini gösterebilir. GET ile yasanan bir diger problem, URL ile tasiyabileceginiz veri miktarinin sinirli olmasidir.

**POST Metodu**

POST Metodu, form bilgilerini sayfanin bir parçasiymis gibi olusturur. Sunucu verileri dosyadan okuyarak alir. Bu metod daha çok verinin transfer edilebilmesine izin verir, ve tarayicinin cache'deki eski bilgileri göstermesi sorununu ortadan kaldirir.

**Scriptin (ya da Programin) Çalistirilmasi**

** **Kullanicidan gelen istegi web sunucusu alir ve islenmesi gereken programa gönderir. Daha önce web sunucularinin kurulumunu anlatirken konfigürasyon dosyalarina bazi satirlar eklemistik, web sunucusu bu satirlar sayesinde hangi dosyalari hangi programlarla çalistirmasi gerektigini bilir ve ona göre davranir.

** ****Form Verilerinin Islenmesi**

Ilk örnekte forma girilen bilgiler tekrar ayni dosyaya dönüyordu. Bu bilgileri rahat biçimde kullanabilmek için baska bir dosyaya göndermemiz gerekir. Örnegin .html olarak hazirladigimiz formdaki bilgilerin .php olarak hazirladigimiz dosyaya gitmesini saglayabiliriz. Bu hem kodumuzun temiz olmasi hem de kontrolü kaybetmememiz için gereklidir:

<HTML> <!-- userform.html --> <FORM ACTION="formisle.php3" METHOD=POST> Lütfen kullanici adinizi yazin:<BR> <INPUT TYPE=TEXT NAME="username"><BR><BR> <INPUT TYPE=SUBMIT VALUE="Gönder"> </FORM> </HTML>Kullanici "Gönder" tusuna bastiginda, POST metodu kullandigimiz için, formdaki veriler formisle.php3 dosyasina "HTTP Header" yoluyla tasinacaktir. Metodu "GET" ile degistirerek ikisi arasindaki farki görebilirsiniz.

<HTML> <!-- formisle.php3 --> <?php **echo** ("*Merhaba, *" . **$username** . "*!*"); ?> </HTML>Degiskenin nasil kullanildigina dikkat edin. Formda <INPUT> tag'i içerisinde "NAME"'in aldigi deger ile degiskeninizin ismi aynidir, ve bunu PHP kodu içinde kullanmak için ekstra bir komut kullanmaniz gerekmez, degisken otomatik yaratilir. Bu özellik sadece <INPUT> tag'i için degil bütün NAME özelligi olan tag'lar için geçerlidir.

Artik PHP ile form bilgilerini nasil alip isleyebileceginiz ve kullaniciya geri bildirim yapabileceginiz hakkinda fikir sahibisiniz. Böylece verilerin veritabanina kaydedilene kadar hangi yollardan geçtigini, ya da formdan alinan bilgilerin e-posta ile gönderilmek için nasil hazirlandigini da ögrenmis oldunuz.

Bundan sonra alistirma olmasi için küçük programlar yazmaya baslayacagiz, size de tavsiyem kendinizi gelistirebilmeniz için, kendinize ait küçük projeler yaratmaniz ve kodlar yazmaniz. Baskalarinin kodlari ne kadar açiklayici ve bilgi verici olursa olsun, her programcinin teknigi farklidir, kendi tekniginizi gelistirebilmeniz için kendinize ait programlar yazmaniz gerekir.

Son olarak formdan aldiginiz bilgileri formatlayip e-posta yoluyla size gönderen ufak bir script örnegi verecegim, böylece nette en çok aranan scriptlerden birine sahip olmus olacaksiniz ;o)

<!-- formmail.php3 --> <?php **$kimden **= "*\\"Admin\\" <admin@adresim.com>*"; **$mesaj** = "*Isim: *" . **$isim** . "*\\n*"; **$mesaj** .= "*Soyisim: *" . **$soyad**. "*\\n*"; **$mesaj** .= "*Telefon: *" . **$telefon** . "*\\n*"; **$header** .= "*From: *" . **$kimden** . "*\\n*"; **$header** .= "*Reply-To:* " . **$reply-to** . "*\\n*"; **$header** .= "*Content-Type:* *text/plain; charset=iso-8859-9 \\n*"; **$header** .= "*Content-Transfer-Encoding: 8bit \\n*"; **$kime **= "*eposta@adresim.com*"; **$konu** = "*Formdan Maile Programi*"; **mail**(**$kime**, **$konu**, **$mesaj, $header**); ?>Yukardaki isim,soyisim ve telefon alanlarini (ya da keni istediginiz diger alanlari) içeren bir form yaratip ACTION degerini daha önceki örneklerde oldugu gibi "formmail.php3" dosyasina yönlendirin ve bunu HTML olarak kaydedin. **$kimden** gibi sizin belirtmeniz gereken alanlari degistirmeyi unutmayin. Iste, Türkçe destekli formmail programiniz hazir ;o)

[](javascript:history.go(-1))

[](PHP-2-13.md)

[](PHP-2-6.md)

[ ](javascript:window.external.AddFavorite('http://www.e-dersane.com','E-DERSANE.com - Internetle Yasamayi Ogretir!'))

Copyright © 2001- **[www](http://www.e-dersane.com)**[.**E-Dersane.com**](http://www.e-dersane.com)** - Offline Dersler**. All Rights Reserved.
**[](http://www.e-dersane.com)****[](http://www.php.org.tr)****PhP Offline Dersleri **bolumunde yayinlanan bütün metin ve makaleler GPL lisansli olup ayrintili bilgi için [GNU.org](http://www.gnu.org) adresine bakiniz.

---
*Kaynak: `PHP 2/ekitap-Anonim-PHP_Offline/ders2.htm`*
*Görseller: `PHP-2/gorseller/` (1 dosya)*
