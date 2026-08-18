# Ses Kartlarinda Bilmeniz Gerekenler

SES KARTINDA BİLMENİZ GEREKENLER

l WaveTable: Eskiden hemen tüm sistemlerde ve ucuz PC satacağım diye direnen satıcıların hala bile kullandıkları eski ses kartlarında, sayısal ses verilerini işlemeye yarayan bir FM syntesiser vardır. Taa 1970'lerin teknolojisi olan FM (Frequency Modulation) sonraları Yamaha tarafından geliştirilmiş ve ortaya FM OPL3 Synthesiser yongası çıkmıştı, çok uzun yıllar özellikle oyun dünyasının bir numaralı ses elemanı olan OPL3 o dönemde akustik ve elektronik enstrüman seslerinin maksimum alınabilmesi için en yaygın yoldu. Tabii bu hoşnutluk önemli oranda da beklentilerin kısıtlı olmasından kaynaklanıyordu. Zaman içerisinde özellikle oyunların gelişmesiyle yerini Wavetable Synthesis'e bıraktı. Wavetable, FM'in tersine ses yaratmak içim modülatörler filan kullanmıyor bunun yerine enstrümanların gerçek seslerinin kaydedilmiş örneklerini kullanıyor. ISA veri yolunu kullanan ses kartları bu örnekleri (samples) kendi ROM'larında saklarken, bu incelemede göreceğiniz gibi PCI yuvasını kullananlar sistem RAM'inin belli kısmını bu saklama işlemi için istiyorlar. Bu örneklemelerin boyutları ne denli büyük olursa elde edilecek ses de o denli kaliteli olacaktır. Eminim şimdi bir çoğunuz Wavetable'ı daha etkin kullanmak için nasıl bellek arttıracağını aradığı günleri düşünmüştür. ISA kartların önemli dezavantajlarından biri de işte bu bellek sorunu. Hatta daha çok ses saklanabilmesini sağlayan Wavetable daughterboard (ek wavetable kartı) bağlantılarının hemen her 16 bit kart üzerinde bulunmasının sebebi de bu.

l DSP: Kartın ses üreticisi aslında DSP (Digital Signal Processor), yani sayısal sinyal işlemcisidir. DSP ne yapar? DSP, gerekli notaları wavetable belleğin değişik bölgelerinden değişik hızlarda okuyarak müziğin ya da sesin ortaya çıkmasını sağlar. Bu DSP'nin işleme gücüne göre aynı anda çalabileceği maksimum ses sayısı da kartın Polyphony'si olarak tanımlanır. Hani ses kartlarının sonunda 32, 64 hatta 128 gibi eklentiler görüyoruz ya işte bu o sayı aslında o kartın polyphony'sidir. Örneğin SoundBlaster PCI64 kartı, sanılanın ve yagın kanaatin aksine 64 bit veri işlemez, 64 sesi aynı anda verebilme kapasitesinde bir kart olduğu ifade edilmek için sonuna 64 ibaresi eklenmiştir.

l MIDI: Her ne kadar PC'de MIDI dosyalar dinlemek artık iyiden iyiye popülaritesini kaybetse de MIDI (Musical Instrument Digital Interface) her ses kartının vazgeçilemez bir öğesi, enstrümanların kendi aralarında anlaşabilmelerini sağlayan bir standarttır. Bugün hemen her ses kartının joystick bağlantısından MIDI aygıtları bağlanabilmekte. Testimizde de bunun klavyeli bir örneğini göreceksiniz, gerçi ilk başta biz bir MIDI gitar kullanmayı düşünmüştük ama sonradan klavyenin daha uygun olacağını düşünerek vazgeçtik. Anlatmaya kalksak sayfalar alacak MIDI konusuna ilişkin bilmeniz gereken bir şey daha var; General MIDI kavramı. MIDI ilk icat olduğunda müzisyenler ellerinde hangi MIDI enstrüman varsa onunla bir takım arajmanlar yapıyordu, ancak iş başka synthesiserda dinlemeye gelince aynı sesler alınamıyordu. Çünkü her synth yapımcısı enstrümalara kafasına göre program numarası veriyordu, böylece orjinali piyano olarak kaydedilen bir ses, bir başka synth'de sözgelimi klarnet olarak duyuluyordu. İşin uzmanları bunu da bir standarta bağlayıp bir enstrüman haritası çıkardılar, adını da General MIDI koydular. Ses kartının kalitesindeki önemli etkenlerden biri de işte bu General MIDI enstrümanlarını orjinaline ne denli yakın çalabildiği.

l Veri yolu: Neden PCI? Yukarıda ISA'nın yerine PCI kullanılmasının önemli sebeplerinden biri olarak PCI ses kartlarının Wavetable için sistem belleğini kullanmasını göstermiştik. Aslına bakılacak olursa çok daha önemli bir neden daha var, o da bant genişliği. ISA veri yolu teorik olarak maksimum 8 Mbps (saniyede 8 Mb) veri aktarabilirken bu rakam PCI'da 132 MBps'a yükseliyor. Doğal olarak ISA'nın sadece 16 kanal kapasitesi de ortadan kalkmış oluyor. Bugünün 32 hatta 64 kanal kullanabilen uygulamaları göz önüne alındığında PCI veri yolunu kullanan ses kartlarının farklılığı da ortaya çıkmış oluyor. Haliyle veri hızı bu denli yüksek olunca da 3 boyutlu ses ya da çoklu kaynaklardan gelen ses verilerini işlemek gibi gelişmiş özellikler de rahatlıkla kullanılabiliyor. 44.1 kHz (CD kalitesi) bir sample çalmak için ana işlemcinin yüzde 20 gücünü işgal eden ISA nerde, neredeyse hiç kullanmayan yeni nesil PCI ses kartları nerede? Yakın geçmişte daha hızlı oyun oynayabilmek için sesleri kapatmak zorunda kaldığımız günleri düşündükçe insan gerçekten ne kadar ilkel bir evre geçirdiğimizi düşünmeden edemiyor doğrusu.

l Dijital Ses Nedir?: Hemen bir örnekle açıklayalım da akılda kalıcı olsun. CD-ROM'unuzda müzik CD'leri çalabilmek için bildiğiniz gibi sürücünün arkasındaki analog line çıkışından ses kartının üzerindeki line girişine bir bağlantı yapılır. İşte bu bağlantı analog olduğundan dolayı dış dünya etkilerine, mesela PC'nizin güç kaynağı etkilerine açıktır. Bu sebepten (anten gibi davranan bağlantı yüzünden) sinyal kaybı ya da acayip sesler olasıdır. Dijital (sayısal) bağlantı kullandığınız takdirde ise dış etkilerden etkilenmezsiniz, çünkü veriler sayısal ortamda akıp gitmektedir. Günümüzde özellikle temiz kayıt isteyenlerin kullandığı dijital bağlantının en önemli öğesi SPDIF çıkışı/girişidir.

