# Bilgisayar Ağlarinda Temel Kavramlar

** Bilgisayar ağlarında temel kavramlar ******

Burada yapılan tanımlar, şu anda elimde herhangi bir yazılı kaynak olmadığı için, sadece bugüne kadar okuduğum yazılı kaynaklardan hatırımda kalan bilgilerin derlenmiş halidir....
**
Node:
**Bir bilgisayar ağına adapte olmuş herbir uç elemana denir. Bu kavram ile bir bilgisayar, ya da özelleşmiş elektronik cihazlar kastedilebilir.

**Paket:
**Herhangi bir protokol tarafından işlenmiş olan ve kendi içinde bütünlüğü olan en küçük veri parçasına, o protokole ait bir paket denir.

**Protokol:
**Birbirleriyle haberleşen sistemlerde, bu haberleşmenin yöntemlerini belirleyen kurallar bütününe protokol denir.

**Switching(Anahtarlama):
**Bir ağ içerisinde, bir paketin ulaşması gereken hedefe ulaştırılması için o paket üzerinde yapılan işleme switching(anahtarlama) denir. Bu işlem, switch adı verilen cihazlar tarafından gerçekleştirilir.

**Routing(Yönlendirme):
**İki ağ arasında, bir paketin ulaşması gereken hedef ağa ulaştırılması için o paket üzerinde yapılan ağlar arası transfer işlemine routing(yönlendirme) denir. Bu işlem, router adı verilen cihazlar tarafından gerçekleştirilir.

**Connection(Bağlantı):
**İki node arasında, asıl bilgi transferinin dışında, iletişimin ayrıntılı özelliklerini belirleyerek ve senkronizasyon kurmaya dayalı olarak yapılan anlaşmaya connection(bağlantı) denir.

**Connection-oriented Communication(Bağlantılı İletişim):
**İki node arasında, güvenli bir iletişim maksadıyla kurulan bağlantı tabanlı iletişim yöntemleridir. Bağlantı'nın gereklerini yerine getirmek uzun bir zaman aralığı istediği için performansı daha düşüktür.

**Connectionless Communication(Bağlantısız İletişim):
**İki node arasında, bağlantı tabanlı olmayan iletişim yöntemleridir. Bağlantı'nın gereklerini yerine getirmek durumunda olmadığı için performansı daha yüksektir.

** Transmission Control Protocol / Internet Protocol
İletim Kontrol Protokolü / İnternet Protokolü ******

İnternetin temel protokol paketidir. Protokol kelimesinin tanımı için bilgisayar ağları başlığı altına bakabilirsiniz.

Internet üzerinde verilerin akışını kontrol eden TCP/IP bir çok protokolün bir araya gelmesiyle oluşturulmuş olduğu için ona protokol paketi diyoruz. TCP bu protokol paketinin "Noktalar arası veri transferinde dikkat edilecek hususlar" kısmını yürütürken, IP ise "Verilerin taşınacağı yolu nasıl belirlesek!" kısmıyla ilgilenir. TCP/IP sisteminin 7 katmanlı OSI yapısına uymadığı bunu tartışan kitaplarda belirtilir. Bunun ne gibi bir soruna yol açtığını ise pek bilemiyoruz. (Aslında bilebiliriz de; uzun mesele. Boşverin gitsin)

TCP/IP' yi anlatan kitapları karıştırdığımızda onun tarihi ile ilgili bazı bilgiler verilir. Ben de hatırımda kaldığı kadarıyla bunları derleyeyim. ABD' de DARPA adında askeri bir kurum bir nükleer savaş esnasında bile ayakta kalabilecek bir bilgisayar iletişim yapısı kurulması için çalışmalar başlatır. Bu projenin temel amacı, herhangi iki nokta arasındaki iletişimin kopması durumunda bile başka yollar üzerinden noktalar arası iletişimi devam ettirebilen bir sistem meydana getirebilmekti. Bu dokümanda işin tarihi ya da edebi yanından çok bu noktası açıklanacak. Yani sistem bunu nasıl olabiliyor da yapabiliyor? Neyse bir kaç noktaya daha değinip bu faslı kapatalım. Daha sonra ABD çapında üniversite öğrencileri ya da akademisyenlerden oluşan bir yazılım grubunun uzunca bir çalışması sonucunda TCP/IP yapısı oluşturuluyor.

** TCP/IP adreslemesi ve LAN' lardaki analizi ******

O zaman öncelikle TCP/IP' nin yerel ağımızdaki iletişimi nasıl sağladığıyla başlayalım konuya. Bilgisayar Ağları kısmında da anlatıldığı gibi yerel alan ağı, 5-10 makine kadar bir bilgisayar topluluğunun ethernet vb. protokollerle bağlanmasıyla ortaya çıkıyordu.

