# Sayisal Elektronik Notlari

**Sayısal Elektronik Notları 1**

| Sayısal elektroniğe başlarken öncelikle sayı sistemlerinden biraz bahsetmek istiyorum. **Binary sayı sistemi** Bildiğiniz gibi kullandığımız sayı sisteminde 10 tane rakam vardır 0.1.2.3.4.5.6.7.8.9 ve böylecede bir haneli sayıda 10 çeşit rakamı ifade edebiliyoruz bizim kullandığımız sayı sistemine desimal sayı sistemi denir. Oysaki elektronikte kullanılan sayı sisteminde toplam 2 çeşit rakam vardır 0 , 1 Bir başka deyişle var yada yok. Bir hanede 2 farklı durumu ifade edebiliriz. Bu sayı sistemine binary sayı sistemi denir. Bir örnekle açıklarsak binary 10 =desimal 3 , binary 101 = desimal 5 demektir. |
| --- |
| **Hexadesimal sayı sistemi **Hexadesimal sayı sisteminde ise 16 çeşit rakam vardır. Bir haneli sayıda 16 ya kadar değişik durum ifade edebiliriz. 0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F Hexadesimal A= Desimal 10 Hexadesimal 10 = Desimal 16 |
| **1 ve 0 **Sayısal elektronikte gerilimin var olduğu duruma 1 olmadığı duruma 0 deriz yani (+5 Volt =1) (0 Volt = 0 ) durumunu ifade eder. |
| ** KAPILAR** Sayısal elektroniğin temelinde kapılar vardır .Filip floplar hatta mikro işlemciler bile kapıların birleşmesinden oluşmuştur. Kapılar 2 yada daha fazla girişli ve tek çıkışlı olurlar. Her kapıya hangi girişler gelince ne çıkacağı kapının özelliğinde bellidir. Bu özellikleri kullanarak tasarım yapar sayısal işlemleri yaparız. Örneğin VE kapısı 1. VE 2. Girişi 1 olursa 1 çıkarır. Yada VEYA kapısı 1. Veya 2. Girişi 1 olursa 1 çıkarır .Hetırlamak basittir. Değilleride bunların tam tersi durumlardır. |

Elektronik devrelerde genel olarak bir iş yapabilmek için mikro işlemciler bölümünde belirttiğimiz gibi giriş birimleri olur. Bu birimden gelen verileri işleyecek işlem bölümü ve işlediği bilgileri göstercek çıkış birimi olur . **Sayısal elektronik nedir ? **. İşlenecek bilgilerin 1 ve 0 gibi sayılara çevrilerek iişlenmesi ve sonuç birimine aktarılmasıdır. Analog elektronikte ise bu işlemler farklı olarak yapılır.

Örneğin : Bir motor devir göstergesi yapmak istersek sayısal elekronikte motorun dönüş sinyallerini her devirde bir pulse gelecek şekilde 1 ve 0 sinyaline çeviririz bu sinyali sayıcıya girer sayıcı çıkışını gösterlere aktarırız. Analog elektronikte ise motorun devrini voltaja çevirecek bir giriş devresi yaparız. bu sinyali kalible ederek bir voltmetreye veririz. Sonuçta iki devrede aynı işi yapar ve motorun devrini gösterir.

Sayısal elektronikle ilgili filip floplar ve kaydediciler gibi diğer elemanların anlatımına geçmeden evel kapılarla ilgili değişik bir kaç uygulama örneği vermek istiyorum.

Tasarımlarda gerektiğinde kullanmak için basit bir kare dalga osilatörü.

Bildiğiniz gibi değil kapısında girişinde ne varsa çıkışından tersi çıkar. Çıkışını girişe bağlarsak kapının çalışma frekanslarının sınırıyla limitli yüksek frekanslı bir osilatör olur. Çıkışı girişe gecikmeyle aktarırsak çıkış frekansını ayarlamış oluruz. Buradaki direnç ve kondansötör değeri çıkış frekansını belirler.

İlk şekildeki çıkışta 1 ve 0 oranı eşittir . Eğer farklı olmasını istersek çıkışı girişe aktarırken 1 ve 0 için değişik gecikme koymamız gerekir bunu sağlamak için bir diyot ve direnç ilavesi yeterlidir. Diyota seri direncin değerin ne kadar düşerse çıkıştaki pozitif pulse o kadar daralır.

---
*Kaynak: `SAYISAL ELEKTRONİK NOTLARI/SAYISAL ELEKTRONİK NOTLARI.doc` — Çetin Arslan — 2004*
