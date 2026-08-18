# ISA Hakkinda Herşey

**ISA HAKKINDA HERŞEY******

Ayhan ERGUN

ISA SERVER'I TANIMAK

-ISA Server'ın özelliklerini açıklamak.

-Caching, Firewall özelliklerini açıklamak.

I. GİRİŞ

ISA (Internet Security and Acceleration) Server 2000, özellikle Internet'e erişim için kendi networklerini genişleten şirketler için geliştirilmiştir. ISA Server, caching (ön belleğe alma) özelliğiyle özellikle kullanıcıların Web erişimini hızlandırır. Bunun dışında ISA Server, şirketin network kaynaklarını, network dışından gelecek yetkilendirilmemiş kullanıcılara karşı korumak için firewall görevi üstlenir.

A. ISA SERVER SÜRÜMLERI

ISA Server, ölçeğe göre iki ayrı sürüm olarak pazara sürülmüştür:

-ISA Server Standard Edition

-ISA Server Enterprise Edition

Standart sürüm, küçük şirketler için firewall ve Web caching hizmetleri sağlar.

Enterprise sürüm ise, standart sürümün özelliklerinin yanı sıra, özellikle daha fazla Internet trafiğini yönetmek ve performans sağlamak için geliştirilmiş bir üründür.

B. ISA SERVER'IN SAĞLADIĞI ŞEYLER

ISA Server şirketlere şu yararları sağlar:

• Hız (acceleration)

• Güvenlik (security)

• Yönetim

• Genişleme

ISA Server, caching olanağıyla Internet üzerindeki network trafiğini azaltır. Değişik katmanlarda network trafiğini izleyerek güvenliği sağlar. Güvenliği sağlamak için gelen ve giden network trafiğine filtre konur.

ISA Server, güvenlik ve caching özelliklerinin yanı sıra merkezi bir yönetim ve şirket ilkelerinin geliştirilmesini sağlar.

C. KURULUM MODLARI

ISA Server değişik modlarda kurulur:

• Cache mod

• Firewall mod

• Integrated mod

Cache mode Web erişimi hızlandıran bir moddur. Firewall ise güvenlik sağlar. Integrated modda ise her iki mod bir araya getirilebilir. Genellikle her iki mod bu Integrated mod ile bir araya getirilerek kolay yönetim sağlanır.

II. CACHİNG (ÖN BELLEĞE ALMAK)

Caching erişilen Web nesnelerinin ön bellekte tutulmasıyla network performansının artırılmasını sağlar. Caching işlemi Intranet ve Internet için kullanılabilir.

ISA Server değişik caching işlemlerini destekler:

• Forward caching.

• Reverse caching.

• Distributed caching.

Forward caching işlemi iç istemcilerin Internet üzerindeki adreslere erişmesini hızlandırır. Sık istenen nesneler merkezi bir ön bellekte tutulur ve diğer istemcilerin buradan erişmesi sağlanır.

Reverse caching işlemi ise, dış istemcilerin iç Web server üzerindeki kaynaklara erişmesini sağlar. Distributed caching işlemi ise birden çok ISA Server arasında yük dengelemesini sağlar.

III. FİREWALL

Firewall, donanım, yazılım ya da her ikisinin bileşimi olarak düzenlenen güvenlik sistemleridir. Firewall'lar network üzerindeki paketleri filtreleyerek özel networkleri izinsiz kullanıcıların erişiminden korur. Değişik türde firewall tasarımları vardır. Buların içinde three-homed firewall ya da back-to-back firewall gibi düzenlemeler vardır.

Firewall'lar iki amaca hizmet ederler:

Networke giren ve networkten çıkan bütün trafiği kontrol eder ve izinsiz kullanıcıları engellerler. Bunun dışında şirket için güvenlik ilkesi uygularlar.

ISA Server network trafiğinin kontrolü için şu işlemleri yapar:

• IP Paketlerinin Filtrelenmesi

• Uygulama Filtreleleri

• Kötü Niyetli Kişilerin Bulunması

Paket filtreleme network paketlerinin özelliklerine göre yapılır. Uygulama filtereleri ise belli bir tür veriye göre yapılır.

KURULUM

-ISA Server'ı kurmak.

-ISA Server Client'ı kurmak.

I. PLANLAMAK

Bu konuda ISA Server'ın planlanması ve dağıtılmasıyla ilgili konular yer almaktadır. Aşağıdaki tabloda ISA Server kurulumunda ve dağıtımında göz önünde bulundurulacak konular yer almaktadır:

Konu Açıklama

Gereksinim duyulan bilgisayar sayısı Donanım yapılandırması ve Internet bağlantısı.

Hangi ISA Server özelliklerine gereksinim duyacağız? Belli network özelliklerini karşılamak için belli ISA Server özelliklerini seçmek.

Kullanıcı gereksinimleri nelerdir? Kullanıcıların gereksinim duydukları uygulamaları ve servisleri belirlemek.

Var olan network üzerinde yeniden yapılandırma gerekecek mi? ISA Server'ın var olan network ile olan ilişkisini belirleyin.

A. KAPASİTE PLANLAMASI

Performans bakımından iyi sonuçlar almak için ISA Server donanımını ve Internet bağlantısını tahmin edilen yüke göre planlamak gerekir.

Minimum Gereksinim:

ISA Server'ı kullanmak için gerekenler:

-300 MHz (MHz) ya da daha yüksek bir Pentium II-compatible CPU.

-Microsoft Windows 2000 Server Service Pack 1 ya da daha yenisi, Windows 2000 Advanced Server Service Pack 1 ya da daha yenisi Windows 2000 Datacenter Server.

