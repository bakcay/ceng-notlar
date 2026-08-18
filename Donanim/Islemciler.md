# İşlemciler

## **İçindekiler **

**İşlemciler.............................................................................. 2**

**İşlemci nedir ................................................... 2**

**Tarihçe .............................................................2**

**İşlemcilerin Yazılım Destekleri ........................................... 3**

**MMX ............................................................. 3**

**3Dnow ........................................................... 3**

**SSE ..................................................................3**

**Mimari ................................................................................. 4**

**CISC işlemsiler ..............................................4**

**RISC işlemciler...............................................4**

**CISC ve RISC işlemcilerin karşılaştırılması...5**

**CACHE ....................................................................................5**

**İşlemcinin Hızı ........................................................................5**

**Nasıl Çalışır .............................................................................6**

**Microişlemci Temel Yapısı.....................................................6**

**İletim yolları....................................................7**

**Veri yolları ......................................................7**

**İç veri Yolları ...................7**

**Dış veri yolları .................. 8**

**Adres yolları .....................................................8**

**Kontrol Yolları ...................................................8**

**Aritmetik Mantık Birimi (ALU) ..........................8**

**ALU’ nun İşlevi ..................................................9**

**Kaydediciler ve Sayıcılar .....................................................9**

**Kontrol Birimi .........................................................................11**

**Merkezi İşlem Biriminin Yapısı ............................................ 11**

**8 bit microişlemciler .................................... 12**

**16 bit microişlemciler .................................. 13**

**32 bit microişlemciler .................................. 13**

**Microişlemci Özellikleri ......................................................14**

**Microişlemci Destek Devreleri ........................................... 16**

**Pentium 4 ile 3 arasındaki farklar ...................................... 18**

**Özet ...................................................................................... 19**

## İŞLEMCİLER - (CPU)

## **İşlemci nedir : **

** Bir bilgisayarın en popüler ve en önemli parçası işlemcidir. Kısaca CPU (Central Processing Unit / Merkezi İşlem Birimi) olarak anılan işlemciler, adından da anlaşılacağı üzere bir bilgisayardaki işlemleri yürüten ve sonuçları gerekli yerlere gönderen elemandır.**

**1971 yılında Intel firmasının ilk defa binlerce transistörü bir silikon çip üzerinde birleştirmesiyle bilgisayar çağında devrim gerçekleştirilmiş oldu. Bu şekilde daha önce sadece büyük şirketlerin ve üniversitelerin kullanabildiği bilgisayarlar iyice küçüldü ve evlere girmeye başladı.**

**Eskiden işlemci PC'nin en önemli parçasıyken bir PC'nin değerini belirleyen şeyin performans ve sunduğu imkanlar olduğunu düşünürsek artık en önemli parçalarından biri diyebiliyoruz. Çünkü bir PC'nin performansını grafik kartı, sabit disk, bellek gibi bileşenler de belirlediği gibi, özellikleri de kullanılan anakarta, multimedya donanımlarına ve çevre birimlerine bağlı. Bu yüzden hızlı bir işlemci ile yavaş bir sabit disk veya grafik kartı kullanmak veya yavaş bir işlemciyle hızlı bir grafik kartı veya sabit disk kullanmak pek anlamlı olmuyor. Donanımların birbirine ayak uydurduğu, başka bir donanımın işini görmesi için nispeten daha az süre beklediği sistemler dengeli sistemlerdir.**

## **Tarihçe :**

** İşlemci yada diğer ismiyle CPU (central processing unit - merkezi işlem birimi) aslında bir yonga (chip) üzerine yerleştirilmiş bir hesap makinesinden başka bir şey değildir. İlk işlemci Intel 4004 1971 üretildiğinde çok güçlü değildi. Yapabildiği tek şey toplama ve çıkarmaydı ve bir kerede sadece 4 bit işlem yapabiliyordu. Fakat her şeyin bir chip üzerine sığdırılmış olması o zamanlar için gerçekten bir başarıydı. 4004'ün üretiminden önce mühendisler bilgisayarları çok sayıda chip ve parçaların birleşiminden yapabiliyorlardı. 4004 ilk taşınabilir elektronik hesap makinesine hayat verdi.**

**Ev bilgisayarları için kullanılan ilk işlemci Intel 8080'di. **

** 1974 yılında üretilen bu işlemci 8bit'lik bir chipti. Fakat piyasalar asıl etki yapan işlemci yine Intel'in 8088 adlı işlemcisiydi ve bu işlemci 1979 yılında üretildi. IBM PC makinelere hayat veren bu işlemci tam olarak adını 1982 yılında duyurmaya başladı. Eğer bilgisayarlarla biraz ilgiliyseniz PC pazarının 8088'den 80286 oradan 80386, 80486, Pentium, Pentium II, Pentium III ve son olarak Pentium 4'e geçtiğini bilirsiniz. Bütün bu işlemciler Intel tarafından üretildi ve hepside temelde 8088 tasarımının geliştirilmesiyle ortaya çıktı. Günümüzde kullandığımız Pentium 4, 8088'lerdeki her hangi bir kodu çalıştırabilir fakat 5000 kez daha hızlıdır.**

**Aşağıdaki tablo Intel işlemciler arasında nasıl farklar olduğunu görmenize yardımcı olacak:**

**İsimTarihTransistörMikronSaat HızıVeri GenişliğiMIPS********808019746,00062 MHz8 bit0,64********8088197929,00035 MHz16 bit-8 bit0,33********802861982134,0001,56 MHz16 bit1********803861985275,0001,516 MHz32 bit5********8048619891,200,000125 MHz32 bit20********Pentium19933,100,0000,860 MHz32 bit-64 bit100********Pentium II19977,500,0000,35233 MHz32 bit-64 bit~300********Pentium III19999,500,0000,25450 MHz32 bit-64 bit~510********Pentium IV200042,000,0000,181,5 MHz32 bit-64 bit~1,700**************

**Tablo hakkında bilgi :**

**Tarih, işlemcinin ilk üretildiği tarihtir. Çoğu işlemcinin daha sonra daha hızlı versiyonları da çıkmıştır. **

**Mikron, yonga üzerindeki en küçük kablonun genişliğidir. Karşılaştırmak için insan saçının 100 mikron kalınlığında olduğunu söyleyebiliriz. Yonga üzerindeki kablo kalınlığı azaldıkça transistör sayısının arttığını görebiliriz. **

**Saat Hızı, yonganın ayarlanabildiği en yüksek saat hızıdır. Bir sonraki bölümde ayrıntılı olarak incelenecektir. **

**Veri Genişliği, işlemcinin ALU (arithmetic/logic unit - aritmetik/mantık birimi) biriminin genişliğidir. 8 bitlik bir ALU 2 adet 8 bitlik sayı üzerinde topla, çıkarma, çarpma, bölme yapabilirken, 32 bitlik bir ALU 32 bitlik 2 sayı üzerinde aynı işlemleri yapabilir. 8 bitlik bir ALU 32bitlik 2 sayı üzerinde 4 seferde işlem yaparken, 32 bitlik bir ALU aynı işlemi 1 kerede yapabilir. Genellikle dış veri yolu genişliği ALU veri genişliğiyle aynı olur. Fakat 8088 işlemciler 16 bit ALU' ya sahipken 8 bit veri yolları vardı. Modern Pentiumlar ise 32bit ALU' ya 64 bit veri yoluyla hizmet sunarlar. **

**MIPS, "millions of instructions per second" yani saniyede yapılan işlem miktarıdır ve işlemcinin performansı hakkında genel bir bilgi verebilir. Günümüzde işlemcilerde kullanılan farklı teknikler bu MIPS değerinin önemi azaltsa da, genel anlamda işlemci performansıyla ilgili bilgi verebilir. **

**Yonga, genellikle küçük, ince bir silikon parçası üzerine asitle oyularak yerleştirilen transistörlerin oluşturduğu bütünleşik devredir. Bir yonga 2-3 cm büyüklüğe milyonlarca transistör sığdırılarak üretilir.**

**Yukarıda ki tablodan saat hızıyla MIPS arasında bir bağlantı olduğunu görebilirsiniz. En yüksek saat hızı yonganın üretim teknolojisine bağlıdır. Ayrıca transistör sayısı ve MIPS arasında da bir bağlantı vardır. Örnek olarak 8088 işlemci 5 Mhz hızında çalıştığı halde 0.33 MIPS (yaklaşık olarak 15 saat turunda 1 işlem) yapabilmektedir. Günümüzde ise modern işlemciler yaklaşık olarak her saat turunda 2 işlem yapabilmektedir**

