# TCP IP Ve Firewal

Daha önceki yazıyı Asyncronous Transfer Mode şeklinde bir başlık atarak sonlandırmıştım. Ancak TCP/IP ve Firewall konusu araya girmediği takdirde konu bütünlüğünün tam olarak oluşmayacağını düşündüğümden; bu konuyla devam etmeyi tercih ediyorum. Eğer TCP/IP' ye yeterince hakim olduğunuzu düşünüyorsanız doğrudan Firewall başlığına atlayabilirsiniz.

| **TCP / IP ve Firewall** |
| --- |
| **Giriş** |

Yeniden merhaba;

Öncelikle bir önceki yazım olan **Bilgisayar Ağları** başlıklı yazıya olan okur ilgisinin beni çok sevidirdiğini belirtmek istiyorum. Yazının altına eklenmiş yorumları okudum. Fikir bildiren herkese ayrıca teşekkürlerimi bildiririm. Diğer taraftan arayı da çok uzattık; bunun da gayet farkındayım. Eğer beklemekten sıkılmış arkadaşlar olduysa onlardan da ayrıca özür diliyorum.

Daha önceki yazıyı **Asyncronous Transfer Mode** şeklinde bir başlık atarak sonlandırmıştım. Ancak **TCP/IP ve Firewall** konusu araya girmediği taktirde konu bütünlüğünün tam olarak oluşmayacağını düşündüğümden; bu konuyla devam etmeyi tercih ediyorum. Eğer TCP/IP' ye yeterince hakim olduğunuzu düşünüyorsanız doğrudan **Firewall** başlığına atlayabilirsiniz.

## **TCP/IP**

(Transmission Control Protocol / Internet Protocol)
(İletim Kontrolü Protokolü / Internet Protokolü)

