# Yazilim Geliştirme Teknikleri İle Yazilim Üretimi

## ** ****Yazılım Geliştirme Teknikleri ile Yazılım Üretimi**

Bir sistemin analizi yada yeni bir yazılım yaratımı müşteriden gelen talep ile olur. Müşteri yazılım geliştiricilerine ihtiyaçlarını ifade eder ilk aşamada. İhtiyaç belirlemede, düşünülen sistemin tam olarak bir canlandırması çizilmeli ihtiyaçların ifadesi yapılmalı sistem gelişiminde temel olarak kullanılacak formal doküman oluşturulmalıdır.

Bir yazılım gelişiminin aşamalarını daha ayrıntılı biçimde aşağıda görebiliriz. Bu şemaya Fision metodu diyoruz.

*ANALİZ*

Alt Sistem

*DİZAYN*

*UYGULAMA***

İlk adım olan gerekliliklerin yada ihtaçlar dökümanının belirlenmesi aşamasına bakalım. Müşteriden gelen talep doğrultuda ilk önce bu requriment document denen aşamanın geçilmesi gerekir bunu başarabilmek için örnek sorular aşağıdadır.

İhtiyaçların belirlemesinde sorulabilecek sorular:

Problemin kapsamı:

Yazılım ne için?

Yazılıma neden ihtiyaç duyulmuştur?

İhtiyaçlar:

Düşünülen kullanıcı tipi kimlerdir?

Sistem neler yapabilmelidir?

Ara yüze konulacaklar?

Uygulama kontexti:

Düşünülen donanım nedir?

Düşünülen işletim sistemi nedir?

Kabullenişler:

Hangi kabullenişler sistemin tasarlandığı şekilde çalışmasını sağlar?

Performans

Yanıt süresi,

Hafıza ve disk yeri talebi,

Cpu talebi nelerdir?

Gereklilik dökümanı belirlendiksen sonra analiz aşamasına geçebiliriz.

**Analiz aşamasının detaylı gösterimi **

**Prosedüre yönelik Analiz nedir?**

Prosedüre yönelimli analiz sistemi etkileşimdeki prosürlerle datayı ayrı olarak düşünür. Örneğin C dilinde datalar Structure’lara function’larda prosedürlere denk gelir.

Burada data dictionary kayıtlı olan prosedürlerin kullandığı bilginin tanımlarını içerir. Bu yaklaşım programcıyı , sistem bileşenlerini , bileşenler arasındaki ilişkileri ve nasıl bileşenlerle sistemin tasarlanıp işleneceği konusundan uzaklaştırır. Bu analiz tipinde prosedürlerden gelen tüm bilgi tek bir mantıksal analiz dökumanı içerisinde saklanır.

**Nesneye yönelimli analiz nedir?**

Bu sorunun cevabını verebilmek için ilk önce nesnenin ne demek olduğuna bir göz atalım. Geleneksel olarak programcılıkta bilgi ve kod bir birinden ayrı tutulur fakat nesneye yönelimli programlamada data ve tek bir görünür nesne haline gelmiştir. Bu şekilde data ve kod paketleri halindeki nesneler birbirleriyle mesajlar aracılığıyla iletişim kurarlar. Bir nesnenin yapabileceği her şey bu mesaj ara yüzleriyle temsil edilir böylece bir nesneyi kullanmak için içinde neler olduğunu bilmek zorunda kalmayız bu bize daha sonra nesneler üzerinde yapabileceğimiz değişiklikler açısından esneklik sağlar. Bu şekilde nesnelere sadece mesajlar üzerinden erişim sağlayarak bir tür data gizliliği sağlanır buna kapsülleme (encapsulation) denir.

Tüm bu yapılanların amacı yazılımı en kolay şekilde nasıl tekrar yazabileceğimiz sorusana cevap vermektir. Unutmamak gerekir ki “yazılım yazılmaz yeniden yazılır(Software is not written , its rewritten)”. Nesneye yönelimli programlamada amaç programı küçük sınıflara ayırarak sistemin esnekliğini artırmak buna bağlı tekrar yazma gibi durumları ortadan kaldırarak yazılım geliştirme sürecine en aza indirmektir ve dolasıyla masrafları düşürmektir.

Nesneye yönelik programlamada anlamamız gereken bir başka konuda sınıflardır. Kısaca söylemek gerekirse nesneler sınıfların tekil birer örnekleridir. Bu ne demektir? Bir örnekle konuya açıklık getirelim mesela elimizde bir ev sınıfı olsun bizde ev sınıfından pencere diye bir nesne çağıralım. Pencere bir ev sınıfı nesnesi örneğidir, ev sınıfı bu nesnenin yapabileceği işleri ve kendisini tanımlar. Bir sınıf birden fazla nesne üretebilir ve ev sınıfı nesnelerinin anlayabileceği mesajlar üretir. Bu tip sınıflardan nesne örnekleri yaratma olayına nesneye yönelik programlamada”Factory” denir. Nesnelerin gönderdikleri mesajlar içindeki kodlara verilen addır ve bu mesajlarla genelde argumanlarda yollanır bunlar genelde nesnenin neyi,ne zaman ne kadar yapacağı gibi sorulardır. Örnek olarak bir temizle mesajı “hangi pencere” veya “ne zaman” sorularının cevaplarıyla gelebilir.

