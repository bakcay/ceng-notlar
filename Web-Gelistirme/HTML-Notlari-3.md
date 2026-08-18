# HTML Notlari

**HTML Hakkında**

**İlk HTML dökümanınızı yazmak**

**HTML dökümanınızı düzenlemek**

**Başlıklar (headings)**

**Paragraflara ayırmak**

**Dökümana stil kazandırmak**

**Listeler (lists)**

**Grafikler ve dosya biçimleri**

**Resim kullanımı**

**9. Bağlantılar kullanmak**

**Yerel dosyalara linkler**

**URL’ler **

**İnternet’ e linkler oluşturmak**

**Bir sayfanın bölümlerine linkler eklemek**

**Hipergrafik linkleri**

**Text biçimi (<pre> belirteci)**

**Özel karakterler**

**Açıklama listeleri**

**Adres Satırları ve e-mail linkleri**

**Blockquote belirteci**

**Renk kullanımı**

**Text düzenlemeleri**

**<hr> belirteci**

**Text ve grafik konumunu ayarlamak**

**Tablo kullanımı**

## **1. HTML Hakkında**

HTML, ya da HyperText Markup Language, bir web browser’ın multimedya dökümanlarını gösterme yoludur. Dökümanlar aslen ASCII text formatında bazı özel “tag”ler (belirteç) içeren, browserların anlayabileceği kodu içerir.

Web’deki öncelikli amaç, herkesin yayıncılık yapmasını sağlayacak standart ve geliştirilmesi basit bir sistem kurmaktı. HTML’in özellikleri ilk günlerinden bu yana oldukça uzun bir yol aldı. Bugün, HTML için üç ayrı standart tanımlanmıştır. Bunlar:

HTML 1.0

HTML 2.0

HTML 3.0

Bugün artık genel olarak HTML 2.0 ve HTML 3.0 kullanılmaktadır. HTML 3.0

da eklenen özellikler ise şunlardır:

Sayfa düzeni üzerinde ileri derecede kontrol

Manşetler

Görüntülerdeki popüler noktaların istemci tarafından işlenmesi

Özelleştirilmiş listeler

Matematik denklemler

Stil yaprakları

Form içi tablolar

HTML dökümanımızda hangi standartları kulanacağımızı dökümanımızın başında belirtmemiz gerekir (bir sonraki dersimizde bunu göreceğiz). Bu sayede, dökümanı görüntüleyen bilgisayar neye göre işlemler yapacağını bilir.

## **2. İlk HTML Dökümanınızı Yazmak******

**HTML belirteçleri nedir?**

Bir web browser bir sayfayı görüntülediği zaman, öncelikle normal bir text dosyasından sayfa hakkında bilgileri okur ve < ve > işaretlerinin (tag/belirteç) kullanıldığı özel kodlara bakar. Bir HTML belirteci için genel format şöyledir:

<belirteç\_ismi>yazılacak text</belirteç\_ismi>

Örnek olarak, bu kısımdaki başlığı sayfanızda çıkarmak için:

<h4>HTML belirteçleri nedir?</h4>

Bu belirteç, web browser’ına **HTML belirteçleri nedir? **textini 4’lük başlık şeklinde (bunun hakkında geniş bilgi ileride verilecek) göstermesini söyler. HTML belirteçleri, bir browser’a texti koyulaştırmasını, italik yapmasını, başlık olarak göstermesini ya da bir link olarak göstermesini söyleyebilir. Not edilmesi gereken nokta, bitiş belirtecinin,

</belirteç\_ismi>

şeklinde, bir bölü “/” işareti ile başlamasıdır. Bu bölü işareti, browser’a o anki komutun texte uygulanmasının bitirilmesini söyler. Eğer bölü işaretini unutursanız, browser son texti izleyen texte de aynı komutu uygulamaya devam eder; bu da istenmeyen sonuçlar doğurur.

**NOT: Bir web browser, büyük ya da küçük harf arasında ayırım yapmaz. **

** Mesela, <h3>…</h3> ile <H3>…</H3> arasında bir fark yoktur.**

HTML’in, bilgisayar programlarından bir farkı da, dökümanda bir hata yaparsanız browser ya da bilgisayarınız kilitlenmez, sadece görüntülenen döküman yanlış görüntülenir; bu durumda dökümanı açıp yanlışlığı düzeltirsiniz.

Browserınızın küçük bir sözlüğü vardır, ve HTML’in ilginç bir yanı da bu sözlükte bulamadığı komutları sadece gözardı etmesidir. Mesela:

<ahmet><h4>HTML belirteçleri nedir?</h4></ahmet>

gene aynı başlığı verir (<ahmet> diye bir komut henüz hiç bir browser tarafından desteklenmiyor!); yani browser <ahmet> komutunu gözardı eder.

## **HTML Dökümanınızı Oluşturmak**

Bir HTML dökümanı iki ayrı parçadan oluşur, head ve body (baş ve vücut). Head kısmı, döküman hakkında ekranda görünmeyen bilgileri taşır. Body ise geri kalan tüm bilgileri içerir.

Tüm HTML sayfalarının temel görüntüsü şöyledir:

<!DOCTYPE HTML PUBLIC “-//W3C//DTD HTML 3.2//EN”>

<html>

<head>

<!-- bu döküman hakkında ek bilgilerin bulunduğu başlık kısmı , ekranda görünmez -- >

</head>

<body>

<!-- görüntülenen tüm HTML -- >

: :

: :

</body>

</html>

İlk satır:

<!DOCTYPE HTML PUBLIC “-//W3C//DTD HTML 3.2//EN”>

teknik olarak gerekli değildir, fakat browser’a o anki sayfanın hangi HTML standardına göre yazıldığını gösterir.

Tüm HTML çalışmanızı <html>…</html> belirteçlerinin içine yerleştirin. Web sayfalarınız bu belirteçler olmadan da bir çok bilgisayarda çalışabilir, fakat bunları kullanarak sayfanızın Uluslararası standartlara tamamen uygun hale gelmesini, ve bu standartları kullanan her makinada çalışmasını garanti altına almış olursunuz.

Ayrıca dikkat ederseniz <!-- …… -- > arasında yer alan satırlar web sayfanızda görünmez, buraya sayfa hakkında size ya da onu inceleyen başkasına yararlı olabilecek bilgileri yazarsınız. Web sayfalarınız daha karışık hale geldiğinde (tablolar ve çerçevelerle çalışırken bolca başınıza gelecek) bu komutlar eski bir sayfanızı kontrol ya da update ederken oldukça işinize yarayacak.

İşte ilk HTML dosyanızı oluşturmak için yapmanız gerekenler:

Önce text editörünüzü açın (bunun için notepad’i kullanmanızı öneririm).

Text editör ekranına gidin.

Aşağıdaki texti girin:

<!DOCTYPE HTML PUBLIC “-//W3C//DTD HTML 3.2//EN”>

<html>

<head>

<title>Volkanlar Sayfası</title>

</head>

<!-- HTML ders notları için yapılmıştır, Ahmet Münir Piroğlu,

3 Eylül, 2000 -- >

<body>

Bu derste interneti volkanlar hakkında bilgi toplamak için kullanacak ve bulgularınızdan bir rapor hazırlayacaksınız.

</body>

</html>

**NOT: <title>…</title> belirtecinin bulunduğu yere dikkat edin. <head>…</head> belirtecinin içinde bulunuyor ve ekranda görünmüyor. <title>…</title> belirteci, dökümanları tanımlamaya yarar ve browserınızın başlık bölümündeki yazıyı belirlemeye yarar.**

Dökümanı “volkanlar.html” isminde kaydedin ve bunun için ayrı bir dizin yaratmayı unutmayın.

**NOT: Windows 3.1 kullanıcıları dosya isminin uzantısını .htm yapmak zorundadır. Browserlar .html ya da .htm dosyalarını aynı kabul ederek açarlar.**

## **Dökümanınızı bir web browser’da görüntülemek**

Web browser’ınızı açın.

**File **menüsünden **Open File…** komutunu seçin.

“yunuslar.html” dosyanızı bulun ve açın.

Şimdi browserın başlık kısmında “Volkanlar Sayfası” yazısını ve aşağıda web sayfasında da <body> belirtecinin içine yazdığınız yazıyı görüyor olmalısınız.

Sayfanız şu an aşağıdaki gibi görünüyor olmalı:

Bu derste interneti volkanlar hakkında bilgi toplamak için kullanacak ve bulgularınızdan bir rapor hazırlayacaksınız.

## **3. HTML Dökümanınızı Düzenlemek**

İlk HTML dökümanınızı yaptığınıza göre şimdi bir döküman üzerinde nasıl değişiklikler yapacağınızı ve nasıl yenileyeceğinizi göreceksiniz. Şimdi,

Eğer değilse browserınızda dökümanınızı tekrar açın.

Text editörünüzü tekrar açın (mesela notepad).

Text editöründe “volkanlar.html” dosyasını açın.

## **HTML Dökümanınızda Değişiklikler Yapmak**

Text editör ekranına gidin.

Daha önce yazdığınız textin altında bir kaç kere ENTER a basın ve aşağıdaki texti yazın:

Volkan, bir gezegenden erimiş kaya

veya mağmanın yüzeye çıktığı noktadır.

Bu çıkış, büyük bir patlama ile olabileceği

gibi sessiz ve yavaş bir şekilde de olabilir.

Dikkat etmeniz gereken nokta, bu text </body> ve </html> belirteçlerinin üstünde ve HTML dosyanızın en alt kısmında olmalıdır.

**File **menüsünden **Save **komutunu seçin.

## **Web Browserınızda Dökümanı Tekrar Yüklemek**

