# Kablosuz Ağ Teknolojisi

## ** Kısa Bir Tarihçe**

Kablosuz ağ teknolojisinin tarihi aslında tahmin ettiğinizden daha da gerilere dayanıyor. Elli yıl önce, İkinci Dünya Savaşında Amerika Birleşik Devletleri ordusu veri transferi için ilk defa radyo sinyallerini kullandı. Çok ciddi bir şifreleme kullanan bir radyo dalgaları ile veri transferi teknolojisi geliştirdiler. Bu teknoloji Amerika ve müttefikleri tarafından savaş sırasında oldukça fazla kullanıldı. Bu gelişme 1971 yılında Hawaii Üniversitesindeki bir grup araştırmacıya ilham kaynağı oldu ve ilk paket tabanlı radyo iletişim ağını kurmalarını sağladı. Adı ALOHNET olan bu ağ, bilinen ilk kablosuz yerel iletişim ağı (Wireless Local Area Network - WLAN) oldu. Bu ilk WLAN çift yönlü yıldız topolojisini kullanan 7 bilgisayardan oluşuyordu.

ALOHNET bünyesindeki bilgisayarlar dört ayrı Hawaii adasında yerleşik durumda idi, merkez bilgisayar Oahu adasında bulunuyordu. İşte kablosuz ağın doğuşu bu gelişme ile gerçekleşti.

Ağ pazarının tamamen kablolu yerel iletişim ağlarının hakimiyeti altında olduğu bir gerçek, ancak son bir iki yılda kablosuz ağ kullanımında belli bir artış göze çarpıyor. Bu artış özellikle akademik ortamlarda (üniversite kampüslerinde), sağlık kurumlarında, üretim ve depolama dünyasında görülüyor. Tüm bu zaman boyunca bu teknoloji sürekli gelişme halinde. Amaç, firmaların kablosuz ortama geçmelerini kolaylaştırmak ve maliyetleri düşürmek.

Topoloji: Elemanların fiziksel (gerçek) veya mantıksal (sanal) dizilişleri.

Bizim durumumuzda, topoloji kelimesi ağa bağlanan düğüm noktalarının (bilgisayarlar, ağ yazıcıları, sunucular, vs.) yerleşimini simgeliyor. Günümüzde kablolu iletişim ağlarında beş ana topoloji tipi kullanılıyor: Bunlar Bus, Ring, Star, Tree, ve Mesh isimleri ile adlandırılıyorlar. Bunlardan sadece ikisi kablosuz ağ ortamında işe yarıyor: "Star" (yıldız) ve "mesh" (ağ örgüsü) topolojileri.

Yıldız topolojisi (ki günümüzde en fazla kullanılan topoloji tipi budur) söz konusu olduğunda bir ağdaki iletişimi düzenlemek için bir baz istasyonu veya erişim noktası (Access Point - AP) kullanılıyor. Bir noktadan diğerine giden bilgi önce göndericiden erişim noktasına geliyor, oradan da hedef noktaya aktarılıyor.

Bu erişim noktası yada istasyon ayrıca kablolu bir ağa köprü ödevi de görebiliyor. Böylece kablosuz olarak bağlanan istemciye ağ üzerindeki diğer bilgisayarlara, Internet'e veya diğer ağ aygıtlarına erişim sağlanabiliyor. İncelediğimiz sistemde Compex'in SoftBridge programı herhangi bir erişim noktası veya donanıma ihtiyaç duymadan kablolu kaynaklara veya servislere bir "yazılım köprüsü" kuruyordu. Bu yazılım yardımı ile, kablolu bir ağa bağlı olan ve bir kablosuz ağ kartına sahip olan herhangi bir bilgisayar bir köprü olarak çalışabiliyor.

Ağ örgüsü topolojisi ise yıldız topolojisinden biraz daha farklı. Sistem aynı olmasına rağmen bir erişim noktası bulunmuyor. Birbirinin kapsama alanındaki her aygıt birbiri ile haberleşebiliyor.

## **IEEE 802.11, 802.11a, ve 802.11b**

