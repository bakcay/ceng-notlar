# Veri Tabani Üzerine

**ÖNSÖZ**

*Gerçeklikle karşılaştırıldığında, bilimde vardığımız düzey ilkeldir, çocuk oyucağıdır. Ama sahip olduğumuz en değerli şey de odur.*

## * ALBERT EINSTEIN ( 1879-1955)*

Daha önce matbaanın, radyonun ve televizyonun gündelik yaşamda yarattıkları devrimlerin bir benzerini bugün internet gerçekleştiriyor. İnternet henüz emekleme aşamasında, ama daha şimdiden dünyayı değiştiriyor. Bugün, ABD deki 1000 den fazla kasabanın ve kentin homepage i , internet de bir sitesi var. 200’den fazlasının şimdiden, birbirine bağlanmış bilgisayarlar kullanarak hayata geçirmeyi planladıkları yerel siyasi enformasyon yurttaş ağı ( civic networking) projeleri var. Sadece Hollanda da, altmış kasaba bilgisayar aracılığıyla iletişimi benimsemiş durumda ve bir çeşit yurttaş ağına sahip.

Database firmalari her geçen gün daha fazla veri depolamak, verileri hiçbir durumda kaybetmemek, verilere kolayca ve daha hızlı ulaşabilmek adina birbirleriyle yarışıyorler. Peki ama neden verilerle uğraşıyoruz ? Çünkü verileri topladiğimizda bir sonuca ulaşmak ve raporlar elde etmek çıkan sonucu görerek geleceği tahmin etmek istiyoruz. Verileri değerlendirme aşamasinda ise işin içine istatistiksel yöntemlerin girmesi kaçınılmaz oluyor.

Database firmalarının bugün hemen hepsinin hedefi ınternet uzerinde databaselerini kullanmak ve degerlendirmek. Database i internet üzerinden çalıştırımayan, uygulamalarını internet’e taşıyamayan firmalar , ürünlerini pazarlayamıyacaklarını biliyorlar.Bu nedenle hem internet hem de database kavramları gelecekte son derece önemli olacaktır.

Okul sırasında ekonomik nedenlerden dolayı piyasadaki bilgisayar firmalarinda çalışmak zorunda kaldık. Bu hem ekonomik anlamda bir rahatlama getirdi hem de okulda ogrendiklerimizi piyasada kullanma olanagı verdi. Çoğu öğrenci okuldaki bilgilerinin iş hayatinda hiç yararli olmadığı düşüncesindedir. Biz bu düşüncede değiliz. İstatistik bolumunde değerli hocamiz Prof.Dr Aziz Bener in bizlere bilgisayar programlama dersinde, iki donem boyunca gosterdiği C programlama dili sayesinde , programlama ve database ile ilgili temel kavramları çok daha hızlı ve çabuk kavradığımızı söyleyebiliriz. Piyasadaki nesneye yönelik programlama araçları ve dördüncü kuşak dilleri kolayca öğrenebiliyorduk çünkü hepsinin mantiği ayni idi ve C programlama dilini bilen bir öğrenci için diğer dillerde uygulama geliştirmek su içmek gibi bir şeydi.

Internet ve database uzerine bir bitirme odevi hazırlamak oldukça zordu ve bu odevin hazırlanması ile bildiklerimizin uzerine yeni bilgiler katmış olduk. Oyle bir odev hazırlamalıydık ki bizden sonra bölüme girecek öğrenciler bu ödevi okuyarak internet üzerinde bir veritabanı uygulaması geliştirebilmeliydi.Umarız bu konuda başarılı olabilmişizdir.Bu ödevin hazırlanması sırasında yardımlarını bizlerden esirgemeyen Progress ve Oracle firması yetkililerine ve değerli hocamiz Sayin Prof.Dr Aziz Bener e sonsuz teşekkürler.

Reşat Bayraktar.

Baran Ertaş.

**Veritabanı**

**Veritabanı ve Akılcı Düşünce Üzerine**

Veritabanı bir yazılımdır. Veritabanı bilginin hammaddesinin depolandığı yerdir. Bilgiyi oluşturan bileşenleri sınıflara ayırarak ama aralarındaki ilişkileri de dikkate alarak depolar, istendiği zaman birleştirerek sunar. Bilgi teknolojileri ile ilgili hemen her konunun bileşenlerden birini veritabanı oluşturmaktadır.Kişisel fax yazılımlarından, en gelişmiş fax sunucu sistemlerine kurumsal kaynak planlamasına (Enterprise Resources Planing-ERP) yazılımlarından, döküman arşiv sistemlerine, CAD/CAM uygulamalarından, OT/VT sistemlerine ve nihayet veri ambarı uygulamalarına kadar her sistemin içerisinde mutlaka bir veri tabanı bulunmaktadır. Hatta işletim sistemleri bile sistem bilgilerini özel yapıları olan veritabanlarında tutmaktadır.

Geçmişten günümüze yaklaşımlar ve yapısal özellikler değişime uğramış olsa bile, onlardan beklenen hizmet hep aynı kalmıştır ki o da “Hemen şimdi bilgi” olarak ifade edilebilir. Veritabanı dendiğinde yalnızca verilerin depolandığı bir kavram algılamak çok doğru bir yaklaşım olmayacaktır.

O verinin bilgiye dönüştürülerek diğer verilerle işlendiği koca bir fabrika gibidir. Bugün teknoloji üretenlerin pek anlamlı olmayan düşünce biçimlerinin bir sonucu olarak bazı benzer kavramlar istemeden de ayrı ayrı ele alınıyor olsa bile, (daha fazla ürün satmak adina uygulanan pazarlama stratejilerinin bir sonucu bu belki de !) gelecekte bugünün veri ambarı olarak adlandırılan yaklaşımları da aslına dönerek, veritabanı kavramı içerisindeki olması gereken yere oturacaktır.

Veritabanı kavramını tek başına ele almak kurumsal bilgi teknolojileri profesyonelleri için pek anlamlı olmayacaktır. Çünkü veritabanı mimarileri, algoritmaları, bellek ve kaynak kullanımı gibi konular kimi zaman oldukça ağdalı bir dilin kullanılmasını gerektirecektir. Bu dili anlayacak mühendislik eğitimi almış teknik elemanlar, çoğunlukla bu bilgiler sahiptirler (sahip olmaları gerekir) ve profesyonel yöneticiler, yanlarında çalıştırdıkları bu çalışanlardan dilerlerse bu bilgileri alabilirler. Yanlarında personel çalıştırmayan ve bu tip hizmetleri dış kaynaklı firmalardan alan kurumlar içinde bu hizmeti sağlayan danışmanlık şirketleri mevcuttur. Veritabanı kullanarak kurumlar hangi katma değeri sağlayabileceklerini çok iyi bilmelidirler. Eğer bir profesyonel kurum kullanacağı veritabanı ile teknik ayrıntıları detaylı olarak öğrenmek isterse, bu onun tercihidir. Ancak bu bir zorunluluk değildir.

Devlet kurumlarında ya da yerel yönetimlerin yazılım ve donanım ihalelerine katılan ve bilirkişi olduğunu söyleyen kişiler kendi aralarında veritabanı sistemlerinin üzerine tartışırken içlerinden biri “Benim veritabanım 10 yıllık bilgiyi saklar” derken diğeri “Ama benim veritabanım renkli ekranda çalışıyor” demişti. Dünyaca kabul görmüş veritabanı sistemleri arasında yaptıkları tartışmada sonucun ne olduğunu tahmin etmek zordu, çünkü hangi kriterlere göre karar verildiğini anlamak veritabanı kavramını anlamaktan daha da zordu.

Teknolojiyi takip edenler, eski dergileri karıştırdıklarında daha birkaç yıl öncesine kadar yere göğe sığmayan teknolojilerin bugün anlamını yitirdiğini kavramakta güçlük çekmeyeceklerdir. Birkaç yıl öncesine kadar sözü edilen Client/Server (İstemci/ Sunucu) mimarisi bugün gözden düşmüş durumda. Teknoloji firmalarının profesyonel kurumlara şöyle bir dayatması oluyor.Eğer yeni çıkan teknolojiyi satın almazsan dünyanın gerisinde kalırsın ve bunu satın alan diğer rakip kuruluşlar senin 5 yıl önünden gidecektir. Bu dayatma veya tehdit diyelim bir pazarlama ya da satış staretejisi olarak görülebilir ama bazı durumlarda doğru da olabilir. Bu yüzden kavram kargaşaları yerine yeni teknolojilerin kurumsal katma değerini firmaya uygulanabilirliğini ayırt etmek en doğru yaklaşım olacaktır.

Bugün kullanılan veri tabanları ve geliştirme araçları bazı çekirdek algoritmalarda farklılık gösterse bile, birbirlerine yakın ölçüm değerleri veriyorlar. Bir veritabanı bir test işleminde belli bir kritere göre en yüksek değeri verirken diğeri aynı test işleminde farklı kriterler kullanarak kendisinin en yüksek değeri verdiğini söylemekte. Önemli olan teknik personelin bu bilgileri yorumlayabilme becerisine sahip olmasıdır.Çalıştığı kurum hangi tür işlemleri daha fazla kullanıyor ? Bugün yoğun olarak kullanılan sistem gelecekte neler ihtiyaç duyacak ?

Son zamanlarda büyük mağaza ve alışveriş merkezlerinde local ya da internet müşteri bilgi formları dolduruluyor. Bazı müşterilere o mağazaların manyetik kartları veriliyor.Manyetik kartla mağazadan alışveriş yapan ya da internet üzerinden alışveriş yapan müşteri bilgisini ele geçirdikten sonra o müşterinin hangi saatte, hangi ürünü aldığını , promosyon satışlarından yararlanıp yararlanmadığı gibi bilgiler veri tabanına aktarılıyor. Aslında başlangıçta bir sayfalık form ve döküman arşiv sistemi ile başlayan bilgiler, bir anda veritabanı ve nihayet veri ambarı sistemine dönüşüyor. Eğer bu dönüşüm planlı değilse veritabanı ve sistem değişikliğinin yarattığı lisans ücreti, yazılım ve donanım maliyeti başlangıçta düşünülmeyen pahalı yatırımların yapılmasına neden olur.

Kurumsal firmaların kullandıkları veri tabanları bazen gömülü bazen de açık olmaktadır. Kuruluşun ihtiyaçlarına göre veritabanı üzerinde yeni yazılımlar geliştirmek mümkündür. Çok gelişmiş bir uygulama geliştirme aracınız olabilir ama veritabanı sisteminiz iyi değildir ya da veritabanı sisteminiz çok iyi olmasına rağmen uygulama geliştirme aracınız istediklerinizi karşılamayabilir.

1986 yılında ANSI ( American National Standart Institute) tarafından kabul edilen SQL(Structure Query Language -Yapısal Sorgulam Dili) ile tüm veri tabanları tek bir dil ile ortak sorgulanabilmesi ve belli standart sağlanması hedeflendi. İlerleyen yıllarda veritabanlari giderek daha fazla bilgiyi depolamaya başladı.Başlangıçta düşünülen veri yapılarından çok daha fazlası ile çalışıyordu ve herşey veri olarak saklanabiliyordu. Ses, resim, harita, video ,hesap tabloları gibi pek çok veri vardı ve bu verilerle uğraşmak için her veritabanının kendi özel yazılım geliştirme araçları ortaya çıktı. Bu araçlar ortaya çıkarken her ne kadar yalnızca kendi veritabanları ile değil, tüm sistemlerle uyumlu olduklarını savunsalarda, bazı istisnalar dışında her veritabanı en iyi sonucu kendi uygulama geliştirme aracında veriyordu. Sonuç olarak SQL tüm veri tabanları için ortak bir dil olmasına rağmen günümüzde yalnızca belli başlı basit sorgulamalar için kullanılmakta. Karmaşık uygulamalarda, veritabanı şirketleri kendi yazılım geliştirme araçlarını ve kendi programlama dillerini kullanmaktadır.

Veritabanlarını genel anlamda üç değişik grupta toplanabilir.Birincisi kişisel diyebileceğimiz veritabanı sitemleri. MS-Office Proffessional paketi içerisinde bulunan Access bunun dışında dBase, FoxPro, Paradox ve çok küçük de olsa Excel. Bu veritabanı sistemleri diğerleri ile karşılaştırıldığına dezavantajları olduğu tartışma götürmez. Ancak hataları nedeniyle değil kapasitelerinin yetersizliği nedeniyle böyle. Örneğin xbase tabanlı bu sistemlerde “dbspace” adı verilen özel bir disk bölümü yoktur ve veritabanı dosyaları geleneksel dosya yapılarıyla aynı güvenlik yapısına sahiptir. İkinci grup İlişkisel veritabanları (Relational Database) adiyla bilinen uygulamalar ve bu uygulamalar bugün ve gelecek stratejilei karşılamaktadır.İlişkisel veritabanları bilgiyi saklama, işleme, yedekleme, raporlama ve geri getirme konularında çözümler getirmektedir. Kurumsal firmaların tercihi bu sistemlerdir.Bugün bilinen popüler ilişkisel veritabanları arasında Oracle, DB2, Sysbase, Informix, Progress, Ms SQL Server bulunmakta.Veritabanı ile ilgili üçüncü ve son grup kurumların çok büyük ve boyutlu veri tabanı analizlerine dayalı gereksinimlerini karşılamak amacıyla kurduğu Veriambarı (Datawarehouse) türü teknolojilerdir. Karmaşık veriler ve bu veriler arasındaki analize dayalı teknolojiye OLAP ( On line Analytical Processing) işlemleri veriambarında kullanılmaktadır.İlişkisel veri tabanı kuruluşlarının neredeyse tamamının veri ambarı çözümü bulunmaktadır. Geleneksel anlamdaki veri ambarı projeleri yalnızca veritabanı sistemlerinin değil, donanım ve işletim sistemini de içine almaktadır. Ancak günümüze gelindiğinde tüm eğilimler, veri ambarı kavramının ortam bağımsız bir şekilde günden güne Internet e dayalı teknolojilere üzerinde çalıştığını gösteriyor.

Internet üzerinden veriye ulaşabilen, bu verileri saklayabilen , gerektiğinde istediği raporları bu veriler üzerinden alabilen kuruluşlar güçlü veri tabanı sistemlerine sahip olduklarında kurumsal yapılanmaları ve gelişmeleri çok daha hızlı olacaktır. Günümüzde güç bilgi ile , bilgi de veri ile sağlanmaktadır.Bilgi kimin elindeyse gücün de sahibinin o olması kaçınılmaz görünüyor.

**VERİTABANI HAKKINDA GENEL BİLGİLER**

Bilgisayar programları, seçilen bir bilgisayar dilinde, bir konu ile ilgili verilerin girildiği ve değerlendirildiği komutlar topluluğudur. Programlamayı öğrenirken bir programcının ilgilenmesi gerekli olan konuları aşağıdaki gibi sıralayabiliriz.

Girilecek verilerin yapılarını tanımlayabilmek(Veritabanı)

Kullanıcı ile irtibatı sağlayan ekranların görüntüsünü (Ekran Dizaynı) ve çıktıların şeklini (Rapor Dizaynı) tasarlayabilmek

Bu iki şık arasındaki bağlantıları gerektiren program parçalarını yazabilmek

Yeni windows tabanli nesneye yönelik programa dilleri ile yukarıda belirtilen 3 şıkkı gerçekleştirmek çok basittir.

**Veritabanı** tasarımı ve tanımı için, **Data Dictionary** hizmet programı kulllanılır.

**Ekran dizaynları** ve **bağlantılar,** SMARTOBJECTS (Programlanabilir Akilli Nesneler) tanımlama ve onları programlama işlemini gerçekleştiren **APPBUILDER **(Uygulama Geliştiricisi) hizmet programı ile sağlanır **Çıktılar** için ise **REPORT** **BUILDER** (Çıktı Formları Düzenleyicisi) kullanılır..

Yukarida belirtilen Data Dictionary, Smart Objects , AppBuilder, ReportBuilder programlari her database de aynı isimde olmayabilir.Veritabaninin ozelliklerine gore farkli isimler alabilirler , işleyişleri ve database e ulaşma mantıkları aynıdır.

Netice olarak biz; **veritabanı**, **basit nesne** ve **SMARTOBJECTS** kavramlarını iyi öğrenirsek buna da nesneye dayali proglama dillerin** **komutlarını eklersek, veritabani uzerinde programlamayı öğrenmiş oluruz.

**Veritabanı**

Bugün kullanılmamakla beraber, kartoteks sistemini hatırlamayan yoktur. Örneğin müşterilerimizle ilgili bilgileri, aşağıda gösterildiği gibi, kartonlar üzerine kaydederdik. Sonra da bu kartonları çekmecelerde saklardık. Siparişler ve stoklar için aynı yöntem kullanılırdı. Bunu yaşayanlar, karşılaştıkları problemleri çok iyi hatırlarlar (Müşteri bulmak, değişiklikleri yansıtmak,müşteri-stok-sipariş bağlantısını kurmak ve bunu güncelleştirmek vs.)

| Müşteri Adı | Borcu | Telefonu |
| --- | --- | --- |
| Ali Uyanık | 50000000 | 345 34 34 |

Bilgisayarda da veritabanı zihniyetini kullanan diller bu yöntemi, tabiyatıyla problemleri ortadan kaldırarak, devam ettirmişlerdir. Fakat bilgisayarın gözü olmadığı için bir kartoteksi görerek değil, ismi ile tanıyabilir, müşteri adı için ayrılan yerin adını ve niteliğini önceden bilmesi gerekir, müşteri-stok-sipariş bağlantılarını kurabilmesi için bu bağlantıları ona önceden tanımlamak gerekir vs.. Kısaca; programcının veritabanı dediğimiz müşteri-sipariş-stok bilgilerinin nereye ve nasıl depolanacağını yani “kalıbını” tanımlayarak bu veriler arasındaki bağlantıları da bilgisayara bildirmesi gerekir. Bu tanımların nasıl yapıldığını az sonra göreceğiz.

**Veritabanının bilgisardaki avantajları**

Veritabanının bilgisayarda sağladığı avantajları sıralayalım.

