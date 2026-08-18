# HTML Notlari

**"Web Style Sheets" Kavramı ve CSS (Cascading Style Sheets = Yığılmalı Stil Kağıtları):**

CSS (ingilizce açılımı Cascading Style Sheets olan Türkçeye çevrildiğin de ise Yığılmalı Stil Kağıtları) bizi HTML'in kalıplaşmış olan stil etiketlerinden bir bakıma kurtarıyor.

CSS kod kümesi sayfamızın **<head> </head>** etiketleri arasına yazılıyor.

"Style Sheets" kavramı oldukça geniş bir teknolojik yaklaşımı ifade ediyor. Açıkçası CSS konusu bu teknolojinin sadece bir bölümünü oluşturmakta olup, Style Sheets teknolojisi çerçevesinde CSS'den başka XSL, XSLT, DSSL gibi biçimlendirme teknikleri ve dillerinden de söz etmek mümkündür.

Bir web sayfasının tasarım elemanları (stil öğeleri) denilince aklımıza şunlar geliyor;

• arka planlar,

• başlıklar, yazılar, fontlar,

• tablolar,

• listeler,

• renkler ve görsel biçimler,

• bağ renkleri, efektler,

• imaj, katman vb. nesneler ve bunların sayfa üzerindeki yerleşimleri vs.

"Web Style Sheets" kavramı; işte bu tasarım elemanları üzerinde tam denetim sağlamak ve web dökümanlarının görünümlerini tayin etme işinde tasarımcılara ekstra güç kazandırmak için geliştirilmiş bir teknolojik yaklaşımı ifade etmektedir.

"Style Sheets" teknolojisini kullanmak demek, stiller belirlemek suretiyle belge biçimlendirmek demektir. Burada web dökümanlarının nasıl görüneceğini tayin etmek üzere geliştirilmiş bir takım kurallar sözkonusudur.

W3C'nin sitesinde "Web Style Sheets" teknolojisi çerçevesinde CSS, CSS1, CSS2, CSS3, CSS-P, XSL, XSLT, XPath, DSSL gibi kavramlardan sözedilmekle birlikte temelde **2** "Style Sheet" dili olduğu ifade edilmektedir.

Bunlar;

1- **CSS** (Cascading Style Sheets),

2- **XSL** (eXtensible Style Language)

Kursumuzda CSS konusunu ele alacağız.

**CSS (Cascading Style Sheets)******

CSS; çok daha etkin web sayfası biçimlendirebilmek amacıyla HTML'ye destek olması için oluşturulmuş bir işaretleme dilidir.

CSS'ye, herhangi bir web dökümanındaki yazı, başlık, font, arkaplan (background), imaj, katman, tablo ve liste gibi tasarım elemanlarının (stil öğelerinin) **HTML kodlamasındaki** uygulanış ve belirtim kurallarını belirleyen bir "web style sheets" teknolojisidir. Bu teknolojinin geliştirilmesindeki en temel amaç, HTML'nin sayfa biçimlendirme işlevlerini ekstra katkılarla arttırmak ve tasarımcıya çok daha etkin sayfa yapma imkanları sağlamaktır.

HTML belgesi (web sayfası) tarayıcıya yüklendiğinde yaptığımız stil tanımlamaları deyim yerindeyse üst üste yığılarak (basamaklandırılarak) ele alınır ve stil tanımlamasındaki yönteme bağlı olarak değerlendirilir. Yani belgedeki stil tanımlamalarının nerede yapıldığına bakılarak komutlar bir nevi basamaklandırmak suretiyle kademe kademe işlenir ve sayfa ekranda öyle gösterilir. Burada CSS komutlarının tarayıcılar tarafından işletilmesinde bir basamaklandırma modeli sözkonusudur. Bu nedenle stiller belirlemek suretiyle belge biçimlendirme olayına "**Cascading Style Sheets**" adı verilmiştir.

**CSS'nin belli başlı faydaları;**

- daha iyi sayfa kontrolu (tek dosya ile tüm sitenin kontrol edilebilmesi imkanları),