WLAN'ların bük kitleler tarafından kabul görebilmesi için aygıtların üretici firmalarının arasındaki uyum ve güveni sağlayabilecek bir endüstri standardı gerekli. Institute of Electrical and Electronics Engineers (IEEE) adlı kuruluş bu endüstri standardını sağladı. IEEE 802.11 adındaki orijinal standart 1997 yılında konuldu, hemen arkasından IEEE 802.11a çıktı ve 1999 yılının Eylül ayında da IEEE 802.11b geldi. Orijinal standart 2.4GHz radyo frekansı (RF) bandında çalışıyor, 1Mb/s ve 2Mb/s veri transfer hızı ve bir dizi temel sinyalleşme metod ve servislerini barındırıyor. IEEE 802.11a ve IEEE 802.11b standartları sırasıyla 5.8GHz ve 2.4GHz bantlarını kullanıyorlar. Bu iki yeni standart ayrıca 5Mb/s, 11Mb/s, son olarak da IEEE 802.11a ile 54Mb/s veri transfer hızlarını sağlayacak fiziksel ortamları tanımlıyorlar. Bu standartlar Endüstriyel, Bilimsel ve Sağlık (ISM) adı verilen frekans bantlarında çalışıyorlar. Tipik bantlar 902-928MHz (26MHz bant genişliği), 2.4-2.4835 GHz (83.5 MHz bant genişliği), ve 5.725-5.850 GHz (125MHz bant genişliği) şeklinde, sonuncusu da IEEE 802.11a'a yüksek veri transfer hızı getiriyor.

Bu standart, kablosuz iletişimin PHY ve Medya Erişim Kontrolü (Media Access Control - MAC) katmanlarını tanımlıyor. Burada 'katman', birbiriyle ilişkili fonksiyonlardan oluşan her gruba verilen isim; her katman, içerdiği fonksiyonların birbirleri ile ilişkisi ölçüsünde gruplanarak diğer gruplardan ayrılıyor. Bizim kablosuz ağ senaryomuzdaki katmanlar şu benzetme ile kolayca anlaşılabilir: Bir kitap var (bu kitap burada bir veri paketini simgeliyor) ve siz bu kitabı bir odanın bir kenarındaki bir raftan alıp diğer kenarındaki masanın üzerine koyacaksınız. MAC katmanında bu kitabın raftan nasıl alınacağı, PHY katmanında ise odanın içerisinde nasıl yürüneceği tanımlanıyor.

Standartta tanımlanan bu PHY katmanı iki değişik tür radyo frekansı (RF) iletişim modülasyon şeması içeriyor. Bunlar Direct Sequence Spread Spectrum (DSSS - Doğrudan Sekans yayılma Spektrumu) ve Frequency Hopping Spread Spectrum (FHSS - Frekans Sıçramasıyla yayılma Spektrumu). İki tür de güvenilirlik, bütünlük ve güvenlik göz önüne alınarak Ordu tarafından geliştirilmiş. İkisinin de kendilerine özgü veri transfer etme yöntemleri bulunuyor.

FHSS kullanılabilen frekans bandını birkaç kanala ayırarak çalışıyor. FHSS dar bir bant taşıyıcı dalga kulllanır ve bu dalga 2-4 seviyesinde Gaussian Frequency Shift Keying (GFSK - Gauss Tipi Frekans Kayma Modeli) sekansında sürekli olarak değişir. Başka bir deyişle, transferin frekansı sürekli olarak, belirli bir hesap süreciyle rasgele oluşturulmuş ama gönderici ve alıcı aygıtlar tarafından bilinen bir şekilde değiştiriliyor. Böylece katmana biraz güvenlik eklenmiş oluyor. Hackerlar, sinyalin tamamını alabilmek genelde bir sonraki frekansın ne olacağını bilemiyorlar. FHSS'nin bir avantajı aynı fiziksel ortamda birden fazla ağın çalışabilmesine imkan verebilmesi.

