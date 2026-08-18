# Autocad Ders Notlari

## **AutoCAD R14**

**Başlamak: Start Up**

AutoCAD'i çalıştırdığınızda ekrana *Start Up** *yani başlatma kutusu gelmekte. Buradan yeni bir çizime başlayabilir, şablon kullanabilir ya da daha önceden yapmış olduğunuz bir çizimi açabilirsiniz. Gerekli ayarlardan sonra OK ile onay verebilirsiniz.

**Use a Wizard: Sihirbaz Kullan**

Burada iki tür seçeneğiniz var. *Quick Setup, Advanced Setup**.*En çok kullanacağımız yer Quick Setup. Tabi ileride daha çok öğrenince Advanced Setup'a da ihtiyacınız olacak.

**Quick Setup:**

iki Aşamdan sonra çizime geçebileceğiniz yer.

*-Step 1:Units(Birimler):* Bu sekmede çizim birimini değiştirmeniz için bazı seçenekler var. Bunlar Decimal(Ondalık), Engineering(Mühendislik), Architectural(Mimarlık), Fractional(Kesirli) ve Scientific(Bilimsel) olmak üzere beş tanedir. tabi bu sekmede en çok kullanacağınız ölçü birimi, herkesin bildiği Decimal(ondalık) sistem olmalı. tabi arkadaşlar branşlarına göre de diğer seçenekleri kullanabilirler.

-*Step 2:Area(Alan):** *Bu sekmede çizim kağıdınızın, genişlik ve uzunluk olmak üzere boyutlarını belirleyebilirsiniz.

**Advanced Setup:**

AutoCAD'da uzmanlaştıktan sonra Quick Setup'daki iki sekmenin size yetmediğini göreceksiniz. Ancak burada ileride içeriğine değinmek üzere sadece sekmelerin isimlerini verip geçeceğim.

*-Step 1:Units(Birimler)*

*-Step 2: Angle(Açı**) *Açının birimini değiştiryorsunuz.

*-Step 3: Angle Measure(Açı Başlangıç Yönü)** *Açı belirtirken 0 derecenin hangi yönde kabul edileceğine karar veriyorsunuz.

*-Step 4: Angle Direction(Açı Yönü**) *Açının hangi yönde ilerleyeceğine karar veriyorsunuz.

*-Step 5: Area(Alan)*

*-Step 6: Title Block(Pafta)** *Pafta sınır çizgileri ve antetini oluşturmak için bir dizi hazır seçenek sunar.

*-Step 7: Layout(Pafta Düzeni)*

**Use a Template: Şablon Kullan**

Bu seçenek ile eldeki şablon dosyalarını kullanabilirsiniz. Şablon dosyalarının uzantısı DWT(Drawing Template File)'dir. Sizde istediğiniz bir dosyayı şablon haline getirebilirsiniz.

**Start From Scratch: Ayarsız Başla**

Önceden hiçbir ayar yapmadan bir çizime başlamak istediğinizde bu seçeneği kullanabilirsiniz. Eğer çiziminiz hakkında bir fikriniz yoksa, çiziminiz içinde bazı ayarları yapabilirsiniz. Tabi başlangıçta çizim ölçü biriminizi ayarlamanız gerekiyor.

**Open a Drawing: Çizim Aç**

AutoCAD'i başlattığınızda daha önceden yapılmış bir çizimi açabilirsiniz.

Aslında bu sekmeler Windows kullanıcılarının pekde yabancı olmadığı aşamalardır. Açılış penceresinde ikonların ne işe yaradığı altındaki küçük bir pencerede belirtiliyor. Oraya bakarak ta çiziminiz için en uygun ayaraları yapabilirsiniz.

**AutoCAD R14 Ekranı:**

Standart olarak Başlık Çubuğu, altında menü çubuğu, daha sona Standart araç çubuğu ve Properties Araç çubuğu yer alır. Bu çubuklar bir dizi yararlı komut düğmesi içerirler. Ekranın en altında ise durum çubuğu yer alır. Burada *Snap, Grid, Ortho, Osnap, Model ve Tile *düğmeleri bulunur. Alt tarafta bir de komut penceresi bulunur ki; komutların kısayollarını öğrendiğinizde buradan yazarak istediğiniz komutu çalıştırabilirsiniz. Ve ayrıca metin penceresini açarak da, çizim boyunca neler yaptığınızı buradan öğrenebilirsiniz. Siz Komutları mouse ile birlikte vermiş olsanız bile, komut buraya yazılır. F2 tuşunu kullanarak pencereyi ekrana getirebilirsiniz.

**Komut vermek ve veri girmek**

**Undo:**** **Undo komutu diğer programlarda olduğu gibi hatalarınızı geri almaya yarar.

*komut:** *Undo

*kısayol**: *Ctrl+Z

*komut kestirmesi: *U

**Redo:**** **Adı üstünde, geri aldığınız hatalarınızdan tekrar dönebilirsiniz. Ama sadece bir defa. Ne güzel değil mi? Bu da size Undo yaparken dikkatli olmanızı hatırlatan bir şey gibi. Undo'da istediğiniz kadar geri gidebilirken, Redo komutu sadece en son geri aldığınız komutunuzu geri getirir.

*komut:** *Redo

*kısayol**: *Ctrl+Y

**Esc:**Herhangi bir diyalog kutusundan çıkmak için Bu tuşu kullanıyoruz

Ayrıca F7, Grid(ızgara) kutucuğunun, F9 ise Snap kutucuğunun kısayol tuşlarıdır. ileride kullanabilirsiniz.