İnternetin temel protokol**\*** paketidir. Ve OSI**\*** katmanlı yapısının Ağ katmanı**\*** ve daha yukarısını kapsar. ( **\***' lı terimlerin tanımı için Bilgisayar Ağları başlıklı önceki yazıya bakabilirsiniz.)

Internet üzerinde verilerin akışını kontrol eden TCP/IP bir çok protokolün bir araya gelmesiyle oluşturulmuş olduğu için ona **protokol paketi** diyoruz. **TCP** bu protokol paketinin "Noktalar arası veri transferinde dikkat edilecek hususlar" kısmını yürütürken, **IP** ise "Verilerin taşınacağı yolun belirlenmesi" kısmıyla ilgilenir. TCP/IP sisteminin 7 katmanlı OSI yapısına uymadığı bunu tartışan kitaplarda belirtilir. Bunun ne gibi sorunlara yol açtığı bizi pek ilgilendirmiyor. Ancak şekilden de görebileceğimiz üzere yıllardır kullanageldiğimiz **telnet** veya **ftp** gibi servisler sadece bize arayüzde gözükmekle kalmıyorlar taşıma katmanına kadar olan bütün gürevleri tekbaşlarına hallediyorlar. Bu da tabii katmanları doğrudan doğruya ihlal etmek anlamına geliyor.

Bu arada aklımıza şu soru gelebilir: "Piyasada *CuteFTP*, *CoffeeCup* ya da *WS-FTP* gibi bir çok yazılım var ve bunlar aralarında birçok farklar bulunan programlar, nasıl oluyor da TCP/IP olarak bahsedilen standart paketin bir kısmını karşılayabilirler?". Burada ftp derken, Windows veya Unix sistemlerinde **Komut İstemi** ya da **Konsol**' dan klavye yoluyla verdiğimiz "ftp" komutundan bahsediyoruz. İsterseniz siz de bu yolla "ftp" komutunu vermeyi bir deneyin. Sonuç olarak adı geçen programlar bu standart servisin üzerine alacalı-bulacalı bir kıyafet geçirilmiş şekilleridir.

TCP/IP' yi anlatan kitapları karıştırdığımızda onun tarihi ile ilgili bazı bilgiler verilir. Ben de hatırımda kaldığı kadarıyla bunları derleyeyim. ABD' de DARPA adında askeri bir kurum bir nükleer savaş esnasında bile ayakta kalabilecek bir bilgisayar iletişim yapısı kurulması için çalışmalar başlatır. Bu projenin temel amacı, herhangi iki nokta arasındaki iletişimin kopması durumunda bile başka yollar üzerinden noktalar arası iletişimi devam ettirebilen bir sistem meydana getirebilmekti. Bu yazıda işin tarihi ya da edebi yanından çok bu noktası açıklanacak. Yani sistem bunu nasıl oluyor da yapabiliyor? Neyse bir kaç noktaya daha değinip bu faslı kapatalım. Daha sonra ABD çapında üniversite öğrencileri ya da akademisyenlerden oluşan bir yazılım grubunun uzunca bir çalışması sonucunda TCP/IP yapısı oluşturuluyor.

## **TCP/IP adreslemesinin analizi**

Bir seferliğine bu adresleme sistemini kendimiz kuracağımızı varsayalım. Dünyadaki tüm bilgisayarlara bir tekil adres vermemiz gereği, en öncelikli problemimizi oluşturmaktadır. Her isteyene istediği adresi verebilmemiz zaten imkan dışıdır. (Öyle olabilseydi muhtemelen **Yüzüklerin Efendisi**' ndeki karakterlerin isimlerini hangi torpillilere vermemiz gerektiği problemi, teknik problemlerin de ötesinde bir problem oluşturacaktı **:)** ) Tekil olma gereği, adreslerimizin en önemli özelliği olduğu için anlamlı kelimelerden oluşabilen adresleri, internetin büyüklüğü gözönüne alındığımızda doğrudan elememiz gerekiyor. "**www.teknohaber.net** adresi, anlamlı bir adres ama !" derseniz; ben de size internete bağlı her sistemin bu kadar şanslı olmadığını ve bu anlamlı isimlendirme sisteminin TCP/IP içerisinde, daha sonra değineceğimiz **DNS** adındaki özel bir yapı olduğunu söylerim.

Kullanacağımız adresin anlamlı kelimlerden oluşamayacağı veya kullanıcının tercihine bırakılamayacağı konusunda sanırım hemfikiriz. Bir konu daha var ki, internet her bilgisayarın bir adet büyük **orta göbeğe** bağlanıp oradan dallandığı bir yapı değildir.

Zaten böyle olması, başlangıçta izah ettiğimiz amaca da aykırıdır. Yani orta göbek çökerse tüm sistemin devre dışı kalması riski sözkonusu olur. İnternet, her gün biraz daha büyüyen dinamik bir yapı. Öyleyse bir çok orta göbeğin birbirine bağlı olduğu bir yapı hayal etmemiz daha doğru olur. Bu göbek yapıları da birtakım bilgisayar sistemleri olacağından ve birbirleriyle haberleşmelerini otomatik yollarla gerçekleştireceklerinden; adres yapısının bilgisayarlara kolaylık sağlayacak bir yönteme altyapı oluşturacak şekilde olması gereklidir. Sonuç olarak baklayı ağzımızdan çıkaralım: **adresler rakamlardan oluşmalı**. Çünkü rakamlara dayanan bir çözüm yöntemi -yani bilgisayarcı diliyle **algoritma**- kurmak programcılar açısından en kolayıdır. Diğer yandan teknik insanlar açısından da anlamsız harfleri akılda tutmaktansa, alakasız rakamları akılda tutmak daha uygun bir hafızalama yöntemidir. (Nasıl olsa bu alakasız rakamlara bile anlam yükleyecek bir akıllı her yerde bulunacaktır**:)** )

Evet, rakamlarda da karar kıldığımıza göre, yeni bir sürprize daha hazırlıklı olun. Rakamlar kendi içerilerinde anlamsal bazda gruplanacaklardır. Gruplanacaklardır ki; *hepsi değil ama bazı birbirine yakın rakamların*, daha sonra konumsal olarak birbirlerine yakın bölgelerde toplanmış bilgisayarları temsil etmeleri sağlanabilsin. Bir üniversite kampüsünde, bir şirkette, bir Internet Servis Sağlayıcısı' nda ya da -daha geniş düşünelim- bir ülkede; bulunan 10 ya da 100 ya da 100.000 bilgisayarın birbirlerini takip eden veya yakın değerleri temsil eden numaraları adres olarak almaları, veri paketlerinin bu bilgisayarlara ulaştırılmasını sağlayan yazılımlar için ya da bilgisayarlara servis götüren personel için ya da daha birçok değişik sebep yüzünden oldukça önemli bir kural olarak tanımlanmaktadır. Aksi taktirde birçok anlamsız rakam bir çorbadan başka birşey ifade etmeyecektir.

Yani bu gruplandırma yoluyla adresimizin bir bölümü **uç noktanın ait olduğu ağı**, geri kalan bölümü ise **uç noktanın kendisini** tekil olarak ifade edebilir hale getirilebilir.

Adreslerimiz günümüzde pratikte halen geçerli olduğu haliyle **32 bit**lik (2' lik sayı sisteminde 32 basamaklı) , az önce ifade ettiğimiz gibi kendi içerisinde gruplandırılmış sayılar ile temsil edilmektedirler. Internetin ilk tasarlandığı yıllarda, onu tasarlayanlara gayet yeterli gelen 32 bitlik rakamlardan oluşan adresler şimdilerde yetmemeye de başladı. Yeni nesilde karşımıza çıkacak olan **IPv6** (versiyon 6) adresleri 128 bit olacaklar. Bunu da bir extra bilgi olarak geçelim.

Bilgisayarlar rakamları ikilik düzende ele alırlar. 32 bit ile -Windows' un Hesap Makinesi' nde sizler için az önce taze taze hesapladım- **4.294.967.296** farklı alternatif adres oluşturulabilir. Ancak ileride anlayacağınız bazı sebeplerden dolayı bu adreslerin bir çoğu boşa gidiyor. Bu adresleri gösterimde **8' lik** gruplara ayırıyoruz. Hem gösterimde kolaylık oluyor;
(11111111111111111111111111111111 şeklinde bir rakam hiç de sempatik gelmiyor değil mi? Eee, yeni gelen bilgisayar nesline bu işleri çok zor olarak göstermemek lazım**:)** ) hem de her 8' li gruba farklı bir işlev yükleyebiliyoruz. Ve bu her 8' li grubu 10' luk düzende, aralarına noktalar koymak suretiyle gösterirsek 255.255.255.255 şeklinde bir hal alıyor. (Hah şimdi oldu işte!) Elbette böylesi daha kolay. Bu şekilde düzene soktuğumuz adrese ismini de verelim: **IP adresi**. Bir de bundan sonra her 8' lik grubu oktet adıyla çağıracağız. (Latincede 8 ile alakalı bir kelime olması lazım)

Bu şekilde oktetlerin bazısı uç noktadaki sistemi -ki node olarak tabir edilir- temsil ederken, bazısı da node' un ait olduğu bilgisayar kümesini, yani ağı temsil eder(oktetlere farklı işlevlerini de yükledik). Mesela **193.255.88.1** gibi bir adresi ele alalım. Bu adreste soldan itibaren *ilk üç oktet* -yani **193.255.88** kısmı- halen öğrencisi bulunduğum Erciyes Üniversitesi' ndeki tüm bilgisayarlarda aynıdır. En sağdaki oktetin değerinin ise, üniversite bünyesinde bulunan ayrı ayrı sistemleri temsil edecek şekilde değişkenlik gösterdiği gözlenir. Bu Erciyes Üniversitesi için bu şekildeyken, başka bir kurumda *ilk iki oktet* -**193.255** kısmı gibi- ağı temsil ediyor olabilir. Bazı kurumda ise sadece *ilk oktet* ağı temsil ediyor olabilir. *İlk okteti* ağ adresini temsil eden IP adresleri **A sınıfı** IP adresi olarak adlandırılmaktadır. Eğer *ilk ikisi* ağı temsil ediyorsa **B sınıfı**, *ilk üçü* temsil ediyorsa da **C sınıfı** olarak adlandırılırlar.

Tabii bu sınıfın tayini, iş başındaki teknik elemanların keyfine göre yapılan bir ayarlama değildir. Belirli kurallar yetkili kurumlat tarafından ayarlanmıştır. Mesela ilk okteti **1..127** arası olan adresler A sınıfı **128..191** aralığı B sınıfı ve **192..223** aralığı ise C sınıfı olarak belirlenmiş aralıklardır.

Bir A sınıfı adres aralığı içerdiği yaklaşık 16 milyon adres ile sadece bir kuruma ait oluyor. Sadece buna bakarak 4 milyardan fazla adresin nerelere gittiği ve IPv6 ya niçin ihtiyaç duyulmaya başladığı konusunda yorumlar yapılabilir.

## **ARP **

(Address Resolution Protocol - Adres Çözümleme Protokolü)

Adres Çözümlemesi' nden kasıt, karşı bilgisayarın *IP adresini* sisteme vermemize karşılık veri-hattı katmanından karşı makinanın *LAN adaptörü***\*** ne ait olan *MAC** adresini* elde etmektir. Veri-hattı/fiziksel katman protokolleri; yaygın olanları hatırlayacağınız üzere **Ethernet**, **Token-Ring**, **FDDI** idiler. Ve yine hatırlayacağınız üzere veri-hattı/fiziksel katmanlarında, ağ katmanı protokolleri (TCP/IP, Netbios gibi) adreslerinin hiç bir önemi yoktur. Bu adresler ethernet gibi protokoller tarafından, herhangi bir veriden farksız biçimde işlem görürler. Dolayısıyla LAN' ımızda yapacağımız her türlü iletişim için karşı bilgisayarın LAN adaptör kartının donanımsal adresini bilmemiz gerekiyor. Çünkü fiziksel bazda asıl iletişimi bu alt seviye katmanları yapacaktır.

İşte LAN üzerinden iletişime geçeceğimiz sisteminin, LAN adaptör kartının MAC adresini öğrenme işine **ARP** adı verilmektedir. Yapısal olarak son derece basittir. Yaptığımız iş bütün bilgisayarlara, aranan IP adresinin o makineye ait olup olmadığını sormak ve eğer ait ise MAC adresinin geri gönderilmesini istemektir.

*Şaka bir yana ARP, ağ üzerindei tüm sistemleri gereksiz yere meşgul ederek
sistem performansını olumsuz yönde etkiler.***

Bu arada şöyle bir soru akıllara gelebilir: "Her ulaşmak istediğimiz sistemin adresini tüm bilgisayarlara sormak önemli bir performansın boşa harcanmasını gerektireceği gayet açık iken, bunun yerine ağımız üzerinde IP adresi belli bir sabit bilgisayar kursak ve o bize ihtiyacımız olan adresleri sorunca söylese daha iyi olmaz mı?"

Bu sorunun cevabı şöyle verilebilir: LAN' larımız çoğunlukla basit amaçlarla kurulmuş ucuz sistemlerdir ve fazla bir performansa ihtiyaç duymamaktadırlar. Ve her LAN için bu tür bir sistemi kurmak ve gerekli servis desteğini vermek son derece maliyetlidir. Daha yüksek performansa ihtiyacı olan LAN' larda kullanlılan bridge vb. aktif cihazlar**\*** bu ihtiyacı başka bir yoldan çözmektedirler. Daha fazla bilgi için bir önceki yazıya bakabilirsiniz.

## **Routing - Yönlendirme**

Daha önce örnek olarak seçtiğimiz 193.255.88.1 adresinde **193.255.88** kısmının ağı temsil ettiğini söylemiştik. Evet, uç noktaları olduğu gibi, ağları da tarif eden adreslere ihtiyacımız vardır. Bir ağ adresi, uç noktayı temsil eden bitlerin yerine **0** koyulmak suretiyle elde edilebilir. Burada, sondaki **.1** rakamı hatırlayacağınız üzere **8 bittir** ve yerine **8 adet ****0** yerleştirildiğinde 10' luk sistemde de 0 'a dönüşür. **193.255.88.0**, ağ adresini temsil eder hale gelir. "**193.255.88.0 ağı**" diyerek ağımızı adlandırırız. Öyleyse her ağda bir adres ağ adresi yapılmak suretiyle harcanmış oldu. Ayrıca bir de **broadcast** (yayınlama) adresi vardır ki bu da kimselere verilmez. Bu adresi elde etmenin yolu da ağ adresini elde ederken 0 yerleştirdiğimiz yerlere bu kez **1** yerleştirmektir. Yani **193.255.88.255** elde ediyoruz. Eğer bu adresi hedef IP adresi yaparsak yayınladığımız mesaj o ağdaki tüm node' lar tarafından kabul görür ve değerlendirmeye alınır.

Bütün bunları gözönüne aldığımızda C sınıfı ağlarda 254 tane uç eleman tanımlanabileceğini hesaplayabiliriz. B sınıfı adreslerde 65534 node olabilir. A sınıfında ise yaklaşık 16 milyon adet uç IP olur.

Eğer bizim göndereceğimiz paketin sahibi bizim ağımızda değil de internet üzerinde başka bir ağda ise bu paket için ARP işlemi yapmayız. Paketimizi, makinemizde tanımı daha önceden yapılmış olan **gateway** (Çıkış Noktası)' e göndeririz. Gateway IP' sine sahip olan cihaz, bir bilgisayar olabileceği gibi **router** dediğimiz özel tasarlanmış cihazlar da olabilir. Yaptığı işe **routing** (yönlendirme) denir. Bu cihazın birden fazla arayüzü vardır. Her arayüzü farklı bir ağa bakar ve her arayüz baktığı ağa ulaşabilmek için o ağdan bir IP adresi alır. Üzerinde çalışan algoritmaya bakarak, bir arayüzünden aldığı paketi hangi arayüzünden göndereceğine karar verir. Göndereceği paketin hedefi, paketin gerçek sahibi olabileceği gibi, yol üzerindeki başka bir router da olabilir.

Paketin gittiği yolda, üzerinden geçtiği her bir router bir "**hop**" tur. Yönlendirme yöntemlerinden birinin sistemi; router üzerinde çalışan yazılımın algoritması tarafından her interface için hedef ağa varmak amacıyla kaç hop' tan geçmek gerektiğinin bulunması ve paketin yollanacağı yöne bu hop sayılarına bakarak karar verilmesine dayanmaktadır. Diğer başka bir yöntem ise her bir yöndeki ağ yoğunluğunun bulunmasıdır. Veri paketleri, yoğunluğu daha az olan interface üzerinden gönderilir. (Eğer bu konularda daha derin merakınız varsa, bu algoritmaların detaylı incelemesi için **Cisco** referans kaynaklarını bir yolla edinip inceleme yoluna gidebilirsiniz. Cisco sertifikasyonuna kadar gidebilecek sürecinizde yolunuz açık olsun. **:)** )

## **Subnet Mask - Alt Ağ Maskesi**

Bir başka mesele de makinamıza kendi ağ adresini ve göndereceği paketlerin hedef IP' lerinin ağ adreslerini bulmasını öğretmektir. Evet, router gondereceğimiz paketleri hedef ağa ulaştırmakla yükümlüdür ancak; haberleşeceğimiz bilgisayarla aynı ağda mıyız değil miyiz bunu bilgisayarımız bilebilmelidir. Aksi halde paketleri doğrudan veri-hattı/fiziksel katmana indirip daha önce üzerinde durmuş olduğumuz yöntemlerle mi hedef sistemle iletişime geçecek; yoksa paketleri gateway' e mi iletecek buna karar veremez. Bunun için kullandığımız yönteme maskeleme diyoruz ve IP adresine benzer bir 4 okteti daha bu işe ayırıyoruz. Bu 4 oktetlik rakamlar zincirine **Subnet Mask** denir. Ağ tanımlayan bitler **1**, node tanımlayan bitler **0** ile değiştirilirse o adres sınıfı için Subnet Mask elde edilmiş olur. C sınıfı IP' ler için standart subnet mask **255.255.255.0**' dır.

Kendi ağ adresimizin bulunması için; sistemimize, onu kurarken yaptığımız ayarlamalarımız sırasında bir parametre olarak tanımladığımız Subnet Mask yine çoğunlukla aynı süreçte tanımladığımız IP adresimizle bilgisayarımız tarafından **lojik AND** (VE) işlemine tabi tutulur(Her bir bit ayrı ayrı olacak şekilde - **bitwise and**). Merak etmeyin basit de olsa lojik görmemişler için alın size AND işlemi tanım tablosu.

Tablodan çıkartmamız gereken sonuç; **0' ın** birlikte işleme girdiği elemanı **yuttuğu**, **1' in** ise işleme girdiği elemanın **kopyasını çıkarttığı**dır. Yani 255.255.255.0 maskesi 193.255.88.1 IP adresi ile şu şekildeki gibi işleme girer.

Az önce de ifade ettiğimiz gibi 1' li bölgeler, IP adresindeki karşılık gelen bölgenin kopyasını çıkarmış, 0' lı bölgeler ise karşılık gelen bölgeyi 0' a çekmiş. Evet, IP adresinden ağ adresini Subnet Mask kullanarak çıkartmanın yolu bu...

Uygulama katmanımızdan TCP/IP katmanlarına 193.255.100.1 adresine gönderilmek üzere bir paket geldiğini düşünelim. Bizim IP adresimiz ise 193.255.88.1 olsun. Subnet mask ise C sınıfı olduğu için 255.255.255.0 . 255' li kısımlar ayırt edici kısımlar, yani ağ tanımlayıcısını belirleyen kısımlar olduğu için hedef ağ 193.255.100.0 olarak bulunur.

Kendi IP' miz için de aynı işlem uygulandığında 193.255.88.0 ağı olduğu görülür. İki ağın aynı olmadığı anlaşıldığı için paket gateway' e yollanır. Yok eğer Subnet Mask 255.255.0.0 seçilseydi, ağ tanımlayıcıları 193.255.0.0 olarak bulunacağından gateway' e gidilmeyecek, LAN protokolü üzerinden direkt olarak ulaşılmaya çalışılacaktı.

Ancak bu şekilde kafamıza göre Subnet Mask seçmeden önce iki kere düşünmek lazım: Mesela, yine 193.255.100.1 adresine gönderilmek üzere gelen bir paket için en son yaptığımız ayarlara göre hedef sistemle bizim sistemimiz aynı ağda gözükmekte olduğu için paket için ARP uygulanacak fakat böyle bir bilgisayar yerel ağda mevcut olmadığı için de ARP' a herhangi bir cevap alınamayacak, dolayısıyla hatalı Subnet Mask ayarından dolayı 193.255.100.0 ağı ulaşılmaz hale gelmiş olmaktadır.

Evet, az önce iki kere düşünelim dedik ama yapmayalım demedik. Kurcalamaya devam ediyoruz. Bir biti daha 1 yaparak Subnet Mask' ımızı değiştirelim. Bakalım ne olacak.

Merak etmeyin korakacak birşey yok. Bu noktada elinize kağıt kalem alıp, IP adresimizi Subnet Mask ile işleme sokarak biraz pratik yaparsanız dördüncü okteti 128' den küçük olan adreslerin ağ adresinin **X.X.X.0**, büyük olanların ise **X.X.X.128** olarak çıktığını tespit edeceksiniz. Önceden gelen tecrübemizle .127 ve .255 adreslerinin de, sırasıyla, bu ağlar için broadcast adresleri oldukları öngörüsünde bulunabiliriz.

Öyleyse bize C sınıfı olarak hediye edilmiş 254 adet kullanılabilir IP' yi biz bu bitlerle oynayarak ihtiyacımıza göre parçalara bölebilirmişiz. Mesela üniversitenin hem Kayseri' de hem Yozgat' ta kampüsü var. Ve bize yetkili kurum tarafından "Alın size C sınıfı bir IP aralığı. Ne yaparsanız yapın!" dendi. (Ki genelde -daha nazik bir uslupla da olsa- böyle denir.) Bu noktada 128' den düşük olan IP' leri bir kampüse, yüksek olanları da diğer kampüse atayarak ve araya da yönlendiriciler koyarak ve bu yönlendiriciler üzerinde gerekli ayarlamaları yaparak bu problemin üstesinden gelebiliriz.

Burada akıllara hemen şu soru gelecektir: -ki bu konuları ilk öğrendiğimde benim de aklıma gelmişti- "Niçin parçalara bölmek için zorluyoruz ki?" Evet, gerçekten de öyle. Niçin illa ki bölmek zorunda olalım. İki kampüs arasında noktadan noktaya bir bağlantı çekelim olsun bitsin. Değil mi?

Maalesef değil. Gözden kaçırdığımız ayrıntı teorikte değil pratikte başgösteriveren bir sorun. Yerel ağlarda bağlantı 10-100 Mbit' ler hatta Gbit' ler seviyesindeyken bir ARP yapmak ve sonuçlanmasını beklemek pek bir sorun oluşturmuyor. Ancak kampüsler arasına kuracağımız bir bağlantı hızı çoğunlukla Mb' ler seviyesinde değil Kb' ler seviyesinde olur. Bu da sizin gereksiz yere ARP paketciklerini 100' lerce km öteye taşımanız ve bu sırada yüzyüze geleceğiniz gecikme yüzünden ağ performansı diye birşeyden bahsedememenize demektir. Hem önceki yazımızda Aktif Network Cihazları başlıklı kısımda, aynı yerel alanda bile performans artırımı için mesaj süzme aktivitesinin önemini vurgulamışken, aralarında 10' larca km' ler bulunan bölgeleri illa ki birarada tutalım diye böyle bir performans problemine altyapı hazırlamak hatalı bir tutum olacaktır.

(Diğer bit kombinasyonları için toplam kaç adet ağ, kaç adet uç elde edebileceğinizi kendi başınıza hesaplarsanız, subnet mask üzerinde müdahale' de bulunma hakkınız içerisindeki 1 ve 0 ların adedine bağlı 2 adet formül bulabileceğinizi fark edebilirsiniz. Ne kadar çok ağ olursa o kadar çok adresin boşa gittiğini de fark etmelisiniz.)

## **TCP/IP' nin temel servisleri**

**DNS (Domain Name System)******

DNS servisi sayesinde internet uygulamalarımızı kullanırken, bağlanmak istediğimiz karşı sistemin IP numarasını bilmek zorunda kalmıyoruz. Örneğin, Internet Explorer' da www.teknohaber.net yazdığınızda biz farkında olmadan program, bir **DNS Server** sistemiyle bağlantıya geçer ve www.teknohaber.net sistesinin IP numarasını elde eder. Daha sonra da bildiğimiz prosedürü uygulayarak devam eder. Zaten bu şekilde olmuyor olsaydı, karşı sistemin konumunu ve ona ulaşmamızın yolunu elde etmemiz mümkün olmazdı.

Yalnız kendisinden hizmet aldığımız DNS Server' ın IP adresini bilmek zorundayız. Bundan 1 ya da 2 yıl öncesine kadar dial-up bağlantılarımızda da DNS Server ayarı yapmak mecburiyetinde kalıyorduk. Fakat yeni ortaya çıkan bazı kolaylıklar sayesinde dial-up bağlantıyı kurmamızla birlikte DNS bilgilerini de servis sağlayıcımızdan otomatik olarak alıyoruz.

**SMTP (Simple Mail Transfer Protocol)******

Bu servisin çalıştığı bir server üzerinden maillerimizi gönderiyoruz. Yani bu servis çoğunlukla PC' miz üzerinde değil bir server sistem üzerinde çalışır.

**POP (Post Office Protocol)******

Bu servisin çalıştığı bir server üzerinden mail alıyoruz ve maillerimiz bu serverda saklanıyor. POP ve SMTP hizmeti alabildiğiniz serverlardaki mail hesaplarımızı Outlook Express tarzı programlarla yönetebiliyoruz.

**FTP (File Transfer Protocol)******

Dosya transferi işlerini profesyonelce yaptığımız servistir. Orijinalinde bir sürü öğrenilmesi gereken ayrıntılı komutları ve özellikleri vardır. Ancak shareware ftp programları bizim için bu ayrıntıları bilme mecburiyetini ortadan kaldırmıştır.

**Telnet (Terminal Emulation)******

Internet üzerinden terminal emülasyonu sistemidir. Yani sistemimizi, uzaktaki başka bir sistemin terminali gibi kullanabildiğimiz bir servistir. Bu servisi kullanarak dünyanın öbür ucundaki bir sistemin monitöründeki görüntüyü görüyor, klavyesini kullanıyor gibi o sistemi kontrolümüz altına alabiliriz. Ayrıca terminal görüntüsü arabirimi üzerinden kontrol edilebilen **BBS** gibi yazılımlara da telnet servisi üzerinden bağlanabilmekteyiz.

**NEWS******

Haber grupları olarak da bilinir. Sistem yöneticisi tarafından açılmış konubaşlıkları altında kullanıcılar arasında bilgi alış-verişi maksatlı mesaj bırakma hizmetidir. Bir kişinin yeni oluşturduğu bir soru üzerine, bir çözüme ulaşılıncaya kadar o soruyla bağlantılı cevaplar bırakılması metoduyla çalışır. Bu servisin bütün dünya çapında etkileşimli birçok **news server**' ın birbiriyle online olarak çalıştığı bir sistem olan **Usenet **adındaki bir şekli de vardır. Usenet' in bir uzantısı olan yerel news server' ınızın üzerine bıraktığınız bir mesaj, belirli bir süre sonra dünya üzerindeki tüm Usenet news serverlarında yerini alır. Bu şekilde bütün dünyada belli bir konuyla ilgili kullanıcılar aynı sanal ortamda buluşmuş olur. Fakat son zamanlarda her web sietsinde görmeye başladığımız web tabanlı **forum **yazılımları news serverların yerini almakya başladı gibi görünüyor.

Tabii ki bütün bu servisleri kullanabilmek için server makinalarda bu servislerin başlatılmış ve çalışıyor durumda olmaları gerekmektedir. Yoksa internet üzerindeki her makineye telnet ya da ftp komutunu çekemezsiniz.

## **Firewall**

Firewall (ateş duvarı) şeklinde adını sıklıkla duyduğumuz şey, yerel ağın internet ile arasındaki iletişimi kontrol altında tutan, çoğunlukla yazılım tabanlı bir sistemdir. Yerel alanımıza internet üzerinden gelen veya yerel alanımızdan internete çıkan her bir paket firewall sisteminin kontrolü altında hareket etmektedir. Bu sistemin amacı yerel ağımızdaki veri güvenliğini sağlamak, onu dış dünydan gelebilecek ve failini bulabilmenin muhtemelen imkansız olacağı her türlü tehlikeli eyleme karşı korumaktır.

Firewall sistemleri üzerinde genellikle basit bir takım kurallar tanımlanır. Örneğin; dış dünyadan yerel alana doğrudan erişmek isteyen her türlü veri paketini düşürmek, yerel ağdan dış dünyaya erişmek isteyen hiçbir pakete müdahele etmemek vs. gibi...

Evet bazı temel kurallara hep beraber karar verebiliriz. Örneğin, dış dünyadan doğrudan gelen her türlü paket atılmalıdır. Eğer herhangi bir paketin masum bir amaçla bile olsa doğrudan içeri girmesine izin verilirse, kötü niyetli bir hacker bu yolu kullanarak yaptığı her türlü zararlı işi, bu görünüşte masum olan yolun içerisine gizleyebilir. Bu yolu kullanarak kötü amaçlarına ulaşabilir. Öyleyse temel kuralımız çok kesin ve sert olmalıdır. Dışarıdan gelen hiç bir **direkt paket** içeri giremeyecektir!.

Fakat diğer bir yandan bazı istemlerin içeriye girmesine müsaade etmeye de mecburuz. Çünkü **web server**, **ftp server**, **mail server** gibi kurumsal ağın bir takım parçaları dış dünyadan gelen istemlere cevap vermek zorundadırlar. Öyle ise ne tam iç dünya ne de tam dış dünya olarak tanımlayabildiğimiz bir ara bölge oluşturmalıyız. Bu bölgeye genellikle, askerden arındırılmış alan anlamından gelen **Demilitary Zone** kelimesi harflerinden **DMZ** adı verilir.

Şekilden de anlaşılabildiği üzere dış dünyadan bu bölgeye iletişim kısıtlandırılmıştır. Sadece o bölgede kurulmuş serverlara onların belirlenmiş port numaraları üzerinden erişime müsaade vardır. Bunun haricinde gelen paketler atılır. Kurumsal ağdan DMZ' ye olan erişimlere ise müsaade edilmelidir. Çünkü, örneğin herhangi bir kullanıcı maillerini kontrol etmek ve onları belki de yerel ağdaki kendi bilgisayarına kopyalamak isteyecektir.

DMZ' ten iç ağa girişlere de kesinlikle izin verilmemelidir. Çünkü bir hacker DMZ' deki kısıtlı hakların bir şekilde açıklarını yakalayarak DMZ' yi ele geçirebilir. Bu noktada içeriye geçiş için gene bir yol bulamamalıdır. Bu bilgilerden şunu da anlıyoruz ki bazı hackerların CIA, NASA vs. gibi yerlerin web sitelerine arada sırada gerçekleştirdikleri saldırılar, bu kurumların çok gizli bilgilerini de sızdırabildikleri anlamına gelmemektedir.

Şekilde her ne kadar içeriden dışarıya her türlü erişime müsaade ediliyor olarak gözükmekte ise de, son zamanlarda terörizm veya pornografik içerikli bölgelere olan erişimi kısıtlamaya dair eğilimler artmaktadır. Ayrıca dışarıdan içeriye download edilen dosyaların virüs ve trojan kontrollerinin yapılması da sıklıkla firewall' a yüklenen bir görevdir.

Buraya kadar verilen bilgilerden çıkarılacak bir sonuç da firewall' un aslında bir çeşit router olduğudur.

## **Sanal IP' ler ve NAT**

Interneti düzenleyen kurumların bir üniversiteye ancak C sınıfı bir IP aralığı verebiliyor olmalarına rağmen(çünkü uygun IP adreslerinden her isteyene istediği kadar verebilecek kaynak bulunmamaktadır), bir üniversitede 1000' lerce PC bilgisayar internet erişimine ihtiyaç duyabilmektedir.

Eğer internet üzerinde örneğin A sınıfı bir adres aralığına sahip bir kuruma bağlanamamayı göze alabilirsek bu IP aralığını kendi yerel alanımızda kullanmamızda teorikte bir mahsur yokmuş gibi gözüküyor (ki aslında öyle değil. Bizim paketlerimiz doğru adrese ulaşabilseler bile, karşıdan gelen bilgiyi routerlar adresin gerçek sahiplerine yönlendirecekler, onlar da böyle paketler talep etmedikleri için paketleri atacaklardır.) Öyleyse interneti düzenleyen kurumlar bazı adres aralıklarını kimseye vermeseler ve dolayısıyla da internet üzerindeki hiçbir router bu adreslere yönlendirme yapmasa bütün bu sorunlar ortadan kaldırılmış, teknik konfigurasyonlarda kullanılabilecek, ihtiyaç duyulan bu tür IP adresleri sağlanmış olur. Nitekim tarif ettiğimiz özelliklerde bir takım IP aralıkları, yerel alanlarda kullanılabilmek maksadıyla boş bırakılmışlardır. Bu aralıklardan bazıları **A sınıfı** için **10.0.0.0** ağı, **C sınıfı** için **192.168.16.0** ağı gibidir. Bu IP aralıklarındaki IP numaralarına **sanal IP** diyoruz.

Evet, bu adresleri sorunsuzca ve pervasızca yerel alandaki sistemlerimize dağıttık. Ama az önce sözünü ettiğimiz bir problem hala ortada duruyor. Bu paketler belki yerlerine ulaşacaklar ama geri dönüş yolunda paketler, kendilerine dünya üzerinde hiçbir router' ın (yerel router' lar dışında) yönlendirme yapmadığı ağları hedefleyen paketler nasıl olup da yollarını bulabilecekler?

Evet, demek ki bu paketlerin geri dönebilmeleri için paketin üzerinde yer alan ve kaynak IP adresini içeren bölgesinin gerçek bir IP adresini içermesi gerekmektedir. Öyleyse bizim firewall' umuza şöyle bi kabiliyet daha kazandırsak: Dış dünyaya giden her paketi gerçek IP aralığından belirli bir geçerli IP adresi içerecek şekilde yeniden düzenleyerek dış dünyaya gönderse ve cevap olarak gelen paketleri de tersi işlem yaparak doğrudan istemci sistemi hedefleyerek gönderilmiş gibi düzenlese... Tabii ki yapabiliyor. Bunun için o kadar para sayıp alıyoruz.

Firewall ya da router sisteminin yaptığı bu adres kandırmacası işlemine **Network Address Translation **(ağ adres çevirisi/dönüşümü) yani **NAT** adı verilir.

NAT aynı zamanda DMZ bölgesindeki serverlara da dış dünyadan gerçek IP adresleri atama prosedüründe kullanılır. Evet, dış dünyaya açık her bir serverımızın gerçek IP adresleri olması gerekmektedir.

Ayrıca, bu üç bölgenin de birbirlerinde farklı ağ adresleri olmalıdır ki firewall bu üçünün arasında gerçek manada bir yönlendirme işini kontrollü olarak gerçekleştirebilsin. Aksi halde örneğin, dış dünyaya kısıtlı bir açıklığı bulunan DMZ bölgesi bir hacker tarafından ele geçirilmiş olsa, bu hacker oradan da kurumsal ağ bölgesine rahatlıkla atlayabilir. Çünkü iki bölge de aynı ağda tanımlanmıştır şeklinde bir kabulde bulunmuştuk.

Bütün bu anlattıklarımızdan sonra, bir internet kafeye gittiğimizde niçin büyük olasılıkla 192.168.16.0 ağından bir IP adresimiz PC makinamıza atanmış olduğunu yorumlayabiliyor olmamız gerek. Çünkü internet kafelerin kullandıkları tek internet bağlantısını bir çok bilgisayara paylaştırma işini yapan cihaz olan **Ip Sharer**, firewall' un yerine getirdiğini söylediğimiz NAT işlemini gerçekleştiren bir elektronik aygıttır ve aynı teorik altyapıya dayanmaktadır.

**II. yazının sonu******

Bu sefer de yazımızı burada bitirelim. İnşallah bir sonraki yazının başlığını ATM - Asyncronous Transfer Mode yapmaya muvaffak olabiliriz. Hepinize başarılar dilerim. Umarım bu yazı birilerinin işine yarar.

---
*Kaynak: `TCP  IP ve FİREWAL/TCP.doc` — ekim kaya — 2004*
