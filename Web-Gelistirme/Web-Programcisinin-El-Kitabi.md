# Web Programcisinin El Kitabi

## **Web Programcısının El Kitabı **

Bu doküman, Web programcıları için, mosaic, netscape, lynx gibi web programlarını kullanabildikleri gözönüne alınarak yazılmıştır. Yazının amacı yeni başlayanlara ve HTML programlama hakkında az bilgisi olanlara yol göstermektir.

Dökümanın İngilizce sürümüne www.w3.org adresinden ulaşabilirsiniz.

İnternet üzerinde yeralan tüm popüler HTML tarayıcıları, ister UNIX altında ister Windows altında olsun, Türkçe desteği vermektedirler. HTML dosyalarınızda rahatlıkla Türkçe karakterler kullanabilirsiniz.

Sürüm 0.1 1993
Sürüm 0.2 Ağustos 1997

gorkem@cclub.metu.edu.tr

**İçindekiler**

HTML dökümanın hazırlanması

Temel belirtecler

Konular

Başlıklar

Paragraf ve satırlar

Bağlantılar

Bağıl bağlantılar

Kaynak bağlantıları

Döküman içi bağlantılar

Diğer döküman bağlantıları

Diğer komutlar

Listeler

Düz listeler

Numaralı listeler

Tanımlı listeleri

İçiçe listeler

Formatlı metinler

HTML yorum satırları

Özel karakterler

Resim görüntüleme

Tablo hazırlama

Tablo örnekleri

Formlar

Daha geniş bilgi için

## **HTML dökümanın hazırlanması **

HTML dökümanlarının tamamı ASCII karakterlerden oluşan ve herhangi bir editörde yazılabilen metinlerden oluşmuştur. UNIX üzerinde pico, vi veya sevdiğiniz herhangi bir metin editörü kullanarak HTML dökümanlarınızı hazırlayabilirsiniz.
Bunun dışında, kullanıcının HTML dilini bilmediği farzedilerek Windows ve DOS altında çalışan çeşitli yazılımlar hazırlanmıştır. Ayrıca, HTML kodunun doğruluğunu kontrol eden yardımcı programlara da Internet üzerinden erişilebilir.

Temel bir HTML dökümanı aşağıdaki gibi yazılabilir:

< title> Burası konunun yazılacağı yer </title>

< h1> Bu, 1 numaralı başlık </h1>

HTML dünyasına hoşgeldiniz. <br>

Birinci paragrafımız. <p>

Bu da ikinci.. <p>

HTML yazarken, metnin Web tarayıcının anlayacağı şekilde gösterilebilmesi için belirteçler kullanır. Yukarıdaki örnekte:

**< title> **ve **< /title> **belirteçleri, dökümanın konusunu gösterir.

**< h1> **ve **< /h1> **belirteçleri, dökümanın başlığını tanımlar.

**< p> **belirteci, paragraf tanımlar.

Tüm HTML belirteçleri, küçüktür işareti (**< **), belirteç ismi ve büyüktür işaretinden (**> **) oluşur. Genellikle her belirtecin **< h1> **ve **< /h1> **örneklerindeki gibi bir çifti olur ve sondaki belirtecin ismi önüne ayraç gelir.
Yukarıdaki örnekte **< h1> **, Web programına 1 numaralı başlık formatında yazmasını, **</h1> **ise bu formatı kapatmasını söyler. **< p> **belirteci istisna bir durumdur ve < /p> olarak kapatılmaz.

Not1: HTML belirteçleri küçük-büyük harf ayrımı yapmaz. **< title > **, **< tITLE> **veya **< tiTlE> **belirteçleri aynı görevi yaparlar.
Not2: Her belirtecin bir WWW "browser"ında tanımlı olma zorunluluğu yoktur. Eğer browser desteklemediği bir komut ile karşılaşırsa kullanıcıyı uyarmadan belirteci gözardı eder.

## **Temel Belirteçler **

Bu bölümde en sık kullanılan belirteçler kısaca anlatılacaktır.

***Konular *********

Her HTML sayfasının ile ayrılan bir konusu olmak zorundadır. Konular genellikle sayfadan bağımsız olarak ekranın en üstüne basılır.

<title> Sayfamın konusu </title>

***Başlıklar *********

HTML, 1'den 6'ya kadar numaralanmış 6 çeşit başlık destekler. Başlıklar normal karakterlerden daha büyük ve kalın yazılırlar. Temel olarak,

<Hy> Sayfamın başlığı </Hy>

olarak tanımlanmış bir belirteçte y, 1 ile 6 arası bir değer alabilir. Y sayısı arttıkça fontun büyüklüğü azalır.
Pek çok uygulamada, sayfanın konusu ile başlığını aynı tutabilirsiniz.