Nesneye yönelik programlamada yaratmamış olduğumuz sınıfları daha spesifik alt sınıflara ayırabiliriz. Bunlara alt sınıflar(sub classes) denir, alt sınıflar yaratılığı atasına (parent class) ait tüm var olan mesajları ve davranışları da alır bu olaya miras (İnheritance) denir. Yani daha üst sınıflara ait mesajlar yeniden(reuse) kullanılabilir ve kendi alt sınıfımıza ait spesifik yeni mesajlar yaratabiliriz. Mesela ev sınıfımızdan bir oda alt sınıfı yaratalım ev sınıfından kalma bir evde “renk” mesajı oda sınıfında kullanılabilir veya oda için “yatak” gibi bir yeni mesaj tanımlayabiliriz.

Piyasada nesne yönelimli bir çok programlama dili vardır özellikle bu sayı her gün artan yeni internet yazılım geliştirme ortamıyla büyük bir artış göstermiştir. Ancak eskiden beri gelmiş kabul gören ve çok kullanılan üç programla dili vardır.

C++: C’nin Object oriented versiyonudur.

Java: Sun microsystems’in geliştirmiş olduğu bu dilin İBM, Microsoft, Symantec gibi versiyonlarıda bulıunmaktadır. Bu dilin çok tutulmasının nedeni internet ve internet uygulamalarında ve web browserlarla son derce uyumlu ve güvenilir olarak çalışabilir olmasıdır.

Smalltalk: Tam standardı oturmamıştır bu yüzden üç ayrı ticari sürümü vardır.** **

**VisualWorks** *ParcPlace-Digitalk, Inc.*

**Smalltalk/V and Visual Smalltalk** f *ParcPlace-Digitalk Inc.*

**VisualAge** *IBM*

Nesneye yönelimli analiz bir nesneye yönelimli sistem analiz tekniğidir. Birbiriyle iletişimde olan nesnelerin esas karakteristiğini ortaya koymada etkili bir tekniktir. Temel kavramları sistem bilgisinin biçimsel tanımı ve davranış biçimi modellemedir. Burada datalar arası ilişkiler mesajlarla , argümanlar aracılığıyla yapılan metotlarla olur.

Metod

Metod

Metod Metod Metod

Mesajların içerdiği metotlar gittiği yerdeki mesaj alıcı tarafından işlenir. Oo analizin temel kavramları sistem bilgisinin formal tanımına ve davranış biçimi modellemeye dayanır. NYA’de modellenen tüm bileşenler sistemin önemini kavratacak şekilde tasarlanır yani sistem nasıl uygulanacağı sorusu yerine gerçek ne olduğu sorusu üzerine inşa edilir

Nesneye yönelik analiz , prosedüre yönelik analizden farklı olarak sistemi “nasıl” sorusundan ziyade ne sorusu üzerine inşa eder böylece erken bir tasarım aşamasına geçişten programcıyı alı koyar.

**Nesneye Yönelik Sistem modellemin bileşenleri:**

OSA (Object-Oriented System Analysis): Kısaca NYA diyebileceğimiz bu kısım nesne yönelik teknikleri kullanarak sistemin analizini içerir.

OSS (Object-OIriented System Spesification): Formal şartların geliştirilmesinde kullanılan tekniktir.

OSD (Object-Oriented System Design): OSA modellerini istenilen özelliklerde tasarım modellerine aktarılmasını içerir.

OSI (Object-Oriented System İmplementation): OSD modellerinin uygulamaya dökülmesidir.

OST (Object-oriented Systems Testing): Muhtemel hataları bulmak için yapılır.

OSE: (Object-oriented Systems Evolution): Sistem bitirilip üretim aşamasına geçtikten sonra çalışmasının izlenmesidir.

OSR (Object-oriented Systems Reverse Engineering): Bitirilmiş Sistemin tersine aşamalardan geçirilebilmesidir.

**NYA’nın formal Temeli:******

Daha önce NYA’nın temel kavramlarının sistem data ve davranış biçimi modellemenin formal tanımlarına dayandığını söylemiştim. Formal tanımlara dayanan modeller model güvenirliğinin testi ve analizin tamamlanabilirliğinde kolaylık sağlar. Formal modelleme istikrarlı bir yorumlama sağladığından analizcilere iyi bir iletişim ortamı kurabilir daha da ötesi analizciler dışındaki gruplarla da iyi bir iletişim ortamı geliştirebilir.

**Nesneye Yönelik Analiz Bileşenleri:******

Nesneye yönelik analiz bize gerçek dünyadaki herhangi problemi modelleme bize gerekli tüm öğeleri verir. Bir bütün olarak gözüken NYA aslında üç ana parçadan oluşur:

Object-Relation Model(ORM) : ORM gerçek dünyanın tüm üyelerini sınıfları , nesneleri , nesneler ve sınıflar arası ilişkileri nesnelerin ve sınıfların tanımlarını göstermemize yarayan yoldur.

Object-Behaviour Model(OBM): OBM adından da anlaşılacağı gibi nesnelrin davranışlarını tanımlayan yoldur yani nesnenin mümkün durumları ve başka bir duruma nasıl ve neden geçeğini açıklar.

Object-İnteraction Model(OİM): OİM nesnelerin diğer nesnelerle olan etkileşimlerini tanımlayan yoldur.

**Object-Relation Model:**** ******

OSA’nın statik kısmıdır . Nesnelerin hangi sınıflara ait olduğunu nesenler arası ilişkileri belirler. ORM sınıflar , nesneler , kısıtlar , ilişkiler , ilişki setleri ve açıklamalardan oluşur.

ORM: ORM aşağıdakileri kapsar.

