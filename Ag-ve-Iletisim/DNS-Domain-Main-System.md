# DNS - Domain Main System

**DNS, DOMAIN NAME SYSTEM (domain isim sistemi)
**

**DNS nedir?**

DNS,Domain Name System’in kısaltılmış şeklidir. Türkçe karşılığı ise Alan İsimlendirme Sistemi olarak bilinir.

DNS, 256 karaktere kadar büyüyebilen host isimlerini IP’ye çevirmek için kullanılan bir sistemdir. Host ismi,tümüyle tanımlanmış isim (full qualified name) olarak da bilinir ve hem bilgisayarın ismini hem de bilgisayarın bulunduğu Internet domainini gösterir. Örneğin murat.anadolu.com.tr ismi. Bu isimde “anadolu.com.tr” ifadesi internet domainini, “murat” ifadesi ise bu domaindeki tek bir makineyi belirtir. DNS , verilen bir makina adının IP adresini çözerek makinaların Internet üzerinde host isimleri ile haberleşmelerine olanak tanır.

**DNS’in amacı nedir?**

DNS, kolay anlaşılabilir ve kullanılabilir makine ve alan isimleri ile makine IP adresleri arasında çift taraflı dönüşümü sağlar. IP adreslerinin gündelik hayatta kullanımı ve hatırlanması pek pratik olmadığı için domain isimlendirme sistemi kullanılır.

Ana amacı, ağ uzerinden gelen alan adı veya IPnumarası ile ilgili sorgulamalara yanıt vermektir. Bu amaç için cok yaygın olarak "Berkeley Internet Name Domain (BIND)" yazılımı kullanılmaktadır. Siz bir siteye erişmek istediğinizde, DNS sayesinde hangi site nerde , hangi IP hangi bilğisayara ait olduğu belirlenir, ve istediğiniz yere erişirsiniz.

**DNS tarihçesi**

1984 yılına kadar DNS diye bir şey yoktu. O yıla kadar isim-IP çözümlemesi HOSTS adında bir metin dosyası ile yapılmaktaydı. Internetteki bilgisayarların isimleri ve IP adresleri bu dosyaya elle kaydediliyordu. Internetteki bilgisayarların herbirinde bu dosyanın bir kopyası bulunmaktaydı. Bir bilgisayar bir başka bilgisayara ulaşmak istediğinde bu dosyayı inceliyor,eğer dosyada o bilgisayarın kaydı bulunuyorsa IP adresini alıyor ve iletişime geçiyordu.

Bu sistemin iyi işleyebilmesi için HOSTS dosyası içeriğinin hep güncel kalması gerekiyordu. Bunu sağlamak için de dosyanın aslının saklandığı ABD’deki Stanford Universitesine belli aralıklarla bağlanarak kopyalama yapılıyordu.

Ama internetteki bilgisayarların sayısı arttıkça hem bu dosyanın büyüklüğü olağanüstü boyutlara ulaşmaya başladı,hemde internetteki bilgisayarların dosyayı kopyalamak için yaptığı bağlantı Standford’daki bilgisayarları kilitlemeye başladı.

Tek bir HOSTS dosyası kullanmanın başka bir kötülüğü de şuydu: bütün bilgisayarlar aynı düzeyde yer aldığı için bir bilgisayar isminin bütün internette bir eşinin daha bulunmamasını sağlamak gerekiyordu.

Bu sorunlar yüzünden internet yetkili organları 1984 yılında DNS’i ürettiler.DNS hem bilgisayar veri tabanını dağıtık bir yapıya sokuyor,hemde bilgisayarlar arasında hiyerarşik bir yapı kurulmasını sağlıyordu.

DNS’de dağıtık veri tabanı şöyle sağlanıyordu. Bilgisayarlar bulundukları yerlere,ait oldukları kurumlara göre sınıflandırılıyorlardı. Örneğin türkiyedeki bilgisayarların listesini(.tr domaini) türkiye’den sorumlu bir DNS sunucu makine tutuyordu.böylece internet ortamındaki bütün bilgisayarların bilgisinin tek bir yerde tutulması zorunluluğu kalmıyordu.

**DNS’in yapısı**

DNS sistemi isim sunucuları ve çözümleyicilerinden oluşur. İsim sunucuları olarak düzenlenen bilgisayarlar host isimlerine karşılık gelen IP adresi bilgilerini tutarlar. Çözümleyiciler ise DNS istemcilerdir. DNS istemcilerde, DNS sunucu yada sunucuların adresleri bulunur.