**İşlemcilerin Yazılım Destekleri :****
****
MMX: Intel'in geliştirdiği MMX'in açılımı Multimedya Uzantılarıdır (Multimedia Extensions) ve işlemcilere eklenen 57 multimedya komutuna verilen addır. AMD’ de bu komut setinin lisansını Intel'den almıştır. MMX işlemciler bazı genel multimedya operasyonlarını üstlenirler (örneğin, normalde ses kartı veya modemler tarafından yapılan dijital sinyal işleme). Ancak bu komut setinin kullanılabilmesi için MMX uyumlu yazılımların kullanılması gereklidir. MMX işlemcilere ekleneli uzun bir süre olmasına karşın, MMX destekli yazılımların beklendiği kadar çabuk artmadığı gözlenmiştir.
3DNow: 3 Boyutlu grafikler ile ilgili hesapların hızlandırılması için AMD işlemcilerde kullanılan komut setinin adıdır. Özellikle 3DNow! destekli oyunların sayısı hızla artmıştır. Ekran kartlarının da 3DNow! destekli sürücüleri olabilir.
SSE: Intel tarafından geliştirilip Pentium III işlemcilere uygulanan 70 adetlik yeni komut setidir. Yakında Celeron ve Pentium II işlemcilere de uygulanması beklenmektedir. SSE'nin açılımı "Strea-ming SIMD Extensions'dır (SIMD = Single Instruction Multiple Data). Mutlaka Türkçeleştirmek gerekirse "akıcı, tek komutla çoklu veri işleme uzantıları" diyebiliriz. Yani işlemciye bir komut verirsiniz bir çok veriyi bir amaca yönelik olarak işler. Grafik, resim, video, animasyon, 3 boyut işlemleri, ses tanıma öğelerine sahip, SSE destekli uygulamalarda ciddi bir performans artışı sağlar. Henüz çok yeni olduğundan piyasada SSE destekli yazılım çok sayıda değildir ama hızla yaygınlaşması beklenmektedir.**

## **Mimari :**

**Mikroişlemciler mimari (architecture) olarak gruplara ayrılırlar. Ortak mimariye sahip olan işlemciler aynı komutları tanımakta ve aynı yazılımları çalıştırabilmektedirler.**

** En meşhur mikroişlemci mimari si Intel’in x86 işlemcisidir. Intel ilk x86 tabanlı işlemcisini 8086 olarak 1978 yılında piyasaya sürdü. Daha sonraki yıllarda yeni nesil x86 tabanlı işlemciler çıkarıldı. 286,386,486, Pentium ve Pentium Pro olarak bu kuşakları görebilmekteyiz. Pentium II, Celeron, Pentium III, Xeon ve Katmai, altıncı kuşak Pentium Pro’nun varyasyonlarıdır.**

** Intel’in haricindeki diğer mimariler ise şunlardır: Modern Machintosh’larda bulunan PowerPC, eski Mac’lerdeki 68oxo serisi, Digital ve Compaq’ın güçlü serverlerinde kullanılan Alpha ailesi, Silicon Grahics’in Mips Rxooo serisi, Hawlett-Packard’ın PARISC’i ve Sun Microsystems’e ait SPARC’tır.**

** Mimariler, ortaya çıktıkları dönemin felsefesine göre dizayn edilirler. 1970’lerde veri saklama cihazları ve hafıza bu güne göre çok kısıtlıydı. Bu kaynakları tasarruflu bir şekilde kullanabilmek için Intel x86 tabanlı işlemcilerde CISC (Complex Instruction Set Computing - Karmaşık komut seti ile hesaplama) diye bilinen bir mimari kullandı. CISC’ın karakteristik iki özelliği, değişken uzunluktaki komutlar ve karmaşık komutlardır. Değişken uzunluktaki komutlar hafıza tasarrufu sağlar. Çünkü basit komutlar karmaşık komutlardan daha kısadır. Karmaşık komutlar da iki ya da daha fazla komutu tek bir komut haline getirdikleri için hem hafızadan hem de programda yer alması gereken komut sayısından tasarruf sağlar.**

** İlerleyen yıllarda CISC’in kısıtlamaları ve hafızayı tasarruflu kullanmanın önemini yitirmesi neticesinde CISC’a rakip olarak RISC (Reduced Instruction Set Computing - daraltılmış komut seti ile hesaplama) ortaya çıktı.**

** RISC’ın komutlarının uzunluğu sabittir (genelde de 32 bit’tir) ve her bir komut basit bir işlemi yerine getirir. Bir RISC çipi bu iki karakteristik özelliği sayesinde, fetch (komutu hafızadan taşıma), decode (komutun anlamını çözme) ve komutu çalıştırma işlemlerini daha kolay bir şekilde yapabilir. **

** RISC’ın bir dezavantajı kodun uzamasıdır. Tüm komutlar gerek olsun olmasın 32 bitliktir. Dolayısıyla RISC programları CISC programlarından daha fazla hafıza gerektirebilirler. Buna rağmen decode aşamasının CISC’e göre daha hızlı gerçekleşmesine ek olarak, çoğu RISC komutları sabit bir zaman diliminde işlem görür. Bu da superscalar pipelining teknolojisi kullanan modern işlemciler için önemli bir özelliktir.**

**CISC İŞLEMCİLER : ****PC’ lerde günümüze kadar RAM’ların sınırlı ve pahalı olduğu 1960 ve 1970’li yıllarda geliştirilen CISC işlemci mimarisi kullanılmaktadır. Daha çok programların az bellek kullanımı gerektirdiği sistemlerde yer almakta ve az bellek kullanımı için kompleks komutların ve mimarinin oluşumunu ortaya çıkardı. **

** Mimarideki kompleksliğin artması işlemci performansında negatif oluşumların ortaya çıkmasına sebep oldu. Bununla birlikte programların yüklenmesinde ve çalıştırılmasında düşük bellek kullanımının hızlı olması mesele teşkil etmekteydi. 1980 ve 1990’lı yıllarda bellek ihtiyacının artması işlemci tasarımcılarının kararlarını gözden geçirmesine sebep oldu. Eskiden kullanılan bellekler 16-32 Kbayt iken yeni mimarilerde 8-16 Mbayt çıktı ve günümüz kişisel bilgisayarlarında bir standart halini aldı. ,**

**RISC İŞLEMCİLER : ****RISC işlemcili sistemlerde amaç, komut işlemcisinin mümkün olduğu kadar hızlı olmasıdır. Bunu başarmak için ana yol, işlemcinin çalıştırdığı komutların basitleştirilmesidir. Komutların basitleştirilmesi ve azaltılması işlemcinin uzun ve kompleks olandan daha hızlı çalışabilmesi demektir. RISC mimarisi, aynı anda birden fazla komutun işlendiği tekniği içeren hattı (pipelining) ve süperskalar çalışmasının kullanımıyla yüksek bir performans sağladı. **

** Doğal olarak bu tasarım tekniği yüksek bellek ve çok ileri derleme teknolojisini gerektirdi. 1980’lerin ortasında bellek fiyatlarının ucuz olması yüksek performanslı işistasyonlarında RISC tabanlı işlemcilerin çok sık kullanılmasına sebep oldu. 1990’larda VLSI teknolojisinin gelişimiyle birlikte belleklerin eskiye nazaran daha ucuz oluşu ve makine diline bağımlılığı ortadan kaldıran ileri derleyicilerin çok yaygın olduğu sistemlerde ve hatta PC’ lerde yüksek performanslı RISC işlemciler kullanılmaya başlandı. **

** CRAY, IBM, DEC, HP, APPLE, ve SUN gibi süper bilgisayar, Çok büyük bilgisayar, büyük bilgisayar, işistasyonları ve PC’lerde kullanılmaktadır.**

## **CISC ve RISC TABANLI İŞLEMCİLERDE KARŞILAŞTIRILMASI :**

** CISC ve RISC tabanlı işlemcilerin karşılaştırılmasında iki önemli faktör farklılıklarını ortaya çıkarmada yeteridir. **

**HIZ:**** Genelde RISC çipleri, iş-hattı (pipelining) tekniği kullanarak eşit uzunlukta segmentlere bölünmüş komutları çalıştırmaktadır. İş-hattı tekniği komutların kademeli işlenmesini sağlar. Bu yüzden RISC’in bilgi işleme hızı CISC’den daha hızlı olur.RISC işlem cinsinde tüm komutlar 1 birim uzunlukta olup, iş-hattı tekniği ile işlenmektedir. Bu teknikte bazı komutlar hariç,her bir basamağında aynı işlemin uygulandığı birimlerden geçerler. İş hattı teknolojisini açıklamak için herhangi bir komutun işlenmesindeki adımlar ele alınırsa :**

** Komut kodu ve işlenecek veriler dahil bütün bilgilerin CPU’daki kaydedicilerin olduğu düşünülürse, birinci adımda yapılacak işin kaydedicide bulunan komut kodu çözülür, ikinci adımda üzerinde çalışacak veri (işlenen) kaydediciden alınıp getirilir, üçüncü adımda veri, komuta göre Aritmetik ve Mantık Biriminde işleme tabii tutulur ve dördüncü adımda sonuç kaydediciye yazılacaktır. Böylece bir komutun işlenmesi her bir basamak bir saat çevrimi gerektirirse, dört çevrimli (adımda) gerçekleşmiş olmakta ve bir adım bitmeden diğeri başlayamamaktadır.**

** İş-hattı tekniği ile çalışan işlemcilerde birinci adımda komut kodu çözülür, ikinci adımda birinci komutun üzerinde çalışacağı veri (işlenen) kaydediciden alınırken, sıradaki ikinci işlenecek olan komutun kodu çözülür. Üçüncü adımda ilk komutun görevi ALU’da yerine getirilirken, ikinci komutun işleyeceği işlenen alınıp getirilir. Bu anda sırada üçüncü komutun kodu çözülür ve işlem böylece devam eder.**