***Paragraflar *********

Diğer kelime işlemcilerdekinin aksine, HTML dökümanlarında programcı özel bir belirteç kullanmadıkça bir cümle herhangi bir yerinden ayrılıp kalan kısmı altta görünebilir, birden fazla boş satır tek satır olarak algılanır.
Aşağıdaki örnekte, kaynak kodunda iki satır olmasına karşın, WWW tarayıcı bunu algılamaz ve ekranda tek satır olarak görüntüler. Bir tarayıcı satır sonlarını ve boş satırları gözardı edeceğinden, paragrafları mutlaka **< p> **belirteci ile ayırmalısınız.

HTML'ye hoşgeldiniz <br>

Bu ilk paragraf <p>

Buna göre aşağıdaki örnek, okuduğunuz dosyanın başındaki örnekle aynı çıktıyı verir.

<title> Burası konunun yazılacağı yer </title>

<h1> Bu, 1 numaralı başlık </h1>

HTML dünyasına hoşgeldiniz. Birinci paragrafımız. <p>

Bu da ikinci.. <p>

HTML dosyalarının okunurluğunu artırmak için başlıklar ile karşılık gelen belirteçleri aynı satirda, paragraf düzenleyen komutlar ise satır sonunda olmalıdır.

***Satır sonu belirteci *********

Paragraf, iki satır arasında bir satır boşluk bırakırken, satır sonu belirteci kullanıldığı kursör alta geçer ve takip eden tüm metin,*boşluk bırakmadan* bir alttan yazılır.

Bu ilk satır. <br>

İkinci satır daha uzun. <br>

Ama bu bir paragraf sonu..<p>

***Sayfanın ortalanması *********

Paragraflar ortalanırken **< center> **ve **</center> **belirteçlerinden yararlanılır. Ortalanması istenen tüm metin, bu iki belirtecin arasına yazılır.

<center>

In practical terms, HTML is a collection of styles.

</center>

## **Bağlantılar **

HTML'nin en büyük özelliklerinden birisi, tek sayfa ile sınırlı kalmamasıdır. Böylece bir sayfadan diğerine bağlantı yapılabilir. HTML'in bu görevini yerine getirmesini sağlayan belirteç **<a> **'dir Dökümanınızdan başka dökümana bağlantı ypabilmek için:

Belirteci girin.
(Kısaca ilk satıra **<a** yazın)

Hangi dökümana geçiş yapmak istiyorsanız, ismini yazın.
HREF="*dosyaismi*"

Bu dökümanı ekranda hangi isimle göstermek istediğinizi belirtin.

Belirteci kapatın.
**</a> ******

Kısa bir örnekle açıklayalım:

<a href="internet.html"> İnternet'ten nasıl yararlanabilirim ? </a>

Ekranda "İnternet'ten nasıl yararlanabilirim ?" yazısı belirecek ve kullanıcıdan burayı seçmeyi bekleyecektir. Kullanıcı fare ile bu yazı üzerine tıkladığında ise program kontrolü yine bir HTML dosya olan *internet.html* dosyasına bırakacaktır. Bu durumda bulunduğunuz dizinden farklı bir dizindeki dosyaya bağlantı yapmak isterseniz, o dosyanın ait olduğu dizini yazmak zorundasınız.Buna göre *"diller/Fortran/giris.html" *dosyasını kullanabilmek için

<a href="diller/Fortran/giris.html" >

Fortran diline giriş </a>

şeklinde bir belirteç yazmak gerekir.

***Kaynak Bağlantıları *********

HTML'in bir diğer özelliği ise, tek bir makinaya bağımlı kalmadan diğer İnternet servisleriyle bağlantı kurabilmesidir. Bunun için URL (Uniform Resource Locator) kullanılır. URL, http,gopher, news ve telnet gibi servisler olabilir. Kullanım şekli,

*URL-ismi://makina-ismi\[:port\]/dizinler/dosya-ismi ***

Burada URL,

*file :* Kendi makinanız üzerindeki bir dosyaya,
*http :* Bir WWW sunucusu üzerindeki bir dosyaya,
*gopher : *Gopher sunucusu üzerindeki bir dosyaya,
*news : *Bir UseNet haber grubundaki bir dosyaya,
*WAIS : *WAIS sunucusu üzerindeki bir dosyaya

erişmek için kullanılır.

Birkaç örnek vermek gerekirse,

<a href=http://yardim.bilkent.edu.tr> Yeni başlayanlar için yardım sayfası </a>

Port numarası, genellikle yazılmaz. Size aksi durum belirtilmedikçe, kullanmanıza gerek yoktur. WWW standart portu 80'dir.

