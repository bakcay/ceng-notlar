# Yapay Sinir Ağlari

**Yapay Sinir Ağları******

**1.SİSTEM MODELLEME**

Doğa bilimleri, sosyal bilimler, mühendislik, iş dünyası ve finansın birkaç örnek başlık olarak sıralanabileceği çeşitli alanlarda modelleme ve öngörü gerçekleştirilmesi arzu edilen ve dolayısı ile yoğun çaba sarfedilen araştırma konularıdır. İncelenen sistemin giriş-çıkış ilişkisini tanımlayan ifadeye matematik model veya kısaca model denir \[1\].

Sistemin modeli, giriş uzayı *u*’dan çıkış uzayı *y*’ye bir *P* operatörü olarak tanımlanır ve tanımlama işlemiyle *P*’nin ait olduğu kümesinin özellikleri yakalanmaya çalışılır. kümesi verilmiş ve *P* olduğu biliniyorken, tanımlama işleminin hedefi olmak kayıdıyla öyle bir elemanı tespit etmektir ki iken , *P*’ye arzu edilen tarzda yaklaşsın \[2\].

Modelleme işleminde kullanılan iki temel yaklaşımın ilki, kümelendirilmiş parametre modellemesi(lumped-parameter modelling), ikincisi ise sistem tanımadır \[1\]. Kümelendirilmiş parametre modellemesi yaklaşımında, sistem, giriş-çıkış ilişkisi basitçe ifade edilebilen bileşenlerle yapılandırılmaya çalışılır. Sistem tanıma yaklaşımında ise deneysel olarak elde edilmiş veya hipotetik olarak üretilmiş giriş-çıkış verilerinin kullanılarak sistemin matematik modelinin kurulmasına çalışılır. Sistem tanıma, parametrik ve nonparametrik başlıkları altında iki grupta incelenebilir. Parametrik model, sonlu sayıda parametre ile tamamen belirlenen fonksiyonel bir formu benimsediği halde nonparametrik modelde ne fonksiyonel form ne de parametre sayısı ile ilgili bir kısıtlama vardır.

Modelin kurulabilmesi için üç temel gereksinim:

Giriş-çıkış verisi

Model adaylarının belirlenmesi

Modelin seçim kriteridir.

Gelecekteki verilerin istatistiksel özelliklerinin geçmiştekilerle uyumlu olacağı varsayımından hareketle, modellemeye konu olan sisteme ait geçmişe dönük verilerin istatistiksel özelliklerinden yararlanılarak kurulan modele zaman-serisi modeli denir. Modelin, geçmişteki verileri yeterli doğrulukta sağlaması kadar gelecekte tekrarlanma ihtimali yüksek özellikleri tanımlaması da gereklidir.

“Kestirim zordur; özellikle, geleceğe dönükse” Nils Bohr.

Sistemin karmaşıklığı veya hedefin hassaslığına bağlı olarak, tasarlanan modellerin yoğun işlem gerektiren algoritmalarının geçerliliği, gelişen teknolojinin harikası ve vazgeçilmez unsuru bilgisayarların elverdiği kolaylıkla ve hızla sınanabilmektedir. Sınamayı başarıyla geçen modeller öngörü işleminde kullanılmaktadır. Başarılı modellerin sahip olması istenilen diğer özellikler:

Parametre sayısı asgariye indirilmeli

Parametrelerin kestirimi kolay olmalı

Parametreler fiziksel olarak anlamlıca yorumlanabilir olmalıdır.

İdeal durumda, yukarıdaki maddeler de gerçeklenmiş olacaktır, modelin lineer olması arzu edilir. Bir H sistemi, ve keyfi giriş değerleri ve keyfi sabitleri için;

(2.1a)

denklemini sağlıyorsa; *lineerdir*. Bu denklemde lineer sistemlerin taşıdığı iki özellik olan *toplanabilirlik* ve *homojenlik* verilmiştir. Ayrı ayrı (2.1a) ve (2.1b) şeklindedirler:

Toplanabilirlik özelliği:

(2.1b)

Homojenlik özelliği:

(2.1c)

Bu özellikler, süperpozisyon ilkesi sayesinde sonlu olmak kaydı ile keyfi sayıda giriş teriminin toplamına genişletilebilir. Özelliklerden birinin sağlanamadığı durumda sistemin nonlineer oluşuna delil elde edilmiş olunur. Yapılabilecekler sistemin lineerleştirilmesi veya nonlineerlik ile başedebilecek bir tanıma algoritmasının geliştirilmesi ile sınırlıdır. Lineer sistemler için geliştirilmiş pek çok tanıma algoritması mevcuttur. Ancak, ilgi alanı nonlineer sistemlere kaydığında olanaklar kısıtlıdır. Yapay sinir ağlarının nonlineer ilişkileri öğrenme ve arzulanan toleranslar dahilinde yaklaşımda bulunma yeteneği duyulan ilginin sebeplerindendir.

Öncelikle parametrik modellerden AR modeli hakkında kısa bilgi verilecek ve parametrik olmayan modellerden yapay sinir ağları Bölüm 3’ te detaylı bir şekilde ele alınacaktır.

**Parametrik Model**

**AR Modeli**

Giriş-çıkış ilişkisini basitçe tanımlayan fark denkleminin genel ifadesi (2.2) ile verilmiştir. ve sabit çarpanlar, çıkış değerleri ve giriş değerleri dizisi olmak üzere,

(2.2)

Bu denklem, *n* anındaki çıkışın, önceki çıkış değerlerine bağlılığını sağlayan katsayıları ve önceki giriş değerlerine bağlılığını sağlayan katsayılarını içerdiğinden ARMA modeli olarak anılır. Özel durumlar olarak, AR ve MA modelleri, sırasıyla, (2.2a) ve (2.2b) numaralı denklemlerle tanımlanırlar \[3\].

AR Model:

** ** (2.2a)

MA Model:

** ** (2.2b)

AR modelin revaçta olmasının altında yatan başlıca sebep, AR parametrelerinin hesabı için kullanılan yöntemlerin çoğunun doğrusal denklem takımlarının çözümüne dayanması nedeniyle kolay olmasıdır.

**AR Model Mertebesinin Belirlenmesi**

AR model mertebesi için en iyi değer, genellikle, önceden bilinemez. Düşük mertebeli modeller az bilgi içeren spektral kestirim sonucu üretirken çok yüksek mertebeli modellerin kestirimi sahte detaylar verme eğilimindedir. AR model mertebesi arttıkça kestirimin gücü azalır. Buna karşı kestirim hatası gücü, artan model mertebesiyle monoton azaldığından arama sürecinin ne zaman durdurulması gerektiği açık değildir.