Ortaklaşa kullanım :** **Çekmecelerdeki bir kartotekse, aynı anda iki kişinin yerlerinden kalkmadan bakabilmesi adeta olanaksızdır. Ayrıca, yoğun çalışan kişilerden bazıları iş yerlerindeki dosyaları yüklenerek evlerine taşırlar. Bilgisayar ortamında, birden fazla kişi farklı terminallerden aynı veriye erişebildiği gibi, evde çalışması gereken kişinin de dosyaları eve taşımasına gerek yoktur.

Yerden tasarruf:** **Kağıt, dosya, klasör gibi çok yer tutan veri depolama ortamlarını büyük ölçüde ortadan kaldırarak yerden tasarruf edilir.

Kolay güncelleştirmek: Örneğin gerçekleşen bir siparişin bilgilerini anında ve otomatik olarak stok ve müşteriye yansıtmak mümkündür.

Kolay erişim: Bir veriyi bulmak, sıralamak, istenen bilgileri ve toplamlarını yazıcıdan almak kartoteks örneği ile kıyaslanmayacak kadar kolaydır.

Emniyet: Girilen verilerin geçerliliğini kontrol etmek, bazı kişilere erişimde kısıtlamalar koymak mümkündür.

Analiz imkanı:** **Özellikle üretimde çok büyük bir avantajdır. Fakat maalesef genelde, bilgisayardan sadece “takip” ten (ne gitti, ne geldi) yararlanılmaktadır.

**Relational Database ya da İlişkili(Bağlantılı) veritabanı**

Müşterimizin yaptığı bir ödeme, doğal olarak müşteriyi etkiler. Kartoteks devrinde, bu ödemeyi müşterinin borcundan elle düşüyorduk. Bilgisayarda ise bunun otomatik olarak yapılması gerekir. Bunun için, müşteri bilgilerinin müşteri hareket bilgileri ile bağlantılı olarak tanımlanması gerekir. Diğer bir deyimle, veritabanımızı iyi tanımlarsak, programlamayı çok basit bir şekilde halledebiliriz.

Örneğin, tasarımı tamamlanmış bir veritabanında, aşağıdaki kısa program:

Tüm müşterileri listeler(Müşteri numarası, Unvanı)

Kullanıcının gireceği birkaç harfle başlayan müşteriyi bulur, gösterir

Bu müşteri ile ilgili tüm sipariş bilgisini gösterir(Sipariş ana bilgileri:Sipariş numarası, sipariş tarihi, gerçekleşen tarih vs.)

Bu siparişle ilgili tüm detay bilgilerini gösterir (Sipariş detay bilgileri.:Stok numarası, fiyatı, indirim oranı, miktarı, tutarı vs.)

**İlişkili(bağlantılı) veritabanını tasarlamak**

Bir veritabanında: müşteri, sipariş, stok vs. ile ilgili tüm bilgilerin bulunduğunu söyledik. Bu kadar çok veriyi içeren bir bütünün içerisinden istenen verileri bulabilmek ve bu verilerin birbirleri ile bağlantılarını kurmak için veritabanını oluştururken, bazı ek tanımların yapılması gerektiği açıktır.

Örneğin; sadece muşteri bilgilerine ulaşabilmemiz gerekir, müşterilerden sadece istenen bir müşteriye hızlı bir şekilde erişebilmemiz gerekir, bu müşterinin siparişlerine erişebilmemiz için bir müşteriye göre müşteri-sipariş bilgilerini ilişkilendirmemiz gerekir.

Bu sebeplerden dolayı, ilişkili bir veritabanı aşağıdaki tanımlardan oluşur:

Veri Tablosu (Table)

Sütun (Column) veya alan (Field)

Satır (Row) veya kayıt (Record)

Anahtar (Key)

İndeksler(Indexes)

| Mus-adi | Borcu | Telefonu |  |
| --- | --- | --- | --- |
| Ali Uyanık | 50000000 | 345 34 34 | 1.Satır, Kayıt (Row,Record) |
|  |  |  | 2.Satır |
|  |  |  | 3.Satır |
|  |  |  | 4.Satır |
| 1.Sütun,Alan (Column,Field) | 2.sütun | 3.Sütun |  |

**Veri Tablosu**

Yukarıda gördüğümüz gibi çok basit düzeyde bir müşteri veri tablosu tasarlanmıştır. Bunun gibi sipariş, stok ve uygulamada gerekli olan diğer tablolar aynı çatı altında tasarlanarak bu uygulamanın veritabanını oluşturabiliriz.

**Anahtar (Key)**

Ana anahtar (Primary Key) , iç anahtar

Bağlantı anahtarı (Foreign Key), dış anahtar

Ana anahtar, bir veri tablosunda bir kaydı tamamen, ve sadece o kaydı, temsil edebilecek sütun veya sütunlardır. Belirlenen bir kaydı ve sadece onu temsil edebilmesi için tek olmalıdır. Örneğin, isme göre bir müşteriye erişmeyi düşünürsek, aynı isimli birden fazla müşteri olabileceği için, erişimde ve bağlantılarda karışıklıklar doğabilir(İstemediğimiz bir “AHMET”in telefonu veya siparişleri ile kaşı karşıya kalabiliriz).Bundan dolayı müşteri kayıtlarını temsil etmek için her bir müşteriye ayrı bir numara vermek uygundur.

Ana anahtarın özelliklerini aşağıdaki gibi sıralayabiliriz.

Tek olma özelliği: İki ayrı müşteri, boş bilgi dahil, aynı bilgiyi içeriyorsa, verdiğimiz anahtarın hangi müşteriyi temsil ettiğini bilemeyiz.

Değişmemesi gerekir: Bir müşteriye bir numara verdikten sonra o numarayı değiştirirsek, müşteriyi temsil eden iki ayrı numara elde ederiz.

Kısa olmalıdır: Çok yer almamalı, ayrıca ne kadar kısa olursa ona erişim daha hızlı olur.

Bu bilgilerin ışığı altında yukarıda tanımlanan musteri veri tablosu aşağıdaki şekli alır.

| MUSNO | MUS-ADI | BORCU | TELEFONU |
| --- | --- | --- | --- |
| 1 | Ali Uyanık | 50000000 | 345 34 34 |

Aynı şekilde stok veri tablosunda, stok numarası ana anahtar olarak tasarlanabilir.

Bağlantı anahtarı(dış anahtar), adından da anlaşılacağı gibi, veritabanındaki diğer veri tablolarıyla irtibat kurmaya yarayan bir anahtardır. Tabloları birleştirmek için de kullanılır.Bu anahtar, irtibat kurulan veri tablolarının bir tanesinin de ana anahtarıdır.

Anahtar kavramının önemini daha iyi anlamak amacıyla; Stok, Sip-Detay, Siparis ve Musteri veri tablolarının tanımlandığını varsayalım ve bu tablolar arasında bazı ilişkiler kuralım. İlişki kurarken, amaç çok önemlidir. Amaç, verilen bir maldan hangi müşteriye satış yapıldığını bulmak olsun. Bunun için, Stok musteri ilişkisini ve dolayısıyla ara ilişkiler de dahil olmak üzere, Stok  Sip-Detay  Siparis  Musteri ilişkisini gerektiği gibi kurmamız lazımdır.

*Önemli Not:* İlişkiler sadece anahtarlarla kurulmayabilir. Başka metodlar da vardır.

| Tablo Adı | Ana anahtar | Bağlantı Tablosu | Bağlantı anahtarı |
| --- | --- | --- | --- |
| Musteri | MusNo | Siparis | MusNo(Siparis’te) |
| Siparis | SipNo | Sip-Detay | SipNo(Sip-detay’da) |
| Sip-Detay | SatNo | Stok | StokNo(Sip-Detay’da) |
| Stok | StokNo |  |  |

Ana anahtarlar, bulundukları veri tablosu haricinde, bu tablo ile ilişkili tabloda da dış anahtar(bağlantı anahtarı) olarak tanımlanmalıdır.

Burada görüldüğü gibi, müşteri (Musteri) tablosunda **MusNo **ana anahtar olmasına karşın, bağlantı kurmak istediğimiz sipariş (Siparis ) tablosunda bağlantı anahtarı olarak tekrar tanımlanmıştır. Aynı şekilde; **SipNo **hem sipariş(ana anahtar) hem de Sipariş detay(dış anahtar), **StokNo** da hem Sipariş detay (dış anahtar) hem de Stok tablolarında (ana anahtar) olarak tekrar tanımlanmışlardır.

Basit bir örnek, bunu daha iyi açıklayacaktır. Kayak botu alan tüm müşterilerimizi görelim..

Bunun için:

**Stok tablosundan** kayak botunun stok numarasını buluruz(**I1**).

Stok ile sipariş detay tabloları ilişkili olduğu için, I1 ile ilgili sipariş numaraları (SipNo) **sipariş detay tablosundan** bulunur. (**01 ve 04**)

Sipariş detay ile sipariş, SipNo ile ilişkili olduğundan, hangi müşterilerin bu stokları aldığını bulmak için (müşteri numaraları önemli) **sipariş** **tablosundan ** 01 ve 04’e denk gelen müşteri numaralarını buluruz (**C1 ve C3**).

**Müşteri tablosundan** C1 ve C3’ün karşılığındaki müşteri isimlerini buluruz (**Kemal Öz ve Oya Şafak**).

Netice olarak tabloları ilişkilendirmek için, ilişki kurulan tablolarda ortak bir alan (sütun) tanımlanacak ve bu sütun; bir tabloda ana anahtar olarak, diğerinde ise dış anahtar olarak tanımlanacaktır. Başka bir deyimle, ana anahtar olarak tanımlanan sütun (alan) diğer tabloda da tanımlanacak ve bu sütun, bu tabloda dış anahtar görevini üstlenecektir.

**Indeks (index)**

Bir kitabın sonundaki indeksi hepimiz biliriz. Aranan kelimeyi belirledikten sonra, indeksten bakarak hangi sayfada olduğunu bularak, o kelime ile ilgili tüm bilgileri kitaptan alabiliriz. Bir veritabanındaki indeks de buna benzer. Örneğin müşteri arama ve sıralamalarında, müşteri adını içeren sütunu indeks olarak tanımlarsak, arama çok çabuk gerçekleşir.

Bir sütuna göre indeks oluşturabileceğimiz gibi, birden fazla sütunu birleştirerek **birleşik** **indeks** adını verdiğimiz indeksler de oluşturabiliriz. Ana anahtarı içeren sütünla indeks oluşturmak, çok doğaldır(Yukarıdaki örnekte, MUSNO sütunu indeks oluşturmak için iyi bir örnek teşkil edebilir).

Her tabloda bir indeks olmalıdır. Birinci indeks her zaman tablonun ana indeksi olarak otomatik olarak tanımlanır. Örneğin, sipariş veri tablosunda SipNo ana indeks , Sip-Tarih ise tarihe göre bir indeks şeklinde tanımlanabilir.

İndeks oluşturmanın faydalarını aşağıdaki şekilde sıralayabiliriz.

Hızlı kayıt arama: Veri tablosu sıralı ise istenen bilgiye erişim daha hızlı olur.Örneğin sayfası belli olmayan bir kitapta bir bilgiyi aramak zordur.Fakat, sayfası ve aranan bilginin hangi sayfada olduğu belli olan bir kitapta arama doğal olarak kolaydır.

Kayıtların sıralanması: Tüm kayıtlar seçilen indekse göre otomatik olarak sıralanır. Örneğin, bir müşteri veri tablosunu alfabetik sırada listelemek için, müşteri ismini içeren alanın indeks olarak seçilmesi yeterlidir.

İlişkili erişim: Veritabanı içerisindeki veri tabloları birbirleri ile ilişkili oldukları takdirde, bir veri tablosundan itibaren diğer veri tablolarındaki ilgili kayıtlara erişim kolay ve hızlıdır.

Çoklu sütun: Birleştirilmiş bir indeks kullanılırsa, gruplandırma kolaylaşır. Örneğin Türkiye’deki tüm bilgisayar firmalarını içeren bir veritabanında İSTANBUL’un tüm semtlerindeki firmaların listesini alfabetik sırada almak için, indeksi, şehir + semt’e göre yapmamız yeterlidir. (Şehirler ve onun içerisinde semtler otomatik olarak alfabetik sıraya sokulurlar).

Tabloları birleştirmek: İki farklı tablodan bir çıktı alınacaksa, ortak sütunu indeks olarak tanımlamak faydalıdır.

Tabloları ilişkilendirmek: Bir tablodaki bir sütun değeri ile diğer bir tablodaki bir kayda (satıra) erişilebiliyorsa, bu iki tablo ilişkilidir. İkinci tablodaki aramnın hızlı olması için, aranan değere göre indeksli olması arzulanan bir durumdur.

*NOT:* İki tablo arasındaki ilişkiyi kuran sütunların aynı ismi taşıması gerekmez.

İndeks oluşturmanın bazı zararları da vardır.

Her bir indeks için, diskte bir yer ayırımı yapılır. İndeksin değeri ve bu değeri içeren kayıt numarası ROWID, ağaç yapısını andıran biçimde diskte depolanır. İndeks bölümünden, aranan indekse denk gelen kayıt numarası bulunduktan sonra, bu kayıt numarasını içeren kayıt ana dosyadan bulunur.

Yeni bir kayıt eklendiği veya bir kayıt silindiği zaman, ilişkisel veritabanı indeks bölümünü otomatik olarak yeniden düzenlediği için bir zaman kaybına neden olur.

Ne zaman indeks kullanmalıyız ? sorusu aklımıza gelebilir.

Sıkça silme veya ilave yapılan küçük tablolarda indeks kullanmamalıyız; sıralama yapmalıyız.

Veri aramada, aranan veri oranı tüm verilere oranla büyükse, indeks kullanma yerine sıradan arama yaptırmalıyız(Örneğin, arama neticesinde 20 000 kayıttan 19 000 kayıt bulunacaksa sıradan arama, 20 000 kayıttan 100-200 kayıt bulunacaksa indeks kullanımı tercih edilmelidir).

*NOT:* Tüm ilşkisel veritabanı sistemleri işletim sistemine göre 1024, 2048, 4096, 8192 byte’lık bloklara ayrılmıştır. Veri erişiminde, sadece bulunan kayıdı içeren blok diğer kullanıcılara kapalıdır(Genelde, diğer dillerde erişim şekline bağlı olarak tüm indeks dosyası kilitlenerek, o anda diğer kullanıcılara kapalıdır).

Hatalı tasarım örnekleri:

| MusNo | İsim | Sehir | SipNo |
| --- | --- | --- | --- |
| 101 | Kemal Öz | İSTANBUL | M31, M98, M129 |
| 102 | Ali Kara | İSTANBUL. | M56 |
| 103 | Oya Şafak | ANKARA. | M37, M40 |
| 104 | Filiz Sarı | BURSA. | M41 |

**Doğrusu:** Müşteri ana tablosu ve bu müşteri ile ilgili sipariş hareketlerini ayrı ayrı tablolar şeklinde düzenlemektir.

Müşteri tablosu

| MusNo | İsim | Sehir |
| --- | --- | --- |
| 101 | Kemal Öz | İSTANBUL |
| 102 | Ali Kara | İSTANBUL. |
| 103 | Oya Şafak | ANKARA. |
| 104 | Filiz Sarı | BURSA. |

Sipariş tablosu

| SipNo(Ana anahtar) | MusNo (Dış, bağlantı anahtarı) |
| --- | --- |
| M31 | 101 |
| M98 | 101 |
| M129 | 101 |
| M56 | 102 |
| M37 | 103 |
| M140 | 103 |
| M41 | 104 |

*Not:* Aynı mantıkla, tüm bilgileri bir dosyada toplamak yerine, güncel değişmeyen bilgileri içeren bir ana bilgi dosyası ve güncel değişen hareket dosyası oluşturmak ve ikisini bağlayan bir anahtar kullanmak en doğal tasarım şeklidir.

**Veri tasarımı için pratikte izlenen yol**

Kağıt üzerinde veya akıldan:

Uygulamada gerekli olan veriler ortaya dökülür

Bu verilerin veri tablosu şeklinde, paylaşımları tasarlanır (Tablo adedi ortaya dökülür)

Veri tabloları arasındaki bağlantılar tasarlanır

Veri tablolarının kalıbı tasarlanır

Her bir tablo için ana anahtar ve gerekiyorsa, her bir alan için geçerlilik kuralları tasarlanır

Bu aşamadan sonra, veri yapısının daha ayrıntılı tasarımına geçilir.

Ortak kullanılan veriler hangileridir?

İndeks, hangi sütuna göre seçilecek?

Optimizasyon (En verimli durum) nasıl sağlanır?

Performans için, yapı değişikliği gerekir mi? (Örneğin, KDV her zaman miktar ve KDV oranından hesaplanabilir. Normalde, tabloda KDV sütunu açmaya gerek yoktur.Fakat KDV miktarının sıkça istendiği bir şirkette, her defasında, KDV’yi yeniden hesaplatmak performansı düşüreceği için KDV sütunu tabloya eklemek daha mantıklıdır)

Bu bilgilerin işiği altında veritabanını oluşturmadan önce; hangi veriler girilecek, veriler bağlantılı olarak nasıl işlenecek ve hangi raporlar alınacak sorularına yanıtlar verebileceğimiz bir veritabanı kalıbının hazırlanması gerektiğini aklımızdan asla çıkarmamalıyız. Veritabanlari sistemlere install edildiğinde içlerinde ilişkisel veritabanının özelliklerini sağlayan küçük bir prototip bulunmaktadir. Örnek standart ilişkisel veritabani genellikle müşteri, sipariş ve sipariş detay gibi table lar içerir.. Bu veritabanında maçlananlardan bazılarını şu şekilde sıralayabiliriz.

Müşteri, sipariş ve stok bilgi girişlerinin sağlanması.

Kayıt eklemek, silmek ve değiştirmek

Müşteri adreslerini şehir koduna göre sıratmak

Bakiyesi belirli bir miktarı geçen müşterileri alfabetik sıraya göre listelemek

Bir bölgedeki müşterilerin belirli bir tarihe kadar, tüm senelik satiş ve borçlarının listelerini alabilmek

Verilen bir stokla ilgili tüm siparişleri görebilmek

Stoklarımızın son durumlarını görebilmek. Gerekiyorsa, sipariş vermek.

Satılan malların satış tutarlarını gözleyebilmek

Müşterilerimizle ilgili borç alacak takibini yapabilmek

Müşterilerimizle ilgili sipariş bilgilerini gözleyebilmek

