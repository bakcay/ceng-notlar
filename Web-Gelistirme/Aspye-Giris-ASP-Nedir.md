# Asp'ye giris.Asp Nedir

**Asp'ye giris.Asp nedir? ******

Asp Microsoft tarafindan gelistirilmis bir script dilidir. Asil adi Active Server Pages (Etkin Sunucu Sayfalari)'dir. Asp çagimizda gittikçe yayginlasan bir dildir, bunun en büyük nedeni kolay yönetilebilir olmasi, veritabani baglantilari ile birçok form isini kolaylastirma gibi özelliklere sahip tabii bunlara birçogunu ekleyebiliriz. Asp dosyalarini çalistirmak için bir browserdan baska asp teknolojisini taniyan bir server (sunucu) lazim. HTML dosyalarinda dosyanin üzerine iki defa tikladigimizda tarayimiz açiliyordu kodlari yorumlayip sayfayi gösteriyordu, ama asp dosyalarinda yani uzantisi .asp olan dosyalarin eger üzerine iki defa tiklarsaniz ya sadece kodlar görünecek ya da tarayiniz bu dosyayi download etmeye çalisacaktir. Çünkü sadece browser asp kodlarini yorumlayamaz ve az önce söyledigim seylerden biri olur. Iste bunlarla karsilasmamak için bir web sunucu kurmaniz gerekir tabii bu dili Microsoft gelistirdigi için Microsoft'un bir web sunucusunu kurmaniz lazim.Eskiden asp sadece Microsoft tabanli sunucularda çalistirilabiliyordu ama su an Unix tabanli isletim sistemlerinde de çalistirilabiliyor. Eger Windows 95/98 kullaniyorsaniz PWS ( Personal Web Server - Kisisel Web Sunucu ) veya Windows 2000/Nt kullaniyorsaniz IIS( Internet Information Services - Internet Hizmetleri Yöneticisi ) kullanmaniz gerekir. PWS Windows 98 Cd'si ile birlikte geliyor ve CD'nin Add-on klasöründe bulunuyor. IIS ise Windows'a sonradan ekleniyor. Windows 2000 Professional da kurulmamis, Server da ise kurulmus olarak geliyor. Gerçi Windows 2000 de de Denetim Masasi\*Program Ekle/Kaldir\*Windows Bilesenleri Ekle/Kaldir'dan ekliyorsunuz. Asp CGI/Perl'e karsi gelistirildigi düsünülmektedir çünkü Asp'den önce veri isleri, form doldurma, email yollama gibi isler için CGI kullaniliyordu ama CGI bazi yerlerde yetersiz kaliyordu özellikle veritabani islemlerinde ASP ise bu isi kolaylastirarak bize sunuyor. Asp'nin su an 3.0 versiyonu mevcut ve eminim ki Microsoft 3.5 gibi sürüm üzerinde çalisiyorlardir. Asp sunucu tarafli bir dildir.Peki bu nedemek? Sunucu tarafli demek kodlarin sunucuda yorumlarinip sonuçlarin istemciye gönderilmesi demek.Yani söyle açiklayim siz bir istemci olarak asp sayfalari kullanan bir siteye gittiginizde tarayiciniz sunucudan adresini yazdigini dosyayi ister.Sunucu bakar eger Asp dosyasi ise önce kodlari yorumlar bunu Asp.dll dosyasini kullanarak yapar ve eger hata yoksa bildigimiz HTML halinde sonuçlar çikar bunlarida tarayiciniza yollar tarayicinizda o kodlari yorumlayip sonuçlari size gösterir.Bir sitede eger bir asp dosyasini görüntülüyor olsaniz bile kaynaklarinda tek kelime bile asp kodu yoktur bunun nedeni az önce an yazdigimiz server tarafli olmasidir

**Asp'nin A'si**

Iste sonunda ASP'nin o güzel dünyasina adim atiyoruz...Simdi bazi temel kurallari verelim. Asp kodlarini küçük "<" ve büyük ">" isaretleri arasina yaziyoruz gene ama bir farkla bu sefer söyle yapiyoruz "<%" ve "%>" , yani bu isaretler arasi ASP kodu demek buda bunlarin arasinda yer alan kodlar hiç bir zaman tarayiciya gitmeyecek demektir. Bunun nedenini ise daha önceki yazilarimizda açiklamistik ama söyle kisaca tekrar deginelim.Web sunucusu siz browseriniz araciligi ile bir sayfa talep ettiginizde bunu bulur ve tarayiciniza yollar ama sunucunuz eger siz bir **.asp** uzantili sayfa talep ediyorsaniz durur ve bu sayfayi Asp.dll dosyasina yorumlamasi için yollar.Bu dosya bu asp sayfasini yorumlar kodlari yürütür ve sonucu saf bir HTML dökümani olarak yollar ama sunu unutmayin ASP.DLL sadece Asp kodlarini yürütür yani bütün sayfayi yürütmez..

Evet, kisa bir bilgiden sonra isimize dönelim ve ilk asp sayfamizi yazalim.Simdi bir metin editçrü açin ve asagidakiler yazip Web sunucunuzun kök dizinine **ilksayfa.asp** adi ile kaydedin.

| <% @Language=VBScript %> <% Dim merhabayazisi merhabayazisi="Merhaba Dünya :)" %> <html> <head> <title>Asp ile merhaba</title> </head> <body><center> Browser bize:<b> <%=Response.Write(merhabayazisi)%></b> diyor!</center> </body> <html> |
| --- |

Ilk satirda bulunan kod Web Sunucusuna bu **.asp** sayfasinin VBScript kullanilarak yazildigini bildiriyor.Ikinci satirda bulunan Dim ise degisken tanimlamak için kullaniliyor Onun altinda ise az önce belirttigimiz degikene deger atiyoruz burada degiskene "Merhaba Dünya :)" degerini atiyoruz ve asp kodlarimiz bitiyor...Simdi standart HTML etiketleri basliyor ve 10.satira kadar böyle gidiyor. 10. satirda ise tekrar ASP kodlari görüyoruz iste burda ASP ile HTML 'nin ne kadar rahat iç içe girdigini görüyoruz. Bu satirda ise az önce tanimladigimiz degiskenin degerini ekrana yazdiriyoruz ve etiketlerimizi kapatip bitiriyoruz sayfayi.

Asp kodlari iki dil ile yazilabilir. Microsoft bu dili hazirlarken bunu iyi düsünmüs, çünkü asp'yi ya JavaScript yada VBScript ( Visual Basic Scripting Edition ) dili ile yazabilirsiniz. Dedim ya Microsoft iyi yapmis çünkü eger JavaScript biliyorsaniz onu kullanabilirsiniz ayri bir dil ögrenmeye gerek yok zaten bu kadar çok dil karmasikligi varken. Ama JavaScript asp'de hiçbir zaman VBScript kadar yogun kullanilmadi. Bizde bu sitede su anlik en yogun dil olan VBScripti görecegiz belki ileride JavaScript'ide ekleriz. Asp kodlari yazmaniz için sadece basit bir metin editörüne ihtiyaciniz var tabii çalistirmak için az önce anlattigimiz gibi bir web sunucuya ihtiyaciniz var. Asp kodlarini ne yazikki kafaniza göre hd'nizin her tarafina kaydedemiyorsunuz sadece web sunucunuz kök dizinine kaydedebiliyorsunuz, bu dizinde eger degistirmediyseniz standart olarak C:\\inetpub\\wwwroot klasörüdür. Bu klasörün içine kaydederek çalistirabilirsiniz tabii içinde klasörler yaratip onlarin içinden de çalistirabilirsiniz. Peki madem çift tiklayamiyoruz nasil çalistiracagiz. Bunun yolu ise bilgisayarinizin adini kullanmaktir. Mesela benim bilgisayarimin adi maxipower ise ben tarayicimin adres satirina http://maxipower yazinca az önce verdigim klasöre gider ve içindeki default.asp dosyasini çalistirir. Eger siz bilgisayarinizin adi bilmiyorsaniz karsinizda üç seçenek var ya adreste bilgisayar adi yerine localhost yazacaksiniz ya 127.0.0.1 (bu yerel ip numarasidir) yazacaksiniz ya da bilgisayar adinizi belirleyeceksiniz.Kendi bilgisayar adini belirlemeyide konularimiz arasinda bulabilirsiniz. Eger ben adi default.asp den farkli bir dosya çalistiracagim diyorsaniz mesela adi yaz.asp olan dosyayi çalistiracaksiniz adres satirina ör http://maxipower/yaz.asp yazacaksiniz veya diyelim ki yaz.asp kodlar klasörünün içinde bizde o zaman http://maxipower/kodlar/yaz.asp yazacagiz.

Asp kodlarini yazmak ise çok basittir.Asp kodlari normal html etiketleri ile birlikte yazilabildigi gibi hiç html kodu olmadan da yazilabilir. Suna dikkat edilmelidir, bir .asp uzantili dosyada HTML etiketi bulunabilir ama bir .htm uzantili dosyada ASP etiketi bulunamaz!

**ASP Nesneleri******

Asp ile programlama yaparken ASP'nin nesnelerini kullanır ve bunlara dayalı programlama yaparız.Bunları verileri, almada, kullanmada ve ziyaretçiye yollamada kullanırız.Bu nesneler 6 gruptan oluşur.

| **1-****** | Application/Uygulama |
| --- | --- |
| **2-****** | Session/Oturum |
| **3-****** | Request/Talep |
| **4-****** | Response/Karşılık |
| **5-****** | Server/Sunucu |
| **6-****** | ObjectContext/Nesne Bağlamı |

**Application/Uygulama:** Asp'yi yaratanlar ASP teknolojisinin kullanıldığı bir siteyi uygulama programı olarak düşünmüşler ve bu siteye girecek herhangi biri ziyaretçiyide bu programı kullanan bir kullanıcı olarak düşünmüşler.Yani sitenize her bir kullanıcı girdiğinde bir onun için bir program açılıyor gibi düşünülebilir.Application nesnesi bize birçok yarar sağlarki bunları daha sonra ele alacağız.

**Session/Oturum: **Bu nesne Application nesnesi ile en çok karıştırılan nesnedir.Çünkü ikiside tanımlamalarda aynı özellikleri taşır.Session nesnesi ileride değişkenleri tutmak için çok sık kullanıcağız.

**Request/Talep:** Adından anlışabileceği gibi veri talep etmek için kullanılır.Gerek formlarda, gerek sorgulardan gerekse cookilerden verileri almak için kullanırız.

**Response/Karşılık:** Ziyaretçinin browserına gönderilen verilerin hepsini kapsar.Ayrıca cookilerde Response öğesinenin özellikleri arasında yer alır.Bu nesne ile ziyaretçiye veri yollarız.

**Server/Sunucu:**Web sunucusu üzerinde bulunan bileşenleri kullanmamızı sağlar.Mesela E-mail yollamak için, o sunucuda email componentının bulunması gerekmektedir.

**ObjectContext/Nesne Bağlamı**: MTS (Microsoft Transaction Server) programının nimetlerinden yararlanmamızı sağlar.İleri düzey asp programcılarına hitap eder.

**Response Nesnesi******

**Response** nesnesi kısaca kullanıcıya karşılık vermekte kullanılan nesnedir.Zaten dilimizde ki karşılığıda bu. Peki bunu hangi durumlarda ve neden kullanılırız?
**Response** nesnesini en çok ziyaretçinin tarayıcısına birşey yazdırmak için kullanırız.Tabii sadece bu değil bu nesne ile web sayfamızın bir çok özelliğini belirleriz.

**Response** nesnesini sadece bu haliyle kullanmayız bu nesneyide birçok ASP kodunda olduğu gibi "." yazıp sonra özelliğini yazarız.Şimdi bunların neler olduğunu ve ne işe yaradığını görelim.

**Write(Yazdır)** : **Response** nesnesinin en çok kullandığımız özelliğidir.Bu kodu ziyaretçinin ekranına birşeyler yazdırmakta kullanırız.

Kullanımı: <% **Response**.Write "Yazı yaz(dır)ıyoruz" %> veya <%="Yazi yaz(dır)ıyoruz"%> şeklinde.