Model mertebesi, ikisi Akaike tarafından ortaya atılmış çeşitli kriterler doğrultusunda belirlenebilir. Akaike’nin ilk kriteri, nihai kestirim hatası (*final prediction error*(FPE)) adıyla anılır. Veri sayısı N, model mertebesi , karşılık gelen kestirim hatası gücü olmak üzere AR modelinin FPE’si (2.3) eşitliği ile tanımlanır \[4\].

(2.3)

Artan p’ye karşılık azaldığı halde (2.3) eşitliğindeki diğer çarpan artar. Artan ’ye karşılık değerinin bir minimuma ulaşması beklenir. Minimum değerini sağlayan değeri AR mertebesi olarak seçilir.

Akaike’nin ikinci kriteri, kestirim hatasının gücünün, mertebeli filtrenin bir fonksiyonu gibi alınarak log-likelihood’unun minimizasyonuna dayanır. Akaike’nin bilgi kuramlı kriteri (Akaike Information Theoretic Criterion(AIC)) olarak anılan yaklaşım (2.4) eşitliği ile tanımlıdır.

(2.4)

(2.4) eşitliğindeki ilk terim, artan değerine karşılık monoton azalır. Eşitlikteki ikinci terim, model mertebesini arttırmaktan doğan ceza terimi olarak düşünülebilir.

Veri sayısı N, sonsuza gittikçe ve denk olurlar \[4\].

**YAPAY SİNİR AĞLARI**

Bu bölümde, öncelikle yapay sinir ağlarının biyolojik kökeninden bahsedilecek ve daha sonra yapay sinir ağları hakkında genel bilgi verilecektir.

**Yapay Sinir Ağlarının Biyolojik Kökeni**

İnsan beyni, düşünme, hatırlama ve problem çözme yeteneklerine sahip karmaşık bir sistemdir. Beyin fonksiyonlarının bilgisayarla taklit edilmesine yönelik girişimlerin başarısı henüz kısmi olmaktan öteye gidememiştir.

Bu karmaşık yapının temel birimi nörondur. Şekil 3.1’de gerçek sinir hücresinin şematik gösterimi verilmiştir. Nöron, dendritler aracılığıyla sinyalleri alır ve birleştirir. Bileşke sinyalin yeterince güçlü olduğu durumda nöron ateşleme yapar ve sinyal, terminalleri aracılığıyla diğer nöronların dendritleriyle bağlantılı olan akson boyunca yol alır. Akson boyunca yol alarak nörona ulaşan sinyaller, elektriksel yükü değişken hızlarda ileten sıvı ile dolu çok küçük boşluklardan geçerler. Bu boşluklar, sinaptik bağlantılar olarak anılır. Sinaptik bağlantının empedans veya kondüktans değerinin ayarlanması, bellek oluşumu ve öğrenmeyi sağladığından kritik önemdedir \[5\].

**Şekil 3. 1 **Gerçek sinir hücresinin şematik gösterimi

**Yapay Sinir Hücresi**

Sinir ağları biribirine paralel olarak çalışan basit elemanlardan oluşur. Gerçek bir sinir hücresinin birimlerine eşdeğer bileşenlerle modellenen yapay sinir hücresi Şekil 3.2’de gösterilmiştir. Gövdenin giriş birimi olan bağlantıların herbirinin kendine ait bir ağırlık çarpanı vardır. Ağırlık değeri pozitif veya negatif olabilir. Uygulanan sinyallerin ağırlık değeriyle çarpımları, iki kısımdan oluşan gövdenin ilk kısımında toplanır. Bu toplam, ikinci kısmı tanımlayan aktivasyon fonksiyonunun argümanı olur.

**Şekil 3. 2 **Yapay Sinir Hücresi \[6\]

**Nöron Modelleri**

Nöronlar, yapay sinir ağlarının bilgi işleyen yapısal elemanlarıdır. Bir nöronun yapısında üç temel yapıtaşı bulunur:

**Sinaps adı verilen bağlantılar:** Her sinapsın kendine ait *w**ij* ile gösterilen bir ağırlık çarpanı vardır. Bu ifadede *i* ile söz konusu nöron, *j* ile sinapsın giriş uygulanan ucu tanımlanmaktadır. Ağırlık çarpanı pozitif değerli olabileceği gibi negatif değerli de olabilir \[7\].

**Toplayıcı:** Uygun ağırlıkların uygulanmış olduğu giriş sinyallerini toplamak için kullanılır \[7\].

**Aktivasyon fonksiyonu:** Nöronun çıkışının genliğini kısıtlamak için kullanılır. Genelde bir nöronun normalize edilmiş genliği \[0,1\] veya \[-1,1\] kapalı aralığında ifade edilir \[7\].

**Aktivasyon Fonksiyonu Çeşitleri**

*arg = I**j**+b**j* tanımlaması kullanılarak bir nöron için aktivasyon fonksiyonu Φ*(arg)* ifadesiyle gösterilir. Aktivasyon fonksiyonunun üç temel tipi takip eden alt başlıklarda verilmiştir.

**Eşik Fonksiyonu**

Eşik fonksiyonu kullanılarak yapılmış bir nöron literatürde McCulloch-Pitts modeli olarak adlandırılır. Fonksiyonun grafiği Şekil 3.3’te gösterilmiştir \[8\].

**Şekil 3. 3 **Eşik Fonksiyonu

**Kısmi Doğrusal Fonksiyon**

Doğrusal olmayan bir genlik artımı sağlayan bu aktivasyon fonksiyonu Şekil 3.4’te gösterimiştir. Eğer doğrusal bölgedeki genlik arttıran katsayı yeterince büyük alınırsa parçalı doğrusal fonksiyon eşik fonksiyonunua dönüşür \[8\].

**Şekil 3. 4 **Kısmi Doğrusal Fonksiyon

**Sigmoid Fonksiyonu**

Yapay sinir ağları oluşturulurken en çok kullanılan aktivasyon fonksiyonudur. Doğrusal ve doğrusal olmayan davranışlar arasında denge sağlayan sürekli artan bir fonksiyon olarak tanımlanır. Sigmoid fonksiyona bir örnek lojistik fonksiyondur ve Şekil 3.5’de gösterilmiştir \[7\].

**Şekil 3. 5 **Lojistik Sigmoid Fonksiyonu

Görüleceği üzere sigmoid fonksiyonunun türevi alınabilirken eşik fonksiyonunun türevi alınamaz.

Hiperbolik tanjant fonksiyonu da sigmoid fonksiyon örneğidir ve Şekil 3.6’da görülebilir.

**Şekil 3. 6 **Hiperbolik tanjant fonksiyonu

**Yapay Sinir Ağı**

