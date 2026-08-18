# Mini HTML

HTML

HTML dosyası uzantısı .HTM veya .HTML olan web tasarımı için kullanılan dosyadır. Derste, bu tip dosyalar hazırlanırken Başlat/Programlar/Donatılar/Not Defteri(=NotePad) programı kullanılacaktır.

**2.1.1 Yeni Bir HTML Dosyası Hazırlamak******

1. Internet Explorer penceresini açın,

Adres çubuğuna about:blank yazıp **Enter** tuşuna basın.

(Yeni boş bir dosya oluşturulmuştur.)

Bu sayfada farenin sağ tuşuna, boş bir zemini, tıklayın.

Çıkan menüden **Wiew Source/Kaynağı Görüntüle** komutunu verin.

(Bir Not Defteri dosyası açılacaktır.)

Bu programı **Dosya** menüsünden **Farklı Kaydet** i tıklayın.

Dosya adı kendi soyadınız ve uzantısı .HTM veya .HTML olacak biçimde dosyanızı, masa üstünde html adlı bir klasör açıp bu klasörün içine kopyalayın. (Hazır).

## **HTML Kodları******

HTML kodları(=deyimleri,komutları) <> şeklinde ifade edilen işaretlerin arasına yazılan HTML deyimleridir. Hemen hemen her kodun başlangıcı <> ve bitişi </> şeklindedir. Bu ibareler arasında kalan işlemler ilgili komut tarafından icra edilir. Bazı deyimlerin bir veya daha fazla parametresi vardır. Bu parametrelerin hepsi seçimliktir. Yani kullanma zorunluluğu yoktur. Fakat kullanıldığı takdirde deyime zenginlik katar. Ayrıca bu parametrelerin kullanılması için belli bir sıralama yoktur. HTML kodları yazılımında büyük harf küçük harf ayrımı da yoktur, örneğin <BODY>=<body> gibi. Aşağıda verilen örneklerin bir çoğunda büyük harf kullanılmıştır.

**2.1.2 Giriş******

**<HTML></HTML>******

Bütün HTML dosyaları <HTML> kodu ile başlar </HTML> kodu ile biter. Yani Web sayfası ile ilgili tüm deyimler bu iki kodun arasında kalmalıdır.

**<HEAD></HEAD>******

Web sayfası ile ilgili temel özellikler,Sayfa Başlığı, Yazı karakterler kümesi, link özellikleri gibi, burada tanımlanır.Kısaca head kısmında sayfanın nasıl görüntüleneceği gibi bölümler yer alır.Yeri geldikçe bu deyimin kullanımı gösterilecektir.

**<TITLE></TITLE>******

<TITLE> satırında Internet Explorer (=IE) programına sayfaya başlık verilmek istendiği işaret edilmektedir. IE <TITLE> ve </TITLE> arasında yazılan metni pencere başlığı olarak kabul eder. Bu deyimler <HEAD></HEAD> deyimleri arasına yeralır.

**<BODY></BODY>******

Web sayfasında yer alacak asıl bilgiler HTML formatındaki dosyanın <BODY> deyimi belirlenen kısma yazılır. İşlem </BODY> deyimi ile biter. Bu iki deyim arasında herhangi bir metin web sayfasında ekranda aynen görülür.

**<!-- ... -->******

Dosyanın içinde bir açıklama yapmak için kullanılır. Açıklama **...** ile belirlenen kısma yazılır.

Örnek 1: Aşağıdaki örneği bir not defterine yazın ve dosya uzantısını **htm** veya **html** olarak belirleyin.

| <HTML> <HEAD><TITLE>Ornek01.html</TITLE></HEAD> <BODY> Merhaba Dünya!... </BODY> </HTML> |
| --- |

**<BR>******

Bir metin yazılırken bir alt satıra geçmek için kullanılır. Bu deyim kullanılmazsa Tüm işlemler aynı satırdaymış gibi işlem görür. Yani <BR> deyimi Enter tuşunun görevini görür.

**<CENTER></CENTER>******

Bir veya daha fazla satırı sayfa içinde ortalamak için kullanılır.

Örnek 2:

| <HTML> <HEAD><TITLE>Ornek02.html</TITLE></HEAD> <BODY> Gölbaşı<BR>Meslek Yüksek Okulu <!-- Bir yukarıdaki ve bir aşağıdaki satırları dikkatle inceleyin. --> Gölbaşı Meslek Yüksek Okulu <BR> <CENTER> A D I Y A M A N </CENTER> </BODY> </HTML> |
| --- |