-Nesneler

-Nesne Sınıfları

Leksikal Nesne Sınıfları

İlişkisel Nesne Sınıfları

Yüksek Seviye Nesne Sınıfları

-İlişkiler

-İlişki Setleri ve özel formları

Genelleme /Özelleştirme

Roller

Toplamsallık

Tümsellik

-Kısıtlar

Katılım Kısıtları

Tekrarlanma Kısıtları

Nesne-Sınıfı Kardinalite Kısıtları

Özelleştirilmiş Nesne Sınıfları

Genel Kısıtlar

-Yüksek seviye ilişki setleri

-Notlar

## **Nesneler:**

Nesneler siyah noktalarla ifade edilir ve özeldirler. Özelden kasıt tek olmalarıdır tek bir şeyi ifade ederler genel bir tanım olamaz.

** Ahmet İstanbul 7:20**

Yukarıdakilerin her biri nesnedir fakat aşağıdakiler değildir.

**İsim Yer Saat**

Buradaki örneklere sınıf deriz çünkü belirli nesleri belirmezler daha çok nesnelerin genel isimleridirler .

Nesneler soyut veya somut olabilirler nesneleri üç ana gruba ayırabiliriz.

Concrete Nesne: Canlılar , cansızlar , eşyalar , ağaçlar , binalar , insanlar , hatvanlar kısacası somut nesnelerin hepsidir.

Conseptual Nesne: Tarih , yüzde , sözleşmeler , organizasyonlar gibi soyut nesnelere verilen addır.

Event and State Nesne: Sıcaklık derecesi , yağmur yağması , ürün satma gibi durumlar ve olaylara denir.

## **Nesne Sınıfları:**

Nesne sınıfları dikdörtgenlerle ifade edilir. Nesne sınıfları ortak özellikleri olan nesne setlerine denir. Nesne sınıfı olmak için ORM’nin belirlediği kısıtlara uyulması gerekir. Zamanla bir nesne bir kaç sınıfın üyesi olabilir buna sınıf göçü denir. Bir nesne sınıfı içindeki nesne sayısı nesne sınıfı kardinalite kısıtları tarafından belirlenir. Nesneler ilişki setleriyle birbirine bağlanabilir.

Lexical , ilişkisel ve yüksek seviye olmak üzere nesne sınıfları da alt bölümlere ayrılır.

**Lexical Nesne Sınıfları:******

Lexical sınıftaki nesneler gösterimleriyle birebir ifade edilebilirler çok genel değildirler. Örneğin renk sınıfı bu sınıfta sadece aklımıza renkler gelir ama bir taşıt sınıfı lexical değildir çünkü araç kara,hava,deniz taşıtı veya daha da çeşitlendirebileceğimiz alt sınıflara da ait olabilir. Genel sınıf gösterimiyle aynı gösterimdedirler fakat dikdörtgenler içine aynı anlama gelen birden fazla kelimeyi girebiliriz. Gösterimde kelimelerin arasına dikine çizgi koyarız ve noktalı dikdörtgenlerle belirtiriz lexical nesne sınıfını.

Lexical nesne sınıfı diğer ilişki setleriyle etkileşebilir ve diğer normal nesne sınıflarının sahip olduğu katılım kısıtlarına sahiptir. Ayrıca kesikli diktörtgenin köşelerine yazılan kardinalite kısıtlarına sahiptirler.

**İlişkisel Sınıf:**

Bazen nesne sınıfıyla ilişki seti arasındaki fark hafif seçimseldir. Böyle bir durumda OSA bize bir ilişki setine bir nesne sınıfı gibi davranmamıza olanak verir. Bunlara ilişkisel nesne sınıfı denir.

sürer

Örneğin *hayvanat bahçesi hayvan satın alır* ilişki seti **Satın Alma** nesne sınıfı olarak kabul edilebilir. Nesne sınıfı **Satın Alma** , Satın alım tarihi ve Fatura Nosuna sahip olduğunu belirten vb. ilişkilere katılabilir.

**Yüksek Seviye Nesne Sınıfı:******

Yüksek sınıf ise diğer tüm ilişki sınıflarını , kısıtları , notları içerir ve içi taralı dikdörtgenler biçimde gösterilir. Yüksek seviye nesne sınıfları açık ve kapalı olmak üzere iki şekilde gösterilir. Açık gösterimde Yüksek-Seviye Nesne Sınıfının tamamıyla neler içerdiğini görebiliriz; kapalı gösterim bütün içeriği saklar.

Aşağıda Telefon yüksek seviye nesne sınıfının açık gösterimi vardır ve Telefon priziyle ilişkisini aktarır.

Bu aşağıdaki ise Telefon yüksek seviye nesne sınıfının kapalı formda gösterimidir.

Bir ilişki setinin kapalı gösterimde yüksek seviyeli bir nesne sınıfına geçerken etiketsiz kesikli çizgiyle gösterildiğine dikkat edin.

## **İlişkiler:**

İlişkiler nesneler arasındaki mantısal bağlantıları gösterir. Örneğin: Ali fort ka kullanır cümlesindeki *kullanır* ilişkimizdir. ORM’de ilişkiler çizgiyle gösterilir ve bir ad verilir. Ad genellikle ilşkiyi anlatan bir cümledir. İlişkinin adında bağladığı her iki nesnenin adınıda kapsamasına dikkat edilmelidir.

Ali ford ka kullanır.

Ali ford ka

