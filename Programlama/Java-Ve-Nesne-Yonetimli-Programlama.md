# Java & Nesne Yönetimli Programlama

**Java & Nesne Yönelimli Programlama**

**Hafta 5 Ders Notları (6 Nisan 2002)**

**İçindekiler**

** ** 1.Soyut(Abstract) Sınıflar 1

2.Arabirim(Interface) Sınıfları 2

3. Paketler 2

4. Grafikler 3

4.a Renk 4

4.b Çizim 4

4.c Font ve Yazı 4

4.d Bütün Grafik Konularını İçeren Bir Applet Örneği 5

## *** 1.Soyut(Abstract) Sınıflar***

Soyut sınıflar, tüm alt sınıfları tarafından paylaşılacak metodların tanımlarını içeren sınıflardır. Soyut sınıflar içeriği belirlenmemiş sadece etiketi(C’deki prototip belirtimi gibi) belli bir ya da daha fazla soyut metod içerirler. Bu metodların içeriklerine alt sınıflarda bindirme (override) yapılarak içerik kazandırılır. Bir soyut sınıftan türeyen tüm alt sınıflarda bu soyut metodlara bindirme yapılmalıdır. Bir soyut sınıf tamamlanmamış olduğu için nesne haline getirilemez. Mutlaka “extends” anahtar sözcüğü ile yeni sınıflara miras bırakarak kullanılmalıdır. Kısaca bir sınıf isminden önce “abstract” kelimesi vars o sınıf soyuttur ve ve en az bir adet “abstract” tanımlı metod içermelidir.

Aşağıdaki örneklerde sekil soyut sınıfından önce noktaX türetilmiş ve soyut metod olan isimoku()’nun içeriği noktaX’de tanımlanmıştır. noktaX’den daireX’e, daireX’ten de silindirX’e miras kalan isimoku()’nun içeriği hepsinde farklıdır. Demo programında bu üç farklı sınıftan türeyen üç farklı nesne, soyut sınıf tipinde oluşturumuş diziye atanabilmiştir. Kısaca üç farklı nesne tek çatı altında toplanmıştır. Hepsi de isimoku(),alan() ve hacim() metodlarına cevap verebilmiştir. Diğer bir örnekle bir bisiklet, bir otomobil ve bir tır aynı garajda toplanmış ve üçüne de “kornaya bas” emri verildiğinde kendi tarzlarında aynı anda kornayı çalmışlardır.

| ***sekil.java*** | ***noktaX.java*** |
| --- | --- |
| *public abstract class sekil {* * public double alan() {return 0.0;}* * public double hacim() {return 0.0;}* *** public abstract String isimoku();*** *}* | *public class noktaX extends sekil {* * protected double x,y;* * public noktaX(double a,double b) {* * x = a; y = b; * * }* *** public String isimoku() {return "Nokta";}*** * }* |
| ***daireX.java*** | ***silindirX.java*** |
| *public class daireX extends noktaX{* * protected double yaricap;* * public daireX(double a, double b, double r) {* * super(a,b);* * yaricap=r;* * }* *** public String isimoku(){ return "Daire";} *** * public double alan() {return Math.PI\*Math.pow(yaricap,2);}* *}* | *public class silindirX extends daireX{* * protected double yukseklik;* * public silindirX(double a, double b, double r, double h) {* * super(a,b,r);* * yukseklik=h;* * }* *** public String isimoku(){ return "Silindir";} *** * public double alan() {return 2\*super.alan() + yukseklik \* 2\*Math.PI\*yaricap;}* * public double hacim() {return super.alan() \* yukseklik;}}* |
| ***soyutdemo.java*** | **Çıktı** |
| *class soyutdemo { * * public static void main(String args\[\]) {* * sekil sekiller\[\]=new sekil\[3\];* * noktaX n;* * daireX d;* * silindirX s;* * n=new noktaX(2.0, 1.0);* * d=new daireX(3.0, 4.0, 10.0);* * s=new silindirX(2.0, 4.0, 3.0, 4.0);* * sekiller\[0\]=n;* * sekiller\[1\]=d;* * sekiller\[2\]=s;* * int i; * * for(i=0;i<sekiller.length;i++) {* * System.out.println("Nesne....: " + sekiller\[i\].isimoku()+ " "+sekiller\[i\].alan() + " " +sekiller\[i\].hacim());* * } } }* | C:\\java\\prog\\java soyutdemo Nesne….: Nokta 0.0 0.0 Nesne….: Daire 314.15 0.0 Nesne….: Silindir 131.95 113.09 |

## *** 2.Arabirim(Interface) Sınıfları***