Yapay Sinir Ağı, öngörülen sayıda yapay sinir hücresinin, veri işlemek amacıyla belirli bir mimaride yapılandırılmasıyla şekillenir. Bu yapı, genellikle,numaralandırılan birkaç katmandan oluşur. İlk katman, çoğunlukla numaralandırılmayan, giriş katmanıdır. Bu katmanın numaralandırılmaya katılmayışının sebebi, giriş katmanındaki elemanların ağırlık çarpanları ve aktivasyon fonksiyonlarının olmaması sebebiyle veri girişinden başka bir işlem yapmamalarıdır. Çıkış katmanı da son katmandır. Tercihe bağlı olarak farklı sayıda olabilen diğer ara katmanların ortak adı gizli katmandır \[7\].

**Ağ Yapıları**

Ağ yapıları tek katmanlı ileri beslemeli, çok katmanlı ileri beslemeli ve döngülü yapay sinir ağları olmak üzere üç temel başlıkta toplanabilir.

**Tek Katmanlı-İleri Beslemeli Sinir Ağları (FF)**

Tek katmanlı ileri beslemeli yapay sinir ağı en basit ağ yapısıdır. Bir giriş katmanı ve bir çıkış katmanı vardır. Örnek yapısı Şekil 3.7’de gösterilmiştir. Bu tip bir ağda bilgi girişten çıkışa doğru ilerler yani ağ ileri beslemedir. Tek katmanlı olarak isimlendirilmesinin sebebi, giriş katmanının veri üzerinde hiçbir işlem yapmadan veriyi çıkış katmanına iletmesidir \[7\].

**Şekil 3. 7 **Tek katmanlı yapay sinir ağı

**Çok Katmanlı-İleri Beslemeli Sinir Ağları (FF)**

Bu tip yapay sinir ağlarının özelliği, Şekil 3.8’da da görüleceği üzere bir veya daha fazla gizli katman içermesidir. Gizli katmanların amacı giriş ve çıkış katmanları arasında gerekli bir takım işlemler yapmaktır. Giriş katmanı geniş olduğu zaman gizli katmanlar sayesinde yüksek dereceli istatistiksel veri elde edilebilir. Çok katmanlı yapılarda *(n).* katmanın çıkış sinyalleri *(n+1).* katmanın giriş sinyalleri olarak kullanılır. *m *adet giriş düğümü, ilk gizli katmanında *h**1* adet nöron, ikinci gizli katmanında *h**2* adet nöron ve çıkış katmanında *q* adet nöron bulunan bir çok katmanlı ileri besleme ağı *m-h1-h2-q *ağı olarak adlandırılır. Eğer her katmanda bulunan nöronlar bir sonraki katmanın tüm nöronlarına bağlı ise bu tip ağa tam bağlantılı ağ denir. Eğer bu sinaptik bağlantılardan bazıları eksikse ağ, kısmi bağlantılı ağ adını alır \[7\].

**Şekil 3. 8 **Çok katmanlı yapay sinir ağı

**Radyal Tabanlı Sinir Ağları (RBF)**

Radyal tabanlı ağlar, duyarlı almaç bölgelerinin olduğu giriş tabakası, radyal tabanlı nöronları, Şekil 3.9, içeren gizli tabaka ve çoğunlukla doğrusal aktivasyon fonksiyonlu nöronlardan ibaret çıkış tabakasından oluşur. Radyal tabanlı ağlar, geriyayılım algoritmalı ileri beslemeli ağlardan daha fazla nöron kullanımına ihtiyaç duyabilirse de eğitim süresi çok daha kısadır. Yoğun eğitim verisiyle daha iyi sonuçlar verir \[8\].

**Şekil 3. 9 **Radyal tabanlı nöron

Radbas transfer fonksiyonunun net girişi, ağırlık vektörü, *w,* ile giriş vektörü, *p*’nin vektörel uzaklığının bias terimi ile çarpımıdır. *w* ile *p* arasındaki uzaklık azaldıkça transfer fonksiyonunun çıkışı artar ve uzaklık sıfırken çıkış maksimum değeri 1’e ulaşır. *w* ile *p* arasındaki uzaklık arttıkça çıkış sıfıra gider \[8\].

**Şekil 3. 10 **Radyal tabanlı fonksiyon

Radyal tabanlı bir ağın topolojisi Şekil 3.11‘ de gösterilmştir.

**Şekil 3. 11 **Radyal tabanlı ağ topolojisi

**Döngülü Yapay Sinir Ağları (RNN)**

Döngülü yapay sinir ağlarının ileri beslemeli ağlardan farkı en az bir adet geri besleme çevriminin olmasıdır.

Yukarıda verilen sınıflandırmada, bağlantıların simetrik veya asimetrik olması durumuna göre alt sınıflar ortaya çıkar. *i* nöronundan *j* nöronuna yönelik bir bağlantı varsa *j*’den *i*’ye yönelik bir bağlantı da vardır. Bu iki bağlantının ağırlıkları *w**ij**=w**ji* eşitse bağlantı simetriktir denir. Eşitsizlik durumunda, bağlantı asimetrik olur.

Farklı katmanlara ait nöronların bağlantısına, katmanlararası(interlayer) bağlantı denir. Aynı katmandaki nöronların bağlantısına, katmaniçi(intralayer) bağlantı, komşu olmayan katmanlardaki nöronların bağlantısınada katmanlarötesi(supralayer) bağlantı denir. Bunlardan başka, bir nöron kendisiyle bağlantılı olabilir. Sıkça kullanılan bir terim olan tam-bağlantılılık, bir katmana ait tüm nöronların komşu katmandaki tüm nöronlarla bağlantılı olduğu durumu tanımlar \[7\].

**YSA’da Öğrenme ve Hatırlama**

YSA’nın gerçekleştirdiği iki temel fonksiyon, öğrenme ve hatırlamadır. Öğrenme, ağırlık değerlerinin, bir giriş vektörüne karşılık arzu edilen çıkış vektörünü sağlamak üzere uyarlanmasıdır. YSA’nın, belirli bir girişe, ağırlık değerlerine uygun bir çıkış üretmesi de hatırlama olarak tanımlanır.

Ağırlık değerlerinin ayarlandığı öğrenme süreci denetimli, denetimsiz olabilir. Aralarındaki farkın kaynağı eğitim verisinin sınıflandırmasını yapan denetim mekanizmasının olup olmadığıdır. Bu durumda, denetimsiz öğrenme sürecinde

öğrenmenin yanısıra eğitim verisinin sınıflandırması da başarılması gereken bir başka görevdir \[7\].

Mühendislik uygulamalarının büyük çoğunluğu denetimli öğrenmeyi kullanır. Yapay sinir ağına, yapması istenilen göreve dayalı bir dizi örnek bilgi verilerek sinir ağı eğitilir. Burada amaç belirli bir giriş için hedef bir çıkış elde etmektir. Hedef çıkış, denetmen tarafından sağlanır. Elde edilen çıkışla hedef karşılaştırıldığı zaman hedefe ulaşılamamışsa bağlantıların ağırlıkları benimsenen öğrenme yaklaşımına göre ayarlanarak işlem tekrarlanır. Blok diagram olarak Şekil 3.12’de gösterilmiştir.