-256 MB RAM

-20 MB hard-disk space

-Windows 2000 network adapter

-Local hard-disk üzerinde bri NTFS disk bölümü (partition)

Uzaktan Yönetim Gereksinimleri:

Uzaktan yapılacak ISA Server yönetimi için yalnızca ISA Management'i kurmanız yeterlidir. Bu program Windows 2000 Professional ya da Windows 2000 Server üzerinde çalışabilir.

Ayrıca ISA Server'ı çalıştıran bilgisayar üzerinde Terminal Servislerini Remote Administration modunda kurabilirsiniz. Bu durumda diğer bir bilgisayara ISA Management araçlarını yüklemek zorunda kalmazsınız. Bunun yerine ISA Server'ı yönetmek için Terminal Services oturumunu kullanırsınız.

Forward Caching Gereksinimleri:

ISA Server bir forward caching server olarak kullanılabilir. Forward caching server, sık erişilen Internet nesnelerinin merkezi olarak saklanmasını (cache) sağlar. Bu durumda kaç tane Web tarayıcısının Internet'e erişeceğini belirleyin.

Aşağıdaki tabloda şirket içindeki kullanıcıların Internet'e erişimini en şekilde sağlamak için gereken donanım açıklanmaktadır:

Kullanıcı Sayısı ISA Server Bilgisayarı RAM Disk Alanı

-500 Tek bir Pentium II Bilgisayar 256 2-4 Gigabytes (GB)

500 – 1,000 Tek bir Pentium III ve 500 MHz

ya da daha hızlı bilgisayar. 256 10 GB

1,000 - İki tane Pentium III ve 500 MHz

ya da daha hızlı bilgisayar. 256 10 GB

B. ISA SERVER'IN ÖZELLİKLERİNİ SEÇMEK

ISA Server, firewall ve caching özellikleriyle kurulabilir. Yalnızca firewall ya da caching özellikleri kurulabilir. Kuruluş sırasında bu modlar seçilebilir:

-firewall,

-cache

-ya da integrated.

Firewall modunda network iletişimini kurallarla (rules) yapılandırarak korumak söz konusudur. Cache mod ise network performansını artırmayı amaçlar.

Integrated modda ise bütün cache ve firewall özellikleri kullanılabilir. Seçilen moda göre farklı özellikler seçilebilir. Aşağıdaki tablodaki özellikler firewall ve cache modları için geçerlidir. Integrted modda ise bütün özellikler kullanılabilir:

Özellik Firewall Cache

Access policy Yes Yes (HTTP ve HTTPS protokolları)

Application filters Yes No

Cache configuration No Yes

Firewall and SecureNAT client support Yes No

Packet filtering Yes No

Real-time monitoring Yes Yes

Reports Yes Yes

Server publishing Yes No

Virtual private networking Yes No

Web filters Yes Yes

Web publishing Yes Yes

Web Proxy client support Yes Yes

C. İSTEMCİ GEREKSİNİMLERİ

ISA Server aşağıdaki türde istemcileri destekler:

-Web Proxy clients: Bir Web Proxy istemcisi isteğini doğrudan ISA Server'a gönderir. Ancak Internet erişimi tarayıcıyla sınırlıdır. Web tarayıcısının Web Proxy olarak yapılandırılması gerekir.

-SecureNAT clients: Secure network address translation (SecureNAT) istemcileri ise güvenlik ve caching sağlarlar, ancak kullanıcı düzeyli authentication işlemine izin vermezler. Bir SecureNAT istemcisini yapılandırmak için istemci bilgisayarda ISA Server'ın IP adresi default gateway olarak düzenlenir.

-Firewall clients. Firewall istemcileri ise kullanıcı bazında bağlantıya sahip olurlar. a Firewall client yapılandırmak için Firewall client programının istemci bilgisayar üzerine kurulması gerekir. ISA Server Firewall client programı yalnızca Microsoft Windows Millennium Edition, Microsoft Windows 95 OSR2, Microsoft Windows 98, Windows NT 4.0 ve Windows 2000 bilgisayarlara yüklenir.

II. KURULUM

ISA Server CD'sinin takılmasıyla başlatılan kurulum aşamalarında şunlar göz önünde bulundurulur:

A. KURULUM MODUNUN SEÇİLMESİ

ISA Server kurulumuna başlamak için ISA Server CD'si bilgisyara takılır. Ardından Continue ile kuruluma başlanır. Lisans anlaşmasının ardından kurulum şekilleri seçilir:

-Typical Installation

-Full Installation

-Custom Installation

Yaygın olarak kullanılan ISA Server bileşenlerini kurmak için Typical kurulum seçilir.

Ardından kurulum modu seçilir:

-firewall,

-cache

-ya da integrated.

Eğer ISA Server'ı cache modda ya da Integrated modda kuracaksanız, kurulum programı cache için yerin düzenlendiği bir iletişim kutusunu kullanır. Bu işlem için NTFS ve yeterince yer olan bir disk seçilir.

Varsayılan cache büyüklüğü 100 MB'dır. Minimum cache büyüklüğü ise 5 MB dir.

B. LAT YAPILANDIRMASI

LAT (Local Address Table), iç IP adreslerinin bir tablosudur. ISA Server'ı firewall modda ya da Integrated modda kurulmuşsa, kurulum sırasında LAT'ı yapılandırabilirsiniz. ISA Server, LAT'ı şirket içindeki iç IP adreslerini tanımlamak için kullanır. Böylece ISA Server, LAT'ı kullanarak iç (internal) network içindeki bilgisayarların dış network üzerindeki bilgisayarlarla iletişim kurmasını sağlar.

