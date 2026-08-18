# Windows 2000 'De DNS

**Windows 2000 ‘de DNS**

DNS (Domain Name System) , host isimlerinin (örneğin www.turkmcse.com) IP adreslerine çözümleme işini yapar.Bu işlem ,hatırlanması zor olan IP adreslerini ezberlemek yerine ,daha kolay olan ve hafızada daha da kalıcı yer eden host isimlerinin kullanımına izin verir.
Windows 2000 ‘in Active directory özelliğini kullanacaksanız ,yani bir domain oluşturacaksanız ,networkünüzde mutlaka bir DNS server olmalıdır. Bu DNS server’ı Active Directory’nin kurulumu sırasında kurabileceğiniz gibi ,Active Directory kurulumunu başlatmadan önce bir member server(üye sunucu) üzerinr bir DNS kurarak da Active Directory kurulumunu başlatabilirsiniz.

Peki neden DNS ile Active Directory birbiriyle bu kadar ilişki içerisinde? Birincisi Active Directory ,DNS ‘deki hiyerarşik isimlendirme standardını kullanır. İkincisi ise Active Directory istemcileri ,Domain Controller ‘ları ve Active Directory ‘deki kaynakları bulmak için DNS’i kullanırlar.

DNS ,domain name space olarak adlandırılan hiyerarşik yapıyı kullanır. Bu yapıda bir root domain vardır ve (.) şeklinde ifade edilir. Bu root domain altında top-level domain olarak adlandırılan com ,edu,gov gibi domainler vardır. Bu top-level domainlerin altında ise second-level domainler vardır. Örneğin turkmcse gibi. Gerçekte second-level domainler top-level domainlerin bir alt domainleridir.Örneğin turkmcse.com gibi. Eğer şirketiniz internete bağlanmayacaksa istediğiniz domain adını kullanabilirsiniz. Fakat şirketiniz internete bağlanacaksa kendi domain isminizi register etmeniz gerekecektir.

Windows 2000’de DNS’i anlatmadan önce DNS ‘deki zone (bölge) kavramını açıklayalım. Zone, bir DNS domaininin veya bir DNS domaini ve bunun alt domainlerine ait bilgilerin tutulduğu veritabanıdır. Bu dosya özel text dosyadır ve ‘zone file’ olarak bilinir. DNS Server servisi kurulduğunda varsayılan olarak hiçbir zone tanımlı değildir. Bu bölgeleri sizin oluşturmanız gerekir. Bir DNS server’da birden fazla zone olabilir. Ayrıca bir zone dosyası birden fazla DNS Server ‘da olabilir.Bu da hem hata toleransı hem de load balancing sağlar.

Bir DNS Server içerdiği zone tiplerine göre değişik roller üstlenebilir. Şimdi sırasıyla bu rolleri inceleyelim.

• **Primary Name Server** : Bu tür DNS server’da host ismi –IP eşlemelerinin tutulduğu bir zone dosyası bulunur. Bu server’da zone dosyasının asıl kopyası bulunur.Eğer zone içindeki datalar üzerinde bir değişiklik yapılacaksa bu değişiklik primary name server üzerinde yapılmalıdır.

• **Secondary Name Server** :Bu tür DNS Server’lar zone bilgilerini Primary Name Server’dan alırlar. Bu tür bir DNS Server kullanmanın başlıca faydalarını şöyle sıralayabiliriz.

1. Hata Toleransı.
2. Uzak kullanıcıların isim çözümleme işlemlerini hızlandırmak.
3. Primary Name Server’ın yükünü azaltmak.

• **Master Name Server** : Bu tür DNS server’ın görevi zone bilgilerinin Secondary DNS Server’a kopyalamaktır. Bu server Primary veya Secondary Name Server olabilir.

