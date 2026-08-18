# Ethernet Teknolojileri

**ETHERNET TEKNOLOJİLERİ******

Ethernet 1970 yılları sonunda PARC'da (Palo Alto Research Center) yapılan çalışmalarda meydana geldi.Amaç bilgisayarları haberleştirmekti ve haberleşme ortamı olarak hava kullanıldı ve haberleşme uydular üzerinden gerçekleşti.Etherin ismi buradan gelmektedir.Hızı 3 Mbps kadardı.Şimdi kullandıgımız ethernetler ise 10/100 Mbps'lık hızı desteklemektedir.Ethernet fast ethernet , giga ethernet gibi çok yüksek hız saglayan çeşitleride sahiptir.

IEEE (international Electric Elektronic Engineering) 1980'lede etherneti bir standarta oturmuştur bu standar 802.x (1980'in 2. ayı).Bu standartlardan 802.2 ile ethernet hemen hemen aynı yapıya sahiptir sadece çerçeve yapıları farklıdır.

**802.x Ailesi ve Protokolleri******

IEEE LAN standartlarına karşı düşen modellemeri 1980 yılının ikinci ayında başladıgı için bu aileye 802.x ailesi adı verildi.Bu ailedeki standartlardan 8023 bilinen adıyla Ethernet teknolojisidir.Jetonlu halka 802.5 , fast ethernet 802.3u , gigabit ethernet 802.3z , jetonlu yol için 802.4 kullanılır.

**Ethernet –IEEE 802.3******

Ethernet ilk olarak PARC’ta uydu üzerinden bilgisayarların haberleşmesinde kullanıldı.İletim hızı 2.94 Mbps idi.Günümüzde kullanılan çeşitleri genelde 10Mbps ya da 10/100Mbps’tır.Dünyadaki LAN’ların %95 ‘i etherneti kullanılır.Kurulum kolaylıgı , maliyet , hız randıman , basitlik ve bol miktarda parça bulunması bu tip agların seçiminde önemli etkenlerdir.Teknoloji olarak zayıf ve güvensiz bir yöntem olan broadcast (yayın) kullanılır.Yayın yönteminde bir paket aga girince tüm agın band genişligini kullanır ve iki yönlü veri aktarımına da izin verilmez.Ethernetin temel sorunlarından birisi ise CSMA/CD’dir.

CSMA/CD-çatışma (carrier sense multiple access / collision detect)