İlişkinin bağladığı nesne sayısına göre ilişki çeşidi değişir. İki nesne bağlanırsa ikili üç nesne bağlanırsa üçlü dört bağlanırsa dörtlü vb. gider.

Ali ford ka

15 Mayıs 1997

## **İlişki Setleri:**

Bir ilişki setinde ise ilişkiler nesne sınıfları arasında kurulur ve gösterimi şu şekilde olur.

İnsanlar araç sahibi olur

Şekilden de görüldüğü üzere ilişki elmas şekliyle ifade edilir. Gerek ilişkilerde olsun gerek ilişki setlerinde ilişkiler bir tane olmak zorunda değildir. Birden çok nesne yada sınıf arasında ilişki kurulabilir. İkili ilişkilere binary , üçlülere ternary , dörtlülere quartary vs. denir.

Yüksek seviye bir sınıf diğer tüm ilişki türlerini , kısıtları , sınıfları ve nesneleri içerir. Modeli basitleştirmeye yarar.

İlişki setlerinin özel biçimleri vardır bunları özetlemek gerekirse:

“İs a” ilişki setleri Generelazation/Specilazation tipidir.

“is part of” ilişki setleri Aggregation tipidir

“is member of” ilişki setleri Association tipidir.

**Genelleme:**

Genelleştirme/Özelleştirme **is a **ilişki setini belirtir ve nesneye yönelik programlamanın temellerindendir. Genelleştirme/özelleştirmedeki ana fikir bir nesne sınıfının (özelleştirme) bir diğerinin altsınıfı olmasıdır. (genelleştirme)

ORM’de genelleme/özelleştirme bi uçu genellemeye giden ve karşı tabanı da özelleştirmeye giden saydam bir üçgen ile belirtilir. **İs a** ilişki seti açıkça yazılmaz çünkü ilişki saydam üçgende kapsanmıştır. **İs a** ilişkisinin yönü özelleştirmeden genelleştirmeye doğrudur.

Aşağıdaki örnekte taşıt bir genellemedir ve uçak ise ,uçağın özel bir tür taşıt olduğunu ifade eden , özelleştirmedir. Uçak nesne sınıfındaki her nesne taşıt nesne sınıfınında bir üyesi olduğundan uçak sınıfı taşıt sınıfının alt kümesidir denir. Başka bir deyişle taşıt uçağın , genellemesi ve uçakta taşıtın özelleştirmesidir.

Diyagramda hiçbir katılım kısıdının olmadığı fark edilebilir; çoğu zaman bunlar güvenle göz ardı edilebilir. Özelleştirmede , özelleştirme nesne sınıfındaki her nesne genelleme nesne sınıfında da olduğundan ,her zaman katılım kısıdı 1:1’dir. Bu durumda her uçak bir taşıttır. Genellemede iki olanak vardır. En çok kullanılanı 0:1’dir. Diğer olasılık ise genelleme sınıfındaki nesne setlerinin her zaman özelleştirme sınıfındakilerle aynı olmasıdır.

Bu durumda katılım kısıtı 1:1’dir. Unutmamalıdır ki modellenen sistemin katılım kısıtları genelde tüm dünya için geçerli değildir. Örneğin eğer modellediğimiz sadece uçaklarla ilgilenen bir bilgisayar sistemiyse 1:1 katılım kısıtı uygun olacaktır. Buna rağmen gerçek dünyada bütün taşıtlar uçak değildir fakat bu sistemde bütün taşıtlar uçaktır.

**Çoklu Genelleme/Özelleştirmeler ******

Bir nesne sınıfı birden fazla nesne ile is a ilişkisine sahip olabilir. Bu durum ORM’de şeffaf üçgenin tabanından özelleşen nesne sınıflarına ve genelemedeki nesne sınıfına giden köşeden çizgi çekerek belirtilir.

Aşağıdaki örnekte Bakıcı nesne sınıfının birçok özelleştirmesi vardır. Bu ilişki seti “Eğitmen bir bakıcıdır ve besleyici bir bakıcıdır ve veteriner bir bakıcıdır.” şeklinde okunur.

Buradaki örnek ise bir özelleştirme için çoklu genellemeleri temsil eder.

Çok sık meydana geldiklerinden daha önceden tanımlı dört tip özelleştirme kısıtı vardır:

-Birleşim (Union)

-Ortak hariç tutma (Mutual exclusion)

-Bölüşüm (Partition , Hem union hem mutual exclusion )

-Kesişim (İntersection)

Diyagram bu tiplerden hiç birine sahip olmadığı sürece özelleştirme sınıflarının sayısında hiç bir kısıtlama olmaz. Bu örnekte bir çalışan bir eğitmen olabileceği gibi besleyici de olabilir. Başka bir çalışan eğitmen , Besleyici ve tur rehberi olabilir. Bir çalışan herhangi bir özelleştirmenin sahibi olmayabilir. Bir yönetici bir çalışan olabilir fakat bu diyagram üzerinde hiç bir özelleştirme sınıfına dahil değildir.

Miras nesneye yönelik programlamanın temel elemanlarından olduğundan bu özellik OSA’da tam olarak desteklenmiştir. Özünde özelleştirme nesne sınıfları ilişki setlerini miras olarak alır ve genelleme nesne sınıflarından gelen , davranışları ve kesişimleride kapsayan , diğer tüm ortak özellikleri de miras olarak alır.

## **Roller:**

Bir rol ilişkiye katılan tüm nesnelere özel bir isim veren ilşki setinin yanına yazılan bir etikettir. Bir rol ORM’de ilişki setinde uygulandığı nesne sınıfının yanına yazılarak belirtilir.

