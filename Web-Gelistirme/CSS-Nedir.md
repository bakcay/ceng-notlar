# CSS Nedir

**CSS Nedir?**

Css’in açılımı ile söze başlayalım. Cascading Style Sheets. Biz kısaca konularımız dahilinde Stil Şablon olarak bahsedeceğiz. Gelelim Stil Şablonun varoluş amacına. Sizinde bildiğiniz üzere Html yazım şekli olarak etiket türünde bir yazım dili. Bu yüzden pek fazla özelliklere sahip değil. Bu sahip olamadığı özellikler nedeniyle sayfanın dizaynında bize tam esneklik veremiyor. Css bu amaçla üretilmiş bir dil. Kullanım kolaylığı ve kullanışlılığı ile Html’e eklenmesinden itibaren çoğu web tasarımcısının gözdesi oldu. Çünkü her türlü sayfa dizaynını bize bırakarak müthiş bir esneklik sağlıyor. Ayrıca ileriki konularımızda bahsedeceğimiz üzere bağlantılı stil şablonlar aracılığı ile de birden çok sayfaya etkiyebiliyor. Bu da bize sitenin görünümün değiştirmek istediğimizde elimizdeki onlarca belki de yüzlerce sayfanın kodlarını değiştirmeden sadece css dosyasının değiştirerek bu imkanı sağlıyor.

Stil Şablon’un tarayıcılara eklenmesinden sonra iki versiyonu çıktı. Bunlar Css 1 ve Css 2. Ayrıca bazı konularda MSIE (Internet Explorer) ve NN (Netscape Navigator) tarayıcıları aynı kodları kabul etmiyorlar. Biz derslerimizde her iki tarayıcıda da etkin olan veya etkin olmayıp dizaynı bozmayan (A:hover gibi) Stil Şablon özelliklerini göreceğiz. Şimdi derslerin içeriğinde neler var onları görelim :

**1. Stil Şablon çeşitleri :**

Css’in en çok beğenilen yönü istendiğinde sadece bir öğeye etkimesi, istendiğinde tüm sayfaya etkimesi, istendiğinde site içindeki tüm html dosyalarına etkimesidir. Bunlar kısaca Stil Şablonun kullanım çeşitleridir.

**2. Html etiketleri ile Css :**

Bu dersimizde Html’deki font,background gibi çeşitli özelliklerin Stil Şablon tarafından nasıl belirlenebileceğini göreceğiz.

**3. Seçiciler (Selectors) :**

Kimi zaman Html etiketlerinden fontu hepimiz kullanırız. Örneğin bir sayfa içerisinde font etiketine birden çok görünüm eklemek isteriz. Bu durumda seçiciler imdadımıza yetişir. Bu dersimizde de seçicilerin nasıl kullanıldığını ve yazım kurallarını öğrenceğiz.

**4. Genel kullanım şekilleri :**

Bu dersimizde ise A (link) etiketinin çeşitli kullanım biçimleri ile birlikte bir Stil Şablonun nasıl kullanırsak işimize daha fazla yarayacağını göreceğiz. Siz buradaki kullanım tarzına göre Css’i kullanırken kendinize nasıl bir yön izleyeceğinize karar vereceksiniz.

**CSS Çeşitleri**

Css’in (Stil Şablonu) 3 farklı kullanım alanı vardır. Bunlar ;

**Yerel, yani sayfada sadece bir kez:** Yerel stil şablonlar bir html etiketi için özel olarak kullanılırlar.

**Global, yani tüm sayfa için:** Global stil şablonlar sayfadaki tüm html etiketlerinin belirlenen özellikte olması istendiğinde kullanılırlar.

**Bağlantılı, yani birden çok sayfa için:** Bağlantılı stil şablonlar birçok sayfada aynı biçimde olması istendiğinde kullanılırlar.

**2.1 Yerel Stil Şablonu**

