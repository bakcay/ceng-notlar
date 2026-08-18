# CMOS Nedir - TTL Nedir

## **CMOS NEDİR? TTL NEDİR? CMOS İLE TTL ARASINDAKİ FARKLAR NELERDİR?**

CMOS ile TTL adlı yapılar, “entegre” olarak adlandırılan devre grubuna girerler.Bu sebeple önce “entegre “ kavramını açıklayım.Bu sayede CMOS ile TTL tanımlarını daha rahat ve anlaşılır hale getiririz.

**Entegre:** Belli bir fonksiyonu gerçekleştirmek amacıyla çok sayıda direnç, diyot ve transistörlerin bir araya getirilerek oluşturulan devrelere **entegre** adı verilir. Entegreler, entegrasyon seviyelerine ve yapılarında kullanılan transistör tipine sınıflandırılabilirler. Lojik uygulamada seçilecek entegre devre familyası, devrenin özelliklerine göre belirlenir. Günümüzde çok özel devreler hariç genellikle devre gerçekleştirmede TTL ve CMOS familyasını entegre devreler kullanılmaktadır.

Entegrasyon Seviyelerine göre:

•SSI (Small-Scale Integration): 12’den az transistör içeren entegreler
•Medium Scale Integration ( MSI ): 12 ile 99 arası transistör içeren entegreler. (örneğin flip-floplar, sayıcılar)
•Large Scale Integration (LSI): 100 ile 9.999 arası transistör içeren entegreler (örneğin hafıza elemanları EPROM, ROM)
•VLSI (Very Large Scale Integration): 10.000-99.999 arası transistör içeren entegreler (örneğin 8-bit basit mikroişlemciler)
•ULSI (Ultra Large Scale Integration): 100.000- ve fazlası transistör içeren entegreler (örneğin gelişmiş entegreler)

Yapılarında kullanılan transistör tiplerine göre:

**TTL (Transistor-Transistor Logic) Entegreler:**

Yapılarında bipolar transistörler kullanılır. Besleme gerilimleri 5V’tur. CMOS entegrelere göre güç kayıpları çok fazladır.

•Standard TTL (74XXX ailesi): en eski, yavaş ve güç kayıpları çok fazla
•Low Power TTL (74LXXX ailesi): daha az güç kayıpları
•Schottky TTL (74SXXX ailesi): hızlı fakat güç kayıpları fazla
•Low Power Schottky TTL (74LSXXX ailesi): hızlı ve düşük güç kayıplarına sahip
•Advanced LS TTL (74ALSXXX): hız-güç kayıpları oranı çok iyi
•FAST TTL (74FXXX): hız ve güç kayıpları açısından en iyi TTL entegresi

**CMOS (Complementary Metal-Oxide Silicon) Entegreler**:

Yapıları FET türü transistörlerden oluşur. Besleme gerilimleri 3V ile 15V arasında olabilir. TTL’den çok daha az güç kayıpları vardır.

•40XX ailesi: En eski CMOS, yavaş, güç kaybı çok az.
•74HCTXXX ailesi: TTL uyumlu (besleme gerilimi 5V), CMOS’un avantajları (çok düşük güç kayıpları) ile TTL’in avantajlarını (çok hızlı) birarada bulundurur. En popüler entegre.

Bi önceki sayfada entegreleri sınıflandırırken TTL ile CMOS’un tanımlarına az da olsa girdik.Açıklamada görüldüğü gibi CMOS ile TTL yapılarında kullanılan transistörlere göre birbirlerine farklılık gösterirler.Şimdi daha detaylı olarak CMOS ile TTL’i inceleyip,sonrada aralarındaki farkları sıralayalım.

**CMOS**** **(Complementary Metal Oxide Semiconductor-Tamamlayıcı Metal Oksid Yarı İletken):

CMOS lojik ailesi, mantık fonksiyonlarını oluşturacak şekilde birbirine bağlı her iki tip(hem n-kanallı hem p-kanallı) MOS elemanlarından oluşmaktadır.Temel devre aşağıdaki şekillerde gösterildiği gibi,p-kanallı bir transistörden ve n-kanallı ikinci bir transistörden oluşan bir tersleyicidir.

p-kanallı elemanın kaynak ucu Vdd düzeyinde, n-kanallı elemanın kaynak ucuda toprak düzeyindedir.Vdd değeri +3V ila +18V arasında herhangi bir değerde olabilir.Gerilim seviyeleri,alçak seviye için 0V,yüksek seviye içinde Vdd’dir.

CMOS’un çalışması şöyle özetlenebilir.