Bir DNS istemci bir bilgisayarın ismine karşılık IP adresini bulmak istediği zaman isim sunucuya başvurur. İsim sunucu, yani DNS sunucu da eğer kendi veritabanında öyle bir isim varsa, bu isme karşılık gelen IP adresini istemciye gönderir.

DNS veritabanına kayıtların elle,tek tek girilmesi gerekir.

Internet adresleri ilkönce ülkelere göre ayrılır. Adreslerin sonundaki tr, de , uk gibi ifadeler adresin bulunduğu ülkeyi gösterir. Örneğin tr Türkiyeyi, de Almanyayı, uk İngiltereyi gösterir. ABD adresleri için bir ülke takısı kullanılmaz çünkü DNS ve benzeri uygulamaları yaratan ülke ABD’dir.

Internet adresleri ülkelere ayrılıdıktan sonra com, edu, gov gibi daha alt bölümlere ayrılır. Bu ifadeler DNS’de üst düzey (top-level) domainlere karşılık gelir. Üst düzey doainler aşağıdaki gibidir:

**Com** :Ticari kuruluşları gösterir.

**Edu **:Eğitim kurumlarını gösterir.

**Org **:Ticari olmayan, hükümete de bağlı bulunmayan kurumları gösterir.

**Net **:Internet omurgası işlevini üstlenen ağları gösterir.

**Gov **:Hükümete bağlı kurumları gösterir.

**Mil **:Askeri kurumları gösterir.

**Num **:Telefon numaralarını bulabileceğiniz yerleri gösterir.

**Arpa **:Ters DNS sorgulaması yapılabilecek yerleri gösterir.

Alan isimleri, agaç yapısı denilen ve belli bir kurala göre dallanan bir yapıda kullanılmaktadır.

Amerika haricinde, internete baglı olan tüm ülkelerdeki adresler, o ülkenin ISO3166 ülkekodu ile bitmektedir. Türkiye'deki tüm alt alan adresleri, .tr ile bitmektedir. Örneğin;

marine.ulakbim.gov.tr adresinde;

tr Türkiye'yi,

gov alt alanın devlet kurumu olduğunu,

ulakbim bu devlet kurumunu,

marine bu kurumda bulunan bir makineyi göstermektedir.

**Yetki Bölgesi (Zone of Authority)**

Yetki bölgesi DNS sisteminde belli bir adres aralığıdır. Örneğin, yukarıda verdiğimiz örnekte murat.anadolu.com.tr , bir yetki bölgesini gösterir.

Her yetki bölgesinden sorumlu bir isim sunucusu, yani DNS sunucusu vardır. DNS sunucu yetkili olduğu bölgedeki bilgisayarların isimlerini IP adreslerini içerir. Aynı zamanda bu bölgeye dair sorgulamalara da yanıt verir.

DNS sunucunun yetki bölgesi en az bir tane domain içerir. Bu domain bölgenin kök domaini olarak adlandırılır. Yetki bölgesinde kök domainin altında bir veya birden fazla alt domain içerebilir. Bir DNS sunucu birden fazla bölgeyi yönetebilir.

**DNS sunucu çeşitleri**

Çalışmalarına göre DNS sunucular üçe ayrılır.

*Birincil isim sunucu(Primary Name Server):* Bölgesiyle ilgili bilgileri kendisinde bulunan bölgeden (zone file) elde eder. Bu dosyaya bilgiler elle tek tek girilir.

*İkincil isim sunucu(secondary name server):* Bölgesiyle ilgili bilgileri bağlı bulunduğu bir DNS server’dan alır. Yani bilgileri bu sunucuya elle girmek gerekmez.

*Yalnızca-Kaşeleyen isim sunucu (caching-Only name server):* Kendisinde bölge bilgilerinin tutulduğu bir dosya bulunmaz. Bağlı bulunduğu sunucuya sorarak topladığı bilgileri hem istemcilere ulaştırır, hemde kaşesine koyar

**Birincil DNS Sunucu**

Birincil DNS sunucu yetkili olduğu bölge ile ilgili bilgileri kendi üzerinde bulunan bölge dosyasından (zone file) alır demiştik. O bölgede bulunan bilgisayarlara da DNS sunucu adresi olarak Birincil DNS sunucunun adresi verilir. Böylece isim/IP çözümlemesi yapan istemci bilgisayarlar Birincil DNS sunucuya başvururlar, isme karşılık IP adresi bilgisini ondan alırlar.

**İkincil DNS Sunucu**

