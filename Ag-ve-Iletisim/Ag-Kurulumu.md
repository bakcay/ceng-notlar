# Ağ Kurulumu

AĞ Ağ ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Ağ simgesine çift tıklayın...

Ağ ayarlamaları, bir network(workgroup) içinde yer alan Windows 98 bilgisayarının network adaptörü, protokol vb... bileşenlerinin kurulmasını ve yapılandırılmasını sağlayan bir menüdür. Windows 98, kuruluş sırasında network kartını ve bağlı olunan network' u tanıyıp bilgisayarın yapılandırılmasını sağlayabilir. Bu menü 3 katmandan oluşmaktadır. Yapılandırma, Tanımlama, Erişim Denetimi.

Yapılandırma Katmanı:

Bu katman Ağ menüsüne ilk girildiğinde zaten aktif durumdadır. Burada ağ için gerekli bileşenlerin mevcut olanlarının bir listesi görülecektir. Biz burada gerekli olacak yeni bir bileşeni daha ekleyebiliriz. Örneğin ethernet kartı tanımlanmıyorsa, buradaki menüde Ekle butonuna tıklayarak Bilgisayar yapısında mevcut bulunan(eğer varsa) ethernet kartını tanımlayabilir ve bu bileşenler içine katabiliriz.

Tanımlama Katmanı:

Bu katmanı kısaca açıklayacak olursak, ağ üzerindeki bilgisayarların birbirlerini tanımalarına kolaylık kazandırır. Herkesin bir ismi vardır; Ahmet, Ali, Ayşe...Biz de burada bilgisayarımıza bir isim vererek onun ağ üzerinde tanınmasına sebebiyet veririz. Ayrıca bulunacağı ağ ortamınında bir ismi olacaktır. Mesela bizler insanlar ile çalışırız. Burada da bilgisayarın çalışacağı ortamın ismini "Çalışma Grubu" yerine yazarak adlandırabilir ve o bilgisayarı, ağ ortamına sokmuş oluruz.

Erişim Denetimi Katmanı:

Bu katman sayesinde ağ ortamına soktuğumuz bilgisayarımızın etkinliğini ayarlarız. Yani bu ağ ortamında kullanılacak kaynakların veyahut dosyaların kullanımına bir parola getirebilir yada serbest bırakabiliriz. Bu katman menüsünde de görüleceği üzere 2 seçenek mevcuttur. Bunlar "Paylaşım düzeyi erişim denetimi", "Kullanıcı düzeyi erişim denetimi". Bunlardan paylaşım düzeyi erişim denetimi, ağ ortamına soktuğumuz bilgisayarımızın her kaynağına bir parola getirmemizi sağlar. Kullanıcı düzeyi erişim denetimi ise bu kaynakların kullanımına izin verdiğimiz bilgisayarların tanımlanmasını sağlar.

Bağlantıyı sağlayan ve ulaşılmak istenen bilgisayara giden yolu bulan katmandır. Yönlendirme protokolleri bu katmanda çalışır.

Ağ tabakası alt ağda yapılan işlerin denetimi ile ilgilidir. Tasarımında anahtar konu veri paketlerinin kaynaktan hedefe nasıl yönlendirileceğidir. Yönlendirmeler sabit tablolara dayalı ve sıkça değişmeyecek şekilde ağ ile birlikte tanımlanmış olabilir. Bu yönlendirmeler ayrıca bir terminal oturumunda olduğu gibi, her oturum için ayrıca belirlenebilir. Son olarak anlık ağ yüküne bağlı olarak her bir yeni paket için yeniden belirlenecek şekilde dinamik olabilir. Aynı anda ağa birbirinin rotası üzerine çakışan birçok paket ağa sunulursa performans sıkıntıları oluşabilir. Bu tür çakışmaların önlenmesini sağlamak ağ katmanının sorumluluğundadır.

Ağ operatörleri, servisi paralı olarak vermek istediklerinde ayrıca ağ katmanı üzerinde raporlama özellikleri de eklenir. Sonuç olarak bir yazılım aracılığı ile her müşterinin ilettiği veya aldığı paket veya karakter sayısı faturalama bilgisinin üretilmesi sayılır. Raporlama, değişik ücretlendirme oranlarının uygulandığı sınırları geçildiğinde daha karmaşık bir hal alabilir.

Bir paket hedefine ulaşmak için bir ağdan diğer bir ağa geçmek zorunda kaldığında başka problemler de baş gösterebilir. Adresleme ağlar arasında farklı olabildiği gibi, bir ağ diğerinden çok geniş olduğu için paketi kabul etmeyebilir veya protokoller farklı olabilir. Heterojen ağların ara bağlantılarının sağlıklı bir şekilde yapılıp bu problemlerin üstesinden gelme ağ katmanın sorumluluğundadır. Yayın ağlarında, ağ katmanı çok ince veya hiç varolmadığından, yönlendirme problemi daha basittir.

TCP/IP (Transmıssıon Control Protocol/Internet Protocol) TCP/IP’ nin Tarihçesi TCP/IP nin kökenleri 1960 ların sonunda ve 1970 lerin başlarında Amerikan savunma bakanlığına bağlı İleri Araştırma Projeleri Ajansının (Advanced Research Projects Ağency,ARPA) yürüttüğü paket anahtarlı ağ deneylerine kadar uzanır. TCP/IP’nin yaratılmasını sağlayan proje , ABD deki bilgisayarların bir felaket anında da ayakta kalabilmesini , birbirleriyle iletişimin devam etmesini amaçlıyordu. Amacına fazlasıyla ulaştığı gibi interneti de ortaya çıkardı. TCP/IP (Transmıssıon Control Protocol/Internet Protocol) TCP/IP, Transmission Control Protocol/Internet Protocol ifadesinin kısaltılmasıdır. Türkçesi “İletim kontrol protokolü/İnternet Protokolü” dür. Protokol belli bir işi düzenleyen kurallar dizisi demektir. Örneğin devlet protokolü devlet erkanının nerede duracağını, nasıl oturup kalkacağını düzenler. Ağ protokolüde bilgisayarlar arası bağlantıyı, iletişimi düzenliyor.

TCP/IP Unix dünyasının standart iletişim kuralıdır. Aynı zamanda internetin de temeli olan Savunma Bakanlığı(ABD) tarafından geliştirilmiştir. İnternet adresleri InterNIC tarafından atanır. Eğer TCP/IP ağınız internete bağlı değilse ve hiçbir zaman bağlanmayacaksa, geçerli herhangi bir adres alanını kullanabilirsiniz. Ancak eğer ilerde bağlanma şansınız varsa adres için başvurmanız gerekir.

Netware’in içinde TCP/IP desteği vardır ve tünelleme olarak bilinen süreç ile bir TCP/IP ağda IPX çalıştırmanıza imkan verir.

Tünelleme; IPX paketi bir TCP/IP önbilgi ve artbilgiyle çevrelenir. Böylece paket IPX ağdan TCP/IP ağa, oradan tekrar IPX ağa geri yöneltilebilir.

Artık çoğu işyerlerinin internete doğrudan bağlantısı yoktur. Doğrudan bağlantı büyük bir güvenlik riski doğurmaktadır.Genellikle “firewall” olarak bilinen iç ağ ile internet arasında sadece izin verilen trafiğin olmasını sağlayan bir sunucu veya yöneltici kullanırlar. Firewall kullanıldığında iç ağ numaraları herhangibir geçerli adres olmayabilir ve firewall yönelticinin ihtiyacı olan tek şey “düzgün” yetkili bir internet numarasıdır. Değişik tipte bilgisayarların bir arada çalışabilmelerini garantilemek amacıyla programcılar programlarını bazı standart protokolleri kullanarak yazarlar. Bu protokol, teknik bir terim olarak işlerin nasıl yapılması gerektiğini tarif eden kurallar bütünüdür. Örneğin, bir posta mesajı için hangi formatın kullanılacağını tam olarak tarif eden bir protokol bulunmaktadır. Tüm internet posta programları, mesaj gönderecekleri zaman bu protokolü takip ederler. TCP, gerçekte iki ayrı protokolden oluşur: TCP ve IP. TCP/IP ikisinin beraber kullanıldığı zamanlarda genellikle tercih edilir.

IP- Bu bölümde datagramlara bölünmüş bilgi paketleri diğer bilgisayar ve ağlara yönlendirilir. Bu datagramların herbiri IP’den bağımsız olarak düşünülür.

IP datagramın hedefine ulaşacağını garantilemez veya herhangi iki datagramın aynı yolda alınacağıyla protokol datagramların sıralandığı gibi gönderilmesini sağlamaz.

Bu protokolün basitliği ve her datagramın bağımsız olması sebebiyle IP bir bağlantısız(connectionless protocol) olarak düşünülür.

TCP- TCP, datalardan segmentleri düzenler ve gönderilmesi için IP katmanına geçirir. Bu katmanda IP katmanından alınan datagramlar tekrar sıralanır ve verinin değişmiş olup olmadığı, hatasız geldiğinden emin olunur. TCP veriyi ilettiğinde bir zamanlayıcı(timer) düzenler. Bir paket uzak bir bilgisayara ulaştığında bir onay(acknowledment) göndericiye ulaştırılır. Eğer onay ulaşmadan zamanlayıcının süresi dolarsa paket tekrar transfer edilir. Tüm pratik amaçlar için bir makinedeki TCP protokolü uzak bilgisayarlara bağlantı kurmak için TCP protokolüyle iletişim kurar.

TCP; bağlantı tabanlı protokoldür(connection-oriented protocol). Bir uzak bilgisayarla sanal bir dolaşım sağlamaya yarayan, port adı verilen başka adresleri formlamayı kullanır. TCP Telnet gibi birden fazla kullanıcı olduğunda aynı porttan çoklu işlemlere(Multiple processes) izin verir.

TCP/IP; katmanlardan oluşan bir protokoller kümesidir. Her katman değişik görevlere sahip olup altındaki ve üstündeki katmanlar ile gerekli bilgi alışverişini sağlamakla yükümlüdür.

TCP/IP katmanlarının tam olarak ne olduğu, nasıl çalıştığı konusunda bir fikir sahibi olabilmek için bir örnek üzerinde inceleme yapalım:

TCP/IP’nin kullanıldığı en önemli servislerden birisi elektronik postadır (e-posta). E- posta servisi için bir uygulama protokolü belirlenmiştir (SMTP). Bu protokol e- posta’nın bir bilgisayardan başka bir bilgisayara nasıl iletileceğini belirler. Yani e- postayı gönderen ve alan kişinin adreslerinin belirlenmesi, mektup içeriğinin hazırlanması vs. gibi. Ancak e-posta servisi bu mektubun bilgisayarlar arasında nasıl iletileceği ile ilgilenmez, iki bilgisayar arasında bir iletişimin olduğunu varsayarak mektubun yollanması görevini TCP ve IP katmanlarına bırakır. TCP katmanı komutların karşı tarafa ulaştırılmasından sorumludur. Karşı tarafa ne yollandığı ve hatalı yollanan mesajların tekrar yollanmasının kayıtlarını tutarak gerekli kontrolleri yapar. Eğer gönderilecek mesaj bir kerede gönderilemeyecek kadar büyük ise (Örnegin uzunca bir e-posta gönderiliyorsa) TCP onu uygun boydaki segment’lere (TCP katmanlarının iletişim için kullandıkları birim bilgi miktarı) böler ve bu segment’lerin karşı tarafa doğru sırada, hatasız olarak ulaşmalarını sağlar. İnternet üzerindeki tek servis e-posta olmadığı için ve segment’lerin karşı tarafa hatasız ulaştırılmasını sağlayan iletişim yöntemine tüm diğer servisler de ihtiyaç duyduğu için TCP ayrı bir katman olarak çalışmakta ve tüm diğer servisler onun üzerinde yer almaktadır. Böylece yeni bir takım uygulamalar da daha kolay geliştirilebilmektedir. Üst seviye uygulama protokollerinin TCP katmanını çağırmaları gibi benzer şekilde TCP de IP katmanını çağırmaktadır. Ayrıca bazı servisler TCP katmanına ihtiyaç duymamakta ve bunlar direk olarak IP katmanı ile görüşmektedirler. Böyle belirli görevler için belirli hazır yordamlar oluşturulması ve protokol seviyeleri inşa edilmesi stratejisine ‘katmanlaşma’ adı verilir. Yukarda verilen örnekteki e- posta servisi (SMTP), TCP ve IP ayrı katmanlardır ve her katman altındaki diğer katman ile konuşmakta diğer bir deyişle onu çağırmakta ya da onun sunduğu servisleri kullanmaktadır. En genel haliyle TCP/IP uygulamaları 4 ayrı katman kullanır. Bunlar: ...Bir uygulama protokolu, mesela e-posta ....Üst seviye uygulama protokollerinin gereksinim duyduğu TCP gibi bir protokol katmanı ...IP katmanı. Gönderilen bilginin istenilen adrese yollanmasını sağlar.

...Belirli bir fiziksel ortamı sağlayan protokol katmanı. Örneğin Ethernet, seri hat, X.25 vs.

İnternet birbirine geçiş yolları (gateway) ile bağlanmış çok sayıdaki bağımsız bilgisayar ağlarından oluşur ve buna ‘catenet model’ adi verilir. Kullanıcı bu ağlar üzerinde yer alan herhangi bir bilgisayara ulaşmak isteyebilir. Bu işlem esnasında kullanıcı farkına varmadan bilgiler, düzinelerce ağ üzerinden geçiş yapıp varış yerine ulaşırlar. Bu kadar işlem esnasında kullanıcının bilmesi gereken tek şey ulaşmak istediği noktadaki bilgisayarın ‘Internet adresi’ dir. Bu adres toplam 32 bit uzunluğunda bir sayıdır. Fakat bu sayı 8 bitlik 4 ayrı ondalık sayı şeklinde kullanılır (144.122.199.20 gibi). Bu 8 bitlik gruplara ‘octet’ ismi de verilir. Bu adres yapısı genelde karşıdaki sistem hakkında bilgi de verir. Mesela 144.122 ODTU için verilmiş bir numaradır. ODTU üçüncü octet’i kampüs içindeki birimlere dağıtmıştır. Örneğin, 144.122.199 bilgisayar merkezinde bulunan bir Ethernet ağda kullanılan bir adrestir. Son octet ise bu Ethernete 254 tane bilgisayar bağlanmasına izin verir (0 ve 255 bilgisayar adreslemesinde kullanılmayan özel amaçlı adresler olduğu için 254 bilgisayar adreslenebilir). IP bağlantısız “connectionless” ağ teknolojisini kullanmaktadır ve bilgi “datagramlar” (TCP/IP temel bilgi birim miktarı) dizisi halinde bir noktadan diğerine iletilir. Büyük bir bilgi grubunun (büyük bir dosya veya e-posta gibi) parçaları olan “datagram” ağ üzerinde tek başına yol alır. Mesela 15000 octet’lik bir kütük pek çok ağ tarafından bir kere de iletilemeyecek kadar büyük olduğu için protokoller bunu 30 adet 500 octetlik datagramlara böler. Her datagram ağ üzerinden tek tek yollanır ve bunlar karşı tarafta yine 15000 octetlik bir kütük olarak birleştirilir. Doğal olarak önce yola çıkan bir datagram kendisinden sonra yola çıkan bir datagramdan sonra karşıya varabilir veya ağ üzerinde oluşan bir hatadan dolayı bazı datagramlar yolda kaybolabilir. Kaybolan veya yanlış sırada ulaşan datagramların sıralanması veya hatalı gelenlerin yeniden alınması hep üst seviye protokollerce yapılır. Bu arada “paket” ve “datagram” kavramlarına bir açıklama getirmek yararlı olabilir. TCP/IP ile ilgili kavramlarda “datagram” daha doğru bir terminolojidir. Zira datagram TCP/IP’de iletişim için kullanılan birim bilgi miktarıdır. Paket ise fiziksel ortamdan (Ethernet, X.25 vs.) ortama değişen bir büyüklüktür. Mesela X.25 ortamında datagramlar 128 byte’lık paketlere dönüştürülüp fiziksel ortamda böyle taşınırlar ve bu işlemle IP seviyesi hiç ilgilenmez. Dolayısıyla bir IP datagramı X.25 ortamında birden çok paketler halinde taşınmış olur. TCP/IP protokoller kümesidir. Her biri değişik işler yapan bir yığın protokolden oluşur.

TCP/ IP kurulan bir bilgisayar ağında bilgisayarı üç parametre ile tanımlarız.

1. Bilgisayar İsmi : Kullanıcı tarafından işletim sistemi kurulurken bilgisayara verilen addır.

2. IP Adresi : 4 bölümden oluşan adrestir xxx.xxx.xxx.xxx her bölüm 0-255 arasında değer alabilir.

3. Mac Adresi: bilgisayar ağ kartlarının ya da ağ cihazlarının içine değiştirilemez bir şekilde yerleştirilmiş bulunan bir adrestir. 0020AFF8E771 örneğinde olduğu gibi 16 lık düzende (hexadecimal) rakamlardan oluşur. Mac adresi yerine donanım adresleri ya da fiziksel adreste kullanılabilir.

Ağ üzerinde iletişimler aslında Mac adresleri ile gerçekleşir. Çünkü IP adresleri TCP/IP protokolüne özeldir. Başka protokolde , örneğin , Novell’in kullandığı IPX/SPX protokolünde IP adresi diye birşey yoktur. Bütün protokollerde değişmeyen tek şey MAC adresidir.

Her protokol kendine göre bir adresleme şeması kullanır ama bu şemalarda yer alan adreslerin dönüp dolaşıp en altta MAC adresine çevrilmesi gerekir.

TCP/IP’ nin Yapısı TCP/IP Katmanları: TCP/IP protokol kümesinin sahip olduğu mimari uygulama programlarının bulunduğu katman sayılmaz ise 4 katmanlıdır.En üstte uygulama programları vardır, altında ise iletişim işini yapan programlar bulunur.

Uygulama katmanın altında sırasıyla ulaşım, yönlendirme ve fiziksel katmanlar vardır. Ulaşım katmanında TCP ve UDP protocolleri, yönlendirme katmanında IP ve ICMP protokolleri tanımlıdır. Her katmanda birçok protokol vardır; ancak uygulama programları tarafından istenen bir iş yerine getirilirken, her katmandaki protokollerden yalnızca biri kullanılır.

Uygulama Katmanı Programları: Uygulama katmanı için tanımlı olan STMP,TELNET… gibi protokoller bir üstünde bulunan programlara hizmet verir. Bunlar, kullanıcının doğrudan etkileşimde bulunduğu veya bilgisayar kaynaklarını başka kullanıcılara erişme olanağı sağlayan programlardır.

STMP(Simple Mail Transport Protocol): Ağ içindeki kullanıcılar arasındaki elektronik mektup alış verişini düzenler.

SNMP(Simple Network Management Protokol): Ağ içinde bulunan yönlendirici, anahtar ve HUB gibi cihazların yönetimi için kullanılır. SNMP desteği olan ağ cihazları SNMP mesaj alış verişleriyle uzaktan yönetilebilir. Bunun için cihazlarda SNMP (agent) olmalıdır.

TELNET: Bir sistem üzerindeki başka bir sisteme bağlanarak, sanki onun terminalindeymiş gibi bağlandığı sistemi kullanmasını sağlar.

FTP (File Transfer Protocol): Bir Bilgisayardan başka bir bilgisayara dosya aktarımı için kullanılan temel protokoldür.

FSP(File Send Protocol): Bu protokol FTP ‘ye alternatif olarak geliştirilmiş. Tek üstün özelliği, bir dosya transfer edilirken herhangi bir sorun olur da hat kesilirse yeni bağlantıda dosyanın yarım kaldığı yerden alış- verişe devam edilmesine olanak vermesi. Ancak hat hızları arttığından FSP’ye çok fazla rağbet olmamamış. FTP daha çok kullnılmıştır.

NNTP (Netwok News Transpor Protocol): USENET postalama hizmetinin kullanımını sağlar.

