# Mikroişlemciler

## **MİKROİŞLEMCİ NEDİR ?**

Mikroişlemci; gerek yaptığı işlemlerin mikro saniyeler mertebesinde olması aynı zamanda içindeki elektronik devrelerin ve bölümlerin mikron boyutlarında olması nedeniyle bu adı almıştır.

Mikroişlemci; bir bilgisayar sisteminin en önemli 3 donanımından biridir ve bu 3 donanım arasında en çok adı anılandır,diğerleri hafıza (RAM-ROM) ve giriş-çıkış (I/O) birimleridir. Mikroişlemci dünyasındaki gelişmelerin yanında diğer donanımların zaman içinde gelişmesi epey yavaş kalır. İnsanlar bilgisayarlarını birbirlerine tarif ederlerken önce mikroişlemcisini söylerler “bende Pentium III 500 var senin sistem nedir?” gibi atıflarda bulunuruz

Bilgisayarlarda bu kadar önemli bir yere sahip olan mikroişlemcilerin tabi ki sadece bir tek adı olması düşünülemez bile. Mikroişlemcinin CPU (sipiu diye okunur - Central Processing Unit ), MİB (CPU nun Türkçe karşılığı - Merkezi İşlem Birimi), µP (mikro processor-mikro prosesır diye okunur ) ve genelde işlemci olarak bildiğimiz isimlerini de kullanıyoruz.

Adından da anlaşılacağı gibi mikroişlemci (veya işlemci) matematiksel işlemleri yapabilen bir elektronik yonga (chip) dır. Boyutları çok küçük olmasına rağmen içinde binlerce, yüz binlerce veya milyonlarca elektronik devre elemanı bulunduran mikroişlemci aslında matematiksel işlemleri, elektriğin var olması yada olmaması temelinden yararlanarak hesaplar. Chip (‘çip’ diye okunur) lerin nasıl yapıldığı hakkında daha fazla bilgi edinmek isterseniz, chip ler nasıl yapılır bölümüne bir göz atın.

Matematikçilere soracak olursanız kendi bilim dallarının temelinde aslında sadece toplama işleminin olduğunu söylerler. Mikroişlemcide aslında sadece toplama işlemi yapar. Mikroişlemci için çok kaba olmakla beraber toplama işlemini çok hızlı yapan bir elektronik devredir de diyebiliriz. Sadece toplama işlemini yapması pek çekici görünmüyor asıl ününü buradan almaz zaten, mikroişlemciyi mikroişlemci yapan matematiksel işlemleri çok kısa bir zamanda hatasız olarak gerçekleştirebilmesidir. Saniyede milyonlarca işlem yapabilir

Sonuç olarak mikroişlemci matematiksel, aritmetik ve mantık işlemlerini çok kısa sürelerde yapabilen bir elektronik devredir, bir bilgisayar sisteminin beynidir (kalbi diyenlerde var), diyebiliriz. Şayet sizinde bir bilgisayarınız varsa kapağını açıp içindeki mikroişlemciyi görebilirsiniz, fakat kasanın kapağını açmaktan korkuyorsanız değişik mikroişlemcileri görmek için galeri (şu an yapım aşamasında) bölümüne bakabilirsiniz

Bir bina yapılırken nasıl çimento,kum ve çakıl kullanılıyorsa mikroişlemciler yapılırken de bazı elektronik devre elemanları kullanılır, transistor dediğimiz cihaz ise çoğu kişinin yabancı olmadığı bir devre elemanıdır. Günümüz mikroişlemcileri milyonlarca transistoru bir arada barındırır. Transistor lerle ilgili yazımızı okuyanlar anlayacaklardır ki 1 transistor sadece bir olay gerçekleştirir, birkaç tanesi bir araya gelerek bir iş yapar, şayet güzel ve kayda değer işler yapmak istiyorsanız binlercesini veya milyonlarcasını bir araya getirmeniz lazım . Bu arada küçük bir transistor bir nohut tanesi kadardır, milyonlarca transistor çok fazla yer kaplar ama günümüz teknolojisi bu kadar devre elemanını santimetrelere sığdırmayı başarmıştır

## **AGP NEDİR ?**

Accelerated Graphics Port (Hızlandırılmış Grafik Portu)

Acclerated Graphics Port (A.G.P.) arabirimi ana satış gurubunu oluşturan PC lerde,özellikle 3D uygulamalarında yüksek grafik performansı sağlayan yeni bir bus(veri yolu) şartlandırıcıdır.Monitördeki resmin yenilenmesi(refresh) için yeterli bilgi deposu gerektirmekle kalmayıp, doku(texture) mapping, z-buffering ve alfa karışımı gibi olaylar için de büyük bellek deposu gerektiren 3D uygulamaları, bu arabirim şartlandırıcı ile mümkün kılınmaktadır. A.G.P. ana satış gurubunu oluşturan PC lerde 3D uygulamalarının daha hızlı çalışmasını ve daha mükemmel görünmesini sağlayacaktır.
AGP arabirimi, grafik hızlandırıcılarına, ana belleğe ulaşım için özel veri yolu ve daha hızlı transfer gibi yeni özellikler katar. Bu, sistem bellek bağlantısında, geniş bant aralığı ve daha az gecikme sağlar. AGP arabirimi, texturing, z-buffering, ve alfa blending olaylarında ana belleğin kullanılmasını mümkün kılarak ana satış gurubunu oluşturan PC lerde 3D grafik uygulamalarının yüksek performansta çalışmalarını sağlar.