l Öyleyse S/PDIF Nedir?: Spee-deef olarak teleffuz edilen SPDIF'in açılımı Sony/Philips Digital Interface'dir. Philips ve Sony tarafından geliştirilen bu arabirim ile CD player, DAT gibi kaynaklardan sayısal veri aktarımı kayıpsız yapılabilir. Bu kayıpsız veri aktarımı sayesinde de özellikle DVD gibi dijital ses barındıran medyalardan daha iyi sonuç alınabilir.

l TAD: Kimi ses kartlarının üzerinde TAD girişi bulunur. TAD'ın anlamı Telephone Answering Device'dır. Voice özellikli dahili modemlerin çoğunda bu bağlantıyı gerçekleştirebilirsiniz.

l AUX: Yine ses kartlarında bulunan bir giriş. Aslında passthrough demek daha doğru, çünkü kendisi üzerinden MPEG, TV ya da radyo kartlarının sesi iletilebiliyor.

3 BOYUTLU SES NEDİR? İLGİLİ TEKNOLOJİLER NELERDİR?

Herkesin çok net bildiği gibi insanoğlunun iki adet kulağı var. Bu kulaklar sayesinde etrafımızı çevreleyen 3 boyutlu ortam içerisinde sesin ne yönden geldiğini anlayabiliyoruz. Madem ki gerçek dünyada sadece iki kulakla 3 boyutlu duyabiliyoruz, 2 ya da daha çok adet hoparlör ile ya da bir kulaklık ile de aynı etkiyi almamız mümkün olabilir. Bu 3D sesi ortaya koyabilmenin 3 farklı yöntemi var. Birincisi stereo expansion adı verilen yöntem, örneğin 3D özelliği olmayan bir müzik parçasına bu etkiyi verebilen özel bazı teknikler var. Kimi müzik setlerinde ya da hoparlörlerde görmüşsünüzdür, bir düğmeye basarsınız veya yazılım ile ayarlarsınız ve daha değişik bir etki alırsınız dinlediğiniz müzikten. Anlaşıldığı gibi burada kaynağın 3D ses barındırması gerekmez. Buna benzeyen diğer bir teknik de Virtual Surround, yani sanal çevreleme. Bu tenikte de 3D sonradan eklenir, örneğin şu ünlü Philips surround Sound reklamında gördüğümüz cihazlar bu tür bir etki yaratmak üzere tasarlanmışlardır.

3D ses alabilmenin üçüncü ve bizi ses kartları açısından ele alındığında en çok ilgilendiren yolu Positional 3D Audio olarak ortaya konabilir. Burada birden fazla ses 3 boyutlu ortamda birbirinden farklı yerlerde konumlandırılmaya çalışılır, böylece 3D etkisi oluşur. Örneğin bir filmde görünürde uçak olmamasına karşın önce arkanızdan yaklaştığını duyabilmeniz, sesin giderek yaklaşması ve derken üzerinizden geçip giderken sesin kaynağını konumlandırabilmeniz hep bu sayede olur. Aklınız karışmasın örneğin sinemalarda gördüğümüz Dolby Digital ses sistemleri de aslında birer Positional 3D Audio'dur, sadece hoparlör sayısı çok daha fazla olduğundan dolayı çok fazla sayıdaki ayrı ses, ayrı ayrı pozisyonlandırılabilir, üstelik bu işlemler özel bir kodlama ile gerçekleştirildiğinden veri kaybı da söz konusu değildir. Biz denemelerimizde Cambridge SoundWorks Desktop Theater 5.1 ile ses kartlarının hem oyunlarda hem de filmlerde bu özelliklerini denedik, aynı denemeleri 4 hoparlöre izin vermeyen kartlarda ise Yamaha YST-M100 hoparlör seti ve YST-MSW5 subwoofer karışımı ile denedik. Doğrusunu söylemek gerekirse 4 hoparlör gibisi yok, evet 2'li hoparlör setlerinde de 3 boyut etkisi hissedilebiliyor, ama çoklu hoparlör setleri ile deneyim olarak çok farklı etkiler bırakıyor.

Yazımızın girişinde de söylemiştik. Neredeyse her kart firması kafasına göre bir 3D teknolojisi kullanıyor. Dolayısıyla bu teknolojilerin en sık kullanıldığı mekan olan oyunlarda hangi teknolojiyi destekleyeceğini şaşırmış durumdalar. Durum tıpkı grafik dünyasındaki OpenGL, Direct3D ve Glide arasında yaşanan API çekişmesine benziyor. Burada API tanımını net bir şekilde yapalım daha sonra kafanız karışmasın: 3D ses API'si aslında sadece 3D sesi size iletmek isteyen programcının kullandığı ve sesin 3 boyutlu uzayda hangi konumdan ve hangi şiddette geleceğini ses kartına söylemesine yarayan komutlar topluluğudur. Biz sizin için 3D ses destekleyen oyunların hangi teknolojileri kullandığını gösteren bir tablo yaptık, umarız ilginizi çeker. Herneyse biz şimdi kısaca bu teknolojilerin (ya da API'lerin) hepsine biraz göz atalım, bir ses kartının birden fazla API kullanabileceğini ve bir oyunun da birden fazla API için yazılmış olabileceğini hatırlattıktan sonra da testimize geçelim. Eğer bu API'lerden hangisinin daha başarılı da ayrıca olduklarını merak ediyorsanız Mart 99 sayımızı okumanızı tavsiye ederiz.

l DirectSound3D: Microsoft'un geliştirdiği Direct Sound 3D, aslında DirectX'in bir parçası. Bu sebepten DirectX destekli her yeni PCI ses kartı tarafından rahatlıkla kullanılabiliyor, bu yagınlık sayesinde de en sık karşımıza çıkan 3D ses API'si. Oyun programcılarının da kolayına geldiği için çoğu yeni oyunda kullanılabilir olması gerek. Zaten kullanılabiliyor da ancak çok fazla tercih edildiği söylenemez, nedenine gelince programcıya sunduğu imkanlar bugünün oyunlarında kısıtlı. Bu kısıtlı ortamdan sıyrılmak isteyen ilk firma Aureal oldu ve DirectX 3 ile birlikte çalışmalarına başlayarak A3D'yi ortaya koydu.