Kurulum sırasında LAT'ı yapılandırmak için:

1. Kurulum sırasında Table'ı tıklayın.

2. Özel IP adresi aralığını girmek için Add address ranges based on the Windows 2000 Routing Table onay kutusunu seçin. Ardından iç (internal) network için olan netwotk kartı için olan onay kutusunu da işaretleyin.

3. Internal IP ranges kutusunda, IP adres aralıklarının listesini gözden geçirin ve gerekli düzeltmeleri yapın.

C. ISA CLİENT

ISA Server, daha önce de bahsettiğimiz gibi üç tür istemciyi (clients) destekler:

-Web Proxy clients

-SecureNAT clients

-Firewall clients

Hangi tür istemci kullanımına nasıl karar vereceğiz?

Yalnızca Web isteklerinin performansını artırmak için Web Proxy istemcisi kullanılır.

İstemci yazılımına gerek duyulmadan ISA Server'a erişmek için SecureNAT istemcileri kullanılır. Ancak şirketlerde daha çok Firewall istemcileri kullanılır. Çünkü Firewall istemcileri Internet erişiminin yalnızca kimlik denetim yapılmış (authenticated) kullanıcılar tarafından yapılmasına izin verir.

Ayrıca Firewall istemciler, kullanıcı bazında ilke (policy) düzenlemesinin yapılmasını sağlar.

Firewall Client Yazılımının Kurulması

ISA Server kurulumunun ardından MSPInt adlı bir dizin yaratılarak istemcinin buradan setup.exe programıyla kurulması sağlanır.

\\\\Server\\MSPInt dizinine geçin.

Buradaki Server, ISA Server'ın kurulduğu bilgisayarın adıdır.

Ardından Setup.exe programıyla istemci yazılımı kurulur.

D. MİCROSOFT PROXY SERVER 2.0'DAN YÜKSELTMEK

ISA Server Microsoft Proxy Server 2.0'dan full geçişi destekler. Diğer bir deyişle Proxy Server 2.0 kuralları (rules), network düzenlemeleri ve caching yapılandırması aynen benimsenir.

INTERNET ERİŞİMİNİ GÜVENLİ HALE GETİRMEK

-Policy ve Rule düzenlemelerini açıklamak.

-Policy oluşturmak.

I. ACCESS POLICY VE RULE

ISA Server, iç networkünüzü Internet'e bağlar. Ancak şirket içinden Internet'e erişim için verilen izin düzenlenmesi gerekir. Bu düzenlemeler Access Policy ve ilgili kuralların (rule) oluşturulmasıyla sağlanır.

ISA Server üzerinde düzenlenen Access Policy ve ilgili kurallar (rule), kullanıcıların belli bir protokole erişmesi için izin verilmesini ya da engellenmesini (deny) sağlar.

İPUCU: ISA Server kurulumunun ardından istemcilerin Internet erişimini sağlamak için bir kural (rule) tanımlayarak http protokolünü kullanıma açmanız gerekir.

A. ACCESS POLİCY BİLEŞENLERİ

Bir access policy (erişim ilkesi) şu bileşenlerden oluşur:

Protokol Kuralları

ISA Server istemcilerinin iç ve dış network ile iletişim kurmak için kullanabileceği protokolleri tanımlar.

Site ve İçerik Kuralları

İzin verilen ya da engellenen Web proxy istemcilerinin erişebileceği site ve içerikleri tanımlar.

Policy Elemanları

Kuralların bir kısmı olarak kullanılacak ayarlamaları tanımlar. İlkeler (policy) belli bir zamanlamayı ya da belli bir içeriği tanımlar.

B. BİR ERİŞİM İLKESİ (ACCESS POLİCY) PLANLAMAK

Bir erişim ilkesini oluşturmadan önce şirketinizin gereksinimlerini karşılayacak olan strateji geliştirmenizde yarar vardır. Bir erişim ilkesi geliştirmek için şu kriterleri göz önünde bulundurabilirsiniz:

-Şirketin gereksinimleri.

-Gerek duyulan kurallar.

-Kuralları tanımlamak için gereken ilkeler (policy).

C. PROTOKOL KURALLARI OLUŞTURMAK

Protokol kuralları, istemcilerin Internet'e erişmek için kullandıkları protokollardır. Örneğin http gibi.

Bir protokol kuralı yaratmak için şu adımları izleyin:

1. ISA Management programını başlatın.

2. Konsol ağacında Access Policy'ı genişletin.

3. Protocol Rules'ı ve ardından Create a Protocol Rule'ı tıklayın.

4. Rule Action sayfasında Allow ya da Deny tıklayarak kural işlemini tanımlayın.

5. Next'i tıklayın ve Protocols sayfasındaki seçeneklerden birisini tıklayın.

Seçenekler:

All IP traffic: Firewall istemciler için bütün IP trafiğine izin verilmesi ya da engellenmesi.

Selected protocols: Kuralın uygulanacağı bütün protkoller.

All IP traffic except selected: Kuralların uygulanmayacağı bütün protokoller.

6. Schedule sayfasında belli bir zaman planını seçin ve Next'i tıklayın.

7. Client Type sayfasında ise şu seçenekleri düzenleyebilirsiniz.

Seçenekler:

Specific computers (client address sets): Kuralların uygulanacağı istemci bilgisayarlar.