Bir rol genelleme /özelleştirme ilişkisini modellemenin kısa yoludur.. Yukarıdaki örnek aşağıdaki gibide modellenebilirdi.

Rolü içeren ilişki normal katılım kısıtlarına sahiptir.

## **Toplamsallık (Aggregation):**

Toplamsallık ilişki setinin is **a part** of veya **subpart of** bölümünü temsil eder. Bu toplamsallık sınıfındaki herhangi nesnenin , alt sınıflardaki diğer nesnelerden oluştuğunu gösterir.

Örneğin Toplamsal sınıf bina , temel , ilk kat , ikinci kat gibi alt sınıflara bölünebilir.

Toplamsallık ilişki seti ORM’de köşelerinden birinden toplamsallık sınıfına giden ve karşıt tabanda her biri alt sınıflara giden çizgilerden oluşan içi dolu bir üçgenle temsil edilir.

Örneğin :

Bu ilişki seti “Temel binanın alt sınıfıdır ve ilk kat binanın bir alt sınıfıdır ve ikinci kat binanın alt sınıfıdır.” diye okunur.

Toplamsallık ilişki seti katılım kısıtlarına sahiptir. Her bir alt sınıfın yanındaki kısıt toplamsallık sınıfında her bir alt sınıftaki nesneyle kaç tane ilişkili olabileceğini belirtir.

**Kısıtlar:**

Kısıtlar olmadan da bir sistem diğer bileşenlerle geliştirilebilir. Kısıtların amacı sistemin çalışmasını daha tatminkar hale getirmektir. Örneğin

kullanır

İnsanlar için araç kullanma yaşı 18 ve üstü belirtilmesi bir kısıttır. Kısıtlarında çeşitleri vardır.

Kardinalite kısıtı :Sınıftaki neslerin sayılarıyla ilgili kısıttır.

Katılım (participatiant) ve ön görünüm (Co-occurance) kısıtları ilişkilerle ilgi kısıtlardır.

Genel kısıtlar: Diğer kısıt türleri buna girer.

**Notlar: **Semantik dizilimde bir anlamları yoktur sadece okuyucuya açıklayıcı bilgi vermek amacıyla italik harflerle yazılır.

**Object Behaviour Model:******

OSM ‘nin ,sistem içindeki nesnelerin davranışını açıklaya yönelik bölümüdür. OBM’nin üç ana bileşeni vardır:

Nesnelerin varoluşlarından doğan durumlar.

Nesnelerin bir durumdan bir başkasına geçmesine neden olan şartlar.

Geçişlerde ve durumlarda nesnenin yaptığı hareketler.

**OBM bileşenleri:**

OBM bileşenlerinden ilki olan nesnelerin durumlarına kısa bir gözatalım.

**Durumlar (States)** nesnelerin pozisyonlarını , hareketlerini , evrelerini kısacası bulundukları hali tarif eder.

Durumları belirlemek için belirli bir yol olmamasına rağmen nesnelerin durum hallerini çıkarabiliriz. Örneğin “Ali okula arabayla gidiyor.” cümlesinde durumlar için gitme işi bir durumdur çünkü bir yapılan bir hareketi belirtir. Aynı şekilde Ali’nin pozisyonu için arabada diyebiliriz bu da bir durumdur yada başka bir düşünceyle okula arabayla gitme işinin bir faz olarak alınabilir işte bu yüzdendir ki durumları belirtmek biraz sezgiseldir.

Durumların gösterimi kenarları yuvarlatılmış dikdörtgen şeklindedir.

Durumların olumlu ve olumsuz olmak şeklinde iki halleri vardır. Bu haller kapalı – açık , hazır – hazır değil gibi düşünülebilir. Daha düşük seviyedeki durumlar , geçişler , kısıtlar ve notların bileşiminden oluşan durumlara yüksek seviyeli durumlar denir.

Genel akışda bir durumdan diğerine geçerken biri aktif yapılırken diğeri inaktif yapılır ama istisnalarda mevcuttur. Üç tür akış istisnası mevcuttur; çoklu threatler (multiple threats ), önceki durum birleşimleri (Prior state conjuction ) , sonraki durum birleşimleri ( Subsequant state conjuctions ) . Kısaca bu üç öğeden bahsedelim. Threadler yürütme veya kontrol akışına verilen addır. Çok threatlerde bir nesne bir durumdan diğerine geçerken bir durumu bitirmek zorunda değildir. Bunun karşılığı günlük hayatta iki işi aynı anda yapmak olabilir. Örneğin:

Bu akıştan da anlaşılacağı gibi koltukta oturma durumundan yemek yeme durumuna geçmek için ilk durumu bitirmek zorunda değiliz koltukta otururken yemeğimizi de yiyebiliriz.

Yemek yeme durumundan bizi televizyon izleme durumuna geçiren eğlence geçiş buna tetik diyebiliriz. Aynı şekilde yemek yerken televizyonda izleyebiliriz. Akışta görülen sonu yarım daire biçiminde oklar durum geçişlerinde çoklu durum threadlarını işaret eder ve önceki durumun bitmediğini ifade eder.

İkinci akış istisnası olan önceki durum birleşimleri ise bir geçişin gerçekleşebilmesi için bir kaç ön durumun oluşması gereken durumlardır.