Başlangıçta belirttiğimiz gibi Yerel Stil Şablonlar, uygulanacak etiketi sadece bir kez bulunduğu yerde (yerel) etkiler. Şimdi bir örnek verelim.

| PRIVATE<html> <head> <title>Css</title> </head> <body> <h2>Web Teknikleri</h2><br> <h2 style="font-size:20pt; color:blue">Web Teknikleri</h2> </body> </html> |
| --- |

Bu örneğimizi **css.htm** adıyla kaydedip tarayıcı yardımıyla açtığımızda iki tane Web Teknikleri yazısıyla karşılacağız. Fakat bunların yazım tarzı farklı olacak. Çünkü biz ikinci **<h2>** etiketimize etkimek üzere bir stil şablon ekledik.

**2.2 Global Stil Şablonu**

Global Stil Şablonları bir önceki örnekte yaptığımız **<h2>** etiketinin tüm sayfada aynı özellikte olması istendiğinde kullanılır. Bunu için Stil Şablon özellikleri sayfanın başlangıcında (**<head></head>** etiketleri arasında) tanımlanmalıdır.

Örnek ile biraz daha ayrıntılı inceleyelim.

| PRIVATE<html> <head> <title>Css</title> <style type="text/css"> <!-- h2 {font-size:20pt; color:blue} --> </style> </head> <body> <h2>Web Teknikleri</h2> </body> </html> |
| --- |

Burada ne yapmış olduk? Sayfa içerisinde kullanacağımız tüm **<h2>** etiketlerinin özelliklerini sabitlemiş olduk. Yani sayfa içerisinde nerede kullanırsanız kullanın **<h2>** etiketinin stil özellikleri hep aynı olacaktır. Yazım kurallarına biraz değinirsek, Stil Şablon tanımlamaları **<head> </head>** etiketleri arasında **<style type="text/css">** ile başlayıp **</style>** ile bitmelidir. **<!--** etiketi ile Css’den anlamayan tarayıcıların bu kısmı geçmesini sağlıyoruz. Bu saklama işlemi **-->** etiketi ile son bulur.

**2.3 Bağlantılı Stil Şablon**

Global stil şablonu ise sitemiz içerisindeki tüm sayfalarda aynı stil özelliklerini kullanmak istediğimizde kullanırız.

Her zaman olduğu gibi stillerimizi yukarıda örneklerini verdiğimiz şekilde hazırlarız. Fakat bunu html dosyamızın içerisinde değil de boş bir sayfaya yazarız. Sonra onu kaydederken **css** uzantılı bir şekilde kaydederiz. Ardından da html dosyamızın içerisine yine **<head> </head> **etiketleri arasına**
<link rel="stylesheet" type="text/css" href="dosya\_ismi.css">**
şeklinde ekleriz. Şimdi hemen bir örnek verelim.

| PRIVATEh1 {font-size:13pt; color:green} h2 {font:20pt; color:blue} h3 {font-size:15pt; color:red} |
| --- |

Bu dosyamızı **stil.css** olarak kaydedelim. Şimdi de html dosyamıza gelelim. Html dosyamızın kodları da şu şekilde olmalıdır.

| PRIVATE<html> <head> <title>Css</title> <link rel="stylesheet" type="text/css" href="stil.css"> </head> <body> <h1>Web Teknikleri</h2> <h2>Web Teknikleri</h2> <h3>Web Teknikleri</h2> </body> </html> |
| --- |

Html dosyasının kodları arasında geçen **<link rel="stylesheet" type="text/css" href="stil.css">** kodu **stil.css** dosyasındaki stil özelliklerini kullanmamızı sağlar. Bu kodu istediğimiz diğer html dosyalarına da eklediğimizde orada da kullanabiliriz.

Böylelikle her sayfada stil özellikleri tanımlamamış, başlangıçta tanımladığımız stil özelliklerini kullanarak hem koddan tasarruf etmiş oluruz hem de paradan :)

**HTML etiketleri ile CSS**

