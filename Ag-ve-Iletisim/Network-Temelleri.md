# Network Temelleri

| **Network Temelleri****** |
| --- |

***Bu diyagram...Dr. Robert M. Metcelfe tarafından 1976 yılının haziran ayında National Computer Conferance'da ethernetin doğuşu sırasında çizildi. Ethernetin doğuşundan beri bu diyagramdaki temellere dayanan kullanım süregeldi.****
*
***Yerel Ağ Mimarileri***

Günümüzde en çok kullanılan yerel ağ mimarileri Ethernet, Token Ring ve ARCnet tir. Halihazırda tüm dünyada küçük büro networklerinden, kampüslere, evlerde kurulan basit networklerden, çok büyük networklere kadar, ucuz, kolay ve performanslı olması nedeniyle ethernet kullanılmaktadır.

***Ethernet***

1960'li yılların sonlarında Hawaii Üniversitesi ALOHA adını verdiği bir geniş ağ kurdu. Üniversitenin amacı kampüsün değişik noktalarına yayılmış olan bilgisayarları birbirine bağlamaktı. Bu network modelinin günümüze kadar gelen en önemli özelliği CSMA/CD olarak adlandırılan tekniktir. CSMA/CD nin açılmış hali carrier detect,multiple access with collusion detect (taşıyıcı sinyalin algılanması, çoklu erişimce çarpışmanın tespiti). Taşıyıcı sinyalin algılanması -carrier sence- ağ kartının kablodan bilgi transfer etmeden önce belirli bir süre hattı dinlediği anlamına da gelir. Çoklu erişim, aynı kabloya birden fazla bilgisayarın bağlanabileceğini belirtir. Çarpışmanın tespiti ise hattaki verilerin çarpışmasını engellemek için alınmış bir güvenlik önlemidir. Bu eski ağ tasarımı bu günkü ethernetin temelidir.1972 yılında XEROX firması deneysel amaçlı ilk ethernet kartını üretti ve 1975 yılında ilk ethernet ürününü piyasaya sürdü. Bu ürünün orijinal versiyonu 2.95 Mbps hızında 1km kablo ile 100 den fazla bilgisayarı birbirine bağlamak üzere tasarlanmıştı. XEROX ethernet kartı çok başarılı oldu. Intel, Xerox ve Digital 10 Mbps ethernet konusunda yeni bir standart getirdiler. Oluşturulan bu standart bugün kabul gören IEEE 802.3 standartı ile büyük benzerlikler göstermektedir. Ethernet networkler değişik kablolar ile bağlanabilir. Ethernet yerel iletişim ağı altında sistemleri birbirine bağlayan bir tür kablolama ve sinyalleşme biçimidir. Bilgisayar haberleşmesinin temelinde OSI modeli geçerlidir. OSI modellemesinde ilk iki katmanda (1. katman -fiziksel- ve 2.inci katman -data link-) belirlenen Ethernet, ilk kez, 1970'lerin sonlarında, Xerox tarafından geliştirilmiştir. 1980'lerde Xerox firmasının DEC ve Intel firmalarıyla ortaklaşa yaptığı çalışmalar sonucunda, Ethernet Versiyon I. için \`Blue Book Standard' (Standart Mavi Kitap) adı altında, bu versiyonun kullandığı standartları açıklayan bir kitap ortaya çıkarılmıştır. Burada açıklanan standartlar arasında, \`baseband' tekniği, CSMA/CD (Carrier Sense Multiple Access/Collision Detect) network standardı ve ethernetin ilk dönemlerinde kullanılan ve uzun yıllar yaygın bir şekilde uygulanan coaxiel kablo kullanım standartları anlatılmaktadır. Bu standart daha sonra 1985 yılında çıkan Ethernet II adlı yeni standartla revize edilmiştir. IEEE (Institute of Electrical and Electronics Engineer) 802 numaralı projesinde ve 802.3 CSMA/CD network standardının oluşumunda, Ethernet II Versiyonu baz alınmıştır. Genelde de ethernet paketinin başında yer alan bilgi (header) dışında bir farkları olmadığı için, ikisi birbirlerinin yerine anılırlar.

**CSSMA/CD nedir?****

**CSMA/CD protokolü, Ethernet ve 802.3 networkler tarafından kullanılan bir çeşit medya erişim kontrol mekanizmasıdır. Başka bir deyişle, iletişim hattına bilgi paketinin nasıl yerleştirileceğini belirler. CSMA/CD \`Cariner Sense Multiple Access/Collision Detect'in kısaltılmışıdır. Bir birim network hattına bilgisini bırakmadan önce, başka bir birimin hatta bilgi bırakıp bırakmadığını anlamak amacıyla, hattı dinler.
Bilgi göndermek isteyen cihaz hattın boş olduğuna karar verince, bilgisini bırakır ve başka bir cihazın bu sırada hatta bilgi bırakıp bırakmadığından emin olmak için dinlemeyi sürdürür. Eğer bu sırada başka bir cihaz, hattın boş olduğunu sanarak o da hatta bilgisini bırakırsa, \`collision' yani çarpışma olur.

**Baseband network ne demektir?**

Fiziksel medya (yani kablo) üzerinde kominikasyon sağlamak amacıyla, sadece bir tek band kullanılmasına izin veren haberleşme standardıdır. Yani, aynı anda sadece bir tek cihaz bilgi gönderebilir.
Baseband transmisyon tekniğini kullanan Ethernet gibi standartlarda, cihazlar bilgi transferi yaparken hattın sağladığı tüm bant genişliğini (ethernet için 10Mbit ya da l00Mbit) kullanırlar. Bu durum telefon sistemine benzer. Herkes konuşmak için sırasını beklemek zorundadır ve konuşmaya başladığında tüm hat ona ayrılmış olur. Başka biri de aynı telefondan konuşmak istediğinde, konuşmanın bitmesini beklemek zorundadır.

**Broadband network nedir?****
**
Baseband networklerin tam tersidir. Burada fiziksel kablo, broadband tekniği ile, sanal olarak birçok kanala bölünmüştür. Her kanalın, \`frekans bölme modülasyonu' adı verilen bir teknik aracılığıyla belirlenen, kendine ait taşıyıcı bir frekansı vardır. Bu farklı frekanslar, network kablosunun üzerinde aynı anda konuşulabilecek şekilde, çoğaltılırlar. Belli bir frekanstan bilgi transferi yapan bir cihaz, başka bir frekanstan yayın yapan cihazın bilgilerini dinleyemez. Örnek vermek gerekirse, kablolu televizyon, broadband yayın uygulamaktadır. Aynı anda pek çok kanal programı tek kablo üzerinden yayın yapar ve seyretmek istenilen bir tane kanal seçilerek seyredilir.
**
****Ethernet Paketi** **nedir?****
**
60 byte'tan oluşan Ethernet paketi cihazın içindeki ethernet kartında yeralan chipset tarafından yaratılır. Paket, tam olarak, 6 byte uzunluğundaki bilginin yaratıldığı kaynak adresinden, 6 byte bilginin gönderileceği alıcı adresinden, 2 byte uzunluğundaki bilginin tipini belirten bilgiden ve 46 byte uzunluğundaki data'dan oluşmaktadır. Bu formatın tam ve doğru olarak oluşumundan tamamı ile kullanılan yazılım sorumludur. Bu bilgilerin ışığında, en kısa ethernet paketinin boyu 62 byte, en uzun ethernet paketinin boyu ise 1514 byte'dır.

**Ethernet ve IEEE 802.3 arasındaki fark nedir?**

IEEE, Ethernet'in standartlaştırılmasında çalışmış ve bunu yaparken orijinal Xerox tarafından geliştirilen spefikasyonlarında bazı değişiklikler de yapmıştır.

**Mac Adresi nedir?**

Ethernet network cihazlarına, tanınabilmeleri için, hexadecimal ve dünyada bir eşi daha olmayan seri numarası verilir. Bu numaralar, üretici firmalar tarafından fabrikada verilmektedir.

**Ethernet adreslerinde özel bir numaralandırma kullanılmakta mıdır?****
**
MAC Adresleri 6 byte uzunluğundadır ve hexadecimal olarak yazılırlar. Örnek olarak 12:34:56:78:90:AB bir MAC adresidir. Her üretici firmanın kendi ürünleri için kullanabileceği belli bir MAC adresi alanı vardır. İlk 3 byte üretici firma kodundan oluşmaktadır. RFC-1700, bu üretici kodlarının listesini içermektedir. Daha güncel olan MAC adresi listesi ftp.lcs.mit.edu internet adresinde pub/map/Ethernet-codes içinden edinilebilir.

**CRC ne demektir?****
**
Cyclical Redundancy Check- gönderilen bilginin içindeki bit'lerle matematiksel hesaplar yaparak bu sonucu da bilgiyle göndermek suretiyle, bir mesaj içindeki hataları belirleme metodudur. Alıcı cihaz da aldığı mesajın üzerinde aynı matematiksel işlemi yaparak sonucu mesajla birlikte gönderilenle karşılaştırır. Eğer sonuçlar birbirinin aynısı değilse, mesajı aldığı cihazdan bilgiyi yeniden göndermesini ister.

**Broadcast Adresi nedir?**

Gönderilen bilgi paketinin tüm cihazlar tarafından alınmasının istendiğini belirten özel bir adrestir.

| **Kablolama****** |
| --- |

**
****1OBase5; 10Base2, 10BaseT, 10Broad36 ne anlama gelmektedir?**

Bunların hepsi de farklı Ethernet tiplerini belirten IEEE isimleridir. Buradaki \` 10' sinyalin hızını belirtmektedir (10MBit/saniye). \`Base' Baseband'in kısaltılmışıdır. Aynı şekilde \`broad' da \`Braoadband'in kısaltılmışıdır. Daha sonrasında yer alan rakam da, bir segmentte kablonun maksimum uzunluğunu belirtir. Bu durum sadece \` 10BaseT'de bozulmaktadır. Burada \`T' kablonun \`twisted pair' olduğunu belirtmek için kullanılmıştır. Aynı şekilde, \` 10BaseF' içerisinde kullanılan \`F' de, kablonun fiber olduğunu belirtmektedir.

**10Base2**

İnce coaxiel kablo üzerinde 10Mbit hızında Ethernet demektir. Ucuzluğu nedeniyle \`Cheapernet' (ucuz net) veya ince kablo kullanıldığı için ince ethernet diye de anılır.
**
****1OBase5**

Kalın coaxiel kablo üzerinde 10Mbit hızında Ethernet. Kalın ethernet diye de anılır.

**10BaseF**

Fiber kablo üzerinde 10Mbit hızında Ethernet.
**
****10BaseT****
**
Unshielded (zırhsız) twisted pair kablo üzerinde 10Mbit hızında Ethernet (günümüz networklerinde ençok kullanılan tip).
**
****10Broad36**

Broadband yayın yapan kablo üzerinde 10Mbit hızında Ethernet
**
****Ethernet'te kablo kısıtlaması var mıdır?**

Gerek uzaklıkta, gerekse kullanılan cihaz sayısı ve bağlanan kullanıcıların sayılarında kısıtlamalar vardır.
**
****1OBase2****
**
Segment başına maksimum uzunluk 185 m ile sınırlıdır.
**
****1OBase5****
**
Segment başına maksimum uzunluk 500 m.ile sınırlıdır.
**
****1OBaseF****
**
Kullanılan sinyalleşme teknolojisine göre, fiber kablo 2 km.'ye kadar gidebilir.
**
****10BaseT****
**
Segment başına maksimum uzunluk 100 m

**1OBroad36****
**
Segment başına maksimum uzunluk 3600m ile sınırlıdır.
**
****Segmetleri büyütürken uygulanan kısıtlamalar 5-4-3 kuralı****
**
Ethernette maksimum 4 repeater ,5 segment(bunun sadece 3 ü kullanıcı segmenti) kuralı vardır. Mesafeyi arttırmak için repeater denilen cihazları ekleyerek yeni bir segment eklemek mümkün olmaktadır. Ancak, bu kullanılan repeater cihazlarının sayısı maksimum 4 adet olabilmektedir. Böylelikle, toplam 5 adet segmentiniz olabilmektedir. Ancak, bunların sadece 3 tanesine kullanıcı ya da başka cihazlar bağlamanıza izin verilmiştir. Geri kalan 2 tanesi, sadece mesafe uzatmak için kullanmaktadır. Network içerisinde bir noktadan diğerine giderken, bu kuralın ihlal edilmediğinden emin olunması gerekir. Aksi takdirde, networkte ciddi problemler olabilir. Bu sayıların da üzerine çıkmak istiyorsak veya segmentlerdeki performans problemlerini gidermek istiyorsak, bu durumda, bridge (köprü), router (yönlendirici) ya da switch kullanılması gerekmektedir.
|Ayrıntı için|
**
****Bağlanan istasyon (kullanıcı ve/veya cihaz) sayılarındaki kısıtlamalar
**
10Base2 standardında, bir segment içinde, birbirlerinden 50 cm. uzaklıkta olmak şartıyla maksimum 30 adet cihaz bağlanabilir. 1OBase5 standardında, bu sayı birbirlerinden 2,5 m. uzaklıkta olmak şartıyla, maksimum 100 olabilmektedir. 10BaseF ve 10BaseT yıldız topolojide oldukları için her bir cihaz direk olarak repeater/hub adı verilen network cihazına bağlıdır ve burada mesafe, maksimum kablo uzunluğuyla sınırlıdır. Bu standartlarda network başına maksimum 1024 adet cihaz bağlanabilir.

**Tek bir segmentte 10Base2 ve 10BaseT standartları aynı anda kullanılabilir mi? **

Farklı kablo tiplerini kullanırken arada geçişi sağlamak amacıyla repeater kullanılarak mümkün olur.
**
****Kablosuz ethernet var mıdır?**

Birçok firma, bu alanda, spread-spectrum radyo transmiyonu, laser, mikrodalga gibi değişik teknikler kullanarak kablosuz ethernet ürünleri üretmişlerdir. Ancak bu alanda belli bir standart oturtulmadığı için, maalesef, bir üreticinin ürününün diğeriyle birlikte çalışması çoğu zaman mümkün olamamaktadır.
**
****Kablo seçimi****
**
10Base2 veya 10BaseT arasında seçim yapmak gerektiğinde, dikkate alınacak iki konu mesafe ve fiyat olmaktadır. Her ikisi de bina içi kablolama da kullanılan standartlar olmak birlikte, bugün 10BaseT yavaş yavaş 10Base2 standardının yerini almış gözükmektedir. Bina içinde kullanılacak kablolarda seçim 10Base2 veya 10BaseT yönünde olurken iki bina arasında daima 10BaseF kullanılması iyi olur. Fiber kablo içinde manyetik bir alan oluşmaz ve bina dışlarında yıldırımdan korunmak için idealdir. Yüksek manyetik alanların bulunduğu ortamlarda da kullanılması bilginin doğru transferi açısından önemlidir. 10Base5 omurga oluşturmada veya 10BaseF in daha ucuz alternatifi olarak karşımıza çıkabilir.

| **CABLE TYPES****** **CG NETWORK APPLICATIONS****** **BANDWIDTH****** COAXIAL Thin 10Base2 10Mbps Thick 10Base5 10Mbps TWISTED PAIR Unshielded Twisted Pair - UTP 10BaseT 100BaseTX 1000BaseT 10Mbps 100Mbps 1000Mbps Shielded Twised Pair - STP 10BaseT 100BaseTX 1000BaseT 10Mbps 100Mbps 1000Mbps Foiled Twisted Pair - FTP 10BaseT 100BaseTX 1000BaseT 10Mbps 100Mbps 1000Mbps FIBER OPTIC Single Mode (laser) or Multi Mode (led) 10BaseF 10-20Mbps Single Mode (laser) or Multi Mode (led) FDDI 100Mbps Single Mode (laser) or Multi Mode (led) 100BaseFX 1000BaseSX/LX 100-200Mbps 1-2Gbps |
| --- |

## **TOPOLOJİ NEDİR ?******

Topolojiye network alt yapısı kurulurken, kullanılacak kablolama biçimi diyebiliriz. Seçilecek topoloji kurulacak sistemle de alakalıdır.

Fiziksel olarak kablolama yaparken üç tip topoloji seçeneği vardır :
Bus, star, ring.

Bus : Bu tip topolojide tek bir hat tüm terminalleri dolaşır. Kablonun her iki ucu uygun omajda bir direç ile sonlandırılmalıdır. Genellikle koaksiyel kablo kullanılır. Ucuz ve kurulumu kolay bir çözümdür. Ancak tüm terminalleri tek bir kablo dolaştığı için, kablonun herhangibir noktasındaki problem (temassızlık, kopukluk, kısadevre vs.) tüm sistemi çökertir.

Star : Her terminale ayrı kablo çekilir. Daha sonra bu kabloların uçları, hub adı verilen cihaza takılır. Kablolardan birinde oluşan problem, sadece o kablo üzerindeki tek terminali etkiler. Günümüzde en sık tercih edilen kablolama tipidir. Genelde Twisted Pair kablo kullanılır.

Ring : Tüm aygıtlar, birinden diğerine olacak şekilde bağlıdır. Bu topoloji, IBM'in sistemlerinde kullanılan bir topolojidir (Token-Ring). Sistemde dolaşan ve jeton adı verilen bir taşıyıcı sinyal veri iletişimini sağlar.

| **Thin Ethernet 10base2****** |
| --- |

***Koaksiyel Kablo***

Coaxiel kablo, merkezde iletken kablo, kablonun dışında yalıtkan bir tabaka, tel zırh ve en dışta yalıtkan dış yüzeyden oluşur. Coaxiel kabloya örnek olarak evlerimizdeki anten kablosunu verebiliriz. Ama anten kablosu 75 ohm, network için kullanılan koaksiyel ise 50 ohm'luktur. Coaxiel kablo sinyal zayıflaması ve manyetik alanlara karşı diğer kablo türlerine göre daha dayanıklıdır. Bu nedenle coaxiel kablo uzak mesafelerde ve kritik veri transferlerinde UTP kabloya göre daha güvenlidir. Coaxiel kablonun değişik formları bulunur. Bunlardan en çok kullanılanları thinnet ve thicknet coaxiel kablodur. Aslında coaxiel kablo, RF (radyo frekans) ve bazı data transmisyonu için kullanılan metalik bir elektrik kablosudur. Kablonun ortasında elektrik geçirmeyen dış kaplamayla çevrili iletken, belli bir kalınlıkta ve yüksek rezistanslı bir tel yer alır. Bu yüzden network gibi yüksek frekanslı uygulamalar için uygundur. Fakat, daha kısa mesafede kullanılan (100 metre) UTP ve STP tipi kablolar diferensiyal modülasyon tekniği kullandığı için coaxiel kabloya nazaran network uygulamaları için daha uygundur.

Thinnet veya ince kablolu ethernet 50 ohm 1/4" kalınlığında yumuşak coaxiel kablodur. Bu özellikteki kablonun standart adı RG-58 dir. İnce ethernet kısa mesafelerde ve bilgisayarlar arasında kablolamanın kolay olduğu yerlerde kullanılır. İnce ethernet bir T konnektor ve bir BNC konnektor ile ağ kartına takılır.
Thin ethernet standardı 10 Mbit Baseband özelliğinde koaksiyel kablo ile yapılan kablolamadır.

Kablonun iki ucu da 50 direnç ile sonlandırılmalıdır. Bu durumda 1/R=1/50+1/50=1/25
R=25 ohm olacaktır.

Herhangi bir T konnektörün ucu Ohmmetre ile ölçüldüğünde 25 ohm okunmalıdır. Kablo uzarsa 25~30 ohm okunabilir. Eğer 0 ohm okunuyorsa kısa devre vardır, sonsuz gösteriyorsa kopukluk vardır veya sonlandırıcı bozuktur.

Topraklama : Kablonun iki ucundan biri topraklanmalıdır,diğeri ise topraklanmamalıdır.

Şekildeki gibi T konnektörün ucu network kartına takılmalıdır. Aşağıdaki doğru bir bağlantıdır.

Aşagıdaki ise yanlış bir bağlantıdır.

Eğer yukardaki gibi bir durumla karşılaşılırsa :

Veya uzun mesafeler için;

yapılabilir.

Aşağıda gerçek bir bağlantıyı görüyosunuz :

Kablonun sonlandırılmasında kesinlikle 50 ohm direnç kullanılmalıdır. Piyasada hazır sonlandırıcılar (terminatör) bulunabilir. İki tip sonlandırıcı vardır :

Bunlardan bir tanesi topraklamaya müsaittir. Kablonun bir ucunda bu kullanılmalı ve toprağa bağlanmalıdır.

**Topraksız terminator**.

**Zincir vasıtası ile toprağa (bilgisayarın metal bir noktasına) bağlanarak topraklama yapılabilecek, topraklı terminatör.******

**Network sistemlerinde topraklama hayati önem taşır.**

Topraklaması doğru yapılmamış bir sistemde veri güvenliği sağlanamaz. Doğru topraklama için binada toprağa gömülmüş bir bakır levha ya da bakır çubuğa bağlantısı yapılmış toprak hattı olmalıdır. Eğer buna imkan yoksa geçici bir çözüm olarak toprak hattı nötr hattına bağlanarak "sıfırlama" yapılabilir. Sonuçta doğru yapılmış bir topraklamada daima prizde voltmetre ile şu değerler alınmalıdır: (F faz,N nötr,T toprak)
F-N= 220 V (doğal olarak)
F-T=220 V
N-T=0~1 V (Eğer burada 40-50-60 gibi acayip ve değişken değerler varsa topraklamada problem olduğu kesindir. Ve bu arızalara,veri kayıplarına yol açacaktır.)
Eğer daha önce anlatılan, network hattının topraklanması yapılmaz ise, bir makinadaki elektrik kaçağı tüm sisteme koaksiyal kablo ile yayılır. Bazen koaks kablo ile herhangi bir terminalin şasesine dokunduğumuzda çarpılıyorsak, kesinlikle bir yerlerde kaçak veya topraklama hatası vardır.

Çok segmentli network :

Kablolama yapılırken kablo boyu sınırlamaları vardır. 185 metreden uzun kablolamalarda "repeater" kullanılmalıdır. Bu cihaz zayıflayan network sinyalini güçlendirerek iletir.

| \| Bir networkte birden fazla repeater kullanılabilir,ancak onun da bazı limitleri vardır.\| |
| --- |

## **Büyük Networklerde 5-4-3 Kuralı******

Bir networkün büyümesinin bazı sınırları vardır. Repeater ve hublar bu limitleri genişletmekte kullanılır. Ancak daha büyük networklerde network hızını ve veri sağlamlığını koruyabilmek için Switch'ler kullanılır.

Thin ethernetin kuralı şudur:

Ve maksimum 30 bağlantı.

Kablo, Repater kullanılıp,sinyal güçlendirilerek uzatılabilir:

Her bir repeater segmentte bir node (uç) olarak kabul edilir. Networkün herhangibir yerinden bağlanabilir. Ancak eğer networkünüz ikiden fazla repeater kullanıyorsa bazı kısıtlamalar ortaya çıkar.

Kısıtlamalar şunlardır :

Ethernet sinyali kaynak noktasından hedef istasyona kadar şunlardan geçerek gezebilir :

Max 5 segment

Max 4 repeater veya Hub

Max 3 populated segment. (Populated segmentler 2'den fazla uç içeren segmentlerdir,un-populated segmentler ise tek bir uçta sonlanan segmentlerdir. 10baseT segmentler non-populated segment olarak kabul edilirler.)

Buna göre 10baseT hub bir repeater gibidir,ve 10baseT hub 10 base2 üzerinde bir tek sistem gibi kabul edilir.

Ethernet sinyali en fazla 4 repeater veya hub'ı geçebilir.

**Networkün Geçerli Yapılması******

Aşağıda geçerli bir networkü görüyorsunuz. 5 adet hub olmasına rağmen geçerli. Çünkü uygun konuma konulan bir switch networkü geçerli kılıyor.

Bu örnekte A ile B bilgisayarları arasındaki segment (kablo parçaları) sayısı sadece üç tane, bunun sebebi, üçüncü parçadan sonra başka bir hub daha kullanmak yerine switch kullanılmasıdır. Switch parçaların tekrar sayılmasını başlatarak sayının standartlar içinde kalmasını sağlamıştır. Bir switch veya bridge birbirine bağlı iki hubı takip etmelidir. Bu örnekteki hubların hepsine bilgisayarları direk olarak bağlayarak doldurduğumuzda 40 bilgisayar içerir. Bununla birlikte hala hub sayısını sekize çıkararak genişleyebilme imkanımız da vardır.

Asağıda ise sadece 5 hub içeren geçersiz bir networkü görüyorsunuz. Bu örnekte A ile B bilgisayarları arasındaki segment (kablo parçası) sayısı altı tanedir ve Ethernet standartlarının dışındadır.

Birbirine bağlı iki habı takip eden switch veya bridge yok. Kablo sayısının beşi aşması A ile B bilgisayarları arasındaki sinyallerin gecikmesine ve zayıflamasına neden olur. Bu örnekteki network önceki örnekten küçük bir network olmasına rağmen geçersiz bir networkdür.

| **Twisted Pair Ethernet 10baseT/UTP****** |
| --- |

Twisted Pair (Çift dolanmış sarmal) kablo, bazen UTP (unshielded twisted pair) olarak da geçer. Evlerimizdeki telefon kablolarına benzer bir yapıdadır. Bu kablonun ucuna 8 bağlantı noktası olan (yukarıdaki resim) RJ-45 jak takılır ve bilgisayarımızdaki network kartına bağlanır. Evlerimizde telefonlarımızın arkasına giren RJ-11 kodlu jaktır ve 4 bağlantı noktası mevcuttur (ancak biz ortadaki iki tanesini kullanırız, telefon teli 2 tanedir çünkü -bazı ülkelerde de bu dört yoldan dıştaki iki tanesi kullanılır, modemlerin içinden çıkan kablo bazen böyle olabiliyor, buna dikkat edin-). 10Mbit kablolamada Category 3 veya Category 5 kablo kullanılabilir. Ancak günümüzde kablo fiyatları düşünüldüğünde direkt CAT5 kullanmak en sağlıklı yoldur. CAT5 kablo 100Mhz 'e kadar veri iletimini güvenli kılar. 8 adet birbirine dolanmış, ayrı olarak reklendirilmiş, tek damarlı kaliteli bakır telden yapılmıştır. İki tipi mevcuttur: Kaplamalı (shielded) ve kaplamasız (unshielded). Kaplamalıda tel çiftlerini örten metal bir koruma ve bunun üstende plastik kılıf mevcuttur. Kaplamasız da ise sadece plastik kılıf ile tel çiftleri birarada tutulur.

Tüm bunların yapılış sebebi (çift dolama,metal kılıf) kablodan geçen sinyalin çevredeki elektromanyetik alanlardan geçerken bozulmasını önlemektir. Motorlar, fülorasan lambalar, elektrik kabloları vb. birer elektromanyetik alan üretecidirler.

Bu arada şunu da söylemek gerekiyor, 100 Mbit çalışacak ve veri güvenliğinin ön planda olduğu bir networkte, sadece kullanılacak kablonun değil, jak'tan, duvar prizine kadar tüm kablolama parçalarının CAT 5 standardında olması gerekir. Unutmayın "zincir, en zayıf halkası kadar sağlamdır ! ".

Dolanmış çiftlerin manyetik koruma özelliğinden faydalanabilmek için
renk sıralamasına dikkat etmek gerekir
(doğru renk sıralaması için sayfanın devamına bakın).

Dikkat ! Eğer kullandığınız network kartı COMBO ise, yani hem 10base2 T konnektor girişi, hemde 10baseT RJ-45 jak girişi var ise network kartının ayarlarında kullandığınız, yani kablonun takılı olduğu girişi aktif hale getirmeyi unutmayın. Günümüzde bir çok network kartı bunu otomatik olarak yapacaktır.

**HUBLAR:**

Twisted Pair kablolamada bilgisayarları birbirine bağlamada HUB adı verilen cihazlar kullanılır.
Bu tip kablolama Star(yıldız) topolojisine göre yapılır.Yani her bir terminale kendisine ait bir hat çekilir. Daha sonra tüm bu hatların uçları, Hub adı verilen cihazda birleşirler.

Hub'lar herhangi bir portuna takılı kablo üzerinden gelen network sinyalini güçlendirerek diğer portlara iletir.

Hublar çoğu zaman ayrı bir güç beslemesine ihtiyaç duyarlar. Bunun için hub'la beraber bir adaptör veya direk prize takmak üzere power kablosu gelecektir.

Hub'lar 5-8-16-24 ... portlu olabilirler. Birçok Hub'da ayrıca bir adet 10base2 Thin Ethernet konnektörü bulunur.

Sistem açıkken dahi Hub üzerinden herhangi bir kabloyu söküp takabilirsiniz. Ayrıntı için Twisted Pair ve Koaksiyel sayfasına bakın.

Netwokünüz büyüdükçe birden fazla hub'a ihtiyaç duyacaksınız.

Dikkat! Eğer iki Hub'ı birbirine bağlayacaksanız şuna dikkat edin : Bazı Hub'larda diğer bir Hub bağlantısı için özel bir port bulunur, yada en son port bir ayar anahtarı ile normal bağlantı portu veya diğer bir Hub bağlanması için konfigure edilebilir. Eğer elinizdeki böyle bir cihazsa, gerekli ayarı yaptıktan sonra normal bir TP kablo ile iki hub'ı birbirine bağlayabilirsiniz. Ancak Hub üzerinde böyle bir ayar veya özel port yoksa, yani tüm portlar normal bağlantı içinse iki hub arasında CROSS kablo kullanmalısınız.

Çok büyük ağlarda birden fazla hub kullanılır.

Sıklıkla 10base2 bir kablonun Backbone(omurga) olarak kullanıldığı,10baseT ağlar
görebilirsiniz.

Burada tüm netwok trafiği sonuçta backbone üzerinde olacaktır. Günümüzde backbone olarak Fiber kablolar kullanılmaktadır.Thin Ethernet en fazla 10 Mbit veri aktarım hızını desteklediği için günümüz hızlı networklerinde backbone olarakta kullanılmaz.

**Eğer sadece iki bilgisayarı TP kablo ile bağlayacaksanır hub'a gerek yok !******

Ancak burada kullanacağını normal bir kablo değil CROSS kablodur.

**KABLO BAĞLANTILARI******

10 Mbit Twisted Pair normal kablo bağlantısı:

Pin

JAK #1

<---kablo--->

Pin

JAK #2

1

White/Orange

1

White/Green

2

Orange/White

2

Green/White

3

White/Green

3

White/Orange

6

Green/White

6

Orange/White

Görüldüğü gibi 10Mbit (10baseT) bağlantıda yalnızca 4 tel kullanılır.
100mbit bağlantıda ise 8 telin hepsi de kullanılır.
Kural olarak normal kabloda (cross değil ! ) hiçbir şekilde çaprazlama yada
karışıklık yoktur. Yani birinci jakın 1 nolu pini,diğer jakın 1 nolu pinine, iki ikiye ...
bağlanır.

10 Mbit Twisted Pair CROSS kablo bağlantısı:

Pin

JAK #1

<---kablo--->

Pin

JAK #2

1

White/Orange

3

White/Green

2

Orange/White

6

Green/White

3

White/Green

1

White/Orange

6

Green/White

2

Orange/White

Bir Numaralı Pin Nerede ??

Netwok Kartınızın girişi :

Kablo üzerindeki Sinyaller:

Pin

Kablo

Sinyal

1

White/Orange

Transmit -

2

Orange/White

Transmit +

3

White/Green

Receive -

4

Blue/White

5

White/Blue

6

Green/White

Receive +

7

White/Brown

8

Brown/White

| **Twisted Pair Ethernet 100baseTX****** |
| --- |

10baseT ve 10base2(Thin ethernet) maksimum 10 megabit veri hızını desteklerken 100BaseTx ile 100 megabit veri hızına ulaşmak mümkündür. 100BaseTx hızında çalışabilmek için, bir zincir en zayıf halkası kadar güçlüdür kuralı nedeniyle tüm sistemin 100mbit olarak tasarlanmış olması gerekir.
Yani birbiri ile haberleşecek tüm terminallerde 100mbit'lik ethernet kartı (fast ethernet) takılı olması, aralarında 100mbit standardında (8 tel) CAT5 kablolama yapılması ve kullanılan Hub'ında 100Mbit'lik Hub olması gerekir.

**100baseTx sadece CAT5 kablo ile çalışır.**

Kablodan tasarruf etmeye çalışmayın, 100Mhz çok yüksek bir frekanstır. Unutmayın network sistemlerinde kablolama toplam maliyetin %1-2 'si kadar tutarken, çıkan arızaların %70-80'inin sebebidir.

**Kablo bağlantıları**

**100Mbit için Normal Bağlantı ve sinyaller**
(8 telde paralel gidiyor, yani 1'e 1, 2'ye 2... bağlanıyor.)

**Signal A******

**Pin A**

**Signal B******

**Pin B**

**Tx\_D1 +******

**1**

**Tx\_D1 +******

**1**

**Tx\_D1 -******

**2**

**Tx\_D1 -******

**2**

**Rx\_D2 +******

**3**

**Rx\_D2 +******

**3**

**Rx\_D2 -******

**6**

**Rx\_D2 -******

**6**

**Bi\_D3 +******

**4**

**Bi\_D3 +******

**4**

**Bi\_D3 -******

**5**

**Bi\_D3 -******

**5**

**Bi\_D4 +******

**7**

**Bi\_D4 +******

**7**

**Bi\_D4 -******

**8**

**Bi\_D4 -******

**8**

Renklere göre bağlantı ise şöyle:
(bu görüntü jakın ucu ileri ve metal pinleri bize bakıyorken ki hali, yani tırnak altta)

Her iki ucu yaparken de, yukarıdaki gibi bağlamalısınız !

**100 Mbit Cross Kablo Bağlantısı ve Sinyaller******

**Signal A******

**Pin A**

**Signal B******

**Pin B**

**Tx\_D1 +******

**1**

**Rx\_D2 +******

**3**

**Tx\_D1 -******

**2**

**Rx\_D2 -******

**6**

**Rx\_D2 +******

**3**

**Tx\_D1 +******

**1**

**Rx\_D2 -******

**6**

**Tx\_D1 -******

**2**

**Bi\_D3 +******

**4**

**Bi\_D4 +******

**7**

**Bi\_D3 -******

**5**

**Bi\_D4 -******

**8**

**Bi\_D4 +******

**7**

**Bi\_D3 +******

**4**

**Bi\_D4 -******

**8**

**Bi\_D3 -******

**5**

| Cross Bağlantı Diagramı *Kablonun renklerine dikkat etmeden, ancak doğru pinler birbirine bağlanacak şekilde bağlarsak da sistem çalışır. Ancak tel çiftlerinin birbirine dolanması ile oluşan manyetik alan korumasından faydalanmamış oluruz !*** |
| --- |

**Twisted Pair veya Koaksiyel****
****Güvenilirlik / Avantajlar******

Hangi tip kablo kullanmalıyız ?? Koaksiyel veya TP.
Eğer sadece 2 bilgisayarı bağlıyacaksanız koaksiyel iyi bir çözümdür. Veya Cross kablo yaparak,Hub kullanmadan TP kablo ile çok ucuza halledebilirsiniz.
Ancak 3 ve daha fazla sistem için durup biraz düşünelim !

Avantaj/Dezavantaj

Twisted Pair

Koaksiyel

Maliyet

Hub nedeniyle pahalı

Çok ucuz

Kurulum

Kolay

Kolay

Kullanılan Topoloji

Star

Bus

Güvenlik

Yüksek

Düşük

Maksimum hız

100Mbit

10 Mbit

Günümüzde gerek ekipmanların ucuzlaması, gerek hız avantajı ama bilhassa kullandığı topoloji nedeniyle kablo arızalarının tüm sistemin çökmesini engellemesi nedeniyle Twisted Pair kablolama tercih edilir.

Şimdi bus yapıdaki aşağıdaki şekle bakalım :

Kablonun herhangi bir noktasındaki bir arıza tüm sistemin çökmesine sebep oluyor:

Ancak TP kablolamada her terminale ayrı bir kablo gittiği için ;

Kablolardan birinde bir problem olsa da;

sadece tek bir terminal devre dışı kalır. Tabii Server-Client bir sistemde serverin bağlı olduğu kablo arızalanırsa bu da dolaylı yoldan sistemin işlemez hale gelmesi demektir : )

Ancak her halukarda TP kablolamada arıza bulma ve giderme daha kolaydır. Bus topolojide sistem çalışırken terminal eklemek ve çıkarmak mümkün değilken,TP sistemde istediğimiz zaman herhangi bir makinanın jakını hub dan çıkarıp-takabiliriz.
Bu sebeplerden ötürü,günümüzde tüm network sistemleri Twisted Pair, star topoloji üzerine kurulmaktadır.
Artık küçük ev networklerinde bile TP kablolamayı tercih etmelisiniz, Tabii 100 Mbit avantajı da oldukça önemli.

## **Repeater-Hub-Switch******

Networkler sürekli gelişme ve büyüme trendindedir. Gün geçtikçe
daha çok repeater ve hub kullanılmaya başlanır.

10base2 - Thin Ethernet (Coax):

10baseT - Twisted Pair (TP/UTP):

Fakat bu şekilde networkü büyütmek, bir süre sonra network performansında ciddi
düşmelere sebep olur.

Hub ve repeater'lar akıllı olmayan cihazlardır. Bu cihazlar herhangi
bir porta gelen sinyali yükseltip diğer tüm portlara yollar. Böyle
olunca tek bir terminalin aktivitesi ile tüm segmentler ve tüm network
meşgul hale düşer. Ethernetin çalışma prensibi gereği iki cihaz aynı segmentte aynı anda veri paketleri gönderemeyeceği için network performansı düşer.

Böylece aynı anda birden fazla terminal veri yollamak istediğinde :

sinyaller çarpışır,her iki sinyal (veri paketi) de iptal edilir, zaman
israf edilir. Her iki terminal de rastgele bir süre bekleyerek tekrar
denerler. Tüm bunlar sistem performansını düşürür.

Bu problemleri network optimizasyonu ile gidermek mümkündür.

Bridge (köprü) : Network sistemlerinin ilk yıllarında bridge'ler ilk
"akıllı" cihazlar olarak kullanılmaya başlandı. Bu cihazın iki portu
vardır. Bir porttan gelen sinyali eğer ihtiyaç yoksa (diğer
segmentteki bir makinaya gitmeyecekse) diğer segmente yollamaz.
Böylece büyük bir networkü 2 küçük networke bölmüş olur.

Switch: Switch'ler ise gerçekten çok akıllıdırlar. 2 den fazla portları
vardır ve aynı anda 2 den fazla iletişim yaptırabilirler. Bir porta gelen
sinyali inceler ve sinyalin gitmesi gereken mac adresine sahip
network kartı hangi portuna bağlı segmentte ise ona gönderir. Diğer
portlara göndermez.

Büyük bir networkte aynı anda bir çok veri aktarım isteği olur :

Yukarıdaki animasyonda Switch'in tam olarak ne yaptığı
çok güzel anlatılıyor.

Gerçekten yüksek performanslı bir networke sahip olunmak isteniyorsa,network trafigi iyi izlenip analiz edilmeli ve networkün yapısı ona göre düzenlenmelidir.

Tek SERVER'lı yapı:

Burada bir Hub'ı Switch ile değiştirmek çok şey ifade etmez,çünkü
hala TP-Hub'dan servere bir darboğaz vardır.

Multi Server configuration:

Eğer network trafiği genelde workgroup'ların kendi içinde ise, yani
workgrouplar arasında çok fazla trafik yoksa Switch network
performansını arttırmakta kullanılabilir. Yukarıdaki şekilde
Department1'in kendi içinde gerçekleşen hiçbir iletişim Dep2 ye aktarılmaz,
aynı şekilde de Dep2'nin kendi içindeki iletişimi Dep1'i meşgul etmez.

10 Mbit networkü 100Mbit server bağlantısı ile optimiz etmek :

Halihazırdaki 10mbit sistemlerin performansını arttırmak için
Server ile sistemin bağlantısı 100Mbit yapılabilir.
Ancak yukarıdaki şekilde Blackbox olarak isimlendirilen cihaz,
eğer bir hub veya 10/100 Otomatik ayarlı hub ise
hala segmentteki tek bir terminalin gönderdiği sinyal tüm sistemi
meşgul edeceği için performans artışı istenen seviyede olmaz :

Eğer Blackbox bir switch ise her bir terminal server ile tam 10 Mbit
bağlantı kurabilir. Çünkü switch bir terminalden servere giden
bir veri paketini diğer terminallere yollamaz. Böylece gereksiz trafik,
çarpışmalar, zaman ve performans kaybı önlenmiş olur.
Aynı zamanda birden fazla terminal server ile haberleşebilir, üstelik
performans kaybı olmaksızın !

Zaten çoğu zaman bir server aynı anda birçok istek alır. Ancak
ethernetin yapısı gereği (eğer switch kullanılmamışsa) aynı anda
sadece bir terminale cevap verebilmektedir. Doğru konumdaki
bir switch sistem performansını doğrudan etkiler. Server'ın da
tam kapasite kullanılabilmesine imkan tanır.

Kablo altyapısını 10Mbit'ten 100Mbit'e değiştirmek bir çok işyeri
için pahalı ve zahmetli olduğu için, 10Mbit Hub'ları 10/100 Mbit
Switch'ler ile değiştirip,server'ın bağlantısını da 100Mbit'e yükseltip
çok uygun bir çözüm üretmek mümkündür.

| **Temel Bilgiler**** ****** |
| --- |

Windows Network Setup çok karışık değildir,siz sadece gereken
modülleri yükleyin.

Şunları yüklemeniz ve/veya ayarlamanız gerekli :

Öncelikle network kartının driverini yüklemelisiniz.

Bir protokol yüklemelisiniz. (Tüm sistemlerde aynı protokol
yüklü olmalı)

Windows'ta "NetBEUI","IPX/SPX" ve "TCP/IP" den birini
tercih etmelisiniz.

Bir Client-Module (istemci) yüklemelisiniz. Bu sizin diğer
makinaların disklerine erişebilmenizi sağlayacaktır.

Eğer başkalarının sizin sisteminizin kaynaklarını (disk,printer,
floppy vs.) kullanmasını istiyorsanız "***File and Printer ******
******Sharing***" (dosya ve yazıcı paylaşımı) yüklemelisiniz.

| **Basit Bir PC-to-PC networkte hangi protokol kullanılmalı ?****** |
| --- |

Windows 95,98 ve NT size 3 tane protokol kullanma imkanı sunar :

"*IPX/SPX-protocol*" Novell firması tarafından Novell-Netware Server'lar için tasarlanmıştı. Bu çok hızlı ve yönlendirilebilir bir protokoldür (büyük işletmelerde Win9x sitemlerin netware server'lara bağlanmasında da kullanılır. Dikkat : Bu protokol farklı Frame yapıları kullanır. Lütfen IPX/SPX Temellerine ve IPX Frame Tuzağına bakın !).

"*NetBEUI*" Microsof tarafından kendi Workgroup-Networklerinde (Windows 3.11 for Workgroups ? Windows NT 3.1/3.51 Servers?) kullanılmak üzere tasarlandı.

NetBEUI oldukça hızlı,ayar gerektirmeyen ve tüm windows makinalarını birbirine bağlamakta kullanabileceğiniz bir protokoldür.

(NT4 altında NetBEUI konfigure edilemez. Bu seçenek gridir.)

Ve "*TCP/IP*" : Şimdi size Arpanet'ten başlayarak anlatacak değilim, ancak TCP/IP wide area networklerde (WAN) kullanılmak üzere tasarlanmış bir protokoldür. Buna karşılık IPX/SPX ve NetBEUI yerel ağlar için (Local area network-LAN) tasarlanmışlardır. Ve Tcp-ip'ye göre yerel ağ üzerinde daha hızlıdırlar. Ancak Tcp-ip sizi dünyanın heryerine bağlayabilir. Bunu NetBEUI ile yapmak mümkün değildir.

Tcp-ip oldukça komlike bir yapıdadır. Bir Tcp-ip ağında bir çok şeyi ayarlamanız gerekir (IP-address, subnet-mask, gateway, DNS, DHCP, WINS,.....):

Benim önerim şu olacak : Direk Pc-to-Pc networklerde NetBEUI kullanın,çünkü hızlı ve ayar gerektirmeksizin çalışır. Ancak IPX/SPX de oldukça iyi bir seçimdir (tüm oyunları network üzerinden ipx bağlantı ile oynayabilirsiniz).
Ancak hepsinin ötesinde eğer işin içine internet giriyorsa : TCP-IP.

| **Diske Networkten Erişmek****** |
| --- |

Genellikle networklerin kurulum amaçları diğer bir sistemin diskine veya yazıcısına erişmektir.
Diğer bir sistemin üzerindeki dataya network üzerinden erişirken, iki sistemde de şu olaylar gerçekleşir:

Birinci makinanın diğerinin diskine erişebilmesi için onun diskine "map" edilmesi, diğer makinanında diskinin "share" edilmiş olması gerekir.

Diğer sistemlerin diskine erişimine izin veren makinaya Network-Server denilir. Güvenlik için data'ya direkt erişim verilmez. Sadece data'yı kullanacak programa erişim hakkı verilir. Ancak güvenlik çok önemli değilse diğer kullanıcılara da data'ya erişim hakkı verilebilir.

Bütün harddiske veya sadece bir dizine (alt dizinleriyle beraber) erişim hakkı verebilirsiniz. Önce hangi dizini paylaştıracağınıza karar verin ve onun üzerine gelip tıklayın.

Daha sonra sağ mouse butonuna basarak menüyü açın ve "Sharing" i seçin.

RadyoButtonları kullanarak ayarlayın:

"Shared As" : Paylaşımın ismidir, buraya default olarak seçili olan dizinin ismi gelir. Fakat siz yeni bir isim verebilirsiniz. Paylaşılan nesne network üzerinde bu isimle görülecektir.

"Access-Type": Paylaşıma açtığınız nesneye erişim tipidir. Read-Only'yi seçerseniz networkten bu kaynağa erişenler sadece verilerinizi okuyabilirler, kopyalayabilirler.
Ancak veriler üzerinde harhangi bir değişiklik (silme, taşıma, içeriğini değiştirip kaydetme vs.) yapamazlar. "Full" seçeneğini seçerseniz aynen kendi diskleri üzerinde çalışıyormuşçasına hertürlü işlemi yapabilirler.

Artık disk veya dizininiz network üzerinden erişilebilir haldedir.
Artık paylaşıma açtığınız nesnenin üzerinde bir el resmi belirir.

Networkte diğer bir makinanın diskine veya diğer kaynaklarına (yazıcı mesela) erişen makinaya Client denir.

Windows 9X ve Nt4 te networke genellikle masaüstündeki "Network Neighborhood" ikonundan erişilir:

Önce networkten bir sistemi çift tıklayın. Karşınıza o sistem üzerindeki paylaşıma açılmış nesneler gelir. (disks, directories ve/veya printers) Bu nesnelerden birini açmak için üzerine çift tıklayın.

Yukarıdaki gibi network üzerindeki bir sistemin diskine veya diskindeki bir diznine eriştiniz. Eğer bilgisayrınızı her açtığınızda bu erişimi kullanacaksanız, "bilgisayarım" penceresinde bir icon olarak görünmesini sağlayabilirsiniz. Bu sanal diskiniz aynen kendi makinanıza bağlı bir harddisk gibi çalışacaktır. Bu sanal diski yaratmak (network drive) "***Mapping a Network drive***" olarak adlandırılır.

Bunu nasıl yapacağımıza bakalım :

Önce network üzerinde bir sistemi seçin. Bir sisteme (bilgisayara) map yapamazsınız. Menüdeki "map network drive" seçeneği gridir. Şimdi bu makina üzerinde paylaşıma açılmış nesneleri görmek için üzerinde çift tıklayın.

Network diski olarak seçmek istediniz nesneye sağ tıklayın ve "Map Network Drive" seçin.
(Bir Microsoft networkte,paylaşılmış bir disk veya dinizin alt dizinlerine map yapamazsınız. Bu ancak Netware Server'lar üzerinde mümkündür.)

Network diskinize atamak istediğniz sürücü harfini seçin. Eğer bilgisayrınızı tekrar açtığınızda bu bağlantının otomatik yapılmasını istiyorsanız "Reconnect at Logon" 'a tik koyun.

Burada sanal diskimizin path'ını "***\\\\P120\_home\\cserve***" olarak görüyoruz. Bu isimlendirme metodu **UNC**: **U***niversial* **N***aming* **C***onvention* olarak bilinir. Önce iki tane back-slash ile (***\\\\***) ile başlanır. Daha sonra network üzerindeki bilgisayarın ismi ve slash, ve paylaşılan kaynağın ismi yazılır.
Artık bu network sürücüsüne kendi harddiskiniz gibi erişebilirisiniz. Ancak onun bir netwok sürücüsü olduğunu anlamanız için farklı bir iconu olacaktır.

Network sürücüsü.

Diskini paylaşıma açan makinadaki durum.

Networkten bu diske erişen makinanın gördüğü.

| **TCP-IP Temelleri****** |
| --- |

Şimdi size Tcp-ip (Transmit Control Protokol-Internet Protokol) hakkında kısaca bilgi vermek istiyorum (oldukça kısa ! ). Bunu sizin daha kolay anlamanız ve kolayca uygulayabilmeniz için yapacağım. Ayrıca size Tcpi-ip'nin ve internetin tarihinden de bahsedecek değilim. Sadece kurulum gereksinimlerinizi karşılayacak bilgiler bulacaksınız.

IP-Adresi :

Önce şundan bahsedelim : Her bir ethernet kartının dünyada bir eşi-benzeri olmayan bir numarası vardır (mac adres). Bu 48 bit numaranın ilk 24 biti üretici kodudur, son 24 bit ise benzersiz bir numaradır ve sadece bu ethernet kartı için kullanılmıştır. Bir yerel ağ da (Local Area Network-LAN), NetBEUI veya ipx-spx protokollerinden biri kulanılırken bu protokoller her bir bilgisayarı (dolayısı ile bilgisayar üzerindeki ethernet kartını) diğerlerinden ayırmak için bu numarayı kullanır. Bu tip networklerde bilgisayarları birbirinden ayırdetmek için ayrıca bir numaralandırma yapmak gerekmez.
Ancak Tcp-ip geniş alan ağı olarak çevirebileceğimiz wan'lar (Wide Area Network-WAN) da kullanılmak üzere tasarlanmış bir protokoldür. Böyle bir sistemde networkün bazı bölümleri düzgün çalışmıyor olabilir (örneğin İstanbul'dan Arjantine gönderilen bir veri paketini düşünün,yüzlerce santral ve düğüm noktasından geçecektir !) . Sonuçta Tcp-ip kendine has bir numaralandırma sistemi kullanır (IP Adesleri).

Tcp-ip IP adresleri 32 Bit'liktir . Ip adresi 4 adet 8 bitlik parçadan oluşur (192.168.10.1 gibi). Bu parçaların herbirine oktet denir. Her bir parça 0 dan 255'e kadar değer alabilir (0 ve 255 in kullanımı ile ilgili sınırlandırmalar vardır). Eğer küçük-özel bir network kuruyorsanız herhangi bir ip adresini kullanabilirsiniz. Eğer bir şirketin networküne (veya bir kampüs networküne) bağlanacaksanız network yöneticisinden size bir ip adresi atamasını istemelisiniz. Ve eğer internete bağlanacaksanız internet servis sağlayıcınızdan size bir ip adresi vermesini istemelisiniz. Eğer şu anda internete bağlı değilseniz, ancak ilerde bağlanmayı düşünüyorsanız networkünüzü özel ağlar için ayrılmış 192.168.x.y aralığında tanımlayın. Böylece internete bağlandığınızda bunu değiştirmeniz gerekmez. Burada x her bilgisayarda aynı,y ise farklı olmalıdır.
3 sistemin kullanıldığı küçük bir network örneği:

Ip adreslerini Tcp-ip özellikler penceresinden ayarlayabilirsiniz.

Şimdilik Subnet Mask'a 255.255.255.0 girin. Bu dökümanın ileriki bölümlerinde buna değineceğim.
Evet bu kadar.
Bağlantının doğru çalışıp çalışmadığını ping komutu ile kontrol edebilirsiniz.

Eğer küçük bir netwokünüz varsa her makinaya elle ip numarası verebilirsiniz,ama bilgisayar sayısı 50 den fazla ise bu oldukça zor bir iş haline gelir. Ancak Tcp-ip size bu konuda bir kolaylık sağlar : "Otomatik bir ip adresi al" :

Bu otomatik tanımlamayı yapabilmek için network üzerinde dağıtılacak ip adreslerinin belirlendiği ve atamanın yapıldığı bir;
**
****DHCP** (**D**ynamic **H**ost **C**onfiguration **P**rotocol) server olmalıdır.

Her bir bilgisayar açıldığında network üzerinde bir DHCP-server var mı diye mesaj yollar (kendisine otomatik olarak bir ip adresi atansın diye). Atanan bu ip adresleri genellikle kalıcı olmaz, ancak bir süreye bağlı olarak atanmış olurlar (günler, aylar, haftalar boyunca olabilir, ancak internete dial-up bağlantıda bu sadece bağlantı süresincedir). Eğer sistem bu süre içinde DHCP-Server'a tekrar başvurursa ip adresinin süresi uzatılır. Ancak uzun bir süre, otomatik olarak ip adresinin atanmış olduğu sistem, DHCP-Server ile bağlantı kurmazsa, onun için atanmış ip adresinin süresi dolmuş kabul edilir ve bir başkasına atanmak üzere bekletilir. Kendisine verilen ip adresinin süresi geçen sistem yeni bir adres için tekrar başvurur.

Windows 95 te kendiliğinden bir DHCP-Server yoktur.
Bir windows nt server'a bağlanılması gerekir (DHCP-Server olarak tanımlanmış bir Nt server).

Windows 98'de DHCP-Server olmaksızın otomatik ip alma özelliği vardır.

Eveet. Şu ana kadar oldukça basit görünüyordu değil mi ? Bundan sonra biraz işin ayrıntısına girelim. Bilgisayarın kendi ip adresi var, ancak ethernet kartları sadece ethernet adreslerini bilirler. Tcp-ip networkte kendi reklamını yapar ve şöyle der : "Hey ben yaşıyorum,Ethernet adresim *'08000b 0a0238' ve IP-adresim de '192.168.10.2'* ".
Networkteki her bir terminal bu bilgilerden oluşan (hangi ip adresi hangi ethernete -dolayısı ile hangi bilgisayara- karşılık geliyor) bir tablo tutar ve bu tablodaki bilgiler -genellikle- 15 dakidada bir yenilenir.
Eğer sisteminiz diğer bir terminalle iletişim kurmak isterse, ve diğer bilgisayarla ilgili bilgi bu tabloda yer almıyorsa herkesin alacağı bir mesaj yollar (Broadcast mesaj).
"Hey, ben 192.168.10.4 ile haberleşmek istiyorum, fakat onun ethernet (mac) adresini bilmiyorum eğer o sensen bana mac adresini gönder" der. Networkte kim o ip ye sahipse kendi mac adresini gönderir. Diğer sistemler de bu mesaja bakar ve bir işlem yapmazlar (dolayısıyla broadcast mesajları da network trafiğini arttırır).
Bu işlem ARP (**A**ddress **R**esolution** P**rotocol) ve **RARP** (**R**eversed **A**ddress **R**esolution **P**rotocol) olarak adlandırılır.
ARP/RARP protokolleri lan'larda iyi çalışır,ama internette kullanılmaz. Tüm internete böyle broadcast mesaj yollanamayacağı için (milyonlarca bilgisayar var çünkü) kullanılması mümkün değildir.

***Gateway/Router****:*
Tcp-ip ağınızı başka bir Tcp-ip ağına bağlarken (internet bu şekilde bağlanmış networkler topluluğudur) bir cihaza ihtiyacınız olacak : **Gateway** veya **Router******

Genellikle Subnet-Mask '255.255.255.0' dır. Ancak eğer 207.68.137.53 ' e bağlanmak isterseniz (microsoft web sitesi),Tcp-ip senin ve bağlanmak istediğin yerin ip lerini ve subnet-mask larını karşılaştırır (mantıksal and işlemine tabi tutar). Bu karşılaştırma bit seviyesinde yapılır. Subnet-mask aslında ip adresinin ne kadarının network adresi, ne kadarının bilgisayarın özel adresi olduğunu ayırmaya yarar.

**System:******

**IP/subnet-mask******

**Binary******

your system

192.168.10.1

11000000 10101000 00001010 00000001

Microsoft

207.68.137.53

11001111 01000100 10001001 00110101

Subnet-mask

255.255.255.0

11111111 11111111 11111111 00000000

Tcip-ip subnet-mask ta 1 lere karşılık gelen ip adres başlıklarını (bu örnekte ilk 24 bit) karşılaştırır. Eğer sen ve bağlanmak istediğin makina aynı networkteyseniz bu ilk 24 bit aynıdır. Ve Tcp-ip ARP tablosundan diğer makinanın ethernet (mac) adresine bakarak bağlanır.
Ancak bu ilk 24 bit farklı ise, Tcp-ip Gateway'a bağlanır (bu örnekte 192.168.10.20). Artık diğer sisteme bağlanmak Gateway'in işidir. Diğer kişi kimse internet bulutu içindedir. Gateway (geçit) ve Router (yönlendirici) 'lar özel tablolar tutarlar ve kendilerine gelen isteği ileriki router'e geçirirler. O diğerine, o diğerine ... ta ki hedef bilgisayara ulaşana kadar. Hedef bilgisayar ise cevabı gene aynı yol üzerinden geri yollar
(daha fazla bilgi için bakınız: Tcp-ip routing ayarları).

Yukarıdaki örnekte herbirinin internette belirlenmiş ip leri olan bilgisayarlar var. Eğer bir dial-up bağlantı ile yerel networkünüzü internete bağlıyorsanız bir proxy'ye ihtiyacınız var !

Bunu kendi kendinize kontrol edbilirsiniz. Bir ms-dos komut istemci açın ve tracert komutunu kullanın. Ben "ourworld.compuseve.com" adresine tracert yapıyorum :
TRACERT 149.174.213.39

**HOSTS / LMHOSTS:**
Hosts ve Lmhost dosyalarının kullanımı şöyledir : Tcp-ip yüklü bir windows'ta C:\\WINDOWS dizininde bu dosyaları 'hosts.sam' ve 'lmhosts.sam' olarak bulabilirsiniz. Bu dosyaların bir kopyasını yaratın ve isimlerini 'hosts' ve 'lmhosts' haline getirin (uzantılarını yokedin). Ve isimleri tanımlama da kullanın :

Hosts ve Lmhosts dosyalarının tanımlaması aynı yapılır:
ip-adresi,biraz boşluk,bilgisayar ismi

Hosts ve Lmhosts ne zaman kullanılır ?
Bu iki dosyanın iki basit görevi vardır:

Hosts dosyası temel Tcp-ip programlarınca kullanılır (ping, ftp, ......).

Lmhosts ise Microsoft ***Networking/Client/Workgroup*** yönetiminde kullanılır.

Eğer tüm network aynı kablo üzerinde (tek segment) ise bilgisayarlar broadcast mesajları ile diğerlerini bulur ve haberleşilir. Bu durumda Lmhosts dosyasına gerek yoktur.
Ancak Broadcast mesajları yönlendirilmezler, yani eğer birden fazla segment varsa ve bir segmentteki bilgisayar diğer segmentteki bir bilgisayarla haberleşmek isterse ona broadcast mesajı ile ulaşamaz. O zaman Lmhosts dosyasına elimizle diğer segmentteki bilgisayarın ip adresini gireriz ki farklı segmentte olmalarına rağmen haberleşebilsinler.
Not: Lmhosts "***L******an ******M******anager ******HOSTS***" un kısaltmasıdır. Bu tanımlama eski Microsoft networklerinden gelir.

**DNS**** (Domain Name Service):**
Ip adreslerinin hatırlanması zor olduğu için bu servis kullanılır.
Bu servis bilgisayar isimleri ile ona karşılık gelen ip adresini tutar:

Eğer herhangibirserver.com gibi bir adres girerseniz (web browser'a mesela) Tcp-ip şunları yapar :

1.Dns servere herhangibirserver.com'un ip adresini sorar.
2.Dns server ip adresini yollar (192.5.6.111 gibi).
3.Tcp-ip herhangibirserver.com'a 192.5.6.111 ip numarasını kullanarak bağlanır.

Bu basit bir Tcp-ip kursu idi. Daha fazla bilgi için
FTP : File Transfer Protocol ' a bakın.

(Webmaster not: Bu konu ile ilgili, dökümanlar bölümünde çok doyurucu bilgiler bulabilirsiniz)

| **IPX-SPX TEMELLERİ****** |
| --- |

Ethernet network kartları habeşlemek için MAC adreslerini kullanmak zorundadırlar. MAC adresi herbir network kartına üreticisi tarafından, daha sonra değiştirilemeceyecek ve dünyada bir eşi daha olmayacak şekilde verilen hexadesimal bir numaradır. MAC adresini bir çok şekilde öğrenebilirsiniz. Mesela kartınızın ayar ve kontrol programı ile :

Eğer sisteminizde TCP-ip yüklü ise "winipcfg" programı ile de öğrenmeniz mümkün (aynı zamanda tcp-ip bilgilerini de öğrenebilirsiniz).

Hexadecimal MAC adresinin ilk 6 rakamı üretici kodunu belirtir (büyük üreticilerin birden fazla kodu olabilir). Son 6 rakam ise üretici tarafından kendi ürettiği her karta ayrı ayrı verilmiş numaradır.

Her bir ethernet kartının dünyada eşi olmayan bir MAC adresi vardır.

IPX-SPX protokolu ile ilgili bazı teknik bilgilere geçmeden isterseniz bu protokolun gelişimine bir göz atalım.
Bu protokol, NOVELL firması tarafından kendi pc tabanlı file server uygulaması "Netware" için geliştirmiş olduğu bir protokoldür. Netware server üzerine birden fazla network kartı takılabilir. Bu networkü segmentlere bölerek performansı arttırmak için sıklıkla başvurulan bir yoldur.

Server üzerinde takılı ve network kablosuna bağlı herbir network kartına bir net numarası atanır (ayrıca server'a da bir "internal net number" atanması gerekir). Bu net numaraları tüm networkte tek olmalıdır.
Artık ipx-spx protokolu sistemde kullanılan mac ve net adreslerinin bir kombinasyonu ile çalışmaya başlar. Örneğin Net=2 üzerindeki PC#1 2.0060086DD3EE (2 net numarası, 0060086DD3EE ise MAC adresi) olarak, Net=3 üzerinde PC#3 ise 3.080000060560 olarak bilinir.

Novell'in ilk geliştirdiği IPX-SPX ten bu yana bazı değişiklikler ile bu protokolun birden fazla varyasyonu ortaya çıkmıştır. Farklılıkları FRAME tiplerinden kaynaklanır.

- Ethernet 802.3
- Ethernet 802.2
- Ethernet\_II

(Dos'ta Novell driverlerini yüklerken frame tipi NET.CFG dosyasında doğru olarak belirtilmelidir.)

Win9x'ten veya NT den Novell-Netware servera bağlantı yapabilmek için yapmanız gerekenler çok basit :

Network kartını yüklediğinizde windows protokol ve client'leri yükler (dikkat w98 sadece tcp-ip'yi yükler).

Eğer sadece Netware server'a bağlanacaksanız diğer ihtiyaç duyulmayan protokol ve clientleri silin !

Eğer ipx yüklü değilse yapmanız gereken "add" butonuna basmaktır.

Şimdi ayarlara bir göz atalım (properties'e tıklayın)

Tab: Advanced
Item: Frame-Type:
Default değeri: AUTO.

Eğer bir Netware servere veya NT servere bağlanıyorsanız bu değer AUTO olmalı. Böylece kullanılan frame tipi otomatik olarak seçilecektir.

Ancak serverin bulunmadığı bir ortamda (pc-to-pc), frame tipinin alınabileceği bir yer de yok demektir. Eğer pc-to-pc networkünüzde ipx kullanmak istiyorsanız frame tipini her makinada ayrı ayrı elle belirtmelisiniz.

Bir frame tipi seçin :

Ben genellikle "Ethernet 802.3" kullanıyorum.

Ayrıca tüm sistemlerde network numarasını aynı yapmalısınız:

Pc-to-Pc bir networkte ipx kullanmak ile ilgili ayrıntılı bilgi için tıklayın !

## **Network Hızı ve Erişim Metodları******

10base2 veya 10baseT networkümüzden ne kadar hız bekleyebiliriz ?

Her iki tip networkte 10 Megabit/saniye networktür.

1 Byte=8 Bit
1 bit=1 karakterdir.

Buna göre;

10Megabit/saniye = 1.25Megabyte/saniye

olur ki bu bir disketin alabileceği bilgiden bile azdır. Ve bu hız değerine de gerçek hayattta asla ulaşamayız. Yani biz bu tip bir networkte en iyi şartlarda bile 1 saniyede bir disketlik (1.44 Mbayt) bilgi aktaramayız.

Şimdi bir testle ne olduğuna bakalım :

Sistemde iki tane bilgisayar var.

test #1:
30 Mbyte büyüklüğünde tek bir dosya 600 KByte/sn hızla kopyalanabildi.

test#2:
1900 dosya (18 MByte)
300 KByte/sn hızla kopyalanabildi.

Hızın beklenenden de düşük olmasının sebepleri :

Sebep 1: Kopyalanan data ile beraber, datanın doğru gidip gitmediğini içeren kontrol kodları da yollanıyor. Bu sebeple ikinci testte daha da düşük bir sonuç çıkıyor. Çünkü 1900 tane dosyanın kontrol bilgisi tek dosyanınkinden fazla.

Sebep 2: 10base2 ve 10baseT Ethernet **CSMA/CD**:
***C****arrier ****Sense**** ****M****ultiple ****A****ccess / ****C****ollision ****D****etection* temellidir. (Tcp-ip Network hızını registry ayarları ile arttırabilirsiniz.)

Carrier Sense: Bir terminal veri trasferine başlamadan önce kabloyu dinler. Eğer kablo başka bir veri transferi nedeniyle meşgul değilse, transfere başlar.

Multiple Access: Aynı kabloya birden fazla terminal bağlıdır.

Collision Detection: Eğer iki veya daha falzla terminal aynı anda iletime geçerse sinyal çarpışması olur. Terminaller tarafından çarpışma tespit edildiğinde ise transfer iptal edilir,rasgele bir süre beklenilir ve tekrar denenir.

Collisionlar tekrar göndermeye sebep olur. Bu sepebten dolayı 10base2 ve 10baseT networklerde teorik hızın %70-75'i kullanılabilir.

Ethernetin çalışmasını insanların konuşmasına benzetirsek :

Eğer kimse konuşmuyorsa konuşmaya başlayabilirsin.

Eğer iki kişi aynı anda konuşmaya başlarsa, ikisi de susar,rasgele bir süre bekler ve tekrar dener.

| **Networkteki Hız Problemleri Ve Çözümler****** |
| --- |

Kablolamanızı yaptınız,en pahalısından ve hızlısından bilgisayarlar aldınız,
kurdunuz. O da ne ? Networkünüz yavaş mı ????

test 1 ve 3:
1 34 Mbyte'lık tek dosya
test 2 ve 4:
18.5 Mbyte'lık 2100 dosya

Datanın akış yönüne göre farklı hız değerleri alabilirsiniz.

test 1 ve 3:
1 34 Mbyte'lık tek dosya
test 2 ve 4:
18.5 Mbyte'lık 2100 dosya

Bu örneklerde,ağdan data okumanın yazmaya göre yaklaşık %60 daha
yüksek performans verdiğini görüyoruz.

Bunun sebebi re-trasmittion (tekrar gönderim)'lerdir. Genellikle de kablo problemlerinden kaynaklanır.

Ancak Tcp-ip kullanan networklerde bunun başka bir sebebi daha olabilir:
Bazı browser'lar (neoplanet gibi) Tcp-ip parametrelerini değiştirerek, küçük
Tcp-ip paketleri kullanmak suretiyle internet hızını optimize etmeye çalışırlar.
Ancak bu değişiklikler yerel ağın performans kaybına uğramasına yol açar.
(Tcp-ip registry girdileri ile ilgili daha detaylı bilgi için: http://support.microsoft.com/support/kb/articles/q158/4/74.asp)

Ağın hızını arttırmak için Tcp-ip değerlerini eski haline getirmek gerekir.

MTU/MaxMTU:

(start->run->regedit->F3)
Şu keyi bulun : (start->run->regedit->F3)

*HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\Class\\NetTrans*

"0000", "0001", "0002", "0003" alt-keyleri network kartı veya modem için tüm Bindings'leri gösterir.
Bunlardan resimdeki gibi ip adresi ve maske tanımlanmamış olan modem'dir. MaxMTU değerinin optimum internet erişimi için "576",lan performansını
arttırmak içinse "1500" olması gerekir (1500 windows default'tur).

RWIN / DefaultRcvWindow :

Şu keyi bulun:

*HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\VxD\\MSTCP*

"DefaultRcvWindow" anahtarı optimum internet hızı için "2144",optimum Lan performansı içinse "8192" olmalıdır (windows default'tur).

Not: Bu key W95 ve W98 arasında farkılık gösterir. KB artikeli W95 için
DWORD veri tipinde,W98 de ise String-Value tipindedir.

| **Ağım Niye Yavaş Çalışıyor?****** |
| --- |

Networkünüzü yeni kurdunuz,veya varolan networkünüzü upgrade ettiniz,beklentiniz elbette çita gibi hızlı bir network !

Ama o da ne ? Aynen bir tırtıl gibi çalışıyor, neden acaba ??

(Eğer bir Tcp-ip ağınız var ise önce buna bakın!)

Hadi aşağıda sağlıklı bir networkün nasıl çalıştığına bakalım:

Şimdi de adım adım inceleyelim :

Client bir istekte bulundu (bir dizinin listelenmesi,bir dosyanın açılması,bir dosya(ya)nın okunup yazılması,yazıcı çıkışı gibi..)

Bu istek bir Network-Veripaketi haline getirildi.

Bu "paket" bir elektrik sinyali olarak,ethernet kartından çıktı,kablolardan geçerek "server" isimli makinaya gönderildi.

"Server" veripaketini aldı.

"Server" gelen isteği işledi,cevap olacak veri paketlerini hazırladı.

Cevap tekrar bir veri paketi haline getirildi.

Cevabı içeren veripaketi Cliente gönderildi.

Client veri paketini aldı,işledi ve.. evet ona gelen cevaptı bu.

Ancak eğer kablolamada bir problem var ise bakın neler oluyor :

Şimdi bunu da adım adım inceleyelim :

Client bir istekte bulundu (bir dizinin listelenmesi,bir dosyanın açılması,bir dosya(ya)nın okunup yazılması,yazıcı çıkışı gibi..)

Bu istek bir Network-Veripaketi haline getirildi.

Bu "paket" bir elektrik sinyali olarak,ethernet kartından çıktı,kablolardan geçerek "server" isimli makinaya gönderildi. Gönderildi ama kablodaki bir problem nedeniyle yerine tam ve hasarsız ulaşamadı !

"server" veripaketini aldı. Ancak paket yolda bozulduğu için "server" bunun ne olduğunu anlayamadı. Dolayısıyla da bir cevap üretmedi.

"server" ne olduğunu anlayamadığı için bir cevap üretemedi ve yollayamadı. Sonuçta (bir süre beklendikten sonra) Client gönderdiği veri paketinin yolda kaybolduğunu kabul etti. (time out)

Client isteğini yineledi.

Sonuçta bu beklemeler,tekrar-tekrar gönderimler ağ performansını düşürür.

Böyle durumlarda; NET DIAG/STATUS (Networkümün durumu ne??) yaparak network istatistiklerinizden yararlanarak problemi çözmeye çalışabilirsiniz.

Ethernet Paketleri (veripaketleri) genellikle aşagıdaki nedenlerden dolayı bozulmaya uğrarlar :

Bozuk Network Kartları

Yanlış bağlanmış terminatorler,bozuk terminatörler ve Hub portları

Kablo çok uzunsa

Bozuk T konnektörleri

Bazen yukarıdaki sebeplerden bir tanesine sahip bir terminal bile networke sürekli bozuk veripaketleri göndermek suretiyle,tüm sistemi işlemez hale getirebilir. Hub üzerindeki ışıklardan takip edildiğinde üzerinden veri transferi olmadığı halde bir terminalin ışığı sürekli yanıyorsa (veri iletimi durumunu gösteren ışık) orada bir problem var demektir.

| **Yönlendirme (ROUTING)****** |
| --- |

Küçük networklerde tüm bilgisayarlar aynı kabloya bağlıdır:

Herhangi iki sistem haberleşmek için standar windows özelliklerini kullanırlar :

System#1 çalışır ve (network clienti) System#2(network server) üzerindeki data ya erişir. Bu bağlantı iki sitem üzerindeki network kartları ve protokoller ile sağlanır.

Fakat networkler büyüme eğilimindedirler. Zamanla birden fazla network kablosu (segment) ve farklı network cihazları (modem, isdn vs.) networke dahil olmaya başlar.

Şimdi yukarıdaki şekle bakalım; #2 üzerinde iki tane ethernet kartı var.
Ve system#1, #3 ve #4 ' e #2 üzerinden erişiyor.
Şimdi #2 üzerinde farklı bir iş daha var: kendisi üzerinden geçen veriyi iletmek. Bu iletmeye ROUTING denir.

Bunu yapabilmek için windows networklerinde bazı ek hizmetlerin yüklenmesi gerekir :

Router (#2) üzerindeki protokol bu yönlendirme işini yapar. Bu noktada seçilecek protokol önem kazanır.

- NetBEUI yönlendirilemez
- IPX/SPX ve TCP/IP yönlendirilebilir.

Network üzerinde birden fazla yönlendirme olabilir :

Ve internet üzerinde kullanılan TCP-IP ile 10 dan fazla router üzerinden geçilerek hedef siteye ulaşılabilir.

| **TCP/IP YÖNLENDİRME****** |
| --- |

Aşağıdakine benzer bir network kullanacaklar için routing ayarlamalarını anlatmak istiyorum. ( TCP/IP ve Birden fazla network kartı konularını öncelikle okuyun).

Yukarıdaki sitemlerden bazıları üzerinde Windows95/98, bazılarında ise NT4 olabilir (olmalı).

**System #1:**
Bu sistem* (Windows95/98 veya NT4 olabilir)* 1 Network kartına sahip ve şöyle ayarlanmış *(resim NT4 içindir)* :

Bu bilgisayar, sadece kendiyle aynı kablo üzerindeki sistemler ile direk olarak haberleşebilir (192.168.1.x). Ve Gateway/Router olarak ayarlı 192.168.1.2 (System#2) üzerinden de diğer sistemlerle haberleşebilir.

**System#2:**
Bu bir Windows NT4 makinası ve 2 Network kartına sahip :

İlk kart System#1 ile haberleşiyor:

İkinci kart System#3 ile haberleşiyor.

İlave olarak, NT4 TCP/IP protocol "***route***" için ayarlanmış olmalı (ki System#1 bunun üzerinden diğer makinalara erişebilsin, yukarıda System#1 in gateway olarak bunu gördüğünü hatırlayın):

System#2 direk olarak System#1 ve System#3 ile haberleşebilir, ancak System#4 ile haberleşemez (Çünkü 192.168.3.x networküne erişmekle ilgili hiçbir bilgisi yok).

Şimdi biz System#2 ye System#4'e erişebilmesi için yardım etmeliyiz. Bunu System#3'ü Gateway (geçit) olarak ayarlayarak veya elimizle TCP/IP routing tablosunu değiştirerek (ms-dos komut isteminde route.exe'yi kullanarak) yapmalıyız.

ROUTE.EXE Windows ve NT ile beraber gelir ve Resource Kit içinde açıklanmıştır :

Bizim örneğimizde, system#2 üzerinde :
*
**ROUTE ADD 192.168.3.**0** 192.168.2.11*
Bu komut satırını çalıştırınca System#2'ye , tüm 192.168.3.x TCP/IP adreslerine *('**0**'** **'**192.168.3.x** adreslemesine sahip tüm makinalar'** anlamına gelir, bizim örneğimizde System#4 böyle bir makina)* 192.168.2.11 üzerinden *(System#3)* gitmesini söylemiş oluyoruz..

Yukarıda Systems#1 ile #2 arasındakine benzer bir ayarlama yapmış olduk.
Eğer Route komutu ile ilgili daha fazla bilgi almak istiyorsanız aşağıdaki linke bakın :
http://support.microsoft.com/support/kb/articles/q158/4/74.asp

Şimdi yaptığımız ayarlamaların işe yarayıp yaramadığını PING ile kontrol edelim (System#1):

System#1, System#2 ve #3 ile haberleşebildi.

System#3, System #2 ile haberleşebildi, ama System#1 ile haberleşemedi. Çünkü System#3 üzerinde System#1'in bulunduğu 192.168.0.1.x networkü ile ilgili bir tanım yapmadık, tersini yapmış olsak (System#1 den #3 'e yani) ta network mantığı gereği çalışmayacaktır. Çünkü #1 #3'e erişebiliyorsa da, #3 #1 e erişememektedir.

Tüm sistemlerin ip adreslerini, Gateway'larini ve IP FORWARDING'lerinin enable olmasını kontrol edin.

***Unutmayın: Network Sadece İki yönlü haberleşme olabildiğinde çalışır. PING-test-sinyalleri geriye cevap gelmediğinde düzgün çalışamaz (echo-back) !******
******
***Router Üzerinden Erişilen Bir Sisteme Göz Atmak***

***Workgroup'ların bazı kısıtlamaları vardır:
Farklı kablolar üzerindeki sistemler aynı workgroup'ta olamazlar. Router üzerinden bir sisteme erişmek için "Find Computer" i kullanın :

Bu hata mesajından kurtulma için tabii ki:

"LMHOSTS" dosyasını oluşturmalı veya düzenlemelisiniz :

***
***
Windows 95'te, örnek bir dosya olan *"LMHOSTS.SAM*", TCP/IP ile beraber windows dizinine yüklenir.
Bu dosyayının ismini değiştirerek veya kopyalayarak "LMHOSTS" isminde bir dosya oluşturun. Ve bu dosyayı notepad ile açarak computername ve ip adresini girin:

| ***Şimdi büyük soru geliyor : Windows 95'i Router olarak kullanabilir miyim ?****** ***Resmi olarak: Hayır. Microsoft bu özelliği sadece NT'ye koymuştur. Gayrıresmi olarak: Evet,* ama bazı sınırlamalarla.* Bunu henüz test etmedim ama, newsgroup'lardaki bir çok mesaj da işe yaradığını okudum. *** ******"******Windows 95'i router yapmak istiyorum!****** "****** ***( http://gargoyle.apana.org.au/~nat ) Windows95 bir TCP/IP Router olarak, ***TEK*** Ethernet-Kablo ve bir Dialup Networking bağlantısı ile, ve ***STATIC*** IP-address ile kullanılabilir: Dialup-Networking Upgrade 1.2 (TCP/IP upgrade içinde) yüklemiş olmanız, ve bu Windows95 Registry değerini değiştirmeniz gerekiyor: key:\[HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\VxD\\MSTCP\]*** ***new value (as StringValue): "1"" |
| --- |

---
*Kaynak: `NETWORK TEMELLERİ/NETWORK TEMELLERİ.doc` — ildomuh1 — 2004*