Bu gibi bir durum önceki durum birleşimine istisnasına örnektir. Bu akıştan da görüldüğü üzere önceki iki durum bitirildikten sonra haber saati geçişiyle bir başka duruma geçebiliriz buna bir nevi ön koşul diyebiliriz.

Son akış istisnası ise sonraki durum birleşenleri de adından anlaşılacağı üzere bittiği zaman birden fazla durumu aktif hale getiren durumlara verilen isimdir.

Haberlerin bitmesi yemek yeme , müzik dinleme ve uyuma gibi üç farklı duruma geçişi sağlamış.

**Geçişler(Transitions):**

Nesneye yönelik sistem analizinde nesneler geçişler üzerinden durum değiştirirler. Gösterimi ikiye bölünmüş dikdörtgen şeklindedir. İlk kısma triger yani tetik denir burası durum değiştirmenin başlaması için gerekli koşulu barındırır. Alt kısım ise tetik sonucu verilen tepkinin açıklamasını içerir. Tetik (triger) şartları ve olayları içeren mantıksal kısımdır ve olaylar önlerinde @ sembolünü taşırlar. Hareket (action) kısmı ise bir alt duruma geçemeden önceki yapılacak hareketleri içermelidir. Durumlardan farklı olarak hareketler bitmelidir. Geçiş simgesinin sol üst köşesinde geçiş belirteci vardır bu sadece geçişin ismini belirtir ve braketler içine yazılır. İlk geçişin önceki durumu yoktur ve her zaman aktiftir. Son geçişin ise hiçbir sonraki durumu yoktur ve kendinden önceki tüm durumları bitirir. Daha aşağı seviyedeki durum , not ve kısıtlardan oluşan geçişlere yüksek seviyeli geçişler denir. Tipik bir geçişin gösterimi aşağıdadır.

\[Belirteç\]

**İlk Geçişler (İnitial Transitions):**

*İlk geçiş şekli*

İlk geçişler ilk durumları harekete geçirir önceki durumları yoktur ve her zaman hazır haldedir. Bitmiş durumlar ağının ilk başlangıdır ve her ne zaman tetiklenirse ilk geçiş başlar. İlk geçiş ateşlendikten sonra ilk durum veya durumlar aktifleşir.

Bir çok durumda ilk geçişler durum ağının başlangıçıdır bu bazı oluşum olaylarının olduğunu gösterir yani bir nesne veya nesneler sistemde gözükmeye başlar (Böylece ilk değerlerini alabilirler). Buna genelde tetik denir ve @ sembolüyle gösterilir.

*İlk geçiş için şekil*

Bazen ilk durum aksiyonu boş olabilir böyle bir durumda ilk durumu düşey düz bir çizgiyle belirtiririz.

*İlk geçişin kısa gösterimi***

**Son Geçişler:******

Son geçiş hiç bir alt duruma birleşimi olmayan geçişlere denir.

Son durumlarda da ilk durumlarda oldoğu gibi eğer geçişin aksiyon kısmı boşsa kısa olarak Düşey düz çizgiyle belirtilir.

Aşağıdaki veteriner nesne sınıfında iki durum arasındaki geçişi aşağıda daha iyi görebiliriz burada dikkat edilmesi gereken şey Action kısmındaki hareketlerin bitmeden diğer duruma geçişin sağlanmamasıdır.

Burada geçiş anlık değildir bunu geçiş zamanlama diyagramından daha iyi anlarız . Hasta hayvan t1 anında getirilmiştir ama veteriner müsait olmasına rağmen t2 anına kadar harekete geçmemiştir bu geçikme gri kutuyla gösterilmiştir t2 ve t3 anları arasında ekipmanlarını almış temizlenmiş ve maskesini takmıştır. Tüm bu aşamalardan sonra alt duruma geçebilmiş ve hasta hayvanın tedavisine başlamıştır.

Burada tetik şartlar ve olaylara biraz daha değinelim.

**Tetikler **genelde sistem şartlarını ve olaylarını tarif eden mantıksal cümlelerdir. Bir geçişin trigeri gerçekleştiğinde True (doğru) olur ve geçiş başlar. Koşulara bağlı tetiklerle olaylara bağlı tetikler arasındaki önemli ayrımın yapılması gerekir.

**Koşullar** sistemin durumu nesnenin durumu veya varlığı veya nesneler arasındaki ilişkilerin varlığı hakkındaki mantıksal ifadelerdir. Koşulara örnek vermek gerekirse

hesap 1.000.000 TL altında

müşterinin kredi kartı var.

Koşullara bağlı tetiklerde koşulun doğru olduğu herhangi bir anda geçiş başlayabilir. Koşul doğru olduğunda geçiş başlayacaktır ve tetik hangisinin daha önce olduğuna bakmadan ateşlenecektir.

Bu ilk örnekte ilk önce geçiş doğru olur daha sonra koşul sağlanır ve geçiş başlar.

İkinci örnekte ise ilk önce koşul doğrulanmıştır fakat geçiş doğrulanmasına kadar geçiş başlamamıştır.

Bu örnekte ise geçişin geçerliliğini kaybettikten son koşulun sağlanmasıyla geçişin başlamayacağını gösterir.

**Olaylar:**

Olaylar nesnelerin veya ilişkilerin oluşturulmasını silinmesini aktivetin başlatılmasını bitirilmesini ve mesajların diğer nesneler tarafından kabulünü içeren sistem değişiklerine verilen addır.

Çalışan kovulur.

Müşteri bir hesap açar.