DSSS ise tamamen farklı bir yöntemle çalışıyor. Veri akışını yüksek hızlı bir sayısal kodla birleştiriyor. Her veri birimi (her bit) hem gönderici hem de alıcı tarafından bilinen bir veri desenine eşleştiriliyor. Bu desene ise "Chipping Code" (şifreleme kodu) adı veriliyor. Bu kod, rasgele bir sıra yüksek ve alçak sinyalden oluşmuş şekilde esas veri birimini simgeliyor. Aynı kod, veri sekansındaki bir sonraki karşıt veriyi (biti) temsil tmesi için ters çeviriliyor (bkz. resim). Eğer veri iletimi doğru olarak senkronize edilmiş ise bu frekans değişiminin kendi hatasını düzeltme imkanı var, böylece girişim (interference) konusunda daha az hassas.

MAC katmanı fiziksel bir katmana erişmek için bir yol tanımlıyor, ayrıca hareket (nobilite) ve radyo kaynağı ile ilgili servisleri kontrol ediyor. Veri transferi için kullanılan kablolu Ethernet standardına benzediği söylenebilir. Fark, veri paketlerinin çarpışmalarının çözülmesi konusunda ortaya çıkıyor. Kablolu standartta veri paketleri ağ üzerine aralarında fark gözetmeksizin gönderilirler. Sadece iki paket birbiri ile "çarpışınca" sistem paketlerin doğru hedeflerine varmalarını sağlamak için ekstra işlem gerçekleştirir. 802.11 standartlarında, veri paketlerinin çarpışmasını önleme özelliği bulunuyor. Bu özellikte, hedef bilgisayar veriyi başarı ile aldığında gönderici bilgisayara bir "teslimat tamamdır" (Acknowledgement - ACK) paketi yolluyor. Eğer gönderici bilgisayar ACK paketini ("tesimat tamam" onayını) almazsa bir süre daha gelmesini bekliyor ve gelmeyince veriyi tekrar gönderiyor.

Ne var ki, hala 802.11 standardının çözülmesi gereken sorunları bulunuyor. Standardın hedefi "standartlaşmak" ve "ürünler arası uyumluluk". Ancak hala birden fazla üretici firmanın ürününün birbiri ile çalışabilmesi için gerekli bazı kilit meseleler çözülebilmiş değil. Bu meselelerden biri, iki cihazın birbiriyle anlaşması için (ülkeler arasında farklı GSM operatörlerinin anlaşabilmesi için yapılan anlaşmada olduğu gibi buna "roaming" deniyor), bir erişim noktası koordinasyonunun oluşturulması. Standartta bir aygıtın bir erişim noktasının kapsama alanından çıkıp başka birinin alanına girdiğinde ne yapılacağı tam olarak tanımlanmış değil; bunun için otomatik bir mekanizma yok. Ayrıca, bir aygıtın standarda tam olarak uyup uymadığını kontrol etmek için bir test de geliştirilmiş değil.

## **Ağ Güvenliği Ve Gizlilik**

Doğal olarak kablosuz ağlar olgunlaşmış kablolu ağlara göre daha az güvenli. Kablosuz ağ kartları verileri havadan transfer ettikleri için yetkisiz kullanımlara ve "kulak misafirliğine" açıklar. Bir ağ "koklayıcısı" (sniffer) aygıt kullanılarak kablosuz bir ağda gerçekleştirilen iletişim kablolu bir ağa göre çok daha kolay bir şekilde izlenebilir ve çalınabilir. Ağa fiziksel bir bağlantıya gerek olmadığı için, bu ağlara dışarıdan çok kolay giriş yapılabilir. Bir hacker özentisinin bu gibi bir işe girişmek için tek ihtiyacı kablosuz bir ağ kartı ve söz konusu ağın zayıflıklarını tespit etmektir!

Hacker özentilerinden gelen saldırıları engellemeyi denemek için, standarda Kablolu Eşdeğeri Protokol(WEP - Wired Equivalency Protocol) adında bir protokol eklendi. Teorik olarak, bu protokolün ana fikri ağdaki gizliliği sağlamak. İkinci fonksiyonu ise kablosuz ağa yetkisiz girişi engellemek. Birkaç araştırmacı tarafından yapılan analizler, bu protokolün iki amacını da tam olarak başaramadığını gösteriyor. Görülen o ki, bu protokol şu saldırılara açık:

İstatistiksel analizi taban alan trafiği çözmek için pasif saldırılar.

Yetkisiz mobil istasyonlardan ağa yeni trafik sokmaya dayalı aktif saldırılar.

Trafiği çözmek için erişim noktasını kandırmaya dayalı aktif saldırılar.

Gerçek zamanlı trafiği otomatik olarak çözmek için, bir günlük trafiğin izlendiği ve analiz edildiği bir "sözlük oluşturma" saldırısı.

WEP protokolü, temel servis setinde (kablosuz bir erişim noktası ve ilişkili düğüm noktaları dizisi) paylaşılan gizli bir anahtara dayanıyor. Bu anahtar kullanılarak veriler transfer edilmeden önce şifreleniyorlar. Ayrıca paketlerin yolda değiştirilip değiştirilmediği de kontrol ediliyor. 802.11 standardının bir açığı paylaşılan bu anahtarların nasıl kurulacağı konusunda yaşanıyor. çoğu kablosuz ağ kurulumunda, her düğüm noktası ve erişim noktası arasında paylaşılan tek bir anahtar var ve bu anahtar elle ayarlanıyor.

Bu şifreleme yöntemindeki problem aslında şifreleme algoritmasının kalbinde yatıyor. WEP, "Stream Cipher" olarak adlandırılan RC4 algoritmasını kullanıyor. "Stream Cipher" kısa bir anahtarı sonsuz sayıda gelişigüzel anahtar sıralamasına genişletiyor. Gönderici bu anahtar sırasını göndereceği metin ile XOR'luyor ("XOR - Exclusive or" - Ayrıcalıklı 'veya') ve şifrelenmiş metni üretiyor. 2 bit veriyi XOR fonksiyonuna tabi tuttuğunuzda karşılaştırılan iki bitten biri 1 ise (ancak ikisi birden 1 olmayacak) sonuç 1, aksi takdirde sıfır çıkıyor. Bu yöntemi aklında tutan alıcı şifreli metni çözmek için anahtarın kendisindeki kopyasını kullanıyor. Alıcıdaki şifreli metin anahtar akışı ile XOR'lanınca orijinal metin elde ediliyor.

Bu yöntemle çalışan "Stream Cipher"lar kendilerini birkaç saldırı türüne açık ediyorlar. Bu saldırılardan biri ağdan çalınan bir paketteki bir biti değiştirmek. Bu biti değiştirdiğinizde, veri çözüldüğünde hata çıkıyor. Diğer saldırı ise bütün düz metinleri elde tme imkanına sahip. Bu saldırıda dinleyen hacker'ın aynı anahtar ile şifrelenmiş iki metni elde etmesi yeterli. Bunu yaparak iki düz metnin XOR'u ele geçirilmiş oluyor. Bu XOR bilindiğinde istatistiksel saldırılar ile düz metinler çözülebiliyor. Paylaşılan bir anahtarın ele geçirilen şifreli metinlerinin sayısı çoğaldıkça saldırı daha da kolaylaşıyor. Tek bir düz metin çözüldükten sonra diğerlerini çözmek çocuk oyuncağı.

WEP'in bu iki saldırıya karşı eli armut toplamıyor elbette. Paketin transfer esnasında değişmediğini garantiye almak için pakette bir Integrity Check (IC - Bütünlük Kontrolü) alanı bulunuyor. Initialization Vector (IV - Başlangıç Vektörü) kullanılarak aynı anahtar dizisiyle iki metnin şifrelenmesi engelleniyor. Ancak araştırmalar bu önlemlerin hatalı uygulandığını ve bu yüzden güvenlik tedbirlerinin etkisinin azaldığını gösteriyor.

IC (Bütünlük Kontrol) alanı bir CRC-32 sağlaması (çok sık kullanılan bir hata tespit şeması) olarak uygulanıyor. Bu şemanın problemi lineer olması. Veri paketleri arasındaki bit farkını temel alarak iki CRC arasındaki bit farkını hesaplamak mümkün. Bunu yaparak bir saldırgan ağa göndereceği paketteki hangi bit'leri değiştireceğini ve paketi "kabul edilebilir" hale getireceğini tespit edebiliyor.