**<H?></H?>******

Bu deyim Web sayfasında yazılacak olan metnin puntosunda değişiklik yapmak için kullanılır. ? İşareti yerine 1-5 arası bir rakam gelir. Örneğin,<H1> büyük puntolu yazı yazmak için kullanılır.Sayı değeri büyüdükçe punto küçülür.</H1> ile bitirilir.

**<FONT SIZE=”sayı” COLOR=”renk” FACE=”yazı tipi”></FONT>******

<H?></H?> deyimlerini kullanmak yerine bu deyim kullanılabilir.

Parametreler:

SIZE : Sayfada bulunan bir yazının punto ayarı burada yapılır. Örneğin sayı yerine +4 yazılırsa

FONT deyiminin arasına yazılmış olan metnin boyutu +4 birim daha büyük görülecektir, -2

yazılırsa metin -2 birim daha küçük görülecektir.

COLOR : Yazının rengi burada belirlenir. Red,Blue... gibi

FACE : Yazı tipi ayarlamalarını burada yapılır. Arial, Tahoma... gibi

Örnek 3:

| <HTML> <HEAD><TITLE>Ornek03.html</TITLE></HEAD> <BODY> <CENTER> <!-- 3 punto ile --> <H3> Ecevit CAN </H3> <!-- punto ayarı verilmemiş --> <FONT FACE=”Courier New” COLOR=”Blue”> Ecevit CAN </FONT> <!-- punto ayarı 2 birim azaltılmış --> <FONT COLOR=”Green” SIZE=”-2”> Ecevit CAN </FONT> </CENTER> </BODY> </HTML> |
| --- |

**<B></B>******

Bu iki deyim arasına yazılan metni koyu (=**Bolt**) olarak sayfada gösterilmesini sağlar.

**<U></U>******

Bu iki deyim arasına yazılan metni altıçizili (=Underline) olarak sayfada gösterilmesini sağlar.

**<I></I>******

Bu iki deyim arasına yazılan metni italik (=*Italic*) olarak sayfada gösterilmesini sağlar.

**<SUP></SUP>******

Bu iki deyim arasına yazılan metin üstindis olarak işlem görür.

**<SUB></SUB>******

Bu iki deyim arasına yazılan metin altindis olarak işlem görür.

Örnek 4:

| <HTML> <HEAD><TITLE>Ornek04.html</TITLE></HEAD> <BODY> <CENTER> <B>Bu metin koyu </B><BR> <I>Bu metin italik</I><BR> <U>Bu metin altıçizili</U><BR> <B><I>Bu metin koyu ve italik</I></B><BR><BR> </CENTER> a kare + ab kare = a<SUP>2</SUP> + b<SUP>2</SUP><BR> x1 + x2 = x<SUB>1</SUB> + x<SUB>2</SUB> </BODY> </HTML> |
| --- |

## **2.1.3 Paragraf Biçimlendirme******

**<PRE></PRE>******

Web sayfasında yazılan kelimelerin arasında yalnız bir boşluk vardır. Ayrıca bir alt satıra geçerken <BR> deyiminin kullanılması gerektiği daha önce bahsedilmişti. Web sayfasında yazdığınız metnin NodPad e yazdığınız formatta görünmesi için bu deyim kullanılır.

Örnek 5:

| <HTML> <HEAD> <TITLE>Ornek05.html</TITLE> </HEAD> <BODY> Ecevit CAN <!-- Yazı tipinin varsayılan değeri Courier New dir.--> <PRE> Ecevit CAN </PRE> </BODY> </HTML> |
| --- |

**<P ALIGN=”Right|Left|Center”></P>******

Eğer uzun bir metin birden fazla paragrafla belirlenmek istenirse paragrafın başına ve sonuna bu deyimler yazılır.

Parametreler:

ALIGN : Paragrafın tipini belirler.Örneğin <P ALIGN=”Right”> olarak kullanılırsa paragraf

sağa dayalı yazılır.<P ALIGN=”Left”> sola dayalı olarak ve <P ALIGN=”Center”>

paragraf ortalanarak sayfada görüntülenir.

Örnek 6:

| <HTML> <HEAD><TITLE>Ornek06.html</TITLE></HEAD> <BODY> <P ALIGN=”RIGHT”>HTML de font ayarları SIZE ile yazılan metnin punto ayarı yapılabilir. sayı, +5 olarak seçilirse yazı büyüklüğünün 5 punto kadar arttır anlamındadır.-5 seçilseydi 5 birim azalt anlamındadır. COLOR ile yazının rengi belirlenir. Renk ingilizce renk adlarından biri olmalıdır, yellow gibi. FACE ile yazı tipi belirlenebilir. Bu üç parametre seçimliktir ve sırası önemli değildir. İstenilen parametre kullanılabilir. </P> <P><B>Ecevit CAN</B></P> <BR> <H2> <I>Gölbaşı </I><U>MYO</U> </H2> </BODY> </HTML> |
| --- |

**2.1.4 Sayfanın Artalanını Belirleme******

Bu işlem <BODY> deyiminin parametreleri kullanılarak yapılır. Daha önce <BODY> deyimini kullanırken bu parametrelerden bahsedilmemişti.

**i) Artalan Rengini Belirleme******

**<BODY BGCOLOR=”renk”></BODY>******

Renk kısmına sayfanın istenilen artalan rengi yazılır. Bu renkler ingilizce renk isimleri olmalıdır.

Örneğin: Blue, Black, Green, Yellow, Red, Gray, Cyan... gibi.

**<BODY BGCOLOR=”#kkyymm”></BODY>******

Yukarıdaki kısımda kullanacağınız renk sayısı sınırlıdır. Dolayısıyla Aradığınız renk tonu yukarıdaki özellikte bulamayabilirsiniz. doğada bulunan üç ana renk kırmızı,yeşil,mavi dir. Tüm renkler bu renklerin karışımından elde edilebilir. #kkyymm ifadesini kullanarak bir k-y-m renklerinden bir karışım elde edebilirsiniz. Burada kk,yy,mm ifadeleri birer rakama karşılık gelmektedir. Örneğin #990000 tam olarak kırmızı renge karşılıktır. Renk tonu ayarları bu rakamlar aracılığı ile yapılır. Bazen bir renk tamamen kullanılacaksa, yani ilgili pozisyona 9 konacaksa, F(=Full) kullanılabilir. Örneğin;

#FF15FF = #991599, #0F5FFF = #095999 gibi.(yaklaşık olarak!)

Örnek 7:

| <HTML> <HEAD><TITLE>Ornek07.html</TITLE></HEAD> <BODY BGCOLOR=”#FF00FF”> <!-- Artalan Mor renk olarak seçildi. --> <CENTER><FONT COLOR=”WHITE” SIZE=”3”>MERHABA DUNYA!..</FONT></CENTER> </BODY> </HTML> |
| --- |

**ii) Artalana Resim Ekleme******

**<BODY BACKGROUND=”file://artalana\_konacak\_olan\_resmi\_ konumu”></BODY>******

Artalanı belli bir renkte boyamak yerine, artalana konumu bilinen bir resim dosyası eklenebilir. Bu dosyaların uzantıları .GIF,.JPG,.JPEG veya .BMP olmalıdır.

Örnek 8:

| <HTML> <HEAD><TITLE>Ornek08.html</TITLE></HEAD> <BODY BACKGROUND=”File:///a:/resimler/artalan.gif”> <!-- Diskette bulunan bir resim artalan olarak görüntüleniyor... --> <P ALIGN=”Center”><B>Ecevit CAN</B></P> </BODY> </HTML> |
| --- |

## **2.1.5 Sayfaya Yatay Çizgi Ekleme******

**<HR WIDTH=”uzunluk” COLOR=”renk” SIZE=”yükseklik” NOSHADE>******

Web sayfasına belli bir uzunlukta,renkte ve boyutta yatay bir çizgi çizmek için kullanılır.

Parametreler:

WIDTH : Sayfada bulunan yatay çizginin uzunluğunu piksel veya % olarak burada belirlenir.

Piksel ekrandaki nokta sayısı ile ilgilidir. % ise ekrandaki bir satırı kaplama oranıdır.

Örneğin 80% bir satırın %80 ni kaplayacak şekilde bir yatay çizgiyi işaret eder.

SIZE : Çizginin kalınlığı burada ayarlanır. 1-5 arası değerler kullanılır.

COLOR : Yatay çizginin rengi burada belirlenir.