Olaya dayalı tetik sadece geçiş doğrulandığında belirli bir anda koşul sağlanırsa ateşlenir.Bu tip geçiş başlatan olay tetiklerine olay monitorleri adı verilir ve önünde @ işaretiyle belirtilir.

Olay geçişten önce veya sonra olursa geçiş ateşlenmez.

**İstisnalar ( Exceptions):**

İstisnalar ( Exceptions)** **normal sistem akışında yeri olmayan olay veya şartlardır. Bunu akış istisnasıyla karıştırmamak lazımdır. Akış istisnası durumlarını sistem içinde normal karşılanır fakat istisnalar bu istisnayi hali belirtmek için içinde dikine çizgi bulunan okla belirtilir. İstisnaları daha iyi açıklamak için bir örnek verelim. Elimizde dışarı çıkmayı sevmeyen bir adamımız olsun.

Dışarı çıkma hali adamımız için bir istisna olacağından bu bir istisna (exception) olarak kabul edilir ve durum ağında birden fazla istisna mümkündür.

**Threadler:******

Threadler yapılışın veya kontrolün akışıdır. Bir nesne bir anda birden çok durumda veya geçişte olabilir böyle bir durum çoklu threadlerin ortaya çıkmasıyla sonuçlanır. OBM de bir durumdan geçiş yapılmışsa bile geçişin yapıldığı durum halen var olabilir. Bu durum bir ucunda yarım halka bulunan ok ile belirtilir.

Burada görüldüğü gibi koşucu hala koşuyor olabilir ve aynı andada walkmani açıp müzik dinleyebilir Bu durumda başka bir thread başlatılmış ve koşucu birden fazla durumdadır. Çoklu threadlar geçiş bittiğinde birden fazla duruma gidildiğinde de ortaya çıkar ayrıntılar için aşağıdaki örneği inceliyelim.

Bu örnekte koşucu koşmayı bırakmış ve hala müzik dinliyor olabilir. Bir insan varlığının bitmesi için son geçişe gelinmesi ve ya bir istisna tarafından bitirilmesi gerekir.

Threadler bir çok yolla birleştirilebilir. Aşağıdaki örnek bir insanın sinema içinde durumunda iken bir threadle pop-corn alma durumuna geçişinini ve tekrar threadları tekrar sinema içinde durumunda birleştirilmesini anlatır. Var olan temel bir duruma geçiş olduğunda bağlanan thread yok olur ve durum kalır. Burada , sinema içinde temel durumundan pop-corn alma durumuna tekrar bağlanmasında görebiliriz.

Buradaki örnek tetiği film bitti olan geçişin aksiyonunu hazır olduğunda binayı terket veya Pop-corn alma durumu bitmeden sinema dışı durumuna geçişi engelleyen herhangi bir aksiyon olarak kabul eder. Bu halde thread sinema içinde durumunda hapsedilmiştir.

Threadlerin birleştiği bir başka durum ise bir geçişin başlaması için birden çok durumun gerektiği durumlardır. Aşağıdaki örnekte bunu görebiliriz.

**KISITLAR:**

**Kısıtlar** da ORM’de olduğu gibidir. Ortaya çıkabilecek hatalı durumları engellemek için konur. Karar verilmemiş ve kararsız durumlar için genel bir çözüm yolu gösterir. Örnek olarak üsteki örnekte sıkılan adam her seferinde televizyon izleyebilir . Bu soruna her seferinde tüm durumları günde en az bir kere yapması koşulunu koyarak aşabiliriz. Fakat gene unutmamalıdır ki adamımız dışarı çıkmayı sevmediğinden bunu bir notla belirtebiliriz.

**Gerçek Zamanlı Kısıtlar:******

Sıkça Belirli olayların bir nesne tarafından veya bir nesne üzerinde yapıldığını göstermek isteriz. Bunlara gerçek zamanlı kısıtlar denir. Bu kısıtlar tipik olarak ilk durumlar ağı tamamlandıktan sonra modele eklenir ve durum ağ diyagramında “{}” süslü parantezler arasında text olarak gösterilir.

Gerçek zaman kısıtları bütün bir geçişşe , bir tetiğe , bir aksiyona , bir duruma veya yol

işaretçilerine uygulanabiilir.

Şekil birde bütün bir geçişe uygulanan gerçek zamanlı kısıtı görebiliriz. Bu şekil aslan terbiyecisinin boş durumundan aslanı arama durumuna geçişinin 5 dakikadan daha uzun süremeyeceğini gösterir.

Tetiğe uygulanan gerçek zamanlı bir kısıta , geçişin tetiklendiği anla nesnenin o anki durumunu terk edip geçişe giridiği an arasında kalan izin verilen zaman denir. Aşağıdaki şekilde ise gerçek zaman kısıtı geçişin aksiyon kısmına uygulanmıştır. Bu örnekte bir kere hasta hayvan geldiğinde veteriner boş durumundan çıkar ve ekipmanların toplanması, maskenin takılması 5 dakika içinde gerçekleşir.

Gerçek zaman kısıtları bir aksiyonlar bütününe veya tek bir durumu veya geçişi kapsarsa yol işaretçileri (path markers) kullanılır. Bir geçişten çıkan ok üzerinde bulunan yol işaretçileri alt bir duruma geçişe girişi belirtir. Geçişlere giren yol işaretçileri ise ilk durumdan çıkış zamanını belirtir. Aşağıdaki örnekte bunu görebiliriz.

PAGE 1

PAGE 1

Bakım

Uygulama

Tasarım

Analiz

İhtiyaçların belirlenmesi

DATA

