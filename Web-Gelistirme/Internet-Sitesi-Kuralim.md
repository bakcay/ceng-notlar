# İnternet Sitesi Kuralim

## Internet'e Çıkmak

İşin asıl zevkli tarafı olan Web sitesi oluşturmaya ve bunu Internet'e açmaya geçmeden önce Web'de "ne yapacağınız" sorusuna cevap aramak zorundayız. Bu soru şu anda belki çok anlamsız görülebilir. Ama Web'te neler yapılabileceğini sıraladıktan sonra, bu soruya gerçekten bilinçi bir şekilde cevap aramamız gerektiğini göreceksiniz.

Internet bir teknoloji yumağıdır. Bu teknoloji, TCP/IP protokolüne dayanan bir dosya aktarma sisteminde, HTTP protokolüne uygun bilgisayar dosyalarının bir ağ ortamında bir merkezden o merkeze bağlı bilgisayarlara aktarılmasını sağlar. Bu teknolojiyi, bugün Internet dediğimiz ortamda (ağlar-arası ağ) yapabileceğiniz gibi, bir şirketin Yerel Ağ ortamında da yapabilirsiniz. Buna intranet (ağ-içi ağ) denilir.

Internet'teki Web alanlarından belirli görüş ve düşüncenin propagandası, bir örgüt, kurum veya şirketin halkla ilişkiler hizmetleri için yararlanabileceğiniz gibi, Web sayfanızı bir başka yayının tamamlayıcısı olarak da düşünebilirsiniz. Günümüzde Internet, ticaret aracı haline gelmeye başlamış bulunuyor. Özellikle HTTP'nin daha açık iletişime dayanan bazı bölümlerinin şifreli hale getirilmesi ile ortaya çıkan yeni sürümü, SHTML (Güvenli HTML) kredi kartına dayanan alışveriş işlemlerini kolaylaştırmış bulunuyor. Bunun sonucu, bugün bir çok firma Web alanını, bir dükkanın vitrini ve yazarkasası gibi tasarlıyor ve kullanıyor. Bir çok toptancı ve perakendeci Web alanını normal işinin bir uzantısı gibi kullanırken, bir çok kişi sadece Web'de mevcut ve alışverişin sadece Web kanalıyla yapılabildiği "sanal mağazalar" açıyor.

Özetle, yapacağınız Web sayfalarını bir Site bütünlüğü içinde Internet'e açmak veya tabir yerinde ise "Web'e çıkmak" için önünüzde beş yol var. Şimdi bunları sırasıyla inceleyelim:

### 1. Kendi Web Server'ınızı Oluşturmak:

Web sitesi kurmakta en pahalı, buna karşılık gelecek için en verimli yol, kendi bilgisayarlarınızda, kendi ağınızda, kendi Web Server'ınızla kendi sitenize sahip olmaktır. Bir kere kendi URL adresiniz olacak. Sayfalarınızın güvenliğinden siz sorumlu olacaksınız. Ve, biraz sonra değineceğiz, bu Server, size başkaları için Web alanı sunarak para kazanma imkanı da sağlayacaktır.

Ama Web Server kurmak deyince bir çok kişinin adeta yerine çakılıp kalıyor. Çünkü son derece yanlış, ama o derece de yaygın bir şekilde Web Server deyince, bu işten biraz anlayanların aklına hemen UNIX işletme sistemi geliyor; bu kurması ve işletmesi son derece zor sistemin sadece ve sadece "büyük" bilgisayarlar gerektirdiği düşünülüyor. Dolayısıyla kendi Web Server'ını kurmaya hevesli bir çok kişinin hevesi, tabir yerinde ise, kursağında kalıyor. Sizin de böyle bir korkunuz varsa, hemen belirtelim: Piyasada satılan, hatta büyük bir ihtimalle şu anda sizin evinizde de bulunan herhangi bir PC ile Web Server sahibi olabilir ve bu serverda oluşturacağınız siteyi bütün dünyaya açabilirsiniz.

"Herhangi bir PC" sözünü biraz açmak şart: Bu bilgisayarın ziyaretçilerinizi canından bezdirmeden hizmet verebilmesi için en az Intel 66 MHz 486 veya dengi CPU'ya, en az 32 MB belleğe ve 1 GB sabit diske sahip olması gerekir. Sayfalarınıza günde 15'den fazla ziyaretçi gelmesini bekliyorsanız, CPU'nun en az 90 MHz Pentium, belleğin 64 MB'dan fazla, sabit disk alanının da en az 2 GB olması iyi olur. Tabiî, sabit disk alanının büyüklüğünü, içeriğiniz belirleyecektir.

Ama gördüğünüz gibi, "Artık iyice eskidi," dediğiniz 66 MHz 486 CPU'su bulunan bilgisayarla bile Web sitesi kurulabilir ve işletilebilir. Önemli olan "İnternet için UNIX sistemi gerekir!" şeklindeki yanlış kanıyı bir kenara bırakın.

Muhtemelen aşina olduğunuz Microsoft Windows işletme sisteminin NT türü ile, Windows ortamında yine Microsoft'un Internet Information Server yazılımını kullanarak, en geç bir hafta içinde Web sahibi olabilirsiniz. Bir hafta diyoruz; çünkü bağlantı için başka kurum ve firmaların harekete geçmesini beklemek zorundasınız. İş sadece size kalsa, Web siteniz yarın hazır!

NT'nin herhangi bir UNIX sürümünden daha iyi Internet platformu olduğuna inanıyoruz. Herşeyden önce, NT, karşınıza Windows 95 ve 98'den aşina olduğunuz bir çehre ile çıkıyor. UNIX, DOS gibi, komut satırından işletilen bir sistemdir. NT'nin bir bilgisayara kurulması, Windos 3.1, 95 veya 98'in kurulmasından daha zor değil. Bir Web alanının NT platformunda yönetimi, herhangi bir Windows kelime-işlem veya muhasebe programını öğrenmekten daha fazla bilgi gerektirmiyor. Ayrıca, günün birinde sisteminizi gerçekten büyütmek isterseniz, UNIX gibi yeni donanım, yeni yazılım gerektirmeyecektir; çünkü NT istediğiniz kadar bilgisayara yayılabilen bir sistemdir.

Ve en önemlisi, bugün UNIX dediğiniz zaman karşınızda ciddî bir muhatap bile bulmanız şans işi iken (çünkü UNIX Internet'ten ücretsiz edinilebilecek bir işletim sistemidir!) NT, size Microsoft'un bütün desteğini sağlayacaktır. NT, 16 MB belleği olan bir bilgisayarda da, 1 GB belleği olan bir bilgisayarda da, aynı etkinlikte çalışacaktır. Ayrıca NT, birden fazla CPU bulunan sistemlerde, kendiliğinden iş yükünü çipler arasında paylaştırarak, daha hızlı çalışabilir. NT, diğer bütün sistemlerin aksine, 32 Terabyte (1 Terabyte, bin Gigabyte demlektir) disk alanını tanıyabilir. Bunlara ek olarak NT, donanımdan bağımsız bir işletme sistemidir; yani her türlü PC sisteminde çalışabilir. Buna karşılık belirli UNIX türleri belirli imalatçıların bilgisayar sistemlerinde çalışabilirler.

Bütün bunlar NT sisteminin üstünlüğü için ikna edici değilse, NT Server sistemi, paketten her türlü iletişim protokolü ve Internet'in kullandığı WWW, FTP, Gopher, DNS gibi (UNIX sisteminde ancak parayla edinilebilecek) bağlantı programları ile birlikte çıkacaktır.

Kendi bilgisayarınızda kendi bağlantınızla, kendi Web Server'ınızla Wb sitesi sahibi olmaya karar verirseniz, önünüzde başka imkanlar da açıldığını hatırlamalısınız: Siz de Web evsahipliği yapabilirsiniz! Yapacağınız yatırımı ticarete dönüştürebilir, başkalarına Web servisi verebilirsiniz. Sonuç itibariyle bilgisayarı, Web Server programı, Internet bağlantısı ile, şu anda milyonlarca kişinin Web sayfasına ev sahipliği yapan bir firma kadar yatırım yapmış olacaksınız. Neden bu imkandan sadece kendi sayfanıza ev sahipliği yapmak için yararlanmakla yetinmek zorundasınız? Sizin bir Internet Sitesine sahip olmanızı gerektiren sebepler, hemen hemen aynen, başka bir çok kişinin de Web sayfasına sahip olmasını gerektiriyor. Fakat bir çok kişi, bunu ya zor, ya da pahalı sayarak, böyle bir çabadan kaçınıyor. Oysa siz, yapacağınız yatırımla ve bu arada edineceğiniz deneyimle, bir çok kişiye Web alanı kurması için gerekli cesareti ve teşviki sağlayabilirsiniz. Bilgisayar dergileri, gazete ve diğer dergilerin ilgili sayfaları Web Sayfası Evsahipliği Servislerinin ilanlarıyla dolu. Bu kişilerin hemen hemen hepsi, sizin gibi Web Sitesi Evsahipliği işine bir bilgisayar ve bir modemle başlamış kişiler.

Yapacağınız yatırımla Internet'le ilgili iki ayrı hizmet verebilirsiniz: Internet Sitesi Evsahipliği ve Internet Servis Sunuculuğu.

Internet Sitesi Evsahipliği: Uygulamada, isteyene kendi bilgisayarınızdan sabit disk alanı kiralamaktan ibaret olan Web Evsahipliği, adından da anlaşılacağı üzere, başkalarının Web alanlarını kendi sabit diskinizde yer vermektir. Bir çok kişi, Web sitesi oluşturmayı bir kenara bırakın, kendi bilgisayarında, kendi kullanımı için dahi HTML sayfası yapamaz. Oysa gazeteye veya dergiye vereceğiniz bir ilanla, isteyene, Web sayfalarına ev sahipliği yapabileceğinizi bildireceksiniz. Bu işten biraz anlayanlar, kendi yaptıkları sayfaları onlara vereceğiniz parolayı kullanarak, sabit diskinizde kendilerine açtığınız dizine koyacaklardır. Hiç anlamayanlar ise, muhtemelen kağıt üzerinde nasıl bir sayfa ve nasıl bir tasarım istediklerini size anlatacaklar, içerik unsarlarını yine ya kağıt üzerinde, ya da floppy disketlerde size verecekler ve siz de bu malzeme ile onların HTML sayfalarını tasarlayacak, onlara ayırdığınız Web alanına koyacaksınız. Başkalarının teknik sorunlarıyla uğraşmak ve gece-gündüz bilgisayarınızı en mükemmel şekilde çalışır vaziyette tutmaktan sorumlu olmak istemiyorsanız, Web sitesi oluştururken HTML alanında edineceğiniz tecrübe ile başkalarına Web sayfaları tasarımı yapabilirsiniz. Bir çok Web Sitesi Evsahibi firma, ev sahipliğinden çok içerik geliştirme ve sayfa tasarımından para kazandığını bildiriyor.

Internet Servis Sunuculuğu (ISS): Büyük bir ihtimalle şu anda sizin de bir ISS'niz var. Bu kişi veya kurumla yaptığınız bir anlaşma ile, bilgisayarınızın browser programına onların verdiği bir telefon numarasını arattırarak, Internet bağlantısı sağlıyorsunuz. Elektronik posta adresi olarak da bu kişi veya kurumun bilgisayarındaki Web adresini gösteriyorsunuz. Internet'te kendi alanınızı oluşturduğunuz zaman, bu kişi veya kurumun şu anda size verdiği hizmeti verebilecek bir sisteminiz olacak demektir. Tabii Web sahipliği ile ISS arasındaki fark, ikincisinin daha fazla donanım ve yazılıma sahip olması zorunluğudur. Web sayfalaranızı 24 saat hizmete açık tutmak isteniz bile bir telefon bağlantısı (daha hızlı bağlantı istiyorsanız, daha farklı bir bağlantı) işinize yetecektir. Fakat ISS işinde öyle değil: Her an birden fazla müşterinin sizin bilgisayarınıza girip, oradan Internet'e çıkabilmesi için sizin çok sayıda modeme ve çok sayıda telefon hattına ihtiyacınız var demektir. Ayrıca bir Web Evsahipliği firmasının sahip olması gereken türden Internet bağlantınız olması gerekecek. Web sitesi işletmecisi olarak, alanınızı ziyaret edecek kişilere istediğiniz sür'atte hizmet sağlamakta serbestsiniz. Ama ISS olarak müşterilerinize en hızlı bağlantıyı vermekle yükümlüsünüz; yoksa müşterilerinizi daha hızlı hizmet veren ISS'lere kaptırırsınız. ISS olarak yapacağınız yatırım ne kadar yüksek olursa, muhtemel geliriniz de o kadar yüksek olacaktır.

Bilgisayarı sağladıktan ve önce NT işletim sistemini sonra Microsoft Web Server programını kurduktan sonra, bu sistemi dışarıya, Internet'e bağlamanız gerekir. Bir Server'ı Internet'e bağlamakla, bir başkasının evsahipliği yaptığı Web sitesindeki sayfaları güncelleştirmek için gerekli bağlantı arasında çok fark vardır. Bir Web Server, üzerinde bulunduğu bilgisayar kadar, modem ve kendisini Internet'e bağlayan telefon hattından oluşur. Hatta "Internet telefon hattının kendisidir!" dersek, durumu fazla abartmış olmayız. Sonuç itibariyle iyi bir bilgisayar ve oluşturacağınız Web server ne kadar mükemmel olursa olsun, bir telle dış dünyaya bağlı değilse, Web siteniz fiilen yok demektir.

Dış dünya ile bağlantınız için seçebileceğiniz çeşitli imkanlar var. Seçimi sahip olmak istediğiniz bağlantı hızı belirleyecektir.

Hat genişliği veya İngilizce ifadesiyle bandwidth, belirli bir zaman diliminde (standart ölçüyle bir saniyede) bilgisayarınızdan ne kadar veri çıkacağı ve ne kadar veri gireceğini gösterir. En yaygın ölçü, bilgisayar işlemlerinde kullanılan en küçük veri birimi olan bit'tir. Bit, yani iki karakterden (sıfır ve bir rakamlarından) oluşan ve bilgisayar dilinin kelimelerinin en küçük hecesidir. Bilgisayar iletişiminin ölçüsü olan bps (saniyede … bit), çoğunlukla bin bit (kilobit, Kbps) veya bin Kilobit (Megabit, Mbps) olarak ifade edilir.

Web alanınızın bağlantı hızını (hattın genişliğini) belirlerken, dikkate alacağınız önemli bir unsur maliyet olacaktır. Hattınız ne kadar geniş olsun veya iletişiminizin ne kadar hızlı olsun istiyorsanız, hat ve modem masrafı o kadar artacaktır.

Hat genişliği ile sistemin merkezi olan bilgisayarın işlemci (CPU) hızı, belleği (RAM) ve sabit disklerinin toplamını belirlerken Web alanınızın kapasitesini gözönünde tutmalısınız. Önce kapasite planlamadan söz edelim, sonra buna göre donanım özelliklerini ele alalım.

#### Kapasite Planlaması

Bir Web alanının üzerinde durduğu bilgisayarın ve dış dünya ile bağlantısının alt sınırını Web alanının içeriği belirlemelidir. Üst sınırı ise, Web alanı sahibinin bu iş için ayırabileceği paranın miktarı belirleyecektir.

İçeriğini belirlerken, gerçekleştiremeyeceğiniz hedefler koyarak, kendi kendinizi başktan başarısızlığa mahkum etmemelisiniz. Siteniz, metne mi ağırlık verecek, grafiğe mi? Fotoğraflarınızı kamuoyuna göstermek ve gazete-dergi yayıncılarının ilgisini çekerek, pazarlamak için bir alan yapıyorsanız, her bir fotoğrafın, on sayfa yazı kadar yer tutacağını hesaba katmalısınız.

Web sitenizin kapasitesine ilişkin tahmin hesapları yaparken, mutlaka ama mutlaka gerçekçi bir cevap bulmanız gereken soru kaç ziyaretçi beklediğinizdir. Bir fotoğrafçının kişisel Web alanı günde 10 kişi tarafından ziyardet edilirse, bu iyi bir oran sayılabilir. Buna karşılık bir gazete, dergi, radyo veya televizyon istasyonunun halka ilişkiler, promosyon ve haberlerinin daha güncel sunma çabasıyla kurduğu Web sitesine günde 3 bin ziyaretçi gelirse, bu çok düşük bir rakam sayılabilir. Bu soruyu cevaplarken, aynı anda kaç ziyaretçi beklediğinizi de belirlemeye çalışmalısınız. Yüksek bir toplam ziyaretçi rakamının sisteminize yükü başka olacaktır, aynı anda sitenize gelecek ziyaretçi sayısının yüksekliğinin etkisi başka olacaktır. Web alanlarını sınıflandıranlar, genellikle üç gruba ayırırlar: Düşük trafik alanları, aynı anda 5 veya daha az ziyaretçinin uğradığı sitelerdir. Bu rakam 20'e çıkarsa, site orta trafik tlanı sayılır. Anda gelen gelen ziyaretçi sayısı 20'yi aşınca, bu siteyi yüksek trafik alanı saymak gerekir.

Ziyaretçiler Web sitenizde ne gibi işler yapacaklar? Alanınıza, on-line, yani ziyaretçi size bağlı iken, oynanabilecek oyunlar koyacak mısınız? Bu çok, ama pek çok bellek gerektirir. Ziyaretçileriniz Web sitenizde bir form dolduracaklar mı? Bu, Web Server programınıza program çalıştırma yeteneği kazandırmanızı gerektirecektir. Sayfalarınızda ziyaretçinin bilgisayarındaki browser programın türüne göre ve sitenizde iken yaptığı bazı tercihlere göre değişen, yani dinamik bir içerik mi sunacaksınız? Web Server programınızın bayağı ileri düzeyde olması gerekir. İleri düzeyde Windows programlarının ise daima daha fazla bellek ve sabit disk alanı istediğini hep biliyoruz.

Kapasite planlamasında üçüncü grup ögeler ise gelecekle ilgili tahminleriniz olacaktır. Web alanınızın gerçek genişlemesini, duyulmasını ve ziyaretçi sayısının artmasını istiyor ve bekliyor musunuz? Ticarete yönelik bir site oluşturan kişinin en büyük arzusu, adının duyulmasıdır. Hergün daha çok kişinin alanınıza gelmesi, başlıca amacınız olduğuna göre, sisteminizin genişlemeye müsait olması şart. Fakat fotoğrafçı arkadaşımızın örneğine dönersek, onun böyle bir amacı olmadığını kolayca görebiliriz. Dünyadaki bütün fotoğraf alıcısı yayın editörleri sözleşip aynı anda dostumuzun web sitesini ziyarete gelmeyeceklerine göre, bu alanın düşük trafik alanı olarak kalacağını varsayması yerinde olur.

#### Bilgisayar

Kapasite planını yaptığınız zaman karşınıza çıkan tablo, genel hatlarıyla üç gruptan birisine girebilir:

1. Düşük trafik, az ziyaretçi ve ziyaretçilerin Server'da ek program kullanmayacakları alanlar

2. Orta trafik, orta ziyaretçi ve ziyaretçilerin bir ya da iki form doldurmaktan başka bir şey yapmayacakları alanlar.

3. Yüksek trafik, çok ziyaretçi ve ziyaretçilerin aynı anda bir çok program çalıştıracakları alanlar.

Şu anda planladığınız siteyi bu alanlardan hangisine koyarsanız koyun, daima biraz büyümeye müsait tercihler yapmanız gerekir. Ayrıca, ziyaretçi bakımından sınırlı bir Web sitesi, içerik bakımından orta büyüklükte bir alandan daha çok sabit disk gerektirebilir. Örneğin bizim fotoğrafçı dostumuz, çok az ziyaretçi beklediği ve ziyaretçilerine sadece bir sipariş formu doldurtacağı halde, eğer bütün fotoğraf arşivini ziyaretçilerine açmayı planlıyorsa, çok ama çok geniş sabit disk alanına ihtiyacı olacak demektir. Buna karşılık bilgisayar oyunları satan bir firmanın Internet sayfasında, fotoğrafçıya oranla daha az yer kaplayan malzeme bulunacak, buna karşılık ziyaretçilerinin oyunları sınamasını istiyorsa, sistemine çok bellek koymak zorunda olacaktır.

Bu nedenle, donanım tavsiyelerimizi, sadece fikir edinmek için gözönünde tutmanız gerekir.

**Servisler Düşük trafik Orta trafik Yüksek trafik**

WWW 166MHz/32MB/1GB 200MHz/32MB/1GB 233MHz/48MB/2GB

FTP 166MHz/32MB/1GB 166MHz/32MB/1GB 166MHz/48MB/2GB

E-Posta 133MHz/48MB/1GB 133MHz/48MB/1GB 166MHz/64MB/2GB

4 Servis 133MHz/48MB/2GB 166MHz/64MB/2GB 300+MHz/124MB/3GB

Bu listenin sadece yolgösterici olduğunu, donanım fiyatlarının nerede ise her gün düştüğünü gözönüne alırsak, donanım seçerken mümkün olduğu kadar imkanınınızı daha büyük, daha geniş ve daha hızlı donanım yönünde zorlamanız kolaylaşıyor. Bu listeye göre, ziyaretçilerine dosya aktarma imkanı tanımayacak (FTP server kurmayacak), elektronik posta imkanı vermeyecek ve sadece Web hizmetiyle yetinecek bir alanın 166 MHz işlemci ile bu işi idare etmesi mümkündür. Aynı işi 66 MHz hızında bir Intel 486 CPU bilgisayar ile de yapmak mümkün. Ama bu iş için yeni bir donanım almaya kalkıyorsanız, kesinlikle paranızın elverdiği en gelişmiş donanımı almalısınız.

Yine bu liste size, herbiri 400 MHz hızında iki CPU'su olan, belleği 124 MB'ın üzerinde, 10 Gigabyte sabit diski olan bir bilgisayara ihtiyacınız olmadığnını da gösteriyor. Bu tür sür'at ile işlem ve kayıt ortamı edinmek için harcayacağınız yatırım parasını, aslında modem hızını ve hat genişliğini arttırmaya harcamakla daha kârlı çıkabilirsiniz. Sabit diski ya da belleği yetmeyen bir bilgisayara bunların hepsi her zaman eklenebilir. Ama belirli bir hızda kablo için anlaşma yaptığınız zaman kablonun hızını anlaşma süresince arttırmak o kadar kolay olmayabilir. (Kiralık hat veren firmalar, anlaşmaya erken fesih halinde tazminat hükmü koymuş olabilirler; ama çoğu kapasite artırımı maksadıyla anlaşmayı yenilemeyi kabul ederler.)

Donanım bahsinde genel ilkeler arasında mutlaka sayılması gereken bir husus, sabit disklerinizin mutlaka yedeklenmesi gereğidir. Bir Web Server'ın çökmesi ve bu sırada bir çok veri ve program dosyasının kullanılamaz hale gelmesi, Web'in yeniden kurulması zorunluğunun ortaya çıkması, artık sadece bir zorluk olmaktan çıktı. Böyle bir durum, firmanın iş kaybına da neden olabilir. Web Server programının çalıştığı ve Internet kablonuzun bağlı olduğu bilgisayarın çökmesi, sipariş alma ve verme imkanının kaybına, bilgi ulaşımında aksamaya, ve dolayısıyla para kaybına neden olacaktır. Buna ek olarak Web Server'ın onarılması ve yeniden kurulması için ayıracağınız zaman ve belki de ücret ödeyerek edinmek zorunda kalacağınız servisi de hesaba katmalısınız. Başlangıçta iyi bir yedekleme sistemine yapılacak yatırım, ilerde sizi bu tür masraflardan ve gelir kayıplarından kurtaracaktır. Günümüzde bilgisayar sistemlerinin çökmesinde birinci sebep, sabit disk arızasıdır. Hemen hiç bir parçası hareketli olmayan bilgisayarın içindeki tek hareketli bölüm olan sabit diskler, bunun sonucu olarak, kimi zaman sistemin tümüne ayak uyduramazlar. Bilgisayar sistemlerinin çökmesinde ikinci en büyük sebep, yazılımlardaki hatalardır.

Internet işinizin bir parçası olacaksa, sisteminizin hata toleransını yükseltmek zorundasınız. "Hata toleransı" bir sistemin hayatî birimlerinin yedeklenmesi ile yükseltilebilir. Web sisteminin durduğu bilgisayardaki bütün yazılım sistemi ve ayarlar ile verilerin Disk Yansıtma Sistemi (Disk mirroring) ile yedeklenmesi gerekir. Bu yöntem, muhtemelen şu anda sabit diskinizi yedeklemekte kullandığınız teybe veya Zip disklere kopya almaktan farklı bir yöntemtir. Sistemin esası, bilgisayarın içinde en az iki sabit bulunması ve bu disklerin birbirinin aynı olmasını sağlamaktan ibarettir. Bu amaçla geliştirilmiş programlar, bir sabit diskteki girdi/çıktı hareketini aynen diğer diske yansıtırlar. Bir anlamda, bilgisayarınızda her an birbirinin aynı iki sabit disk olur, fakat CPU bunlardan sadece birini gerçek kayıt ortamı olarak kabul eder. Sistem, sabit disk arızası nedeniyle çöktüğü anda, çoğu zaman sistem operatörünün müdahalesine bile lüzum kalmadan, Disk Yansıtma programı devreye girerek, yedek sabit diski ana sabit disk yapacak ve o anda Web alanınızda bulunan ziyaretçilerin bile ruhu duymadan, sistem hiçbirşey olmamış gibi, hizmete devam edecektir. Disk Yansıtma, Microsoft Windows NT Server işletme programının aslî parçalarından biridir; ayrıca para vererek yeni bir yazılım almaya bile gerek yoktur.

<web008.tif>

Windows NT'nin Disk Yönetmemin (Disk Administrator) programı, diskleriniz arasında Yansıtma sistemi oluşturmanız, iki ya da üç tıklama ile yapılabilecek kolaylıktadır.

Bu kolaylığa aldanıp, bugüne kadar yapageldiğiniz, disk yedekleme işleminden asla vaz geçmemeniz gerekir. Tam tersine, Yansıtma yoluyla oluşturduğunuz ikinci sabit disk devreye girdikten sonra, muhtemelen Server'ı düzenli bir şekilde kapatıp, sür'atle birinci sabit diski eski şekline getirmeniz gerekir. Yansıtma Takımı'nın bir diskini diğerine aynen kopya edebilirsiniz; ama bu bilgisayarın çökmesine sebep olan arıza her ne ise, onu yeniden ana sabit diske yeniden aktarmak olabilir. Dolayısıyla, bir yerde mutlaka bilgisayar sisteminin en mükemmel durumda iken çıkartılmış bir teyp veya Zip disk yedeği olmalıdır. (Büyük bir ihtimalle 100 MB'lık Zip disk, bir Web Server sistemini yedeklemeye yetecektir. Ancak en azından birinci sabit disk veya boot partisyonu genişliğinde bir teyp yedekleme sistemi, her zaman için daha garantili bir önlem olur.

#### Bağlantı

Büyük bir ihtimalle şu anda Internet'e modemle bağlanma imkanınız var! Aramızda talihli olanlar normal telefon bağlantısı yerine ISDN veya kiralık hat kullanıyor olabilir. Kullanıcı olarak yararlandığınız bütün bağlantı türleri, Web Sitesi sahibi olarak Internet'te hizmet vermenize de yarar. Burada dikkat edeceğiniz husus, "Yeter" değil, "Yarar" demiş olmamızdır.

Bağlantının hızı, sitenizin çok ziyaretçi çeken bir site olmasını veya olmamasını tayin edecektir. Günümüzde hiç kimsenin, "Web alanı bulundu; cevap bekleniyor!" mesajını seyretmeye tahammülü yok. Ünlü Web ustaları, sizin bağlantınızın tıklanmasından sayfanızın ziyaretçinini bilgisayar ekranını domdurması arasında en fazla 20 saniye geçmesi gerektiğini söylüyorlar.

Saniyede 36 Kilobit bilgi aktaran bir bağlantı ile 20 saniyede 720 bin bit'lik bilgi aktarabilirsiniz. Bu ise HTML sayfalarının içeriği gözönüne alınırsa, küçük bir başlık grafiği ve 50 kelimeden az bir paragraf yazı demektir. Boş yere bağlantı hızı arttıkta, fiyatı da artmıyor!

Seçeceğiniz bağlantı, bilgisayarınıza ekleyeceğiniz bağlantı donanımının türünü ve niteliğini belirleyecektir. Hiç şüphesiz, bağlantı donanımı türünü belirlediğiniz anda, bu tür cihazlardan hangi marka ve modellerin sizin bilgisayarınıza ve Windows NT işletme sistemine uyumlu olduğunu araştırmak zorundasınız. Bunun için şimdiden Microsoft firmasının Internet alanından Windows NT Server Donanım Uyum Listesi (HCL, Harware Compatibility List)) denen belgeyi alarak, bir yanınızda bulundurun. Bu listede olmayan bir cihazı satın almak, kendi paranızla başınıza dert almak demektir.