***Döküman içi bağlantılar *********

Bir metin üzerinde belirli bölgelere ulaşmak için yine belirteçler kullanılabilir. Diyelim ki bir döküman hazırladınız ve bunu kullanıcının erişebileceği 2 parçaya ayırmak istiyorsunuz. Yapmanız gereken, bu üç parçanın isimlerini belirlemek ve dökümanda yerlerini ayırmaktır. Örnekte,

<a href="bu\_dökümanın#1.parça"> Buradan ilk bölüme gidin </a>

<a href="bu\_dökümanın#2.parça"> Buradan ikinci bölüme </a>

<a name="1.parça"> İşte ilk bölüm

İlk bölüm ile ilgili metinler burada... </br>

<a name="2.parça"> İşte ikinci bölüm

İkinci bölüm ile ilgili metiner burada.. </bt>

*<a href= *ile başladığınız belirteçte önce döküman ismini, sonra da dökümanın içindeki parça ismini girmelisiniz. *<a name= *belirtecinde ise o belirteçten itibaren parçanın başladığını anlıyoruz.

Kullanıcı ilk bölüme gitmek için fareyi kullandığında ekranda ,

İlk bölüm ile ilgili bilgiler burada

ifadesini görecektir.

***Diğer döküman bölgelerine bağlantı *********

Yukarıdaki örnek doğrultusunda farklı olarak tek yapılması gereken, döküman ismine, hangi dökümana bağlantı yapmak istiyorsak o ismi vermektir.

<a href="diğer\_döküman\_ismi#parça\_ismi"> başka dökümana geçiş</a>

## **Ana komutlar **

***Listeler *********

Dökümanların göze hoş görünmelerini sağlamak amacıyla listeler yaygın olarak kullanılır. HTML, pek çok liste çeşidi destekler. Bunlar, *düz listeler, numaralı listeler, tanımlı listeler* ve *içiçe listelerdir.*

**Düz listeler **

Düz liste yaratmak için,

Listeye başlamak için belirteç açılır.
*<ul> ***

Liste elemanlarını teker teker girerken başına *<li> *belirteci girilir. Kapatmak için *</li> *belirtecine gerek yoktur.

Listeyi bitirmek için belirteç kapatılır.
*</ul> ***

Örnek olarak,

<ul>

<li> Elma

<li> Armut

</ul>

Örnek, ekranda şu şekilde görülür :

Elma

Armut

*<li> *belirteçleri içinde paragraflar, diğer dökümanlara bağlantılar, ve diğer belirteçleri kullanabilirsiniz.

**Numaralı Listeler **

Numaralı listeler, düz listelerden farklı olarak, *<ul> *belirteci yerine *<ol> *kullanırlar. Ekrandaki liste elemanlarının başına 1'den başlayarak sayılar eklenir.
Aşağıdaki HTML kodu,

<ol>

<li> Linux İşletim Sistemi

<li> Linux'un desteklediği donanımlar

</ol>

ekrana şunları yazar:

Linux İşletim Sistemi

Linux'un desteklediği donanımlar

**Tanımlı Listeler **

Genellikle birden fazla başlığı olan, her başlık altında kısa bir metin içeren yazılar, tanımlı listeler ile oluşturulur. Tanımı yapılacak başlık, *<dt> *ile belirtilir, *<dd> *ile başlık altına metin girilir. Tüm liste, *<dl> *ile *</dl> *arasına alınır.

<DL>

<DT> Kişisel Kullanım

<DD> Linux evinde veya işinde UNIX işletim sistemi altında çalışmak

isteyenler için ideal bir platformdur. Özellikle işi veya eğitimi

sırasında UNIX platformlar altında çalışmak, uygulamalar kullanmak

veya yazılım geliştiren kişiler kendi kişisel bilgisayarlarında benzer

ortamı yakalayabilmektedirler.

<DT> Internet Sunucusu

<DD> Linux doğrudan TCP/IP desteği ile gelmektedir. Bu yönü ile TCP/IP

temelli bilgisayar ağlarında hem istemci hem de sunucu olarak yaygın

kullanım bulmuştur.

</DL>

Ekrandaki çıktı şu şekilde görünür:

Kişisel Kullanım

Linux evinde veya işinde UNIX işletim sistemi altında çalışmak isteyenler için ideal bir platformdur. Özellikle işi veya eğitimi sırasında UNIX platformlar altında çalışmak, uygulamalar kullanmak veya yazılım geliştiren kişiler kendi kişisel bilgisayarlarında benzer ortamı yakalayabilmektedirler.

Internet Sunucusu

