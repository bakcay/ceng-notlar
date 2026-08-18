# Autocad Ders Notlari

## **AutoCAD ile ÇİZİM**

AutoCAD’de çizime başlamadan önce başlangıç ve bitiş noktalarımızı bilmeliyiz. Bu iki noktayı belirledikten sonra çizimimizi yapmak daha da kolay bir hal alacaktır. Çizimi oluşturmanın bir kaç yöntemi var:

Mutlak koordinat girişi: x ve y koordinatlarının, eğer üç boyutlu çalışıyorsak z koordinatının değerlerini mutlak koordinat olarak girme işi. Örneğin komut satırına 10,15,5 girerseniz, çizginizin başlangıç noktası x’de 10 birim, y’de 15 birim ve z’de ise 5 birim uzaklıkta oluşan noktadır.

Göreceli koordinat girişi:** **bir önceki noktayı orjinmiş gibi varsayarak gireceğiniz yeni noktanın uzaklığını girme işi.Mutlak koordinat girişinden farklı olarak komut satırında girerken başına @ işaretini koyuyoruz. Örneğin @3,5,7 girdiğimizde, oluşturacağımız çizginin son noktasının yeri, bir önceki noktaya göre x’de 3, y’de 5, ve z’de ise 7 birim uzaktaki noktadır.

Kutupsal koordinat girişi:** **bir önceki noktayı orjinmiş gibi varsayarak gireceğiniz yeni noktanın uzaklığını açı ile birlikte girme işi. Burada da @ işaretini komutun önüne yazıyoruz. Örneğin, @10<30 ifadesi, son girilen noktadan x eksenine göre 30 derece açı ile,10 birim uzaklıkta oluşan noktaya birleştirilir. Silindirik koordinatlar: @10<30,5 (r, Φ ,z) ifadesi ise, x ekseni ile 30 derece açı yapan, 10 birim uzaklıktaki noktanın z eksenine paralel uzantısı ile z=5 doğrusunun kesiştiği noktaya birleştirilir. Küresel koordinatlar: Bir başka giriş şeklide, örneğin @10<30<60 (R, θ,Φ) gibidir. Bu durumda ise x-y düzleminde x ile 30 derece açı yapan, 10 birim uzunluğunda ki nokta ile x-z düzleminde 60 derece açı ile noktanın z’ye paralel uzantısının keşistiği noktaya birleştirlir.

Nesne kenetlemelerini kullanmak:** **Daha önce değindiğim nesne kenetleme yöntemlerini kullanarak belli bir noktaya çizginizi birleştirebilirsiniz.

Mouse’u kullanmak:** **mouse kullanarakta çizgiler oluşturabilirsiniz. Tabi burada ölçülü olması biraz zor olabilir. Eğer Grid(ızgara) modunda iseniz ve doğrusal olarak çizim yapacaksanız tabi ki kullanabilirsiniz. Hem daha da hızlı olur.

## **Çizim Ayarları**

*Tools *menüsünün altından *Drawing Aids’*i tıkladığınızda karşınıza dört ayar kutucuğuna sahip Drawing Aids diyalog kutusu gelir.

Modes: Nesne oluşturma, seçme ve ekran görünümüne ait bir kısım ayarlar içerir.

*Ortho:** *imlecin sadece x ve y eksenlerine paralel hareket etmesine izin verir. F8 tuşu ile On, Off yapabilirsiniz.

*Solid fill:*** **Donut ve Solid nesnelerin içlerinin dolu görünmesini sağlar.

*Quick Text:*** **metinlerin ekranda dikdörtgen kutucuklar içersinde gösterilmesini sağlar.

*Blips:*** **ekranda imleç izlerinin kalmasını sağlar.

*Highlight:*** **seçili nesnelerin** **belirgin bir biçimde gösterilmesini sağlar.

*Groups:*** **açık olması durumunda, gruplandırılmış nesneler arasından bir nesneyi seçseniz bile tüm nesneler seçili hale gelir.

