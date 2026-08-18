# HTML Notlari

CSS (Cascading Style Sheets) 30 Ocak 2002

2

Giri¸s CSS Nedir?

Sanaldoku programlamada ¨onemli bir yere sahip CSS kavramı, 1995 yılında W3C (World Wide Web Consortium) tarfından geli¸stirilmi¸stir. O yıllarda ¸cok hızlı bir ¸sekilde geli¸sen HTML kullanımına ¸cok b¨uy¨uk kolaylıklar ge- tirmi¸stir. CSS ile HTML’de yapılması zahmet gerektiren i¸sler, daha basit ¸sekilde yapılabilir.

HTML imleri genel olarak d¨ok¨umanın tarayıc ¨uzerinde nasıl g¨or¨unece˘gini belirler. Renkleri, yazı karakterlerini, resimleri ve daha bir ¸cok veriyi tarayıcı ¨uzerine istedi˘giniz ¸sekilde yerle¸stirebilirsiniz. HTML’in ilk zamanlarında yeter- siz olan buyrukları bu i¸s i¸cin giderek zenginle¸stirilmi¸stir. Sadece resim veya yazı de˘gil, ses ve g¨or¨unt¨u dosyalarını tarayıcı i¸cerisinde g¨or¨unt¨ulemek m¨umk¨un olmu¸stur. Ancak 90’lı yıllarda geli¸simini hızlandıran HTML beraberinde bazı uyumsuzluk hatalarını getirmi¸stir. Bunun ¨uzerinde HTML’i belli standartlara oturmak i¸cin W3C tarafından bazı ¸calı¸smalar ba¸slatılmı¸stır. Buna g¨ore W3C, “recommedation” denilen tavsiye nitele˘gi i¸ceren d¨ok¨umanlar olu¸sturmu¸stur.

Bu d¨ok¨umanlar http://www.w3c.org adresinde yayımlandıktan sonra ta- rayıcı ¨ureticileri tarafından hayata ge¸cirilmeye ba¸slanmı¸stır. B¨oylece d¨unya ¸capında ge¸cerli olan bir HTML standardı olu¸smaya ba¸slamı¸stır.

Bu ba˘glamda HTML kullanımı kolayla¸stıran ve etkin bir ¸sekilde kul- lanılması durumunda belli standartları yakalamayı sa˘glayan CSS g¨undeme gelmi¸stir. Bununla ilgili yine W3C tarafından bazı tavsiyeler yayımlanmı¸stır.

1996 yılında CSS1 olu¸sturulmu¸s, 1998 yılında ise CSS2, CSS1 ¨uzerine otur- tulmu¸stur.

Temel

¨

Ozellikler

˙

Zengin I¸cerik HTML i¸cerisinde kolaylıkla yapılamayacak ¸seyleri CSS kullanarak ¸cok rahat bir ¸sekilde yapabilirsiniz. Mesela, sanaldoku sayfanızda yer alan b¨ut¨un H1

3

4

ba¸slıklarının arka plan rengini, font b¨uy¨ukl¨u˘g¨un¨u ve rengini ayarlamak is- tiyorsunuz. Bunu klasik HTML kuralları ile yapmaya kalkarsanız bir tablo olu¸sturmak zorundasınız. Ayrıca b¨ut¨un sayfalarda bu de˘gi¸siklikleri yapmalı- sınız. Ama CSS kullanarak tek bir satırda bunu halledebilirsiniz.

H1 {color: black; background: yellow; font: italic} Kullanma Kolaylı˘gı CSS genel itibariyle kullanımı kolay bir dildir. HTML’e g¨ore daha kolay olu¸sturulabilecek bir yapıya sahiptir. HTML’de kullanılan < ve > i¸saretlerini CSS i¸cerisinde kullanılmaz. Bu y¨uzden yazma kolaylı˘gı sa˘glanır.

Esneklik Yapılan bir de˘gi¸siklik ile birden fazla web sayfası ile oynayabilirsiniz.

Sadece bir adet dosya ile y¨uzlerce web sayfasının g¨or¨un¨um¨un¨u de˘gi¸stirebi- lirsiniz.

