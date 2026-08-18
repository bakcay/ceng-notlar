# WAN Teknolojileri

Network yazı-dizisine Mehmet Seckiner'in hazırladığı WAN Teknolojileri makalesi ile devam ediyoruz. Bu yazıda;Analog-Digital haberleşme,Çoğullama - Multiplexing,Frequency Division Multiplexing - FDM,Time Division Multiplexing - TDM,T1 / E1 iletim hattı,SONET/SDH X.25,Frame Relay konuları hakkında detaylı bilgi bulabileceksiniz.

## **WAN Teknolojileri - I**

## **Giriş**

Merhaba;

Aradan bu kadar zaman geçtikten sonra bu yazı dizisinin devamından ümidinizi kesmiştiniz biliyorum; ama araya okul mezuniyeti dahil bir çok iş girdi. Hiçbir bahanenin arkasına sığınmayarak bu gecikme için özür diliyorum. Yine ikazımızı yapalım: Bu makalenin hedefi wan teknolojileri hakkında temel bilgiler edinmek isteyen öğrenci seviyesindeki meraklılar ya da iş hayatına girdiği halde bilgi dağarcığına bu konuları da eklemek isteyenlere yardımcı olmaktır. Bir yan amaç da, WAN' larla alakalı karşımıza çıkması muhtemel dokümanları incelerken rastlayacağımız terimlere aşina olabilmek, hatta onların ne olabilip ne olamayacaklarını yorumlayabilmektir. Bu terimler için yeri geldiğinde parantez içerisinde hemen açıklamaları verilecektir.

Hep beraber birşeyler öğrenmek istiyoruz. Bu yazının içerebileceği hatalar ve eksikler peşinen kabulümdür.

Bir önceki yazının sonunu da, iki önceki yazı gibi ATM ile devam edeceğiz şeklinde bağlamıştık. Ancak yine olmadı. ATM' e bahis açmadan önce, daha önceki WAN teknolojileri olan X.25, Frame Relay vb. lerine de bir değinsek iyi olur diyerek internette araştırmalar yapmaya başladım; ki konu konuyu açtı. Ta telekomünikasyonun temellerine kadar gitmek zorunda kaldım. Merak etmeyin sizlere telefonun mucidi A. Graham Bell' den bahis açmayacağım. :) Ama telefon teknolojisinden girmek lazım mevzuyu iyi anlamak için...

## **Analog - Dijital Haberleşme**

Konuya ses iletişimini anlamaya çalışarak başlayacağız.

Analoji benzerlik demektir. Fiziksel olarak olmasa da yapısal olarak birbirine benzeyen, birbirini karşılayan sistemler birbirinin analogudur. Akım ya da voltaj ölçtüğümüz bir ölçü aleti görmüşsünüzdür. İstediğimiz büyüklük ölçüldükten sonra elde edilen veri, birbirinin analogu olan mekanizmalar arasında aktarıldıktan sonra kadran sınırsız hassasiyetli bir skala üzerinde ölçülen değere karşılık gelen bir noktayı gösterir. Buradan hareketle, analog işaretlerin bir özelliği de süreklilik ifade eden bir aralıkta sınırsız hassasiyette değer almalarıdır, diyebiliriz. Kaç ondalıklı hassasiyete kadar temsil edilebileceği, bizim mekanizmalarımızın ne kadar duyarlı olduğuyla alakalıdır.

Dijital bir ölçü aletinde sonuç elde edildikten ve ikili sayı sisteminde temsil edilebilecek dönüşüm uygulandıktan sonra elektronik bir yöntemle sonuç ekran(display) üzerine iletilir. Bu dijital bir iletimdir. Dijital işaretler önceden belirlenmiş bir basamak sayısıyla temsil edilirler ve verimiz bir kere dijitize edildikten sonra hassasiyete müdahale edebilme imkanı yoktur.

Analog ve Dijital ölçü aletleri

Pratik yaşamda her tür işaretin sınırsız hassasiyette analog işaretler olmaları sebebiyle, pratik hayattan gelen analog işaretlerin dijital işleme yapan bir sistemde herhalukarda dijital işarete dönüştürülmeleri ve işlendikten sonra tekrar analog işarete dönüştürülerek pratik yaşama aktarılmaları gerekir.

Yukarıdaki ölçü aleti örneğine benzer şekilde sesimiz de karşıya iletilmeden önce ölçülmelidir. Bu işi telefon ahizesindeki mikrofon yapacaktır. İnsan sesi analog bir işarettir. İnsan sesinin meydana getirdiği titreşimlerle mikrofonun sistematiği birbirinin analogudur. Mikrofon, sesi analog elektriksel işarete dönüştürür. Elektriksel işaret iletken kablolarla gidilecek hedefe taşınır. Hedefe ulaşıldığında mikrofonun yaptığı işlemin tersini yapacak bir hoparlör(speaker) analog elektriksel işareti ses işaretine dönüştürür.

Birden çok ses bilgisi iletilebilen hatta Trunk denir.