Netbios gibi bir protokolü ele aldığımızda bu protokolün her makineye verilen bir isim ile bu iletişimi sağladığını görüyoruz. Sisteminiz, ağ üzerinde şöyle bir tarama yapar ve size Netbios protokolünü kullanan diğer makinelerin isimlerini bir liste halinde getirir. Sonra da verilerinizi transfer edersiniz.Fakat TCP/IP global bir sistem olduğu ve öyle sadece 10 makinayı birbirine bağlamakla yetinemeyeceği için daha global bir adresleme sistemi kullanmaktadır. TCP/IP' nin adresleri , notasyonal bazda birbirinden "." larla ayrılmış 4 er adet 8 bitlik (oktet) rakamdan oluşmaktadır. Bu adresleme sistemine bir örnek olarak 193.255.88.197 adresini verebiliriz. 8 bitlik parçalardan oluşmasından dolayı iki nokta arasında kalan sayılar 0-255 arasında değişen değerler alırlar. Rakam kullanmak, çok geniş bir adresleme aralığı sağlamasının yanında, bilgisayar programlamayla uğraşanların hemen yorumlayabileceği gibi, yönlendirme işlemleri için algoritmik tasarım esnekliğini de sunar. Yerel alanda zorluk gibi gelen bu numaraların kullanılması, internet alanında bir zorunluluktur. Sistemi tasarlayan kişiler de bu numaraları hafızada tutmanın zor olduğunu bildiklerinden, DNS adını taşıyan ve www.erciyes.edu.tr gibi hafızada tutulması kolay (insan hafıza yapısına uygun) olan domain isimlerini, bunlara karşılık gelen IP adreslerine eşleyebilen bir sistem geliştirmişlerdir. Bu sayede bizim ezberlememiz ya da öğrenmemiz gereken IP numaralarının sayısı (kendi makinemizin ayarlarını buna katmazsak) sadece 1' e indirilmiş oluyor. Dolayısıyla bu numaralardan kaynaklanan zorluğu da aşmış bulunuyoruz.

** ARP ******

** (Address Resolution Protocol - Adres Çözümleme Protokolü) ******

Adres Çözümlemesi' nden kasıt, karşı bilgisayarın IP adresini sisteme vermemize karşılık ethernet katmanından karşı makinanın ethernet adaptörüne ait olan MAC adresini elde etmektir. Biliyorsunuz ethernet katmanında yazılımsal protokollerin (TCP/IP, Netbios gibi) adreslerinin hiç bir önemi yoktur. Bu adresler ethernet gibi daha alt seviyedeki protokoller tarafından, herhangi bir veriden farksız biçimde işlem görürler. Dolayısıyla LAN' ımızda yaptığımız her türlü iletişim için karşı bilgisayarın ethernet kartının donanımsal adresini bilmemiz gerekiyor. (Bu arada sürekli olarak ethernet üzerinden örnekler veriyorum. Çünkü TCP/IP nin token-ring veya FDDI gibi protokoller üzerindeki uygulamaları hakkında bir bilgiye sahip değilim. Ama önemli olan şu ki TCP/IP açısından değişen bir şey yok.)

İşte bu karşı IP adresine sahip olan makinanin ethernet adaptörünün MAC adresini öğrenme işine ARP adı verilmektedir. Yapısal olarak son derece basittir. Yaptığımız iş bütün bilgisayarlara aranan IP adresinin o makineye ait olup olmadığını sormak ve eğer ait ise MAC adresinin geri gönderilmesini istemektir. Peki burada neden DNS' e benzer bir sistemle bu adresleri öğrenerek, sistemin performansını artırmıyoruz? Çünkü LAN' larımız çoğunlukla basit amaçlarla kurulmuş ucuz sistemlerdir ve fazla bir performansa ihtiyaç duymamaktadırlar. Ve her LAN için bu tür bir sistem son derece maliyetlidir. Daha yüksek performansa ihtiyacı olan LAN' larda kullanlılan bridge vb. aktif cihazlar bu işin bir benzerini yapmaktadırlar.

** Routing - Yönlendirme ******

Yukarıda da bahsedildiği üzere IP adreslerini LAN'ımızdaki makineleri birbirlerinden ayırmak için kullanıyoruz. "E o zaman tek oktetli bir adres kullansaydık. Bu kadar uzununa ne gerek var?" diyenleriniz olabilir. Tahmin edilebileceği üzere oktetlerin sadece bir kısmı LAN' ımızdaki uç makineleri (node) tarif eder. Geri kalan kısmı internet üzerindeki paket yönlendirme işlemlerinde işe yarar. Eğer 193.255.88.197 gibi bir adresin 197 olarak gördüğümüz dördüncü okteti nodelarımızı tarif etmekte kullanılacaksa, geri kalan 193.255.88' lik kısım, yerel alan ağımızı tarif etmekte kullanılır. Fakat biz değişken olarak seçtiğimiz 197' nin yerine sıfır koyarız. "193.255.88.0 ağı" diyerek ağımızı adlandırırız.