**Şekil 3. 12 **YSA’nın eğitimi

**Eğitim ve Test Verisi Seçimi**

Yapay sinir ağının eğitimi ve sınaması için toplanan veri sistemin düzgün çalışma uzayını kapsamalıdır. Örnek kayıtlarının çalışma uzayının sınırlarını belirlediği ve yapay sinir ağlarının yalnızca eğitildiği çalışma aralığı için güvenilir sonuç verebildiği, yani, ekstrapolasyon yeteneğinin güvenilemeyecek derecede kısıtlı olduğu unutulmamalıdır. Genel özelliklerin net olarak belirlenmesi için örnek kayıdı koleksiyonunun geniş olması tercih edilir. Bu kayıtların bir kısmı eğitim aşamasında kullanılırken bir kısmı sınama aşamasında ağın genelleştirme yeteneğinin teyidi amacıyla kullanılır. Sınamanın başarısızlığı durumunda, sınama amacıyla kullanılan kayıtların bir kısmı eğitim verisine katılarak eğitim ve sınama işlemleri kabul edilebilir bir performans kriterine kadar tekrarlanır \[7\].

Yapay sinir ağı eğitiminde karşılaşılan temel bir sorun ezberlemedir. Yapay sinir ağının eğitim sürecindeki hata seviyesi, test sürecindeki hata seviyesine göre bariz farklılıklar gösterdiği takdirde ezberleme sorunu ile karşılaşılmış olur. Bu da tanımlanması istenen fonksiyel ilişkiden ziyade eğitim verisindeki gürültü gibi tuhaflıkların da öğrenildiği anlamına gelir. Ezberlemeyi azaltmak için yapılabilecekler:

Eğitimde kullanılan kayıt sayısını arttırarak gürültünün ortalamasının kendiliğinden düşmesini sağlamak,

Serbest parametre olan nöronların sayısını kullanılması gerekenin asgarisi ile sınırlamak,

Eğitimi, ezberleme başlamadan kesmek. Yöntem, çapraz değerlemeli eğitim olarak adlandırılır. Esası, eğitim sırasında ezberleme kontrolü yapmaya dayanır. Eğitim aşamasında biri eğitim, diğeri kontrol için olmak üzere iki veri grubu kullanılır. Her epokun sonunda her iki grup için hatanın RMS değeri hesaplanır ve kontrol kümesinin hatasında değişim olmadığı halde eğitim kümesinin hatasının azalmaya devam ettiği aşama tespit edilmeye çalışılır. Bu aşamada eğitim kesilir \[7\].

**Geri Yayınım Algoritması (BP)**

Uygun ağırlıkların bulunması için en sık kullanılan yöntem geriyayınımdır. Geriyayınım algoritması, bir hedef fonksiyonu minimize etmek üzere tasarlanmış optimizasyon tekniğidir\[9\]. En sık kullanılan hedef fonksiyon hatanın karesidir. , hata terimini göstermek üzere, hata (3.1a) ve hedef fonksiyonun tanımlanmasında kullanılan hatanın karesi (3.2b) eşitliğiyle verilir.

(3.1a)

(3.1b)

Yukarıda kullanılan gösterimde, *k* katman numarası, *q* nöron numarasını belirlemektedir. Delta kuralıyla ifade edildiği üzere, ağırlık değerindeki değişim, hatanın karesinin ağırlığa göre değişim oranıyla orantılıdır.

(3.2a)

Kısmi türev, zincir kuralı kullanımıyla açılarak

(3.2b)

Bu eşitlikte,

(3.3a)

(3.3b)

(3.3c)

(3.3d)

(3.3) eşitlikleri (3.2b) eşitliğine yerleştirilirse;

(3.4)

Esasen geriyayılacak hata terimi olan δ aynı zamanda kısa bir gösterim elde etmek için;

(3.5)

olarak tanımlanırsa;

(3.6)

N, iterasyon sayacı olmak üzere, (N+1). adım için ayarlanacak ağırlık değeri;

(3.7)

ile elde edilir.

(3.7) eşitliğinde tanımlanan işlem, uygun ağırlık değerlerine ulaşabilmek için çıkış katmanının tüm nöronlarına uygulanır. Hedef değerlere ulaşılamamasının bir sebebi hatalı çıkış katmanı ağırlıklarıyken diğeri, gizli katmanın ürettiği hatalı çıkışlardır. Gizli katmanın ağırlıklarının ayarlanmasında kullanılan denklemler, hedef değer olmaksızın hesaplanması gereken hata terimi haricinde aynıdır. , çıkış katmanında bağlantılı olduğu her nöronun hata terimine katkı yapan gizli katman nöronlarının herbiri için ayrıca hesaplanmalıdır.

Hatanın ağırlıklara göre gradyanı başlangıç noktası alınıp zincir kuralıyla devam edilirse,

(3.8a)

(3.8b)

(3.8b) Eşitliğinin sağ tarafındaki terimleri ayrı ayrı ele alalım:

(3.9a)

(3.9b)

(3.9c)

(3.9d)

(3.9e)

(3.9) eşitlikleri (3.8b) eşitliğinde yerlerine koyulursa,

(3.10a)

(3.10b)

(3.11)

elde edilir.

Son adım olarak, gizli katman nöronunun (N+1). iterasyon için değeri (3.12) ile bulunur:

(3.12)

Tüm gizli katman nöronları için değişiklik yapıldıktan sonra yeni girişler uygulanır ve süreç yeniden başlar. Hedeflenen hata kriterine ulaşılana dek iterasyon devam eder. Hata kriterine ulaşıldığında eğitim tamamlanmış olur \[5\].

**Geri Yayınımlı Eğitimi Etkileyen Etmenler**

Geriyayınımlı eğitimin başarımını arttırmak için yapılabilecek bir takım düzenlemeler önerilmiştir.

**Bias**

Her bir nöron için bir bias elemanı ilave edilebilir. Aktivasyon fonksiyonunun apsisi

kestiği noktayı öteleyerek nöronun eşik seviyesinde değişiklik etkisi yaratır. Genelde, eğitim hızını olumlu etkiler. Giriş elemanlarının biası (+1) olmak durumunda olmasına karşın diğer biaslar herhangi bir değer alabilir ve eğitilebilir \[5\].

**Momentum**

Hareketli bir cismin momentumunun etkisine benzer, eğitim sürecinin yönünün korunması sağlar. Bunun için, ağırlık ayarlaması sırasında, önceki ağırlık değişimiyle orantılı bir terim ilave edilir. , momentum terimi olmak üzere denklem (3.13) elde edilir:

(3.13)

Yerel minimumdan kurtulmayı sağlayabildiği için ilgi gören düzenlemelerdendir. Ancak, geriyayınımın olamadığı gibi momentum ilavesi de her derde deva değildir \[5\].

**Öğrenme Katsayısı( )**