Cascading Cascading kavramı, CSS ile yapılmı¸s tanımlamaların ek bir i¸s yapmaya gerek kalmadan d¨ok¨umanın b¨ut¨un elemanlarını etkilemesini sa˘glar. Bu ¨ozellik ile H1 {color: black; background: yellow; font: italic} ile yaptı˘gınız bir tanım, h1 t¨ur¨undeki b¨ut¨un ba¸slıkları etkiler.

Uygun Dosya Boyutları CSS kullanarak HTML d¨ok¨umanlarının boyutlarını makul seviyelere ¸ce- kebilirsiniz.

CSS ve HTML HTML dosyalarına CSS dosyalarını uygulayabilmek i¸cin CSS dosyasını HTML i¸cerisinden ¸ca˘gırmanız gerekmektedir. Bu i¸s i¸cin <LINK>im’i kullanılır.

<LINK rel="stylesheet" type="text/css" href="stil.css"> Bu t¨ur “stylesheet” dosyalarına “external style sheets” denir. “Stylesheet” dosyalarını ayrıca html d¨ok¨umanı i¸cerisine g¨omebilirsiniz. Ancak bu y¨ontem genellikler tercih edilmez. C¸ ¨unk¨u CSS kullanmanın nedenlerinden biri olan esnekli˘gi zedeler. Bu i¸s i¸cin <STYLE> adlı im kullanılır.

<STYLE type="text/css">

h1 {color: black}

</STYLE>

5

Bu y¨ontemi kullanırken bir ¸seye dikkat etmeniz gerekir. E˘ger eski bir tarayıcı kullanıyor iseniz yukarıdaki satırlar tarayıcı ekranında oldu˘gu gibi g¨or¨unecek- tir. C¸ ¨unk¨u <STYLE>im’i HTML’e yeni eklenen bir ¨ozelliktir. Bu handikapı ¸c¨ozmek i¸cin yukarıdaki kodu a¸sa˘gıdaki ¸sekliyle de˘gi¸stirin.

<STYLE type="text/css"> <!--

h1 {color: black}

--> </STYLE> CSS buyruklarını <!--ve-->imleri i¸cerisine alarak eski tarayıcıların bu buyruk- ları g¨ormemesini sa˘glarsınız.

CSS Yorumları CSS i¸cerisine yorum satırları eklemek i¸cin C dilindeki yapıya benzer ¸sekilde /\*\*/ sembollerini kullanabilirsiniz. h1 {color: black} /\* Bu kısım dikkate alınmaz \*/

6

Genel Yapı Temel Kurallar Yapı CSS i¸cerisinde yapılan b¨ut¨un tanımlar belli bir d¨uzene g¨ore yapılır.

h1 {color: black}

Yukarıdaki tanımda sol tarafta, kuralnın uygulanaca˘gı olan eleman bulunur.

Buna “selector” denir. S¨usl¨u parantezler i¸cerisine : i¸sareti ile ayrılmı¸s olarak bulunan kısım ise tanım b¨ol¨um¨ud¨ur. : i¸saretinin sol tarafı ¨ozelli˘gi belirtir. Sa˘g tarafta ise de˘ger belirtilir. Buna g¨ore “h1” “selector”, color ¨ozellik, black ise de˘ger olarak adlandırabilir.

Basit Se¸ciciler Bir se¸cici genellikler basit HTML imleridir. H1, BODY v.b. Bununlar be- raber bir XML d¨ok¨umanını ¸sekillendirmek i¸cin kullanılan CSS d¨ok¨uman- larında XML i¸cerisinde yer alan imler de bulunaabilir. kitap {color: yellow} gibi. Burada kitapimi normal HTML imlerinde bir de˘gildir.

Tanımlar Biraz ¨once CSS tanımlarının uygulandı˘gı imlerden bahsettik. Peki tanımlar nasıl yapılıyor. Bunun i¸cin : ile ayrılmı¸s bir yapı kullanıyoruz. Sol taraf

¨

¨ozelli˘gi, sa˘g taraf ise de˘geri g¨osteriyor.

Ozelli˘gi ifade etmek i¸cin ¨onceden tanımlı bazı anahtar s¨ozc¨ukler kullanılır.

7

8