Dosyanızın bir önceki halinin görüntülendiği browsera dönün. Şu an son yazdığınız textin ekranda görünmediğine dikkat edin. Değişiklikleri görmek için **Reload **tuşunu kullanın. Bu komut, browserınıza o anki dökümanı tekrar yüklemesini belirtir. Artık yaptığınız değişiklikler ekranda görünüyor olmalı. Dikkat ederseniz yazı ekranda yazdığınız şekilde görünmez. Browser, normal olarak yazdığınız texti tüm ekrana yayacak şekilde görüntüler. İlerleyen derslerde sayfanızı istediğiniz şekilde düzenlemeyi öğreneceksiniz.

## **4. Başlıklar**

Başlıklar, HTML dilinde başlığa yazmak istediğiniz yazıyı başlık belirteçleri arasına yerleştirilerek oluşturulur. HTML formatında başlık belirteci şu şekildedir:

<hN>Başlıkta görünecek yazı</hN>

N, 1’den 6’ya kadar başlık boyutlarını belirten bi rakamdır. Değişik boyutlara göre bazı başlık örnekleri:

## **Düzey Başlık**

## **Düzey Başlık**

## **Düzey Başlık**

**Düzey Başlık**

**Düzey Başlık**

**Düzey Başlık**

## **HTML Başlıklarını Dökümanınıza Yerleştirmek**

Text editörünü tekrar açın.

“volkanlar.html” dosyasını açın.

Öncelikle en büyük başlığı yapmak için <h1> belirtecini kullanacağız. Aşağıdaki yazıyı şu anki textin üzerine ve </head><body> belirteçlerinden sonra yerleştirin:

<h1>Volkanlar Sayfası</h1>

Bunun altına da ileride kullanacağımız başlıkları yazın. (Bazı başlıkların h3, bazılarının h2 ile yazıldığına dikkat edin, aynı önem derecesine sahip başlıkları aynı boyutta kullanırsanız daha düzenli bir sayfanız olur.)

<h2>Giriş</h2>

<h2>Volkan Terminolojisi</h2>

<h3>St Helen Dağı</h3>

<h3>Long Valley</h3>

<h2>Mars’ta Volkan Bölgeleri</h2>

<h3>Araştırma Projesi</h3>

<h3>Referanslar</h3>

Text editöründe değişiklikleri kaydedin.

Browserınıza geri dönün, dökümanı **Reload** edin.

Browserınızda sonuç şöyle görünmelidir:

## **Volkanlar Sayfası**

Bu derste interneti volkanlar hakkında bilgi toplamak için kullanacak ve bulgularınızdan bir rapor hazırlayacaksınız. Volkan, bir gezegenden erimiş kaya veya mağmanın yüzeye çıktığı noktadır. Bu çıkış, büyük bir patlama ile olabileceği gibi sessiz ve yavaş bir şekilde de olabilir.

## **Giriş**

## **Volkan Terminolojisi******

## **St Helen Dağı******

## **Long Valley******

## **Mars’ta Volkan Bölgeleri******

## **Araştırma Projesi**

## **Referanslar******

## **5. Paragraflara Ayırmak**

Daha önce browserınızın textinizi yazarken kullandığınız ENTER’ları gözardı ettiğini gördük (browser tüm yazıyı boşlukları dolduracak şekilde dağıtıyordu). Fakat browser, bir paragraf belirteci gördüğü anda yazıya bir boşluk koyar ve yeni bir paragrafa başlar. Bir paragraf başlatmak için yazılması gereken kod:

<p>

Not edilmesi gereken nokta bu belirtecin bir bitiş belirtecine ihtiyacı yoktur. (Yani </p> belirtecini kullanmanıza genel olarak gerek yok).

Ayrıca başlık belirteçlerinde <p> belirteci hazır olarak vardır, yani <hN> ile <p> belirtecini birlikte kullanmanıza gerek olmaz. (<h> belirteci kullanıldığında browser otomatik olarak başlığın başına ve sonuna bir satır boşluk bırakır.)

## **Paragraf Belirtecini kullanmak**

HTML dökümanınıza paragraf belirteci koymak için aşağıda anlatılanları uygulayın.

Dökümanınızı notepad’de tekrar açın (eğer açık değilse).

Öncelikle (“Volkan, bir gezegenden…”) cümlesiyle başlayan bölümü yeni bir paragraf yapalım ve ardından yeni bir paragraf ekleyelim. Şimdi yazımız yaklaşık olarak şöyle görünmelidir:

Bu derste interneti volkanlar hakkinda bilgi toplamak için kullanacak ve bulgularinizdan bir rapor hazirlayacaksiniz.

<h2>Giriş</h2>

Volkan, bir gezegenden erimiş kaya

veya mağmanın yüzeye çıktığı noktadır.

Bu çıkış, büyük bir patlama ile olabileceği

gibi sessiz ve yavaş bir şekilde de olabilir.

<p>

Volkanlar, insanlardan çok önce dünya tarihinde yer almışlardır. İnsanların birkaç milyon yıllık tarihini, dört milyar yıl ile karşılaştırın.

Dökümanı kaydedin.

Browserınıza dönün ve sayfayı **Reload **edin.

## **Yazıyı bölmenin başka yolları**

Dökümanınızı bölümlere ayırmak için “hard rule/ hr” belirtecini kullanabilirsiniz. Bu

belirteç dökümana aşağıdaki gibi bir çizgi ekler:

Şimdi bunu deneyelim. Volkanlar dökümanında ilk paragraftan sonra bir <hr> belirteci kullanın. Dökümanın ilgili parçası:

<h1>Volkanlar Sayfası</h1>

Bu derste interneti volkanlar hakkında bilgi toplamak için kullanacak ve bulgularınızdan bir rapor hazırlayacaksınız.

<hr>

<h2>Giriş</h2>

Volkan, bir gezegenden erimiş kaya

veya mağmanın yüzeye çıktığı noktadır.

Bu çıkış, büyük bir patlama ile olabileceği

gibi sessiz ve yavaş bir şekilde de olabilir

<p>

Volkanlar, insanlardan çok önce dünya tarihinde yer almışlardır. İnsanların birkaç milyon yıllık tarihini, dört milyar yıl ile karşılaştırın.

şeklinde görünmelidir.

Son olarak da textin istediğiniz yerinden diğer satıra geçmesini sağlayan bir belirteç: <br>. Bu belirteci bir liste yaparken, bir şiirin mısralarını yazarken, vb. yerlerde kullanabilirsiniz. İzleyen iki örnekte <br> ve <p> belirteçleri arasındaki farkları inceleyin:

## **Sadece Paragraf Belirteci**

## ** ****HTML Sonuç**

Tüm kontrolü bilgisayara Tüm kontrolü bilgisayara bırakmaktansa onu

bırakmaktansa onu istediğiniz istediğiniz gibi yönlendirmeniz daha iyidir.

şekilde yönlendirmeniz daha

iyidir.

**<p>** Devam ediyor…

Devam ediyor…

**<p>** Gördüğünüz gibi belirteçler bu iş için

Gördüğünüz gibi belirteçler var!

bu iş için var!

## **Paragraf <p> ve <br> belirteci**

## ** HTML Sonuç**

Tüm kontrolü bilgisayara**<br>** Tüm kontrolü bilgisayara

bırakmaktansa onu istediğiniz**<br>** bırakmaktansa istediğiniz

şekilde yönlendirmeniz daha şekilde yönlendirmeniz daha iyidir.

iyidir.

**<p>** Devam ediyor…

Devam ediyor… Gördüğünüz gibi belirteçler

**<br> **bu iş için var!

Gördüğünüz gibi belirteçler**<br>**

bu iş için var!

## **6. Dökümana *****Stil *****Kazandırmak**

HTML, textinize stil kazandırmak için size bir çok belirteç sunar. Bunlardan bazıları:

## **Stil Belirteçleri**

## ** ****HTML Sonuç**

<b>Bu yazı koyu…</b> **Bu yazı koyu**

<i>Bu yazı italik…</i> *Bu yazı italik*

<tt>Bu yazı typewriter…</tt> Bu yazı typewriter

Bu belirteçleri içiçe kullanabileceğinize dikkat edin. Fakat belirteçleri doğru sıralamaya dikkat etmeniz gerekiyor, mesela ilk açtığınız belirteci son olarak kapatmanız gerekir.

<i><b>Bu yazı koyu ***Bu yazı koyu ve italik***

ve italik</b></i>

<b><i>Bu yazı da</i></b> ***Bu yazı da***

Ayrıca, bu belirteçleri başlık textinize de uygulayabilirsiniz.

<h2><i>Yeni</i> ve

<tt>Gelişmiş!</tt></h2> ***Yeni ***** ve Gelişmiş**

## **HTML Dökümanınıza Eklemeler**

Dökümanınızı tekrar açın (eğer değilse).

Text editörünüze dönün (volkanlar.html dosyasına).

Giriş bölümündeki ilk kelime olan “Volkan” kelimesinde bir değişiklik yapacağız.

Bu kelimeye şu belirteci ekleyin:

<b>Volkan </b>

Şimdi de ikinci cümledeki “milyar” kelimesinin önemini artırmak için bu kelimeyi koyu ve italik yapacağız. Değişiklikten sonra paragraf şöyle gözükmeli:

<p>

Volkanlar, insanlardan çok önce dünya tarihinde yer almışlardır. İnsanların birkaç milyon yıllık tarihini, dört <b><i>milyar</i></b> yıl ile karşılaştırın.

Son olarak, özel bir kelimeyi belirtmek için typewriter belirtecini kullanacağız

**Volkan Terminolojisi **başlığı altında şu texti girin:

Volkan araştırmaları, ya da <tt>Volkanoloji</tt>,

birçok garip terim içerir.

7. Çalışmanızı kaydedin ve browser’da tekrar yükleyin (Reload).

## **7. Listeler (lists)**