Tek oktetin değişken olarak seçildiği bu tür ağ IP adreslerine C sınıfı IP adresleri denilir. 0, ağ adresini 255 de broadcast(yayınlama - paketin bütün nodelara gönderilmesi durumu) adresi olduğu için C sınıfı ağlarda 254 tane uç eleman tanımlanabilir. Eğer iki oktet kullanılırsa B sınıfı olur. 65534 uç eleman olur. Üç oktet kullanılması durumunda ise A sınıfı ve yaklaşık 16 milyon adet uç IP olur. 1' den başlayıp 120 gibi bir rakama kadar giden (şu anda bunun kaç olduğunu hatırlayamıyorum. Çok da önemli değil zaten. İhtiyaç anında öğrenilebilir) numaralarla başlayan IP adresleri A sınıfı olarak tanımlanmışlardır ve internet üzerinde bu makinelerin düzgün çalışabilmesi için A sınıfı olduklarını belirten bir subnet mask ayarlaması yapmalıdırlar. (Subnet Mask' a birazdan değineceğim.) 192' ye kadar olanlar B sınıfı, 192' den 255' e kadar olanlar da C sınıfı... İstisnalar haricinde bu olay böyle.

Eğer bizim göndereceğimiz paketin sahibi bizim ağımızda değil de internet üzerinde başka bir ağda ise bu paket için ARP işlemi yapmayız. Paketimizi, makinemizde tanımlaması daha önceden yapılmış olan Çıkış Noktası (Gateway)' na göndeririz. Çıkış Noktası IP' sine sahip olan cihaz bir bilgisayar olabileceği gibi router dediğimiz özel tasarlanmış cihazlar da olabilir. Yaptığı işe routing(yönlendirme) denir. Bu cihazin birden fazla arayüzü vardır. Her arayüzü farklı bir ağa bakar ve her arayüz baktığı ağa ulaşabilmek için o ağdan bir IP adresi alır. Üzerinde çalışan algoritmaya bakarak, bir arayüzünden aldığı paketi hangi arayüzünden göndereceğine karar verir. Göndereceği paketin hedefi, paketin gerçek sahibi olabileceği gibi, yol üzerindeki başka bir router da olabilir. Paketin gittiği yolda, üzerinden geçtiği her bir router bir "hop" tur. Router' ların üzerindeki algoritmalar tarafından her interface için hedef ağa varmak amacıyla kaç hop' tan geçmek gerektiği bulunur ve paketin yollanacağı yöne bu hop sayılarına bakarak karar verilebilir. Bu yöntemlerden sadece biridir. Diğer başka bir yöntem ise her bir yöndeki ağ yoğunluğunun bulunmasıdır. Yoğunluğu daha az olan interface üzerinden gönderilir.

Bir başka mesele de makinamıza kendi ağ adresini ve göndereceği paketlerin hedef IP' lerinin ağ adreslerini bulmasını öğretmektir. Hedef ağların tam ve net olarak bulunması pek önemli değilse de en azından makinemizin hedef IP' nin kendi LAN' ında olup olmadığını fark edebilmesi önemlidir. Bunun için kullandığımız yönteme maskeleme diyoruz ve IP adresine benzer bir 4 okteti daha bu işe ayırıyoruz. Bu 4 oktetlik rakamlar zincirine Subnet Mask denir. C class IP' ler için standart subnet mask 255.255.255.0' dır. Bu olayı en iyi şekilde bir örnekle açıklayabiliriz. Uygulama katmanımızdan TCP/IP katmanlarına 193.255.100.1 adresine gönderilmek üzere bir paket geldiğini düşünelim. Bizim IP adresimiz ise 193.255.88.1 olsun. Subnet mask ise C class olduğu için 255.255.255.0 . 255' li kısımlar ayırt edici kısımlar, yani ağ tanımlayıcısını belirleyen kısımlar olduğu için hedef ağ 193.255.100.0 olarak bulunur. Kendi IP' miz için de aynı işlem uygulandığında 193.255.88.0 ağı olduğu görülür. İki ağın aynı olmadığı anlaşıldığı için paket gateway' e yollanır. Fakat Subnet Mask eğer 255.255.0.0 seçilseydi, ağ tanımlayıcıları 193.255.0.0 olarak bulunacağından gateway' e gidilmeyecek, LAN protokolü üzerinden direkt olarak ulaşılmaya çalışılacaktı.