Linux doğrudan TCP/IP desteği ile gelmektedir. Bu yönü ile TCP/IP temelli bilgisayar ağlarında hem istemci hem de sunucu olarak yaygın kullanım bulmuştur.

**İçiçe Listeler **

Tüm liste çeşitleri, 3'den fazla bölüm kullanmadıkça içiçe yazılabilir. Örnek olarak,

<ul>

<li> İstanbul'un büyük semtleri

<lu>

<li> Beyoğlu

<li> Taksim

<li> Bakırköy

</lu>

<li> Ankara'nın belli başlı yerleşim birimleri

<lu>

<li> Kızılay

<li> Ulus

</lu>

</lu>

Ekrandaki görüntüsü,

İstanbul'un büyük semtleri

Beyoğlu

Taksim

Bakırköy

Ankara'nın belli başlı yerleşim birimleri

Kızılay

Ulus

**Formatlı Metinler **

HTML'de, programda yazıldığı gibi ekrana çıktı vermeyi sağlayan komutlar *<pre> *ve *</pre> *belirteç çiftleridir. Bunlar kullanıldığı zaman tüm metin, yazıldığı gibi ekranda görünür. Aşağıdaki satırlar,

<pre>

PATH=.:~/bin/:$PATH

export PATH

\# Set up the terminal:

stty erase "^?" kill "^U" intr "^C" eof "^D"

stty hupcl ixon ixoff

date '+Tarih :%D'

TERM=vt100

</pre>

ekranda şu şekilde görünür :

PATH=.:~/bin/:$PATH

export PATH

\# Set up the terminal:

stty erase "^?" kill "^U" intr "^C" eof "^D"

stty hupcl ixon ixoff

date '+Tarih :%D'

TERM=vt100

**HTML'de yorum satırları**

HTML dokumanda yorumlayıcı tarafından gözönüne alınmayacak olan yorum satırları **<!-- **ve **--> **belirteçleri arasına alınır. Bu sayede programı yazmayı kolaylaştıracak yorumlar eklenebilir. Örneğin,

<!--

karakterler..

karakterler...

-->

veya

<!-- karakterler... --

-- karakterler.. --

>

**Özel karakterler **

Web programı, birtakım karakterleri ekranda göstermek için farklı bir format kullanır. Aşağıda, bu tür farklı karakterleri göstermek için girilmesi gereken kodlar verilmiştir.

&lt;

< (küçüktür)

&gt;

> (büyüktür)

&amp;

& (ve)

&quot;

" (tırnak)

## **Resim Görüntüleme **

Eğer Web sayfalarını gezerken grafik destekleyen bir program ( Mosaic, Netscape) kullanıyorsanız, ekranda resimlerin, arkaplanların ve hatta animasyonların olduğunu farketmişsinizdir. Bu resimler genellikle X Bitmap (XBM) , GIF, veya JPG formatlı olurlar ve dosyaya görsel bir çekicilik katarlar. Buna rağmen aynı ekranda çok miktarda resim kullanmaktan sakınmalıdır, çünkü bu durumda resimler kullanıcıya daha geç bir sürede ulaşır.

Ekranda resim görüntülemek için,

<img src="resmin bulunduğu dizin">

demeniz yeterlidir. Burada, nasıl HTML dökümanların hepsi *.html *ile bitiyorsa, tüm resim dosyalarının sonu da *.xbm , .gif *veya *.jpg *ile bitmelidir. Özel bir durum olmadıkça görüntülenen resmin alt kısmı ile metin yanyana gelirler.

<img src="g.gıf">

Metin resmin altında ..

Örneği, ekranda şu şekilde gösterilir:

Metin resmin altında ..

Sözkonusu metni resmin yanına veya üstüne koymak için *ALIGN=TOP *seçeneğini yerleştirin.

<img src="g.gif" align=top>

Metin resmin üstünde ..

Metin resmin üstünde ..

Veya ortaya almak için *ALIGN=MIDDLE *kullanın.

<img src="g.gif" align=bottom>

Metin resmin yanında ..

Metin resmin yanında ..

Görüntünün orijinal formatında değişiklik yapmadan ekranda enini ve boyunu ayarlamak mümkündür. Bunun için **height=sayı **ve **width=sayı **ara belirteçleri kullanılır. "Sayı" değişkeni piksel olarak verilir.

<img src="g.gif" height=20 width=30>

## **Tablo Hazırlama**

Grafik destekli Web programlarının tablo desteği ile çok çeşitli istatistiki bilgiler, programlar, her türlü listeler ekranda derli toplu gösterilebilir. Tablo hazırlama başlığı altındaki örnekler, her çeşit tablonun oluşturulması için yeterli değildir. Kullanıcı, isteği doğrultusunda bunları gerçekleştirmelidir.