- kolay renk yönetimi,

- etkin kenar boşluğu denetimleri,

- metin biçimlendirme, gölgeleme olanakları,

- geçişler gibi görsel etkiler yaratabilme olanakları,

- nesne konumlandırma kolaylıkları,

**CSS Syntax Sözdizimi - Genel Kavramlar**

CSS kodu oluşturmanın en basit yolu HTML kodlamasında olduğu gibi herhangi bir metin editöründe (NotePad vs.) elle kodlama yapmaktır. Çünkü harici CSS dosyaları (*örneğin "style.css"*) da dahil olmak üzere CSS kodları da HTML dökümanları gibi ASCII (plain-text) formatındadırlar. Bu nedenle CSS kodlamasını basit text editörleri yardımıyla yapılabilir.

HTML ile web sayfası tasarımcılığında CSS kavramı önemli yer tutar. Bu nedenle iyi bir tasarımcı olmanın koşullarından birisi de CSS konusunu bütün yönleriyle iyice öğrenmektir.

Bir style sheet ifadesi, **selektör** ve **bildirim** olmak üzere 2 ana kısma ayrılır. Bildirim kısmı da yine aynı şekilde **özellik** ve **değer** olmak 2 bölümden oluşur. Bu söylediklerimizi aşağıda şematik olarak görebiliriz.

**En yalın CSS kodlaması;******

HTML'de yer alan ve stili belirlenebilen yani "selector" kimliği taşıyan etiketlerden herhangi birisini, örneğin **H** (Heading) etiketini baz alarak CSS kodlamasındaki en yalın hali ifade eden bir kod satırı yazalım. Aşağıda bildirim ve selectör kavramları gösterilmektedir. SELEKTÖR (selector) bir style sheet bildiriminin ilk öğesine verilen isimdir. Selektör CSS’lerde hangi etiket ile ilgili işlem yapacağımız seçmeye yarar.

Bildirim (decleration) kısmının da kendi içinde ÖZELLİK ve DEĞER olarak 2 temel bileşene ayrıldığını görmekteyiz.

Yukarıda belirttiğimiz CSS kod satırına (Style Sheet) dikkat ederseniz, temel bileşenlerin biraraya getirilmesinde kullandığımız **{ }** ve **:** şeklindeki noktalama işaretlerinin de bu yalın haldeki kod satırının tamamlayıcı öğeleri olduğunu görürüz.

Burada birbir önemli husus da; <STYLE> ... </STYLE> etiketi arasındaki stil ifadelerinde, değer ataması yapmak için yazılan sözcükler " veya ' işaretleri ile sınırlandırılmaz. Örneğin aşağıdaki ifade yanlıştır. **H1 {color: "blue"}** CSS2 ile kurallaşan bu hususa özen göstermek gerekmektedir.

CSS kapsamında ayrıca tasarımcı tarafından oluşturulabilen ID (kimlik) ve CLASS (sınıf) türünde 2 tip selektör daha vardır.

**CSS kod satırlarını (style sheet belirtimlerini) gruplandırmak;**

Aynı stil belirtiminde bulunacağımız selektör etiket sayısı birden çok ise, örneğin aşağıdaki kodlamada olduğu gibi;

Bu 3 satırlık kodlama biçimini GRUPLANDIRMAK suretiyle aşağıda görüldüğü gibi tek satır halinde daha kolay bir şekilde ifade etmek mümkündür.

**Miras Kavramı (inheritance)**

Miras kavramı; bir etikete atanan bir stil tanımının ilgili etiket kapsamı içinde kullanılan bir başka etiket tarafından aynen üstlenilmesi olayıdır. Örneğin;

Stil ifadesi;**H1 {color: green} **olsun,HTML kodu ise;

**<H1>Bu cümlede H1'in stilini miras alan bir <EM>etiket</EM> var.</H1>**
şeklinde olsun.