Bu ethernetin temel iletitimi olan yayın (broad cast)dan dolayı ortaya konmuş bir protokoldür.Bu protokol collision (çarpışma) engellemek degil de sezmek için kullanılır.CSMA/CD protokolü, Ethernet ve 802.3 networkler tarafından kullanılan bir çeşit medya erişim kontrol mekanizmasıdır. Başka bir deyişle, iletişim hattına bilgi paketinin nasıl yerleştirileceğini belirler. CSMA/CD \`Carrier Sense Multiple Access/Collision Detect'in kısaltılmışıdır. Bir birim network hattına bilgisini bırakmadan önce, başka bir birimin hatta bilgi bırakıp bırakmadığını anlamak amacıyla, hattı dinler.

Bilgi göndermek isteyen cihaz hattın boş olduğuna karar verince, bilgisini bırakır ve başka bir cihazın bu sırada hatta bilgi bırakıp bırakmadığından emin olmak için dinlemeyi sürdürür. Eğer bu sırada başka bir cihaz, hattın boş olduğunu sanarak o da hatta bilgisini bırakırsa, \`collision' yani çarpışma olur.

Çatışmanın sezilmesi için verinin tamamının karşı bilgisayar geçmeden hissedilmesi gerekir.Yani ilk biti çıkardıktan ve son bitin bizden çıkana kadar geçen sürede bir çatışma olması durumunu hissetmek için belli bir süre geçer.Bu süre kadar geçen zamanda bilgisayar paket üretmeye devam etmelidir ve bu 10Mbps lık aglarda 64bitlik bir veri üretilir 100Mbpslık aglarda 640bitlik veri üretilir.Eger üretilecek veri 64byte ya da 640bytetan küçükse bunları bu rakamları tamamlamak için dolgu bitleri kullanılır.Mesela 10/100Mbps ‘lık bir agda bir bilgisayar karşı tarafa bir bitlik bir veri göndermesi gerekse bile bunu 640 byte tamamlaması için gerekli dolguları eklemelidir.Çatışma sezilince ne yapılır?çatışmayı sezmiş olan dügümler (bilgisayarlar) rastgele bir müddet bekler.En küçük sayıyı seçen dügüm bilgisini yola çıkarır.Aynı sayıyı seçmemeleri için belli bir sayı kümesi arasından seçilir bu rastgele sayılar.Bu sayı kümesi ise bazı matematiksel hesaplamalar sonucunda ortaya çıkmıştır (mühendislikte hiç birşey tesadüfe bırakılmaz). Sizin canınızı bu sayı kümesinin nasıl hesaplanacagını anlatarak sıkmayacagım  .Eger iki bilgisayar aynı sayıyı çekipte gene çatışma olursa bu durumda çatışan bilgisayarlar yeniden bir sayı çekerler 16 defa arka arkaya çatışma olursa ethernet kartının arkasında kırmızı ışık sürekli yanar ve üst katmana hata mesajı geçer.Çatışmayı ilk sezen dügüm diger dügümlere "jamming" adı verilen özel bir mesaj yayınlar.

**Ethetnet topolojileri******

Ethernet broadcast ile haberleşme yapmasından ötürü topoloji olarak temeli ortak yol şekline dayanır.Günümüzde ethernetin hub ile birlikte kullanımı yaygındır.Hub cihazlar oldukça basit yapıya sahiptir.Sadece ethernet için ortak yol saglar bunların yerine switch adı verilen daha fonsiyonel ama daha pahalı cihazlarda kullanılabilir.

Ortak yolda sadece bir anda bir göndericinin verisi yolda bulunabilir.Aynı anda iki kullanıcı veriyi çıkarmaya kalkarsa yukarıda anlatıldıgı gibi çatışma olur.Ethernet teknolojisinin fiziksel katmanı temel band kullanır yani yolda aynı anda tek bir işaret kullanır ve band genişligi onu kullanan işaret tarafından harcanabilir.Hub fiziksel olarak yıldız topolojisinde görünsede mantık olarak ortak yol teknolojisini kullanır.

Ortak yol (BUS)

Yola ilgili paket çıkarılır ve bu veri tüm bilgisayarlara gider.Paketin sahibi olan bilgisayar paketi alır.Digerleri ise dinlemede kalır.Eger iki bilgisayar aynı anda veri çıkarırsa temel band olarak verilerin ikiside tüm band genişligini kendisi kullanmak isteyecek işaretler birbirleri içinden geçerlerken girişim yapacaklar ve düzeltilemeyecek derece bozulacaklardır.

Hub ile baglanmış dügümler (bilgisayarlar)

Ethernet ile birbirlerine baglı bilgisayarlar.Hub aracalıgı ile birbirlerine görünüm olarak yıldız topolojisinde baglı görünsede hub’ın işlevi sadece bilgisayarlar için ortak yol kullanımı saglamaktır.

**Ethernet Çerçeve Formatı******

Ethernetin mantıgı veriler çeşitli çerçeveler haline getirilir ve diger bilgisayarlara gönderilir.Bilgiler fiziksel ortama çıkarılmadan önce çeşitli protokoller tarafından başlık bilgileri eklenir ve en son olarakta ethernetin çerçeve formatı biçimine sokulur.

802.3 ile ethernetin çerçeve yapısı hemen hemen aynıdır

Aşagıdaki yapı 802.3'ün çerçeve yapısıdır.Ethernetle arasındaki fark sadece başlık kısmında olup ethernetin başlık kısmının öntakı+başla birleştirilmiş öntakı adı altında konmuş ve ayrıca 8 byte olarak tanımlanmamıştır.

Ethernet:öntakı 8 byte

**Öntakı:** 802.3 standardında senkronizasyon için kullanılır.Alıcı saayi ile gönderici saatinin senkronize olmasını sağlar.Ethertte öntakı ve başla ayıracı birlikte kullanılır ve 8 bitlik öntakı olarak karşımıza çıkar.

**Alıcı adresi:** Çerveyi alacak dügümün adını içerir ve 48bitlik (6 byte) MAC adresini içermelidir.Birebir , grup , ya da yayın olarka adresleme yapılabilir.

MAC (Media Access Control)adresi:Ethernet network cihazlarına, tanınabilmeleri için, hexadecimal ve dünyada bir eşi daha olmayan seri numarası verilir. Bu numaralar, üretici firmalar tarafından fabrikada verilmektedir.6 bytetır ethernet kartının üzerindeki ROM'a yazılır.(bazı networklerde bu numaralar kullanılarak güvenlik saglanmaktadır)

**Gönderici adresi:** Çerçeveyi gönderenin adresini içerir.

**Tür:** Bu iki byte tür alanıyla alınan çerçevelerin hangi üst katman protokoluna veya fonksiyonuna gönderilecegini belirler (ftp,telnet vs.)

**Veri: **aktarılacak veridir.46-1514 byte arasında olabilir.10Mbpslık ethernet agları için en az 46 byte olmalıdır.Nedeni yukarıda açıklanan 64byte ile ilgilidir.

**Çerçeve hata sınama-Frame Check Sequence (FSC):** 32 bitlik CRC degeri yerleştirilir (CRC bir tür hata sınama algoritmasıdır).Hata sınaması öntakı dışında çerçevenin tüm bitleri için yapılır.

**Ethernetin Lojik Kodlama Sistemi******

Çok çeşitli sayısal işaret kodlama biçimleri vardır.Başlıcaları ; NRZ-L , NRZI , Manchester , farksal Manchester ve 4B5B gibi.

Ethernette verilen lojik kodlama sistemi olarak Manchester ya da 4B5B kodlamasını kullanırlar.Manchester kodlamasının temel ilkesi hat üzerinden ne iletilirse iletilsin bir şekilde titreşim oluşturulmasından ileri gelir böylece hattın kullanılıp kullanılmadıgı kolay bir şekilde anlaşılır.Bu tip taşıma kullanması ethernetin gereklerindendir.

**Kablolama Teknolojileri ******

10base-2 İnce koaksiyel

10base-5 kalın koaksiyel

10base-T UTP,STP (bükümlü çiftler) kablolar.

Ethernet aglarında standart olarak üç tip kablolama bulunur:

Korumasız bükümlü çift (UTP unshield twited pair), korumalı bükümlü çift (STP shield twisted pair) , thin (ince) Ethernet (koaksiyel) , ve kalin (thick) Ethernet.

Network temeli band genişligi ve hızını seçilen kablolama teknolojisi belirler.

Bükümlü çift tel (twisted pair):

Network haberleşme sistemleri ve yüksek dereceli telefon hatlarında kullanılan kablodur. İki çeşidi vardir: Korumalı (STP) ve korumasız (UTP).Korumalı olanının içinde verilerin dışetkenden etkilenmemesi için koruyucu bir kılıfı vardır.Çok gürültülü olan ve hassas ortamlarda kullanılır kılıfsız olana göre maliyeti biraz daha yüksektir. 10BaseT/100BaseTX standardlarında kullanılır. RJ-45 konnektörlerle sonlandırılır.Bunlarda 8 adet iletkenden çift pair kullanılır.

Thin Ethernet Koaksiyel: Network koaksiyel, 10Base 2 olarakta adlandırılır. BNC konnektörleri kullanırlar.

Thick (Kalın) Ethernet: Standart Ethernet olarakta adlandırılır. 10 Mbps bandgenişlikli ağlarda kullanılır. Ağır, sert ve kurulumu güç ve pahalı bir kablolama yöntemidir. BNC konnektör kullanırlar.

Fast Ethernet: 100 Mbps veri taşıyabilen sistemdir. 100 BaseTX olarakta bilinir. 10Base-T Ethernet’le benzerlik gösterir, fakat 10 kat daha hızlıdır.

Kategori 3 (10Base-T, 10 Mbps ağlar için) ve Kategori 5 (100Base-TX 100 Mbps Fast Ethernet Ağlar için) kablolama ile kullanılabilir.

İnce, esnek ve RJ-45 konnektörleri ile kurulumu ve kullanımı basittir.Bir adet pense ile orta halli bir bilgisayarcı için bu tip konnektörlü kablolar hazırlaması pek güç degildir.Renk sıralaması önemlidir. En önemli iki avantajı ve ekonomik olması ve star yapı ağlarda kurulum kolaylığıdır.Diğer bir avantajı arıza tesbitinin kolaylığı ve hub ile bir node arasındaki bağlantının gitmesi durumunda sadece o node’un ağ özelliklerinden yararlanaması, bu durumun tüm ağı etkilememesidir.

Ağınızı genişletmek istediğinizde, “crossover” kablolama ile hub veya switch’inizi diğer hub veya switch’lere bağlamak mümkün olduğundan ağın büyümesi oldukça kolay olacaktır.Crossover kablolama için kullandıgınız renk pairlerini bilmelisiniz ve 1-3 , 2-6 olacak şekilde ayarlama yapmalısınız.

Kablo Kalite Standartları

Network standartları 10 Mbps ve 100 Mbps Ethernet ağları için kablo tiplerini belirler. Kategori derecesi kalite veya veri taşıma yeteneğini gösterir. Kategori derecesinin yükselmesi verinin güvenilirliğini arttırır.

Evlerimizde telefon kablosu olarak kullandığımız kablo Kategori 1 kablodur ve RJ-11 konnektör kullanır. Bazı ticari kurumlar telefon hatlarında Kategori 3 kablolama kullanır. Ağ bağlantılarında Kategori 1 kablo kullanılamaz, sadece Kategori 3 ve 5 kullanılır.

Kategori 3 UTP

Kategori 3, 10 Mbps bandgenişliğindeki ağlarda kullanılır . 100 Mbps ağlarda kullanılamaz.

Kategori 5 UTP

Kategori 5, 100Mbps band genişliğinde veri transferi yapabilen ağlarda kullanılır. 10 Mbps ağlarda da sorunsuz çalışır fakat Kategori 3’ten biraz pahalıdır. İlerde 100 Mbps’e geçmek isteyen ağlar şimdiden Kategori 5 kablolama kullanabilir.

Koaksiyel Kablolama

Koaksiyel kablo, kablo TV veya bildigimiz anten kablosuna benzer fakat daha yüksek kalitede veri transferine izin verir. Ağlarda kullanılan iki çeşit koaksiyel kablo vardir. Bunlar 10BASE 2 ve 10BASE 5. 10BASE 5’dir. Kalın koaksiyel günümüzde çok kullanılmaktadır.

10BASE 2

BNC konnektör kullanır. Küçük ve orta büyüklükteki ağlarda kullanılır. Güvenilir fakat oldukça pahalıdır. BUS yapı ağlarda kullanılır.

**Konnektor ve Portlar******

RJ-45 Konnektörler

10 BASET ve 100BASETX kablolar RJ-45 konnektörleri ile sonlandırılır

Hub veya Switch üzerindeki porta takılarak güvenilir bir bağlantı sağlar.

BNC Koaksiyel Konnektörler

BNC kablo bağlantısı bilgisayarınız ile ağ arasındaki durumu LED’ler yardımıyla izleminize olanak vermez. Kablonun açık uçları 50 Ohm luk direnç ile sonlandırılır.

RJ-45 Düz Portlar

Bunlar Hub ve Switch’lerde bulunan standart portlardır. Hub (veya switch) ile node arasında bağlantı bu portlardan sağlanır.

RJ-45 Crossover Portları

Ağ bağlantılarında merkezi bağlantı noktasından buna bağlı olan ekipmanlar arasında düz kablo kullanılır. Fakat ağ genişlemesi durumunda iki hub’ı birbirine bağlayacağımız durumlarda crossover bağlantı kullanmamız gerekir. Bazı hub veya switch’lerde “crossover” bağlantı gerektirmeyecek extra port bulunur.

BNC Portları

10 BASE2, koaksiyel kablo bağlantıları için kullanılır.

**Kaynakça: Bilgisayar haberleşmesi ve Network Ders Notları.******

---
*Kaynak: `ETHERNET TEKNOLOJİLERİ/ETHERNET TEKNOLOJİLERİ.doc` — Server — 2004*