l A3D: Modern ses kartlarında en sık rastlayacağınız 3D API'si olan A3D, ana işlemciye fazla yüklenmemesi ile dikkat çekiyor. Donanımdan 3D ses hızlandırılması olayının atası sayılabilicek A3D, aslında Direct Sound3D komutlarını kendi algoritmleri ile kullanıyor, biraz karışık ama bu kadarını bilmeniz yeterli. Asıl tereddüte düşebileceğiniz nokta ise bu A3D'yi kullanan kartların çeşitleri. Bunlardan birincisi emülatörler, oyundan gelen A3D bilgilerini alarak sahte bir A3D.dll dosyası ile DirectSound3D altında işliyorlar, yani bir anlamda oyunu kandırıyorlar. Creative'in Sound Blaster Live ses kartı bunun güzel bir örneği. A3D kullanan ikinci tür kartlar DSP tabanlı ürünler. Bunlarda programlanabilir bir DSP işlemcisi var, bu generic işlemci üzerine A3D'nin algoritmaları işleniyor böylece A3D donanım hızlandırıcılı bir ses kartınız oluyor. Bu tip kartların 3D ses başarısı tamamen sözünü ettiğimiz DSP'nin kapasitesi ile doğru orantılı. Son olarak A3D kategorisinde karşımız Vortex 1 ve Voretx 2 yongaları çıkıyor. Vortex 1, 8 adet 3D, 8 adet de 2D ses işleyebiliyor, en gelişmiş A3D kullanıcısı Vortex 2'de ise imkanlar ve kalite çok daha geniş. Nitekim testimizin gözdelerinden Diamond MX-300 de bu yongayı kullanmakta.

l EAX: EAX'ın açılımı Environmental Audio Extensions. Creative tarafından geliştirilen bu API'ye geçmeden önce reverb kavramına biraz değinmemiz gerekli. Duyduğumuz sesler iki bileşenden meydana geliyor; orjinal kaynaktan yola çıkan ses ve bu sesin kulağımıza ulaşıncaya dek çevreden aldığı etkiler. Örneğin duvarlar, etrafımızdaki insanlar ya da diğer objeler seste bir deformasyona yol açar. İçinde bulunduğumuz oda ya da ortamın şekli, içerdiği materyallerin büyüklüğü ve çeşidinin yarattığı etki reverb olarak tanımlanır. İşte Creative'de bu yüzden API'sine çevresel ses anlamına gelen Enviromental Audio adını koymuş. Creative'in yapmak istediği şu: Programcıya içinde hazır çevresel efektler bulunan bir reverb motoru sunuyor ve "al bunu oyuncunun 3D ortamı hissetmesi için hangisi uygun geliyorsa kullan" diyor. EAX'da aslında bir DirectSound3D uzantısı, yani o da tıpkı A3D gibi DS3D komutlarını kullanıyor ama kendi algortitmaları ile.

l Q3D: Qsound firmasının bir ürünü olan Q3D henüz pek yaygın olarak kullanılmıyor. Testimizde Aztech'in 368DSP ses kartında gördüğümüz Thunderbird yongasının yanı sıra Sega'nın Dreamcast yongası ile Trident 4Dwave-DX'i de Q3D kullanıcılarından. Amacı diğerlerinde olduğu gibi sadece 2 hoparlör aracılığı ile 3D ses ortamı yaratmak. Programcı firmanın iddiasına göre aslında kulaklık üzerinde çalışmak üzere geliştirilmiş olan Head Related Transfer Functions (HRTF), 2 hoparlör üzerinde doğru çalışmıyor ve kayıplara yol açıyor. Bu yüzden Q3D bu tekniğin yanı sıra çapraz konuşma (cross talk) adı verdiği bir tekniği de kaynaştırmış. Tıpkı diğer API'lerde olduğu gibi Q3D'nin de 2.0'ı tamamlanmış bile. Anlayabildiğimiz kadarıyla anormal detayları olan Q3D büyük iddialar taşıyor, ancak henüz uygulama bazında belirgin bir farkını göremediğimizi belirtmek gerek. Sanırız ileride daha fazla etkisini hissettirecektir.

Unutmadan belirtelin Q3D, DVD kullanımı için Qsurround adını verdiği yeni bir teknoloji de kullanıyor. Buna göre AC-3 (ya da herkesin bildiği adıyla Dolby Digital 5.1) kodlarını çözebilen bir yazılım kullanıldığında Q3D kartlar ile film seyredilebiliyor. Aslında bunu hemen her API yapabiliyor, örneğin Vortex2 yongasına sahip Diamond MX300'de A3D API'sini kullanarak bu sinyalleri çözebiliyor. Yani açıkçası soru bu işi ne kadar kaliteli yapabildiğinde.

l Sensaura: Yamaha'nın bu teknolojiyi kullanmaya başlaması ile adını duyuran Sensaura, temelde diğer API'ler ile büyük farklılıklar taşımıyor. Yukarıda bahsettiğimiz HRTF olayına yeni bir boyut kazandıracak olan ve bir metreden yakın mesafelerde de iyi sonuçlar vermek üzere tasarlanan MacroFX ile, yakınlaşan objelerin dinleyiciye yaklaştıkça farklı sesler de verebilmesini sağlayan ZoomFX (trenin yaklaştıkça duyulabilecek seslerinin de -örneğin tekerlek ya da ray sesi- aktarılabilmesi) özellikleri Sensaura'nın öne çıkan yeni teknolojileri.

SONUÇ OLARAK

3D ses özellikli her ses kartı kullandığı API ne olursa olsun (ister Q3D ister A3D ya da EAX) kendiliğinden DirectSound3D uyumlu hale gelir. Bir örnekle açıklayacak olursak DS3D programlanan oyun çalıştırıldığında sistemde ses için bir 3D donanımı arayacak ve bulduğunu kullanacaktır, bu sebepten herhangi bir 3D ses kartında temel 3D konumlandırmalarını gerçekleştirecektir. Sonuç olarak 3D ses kartlarının verdikleri sesin 3D kalitesinde tüm bu saydığımız API'lerin DS3D'yi nasıl kullandıkları belirleyici olarak karşımıza çıkıyor.

| PRIVATE**SES KARTLARI (1 YIL GARANTİ)****** | **USD****** |
| --- | --- |
| **64 BIT 3D 4 CHANNEL****** | **14****** |
| **64 BIT 3D 6CHANNEL WIN DVD SOFTWARE****** | **19****** |
| **64 BIT WINFAST 4 CHANNEL (DIGITAL OUT)****** | **22****** |
| **CREATIVE SOUND BLASTER 128 BIT VIBRA PCI JOY. PORT****** | **15****** |
| **CREATIVE SOUND BLASTER LIVE 5.1 BOX****** | **49****** |
| **AUDIGY DIGITAL ****** | **94****** |

| PRIVATE**AUDIGY PLATUS INTERNAL (Uzaktan Kumandalı)****** | **179****** |
| --- | --- |
| **AUDIGY PLATUS EXTERNAL****** | **229****** |

## **CAMERA**

## **CAMERA******

## **CAMERA******

## **CAMERA******

**INTEL EASY WEBCAM CAMERA**

## **47******

**INTEL QX3 MİKROSKOP**

**61** **CREATIVE WEBCAM GO MINI (DIGITAL CAMERA)**

**75** **CREATIVE WWBCAM GO PC 300**

## **155******