Specific users and groups: Kurallın uygulanacağı kullanıcı ve gruplar seçilir.

D. SİTE VE İÇERİK KURALLARI

Site ve içerik kuralları ise, kullanıcıların belli sitelere erişmesine izin verir.

Bir protokol kuralı yaratmak için şu adımları izleyin:

1. ISA Management programını başlatın.

2. Konsol ağacında Access Policy'ı genişletin.

3. Site and Content Rules'ı ve ardından Create a Site and Content Rule'ı tıklayın.

4. New Site and Content sihirbazında Site and Content rule name kutusunda kuralın adını yazın ve Next'i tıklayın.

5. Rule Action sayfasında Allow ya da Deny tıklayarak kural işlemini tanımlayın.

6. Destination Sets sayfasındaki seçenekleri tıklayın.

Seçenekler:

All destinations: Bir zaman planını seçin, ardından istemci türünü seçin.

All internal destinations: Bir zaman planını seçin, ardından istemci türünü seçin.

All external destinations: Bir zaman planını seçin, ardından istemci türünü seçin.

Specified destination set: Bir zaman planını seçin, ardından istemci türünü seçin.

E. POLİCY ELEMANLARI OLUŞTURMAK

ISA Server kurallarını oluşturmak için policy (ilke) bileşenlerine gerek duyulur. İlke elemanları kullanıcılar, yer ve bant genişliğinin kullanımı konusunda daha fazla kontrol sağlar.

ISA Server policy elemanları şunları içerir:

• Schedules (zaman planları)

• Bandwidth priorities (bant genişliği öncelikleri)

• Destinations Sets (hedef bilgisayarlar)

• Client address sets (istemci adresleri)

• Protocol definitions (protokol tanımlamaları)

• Content groups (içerik gruplamaları).

• Dial-up entries (çevirmeli bağlantılar).

CACHING'İ YAPILANDIRMAK
-Caching (önbellekleme) fonksiyonunun özelliklerini açıklamak.

-Caching ilkelerini yapılandırmak.

I. CACHING FONKSİYONLARI

ISA Server, Web nesnelerine hızlı ve etkin erişim sağlamak için çeşitli caching fonksiyonlarına sahiptir. ISA Server'ın cache performansını artırmak için yaptıklarında bazılarını şu şekilde açıklamak mümkündür:

RAM ve Disk Caching

Disk üzerinden erişilen nesneler için RAM (ana bellek) üzerinde alan ayırmak ve ardından onları disk üzerine kaydetmek.

Cache Edilen Nesnelerin Dizinini Oluşturmak

Cache edilen nesnelerin bir dizinini RAM üzerinde tutar.

ISA Server, caching fonksiyonları bu işlemlerin yanı sıra, bu işlemleri dinamik olarak günceller ve kullanılmayanları da silerek caching işlemini sürekli olarak güncel ve etkin tutmayı sağlar.

A. YENİ NESNELERE ERİŞMEK

Kullanıcı bir HTTP isteğinde bulunduğunda, Web Proxy istemcisi isteğini ISA Server üzerindeki Web Proxy servisine gönderir.

Web Proxy servisi isteği aldığında şu şekilde işler:

1. Web Proxy servisi cache dizinine bakar ve istenen nesnenin cache içinde bulunup bulunmadığını kontrol eder. Nesne cache içinde yer almıyorsa, nesne için cache içinde bir kayıt ayrılır.

2. Wep Proxy servisi nesneyi Internet üzerinde elde eder ve bir kopyasını RAM cache üzerine koyar.

3. Web Proxy servisi nesneyi istemciye döndürür. Bu arada Web Proxy servisi nesneyi disk cache içinde de saklar.

B. VAROLAN NESNELERE ERİŞMEK

Kullanıcı bir HTTP isteğinde bulunduğunda, Web Proxy istemcisi isteğini ISA Server üzerindeki Web Proxy servisine gönderir.

Web Proxy servisi cache dizinine bakar ve istenen nesnenin cache içinde bulunup bulunmadığını kontrol eder. Nesne cache içinde yer alıyorsa, nesne bir Internet trafiği oluşturmadan doğrudan istemciye ulaşır. Böylece hız artar.

II. CACHING İLKELERİNİ YAPILANDIRMAK

Bölümün önceki konusunda ISA Server'ın caching fonksiyonlarından söz ettik. Ancak, bu fonksiyonları ayarlamak için belli ilkeler (policy) kullanılabilir. Bu konuda bu ilkelere bakacağız:

A. HTTP CACHİNG'İ YAPILANDIRMAK

HTTP Caching işlemini etkinleştirdiğinizde, ISA Server'ın HTTP nesnelerini (Internet erişimi) cache içinde tutmasını sağlarsınız. ISA Server belirtilen bir süre kadar erişilen içeriği cache içinde tutar ve bir sonraki erişimin istemcilere hız sağlar.

Ancak, nesneler ne kadar süre cache içinde duracak?

Bir nesnenin cache içinde kaldığı süre TTL (Time to Live) olarak adlandırılır.

HTTP caching işlemini etkinleştirmek için:

1. ISA Management içinde, konsol ağacını açın.

2. Cache Configuration'ı tıklayın. Ardından ayrıntılar bölmesinde Configure Cache Policy'i tıklayın.

3. Cache Configuration Properties iletişim kutusunda HTTP sekmesinde Enable HTTP Caching onay kutusunu işaretleyin.

ISA Server, HTTP nesnelerinin cache içinde saklanması için önceden tanımlı düzenlemeler sağlar:

Frequently: Nesnelere Internet üzerinde sıklıkla erişim sağlar. Bant genişliği sınırı olmadığında tercih edilebilir.

Normally: Frequently ve Less Frequently seçeneklerinin arasında bir ayarlama. (Varsayılan ayar).

Less frequently: Nesnelere Internet üzerinde daha az sıklıkta erişilir. Bant genişliği sınırlı olduğunda tercih edilebilir.

B. FTP CACHİNG

Aynı şekilde, FTP trafiği içinde caching ayarlamaları yapılabilir.

III. CACHE BOYUTUNU AYARLAMAK

ISA Server, caching için .cdat dosyasını kullanır. ISA Server, nesneleri caching alanına attıkça bu dosyaya yerleştirilir. .cdat dosyası dolduğunda, ISA Server, eski nesneleri silerek yeni nesnelere yer açar.

Cache boyutunu ayarlamak:

1. ISA Management içinde, konsol ağacını açın.

2. Cache Configuration'ı tıklayın. Ardından Drives'i tıklayın.

3. Ayrıntılar bölmesinde, ISA Server üzerinde sağ tıklayın ve Properties'ı seçin.

4. Maximum cache size (MB) kutusunda sürücünün boyutunu yazın ve Set seçeneğini tıklayın.

Aynı şekilde bellekte oluşturulacak caching boyutu da ayarlanabilir:

1. ISA Management içinde, konsol ağacını açın.

2. Cache Configuration'ı tıklayın. Ardından Properties'i tıklayın.

3. Cache Configuration Properties iletişim kutusunda Advanced sekmesinde Percentage of free memory to use for caching kutusunda 1 ile 100 arasında bir değer yazarak ISA Server'ın kullanacağı bellek alanı yüzdesini belirtin.

FİREWALL YAPILANDIRMAK
-Server'ı güvenli hale getirmek.

-Perimeter Networkler.

-Packet Filtreleme ve IP Routing.

I. SERVER GÜVENLİĞİ

ISA Serve 2000 ©'ın en önemli olması bir güvenlik sistemi olan firewall özelliğine sahip olmasıdır. ISA Server, güvenlik ilkelerini uygulamak için çeşitli güvenlik özelliklerine sahiptir.

A. SECURİTY CONFIGURATION WIZARD

ISA Server Security Wizard ile Windows 2000 üzerinde çeşitli güvenlik düzenlemeleri yapılabilir. Bu güvenlik düzenlemeleri belli şablonların uygulanması olarak düşünebilirsiniz.

ISA Server için güvenlik şablonlarının düzeyleri ve şablon adları şunlardır:

Güvenlik Düzeyi Server Bilgisayar İçin Domain Controller

Dedicated Hisecws.inf Hisecdc.inf

Limited Services Securews.inf Securedc.inf

Secure Basicsv.inf Basicdc.inf

ISA Server Security Wizard'ı başlatmak için:

1. ISA Management içinde, konsol ağacı içinde sunucunuzu genişletin.

2. Computer'a tıklayın.

3. Ayrıntılar bölmesinde sunucu üzerinde sağ tıklayın, ardından Secure'ı tıklayın.

II. PAKET FILTRELEME VE IP ROUTING

Windows 2000 ve network konularında (diğer kurslarımızda da) söz ettiğimiz gibi, network güvenliğini sağlamak için IP paketlerinin kontrol edilmesi gerekir. Bunun içinde yapılacak işlemler paket filtreleme (packet filtering) ve IP yönlendirme (IP routing) işlemleridir.

Paket filtreleme, bilgisayar için IP paketlerine izin vermek ya da bloklamak anlamına gelir. Routing (yönlendirme) ise, network trafiğinin iç (internal) ve dış (external ya da Internet) networklar arasında yönlendirilmesidir.

A. PAKET FİLTRELEMEYİ ETKİNLEŞTİRMEK

Paket filtrelemeyi etkinleştirdiğinizde, ISA Server, ISA Server bilgisayarı üzerinde geçen IP paketini izler.

Paket filtrelemeyi etkinleştirmek için:

1. ISA Management içinde, konsol ağacı içinde sunucunuzu genişletin.

2. Access Policy'yı genişletin ve IP Packet Filters'ı sağ tıklayın ve ardından Properties'ı seçin.

3. General sekmesinde, Enable packet filtering onay kutusunun işaretli olmasına dikkat edin.

B. IP PAKET FİLTRELERİ OLUŞTURMAK

Bir IP paket filtresi oluşturmadan önce, paket ile ilişkili olan port ve protokolün belirlenmesi gerekir. Ayrıca kaynak ve hedef bilgisayarlar için IP adreslerinin de bilinmesi gerekir.

Bir IP paket filtresi oluşturmak için:

1. ISA Management içinde, konsol ağacı içinde sunucunuzu genişletin.

2. Access Policy'yı genişletin ve IP Packet Filters'ı tıklayın ve ardından Create a Packet Filter'ı seçin.

3. New IP Packet Fitler Wizard'da filtreyi tanımlayan bir ad girin ve Next'i tıklayın.

4. Fitler Mode sayfasında, Allow packet transmission ya da Block packet transmission seçeneklerinden birisini seçin ve Next'i tıklayın.

NOT: Allow izin vermek, Block engellemek anlamında.

5. Fitler Type sayfasında oluşturulacak filtre için Custom ya da Predefined olarak türünü belirleyin. Ardından Next'i tıklayın.

Fiter Settings sayfasında Custom (özel) filtre seçtiyseniz, aşağıdaki bilgilere göre seçeneklerinizi belirleyin:

IP Protokol: Özel protokolü belirlersiniz: TCP, UDP gibi.

Number: IP protokolü sayısı.

Direction: İletişimin yönü: Inbound (gelen), Outbound (giden) ve Both (her ikisi) gibi.

Local port: Kuralın uygulanacağı portlar.

NOT: Kuralı bütün portlara uygulayacaksanız All Ports seçeneğini seçmelisiniz.

Remote ports: Kuralın uygulanacağı uzak portlar.

NOT: Kuralı bütün uzak portlara uygulayacaksanız All Ports seçeneğini seçmelisiniz.

C. UYGULAMA FİLTRELERİ

Uygulama filtreleri (application filters), Firewall servisine ek bir güvenlik katmanı yaratmak için kullanılır. IP paket filtrelerinde farklı olarak, uygulama filtreleri istemci uygulama ile sunucu uygulama arasındaki bütün işlemleri izler ve özel bazı işlemlerin yapılması sağlar. Örneğin kimlik denetimi (authentication) ve virüs kontrolü gibi.

ISA Server'ın kurulmasıyla birlikte, SMTP dışındaki bütün uygulama filtreleri (application fitler) etkinleştirilir. Aşağıdaki listede bu uygulama filtreleri yer almaktadır.

Uygulama filtrelerinin bazıları:

DNS Intrusion Detection Filter: İzinsiz DNS kullanıcılarını bulur.

POP Intrusion Detection Fitler: İzinsiz POP kullanıcılarını bulur.

FTP Access Filter: FTP protokol desteği.

H.323 Filter: H.323 protokolünü kullanan network trafiğini kontrol eder.

ŞİRKET İÇİ KAYNAKLARA ERİŞİM

Amaçlar:

• Web yayıncılığını yapılandırmak.

• Server yayıncılığını yapılandırmak.

I. GİRİŞ

ISA Server’ı iç (internal) sunucularınızı Web içeriği ve e-mail servislerini dış (external) istemcilere yayınlamak için kullanabilirsiniz. Sunucuları (server) yayınlama (publishing) kurallarını (rule) ile dış istekleri içteki sunuculara yönlendirecek şekilde yapılandırarak bu işlemler yapılır. Sunucuları yapılandırarak ve Internet istemcilerinin isteklerini bir ISA Server bilgisayarına yönlendirerek şirketin iç (internal) sunucular üzerinde daha gelişmiş bir güvenlik sağlanır.

II. YAYINLAMA (PUBLISHING) İŞLEMİ

Sunucucuları (server) yayınlamak kaynaklara güvenli bir şekilde erişmeyi sağlar. Bir sunucuyu yayınlamak için bir yayınlama kuralı ilkesi oluşturulur. Yayınlama ilkeleri ISA Server’ın gelen istekleri işleyeceğini tanımlar. Bu yayınlama ilkeleri Web Server’lar ve diğer sunucular için oluşturulabilir.

Şirket içindeki bir sunucuyu yayınlamak, ona Internet üzerinden de erişimi olanaklı hale getirir. Web Publishing ile bir Web server, Server Publishing ile de diğer sunucular yayınlanır.

\[img\]www20.brinkster.com/ayhanergun/isa.jpg\[/img\]

Bir Web Server’ı yayınladığınızda kullanıcılar ISA Server’ın dış network adaptörüne bağlanırlar. Ardından ISA Server, iç network adaptörünü kullanarak isteği iç networke ulaştırır.

A. WEB SERVER’LARI YAYINLAMAK

Bir Web Server’ı yayınlamak (publishing a Web server), ISA Server aracılığıyla dış kullanıcıların şirket içindeki Web Server’a erişmesine izin verir. Bu düzenleme içinde; Web Server’dan istenen dış istekler aslında ISA Sever’dan yapılmış olacaklardır. Bunun dışında şirket içindeki Web Server’ın IP adresinin de dış kullanıcılara gösterilmemesi sağlanmış olur. Dış kullanıcılar ISA Server’ın IP adresini bilirler.

Bir Web Server’ı yayınlamak için önce bir Web Publishing rule oluşturmak gerekir. Bir Web publishing kuralı oluşturarak ISA Server bilgisayarını yapılandırılır. Böylece dışarıdan gelen istekler şirket içindeki Web Server’a yönlendirilir.

Bu işlem diğer erişim ilkelerinde (Access policies) olduğu gibi destination sets’ler aracılığıyla yapılır. Ancak yayınlanma ilkeleri için düzenlenen destination sets tanımlamaları, dış kullanıcıların bağlanacağı şirket içindeki bilgisayarları belirtir.

Yeni bir Web Publishing Rule Yaratmak:

1. ISA Management içinde, konsol ağacında, sunucuyu genişletin. Ardından Publishing’i genişletin ve Web Publishing Rules’ı tıklayın. Ardından ayrıntılar bölmesinde (sağ taraf), Create a Web Publishing Rule’ı tıklayın.

2. New Web Publishing Rule Wizard içinde; oluşturulacak kurala bir ad verin. Ardından Next ile ilerleyin.

3. Destination Sets sayfasında, bir destination set ve ilgili bilgileri belirtin. Ardından Next ile ilerleyin.

4. Client Type sayfasında istediğiniz istemci türünü belirtin ve yine Next ile ilerleyin.

5. Rule Action sayfasında, Redirect the request to this internal Web server seçeneğini tıklayarak yayınlanan Web Server’ın adını belirtin. Ardından yine Next ile ilerleyerek sihirbazı sonlandırın.