Eğer ağımızda çok sayıda bilgisayar varsa bütün bilgisayarların tek bir DNS sunucuya gitmeleri sonucunda isim/IP çözümleme performansımız düşecektir. Bu durumda ikinci bir DNS sunucu kurup bilgileri ona da tek tek elle gireriz ve bilgisayarların yarısında DNS sunucu olarak bu bilgisayarı gösteririz. Ama ağımızda çok bilgisayar olduğu için ikinci DNS sunucuya bilgileri girmek büyük bir yük getirecektir. Üstelik işlerimiz ilk girişle bitmeyecek. Bir de her iki DNS sunucusunun bilgilerinin güncel kalmasını sağlamamız gerekecektir. İkinci DNS sunucuda burda bize kolaylık sağlar.

İkincil DNS sunucunun bilgilerini bağlı bulunduğu DNS sunucusundan alması “bölge bilgisi aktarımı”(zone transfer) olarak adlandırılır.

İkincil DNS sunucu hem yük dağıtımı yapmamızı hem de bir arıza durumunda sistemin ayakta kalmasını (isim/IP çözümlemesi yapılabilmesi) sağlar.

Her bölgenin bilgisi ayrı dosyalarda saklanır. Bu yüzden birincil, ikincil gibi gibi ayrımlar bölge temelinde yapılır. Yani bir DNS sunucu bir bölge için birincil DNS sunucu iken, başka bir bölge için ikincil DNS sunucu olabilir.

**Yalnızca-Kaşeleyen DNS sunucu**

İkincil DNS sunucu tek bir lokasyonda, hızlı bir ağ üzerinden birbirine bağlanmış çok sayıda bilgisayarın bulunduğu kurumlar için oldukça iyi bir çözümdür. Fakat kurumda çok sayıda bilgisayar bulunuyorsa birincil ile ikincil DNS sunucular arasındaki bölge bilgileri aktarımı büyük bir trafik üretecektir. Bunun çözümü için yalnızca-kaşeleyen DNS sunucu kurulmalıdır.yalnızca-kaşeleyen sunucuya bilgiler elle girilmez. İkinci lokasyondaki bilgisayarlara DNS sunucu olarak kendi lokasyonlarındaki yalnızca-kaşeleyen sunucunun adersi verilir.yalnıca-kaşeleyen DNS sunucuda birinci lokasyondaki birincil ya da ikincil DNS sunucunun adresi vardır.

Bir bilgisayar isim/IP çözümlemesi yapacağı zaman bu yalnızca-kaşeleyen DNS sunucuya gider. Yalnızca-kaşeleyen DNS sunucuda bir bilgi yoktur bu yuzden yalnızca-kaşeleyen DNS sunucu iki lokasyon arasındaki hatta çıkar, bağlı bulunduğu DNS sunucuya gider, sorgulamasını yapar, aldığı yanıtı da soru soran kendi lokasyonundaki bilgisayara iletir ve elde ettiği bilgiyi bir DNS kaşesinde saklar. Eğer aynı bilgiye belli bir zaman diliminde ikinci bir bilgisayar daha erişmek isterse artık aradaki hatta çıkmadan elimizdeki bilgiyi kullanırız.

**DNS dosyaları**

DNS için gerekli olan dosya türleri şunlardır:

**1-named.boot:** Bu dosya, DNS çalışmaya başladığında program tarafından okunan ilk

dosyadır.

**2-named.local:** Bu dosya, "loopback" denilen ve makinenin kendisini gösteren adresin

çözümlenmesi icin kullanılan bir dosyadır.

**3. named.ca:** En üst seviyede bulunan ve "root server (.)" denilen makinelerin adreslerini içerir.

**4. named.hosts:** Bu dosya, DNS çalıştıran bir alt alanda bulunan makinelerin adreslerinin yazıldığı yani sorumlu olduğunuz alanınızda çalısan tüm bilgisayarların adreslerinin tutuldugu dosyadır.

**5. named.reverse:** Bu dosya, yukarıda açıkladığımız named.hosts dosyasının içerdiği IP adreslerini makinelerin isimlerine çevirmek için kullanılır ve yapı olarak named.local dosyasına benzer.

**DNS'te kullanılan kaynak kodlar ve anlamları**

Standart DNS kaynak kodlarının yazım formatı şu şekildedir:

; \[isim\] \[ttl\] \[sınıf\] \[kod\] \[diger uygun tür - adres,açıklama vs.\]

\[isim/name\] : Sorumlu olunan alt alan ismini belirtir.