Buraya kadar diğer windows altında çalışan programlarda olan, ya da windowsun kendisinde olan komutları kısaca tanıtmaya çalştım. Birçoğunu sizde biliyorsunuzdur. Artık yavaş yavaş AutoCAD'in renkli dünyasına girmeye başlayalım. Çizim konusunda size verdiği kolaylıkları gördükçe eminim sizde çok seveceksiniz.

**NESNE YAKALAMA ve KENETLEME**

Belirli bir başlangıç noktası ve bitiş noktası arasını nesne yaklama ve kenetleme araçları ile çok daha hızlı yapabilirsiniz. Çok fazla işinize yarayacağını düşündüğüm bu komutlar size bir nebze olsun hesaplama derdinden kurtaracak.

**Tracking:**

İki noktayı referans alarak çizme işini yapar. Örneğin bir dörtgenin içine başka bir çokgen çizmek istiyorsunuz. Bunun için öncelikle *polygon *seçeneğinden çokgeninizin boyutunu ayarlayın(ya da daire). Daha sonra sizden *center point *istedinde tracking düğmesine tıklayın. Size ilk önce, ilk referans noktasını soracaktır. Dörtgenin Alt orta noktasını tıklayın ve Enter'layın. daha sonra ikinci referans noktasını soracaktır. Burada da Yan Kenarlardan birinin orta noktasını tıklayın ve Enter'layın. Artık çokgeninizin merkezi tam olarak dörtgenin ortasındadır.

**Snap to Endpoint:**

Bu kenetlenme aracı, üzerine tıkladığınız nesne ya da çizginin tıklanan noktaya en yakın olan uç noktasına kenetlenir.

**Snap to Midpoint:**

Herhangi bir çizgi veya yayın tam orta noktasını yaklamak için kullanılır.

**Snap to Intersection:**

Aynı düzlem üzerinde bulunan iki noktanın sanal olarak kesiştiği noktayı yakalar.

**Snap to Apparent Intersection:**

Kesişmeyen veya aynı düzlemde olmayan iki çizginin izdüşümlerinin sanal kesişme noktasını yakalar.

**Snap to Center:**

Çember ve yayların merkez noktasını yakalar.

**Snap to Quadrant:**

Çember, Yay ve Elipslerin 0,90,180,270 derecelik açılardaki noktalarını yakalar.

**Snap to Perpendicular:**

Son işaretlediğimiz noktadan, başka bir çizgiye 90 derecelik açı ile gelen çizginin son noktasını yakalar.

**Snap to Tangent:**

Bir çember veya yaya teğet oluşturan noktayı yakalar.

**Snap to Nearest:**

Bir çizim nesnesi üzerinde imlece en yakın olan noktayı yakalar.

**Snap to None:**

Tanımlanmış tüm nesne işlevlerinizi o an için iptal eder. Bir sonraki hareketinizde ise kenetlenme seçenekleri yine geçerli olur.

**Otomatik Yakalama: Osnap**

Yukarıda sözünü ettiğim nesne yaklama ve kenetleme araçlarını mouse ile daha kullanışlı hale getirebiliriz. *Osnap Settings *diyalog kutusunu açtığınızda, çizim esnasında hangi araçların aktif olacağını gösteren tikler göreceksiniz. Burada işinize yarayanları işaretlerseniz, mouse çizim sırasında size orta noktaları, uç noktaları vb. belirli renkteki bir yuvarlağın içine alarak gösterir. Tabi hangi renk olacağını da siz belirliyorsunuz.(AutoSnap'tan)

**Nesneleri Seçmek:**

Çizim esnasında ya da herhangi bir düzenleme komutu içerisinde bir nesneyi seçmek için onun herhangi bir noktasına tıklamanız onu seçmek için yeterli. Ancak komutun içinde onu seçtiğinizi belirtmek için Enter'lamanız gerekiyor. Eğer birden fazla nesneyi seçmek istiyorsanız birkaç yolunuz var. Tek tek mouse ile işaretleyebilirsiniz ki uzun bir yoldur. diğer bir seçenek ise; mouse'u basılı tutarak sağdan sola doğru hareket ettirirseniz, oluşan kesik çizgili pencere içerisinde temas edilen tüm nesneler seçili hale gelir. Eğer soldan sağa doğru sürüklerseniz, oluşturacağınız pencerenin içerisinde tümüyle kalan nesneler seçili hale gelir. İyi bir seçim özelliği, ama ne taraftan sürükleyeceğinizi karıştırmayın.

Komut satırına CP yazdıktan sonra işaretleyici ile oluşturacağımız sanal çokgen pencerenin temas ettiği tüm nesneleri seçili hale getirir.

Komut satırından WP yazdıktan sonra işaretleyici ile oluşturacağımız pencerenin tümüyle içinde kalan tüm nesneler seçili hale gelir.

Komut satırına F yazdıktan sonra işaretleyici ile oluşturacağımız bir çizgiye temas eden tüm nesneleri seçili hale getirir.

Birkaç seçim yöntemi daha var, ancak en çok işinize yarayacak seçim komutları bunlar.

Bu aylık bu kadar. Eğer buradaki yazıları bir yere kaydederseniz, AutoCAD için arşiv niteliğinde bir kaynak oluşturabilirsiniz. Gelecek ay çizim komutları, kısayolları, iki ve üç boyutlu çizimler hakkında bir şeyler yazmayı düşünüyorum. AutoCAD'de merak ettiğiniz konular için bana ulaşabilirsiniz...

alialan@mailcity.com

Kaynak: Kim Korkar Bilgisayardan? AutoCAD R14

Gökalp BAYKAL

Pusula Yayıncılık ve İletişim Ltd.

---
*Kaynak: `AUTOCAD DERS NOTLARI/autoc.doc` — 2000*