2. İSTEKLERİ DİĞER PORTLARA YÖNLENDİRMEK

Web yayınlama kuralları, istenen nesneleri istemcilere hangi sunucunun vereceğini belirtir. ISA Server, varsayım olarak HTTP isteklerini sunucudaki varsayım portlara yönlendirir. Şirket içindeki sunucu HTTP istekleri için farklı bir (standart olmayan) bir port kullanıyorsa, gelen Web isteklerini şirket içindeki bir yayınlanan sunucuya yönlendirmek gerekir.

Web isteklerini yayınlanmış bir sunucuya (published server) yönlendirmek:

1. ISA Management içinde, konsol ağacında, Web Publishing Rules’ı tıklayın.

2. Ayrıntılar bölümünde (sağ tarafta), oluşturduğunuz Web publishing kuralını tıklayın. Ardından Configure a Web Publishing Rule’ı tıklayın.

3. Web publishing kuralının Properties iletişim kutusundaki Action sayfasında Redirect the request to this Web Server’ı tıklayın.

Ardından HTTP isteklerinde kullanılacak port numarasını düzenleyin.

B. SERVER PUBLISHING İŞLEMİ

Bir sunucuyu (server) yayınladığınızda, aynı Web server’ın yayınlanmasında olduğu gibi, sunucu yayınlama kuralları (server publishing rules) istemcilerin dışarından gelen isteklerini şirket içindeki sunuculara yönlendirirler. ISA Server sunucu yayınlama kurallarıyla dışarıdan gelen istekler, ISA Server’ın arkasında kurulu olan SMTP sunucularını, SQL sunucularını ve FTP sunucuları gibi iç sunuculara ulaştırılırlar.

Yeni bir Web Publishing Rule Yaratmak:

1. ISA Management içinde, konsol ağacında, sunucuyu genişletin. Ardından Publishing’i genişletin ve Server Publishing Rules’ı tıklayın. Ardından ayrıntılar bölmesinde (sağ taraf), Publish a Server’ı tıklayın.

2. New Server Publishing Rule Wizard içinde; oluşturulacak kurala bir ad verin. Ardından Next ile ilerleyin.

3. Address Mapping sayfasında, iç ve dış sunucuların IP adreslerini belirtin. Next ile devam edin.

4. Protocol Settings sayfasında kuralın kullanacağı protokolü seçin.

5. Client Type sayfasında istediğiniz istemci türünü belirtin ve yine Next ile ilerleyin.

İZLEME VE RAPORLAMA

Amaçlar:

• Intrusion Detection.

• ISA Server aktivitelerini izlemek.

I. İZLEME ve RAPORLAMA

İzleme (monitoring) ve raporlama (reporting) araçları ISA Server’ın güvenliği izlemek ve oluşan olayları göstermek için kullandığı önemli araçlardır. ISA Server’da izleme ve raporlama işlemleri öncelikle bu işlemlerin planlanmasıyla başlar:

A. RAPORLAMA STRATEJİSİ OLUŞTURMAK

ISA Server’da bir raporlama ve izleme stratejisi oluşturmada için şu konuları göz önünde bulundurun:

1. Öncelikle izleme ve raporlama stratejinizi belgeleyin.

2. Aktivitelerden toplayacağınız bilgileri kategorize edin. Örneğin real-time alerts (uyarılar), performans ve güvenlik (security) olayları.

3. Oluşan logları yedeklemek için bir plan yapın.

B. INTRUSION DETECTION

ISA Server, “intrusion detection” olarak adlandırılan kötü niyetli kişilerin sisteme karşı ataklarını izleme ve tepkileri yapılandırma olanağına sahiptir. Bu işlem IP paketleri düzeyinde ve uygulama düzeyinde yapılabilir.

1. IP PAKET DÜZEYİ ATAKLARI

IP paket düzeyinde yapılan bu düzenlemede ISA Server birçok olayı anlar ve karşı işlemin yapılmasını sağlar. Bunlardan bazıları şunlardır:

All ports scan attack: Kötü niyetli kişilerin sistemde tanımlı portların dışında, diğer portlara erişmeyi denediklerinde oluşur. ISA Server ile erişilebilecek port sayısını belirtilir.

IP half scan attack: Kötü niyetli kişilerin hedef bilgisayara sürekli (tekrarlayarak) bağlanmak istemesi durumunda ve TCP paketlerinin belli bayrakları (flag) içermesi durumunda oluşur.

2. UYGULAMA DÜZEYİ ATAKLAR

Uygulama düzeyinde ise ISA Server yine çok fazla olayı bulur. Bunlardan bazıları şunlardır:

DNS hostname overflow: DNS’in host adı olarak belli bir uzunluktan fazlasını yanıtladığında.

DNS length overflow: IP adresinin 4 bayttan büyük olması durumunda oluşur.

3. INTRUSION DETECTION İŞLEMİNİ YAPILANDIRMAK

1. ISA Management içinde, konsol ağacında, sunucuyu genişletin. Ardından Access Policy’i genişletin ve IP Packet Filters’ı sağ tıklayın ve Properties’i seçin.

2. IP Packet Filtering Properties iletişim kutusunda, General sayfasında Enable packet filtering ve Enable Intrusion detection seçeneklerini seçin.

3. Intrusion Detection sayfasında ise diğer IP paketi düzeyini seçeneklerini seçin.

Port scan seçeneğini seçtiyseniz, portları belirleyin.

C. ISA SERVER OLAYLARI (EVENTS)