AGP arabirim şartlandırıcı 66MHz PCI (revision 2.1) şartlandırıcıyı temel işlem yolu olarak kullanır ve PCI şartlandırıcıya üç performans uzantısı veya güçlendiricisi sunar ki bunlar 3D grafik uygulamalarında AGP nin yüksek performansını optimize eder. Bu AGP uzantıları PCI şartlandırıcı (rev. 2.1). de tanımlanmamış ve ya gerekmemiştir. Bu uzantılar:

Bellek yazma ve okuma işlemlerinde derinlemesine ayrılmış yol; bellek erişim gecikmesini yok eder.

Veri yolundaki adres ve dataların demultiplexasyonu; hemen hemen %100 verimli veri yoluna izin verir.

133 Mhz data transferi için AC timing(zamanlama); 500 MB/s gerçek data aktarımı sağlar...

Bu güçlendirmeler "sideband" sinyali kullanımı ile gerçekleşmiştir. PCI şartlandırıcı hiçbir değişikliğe uğratılmamıştır, AGP arabirim şartlandırıcı, PCI daki "reserved" alanlar, encodingler, pinler, vb... bölümleri kullanmaması için özel olarak geliştirilmiştir. Asıl eğilim, PCI ın tasarımından faydalanarak grafik yönlü performans artışını karmaşıklık/performans oranını değiştirerek sağlamaktır.
AGP sistem PCI ını ne küçültür nede yerini alır. Bu yüksek hızlı port (AGP) fiziksel, mantıksal ve elektriksel olarak PCI dan tamamen bağımsızdır. Sistemde ek bir bağlantı noktasıdır (Bkz. Fig.1-1). Özel görüntü araçları için tasarlanmıştır; diğer tüm I/O araçlar PCI bus ta kalacaktır. AGP için eklenen ek slot yeni bir bağlantı gövdesi kullanır( elektriksel sinyalizasyon sebebi ile) ki bu PCI bağlantısı ile uyumlu değildir; PCI ve AGP boardlar mekanik olarak birbirleri yerine geçemezler.

AGP arabirim şartlandırıcı Intel tarafından PCI özel gurubundan bağımsız olarak geliştirilmiştir. Bu gurup tarafından desteklenmemiş ve gözden geçirilmemiştir. Kişisel bilgisayar kullanımında grafik teknolojisi ve ürünlerindeki gelişmeyi desteklemek için tasarlanmıştır.
PCI genel amaçlı sistemlerin I/O yolu olmaya devam edecektir. AGP arabirimi PCI ın yerini almak için değil özellikle grafik kontolerler için tasarlanmıştır. PCI I/O fonksiyonları için gerekli bant genişliği 133Mb/s, 32-bit, 33MHz sürümünün sınırlarına yaklaştıkça PCI daha geniş ve daha hızlı yayılacaktır. AGP özellikle noktadan noktaya grafik bileşenleri için tasarlanmıştır. Fiziksel olarak PCI dan ayrılmıştır ve apayrı bir bağlantı kullanır.

## **PCI NEDİR ?**

PCI Veri Yolu Master

PCI Veri Yolu Master, lokal CPU yardımına ihtiyaç duymadan veri transferi gerçekleştirebilir ve CPU Veri Yolu master larının herhangi biri gibi düşünülebilir. PCI SIG grubu, uyumlu PCI işlemlerini destekleyen PCI rev 2.1 sürümünü satışa sunmuştur. Yeni özellikler lokal CPU ve Veri Yolu master' ın eş zamanlı çalışmasına imkan verecektir. Veri Yolu master nasıl çalışır? Cevap hangi aygıtın Veri Yoluna doğru erişime sahip olduğunda yatmaktadır. Çözüm şeması sistem mantığına göre uygulanır. Her veri yolu Master aygıtının kendine has istekleri (REQ#) ve kabul sinyali (GNT#) vardır. Veri Yolu kabul sinyali REQ# söz sahibine Veri Yoluna erişim için doğru seçimi kabul etmesini söyler. Kabul sinyali Veri Yoluna erişim hakkı olan master aygıta izin verildiğini gösterir. Pci kısaca genişletme yuvasıdır. Yeni tip bütün anakartlarda mevcuttur. Modem, ses kartı, tv kartı, ethernet, ve agp çıkışlı olmayan ekran kartları gibi bileşenler bu yuvaya takılarak kullanılır.

---
*Kaynak: `MİKROİŞLEMCİLER/MİKROİŞLEMCİLER NEDIR 2.doc` — mehmet akif — 2004*