Soyut sınıflarda ve miras konusunda görüldüğü gibi tek bir sınıftan kalıtım mümkün oluyordu. Fazla sayıda sınıftan farklı özellikleri aynı anda almak için interface(arabirim) sınıfları mevcuttur. Arabirim sınıflarında hiçbir metodun içeriği yazılmaz, içerikler altsınıflarda oluşturulur. Altsınıflar arabirim sınıflarını “implements” sözcüğü ile çağırırlar. Kısaca arabirim sınıfları “interface” kelimesi ile tanımlanır(class ibaresi geçmez), ve bu arabirimi kullanacak altsınıflarda sınıf adından sonra “implements” kelimesi ve ardından arabirim sınıfının adı gelir. Örneğin sekil sınıfı arabirim sınıfı, noktaY sınıfı da onu kullanan altsınıf olsun. Gösterimleri aşağıdaki gibi olacaktır.

| *interface nehaber{* *String isimoku(); * *}* | *class dene implements nehaber {* *String isimoku() { // Burada içerik var * *}}* |
| --- | --- |

Miras ve arabirimler birarada kullanılabilirler, Bunun en güzel örneği grafik kullanıcı arayüz programlarıdır. Aşağıdaki applet sınıfı tanımını inceleyiniz.

*public class goster extends Applet implements ActionListener, MouseListener, ItemListener {*

Görüldüğü gibi sadece tek sınıftan(Applet) miras alabiliyor ama birden fazla arabirim sınıfını kullanabiliyor.

## *** 3. Paketler***

Daha önceden bazı programlarda import deyimi ile java.awt.\*; java.applet.Applet; gibi bildirimleri programların başında yazmıştık. Bunları C’deki include veya Pascal’daki unit ile yüklenen kütüphanelere benzer olduğunu söylemiştik. Hatta aynı dizinde iki ayrı dosyada bulunan iki sınıftan biri diğerini kullanıyorsa import deyimi kullanmaya gerek olmadığı belirtilmişti. Çünkü java bir dizin içindeki tüm dosyaları tarayabilme ve gerekirse kullanabilme yeteneğine sahiptir.

Java’da benzer işleri yapacak sınıflar karışıklığı önlemek ve sonradan kolayca kullanabilmek maksadıyla paketlenebilirler. Diyelim ki, bir fourier transformu yapan metodunuz var ve yüzlerce sınıfınız veya dosyanız içinde herhangi birisinde. Bunun nerede olduğunu aramak dakikaları alabilir. Eğer bu yüzlerce sınıf paketlernirse kullanıcının artık kullanacağı metodun hangi sınıfta olduğunu bilmesine gerek kalmayacaktır. Sadece paketin adını “import” kelimesi ile çağırması yeterli olacaktır. Bu aşamada, bir paketin nasıl oluşturulduğunu ve kullanıldığını göreceğiz.

Bir paketin import edilerek sınıflarının kullanılabilmesi için sınıfların “public” tanımlanması gereklidir. main() metodu içeren bir sınıf ise public olmasa bile başka bir yöntemle çalıştırılabilir. Paketlerin ve çalıştırılacak sınıfların birbirini görmesi ve tanıması için aynı sınıf yoluna bağlı olmaları gerekir. Javada sınıfyolu(classpath) adı verilen yol bu işi görür. Oluşturduğunuz paketi ve sınıfların olduğu dizini bu yola eklemek için komut satırında

*C:\\ CLASSPATH=%CLASSPATH%; c:\\jdk1.3\\prog\\paketim\\ *

gibi bir satır yazılması gerekebilir.

Javada paket olacak sınıflar bir diine toplanır ve tüm dosyaların en başına “package” kelimesinden sonra o dizinin yani paketin adı yazılır. “package” kelimesi bir dosyada ilk ifade olmak zorudundadır. Örneğimizde oluşturacağımız paketin adı : “paketim”. Bu nedenle prog çalışma dizinimiz altında paketim adında bir dizin oluşturmalıyız. Paketim dizininin altında paket sınıfları olacak paket0 ve paket00’ı içeren paket0.java programını yazarız. Dosya ismi olarak paket0.java verildi çünkü paket0 sınıfı public bir sınıf olup, eğer bir dosyada public bir sınıf varsa dosya o isimde kaydedilir. Eğer yoksa main() metodu içeren sınıfa bakılmalıdır ve varsa onun isminde kaydedilmelidir.

| ***paket0.java*** | ***callpaket.java*** |
| --- | --- |
| *package paketim;* *public class paket0 {* *public paket0() {* *System.out.println("merhaba");* *}* *}* *class paket00 {* *public static void main(String args\[\]) {* *System.out.println("pakettesin...");* *}* *}* | *import paketim.\*;* *class callpaket {* *public static void main(String args\[\]) { * *paket0 p0=new paket0();* *}* *}* |
| *C:\\java\\prog\\paketim\\javac paket0.java* *C:\\java\\prog\\java paketim.paket00* *pakettesin * | *C:\\java\\progjava\\javac callpaket.java* *C:\\java\\progjava \\java callpaket* *merhaba* |

Yukarıda görüldüğü gibi main metodu içeren paket00 sınıfı java komutu ile başına paketin ismi getirilerek çalıştırılmıştır. Public olan paket0 sınıfı ise callpaket adlı programda import ile yüklenip daha sonra çağırılınca kurucu metodu çalışmıştır.

## *** 4. Grafikler***

Javada grafik çizim kütüphanesi geniştir ve çizim daha kolaydır. Applet direk Graphics sınıfı ile çalıştığı için applet yüzeyi çizim alanı olur. Koordinat sistemi kullanımı daha önceden alışık olunan sistemler gibidir. Yani ekranın üst sol köşesi (0,0) noktası olup ekranı sağına gidildikçe x değeri, aşağı gidildikçe y değeri artar. Maksimum (x,y) değeri ekranın çözünürlük değeridir. Mesela, 640\*480 çözünürlük için maksimum x değeri 639, y değeri ise 479 olacaktır. Bu bölümde sadece 2 boyutlu temel grafik konuları sunulacak olup, Java çok daha fazla çizim kabiliyetine sahiptir.

** 4.a Renk **

Renk için Color nesnesi kullanılır. Color nesnesinin değişik sayıda kurucu metodu vardır. Mesela kırmızı rengi, Color.red, new Color(255,0,0) veya new Color(1.0, 1.0, 1.0) komutlarından birisi ile oluşturabiliriz. Red, Green, Blue kelimelerinin kısaltılmışı olan RGB renkteki kırmızı, yeşil ve mavi tonlaın oranını ister 0-255 arasındaki tamsayı rakamlarla, isterse 0.0-1.0 arasındaki ondalık sayılarla ifade edebilir. R,G ve B değerlerinin eşit olması gri bir tonlamayı ifade eder, üçü de 0 olursa siyahı, üçü de 255 veya 1.0 olursa beyazı ifade eder. Diğer bir renk ifade standardı olan HSB ile RGB arasında dönüşüm Java komutları ile yapılabilir. Java grafik ortamında 24 bit renk derinliği sağlanabilir.

Bir appletin veya örneğin panelin arkaplan rengini değiştirmek için setBackground() komutu kullanılır. Kullanılmazsa varsayılan arkaplan rengi gri veya beyaz olabilir.

Yazım veya çizim rengini değiştirmek için ise Graphics nesnesinin setColor() metodu kullanılır. O anda çalışılan rengin muhteviyatını öğrenmek için getGreen(), getBlue(), getRed() gibi komutlar bulunmaktadır. Renklerin kullanımı daha sonra verilecek örnekte görülecektir.

** 4.b Çizim**

İki boyutlu çizim komutları aşağıdaki örnekte verilmiştir. Java grafik kütüphanesinde pixel çizdirmek için komut bulunmadığı için drawLine komutuna başlangıç ve bitiş koordinatları aynı verilerek bu sağlanmaktadır. Üç boyutlu dikdörtgen çizimi sağlayan draw3DRect komutu siyah renkte iyi sonuç vermemektedir, çünkü aslında gölgelendirme yaparak 3 boyutlu hissi uyandırmaktadır.

SHAPE \\\*

Yukarıda Oval için örnek komut satırı verilmiştir. Yani cismin merkez koordinatı önemli değildir, sadece bir dikdörtgen olarak düşünüldüğünde sol üst koordinatı ve o dikdörtgenin en ve boy değerleri verilmektedir. Tüm çizimlerde bu mantık uygulanır. Yalnızca yay da ayrıca açı değerleri de vardır. Birinci açı yayın başlayacağı dereceyi, ikinci açı da yayın boyutunu değil yayın bitiş açısının 0 açısından ne kadar uzakta olduğunu verir.

** 4.c Font ve Yazı **

Grafiksel yazı biçimimi değiştirmek için Font nesnesi ve setFont() komutu kullanılır. Font için 3 parametre önemlidir. 1. Font ismi: “TimesRoman”, “Arial”, “Courier” gibi. 2. Font tipi: Font.PLAIN ya da 0 düz yazım tipidir. Font.BOLD ya da 1 kalın yazı için, Font.ITALIC ya da 2 italik yazı için,Font.BOLD+Font.ITALIC ya da 3 hem kalın hem de italik yazı için kullanılır. 3. Punto: Yazı fontunun ne kadar büyük olacağı piksel cinsinden verilir.

Font f=new Font(“TimesRoman”,Font.ITALIC,30) ;

** 4.d Bütün Grafik Konularını İçeren Bir Applet Örneği**

***grafik.java***

*import java.awt.\*;*

*import java.applet.Applet;*

*public class grafik extends Applet {*

*public void paint(Graphics g) {*

*Font ff=new Font("Helvetica",Font.PLAIN,10); g.setFont(ff);*

*g.drawRect(10,10,70,70); g.fillRect(10,100,70,70);*

*g.drawString("drawRect",10,90); g.drawString("fillRect",10,180);*

*g.setColor(new Color(230,56,2)); *

*g.drawRoundRect(100,10,70,70,20,30); g.fillRoundRect(100,100,70,70,40,10);*

*g.drawString("drawRoundRect",100,90); g.drawString("fillRoundRect",100,180);*

*g.setColor(Color.red); *

*g.draw3DRect(180,10,70,70,true); g.draw3DRect(180,100,70,70,false);*

*g.drawString("draw3DRect",180,90); g.drawString("fill3DRect",180,180);*

*int xler\[\]= {289, 344, 347, 392, 303, 308, 276 };*

*int yler\[\]= {3, 44, 6, 40, 78, 50, 76 };*

*int yl\[\]= {103, 144, 106, 140, 178, 150, 176 };*

*int pts=xler.length;*

*Color c=new Color(0,250,0); g.setColor(c);*

*g.drawPolygon(xler,yler,pts); g.fillPolygon(xler,yl,pts);*

*g.drawString("drawPolygon",300,100); g.drawString("fillPolygon",300,190);*

*g.setColor(Color.gray);*

*g.drawArc(400,10,80,60,30,330); g.fillArc(400,100,80,60,100,300);*

*g.drawString("drawArc",400,90); g.drawString("fillArc",400,180);*

*g.setColor(new Color(30,56,250));*

*g.drawOval(500,10,80,60); g.fillOval(500,100,60,80);*

*g.drawString("drawOval",500,90); g.drawString("fillOval",500,200);*

*Font f=new Font("Arial",Font.PLAIN,14); *

*Font fB=new Font("TimesRoman",1,16);*

*Font fI=new Font("Helvetica",Font.ITALIC,18);*

*Font fBI=new Font("Tahoma",Font.BOLD+Font.ITALIC,20);*

*g.setColor(Color.blue);g.setFont(f);*

* g.drawString("Bu düz Arial düz fontla yazılmıştır. 14 punto ",10,200);*

*g.setColor(new Color(0,255,0));g.setFont(fB);*

*g.drawString("Bu koyu TimesRoman fontla yazılmıştır. 16 punto",10,230);*

*g.setColor(Color.yellow);g.setFont(fI); *

*g.drawString("Bu italik Helvetica fontla yazılmıştır. 18 punto ",10,260);*

*g.setColor(Color.gray);g.setFont(fBI); *

*g.drawString("Bu koyu ve italik Tahoma fontla yazılmıştır. 20 punto ",10,290);*

*setBackground(new Color(230,250,230));*

*g.setColor(Color.red);*

*g.fillRect(50,300,200,140);*

*g.setColor(Color.white);*

*g.fillOval(70,320,100,100);*

*g.setColor(Color.red);*

*g.fillOval(100,330,80,80);*

*// TURK BAYRAGI CIZIMI *

*int i,faz,aci,icfaz,xm,ym,dr,ir ;*

*int koordx\[\]=new int\[10\];*

*int koordy\[\]=new int\[10\];*

* faz=36; aci=(int) (360/5); icfaz=(int)(aci/2); xm=185; ym=370; dr=30; ir=10;*

*for(i=0;i<koordx.length;i+=2) {*

*koordx\[i\] = xm + (int) ( dr \* Math.cos(Math.PI \* faz / 180)); *

*koordx\[i+1\] = xm + (int) ( ir \* Math.cos(Math.PI \* (icfaz+faz) / 180)); *

*koordy\[i\] = ym + (int) ( dr \* Math.sin(Math.PI \* faz / 180)); *

*koordy\[i+1\] = ym + (int) ( ir \* Math.sin(Math.PI \* (icfaz+faz) / 180)); *

*faz+=aci;*

*}*

*g.setColor(Color.white); g.fillPolygon(koordx,koordy,koordx.length);*

*g.setFont(new Font("Arial",0,20)); g.setColor(Color.black); g.drawString("TURK BAYRAGI",270,350); *

*} *

*}*

**Gelecek Haftalarda İşlenecek Konular: **

Arayüz, yerleşim yöneticileri, olay kontrolleri

Çok kanallılık, istisna işleme

Marmara Üniversitesi Teknik Bilimler Meslek Y.O.

Java Ders Notları

-----------------------------------------------------------------------------------------------------------------

Hazırlayan : Savaş Öztürk

Boy=30

En= 50

20,30

g.drawOval(20,30,50,30);

---
*Kaynak: `JAVA & NESNE YÖNETİMLİ PROGRAMLAMA/JAVA & NESNE YÖNETİMLİ PROGRAMLAMA.doc` — Savaş Öztürk — 2004*