• **Caching –Only Server **: Bu tür DNS sunucuda herhangi bir zone dosyası tutulmaz. Bu server istemcilerden gelen host ismi- IP sorgularını çözer ve kendi cache’inde saklar. Daha sonra aynı host ismni için tekrardan bir istek gelirse asıl DNS sunucuya başvurmadan IP bilgisini kendi cache’ inden istemciye yollar. Bu bilgiler cache ‘de belli bir TTL (Time –To- Live) zamanı boyunca tutulur ve daha sonra cache’den silinir.

• **Forwarder** : Bu tür DNS Server’lar şirket içindeki DNS server’lardan gelen harici DNS sorgularını çözümlemek için kullanılırlar.

Bunun haricinde DNS server’larda kullanılabilecek zone tipleride şunlardır.

• **Standart Primary** : Bu zone tipinde ,DNS kayıtları özel formatlı bir text dosyada saklanır.

• **Active Directory Integrated** : Bu zone tipinde ,DNS kayıtları Active Directory veritabanında tutulur ve Active Directory replikasyonunu kullanarak replike olurlar.

• **Standart Secondary** :Bu zone ,Standart Primary zone dosyasının bir kopyasıdır.Zone dosyasının Secondary DNS server’a kopyalanması işine ‘zone transfer’ adı verilir.

Şimdi’de sıra Windows 2000’de DNS server kurulumuna geldi. DNS server’ın kurulacağı bilgisayardaki işletim sistemi Windows 2000 Server veya Advanced Server olmalıdır. Yani Windows 2000 Professional’a DNS server servisini kuramazsınız. Windows 2000’deki DNS server servisi dinamik güncelleme özelliğine sahiptir. Böylece istemci veya serverlar kendi host isim ve IP adreslerini kendileri DNS server’a kaydedebilir, güncelleyebilir. DNS’in eski versiyonlarında bu işlemleri gerçekleştirmek için böyle bir mekanizma yoktu. Yani tüm bu host ismi –IP eşlemeleri DNS Server’a elle girilirdi.

Windows 2000’de DNS Server servisini yüklemek için Control Panel’den Add/Remove Programs uygulaması çalıştırılır. Ardından açılan pencereden ‘**Add/Remove Windows Components**’ seçilir. Karşımıza çıkan pencereden ‘**Networking Services**’ seçeneği seçilerek ‘Details’ butonuna basılır. Burada Domain Name System (DNS) işaretlenerek windows 2000 DNS Server servisinin kurulumuna başlanır.

Kuruluma başlamadan önce dikkat edilemsi gereken önemli bir şey de DNS server servisinin kurulacağı bilgisayarın IP adresinin statik olmasıdır. Yani bu bilgisayar IP adresini herhangi bir DHCP sunucudan almamalıdır.

DNS Server servisi kurulduktan sonra sıra bu DNS Server’ın konfigüre edilmesine geldi. Bunu gerçekleştirmek için Administrative Tools ‘dan DNS ‘i çalıştırıyoruz ve karşımıza aşağıdaki ekran çıkıyor.

Bu ekran henüz DNS Server’ımızı konfigüre edilmedigini gösteriyor. Fakat DNS Server ‘ı konfigüre etmeden önce DNS Server’ın kendisini kendisine DNS istemci olarak tanıtmalıyız. Bu işlemi gerçekleştirmek için masaüstündeki My Network Places ikonunun üzerine mous ile sağ tıklayıp açılan menüden Properties ‘i tıklıyoruz.Açılan pencereden Local Area Connection ikonunun üzerine mous ile sağ tıklayıp açılan menüden Properties’i tıklıyoruz. Karşimıza network ile alakalı ayarların yapıldığı bir pencere çıkıyor.

Bu penceredeki seçeneklerden Internet Protocol (TCP/IP ) seçeneğini tıklayıp alttaki Properties butonuna basarsak karşımıza DNS Server’ın adresini girebileceğimiz bir pencere çıkar.