WEP algoritmasının diğer bir zayıflığı ise 24-bit Başlangıç Vektörü (IV) kullanması. Bu, mümkün olabilen IV'lerin sayısını çok düşürüyor. Yani görece olarak kısa bir süre sonra aynı anahtar dizisinin tekrarlanması mümkün. Orta büyüklükteki paketlerin söz konusu olduğu ve çok fazla işleyen bir erişim noktasında bu süre yaklaşık olarak 5 saat. Eğer paket boyutu düşerse bu zaman daha da kısalıyor. Bu şekilde sabırlı bir saldırgan aynı anahtar dizesiyle şifrelenmiş iki metni bekleyɩp istatistiksel analizine başlayabiliyor. Ayrıca bütün mobil aygıtlar aynı anahtarı kullandığında, IV çarpışma olasılığı da gittikçe büyüyor. Sanki bunlar yetmezmiş gibi 802.11 standardı her pakette IV değişimini "opsiyonel" olarak bırakmış.

Bu tür saldırılara karşı güçlü önlemler almak için daha gelişmiş anahtar yönetim yöntemleri kullanılabilir. Bu saldırılar aslında düşündüğünüz kadar basit değil. Şurası bir gerçek ki, günümüzde piyasada olan 802.11 ürünler hacker özentilerinin 2.4GHz sinyali çözmelerini kolaylaştırıyor ancak işin zor tarafı donanımın kendisinde. Çoğu 802.11 aygıt, kendisinde anahtarı olmayan şifrelenmiş bir içerik geldiğinde bu içeriği yok sayacak şekilde ayarlanmış. Ancak sürücülerin ayarlarını değiştirerek bu tanımlanamayan şifreli metinlerin daha sonra analiz edilmek üzere geri döndürülmesini sağlamak mümkün. Veri transferinin söz konusu olduğu aktif saldırıları gerçekleştirmek imkansız gibi görülmese de, daha zor.

Bütün bunlar, kablosuz ağ teknolojisine çekinceli yaklaşılmasına neden oluyor. Problem kablosuz standartların kriptografik temellerinin yanlış anlaşılmasından ve yanlış kullanılmasından dolayı ortaya çıkıyor. 802.11 standardının güvenlik ve gizliliğini artıracak yeni bir standart çıkana dek yüzde yüz güvenli kablosuz ağlar maalesef mümkün değil.

**Performans: Gerçek Hayattan Bir Örnek** Şimdi, teknik bilgi konusunda eteğimizdeki bütün taşları döktüğümüze göre, artık kullanıcı için gerçekte önemli olan soruya gelebiliriz: "Ne kadar hızlı?". Bu konuya girmeden önce kullandığımız ürünle sizi tanıştıralım.

Compex'ten gelen kablosuz ağ kiti - C-Kit 811WL WLAN. Paket içerisinde iki WavePort WL11 11Mb/s kablosuz PCMCIA LAN kartı, bir PCMCIA/PCI adaptörü ve bütün bunları birbirine bağlayacak olan sürücüler ve yazılımlar bulunuyor.

Bu kartlar DSSS modülasyon şemasını kullanıyorlar ve FCC kurallarına göre mümkün olan 14 kanaldan 11 tanesi kullanacak şekilde sınırlandırılmışlar. Üreticinin ürün hakkındaki özellikler sayfasında kartın 3.8-4.0 Mb/s kapasite ile 11 Mb/s veri transfer hızının olduğu yazıyor. Birazdan bu özelliği tam olarak test edeceğiz.

Kartların sisteme kurulumu oldukça standart ve kolay. Sistemi kapatıyoruz, kartları takıyoruz, sistemi açıyoruz ve bizden istenildiğinde sürücü diskini takıyoruz. Bundan sonra geriye kalan gerektiğinde ayarları değiştiren ve sürücüyü Reset eden konfigürasyon programını sisteme kurmak. Program ayrıca ağ bağlantısının durumunu size rapor eden bir sistem simgesi de gösteriyor.