NOSHADE : Yukarıdaki 3 durumda da çizginin bir gölgesi vardır. Bu parametre kullanılırsa yatay

çizginin gölgesi ortadan kalkar.

Örnek 9:

| <HTML> <HEAD><TITLE>Ornek09.html</TITLE></HEAD> <BODY BGCOLOR=”#000000”> <HR> <HR WIDTH=”75%” NOSHADE> <CENTER><FONT COLOR=”White” FACE=”Arial”>ECEVİT CAN...</FONT> <HR COLOR=”#F0FF09” WIDTH=”200” SIZE=”2” NOSHADE> <HR COLOR=”White” WIDTH=”200” SIZE=”2”> </CENTER> </BODY> </HTML> |
| --- |

## **2.1.6 Sayfaya Resim Ekleme******

**<IMG SRC=”file://dosya” WIDTH=”genişlik” HEIGHT=”yükseklik” ******

** ALT=”açıklama” BORDER=”sınır”>******

Web sayfası içinde resim dosyası yerleştirmek için bu deyim kullanılır.

Parametreler:

SCR : file:// dan sonra sayfaya eklenecek olan resim dosyasının konumu yazılır.

WIDTH : Sayfaya eklenmiş olan resmin eninin ebatları piksel veya % olarak burada belirlenir.

HEIGHT : Sayfaya eklenmiş olan resmin boyunun ebatları piksel veya % olarak burada belirlenir.

ALT : Sayfaya eklenmiş olan resmin fare ile üzerine gelindiğinde, açıklama amaçlı bir yazı

göstermek için kullanılır.

BORDER : Sayfaya eklenmiş olan resme kenarlık vermek için kullanılır. Sınır (0-6) arası.

Örnek 10:

| <HTML> <HEAD><TITLE>Ornek10.html</TITLE></HEAD> <BODY> <BR>...RESiMLERiM...<BR> <!-- diskette bulunan birkaç resmin eklenmesi --> <IMG SRC=”File:///a:/resimler/resim1.jpg” ALT=”Gölbaşı”><BR> <IMG SRC=”File:///a:/resimler/resim2.gif” WIDTH=”60” HEIGHT=”30%”><BR> <IMG SRC=”File:///a:/resimler/resim3.gif” ALT=”MYO” WIDTH=”100” BORDER=”1”> </BODY> </HTML> |
| --- |

## **2.1.7 Sayfaya Madde işaretleri(=İmleri) Ekleme******

**<UL>,<OL> ve <LI>******

Web sayfası dahilinde liste hazırlarken bu deyimler listeleme özelliğini başlatmaktadır. Eğer listede bulunan maddelerin başına büyükçe bir noktanın konulması isteniyorsa <UL> deyimi kullanılmalıdır. Listedeki maddeleri numaralı sıralamak için <OL> değimi kullanılır. Madde olarak kullanılacak her satır <LI> deyimi ile başlayıp </LI> deyimi ile bitmelidir.

**<UL TYPE=”DISC|CIRCLE|SQUARE”></UL> ******

Bir listede bulunan maddelerin başına büyükçe bir nokta,küçük bir çember veya içi dolu bir kare işareti koymak için kullanılır.

Parametreler:

TYPE : Listedeki maddelerin başına konacak olan işaret tipi burada belirlenir. Notka için DISC, içi

boş bir nokta için CIRCLE ve kare işareti için SQUARE deyimleri kullanılır.Bir şey

belirtilmezse varsayılan değer noktadır.

Örnek 11:

| <HTML> <HEAD><TITLE>Ornek11.html</TITLE></HEAD> <!-- maddelerin yanına büyük nokta koyar --> <BODY BGCOLOR=”#00FFFF”> <U>TÜRKİYE 1.FUTBOL LIGINDEDE ŞAMPİYON OLAN TAKIMLAR</U> <UL TYPE=”disc”> <LI> Galatasaray SK 14 kez </LI> <LI> Fenerbahçe SK 13 kez </LI> <LI> Beşiktaş JK 9 kez </LI> <LI> Trabzonspor SK 6 kez </LI> </UL> </BODY> </HTML> |
| --- |

**<OL TYPE=” A|a|I|i|1” START=”sayı”></OL>******

Bir listedeki maddeleri numaralı olarak sıralamak için kullanılır.

Parametreler:

TYPE : Listedeki maddelerin sıralanma tipleri burada belirlenir. Örneğin <OL TYPE=”a”>

kullanılırsa maddeler a,b,c.. şeklinde sıralanır. TYPE belirtilmezse varsayılan değer 1,2,3...

START : Sıralamaya kaçıncı maddeden başlanacağı burada belirlenir.

Örnek 12:

| <HTML> <HEAD><TITLE>Ornek12.html</TITLE></HEAD> <!-- Maddeler Romen rakamı ile sıralanır. --> <BODY> <CENTER> TÜRKİYE 1.FUTBOL LIGINDEDE ŞAMPİYON OLAN TAKIMLAR <!-- Sıralama Romen rakamı ile III(=3) başlanarak sıralanır --> <OL TYPE=”I” START=”3”> <LI> Galatasaray SK 14 kez </LI> <LI> Fenerbahçe SK 13 kez </LI> <LI> Beşiktaş JK 9 kez </LI> <LI> Trabzonspor SK 6 kez </LI> </OL> </CENTER> </BODY> </HTML> |
| --- |

**2.1.8 Sayfaya Tablo Ekleme******

**<TABLE>,<TR> ve <TD>******

Bu deyim sayesinde web sayfalarında tablolar hazırlanabilir. Bu deyim <TD> ve <TR> deyimleri ile birlikte kullanılmalıdır. <TR> satır , <TD> tablonun satırlarının içindeki işlemler için kullanılır.

**<TABLE BORDER=”sınır” WIDTH=”en” HEIGHT=”boy”></TABLE>******

<TABLE></TABLE> deyimleri tablonun başlangıcını ve bitişini gösterir. Unutmayın! bütün parametreleri kullanmak zorunda değilsiniz.

Parametreler:

BORDER : Tabloyu oluşturan çerçevenin kalınlığı burada belirlenir.sınır ifadesi 1-5 arası bir sayıya

karşılık gelir.

WIDTH : Tüm tablonun ister piksel ister % olarak genişliği.

HEIGHT : Tüm tablonun ister piksel ister % olarak yüksekliği.

**<TR></TR>******

Tablonun satırlarında yapılacak olan işlemlerde bu deyim kullanılır. Her satır için farklı işlem yürütülebilir.

**<TD BGCOLOR=”renk” ALIGN=”LEFT|RIGTH|CENTER”></TD>******

Tablo hücrelerini düzenlemek için kullanılır. <TR></TR> deyimleri arasına yazılmalıdır.

Parametreler:

ALIGN : Tablo içine yazılan metnin biçimi belirlenir. Sağa dayalı, ortalı gibi.

BGCOLOR : Tablo hücrelerinin artalan rengi burada belirlenir.

Örnek 13:

| <html> <head><title>Ornek13.html</title></head> <body> <table border="3"> <tr> <td>Adı soyadı </td> <td>Numarası </td> <td>Notu</td> </tr> <tr> <td>Ali Çalışkan</td> <td>2001 </td> <td>75 </td> </tr> <tr> <td bgcolor=”Yellow”>Mehmet Zafer</td> <td>2054 </td> <td>96 </td> </tr> </table> </body> </html> |
| --- |

Örnek 14:

| <html> <head><title>Ornek14.html</title></head> <body bgcolor="#000000"> <center> <table border="0" width="80%" height="100%"> <tr> <td bgcolor="#909090"> <font color="#000080" size="5"> <b>Web Sayfama Hoş Geldiniz..</b> </font> </td> </tr> </center> </table> </body> </html> |
| --- |

## **2.1.9 Sayfalara e-mail Adresi Ekleme******

**<A HREF=”mailto:e-mail\_adresi”></A>******

Web sayfasında e-posta (=elektronik posta) adresi eklemek için <A> ve HREF deyimlerini kullanmak gerekir.

Örnek 15:

| <HTML> <HEAD><TITLE>Ornek15.html</TITLE></HEAD> <BODY> <a href=”mailto:ecevitcan@mailsurf.com”>E-Mail</a> </BODY> </HTML> |
| --- |

## **2.1.10 Başka Web Sitelerine Geçiş******

**<A HREF=”http://bağlantı\_kurulacak\_olan\_sayfanın\_adresi”></A>******

Bir kişi veya kurumun web sitesine hazırladığınız web sayfasından bağlantı kurmak için yine <A> ve HREF deyimleri kullanılır.