Bu işlemi gerçekleştirdikten sonra sıra network’teki root server’ı belirlemeye geldi. Dns Server’ın fonksiyonlarının doğru çalışabilmesi için bir root server tanımlamak gerekir. Eğer kurduğunuz DNS Server ,ağınızdaki ilk DNS Server ise bu server aynı zamanda root server olarak konfigüre edilir. DNS’de herhangi bir zone tanımlamadan önce mutlaka root server ayarının yapılmış olması gerekir.

Şimdi DNS Server için root server ayarını yapalım.Şekil 2 ‘de görülen ekrandaki sağ tarafta bulunan server’ın üzerine sağ tıklayıp açılan menüden ‘ **Configure the server** ’ seçenegini seçelim. Bu seçeneği seçtiğimizde karşımıza root server tanımlamalarında bize yardımcı olacak ‘**Configure DNS Server Wizard’ **sihirbazı çıkar.Next butonuna tıkladığımızda karşımıza Şekil 5 ‘deki ekran çıkar. Bu ekrandaki ‘**This is the first DNS server on this network**’ seçeneğini seçerseniz bu DNS server networkünüzdeki root server olur.Eğer networkünüzde root server varsa o zaman ‘**One or more DNS servers are running on this network**’ seçeneğini seçerek alttaki IP address kısmına bu root server’ın IP adresini girmelisiniz. Bizim örneğimizde kurduğumuz DNS Server networkumuzdeki ilk DNS Server olduğu için birinci seçeneği seçip Next butonuna basarak devam ediyoruz.Bir sonraki ekranda bize ,bir ‘**forward lookup zone**‘ oluşturmak isteyip istemediğimizi soruyor.Biz bu aşamada bir zone oluşturmak istemediğimiz için alttaki seçeneği seçip Next butonuna basıyoruz.Böylece DNS server
’ın root server ayarını yapmış oluyoruz.

Network’deki root server’ı belirledikten sonra sıra DNS Server’ı konfigüre etmeye geldi. Administrative Tools ‘dan DNS ‘i çalıştırın. Şekil 2 ‘deki ekranla karşılaşırsınız. Burada server’ın üzerine sağ tıklayıp açılan menüden Properties’i seçin .Karşınıza Şekil 6'da görülen altı sekmeli bir pencere çıkar.

Şimdi **Interface** sekmesindeki seçeneklere değinelim.Aslında buradaki seçenekler DNS ‘in kurulu olduğu bilgisayarda birden fazla IP adresi varsa bir anlam ifade ediyor. Şöyle ki ,eğer DNS Server bilgisayarında birden fazla IP adresi varsa ve biz bu IP adreslerinin tümüne gelen DNS sorgularının bu DNS Server tarafından cevaplandırılmasını istiyorsanız o zaman ‘**All IP addresses**’ seçeneğini seçin. Yok eğer ben sadece DNS Server ‘ın şu IP adreslerine gelen sorguların DNS Server tarafından cevaplandırılmasını istiyorum diyorsanız o zaman ‘**Only the following IP addresses**’ seçeneğini seçerek IP address kısmına bu IP adresini yazın.

**Forwarders** sekmesinde ise DNS Server’ın isim çözümleme işlemi için başka bir DNS Server kullanıp kullanmayacağını belirleyebilirsiniz. Eğer Forwarder DNS Server kullanılacaksa bu DNS Server’ların IP adreslerini girebilirsiniz.Birden fazla Forwarder Server kullanılıyorsa bunların sıralamasını da bu pencereden ayarlayabilirsiniz.

Bu pencereden ‘**Enable forwarders**’ seçeneğini seçerseniz aşağıdaki ‘**Do not use recursion**’ seçeneği de seçilebilir hale gelir. Bu seçeneği seçerseniz DNS Server’ın Forwarder server’lar tarafından çözülemeyen isimleri root server’a sormasını engellersiniz.