**INTEL POCKET PC (DIGITAL PHOTOGRAPH 8MB USB)**

## **118******

## **SPEAKERS (1 YIL GARANTİLİ)**

**USD** **SPEAKERS 300 WATT** **6** **DIANA KA-10T 280WATT**** ****8** **DIANA KA-653C 400 WATT** **13** **PEGASUS PS1200 FAST POINT 780 WATT**** ****43** **PEGASUS 800 WATT AHŞAP** **62** **PEGASUS XPOWER 5.1 1200 WATT** **75** **CREATIVE FPS-1000 4x7W RMS+ 10W RMS** **57** **CREATIVE FPS-1500 4x6W RMS+ 17W RMS** **67** **CREATIVE DTT 2200D AC-3, 5.1 DOLBY DIGITAL** **124** **CREATIVE DTT 3500 AC-3, 5.1 DOLBY DIGITAL** **291** **CREATIVE INSPIRE 4400 4+1** **64** **CREATIVE INSPERE 5300 5+1** **119** **JAZZ J9902 5+1 SURROUND** **60** **JAZZ 800W J7907 4+1** **37******

PRIVATEBAS, TİZ, FREKANS NEDİR?

Bas nedir? Tiz nedir? İki yollu-üç yollu kolon neyi ifade eder? Tweeter-woofer-subwoofer nedir? "Ben bu işin kitabını yazdım. Arabada ne tesisat var, sen biliyon mu?" diyen arkadaşlar bile, bu kısmı okumalı. Sesler bilindiği üzere frekanslara ayrılır. Şu setlerin üzerinde gördüğünüz hani 50 veya 60’lardan başlayıp yükselerek Hz cinsinden frekansı gösteren ayarlar var ya, işte onlar bu frekans aralıklarını ifade eder. Hani şu 10 Band veya 8 Band Graphics Equalizer dediğimiz ayarlar aslında isteğimiz doğrultusunda bize bas tiz ayarı yaptırır.

Hz’den KHz’e doğru ses tizleşir. İnsanlar belirli frekans aralıklarını duyabilirler. Köpekler insanlardan daha fazla frekans aralığına sahip sesleri duyabilirler. Şu bildiğimiz, sadece köpeklerin duyabildikleri düdükler gibi. Hoparlörler de bu frekans aralıklarını doğal olarak ayrıştırırlar. Küçük çaptaki hoparlörler tiz sesleri, büyük çaptaki hoparlörler bas sesleri verirler. Bir kolon üzerinde gördüğünüz küçükten büyüğe sıralanan hoparlörler tizden basa kadar sesleri ayrıştırır. Sırf tiz sesleri verebilen küçük çaplı hoparlörlere "TWEETER"; alçak frekanslı yani bas sesleri verebilen geniş çaplı hoparlörlere de "WOOFER" denir. Bir kolon üzerinde birkaç hoparlör görüyorsanız bu hoparlörler çok yolludur.

Küçük çaptan büyük çaplı hoparlöre doğru, tizden basa doğru sesi ayrıştırır. Çok yollu hoparlörün amacı tiz ile bası tek hoparlör üzerinden alıp daha iyi ayrıştırarak, yani görevi dağıtarak her frekanstan sesi daha net duyabilmenizi sağlamaktır. Hatta bazı orta ve üst kalite kolonlarda fiyat ve marka ile doğru orantılı olarak bu frekansları mevcut hoparlörlere frekanslarına göre ayırıp da yollayan devreler bile mevcuttur.

NEDİR ŞU 300, 500,

3000 WATT SAÇMALIĞI?

Sokaklarda veya Amerikan filmlerindeki gençlerde birer teyp görürsünüz: "Hey moruk çektim teybi". Alacalı bulacalı, üzerinde yazar 1000 WATT. Bilgisayar dükkanlarına girersiniz ve görürsünüz: 600W. Yok devenin bale pabuçları. Nezih ve çok pahalı bir markanın kolonunun arkasını çevirisiniz; 60, bilemediniz 80 WATT yazar. Üstelikte derinden, o 600W’lık kolondan kat kat kuvvetli ancak insanı rahatsız etmeyen, okşayan bir ses veriyor. Nedir işin sırrı? Arkadaşlar iki ayrı birimden konuşuyor. Biri RMS, yani Gerçek Müzik Çıkışı; diğeri ise PMPO, Maksimum Müzik Çıkışı. Geçerli olan RMS’dir. Biri 60 W derken, diğerleri, hatta saygın markalar bile, alt kesime hitap eden ürünlerine insanı çekmek, "Benim kolonlarım 600 WATT" diyebilmek için, PMPO cinsinden birim atmaktadırlar. Ancak hiçbir orta seviye ve üstü müzik sisteminde bu ibareyi fosforlu mor üstüne sarı puntolarla göremezsiniz. Artık kanmayalım ve yavaş yavaş kutuların üzerinde küçük harflerle yazılmış parantez içinde RMS yazan birimi okuyup değerlendirelim. Böylece hem tekliflere daha bilinçli yaklaşmış oluruz hem de "Kolonlar 600W olsun!" deyip komik duruma düşmemiş oluruz.

NEDİR ŞU DOLBY ve TÜREVLERİ?

Dolby Surround Sound nedir? Dolby Pro Logic nedir? Dolby Digital nedir? Müzik setlerinin üzerinde Dolby B-C NR; film afişlerinde Dolby Surround Sound, Dolby Pro Logic, Dolby Digital ibarelerini görüyoruz. Nedir bunlar yenir mi? Bir de başımıza DVD çıktı. DVD’lerin üzerinden de eksilmiyor meret.

Dolby bir teknoloji kuruluşudur. Ses teknolojilerini üretip standartlarını koyar. İlk başlarda ses gürültülerini hışırtılarını ayrıştırıp temizleme amaçlı olarak müzik setleri üzerinde gördüğümüz Dolby B veya Dolby C gibi özelliklerle karşılaştığımız bu firma daha çok film endüstrisi için ses teknolojileri üretiyor.

Önce "mono" vardı. Taş devrinin ardından "Stereo" geldi. Yetmedi, sesin bizi çevrelemesi gerekiyordu. Arkaya iki veya salonun büyüklüğüne göre ikinin katları olarak "Surround" "Çevreleyen" hoparlörler koydular ve sesi ayrıştırarak belli frekanstan seslerin arka kolonlardan dönmesini sağladılar. Tabii aslında çok basit bir tarifle anlattığımız bu olaya "Dolby Surround Sound" dediler.

Bu da yetmedi; sesi daha iyi ayrıştırarak ön konuşmaları arka seslerden ayırdılar bir orta kolon koydular. Oldu size "DOLBY PRO LOGIC"