Veritabanının özelliğine göre diğer seçenekler

**HTML (HyperText Markup Language)**

**HTML Nedir?**

HTML (HyperText Markup Language / Hareketli-Metin İşaretleme Dili) basitçe, browserlarla görebileceğimiz, internet dökümanları oluşturmaya yarayan bir çeşit dildir. Örneğin okuduğunuz bu sayfa HTML dili kullanılarak hazırlandı. Siz de browser'ınızı (Internet Explorer, Netscape Navigator,..) kullanarak bu sayfayı ekranınızda görüntülüyorsunuz. Tanımda geçen "internet dökümanı" ifadesinin yanısıra HTML ile oluşturduğunuz belgeleri harddiskinize kaydedebilir ve internet bağlantınız olmasa bile bu belgeleri görüntüleyebilirsiniz.

HTML, programlama dilleri (pascal, basic,..) gibi bir programlama mantığı taşımadığından öğrenilmesi gayet kolay bir dildir. Dilden ziyade kabaca metinleri ya da verileri biçimlendirmek, düzenlemek için kullandığımız komutlar dizisi bile diyebiliriz HTML için.

**HTML'de Temel Unsurlar**

HTML nispeten kolay bir dildir dedik. Bu dilde binary veya hexadecimal kodlar yok. Herşey metin tabanlı ve bir HTML dökümanı oluşturmak için ihtiyacınız olan şey bir editör. Hatta sizde herhangi bir HTML editörü bulunmuyorsa bu işi Windows'un *Notepad*'i ile dahi halledebilirsiniz. Piyasada iki tip editör bulunuyor. Birisi metin tabanlı, kod yazmayı gerektiren fakat bunun yanısıra rutin bazı işlemleri kolaylaştıran editörler *(HotDog, HomeSite..)* diğeri **WYSIWYG** (What You See Is What You Get / Ne görürsen onu alırsın) tarzı denen kısaca görsel, kodlamayla uğraştırmayı gerektirmeyen editörler *(FrontPage, Dreamweaver, NetObjects Fusion,..)*. Benim yeni başlayanlara tavsiyem Windows'un Notepad'i. Bu işlerin nasıl yapıldığını öğrendikçe ilerde siz de görsel editörlere geçebilirsiniz. Çünkü bir yerde istenmedik sonuçlar çıkabilir ve kodlara müdahele etmeniz gerekebilir. Üstelik görsel editörler bazen istenmeyen kodlar ekliyorlar, bu da döküman boyutunun büyümesi demek.

Burada şunu da belirtmek gerekiyor; browserlar arasındaki yorum farklarından dolayı sayfanız bir browser'da iyi görünürken bir başka browser'da hiç istemediğiniz bir şekilde görüntülenebilir. Hele yeni bazı teknikleri (css, dhtml gibi) sadece MS Internet Explorer 4 ve üstü desteklerken Netscape henüz bu teknikleri tam olarak desteklemiyor. Yine de piyasayı neredeyse yarı yarıya paylaşan bu iki browser'ın birbirlerine üstün olduğu yönleri var. Sonuçta, ne kadar fiyakalı bir sayfa da yapsanız elde ettiğiniz başarı sayfanızı ziyaret eden kişinin kullandığı browser'a mahkum. Hatta ziyaretçiniz browser'ına verdiği bir talimatla "yalnız şu fontu kullan", "grafikleri görüntüleme" şeklinde bir ayar yapmışsa emekleriniz boşa gitti demektir. Yine de bu kadar karamsar olmayalım.

**İlk sayfam**

İşte ilk HTML sayfamızı yapıyoruz.

Öncelikle çalışmalarınızı saklamak için kullanacağınız boş bir klasör oluşturup uygun bir ad verin, mesela html\_ders olsun. Daha sonra bu ad bize lazım olacağından kolaylık olması için siz de yeni klasöre bu adı verebilirsiniz.

Şimdi de bu klasörü açıp yeni bir **metin belgesi** oluşturun *(sağ fare/Yeni/Metin belgesi)*.

Dosyayı çift tıklayarak açın ve şunları yazın:

```html
<head>
<title>İlk Sayfam</title>
</head>
<body>
Sayfama Hoşgeldiniz
</body>
</html>
```

Şimdi dosyayı kaydedin *(Dosya/Farklı Kaydet...)*. Dosya adı kısmına şöyle yazın: *"sayfa1.htm"* (tırnaklar dahil) ve Tamam'a basın.

Notepad'i kapatın, metin dosyasını silin ve oluşan yeni dosyayı açın. Dosya varsayılan browser'ınız (Internet Explorer, Netscape Navigator gibi) tarafından açılacaktır. Şöyle bir görüntü elde edeceksiniz:

Tebrikler ilk HTML sayfanızı yaptınız.

Şimdi de bu belgeyi nasıl oluşturduğumuzu birlikte inceleyelim. Birşey dikkatinizi çekti mi? İngilizce bir takım kelimeler var ve bu kelimeleri küçük < ve büyük > sembolleri arasına yazdık. Bu ifadelere **tag** (etiket) deniyor. Etiketler etki etmesi istenilen metnin önüne ve arkasına yazılıyor. Önce etiketi yazıyoruz, sonra metni yazıyoruz daha sonra aynı etiketi önüne bir bölü işaretiyle tekrar yazıyoruz. Bu son yaptığımız etiketi sonlandırıyor. Bir kaç istisna dışında tüm etiketler belge içerisinde sonlandırılmak zorunda.

Burada kullandığımız etiketler ve anlamları şöyle:

```html
<html>...</html>
```

| Tarayıcıya HTML dosyasının başladığını ve bittiğini belirtiyor. Diğer tüm kodlar bu iki etiket arasına yazılır. |
| --- |

```html
<head>...</head>
<body>...</body>
```

| Bir HTML belgesi iki bölüme ayrılıyor: head(baş) ve body(gövde). <head>...</head> etiketleri arasına sayfa hakkında bilgiler yazıyoruz. meta ve title gibi etiketler burada yeralıyor. Meta etiketlerine ileride değineceğiz. <body>...</body> arası ise sayfamızın gövde bölümü. Ekranda gösterilecek kısımlar bu tagler arasında yeralıyor. |
| --- |

```html
<title>...</title>
```

| Title sayfanın başlığını belirtiyor. Burada yazılanlar browser'ın üst tarafında browser adıyla beraber gösteriliyor. |
| --- |

Hazırladığımız sayfada dikkat ederseniz sadece temel etiketleri kullandık. Yani metin biçimlendirmeye yarayan hiçbir etiket kullanmadık. Bu yüzden <body>....</body> arasına yazdığımız **Sayfama Hoşgeldiniz** yazısı browser'ın varsayılan metin ayarlarıyla gösteriliyor. İşin ilginç tarafı hiçbir kod yazmadan sadece **Sayfama Hoşgeldiniz** yazıp kaydetsek ve browser'da böyle görüntülesek de aynı neticeyi elde edecektik.

**Metin Biçimleme**

Bu bölümde öğreneceğimiz etiketler:

• Başlık etiketleri : <h1>...<h6>
• Paragraf etiketi : <p>...</p>
• Ortalama : <center>...</center>
• Diğer etiketler : <b>...</b>,<i>...</i>,<u>...</u>

HTML'de metin stillerini üç şekilde belirleyebiliriz:

Düzenlemek istediğimiz metnin hemen önüne koyacağımız bir etiketle biçimleme stili. Buna in-line (satır içi) biçimlendirme denir.

Sayfanın head (baş) kısmına koyulan stillere body (gövde) bölümden atıf yapılarak metin biçimleme. (Embedded-Gömülü biçimlendirme)

HTML dosyasının dışında başka bir stil dosyası oluşturarak stil için bu dosyayı kullanma. Buna Cascading Style Sheets-Yığılmalı Stil Kağıtları deniyor. Kısaca CSS. Bu teknik bize örneğin yüzlerce sayfanın stilini tek bir stil dosyası ile belirleme gibi geniş imkanlar veriyor.

Birinci metotta her metin için ayrı ayrı stil belirtirken ikinci ve üçüncü metodlarda stil bir defa belirleniyor ve bu stilleri istediğimiz metne uygulayabiliyoruz. Burada önemli olan bir diğer husus da ilk metodu tüm browserlar sorunsuz yorumlayabiliyor fakat 2. ve 3. metodu Internet Explorer ve Netscape'in son sürümleri (yorum farklılıkları ile beraber) destekliyorlar.

Burada konumuz birinci metoda göre biçimlendirmeyi öğrenmek. Başlık etiketlerinden başlıyoruz. Notepad'i açıyor ve şu kodları yazıyoruz;

```html
<html>
<head>
<title>Başlık Etiketleri</title>
</head>
<body>
<h1>Başlık 1</h1>
<h2>Başlık 2</h2>
<h3>Başlık 3</h3>
<h4>Başlık 4</h4>
<h5>Başlık 5</h5>
<h6>Başlık 6</h6>
</body>
</html>
```

Sayfanın işleyişine baktığımızda, önce her zaman yapmamız gerektiği gibi <html>, <head>, <title> etiketlerini yerleştirdik. Sayfa başlığı olarak "Başlık Etiketleri"ni seçtik ve sayfanın gövde <body> kısmına istediğimiz metinleri yazdık ve bu metinleri <h1>'den <h6>'ya kadar olan biçimlendirme etiketlerinin arasına aldık. Browser metin biçimleme etiketleri olan <h1>...<h6> etiketleri arasındaki kelimelere belirli büyüklükler verdi.

Şimdi de kendiniz <h1>...<h6> etiketlerinin yerlerini değiştirerek alıştırma yapın ve tam olarak bu işin nasıl olduğunu kavrayın. Hatta iyi bir deneme-yanılma olması açısından örneğin her seferinde değişik bir etiketi veya sonlandırma etiketini HTML kodundan silerek ne gibi etkiler oluşturduğunu gözlemleyin. Denemelerinizin bir kısmında hiçbir değişiklik olmadığını gözlemleyeceksiniz bunun sebebi, browser'ınızın otomatik olarak hatayı algılayıp düzeltmesidir.

Diğer etiketleri toplu olarak kullanarak yeni bir HTML dosyası oluşturalım. Kodlar şu şekilde olsun:

```html
<html>
<head>
<title>Başlık Etiketleri-2</title>
</head>
<body>
<h1><center>Sayfama Hoşgeldiniz</center></h1>
<p>HTML etiketleri ile, </p>
Yazıları <b>koyu </b> <i>italik </i> ve <u>altı çizili </u> olarak yazabiliyorum
</body>
</html>
```

Etiketleri kullanma mantığını anladınız herhalde. Biçimlendirmek istediğimiz metnin başına ilgili etiketi yazıyoruz ve metnin sonunda da ilgili etiketi sonlandırıyoruz. Etiket biz sonlandırmadığımız müddetçe etkisini göstermeye devam ediyor. Eğer hala tereddütleriniz varsa örnekler üzerindeki kodların yerlerini değiştirerek kaydedin ve diğer taraftan browser'ınızın **reload/yenile** tuşuna basarak değişiklikleri gözlemleyin.

Yeni öğrendiğimiz kodlara bir göz atalım:

```html
<center>....</center>
```

| Aradaki metinleri sayfaya göre ortalar. (center) |
| --- |

```html
<b>....</b>
```

| Aradaki metni koyu (bold) yazar. |
| --- |

```html
<i>....</i>
```

| Aradaki metni eğik (italic) yazar. |
| --- |

```html
<u>....</u>
```

| Aradaki metni altı çizili (underline) olarak yazar. |
| --- |

```html
<h1>....<h6>
```

| Başlık (heading) etiketi. h1 en büyük, h6 en küçük. |
| --- |

```html
<p>....</p>
```

| Aradaki metin paragraf özelliği kazanır. Sonlandırıldığında, takib eden metin bir satır boşluk bırakılarak ve satır başına yazılır. |
| --- |

Burada bilmeyenler için küçük bir bilgi; bir html dökümanını açtığımızda ve ekran üzerinde farenin sağ tuşuna tıklayıp *kaynağı görüntüle/view source*'u seçtiğimizde Internet Explorer için Notepad, Netscape için kendi Source Viewer'ı açılacak ve bize o sayfanın kodunu gösterecektir.

**Fontlar**

Font etiketinin kullanımı;

```html
<font face="..." size="..." color="...">...</font>
```

face= yazıtipinin adı (arial, tahoma, verdana, ...)
size= yazının büyüklüğü (1-7 arası)
color= yazının rengi (red, green gibi renklerin ingilizce karşılığı yada RGB renk değeri)

Bunlara font etiketinin parametreleri diyoruz.

<font> etiketinin yanısıra öğreneceğimiz bir diğer etiket <br> etiketi. Önce bu etiketin kullanımını göreceğiz. <br> etiketi bir bakıma enter tuşunun görevini görüyor. Bunu biraz açıklayalım; HTML'de metinleri yazarken kullandığımız editörde bir alt satıra geçmek için **Enter** tuşunu kullanırız. Fakat HTML dilinde bunun hiçbir anlamı yoktur, tüm kodları ve metinleri tek satırda dahi yazsanız browser açısından farketmeyecektir. Bu yüzden metinleri bölmek, yani ikinci satıra atmak için <br> etiketini kullanıyoruz. İstisnai etiketlerden birisi bu, <br> etiketi sonlandırılmıyor.

Buna bir örnek verelim;

```html
<html>
<head>
<title>BR etiketi</title>
</head>
<body>
pazartesi salı çarşamba
<br>ocak<br> şubat<br> mart<br> nisan
</body>
</html>
```

Yukarıdaki örneğimizde "pazartesi, salı ve çarşamba"yı yazarken Enter tuşu ile bir alt satıra geçmemize rağmen browser bunu gözönüne almayarak tüm metni bir satırda yazdı. Fakat ikinci sefer ay adlarını tek bir satıra yazdığımız halde bu kez browser aradaki <br> etiketine bakarak bir sonraki metni satır başına aldı. Buradan da anlaşıldığı üzere Enter tuşu etkisini <br> etiketiyle veriyoruz. Bu etiketin bir özelliği de sonlandırılmaması.

Şimdi font etiketinin kullanımını bir örnekle inceleyelim. Eğer kullanmak istediğiniz font bilgisayarınızda yüklü değilse font etiketi ile biçimlemek istediğiniz metin browser'ın varsayılan fontu ile gösterilecektir. Bu yüzden önce sisteminizde yüklü olan fontları inceleyin *(Başlat/Ayarlar/Denetim Masası/Yazıtipleri)*. Buradan yazıtiplerini açarak inceleyebilir ve beğendiklerinizi kullanabilirsiniz. Eğer benim örnekte kullandığım yazıtipleri *(tahoma, comic sans ms, verdana, arial)* sisteminizde yüklü değilse bunun yerine sizde olan istediğiniz fontu kullanabilirsiniz.

```html
<html>
<head>
<title>Renkler ve Mevsimler</title>
</head>
<body>
<font face="tahoma" size="5" color="#008000">İlkbahar</font> <br>
<font face="verdana" size="5" color="#ff0000">Yaz</font> <br>
<font face="arial" size="5" color="#ffff00">Sonbahar</font> <br>
<font face="comic sans ms" size="5" color="#0000ff">Kış</font> <br>
</body>
</html>
```

Her zamankinden farklı olarak ve ilk defa sayfamızda renk kullandık. Örnekte de gördüğünüz gibi bu işi renk kodlarıyla yaptık. Aslında bunun bir yolu daha var o da renk kodu yerine rengin ingilizce adını yazmak (color="red" gibi).

**Listeler**

HTML bize üç tip liste hazırlama imkanı veriyor. Bunlar;

Sıralı Listeler (ordered list)

Sırasız Listeler (unordered list)

Tanımlama Listeleri (definition list)

Sıralı listeler rakam veya harf yada her ikisini içiçe kullanarak liste oluşturmamızı, sırasız listeler rakam/harf yerine madde imleri koyarak liste oluşturmamızı sağlar. Tanımlama listeleri ise bir listeden çok kalabalık metinlerde okumayı kolaylaştırmaya yardımcı olabilecek bir araçtır.

**Sıralı Listeler**

Liste içine alınacak metinler <ol>...</ol> etiketleri arasına alınarak yazılır. Bu etiketler listenin başladığını ve bittiğini belirtir. Listenin maddelerinin başına ise <li> (list item) etiketini getiriyoruz. Bu etikette tıpkı <br> etiketi gibi sonlandırılmıyor. <ol> etiketine parametreler ekleyebiliyoruz. Bunlarla listemizin rakamla mı harfle mi başlayacağını **(type)** yada hangi rakam/harfle başlayacağını **(start)** belirtebiliyoruz. **Compact** parametresi ise listenin mümkün olan minimum satır aralığına sahip olmasını sağlıyor.

Bundan sonraki örneklerimizde sayfa kodunun yalnız body (gövde) bölümünü vereceğiz. Kodun geri kalan kısımlarını kendi sayfanızda tam olarak yazmayı unutmayın.

```html
<ol type="1">
<li>Kimya
<ol type="a">
<li>İnorganik
<li>Analitik
</ol>
<li>Fizik
<ol type="a">
<li>Dinamik
<li>Statik
</ol>
<li>Matematik
<ol type="a">
<li>Sayılar
<li>Diğer
<ol type="i">
<li>Türev
<li>İntegral
</ol>
</ol>
</ol>
```

| Kimya Organik İnorganik Analitik Fizik Dinamik Statik Matematik Sayılar Diğer Türev İntegral |
| --- |

Listeleri buradaki örnekte olduğu gibi iç içe hazırlamak ta mümkün. Dikkat edeceğimiz nokta, işe <ol> etiketi ile başlayıp liste maddelerinin her birisinin başına <li> etiketini getirmek ve listelemeyi bitirmek istediğimiz yerde </ol> etiketini yazmak. Liste içinde yeni bir liste oluşturmak istediğimizde listelenecek maddeden sonra tekrar <ol> etiketini yazıyoruz ve bahsedilen kuralları aynen uyguluyoruz. **Type** parametresinde kullanabileceğimiz değerler şunlar olabilir; sayılar,harfler (küçük/büyük) ve romen rakamları (i,ii,iii gibi)

**Sırasız Listeler**