Ekranda tablo gösterirken, o an kullanılan pencerenin büyüklüğüne ve tablo içindeki metinin genişliğine göre tablonun en ve boyu değişebilir.

Tablo, satır ve sütunlardan oluştuğu için her hücre ayrı ayrı tanımlanır. Her satır ve sütun, kendi içinde başka satır ve sütunları ihtiva edebilir.

Tablolara başlık, liste, paragraf, form, figür ve her formatta metin konabilir.

Örneğin,

<TABLE BORDER>

<TR><TH ROWSPAN=2><TH COLSPAN=2>Average

<TH ROWSPAN=2>other<BR>category<TH>Misc

<TR><TH>height<TH>weight

<TR><TH ALIGN=LEFT>males<TD>1.9<TD>0.003

<TR><TH ALIGN=LEFT ROWSPAN=2>females<TD>1.7<TD>0.002

</TABLE>

Yukarıdaki örnek, aşağıdaki gibi görünür:

|  | **Average ****** | **other category ****** | **Misc ****** |  |
| --- | --- | --- | --- | --- |
| **height ****** | **weight ****** |  |  |  |
| **males ****** | 1.9 | 0.003 |  |  |
| **females ****** | 1.7 | 0.002 |  |  |

Dikkat edilmesi gereken noktalar:

Öntanımli olarak, header hücreler merkeze alınır, diğerleri sağa yanaşık olarak ekrana gelirler. Bunu engellemek için hücre için** <ALIGN=.. **belirteci, tüm tablo için **<COLSPEC=.. **belirteci kullanılır.

Hücreler boş olabilir.

Tablodaki her satırdaki kolon sayısının eşit olmadığı durumlarda kayıp hücreler tablonun sağına yerleştirilir ve içleri boş kalır.

Tablodaki satır sayısı **<tr **belirteci tarafından tanımlanır.

**<th> **ve **<tc> **belirteçleri sadece **<tr> **belirteçleri arasında olabilir.

Hücrelerin üstüste gelmemesine çalışın, bu gibi durumlarda hatalı tablo görüntüleri ortaya çıkabilir.

**Tablo ebadı **

Tüm tablonun uzunluğu, en geniş satırla belirlenir. Kelimeler kısaltılmadığı için paragraflar **<br> **ile kesilmedikçe ekrana gelirler. En kısa uzunluk da en geniş kelime veya resmin uzunluğu ile bağıntılıdır. **Align ******

Tablonun dik halinin nasıl olacağını belirler.

**Left**

Metini ekranın soluna yanaşık yazar.

**Right**

Metini ekranın sağına yanaşık yazar.

**Colspec ******

Sütunların ebadını ayarlar. Sütunlar soldan sağa, bir büyük harf ve onu izleyen bir sayı ile listelenirler (örneğin **<COLSPEC="L20 C8 L10" > **). Hücrenin ihtiva etttiği yazıları **L **harfi sola, **R **harfi sağa alır. **C **harfi ortalamak için kullanılır. Burada belirteç seçenekleri mutlaka büyük harfle yazılır.

**Border ******

Bu belirteç, tablo kenarlarının ebadını kontrol etmeye yarar.
<table border=10>

**Nowrap ******

Programın tablo içinde paragrafları otomatik olarak kesmemesi için kullanılır.Böylece kullanıcı istediği yerde **<br> **belirtecini kullanabilir.

**Tablo Örnekleri **

***Temel bir 3X2 tablo *********

| A | B | C |
| --- | --- | --- |
| D | E | F |

<table border>

<tr>

<td>A</td> <td>B</td> <td>C</td>

</tr>

<tr>

<td>D</td> <td>E</td> <td>F</td>

</tr>

</table>

***"Rowspan" kullanılması *********

| 1. hücre | 2. hücre | 3. hücre |
| --- | --- | --- |
| 4. hücre | 5. hücre |  |

<table border>

<tr>

<td>1. hücre</td>

<td rowspan=2>2. hücre</td>

<td>3. hücre</td>

</tr>

<tr>

<td>4. hücre</td> <td>5. hücre</td>

</tr>

</table>

| 1. hücre | 2. hücre | 3. hücre | 4. hücre |
| --- | --- | --- | --- |
| 5. hücre | 6. hücre | 7. hücre |  |

<table border>

<tr>

<td rowspan=2>1. hücre</td>

<td>2. hücre</td> <td>3. hücre</td>

<td>4. hücre</td>

</tr>

<tr>

<td>5. hücre</td> <td>6. hücre</td> <td>7. hücre

</td>

</tr>

</table>

***"Colspan" kullanılması *********

| 1. hücre | 2. hücre |  |
| --- | --- | --- |
| 3. hücre | 4. hücre | 5. hücre |