Şimdi bu 255' li kısımların ayırt edici olma meselesine bir göz atalım. Burası lojikle alakalı bir mesele olduğu için dileyen burayı atlayabilir. Önceki örneğe bağlı kalarak, 193.255.100.1 adresi bitler seviyesinde açılır. 11000001.11111111.01011000.00000001 olduğu görülür. 11111111.11111111.11111111.00000000 (Subnet Mask da bitler seviyesinde açılır) Yukarıdaki gibi olduğu görülür. Alt alta gelen sayılar lojik AND işlemine tabi tutulur. Bu işlem sonucunda 255' li kısımların kopya almakta, 0' lı kısımların ise yutmakta olduğu açıkça görülmektedir. Öyleyse hangi oktet Subnet Mask'ta 0' lardan oluşmakta ise, adres kısmındaki o oktet, ağ adresi bulunurken yutulacağı için ayırt edici olma özelliğini yitirecektir.

Ayrıca Subnet Mask'ta daha çok biti 1'olarak ayırırsak ne olur bir de ona bakalım. Subnet Mask'ımız
11111111.11111111.11111111.11111100 olsun. Eski örneğe bağlı kalarak 193.255.88.0'ın bir ağ, 193.255.88.4'ün bir ağ, .8'in bir ağ, 12'nin bir ağ ... şeklinde ağ sayısının arttığını görmekteyiz. Ağ sayıları artmış fakat node sayıları azalmıştır. Demek ki C class bir IP'miz varsa ve biz onu sıkarak suyunu çıkarmak istiyorsak, böyle bir yöntem kullanmalıymışız. Pratik bir hesaplama yöntemiyle; 2 üzeri 1'li bit adedi kadar (bu örnekte 2 üzeri 6 = 64) ağa parçalamak mümkün. Her parçada da 2 üzeri 0'lı bit adedi - 2 (yazıyla: iki üzeri sıfırlı bit adedi eksi iki) adet nodeumuz oluyor. Yine bir adresin ağ tanımlayıcısına, diğerinin de broadcast' e gittiğini unutmayalım; niye - 2 oluyor diye sormayalım.

Bugünlük de bu kadarla bitirelim.

** OSI Modeli' ne bir bakış **

OSI, ismini standartlaşma konusunda sıkça duymuş olduğunuz ISO (9001, 9002 vs.) International Standards Organization'in bilgisayar ağlarına bir standart getirmek için ortaya atmış olduğu bir standartlar yapısıdır. Open Systems and Interconnections kelimelerinin kısaltılmasından oluşuyor OSI ifadesi.

Şimdi bu standartlaşma işini biraz açmakta fayda var. Dünya üzerinde bir çok bilgisayar sistemi vardır ki; birinde kullanabildiğiniz disketi diğerinde doğrudan kullanamazsınız. Dosya sistemleri farklıdır vs. yani kısacası biz bu sistemlere "birbirleriyle uyumsuz sistemler" deriz. Eğer bu sistemler arasındaki bilgisayar ağı yeterince esnek dizayn edilmezse, sistemler birbirleriyle ağ üzerinden haberleşemez hale gelirler. Varın internetin halini siz düşünün artık...

Her ne kadar sistemler birbirleriyle uyumsuz olsa da her sistemin dizaynı esnasında göz önünde bulundurulan Bilgisayar Mimarisi, İşletim Sistemleri gibi bilimler vardır. Sistemler bu bilimlere uygun dizayn edildiklerinden ötürü bir sistemin yaptığı bir işe karşı öbür sistemde de aynı ya da benzeri işi yapan bir birim vardır. Ve eğer siz iki bilgisayarın haberleşmesi sırasında yapılan işleri tam ve net olarak tarif edebilirseniz, her sistemde bu yapılan işlere denk gelen bölümleri birbirlerinden bağımsız olarak düşünebilirsiniz. Sistemlerin birbirleriyle uyumsuz oldukları noktalarda, her sistem için o sisteme özgü modüller oluşturur, transfer edilmesi istenen veriyi diğer sistemle uyumlu olacağı noktaya kadar o modüller ile işler ve karşı tarafla uyumlu olacağı bir noktaya kadar getirirsiniz. Daha sonra bu sistemler birbileriyle uyumlu oldukları bir kıvama geldiklerinde iki sistem arasında bir ortak dil/arayüz bulunmuş olur ve bu noktada veriyi transfer edebiliriz. Sonra karşı tarafa ulaşan veri bu sefer ters işlemlere tabi tutulur ve karşı tarafa özgü olan modüllerle işlenir. Ve işlenme bittiğinde o verinin karşı sistemdeki tam karşılığı elde edilmiş olur.