Bu tip listede de mantık aynı. Fark, listeleme yaparken maddelerin başına harf, rakam gibi unsurlar yerine küçük yuvarlaklar,kareler kullanabilmemiz. <ol> etiketi yerine <ul> etiketini kullanıyoruz, liste maddeleri için kullandığımız <li> etiketi burada da geçerli. <ol> için kullanılabilecek parametreler ise şöyle; **type** için **disc** (içi dolu daire), **circle** (içi boş daire), **square** (içi dolu kare). **Compact** parametresi sırasız listelerde de kullanılabiliyor.

```html
<ul type="disc">
<li>Kimya
<ul type="square">
<li>İnorganik
<li>Analitik
</ul>
<li>Fizik
<ul type="square">
<li>Dinamik
<li>Statik
</ul>
<li>Matematik
<ul type="square">
<li>Sayılar
<li>Diğer
<ul type="circle">
<li>Türev
<li>İntegral
</ul>
</ul>
</ul>
```

| Kimya Organik İnorganik Analitik Fizik Dinamik Statik Matematik Sayılar Diğer Türev İntegral |
| --- |

**Tanımlama Listeler**

Bu listelemede kullanılan etiketler şöyle; <dl>...</dl> , <dd> , <dt> Listenin maddelerini belirtmek için kullandığımız <li> etiketinin yerini burada <dd> ve <dt> etiketleri alıyor. Aynı şekilde <ol>...</ol> veya <ul>...</ul> etiketleri arasına aldığımız listeyi bu sefer <dl>...</dl> arasına yazıyoruz. Yine parametre olarak <dl> etiketi içinde compact ifadesini kullanabiliriz.

**Renkler**

Metin renklendirmeyi yüzeysel olarak fontlar konusunda öğrendik. Şimdi daha ayıntılı olarak ve bu işin mantığına inerek yeniden ele alacağız. Aynı zamanda sayfamıza artalan rengi vermeyi öğreneceğiz.

Bu bölümde öğreneceğimiz konular:

**Renk Kodları**

Fontlar konusunda, metnin rengini belirlerken <font color="..."> etiketini kullanmıştık ve **color** komutunun karşısına rengin ingilizce karşılığını yazabiliriz demiştik. Fakat bunun daha karmaşık olan bir başka yolu vardı; o da 16'lık sayı düzeninde renk kodu girmek. Önce sayı düzenleri nedir nasıl olur ona bakalım.

Günlük hayatımızda kullandığımız sayı sistemine 10'luk sayı sistemi deniyor, tüm sayıları 0-9 arası toplam 10 rakamdan oluşan sembollerle ifade ediyoruz. 10'luk sayı sisteminin yanısıra diğer sayı sistemleri de vardır. Bunlardan bilgisayar alanında kullanılan iki tanesi ikili (binary) ve onaltılı (hexadecimal) sayı sistemleridir.

İkili sayı sistemi nasıl olur? Bildiğiniz gibi günlük hayatta kullandığımız 10'lu sayı sisteminde 0-9 arası toplam 10 rakam vardır. Aynı şekilde ikili sayı sisteminde de toplam 2 rakam var (bunlar 0 ve 1) ve tüm sayılar bu iki rakamı kullanarak ifade edilebilir, nasıl mı? İşte burada işin içine matematik giriyor. Kısa ve öz olarak belirtmek gerekirse 10'luk düzendeki bir sayıyı ikilik düzene çevirmek için o sayı devamlı olarak 2'ye bölünür ve kalanlar soldan sağa doğru yanyana yazılır.

Gelelim asıl konumuz olan 16'lık sayı sistemine. Bu sayı sisteminde de toplam 16 rakam var bunlar;