<table border>

<tr>

<td>1. hücre</td>

<td colspan=2>2. hücre</td>

</tr>

<tr>

<td>3. hücre</td> <td>Item 4</td> <td>5. hücre</td>

</tr>

</table>

***"Colspan" ve Başlıkların birlikte kullanılması *********

| **Head1****** | **Head2****** |  |  |
| --- | --- | --- | --- |
| A | B | C | D |
| E | F | G | H |

<table border>

<tr>

<th colspan=2>Head1</th>

<th colspan=2>Head2</th>

</tr>

<tr>

<td>A</td> <td>B</td> <td>C</td> <td>D</td>

</tr>

<tr>

<td>E</td> <td>F</td> <td>G</td> <td>H</td>

</tr>

</table>

***Yan Başlıkların kullanımı *********

| **Başlık1****** | 1. hücre | 2. hücre | 3. hücre |
| --- | --- | --- | --- |
| **Başlık2****** | 4. hücre | 5. hücre | 6. hücre |
| **Başlık3****** | 7. hücre | 8. hücre | 9. hücre |

<table border>

<tr><th>Başlık1</th>

<td>1. hücre</td> <td>2. hücre</td> <td>3. hücre</td></tr>

<tr><th>Başlık2</th>

<td>4. hücre</td> <td>5. hücre</td> <td>6.hücre</td></tr>

<tr><th>Başlık3</th>

<td>7. hücre</td> <td>8. hücre</td> <td>9. hücre</td></tr> </table>

***"Rowspan" ve yan başlıkların birlikte kullanılması *********

| **Başlık1****** | 1. hücre | 2. hücre | 3. hücre | 4. hücre |
| --- | --- | --- | --- | --- |
| 5. hücre | 6. hücre | 7. hücre | 8. hücre |  |
| **Başlık2****** | 9. hücre | 10. hücre | 11. hücre | 12. hücre |

<table border>

<tr><th rowspan=2>Başlık1</th>

<td>1. hücre</td> <td>2. hücre</td><td>3. hücre</td> <td>4. hücre</td>

</tr>

<tr><td>5. hücre</td> <td>6. hücre</td><td>7. hücre</td> <td>8. hücre</td>

</tr>

<tr><th>Başlık2</th>

<td>9. hücre</td> <td>10. hücre</td> <td>11. hücre</td> <td>12. hücre</td>

</tr>

</table>

***10 birim kenarı olan tablo *********

| 1. hücre | 2. hücre |
| --- | --- |
| 3. hücre | 4. hücre |

<table border=10>

<tr> <td>1. hücre</td> <td>2. hücre</td>

</tr>

<tr> <td>3. hücre</td> <td>4. hücre</td>

</tr>

</table>

***Cellpadding ve Cellspacing belirteçlerinin kullanılması***** **

| A | B | C |
| --- | --- | --- |
| D | E | F |

<table border cellpadding=10 cellspacing=0>

<tr>

<td>A</td> <td>B</td> <td>C</td>

</tr>

<tr>

<td>D</td> <td>E</td> <td>F</td>

</tr>

</table>

| A | B | C |
| --- | --- | --- |
| D | E | F |

<table border cellpadding=0 cellspacing=10>

<tr>

<td>A</td> <td>B</td> <td>C</td>

</tr>

<tr>

<td>D</td> <td>E</td> <td>F</td>

</tr>

</table>

| A | B | C |
| --- | --- | --- |
| D | E | F |

<table border cellpadding=10 cellspacing=10>

<tr>

<td>A</td> <td>B</td> <td>C</td>

</tr>

<tr>

<td>D</td> <td>E</td> <td>F</td>

</tr>

</table>

***Tablo içinde birden fazla satır kullanımı *********

| **Ocak****** | **Şubat****** | **Mart****** |
| --- | --- | --- |
| Bu 1. Hücre | 2. Hücre | Diğer hücre, 3. hücre |
| 4. Hücre | ve işte bu 5. hücre | 6. hücre |

<table border>

<tr>

<th>Ocak</th>

<th>Şubat</th>

<th>Mart</th>

</tr>

<tr>

<td>Bu 1. hücre</td>

<td>2. hücre</td>

<td>Diğer hücre,<br>3. hücre</td>

</tr>

<tr>

<td>Cell 4</td>

<td>ve işte bu<br>5. hücre</td>

<td>6. hücre</td>

</tr>

</table>

***Hücrenin sağına, soluna ve ortasına metin yazmak***** **

| **Ocak****** | **Şubat****** | **Mart****** |
| --- | --- | --- |
| Hepsi ortada | 2. hücre | Diğer hücre, 3. hücre |
| sağa yanaşık | merkezde | default, sola yanaşık |