Örnek 16:

| <HTML> <HEAD><TITLE>Ornek16.html</TITLE></HEAD> <BODY> <A HREF=”http://www.gantep.edu.tr”>Gaziantep Üniversitesi</A><BR> Gölbaşı MYO sayfasını <A HREF=”http://www.golbasimyo.8m.com”>tıklayın</A> </BODY> </HTML> |
| --- |

## **2.1.11 Başka HTML/Text dosyalarına Bağlantı Kurma******

Daha evvelden hazırlamış olduğunuz HTML dosyalarına bağlantı kurmak için yine <A> ve HREF deyimleri kullanılır. Bağlantı kurulacak dosyanın uzantısı txt, htm veya html olabilir. Bunun için;

**<A HREF=”file://dosyanın\_konumu”></A>******

file:// ile belirtilen yerden sonra bağlantı kurmak istediğiniz dosyanın konumu yazılır.

Örnek 17: Bu örnekten önce masaüstüne Dosya1.html ve Dosya2.txt adlı dosyaları oluşturun.

| <HTML> <HEAD><TITLE>Ornek17.html</TITLE></HEAD> <BODY> <A HREF=”file:///c:/windows/desktop/Dosya1.html”>Dosya1</A><BR> <A HREF=”file:///c:/windows/desktop/Dosya2.txt”> Dosya2</A> <!-- Eğer ornek16.html ve bağlantı kurulacak dosya aynı klasörde olursa HREF deyiminden hemen sonra dosyanın adını yazmak yeterlidir. --> <A HREF=”ornek15.html”>15. Örnek</A> </BODY> </HTML> |
| --- |

## **2.1.12 Bağlantı (Link) Özelliklerini Ayarlama******

**i) Link Renklerinin Ayarları******

Yukarıdaki iki örnekte Web sayfanızda linklerin renkleri altı çizili ve mavi renktedir. Bir siteyi ziyaret ettiğinizde IE ziyaret edilen bu sitenin link rengini eflatun renginde gösterir. Kendi sayfanızda bulunan linkleri rengini ayarlayabilirsiniz. Bunun için <BODY> deyiminin aşağıda verilen özelliklerini inceleyin.

**<BODY LINK=”link” ALINK=”aktif\_link” VLINK=”ziyaret\_edilen\_link”></BODY>******

Parametreler:

LINK : Sayfada bulunan linklerin ayarlamaları burada yapılır.

ALINK : Fare ile link tıklandığında link in alacağı renk burada belirlenir.

VLINK : Eğer bir link daha önce ziyaret edilmişse, o sitenin ziyaret edildiğini gösteren renk ayarı

burada yapılır.

Örnek 18:

| <HTML> <HEAD><TITLE>Ornek18.html</TITLE></HEAD> <BODY BGCOLOR=”Black” LINK=”Yellow” VLINK=”White” ALINK=”Gray”> <BR><A HREF=”http://www.metu.edu.tr”>ODTU</A> <BR><A HREF=”http://www.microsoft.com”>Microsoft</A> <BR><A HREF=”mailto:ecevitcan@mailsurf.com”>E-Mail</A> </BODY> </HTML> |
| --- |

**ii) Linklerin Altı Çizili Özelliğini Kaldıra******

Sayfanızda bulunan linklerin altı çizili özelliğini kaldırma işlemi <HEAD></HEAD> deyimleri arasına aşağıda verilen kodları yazmalısınız. Ayrıca bu deyimlerle altı çizili özelliği fare *linkin üzerine geldiğinde*, link altı çizili, üstü çizili veya altı-üstü çizili duruma getirilebilir.

**<style>******

**A:link { color : renk; text-decoration :none|underline }******

**A:active { color : renk; text-decoration :none|underline }******

**A:visited { color : renk; text-decoration :none|underline }******

**A:hover { color : renk; text-decoration :none|underline|overline }******

**</style>******

Parametreler:

link : Sayfada bulunan bir link renk ve durumu

active : Link tıklandığında alacağı renk ve durum

visited : Ziyaret edilmiş bir linkin alacağı renk ve durum

hover : Fare ile linkin üzerine gelindiğinde özelliklerinin işleme konulması. Örneğin

*fare* *linkin üzerine geldiğinde* altı çizili olması isteniyorsa hover kısmında

underline seçilmelidir. Üstü çizili olması için overline seçilmelidir. Hem