Pozitif değerli olmak zorundaki öğrenme katsayısı 2’den büyük seçildiğinde YSA’nın kararsızlığına, 1’den büyük seçildiğinde de çözüme ulaşmaktansa salınım yapmasına sebep olur \[7\]. Öğrenme katsayısı için uygun aralıktır. Bu aralıkta seçilen katsayının büyüklüğüyle, öğrenme adım aralığı orantılıdır. Eğitim verisinin değişim oranına uygun katsayı seçilmelidir. Uyarlanabilir öğrenme katsayısı kullanımı da başvurulabilecek yöntemlerdendir.

**Sigmoid Fonksiyonunun Eğim Parametresi( ) **

Eğim parametresine bağlı değişim Şekil 3.13’de gösterilmiştir. Artan ağırlık değerleri, nöronun, sigmoid fonksiyonun eğiminin(türevinin) çok küçük değerli bölgelerinde işlem yapmasına sebep olur. Geri yayımlanan hata terimi türevle orantılı olduğundan, düşük eğimde yeterli eğitim gerçekleşmez. Eğimin ayarlanması, eğitim süresini ve başarısını doğrudan etkiler \[7\].

**Şekil 3. 13 **Lojistik sigmoid fonksiyonunun eğim parametresiyle değişimi

**Yerel Minimum**

Geriyayınım algoritmasının sıkıntı yaratan yanı, yerel minimuma takılmasıdır. Algoritma, gradyan azaltma yöntemini kullandığı için hata yüzeyinin eğimi negatif olduğu sürece ağırlıkların minimuma ulaşmayı sağlayacak şekilde ayarlandığı kabul edilir. Hata yüzeyi, kolaylıkla düşülebilecek fakat kurtulmanın mümkün olamayabileceği tepe ve çukurları barındırabilir. Atanan ilk ağırlık değerleri, civarında, azalan gradyan yönünde arama yapılacak noktayı belirler. Rasgele seçilen ilk noktadan, global minimuma kadar olan mesafede yerel minimum problemini yaratabilecek hata değerleriyle karşılaşmak muhtemeldir. Şekil 3.14 yerel minimumları göstermektedir.

**Şekil 3. 14 **Karşılaşılan minimum türleri

**YSA ile Zaman Serisi Modelleme**

YSA, geçmişe ait verilerin oluşturduğu zaman serisinin modellenmesi ve geleceğe dönük kestirim yapılması işlemlerinde artan bir ilgi görmekte ve kullanılmaktadır. Mertebesi belirlenmiş AR, MA veya ARMA modeli kullanılarak yapılan kestirime benzer olarak, uzunluğu YSA’nın giriş elemanlarının sayısına eşit bir pencere, zaman serisi üzerinde adım adım ilerleyerek giriş olarak uygulanacak zaman serisi elemanlarını tanımlar. İşlem Şekil 3.15’de gösterilmiştir. Bu işlem, hem modelleme hem de kestirim sırasında kullanılır. Modelleme sırasında, pencere uzunluğunun *p* ile verildiği durumda, serinin *(p+1)*. elemanı hedef değer olarak alınır. Seri boyunca ilerleyen kayan pencerenin belirlediği veriler için hedeflenen hata kriterine ulaşılana dek YSA eğitimi devam eder. Geleceğe dönük kestirim, bir adımdan daha fazlası için yapılabilirse de hata artacaktır. Hatanın, bir çıkış değerine göre azaltılmaya çalışılması çözümün doğruluğunu arttıracaktır \[7\]. Bu noktada vurgulanması gereken özellik algoritmanın ek yük getirmeden SISO(Tek Giriş Tek Çıkış), MISO(Çok Giriş Tek Çıkış) veya MIMO(Çok Giriş Çok Çıkış) çalışabilmesidir \[10\].

Bundan başka, farkı, eğitimde kullanılacak veriden kaynaklanan iki alternatif modelleme yaklaşımından birincisinde ilk adım, mevsimsel değişimler gibi periyodikliği bariz bileşenlerin veriden çıkarılmasıdır. Gerikalan, detay niteliğindeki veri üzerinden YSA eğitilir. Eğitilen YSA’nın kestirimlerinin, daha önce tespit edilmiş periyodik bileşenlerle toplanmasıyla işlem tamamlanır. Diğer yaklaşımda eğitim verisi, ardışık elemanlar arasındaki farkın veya değişim oranının hesaplanmasıyla elde edilir \[7\].

**Şekil 3. 15 **YSA ile zaman serisi modelleme işleminin gösterimi

**EVRİMCİ ALGORİTMALAR**

Evrimci Algoritmalar, tasarım ve gerçekleştirilmesinde evrim sürecinin hesaplamalı modellerinin esas alındığı bilgisayar tabanlı problem çözme sistemlerini tasvir etmekte kullanılan genel başlıktır \[11\]. “Evrimci Programlama”(Fogel, Owens ve Walsh 1966), “Evrim Stratejileri” (Rechenberg 1973) ve “Genetik Algoritmalar” (Holland 1975) bu alandaki baskın yöntemlerdir. Geliştiricilerinin benimsedikleri gösterim tarzı, seçim stratejileri, nüfus yönetimi ve genetik operatörlerin önemsenme derecesine göre farklılıklar arz ederler.

**Temel İlkeler**

Şekil 4.1’deki gösterimle tanımlanabilecek olan standart EA’nın çalıştırılabilmesi için tespit edilmesi gereken temel noktalar: kromozom gösterimi, seçim stratejisi, çoğalma operatörleri, ilk topluluğun yaratılması, sonlandırma kriteri ve değerlendirme fonksiyonudur. Bu noktaların belirlenmesinde probleme uygunluğu gözetilmelidir.

**Şekil 4. 1 **Evrimci Algoritma akış diagramı

**Kromozom Gösterimi**

Uygun gösterimden kasıt, muhtemel çözümün bir dizi parametre ile temsil edilebileceği ilkesinin gayri ihtiyari kabulüne uygun olarak parametre sayısının belirlenmesidir. Parametreler, gösteriminde belirli bir alfabenin kullanıldığı genler olarak kodlanırlar. Genler bir araya gelerek kromozomları oluştururlar. Genlerin kromozom üzerindeki yerleri lokus adıyla anılır. Alfabe sembollerden, iki tabanlı sayılar olan {0,1}’den, tamsayılardan, gerçel sayılardan, matrislerden oluşabilir. EA’nın kullanılmaya başlandığı ilk zamanlarda, parametre değerleri için iki tabanlı gösterim daha uygun görülüp yaygın olarak kullanılmış olsa da gerçel değerli gösterim de mümkündür. Michalewicz, çalışmalarıyla göstermiştir ki arama uzayının doğasıyla uyumlu gösterimler daha iyi sonuçlar sağladığından daha verimlidir. Bu bağlamda, fonksiyon optimizasyonunda, kromozomların temsili için alt ve üst sınırlar dahilinde gerçel sayıların kullanımı alışılageldik iki tabanlı gösterime kıyasla