*Hatch:*** **açık olması durumunda ilişkilendirilmiş bir tarama dokusunu seçtiğinizde dokunun sınırını oluşturan nesneyi de seçmiş olursunuz.

Snap: Ekranda görünmez bir ızgara varmışçasına, imlecin ızgaranın düğüm noktalarına kenetlenmesini sağlar.

*On:** *Açık olması durumunda Snap’I etkin hale getirir.

*X spacing**:* x ekseni yönündeki kenetlenme aralığını belirler.

*Y spacing:* y ekseni yönündeki kenetlenme aralığını belirler.

*Snap Angle:* Kenetlenme ızgarasını döndürmenizi sağlar.

*X Base:** *Kenetlenme ızgarası için x ekseni yönünde bie temel nokta belirlemenizi sağlar.

*Y Base:** *Kenetlenme ızgarası için y ekseni yönünde bie temel nokta belirlemenizi sağlar.

Grid: Ekrana belirli aralıklarla ızgaraya böler.

*On:** *Izgarayı aktif hale getirir.

*X Spacing:* x ekseni yönündeki ızgara aralığını belirler.

*Y Spacing:* y ekseni yönündeki ızgara aralığını belirler.

Isometric Snap/Grid: eksenleri artı, eksi 30 derece eğik hale getirmeye yarar.

*On:** *Aktif hale getirir.

*Left:* y ekseni 90 derece, x ekseni 150 derece olarak düzenlenir.

*Right:* y ekseni 90 derece, x ekseni 30 derece olarak düzenlenir.

*Top**:* x ekseni 30, y ekseni 150 derece olarak düzenlenir.

## İKİ BOYUTLU ÇİZİM

**Line: Çizgi**

Komut: line

Kısayol: L

Belirli iki nokta arasında çizgi çizme işini yapar. En çok kullanacağınız komut budur herhalde.

Komut: line

From point: (çizginin başlangıç noktasını girebilir ya da mouse ile işaretleyebilirsiniz)

To point: (yukarıda bahsettiğim yöntemlerden biri ile çizginin bitiş noktasını girbilir ya da mouse ile işaretleyebilirsiniz)

To point: (Enter ile çıkabilir ya da başka bir nokta ile devam edebilirsiniz)

**Polyline: Çoklu Çizgi**

Komut: polyline

Kısayol: pl

Normal çizgiye benzeyen, ancak birbirine eklenmiş çizgi, ve yaylardan oluşan çizgiler topluluğu. Normal çizgiden farkı, bu birleşimlerin tek bir nesne olarak kabul edilmesidir.

Komut: polyline

From point: (Başlangıç noktasını giriyorsunuz)

Current line-width is 0.0000 (geçerli çizgi kalınlığının sıfır olduğu bildiriliyor)

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: (Büyük harflerle yazılmış harflerden birini yazarak onlara geçiş yapabilir ya da çizginin son noktasının koordinatlarını girbilirsiniz)(örneğin “a” yazarsanız yay çizme komutuna girmiş olacaksınız ve sizden istediği noktaları girmeniz gerekir. İleride yay konusuna değinilecektir)

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: (yukarıda birkaç çizgi veya yay girdiğinizi kabul edelim, ve en son bir çizgiden sonra “c” ye basarsanız, çoklu çizginizi kaldığı yerden başlangıç çizgisine en kısa doğru ile birleştirir.)

Arc/Close/Halfwidth/Length/Undo/Width/<Endpoint of line>: (eğer “w” harfine basarsanız çizginizin kalınlığını belirleyebilirsiniz,eğer başlangıç ve bitiş kalınlığını farklı değerler olarak girerseniz, çiziginiz veya yayınızın kalınlığı başlangıçtan bitişe değişerek ilerleyecektir.)

**Multiline: Çok Çizgi**

Komut: mline

Kısayol: ml

İki nokta arasında birbirine paralel çizgiler çizme işini yapar.

Komut: mline