** İş-hattı tekniğinde çevrim zamanın düşmesi için komut kodlarının hızlı çözülmesi gereklidir. RISC mimarisinde tüm komutlar 1 birim uzunlukta oldukları için komut kodunu çözme işlemi kolaylaşır. Sistemde kullanılan kaydedicilerin simetrik bir yapıda olması, derleme işlemini kolaylaştırmaktadır. RISC işlemcilerde belleğe yalnız yükle ve depola komutlarıyla ulaşılır.**

** Bazı eski CISC mimarisinde de olmasına rağmen RISC mimarisinin sabit uzunluktaki basit komutlarla çalışması iş-hattı sistemini daha iyi kullanmasına sebep olmaktadır. Bu yüzden hesaplama oranlarının birinci öncelik arz ettiği yerlerde iş-istasyonları ve dağıtıcılarda çok tercih edilmektedir.**

## **Cache :**

** Cache , çalışmakta olan bir programa ait komutların geçici olarak saklandığı bir hafızadır. Cache hafızalar, işlemcinin komutları daha hızlı yüklemesini sağlayan yüksek hızlı hafızalardır. Cache hafızlar, Level 1 (L1) ve Level 2 (L2) olmak üzere ikiye ayrılırlar. İşlemci ihtiyaç duyduğu komutu ilk önce L1 cache hafızada arar. Eğer işlemcinin aradığı komut burada yoksa L2 cache hafızaya bakılır. Eğer burada da yoksa (cache miss durumu) sırayla, RAM ve HDD üzerindeki sanal hafıza üzerinde arar. L1 cache hafıza bunlar içerisinde en hızlı olanıdır ve genellikle işlemcinin üzerine imal edilir. L2 cache hafıza ise L1 e göre daha yavaş olmasına rağmen gene de hızı çok yüksektir. **

** Bir kısım işlemcilerde (Celeronların ilk nesillerinde olduğu gibi) L2 cache hafıza bulmayabilir. Bu durumda L1 cache hafızaya sığmayan komutlar L2 olmadığı için direkt olarak daha yavaş olan RAM a yazılmakta ve işlemcinin performansı düşmektedir. L2 cache hafıza genelde işlemcinin yakınındaki yüksek hızlı hafıza çiplerinden oluşur. Bazı yeni işlemcilerde (Celeron 300A ve sonrası gibi) L2 cache hafıza işlemcinin içine monte edilmiş ve daha hızlı erişim sağlanmıştır.**

**İşlemcinin Hızı :****
Bir işlemcinin hızını, kullanılan mikron teknolojisi, üretim teknikleri, kalıp boyutu ve proses kalitesi belirler. Ayrıca üretim sırasındaki koşullar, aynı banttan çıksa bile bir işlemcinin diğerinden hızlı olmasına yol açabilir. Ama sonuçta işlemci fabrikada son testlerden geçirilirken üzerine güvenli olarak çalışabileceği hız basılır. Işlemcinin hızı MHz cinsindendir. Bunu biraz temelden anlatmak gerekirse;
Her PC içinde, talimatların yerine getirilme hızını belirleyen ve çeşitli donanım aygıtları arasında senkronizasyonu sağlayan dahili bir saat vardır (bu saatin hızını normal saat ile karıştırmayın).
İşlemci, her bir talimatı belirli bir saat tıklamasında (saat döngüsünde) yerine getirir. Saat hızlıysa, işlemci saniyede daha fazla talimatı yerine getirir. 1 MHz, saniyede 1 milyon saat tıklamasına (döngüye) karşılık gelir. Yani, 400 MHz'lik bir işlemci, saniyede 400 milyon döngü yapar.
Bir işlemcinin MHz cinsinden hızı, anakartta kullanılan sistem veriyolu hızının belirli bir çarpanla çarpılması sonucu elde edilir. Örneğin 100 MHZ'lik anakartlarda 400 MHz'lik bir işlemci 4 çarpanını kullanarak 4x100=400 MHz'e erişir. Farklı işlemci serileri, aynı hıza sahip olsa da farklı mimarilere sahip olmaları nedeniyle aynı hızda olmazlar; yani saniyede yerine getirdikleri komut sayı farklıdır. Ayrıca "superscalar" mimariye sahip yeni işlemciler aynı anda birde fazla komutu yerine getirebilmektedir.

**

## **Nasıl Çalışır :**

** Mikroişlemciler, açma kapama anahtarı gibi çalışan milyonlarca transistörden oluşmaktadır. Bu anahtarların programlanma durumuna göre elektrik sinyalleri bunların üzerinden akar. Bu sinyaller, bilgisayarın yaptığı tüm işleri toplama, çıkarma, çarpma ve bölme gibi temel matematiksel işlemlere indirir. İşlemci de bu işlemleri en basit sayma sistemi olan ikilik düzen yani sadece 0 ve 1 sayılarını kullanarak yapar.**

**Bu sayı grupları üzerinde işlem yapmak için işlemci içerisinde bir takım komut listesinden ibaret bir program mevcuttur. Bu komutlar işlemciye iki sayının çıkarılması, toplanması yönünde emir verebildiği gibi klavyeden girilen tercihlere göre bir takım komut satırını atlayıp (şartlı dallanma - conditional branch) diğer komut satırlarını icra etmeye devam edebilir. Yani klavyeden bir soru karşısında gireceğimiz “E” (evet) veya “H” (hayır) ifadelerine göre program belirli komut satırlarını icra eder veya etmez. Temel olarak, mikroişlemcinin yaptığı iş, bitler üzerinde işlem yapmak üzere komutları çalıştırmaktır.**

**Bir mikroişlemcili otomasyon sistemi için, mikroişlemcinin yanı sıra yardımcı elemanlara ihtiyaç duyulur. Bunlar :**

**Input (Giriş) birimi**

**Output (Çıkış) birimi**

**Memory (bellek) birimi **

**CPU, Giriş/Çıkış ve Bellek birimlerinin oluşturduğu sisteme mikrobilgisayar adı da verilir. Giriş/Çıkış ve Bellek elemanları mikrobilgisayar kartı üzerinde bir yerde CPU chip’inden bağımsız olarak yerleştirilmiş chip’lerden v elektronik devre elemanlarından oluşur. Aralarındaki iletişimler ise yollar aracılığı ile sağlanır (Adres bus, Data bus , Control bus).**

** Intel, Cyrix, AMD, Motorola, Zilog mikroişlemci üreticilerinden bir kaçıdır. Mikroişlemci-ler işleyebildikleri kelime uzunlukları ile anılırlar. Örneğin; farklı firmalar tarafından üretilen 8080A / 8085A, Z80, MC6800, 8 bitlik işlemciler olarak anılır, aynı aile ye üye işlemcilerdir.**

**Bir mikroişlemcinin yapısı tahmin edilebileceği üzere çok karmaşıktır. Bununla birlikte kullanıcı açısından aşağıdaki birimlerden meydana geldiği söylenebilir.**

**Birkaç bitlik bilgiyi tutan belirli sayıdaki kaydediciler (geçici saklama elemanları). Bu yazaçlar 8 bitlik (1 byte), 16 bitlik (2 byte) makine kodu, veri veya adres bilgisi saklarlar.**

**Mantıksal kararlar veren veya aritmetik işlemleri yapan “Aritmetik Mantık Birimi” (ALU – Aritmetic Logic Unit)**

**Hem mikroişlemcinin iç işlemesini hem de tüm dış mikrobilgisayar sisteminin işlemesini kontrol eden zamanlama ve kontrol devreleri. Bu devreler ALU ve kaydedicilerin çalışmasını, bellek I/O portlarına dışarıdan yapılan bilgi transferleri ile bu devreler program komutları tarafından belirlenen işlerin yerine getirmesini sağlar.**

## MİKROİŞLEMCİ TEMEL YAPISI

** Mikroişlemci temel yapısı kapsamına, mikroişlemci entegresi içerisinde kalan kısım ile mikroişlemci ve bilgisayarın diğer birimleri arasındaki bağlantıları sağlayan pin çıkışları girmektedir.Hangi tür mikroişlemci olursa olsun ,temel yapısı şu bölümlerden oluşmaktır:**

** İletim Yolları(Buses).**

**Aritmetik Mantık Birimi(ALU).**

**Kaydediciler ve sayıcılar(Registers and counters)**

**Kontrol Birimi(CU).**

**Giriş-Çıkış tampon devreleri (Buffers).**

## **İLETİM YOLLARI:**

** İletim yolları, mikroişlemcilerden başlayarak, bilgisayar devre bağlantılarını sağlayan iletkenlerdir. Bunlardan bir kısmı tek iletkenlerden oluştuğu halde,çoğunluk kısmı,taraklı kablo veya baskı devre şeklinde ki yan yana dizilmiş izoleli çoklu iletkenlerden oluşmuştur. Bu çoklu iletkenlere, görüntüsünden dolayı yol(bus) adı verilmiştir. iletim yolları şu üç guruba ayrılır:**