daha elverişlidir \[7\]. Yapılan çalışmada gerçel değerli gösterim kullanılmıştır. Gen bilimi terminolojisinde, belirli bir kromozomun gen içeriği, genotip olarak anılır. Genotip, bir organizmayı teşkil etmekte gerekli olan bilgiyi içerir. Teşkil edilmiş görüntü de fenotip olarak anılır. Aynı terimler EA için geçerlidir. Örneğin, bir tasarım işinde, belirli bir tasarımı temsil eden parametreler genotipi oluştururken gerçekleştirilen tasarım fenotiptir. Kromozomun uygunluk değeri, fenotipin başarımına dayanır. Bu da uygunluk fonksiyonu kullanılmak suretiyle kromozomdan hesaplanabilir.

**Uygunluk fonksiyonu**

Çözümü istenen her problem için bir uygunluk fonksiyonu belirlenmelidir. Uygunluk fonksiyonu, belirli bir kromozomun çözüme yakınlığının göstergesi olan uygunluk değerinin hesaplanmasında kullanılır \[12, 13\].

**Olgunlaşmamış Yakınsama**

İlk topluluk rasgele değerlerle yaratıldığından bireylerin uygunluk değerleri ve belirli bir lokusa ait genler arasında ciddi farklılık olacaktır. Topluluk yakınsadıkça uygunluk değerlerinin varyansı azalır. Çözüme yakınlığının göstergesi olan uygunluk değerinin değişimine bağlı olarak karşılaşılabilecek sorunlar da vardır. İlki olgunlaşmamış(premature, erken) yakınsama ve ikincisi yavaş sonlanmadır(slow finishing) \[12, 13\].

Holland'ın şema teorisi, bireylere, uygunluk değeriyle orantılı çoğalma fırsatı tanınmasını önerir. Ancak topluluk nüfusunun sonlu olması zorunluluğu nedeniyle olgunlaşmamış yakınsama gerçekleşebilir. EA’nın nüfusu sınırlı topluluklarda etkin çalışabilmesi için bireylerin kazanacağı çoğalma fırsatı sayısının ne çok fazla ne de çok az olacak şekilde denetlenmesi gerekir. Uygunluk değeri ölçeklenerek, erken nesillerde, aşırı uygunluk değerli bireylerin toplulukta hakimiyet kurması engellenir.

**Yavaş Sonlanma**

Olgunlaşmamış yakınsamaya karşıt sorun yavaş sonlanmadır. Epey nesil geçmesine rağmen topluluk yaklaştığı halde global minimumu konumlandıramayabilir. Ortalama uygunluk değeri yeterince yüksek değerli olup en iyi bireyin uygunluk değerine yakınsamış olabilir. Olgunlaşmamış yakınsamayı önlemede kullanılan yöntemler bu soruna karşı da kullanılır \[12, 13, 14\]. Kullanılan yöntemlerle topluluğun etkin uygunluk değerinin varyansı arttırılır.

**Seçim**

EA’da çözüme giden yol, bireylerin uygunluk değerinin artışını sağlayan gen içeriğinin edinilmesinden geçer. Bu sebeple, yeni nesili oluşturacak bireylerin seçimi hayati önemdedir. Önerilen çeşitli temel yaklaşımlar ve çeşitlemeleri mevcuttur. Sıklıkla kullanılan stratejiler, kesme seçimi, rulet tekerleği ve stokastik örneklemedir.

**Kesme Seçimi**

“En Güçlüler Yaşar” prensibinden hareketle uygunluk değerine göre büyükten küçüğe sıralanan bireylerden belirlenen sayıda en yüksek değerli bireyler seçilir, diğerleri yok edilir.

**Stokastik Evrensel Örnekleme**

James Baker(1987) tarafından önerilen yöntemde rulet stratejisine benzer yaklaşımla, bireyler doğru üzerine yerleştirilir. Seçilecek birey sayısına eşit sayıda işaretçinin, doğru üzerine eşit aralıklarla yerleştirilmesiyle örnekleme yapılır. Örneğin, seçilecek birey sayısı *Npointer=6 *olduğunda, örnekleme periyodu *1/Npointer=0.167 *olur ve ilk işaretçinin yeri \[*0, 1/NPointer*\] aralığında olmak koşuluyla rasgele seçilir \[15\].

**Şekil 4. 2**** **Stokastik evrensel örnekleme

**Rulet tekerleği seçimi**

Stokastik bir yöntemdir. Bireyler, uygunluk değerleriyle orantılı uzunluklarla, ardışık olarak bir doğru üzerine veya her bir diliminin alanı uygunluk değeriyle orantılı olacak şekilde rulet tekerleği üzerine yerleştirilirler. Üretilen rasgele sayının rastladığı aralığın sahibi birey seçilir. Önceden belirlenen birey sayısına ulaşılana dek işlem tekrarlanır \[15, 16\].

**Şekil 4. 3 **Rulet tekerleği seçimi

**Çoğalma**

Uygunluk değerini gözeten seçim stratejisi sonucu seçilen kromozomların çaprazlanmasıyla yeni nesili oluşturan bireylerin üretildiği evre, çoğalmadır. Ebeveyn olarak iki kromozom seçildikten sonra gerçekleşen çaprazlama işlemi tek veya çok noktalı olabilir. Rasgele belirlenen noktadan ikiye ayrılan kromozomlardan baş ve kuyruk dizileri elde edilir. Şekil 4.4 ve Şekil 4.5’te görüldüğü gibi, baş veya kuyruk dizilerinin değiştokuşu sonrasında birleştirilen diziler yeni nesilin iki ferdi olarak kromozom havuzuna kaydedilirler.

**Şekil 4. 4 **Tek noktalı çaprazlama

**Şekil 4. 5 **Çok noktalı çaprazlama

**Mutasyon**

Faydası tartışılmaya devam etmekle birlikte sıkça kullanılan bir diğer genetik operatör mutasyondur. Rasgele seçilen kromozomdaki bir veya birkaç geni rasgele değişikliğe uğratan mutasyon operatörünün nesil başına uygulanma oranının düşük olması tavsiye edilir. Şekil 4.6’da tek noktada ve Şekil 4.7’de çok noktada mutasyon işlemi gösterilmiştir. İki tabanlı gösterimde, genin alabileceği değer { 0 , 1 } ile kısıtlı olduğundan 01’e, 10’a dönüşür. Gerçel sayılı gösterimde ise, gendeki değişim, rasgele belirlenen bir sayıyla yerdeğişimine bağlı olabileceği gibi mevcut değere mutasyon adımı olarak anılan küçük ilavelerle de gerçekleşebilir \[7\].

**Şekil 4. 6 **Tek noktada mutasyon

