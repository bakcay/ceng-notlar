# OSI Referans Modeli

## ** ****OSI REFERANS MODELİ**

**(OSI-Open Systems Interconnection-Açık Sistem Bağlantısı)**

Bilgisayarlar arası iletişim başladığından beri farklı bilgisayar sistemlerinin birbirleri arasındaki iletişimin sağlanması büyük bir problem olmuş ve bu problemi çözebilmek için çeşitli çalışmalar yapılmıştır. 1980’li yılların başında ISO( Uluslar arası Standartlar Organizasyonu) piyasadaki bilgisayarlar arası iletişim üzerine ürünler çıkaran şirketler arasındaki iletişimi bir standart üzerine oturtmak ve farklı standartlar arası uyumsuzlukları ortadan kaldırmak amacıyla OSI (Open Systems Interconnection) referans modelini ortaya çıkarmıştır.

OSI referans modeli temelde bir network ü oluşturan bilgisayarların iletişim problemlerini kuramsal olarak 7’ye böler. Diğer bir deyişle OSI referans modeli 7 katmanlı bir ağ sistemidir. Bu 7 katmanda her bir katman farklı işlevlere ve farklı bir isme sahiptir.

Fiziksel Katman

Veri İletim Katmanı

Ağ Katmanı

Ulaşım Katmanı

Oturum Katmanı

Sunum Katmanı

Uygulama Katmanı

Kısaca OSI modeli bir bilgisayarda çalışan uygulama programının iletişim ortamı üzerinden başka bir bilgisayarda çalışan diğer bir uygulama programı ile olan iletişiminin tüm adımlarını tanımlar. En üst katmandaki bilgi alt katmanlara inildikçe makine diline dönüşür ve sonuç olarak 1 ve 0’lardan ibaret elektrik sinyalleri halini alır.

Uygulama protokolü

Sunum Protokolü

Oturum Protokolü

Ulaşım Protokolü

Haberleşme Altağ Sınırı

**OSI Referans Modeli Mimarisi**

OSI referans modeli 7 tabakalı hiyerarşik bir yapıya sahiptir. Bu yapı oluşturulurken aşağıdaki prensipler uygulanmıştır.

Değişik seviye bir ayrım gerektirdiğinde bir tabaka oluşturulmalıdır.

Her tabaka iyi tanımlanmış bir fonksiyonu yerine getirmelidir.

Her tabakanın fonksiyonu uluslar arası standartlaştırılmış protokoller arasından seçilmelidir.

Tabaka sınırları arabirimler arası bilgi akışını en aza indirecek şekilde seçilmelidir.

Tabakaların sayısı belirgin fonksiyonların aynı tabakalar üzerinde atlama yapmayacak kadar geniş mimariyi hantallaştırmayacak kadar az olmalıdır.

| Uygulama Katmanı(Application Layer) |
| --- |
| Sunum Katmanı(Presentation Layer) |
| Oturum Katmanı(Session Layer) |
| Ulaşım Katmanı(Transportation Layer) |
| Ağ Katmanı(Network Layer) |
| Veri İletim Katmanı(Data Link Layer) |
| Fiziksel Katman(Physical Layer) |

**FİZİKSEL KATMAN (PHYSICAL LAYER)**

Verinin fiziksel olarak hat üzerinden iletilmesi için gerekli işlemleri kapsar. Diğer bir deyişle ağın elektriksel ve mekanik karakteristiklerini belirler. Modülasyon teknikleri, çalışma frekansı bu katmanın temel özellikleridir. Örneğin; RS 232C ve V.35 bu katmanın standartları arasındadır.

**Repeater (Tekrarlayıcı): **Tekrarlayıcının ana görevi; kablo, fiber-optik, radyo dalgası gibi bir fiziksel ortamdaki sinyali alıp, kuvvetlendirip başka bir fiziksel ortama iletmektir. Ağların fiziksel büyüklük sınırlarını genişletmek amacıyla kullanılırlar. Teorikte bir bilgisayar ağını sonsuza kadar genişletebilirler. Ancak, çeşitli tasarım sınırlamaları nedeni ile gerçekte bu genişleme belli sınırlar içinde kalmaktadır.