altı hem üstü çizili olması için *iki tane* hover kullanılmalıdır.

color : Linklerin, ziyaret edilen linklerin.. renk özelliğinin ayarlanması burada

yapılır.

text-decoration : Bu kısımda linkin tipi belirlenir. Fare linkin üzerine geldiğinde, linkin

alacağı durum burada ayarlanır. none seçilirse ilgili linkin altı çizili özelliği

ortadan kalkar. underline seçilirse ilgili linkin altı çizili özelliği devam

eder.

Örnek 19:

| <html> <head> <style> A:link { color : Yellow; text-decoration :none } A:active { color : Yellow; text-decoration :none } A:visited { color : White; text-decoration :none } A:hover { color : Yellow; text-decoration :underline} A:hover { color : Yellow; text-decoration :overline } </style> <title>Ornek19.html</title> </head> <body bgcolor=”#000080”> <a href=”http://www.gantep.edu.tr”>Gaziantep Üniversitesi</a> </body> </html> |
| --- |

**ii) Aynı Sayfa İçinde Bağlantı Kurma******

Web sayfalarında birbirine bağlı konular aynı sayfa içinde yer alabilir. Bu konular başka sayfalara geçmeden *aynı sayfa içinde* birbirleri için link oluşturulabilir. Bunun için yine <A> deyimi kullanılır. Çok uzun metinlerde kullanılması kolaylık sağlar.

**<A HREF=”#isim”></A>******

Aynı sayfa içinde link yapılırken link burada bir adres veya dosya değildir. Sadece fare ile link e tıklandığında aynı sayfa içinde, link bizi başka bir yere yönlendirecektir(=gönderecektir). Bu işlem sayfa içinde gidilecek olan yere bir isim vermekle yapılır.

**<A NAME=”isim”></A>******

Link e tıklandığında sayfada gidilecek yer burasıdır. Dikkat linkdeki isimle gideceği yer ismi aynı olmalıdır. Aksi takdirde bağlantı kurulamaz.

Örnek 20:

| <HTML> <HEAD><TITLE>Ornek20.html</TITLE></HEAD> <BODY> <a name="BAS">İÇİNDEKİLER</a><br><br><br><br><br> <ul> <li><a href="#Bolum1">Bolum1</a> <li><a href="#Bolum2">Bolum2</a> <li><a href="#Bolum3">Bolum3</a> </ul> <br><br><br><br><br><br><br><br><br><br><br><br> <hr> <a name="Bolum1">Burası Bolum1</a> <a href="#BAS">Başa Dön</a> <hr><br><br> <a name=”Bolum2”>Burası Bolum2</a> <a href="#BAS">Başa Dön</a> <hr><br><br> <a name=”Bolum3”>Burası Bolum3</a> <a href="#BAS”>Başa Dön</a> </BODY> </HTML> |
| --- |

## **2.1.13 Sayfaya Çerçeve(Frame) Özelliği Kazandırma******

Web sayfalarının bir çoğu ikiye bazen üçe bölünmüş olarak görülür. FRAMESET deyimi aynı IE penceresinde birden fazla IE penceresi ile çalışma imkanı verir. Bu şekilde daha aktif bir Web sayfası hazırlanabilir. Ana sayfanızı 2 veya 3 e bölmek için BODY deyimi yerine FRAMESET deyimi kullanılmalıdır.

**<FRAMESET ROWS|COLS=”?,\*” BORDER=”?”></FRAMESET>******

Aynı pencerede birden çok sayfayı kontrol etmek için kullanılır. FRAMESET deyimi kullandığınızda BODY deyimi kullanılmaz.

Parametreler:

ROWS : Web sayfasını yatay olarak bölmek için kullanılır. ROWS=”100,\*” seçilirse yukarıdan

itibaren 100 piksel ayrılır ve yatay bir çizgi ile sayfa ikiye bölünür.

COLS : Web sayfasını dikey olarak bölmek için kullanılır.

BORDER : Sayfa bölündüğünde ortaya çıkan çizginin kalınlığı burada ayarlanır. ? yerine 0-5 arası bir

rakam gelir.

**<FRAME SCR=”dosyaadı” NAME=”çerçeve\_ismi” SCROLLING=”YES|NO|AUTO” NORESIZE>******

<FRAMESET></FRAMESET> deyimleri arasında belirlenen çerçevelerin formatları bu deyimle yapılır.