**Şekil 4. 7 **Çok noktada mutasyon

**Yakınsama**

EA’nın doğru gerçekleştirildiği uygulamalarda, kromozom topluluğundaki en iyi ve ortalama uygunluk değerleri, bireylerin, evrim sonucu gelişimiyle biribirine ve global optimuma yakınsar. Uygunluk kriterini sağlayan birey yakınsamıştır denir. Topluluk ortalamasının, en iyi bireyin uygunluk değerine yakınsadığı durumda topluluk yakınsamış olur. Topluluk ve kromozomun yakınsamasından başka, genin yakınsaması da tanımlanmıştır. Bir nesildeki kromozomların belirli bir lokusu %95 oranında aynı gene sahipse gen yakınsamıştır denir \[12, 17\].

**Tersten Sıralama ve Yeniden Düzenleme**

Genlerin sıralanışı çok önemlidir. Sıralamayı değiştirerek arama uzayını genişleten bir operatör tersten sıralamadır. Bu operatör, bir kromozom üzerindeki genlerden rasgele belirlenmiş iki lokus arasında kalanları ters sırayla yerleştirir.

**Çift Değerlilik ve Baskınlık**

İleri hayat formlarında, kromozomlar ikili sarmal düzenindedir, genler iki şerit üzerine kodlanmıştır. Biribirinin alternatifi iki genin kodlandığı yapı, çift değerli(diploid) kromozom adıyla anılır. Bugüne kadar olan EA çalışmaları tek şerit üzerine kodlanmış genlerle gerçekleştirilmiştir. Tek şeritli yapı haploid kromozom adıyla anılır. Çift değerliliğin sağlayabileceği faydalar olmasına karşı programlama ve işlem kolaylığı sağlamasından dolayı haploid yapı tercih edilmiştir. Zamana bağlı değişimin sözkonusu olabileceği ortamlarda farklı iki çözümü barındıran diploid kromozomlar avantajlıdır. Aynı parametreyi kodlayan genlerden biri baskın diğeri çekinik olacaktır ve ortamdaki değişimle genler de baskınlık/çekiniklik özelliğini değiştirebilecektir. Çift değerlilik, gende evrim sürecinden daha hızlı değişim sağlar \[7\].

**Epistasis**

Genlerarası etkileşim epistasis adıyla anılır. Bir genin uygunluk değerine katkısı, diğer genlerin sahip olduğu değerlere bağlıdır. Epistasis çok fazla ise EA verimli olmayacaktır. Çok düşük olduğunda ise diğer yöntemlerin başarımı EA’ya göre yüksek olacaktır \[7\].

**Aldanma**

Evrim süreci işledikçe, global optimumu sağlayacak olan şemaların veya yapıtaşlarının toplulukta görülme sıklığı artacaktır. Bu optimal şemalar, çaprazlama operatörüyle, nesiller geçtikçe biraraya toplanır ve global optimum sonucu sağlar. Global optimumu bulunmasına katkı sağlamayacak şemaların görülme sıklığının artışı ıraksamaya sebep olacaktır. Bu sonuç, aldanma olarak bilinir. Aldanma için epistasis gerekli fakat yeterli değildir.

**Evrimci Algoritmaların Çalışması**

Yaratıcılarınca dahi tam olarak anlaşılamadığı halde, doğal seçim sürecine benzeşimle evrim geçirerek problem çözen bilgisayar programları \[18\] olan EA’nın iyi çalışmasını garantileyebilmek amacıyla deneye dayalı kuralların bulunmasına dönük araştırmaların sonucu ulaşılmış ve kabul görmüş bir genel teori henüz yoktur \[12\]. Yine de başarılı uygulamalar geliştirilmesinde yardımcı olan ve EA’nın başarısını kısmen izah edebilen iki ekol vardır. Sırasıyla izah edilmiş olan bu iki yaklaşım Şema Teoremi ve Yapıtaşı Hipotezi’dir \[12\]. Şema teorisinin bir özelliği de EA’nın sahip olduğu aleni ve üstü örtülü paralellik(koşutluk) özelliklerinden ikincisini açıklamasıdır. Aleni paralellik, çözüm sağlayacağı umulan birden fazla parametre kombinasyonunun işletilmesinden doğar \[19\].

**Arama Uzayında Keşif ve Keşfin Kullanımı**

Global maksimumun bulunması için etkin optimizasyon algoritmasının kullanması gereken iki teknik, arama uzayının yeni ve bilinmeyen bölgelerini araştırmak üzere yapılan keşif ve daha önce tetkik edilen noktalardan elde edilen bilginin daha iyi noktalar bulmak üzere kullanılmasıdır. İyi bir arama algoritması, çelişen iki gereklilik arasında bir denge noktası bulmalıdır.

Sade rasgele arama, keşif konusunda iyi olduğu halde keşfin kullanımı söz konusu değildir. Tepe-tırmanma yöntemi ise az keşif yapmasına karşı keşfin kullanımı konusunda başarılıdır. Bu iki yöntemin birleştirilerek kullanımı gayet verimli olabilir. Ancak, daha fazla keşif yapmaya karar vermeden önce mevcut keşfin kullanımına ne kadar süreyle devam edileceği konusunda dengenin bulunması kolay olmayabilir.

Holland göstermiştir ki EA, keşif ve keşif kullanımını aynı anda ve en uygun şekilde birleştirmektedir. Teoride doğru olmasına karşın, uygulamada, kaynağı Holland’ın basitleştirici kabulleri olan kaçınılmaz sorunlar mevcuttur. Bu kabuller:

Toplululuk nüfusu sonsuzdur.

Uygunluk fonksiyonu, çözümün işe yararlığı için doğru göstergedir.

Kromozomdaki genlerarası etkileşim bariz değildir.

Birinci kabulün, uygulamada gerçekleştirilmesinin imkansızlığına bağlı olarak EA stokastik hataya açık olacaktır. Test fonksiyonlarının nispeten kolayca sağladığı ikinci ve üçüncü kabullerin, gerçek problemlerde sağlanması daha güç olabilir \[12\].

**Kullanılabilirlik**

Geleneksel EA uygulamalarının çoğunluğu, fonksiyonların sayısal optimizasyonunda yoğunlaşmıştır. Süreksizlik içeren, çok-tepeli, gürültülü verilerin ve fonksiyonların optimizasyonunda diğer yöntemlerden daha başarılı olduğu gösterilmiş olan EA, rasgele verilerin modellenmesi için çok uygundur \[13\].

Öğrenme yeteneğine sahip sistemlere yönelik uygulamaları da olan EA’nın, ekonomik modelleme ve piyasa işlemleri \[13\] gibi belirli bir durumu analiz ederken kural tabanlı gelişim göstermesi sağlanabilir.

**Evrimci Yapay Sinir Ağları**