n-kanallı MOS,kapıdan-kaynağa gerilimi pozitif olduğu zaman iletir.

p-kanallı MOS,kapıdan-kaynağa gerilimi negatif olduğu zaman iletir.

Kapıdan-kaynağa gerilimiz sıfır olması durumunda her iki tip elemanda kapanır.

Örneğin tersleyici devresini açıklayalım:

Tersleyici devresinde giriş alçak olduğu zaman,p-kanallı eleman açılırken ,n-kanallı eleman kapanır.(p-kanallı eleman kaynağa göre –Vdd seviyesinde ,n-kanallı eleman kaynağa göre 0V seviyesindedir.)

Giriş yüksek olduğu zaman her iki elemanda Vdd düzeyindedir. Ve durum tersine döner.p-kanallı eleman kapanırken ,n-kanallı eleman açılır.Sonuçta çıkış 0V alçak seviyesine yaklaşır.

CMOS mantık ailesinin güç tüketimi oldukça düşüktür.Genellikle harcadıkları güç 10 nW civarındadır.CMOS’lar genellikle 5V-15V aralığında tek kaynaklı çalışma için tanımlanırlar.Ancak bazı devreler 3V veya 18V düzeyinde de çalışabilmektedir.

**\*Örnek olarak bir CMOS entegre olan 16f84’ün kullanum yerlerini inceleyelim.**

CMOS entegrelerde giriş uçlarını +5 Volt'a bağlamak gerekir.16F84 de bir CMOS entegredir, fakat burada pic içinde I/O pinleri özel şekilde bağlanmışlardır ve program aracılığı ile giriş veya çıkış haline getirilir. Giriş pozisyonunda bu uçlar pull-up konumundadır, yani pic içinde bir şekilde +5 volta bir direnç üzerinden bağlı gibidir. Burada pull-up dirençleri 50 K kadardır.

16F84'ün çalıştırılmasında en çok kullanılan yöntemler :

1-) Xtal osilatör
2-) Seramik rezonatör
3-) Osilatör Modülü

(3. Şıkta bahsedilen osilatör modülleri sıcaklık değişimlerine karşı da korunmuş oldukları için çok kararlı çalışırlar. )

Bir 16F84'de (+) gerilim ile

GND uçları arasına bir adet 0.1 uf’lık

kondansatör konması, istenmeyen

bazı gerilim dalgalanmalarını önler!

**TTL**(Transistor-Transistor Logic-Transistörlü Mantık Devresi):,

TTL’de aynı CMOS gibi entegre bir mantık devresidir.Ayrıca günümüzde en çok kullanılan entegre grubudur.Sayısal entegre yapımıyla ilgilenen tüm firmaların TTL imalatı mevcuttur.TTL grubu, 5 alt gruba ayrılır.

## Standart TTL

## Düşük Güçlü TTL

## Yüksek Güçlü TTL

## Schottky TTL

## Düşük güçlü Schottky TTL

Bütün alt grublar +5V beslama voltajı ile çalışır.Hız ce güç bakımından çeşitli farklılıkları vardır.

## **1.STANDART TTL:**

Şekilde Vedeğil kapısının eşdeğeri olan standart TTl devresi görülmektedir. Girişlerden biri veya her ikisi “0” olduğunda T1 doyuma girer.T2’nin base’i T1 üzerinden “0” a bağlanır.Bu nedenle T3 kesime girer.Çıkış “1” olur.Fakat çıkış voltajı T4 transistörünün CE uçları arasındaki voltaj ve VR4 gerilim düşümü nedeniyle yaklaşık 3,5V civarındadır.Her iki giriş “1” yapıldığında T1 kesimde,T2 iletimde çalışır.T3 iletime,T4 kesime girer.Çıkış “0” olur.Bu açıklamalar Vedeğil kapısının özellikleridir aynı zamanda.Standart TTL’in kapı başına güç harcaması 10mW,gecikme zamanı ise 10 nsn’dir.Maksimum hızıda 35MHz’dir.

## **2.DÜŞÜK GÜÇLÜ TTL:**

Standart TTL devresindekinin aksine devredeki bütün direnç değerleri büyütülmek suretiyle çekilen güç azaltılmıştır. Standart TTL devresindeki diyotta kaldırılmıştır.Bu devrede bi Vedeğil eşdevresidir.Kapı başına güç harcaması 1mW,gecikme zamanı 33 nsn,maksimum hızıda 3 MHz’dir.

## **3-YÜKSEK GÜÇLÜ TTL:**

Önceki devrelerdeki tüm dirençlerin küçültülmüş halinin olduğu devredir.Bu sayede çok güç çeker.