| Modem |
| --- |

Internet'e modemle bağlantı, en ucuz bağlantı türüdür. Standart telefon teli ile evinize veya işyerinize gelen telefon bağlantısının sağladığı analog sinyali modüle ederek ve modülasyonu çözerek (cihazın adı olan modem kelimesi Modulation-Demodulation kelimelerinin kısaltılmışıdır) sayısal sinyale çeviren bu araç, bugün saniyede 56 Kilobit'e varan bir hıza ulaşmış bulunuyor. Gerçi, telefon şirketlerinin özellikle büyük kentlerde ve sayısal santral kurulmuş olan yörelerde, bir çift telefon telinden aynı anda birden fazla telefon sinyali alıp-vermeye yarayan multipleks teknolojisi, azamî hızı ne olursa olsun, modemlerin saniyede 26 Kbps'ın üzerine çıkmasını engellemektedir; ama telefon hattı elverişliği olduğu anda, ve ISS 56 Kbps uyumlu hizmet sunduğu taktirde, bu rakama yaklaşmak mümkündür. Bu hız Internet kullanıcının sayfadtan sayfaya gitmesine, hatta arada bir oldukça büyük dosyalar indirmesine elverişlidir. Ama, sizin bu hızla Internet'e servis sunmanız, özellikle orta büyüklükte bir trafik bekliyorsanız, gerçekçi olamaz. Hele 26 Kbps hızda bir bağlantıyla Internet'te ticaret yapmak mümkün olamaz. Telefon-modem yoluyla kurulacak Internet bağlantısı daimi değildir; ISS'e telefon bağlantınız kesildiği anda Internet bağlantınız da kesilmiş demektir.

Internet bağlantınız için başka bir hat masrafı yapmadan telefon sistemini kullanmaya karar verirseniz, bunun için bir modem satın almanız gerekir. Modemler, ya bilgisayarın içine kart şeklinde takılır, ya da bilgisayarın dışında durur ve bilgisayara COM 1 veya COM 2 seri iletişim kapısından ya da USB kapısından bağlanırlar. Bilgisayarın içine takılan modem kartı, ancak bilgisayarın kapağı açılmak suretiyle çıkartılabilir. Oysa dışarıda duran modemler, bilgisayardan bilgisayara nakledilebilir; hatta bir anahtarla ve aynı anda sadece biri tarafından kullanılmak şartıyla, iki bilgisayara birden hizmet verebilirler. Seri iletişim kapısını kullanmak suretiyle bir NT sistemine aynı anda 256 dış modem birden takılabilir. Internet sitenizin zamanla gelişebileceğini, birden fazla telefon hattı ve modem bağlayabileceğini dikkate alarak, bilgisayarın içine takılan kart modem yerine dış modemi salık veririz.

| ISDN |
| --- |

İngilizce Entegre Sayısal Ağ Hizmeti (Integrated Services Digital Network) kelimelerinin kısaltması olan ISDN, telefon şirketinin ev veya iş yerinize en yakın merkezinden (servis kutusundan) size çekilecek sayısal bir hattır ve 128 Kbps'a kadar hız sağlayabilir. ISDN'i size özel bir telefon hattı sayabilirsiniz. Size çekilecek kablo, başka hiç bir abone ile sizin telefon sinyalinizi multipleks yoluyla birleştirmeyeceği için, hat sadece bize ait olacaktır. Bu yolla Internet bağlantısı da, telefon bağlantısı devam ettiği sürece devam eder.

ISDN bağlantısı da modeme benzer bir cihazdan geçerek bilgisayara girer; ancak bu kez modeme benzer cihazın bilgisayarın içine takılması şarttır. Bilgisayarların COM1 veya COM2 seri iletişim kapılarına bağlanacak bir cihaz bilgisayarın ana veri yolu ile 115 Kbps hızıyla iletişim yapabilir. Bu, ISDN'in hızından düşük olduğu için, hattan gelecek sinyaller seri kapısından geçerek bilgisayara girmek için sıra beklemeye başlayacaklar ve bu sistemi sık sık çökertecektir. Oysa ISDN hattından gelen sinyal, bilgisayarın kendi sinyali gibi sayısal olduğuna göre, doğruca veri anayoluna bağlanabilir. Bu nedenle ISDN kartı (çoğu zaman yanlış bir ifadeyle ISDN modemi denilir; ISDN sinyali zaten sayısal olduğu için modüle edilmesine ihtiyaç yoktur!) bilgisayarın içine takılır.

ISDN servisi veren telefon kurumu, kendi sistemine uygun ISDN kartını da abonesine sağlamakla yükümlüdür. ISDN servisi seçerken, kartlarının NT sürecese olup olmadığını mutlaka sorunuz.

Bir çok ülkede ISDN servisi toptan fakat sabit fiyatla veya bir sisteme bir sayaç bağlanmak suretiyle birim fiyatıyla verilmektedir. Günün belirli saatlerinde Internet bağlantınızı kesecek ve Web alanınızı ziyaretçilere kapatacaksanız, sayaçlı yöntem daha hesaplı olabilir. Buna karşılık 365 gün ve 24 saat hizmet Web varlığınızı sürdürecekseniz, toptan sabit fiyat anlaşması yapmanız daha kârlı olabilir.

| Frame Relay |
| --- |

Bir firmanın Internet'e bağlı ağına, doğrudan bağlanmaktan ibaret olan bu yöntemde, bağlantı hızınız 56K'dan T1'e (1.5 Mbps) kadar değişebilir. Bu bağlantı süreklidir; telefon bağlantısı gibi kesilmez. Burada önemli olan bağlandığınız ağın size sunduğu servisin hızıdır. Frame Relay, eski bir ağ protokolü olan X25'in modern bir türevidir. Yoğun trafik bekleyen Server sitesi, Network ile girdi/çıktı ilişkisini Server'ın durduğu bilgisayara yaptırmamak için devreye ikinci bir bilgisayar sokmalıdır.

| Kiralık Hat |
| --- |

Web Server Sitenizi, telefon şirketinden hızı 56 K'dan T3'e (45 Mbps) kadar bir daimi hat kiralayarak, araya hiç kimseyi sokmadan doğrudan Internet'e bağlayabilirsiniz. Internet ile daimi bağlantının en iyi yolu budur. Ancak daimi hattın kirası çok yüksek olabilir.

### 2. Bir Web Sitesinde Ücretsiz Sayfa

<webfree.tif: Resimaltı: Web alanında ücretsiz sayfa imkanı veren firmaların Yahoo!'daki listesi bile bir ekrana sığmıyor. Bu firmaların tam listesini bir çok Arama sitesinde kolayca edinebilirsiniz.>

Bugün bir Web sitesine sahip olmak için en kolay yol, abonelerine ücretsiz Web sayfası imkanı tanıyan bir ISS ile anlaşmaktır. Burada hatırlamanız gereken bir atasözü var: Ucuz etin yahnisi..

Evet bu sayfanın size maliyeti, sıfır. Ama verilen imkanlar da o ölçüde kısıtlı ve sınırlı olabilir. Bu yöntemin esası, bir başkasının Web Server'ın durduğu bilgisayarda bir dizine sizin sitenizin adının verilmesinden ibarettir. ISS'ler müşteri çekebilmek için başvurdukları bu yöntemde genellikle ücretsiz sayfalara sınırlı bir ayırırlar.

Çoğu size ayrı bir Domain adı edinme hakkı tanımaz. Yani sizin kendi adınızla bir alanınız olmaz, URL olarak size ücretsiz sayfa veren firmanın Server'ının Domain adını kullanırsınız. Örneğin, http://www.webevsahibifirma.com/bedavasayfalar/alininsayfası.html. America On Line'dan tutun, Geocities ve Tripod firmasına kadar bir çok kuruluş, abonelerine ücretsiz sayfa alanı sağlıyor. Fakat bu sayfaların çoğunda, site sahibine form ve ona bağlı CGI programı kullanma hakkı tanınmaz.

Fakat cebinizden hiç para çıkmadan Web sitesi sahibi olmak istiyorsanız, bundan başka bir yol da yok. Özellikle belirli bir görüş ve düşüncenin yayılması için kurulmuş kâr amacı gütmeyen dernek ve gruplar, ziyaretçileri ile etkileşmeli (interaktif) ilişki kurması gerekmeyen sayfalar için ideal bir ortam, ücretsiz Web sayfası siteleri olabilir.

### 3. Cybermall

<webmall.tif Resimaltı: Access Market Square, bugün Internet'te mevcut yüzlerce alış-veriş merkezi kavramına dayanan Web alanından biri. Bu "alış-veriş merkezi" içinde bir sanal mağaza açacak olursanız, mağazanız ilgili grubu belirten düğme ile ulaşılan bir ikinci sayfada gösterilecek. Bir arama alanında "Online Shopping" kelimeleriyle bu tür alanları araştırabilirsiniz.>

Tıpkı içinde yüzlerce mağaza bulunan dev alış-veriş merkezleri gibi, Internet'in sanal ortamında da mağazalar açılıyor. Bu alanı işleten firma ile bir anlaşma yapıyorsunuz; sayfa veya sayfalarınız bu firmanın Web sitesinde bir alt-site oluşturuyor. Kendinize ait bir URL ulabilir veya olmayabilir. Sizin sayfalarınız çoğu zaman "Mall" firmasının Domain'i içinde bir alt-domain oluşturacaktır.

Bu yöntemin de iyi tarafları-kötü tarafları var. Bir kere Internet'te alışveriş artıyor ve Internet aboneleri giderek daha çok elektronik alışveriş yapıyorlar. Ayrıca "Mall" firması kendi alanının duyurusunu yapacağı için sizin sitenizin de otomatik olarak reklamı yapılmış olacaktır. Fakat sizin siteniz sanal mağaza türü değilse, bu yöntem size uygun olamaz. Siteniz alış-veriş sitesi bile olsa, unutmayın koca alış-veriş merkezi içinde sizin siteniz yüzlerce "dakkandan" sadece biri olacak! Hele kendi URL'iniz olmayacaksa, kendi sitenizin duyurusunu yaparken, belki de aynı Mall'da sitesi bulunan rakiplerinizin de reklamını yapmış olacaksınız!

### 4. Web mağazaları

Günümüzde Sanal Mağaza açan firmaların sayısı arttıkça, bu mağazalarda sattıkları belli mamüllere kendi siteleri içinde "sayfa" vermeye başlayanların sayısı da artıyor. Gerçi bu "sayfa" gerçek anlamda bir "site" sayılmaz, ama yine de bir mamülün tanıtımı açısından, üstelik o tür mamülü arayanların uğrak yerinde bulunacağı için, iyi bir reklam vasıtası sayılabilir. Sizin firmanızın ürettiği trikoların büyük bir giyim-kuşam zincirinin Web alanında, kendine ait bir sayfada tanıtılması, hele bu sayfanın içeriğini belirleme hakkı mamülün üreticisi olarak size tanınacaksa, bulunmaz bir fırsat olarak değerlendirilebilir.

### 5. Web Evsahibi Şirketler

Ve dünüp dolaşıp, asıl tavsiye edeceğimiz Web Sitesi yöntemine geldik. İşte size Yoksul Richard'ın 50 Dolarlık Web alanı! Hele şu anda bilgisayarınız varsa, ve Internet'e ulaşım hakkına sahipseniz, hiç lafı döndürüp-dolaştırmadan söyleyelim ki, hemen çarşıya çıkıp bir Microsoft FrontPage 98 programı satınalıp, iki ya da üç saat sonra Web sitenizi yapmış olabilirsiniz. 24 saat sonra kendinize ait bir URL adresiniz olabilir. Hele HTML sayfalarınızı tasarlarken, ilerde değineceğimiz ilkelere uyar, ve bir gün ve gecenizi bu yeni alanınızı Internet Arama firmalarına tanıtmakla geçirirseniz, bir hafta içinde hedeflediğiniz ziyaretçi sayısına ulaşmanız işten bile olmayacaktır.

Bir kere, bir Web Evsahibi şirketle anlaşıp, kendi URL adresinizi tescil ettirir ve kendi sitenizi kendiniz tasarlarsanız, herşeyden önce ziyaretçilerinize kendi arzu ettiğiniz etkileşme imkanını verebilirsiniz; ziyaretçileriniz sizin kendi Domain adınız olduğuna bakarak, işinizin ciddî olduğunu anlarlar. Seçeceğiniz ev sahibi şirkete bağlı olarak, en az bir, fakat çoğunlukla 5 POP elektronik posta kutunuz olabilir. Bunun yararı ne? Düşünün bir firmanın gazete-dergi reklamını inceliyorsunuz. Reklamda, "Toptan satışlarımızla ilgili TOPTAN@BENIMFIRMA.COM.TR'ye, perakende satışlarımızla ilgili PERAKENDE@BENIMFIRMA.COM.TR'ye elektronik posta gönderebilirsiniz" deniliyor. Samimiyetle söyleyin; bu firmanın sağlam, güvenilir ve büyük olduğunu düşünür müsünüz, düşünmez misiniz? Gerçekte her iki elektronik posta adresi de bu site sahibinin edindiği Domain adına, aynı IP adresinde POP kutusuna gidecektir. Yani size. Reklamınız görenlerde arzu ettiğiniz etkiyi sağlayacaktır! (Bu etkinin gereğini yapabilecek imkanlara sahip olup olmadığınız, yani gerçeğe dayalı reklam yapıp-yapmadığınız ayrı bir ahlâk konusu.) Web evsahibi şirketlerle anlaşarak oluşturacağınız Web alanınıza, on-line sipariş ve elektronik ticaret imkanları koyabilirsiniz. Sitenizi ziyaret edecek kişilere bir forma adlarını ve adreslerini yazarak, sizin katalog gönderme listenize girmelerine imkan verebilirsiniz. Ve en güzel tarafı, URL size ait olacağı için, evsahibi şirketten mennun kalmaz da yarın bir başka evsahibi firmayla anlaşacak olursanız, yeni firmaya URL'inizi de beraberinizde götürebilirsiniz. Bastırdığınız kartvizitler ve broşürler çöpe atılmamış olur!

Evsahibi firma tercihiniz için, en çok imkanı, en ucuza veren ve bu işi en uzun süre yapmakta olan bir firmayı seçmenizi tavsiye etmekten başka bir şey söylemeyeceğiz. Internet'in coğrafya ve uluslararası hukukun sınırlarını ortadan kaldığı dünyamızda, evsahibi şirket tercihiniz illâ Türkiye ile sınırlı da değil. Bu sınırsızlık, Web evsahibi şirketleri hergün daha fazla imkanı, daha az ücretle sunmaya zorluyor. Çevrenizle konuşun; şu anda böyle bir firmadan Web sitesi almış tanıdıklarınıza sorun. Hatta böyle bir kaç firmaya elektronik mektup yollayın, telefon edin; verecekleri karşılıkları, konuşma usluplarını değerlendirin. Bir kaç teknik soru sorun; neden bahsettiğinizi anlıyorlar mı? Bu tür firmaların seçiminde gözeticilecek ilkelerle ilgili bir Internet sohbet alanında bulduğumuz şu tavsiyeyi aktarırsak, ev sahibi firma seçiminde herkesin nasıl davrandığını görmüş olacaksınız:

"Evsahibi firmalar arasında başka bakımlardan uygun bulduklarınızın Internet sitelerine girin ve teknik destek bölümünün telefon numarasını alın. Sonra o gece sabaha karşı 03'de bu namarayı arayın. Cevap veren biri var mı? Cevap veren varsa, kendisini tanıtın ve teknik yardım sisteminin işleyip işlemediğini sınamak için aradığınızı ve işbaşında birini bulmaktan memnun olduğunuzu söyleyin. Ertesi gün de firmayla anlaşma yapın. Telefona cevap veren olmazsa, başka bir firma aramaya başlayın."

24 saat teknik yardım hizmeti veren böyle bir firma buldunuz diyelim. Nasıl bir anlaşma yapmalısınız? Bu tür firmaların sundukları servisleri dörte ayırabiliriz. Şimdi sırasıyla bu hizmet türlerini inceleyelim.

#### Dizin Şeklinde Web Sitesi

Bu usulde kendinize ait bir URL almazsınız. Bu sizi Domain adı için ruhsat ücretinden kurtarır. Siteniz, evsahibi firmanın Domain'inde bir dizin olur. Örneğin, http://www.webevsahibifirma.com/alininsitesi/ gibi. Bu sitede POP e-posta, FTP, vs. gibi her türlü imkanınız olabilir. Ama evsahibi firmayı değiştirmeye karar verirseniz, bu adres de değişir; yaptığınız tanıtım ve bu ardresi içeren basılı kağıtlarınız da değişmek zorunda kalır.

#### Alt-domain Şeklinde Web Sitesi

Siteniz evsahibi firmanın Domain'inde dizin değil, alt-domain olacaktır. Örneğin, http://www.alininsitesi.webevsahibifirma.com/ gibi. Bu sitede POP e-posta, FTP, vs. gibi her türlü imkanınız olabilir. Ama evsahibi firmayı değiştirmeye karar verirseniz, bu adres de değişir; yaptığınız tanıtım ve bu ardresi içeren basılı kağıtlarınız da değişmek zorunda kalır.

Bazı Internet şirketleri, örneğin Monolith@Home, bu suretle alacağınız bir alt-domain Internet adresini çok daha kısa ve kullanışlı hale getiriyor. Bu firmayla anlaşarak, URL olarak örneğin http://alininsitesi.home.ml,org adresini kullanıyorsunuz. Ziyaretçileriniz bu adresi aradıklarında, firmanın Domain Server bilgisayarı, ziyaretçiye doğru IP adresini veriyor. İlerde alt-domain olduğunuz evsahibi firmayı değiştirirseniz, adres değiştiren firmayı örneğin Monolith@hHome şirketini uyararak, adresinizi düzeltmesini isteyebilirsiniz. Tanıtım ve basılı kağıtlar boşa gitmemiş olur!

#### Sanal Web Sitesi

Kendi işyerinizde, kendi bilgisayarınızla, kendi Web Server'ınızla ve kendi hattınızla Web sitesi sahibi olmayacaksanız, ikinci en iyi Web sitesi bu yöntemle kurulur. Evsahibi firma aracılığıyla veya kendiniz InterNIC denen kurumla temasa geçerek, kendi Domain adınızı tescil ettirir ve ruhsat ücretinizi ödersiniz. Kendi URL'iniz olur. Tescil işlemini evsahibi firmaya yaptırmak, belki daha kolay görünebilir; ama evsahibi firma büyük bir ihtimalle seçeceğiniz Domain adını kendi adına tescil ettirecektir. Evsahibi değiştirmek istediğinizde, URL'inizi kullanmaya devam edebilmek için, ya evsahibi firmanın Domain adını sizin adınıza tescil ettireceğinden emin olun, ya da bu işi kendiniz yapın. İlerde bunun ne kadar kolay olduğunu göreceksiniz.

Bu yöntemde, InterNIC ve onun hergün Domain Name Server'ı vasıtasıyla bütün dünyaya dağıttığı Domain adları listesini alan aracı Domair Name Serverlar, sizin URL olarak aldığınız adın karşısına, evsahibinin firmanın Web Server'ının IP adresini yazacaktır. Böylece ziyaretçiniz browser ekranına http://www.alininsitesi.com yazdığında, Internet sistemi, browser'a evsahibi firmanın IP adresini gösterecektir. Domain adı size ait olursa, evsahibi firmayı değiştireceğiniz zaman, InterNIC'e IP adresinizin değiştiğini bildireceksiniz ve Domain Name Server sisteminde gereken düzeltme yapılacaktır. Yani ziyaretçileriniz browser ekranına http://www.alininsitesi.com yazmaya devam edecekler, fakat bu kez browserlarına başka bir IP adresi verilecektir. Sonuç olarak herkes hangi evsahibi firmanın Web Server'ında durursa dursun URL'iniz değişmeden kalacaktır.

#### Sadece İsimden İbaret Web Sitesi

Yukarıda Domain adı olan URL'in Internet dünyasında bir Web Server IP adresi olduğunu söyledik. Birden fazla URL'i, aynı Web Server IP adresine bağlayamaz mıyız? Tescil ücretini verdikten sonra aynı IP'ye isterseniz yüz adet Domain adı bağlayabilirsiniz. Sonuçta hepsi aynı kapıya çıkar; ama siz neden birden fazla URL edinmek istemişseniz, o amaç gerçekleşmiş olur.

Neden birden fazla URL sahibi olmak isteyebilirsiniz? Bu sorunun cevabı sizin ihtiyaçlarınıza bağlı. Ama örneğin bir firma birden fazla alanda faaliyet gösteriyorsa, her alanı temsil eden bir URL edinmek isteyebilir. Ama firma, birden fazla Web sitesi oluşturmak ve bakımını yapmak kolay olmayacağı için, hangi URL'i izleyerek gelirse gelsin, bütün ziyaretçilerin aynı sayfaya ulaşmasını isteyebilir. O zaman çare, evsahibi firmanın size ayıracağı alanda sitenizi oluşturmak ve bu sitenin durduğu Web Server'ın IP numarasını farklı Domain isimleri için adres olarak tescil ettirmekten ibarettir.

# Bölüm II: İnşaata Hazırlık

Kendi işyerinizde, kendi bilgisayarınızla, kendi Web Server'ınızda, kendi hattınızla kendi sitenizi oluşturacaksanız, yapacağınız ilk iş, bu işin uzmanı bir kişinin yardımını istemek olmalı. Bilgisayara Web Server kurmak, başta da belirttik, herhangi bir Windows uygulama programını kurmaktan farklı değil. Ama işin teknik bölümleri, özellikle hat kiralamak, bu hat T1 veya T3 olacaksa, bilgisayarla binanıza gelecek hattın arasında Router denen ikinci bir bilgisayar yerleştirmek tecrübe isteyebilir. Teknik cihazların içinden çıkan broşürleri ve kullanma kılavuzlarını okuma alışkanlığınız varsa, Router cihazını kurmak da o kadar zor olmayabilir. Ama bir teknik uzman sizi bir çok uykusuz geceden ve başağrısından kurtarabilir.

## Evsahibi Seçmenin İlkeleri

Ama bu yola gitmiyor ve Web sitenizi, kendi Domain adınıza tescil ettirerek, ama bir başka evsahibi firmanın Web Server'ına koyarak Internet'e açmak istiyorsanız, başınız hiç ağrımayacak demek değildir! Web evsahibi seçmek, Router veya Web Server kurmaktan daha kolay görünebilir. Ama ev ödevinizi iyi yapmaz ve dikkatli bir seçimde bulunmazsanız, başınız daha çok ağrıyabilir. Şimdi bu seçimin ilkelerini ele alalım.

### Microsoft FrontPage Server Extensions Var mı?

Web sitesi sahibi olmanız, bilgisayar programcısı olduğunuz anlamına gelmez. Ayrıca bu hiç de gerekmez. Konuyla biraz ilgilendiyseniz, Form denen HTML etiketini kullanarak, sayfalarınızı ziyaret edecek kişilerin sizin Web alanınızda "birşeyler yapmasına" imkan verebileceğinizi biliyorsunuz demektir. Bu basit bir adını-adresini bildirme formu olabilir; tam teşekküllü bir elektronik alışveriş sayfası olabilir. Ziyaretçi, Web browser programının ekranında "Gönder," "Satın al!," "At Sepete!" gibi düğmeleri tıkladığında, tabir yerinde ise perde gerisinde bir takım programlar harekete geçer, bazı bilgiler bir yerlere kaydedilir; bir yerlere elektronik posta mesajları veya dosyalar gönderilir. Hatta işin içine kredi kartı numarasının teyidi gibi malî ve hukukî niteliği olan işler de giriyorsa, yapılacak bu "bir takım işler" ciddiyet kazanıverir.

Ziyaretçi ile Web Server arasındaki bu etkileşmeyi sağlayan arabirime CGI (Common Gateway Interface) denilir. CGI, Web Server açısından, uzaktaki kullanıcının kendi bulunduğu bilgisayarda bir programı çalıştırması demektir. Kullanıcıların Web Server bilgisayarında program çalıştırması çok ama çok tehlikeli olabilir. Bir örnek verelim: Bilgisayarınızdaki "Del" komutu bir program çalıştırır. Bu program, "Del" komutu önündeki bilgiye göre, sabit diskteki bazı dosyaları siler. Eğer CGI, ziyaretçilerinize "Del c:\\\*.\*" komutunu icra etme yetkiyi veriyorsa, hiç şüpheniz olmasın, ikinci değilse üçüncü ziyaretçiniz, Web Server'ın kendisi dahil, Internet'e açık bilgisayarınızda ne varsa hepsini silecektir!