Şekil 1 ve 2’de göreceğiniz üzere ev ve sinema tipi sistemlerde iki ön kolon, bir orta kolon ve arkayı sarmalayan "Surround" kolonları görüyorsunuz. Bunların amfileri bir nevi ayrıştırıcı görevi görerek, tek kanaldan gelen sesi frekanslarına ayırarak bunu dağıttılar. Şu ana kadar gelen ses bildiğimiz analog kablo üzerinden gelen sesti. Bu da, azmış kudurmuş teknolojiye yetmedi tabii... Sesi çeşitli yönlere kaydedici cihazlar koyarak 5 kanaldan, ayrı ayrı kaydettiler. Bunu bildiğimiz 0 ve 1’ler ile kodlayarak sayısal olarak işlediler. Ve filmlere yerleştirdiler. Yani bu sistemin amfileri bildiğimiz iki telli kablo üzerinden ses olarak değil, sayısal olarak alıyor ve "hımmm bu ses arka kamyondan geliyor" diyerek arka iki kolondan kamyon geçiriyor. "Ön sağda kadın çığlık atıyor" diyerek ön sağ kolona o kanaldan gelen sesi yönlendiriyor. Üstüne üstlük bir de insanın tüm organlarını gıdıklayan şu doygun bas sesi ayrıştırıp daha önce anlattığımız ve "LFE - Low Frequency Effects" diye şemalarda göreceğiniz ‘Subwoofer’a veriyor. Yani her kolonu tek tek yönetiyor. Ve işte size ünlü "Dolby Digital". Sıfır ses kaybı; çünkü sesler CD’deki gibi sayısal olarak kaydedilmiş. Tamamen sesler kendi kaynaklarında kaydedildiğinden yönleri tam ayrıştırılmış ve gerçekçi.

Yan kutudaki şemalarda göreceğiniz üzere, 2 ön kolon, arka sağ ve arka sol olmak üzere 2 arka çevreleyen kolon, 1 orta kolon; ediyor 5. Bir de Bas sesleri veren Subwoofer; ediyor 5+1 "Dolby Digital". Tabii sinemada arka kolonları yayıyorsunuz. 250 koltuklu bir sinema ile bizim salon aynı olmuyor tabii.

Yetti mi? Olur mu? Şimdi de niyeti bozup, iki ön kolonun yukarılarında iki noktaya, iki ayrı kolon daha koyarak 7+1’e soyundular. Yakında sinemalar küre bir kolonun içinde olacak, biz de içine oturacağız herhalde.

BİLGİSAYAR CEPHESİNDE DURUM NASIL?

Artık bilgisayar ile "Home Theatre", yani Ev Sineması dediğimiz sistemler neredeyse iç içe geçti. Bir Dolby PRO Logic veya kesenize göre bir Dolby Digital amfi ile, 5+1 kolon seti alıp DVD-ROM ve DVD çözücü kartınızdan doğrudan televizyona ve bu amfiye çıkış yapabiliyorsunuz. Bu amfiyi TV ile, bilgisayar ile, müzik seti ile ortak paylaştırabiliyorsunuz. Ev Sineması ortamında muazzam zevkli Quake II veya Unreal oynayabiliyorsunuz. Çünkü sistem geriye de uyumlu.

Sirkeci’de yaptığımız bir araştırmada, 5+1 ve 7+1 sistemlerin oldukça tuzlu olduğunu öğrendik. Dolby PRO Logic sistemler ise nispeten daha ucuzdu.

Ev Sineması ile ilgili fiyat ve dokümanları sağlayan FORUM HOME CINEMA’dan Ender Alkan Bey’e teşekkür ederiz.

Peki daha basit ve ucuz , sırf bilgisayar için bu işin çözümü yok mu? Testimizde inceleyeceğimiz Cambridge Soundworks Desktop Theatre 5.1 – Dolby Digital sistemde ve Eastern DA-9000 Home Theatre - Dolby Pro Logic sistemde bu konuya el atıyoruz.

BİLGİSAYARDA ÜÇ BOYUTLU

VE KONUMSAL SES

Bildiğiniz üzere Sound Blaster Live!, 4 kolon teknolojisini oyunlara ve masaüstüne taşıdı. Yukarıdaki sistemlerle karşılaştırılamaz ancak şu konum ve ses meselesini, arkadan gelen patlama sesinin arka konumdan gelmesini oyun ve uygulamalar içine sokan önemli bir noktadır. İki ayrı çıkışla ön ve arka kolonlara ayrı sesleri yollayarak oyuna bir derinlik ve tat getirmiştir. Bu sistemle bir takım oluşturması düşünülen PCWorks Four Point Surround’u da testimizde tartışacağız.

NASIL TEST ETTİK?

Doğrusu ilk bu teste giriştiğimizde 31 parça malzeme geleceğini bizde beklemiyorduk. Gelen malzemeyi 4 ayrı kategoriye ayırmak zorunda kaldık.

1. Hoparlörler: Birer çift olarak gelen hoparlör sistemleri.

2. Subwoofer’lar: Giriş konusunda anlattığımız gibi düşük frekansları, yani bas sesleri veren ve hoparlörlere ek olarak bas lezzetini ayırabileceğiniz subwoofer sistemleri.

3. Sistemler: Bir çift kolon ve subwoofer ile birlikte gelen sistemler.

4. 4 Kolon/Dolby Pro Logic ve Dolby Digital Sistemler.

Değerlendirme yaparken bir müzik otoritesi olmadığımızı ve o ünlü Hi-Fi dergilerindeki gibi bir kolona sekiz sayfa ayırarak osiloskop cihazlarıyla tüm kolonlara saldıramayacağımızı bildiğimizden, üç tip test uyguladık. Büyük bir iş hanında bulunan test merkezimizde, gece yeri göğü inleterek yaptığımız testler şöyleydi:

1. Frekans Aralığı Testi: Yamaha’nın insanın duyabileceği tüm frekans aralığındaki sesleri bir kolonun verip veremeyeceğini test edebilen bir yazılımı kullandık. Yazılımı ve kullandığımız YAMAHA XG PCI ses kartını bize sağlayan ve konu ile ilgili bizden bilgilerini esirgemeyen Sky Bilgisayar’dan Mansur Karakoç ve Fırat Güneyi Beylere teşekkür ederiz.

2. Bas Testi: İki kişi ayrı ayrı sistemde Eurythmics’in ünlü bas çatlatan parçalarından birini kullanarak kolonların veya subwoofer’ların seslerinin çatlayıp çatlamadığını, ses kalitesini ve kasaların zangırdayıp zangırdamadığını test ettik.

3. Ses Ayırım Testi: İki kişi, ayrı ayrı basları her sistemde aynı seviyede tutarak, Quake II’nin ilk bölümündeki giriş sahnesinde, arka planda CD müziği çalarak oyundaki camları patlattık. Bu esnada sesi berrak olarak ayırdedip edemediğimizi, bas ve tiz seslerin ayrı ayrı ve düzgün gelip gelmediğini dinledik. Sesi çok açtığımızda seslerin net gelip gelmediğini inceledik.