\[ttl\] : (Time To Live). Saniye olarak bellekte (cache) tutulacak olan bilginin süresi.

\[sinif/class\] : Kaydın sınıfını belirler. Diğer sınıflar olmasına rağmen DNS'te genelde IN kullanılır.

\[kod\] : Kaynak kodunun ne oldugunu gösterir. A,NS,MX,vs...

*A – Address* : Belli bir makinenin internet adresini bildirmek ve makine ismini IP adresine eslemek icin kullanılır.

*CNAME - Canonical Name* : Esas makine ismine ek olarak başka bir isim daha tanımlamak için kullanılır.

*HINFO - Host Information *: Bilgisayarın donanım ve işletim sistemi bilgilerini yazmak için kullanılır

*MX - Mail Exchanger* : Belli bir alan adına gelen e-postaların hangi makineye dağıtılacağını gösterir

*NS - Name Server:* Internet üzerindeki belli bir alandan sorumlu olan bilgisayarın adresini belirtir

*PTR – Pointer *: Bilgisayar IP adresini bilgisayar ismine eşlemek için kullanılır.

*SOA - Start of Authority* : SOA tanımı, internet üzerindeki bir alanın başlangıcını ve bu alandan sorumlu olunduğunu belirlemek için kullanılır.

*TXT - Text Data* : Açıklayıcı bilgi vermek amacıyla kullanılır

*WKS - Well Known Services* : Bilgisayar tarafindan sunulan servisler hakkında bilgi verme amacıyla kullanılır

**DNS dosyaları içinde kullanılan anahtar sözcükler**

*Directory:* Belirtilen dosyaların bulunacağı dizin burada verilir.

*Cache:* Cache dosyasını belirtir.

*Primary:* Ana sunucunun (Primary Name Server) adı burada verilir. Alana ait temel bilgiler burada bulunur ve program ilk olarak aramaya bu sunucudan başlar.

*Forwarders:**** ***Ana sunucuda makine bulunamazsa burada belirtilen sunucuda aramaya başlanır

*Serial:* Burada seri numarası bulunur ve bu numaranın dosyada yapılan her değişiklikten sonra bir artırılması gerekir.
*Refresh:* Burada, ayarlama yapılan dosyaların ne kadar sürede bir kendini yenilediği belirtilir.
*Retry:* Burada ne kadar sürede bir aramanın yeniden deneneceği belirtilir.
*Expire:* Ne kadar süre sonra aramanın sonlandırılacağı belirtilir.

*Ttl (Time-To-Live):* Belirtilen süre kadar cache tutulabileceğini belirtir. Burada süre verilmemişse SOA'daki değer kullanılır.
*Name :* Makine adı belirtilir.
*Data :* IP numarası belirtilir.

**Bir name server’ın görevi**

\*İsim/IP çözümlemesi yapmak

\*Yaptığı sorgulamaların sonuçlarını belli bir süre saklamak

\*Kendi domaini için isim/IP bilgilerini sunmak

**DNS sorgulaması**

Bilgisayar herhangi bir adres sorgusu yapmak istediğinde bu sorgusunu Lokal DNS’e gönderir(1). Lokal DNS ise bu adresi bularak isteğe cevap verir(2). Eğer Lokal DNS üzerinde bu bilgi yoksa sorgulama işleri aşağıdaki şekilde görüldüğü gibi ilerler.

Bilgisayar sorgusunu Lokal DNS’e gönderir(1). Lokal DNS bu isteği alır. Kendi verilerinde bu isteğin karşılığı bulunmadığı için kendisinin bir üst seviyesindeki yetkili root DNS makinasına bu isteği iletir(2). Root DNS aranılan adresten sorumlu olan sunucunun adresini yani uzaktaki DNS’in adresini Lokal DNS’e iletir(3). Lokal DNS aldığı bu adrese istenen sorguyu gönderir(4). Uzaktaki DNS istenen veriyi Lokal DNS’e gönderir(5). Lokal DNS ise aldığı veriyi sorgulama işleminin yapan ilk bilgisayara verir(6).

Aynı isteklerin bir yerde toplanması(cache) sorgulama işleminin hızını arttırır. Lokal sunucu aynı adrese bağlanmak isteyen başka bir bilgisayar için (2) ve (3).cü adımları atlayarak işlemi daha hızlı gerçekleştirir.

**Ters DNS Sorgulaması**

DNS sunucusu herzaman isim/IP çözümlemesi yapmaz. Eğer uygun bir şekilde kurulursaIP/isim çözümlemesi de yapabilir. Yani bir DNS sunucuya IP adresi verip, karşılığında isim de alabiliriz. Buna ters sorgulama (inverse query) denilir.