Bir örnekle bu konuya yaklaşalım: Eski zamanda iki ülke hükümdarından birinin diğerine bir mektup yollamak istediğini hayal edelim. Bu noktada, iyi bildiğimizi düşündüğümüzden dolayı fazlaca önem vermediğimiz bazı ayrıntıları vurgulamak istiyorum. Bir hükümdar, hiçbir zaman yazacağı mesaja muhattap olarak, kendinden daha alt seviyede bir insanı almaz. Bu ne demektir? Yani hükümdarın muhattabı ancak diğer ülkenin hükümdarıdır. Söylemek istediği şeyleri hükümdarlar arasında alışılagelmiş bir ortak üsluba dikkat ederek söyler. Yani birbirlerinin ne demek istediklerini gayet iyi anlamaktadırlar. Buraya kadar olan yer mektubun içeriği meselesiydi.

Peki mektubun iletilmesi problemini hükümdar nasıl çözecek? İşini gücünü bırakıp atına binerek dört nala sürecek mi? Yoldan geçen herhangi bir atlıya rica mı edecek? Ya da bütün yolculuk organizasyonunu kendisi mi yapacak? Hayır, bunların hiçbiri değil. Evet; cevabı siz de tahmin etmiş olmalısınız. Tabii ki en güvendiği bir vezirini çağırıp; "Şu mektubun icabına bak!" diyecektir. Bu şekilde bütün işinin gücünün arasında, herhangi bir mektuba mesaisini ayırmaktan kurtulmuş olur. Hesap sormak istediğinde de yalnız bir tek kişiyle muhattap olur. Peki vezir ne yapar? Onun da işi başından aşkın. Tabii ki, o da kendinden bir alt kademedeki memuruna bu işi havale eder. Ta ki atlı elçiye mektubun teslim edilme noktasına kadar.

İşte bu şekilde işlerimizin daima tıkırında işlemesine vesile olan ve adına bürokrasi(!) denen kavramı hep birlikte icad ederek tarih sahnesine sunmuş olduk. Şaka bir yana yukarıda tarif etiğimiz yöntemle her birim bir altındaki birime bir görev havale ediyor ve o görevin nasıl yapılması gerektiğini, hassasiyetlerini, inceliklerini vb. ayrıntıları en iyi şekilde biliyor ve kendinden bir üstteki birime karşı da göreviyle alakalı sorumluluk duyuyor. Ve tabii gerektiğinde hesabını da oraya veriyor.

İşte buraya kadar anlatmış olduğumuz bu hikaye, bilgisayar ağlarının haberleşme algoritmasına karşılık benim uydurduğum bir yaklaşımdır. Hikayede adı geçen birimler, haberleşmede tarif edilen katmanlara karşılık gelir. En alt birim olan atlı-elçi, fiziksel katman adı verilmiş olan ve bilgisayarlarımız arasına döşenen kablolar ile içlerinden akan sinyaller olarak düşünülebilir. Hem nasıl bir atlının yolu üzerinde başına bir iş gelse veya atı hastalanıp ölse, o problemini kendi uzmanlık alanı olduğu şekliyle çözerek aldığı görevi yerine getirir ve hükümdarın da bundan haberi bile olmaz; haberleşen sistemlerde de üstteki katman alttaki katmana yapması gereken işi söyler ve yapılıp yapılmadığını kontrol eder, ama oranın kendi iç problemlerinin ne olduğuyla ilgilenmez. Çünkü üst katmanın asıl işi kendisine ait olan problemleri çözmektir.

Yapılan işlemleri birbirlerinden ayrı düşünmenin bir faydası da bunları modül modül ele alarak kazanmış olduğumuz esneklik avantajıdır. Tasarımcılar her seviye üzerine ayrı ayrı konsantre de olabilirler. Bir bilgisayar sisteminde kullanıcıya yakın olan seviye üst seviye, elektroniğe yakın olan seviye ise alt seviye olarak bilinir. Seviyeler bu bakış açısıyla belirlenir. İşlevleri tam olarak tarif edilmiş olan bu seviyelere katman(layer) adı verilmiştir. ISO uzmanları oturmuşlar bunları tarif ederek bir standarda bağlamışlardır. Katmanlar 1 den 7' ye kadardır ve şöyle tarif edilmişlerdir.

Application, Presentation, Session, Transport, Network, Data-Link, Physical

Net olarak ne iş yaptıklarıyla alakalı bir miktar bilgi staj notlarında olacak. Oradan bakabilirsiniz. Zaten ulaşılması da son derece kolay bir bilgidir. Biz biraz yorumuna bakalım isterseniz.

Şimdi bu katmanlar bir seviyeye kadar donanımsal, ondan sonra ise yazılımsal bazda işliyorlar. Donanımsal sistemler son derece hızlı fakat yeterince esnek değillerdir. Yazılımsal sistemler ise son derece esnektir fakat donanımsal sistemler kadar hızlı değillerdir. Dolayısıyla işlerimizi olabildiğince donanım üzerinden yapmaya çalışıyoruz. Yapamadığımız yerde ise yazılımsal sistemlerin esnekliğinden istifade ediyoruz.