Prosedür

## **Global Data**

DATA

DATA

Prosedür

Prosedür

**D**

**A**

**T**

**A**

** D**

**İ**

**C**

**T**

**İ**

**O**

**N**

**A**

**R**

**Y**

Program

Miras grafikleri

(İnheritance Graphs)

Sınıf tanımları

(Class descriptions)

Görünürlük grafikleri (Visibility Graphs )

Nesne etkileşim grafikleri

(Object İnteraction graphs)

Nesne Modeli

(Object Model)

Arayüz Modeli

(İnterface Model)

Gereklilikler dokümanı

(Requriments documents)

Triger açıklaması

Action açıklaması

İsim

Balık

Saat

Kent | Şehir | İl

Renk

Hayvanat Bahçesi

Hayvan

Alım

Tarihi

İnsanlar

Araç

Araç

İnsanlar

Yaş>=18

Durum İsmi

Eğlence istedi

Açıktı

Koltukta oturmak

Yemek yemek

Televizyon izlemek

Ödev çalışıyor

Haberleri izleme

Yıkanıyor

Haberler saati geldi

Haberleri izleme

Yemek yiyor.

Müzik dinliyor.

Uyuyor.

Haberler saati bitti.

Koltukta oturuyor

Müzik dinle

Kitap oku

Televizyon izle

ADAM

Sıkıldı

Dışarı çık

ADAM

Dışarı çık

Sıkıldı

Televizyon izle

Kitap oku

Müzik dinle

Koltukta oturuyor

ADAM

Sıkıldığında her durumu günde en az bir kere yapmalıdır.

*Dışarı çıkma birden fazla seçmemekte fayda vardır.*

@ hasta hayvan getirilir

ekipmanları alır

temizlenir

maskesini takar

Müsait

Hasta hayvana bakar

VETERİNER

Müsait durumda

Geçiş Durumunda

Hasta Hayvana Müdahale Durumunda

Ekipmanları alır

Temizlenir

Maskesini takar

t1

t2

t3

Geçiş doğru

Koşul doğru

Geçiş Başlar

Geçiş Başlar

Koşul doğru

Geçiş doğru

Olay Olur

Koşul doğru

Geçiş doğru

Geçiş olur

Geçiş ateşlenir

Olay Olur

Olay Olur

Geçiş olur

Geçiş Hiç bir Zaman Başlamaz

Açılış

Açılış Zamanı

Kapıyı aç

Dükkan

\[0\]

Müşteri

\[1\]

\[0\]

\[2\]

\[3\]

@ içeri girer

Raflara gider

Bir şeyler Arama

İstrediğini bulur

Raftan alır

Başka şeylere ihtiyaçı var veya yok

Parası yeter mi bakar

Ödeme

Cıkış yapılır

Yürüme

@LOGIN

Parola Sor

Doğrulama

@LOGOUT

Çıkışı Onayla

Öğrenci

Öğrenci

@Mezun oldu

Koşuyor

Müzik dinliyor

Walkman’i açtı

## )

Motor kapalı

Kontağı çevirdi

Motor çalışıyor

Elektrik geldi

Eksoz Dumanı başladı

Koşuyor

Walkman’i açtı

Müzik Dinliyor

Walkmani Kapatıldı

Piller bitti

Koşucu Yoruldu

Dinleniyor

Film saati

Sinema içi

Açıktı

Pop-corn aldı

Pop-corn alma

Film bitti

Sinema dışı

Dükkan içinde

Para var

Para kadar yiyecek aldındı

Kasada

Aldıklarının parası verildi

Dükkan dışında

Boş

Aslanı ara

@ aslan kaçar

organize arama grubu

{ < 5 Dakika }

Aslan Terbiyecisi

Şekil 1 Bütün geçişe uygulanmış Gerçek Zaman Kısıtı

Boş

Hasta hayvana bak

@ hasta hayvan gelir

ekimanı toparla

maskeyi tak

Yem hazırla

Yılanları besle

@ besleme zamanı 1

Veteriner

Bakıcı

{a}

@ besleme zamanı 1

Yem hazırla

@ besleme zamanı 1

{b}

a dan b’ye < 1 saat

Metod

Satın Alma

0:\*

1

Satın Alır

Fatura Nosu

Var

Var

1

1

1:\*

1

Telefon

Telefon Prizi

Bağlantı kablosu

Baz

Tuş Paneli

Tuş

Tuş Etiketi

Ahize Kablosu

Ahize

Takılır

0:1

0:1

Takılır

Takılır

Takılır

Sahip

Sahip

Sahip

1

1:\*

1

1

1

1

1

1

1

1

12

1

1

Telefon Prizi

**Telefon**

*İkili İlişki*

*Üçlü İlişki*

Ali 15 Mayıs 1997’den beri ford ka kullanır.

Taşıt

Uçak

Bakıcı

Eğitmen

Besleyici

Veteriner

At

Eşek

Katır

Hayvan

Bebek Hayvan

Ebeveyn Hayvan

1:\*

2

Çocuğu var

Hayvan

Ebeveyn Hayvan

Bebek Hayvan

1:\*

2

Çocuğu var

Bina

Temel

İlk Kat

İkinci Kat

1

1

1

1

1

1

---
*Kaynak: `YAZILIM GELİŞTİRME TEKNİKLERİ İLE YAZILIM ÜRETİMİ/YAZILIM GELİŞTİRME TEKNİKLERİ İLE YAZILIM ÜRETİMİ.doc` — Orkun — 2004*