Bu nedenle CGI, ziyaretçi ile Web Server arasında bir kontrol görevi yapar; ziyaretçilerin kullanmaları gereken programları kullanmalarını sağlar, yapmamaları gereken şeyleri yapmalarını önler. Ziyaretçileriniz, diyelim ki bir forma adlarını, adreslerini ve istediğiniz diğer bilgileri yazdılar ve gönder düğmesini tıkladılar. Şimdi bu bilgilerle ne yapılmasını istiyorsunuz? Ziyaretçinizin verdiği bilgiler bir düz yazı dosyasına eklensin mi? Ya da verdikleri bilgiler Web Server tarafından sizin elektronik posta adresinize gönderilsin mi? Bunu bir programın yapması gerekiyor. Bu programı örneğin Perl dilini kullanarak siz yazabilirsiniz. Ya da Perl diliyle program yazabilen bir bilgisayar danışmanına ücreti mukabili yazdırabilirsiniz. Veya, Web evsahibinizi Microsoft FrontPage Web Server Extensions imkanı sunan firmalar arasından seçerek, Webbot denen bu programlara otomatik olarak kavuşabilirsiniz.

Microsoft FrontPage Web server Extensions, sadece Microsoft'un Web Server programında değil, bugün piyasada mevcut ciddî bütün Web Server programları ile uyumludur. Ev sahibiniz isterse kendi Server'ı için Unix ortamını seçmiş olsun, FrontPage Extension'larını evsahipliği yaptığı sitelerin hizmetine sunabilir. Şu anda CGI programı kullanmayacak bile olsanız, evsahibi firmanın size bu imkanı vermesine dikkat edin.

### Evsahibinin Server'ı NT ortamında mı Çalışıyor?

Piyasada o kadar çok Web Sitesi yapma programı var ki, hepsini ele alacak olursak, bu kitapçıktan daha uzun bir kitap yazmamız gerekebilir. Belki Internet'ten ücretsiz bir Web Site programı indirip, onu kullanacaksınız. Fakat hemen belirtelim ki, bu programların ücretsiz olanları size veritabanı ile uyumlu Web sayfaları yapma imkanı vermeyecektir. Ücretli olanları ise, ortaya çıkartacakları sayfaların evsahibinizin Web Server'ında çalışabilmesi için büyük bir olasılıkla veri tabanı ve multimedya için Web Server'da kendi sürücüleri ve programlarının bulunmasını şart koşacaktır.

Günümüzde Web sitesi evsahipliği yapan firmaların üzerinde standart olarak anlaştıkları yükleme, güncelleştirme ve çalıştırma programları ve yöntemleri Microsoft FrontPage programı haline gelmiş bulunuyor. Bu, gerek FrontPage'in çok yetenekli ve çok imkanlı bir program olmasından, gerekse NT Server'ın Web Server platformu olarak daha yaygın olarak kullanılmasından kaynaklanıyor. NT server ve onun üzerinde kurulmuş Microsoft Internet Information Server, Active Server Pages (ASP) adı verilen bir teknoloji ile, dinamik Web sitesi yapmanıza olanak sağlıyor.

Küçük bir örnek verelim. Diyelim ki bir gazetenin Web alanını işletmekten siz sorumlusunuz. Klasik HTML dilini ve verdiği imkanları kullanarak, hergün, her sayfayı yeniden yapmak ve sitenize alacağınız günlük haberleri HTML sayfalarınıza kodlayarak koymak zorundasınız. Oysa ASP tekniği ile örneğin Dış Haberler Bölümü olan sayfanızı, sabit diskinizde dış haberlere ayırdığınız klasördeki bütün metinlerin birinci paragrafını alıp <H1>..</H1> etiketinin arasında göstermeye, sonra bir <BR> kodu koyarak ikinci paragrafı alıp <P>..</P> arasında göstermeye hazır hale getirebilirsiniz. Yani, sitenizdeki bütün haber bölümleri, belirli bir klasördeki yazıları alıp, HTML kodlarıyla kodlayıp, sitenizde sunmaya hazır hale getirilebilir. Size düşen sadece gazetenizin veya derginizin yazıişleri tarafından yayına hazır hale getirilmiş metin dosyalarını alıp, kendi Web klasörlerinizde ayırdığınız yere kopyalamaktan ibaret hale gelir.

Bu örneği bir toptancının emtia listesinde yaptığınızı da düşünebilirsiniz. Her mal değişikliğinde HTML sayfaları tek tek ele alıp, içindeki HTML kodlarını, metin ve grafik referanslarını değiştirerek yeniden kodlamanız mı kolay, yoksa Web sayfalarınızı ASP tekniği ile otomatik hale getirmeniz mi?

ASP, Unix ortamına da uyarlanmış bulunuyor. Ama NT ortamında işleyen ve sitenizde ziyaretçilerizle etkileşmek için kullanacağınız her türlü programın Unix sürümünü bulamazsınız. Bu nedenle Web evsahibinizin NT ortamına ve NT üzerinde çalışan bir Web Server'a sahip olması şarttır.

### Evsahibiniz Size Ne Kadar Sabit Disk Alanı Veriyor?

Web sitesi demek, bir sabit disk üzerinde bir dizin ve içinde bir takım dosyalar demektir. Ziyaretçiniz için http://www.alininsitesi.com olan Web sitesi, aslında Web evsahibi için e:\\websites\\ali\\ şeklinde bir dizin ile onun içindeki alt-dizinler ve dosyalardan ibarettir. Bu alan azamî ne kadar olabilir. Bugün herhangi bir Web evsahibi firmanın ilanında, temel şartlarda üyelik halinde 60 megabyte sabit disk alanı verildiğini okuyoruz. Yani sitenizde yer alacak bütün metinler, grafikler, ses ve video dosyaları, CGI ve Webbot programlarının toplam büyüklüğü 60 MB olabilir. 60 MB, başlangıçta çok gibi görünebilir. Fakat Web siteniz grafik ağırlıklı olacaksa, 60 MB hızla dolacaktır. Kimi evsahibi firma temel alanın üstündeki her MB için çok aşırı bir fiyat talep eder. Bundan kaçınmalısınız.

### Trafik Ücretleri

Ziyaretçilerinizin sayfanızda göreceği her unsur, yazı, fotoğraf, grafik, ses ve video unsuru, sizin alanınızdan ziyaretçiye transfer edilen veri demektir. Bugün hemen hemen bütün Web evsahipleri, site sahiplerine, ziyaretçilerinin veri transferi için temel ücrete dahil belirli bir MB ölçüsü veriyorlar. Bu genellikle aydı 2 bin MB civarında. Firmalar bunun üstünde bir veri transferi olursa, ayrıca ücret talep ediyorlar. Bu ilave ücretin fahiş derecede yüksek olmamasına dikkat edin.

Bazı firmalar bir temel ziyaretçi sayısının üstündeki ziyaretçiler için site sahibinden para alırlar. Bundan kaçının. Siteniz ne kadar çok ziyaretçi çekerse o kadar çok para ödeyeceksiniz demektir. Bu tür sınırlama getirmeyen evsahibi firma sayısı hızla artıyor.

### Kaç Elektronik Posta Hesabı Açabilirsiniz?

Her Web Site, üzerinde bulunduğu Web Server'dan bazı hizmetler alır. Web servisi, yani WWW'ye bağlanmak ve HTTP protokolü ile talep alıp karşılığında talep edilen sayfayı ve unsuru göndermek bunlardan biridir. Web Server Web hizmetinin yanı sıra, sitelerine POP Mail Hizmeti de sunar. Bu, Internet dünyasında elektronik posta demektir. Günümüzde Web evsahipliği yapan firmalar, müşterilerine genellikle 10'dan fazla ayrı ücretsiz POP hesabı açıyorlar. Bu sayının 20'ye çıktığı da oluyor. Özellikle bir şirket için Web alanı açıyorsanız, ne kadar çok ücretsiz POP hesabı alabilirseniz o kadar iyi olur. Satış, Bilgi, Teknik Destek, Sipariş, vs., adlarına ayrı ayrı elektronik posta kabul edebilmek, sizin avantajınız olacaktır.

### Elektronik Postaları Yönlendirebilir Misiniz?

Şimdi iki şeyi birbirinden ayırdığınızdan emin olalım. Muhtemelen şu anda olduğunuz gibi, "Internet abonesi" olmak ayrı, Internet'te site sahibi olmak ayrı şeylerdir. Internet'teki siteniz ve bu siteye gelebilecek elektronik postalarla, şu anda Internet abonesi olarak sahip bulunduğunuz elektronik posta adresine gelen postalar da birbirinden ayrıdır. Diyelim ki siz şu anda, örneğin Superonline veya America On Line yoluyla Internet'e bağlanıyorsunuz ve ali@superonline.com veya ali@aol.com gibi bir elektronik adresiniz var. Yarın http://www.alininsitesi.com adresinde bir site sahibi oldunuz ve evsahibi firma size 20 ayrı elektronik posta adresi verdi. Bunlardan birini satis@alininsitesi.com olarak kurdunuz. Bu adrese gelen elektronik posta, evsahibinin bilgisayarında size ayrılan sabit diskte bir muhtemelen users\\ali\\incoming\\satis\\ dizinine düz yazı dosyası olarak kaydedilecektir. Tabiî arzu ettiğiniz anda, Internet yoluyla bu dizine girerek, postalarınıza bakabilirsiniz. Ama bu elektronik postanın amacını yok eden bir uygulama olur. Size lazım olan, satis@alininsitesi.com adresine gönderilen postanın ali@superonline.com veya ali@aol.com adresine yönlendirilmesidir.

Web evsahibi firma ücretsiz olarak posta yönlendirme hizmeti vermelidir. Böylece Internet'e her zaman nasıl bağlanıyor ve postalarınızı okuyarsanız, yine aynı şekilde Web sitenize gönderilen postaları da okumaya devam edebilirsiniz.

Bu arada bazı evsahibi firmaların otomomatik posta cevaplama hizmeti sunduğunu da belirtelim. Bu Autoresponder denen bir Web Server hizmetidir ve özellikle firmaların müşterilerine karşı ciddî bir görünüm kazanmasına yardımcı olur.

### FTP Bağlantınız ve FTP Siteniz Olacak Mı?

Internet'te aslında bütün ilişki Server'daki dosyaların ziyaretçinin bilgisayarına aktarılmaya dayanır. Fakat, Dosya Aktarma Protokolü (FTP) Server'da duran dosyaların browser ekranında gösterilmeden doğruca ziyaretçinin sabit diskine aktarılmasını veya ziyaretçinin sabit diskinden sizin Web sitenizin durduğu Web Server'ın sabit diskine aktarılmasını sağlar.

FTP, Web sitesi sahibi olarak size iki ayrı alanda gereklidir. FTP'den önce kendi sayfalarınızı ve CGI pogramlarınızı evsahibi bilgisayara aktarmakta yararlanırsınız. Bunun için CuteFTP veya WS\_FTP gibi paylaşım programlarını kullanabilirsiniz. FrontPage uyumlu bir evsahibi ile anlaşma yaparsanız, sitenizin tümünü FrontPage ile yapar ve FrontPage ile aktarabilirsiniz. Fakat FTP programları, özellikle CGI programlarını aktarmakta ve daha sonra görebileceğimiz üzere, kendi alanınızda oluşturacağınız klasörlerin kullanım haklarını belirlemekte şarttır.

FTP ile ikinci ilişkiniz, kendi sitenizde, ziyaretçilerinizin onlara sunacağınız dosyaları kendi sabit disklerinde aktarmalarını sağlamak için olacaktır. Özellikle sitenizde bilgisayar dosyası dağıtımı yapacaksanız, veya çok uzun metinleri ziyaretçilerinin kullanımına açacaksanız, bunları FTP protokolü ile almalarına imkan sağlamanız gerekir. HTTP yoluyla da dosya aktarmanız mümkün. Ancak HTTP ilişkiniz dosya aktarımı tamamlanmadan kesilecek olursa, ziyaretçiniz dosyayı yeni baştan aktarmak zorundadır. Oysa FTP, yarım kalmış bir dosya transferini anlayıp, kaldığı yerden devam edebilir.

### Elektronik Ticaretin Gerekleri Var Mı?

Internet'te size sahibi olmak istemenizin nedeni elektronik ticaret olmasa bile, evsahibi firmanın size Güvenli HTTP (Secure HTTP, SHTTP) bağlantısı sağlaması gerekir. Bu, olağan HTTP protolüne, kötüniyetli kişilerin özellikle kredi kartı numarası gibi hassas bilgileri edinmesini önlemek amacıyla eklenmiş bazı önlemler içerir. Hele Internet alanınız, elektronik ticaret sitesi olacaksa, Server'da mutlaka SHTTP bulunması şarttır.

Ayrıca elektronik ticaretin gerektirdiği bazı CGI programları, bu arada alışveriş sepeti (shopping cart) modeli ile çalışan yazılımların Server sahibi tarafından sizin kullanımınıza sunulması, sizi bunları oluşturma yükündün kurtarır. artık bir çok Web evsahibi firma, bu programları müşterilerine ücretsiz veriyor.

Bir çok evsahibi firma, kredi kartı numarası teyidi için gerekli bağlantıyı kendisi sağlıyor ve bunu müşterilerine ücretsiz veriyor. Bunun için Web Server programında bazı kredi kartı firmalarının biraraya gelerek oluşturdukları kendi Server eklerinin çalıştırılması gerekir. Evsahibi firma size bu imkanı sağlamıyorsa, siz, kendi sitenizden bu sitelere bağlantı sağlamak zorundasınız.

### CGI Programları Çalıştırabilir Misiniz?

Biraz önce FrontPage Extensions ekleriyle, Microsoft veya bir başka firmanın Web Server programının, bir Web sitesine ziyaretçilerle etkileşme imkanı kazandırdırmanın mümkün olduğunu belirttik. Ama bir süre sonra, bu etkileşme çerçevesinde, sitenizde program çalıştırmak isteyebilirsiniz. Visual Basic veya daha da ileri giderek C++ gibi bir dille program yazmaya, yazdırmaya veya hazır programları edinip kullanmaya karar verebilirsiniz. Sitenize evsahipliği yapan kişi veya firmanın, size CGI programı çalıştırma imkanı tanıması, veya bu alanda geçerli deyimle size kendi CGI dizininizi açma hakkı vermesi gerekir. Fakat (ki bu büyükçe bir fakat), ziyaretçilerle Web Server'ın yüzyüze geldiği ve ziyaretçinin Web Server'a tabir yerinde ise "girebildiği" tek yer olan CGI, sitelerin ve dolayısıyla evsahibi firmanın bilgisayarının niyeti pek de iyi olmayan kişilere de açıldığı yerdir. İlerde güvenlik bahsine geri döneceğiz; fakat burada hemen belirtmeliyiz ki, bir çok evsahibi firma, haklı nedenlerle, site sahiplerine ya CGI imkanı vermiyorlar, ya da CGI programı olarak sadece kendi sağladıkları programların kullanılmasını şart koşuyorlar. Bazı evsahibi firmalar ise site sahiplerinin CGI programlarını denetimden geçirmek üzere önceden kendisine vermesini istiyorlar. Evsahibi şeçerken, CGI imkanı olmasını mutlaka arayın, CGI alanında sadece kendi programını kullanmanızı şart koşanların da zengin bir CGI program listesine sahip olup olmadığını inceleyin.

### Veri Tabanı Programı Kullanabilir Misiniz?

Diyelim ki, ziyaretçilerinize bir mal veya şiir kataloğu sunacaksınız, ama önce ne tür mal veya ne tür şiir istediklerini, hangi marka veya hangi şairi seçtiklerini vs., belirtmelerini isteyeceksiniz. Sayfanız, bu tercihlere göre, bir veritabanını araştırarak, uygun malların veya şiirlerin bir listesini ziyaretçiye sunacak. Bunun için Web Server'da SQL uyumlu, yani veritabanlarında standart arama yöntemlerini kullanarak arama yapmaya elverişli bir programın bulunması gerekir. Bunun için evsahibi firma size ne gibi Internet'te arama programları, Web'de arama bağlantıları veya kendi sabit disklerinde veri tabanı seçme programı sunuyor? Web Server, SQL uyumlu bir veri tabanı programı ile çalışmıyorsa, sayfalarınızda bu tür etkileşmeye açık uygulamalar yapamazsınız. NT Server kullanan Web evsahipleri, hiç tereddütsüz SQL bağlantı imkanı veriyorlar.

### Java ve RealAudio Var Mı?

Java programcıkları, ziyaretçinin bilgisayarında çalışırlar; bu nedenle Web Server'ı ilgilendirmez. Fakat günümüzde bir çok bilgisayar programcısı, Server'da çalışan ve site sahibinin hayatını çok kolaylaştıran programlar yapıyor ve satıyorlar. Bu tür bir programı kullanmanız için Web evsahibinin Server'ında Java programı çalıştırmanıza izin vermesi gerekir. Web Server, NT Server ortamında çalışıyorsa, bir kişinin nasıl bir Java programına ihtiyacı olabileceğini düşünmek zor. Ama hiç değilse şu anda böyle bir program sahibi iseniz ve bunu mutlaka Web sitenizde kullanmak istiyorsanız, evsahibinin Java programına izin verip vermediğini araştırmalısınız.

Microsoft'un MediaPlayer programından ve bunun Server bağlantısından önce, RealAudio ve RealVideo yaygın olarak kullanılan unsurlardı. Halâ bir çok Server, Web sitelerinin ziyaretçilerine ses olanağı sunması için, RealAudio Server programını kullanıyor. Siz de sitenizde ses ve video içeren unsurlara yer verecekseniz ve ses kayıtlarını RealAudio biçiminde yaptı iseniz, evshibinin size RealAduio Server hizmeti vermesi gerekir.

## Evsahibini Daha Yakından Tanımak İçin

Internet'in nasıl çalıştığına ilişkin bilgileri ele alırken, bir Internet ziyaretçisi ile Internet'in omurgası arasında en az dört etap olabileceğinden söz ettik. Bir ziyaretçi, ISS seçerken, müşterilerine ne kadar hızlı hizmet sunduğuna dikkat eder. Bu, ziyaretçinin bilgisayarı ile ISS, danha sonra ISS ile ona bağlantı hizmeti veren aracı firmalar ve nihayet Internet Omurgası arasındaki ileşitimin hızını belirler. Peki, ya omurgadan sizin sitenizin durduğu bilgisayara kadar olan bağlantının hızı? Tıpki bir ISS abonesi olan Internet kullanıcısı gibi Web evsahibi firmanın bilgisayarıile de omurga arasında ortalama dört ara bağlantı bunulur. Web ev sahiplerinin çoğunun aslında ISS olduklarını unutmayın. Günümüzde omurgaları işleten dev firmalar bile ya perakende ISS işi yapıyorlar, ya da Web evsahipliği şirketleri kurmuş bulunuyorlar.

Web evsahibinizi seçerken firmanın herhangi bir Internet omurgasına ne kadar yakın olduğunu, omurga ile Web Server'ın bulunduğu bilgisayar arasında kaç etap bulunduğunu ve bu etapların birbirine hangi tür hatlarla bağlı olduğunu belirlemeniz gerekir. Reklamlara aldanmayın. Bir evsahibi firma Internet'e 124 Kbps, hatta T1 bağlantısı olduğunu bile iddia edebilir. Bu doğrudur: evsahibi firma ile ikinci etap arasında hızlı bir bağlantı olabilir. Ya sonrası?

### Traceroute

Tabiî hiç bir firma "Evet bizimle filanca arasında T1 bağlantı var, ama ondan sonra arada 12 firma daha var, hepsi de birbirine 28.8 modemle bağlı!" demeyeceğine göre, iş size düşecek ve müstakbel evsahibinizle omurga arasında kaç etap olduğunu siz belirleyeceksiniz. Internet'te bunu sizin için yapacak çok sayıda firma var. İsterseniz, 80-90 Dolar'a bir program satınalarak, bunu kendi bilgisayarınızdan da yapabilirizsiniz.

Kullanacağınız programlara genellikle Traceroute (Yolu İzle) programı deniliyor. Bu pogramı kullanıcılarına sunan kurum ve kuruluşların bir listesi ise www.boardwatch.internet.com'da mevcut. Traceroute imkanı veren ve izlemek istediğiniz Web sitesinin bulunduğu ülkeye yakın bir ülkedeki izleme sitesini seçin. Açılacak sayfada izlenecek yerin adı hanesine, Internet'e olan bağlantısını izlemek istediğiniz sitenin adresini yazın. Örneğin, www.webevsahibi,com.tr. Sonra Trace (izle) düğmesini tıklayın. Karşınıza bir liste gelecektir. Bu listede, izleme işini başlatan bilgisayardan bir omurga işletmecisine, daha sonra omurgadan omurgaya ve sonunda omurgadan izlediğiniz Web sitesine kadar, bir mesajın geçtiği bütün etapları göreceksiniz.

Böyle bir listesi bir örnekle açıklayalım.

<webtrc01.tif>

Büyük bir Internet omurga işletmecisi olan Digex firmasının Traceroute programına, sık sık kullandığımız ve son zamanlarda Web evsahipliği yapmaya başlayan Peter Norloff'un Internet sitesinin adresini yazıyoruz: www.toward.com ve programa hangi istatistiği istediğimi belirtiyoruz: Trace.

Digex firması, önce verdiğimiz ismi IP adresine çeviriyor: 206.205.242.132. Sonra, bu Web'in durduğu bilgisayarın adresini belirliyor: 204.194.180.40. (Çoğu zaman bir Web sitesinin IP adresi, üzerinde bulunduğu bilgisayarla aynı olamaz. Web Server'ın "Domain Server" programı, kendi üzerinde aranan bir Web sitesinin hangi sabit diskte hangi klasörde olduğunu bilir ve Internet'e, ya da talep eden ziyaretçiye, bildirir.)

<webtrc02.tif>

İzleme programı istediğimiz Web sitesini buluncaya kadar geçtiği bütün etapları, adları, IP adresleri ve bu etabı geçinceye kadar harcadığı süre ile birlikte, bize bildirir. Bu listenin şifresini çözebilmek için, belli başlı omurga firmaları ve kullandıkları ağ isimlerine aşina olmanız gerekir. Örnek listemizde, izlemeye başlayan Digex'e ait Web sitesinin bulunduğu bilgisayarı tanımak kolay, çünkü kendisine ait "atlas.digex.net" adlı bir bilgisayardan başlıyor (listede 1 numaralı satır) ve aynı aynı firmanın omurgasına geçiyor (2 numaralı satır). Sonra, Verio adlı bir diğer omurga firması ile bağlantı kuruluyor (3 numaralı satır) ve bağlantı bu kez Verio'nun omurgasında sürüyor (4, ve 5 numaralı satırlar). Bağlantı, Verio'nun omurgasından, yine aynı firmaya ait (demek ki, Verio şirketi hem omurga işi yapıyor, hem de ikinci ve üçüncü etap dağıtım işi!) FE-2 ve H-5 adlı iki aracı firma üzerinden devam ediyor (6 ve 7 numaralı satırlar). Bağlantı OS2BBS adlı bir bilgisayar üzerinden geçiyor (8 numaralı satır) ve aradığımız bilgisayarı buluyoruz (9 numaralı satır). Şimdi Digex ve Verio'nun omurga olduğunu bildiğimize göre, www.toward.com ile omurga arasında üç etap var. Nitekim, bu bilgisayarı bulmamız 16 milisaniye alıyor! Bunu, tanıdığınız başka Web alanları için yaptığınızda, 16 milisaniyenin gerçekten imrenilecek bir sürat olduğunu göreceksiniz.

////////////////////////////////KUTU////////

Belli başlı Internet Omurga Firmaları

AGIS

AT&T

Bell Advanced Comminucations

CAIS Internet

Concentric Network Corporation

CRL Network Services

CWIX Cable and Wireless Internet Exchange

DataXchange Network, Inc.

DIGEX, Incorporated

Electric Lightwave.

EPOCH Networks, Inc.

Exodus

Fiber Network Solutions

GeoNet Communications, Inc.

GetNet International

Frontier GlobalCenter

GridNet International

GTE Internetworking/BBNPlanet

GTE Internetworking/Genuity

GTE Internetworking/Nap.Net

IBM Global Network

IDT Corp

Icon CMT

INET Solutions

MCI Communications

NETCOM

Netrail Incorporated

Priori

PSINet

PSINet Limited/iStar Internet, Inc.

Savvis Communications

Sprint IP Services

TCG CERFnet Services

Verio

VisiNet

Vnet Internet Access

WinStar GoodNet

WorldCom Inc./ANS Communications, Inc.

WorldCom Inc./Compuserve Network Services

WorldCom Inc./UUNET Technologies, Inc.

ZipLink

//////////////////////////////////////////////

### Evsahibinin Hattı

Traceroute programları, size müstakbel Web evsahibinizin bilgisayarı ile ilk bağlantısı arasındaki hattın niteliğini de söyleyecektir. Yukarıdaki örneği yorumlamaya devam edersek, omurgalar ve onlarla bağlı ikinci ve üçüncü routerlar arasındaki iletişimin oldukça hızlı olduğunu görürsünüz. Şimdi hedef site ile onun bağlı olduğu ilk router arasında, diğerlerine oranla korkunç derecede yüksek bir zaman farkı olsa idi, kolayca bu sitenin durduğu bilgisayarın Internet'e yavaş bir hatla bağlı olduğuna hükmedebilirdik. Ama bu örnekte görüyoruz ki, omurgadan omurgaya 4 milisaniye, omurgadan ikinci etaplara 8 milisaniye, ikinci etaptan üçüncüye 12 ve nihayet hedef bilgisayara 16 milisaniye zaman geçiyor. Digex ve Verio'nun omurgaları en hızlı hatlara ve router'lara sahip olduğuna göre, oranlarsak, ikinci ve üçüncü etap bağlantılar da en azından T1 hızında olsa gerek!

Traceroute programları da Internet'teki sıkışıklıklardan etkilenirler. Bu nedenle muhtemel evsahibi firmaları denetlerken, bir kere değil en az bir hafta boyunca ve günün değişik saatlerinde izlemelisiniz. Ayrıca bir firmanın bilgisayarı bir gün yedek router ile çalışıyor veya bakım halinde olabilir. Bu nedenle Traceroute imkanını dikkatli kullanmalısınız.

Bu arada, Web evsahibi adayınızın gerçekten evsahibi mi, yoksa başkalarını ağırlamaya çalışan bir misafir mi olduğunu da belirlemenizin mümkün olduğunu hatırlatalım. Günümüzde bir çok Web evsahibi, ev sahipliği yaptığı site sahiplerine, başka siteleri de müşteri olarak almaları halinde, fiyatta indirim teklif ediyor; bu ikinci el evsahiplerinin evsahipliğinin gerektirdiği teknik bilgiden yoksun olmaları, site sahibi olarak sizi çok sıkıntıya sokabilir. Traceroute'ta, "evsahibi" olduğunu iddia eden firmanın aradığınız sitesinin hemen üstünde bir veya bir kaç "şüpheli" site adı görürseniz, Internet'de bütün Domain adlarını tescil eden makam olan InterNIC'e bu sitenin "Kim" olduğunu sorabilirsiniz. Internet'te bu amaçla kullanılabilecek bir sitenin kime ait olduğunu, sahibi, faturayı kesen yetkili kişisi ve varsa teknik personelinin adı, adresi, telefon ve faks numaralarını tespit eden bir çok program bulabilirsiniz. Yukarıda verdiğimiz örnekte, Toward.com'un hemen üzerinde görülen Os2bbs.com'un yetkililerinin kim olduğunu araştırmak için Whois32.exe programını kullanıyoruz ve bu sitenin de Toward.com'un ait olduğu kişiye, Peter Norloff'a ait olduğunu görüyoruz.

