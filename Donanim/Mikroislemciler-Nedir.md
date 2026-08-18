# Mikroişlemciler Nedir

## **GİRİŞ**

MİKROİŞLEMCİ NEDİR?

MİKRODENETLEYİCİ NEDİR?

MİKRODENETLEYİCİLER HAKKINDA GENEL BİLGİLER

PIC PROGRAMLAMA İÇİN NEYE İHTİYACIMIZ VAR

**MİKROİŞLEMCİ NEDİR?**

Günümüzde kullanılan bilgisayarların özelliklerinden bahsedilirken duyduğunuz 80386, 80486, Pentium-ll, Pentium-lll birer mikroişlemcidir (Microprocessor). Mikroişlemciler bilgisayar programlarının yapmak istediği tüm işlemleri yerine getirdiği için, çoğu zaman merkezi işlem ünitesi** (CPU-** Central Processing Unit) olarak da adlandırılır. PC adını verdiğimiz kişisel bilgisayarlarda kullanıldığı gibi, bilgisayarla kontrol edilen sanayi tezgahlarında ve ev aygıtlarında da kullanılabilmektedir. Bir mikroişlemci işlevini yerine getirebilmesi için aşağıdaki yardımcı elemanlara ihtiyaç duyar. Bunlar:

**1**. Input (Giriş) ünitesi.

**2**. Output (Çıkış) ünitesi.

**3**. Memory (Bellek) ünitesi.

Bu üniteler CPU chip'inin dışında, bilgisayarın ana kartı üzerinde bir yerde farklı chip'lerden veya elektronik elemanlardan oluşur. Aralarındaki iletişimi ise veri yolu (Data bus), adres yolu (Address bus) denilen iletim hatları yapar.

Intel, Cyrix, AMD, Motorola mikroişlemci üreticilerden birkaçıdır, Günümüzde mikroişlemciler genellikle PC adını verdiğimiz kişisel bilgisayarlarda kullanılmaktadır.

**MİKRODENETLEYİCİ NEDİR?**

Bir bilgisayar içerisinde bulunması gereken temel bileşenlerden RAM, I/O ünitesinin tek bir chip içerisinde üretilmiş biçimine mikrodenetleyici **(Microcontroller)** denir. Bilgisayar teknolojisi gerektiren uygulamalarda kullanılmak üzere tasarlanmış olan mikrodenetleyiciler, mikroişlemcilere göre çok daha basit ve ucuzdur. Günümüz mikrodenetleyicileri otomobillerde, kameralarda, cep telefonlarında, fax-modem cihazlarında, fotokopi, radyo, TV, bazı oyuncaklar gibi sayılamayacak kadar pek çok alanda kullanılmaktadır.

Günümüz mikrodenetleyicileri birçok chip üreticisi tarafından üretilmektedir. Her firma ürettiği chip'e farklı isimler vermektedir. Örneğin Microchip firması ürettiklerine PIC adını verirken, Intel'in ürettiği ve 1980'lerin başında piyasaya sürdüğü 8051, bazen MCS-51 olarak da adlandırılır.

**Neden Mikroişlemci Değil de Mikrodenetleyici Kullanılıyor?**

Mikro işlemci ile kontrol edilecek bir sistemi kurmak için en azından şu üniteler bulunmalıdır; CPU, RAM, I/O ve bu ünitelerin arasındaki veri alış verişini kurmak için DATA BUS (data yolu) gerekmektedir. Elbette bu üniteleri yerleştirmek için baskılı devreyi de unutmamak gerekmektedir. Mikrodenetleyici ile kontrol edilecek sistemde ise yukarıda saydığımız ünitelerin yerine geçecek tek bir chip (Mikrodenetleyici) ve bir de devre kartı kullanmak yetecektir. Tek chip kullanarak elektronik çözümler üretmenin maliyetinin daha düşük olacağı kesindir. Ayrıca da kullanım ve programlama kolaylığı da ikinci bir avantajıdır. İşte yukarda saydığımız nedenlerden dolayı son zamanlarda bilgisayar kontrolü gerektiren elektronik uygulamalarda mikrodenetleyici kullanmaya eğilimin artmasının haklılığını ortaya koyuyor.

**MİKRODENETLEYİCİLER HAKKINDA GENEL BİLGİLER**