Justification/Scale/STyle/<From point>: (başlangıç noktasını giriyoruz)

(Justification: Sanal çizim hattımızın, çoklu çizginin neresinde kalacağını belirliyor(Top,Zero, Bottom)

Scale: Çoklu çizginin kalınlık ölçüsünü ayarlamaya yarıyor.

Style: Daha önceden hazırlanmış çoklu çizgileri çağırmanıza yarıyor.)

To point: (ikinci noktayı giriyoruz) devam ederek daha çok nokta belirtebilirsiniz. Eğer klavyeden “c” harfine basarsanız, close anlamında şeklinizi başlangıç noktasına birleştirir.

**Construction Line: Yardımcı Çizgi**

Komut: xline

Kısayol: xl

Çiziminizde size yardımcı olacak sanal doğrular çizer. Çiziminizin bir parçası değildir. Mimarlıkta okuyanlar ya da “Teknik Resim” dersini almış olanlar bilirler. Asıl çizgiyi çizmek için bazen yardımcı çizgiler çizersiniz. İşte “construction line” da aynen bu işe yarıyor.

Komut: xline

Hor/Ver/Ang/Bisect/Offset/<From point>: (buradaki büyük yazılı olan baş harfleri girerek, size yardımcı olacak çizgilere girebilirsiniz. Örneğin “h” harfi ile horizontal(yatay) sonsuz bir çizgi çizebilirsiniz. Artık çizginin başlangıç ve bitiş noktalarını söylemiyorum. Önünüze gelen menüde bunları da girerek çizginizin nerede görünmesini isterseniz, bunları belirleyebilirsiniz.)

Ver:(Vertical) dikey çizgi

Ang:(Angle) belirli bir noktaya göre verilen açının doğrultusunda çizgi çizer

Bisect:(Bisector) iki çizginin açıortayından geçen çizgiyi çizer.

Offset: Çizginizi bir başka çizgiye göre belirli bir mesafe öteden çizmenizi sağlar.

**Ray: Işın**

Komut: ray

Construction line dan pek de farklı değil. Aynen doğru ile ışın arasındaki fark gibi. Construction line her iki tarafta sonsuza uzanan çizgi çizerken, “Ray” komutu ile ise başlangıç noktası belli, diğer tarafta sonsuza giden bir çizgi çiziyorsunuz. İşte size “ışın”ın tanımı.

**Rectangle: Dikdörtgen**

Komut: rectang

Kısayol: rec

Adı üstünde; dikdörtgen çizmenizi sağlar.

Komut: rectang

Chamfer/Elevation/Fillet/Thickness/Width/<First corner>: Dikdörtgenin ilk köşesini giriyoruz.

(Chamfer: Dikdörtgenin köşelerinde iki uzunluğu da ayarlanabilen birer pah kırmanızı sağlar.

Elevation: Çizilecek Dikdörtgenin z eksenindeki yüksekliğini ayarlamanıza yarar.

Fillet: Dikdörtgenin köşelerini belirleyeceğiniz bir yarıçap doğrultusunda yuvarlar. Böylece oval şekiller elde edebilirsiniz.

Thickness: Dikdörtgenin z eksenindeki kalınlığını ayarlar

Width: dikdörtgeni oluşturan çizgilerin kalınlığını ayarlar.)

**Polygon: Çokgen**

Komut: polygon

Kısayol: pol

Çokgen çizmenizi sağlar. Aman anlamını iyi öğrenin. İlk zamanlarda bu komutu bilmediğimden, bir beşgen oluşturmak için tek tek bütün çizgilerini çizmiştim. Tabi bunu yapmak içinde aradaki açı, mesafe falan hepsini hesapalamak zorunda kalmıştım. AutoCAD’in size sunduğu bir kolaylık. Çokgenlerinizi çok rahat bir şekilde oluşturabilirsiniz.

Komut: polygon

Number of sides <4>: (çokgeninizin kaç kenarlı olacağına kara veriyorsunuz, örneğin bir beşgen çizmek için, 5 rakamını giriyorsunuz)

