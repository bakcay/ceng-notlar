# Autocad Ders Notlari

## **POLYGON, RECTANGLE**

Bu ayki konumuzda, “*polygon”(çokgen) *ve *“rectangle”(diktörtgen) *konuları hakkında basit birkaç örnek vereceğim. Yanlarına türkçe anlamlarını verdim, çünkü komutun anlamını bilmek AutoCAD kullanımını basitleştirmek için çok önemli. AutoCAD, çizimi kolaylaştırmak için bir sürü komut ya da kısayolu kullanımımıza sunmuştur. Ancak bunları bilmeden AutoCAD’in avantajlarını lehimize kullanmamız olası bir şey değildir. Aksi taktirde yapacağımız çizimlerin, basit bir çizim programı ya da “paint brush” kullanarak yapacağımız bir çizimden pekde farkı kalmaz. Size bunu kendimden bir örnek vererek açıklayayım. Önceden uyarayım, aslında bu bir çözüm bulma politikasıdır ya da zorda kaldığınızda yapabileceklerinizin sınırlarını zorlamak gibi bir şey... AutoCAD dersini okulda almaya başladığımız yıl, derse giren hocamız bizi küçük bir quiz yapmak için sırayla bilgisayarların başına alıyordu. Konu şu an için çok basit; eşkenar bir “beşgen” çizilecek, yanında da birkaç ufak atraksiyon( çizgilerle). Tabi zamanda kısıtlı. Ne yaptım dersiniz? “Polygon kullandın” dediğinizi duyar gibi oluyorum. Ama işin aslı öyle değil... AutoCAD’de böyle bir komut olabileceğini tahmin ediyorumi ancak ne polygon(çokgen) aklıma geliyor ne de başka bir şey. Üstün matematik bilgimi kullanarak, eşkenar bir beşgenin iç açılarının ölçüsünü buldum( düşünmeyin: 72 derece ). Tabi sonra klasik AutoCAD komutlarını kullanarak, bir diğer deyişle, çizgileri birleştirerek beşgeni oluşturdum. Sonuç aynı, uzaktan bakınca o da beşgen, ancak zaman kısıtlı demiştim ya; tabi zaman çizimin tamamını bitrmeme müsade etmedi. Bir düşünün böyle bir konumda, şu “polygon” komutunu bilseydim... işte size kıssadan hisse, AutoCAD ile yapabileceklerinizi düşünün...

**POLYGON:**

Command: polygon

Enter number of sides <4>: 5 (çokgenimin kenar sayısını giriyorum)

Specify center of polygon or \[Edge\]: 7,5 ( çokgenin merkez noktasını x=7, y=5 olarak giriyorum)

Enter an option \[Inscribed in circle/Circumscribed about circle\] <I>: (Enter ile geçiyorum, çokgenimin dışına hayali bir çember çizerek oluşturulacak)

Specify radius of circle: 0.5 (çemberin yarıçapı)

Burada sadece çemberin yarıçapını uzunluk olarak girdiğim için, normal olarak çokgeni oluşturdu... aşağıdaki örneklere lütfen dikkat edin...

Command: polygon

Enter number of sides <5>: 3

Specify center of polygon or \[Edge\]: 7,5

Enter an option \[Inscribed in circle/Circumscribed about circle\] <I>: c

Specify radius of circle: 0.5 (yine normal olarak bir üçgen oluşturdu)

Command: polygon

Enter number of sides <5>: 4

Specify center of polygon or \[Edge\]: 7,7

Enter an option \[Inscribed in circle/Circumscribed about circle\] <I>:

Specify radius of circle: @0.5<0 (kareyi oluşturdu ancak, burada dikkat edilmesi gereken nokta; çemberin yarıçapını giriş şekli. Çember, çokgenin dışında olacağı için köşesine değmektedir. Ve burada verilen açıda, çokgenin köşesinin bulunacağı açıyı belirtmektedir.)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Command: polygon

Enter number of sides <5>: 5

Specify center of polygon or \[Edge\]: 8.5,7

Enter an option \[Inscribed in circle/Circumscribed about circle\] <I>:

Specify radius of circle: @0.5<0 (aynı şekilde burada da beşgenin köşe açısı “0” derece olarak girilmiştir.)

Açıları değişik girerek şeklinizin nasıl oluşturulacağını görün...

**RECTANGLE:******

Command: rectangle

Specify first corner point or \[Chamfer/Elevation/Fillet/Thickness/Width\]: 7,7

Specify other corner point: 8,6

Polygon komutu kullanılarakda basitçe bir dörtgen çizilebilir. Rectangle(dörtgen) çiziminde, yukarıda gösterilen “*Chamfer/Elevation/Fillet/Thickness/Width” *özelliklerini burada tekrar örneklerle anlatmayacağım. Temmuz ayındaki konumuzda, rectangle komutunu tanımlarken ne işe yaradıklarını söylemiştim. Oradan yararlanarak kendiniz denemeler yapabilirsiniz...

Gelecek ay görüşmek dileğiyle...

---
*Kaynak: `AUTOCAD DERS NOTLARI/acadsub.doc` — amanda10 — 2001*