**Buffer(Tampon)** : Bu özellik "TRUE" olarak ayarlandığında asp sayfasının tüm kodlarının yorumlanması bitmeden tarayıcıya çıktı yollanmasını engeller.Bu sayede çok işlem gerektiren sayfalar bu yöntem ile tamamen yorumlanınca çıktısı tarayıcıya yollanır.Veya sizin asp sayfanız yorumlanması bitince ziyaretçiyi başka bir siteye yolluyor bunun için tüm kodların önce yorumlanması gerekir ozamanda bu özellik işinize yarayacak.

Kullanımı: <% **Response**.Buffer=TRUE %>

**Flush(Hemen Gönder)** : Kısaca Buffer özelliğinin tam tersi bir işlem yapar.Sayfa yorumlandıkça çıktı tarayıcıya yollanır.

Kullanımı: <% **Response**.Flush %>

**Clear(Temizle)** : Buffer özelliğini kullandığınız zaman sayfa yorumlanır, yorumlanan kısım geçici bir alanda tutulur.Clear özelliği ile de bu alandaki tüm veri silinir.Ama bu özellik neden işimize yarayabilir? Sitemizde alışveriş yapan bir kullanıcı , vazgeçtiği zaman verdiği bütün bilgileri silmek en iyisidir.O zamanda bu özellik yardımımıza koşacaktır

Kullanımı: <% **Response**.Clear %>

**Expires(Süresi Geçme)** : Bir internet sitesine girdiğiniz zaman tarayıcımız bu sitedeki resimleri ve kodları cache denen ( bilgisayarımızıdaki Temporary Internet Files klasörü ) bir alanda tutar.Böylece daha sonra siz bu siteye tekrar girmek istediğinizde tarayıcı sayfayı buradan yükler.Ama kullanıcılar gidip buradan sayfanızın kodlarını görebilir ve bizim asp sayfamızda önemli kodlar olabilir veya bazı şifreler bu sayfada tutuluyor olabilir, o zaman bu sayfanın cache'e alınması pek iyi olmaz.Veya sitemiz çok sık yenileniyor ise kullanıcı eski halini görüyor olacak.Bunun için biz bu özelliği kullanarak sayfamızın cache'te ne kadar tutulucağını belirleyebiliriz.

** ** Kullanımı: <% **Response**.Expires=10 %> Buradaki 10 dakika olaraktır.Bu sayıyı 0 yaparsanız hiç cache'e alınmaz.

**End(Son)** : Sayfamızda belli durumlar sonucunda kullanıcıya karşılık vermemesini (yani küsmesini ) sağlayabiliriz. Bu durumda o ana kadar yorumlanan bütün kodlar tarayıcıya ulaşır ve ondan sonraki hiçbir kod yorumlanmaz, buna HTML de dahil. Ayrıca bu özellik ile Buffer özelliğiyle geçici alanda tutulan tüm veri ziyaretçinin tarayıcısı ile buluşur.

Kullanımı: <% **Response**.End %>

**Request nesnesi******

Sıra geldi ASP de kullanıcıdan veri almaya.Hatırlayacağınız gibi en son kullanıcıya veri yollamayı öğrenmiştik, şimdi ise kullanıcıdan veri alacağız böylece asp sistemlerimizi kullanıcıyla tam entegre olarak çalıştırabileceğiz.

Kullanıcıdan veri alma nesnesinin adı **Request**'tir.Bu nesne ile kullanıcıdan bir çok şekillerde veri alabiliriz. Tabi bunun için **Request** nesnesinin metotlarını kullanacağız.Şimdi bunları görelim.

1.**Request**.Form: Kullanıcının doldurduğu herhangi bir form öğesinden veri almak için kullanılır.Aldığınız bu veriyi sayfanızda herhangi bir yerde kullanabilirsiniz.

Kullanımı: **Request**.Form("form\_oge\_adi") şeklinde veriyi alabilir ve bir değişkene atayabilirsiniz.
Degisken\_Adi=**Request**.Form("form\_oge\_adi")
*Not:Yukarıdaki örnekte bulunan form\_oge\_adi denen isim formdaki öğenin adıdır.***

2.**Request**.QueryString: sayfa.asp?degisken=deger gibi bir urldeki degisken adlı değişkenin değerini almada kullanılır.

Kullanımı:**Request**.QueryString("degisken\_adi") şeklinde veriyi alabilir ve **Request**.Form'daki gibi bir değişkene atanabilir.
Eğer birden fazla değişken url ile yollanacak ise sayfa.asp?degisken1=deger&degisken2=deger şeklinde yollanıp yukarıdaki gibi alınabilir.

3.**Request**.ServerVariables:Server değişkenlerinden veri alma. Hep kullanıcıdan değil de bazen sunucudan veri almamız gerekir, mesela o sırada çalışan asp sayfasının adresini buradan alabilirsiniz.

Kullanımı:**Request**.ServerVariables("degisken\_adi") şeklinde bir kod ile değeri alabilirsiniz ve bir değişkene yükleyebilirsiniz.
degisken\_adi adlı bölümde hangi kodları kullanacağınızı bilmiyorsanız buraya tıklayın ve listeyi görün.

Genel olarak **Request** nesnesi bu metotlarla kullanılır ayrıca Cookies metodu da var ama onu daha sonraki bir konuda göreceğiz.

**Session nesnesi******

** Session** nesnesi ASP uygulamalarınızda çok kullanacağınız bir nesnedir.Bu nesnemizi genel olarak tanımlamak gerekirse, eğer sitemizi bir programa benzetirsek sitemize gelen her ziyaretçi bu programı çalıştıran bir kullanıcıdır ve biz bu kullanıcı programı kapatana ( sitemizi terk edene ) kadar bir değişkende veri tutmak isteyebiliriz.Ama bu normal yollarla çok zor olur. Çünkü bir değişkeni her sayfada kullanmak için ya url ile bu değişkenleri dolaştıracak ya da cookie kullanacaksınız.İşte **session** nesnesi bu zorluğu yok ediyor.

** Session** nesnesi verilen değeri 20 dakika hafızada tutar ve sonra siler. Ama nasıl? Siz sitenizde her bir **session** tanımladığınızda ASP uyumla web sunucumuz hemen kullanıcıya 20 dakika sonra geçersiz olacak bir cookie yollar.Ve bunu siz kullandıkça otomatik olarak okur.Yani böyle bir durumda sizin bir şey yapmanıza gerek yok.

Şimdi de **session** nesnesinin özelliklerini görelim.

1.Veri yüklenmesi ve okunması

**session** nesnesine normal bir değişkene veri yükler gibi yüklenir.

Kullanımı: **session**("**session**\_adi")="deger"

Okurken de normal bir değişken gibi okunur.

Kullanımı: degisken=**session**("**session**\_adi")

2.Zamanın Uzatılması

**session** nesnesi sizin verdiğiniz bir değeri normal olarak 20 dakika tutar.Tabi siz bunu istediğiniz kadar uzatabilirsiniz.

Kullanımı: **session**.TimeOut=zaman ( zaman yerine dakika olarak bir değer yazın örnek 30 )

3.Tüm **session** nesnelerinin değerini sıfırlama

Sitemizde öyle bir an olur ki **session** nesnelerine yüklediğimiz tüm verileri bir defada silmek isteyebiliriz.

Kullanımı: **session**.Abandon

**ASP ile Cookie Kullanımı******

Arkadaşlar ASP öğrenimimizde sıra **Cookie**lere geldi şimdi.**Cookie**ler ASP uygulamalarımızda bize çok yardımcı olacak.Peki bunun ne gibi yararları var?
Mesela web sayfanıza koyduğunuz bir ankette ziyaretçiler aynı bilgisayardan üst üste oy vermesini engelleyebilirsiniz veya siteye gelip bir form dolduran ziyaretçinin tekrar geldiğinde istediğiniz bilgileri tekrar yazarak zaman kaybetmemesi için verileri o bilgisayara kaydederek buradan hemen okutabilirsiniz.

**Cookie** yollama ve okuma işlemlerini Response ve Request nesnesi ile yapıyoruz.Çok basit olan bu işlemleri şimdi yapacağız.

**Cookie** Yollama

Ziyaretçinin bilgisayarına **Cookie** yollamak için kullanılan kod.
Kullanımı:Response.**Cookie**s("**Cookie**\_adi")("anahtar")="Değer"

**Cookie**'nin Süresi

**Cookie**'nin ne zaman geçersiz olacağını belirlemek için kullanılan kod.
Kullanımı:Response.**Cookie**s("**Cookie**\_adi").Expires=# tarih # ( Tarih # July 15, 2001 # )

**Cookie**'nin Domaini

**Cookie**'nin sadece istenilen domaine yollanmasını sağlar.Tam olarak ne olduğunu anlayamadım :(
Kullanımı:Response.Cookis("**Cookie**\_adi").Domain="isim.com"

**Cookie**'nin Gönderileceği Yol

**Cookie**'nin karşı bilgisayarda istediğiniz klasöre yollanmasını sağlarsınız.
Kullanımı:Response.**Cookie**s("**Cookie**\_adi").Path="www/home"

Cooki gönderilmesi için bu kodlar size yetecektir.Bunlardan başka 2 özelliği daha var ama onları yazmıyorum.

**Cookie** Okuma

Daha önce gönderdiğiniz **Cookie**'yi okumanızı sağlar.
Kullanımı: **Cookie**\_degeri=Request.**Cookie**s("**Cookie**\_adi")("Anahtar")

**String Düzenleme******

Bu ne işimize yarayacak? ASP sayfalarında kullandığımız, aldığımız, gönderdiğimiz her veri bir stringtir.Mesela bir ziyaretçi bir formu doldurur ve gönderir işte asp sayfamıza ulaşan bu veriye biz String diyoruz.Ama aldığımız bu veri bize geldiği hali ile işimize yaramayabilir o zaman biraz operasyon yaparak bu işi halletmeliyiz.

Bu derste örnek olarak adı ' MaxiASP ' değeri ise ' Türkçe ASP Merkezi ' olan bir string kullanacağım.

**InStr **:** **Yukarıdaki gibi uzun bir string içinde daha kısa bir stringi bulmak için kullanılır.Şayet sonuç bulunursa bulunduğu noktanın karakter olarak başlangıca uzaklığını verir örn: 3 . Bunun kullanımını biraz daha açıklarsak elimizde zaten MaxiASP değişkeni var ayrıca biz Kelime adlı bir değişken oluşturuyoruz ve bunun değerini ' ASP ' yapıyoruz. Sonra sonuç 8 çıkıyor

Kullanımı: Nokta=InStr(MaxiASP, Kelime)
Bu işlemden sonra Nokta değişkeninin değeri 8 çıkmalı.

**Len** : Kullandığımız bir değişkenin uzunluğunu verir.

Kullanımı:Uzunluk=Len(MaxiASP)
Bu fonksiyon Uzunluk değişkeninin değerini 18 yapmalı.

**UCase ve LCase** : İşleme koyduğunuz değişkeni UCase ile büyük harflere çevirebilir. LCase ile küçük harflere çevirebilirsiniz.

Kullanımı: Buyuk\_Harh=UCase(MaxiASP)
Bu fonksiyon TÜRKÇE ASP MERKEZİ gibi bir sonuç çıkarmalı.
Kucuk\_Harf=LCase(MaxiASP)
Bu fonksiyon ise türkçe asp merkezi gibi bir sonuç ile karşımıza çıkmalı.

**LTrim, RTrim, Trim** : Verdiğiniz değişkenin değerinde bulunan stringin ( sırası ile ) solundaki , sağındaki ve hem sağındaki hem solundaki boşlukları temizler.

Kullanımı: Temiz\_Hal=Trim(MaxiASP) veya LTrim(MaxiASP) veya RTrim(MaxiASP)

**Space **: Vereceğiniz değer kadar içinde boşluk olan bir değişken oluşturur.

Kullanımı: Bosluk=Space(10)
Bu işlemden sonra Bosluk değişkeninin değeri ' ' olmalı.

**String** : Yeni bir string oluşturmakta kullanılır.Verdiğiniz karakter sayısında ve karakterde bir değişken oluşturur.

Kullanımı: YString=String(3, "A")
Bu işlemden sonra ise değeri ' AAA ' olan YString adında bir değişkenimiz olur.** Left, Right** : İstediğiniz bir değişkende soldan ve sağdan istediğiniz karakter kadar görüntülersiniz.

Kullanımı: Soldan=Left(MaxiASP, 6)
Şu andan itibaren Soldan değişkeninin değeri ' Türkçe ' olacak.
Sagdan=Right(MaxiASP,7)
Sagdan değişkeninin değeri ise ' Merkezi ' oldu.