body {background: purple} De˘ger olarak ise d¨uzg¨un tanımlı bir veya birden fazla s¨ozc¨uk ardarda kullan- abilirsiniz. body {font: italic Verdana} E˘ger anahtar s¨ozc¨uk yanlı¸s ise yazdı˘gınız buyruk satırı bo¸sa gider. De˘ger olarak yanlı¸s bir ¸sey yazarsanız ise, satır de˘gil sadece ilgili kısım ihmal edile- cektir. Hatta birden fazla de˘ger atanmı¸s ise yanlı¸s olan de˘gerden bir sonraki de˘ger i¸slenecektir. C¸ o˘gu tarayıcı bu gibi hataları tolare edebiliyor. Bu kolaylık ilk ba¸sta g¨uzel g¨or¨unmesine ra˘gmen, programcılara bazı k¨ot¨u alı¸skanlıklar kazandırabilir.

Gruplama Se¸cicileri Gruplama CSS tanımları i¸cerisinde yer alan se¸ciciler gruplar halinde verilebilir. h1,h2,h2 {color: gray} Yukarıdaki ¨ornekte renk ¨ozelli˘gi h1, h2 ve h3 imlerinin hepsine birden kazan- dırılmı¸stır.

¨

Ozellikleri Gruplama Se¸ciciler gruplanabildikleri gibi ¨ozellikler de gruplar halinde tanımlanabilir. p {color: blue; background: grey; font: Verdana; } Her¸seyi Gruplama Bir ¨onceki gruplamalar toplu bir ¸sekilde yapılabilir. h1, h2 {color: yellow; font: Lucida; background: blue;}

9

Sınıf ve ID Se¸cicileri Sınıf Se¸cicileri Sınıf (Class) tanımlarının yapıldı˘gı HTML d¨ok¨umanlarını CSS i¸cerisinde ¸se- killendirebilmek i¸cin kullanılır. Elimizde a¸sa˘gıdaki gibi bir HTML d¨ok¨umanı olsun.

<h1 class="onemli">Onemli Bir Baslik</h2> Sınıfı “onemli” olan imleri CSS i¸cerisinden tanımlayabilmek i¸cin a¸sa˘gıdaki buyru˘gu kullanabiliriz.

.onemli {color: red} Bu sayede HTML i¸cerisinde herhangi bir im “onemli” olarak nitelendirilirse yazı rengi olarak kırmızı kullanılacaktır. Yukarıdaki tanımım yerine h1.onemli {color: red} buyru˘gunu kullansaydık sadece h1 imi bu kurala uyacaktı.

ID Se¸cicileri ID ile Sınıf bir¸cok y¨onden birbirine benzerler ancak arada temel birka¸c fark vardır. Ilk olarak ID tanımlarında #i¸sareti kullanılır. Ayrıca bir HTML d¨o- k¨umanında ID’ler tektir.

<h2 ID="onemli">Onemli Bir Baslik</h2> #onemli {color: red}

10

Birimler Renkler Tanımlı Renkler

˙

Isimleri ile ¸ca˘grılabilecek ve yaygın tarayıcıların destekledi˘gi 16 ana renk vardır. Bu 16 renk Windows i¸sletim sisteminden geliyor. Windows’un ilk zamanlarında VGA monit¨orlerde kullanılabilen renkler bu 16 renk idi. Bu standart 16 renk haricinde bazı tarayıcı’ların tanıdı˘gı renkler de mevcuttur.

Mesela “orange” 16 renk i¸cerisinde olmamasına ra˘gmen bazı tarayıcı’larda kullanabilirsiniz.

RGB Kullanarak Renk Tanımı RGB kelimesi Red, Green ve Blue kelimelerinin ba¸s harflerinde olu¸sturlmu¸stur.

Kırmızı, Ye¸sil ve Mavi renkleri karı¸stırarak b¨ut¨un renkleri ifade etmek m¨um- k¨und¨ur ger¸ce˘gine dayanır. Bu sistemde hangi renkten ne kadar katkı yapılaca˘gı belirlenir ve buna g¨ore renk olu¸sturulur. rgb(100%, 100%, 100%) Yukarıdaki ¨ornekte 3 ana renkten 100%’l¨uk katkılar sa˘glanarak bir renk olu¸sturuluyor. Bu beyaz renge kar¸sılık gelmektedir. A¸sa˘gıdaki ¨ornekte gri rengin tonlarını nasıl elde edebilece˘gimizi g¨or¨uyoruz.