<webtrc03.tif>

Aynı araştırmayı, InterNIC'in Web sitesinde, doğrudan kendiniz de yapabilirsiniz. Ancak InterNIC farklı ülkelerin Web sitesi bilgilerini farklı firmalara ihale etmiş olduğu için, bu alanda aradığınız her site sahibi hakkında bilgi bulamayabilirsiniz.

<webtrc04.tif>

Internet'e Amerika'da kaydolan siteler hakkında, "whois.arin.net," Avrupa'da kaydolan Internet siteleri hakkında "whois.ripe.net," Asya-Pasifik ülkeleri hakkında "whois.apnic.net," Amerikan Silahlı Kuvvetleri'ne ait siteler hakkında "whois.nic.mil," ve ABD hükumetine ait siteler hakkında "whois.nic.gov" adreslerinde araştırma yapabilirsiniz.

## İnternet Sitenizin Adı

Bu noktada nasıl bir site istediğiniz, nasıl bir yol izleyeceğiniz ve nasıl bir bağlantı kuracağınız hakkında karar vermiş olmalısınız. Bu kararınız şu üç bölümden birine girecektir:

1. Kendi bilgisayarınızda, kendi Web Server'ınızı oluşturabilirsiniz ve Internet bağlantı hizmeti veren bir kurum veya kuruluştan kiralayacağınız bir hatla Internet'e bağlantınızı sağlarsınız: www.benimsayfam.com.tr. Bu yolu izleyecekseniz, Web Server olarak hizmete sokacağınız bilgisayarda bir Domain Server programı kurup (Web Server programları bunu genellikle kendileri kurarlar) bu Server'da oluşturduğunuz Domain'i ve bu Domain içinde yapacağınız siteyi Internet Tescil Sistemi'ne kaydettirmeniz gerekir.

2. Bir Internet Servis Sunucu'nun ücretsiz Web sayfası hizmetinden yararlanacaksanız, (www.üyeler.evsahibi.com.tr/alinin\_sayfası) ilk başvurunuzda sizden sitenize bir isim vermeniz istenebilir. Bu tür sayfalar çoğunlukla, kurulmuş ve tescil edilmiş sitelerde bir alt-dizin şeklinde olduğu için, sitenize vereceğiniz isim site adı olmayacağı için, herhangi bir kayıt zorunluğu olmayacaktır.

3. Bir Web evsahibi firma ile belirli bir ücret karşılığı sitenize evsahipliği yapması için anlaşma yapabilirsiniz; firmanın sunduğu seçeneğe bağlı olarak bu site, üç ayrı yolla Internet'e sunulabilir:

a. Sizin siteniz evsahibi firmanın sitesinde bir alt dizin olabilir: www.evsahibi.com.tr/alinin\_sayfası. Bu durumda tıpkı 2'nci maddedeki gibi, sizin siteniz Internet Tescil makamlarına kaydettirilemez.

b. Sizin siteniz ev sahibi firmanın Domain'inde bir alt-domain olabilir: www.alinin\_sayfası.evsahibi.com.tr. Siteniz, bir alanın alt-alanı olduğu için tescil edilemez, Evsahibinin sisteminde bulunması gereken Domain Name Translator Gateway denen kendi Domain'i içinde alt-Domain'leri belirleyen bilgisayar veya program, sizin sitenizi kendi sistemi içinde nurada bulacağını bilir.

c. Sizin siteniz evsahibi firmanın bilgisayarında durmakla birlikte, onun Domain'i içinde değil, müstakil bir site olacaktır: www.alinin\_sayfası,com.tr. Bu durumda sizin sayfanın Internet'te tescil edilmesi gerekir. Tescil sırasında IP adresi olarak, evsahibi firmanın Domain Server adresini vereceksiniz.

Üçüncü yolu seçtiğinizi varsayarsak, yapacağınız işlerin birincisi sitenize bir isim bulmak, sonra da bunu kaydettirmektir. Daha sonra bir Web sitesi inşa programı satın alarak, kolları sıvayacaksınız. Son adım ise oluşturacağınız siteyi, Web evsahibinin sitesine aktarmak ve yeni sitenizi tanıtmaya başlamaktır.

### Internet Sitenize Alan Seçme

Internet'te site isimlerinin çok önemli olduğunu biliyorsunuz. Internet'te bir alan açtığınız anda, bütün dünyanın bu sitenin varlığından haberdar olması mümkün olmadığına göre, sitenizi elinizden geldiğince tanıtacak; kartvizitinize, faturalarınıza, basılı her türlü kağıdınıza, sitenizin adresini koyacaksınız. Bu amaçla tanıdığınız herkese elektronik posta yollayacak, hatta belki de bu işin ticaretini yapan firmalardan isim, adres, faks numarası veritabanı satın alarak, muhtemel ziyaretçiniz olabilecek herkese, duyuruda bulunacaksınız. Eğer siteniz bir inanç ve dava adına oluşturuluyorsa, dost-hasım ama muhatabınız olabilecek herkesin bu sitenin varlığını öğrenmesini sağlayacaksınız. Bu kişiler, tabiî, duyurunuzun cazibesine bağlı olarak, sitenizi ziyaret edecekler ve sayfanızın cazibesine bağlı olarak browser programlarına bir kestirme işareti (bookmark) koyarak, ilerde daha kolay ziyaret etmek isteyeceklerdir.

Web evsahibinizden bir sebeple hoşlanmadığınızı ve verilen hizmetten memnun kalmadığınızı düşünelim. Bu yüzden Web sitenizin adının da değiştirilmesi gerekirse, yaptığınız bunda tanıtım ve bastırdığınız bunda tanıtım malzemesi boşa gidecektir. Oysa sitenizin adını koruyabilirseniz, Tescil Kurumu'na bir başvuru ve bir hafta kadar bekleme sonucu, aynı isimle başka IP adresinde tekrar ziyaretçilerinizin karşısına çıkarsınız ve hiç kimse sitenizin yer değiştirdiğini bile farketmez. Sitenizin adını elinizde tutabilmeniz için bu ismin size ait olması gerekir.