Edge/<Center of polygon> (çokgenin içine veya dışına geçecekçemberin merkezini girebilir ya da mouse ile işaretleyebilirsiniz)

Inscribed in circle/Circumscribed about circle (I/C) <I>: (eğer çokgenimizin çemberin içinde kalmasını istiyorsak “i”, çemberin dışında teğet olmasını istiyorsak “c” yazıyoruz)

Radius of circle: (çemberin yarıçapını giriyoruz)

Eğer bunlarla uğraşmadan kenarlarla çalışmak istiyorsanız “Edge/<Center of polygon>” esnasında komut satırına “e” yazarak kenar moduna geçmiş olursunuz. Sizden çokgeninizin bir kenarının ilk noktasını ve daha sonra ikinci noktasını isteyecektir. Bu bilgileri girdikten sonra kenar uzunluğu esas alınarak çizim yapılır.

**Region: Bölge**

Komut: region

Kısayol reg

Çevresi kapalı bir nesne ya da şekli dolu bir alan olarak tanımlayabilirsiniz.

Komut: region

Select objects: (istediğiniz nesneyi seçiyorsunuz, seçiminizi tmamladıktan sonra Enter ile onaylarsanız, seçtiğiniz bölgeler kapalı alan haline gelecektir.)

**Circle: Çember**

Komut: circle

Kısayol: c

Değişik çember çizme yöntemleri var. Kullandıkça hangisinin daha çok işinize yaradığını göreceksiniz. Onu kullanmanızı tavsiye ederim. Tabi çiziminiz için uygun olan yöntemi de.

Komut: circle

3P/2P/TTR/<Center point>: (çemberin merkez noktasını giriyoruz.)

Diameter/<Radius>: (çemberin yarıçapını giriyoruz, “d” seçeneği ile çapını da girebiliriz, tabi yarıçapını girmek daha akıllıca…)

Yukarıdakilerden diğerlerine geçerek de çemberinizi oluşturabilirsiniz.

3P: Çemberin üzerindeki herhangi üç noktayı işaretleyerek ya da koordinatlarını girerek çemberimizi oluşturuyoruz. Sizden üç noktayı isteyecektir. Onları girin yeter. AutoCAD sizin için çemberi oluşturur.

2P: Çemberin çapının geçeceği iki noktayı girerek çemberimizi oluşturuyoruz. Biraz zor bir yol. Ancak iki doğru arasına çember yerleştirmek isterseniz kullanmak akıllıca olur.

TTR (Tan,Tan,Radius): çemberin teğet olmasını istediğimiz iki nesneyi seçiyoruz. Daha sonra çemberimizin yarıçapını giriyoruz. Çemberimiz en uygun şekilde yerine yerleşmiş oluyor.

Tan, Tan, Tan: diğelerinden farklı olarak komut satırında yer almaz. Yukarıdaki *Draw *menüsünün altından *circle *seçeneğinin altında açılan seçeneklerde yer alır ve üç teğetin arasına yerleşecek bir çember oluşturur.

**Arc: Yay**

Komut: arc

Kısayol: a

Yay çizme işini yapar. Burada da circle’da ki gibi birden çok seçeneğimiz var.

Komut: arc

Center/<Start point>: (yayın başlangıç noktasını giriyoruz)

Center/End/<Second point>: (Yayın geçeceği ikinci noktayı giriyoruz)

End point: (yayın bitiş noktasını giriyoruz)

Diğer bir seçeneğimiz, Center/<Start point>: komutu sırasında “c” yazarak yayın merkezini belirleyebiliriz.

Komut: arc

Center/<Start point>: c (Center komutuna giriyoruz)

Center: (yayın merkezini giriyoruz)

Angle/Length of chord/<End point>: (Buradan “a” yazarak yayın açısını belirleyebilir, ya da “L” yazarak yayın uzunluğunu belirleyebilirsiniz. Seçim size kalmış)