Burada önemli bir sorun elektriksel işarete dışarıdan gürültü dediğimiz bir takım ekstra sinyallerin karışarak orijinal işareti bozmasıdır. (Oda içerisinde yanan masum bir florasan lambasının işarete neler yaptığını, elektronik editörü arkadaşımız Emre Ceyhan' a sorabilirsiniz.) Ayrıca mesafe uzadıkça işaretin şiddeti zayıflar.

İşaret dijital olarak kodlandıktan sonra, bir takım matematiksel formüllerin işarete uygulanması ile elde edilen sayısal değerler işaretimize ilave edilir. İletimdeki hedef noktada aynı formüllerle verimiz tekrar test edilir ve sonuçlar karşılaştırılır. Eğer veri gürültüden dolayı bozulmuş ise elde edilen sonuçlar birbirini tutmayacaktır. Dolayısıyla doğru sonuca ulaşılana kadar veri tekrar tekrar transfer edilebilecektir. Bu dijital verilerdeki hata ayıklama yöntemleriden en çok kullanılan birisidir. Analog işaretlerde ise bu performansta bir hata ayıklama sözkonusu olamaz.

Gürültünün iki işaret türüne etkisinin bir yönü de analog işaretlerin pratikte tam anlamıyla engellenmesi imkansız olan gürültüye her şartta maruz kalmaları, aktarım esnasında az ya da çok orijinalliklerini kaybetmeleri durumudur. Dijital işaretlerde ise gürültü, işaretin ya 1 ya da 0 olabilen durumunu değiştirecek kadar kuvvetli olmadığı takdirde bir problem teşkil etmez. Durum değişmesi sözkonusu olması halinde de az önce ifade edilen veya benzeri yöntemlerle hata düzeltilebilir.

## **Çoğullama - Multiplexing**

Bir elektriksel iletim hattı sadece iki kişi arasındaki konuşmayı iletmek üzere ayrıldığı zaman önemli bir israf yapılmış olur. Çoğullama teknikleri kullanılarak bir hat üzerinden birden fazla bilgi simultane ya da sırayla iletilebilir. Analog işarette çoğullama yöntemi *Frekans Bölmeli Çoğullama - Frequency Division Multiplexing - FDM*; dijital işarette ise *Zaman Bölmeli Çoğullama - Time Division Multiplexing - TDM*' dir.

**Frequency Division Multiplexing - FDM**

(*bantgenişliği* - analog sinyal üzerinde en yüksek frekans ile en düşük frekansın farkına denir; dijital veride ise bantgenişliği tabiri kullanıldığında, hattın birim zamanda (saniyede) veri taşıma kapasitesi anlaşılmalıdır.)

(*ses kanalı* - bir dijital iletim hattında, bize dijital ses verimizi transfer edebilmemiz için tahsis edilmiş kısım. sanal bir kavram olarak algılanmalıdır. sözkonusu dijital iletim hattının birden çok ses verisini simultane (aynı anda) iletebildiği kabul edilmektedir.)

Bu çoğullama tekniğinde ses kanalının bantgenişliği üzerindeki parçalar herbir ses işaretine bölüştürülür. İnsan sesinin frekans aralığı yaklaşık 4 KHz olarak kabul edilir. İletim hattı 60-108 KHz aralığındaki sinyali taşıyabildiğine göre (108-60)/4 = 12 adet ses işareti taşınabilir demektir. Mesela, 60-64KHz aralığında birinci ses işareti, 64-68 KHz ikinci vs.

(VF - Voice Frequency - Ses Frekansı)

Analog ses iletiminde cross-talk dediğimiz komşu hatların yayınımlarından etkilenerek seslerin birbirine karışması olayıyla da sıklıkla karşılaşırız. Bazen telefonda konuşurken başkalarının konuşmalarının araya karışmasıyla gündelik olarak çoğumuzun farketmiş olduğu cross-talk, analog sistemlerin düşük ses kalitesini açığa vuran bir faktördür.

**Time Division Multiplexing - TDM**

Sayısal işaret süreklilik ifade eden bir fonksiyonla tanımlanamaz. Kesikli ya da ayrık adıyla ifade ettiğimiz bir fonksiyonla temsil edilir. Belirli bir zaman aralığında değişmeyen değerler alır. Değişim durumu ise ani ve keskindir.

Daha önce doğada işaretlerin analog olarak bulunduğunu belirtmiştik. Ve bu işaretleri işleyebilmek için dijital işarete dönüşüm uygulamamız gerekir. Analog ses işaretini dijitale dönüştürmek için PCM (Pulse Code Modulation) adıyla tanımlanan bir işlem uygularız.

PCM işlemi dört aşamada gerçekleşir. ***Filtreleme (Filtering)***** **- frekans aralığı dışına düşen sinyalleri süzer, ***Örnekleme (Sampling) ***- işaretin anlık değeri tespit edilir. Bu aşamada elde edilen sinyale PAM denir, ***Nicelik Belirleme (Quantizing) - ***alınan örnek 256 alternatif değerden biri ile temsil edilir, ***Kodlama (Encoding)*** - elde edilen değer bit serisine dönüştürülür. +45 için 10101101 gibi. (*sol baştaki 1*: işaret biti)

Burada Nyquist teoremini dikkate alarak bir hesap yapalım. Bu teoreme göre işaret bantgenişliğinin iki katı frekansında örnekleme yapılmalıdır. Ses işareti 4 KHz kabul edildiğinde 2x4000 = 8000Hz, saniyede 8000 örnek alınmalıdır. 256 alternatif işaret 8 bit ile temsil edildiğine göre, dijital ses transferi için 8x8000 = 64000bps = 64Kbps taşıma kapasitesine sahip bir ses kanalına ihtiyacımız olacaktır. Elde ettiğimiz bu işarete DS-0(Digital Signal - 0) denir ve bu; arkadaşlar, her yerde karşımıza çıkıyor. Onun için bilmek lazım.

TDM konusu bu kadarla bitiyor mu? Bitmiyor... Daha sonra elde edilen ses verisi, başka ses verileriyle ardarda eklenip birleştirilerek simultane iletilecektir.

(*PSTN* (Public Switched Telephone Network) - Amerikalıların anahtarlamalı telefon şebekelerine verdikleri ad. Public, kamusal demektir. Dileyen herkes ücretini ödemek suretiyle bu hizmetten yararlanabilir. Devlete özel ya da askeri amaca yönelik değildir. Switched, anahtarlamalı demektir. Eski filmlerde görüldüğü üzere santral memuru bize hat tahsis etmez. Anahtarlama otomatik anahtarlayıcılar yoluyla yapılır. Terimin ilk ortaya çıkış yeri Amerika olsa da her ülke için telefon ağına teknik anlamda bu isim verilebilir.

*IXC/LEC* (IntereXchange Carrier/Local Exchange Carrier) - Amerikan telefon altyapısında bizdeki gibi tek bir kurumun varlığı sözkonusu değildir. Şehiriçi/lokal telefon hizmetlerini ayrı ayrı küçük şirketler sunarken, ülke çapında uzun mesafe erişiminde sayılı büyük şirketler vardır. Ülke çapında uzun mesafe taşıyıcı firmalara IXC, yerel taşıyıcılara LEC denmektedir. Altyapının ilk dönemlerinde uzun süre American Telegraph and Telephone Company (AT&T) uzun mesafede tekbaşına söz sahibiydi. Daha sonra devlet müdahalesiyle bir takım düzenlemeler getirildi. Küçük taşıyıcılara ise Bell grubu şirketleri örnek gösterilebilir.

*POTS* (Plain Old Telephone System) - Eski basit telefon sistemi demektir. Genelde dokümantasyonda telefon ağının dijital veri için uygun olmayan, düşük veri taşıma performansına vurgu yapılmak istendiğinde kullanılan bir terim. İletişim altyapısının analog olduğuna da vurgu yapar.)

**T1 / E1 iletim hattı - Plesiokron Dijital Hiyerarşi (PDH)**

ABD' de (dokümantasyonlarda en çok karşımıza çıkan) *T1* (Trunk Level 1) dijital iletim hattı, standart olarak benimsenmiştir. Bu standart 1960' lardan beri telefon şirketlerinin merkez istasyonları arasında yüksek kaliteli sayısal ses işaretinin aktarımı için kullanılmaktadır. *E1* (European 1) bu standardın *ITU-T *(International Telecommunications Union) tarafından dünya standardı olarak yeniden düzenlenmiş halidir.

*Channel Bank* adıyla anılan bir cihazın kullanımıyla 24 adet ses verisi birleştirilir ve ayrıştırılır. Ayrıca channel bank ile T1 hattı arasına, hattı sonlandırmak için *CSU* (Channel Service Unit) cihazı yerleştirilmelidir.

24 adet kanal, kanal başına 64000 bps veri olduğu gözönüne alınırsa 24x64000 = 1.536 Mbps yapar. Fakat bu T1' in kapasitesi için doğru bir hesaplama değildir. Çünkü 24 adet 8 bit ses örnekleri birleştirildikten sonra *framing bit *(çerçeveleme biti) adı verilen bir bit ilavesi yapılır. (24x8)+1=193; 193x8000 = 1.544 Mbps gerçek T1 bantgenişliğini verir.

Şekilde de görüldüğü gibi T1 kablolaması iki adet bükümlü çift teldir. TX-Transmit, RX-Receive

Dijitize edilmiş birden çok veri kanalı, basit bir şekilde sıraya dizme mantığı (bir ondan, bir bundan - round robin) ile birleştirilir.

Eğer T1 hattı veri aktarımı için kullanılacaksa, channel bank ve CSU yerine *CSU/DSU* cihazı kullanılır. Takip eden şekilde de görüldüğü gibi T1 kullanımı ile noktadan noktaya LAN bağlantısı kurulabilmektedir. Biraz dikkatli arkadaşlar, *Napster*' ın parladığı dönemlerde T1 bağlantısının T1/LAN olarak ifade edildiğini ve bu bağlantıya sahip olan kullanıcılardan gayet yüksek hızda veri transferi yapılabildiğini hatırlayacaklardır.

T1 standardı 1980' lerden beri veri aktarımı için de kullanılmaktadır.

T1 sisteminde bantgenişliği sadece veriye ya da sadece ses iletimine tahsis edilmek zorunda değildir. Hem veri hem ses iletilecek, hatta video konferans uygulamaları da gerçekleştirilebilecek şekilde belirli oranlarda bölüştürülebilir. Buna *Fractional T1* denir.

T1' in Amerikan, E1' in dünya standardı olduğunu daha önce söylemiştik. Japon standardı da J1 olarak biliniyor ancak çok fazla karşılaşmıyoruz ve bizi pek de ilgilendirmemekte. Genelde teknolojik gelişmelerin ilk uygulama alanı Amerika oluyor ve bu da standartlaşmanın çoğunlukla ilk olarak Amerikan *ANSI *(American National Standards Institute) tarafından ele alınmasına sebebiyet vermektedir. Genelde daha sonra Avrupa işi ele alır ve ITU (eski *CCITT *- Consultative Committee on International Telephone and Telegraph) tarafından dünya standardı adıyla standardize edilir. Fakat Amerika her halukarda kendi standardını kullanmaya devam eder. Bu televizyon görüntü standartlarında da böyle (NTSC - PAL), az sonra ele alacağımız SONET/SDH' da da böyle. Belki benim bilemediğim bir çok alanda da sözkonusu olabilir. Tabii bizim işimiz burada bunu tartışmak değil, aynı konuda neden farklı standartlar olduğuna dair kafa karışıklığı oluşmamasına yardımcı olabilirsek yeterli...

Tabloda T1 için, nadiren de olsa karşımıza çıktığı şekliyle DS1 ifadesine de yer verilmiş. E1 içinse eşanlamlısı CEPT1' e de yer verilmiş...

Yukarıdaki tabloda E3 de dahil olmak üzere ilk bölüm PDH' i tarif eder. Az önce tarif ettiğimiz T1/E1 yapıları da kendi içlerinde çoğullanarak tablodaki yapıları meydana getirebilirler.

Başlığımızda T1-E1 için *Plesiokron* (Plesiochronous) terimini kullanmışız. Bu terim, iletişim kuracak iki dijital sistem arasındaki saat frekansı uyumunu belirten bir terimdir. Biliyorsunuz (ya da artık bilmeniz gerekir) ki sayısal sistemlerde 1' ler 0' ların belli bir sıklıkta (frekansta) durum değişimine uğramaları gerekir. Bu durum değişimini tetikleyen elektriksel işarete de *saat işareti* (clock pulse) denir. Bilgisayarlarımızın hızını da belirleyen (500MHz-2GHz gibi) bu işaret, haberleşme esnasında ileteceğimiz sinyalin dahi frekansını belirleyen unsurdur. (Biz clock' u dilediğimiz frekansa ayarlayabiliriz. Ama işlemcimiz çalışır mı çalışmaz mı önemli olan budur: overclock olayı) Maalesef pratikte birbiriyle tıpatıp aynı frekansta (küsuratıyla beraber) işaret üretebilen *saat işareti üreticileri* (clock pulse generator) yapabilmek imkansızdır. İhmal edilebilecek kadar yakın olanlarını yapmak ise çok pahalıdır. Dolayısıyla gönderen tarafın ilettiği işaretle bizim algılayışımız arasında bit kaymaları oluşacak (bit kaçırma ya da aynı bitin iki defa alınması şeklinde), bir noktada işaret bozulacaktır.

(*Plesiokron (Plesiochronous)* - latinceden gelir ve yakın zamanlı demektir. Gönderen ve alan tarafların saat işaretlerinin birbirine yakın saat frekansında çalışmasını belirten bir terimdir.)

(*Senkron (Synchronous)* - latinceden gelir ve zaman birlikteliği demektir (*eşzamanlı* olarak da çevrilebiliyor). Gönderen ve alan tarafın en azından ortalamada aynı frekansta çalıştıklarını belirtir. İşaretler arasındaki faz uyumu hassas şekilde kontrol altındadır. Senkron çalışmayan sistemler *asenkron* (asynchronous) sistemler olarak tarif edilir.)

**SONET/SDH (Synchronous Optical NETwork - Synchronous Digital Hierarchy)**

SONET/SDH, az önce standartlar bölümünde kısmen ayrıntısına girildiği gibi; burada da SONET,ANSI / SDH,ITU standardı olmak üzere, fiber optik kablolama altyapısını kullanan senkron sayısal iletişim standartlarıdır.

Fiber optik kabloların ortaya çıkması ve bununla ilgili dijital iletişim uygulamalarının ortaya konmaya başlamasıyla birlikte, standart belirleyen kurumlar üzerinde fiber optik altyapı için standart belirlenmesi talepleri yoğunlaşmıştı. Bu yeni ortaya konacak standartlarda PDH standartların eksik yönlerinin de kapatılması gözönüne alınacaktı.

(*bit stuffing* - temeli PDH' in tam senkronize çalışmamasına dayanan, senkronizasyon problemlerinin önüne geçebilmek için veri bitleri içerisine, bilgi değeri taşımayan bitler ilave edilmesi tekniği. Sözkonusu bitler multiplexing (mux) işlemi esnasında ilave edilir. Bu teknik, demultiplexing (demux) yapılmadan veri bitlerine erişebilmeye engel oluşturur.)

PDH' in ilkbakışta ortaya çıkan yetersizlikleri şunlardı:

PDH' da bit stuffing tekniği kullanılması dolayısıyla, tek bir DS-0 kanalına ulaşabilmek için her bir mux aşamasına karşılık demux işlemi yapılmak zorunda kalınmaktadır. Bu, özellikle hiyerarşinin üst seviyelerinde büyük problem oluşturur; çünkü hiyerarşinin her basamağı ayrı bir mux/demux işlemidir.

PDH' in yönetilebilirlik özellikleri patentli uygulamalardı ve bu önemli bir yönetilebilirlik sorununu beraberinde getiriyordu. Kolay yönetilebilirlik özellikleri de yeni standartlar çerçevesine alınmalıydı.

Yeni standartların tanımlanması, birçok farklı üreticinin ürünlerinin birarada sorunsuzca kullanılabilmelerini sağlamalıydı.

Drop & Add işlemi DS-0 kanalına yapılan ekleme/çıkarma müdahalesini temsil ediyor.

SONET/SDH standartlarının en stratejik özelliklerinden biri senkron olmasıdır. Senkronizasyonun sağlanabilmesi için saat hassasiyetini belirleyen çeşitli *stratum* (yine latinceden gelen bir kelime) seviyeleri tanımlanmıştır. Buna göre stratum seviyesi daha düşük olan bir cihaz daha yüksek olan bir cihaza göre clock durumunu ayarlar.

Şekilde görüldüğü gibi en yüksek seviyeli clockun hassasiyeti yılda sadece 2.5 bit kaymasıdır.

Network içerisinde kendisi referans alınarak clock ayarlaması yapılan en yüksek seviyeli saat *Primary Reference Source* (PRS) olarak tanımlanır.

SONET/SDH' da bit stuffing yoktur; mux/demux işlemine gerek olmadan doğrudan DS-0 kanalına erişim mümkündür. Kolay yönetilebilirlik özelliklerine sahiptir (OAP&M - Operations, administration, maintenance and provisioning). DS-1, PDH' deki temel çoğullanmış sinyalin adı olduğu gibi SONET' de temel sinyal OC-1 ya da STS-1 olarak karşımıza çıkıyor ve 51.840 Mbps bantgenişliği sağlıyor. SDH' da temel sinyal STM-1' dir ve bantgenişliği 155.520 Mbps bantgenişliği sunar. SONET aynı bantgenişliğini OC-3/STS-3 sinyali ile yakalamaktadır. Fakat her ne kadar aynı bantgenişliğinde olsalar da STS/STM çerçeve yapıları farklıdır. 155 Mbps kapasite, çokca karşımıza çıkan popüler bir kapasitedir.

Evet, buraya kadar gördüklerimiz temel altyapı sistemleriydi. Bir nevi Fiziksel ve Veri hattı katmanlarını gördük.

**Devre Anahtarlama / Paket Anahtarlama - (Circuit Switching / Packet Switching)**

Eğer iki nokta arasında kurulan iletişim kanalı veri aktarımı tamamlanana kadar kesintiye uğratılmadan açık bırakılıyor, bir açıdan işgal ediliyorsa bu tür iletişime *devre anahtarlamalı iletişim* (circuit switched communication) denir. Bir nevi iki nokta arasında sanal bir kablo varmış gibidir. Klasik analog ses iletişimi bu başlığa dahil olduğu gibi T1 gibi bir dijital iletişim altyapısında da kanal işgali sözkonusudur.

Paket anahtarlamalı bir ağ altyapısı ise öncelikle veri transferi maksadıyla kurulmuş bir altyapıdır. Paket anahtarlamalı yapılarda veriler paketler olarak adlandırılan küçük parçalara bölüştürülmüştür ve parçalar iki nokta arasındaki yollardan hangisi o an için en uygunsa o yolu tercih ederek hedefe ulaşırlar. Bu durumda gönderilecek verimizden bir kısım paketler belli bir yolu tercih etmiş durumdayken bir kısım paketler başka bir yoldan hedefe yönlendirilmiş olabilirler. Bu tür bir durumda, hedefe ulaşıldığı noktada paketlerin sırası karışmış da olabilir. Hedefteki alıcı bu paketleri, kullanılan protokolde tanımlanan yöntemlere göre orijinal sıralarına koyar.

Paket anahtarlamada bazen bir takım paketlerimizin taşındığı yol üzerinde geçici aksaklıklar yaşanabilir ve bu veri transferinde geçici kesilmelere sebebiyet verebilir. Fakat veri transferi bu tür kısa gecikmelere karşı son derece hoşgörülüdür. Halbuki ses, video ve benzeri zaman-kritik uygulamalarda, yerine zamanında ulaşmayan bir veri paketi, seste çatlama/bozulma vb. problemlerle görüntüde de kayma/atlama vb. bozulmalara sebep olabilmektedir.

Ses transferi, *VoIP* (Voice over IP) gibi yöntemlerle paket anahtarlamalı internet altyapıları üzerinden taşınır hale getirilmedikçe; onların dijital altyapılarla taşınmaları, bizleri, paket anahtarlamalı olarak taşındıkları gibi yanlış yorumlara sevketmemelidir.

**X.25**

Bir firmamız olduğunu ve İstanbul, Ankara ve Kayseri gibi merkezlerde şubeleri olduğunu varsayalım. Aynı şehirde aynı santrale bağlı iki firma bürosu için, bürodan santrale iki hat satın almak ve bu hat üzerinden bürolar arası veri transferi yapmak belki mali açıdan kabul edilebilir görünebilir ancak iki şehir arasında bir iletişim kanalını boşta bırakıp bir kimseye tahsis etmek, bir telekom şirketi için çok maliyetli bir şeydir ve telekom bu maliyeti kullanıcıya yansıtacaktır.

Halbuki paket anahtarlamalı bir ağ yaklaşımıyla bu maliyet bir çok kimseye bölüştürülebilir ve firmalar ve özel/tüzel kişiler için maliyeti daha uygun uygulamalar gerçekleştirilebilir.

X.25, 1970' li yıllarda henüz yüksek performanslı dijital iletişim yöntemlerinin yaygınlaşmadığı dönemlerde tavsiye edilmiş bir ITU standardı paket anahtarlamalı veri ağıdır (PSN - Packet-Switched Network). Fiziksel katmanda istenen güvenli veri iletişim düzeyi yakalanamadığı için iletişimindeki hata denetim özelliklerini de kendi bünyesinde barındırır.

X.25' in, ilk ortaya konduğu yıllarda PSTN telefon şebekesinin ses iletiminde ortaya koyduğu popülarite ve yaygınlık ölçüsünde veri şebekesi olarak yaygınlık ve popülariteye ulaşacağı öngörülmüştü. Ancak özellikle Amerika' da istenen başarıyı yakalayamadı.

Güvenilir dijital iletim ortamları için gereksiz olan bu hata denetim özelliklerinden dolayı düşük performanslı bir protokol olarak bilinir. OSI' nin ilk üç katmanında tanımlanmıştır. Kullanıcı sistem üzerinde kanal işgal ederek değil paket transferi yaparak kaynak tüketeceği için bu tür bir paket anahtarlamalı sistemde, transfer edilen paket üzerinden ücretlendrme yapılacaktır. Bu da özellikle noktalar arası veri transferi sınırlı kullanıcılar için büyük avantaj oluşturacaktır. Sistem ses bandı modemlerle 19.2 Kbps, baseband modemlerle 64 Kbps ile bağlantıyı destekler.

X.25, *DTE* (Data Terminal Equipment), *DCE* (Data Circuit-terminating Equipment) ve *PSE* (Packet Switching Exchange) arasındaki veri iletişim ilişkilerini düzenleyen bir protokoldür. DTE, ağa bağlanarak veri iletişim hizmetinden yararlanacak olan kişisel bilgisayar, terminal ya da network host türü (server gibi) bir donanım olabilir. DCE, devre sonlandırıcı modem cihazı olup ağ ile DTE arasındaki arabirimdir. PSE kavramı, ağ üzerindeki anahtarlayıcılar olarak düşünülebilir.

X.25 ayrıca, ATM sistemlerinde de inşallah ele alacağımız *sanal devre* (virtual circuit) yaklaşımının ilk defa karşımıza çıktığı standarttır. Bu yaklaşıma göre iki nokta arasındaki fiziksel devre (veri hattı) üzerinde birden çok sanal devre tesis edilir. Sözkonusu sanal devreler iki nokta arasındaki iletişimin sona ermesiyle birlikte sonlandırılır. Ve başka DTE' lerin ihtiyacına hizmet vermek için yeni sanal devreler kurulabilecek kaynak oluşturulmuş olur.

Çoğullama yoluyla sanal devrelerin tek bir fiziksel devreyi paylaşmaları

Bu sanal devrelerden bazıları sistem tarafından o an boşta olan kaynakların düzenlenmesiyle tahsis edilir ki buna SVC (Switched Virtual Circuit) denir. Aralarında sıklıkla bağlantı kurulan noktalar içinse sistem yöneticisi tarafından kalıcı sanal devre olan PVC (Permanent Virtual Circuit) tanımlamak mümkündür. PVC tanımlanan noktalar arasında, daima aktif olup hiç sonlandırılmayan bir oturum sözkonusudur. Çünkü sıklıkla oturum açıp sonlandırmak da bir performans kaybıdır.

**Frame Relay**

Frame Relay, asıl olarak ISDN arabirimi üzerinde kullanılmak üzere tasarlanmıştır. ISDN' i bu yazıda ele almayacağız ancak güvenli bir altyapı olarak düşünebiliriz. Dolayısıyla X.25' in içerdiği hata denetim mekanizmalarını içermez. Bu da onu daha performanslı ve verimli bir protokol yapmaktadır. Hata denetimini üst katman protokollerine bırakacak şekilde OSI' nin alt iki katmanında çalışır. Yüksek performanslı yapısı, FR' i noktadan noktaya LAN arabağlantısı için daha uygun bir seçim yapar.

İlk standartlaşma 1984 yılında CCITT tarafından teklif edildi. Standardizasyonun tam oturmaması yüzünden 1980 sonlarında kadar geniş bir şekilde uygulama alanı bulamadı. Daha sonra 1990 yılında Cisco, DEC, Northern Telecom gibi firmaların katılımıyla Frame Relay forumu oluşturuldu ve forum başlangıçta teklif edilen standartları sektörün desteğini alacak şekilde genişletti. Tüm bu genişletmelere toptan *LMI* (Local Management Interface) denir. (ATM' de de karşımıza çıkacak bu terim.)

Yine X.25' de olduğu gibi DTE ve DCE tanımları vardır. PVC ve SVC yaklaşımı sözkonusudur.

Frame Relay' de ileri ve geri yönlü sıkışma kontrol mekanizması vardır. Ağ üzerinde belli bir noktada veri yoğunluğu kaynaklı sıkışma oluştuğu zaman bu mekanizma yoluyla diğer anahtarlayıcılar sorundan haberdar edilir. Sıkışmayı bertaraf edebilmek için transfer edilen bir takım paketler üzerindeki *DE *(Discard Eligibility - Atılmaya Uygunluk) bitinden istifade edilir. Bu bit ile diğer paketlere göre önem seviyesi daha düşük olan paketler belirlenerek atılabilir (discard). Ve bu sayede sıkışma ortadan kaldırılmış olur.

Frame Relay' de hata tespit mekanizması yok değildir. Bu maksatla ilk başta belirttiğimiz matematiksel formülasyona dayalı hata tespit yöntemi olan *CRC* (Cyclic Redundancy Check) kullanılır. Fakat, bu hataların düzeltilmesi yerine hatalı paketlerin atılması yöntemi benimsenmiştir.

**Türkiye Altyapısı**

Türkiye' de paket anahtarlamalı ağ için ilk ticari girişim, Turpak Türkiye Paket Anahtarlamalı Kamusal Ağı' dır. X.25 altyapısını kullanır. Daha sonra başarısızlıkla sonuçlanan Turnet girişimi olmuş en sonunda internet altyapısına da tatminkar çözüm getiren TTNet, yüksek performanslı ATM omurgasıyla kurularak faaliyete geçirilmiştir.

Türkiye TTNet altyapısında, yüksek performanslı ATM omurgası kullanılmaktadır. Ayrıca üniversitelerarası akademik ağı ULAKNET omurgası da yine ATM üzerindedir. ATM konusunda ayrı bir yazı yazacağım; artık bu şart oldu. Ancak omurgayı anlayabilmek için ATM' in bilinmesi mecburiyeti yoktur.

Bunun için TTNet Hakkında başlıklıklı TTNet web sunucularında yayınlanan sayfaya kısaca bir göz atalım. Bu sayfada mesela yurtdışı bağlantı hızlarından bahsediliyor. Bu hızların nereden kaynaklandığını bu yazı yardımıyla bulabilirsiniz. ATM ile birlikte ayrıca ISDN, ADSL ve KabloTV erişimlerinden bahsetmedik. İmkanlarımız şimdilik bu kadar elverdi. Ve ileride bahsedebileceğimize dair bir garanti de maalesef veremeyeceğim.

Sayfanın en alt kısmında bir PowerPoint-ppt sunumu linki var. Bu link yardımıyla ulaşılan sunumda telekom, sunduğu hizmetler beraberinde altyapısını da anlatmış. İndirip incelemenizde fayda var. Bu sunumdan bir görüntüyü sizler için yakaladım.

Bu görüntüde STM1 ve E3 göze çarpıyor. Bunların ne olduğunu yine bu yazı yardımıyla anlayabilirsiniz. Ve niçin STS3 ve T3 olmadıklarını da...

Şu anda görülen o ki hızı sınırlayan temel faktör kullanılan SDH sinyalidir. ATM omurgasını oluşturan anahtarların veri anahtarlama kapasiteleri müsaade ettiği sürece geçerli SDH arabirimini terfi ettirerek hızın arttırılması teoride mümkün görünmektedir. Ancak merkezdeki anahtarlayıcı yeterli kapasiteye sahip değilse hattaki böyle bir kapasite artırımı istenen sonucu vermeyecektir. Bunu şöyle anlayabiliriz: bir kavşağa giden yollar trafik sıkışmasından dolayı genişletilebilir. Ancak kavşak merkezinde araçların rahat hareket etmelerine imkan verecek genişlikte bir göbek mevcut değilse bu trafik sıkışıklığı problemine çözüm getirmez.

Yukarıda getirmiş olduğum yorumlar tamamen şu ana kadar incelemiş olduğumuz temel teoriler ışığında yapmış olduğum yorumlardır. Ancak her zaman olduğu gibi pratikte akla gelemeyecek nice sorunlar mevcut olabilir. Eğer konunun profesyonelleri yorum getirecek olurlarsa, site yöneticisi arkadaşlar eminim ki bu yazıya onları da ilave edeceklerdir. Başta da belirttiğim gibi hep beraber bir şeyler öğrenmeye çalışıyoruz. Bir sonraki yazının başlığını ATM olarak atabilmek dileğiyle; Sağlıcakla...

**Yararlanılan Kaynaklar**

Internette her türlü bilgi arama faaliyetinde olduğu gibi Google vb. motorlardan incelemelerimize başlıyoruz ama maalesef ilk önümüze gelen kaynaklar çoğunlukla aradığımız şey olmuyor. Belli bir zaman sonra, içeriğini aradığınız bilgilere odaklanmış bir siteye rastladığınızda oradan faydalı linkleri takip ederek konunun piri/başucu kaynağı vb. diyebileceğimiz sitelere/bilgilere ulaşabiliyoruz. Ben de tam bu uzunca araştırma ve bilgiye ulaşma sürecini sonlandırdığımı düşündüğüm noktada Marconi nin web sayfasındaki ücretsiz eğitim bilgileriyle karşılaştım. Ve ilk başlangıçta o siteye ulaşamadığım için epey hayıflandım. Çünkü faydalı bilgiler elde etmenin yanında, gerçekte öğrenmek istemediğim birçok ayrıntı ile de boğuşmak zorunda kalmıştım; istediğim belki de bir paragraflık öz bilgiye ulaşabilmek için. Asıl istenen öz ve özet bilgiyi en derli toplu şekilde veren ve var olabilecek olan eksiklikleri çok iyi bir şekilde kapatan bir kaynak konumunda bu site. İngilizcesi yeterli olan ve konuya azbuçuk vakıf olan arkadaşlar ilgileniyorlarsa başka yerlerle çok boğuşmadan orayı da incelemelerini tavsiye ederim. Göz atmadım ama WAN haricinde LAN' lar hakkında da eğitim bilgileri var. Yüklü meblağlar ödenerek satın alınan eğitimlere inat, o ayarda ücretsiz bir site. İlgilenenlere...

Ayrıca:

Web ProForum Tutorials, http://www.iec.org/online/tutorials/
Fundamentals of Telecommunications, SONET/SDH (Tektronix)

TelecomWriting.com, http://www.telecomwriting.com ya da http://www.privateline.com

Pulse Inc. - T1 Networking Made Easy, http://www.pulsewan.com/data\_101.htm

A Historical Perspective on Telecommunications Network Synchronization, Stefano BREGNI

cs.williams.edu Digital Transmission ders notları

pulsewan.com' sitesinden yayınlanan Cisco X.25 ve Frame Relay Tutorial' leri

Veri Haberleşmesi Kavramları, Yasin KAPLAN, Papatya Yayıncılık

Chandler-Gilbert Community College, Homepage of Data Communications (CIS270) http://cgcc.williamson.cx

Bunlarla beraber konuyla alakalı guru derecesindeki isimlerden biri olduğu aşikar olan Prof. Raj Jain' in internet üzerinde online dersleri sesli ve sesli/görüntülü RealMedia formatında bulunabiliyor. Ancak ulaşmayı en çok istediğim bölümlerin ZIP dosyaları birkaç kere download denememe rağmen sürekli CRC hatası verdiler. Bir noktada pesetmek zorunda kaldım. Yine de ilgilenenlerin bilgisine.

**Son bir söz**

Bilgisayar Bilimleri en önemli hobilerimden birisi. Bu yazıyı hazırlarken bir sürü dokümanı tekrar tekrar incelerken inanın hiç sıkılmadım. Özellikle de senkronizasyon ile ilgili kısım gerçekten çok ilgimi çekti ve incelemesi en zevkli konulardan biri. O konuyu da arayı fazla uzatmadan ayrıca bir yazıyla ele almak istiyorum. cs.williams.edu' daki sayfalar konuya çok güzel bir giriş yapıyor fakat tam senkronizasyonla ilgili kısımlara geldiğinde eksik kalmış ya da bırakılmış. Elimde olan Van Steen/Sips, Computer and Network Organization kitabı konuyu daha ileri götürüyor ancak sonlandırmıyor. Eğer Tanenbaum' un Computer Networks' u gibi kapsamlı bir kitaptan konuyla ilgili kısımları inceleyebilme fırsatım olursa sanırım tutarlı bir bütünlüğü olacak şekilde bir yazıyı tamamlayabilirim. Hepinize güzel günlerde, güzel başarılar diliyorum.

---
*Kaynak: `WAN TEKNOLOJİLERİ/WAN TEKNOLOJİLERİ.doc` — ekim kaya — 2004*