Ulaşım Katmanı Protokolü: TCP ve UDP ulaşım katmanı protokolleri, bir üst katmandan gelen veriyi paketleyip bir alt katmana verirler,. Eğer veri bir seferde gönderilemeyecek kadar uzunsa, alt katmana verilmeden önce parçalara ayrılır (segment) ve her birine bir sıra numarası verilir.Genellikle TCP kullanılır, Sorgu amaçlı olarak da UDP kullanılır.

TCP(Transmission Control Protocol): Görevleri şunlardır; Bir üst katmandan gelen verinin uygun uzunlukta parçalara bölünmesi; Herbir parçaya, alıcı kısmında aynı biçimde sıraya koyabilmesi amacıyla sıra numarası verilmesi; Kaybolan veya bozuk gelen parçaları tekrarlaması; TCP kendisine atanmış olan bu görevleri yapabilmek amacıyla, ulaşım katmanında veri parçalarının önüne başlık bilgisi ekler. Başlık bilgisi ve veri parçası, ikisi birlikte TCP segmenti olarak anılır. Bir alt katmana örneğin, IP katmanına bu TCP segmenti gönderilir; oradan da bu segmente IP başlığı eklenerek alıcıya gönderilir.

UDP (User Datagram Protocol): UDP’nin farkı sorgulama ve sınama amaçlı, küçük boyutlu verinin aktarılması için olmasıdır; veri küçük boyutlu olduğu için parçalara gerek duyulmaz. UDP, TCP’den kısadır. Fakat, bir kaynak ve hedef adrese sahiptir.

Yönlendirme Katmanı Protokolleri: Bir üst katmandan gelen segmentleri alıcıya, uygun yoldan ve hatasız ulaşımla yükümlüdür.

IP(Internet Protokol): Bir datagramın hangi üst katmana katmana ait olduğunu belirler. Alıcı IP bu alana bakarak paketi bir üstte bulunan protokollerden hangisine ileteceğini anlar.

ICMP (Internet Control Message Protokol): ICMP kontrol amaçlı bir protokoldür; genel olarak sistemler arası kontrol mesajları IP yerine ICMP üzerinden aktarılır. ICMP, IP aynı düzeyde olmasına karşın aslında kendiside IP’yi kullanır. ICMP mesajları IP üzerinden gönderilir.

TCP/IP Ağ Çalışma Temelleri:

TCP/IP’nin öncelikli fonksiyonu bir noktadan-noktaya iletişim mekanizması sağlamaktır. Bir makine üzerindeki bir süreç diğer bir makine üzerindeki başka bir süreçle ile haberleşir. Bu İletişim iki veri akımı olarak görünür. Akımdan biri bir işlemden diğerine veri taşırken, diğeri ters yönde veri taşır. Süreçlerin her biri normal koşullarda diğeri tarafından yazılan veriyi okuyabilir, alınan veri gönderilen veri ile aynı sıradadır. Bir noktadan noktaya iletişim sistemi desteklemek için, her bir düğüm bir telefon numarasına benzeyen tek bir adrese ihtiyaç duyar. Bu adres bir 32 bit ikili sayı biçimindedir. Genel olarak, insanlar uzun ikili sayılarla başa çıkamadıklarından bu adresler her biri 0 ile 255 arasında olan dört onluk sayı ile gösterilir. Bu geliştirmede daha doğal adların kullanıldığı mekanizmalara uyarlanmıştır. IP Adresi

Dört ayrı onlu sayı halinde gösterimi

“helpful.com” bölgesi için ad sunucu veri tabanındaki kayıt

Adrese karşılık uygun bir ad sağlama

Barney.helpful.com

TCP/IP de kullanılan adresleme formatlarının karşılaştırılması Adres Verilirken Yapılan Düzenlemeler: Adres tekrarı olmaması için ağlara verilen adreslerin sınıflandırılıp verilmesi düşünülmüştür. Ağların hepsinin büyüklükleri aynı değildir. Çok büyük bir ağ adres talep ederken 10-15 bilgisayardan oluşan bir ağ da adres istemektedir. Onun içinde adresler sınıflanmıştır, A,B ve C sınıfı adresler oluşturulmuştur.Bir ağın hangi sınıfta olduğunu anlamak için örnek verdiğimiz numaralardaki ilk üç basamaklı sayıya bakılır. A sınıfı adresler: İlk üç basamak 0 ile 126 arasındadır.

B sınıfı adresler: İlk üç basamak 128 ile 191 arasındadır.

C sınıfı adresler: İlk üç basamak 192 ile 223 arasındadır.

Ağ Layer’ ı bilgisayarda bulunan ağ kartını, kabloları vb şeyleri gösteriyor. Veri paketlerinin ağa iletilmesinden ve ağdan çekilmesinden bu layer sorumlu.

IP Layerında IP’ye göre düzenlenmiş veri paketlerini görüyoruz. İletim layerından gelen veriler burada internet paketleri haline getiriliyor. Paketlerin yönlendirilmesi ile ilgili işler burada yapılıyor. Burada 4 protokol bulunuyor.

ICMP: Kontrol mesajları gönderip paketlerin gidip , gitmediği bilgisini alır. PING komutu bu protokolü kullanarak karşı bilgisayarın TCP/IP konfügürasyonu bakımından ayakta olup olamadığını anlar.

ICMP Multicast gruplarını belirtmek için kullanılır. Bu ağda mesajlar 3 şekilde gönderilir. Mesaj ya tüm makinalara (Broadcast) ya bir gruba(multicast) ya da bir makinaya (direct) gönderilebilir.

IP: paketleri adresleme ve yönlendirme işleri yapar.

İletim layerında ise iletişim için oturumlar düzenlenir. İki seçenek söz konusudur.

TCP: Bağlantılı ve güvenilir bir iletişim sağlar. Bağlantılı mantıksal bir bağlantıdır. İki bilgisayarın iletişim kurmaları için anlaşmaları demektir.TCP’ ye uygun olarak gönderilen paketler için bir onay mesajı beklenir. Belli bir süre içinde onay mesajı gelmezse paket tekrar gönderilir.Bu da iletimin güvenli olmasını sağlar.

UDP: Bağlantısız ve güvenilir değildir. Neden kullanıyoruz öyleyse ? İletim için karşı tarafla anlaşma gerekmiyorsa ve kontrol gerekmiyorsa kullanılır. Bu protokol ile daha hızlı veri iletişimi sağlanır.

Uygulama layer’i ağ üzerinden iş yapacak uygulamaların bulunduğu layer’dır. FTP,DNS,WINS,HTTP,GOPHER:...

İçinde ağ işlevi olan uygulama geliştirmek için iki API’ miz var. API uygulama geliştirme arabirimi anlamına geliyor. Program yazarken kullanılacak fonksiyonlar uyulacak kurallar demektir. Örneğin program yazmak için win95 ve WinNt ortamlarında çalışabilecek 32 bitlik program oluşturunuz.

İnternet üzerinde ağ uygulamaları için Microsoft ve IBM in birlikte geliştirdiği NETBIOS API ‘ si ya da internet ortamındaki standart API olan Sockets ‘ in windows uyarlaması , Windows Sockets kullanılır. Bir programı NETBIOS API si ile yazarsanız microsoft işletim sistemleri altında çalışır internet ortamında çalışmaz.Uygulama Windows Sockets API ‘ sine uyumlu yazılırsa her iki ortamda da çalışır. Sockets uyumlu uygulamaya örnek PING programı verilebilir. Netbios uyumlu uygulamaya örnek ise NET komutu verilebilir. WINDOWS SOCKETS TCP/IP ortamında uygulama geliştirmek için kullanılan API lerden biriside sockets’ dir. Bu uygulama 3 şey ile tanımlanır:

1. IP adresi 2. Servis tipi(UDP,TCP) 3. Kullanılan port Port numarası birkaç uygulama TCP yi birkaç uygulama UDP yi kullanırken uygulamalara verilen numaradır. 0- 65535 arasında sayı alabilir.1 ile 1024 arasındakiler iyi bilinenlerdir. Bu port numaraları internette standart servislerde kullanılır. Örneğin DNS 53 nolu portu , FTP serviside 21 nolu portu kullanırlar.

Echo,discard,systat , daytime ... servisler aynı port numaralarını kullanıyorlar. Ama bunların servisleri farklı. (TCP,UDP gibi) TCP/IP protokolünde uygun olarak yazılan diğer protokollerinde birer port numarası kullanması gerekir.

Çalışma şekli şu şekilde oluyor . Bir başka bilgisayarda bulunan program ile iletişime geçmek isteyen program soket yaratır ve iletişim süresince bu soketi kullanır.

TCP PROTOKOLÜ TCP(Transmission Control Protocol), IP gibi şu problemleri çözmek için çok bahsedilen bir protokoldür. Birine bir kitap göndermek isteyip de posta ofisinin sadece mektup kabul ettiği bir ortamda ne olurdu?Neler yapılabilirdi?Kitabın her sayfasını ayırıp zarflara bölerdin ve bir posta kutusuna atardın. Alıcı tüm sayfaların ulaştığından emin olmalıdır ve onları doğru sırada yapıştırır. Bu, TCP’nin ne yaptığıdır. TCP, göndermek istediğiniz bilgiyi alır ve onu parçalara böler. Her parçayı numaralandırır ve böylece alış işlemleri kontrol edilebilir, veri düzgün bir sırada geri dönebilir. Geliş sırasına göre bu numaralar ağı geçerler. Verinizin bir parçası bir TCP zarfına yerleştirilir, TCP zarfının içerisine bir IP yerleştirilir ve ağa verilir. Öncelikle içinde bir IP zarfı olan bir şeye sahip olun ki network onu taşısın. Alış kısmında bir TCP yazılım paketi zarfları biriktirir, verileri çıkarır ve onu düzgünce sıralar. Eğer bazı zarflar eksikse göndericiye bunu sorar ve onları tekrar transfer eder. Öncelikle alıcı bütün bilgilerin doğru sıralanışına sahip olmalıdır. O veriyi hangi uygulama programı kullanıyorsa onun seviyesine geçirir.

Bu, gerçekte TCP’ nin oldukça ütopik yanıdır. Gerçek hayatta paketler kaybolmakla kalmaz aynı zamanda ulaşma esnasında telefon hatlarındaki sorunlar yüzünden değişebilir de. TCP aynı zamanda bu problemlere sahiptir. Veriyi zarfa koyduğu gibi bir toplama(checksum) de yapar. Kontrol, pakette hata olup olmadığını kontrol eden bir numaradır. Paket ulaştığı zaman bir karşılaştırma işlemi yapılır eğer gönderilen ile alınan eşleşmezse transfer işleminde bir hata oluşur. Hatalı paketleri TCP atar ve bir daha gönderilmesini ister. IP’nin görevi ham verileri-yani paketleri- bir yerden bir yere göndermektir. TCP’ nin görevi ise akışı denetlemek ve verilerin doğruluğunu kontrol etmektir.

Bağlantılı ve güvenilir iletişim sağlar . Bağlantılı olması bilgisayarların iletişime geçmeden önce aralarında oturum açılması sırasında kendi iletişim parametrelerini birbirlerine göndermeleridir. İletişim sırasında bu parametrelere göre hareket ediliyor.

Güvenilir olması da bilginin karşı tarafa ulaştığından emin olmaktır. Bunun için ACK ,acknowledge onay mesajının bize gelmesini sağlıyor. Eğer belli bir sürede mesajı alabilirsek bizden çıkan bilgi karşı tarafın eline geçmiş oluyor alamazsak gönderilen bilginin başına birşey geldi demektir bilgi tekrar gönderiliyor.

Bu veri iletişim performansını düşürüyor ama güvenli bir şekilde hedefe ulaşmasını sağlıyor.

TCP/IP protokolünde kritik işler yapan protokoller ve servisler verilerini TCP ile iletirler. Örneğin 21 nolu portu kullanan FTP , 23 nolu portu kullanan telnet ve 53 nolu portu kullanan DNS.

TCP iletişimini Network Monitör programı ile gözlediğimizde ilkin 3 veri çerçevesinin ( frame) gidip geldiğini görüyoruz. Bu 3 verinin amacı veri paketinin ( bu paketlere TCP de segment deniyor)geliş ve gidişi senkronize etmek , karşı tarafa tampon bellek miktarı hakkında bilgi vermek ve TCP bağlantısını kurmaktır.

Bu 3 çerçeve ile TCP bağlantısı açıldıktan sonra dosya listesinin aktarımı, dosyanın listeden seçilip aktarımı için Netbios oturumu açılıyor hemen ardından da SMB oturumu açılıyor(server message block). SMB microsoft ağlarında bilgisayarlar arası kaynak paylaşımı için kullanılıyor.

TCP iletişiminde iletilmek istenen veriler segmentlere ayrılır , her segmente sıra numarası verilir . Gönderici bilgisayar , segmentleri yani çerçeveleri teker teker gönderip bunların herbirisi için onay bekler . Bunun yerine belli sayıda topluca göndeririz. Örneğin 10 ar 10 ar.Bu belli sayıya pencere denir.

Alıcı bilgisayar da çerçeveler kendisine ulaştıkça bunları kendi tampon belleğine yerleştirir.İki ardışık çerçeve tampon belleğe yerleşince alıcı bilgisayar aldığı en son çerçeve için mesaj gönderir.

Örneğin gönderici 45 adet segment tutuyor pencere büyüklüğü 10 olsun. Bu çerçevelerin 10 ar 10 ar gönderileceği anlamına geliyor. İlk 10 çerçeve gönderildi onay geldi. 17. çerçevenin başına birşey geldi. Bu durumda en son 16. çerçeve için mesaj gider.Veri iletimi tekrarlanacaktır. Ama çerçeveler teker teker gönderilmediği için 17. çerçeveden başlamak üzere 10 çerçeve gönderir. Bu sefer 1-10-20... den oluşan pencere 17-27-37... şekline dönüşür.Bu yönteme kayan pencereler denir. TCP iki kısımdan oluşur. Başlık (header) ve veri (data) kısmı. Başlık kısmı şu alanlardan oluşur.

Kaynak Portu (source port): Gönderilen bilgisayarın TCP portu

Hedef Portu( destination port ) : Alıcı bilgisayarın TCP portu

Sıra Numarası ( sequence number ) :Segmentlere verilen numara

Onay Numarası( Acknowledgement number)

Veri Uzunluğu ( Data lenght ): TCP segmentinin uzunluğu

Rezerve ( reserved) :Gelecekte kullanılmak üzere rezerve edilmiş

Bayraklar ( Flags) : Segmentin içeriğine dair bilgi

Pencere (window): TCP penceresinde ne kadar yer kalmış olduğunu gösterir.

Kontrol Toplamı (checksum): Başlık kısmının bozulup bozulmadığını gösteren kontrol kısmı

Acil Veri Göstergesi (Urgient pointer) : Bayrak kısmında gösterilen acil bir verinin iletilmek istediğini gösterir.

IP ADRESLEME Bir kablo veriyi bir yerden başka bir yere taşıyabilir. Bununla beraber biliyoruz ki internet dünyanın çoğu yerine dağılmış ve farklı yerlerdeki veriyi alabilir. Bunu nasıl yapar?

İnternetin farklı parçaları ağları birbirine bağlayan yönlendirici(router) adı verilen bilgisayar seti tarafından birleştirilmiştir. Bu ağlar bazen ethernet, bazen token rings ve bazen de telefon hatlarıdır.

Telefon hatları ve ethernetler karşılıklı değiş tokuşu sağlarlar ve posta servislerini planlarlar. Bu onların maili bir yerden başka bir yere taşımaları anlamına gelir. Yönlendiriciler gönderimin alt istasyonlarıdır, onlar verinin(paketlerin) nasıl yönleneceği hakkında bir posta istasyonunun mektup içeren zarflarını yönlendirdiği gibi karar verilmesini sağlarlar. Her alt istasyon veya yönlendiricinin diğerlerinin her biriyle bağlantısı yoktur. Eğer bir mektubu Dixilville Notch, New Hampshire’da zarflayıp Bonville, California’ya göndermek istersen, posta ofisi New Hampshire’dan California’ya götürmek için bir uçak ayarlamaz. Yerel posta ofisi mektubu bir alt istasyona, alt istasyon başka bir alt istasyona gönderir ve hedefe ulaşana kadar bu böyle devam eder. Yani her istasyon sadece hangi bağlantıya ulaşabileceğine ve hangisinin hedefine yaklaşmak için en iyi yol olduğunu bilme ihtiyacı duyar. Benzer şekilde internette bir yönlendirici verinizin nereye gideceğine bakar ve onu nereye göndereceğine karar verir. Hangi kanalın en iyi olacağına karar verir ve onu kullanır. Ağ verinizin nereye gittiğini nasıl bilir? Bir mektup göndermek isterseniz mektubu yazıp direk posta kutusuna atamazsınız. Kağıdı bir zarfa koyma, zarfın üstüne adres yazma ve onu pullamaya gereksiniminiz vardır.

Posta ofisinde olduğu gibi ağ da nasıl çalıştığıyla ilgili tanımları içeren kurallara sahiptir. İnternet işlemlerinin nasıl yönetildiğiyle ilgili kurallardan biri de IP(Internet Protocol)’dir. IP adreslemeye veya veri ulaştığında yönlendiricinin ne yapmasını bilmesinden emin olmaya dikkat eder. Posta ofisinin analojisiyle internet protokolünün çalışmasını saptamak bir zarfın işleyişine benzer. IP adresi 32 bitlik bir numaradır. TCP/IP protokolünü kullanan her bilgisayarın IP adresi olmalıdır. IP adresi hem bilgisayarın dahil olduğu ağı hem de o bilgisayarın ağ içerisindeki adresini belirler.

Elimizde adresleme için kullanabileceğimiz 32 bit varsa toplam 2 üzeri 32 den 4 milyon bilgisayarı adresleyebiliriz.

IP adresini oluşturan 32bit, kolayca okunabilmesini sağlamak için 8 bitlik dört gruba ayrılmıştır bu grupların her birine “octet” denir.Örnek bir IP adresi şu şekilde olabilir:

10000011 01101011 00000001 00001100 Yukarıdaki adres her ne kadar 4 oktede ayrılmışsa da okunması zordur; çünkü bizler rakamları 10’luk düzende okuruz. Bunun için her bir okteti 10’luk düzene çevirip oktetlerin arasına nokta koyuyoruz. Örneğin yukarıdaki adres 131.107.1.12 şeklinde yazılır.

IP numarası yetkili kuruluşlar tarafından verilir. Bunların en üst düzeyi NIC(Network Information Center)’tir. Türkiye’de bu işle ilgili olarak ODTÜ ve TÜBİTAK’ın ortaklaşa yürüttükleri TR-NET grubu çalışmaktadır.

İnternetin yapısı gereği Türkiye’deki internete bağlanacak tüm bilgisayarların hepsinin TÜBİTAK’a bağlanması gerekmemektedir. Örneğin Ankara’da ODTÜ, TÜBİTAK’a zaten bağlı olduğundan ODTÜ’ye bağlanacak kuruluşlar da doğrudan internete erişim olanağı bulurlar.

YÖNLENDİRME:

Bu bölümde farklı coğrafi noktalarda yer alan TCP/IP ağlarının birbirleri ile olan iletişiminin sağlanması için en önemli anahtar olan, yol bulma yani yönlendirme konusu açıklanacaktır.