Neredeyse her mikroişlemci (CPU) üreticisinin ürettiği birkaç mikrodenetleyicisi bulunmaktadır. Bu denetleyicilerin mimarileri arasında çok küçük farklar olmasına rağmen aşağı yukarı aynı işlemleri yapabilmektedirler. Her firma ürettiği chip'e bir isim ve özelliklerini birbirinden ayırmak için de parça numarası vermektedir. Örneğin Microchip ürettiklerine PIC adını, parça numarası olarak da 12C508, 16C84, 16F84, 16C711 gibi kodlamalar verir. Intel ise ürettiği mikrodenetleyicilere MCS-51 ailesi adını vermektedir. Genel olarak bu adla anılan mikrodenetleyici ailesinde farklı özellikleri bulunan ürünleri birbirinden ayırt etmek için parça numarası olarak da 8031AH, 8051AH, 8751AHP, 8052AH, 80C51FA gibi kodlamalar kullanılmaktadır.

Bir uygulamaya başlamadan önce hangi firmanın ürünü kullanılacağına, daha sonra da hangi numaralı denetleyicinin kullanılacağına karar vermek gerekir. Bunun için mikrodenetleyici gerektiren uygulamada hangi özelliklerin olması gerektiği önceden bilinmesi gereklidir. Aşağıda bu özellikler sıralanmıştır:

Programlanabilir dijital paralel giriş/çıkış.

Programlanabilir analog giriş/çıkış.

Seri giriş/çıkış ( senkron, asenkron ve cihaz denetimi gibi).

Motor veya servo kontrol için pals sinyali çıkışı.

Harici giriş vasıtasıyla kesme.

Timer vasıtasıyla ile kesme.

Harici bellek arabirimi.

Harici bus arabirimi (PC ISA gibi).

Dahili bellek tipi seçenekleri(ROM, EPROM, PROM ve EEPROM).

Dahili RAM seçeneği.

Kayan nokta hesaplaması.

Daha da ayrıntıya girecek olursak bu listede sıralanacak özellikler uzayıp gidecektir. Şimdi de bizim bu kitapta ele aldığımız Microchip'in ürünü olan PIC'i neden seçtiğimize değinelim. Microchip, 8-bit'lik mikrodenetleyici ve EEPROM üreten bir Amerikan şirketidir. Arizona eyaletinde iki, Tayland ve Tayvan'da da birer tane olmak üzere toplam dört fabrika ile kendi alanında dünyada söz sahibi olan bir chip üreticisidir.

**Neden PIC?**

Bilgisayar denetimi gerektiren bir uygulamayı geliştirirken seçilecek mikrodenetleyicinin ilk olarak tüm isteklerinizi yerine getirip getirmeyeceğine, daha sonra da maliyetinin düşüklüğüne bakmalısınız. Ayrıca, yapacağınız uygulamanın devresini kurmadan önce seçtiğiniz mikrodenetleyicinin desteklediği bir yazılım üzerinde simülasyonunu yapıp yapamayacağınızı da dikkate almalısınız.

Yukarda saydığımız özellikleri göz önüne aldığımızda Microchip'in ürettiği PIC'leri kullanmak en akılcı bir yol olduğunu görülmektedir. İşte, bu kitapta PIC'leri ele alınmamızın nedenlerini şöyle sıralayabiliriz.

Yazılımın Microchip'ten veya internetten parasız olarak elde edilebilmesi.

Çok geniş bir kullanıcı kitlesinin bulunması.

PIC'lerin çok kolaylıkla ve ucuz olarak elde edilebilmesi.

Elektronikle hobi olarak uğraşanların bile kullanabildikleri basit elemanları kullanarak yapılan donanımla programlanabilmesi.

Çok basit reset, clock sinyali ve güç devreleri gerektirmeleri.

PIC, adını İngilizce'deki Peripheral Interface Controller cümlesindeki kelimelerin baş harflerinden almış olan bir mikrodenetleyicidir. Eğer bu cümleyi Türkçe'ye çevirirsek,** çevresel üniteleri denetleyici arabirim** gibi bir anlam çıkacaktır. PIC gerçekten de çevresel üniteler adı verilen lamba, motor, role, ısı ve ışık sensörü gibi 1/0 elemanların denetimini çok hızlı olarak yapabilecek şekilde dizayn edilmiş bir chip'tir. RISC mimarisi adı verilen bir yöntem kullanılarak üretildiklerinden bir PIC'i programlamak için kullanılacak olan komutlar oldukça basit ve sayı olarak da azdır. 1980'lerin başından itibaren uygulanan bir tasarım yöntemi olan RISC (Reduced Instruction Set Computer) mimarisindeki temel düşünce, daha basit ve daha az komut kullanılmasıdır. Örneğin PIC16F84 microdenetleyicisi toplam 35 komut kullanılarak programlanabilmektedir.