Bu grupta kapı başına güç harcaması 22 mW, gecikme süresi 6 nsn ve hızıda 50 MHz’tir.

## **4-SCHOTTKY TTL:**

TTL grubunun en hızlı çalışan alt grubudur.Kapı başına güç harcaması 19 mW, gecikme süresi 3 nsn, hızı da 125 MHz’tir.

## **5-DÜŞÜK GÜÇLÜ SCHOTTKY TTL:**

Düşük güçlü TTL ile,düşük güçle yüksek çalışma hızına erişilmiştir.Devrede bütün dirençler büyütülmüş ve T1 transistörü yerine Schottky diyotları kullanılmıştır.Kapı başına güç harcaması 2 mW, gecikme süresi 10 nsn, hızı da 35 MHz’tir.

**TTL TÜMLEŞİK DEVRELER İÇİN ÖNEMLİ VERİLER******

| **\*\*\*\*ENTEGRE ÇEŞİTLERİ \*\*\*\*** |  |
| --- | --- |
| 1-RTL "RESİSTOR TRANSİSTÖR LOJİK" DİRENÇ TRS.MANTIĞI |  |
| 2- DTL "DİODE TRS. L." DİYOT TRS. MANTIĞI |  |
| 3- HTL "HİGH TRS. L. " YÜKSEK EŞİKLİ MANTIK |  |
| 4- TTL " TRS.- TRS. L." TRANSİSTÖR-TRS. MANTIĞI |  |
| 5- ECL "EMİTTER COUPLED L. " EMİTERDEN BAĞLI MANTIK |  |
| 6- MOS " METAL OXİDE SEMİCONDUCOR " METAL OKSİT YARI İLETKEN |  |
| 7- C-MOS "COMPLEMENTARY METAL OXİDE SEMİ." TÜMLER-METAL OK.YARI İLET. |  |
| 8- I L2 "INTEGRATED INJECTİON LOJİK" TÜMLEŞİK MANTIĞI |  |
| **\*\*\*\*\*TTL ÇEŞİTLERİ \*\*\*\*\*** |  |
| 54 / 74 ORTA HIZLI TTL |  |
| 54H / 74H YÜKSEK HIZLI TTL |  |
| 54L / 74L DÜŞÜK GÜÇ TÜKETİMİ TTL |  |
| 54S / 74S SCHOTTLEY DİYODU KENETLENMİŞ TTL |  |
| **\*\*\*\*TTL ENTEGRENİN ÇALIŞMA DEĞERLERİ\*\*\*\*\*** |  |
| Güç kaynağının en yüksek mutlak değeri | **7V** |
| Çalışma için gerekli kaynak gerilimi | **4.75V-5.25V** |
| Giriş akımının en yüksek değeri 0 Durumu (Vg =0.4V için) 1 Durumu (Vg =2.4V için) | **-1.6mA + 40mA** |
| Güç tüketimi "Geçit başına" | **12mW** |
| Yayılım gecikmesi | **13ns** |
| En yüksek saat frekansı | **20Mhz** |
| Çıkış yükleme faktörü | **10** |
| Eşik gerilimi | **1.4V** |
| 1 Durumdaki Giriş empedansı "Zg1" Çıkış empedansı "Zç1" Çıkış gerilimi "olağan değer Vç" Giriş gerilimi en yüksek değeri | **440K 70 Ohms 3.5V 5.5V** |
| 0 Durumdaki Giriş empedansı "Zg0" Çıkış empedansı "Zç0" Çıkış gerilimi "olağan değer " Giriş gerilimi en yüksek değeri | **10 Ohms 4K 0.2V 0.5V** |
| Endüstriyel devrelerin dayanabildiği sıcaklık Çalışma için depolama için | **0 - + 70 Cº -55 +125** |
| Askeri dev. Çalışma sıcak. Çalışma için depolama için | **-55 +125 C -65 +150 C** |

## **CMOS İLE TTL ARASINDAKİ FARKLAR******

| **Çalışma Sıcaklığı** |  |  |
| --- | --- | --- |
| **Endüstri Tipleri****** | **:** | 0 0C ile +70 0C (74XX) |
| **Askeri Tipleri****** | **:****** | -55 0C ile +125 0C (54XX) |

| **Besleme Gerilimleri****** |  |  |
| --- | --- | --- |
| **TTL****** | **:****** | +5 V (+/- 0,25V) |
| **CMOS****** | **:****** | +3 V ile +18 V |

| **Gerilim Seviyeleri****** |
| --- |

**TTL******:0 V-0,8 V=" 0 "

*** Giriş***

*** Konumları***2 V-5 V=" 1"0,8 V-2 V=Belirsiz

