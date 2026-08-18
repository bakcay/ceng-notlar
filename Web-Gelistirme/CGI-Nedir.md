# CGI Nedir

## GİRİŞ

## CGI Nedir?

CGI'nin uzun hali "Common Gateway Interface"dir. Türkçesi "Web Server'a Ortak Çıkış Kapısı" dir. Server'ın veritabanlarına, dökümanlara ve diğer programlara bilgi gönderebileceği (veya alabileceği), ve bu bilgiyi web üzerinden kullanıcılara sunabileceği bir metoddur. Kısaca web için programlama diyebiliriz yani. CGI programları değişik dillerde yazılabilir. Ama en popüleri Perl'dür ve Perl'ü anlatacağız.

## Neden CGI bilmeliyiz?

Bir web sayfası hazırlıyorsanız, sayfanızın kaç kişi tarafından ziyaret edildiğini bilmek, ya da sayfanızda ziyaretçilerin düşüncelerini mail adresinize gönderebileceği bir form olmasını istersiniz. Bugün profesyonelce hazırlanan web sayfaları form gönderme ve sayaç gibi basit scriptlerden tutun da karmaşık veritabanı scriptlerine varana kadar birçok değişik scriptle desteklenmektedir. Kısacası günümüzde CGI bilmek bir ayrıcalıktır.

## Başlangıç için neler gerekli?

Her ne kadar UNIX sistemi üzerinde Perl ile CGI programlamayı anlatacak olsak da başlangıç için UNIX bilgisine sahip olmanız gerekmiyor. Çünkü zaten bilmeniz gereken kısmı burada size anlatılacak. UNIX bilgisi gerekli değil dedik ama, tabi ki bir UNIX accountunuzun olması gerekiyor. Eğer yoksa size http://www.virtualave.net'de bir account açtırmanızı tavsiye ederim. Aslında tam olarak bir UNIX accountu vermiyorlar ama CGI scriptlerinizi çalıştırabileceğiniz bir cgi-bin dizininiz oluyor. Buraya FTP ile bağlanıp scriptlerinizi gönderebilirsiniz. Bu konuda daha ayrıntılı bilgi edinmek için web sitesini ziyaret ediniz.

Eğer UNIX değil de Windows NT kullanıyorsanız yine de buradaki programların çoğunu çalıştırabilir ve Perl öğrenebilirsiniz. Çoğu NT makinesi UNIX makinesinin çalıştırdığı kodları çalıştırabilir. Ama örneklerimizden bazıları UNIX'e özel yazıldığı için makinenizde çalışmayacaktır. Daha fazla bilgi için perl.com'un Perl Resources For Windows (Windows İçin Perl Kaynakları) listesini gözden geçirin.

Scriptlerinizi Windows kurulu bir bilgisayarda çalıştırmak için http://www.activestate.com/ActivePerl/download.htm adresinden ActivePerl'ü indirebilirsiniz. Eğer yazdığınız scriptleri UNIX sistemine göndermeden önce kendi bilgisayarınızda denemek istiyorsanız bu programı mutlaka indirin.

UNIX sistemine telnet ile bağlanacağımız için bir telnet programına ihtiyacınız olacak tabi. Windows'la birlikte gelen basit telnet programı da işinizi görür. Windows kullanıcısı değilseniz ya da başka bir program kullanmak istiyorsanız tavsiye edeceğim program:

Macintosh için: NCSA Telnet
Windows için: CRT

Eğer scriptlerinizi kendi bilgisayarınızda yazıp gönderecekseniz tavsiye edeceğim program:

Macintosh için: Fetch
Windows için: CuteFTP

Okuma kolaylığı açısından Perl ve HTML kodlarını sabit genişlikli bir font kullanarak yazacağım. Mesela:

print "Bu bir Perl kodu.\\n";

Ayrıca UNIX komut satırında yazmanız gereken komutları anlatırken <Dosya Adı> gibi < ve > karakterleri arasında yazacağım kısımları kendinize uygun şekilde değiştirmeniz gerekecek. Örneğin chmod 755 <dosya adı> dediğim zaman yapmanız gereken dosyanızın adı sayac.cgi ise komut satırında chmod 755 sayac.cgi yazmak.

Sanırım bu kadar hazırlık yeterli. Şimdi ilk bölüme geçebiliriz.

## **Bölüm 1: Başlangıç**

Programlama dili olarak Perl'ü seçtik, çünkü basit bir dil, kolay öğreniliyor ve karmaşık problemleri halledebilecek kadar da güçlü. Ayrıca hem ücretsiz hem de bulunması çok kolay. Zaten çok büyük bir ihtimalle UNIX server'ınızda ya da NT makinenizde kuruludur. Yine de download etmeniz gerekiyorsa www.perl.com'u ziyaret ediniz. Perl ile yazdığınız scriptleri derlemenize gerek yoktur. Scriplerinizi yazar ve çalıştırırsınız (Daha doğrusu web server'ınız çalıştırır). Script kendi başına sadece text kodudur. Aslında bütün işi web server'ınızda kurulu olan Perl yorumlayıcısı yapar. Bunun size sağladığı avantaj yazdığınız scriptleri ya hiçbir değişiklik yapmadan ya da çok küçük bir iki değişiklikle istediğiniz servera kopyalayabilecek olmanız. Dezavantajı ise scripti çalıştırmadan hatalı olup olmadığını anlayamamanız.

Perl scriptlerinizi kendi bilgisayarınızda istediğiniz text editörü ile (Notepad, SimpleText vb.) ya da UNIX'te yazabilirsiniz. UNIX kullanıyorsanız pico'yu deneyin. Basit ve kullanımı kolay bir text editörü. UNIX komut satırında pico <dosya adı> yazarak yeni bir dosya ya da varolan bir dosyayı açabilirsiniz. Pico ile ilgili daha fazla bilgi almak için man pico yazınız.

Scriptlerinizi kendi makinenizde yazıp FTP ile gönderecekseniz dikkat etmeniz gereken husus binary değil ASCII olarak göndermek. CuteFTP kullanıyorsanız sorun yok. Ama WS FTP programı Perl dosyaları için genelde ASCII değil binary kullanıyor.

Scriptlerinizi server'ınızda CGI scriptlerini çalıştırabileceğiniz dizine (public\_html ya da /home/httpd/cgi-bin olabilir) upload etmelisiniz. Başka bir dizine upload etmişseniz daha sonra da taşıma işlemini yapabilirsiniz. UNIX'te taşıma işlemini şu komutla yapabilirsiniz:

mv <taşınacak dosya> <taşınacağı dizin> (Daha fazla bilgi için man mv)

Scriptinizi gerekli dizine taşıdıktan sonra bu dosyayı "çalıştırılabilir" hale getirmeniz gerekir. Bunun için kullanmanız gereken komut:

chmod 755 <dosya adı>

Bu komut dosyanın sizin tarafınızdan okunabilir, yazılabilir ve çalıştırılabilir, diğer bütün kullanıcılar tarafından da okunabilir ve çalıştırılabilir hale getirilmesini sağlar.

Aynı işi çoğu FTP programı ile yapabilirsiniz. Fakat dikkat etmeniz gereken kısım bütün kullanıcılara okuma ve çalıştırma hakkı vermek ve tabi ki sadece kendinize yazma hakkı vermek.

UNIX ve Perl'de büyük küçük harf ayrımı vardır. Yani UNIX'te "perl" ile "PERL" aynı şey değildir.

## Perl Scriptinin Temelleri

Bir HTML dosyasının yapısında <head> ve <body> etiketlerinin mutlaka bulunması gerektiği gibi bir Perl scriptinin ilk satırında

#!/usr/bin/perl

satırının mutlaka bulunması gerekir. Bu satır server'a bu dosyanın bir Perl scripti olduğunu ve Perl'ün nerede olduğunu söyler. Bu satır sisteminizde Perl'ün nerede olduğuna bağlı olarak değişebilir. Bunu öğrenmenin en emin yolu which perl ya da whereis perl komutunu kullanmaktır. Perl sisteminizde kurulu ise Perl'ün hangi dizinde olduğu yazacaktır.

Server'a Perl'ün yerini tanıttıktan sonra Perl kodlarınızı yazabilirsiniz. Hatırlamanız gereken önemli bir konu Perl'de büyük küçük harf ayrımının olduğu. Yani Perl için "x" ile "X" aynı şeyler değildir. Ayrıca çoğu Perl kodunun sonunda noktalı virgül (;) kullanmalısınız (Bazı döngü ve özel yapılar hariç).

Şimdi birlikte ilk scriptimizi yazalım. Yeni bir dosya oluşturun ve şunları yazın. (Daha iyi aklınızda kalması açısından Kopyala - Yapıştır yöntemini kullanmamanızı tavsiye ederim.)

#!/usr/bin/perl
print "Merhaba\\n;"

Bu dosyayı "ilkscript.pl" adıyla kaydedin ve UNIX komut satırında şunu yazın:

chmod 755 ilkscript.pl

Bu komut dosyanın erişim yetkilerini değiştirerek onu çalıştırılabileceğiniz hale getirir. Bunu her yeni script yazışınızda yapmanız gerekir. Fakat varolan bir dosya üzerinde değişiklik yaptığınız zaman bu komutu vermenize gerek yoktur.

Şimdi, yazdığınız scripti çalıştırmanız için vermeniz gereken komut:

./ilkscript.pl

Eğer herşey yolunda gitmişse ekranda "Merhaba" yazması gerekir.

| ** Olmadı mı?** Eğer scriptiniz çalışmazsa şunları kontrol edin: **1.** Scriptinizi ASCII olarak upload ettiniz mi? **2.** Scriptinizin ilk satırı #!/usr/bin/perl mü? **3.** Perl'ün yeri gerçekten #!/usr/bin/perl mü yoksa başka bir dizinde mi? Perl'ün nerede olduğunu which perl ya da whereis perl yazarak bulabilirsiniz. |
| --- |

## CGI Scriptinin Temelleri