Bir çok web sayfası listelenmiş bilgi gösterir. HTML’de bu listeleri oluşturmak kolaydır, hatta bu listeler liste içinde liste oluşturabilirler (mesela bir outline oluşturmak için). Listeler ayrıca bir içindekiler bölümü hazırlarken ya da bir seri bilginin bölümlerini göstermek için uygundur.

## **Sırasız (unordered) listeler**

Sırasız listeler ya da “ul” belirteci, browserda, başında noktalarla belirtilen satırlar oluşturur. Noktaların şekli, kullanılan browsera ve yapılan ayarlarına göre değişir (tanımlanan font da etkilidir; mesela Macintosh’ta bu noktalar option-8 karakter denen bir karakterle, Times fontunda bu küçük bi kare, Genova fontunda ise büyükçe bir nokta).

**Sırasız listeye bir örnek:******

birinci parça

ikinci parça

üçünçü parça

Bu listeyi yapmak için HTML kodu:

<B>Sırasız listeye bir örnek:</B>

<ul>

<li> birinci parça

<li> ikinci parça

<li> üçüncü parça

</ul>

<ul> belirteci listenin başlangıç ve bitişini belirtir.

## **Sıralı Listeler**

Sıralı listeler browserın her parçaya bir numara atadığı listelerdir (1., 2. gibi). Sırasız listeden tek farkı <ul> belirteçlerini <ol> haline değiştirmektir. Bir önceki örneği kullanırsak:

**Sıralı listeye bir örnek:**

Birinci parça

İkinci parça

Üçüncü parça

Bu listeyi oluşturmak için HTML kodu:

<B>Sıralı listeye bir örnek:</B>

<ol>

<li> Birinci parça

<li> ikinci parça

<li> üçüncü parça

</ul>

## **İçiçe Listeler**

Sıralı ve sırasız listeler değişik derecelerde kullanılabilir, her biri browser tarafından gerektiği gibi işlenecektir. Fakat önem vermeniz gereken nokta her listenin doğru bir bitiş belirteci olması ve içiçe sıralanışında bir hata olmamasıdır.

Tüm bu <ol> <li> </ul> <li> belirteçleri ile işler biraz karışıyor gibi görünmeye başlayabilir, fakat öncelikle aklınızda tutmanız gereken listelerin temel görünüşüdür.

<ul> <ol>

<li> <li>

<li> <li>

</ul> </ol>

Başka listelerin içinde kullanılmış bir sırasız liste:

**İçiçe Sırasız Liste**

Bu birinci parça

Bu ikinci parça

Bu ikinci parçanın ilk alt parçası

Bu da bir alt parçanın alt parçası

Bu, alt parçanın ikinci alt parçası

Bu, ikinci parçanın ikinci alt parçası

Bu, ikinci parçanın üçüncü alt parçası

Bu üçüncü parça

Liste işaretlerinin her derecede değiştiğine dikkat edin.

Bu formatı oluşturmak için HTML kodu:

<B>İçiçe Sırasız Liste</B>

<ul>

<li>Bu birinci parça

<li>Bu ikinci parça

<ul>

<li>Bu ikinci parçanın ilk alt parçası

<ul>

<li>Bu da bir alt parçanın alt parçası

<li>Bu, alt parçanın ikinci alt parçası

</ul>

<li>Bu, ikinci parçanın ikinci alt parçası

<li>Bu, ikinci parçanın üçüncü alt parçası

</ul>

<li>Bu üçüncü parça

</ul>

## **İçiçe Listeler – Hepsini Kullanmak**

Sıralı listelerde sadece sıralı listeleri kullanmanız gerekmez, liste çeşitlerini birlikte içiçe kullanabilirsiniz.

Mesela, bu örnekteki sıralı listenin içinde bir sırasız liste kullanılıyor:

**İçiçe sırasız liste**

Bu birinci parça

Bu ikinci parça

Bu ikinci parçanin birinci alt parçası

1. Bu da bir alt parçanın numaralı alt parçası

Bu da bir alt parçanın numaralı başka alt parçası

Bu ikinci parçanın ikinci alt parçası

Bu ikinci parçanın üçüncü alt parçası

Bu üçüncü parça

Bu çıktının sağlanması için gerekli HTML kodu:

<B>İçiçe sırasız liste</B>

<ol>

<li>Bu birinci parça

<li>Bu ikinci parça

<ul>

<li>Bu ikinci parçanin birinci alt parçası

<ol>

<li> Bu da bir alt parçanın numaralı alt parçası

<li>Bu da bir alt parçanın numaralı başka alt parçası

</ol>

<li>Bu ikinci parçanın ikinci alt parçası

<li>Bu ikinci parçanın üçüncü alt parçası

</ul>

<li>Bu üçüncü parça

</ol>

## **HTML Dökümanınıza Listeler Yerleştirmek**

Şimdi, liste belirteçlerini kullanarak Volkanlar Sayfasına sıralı ve sırasız listeler koyacaksınız.

Açık değilse çalışmanızı açın.

HTML dökümanınızı text editöründe açın.

Volkan terminolojisi başlığı altında teknik kelime örnekleri göstermek için sırasız liste belirteçlerini kullanacağız. Dökümanınızda bu bölüme gidin.

Önce aşağıdaki cümleyi yerleştirin.

Ne kadarını biliyorsunuz?

Şimdi listeyi oluşturmak için HTML formatını kullanacağız:

<ul>

<li>kaldera

<li>vesikularite

<li>pahoehoe

<li>reoloji

<li>lahar

</ul>

Şimdi, gerekli kısımların yazılması için sıralı liste kullanacağız. Araştırma Projesi kısmı altında aşağıdaki yazıyı girin:

Göreviniz, yukarıdaki listenin dışında son yüz yıl içinde faaliyete geçmiş bir volkan hakkında bilgi toplayıp rapor etmek. Raporunuzda şunlar olmalı:

<ol>

<li>Volkanın çeşiti

<li>Jeografik konumu

<li>En yakın şehrin ismi, popülasyonu, ve volkana uzaklığı

<li>En son faaliyeti ve verdiği hasar.

<li>Faaliyetle birlikte görülen olaylar (toprak kaymaları, depremler, vs.)

</ol>

<p>

Sonra, bu volkanın yol açtığı genel hasarlar üzerine bir gözlem ve bunların azaltılması için neler gerektiği konusunda bir paragraf yazın.

HTML dosyanızı kaydedin ve browserınızda tekrar yükleyin.

## **8. Grafikler ve Dosya Biçimleri**

İnternet üzerinden sadece text göndermek klasik e-mail’dan farklı değildir. Grafikleri kullanmaya başladığınızda mesajlarınız çok daha çarpıcı hale gelir.

## **Web’in Grafik Biçimleri**

Bilgisayar grafikleri için bir çok grafik biçimi vardır. PICT. GIF. TIFF. EPS. BMP. JPEG…

Bir browserın grafikleri gösterme yolu, HTML formatında grafik dosyasının yerini ve ismini belirtmektir. Bu format birçok browserın tanıyabileceği bir format olmalıdır.

Teknik olarak söylemek gerekirse, resim formatınız **platform bağımsız** olmalıdır. HTML’in kendisi platform bağımsızdır, sonuçta text karakterleri tüm bilgisayarlar tarafından anlaşılabilir.

Bir web sayfasında görüntülenebilen standart format GIF ya da “Graphics Interchange Format”dır. GIF, resim boyutunu sıkıştırır (dolayısıyla boyutlarını küçültür) ve sonucu internette gönderilebilecek ikilik (binary) sisteme çevirir. GIF sıkıştırması, grafik büyük boyutlarda tek renk olursa çok etkilidir; ve bir renk yatayda sürekli olursa sıkıştırma çok daha iyidir.

Web de kullanılan diğer dosya formatı JPEG’dir (ismini bu formatı dizayn eden gruptan, Joint Photographic Expert Group, alır). Eskiden, JPEG resimleri browserlarda direk olarak gösterilmez, bunun için yardımcı bir program kullanılır ve resim ayrı bir ekranda görünürdü. Bugün browserların tamamına yakını bu formatı destekler.

JPEG sıkıştırması fotoğrafik resimlerde genellikle çok etkilidir. Bazen dosya boyutunu 1/10 a kadar düşürür.

## **Grafik kullanırken akılda tutulması gereken bazı noktalar**

Artık web sayfanızı tasarlamaya başladığınıza göre, resimlerinizi GIF ya da JPEG formatında kullanmayı öğrenmelisiniz.

Büyük ve çok sayıda resim sayfanızın mükemmel görünmesini sağlayabilir fakat bu resimlerin yüklenmesini bekleyecek kullanıcılar için sonuç sıkıcı ve yorucu olur. Bir tavsiye olarak, resimlerinizin boyutlarını 100k’dan az tutmanız iyidir. Küçük boyutlar her zaman iyidir.

Grafik boyutlarını çok büyük tutmamanız (genişlik 480, yükseklik 300 pixeli genelde geçmemeli) iyidir, sonuçta sayfanızı görüntüleyenlerin ekran boyutları her zaman 21 inch olmaz! Verdiğim boyutların üzerindeki görüntüleri ekranda görebilmek için genelde ekranı sağa-sola ya da yukarı-aşağı kaydırmak gerekir.

Macintosh bilgisayarlarında birçok koyu ton Windows bilgisayarlarında görünmez.

Tüm resimleri bir anda göstermek yerine bu resimlere bağlantılar (link) koymak daha iyidir, bazen internete yavaş bağlantısı olanlar bu resimleri görüntülemeyerek zaman kazanmak isteyebilirler.

Tek bir resim (mesela bir düğme) sayfanın bir çok yerinde kullanılabilir. Bu durumda browser her defasında resimi baştan yüklemek yerine ilk yüklemeden sonra geri kalan yerlerde bunu hafızadan yükler.