4. Manyetik Alan Testi: Kolon ve sistemlerde masa üzerinde olması gereken parçaların ekrana yaklaştırıldığında ekranda titremeye, daha kötüsü renk çekilmesine sebep olup olmadığı denendi. Eğer ekranlarınızda sürekli bir dalgalanma varsa bir de kolonları fişten çekerek (kapatarak değil!) denemenizde fayda var. Bu tip problemlerin %80’i bu tip sorunlardan kaynaklanıyordur. Özellikle adaptörsüz doğrudan elektriğe bağlanan hoparlörlerde bu tip sorunlara rastlanıyor.

5. Özellikler: Subwoofer olup olmadığı, kulaklık takılabilme; bas/tiz ayarları, sese derinlik veren Surround, 3D gibi özellikler, ayrıntılı kullanım kılavuzları, ikinci bir ses aygıtı bağlanabilme gibi özellikler değerlendirildi.

İki kişi ayrı incelememize rağmen, yaptığımız sıralamalarda pek bir fark olmadı. Aşağıda, test ettiğimiz ses sistemlerini, her bir kategoride en çok puan alandan daha az puan alana göre sıraladık.

JBL MEDIA 3

Dünyanın en tanınmış konusunda en üstün üreticilerinden biri olan JBL, 2x14 W’lık kolonlarıyla diğerlerine fark atıyor. Ancak Yamaha YST-M100 ile karşılaştırırken çok zorlandık. Yamaha’nın ses kalitesi JBL’i özellikle bas seslerde bastırıyordu. Ancak manyetik alan testinde Yamaha ekranı titretince, en yakın rakibi ipi göğüsledi. 99$ + KDV son kullanıcı fiyatı ile de çekici hale gelen bu kolonda tek kusur sesi çok açtığımızda hafif bir "hıss" vermesi. Tüm kolonlar içinde en net bas/tiz ayırımını bu kolonda hissettik. Ayrıntılı kullanım kılavuzu, ek bir ses aygıtı bağlanabilme ve Subwoofer çıkışlarıyla gerekli tüm özellikleri sağlıyor. Internet sitesinde rastladığımız modelleri çok daha yeni idi. Umarız yeni modelleri yakın zamanda ülkemizde görebiliriz.

À YAMAHA YST-M100

Tek kolon olarak en tok ve en net sesleri bu konusunda en iddialı üründen elde ettik. Tahta kasasıyla , sese derinlik veren Ymersion 3D Enhance teknolojisiyle neredeyse subwoofer’a hiç ihtiyaç duymazmış gibi verdiği bas sesleri ile, eksiksiz gelen kullanım kitapçıkları ve kablolarıyla, ek bir ses aygıtı bağlanabilme ve Subwoofer çıkışlarıyla gerçekten masaüstünde neredeyse orta bir müzik seti kalitesinde ses alabiliyorsunuz. Bir de ekran yanına koyduğumuzda titretme yapmasaydı, sonuna kadar bizim favorimizdi. Öğrendiğimize göre bu kolonlar 5-6 saat gibi uzun süreler ses tam açık çalıştırıldığında sistemin arızalanmasını önlemek için devreyi kesiyorlar. Oldukça önemli bir özellik. Kalitesi ağırlığından da anlaşılıyor; öyle iki parmakla kaldırabileceğiniz kolanlardan değil, biraz ağırca. En önemli kusuru - ki kadı kızında bile olur - 147$ + KDV son kullanıcı fiyatı.

Ã PHILIPS DSS 350

Dynamic Bass Boost – Incredible Surround Sound gibi yakışıklı isimlere sahip teknolojileri barındıran bu sistem teste katılan USB destekleyen iki sistemden biri. USB sistemlerde sesi düğmeden kapadığınızda sistemden de eşzamanlı olarak kısıyor. Ancak normalde sırf ses kartından çıkış aldığınızda düğme ile sesi kontrol edebilmeniz gerekirken ne yazık ki burada düğmeden etki edemiyorsunuz. USB yazılımları ile birlikte gelen sistemi USB yuvanız olmadan da bağlıyabiliyorsunuz; ancak o zaman düğmeden değil sadece sistemden sese müdahale edebiliyorsunuz. USB yuvanız var ise ses kartınız olmadan bile bu USB sistemi ile ses alabiliyorsunuz ve CD-ROM’unuz destekliyor ise ses kartı olmadan da kolonlardan CD müziği dinleyebiliyorsunuz. Testimizde yine en lezzetli baslardan birini bu sistemde aldık ancak basları kıstığımızda bile tiz sesleri tam alamadık. Yine de gerçekten güzel ses verdiğini kabul etmemiz gerekli. Piyasada pek de iyi ses vermeyen ve kalite olarak bizi üzen diğer Philips kolonlarla karıştırılmamalı. Ne yazık ki fiyat olarak oldukça yukarılarda: 173$+KDV son kullanıcı fiyatına sahip. Ancak sisteminiz USB ise ses kartı fiyatından biraz kurtarabilir. Subwoofer çıkışı var ancak pek de ihtiyaç duymuyor. Manyetik alan testini de başarıyla geçti.

Õ YAMAHA YST-M20

Kaliteli Yamaha serisinin bu üyesinde de yine derinlik veren Digital Surround Processing özelliği var. Bas/tiz ayarı yerine tek bir Tone düğmesi bulunan sistemde ayrıntılı kullanım kılavuzu, ek bir ses aygıtı bağlanabilme ve Subwoofer ve kulaklık çıkışlarıyla gerekli özellikleri sağlıyor. Eurythmics parçasında ve Quake’te M15 modelinden daha iyi bas vurduğunu hissettik.

Œ YAMAHA YST-M15

YAMAHA YST-M20 in tüm işlevsel özelliklerini barındıran sistemde fark olarak DSP özelliği yok. M20 den biraz daha az bas kuvveti ve hafif bir "hıss" sesi hissettik.

œ JAZZ JS-300

Zengin özelliklere sahip sistemde Game/Theatre/Music gibi sese daha önceden belirlenmiş bas tiz ayarlarını uygulayan bir buton. Ek aygıt ve subwoofer eklenebilme özelliği. Mikrofonu kolonun üzerinden ses kartına bağlayabilme özelliği var ki genelde kısa olan mikrofon kablolarına ilaç gibi geliyor. Ne yazık ki tizlerde oldukça olumsuz sonuçlar verdi.

– EDTASONIC G950

İlk kez duyduğum ve Karma adına teste katılan bu kolonlarda tahta kaplı ve gayet temiz ses veriyor. Sesi çok çok fazla açamıyorsunuz ama komşuları aşağı getirtecek kadar da ses çıkıyor. Ses sınırlı ancak dediğimiz gibi kayda değecek kadar temiz. Bu kolon da ne yazık ki ekrana yaklaştırdığınızda titretiyor. 41$+KDV son kullanıcı fiyatı ile hiç de fena değil.