**Veri Yolları (Data Bus).**

**Adres Yolları (Adress Bus).**

**Kontrol Yolları ( Control Bus).******

** Adress Bus**

** Micro**

** Processor Scrial**

** İnterface **

** Clock Eprom Ram I/O **

** Data Bus **

** Control Bus**

## **VERİ YOLLARI:**

** Veri yolları ,gerek bilgisayarın giriş birimlerinden gelen ön bilgi ve komutların, gerekse de bilgisayar içerisinde işlem görmekte olan ve işlem görmüş olan bilgilerin ve komutların iletildiği iletim yoludur. Bu nedenle , veri yollarından iki yönlü çalışma için yaralanılır. Veri yolları birbirine paralel, izole edilmiş, çoklu iletkenlerden oluşur. İletken sayısı, kullanılan mikroişlemcinin ve mikrobilgisayarın tasarımına bağlıdır. İletken ayısı 4, 8, 16, 64 olabilmektedir. **

** Mikroişlemcilerde, yukarıda da belirtildiği gibi genelde 7’li ASCII kodu kullanılmak dadır ve bunun için 8 iletkenli iletim yolu uygun bulunmaktadır. Eğer aynı anda çok karakter bitlerinin iletimi sağlanabilirse o oranda da bilgisayar çalışma hızı artmış olacaktır. Bu nedenledir ki 8’in katları şeklindeki 16, 32, 64 bitlik veri yolları ve çalışma sistemleri geliştirilmiştir. Her mikroişlemciyi dıştaki devrelere bağlayan veri yolları, mikroişlemci içerisinde de devam etmektedir. Ayrıca mikroişlemci içerisinde yoğun biçimde bulunan veri yolları ****iç ****ve ****dış ****veri yolları olmak üzere ikiye ayrılır. Bunlar**

## **a- İç Veri Yolları:**

** Mikroişlemci içerisinde bir ana veri yolu boydan boya uzanmakta ve devre birimlerine ait veri yolları da bu ana yola bağlanmaktadır. Bu veri yollarının çoğunluğu bağlantılarında giriş ve çıkış olarak işlem yapmaktadırlar. Ancak ALU’ da olduğu gibi bazı devrelerde de bir yönden gidip öbür yönden** **çıkmaktadırlar. Prensip olarak veri yolları iki yönlü iletim yapan yollarıdır. Yalnızca komut kaydediciye gelen veri yolu tek yönlü olup, bütün komutlar buraya gelerek, kod çözücüde yorumlandıktan sonra, kontrol devresine ulaşmakta ve kontrol devre buna göre belirli iletim yolarını kapayarak bilgisayarın çalışmasını yönlenmektedir. **

** Ana veri yolundan devrelerin yaralanması sıra ile olmaktadır. Ana veri yolunda gelen bilgilerin hangi devreden ana veri yoluna bilgi çıkışı yapabileceği anahtar ve üç durumlu kapı devreleri tarafından belirlenmektedir. Bunların çalışmaları kontrol devreleri tarafından yönetilmektedir.**

## **b -Dış Veri Yolları:**

** Dış veri yolları, mikroişlemci ile bellek ve giriş - çıkış kapıları arasındaki veri ve komut iletimini sağlayan iletim yollarıdır. Ayrıca çevre birimleri ile bilgisayar arasındaki bağlantıları sağlayan iletim yolları da dış veri yolunun bir bölümünü oluşturur.**

## **ADRES YOLLARI:**

** Adres yolları mikroişlemci ile bellek ve giriş - çıkış kapıları arasındaki iletişimin, hangi bellek gözü veya giriş – çıkış kapısı ile yapılacağının belirlenmesini sağlayan bağlantı yollarıdır. Adres yolu iletken sayısı, mikroişlemcinin, adresleyebileceği bellek gözü veya giriş – çıkış kapısı sayısını belirler. Bu bir adresleyebilme kapasitesi olayıdır. Adresleyebilme kapasitesi özellikle bellek kapasitesini belirler. Zira giriş - çıkış kapısı adresleme adedi ihtiyacı belleğe göre çok daha azdır. Adres yolu tek yönlü çalışır. Ancak son gelişmelerin ürünü olan mikroişlemcilerde iki yönlü de yararlanılmaya başlanmıştır. Adres yolu ileteceği adres numarasını program sayıcıdan almaktadır.**

## **KONTROL YOLLARI:**

** Kontrol yolları, mikroişlemcinin kontrol devresinden çıkarak, gerek mikroişlemci içerisindeki devrelere, gerekse de bilgisayar içerisindeki devrelere bir ağ gibi yapılır. Ayrıca da bilgisayar çevre birimlerinin işleme başlama diğer bir deyimle el sıkışma (hand shake) işlemi ve bitiminin sağlanması için kullanılırlar. Kontrol yolları insanın sinir sistemine benzetilebilir. Bütün bu sistemin çalışması, kontrol yollarından iletilen saat darbeleri ile yöneltilir dolayısıyla, bunlardan da iç ve dış olarak bir ayrıma gerek kalmamaktadır. Bir toplama, çıkarma veya kayma işleminin doğru yapılabilmesi için giriş sinyalleri sırasının doğru olması gerekir. **

** Bu doğruluğu kontrol devresi sağlamaktadır. Keza bellek işlem görecek değerlerin alınması ve sonuç bilgilerinin belleğe depolanması da kontrol sistemi aracılığı ile gerçekleşmektedir. Burada bir hususu belirtmek gerekiyor. Mikroişlemci iç devresindeki kontrol işlemi doğrudan gerçekleşmektedir. Yani kontrol yolu ile adres yolunun eş zamanlı çalışması gibi bir durum yoktur. Bu durum zaman kazancı sağlamakta mikroişlemci kaydedicilerinin geçici olarak ve ana işlemler için yüklenmelerine uygun gelmektedir.**

## **ARİTMETİK MANTIK BİRİMİ( ALU ):**

** Mikroişlemci için birinci dereceden önem taşıyan bir birimidir. Nasıl ki, mikroişlemci için bilgisayarın tanımlaması yapılmaktadır, ALU için de, mikroişlemcinin kalbidir denilebilir. Zira , mikroişlemcinin işlem gücünü Aritmetik Lojik İşlem birimi belirlemektedir. Diğer bir deyimle, ALU’nun değişik işlemleri yapabildiği orada mikroişlemci önem kazanmaktadır. **

** Teknikteki gelişmelere paralel olarak, bütün elektronik sistemler gibi ALU devreleri de sürekli gelişim içerisinde bulunmaktadır. Bu gelişmeler de, daha değişik işlem yapabilme, hacim küçültme ve hızın arttırılması şeklinde olmaktadır. Başlangıçta LSI tekniği ile üretilen elemanlar 1980’lerden başlayarak VLSI(Very Large Scale Integration) tekniği ile üretilmiş ve her yeni üretimde de bir taraftan işlem kapasitelerinin ve hızını arttırımı sağlanırken diğer taraftan da boyutlar biraz daha küçülmüştür. ALU devreleri de başlangıçta yalnızca toplama ve çıkarma yapabiliyorken, giderek çarpma, bölme ve büyük sayılarıda kayan nokta (floting point) işlemleri, bilimsel işlemler gibi çok yönlü işlem yürüten devreleri haline gelmiştir.**

** İşlev Veri Veri Elde Girişi **

** Girişi A Girişi B **

** Girişleri**

** Aritmetik – Lojik**

** Birimi **

** Durum Veri**

** Çıkışı Çıkışı**

## **ALU’NUN İŞLEVİ:**

** ALU yukarıda da belirtildiği gibi mikroişlemcinin işlem yapan birimidir. ALU‘nun yapabildiği işlemler şu iki ana grupta toplanır. **

** - Aritmetiksel işlemler**

** - Mantıksal(lojik) işlemler**

** ALU’nun çalışma prensibi büyük ve küçük bilgisayarlarda aynıdır. Ancak, büyük bilgisayarlarda bazı özel tekniklerle hız geliştirilmiştir ve daha değişik işlemleri yapma özelliği kazandırılmıştır. ALU, işlemleri, adder (toplayıcı) ve shifter (kaydırıcı) denilen iki esas devre ile gerçekleştirilir. Genelde, bu esas devreler ALU olarak anılmaktadır. Ancak, bilgileri depolayıcı ve değerlendirici bazı yardımcı devrelerden de yararlanılır. Bu yardımcı devreler:**

**\* Akümülatör : Başlangıç ve sonuç bilgilerini depolamak için akümülatör kullanılır. **

**Bazı mikroişlemcilerde akümülatör yerine veri kaydedici (dat reg) kullanılmıştır.**

** Geçici Kaydedici : Bellekten alınan işlem bilgilerinin ilk durak yeridir.**

** Bayrak Kaydedici: Bazı mikroişlemcilerde bayrak kaydedicileri yerine; ALU tarafından yapılan **

** İşlemlerin sonucunu gösteren ve bu sonuçları değerlendiren ortamını hazırlayan devredir. Bu sonuçlara göre bazı düzeltmeler gerekiyorsa, bilgisayar bunları kendi kendine yapabildiği gibi, bayrak ekrana çağrılarak bazı uyarıları dışarıdan yapılabilmesi mümkündür.**