Genel itibariyle Data-Link ve Physical katmanları donanımsaldır ve çoğunlukla ethernet kartları gibi LAN adaptör kartları gibi donanımlar ile uygulanırlar.

Network ve daha yukarı katmanlar ise yazılımsaldır. Fakat eğer bu işler için özellikle yapılmış bir donanım üzerinden akan bir veriden söz ediyorsak, bu donanım için donanımsal işler daha üst katmanlara kadar çıkabilir.

Bir sistemin herhangi bir katmanı üzerinde çalışan bir protokol, ancak karşı sistemin aynı katmanında çalışan aynı protokol ile haberleşebilir.

Böylece sistemler arasında bir uyumsuzluk olma ihtimali tamamen ortadan kaldırılmış olur. (Macintosh üzerinde çalışan TCP/IP ile IBM mimarisi bir PC'nin üzerinde çalışan TCP/IP'nin haberleşebilmesi gibi)

OSI modeli katmanlarının Physical ve Data-Link katmanlarında LAN protokolleri olarak bildiğimiz Ethernet, Token-Ring ve FDDI çalışır. Bu protokoller genelde bilgisayarlarımıza taktığımız bir takım adaptör kartları tarafından uygulamaya geçirilirler. Katmanlı yapının temel özelliği olarak daha önce de anlattığımız gibi, adaptör kartı tarafından kablo üzerinden çekilen bilgi, işlenmek üzere yukarı katman protokolünün emrine verilir.

Network Layer kısmında genelde yazılımsal adresleme işleriyle uğraşırız. Bizim kendi yaılımsal adresimiz ve karşıdaki makinanın adresi gibi...

Transport'ta ise verilerin parçalara bölünmesi ve bu parçaların gönderiliş-alış esnasında karışmaması gibi meseleler halledilir. TCP/IP nin TCP ve UDP' si, Netbios, IPX gibi protokollerin bu katmanlarda çalıştıklarını söyleyebiliriz.

TCP/IP; bazen data-link'ten sonrasını bütünüyle ele alması (örnek: telnet) gibi özelliklerinden dolayı OSI modeline uymaz.

Bu şekilde işlene işlene gelen bilgi masanızın üzerinde bazen bir chat sürecindeki bir satır bilgi olur, bazen de bir html dokümanı olarak web browserınız tarafından işlenir.

OSI modeli Tannenbaum'un Computer Networks kitabında da ayrıntısıyla kritik edildiği gibi pratik hayatta pek de uyulmayan bir standartlar bütünüdür. Fakat ağ sistemlerinin çalışma prensiplerini kavrayabilmek açısından çok faydalı olduğundan, ağları anlatan kitaplarda başköşelerdeki yerini daha uzun süreler koruyacağa benziyor.

En önemli dört katmanın da görevlerinden az da olsa bahsettiğimize göre bu bahsi burada noktalayabiliriz.

** Aktif Network Cihazları ******

Ethernet'ten bahsederken collision denen bir hadiseden bahsetmiştik.

Hakikaten ethernet'in en büyük baş belası bu collision denen hadise olsa gerek. En basitinden şöyle bir örnek verelim: Geçen bir arkadaşla ağ üzerinden oyun oynuyorduk. Başka bir kullanıcı da aynı ağ üzerinden internet bağlantısı alıyordu. Daha sonra bu internet kullanıcısı yok yere makinasını mı denemek için yaptı artık orasını bilmiyoruz, 14 tane IExplorer penceresi açtı arka arkaya. Herhelde açılan her pencere de ağ üzerinden bir sorgulama mı yapıyor onu da bilmiyoruz, oyunumuzun kesilmesine sebep oldu. Eğer siz de oyun oynamak gibi, ağ üzerinden zaman-kritik işler yapıyorsanız; beklenmedik bir anda, bilinmeyen bir sebeple gelen bir veri dalgası işinizin aksamasına, daha da kötüsü kesilmesine sebep olabilir.(Ağ üzeinde oynanan oyunlarda zaman senkronizasyonu çok önemlidir. Çünkü her oyuncunun aynı anda, aynı ortamda bulunduğu duygusu verilmelidir.)

