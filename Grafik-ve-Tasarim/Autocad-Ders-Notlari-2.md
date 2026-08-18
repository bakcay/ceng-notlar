# Autocad Ders Notlari

AutoCAD İLE ÇİZİM

Bu ay AutoCAD konularına biraz mola veriyoruz. İşte beklediğiniz örnekler yavaş yavaş geliyor. Hatta geçenlerde sitenin ziyaretçi defteri bölümünde bir arkadaşımız site resimli olsa daha güzel olur diye bir öneride bulunmuş; güzel bir öneriydi. Bende bu ayki yazımda biraz “resmi” takılacağım… hepinize iy seyirler…

**Line:**

Komutları yazdıktan sonra “Esc” tuşu ile yada mouse’in sağ tuşuna tıklayarak çıkabilirsiniz. Yukarıda görülen şekil oluşacaktır. Eğer elinize ölçülü halde çizmenizi istenen birşey verirlerse, komut satırından çok kolayca çizebilirsiniz. Tabi bazende çizmek için aklınıza birşey gelmez. Mouse’u oynatarak acayip şekiller ortaya çıkarabilirsiniz… 

Burada komutların yazılımlarına dikkat etmenizi istiyorum. AutoCAD’de ölçülü çizimin temeli diyebiliriz. Eğer koordinat sisteminde bildiğiniz noktalara ilerlemek için direk olarak noktayı gireblirsiniz.(örneğin 80,70). Fakat bir noktadan belirli bir açıyla gitmek istiyorsanız; komut satırının başına “@” işaretini koymanız gerekecek. Daha sonra gitmek istediğiniz mesafeyi yazdıktan sonra”<” işaretini koyarak açının ölçüsünü yazıyorsunuz.(örneğin @40<210).

Düşündüm de; konuyu daha önceden anlatmıştık. Burada tekrar anlatmaya sanıyorum hiç gerek yok. Sadece örnekler. Bakalım bakarak anlayabilecekmisiniz…

**Polyline:**

Command: pline

From point: 0,0

Current line-width is 0.0000

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: 0,150

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: w (Çizgi kalınlığını belirlemek için “w” yazıyorum”)

Starting width <0.0000>: 0

Ending width <0.0000>: 25

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: a (yay çizmek için “a” yazıyorum)

Angle/CEnter/CLose/Direction/Halfwidth/Line/Radius/Second pt/Undo/Width/

<Endpoint of arc>: @50<0

Angle/CEnter/CLose/Direction/Halfwidth/Line/Radius/Second pt/Undo/Width/

<Endpoint of arc>: w (ikinci yayın kalınlığını belirteceğim)

Starting width <25.0000>: 25

Ending width <25.0000>: 0

Angle/CEnter/CLose/Direction/Halfwidth/Line/Radius/Second pt/Undo/Width/

<Endpoint of arc>: @50<0

Angle/CEnter/CLose/Direction/Halfwidth/Line/Radius/Second pt/Undo/Width/

<Endpoint of arc>: l (çizgi çizmek için “l” yazıyorum.)

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: w (çizgi kalınlığını belirteceğim)

Starting width <0.0000>: 0

Ending width <0.0000>: 15

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: @20<90

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: w (ikinci çizgini kalınlığını belirteceğim)

Starting width <15.0000>: 15

Ending width <15.0000>: 0

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: @20<90

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: a (başka bir yay)

Angle/CEnter/CLose/Direction/Halfwidth/Line/Radius/Second pt/Undo/Width/

<Endpoint of arc>: w (yay kalınlığı için)

Starting width <0.0000>: 0

Ending width <0.0000>: 0

Angle/CEnter/CLose/Direction/Halfwidth/Line/Radius/Second pt/Undo/Width/

<Endpoint of arc>: @25<-30

Angle/CEnter/CLose/Direction/Halfwidth/Line/Radius/Second pt/Undo/Width/

<Endpoint of arc>: d (yön belirterek bir yay çizeceğim)

Direction from start point: 120,150

End point: 185,40

Angle/CEnter/CLose/Direction/Halfwidth/Line/Radius/Second pt/Undo/Width/

<Endpoint of arc>: r ( çember komtlarını kullanarak bir yay çizeceğim, yayın ağababası diyebiliriz)

Radius: 185,40 (yayın başlangıç noktasını giriyorum)

Second point: 55,40 (ikinci nokta)

Angle/<End point>: a (yayımı açıyla belirtmek istiyorum)

Included angle: 180

Direction of chord <323>: -40,160 (yayın gideceği yönü bir nokta ile belirtiyorum)

Angle/CEnter/CLose/Direction/Halfwidth/Line/Radius/Second pt/Undo/Width/

<Endpoint of arc>: l (çizgi çizmek için “l” yazıyorum)

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: c (polyline’ımı kapatmak için “c” yazıyorum)

Polyline; bildiğiniz gibi birden çok nesneyi tek bir nesne gibi kabul eder. Yani eğer bu noktalardan herhangi birini seçerseniz, tüm elemanları seçmiş olursunuz. Polyline, çizimlerde yapacağınız aktarmalarda, ya da çiziminizde birçok defa kullanacağınız yerlerde işinize yarayabilir. Tabi çizgileriniz hep böyle bileşik halde kalmak zorunda değil. “explode” komutunu kullanarak çizgileri bağımsız hale getirebilirsiniz.

Bu aydan itibaren, her ay birkaç ipucu vereceğim:

**Ipucları :**

eğer herhangi iki nokta arasındaki mesafeyi merak ediyorsanız, “Toolbar” lardan “Inquiry” menüsünü ekrana getirin. “distance” komutu ile bunu öğrenebilirsiniz.

“Tools” menüsünün altında “Object Snap Settings…” e girerseniz, belli noktalara mouse’u snap ettirebilirsiniz. Mouse ile çizim için güzel bir yol.

AutoCAD’in siyah-beyaz ekranı size klasik mi geliyor? O halde renkleri siz belirleyin. “Tools” menüsünün altında “Preferences” e tıklayın. “Display” menüsünün altında ki “color” işinizi görecektir.

Çiziminize yazı ekleyebilirsiniz. Komut satırına “dtext” yazın. Ve görün…

Command: l (önce çizgi çizmek için komutu verdik) (bu arada tüm komutlar bulunduğumuz yerden devam ediyor)

LINE From point: 0,0(başlangıç noktasını giriyoruz)

To point: 0,100 (x =0, y=100 noktasına ilerlemek için)

To point: 50,100 (bulunduğumuz yerden x=50, y=100 noktasına çizgi çiziyoruz)

To point: @30,40 ( x yönünde “30”, y yönünde “40” birim ilerlemek için.)

To point: @40<-90 (“-90” derece açıyla 40 birim ilerlemek için)

To point: @30<0 (“0” derece açıyla 30 birim ilerlemek için)

To point: 80,70 (x=80, y=70 noktasına ilerlemek için)

To point: @40<210 (“210” derece açıyla “40” birim ilerlemek için.)

To point: @35<-60 (“-60” derece açıyla 35 birim ilerlemek için)

To point: 0,0 (x=0, y=0 noktasına gitmek için)

---
*Kaynak: `AUTOCAD DERS NOTLARI/acadar.doc` — Hakan — 2000*