**Neden PIC16F84?**

Bu kitapta programlanması ve örnek uygulamaları verilen PlC'in 16F84 serisi olmasının en önemli nedeni: PIC16F84 (veya PIC16F84A) mikrodenetleyicisinin program belleğinin flash teknolojisi ile üretilmiş olmasıdır.

Flash memory teknolojisi ile üretilen bir belleğe yüklenen program, chip'e uygulanan enerji kesilse bile silinmez. Yine bu tip bir belleğe İstenirse yeniden yazılabilir. Flash bellekler bu özellikleri ile EEPROM bellekler ile aynı görünmektedirler. Gerçekten de Flash ile EEPROM bellek aynı şeylerdir. Ancak bazı üreticiler tarafından EEPROM belleğe Flash ROM da denilmektedir.

Flash belleğe sahip olan PIC16F84'i programlayıp ve deneylerde kullandıktan sonra, silip yeniden program yazmak PIC ile yeni çalışmaya başlayanlar için büyük kolaylıktır. Böylece işe yeni başlayanlar yaptıkları programlama hataları nedeniyle chip'i atmak zorunda kalmayacaklardır. Gerçi EPROM program memory'si olan chip'lere de yeniden yazmak mümkündür ama, bu durumda bir EPROM silici cihazına ihtiyaç vardır. Bir silici cihaz bulunsa bile programı bellekten silmek için en azından 10-15 dk beklemek zorunda kalınacaktır. İşte PIC16F84'ün bu özelliği mikrodenetleyici kullanmaya yeni başlayanlar için ideal bir seçenektir.

PIC16F84'ü seçmemizin ikinci nedeni de, programlama donanımının çok ucuz ve kullanışlı olması ve hatta çoğu meraklı elektronik kullanıcı tarafından bile üretilebilmesidir. Kitabın Ekler bölümünde adresini verdiğimiz firmanın ürettiği programlayıcı donanımı ve yazılımı ödemeli olarak istenebilmesi Türkiye'deki kullanıcılar için çok büyük bir avantajdır.

PIC16F84'ü programlamak için öğrendiğiniz her şeyi diğer PIC 16/17 mikrodenetleyicilerinin uygulamalarında da 'kullanabilmeniz, yapılan seçimin doğruluğunu göstermektedir.

**PIC PROGRAMLAMAK İÇİN NELERE İHTİYACINIZ VAR?**

PIC 16/17 mikrodenetleyicilerin programlamasını ve uygulamalarda nasıl kullanılacağını öğrenmek için neleri bilmek ve nelere sahip olunması gerekenler aşağıda sıralanmıştır:

IBM uyumlu bir bilgisayara sahip olmak ve temel kullanımları bilmek.

Bir metin editörünü kullanmasını bilmek.

Bir assembler programına sahip olmak.

PIC programlayıcı donanımına sahip olmak.

PIC programlayıcı yazılımı.

PIC

Programlanmış PIC'i denemek için breadboard, güç kaynağı ve elektronik elemanlar.

Programlanmış bir PIC'i deneme kartı.

**IBM Uyumlu Bilgisayar**

Assembly program kodlarını kolayca yazabilmek, doğru ve hızlı bir şekilde PIC'in program belleğine gönderebilmek için bilgisayara ihtiyaç vardır. Bir metin editörü kullanarak yazılan program kodları, derlendikten sonra PIC'e gönderilmesi gerekir. Program kodlarının PIC'e yazdırma işlemi paralel veya seri porta bağlanan bir elektronik devre aracılığı ile yapılır. Bu işleri yapabilmek için bilgisayarın temel kullanım fonksiyonlarını bilmeniz gerekir. Aşağıda bilmeniz gereken bazı temel işlemleri ve sahip olmanız gereken minimum konfigürasyonu veriyoruz:

DOS ya da VVINDOVVS işletim sistemi bildiğinizi, bu işletim sistemi. komutlarıyla klasör oluşturma, dosya kopyalama ve silme, listeleme gibi işlemleri yapabildiğinizi.

Basit bir editör (EDIT, Notpad gibi) kullanabildiğinizi, bu editörde bir text dosyası oluşturup disket ya da hard diske kaydedebildiğinizi, diskteki bir dosyayı yükleyip üzerinde düzeltmeler yapabileceğinizi,