En önemlisi, kullanacağınız resimin o sayfa için gerekli olup olmadığından emin olun. Böylece gereksiz resimlerin yüklemeyi yavaşlatmasını engellemiş olursunuz.

Büyük resimlerden oluşmuş ve güzel görünen bir sayfa tasarlamış olabilirsiniz, fakat sayfanızı görüntülüyecek insanlar yavaş bir modemden ve yavaş bir hattan sayfanıza ulaşmaya çalışıyor olabilir.

**Sayfanız için grafikler bulmak**

Şimdi, tasarladığınız sayfa için bir kaç resim bulmanın tam zamanı. İnternete girip konuyla ilgili biraz araştırma yapabilirsiniz. Sayfanız için yararlı olabilecek birkaç resim bulmaya çalışın. Deneyebileceğiniz bir kaç yer: http://www.yahoo.com, http://altavista.digital.com

## **8a. Resim Kullanımı**

**Resimleri Gömmek için HTML Belirteçleri**

Gömülen resim, bir web sayfasının texti ile birlikte görülen

resimdir. Buradaki “Büyük M” harfi gibi.

Gömülen resim için HTML belirteci:

<img src=”dosyaismi.gif”>

Buradaki dosyaismi.gif, HTML dökümanınızın bulunduğu dizinde bulunan grafik dosyasıdır. “gömülen” kelimesiyle kastımız, bir browser bu resimi textlerin arasına yerleştirir.

Yukarıda “Büyük M”nin yanındaki yazıyla aynı satırda olduğuna dikkat edin. Eğer bu resimin kendi başına bir satırda olmasını isteseydik ne yapardık? Resmin kendi başına bir satırda görünmesini sağlamak için,

yanlızca belirtecinin başına bir paragraf belirteci yerleştirin:

<p> <img src=”dosyaismi.gif”>

## **Text ve Gömülen Resimin Düzeni**

<img…> belirteciyle bazı özellikleri kullanarak text ve resim arasında nasıl bir düzen olmasını istiyorsanız ayarlayabilirsiniz. <img> belirtecinin içine yerleştirilen *align* özelliği sayesinde aşağıdaki efektleri yapabilirsiniz:

**align=top**

** **<img align=top src=”dosyaismi.gif>

Yazı buraya gelecek. Dikkat ederseniz, ilk satırdan sonraki yazı ** **

boşlukları dolduruyor.

**align=middle**

<img align=middle src=”dosyaismi.gif”>

Yazı buraya gelecek. Bu sefer “align=middle” yani “orta” dediğimiz

için yazı grafiğin ortasından devam ediyor.

**align=bottom (normal)**

** **<img align=bottom src=”dosyaismi.gif”>

Yazı bu sefer buraya gelecek. “align=bottom” demekle yazının en

alt kısımda olacağını belirttik.

## **HTML Dökümanımıza Resim Yerleştirelim**

Bu çalışmada, üzerinde çalıştığımız dökümana bir giriş resmi koyacağız.

Çalışmanızı, açık değilse tekrar açın.

Text editörünüzde volkanlar.html dosyasını açın.

<h1>Volkanlar Sayfası<h1> başlığının üzerine şunu yazın:

<img src=”lava.gif”>

Bu belirteç, sayfanızın en üstüne daha önce bulduğunuz volkan resimini yerleştirir. “lava.gif”, bu dosyanızın ismidir; eğer dosyanızın ismi değişikse, “lava.gif” yerine o ismi yazmalısınız.

Dosyanızı kaydedin ve browserınızda tekrar yükleyin.

**NOT: Dikkat etmeniz gereken nokta, lava.gif ya da kullandığınız resim dosyası HTML dökümanınızla aynı dizinde olmalıdır. Eğer değilse, dosyanın bulunabileceği yerin tam yolunu yazmalısınız.**

Resimi yerleştirdiğinizde aklınıza neden resim belirtecinden sonra <p> belirtecini kullanmadığınız gelebilir, bunun sebebi resim belirtecinden hemen sonraki belirtecin bir başlık <hN> belirteci olmasıydı; daha önce gördüğümüz gibi bir browser başlık belirteçlerinden önce ve sonra bir satır boşluk bırakır (paragraf belirtecine gerek kalmaz).

## **Alt=”…” Özelliği**

Eğer sayfanız yanlızca text tanıyan bir browser kullanan kullanıcılar tarafından görüntülenecekse, bu kullanıcılar tarafından hiç bir resim görüntülenemez. Ya da bazen, kullanıcılar daha hızlı erişim için browserın resimleri yükleme özelliğini kapatırlar. Bu durumda <img…> belirtecinde kullanacağınız “alt” özelliği resimin yerine, orada bir resim olduğunu belirten bir boşluk koyarlar.

Bu gibi durumlarda, yanlızca text kullanan bir browser sizin yaptığınız sayfanın başlangıç kısmını şu şekilde görürler:

\[IMAGE\]

Volkanlar Sayfası

Bu derste interneti volkanlar hakkında bilgi toplamak için kullanacak ve bulgularınızdan bir rapor hazırlayacaksınız.

Bu sayede kullanıcı, sayfanın başında bir resim olduğunu anlar. Buna ek olarak <img…> belirtecini bu gibi durumlarda buraya boşluk gelmesi yerine bir text gösterecek şekilde düzenleyebilirsiniz. Mesela, düzenlediğimiz sayfada bu gibi durumlarda resimin yerine “Volkanlar üzerine bir inceleme” yazısının gelmesini sağlayalım. Bunun için textinizde şu değişikliği yapın:

<img alt=”Volkanlar üzerine bir inceleme” src=”lava.gif”>

Buradaki *alt=”…” *özelliği gerekli olduğunda resimin yerine verdiğiniz textin yerleşmesini sağlar. Çalışmamızın bu bölümü artık yanlız text özelliği olan browserlarda şu şekilde görünür:

Volkanlar üzerine bir inceleme

Volkanlar Sayfası

Bu derste interneti volkanlar hakkında bilgi toplamak için kullanacak ve bulgularınızdan bir rapor hazırlayacaksınız.

## **Yükseklik (height) ve genişlik (width) özellikleri**

<img…> belirtecinize dahil etmek isteyeceğiniz başka iki özellik de “height” ve “width” özellikleridir. Bunlar resimin boyutlarını pixel olarak belirlemenizi sağlar. Neden? Normal olarak browserınız bu boyutlara kendi karar vermek zorundadır, eğer boyutları siz belirlerseniz sayfanızın yüklenmesi daha hızlı olabilir. Ayrıca, bazen HTML 2.0 standratlarını kullanan kullanıcıların başına gelen browserlarının çökmesi sorununu engelleyebilirsiniz.

Bu özelliği eklemek için gerekli biçim şöyledir:

<img src=”dosyaismi.gif” width=X height=Y >

Burada X resimin genişliği, Y de yüksekliğidir (pixel cinsinden).

Bizim kullandığımız “lava.gif” dosyasının boyutları 300 pixel genişlik ve 259 pixel yüksekliktir. Bu durumda son olarak şu değişikliği yağmalıyız:

<img alt=”Volkanlar üzerine bir inceleme” src=”lava.gif” width=300 height=259>

**NOT: Belirtecin içinde kullanılan özelliklerin sırası önemli değildir. **

Üzerinde çalıştığımız dosyanın son görünüşü şöyle olmalı:

## **Volkanlar Sayfası**

Bu derste interneti volkanlar hakkında bilgi toplamak için kullanacak ve bulgularınızdan bir rapor hazırlayacaksınız.

## **Giriş**

Volkan, bir gezegenden erimiş kaya veya mağmanın yüzeye çıktığı noktadır. Bu çıkış, büyük bir patlama ile olabileceği gibi sessiz ve yavaş bir şekilde de olabilir

Volkanlar, insanlardan çok önce dünya tarihinde yer almışlardır. İnsanların birkaç milyon yıllık tarihini, dört milyar yıl ile karşılaştırın.

## **Volkan Terminolojisi******

Volkan araştırmaları, ya da Volkanoloji, birçok garip terim içerir.

kaldera

vesikularite

pahoehoe

reoloji

lahar

## **St Helen Dağı******

## **Long Valley******

## **Mars’ta Volkan Bölgeleri******

## **Araştırma Projesi**

Göreviniz, yukarıdaki listenin dışında son yüz yıl içinde faaliyete geçmiş bir volkan hakkında bilgi toplayıp rapor etmek. Raporunuzda şunlar olmalı:

1.Volkanın çeşiti

2.Jeografik konumu

3.En yakın şehrin ismi, popülasyonu, ve volkana uzaklığı

4.En son faaliyeti ve verdiği hasar.

5.Faaliyetle birlikte görülen olaylar (toprak kaymaları, depremler, vs.)

Sonra, bu volkanın yol açtığı genel hasarlar üzerine bir gözlem ve bunların azaltılması için neler gerektiği konusunda bir paragraf yazın.

## **Referanslar******

## **9. Bağlantılar Kullanmak**

## **URL Nedir?**

Web’in gerçek gücü istenen yerlere hipertext bağlantıları oluşturabilmektir. Bu istenen yerler başka web sayfaları olabileceği gibi, grafikler, sesler, dijital filmler, animasyonlar, programlar, bir ftp arşivi vb. olabilir.

WWW (World Wide Web), URL (Uniform Resource Locators) olarak bilinen bir adresleme sistemi kullanır. Bu hipertext bağlantıları (altı çizgili ve genellikle mavi olarak görünüler) *çapa* olarak da tanınır.

## **9a. Yerel Dosyalara Linkler**

En basit bağlantı şekli, aynı dizinde bulunan başka bir HTML dosyasını açmaktır. Bunun için yazılması gereken HTML komutu şöyledir:

<a href=”dosyaismi.html”>bağlantıyı sağlayacak yazı</a>