Biz bundan sonraki tüm Stil Şablon örneklerimizde Global Stil Şablonu kullanacağız. Bu yüzden Css ile Html dosyalarımız beraber olacak böylece de konuyu kavrama ve anında uygulamanız daha kolay olacak. Şimdi Css’in etkidiği Html etiketlerini hangi özelliklerini değiştirdiğini görelim.

**3.1. Font Özellikleri**

Adı üzerinde Font özelliklerini değiştirmeye yarayan bir stil şablon özelliğidir. Nasıl kullanıldığına hemen bir bakalım.

| PRIVATE<html> <body> <head> <title>Css</title> <style type="text/css"> <!-- p { font-size : 12pt; font-family : Arial; font-weight : bold; font-style : italic; color : #00FFFF; } --> </style> <body> <p>Web Teknikleri</p> </body> </html> |
| --- |

Alt özellikleri tanıyalım.

**font-size :** Font büyüklüğünü belirtir.
İsterseniz aşağıdaki gibi standart değerleri seçersiniz;

xx-large (en büyük )
x-large (biraz büyük)
large (büyük)
medium (orta)
small (küçük)
x-small (biraz küçük)
xx-small (en küçük)

isterseniz direkt olarak punto (pt) değerini verebilirsiniz.

**font-family :** Font tipini belirler.

Arial, Courier, Verdana gibi font isimlerini alabilir.

**font-weight :** Fontun kalınlı incelik durumunu belirler.

bold : Fontu kalın yapar. normal : Fontun normal halde olmasını sağlar.

Bu özellik yazılmadığında normal özellik alınır.

**font-style :** Fontun yatık olup olmamasını sağlar.

italic : Yazının sağa doğru yatık olmasını sağlar. normal : Fontu normal halde olmasını sağlar.

Bu özellik yazılmadığında normal özellik alınır.

**color :** Fontun rengini belirler.

Blue, red,green gibi renklerin ingilizce karşılıklarını alabilir.

**3.2 Text Özellikleri**

Text özelliği ile de font özelliğinin sahip olmadığı bazı özellikleri etiketimize ekleriz. Örnek ile açıklayalım.

| PRIVATE<html> <body> <head> <title>Css</title> <style type="text/css"> <!-- p { text-transform **:** lowercase; text-decoration **:** underline; text-align **:** left; line-height **:** 20px; text-indent **:** 15px; } --> </style> <body> <p>Web Teknikleri</p> </body> </html> |
| --- |

Alt özellikleri tanıyalım.

**text-transform : ******

lowercase : Yazının tümünün küçük harf olmasını sağlar.
uppercase : Yazının tümünün büyük harf olmasını sağlar.
capitalize : Yazının istenilen şekilde kalmasını sağlar.

**text-decoration :**

underline : Yazının altının çizili olmasını sağlar.
overline : Yazının üstünün çizili olmasının sağlar.
line-through : Yazının üstünün çizili olmasını sağlar.
none : Yazının herhangi bir yerine çizgi çekilmemesini sağlar.

**text-align:**

left: Yazının sola bitişik olmasını sağlar.
center : Yazının ortada olmasının sağlar.
right : Yazının sağa bitişik olmasını sağlar.
line-height :Yazının normal satırdan çizgi yüksekliğini belirler. 3px, 5px gibi değerler alır.
text-ident : Yazının soldan ne kadar boşlukla içeriden başlayacağını belirler. 5px, 10px gibi değerler alır.

**3.3 Background Özellikleri**

Background ile html sayfamızın arkafonlarının özelliklerini değiştirmemizi sağlar.

| PRIVATE<html> <body> <head> <title>Css</title> <style type="text/css"> <!-- p { background-color :#00ff00; background-image : url ("resim\_adi.gif"); background-position : center; background-repeat : repeat-y; } --> </style> <body> <p>Web Teknikleri</p> </body> </html> |
| --- |

**background-color : **Arka fonun rengini belirler. Css’te renkleri blue, red gibi tanımlayabileceğimiz gibi Html kodunu vererek de tanımlayabiliriz.

**background-image : **Arka fonu bir resim dosyası yapmak için kullanılır. url etiketinin içine resim dosyasının yolu ve ismi tam olarak yazılmalıdır.

**background-position :**

left : Arka fondaki resmin sadece sol tarafta olmasını sağlar.
center : Arka fondaki resmin sadece sol tarafta olmasını sağlar.
right : Arka fondaki resmin sadece sol tarafta olmasını sağlar.

**background-repeat : **Arkafondaki resmin tekrarlanması istendiğinde kullanılır.

repeat : Tüm yönlerde tekrar edilmesini sağlar.
repeat-x : X (yatay) yönünde tekrar edilmesini sağlar.
repeat-y : Y (dikey) yönünde tekrar edilmesini sağlar.
no-repeat : Resmin tekrar edilmeyerek bir kere gösterilmesini sağlar.

**3.4 List Özellikleri**

Bu Css özelliği **<ul>** ve **<li>** html etiketleri ile oluşturduğumuz listelerin özelliklerini belirlemek için kullanılır.

| PRIVATE<html> <body> <head> <title>Css</title> <style type="text/css"> <!-- li { list-style-type : circle; list-style-position : inside; list-style : decimal; list-style-image : url ("resim.gif"); } --> </style> <body> <ul> <li>Web Teknikleri <li>Html <li>Javascript <li>Css <li>Web Grafik </ul> </body> </html> |
| --- |

**list-style-type :**

disk : Liste biçiminin disk (içi dolu yuvarlak) şeklinde olmasını sağlar. circle : Liste biçiminin çember şeklinde olmasını sağlar. square : Liste biçiminin kare olmasını sağlar. decimal : Liste biçiminin rakamlardan oluşmasını sağlar.

**lower-roman : **Liste biçiminin i,ii,iii, gibi roma rakamlarının küçük harfi olmasını sağlar.

upper-roman: Liste biçiminin I,II,II gibi roma rakamlarının büyük harfi olmasını sağlar. lower-alpha : Liste biçiminin a,b,c şeklinde olmasını sağlar. upper-alpha: Liste biçiminin A,B,C şeklinde olmasını sağlar. none : Listenin imgesiz olmasını sağlar.

**list-style-position :**

inside : Listenin ikinci satırının en soldan başlamasını sağlar. Outside : Listenin ikinci satırının ilk satır ile aynı yerden başlamasını sağlar.

**list-style-image :** Liste biçiminin resim olmasını sağlar.

**3.5 Position Özelliği **

Html’de kullandığımız Layer (katman) etiketlerinin html üzerindeki yerleştirme işlemi için kullanılır. Hemen bir örnek ile görelim.

| PRIVATE<html> <head> <title>Css</title> <style type="text/css"> <!-- div { position:absolute; top:20px; left:10px; width:200px; height:200px; clip:auto; overflow:scroll; z-index:auto; visibility:visible; } --> </style> <body> <div> Web Teknikleri<br> Html<br> Javascript<br> Css<br> Grafik<br> </div> <p> Web Teknikleri </body> </html> |
| --- |

**position :**

absolute : Katmanın yerinin kesin olarak belirlenmek istendiğinde kullanılır.
relative : Katmanın yerinin göreli(diğer öğelere göre değişebilen) olarak belirlenmek istendiğinde kullanılır.
static : Katmanın yerinin sabit olarak belirlenmek istendiğinde kullanılır.

top : Katmanın üst kısımdan kaç piksel aşağıda olması gerektiğini belirler.

left : Katmanın sol kısımdan kaç piksel aşağıda olması gerektiğini belirler.

width : Katmanın genişliğinin kaç piksel olacağını belirler.

height : Katmanın boyunun kaç piksel olacağını belirler.

clip : Katmanın görünmesi istenen bölgeyi içeren kutucuk.

overflow : Katmanın belirtilen yükseklik ve genişliğe sığmayan kısmına ne olacağını belirler.
auto : Otomatik olarak belirlenir.

scroll : Kaydırma çubukları ekler.

visibility : Katmanın görünebilirlik ayarı yapar
visible : Görünür hale getirir.
hidden : Gizler.

z-index : Katmanın sayfa üzerindeki sıra sayısı.

**Seçiciler (Selectors)**

Css’te seçiciler en çok kullanılan öğelerdendir. Örneğin **<h1>** etiketine Css yardımıyla belli bir şablon yüklediniz. Ama sayfanızda kullanacağınız **<h1>** etiketlerinin tümünün aynı şekilde olmasını istemiyorsunuz. Bu durumda bize seçiciler yardımcı olur.

İki çeşit seçici göreceğiz. Bunlar :

Id Selector (Id seçicisi)

Class Selector (Sınıf Seçicisi)

**4.1 Class Selector (Sınıf Seçicisi)**

Bu seçiciyi sayfanızdaki **<h1>** gibi etiketlerin tümünün aynı olmasını istemediğiniz durumlarda kullanırız. Böylelikle genel bazı özellikleri koruyarak farklı özellikleri özelleştirebilirsiniz. Sınıf seçicisinin iki türü vardır. İlk önce birinci şeklini görelim. Hemen bir örnekle bu seçiciyi tanıyalım.

| PRIVATE<html> <head> <title>Css</title> <style type="text/css"> <!- h1.mavi {color:blue} h1.kirmizi {color:red} --> </style> </head> <body> <h1 class=mavi>Mavi sınıf seçicisi ile </h1><br> <h1 class=kirmizi>Kırmızı sınıf seçicisi ile </h1> </body> </html> |
| --- |

Burada sınıf seçicisini sadece **<h1>** için tanımladık. Sınıf seçicisinin ikinci türü de genel bir sınıf seçicisi tanımlamaktır. Bunu da bir örnekle görelim.

| PRIVATE<html> <head> <title>Css</title> <style type="text/css"> <!- .mavi {color:blue} .kirmizi {color:red} --> </style> </head> <body> <h3 class=mavi>Mavi sınıf seçicisi ile </h1><br> <h4 class=kirmizi>Kırmızı sınıf seçicisi ile </h1> </body> </html> |
| --- |

**4.2 Id Selector (Id Seçicisi)**

Id Selector’lerini tanımlayıcı adlarının önündeki # işaretinden tanırız. Html belgesinde kendi tanımlayıcı adlarına gönderme yaparak herhangi bir Html etiketine stil vermekte kullanılırlar. Bu etiketler span’dan tutunda paragraf(p)’a kadar olabilir. Bir örnekle açıklayalım.

| PRIVATE<html> <head> <title>Css</title> <style type="text/css"> <!-- Eski tür tarayıcılardan kodumuzu saklayalım --> #mavi { background:blue; color:white; } #yesil { background:green; color:white; } --> </style> </head> <body> <span id=mavi>Bu yazının arkafon rengi mavi font rengi beyaz</span><br><br> <span id=yesil>Bu yazının arkafon rengi yeşil font rengi beyaz</span> </body> </html> |
| --- |

**Genel kullanımı**

Css’i Html üzerinde kullanmak için 3 yöntem (yerel-global-bağlantılı) olduğunu daha önce belirtmiştik. Şimdi ise komple bir css dosyasını Html üzerinde nasıl kullanacağımız görelim. Fakat öncelikle Html’deki **<a>** etiketinin diğer etiketlerden farklı olarak bir kullanım tarzı bulunmakta. İlk önce ona değinelim.

**A etiketinin Css ile kullanımı **

Bildiğiniz üzere **<a>** etiketi Html’e çok büyük bir özellik katan link etiketidir. Bu etiket ile diğer bir web sayfasına veya bir mail adresine gönderme yapabiliriz. Bu etiketin belli durumlarda aldığı değişik değerler vardır. Yani link tıklandığında etiket artık visited (ziyaret edilmiş) pozisyonuna geçecektir. Biz Css yardımıyla **<a>** etiketinin aldığı posizyonlara istediğimiz biçimi verebiliriz. Şimdi **<a>** etiketinin aldığı pozisyonları görelim :

İlk poziyon linke herhangi bir tıklama olmadığındadır. Bu değer linkin sayfada görülecek ilk halidir.

Visited : Bu pozisyon link tıklandığından sonra etiketin aldığı değerdir. Active : Bu pozisyon linkin aktif olduğu durumdur. Yani imleç linkin tıklandığı andaki durumdur. Hover : Bu pozisyon Linkin üzerine gelindiği durumdur. Yani linkin üzerine gelindiğinde nasıl bir biçimde olması isteniyorsa stil o şekilde verilir.

Şimdi **<a>** etiketi için bir stil dosyası yapalım.

| PRIVATE<html> <head> <title>Css</title> <style type="text/css"> <!- A.normal { background-color:white; color:blue; } A.ziyaret:visited { background-color:white; color:maroon; font-weight:normal; } A.aktif:active { background-color:white; color:red; font-weight:normal; } A.degisken:hover { background-color:blue; color:white; font-weight:bold; } --> </style> </head> <body> <a href="#" class="normal">Linkin normal durumu</a><br> <a href="#" class="ziyaret">Linki tıklayın ve değiştiğini görün</a><br> <a href="#" class="aktif">Linkin aktif durumu</a><br> <a href="#" class="degisken">Linkin üzerine geldiğinde stil değişecek</a><br> </body> </html> |
| --- |

Şimdi **<a>** etiketinin özel durumunu da gördükten sonra esaslı bir css kullanma tekniğini görelim. Bu örneğimizde **<div>**, **<table>**, **<span>**, **<h1>**...**<h6>**, **<p>**, **<a>** gibi Html etiketlerini kullanırken nasıl bir yöntem izlememiz gerektiğini göreceğiz.

İlk öncelikle stillerimiz hem bağlantılı hem global hem de yerel kullanacağız. Bunu belirteyim. Böylelikle sizde nasıl bir yol izlemenize karar verin.

Şimdi bağlantılı css dosyamızı hazırlayalım. Hatırlayacağınız üzere bu dosyanın uzantısı css olmalı. Bu css dosyasını Html dosyamızın içerisinde çağıracağız. Aşağıdaki kodları **stil.css** adıyla kaydedelim.

| PRIVATEA {font-style : normal; color : navy; font-family : Times New Roman ! important; text-decoration : none; <!-- bu satır linkin altında satır olmamasını sağlar -->} A:Visited {font-family : Times New Roman ! important; font-style : italic; color : olive; } A:Active { font-family : Times New Roman; color : red;} A:Hover {text-decoration : underline; font-family : Times New Roman ! important; font-weight : bold; font-style : normal; color : maroon;} BODY { background: white url("fon.gif"); background-repeat: repeat-y; background-position: left; } p#sol {position : relative; visibility : visible; left : 30pt; width : 450pt; font-family:"Verdana,Arial,Helvetica" ! important; font:15pt;} |
| --- |

Aşağıdaki kodları da **css.html** adıyla kaydedelim. (Dikkat ! html uzantlı kaydedin )

PRIVATE<html>
<head>
<title>Css</title>
<style type="text/css">
<!--
.onemli {font-weight:bold;}
h4 {color:blue;
position : relative;
visibility : visible;
left : 25pt;
font-size:large;
.solic { color:brown;
font-family:"Verdana,Arial,Helvetica";
position : relative;
visibility : visible;
left : 20pt;
font-weight:bold; }
li { list-style-type : circle;
list-style-position : inside;
list-style : decimal;}
; -->
</style>
<link rel=stylesheet href="stil.css" type="text/css">
</head>
<body>
<table width="500" align="center">
<tr><td> <!-- Global -->
<h4>Bilgisayar;<a name="bsl">&nbsp;&nbsp;</a></h4>
<!-- Eğer koordinatları tam olarak ayarlamak istiyorsanız (MSIE ve NN icin) Global Stil Şablonu Kullanmalısınız. -->
<!-- Bağlantılı -->
<p id="sol">
Aldığı komutlar uyarınca, veri işleyerek problem çözen otomatik elektronik aygıtların ortak adı. Bu tür aygıtlar, çalışma ilkeleri,donanım tasarımları ve uygulama alanları bakımından örneksel, sayısal ve karma bilgisayarlar olarak <font class="onemli">üçe</font> ayrılır.</p>
<p id="sol">
<ul>
<li><a href="css.html#orneksel">Örneksel (analog) bilgisayarlar</a>
<li><a href="css.html#sayisal">Sayısal bilgisayarlar</a>
<li><a href="css.html#karma">Karma bilgisayarlar</a>
</ul>
</p> <p class="solic">
Örneksel (analog) bilgisayarlar<a name="orneksel">&nbsp;&nbsp;</a></p>
<p id="sol">Açısal konum ya da gerilim gibi değişken nicelikleri temsil eden veriler üzerinde işlem yapar ve çözülmesi istenen matematiksel problemin fiziksel bir örneğini oluştururlar. Sıradan diferensiyel denklemleri çözebilen örneksel bilgisayarlar, sistem mühendisliğinde, özellikle bazı süre ve donatımların gerçek zamanlı benzetim modellerinin oluşturulmasına çok elverişlidirler. Bu bilgisayarların bir başka yaygın kullanım alanı da elektrik dağıtım sistemi gibi şebekelerin analizidir.<br>
<a href="css.html#bsl">Başa Dön</a>
</p>
<p class="solic">Sayısal bilgisayarlar,<a name="sayisal">&nbsp;&nbsp;</a></p>
<p id="sol">Çeşitli üretim süreçlerine, takım tezgahlarına , karmaşık laboratuvar ve hastane aygıtlarına kumanda etmekte kullanılırlar. Aynı özellikten, uçakların ve uzay araçlarının karmaşık iletişim sistemlerinin otomatizasyonunda da yararlanılır. Sayısal bilgisayarlar ayrıca, eğitimde yardımcı olarak (örn. temel dil ve matematik becerilerinin kazandırılmasında) , bilimsel araştırmalarda ise verilerin analizi ve matematiksel modellerin geliştirilmesi amacıyla kullanılır.
<br> <a href="css.html#bsl">Başa Dön</a> </p>
<p class="solic">Karma bilgisayarlar,<a name="karma">&nbsp;&nbsp;</a></p>
<p id="sol">Örneksel ve sayısal bilgisayarların özelliklerine ve yararlarını birleştirirler; örneksel bilgisayarlara oranla daha fazla kesinlik, sayısal bilgisayarlara oranla daha fazla deneteleme sağlarlar.
<br><a href="css.html#bsl">Başa Dön</a>
</p> </td> </tr> </table>
</body>
</html>

Burada birkaç konuya açıklık getirelim.

Bazı stil özelliklerinin sonunda gördüğünüz !important ifadesi ile ziyaretçi kendi bilgisayarındaki tarayıcı özelliklerini değiştirmiş olsa dahi bu değerleri kullanmamasının bizim belirttiğimiz değerleri kullanmasını söylemiş oluyoruz. Font özelliklerinde çoğu zaman birden çok font ismi kullandık. Bunun nedeni eğer ziyaretçinin makinasında ilk font yoksa ikincisi o da yoksa üçüncü font kullanılır. Şayet o fontta yoksa tarayıcının kendi banko fontu kullanılır. Böylelikle bizde değişik ziyaretçi makinalarında sayfamızın nasıl görünebileceğini öncelikle kontrol altına almış oluruz.

---
*Kaynak: `CSS NEDIR/CSS NEDIR.doc` — selcuk — 2004*