Compex konfigürasyon programının simgesi, yeşil ekranlı, dalgalar çıkartan antene sahip bir bilgisayara benzeyen simge.

Ağ kartının bağlantısı kesildiğinde simgedeki bilgisayarın ekranı kırmızı oluyor ve antenden dalgalar çıkmıyor.

Bu simgeye çift tıklayınca ekrana ayarları yapabileceğiniz uygulama penceresi geliyor. Pencerenin dört bölümü bulunuyor.

Gördüğümüz gibi birinci bölümde yaklaşık olarak saniyede bir kere tazelenen bir bilgi sayfsı var. "State" kartın bağlı olup olmadığını bildiriyor. Görüldüğü gibi, kart şu anda BSS ID (Temel Servis Seti Kimliği) ile bağlı, kanalı 11 olarak ayarlanmış ve veri transfer hızı şu anda 11Mb/s. Throughput (Trafik), sayfa tazelendiğinde gerçekleşmekte olan dışarı yönlü (Tx) ve içeri yönlü (Rx) tafiğin anında ölçümünü gösteriyor. Bağlantı kalitesi ve sinyal gücü sadece Infrastructure (altyapısal) topoloji için geçerli. O an oluşan (Ad Hoc) ağ topolojisi için geçerli değil (pencerede "Not Applicable" olarak gösterilmiş), çünkü bu durumda veri birçok değişik bilgisayardan geliyor.

Bu bölümde şifreleme kelimesi dışındaki bütün ağ ayarları yer alıyor. Compex'in "Ad Hoc", "802.11 Ad Hoc" ve "Infrastructure" modlarından birini tercih edebiliyorsunuz. "Non-802.11 Ad Hoc" topolojisi bir zamanlar SSID söz konusu değilken üretilen kablosuz ağ kartları için geçerli. Örneğin, eğer değişik SSID'ler ile ayarlanmış iki "Ad Hoc" istemci varsa, yine de birbirleri ile iletişim kurabiliyorlar. "802.11 Ad Hoc" ise SSID kullanıyor. İki "802.11 Ad Hoc" istemcinin birbiri ile bilgi alışverişinde bulunabilmesi için ikisinin de SSID'leri aynı olmalı. Her zaman "802.11 Ad Hoc" kullanılmalı, aksi takdirde ağ güvenliğinden ödün verilmek zorunda kalınıyor. Compex bu "non-802.11 Ad Hoc" seçeneğini SSID desteği olmayan diğer ağ kartları ile haberleşebilmeye imkan vermek için bırakmış. "Infrastructure" modu elbette 802.11 ile uyumlu. Default olarak "ANY" olan SSID ayarı iletişim için hangi ağ ID'sinin kullanılacağını belirliyor ve böylece aynı alanda farklı kablosuz ağların birbirlerine bulaşmadan çalışmalarına imkan veriyor. "Tx Rate" ayarı (burada 11 Mb/s olarak ayarlanmış) Fully Automatic, 1Mbps, 2Mbps, 5.5Mbps, 11Mbps veya otomatik 1 veya 2Mbps olarak ayarlanabiliyor. "WEP", daha önce bahsettiğimiz Wired Equivalency Protocol (Kablolu Eşdeğeri Protokol) şifrelemesini ayarlıyor. Kapatılabiliyor veya 64 ve 128-bit şifreleme olarak ayarlanabiliyor. "PS Mode" güç koruma ile ilgili. "Channel" ayarı iletişim için hangi kanalın kullanılacağını belirlemek için kullanılıyor.

Üçüncü bölümde şifreleme ayarları bulunuyor. Bu bölüm sadece "WEP 128-bit" olarak ayarlandığında aktif. 64-bit olarak ayarlandığında değişiyor. Her birinde beş ikili şifreleme anahtarı alanı olan dört anahtar alanı geliyor.

Son olarak da "About" bölümü var. Her programda olan, firma bilgilerini ve versiyonu gösteren bir bölüm burası. Firmware revizyon numarasını bu bölümün üstünde, programın versiyon bilgisini de alttaki kutuda bulabilirsiniz.

## **Testler**