“a” için *anchor (çapa) *ve “href” için ***h****ypertext ****ref****erence* diyebiliriz.

Dosya ismi başka bir HTML dosyası olmalıdır. “bağlantıyı sağlayacak yazı”, hipertext ve altı çizgili olacak yazıdır.

Şimdi, çalışmamızda yerel bir dosyaya bağlantı oluşturmak için aşağıdakileri yapacağız:

Volkanlar.html dosyanızı text editöründe açın.

St Helen Dağı başlığı altında şunları yazalım:

Mayıs 18, 1980’de, uzun bir dinlenmeden sonra Washington’daki bu sessiz dağ büyük patlamalar hakkında bize <a href=”msh.html”>önemli incelemeler</a> olanağı sunmuştur.

Çalışmanızı kaydedin ve browserda tekrar yükleyin.

Şimdi text editörünüzde yeni (New) bir sayfa açın.

Aşağıdaki yazıyı girin:

<html>

<head>

<title>St Helens Dağları</title>

</head>

<body>

<h1>Mount St Helens</h1>

Tepesi ağaçlarla kaplı ve bir zamanlar sessiz olan bu dağ faaliyete geçtiğinde etrafını oyuncaklar gibi dağıttı.

</body>

</html>

Bu dosyayı msh.html adında diğer dosya ile aynı yere kaydedin.

Browserınızda Volkanlar.html dosyasını tekrar yükleyin.

“önemli incelemeler” bağlantısını test edin. Buraya kliklediğinizde browserın msh.html dosyasını yüklemesi gerekir.

## **Bir Grafiğe Bağlantı**

Bir grafiğe bağlantı yaparken kullanacağınız biçim dosyaya bağlantı yapma mantığıyla aynıdır. Bu sefer bağlantıyı yapan yazıya kliklediğiniz zaman karşınıza başka bir döküman yerine bağlantının sonundaki grafik gelir.

## **Başka Dizinlere Bağlantı**

Başka dizinlerdeki dosyalara bağlantı kurmak için dosya adını yazdığınız yere dosyanın tam yerini (path) ve dosya ismini yazmanız gerekir. Mesela, bundan sonra dökümanımızda kullanacağımız resimleri /resimler adlı bir dizine koyalım. Böylece resimlerimizin sayısı arttıkça oluşacak karışıklığı azaltmış oluruz.

Şimdi çalışmamıza yeni bir resim ekleyelim:

Bilgisayarınızda Volkanlar.html dosyasının bulunduğu yere “resimler” adında bir dizin açalım.

Bu dizinin altına St. Helens Dağını gösteren bir resim koyalım. Bizdeki bu resimin adı “msh.gif”.

“msh.html” dosyasını text editörümüzde açalım.

Resime ulaşmak için gerekli yere bir bağlantı kuralım:

Tepesi ağaçlarla kaplı ve bir zamanlar sessiz olan bu dağ faaliyete geçtiğinde <a href=”resimler/msh.gif”>etrafını oyuncaklar gibi dağıttı</a>.

Dökümanınızı kaydedin ve browserınızda tekrar yükleyin.

Son olarak “etrafını oyuncaklar gibi dağıttı” yazısına kliklerseniz aşağıdaki resimin ekranda görünmesi gerekir:

Gördüğünüz gibi başka dizinlere bağlantı kurarken tüm yolu yazmak yerine o an bulunduğumuz dizine göre olan konumu yazmamız yeterli olur. Aslında bu bağlantıları yaparken dosyaların yolunu *root* dizininden itibaren yazabilirdik. Fakat kullandığımız şeklin bir avantajı, dosyalarımızı bilgisayarımızdan başka bir yere taşıdığımızda (mesela kendi adresine) üzerinde değişiklik yapmamıza gerek kalmaz. Aksi taktirde dosyaların bulunduğu yerleri baştan yazmak gerekirdi.

**Üst Dizindeki Dosyalara Bağlantı**

Eğer bir dosya dökümanınızın bulunduğu dizinden daha önceki dizinlerde yer alıyorsa ne yapacağız? Gene *root* tan itibaren dizinleri yazmaktansa başka yollar deneyebiliriz.

Mesela şu anki dizin ve dosya sıralamamız şöyle olsun (bundan sonra dosyalarımızı bu düzene göre yazacağız):

Bu durumda, msh.html dosyasından msh.gif dosyasını görüntülemek için:

<img src=”../resimler/msh.gif”>

yazmamız gerekir. Burada kullandığımız “..” iki nokta bir önceki dizini belirtir.

Şimdi dizin ve dosyalarımızın yerinde bir değişiklik daha yapalım. “lava.gif” dosyasını “resimler” dizinin altına yerleştirelim. Bunu yaptıktan sonra dökümanımızı browserda görüntülersek lava.gif dosyasının görüntülenmediğini görürüz. Bunun sebebi artık dosyanın, bulunduğunu belirttiğimiz yerde olmamasıdır. Şimdi Volkanlar.html dosyamızı text editörümüzde tekrar açalım ve lava.gif dosyasının sayfaya eklendiği yerde şu değişikliği yapalım:

<img alt="Volkanlar üzerine bir inceleme" src="../resimler/lava.gif" width=300 height=259>

**Bir değişiklik daha:**

Artık yapmamız gereken değişiklik Volkanlar.html dosyasının ismini index.html yapmak. Neden mi? Bu dersleri bitirdiğinizde sayfanızı TR-net’teki accountunuza atacaksınız. Diyelim ki sayfanızın adresi http://www.deneme.com.tr/ . Son haliyle sayfanıza ulaşmak için yazmanız gereken adres: http://www.deneme.com.tr/Volkanlar.html dir. Fakat başlangıç dosyanızın adı index.html olsaydı adrese http://www.deneme.com.tr yazmanız yeterli olacaktı. Bunun sebebi, bir standart olarak browserlar, eğer bir dosya ismi belirtilmemişse index.html dosyasının olup olmadığına bakar, varsa bu dosyayı görüntüler.

## **9b. URL’ler**

URL, WWW’nin bilgisayarları ve dosyaları bulmak için kullandığı yoldur. URL’in içerdikleri:

İnternet servisçi makinasının çeşiti

bir internet adresi

ulaştığı dosyanın dizin sırası (path)

**URL’ler nasıl kullanılır?**

URL’lerin kullanılma şekli şudur:

şekil://in.ter.net.adresi/dizin/alt-dizin/…/dosyaismi

“şekil” ile belirtilen yer, ulaşılan servisçi makinanın cinsini belirler:

**http**

** “**HyperText Transfer Protocol” denen dosya aktarım biçimidir.

**gopher**

** **dizinlerin bir menü şeklinde göründüğü bilgi iletim servisi

**ftp**

“File Transfer Protocol (FTP)” denen servisçi dosya aktarımının gerçekliştiği makinalar için kullanılır.** **

**telnet**

Servisçi makinaya uzaktan erişebilmek için kullanılan bir servistir. Telneti kullandığınızda browserınız, bunun için yardımcı bir program kullanacaktır.

**WAIS**

“Wide Area Indexed Server”—genelde bir konu üzerine anahtar kelimelerden arama yapan servisçi

**file**

** **kendi bilgisayarınızdaki dosyaya ulaşmak için kullanılır.

Şekil ile belirttiğimiz yerden sonra hep “://” kullanılır. Bunu ise ulaşacağımız makinanın internet adresi izler.

**NOT: Bir çok servisçide büyük küçük harf arası fark vardır. UNIX ve LINUX bilgisayarları büyük küçük harf duyarlıdır ve bugün bir çok web sayfası bu bilgisayarlar üzerinden çalışır (TR-net’te olduğu gibi).**

** Volkanlar.html **

** dosyası**

** volkanlar.html**

** dosyasından farklıdır.**

## **9c. İnternet’e Linkler Oluşturmak**

Daha önce dosyalara bağlantılar oluşturduk. İnternet’teki sayfalara link oluşturmak da aynı yolla yapılır. Yapmanız gereken sadece dosya yerine yazdıklarınız yerine internet adresini yazmaktır. Yani, yazmanız gereken yaklaşık olarak şöyledir:

<a href=”URL”>Bağlantıyı sağlayacak yazı</a>

Şimdi, kendi dökümanımıza, Mars’taki volkanları gösteren bir sayfanın bağlantısını yapacağız.

“index.html” dosyanızı text editörünüzde açın.

Mars’ta Volkan Bölgeleri başlığının altına şunları yazalım:

<a href="http://bang.lanl.gov/solarsys/mars.htm">

Mars’ın</a> kendine özgü volkanik bölgeleri vardır. Bunlardan birinde ise Güneş Sisteminin bilinen en büyük volkanı, <a href="http://bang.lanl.gov/solarsys/raw/mars/olympus.gif"> Olympus Mons</a> yer alır.

Çalışmanızı kaydedin ve browserda tekrar yükleyin.

Buna ek olarak, dökümanımızdaki referanslar kısmına volkanlarla ilgili bir kaç bağlantı daha ekleyelim. Burada listeler ile bağlantıların birlikte kullanımına dikkat edin:

<ul>

<li><A HREF="http://www.avo.alaska.edu/">

Alaska Volcano Observatory</A>

<li><A HREF="http://vulcan.wr.usgs.gov/home.html">

Cascades Volcano Observatory</A>

<li><A HREF="http://www.dartmouth.edu/~volcano/">

The Electronic Volcano</A>

<li><A HREF="http://www.geo.mtu.edu/volcanoes/">

Michigan Tech Volcanoes Page</a>

<li><A HREF="http://www.geo.mtu.edu/eos/">

NASA Earth Observing System (EOS) IDS Volcanology Team</A>

<li><A HREF="http://www.geol.ucsb.edu/~fisher/">