Diğer seçenekleri, Draw menüsünün altındaki Arc seçeneğinin altında karşınıza gelecek seçeneklerden bulabilirsiniz. Ben sadece isimlerini vereceğim.

3 Points

Start, Center, End

Start, Center, Angle

Start, Center, Length

Start, End, Angle

Start, End, Direction

Start, End, Radius

Center, Start, End

Center, Start, Angle

Center, Start, Length

Continue

**Ellipse: Elips**

Komut: ellipse

Kısayol: el

Elips çizer. Hani derler ya dünyamız elips şeklinde bir eksende döner diye. İşte artık sizde ekseni oluşturabileceksiniz.

Komut: ellipse

Arc/Center/<Axis endpoint 1>: (ilk eksenin ilk noktasını giriyoruz)

Axis endpoint 2: (ilk eksenin ikinci noktasını giriyoruz)

<Other axis distance>/Rotation: (diğer eksenin yarı uzunluğunu giriyoruz)

Diğer seçeneklerde , iki eksenle tanımlanan eliptik bir yay çizebilir, ya da diğer seçenekle elipsin merkezini belirleyip, eksen uzunluklarını girerekte elipsimizi oluşturabiliriz.

**Spline: Bütün Eğri**

Komut: spline

Kısayol: spl

Size bütünleşik eğriler çizme imkanı verir. Özellikle Elektronikçiler için osiloskopta oluşturamadığınız voltaj akım grafiklerini, burada oluşturabilirsiniz.

Spline’ı seçtikten sonra ekranda çeşitli noktalar işaretleyin. Noktalar arasında eğrilerin oluştuğunu göreceksiniz. Eğriliğini de tabi noktaları koyduğunuz yere göre oluşturmuş oluyorsunuz.

**Donut: Halka**

Komut: donut

Kısayol: do

Bildiğimiz simit şekillerini oluşturuyor. Tabi içi dolu olarak…

Komut: donut

Inside diameter <10.0000>: (simidin iç yarıçapını giriyoruz)

Outside diameter<20.0000>: (simidin dış yarıçapını giriyoruz)

Center of doughnut: (simidimizin merkezini giriyoruz. Burda her ne kadar tatlının merkezi dese de…)

Center of doughnut: ( Başka bir simit çizmeyeceksek Enter ile çıkıyoruz)

**Point: Nokta**

Komut: point

Kısayol: po

“Bu da ne?” demeyin. Nokta işte. Nokta koyuyorsunuz. Hani tanımları vardır ya:” kalemimizi deftere deydirip çektikten sonra oluşan şekle nokta denir” diye. İşte aynen öyle nokta. Ancak “style” ile noktanızın büyüklüğünü değiştirebilir, birkaç özellik verebilirsiniz. Pek işinize yarayacağını düşünmüyorum. Ancak referans noktalar oluşturmak için kullanılabilir.

Bu aylık bu kadar. Eğer buradaki yazıları bir yere kaydederseniz, AutoCAD için arşiv niteliğinde bir kaynak oluşturabilirsiniz. İlerleyen aylarda uygulamalı ve resimli örnekleri ile daha detaylı olarak AutoCAD’i öğreneceğimize inanıyorum. Şimdilik buradaki konuları anlamaya çalışın (tabi uygulama da öğrenme de vazgeçilmez bir yöntem). Gelecek ay 3 Boyutlu çizim ve kullanıcı koordinat sistemi( UCS ) hakkında bir şeyler yazmayı düşünüyorum. AutoCAD hakkında merak ettiğiniz konular için bana ulaşabilirsiniz...

## Ali ALAN

## alialan@mailcity.com

## Kaynak: Kim Korkar Bilgisayardan? AutoCAD R14 ‘den yararlanılmıştır…

## Gökalp BAYKAL

Pusula Yayıncılık ve İletişim Ltd.

---
*Kaynak: `AUTOCAD DERS NOTLARI/acadtem.doc` — Hakan — 2000*