Daha önceki açıklamalarımızda IP (Internet Protokol) katmanının datagram'ların (TCP/IP’de iletişim için kullanılan bilgi birim miktarı) varış noktasına ulaşmasını sağlamakla yükümlü olduğundan bahsettik. Fakat bu işlemin nasıl yapılacağının detaylarını incelemedik. Bir datagram'ın varış noktasına ulaştırılmasına 'yönlendirme' (routing) adı verilmektedir. Yönlendirmenin nasıl yapıldığını kavrayabilmek için IP'nin dayandığı modeli anlamak gereklidir. IP katmanı daima, bir sistemin bir ağa bağlı olduğunu varsayar. Ethernet tabanlı bir ağ üzerinde sadece karşı istasyonun Ethernet adresini bilmek yeterli olduğu için herşey çok kolaydır. Fakat datagram'lar farklı ağlar üzerindeki noktalara gönderilmek istendiğinde sorunlar başlar. Bir ağ üzerinden diğer ağ üzerine geçecek bilgi trafiğini kontrol etmek, onu yönlendirmek görevi genel olarak 'geçiş noktası aygıtlarına' (gateway) aittir. Internet üzerinde IP protokolü kullanan ağlarda bu işleri yerine getiren aygıtlara yönlendirici (router) adı verilir. Böyle bir görev üstlenen makine üzerinde birden fazla bilgisayar ağı bağlantısı yer alıp, farklı ağların bilgi trafikleri bu yolla birbirlerine iletilir. IP ağlarındaki yönlendirme tamamen varış noktası adresi temeline oturmaktadır. Örneğin ODTÜ'nün uluslararası Internet bağlantısını yapan yönlendirici 144.122.1.2 adresinde bulunmaktadır. Dolayısıyla 144.122.1 ağı üzerinde yer alan diğer sistemler 144.122.1.2 adresini yurt dışı adreslere ulaşmak için geçiş noktası olarak tanımak zorundadırlar. Benzer bir şekilde Bilgisayar Mühendisliği bölümünün kampus omurga ağına geçiş noktası olarak kullandığı bilgisayarın adresi de 144.122.71.1'dir. 144.122.71 ağı üzerinde bulunan bir bilgisayar, kampus içindeki başka bir bilgisayara ulaşmak için bu geçiş noktasından geçmek zorundadır. Bu ağ üzerinde bulunan bir bilgisayar datagram yollamak istediğinde öncelikle ulaşmak istediği adresin aynı ağ üzerinde olup olmadığına bakar, eğer varış noktası aynı ağ üzerinde ise bilgi doğrudan varış adresine yollanır. Eğer değilse, sistem varış noktasına ulaşmak için gerekli bilgileri araştırmaya başlar.

Burada 195.194.34.2 nolu bilgisayar ile 200.123.89.3 nolu bilgisayarın haberleşebilmesi için önce aynı ağda olup olmadıklarını subnet maskesi ile kontrol etmeleri gerekir. Bu bilgisayarlar aynı ağda olmadıkları için yönlendirici kullanmalıyız.

Yönlendiricinin iki bacağı vardır. TCP/IP protokol kümesi ağdaki her ucun ayrı bir IP adresinin olmasını şart koşuyor bu yüzden yönlendiricinin bacaklarına da IP adresi koyuyoruz. Yönlendiricinin bacaklarından adres verirken o bacak hangi ağa bağlıysa o ağa uygun bir adres veririz. Burada da ağdaki ilk adresi veriyoruz. İki ağında yönlendiriciden haberdar olması için TCP/IP konfigürasyonu kısmında “default gateway” parametresi yani kendi ağımızda olmayan adrese ulaşmamız gerekirse ilişki kuracağımız yönlendirici gösteriyor. 195.194.34.0 ağında bulunuyorsak bilgisayarların hepsinde default gateway olarak 195.194.34.1 adresini veriyoruz. Bu adres yönlendiricinin bize bakan bacağını gösteriyor.

Yönlendirici olarak router adı atılda satılan cihazlar ya da WinNT bilgisayarı (server ya da workstation) yönlendirici olarak kullanılır.

Yönlendirme Protokolleri Yukarıda da açıklandığı gibi yönlendirme, bir bilgisayar ağı üzerinde yer alan bir bilgisayarın aynı ya da farklı bir ağ üzerinde yer alan başka bir bilgisayara nasıl ulaşacağına karar verirken kullanılan yöntemdir. Bu sayede herhangi iki farklı noktada yer alan kullanıcılar birbirleri ile bilgisayar kullanarak haberleşebilmektedir. Dolayısıyla yönlendirmeyi bir nevi yapıştırıcı gibi düşünebiliriz. İletişimin en önemli noktası olmasından dolayı yeni bilgisayar ağı kuruluşlarında en önemli sorunlardan birisi yanlış yapılan yönlendirme olmaktadır. Bu noktada yönlendirme ve yönlendirme protokolü arasındaki farkı açıklamak ileride oluşabilecek yanlış anlamaları önlemek açısından yararlı olacaktır. Bir bilgisayar ağına bağlı her sistem bilgiyi bir noktadan bir diğerine yönlendirebilir ama her sistem üzerinde yönlendirme protokolü çalışmaz. Yönlendirme, bir yönlendirme tablosundaki bilgiye göre bilgi paketlerinin geçirilmesidir. Yönlendirme protokolü ise bu tabloların oluşturulmasında bilgi değişimini sağlayan programlardır. Basit bir bilgisayar ağında bir yönlendirme protokolü çalışmadan, sabit tablolar kullanarak iletişim sağlanabilir. Temel olarak 3 yönlendirme yöntemi vardır (Aşağıda verilecek olan komutlar UNIX işletim sistemlerinde bulunmakta olup diğer sistemlerde farklı komutlar kullanılabilir):

Minimum Yönlendirme: Bir bilgisayar ağı başka bir bilgisayar ağına bağlı olmaksızın tek başına çalışıyorsa minimum yönlendirme ile ağ üzerindeki iletişimi sağlayabiliriz. (Bu yönlendirme genelde sadece <<if config>> komutu ile yapılır) Sabit Yönlendirme: Kurulu bir bilgisayar ağının dış dünyaya bir ya da birkaç çıkışı varsa sabit yönlendirmeyi kullanabilir. (Bu yönlendirme genelde route komutu ile yapılır). Gerekli komut kullanılarak ağın dış dünyaya çıkan trafiği çıkış noktasına yönlendirilmiş olur.

Dinamik Yönlendirme: Ağın dış dünya ile olan iletişimi birden fazla noktadan yapılıyorsa, yönlendirme protokolü ile dinamik olarak bir yönlendirme tablosu tutulur ve yönlendirme protokolleri birbirleri ile gerekli bilgi alışverişini yaparak en uygun çıkışı kullanırlar. Böylece ağ yöneticisinin elle müdahalesi gerekmeksizin en uygun yolu bu protokoller bulurlar. Dolayısıyla bir çıkış noktasında meydana gelen bir sorunda tüm trafik otomatik olarak diğerine yönlendirilebilir.

Bu yönlendirme yöntemlerini biraz daha detayları ile örnekler vererek inceleyelim.

(Şekil 3.1) Minimum yönlendirme

Minimum Yönlendirme Tablosu Aşağıdaki şekilde görülen ağ üzerinde

\# ifconfig le0 144.122.99.2 netmask 255.255.255.0 broadcast 144.122.99.255

komutu kullanılarak arayüzünün ağ bağlantısı yapılmış olan bir bilgisayarın yönlendirme tablosunun içeriğine bakarsak

% netstat -rn

Routing Tables Destination Gateway Flags Refcnt Use Interface 127.0.0.1 127.0.0.1 UH 1 132 lo0 144.122.99.0 144.122.99.2 U 26 49041 le0 İlk satırdaki 127.0.0.1 loopback adres olarak bilinen lokal bilgisayarın kendisini tanımlayan ve Internet protokolünü çalıştıran her bilgisayarda bulunan standart bir adrestir. İkinci satırda ise 144.122.99.0 ağına, ethernet le 0 arayüzü üzerinden gidileceğini belirtiyor. 144.122.99.2 ise uzaktaki (remote) bir geçiş noktası (gateway) adresi değil le 0 arayüzünün kendi adresidir. Flags alanlarına bakacak olursak her iki satırda da bulunan U (up), her ikisinin de kullanıma hazır olduğunu gösterir. Her iki satırda da Flags alanında G (Gateway) işareti yoktur zira her iki arayüze aradaki bir geçiş kapısı (gateway) üzerinden ulaşılmamaktadır. Loopback yönlendirme tanımının bulunduğu satırdaki H (Host) işareti bu yönlendirme ile sadece bir bilgisayara (yani kendisine) ulaşılabileceğini tanımlamaktadır. Bu satır bilindiği gibi her yönlendirme tablosunda bulunmaktadır. Bu yönlendirme tablosu görüldüğü gibi sadece 144.122.99.0 ağı ile ilgili yönlendirme bilgisine sahiptir. Dolayısıyla sadece bu ağ üzerinde yer alan bilgisayarlar birbirleri ile iletişime geçebilmektedirler. Bu yönlendirme tablosu oluştuktan sonra herhangi bir problem olup olmadığının testi ping komutu ile kolayca yapılabilir. Önce bu ağ üzerinde yer alan bir bilgisayarı ping komutu ile kontrol edelim:

% ping 144.122.99.3

PING 144.122.99.3: 56 data bytes 64 bytes from 144.122.99.3: icmp\_seq=0, time=11, ms 64 bytes from 144.122.99.3: icmp\_seq=1, time=11, ms

C ----144.122.99.3 PING statistics---- 2 packets transmitted, 2 packets received, 0% packet loss round-trip (ms) min/avg/max =10/10/11 Görüldüğü gibi 144.122.99.3 ile olan iletişimin başarılı olduğu test edilmiş oldu. Bunun yanında aynı ağ üzerinde bulunmayan bir adrese ulaşmak istediğimizde nasıl bir sonuçla karşılaşacağımızı test etmek istersek :

% ping 26.40.0.17

sendto: Network is unreachable Gelen cevaptan da anlaşılacağı gibi, ulaşmak istediğimiz bilgisayara ait yönlendirme bilgisine sahip olmadığı için, bilgisayarımız datagram ları varış noktasına iletemediğini ve o noktaya ulaşılamaz olduğu mesajını veriyor. Eğer bilgisayar ağınızın dış dünya ile irtibatı yoksa ifconfig ile yaratılan tablo tüm ihtiyaçlarınızı karşılamaya yeterlidir. Ancak bir dış bağlantı varsa o zaman yönlendirme tablosunun daha fazla bilgiye ihtiyacı vardır. Sabit Yönlendirme Tablosu Yukarıda da gördüğümüz gibi minimum yönlendirme tablosu ile aynı ağ içindeki bilgisayarlara ulaşmak mümkündür. Başka ağlar üzerindeki bilgisayarlara ulaşmak için bunlarla ilgili bilgiler yönlendirme tablolarına girilmelidir. Yönlendirme tablosunu yaratmak için kullanılan yolların en popüleri route komutudur. route komutu ile yönlendirme tablosuna elle yeni yönlendirme bilgileri eklenip çıkartılabilir.

(Şekil 3.2) Sabit yönlendirme Örnek verecek olursak, yukarıdaki şekilde görülen 144.122.99.0 ağındaki bir bilgisayardan 144.122.71.0 ağına ulaşmak için şöyle bir tanım yeterlidir:

\# route add 144.122.71.0 144.122.99.1 1

add net 144.122.71.0: gateway 144.122.99.1 route komutundan sonraki 'add' argümanı yönlendirme tablosuna bir ek yapılacağını söylemektedir. Tablodan bir bilgi silineceği zaman 'add' yerine 'delete' kullanılarak bu silme işlemi yapılır. Aynı satırdaki üçüncü bilgi bu yönlendirme bilgisi ile ulaşılmak istenen adresi belirtmektedir. Ulaşılacak adres 4 farklı şekilde tanımlanabilir: a- bir IP adresi , b- /etc/networks dosyasındaki bir ağ ismi, c- /etc/hosts dosyasındaki bir bilgisayar ismi, d- default.

Eğer ulaşılmak istenen adres olarak default kullanılırsa aynı ağ üzerinde yer almayan her adrese burada tanımlanan geçiş yolu üzerinden ulaşılmaya çalışılır. Eğer bir ağın dış dünyaya çıkışı tek bir noktadan ise default olarak bu çıkış adresi tanımlanmalıdır.

Komut satırındaki dördüncü bilgi geçiş yolu adresidir. Bu adres ağın dış dünya ile iletişimini sağlayan geçiş kapısıdır. Son argüman ise yönlendirme metrik bilgisidir. Bu bilgi, sadece ROUTE bilgisinin eklenmesi durumunda kullanılır. Metrik bilgisi değerinin 0 olması durumunda yönlendirme bilgisinin lokal ağa ait olduğu şeklinde yorumlanır ve daha önce netstat komutunda gördüğümüz Flags alanındaki G (Gateway) işareti gözükmez. Ama eğer Metrik 0 değerinden büyükse bu o zaman bu yönlendirme bilgisinin dış dünyaya açılan geçiş yolunu tarif ettiği anlaşılır ve Flags alanına G işareti konulur. Sabit yönlendirme 0 ve 1 dışında bir Metrik değeri kullanmaz. Diğer Yönlendirme Protokolleri Bütün yönlendirme protokolleri temelde en iyi yönü ve yolu bulma işlevini yerine getirirler ve bu yönlendirme bilgisini ağ üzerinde dağıtırlar. Yönlendirme protokolleri iki temel gruba bölünebilirler: İnterior (ic) ve Exterior (dis). i-Interior (ic) Protokoller: Bu protokoller bağımsız bir bilgisayar ağı içinde kullanılırlar. TCP/IP terminolojisinde böyle bilgisayar ağı sistemlerine Otonom sistemler (AS) adı verilir. Otonom sistem içinde yönlendirme bilgisi, o ağın yöneticisi tarafından belirlenen bir iç yönlendirme protokolü ile dağıtılır. Bu amaçla kullanılabilecek değişik Interior (ic) protokoller mevcuttur.

HELLO en iyi yönü seçerken gecikme faktörünü kullanan bir protokoldür. Gecikme olarak çıkış noktasından varış noktasına gönderilen bir paketin çıkış noktasına ulaşana kadar geçen zaman süresi kabul edilir. Bu protokol çok yaygın olarak kullanılmamaktadır. NSFNET omurgası 56 Kbps hızında iken kullanılmış ve zaman içinde başka protokoller ile değiştirilmiştir.

Son zamanlarda yaygınlaşmaya başlayan bir diğer iç protokol de OSPF'dir (Open Shortest Path First). OSPF 'equal cost multipath routing' (eşit maliyetli çok yollu yönlendirme) mantığı ile çalışmakta ve çok büyük ağlarda kullanılmaktadır. OSPF aynı varış noktasına birden fazla yönlendirme bilgisini tutmaktadır. Ancak OSPF'in bugün için sadece özel yönlendirme cihazları üzerinde var olması ve henüz UNIX sistemlerin bir parçası haline gelmemesinden dolayı yaygın kullanıma geçilememektedir. RIP (Routing Information Protocol) bu protokoller içinde en çok kullanılanıdır. RIP'i popüler yapan sebeplerin başında bu protokolün UNIX sistemlerin bir parçası olması gelmektedir. RIP protokolü yönünü en düşük sıçrama sayısı-hop count (metrik) ile seçer. RIP 'hop count', bilginin varış noktasına ulaşana kadar geçeceği geçiş yolları sayısını gösterir. Dolayısıyla RIP en az geçiş yoluyla ulaşılabilecek yolu en iyi yol olarak seçer. Bu yaklaşımla yol seçme işlemine 'distance- vector algoritması' adı verilir. RIP protokolünün kabul edebileceği maksimum geçiş yolu (gateway) sayısı 15 ile sınırlıdır. Ulaşılmak istenen yön ile ilgili metrik 15'den büyükse, RIP o noktaya ulaşılamaz olduğunu varsayar ve ilgili yönlendirme bilgisini atar. Dolayısıyla RIP çok büyük Otonom Sistemler için uygun bir protokol değildir. Bunun yanında en kısa yol en iyi yoldur yöntemi de yavaş ve yüklü hatlar kullanılması durumunda doğru olmamaktadır. Çok kullanılan bir yönlendirme protokolü olmasından dolayı RIP protokolünün biraz daha detaylarına girelim. Daha önce de belirttiğimiz gibi RIP pek çok UNIX sisteminin bir parçası olarak gelmektedir. RIP bu işletim sisteminde bir yönlendirme deamon'u olarak çalışır. UNIX'deki bu deamon routed'dir. routed çalıştırıldığında yönlendirme tablosunu güncellemek (update) için hemen bir istek paketi yollar ve ardından gelecek olan cevapları dinlemeye başlar. RIP çalıştıran başka bir sistem bu isteği aldığında kendi yönlendirme tablosu ile ilgili güncel bilgileri cevap olarak yollar. Bu paket adresler ve bu adreslerle ilgili metrik bilgilerini içerir. Bunun yanında güncelleme paketleri sadece istek üzerine değil periyodik olarak yollanmaya başlanır. Routed bir güncelleme bilgisini aldığında gelen paket içindeki bilgiyi alır ve kendi tablolarını günceller. Gelen bilginin içinde yeni bir yönlendirme bilgisi varsa bunu da hemen tablolarına ekler. Gelen paket içindeki yönlendirme bilgileri arasında lokal tabloda bulunan bir adres için ikinci bir yol belirtiliyorsa bu durumda lokal tablodaki ve gelen güncelleme tablosundaki metrik bilgileri karşılaştırılır. RIP protokolü Metrik bilgisi düşük olan noktaya daha kolay ulaşılacağı varsayımı ile çalıştığı için tabloya bu değere sahip yöne ilişkin adres yerleştirilir. RIP tabloları tabii ki belli bir yerden sonra çok fazla büyüyeceği için bir şekilde kontrol altında tutulmalıdır. Bunun için iki yol mevcuttur. Birincisi, bir noktaya ulaşmak için gereken metrik 15'in üzerindeyse bu nokta ulaşılamaz kabul edilir ve tablodan çıkarılır. İkincisi, eğer bir geçiş noktası belli bir süre güncelleme bilgisi yollamazsa RIP o noktanın ölü olduğunu ve ulaşılamadığını varsayar. Genel olarak güncelleme cevabı bekleme suresi 30 saniye civarındadır. Bir UNIX sisteminde RIP protokolünü çalıştırmak için

\# routed

komutunun girilmesi yeterlidir. Genellikle komut hiç bir argüman verilmeden çalıştırılır. Fakat kullanılan sistem bir geçiş noktası değilse ve elindeki yönlendirme bilgisini sürekli yayınlaması gerekmiyorsa bu durumda komut -q opsiyonu ile çalıştırılabilir. Böylece sistem sadece yeni duyurulan yönlendirme bilgilerini dinleyip tablolarını güncelleyecek ancak kendisi bir duyuru yapmayacak dolayısıyla gereksiz trafik yaratılmayacaktır. ii-Exterior (dis) Protokoller: Otonom Sistemler arasında yönlendirme bilgisinin birbirleri arasında değiştirilmesi amacı ile kullanılır. Bu belli bir Otonom Sistem üzerinden hangi ağlara ulaşılabileceği bilgisini içerir. Bu protokoller içinde en popüler olanları EGP (Exterior Gateway Protocol) ve BGP'dir (Border Gateway Protocol). Bu dokuman içinde EGP ve BGP protokollerin detaylarına girilmeyecektir. BDE ADMİNİSTRATOR Denetim masasının en önemli elemanlarından biridir. Denetim masasındaki simgeyi tıkladığımızda aşağıdaki gibi pencere ekrana gelecektir. (bkz.resim-4) BDE Administrator veri tabanı ile ilgilidir. Kullanılacak veri tabanlarının ve bunlara sahip olan dosyaların ilişkilendirilmesinde ve birbirlerine bağlanmasında BDE Administrator' un önemi ve gerekliliği vardır.

BÖLGESEL AYARLAR Bölgesel ayarlar ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Bölgesel Ayarlar simgesine çift tıklayın...

Bölgesel ayarlar başta zamanı gösterme biçimi, para birimi ve sayıları ayırmak için kullanılan karakterlerin düzenlenmesini sağlar. Bu karakterler her ülkeye göre farklıdır. Özellikle uygulama programlarında karşılaşılan birçok sorun bu ayarlamaların yapılmamasından kaynaklanır. Bu pencere 5 katmandan oluşur.Bunlar Bölgesel Ayarlar, Sayı, Para Birimi, Saat, Tarih dir.

Bölgesel Ayarlar Katmanı:

Bu katmanda kullanılacak olan karakterlerin ve ayarların hangi ülke standartlarında olacağı belirlenir. Bunun için ekranda görülen combobox' tan istenilen seçenek işaretlenir.

Sayı Katmanı:

Bu katman, decimal(onlu) sayı ayracı(kuruşları göstermek için) kullanılır. Ayrıca sayıların basamaklarını ayırmak için (grouping character) kullanılan karakterlerin seçilmesini sağlar.

Para Birimi Katmanı:

Bu katman, para biriminin seçilmesini, para birimi simgesinin yeri, ondalık karakterinin simgesini basamak sayısı gibi değişiklikleri yapmamızı sağlar.

Saat Katmanı:

Bu katman, saat bilgisinin biçimi ve ayracının seçilmesini sağlar.

Tarih Katmanı:

Bu katman, Tarih bilgisinin biçimi ve ayracının seçilmesini sağlar.

ÇOKLU ORTAM Çoklu ortam ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Çoklu Ortam simgesine çift tıklayın...

Bu menüden istenilen aygıt ayarları yapılabilir.Bu menü 5 adet katmanı içermektedir. Bunlar; Ses, Video, Midi, CD Müziği, Aygıtlar' dır. Bu menü ile bilgisayara konulan ekstra donanım parçalarının özellikleri ayarlanabilir.

Ses Katmanı:

Bu menü zaten Çoklu Ortam simgesine tıklanıldığında aktif durumdadır. Bilgisayardan çıkacak ses özelliği ile bilgisayar kayıt edilebilecek ses özelliği bu menüden ayarlanabilir. Ayrıca bu menüde Gelişmiş Özellikler adlı bir buton daha vardır. Bu buton ile kayıttan çalınacak ses özelliğine ait donanım ayarlaması yapılabilinir.

İkinci Frame kutusunda ise kaydetme araçlarına ait ayar grubu bulunmaktadır. Burada bulunan combobox text kutucuğundan kaydedilecek sesin hangi aygıt yoluyla elde edileceği kararı verilir.

Video Katmanı:

Bu menüden uygulamaya koyacağımız "avi,dat,cdi...." uzantılı dosyaları göstereceğimiz ekranın boyutunu ayarlayabiliriz. Video gösterisi adlı Frame kutucuğunun içinde iki adet radyo butonu bulunmaktadır. Bunlar Pencere ve tam ekran seçenekleri- dir. Eğer Pencere seçeneği işaretli ise gösterilecek dosyanın boyut ayarlaması yapılmasına izin verilmektedir. Eğer tam ekran seçeneği işaretli ise gösterilecek dosyanın boyutu ekran boyutuna birebir olarak ayarlanmaktadır.

Midi Katmanı:

Bu menü ile bilgisayara yeni bir ses aygıtı bağlamamıza olanak sağlanır. Eğer yeni bir aygıt yükleyeceksek ve bunun kararını biz vereceksek o zaman Özel yapılandırma seçeneğini işaretlememiz gerekir. Daha sonra Yeni Gereç Ekle butonuna tıklayıp istediğimiz ses gerecini yüklememiz gerekmektedir.

CD Müziği Katmanı:

Bu katmanda kullanılacak olan CD sürücüsünün hangi sürücüye bağlı olduğu kullanıcıya gösterilir ve değişiklik yapılmasına imkan verilir. Ayrıca bu menüden CD müzik ses seviyesi de ayarlanabilinir.

Aygıtlar Katmanı:

Bu pencere ile çoklu ortam aygıtlarının bir listesi kullanıcıya bildirilir. Bu aygıtların bileşenleri de bu pencerede alt dizin olarak gösterilir. Bu sayede hangi aygıtın hangi bileşenleri olduğunu bilebiliriz. Eğer bu listeden istediğimiz bir aygıtı seçersek Özellikler butonu aktif duruma gelecektir.(Alt dizine sahip aygıtlarda bileşende seçilmelidir. )

Özellikler Butonu:

Bu buton ile seçili olan bileşen ile ilgili ayarlamalar yapılabilinir. Örneğin Ortam Denetim Aygıtlarından CD Ses Aygıtını seçmiş olalım. İşte bu anda özellikler butonu aktif hale gelecektir. Bu Özellikler butonuna tıklarsak aşağıdaki gibi bir pencere ekrana gelecektir. Burada seçenekler arasından bu bileşenin kullanılıp kullanılmayacağını yada bu bileşenin kaldırılmasını işaretleyebiliriz. İstenilen görev bu şekilde yerine getirilecektir.

FARE Fareyle ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Fare simgesine çift tıklayın...

Fare (mouse) ayarları öncelikle farenin tuşlarıyla ilgilidir. Windows 98' de farenin sol ve sağ olmak üzere iki düğmesini kullanırsınız. Asıl fare düğmesi sol düğmedir. İşlemlerin çoğunu bu düğmeye basarak yapabiliriz. Sağ düğme ise genellikle özel işlemlerin yerine getirilmesi için bir menünün açılmasını sağlar.

Denetim masasındaki Fare sembolüne tıklayınca yukarıdaki menü ekrana gelir.Bu menü 3 katmandan meydana gelir. Bunlar Düğmeler, İşaretçiler, Hareket katmanlarıdır.

Düğmeler Katmanı:

Bu katman zaten Fare menüsüne ilk girildiğinde aktif durumdadır. Burada kullanıcıya düğme yapılandırması adı altında iki seçenek sunulur. Bu seçeneğin faydası tabii ki mevcuttur. Örneğin "solak" bir kullanıcıysanız yada farenin sol ve sağ tuşu işlevlerini yer değiştirmek istiyorsanız burada sol elini kullanan seçeneğine tıklamanız gerekmekte. Bunun dışında farenin çift tıklatma hızı bu katmanda ayarlanabilmekte.

İşaretçiler Katmanı:

Bu katman Fare işaretçisine şekil ve boyut vermek amacıyla vardır. Windows 98' te farenin işaretleyicisi yada göstergesi değişik şekiller alabiliyor. Yani alıştığımız gösterge yerine daha ilginçlerini koymak mümkün. Üstelik bu göstergeler hareketli de olabiliyor. Bir işlemin bitmesini beklerken öylesine duran bir kum saati yerine dönüp duran bir kum saatine bakabiliriz. Düzen isimli kutudan istediğimiz fare göstergeleri düzenini seçebiliriz.Biz seçince buradaki fare göstergeleri değişecek.

Hareket Katmanı:

Bu katman Fare işaretçisinin hızını ayarlamamıza ve bu işaretçiye bir iz verebilmemize olanak sağlar. İşaretçi hızını Hızlı yazısına yaklaştırdıkça mouse' un hareket kabiliyeti artar. Aksi istikamete doğru ilerlersek de bu olay yavaşlar. İşaretçi izlerini göster seçeneğini işaretlersek de mouse' u her hareket ettirdiğimizde bir gölgenin oluştuğunu görürüz. Bu izin kalıcılığını da imleci kısa ve uzun yazılarına yaklaştırdığımızda ayarlayabiliriz.

GÖRÜNTÜ Görüntü ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Görüntü simgesine çift tıklayın...

Kontrol Panel aracılığıyla kullanılan görüntü kartı sürücüsünü ve özelliklerini değiştirerek ekrandaki görüntünün özelliklerini kontrol etmemizi sağlar. Bu ayarlar şu işlemleri kapsar:

\*\*\* Desenler(patterns) ve duvar kağıdı(wall paper) olmak üzere zemin ayarlaması.

\*\*\* Ekran koruyucu düzenlemeleri \*\*\* Font ve renkler olmak üzere görünümler \*\*\* Simge değiştirme \*\*\* Pixel ayarlama Denetim masasındaki Görüntü sembolüne tıklayınca yukarıdaki menü ekrana gelir.Bu menü 6 katmandan meydana gelir. Bunlar Arka Plan, Ekran Koruyucusu, Görünüm, Etkiler, Web, Ayarlar katmanlarıdır.

Arka Plan Katmanı:

Bu katman zaten Görüntü menüsüne ilk girildiğinde aktif durumdadır. Bu katmanda windows' umuzun ana görünüm penceresindeki (masaüstü) görüntüyü değiştirmemize, bir duvar kağıdı oluşturmamıza olanak sağlar. Bu konacak olan resimin ne şekilde monte edileceği de combobox bileşenindeki menüden seçilebilir.

Ekran Koruyucusu Katmanı:

Bu katman monitörün sağlığı için yapılmıştır. Tabii ki zevke de bağlıdır. Hareketsiz kalan bir monitör ekranı, monitörümüzün daha hızlı eskimesine yol açar. Bunun için ekran koruyucusuna ihtiyaç vardır. Ekran Koruyucusu menüsünden istediğimiz simüleyi kullanabiliriz. Ayrıca "monitörün enerji kazandıran özellikleri" adı altında ayar yapmamıza olanak sağlayan bir menü daha vardır.

Görünüm Katmanı:

Bu katman Windows ekranındaki her ileti kutusu barı ve her program çubuğu için renk vermemize olanak sağlar. Etkin pencerelere ve bunların başlıklarına istediğimiz rengi verebiliriz.

Etkiler Katmanı:

Etkiler ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Etkiler simgesine çift tıklayın...

Buradaki ayarlama masaüstü temaları üzerinedir. Masaüstü temalarına istediğimiz şekili burada bulunan mevcut resimlerden verebiliriz. Simge Değiştir butonu bu ayar içindir. Ayrıca görsel etkiler adı altında masaüstü temalarının fiili özellikleri ile ilgili ayarlar bulunmaktadır. Burada istediğimiz etkinliğin üzerine mouse yardımı ile işaret koymamız yeterlidir.

Web Katmanı:

Web ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Görüntü simgesinden Web simgesine tıklayın...

Buradaki ayarlama masaüstü temalarının web biçemi halinde gösterilmesine ve Klasör Seçenekleri ile klasör ayarlamalarında yardımcı olmak ile ilgilidir. Yeni bir web biçimini masaüstüne taşımamıza olanak sağlar veya bulunan biçemi kaldırmamızı sağlar.

Ayarlar Katmanı:

Ekran görüntüsü ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Görüntü simgesinden Ayarlar simgesine tıklayın...

Bu pencerede ekranda karşımıza çıkacak görüntünün renk dağılımını, bir birime düşen renk adedini(ayrıntıyı) ve ekran boyutunu ayarlayabiliriz.

GÜÇ YÖNETİMİ Güç yönetimi ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Güç Yönetimi simgesine çift tıklayın...

Windows 98, "yeşil" bilgisayar sistemlerini destekler. Bu amaçla ekranın ve sabit diskin kullanılmadığı zamanlarda elektrik tüketimini azaltmak için onları kapatır. Elektrik tüketiminin ayarlamaları donanıma göre değişebilir. Bununla ilgili olarak gerekli bilgilendirme denetim masasındaki görüntü simgesine çift tıklayarak gelecek olan pencerede ekran koruyucusu seçilerek, monitörün enerji kazandıran özelliklerinde ayarlar tıklanarak görülecektir.

HIZLI BUL Bu simgeye tıkladığınızda aradığınız konunun yada kelimenin nerede bulunacağını arıyorsunuz demektir. Bu olanak Office programını gerektirmektedir. Eğer Office kurulumunda bu bilgiler yüklenmedi ise bu simgeyi tıklayınca bilgisayar Office CD' sini isteyecek ve daha sonra bu CD' den gerekli dosyaları otomatik olarak yükleyecektir.

İNTERNET SEÇENEKLERİ Günümüzün teknolojisi ile beraber gelen internet, bu simgenin gerekliliğini ortaya koymuş ve bu ayar grubuna ihtiyaç artmıştır. Nedir bu İnternet Seçenekleri? Ne işe yarar?

İnternet ile olan bağımız bu simge içinde saklı pencerelerden oluşmaktadır. Bu simge 6 adet katmandan oluşmaktadır. Bunlar; Genel, Güvenlik, İçerik, Bağlantılar, Programlar, Gelişmiş.

Genel Katman:

Bu pencere İnternet Seçeneklerine çift tıkladığımızda zaten aktif durumdadır. 3 adet frame penceresinden oluşmaktadır. Bunlar; Giriş sayfası, Geçici İnternet Dosyaları ve Geçmiş pencereleridir.

Giriş Sayfası frame penceresinde, internete ilk bağlanıldığı zaman hangi pencerenin aktif olacağı kararı verilir. İnternete ilk girdiğimizde açılmasını istediğimiz web sayfasının adresini bu frame içindeki adres yazısının karşılığına gelen text bileşenine yazmamız yeterlidir.

Geçici İnternet Dosyaları frame penceresinde bizlere iki seçenek sunulur. İnternete bağlanıldığı zaman hangi site sayfalarının ziyaret edildiği bir klasörde tutulur. İşte birinci seçenek bu dosyalarının silinmesi için gerekli olan Dosyaları Sil butonudur. İkinci seçenek ise, bu ziyaret edilen sayfaların dosyalanması sırasında gerekli güncelleme ve disk alanı ile ilgili olan Ayarlar butonudur.

Geçmiş frame penceresinde, ziyaret edilen sayfaların özellikleri ile ilgili seçenekler yer alır. Geçmişi Sil seçeneği, ziyaret edilen sayfaların tutulmadan silinmesini öngörür. Renkler seçeneği bu sayfaların rengini, Yazı Tipleri seçeneği bu sayfaların rengini, Diller seçeneği bu sayfaları tutulacağı dili, Erişebilirlik seçeneği ise bu sayfalara bizim vereceğimiz istek doğrultusunda renk, yazı tipi gibi değişikliklere olanak sağlar.

Güvenlik Katmanı:

Bu pencerede 1 frame penceresi ve 1 adet de liste penceresi bulunmaktadır. Liste penceresinde isteğe göre bazı sitelere yasak konabilir, serbestleştirilebilinir yada iletişim kurulabilinir. Bunun için gerekli simge üzerine bir kez tıklayıp Siteler butonuna tıklamamız gerekmektedir. Açılan pencerede de gerekli alan yerlerine sayfa adresi yazılır. Bu şekilde altta bulunan frame penceresindeki imleç otomatik olarak hareket edecektir. Bu imlecin görevi ise güvenlik düzeyinin ayarı içindir. İstersek bu ayarı kendimizde Özel Düzey butonuna tıklayarak yapabiliriz.

İçerik Katmanı:

Bu pencerede 3 frame penceresi göze çarpar. Birinci frame penceresinde sitelere konulan yasağın etkinliği ve ne şekilde olacağına karar verilir. İkinci frame penceresinde kullanıcıyı diğer sayfa yetkililerine tanıtacak bilgiler bulunur. Üçüncü frame penceresinde ise 3 adet seçenek vardır. Birinci seçenek olan Otomatik Tamamla butonunda, eski metinler ile yeni yazacağımız metinleri karşılaştırıp, eskileri kullanmamıza olanak sağlayan seçenek mevcuttur. İkinci seçenekte ise Wallet butonu bulunur. Bu buton sayesinde internette yapacağımız alışveriş için kullanacağımız kredi kartı bilgileri, isim, soyisim ve şifre gibi gizli kalması gereken bilgiler gizli tutulur. Üçüncü seçenekte bulunan Profilim butonu ile kullanıcının kendisini tanıtması olanağı sunulur.

Bağlantılar Katmanı:

Bu pencerede, bilgisayarı internete bağlamak için bağlantı sihirbazını oluşturmamız öngörülür. Yada var olan bir bağlantı programı bu pencerede bulunan Ekle butonu sayesinde eklenebilinir.

Genel Katman:

Bu pencere, internet ile kullanıma sunulan programların ayar grubu ile ilgilidir. HTML düzenleyici olarak hangi programın kullanılacağı, E-posta olarak hangi programın kullanılacağı, Haber\_grupları olarak hangi programın kullanılacağı, internet çağrısı olarak hangi programın kullanılacağı, takvim olarak hangi takvimin kullanılacağı ve kişi listesi olarak hangi programın kullanılacağı kararı bu pencerede verilir. Windows otomatik olarak bu programları kendisi atar. Yalnız biz farklı bir program kullanmak istiyorsak, gerekli programı bilgisayara kurup bu listelerden herhangi birinden seçmemiz gerekmektedir. Ayrıca burada İçerik Katmanında öngörülen değerleri sıfırlamak için Web Ayarlarını Sıfırla butonu da mevcuttur.

İçerik Katmanı:

Bu pencerede 3 frame penceresi göze çarpar. Birinci frame penceresinde sitelere konulan yasağın etkinliği ve ne şekilde olacağına karar verilir. İkinci frame penceresinde kullanıcıyı diğer sayfa yetkililerine tanıtacak bilgiler bulunur. Üçüncü frame penceresinde ise 3 adet seçenek vardır. Birinci seçenek olan Otomatik Tamamla butonunda, eski metinler ile yeni yazacağımız metinleri karşılaştırıp, eskileri kullanmamıza olanak sağlayan seçenek mevcuttur. İkinci seçenekte ise Wallet butonu bulunur. Bu buton sayesinde internette yapacağımız alışveriş için kullanacağımız kredi kartı bilgileri, isim, soyisim ve şifre gibi gizli kalması gereken bilgiler gizli tutulur. Üçüncü seçenekte bulunan Profilim butonu ile kullanıcının kendisini tanıtması olanağı sunulur.

Gelişmiş Katmanı:

Bu pencerede internet ayarlarına yeni bir şekil verilebilinir. Bu İnternet Seçenekleri simgesine ait katmanlara biraz daha yeni bir ayar şekli getirmiştir. Varsayılanları Yükle butonu ile yapılan değişiklikler yok sayılabilinir.

KLAVYE Klavye ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Klavye simgesine çift tıklayın...

Gelecek olan pencerede iki katman mevcuttur. Hız ve Dil. Klavye ayarlaması klavyenin kullanımında; tuşların görünmeleriyle ilgili hız(speed) olarak ve klavyenin dil seti(language) olarak yapılır.

Hız Katmanı:

Bu katman zaten Klavye menüsüne ilk girildiğinde aktif durumdadır. Bu katmanda klavyeye bağlı olarak karakter yineleme (tuş basma) özelliğinin hızı ayarlanabilir. Ayrıca ekranda yanıp sönen imlecin, yanıp sönme hızı da buradan ayarlanabilir.

Dil Katmanı:

Bu katman kulandığımız dilin klavyeye yansıtılması ile ilgilidir. Buna bağlı olarak her tuşun üstlendiği görev değiştirilebilinir. Ayrıca buradan kullanılan dilin düzeni de değiştirilebilinir.

KULLANICILAR Bu simge tıklandığı zaman aşağıdaki gibi bir pencere ekrana gelecektir. Bu pencerede birden fazla kullanıcı için ayar yapılmasına olanak sağlanır. Burada bulunan İleri butonuna tıklanacak olursa, yeni kullanıcı oluşturmak için kullanıcı adı bilgisinin girileceği pencere ekrana gelecektir. Bu pencereye istenilen bilgi girildikten sonra İleri butonuna tıklanacak olunursa Windows oturumu için parola istenecektir. İki textden oluşan bu pencerede ilk texte istenilen şifre, ikinci texte ise şifrenin aynısı girilmesi zorunludur. Daha sonra İleri butonuna tıklanacak olunursa hangi öğelerin kullanıma açılacağı, hangi öğelerin kullanılmayacağı bilgileri gelecek olan pencerede işaretlenir.

LİVE UPDATE Bu simge ile intenete bağlanmak için gerekli bağlantı, modem ve intenet ayarlarını yapmamız öngörülmektedir. Bu pencere 3 katmandan oluşmaktadır. Bunlar; Connection, Internet, Modem.

Connection Katmanı:

Bu katman zaten Live Update penceresine ilk girildiği zaman aktif durumdadır. İntenete bağlanmak için gerekli olan bağlantı şeklinin nasıl olacağına bu pencereden karar verilir. Burada önerilen otomatik algılama olan ve algılanan sistemi kullanan Find Device automatically' dir.

İnternet Katmanı:

Bu katman ile gelecek olan pencerede internete bağlanmak için kullanıcı modem ayarlamaları bulunur. Kullanıcı adı ve şifre yapılandırması da bu pencereye ait bir özelliktir.

Modem Katmanı:

Bu katman ile gelecek olan pencereden çevrim yeri ve ayarlamalarına ilişkin yapı mevcuttur. Bu pencerede Arama Ayarları ve modemin cinsi ile ilgili olan Ayarlar butonu mevcuttur.

MODEM Modem telefon aracılığıyla iletişimi sağlayan bir aygıttır. Windows 98, normal modemlerin ve ISDN modemlerin kolayca yapılandırılmasını sağlar. Windows 98, açılış sırasında modemi tanır. İşte denetim masasında da bu modemin ayarlanması için bir menü vardır ki bu menü 2 katmandan oluşur. Gene

l ve Tanı olmak üzere bulunan 2 katman bize yeni bir modemi kurmasından, kaldırmasına; özelliklerinden bu modemin ayarlarına kadar herşeyi gösterir ve değişikliklere olanak verir.

Genel Katman:

Bu katman modem dialog penceresini ilk açtığımızda karşımıza gelecek aktif penceredir. Burada Windows 98' in algıladığı modem türü, adı ve özellikleri mevcuttur. Eğer ekle butonunu tıklayacak olursak yeni bir modem algılanmaya çalışılır. Kaldır butonuna tıklarsak da seçili olan modem kurulumdan kaldırılır. Özellikler butonu da bu modem ve yapısı ile ilgili bilgi verir bizlere. Ayrıca aramaların çevrilme biçimlerini değiştirmek için Çevirme Özellikleri adı altında bir butonda bulunmaktadır.

Özellikler Butonu:

Bu butona tıklarsanız aşağıdaki gibi bir pencere göreceksiniz. Bu pencerede görüldüğü gibi 2 katman mevcut.Genel ve Bağlantı olarak adlandırılan bu katmanlardan Genel olanı, modemimizin ismini ve türünü görüntüler. Modemimizin hangi bağlantı noktasıyla uyuştuğunun(konulduğunu) görülmesine ve de bu bağlantı noktasının(port) değiştirilmesine olanak verir. Ayrıca bağlantıyı kuracak olan modemimizin hangi hızda çalışacağını, karşı bilgisayarın(server) hızına eşitlik sağlamasını, daha doğrusu uyum sağlamasını bu katmanda sağlayabiliriz.

Bağlantı Katmanı:

Bu katman bağlantı tercihlerine olanak verir. Bunun için birim zamanda ne kadar veri biti alınacağı, eşlik değeri, dur bitlerinin değerleri, bağlantı noktası ayarları bu pencereden gerçekleştirilir.

Çevirme Özellikleri:

Bu butona tıklarsanız aşağıdaki gibi bir pencere göreceksiniz. Bu pencerede görüldüğü gibi bağlantı noktası ayarları ve arama ayarları bulunmaktadır. Bulunulan ülke, alan kodu, bir dış hatta erişmek gerekiyorsa çevrilecek numara...hepsi bu pencerededir.

Tanı Katmanı:

Bu katman modemin bağlantılı olduğu noktayı(port) görüntüler. Sürücü butonunda bu COM' un boyutu ve ne zaman yüklendiği(tarih ve saat) kullanıcıya gösterilir. Daha fazla bilgi butonuna tıklarsanız Windows otomatik olarak bu port ile bağlantı kurar ve size daha detaylı bilgi verir.

OYUN DENETLEYİCİLERİ Oyun Denetleyicileri ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Oyun Denetleyicileri simgesine çift tıklayın...

Oyun oynamak için gerekli aygıt kullanımını aktif hale getirmek için bu pencereye ihtiyacımız var. Bu pencerede bir liste ekranımıza gelecektir. Eğer liste boş yada istediğimiz aygıt ismi yok ise Ekle butonuna tıklayarak istenilen aygıtı yeni gelecek pencereden seçebilir ve aktif hale getirebiliriz. Bu gelecek pencerede de istenilen aygıt yoksa Başka Ekle butonuna tıklayarak yeni pencere açılmasını sağlarız. Bu açılan pencerede firma isimlerinin ve ürünlerinin bulunduğu bir liste görürüz. Buradan istediğimiz aygıt ismini seçerek, eğer disketi varsa disketi var seçeneğini işaretlememiz, şayet yoksa İleri tuşuna basmamız gerekmektedir. Gelişmiş katmanında ise bu oyun denetleyicilerinin bağlantı noktaları ile ilgili ayar yapıları karşımıza gelecektir. Buradan da istenilen ayar yapısı seçilerek Tamam butonuna basılması yeterlidir.

PAROLALAR Parolalar ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Parolalar simgesine çift tıklayın...

Parolalar, adından da anlaşılacağı üzere kullanıma bir kısıtlama getirmek demektir. Tabii ki Windows kullandığımız için bu kısıtlama Windows' u kapsayacaktır. Eğer bilgisayar oturumunu izin verilen kişi dışında kullanılması istenmiyorsa, bu simgeden açılacak pencere ile bu kısıtlama uygulanabilinir, değiştirilebilinir ve ayarlanabilinir. Bu pencere iki katmandan oluşmaktadır. Bunlar Parolaları Değiştir ve Kullanıcı Bilgileri. Parolaları Değiştir Katmanı:

Bu pencere zaten Parolalar simgesine çift tıklanıldığında aktif durumda olacaktır. Bu pencerede yapabileceklerimiz şunlardır; Var olan bir parolayı değiştirebiliriz. Bu uygulamayı da "Windows Parolasını Değiştir" butonu kullanılarak gerçekleştirebiliriz.

Eğer başka programlarda da aynı şekilde parola uygulaması bulunuyorsa(Windows hariç), bu parolaları da "Diğer Parolaları Değiştir" butonuna tıklayarak gerçekleştirebiliriz.

Windows Parolasını Değiştir Butonu:

Bu pencere var olan Windows parolasını değiştirmemizi sağlar. İlk text penceresine eski, diğerlerine yeni parolamızı girmemiz yeterli olacaktır.

Kullanıcı Bilgileri Katmanı:

Bu pencerede kullanıcıya iki seçenek sunulmuştur. Bunlardan birincisi ve ilk seçenek olanıyla, parola kullanarak bilgisayara girenlere tek tip ayar yapısı geçerlidir. Yani bilgisayarın tüm özellikleri her kullanıcı için geçerli olacak ve tüm kullanıcılar bu ayar yapısında işlem yapacaklardır. Diğer seçenekte ise, parola kullanarak bilgisayara girenlere ayrı bir özgürlük tanınacak ve ayarları kendilerinin yapması imkanı verilecektir.

POSTA Posta ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Posta simgesine çift tıklayın...

Bu simgeye tıkladığımızda aşağıdaki gibi pencere açılacaktır. Bu pencerede bilgisayarda kayıtlı olan kişi profilleri liste halinde yer alacaktır. Eğer liste boş ise yeni profil tanımlanmasına izin verilir. Bunun için Ekle butonuna tıklamamız gerekir. Burada Microsoft Outlook ile kullanmak istediğimiz bilgi hizmetlerini açılan pencerede görebiliriz. İstenilen seçenek işaretlendikten sonra İleri butonuna tıklayarak yeni bir kişi profili belirleyebiliriz. Bu kişi profillerini elektronik posta gönderirken kullanabilir ve o kişiler hakkında bilgi edinebiliriz.

PROGRAM EKLE/KALDIR Program ekle/kaldır ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Program Ekle/Kaldır simgesine çift tıklayın...

Windows 98, Plug and Play teknolojisi ile kuruluş ve başlangıç sırasında yeni eklenmiş donanım birimlerini tanır. Eğer yeni aygıt otomatik tanımalı değilse o zaman bu özellik kullanılır. Bu pencereye ait 3 katman mevcuttur. Bunlar; Yükle/Kaldır, Windows Kur, Başlangıç Disketi.

Yükle/Kaldır Katmanı:

Bu pencere zaten Program Ekle/Kaldır simgesini tıkladığımızda aktif haldedir. Herhangi bir programın kaldırılması isteniyorsa menüde bulunan listeden istenilen program seçilir ve Ekle/Kaldır butonuna basılır. Bu sayede program uninstall edilmiş olur. Şayet yeni bir program kurulacaksa o zaman, yüklenecek olan programın disketi veya CD' si takılır yükle butonuna basılır.

Windows Kur Katmanı:

Windows 98 bize çok değişik ve çeşitli bileşenlerle beraber sunulmuştur. Bu bileşenleri aktif hale getirmek ya da kaldırmak bize bırakılmıştır. Bu katman seçildiğinde Windows 98 otomatik olarak bileşenleri aramaya başlayacaktır ve bileşen listesini ekrana getirecektir. İstenilen bileşenin yanındaki onay kutusuna mouse yardımıyla işaret bırakmamız veya kaldırmamız yeterli olacaktır. Daha sonra tamam butonuna tıklamamız gerekecek. Bu bileşenlerle ilgili detaylı bilgiyi, istenilen bileşenin üzerine bir kez tıklayarak ve daha sonra ayrıntılar butonuna basarak edinebiliriz.

Başlangıç Disketi Katmanı:

Windows 98' i başlatırken bir sorunla karşılaşırsak, bilgisayarımızı başlatmak için bir başlangıç disketini kullanabilir ve tanı programlarını çalıştırarak birçok sorunu giderebiliriz. İşte bu başlangıç disketini oluşturmak için disket sürücüsüne boş bir disket yerleştirmek ve daha sonra buradan sistem dosyalarının yüklenebilmesi için Disket Oluştur butonuna tıklamamız yeterli olacaktır.

SES Ses ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Ses simgesine çift tıklayın...

Bu simgeye tıkladığımız zaman aşağıdaki gibi bir pencere açılacaktır. Buradaki listeden istenilen ses düzenlerinden herhangi birinin üzerine bir kez tıklayarak Önizleme butonu ile görebilir ve play(

) tuşuna basarak bu sesi dinleyebiliriz. Gözat butonu ile farklı ses biçimlerini görebilir, Ayrıntılar butonu ile de bu ses biçimlerinin özelliklerini(uzunluğu, biçimi, ...vs) görmemiz mümkün. Düzenler frame' inde bulunan Farklı Kaydet butonu ile mevcut bulunan ses biçiminin ismi değiştirilebilinir, Sil butonu ile de kaydedilen yeni isim silinebilinir.

SİSTEM Sistem ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Sistem simgesine çift tıklayın...

Bu işlemden sonra açılacak pencerede 4 ana katmanın olduğunu göreceğiz. Bunlar; Genel, Aygıt Yöneticisi, Donanım Profilleri, Başarım.

Genel Katmanı:

Bu pencere zaten Sistem simgesine çift tıkladıktan sonra aktif duruma gelecek ve ekranda görünecektir. Bu pencerede kullanılan pencerenin ne olduğu, hangi zamanda oluşturulduğu, kimin tarafından oluşturulduğu, bilgisayarın işlem hızı, ram boyutu ve sistemin hangi firmaya ait olduğu bilgilerine yer verilir.

Aygıt Yöneticisi Katmanı:

Bu katmanda bilgisayar donanım elemanlarına ait bir liste penceresi yer alı. Eğer bu donanım elemanlarının başka alt bileşenleri de varsa burada gösterilir. Bu liste iki şekile göre oluşturulur. Birincisi Türe göre, ikincisi ise bağlantıya göredir. Bu listeleme şeklini bu penceredeki en üstte bulunan radyo seçeneklerinden yapabiliriz. Liste elemanlarından herhangi birinin üzerine tıklayıp Özellikler butonuna basarsak, işaretli bulunan donanım elemanı ile ilgili bilgiler önümüze gelir. Eğer Yenile butonuna tıklarsak, işaretli bulunan donanım elemanının sürücüsü güncelleştirilir. Kaldır butonunun görevi ise seçili bulunan donanım elemanının kaldırılması, başka bir deyişle silinmesidir. Yazdır butonu, seçili bulunan donanım elemanının özelliklerini yazdırmaya yarar.

Donanım Profilleri Katmanı:

Burada bize yani kullanıcıya, ağ halinde bulunduğu ortamdan yada başka bir ortamdan yeni donanım profillerinin yüklenmesi olanağı sağlanır. Veyahut da mevcut yapının isminin değiştirilmesi olanağı sunulur.

Başarım Katmanı:

Bu pencerede sistem kurulumunun başarısı hakkında kullanıcıya bilgi verilir. Bellek olarak kullanılan Ram' in boyutu, sistem kaynaklarının durumu, dosya sistemi, sanal bellek, disk sıkıştırması, PC kartları ile ilgili bilgiler bu pencerede yer alırlar. Gelişmiş Ayarlar frame' inde bulunan butonlardan Dosya Sistemi, bilgisayarda mevcut bulunan sürücü ayarlarının yapılandırılması ile ilgilidir. Sabit disk, CD rom, disket, çıkarılabilir disk bunlardan bazılarıdır. Grafik butonu ile bilgisayarda kullanılacak grafiklerin boyut ayarlamaları ve buna bağlı olarak donanım ivmesinin ayarı yapılabilinir. Sanal Bellek butonu ile oluşturulacak bir sanal belleğin, kullanıcının kendisinin mi oluşturacağı yoksa bilgisayar tarafından otomatik mi yapılacağı bilgilerine ulaşılır.

TARİH/SAAT Tarih ve saat ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Tarih/Saat simgesine çift tıklayın...

Bu menüde sistem zamanı ve bu zaman hakkındaki ayarları bulabiliriz.

Denetim masasındaki Tarih/Saat sembolüne tıklayınca yukarıdaki menü ekrana gelir.Bu menü 2 katmandan meydana gelir. Bunlardan birincisi Tarih ve Saat, ikincisi ise Saat Dilimi dir.

Tarih ve Saat Katmanı:

Bu katman zaten Tarih/Saat menüsüne ilk girildiğinde aktif durumdadır. Burada kullanıcıya zaman ayarlaması olarak iki seçenek sunulur. Birinci ayar grubu Tarih için ikinci ayar grubu saat içindir. Tarih seçeneğinde sistem zamanını gün, ay, yıl olarak ayarlamamız sağlanır. Saat seçeneğinde ise sistem zamanını saniye, dakika, saat olarak ayarlamamız sağlanır.

Saat Dilimi Katmanı:

Bu katman evrensel olarak kabul görmüş saat uygulamasının bölgesel dağılışını göstermektedir. Kullanıcının bulunduğu saat dilimi yeri buradan ayarlanabilir. Hemen altındaki uyarı da işaretli ise bilgisayar otomatik olarak yaz saati uygulaması ve kış saati uygulamasını gerçekleştirir.

TELEFON Telefon ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Telefon simgesine çift tıklayın...

Bu simge size bir nevi dünyaya açılma kapısının anahtarı olacaktır. Çünkü bu menüden internete giriş yapılması için gereken telefonun ayarlarını yapabilirsiniz.Bu simge içerisinde 2 tane katman vardır. Bunlar Yerlerim ve Telefon Sürücüleri.

Yerlerim Katmanı:

Bu menü penceresi zaten siz telefon simgesine çift tıkladıktan sonra açılan pencerede aktif olacaktır.Aşağıda görüldüğü gibi pencere, arama yeri bulunulan ülke ve bu ülkeye ait alan kodlarını içerir. Şayet bir dış hatta erişilecekse bu hat numarasıda "yerel aramalar için" veyahut "şehirlerarası aramalar için" yazan bölüme hat numaraları girilmesi gereklidir. Ayrıca kullanılacak erişimin tonlu arama ile mi yapılacağı yoksa darbeli aramayla mı yapılacağı bu menü penceresinden de işaretlenebilir.

Telefon Sürücüleri Katmanı:

Bu menü penceresi, kullanılacak telefon servisinin bilgisayarımıza yüklenmesi ve bilgisayarımızın bu servisi tanıması içindir. Burada bulunan listeden uygun telefon sürücüsü, üzerine bir kez tıklanarak ve daha sonra ekle butonu kullanılarak bilgisayarımıza yüklenebilinir. Şayet istenilen telefon sürücüsü listede yoksa yapılandır butonu kullanılarak gerekli sürücü bilgisayara yüklenebilinir.

YAZI TİPLERİ Yazı tipleri ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Yazı Tipleri simgesine çift tıklayın...

Gelecek olan pencerede Birçok yazı tipi olacaktır. Windows işte bu yazı tiplerini kullanmakta. Ortak özellikler taşıyan bir karakter grubuna font denir. Yazı tipi, bir kelime işlemcinin en önemli özelliklerinden biridir. Karakterlerin şeklinin biçem ve boyutla birleşmesi sonucunda yazı tipini tanımlayabiliyoruz. Karakterlerin normal, kalın(bold), italik olması gibi biçem seçeneklerimiz var. Bu ekrandaki yazı tiplerinin ne şekilde olduğunu görmek için üzerine çift tıklamamız yeterli ve aynı zamanda bu şekilde bu yazı tipini yazdırabiliriz de. Ayrıca Yeni Yazı Tipi Yükleyip, var olan Yazı tipini de kaldırabiliriz. Kaldırma olayını silmek istediğiniz tipin üzerine gelerek mouse' un sağ tuşuna basıp sil menü elemanını işaretleyerek gerçekleştirebilirsiniz...

Yeni Yazı Tipi Yüklemek:

Bilgisayarınıza yeni bir yazı tipi yüklemek için önce Fonts başlıklı pencerenin Dosya menüsünü açın. Sonrada yeni yazı yükle satırına tıklayın. Yükleyeceğiniz yazı tiplerinin yerini bulup adlarını seçmeniz için bir menü açılacaktır. Kopyalayacağınız yeri seçin ve tamamı tıklayın. Hepsi bu kadar.

YAZICILAR Yazıcı ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Yazıcılar simgesine çift tıklayın...

İşte o zaman aşağıdaki pencere ekrana gelecektir.(Eğer yazıcı yoksa) Daha sonra bilgisayara bir yazıcı eklemek için pencere içinde bulunan Yazıcı Ekle simgesine tıklamamız gerekecek.

Yazıcı Ekle Simgesi:

Yazıcı Ekle simgesine tıkladığımızda aşağıdaki gibi bir pencere açılacaktır. Buradan yüklemek istediğimiz yazıcıyı İleri butonuna tıklayarak görebiliriz.

İleri Butonu:

Bu butona tıkladığımızda aşağıdaki gibi pencere ekrana gelecektir. Burada yazıcı adlarına ait bir liste ve bunları üreten firma isimlerini görebiliriz. Buradaki listelerden elimizdeki yazıcıya uygun üretici ismini ve yazıcı modelini işaretleyip, eğer bu yazıcının sürücüsü varsa disketi var butonuna tıklayın ve disket sürücüye yada CD sürücüye gerekli yazılımı içeren sürücüyü koyun. Daha sonra Yazıcı Ekleme Sihirbazını takip edin.

YENİ DONANIM EKLE Yeni Donanım Eklemek ile ilgili ayarları yapabilmek için önce Denetim Masası penceresindeki Yeni Donanım Ekle simgesine çift tıklayın...

Bu simgeye tıklamakla beraber donanıma kattığımız yeni aygıtları görebilir ve tanımlayabiliriz. Ve böylece bu aygıtları çalıştırabiliriz.

İleri butonuna tıklarsak karşımıza şu şekilde bir pencere açılır.

Bu pencerede Windows kendi içinde bir arama yapacak be bağlantı noktalarını kontrol edecektir. Yeni bir donanım elemanı bulduğunda(tanımlanmış, tanımlanmamış, yanlış tanımlanmış) aşağıdaki pencereye benzer bir pencere ekrana getirecektir.

Bu penceredeki yazılanlardan da anlaşılacağı üzere listede, istenilen donanım aygıtının olup olmadığı karara bağlanır, eğer varsa bu öğe seçildikten sonra ileri butonuna , yoksa "Hayır,aradığım aygıt,aygıt listesinde yok" seçeneğini işaretlememiz gerekmektedir. Daha sonra ileri butonuna tıklamamız ve yüklenecek olan aygıtı bir listeden seçmemiz gerekmektedir.