** ALU tarafından şu aritmetiksel işlemler yapılır :**

** Toplama, çıkarma, çarpma, bölme, kıyaslama, artırma, eksiltme, tümleme, sağa kaydırma, sola kaydırma, sağa döndürme, sola döndürme. Ayrıca yapılan mantıksal işlemler yapılmaktadır: Mantıksal toplama, mantıksal çarpma, özel veya işlemi, değil işlemi.**

## **KAYDEDİCİLER VE SAYICILAR:**

** Kaydediciler ve sayıcılar gerek mikroişlemci içerisindeki gerekse de mikroişlemci ile diğer devreler arasındaki işlemleri destekleyen devrelerdir. Saklayıcılar CPU’nun ufak birer bilgi depolama birimleridir ve diğer bellek birimleri gibi ikili(binary) hücrelerden ( filp,floplardan) oluşturulmuşlardır.**

** Bazıları yazılım kontrolü altındadır ve CPU’nun her bir bilgi alış – verişi için bellek bölümüne başvurmamam olanağı sağlarlar. **

** Böylece işlem süresi çok kısa olur. Bazıları ise denetim için gerekli bilgileri saklarlar. Temel yapısı, D ve J –K Flip – Floplardan oluşur. Sayıcıların görevi ise işlemi yapılacak olan komut verilerin adresini belirlemektir. Temel yapısı, J-K Flip – Flop gruplarıdır.**

**Hemen hemen her bilgisayarda rastlanan kaydedici ve sayıcı türleri aşağıda sıralanmıştır.**

** - Program sayıcısı (Program counter-PC)**

** - Komut kaydedici (Instruction register-IR)**

** - Bellek adres saklayıcısı (Memory adress register-MAR)**

** - Akümülatörler (accumulators)**

** - İndis saklayıcıları (Index registers)**

** - Durum kaydedicisi (Status Registers-SR)**

** - Yığın göstericisi (Stack pointer-SP)**

** - Genel amaçlı yazmaçlar(general prupose registers)**

**Program sayıcısı :** **Bilindiği gibi bir programı oluşturan komutlar ve veriler normal halde bellekte saklıdır. Bilgisayarın çalışması sırasında hangi verinin hangi sıra ile kullanılacağının bilinmesi gerekir. Bu görevi program sayıcı yerine getirir. Program sayıcının bit genişliği adres yolu genişliği kadardır.**

** Bellekten alınan her bilgiden sonra alınacak yeni bilginin adresi program sayıcıya kaydedilir. Komut çevrimi, program sayıcının yeni adresi adres yoluna koyması ile başlar. Bunun ardından da ilgili kontrol sinyali gönderilir. Bellekten gelen her bilgiden sonra program sayıcısı kontrol devresinden aldığı işarete uyarak adres satırını 1 arttırır. Böylece bilgilerin bellekten CPU ya ardışık olarak gelmesi sağlanır.**

** Program sayıcı saymaya en küçük adresten büyüye doğru devam eder. Ancak, bu durumun şu istisnası olabilir. Eğer programda ATLA veya DALLAN gibi komutlar varsa belleğin bir bölümünden diğer bölümüne geçileceğinden sıra bozulur. Ancak yeni adreste tekrar sıralı olarak devam eder.**

** Böylece program sayıcı kaç bit'likse 2 nin bu bit kadar kuvvetine eşit adrese ulaşmak mümkün olacaktır.burada program sayıcı 16 bit'liktir. Dolayısıyla 216 = 65536 adrese ulaşabilecektir. **

** Her programdan sonra veya yeni bir programa başlamadan program sayıcı sıfırlanabilir. Zira her çalışma bitiminde program hangi adreste bitmişse sayıcı üzerinde o adres kayıtlıdır. Ve yeni bir çalışmada bu adresten saymaya başlar.**

**Komut kaydedicisi:**** Komut çözümleninceye kadar burada tutulur. Genellikle yazılımcı tarafında ulaşılmayan bir saklayıcıdır.**

**Bellek adres kaydedicisi: Ulaşılmakta olan verinin adresini içerir.**

**Bellek veri kaydedicisi: Adreslenmiş olan bellek konumunu yazılmakta veya o konumdan okunmakta olan veriyi içerir.**

**Genel Amaçlı Kaydediciler : ****Bu kaydediciler tek tek çalıştırılıp 8 bit'lik kaydediciler olarak kullanılabildikleri gibi ikişer ikişer çalıştırılıp 16 bit'lik kaydediciler halinde de kullanılabilmektedirler. Bu durum uygulanan programa bağlı olarak ayarlanır. Bilgisayarın çalışması sırasında, CPU ile bellek ve I/O arasındaki bilgi alışverişinin muhtelif safhalarında, bilginin geçici olarak depolanması için kullanılır.**

** Böylece her işlemde RAM ana belleğine kadar gitme gereksinimini azaltmış olurlar. Özellikle aritmetik işlemlerinde, akümülatörde bulunan birinci operanda ilave edilecek ikinci operandı, geçici kaydedici, genel amaçlı kaydedicilerden alarak bir an önce işleme girmesini sağlar.**

** Benzer şekilde, akümülatör de hesap sonuçlarını genel amaçlı kaydedicilere yükler. Böylece daha hızlı çalışma olanağı yaratılmaktadır. Bu bakımdan, CPU ' da ne kadar çok kaydedici bulunursa , bilgisayar da işlemleri o kadar hızlı yapabilme olanağına sahip olacaktır. Büyük boy bilgisayarlarda bunu gerçekleştirmek mümkündür. Fakat mikro bilgisayarlarda entegre devrenin mümkün olduğu kadar küçük yapılması ihtiyacı, eleman sayısı bakımından sınır getirmektedir.büyük boy bilgisayarların işlem hızının yüksek olmasının en önemli faktörlerinden biri bunun gibi olanakların bulunmasıdır.**

**Akümülatör:**** Aritmetik veya mantık işlemleri sırasında kullanılan geçici olarak saklandığı bilgi kaydedicileridir. Bazı bilgisayarlarda bir, bazılarında ise birden fazladır. Bu da hesaplama işlemi kolaylaştırır.**

**İndis kaydedicisi:**** Adresleme işlemi için kullanılır. **

**Bayrak Devresi ****: Bayrak devresi, Aritmetik-Lojik birimi (ALU) içindeki işlemlerin sonucunu gösteren bir bilgi devresidir.Bayrak devresi flip-flop lardan oluşmaktadır. 8 flip-flop devresi bir araya gelerek BAYRAK KAYDEDİCİSİ ni (Flag Regiter) oluşturmuştur.**

**Yığın göstericisi:**** ****Yığın gösterici 16 bit'lik bir kaydedicidir. Yığın belleğinin adres göstericisidir. Yığın belleği, RAM belleğin bir bölümüdür.Yığın gösterici, kaydedicilerdeki bilgilerin, aktarılabileceği yığın bellekteki boş adresleri belirlediği gibi, yığın bellekten alınacak bilgilerin adreslerini de belirler.**

** Ayrıca şu görevleri de vardır: **

** \* Alt yordam ile, değişmemesi veya kaybolmaması gereken kaydedici bilgilerin depolanması .**

** \* Alt yordam çağrısı sırasında dönüş adresinin saklanması.**

** \* Kesme denetimi. **

** \* Verilerin program denetimi altında geçici olarak saklanması.**

**Durum saklayıcısı:**** CPU’nun içerisindeki durumu gösteren ve bayrak adı verilen flip-floplar grubudur. Bilgisayarın karar verme mekanizmasının temeli bu bayraklardır ve sayıları bilgisayardan bilgisayara değişebilir. Yaygın olarak kullanılan bayrak türleri elde(carry), taşma(overflow), sıfır(zero), eksi(negative), yarım elde(half carry), kesme maske(interrupt mask) dır.**

## **KONTROL BİRİMİ:**

** Bilgisayarın en önemli birimi olan bu bölümün ana görevi bilgi işlemektedir. Dolasıyla da merkezi işlem birimi (central processing unit –CPU) olarak adlandırılır. CPU bellekten komutları alır, çözümler, zamanlama ve denetim işaretlerini üretir, bellek ve I/O(giriş-çıkış) bölümlerinden veya bölümlerine veri transfer eder veri üzerinde aritmetik ve mantık işlemleri yapar ve dıştan gelen işaretleri (kesme gibi) tanır ve gereğini yapar.**

** Giriş veri taşıtı Çıkış veri taşıtı **

** *****Komut İşleme Kaydediciler***

** Alanı**

** Zamanlama Adres Aritmetik**

** Ve Denetim İşleme Birimi**

** Denetim taşıtı Adres taşıtı******

## **Merkezi İşlem Birimini Yapısı :**

**Bir komutun yerine getirilmesi sırasında CPU’nun yaptığı işler aşağıda sıralanmıştır.**

**1- Komutun adresini adres taşıtına çıkarır.**

**2- Komutu veri taşıtından alır ve kodu çözer.**

**3- Komutun gerektirdiği adresleri ve veriyi içeri alır. Bunlar bellekte veya kaydedicilerde olabilir.**