Yapay Sinir Ağları ve Evrimci Arama süreçlerinin ortak kullanımı ile türetilen Evrimci Yapay Sinir Ağları (EYSA), sağladığı öğrenme yeteneği olan daha etkin yapay sistemler tasarım olanağı ile ilgi görmektedir. Ayrı ayrı, çeşitli amaçlarla kullanılan bu yaklaşımların etkileşimli kullanımı konu olduğunda bahsedilebilecek uygulamalar, YSA bağlantı ağırlık değerlerinin, YSA yapısının ve YSA öğrenme kurallarının belirlenmesidir \[20, 21, 22\]. Genel çerçevesi Şekil 4.8’de verilen etkileşimli üç evrim süreciyle başarımı en iyileştirilmiş YSA tasarımı gerçekleştirilebilir. Gerçekleştirilen uygulamada, zaman serisi modellemede kullanılan YSA’ nın bağlantı değerleri geri yayınım algoritmasının yanısıra evrimci algoritma kullanımıyla belirlenmiştir.

**Şekil 4. 8 **Evrimci Yapay Sinir Ağı genel yapısı

**EYSA Bağlantı Ağırlıklarının Evrimi**

YSA’da öğrenme, denetimli veya denetimsiz gerçekleşebilir. Önceden belirlenmiş uygunluk kriteri gerçeklenmek üzere ağırlıkların ayarlanma süreci olan denetimli öğrenmede en sık kullanılan eğitim algoritması geriyayınımdır(backpropagation). Gradyan azaltarak arama yapan yöntem, YSA çıktısı ile hedef değer arasındaki

farktan doğan hatanın karesinin ortalaması veya bu ortalamanın karekökünün minimizasyonunu hedefler. Daha önce de belirtildiği üzere, çok tepeli fonksiyonlarda yerel minimum problemiyle başedemez ve türevlenemeyen fonksiyonlarla işlem yapamaz. Başarılı uygulamaları görmek ve daha detaylı bilgi edinmek için \[20, 21, 22\]’ye ve referanslarına bakılabilir.

Yerel minimum probleminin üstesinden gelmekte, uygunluk değerlendirmesi için YSA’nın hata kriteri seçilerek, evrim sürecine işlerlik kazandırılabilir. Sürecin belli başlı adımları aşağıda verilmiştir.

Kromozomların, ağırlık değeri olarak atanması

Uygunluk değerinin hesaplanması

Uygunluk değerini gözeterek çoğalma sürecinin başlatılması

Genetik operatörleri kullanarak yeni neslin elde edilmesi

Kromozomları oluşturan ağırlık değerlerinin gösterimi ve benimsenen evrim süreci, evrimci eğitim sürecinin iki ana başlığını teşkil eder. Ağırlık değerlerinin temsilinde gerçel sayılı veya iki tabanlı gösterim kullanılabilir.

**İki Tabanlı Gösterim**

Her ağırlık değeri, sabit uzunluklu bit dizisi ile temsil edilir. Kromozomlar ise bit dizilerinin biribirine eklenmesiyle elde edilir. İki tabanlı gösterim kullanıldığı durumlarda doğrudan iki tabanında kodlamanın yanısıra Gray kodu, üssel kodlama veya daha karmaşık bir kodlama kullanılabilir. Gösterimin çözünürlüğü, belirlenmeye çalışılan ağırlık değerinin hassasiyetini belirlediğinden hayati önem

taşır. Çok kısa gösterim yakınsamayı imkansızlaştırabilecekken uzun gösterim işlem yükünü ve süresini arttırır. Kullanılacak bit sayısının optimizasyonu, kodlamada kullanılacak değer aralığı, kodlama yöntemi açık problemdir \[7\].

**Gerçel Sayı Kodlamalı Gösterim**

İki tabanlı gösterimin noksanlarını gidermek üzere her bir ağırlığa karşılık bir gerçel sayı ataması önerilen yöntemde kromozomlar, değerlerin dizi oluşturacak tarzda sıralanmasıyla oluşturulur \[23, 21, 22\]. Çaprazlama işlemi, diziyi herhangi bir noktadan bölerek gerçekleşebileceği gibi genleri bölerek basamak düzeyinde de gerçekleşebilir. Ebeveynlerin ortalamasını alan çaprazlama, rasgele mutasyon ve arama uzayına özel tanımlanabilecek işlemler, genlerin uygunluk değerini arttıracak gelişimi sağlayan diğer genetik operatörlerdir. Montana ve Davis, çalışmalarında gelişime açık evrimci yaklaşımın eğitim süresinin, ilgilendikleri problem için, geriyayınım algoritmasına göre daha kısa olduğu sonucuna ulaşmışlardır \[21\]. Benzer sonuca ulaşan Bartlett ve Downs EYSA’nın boyutlarının artımıyla yakınsama süreleri arasındaki farkın evrimci algoritmalar lehine açıldığı sonucuna ulaşmışlardır. Bu sonucun genel olarak doğru olduğunun teyit edilmesi için daha fazla çalışma yapılması gerekmektedir \[21\].

**Evrimci Eğitim ve Geriyayınımlı Eğitim Karşılaştırması**

EA gibi global arama algoritmalarına dayanan ve yerel minimumlara yakalanmayan evrimci eğitim, daha önce de belirtildiği üzere, karmaşık, çok tepeli ve türevlenemeyen fonksiyonların da dahil olduğu geniş bir problem uzayına çözüm sağlayabilmesi sebebiyle caziptir. Hata fonksiyonun türevine ihtiyaç duymaması nedeniyle türevlenemeyen hata fonksiyonlarıyla karşılaşıldığında sıkıntı yaşamaz. Ayrıca, eğitilmek istenen YSA’nın türüyle ilgili kısıtlama getirmez. Algoritmik açıdan, EA’nın ve özel olarak EA’nın global örnekleme yeteneği ince ayar yapabilme yeteneğinin önüne çıkar. Üç katmanlı ve ileri beslemeli YSA’lar için belirtilen avantajlarına karşı, evrimci algoritmaların hesaplama maliyeti yüksektir \[22\].

**Hibrid Eğitim Yaklaşımı**

Evrimci eğitimin etkinliği, EA’nın global örnekleme yeteneği ve yerel arama yaklaşımının ince ayar becerisiyle birleştirilerek arttırılabilir. Yüksek uygunluk değeri vaad eden bir bölgenin bulunması için EA kullanımını takiben bölgede arama yapmak üzere yerel arama yöntemleri işletilebilir.

Belew, ağırlıkların ilk değer atamasını EA kullanarak yaptıktan sonra bulduğu yeterince iyi değerleri iyileştirmek için geri-yayınım algoritması kullanmıştır \[21\]. Sistemin başarımı, sade EA’ya ve sade geri-yayınıma göre nispeten artmıştır.

---
*Kaynak: `YAPAY SİNİR AĞLARI/YAPAY SİNİR AĞLARI.doc` — bim — 2004*