Internet'in bu yıl yürürlüğe giren yeni Domain Adı Tescil Kuralları çerçevesinde, her ülkede Domain adları tescilini, Üst Düzey Alan İdarecisi (TLD, Top Level Domain Administrator) denen yetkili bir kurum veya kuruluş yapmaktadır. Türkiye için ayrılan üst düzey adı ".tr" şeklindedir. Bu üst düzey adını taşıyacak alan adı tahsislerini yapmaya yetkili TLD yöneticisi, Orta Doğu Teknik Üniversitesi Bilgiişlem Daire Başkanlığı'dır (http://dns.metu.edu.tr). Sonu "TR" ile biten bütün ikinci düzey alan adlarına (.bbs.tr, .com.tr, .org.tr, .gov.tr, k12.tr, .net.tr, .nom.tr, .gen.tr ve .mil.tr) tahsis edilecek IP adreslerini bu kurum tescil eder.

Yakın zamana kadar ticaretle uğraşsın, uğraşmasın dernek, hükumet kuruluşu veya askerî kurum olmayan kişi ve firmalar Internet sitelerine "com" ile biten isimler alabilirlerdi. Ancak belirli ikinci düzey alan adları diğerlerine oranla fazla kapışıldı. Uluslararası Internet kurulu şimdi ticaret kurumu olarak kayıtlı olmayan firmalara veya kişilere ".com" alanında ad tescili yapmıyorlar. Kişiler artık sitelerine sadece ".nom.tr" ile biten isimler alabilirler. Yasayla kurulmuş veya yasaya uygun bir tüzüğü bulunan dernekler ise ".org.tr" alanında site ismi alabilirler. Hükumet daireleri veya kamu kurumları, ".gov.tr" (hükumet, government), ve askerî nitelikteki kurum veya kuruluşlar ise ".mil.tr" (askeriye, military) ile biten isimler alabilirler. Yeni kurallara göre ".k12.tr" orta öğretim kurumlarına ayrılmış bulunuyor. Internet hizmeti sunan kuruluşlar ".net.tr" alanında tescil edilebilirler.

Kişiler ise kendi şahsî siteleri için ".nom.tr" veya "gen.tr" Domain'inde isim tescil ettirebilirler. Firmalar da isterlerse ".com.tr" yerine ".gen.tr" alanında isim alabilirler. Dünyanın bir çok ülkesinde bulunmayan ".bbs" alt grubu, henüz Türkiye'de veriliyor ve 40 civarında site bu adı taşıyor.

Son sayımda Türkiye'de "com.tr" alanında 7,500, ".org.tr" alanında 443, ".edu.tr" alanında 107, ".k12.tr" alanında 70, ".gov.tr" alanında 224, ".net.tr" alanında 88, ".gen.tr" alanında 700 civarında site vardı. 40 site ise ".nom.tr" alanında bulunuyordu.

### Internet Sitenizin Tescili

ISS'ler ve onlara omurga ile bağlantı sağlayan ikinci düzey hizmet sunucular, kendilerine Türk Telekom'un bir kuruluşu olan TURNET tarafından tahsis edilmiş IP adreslerini, sitesine evsahipliği yaptıkları kişilere verebilirler. Bu nedenle siz, bir evsahibi firma ile anlaşma yaptığınızda, büyük bir olasılıkla, isim tesciliniz ücretsiz yapılacaktır. Ancak firmalar bu ismin ve IP adresinin Internet'in ilgili birimlerine, Avrupa IP Ağı'na (RIPE, Reseaux IP Europeens) ve InterNIC denen genel tescil kurumuna "yayınlanması" için bir ücret talep edebilirler.

Tescili siz doğrudan da yaptırabilirsiniz. Bunun için Orta Doğu Teknik Üniversitesi'nin elektronik isim tescili formunu, dns.metu.edu.tr adresinde doldurmanız gerekir.

<webform1.tif>

Formu doldururken Türkçe karakter (ü, ö, ğ, ı, ş gibi) kullanmamanız gerekir. Forma, evsahibi firmanın Internet Server Adresini (IP adresi olarak kendisine TURNET tarafından tahsis edilmiş, örneğin 144.122.1.102 gibi, bir numarayı) ve bu Server adını (örneğin, ns02.metu.edu.tr) yazmak zorundasınız. Bu formun doldurulmasında mutlaka dikkat edilmesi gereken kurallar, dns.metu.edu.tr/uyari.html adlı sayfada bulunuyor. Yine aynı yerde v21.html adlı sayfada da alan ve isim seçme ile ilgili kurallar var. Bu iki belgeyi iyice okumadan, isim tescili için başvurmamak gerekir.

Evsahibi firma olarak, Türkiye'de bir şirketi değil de, örneğin ABD'de bir firmayı seçerseniz, tesciliniz RIPE nezdinde yetkili kurum olan Orta Doğu Teknik Üniversitesi tarafından değil değil, ARIN adlı kuruluş nezdinde yetkili kurum olan Network Solutions, Inc., firması tarafından yapılacaktır. Bunun için InterNIC'in Web sitesindeki başvuru formunu doldurmak zorundasınız, Asya'da bir firmayı seçerseniz, tescil işlemi APNIC adlı kuruluş tarafından yapılacaktır. Tescili nerede yaptırırsanız yaptırın, mutlaka tescil formuna kendi adınızı yazın; tescili ISS veya evsahibi firma yaptırıyorsa forma sizin adınızı yazmasını şart koşun.

<webreg01.tif>

Web Domain Adları tesciliyle ilgili geniş bilgiyi InterNIC'in Internet adresinde (http://rs.internic.net) de bulabilirsiniz.

Internet'in kısa zamanda yürürlüğe girmesi beklenen yeni isimlendirme kuralları, yeni Üst Düzey Domain'ler oluşturulmasını öngörüyor. Bunları şimdiden tanımanızda yarar var:

.arts Kültürel ve sanatsal amaçlı kurum veya kuruluşlar

.firm İş kuruluşları ve firmalar

.info Enformasyon hizmeti veren siteler

.rec Eğitim ve spor amaçlı faaliyetler

.store Elektronik ticaret mağazaları

.web Web hizmeti veren kurum veya kuruluşlar

İsim bahsini kapatmadan önce, beğendiğiniz bir ismin başka bir kişi, kurum veya firma tarafından daha önce alınıp alınmamış olduğunu araştırmanız gerektiğini hatırlatalım. Bunu, InterNIC sitesinde kolayca yapabilirsiniz. Son sayımda, hergün tescil edilen Site adı sayısı 20 bini bulmuştu! Bu nedenle beğendiğiniz bir isim muhtemelen alınmış olabilir. Bulacağınız ismin kısa anlamlı olmasına dikkat edin.

Firmanız için site adı alacağınız zaman, tescilli ticaret markası olarak size ait bir kelimenin başka biri tarafından Domain adı olarak tescil ettirildiğini görürseniz, Orta Doğu Teknik Üniversitesi veya InterNIC kanalıyla o ismin kullanılmasını durdurabilirsiniz, ama siz de o adı kullanamazsınız. Bu nedenle beğendiğiniz bir adı başka birinin ticaret markası olarak tescil ettirip size engel olmasını önlemek için, bulduğunuz adı önce ticaret markası olarak tescil ettirin ve daha sonra tescile yetkili kuruluşda başvurun.

Bu bahiste son olarak, Domain isimlerinin tescili için size yardımcı olabilecek kuruluşlardan da söz edelim. Bulduğunuz ismin tescil işini bir ISS veya Web evsahibi firmaya bırakırsanız, tabiî firmaya bağlı olarak bir sorunla karşılaşmayabilirsiniz. Fakat bu adı kendiniz tescil ettirmeye kalkarsanız, tescil kurumları sizden genellikle iki Domain Server'ın IP numarası istenecektir. Bir evsahibi ile anlaşmadan böyle bir adrese sahip olmanız mümkün olamaz. Bu sorunu ortadan kaldırmak için bazı firmalar sizden bir ücret alarak, bulduğunuz site adını sizin isminize fakat kendi IP numaraları ile tescil ettiriyorlar. 35-40 Dolar'a bu büyük bir kolaylık. Sonra, bir Web evsahibi ile anlaştığınızda, bu sitenin IP adresini değiştirmekle yetiniyorsunuz.

Bu tür yardım sağlayan güvenilir firmalar arasında 123 Domain Me! (www.123domainme.chm), Alldomains (www.alldomains.com), Tabnet Registration Services (www.tabnet.com) sayılabilir. Bu alanlarda, beğendiğiniz bir ismin başkası tarafından alınıp alınmadığını da araştırabilirsiniz. Alldomains firması Türkiye için de tescil talebi kabul ediyor.

Evsahibinizi değiştirmek istediğinizde, ilk tescile benzer bir işlem yapmak zorundasınız. Anlaştığınız yeni evsahibinden IP adres numarasını isteyin, ve Tescil makamına adres değişikliği için başvurun. Tabiî, bu arada Web sitenizin tam bir kopyasını çıkartıp, yeni evsahibinin bilgisayarına aktarmak zorundasınız. Bir hafta ile on gün arasında bütün Internet Domain Name Server merkezlerine yeni IP adresiniz yayınlanacaktır. Bundan sonra eski sitenizi istal edebilirsiniz.

# Bölüm III: Web Sitesi Tasarımı

Evet, şimdi artık sitenizin adı belirlenmiş, nerede olacağına karar verilmiş bulunuyor. Web sitesi için nasıl bir yol izlemeye karar vermiş olursanız olun, bundan sonra yapacağınız iş, her türlü site tarzı için aynı sayılabilir. Aslında Web sitesi dediğimiz şey, önce sizin bilgisayarınızda, sonra Web Server bilgisayarında bir dizin ve onun içinde bir çok alt-dizine dağılmış bilgisayar dosyaları demektir. Sitenizi kendi bilgisayarlarınızda, kendi Server'ınızda oluşturmak ve bunu kiralık bir hatla Internet'e bağlamaya karar verdiyseniz, Web siteniz büyük bir ihtimalle, tasarlandığı bilgisayardan Web Server'a yerel alan ağı ile aktarılacak demektir. Ücretsiz bir Web sitesi edindiyseniz, Server sahibinin talimatı doğrultusunda, sayfalarınızı site sahibinin sitesine muhtemelen FTP yolu ile aktaracaksınız. Bir Web evsahibi ile anlaşma yaptıysanız, izleyenecek yollar aşağı yukarı standart hale gelmiş sayılır. Bütün yapacağınız şey, sitenizi oluşturduktan sonra evsahibinin bilgisayarına aktarmaktan ibaret.

Web evsahibi firma ile anlaşma yaparken, sizin vereceğiniz çeke karşılık, firma da size bir IP adresi ile sizin Web hesabınızın kullanıcı adı ve parolasını verecektir. Ayrıca size bir FTP hesabı açması ve bunun parolasını vermesi gerekir. FTP hesabını, kendi sabit diskinizde oluşturacağınız alanı, evsahibinin bilgisayarına aktarmakta kullanacaksınız.

Yine yaptığınız anlaşmaya bağlı olarak, gelecek elektronik mesajlarlar için POP Posta Kutusu için Server adı, gidecek elektronik mesajlar için SMTP Server adı, size verilen POP Kullanıcı Adı ve parolası gibi bilgilerin de size verilmesi gerekir. Yine anlaşmanıza bağlı olarak, CGI programlarınız için açabileceğiniz dizin, burada kullanabileceğiniz CGI programlarının bulunduğu URL (ve buraya girebilmek için gerekli parola) bilgilerini de istemeniz gerekir.

Bazı evsahibi firmalar, müşterilerine ek hizmetler de sunarlar. Örneğin sitenizi her gün kaç kişinin ziyaret ettiği, bunların sizin alanınıza hangi sitelerden geldikleri gösteren ziyaretçi istatistikleri, ya size hergün elektronik postayla gönderilir; ya da siz firmanın vereceği bir URL'e giderek, kendi istatistiklerinizi kendiniz ararsınız. Bu ikinci durumda muhtemelen size bir parola vereceklerdir.

Evsahibi firma ile anlaşma yaparken verilmesi gereken bütün bilgileri isteyin. Gerçi araştırmalarınız sonucu 24 saat teknik servis veren bir firma bulmuş olmalısınız; ama daha ilk günden sizi zora sokmalarına izin vermeyin.

## Site Yönetim ve HTML Yazma Programları

Bu noktadan sonra HTML veya ASP sayfalarınızın tek tek oluşturulması ve bir site bütünlüğüne kavuşturulması gerekir. Site edinmekte hangi yolu izlemiş olursanız olun, sitenizi oluşturmaya FrontPage ile başlamanızı şiddetle tavsiye ederiz. Piyasada yüzlerce HTML editörü ve site yönetim programı bulacaksınız. Bunların bazılarına ihtiyacınız olacak. Ama FrontPage, şu anda piyasada mevcut site oluşturma ve yönetim programlarının sadece en beceriklisi değil, aynı zamanda en kolayı. Ve tabiî, en yaygını ve adeta standart haline gelmiş olanı. Bununla birlikte FrontPage'de de sayfa yaparken olmasını arzu ettiğiniz bir çok imkan ve yeteneğin bulunmadığını göreceksiniz. HTML dilini öğrenmeye başladıkça, sık sık bir düz yazı programının size her türlü HTML editöründen daha kullanışlı geldiği anlar olacak. FrontPage ile yapacağınız sayfalara, başka firmaların programlarında multimedya ekleri yaptığınız günler gelecek. Fakat FrontPage, sadece sayfa tasarımında değil, fakat aynı zamanda yapacağınız sayfaların bir site olarak, evsahibi bilgisayara aktarılmasında, ileride sitenize ekler yaptıkça veya sayfalarda bazı unsurları değiştirdikçe yapabileceğiniz hataları özellikle bağlantı kopukluklarını belirlemenize yardımcı olacaktır.

FrontPage'i kullanmak zorunda değilsiniz; fakat kullanacağınız site yönetim ve HTML sayfa oluşturma programlarının, mutlaka FrontPage'de bulunan şu özelliklere sahip olmasına dikkat edin:

Gördüğünüz Gibi Sayfa Oluşturma: Masaüstü yayıncılık programları ile bilgisayar diline garip bir kısaltma daha girmişti. İngilizce Ne Görürsen Onu Alırsın (What You See Is What You Get) kelimelerinin kısaltılmışı olan WSIWIG (Vizivig, okunuyor) şimdi HTML sayfa yapma programlarının da bir özelliği. Sayfalarınızı, sanki bir kelime işlem programında, ya da masaüstü yayıncılık programında kağıda dökülmek üzere sayfa yapıyormuş gibi, yapıyorsunuz; program sayfanızı HTML kodlarını koyarak saklıyor. Bu programlarla HTML dilini öğrenmek zorunluğu asgariye iniyor. Dikkat edin, "Ortadan kalkıyor," demiyoruz. Çünkü eninde sonunda HTML kodlarına elle ince ayar yapacağınız bir an mutlaka gelecektir. En azından, kullanma izni verilen bir Javascript veya benzeri program parçacığını bir yerde beğenip, sayfanıza ithal etmek isteyeceksiniz. Ne kadar WSIWIG olsalar da HTML editörleri çoğunlukla ilave Script tarzı programları kendi kodlarına ithal etmekte fazla yardımcı olmuyorlar.

Kopuk Bağlantıları Bulma: Site yönetim programınızın, sayfalarınızın arasında veya bir sayfanın çeşitli unsurları arasındaki bağlantıların kopuk olup olmadığını belirlemesi gerekir.

Bütün Sitenizin Şeması: Kullanacağınız site yönetim programı, sitenizin bütün sayfalarını, küçük pullar halinde ve birbirlerine bağlantılarını çizgilerle gösterebilmelidir. Böylece hangi sayfanın nereye bağlandığını, bağlanmamış sayfa olup olmadığını ve özellikle sitede bir sayfaya değil de, tasarlandığı sıradaki gibi sabit diskte bir dizinde duran sayfalara bağlanmış sayfaları görebilirsiniz. Site kavramıyla değil de tek tek sayfalar hazırlamak üzere geliştirilmiş HTML editörleri, çoğunlukla bir sayfadan bir başka sayfaya veya unsuruna bağ yaptığınız zaman, HTML'in bu amaçla açtığı HREF koduna, sabit diskin ve dizinin adını yazar. Site yönetim programınızın, bu sayfaları Internet'teki yeni alanınıza yüklerken, bütün bağlantıları düzeltme kabiliyeti olması, işinizi büyük ölçüde kolaylaştırır.

Microsoft FrontPage, bunlara ek olarak, oluşturacağınız Internet sitesinde, Web Server olarak kullanılan programa bağımlı olmak şartıyla, ziyaretçilerinizle etkileşmenizi kolaylaştıracak başka özelliklere de sahiptir. Bunları da kısaca sıralayalım:

CGI programı yazmadan, Form'lara Action/Hareket kazandırmak: Form'larınıza koyacağınız "Gönder" veya benzeri komut düğmelerinin karşılığı, HTML'in FORM etiketinde ACTION komutunun karşısınaz yazacağınız bir program olacaktır. Bu programlara genellikle CGI programı denilir. Eskiden bütün Web Server'ların UNIX işletim sistemiyle çalıştığı zamanlarda, bu tür CGI programlarını yazmanın en kolay yolu Perl dilini öğrenmekti. Perl nisbeten kolay bir programlama dili olmakla birlikte, işi bilgisayar programı yazmak olmayan kişiler için CGI programı ciddî bir sorun olurdu. FrontPage, Web Server'da FrontPage Extensions adı verilen program yönetmeni yüklenmiş ise, site sahibinin hiç bir programlama dili öğrenmeden Form'larına hareket kazandırmasını mümkün kılıyor.

Tartışma ve Sohbet Grupları Açma: FrontPage ile Web sitenizde kolayca tartışma ve sohbet "odaları" açabilirsiniz ve ziyaretçileriniz bu sayfalarda birbirleri ile karşılıklı yazışabilirler. Yine eski UNIX sistemlerinde bunun için ek program satın almanız gerekiyordu.

Web Sitenizde Özel Alanlar Açma: Frontpage ile oluşturacağınız sayfaları istediğiniz ziyaretçiye açma, istediğinize kapatma imkanı vardır. Özel bir sayfaya girmek isteyen ziyaretçiye, FrontPage Extensions'ın yardımıyla parola sorabilirsiniz. Yine eski Server'larda bunun için özel Unix programları gerekiyordu.

Arama Kutuları Koyma: FrontPage sayesinde ziyaretçilerinize Web sitenizdeki bütün HTML belgelerinin içinde geçen bütün kelimeleri kullanarak arama yapma imkanı verebilirsiniz. "Arama motoru" da denen bu imkandan yararlanabilmek için ilave program üreten firmalara tek kuruş ödemek zorunda değilsiniz.

Ve tabiî, FrontPage'in Internet'ten kolayca indirebileceğiniz ücretsiz bir program olmadığını da hatırlatalım. Perakende satış fiyatı 80 Dolar'la 100 Dolar arasında değişen bu programı, NT Server işletim sistemi ile ücretsiz edinebilirsiniz. Programın sadece sayfa editörü olarak kullanılabilecek bir sürümü, Internet Explorer ile ücretsiz verilmektedir. Internet Explorer da çeşitli Internet alanlarından (örneğin, www.microsoft.com) ücretsiz edinilebilir.

## Sitenizin Etkinliği

Bir Web sitesi oluştururken, mimarîden basılmak üzere yayın hazırlamaya kadar hemen her tasarım projesinde karşı karşıya kalınan sorunla karşılaşacaksınız: Şekil mi, işlev mi?

Kimine göre, Internet bilgisayarı televizyona çevirdiği için bu kadar ilgi çekmektedir; dolayısıyla Web siteniz baştan sona bir televizyon programı gibi tasarlanmalıdır. Kimine göre, ziyaretçiler bu kadar masraf ve zahmet ederek bir Web sitesine ulaştıklarında, mutlaka yararlanacakları şeyi bulmalıdırlar.

Siz, mimarîde veya mobilyada hangi tarzı daha çok seversiniz? Şekle önem vereni mi, kullanışlılığa önem vereni mi? İnanın bu tercihiniz, yapacağınız sayfalara ve bu sayfaların tümünün oluşturacağı Web Sitesine de kişiliğini verecektir. Web sitesi, bir görsel ifade tarzıdır. Burada biz ne desek, siz yine kendi ifade tarzınızı kendiniz oluşturacaksınız.

Fakat… Unutmamak gereken tek şey, Web sitesinin oyuncak olmadığıdır. Sahibi için oyuncak niteliğinden ileri gitmeyen Web siteleri de vardır. Ama siz, bu kitapçığın en başında kendi kendizine sormanızı istediğimiz soruya verdiğiniz cevaba göre, nasıl bir Web sitesi oluşturmalısınız? Web sitesini sırf eğlenmek, bilgisayarla yeni bir oyun türüne kavuşmuş olmak için mi kuruyorsunuz? Yoksa belirli bir ticarî, fikrî, duygusal, vs., amaca mı hizmet edeceksiniz? Ya da, Web sitenizi kendiniz için mi kuruyorsunuz, başkaları için mi?

Cevabınız "Başkaları" ise, o zaman uygulamanız gereken bazı metamatik kurallar var. Bunların başında da sitenin etkin olması geliyor.

Ekonomi uzmanları, "Etkinlik, harcanan zamana göre elde edilen yararın oranıdır," derler. Bunu kendi Web sitenize uyguladığınızda şu sorulara cevap bulmak zorundasınız:

1. Bu sayfaya gelecek ziyaretçi aradığını kolay buluyor mu?

Bir Web sayfasında aranan unsurun kolay bulunması, herşeyden önce sayfanızın ziyaretçinin bilgisayarına çabuk aktarılmasını gerektirir. Oluşturduğunuz sayfaları kendi sabit diskinizde kolayca açıp kapatabilirsiniz. Sonuç itibariyle sayfalarınız browserınızla aynı sabit diskte duruyor! Ziyaretçinin browserı ile sayfalarınızın arasına binlerce kilometre mesafe ve sayısız router ile telefon teli ve uydu sinyali girdiği zaman, aynı hızı bulamayacaksınız.

Kolaylığın bir diğer ögesi ise sunuluşta içgüdüsel yaklaşımlara uygun bir tasarıma bağlı kalmaktır. Her konu, kendi içinde doğal bölümlere ayrılır. Mimar Sinan'ın hayatını ve eserlerini anlatan bir sayfa yaptığınız zaman, sitenizin "Hayatı" ve "Eserleri" diye ikiye bölünmesinden daha tabiî bir şey olamaz. "Hayat" bölümüne girebilecek bir unsuru "Eserler" bölümüne koyarsanız, bu unsura ziyaretçileriniz açısından kayıp gözüyle bakabilirsiniz. mimar Sinan'ın hayatını ile ilgilenenler bu unsuru göremeyecekler, eserlerine ilgi gösterenler ise ilgisiz buldukları bu unsura dikkat etmeden geçeceklerdir.

2. Sayfanızın temel karakterine uygun olmayan, "Olmasa da olur" diyebileceğiniz şeyler var mı?

Grafikler, zemin fotoğrafları, ses, anime grafikler ve video klipleri çoğu zaman hiç bir sayfada olmasa kimsenin "neden yok" diyeyeceği şeyler değildir. Mimar Sinan'ın eserlerini fotoğraf ve grafik olmadan anlatabilmek, hemen hemen imkansız olsa gerek; ama sırf başkaları yapıyor diye, sayfanıza açılırken çalmak üzere Mimar Sinan devri Klasik Türk Müziği'nden güzel bir örnek koymanın sayfanızın Internet'e 16 etapta bağlanan bir ISS'in abonesi ziyaretçiye vereceği sıkıntı, belki de sayfanızın tümünün görülmesini önleyecektir. Çağımızda, hiç kimsenin 10-15 saniyeden fazla kum saati seyretmeye tahammülü olmadığını bilmek zorundasınız.

3. HTML'in kurallarına tümüyle riayet ettiniz mi?

Etkin olmasını sağlamaya çalıştığınız sayfalar, kolay gibi görünen, ama bütün bilgisayar dilleri gibi incelikleri ve kuralları olan bir dille yazılıyor. HTML, diğer bir çok bilgisayar programlama dilinden farklı olarak, hata halinde de çalışabilen bir dildir. HTML'in birinci satırında hata yaparsanız, o satırdaki komutlar icra edilmez, ama ikinci satırdakiler edilir. HTML'i yorumlayan browser, hatalı birinci satırı atladığı için o satırın gereğinin yerine getirilmemesi, sayfanızın geri kalan bölümünün ziyaretçinin ekranında tümüyle amacınıza aykırı canlandırılmasına neden olabilir.

HTML'in her kuralı belirli bir amaç için vardır; bu kuralları keyfî olarak çiğneyemezsiniz. Örneğin, bir sayfanın browser tarafından Türkçe karakterlerle canladırılması için baş tarafındaki <HEAD>..</HEAD> etiketi içinde sayfa kodlama sistemiyle ilgili bir META TAG bulunması gerekir. Bir büyük yayın organının Internet sayfalarında bu etiket bulunduğu halde sayfalarındaki Türkçe altı karakter (İ, ı, ğ, Ğ, Ş ve Ş), Almanya, Fransa, İngiltere ve ABD'de, ülkenin varsa standart ASCII dizisi dışındaki harflerine veya High ASCII karakterler dediğimiz karakterlere çevrilerek gösteriliyor. Neden? Dikkat ettiyseniz, META TAG'in <HEAD>..</HEAD> etiketi içinde olması gerektiğini söyledik. Bu yayın organının sayfalarında <HEAD>..</HEAD> etiketi bulunmuyor. Sayfayı tasarlayan "Bu etiket olmasa da olur," diye düşünmüş olmalı. Bu tasarımca, kendi sayfalarını, Türkiye'de Türkçe sistemle çalışan bir bilgisayarda sınadığı için, bu basit ve görünüşte hiç bir yayarı olmayan etiketi atıp, iki satır az kod yazmaktan kurtulduğuna seviniyor olmalı!

Özetlersek, sayfalarınızın amacına uygun ve etkili olabilmesi için kolay ve çabuk yüklenen, amaç dışı unsurlarla içgüdüsel arayıp bulma davranışını bozmayan ve HTML'in tüm kurallarına harfi harfine riayet eden sayfalar olması gerekiyor.

## Hayatınızın Gerçeği: İki Browser

Üzülerek belirtmeliyiz ki, sayfalarınız zilyaretçilerinizin ekranlarında hiç bir zaman sizin ekranınızda göründüğü gibi görünmeyecektir. Bunun birinci nedeni, ziyaretçileriniz Internet Explorer kullananlar, Netscape Navigator kullananlar ve Diğerleri olmak üzere üçe ayrılacaktır. HTML, Internet'in ortak dili olmakla birlikte, browserların yorumuna bağlı bir dildir. Bunun sonucu olarak bazı site sahipleri, sayfalarının başına kullanıcının browser'nın türünü ve sürümünü araştıran programlar koyarlar ve buna göre ziyaretçilerine farklı sayfa gönderirler.

Bu, her sayfanın iki ayrı türünü yapacak zaman ve paranız varsa, takip edilebilecek, ama kesinlikle gereksiz bir yoldur. her iki browser'ın birbirinden ciddî olarak ayrıldığı noktalar özellikle Dinamik HTML dediğimiz, sayfaları duraganlıktan kurtaran özellikler kazandıran tasarım komutlarıdır. DHTML unsurları, zaten bir sayfanın ziyaretçiye gönderilme süresini uzatan unsurlardır. Amacınız ektili bir iletişim ise, bu süreyi mümkün olduğu kadar kısaltmak başlıca amacınız olmalı. Sayfalarınızı her iki browser'ın ortak yorum özelliklerine göre tasarlamanız, yani mümkün olduğu kadar DHTML ögelerinden kaçınmanız, iki türlü sayfa tasarlamanıza ve gerçekleştirmenize lüzum bırakmaz.

Bunu demiş olmakla birlikte, DHTML'in ne kadar yaygın kullanıldığını da görmemezden gelemeyiz. DHTML ile sayfalarınız hareket ve ziyaretçinin tercihlerine göre içerik kazanabilir. Bu ise etkinliği arttıran bir araç olarak kullanılabilir. COOKIE denilen, sizin sitenizden ziyaretçinin bilgisayarına gönderilen küçük bilgi dosyacıkları, ziyaretçinin örneğin sizin sitenize ilk geldiğinde nelerle ilgilendiğini, hangi sayfalara gittiğini, ne gibi araştırmalar yaptığını içeren bilgileri, ikinci seferinde size ulaştırabilir. Bu kez bu ziyaretçiye sunacağınız sayfada, sadece onun ilgi alanına giren unsurlara yer verebilirsiniz. Bu dinamizmi klasik HTML ile sağlayamazsınız. DHTML, JavaScript, VBSCript gibi dillerle yazılmış programcıklarla, sayfalarınızı vermek istediğiniz ana mesajı daha kolay, daha etkili vermenizi sağlayabilir.

Bunu yaparken sadece bir browser'ın yorum özelliklerine bağlı kalırsanız, bir Javascript programının sadece IE'da tam icra edilmesine dikkat eder, Netscape kullananlar hakkında "Ne görürse görsün!" diye düşünürseniz, siteniz ticarî amaçlı ise muhtemel müşterilerinizin yüzde 50 ile 60'ını elden kaçıracaksınız demektir. Evet, Netscape halâ IE'ın bütün becerilerine sahip değil; ama ne var ki Internet'den yararlanan kişilerin büyük bir bölümü Netscape kullanıyor.

Ayrıca Netscape'in beceri alanına girse bile, IE'ın yorumlayabildiği bazı JavaScript programları, dinamik STYLE kağıtları, DIV ve SPAN etiketleri ile yapabileceğiniz bir dizi "Web oyunu," IE'ın ve Netscape eski sürümleri ve halâ kullanılan diğer browser programlar tarafından anlaşılamaz. Bu tür programları kullanan ziyaretçilerinizi düşünerek, sayfalarınızın en azından vermek istediğiniz mesajı aşağı yukarı veren bir "Sadece metin" sürümünü de yapmanızda yarar var.

Sayfalarınız bittiğinde, Internet'e koymadan önce, çeşitli bilgisayarlarla, çeşitli browser'larla sınayın. Farklı ortamlarda, nasıl durduğuna bakın. Ve en önemlisi, Internet'e koyduğunuz anda, Internet'e 28.8 K modemle bağlı bir bilgisayardan sayfalarınızın nasıl geldiğini inceleyin. Saat tutun!

Sayfanızı 15, 17 ve 21 inç ekranlarda, VGA ve SVGA grafik kartlarında, ve 640X480, 800X600 ve 1024x768 çözünürlükte inceleyin. Bununla, sayfalarınızı en az üç, en fazla altı ayrı bilgisayarda incelemeniz gerektiğini söylemiş oluyoruz. Web tasarımcıları, genellikle en gelişmiş, bol hafızalı grafik kartları bulunan, büyük ekranlı bilgisayarlarla çalışırlar. Sabahtan akşama bilgisayar ekranı karşısında çalışmak için aslında böyle bir sistem şarttır. Fakat ziyaretçilerinizin çoğu, genellikle 15 inç ve halâ bir VGA grafik kartına bağlı, 640X480 çözünürlükte bir ekran sahibi olacaktır. Sizin özene bezene oluşturduğunuz sayfalarınız, böyle bir ekranda hiç de arzu ettiğiniz görsel etkiyi yapmayabilir.

Etkinlik ve kolaylık ilkesi, birinci sayfanızda hiç bir zaman yukarı-aşağı ve sağ-sol kaydırma çubukları olmadan canlandırılmasını gerektirir. İç veya sonraki sayfalarda yukarı-aşağı kaydırma çubuğu olabilir, ama asla sağdan sola kaydırma çubuğuna basmaya gerek bırakmamalısınız. Kağıda basılmak üzere hazırladığınız sayfalarda grafiklerin ortadan bölünmeden basılacağı bir yere denk gelmesine dikkat edin.

## FrontPage ile Web Sitesi İnşaatı

FrontPage (FP) ile Web sitesi oluşturmak için şu altı adımı atacaksınız:

1. FrontPage'i kurun:

<webFP01.tif>

FrontPage programını bilgisayarınıza kurmak çok kolay bir işlem. Ayrıca program kutusundan çıkan kullanma kılavuzu, İngilizce bilenler için yeterli bir kaynak. Ayrıca bir çok yazarın FrontPage'in inceliklerini anlatan kitabı da var. FrontPege'i kullanabilmek için bilgisayarınızın Windows 95, 98 veya NT ile çalışıyor olması gerek.

2. Frontpage'de sitenizi oluşturun:

<webFP02.tif>

Program açılırken, sizden sabit diskinizde bir Web alanı oluşturmanızı isteyecektir. Bilgisayarı başkalarının da kullanabileceğini düşünerek, kişisel Web alanınızın sabit diskteki bu kopyasını isterseniz parola ile gizleyebilirsiniz. FrontPage'in Kişisel Web Alanı dediği, aslında sabit diskinizde açılacak bir dizinden ibarettir.

3. Ana sayfanızı ve bağlı sayfalarınızı oluşturun.

<webFP03.tif>

Sayfalarınızı oluşturabilmek için önce bir site planlaması yapmanız ve hangi sayfanın hangi sayfaya gideceğini planlamanız gerekir. Bunu aşağıda ele alacağız. FrontPage tek tek sayfaları oluşturmak için size sayısız hazır örnek sayfadan veya tamamen boş bir ekrandan hareket etme imkanı veriyor. Ayrıca FP'in sabit diskindeki binlerce grafik unsurdan yararlanabilirsiniz. Kullanılmaya hazır düğmeler, çizgiler, bağlantı simgeleri, animasyon grafikleri, istediğiniz gibi kullanabilirsiniz; veya Microsoft'un Tema (Theme) adını verdiği tarzda, sayfalarınız arasında görsel birlik sağlayacak tarzda, hazır örneklerden hareket edebilirsiniz.

4. Sitenizi Internet'e Aktarın.

<webFP04.tif>

Bu yapabilmek için, daha önce ele aldığımız gibi, FP Weblerine ev sahipliği yapabilen bir Server'da yer kiralamış ve kendinize bir URL almış olmalısınız. Evsahibi firma, FrontPage'in adını duyunca, programın sizden isteyeceği bilgilerin tümünü verecektir. FP'in dilinde sitenizi Internet'e aktarmanın adı "Yayınlamak"tır. Menü çubuğundaa Publish (Yayınla) düğmesine bastığınızda karşınıza gelecek bir dizi ekranda, evsahibinin vereceği bilgileri gireceğiniz kutular olduğunu göreceksiniz. Bundan sonrası tamamen kendiliğinden devam edecek ve Web siteniz Internet'te yerini alacaktır.

Burada ikinci adımda belirtilen işler, sitenizi inşa ederken en çok zaman harcayacağınız adım olacaktır. Bu adımı ikiye ayırarak, biraz yakından inceleyelim

### İçeriği Derleme

Sayfalarınızı yapmaya başlamadan önce şu bilgilerin kağıtta, sabit diskte veya diskette elinimizin altında olmasını sağlayın:

Ürünler ve hizmetleriniz hakkında ayrıntılı bilgi

Müşteri hizmetleri bilgileri, broşürler, el kitapları, kılavuzlar

Firmanızın, derneğinizin veya dairenizin yayınladığı bütün bültenler, dergiler, eleman arama ilanları, basın bültenleri.

Daha önce yapılmış Web sayfaları

Kurum veya kuruluşunuzun emir-komuta zinciri sırasına göre yukarıdan aşağı yetkililerinin adları, sıfatları, adresleri, telefon numaraları

Kurum veya kuruluşunuzun yıllık faaliyet ve malî raporları

Personel listesi

Müşteri listesi

Kurum veya kuruluşunuzun faaliyet takvimi

Bu bilgileri belki sitenizde kullanmayacaksınız. Ama bu bilgileri önceden derlerseniz, sitenizde kullanmanız gerektiğinde sayfa tasarım işine ara verip, malzeme peşinde koşmaktan kurtulmuş olursunuz.

Bu arada sayfalarınızda kullanmanız gereken resimler, fotoğraflar, grafikler hazır mı? Hiç bir işe başlamadan, sayfalara girmesine karar verdiğiniz her türlü malzemeyi bir kenara yığın ve bunlarla aşina olmaya çalışın. Hangi rapordan hangi fotoğrafı veya grafiği alacağınızı belirleyin.

Kağıt üzerindeki malzemenin bilgisayar ortamına aktarılması için gerekli tarayıcı (scanner), elektronik kamera, vs., gibi cihazların hazır olmasına, çeşitli bilgisayarlar arasında disketle aktarılamayacak büyüklükte malzemenin alınıp verilmesi için gerekli ağ bağlantıları veya ortak tanışabilir medya (Zip disk veya benzeri büyük disketler) bulunmasını sağlayın.

Web sayfalarına girecek metin ve başlıklarla düğmelerle seyir (Navigasyon) grafiklerindeki kelimelere kadar bütün yazıların ve başlıkların hem doğru hem de ortak bir dili olması gerekir. Metinlerin çeşitli kaynaklardan denetimi, dikkatli editörler tarafından yapılabilir. Ortak ifadeyi ise ya tek kişi, ya da birbirini çok iyi anlayan bir editörler grubu sağlayabilir. Bu nedenle Web sitesinin en az bir editörü olmalıdır. Web sitesinin herşeyi bir kişi, ve o kişi de siz iseniz, yazar sıfatınızla düzeltmen sıfatınızı birbirinden ayrı kullanmaya çalışmalısınız. Bir kişinin kendi hatasını yakalaması hiç de sanıldığı kadar kolay değildir. Bu nedenle yayın kurumlarının eskiden beri uyguladığı ilkeyi uygulayarak, yazdıklarınızın "ikinci bir çift göz tarafından görülmesini" sağlayın. Bu mümkün değilse, yazdığınız bir şeyi bitirdikten en az 24 saat sonra yeniden okuyun.

Eğer içerik derleme ve denetimini bir kurul yapacaksa, şu hususlara dikkat edin:

Eskimiş bilgileri kim ayıklayacak?

Yeni bilgiler kimden gelecek; kimde toplanacak? Bunları sayfalara yerleştirme konusunda kim karar verecek?

Örgüt içinde farklı gruplardan gelecek malzeme kimde toplanacak?

Değişiklikleri ve güncelleştirmelerden kim sorumlu olacak?

Site Internet'e açıldıktan sonra gelecek talep ve eleştiriler kimde toplanacak?

Dil ve imlâ hatalarını yakalamaktan ve düzeltmekten kim sorumlu olacak?

Web sitesi, bir anlamda grafik demektir. burada kastettiğimiz istatistik bilgilerinin belirli şekilsel sunuluş tarzı olan istatistik grafikleri değil. Her türlü resim, çizgi, fotoğraf, ve bunların belirli bir alanda sunuluşu grafik öge sayılır. Grafik unsurlar, her bir sayfanın kişiliğini belirlemekle kalmazlar, her sayfada tekrar ederek siteye bütünlük kazandırırlar. Bu nedenle tıpkı yazılardaki dil birliği gibi, grafik unsurlarda da görsel birlik sağlanmalıdır. Görsel birlik, düğmelerin biçim ve renginden tutun, üzerine yazılacak başlıklarda kullanılacak harfin türüne, şekline ve büyüklüğüne kadar aynı olmalarını gerektirir. Ayrıca sayfalarınızda fotoğraf ve çizgi resimler kullanacaksanız, hepsinin aynı tarz olması gerekir. Grafik unsurlarla ilgili teknik kurallar, bu kitapçığın kapsamını aşıyor. Grafik, grafikçilerin işidir. Bir çok grafik programı, bilgisayarda grafik unsur yapmayı olağanüstü kolaylaştırmış bulunuyor. Bu, kolayca yapılan her grafiğin "grafik" olduğu anlamına gelmiyor. Tıpkı yan yana ve alt alta dizilen bir çok kelimenin bir şiir oluşturmadığı gibi. Özellikle ticaret amacıyla oluşturacağınız Web sitesinde mutlaka bir grafik sanatçısının yardımını istemelisiniz.

Aslına bakarsanız, HTML dilini kullanarak yapacağınız bir ekran dolusu sayfa, yazıları, resimleri, çizlegileri ile, kendisi bir grafik unsur olacaktır. Bu nedenle en azından kağıt üzerinde basılmak amacıyla sayfa hazırlama deneyiminiz yoksa, mutlaka FrontPage'in hazır şablon sayfalarını kullanmalısınız.

### İçeriği Sayfalara Geçirme

İnternet sitenizde yer alacak unsurları belirledikten sonra sıra bunları bir veya daha çok sayfa halinde "siteleştirmeye" geliyor. Bir site, biraraya doldurulmuş ve aralarında kavramsal bir birlik olmayan sayfalar demeti demek değildir. Bir sitenin birinci sayfasından (Index Page) son sayfasına kadar her bir sayfasının ve her sayfadaki her bir ögenin bir anlamı, sitenin varlık sebebine bir katkısı olması gerekir.

Tıpkı Gütenberg'den bu yana basılı eserlerin, kitapların, dergilerin gazetelerin, broşürlerin okuyucu olarak bizlere kazandırdığı "anlam verme davranışı" gibi, son on yıldır tasarlanan Web sayfaları da Web ziyaretçilerinde belirli bir "anlamlandırma dili" meydana getirmiş bulunuyor.

Bunu biraz açalım. Bir gazetenin birinci sayfasında, az sayıda kelime ile fakat oldukça büyük harflerle bir başlık görürseniz, başlığın kelimelerini bile okumadan bu haberin önemli olduğunu anlarsınız. Bir dergide oldukça süslü bir harf türüyle ve renkli bir zemin üstünde, yanında tanınmış bir sinema sanatçısının fotoğrafı bulunan bir başlık görürseniz, o haberin acil önemde olmadığını bilirsiniz. Bu anlama ve bilme durumu sağlayan, sizin okuyucu olarak bugüne kadar edindiğiniz tercübelerden çıkan "anlamlandırma davranışı"dır. Her davranış gibi "anlam verme" de zamanla ve deneyimle öğrenilir. Şimdi, bugüne kadar yapılmış bütün Web sayfalarını bir yere toplarsanız, her on sayfadan 7'sinde site içinde değişik yerlere gitmekte sullanılan seyir (Navigation) düğmeleri ve metinlerinin ekranın sol tarafına dizildiğini göreceksiniz. Diğer sayfalardan ikisinde seyir unsurları sayfanın altında sadece birinde sağında olacaktır. Bu, Internet abonelerine, Web sayfalarında belirli bir deneyim, alışkanlık ve beklenti oluşturmuş bulunuyor. Elbette bu "kuralı" kırmak elinizde. Ama oluşturacağınız "kural dışı" sayfa, ziyaretçilerinizde alışmadıkları bir durumla karşı karşıya oldukları hissine yol açar. Bu, dikkatli kullanılırsa, sürüden ayrılarak dikkat çekme şeklinde, olumlu bir unsur da olabilir. Ne var ki, kural dışı uygulamalara başvurabilmek için önce kuralları ustaca uygulama becerisi edinmek şarttır.

FrontPage'in şablon sayfaları arasında çok "kuralcı" olanları kadar, kurallara iyice aykırı görünler de var. Program kurulurken, bu şablonlarla yapılmış örnek sayfalar da sabit diskinize koypa edilecektir. Bunları dikkatle inceleyip, işinize uygun bir şablonu seçebilirsiniz.

FP'i ilk açtığınızda karşınıza FP Explorer adı verilen Site Yönetim programı gelecektir. Bu programda Personal Web (Kişisel Web) görünümünde (View/Navigation) menüdeki New Page (Yeni Saya) simgesini her tıkladığınızda sitenizin tümünün görünümünü veren ortadaki alanda bir sayfa simgesi oluşacaktır. Bu simgenin üzerini farenin sağ düğmesi ile tıklayarak açılacak menüden Remane (Yeniden Adlandır) maddesini seçerek, sayfalarınıza istediğiniz adı verebilirsiniz.

İyi bir site planlaması kağıt üzerinde yapılmalıdır. Sonra bu planı FP Navigation ekranında oluşturabilirsiniz. Tipik olarak sitenizin bir açılış sayfası (buna genel olarak Home Page veya Splash Page deniliyor) ve bu sayfanın içinde yer alacak seyir düğmelerine veya kelimelerine tıklayarak gideceğiniz içerik sayfaları olmalıdır.

Burada, basit bir örnek site oluşumunu görüyorsunuz:

<website1.tif>

Bu noktada sitenizdeki bütün sayfalar için ortak bir ana tema seçebilirsiniz. FP size 100'e yakın tema veriyor. Tema seçimini FP Explorer'ın soldaki memü simgeleri arasında bulunan Themes (Temalar) simgesini tıklayarak yapabilirsiniz. İşte Küresel Pazarlama (Global Marketing) adı verilen tema:

<website2.tif>

Home Pege olarak adlandırılan sayfayı iki kez tıkladığımızda, FP'in HTML editörü çalışacak ve içi boş olan bu sayfayı, seçtiğimiz temaya göre işlenmeye ve içi doldurulmaya hazır olarak karşımıza getirecektir.

< website3.tif>

Burada dikkat ederseniz, site planında ana sayfaya bağladığımız Yeni Sayfa 1 ve Yeni Sayfa 1 adlı iki sayfa, bağlantısı kurulmuş (link) olarak, ekranın sol tarafında seyir satırları olarak hazır bulunmaktadır. Bu sayfaların adını Navigation ekranında değiştirecek olursak, FP bu sayfalara yapılan bütün atıfları (linkleri) düzeltecektir.

Bu kitapçıkta HTML ile sayfa oluşturma konusuna girmiyoruz. HTML ile sayfa oluşturma konusunda temel bilgileri edinmek için, Byte Eğitim Dizisi'nin 15'nci kitabı olan HTML Rehberi'ne başvurmanız gerekir.

Sayfalarınızın tümünü inşa ettikten, içeriklerini yerleştirdikten, bağlantılarını kurduktan sonra, FP Explorer'a bu sayfaları ve içlerindeki bütün unsurları Wes sitenize evsahipliği yapacak firmanın Web Server'ına göndermeniz, veya FP'nin diliyle "Yayınlamanız" (Publish) gerekir. Web evsahibinizin Server'ı FrontPage-uyumlu ise FP bunu mevcut Internet bağlantınızı kullanarak yapacaktır.

### Web Sitenizin Yönetimi

Site yönetimi, bir siteyi oluşturmak kadar önem taşıyor. Sitenizi FP uyumlu bir Server'da oluşturuysanız, evinizde veya işyerinizdeki bilgisayardan evsahibinin Server'ındaki sitenizi kolayca yönetebilirsiniz. Site yönetimi ile kastedilen işler arasında, Açma İzni, Sayfa Değiştirme ve Güncelleştirme ve İdare Yetkileri bulunur.

Yapacağınız Web sayfalarının otomatik olarak herkes tarafından görülme, yani Browser programı ile açılabilme izni vardır. Fakat tamamen özel bir Web sitesi yapıyorsanız, sitenizi sadece belirli kişilere veya belirli bir parolayı verecek kişilere açabilirsiniz.

Sitenizdeki sayfaların inşası, güncelleştirilmesi ve FP HTML Editörünü kullanarak değiştirilmesi yetkisini, ancak Authoring yetkisi olan kullanıcılar kullanabilir. Siteyi oluşturan kişi, FP tarafından Yönetimi (Administrator) olarak bilinir ve program kurulurken yöneticiden bir kendisine bir parola seçmesi istenir. Bu parola verilmedikçe FP bilgisayarda oluşturulacak Kişisel Web'i açmayacaktır. Yeni bir Web alanı oluşturmak isterseniz, FP kim olursanız olun sizden bir parola seçmenizi ister ve yapacağınız Web sitesi bu parola verilmedikçe yeniden açılamaz. Bir Web sitesini oluşturan kişi, FP'nin deyimiyle sitenin yöneticisi, sitede ve sayfalarında değişiklik yapma yetkisine sahiptir ve bu yetkiyi istediği isme verebilir. Yönetici herhangi bir FP Web sitesi için yetki vereceği kişilere bir de parola seçmek zorundadır.

Bir FP Web sitesinde yetki dağıtma yetkisi de sitenin yöneticisine aittir. Yönetici bu yetkiyi de tıpkı Authoring yetkisi gibi istediği isimlerle, parola vererek, paylaşabilir. Yönetici, isterse kendi yetkilerini de değiştirebilir. (Yetki verme veya Authoring yetkisini başka bir kişiye devretmeden yöneticinin kendi kendisinin yetkisini yok etmesi halinde Web sitesi açılamaz hale gelebilir!)

Bir sitede oluşturulacak dizinlere kimin erişebileceği ve içindeki kimin görebileceğine ilişkin yetkiler ise FP'den değil Web Server'dan yapılabilir.

### FrontPage'in Özel Unsurları (Components)

FP'i diğer Web yönetim programlarından ayıran önemli özelliklerinden biri Component adı verilen bazı unsurlarla, sayfalarınıza ve sitenize ziyaretçilerle etkileşme, güvenlik ve kullanım kolaylığı sağlamasıdır. Component'lar genellikle dinamik nesnelerdir; Web sayfanızın durumuna veya kullanıcının bir hareketine bağlı olarak bir şeyler yaparlar.

Component'lar, FP'in HTML editöründe Insert (Ekle) menüsünden Insert FrontPage Components maddesi (FrontPage Unsuru ekle) seçilerek girilir. Bazı Component'lar ise yine Insert menüsünden Active Elements seçilerek girilebilir. Bu unsurları kısaca tanıtıtalım:

"İçindekiler Tablosu" unsuru, içinde yer aldığı HTML sayfasında bir Web sitesindeki bütün sayfaların bağlantısı ile birlikte bir listesini oluşturur. Ziyaretçileriniz bu listede istedikleri satırı tıklayarak arzu ettikleri sayfaya ulaşırlar.

Arama Formları: Sitenize koyacağınız ve içinde metin arama kutusu, arama düğmesi veya kutuyu temizleyerek yeniden başlama imkanı veren Sil düğmesi bulunan bir formla, verilecek kelime veya kelimelerin sitenizdeki bütün sayfalarda aranmasını sağlayabilirsiniz. Sonuçlar, metnin geçtiği sayfaların adları ve bağlantıları ile gösterilecektir.

Sayfa ve Grafik Ekleme Unsurları (Include Component): Diyelim ki bazı sayfalara belirli bir konuda bir metin koyacaksınız. Ancak bu metin, zaman zaman değişecek. Bu metnin yer aldığı 10, 15 sayfayı tek tek her seferinde düzeltmek yerine, bu bilgiyi bir HTML sayfasına koyabilirsiniz; sonra bu sayfayı, sözkonusu metnin görülmesi gereken heryere eklersiniz. Ekleme sayfanın içeriği değiştiği zaman eklendiği heryerdeki bilgi de değiştirilmiş olacaktır. Bunu metinle değil de grafikle de yapabilirsiniz.

Zaman damgaları (Timestamps): Bir sayfaya konulan "zaman damgası", sayfanın en son değiştirildiği tarih ve saati metin olarak gösterir. Siz sayfanıza sadece zaman damgası unsuru koyarsınız; ancak bu damga ziyaretçinin ekranında, tarih ve saati belirten metin olarak gösterilir.

Yer tutma unsurları: Bir HTML sayfasının ilk tasarımını yapan ve daha sonra sayfayı değiştiren kişilerin adı ve soyadı ile sayfanın tanımının yerini tutacak bu unsurlar sayfa sabit diske kaydedildiğinde, yerini tuttukları unsurun içeriğini kendi yerlerine yazarlar. Böylece bir sayfanın kimin tarafından tasarlandığı, kimin tarafından değiştirildiği ve tanımı herseferinde hatırlanarak değiştirilmek külfeti ortadan kalkmış olur.

### FrontPage'in Form Unsurları

FP, ziyaretçilerin Web siteleri ile etkileşmesini sağlamada CGI programlama zorunluğunu da ortadan kaldırır. Formları şu maksaklarla kullanabilirsiniz:

Ziyaretçilerden, isim, adres, telefon numarası, elektronik adres, görüş ve düşüncelerini derlemek için yararlanabilirsiniz.

Ziyaretçilerin, siteniz veya sitenizi tahsis ettiğiniz konular hakkında görüşlerini, düşüncelerini ve tepkilerini derleyebilirsiniz.

Sitenizde tanıtımını yaptığınız mal ve hizmetlerin satışını yapmak üzere, kredi kartı numarası ve teslim adresi gibi bilgileri alabilirsiniz.

Belirli bir konuda ziyaretçileriniz arasında tartışma açabilir, herkesin görüş ve düşüncesini belirtmesine, veya başkalarının görüş ve düşüncelerine tepkisini göstermesine imkan sağlayabilirsiniz.

Form oluşturmanın HTML bölümüne girmeden, FP'in formla elde edilecek bilgileri işlemesine imkan veren komutlar ve unsurlarından söz edelim. FP, oluşturacağınız forma otomatik olarak Form Handlers adını verdiği, formla elde edilecek bilgilerin işlenmesinde kullanılacak unsurlar ekler. Bu unsurlar, ya FrontPage Server Extensions adı verilen, kullanılması son derece kolay ve Sadece Microsoft'un değil fakat başka firmaların, hatta Unix ortamında çalışan bazı Web Server'ların da kullanabildiği mini-programlar sayesinde hizmete sokulabilir. FP bir formla elde edilecek bilgiyi ya Server'daki Web alanında, ya da sabit diskte ayrılacak bir dizinde belirlenecek bir yazı dosyasına ekleyebilir. FP ayrıca bu bilgileri verilecek bir elektronik posta adresine gönderebilir.

FP, arzu ederseniz, Form Handler'ları, ISAPI (Internet Server Application Program Interface), NSAPI (Netscape Server Application Program Interface), CGI (Common Gateway Interface) veya ASP (Active Server Page) uyumlu bir şekilde de oluşturabilir. Bu arayüzlere uygun oluşturulacak Handler'ların kullanılabilmesi için Web Server'de bu arayüzlerle çalışan programların kurulmuş olması gerekir.

FP'nin sitenizi sadece kayıtlı kullanıcıların ziyaret etmesine imkan veren Kayıt (Registration) formu ile tartışma grupları oluşturmaya yarayan Discussion Groups sihirbazı, özel bir çaba gerektirmeden, kolayca uygulanabilecek formlardır. Bu formların kullanılması için Microsoft'un Internet sitesinde (www.microsoft.com/frontpage) geniş bilgi bulabilirsiniz.

## Tavsiyeler

Bir Web sayfası tasarımcısının en büyük yardımcısı, diğer Web siteleridir. Web sitelerinin iyi, güzel, zevkli, çabuk açılan, içinde hareket etmesi kolay olanlarından örnek almak gerekir. Buna karşılık kötü, çirkin, zevksiz, yavaş açılan ve en önemlisi ziyaretçi olarak sizi sinirlendiren sayfalardan ders almak gerekir.

HTML tasarımı üzerine okuyacağınız ciltler dolusu kitaptan daha fazla yararı şu tavsiyeyi tutarak elde edebilirsiniz:

Internet'te "En İyi" sayfaları bir araya getiren şu sayfadaki bağlantıları izleyin ve ulaşacağınız sayfalardan hoşunuza gidenlerin ekran görüntüsünü yakalayın:

<webbest.tif>

http://dir.yahoo.com/Computers\_and\_Internet/Internet/World\_Wide\_Web/Best\_of\_the\_Web/

Internet'te "En Kötü" sayfaları bir araya getiren şu sayfadaki bağlantıları izleyin ve ulaşacağınız sayfalardan en itici ve çirkin bulduklarınızın ekran görüntüsünü yakalayın:

< webnotbs.tif>

http://dir.yahoo.com/Computers\_and\_Internet/Internet/World\_Wide\_Web/Best\_of\_the\_Web/Not\_Really\_the\_Best/

//////////////////KUTU////////////

Ekran Görüntüsü Yakalamak

Browser programında, veya başka bir programın penceresi içindeki görüntüyü, grafik olarak yakalamak ve sabit diskinize kaydetmekle, ekranın o andaki fotoğrafını çekmiş olursunuz. Bunun için piyasada çeşitli programlar satılıyor. Ancak Windows ortamında bunu başka programa ihtiyaç duymadan yapabilirsiniz. Bütün ekranın görüntüsünü yakalamak için klavyenizdeki Print Screen tuşuna bir kere basın. Sadece o anda odak noktası olan, en önde veya fare simgesini içine tıklamış bulunduğunuz tek pencerenin görüntüsünü elde etmek için önce ALT tuşunu tutun ve bırakmayın, sonra Print Screen tuşuna basın. Sonra herhangi bir grafik programını, örneğin Windows'un Paint programını açın Edit menüsünden Yapıştır/Paste maddesini seçin. Yakaladığınız ekran görüntüsünü şimdi BMP biçiminde grafik doysayı olarak sabit diskinize kaydedebilirsiniz.

<websccap.tif Resimaltı: İşte bir MS Word ekranının görüntüsü Paint programında.>

//////////////////////////////////////////

İyi tasarım, iyi saç traşı gibidir: Göze görünmez. Ya da iyi tasarım iyi radyo spikeri gibidir; konuşanı değil, haberi dinlersiniz. İyi tasarlanmış bir sayfada, dikkatiniz tasarımın kendisine değil, içeriğe döner. Ve iyi bir tasarımın yerini hiç bir şey tutamaz. "Sayfam kötü de tasarlanmış olsa, önemli değil; nasıl olsa içeriği önemli!" diyen bir site sahibi, kendisini başarısızlığa mahkum eder.

Bir Web sayfası, sayfayı oluşturulan sanatçı ve teknik ekibin üzerinde çalıştığı bilgisayarın ve özellikle ekranının imkanları değil, ortalama bir bilgisayar sahibinin edinebileceği bilgisayarın imkanları ve yetenekleri gözönüne alınarak yapılmalıdır. Sayfalar baştan aşağı grafikle dolu olur ve grafikler renk ve diğer unsurlar açısından büyük bilgisayar dosyaları oluşturursa, bu sayfaların yavaş bir bağlantıya sahip bilgisayara aktarılması da yavaş olur. Bu nedenle Web sayfaları, 14 inç VGA ekran standartı dikkate alınarak, 72 DPI çözünürlükte, Windows sisteminin temel 16 rengi kullanılarak yapılmalıdır.

### Index.html

Web sitenizi yaptığınızda, mutlaka ana sayfanızı Index.html olarak adlandırın. FP bunu sizin için otomatik olarak yapacaktır ve bunun bir sebebi var. Bir bilgisayar kullanıcı Browser'ının adres kutusuna bir sitenin adresini yazar ve bu site içinde belirli bir sayfanın adını vermezse, (örneğin, sadece www.alinin\_sitesi.com.tr yazarsa) Web Server hangi sayfayı gönderir? Bir çok Web Server için varsayılan sayfa Index.html'dir. Bazı Server'lar varsayılan sayfanın Default.html olarak adlandırılmasını isterler. Eski sürüm Server'lar arasında sayfa adı vermeyen ziyaretçiye web sitesinin kök dizini (root directory) içinde yer alan dosya adlarını gösteren bir liste sunanlar veya ziyaretçiye hata mesajı verenler de vardır. Web evsahibinize, Server'ının varsayılan sayfa olarak hangi adı vermeniz gerektiğini sorun ve ana sayfanıza daima bu adı verin.

### Davranış Kuralları

Özellikle ticaret amaçlı Internet sayfasının muhtemel müşteri olan kişinin bilgisayarına yavaş aktarılması, kişinin ilgisinin dağılmasına ve bizim muhtemelen bir satış imkanını kaçırmamıza neden olur. Web sayfası tasarım programlarının çoğu zaman bir sayfanın Internet Server’ından kişinin bilgisayarına yüklenmesi için geçecek süreyi hesap etme imkanları bulunmaktadır. Bu imkandan yararlanılarak, sayfamızın Internet’e örneğin saniyede 14.4 Kbps aktarabilen bir modemle bağlı kişinin bilgisayarına ne kadar sürede aktarılacağını daima gözönünde tutmalıyız.

Web sayfalarımızı, Microsoft firmasının Internet Explorer programı ile izleyecekler kadar, hatta onlardan daha çok sayıda Netscape firmasının Navigator programını kullanarak ziyaret edecek kişiler olacağını hiç bir zaman akıldan çıkartmamalıyız.

Web sayfalarımız, bizi ziyaret eden kişinin bilgisayarında mevcut düzenleri asla bozmamalıdır. Bizim sayfamız, örneğin ziyaretçinin kullandığı programı tam ekran çalışmaya zorlarsa, ortaya hiç istemediğimiz sonuçlar çıkabilir. Biz bir takım bilgisayar programlarının nelere muktedir olduğunu, bilgisayar kullanıcılara kanıtlamak üzere Web sayfası yapmıyoruz. Adı üstünde sayfamızı ziyaret eden kişi ziyaretçi olduğuna göre kendisine mümkün olan bütün saygımızı göstermek zorundayız.

Ağ Davranış Kuralları adıyla (Network Etiquette--Netiquette) yaygın olan kuralları burada kısaca tekrar edelim:

1. Kimseye hakaret etmeyin ve kimseyi öfkelendirmeyin. Sayfanıza sadece güzel şeyleri alın. Kimseyi küçük düşürücü yazı veya resim yayınlamayın.

2. Sahibinin izni olmadan, telif hakkı başkasına ait eserleri sayfanıza koymayın. Bir yazı ve resmin, ya da bir başka sanat eserinin fotoğrafının mutlaka bir telif hakkı sahibi vardır. Bir yazının yazarının, bir fotoğrafın fotoğraçının, bir resmin ressamın izni olmadan bir basın-yayın aracına alınarak yayınlanması nasıl yasaksa, aynı şekilde Web sayfasına da konması da yayınlanması anlamına gelir ve aynı şekilde yasaktır. Bir Web yöneticisinin günümüzde söyleyebileceği en yanlış söz, “Nereden bilecekler!” sözü olsa gerek.

3. Ticaret simgesi ve ticari marka gibi, yanında belirleyici simgesi olan logoları, ilgili firma ile açıkça yapılmış bir anlaşmanız yoksa kullanmayın.

4. Sizden kendi sayfasına bağlantı vermenizi istememiş veya sayfasında bunu açıkça belirtmemiş kişi veya kuruluşların sayfalarına asla bağlantı vermeyin. Belirli bir Web alanına veya sayfasına bağlantı vermeniz gerektiğini düşünüyorsanız, sayfanın sahibinden yazılı izin alın.

5. Ziyaretçilerinizin size, alanınız ve sayfanız hakkında ne düşündüklerini söyleme fırsatı verin; sayfalarınızın altında, Webmaster’ın adresini vermeyi ihmal etmeyin.

### Görsel Denge

Günümüzde içeriği tayin ederken düşülen en büyük yanlışlardan biri, Internet’in en büyük müdavimlerinin iki satırdan daha fazlasını okumayan kişiler olduğu varsayımıdır. Internet’ten toplumun her kesiminden kişilerin yararlandığını varsaymak zorundayız. Sayfamızın amacı uzun uzun bilgi vermekse, “Nasıl olsa kimse okumuyor!” diye bu bilgileri kırpmak, gerçekten o bilgiye ihtiyacı olan kişilere haksızlık olur. Sayfamızın bir hareket noktası, bir geçiş noktası olduğunu tahmin ediyorsak, kimseyi fazla oyalamaya, istemediklerini bildiğimiz bilgileri zorla vermeye de hakkımız yoktur.

Grafik tasarımcı, içeriğin trafik polisidir, dersek gerçeği abartmış olmayız. Hangi görsel etkinin nasıl sağlanacağını belirlemek görsel tasarımcının işidir. Tasarımcı, bu işi yaparken önemli unsurların zincirin başında gelmesini sağlamalı, bilgi akışının belirlenmiş kurallara uygun bir şekilde ziyaretçiye ulaşmasına yardımcı olmalıdır.

Yale Tıp Fakültesi’nin, ekrana bakan kişinin göz hareketlerini belirleyen cihazlarla donattığı bilgisayarların başına oturttuğu 12 bin kişiyle yaptığı araştırma bir bilgisayar ekranının görsel taranma çizgisinin, (1) soldan üst köşeden sağ üst köşeye, (2) sağ üst köşeden sağ alt köşeye doğru genel tarama (3) yeniden sol üstten itibaren okuma, ve (4) üst orta noktadan aşağı doğru okumayı sürdürme tarzında olduğunu gösteriyor.

<webgors2.tif>

Buna göre, izleyici Web sayfasında önce büyük şekil kitlesini ve renkleri görmekte, önplandaki unsurlarla arka plandaki unsurlar arasındaki kontrastın farkına varmaktadır. İzleyici ancak daha sonra, varsa grafik unsurların verdiği bilgiyi almakta, üçüncü olarak da okumaya başlamaktadır. Okuma tahmin edilebileceği gibi, en büyük kitleden benzetme yoluyla başlamakta ve daha sonra kelimelere inmektedir.

Bu belirleme, bize, Web sayfasının bütünü itibariyle mükemmel bir grafik dengesine sahip olması gerektiğini gösteriyor: salt metinden ibaret gri bir sayfa itici ve sıkıcı iken, büyük ve geniş grafikler, büyük ve kara likeler halindeki harfler özellikle içerik arayan daha rafine izleyiciye “içi boş” izlenimini verecektir. Grafik sanatçı, bu noktada sayfanın beklenen “müşterisi”nin varsayılan ilgi odağını, grafikle metni dengeleyerek bulmak zorundadır.

<webgors1.tif>

Bu dengede oran ve uygunluk, sadece sayfanın hedef kitlesi, ya da başka bir deyişle sayfanın içeriği dikkate alınarak bulunabilir.

Yazıyı soldan sağa doğru okumaya alışmış toplumlarda, görsel dikkatin ekranda da soldan sağa doğru gitmesi doğaldır. Bu nedenle Web sayfalarında da ekranın üst yarısı, görsel odak noktası olmalıdır. Ne var ki, 14 ile 16 inç arasında değişen en yaygın ekran türünde, önce işletme sisteminin menüleri, altında browser’ın başlık ve menüleri, genellikle grafik sanatçısına, çalışabileceği temiz alan olarak 8 cm’e 13 cm’lik bir alan bırakmaktadır. Bu alanın mümkün olduğu kadar yumuşak, pastel renklerle doldurulması; sert, aşırı yoğun çarpıcı renklerden kaçınılması gerekir. Bu tür renkler ancak çok fazla dikkat çekmek istediğimiz, bir ya da iki unsur için saklanmalıdır. Yazılar mutlaka arkalarındaki zeminle çarpıcı bir kontrast oluşturmalıdır. Dramatik ve karmaşık grafikler, mutlaka grafik sanatçıları tarafından yapılmalıdır.

Metinleri daha belirgin hale getirecek noktalar, kutular, yatak ve dikey çizgiler, çoğu zaman görsel bütünlük sağlamak yerine sayfanın tümüne yama hissi verirler. Görsel sanatçıların çoğunun HTML dilinden nefret etmelerinin sebebi, H1 ve H2 başlık etiketlerinin çoğu zaman aşırı büyük başlıklar oluşturmasındandır. Grafik sanatçıları, görsel etki unsurlarının etkisini iyi bildikleri gibi, HTML gibi, hassas ayara izin vermeyen bir dille, stilistik ürünler vermenin zor olduğunu biliyorlar. Aşırı kullanılan grafik etkinin, nasıl bir sonuç verdiği, palyaçoların makyajlarından ve giysilerinden kolayca anlaşılabilir.

Bütün görsel tasarımlarda olduğu gibi, Web sayfası tasarımında da tutarlılık şarttır. Web alanları, günümüzde firmaların kurumsal imajlarının oluşumunda en önemli unsur haline gelmiş bulunuyorlar. Bir firmanın basın ve televizyon reklamlarında nasıl aynı imaj sürdürülmek zorunda ise, sonuçta bir tür televizyondan ibaret olan Web’de de aynı imajın korunması gerekir.

Grafik unsurlarla “stil” oluşturmaya kalkmak, grafikçilerin işidir. Bir Web alanının başından sonuna tutarlı bir şekilde izlenen grafik uygulama, sonunda izleyicide Web alanının sahibi kurum hakkında bir yorum uyandırır. Bu nedenle sırf süsleme amacıyla, sayfaların orasına burasına çizgi ya da fotoğraf unsurları konulmamalıdır. Özellikle çizgi grafiklerin üç boyutlu görünmesini sağlamak gerektiği inancı, günümüzde hemen hemen bütün Web tasarımına egemen olmuş ve hemen hemen her grafik unsurun bir tarafına gölgeler yerleştirilmiş bulunuyor. Gölge, bir görsel öge olarak kullanılacaksa, sayfanın tümünün bir bütün olduğu unutulmamalıdır. Bir unsurun gölgesi sağa aşağı, diğerininki sola yukarı düşemez. Böyle bir uygulama, sayfayı izleyende derinlik duygusundan çok baş dönmesi ve mide bulantısı duygusu verir!

Ana sayfa, ya da yaygın adıyla home page, ya da giderek moda olan bir yaklaşımın verdiği isimle splash page, izleyicinin bizim Web alanımıza daldığı noktadır. Bu nedenle sayfada bir davet unsuru olması şarttır. Bu sayfanın az ve öz unsun içermesi de giderek yaygın bir tarz olmaya başladı.

Ancak izleyicinin içi tamamen boş, alanımızın ana unsurlarına bağlantılar vermeyen, buna karşılık görkemli grafikler içeren bir sayfa ile zaman kaybetmesi, bize ne kazandırır? Bir gazete veya derginin Web alanı, yayınladığı organın kapak sayfasına benzeyebilir. Ama bir üretim firması, ana sayfasında hiç değilse belli başlı mal gruplarının bağlantıları olmalıdır.

Çoğu Internet’e modemle bağlanan izleyiciler için, minimalist, yani küçük grafiklerin geniş alanlar işgal etmesini sağlayan, başlıklardan ve beyaz alanlardan yararlanan, buna karşılık görsel etkisi son dere yüksek sayfalar yapılması mümkündür.

### Ekranın coğrafyası

Özellikle meslek yaşamı boyunca kağıt üzerinde grafik üreten sanatçıların, bilgisayar ekranında izlenmek üzere grafik yapmaya başladıklarında karşı karşıya kaldıkları ilk sorun, ekranda büyük görünen grafiğin kağıt üzerinde küçücük kalmasıdır. Kağıt üzerine geçirilecek grafikleri bilgisayarla çizen grafik sanatçılarından kimi de kullandıkları 21 inçlik ekranda yaptıkları grafiklerin, evlerdeki 14 inçlik ekranlarda nasıl görüneceğini pek hesaba katmazlar. Yapılan hemen hemen bütün araştırmalar, Web ziyaretçilerinin sadece yüzde 10'unun bir ekranın sağında ve altında kalan unsurları görmek için, kaydırma çubuklarını kullandıklarını gösteriyor. Başka bir deyişle, grafiğiniz, 14 inçlik bir ekranın sağından ve altından dışarı taşıyorsa, izleyicilerinizin yüzde 90'ını kaybediyorsunuz, demektir.

Bilgisayar ekranı, çoğu zaman gazete ve dergi sayfalarından küçüktür. Web tasarımında sık sık yapılan hata, grafiklerin 14 inçlik bir ekranın temiz görüntü alanının dışına çıkmasıdır. Macintosh ve Windows’un kapladıkları alanlarla Internet Explorer ve Netscape Navigator’ın çerçeve başlıkları çıktıktan sonra kalan bu temiz alanın ölçüsü, 535 pixel genişliğinde320 pixel yüksekliğindedir. Pixel, ekranda görüntüyü oluşturan noktaların ölçüdür ve ekran imalatçısına göre ve ekranın büyüklüğüne göre değişmektedir. Bu ölçüyü geçen bir grafik, A4 kağıda basılamaz.

<webalan.tif>

Buna göre, tasarımcı genişliği 13 ile 15 inç arasında değişen bir ekrana göre çalışsa bile yapacağı sayfanın kağıda dökülmesi ihtimali varsa, sayfasının enini, 600 değil, 535 pixel’i geçmeyecek şekilde ayarlamalıdır. Ekrandaki sayfamızın eni kağıt üzerinde yaklaşık 21 cm olur. Oysa bunun yaklaşık 19 cm’si kağıda basılabilir. Buna karşılık kullanıcının sayfasını aşağı-yukarı kaydırmasını önlemek üzere tasarlanan bir ekran sayfasının yüksekliği 350 pixel (yaklaşık 12.5 cm) olurken, 672 pixel (yaklaşık 23.5 cm) bir ekran sayfası sayfa rahatça A4 veya ABD standardı dosya kağıdına basılabilir. Bir çok Web sayfasının kağıda dökülmesi tasarımcının ilk olarak gözönünde tuttuğu husus değildir. Tasarımcı, çok metin unsuru yeralan sayfaların hemen hemen daima kağıda döküleceğini unutmamalıdır. VGA ekranı sağından soluna dolduran bir yazı, kağıda döküldüğünde, sağdan 2 santimetresini kaybedecek demektir. Browser programların Macintosh veya Windows ortamında tam ekran olarak gösterdikleri temiz alan farklıdır. Bu nedenle kayıp, 2 cm’nin altında veya üstünde olabilir.

Baskı bakımından kayba uğramayacak “tam ekran” ölçüleri Netscape Navigator ve Internet Explorer’da azami genişlik 535 pixel, azami yükseklik 295 pixel olarak planlanmalıdır. Buna karşılık basılması düşünülmeyen sayfalar 595'e 295 pixel olarak çalışılabilir.

Burada sayfanın uzunluğundan da söz etmek zorundayız. Bilgisayar ekranlarının sağındaki kaydırma çubuğu, ekrandan uzun bir içeriğin yukarı doğru kaydırılmasını sağlar. Özellikle firmanın Web alanı için önemli sayfaların bağlantıları, bir ekran dolusu içeriğin altında kalırsa, izleyicinin nerede ne gibi bağlantı olduğunu bilmediğini ve çok az kişinin ekranında sayfayı yukarı doğru kaydırdığı gerçeğini hatırlarsak, büyük bir ihtimalle ana sayfamıza kadar gelmiş bir ziyaretçinin bizim için önemli sayfalara gitmesini sağlayamamış oluruz.

Sayfamızı ekrandan uzun tutmaya karar verirken, izleyicinin sayfayı mutlaka kaydıracağından emin olmalıyız. Bir gazetenin haber özetleri sayfasını tasarlayan kişi, bundan hemen hemen yüzde 100 emin olabilir; ziyaretçi zaten haberi okumak için o sayfada bulunmaktadır ve haber ne kadar uzunsa, ekranını o kadar kaydıracaktır. Ama metin halinde bilgi verilmeyen buna karşılık tasarımcı için önemli bağlantılara yer verilen bir sayfanın, bağlantıların bulunduğu alt kenarı, tasarımcının bir yanlış hesabı sonucu ekranın 2 santimetre altında kalmış ise, bağlantıların orada olabileceğini tahmin etmeyen bir çok kişi, bu içi boş sayfaya bir kaç dakika baktıktan sonra mouse’ını Geri Dön düğmesine doğru sürmeye başlayacaktır.

HTML dilini kullanarak yaptığımız sayfaların, gazete dergi sayfası gibi statik olmadığını hatırlamamız gerekir. Adı üzerinde HTML, hypertext’e--ekranı yani birbirine sıçratabilecek hyper bağlantılar içeren metinlere--dayanmaktadır. Verilecek bilgiler ekranlar dolusu bir metin oluşturuyorsa, bunu bir ekranlık parçalara bölerek, ve parçaları birbirine bağlantılayarak, izleyicinin kaydırma çubuğunu kullanma zorunluğunu ortadan kaldırabiliriz. Verdiğimiz bilgi gerçekten çok uzunsa, örneğin bir şirketin yıllık mali raporunu Web sayfalarımıza koyacaksak, daha iyi bir teknik raporun yazı ve grafikleri ile birlikte kullanıcının bilgisayarına download edilmesi için bir bağlantı koymak olabilir.

### Web’de Sayfa Düzeni

Mevcut Web sayfası tasarım programları, Quark Express, Corel Ventura veya Adobe PageMaker gibi sayfa tasarım programlarından çok daha az denetim imkanı getirmektedir. Bunun başlıca nedeni, kullanıcının bilgisayarı ile Web Server programının bulunduğu bilgisayar arasındaki iletişim protokolüne (HTTP) uygun bir iletişim sağlamak zorunda olan HTML dilinin karşı karşıya olduğu teknik zorluklardır. Ama bu zorluklar, bir taraftan HTTP protokolünde, diğer taraftan browser programlarının HTML’i yorumlayışlarındaki sürekli gelişme sayesinde, yavaş da olsa, giderek azalmaktadır. Şimdilik bazı zorluklar var diye, HTML sayfaların palyaço makyajı gibi olması da gerekmez. HTML ile yapılabilecek muhteşem tasarımlar vardır. Hele, HTML 4.0 sürümü ile sağlanan ve sayfalarda görsel birlik bağlamakta kullanılması gereken yerel STYLE kodu veya Cascading Style Sheet (CCS) adı verilen stil komutları dosyası oluşturma imkanı, görsel açıdan etkili HTML sayfalar yapmayı mümkün kılmaktadır.

Aşağıda, görsel açıdan arzu edilen etkiyi sağlamakta kullanılabilecek bazı HTML tasarım kolaylıkları sıralanmaktadır:

| Renk |
| --- |

Bir Web alanının çeşitli sayfaları arasında görsel birliği, belki de diğer grafik unsurlardan daha fazla, renk birliği sağlar. Daima Macintosh sisteminin daha zengin renk skalası yerine Windows’un daha kısıtlı temel renklerini kullanınız. Windows 95 ile PC dünyasına da 256 renk içeren paletler gelmiş olmakla birlikte, Windows sistemi gerçekte 216 renk üretebilir. güvenli bir renk skalası, en az üç en fazla beş renk içermelidir. Bu renklerin Windows’ın sistem renkleri olmasına dikkat ediniz. Sistem skalasında yer almayan bir renk seçtiğiniz zaman, bu rengin hangi tür bilgisayar ekranında nasıl gösterildiğini mutlaka sınayınız. Sizin ekranınızda hafif bir sarı, bir başka bilgisayarın ekranında neon sarısı olabilir. İzleyicinin bizim arzu ettiğimiz rengi, arzu ettiğimiz tonda görmesini sağlamak için, sayfanın geri planına renklendirlmiş boş kutudan oluşan grafik yerleştirmek, sadece sayfanın aktarılmasını geciktirmeye yarar. Renk tonundan fedakarlık ederek, sayfalarımızın hızlı aktarılabilir olmasını sağlamalıyız. Netscape’in renkleri Hexadecimal sayılarla tanıdığı, buna karşılık Explorer’ın renkleri isimleriyle tanıyabildiğini unutmamak gerekir. Explorer da hexadecimal değerleri tanıyabildiğine göre, güvenli bir uygulama daima renklerini sayıyla ifade etmektir.

| Ölçüler |
| --- |

Sayfanın kodlanması sırasında işi şansa bırakarak, ölçüleri yüzde olarak vermeyiniz; daima pixel olarak veriniz. Yatay olarak bütün unsurlarınızın genişliği, sayfanın izleyici tarafından kağıda basılacağını tahmin ediyorsanız 539 pixel’i, sadece ekranda seyredileceğini düşünüyorsanız 350'yi geçmemelidir. Bununla birlikte sayfada yatay veya dikey kaydırma çubuğunun çıkmasına neden olmayacak bir tasarımda, ölçülerin yüzde olarak verilmesi, büyük ekranı olan izleyicilerin teknik imkanlarından kendi lehimize yararlanmamızı sağlar.

| Sütun |
| --- |

HTML, sayfayı sütunlara bölemez. Bu bakımdan sütunlu sayfa düzeni ya tablo ile, ya da grafik unsurların mutlak koordinatları verilerek yapılabilir. Mutlak koordinat yöntemi sadece browser programlarının 4.0'ncü sürümüyle uygulanabilir olduğuna göre, eski sürüm browser sahipleri, bizim sütunlar halinde görüleceğini sandığımız unsurları, alt alta dizilmiş olarak görebilirler. Tabloların kutularına arka plan rengi ve görüntüsü verebiliriz. Bu imkandan yararlanırken, sayfanın aktarılması hızını ne ölçüde yavaşlattığımızı hesaba katmalıyız. Tablonun her bir kutusunu, bağımsız bir HTML sayfası gibi ele alabilir ve içine metin ve grafikleri yerleştirebilirsiniz. Yeni sürüm browserlar, tablo kutusu içine yeni bir tablo bile kabul edebilirler. Tablo, etkili bir sayfa tasarımında güçlü bir araç olarak kullanılabilir.

| Çerçeve |
| --- |

HTML’e sütun görüntüsü veren bir diğer imkan çerçeve (frame) komutlarıdır. Ne var ki, bilgisayar kullanıcılarının sahip olduğu browserların eski sürümleri, çerçeve komutlarını yorumlayamazlar. Çerçeveli sayfaların yavaş yüklendiği gerçeği de bir çok kullanıcıda çerçeveye karşı olumsuz bir önyargı oluşturmuş bulunuyor. Bununla birlikte çerçeve, sayfanın bir köşesini sabit hale getirerek, tasarımcıya değişmeyen bir seyir denetim alanı verir ve bağlantılar buraya yerleştirilebilir; ama tasarımı önce hiç çerçeve kullanmadan yapmanın yollarını aramalıyız. Seyir (navgation) bağlantılarımızı, her sayfada tekrarlamak veya bağlantı komutlarını içeren basit grafiği her sayfada tekrar ederek, çerçeveye başvurmaktan kurtulmak mümkündür. Çerçeve kullanmaktan başka çare yoksa, çerçeve genişliklerinin toplamının, tayin ettiğiniz sayfa genişliğini aşmamasına özen gösteriniz. Bir sayfanın ortasında beliren kaydırma çubuğu kadar kötü görsel etki oluşturulan başka bir uygulama olamaz! Kaydırmak çubuğundan kurtulmak için çerçevelerin kaydırılamaz olmasını (scrolling=none) sağlamak ise, doludan kaçarken yağmura tutulmak olur. Çerçevenin içeriği çerçeveye kalan alanı aşmıyorsa, kaydırma çubuğu ekrana gelmeyecektir. Kaydırma tümüyle önlenir ama içerik ekranın sağından dışarı taşarsa, izleyicinin içine düşeceği öfkeyi düşünün ve kaydırma komutunu otomatik’te tutun (scrolling=auto). Her sayfanın bir de çerçevesiz türünü yapıp, her ikisini birbirine bağlantılandırmak, izleyeciye saygılı bir tasarımcının başlıca ilkelerinden biri olmalıdır. Bu arada IFRAME komutu ile ilgili ufak bir hatırlatma yapmakta yarar var: Frameset komutu kullanmadan, bir HTML sayfasının içine yüzen bir başka çerçeve yerleştirmeye imkan veren bu komut, şu anda sadece Explorer tarafından tanınmaktadır. Etkili bir görsel unsur oluşturulan ve Frameset gibi bilgisayardan bilgisayara aktarılması zaman almayan bu yararlı komutu kullanabilmek için en azından Nestcape 5.0'e kadar beklemek gerekiyor.

| Grafiklere konulacak bağlantı komutları (map’ler) |
| --- |

Daima client side map kullanmaya özen gösteriniz. Server side map komutları, izleyicinin bilgisayarı ile Web Server bilgisayarı arasında iletişimi iki kez arttırmaktan başka bir işe yaramayan eski bir teknolojidir.

| Metin Biçimlerdirme |
| --- |

HTML’de yazıları şekillendirme, henüz yeni başlıyor. Quark’ın imkanlarının HTML’e gelmesi için daha çok zaman geçmesi gerekiyor! Ama durum o kadar da umutsuz değil. Explorer’da 3.0'den beri olan HTML dosyası dışı stil dosyası (cascading style sheet, CCS) tanıma imkanı, Netscape 4.0'e de bir ara sürümle gelmiş bulunuyor. Ama browser’ları en son sürümle güncelleştirilmiş kaç kişi var? (Kendi sorumuzun cevabını verirsek, bir araştırma Türkiye’deki tüm browser’ların sadece yüzde 12'sinin her iki programın 4'ncü sürümü olduğunu gösteriyor.) Fakat her iki programın 3'ncü sürümlerinden bu yana ortak tarafı, HTML’in içine yerleştirilmiş STYLE komutunu tanımalarıdır. Bu imkanısayfalarınızı zenginleştiren bir şekilde kullanmak mümkündür. SPAN komutunu, STYLE ile birlikte kullanarak, H1-H6'ya bağlı kalmadan etkili sayfalar yapılabilir. Paragrafların sayfanın sağına, soluna veya ortasına bloke edilmesini sağlayan “text-align:” komutu, bir başka güçlü tasarım unsuru olarak kullanılabilir. Her bir paragrafa, bir diğerinden bağımsız sağ ve sol boşluklar (margin) vermek mümkündür. Biçimlendirme komutlarınızı sayfanın başında tanımlarsanız, aşağıda istediğiniz gibi yararlanabileceğiniz tag’ler elde etmiş olursunuz.

| Form |
| --- |

Bir gazete veya dergi sayfasının ya da televizyonun yapamayacağı fakat HTML’in yapabileceği bir şey varsa, o da FORM komutunun kullanılması olmalı. Form, kullanıcının Web server ile ile etkileşmesinde doğrudan kullanabileceğimiz bir işleve sahiptir. Form ile ziyaretçi bize bilgi verebilir, bilgi isteyebilir; hatta form komutu ile izleyiciye bizim bilgisayarımızı kullanma, izin verdiğimiz programları işletme imkanı bile verebiliriz. Form sayfanın kendisinden beklenen etkileşmeyi sağlayabilmek için teknikten önce uygun bir görsel etkiye sahip olması gerekir. Bu nedenle formlar, Web sayfasının teknik yönetmeni tarafından komutlandırılmadan önce, grafik tasarımcısı tarafından çizilmelidir. Form sayfalarında izleyicinin kutudan kutuya gitmesinin mantıksal bir çizgi izlemesi gerekir. Örneğin, izleyicinin adresini yazarken, sokak adı ve bina numarasından önce kenti yazmasını istemeyiniz. Herkes, yıllarca resmi ya da resmi olmayan formlar doldurarak, adeta belirli bir form beklentisine sahiptir. Bu beklentiyi bozmak izleyiciyi şaşırtabilir. Formlarda istenen bilgilerden radyo düğmesi veya işaretleme kutusunun seçilmesi suretiyle verilecek olanların değişkenleri aynı ismi taşımalıdır. Aksi taktirde, örneğin bu formla elde edilecek bilgi bir veri tabanına işlenecekse, ortaya kullanışlı olmayan bir sütun çıkartmış olursunuz. Formlarda, mutlaka doldurulması gereken kutular, belirgin bir renkte ve açık ifadelerle işaretlenmiş olmalıdır. Formların bağlı olduğu CGI programları, formu dolduran kişiye o anda ekran başında ve daha sonra elektronik posta ile formunun alındığını bildirmelidir. Kısa bir teşekkür mesajı içerek bu bildirim ekranında, mutlaka formdan bir önceki sayfaya geri dönme imkanı olmalıdır. Formun yanlış doldurulduğu kullanıcıya ayrıntılı olarak bildirilmeli, hangi kutuda, hangi bilgide hata olduğu veya hangi kutunun mutlaka doldurulması gerektiği açıkça kaydedilmelidir. Hata bildiren ekrandan geriye dönüşte, formun boş şekli ne değil, hatalı da olsa doldurulmuş şekline dönme sağlanmalıdır. Formda kredi kartı numarası, adres, ya da kişinin özel yaşamıyla ilgili izinsiz açıklanması mümkün olmayan bilgiler isteniyorsa, formun belirgin bir yerinde bu bilgilerin gizli tutulacağı güvencesi yer almalı ve bu gizliliğin sağlanması için CGI tarafında gereken önlemler alınmalıdır. Elektronik ticaretle ilgili formlarda, bize güvenliği veren firmanın, sistemin veya bankanın güvenlikle ilgili logosu belirgin şekilde kullanılmalıdır.

| ALT |
| --- |

Grafikleri bilgisayarına aktaramayan bir izleyici, sizin koyduğunuz grafik yerine çirkin bir kopuk bağlantı simgesi görür. Oysa bunun yerine, yüklenemeyen grafiği anlatan bir kaç kelime, kullanıcıyı meraktan kurtarır.

| META ETİKETLER |
| --- |

Web alanımızın izleyene bir şey kazandırmasını sağlamak, ziyaretçiye yeniden gelmesi için çıkartılmış en etkili davetiyedir. Yeniden ziyareti sağlamak kadar, sayfalarımızın varlığını bile bilmeyen, özellikle belirli bir koruda arama yapan kişilerin karşısına kolayca çıkabilmemiz gerekir. Belirli arama sistemlerini işleten kurum ve kuruluşlar, Internet’teki sayfaların tümünü inceleyerek içindekileri indekslemek yerine, HTML sayfalarının başındaki META tag’lerini kaydetmekte ve indekslerini burada yer alan bilgilerle yapmaktadırlar. Bu nedenle, bütün HTML dosyalarımızın başında, örneğin:

<META name="description" content=" Filanca Gazete / Filanca Online / Filanca Newspaper ">

<META name="keywords" content= "filanca, hurriyet, turkiye, turk, turkce, basin, gazete, haber, gundem, politika, dunya, spor, ilan, ekonomi, yazar, news, newspaper, press , journal, daily, politics, international, sports, journalist, economy, advertisement ">

şeklinde tanıtma satırları bulunmalıdır. Ayrıca SubmitIt.com firmasının sağladığı, sayfalarımızı ilgili alanlara ulaştırarak, bağlantı verilmesi imkanından yararlanma yollarını aramalıyız. Başkalarının bağlantı verdiği sayfaların HTTP adresini değiştirmemeye özen göstermeliyiz. Adresimizi değiştirmek zorunda kalırsak, en az altı ay süreyle eski adresi koruyup, buradan yeni adrese otomatik ve elle kullanılabilen bağlantılar vermek, mevcut ziyaretçi kitlesini kaybetmemek açısından önem taşır.

| Bağlantıları Kontrol Edin |
| --- |

Sitenizi Server'a gönderdikten sonra, ziyaretçi gibi sitenize girin ve bütün bağlantıları tıklayın. Bazı HTML editörleri, metin veya resim unsurlarına veya diğer sayfalara bağlantı (link) kurduğunuz zaman, HREF etiketinin karşısına bağlantının hedefini yazarken, bu unsurun bulunduğu sabit diskin ve dizinin adını da yazarlar: <A HREF="c:\\Web\\yenisayfa.htm"></A> gibi. Böyle bir bağlantıyı içeren sayfayı sitenize koyduğunuz zaman, Server'ın bulunduğu bilgisayarda sayfanız gerçekten C: diskinde ve Web dizininde ise, bazen mesele olmayabilir. Çoğunlukta ziyaretçiniz bir hata mesajı alacaktır. Sitenin durduğu dizin, Server açısından o sitenin kök dizinidir ve bütün diğer dizinler kök dizine göre göreli (relatif) olarak gösterilmelidir. Sayfanız, sitenizin içinde Web dizininde ise bu bağlantının doğru şekilde gösterilmesi şöyle sağlanır: <A HREF="./Web/ yenisayfa.htm"></A>. Dikkat ederseniz, ters bölü işaretinin yerine düz bölü işareti kullanıyoruz.

| Yükünüzü Azaltın |
| --- |

Sayfanızda gerçekten bir anlamı olmayan, bir maksada hizmet etmeyen ne varsa atın. Hele, "Siz bilmen ne zamandan beri bilmem kaçıncı ziyaretçisiniz!" diyen sayaçların ziyaretçiye ne faydası var? Coğrafî olarak binlerce kilometre uzakta ve Internet'te omurgaya 30 etap ötede bulunan bir ziyaretçi, sitenizi kaçıncı ziyareççi olarak ziyaret ettiğini bilse ne olur? Oysa bu sayacın bağlı olduğu CGI programının çalışması ve sonucu bildirmesi, ziyaretçi için fazladan zaman kaybıdır.

Yazıyla belirtebileceğiniz bir unsuru, grafikle belirtmekten vazgeçin. Browser'ının kuruluş özelliklerinde grafikleri istemediğini belirtmiş ziyaretçileri düşünerek, her grafik bağlantı unsurunun bir de metin bağlantı unsuru olmasını sağlayın.

Özellikle grafik olarak sunulan metinlerde kısaltma yapmayın; kısa bir kelime bulun.

| Türkçe.. Türkçe.. Türkçe.. |
| --- |

Bu bölümü kapatırken, buraya kadar söylenenler ölçüsünde--hatta onlardan çok daha fazla-- önemli şu uyarıyı asla unutmayın:

Sayfalarınızda Türkçe dil bilgisi ve yazım hatası yapmayınız. İyi bir İmla Klavuzu, ve metinlerin (özellikle grafik halinde sunulan yazıların) daktilo ve Türkçe hatası içermemesi gerekir. Bu, söylemesi kolay ama yerine getirmesi oldukça güç kurala riayet, ziyaretçilerinize ve ortak kültürümüze ne denli saygılı olduğunuzun en büyük göstergesi olacaktır.

# Ek 1 Özel Internet: Intranet

İster parekende, ister toptan alışveriş amacıyla olsun, elektronik alışveriş yapmak üzere bilgisayarı ile bir firmanın Web sitesine bağlanacak kişinin karşısına çıkacak Web sayfaları ne kadar dinamik, ne kadar albenili olursa olsun, bu sayfaların gerisinde, o sayfalarda sunulacak mal ve hizmetlerin arzını sağlayacak, yani kredi kartı bilgisini anında doğrulatacak, mal ve hizmetin teslim edilmeye hazır olup olmadığını belirleyecek, dolayısıyla firmanın bütün mal ve hizmetlerinin envanterini tutacak, satılan malın sevk belgelerini dolduracak, dağıtıcıya teslim fişlerini yazacak ve envanteri güncelleştirecek bir sistem yoksa, elektronik ticaretin yararlarını görmek şöyle dursun, kendi kendimize--sağlayacağı gelirle oranlı olmayan--yeni masraf kapıları açıyoruz, demektir.

Gerçek zamanlı olmayan, yani günün sonunda bir personelin klasik yöntemlerle kredi kartını doğrulatmasına dayanan sistem, bize kolaylık değil, ikinci bir yük getirir. Satılan malın envanterinin tutulması elektronik değilse--bu sistemin mağazalar sistemi ile birleştirilmesi zorunluğu nedeniyle--mağazalarda mevcut sistemin dışında ikinci bir uğraşı anlamına gelir.

Oysa elektronik ticaret, sabit masrafları asgari düzeyde tutarak, azami kazancın elde edilmesini sağlamalıdır. Internet’teki Web sayfaları, tek ya da iki kişilik işletmelerin, 10-20 kişilik perakende satış yerlerinin yaptığından daha fazla kazanç elde ettiğine ilişkin başarı öyküleri ile dolu ise, nedeni, bu bir ya da iki kişinin yanında, depolamayı nerede ise sıfıra indiren, kayıt ve takip işlemleri dahil bürokratik tüm işlemleri otomasyona bağlayan, bilgisayar şebekesi bulunmasıdır.

Günümüzde, bilgisayarlardan yararlanmayan ve bilgisayarları şebekeleşmemiş bir kurum düşünmek hemen hemen imkansız hale gelmiş bulunuyor. Firmaların ister elektronik ticaret, ister reklam, ister prestij amaçlı olsun, Internet’te giderek artan varlıkları da kendi kurumları içindeki işlemlerinin bilgisayar şebekelerine dayanmasını ayrıca zorunlu kılıyor.

Bir firma, bazı bölümlerinde bilgisayara dayalı bile olsa bilgisayarları arasında veri deposu, envanter, elektronik iletişim ve bu bilgilerin Internet yoluyla müşterilere açılması gibi alanlarda henüz şebekeleşmiş olması şarttır. Bu amaçla,

1. Bir firmanın genel merkez idare birimleri, fabrikalar, tasarım atölyeleri ve mağazalarında, Yerel Alan Ağı (Local Area Network, LAN) oluşturması ve LAN’ların arasında Geniş Alan ağı (Wide Area Network, WAN) kurması şarttır.

2. WAN çapında, sadece firma mensuplarının kullanacağı bir "dahilî Internet, yani intranet kurması ve bunu Internet’e bağlaması gerekir.

3. Bu sağlandıktan sonra firma Internet'te Web sitesi kurabilir veya varolan Web sitesini elektronik ticaret amaçlı hale getirebilir.

İki bilgisayarın bir şekilde birbirine bağlanması, ortaya iki üyeli bir Yerel Bilgisayar Ağı çıkartır. Birbirine bağlanınca kadar bu iki bilgisayar arasındaki alış-veriş, ya disket değişimi yoluyla, ya da birincisinde elde edilen bilginin ikincisine yeniden girilmesi yoluyla yapılabilirdi. Ne var ki, günümüzde bir bilgisayarın elde ettiği bilgiler, ya da bir bilgisayarda oluşturulan dosyalar o denli büyük olmaya başladı ki, bu bilgilerin disketle, hatta seyyar disklerle taşınması imkanı kalmadı. Bilgisayardan bilgisayara bilgi naklinin disketle yapılması, ya da bilgilerin ikinci bilgisayara yeniden girilmesi, gerçekte bilgisayardan beklenen yararı da ortadan kaldıran, kendi-kendi kendini yok eden bir uygulama olmaktadır. Bilgisayar eğer bilginin hızla naklini sağlamak ve yapılan bir işin bir kere daha yapılmasını önleyerek personel ve zamandan tasarruf için kullanılıyorsa, bilgisayarlar arası bilgi naklinin mutlaka bu ilkeye uygun yapılması gerekir. Bu, bir işyerinde birbirine bağlı olmayan bilgisayar kalmamasını gerektirir.

## Önce Ağ

Bilgisayarlar arası ağlar, genellikle yavaş olmasıyla; ileri teknolojiye dayanan geniş çapta imalat yapan, demir-çelik ya da otomobil fabrikaları için geliştirilmiş sistemler olarak tanındı. Bu kötü şöhretin silinmesi zamanı ise çoktan gelmiş bulunuyor. İki yıl öncesinin siyah-beyaz ekranlı bilgisayar ağlarının yerini, firmalar içi Internet (Intranet), firma-içi elektronik posta, firmanın farklı kentler ve ülkelerdeki ağları arasında ise Internet-Intranet bağlantısı yoluyla ve neredeyse bedava iletişim almış bulunuyor.

Ağ teknolojisindeki gelişmelerin firmalara sağladığı bir başka kazanç ise, düne kadar bilgisayar ağı kurmak, bilgisayar bölümü adı verilen ve bir kaç kişinin gece-gündüz istihdam edildiği bir birimi zorunlu kılarken, bugün ilk kurma aşamasından sonra bilgisayar ağının, firmanın Intranet’ini ve Internet’ini idare eden kişi tarafından bakılıp, onarılabilecek kadar basitleşmesi oldu.

<webnet01.tif>

Günümüzde yerel alan bilgisayar ağları Client/Server (müşteri/hizmetkar) bağı adı verilen donanım ve yazılımla kuruluyor. Bunun için genellikle işlevsel ve fiziksel olarak birbirine yakın personelin bilgisayarları (client), bir merkez bilgisayara (server) bağlanmaktadır. Client bilgisayarların kullandığı yazılım (yazı yazma, grafik yapma, muhasebe programları) merkez bilgisayarda durmakta; merkez bilgisayar müşterilerine yazıcıdan ve fakstan yararlanma, elektronik posta alıp-verme, Intranet ve Internet’e ulaşma gibi hizmetleri sunmaktadır. Bugünün teknolojisi, client bilgisayarların doğrudan yazıcıya, faksa hatta Internet’e sahip olmalarına imkan vermekle birlikte, bu hizmetlerin yerel-merkez bilgisayarda toplanması, masraf denetimi ve yatırımın kontrolü açısından daha çok tercih edilmektedir. Bir merkez yoluyla birbirine bağlı bütün bilgisayarların kullanıcıları, birbirlerine Intranet yoluyla bağlı oldukları gibi, ağ hizmetleri çerçevesinde de alış-veriş yapabilirler. Tasarım bölümünün çizdiği bir grafik, bir anda bütün yöneticilerin bilgisayarlarından çağrılıp, bakılabilir, arzu edilirse değiştirilebilir. Muhasebe servisinin son rakamları, kağıda dökülmeden, yetki verilen bütün diğer bilgisayar kullanıcıları tarafından görülebilir.

Perakende satış noktalarında kurulacak yerel ağın merkez bilgisayarı (server), satış kasalarını da müşteri (client) gibi görebilir. Kasa makinalarını oluşturan bilgisayarlar, bütün muamelelerini server’a anında bildirirler ve server bu bilgileri gerekli veritabanlarına işlemek üzere bir kenara kaydeder.

Yerel-merkez bilgisayarları (LAN server), daha geniş bir ağın (WAN) müşterileri olabilirler. Geniş alan ağı da tıpkı yerel alan ağı gibi oluşturulur ve ağlar arasında alışverişi sağlar. LAN-WAN bağı, düne kadar firmaların telefon idarelerinden kiraladıkları gerçek zamanlı özel hatlarla gerçekleştiriliyordu. Bunun bir çok nedeninin başında, güvenlik kaygısı geliyordu. Firmalar, bilgisayar ağlarını, Internet kullanıcılarının da kullandığı bir yolla birbirine bağlamak, başkta bir deyişle kendi ağlarını Internet’e açmak istemiyorlardı.

Oysa bugün TCP/IP protokolüne, Microsoft firmasının yaptığı eklerle, günümüzde herkesin kullandığı Internet’ten tıpkı kendi özel kablo bağlantımızdan yararlanıyor gibi yararlanma imkanı var. Kısaca Tunnelling adı verilen bu yöntemler, kamuya açık Internet’te, sadece bizim kullanıcılarımızın girebildiği bir tünel açmamızı sağlıyor. Bu tünelin iki ucunda yangın duvarları \[firewall\] bulunduğu da düşünülürse, Internet’in hızı yeterli olduğu durumlarda, LAN’larımızı, WAN’ımıza Internet yoluyla bağlamamız mümkün.

Böyle bir bağlantı, firmaya Internet’ten güvenli iletişim için yararlanma imkanı verir. Ana merkez dışındaki yerel ağlarımız arasında güvenli iletişimi böylece sağlayabiliriz.

Internet’i, kendi iletişim ağının anayolu haline getirmek isteyen firmanın yapacağı ilk iş, kendisine bir Alan Adı (Domain Name) almaktır. Sonra mevcut donanımın Yerel ve Geniş Alan ağları şeklinde bağlanması gerekir. Bu iki aşamada gerçekleştirilebilir: Mevcut bilgisayarların, ağ’a bağlanabilecek şekilde Ağ Kartı ile teçhiz edilmesi ve içlerinden birinin Server olarak seçilmesi; ve sisteme bir işletme programı yüklenmesi.

Bir ağ’a bağlanacak bilgisayarın, önce kendisinin varlığını ağ’a bildirmesi, sonra ağ’ın sunacağı imkanlardan yararlanması gerekir. Bu amaçla, IBM uyumlu bilgisayarlara, çeşitli hız ve yetenekte network kartı takılır. Network kartı, adından da anlaşılacağı üzere, ağı oluşturan kablonun bilgisayara bağlanmasını sağlar. Ağı oluşturan kablo ve network kartlarının oluşturacağı kombinasyon, ağ’ın hızını ve genişliğini tayin eder. Yakın zamana kadar tipik bir yerel alan ağı mimarisi, Ethernet sistemi idi. Günümüzde Ethernet şebekesinin yeni bir türü Fast Ethernet en çok revaç gören sistem olmuştur. Kolay bulunması ve ucuz oluşu nedeniyle, Ethernet’in yıldız topoğrafyasında yapılması tercih edilmektedir. Yeni bilgisayarların ve çoğunda hazır bulunan Windows 95 işletim sisteminin, bu tür kartları takıldığında tanıması ve gerekli programları kendi kendine yüklemesi dikkate alınırsa, genellikle revaç gören bir sistemin dışına çıkarak, gereksiz para, işgücü ve zaman ayırmanın yerinde olmadığı görülebilir. Network kartlarından çıkan kablolar Hub adı verilen ve yıldızın merkezini oluşturan bir cihaza bağlanırlar. Bir ağın müşterisi (Client) veya hizmetkarı (Server) olan tüm bilgisayarlar, aynı teknik donanımla, aynı Hub’a, bağlanırlar. Hub’lar da birbirine bağlanabilir. Hub’ların teknik niteliği, Hub’dan Kart’a olan mesafeyi de tayin eder. Bu mesafe, ilave bir masraf yapmadan alınabilecek herhangi bir kart, hub ve kablo kombinasyonunda 200 metredir.

Bu işlerin gerçekleştirilmesi için, bir Enformasyon Teknoloji Bölümü kurulması mümkün olduğu gibi, şebekenin anahtar-teslimi bir müteahhit firmaya yaptırılması da mümkündür. Hangi yol izlenirse izlensin, firma yönetiminin alınacak cihazların en hızlı iletişime açık olmasını sağlaması ve firmanın elinde bulunan müstakil bütün bilgisayarların ağa dahil edilebilmesi gerekir.

Biz, firmasınnda yeni bir ağ kuracak herkese Microsoft® Windows™ NT Ağı öneriyoruz. Bu öneri yapılırken, NT sisteminin sadece farklı marka ve network kartlarına sahip bilgisayarlardan oluşan bir ağı mükemmel şekilde ve en az personelle işletmesindeki kolaylık ve üstünlükleri değil, fakat aynı zamanda bir tek paketle hem Intranet, hem Internet hem de elektronik ticaret yazılımı edinmenin mümkün olduğu gerçeği dikkate alıyoruz. Microsoft® Windows™ NT Server sistemi, Macintosh bilgisayarlarının da bulunduğu, Ethernet, Fast Ethernet, Fiber Optik, Token Ring gibi farklı işletim sistemleri, topoğrafya ve medyaya sahip bir yerel ve geniş alan ağını işletebilir. Böyle bir sistem ayrıca Backoffice adı verilen bir paketle, ağ’a ve ağda bulunan bütün bilgisayarlara hertürlü veri bankasını paylaşma, birbirinin yazıcısından yararlanma, ortak dış faks sistemi kullanma, ve piyasada mevcut 12 bine yakın kullanılmaya hazır programı ortaklaşa kullanma imkanı vermektedir. Backoffice’in elektronik ticaret imkanları aşağıda ele alınmıştır.

NT sisteminde sadece bir bilgisayar bütün sistemin ana merkezi olarak görevlendirilir. Bu bilgisayara NT sistemi yüklenirken, kendisinin Primary Domain Controller olduğu bildirilir. Bir sistemde sadece bir Primary Domain Controller bulunur, ama birden fazla Server bulunabilir. Bu Server’lar, (ana Server’ı yedeklemek amacıyla) Backup Domain Controller, (kaynakları paylaşmak amacıyla) File Server, yazıcıları paylaşmak amacıyla Print Server, Internet Information Server, Internet Commerce Server (eski adıyla Merchant Server) ve Web Server şeklinde Member Server görevleri verilir. Bu görevler, taşıyacağı ağ hizmetleri ve ağın trafiği çok değilse, ana server’a da verilebilir. Ana server’a verilen member server hizmetleri NT ortamında her an başka bilgisayarlara (server) kaydırılabilir.

Yerel ağın (LAN) oluşturulmasından sonra, sıra LAN’ın Internet’e bağlanması konusu üzerinde düşünmeye geliyor. Bu bağın niteliği, LAN’ımızın ne ölçüde hızlı bir geniş alan ağına (WAN) dönüşeceğini de tayin edecektir. Bir kere daha belirtmek gerekirse, burada kastedilen Internet bağlantısı, sadece Web sayfası demek değildir. Bu suretle oluşturacağımız Internet Sitesine bizim firmamızın personeli dışında kimse zaten girmeyecektir. Bu site ile varsa firmanın Web sayfaları arasında ilişki kurulabilir; hatta kurulmalıdır. Özellikle servisler ve yöneticiler Web Sitesine girmesini istedikleri mal ve hizmetleri, Web operatörüne ileteceklerdir. Firmanın Web sitesini ziyaret edecek kişiler sadece bu sayfalara girmiş olacaklar, fakat firmanın özel amaçlı Internet sitesinin farkında bile olmayacaklardır. Bu Internet Sitesi sadece firma içi iletişim için kullanılacaktır.

LAN ile Internet arasındaki bağlantının büyüklüğü (bandwidth) firma içi iletişimin yüküne göre belirlenmelidir. Eğer firma içi iletişimin çok yüksek olması bekleniyorsa, örneğin mağaza yöneticileri ile merkez satış yönetimi arasında hergün video konferans yapılacaksa, bağlantının T1 veya ISDN hattı ile olması şarttır. Böyle bir bağlantı düşünülmüyor, fakat sadece dosya alış-verişi ile yetinileceği bekleniyorsa, özel (dedicated) hat yerine, çevirmeli erişim yoluyla (dial-up connection) ihtiyaç anında modemle bağlantı kurulması ile yetinilebilir.

Internet Hizmet Sunucu ile LAN’ımız arasında kuracağımız bağlantının başlangıçta, ISDN hattından ibaret olması düşünülebilir. Bu hattın doğacak trafiği taşıyamaması halinde, kiralık daimi hatta bağlantıya geçilebilir.

Seçilecek bu bağlantı, bizim LAN’ın Hub’larından birine, araya Router denen bir cihaz konularak bağlanır. NT sistemi, Router olmadan da, kendisine gelecek TCP/IP mesajlarını yönlendirebilir. Ancak LAN-Internet trafiğinin yükü, araya Router koymadan yapılacak bir bağlantıda, NT Server’ı aşırı meşgul edebilir.

NT sisteminin ya ana Server’ı, ya da tayin edilecek bir üye Server’ı, elektronik posta (E-Mail) Server'ı görevi yapabilir. Bu bilgisayar, ağ’a girme yetkisi tanınmış bütün personelin IP adresini ve o anda sistemde olup olmadığını, sistemde ise fiziken hangi bilgisayarda çalıştığını bilecektir. Dış Internet’ten gelen bir TCP/IP mesajı (elektronik posta, gönderilen bir dosya, bir yazı, bir muhasebe programının spread-sheet’i, bir grafik programının tasarımı, video konferans görüntüsü, ve saire) doğruca bu bilgisayara yönlendirilecektir. Bunun için sistemdeki bütün bilgisayarlarda TCP/IP protokolünün etkin hale getirilmesi, ve NT sisteminin Internet için ana kapı olarak seçilmiş olması gerekir. Windows 95 ve Windows for Workgroups sistemlerinde TCP/IP iletişim ve NT ile bağlantı protokolü vardır. Macintosh bilgisayarlarına ise dışarıdan yüklenmesi mümkündür. Başka bir deyişle, çok eski olmamak şartıyla, günümüzde hemen hemen bütün bilgisayarlar, 25 Dolarlık Network kartı ve 10 Dolarlık kablo, 50 Dolarlık Hub ile birbirine bağlanarak, NT sistemine bağlı bir LAN haline getirilebilir; Internet Hizmet Sunucuya verilecek abone bedeli ve şehiriçi telefon ücretiyle, Türkiye’nin her tarafından, Türkiye’nin her tarafına WAN oluşturabilirler.

Bu suretle yapacağımız bir LAN-WAN-Internet bağlantısından network-centric (NC) bilgisayar şebekesi oluşturmak, Intranet kurmak ve elektronik ticaret alt yapısı için yararlanacağız.

## Intranet'in Yararları

Bir firmanın LAN ağına sahip olması, kaynakların birleştirilmesi ve daha etkin kullanılmasını sağlamak için gerekli adım olmakla birlikte yeterli adım değildir. Bunun için, oluşturulacak donanımın üzerine ya groupware adı verilen Lotus Notes veya Novell GroupWise gibi bir uygulama paketi konulması, ya da günümüzün teknolojisi olan Internet’i firma içinde gerçekleştirmek gereklidir.

Firma içi internet (Intranet), internet değildir. Intranet bir elektronik posta programı da değildir; ama firma içi ve dışı elektronik postanın getirdiği imkanlarından yararlanmak için hem iç, hem de dış e-posta programlarına sağlı olması gerekir. Birbiriyle ileşitim yapamayan bir çok farklı donanımı, Internet teknoloji yardımıyla hep birlikte devreye sokmayı başardığı için Intranet’e, günümüzde firmaların içinde karar alma sürecini hızlandıran; öğrenme sürecini kolaylaştıran; alt ve üst arasında iletişimi sağlayan; işbirliğini ve uzmanlık bilgisinin firma içinde daha kolay dolaşmasını mümkün kılan bir sihirli değnek diye bakanlar bile var.

Bir intranet firmaya iş ilişkilerinde avantaj sağlar. Günümüzün dinamik ve kıyasıya rekabete açık iş ortamında, firmaların sürekli ve hızlı şekilde yeni mamülleri piyasaya sürmesini gerekli kılmaktadır. Piyasanın değişen taleplerine cevap vermekte geç kalmak, piyasa payının kaybedilmesi tehlikesini taşımaktadır. Ayrıca günümüzün giderek artan tüketiciyi koruma anlayışı, tüketicinin firmalardan taleplerini de artırmaktadır. Intranet, bir firma içinde iletişim ve karar süreçlerine getirdiği akışkanlık ve düzen sayesinde, firmaların piyasa koşullarına cevap vermelerini hızlandırmaktadır. Bölümler arasında bilgi alışverişi artmakta, bölümlerin birbirlerinin sorularına cevap vermesi ve taleplerini yerine getirmesi daha hızlı olmaktadır. Kademeler arasındaki yazışmalar aşağıdan yukarı artan bir yetki silsilesi içinde denetlenebildiği için, birimler arasında üstünden sorumluluk atma sorunu ortadan kalkmakta, sistem-içi sorunlar bunalıma dönüşmeden çözülebilmektedir.

Intranet'in imalat ve operasyonda da avantjaları olacaktır. İmalat takvimi ve envanter kontrolü, hemen her firma içinde iç ve dış bilgilerin derlenmesine, hammadde ve ara madde arzına, satış tahmin cetvellerine, kaynak tahsis kararlarına, mühendislik bilgilerine, depo ve ulaştırma imkanlarına dayanan dinamik süreçlerdir. Intranet, sağladığı hızlı iletişim ve süratli karar mekanizması sayesinde parça sipariş ve satınalma işinde masraflı depolama zorunluklarını kaldırabilir; üretim takvimlerinin ilgili tüm personelin her an istifade edebileceği bir tarzda tutulmasını sağlayabilir; malzeme, tarif, tasarım bilgisinin daha kolay paylaşılmasını sağlayarak israfı önler.

Intranet'in muhasebe alanında sağladığı avantajlar da dikkat çekicidir. Çeşitli kaynaklardan mali analiz bilgileri toplamak ve firma bütçelerini oluşturmak, Intranet uygulamasında çok daha etkin ve hızlı yapılabilir. Intranet uygulamasında mali bilgilerin derlenmesi çok daha güvenli olabilir. Firmanın kağıda döküldüğünde daha kolay yayılabilecek bilgileri, son ana kadar Intranet’te sadece ilgililerin görebileceği tarzda saklanabilir. Mali raporlar tek merkezde ve her an istifadeye hazır olarak tutulabilir ve çeşitli ihtimal senaryoları ile kaynak tahsisi daha bilgili ve bilinçli tarzda yapılabilir. Birimlerin mali durumları hakkında daha hızlı bilgi vermesi sağlanabilir. Bordrolar daha güncel ve doğru hazırlanabilir.

Intranet'in satış ve pazarlama alanında da avantajları olacaktır. Günümüzde firmaların satış ve pazarlama bölümlerinin karşı karşıya olduğu sorunların başında firmanın sürekli değişen üretim listesini takip ve bunu yönlendirme çabası gelmektedir. Fuarlar ve sergilerin takibi, defileler ve rekabet hakkında bilgi edinilebilecek başka mecraların izlenmesi ve buralardan elde edilecek bilgilerin firmasının kendi üretimine yansıtılması, satış ve pazarlama birimlerinin en çok zaman ayırdığı işler olmakdadır. Intranet gibi, bilgi paylaşmayı en kolay ve zahmetsiz iş haline getiren bir sistem, bir firma içinde en çok pazarlamacıların işine yarayacaktır.

Özetle, Intranet, bir firma içinde bilgi alış verişinin artmasını sağlayacak ve firmanın kararları daha doğru, daha güncel ve verimli olacaktır. Intranet, bir firmanın Internet’te başarılı ticaret yapmasının da temel taşı olacaktır.

## Internet'te Ticaret

Elektronik ticaret yeni bir kavram değil. Firmalar ve kişiler yıllardan beri çeşitli türde elektronik ticaret yapıyorlar. Ancak yakın tarihe kadar yüksek masrafı ve karmaşık teknik zorunlukları dolayısıyla elektronik ticaret kitlelere yayılamıyordu. Internet, hem kolay, hem ucuz bağlantı sağlayarak, elektronik mal ve hizmet alış verişini kitlelere yaymayı başardı.

Internet’te ticaret, çok kısa süre içinde yüzmilyonlarca Dolarlık bir potansiyel oluşturmuş bulunuyor. Özellikle firmalar açısından Internet’te ticaretin sağlayabileceği kazancın, ancak yatırımcıların hayal gücü ile sınırlı olduğunu söylemek yanlış olmaz. Herşeyden önce giderek artan oranda kabul gören standartlar, firmaların iş yaptıkları diğer firmalarla ilişkilerine yeni bir görünüp kazandırmaktadır. Firmalar arası toptan ticaret, Internet aracılığıyla ticaretten en fazla yararlanan alan olmuştur. Firmalarla perakende alıcı arasındaki ilişki ise toptan ticarete oranla daha yavaş gelişmektedir. Bunda, henüz Internet’te ticaret yapan perakende satıcı sayısındaki artışın toptan alış-verişe oranla daha yavaş artıyor olması kadar, tüketicide sorumsuz yayıncılık sonucu son yıllarda yerleşmiş güvensizliğin silinmemiş olması da rol oynamaktadır. Ortalama bir bilgisayar kullanıcı, hala, bilgisayarının ekranına yazacağı bir kredi kartı numarasının ve adresin, kolayca sorumsuz ellere düşeceği kanısındadır. Bununla birlikte özellikle enformasyon teknolojisi ile uğraşan kişilerden başlayarak, aşağı doğru, bilgisayarlı alış-verişin örneğin telefonla yapılan alış-verişten daha güvenli olduğu kanısı gelişmektedir. Bu tespite parallel olarak, ABD’de elektronik ticaretin en çok bilgisayar yazılımı ve donanımı konusunda olduğu, onu yayın aboneliği, bilet ve yer ayırtma, ve borsa ile ilişkili mali hizmet alış verişinin izlediği, doğrudan perakende mal alımının ise en son sırada yer aldığı belirtilirse, Internet’e güvenin, toplumun elektronik gelişmelere en açık kesiminden, ortalama üyesine doğru geliştiği bir kere daha görülmüş olur.

Internet’te ticarete açık Web alanlarının oluşturulmasını ya da geçerli terminoloji ile ifade edersek “Elektronik mağaza” kurmayı sağlayan hazır paket programların sayısı hergün artmaktadır. Örneğin Netscape firması, yeni piyasaya sürdüğü Kiva adlı paketle, NT veya Unix sistemleri için, bir firmanın ihtiyacı olabilecek bütün yazılımları sunmaktadır. Bir ağ’da kullanma hakkı 25 bin Dolar olan bu yazılım, Web Server hizmeti gören ağ merkezine yüklenmekte ve bu ağ’a, müşterinin kredi kartının teyidinden, firmanın envanter veri tabanından bilgi alma, faturalama ve sevkiyata kadar hemen hemen elektronik ticaret için gerekli bütün işlemleri yapabilecek otomasyonu kazandırmaktadır.

Benzeri bir başka yeni program ise dünyanın en büyük bilgisayar imalatçı firmalarından Intel ile Almanya’nın dev program üreticilerinden SAP arasında kurulan ortaklık olan Pandesic LLC’nin piyasaya sunduğu paket de 25 bin Dolar civarında bir fiyat etiketi taşımakta, firmanın envanter veritabanından bilgi almakta ve müşteriye sunmaktan, bankalarla işlemi tamamlamaya ve sevkiyatı hazırlamaya kadar hemen hemen bütün işlemlere imkan sağlamaktadır.

Ancak biz burada, Microsoft firmasının sunduğu paket programın uygulanmasını öneriyoruz. Microsoft, Internet’te ticaret imkanı veren yazılımı, NT ağlarını işleten Backoffice adlı paketine entegre etme yolunu seçmiş bulunuyor. Bu paketin 5 “client” bulunan bir ağ’ın Server merkezine konulmasının bedeli 3 bin Dolar civarındadır. Ağ’daki client bilgisayar sayısı arttıkça, bu fiyat da artmaktadır.

Ağ işletim sistemine entegrasyonu nedeniyle “tek sistem-tek çözüm” ilkesi çerçevesinde bakım-oranım ve kullanımın öğrenilmesi gibi cari harcamalarda tasarruf sağlayan Microsoft’un Internet’te ticaret stratejisini benimsiyoruz. Microsoft Site Server Enterprise Edition adlı bu paket, NT ağ işletim sisteminin bir parçası olarak (3 bin Dolar civarında satılan paketin içinde) edinilebileceği gibi, Commerce Server adıyla, sisteme daha sonradan da ilave edilebilir.

Microsoft firması, Internet’te ticareti kolaylaştıran ve belirli bir standarta bağlayan unsurları, Microsoft Windows işletim sistemine ve Microsoft Internet Explorer programına da yerleştirmektedir. Özellikle yeni piyasa sürülecek Windows 98 işletim sistemi Microsoft Wallet programını da içerecek ve bu sistemi kullananlara, ilave bir güvenlik sağlayacaktır. Bu program kullanıcılar tarafından şu anda bile Microsoft firmasının Web alanlarından ücretsiz edinilebilmektedir.

Microsoft’un Internet ticaret stratejisi üç parça üzerine inşa edilmiş bulunuyor:

Server Tabanı: Microsoft’un kullanıcılarla güvenli ve hızlı iletişim sağlamayı amaçlayan Web platformu, Active Server Pages teknolojisine dayanmakta ve firmanın Transaction Server programı ile bütünleşmektedir. Başka bir deyişle, Microsoft, NT ağına koyduğu güvenlik sistemini, Web ile ilişkileri ve Web dünyasında alış-verişi düzenleyen Server’ına da uygulamaktadır. Bu pakette firma ağ operatörünün, elektronik mağazayı kolaylıkla oluşturmasını sağlayacak yardım ekranları vardır. Programa yerleştirilmiş bir çok yardımcı program, firmanın Internet mağazasına reklam alınmasını ve bu reklamların müşterinin ilk tercihiyle birlikte “müşterinin zevkine uygun” şekilde sunulmasını sağlamaktadır. Yine Server’da yer alan sipariş işleme kolaylıkları, firma tarafından kendi muhasebe ve sevkiyat sisteminin gereklerine göre tanzim edilebilmektedir. Başka bir deyişle, Server, kendi kurallarını firmaya empoze etmek yerine, firmanın her türlü işleyiş özelliğine uygun hale getirilebilmektedir.

Ödeme: Microsoft firması Açık Ödeme Mimarisi adını verdiği sistem üzerine bina ettiği Microsoft Wallet programını, kullanıcının bilgisayarına yerleştirerek, ve arzu ettiği ödeme tarzını seçme işini bilgisayar kullanıcıya bırakarak, güvenliği artırmak istemektedir. Wallet mevcut gerçek-zamanlı ve yüzde 100 güvenli ödeme yöntemlerinden birini seçebileceği gibi, ilerde çıkacak yeni yöntemleri de benimseyebilir. Server, kullanıcının seçeceği her türlü sisteme açık ve Wallet’ın göndereceği onay kodunu kabule hazırdır. Bu sistem, firma, müşteri ve banka sistemi arasında ortak-işletim kolaylığı getirdiği gibi, müşteri açısından da firmayı kendisi ile banka arasındaki ilişkiden çıkarttığı için ayrıca ilave güvenlik duygusu kazandırmaktadır. Kullanıcı açısından firma sadece kredi kartının onaylandığı mesajını almakta ve dolayısıyla satıcı firmaya kredi durumuyla ilgili, alış-veriş açısından gerekli olmayan bilgileri vermemiş olmaktadır. Wallet programının özellikle Windows 98 işletim sistemi ile birlikte bu sistemi kullanan tüm bilgisayar sahiplerine verileceği düşünülürse, tüketici açısından standart hale gelmesi beklenmelidir.

Ticaret Ortakları Programı: Microsoft firması, Commerce Server sistemine daha geniş bir kabul kazandırmak için, özellikle ABD’de geçerli bir firmalar arası işbirliği ve dayanışma sistemine de öncülük etmekte, bu sistemden yararlanacak firmaların birbirleri ile işbirliğini arttırıcı çözümler önermektedir.

Microsoft’un entegre çözümü, bilgisayar kulanıcısına bugün Internet Explorer 4.0 ile yakında Windows 98 işletme ortamı ile, bu örnekte olduğu gibi, hızlı ve güvenli alış-veriş imkanı kazandıran Wallet ve Buy Now ek programlarını kazandırıyor. Bu iki program da Netscape firmasının Internet programı ile kullanılabilmektedir. Firma ise NT ağ işletim sisteminde mevcut Internet Information Server programına Internet Commerce Server programını ilave etmekle yetiniyor. Bu ekle, firmanın NT ağında Microsoft’un Commercial Internet System adını verdiği entegre sistem oluşmaktadır. Bu sistemin bir başka yan yararı, firmanın varsa Web alanını ve bu alanda yer alan sayfalarını, her ziyaretçinin özelliklerine göre kişiselleştirmesine imkan sağlamasıdır. Internet’te daha iyi ticaret anlamına gelebilecek Web sayfasının ziyaretçinin belirlenebilen veya bilinen özelliklerine göre kişiselleştirmek, bir ölçüde bu raporun kapsamı dışında kalmaktadır.

Özetlemek gerekirse,

-- gerek bugün mevcut (SMTP ve HTTP gibi) Internet ve ağ iletişim protokollerinin tümünü uygulamış olması, gerekse geliştirilmekte olan (XML ve EDI gibi) yeni bilgisayarlar arası veri alış-veriş protokol önerilerine açık olması,

-- elektronik alış-verişe sunulan mal ve hizmetlerin Web alanında temsilini son derece kolay ve çok az sayıda personelle sürdürülebilir hale getirmesi

nedeniyle, Microsoft Site Server 3.0 Commerce Edition, çok kısa süre içinde piyasa payını en hızlı artıran Internet’te ticaret yazılımı olmayı başarmış bulunuyor.

---
*Kaynak: `İNTERNET SİTESİ KURALIM/ekitap-Hakki_Ícal-Kitapcik_Internet_Sitesi_Kuralim.html`*