**4- Komut kodunu belirttiği işlemi yerine getirir.**

**5- Kesme işareti gibi denetim işaretlerine bakar ve gereğini yerine getirir.**

**6- Bellek ve I/O bölümlerinin kullanımı için durum, denetim ve zamanlama işaretlerini üretir.**

## **8 BİT MİKROİŞLEMCİLER :**

** 1971 yılında Intel firmasınca üretilen mikro işlemciye benzer 4-bitlik 4004 entegresi masa üstü hesaplayıcılarda kullanılmıştır. Bir bilgisayar için tasarlanmış olmasına rağmen ilk genel amaçlı entegre olarak kabul edilmiştir.**

** Yine aynı firma tarafından PMOS teknolojisiyle 8008 işlemcisi geliştirilmiş ve sınırlı görev yapsa da ilk kuşak mikroişlemci olarak anılmıştır. Daha sonra NMOS teknolojisi kullanılarak ikinci kuşak 8-bitlik ilk genel amaçlı 8080 işlemcisi geliştirildi. **

** 1974 yılında yine dünyaca ünlü başka bir entegre üreticisi olan Motorola 8-bitlik 6800 mikroişlemcisini üretti. Bu işlemci bazı küçük farklılıklarla birlikte 8080 işlemcisinin bir benzeri sayılmaktadır. Hemen bir sonraki yılda MOS Tegnology ve Fairchild firması bu kitabında temelini oluşturan 6500 serisi işlemcileri üretmeye başladı. **

** Bu işlemcide çok büyük birkaç ayrıcalıklarla 6800 ile benzerlik göstermekteydi.. her iki işlemcide kullanılan bütün yardımcı elemanlar birbirini tam olarak desteklemekteydi. Daha sonra Zilog firması 8080 işlemcisinin bir benzeri olan ve birkaç üstün özellikle donatılı Z-80 işlemcisini tanıttı. Bütün bu dört çeşit mikroişlemci kendi aralarında bazı özelliklerinden dolayı iki gruba ayrılırdı. Bunlardan 8080 ile Z-80 ve 6800 ile 6500 işlemcileri yapısal bakımdan birbirleri ile benzerlik göstermekteydi.**

** 8-bitlik 8080/Z-80 grubu mikroişlemcilerin hesaplayıcılar olarak tasarlanması ve bundan dolayı da kaydedicilerin bol kullanılması, bunların kaydediciye dayalı mimari olarak anılmasına sebep odu. 6500/6800 işlemci grubunun küçük bir bilgisayar sınıfına girebilecek şekilde daha anlaşılır komutlar ve daha fazla adresleme modu kullanması sebebiyle belleğe dayalı mimari olarak anıldılar. Bu iki grup 1980 yıllarının en iyi satan işlemcileri olarak ün yaptılar.**

** 8-bitlik işlemcili bilgisayarların bellek adresleme kapasiteleri, (16-bitlik adres yoluyla 2****16****=64 KB) 65.566 Bayt ile sınırlıydı ve bu kapasite gittikçe büyüyen yazılım ve programlara yetersiz kaldı.**

** 8-Bitlik Popüler Mikroişlemcilerin Teknik Özellikleri**

## **16 BİT MİKROİŞLEMCİLER**

** Intel veya Motorola’nın haricinde birçok üretici firma, 8 veya 16 bitlik işlemci geliştirmiş fakat, ülkemize ilk giren bilgisayarda bu iki firmanın işlemcisinin kullanılmış olması sebebiyle daha çok bu iki işlemci üzerinde durulmuştur.**

** Intel firması 1974 8 bitlik başka bir 8080 versiyonu mikroişlemci geliştirmesine rağmen asıl atılımı 1978 yılında NMOS teknolojili tek entegrelik 16 bitlik8086 işlemcisiyle yaptı. 8086, 8080’in bir ileri versiyonu olmasıyla beraber birbirleriyle uyumlu değildirler. Daha sonra Intel firması 8086 ile aynı mimari yapıya sahip bir türevi olan 8088’i çıkardı. **

** Bu işlemcilerden 8086, 16 bitlik veri yoluna sahip olmasına rağmen 8088, 6 bitlik veri yoluna sahipti. Bu sebepten 8088, 8086’dan biraz daha yavaştır. Bu sıralarda IBM firması artık bir endüstri standardı haline gelen PC bazlı bilgisayarında 8088 işlemcisini kullandı. O günlerde üretilen bilgisayarlar iki standart birden kazandılar. Birincisi PC (Personel Computer-kişisel Bilgisayar) standardı ikincisi, 8-bitlik mikroişlemcilerden sonra 16-bitlik işlemcilerin kullanıldığı bilgisayarlar XT(eXtended Technology-Gelişmiş Teknoloji) standardıdır.**

** 1979 yılında Motorola 68000 oldu 16-32 bit arasında bir mikroişlemci üretti. 16 bitlik veri yoluna sahip bu işlemcideki kaydedicilerin 32 bitlik olması, 16 Megabaytlık bir bellek adreslemesini de beraberinde getirdi. Adresleme kapasitesinin bu denli büyük olması 68000 mikroişlemcisini popüler yaptı ve Apple Machintosh, Amiga ve Atari gibi ünlü firmalarca bilgisayarlarda kullanılmıştır.**

** 1982 yılında yine Intel firmasınca yeni bir standart olan ve kullanıldığı bilgisayarlara AT(Advandec Technology-İleri teknoloji) denilen 80286 mikroişlemcisini üretti. Bu işlemcide kaydedicilerle birlikte hem veri yolu hem de adres yolu 16-bit olarak tasarlandı. Mikroişlemci içerisindeki 16-bitlik kaydedici çıkışları çoğaltılarak (bir kaydıran kaydedici vasıtasıyla dört defa kaydırılarak) 20-bite çıkarıldı(2****20****=16 Megabayt) ve böylece 1 Megabaytlık adresleme kapasitesi elde edilmiş oldu. **

** 1985 yılına kadar bilgisayarların önemli pazar payına sahip iki işlemcisi , Dos(Windows) işletim sistemini kullanan 80286 işlemcisini üretti. Böylece büyük yazılımlar için gerekli olan büyük bellek kapasiteleri, sistemde kullanılan disklerin bir bölümünün ana belleğin bir parçasıymış gibi davranması sağlanarak halledilmiş oldu.**

## **32 BİT MİKROİŞLEMCİLER :**

** Mikro elektronik teknolojisinin hızla gelişmesi beraberinde mikroişlemcilerin gelişmesini dolayısıyla da sistemde kullanılan program ve yazılımlarında gelişmesini sağladı. **

** Yeni geliştirilen bir mikroişlemci anında bir bilgisayarda kullanıldı ve buna göre de kısa sürede bir çok yazılımlar geliştirildi. Yazılımların kapladığı bellek alanlarının büyümesi beraberinde bellek problemini doğurdu ve mikro işlemcilerde yeni tasarımların oluşması gerçekleşti. Bunlardan en önemlisi gerçek ve bütünüyle 32-bitik mikroişlemcilerin ortaya çıkması ve işlemcilerin performansını artıran destek devrelerinin geliştirilmesidir. **

** 1984 yılında Motorola 68020 işlemcisini, ardından1985 ‘de Intel 80386 işlemcisini üretti. Bu iki mikroişlemci de gerçek birer 32 bitlik işlemcidir. 80386 aşağı-yukarı daha önceki üretilen 80286’dan 8086’ya kadar geriye doğru uyumludur. 8086’da yazılmış programlar 80386’lı bilgisayarlar da çalışır fakat, 80386’da yazılan gerçek mod (Real Mode) dışındaki programlar alt versiyondaki işlemcili bilgisayarlarda çalışmaz. AT tipi makinaların önemli bir özelliği de gerçek mod ve korumalı mod (Protected Mode ) denilen 2 ayrı modda çalışabilmeleridir. Gerçek modda sistem normal olarak 1 megabaytlık bellek kullanarak kendi başına çalışır.**

** Korumalı modda , bilgisayar başka bilgisayarlarla ortak olarak çalışabilir ve aynı anda ortak dosya paylaşımı, ortak sistem kullanımı ve zaman paylaşımı denilen sistem kullanılır. Ayrıca bu modda 1 megabayt sınırı aşılarak büyük bellek kapasiteleri kullanılabilmektedir. 32-bitlik işlemciler 2****46**** adres yolu ile tele bayt cinsinden bellek kapasitesi kullanılabilir. Fakat günümüzde bu rakam çok fazla ve aynı zamanda pahalıdır. **

** Bu yıllarda Intel’in ürettiği işlemciler IBM uyumlu PC ve AT tipi bilgisayarlarda kullanılırken Motorola işlemcileri, masa üstü yayıncılık ve grafik işlemler için kullanılan bilgisayarlarda tercih edildi. **

## **Intel Mikroişlemci Ailesi**

**yılında 80386’nın bir değişik modeli olan 80386SX geliştirildi. Bu işlemcide de 32-bitlik kaydediciler kullanılırken,80286 ile soket uyumluluğu sağlamak için veri yolu 16-bite indirildi. 80386SX teriminin kullanılması normal 80386’nın 80386DX olarak anılmasına sebep oldu (Eğer 8088, 8086’nın bir sonraki alt versiyonu ise buna 8086SX denilebilir).**