Minimum 80486 CPU, 4 MB RAM, 100 MB harddisk ve CD-ROM sürücüsü (Microchip'in CD'lerini kullanabilmek için) bulunan bir PC'ye sahip olduğunuzu kabul ediyoruz.

**Metin Editörü**

Assembly dili komutlarını yazıp bir metin dosyası oluşturmak için EDIT veya NotPad gibi bir editörü kullanabilmeniz gerekir. İsterseniz ASM uzantılı metin dosyalarınızı yazabileceğiniz** PFE** editörünü de kullanabilirsiniz. Bu editörün hem DOS hem de VVINDOVVS altında çalışan versiyonları bulunmaktadır ve PIC konusunda destek veren bir internet sitesinden alınmıştır. Ekler bölümünde adını verdiğimiz firma da bu programı disket içerisinde sunmaktadır.

**Assembler Programı**

PIC Assembly dili adı verilen ve toplam 35 komuttan oluşan programlama dilini bu kitapta öğreneceksiniz. Bu komutları basit bir editörde yazabiliyoruz. Ancak, İngilizce'deki bazı kelimelerin kısaltmasından oluşan bu dilin komutlarını PIC'in anlayabileceği makine diline çeviren bir programa ihtiyacımız vardır. Bu programa assembler adını veriyoruz. Text dosyası biçiminde kaydedilmiş olan assembly dili komutlarını makine diline çeviren MPASM'nin hem DOS altında hem de WINDOWS altında çalışan versiyonu bulunmaktadır. Bu program Microchip firmasının internetteki www.microchip.com adlı sitesinden parasız olarak download edilebileceği gibi kitabın Ekler bölümünde adresi verilen firmadan da elde edebilirsiniz. MPASM'nin kullanımı hakkında detaylı bilgiyi 5. bölümde bulacaksınız.

Microchip bir de içerisinde hem metin editörü hem MPASM assembler programını bulunduran** MPLAB** programını PIC programlayıcılarının kullanımına sunmaktadır. Bu programın bulunduğu CD-ROM yine www.microchip.com adresinden parasız olarak istenebilir. MPLAB'ın kurulumu ve kullanılmasıyla ilgili gerekli detay bilgiyi Ekler bölümünde bulacaksınız.

Yukarıda (sağda) PIC16F84 ve PIC16C84 mikrodenetleyicileri programlayabileceğiniz, çok basit bir donanımı bulunan programlama kartı resmi verilmiştir. Bu kartla ilgili detaylı bilgiyi Ekler bölümünde bulacaksınız.

**PIC Programlayıcı Yazılımı**

MPASM tarafından derlenerek makine diline dönüştürülmüş assembly programı kodlarının PIC'e yazdırılmasında kullanılan bir programa gereksinim vardır. Programlayıcı yazılımları, PIC'i programlamak için kullanılan elektronik karta bağımlıdır. Yani her programlayıcı yazılımı ile elinizde bulunan karta kod gönderemeyebilirsiniz. Genellikle programlama kartı üreticileri, ürettikleri karta uygun yazılımı da birlikte sunarlar. Biz bu kitapta ProtoPIC programlama kartına gönderdiği kodlarla PIC'ieri sorunsuz olarak programlayan** P16PRO** adlı yazılımı kullandık ve nasıl kullanılacağını anlattık. P16PRO'yu Windows ortamından da çalıştırabileceğiniz için bu size büyük kolaylık sağlayacaktır.

**Programlanmış PIC'i Deneme Kartı**

Programladığınız PIC'İ breadboard üzerinde kendi kurduğunuz devre de deneyebileceğiniz gibi şekilde görülen özel bir deneme kartı üzerinde de deneyebilirsiniz. Başlangıç ve orta düzey PIC programlayıcılara hitap etmek üzere geliştirilen bu kart üzerinde deneme yapmak, breadbord üzerinde devre kurmaktan çok daha kolaydır. PIC'in port çıkışlarındaki sinyalleri izlemek amacıyla 8 tane LED, bir tane de 7 segmentli LED yerleştirilmiştir. Kart üzerindeki, butonlar, potansiyometre ve LED'ler aracılığıyla farklı şekilde programlanan PIC'lerin kolayca denenmesini sağlanır. Bu kartın yapısı ve kullanılması hakkında Ekler bölümünde geniş bilgi bulacaksınız.

## PAGE

## PAGE 1

## **10******

---
*Kaynak: `MİKROİŞLEMCİLER NEDİR/MİKROİŞLEMCİLER NEDİR.doc` — Knowledge — 2004*