**CMOS******:0 V-1,5 V=" 0 "3,5 Vveüstü=" 1 "1,5 V-3,5 V=Belirsiz

**TTL******:0 V0,4 V=" 0 "*** Çıkış***

*** Konumları***2,4 V-5 V=" 1 "0,4 V-2,4 V=Belirsiz

**CMOS******

|  | : | 0 V 'A çok yakın | = | " 0 " |  |
| --- | --- | --- | --- | --- | --- |
| Beslemenin %99'u | = | " 1 " |  |  |  |

AYRICA:

CMOS'un özelliği\[entegre olarak\] 0,5-1,5 volt arası çalışabilmesi.Bilgisayarların anakartlarında kullanılan entegreler CMOS’tur .Çünkü TTL entegrelerin girişine hiç birşey uygulamazsanız direkt çıkışı 1'e aktaracak ve sistemde soruna neden olacaktır.Ancak Cmos'larda eğer çıkışı aktif yapmak istiyorsanız illaki girişe 1 vermeniz gerekmektedir.

TTL Entegreler; Yapılarında bipolar transistörler kullanılır. Besleme gerilimleri 5V’tur. CMOS entegrelere göre güç kayıpları çok fazladır.

CMOS’ların yapıları FET türü transistörlerden oluşur. Besleme gerilimleri 3V ile 15V arasında olabilir. TTL’den çok daha az güç kayıpları vardır.

TTL daha hızlı ve yaygındır-çok güç kaybı görülür.

CMOS daha az güç kaybına neden olur-şilem hızı yavaştır.

**ANCAK **74HCTXXX ailesi TTL uyumlu (besleme gerilimi 5V), CMOS’un avantajları (çok düşük güç kayıpları) ile TTL’in avantajlarını (çok hızlı) bir arada bulundurur. Bundan dolayı en popüler entegredir.