**0 1 2 3 4 5 6 7 8 9 A B C D E F **
\[10'un karşılığı A ... 15'in karşılığı F'dir.\]

Etikette kullandığımız color=#xxxxxx ifadesi ise RGB (red-green-blue,kırmızı-yeşil-mavi) renklerinin karışım oranlarını belirtir. Bu renklerden herbirinin alacağı değer 00 ile FF aralığında olabilir (FF maksimum, 00 minimum karışımı verir).

Buna göre; **#000000 siyah****, ****#FF0000 kırmızı****, ****#00FF00 yeşil****, ****#0000FF mavi****, ****#FFFFFF beyaz**'dır. Diğer renkleri sayıları değiştirerek kendiniz deneyebilirsiniz.

**Artalanı Renklendirmek**

Bu renklerle yalnızca metinleri değil sayfamızın artalananını da renklendirebiliriz.

Bunun için <body bgcolor=#xxxxxx> etiketini kullanıyoruz. Daha doğrusu sayfamızın gövdesini belirtmek için yazdığımız <body> etiketini, <body bgcolor=#xxxxxx> şeklinde değiştiriyoruz.

```html
<body bgcolor="#ffcc00">
<font type="verdana" size="4" color="#ffffff">
<ol><h2><u>Günler</u></h2>
<font color="#0000ff">
<li>Pazartesi <li>Salı <li>Çarşamba <li>Perşembe <li>Cuma
</font>
<font color="ff0000">
<li>Cumartesi <li>Pazar
</font>
</ol>
</font>
</body>
```

**Resimler**

Renkleri de öğrendikten sonra geldik en heyecanlı konuların bir diğerine, evet bu konuda sayfamıza ve artalana nasıl resim ekleyebileceğimizi öğreneceğiz. Bu konu aslında tablolar ve bağlantılarla da alakalı, bu yüzden burada genel olarak işleyeceğiz. Resim seçiminde, seçtiğimiz resmin **gif** yada **jpg** formatında olması zorunluluğu dışında herhangi bir kısıtlama yok. (telif hakları kanunu dışında tabi)

Resim ekleme işi gayet kolay. Yapmamız gereken browser'a sayfaya koyacağı resmin nerede olduğunu göstermekten ibaret. Her ne kadar şart olmasa da resmin pixel cinsinden en ve boy uzunluğunu belirtmeniz sizin hayrınıza olacaktır. Kullanacağımız etiket şu şekilde olacak;

```html
<img src="resmin bulunduğu yer ve adı" width="x" height="y">
```

Burada **x** resmin enini y ise boyunu belirtiyor. Bu bilgileri, resmi herhangi bir grafik editörüyle açarak öğrenebilirsiniz.

**Dikkat Edilecek Hususlar**

Örneğin bu sevimli kediyi sayfamıza ekleyelim, peki işte size bir soru: bu resmin nerede olduğunu browser'a nasıl izah ederiz?
Diyelim ki resmimizin adı **kedi.gif** eni **65**, boyu da **91** piksel, eğer bu resim html sayfamızla aynı dizinde duruyorsa sorun yok, kod aynen şu şekilde olmalı:

```html
<img src="kedi.gif" width="65" height="91">
```

**Bağlantılar**

```html
<a>...</a>
```

Geldik HTML'de en önemli unsurlardan birisi olan bağlantılara. Bağlantılar sayesinde hazırladığımız birçok sayfayı birbirleriyle ilişkili hale getirebiliriz. Bir tıklama bizi istediğimiz yere götürecektir. HTML'de metinlere ve resimlere bağlantı kazandırmak mümkündür. Örnek için bu sayfayı incelemeniz yeterli. Sol tarafta konuları veren bir menü bölümü var. Siz bu bağlantılardan birisini tıkladığınızda ilgili konu açılıyor, sayfa sonlarındaki ileri-geri düğmeleriyle de bağlantılar oluşturulmuş, bunlar da tıklandığında ilgili sayfa açılıyor. Bu yolla başka neler yapılabilir? Ses, grafik dosyaları, sıkıştırılmış dosyalar, internet adresleri,.. bunların hepsine bağlantı kazandırmak mümkün. Hatta yapacağımız bağlantı sayfa içinde, yani dahili bir bağlantı da olabilir.

Şimdi yapmak istediğimiz bağlantıya göre kullanacağımız komutları inceleyim:

```html
<a href="....">...</a>
```

Bu komutla oluşturduğumuz bağlantı ile yeni bir sayfa açabilir, kullanıcıyı farklı bir internet adresine yönlendirebilir, kullanıcının kendisine sunduğunuz bir dosyaya ulaşmasını sağlayabilirsiniz. Yani bu tanıma göre bildiğimiz bağlantıları oluşturmak mümkün.

Şimdi aşağıdaki örnekleri birlikte inceleyelim, fakat öncelikle bir kuralı belirtelim; <a>...</a> etiketi arasına yazdığımız yazılar bağlantı özelliğine sahip olacaktır, yazının bağlantı olduğu eğer aksi belirtilmemişse browser tarafından altı çizili ve mavi renkli gösterilir.

<a href="meyve.gif"> buraya tıklandığında meyve resmi açılacak </a>

Birinci örnekte "buraya tıklandığında meyve resmi açılacak" yazısına bağlantı özelliği kazandırdığımızdan browser tarafından altı çizili mavi yazıyla gösterilecek ve kullanıcı fare imlecini yazı üzerine getirdiğinde imleç el şekline dönüşecektir. Kullanıcı bu linke tıkladığında browser o anda açık bulunan sayfa ile aynı dizinde bulunan **meyve.gif** resmini açacaktır. Tabii ki dosya farklı bir dizinde ise kullanıcı hata mesajıyla karşılaşır.

<a href="midi.zip"> midi dosyalarını çekmek için tıklayın </a>

İkinci örnekte aynı şekilde "sıkıştırılmış midi dosyalarını çekmek için tıklayın" yazısına bağlantı özelliği kazandırdık. Fakat dosya tipinden kaynaklanan bir fark var; ilk örnekte **meyve.gif**'e tıklandığında browser resmi açacaktır fakat bu örnekte browser kullanıcıya **midi.zip** dosyasını açmak mı yoksa diske kaydetmek mi istediğini soran bir pencere açar. Bunun sebebi browser **htm**, **txt**, **jpg**, **gif**,.. uzantılı dosyaları görüntüleyebilirken **zip**, **doc**, **xls**, **mp3** gibi dosyaları görüntüleyememesidir.

<a href="sayfa2.htm"> 2.sayfaya gitmek için tıklayın </a>

Yine üçüncü örneğimizde oluşturduğumuz linke tıklandığında aynı dizinde bulunan sayfa isimli başka bir html dökümanı açılacaktır.

<a href="resim/kedi.jpg"> kedi resmi </a>

<a href="resim/bitki/karanfil.gif"> işte çok güzel bir karanfil </a>

<a href="../araba/bmw.jpg"> otomobil resimleri </a>

Bu 3 örnekte altdizinlere/üstdizinlere verilen bağlantıya misaller görüyorsunuz, resimler konusunda gördüğümüz kurallar burada da geçerli.

<a href="http://www.benimsitem.com/"> tıklayın sitemi ziyaret edin </a>

Yedinci örnekte bir internet adresi verdik.

<a href="ftp://ftp.benimsitem.com/"> tıklayın dosyaları indirin </a>

Bu ise bir ftp adresine verilen link örneği.

<a href="mailto: mdurcan@mail.com"> mail atın </a>

Buradaki linke tıklandığında kullanıcının ilgili mail programı açılacak ve mail'in send to (kime) kısmına verdiğimiz mail adresi otomatik olarak yazılacaktır.

**Resimlere bağlantı özelliği kazandırmak**

Metinlere bağlantı vermeyi öğrendik, peki sayfadaki resimlere nasıl link vereceğiz? Bunun için resmi yerleştirmek için kullandığımız:

<img src="..." width="x" height="y"> etiketini <a href>...</a> etiketinin arasına alıyoruz.

İşte örnek;

| <a href="sayfa1.htm"><img src="resim.gif" border="0"></a> |
| --- |

**resim.gif** tıklanacak resmi, **sayfa1.htm** resme tıklandığında açılacak sayfayı gösteriyor. **Border** komutu ise resimde bağlantı özelliği olduğunu belirten çerçeveyi kontrol ediyor, 0 (sıfır) değeri bu çerçeveyi tamamen yok eder. Bu komutu değişik sayılarla deneyebilirsiniz.

**Target parametresi**

Son olarak bağlantının açılacağı pencereyi belirtmek için kullanılan **target** parametresini öğrenelim. Kullanımı :

<a href="..." target="...">...</a>

target="\_blank"

| Bağlantı yeni bir pencerede açılır. |
| --- |

target="\_self"

| Bağlantı aynı pencere içerisinde açılır. |
| --- |

target="\_top"

| Bağlantı aynı pencere içerisinde en üstten itibaren açılır. |
| --- |

Target="\_parent"

| Açılan bağlantı, o anda açık sayfayı oluşturmuş bir ana sayfa varsa onun yerine konur. |
| --- |

**ASP (Active Server Pages)**

**ASP'nin Unsurları**

ASP tasarımcısı olarak, biz gerçekte ASP'nin Nesneleri ile birşeyler yaparız; başka bir deyişle ASP kodlarımız bu nesnelere yöneliktir, onları kullanma ve onlardan bir sonuç alma veya onlara bir sonuç aktarma amacına yöneliktir. ASP'nin Nesneleri altı grupta toplanır:

**Application/Uygulama:** Bir ASP sitesi, gerçekte bir Uygulama Programı olarak görülür. Bu, HTML/CGI geleneğine aşina tasarımcı için yeni bir kavram. ASP'yi icad edenler; bir ziyaretçi bir ASP sayfasından girerek, bir sitede **surfing**'e başladığında, onu bir programı işleten bilgisayar kullanıcısı olarak görüyorlar. Böylece, sitemiz, her ziyaretçinin karşısına çıktığında "bir program çalışmış" gibi sayılıyor. Bu yaklaşımın Web tasarımcısı olarak bize kazandırdığı imkanları ele alacağız.

**Session/Oturum:** Bir ziyaretçi sitemize geldiğinde, hangi sayfamızı talep ederse etsin, bu bağlantı ASP açısından bir oturum sayılır. Her oturumun belirli bir süre devam eden özellikleri, değişkenleri ve değerleri vardır. Site tasarımında oturum özelliklerinden geniş ölçüde yararlanacağız.

**Request/Talep:** Browser'dan Server'a ulaşan bütün bilgiler, **Request** (Talep) nesnesinin ögeleridir. Bu nesneyi kullanarak, istemciden gelen her türlü HTTP bilgisini kullanırız.

**Response/Karşılık:** Server'dan ziyaretçinin bilgisayarına gönderdiğimiz bütün bilgiler, çerezler (**cookie**) ve başlıklar (**Header**) **Response** (Karşılık) nesnesinin ögeleridir. Bu nesneyi kullanarak ziyaretçiye göndermek istediklerimizi göndeririz.

**Server/Sunucu:** ASP, Web Server programını bir nesne olarak ele alır ve onun bize sağladığı araçları ve imkanları kullanmamızı sağlar.

**ObjectContext/Nesne Bağlamı:** Microsoft'un Transaction Server (MTS) programının sunduğu hizmetlere erişmemizi sağlar. MTS, ASP sayfaları içinden, uygulama programlarından yararlanmamızı sağlar. ASP uzmanlığınızı ileri düzeylere ulaştırdığınız zaman MTS ve ObjectContext nesnesinden yararlanabilirsiniz.

**ASP'nin Dili **

ASP, bir teknolojidir. Kendi başına bir yazım kuralı yoktur. ASP tekniğini kullanabilmek için, ASP sayfasının talep edilmesi halinde ziyaretçiye gönderilmeden önce ASP.DLL'ye teslim edilmesi bu teknolojinin kullanılabilmesi için hemen hemen tek şarttır. Bunu, dosya uzantısını .asp yaparak sağlarız.

ASP.DLL ise, dünyada mevcut bütün Script dilleri ile verilecek komutları kabul edebilir. Sadece ASP.DLL'e sayfadaki kodların hangi dilde olduğunu söylemeniz gerekir. Bunu, ASP sayfasının birinci satırında yaparız. Örneğin ASP'ye VBScript dilini kullanmasını belirtmek için bu satırı şöyle yazarız:

<% @Language=VBScript %>

ASP sayfalarında genellikle VBScript, JavaScript ve JScript kullanılır. Ancak örneğin Perl dilinden türetilen PerlScript, PHP'den türetilen PHPScript de giderek ilgi çeken ASP dilleri arasına giriyor.

Bir ASP sayfası içinde farklı Script dilleri kullanılabilir.

**VbScript (Visual Basic Script)**

**VBScript'e Giriş**

Visual Basic dilini biliyorsanız, VBScript biliyorsunuz sayılır. VBScript, güçlü bir dildir; ancak Netscape firmasının hiç bir zaman Browser'ında istemci tarafında çalıştırılabilecek diller arasında kabul etmemesi sebebiyle VBScript, Web'in istemci tarafında kendisinden bekleneni yapamadı. MS'un Browser'ı Internet Explorer ise VBScript ile yazacağınız İstemci-Tarafı kodları okuyabilir ve icra edebilir.

Ne var ki ASP kodlarımız hiç bir zaman ziyaretçinin Browser'ının yüzünü göremeyeceği ve sadece Server'da çalışacağı için Server'da VBScript desteği bulunduğu sürece, ASP sayfalarınızı VBScript ile yazabilirsiniz. Bir Server'da ASP desteği varsa, VBScript desteği de var demektir.

VBScript'in hemen hemen bütün komutlarını ve yöntemlerini ASP'de kullanabilirsiniz. Ancak bunun bir kaç kısıtlaması vardır. VB veya VBScript'e ASP dışında aşina iseniz, mesaj kutusu (MsgBox) ve girdi kutusu (InputBox) aracılığı ile programlarınıza kullanıcının bilgi girmesini sağlayabileceğinizi biliyorsunuz demektir. Bu iki komutu ASP içindeki VBScript kodunda kullanamayız. Ayrıca ASP teknolojisi zaten VBScript'in bütün komutlarını ve deyimlerini kullanmanızı da gerekli kılmayacaktır. Göreceksiniz ki, mükemmel ASP sayfaları oluşturmak için bile bir avuç VBScript komutu kullanacağız.

ASP sayfalarımızdaki HTML kodları ile VBScript (veya diğer Script dillerinin) kodlarını birbirinden ayırmamız gerekir. Bu ASP.DLL'ye, HTML'in nerede bittiğini, Script diliyle yazılmış kodun nerede başladığını gösterebilmemiz için gerekli. Bunu sağlamak için Script diliyle yazılmış herşeyi "<%" ve "%> " işaretleri arasına alırız. ASP.DLL bu işaretleri görünce, içindekileri "yazmak" yerine "yapar." Bir ASP sayfanızda HTML'in klasik "<" ve ">" işaretleri arasındaki unsurlar, ASP.DLL tarafından ziyaretçiye gönderilecek olan sayfaya aynen aktarılır; ancak "<%" ve "%> " arasındaki herşey, başta belirttiğiniz LANGUAGE etiketinde yazılı Script dilinin yorumlayıcısına verilir; yorumlatılarak, gereği yerine getirilir.

"<%" ve "%>" işaretlerine "sınırlayıcı" denir. Sınırlayıcının içinde bir veya daha çok satır kod bulunabilir. Sınırlayıcılar ve içindeki Script, HTML etiketlerinin içinde veya dışında yer alabilir. Sınırlayıcının içindeki kodlarımızı açıklamak için koyacağımız yorum satırlarının başına tek tırnak işareti (') koyarız. İşte bu kuralları uyguladığımız bir ASP sayfası örneği:

<% @LANGUAGE=VBscript %>

<html>

<head>

<title>Hoşgeldiniz!</title>

<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</head>

<body>

<center>

<%

' Yazı tipi boyutunu tutacağımız bir değişken

tanımlayalım

Dim fontBoyut

%>

<%

' yazı tipi boyutunu 1'den 7'ye kadar değiştirelim

For fontBoyut = 1 To 7

%>

<font size = <%=fontBoyut%>>

Hoşgeldiniz!<br>

<% Next %>

</center>

<h3>Bugün <% =WeekdayName(Weekday(Date)) %>, <% = Date %>.

Şu anda Server'da saat: <% = Time %>.<p>

</h3>

</body>

</html>Burada sınırlayıcı arasında tek veya çok satırlı VBScript kodları ile başında tek tırnak olan icra edilmeyen, yorum satırlarını görüyorsunuz. HTML etiketinin içine gömülmüş VBScript kodu ise HTML'in <FONT> etiketinde yer alıyor: <font size = <%=fontBoyut%>>. Burada karşılaştığımız "<%=" ifadesi, ASP'ye, "Bu değişkenin değerini bul ve tam buraya yaz!" dememizi sağlıyor. Bu ifade daha sonra yakından ele alacağımız Response.Write metodunun kısaltılmış halidir. HTML etiketinin içine yazdığımız VBScript bölümünün kendi sınırlayıcı işaretlerinin yine de kullanıldığına dikkat edin.

**JavaScript**

**Javascript Nedir?**

Başlangıçta bazı konulara açıklık getirelim. Java ile JavaScript oldukça fazla derecede karıştırılmakta. Java Sun firması tarafından Pascal ve Delphi dillerinden esinlenerek yazılmış bir programlama dilidir. Sonuçta tarayıcıdan bağımsız bir program elde edersiniz. Yani bir exe veya com uzantılı dosya vardır elinizde. Fakat JavaScript bu tür bir programlama dili değildir. Yorumlanması için bir tarayıcıya ihtiyaç duyar. Bu yüzden script dilidir. Html dosyasını içine gömülüdür. Sonuçta elinizde exe veya com uzantılı bir dosya yoktur. Javascript , Netscape firması tarafından C dilinden esinlenilerek yazılmıştır. Yazılma amacı Html'in sahip olmadığı bazı özelliklerin web sayfalarında kullanılmak istenmesidir. Yani ziyaretçi ile etkileşim gibi önemli unsurlar Html'de yok veya oldukça az kapasitede diyebiliriz. Netscape firması bu konuya ağırlık vererek JavaScript script dilini internet ortamına kazandırmıştır.

Gelelim Netscape ve Internet Explorer tarayıcılarının JavaScript kodundaki farklı anlayışa. Bu gerçekten doğrudur. Netscape firması JavaScript dilini hazırladığında Microsoft firması bu dilin özelliklerini veya yazılım tarzını tam anlamıyla Internet Explorer'a eklemedi. Kendi yazım kurallarını belirledi. Bu yüzden biz JavaScript kodu yazarken bu iki tarayıcı özelliklerini de göz önünde bulundurmalıyız. Fakat bu her kodda karşımıza çıkmaz. Biz derslerimizde gerektiği yerde bu konuya yer vereceğiz.

Java Script'in bazı genel özellikleri :

Javascript kodlarını yazmak için Windows kullanıcıları için NotePad, Mac. kullanıcıları için Simple Text yeterlidir.

JavaScript kodları etiketi ile biter.

Etiketi JavaScript'i anlamayan eski sürüm tarayıcıların bu kısmı geçmeleri içindir.

Genellikle yazım tarzı

| <script> <!-- JavaScript kodları --> </script> |
| --- |

şeklindedir.

İyi bir programcı kod satırlarında açıklama yapar. Bu satır şu işlemi gerçekleştiriyor gibi açıklayıcı bilgiler yazar kodlarının yanına. JavaScript'te bu tür açıklama // ile başlar ve // ile biter. Eğer açıklamanız bir satırdan fazla ise /\* ile başlar \*/ ile biter.

| // bu satır kullanılacak değişkenlerin tanımlanması /\* açıklama satırı 1 açıklama satırı 2 açıklama satırı 3 \*/ |
| --- |

JavaScript kodları Html kodların arasında yer alır. Veya uzantısı js olan dosyalarda saklanarak yine Html içerisinden çağırılır. Java Appletleri gibi Html'den ayrı bir unsur değildir. Javascript Html'in bir parçasıdır.

Kullanılacak yere göre Html'in içerisinde kullanılır. Fakat genelde <head>...</head> etiketleri arasında kullanılır.

Javascript kodları bittiğinde elinizde asla kendi başına çalışan uzantısı exe veya com olan bir dosya olmaz. Her zaman için tarayıcı tarafından yorumlanması gerekir. Yorumlanması demek Javascript kodunun çalışması anlamındadır.

Nesne ve buna uygulanan olaylar ile ilgili bir takım görevleri vardır. Javascript kullandığı her unsuru nesne olarak algılar. Siz bu nesneleri tıklamak, üzerine gelmek, üzerinde çıkmak gibi olaylar ile çalıştırırsınız ki bu da Javascript'in ziyaretçi ile etkileşmesi demektir.

Genel öğrenim yapımız diğer programlama dillerine nazaran biraz farklı olacaktır. Bu Javascript'in bir script dili olmasında ileri gelir.

**Değişkenler**

**Genel Değişken Özellikleri**

Değişkenler Javascript'te ve diğer programlama dillerinde olduğu gibi bilgi depolamak bu bilgiyi kullanmak amacıyla kullanılırlar. Değişkenler "var" komutu ile oluşturulurlar. Karakter olarak kullanıldıklarında işlem yapılamazlar. Nümerik olarak kullanıldıklarında ancak işlem yapabilirler. Kullanımına bir örnek verelim.

| var sayi; var sayi1=10; var yazi1="10"; |
| --- |

Burada birinci satırdaki "sayi" değişkeni script kodunun herhangi bir yerinde kullanılmak üzere oluşturulmuştur. İkinci satırda "sayi1" adındaki değişkenin değeri hemen o satırda = ifadesinden sonra verilmiştir. Böyle değişken tanımıda yapılabilir. Üçüncü satırda ise değişkenin karakter ifadesi olarak kullanımını görüyoruz. Burada önemli olan karakter değişkenlerin alıntı " " ifadesinin arasında kullanılmasıdır. Her değişkenden sonra ; işareti konulmalıdır. Tarayıcı, bir başka komut satırına geçtiğini bu yol ile anlar.

Şimdi değişkenlerle ilgili matematik işlemlerinin nasıl olacağını görelim. Bunu daha iyi açıklayabilmek için örnekler üzerinde çalışalım.

| var sayi1=10; var sayi2=20; var sayi3=sayi1+sayi2; |
| --- |

Birinci ve ikinci satırlarda değişkenler oluşturduk. Üçüncü satırdaki ise sayi3 değişkeni ile diğer iki değişkeni topladık. Burada önemli olan işlem yapmak istediğimizde değişken değerinin alıntı " " işaretlerinin arasına konmamasıdır. Üçüncü satırı - ileride göreceğimiz write () fonksiyonu ile - tarayıcıda yazdırırsak göreceğimiz değer 30'dur.

Şimdi de değişkenleri karakter olarak tanımladığımızda neler olduğuna bakalım.

| var sayi1="10"; var sayi2="20"; var sayi3= sayi1+sayi2; |
| --- |

Bir önceki örnekten farklı olarak değişken değerlerinin alıntı işaretleri içerisinde yazdık. Eğer sayi3 adlı değişkeni tarayıcıda bastırırsak göreceğimiz ifade 1020 ifadesidir. Yani tarayıcı karakter olarak tanımladığımız değişkenleri ardada ekledi. Burada unutulmaması gereken şey bunun sadece + işleminde geçerli olmasıdır. Diğer işlem türlerinde bu tür bir sonuç alınamaz.

Değişkenlere ad verirken uymamız gereken kurallar.

Değişken isimleri harf veya \_ karakteri ile başlayabilir. Rakam kullanmak istersek 2. karakterden sonra kullanabiliriz. Yani değişkenin ilk karakteri rakam olamaz.

| var url="webteknikleri"; doğru var \_rakam=12; doğru var a1=123; doğru var 3uzler="üçüzler" yanlış |
| --- |

Değişken tanımlarken bir veya birden fazla boşluk bırakmak tanımlama açısından herhangi bir sorun teşkil etmez.

Değişken adı verirken kullandığımız harflerin büyük veya küçük olması bazı tarayıcılarda fark etmezken çoğu tarayıcıda farklı bir değişken anlamındadır.

**Değişkenlerin işlem operatörleri ile kullanımı **

Değişkenlere işlem yaptırabilecek operatörleri ve özelliklerini inceleyelim. Operatörleri birkaç kısıma ayırarak inceleyelim;

Aritmetik operatörler

Karşılaştırmak operatörleri

Mantıksal operatörler

Özel operatörler

**Aritmetik Operatörler**

Her zaman kullandığımız bu operatörler + , - , \* , / , % 'dir.Değişkenlerin çeşitli aritmetik operatörlerle kullanımına bir örnek verelim.

| var i=10; var j=11; var k=12; var m,n; m=i\*j+k; n=i\*(j+k); |
| --- |

Şimdi örneğimizi inceleyelim:

İlk üç satırda değişkenlerimizi hem tanımlayıp hem de değer atadık. Dördüncü satırda ise m ve n değişkenlerini tanımlayıp değer atamdık. Diğer satırlarda ise m ve n değişkenlerinden istenen işlemleri tanımladık. Buna göre son iki satırın sonuçları farklıdır. Çünkü parantezlerin işlem önceliği vardır.

Beşinci satırın cevabı (10\*11)+12 = 122 şeklinde olacaktır. Son satırda ise sonuç 10\*(11+12) = 230 olacaktır. Diğer bir işlem operatörü olan % 'nin yaptığı işlemi şu şekilde anlatabiliriz.% operatörü % işaretinin solundaki değişkeni sağındaki değişkene böler ve kalanı verir. Örnek olarak;

| var a=100; var b=9; var c=100%9; |
| --- |

Burada c değişkenin değeri 100/9'un kalanı 1'dir. Yani c değişkeninin değeri 1 olacaktır. Diğer -(eksi) ve / (bölme) operatörlerinin işlemleri kendilerine atanan çıkartma ve bölme işlemidir.Bu operatörlerin kısa kullanımı içinde Javascript bize kolaylık sağlar. Bu operatörleri sıralamak istersek;

-= : \*= : /= : %= : ++ : --

Bu operatörlerin kısa uzun şekilde yazılışları ise;

| x+=y x=x+y x-=y x=x-y x\*=y x=x\*y x/=y x=x/y x%=y x=x%y x++ x=x+1 x-- x=x-1 |
| --- |

şeklindedir.

Bu operatörlerin nasıl işlem yaptığını bir örnekte görelim.

| var x,y,z; x=10; y=20; z=30; x++; x+=y; z--; y\*= z; |
| --- |

Şimdi her zamanki gibi işlem satırlarının cevaplarını birlikte bulalım.

x++ satırı x=x+1 işleminin yapılmasını söyler. Buna göre x değişkeni 11 değerini alır.İkinci satıra geldiğimizde x+=y satırı x=x+y işleminin yapılmasını söyler. Bir önceki satırdaki x'in değeri 11 idi. Böylelikle yeni x'in değeri 11+20=31 olacaktır. Diğer satırda z-- işlemi sonucunda z'nin değeri 29 olacaktır. Son satırda ise y=y\*z işlemi ile y değişkeni 20\*29= 380 değerini alacaktır.

**Karşılaştırma operatörleri**

Bu operatörler değişkenlerin birbirleri ile karşılaştırılmak istendiğinde kullanılır.

**==** operatörü iki değişkenin birbirine eşitliğini kontrol eder.

**!=** operatörü iki değişkenin birbirine eşit olmadığı durumlarda kullanılır.

**<** operatörü bilindiği üzere küçüktür operatörüdür. Soldaki değişkenin sağdakinde

küçüklüğünü kontrol eder.

**<=** soldaki değişkenin sağdaki değişkene küçük eşitliğini kontrol eder.

**>** soldaki değişkenin sağdaki değişkene göre büyük olup olmadığını kontrol eder.

**>=** soldaki değişkenin sağdaki değişkene büyük eşitliğini kontrol eder.

**Mantıksal Operatörler**

Bu tip operatörler iki değişkene bağlı karşılaştırılmaların yapılmak istendiği durumlarda kullanılır.

Operatörler && , || , ! operatörleridir.

**&&** And (ve) operatörü iki değişkenin de değeri doğru olması istendiğinde kullanılır.

**||** Or (veya) operatörü iki değişkenden en az birinin doğru olması durumu

istediğinde kullanılır.

**!** Not (değil) operatörü değişkenin değeri doğru ise yanlış , yanlış ise doğru olması istendiği durumlarda kullanılır.

**Özel karşılaştırma Operatörü**

Bu operatör iki değişken arasında karşılaştırma yapmanın en sade ve kısa yoludur.

Operatörün kullanım biçimi :

| değişken\_1 \[istenen karşılaştırma operatörü\] değişken\_2 ? değişken\_3 : değişken\_4 |
| --- |

Bunu bir örnekle açıklayalım.

Değişkenleri var ile tanımladığımızı farz ediyorum. Buna göre;

| a < b ? c : d |
| --- |

Yukarıdaki satırda yapılması istenen işlem;

a değişkeninin b değişkeninden küçük olup olmadığı karşılaştırılıyor. Buna göre cevap doğruysa işlemin sonucu c değişkeninin değeri değilse d değişkeni oluyor.

Şimdi tüm bu öğrendiklerimizi bir Javascript kodunda görelim. Bu bizim ilk Javascript kodumuz olacak.

| <script Language="JavaScript 1.2"> <!-- var i=1; var j=2; var k=3; var m=4; var n=5; var p=6; var q=7; i=+j; j++; k--; m=m+k; n=\*j; i < j ? 3 : 1 ; k >= n ? 0 : 1 ; k=2 && j=5 ? p : q ; i=2 \|\| j=3 ? m : n ; p!=2 ? k : 10 ; -- > </script> |
| --- |

İlk yedi satırda değişkenlerimizi hem tanımladık hem de değer atadık. Böyle bir yazımı yapabileceğimizi değişkenleri anlatmaya başlarken söylemiştik.

İşlem satırlarına geçtiğimizde ise;

**i+=j;**

Bu işlem daha da önce gördüğümüz gibi bize i=i+j işlemini yapmamızı söyler. Buna göre i değişkeninin değeri 3 olacaktır. Hemen altındaki satırda bulunan j++ işlemi dolayısıyla da j değişkeni 3 değerini alacaktır. Diğer işlem satırında k--işlemi ile de k değişkeni 2 değerini alır. Bir diğer satırdaki m=m+k işlemi ile m(m=4) değişkeni k(k=2) değişkeni toplanarak 6 değerini alır. n=\*j işlemi ile de n(n=5) değişkeni 3\*5=15 değerini alacaktır.

Şimdi diğer karşılaştırma işlemlerine geçmeden önce değişkenlerimizin işlem sonrası aldığı değerleri yazalım.

**i=3 , j=3 , k=2 , m=6 , n=15 , p=6 , q=7 ; i < j ? 3: 1; **

Bu satırın 3 < 3 işleminin cevabı doğru ise 3 değilse 1 değeri alacağını görebiliyoruz. Tabi ki üç üçten küçük olmadığı için cevabımız 1 olacaktır.

**k>=n ? 0 : 1;**

Bu satırda ise 2>=15 işlemi gerçekleşir ki bunun cevabı da yanlıştır ve ikinci değer işlem satırının cevabıdır yani 1 dir.

Şimdiki karşılaştırma işlemimiz ise mantıksal operatörlerle ilgili. Buna göre;

**k=2 && j=5 ? p : q; **

İşlem bize ne söylüyor ? k değişkeni ve j değişkeninin kesin olarak bir değere eşit olup olmadığını karşılaştırmamızı söylüyor. Bu iki değer de doğruysa çünkü &&(and) mantıksal operatörünün anlamı bu işlem doğrudur değilse yanlıştır. Buna göre k=2 'dir. Fakat buna karşılık j'nin değeri 5 değildir. Bu yüzden karşılaştırmanın cevabı yanlıştır. Dolayısıyla işlem q yani 7 değerini alır.

**p!=2 ? k : 10;**

İşlemde istenilen p değişkeninin değerinin ikiden farklı olması durumdur. Yani 6!=2 bunun anlamı doğrudur. Gerçektende 6=2 değildir. Bizde bu satırda bunu istiyorduk. O halde cevap doğrudur. Böylelikle işlem k yani 2 değerini alır.

Şimdi biz bu yaptıklarımızla sadece javascript'te bir şeyler hesap etmesini ve karşılaştırmasını söyledik. Tarayıcı da bu işlemleri yapar ve hafızasında tutar. Daha sonra öğreneceğimiz komutlarla bunları istersek tarayıcıya yazdırabilir. Başka bir yerde kullanılmasını söyleyebiliriz.

**Internet Explorer & Netscape Farkı**

Giriş kısmında belirttiğimiz gibi Javascript kodlarında MSIE (Microsoft Internet Explorer) ve NN (Netscape Navigator) yönünden farklılık vardır. Bu tarayıcının html dökümanı nasıl modellediğine bağlıdır. Tarayıcının nesne döküman modeli, bir Html sayfasındaki çeşitli elemanların tarayıcı tarafından nasıl algılanıp yorumlandığı ile ilgilidir. Javascript gerçekte W3C (Web tekniklerinin standartlarını belirleyen kurum www.w3c.org) konsorsiyumu tarafından belirlenen kodlardan oluşmamıştır. Tarayıcı üreten firmalar bu konuları kendilerince yorumlayıp tarayıcılarına yerleştirmişlerdir. Yani kendi nesne döküman modellerini oluşturmuşlardır.

Biz bu kısımda her iki tarayıcınında nesne döküman modelini incelemeyeceğiz. Bize gerekli olan kısmını öğreneceğiz. Şimdi tarayıcı farkının nasıl ayırt edilebileceğini görelim.

| ie4 = (document.all) ? true : false; nn4 = (document.style) ? true : false; |
| --- |

Biz bu iki satırla bir önceki ders olan değişkenler ve mantıksal operatörler yardımıyla iki tarayıcıyı da kontrol altına aldık. Bir diğer örnekle yapıyı pekiştirelim.

| <script language="Javascript"> <!-- // Kodları eski sürüm tarayıcılardan saklayalım. ie4 = (document.all) ? true : false ; nn4 = (document.style) ? true : false ; if (ie4) { // MSIE 4.0 için uygun kodları buraya yazacağız } else { // NN 4.0 için uygun kodları buraya yazacağız. } //Saklamayı bitir --> </script> |
| --- |

Şimdi bu kodları inceleyelim. Değişken tanımlama kısmının anlaşıldığını varsayarak geçiyorum. Anlamadığınız bir kısım varsa 1. Değişkenler kısmına tekrar geri dönün.

**If (ie4) ve if (nn4)**

Burada ileriki derslerde öğreneceğimiz koşul ifadesini kullanıyoruz. Bu kodları Javascript'in anlayış tarzı şu şekilde olacaktır. Eğer nn4 , ie4 değişkenlerinden doğru olanı ie4 ise -ki bunu true ve false değerlerinden algılar- alt satıra geçip ona uygun kodu uygulayacaktır. Şayet ie4=false yani nn4=true ise diğer if koşulu yorumlanarak işleme konulacaktır. Bu da nn4 için gerekli kodun çalıştırılması demektir.

| <html> <head> <title>Tarayıcı kontrolü</title> <head> <script language="Javascript"> <!-- // Kodları eski sürüm tarayıcılardan saklayalım. function tarayici() { ie4 = (document.all) ? true : false ; nn4 = (document.style) ? true : false ; if (ie4) { // MSIE 4.0 için uygun kodları buraya yazacağız. window.location="ie.htm"; } else { // NN 4.0 için uygun kodları buraya yazacağız. window.location="nn.htm"; } } //Saklamayı bitir --> </script> </head> <body onLoad=tarayici()> </body> </html> |
| --- |

Bu kodları herhangi bir editör (NotePad gibi) yardımıyla yazıp **tara.htm** olarak kaydedin.

| <html> <head> <title>MSIE tarayıcı kullanıyorsunuz</title> </head> <body> <h3>Tarayıcınız Internet Explorer</h3> </body> </html> |
| --- |

Bu kodu **ie.htm** olarak kaydedin.

| <html> <head> <title>Netscpae tarayıcı kullanıyorsunuz</title> </head> <body> <h3>Tarayıcınız Netscape Navigator</h3> </body> </html> |
| --- |

Bu kodu **nn.htm** olarak kaydedin.

**Önemli!:** Bu üç Html dosyasının da aynı klasörde olması gereklidir

**Ekrana Çıktı ve Klavyeden Bilgi Giriş**

Bu dersimizde Html üzerinden klavye aracılığı ile ziyaretçiden bilgi almasını ve herhangi bir değişken vb. Türde yazıların html e nasıl yazdırılacağını göreceğiz.

**Prompt ()**

Ziyaretçiden bilgi alma iki tür JavaScript komutuyla gerçekleşir. Birisi Prompt yani bizim burada bahsedeceğimiz komut. Diğeri ise Form yoluyla bilgi alınması. Form yoluyla alınan bilgiler formun Html üzerinde yer alması yüzünden Prompt komutu ile birbirinden ayrılır. Prompt komutu ile Html sayfasından hariç bir pencere açılır. Alınmak istenen bilgi ziyaretçiye bu yol ile sorulur ve hemen altındaki boşluk yardımıyla cevap alınır. Şimdi kodun nasıl kullanıldığına bir göz atalım.

| prompt ("Sorulan soru" , "Cevap örneği") |
| --- |

Bu komutun yorumlanışı şu şekildedir. Html üzerinde Html'den bağımsız bir pencere aç. (bu prompt komutu ile yapılır) İlk çift tırnak içerisinde olan kelime veya kelime grubu, pencerenin üst kısmında ve değiştirilemeyen kısımdır. Burada soru veya pencerenin niçin açıldığı ile ilgili bir açıklama verilir. İkinci çift tırnakta ise doldurulacak olan cevap satırının içinde seçili bir haldedir. Bu ise genel olarak cevap örneği olarak ziyaretçiye sunulur. Kullanılması zorunlu değildir. Kullanılmadığınızda undefined gibi tanımlanmamış uyarısı alınır.

| prompt ("Tarayıcınızın türünü giriniz ?" ,"lütfen cevabı ie veya nn olarak veriniz"); |
| --- |

Şimdi kullanıcıdan nasıl bilgi alınacağını gördük fakat bu bilgiyi nasıl kullanabiliriz? Bu sorunun cevabı prompt komutunu var ile bir değişkene atmak suretiyle kullanabiliriz olacaktır. Yani;

| var tara=prompt ("Tarayıcınızın türünü giriniz ?" ,"lütfen cevabı ie veya nn olarak veriniz"); |
| --- |

Biz bu satır ile ne yapmış olduk ? Ziyaretçiden prompt komutu ile tarayıcısı sorduk ve bunu var değişken tanımlama komutuyla tara değişkenine atadık. Ziyaretçiden aldığımız bu bilgi sonucunda tara değişkeni ya ie yada nn değerini alacaktır. Biz daha sonraki satırlarda bu değişkeni belli bir koşul koyarak kullanabiliriz. Mesela daha önceki örneklerimizde olduğu gibi ie ise şu sayfayı aç nn ise şu sayfayı aç.

Bir öneri , bu tip tarayıcı tanıma yöntemi oldukça yanlış bir yöntemdir. Çünkü ziyaretçiden alınan bilgi ile bizim daha sonra kullandığımız koşul ifadeleri uyuşmayabilir. Bu yüzden kodumuz doğru çalışmaz.

**Write()**

Html dosyasına yazı yazdırma komutu ise write dır. Bu kodun yazım kurallarını inceleyecek olursak;

| document.write ("görüntülenmek istenenler" , değişken\_ismi ); |
| --- |

Kodu inceleyelim. Javascript html üzerinde yazı yazmak istediğinde write komutunu tek başına kullanamaz. Bunun için document fonksiyoneli (yardımcısı manasında) ile birlikte kullanılır. document.write komutundan sonra parantez açılır. Daha sonra yazılmak istenen sıraya göre değişken ismi veya görüntülenmek istenenler yazılır. Değişkenler çift tırnak içerisinde yazılmazlar. Sadece görüntülenmek istenenler çift tırnak içerisinde yazılır.

Şimdi prompt komutu ile write komutunu birleştirerek bir kod hazırlayalım. Bu kodumuzda prompt aracılığıyla ziyaretçiye adını sorup ad değişkenine atıyoruz. Daha sonra bu değişkeni write komutu yardımıyla ziyaretçiye Merhaba diyoruz. Şimdi kodlara geçelim.

| <html> <head> <title>Prompt , write örneği </title> </head> <body> <!-- //Kodları eski tarayıcılardan gizliyoruz var isim = prompt ("İsminizi Giriniz " , "Küçük harf veya büyük harf kullanabilirsiniz" ); document.write ("Merhaba " , isim , " !" ); // Saklamayı bitir --> </script> </body> </html> |
| --- |

Eski kodlarımıza göre bu kod biraz farklı değil mi ? Hemen göze çarpıyor ki Javascript kodumuz **<head>** etiketleri arasında değil. Daha öncede dediğimiz gibi uygulanması istenen sıraya bağlı olarak kod yerini aldı.

Biz aslında Html'de font kurallarını kullanarak yazı da yazdırabiliriz. Eğer hiçbir kural uygulamadığınız tarayıcının banko (default) değerleri kullanılır. Örneğin Merhaba dedikten sonra alınan ismin bir alt satırda görüntülenmesini istiyorsak bunu Javascript'e şu şekilde yaptırabiliriz.

| document.write ("Merhaba" , " " , isim) |
| --- |

Bu tür (yani **<br>** türünde) Html etiketlerinin tümünü Javascript'e yaptırabilirsiniz. Hatta ileride göreceksiniz ki Javascript zerinden Html yazmadan web sayfası yapılabilir. Aslında Html yazmıyor değiliz fakat bunu **<body>** etiketlerinde yani Html dökümanı içerisinde yapmıyoruz. Bunu için Javascript'e emir veriyoruz. Bu normal olarak kimi zaman hissedilir derecede olmasa bile sayfanın yavaş yüklenmesine neden olur. Bu yüzden web sayfası üzerinde yaptığınız işleme göre kodunuzu yazın.

**Koşul Yapıları**

Bu dersimizde Javascript'in en önemli özelliklerinden birine değineceğiz. Aslında bu konu sadece Javascript'in değil bilgisayarın da en önemli konusudur. Bilgisayarı bilgisayar yapan konu budur. Çünkü hiçbir bilgisayar kendi kafasına göre yorum yapamaz. Bizim verdiğimiz belli kıstasları göz önünde bulundurarak seçim yapar o kadar. Şimdi konunun inceliklerine bir göz atalım.

**If (Eğer)**

Javascript'te çoğu dilde olduğu gibi koşul yapısının kodu If (eğer) komutudur. Yazılım şekli ise şu şöyledir.

| If (a==b) //koşul doğru ise ilk satır işleme konulur //koşul doğru değilse ilk satırın altındaki komut satırı işleme konulur. |
| --- |

Koşul komutu yani if ile işleme başlıyoruz. Daha sonra karşılaştırılacak değişkenler veya başka nesneler parantez içerisinde sorgulanıyor. Dikkat ederseniz çift eşittir kullandık. Çünkü tek eşittir işareti değer atama işlemidir. Çift değişken ile koşul yapısı sağlanır. Eğer koşul doğruysa hemen altındaki satır işleme konulur. Eğer koşul yanlış ise ikinci satır işleme konulur. Yok ben koşul doğru ise 2 ve daha çok işlem yaptırmak istiyorsanız bunun cevabı yapılması istenen işlemlerin { } arasında yer almasıdır. Yani:

| If (a==b) { // 1.işlem //2. İşlem ... ... } |
| --- |

**If .. Else (Eğer ... Değilse)**

Bu bölümde ise If koşul ifademize Else komutunu ekleyerek koşul yapımızı güçlendiriyoruz. Şimdi bu ne demek. Hemen bir örnekle açıklayalım.

| If ( a==b ) { // şunları şunları yap } else { //değilse şunları yap } |
| --- |

Yani örnekten de anlaşıldığı gibi if koşulu ile a ile b nin eşitliği karşılaştırılıyor. Eğer doğruysa hemen altındaki kısım işleme konuluyor. Else ile yok değilse altındaki kısmı işleme koy diyoruz. Şimdi diyeceksiniz ki bir öncekinden ne farkı var. Bu haliyle hiçbir farkı yok. Fakat şu örneğe bir bakalım.

| If (a==b) { //şunları yap } if (a==c) { //şunları yap } else { //şunları yap } |
| --- |

Şimdi bu kodda Javascript'e ne yapmasını söyledik. a değişkeni b değişkenine eşitse normal olarak alt satırı işleme koy. Eğer bu karşılaştırma yanlış ise altındaki işlemleri geçerek a'nın c'ye eşitliği kontrol edilecek. Bu da değilse (else) alt satırdaki işlemleri devreye koy.

Else yapısı genel olarak bir karşılaştırma sonucunda cevap yanlış ise diğer bütün durumlarda şu işi yap manasında kullanılır.

| <html> <head> <title>Koşul yapıları </title> </head> <body> <script language="JavaScript"> <!-- //eski sürüm tarayıcılardan kodumuzu saklayalım var gun = prompt ("Bugün günlerden ne ?" ,"lütfen küçük harf kullanınız"); if (gun=="pazar") { document.write ("Bugün günlerden " , gun , " olduğuna göre hatfa sonundayız" ,"<br>") document.write ("<b>" , "İyi tatiller.." , "</b>") } else { document.write ("Bugün günlerden pazar olmadığına göre tatil gününde değiliz !" ,"<br>") document.write ("İyi çalışmalar..") } //saklamayı bitir--> </script> </body> </html> |
| --- |

**Döngü Yapısı**

Javascript'te diğer programlama dillerinde olduğu gibi istediğiniz işlemi 2 veya daha fazla kez yaptırmak için belli program kodları mevcuttur. Bu diğer dillere çok benzer olan for döngü komutudur. Bu komutun yaptığı işlem , istenilen fonksiyon veya fonksiyon parçalarını istenilen değerde tekrar etmektir. Şimdi ayrıntılara geçelim.

| for ( değişken\_başlangıç\_değerler1 , değişken\_başlangıç\_değeri2 ; döngü sayısı ; değişecek\_değişken\_adı\_ve\_türü ) { yapılması istenen işlemler } |
| --- |

Burada parantezler içerisinde verilen değişken\_başlangıç\_değerler kısmı ve değişecek\_değişken\_adı\_ve\_türü kısmını yazmanız gerekmez. Döngü içerisinde kullanılan değişken daha sonra da istenilen şekilde arttırılabilir veya azaltılabilir. Yapı gözünüzü korkutmasın hemen bir örnekle daha iyi anlayalım.

| for (a=0 , b=0 ; c<=3 ; c++) { yapılması istenen işlemler } for ifadesi için kısa yazılım : var a,b=0; for (;c<=3;c++) { yapılması istenen işlemler } |
| --- |

Varsalım ki elimizde bir çarpım tablosu yapmak istiyoruz. Buna göre 5 sayısı için 1'den 10'a kadar sayıları bir tablo içerisinde vereceğiz. Şimdi bu durumda for döngüsüz 10 adet tablo yazmamız gerekecekti fakat biz for döngüsü ile işlemi 1 satıra indirgeyeceğiz.

| <html> <head> <title>for döngüsü</title> </head> <body> <script language="JavaScript"> <!-- //eski sürüm tarayıcılardan kodumuzu saklayalım var cevap=0; for ( sayi=0 ; sayi>=10 ;); { sayi--; var cevap = 5 \* sayi ; document.write( "5 \* " , sayi , " =" , cevap ,"<br>") } //saklamayı bitir--> </script> </body> </html> |
| --- |

Şimdi de for döngüsünün yapmak istediğimiz işlemlerde yetersiz kaldığı durumlarda kullanabileceğimiz yapıları görelim.

**Şartlı döngü yapısı while**

Javascript kodu yazarken -programda bir önceki örnekte olduğu gibi- sayaç değişkeninin her değeri için istediğiniz işlemi yapmasını istemeyebilirsiniz. Bunun için while komutunu kullanırsınız ki bu Javascript'e "İstediğim işi şu şart sağlanıyorsa yap !" demiş olursunuz.

While döngüsünde for döngüsünden farklı olarak döngü içerisindeki değişkenlerin tanımlanması gerekir. Şimdi yazım kurallarına bir göz atalım.

| while ( döngü şartı ) { şart doğruysa yapılacak işlemler} şart doğru değilse yapılacak işlemler |
| --- |

**Do .. while yapısı**

Do ... while yapısı genel olarak bir döngünün yapısını eğer şart doğruysa tekrar et manasındadır. Yani do ile başlangıçta hiçbir koşul olmadan işlem yapılır. Daha sonra while şartı doğru ise tekrar do yapısında geri dönülür. Bunu bir örnek ile açıklamak gerekirse;

Örneğin bir ticari siteniz var. İnsanlar sizden gelip istedikleri ürünleri satın alıyorlar. Bir ürün için siparişlerini verdiler ve bizde bunun karşılığı olarak ücret + kargo + kdv miktarını hesapladık ve müşterimize dedik ki istediğiniz ürün şu fiyata şu gün elinizde olur. Bu hesaplamaların hepsini do yapısı ile yap dedik. Ve sonra sorduk daha başka ürünlerde almak istiyor musunuz ? İşte bu da while yapısı ile sorulur. Şayet cevap evet ise do yapısı tekrarlanır değilse do döngü yapısında çıkılır.

Bizim kitap, cd ve kaset sattığımız varsayalım. Bizden de 2 kitap ve 3 cd aldığını varsayarsak;

var kitap=2000000; var cd=3000000; var kaset=1500000;
do {
var kitapistek =prompt ("Kaç tane kitap almak istiyorsunuz ?" , "lütfen rakam giriniz");
var cdistek= prompt ("Kaç tane cd almak istiyorsunuz ?" , "lütfen rakam giriniz");
var kasetistek= prompt ("Kaç tane kaset almak istiyorsunuz ?" , "lütfen rakam giriniz");
var kitaptutar=kitapistek\*2000000;
var cdtutar=cdistek\*3000000;
var kasettutar=kasetistek\*1500000;
var toplamtutar = kitaptutar+cdtutar+kasettutar;
document.write (kitapistek ," tane kitap ", cdistek ," tane cd " , kasetistek , " tane kaset siparişiniz alınmıştır ", "<br>");
document.write ("<br>" , "Aldığınız ürünlerin toplam tutarı = " ,toplamtutar);
var istek =prompt("Başka ürünlerde satın almak istiyor musunuz ?", "e veya h giriniz"); }
while (istek="e")
document.write ("<br>" ,"Bizden alışveriş yaptığınız için teşekkürler")

**Break ve Continue İfadeleri**

While komutu ile şartı belirledikten sonra yapılan işlemin kesilmesi veya devam etmesi otomatik hale gelmektedir. For döngüsü içerisinde de bu tür bir olayı break ve contine ifadeleri ile gerçekleştiririz.

Javascript break ifadesini gördüğü anda döngü işlemini keser ve bir sonraki komut satırını işleme koyar. Continue ifadesinde ise döngü break ifadesindeki gibi kesilir fakat işleme konulan satır bir sonraki satır değildir. Continue'de döngü başına dönülür.

| for () {işlem1; işlem2; break; } |
| --- |

Burada işlem2 ile verilen kısımda örnek olarak bir sorgu yapılabilir. Sorgu doğru ise break ifadesine gelinir ve burada döngü kesilir.

| for () { işlem1; işlem2; continue;} |
| --- |

Burada yine işlem2 ile sorgu yapılırsa contine ifadesi ile döngünün devamı sürdürülür.

**Önemli:** Break ve Continue ifadeleri her komutu kesmek veya devam ettirmek için kullanılamaz. Mesela bir if (Eğer) ifadesi şart doğru değilse break ile kes denilemez. Sadece döngü içerisinde döngünün kesilmesi veya devam ettirilmesi için kullanılabilir.

**Switch-Case İfadesi**

Bu ifade genel olarak menü kullanımında veya sorgu işlemlerinde işe yarar. Swicht ile ifade alınır case ifadesi ile işlemler sorgulanarak yapılır. Yazım kurallarına bir göz atalım.

| switch (parametreler) { case "ifade1" : case "ifade2" : ... } |
| --- |

Bir örnek verelim. Burada web sayfamızdaki herhangi bir işlemde çıkıp çıkmak isteyip istemediği soruluyor. Cevap evet ise işlem istenilen yönde yönlendiriliyor. Cevap hayır ise döngüden çıkılmaktadır. Burada kendimizi ziyaretçinin klavyesinde Caps Lock tuşuna basılı olup olmadığını önemsemiyoruz. Çünkü koşul ifademizi hem küçük harf hem de büyük harfe göre yazıyoruz.

| var sec; sec = prompt ("Çıkmak istiyor musunuz " ,"Evet için E veya e , Hayır için H veya h giriniz") switch (sec) { case "e" : case "E" : document.write ("Tekrar hoşgeldiniz") //yapılması istenen işlemler case "h": case "H" : document.write ("Bizi tercih ettiğiniz çin teşekkürler") break //Çıkılması istendiği için döngüyü kesmek için break komutunu kullanıyoruz. |
| --- |

**Fonksiyon Kavramı**

Çoğu zaman Javascript kodunuzda bir işlemin birden fazla yapılması gerekebilir. Hatta kimi zaman Javascript'e bir işlem yaptırmadan önce başka bir işlemi yaptırmak istenebilir.

İşte bu tür tekrarlanan işin yapılması için gerekli işlem ve komut gruplarına Fonksiyon adı verilir. Fonksiyonlar genelde , filanca isimli gruptaki işlemleri yap oradan bir değer al bunu filanca isimli gruba götür gibi işlemler için kullanılır. Bu tür komut sistemleri Javascript'te en çok kullanılan komut türlerindendir. Fonksiyonun yazım kuralları şu şekildedir:

| function fonksiyon\_ismi (parametre1 , parametre2 , .... ) { yapılması istenen işlemler } |
| --- |

**Fonksiyona Değer Gönderme ve Değer Alma**

Bir fonksiyonun Javascript içerisindeki ilk önemli görevi diğer fonksiyonlardan veya herhangi bir yerden bir değer alıp onu kendi içerisinde işletip sonra istenilen fonksiyona veya yere göndermektir.

Mesela herhangi bir muhasebe işleminin yapılıp bize geri gönderilmesini istediğimiz düşünelim. Genel yapı olarak kodumuz şu şekilde olacaktır.

Veri1 ve Veri2'nin işleme konulacağı fonksiyonların tanımlanması

Veri1'in alınması

Veri2'in alınması

Veri1'in fonksiyona gönderilmesi

Veri2'nin fonksiyona gönderilmesi

Alınan verilerin ekrana yazdırılması

Şimdi bu genel kodu Javascript'te nasıl yapacağımızı görelim :

| <html> <head> <script language="JavaScript"> <!-- //eski sürüm tarayıcılardan kodu gizleyelim function veri1(ilkveri) { var ilktoplam = (ilkveri \* 30 )/100 ; return ilktoplam ; } function veri2 (ikinciveri) { var ikincitoplam = (ikinciveri \* 45 )/100; return ikincitoplam; } -- > </script> </head> <body> <script language="JavaScript"> <!-- var data1 = prompt ("Birinci miktarı giriniz" ,"rakam gir"); var data2 = prompt ("İkinci miktarı giriniz" , "rakam gir"); document.write ("İlk işleminizin sonucu = " , veri1(data1) ); document.write ("İkinci işlemin sonucu = " , veri2(data2) ); -- > </script> </body> </html> |
| --- |

İlk satırların function tanımlama olduğunu görüyorsunuz. Burada veri1 , veri2 adlı iki tane fonksiyonu tanımladık. Diğer satırlarda prompt komutu ile klavyeden bilgi girişi sağladık. Daha sonra bu verileri fonksiyonlara göndererek istediğimiz işlemi yaptırdık ve daha sonrada bunu return yöntemiyle geri aldık. Bu kısma kadar yaptığımız fonksiyona bir değer göndermekti.

Yeniden bir bakış.veri1(data1) komutuyla prompt yoluyla aldığımız data1 değişkenini veri1 adlı fonksiyona gönderdik. Yani function veri1(ilkveri) şeklindeki fonksiyona biz data1 değişkenin gönderdik. Fonksiyon bu değeri yani data1 değişkenin aldığında otomatik olarak ilkveri değişkenine atadı. Böylelikle ilkveri=data1 oldu. Daha sonra istenilen işlemler yapıldı. Ve ardından return ilktoplam değeri geri gönderildi. Bu değer daha sonra ekrana yazdırıldı. Diğer veri2 adlı değişken için de aynı tür bir işlem sözkonusudur.

**Nesneler ve Özellikleri**

Günümüzde bilişim Teknolojileri ile ilgilene hemen herkesin duyduğu bir terim var. Nesneye Yönelik programlama. Nedir bu Nesneye Yönelik programlama ? Bu tip programlamada kullanılan her öğe bir nesne olarak kabul edilir. Bu nesnelerin özelliklerini kullanarak onları değiştirerek program yazılır. Javascript'te bu tür bir programlama dilidir. Örneğin webde sörf yaparken herkesin karşısına çıkan formlar birer nesnedir. Bu nesnelerin tepkiye göre cevap vermesi gibi özellikler de onun yani nesnenin özellikleridir.

Örneğin şimdiye kadar çoğu kez kullandığımız document.write komutu aslında bir nesnenin özelliğine atıfta bulunmaktan başka bir şey değildir. Yani document nesnesinin write özelliğini kullanarak html sayfamıza yazı yazdırıyoruz.

**Window Nesnesi**

Genel olarak pencere özellikleri ile ilgili bir nesnedir.

**Pencere açmak ve kapamak**

Birçok yerde gördüğünüz pencere açma pencerelerin çeşitli özelliklerini değiştirme işte bu nesne yardımıyla yapılmaktadır.

Şimdi bu nesneyi nasıl kontrol edeceğiz onu görelim.

Pencere açmak için:

| window.open("Url\_adı" , "pencere\_adı" , "pencere\_özellikleri"); |
| --- |

Pencere kapatmak için:

| window.close(); |
| --- |

Pencere kapatmak için window.close() komutu vermek yeterlidir. Burada kapatılan pencere ona kullanılmakta olan penceredir.

Gelelim pencere açma işine. Burada window.open ile pencerenin açılmak istendiği belirtilir. Parantez içerisinde verilenler ise açılması istenen pencerenin özelliklerini belirtir.

**Url\_adı:** Buraya yazılacak dosya ismi açılacak pencerenin içerisinde olacaktır.

| window.open("http://webteknikleri/owp/index.htm") |
| --- |

veya;

| window.open("index.html") |
| --- |

**Pencere\_adı:** Bu açılacak pencerenin adını belirtir. Birden çok pencere ile işlemler yapıyorsanız hangi pencereye bir komut gönderdiğinizin belli olması için gereklidir.

| Window.open("index.html" , "ana"); |
| --- |

**Pencere\_özellikleri:** Bu özellikte adından belli olduğu ölçüde pencerenin özellikleri ile ilgilidir. Bir pencerenin değiştirilebilir özellikleri şunlardır :

**menubar:** Tarayıcıların en üst kısmında bulunan File(Dosya) , Edit(Düzen) vb. menülerin bulunduğu satırdır.

**toolbar:** Tarayıcılarda üst kısımda Back(Geri) , Forward(İleri) vb. tuşların bulunduğu kısımdır.

**location:** Tarayıcılarda ziyaret etmek istediğiniz web adresini yazdığınız kısım.

**status:** Tarayıcıların en alt kısmında hangi dosyanın yüklendiği ile ilgili bilgi veren kısımdır.

**scrollbars:** Sağ tarafta bulunan sürgü çubuklarıdır.

**resizable:** Pencerenin boyutlarının kullanıcıya bırakılması veya kesin değerler almasıyla ilgilidir.

**width:** Açılacak olan pencerenin piksel cinsinden genişliğidir.

**height:** Açılacak olan pencerenin piksel cinsinden boyudur.

**left:** Açılacak olan pencerenin ekranın sol tarafından kaç piksel uzaklıkta olacağını belirler.

**top:** Açılacak olan pencerenin ekranın üstünden kaç piksel aşağıda olacağını belirler. Eğer pencere özellikleri kısmında değişmesini istemediğiniz bir özellik varsa onu yazmanıza gerek yoktur. Bu değerler tarayıcının banko(default) değerlerinden alınır.

Şimdi bir pencere açalım. Açtığımız pencerede dosya,düzen ve ileri,geri tuş takımı olmasın. Pencerenin boyutları 200x300 piksel olsun. Bizi www.webteknikleri.com adresine göndersin.

| window.open ("http://webteknikleri/owp/index.htm", "webteknikleri" ," menubar=no, toolbar=no, scrollbars=yes, location=yes, width=200, heigt=300";) |
| --- |

**window.location.protocol**

Window nesnesinin location.protocol nesnesi ise yüklenen dosyanın sabit diskten mi yoksa internetten mi yüklendiğini gösterir.

**http:** ile dosyanın internetten yüklendiğini belirtir.

**file:** ile dosyanın sabit diskten yüklendiğin belirtir.

Mesela şöyle bir örnekle dosyanın nerden yüklendiğini kontrol edelim.

| if (window.location.protocol == "http:" ) { document.write ("Bu belge Internet'ten geliyor.") } else { document.write ("Bu belge sabit diskten geliyor") } |
| --- |

**window.history.go**

Window'un history özelliği ile bir önceki sayfaya erişim sağlanabilir. Örneğin kullanıcı herhangi bir formu doldurmadı ve işlem yapılamadı bu durumda bir hata mesajı ile kullanıcıyı uyardıktan sonra history nesnenisin kullanarak bir önceki sayfaya kullanıcıyı gönderebilirsiniz. Bunun için gerekli kod yazımı şu şekildedir.

| Window.history.go(-1) |
| --- |

Bir önceki sayfaya -1 ile ulaşabilirsiniz. Bu değeri arttırarak daha önceki sayfalara da ulaşabilirsiniz.

**Status Bar kullanımı**

Status bar window nesnesinde belirttiğimiz gibi tarayıcıların en alt kısmında yer alan hangi dosyaya gidileceği veya yüklendiği ile ilgili bilgi veren kısımdır.

Status barı değiştirmek için şu kodları yazmalıyız.

| window.status="Webteknikleri'nden Merhaba !"; |
| --- |

Bu şekilde kullandığımız bir status kodu ile sayfa açık kaldığı sürece Webteknikleri'nden Merhaba ! yazısı karşımızda olacaktır.

**Tarayıcı Nesnesi**

Tarayıcılar Javascript tarafından bir nesne olarak algılanır. Bu nesnenin özelliklerini şöyle sıralayabilir.

**appname** Tarayıcı adı

**appVersion **Tarayıcının Versionu

**appCodeName** Tarayıcının kod adı

**userAgent** Tarayıcının anamakinaya(server) kendini tanıtırken verdiği isim

| <html> <head><title>Tarayıcı Özellikleri</title></head> <body> <script language="javascript1.2"> <!-- document.write("Şu anda kullandığınız tarayıcının özellikleri :" , "<br>"); document.write(navigator.appname + navigator.appVersion + navigator.appCodeName + navigator.useAgent ) ; --> </script> </body> </html> |
| --- |

**Çerçeve (Frame) Nesnesi**

Çerçeve tekniği bir web sayfası üzerinde birden fazla web sayfası görüntülenmek istendiğinde kullanılır. Daha ayrıntılı bilgi için HTML adlı bölümümüze bakınız.

Javascript açısından her bir çerçeve bir pencere sayılır. Bunların içeriğini kontrol etmek için belli komut stilleri vardır.

Şimdi onları görelim:

**Top:** En üst pencere (Yani tarayıcının kendisi)

**Parent:** Herhangi bir çerçeveyi oluşturan düzenleyici bölüm

**Self:** Çerçevenin kendisi

Javascript çerçeve düzenleyici(FrameSet)leri içerisindeki diğer alt çerçeveleri 0 'dan başlayarak numaralar. Bu numaralar yardımıyla çerçeve özelliklerini değiştirebiliriz. Örneğin iki tane çerçeveye sahip bir sayfada birinci çerçeve parent.frames\[0\] diğeri ise parent.frames\[1\] olarak adlandırılır. Örneğini verdiğimiz gibi iki çerçeveli bir web sayfamız olduğunu varsayalım.

Ana sayfamız ki bu sayfa tarayıcıya sayfanın iki html sayfasında oluştuğunu söyleyen , çerçeve düzenleyicisinin olduğu sayfanın kodları şu şekilde olsun.

**! Uyarı:** Bu sayfayı frame.html olarak kaydedin.

| <html> <head><title>Frame (Cerceve)</title></head> <!-- frames --> <frameset cols="50%,\*"> <frame name="sol" src="sol.html"> <frame name="sag" src="sag.html"> </frameset> </html> |
| --- |

Bu sayfayı sol.html olarak kaydedin.

| <html> <head><title>Sol Frame</title></head> <body> <script language="javascript1.2"> <!-- parent.frames\[0\].document.write("Herhangi bir hesaplama vb.unsur icin kullanilacak kod turu", "<br>" , "SOL taraf icin"); --> </script> </body> </html> |
| --- |

Bu sayfayı sag.html olarak kaydedin.

| <html> <head><title>Sag Frame</title></head> <body> <script language="javascript1.2"> <!-- parent.frames\[1\].document.write("Herhangi bir hesaplama vb.unsur icin kullanilacak kod turu", "<br>" , "SAG taraf icin" ); --> </script> </body> </html> |
| --- |

**Form Nesnesi**

Javscript açısından Html'in en önemli nesneleri Formlardır. Çünkü ziyaretçi ile etkileşmede en büyük unsurlardan birisi Formlardır. Html kendi form nesnesini kendisi oluşturabilir. Bu bakımdan Javascript'e düşen bir göre yoktur. Javascript form verilerinin yorumlanması ve işlenmesinde devreye girer. Şimdi form unsurlarını tanıyalım:

**Name :** Formun ismi

**Action :** Formun işleneceği perl veya cgi programının tanımlanacağı etiket

**Enctype :** Formun kodlanma türü

**Method :** Formun gönderme(post) mi yoksa alma(get) işlemi göreceğin belirler.

**Target :** Pencere ismi

**OnSubmit :** Gönderme metodunun ismi

Bunlardan yararlanarak bir form nesnesinin kodunu yazalım.

| <form name="mail" action="http://www.webteknikleri.com/cgi-bin/mail.pl" method="POST"> Form unsurları </form> |
| --- |

Şimdi biz bu kodda "Form Unsurları" diye bir şeyden söz ettik. Bu form unsurları ziyaretçiden nasıl bilgi alınacağını belirleyen unsurlardır. Bunlar bir metin alanı veya aşağı düşmeli bir menü olabilir. Form etiketi içerisindeki tüm unsurlar element adlı dizi-değişken içerisine yazılırlar ve form unsurları kullanılırken bu tip bir atıfta bulunmanız gerekir.

**Text Alanı**

Text alanı form unsurlarının en önemlilerindendir. Ziyaretçilerden bilgi almak amacıyla kullanılır. Kullanımı şu şekildedir.

| <input type="text"> |
| --- |

Şeklinde kullanılır. Bu nesnenin kullanılan etiketleri :

**Name :** text alanının ismi

**Size :** text alanının web sayfasında görülecek kısmının büyüklüğü

**Maxlenght :** text alanına en fazla kaç karakter girilebileceğini belirler.

İşte bir tam teşekküllü text alanı:

| <form name="mail" action="http://www.webteknikleri.com/cgi-bin/mail.cgi" method = POST> <input type="text" name="email" size=15 maxlenght=40> </form> |
| --- |

Buraya kadar işimizi Html ile hallettik. Şimdi bu form nesnesinin özelliklerini Javascript aracılığıyla nasıl değiştirilebileceğini görelim. document.form\_ismi.elements\[numara\]. değiştirilmek\_istenen özellik. numara : değiştirilmek istenen elemanın numarasıdır

Değiştirilmek istenen özellikler şunlar olabilir. value : içerisindeki değer

**Length :** nesnenin uzunluğu

**Name :** ismi

Şimdi bir örnek verelim.(bu örnek bir önceki form içindir)

| document.mail.elements\[0\].lenght=20 |
| --- |

**Şifre Alanı**

Bu alanlar şifreli bilgi almak için kullanılır. Bu alana bir bilgi girildiğinde karakterler gözükmez onun yerine asteriks \* işareti görülür.

| <form action="http://" name="mail"> <input type="Password" name="sifre" > </form> |
| --- |

Bu tür form unsurlarına erişimde text alanı gibi aynı şekildedir.

**Butonlar**

Form unsuru olarak iki tür buton vardır. Bunlar form unsurlarını form görevine göre göndermeye veya almaya yönelik Gönder (Submit) düğmesi bir diğeri ise Form unsurlarının tümünün ilk halini almasını sağlayan Sil (Reset) düğmesidir. Şimdi bunların nasıl kullanıldıklarını görelim.

| <form action="http://" name="mail"> <input type="Submit" name="gonder" value="GONDER"><br> <input type="Reset" name="sil" value="SIL"> </form> |
| --- |

**Radyo (Radio) Düğmeleri**

Bu tür düğmelerin en büyük özelliği radyo düğmeleri gibi olmasıdır. Yani herhangi bir menü üzerinde sadece bir seçim yaptırmak istiyorsanız bu tür form öğelerini kullanırsınız. Şimdi bunun ile ilgili bir örnek yapalım.

| <HTML> <HEAD> <TITLE>Radio</TITLE> <SCRIPT LANGUAGE = "JavaScript1.2"> function sorgu (secim) {var deger = null for (var i=0; i<secim.length; i++) {if (secim\[i\].checked) { deger = secim\[i\].value break } } return deger } </SCRIPT> </HEAD> <BODY> <FORM name="form1"> <p> <input type=radio name="firma" value="Bilemediniz Yazilim">Microsoft</p> <p><input type=radio name="firma" value="Bilemediniz Yazilim">Borland</p> <p><input type=radio name="firma" value="BilemedinizYazilim">Adobe</p> <p><input type=radio name="firma" value="Tebrikler Bildiniz">Copmaq</p> <input type=button value="Bunlardan hangisi bilgisayar ureticisidir" onClick="alert(sorgu(this.form.firma))"> </FORM> </BODY> </HTML> |
| --- |

Gördüğünüz gibi bu form unsuruna da(öğesi) diğer form unsurları gibi aynı şekilde ulaşılır. Fakat diğerlerinden farklı olarak burada checked(seçilmiş) yardımcı etiketini kullandık. Burada Javascript ile bir döngü oluşturarak hangi nesnenin seçili(checked) olduğunu kontrol ediyoruz. Ve alert ile sorulan sorunun cevabının doğruluğunu ziyretçiye bildiriyoruz.

**Select Unsuru**

Select öğesi form nesnelerimizden menü yoluyla ziyaretçi ile etkileşme yollarından bir tanesidir. Bu bir tür seçme kutusudur. Aşağı düşmeli kutu sayesinde kutu içerisindekilerden birisini seçebilirsiniz. Name , Multiple ve Size özelliklerine sahiptir. Bu nesnemizde nesnenin yönelendirilmesi açısından onBlur , OnFocus , OnChange özellikleri kullanılabilir. Nesnenin özelliklerine ulaşım için en çok kullanılan etiket yardımcısı ise value(değer) dır.

Radyo kutularında yaptığımız örneği şimdide Select öğesine uygulayalım.

| <HTML> <HEAD> <title>Select</title> <SCRIPT LANGUAGE = "JavaScript1.2"> function secim(secilen) { return secilen.options\[secilen.selectedIndex\].value } </SCRIPT> </HEAD> <BODY> <FORM name="soru"> <p><SELECT NAME="firma"> <OPTION value="Bilemediniz Yazilim">Microsoft</OPTION> <OPTION value="Bilemediniz Yazilim">Borland</OPTION> <OPTION value="Bilemediniz Yazilim">Adobe</OPTION></P> <OPTION value="Tebrikler Bildiniz">Compaq</OPTION></P><br> <input type=button value="Bunlardan hangisi bilgisayar ureticisidir" onClick="alert(secim(this.form.firma))"> </FORM> </BODY> </HTML> |
| --- |

**Olaylar**

Ziyaretçiye sunulan bir web sayfası üzerinde ziyaretçinin yaptığı her tür hareket bir bağlantıyı tıklaması, bir resmin üzerine gelmesi, resmin üzerinde ayrılması, bir formu yanlış doldurup hataya yol açması hep bir olaydır.

**onClick**

Web sayfası üzerinde bir nesnenin mouse ile üzerine tıklanması sonucu onClick olayı gerçekleşir. Olayın gerçekleşmesi için mouse'un nesneyi tıklayıp bırakması gereklidir. Yani mouse tuşuna basıldığında onClick olayı gerçekleşmiş olmaz. onClick olayı tuşa basılıp bırakıldıktan sonra gerçekleşir. Bağlantılar, resimler, form düğmeleri tıklanabilecek nesneler arasındadır.

OnClick yönlendiricisine bu durumda ne yapacağını Html etiketleri arasında bildirmeniz gerekir. Şimdi bunu bir örnekle açıklayalım.

| <html> <head><title>onClick</title> <script language="javascript1.2"> <!-- function merhaba() {alert ("beni tikladiniz"); } --> </script></head> <body> <input type="button" name="tikla" value="tikla" onClick=merhaba()> </body> </html> |
| --- |

Burada yaptığımız işlem html etiketleri arasında yer verdiğimiz bir butona tıklama (onClick) ile ne yapacağını merhaba fonksiyonuna git diyoruz. Fonksiyonda ekrana bir uyarı ile beni tıkladınız diye bir uyarı mesajı geçiyor.

Şimdi burada alert nesnesini de görmüş olduk. Alert nesnesi ziyaretçiye herhangi bir durumda uyarı vermek amacıyla kullanılır. Görüldüğü üzere parantez içerisinde çift tırnak içine uyarı yazısı yazılır.

OnDblClick olayı da onClick olayı ile yapı olarak aynıdır. onClick'ten farkı nesneye çift tıklandığında çalışmasıdır. Diğer yöntemler onClick ile aynıdır.

**onMouseOver , onMouseOut**

Bu tür nesne olayları ingilizce adı (onMouseOver = mouse işaretçisi(imleç) üzerindeyken , onMouseOut = mouse işaretçisi üzerinden ayrıldığında) üzerinde olmakla birlikte mouse'un nesnenin üzerinde olup olmadığı ile ilgilenir.

Bir örnek ile açıklayalım:

| <html> <head><title>onMouseOver ve onMouseOut </title> <script language="javascript1.2"> <!-- function uzerinde() {window.status="Tıklayın ve Webteknikleri.com adresine gidin" } function disinda() {window.status="Webteknikleri.com baglantisina tıklayın" } --> </script></head> <body> <a href="http://www.webteknikleri/index.htm" onMouseOver = uzerinde() onMouseOut =disinda()> Webteknikleri.com </a> </body> </html> |
| --- |

onMouseOver ve onMouseOut metodu ile ilgili güzel bir örnek daha :

<html>
<head><title>OnMouseOver</title>
<script language="javascript1.2">
<!--
function altavista()
{document.web.mesaj.value="En unlu web motorlarindan biri" }
function altavistasil()
{ document.web.mesaj.value="" }
function yahoo()
{ document.web.mesaj.value="En unlulerden bir tane daha" }
function yahoosil()
{document.web.mesaj.value="" }
function hotbot()
{document.web.mesaj.value="Ve bir tanesi daha" }
function hotbotsil()
{document.web.mesaj.value="" }
-->
</script></head>
<body>
<a href="www.altavista.com" onMouseOver="altavista()" onMouseOut = "altavistasil()"> Altavista</a><br>
<a href="www.yahoo.com" onMouseOver="yahoo()" onMouseOut="yahoosil()">Yahoo</a><br>
<a href="www.hotbot.com" onMouseOver="hotbot()" onMouseOut="hotbotsil()">Hotbot</a><p>
<form name="web">
<input type="text" name="mesaj" size="50">
</form>
</body>
</html>

**onSubmit**

Web-de sörf yaparken çoğunlukla karşımıza çıkan formlar biz doldurduktan sonra sayfanın bağlı bulunduğu server (ana makine) ya gönderilir. Fakat biz bu onSubmit olayı ile form gönderilmeden önce formun düzgün doldurulup doldurulmadığını kontrol edebiliriz.

Bunu örnek bir kod ile açıklayalım. Html sayfamızda body etiketleri arasında doldurulmasını istediğimiz bir form var ve ona ilişkin kod başlangıcı ise şöyle :

| <form action="mail.pl" method="post" onSubmit="dogrula()"> |
| --- |

Bu satır ile formun gönderilmesiyle (onSubmit) dogrula fonksiyonunu çağırıyoruz.

“dogrula” fonksiyonu da şu şekilde olabilir.(Bu fonksiyon head etiketleri arasında olan script etiketleri arasında olmalıdır.)

| function dogrula() { confirm ("Formu düzgün doldurduysanız OK'i tıklayınız'); } |
| --- |

Bu fonksiyonda kullandığımız confirm nesnesi ile kullanıcıya OK ve Cancel tuşları ile emin misin ? Gönderiyorum denilmektedir.

**onReset**

Bu olay ile web sayfanızda bulunan formdaki yazdıklarınızın tamamen silinir. Yani yazdığınızın yanlış olduğunu farkettiniz bu durumda Sil (Reset) tuşunu tıklarsınız ve size boş bir form gelir. Yalnız burada birşeyi belirtmek isterim. Reset(Sil) tuşuna tıkladıktan sonra tarayıcının back(geri) düğmesini tıkladığınızda formunuzda yazdıklarınız tekrar geri gelmez. Fakat siz onReset olayı ile bu durum için son bir ziyaretçiye seçenek sunabilirsiniz.

| <html> <head><title>onReset</title> <script language="javascript1.2"> <!-- function sil() { return confirm('Silmek istediginize emin misiniz?'); } --> </script> </head> <body> <form onReset="return sil()"> <input type="text" name="mail"> <input type="reset" value="sil"> </form> </body> </html> |
| --- |

**onChange**

Web sayfası üzerinde ziyaretçinin değiştirebileceği üç tür alan vardır. Bunlar text (metin) textarea (geniş metin alanı) select (seçim alanı) dır. Mouse u bu alanlar üzerine getirip tıkladığınızda onChange(değişti) olayını gerçekleştirmiş olursunuz. Şimdi bunu select yöntemi ile nasıl olduğunu görelim. Örneğimizde aşağı düşmeli bir menü tasarlayacağız ve şeçili durumda olan web sayfasına gönderme yapacağız.

| <html> <head><title>OnChange</title> <script language="javascript1.2"> <!-- function degisti() { window.open("www.altavista.com"); } --> </script> </head> <body> <form method="post"> <p><select name="degistir" size="1" onChange="degisti()"> <option>Adresi tikla <option>Altavista </select> </form> </body> </html> |
| --- |

**onLoad , onUnLoad**

Bu olaylar bize sayfanın yüklenmeye başlamasında (onLoad) sayfadan ayrılıncaya (onUnLoad) kadar olan yapılacak işlemler için gereklidir. Bir Javascript fonksiyonun web sayfası yüklenmeye başladığında otomatik olarak çalışmasını istiyorsak onLoad olayını kullanırız. Eski DOS'çular bilirler Autoexec.bat dosyası nasıl makine açıldığında yapılmak istenenleri yapıyorsa onLoad olayında da sayfa yüklenmeye başladığında nelerin otomatik olarak başlatılacağını belirleyebiliriz. Mesela sayfa yüklenmeye başladığında (onLoad) ziyaretçiye Web sitemiz hoş geldiniz diyebiliriz. Sayfadan ayrıldığında (onUnLoad) ise İyi sörfler diyebiliriz. Örnek kodlara geçmeden önce şunu belirtmekte yarar var. Bildiğiniz üzere web sayfası kod açısında iki kısıma ayrılır. Bunlar head ve body kısmıdır. Tarayıcı açısında body kısmı asıl kısımdır. Head kısmında sayanın nasıl görüntüleneceği gibi bölümler yer alır. Bu yüzden onLoad ve onUnload kısmı body etiketleri arasında yer alır.

Şimdi de bunun için gerekli kodlara bir göz atalım.

| <html> <head> <title>onLoad onUnLoad</title> <script language="javascript1.2"> <!-- function hosgeldiniz() { alert("Web Sitemize Hosgeldiniz") } function gulegule() { alert("Iyi sorfler..") } --> </script> </head> <body onLoad="hosgeldiniz()" onUnload="gulegule()"> </body> </html> |
| --- |

**onError onAbort**

Ziyaretçi sayfayı herhangi bir neden yüzünden tam haliyle yükleyememiş olabilir. Bu nedenler aktarım hızı veya tarayıcının Javascript kodunu tam manasıyla yorumlayamamış olmasıdır. İşte bu durumda Error(hata) oluşur. Html üzerinde oluşan en sık error(hata) resim haritalarının (image-map) tam anlamıyla yüklenmemesinden kaynaklanır. Çünkü bu durumda resim tam yüklenmemiştir. Bu da ziyaretçinin resim üzerinde tıklayacağı yerlerin yorumlanmamasını doğurur.

| <img src="resim.gif" onError="alert("Resim dosyası tam olarak yüklenemedi')"> |
| --- |

Ziyaretçi resimlerin yüklenmesi çok uzun sürüp yüklemeyi stop(dur) tuşu ile kestiyse bu durumda onAbort olayı gerçekleşir. Bunun sonucu olarak ziyaretçiye bir hata mesajı verebilirsiniz. Bu durum daha önce bahsettiğimiz image-map ler içindir.

| <img src="resim.gif" onAbort="alert("Resim harita dosyası tam olarak yüklenemedi. İlgili resim bir harita olduğu için yüklenmesini tavsiye ederiz.')"> |
| --- |

**Javascript ile DHTML**

Bu kısımda Javascript ile Katman(layer) özelliklerinin nasıl değiştirilebileceğini göreceğiz. Javascript bize Html sayfamızı oluşturan önemli unsurlardan biri olan layer(katman) ların tüm özelliklerini değiştirmemize olanak sağlar. Ayrıca hemen her yerde gördüğünüz resim değiştirme tekniğini de göreceğiz.

**Katman Özelliklerini Değiştirme**

İşe katman nedir sorusuyla başlayalım. Katman adı üzerinde sayfamızın üzerinde ne sayfadan bağımsız ne de her yönüyle sayfamıza bağlı bir unsurdur. Katman kullanarak istediğimiz herhangi bir yapıyı (yazı,resim,video,form) sayfamızın istediğimiz yerine koordinatları vermek koşulu ile yerleştirebiliriz. Zaten katmanın kullanım alanı en çok budur. Şimdi bir katman oluşturalım ve değiştirilebilir özelliklerini görelim.

| <html> <head><title>Layer</title></head> <body> <div id="denem" style="position:absolute ; left:100px ; top:200px; width:300px ; height:400px ; visibility:visible" > Su anda bir katman(layer)in icerisindeyim </div> </body> </html> |
| --- |

Layer oluşturmak istediğinizde **<div>** etiketi ile başlar **</div>** etiketi ile kodunuz tamamlarsınız. Şimdi katman özelliklerine geçelim :

**id :** Katmanın ismi

**style :** Katmanın özelliklerini belirtmek için

**absolute :** Katmanın koordinatlarının kesin olacağını belirler

**left :** Katmanın soldan kaç piksel sonra başlayacağını belirler

**top :** Katmanın üstten kaç piksel sonra başlayacağını belirler

**width :** Katmanın kaç piksel genişliğinde olacağını belirler

**height :** Katmanın kaç piksel boyunda olacağını belirler

**visibility :** Katmanın görünür mü görünmez mi olacağını belirler

Şimdi de Javascript komutlarıyla bu özelliklerin nasıl değiştirildiğini görelim.

Fakat burada karşımıza bir sorun çıkmakta. Internet Explorer ve Netscape tarayıcılarının doküman nesne modelleri farklı olduğundan katmana ulaşma teknikleri de farklıdır. Internet Explorer kod tekniği;

**katman\_adı.style.değiştirilmesi\_istenen\_özellik=yeni\_değer; **

| deneme.style.left=50px; |
| --- |

Netscape Navigator kod tekniği:

**document.katman\_adı.değiştirilmesi\_istenen\_özellik=yeni\_değer;**

| document.deneme.left=50px; |
| --- |

Şimdi bir örnekle bir katmanın yerinin nasıl değiştirilebileceğini görelim.

| <html> <head><title>Katman</title> <script language="javascript1.2"> <!-- function tara() { var tarayici= navigator.appName if (tarayici=="Netscape") degisim = document.katman; if (tarayici=="Microsoft Internet Explorer") degisim = katman.style; } function hareket1() { degisim.left=100 degisim.top=100 } function hareket2() { degisim.left=300 degisim.top=300 } --> </script></head> <body onLoad="tara()"> <div id="katman" style="position:absolute ; left:400px; top:10px"> Bu katmanin yeri degisecek </div> <p><p><p> <a href="javascript:hareket1()">Burayı tıklayın ve katmanınız 100x100'e gitsin</a><br> <a href="javascript:hareket2()">Burayi tıklayın ve katmanınız 300x300' gitsin</a> </body></html> |
| --- |

Buradaki örnekte olduğu gibi sizde katmanın diğer özelliklerini (width,height) değiştirebilirsiniz. Fakat görünebilirlik özelliği için özel bir durum vardır. Katman özelliklerine erişimde olduğu gibi bu özellikte de Internet Explorer ve Netscape Navigator farklılıkları vardır.

Internet Expolorer için Görünebilirlik özelliği

Katmanı görünebilir kılmak için:

katman\_adı.style.visibility="visible"

Katmanı gizleyebilmek için. katman\_adı.style.visibility="hidden"

Netscape Navigator için Görünebilirlik özelliği Katmanı görünebilir kılmak için:

document.katman\_adı.visibility="show"

Katmanı gizleyebilmek için:

document.katman\_adı.visibility="hide"

Şimdi de bununla ilgili bir örnek yapalım.

| <html> <head><title>Katman</title> <script language="javascript1.2"> <!-- function sakla() { var tarayici= navigator.appName if (tarayici=="Netscape") document.katman.visibility="hide" if (tarayici=="Microsoft Internet Explorer") katman.style.visibility="hidden" } function goster() { var tarayici= navigator.appName if (tarayici=="Netscape") document.katman.visibility="show" if (tarayici=="Microsoft Internet Explorer") katman.style.visibility="visible" } --> </script></head> <body> <div id="katman" style="position:absolute ; left:400px; top:10px"> Bu katmanin tikladiginizda yok olacak </div><p><p><p> <a href="javascript:sakla()">Burayi tiklayin ve katmaniniz yok olsun</a><br> <a href="javascript:goster()">Burayi tiklayin ve katmaniniz geri gelsin</a> </body></html> |
| --- |

Sizde bu tıklama özelliklerin değil de onMouseOver ve onMouseOut olay yönlendiricilerini kullanarak çok daha güzel şeyler üretebilirsiniz.

---
*Kaynak: `VERİ TABANI ÜZERİNE/VERİ TABANI ÜZERİNE.doc` — Baran Ertas — 2004*