Volcano Information Center</a>

<li><A HREF="http://vulcan.wr.usgs.gov/Servers/

earth\_servers.html">

Volcano/Earth Science-Oriented Servers</A>

<li><A HREF="http://www.ngdc.noaa.gov/seg/hazard/hazards.html">

NGDC Natural Hazards Data</a>

<li><a href="http://www.nmnh.si.edu/gvp/">

Global Volcanism Program (GVP) </a>

<li><a href= "http://www.soest.hawaii.edu/hvo">

Volcano Watch Newsletter</a>

<li><a href="http://www.jasonproject.org/JASON/HTML/

EXPEDITIONS\_JASON\_6\_home.html">

JASON Project VI: Island Earth</a>

<li><A HREF="http://volcano.und.nodak.edu/">

VolcanoWorld</A>

</ul>

Sayfanızın son hali şöyle olmalıdır:

## **9d. Bir Sayfanın Bölümlerine Linkler Eklemek**

İnternetten sayfalara ve istediğiniz dosyaya bağlantılar kurmayı öğrendiniz. Eğer bir sayfanın/dökümanın belirli bir bölümüne (mesela 80. Satırına) bağlantı kurmak isteseydiniz ne yapardınız? HTML dilinde bu da mümkün. Bu iş için kullanılan belirteçlere “named anchor (isimlere bağlantı)” deniyor. İsimlere bağlantı yapabilmek için aşağıdaki örneği inceleyin:

<a isim=”İSİM”>Bağlantının yapılacağı yazı</a>

Buradaki “İSİM”, bağlantıyı yaparken kullanacağımız adres yerine gelecek. Bir dökümanın kendisinde (sayfanın içinde başka bir yere) bağlantı yaparken belirteç:

<a href=”#xxxx”>Hipertext gibi davranacak yazı</a>

şeklinde kullanılır. “#” sembolü browsera dökümanın geneline bakmasını ve “xxxx” isimli bağlantıya gitmesini söyler. Burada “Hipertext gibi davranacak yazı”ya kliklediğinizde browser “#xxxx” isminin olduğu yeri ekranın başına getirir.

İsterseniz dökümanımızda bu belirteci kullanarak konuyu pekiştirelim:

Text editöründe index.html dosyasını açın.

Giriş başlığına gelin ve şu şekilde değiştirin:

eski hali:

<h2>Giriş</h2>

yeni hali:

<h2><a name=”başlangıç”>Giriş</a></h2>

Aynı mantıkla, dökümandaki diğer başlıklara da birer isim atayalım:

<h2><a name=”term”>Volkan Terminolojisi</a></h2>

<h2><a name=”mars”>Mars’ta Volkan Bölgeleri</a></h2>

<h3><a name=”proje”>Araştırma Projesi</a></h3>

Şu an dökümanınızı browserda tekrar yüklerseniz bir fark göremezsiniz, isim bağlantıları kullanıcılardan gizlenen belirteçlerdir.

**Aynı dökümandaki isim bağlantılarına link eklemek**

Son oluşturduğumuz isim bağlantılarını kullanabilmek için kullanıcıları sayfanın bu bölümlerine yönlendirecek hipertext linkleri oluşturmamız gerekir.** **Dökümanımız üzerinde çalışmaya devam edelim:

Şu an açık değilse, index.html dosyasını açın.

Volkanlar sayfası başlığının altındaki cümleden sonra aşağıdakileri yazın:

<hr>

<B>Bu derste…</B>

<ul><i>

<li><a href=”#başlangıç”>Giriş</a>

** **<li><a href=”#term”>Volkan Terminolojisi</a>

<li><a href=”#mars”>Mars’ta Volkan Bölgeleri</a>

<li><a href=”#proje”>Araştırma Projesi</a>

</ul>

Dökümanı kaydedip browserda tekrar yükleyin.

**Başka bir dökümana isim bağlantıları koymak**

Bu yöntemle başka bir sayfanın istediğiniz satırına (<a name…> belirtecini kullandığınız yerlere) bağlantı yapabilirsiniz. Bu konunun mantığı da dosyalara ya da internetteki adreslere bağlantı yapmakla aynıdır. Bu sefer ek olarak yazmanız gereken “#” işaretidir. Deneme olarak dökümanımızın msh.html dosyasına, index.html dosyasına geri dönmek için bir bağlantı koyalım.

msh.html dosyasını text editöründe açın.

Sayfanın en altına (</body> belirtecinden hemen önce) takip eden yazıyı yazın:

<hr>

<a href=”index.html#başlangıç”>Volkanlar Sayfasına dönüş</a>

Dosyayı save edip browserınızda görüntüleyin.

Artık sayfada Volkanlar Sayfasına dönüş yazısına kliklerseniz index.html sayfasının başlangıç bölümüne dönersiniz.

Bundan sonra önceki bilgilerinizi de kullanarak bilgisayarınızda ya da internette istediğiniz dosyanın istediğiniz bölümüne bağlantı koyabilirsiniz.

## **9e. Hipergrafik Linkleri**

Buraya kadar bağlantıları yaparken düz text kullandık. HTML de kullanabileceğimiz bir yöntem de hipergrafik bağlantılarıdır. Bu bağlantıları kullanarak istediğimiz grafiğe bir bağlantı atayabiliriz.

Şimdi dökümanımıza dönüp bir örnek deneyelim:

Text editörünüzde index.html dosyanızı açın.

Long Valley başlığı altına aşağıdakileri yazın:

Bu alan seismometresi volkanların yüzeye yaptığı basınç sonucu oluşan depremlerin kuvvetini ölçer. Bulunduğu yer, 600 bin yıl önce patlamış bir volkanın platosudur.

<p>

<a href=”../resimler/seismo.jpg”><img src=”../resimler/stamp.gif”>

-- \[Resimin Büyük Hali\] -- </a>

<p>

Dosyayı kaydedin ve browserda tekrar yükleyin.

Ekrandaki resime mouse’u götürürseniz bir hipertext linki olduğunu göreceksiniz.

## **10. Text Biçimi (<pre> belirteci)**

Daha önce gördüğünüz gibi, browserlar yazıları boşlukları dolduracak şekilde ekrana yayar. Fakat yazılarınızın düzenini kendi isteğiniz doğrultusunda oluşturmak isterseniz <pre> belirtecini kullanmanız gerekir.

Mesela basit bir tablo oluşturmak istiyorsunuz:

<pre>

Patlamalar Tarih Alan (km3 cinsinden)

----------- ------- ---------------------

Paricutin,Meksika 1943 1.3

Mt. Vesuvius, Italy MS. 79 3

Krakatoa, Endonezya 1883 18

</pre>

Sonuç:

Patlamalar Tarih Alan (km3 cinsinden)

----------- ------- ------------------------

Paricutin,Meksika 1943 1.3

Mt. Vesuvius, Italy MS. 79 3

Krakatoa, Endonezya 1883 18

Gördüğünüz gibi browserlar <pre>…</pre> belirteci arasında kalan yazıları yazdığınız şeklin aynısı halinde görüntüler.

Bu belirteç çoğu zaman bir kaç satırlık boşluk gerektiğinde de kullanılır. Mesela sayfanızın bir bölümünde 5 satırlık boşluk istiyorsunuz. Yapmanız gereken:

<pre>

</pre>

Browserınız, pre belirteçlerinin arasındaki yazıyı aynen görüntüleyeceği için bu durumda 5 satırlık boşluk bırakır.

## **11. Özel Karakterler**

**>>>**ϖ**òÆñæ **yazısını nasıl yazarsınız? HTML’de, ISO özel karakterlerini kolaylıkla kullanabilirsiniz. Yazmanız gereken sadece :

&xxxx;

XXXX kullanacağınız özel karakterin numarasıdır. Browser, & işareti ile başlayıp “;” ile biten rakamları ya da bazı HTML harflerini ekrana bu karakter ya da numaralara karşılık gelen haliyle aktarır.

Mesela şimdiye kadar eğer <pre> belirtecini kullanmazsak birden fazla boşluk kullanamıyorduk. Özel karakterler sayesinde bu mümkün. Ekrana bir boşluk çıkarmak için:

&nbsp;

yazmanız yeterli.

Diğer karakterleri ise aşağıdaki listeden bakarak kullanabilirsiniz:

|  | Karakter | HTML Girişi | ISO Latin-1 kod | İsim ya da anlam |
| --- | --- | --- | --- | --- |
|  | ¡ |  | &#161; | Cent işareti |
|  | ¿ |  | &#191; | Ters soru işareti |
|  | " | &quot; | &#34; | Tırnak işareti |
|  |  | &nbsp; | &#160; | Boşluk |
| **Semboller****** |  |  |  |  |
|  | & | &amp; |  | Ampersand |
|  | © | &copy; | &#169; | Copyright |
|  | ÷ |  | &#247; | Bölme |
|  | > | &gt; |  | Büyüktür |
|  | < | &lt; |  | Küçüktür |
|  | µ |  | &#181; | Micron |
|  | · |  | &#183; | Orta nokta |
|  | ¶ |  | &#182; | Paragraf |
|  | ± |  | &#177; | Artı/eksi |
|  | £ |  | &#163; | Ingiliz Paundu |
|  | ® | &reg; | &#174; | Müseccel marka |
|  | § |  | &#167; | Bölüm |
|  | ¥ |  | &#165; | Japon Yeni |
| **Diakritikler** |  |  |  |  |
|  | Á | &aacute; | &#225; | Küçük a, dar aksan |
|  | Á | &Aacute; | &#193; | Büyük a, dar aksan |
|  | À | &agrave; | &#224; | Küçük a, grave accent |
|  | À | &Agrave; | &#192; | Büyük a, grave accent |
|  | Â | &acirc; | &#226; | Küçük a, belgili vurgu aksanı |
|  | Â | &Acirc; | &#194; | Büyük a, belgili vurgu aksanı |
|  | Å | &aring; | &#229; | Küçük a, daire |
|  | Å | &Aring; | &#197; | Büyük a, daire |
|  | Ã | &atilde; | &#227; | Küçük a, tilde |
|  | Ã | &Atilde; | &#195; | Büyük a, tilde |
|  | Ä | &auml; | &#228; | Küçük a, dieresis veya umlaut işareti |
|  | Ä | &Auml; | &#196; | Büyük a, dieresis veya umlaut işareti |
|  | Æ | &aelig; | &#230; | Küçük ae diphtong (ligatüre) |
|  | Æ | &AElig; | &#198; | Büyük ae diphtong (ligatüre) |
|  | Ç | &ccedil; | &#231; | Küçük ç, cedilla |
|  | Ç | &Ccedil; | &#199; | Büyük ç, cedilla |
|  | É | &eacute; | &#233; | Küçük e, dar aksan |
|  | É | &Eacute; | &#201; | Büyük e, dar aksan |
|  | È | &egrave; | &#232; | Küçük e, grave accent |
|  | È | &Egrave; | &#200; | Büyük e, grave accent |
|  | Ê | &ecirc; | &#234; | Küçük e, belgili vurgu aksanı |
|  | Ê | &Ecirc; | &#202; | Büyük e, belgili vurgu aksanı |
|  | Ë | &euml; | &#235; | Küçük e, dieresis veya umlaut işareti |
|  | Ë | &Euml; | &#203; | Büyük e, dieresis veya umlaut işareti |
|  | Í | &iacute; | &#237; | Küçük I, dar aksan |
|  | Í | &Iacute; | &#205; | Büyük I, dar aksan |
|  | Ì | &igrave; | &#236; | Küçük I, grave accent |
|  | Ì | &Igrave; | &#204; | Büyük I, grave accent |
|  | Î | &icirc; | &#238; | Küçük I, belgili vurgu aksanı |
|  | Î | &Icirc; | &#206; | Büyük I, belgili vurgu aksanı |
|  | Ï | &iuml; | &#239; | Küçük I, dieresis veya umlaut işareti |
|  | Ï | &Iuml; | &#207; | Büyük I, dieresis veya umlaut işareti |
|  | Ñ | &ntilde; | &#241; | Küçük n, tilde |
|  | Ñ | &Ntilde; | &#209; | Büyük n, tilde |
|  | Ó | &oacute; | &#243; | Küçük o, dar aksan |
|  | Ó | &Oacute; | &#211; | Büyük o, dar aksan |
|  | Ò | &ograve; | &#242; | Küçük o, grave accent |
|  | Ò | &Ograve; | &#210; | Büyük o, grave accent |
|  | Ô | &ocirc; | &#244; | Küçük o, belgili vurgu aksanı |
|  | Ô | &Ocirc; | &#212; | Büyük ö, belgili vurgu aksanı |
|  | Ø | &oslash; | &#248; | Küçük o, eğik çizgi |
|  | Ø | &Oslash; | &#216; | Büyük o, eğik çizgi |
|  | Õ | &otilde; | &#245; | Küçük o, tilde |
|  | Õ | &Otilde; | &#213; | Büyük o, tilde |
|  | Ö | &Ouml; | &#214; | Büyük o, dieresis veya umlaut işareti |
|  | ß | &szlig; | &#223; | Küçük keskin s |
|  | Ú | &uacute; | &#250; | Küçük u, dar aksan |
|  | Ú | &Uacute; | &#218; | Büyük u, dar aksan |
|  | Ù | &ugrave; | &#249; | Küçük u, grave accent |
|  | Ù | &Ugrave; | &#217; | Büyük u, grave accent |
|  | Û | &ucirc; | &#251; | Küçük u, belgili vurgu aksanı |
|  | Û | &Ucirc; | &#219; | Büyük u, belgili vurgu aksanı |
|  | Ü | &uuml; | &#252; | Küçük u, dieresis veya umlaut işareti |
|  | Ü | &Uuml; | &#220; | Büyük u, dieresis veya umlaut işareti |
|  | Ÿ | &yuml; | &#255; | Küçük y, dieresis veya umlaut işareti |

## **12. Açıklama Listeleri**

Daha önce iki çeşit liste gördük- sıralı ve sırasız listeler - . Bunlara ek olarak açıklama listesi dediğimiz ve mantık olarak diğer listelere benzeyen bir liste çeşiti var. Bunun diğerlerinden farkı, parçaların başına numara ya da herhangi bir işaret gelmemesidir. Açıklama listesi belirtecinin kullanılışı şöyledir:

<dl>

<dt> birinci başlık

<dd> birinci açıklama

<dt> ikinci başlık

<dd> ikinci açıklama

:

:

<dt> N. başlık

<dd> N. açıklama

</dl>

Tüm liste <dl>…</dl> belirteçleri arasında yer alır. Arasında da başlık parçaları <**dt**> ve açıklama parçaları <**dd**> bulunur.

Bir browserda denendiğinde yukarıdaki örnek şöyle görünür:

birinci başlık

birinci açıklama

ikinci başlık

ikinci açıklama

:

:

başlık

N. açıklama

## **13. Adres Satırları ve E-Mail Linkleri**

Sayfanızı ziyaret eden insanlar size mail atmak ya da ulaşmak isteyebilirler. Bu durumda adresinizi ve mail adresinizi olduğu gibi yazmak yerine bu işler için kullanılan belirteçlerden faydalanabilirsiniz.

Adres belirtecinin HTML şekli:

<address>

adres bölümüne yazmak

istediğiniz yazı

</address>

Akılda tutulması gereken nokta, adres belirteçlerinin içerisinde diğer belirteçler serbestçe kullanılabilir.

Örnek olarak:

HTML

<address>

<b>Sayfa Başlığı</b><br>

HTML Notları<br>

Hazırlayan:<br>

Kutberk Kargın

(kutberk@tr.net)<br>

<a href=”http://www.

tr.net”>

TR.NET</a><br>

Sonuç

***Sayfa Başlığı*********

*HTML Notları***

*Hazırlayan:***

*Kutberk Kargın*

*( *kutberk@tr.net*)*

*TR.NET***

Ek olarak, adres kısmına e-mail adresini yazmaktan öte **mailto **komutunu kullanarak mail adresinizin (ya da herhangi bir yazının) üzerine kliklendiğinde size mail gelmesini sağlayabilirsiniz. Mesela sayfanızda aşağıdaki gibi bir e-mail hipertext linki oluşturun:

<a href=”mailto:kutberk@tr.net”>Kutberk’e bir

e-mail atın</a>

Hipertext linkinin üzerine kliklendiğinde browser mail yazılabilecek bir ekran yaratır (mesela netscape kullanıcıları için netscape mail).

Son olarak, adres satırlarınızın sonuna sayfanızın adresini yazmak iyi bir alışkanlıktır. Neden mi? Diyelim ki birisi sayfanızı print etti ve çıktı. Sayfanızda görünen tüm bilgileri print etmiş olmasına rağmen sayfanızın adresi normal olarak kağıdın hiç bir yerinde görünmeyecektir. Tabi, sayfanın herhangi bir yerine yazmazsanız, bunun için en uygun yerlerden birisi de sayfanın en alt kısmı, adresin altıdır (tabiki tercih her zaman sizin- sayfanızı istediğiniz gibi tasarlamak sizin elinizde, tabi o sayfayı görecek insanları da akıldan çıkarmamak lazım).

Şimdi dökümanımızı tekrar açalım ve sayfanın sonuna adresimizi ekleyelim:

index.html dosyasını bir text editöründe açın.

sayfanın sonunda (ama </body> belirtecinin üzerinde), aşağıdakileri yazalım:

<HR>

<address><B>Volkanlar Sayfası</B> <br>

HTML Notları , <a href=”mailto:ahmet@tr-net.net.tr”>

ahmet@tr-net.net.tr</a><br>

<tt>Her Hakkı Saklıdır</tt>

</address>

<p>

<tt>URL: http://www.volkanlarsayfası.com</tt>

## **14. Blockquote Belirteci**

<blockquote> (alıntı) komutu fazla kullanılmayan bir komuttur. Dökümanınızda başkalarının sözlerine yer verdiğinizde bu belirteçlerin arasına yazabilirsiniz.

Bu belirteç, arasında kalan yazıyı iki <hr> (hard rule/düz çizgi) arasına alır ve sayfada ortalar.

Mesela:

<blockquote>

Bu bir denemedir.

</blockquote>

Sonucu:

Bu bir denemedir.

Görebileceğiniz gibi, aslında blockquote belirtecinin yaptığını diğer belirteçleri kullanarak da yapabiliriz.

## **15. Renk Kullanımı**

**Arka plan renkleri:**

Sayfamızın arka planını renklendirmek için yapmamız gereken <body> belirteciyle birlikte “bgcolor” özelliğini de kullanmak.

<body bgcolor=#XXXXXX>

#XXXXXX, arkada belirecek rengin kodudur. Bu renkler RGB şeklinde (Red Green Blue/ Kırmızı Yeşil Mavi) ve onaltılık sistemdedir. Her iki basamak bir renkten ne kadar yoğun olacağını belirler (toplam 3 renk 6 basamak). Bu durumda basit bir hesapla kullanabileceğimiz toplam renk sayısının 16.7 milyon renk olduğunu görürüz (genelde bu kadarına ihtiyaç duyulmaz). Sayının başındaki “#” işareti ise sayının Hexadecimal (Onaltılık sistem) olduğunu gösterir.