| **DİJİTAL ELEKTRONİK DİJİTAL ELEKTRONİKTE SAYI SİSTEMLERİ****** |  |
| --- | --- |
| **DİJİTAL ELEKTRONİK ****** Dijital Elektronik, Analog Elektronikten sonra çıkan en gelişmiş elektronik teknolojisidir. Bazı analog sinyallerin saklanması ve daha az kayıpla taşınmasında kullanılır. Ayrıca Şu anda kullansığınız bilgisayarında temeli Dijital Elektroniktir. Harddiskte saklanan bilgiler dijital kodlarla saklanır ve yine dijital kodlarla işlemcide işlenir. Bir kişinin Dijital elektronik öğrenmesi için ilk olarak sayı sistemlerini çok iyi bir şekilde bilmesi gerekir. Sayı sistemleri Dijital Elektroniğin temelidir. Dijital elektronikte en fazla kullanılan sayı sistemi ikilik(binary) sayı sistemidir.0 ve 1 karakterleri kullanılır.Elektronik devre elemanlarının çoğunu 2 durumlu olarak çalıştırmak mümkündür.Örneğin;bir anahtar ya açıktır,ya da kapalıdır.Bir röle ya enerjilidir,ya da enerjisizdir.Bir transistör ya iletimde,ya da yalıtımdadır.Binary sayı sisteminde kullanılan “0” yokluğu “1” ise varlığı temsil eder.Bu sistemle tasarlanan cihazlar hem basit hem de,güvenilirdir ve hata olasılığı en aza indirilmiş olunur.Onluk sayı sistemi dijital sistemlerde kullanılsaydı,10 ayrı voltaj seviyesi ile çalışabilen elektronik bir cihazı dizayn etmek çok güç olacaktı.Ayrıca,yalnız iki voltaj seviyesi ile çalışan bir elektronik cihazı dizayn etmek çok daha basit ve kolaydır. |  |
| **1 ) - Sayı Sistemleri :** Dijital eletronikte dört çeşit sayı sistemi kullanılmaktadır. Bunlar : a) - Desimal Sayı Sistemi b) - Binary Sayı Sistemi c) - Oktal Sayı Sistemi d) - Hexadesimal Sayı Sistemi |  |
| **a) - Desimal Sayı Sistemi :** Desimal say sistemi normal sayma sayılardan oluşur. Yani, 0 1 2 3 4 5 6 7 8 9 sayılarından oluşur. On adet sayı bulunduğu için bu sayı sisteminin tabanı 10'dur. (158 10) şeklinde yazılır. Bu sayı sisteminde ise dört matematiksel işlem bilindiği gibidir. |  |
| **b) - Binary Sayı Sistemi :** Binary sayı sisteminde iki adet sayı bulunur. Bunlar 0 ve 1 dir. Bu yüzden Binary sayı sisteminin tabanı 2'dir. (1011 2) şeklinde yazılır.Aşağıda Binary sayı sistemi ile toplama, çıkarma, çarpma ve bölme işlemleri görülmektedir. |  |
| **Binary sayının Desimal sayıya çevrilmesi :** 101 Binary sayısını Desimal sayıya çevirelim. 1 x 2 ² + 0 x 2 ¹ + 1 x 2 º => 1 x 4 + 0 x 2 + 1 x 1 = 4 + 0 + 1 = 5 10 bulunur. | 2 ² = 4 2 ¹ = 2 2 º = 1 1 0 1 |
| ** Desimal sayının Binary sayıya çevrilmesi :** Desimal sayı Binary sayıya çevrilirken Binary sayının tabanı olan 2'ye bölünür. 9 10 Desimal sayısını Binary sayıya çevirelim. Tablodan görüldüğü gibi 9 sayısı 2 'ye bölünür. Bu işlem bölüm sıfır olana kadar devam eder. Kalan kutusundaki rakamlar aşağıdan yukarı doğru alınarak yan yana yazılır. Sonuç = 1001 2 | İşlem Bölüm Kalan 9 : 2 4 1 4 : 2 2 0 2 : 2 1 0 1 : 2 1 |
| **c) - Oktal Sayı Sistemi :** Oktal sayı sistemindede 8 adet rakam bulunmaktadır. Bunlar 0 1 2 3 4 5 6 7'dir. Taban sayısı 8'dir. (125 8) şeklinde gösterilir. Aşağıda Oktal sayılarla toplama, çıkarma, çarpma ve bölme işlemleri görülmektedir. |  |
| ** Oktal sayının Desimal sayıya çevrilmesi :** 25 8 oktal sayısını desimal sayıya çevirelim. 2 x 8 ¹ + 5 x 8 º => 2 x 8 + 5 x 1 = 16 + 5 = 21 10 bulunur. | 8 ¹ = 8 8 º = 1 2 5 |
| ** Desimal sayının Oktal sayıya çevrilmesi :** Desimal sayı Oktal sayıya çevrilirken Oktal sayının tabanı olan 8'e bölünür. 84 10 Desimal sayısını Oktal sayıya çevirelim. Tabloda görüldüğü gibi 84 sayısı 8'e bölünür. Daha sonra bölüm kutusundaki sayı tekrar 8'e bölünür. (Bölüm sıfır olana kadar). Kalan kutusundaki sayılar aşağıdan yukarı doğru alınarak yan yana yazılır. Çıkan sayı oktal sayıdır. Sonuç = 124 8 | İşlem Bölüm Kalan 84 : 8 10 4 10 : 8 1 2 1 : 8 1 |
| **d) - Hexadesimal Sayı Sistemi :** Hexadesimal sayı sisteminde 16 adet rakam bulunur.Bunlar 0 1 2 3 4 5 6 7 8 9 A B C D E F'dir. Tabanı ise 16'dır ve (1D2A 16) şeklinde yazılır. Aşağıda Hexadesimal sayılarlar toplama, çıkarma, çarpma ve bölme işlemleri görülmektedir. |  |
| ** Hexadesimal sayının Desimal sayıya çevrilmesi :** 4F8 16 sayısını Desimal sayıya çevirelim. 4 x 16 ² + F x 16 ¹ + 8 x 16 º => 4 x 256 + F x 16 + 8 x 1 = 1024 + 240 + 8 = 1272 2 bulunur. Hexadesimal sayılarla hesap yapılırken harf olarak belirtilen sayıların rakama çevrilerek hesap yapılması daha kolay olacaktır. Örneğin (C = 12 , A = 10 , F = 15) gibi. | 16 ² = 256 16 ¹ = 16 16 º = 1 4 F 8 |
| **Desimal sayının Hexadesimal sayıya çevrilmesi :****** Desimal sayıyı Hexadesimal sayıya çevirirken, Desimal sayı Hexadesimalin tabanı olan 16'ya bölünür. 100 10 Desimal sayısını Hexadesimal sayıya çevirelim. Desimal sayı, bölüm sıfır olana kadar 16'ya bölünür. Daha sonra kalan kutusundaki sayılar aşağıdan yukarı doğru alınarak yan yana yazılır. Sonuç = 64 16 | İşlem Bölüm Kalan 100 : 16 6 4 6 : 16 6 |

---
*Kaynak: `CMOS NEDİR  -  TTL NEDİR/CMOS NEDİR . TTL NEDİR.doc` — izzet — 2004*