**Advanced ** ekmesine tıkladığınızda Şekil 8 ‘deki ekranla karşılaşırsınız. Bu pencerede DNS server’ın versiyon numarasını görebilirsiniz. Ayrıca pencereden server seçeneklerini de ayarlayabilirsiniz. Şimdi sırasıyla bu seçeneklere teker teker değinelim.

• **Disable recursion** : Bu seçenek seçilirse DNS Server’ın bir ismiçözümlemek için diğer DNS server’lara başvurmasını engellemiş olursunuz.

• **BIND secondaries** :Bu seçenek varsayılan olarak seçilidir ve zone’ların Master DNS ‘den Secondary DNS Server’a hızlı bölge transfer formatı(fast zone trasfer format) kullanılarak taşınmasını sağlar.

• **Fail on load if bad zone data** :Bu seçenek seçilirseDNS Server zone dosyasındaki hataları algılar , bu hataların loglarını tutar ve hata içeren zone dosyalarını kullanmaz. Fakat varsayılan olarak Windows 2000 DNS ‘ler hata içeren zone dosyalarını kullanır.

• **Enable round robin ** : Varsayılan olarak seçili olan bu özellik Windows 2000’in ‘*load balancing* ‘ özelliğini kulllanarak aynı isime sahip fakat IP adresleri farklıolan birden fazla server arasında yük dağılımını sağlamak için kullanılır. Örneğin şirketinizin web server’ı gün içinde çok hit alıyor ve bu da doğal olarak server’ınızı çok yoruyor ve performansını azaltıyorsa o zaman aynı özelliklere sahip ve aynı web içeriğini içeren aynı adlı bir web server daha kurarak yükün bu iki server’a dağılmasını sağlayabilirsiniz. Eğer DNS server’da bir host ismi için birden fazla kayıt varsa ve bu seçenek seçili ise istemcilerden gelen her DNS sorgusunda farklı bir IP adresi gönderilir ve böylece yük dağılımı sağlar. Bu seçenek seçili değilse DNS server,aynı host ismi için birden fazla kayıt girilmiş ve bu kayıtlara ilişkin bir sorgu olursa o zaman kayıtlar arasında bulduğu ilk kaydı istemciye yollar.

• **Enable netmask ordering :** Bu seçenek birden fazla netwrok kartı olan** **bilgisayarlara ilişkin sorguların DNS Server tarafından nasıl çözümleneceğini belirler. Şöyle ki ,eğer bu seçenek seçili ise DNS server kendisine bu tür bir bilgisayara ilişkin bir sorgu geldiğinde gelen sorguyu bu bilgisayarın istemciyle aynı networkte bulunan IP adresini göndererek cevaplar. Eğer bu seçenek seçili değilse DNS server istemcilerin sorgularına cevap vermek için round robin’i kullanır.

• **Secure cache against pollution :** Bu seçenek DNS Server’ın cache’inde** **ne kadar bilgi tutacağını belirler. Normalde sorgulara verilen tüm cevaplar cache’de tutulur. Eğer bu seçenek seçili değilse sadece son sorguya ait bilgiler cache’de tutulur.

Bu penceredeki DNS Server’la alakalı diğer ayarlarada bir göz atalım.’**Name checking**’ kısmındaki seçenekler ile manuel olarak girilen DNS kayıtlarının DNS Server tarafından nasıl kontrol edileceğini belirleyebilirsiniz. Burada seçebileceğiniz seçenekler **Strict RFC(ANSI)**, **Non-RFC(ANSI)** ve **Multibyte(UTF8)**.’ **Load zone data on startup **’ kısmındaki seçenekler ile DNS Server servisinin başlaması sırasında başlangıç bilgilerini nereden alacağını belirleyebilirsiniz. ‘ **Enable automatic scavenging of stale records **’ ise DNS Server’ın zone içindeki kayıtların arasında ne kadar önce girilmiş kayıtların silineceğini belirtir. Bu seçeneği seçtiğinizde bir kaydın eski olarak kabul edilip silinmesi için geçmesi gereken zamanı belirleyeceğiniz kısım aktip olur. Varsayılan zaman aralığı yani DNS ‘de bir kaydın eski olarak kabul edilebilmesi için geçmesi gereken zaman yedi gündür. Ayrıca server için yapılan bu ayarın ,bu server’daki tüm zone ‘lar için ayrı ayrı yapılması gerekir.