<h1 class="bir">H1 class="bir" tipinde bir ba¸slık<h1> <h1 class="iki">H1 class="iki" tipinde bir ba¸slık<h1> <h1 class="uc">H1 class="uc" tipinde bir ba¸slık<h1> <h1 class="dort">H1 class="dort" tipinde bir ba¸slık<h1> <h1 class="bes">H1 class="bes" tipinde bir ba¸slık<h1> <h1 class="alti">H1 class="alti" tipinde bir ba¸slık<h1>

11

12

h1.bir {color: rgb(0%,0%,0%);} h1.iki {color: rgb(20%,20%,20%);} h1.uc {color: rgb(40%,40%,40%);} h1.dort {color: rgb(60%,60%,60%);} h1.bes {color: rgb(80%,80%,80%);} h1.alti {color: rgb(100%,100%,100%);} Sayılar Kullanarak Renk Tanımı Y¨uzdelik ifade yerine sayı kullanarak da renkleri ifade edebiliriz. Bu sayılar 0 ile 255 rakamları arasında olmak zorundadır. rgb(255,255,255) Yukarıdaki ¨ornekte beyaz reng tanımlanmı¸stır.

Hexadecimal Kullanarak Renk Tanımı Bu y¨ontemde belirli bir renge kar¸sılık gelen hexadecimal sayılar kullanılır. h1 {color: #FFFFFF;} Dikkat etmesi gereken nokta sayıdan ¨once #simgesinin kullanılmasıdır.

Uzunluk Birimleri Mutlak Uzunluk Birimleri •Inches (in) •Santimetre (cm) •Milimetre (mm) •Points (pt) Bu uzunluk birimleri adı ¨uzerinde mutlak uzunluklar belirlerler. Bu y¨uzden sanaldoku tasarımında ¸cok kullanı¸slı de˘gillerdir ¸c¨unk¨u bilgisayardan bilgisa-

¨

yara bir ¸cok ¨ozellik de˘gi¸smektedir.

Ozellikler monit¨orlerin de˘gi¸sik ebatlarda ve ¨ozelliklerde olması bu birimlerin kullanılmasını zorla¸stırmaktır. 14 inch lik bir monit¨orde g¨uzel uygun g¨or¨unen bir resim 17 inch’lik monit¨orde k¨ot¨u g¨o- r¨unebilmektedir.

13

Ba˘gıl Uzunluk Birimleri Bu kavramı bir ¨ornekler a¸cıklayalım. h1 {font-size: 24px;} h1 {margin-left: 1em} Burada ilk ¨once h1 i¸cin 24 piksellik bir font b¨uy¨ukl¨u˘g¨u ¨ong¨ord¨uk. Sonra sol- dan i¸ceriye do˘gru 1em’lik girmesini sa˘gladık. em birimi ¨onceden tanımlanmı¸s font’un b¨uy¨ukl¨u˘g¨une e¸sit olacak ¸sekilde belirlenmi¸stir. Bu durumda h1 soldan i¸ceriye 24 piksel kaydırılacaktır.

Fakat bu a¸samada ince bir nokta devreye giriyor. A¸sa˘gıdaki ¨orne˘gi in- celeyelim.

<p>Bu paragraf i¸cerisinde <small>k¨u¸c¨uk</small> bir kelime var</p> small {font-size: 0.8em} Normalde small imi i¸cerisinde yer alan “k¨u¸c¨uk” kelimesi i¸cerisinde bulundu˘gu c¨umleden %20 oranında k¨u¸c¨uk yazılacaktır. tarayıcılar bu i¸slemi ger¸cekle¸sti- rirken fontun etki ettti˘gi c¨umledeki “x” harfini referans alırlar. Ne yazık ki her font i¸cin “x” harfinin b¨uy¨ukl¨u˘g¨u de˘gi¸sik olacaktır. Bu sebeple “k¨u¸c¨uk” kelimesi her font i¸cin farklı b¨uy¨ukl¨uklerde g¨osterilecektir.

14

Metin

˙

I¸slemleri Hizalama text-indent Yaygın olarak paragrafların ilk c¨umlelerin soldan i¸ceriye kaydırılması i¸cin kullanılan bir ¨ozelliktir. p {text-indent: 1in} text-align 4 tane de˘geri olabilir; left, right, center ve justify. Kolaylıkla anla¸sılabilece˘gi ¸sekilde left sola, right sa˘ga yaslama i¸slemi yapar. center ise yazıyı ortalar. justify ise yazıyı sa˘g ve sol marjinlere uyacak ¸sekilde ayarlar. h1,h2,h3,h4,h5 {text-align: center} buyru˘gu ile b¨ut¨un ba¸slıkların ortalanmasını sa˘glayabilirsiniz. white-space Metnin i¸cerisinde ge¸cen ba¸slukların tarayıcı ¨uzerinde nasıl g¨or¨unt¨ulenec˘gini

¨

belirler.

U¸c farklı de˘geri olabilir; pre,nowrap, normal. Normal se¸cene˘gi ex- tra bo¸slukların ihmal edilmesini sa˘glar. Pre se¸cene˘gi bo¸slukların oldu˘gu gibi g¨or¨unt¨ulenmesini sa˘glar. Nowrap ise metnin satır atlamasını engeller. Satır atlamak i¸cin farklı buyruklar kullanmak zorunda kalırsınız.

<p style="white-space: nowrap;">Bu paragrafın i¸cerisinde "nowrap" se¸ce˘gi kullanılmı¸stır. nowrap metnin boylu boyunca devam etmesini sa˘glar.

<br>Satrı atlamak i¸cin br buyru˘gunu kullanmak zorundasınız.</p>

15

16

Yukarıdaki buyru˘gun tarayıcıda (tarayıcı) elde edece˘gimiz g¨or¨unt¨us¨u a¸sa˘gıdaki gibi olacaktır.

Bu paragrafın i¸cerisinde "nowrap" se¸ce˘gi kullanılmı¸stır. nowrap metnin boylu boyunca devam etmesini sa˘glar.

Satrı atlamak i¸cin br buyru˘gunu kullanmak zorundasınız. word-spacing

¨

Bu ¨ozellik kelimeler arasındaki bo¸slukları belirmeye yarar.

Ornek verelim:

<p style="word-spacing: normal;">Bu paragrafta kelimeler arasındaki bo¸sluk "normal" olarak tanımlanmı¸stır.</p> <p style="word-spacing: 0.5em;">Bu paragrafta kelimeler arasındaki bo¸sluk "0.5em" olarak belirlenmi¸stir.</p>

˙

Ilk ¨ornekte kelimeler arası bo¸sluk normal olarak bırakılacak ama ikinci ¨ornekte bo¸sluk y¨uzde 50 kadar artırılmı¸stır. text-transform D¨ort se¸cene˘gi vardır; uppercase, lowercase, capitalize ve none. Uppercase b¨ut¨un harfleri b¨uy¨uk harfe, lowercase b¨ut¨un harfleri k¨u¸c¨uk harflere, capitalize kelimelerin ilk harflerini b¨uy¨uk harflere ¸cevirir. none ise hi¸cbir ¸sey yapmaz. Fontlar Font Aileleri •Serif •Sans Serif •Monospace •Cursive •Fantasy Yukarıdaki isimler genel font ailelerini tanımlarlar. Serif font ailesindeki font- larda karakterlerin kenarlarında k¨u¸c¨uk s¨usl¨u ¸cıkıntılar vardır. Sans Serif font- larda bu ¸cıkıntılar yoktur. body {font-family: Sans Serif;} Font isimlerini ise a¸sa˘gıdaki gibi belirtebilirsiniz. body {font-family: Sans Serif, Verdana;} Font kullanımına g¨uzel bir ¨ornek verelim. Diyelim ki sayfaların altına imzımızı atmak istiyoruz. Bunun i¸cin bir font belirleyebiliriz. p.imza {font-family: Author99, ScriptTM, cursive; text-align: left;} Bu tanımı yaptıktan sonra HTML i¸cerisinde <p class="imza">Yazar ismi</p> buyru˘gu verildi˘ginde “Yazar ismi” t¨umcesi belirtilen fontta ve sola biti¸sik olarak yazılacaktır.

17

18

font-size Fontun b¨uy¨ukl¨u˘g¨un¨u belirtir. xx-small, x-small, small, medium, large, x- large,xx-large se¸cenekleri vardır.

<p style="font-size: xx-small;">Bu paragraf xx-small boyutunda </p> <p style="font-size: x-small;">Bu paragraf x-small boyutunda </p> <p style="font-size: small;">Bu paragraf small boyutunda </p> <p style="font-size: medium;">Bu paragraf medium boyutunda </p> <p style="font-size: large;">Bu paragraf large boyutunda </p> <p style="font-size: x-large;">Bu paragraf x-large boyutunda </p> <p style="font-size: xx-large;">Bu paragraf xx-large boyutunda </p> Renkler ve Arkaplanlar Renkler Renk tanımlama i¸slemini daha ¨once anlatmı¸stık. Bir ¨ornekle hatırlayalım. body {color:black;} A:link {color: #808080;} A:visited {color: silver;} A:active {color: #333333;} Metinlerin renkleri ayarlanabildi˘gi gibi metni ¸cevreleyen ¸cizgilerin de renkleri CSS iler belirlenebilir. p.cerceve {color: purple; border-style: solid; border-color: black;} Renk tanımımda dikkat edilecek ¨onemli bir nokta vardır. Bir eleman i¸cin renk tanımı yapıldı˘gında o elemanın i¸cerisinde yer alan di˘ger elemanlarda o renk ile g¨osterilecektir. Bu ¨ozelli˘ge “inheritance” denir. Mesela body {color: red;} tanımı yapıldı˘gında aksi belirtilmedi˘gi s¨urece HTML d¨ok¨umanı i¸cerisinde yer alan b¨ut¨un metinlerin kırmızı olmasını zorlarsınız. <body> iminin do˘gal alt ¨uyeleri olan <p><h1>gibi imler <body>iminin ¨ozelliklerini miras alırlar.

Arkaplan Rengi B¨ut¨un elemanlar i¸cin ge¸cerli olmasada ¸co˘g¨u HTML imi i¸cin bir arkaplan rengi belirlenebilir.

19

20

<pre class="alinti">Bu yazi

pre.alinti {background-color: green;}

CSS buyru˘gu ile bi¸cimlendirilmi¸stir.</pre> Yukarıdaki ¨ornekte <pre>imi ve "alinti"sınıfı ile tanımlanan her metinin arkaplan rengini ye¸sil olarak tanımlamı¸s bulunmaktayız.

Arkaplan Resmi Bu ¨ozellikte arkaplan rengi gibi b¨ut¨un elemanlar i¸cin uygulanamaz. Bir ¨ornek verelim. body {background-image: url(meg.jpg)} Burada urlanahtar kelimesi resimlerin yerini belirtmek i¸cin kullanılır. Res- imlerin yerel olarak makinade bulunması gerekmez. Tam URL (Uniform Re- source Locator) kullanarak resim belirtebilirsiniz. body {background-image: url(http://www.w3c.org/background.jpg)} Arkaplan resimleri sadece <body>imi i¸cin kullanılmak zorunda de˘gildir. Bazı HTML imleri i¸cin de kullanabilirsiniz.

<p style="background-image: url(gozler.jpg); background-color: black;">Bu paragrafın arkaplanı olarak bir resim kullanılmı¸stır.

Bunun i¸cin class="alinti">style="background-image: url(gozler.jpg); buyru˘gu kullanılmı¸stır.</p> G¨uzel arkaplan resimleri olu¸sturmak i¸cin CSS’nin sa˘gladı˘gı birka¸c ¨oze- liklen bahsetmekte yarar var. Diyelim ki sanaldoku sayfanızın sol tarafında dikey olarak yerle¸stirilmi¸s bir s¨us istiyorsunuz. bunun i¸cin normalde yap- manız gereken ¸sey y¨uksekli˘gi az ama geni¸sli˘gi fazla olan bir resim dosyayı olu¸sturmak, sonra da bu resim dosyayını <body>imi i¸cerisinde arkaplan resmi olarak g¨ostermenizdir. Sanaldoku tarayıcıları bur resmi dikey olarak uzata- cakları i¸cin resminiz g¨uzel duracaktır. Ancak olu¸sturaca˘gınız resmin sadece sol tafarında bir ¸seyler yer alacak geri kalan b¨uy¨uk kısım bo¸sluktan olu¸sacaktır.

21

bu etkiyi yaratmak i¸cin CSS’nin ¨ong¨ord¨u˘g¨u metod ¸cok basit. Sol tarafa koymayı istedi˘giniz resmi normal boyutları ile ele almak ve resmi dikey do˘grultuda tekrarlamasını sa˘glamak. Bunu yapmak i¸cin background-repeat ¨ozelli˘gi kullanılır. 4 de˘ger alabilir; repeat, repeat-x, repeat-y ve none. Tah- min etti˘giniz gibi repeatde˘geri resmin dikey ve yatay do˘grultularda tekrar- lanmasını sa˘glar. repeat-xyatay do˘grultuda, repeat-yise dikey do˘grultuda aynı i¸si yapar. noneise resmi oldu˘gu gibi bırakır. Bir ¨ornek verelim.

body {background-image: url(button.png);

background-repeat: repeat;

font-family: Sans Serif, Garamond;}

Yukarıda anlatılan ¨ozelliklere ek olarak background-attachment¨ozelli˘gi bah-

˙

sedilebilir.

Iki de˘geri vardır; scroll ve fixed. scroll se¸cene˘gi arkaplanın metinler kaydırıldı˘gında onlarla beraber hareket etmesini sa˘glar. fixed ise arkaplanın sabit kalmasını sa˘glar.

body {background-image: url(button.png);

background-repeat: repeat; background-attachment: fixed;

font-family: Sans Serif, Garamond;}

22

¨

Ornek sample.css

body {background-image: url(button.png);

background-repeat: repeat-y; background-attachment: fixed;

font-family: Sans Serif, Garamond;}

// Tanimli Renkler p.aqua {color: aqua} p.black {color: black} p.blue {color: blue} p.fuchsia {color: fuchsia} p.gray {color: gray} p.green {color: green} p.lime {color: lime} p.maroon {color: maroon} p.navy {color: navy} p.olive {color: olive} p.purple {color: purple} p.red {color: red} p.silver {color: silver} p.teal {color: teal} p.white {color: white} p.yellow {color: yellow} h1.bir {color: rgb(0%,0%,0%);} h1.iki {color: rgb(20%,20%,20%);} h1.uc {color: rgb(40%,40%,40%);} h1.dort {color: rgb(60%,60%,60%);} h1.bes {color: rgb(80%,80%,80%);}

23

24

h1.alti {color: rgb(100%,100%,100%);} p.sol {text-indent: -30px;} p.sola {text-align: left;} p.saga {text-align: right;} p.ortala {text-align: center;} p.ayarla {text-align: justify;} p.imza {font-family: Author99, ScriptTM, cursive; text-align: left;} p.cerceve {color: purple; border-style: solid; border-color: black;}

pre.alinti {background-color: green;}

sample.html <html> <head > <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-9">

¨

<title>CSS Ornek Sayfası</title> <link rel="stylesheet" type="text/css" href="sample.css"> </head> <body> <h1 class="bir">H1 class="bir" tipinde bir ba¸slık<h1> <h1 class="iki">H1 class="iki" tipinde bir ba¸slık<h1> <h1 class="uc">H1 class="uc" tipinde bir ba¸slık<h1> <h1 class="dort">H1 class="dort" tipinde bir ba¸slık<h1> <h1 class="bes">H1 class="bes" tipinde bir ba¸slık<h1> <h1 class="alti">H1 class="alti" tipinde bir ba¸slık<h1> <p class="aqua">AQUA </p> <p class="black">BLACK </p> <p class="blue">BLUE </p> <p class="fuchsia">FUCHSIA </p> <p class="gray">GRAY </p> <p class="green">GREEN </p> <p class="lime">LIME </p> <p class="maroon">MAROON </p> <p class="navy">NAVY </p>

25

<p class="olive">OLIVE </p> <p class="purple">PURPLE </p> <p class="red">RED </p> <p class="silver">SILVER </p> <p class="teal">TEAL </p> <p class="white">WHITE </p> <p class="yellow">YELLOW </p> <p class="sol"><img src="gozler.jpg" width="160px" height="60px" align="left">Bu paragrafın ilk c¨umlesi sol tarafa do˘gru 2 inch kadar itilmi¸stir. Yazının rengi neden mavi? Bunu da siz bulun. </p> <p class="sola">Bu paragraf sola dogru yaslanmı¸stır.

Bu paragraf sola dogru yaslanmı¸stır.

Bu paragraf sola dogru yaslanmı¸stır.

Bu paragraf sola dogru yaslanmı¸stır.</p> <p class="saga">Bu paragraf saga dogru yaslanmı¸stır.

Bu paragraf saga dogru yaslanmı¸stır.

Bu paragraf saga dogru yaslanmı¸stır.

Bu paragraf saga dogru yaslanmı¸stır.</p> <p class="ortala">Bu paragraf ortalanmı¸stır.

Bu paragraf ortalanmı¸stır.

Bu paragraf ortalanmı¸stır.

Bu paragraf ortalanmı¸stır.</p> <p class="ayarla">Bu paragraf sa˘ga ve sola do˘gru ayarlanmı¸stır.

Bu paragraf sa˘ga ve sola do˘gru ayarlanmı¸stır.

Bu paragraf sa˘ga ve sola do˘gru ayarlanmı¸stır.

Bu paragraf sa˘ga ve sola do˘gru ayarlanmı¸stır.</p> <p style="white-space: nowrap;">Bu paragrafın i¸cerisinde "nowrap" se¸ce˘gi kullanılmı¸stır. nowrap metnin boylu boyunca devam etmesini sa˘glar.

<br>Satrı atlamak i¸cin br buyru˘gunu kullanmak zorundasınız.</p> <p style="word-spacing: normal;">Bu paragrafta kelimeler arasındaki bo¸sluk "normal" olarak tanımlanmı¸stır.</p>

26

<p style="word-spacing: 0.5em;">Bu paragrafta kelimeler arasındaki bo¸sluk "0.5em" olarak belirlenmi¸stir.</p> <p style="font-family: Sans Serif;"> Bu paragraf Sans Serif font ailesi ile yazılmı¸stır. </p> <p style="font-size: xx-small;">Bu paragraf xx-small boyutunda yazıldı</p> <p style="font-size: x-small;">Bu paragraf x-small boyutunda yazıldı</p> <p style="font-size: small;">Bu paragraf small boyutunda yazıldı</p> <p style="font-size: medium;">Bu paragraf medium boyutunda yazıldı</p> <p style="font-size: large;">Bu paragraf large boyutunda yazıldı</p> <p style="font-size: x-large;">Bu paragraf x-large boyutunda yazıldı</p> <p style="font-size: xx-large;">Bu paragraf xx-large boyutunda yazıldı</p> <p class="cerceve">Bu paragraf p.cerceve {color: purple; border-style: solid; border-color: black;} CSS buyru˘gu ile bi¸cimlendirilmi¸stir. </p> <p class="imza">Yazar ismi</p> <pre class="alinti">Bu yazi

pre.alinti {background-color: green;}

CSS buyru˘gu ile bi¸cimlendirilmi¸stir.</pre> <p style="background-image: url(gozler.jpg); background-color: black;">Bu paragrafın arkaplanı olarak bir resim kullanılmı¸stır.

Bunun i¸cin class="alinti">style="background-image: url(gozler.jpg); buyru˘gu kullanılmı¸stır.</p> <p style="background-image: url(button2.png); background-repeat; repeat; background-attachment: fixed;">

style="background-image: url(button.png); background-repeat; repeat;

style="background-image: url(button.png); background-repeat; repeat;

style="background-image: url(button.png); background-repeat; repeat;

</p> </body> </html>

27

28

Kaynak¸ca \[1\] Cascading Style Sheets, The Definitive Guide, Eric A. Meyer , O’Reiily Assoc., 1999

29

---
*Kaynak: `HTML NOTLARI/html notları/css-2.pdf`*