Ağ kartları bağlı ve ağda bilgisayarlar birbirlerini görüyor, demek ki test etmeye başlayabiliriz. Bu yazıda kullanacağımız test yazılımı Qcheck. Bu program NETIQ tarafından hazırlanmış olan ağ uygulamaları ve donanım performans test paketi olan Chariot'un bir parçası. Bu ücretsiz programı **http://www.netiq.com/qcheck/default.asp** adresinden çekebilirsiniz. Test verilerini toplarken aşağıdaki testleri beşer kere çalıştırdık ve karşılaştırmak için ortalamalarını aldık.

## **TCP Cevap Süresi**

Bu test bir TCP işleminin yapılıp bitirilmesi için geçen test minimum, ortalama ve maksimum süreyi ölçüyor. Test için 100 baytlık verinin 10'lu iterasyonunu seçtik. Testi klasik "ping" programının soslandırılmış bir versiyonu olarak nitelendirebiliriz. Program, bağlantının "lag" (zaman aşımı) süresini ölçüyor.

## **TCP Trafiği**

Bu test iki nokta arasında TCP protokolü kullanılarak saniyede başarı ile gönderilen veri miktarını ölçüyor. Program test için 1 Mb veri kullanıyor ve paketlerin başarı ile gönderilmesi için geçen zamanı kaydediyor. Test sonucunda bağlantının bant genişliği ölçülüyor.

## **UDP Streaming Kapasitesi**

Bu test akıcı verinin hedef noktada hangi hızla alındığını ölçüyor. Ayrıca hem paket kayıpları hem de CPU kullanımı ölçülüyor. Testte 10 saniye için 1Mb/s kullandık. Test, video yayını gibi gerçek zamanlı uygulamaların davranışını simüle ediyor. UDP gibi akıcı medya protokolleri bağlantıya gereksinim duymuyorlar ve daha yüksek performans için onay sinyali (ACK) almadan veriyi gönderiyorlar.

Kablosuz ağ kurulumunda trasfer hızını otomatik olarak bıraktık. Bunu yaparak, kartların mümkün olan en iyi bağlantıyı ve en yüksek hızı kendilerinin seçmesi sağlandı. Ağ mimarisini "802.11 Ad Hoc" olacak şekilde ayarladık. "802.11 Ad Hoc" ayarında üç farklı "WEP" ayarını denedik: no WEP, 64-bit WEP, ve 128-bit WEP. Bunu yaparak paketlerin şifrelenmesinin ve çözülmesinin ağ performansını etkileyip etkilemeyeceğin görmek istedik.

Kablolu ağ için, Kategori 5e crossover kablo kullandık. Kablosuz ağda ise iki sistem arasında yaklaşık olarak 2 metre mesafe bıraktık. İki sistemde de Windows 98 SE (Windows 98 4.10 Build 2222 A) kuruluydu ve test yazılımı dışında hiç bir uygulama çalışmıyordu.

Bu testlerin hiç biri ağ performansını tam ölçebilen eksiksiz testler değil. Ancak yine de bundan daha fazlası tanıtım amacını güden bu yazımızın konusunun dışına taşmak olacaktı.

Test sistemleri:

## **Sonuçlar**

Testler bitti; sonuçları görmenin ve bunlardan bir anlam çıkartmanın zamanı geldi.

Kablolu ağ için TCP protokolünün cevap zamanın çok daha düşük olması bir sürpriz değil. Bunun nedenini bağlantıların basitliğinde arayabiliriz. Kablolu ağ için DSSS modülasyonu, WEP, IEEE 802.11, girişim vs. yok. Ayrıca veri paketlerini şifrelemek gibi bir işe de kalkışılmıyor.

TCP kapasitesi beklediğimizden daha düşük çıktı. Firma, kartın 3.8-4.0Mb/s'lere ulaşabildiğini belirtiyor, ancak kartlar testte hiç bir şifreleme yokken bu değerden azıcık daha düşük performans gösteriyorlar.

Bir kez daha kablolu ağ ile kablosuz ağ arasında dağlar kadar fark var. Ve yine, verinin şifrelenmesi kapasiteyi etkilemiyor.