**Root Hints** tabında ise bu DNS Server’ın isim çözümleme için hangi DNS Server’lara başvurduğunu gösteren bir liste mevcuttur. Bu listeye Add butonuna basarak DNS Server ekleyebilir ,Remove butonuna basarak bu DNS serverlardan istediğinizi kaldırabilirsiniz.Şekil 9 ‘da bu sekmeye tıkladığınızda karşınıza çıkacak pencereyi görebilirsiniz. Eğer DNS Server’ınız bir root server ise bu liste aktif değildir.

**Logging** sekmesine tıkladığınızda karşınıza Şekil 10 ‘daki pencere çıkar.Bu pencerede DNS ile alakalı loglarının tutulmasını istediğiniz olayları belirleyebilirsiniz. Daha sonra bu olayları Event Viewer ‘daki DNS Server’ı seçerek izleyebilirsiniz. Varsayılan olarak DNS ile alakalı hiçbir olayın log’u tutulmaz.

**Monitoring** sekmesine tıkladığınızda ise karşınıza Şekil 11 ‘deki pencere çıkar. Bu penceredeki seçenekleri kullanarak DNS Server’ı test ederker ne tür sorgu kullanılacağını belirleyebilirsiniz. ‘ **A simple queryagainst this DNS Sever** ’ seçeneğini seçerseniz Test Now butonuna bastığınızda bir test sorgu oluşturulur ve bu sorgu sadece o DNS Server tarafından diğer DNS Server’lara başvurnadan çözümlenmeye çalışılır. Eğer alttaki recursive query ‘i seçerseniz bir test sorgu oluşturulur ve bunu çözmek için DNS Server diğer DNS Server’lara başvurabilir.

Eğer siz kurduğunuz DNS server’ı bir root server kullancak şekilde konfigüre etmişseniz kurmuş olduğunuz DNS server ‘ **Caching –Only** ’ server olacaktır.

Tüm bu ayarları anlattıktan sonra sıra gelgi zone tanımlamaya. DNS Server’a kayıt girmeden önce mutlaka bir zone tanımlamasının yapılması gerekir. Forward lookup zone dosyasında host ismi–IP adresi eşlemeleri tutulurken ,Reverse lookup zone dosyasında ise IP adresi–host ismi eşlemeleri tutulur. İlk olarakbir standart primary zone oluşturarak işe başlayalım. Administrative Tools’dan DNS’i çalıştıralım. Karşımıza çıkan ekrandaki DNS server’ın yanında bulunan + işeretine tıkladığınızda **Forward lookup zones** ve **Reverse lookup zones** adlı iki klasör karşınıza çıkar.Forward lookup zones klasörünün üzerine mouse ile sağ tıklayın ve açılan menüden ‘New zone ’ seçeneğini seçin.(Şekil 12)

Karşınıza yeni bir zone oluşturmak için size yardımcı olacak bir sihirbaz çıkacaktır.Bu sihirbazın hoşgeldiniz ekranını Next butonuna basarak geçtiginizde karşınıza oluşturmak istediğiniz zone tipine seçmenizi isteyen bir pencere çıkacaktır (Şekil 13).

Buradaki seçeneklerden Active Directory integrated seçeneğinin aktif olması için bilgisayarınızda Active Directory’nin kurulu olması gerekir.Bu pencereden Standart Primary’i seçip Next butonuna basalım. Bu sefer karşımıza zone adını gireceğimiz Şekil 14’deki pencere çıkar.Burada zone adını yazdıktan sonra Next butonuna basarsanız karşınıza bu seferde zone için kullanılacak dosyayı belirtmenizi sağlayan Şekil 15’deki pencere çıkar.