Elde ettiğimiz bilgileri kullanarak üzerinde çalıştığımız dökümanın arka planını siyah yapalım (RGB formatında değeri #000000).

Yapmamız gereken tek şey <body> satırını <body bgcolor=#000000> şeklinde değiştirmek. Yazıya browserda bakın. Evet, artık hiç bir şey göremiyoruz! Bunun sebebi, yazı rengimizin de zaten siyah olmasıydı. Neyse ki yazı rengini ayarlayabileceğimiz komutlar HTML’de var:

<body bgcolor=#xxxxxx text=#xxxxxx link=#xxxxxx vlink=#xxxxxx>

xxxxxx renkleri,

bgcolor = arkaplan rengi (normali gri)

text = sayfanın normal yazı rengi (normali siyah)

link = sayfadaki hipertext linklerinin rengi (normali mavi)

vlink = daha önce ziyaret edilmiş adreslerin rengi (normali mor)

‘ni belirleyebilir.

Şimdi sayfamızın okunabilir hale gelmesi için şöyle bir renk ayarı yapacağız:

<BODY BGCOLOR=#000000 TEXT=#EEEEBB LINK=#33CCFF VLINK=#CC0000>

Bu bize siyah bir arka plan, sarı bir yazı, açık mavi hipertext, ve kırmızı ziyaret edilmiş hipertext sunacaktır. Gerekli değişikliği yaptıktan sonra browserda nasıl göründüğüne bakın. Benim browserım sonucu aşağıdaki gibi gösteriyor:

## **16. Text Düzenlemeleri**

**Font Büyüklüğü**

<font>..</font> belirteci yazı fontunun büyüklüğünü ayarlamak için kullanılabilir. Font büyüklüğü sayısal olarak belirtilir. 1 en küçük ve 7 en büyüktür (normali 3).

Hatırlamanız gereken, font büyüklüğü sayfanızın görüntülendiği bilgisayarın ayarlarına bağlıdır. Ama sonuçta sayfanızda bir yazının diğerinden büyük ya da küçük görünmesi sizin elinizde.

**NOT: Eğer bir browser <font> belirtecini desteklemiyorsa HTML 3.0 da kullanılan <big>..</big> ve <small>..</small> belirteçlerini kullanabilirsiniz.**

<font> belirtecinin formatı:

<font size=N>deneme</font>

şeklindedir. N, 1’den 7’ye kadar bir sayıdır. Font boyutlarını kullanmanın başka bir yolu da:

<font size=+2>deneme</font>

<font size=-1>deneme</font>

şeklinde göreceli bir font boyu saptamaktır. Burada kullandığımız +2, o anki font boyutunun üzerine eklenecek bir sayıdır (eksi de de aynı mantık). Bu belirteç bir diğer belirteç ile ilişkilidir- <basefont>.

<basefont size=5>

komutu normal font boyutunu 3’den 5’e değiştirir.

<font> belirteci yazının sadece boyutunu değiştirmeye yaramaz. Bu belirteç sayesinde yazının rengini ve tipini de değiştirebilirsiniz. Dökümanımızda Volkanlar Sayfası yazısını şu şekilde değiştirelim:

<b><font face=”Arial,Helvetica” size=+4 color=#FF66FF>V </font>

<font face=”Arial,Helvetica” size=+3 color=#dd0055>OLKANLAR SAYFASI</font></b>

face komutu yazının tipini belirler. İki tane tip yazılmasının sebebi ise, eğer browser ilk yazı tipini gösteremiyorsa ikinci tipi seçer. “color” komutunu ise “bgcolor” komutundan tanıyorsunuz, ismi hariç herşeyi aynıdır.

**Superscript / subscript**

Bu iki komut matematiksel yazılımda (bazen başka yerlerde) oldukça işe yarar.

<sup>…</sup> üst

<sub>…</sub> taban

Mesela 2 üzeri 5 yazısını gösterebilmek için 2<sup>5</sup> komutunu kullanmak gerekiyor.

**<strike>**

Bu belirteç, <u> (alt çizgi) belirtecine benzer. <strike>…</strike> belirteçlerinin arasına gelen yazıyı ortası çizgili yapar.

## **17. <hr> Belirteci**

Daha önce dökümanımızda <hr> belirtecini kullandık fakat bu belirteci daha geniş olarak kullanmak mümkün. <hr> da kullanılan komutlar:

<hr width=80% size=10>

Bu komut, ekrana çizilecek çizginin, genişlemesine tüm ekranın %80 ini kaplamasını, genişliğinin (dikey) ise 10 pixel olacağını belirtiyor. Bu belirtece bir de “noshade” komutu eklenebilir.

<hr width=80% size=10 noshade>

noshade komutu, browsera çizginin gölgesi olmayacağını söyler. Sonuç ise şöyledir:

## **18. Text ve Grafik Konumunu Ayarlamak**

Şimdiye kadar yazılar normal olarak sol taraftan başlıyordu. Fakat sayfanızı düzenlerken bazı yazıların sağ tarafta olmasını, bir çoğunun da ortada olmasını isteyeceksiniz. Bu durumda <p> (paragraf) belirteci ile bazı komutlar kullanabiliyoruz.

<p align=center>

Burada <p> belirteci ile kullanılan “align” komutu tüm paragrafın yerleşimini belirler. Bir şey belirtilmezse browser bunu “left” kabul eder (normali). “center”, paragrafın ekranda ortalanmasını sağlar (enine). “right” ise yazının sağa kaymasını sağlar.

**Grafik ve Text konumları**

Dökümanımızı tekrar açalım ve ilk bölümdeki yazıyı:

<img alt="Volkanlar üzerine bir inceleme" src="../resimler/lava.gif" width=300 height=259>

<b><font face="Arial,Helvetica" size=+4 color=#FF66FF>V </font>

şu yazıya çevirelim (tek fark <img> belirtecindeki “align” komutu)

<img alt="Volkanlar üzerine bir inceleme" src="../resimler/lava.gif" width=300 height=259 **align=left**>

<b><font face="Arial,Helvetica" size=+4 color=#FF66FF>V </font>

Değişiklik yapmadan önce sayfa:

Değişiklik yaptıktan sonra:

Gördüğünüz gibi <img> belirtecinde kullanılan align=left komutundan sonra geriye kalan yazılar sayfanın boş yerlerini dolduracak şekilde dizilir.

**<div> belirteci**

Bu belirtecin içinde kalan tüm text verilen yerleşimde görüntülenir. Kullanılışı:

<div align=left>…</div>

<div align=right>…</div>

<div align=center>…</div>

Buradaki son komut, <center> belirteci ile aynı işi görür. <center>…</center> belirteci, arada kalan tüm yazıyı ortalayan bir belirteçtir.

## **19. Tablo Kullanımı**

Dökümanlarınızda tablo yapmak için kullanacağınız belirteç, <table> dır. Bir tablonun başlangıcı:

<table border=N>

:

:

</table>

şeklindedir. Bu belirtecin içinde tablonun sıralarını ve kolonlarını belirlemek için <tr> ve <td> komutlarını kullanacaksınız.

Bir tablonun HTML formatı genel olarak şöyledir:

<table border=1>

<tr>

<td>1. satır, 1. kolon</td>

<td>1. satır, 2. kolon</td>

<td>1. satır, 3. kolon</td>

</tr>

<tr>

<td>2. satır, 1. kolon</td>

<td>2. satır, 2. kolon</td>

<td>2. satır, 3. kolon</td>

</tr>

<tr>

<td>3. satır, 1. kolon</td>

<td>3. satır, 2. kolon</td>

<td>3. satır, 3. kolon</td>

</tr>

</table>

Bu tablonun görünüşü ise:

**Satır ve Kolonlar**

Bir <td> belirtecinin içinde colspan ve rowspan özelliklerini kullanarak tablonuzu daha etkin düzenlemeniz mümkün. Aşağıda bununla ilgili iki örnek bulunmakta.

<table border>

<tr>

<td>Kolon 1 Satır 1</td>

<td align=center colspan=2>

Satır 1 Kolon 2-3</td>

</tr>

<tr>

<td>Satır 2 Kolon 1</td>

<td>Satır 2 Kolon 2</td>

<td>Satır 2 Kolon 3</td>

</tr>

<tr>

<td>Satır 3 Kolon 1</td>

<td>Satır 3 Kolon 2</td>

<td>Satır 3 Kolon 3</td>

</tr>

</table>

Bu kodun çıktısı:

<table border>

<tr>

<td>Kolon 1 Satır 1</td>

<td align=center colspan=2>

Satır 1 Kolon 2-3</td>

</tr>

<tr>

<td>Satır 2 Kolon 1</td>

<td valign=top rowspan=2>

Satır 2 Kolon 2</td>

<td>Satır 2 Kolon 3</td>

</tr>

<tr>

<td>Satır 3 Kolon 1</td>

<td>Satır 3 Kolon 2</td>

</tr>

</table>

Bu kodun çıktısı:

**Görünmez Tablolar**

Tabloların dışını görünmez yapmak için border=0 komutu kullanılır. Bu durumda bir tablo hala vardır fakat kullanıcı tabloyu göremez. Görünmez tablolar sayfanızın düzeninde oldukça işinize yarayabilir. Tablo kullanmadan düzenleyemeyeceğiniz yazıları görünmez tablolara yerleştirirseniz yazıları istediğiniz noktada tutmak mümkün olacaktır.

**Tabloları Renklendirmek**

Tabloların her bir hücresini istediğiniz renkte boyayabilirsiniz. Bunun için kullanılacak komut “bgcolor”dır.

**Tablo **<table bgcolor=#880000>

tüm tabloyu belirtilen renge boyar.

**Sıra **<tr bgcolor=#880000>

tüm sırayı belirtilen renk ile doldurur.

**Hücre **<td bgcolor=#880000>

tek hücreyi belirtilen renk ile doldurur.

---
*Kaynak: `HTML NOTLARI/html notları/html notları/html-1.doc` — AMP — 2000*