<table border>

<tr>

<th>Ocak</th>

<th>Şubat</th>

<th>Mart</th>

</tr>

<tr align=center>

<td>Hepsi ortada</td>

<td>2. Hücre</td>

<td>Diğer hücre,<br>3. hücre</td>

</tr>

<tr>

<td align=right>sağa yanaşık</td>

<td align=center>merkezde</td>

<td>default,<br>sola yanaşık</td>

</tr>

</table>

## **Form Hazırlama **

Formlar, kullanıcıdan bilgi girişi olduğu zaman bunları okunmaya hazır duruma getirmeye yarar. Diğer bir deyişle, kullanıcı ile programcı arasında bir köprü kurar. Programcıya mail atmak, WWW üzerinden araştırma yapmak, belirli bir anahtar sözcüğü kullanarak arama yapmak, ve hatta telefon bilgi bankalarına girmek form kullanarak halledilir.

Form konusunu anlayabilmek için, HTML programlamayı bilmek ve en azından bir programlama diline ( tercihan shell, PERL veya C ) hakim olmak gereklidir.

Form hazırlanırken aşağıdaki adımlar izlenir :

Programın, form hazırladığımızı bilmesi için, *<form .. *belirteci açılır. Bu belirtecin iki parametresi vardır:

**Method**

"Method", kullanıcının girdiği bilgileri ne şekilde alacağımızı belirler. Bu konunun dışında kalmasına rağmen, POST metodunu kullanmanızı tavsiye ederim.

**Action ******

Bu bölüme, alınan girdileri işleyecek programın ismi yazılır. Bu program ayrı bir cgi-bin/ dizini altında durmalıdır.

Örnek bir form başlangıcı şöyle olabilir:

<form method="POST" action="http://cclub.metu.edu.tr/cgi-bin/postala" >

Şimdi kullanıcının gireceği bilgiler için forma birkaç bölüm ekleyebiliriz. Bunun için aşağıdaki parametreleri kullanan **<INPUT .. > **belirtecine gerek vardır.

**Name ******

Kullanıcının klavyeden girdiği bilgilerin tutulduğu değişken burada tutulur.

**Size ******

Bu sayı, ekranda kullanıcıya ayrılan boşluğun ne uzunlukta olacağını saptar.

**Type**

Anket tipi (burada anlatılmayacaktır)

Örnek bir girdiyi oluşturmak için şu tür bir program yazılabilir.

<INPUT NAME="isim" SIZE=36>

Birden fazla satır kullanma durumunda, farklı bir seçeneği, **<TEXTAREA ...> </TEXTAREA> **seçeneğini kullanmalısınız :

**Name**

Yine aynı değişken ismi.

**Rows**

Bu sayı kullanıcının yazdığı alanın kaç satır olacağını belirler.

**Cols ******

Bu sayı kullanıcının yazdığı alanın kaç sütun olacağını belirler.

<TEXTAREA NAME="body" rows=10 cols=60></TEXTAREA>

Yukarıdaki alana küçük bir metin de yerleştirebilirsiniz.

<TEXTAREA name="body rows=10 cols=60>

Bu metin, kullanıcının yazacağı alanda görüntülenir.

</TEXTAREA>

Neredeyse bitti. Kullanıcının tüm bilgileri girdikten sonra formu ister yollaması, isterse tekrar silmesi için ikon yaratan bir **<input .. **belirtecine gerek vardır. Bu belirtecin aldığı seçenekler,

**Type ******

Kullanılan formun işleme sokulabilmesi için **type **değeri **submit **olmalıdır. Başka bir seçenek de kullanıcının girdiği tüm bilgileri silmektir. Bunun için type'dan sonra **reset **gelmelidir.

**Value**

Buton içine bir mesaj yazacaksanız, bu seçeneği kullanın. Kullanıcıyı bilgilendirmek amacıyla herhangi bir metin yazılabilir.

*Reset *seçeneği, formu tamamen temizlemez, sadece formdaki değerler eski hale dönerler.

Tipik bir örnek:

<input type="submit" value="Bu formu gönder" >

<input type="reset" value="Temizle" >

Artık formun yazılımı bitmiştir. Formun sonuna **</FORM> **belirteci konarak form kapatılır.

Tamamlanmış form ekranda şu halde görünür.

E-mail adresiniz : HTMLCONTROL Forms.HTML:Text.1

İsminiz : HTMLCONTROL Forms.HTML:Text.1

Buraya herhangi bir not yazabilirsiniz:

HTMLCONTROL Forms.HTML:TextArea.1

HTMLCONTROL Forms.HTML:Submitbutton.1 HTMLCONTROL Forms.HTML:Reset.1