– EASTERN AX-3017

Oldukça yakışıklı bir görünüşe sahip sistemde bas ve tiz gayet düzgün ayrılmış ancak bu da yanına yaklaştırdığınızda ekrana göbek attırıyor. Adaptörsüz direkt bağlandığından olsa gerek. BBS gibi ekstra bas özelliği olan sistem gerçekten basları iyi vuruyor. Ne yazık ki frekans aralığı testinde pek düzgün sonuç veremedi.

— YAMAHA YST-M7

Küçük boyuna rağmen fena ses vermeyen kolonlarda ek bir ses aygıtı bağlanabilme ve Subwoofer ve kulaklık çıkış özellikleri mevcut. ayrıntılı kitapçık ile geliyor. Ne yazık ki küçük olmasının etkisiyle bas seslerde pek varlık gösteremiyor.

“ JAZZ JS-100

Ağabeyi JS-300’e benzeyen bu kolonda Music/Theatre/Game efektleri yok. Ne yazık ki sesi az açınca bas çatlamaya tizler de cazırdamaya başlıyor.

” SONY SRS – PC71

Beni tek şaşırtan ve hayal kırıklığına uğratan kolon oldu. Oldukça şık görünüşüne ve tüm giriş çıkışları üstünde tam olarak taşımasına rağmen, ses kalitesinde ne yazık ki markasıyla ters orantılı bir performans sergiledi. Baslar ne yazık ki çok fazla açmadan bile çatladı. Bir de devamlı bir "hıss" sesi içimizi cızz etti. Hele 112$+KDV gibi bir fiyatla ne desek boş.

EDTASONIC G-550

Ucuz kolonlar arasında üst sıralarda yer alan kolonun kulaklık çıkışı yok. Biraz çirkin bir görünüşe sahip kolon hafif açınca cazırdamaya başlıyor.

SAMSUNG SMS 7631

Kulaklık çıkışı bulunmayan ve bas/tiz ayarı yerine ton düğmesi bulunan kolon ağabeysi SMS 8320’den bir gömlek üstün ses veriyor.

CREATIVE SBS 20

Ne yazık ki sadece ses versin diye yapılan kolonlardan. Tek iyi özelliği üstünde bas/tiz ayarı taşıması. Biraz bile açmaya gelmiyor; ses çatlıyor.

SAMSUNG SMS-8320

Bu kolon da seda olsun diye yapılan kolonlardan. Bir de masada gerçekten şık duruyor. Bas/tiz ayar düğmesi var; tizlerde Creative SBS20’den daha iyi, baslarda daha kötü.

SAMSUNG SMS-7841

Söylenebilecek tek şey 11$ + KDV olması. Sinema parasına kolondan daha ne beklenebilir.

Alacağınız hoparlörlere ek olarak edinebileceğiniz subwoofer’larda manyetik alan ve ses ayırımı gibi özelliklere gerek yoktur. Çünkü aslında doğru bası hissedebilmek için yere konulmaları gerekir ve doğal olarak tiz sesleri çıkarmaları beklenmez. Bu yüzden sadece bas vurmaları ve özelliklerine göre sıralandırdık.

YAMAHA YST-MSW10

Doğrusu etkilenmemek elde değil. Ne kolon alırsanız alın yanına bir tane bundan alın. Oyunları ve müziği bu kadar zevkli hale hiçbir şey getiremez. Tahta kasalı olan bu subwoofer, çok ayrıntılı olarak bir sisteme nasıl entegre edileceğini gösteren bir kitapçıkla geliyor. Tek kusuru kocaman olması, o da zaten olması gereken özelliklerden biri. Oyunu iç organlarınızda bile size hissettiriyor. Editörün Seçimi hiç bu kadar kolay olmamıştı.

JBL MEDIA SUB

Evet kitapçıklarına kalitesine ve iriliğine diyecek yok ancak sesi çok açınca çatladığını duyduk. Tabii bir subwoofer’ın amacına biraz aykırı.

PHILIPS MMS250

Oldukça iri olan bu subwoofer’da fiaytı ile orantılı olarak fena değil ancak tek tip ve mono çıkış taşıması kullanılmasını biraz zorlaştırıyor.

YAMAHA YST-MSW5

Teste katılan en ufak ve en ucuz subwoofer. Kuvvetlice kolonlara tat vermek amacıyla düşünülebilir.

Ne yazık ki bu kategoride test ettiğimiz ürünler fiyat/performans açısından pek tatminkar gelmedi. Çok kuvvetli bir çift hoparlör veya orta kuvvetteki bir çift hoparlör ile, ayrı alınmış bir subwoofer çok daha kaliteli ses çıkışı verdi. Bu yüzden bu kategoride yalnızca sıralama verebiliyoruz. Editörün Seçimi yoktur. Manyetik alan testini yaparken, eğer ayar düğmeleri üzerinde değil ise subwoofer yere konacak kabul ederek test ettik.

YAMAHA YST – M25

Quake’teki cam patlama sesini hiç bu kadar net duymamıştık. Ses ayarı minik tweeter’ların üstünde oldukça pratik ve şık. Gereken tüm çıkışları ve ayrıntılı kitapçığı ile özellikten tam puanı alıyor. Bir de baslar daha kuvvetli olsaydı gerçekten de harika olacaktı.

À MICROSOFT SOUND SYSTEM

Test ettiğimiz ikinci USB sistem olan ve hazine sandığına benzeyen ilginç tasarımdaki bu sistemde Philips’teki hata yapılmayarak normal ses kartındaki çıkıştan kullanılsa ve USB kullanılmasa bile düğmelerden ayar yapılabilmesi sağlanmış. Microsoft’un bir bu konuya el atmadığı kalmıştı. Doğrusu bekliyorduk. Subwoofer kısmı kesinlikle yere konulmalı; yoksa ekranın rengini mora çeviriyor. Üzerinde ayar olmadığı için yere konulacağını kabul ederek puan kırmadık. Baslar oldukça kuvvetli ancak yine de hafif çatlama hissettik.

Ã EASTERN 5108

Bu da üzerinde mikrofon çıkışını barındıran partik zeka ürünlerinden. Ses ayırımı ve basta etkileyici performans gösteriyor. Ne yazık ki ekranda titreme yaratıyor ve kumandalar subwoofer üstünde olduğundan yere konması pek mümkün değil.

Õ EDTASONIC G-900

Tahta kullanan ürünlerden olan bu sistem oldukça kuvvetli bas ses veriyor. Düğmeleri takılma yapan sistemin üzerinde düğmeleri de barındıran kumanda kutusu oldukça büyük. Ses ayarı için masa üstünde durması gerekli ancak ne yazık ki bu sistemde ekranı fena halde titretiyor. Ancak dediğimiz gibi ses özellikleri tatmin edici.