ODBC (Veri Kaynağı Yöneticisi)

Odbc Nedir? Açık Veritabanı Bağlanabilirlik (ODBC) teknolojisi; heterojen SQL veritabanlarına erişim için ortak bir arayüze sahiptir. ODBC, verilere erişmenin bir standardı olarak Yapılandırılmış Sorgulama Dilini (SQL) kullanır. Bu arayüz maksimum birlikte çalışabilirlik sağlar: bir tek uygulama, bir ortak kod seti üzerinden farklı SQL Veritabanı Yönetim Sistemlerine (DBMS) erişebilir. Bu; bir geliştiricinin, spesifik bir DMBS hedeflemeden bir istemci/sunucu uygulaması oluşturup dağıtabilmesini sağlar. Veritabanı sürücüleri; bu şekilde, uygulamayı, kullanıcının seçtiği DMBS'e bağlamak üzere eklenir. ODBC yararları; ODBC Uygulamaları, bir yetkili API satıcısına bağlı değildir.

ODBC 3.0; X/Open ve ISO Çağrı Düzeyi Arayüzü (CLI) standartları ile hizalanır ve bunların bir alt setidir.

Artan performans.

ODBC 3.0 ın Özellikleri Bu özelliklerin birçoğu önceki sürümlerde de yer almaktadır.

Açıklayıcılar:Açıklayıcılar, birçok uygulama işlemlerinin akışını sağlayarak sütun veya parametre verilerine erişim için doğrudan ve değişmez bir yol sunarlar. ODBC 3.0'de gerçekleştirilen ilerlemelerin çoğu açıklayıcı kullanmanın bir sonucudur.

Tanılar: ODBC 3.0'de, fonksiyon çağırmaların sonucu hakkındaki bilgiler bir tanı alanında bulunmaktadır. Her bir görevlinin bir tanı alanı vardır. Bu, geliştirilmiş hata raporlama özelliğine sahiptir ve yapılan hataları hiçbir kayba uğratmadan kurtarmayı sağlar.

Katalog Fonksiyonu Sütun İsimleri: Katalog fonksiyonlarının sonuç setindeki sütun isimleri, X/Open ve ISO CLI standartlarındaki isimlere göre sıralanır.

Ortam Özellikleri: Ortam özellikleri girilir, ve bu özelliklere ulaşıp ayarlayacak olan fonksiyonlar sunulur. Sözcük özelliğinin kendisinin, ODBC 2.x'de kullanılmış olan sözcük seçeneğinin (bağlantı seçeneği ve açıklama seçeneği gibi) yeniden isimlendirilmiş bir hali olduğunu unutmayın. Özelliklere ulaşıp ayarlayacak yeni fonksiyonlar: Ortam, bağlantı, ve açıklama özelliklerine ulaşıp ayarlayacak yeni fonksiyonlar girilir. ODBC 2.x bağlantı ve açıklama seçeneklerine benzerlik göstermelerine rağmen, bu özellikler ara uzunluğu ve çıktı dizisi uzunluğunu belirleyici ek argümanlar içerir.

Geliştirilmiş Özellikler

Yeni veri türleri: Aralık veri türleri için destek ilave edilmiştir, sayısal ve ondalık verileri toplamak için bir C yapısı, ve ayrıca 64-bit tam sayıları toplamak için yeni bir ODBC C türü ilave edilmiştir.

Yığın(Batch) Desteği: Uygulama, sürücüden yığınlı işleme karşı hareketine göre,ayrıntılı bilgi alabilir. Bu, uygulamanın yığınları akıllıca kullanmasını sağlar, bu sayede bir performans artışı elde edilir.

İsimlendirilmiş Parametreler için Destek: Birçok veri kaynağı, kayıtlı prosedür aramaları sırasında dinamik parametrelere isim vererek bunların spesifikasyonlarını destekler. Bu şekilde isimlendirilmiş parametreler için destek, ODBC 3.0'de sağlanır.

Çok satırlı ekrana getirmeler için genişletilmiş hata raporlama: Açıklayıcıya ve tanı alanlarına, uygulamanın satır setindeki kendisi için hata görüntülenen sütun ve satırların sayılarını belirleyebilmesi için ek alanlar ilave edilmiştir.

Parametre Dizileri İçin Genişletilmiş Hata Raporlama: Bir SQL komutunun bir dizi parametre değerleri dizisi ile birlikte işletilmesinden sonra, satır durumu dizisine benzer bir dizi elde edilebilir. Bu dizi, parametre "satırları"ndan her birinin işletilmesinden sonraki durumu içerir.

SQLSetPos'taki SQL\_ADD seçeneğine itiraz: SQLSetPos'un SQL\_ADD seçeneğine itiraz edilmiş ve bu görev, yeni bir fonksiyon olan SQLBulkOperations'ın bir parçası haline getirilmiştir.

Bir "Satırı"n İhmal Edilmesi: SQLSetPos veya SQLBulkOperations sırasında, geçici uygulama alanlarındaki belirli bir satırın o işlem için ihmal edildiğini belirtebilirsiniz. Bir parametre dizisi ile işlem yaptığınızda, verilen bir parametre "satırı"nın ihmal edileceğini belirtebilirsiniz.

Bağlayıcı Geliştirmeleri: Sütun ve parametreler, sabit bir offsetin mevcut bağlı geçici adreslere ekleneceğini belirtilerek, kısa sürede tekrar bağlanabilirler. ODBC 2.x'de, sadece sonuç seti sütunları satır-sıralı bağlanabilir. ODBC 3.0'de, satır-sıralı bağlama aynı zamanda parametreler için de kullanılabilir.

Yer İmleri Geliştirmeleri: Yer imleri ODBC 3.0'de farklı uzunlukta olabilir. Artık, bir satırı bir yer imi veya bir offset ile ekrana getirmek mümkündür. Uygulama, yeni SQLBulkOperations fonksiyonu ile bitişik olmayan satır setlerini güncelleyebilir, silebilir, veya ekrana getirebilir.

SQLGetInfo geliştirmeleri: SQL-92 için sürücü/veri kaynakları desteğini belirleyici yeni bilgi türleri. Birçok bilgi türü, imleç türüne göre elde edilebilir.

Uyum Düzeyleri: Yeni uyum düzeyleri için destekli arayüz elemanları temel olarak alınmıştır. ODBC 2.x'deki uyum düzeyleri için destekli fonksiyonlar temel olarak alınmıştı.

SQL-92 ile Sıralama: ODBC 2.x'de, X/Open SQL spesifikasyonuna göre hazırlanmış bir SQL grameri sağlanmıştı. ODBC 3.0'de, bu gramer kaldırıldı, ve SQL grameri ile ilgili tartışmaların tümü SQL-92'ye dayandırıldı.

Tür bilgileri: Daha fazla tür bilgisi SQLColAttribute fonksiyonundan (ODBC 2.x'den SQLColAttributes'ı kullanan) edinilebilir.

ODBC 3.0 ın özelliklerinden sonra Denetim Masası İçerisinde yer alan ODBC Veri kaynağı yöneticisinin görünümü hakkındaki bilgilere geçelim.

Kullanıcı DSN Sekmesi Kullanıcı DSN’leri olan veri kaynakları ekler, siler veya ayarlar. Bu veri kaynakları, bir bilgisayar için yereldir ve yalnızca geçerli kullanıcı tarafından kullanılabilirler.

Kullanıcı Veri Kaynakları listesi: Her DSN’nin ve DSN ile ilişkili sürücünün adını içeren, tüm kullanıcı DSN’lerine ilişkin listedir. Bir kullanıcı DSN’sinin çift tıklatılması, sürücüye özgü veri kaynağını ayarlama iletişim kutusunu görüntüler.

Yapılandır:Varolan bir kullanıcı veri kaynağının yapısını değiştirmenize olanak tanıyan, sürücüye özgü veri kaynağını ayarlama iletişim kutusunu görüntüler. Yapılandır’ı tıklatmadan önce, bir kullanıcı veri kaynağının adını listeden seçmeniz gerekir.

Ekle:Yeni bir kullanıcı veri kaynağı ekler. Ekle’yi tıklattığınızda, sürücülerin listesiyle birlikte Yeni Veri Kaynağı Oluştur iletişim kutusu görüntülenir. Kendisi için kullanıcı veri kaynağı eklemekte olduğunuz sürücüyü seçin. Son’u tıklattığınızda, sürücüye ilişkin bir kurulum iletişim kutusu görüntülenir.

Kaldır:Varolan bir kullanıcı veri kaynağını kaldırır. Kaldır’ı tıklatmadan önce, kaldırmak istediğiniz kullanıcı veri kaynağının adını listeden seçmeniz gerekir.

Tamam:Yönetici iletişim kutusunu kapatır. Kullanıcı Veri Kaynakları listesindeki değişiklikleri kabul etmek için Tamam düğmesini tıklatmanız gerekmez. Listedeki değişiklikler, veri kaynağını ayarlama iletişim kutusunda Tamam düğmesini tıklattığınızda kabul edilir.

İptal :Yönetici iletişim kutusunu kapatır. İptal’i tıklatırsanız, Kullanıcı Veri Kaynakları listesindeki değişiklikler reddedilmez.

Yardım:Bu Yardım kaynağımı görüntüler.

Sistem DSN Sekmesi Sistem DSN’leri olan veri kaynakları ekler, siler veya ayarlar. Bu veri kaynakları, bir kullanıcıya adanmış değildir ve bilgisayar için yereldir. Sistem veya yetkisi olan herhangi bir kullanıcı sistem DSN’leri olan bir veri kaynağını kullanabilir.

Sistem Veri Kaynakları listesi:Her DSN’nin ve DSN ile ilişkili sürücünün adını içeren, tüm sistem DSN’lerine ilişkin listedir. Bir siste DSN’nin çift tıklatılması, sürücüye özgü veri kaynağını ayarlama iletişim kutusunu görüntüler.

Yapılandır:Varolan bir sistem veri kaynağının yapısını değiştirmenize olanak tanıyan, sürücüye özgü veri kaynağını ayarlama iletişim kutusunu görüntüler. Yapılandır’ı tıklatmadan önce, bir sistem veri kaynağının adını listeden seçmeniz gerekir.

Ekle: Yeni sistem veri kaynağı ekler. Bu düğmeyi tıklattığınızda, sürücülerin listesiyle birlikte Yeni Veri Kaynağı Oluştur iletişim kutusu görüntülenir. Kendisi için sistem veri kaynağı eklemekte olduğunuz sürücüyü seçin. Bitir’i tıklattığınızda, sürücüye ilişkin bir kurulum iletişim kutusu görüntülenir.

Kaldır:Varolan sistem veri kaynağını kaldırır. Kaldır’ı tıklatmadan önce, kaldırmak istediğiniz sistem veri kaynağının adını listeden seçmeniz gerekir.

Tamam:Yönetici iletişim kutusunu kapatır. Sistem Veri Kaynakları listesindeki değişiklikleri kabul etmek için Tamam düğmesini tıklatmanız gerekmez. Listedeki değişiklikler, veri kaynağını ayarlama iletişim kutusunda Tamam düğmesini tıklattığınızda kabul edilir.

İptal:Yönetici iletişim kutusunu kapatır. İptal’i tıklatırsanız, Sistem Veri Kaynakları listesindeki değişiklikler reddedilmez.

Yardım:Bu Yardım kaynağını görüntüler.

Dosya DSN Sekmesi Dosya DSN’leri olan veri kaynakları ekler, siler veya ayarlar. Bunlar, dosya tabanlı veri kaynaklarıdır ve aynı sürücüleri kurmuş olan ve veritabanına erişebilen tüm kullanıcılar tarafından paylaşılabilir.

Bu veri kaynaklarının bir kullanıcıya adanmış olmaları veya bir bilgisayar için yerel olmaları gerekmez.

Dosya Veri Kaynakları listesi: Bakılacak Yer kutusunda görüntülenen dizinde yer alan tüm dosya DSN’leri ve alt dizinleri görüntüler. Bir dosya DSN’nin çift tıklatılması, sürücüye özgü veri kaynağını ayarlama iletişim kutusunu görüntüler.

Ekle:Yeni bir dosya veri kaynağı ekler. Bu düğmeyi tıklatırsanız, sürücülerin listesiyle birlikte Yeni Veri Kaynağı Oluştur iletişim kutusu görüntülenir. Kendisi için dosya veri kaynağı eklemekte olduğunuz sürücüyü seçin. İleri’yi tıklattıktan sonra, dosya DSN’sine ilişkin anahtar sözcükleri doğrulayabilirsiniz.

Kaldır:Varolan bir dosya veri kaynağını kaldırır. Kaldır’ı tıklatmadan önce, kaldırmak istediğiniz dosya veri kaynağının adını listeden seçmeniz gerekir.

Yapılandır:Varolan bir sistem veri kaynağının yapısını değiştirmenize olanak tanıyan, sürücüye özgü veri kaynağını ayarlama iletişim kutusunu görüntüler. Yapılandır’ı tıklatmadan önce, bir dosya veri kaynağının adını listeden seçmeniz gerekir.

Dizin Ayarla: Görüntülenen dizini, ODBC Yöneticisi yürütüldüğünde görüntülenecek dizin olarak belirler.

Bakılacak Yer:Kendisine ilişkin alt dizinlerin ve dosya DSN’lerin aşağıdaki pencerede görüntülendiği geçerli dizini görüntüler. Metin kutusunun sağındaki aşağı ok simgesinin tıklatılması, o dizine ilişkin yolu tam olarak görüntüler. ODBC Yöneticisi ilk kez yürütüldüğünde varsayılan dizin sistem bilgilerine eklenir, ancak Dizin Ayarla düğmesini tıklatarak bu dizini değiştirebilirsiniz.

Yukarı:Bakılacak Yer kutusunda görüntülenen dizini, geçerli dizinin hemen üstündeki dizin olacak biçimde değiştirir.

Tamam:Yönetici iletişim kutusunu kapatır. Dosya Veri Kaynakları listesinde yapılan değişiklikleri kabul etmek için Tamam düğmesini tıklatmanız gerekmez. Listedeki değişiklikler, veri kaynağını ayarlama iletişim kutusunda Tamam düğmesini tıklattığınızda kabul edilir.

İptal: Yönetici iletişim kutusunu kapatır. İptal’i tıklatırsanız, Dosya Veri Kaynakları listesindeki değişiklikler reddedilmez.

Yardım:Bu Yardım kaynağını görüntüler.

ODBC Sürücüleri Sekmesi Kurulu ODBC sürücülerine ilişkin bilgi görüntüler. ODBC Sürücüleri listesinde, bilgisayarınızda önceden kurulu olan sürücüler gösterilir.

ODBC Sürücüleri listesi:Bilgisayarda kurulu olan her ODBC sürücüsünün adı, sürümü, firması, dosya adı ve dosya oluşturma tarihi.

Tamam:Yönetici iletişim kutusunu kapatır.

İptal:Yönetici iletişim kutusunu kapatır.

Yardım:Bu Yardım kaynağını görüntüler.

Bu iletişim kutusunda artık, sürücü eklemek veya silmek için kullanılacak Ekle ve Sil düğmeleri bulunmamaktadır. ODBC sürücülerini kendi kur programlarından eklemeniz veya kaldırmanız gerekir.

İzleme Sekmesi ODBC Sürücüsü Yöneticisi’nin ODBC işlevlerine yönelik çağrıları nasıl izleyeceğini belirtmenizi sağlar. Sürücü Yöneticisi, çağrıları sürekli olarak izleyebilir veya tek bir bağlantı için izleyebilir; dinamik olarak izleme yapabilir; veya izlemenin özel bir izleme .dll dosyası tarafından yapılmasına izin verebilir.

İzlemeyi Şimdi Başlat:ODBC Yöneticisi iletişim kutusu görüntülendiği sürece dinamik izleme yapılmasına olanak tanır. Dinamik izleme, bir bağlantı kurulmuş olsa da olmasa da etkinleştirilebilir. İzlemeyi Şimdi Başlat düğmesini tıklattığınızda, düğme İzlemeyi Şimdi Durdur olarak değişir. İzlemeyi Şimdi Durdur düğmesi tıklatılıncaya kadar, dinamik izleme etkin durumda kalır.

Visual Studio Çözümleme İzlemesini Başlat:Visual Studio çözümleyicisi olaylarının bildirilmesine olanak tanır. Visual Studio Çözümleme İzlemesini Başlat düğmesini tıklattığınızda, bu düğme Visual Studio çözümleme olaylarını izlemeyi etkin durumdan çıkaran Visual Studio Çözümleme İzlemesini Durdur olarak değişir. Visual Studio Çözümleme İzlemesini Durdur tıklatılıncaya kadar, Visual Studio çözümleyicisi olaylarını izleme işlevi etkin durumda kalır.

Günlük dosyası yolu:İzleme bilgilerinin saklanacağı dosyanın yolunu ve dosya adını görüntüler. Varsayılan yol ve dosya adı (sql.log) sistemden alınır, ancak, yeni bir yol ve dosya adı girerek veya Gözat düğmesini tıklatıp bir dizin ve dosya seçerek, yeni bir dosya belirtebilirsiniz.

Gözat: Makine dizinlerine gözatarak, günlük dosyası için yol ve dosya adı seçmenize olanak tanır.

Özel İzleme DLL'i:İzleme gerçekleştirmek için Odbctrac.dll’den farklı bir izleme .dll'i seçmeye olanak tanır. Data Access SDK ile birlikte verilen Odbctrac.dll dosyası, sizin seçtiğiniz özel bir .dll dosyasıyla değiştirilebilir. Özel .dll dosyasının bulunduğu yolu ve dosya adını girin veya dizinlere gözatmak için DLL Seç düğmesini tıklatın.

DLL Seç:Kullanıcının özel bir .dll için dizin yapısına gözatmasına olanak tanır. Bir .dll seçtiğinizde, bulunduğu yol ve dosya adı Özel İzleme DLL'i metin kutusunda görünür.

Tamam:İzleme değişikliklerini kabul eder ve Yönetici iletişim kutusunu kapatır.

İptal İzleme değişikliklerini kabul etmeden Yönetici iletişim kutusunu kapatır.

Uygula:Yapılan izleme değişikliklerini, Yönetici iletişim kutusunu kapatmadan kabul eder. Değişiklik yapılmadıysa, Uygula düğmesi silik olarak görüntülenir.

Yardım:Bu Yardım kaynağını görüntüler.

Bağlantı Toplama Sekmesi Bağlantı toplama kullanırken, bağlantıyı yeniden denemek için bekleme süresini ve seçilen bir sürücü için bağlantı zaman aşımı süresini değiştirmenize olanak tanır. Ayrıca, bağlantı istatistiklerini kaydeden Performans İzleme işlevini de etkinleştirmenize veya etkin durumdan çıkarmanıza olanak tanır.

ODBC Sürücüleri Listesi:Bilgisayarda kurulu olan her bir ODBC sürücüsünün adı, sürümü, firması, dosya adı ve dosya oluşturma tarihi.

Seçilen sürücü için toplama zaman aşımı: Seçilen sürücüsü için bağlantı toplama zaman aşımı süresini saniye cinsinden ayarlar. Bağlantı toplama niteliklerini ayarlamak için, sürücü adını çift tıklatın.

Etkinleştir:Performans izleme işlevini etkinleştirir.

Etkin Durumdan Çıkar:Performans izleme işlevini etkin durumdan çıkarır.

Yeniden Deneme Bekleme Süresi:ODBC Sürücüsü Yöneticisi bir veritabanı sunucusunun kullanılabilir olmadığını saptarsa, yeniden bağlanmayı denemeden önce belirli bir süre bekler. Saniye cinsinden Yeniden Deneme Bekleme Süresi değeri belirterek, bekleme süresini ayarlayabilirsiniz. Değerlerin altıdan az rakam içermesi gerekir.

Yardım:Bu Yardım kaynağını görüntüler.