LAN1

Repeater

Repeater

LAN2

LAN3

Temelde bir ağın genişletilmesi amacı ile kullanılan tekrarlayıcılar çok kolay kurulmaları, çok az bakım gerektirmeleri ve fiyatlarının ucuz olması sebepleri ile çok popüler cihazlardır.

**VERİ İLETİM KATMANI (DATA LINK LAYER)**

Bu katmanın temel görevi; verinin fiziksel katmana ulaşım stratejisini belirlemektir. Diğer bir deyişle veri iletim katmanı gönderilecek verinin sayısal işaretlere dönüştürülmesi, verilerin iletimi sırasında hataların sezilmesi ve düzeltilmesi için gerekli algoritmaların kullanıldığı katmandır. Köprü (Bridge) cihazları bu katmanda çalışırlar. Bu katmanda gönderilecek veri çerçevelerine (data frame) ayrılarak sıralı bir şekilde gönderilir. Fiziksel katman bitlerin yapısı ile ilgilenmeden veriyi ilettiği için çerçeve sınırlarını belirleme ve algılama görevi veri iletim katmanına aittir. Bu nedenle her veri çerçevesinin başına ve sonuna özel bit zincirleri yerleştirilir. Bu bit zincirleri veri içinde yer almaz. Bir veri çerçevesinin formu aşağıdaki gibidir.

| Başlık biti | Veri bitleri | Son biti |
| --- | --- | --- |

Data Frame (Veri Çerçevesi)

**Köprü (Bridge):**Köprü cihazları birbirinden bağımsız ve benzer ağ teknolojilerini kullanan iki ağın birbirleriyle bağlantı kurması için kullanılırlar. Köprü, ağdaki tüm trafiği yürütür, tüm veri paketlerini okur, paketin nereden gelip nereye gittiğini inceler. Bu işlemi MAC (Media Access Control)-Ortam Erişim Kontrolü) adı verilen verinin hangi katmandan geldiğini ve nereye gideceğini (destination) bildiren adres numarasıyla yapar. MAC adresi sayesinde ağdaki tüm adresler taranmaz, diğer bir deyişle adres süzme işlemi yaparak veri trafiğinin yoğunluğunu azaltır.

LAN1

LAN2

Bir köprü TCP/IP, XNS gibi farklı iletişim protokollerini kullanarak aynı protokolleri kullanmayan ağlar arasında fiziksel bağlantı sağlayabilse de bu uygulamalar arasında işletilebilirliğini garanti etmemektedir. Bu nedenle köprülü ağlar, protokol çevrimlerinin olmadığı, güvenlik gereksinimlerinin en az olduğu ve gereken tek şeyin basit yönlendirme olduğu durumlarda başarılıdır.

**AĞ KATMANI (NETWORK LAYER)**

Bağlantıyı sağlayan ve yönlendirme ile ilgili işlemleri yürüten katmandır. Bu katmanın en önemli görevi veri paketinin hangi kaynaktan, ne şekilde hedefe yönlendirileceğini belirlemektedir. Bu nedenle düğümlere ağ adresi denen numaralar verilir. Ağ adresini taşıyan veri bloklarına da paket denir. Bir paket, bir düğüm üzerinden geçtiğinde düğüm, üzerinde bulunan yönlendirme tablolarını günceller. Temel protokol kümesi TCP/IP ve yönlendirmeler (router) bu katmanda çalışır.

**Yönlendirici (Router): **Yönlendirici, ağın tüm haritasını tutar ve veri paketinin gittiği hedefe doğru en iyi yolu belirlemek için tüm yolların durumuna bakar. Yönlendirici, farklı fiziksel yapıdaki ve farklı protokolleri çalıştıran yerel alan (LAN) veya geniş alan ağlarının (WAN) birbirleri ile olan bağlantısında güvenle kullanılabilir. Bir yönlendirici, ağ katmanında genel olarak tanımlanmış protokollerle yerel bölge ağlarını geniş bölge ağlarına bağlar. Yönlendiriciler, yönlendirme tablolarına bakarak ağ üzerindeki yolları en etkin şekilde kullanarak veriyi iletirler. Yönlendiriciler kendi yönlendirme tablolarını oluşturduklarından ağ trafiğindeki değişiklikleri hemen ayak uydurarak veri trafiğini dengelerler. Ayrıca ağdaki değişiklikleri tespit eder ve istenmeyen bağlantıları önlerler.