**Mid **: Bu çok kullanılan bir fonksiyondur. Bu fonksiyon ile bir string veya bir değişkenin değerinde başlangıç noktasından sonra verdiğiniz karakter uzunluğuna kadar olan alanda yer alan değeri verir.

Kullanımı: Deger=Mid(MaxiASP, 8, 3)
Bu işlemden sonra Deger değişkeninin değeri ' ASP ' olacaktır.Ama neden? Bunu da siz bulun :)

**ASP ile Veritabanı******

ASP'yi belki bu kadar yaygınlaştıran en önemli etkendir veritabanı kullanımı. Çünkü ASP ile bir veritabanına ulaşmak bunu değiştirmek kolaydır. Genel olarak ASP ile veritabanına ( bundan sonra VT diyeceğim ) ulaşmak için 2 yol kullanılır.Bunlardan birisi DSN kullanarak diğeri ise DSN-less denen buna gerek kalmayan bir yöntemdir.

DSN'i sunucu bilgisayarda ayarlarsınız ve verilen bir ada göre bağlantı yapılır. Ama DSN bağlantı iyi değildir.Çünkü sunucuyu çok yavaşlatır fakat DSN-less bağlantıda sunucuya gerek kalmadan siz kodlarda VTnin yerini belirlersin ve bağlanırsınız. DSN bağlantısı pek önerilmez ve birçok bedava hosting hizmeti veren yerlerde bunu desteklemez.Ama DSN-less bağlantıyı kullanabilirsiniz.