Burada kullandığımız <EM> etiketi <H1> etiketinin yeşil renk stil belirtimini aynen üstlenir. Yani miras devralır. Kodumuz yazarken miras kavramını göz önüne alarak yazmalıyız.

**Bir stil ifadesine açıklama satırı koymak;******

Stil ifadelerinde açıklama satırı kullanmak için **/\*** ve **\*/** işaretlerinden yararlanılır. Örnek kod aşağıda;

**H1 {color: red} /\* H1'i kırmızı yap \*/**

**Çok kullanılan bazı örnekler:**

**Örnek:******

<html>

<head>

<style type="text/css">

<!--

p {font-family: Verdana; font-size: 10px; color:#000000}

.bold {font-family: Verdana ;font size:10px; font-weight: bold;

color:#000000}

.yesilyazi {font-family: Verdana; font size:10px; color:

#00CC33}

.altinyazi {font-family: Verdana; font size: 10px; color:

#FF6633}

.maviyazi {font-family: Verdana; font size: 10px; color:

#006699}

.italik {font-family: Verdana; font size: 10px; color: #000000;

font-style: italic}

.alticizili {font-family: Verdana; font-size: 10px; color:#000000;

text-decoration: underline}

-->

</style>

<head>

<body>

<p> Galatasaray UEFA kupasını

<span class="bold">(2000 yılında) </span>

müzesine götürdü

<span class="yesilyazi”> Bütün Avrupanın takdirini kazandı.</span>

<span class="altinyazi"> Daha sonra Süper Kupaya sahip oldu</span>

<span class="alticizili"> (2001 yılında)

</span>

<span class="maviyazi"> Daha birçok başarıya imza atacak</span>

<span class="italik">Herkes Galatasaraylı olacak</span>

</p>

</body>

</html>

CSS denen şeyin, sayfanın <head> </head> bölümde parantezler ile yaptığımız kodlamayı görüyoruz.Sayfamızda <p>(paragraf) ile kodladığımız kısımlar Font ailesinden Verdana, Size (genişliği) 10 px ve rengi de Siyah olmak üzere belirlendi. Ve sayfa da <p> kodlamasını yaptığımız da hep aynı şekilde görünecektir.

**Örnek:**

<a href="deneme.htm"> Dinamik CSS link denemesi </a>

<html>

<head>

<style type="text/css">

<!--

a { font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 7pt; color:

#000000; text-decoration: none}

a:active { font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 7pt; color:

#FF0000; text-decoration: none}

a:hover { font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 7pt; color:

#FF0000; text-decoration: underline}

a:link { font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 7pt; color:

#000000; text-decoration: none}

-->

</style>

</head>

<body>

<p> <a href="deneme.htm"> Dinamik CSS link denemesi </a> </p>

</body>

</html>

**Selektörler (seçiciler):**

Bir style sheet ifadesindeki ilk öğelere "selektör" adı verilir. Bu bir HTML etiketi olabileceği gibi, **SINIF (class)** veya **KİMLİK (ID)** niteliğinde tasarımcı tarafından tanımlanabilen selektörler de olabilir. Eğer ilk öğe bir HTML etiketi ise bu "HTML Selektörü" olarak adlandırılır. Şimdi bu selektörleri içeren style sheet ifadelerine bir bakalım; Bu stil ifadeleri harici bir .css dosyasında olabileceği gibi, <head> ..</head> etiketleri arasına da konabilir

Yukarıdaki stil ifadelerinde görüldüğü üzere;

**.** işareti ile başlayan selektörlere sınıf **(class),**

**#** ile başlayan selektörlere ise kimlik **(ID)** tipinde selektör adı verilir.

Buradaki örnek stil ifadelerinin bildirim (deklerasyon) kısımlarında ise CURSOR özelliğine birtakım değerler atanmaktadır. Bunların herhangi bir web dökümanı içerisinde uygulanmasına gelince, kod satırları şöyle olabilir;.

Yukarıdaki kod satırları web dökümanının <body> .. </body> etiketleri arasında yer almalıdır

<STYLE TYPE="text/css">

body { cursor: crosshair }

.yardim { cursor: help }

#bekle { cursor: wait }

</STYLE>

<body>

<P STYLE="color: #c0c0c0"><b>AÇIKLAMA: Mouse imlecini aşağıdaki cümlelerin üzerine götürünüz!. imleçteki değişimlerr dikkat ediniz</b></p>

<br>

<font size="5">

<span class="yardim">Bu cümlede imleç değişir.</span>

<br><br>

<P ID="bekle">Bu cümlede de imleç değişir.</p>

</body>

**Bazı Özel Karakterler:**

Yukarıda anlattığımız selektörler yerine **\*** ve **>** olmak üzere 2 joker karakteri kullanabiliriz... Örneğin;

**\*{font-color: red}**

Bu ifade sayfadaki bütün etiketlere "kırmızı font rengi" stilini uygular.

**>** karakteri ise çocuk selektörler tanımlar. Örneğin;

**ul > li {list-style-type: decimal}******

Bu ifade UL etiketini ebeveyn olarak kabul eder ve UL içindeki LI öğelerini çocuk selektör olarak görür. Böylece sadece UL listelerindeki LI öğelerine stil belirtimi uygulanmış olur.

**Pseudo Classes – Sınıfımsılar**

CSS’de kullandığımız kodlarda da bazı yetersizlikler vardır. Bunlar normal etiketlerle **karşılanamayan **durumlar için düşünülmüş kontrol elemanlarıdırlar. Bütün sınıfımsıların önünde **:** (iki nokta üst üste) işareti bulunur.

**Örnek:**

**A:visited {color: maroon}**

ifadesi sınıfımsı kullanımına dair bir örnek teşkil eder. **CSS2** ile tanımlanmış sınıfımsıları (pseudo-classes) aşağıdaki tabloda görebiliriz;

| ** :first-child ****** | Bir öğenin ilk çocuk öğesi |
| --- | --- |
| ** :first-line ****** | Bir paragrafın biçimlendirilen ilk satırı |
| ** :first-letter ****** | Bir paragrafın ilk harfi |
| ** :link ****** | Henüz ziyaret edilmemiş linkler |
| ** :visited ****** | Ziyaret edilmiş linkler |
| ** :hover ****** | İmlecin o anda üzerinde durduğu öğe |
| ** :active ****** | O anda etkin olan öğe |
| ** :focus ****** | Odakta olan öğe |
| ** :lang ****** | Geçerli dil tanımı |
| ** :before ****** | İçeriği bir öğeden önceye konumlandırır |
| ** :after ****** | İçeriği bir öğeden sonraya konumlandırır |

**Örnek:**

<STYLE TYPE="text/css">

.ilksatirbuyuk:first-line{

font-size:310%;

font-weight:bold;

}

</STYLE>

Body bölümünde yer alacaktır.

<p align="justify" class="ilksatirbuyuk">

Cim Bom Galatasaray

</p>

<br>

<p align="justify">

Cim Bom Galatasaray! Dikkat edelim class ifadesi yok!

</p>

**ÖZELLİKLER:**

Bir web dökümanının tasarım elemanları (stil öğeleri) daha önce de ifade ettiğimiz gibi döküman gövdesi, arka planlar, başlıklar, yazılar, fontlar, tablolar, listeler, renkler ve görsel biçimler, bağlar, efektler, imaj, kutu modeli, katman vb. ile bunların sayfa üzerindeki yerleşimleri gibi birtakım nesnelerden oluşur. CSS içinde bu nesneleri kontrol edebilmek için belirli sayıda "**PROPERTIES**" (Özellik) tanımlanmıştır. Web sayfası oluştururken yapılan stil belirtimlerinde, yukarıda sözünü ettiğimiz tasarım elemanlarıyla ilişkilendirilebilen özellikler baz alınarak, bu özelliklere birtakım değerler (values) atanır. Örneğin **FONT** (EN ÇOK KULLANILAN ÖZELLİK) öğesini ele alırsak, bu öğenin özellikleri ve bu özelliklere atanabilecek değerler şöyledir;

**Font Özellikleri:**

| ** font-family ****** | arial, verdana, times, courier vs. bold |
| --- | --- |
| ** font-style ****** | normal, italic, oblique, inherit |
| ** font-size ****** | xx-small, small, medium, large, x-large, xx-large, larger, smaller, inherit, geçerli yüzde, geçerli uzunluk |
| ** font-variant ****** | normal, small-caps, inherit |
| ** font-weight ****** | normal, bold, bolder, lighter, 100-900, inherit |
| ** font-stretch ****** | normal, wider, narrower, ultra-condensed, extra-condensed, condensed, semi-condenced, expanded, semi-expanded, extra-expanded, ultra-expanded, inherit |
| ** font-size-adjust ****** | none, geçerli sayı, inherit |
| ** font ****** | font-style, font-variant, font-weight, font-size, line-height, font-family, inherit |

**Style Sheet Kullanım Metotları:**

Bir HTML dökümanında CSS kodlaması yapmanın, yani stil tanımlamasında bulunmanın 4 farklı metodu vardır. Bunlar **Inline (İç), Embedded (Gömülü), External (Harici Bağlantı)** ve **Importing (İthal Etme)** şeklinde isimlendirilmektedir. Tabii bu dört metodun hepsinin bir arada kullanıldığı bir beşinci metod'tan da sözetmek mümkün. Buna da "**karma metod**" adını verebiliriz.

**1.**** ****INLINE (İç) Metotu:**

Bu yöntemle; bir HTML dökümanı içerisinde, stili belirlenebilen herhangi bir HTML etiketinin kendi içine stil tanımlaması yapılabilir. Bu metotta çift tırnak olamsına dikkat edilmelidir. <head>…</head> etiketleri içine yazılması gibi durum söz konusu değildir.

**Örnek: **

**<p style="color: blue"> ... </p>**

Böyle birşey yaptığımızda, yani bir HTML etiketine stil ataması yaptığımızda tarayıcılar tarafından bu atama en büyük öncelikle dikkate alınır. Diğer stil belirtimleri geçersiz olur. Bu yöntemi kullanabilmek için ayrıca **2 etiketten** yararlanılır. Bunlar **<DIV>** ve **<SPAN>** etiketleridir.

**<div style="font-color: blue">**

**...**

**</div>**

ve diğer etiket,

**<span style="font-color: blue">**

**...******

**</span>**

Bu iki etiket arasındaki fark şudur;

<div> etiketi blok düzeyinde işlev görür. Yani kapsadığı aralıktaki bütün öğeler bir blok mantığıyla ele alınır ve bu aralıkta bütün HTML öğeleri yer alabilir. Ayrıca <div> etiketi sonlandığında bir satır atlatır. <span> etiketinde böyle bir şey sözkonusu değildir. Bu yüzden <span> etiketini **cümle içlerinde** rahatlıkla kullanabiliriz.

**2-**** ****EMBEDDED (Gömülü) Metot:**

Bu yöntemde stil tanımlamaları **<head>...</head> etiketleri arasında** yer alacak şekilde yapılır. Ve bu amaçla **<style>** etiketinden yararlanılır. Örneğin;

**<style type="text/css">**

**<!--**

** body { background: #c0c0c0;******

** background-attachment: fixed; }**

**-->**

**</style>**

Buradaki **'<!--' ve '-->'** ifadeleri stil kodlarını **eski web tarayıcılardan** saklamak için kullanılmaktadır. BODY ifadesi stil tanımlamasının selektörü, diğer ifadeler ise bu selektöre atanan stil bildirimleridir.

**3-**** ****EXTERNAL (Linked - Harici Bağlı) Metot:**

CSS kodları çok **uzun** olabilir. Bunun için CSS kodlarımızı ayrı bir not defteri sayfasında yazarız ve uzantısını .css yaparız. Daha sonra bunu sayfamıza bağlarız.

Sadece sayfamızın başına yazacağımız CSS etiketlerini Notdefterine yazmak ve uzantısını .html değil de .css yapmak.

“ali.css” dökümanını, bağlanacak olan “.html” dökümanlarınızın olduğu klasöre kopyalanır. Ve bu dosyanın sayfaya eklenmesi için aşağıdaki ifade yazılır;

<link rel="stylesheet" type="text/css" href="ali.css">

etiketini sayfanızın **<head> </head>** etiketleri arasına yazılması gerekir.Böylece .css uzantılı dosyayı sayfanıza link yolu ile eklenmiş olur.

Bu yöntemi kullandığımızda bütün bir siteyi stil tanımlamaları açısından denetim altına almış oluruz. Örneğin sitemizdeki tüm sayfaların arkaplan rengini değiştirmek istediğimizde "ali.css" dosyasındaki tek bir değişiklikle bunu gerçekleştirebiliriz. Aksi durumda sitedeki tüm sayfalar için bunu **tek tek** yapmak zorunda kalırdık.

**4-**** ****IMPORTING (İthal Etme) Metotu:**

Bu yöntemde ise kullanılmak istenen stil tanımlamaları ayrı bir dosyadan ithal edilir. Bu amaçla harici bir stil dosyasını ithal etmek için **@ import** komutu kullanılır. Örnek vermek gerekirse; web sayfasının **<head>...</head>** etiketleri arasına aşağıdaki gibi bir kod satırı yerleştirilir;

**<STYLE TYPE="text/css">**

**<!-- @import url;**

**... stil kodları**

**-->**

**</STYLE>**

**NOT:** Eğer bir web sayfasında yukarıda saydığımız bütün yöntemleri de birarada kullanırsak bunların tarayıcılar tarafından okunma sırası şu şekildedir;

Harici stil -> Gömülü stil -> İç stil

Ancak, okunan stil tanımlamalarının geçerlilik sırası ise tam tersidir;

İç stil -> Gömülü stil -> Harici stil

Yani CSS uyumlu bir tarayıcı herhangi bir web dökümanında bütün stil yöntemleri de uygulanmışsa ilk olarak harici dosyayı, sonra gömülü tanımlamaları ve daha sonra da iç stil tanımlamalarını okur. Ve iş sayfayı ekranda göstermeye gelince öncelikle "iç stil" tanımlamalarını geçerli kılar. Sonra gömülü stildeki tanımlamaları, son olarak ta harici dosyadaki tanımlamaları dikkate alır. Görüldüğü üzere burada iç stil gömülü stile baskın rol oynamaktadır. Aynı şekilde gömülü stil de harici stil üzerinde baskın olur. Böyle bir durumda, tanımladığımız stillerin değerlendirilmesi açısından, tarayıcı ile web sayfası arasındaki ilişkide bir nevi "basamaklama" olayı sözkonusudur. CSS'deki "Cascading" kelimesi de zaten buradan kaynaklanmaktadır.

**CSS Standartları ve W3C:**

CSS'nin gelişimi W3C tarafından kontrol edilmekte olup, şu ana kadar Cascading Style Sheets hakkındaki gelişmeler **CSS1** ve **CSS2** şeklinde iki versiyonda (level) toplanmıştır. CSS3 için ise konsorsiyumun çalışmaları halen sürmektedir. CSS hakkında herhangi bir hususta tereddüte düştüğünüzde ilk bakacağınız yer bu konsorsiyumun teknik belgeleri olmalıdır.

World Wide Web Konsorsiyumu için;

**CSS: *****CSS Homepage - W3C***** **(Cascading Style Sheets)

**CSS1: *****http://www.w3.org/TR/REC-CSS1*** (Cascading Style Sheets, level 1)

**CSS2: *****http://www.w3.org/TR/REC-CSS2*** (Cascading Style Sheets, level 2)

**CSS3: *****http://www.w3.org/Style/CSS/current-work***

## <style> etiketlerine dikkat edelim

---
*Kaynak: `HTML NOTLARI/html notları/CSS-1.doc` — Göksel BİRİCİK — 2003*