## **MİKROİŞLEMCİ ÖZELLİKLERİ :**

** Bilgisayarın beyni sayılan Mikroişlemcileri birbirinden ayırt eden en önemli unsurlar onların işlevleri ve özellikleridir.Bunlar:**

**a- Mikroişlemcinin Bir Defada İşleyebileceği Kelime Uzunluğu**** :Mikroişlemcilerde kelime uzunluğu veya bit uzunluğu paralel olarak işlenen veri bitlerinin sayısıdır. Kelime, işlemcideki genel amaçlı kaydedicilerin büyüklüğü ve aynı zamanda her bir bellek mahalli kapasitesidir. Büyük kelime uzunluğu, aynı anda birçok işlemin birlikte yapılması ve bazı uygulama program yazımları için kolaylık demektir.**

** İşlemciler, her bir saat çevriminde senkronize olarak o anda komut kuyruğunda bulunan komutları ve bunlara göre de bellekteki verileri işlerler. Bilgi bitleri Mikroişlemcinin tipine göre 1, 4, 8, 16, ve 32’lik sıralar halinde işlenir. Bir mikroişlemcili sistemde çok basit problemler tek bit kodunda işlenebilir. Buna örnek olarak içerisinde işlemci bulunan soğuk içecek makinalarıdır ve tek bit esasına göre tasarlanmıştır. **

** Küçük hesap makineleri ve cep bilgisayarlarında basit aritmetik problemlerin çözümünde 4 bit kullanılmaktadır. Normal bilgisayarlarda bütün bilgiler 8 bit (1 Bayt), 16 bit(1Word) veya 32 bit (1 Doubleword)olarak işlenirler eğer komutlar veya veriler küçük gruplar halinde işlenirse hızda bir azalma olacak ve bu yüzden performans düşecektir.**

** Kelime uzunluğu büyük olan işlemcide yapılan aritmetik işlemlerde doğruluk oranları kısa uzunluklu kelimelere nazaran çok yüksektir (4-bit %6, 8-bit %0.4 ve %0.001).Eğer işlemcinin kelime uzunluğu, tek bir kelimeyle ele alınan belirli bir problem için yetersizse, tek bir verinin işlenmesi için işlemci daha fazla zaman harcayacak ve veri işleme hızı düşecektir.**

**b- Mikroişlemcinin Tek Bir Komutu İşleme Hızı :**** Bir mikroişlemcinin hızı saat frekansıyla doğrudan ilgilidir. Fakat saat frekansı her zaman gerçek çalışma frekansını yansıtmaz. İşlemci hızını belirleyen birçok yol vardır. Bunlar, çalışma çevriminin uzunluğudur ki (al-getir kodunu çöz-işlet-depola), bu ölçüm fazla kullanışlı değildir. **

** Bilgisayar üreticileri daha çok hız ölçmek için özel bazı test programları geliştirmişlerdir. Başlıca mikroişlemci hızları mikro saniye olarak 16, 25, 33, 100Mhz ve mibs’tir(saniyede milyon adet komut işleme ).**

**Bir mikroişlemciyi diğerinden daha hızlı yapan unsurlar şunlardır;**

** - CPU’nun devre teknolojisi ve planı. Mesela katı –durum elektroniğinde kullanılan bazı teknolojiler diğerlerine nazaran daha hızlı cevap veren devreler üretmektedirler. **

** - Birinci maddede açıklandığı gibi, işlemcinin bir defada işleyebileceği kelime uzunluğu. Uzun kelime hızlı işlem demektir.**

** - İşlemci komut kümesi çeşidi. Bir işlemcide bir işlem tek bir komutla yapılırken diğerinde daha fazla komutla yapılabilir.**

** - Genel olarak zamanlama ve kontrol düzeni. **

** - Kesme altyordamlarının çeşitleri.**

**Bilgisayar belleğine ve I/O cihazlarına erişim hızı.**

## **c- Mikroişlemcinin Doğrudan Adresleyebileceği Bellek Büyüklüğü :******

**Bilgisayar sistemlerinde ana bellek mikroişlemci tarafından adres yolu vasıtasıyla adreslenir. Adres yolu hattı ne kadar çoksa adresleme kapasitesi de ona göre büyük olur. Adres yolu doğrudan mikroişlemci yapısıyla mikroişlemci yapısıyla ilgili olup işlemciye göre standarttır. Fakat işlemci içerisindeki kaydedicilerin büyüklüğü işlemci adres çıkışında bir kaydıran kaydedici(shift register) yardımıyla arttırabilirken ve adres yolu da çoğaltılmış olur. XT tipi bilgisayarlarda kaydediciler 16 bitlik olmasına rağmen adres bilgisi 4 bit kaydırılarak 20-bitlik hatta verilip, 1 MB’lık bellek adreslenebilmektedir. AT tipi bilgisayarda 24, 32, 46-bitlik adres hattı kullanılarak gerçek modda 4 Gigabayt ve korumalı modda 70 Terabayt adreslenebilmektedir.**

**2****10 **** Kilobayt, 2****20 ****Megabayt, 2****30 ****Gigabayt ve**** ****2****40 ****Terabayta karşılık gelir.**

**Yukarıda anlatılan 3 temel özellik yanında mikroişlemcileri dolaylı olarak etkileyen birçok unsurlar vardır. Bunlar:**

## **d- Kullanıcı Veya Programcının Mikroişlemci Üzerinde Çalışabileceği Kaydedici Sayısı Ve Farklı Tipleri :**

**Kullanıcı verileri bu kaydediciler üzerinde çalıştırır. Kaydedici sayısının fazla olması manevra kolaylığı ve elastikiyet sağlar. Genel amaçlı kaydediciler (EAX, EBX, ECX ve EDX), işaretçi ve indeks kaydediciler (ESP, EBP, ESI, EDI, EIP), bayrak kaydediciler (C, P, A, Z, S, T, D, I, D, O, IOPL, NT, RF, VM, AC) ve Segment kaydediciler (CS, DS, ES, SS, FS, GS). bunlarında haricinde korumalı modda kullanılan Selektör, tanımlayıcı ve bunlara ilişik olarak Tablo kaydedicileri vardır (TR, LDTR, GDTR, IDTR).**

## **e- Programcının Elde Edebileceği Değişik Tipteki Komutlar :**

**Mikroişlemci hızını etkileyen komutlar, veri manevra komutları, giriş/çıkış komutları, aritmetik komutlar, mantık komutları ve test komutları gruplarından birisine dahildir. Mikroişlemcinin kütüphanesinde bulunan komutların çokluğu sisteme belki elastikiyet sağlar fakat, asıl olan komutun az saykılla işlemi tamamlamasıdır.**

## **f - Programcının Bellek Adreslerken Gerek Duyacağı Farklı Adresleme Modlar:**

**Doğrudan adresleme, dolaylı adresleme ve indeksli adresleme gibi adresleme türleri programcıya ekstra kolaylık sağlar. Adresleme modları, üzerinde çalışılan bir verinin bellekten nasıl ve ne şekilde yerleştirileceği veya üzerinde çalışacak bir verinin bellekten nasıl ve hangi yöntemle çağırılacağıdır. Bu işlem bir mektubun gideceği yere birisinin eliyle mi, bir nesne baz alınarak mı, sokaklar ve evler eklenerek mi gibi bir tarifle ulaşmasıdır.**

## **g-Uygulamalar İçin Sistemin Yazılım Uyumluluğu.**

**CP/M, DOS, MacOS, SISTEM 7, WINDOWS, UNIX, OS/2 ve LINUX.**

## **h - İlave Edilecek Devrelerle Uyumluluğu**

**Mikroişlemcili sisteme eklenecek devrelerin en azından işlemci hızında çalışması gerekir. Sisteme ilave edilecek bir SIMM veya SIP kartındaki bellek entegrelerinin hızlarının nanosaniye cinsinden işlemci ile aynı hızda olması tercih edilmelidir. Aynı şekilde sisteme takılan ekran kartının hızlandırıcısı ve VideoRAM’ların hızları ve performansları mikroişlemci ile aynı veya çok yakın olmalıdır. Sisteme eklenen devrelerin mikroişlemciden daha yavaş çalışması, işlemcinin hızını eklenen devrenin hızına düşürür.**

**9. Sistemi Tasarlayanın Kullanabileceği Değişik Tipteki Destek Devreleri.**

**PIA, ACIA, CO-PROCESSOR, CACHE MEMORİ, DMA gibi.**

**Yukarıda sıralanan belli başlı mikroişlemci özelliklerinin yanı sıra, işlemci besleme gerilimi (2.9V, 3V veya 5V), Mikroişlemcinin büyüklüğü, harcadığı enerjiyle birlikte ısınarak soğutucu gerektirmesi, Paketlenmiş ön-bellek 256 KB SRAM ve pipeline özellikleri (komutları çalıştırma işleminin hızlandırma gayesiyle safhalara bölünerek gerçekleştirilmesi işlemi) sayılabilir.**

## **MİKROİŞLEMCİ DESTEK DEVRELERİ**