Ürün Bilgisi Sekmesi ODBC çekirdek bileşenleriyle ilgili, Sürücü Yöneticisi, imleç kitaplığı, kurucu .dll ve çekirdek bileşenleri oluşturan diğer dosyalar gibi bilgileri görüntüler.

Çekirdek Bileşen Listesi:Her ODBC çekirdek bileşeninin açıklaması, sürümü, dosya adı ve yeri.

Tamam:Yönetici iletişim kutusunu kapatır.

İptal:Yönetici iletişim kutusunu kapatır.

Yardım:Bu Yardım kaynağını kapatır.

REGISTRY (KAYIT DÜZENLEYİCİ) Bir uygulama, son pencere boyutu, kullanıcı ayarları ve kullanıcı tarafından kullanılan son dosyalar gibi bilgileri saklamak için ini dosyası kullanmalıdır.

16-bit windows sürümlerinde olduğu gibi 32-bit windowslardaki configrasyon dosyalarının son kullanma tarihide herhalde bir yıl içinde sona erceğe benziyor. Windows üreticilerinin Wistler adlı 64-bit işletim sisteminin üzerinde durduğunu duyuyoruz. İşte, bu tip 16,32,64 bit gibi uygulama proğramlarına ait bilgileri biz windows kayıt düzenleyicisi (Registry ) tutarız. 16-bit windows'da yani Win95 teki registr geniş kullanım alanları sunmuyordu. Win95 ten sonraki 32-bit windows sürümlerinde ise kullanıcı için iyi seçenekler içeriyor. Tabi buradaki ayarlarla uğraşmanız için hiçbir kullanıcıya bir zorlama yok. Fakat registry, uygulama verilerini tutmanın gelişmiş bir yolu ve windowsun beyni vazifesinde olduğu için yapı ve içerik olarak öğrenmek iyi olacaktır. Şimdi registr nedir? Registr’a nasıl gireriz? Bölümleri nelerdir? Bir anahtar nasıl oluşturabiliriz? Sorularının cevabını arayalım. Anlatacağımız konuları Win98 Türkçe versiyonunda gösterdik.

Registry (Kayıt düzenleyicisi) nedir? Registry; Windows'un configrasyonu yada sizin programınızın tanımlanmış uygulama verilerin tutulduğu basit bir veri tabanıdır. Registry'nin nihai görevi OLE nesnelerinin birbirleri ile iletişimi için OLE bilgilerini tutmaktır. (Bu Registry'nin orijinal kullanışıdır). Registry, dosyaların birlikte açılmalarını sağlayan izleri barındırır. Örneğin bir metin belgesine tıkladığınız zaman bu notepad.exe programı ile birlikte açılır. Registry’a nasıl girilir ?

Windows işletim sisteminin hayati dosyalarından biri olan registry (Kayıt düzenleyici) içeriğinde yanlış bir değişiklik yapmak windowsunuzun sonu olabilir. Fakat gülü seven dikenine katlanır. Bence öğrenmekte yarar var. Şimdi windows dizini altındaki “regedit.exe” programını çalıştıralım. Yadaaşağıdaki şekilde gösterdiğim gibi windows masa üstünden “başlat”ı tıklayıp menüde görülen çalıştır kısmını tıklayın. Karşınıza aşağıdaki gibi bir dialog penceresi gelecektir. Bu dialog penceresindeki Aç kısmına “regedit” yazın ve sonra tamamı tıklayın.

Bu işlemden sonra karşımıza aşağıdaki registry anahat ekran görüntüsü gelecektir.

Bu ekranda sol taraftaki klasörler yani registry anahtarları ve içeriklerindeki veriler aşağıda verilmiştir.

Anahtar

OLE ve Windows'un çalışma bilgilerini içerir.

Varolan kullanıcıların kuruduğu değişik bilgileri içerir. Uygulamada belirtilmiş verileri yada Windows'un verilerini içerebilir.

Genellikle sistem hakkında donanım bilgilerini içerir. Başka bilgilerde içerebilir.

Sistemdeki tüm kullanıcılar için genel bilgiler ve varsayılan kullanıcı bilgilerini içerir.

Registry bir ikilik veri tabanıdır. Registry editor uygulaması tarafından yada sadece kod yardımı ile değiştirilebilir. Regedit.exe windows gözatıcısı tarzında (Aşağıdaki Şekilde gösterildiği gibi solda anahtarların listesi sağda anahtarların değerleri ) registry hiyerarşisini gösterir. Regedit Registry'i aramanızı Registry bilgilerini görmenizi ve registry'i değiştirmenizi sağlar.

Regedit Registry anahtarlarını ve verileri gösteriyor Registry verileri Hangi verileri registry'de tutarız? Tabi ki bu uygulamanızın ne yaptığına bağlı. Aşağıda bazı genel tutulan bilgiler bir listesini görüyorsunuz.

Uygulamanın son boyutu ve pozisyonu Uygulamanın durumu(normal büyük yada simge durumunda) Child pencerelerin son durumu.

En son açılan dosyaların yolları Kullanıcı ayarları Dosya yerleri Uygulamada belirtilen özel maddeler

Son madde uygulamanız için herhangi bir özel veriyi tutabilir. Örnek olarak Delphi'nin Kullanıcı seçimlik ayarları da registry'de tutulur. Bu bilgi derleyici ayarları, bağlayıcı ayarları,düzenleyici ayarları,form tasarım ayarları,öğe paleti ayarlarını vs. içerir. Hangi veriyi Registry'de tutmak istediğiniz sadece size bağlı.

Bir noktaya dikkatinizi çekmek isterim; Kaliteli uygulamalar kullanıcının hayatını kolaylaştırmak için Registry'i kullanırlar. Örneğin uygulamada bir dosya açarsam bir dahaki dosya açışımda dizin iletişim kutusunun varsayılan dizin olarak o dizini belirlemesini isterim. Registry bu tür verileri kaydetmeyi ve tekrar çağırmayı kolaylaştırmıştır.

Tregistry VCL Registry ile çalışmak için TRegistry sınıfını ortaya koymuştur. TRegistry anahtar yaratmak,anahtarları açmak,veri yazmak veri okumak, anahtarları silmek, anahtarları kaldırmak gibi işler yapar. TRegistry şu veri tiplerini sağlar.

Binary data(Kullanıcı-tanımlı) Boolean(bool) Currency(Currency sınıfı) Date(TDatetime Sınıfı) Float(float yada Double) İnteger(int) String (AnsiString Sınıfı) Time(TDatetime sınıfı)

Registry gerçekte 3 tip veri tutar: string, integer ve binary. VCL diğer veri tipleri için gerçek tipleri değişikliğe uğratır. Örneğin VCL currency,Date,Datetime,Float ve Time veri tiplerini binary data tipinden oluşturur.ve registry'de öyle tutar. bu adımlar size açık endişelenmeyin fakat farkında olun.

Anlattığımız bu veri tipleri kullanılabilir, pek çok configrasyon değerini string olarak tutma imkanına da sahipsiniz. hatta integer verilerinizi bile. Eğer Delphi için yapılan Registry girişlerine bakarsanız boolean değerler tıpkı bir string gibi tutulmuştur. Hangi metodu kullanacağınız size bağlı. Tregistry size anlattığımız veri tiplerini okuma ve yazma metotları sağlar. String veriyi okuma metoduna ReadString yazmaya WriteString denilir ve bu her veri tipi için böyle devam eder gider.

Anahtarları oluşturmak Registry ile çalışırken ilk öğrenmeniz gereken anahtar oluşturmaktır. TRegistry'yi kullanmak için ilk önce yapmanız gereken kullanacağınız formun uses bölümüne Registry yazmak olacak tıpkı aşağıdaki örnekte olduğu gibi:

Uses Windows, Messages, SysUtils, Classes, Graphics, Controls, Forms, Dialogs, Menus, StdCtrls, Registry;

Şimdi bir anahtar oluşturabiliriz.

MyRegistry := TRegistry.Create;

MyRegistry.OpenKey('

Settings', True); MyRegistry.Free;

Bu örnek kodda açıklamamız gereken bir kaç şey var. ilk önce Tregistry sınıfından bir nesne oluşturduk. TRegistry nesneniz oldu zaman Openkey metodunu kullanarak aynı anda hem oluşturabilir hem de açabilirsiniz. Eğer OpenKey'in son parametresine True Değeri verirseniz. VCL'e Eğer yoksa bunu oluşturmasını söylemiş olursunuz.

Settings adında bir anahtar oluşturduğumuzu görüyorsunuz. Fakat bu anahtar nereye oluşturuluyor? cevabı Tregistry'nin içinde yatıyor. Tregistry HKEY\_CURRENT\_USER anahtarını varsayılan olarak belirlemiştir. Genelde anahtarı değiştirmeye pek ihtiyaç duyulmaz ama kullanmak için kök anahtarın da ismini yazmanız gerekir.

Örneğimizde Settings anahtarı HKEY\_CURRENT\_USER

Myapp'ın içinde oluşturulacaktır. Bu gerçek Registry kullanımında yeni bir açı ortaya koyar. Software anahtarı uygulamalar için kök anahtardır. Software altında uygulamanızın ismiyle bir anahtar yaratmalısınız. Bu anahtarın altında uygulamanıza ait verileri tutabilir yada yeni alt-anahtarlar oluşturabilirsiniz. Regedit'i boş verip Software anahtarına bakarsak mutlaka bilgisayarınızda bulunan programlarını pek çoğunun listesini göreceksiniz. Mesela delphi'nin anahtarı HKEY\_CURRENT\_USER

4.0. dır. Registry'de bilgilerinizi tutarken mutlaka böyle bir yöntem izlemeye özen gösterin. Böylece elle değiştirilmesi gereken anahtarlarda kullanıcılarınız size teşekkür edecektir.

Createkey metodu kullanıldığında sadece anahtarı oluşturur anahtarı açmaz. Bu yüzden CreateKey'in ardından openkey'i kullanırız.

En son olarak Closekey'i çağırmamız gerekiyor.Fakat dikkatinizi çektiyse hiç kullanmadım çünkü bunu benim yerime TRegistry'nin Destructor'ü yapıyor.CloseKey'i başka bir anahtarı kullanacağımız zaman kullanmalıyız. Unutmayın ki Registry'de Sadece bir tane açık anahtar bulunabilir.

Okumak Yazmak Anahtarı yarattıktan sonra içinne herhangi bir veri girebilirsiniz. Uygulamanız sonra bu veriyi okuyacak ve uygun şekilde kullanacaktır. WriteXXX metotlarıyla bir veri nesnesi oluşturabilirsiniz. Tıpkı aşağıdaki örnekte olduğu gibi:

MyRegistry := TRegistry.Create

MyRegistry.OpenKey('

Settings', True) MRURegistry.WriteString('LastFile','myfile.txt') MRURegistry.WriteString('LastDirectory','C:

') MRURegistry.WriteString('Data',1) MyRegistry.Free

Yukarıdaki örnekte bir anahtar yaratıp üç tane veriyi bu anahtar altına depoladık. Gördüğünüz gibi Settings anahtarı üç veri nesnesi bulundurmakta bunlar Data,LastDirectory,LastFile. Bu bir kural değildir. Regedit otomatikman veri nesnelerini sıralar ve verilerinize kolayca erişmenizi sağlar.

Registry'den okumak çok basit bir işlemdir. Örneğin son kullanılan dosyayı istiyorsunuz.Aşağıdaki kod bunu size anlatır.

Var FileName: String; MyRegistry := TRegistry.Create;

MyRegistry.OpenKey('

Settings', True); FileName := MyRegistry.ReadString("LastFile"); MyRegistry.Free;

Gördüğünüz gibi Registry'ye ulaşmak ve onu kullanmak epeyce kolay sizde artık uygulamalarınızı buna göre ayarlarsanız Kullanıcılarınıza çok büyük kolaylıklar sağlamış olursunuz. Kolay gelsin.

Windows 95 işletim sisteminde sistem kaydını geri yüklemek Windows 95 işletim sisteminde registry WINDOWS klasöründe bulunan SYSTEM.DAT ve USER.DAT dosyalarıdır. Sistem bilgileri SYSTEM.DAT dosyasında, kullanıcı ayarları USER.DAT dosyasında tutulur. Sistem kaydının bozulması ihtimaline karşı SYSTEM.DA0 ve USER.DA0 (DAsıfır) adlı yedeklerden yararlanlır. Windows kurulumu yapıldığı andaki ayarları içeren SYSTEM.1ST dosyası da ana klasörde eğer kullanıcı tarafından silinmemişse bulunabilir (1ST uzantısı first kelimesinden geliyor). Eğer system kaydı yedekleriyle birlikte tahrip olursa SYSTEM.1ST dosyası sistemi kurtarmak için ilk akla gelendir (son çare değil). Windows 95 registry dosyalarının yedeklerini geri yüklemeniz gerektiğinde aşağıdaki işlemleri yapmalısınız :

Bilgisayarınızı komut isteminde açın Windows klasörüne geçin Aşağıdaki komutları yazın : ATTRIB -r -s -h SYSTEM.DAT ATTRIB -r -s -h SYSTEM.DA0 ATTRIB -r -s -h USER.DAT ATTRIB -r -s -h USER.DA0 REN SYSTEM.DAT SYSTEM.OLD REN SYSTEM.DA0 SYSTEM.DAT REN USER.DAT USER.OLD REN USER.DA0 USER.DAT Ardından bilgisayarınız yeniden başlatın. Umarım istediğiniz sonucu alırsınız. Eğer işler yolunda gitmezse OLD uzantılı dosyaları geri yükleyebilir ya da SYSTEM.1ST yi SYSTEM.DAT adıyla yeniden adlandırıp WINDOWS klasörüne kopyalayabilirsiniz. O aşamada USER.DAT'ı fazla düşünmeyin.

Windows 98 işletim sisteminde sistem kaydını geri yüklemek Windows işletim sisteminde işler çok daha kolay. SCANREG uygulaması sayesinde registry dosyaları otomatik olarak yedeklenmektedir. En fazla beş adet yedek dosyası tutulur. Bu dosyalar CAB uzantısıyla sıkıştırılmış olarak kaydedilmektedir. Herhangi bir yedeği geri yüklemek istediğinizde aşağıdaki işlemleri yapmalısınız :

Bilgisayarınızı komut isteminde açın SCANREG /RESTORE komutunu verin Ekrana gelen listede çok eski olmayan ve Windows'u başlatabilmiş bir yedeği seçin Ekrandaki direktifleri takip edin.

Büyük ihtimalle bilgisayarınız yeniden başladığında bir sorun çıkmayacak. Zaten Windows 98 de kayıt problemleri büyük oranda çözülmüş durumda.

Windows NT 4.0 işletim sisteminde sistem kaydını geri yüklemek Birden fazla yöntem sıralanabilir. Örneğin boot esnasında LastKnownGood konfigürasyonu yükleyerek bir önceki başarılı logon işlemindeki ayarları geri yükleyebilirsiniz. Windows NT 4 işletim sisteminde ControlSet'in 2 yedeği tutulmaktadır. Yedekleme işlemi bir kullanıcı sisteme lokal olarak oturum açtığında yapılır.

Eğer bir teyp sürücünüz varsa, işiniz kolay. Geri yükleme esnasında daha önceden yedeklediğiniz registry bilgilerinin geri yüklenmesini isteyebilirsiniz.

Bir diğer yöntem ERD (Emergency Repair Disk) kullanmak. RDISK /S komutuyla sistemin son durumuna ait bilgilerin

Repair klasörüne kaydedilmesini sağlayın. İşlem tamamlandıktan hemen sonra, kaydedilen bu bilgilerin bir diskete kaydedilmesi için sizi ikaz edecek. Boş bir disket takarak devam edin. Bu disketteki bilgileri sürekli olarak güncel tutmaya çalışmalısınız. Registry bilgilerini geri yüklemek için önce üç adet NT Kurulum disketine ihtiyacınız var - çünkü ERD bir açılış disketi değil. Eğer elinizde disketler yoksa kurulum dosyalarının bulunduğu klasörde WINNT /OX komutuyla bu disketleri hazırlayabilirsiniz. Sistemi birinci disketle açın. Sorulduğunda R harfini tuşlayarak REPAIR (Onarım) yapmak istediğiniz belirtin. Aşağıdaki gibi bir menü ekrana gelecek :

\[X\] Inspect Registry Files \[ \] Inspect startup environment \[ \] Verify Windows NT system files \[ \] Inspect boot sector

Kontrol etmek istediğiniz bölümleri işaretleyin. Inspect Registry Files seçeneği için ekrana registry bölümleri gelecek. Kontrol etmek (geri yüklemek) istediklerinizi işaretleyerek devam edin.

\[X\] SYSTEM \[X\] SOFTWARE \[X\] DEFAULT \[X\] NTUSER.DAT \[X\] SECURITY \[X\] SAM İŞLEM TAMAM.

NOT: Eğer çok fazla sayıda kullanıcı hesabınız varsa SAM dosyanız çok büyük olabilir (En çok 40 MByte). Yada çok fazla yazılım kurmuşsanız SOFTWARE dosyası çok büyük olabilir. Böyle olunca toplamda registry dosyalarının büyüklüğü bir disket kapasitesini (1.44MB) aşabilir. Bu nedenle NT kurulumunu tamamladıktan sonra oluşturacağınız ilk repair diskini saklamanızda fayda var. Çünkü ERD bir diskete sığmak zorunda.

Windows 95, 98 ve Windows NT 4.0 registry da değişiklik yapmak

Windows'un standart simgelerinin değiştirilmesi

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

cool.dll,11 ;Windows gezgini sol panelde kapalı klasör simgesi "4="C:

cool.dll,18 ;Windows gezgini sol panelde açık klasör simgesi "5="C:

cool.dll,29 ;Ağ sürücüsü - hazır değil "11="C:

cool.dll,4 ;Başlat menüsü - Programlar "20="C:

cool.dll,2 ;Başlat menüsü - Belge menüsü "21="C:

cool.dll,6 ;Başlat menüsü - Ayarlar "22="C:

cool.dll,15 ;Başlat menüsü - Yardım "24="C:

cool.dll,5 ;Başlat menüsü - Çalıştır "25="C:

cool.dll,33 ;Başlat menüsü - Askıya al (95 için) "26="C:

cool.dll,32 ;Başlat menüsü - Çıkart (Docking Station) "27="C:

cool.dll,7 ;Başlat menüsü - Bilgisayarı kapat "28="C:

cool.dll,34 ;Paylaşım işareti "29="C:

shell32.dll,30 ;Kısayol işareti "31="C:

cool.dll,20 ;Geri Dönüşüm Kutusu - Boş "32="C:

cool.dll,21 ;Geri Dönüşüm Kutusu - Dolu "33="C:

cool.dll,27 ;Bilgisayarım - Çevirmeli ağ "35="C:

cool.dll,12 ;Bilgisayarım - Denetim masası "36="C:

cool.dll,24 ;Başlat menüsü - program grupları "37="C:

cool.dll,19 ;Bilgisayarım - Yazıcılar "38="C:

cool.dll,14 ;Denetim masası - Yazıtipleri klasörü "40="C:

cool.dll,26 ;AudioCD Açıklama:Burada cool.dll simgelerin bulunduğu kitaplıktır. DLL ya ICL uzantılı dosyaları kullanırken önce dosya adını, daha sonra istediğiniz simgenin kaçıncı simge olduğunu belirtmeniz gerekiyor. Simgeleri görmek için bir kısayol yaratarak, kısayol özelliklerindeki simge değiştir seçeneğini kullanabilirsiniz.

Sürücülerin gizlenmesi - gösterilmesi

REGEDIT4 \[HKEY\_CURRENT\_USER

Explorer\] "NoDrives"=hex:01,00,00,00 Açıklama:Koyu renkli kısımda yapılabilecek değişiklikler : 00 açık (Bütün sürücüler kullanılabilir) 01 -a (A sürücüsü Windows Gezgini'nde yer almaz) 02 -b 03 -ab 04 -c 05 -ac 06 -bc 07 -abc 08 -d 09 -ad 10 -e 20 -f Bu bilgiyi registrye girdikten sonra Windows'u yeniden başlatmalısınız.

Ekran koruyucusunun parolasını iptal etmek

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

SCRSAVE\] "Description"="Windows Ekran Koruyucu" "ProviderPath"="password.cpl" "ChangePassword"="none" "GetPasswordStatus"="PPGetPasswordStatus" Açıklama:Parola korumalı kutusunu onayladığınızda Değiştir düğmesi çalışmayacaktır. Eski haline getirmek için aşağıdaki satırı değiştirin. "ChangePassword"="PPChangePassword"

Windows açılışında mesaj göstermek

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Winlogon\] "DontDisplayLastUserName"="0" "LegalNoticeCaption"="BURAYA BAŞLIĞI YAZIN" "LegalNoticeText"="GÖRMEK İSTEDİĞİNİZ MESAJ" Açıklama:Eğer DontDisplayLastUserName'e 0 değeri atanırsa Windows'a oturum açan son kişinin adı otomatik olarak gözükmez. (Göstermesi için 1 değeri kullanın)

Başlat menüsünde daha hızlı açılan menüler

REGEDIT4 \[HKEY\_CURRENT\_USER

Desktop\] "MenuShowDelay"="1" Açıklama:MenuShowDelay 1 ile 100 arasında bir sayıdır. Bu değer küçüldükçe bekleme süresi de azalır.

Masaüstündeki özel simgeler

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

NameSpace\] \[HKEY\_LOCAL\_MACHINE

{9EAC43C0-53EC-11CE-8230-CA8A32CF5494}\] @="Winamp"

Özel klasörler için simgeler Özel klasörler için kısayol oluşturmak yerine orjinal simgelerini kullanabilirsiniz. Önce yeni bir klasör oluşturun, ardından aşağıdaki gibi isimlendirin.

Yöntem : Herhangi\_bir\_ad.{anahtar} Denetim.{21EC-2020-3AEA-1069-A2DD-08002B30309D} Dial-up.{992CFFA0-F557-101A-88EC-00DD010CCC48} Yazıcılar.{2227A280-3AEA-1069-A2DE-08002B30309D} Komşular.{208D2C60-3AEA-1069-A2D7-08002B30309D} Bilgis.{20D04FE0-3AEA-1069-A2D8-08002B30309D} Çöp.{645FF040-5081-101B-9F08-00AA002F954E} Fontlar.{BD84B380-8CA2-1069-AB1D-08000948F534}

Görüntü özellikleri ve registry için kısıtlamalar

\[HKEY\_USERS

System\]

DisableRegistryTools

1 değeri atarsanız Registry erişimini"KENDİNİZE DE" kapatmış olursunuz.

NoDispBackgroundPage

1 değeri atarsanız görüntü özelliklerinde Artalan sekmesini göstermez.

1 değeri atarsanız görüntü özelliklerinde Ekran Koruyucu sekmesini göstermez.

NoDispAppearancePage

1 değeri atarsanız görüntü özelliklerinde Görünüm sekmesini göstermez.

1 değeri atarsanız görüntü özelliklerinde Ayarlar sekmesini göstermez.

1 değeri atarsanız görüntü özelliklerine girilemez.

Açıklama:Windows 98' de registrydeki yeri değişmiş --> Software

Setup altında ama nerde bulabilmiş değilim. DeskSaysNoPeekingItsASurprise diye bir ipucu da yakaladım. Büyük ihtimalle burada bir süpriz yumurta var.

INFRA CD ROM'u olanlara büyük kolaylık Aşağıdaki yapıyı kullanarak uygulamaları (9 taneye kadar) INFRA menüsüne ekleyebilirsiniz. Belki biraz fantazi ama gerçekten kullanışlı.

REGEDIT4 \[HKEY\_USERS

Creative Infra Suite

Creative Infra Suite

App0\] "Description"="iNFRA Multimedia Deck" "Command Line"="C:

MCU.EXE" "Parameters"="" \[HKEY\_USERS

Creative Infra Suite

App1\] "Description"="iNFRA Web" "Command Line"="C:

WRMTBRS.EXE" "Parameters"="" \[HKEY\_USERS

Creative Infra Suite

App2\] "Command Line"="C:

CALC.EXE" "Description"="Hesap Makinası" "Parameters"="" \[HKEY\_USERS

Creative Infra Suite

App3\] "Command Line"="C:

RUNDLL32.EXE" "Description"="Internete bağlan" "Parameters"="rnaui.dll,RnaDial Bağlantım" Açıklama:Benim eklediğim App3 adlı girdi browser'ı başlatmadan Bağlantım bağlantısını çeviriyor.

Win NT registry değişiklikleri

Başlamadan önce birkaç önerim olacak. İmla ve notasyon çok önemlidir. Ayrıca değerleri manuel olarak değiştirirken dikkatli olmalısınız. Eğer RegEdit yada RegEdt32 kullanıyorsanız yaptığınız değişikliği geri almak için bir Undo seçeneğiniz yok. Son olarak üzerinde değişiklik yapmak istediğiniz anahtar (key) üzerinde değişiklik yapma yetkiniz bulunmalı.

Eğer arama yapmak, registry'nin bir bölümünü (ya da tamamını) export etmek veya anahtar adını kopyalamak isterseniz Regedit'i; anahtarlar üzerinde NT izinlerini düzenlemek yada Regedit tarafından tanınmayan bir değer (value) eklemek isterseniz Regedt32'yi kullanmalısınız.

Yeni başlayanlara Registry'i doğrudan düzenlemeye başlamadan önce Control Panel'deki appletler, System Policy Editor, TWEAKUI gibi grafik arayüzü bulunan araçları tercih etmelerini öneririm. Registry'de yapılan değişiklikler sisteminizin çökmesine ya da performans kaybına neden olabilir.

Windows NT registry'sinde kullanılan veri (value) türlerini hatırlayalım :

binary (REG\_BINARY) string (REG\_SZ) DWORD (REG\_DWORD) multistring (REG\_MULTI\_SZ) expandable string (REG\_EXPAND\_SZ) full resource descriptor (REG\_FULL\_RESOURCE\_DESCRIPTOR)

ActiveWindowTracking (MOUSE):UNIX'de olduğu gibi, bir pencereyi öne getirmek için fare imlecini üzerine konumlandırmanız yeterli oluyor. Bu değişiklikten sonra sistemi yeniden başlatmanız gerekiyor.

REGEDIT4 \[HKEY\_CURRENT\_USER

Mouse\] "ActiveWindowTracking"=dword:00000001

SnapToDefaultButton (MOUSE) İletişim pencerelerinde fare imlecini varsayılan düğme (default button) üzerine konumlandırıyor.

REGEDIT4 \[HKEY\_CURRENT\_USER

Mouse\] "SnapToDefaultButton"="1"

SecondLevelDataCache (HARDWARE) L2 önbellek özellikle uygulama sunucusu (application server) olarak kullanılan sistemlerde performans üzerinde belirleyici rol oynar. Varsayılan olarak NT HAL anakart üzerindeki L2 önbellek miktarını tespit etmeye çalışır. Bunda bazen başarılı olur, bazen L2 bellek miktarını tespit edemez. Örneğin benim kullandığım sistem ASUS P2B anakart üzerinde Pentium II 350 işlemci olmasına rağmen önbellek miktarı tespit edilememişti. Önce HKLM

Memory Management anahtarındaki SecondLevelDataCache (REG\_DWORD) değerini kontrol edin. Mesela eğer 512 KB cache varsa burada decimal olarak 512 ya da hex olarak 0x200 olmalı. Unutmayın, yanlış L2 değeri belirtmeniz durumunda sisteminiz tutarsız (unstable) olabilir.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Memory Management\] "SecondLevelDataCache"=dword:00000200

NoPopUpsOnBoot & ErrorMode (HARDWARE):NT boot işlemi esnasında açılış esnasında tespit edilen her tür problemin ekrana görüntülenmesi zaman zaman çok can sıkıcı olabilir. Bu hata mesajlarının ekranda görüntülenmesini önlemek için

REGEDIT4 \[HKEY\_CURRENT\_USER

Windows\] "NoPopUpsOnBoot"=dword:00000001

Boot işleminin hemen sonrasında, aygıt sürücüleri ve servislerin yüklenmesi esnasında karşılaşılabilecek hataların ekranda görülmesini önlemek için (hala Event Log dan inceleyebilirsiniz) ErrorMode değerleri :

0 system ve application error' ları göster (varsayılan) 1 sadece application error' ları göster (log edilmeye devam edilecek)) 2 tüm hata mesajlarını gizle (log edilmeye devam edilecek)

REGEDIT4 \[HKEY\_CURRENT\_USER

Windows\] "ErrorMode"="0"

ClearPageFileAtShutdown (HARDWARE) Sisteminizi kapattığınızda disk üzerindeki sanal bellek alanını (pagefile) temizlemek için

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Memory Management\] "ClearPageFileAtShutdown"=dword:00000001

AutoAdminLogon (Winlogon) Sisteminiz açıldığında otomatik olarak logon olmanızı sağlayan bu değerlere dikkat. Registry üzerinde yeterli yetkiye sahip birisi bu hesabın parolasını öğrenebilir.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Winlogon\] "AutoAdminLogon"="1" "DefaultUserName"="kullanıcı adını yazınız" "DefaultPassword"="kullanıcı parolası" "DefaultDomainName"="DOMAIN adı"

DontDisplayLastUserName (Winlogon) Administrator hesabını yeniden adlandırdınız ve diğer kullanıcılar tarafından öğrenilmesini istemiyorsunuz. Logon esnasında son işlem yapan kullanıcı hesabının varsayılan olarak görüntülenmesini önleyebilirsiniz.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Winlogon\] "DontDisplayLastUserName"="0"

PasswordExpiryWarning (HESAPLAR) Diyelim ki Account Policy'niz kullanıcıların her ay parolalarını değiştirmesini gerektiriyor. Ancak kullanıcıları süre dolduğunda değil, mesela sürenin dolmasına 3 gün kala yeni bir parola girmeleri için uyarmak istiyorsunuz. Windows NT 4 altında bu işlemi aşağıdaki şekilde yapabilirsiniz :

1. Registry Editor (Regedt32.exe) yi çalıştırın 2. HKEY\_LOCAL\_MACHINE dalından, aşağıdaki anahtarı bulun:

Winlogon 3. Aşağıdaki değeri ekleyin : PasswordExpiryWarning: REG\_DWORD: <number of days> NOT : <number of days> yerine gün cinsinden bir rakam girmelisiniz. Yukarıdaki örnek için 3. 4. Editörü kapatıp çıkın. İŞLEM TAMAM DİKKAT: Registry Editörün bilinçli kullanılmaması sisteminizin doğru çalışmamasına ya da hiç açılmamasına sebep olabilir. \[HKEY\_LOCAL\_MACHINE

Winlogon\] "PasswordExpiryWarning"=dword:0000000e

DisableSavePassword (DUN) Çevirmeli bağlantılarınızda parolanın kaydedilmesini engeleyebilirsiniz.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

RasMan\] "DisableSavePassword"=dword:00000001

MaintainServerList (Browse) Eğer ağınızda bulunan herhangi bir NT Server'ın master browser olmasını istemiyorsanız, bütün seçimleri kaybetmesini sağlayabilirsiniz.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Parameters\] "MaintainServerList"="No" "IsDomainMaster"="FALSE" PowerdownAfterShutdown (Power Management) Windows NT'nin aynı Windows 98 de olduğu gibi (ATX güç kaynağı kullanıldığında) shutdown işleminden sonra powerdown olması için aşağıdaki işlem sırasını kullanabilirsiniz. Yapmanız gereken Windows NT 4 ile gelen Hardware Abstraction Layer (HAL) i değiştirmek.(NOT : Farklı sistemlerde çalışmayabilir. Ben ASUS P2B anakart ve SP5 ile problemsiz denedim) 1. SP5 içerisindeki HAL.DLL.SOFTEX dosyasını kopyalayın İpucu : Service Pack'i install etmeden açmak için /X parametresini kullanabilirsiniz 2. Bilgisayarı DOS yada Windows 9x ortamında açarak orjinal HAL.DLL dosyasının bir yedeğini alın İpucu : (

SYSTEM32 klasöründe) 3. HAL.DLL.SOFTEX dosyasını yeniden adlandırarak HAL.DLL'nin yerine kaydedin 4. Windows NT'ye logon olarak registryde şu düzenlemeleri yapın

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Winlogon\] "PowerdownAfterShutdown"="1"

Servislerin kapanış süresini kısaltmak Windows NT kapanırken her servisin sonlandırılması için 20 sn bekler. Bu bekleme süresini kısaltarak Windows NT nin daha hızlı kapanmasını sağlayabilirsiniz.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Control\] "WaitToKillServiceTimeout"="20000" Bu değer bir servisi sonlandırmak için ayrılan bekleme süresini milisecond cinsinden belirler. Her servise sonlanması için yeteri kadar süre bırakmaya dikkat edin. Aksi takdirde cache'de bulunan verilerin yazılmasını engelleyebilirsiniz. SQL, Exchange, ve DNS gibi kritik sunucularda kesinlikle bekleme süresini azaltmamanızı tavsiye ederim.

Görevleri otomatik sonlandırmak Windows NT her uygulamanın sonlanması için bir süre tanır. Bu süre sonunda cevap vermeyen uygulamaları sonlandırmadan önce bizi uyararak, beklemek ya da sonlandırmak arasında bir seçim yapmamızı ister. Bekleme süresini (Timeout) kısaltarak ve AutoEndTasks değerini 1 yapmak suretiyle uygulamaları daha hızlı sonlandırabilirsiniz.

REGEDIT4 \[HKEY\_CURRENT\_USER

Desktop\] "AutoEndTasks"="1" "HungAppTimeout"="5000" "WaitToKillAppTimeout"="20000"

Konsolda dosya adlarını otomatik tamamlamak:Konsolda (Command Prompt) çalışırken UNIX shell ortamında olduğu gibi \[TAB\] tuşuna basarak dosya adlarını tamamlamak mümkün

REGEDIT4 \[HKEY\_CURRENT\_USER

Command Processor\] "CompletionChar"=dword:00000009 DWORD değerine 0x09 atadığınız takdirde tamamlama karakteri olarak \[TAB\] tuşu kullanılır. Bu amaçla bir başka tuş kullanmak isterseniz o karakterin Hex değerini yazmanız yeterli olacaktır.

CD lerin otomatik çalıştırılmasını önlemek:CD okuyucunuza yeni bir CD takdığınızda otomatik olarak çalıştırılmasını önleyebilirsiniz.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Cdrom\] "AutoRun"=dword:0

Ağda üzerinde ortak bir Sık Kullanılanlar klasörü oluşturmak:Internet Explorer ve Microsoft Office, kullanıcıların ihtiyaç duyduğu doküman ve kısayollara ulaşmak için Favorites (Sık Kullanılanlar) klasörünü kullanılır. Ağ üzerindeki bütün kullanıcıların ortak bir Favorites klasörü kullanmasını sağlayabilirsiniz.

Önce bir sunucuda ortak kullanılacak klasörü yaratın ve paylaştırın. Eğer dosya sistemi olarak NTFS kullanıyorsanız gerekli erişim haklarını da düzenlemelisiniz. Ardından ortak klsörü kullanmak istediğiniz her istemcinin registry'sinde aşağıdaki düzenlemeyi yapın:

REGEDIT4 \[HKEY\_CURRENT\_USER

User Shell Folders\] "Favorites"="

Favorites" Favorites'e atadığınız değer paylaştırdığınız klasörün tam yolu (UNC a göre) olmalıdır. Örneğin

file://SERVERx/Favorites

gibi. Eğer istemciyi kullanan herkesin paylaştırılan Favorites klasörünü kullanmasını isterseniz değişikliği HKEY\_USERS

.DEFAULT altında yapmalısınız.

REGEDIT4 \[HKEY\_USERS

User Folders\] "Favorites"="

Sistemin çöktüğü anı yakalamak yada alert üretmek:Sisteminiz çöktüğünde crach log'a ilave olarak bir Administrative Alert oluşturulmasını sağlamak isterseniz, SendAlert değerini 1 yapmanız yeterli olacaktır.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

CrashControl\] "SendAlert"="1" Eğer sistemin çoktüğü anı tam olarak öğrenmek isterseniz, bu anın event log'a yazılmasını sağlayabilirsiniz.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

CrashControl\] "LogEvent"="1"

Pencere animasyonlarını durdurmak:Windows NT, Windows 95 de olduğu gibi pencerelerin açılması ve kapanması esnasında "zooming" efekti kullanır. Bu efekti durdurmak pencerelerin daha hızlı açılıp kapanmasını sağlar.

REGEDIT4 \[HKEY\_CURRENT\_USER

WindowMetrics\] "MinAnimate"=dword:00000000

Yetersiz disk alanı ikaz seviyesini belirlemek:Sabit diskinizde yeterli boş disk alanı kalmadığında, Windows NT bu durumu bir mesaj kutusunda bildirir. Bu ikaz için limit, varsayılan olarak disk alanının %90 ıdır. Büyük hacimli bir sabit disk kullanırken %10 yeterli boş alan olmasına rağmen, Windows NT boş alanı byte cinsinden değil de yüzde cinsinden değerlendirdiği için hala yeterli görmeyecektir. Aşağıdaki düzenleme ikaz seviyesini %5 e düşürmektedir.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Parameters\] "DiskSpaceThreshold"=dword:00000005 DiskSpaceThreshold değeri 0 ile 99 arasında olmalıdır. Örneğin dword:00000005, boş disk alanının %5 ine işaret eder.

Uzun dosya uzantılarını kullanmak:Her ne kadar Windows 95 uzun dosya adlarını desteklese de bu uzun dosya uzantıları için doğru değildir. Örneğin medical.doc, medical.doctor, ve medical.doctrine hep aynı şekilde gösterilir. NTFS de böyle bir sınırlama olmadığı için daha uzun dosya uzantıları kullanılabilir.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

FileSystem\] "Win95TruncatedExtensions"=dword:00000001 Win95TruncatedExtensions değeri varsayılan olarak 0 dır. Değeri 1 yaptıktan sonra bilgisayarınızı tekrar başlatmalısınız.

NTFS Partisyonlarda son erişim tarihinin tutulmasını önlemek:NTFS partisyonlarda her dosya ve klasöre son erişim zamanlarının yazılmasını önleyerek performans artışı sağlayabilirsiniz.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

FileSystem\] "NtfsDisable8dot3NameCreation"=dword:00000001 Bu düzenleme "Last modified" (son değişiklik tarihi) üzerinde herhangi bir etki yapmaz.

NT WS da kullanıcı hesaplarının kaydedilmesini sınırlamak:NT workstationlarda varsayılan olarak oturum açan son 10 kullanıcı hesabına dair bilgiler kaydedilir. Böylelikle hedeflenen kullanıcıların ağa daha hızlı oturum açmasını sağlamak ve etki alanı sunucusunun (PDC/BDC) daha az logon isteğiyle uğraşmasını sağlamaktır.

Bu uygulamanın bir başka sonucu, etki alanı sunucusu ağda olmasa bile kullanıcının ağa oturum açabilmesidir. (Hem iyi, hem kötü!) Daha fazla güvenlik için aşağıdaki düzenlemeyi kullanabilirsiniz.

REGEDIT4 \[HKEY\_LOCAL\_MACHINE

Winlogon\] "CachedLogonsCount"="0" Eğer son 15 kullanıcının hesap bilgilerinin kaydedilmesini istiyorsanız "CachedLogonsCount"="15" olmalıdır.

endtask.gif (4484 bytes)

DocumentSummaryInformation

Varsayılan Paragraf Yazı Tipi

HTML Önceden Biçimlendirilmiş

Önceden Biçimlendirilmiş

Gövde Metni Girintisi

Gövde Metni Girintisi 3

Gövde Metni Girintisi 2

---
*Kaynak: `AĞ KURULUMU/AĞ KURULUMU.doc`*