CGI programları aynı zamanda birer Perl scriptidir. Fakat aralarındaki önemli bir fark CGI programlarının genelde bir web sayfası üretmesidir. Örneğin bir form gönderildikten sonra mesajın gönderildiğine dair yeni bir sayfa açılır. Eğer yazdığınız script bir HTML sayfası oluşturacaksa herhangi bir yazı yazdırmadan önce

print "Content-type:text/html\\n\\n";

satırını mutlaka yazmalısınız. Unutulması ihtimaline karşı en başa yazılması daha iyi olur (#!/usr/bin/perl satırından sonra tabi).

Bu satır web browser'ınıza kendisine gönderilecek bilginin bir HTML sayfası olduğunu söyler. Eğer bu satırı yazmayı unutursanız ya da bu satırdan önce başka birşey yazdırırsanız browser <Internal Server Error> (Dahili Server Hatası) verir.

Şimdi yaptığımız Perl scriptini biraz değiştirelim ve web sayfası gösteren bir CGI scriptine çevirelim.

Önce dosyanın uzantısını .cgi olarak değiştirelim. UNIX'te bunu

mv ilkscript.pl ilkcgi.cgi

komutunu vererek yapabilirsiniz. Daha sonra bu dosyanın içeriğini şu şekilde değiştirin:

#!/usr/bin/perl

print "Content-type:text/html\\n\\n";

print "<html><head><title>Deneme Sayfası</title></head>\\n";
print "<body>\\n";
print "<h2>Merhaba</h2>\\n";
print "</body></html>\\n";

Eğer scriptinizdeki değişiklikleri UNIX üzerinde yapmışsanız erişim yetkilerini tekrar düzenlemenize gerek yoktur. Ama kendi bilgisayarınızda yazıp upload etmişseniz chmod 755 ilkcgi.cgi komutunu verip erişim yetkilerini değiştirin ve ./ilkcgi.cgi komutu ile scriptinizi çalıştırın. Ekrana HTML kodları gelecektir. AMA eğer yazdığınız kodlarda bir hata varsa o zaman ekranda hatanın kaçıncı satırda olduğu yazar. Bu da özellikle uzun ve karmaşık scriptler yazarken olası hatayı düzeltmemizde bize oldukça kolaylık sağlar.

Şimdi de browser'ınızın adres satırına tam adresini yazarak scriptinizi çağırın. Browser'ınızda "Merhaba" yazdığını göreceksiniz.

| **Olmadı mı?** Scriptinizin çalışmamasının nedeni şunlar olabilir: **1.** Eğer karşınıza "Merhaba" yerine Perl kodları çıkmışsa scriptin uzantısını .cgi olatak değiştirmemiş olabilirsiniz. Ya da scriptin bulunduğu dizin CGI programlarını çalıştıracak şekilde ayarlanmamıştır (CGI scriptlerinizi hangi dizinde çalıştırabileceğinizi server'ınızın yöneticisine sormalısınız). **2.** Browser'ınız "Internal Server Error" hatası veriyorsa scriptinizi ./ilkcgi.cgi komutu ile çalıştırın. Ekranda hatanın nerede olduğu yazacaktır. |
| --- |

Yukarıdaki scripti şu şekilde yazarsak her satırda print yazmaktan kurtuluruz:

#!/usr/bin/perl

print "Content-type:text/html\\n\\n";

print <<HTMLSonu;
<html><head><title>Deneme Sayfası</title></head>
<body>
<h2>Merhaba</h2>
</body></html>

HTMLSonu
;

print <<HTMLSonu; satırında << ile HtmlSonu arasında boşluk olmadığına dikkat edin.

Bu sayfada Perl kodları, daha anlaşılır olması açısından satır girintileri kullanarak yazılmıştır. Perl kodlarını yazarken mutlaka ilk sütundan başlayarak yazılmalıdır. Özellikle HTMLSonu satırından önce kesinlikle boşluk bırakılmamalıdır. Eğer bırakılırsa scriptiniz çalışmaz.

HTML kodlarını bu yöntemle yazdırırsak aşağıdaki örnekte olduğu gibi print komutunu kullanırken iç içe çift tırnak (") karakteri kullanmak zorunda olduğumuz zaman çift tırnaktan önce ters bölü (\\) karakteri yazmak zorunda kalmayız.

print "<a href=\\"http://cc.sau.edu.tr/\\">"

print komutunda iç içe tırnak karakterleri kullanmak için yukarıdaki gibi çift tırnaktan önce ters bölü karakterini yazmak zorundayız.

## **Bölüm 2: Perl Değişkenleri**

Perl'de işe yarar programlar yazabilmek için Perl değişkenlerini tanımamız gerekir. Değişken demek, değerleri saklayacağımız yer demektir. Değişkene değer atadıktan sonra program boyunca bu değeri geri çağırabilir, kullanabilir ve değiştirebiliriz. Perl'de 3 çeşit değişken mevcuttur: Scalar, Array ve Hash değişkenler.

## Scalar Değişkenler

Scalar değişkenlere tek bir değer atanır. Bu değer bir sayı, bir cümle ya da başka bir scalar değişken olabilir. Scalar değişkenlerin adlarının başında $ işareti bulunur. Örneğin $x, $y, $z, $adres, $kullanici birer scalar değişken adıdır. Scalar değişkenlere değer atama işlemi de aşağıdaki örneklerde görüldüğü gibi yapılır.

$sayi = 1;
$isim = "Sinan";
$pi = 3.141592;

Değişkenleri kullanmadan önce tanımlamanıza gerek yoktur. Ayrıca Perl değişkenleri program içinde tip de değiştirebilir. İşte bir örnek:

$sihir = 23;
$sihir = "Sihirli sayımız $sihir";

Bazı programlama dillerinin tersine Perl bu durumu kabul eder ve bir hata mesajı vermez.

Şimdi ilkscript.pl isimli scripti biraz değiştirelim ve birkaç değişken ekleyelim:

#!/usr/bin/perl
$kursadi = "CGI Programlama";
print "Merhaba. Adın ne?\\n";
$siz = <STDIN>;
chomp($siz);
print "Merhaba $siz. $kursadi kursuna hoş geldiniz.\\n";

Scripti kaydedin ve UNIX'te çalıştırın. Program size isminizi soracak ve birşeyler yazıp enter'a basmanızı bekleyecektir. Bu işlem

$siz = <STDIN>;

satırı dolayısıyla gerçekleşir. Yazdığınız yazı $siz değişkenine atanır. Yazdığınız yazının sonundaki enter tuşunu simgeleyen "Carriage Return" karakteri aşağıdaki komut satırı ile silinir.

chomp($siz);

Aşağıdaki satır işletildiğinde değişkenlerin yerine atandığı değerler ekranınızda görünür. En sondaki \\n Per'de "Carriage Return" işaretini temsil eder. Yani programa, yazıyı yazdıktan sonra enter'a basmasını söyler.

print "Merhaba $siz. $kursadi kursuna hoş geldiniz.\\n";

## Array Değişkenler

Array'ın Türkçe karşılığı "Dizi"dir. Array değişkenler için değerler listesi diyebiliriz. Scalar değişkenler tek bir değer içermesine karşın array değişkenler birden fazla değer içerirler. Array değişken adlarının başında at işareti (@) bulunur. İşte bir örnek:

@renkler = ("sari","kirmizi","yesil");

Perl'de dizi indisleri 0'dan başlar. Yani @renkler dizisinin ilk elemanını $renkler\[0\] verir. @renkler dizisinin tek bir elemanının değerini göstereceği zaman @ işareti yerine $ işareti kullanılır. $ işareti tek bir değeri, @ işareti ise bütün diziyi kastettiğimiz anlamına gelir.

Bir dizinin tüm elemanları şu şekilde yazdırılabilir:

#!/usr/bin/perl

\# bu bir açıklamadır.
# diyez (#) işareti ile başlayan bütün satırlar açıklamadır.

@renkler = ("sari","kirmizi","yesil");

print "$renkler\[0\]\\n";
print "$renkler\[1\]\\n";
print "$renkler\[2\]\\n";

Fakat elbette ki bunu yapmanın daha kolay bir yolu var. foreach yapısı kullanılarak dizileri rahatlıkla yazdırabiliriz.

#!/usr/bin/perl

\# bu bir açıklamadır.
# diyez (#) işareti ile başlayan bütün satırlar açıklamadır.

@renkler = ("sari","kirmizi","yesil");

foreach $i (@renkler) {
print "$i\\n";
}

foreach döngüsünün her tekrarlanışında $i değişkenine @renkler dizisinin bir elemanı atanır. İlk tekrarda $i değişkeninin değeri "sari", ikinci tekrarda "kirmizi" ve üçüncü tekrarda "yesil" olur. { ve } parantezleri döngünün başlangıç ve sonunu belirtir. Yani bu parantezler arasında kalan komutlar $i değişkeninin bütün değerleri için tekrarlanır.

## **Dizi Fonksiyonları**

Perl'de dizilere değer atamayı ve dizilerden değer okumayı kolaylaştıran fonksiyonlar mevcuttur.

@renkler = ("sari","kirmizi","yesil","mavi","turuncu","bordo");

$ilkrenk = pop(@renkler);
# $ilkrenk değişkenine @renkler dizisinin ilk değeri olan "sari" atanır.

$sonrenk = shift(@renkler);
# $sonrenk değişkenine @renkler dizisinin son değeri olan "bordo" atanır.

Bir diziye değer eklemek için push fonksiyonu kullanılır:

push(@renkler,"gri");
# @renkler dizisinin sonuna "gri" ilave edilir.

@yenirenkler = ("lacivert","pembe");

push(@renkler,@yenirenkler);
# @yenirenkler dizisindeki değerler @renkler dizisinin sonuna ilave edilir.

Dizilerle ilgili işe yarayabilecek birkaç fonksiyon daha:

sort(@renkler);
# @renkler dizisinin elemanlarını alfabetik sıraya koyar.

reverse(@renkler);
# @renkler dizindeki elemanların diziliş sırasını ters çevirir.

@join(", ",@renkler);
# @renkler dizisini elemanların arasında ", " olacak şekilde birleştirir.

$uzunluk = $#renkler;
# $uzunluk değişkenine @renkler dizisinin uzunluğu atanır.

## Hash Değişkenler

Hash değişkenleri Array değişkenlerin özel bir hali olarak düşünebiliriz. Hash değişken adlarının başında yüzde işareti (%) bulunur. Hash değişkenler öğe çiftlerinden oluşur: Anahtar ve Değer. Aşağıdaki örneği inceledikten sonra daha rahat anlayacağınızı tahmin ediyorum:

| **Değişken ****** | **Anahtar ****** | **Değer ****** |
| --- | --- | --- |
| %sayfalar = ( | "sinan", | "http://www.sinanilyas.cjb.net", |
|  | "koray", | "http://cc.sau.edu.tr/~ktoksoz", |
|  | "baris", | "http://turk.eu.org/uruzgar"); |

Aynı Hash şu şekilde de tanımlanabilir:

| %sayfalar = ( | "sinan" => | "http://www.sinanilyas.cjb.net", |
| --- | --- | --- |
|  | "koray" => | "http://cc.sau.edu.tr/~ktoksoz", |
|  | "baris" => | "http://turk.eu.org/uruzgar"); |

%sayfalar değişkeninde anahtar olarak kişinin ismini, değer olarak da web sayfasının adresi saklanır. Tıpkı Array'de olduğu gibi, bir Hash değişkenden tek bir değer okunacağı zaman $ işareti kullanılır.

print "$sayfalar{'baris'}\\n";

Yukarıdaki satır Barış'ın web sayfasının adresini yazdırır. Eğer değişkendeki bütün değerleri yazdırmak istiyorsanız bir foreach döngüsü kullanabilirsiniz:

foreach $anahtar (keys %sayfalar) {
print "$anahtar'ın web sayfasının adresi: $sayfalar{$anahtar}\\n";
}

Bu örnekte %sayfalar değişkeninin anahtarlarını öğrenebilmek için bir hash değişkeninin anahtarlarını dizi olarak veren keys fonksiyonu kullanılmıştır. keys fonksiyonunun tek bir dezavantajı vardır: Anahtarları rastgele bir sırayla vermesi. Yani bu örnekte kimin adresinin önce, kiminkinin sonra ekrana yazılacağı belli değildir. Adresleri belli bir sırayla yazdırmak istiyorsanız aşağıda gösterildiği gibi foreach döngüsünde anahtarları kendiniz yazmalısınız.

foreach $anahtar ("sinan","koray","baris") {
print "$anahtar'ın web sayfasının adresi: $sayfalar{$anahtar}\\n";
}

Hash değişkenler formla gönderilen verileri ayırmada çok işimize yarayacak. Örneğin $form{'soyad'} bize formunuzdaki soyad kutucuğuna yazılan değeri verecek. Televizyoncuların deyimiyle: "AZ SONRA!" :)

Neyse, biz yine işimize bakalım ve adres listesi veren bir web sayfası üreten yeni bir CGI scripti yazalım. Tabi ki Hash değişken kullanarak.

#!/usr/bin/perl

%sayfalar = ("sinan" => "http://www.sinanilyas.cjb.net",
"koray" => "http://cc.sau.edu.tr/~ktoksoz",
"baris" => "http://turk.eu.org/uruzgar" );

print "Content-type:text/html\\n\\n";

print <<IlkKisim;
<html><head><title>Adres Listesi</title></head>
<body>
<h2>Adres Listesi</h2>
<ul>
IlkKisim
;

foreach $anahtar (keys %sayfalar) {
print "<li><a href=\\"$sayfalar{$anahtar}\\">$anahtar</a>\\n";
}

print <<SonKisim;
</ul>
<p>
</body>
</html>
SonKisim
;

Yukarıdaki scripti "adreslistesi.cgi" adıyla kaydedin ve çalıştırılabilmesi için erişim yetkilerini 755 olacak şekilde değiştirin. Sonra da web browser'ınızdan çağırın. Açılan sayfada isme tıkladığınız zaman o kişinin web sayfasının açıldığını göreceksiniz.

## **Bölüm 3: CGI Ortam Değişkenleri**

Ortam değişkenleri CGI programı çalıştırılıdığı zaman browser'ınızın (ve web server'ınızın) programa gönderdiği bilgilerdir. Ortam değişkenleri %ENV isimli Hash değişkende saklanır.

| ** CGI Ortam Değişkenleri** |  |
| --- | --- |
| DOCUMENT\_ROOT | Server'ınızın kök dizinini verir. |
| HTTP\_COOKIE | Eğer varsa ziyaretçinin "cookie"sini verir. |
| HTTP\_HOST | Server'ınızın "hostname"ini verir. |
| HTTP\_REFERER | Scriptin çağrıldığı sayfanın adresini verir. |
| HTTP\_USER\_AGENT | Ziyaretçinin browser'ının tipini verir. |
| PATH | Server'ınızın "system path"ini verir. (Genelde /bin, /usr/sbin vs.) |
| QUERY\_STRING | GET metodu ile yollanan bilgiyi verir. |
| REMOTE\_ADDR | Ziyaretçinin IP adresini verir. |
| REMOTE\_HOST | Ziyaretçinin "hostname"ini verir. (\*) |
| REMOTE\_PORT | Ziyaretçinin web server'ınıza bağlandığı portu verir. |
| REMOTE\_USER | Ziyaretçinin kullanıcı adını verir. (.htaccess korumalı sayfalar için) |
| REQUEST\_METHOD | Bilgi gönderme metodunu verir. (GET ya da POST) |
| SCRIPT\_FILENAME | Scriptin tam yolunu verir. |
| SERVER\_ADMIN | Server'ınızın webadmin'inin e-mail adresini verir. |
| SERVER\_NAME | Server'ınızın tam domain adını verir. (Örn: cc.sau.edu.tr) |
| SERVER\_PORT | Server'ınızın dinlemede olduğu portu verir. |
| SERVER\_SOFTWARE | Serverdaki web server programını verir. (Örn: Apache 1.3) |

(\*) Eğer server'ınızda "reverse-name-lookups" yoksa REMOTE\_HOST ziyaretçinin IP adresini verir.

Bazı server'larda bunlardan başka değişkenler de olabiliyor. Daha fazla bilgi için server'ınızın dökümanlarını inceleyiniz. Farketmişseniz bazı değişkenler server'la ilgili, bazıları ise ziyaretçi ile ilgili bilgileri içeriyor. Server'la ilgili olanların programa bildirdiği bilgiler o server'da çalışan bütün CGI programları için aynı olacaktır. Fakat ziyaretçi ile ilgili bilgiler program her çalıştırıldığında farklı olabilir.

Her CGI çalıştırıldığında bütün ortam değişkenleri atanmaz. REMOTE\_USER değişkeni sadece .htaccess dosyası ile korunan dizin ya da altdizinler için atanır. Bu durumda REMOTE\_USER değişkeninin alacağı değer .htaccess dosyasındaki kullanıcı adıdır.

%ENV değişkeni CGI çalıştırıldığında otomatik olarak atanır ve isterseniz tamamını isterseniz sadece belli değerleri kullanabilirsiniz. Mesela aşağıdaki kod ile ziyaretçinin IP adresini yazdırabilirsiniz.

print "IP adresiniz: $ENV{'REMOTE\_ADDR'}\\n";

Şimdi bütün ortam değişkenlerini yazdıran bir CGI yazalım. Yeni bir dosya oluşturun, "ortam.cgi" adıyla kaydedin ve içine şunları yazın:

#!/usr/bin/perl

print "Content-type:text/html\\n\\n";
print <<HTMLSonu;
<html><head><title>Ortam Değişkenleri</title></head>
<body>
HTMLSonu
;

foreach $anahtar (sort(keys %ENV)) {
print "$anahtar = $ENV{$anahtar}<br>\\n";
}

print "</body></html>";

Scripti kaydedin, erişim yetkilerini 755 olarak ayarlayın ve browser'ınızdan çağırın. Eğer hata mesajı alırsanız programı UNIX'te çalışmayı deneyip hatanın nerede olduğunu öğrenebileceğinizi hatırlayın.

Bu örnekte sort fonksiyonu kullanılarak %ENV değişkeninin anahtarları alfabetik sıraya koyduk. Perl'ün sort fonksiyonu karakter değerlerini karşılaştırdığı için sayıları düzgün bir şekilde sıraya koyamaz.

## **Basit Bir Sorgu Formu**

Bir HTML formundan CGI'a bilgi göndermek için iki yol vardır. GET ve POST. Form bilgisinin server'a nasıl yollandığını bu metodlar belirler. GET metodunda formla gönderilen bilgiler URL'in bir parçası olarak gönderilir ve QUERY\_STRING ortam değişkenine atanır. POST metodunda nasıl gönderildiğini bir sonraki bölümde anlatacağız.

QUERY\_STRING değişkenine birkaç değişik yolla atama yapabiliriz. Birinci yöntem aşağıda görüldüğü gibidir.

http://hammer.prohosting.com/cgi-bin/ortam.cgi?deneme1
http://hammer.prohosting.com/cgi-bin/ortam.cgi?deneme2
http://hammer.prohosting.com/cgi-bin/ortam.cgi?deneme3

Yukarıdaki linklerin her birine tıklayın. QUERY\_STRING değişkeninin değerinin soru işaretinden sonra gelen yazı olduğunu göreceksiniz. Bu örneklerde QUERY\_STRING değişkeni "deneme1","deneme2" ve "deneme3" değerlerini alır.

Bir başka yöntem de aşağıdaki gibi basit bir form hazırlamaktır.

<form action="http://hammer.prohosting.com/~sinan/cgi-bin/ornek/ortam.cgi" method="GET">
Buraya birşeyler yazın: <input type="text" name="ornek\_yazi" size=30><p>
</form>

"Gönder" düğmesinin olmadığını farketmişsinizdir sanırım. GET metodu ile sadece enter'a basarsınız ve form gönderilir. (Bu yöntem sadece bir tane girdi alanı olduğu zaman işe yarar. Birden fazla girdi alanını göndermek için mutlaka "Gönder" düğmesi koymalısınız.)

Yukarıdaki kodları kullanarak bir HTML dosyası hazırlayın ve "get.html" adıyla kaydedip browser'ınızla açın. Daha sonra form alanına birşeyler yazın ve enter'a basın. QUERY\_STRING değişkeninin değeri aşağıdaki gibi olur.

$ENV{'QUERY\_STRING'} = ornek\_yazi=iste+yazdiginiz+yazi

Eşittir (=) işaretinin solundaki yazı form alanının adıdır. Sağındaki yazı ise formdaki kutucuğa yazdığınız yazıdır. FAKAT farkettiğiniz gibi boşlukların yerini artı (+) işareti almış. Hatta çeşitli noktalama işaretleri ve özel karakterlerin yerine %-kod şeklinde özel kodlar çıkmış.

Buna "URL Kodlama" denir ve ister GET metodu ister POST metodu kullanılsın, herhangi bir form ile bilgi gönderildiği zaman meydana gelir.

Perl scriptiniz bu bilgiyi eski haline getirebilir fakan uzun ve karmaşık bilgiler yollandığında POST metodunu kullanmak daha iyidir. GET metodu daha çok veritabanından bilgi aratma gibi tek alanlı formlar için elverişlidir.

GET metodu ile birden fazla alanlı formları da gönderebilirsiniz.

<form action="http://hammer.prohosting.com/~sinan/cgi-bin/ornek/ortam.cgi" method="GET">
Adınız: <input type="text" name="ad" size=30><p>
Soyadınız: <input type="text" name="soyad" size=30><p>
<input type="submit" value="Gönder">
</form>

Bo formla gönderilen bilgiler aşağıdaki gibi görünür.

$ENV{'QUERY\_STRING'} = ad=umut+baris&soyad=ruzgar

Değerler & işareti ile ayrılmıştır. Bu iki değeri birbirinden ayırmak için Perl'ün split fonksiyonunu kullanacağız.

@degerler = split(/\\&/,$ENV{'QUERY\_STRING'});
foreach $i (@degerler) {
($alanadi, $deger) = split(/=/,$i);
print "$alanadi = $deger\\n";
}

split fonksiyonu bir karakter sırasını, belirtilen karakter ya da karakterlerden ayırarak bir dizi oluşturur. Örneğimizin ilk satırında QUERY\_STRING değişkeninin değeri & işaretinden ikiye ayrılmıştır. & işaretinden önce \\ kullanılmasının nedeni & işaretinin Perl'de özel bir anlamı olmasıdır. (Perl'de bazı özel karakterleri kullanırken başına \\ işareti koymamız gerekebilir). Bu ayırma işlemi sonucu @degerler dizisine iki değer atanır: ad=umut+baris ve soyad=ruzgar. foreach döngüsünde önce = işaretinden alan adı ve alanlara yazılan yazılar birbirinden ayrılarak $alanadi ve deger değişkenlerine atanır. Sonra da birbirinden ayrılmış olan bu değerler yazdırılır.