Bu dosyayı yeni oluşturabilecağiniz gibi varolan bir zone dosyasınıda burada belirtebilirsiniz.Next butonuna basıp ilerlediğinizde ilk zone oluşturma işlemini başarıyla tamamladınız demektir. Evet nihayer bir zone dosyası oluşturabildik. Eğer Standart Primary Reverse lookup zone oluşturmak istiyorsanız o zaman da DNS penceresindeki Reverse lookup zones klasörünün üzerine mouse ile sağ tıklayıp açılan menüden New Zone seçeneğini seçin. Bu seçenek seçildikten sonra Microsoft ‘un meşhur sihirbazlarından birisi size yardımcı olmaya başlayacaktır.Hoşgeldiniz ekranını Next butonuna basıp geçtikten sonra karşınıza zone tipini seçeceğiniz bir pencere çıkar.Buradan Standart Primary seçeneğini seçip Next’e tıklayın.Karşınıza ‘**Reverse lookup Zone** ’ başlıklı bir pencere çıkacaktır. Bu pencerede reverse lookup zone için iki seçenek mevcutur. Birincisi **Network ID** ,ikincisi ise **Reverse lookup zone name**. Biz birinci seçeneği kullanarak reverse lookup zone oluşturacağız. Size tavsiyem sizde bu seçeneği seçin. Çünkü reverse lookup zone’u zone ismine göre oluşturursanız hata yapma ihtimaliniz artar. Örneğimizde 10.3.9.0 netwrok’u için bir reverse lookup zone oluşturacağız.

Bunun için Network ID kısmına yazmanız gereken sayı Şekil 16 ‘da görüldüğü gibi 10.3.9 olacaktır.

Next butonuna tıkladığınızda ise reverse lookup zone dosyasını belirleyeceğiniz Şekil 17’deki ekran karşınıza gelir.

Burada dosya ismine dikkatinizi çekmek istiyorum.Dosyanın adı bizim yazdığımız Network ID ile alakalı.Yani Yazdığımız Network ID’nin ters çevrilmiş hali ile in-addr.arpa ifadesinin birleştirilmesinden oluşmuş.Next tuşuna basarak reverse lookup zone oluşturma işini başarıyla bitiriyoruz.

Oluşturduğumuz zone’ları konfigüre etmeye başlamadan önce buraya kadar anlattıklarımızın kısa bir tekrarını yapalım. Forward lookup zone,host isimlerinden IP adreslerini elde etmek için kullanılır. Yani siz istemci programda www.turkmcse.com yazdınız ve be istemci program bu DNS isteğini DNS server’a iletti. DNS Server bu isme karşılık gelen IP adresini bulmak için forward lookup zone ‘a bakacaktır. Reverse lookup zone ise IP adresinden host ismini bulmak için kullanılır.Bir DNS Serverda reverse lookup zone tanımlanması zorunlu değildir. Reverse lookup zone ‘u bir örnekle açıklayalım. Farzedelimki siz 10.3.9.174 IP adresine sahip bilgisayarın host ismini öğrenmek için DNS’e başvurdunuz. DNS bu IP adresine karşılık host ismini bulmak için Reverse lookup zone ‘u kullanacaktır.

Şimdi zone’ları konfigüre etmeye başlayabiliriz.Konfigüre etmek istediğimiz zone ‘un üzerine mouse ile sağ tıklayıp açılan menüden Properties’i seçin.Karşınıza beş sekmesi bulunan Şekil 18’deki pencere çıkacaktır.Şimdi bu pencerede yapılabilecek ayarları teker teker inceleyelim.