Bu sonuçlar oldukça şaşırtıcı, özellikle iki sistem arasında sadece iki metre ve herhangi bir engel bulunmadığı göz önüne alındığında.

## **Sonuçlar, Devam **

CPU kullanımı kablosuz kartlar için biraz hatalı. Bunun nedeni bazı testlerde yaşanan bağlantı kopmalarına ve hızın tekrar ayarlanmak zorunda kalınmasına fatura edilebilir.

## **Sonuç ******

SOHO (Small Office/Home Office) kullanıcıları, yani küçük ofislerde ve evlerinde çalışanlar için bu ürün oldukça ilgi çekici. Bu tür bir ürün söz konusu iken evde veya ofiste halıların altından, duvarlardan kablo geçirtmek zorunda kalmıyorsunuz. Notebook kullanıcıları evlerine geldiklerinde veya işyerlerine gittiklerinde verilerini evlerindeki bilgisayarlara transfer etmek için Docking Station veya bunun gibi çözümlere yönelmek zorunda kalmayacaklar. Kablosuz ağ kullanımı bilgisayar kullanıcılarını kablo ve Docking Station maliyetinden kurtarıyor. Ayrıca ofisteki iş büyüdüğünde veya küçüldüğünde, yeni bir bilgisayarı ağa eklemek için ekstra kablo vesaire gibi maliyetlere de girmek gerekmiyor. Büyük depolarda, antrepolarda kablolu ağ kurmanın zorluğu ortada, bu durumda kablosuz ağlar iletişim için tek ilgi çekici alternatif olarak görülebilir. Eğer işyeri bir yere taşınacaksa, ağı da beraberinde taşımak son derece kolay. Görülen o ki, kablosuz ağların hızı ve performansı arttıkça, kablosuz ağ kablolu ağ karşısında oldukça güçlü bir alternatif olmaya başlayacak.

Bu ön çalışmada elde ettiğimiz veriler şu andaki kablosuz ağ performansının yüksek kapasite ve performans isteyen ev kullanıcıları için yetersiz kaldığını gösteriyor. DVD filmleri evdeki bütün bilgisayarlara akıcı olarak göndermek isteyen kullanıcılar ve yüksek kapasite isteyen çok kullanıcılı oyunlarla ilgilenenler her zaman yüksek performanslı bir ağ isterler. Bu kablosuz çözüm bu tür kullanıcılar tarafından pek kabul edilebilecek gibi görünmüyor.

Gizli bilgilerin varolduğu ve güvenliğin çok önemli olduğu ağlarda 802.11 tabanlı ürünlerin kullanılmasına muhalefet şerhi koymak zorundayız. Güvenlik henüz kabul edilebilir seviyede değil.

Bütün bunlarn anlamı nedir? Anlamı şu: Kablosuz teknoloji geliştikçe, güvenlik ve gizlilik seçenekleri sağlamlaştırıldıkça ağ pazarında kablolu ağları geride bırakacak bir seviyeye gelebilir. Avuçiçi aygıtlar, mobil bilgisayarlar ve akıllı ev aletleri hızla çoğaldıkça kablosuz bir ağ kullanmanın pratikliği daha çok anlam kazanıyor. IEEE 802.11a'nın frekansı 5 Ghz bandına kaydıkça ve kanal sayısı arttıkça 54 Mb/s'lik bağlantı hızlarına erişilebiliyor. Eğer bugün bu seçenekler var olsaydı, kablosuz ağları kablolu ağlara çok sağlam bir alternatif olarak ortaya çıkarabilirdi.

Kablosuz ağ ürünlerini izlemeye devam edeceğiz, testlerimizi de geliştireceğiz. En başta söylediğimiz gibi, bu tam teşekküllü bir test değil. Ancak kablosuz ağların anlam taşıyıp taşımadığını tespit edecek yararlı istatistikler yaratmaya doğru attığımız ilk adım olarak kabul edilebilir.

---
*Kaynak: `KABLOSUZ AĞ TEKNOLOJİSİ/KABLOSUZ AĞ TEKNOLOJİSİ.doc` — OSMAN EKER — 2004*