Genelde LAN'ınızdaki makine sayısı 10'un üzerine çıktığında ve ağ üzerinde yoğun sayılabilecek veri trafiği varsa bu collision meselesi problem olmaya başlıyor. (Burada, normal ev kullanıcısı olarak bilinen ve hataya tolerans gösterebilen bir kullanıcı üzerine yapılan pratik bir yorum sözkonusu. Ağ ile taşınan verinin kritikliğine göre ve hata tahammülüne göre bu yorum değişebilir.) Ama tabii profesyonel uygulamalarda buna bile bakılmayıp birden fazla cihazın aynı collision domain'de bulunması zararlı görülerek, pahalı cihazlar kullanılmak kaydıyla bu problem aşılmaya çalışılıyor.

Şimdi, nedir bu cihazlar? Ne iş görürler onu inceleyelim. Aktif bir cihaz olmamasına rağmen önce hub'dan başlamak, konu bütünlüğü açısından daha doğru olacak...

**Hub******

Göbek/dingil manasına gelen bu kelime, elektronik sinyalleri çoğaltarak, bütün ayaklarına ulaştıran basit yapıdaki bir cihaz için kullanılmaktadır. Üzerinde hafıza üniteleri olmadığından ve akıllı bir sistem olmadığı için aktif cihaz sınıfına girmez.

Bilindiği gibi ethernet'de sinyallerin bütün uç elemanlara ulaştırılması esastır. Biz de uç elemanımızı bu cihaza bağlayarak, ağda dolaşan sinyallerin bizim makinamıza da uğramasını sağlamış oluruz yani ağa adapte oluruz.

Bir kablo üzerine birden çok uç elemanın bağlanmasıyla ethernet oluşturulabiliyorken, daha çok kablo kullanması gereği aşikar olan böyle bir sisteme niçin geçilme ihtiyacı duyulmuştur?

Çünkü, bu sayede fiziksel bağlantıların herhangi birinde bir sorun olduğunda, sadece o fiziksel bağlantının sahibi olan bilgisayarın ağ ile olan bağlantısı kesilir. Ağın faaliyeti ise normal olarak işlemeye devam eder. Sorunsuzluk; ufak maliyet artışlarından çok daha önemli bir tasarım kriteridir.

**Bridge******

Bridge(Köprü) adı verilen cihazlar, gerçek bir köprüde de olduğu gibi iki ayağa sahiptirler.

Şöyle bir örnek verirsek:
Bir şirkette, muhasebe ve bilgi işlem departmanlarının bilgisayarları aynı ağda olsunlar. Burada sizin de tahmin edebileceğiniz gibi, bu grupların kendi içlerindeki veri trafiğinin gayet yoğun, birbirleri arasındaki veri trafiğinin ise çok seyrek olarak yaşanması beklenir. Peki böyle bir durumda bir önlem alınmalı mıdır?

Evet. Çünkü ethernet sisteminin yukarıda da bahsettiğimiz Multiple Access özelliğinden dolayı, bir ağa attığımız bilgi bütün uç elemanlara ulaşır. Eğer bir uç elemana, kendisini ilgilendirmeyen verilerin gelme olasılığı, kendisini ilgilendiren verilere oranla çok fazlaysa; bu olay hem o uç elemanı gereksiz yere meşgul edecektir, hem de collision olayının gerçekleşme ihtimalini artıracaktır.

Öyleyse, bu iki bilgisayar grubunun arasına, mesajları süzerek filtre eden bir cihaz konulursa, her grubun mesajını kendi bölgesinde tutmuş olur ve yukarıda saydığımız zararları ortadan kaldırır.

Bu cihazın mantığı, her bir ayağına bağlı olan ethernet adaptörlerinin MAC adreslerini öğrenerek bunları hafızasında tutuyor olmasıdır. Bir ayağına, diğer ayağındaki makinelere ulaştırılması gereken bir paket geldiğinde, onu diğer ayağından ağa gönderir. Diğer bacağını ilgilendirmeyen bir paket geldiğinde ise hiçbir işlem yapmayarak filtre işlemini gerçekleştirmiş olur. Bir bilgisayardan ağa gönderilen bir paket, muhattabına ulaşmasının hemen ardından gereken cevap da postalandığından; bridge cihazı, bir haberleşmede iki adet bilgisayarın hangi bacaklarında bulunduğunu öğrenmiş olur.

**Switch******

İkiden fazla sayıda ayağı olan bridge'lere switch adı verilir. Pratik hayatta bridge'lerden ziyade switch'lerle karşılaşmamız muhtemeldir. Çünkü profesyonel ağ tasarımları gitgide daha çok yaygınlaşıyor ve sorunsuz sistemler isteyen tasarımcılar ve ağ yöneticileri gitgide bu cihazlara doğru yöneliyor.