ISA Server’ın çalışması sırasında çeşitli olayları (events) ve koşulları saptayıp onları bir uyarı (alert) olarak sistem yöneticisine ulaştırabilirsiniz.

Aşağıdaki tabloda detect (saptanabilecek) edilebilecek bazı ISA Server olayları yer almaktadır:

Olay Açıklama

DNS intrusion Host name taşması vb DNS atakları.

Intrusion detected Bir dış kullanıcının kötü niyetli bir atakta bulunması

IP packet dropped Bir ilkeye karşı gelen bir IP paketinin düşürülmesi

IP protocol violation Yanlış IP seçeneklerine sahip bir paketin bulunması ve düşürülmesi.

D. ALERT’LERİN YAPILANDIRMAK

ISA Server’ın alert servisi olayları izler ve belli olayların oluşması durumunda belirlenen bir tepkiyi oluşturur. Bir alert, bir e-mail göndermek, bir programı çalıştıracak şekilde oluşturulabilir. Örneğin bir intrusion detection saptandığında sistem yöneticisine bir email göndermek gibi.

Bir Alert oluşturmak için:

1. ISA Management içinde, konsol ağacında, sunucuyu genişletin. Ardından Monitoring Configuration’ı genişletin. Alert’i sağ tıklayın ve New seçeneğini işaret edin, ardından Alert’i tıklayın.

2. New Alert Wizard içinde, Alert’in adını yazın ve ardından Next’i tıklayın.

3. Events and Conditions sayfasında alert tarafından tetiklenecek olayı seçin. Next ile ilerleyin.

4. Actions sayfasında; Send e-mail message, Run a program gibi seçeneklerden birisini seçin ve düzenlemeyi bitirin.

II. ISA SERVER AKTİVİTELERİNİ İZLEMEK

ISA Server aktiviteleri logging işlemini yapılandırarak izlenir. ISA Server logları gelen ve giden istekleri kaydeder. Logging işlemini yapılandırdığınızda, ISA Server erişim ve güvenlik aktiviteleri için loglar oluşturur. Ardından bu loglar analiz edilerek kullanım, performans ve güvenlik aktivitelerinin izlenmesi sağlanır.

A. LOGGING İŞLEMİNİ YAPILANDIRMAK

Logging işlemi yapılandırıldığında ISA Server şu logları oluşturur:

Packet filter logs: ISA Server bilgisayarı üzerinden geçen paketleri kaydeder.

Firewall service logs: Firewall servisini kullanarak yapılan iletişim girişimlerini kaydeder.

Web Proxy service logs: Web Proxy servisini kullanarak yapılan iletişim girişimlerini kaydeder.

Bu arada ISA Server log dosyalarını değişik formatlara düzenleyebilir. Bunlar W3C formatı, ISA formatı ve ODBC formatıdır.

Logları yapılandırmak için:

1. ISA Management içinde, konsol ağacında, Logs’ı tıklayın.

2. Ayrıntılar bölmesinde (sağ tarafta), Packet filters, Firewall service, Web Proxy service’den birisini sağ tıklayın ve Properties’i seçin.

3. Log sayfasında logları nasıl kaydedeceğinizi belirleyin.

4. Ardından Enable logging for this service onay kutusunu işaretleyerek log dosyası formatlarını düzenleyin.
III. ISA SERVER AKTİVİTELERİNİ REPORTS KULLANARAK ANALİZ ETMEK

ISA Server, loglarda tutulan aktivite kayıtlarını belli formatlarda hazırlanmış raporlar (reports) aracılığıyla sistem yöneticisine sunmayı amaçlar.

A. REPORT İŞLERİ (JOB) OLUŞTURMAK

Bir raporu görmeden önce, bir rapor işi (report job) oluşturmak gerekir. ISA Server, rapor işini çalıştırdıktan sonra, rapor görülebilir.

Bir rapor işi oluşturmak:

1. ISA Management içinde, konsol ağacında, sunucuyu genişletin. Ardından Monitoring Configuration’ı genişletin ve Report Jobs’ı sağ tıklayın ve New’ı işaret edin ve ardından Report Job’u seçin.

2. General sayfasında rapor için bir ad yazın ve Enable seçeneğinin seçili olduğundan emin olun.

3. Period sayfasında rapor işinin süresini seçin. Ardında Schedule sayfasında ise rapor işinin ne zaman oluşacağını belirleyin.

4. Ardından Recurrence pattern altında yinelenme aralığını belirleyin.

5. Credentials sayfasında ise raporu oluşturacak kullanıcı bilgilerini düzenleyin.

B. ÖNCEDEN TANIMLANMIŞ RAPOR FORMATLARI

ISA Server ile değişik tür ve içerikte raporlar oluşturabilirsiniz. Bu raporlar bir Web tarayıcısı tarafından bir Web sayfası olarak görüntülenebilir.

ISA Server tarafından oluşturulabilen rapor türleri:

Summary reports: ISA Server kullanımına ilişkin istatistikler. Bu bilgiler servisler için tutulan loglardan oluşturulur.

Web Usage reports: Web kullanıcılarını görüntülemek için kullanılan raporlar.

Application Usage Reports: Internet uygulamalarının kullanımını raporlamak için kullanılan raporlardır. Gelen ve giden trafik, istemci uygulamalar, en çok kullanan kullanıcılar vb.

Daha detaylı bilgi için http://www.microsoft.com/isaserver

http://www.isaserver.org
adreslerini önerebilirim

---
*Kaynak: `ISA HAKKINDA HERŞEY/ISA HAKKINDA HERŞEY.doc` — technics — 2004*