GET metodu hakkında bazı uyarılar: Bu metod bilgi göndermek için güvenli değildir. Bu yüzden şifre ve kredi kartı bilgileri gibi gizli bilgileri gönderirken asla bu metodu kullanmayınız. Gönderilen bilgi URL'in bir parçası olarak gönderildiği için server'ın log dosyalarında kaydedilir ve log dosyaları da server'daki bütün kullanıcılar tarafından okunabilir. Gizli bilgiler bir sonraki bölümde göreceğimiz POST metodu ile güvenli bir biçimde gönderilebilir.

## **Bölüm 4: Form İşleme**

POST metodunda bilgiler URL ile birlikte gönderilmediği GET metodundan daha güvenlidir. POST metodunun GET metoduna bir diğer üstünlüğü de daha fazla bilgi gönderebilmesidir. Ayrıca, GET metodu ile gönderilen bilgiler web browser, web server ya da proxy server'ın kaşe belleğinde (cache) saklanabilir fakat POST metodu ile bilgiler her defasında yeniden gönderilir. Dezavantajı ise POST ile gönderilen bilgiler daha karmaşık olacağından dolayı bu bilgileri çözmek için daha biraz daha karmaşık bir kod yazmamız gerekir.

Web server, form bilgilerini CGI programına kodlayarak gönderir. Alfanumerik karakterler olduğu gibi gönderilir; boşluklar artı (+) işaretine çevrilir; tab, çift tırnak (") gibi özel işaretler de "%HH" şeklinde kodlanır. Burada "HH" karakterin ASCII karşılığının hexadesimal (16'lık sistemdeki) değeridir. Bu kodlama işlemine "URL kodlama" denir. Aşağıdaki tabloda sık kullanılan bazı karakterlerin kodlanmış karşılıklarını görebilirsiniz.

| **Normal Karakter** | **Kodlanmış Hali** |
| --- | --- |
| \\n (enter) | %0A |
| \\t (tab) | %09 |
| / | %2F |
| ~ | %7E |
| : | %3A |
| ; | %3B |
| @ | %40 |
| & | %26 |

Gönderilen bilgiyle işe yarar şeyler yapabilmek için CGI bu kodlanmış bilgiyi çözmelidir. Neyse ki Perl'de substitute ve translate komutlarıyla bunu yapmak oldukça kolaydır. Perl, karakter içerisinde arama yapma ve değiştirme konusunda oldukça yeteneklidir. substitute komutunun temel yazılış biçimi aşağıdaki gibidir.

$yazi =~ s/aranan/yerinekonan/;

Bu örnek $yazi scalar değişkeninde aranan kelimesinin yerine yerinekonan kelimesini koyar. Araya konan operatör =~ (eşittir ve yanında tilde) işaretidir.

Daha iyi anlaşılacağını düşündüğüm başka bir örnek:

$selamlama = "Merhaba. Benim adım xisimx.\\n";
$selamlama =~ s/xnamex/Sinan/;
print $selamlama;

Yukarıdaki örnek "Merhaba. Benim adım Sinan." yazdıracaktır. $selamlama değişkeninde "xisimx"in yerini "Sinan"ın aldığına dikkat edin.

Buna yakın fakat bir parça farklı bir komut da translate komutudur.

$yazi =~ tr/arananlistesi/yerinekonanlistesi/;

Bu komut "arananlistesi"ndeki bütün karakterleri "yerinekonan" listesindekilerle değiştirir. İşte bir örnek:

$kucukh =~ tr/\[A-Z\]/\[a-z\]/;

Bu örnek bütün yazıyı küçük harfe çevirir. \[A-Z\]'deki parantezler karşılaştırılacak karakter sınıfını belirtir.

Şimdi tekrar formlara dönelim. Formla gönderilen bilginin kodunu çözmeniz için bilgide iki değişiklik yapmalısınız:

$value =~ tr/+/ /;
$value =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;

İlk satırda + işaretleri boşluğa çevrilir. İkinci satırda ise pack() fonksiyonu kullanılarak %HH hex çiftleri ASCII karşılıklarına çevrilir.

Şimdi "post.cgi" adında yeni bir CGI hazırlayalım.

#!/usr/bin/perl

print "Content-type:text/html\\n\\n";

read(STDIN, $tampon, $ENV{'CONTENT\_LENGTH'});
@ciftler = split(/&/, $tampon);
foreach $cift (@ciftler) {
($isim, $deger) = split(/=/, $cift);
$deger =~ tr/+/ /;
$deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;
$FORM{$isim} = $deger;
}

print "<html><head><title>Form Bilgileri</title></head><body>";
print "<h2>Formla gönderilen bilgiler:</h2>\\n";

foreach $anahtar (keys(%FORM)) {
print "$anahtar = $FORM{$anahtar}<br>";
}

print "</body></html>";

Şimdi yukarıdaki kodları açıklayalım. Form ile gönderilen bilgi önce $tampon scalar değişkenine okunuyor. Sonra & işaretlerinden ayrılarak elde edilen "formdegiskeni=deger" şeklindeki form alanı bilgileri @ciftler dizisine yerleştiriliyor. Sonra foreach döngüsünde herbir form alanı bilgisi = işaretinden ayrılıyor ve URL kodu çözülerek %FORM Hash değişkenine atanıyor. %FORM değişkenindeki anahtar adları form alanının adıdır. Mesela <input type="text" name="**ad**" size=30> HTML kodunda koyu yazılan "ad" değeri form alanının adıdır. Formunuzda "ad" ve "soyad" isimli iki form alanı varsa scriptinizde bu değerleri $FORM{'ad'} ve $FORM{'soyad'} şeklinde kullanabilirsiniz.

Aşağıdaki örneği inceleyerek split fonksiyonunun nasıl çalıştığını hatırlayalım.

$yazi = "sari&kirmizi&yesil";
@renkler = split(/&/,$yazi);

@renkler değişkeninin yeni değeri ("sari","kirmizi","yesil") olur.

Şimdi de scriptimizi denemeye geldi sıra. Form için aşağıdaki kodları kullanarak bir HTML dosyası oluşturun ve "post.html" adıyla kaydedin.

<form action="http://hammer.prohosting.com/~sinan/cgi-bin/ornek/post.cgi" method="POST">
<pre>
Adınız: <input type="text" name="ad" size=30><br>
Soyadınız: <input type="text" name="soyad" size=30><br>
</pre>
<input type="submit" value="Gönder">
<input type="reset" value="Tümünü Sil">
</form>

İsterseniz scriptimizi biraz daha geliştirelim. Scriptimiz form bilgilerini mail adresimize göndersin. İlk önce sistemimizde sendmail programının nerede olduğunu bulalım. Bunu öğrenmek için which sendmail ya da whereis sendmail komutunu kullanabilirsiniz. (benim kullandığım serverda bu programın yeri /usr/sbin/sendmail olduğundan örneklerimizde bu şekilde kullanacağız. Eğer sizin server'ınızda farklı bir yerde ise kendi server'ınızdaki yerini yazmanız gerekir.)

**Not:** @ işaretini çift tırnak arasında ya da print <<HTMLSonu bloğunda kullanırken önüne "silyas\\@esentepe.sau.edu.tr" örneğindeki gibi \\ işareti koymalısınız. Tek tırnak arasında 'silyas@esentepe.sau.edu.tr' örneğinde olduğu gibi \\ işareti koymadan güvenle kullanabilirsiniz.

#!/usr/bin/perl

print "Content-type:text/html\\n\\n";

read(STDIN, $tampon, $ENV{'CONTENT\_LENGTH'});
@ciftler = split(/&/, $tampon);
foreach $cift (@ciftler) {
($isim, $deger) = split(/=/, $cift);
$deger =~ tr/+/ /;
$deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;
$FORM{$isim} = $deger;
}

$mailprog = '/usr/sbin/sendmail';

# bunu kendi mail adresinizle değiştirin

$gonderilen = 'silyas@esentepe.sau.edu.tr';

# burada maili göndermek üzere sendmail programı açılıyor
# eğer sendmail programı bulunamazsa hata alt programı (en altta)
# işletilerek programın bulunamadığı yazıyor

open (MAIL, "|$mailprog -t") or &hata("$mailprog bulunamadı!\\n");

# sendmail programına mailin kime gönderileceği bildiriliyor

print MAIL "To: $gonderilen\\n";

# sendmail programına ziyaretçinin email adresi bildiriliyor.
# bu "Yanıtla" tuşuna bastığınızda işe yarar
# kullanmak zorunda değilsiniz
# formunuzda 'email' ve 'isim' kutularının bulunduğu varsayılmıştır.

print MAIL "Reply-to: $FORM{'email'} ($FORM{'isim'})\\n";

# sendmail programına mailin konusu gönderiliyor
# konudan sonra iki tane \\n olduğuna dikkat edin

print MAIL "Subject: Form Bilgileri\\n\\n";

# sendmail programına form bilgileri gönderiliyor

foreach $anahtar (keys(%FORM)) {
print MAIL "$anahtar = $FORM{$anahtar}\\n";
}

# bilgiler gönderildikten sonra sendmail programını kapatmayı unutmayın

close(MAIL);

# teşekkür sayfası oluşturuluyor

print <<HTMLSonu;
<html><head><title>Teşekkürler</title></head><body>
<h2>Teşekkürler</h2>
Mailiniz gönderildi. Formu gönderdiğiniz için teşekkürler<p>
</body></html>
HTMLSonu
;

# hata alt programı

sub hata {
($hatamesaji) = @\_;
print "<html><head><title>Hata!</title></head><body>"
print "<h2>Hata</h2>\\n";
print "$hatamesaji<p>\\n";
print "</body></html>\\n";
exit;
}

Yukarıdaki scriptte yeni bir yapı kullandık: hata isimli bir "alt program". Alt programlar programların sadece çağırıldıkları zaman işletilen komutlarıdır diyebiliriz. Örneğimizde hata alt programı sadece sendmail programı bulunamazsa çalıştırılır. Programınızın bu durumda size bir server hatası vermesi yerine neyin yanlış gittiğine dair bilgi vermesini istersiniz. hata alt programıyla bu yapılıyor. sendmail programının bulunmadığını bildiren bir web sayfası gösteriyor ve Perl'den çıkıyor. Perl'de alt programlar &altprogramadi ya da &atlprogramadi (argümanlar) şeklinde çağrılır. Argümanlar alt programa gönderilen değerlerdir.

Şimdi aşağıdaki kodlarla bir form oluşturun ve scripti deneyin.

<form action="http://hammer.prohosting.com/~sinan/cgi-bin/ornek/mail.cgi" method="POST">
<pre>
Adınız: <input type="text" name="isim" size=30>
E-mail adresiniz: <input type="text" name="email" size=30>
Web sayfanız: <input type="text" name="web\_sayfasi" size=30>
Yaşınız: <input type="text" name="yas" size=3>
</pre>
<input type="submit" value="Gönder">
<input type="reset" value="Tümünü Sil">

</form>

Eğer herşey yolunda giderse birkaç dakika sonra form bilgileri e-mail adresine gelecektir.

Eğer form bilgilerini birkaç adrese birden göndermek istiyorsanız adresleri aşağıdaki gibi aralarına virgül koyarak yazabilirsiniz.

$gonderilen = 'silyas@esentepe.sau.edu.tr', zeytinbey@bbs.ege.edu.tr, sinanilyas@hotmail.com';

## **Bölüm 5: İleri Seviye Formlar**

Bir önceki bölümde form bilgilerinin kodlarının nasıl çözülecegini ve mail olarak gönderileceğini gördük. Fakat yazdığımız scriptte bir eksiklik vardı: Hata kontrolü. Eğer boş formlar almak istemiyorsanız ya da belli alanların mutlaka doldurulmasını istiyorsanız, hatta bir anket yapıyor ve verilen cevaba göre scriptinizin farklı işler yapmasını istiyorsanız şimdi yazacaklarımı dikkatlice okuyun.

Belli bir şartın doğru olup olmadığını kontrol etmek için if blokunu kullanırız.

if ($degiskenadi eq "birseyler") {
# koşul doğruysa işletilecek komutlar
}
elsif ($degiskenadi eq "baskaseyler") {
# bu koşul doğruysa işletilecek komutlar
}
else {
# yukarıdaki koşulların hiçbiri doğru değilse işletilecek komutlar
}

elsif ve else bloklarının konulması şart değildir. Sadece tek bir şartın doğruluğunu kontrol edecekseniz şu şekilde kullanabilirsiniz:

if ($varname > 23) {
# $sayi 23'ten büyükse işletilecek komutlar
}

Perl'de değişkenin sayı ya da yazı oluşuna göre değişik karşılaştırma operatörleri vardır.

| **Karşılaştırma İfadesi** | **Sayı İçin** | **Yazı İçin** |
| --- | --- | --- |
| $x eşittir $y | $x == $y | $x eq $y |
| $x eşit değildir $y | $x != $y | $x ne $y |
| $x büyüktür $y | $x > $y | $x gt $y |
| $x büyük eşittir $y | $x >= $y | $x ge $y |
| $x küçüktür $y | $x < $y | $x lt $y |
| $x küçük eşittir $y | $x <= $y | $x le $y |

Farkettiğiniz gibi, yazıların karşılaştırılmasında karakter operatörler (eq, ne, vs.), sayıların karşılaştırılmasında işaret operatörler (==, !=, vs.) kullanılır.

Şimdi "mail.cgi" isimli scriptimizi açıp sendmail programını açan satırın (open (MAIL, "|$mailprog -t") or &hata("$mailprog bulunamadı!\\n");) hemen öncesine şu kodları yerleştirin ve scripti "mail2.cgi" adıyla kaydedin.

if ($FORM{'isim'} eq "") {
&hata("Lütfen isminizi yazın");
}

Hata mesajının yazdırılmasında hata alt programından faydalanılıyor. Scriptimize bu kodu eklemekle formunuzdaki isim alanının doldurulmasını zorunlu kılmış olduk. Aşağıdaki gibi birden fazla alanı da kontrol edebilirdik.

if ($FORM{'isim'} eq "" or $FORM{'email'} eq "" or $FORM{'yas'} eq "") {
&hata("Lütfen isminizi, e-mail adresinizi ve yaşınızı yazın");
}

Yukarıdaki kod "isim", "email" ya da "yas" isimli alanların herhangi biri boş bırakıldığı takdirde hata mesajının yazdırılmasını sağlayacaktır. Koşullar or operatörü ile ayrılmışlardır. (or yerine || da kullanılabilir.)

## **Onay Kutuları**

Formdaki onay kutularının nasıl yazdırıldığını bir örnekle açıklayalım. İlk önce aşağıdaki kodlarla bir sayfa oluşturun ve "renk.html" adıyla kaydedin.

<html><head><title>Sevdiğiniz Renkler</title></head><body>
<form action="http://hammer.prohosting.com/~sinan/cgi-bin/ornek/renk.cgi" method="POST">

<h3>Sevdiğiniz renkleri işaretleyin</h3>
<input type="checkbox" name="kirmizi" value=1> Kırmızı<br>
<input type="checkbox" name="sari" value=1> Sarı<br>
<input type="checkbox" name="yesil" value=1> Yeşil<br>
<input type="checkbox" name="mavi" value=1> Mavi<p>

<input type="submit" value="Gönder">

</form>
</body></html>

Burada value sıfatına istediğiniz değeri verebilirsiniz. Yukarıda CGI programında daha kısa kod yazabilmek için "1" değeri verilmiştir.

Şimdi de bu formun kodunu çözecek CGI programını yazalım.

#!/usr/bin/perl

print "Content-type:text/html\\n\\n";

read(STDIN, $tampon, $ENV{'CONTENT\_LENGTH'});
@ciftler = split(/&/, $tampon);
foreach $cift (@ciftler) {
($isim, $deger) = split(/=/, $cift);
$deger =~ tr/+/ /;
$deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;
$FORM{$isim} = $deger;
}

print "<html><head><title>Sonuçlar</title></head>\\n";
print "<body>\\n";
print "<h2>Sonuçlar</h2>\\n";

@renkler = ("kirmizi","sari","yesil","mavi");
foreach $renk (@renkler) {
if ($FORM{$renk} == 1) {
print "$renk rengini işaretlediniz<br>\\n";
}
}

print "</body></html>\\n";

## **Radyo Düğmeleri**

Radyo düğmeleri onay kutularından biraz farklıdır. Form hazırlarken radyo düğmelerinin hepsinin name sıfatına aynı değer atandığı için yazdırılması daha kolaydır. Bir örnek vererek bunu açıklayalım.

Aşağıdaki kodlarla bir sayfa hazırlayın ve "renk2.html" adıyla kaydedin.

<html><head>
<title>En Sevdiğiniz Renk</title>
</head>
<body>
<form action="http://hammer.prohosting.com/~sinan/cgi-bin/ornek/renk2.cgi" method="POST">

<h3>İçlerinde en sevdiğiniz renk hangisi?</h3>
<input type="radio" name="renk" value="kirmizi"> Kırmızı<br>
<input type="radio" name="renk" value="sari"> Sarı<br>
<input type="radio" name="renk" value="yesil"> Yeşil<br>
<input type="radio" name="renk" value="mavi"> Mavi<p>

<input type="submit" value="Gönder">

</form>
</body>
</html>

Şimdi de aşağıdaki kodları yazın ve "renk2.cgi" adıyla kaydedin. ("renk.cgi"den tek farkının foreach döngüsünün yerine konan print "En sevdiğiniz renk: $FORM{'renk'}\\n"; satırı olduğuna dikkat edin.)

#!/usr/bin/perl

print "Content-type:text/html\\n\\n";

read(STDIN, $tampon, $ENV{'CONTENT\_LENGTH'});
@ciftler = split(/&/, $tampon);
foreach $cift (@ciftler) {
($isim, $deger) = split(/=/, $cift);
$deger =~ tr/+/ /;
$deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;
$FORM{$isim} = $deger;
}

print "<html><head><title>Sonuçlar</title></head>\\n";
print "<body>\\n";
print "<h2>Sonuçlar</h2>\\n";

print "En sevdiğiniz renk: $FORM{'renk'}\\n";

print "</body></html>\\n";

Scriptimizi bir adım daha geliştirerek ziyaretçiye sadece seçtiği rengi söylemekle kalmayıp aynı zamanda fon rengini seçilen renk yapacak şekilde değiştirelim.

#!/usr/bin/perl

print "Content-type:text/html\\n\\n";

read(STDIN, $tampon, $ENV{'CONTENT\_LENGTH'});
@ciftler = split(/&/, $tampon);
foreach $cift (@ciftler) {
($isim, $deger) = split(/=/, $cift);
$deger =~ tr/+/ /;
$deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;
$FORM{$isim} = $deger;
}

%renkler = ("kirmizi" => "red",
"sari" => "yellow",
"yesil" => "green",
"mavi" => "blue");
print "<html><head><title>En Sevdiğiniz Renk</title></head>\\n";
print "<body bgcolor=$renkler{$FORM{'renk'}}>\\n";
print "<h2>En sevdiğiniz renk: $FORM{'renk'}</h2><br>\\n";
print "</body></html>";

## **Seçim Kutuları**

Seçim kutularının kodunun çözülmesi hemen hemen radyo butonları gibidir. Yine konunun daha iyi anlaşılması bakımından bir örnek verelim.

Aşağıdaki kod ile formu oluşturun ve sayfayı "renk3.html" adıyla kaydedin.

<form action="http://hammer.prohosting.com/~sinan/cgi-bin/ornek/renk2a.cgi" method="POST">

<select name="renk">
<option value="kirmizi"> Kırmızı
<option value="sari"> Sarı
<option value="yesil"> Yeşil
<option value="mavi"> Mavi
</select><p>

<input type="submit" value="Gönder">
</form>

Seçim kutularının değerlendirilmesi radyo botonları ile aynı olduğundan yeni bir script yazmamıza gerek yok. Formumuzu "renk2a.cgi" scriptine gönderebiliriz.

Şu ana kadar öğrendiğimiz bilgilerle onay kutuları, radyo düğmeleri ve seçim kutuları içeren form bilgilerini web sayfasına yazan bir CGI scripti hazırlayabiliriz. Aşağıdaki kodlarla yeni bir HTML dosyası oluşturun ve "form.html" adıyla kaydedin.

<html><head><title>Form</title></head>
<body>
<form action="http://hammer.prohosting.com/~sinan/cgi-bin/ornek/form.cgi" method="POST">

İsminiz: <input type="text" name="isim" size=30><p>

E-mail adresiniz: <input type="text" name="email" size=30><p>

Bu siteye nasıl ulaştınız?
<select name="nasilulasti">
<option value=0 selected>Seçim yapın...
<option value=1>Direk adresini yazdım
<option value=2>Siteyi bookmark etmiştim
<option value=3>Arama motorundan buldum
<option value=4>Başka bir siteden
<option value=5>Adresi bir kitaptan aldım
<option value=6>Diğer
</select><p>

Siteye 5 üzerinden kaç verirsiniz?<br>
<input type="radio" name="puan" value=1> 1
<input type="radio" name="puan" value=2> 2
<input type="radio" name="puan" value=3> 3
<input type="radio" name="puan" value=4> 4
<input type="radio" name="puan" value=5> 5<p>

Aşağıdakilerden hangileriyle ilgilenirsiniz?<br>
<input type="checkbox" name="wds" value=1> Web Design<br>
<input type="checkbox" name="wsy" value=1> Web Server Yöneticiliği<br>
<input type="checkbox" name="tic" value=1> Elektronik Ticaret<br>
<input type="checkbox" name="als" value=1> İnternetten Alışveriş<br>
<input type="checkbox" name="egt" value=1> İnternet Aracılığıyla Eğitim<br>
<p>

Sayfa hakkında yorumlarınız:<br>
<textarea name="yorum" rows=5 cols=70 wrap="virtual">
</textarea>
<p>

<input type="submit" value="Gönder">
<input type="reset" value="Tümünü Sil">
</form>
</body></html>

Şimdi de "form.cgi" programını yazalım.

#!/usr/bin/perl

print "Content-type:text/html\\n\\n";

read(STDIN, $tampon, $ENV{'CONTENT\_LENGTH'});
@ciftler = split(/&/, $tampon);
foreach $cift (@ciftler) {
($isim, $deger) = split(/=/, $cift);
$deger =~ tr/+/ /;
$deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;
$FORM{$isim} = $deger;
}

# "Bu siteye nasıl ulaştınız?" sorusunun cevabı
# numara olarak gönderildiği için bunu çevirebilmek
# için bir hash değişkene ihtiyacımız var

%nasilulasti = ( 0 => "",
1 => "Direk adresini yazdım",
2 => "Siteyi bookmark etmiştim",
3 => "Arama motorundan buldum",
4 => "Başka bir siteden",
5 => "Adresi bir kitaptan aldım",
6 => "Diğer" );

print <<HTMLBas;
<html><head><title>Sonuçlar</title></head>
<body>
<h2>Sonuçlar</h2>

Formla gönderdiğiniz bilgiler aşağıdaki şekildedir:<p>

İsminiz: $FORM{'isim'}<p>

E-mail adresiniz: $FORM{'email'}<p>

Siteye nasıl ulaştığınız: $nasilulasti{$FORM{'nasilulasti'}}<p>

Siteye verdiğiniz puan: $FORM{'puan'}<p>

HTMLBas
;

%secim = ("wds" => "Web Design",
"wsy" => "Web Server Yöneticiliği",
"tic" => "Elektronik Ticaret",
"als" => "İnternetten Alışveriş",
"egt" => "İnternet Aracılığıyla Eğitim" );

print "Aşağıdaki konularla ilgileniyorsunuz:<br>\\n";
foreach $anahtar (keys %secim) {
if ($FORM{$anahtar} == 1) {
print "$secim{$anahtar}<br>\\n";
}
}

print <<HTMLSon;
<p>
Sayfa hakkında yorumlarınız:<br>
$FORM{'yorum'}
<p>
</body></html>
HTMLSon
;

Eğer form bilgilerinin mail adresinize gönderilmesini istiyorsanız geçen bölümde öğrendiğiniz bilgilerle bunu yapabilirsiniz.

## **Bölüm 6: Dosya İşlemleri**

Daha ileri seviye CGI uygulamaları hazırlamaya başladığınızda bilgileri daha sonra kullanmak üzere dosyalara yazarak saklamak isteyeceksiniz. Mesela bir misafir defteri (guestbook) programınız olabilir ve isim, e-mail gibi bilgileri bir log dosyasına kaydetmek isteyebilirsiniz. Ya da bir sayac programının bir dosyadaki sayıyı arttırmasını isteyebilirsiniz. Hatta bir veritabanı dosyasından bilgi tarayarak bulup web sayfasına yazdıran bir program yapmak isteyebilirsiniz. Bütün bunları yapabilmek için dosya işlemlerini yani dosyadan bilgi okuma ve dosyaya bilgi yazmayı öğrenmelisiniz.

Çoğu server minimum erişim yetkileriyle çalışır. Bu server'ın güvenliği açısından önemlidir fakat dosyalara yazmayı güçleştirir. CGI programının yeni dosyalar oluşturmaya yetkisi yoktur. CGI programının dosyaya bilgi yazabilmesi için dosyanın erişim yetkilerinin aşağıdaki komutla "herkes tarafından yazılabilir" yapılması gerekir.

chmod 666 <dosya adı>

Bu komut dosyanın herkes tarafından okunabilir ve yazılabilir olmasını sağlar. Yalnız işin bir de kötü tarafı var. Server'ınızdaki diğer kullanıcılar rahatlıkla dosyanızı silebilirler. Ve malesef bu konuda diğer kullanıcılara güvenmekten başka yapabileceğiniz birşey yok :)

Eğer dosyayı sadece içinden bilgi okumak için kullanacaksanız aşağıdaki komutula sadece okuma yetkisi verebilirsiniz.

chmod 644 <dosya adı>

## **Dosyaları Açma**

Dosyaları açmak için open komutunu kullanırız.

open(dosyadegiskeni,dosyaadi);

Şimdi bunu açıklamak için birkaç örnek verelim.

open(DOSYA,"bilgi.txt"); # bilgi.txt dosyasını okumak için açar
open(DOSYA,">bilgi.txt"); # bilgi.txt dosyasını üstüne yazmak için açar
open(DOSYA,">>bilgi.txt"); # bilgi.txt dosyasını eklemek için açar

Dosya değişkeni, dosyanın programda kullanılacak olan adıdır diyebiliriz. Yani dosyayı açtıktan sonra programın bir yerinde dosyaya erişmek için dosyanın sistemdeki adını değil dosya değişkenini kullanırız. Bu örneklerde dosya değişkeni "DOSYA" olarak seçilmiştir. Fakat dosya değişkeni olarak istediğiniz şeyi yazabilirsiniz.

Dosyanın adının başında eğer > işareti varsa dosya üstüne yazılmak için açılmıştır yani dosyada bulunan bütün bilgiler silinir ve yerine yenileri yazılır. Dosyanın adının başında eğer >> işareti varsa dosya sonuna bilgi eklemek için açılmıştır yani dosyada bulunan bilgiler silinmeden yeni yazacaklarımız dosyadaki bilgilerin sonuna eklenir.

Bu arada bir konuda sizi uyarmak istiyorum: CGI programınız eğer tam yolunu yazmamışsanız dosyanızı bulamayabilir. Bu yüzden sadece "bilgi.txt" yazmak yerine "/home/httpd/cgi-bin/bilgi.txt" şeklinde dosyanın tam yolunu yazmanız gerekebilir.

Dosya açmak için yukarıda kullandığımız kodun eksik bir yönü var: Hata kontrolü. Dosyanın açıldığından emin olmak için dosyayı aşağıda gösterildiği şekilde açmalısınız.

open(DOSYA,">bilgi.txt") or &hata("bilgi.txt dosyası bulunamadı...");

Burada 4. bölümdeki hata alt programı kullanılarak dosya açılmadığı takdirde programın gerekli açıklamayı yazdırarak Perl'den çıkması sağlanır.

Şimdi geçen bölümde yazdığımız "form.cgi" programında bazı değişiklikler yaparak form bilgilerini bir dosyaya yazdıralım. Aşağıdaki kodları "form2.cgi" adıyla kaydedin.

#!/usr/bin/perl
print "Content-type:text/html\\n\\n";

read(STDIN, $tampon, $ENV{'CONTENT\_LENGTH'});
@ciftler = split(/&/, $tampon);
foreach $cift (@ciftler) {
($isim, $deger) = split(/=/, $cift);
$deger =~ tr/+/ /;
$deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;

$deger =~ s/\\n/ /g; # satır sonu işaretlerini yok etmek için eklendi

$FORM{$isim} = $deger;
}

open(DOSYA,">>formbilgileri.txt") or &hata("formbilgileri.txt dosyası açılamadı. Lütfen silyas\\@esentepe.sau.edu.tr adresine mail atarak webmaster'ı uyarınız.");

print DOSYA "$FORM{'isim'}|$FORM{'email'}|$FORM{'nasilulasti'}|$FORM{'puan'}|";

%secim = ("wds" => "Web Design",
"wsy" => "Web Server Yöneticiliği",
"tic" => "Electronic Commerce",
"als" => "Elektronik Ticaret",
"egt" => "İnternet Aracılığıyla Eğitim" );

foreach $anahtar (keys %secim) {
if ($FORM{$anahtar} == 1) {
print DOSYA "$anahtar,";
}
}

print DOSYA "|$FORM{'yorum'}\\n";
close(DOSYA);

print <<HTMLSonu;
<html><head><title>Teşekkürler</title></head>
<body>
<h2>Teşekkürler</h2>
Gönderdiğiniz bilgiler kaydedildi.
</body></html>
HTMLSonu
;

sub hata {
($hatamesaji) = @\_;
print "<h2>Hata!</h2>\\n";
print $hatamesaji;
exit;
}

Şimdi bilgilerin yazılacağı dosyayı oluşturup "yazılabilir" yapmalısınız. Bunun için programı kaydettiğiniz dizinde şu komutları yazın:

touch formbilgileri.txt
chmod 666 formbilgileri.txt

touch komutu ile yeni ve boş bir dosya oluşturulur ve chmod komutu ile herkesin dosyaya yazabilmesi sağlanır.

Şimdi "form.html" dosyasını açın ve formu "form2.cgi" ile göndermesi için gerekli değişikliği yapın. Sonra da "form2.html" adıyla kaydedin. Formu doldurup gönderdiğinizde herşey yolunda gitmişse "formbilgileri.txt" dosyasının içeriği aşağıdaki gibi olacaktır.

sinan ilyas|silyas@esentepe.sau.edu.tr|1|5|wds,egt,|siteniz harika

Bu şekilde text dosyasından oluşan ve her satırı yeni bir kayıt olan veritabanı dosyalarına "flat-file database" denir. Bu örnekte alanlar pipe (|) işareti ile ayrılmıştır. İsterseniz gönderilen bilgide bulunmacak başka bir karakter kullanabilirsiniz.

Yukarıdaki kodla ilgili bir şeyi daha açıklayalım.

$deger =~ s/\\n/ /g;

Bu satırla ifadelerin sonlarındaki satır sonu işarertlerini yok ediyoruz çünkü veritabanı dosyamızda her kaydın tek satırda olması gerekiyor. Ayrıca, dikkat etmişseniz peşpeşe birkaç print komutu kullanmamıza rağmen herşey tek bir satıra yazdırıldı. Bunun nedeni son print komutuna kadar \\n ifadesini kullanmamış olmamız.

Buna bir örnek verirsek sanırım daha iyi anlaşılır.

print "Merhaba, ";
print "ben ";
print "Sinan.\\n";

Kodları aşağıdaki gibi bir çıktı verir.

Merhaba, ben Sinan.

## **Dosyaları Kapatma**

Dosya ile işiniz bittiği zaman dosyayı kapatmalısınız. Bunu aşağıdaki komutla yapabilirsiniz.

close(dosyadegiskeni);

## **Dosyalardan Bilgi Okuma**

Bir gün merak edip formla gönderilen bilgilerin bir özetini görmek isteyebilirsiniz. Bunun için programda bilgilerin kaydedildiği dosyayı açtırıp bütün kayıtları okutup gereken hesapları yaptırmalısınız.

Bir dosyadan bilgiyi okuturken ister tek bir satırı, isterseniz bütün dosyayı okuyabilirsiniz. İşte bir örnek:

open(DOSYA,"formbilgileri.txt") or &hata("Dosya açılamadı.");

$a = <DOSYA>; # $a değişkenine dosyadan bir tek satır okur
@b = <DOSYA>; # @b değişkenine dosyanın tamamını okur

close(DOSYA);

Bu kodlar "formbilgileri.txt" dosyasının ilk satırını $a scalar değişkenine, geri kalan satırları @b dizisine okur. Bu durumda @b disizinin her bir elemanı bir satır olur. Her iki kod satırında da okutma işi <DOSYA> koduyla yapılıyor. Dosyadan ne kadar bilgi okunacağını atanacağı değişkenin tipi belirliyor.

Aşağıdaki dosyanın tamamını bir diziye okuduktan sonra dosyanın içeriğini satır satır ekrana yazdırır.

open(DOSYA,"formbilgileri.txt") or &hata("Dosya açılamadı.");
@bilgiler = <DOSYA>;
close(DOSYA);

foreach $satir (@bilgiler) {
chomp($satir);
print "$satir\\n";
}

Bu kodlar dosyanın açık kalma süresini en aza indirir. Bu yüzden dosyadan bilgi okurken bu metodu kullanmanızı tavsiye ederim.

Şimdi "formbilgileri.txt" dosyasından bilgileri okuyup kaç kişinin formu gönderdiğini, siteye en çok hangi yolla ulaşıldığını, siteye verilen puanların ortalamasını, hangi bilgisayar alanıyla kaç kişinin ilgilendiğini ve yapılan yorumların listesi yazdıran bir CGI programı yazalım.

Şimdi "özet.cgi" adında yeni bir dosya oluşturun ve içine şu kodları yazın:

#!/usr/bin/perl
print "Content-type:text/html\\n\\n";

open(DOSYA,"formbilgileri.txt") or &hata("formbilgileri.txt dosyası açılamadı. Lütfen silyas\\@esentepe.sau.edu.tr adresine mail atarak webmaster'a haber verin.");

@bilgiler = <DOSYA>;
close(DOSYA);

# Bilgileri özetlemek için önce bazı değişkenler hazırlanıyor.
$sayi = 0; # Formu gönderenlerin sayısı
$toplampuan = 0; # Verilen puanların toplamı
$yorumlar = ""; # Gönderilen bütün yorumlar
%nasilulasti\_sayisi = (); # Hangi şekilde kaç kişinin ulaştığı
%ilgi = (); # Hangi bilgisayar alanıyla kaç kişinin ilgilendiğinin sayısı

%nasilulasti = ( 0 => "",
1 => "Direk adresini yazdım",
2 => "Siteyi bookmark etmiştim",
3 => "Arama motorundan buldum",
4 => "Başka bir siteden",
5 => "Adresi bir kitaptan aldım",
6 => "Diğer" );

foreach $i (@bilgiler) {
chomp($i);
($isim,$email,$nasil,$puan,$secim,$yorum) = split(/\\|/,$i);

# Bu satır "$sayi = $sayi + 1" ile aynı işi görür.
$sayi++;

$toplampuan = $toplampuan + $puan;

# Bu satır $yorumlar değişkeninin sonuna $yorum değişkeninin
# içeriğini ekler.

$yorumlar .= "$yorum\\n";

$nasilulasti\_sayisi{$nasil}++;

@ilgilistesi = split(/,/,$secim);
foreach $j (@ilgilistesi) {
$ilgi{$j}++;
}
}

# Verilen puanlarınn ortalaması bulunuyor.

if ($sayi > 0) { # Sıfıra bölmemek için
$ort\_puan = int($toplampuan / $sayi);
} else {
$ort\_puan = 0;
}

# Sonuçları bildiren web sayfası hazırlanıyor.

print <<HTMLSonu;
<html><head><title>Özet</title></head>
<body>
<h2>Özet</h2>

Gönderilen form sayısı: $sayi<p>

Verilen puanların ortalaması: $ort\_puan<p>

Siteye kaç kişinin ne şekilde ulaştığı:<br>
<ul>
<li>(yanıtlamayan) - $nasilulasti\_sayisi{0}
<li>$nasilulasti{1} - $nasilulasti\_sayisi{1}
<li>$nasilulasti{2} - $nasilulasti\_sayisi{2}
<li>$nasilulasti{3} - $nasilulasti\_sayisi{3}
<li>$nasilulasti{4} - $nasilulasti\_sayisi{4}
<li>$nasilulasti{5} - $nasilulasti\_sayisi{5}
<li>$nasilulasti{6} - $nasilulasti\_sayisi{6}
</ul>

Kaç kişinin hangi bilgisayar alanıyla ilgili olduğu:<br>
<ul>
<li>Web Design: $ilgi{'wds'}
<li>Web Server Yöneticiliği: $ilgi{'wsy'}
<li>Electronic Commerce: $ilgi{'tic'}
<li>Elektronik Ticaret: $ilgi{'tic'}
<li>İnternet Aracılığıyla Eğitim: $ilgi{'egt'}
</ul><p>

Sayfa Hakkında Yorumlar:<p>
$yorumlar

HTMLSonu
;

sub hata {
($hatamesaji) = @\_;
print "<h2>Hata!</h2>\\n";
print $hatamesaji;
exit;
}

## **Bölüm 7: Dosyada Metin Arama**

Bu bölümde bir dosyanın içerisinde belli bir metni nasıl aratabileceğimizi anlatacağım. Eğer bütün sitede arama yaptırmak istiyorsanız bunu kendiniz yapmanızı tavsiye etmem. Bunun için Glimpse ve SWISH gibi hazır site indexleme araçlarını kullanabilirsiniz. (SWISH'i tavsiye ederim)

Dosyada arama yaptırmanın değişik yolları vardır. Eğer bir tek dosyada arama yaptıracaksanız, bir döngü ile dosyadaki bütün kayıtları teker teker okutup aradığınız verinin o kayıtta geçip geçmediğini kontrol edebilir, ya da Perl'ün grep() fonksiyonunu kullanarak dosyanın tamamını bir seferde tarayabilirsiniz. Birinci yolu geçen bölümde öğrendiğimiz bilgilerle yapabilirsiniz. Bu bölümde ikinci yol olan grep() fonksiyonunu kullanarak bunu nasıl yapabileceğinizi anlatacağım.

grep() fonksiyonunun kullanımı aşağıdaki gibidir.

@sonuclar = grep(/$arananmetin/,@liste);

Sanırım bir örnek verirsek daha iyi anlaşılır.

#!/usr/bin/perl
@liste = ("sinan","koray","baris","orhan");
$arananmetin = "an";
@sonuclar = grep(/$arananmetin/,@liste);
foreach $i (@sonuclar) { print "$i\\n"; }

Bu programın çıktısı aşağıdaki gibi olur.

sinan
orhan

Şimdi biraz daha gelişmiş bir örnek verelim. Aşağıdaki gibi, öğrencilerin okul numarası, isim ve yaş bilgilerinin kaydedildiği "ogrenci.txt" isimli bir veritabanı dosyamız olsun.

1|768|Hasan Şahin|15
2|515|Mustafa Öztürk|16
3|663|İlhan Yıldırım|16
4|697|Fikret Yılmaz|15
5|716|Haluk Çiçek|15

Şimdi de bu veritabanında arama yaptırmak için bir script yazalım.

#!/usr/bin/perl
$veridosyasi = "ogrenci.txt";
read(STDIN, $tampon, $ENV{'CONTENT\_LENGTH'});
@ciftler = split(/&/, $tampon);

foreach $cift (@ciftler) {
($alanadi, $deger) = split(/=/, $cift);
$deger =~ tr/+/ /;
$deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;
$deger =~ s/~!/ ~!/g;
$FORM{$alanadi} = $deger;
}

$arananmetin = $FORM{'isim'};

open(DOSYA,$veridosyasi);
@bilgiler = <DOSYA>;
close(DOSYA);
print "Content-type:text/html\\n\\n";
print "<html><head><title>Arama Sonuçları</title></head>\\n";
print "<body><h3>Arama Sonuçları</h3>\\n";

$bulunansayisi = 0;

@sonuclar = grep(/$arananmetin/,@bilgiler);

if ($#sonuclar >= 0) {
foreach $i (@sonuclar) {
chomp($i);
($kayitno,$okulno,$adsoyad,$yas) = split(/\\|/,$i);
print "<b>$adsoyad</b> Okul No: $okulno Yaş: $yas<br>\\n";
$bulunansayisi++;
}
print "<br><b>$bulunansayisi</b> kayıt bulundu.<p>\\n";
}
else {
print "Kayıt Bulunamadı.<p>\\n";
}

print "</body></html>\\n";

Bu programı "ogrenci1.cgi" adıyla kaydedin. Şimdi sıra bu scripti çağıracak formu hazırlamaya geldi.

<form action="http://hammer.prohosting.com/~sinan/cgi-bin/ornek/ogrenci1.cgi">
Aradığınız kişinin ismini girin <input type="Text" name="isim"> </form>

**Not:** $#sonuclar @sonuclar dizisinin eleman sayısının bir eksiğini verir.

Formumuzdaki kutucuğa "Hasan" (tırnak koymadan) yazarsanız script size "Hasan Şahin" isimli öğrenciye ait bilgileri verir. Fakat, script kayıtları alan ayırımı yapmadan taradığı için isim yerine örneğin "15" (tırnaksız) yazarsak bize 15 yaşındaki ve okul numarasında 15 geçen öğrencilere ait bilgileri verir. Bunu hatayı gidermek için scriptimizi aşağıdaki şekilde değiştirmemiz gerekir.

#!/usr/bin/perl
$veridosyasi = "ogrenci.txt";
read(STDIN, $tampon, $ENV{'CONTENT\_LENGTH'});
@ciftler = split(/&/, $tampon);

foreach $cift (@ciftler) {
($alanadi, $deger) = split(/=/, $cift);
$deger =~ tr/+/ /;
$deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;
$deger =~ s/~!/ ~!/g;
$FORM{$alanadi} = $deger;
}

$arananmetin = $FORM{'isim'};

open(DOSYA,$veridosyasi);
@bilgiler = <DOSYA>;
close(DOSYA);
print "Content-type:text/html\\n\\n";
print "<html><head><title>Arama Sonuçları</title></head>\\n";
print "<body><h3>Arama Sonuçları</h3>\\n";

$bulunansayisi = 0;

@sonuclar = grep(/$arananmetin/,@bilgiler);

if ($#sonuclar >= 0) {
foreach $i (@sonuclar) {
chomp($i);
($kayitno,$okulno,$adsoyad,$yas) = split(/\\|/,$i);
if ($adsoyad =~ $arananmetin) {
print "<b>$adsoyad</b> Okul No: $okulno Yaş: $yas<br>\\n";
$bulunansayisi++;
}
}
}

if ($bulunansayisi == 0) {
print "Kayıt Bulunamadı.<p>\\n";
}
else {
print "<br><b>$bulunansayisi</b> kayıt bulundu.<p>\\n";
}

print "</body></html>\\n";

**Not:** if ($adsoyad =~ $arananmetin) satırı $arananmetin değişkenine atanan metnin, $adsoyad değişkenine atanan metnin içerisinde geçip geçmediğini bulmak için kullanılmıştır.

Bu örnekte $bulunansayisi isimli değişkenin değeri sadece aranan metin "isim" alanında bulunduğu zaman arttırılır. Eğer aranan metin "isim" alanında değil de örneğin "yaş" alanında bulunursa kayıt ekrana yazdırılmaz ve $bulunansayisi değişkeninin değeri arttırılmaz. Scriptin sonunda $bulunansayisi değişkeninin değeri kontrol edilir ve eğer 0'sa "Kayıt bulunamadı" mesajı yazdırılır.

## **Bölüm 8: Son Birkaç Söz**

Eveeeet. Şimdi neler öğrendik bir gözden geçirelim. CGI nedir, nasıl çalıştırılır, Perl değişkenleri nelerdir ve nasıl kullanılır, form gönderme metodları nelerdir, aralarında ne gibi farklar vardır, web üzerinden gönderilen formlar nasıl okunabilir hale getirilerek e-mail adresine gönderilir, onay kutuları, radyo butonları ve seçim alanları bulunan formlar nasıl değerlendirilir, dosyalara bilgi nasıl yazılır, dosyalardan bilgi nasıl okunur, dosyalarda nasıl arama yapılır...

Ne çok şey öğrenmişiz değil mi? Gerçekten de birçok şey öğrendik, ama hala öğrenmemiz gereken şeyler öğrendiklerimizden çok daha fazla. Bu arada benim bu anlattıklarımdan fazla şey bildiğimi sanmayın. :) Hatta tercüme etmeye başladığımda daha az şey biliyordum diyebilirim çünkü tercüme ederken aynı zamanda öğrenmeye devam ediyordum.

Eğer başka kaynaklar arıyorsanız ilk bakacağınız yer olmalı. Burada zip formatında sıkıştırılmış birçok kitap var. Sanırım bu kitaplar size yeterli olur. Ama hazır scriptler ve daha başka kaynaklar arayanlar için ben yine de bildiğim diğer adresleri buraya yazıyorum.

http://www.worldwidemart.com/scripts/
http://www.lies.com/begperl/
http://agora.leeds.ac.uk/Perl/Cgi/start.html
http://www.xnet.com/~efflandt/pub/
http://cgi.resourceindex.com/rate/rated.html
http://www.speakeasy.org/~cgires/
http://www.eprotect.com/stas/TULARC/webmaster/cgi-scripts1.html

Bu son yazdığım adres tek kelimeyle harika bir yer. Tam 3 sayfa dolusu link var çünkü!

---
*Kaynak: `CGI NEDİR/CGI NEDIR.doc` — SONTAY — 2004*