Œ JAZZ J-7901

Ses derinliğini arttıran 3D özelliği var. Ek Surround kolonlar için ve kulaklık için çıkışları var ancak nedense bas ve tiz ayarları yok. Ses kuvveti fena değil ancak tizlerde cazırdama yapıyor. Ses ayrımı pek iyi değil. Ekranda titreme yapmıyor.

œ SAMSUNG SMS-5100

Bu sistem de tahta olmasına rağmen kasası pek iyi oturmadığından bas vurduğunda fena cazırdıyor. Ne yazık ki ses ayırımı pek iyi değil. Patlama sahnesindeki cam sesini neredeyse hiç alamadık. Bu sistemin subwoofer’ının da üstünde kontrol düğmeleri var ve masa üstünde olması lazım ama ekranı titretiyor. Kulaklık dahil hiçbir giriş çıkış yok.

– EASTERN SS-414A

İki zarif hoparlör ve bir çok gösterişli subwoofer’dan oluşan sistemde ne yazık ki subwoofer biraz çatlıyor. Manyetik koruma özelliği maalesef ekranı titretmesini engellemiyor. Düğmeler üzerinde olduğundan aşağı indiremiyorsunuz.

— JAZZ – J6901

Ne yazık ki gördüğüm en kötü sistem. Azıcık açınca hem bas çatlıyor hem tiz cazırdıyor. Manyetik korumalı değil ekranı titretiyor. Kulaklık çıkışı da yok.

Birbirinden farklı sistemler olduğu için, birbirleri ile yarıştırmak üçüne de haksızlık olur. Onun için sadece sonuçları değerlendireceğim.

CAMBRIDGE SOUNDWORKS

DESKTOP THEATER 5.1

İlk defa sesini duyduğumda kaynaktan amfili ses alıyor olsa gerek; subwoofer’ının fena halde çatladığını duyduğum bu sistem beni yanılttı. Abartılı açınca hafif bir çatlama var, doğru; ancak o kadar sesi açar mıyız bilmem? Yamaha’nın subwoofer’ı gibi bir subwoofer kullansaydı harika olabilirdi. Tek başına sistem temiz ses veriyor. 339 $+ KDV vermek ister misiniz bilmem ama tüm kolonları denedikten sonra ilkinden daha iyi bir izlenim edindim. Tabii malzeme bol ya, dayanamayarak bu sistemin amfisinin ön iki kolonu yerine JBL kolonları ve Yamaha Subwoofer’ı bağladım ve elde edilebilecek en mükemmel sonucu dinledim. Ama böyle bir şey pek akıl karı değil tabii, 500$+KDV gibi rakamlar ödemek gerekli. Creative’in bayisi iddiasındaki üç firmadan ikisi bu ürünü bize gönderdi ve üçüncü göndermek istediğinde yeter dedik. 339$+KDV bu firmalardan alınan en düşük fiyattır. Creative artık Türkiye’deki bayilerinin kim olduğuna karar verse de, biz de rahat etsek diyorum. Bu firmaların kendileri bile bayiler kim sorusuna net cevap veremiyor.

Aslında girişte anlattığımız Dolby Digital sistem için yaratılan bu sistemi doğrudan DVD kartınızın üzerindeki dijital ses çıkışına bağlıyorsunuz. Destekleyen ses kartı yok mu? Diyelim SB Live! kullanıyorsunuz, PC-DVD Encore kartından doğrudan Live!’e çıkış yaptınız ve Live!’in arkasındaki SPDIF çıkıştan doğrudan amfiye girdiniz. Ne yazık ki olmuyor. Creative bu iş için bir çözüm tasarlıyormuş. Biraz geç oluyor ama tasarlasın da. Şu an en iyi çözüm DVD kartından digital çıkışla amfiye ve ses kartından ön ve arka olmak üzere analog çıkışlardan amfideki iki analog girişe kablo atmak. Tüm kablolar ve aksesuarlar bu pakette tam gelmiş. Ve Live!’a uyum sağlaması ve ses kalitesi açısından kablo uç konnektörleri bile altın kaplama. Geriye dönük olarak ta tam uyumlu bir sistem ve amfi ayarları oldukça hoş. Dediğim gibi testten sonra bu sisteme karşı fikirlerim değişti. Küçük surround kolonlar her yere monte edilebiliyor. Tüm montaj aksesuarları da eksiksiz. Eğer 1000$’lar gibi paralara kıyıp da ben eve komple bir Dolby Digital sistem alıp her şeyi ona bağlıyacağım demiyorsanız ve paranız da varsa uygun bir çözüm olabilir.

CAMBRIDGE SOUNDWORKS PCWORKS FOUR POINT SURROUND

Aslında daha çok Creative’in SB Live! Value modeli için uygun olan bu sistem, 4 kolon ve bir subwoofer’dan oluşuyor. Kabloların birleştiği yere takılı bir ayar düğmesi ile ana ses açılıp kısılabiliyor. Bir nevi Desktop Theater’ın kırpılmış hali. Sisteme iki çift hoparlör seti ve bir subwoofer bağlamaktan elverişli tek tarafı derli toplu olması ve sesin tek düğmeden kontrol edilebilmesi. Dediğimiz gibi subwoofer’da hafif bir çatlama söz konusu. Sesi fazla açmaya gelmiyor. Ancak kaliteli malzeme kullanılmış ve tüm kolonlar için gerekli aksesuarlar sistemle geliyor. SB Live! Value kullanan ve sistemi ucuza getirmek isteyenler için çözüm olabilir.

EASTERN HOME THEATRE DA-9000

Testteki Dolby PRO Logic özelliğine sahip bu tek sistemi reklamındaki resmini görüp de istemiştim. Midi bir müzik seti büyüklüğündeki amfi ve bütünleşik subwoofer ile 5 kolondan oluşan sistem uzaktan kumandalı. Kablolar ucu lehimli bildiğimiz çıplak uçların lehimlenmesinden oluşan ve kolonlardaki mandallara doğrudan kıstırılan sistemden. Siyah sistem oldukça şık. Yarı profesyonel sistemden en büyük eksiği tahta olmaması. "Sesi nasıl?" derseniz, hiç de fena değil. Bası köklerseniz hafif bir çatlama var. Odanıza bir mobilya gibi set ve televizyonla entegre edebilirsiniz; çünkü üç adet girişi var. Kumandası da oldukça hoş. 217$+ KDV fiyata da, inanılmaz kalite aramıyorsanız değer. Diğer sistemler içinde geriye uyumluluk söz konusu. Ön panelde THEATRE gibi, LIVE gibi sese derinlik veren ve ortam yaratan tuşlar var.

---
*Kaynak: `SES KARTLARINDA BİLMENİZ GEREKENLER/SES KARTLARINDA BİLMENİZ GEREKENLER.doc` — Akın Sekerci — 2004*