Şimdi çok küçük bir örnek ile veritabanına bağlanalım ve ilk verilerimizi alalım...Ama bunun için önce bir VT oluşturun ve bunun adını ilk.mdb yapın (Access'te yaptığınızı varsayıyorum), sonra Yeni diyerek bir tablo oluşturun ve adını **ilk** yapın. Artık bir tablonuz var.Şimdi karşınıza Excel'e benzeyen hücreler çıkmış olmalı buradan da adı Alan1 olan hücrenin adını Adlar yapın ve alttaki hücreye bir değer yazıp kaydedin.Şimdilik bu kadar yeter sıra ASP kodumuzda.

<% Dim Ac\_Cumle, AdoConn, AdoRs, SQL
Ac\_Cumle="DBQ="& Server.Mappath("ilk.mdb") &";Driver={Microsoft Access Driver (\*.mdb)}" ' Server.Mappath'in içini veritabanı kay-
' dettiğini yere göre değiştirmeniz lazım.Bu hali ile aynı klasördeler demek.

Set AdoConn=Server.CreateObject("Adodb.Connection")
AdoConn.Open Ac\_Cumle

Set AdoRs=Server.CreatwObject("Adodb.Recordset")
SQL="Select \* from ilk"
AdoRs.Open SQL, AdoConn, 1, 3

Response.Write AdoRs("Adlar") AdoConn.close
set AdoConn=nothing AdoRs.Close
set AdoRs=nothing
%>

Bu veritabanını isimler.mdb olarak kaydedin ve metin editörünüzü açın, parmaklarınızı kıtlatıp kod yazmaya başlayın.

<%

' İlk önce veritabanının yerini belirleyelim
Veritabani\_Yer=Server.Mappath("isimler.mdb")
Vt\_Ac="DBQ="& Veritabani\_Yer &";Driver={Microsoft Access Driver (\*.mdb)}"

' Ado nesnemizi açalım.
Set Baglanti=Server.CreateObject("Adodb.Connection")
Baglanti.Open Vt\_Ac

' Kayit dizesini açalım.
Set KayitDizesi=Server.CreateObject("Adodb.Recordset")
SQL="Select \* from Adlar"
KayitDizesi.Open SQL, Baglanti, 1, 3
' Veritabanına bağlandık.Şimdi verileri alalım.
%>
<table>
<tr>
<td>Ad</td>
<td>Soyad</td>
</tr><% ' Verileri tüm kayıtlar bitene dek listeleyelim.
do while not KayitDizesi.Eof %>
<td><%=KayitDizesi("Ad")%></td>
<td><%=KayitDizesi("Soyad")%></td>
</tr>
<% KayitDizesi.MoveNext 'Bir sonraki kayıta geç
Loop ' Buna devam et.
%>
</table>

<% KayitDizesi.Close
Set KayitDizesi=Nothing ' KayitDizesi adlı nesnemizi kapattık.

Baglanti.Close
Set Baglanti=Nothing %>

Bu kodu çalıştırırsanız eğer bir hata yoksa bütün kayıtları bir tabloda Ad ve Soyad şeklinde sıralaması lazım.Kodları biraz incelerseniz ne olduğunu anlayacaksınız.

. ASP ile Vt'ye ActiveX aracılığı ile ulaşırız.Bizim Vt ile işlem yapmamızı ise ADO nesnesi sağlar.Aslında ADO bir ASP nesnesinden çok, sunucu bileşeni sayılır.Tabi ASP ye direk ADO ile değil ADO nesnesinin özellikleri ile ulaşırız.

** Connection: **ADO nesnesinden yararlanabilmek için kullanacağımız ilk nesnedir. Birçok kodda bunu görmüşsünüzdür.

| <% Dim Baglanti Set Baglanti = Server.CreateObject("**ADO**BD.**Connection**") Baglanti.Open "dsn\_adi" %> |
| --- |

Yukarıdaki kod her veritabanına bağlanma işleminde kullanılan koddur. Genel olarak işlevi Vt ile iletişime geçer ve açar yalnız içindeki kayıtlara ulaşmaz.

**Recordset **: Çok fazla kullanacağımız ADO'nun bu nesnesi ise verilerle oynamamızı ve Vt'de kayıtlı duran verileri istediğimiz gibi kullanmamızı, değiştirmemizi ve silmemizi sağlayacak.Recordset nesnesi ile yapabileceklerimizi aslında daha önceki konularımızda gördüğümüz SQL ile de yapabiliriz ama Recordset nesnesinin kullanımı daha kolay olduğu için birçok kişi Recordset'i tercih eder.

Biz genel olarak Recordset'in .Open, .AddNew, .Delete, .Update .Close gibi özelliklerini göreceğiz.

**Open**: Recordset ile bağlantıyı açmak için kullanılır. Yazdığınız SQL koduna göre bağlantıyı açar ve kullanıma hazır bir hale getirir.

| <% Dim Baglanti Set Baglanti = Server.CreateObject("**ADO**BD.**Connection**") Baglanti.Open "dsn\_adi" Dim KayitDizisi Set KayitDizisi = Server.CreateObject("**ADO**DB.**Recordset**") SQL = "Select \* from Tablo\_Adi" KayitDizisi.**Open** SQL, Baglanti, 1, 3 %> |
| --- |

AddNew, Delete, Update ve Close: Bunlar ise Vt'de oynama yapmamız için gerekli olan kodların bir bölümü.Hepsi İngilizce ve Türkçe anlamları var. Yani YeniKayıt, Sil, Güncelle ve Kapat gibi.

SQL Structured Query Languge demektir yani dilimizde Yapısal Sorgu Dili anlamına gelmektedir.Zaten SQL'i biz sorgularımızda kullanacağız.SQL'in bir çok komutu vardır ama biz genel olarak SELECT, UPDATE, INSTERT, DELETE'i göreceğiz. Ama en çok üstünde duracağımız ve sizinde en çok kullanacağınız SELECT olacak diğer komutların işlevlerini ise Recordset ile yapacağız.

**SELECT** : Veritabanından veri çekmeye yarayan kod.Zaten sözlük karşılığı ile Seç anlamına gelen bu komut ile veritabanımızdaki verileri istediğimiz kriterlere göre seçeriz.
Kullanımı: SQL = "Select \* from tablo\_adi" tablo adı yazan yere ise tablonuzun adınızı yazıcaksınız.
Bu komut ile tablo\_adi adındaki tablonun içerdiği tüm kayıtlar seçilmiş olur.

Ama siz belli bir kritere göre seçme yapmasını istiyor olabilirsiniz.Mesela, Kayitlar tablomuzdaki Yas alanından yaşı 18 olanları seçebilirsiniz.
SQL = "Select \* from Kayitlar where Yas = 16"
Bu SQL'in kullanıldığı bir bağlantıda yaşını 16 olarak giren tüm kayıtlar seçilmiş olacaktır.

Buda değil de siz adına göre seçme yapmak istiyorsanız aşağıdaki gibi bir SQL koduna ihtiyacını olacak.
SQL = "Select \* from Kayitlar where Isim = 'Mine' "
Yukarıdaki kod ile aralarında bir fark var değil mi? Evet ' işaretleri fark. Bu işaretler vt'den bir veriyi text ile seçmek için kullanılır ama sayıda buna gerek yoktur.

Bu kadar yöntemden başka siz ben adında geçen harflere göre arama yapmak istiyorum dersleniz.Şöyle bir kod işinizi görür.
SQL = "Select \* from Kayitlar where Isim like 'ER' "
Bu kod ile yaptığınız seçmede adında ER geçen tüm kayıtlar seçilir.(Örn: mERt, bERk,..)

**WHERE NEREDE******

Bir veritabanından sorgularken daha önce verileri nasıl belli bir kritere göre sıralayacağımız görmüştük ama bu kadar yüzeysel yapılan bir iş değil. Bizde şimdi bu işin ayrıntılarını göreceğiz çünkü bunu çok kullanacaksınız. SQL ile sorgulama komutu WHERE dir. Şimdi where komutu ile sorgulamayı görelim.Yalnız where ile 2 çeşit sorgulama yapabiliriz.Tam karşılığa göre sorgulama, yaklaşık değere göre sorgulama.

** Tam Değere Göre Sorgulama:
** 1- Sayı Sorgulamak için: Eğer veritabanımızdaki kayıtlarda örneğin kişilerin yaşına göre sorgulama yapacaksak ve sadece yaşı belli bir sayı olanları alacaksak,
SQL = "Select \* from tablo\_adi where YAS = 17"
Bu komut ile yaşı 17 olan kişileri seçersiniz.

2- Metin Sorgulamak için: Eğer veritabanımızdaki (örn:) kişileri adına göre sorgulayacaksak,
SQL = "Select \* from tablo\_adi where AD = 'MINE' "
Bu komut sayesinde adı Mine olan kızları seçtik** **

**Yaklaşık Değere Göre Sorgulama:
**Aslen yukarıdaki sayı ve metin sorgulama ile aynı komuttur sadece küçük bir değişiklik ve birkaç ek vardır.Bu sorgulama ile (örn:) adında ay geçenleri sorgula dersek Ayla, Ayşe, Tolunay gibi kayıtlarda gelecektir.
SQL = "Select \* from tablo\_adi where AD like '%AY%' "
Bu komut sayesinde yukarıdaki örnekte olduğu gibi isimler gelecektir.

.

ARRAY:

Dizi değişkenlere Array denir ve içinde birden çok değer tutabilir.Ama normal bir değişken sadece bir değer tutar.Bunu bir örnekle açıklayalım.Şimdi bir Hafta adlı bir dizi değişkenimiz olsun ve biz bu değişkene haftadaki günleri yükleyelim.

Dim Hafta=Array("Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi", "Pazar")

Gördüğünüz gibi Hafta değişkeninin toplam 7 değeri var ve siz bunlardan istediğinizi kullanabilirsiniz.Örneğiniz Cumartesi gününü ekrana yazdırmak için <%=Hafta(5)%> gibi bir kod kullanmanız lazım.Bu 5 sayısı Cumartesinin sıra sayısıdır.Şimdi bazı arkadaşlar benim için sayfayı bilmiyor orada 6 yazmalıdır diyebilir ama değil orada 5 yazmalı çünkü VBScript saymaya 0'dan başlar onun için 5 Cumartesi demektir.

ASP sayfalarınızda bir dizi değişken oluşturmak istiyorsanız bunu aşağıdaki gibi belirtmeniz lazım.
Kullanımı: <% Dim Dizi\_Degisken\_Adi() %> normalde parantezler içinde alacağı değerlerin toplam sayısı yer almalı ama biz burada sayı vermeyerek dinamik bir değişken oluşturuyoruz.

Eğer bu dizi değişkeninin eleman sayısını daha sonra belirlemek istiyorsanız,
Kullanımı: <% ReDim Dizi\_Degisken\_Adi(5) %> bu şekilde yazmanız lazım.Ama bu yazacağınız kod değişken içindeki değerleri siler.

Verilerinizi korumak içinse,
Kullanımı : <% ReDim Preserve Dizi\_Degisken\_Adi(5) %> kodunu kullanmanız lazım.Böylece verilerinize birşey olmaz.

Tabi sadece bu işe yaramaz bir dizi değişkende ki her değere 2 tane değer verebilirsiniz.Biraz karışık olan bu olayı bir örnekle açıklayayım.
<% Dim Ogrenciler()
Ogrenciler(1,1)="Bahadır"
Ogrenciler(1,2)="ARSLAN"
Ogrenciler(2,1)="Hasan Aybars"
Ogrenciler(2,2)="ARSLAN" %>

Yukarıda Ogrenciler dizi değişkenine her kullanıcının hem adını hem de soyadını yükledik.Buradaki değerleri de istediğimiz gibi sıralayabiliriz.

Dinamik bir dizi değişkenimizin eleman sayısını öğrenmek içinse,
<% Eleman\_Sayisi=UBOUND(Ogrenciler) %> kodunu kullanmanız lazım.

İF ELSE

Biraz İngilizce bilenler hemen kavrayacaklardır zaten. if dilimizde eğer, else ise veya demektir.Herhalde biraz anlamışsınızdır.Yani burada yapılacak olay eğer şu şöyle ise böyle yap yok öyle değilse böyle yap.

Kullanımı: if koşul then
bu koşulda yapılacaklar
else
else
diğer durumda yapılacaklar.

Bu konuyu kısa bir örnekle özetleyelim ve öğrenelim.

| <% if Hour(Date) > 12 then Response.Write "Günaydın" else if Hour(Date)>12 and <14 then Response.Write "Tünaydın" else Response.Write "İyi Akşamlar" end if %> |
| --- |

Arkadaşlar gördüğünüz gibi çok kısa bir kod ile bunu gördük.Burada ne oluyor.ASP programımız önce öğesinden Hour değerini alıyor böylece saati elde ediyoruz ve diyoruz ki eğer saat 12'den küçükse daha sabahtır günaydın.Yok 12'den büyük ama 14'ten küçükse daha öğlen o zaman tünaydın yok o da değilse akşam veya gecedir biz kısaca iyi akşamlar diyelim diyoruz...

**FSO nedir? ******

FSO’nun açılımı FileSystemObject tir. FSO ile dosya yaratabilir, silebilir, özelliklerine bakabiliriz. Şimdi FSO ile yapacağımız ilk örneğe geçelim.

<HTML><BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#000000" VLINK="#000000">
<BR>
<B>Dosya Arşivim:</B><BR><BR>
<TABLE BORDER=0 CELLPADDING=3 CELLSPACING=0>
<TR BGCOLOR="#b0c4e5"><TD><FONT COLOR="#FFFFFF"><B>Dosyaadı:</B></FONT></TD><TD><FONT COLOR="#FFFFFF"><B>Byte:</B></FONT></TD><TD><FONT COLOR="#FFFFFF"><B>Dosya Tipi:</B></FONT></TD><TD><FONT COLOR="#FFFFFF"><B>Yaratılış Tarihi:</B></FONT></TD>
<%

' FSO objesini yarattık

Set DosyaObjem=Server.CreateObject("Scripting.FileSystemObject")

' Klasor objesini yarattık

Set Klasorum=DosyaObjem.GetFolder(Server.MapPath("shared"))

'Kayıtları tekrarladık

FOR EACH thing in Klasorum.Files

%>
<TR BGCOLOR="#c0c0c0"><TD><A HREF="shared/<%=thing.Name%>"><%=thing.Name%></A></TD><TD ALIGN=RIGHT><%=thing.Size%>byte</TD><TD><%=thing.Type%></TD><TD><%=thing.DateCreated%></TD>
<%

NEXT

%>

</TABLE>
</BODY>
</HTML>

**Çıktısı:**

**Dosya Arsivim:******

| **Dosyaadi:****** | **Byte:****** | **Dosya Tipi:****** | **Yaratilis Tarihi:****** |
| --- | --- | --- | --- |
|  | byte |  |  |

Şimdi de bu kodda neler yaptığımızı açıklayalım. 9.ncu satıra kadar olan kısımda table’ı yarattık. 9.ncu ASP scriptimize başladık. 11.ncu satırda dosya objesini yarattık. 13.ncu satır bizim için çok önem taşıyor. Çünkü burada içini gözetleyeceğimiz klasörün ismini giriyoruz. O da **shared **olarak girilmiş. Ana klasöre yani root’a bakmak istiyorsak o satırı şöyle değiştirmeliyiz:

Set Klasorum=DosyaObjem.GetFolder(Server.MapPath("/"))

Daha sonra thing adlı bir obje yarattık. Thing sayesinde dosyanın özelliklerine bakabildik.

FSO nesnesi aslında tehlikeli bir nesnedir.Yanlış kullanıldığında tüm sunucuyu göçertebilir çünkü tüm dosyalara tam erişim elde edilebilir tabi eğer sunucu güvenlik olayına fazla önem vermedi ise.Yine de pek iyi işler için kullanılmayan bu sistem aslında bir web sitesinin dosyalarını FTP olmadan herhangi bir yerden değiştirmek için kullanılabilir.

FSO nesnesi bir sunucu nesnesi olduğunda veritabanı nesnesi olan ADO'yu açar gibi açıyoruz.Yani,

| <% Dim FSO Set FSO = Server.CreateObject("Scripting.FileSystemObject") %> |
| --- |

Bundan sonra FSO nesnesini kullanabilmek için bazı özellikleri ve değerleri almamız gerekir.Mesela sunucudaki sürücülere ( C:, D: gibi ) ulaşabilmek için. Drives nesnesini kullanırız.Yalnız bizim alacağımız değer bir koleksiyondur.O bilgisayardaki tüm sürücüleri içerir.

| <% Dim Suruculer Set Suruculer = FSO.Drives %> |
| --- |

...

İlk önce standart bağlantı kodlarımızı yazalım...

| <% Dim FSO, Suruculer, Surucu, KokKlasor, glnKlasor glnKlasor = Request.QueryString("klasor") Set FSO = Server.Createobject("Scripting.FileSystemObject") if GlnKlasor = "" then Set KokKlasor = Fso.GetFolder("C:\\Inetpub\\wwwroot") else Set KokKlasor = Fso.GetFolder(GlnKlasor) end if Set altKlasorler = KokKlasor.SubFolders Set Dosyalar = KokKlasor.Files %> |
| --- |

Kodlarımızın başında değişkenleri tanımladıktan sonra glnKlasor diye bir şey aldık url'den.Bunu biraz sonra kullanacağımız bir sorgu için başta alıyoruz.Bundan sonra ise FSO nesnemizi yarattık ve az önce bahsettiğimiz sorguya geldik.Burada glnKlasor değişkeninin boş olup olmadığına bakıyoruz eğer boşsa C:\\Inetpub\\wwwroot klasörüne eğer değilse bize url ile yollanan klasöre gitmesini söylüyoruz.Sıra az önce gittiğimiz klasördeki dosyalar ve alt klasörler.

SubFolder ve Files Dosya nesnesinin birer öğeleridir.Biraz İngilizce biliyorsanız hemen anlamlarını çözeceksinizdir.Alt Klasörler ve Dosyalar anlamına gelir.Bunlarda sürücüler nesnesi gibi koleksiyondur yani tüm klasör ve dosyaları içeririler.Bunları da sıra ile For...Each döngüsü yardımını da alarak listeyebiliriz.

Degiskenler bizim Asp programlari yazarken en yakin dostlarimiz olacaklar.Ilk örnegimizde bir degisken tanimlamistik.Ama simdi biz simdi bu isin ayrintilarina girecegiz.
Hatirladiginiz gibi degiskenleri **DIM** komutu ile tanimliyoruz.Dim kelimesi Dimension kelimesinin kisaltilmasindan geliyor.Bu komutu asp sayfalarinizda çok çok kulanacaksiniz ama isterseniz kullanmayabilirsiniz.Nasil? VBScript diger dillerdeki gibi illa kulanilan bütün degiskenlerin tanimlanmasini zorunlu kilmaz ve sanki siz bunu tanimlamissiniz gibi sayfayi çalistirir.Ama bu iyi bir programcilik degildir.Çünkü siz hiç degisken tanimaladan sayfa içinde kafaniza göre degiskenleri belirliyorsunuz ama bir kaç yerde degiskenin adini yanlis yazarsaniz bir hata mesaji ile karsilasmazsiniz ve hata yaparsiniz.
Peki bu nasil önlenir.VBScript'i yapanlar bunu da düsünmüs.Bunun için sayfanizin basina **<% OPTION EXPLICIT %>** yazarsaniz VBScript eger DIM komutu ile tanimlanmamis bir degiskeni kullanirsaniz hata verdiriyor.
Bu kadar bilgiden sonra artik su isin detayina girelim.Degiskenleri degisik sekillerde tanimlayabilirsiniz ama nasil ?

Mesela böyle:

| <% Dim Ad, Soyad, Yas, Email Ad="Bahadir" Soyad="ARSLAN" Yas=16 Email="maxipower@turk.net" %> |
| --- |

Yukaridaki örnek standart bir yol yani ilk önce degiskenlerin adlari sonra degerleri yazilir ama burda size farkli gelen bir sey var mi?Eger dikkatli bir ziyaretçi iseniz Yas=16 satirinda tirnak (") isaretinin olmadigini fark etmissinizdir degil mi? Bu degisken tanimlanirken bir kuraldir, yani eger bir degiskenin degerini sayi olarak atiyacaksaniz tirnak isareti kullanilmaz.Peki kullanirsaniz ne olur? Eger bu degiskenlerle matematik islemi yapmaya kalkarsaniz toplama hariç hata alirsaniz ama toplamada bu sayilar yanyana gelir.Bunu bir örnekle görelim.

| <% Dim ilksayi, ikincisayi, toplam ilksayi="15" ikincisayi="5" %> <% toplam=ilksayi + ikincisayi %> <%=toplam%> |
| --- |

Bu yukaridaki kodlari web sunucunuzun kök dizinine **toplama1.asp** adinda kaydedin ve açin.Sonuç ne? 155 degil mi? Simdi iki sayinin önündeki ve arkasindaki tirnaklari kaldirip **toplama2.asp** adinda kaydedip açin.Simdi sonuç ne? 20 degil mi? Iste tirnak koymanin farki budur.
Hazir aklima gelmisken bir degisken tanimlarken kesinlikle türkçe karakter kullanmayin çünkü serveriniz bunu desteklemeyebilir.Bunun nedeni çogu asp serverinin Ingilizce olmasi...
Bu konuda bu kadar en kisa zamanda devami ile bulusmak üzere...

**Veriler, hedefiniz ASP sayfasidir.******

Bir formdan ASP ile veri almak çok kolay ve zevklidir.Isterseniz hiç lafi uzatmayalim ve hemen basliyalim.

Simdi basit bir html dosyasindan ASP sayfasina veri aktaracagiz.Iste yukarida da dedikya bu çok kolaydir, HTML veya JavaScript ile ugrasanlar bilirler; bir sayfadan diger sayfaya veri göndermek için o kadar çok çalisirlardi ki sonunda çogu vaz geçerdi ama ASP de bunun ne kadar kolay olduguna simdi hepimiz sahit olacagiz.

Peki nerelerde bunu kullaniriz? En basit örnek ziyaretçi defteri, mesaj formu, kayit islemleri, hep bu yöntemle yapilir.Bunu ögrendikten sonra sizde yavas yavas güzel seyler yapabileceksiniz ASP ile.

Simdi örnegimiz için bir HTML sayfasi yaratip bunu, **form.html** diye kaydediyoruz.

| <html> <head> <title>Form</title> </head> <body> <center>Asagidaki formu doldurur musunuz?</center> <form name=deneme action=veri\_al.asp method=post> Adiniz:<input type=text size=20 name=isim><br> Email Adresiniz:<input type=text size=20 name=email><br> <input type=submit value=Gönder><br> </body> </html> |
| --- |

Burada hersey normal simdi ASP de bu isi nasil yapacagiz? VBScript'te biz baska bir sayfadan form aracilgi ile gelen veriyi almak için

| <% veri=Request.Form("formdaki\_adi") %> |
| --- |

kodunu kullaniriz.Eger veri form ile degilde sorgu ile geliyorsa (örn:söyle bir link ile veri\_al.asp?isim=Maxipower) bu sefer bu veriyi alip kullanmak için ise su kodu kullaniriz.

| <% veri=Request.QueryString("sorgudaki\_adi %> |
| --- |

bu kod hakkindaki bilgiyi bir dahaki konuda bulabilirsiniz.
Neyse biz en son ASP ile veriyi isleyecektik.Simdi **veri\_al.asp** dosyasina bakalim.

| <% Dim isim Dim email ' Degiskenleri tanimladik simdi verileri alalim. isim=Request.Form("isim") email=Request.Form("email") ' Verileri aldik ve HTML sayfasinda kullanmaya hazirladik %> <html> <head> <title>Veri Alindi</title> </head> <body> Adiniz:<b><%=isim%><br> Email Adresiniz:<b><%=email%> </body> </html> |
| --- |

Asp sayfalarinda simdi sira veriyi url ile yollamaya geldi.Peki bu nedemek? Nasil oluyor bu olay? Simdi söyle açiklayayim...
Mesela söyle bir link görmüssünüzdür "falan.asp?konu=asp&sayfa=1" ve gördükten sonra bu ne biçim link böyle sey mi olur öyle sayfa adi mi olur diye düsünmüssünüzdür.Bu çok normal çünkü bu garip bir link ve biz buna sorgu ile veri yollama diyoruz.

Asp sayfalarinda veri sadece form ile gitmez bir de url ile veri yollanir ama sadece yazi olarak yollanir ve bu çesit veri yollamada da veriyi almak çok basittir.Peki bunu nerelerde kullanabiliriz? Bu çesit veri yollama teknikleri ileri asp uygulamalarinda kullanilir, mesela formlarda, alisveris sitelerinde vb...

Mesela bizde bir örnek ile bunu görelim.Asagidaki kodlar basit bir HTML sayfasinin kodlari bu kodlari **link.html** adiyla kaydedin.

| <html> <head> <title>Sorgu Degiskenleri</title> </head> <body> <center>Lütfen <a href="sorgu.asp?ad=Bahadir"> tiklayiniz</a>. </center> </body> </html> |
| --- |

Burada gördügünüz gibi sorgu.asp sayfasina "ad" adindaki bir degisken yollaniyor ve degeri Bahadir. Simdi **sorgu.asp** sayfasinin kodlarina bakalim.

| <% ' Degiskenleri belirleyelim Dim ad ' Simdi veriyi alalim ad=Request.QueryString("ad") %> <html> <head> <title>Sorgu Geldi</title> </head> <body> <center>Adiniz:<%=ad%></center> </body> </html> |
| --- |

Bakin veri ne kadar kolay da geldi.Burda bir tane veri yolladik ya daha fazla olursa nasil olacak o zaman yukaridaki kodlari asagidaki gibi degistirip kaydedin.

| <html> <head> <title>Sorgu Degiskenleri</title> </head> <body> <center>Lütfen <a href="sorgu.asp?ad=Bahadir&cinsiyet=erk"> tiklayiniz</a>. </center> </body> </html> |
| --- |

Farki gördünüz mü? "&" isareti peki ikinci veriyi nasil kullanabiliriz iste size bir örnek...

| <% ' Degiskenleri belirleyelim Dim ad Dim cinsiyet ' Simdi veriyi alalim ad=Request.QueryString("ad") cinsiyet=Request.QueryString("cinsiyet") %> <html> <head> <title>Sorgu Geldi</title> </head> <body> <center>Sayin <%=ad%><%if cinsiyet=erk then Response.Write "Bey" else Response.Write "Hanim" end if %> </center> </body> </html> |
| --- |

**Metin dosyasina giren veriler.******

Asp sadece veri alip bunu ekranda göstermek degildir.Ayni zamanda bu verileri islemektirde.Bu nasil yapilabilir mesela bunlari bir .txt dosyasina kaydedebilirsiniz veya okuyabilirsiniz.Böylece ziyaretçiden verileri alip kaydedebilirsiniz.Bu sayede kendinize basit bir ziyaretçi defteri hazirlayabilirsiniz.

Yukarida yazdigimiz olayi yapmadan önce bazi seyleri anlatalim.VBScript ile sayfa hazilarken bazen sunucu araçlari kullaniriz.Bunlar sunucunuzda belirlidir, mesela veritabanina baglanmak için ( buna ileride deginecegiz ), yukaridaki gibi dosyalara yazi yazdirmak için , sayfanizdan mail yollamak için... Peki bu nasil olacak bunu yapabilmek için su kod kullanilir:

| <% Dim Degisken Set Degisken=**Server.CreateObject("**yaratilacak\_obje**")** %> |
| --- |

"yaratilacak\_obje" yazan yere ise objenin adi yazilir bunlarda örnegin;

| Veritabanina Baglanmak için: | **Adodb.Connection****** |
| --- | --- |
| Dosyalara yazi yazmak için: | **Scripting.FileSystemObject****** |

yukaridakiler.Simdi bunlari anlattiktan sonra böyle bir deneme yapalim.

Önce asagidaki kodlari **forum.htm** adinda kaydedin.

| <html> <head> <title>Bilgi</title> </head> <body> <form method="post" action="yazi\_kaydet.asp"> <table border="0" width="100%" cellspacing="0" cellpadding="0"> <tr> <td width="50%">Adiniz:</td> <td width="50%"><input type="text" name="isim" size="20"></td> </tr> <tr> <td width="50%">Cinsiyetiniz:</td> <td width="50%"><select name="cinsiyet" size="1"> <option value="erk">Bay</option> <option value="byn">Bayan</option> </select></td> </tr> <tr> <td width="50%"></td> <td width="50%"><input type="submit" value="Gönder" name="B1"></td> </tr> </table> </form> </body> </html> |
| --- |

Yukaridaki kodlarda bir anlasilmazlik yok sanirim simdi verileri alacak ve isleyecek olan **yazi\_kaydet.asp** dosyasinin kodlari yazalim.

| <% Dim Dosya\_Sistemi Dim Dosya\_Yaz Dim isim Dim cinsiyet Dim Dosya\_Yol ' Degiskenleri aldik simdi verileri alalim isim=Request.Form("isim") cinsiyet=Request.Form("cinsiyet") ' Verileri de aldik simdi isleyelim Dosya\_Yol=Server.Mappath("veriler.txt") Set Dosya\_Sistemi=Server.CreateObject("Scripting.FileSystemObject") Set Dosya\_Yaz=Dosya\_Sistemi.CreateTextFile(Dosya\_Yol,True) Dosya\_Yaz.WriteLine("Ziyaretçinizin adi:" & isim) Dosya\_Yaz.WriteLine("Ziyaretçinizi cinsiyeti: " & cinsiyet ) Dosya\_Yaz.Close %> <html> <head> <title>Bilgi Alindi</title> </head> <body> <% ' Biraz güzellik olsun if cinsiyet="erk" then cinsiyet="Bey" else cinsiyet="Hanim" end if %> <center><%=isim %>,<%=cinsiyet %></center><br> Bilgileriniz için sagolun. </html> </body> |
| --- |

Simdi bu dosyayi çalistirin ve kaydettiginiz klasörde bir veriler.txt adinda bir dosya var mi diye bakin.Peki olay nasil oldu?
Ilk önce bir sunucu nesnesi olusturduk sonra kodlarda belirttigimiz adreste bir dosya olusturduk ve **WriteLine** komutu ile verilerimizi yazdik.

**ASP ile SAYAC******

Web sayfanizda bir sayac olsun istiyorsunuz ama benim olsun, sonra güzel olsun söyle sah sahali olsun diyorsaniz tamam o zaman bu konu tam size göre... Simdi asagidaki kodlari kullanarak kendi sayacinizi olusturun..

<%
'sayaci olan bir asp sayfasi

Dim DosyaSistemi, sayacDosyasi, sayacdegeri

Set DosyaSistemi = CreateObject("Scripting.FileSystemObject")
Set sayacDosyasi = DosyaSistemi.OpenTextFile("c:\\inetpub\\wwwroot\\asp\\say\\say.txt",1)

sayacdegeri = sayacdosyasi.ReadLine
sayacdegeri = sayacdegeri + 1

'sayacdosyasi.close

If sayacdegeri>0 then

Dim fso, MyFile
Set fso = CreateObject("Scripting.FileSystemObject")
Set MyFile = fso.CreateTextFile("c:\\inetpub\\wwwroot\\asp\\say\\say.txt", True)
MyFile.WriteLine(sayacdegeri)
MyFile.Close

end if

sayacdosyasi.close

dim birler, onlar, yuzler, binler, onbinler

onbinler = int(sayacdegeri / 10000)
sayacdegeri = sayacdegeri - onbinler \* 10000

binler = int(sayacdegeri / 1000)
sayacdegeri = sayacdegeri - binler \* 1000

yuzler = int(sayacdegeri / 100)
sayacdegeri = sayacdegeri - yuzler \* 100

onlar = int(sayacdegeri / 10)
sayacdegeri = sayacdegeri - onlar \* 10

birler = sayacdegeri

%>

<p>
<table border=0 cellspacing=0 cellpedding=0 bgcolor="#000000">
<tr bgcolor=000000>
<td align=center>
<img src="<%=onbinler%>.gif">
<img src="<%=binler%>.gif">
<img src="<%=yuzler%>.gif">
<img src="<%=onlar%>.gif">
<img src="<%=birler%>.gif">
</td>
</tr>
<!--<tr bgcolor=000000>
<td>
<img src="wwwalcisorg.gif">
</td>
</tr>-->
</table>

**AÇIKLAMA:**
kullanilan rakam resimlerini hazirlayiniz.
1.gif 2.gif ... diye bütün rakamlari hazirlamaniz gerekiyor.
sonra ayni dizine koymaniz yeterli.

Site'de bulunan ziyaretçileri sayalim.

Asp teknolojisini web sayfalarinda uygulamak isteyen insanlarin bence yapabilecegi en basit ve güzel sey budur.Yani sitede o an bulunan insanlarin saysini belirtmesi.
Bunun yarari ne olabilir? Ziyaretçi o siteye ne kadar ilgi oldugunu görebilir ve onla beraber sitede kaç kisi oldugunu bilebilir.
Bu nasil olacak, veritabani falan kullanacakmiyiz diye soruyorsaniz hayir, bu isi **global.asa** denen bir dosya ile yapacagiz.Bu dosya ne? Bu dosya PWS ve IIS kurulurken olusturulur.Bu dosyada sitemize bir ziyaretçinin gelmesi durumunda ne olacak çikmasi durumunda ne yapilacagina dair bilgiler tutulur ki bizde zaten bunu kullanacagiz.Ayrica bu dosyada sitenizin tüm sayfalarinda kullandiginiz ve hiç degismemesini istediginiz veriler bulanabilir.Içerigi bir ASP sayfasi ile aynidir ama uzantisi **.asp** degil **.asa** yani **Active Server Application**** ****( Aktif Sunucu Uygulamasidir ).**Web sunucunuz sitenize bir zayretçi geldiginiz hemen bu dosyayi icra eder...
Az önce dedim ya **global.asa **dosyasinda biz ziyaretçi web sitenize ulastiginda ne yapilacagini belirtebiliriz bizde öyle yapip basit bir sayaç koyacagiz, her yeni bir **Session** açildiginda sayaç bir artacak **Session** kapandigin sayaçtan bir çikarilacak.
Simdi bu **global.asa** dosyasini görelim.Bu hiç degistirilmemis halidir.

| <SCRIPT LANGUAGE=VBScript RUNAT=Server> </SCRIPT> |
| --- |

Biz ise bunu isimize yarayacak sekilde degistiriyoruz.

| <SCRIPT LANGUAGE=VBScript RUNAT=Server> Sub Application\_OnStart Application("online") = 0 End Sub Sub Application\_OnEnd End Sub Sub Session\_OnStart Session.Timeout = 5 Session("Start") = Now Application.lock Application("online") = Application("online") + 1 'Her yeni biri geldiginde sayaci bir arttiriyoruz Application.unlock End Sub Sub Session\_OnEnd Application.lock Application("online") = Application("online") - 1 'ziyaretçi browserini kapattiginda ise bir çikariyoruz Application.unlock End Sub </SCRIPT> |
| --- |

Bu kadar basit simdi bunu **default.asp** adindaki ana sayfamizda nasil gösterecegiz ona bakalim.

| <html> <head><title>Online Ziyaretçiler</title></head> <body> <center>Siz <b><%=Application("online") %><b> aktif ziyaretçiden 1'isiniz.</center> </body> </html> |
| --- |

Simdi açin **default.asp** dosyasini yalniz **default.asp** ile** global.asa** ayni klasörde olmali.

*Not: Su an hizmet veren bedava asp serverlarindan yalniz FreeSQLHost global.asa dosyasini desteklemektedirler.Diger serverlar güvenlik açisindan bu dosyanin destegini kapatmislardir.Eger sizin serverinizin destekleyip desteklemediginiz bilmek istiyorsaniz lütfen destek birimlerine sorunuz.***

Verileri birde Veritabanina sokalim bakalim!

ASP'nin bu kadar yayginlasmasinin en büyük sebebi veritabani uygulamalari.Yani ASP veritabani ile baglanti olaylarini çok basitlestirerek bize büyük bir hizmet veriyor.

Ee kolay dedikse o kadar degil, yani çok sorun çikartan bir olay.ASP HTML gibi hatalari umursamayan bir degildir.En ufak bir tirnak (") isareti hayatinizi degistirebilir.Mesela siz yazdiginiz yüzlerce satiri deniyorsunuz ve bir yerde koydugunuz veya koymadiginiz tirnak isareti yüzünden hata verdigi zaman siz o bilgisayara kafa atarak kafanizi kirabilirsiniz.Böyle bir son ile karsilasmamak için sakin olun ve sakin olun, yani sadece sakin olun.

Konularimiz arasinda verileri bir metin belgesine kaydetmeyi gördük ya biz bunlari daha kullanisli olan veritabanina kaydetmek istersek.Biz bunu basit bir uygulama ile görelim ve ögrenelim.

Simdi bir form içeren HTML dosyamiz olsun ve bunun adi **form.htm** olsun.Kodlarida asagidaki gibi olsun,

| <html> <head> <title>Form</title> </head> <body> <div align="center"><center> <form name=bilgi action=kaydet.asp method=post> <table border=1 cellspacing="0" cellpadding="0" > <tr> <td>Adiniz:</td> <td><input type=text name=isim></td> </tr><tr> <td>Mail Adresiniz:></td> <td><input type=text name=mail></td> </tr></table> </form> </div></center> </body> </html> |
| --- |

Bu yukaridaki kodlarda bir form olusturduk ve formun sonuçlarini **kaydet.asp** adli bir **.asp** dosyasina yollamasini söyledik.Simde de **kaydet.asp** dosyasinin kodlarina bakalim.

<% ' Ilk önce verileri formdan alalim. %>
<% ad=Request.Form("isim)
email=Request.Form("mail") %>
<% ' Verileri aldik simdi veritabani için .dmb dosyasinin yerini belirleyelim. %>
<% Vt\_Yol=Server.Mappath("vt.mdb") ' vt.mdb adinda bir dosyamiz oldugunuz varsayiyoruz.
' Simdi Veritabanina baglanacagiz.
Set Baglantim=Server.CreateObject("Adodb.Connection")
Baglantim.Open "DBQ="& Vt\_Yol & ";Driver={Microsoft Access Driver (\*.mdb)}"
' Veritabanina baglanti açtik simdi verileri islemeye yariyacak Recordset nesnesini olusturalim
Set Rs=Server.CreateObject("Adodb.Recordset")
' Sira SQL sorgusunu olusturmaya geldi
Sorgu="Select \* from tblZiyaretci" ' Biz vt.msb dosyamizda tblZiyaretci adinda bir tablo var oldugunu varsaydik.
Rs.Open Sorgu, Baglantim, 1, 3 ' Evet sonunda açma islemleri bitti. %>

<% Rs.AddNew ' Yeni bir kayit ekle
Rs("alnIsim")=ad ' Bunun içinde tblZiyaretci tablosunda alnIsim adli bir alan var diye düsündük
Rs("alnMail")=email
Rs.Update ' Veritabanina girilen bilgileri güncelledik.
%>

<html><head><title>Bilgiler Girildi</title></head>
<body><center>Bilgileriniz girildi</center></body></html>

<% Rs.Close
Set Rs=Nothing
Baglantim.Close
Set Baglantim=Nothing
' Açtigimiz baglantilari kapattik ve islem bitti
%>

Eger hersey dogru ise su an bir sorun olmadan verileriniz veritabanina girilmis olmali.Eger bir sorun var ise lütfen maxipower@turk.net adresine mail atin.

URL sorgusu ile Yönlendirme

Bana en çok yöneltilen sorulardan biri yolla.asp?no=x seklindeki bir url ile nasil islem yapildigi veya veritabanindan verilerin nasil alindigi.Buna zamaninda DownloadYoneticisi adli örnek ile cevap vermek istedim ama yapamamisim onun için bende en iyisi böyle bir uygulama yazisi ile bunu anlatayim dedim.

Arkadaslar daha önceki konularimizda url ile verilerin nasil yollanip alinacagini ögrenmistik onun için burada onun üstünde durmuyorum ve direk konuyu anlatmaya basliyorum.
Yalniz bu örnegi uygulayabilmek için önce bazi hazirliklar yapmamiz lazim, mesela bir veritabani hazirlamaliyiz.Simdi içinde **Sayfalar **adinda bir tablo olan **syf.mdb **adinda bir veritabani olusturun ve bunu bu örnegi uygulayacaginiz klasöre koyun.Sonra veritabani içinde bununda Sayfalar adli tablonun içinde **id , url **adli ili alan olusturun.Ve örnek olarak birinci satirlari su sekilde doldurun.

| **id****** | **url****** |
| --- | --- |
| 1 | birinci.htm |
| 2 | ikinci.htm |

Simdi ilk sayfamizi hazirliyalim ve bu sayfanin adini **default.asp** yapalim.

<% veri\_yol=server.mappath("syf.mdb") ' Veritabaninin yerini belirttik.
set veri=server.createobject("adodb.connection") ' Ado'nun Connecion nesnesine ulastik
veri.open "DBQ="& veri\_yol &";Driver={Microsoft Access Driver (\*.mdb)}" ' Baglantiyi açtik
set kd=server.createobject("adodb.recordset") ' Kayit Dizisine ulastik.
sorgu="select \* from Sayfalar" ' SQL sorgusu, bu ile Sayfalar tablosunu seçtik
kd.open Sorgu, veri, 1, 3 ' Sonunda Kayit dizisini açtik.
' Artik veriler emrimize amade.
%>
<p align="center">Asagidaki sayfalardan birini seçiniz.</p>
<div align="center"><center><% if kd.eof then ' Eger veritabanimizda veri yoksa yazi yaziyoruz.%>
<center>Veritabanimizda sayfa yok</center>
<% else ' Yok eger veri varsa %>
<table border="1" width="25%" cellspacing="0" cellpadding="0" bordercolor="#395BCE">
<tr>
<td width="50%" align="center"><b>id</b></td>
<td width="50%" align="center"><b>url</b></td>
</tr><% do while not kd.eof %>
<tr>
<td width="50%"><%=kd("id")%></td>
<td width="50%"><a href="sayfa.asp?no<%=kd("id")%>"><%=kd("url")%></a></td>
</tr><% kd.movenext
loop %>
</table>
</center></div>
<% end if %>
<% kd.close
set kd=nothing
veri.close
set veri=nothing
' Veritabani baglantilarini kapattik.
%>

Bu sayfa ne yapiyor.Veritabaninda kayitli bulunan sayfalari aliyor bunlari bir asp sayfasina yaziyor, siz istediginize tikliyorsunuz ve sayfa.asp araciligi ile o sayfaya ulastiriliyorunuz.Simdi bazi arkadaslarimizin aklina bir soru gelebilir neden direk link vermiyoruzda böyle ugrasiyoruz? Bunun nedeni sizin bu linke kaç kisinin tikladigini ögrenmek olabilir.Veya önce baska bir islem yapiyor olabilirsiniz degil mi? Bu ve bunun gibi durumlarda çok ise yarayan bu uygulamaya devam edelim.

Sirada asil merak edilen islemi yapacak olan **sayfa.asp** adli dosyanin kodlarinda.

| <% sayfa\_no=Request.QueryString("no") ' Hangi sayfayi görmek istiyoruz onu anlayalim. veri\_yol=server.mappath("syf.mdb") ' Veritabaninin yerini belirttik. set veri=server.createobject("adodb.connection") ' Ado'nun Connecion nesnesine ulastik veri.open "DBQ="& veri\_yol &";Driver={Microsoft Access Driver (\*.mdb)}" ' Baglantiyi açtik set kd=server.createobject("adodb.recordset") ' Kayit Dizisine ulastik. sorgu="select \* from Sayfalar where id= "& sayfa\_no &"" ' SQL sorgusu, bu ile Sayfalar tablosunu seçtik ve içinden yollanan sayfa no ile id degeri ayni olanlari aldik. kd.open Sorgu, veri, 1, 3 ' Sonunda Kayit dizisini açtik. ' Artik veriler emrimize amade. %> <% Response.Redirect kd("url") %> |
| --- |

Asil olay bu sayfada oluyor.Ilk önce no adli degiskeni url degiskeni ile aliyoruz ve bunu SQL sorgusunda **where** komutu ile sorguluyoruz.Bizim yolladigimiz **no** adli degiskenin degeri ile veritabanindaki kayitlar arasindan **id** degerleri ayni olanlari seçiyoruz.Genelde böyle uygulamalarda bunlar bir tane esi olur.Sonra **Response** nesnesinin **Redirect** özelligi ile seçilen kaydin **url** alanindaki adrese yollaniyoruz.

**Basit bir tıklama sayacı **

Uzun bir aradan sonra tekrar bir Kısa Uygulama yazısında beraberiz.İnşallah bundan sonra da her hafta düzenli olarak beraber olacağız.Peki bu fahta bilgimizi kullanarak ne yapağız? Yine bir veritabanı uygulaması.

Bu hafta hep beraber bir link yapacağız ve o linke her tıklandığında bir sayaç artacak.Bu basit uygulama için veritabanını kullanacağım çünkü en iyisi o aslında metin dosyası da kullanılabilir.

Şimdi Access'i açın veritabanını **sayac.mdb** adında kaydedip **Sayac** adlı bir tablo oluşturun.Bu tablonun içinde **Tiklama **adlı bir alan oluşturun ve değerini 0 yapın.

Veritabanını hazırladık şimdi sayfaları hazırlayalım.Bize ilk önce tıklamak için link içeren bir asp sayfası lazım bunun için hemen yapalım.Aşağıdaki kodlar **default.asp** adlı sayfamıza ait olsun.Biz bu sayfadan **arttir.asp** sayfasına link vereceğiz ayrıca şimdiye kadar kaç defa tıklamış onu yazacağız

| <% strVt\_Yol=Server.Mappath("sayac.mdb") ' Veritabanın yeri strVtAc= "DBQ="& Server.Mappath("strVt\_Yol") &";Driver={Microsoft Access Driver (\*.mdb)}" Set strVt=Server.CreateObject("Adodb.Connection") strVt.Open strVtAc Set strRs=Server.CreateObject("Adodb.Recordset") strSorgu="Select \* from Sayac" strRs.Open strSorgu, strVtAc, 1, 3 strTiklama=strRs("Tiklama") ' Şu ana kadar tıklama sayısını bir değişkene atıyoruz. strRs.close set strRs=nothing strVt.close strVt=nothing %> <html> <head> <title>Sayac</title> </head> <body> <br><br> <center>Şu ana kadar <b><%=strTiklama%></b></center> <br> <center><a href="arttir.asp">Sayacı arttır</a></center> </body> </html> |
| --- |

Ne kadar kolay değil mi? Veritabanına bağlanıyor ve Tiklama alanındaki veriyi strTiklama adlı değişkene atadık.Madem bunu yaptık sıra sayacı arttırmada. Bu sayfada sayacın değerini bir arttırıp, tekrar **default.asp **'ye geri döneceğiz.Şimdi bu sayfanın kodlarını görelim.

| <% strVt\_Yol=Server.Mappath("sayac.mdb") ' Veritabanın yeri strVtAc= "DBQ="& Server.Mappath("strVt\_Yol") &";Driver={Microsoft Access Driver (\*.mdb)}" Set strVt=Server.CreateObject("Adodb.Connection") strVt.Open strVtAc Set strRs=Server.CreateObject("Adodb.Recordset") strSorgu="Select \* from Sayac" strRs.Open strSorgu, strVtAc, 1, 3 strRs("Tiklama")=strRs("Tiklama")+1 ' Sayacı bir arttırırız. strRs.Update ' Bu kod ile de girdiğimiz veriyi güncelleştiriyoruz strRs.close set strRs=nothing strVt.close strVt=nothing Response.Redirect "default.asp" %> |
| --- |

Bakın bu iki sayfadaki ilk bölümdeki kodlar neredeyse aynı.Sadece tek fark ilk sayfada sadece alanın değerini alıyoruz ama ikinci sayfada bu alanı bir arttırıyoruz.Her halde bu kodlarda bir sorun yoktur.

Email adresi kontrolü

Herhalde hepimizin çok sık yaşadığı bir sorun yapılan formlarda email adresinin doğru yazılmaması.Bazı kullanıcılar bunu bilerek yapıyor bazıları ise hızlı yazmak isterken hata yapıyorlar.

Biz bu hafta bu sorunumuzu halledeceğiz.Yalnız bu doğrulama için Hakkı ÖCAL'ın kitabındaki kodu kullanıcağız.Bunu buradan belirtelim ve devam edelim.

Önce bize email adresini yazacağımız bir form lazım.Hemen hazırlayalım.

| <html> <head> <title>Email Doğrulama</title> </head> <body> <center> <form action="email\_kontrol.asp" method="post"> Lütfen email adresini yazınız : <input type=text name=email> </form> </center> </body> </html> |
| --- |

Sırada da yazılan email adresini kontrol edecek ASP sayfasının kodları var.

mail=Requst.Form("email") ' girilen adresi alalım
<%
Function dogruMu (byval adres)
AtIsareti=0 'sayaç olarak kullanacağımız
Nokta=0 'değişkenleri sıfırlayalım
dogruMu=false 'Fonksiyonun değerini yanlış olarak belirleyelim
KacKarakter=len(adres) 'adresin boyutunu bir değişkene atayalım
For i=1 to KacKarakter 'döngüyü başlatalım
karakter=mid(adres, i, 1) 'sayacın gösterdiği karakteri alalım
if karakter="@" then '@ işareti olup olmadığına bakalım
AtIsareti=AtIsareti + 1 '@ işareti ise sayacı bir arttıralım
End If
if karakter="." Then 'nokta işaretini arayalım
Nokta=Nokta + 1 'nokta ise nokta sayasını bir arttıralım
End if
Next 'bir sonraki karaktere geçelim
If AtIsareti=1 and Nokta >0 Then 'eğer en az bir @ ve nokta olduysa
dogruMu=true 'Fonksiyonun değerini doğru yapalım
End If
End Function
%>

<% if dogruMu(mail) then %>
Yazdığınız email adresi doğru bulundu şimdi devam edebilirsiniz.
<% else %>
Yazdığınız email adresi doğru değil.Lütfen geri dönün ve kontrol edin.
<% end if %>

Yukarıdaki kodlarda kafanız baya karışabilir.Aslında açık bir kod ama email adresini kontrol eden fonksiyon biraz karıştırıyor ortalığı. Bu fonksiyon email adresi içinde @ , . işaretlerinin olup olmadığını kontrol ediyor.Daha sonra biz aşağıda sayfanın başında aldığımız email adresini kontrol ettiriyoruz.Doğru ise bunu belirtiyor değilse uyarıyoruz.

Asp ile Email Yollama

Yaptığınız web sitesinden size mail gelmesi ne kadar güzel değil mi? Maillerinize bakıyorsunuz ve siteden gelen mailleri okuyorsunuz ama siz hala bu işlem için başkalarının scriptlerini veya servislerini mi kullanıyorsunuz? Ne kadar kötü ama bu yazıyı okuduktan sonra kendi scriptinizi kullanacaksınız.

Ben birazdan vereceğim kodlarda email yollamak için CDONTS adındaki ve web sunucularında genelde kullanılan componentı kullandım.Siz isterseniz gerekli satırı değiştirerek kendinize uygun hale getirebilirsiniz.

İlk önce sitemizden ziyaretçilerin görüşlerini yazabileceği bir form olmalı.Onun için aşağıdaki kodları form.html adında kaydedin.

| <html> <head> <title>Mail Yollama</title> </head> <body> <center>Sayın ziyaretçi düşünceleriniz bizim için çok önemli lütfen aşağıya düşüncelerinizi yazıp yollayınız.</center> <br><br> <form name=mailform action=mail\_yolla.asp method=post> <textarea name=mesaj></textarea><br> <input type=submit value="Yolla"> </form> </body> </html> |
| --- |

İşin aslı ise aşağıdaki kodlarda.

| <% strAlacakKisiIsim = "Adınız" strAlacakMail = "mail@adresi.niz" strKimden = " ziyaretci@siteniz.com" strYollayan= "mail@adresi.com" strKimdenIsim = "Ziyaretçi" strBaslik = "Siteden Mail Yollandı" strMesaj = "Merhaba, " & vbCrLf & vbCrLf strMesaj = strMesaj & "Bu mesajı siteden size yolladılar: "& Request.Form("mesaj") & vbCrLf & vbCrLf %> <% Set objYeniMail = Server.CreateObject ("CDONTS.NewMail") objYeniMail.BodyFormat = 1 objYeniMail.MailFormat = 0 on error resume next objYeniMail.Send strYollayan, strAlacakMail, strBaslik, strMesaj If Err <> 0 Then Err\_Msg = Err\_Msg & "<li>İstediğiniz işlem yandaki nedenden dolayı yapılamıyor: " & Err.Description & "</li>" End if on error resume next ' Ignore Errors %> |
| --- |

Evet artık sizde sitenizden kendi yazdığınız kodlarla kullanıcıların size mail atmasını sağlayabilirsiniz.

Tavsiye Ederiz

Arkadaşlar yaşadığımız ayrılıktan sonra tekrar beraberiz.En son Kısa uygulama olarak mail göndermeyi görmüştük ama bazı sorunlar çıkmıştı onun için bu hafta tavsiye etme olayını göreceğiz.

Birçok sitede görmüşsünüzdür bunu arkadaşına tavsiye et diye.İşte bizde onu yapacağız ve arkadaşımıza tavsiye edeceğiz.

Önce bir htm sayfası ile tavsiye arabirimini hazırlayalım.

| <html> <head> <title>Tavsiye</title> </head> <body> <center> <forum name=tavsiye action=tavsiye\_et.asp method=post> <table border=0 cellpadding=0 cellspacing=0> <tr> <td>Adınız:</td> <td><input type=text name=tavsiye\_eden\_ad></td> </tr> <tr> <td>Mail Adresini:</td> <td><input type=text name=tavsiye\_eden\_mail></td> </tr> <tr> <td>Arkadaşınızın Adı:</td> <td><input type=text name=tavsiye\_edilen\_ad></td> </tr> <tr> <td>Arkadaşınızın Mail Adresi:</td> <td><input type=text name=tavsiye\_edilen\_mail></td> </tr> </table> </forum> </center> </body> </html> |
| --- |

Şimdi ise arkadaşınıza mail atacak olan .asp sayfası.

| <% Set Mail=Server.CreateObject("CDONTS.NewMail") Mail.To=Request.Form("tavsiye\_edilen\_mail") Mail.From=Request.Form("tavsiye\_eden\_mail") Mail.Subject="Tavsiye" govde="http://www.maxiasp.com"& chr(10) govde=govde &" Sevgili arkadaşım "& Request.Form("tavsiye\_edilen\_ad") &","& chr(10) govde=govde & " Geçen gün internette dolaşırken bir site buldum çok güzel.Bence sende bir uğra"& chr(10) govde=govde & " Adresi http://www.maxiasp.com "& Chr(10) govde=govde&" "& chr(10) govde=govde &" Sevgili Arkadaşın "& Request.Form("tavsiye\_eden\_ad") &" "& chr(10) Mail.Body=govde Mail.Send Mail.Close Set Mail=Nothing %> Tavsiyeniz yapılmıştır. |
| --- |

HTML Biçiminde Mail

Uzun zamandan sonra tekrar merhaba.Ne zamandan beri ne yazacağımı bulamıyordum buraya ama sonunda bir konu buldum CDONTS ile HTML biçiminde email yollama.

Geçen haftalarda nasıl email yollayacağımızı görmüştük şimdi ise mailimizde HTML kodları kullanacağız.Aşağıdaki kodlar ile belirtilen email adresine web sayfamızın linkini yollayacağız.

| <% Dim Postaci, Govde Set Postaci = Server.CreateObject("CDONTS.NewMail") Postaci.To = "gidecek@email.com" ' Gidecek kişinin email adresi Postaci.From = "yollayan@email.com" ' Yollayan kişinin email adresi Postaci.Subject = "Başlık" ' Başlık Postaci.BodyFormat=0 Postaci.MailFormat=0 Govde = "<h1>Merhabalar</h1>"& Chr(10) Govde = Govde &"<a href='http://benimsitem.com'>Buraya tıklayarak</a> benim siteme gidebilirsiniz."& Chr(10) Postaci.Body = Govde Postaci.Send %> |
| --- |

Burada size yabancı gelen sadece 2 satır var.Bunlar BodyFormat ile MailFormat satırları . İşte bunları 0 yaparak mailiniz içinde HTML kodları kullanabilirsiniz

CDO ile Dosya

Uzun zamandan sonra tekrar merhaba.Ne zamandan beri ne yazacağımı bulamıyordum buraya ama sonunda bir konu buldum CDONTS ile HTML biçiminde email yollamayıp birde buna dosya ekleme...

Geçen haftala nasıl HTML formatında email yollayacağımızı görmüştük şimdi ise mailimize dosya ekleyelim.Aşağıdaki kodlar ile belirtilen email adresine web sayfamızın linkini ve bir txt dosyası yollayacağız.

| <% Dim Postaci, Govde Set Postaci = Server.CreateObject("CDONTS.NewMail") Postaci.To = "gidecek@email.com" ' Gidecek kişinin email adresi Postaci.From = "yollayan@email.com" ' Yollayan kişinin email adresi Postaci.Subject = "Başlık" ' Başlık Postaci.BodyFormat=0 Postaci.MailFormat=0 Postaci.AttachFile Server.MapPath("dosyam.txt") ' Virtual yol 'Postaci.AttachFile ("C:\\inetpub\\wwwroot\\dosyam.txt") ' Gerçek yol Govde = "<h1>Merhabalar</h1><br>" Govde = Govde &"<a href='http://benimsitem.com'>Buraya tıklayarak</a> benim siteme gidebilirsiniz.<br>" Govde = Govde &"Sana bir dosya yolluyorum ekte<br>" Postaci.Body = Govde Postaci.Send %> |
| --- |

Burada size yabancı gelen sadece 1 satır var.Bu AttachFile. Bunlardan ilkinde yol belirtmeden bu dosyanın bulunduğu klasöre göre eklenecek dosyanın yerini tarif ederek yollayabilirsin, 2.de ise siz tam yolu yazarsanız.

ACCESS olmadan Tablo Yaratmak...

Yoğun kullanımda olan bir siteniz var.Birşeyler ekleyeceksiniz ama bu iş için veritabanını indirmek gerekiyor ama siz bu işi yaparken site geçici olarak hizmet dışı kalacak.Peki bunu nasıl aşabiliriz? Yani ASP komutları ile veritabanımıza nasıl tablo ekleriz? İşte bu hafta bu sorunun cevabını alacağız.

Şimdi veritabanim.mdb adında bir veritabanı oluşturun ve içine hiçbir tablo yaratmayın.Sonra aynı klasöre tablom.asp adında aşağıdaki kodları kaydedin...

| <% Set Conn = Server.CreateObject("Adodb.Connection") Conn.Open "DBQ="& Server.Mappath("veritabanim.mdb") &";Driver={Microsoft Access Driver (\*.mdb)}" Set Deneme = Server.Createobject("Adodb.Recordset") dSQL = "Create TABLE Tablom (Metin CHAR(254), Sayi NUMERIC)" Deneme.Open dSQL, Conn, 1, 3 %> <font face="verdana" size="1"><center>Tablonuz yaratıldı</center></font> |
| --- |

Bu kodu çalıştırdığınızda eğer Tablonuz Yaratıldı mesajını alıyorsanız çok güzel tablonuz yaratılmış yok hata alıyorsanız kodları bir kontrol edin...Bu kod ile yaratılan tabloyu açarsanız göreceksiniz ki sadece 2 alan var.Biri Metin adında Metin alanı diğeri Sayi adında Sayı alanı.

Sizde bu yöntem ile istediğiniz gibi alanlar yaratabilirsiniz ama ne yazıkki alan tipi yerine yazacağınız yazı Access teki İngilizce adları değil.Mesela Access'te Metin alanı Text iken burada Char(uzunluk) şeklinde...

Sayfalama

Uzun zamandır MaxiASP'ye konu ekleyemiyordum ama bu hafta o geçen haftaların acısına ekleyeceğim.Bu haftaki Kısa Uygulamamızda çok sorulan sayfalamayı göreceğiz ve çözeceğiz.

Şimdi önce **verilerim.mdb** adında bir veritabanı oluşturun ve bunun içinde **Veriler **diye bir tablo ve bu tablonun da içinde **Ad** ile **Soyad **isminde iki tane alan yaratın.Sonra bu alanlarınızı veri ile doldurun.Yaklaşık 20 kayıt yaparsanız denemeleriniz kolaylaşır.

Veritabanımız hazırsa bir bağlantımızı kuralım...

| <% Dim Baglanti, Db\_Yer, Kayit, bSQL Db\_Yer = Server.Mappath("verilerim.mdb") Set Kayit = Server.Createobject("Adodb.Connection") Kayit.Open "DBQ="& Db\_Yer &";Driver={Microsoft Access Driver (\*.mdb)}" Set Baglanti = Server.CreateObject("Adodb.Recordset") bSQL = "Select \* from Veriler" Baglanti.Open bSQL, Kayit, 1, 3 %> |
| --- |

Artık tablomuza bağlandık.Sıra sıralama olayları için bilgilere geldi.

| <% Dim Kayit\_Sayisi = 10 ' Bir sayfada görünmesini istediğiniz kayıt sayısı Baglanti.PageSize = Kayit\_Sayisi Baglanti.CahceSize = Kayit\_Sayisi If Request.QueryString("Sayfa") = "" Then Gosterilen\_kayit = 1 Else Gosterilen\_kayit = CInt(Request.QueryString("Sayfa")) End If Toplam\_Kayit=Baglanti.PageCount If Gosterilen\_kayit > Toplam\_Kayit Then Gosterilen\_kayit = Toplam\_Kayit If Gosterilen\_kayit < 1 Then Gosterilen\_kayit = 1 If Toplam\_Kayit = 0 Then Response.Write "Kayıt bulunamadı!" Else Baglanti.AbsolutePage = Gosterilen\_kayit end if %> |
| --- |

Rast Gele Veri

Bir kısa uygulama yazacağım zaman genelde forumu dikkate alırım.Çünkü insanlar orada "Şunu nasıl yaparım?" diye sorunca eğer anlatabilirsem anlatmam gerekir diye düşünür ve başlarım yazmaya.Son zamanlarda ise Veritabanından rastgele nasıl veri alırım diye çok sorulmaya başlandı.Bende bunu Kısa Uygulama olarak yazmaya karar verdim.

Şimdi adı **verilerim.mdb** olan, içinde **Veriler** adında bir tablo ve o tablonun içinde de **Yazi **adında bir alan olan bir veritabanımız olsun.Biz öyle bir sayfa hazırlayalım ki bu sayfa her açıldığında veritabanımızdan bir kayıdı seçsin ama rast gele olarak.

| <% Dim Vt, SQL, Rs, gidilecekKayit,ToplamKayit Set Vt = Server.CreateObject("Adodb.Connection") Vt.Open "DBQ="& Server.Mappath("verilerim.mdb") &";Driver={Microsoft Access Driver (\*.mdb)}" Set Rs = Server.CreateObject("Adodb.Recordset") SQL = "Select \* from Veriler" Rs.Open SQL, Vt, 1, 3 %> |
| --- |

Çok güzel bir şekilde veritabanımıza bağlandık ve Recordset nesnemizi açtık.Sıra verileri rast gele almaya geldi.Bu işlem için biraz matematik işlemi yapacağız.Önce tablomuzdaki kayıt sayısını alacağız.Bu sayıyı ASP'nin Randomize fonksiyonu ile kullanıp bir sayı elde edeceğiz.

Renkli Tablolar

Türk milleti için önemli bir gün olan 19 Mayıs ayrıca MaxiASP içinde önemli çünkü yine bir Cumartesi ve yine bir güncelleme günü :)

Bu hafta beraber şu bir gri, bir beyaz tabloları yapacağız.Eğer ne yapacağımızı anlamadı iseniz kodları yazalım ve görelim :)

Bu sefer bir veritabanı oluşturmayalım ama hazır bir veritabanı kullanalım.Adını ve tablo adlarını siz kendinize göre uyarlayınız ben buradan örnek olarak yazacağım.Benim veritabanımın adı **genel.mdb** ve içinde **Verilerim** diye bir tablo var

| <% Set Conn = Server.CreateObject("Adodb.Connection") Conn.Open "DBQ="& Server.Mappath("genel.mdb") &";Driver={Microsoft Access Driver (\*.mdb)}" Set Rs = Server.Createobject("Adodb.Recordset") rSQL = "Select \* from Verilerim" Rs.Open rSQL, Conn, 1, 3 %> <html> <head> <title>Renkli Tablo</title> </head> <body> <center> <table border = "1" bordercolorlight = "silver" bordercolordark = "white" cellspacing = "0"> <% i = 0 Do while Not Rs.Eof if i mod 2 then bgcolor = "#C0C0C0" else bgcolor = "#E9E8FF" end if %> <tr bgcolor='<%=bgcolor%>'> <td><%=Rs("alan1")%></td> <td><%=Rs("alan2")%></td> </tr> <% i = i + 1 Rs.MoveNext Loop %> </table> |
| --- |

Burada karşılaşabileceğiniz tek yabancı kod mod ifadesi.Bu ifade i değişkeninin 2'nin katı olup olmadığına bakmaya yarar.Yaptığı işlemse Lise 1 de öğrendiğimiz Modüler Aritmatiktir.

Başka Sitelerden Bilgi Alma Nasıl Olur?

Günümüzde en çok merak edilen sorulardan biri de başka sitelerden bilgi alma. Ben de bunun hakkında bir yazı yazayım dedim. Aspciler bencil olur derdi birkaç kişi. Gorsunler bencil mi değil mi. Boyle bir script baya para eder. Neyse biz yazımıza bakalım. Bilgi alma işlemi asp ile yapılırken bileşen (component) yardımı ile oluyor. Bu bileşenler ise aspTEAR ve aspHTTP. Ben bu yazımda aspTEAR kullanımı hakkında bilgi ve örnek vereceğim. İlk iş olarak http://www.alphasierrapapa.com/ComponentCenter/AspTear/ adresinden windowsunuzun versiyonuna göre bileşenimizi indirelim. İndirdikten sonra içinden çıkan asptear.dll’i **c:\\tear **adlı bir klasöre kopyalayalım. Bu işlemi yaptıktan sonra başlat – çalıştır – **regsvr32.exe C:\\tear\\asptear.dll **işlemi ile dll’i kayıt edelim. Şimdi geldik kod yazmaya. Ben bu yazımda yabancı bir siteden haber alma işlemini yapacağım. Kodumda açıklamalarda bulundum. İnşallah yardımcı olabilir ve size mantığı anlatabilirim.

Tear.asp kodları:

<%
const Request\_GET = 2
Dim haberURL, haberim, basliklar, kategori

' Ben web developer kategorisini sectim
' Dilerseniz asagıdaki adresten tam listeye ulasabilirsiniz
' http://w.moreover.com/categories/category\_list\_c\_field.html
kategori = "Web%20developer%20news"

haberURL = "http://p.moreover.com/cgi-local/page?c=" & kategori & "&o=pctsv"

' Bilesenimizi hazırlayalım
Set alma = CreateObject("SOFTWING.ASPtear")

On Error Resume Next
haberim = alma.Retrieve(haberURL, Request\_GET, "", "", "")

' Hata durumunda

If Err.Number <> 0 Then
Response.Write "İşlem yürütülürken hata oluştu... "
' Scripti durduralım
Response.End
End If

basliklar = split (haberim, vbTab)

' Baslik turleri
' basliklar(0) => Haberin URLsi
' basliklar(i+1) => Haber Basligi
' basliklar(i+2) => Haber Kaynağı
' basliklar(i+7) => Haber Tarihi ve Saati

for i=0 to ubound (basliklar)-1 step 9
' baslikları yazdıralım

Response.Write "<a href=""" & basliklar(i) & """><b>" & basliklar(i+1) & "</b></a>"
Response.Write "<br>"
Response.Write "<font color=""#CC0000"">" & basliklar(i+2) & "</font> "
Response.Write " (" & basliklar(i+7) & ")"
Response.Write "<p>"
Next

%>

Bir bilgi daha vermek istiyorum. Ntvmsnbc’den aber almak isterseniz su url’i kullanabilirsiniz:

http://www.ntvmsnbc.com/news/BCList2.txt

Frame ile Yönlendirme

NetBul ve Hotmail gibi sitelerdeki url yönlendirmelerini görmüşsünüzdür.Frame kullanılan bir sayfada altta veya üstte açılacak sayfa çıkar diğer bölümde ise sitenin reklamı.Bu sistem MaxiASP'nin reklamlarında da kullanılmaktadır.Şimdi bu işi nasıl yaptığımızı anlatacağız.

|  | Aslında bu işi veritabanı kullanmadan yapmakta mümkün ama ben size kullanılarak nasıl yapıldığını anlatacağım.Her zamanki gibi önce bir veritabanına ihtiyacımız var.Access ile adı **siteler.mdb** olan bir veritabanı yaratın ve içinde **Siteler** adlı bir tablo oluşturun.Bu tablonun içinde de **sno** , **Site\_Url**, **Hit** gibi alanlar olsun. **sno** alanı otomatik sayı, **Site\_Url** metin ve **Hit** alanı da sayı olsun |
| --- | --- |
| Veritabanımız kullanım için hazır olduğuna göre sıra kodlarda.Biz bu iş için 4 sayfa kullanacağız.Bu sayfalardan bir tanesi ayar dosyası olacak, diğeri veritabanındaki linkleri listeletecek. 3.sayfa sizin reklamınızın olduğu sayfa, 4. sayfa ise frame kodlarının olduğu sayfa.Bu sayfaların kodlarını bu sayfalarda bulacaksınız... |  |

Önce ayar dosyası.Her sayfada veritabanımızın yerini teker teker tanıtmaktansa bu çok iyi bir yoldur.Tavsiye ederim.Bu aşağıdaki kodlar **ayar.asp** sayfasına aittir.

| <% Db = Server.Mappath("siteler.mdb") ' Aynı klasörde bütün dosyalar Set Conn = Server.CreateObject("Adodb.Connection") Conn.Open "DBQ="& Db &";Driver={Microsoft Access Driver (\*.mdb)}" %> |
| --- |

Bundan sonra her sayfaya bu kodu ekleyeceğiz.Böylece otomatikman veritabanına bağlanacak.Sıra listelemeyi yapacak sayfada.Bu aşağıdaki kodlarda **default.asp** sayfasına aittir.

| <!-- #include file="ayar.asp" --> <% Set Siteler = Server.CreateObject("Adodb.Recordset") sSQL = "Select \* from Siteler order by Hit desc" ' Hit'i yüksek olanı en başa Siteler.Open sSQL, Conn, 1, 3 %> <html> <head> <title>Linkler</title> </head> <body> <center><font face="verdana" size="1">Aşağıda sitemize kayıtlı linkler mevcuttur.İstediğinizin üstüne tıklayıp gidebilirsiniz.</font></center> <br> <% Do while not Siteler.Eof Response.Write "<a href='site\_yolla.asp?sno="& Siteler("sno") &"' target='\_blank'>"& Siteler("Site\_Url") &"</a><br>" Siteler.MoveNext Loop Siteler.Close Set Siteler = Nothing %> </body> </html> |
| --- |

PAGE

PAGE 1

---
*Kaynak: `Asp'ye giris.Asp nedir/Asp'ye giris.Asp nedir.doc` — OBILGIC — 2004*