LAN1

X25

TURPAK

**Gateway (Geçit Yolu): **Köprü ve yönlendiricilerden daha yeteneklidirler. OSI modelinin tüm katmanlarında çalışabilirler. Farklı protokoller kullanan ağlar arasında ilişki kurmakla beraber aynı zamanda bir ağdan taşınan verinin diğer ağlarla uyumlu olmasını da sağlarlar. Bu işlem bir ana bilgisayarda bulunan protokol çevirim yazılımıyla yapılır. Internet protokolleri farklı ağlar arasındaki veri aktarımını geçit yolarıyla bağlı alt ağlardan oluşmuş otonom sistem (Autonomous System , AS) gruplarını birbirine bağlayarak yapar. Her AS diğer AS’lere bağlantı sağlayan geçit yolu sunar. Geçit yolları tüm farklı ağları birlikte tutan bir yapıştırıcıdır.

| Uygulama Katmanı |
| --- |
| Sunum Katmanı |
| Oturum Katmanı |
| Ulaşım Katmanı |
| Ağ Katmanı |
| Veri İletim Katmanı |
| Fiziksel Katman |
| Uygulama Katmanı |
| Sunum Katmanı |
| Oturum Katmanı |
| Ulaşım Katmanı |
| Ağ Katmanı |
| Veri İletim Katmanı |
| Fiziksel Katman |
| Uygulama Katmanı |
| Sunum Katmanı |
| Oturum Katmanı |
| Ulaşım Katmanı |
| Ağ Katmanı |
| Veri İletim Katmanı |
| Fiziksel Katman |

**ULAŞIM KATMANI ( TRANSPORTATION LAYER)**

Bu katman gelen bilginin doğruluğunu kontrol eder. Bilginin iletimi sırasında oluşan hataları tespit eder ve bu hataları düzeltmek için çalışır. Yani, bilginin alıcıya her tür hatadan arındırılmış olarak iletilmesini sağlar. Aynı zamanda ulaşım katmanı, oturum katmanı tarafından ihtiyaç duyulan her taşıma bağlantısı için bir sanal ağ bağlantısı oluşturur. Eğer taşıma bağlantısı yüksek bir kapasiteye ihtiyaç duyarsa ulaşım katmanı, birçok ağ bağlantısı oluşturup kapasiteyi arttırmak için veriyi bu bağlantılara paylaştırır. Ayrıca, farklı ağ bağlantılarının oluşturulması, maliyeti arttırdığı durumlarda ulaşım katmanı çeşitli taşıma bağlantılarını bir ağ bağlantısı üzerinde birleştirerek maliyeti azaltabilir.

Bu katman genel olarak uç sistemlerde bulunur. Ve iki uç arasında güvenilir bir iletişim kanalı kurulmasını sağlar.

| Uygulama veya oturum katmanı |
| --- |
| Ağ katmanı |
| Fiziksel Katman |

1.uç düğüm 2.uçdüğüm

| Uygulama veya oturum katmanı |
| --- |
| Ağ katmanı |
| Fiziksel Katman |

Ulaşım katmanı SAP’ları

TSAP

Ulaşım Protokolleri

FB

Ulaşım katmanları arasında karşılıklı aktarılan bilgi birimi Ulaşım Katmanı Veri Birimi (Transport Protocol Data Unit-TPDU) olarak adlandırılır. TPDU’lar paketlere yerleştirilerek ağ içinde taşınır. TPDU içinde TSAP adresi belirtilen üst katmana aktarılır. Bazı uygulamalarda her ulaşım adresi (TSAP) üzerinden farklı tür bir hizmet elde edilebilir.