Parametreler:

SRC : Ana sayfa açıldığında daha önce belirlenmiş yere bağlantı kurulacak olan dosyanın

adı.

NAME : İlgili çerçevenin ismi.

SCROLLING : Ana sayfa açıldığında sayfalar pencereye sığması veya sığmaması ayarı burada

yapılır.

NORESIZE : Ana sayfadaki diğer sayfaları bölen pencereleri ayıran çizginin üstüne gelindiğinde

bu çizginin fare ile ebatlarının değiştirildiği görülür. Kullanıcıya bu izni vermek

istemiyorsanız bu deyimi de eklemelisiniz.

Örnek 21: Bu örnekten önce masaüstüne sayfa1.html, sayfa2.html ve sayfa3.html adlı

dosyaları oluşturun. Bu örneği de masaüstüne index.html olarak kaydedin. Yada bu üç

dosya aynı klasöre kaydedin.

| <HTML> <HEAD><TITLE>Ornek21.html,index1.html</TITLE></HEAD> <Frameset Cols="150,\*"> <!-- İlk yazılan Frame deyimi sol olarak kabul edilir. --> <Frame Src="sayfa1.html" name="Sol" Noresize> <Frame Src="sayfa2.html" name="Sag"> </Frameset> </HTML> |
| --- |

Örnek 22 : Bir sayfanın 3 e bölünmesi

| <HTML> <HEAD><TITLE>Ornek21.html</TITLE></HEAD> <FRAMESET COLS="100,\*"> <FRAME SRC="sayfa1.html" NAME="Sol"> <FRAMESET ROWS="150,\*"> <FRAME SRC="sayfa2.html" NAME="SagUst"> <FRAME SRC="sayfa3.html" NAME="SagAlt"> </FRAMESET> </FRAMESET> </HTML> |
| --- |

## **Bir Çerçeveden Diğerine Bağlantı******

**<A HREF=”URL” TARGET=”Hedef\_Çerçeve”></A>******

Bir çok web sayfasında sol çerçevede bulunan bir linkin etkisini sağ tarafta görülür. Bu özelliği kazandırmak için <A> ve HREF in yanında TARGET parametresi de kullanılmalıdır.

Parametreler:

TARGET : Bağlantı etkisinin görüleceği çerçevenin ismi burada yazılır. TARGET kullanılmazsa link

aynı pencerede açılacaktır. Fakat Hedef\_Çerçeve yerine mevcut çerçeve isimlerinden

başka bir isim yazılırsa link, için başka bir IE penceresi açılır.

Örnek 23: Burada sayfa1.html, sayfa2.html,sayfa3.html ve index.html dosyalarının içerikleri de belirlenmiştir. Bu 4 dosyayı aynı klasörün içine kopyalayın. Böylece link yapılırken dos-

ya yollarını belirtmek zorunda kalmayacaksınız.

| <HTML> <HEAD><TITLE>Ornek23.html,index2.html</TITLE></HEAD> <Frameset Cols="150,\*"> <Frame Src="sayfa1.htm" name="Sol" Noresize> <Frame Src="sayfa2.html" name="Sag"> </Frameset> </HTML> |
| --- |

| <HTML> <HEAD><TITLE>sayfa1.html</TITLE></HEAD> <BODY> SAYFA1 <A HREF=”http://www.gantep.edu.tr” TARGET=”disari”>Gaziantep</A> <A HREF=”sayfa3.html” TARGET=”Sag”>Sayfa3</A> <A HREF=”http://www.golbasimyo.8m.com”>Gölbaşı MYO</A> </BODY> </HTML> |
| --- |

| <HTML> <HEAD><TITLE>sayfa2.html</TITLE></HEAD> <BODY> <P ALIGN=”CENTER”>SAYFA2</P> <!-- Dikkat Target belirtilmemiş --> <A HREF=”sayfa3.html”>Sayfa3</A> </BODY> </HTML> |
| --- |

| <HTML> <HEAD><TITLE>sayfa3.html</TITLE></HEAD> <BODY> <P ALIGN=”CENTER”>SAYFA3</P> <A HREF=”sayfa2.html”>Sayfa2</A> </BODY> </HTML> |
| --- |

---
*Kaynak: `MİNİ HTML/ekitap-Anonim-Mini_HTML_Dersi.doc` — Guest — 2002*