**General **sekmesinde zone’un çalışıp çalışmadığını ve bo zone’un tipini görebilirsiniz. Buradaki Pause butonuna basarak bu zone’un çalışmasını durdurabilir ,Change butonuna basarak bu zone ‘un tipini değiştirebirsiniz. Eğer bilgisayarınıza DNS Server’ı kurduktan sonra Active Directory kurduysanız ,standart primary zone ‘u Active Directory integrated zone ‘a dönüştürebilirsiniz. Bunun bize sağladığı bazı avantajları sıralarsak ;birincisi DNS kayıtları text dosyada değilde Active Directory veritabanında tutulduğu için sorguların çözümlenmesi hızlanır.Dolayısıyla DNS’in performansı artar.İkincisi ,DNS kayıtları Active Directory veritabaınında sakladığı için secondary server’a gerek kalmaz. Yani domain controller olan bir DNS server ,Active Directory’nin replikasyonunu sırasında DNS veritabanını da güncelleyecektir.Zone’un tipini değiştirmek istediğinizde Change butonuna basın.Bu butona bastığınızda karşınıza Şekil 19 ‘daki pencere çıkar. Burada zone ‘un yeni tipini belirleyip OK butonuna basarsanız zone’un tipini değiştirmiş olursunuz.

**Start of Authority (SOA)** sekmesine tıkladığımızda karşımıza Şekil 20’ deki pencere çıkar.Buradaki **serial number **kısmındaki sayı zone’un seri numarasını gösterir.Bu zone’a her yeni kayıt girilmesinde , kayıt güncellemesinde ve kayıt silinmesinde bu sayı bir artar. Secondary Server’lar bu sayıyı kontrol ederek kendilerindeki zone’un ,primary server ‘deki zone’un en son kopyası olup olmadığını anlarlar. **Primary Server** kısmında DNS Server’ın host adı yazılıdır.**Responsible Person **kısmında ise bu DNS Server’dan sorumlu olan kişinin ismi veya e-mail adresi yer alır.

**Refresh interval** kısmında belirtilen değer ise secondary server’ın zone bilgisini güncellemesi için beklemesi gereken zamanı belirtir. **Retry interval **kısmındaki değer ise secondary server’ın zone’un kopyasını güncellemek isterken herhangi bir nedenden ötürü gerçekleşemeyen güncelleme işlemini tekrar başlatmak için beklemesi gereken zamanı belirtir. **Exprises after** kısmındaki değer ise secondary server’ın herhangi bir nedenden dolayı primary server ‘a ulaşıp zonu’u güncelleyemediği durumlarda bu zone’a ilişkin sorgulara ne kadar zaman cevap vereceğini belirtir. Örneğin bu değer 1 gün ise secondary server ,primary server’a ulaşıp zone’u güncelleyemezse bile bir gün boyunca bu zone’a ait DNS sorgularını cevaplamaya devam eder. **Minimum (default) TTL **kısmında ise diğer DNS Server’ların bu DNS ‘den aldığı sorgu sonuçlarını ne kadar süre cache’lerinde tutacaklarını belirleyen bir değer vardır. Buraya girilecek değerin formatı gün:saat:dakika:saniye’dir.**TTL for this record **kısmında belirtilen değer ise diğer DNS Server’ların bu DNS Server’dan sorguladıkları ve cevap aldıkları Start of Authority kaydını ne kadar zaman cache’lerinde tutacaklarını belirtir.

Name Server sekmesine tıkladığımızda karşımıza Şekil 21 ‘deki pencere çıkar.Bu pencerede bu zone’u bulunduran DNS Server’ların listesi bulunur.Bir zone için en fazla bir tane primary server olabilir.siz bu penceredeki Add butonuna basarak bu zone ‘u içeren secondary serverları ekleyebilirsiniz.