<hr>

<p>

<form method="POST"

action="http://cclub.metu.edu.tr/cgi-bin/deneme"><P>

E-mail adresiniz : <INPUT NAME="email" SIZE=38>>/P><P>

İsminiz : <INPUT NAME="name" SIZE=42><P>

Buraya birşeyler yazabilirsiniz: <P>

<TEXTAREA name="body" rows=10 cols=50>Something>/TEXTAREA>

<P>

<input type="submit" value="Gönder">

<input type="reset" value="Temizle"></P>

</FORM>

<p>

<hr>

Yukarıdaki formu doldurup gönderin. Form, cclub.metu.edu.tr adresi üzerinde bir programı çalıştıracaktır. Bu program değişkenlerin ismini ve aldıkları değerleri ekrana basacaktır.

**Kullanıcının yazdığını okuyabilmek **

Bundan sonra kullanıcının forma ne tür bilgiler girdiğini bulmak kaldı. Form bilgilerini okuyabilmek için tercihan perl veya shell bilmek gerekir. Burada örneği verilecek cgi-bin programlarını herhangı bir dilde yazabilirsiniz, buradaki örnekler, hemen herkesin aşina olduğu shell script ile yazılacaktır.

Şimdi aşağıdaki bilgilerin girilmesini isteyen bir form hazırlayalım ve **.html **formatında yazalım.

Haftanın bir günü (gün)

Bir sıfat (sıfat)

Bir fiil (fiil)

Yarattığınız form, cgi-bin dizini altındaki (bu dizine yazma hakkı elde etmeniz gereklidir) form.cgi programını çalıştırsın.

**Bir gün, iki insan ismi, bir sıfat ve bir fiil giriniz..**

Haftanın bir günü HTMLCONTROL Forms.HTML:Text.1

Bir sifat HTMLCONTROL Forms.HTML:Text.1

Bir fiil HTMLCONTROL Forms.HTML:Text.1

HTMLCONTROL Forms.HTML:Submitbutton.1 HTMLCONTROL Forms.HTML:Reset.1

<html>

<title> Form hazırlama </title>

<h3> Bir gün, iki insan ismi, bir sıfat ve bir fiil giriniz..</h3>

<hr>

<form method="POST"

action="http://www.catt.ncsu.edu/cgi-bin/madlib.pl">

<UL>

<LI> Haftanın bir günü <input name="gun">

<LI> Bir sifat <input name="sifat">

<LI> Bir fiil <input name="fiil">

</UL>

<input type="submit" value="Formu postala">

<input type="reset" value="Ekranı temizle">

</form>

</html>

Yukarıda sadece çalıştırılmayı bekleyen bir form hazırladık. Aslında bu haliyle program çalışmayacaktır, çünkü henüz cgi-bin altına yerleştirmemiz gereken shell programımızı (kodu) yazmadık. Yazacağımız kodun amacı, kullanıcının girdiği bilgileri ekranda aynen göstermek.

Kod, programcının isteği doğrultusunda kolayca değiştirilebilir.

\##

\# ayraç.sh

\# Bu program, çağırıldığı zaman, ekrana $STRING\_QUERY değişkeni

\# içindeki değerleri basar. Program, $QUERY\_STRING içindeki değişken

\# sayısını 3 olarak kabul eder.

\##

#!/bin/bash

echo "Content-type: text/plain"

echo

deger=\`echo "$QUERY\_STRING" | awk -F"&" '{ print $1 " " $2 " " $3 }'\`

echo $deger

deger1=\`echo "$deger" | awk '{ print $1 }'\`

deger2=\`echo "$deger" | awk '{ print $2 }'\`

deger3=\`echo "$deger" | awk '{ print $3 }'\`

sabit1=\`echo "$deger1" | awk -F"=" '{print $1}'\`

sabit2=\`echo "$deger2" | awk -F"=" '{print $2}'\`

sabit3=\`echo "$deger3" | awk -F"=" '{print $3}'\`

echo $sabit1 $sabit2 $sabit3

## **Daha geniş bilgi **

Bu döküman sadece HTML programlamaya giriş niteliğindedir. Daha geniş bilgi için aşağıdaki bağlantılara göz gezdirin.

*Başarılar :-)*

Web hakkında bilmek istediğiniz herşey

**HTML hazırlama teknikleri: ******

Composing Good HTML

CERN's style guide

How to write HTML files

**Diğer referanslar ******

A description of SGML

The HTML working group of the IETF

---
*Kaynak: `WEB PROGRAMCISININ EL KİTABI/WEB PROGRAMCISININ EL KİTABI.doc` — ASTEO PC — 2004*