Ters sorgulamayı kolaylaştırmak için in-addr.arpa adında özel bir domain yaratılır. Bu domainde de isim/IP eşlemeleri bulunur ama IP adresleri soldan sağa doğru, isimler ise sağdan sola doğru özelleştikleri için bu domaindeki adreslerin oktetleri tersten yazılır.

In-addr.arpa domaini yaratıldıktan sonra işaretçi kayıtları (pointer records) denilen kayıtlar bu domaine eklenir. Örneğin, 195.142.78.98 adresine karşılık gelen bilgisayar ismini bulmak için DNS sunucuya 98.78.142.195.in-addr.arpa kayıtı sorulur.

**DNS Hizmetinin Kuruluşu**

Anadolu.com.tr gibi bir domain ismine sahip bir işletmenin DNS sunucusunu oluşturmak için izleyeceğimiz basamaklar şunlardır:

Öncelikle bu domain için C sınıfı adreslerin kullanıldığını varsayalım. C sınıfı adresimiz 195.194.34.0 olsun. Yani bu domaindeki adresler 195.194.34.1 ile 195.194.34.254 arasında yer alacaktır.

DNS hizmetini yüklemeden önce TCP/IP özelliklerinden DNS sayfasına gidip domain ismini girmemizde yarar vardır. DNS hizmeti de diğer ağ hizmetleri gibi Denetim Masasındaki Ağ uygulamasından yüklenir, ve sistem yeniden başlatılır.

Sistem açılınca Yönetimsel Araçlar menüsüne DNS yöneticisi şeklinde bir şık eklenir, DNS hizmeti buradan düzenlenir.

DNS yöneticisi bölümüne girip DNS menüsünden New Server şıkkından DNS sunucu ekleriz. Sonra bu sunucu altına yetkili olduğumuz bir bölge (zone) yaratırız. Bunun için eklediğimiz sunucu üzerinde iken DNS menüsünden Yeni Bölge(new zone) şıkkını tıklarız. Sunucumuzu birincil yada ikincil olarak tanımlarız. Biz yeni bir kurulum yaptığımız için birincil’i seceriz. Karşımıza Bölge İsmi(Zone Name) ve Bölge Dosyası(zone file) isminin sorulduğu bir kutu gelir. Zone name kısmına anadolu.com.tr yazıp TAB tuşuna bastığımız takdirde bilgisayar otomatik olarak zone file bölümünü anadolu.com.tr.dns olarak yazar. Bu bilgileri girdikten sonra işlem,i tamamlamak için finish tuşuna basarız.

Yeni oluşturduğumuz bölgede kendiliğinden yaratılmış kayıtlar vardır.bu kayıtların isimleri kayıt tipleri ve dataları yazılıdır.kayıt tipi bölümünde NS,SOA, ve A gibi ifadeler görürüz bu ifadeleri açıklamak gerekirse:

**NS,** bu satırdaki kayıtın isim çözümleyici (name server) bilgisayara ait olduğunu gösterir.

**SOA,** ise yetki bölgesi başlangıcı(start of authority) anlamına gelir ve DNS kuruluşu ile ilgili bilgiler içerir. Örneğin, kayıt sonunda eğer “administrator” ifadesi varsa bu ifade bölgeden sorumlu kişinin adını içerdiğini gösterir.

**A **kayıtı ise isim çözümleyici bilgisayarın, yani DNS sunucu bilgisayarın IP adresini verir.

Ters sorgulama yapacaksak bu aşamada ters sorgulama bölgesini (reserve look-up zone) de yaratmalıyız. Bunun için DNS New Zone şıkkını tıklarız. Yaratacağımız bölge yine birincil olmalıdır. Bölgenin ismi 1.107.195.in-addr.arpa şeklinde olacak. Bu ismin ilk kısmı bir IP adresine karşılık geliyor. İkinci kısım olan in-addr.arpa ise her ters sorgulama bölgesinin isminde bulunması gereken bir ifadedir. Girdiğimiz adres C sınıfı bir adres olduğu için de üç oktet kullandık. Böylece sonuncu oktet ne olursa olsun bize 195.107.1 ile başlayan bir adres sorulduğunda bu adrese karşılık gelen sorgulayabilecez.

PAGE

PAGE 1

---
*Kaynak: `DNS - DOMAIN MAIN SYSTEM/DNS - DOMAIN MAIN SYSTEM.doc` — MURAT — 2004*