**WINS** sekmesine tıkladığınızda ise DNS server’ın bu zone için çözemediği sorguları WINS yardımıyla çözüp çözemeyeceğini ayarlayabileceğiniz Şekil 22 ‘deki pencere çıkar.**Use WINS forward lookup **seçeneğini seçerseniz bu DNS server’ın isim çözümleme için kullanacağı WINS Server’ların IP adreslerini gireceğiniz kısım aktif olacaktır. Kullanılacak WINS Server’ların IP adreslerini yazarak Add butonuna basıp bu server’ları ekleyebilirsiniz. Birden fazla WINS server tanımlamışsanız UP ve Down butonları yardımıyla bu server’ların başvuru sırasını değiştirebilirsiniz. Bu sekme Reverse lookup zone ‘ların özelliklerinde yoktur. Bunun yerine WINS-R sekmesi vardır.

Son sekme olan **Zone Transfer**’e tıkladığınızda karşınıza Şekil 23’deki pencere çıkar. Bu pencerede zone transferini aktif veya pasif yapabilirsiniz. Zone transferini aktif yaparsanız alttaki seçeneklerden birisini seçerek bu zone transferinin tüm secondary serverlara mı, sadece Name Servers sekmesinde listelenen server’lara mı yoksa aşağıda belirteceğiniz IP adreslerine sahip secondary server’lara mı olmasını ayarlayabilirsiniz. Ayrıca **Notify** butonuna basarak zone transferi için uyarılacak secondary server’ları belirleyebilirsiniz.

Eğer standart secondary zone oluşturmak istiyorsanız ilk önce standart primary zone’un oluşturulmuş olması gerekir. Ayrıca standart secondary zone tanımlanacak DNS server ile standart primary zone’un tanımlı olduğu DNS Server’ın farklı bilgisayarlar olması gerekir.

Tüm bu tanımlamalardan sonra sıra DNS ‘deki zone ‘a kayıt eklemeye geldi. Zone a kayıt eklemeden önce önemli bazı kayıt türlerini açıklayalım.**

A** :Standart host ismi –IP adresi eşleme kaydı.**

CNAME** : Takma isim (alias) kaydı. Bu kayıt türünü kullanarak aynı IP adresini birden fazla hsot ismi ile eşleyebilirsiniz.**

MX** : Mail exchanger kaydı. Mail server’ın host isminin tutulduğu kayıt.**

PTR** : Pointer kaydı. Bu kayıt türü sadece Reverse lookup zone ‘da oluşturulabilir ve IP adresi host ismi eşlemesini tutar.

Şimdi örnek bir A kaydı oluşturalım .İlk önce kaydı oluşturacağımız zone üzerine mouse ile sağ tıklayıp açılan menüden New Host seçeneğini seçin.Karşınıza Şekil 24 ‘deki pencere çıkacaktır.

Burada bu kayıt için host ismi ve IP adresini girebilirsiniz. Gerekli bilgileri girdikten sonra Add Host butonuna basarsanız girmiş olduğunuz kayıt zone ‘a eklenecektir.Bu pencerenin alt kısmında yer alan ‘**Create associated pointer (PTR) record** ’ seçeneğini seçerseniz ,eğer bu zone için bir reverse lookup zone oluşturmuşsanız girdiğiniz bu kayıt için reverse lookup zone dosyasında da bir kayıt oluşturulacaktır.

Son olarak DNS alt domainlerin nasıl oluşturulduklarına değinelim. Büyük şirketlerde yönetim işini kolaylaştırmak için second-level domain’i (örneğin sirketim.com gibi) daha alt domainlere (örneğin satis.sirketim.com,muhasebe.sirketim.com gibi) bölmek gerekebilir. Bunu gerçekleştirmek için iki yöntem kullanabilirsiniz. Birincisi second-level domain’in altında bir zone daha oluşturmak. İkincisi ise zone delegasyonunu gerçekleştirmek. İkinci yöntemde ilk önce normal bir standart primary veya Active Directory integrated zone oluşturulur ve daha sonra bu zone’lar ilgili domainlere delege edilir.

---
*Kaynak: `WİNDOWS 2000 'de DNS/WİNDOWS 2000 'de DNS.doc` — blackkoc — 2004*