** Mikroişlemcili sistemlere, sistemin performansını artıran destek devreleri ilave edilebilir. Bunlar sistemin elastiki olmasını ve diğer devrelerle uyumlu çalışmasını sağlar. Belli başlı destek devreleri şunlardır.**

## **A - Ortak İşlemci :**

** Diğer bir adı da Matematik işlemci veya FPU olan bu elaman, ana mikroişlemci bazı hane sayısı fazla olan matematiksel işlemlerde (floating point gibi) veya nokta yoğunluğu artan grafik işlemlerinde mikroişlemci yavaşladığında otomatik olarak iç kontrolörü vasıtasıyla devreye girerek performansı düşürmez. **

** Mesela, yoğun hesap işlemlerinin yapıldığı elektronik tablolama gibi muhasebe programlarının kullanıldığı veya CAD gibi programlar kullanılarak hazırlanan mimari çizimlerin yapıldığı sistemlerde ortak işlemci kullanmak gereklidir. Bunların yerine aynı performansı sağlamasa da emülatör programları kullanılmaktadır.**

## Ortak İşlemcilerin Sistemdeki yeri

**286 ve 386 – 020, 030 ve 040’lara kadar ortak işlemciler ana işlemcilerden ayrı (80287, 80387 gibi) olarak pazarlanmaktaydı, fakat günümüze mikroişlemcilerinde artık ortak işlemci ana işlemcinin bir köşesini işgal etmektedir.**

## **Paralel İşlemci **

**Bazı sistemlere ana işlemciye paralel olarak konulan bu destek elamanı, sistemin aşırı yüklenmesi veya uzun süre çalışmasından dolayı hız yavaşlamasının ortaya çıkmasıyla kendisine gösterir. Tek bir işlemci üzerinde saatlerce süren çalışma o işlemci üzerinde ısınma meydana getirerek sistemin yavaşlamasına, bundan dolayı da performansın azalmasına sebep olur. ******

** Bu gibi durumlarda birinci işlemci ile aynı özelliklere sahip ikinci bir işlemci sisteme dahil edilerek bu problemin üstesinden gelinir. Birinci işlemcideki küçük bir hız düşmesi sistem tarafından algılanarak hemen o anda yedekte beklenen ikinci işlemci devreye sokulur. **

** Daha sonra ikinci işlemci hız azalması gösterildiğinde bu defa dinlenmiş ve soğumuş olan birinci işlemci devreye sokulur. **

** Bundanda anlaşıldığı gibi mikrobilgisayarlarda bu gibi hız azalmasına sebep olacak büyük programlar kullanılmadığında, paralel işlemciler büyük boy bilgisayarlarda veya çok büyük boy bilgisayarlarda kullanılmaktadır. 1995 yılında PC bilgisayar da girmiştir.**

## Paralel İşlemci Temel Yapısı

## ** C - Ön Bellek**

** Her ne kadar adı tampon bellek ise de, mikroişlemcinin performansını doğrudan etkileyen bir eleman da ön-bellektir. İşlemci üzerinde çalıştığı verinin geçici bir süre başka yerde kalmamasına karar verirse bu yer elbette ki ana bellek olacaktır. **

** Fakat kısa bir süre sonra aynı anda data(veri) ile çalışacaksa veriyi tekrar bellekten alıp getirmek veya yeniden oraya koymak, bir hayli zaman gerektirecektir ki, bu da hız azalmasına ve performansının düşmesine sebep olacaktır.**

## *** *****Ön-Bellek Devresinin Sistemdeki Yeri**

** Bu gibi durumların üstesinden gelmek için önceleri mikroişlemci dışında ama anakart üzerinde hemen yanı başında, sonraları mikroişlemci entegresi içerisinde yeri sınırlı bir bellek oluşturuldu ki bunun adı ön-bellektir. İşlevi, adı geçen veri ana belleğe gönderilmeden sistem tarafından hemen yanı başında ön-belleğe yollanır ve gerekli olduğunda da hemen yakınından alınır. **

** Böylece sistem, işlemci dışında harcayacağı zamanı kendi içinde ve çok hızlı olarak (mikroişlemci hızının dahili olarak iki yada dört katına çıkarıldığını hatırlayınız) aşağıya çeker.**

** Günümüz mikroişlemcilerinde L2 ön-bellek ve L1 ön-bellek olmak üzere iki adet bellek vardır. İşlemci ile ana bellek arasındaki bu ön-belleklerden L2 ana belleğe daha yakınken, L1 ön-bellek işlemciye yakındır. Gelecekteki ön-belleklerin hedefi daha fazla bilgileri üzerlerinde tutabilmeleridir.**

## **Pentium 3 ve Pentium 4 arasındaki fark nedir ?**

** Intel Pentium tipi işlemcileri ürettikten sonra yeni çıkardığı farklı tip işlemcileri aile (family) olarak sıralandırdı.**

** Pentium (I) ailesi, Pentium Pro ailesi, Pentium 2 ailesi, Pentium 3 ailesi, Pentium 4 ailesi**

**Aynı aile içinde kalan işlemciler işlemci hızları ile sınıflandırıldılar.**

** Pentium ailesi 75Mhz ile başlayıp Pentium 166Mhz e kadar devam etti. Bu hıza erişildiğin de intel işlemcilerine multimedya desteği sağlayan MMX teknolojisini yerleştirdi. Pentium 166MMX den 233MMX e kadar bu seri devam etti. Intel genelde CISC mimarili (Complex Instruction Set Computer - Karmaşık kod setli bilgisayar) işlemciler üretmekle beraber RISC mimarisi olan Pentium Pro tipi işlemcide üretmiştir.**

** Intel’in halen üretmekte olduğu P2 , P3 ve P4 işlemciler CISC tabanlıdır. Intel hız faktörünü kullanarak teknoloji sayesinde CISC işlemcilerini RISC işlemcilerin avantajlarını da içeren bir hale getirmektedir.**

** O halde P2 P3 ve P4 arasındaki fark onların mimarisidir. En belirgin faktörlerden birisi Cache adı verilen özel belleklerdir. L1 ve L2 tipi cacheler kullanılmaktadır.**

** Cache ve işlemcinin (CPU) arasında ki ilişki aşağıdaki şekilde göstermektedir . (standart Pentium işlemci).**

** İşlemcinin (CPU) burada iki bölümle temsil ediliyor; Cache bellek ve Registers(kayıtçılar) . Registerların sayısı sınırlı olduğu için üzerlerinde tutmaları gereken bilgileri cache bellek üzerinde saklarlar.**

** L2 cache ise CPU grubu ile bilgisayarın asıl RAM hafıza ünitesi arasında bir çeşit köprü görevi görürler. ******

| **CPU - İŞLEMCİ****** | **Cache boyutu****** |  |
| --- | --- | --- |
| **MODELİ****** | **L1****** | **L2****** |
| **80486DX and DX2** | **8 KB L1** |  |
| **80486DX4** | **16 KB L1** |  |
| **Pentium** | **16 KB L1** |  |
| **Pentium Pro** | **16 KB L1** | **256 KB L2 (some 512 KB L2)** |
| **Pentium MMX** | **32 KB L1** |  |
| **AMD K6 and K6-2** | **64 KB L1** |  |
| **Pentium II and III** | **32 KB L1** |  |
| **Celeron** | **32 KB L1 ** | **128 KB L2** |
| **Pentium III Cumine** | **32 KB L1 ** | **256 KB L2** |
| **AMD K6-3** | **64 KB L1 ** | **256 KB L2** |
| **AMD K7 Athlon** | **128 KB L1** |  |
| **AMD Duron** | **128 KB L1** | **64 KB L2** |
| **AMD Athlon Thunderbird** | **128 KB L1** | **256 KB L2** |

## **ÖZET:**

** Mikroişlemci tarafından gerçekleştirilen fonksiyonlar(işlevler) özet olarak şöyle sıralanabilir:**

** a) Bellekten veya bir giriş kapısından VERİ OKUMAK.**

** b) Belleğe veya çıkış kapısına VERİ YAZMAK.**

** c) Kendi içinde işlem yürütmek. Yani, belleğe veya I/O kapılarına gitmeden kaydediciler arası işlem yapmak.**

** Örneğin, bir kaydedicinin içeriğinin diğer bir kaydediciye aktarılması veya bir kaydedicinin içeriğinin aktarılması veya azaltılması gibi.**

** d) Diğer bir bellek bölgesine transferin kontrolünü sağlamak.yani, gerek ana belleğin kendi bölümleri arasında, gerekse ana bellek ile yardımcı bellekler arasındaki bilgi aktarımını sağlamaktır. **

## **- son - **

FILENAME İŞLEMCİLER

## PAGE 2

## Harici Ortak İşlemci

## Ana Bellek

## Mikroişlemciler

## Dahili Ortak İşlemci

## Veri Yolu

## G/Ç

## Harici Ortak İşlemci

## Mikroişlemciler

## Dahili Ortak İşlemci

## G/Ç

## Ana Bellek

## Veri Yolu

---
*Kaynak: `İŞLEMCİLER/IŞLEMCILER.doc` — Tuncay — 2003*