Switch'lerin yaptıkları iş olan anahtarlama, bu cihazların en önemli bir performans kriteri olarak bilinir. Bu kabiliyetleri ne kadar fazlaysa, o kadar yoğun bir ağ yükünün altına girebilirler. En kabiliyetli olan switch'ler, o ağın tasarımının en merkezine ya da göbeğine yerleştirilirler. Daha az kabiliyetli switchler ya da kritiklik durumu daha az olan bölgelerde ise hub'lar, merkezdeki switch'e(core switch) uç eleman olarak bağlanırlarsa; mantık olarak düşünüldüğünde de, pratikteki uygulamalarında da, ağımız bir ağaç yapısı içerisinde büyüyerek genişleyebilir.

Standart olarak en sıklıkla karşılaştığımız switch'ler 24 port olanlarıdır. Merkeze konan büyük switch'ler ise genelde modüler yapıda olup, ihtiyaca göre modüller eklenerek kapasiteleri artırılabilmektedir.

Ethernet'ten çok farklı olan ATM vb. sistemlerde de switch adı verilen cihazlar bulunmakta, yaptıkları iş ise paket süzmekten ziyade, gerçek manada paket anahtarlaması yapmaktır. Bu tür sistemlerde switch'lerin daha akıllı görevleri, sistem yönetim yazılımlarını üzerlerinde barındırmaya varıncaya kadar, oldukça geniş bir yelpazededir. Ayrıca bu tür sistemlerde switch, bir paketin noktadan noktaya hangi yollardan geçerek gitmesi gerektiğini bilebilmekte ya da buna karar verebilmektedir.

** Ethernet **

Ethernet, aynı kablo üzerine bağlanmış birden fazla makinenin oluşturduğu donanımsal bazlı bir protokoldür. Bu protokolde makinelere taktığımız ethernet adaptör kartları, ağa elektronik sinyaller gönderme ve başkaları tarafından gönderilmiş olan sinyalleri algılama özelliğine sahiptir. Herhangi bir protokol tarafından işlenmiş olan ve kendi içinde bütünlüğü olan en küçük veri parçasına, o protokole ait bir paket diyoruz.

Ethernet paket yapısı
(Aslında katmanlı yapıyı anlamaya daha uygun)

Ethernet için bu paketlerin IEEE 802.3 standardında da belirtilmiş olan büyüklükleri vardır. (IEEE LAN sistemlerini standardize etmiş ve onlara 802 ile başlayan kod numaraları verilmiş. Ethernet'in payına ise 802.3 düşmüş.) Bütün adaptör kartları tek bir kablo üzerinden veri alışverişi yaptığı için hangi verinin kimden kime gönderildiğini anlayabilmek gerekir. Bunu belirleyebilmek için, her ethernet adaptör kartının dünya üzerinde diğer kartlardan farklı bir sabit adresi olması öngörülmüştür. İşte bu sabit adrese Media Access Control (MAC) adresi adı verilir. Her ethernet paketinin üzerinde paketi gönderenin ve alıcısının MAC adreslerini gösteren bölgeler vardır. Ethernet kartı bu bölgelerden mesajın kendisine gelip gelmediğini ya da kimden geldiğini anlayabilir. Eğer mesaj kendisine gelmiş ise veriyi üst katman protokollerine gönderir. Eğer paket kendisine ait değilse paketi atar.

Ethernet sistemi, en basit şekliyle CDMA/CD denen bir yöntem ile haberleşmeyi düzenler. Bu kısaltmanın açılımı Carrier Sense (Hattı dinlemek), Multiple Access (Çoklu erişim), Collision Detection (Çarpışmanın fark edilmesi) şeklindedir. Bu kelimeleri yorumlarsak ethernetin çalışma
prensibini anlamış oluruz. Üst katmanlar tarafından ethernet katmanına indirilmiş olan paketler ethernet içinde uygun paketler haline dönüştürüldükten sonra kablo üzerinden ağa gönderilmek üzere iken, ağ üzerinde hareket eden başka verinin olup olmadığını anlamak maksadıyla hat dinlenir.(CS) Eğer hat doluysa hat boşalıncaya kadar beklenir. Bir kablo medyasına aynı anda birden çok ethernet kartı erişebilirler.(MA) Fakat hattın boş olduğunun görülmesiyle hatta aynı anda gönderilen birden fazla adaptör kartına ait veriler, çarpışma (collision) denilen verilerin bozulması olayına maruz kalırlar. Hattı dinleyen diğer bağlı makineler çarpışmanın varlığını anlayabilirler. (/CD) Paketlerinin böyle bir duruma maruz kaldığını algılayan adaptör kartları, paketlerini yeniden göndermek üzere rasgele bir süre beklerler.

İşte ethernet sisteminin çalışma mantığı bundan ibarettir ve gayet basittir.

---
*Kaynak: `BİLGİSAYAR AĞLARINDA TEMEL KAVRAMLAR.doc/BİLGİSAYAR AĞLARINDA TEMEL KAVRAMLAR.doc` — 00 — 2004*