**TCP Protokolü (Transport Control Protocol-Ulaşım Kontrol Protokolü):**

Bu protokolde alıcı ve gönderici iletişime başlamadan önce iletişim yapma konusunda istek ve onaylarını birbirlerine ileterek anlaşırlar. Özellikle ağ katmanının yeterli güvenliğe sahip olmadığı durumlarda TCP protokolü ile bu güvenlik açığı kapatılmış olur. TCP protokolünü destekleyen her uç düğümde bir TCP modülü bulunur. Bu modül üst katmandan gelen veri bloklarını 64 KB’ı aşmayan TPDU’lara ayırır veya birleştirir. Ve bu TPDU’ları IP datagramları içinde gönderilmesini sağlar. Bu protokolle her uçta 2 16 adet farklı TSAP adresi tanımlanabilir. Bu adresler, port olarak adlandırılır. Uç düğümün 32 bitlik IP adresi ve 16 bitlik port adresi beraberce kullanıldığında meydana gelen adrese soket numarası denir. TCP bağlantılar soketler üzerinden sağlanır.

Soket Numarası

| Port No TSAP Adresi | IP Adresi |
| --- | --- |

**OTURUM KATMANI (SESSION LAYER)**

Ağdaki bilgisayarlar arasında oturum açılması, yönetilmesi ve oturumun sonlandırılması işlemlerinin yapıldığı katmandır. Oturumlar, aynı anda tek ya da çift yönlü veri akışına izin verebilirler. Eğer trafik tek yönlü ise oturum katmanı iletim sırasının kimde olduğunu belirtir. Böylece iki bilgisayar arasında dosya transferi yapılmasını sağlar. Oturum katmanının diğer bir görevi de senkronizasyondur. Yani bilgisayarlar arasındaki iletişimin kopması durumunda önceden belirlenmiş senkronizasyon noktaları sayesinde, yeniden bağlantı kurulduğunda bu senkronizasyon noktasından başlayarak iletimin kaldığı yerden devam etmesini sağlar.(Resume-yeniden başla)

**SUNUM KATMANI (PRESENTATION LAYER)**

Bu katman bilginin iletiminde kullanılacak biçimleriyle ilgili işlemlerin yapıldığı katmandır. Bilgisayarlar arasında iletilen verinin değişimini standartlara uygun olarak yerine getirmek bu katmanın görevidir. Ayrıca, iletilen verinin sıkıştırılması/açılması, şifrelenmesi/çözülmesi güvenlik ve kullanıcı doğrulamasının yapılması bu katmanın görevlerindendir.

**UYGULAMA KATMANI (APPLICATION LAYER)**

Uygulama katmanı, uygulama programlarının ağa erişimi için ihtiyaç duyulan birçok protokolü içerir. Kullanıcının etkileşimde bulunduğu uygulama programları bu katmanla iletişim halindedir. Farklı uç birimlerle çalışan programların kullanıldığı bilgisayarlar arasında problemsiz (her uç birim tipini karşılayan) iletişim kurmak için sanal bir ağ uç birimi oluşturmak bu katmanın en önemli görevidir. Uygulama katmanının diğer bir görevi de dosya transferidir. Değişik dosya sistemleri arasında dosya transferlerini gerçekleştirirken ortaya çıkabilecek uyumsuzlukları kaldırmak da uygulama katmanına aittir.

Token Ring

Köprü

Köprü

Token Ring

Yönlendirici

Yönlendirici

Yönlendirici

Yönlendirici

Repeater

Uygulama birimi

Ulaşım Birimi

Ulaşım Birimi

Uygulama birimi

Uygulama birimi

Uygulama birimi

TPDU

Uygulama

Sunum

Oturum

Ulaşım

Ağ

Veri İletim

Fiziksel

Fiziksel

Fiziksel

Fiziksel

Veri İletim

Veri İletim

Veri İletim

Ağ

Ağ

Ağ

Ulaşım

Oturum

Sunum

Uygulama

---
*Kaynak: `OSİ REFERANS MODELİ/OSİ REFERANS MODELİ.doc` — Belgin — 2004*
