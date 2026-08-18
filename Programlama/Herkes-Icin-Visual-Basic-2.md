# Herkes İçin Visual Basic

## **Herkes İçin**

## **Visual Basic******

## 2. Visual Basic Ortamı

## *** Tekrar Gözden Geçirme ve Bir Önbakış***

İlk derste, bir **Visual Basic Projesi’**nin önemli kısımlarını tanıdık. Bir projenin, bir **form** üzerinde, **kontrol’**ler** **kullanılarak nasıl yapılandırıldığını öğrendik.

İkinci (bu) derste; **olaylar**’ı kullanarak ve kontroller yolu ile etkileşime girerek, bizim sağladığımız talimatlar ile, istenilen hedefleri (işleri), bilgisayarın yerine getirmesini sağlayacağız.

Yine bu derste, bir **Proje**nin farklı parçalarını kullanarak, kendi Visual Basic Projelerimizi yapılandırma yolunda, başlangıç adımlarını öğreneceğiz.

Ayrıca bunların Visual Basic ortamı içerisinde birbirine nasıl uygun hale getirileceğini öğreneceğiz.

İlk derste olduğu gibi, öğrenilmeyi bekleyen pek çok yeni terim ve deneyimimiz olacak!

## Bir Visual Basic Projesi’nin Parçaları

İlk derste, bir Visual Basic Projesinin üç ana bileşeninin olduğunu gördük**: ****projenin kendisi, form ve kontroller**.

Visual Basic için** Proje **kelimesi, proje içinde bulunan her şeyi içine almaktadır. Bir **proje**yi açıklamak için kullanılan diğer terimler **uygulama **veya **program **kelimeleridir.

**Form** bir pencere olup, burada kullanıcı ile bilgisayar arasında arabirim yaratabileceğimiz bir yerdir. **Kontroller** ise grafik özellikler veya araçlar olup, kullanıcının bilgisayar ile etkileşime girmesine imkan vermek üzere form üzerine yerleştirilirler **(metin kutuları, etiketler, kaydırma çubukları, komut butonları).******

Formu çağırmak da bir kontroldür. Kontroller aynı zamanda **object(nesne)** olarak da adlandırılırlar. Şekil olarak bir proje aşağıdaki gibidir:

Özetle; **bir proje birkaç kontrol içeren bir formdan oluşur**. Bilgisayarınızda dosyaların bulunduğu dizine göz attığınızda, Visual Basic Projeleri ile ilgili bazı dosyalar gözünüze çarpacaktır.

Bir Visual Basic Projesini kaydetmek için **iki ana dosya** kullanılır.

Proje dosyası, **vbp** (dosya ismi) uzantısına sahiptir(bazen uzantısı **vbw** olan bir dosya da birlikte bulunur). Form dosyası **frm** dosya ismi uzantısına sahiptir(bazen uzantısı **frx** olan bir dosya da birlikte bulunur). Proje dizinlerinize bakın (**VB4Projeleri**, **VB5 Projeleri**, veya **VB6Projeleri**). Burada **Sample.vbp** ve **Sample.frm** dosyalarını göreceksiniz. Bu dosyalar birinci derste açtığınız projenin dosyalarıdır.

Bilmeniz gereken şey, bu dosya uzantılarının, projelerinizi uygun biçimde **açmak** ve **kaydetmek** için gerekli olduğudur.

Bir Visual Basic projesi ile ilgili önemli bir kavram ise **property(özellik)**’dir. Bir kontrol’ün (form’un kendisi de dahil olmak üzere), her karakteristiği bir **property (özellik) **ile tanımlanır. Özelliklere örnekler vermek gerekirse; **names(isimler), captions (başlıklar), sizes(boyutlar), colors(renkler), form üzerinde yerleşim ve içerikler,** bunlardan bazılarıdır.

Bu derste, üzerinde çalıştığımız her kontrolün özellikleri hakkında bilgi sahibi olmak üzere zaman harcayacağız.

Birinci derste, Visual Basic’in bir **event-driven(olay-güdümlü) **dil olduğunu öğrenmiştik. Visual Basic bir **event** **processor(olay işlemcisi) **tarafından yönetilir.

Bunun anlamı, **bir Visual Basic projesinde bazı olaylar ortaya çıkana kadar hiçbir şey olmaz**. Bir kere, bilgisayar tarafından bir olay oluştuğu fark edildiğinde, proje bu olayla ilgili bir seri talimatı bulur. Biz buna **event** **procedure (olay prosedürü)** adını veriyoruz. Bu prosedür çalıştırılır ve program kontrolü olaya geri döner:

Olay prosedürleri bizim gerçek bilgisayar programlarını yaptığımız yerlerdir ve uzantısı **frm** olan dosya içine kaydettiğimiz form ile saklanırlar. Bu **prosedürler (yöntemler),** BASIC dili **statement (bildiri)’**lerini kullandığımız yerlerdir.

Bu derste birçok programlama deneyimi ve BASIC dilini öğreneceksiniz. Öğreneceğiniz **BASIC**, Bill Gates ve Paul Allen’in **Microsoft**’u başlatırken kullandıkları ilk orijinal **BASIC** ile büyük benzerlik göstermektedir.

## Visual Basic Program’ının Parçaları

Visual Basic; bir bilgisayar programlama dilinden de öte, daha da fazlasıdır.

**Bir proje yapılandırma ortamıdır.** Bu ortam içerisinde **projemize başlayabilir****,**** yapılandırabilir****, ****çalıştırabilir, test edebilir****, ****projemizde (eğer varsa) hatalarımızı ayıklayabilir ve ileride kullanmak üzere projemizi kaydedebiliriz****.**

Diğer bilgisayar dilleri ile, programınızı yazmak için, ayrı bir **Metin Editör’**üne, programınızı yaratmak için **compiler(derleyici)** adı verilen ayrı bir programa ve programınızı **test etmek için ayrı bir alana **ihtiyaç duyarsınız.

Visual Basic ise, proje oluşturma (yapılandırma) işleminin her adımını **bütünleştirerek,** hepsini tek bir ortamda gerçekleştirir.

Visual Basic ortamının parçalarına bir gözatalım.

## ***Ana Pencere***

Birinci derste öğrendiğiniz prosedür ile Visual Basic’i çalıştırın. Ekranda birkaç pencerenin birden açıldığını gözlemleyin. **Ana Pencere, **Visual Basic Projesinin pek çok amacını kontrol etmek ve **çalıştırma(run)** işlemini gerçekleştirmek için kullanılır.

## **VB4:**

## **VB5:**

## **VB6:******

***Ana pencere*****, **** başlık çubuğu, menü çubuğu ve araç çubuk’**undan** **oluşur.

Ufak boyuttaki başlık çubuğu; proje ismini ve **o anki çalışma modunu** (**dizayn, break **

**(ara verme) veya çalışma (run))** gösterir.

Menü çubuğu üzerinde bulunan **drop-down menu(çek menü)’**lerden, Visual Basic ortamının işlemlerini kontrol ederiz.

Bu menü seçeneklerinden bazılarına kısa yol oluşturmak üzere, araç çubuğu üzerinde bazı butonlar bulunmaktadır. Birinci derste, bir projeyi açmak, çalıştırmak ve durdurmak için kullandığımız butonlara bakınız.

## ***Form Penceresi***

**Form Penceresi, **Visual Basic uygulamaları geliştirmenin ‘**kalbi**’dir. Sizin uygulamanızı geliştirdiğiniz yerdir:

Eğer bu form ekran üzerinde görünmüyorsa:

**VB4**: Ana menü’den **View**, daha sonra da **Form** seçeneğini tıklayın.

**VB5, VB6**: Ana menü’den **View**, daha sonra da **Object** seçeneğini tıklayın.

Bir alternatif olarak, eğer pencere görünmüyorsa, <**Shift**> tuşunu basılı tutarken, **F7** fonksiyon tuşuna basınız.

## ***Araç Kutusu Penceresi***

**Araç Kutusu Penceresi(Toolbox Window** ),uygulamalarınızda kullandığınız kontroller için **bir seçim menü’**südür. Birçok kereler, kontrollerden **tools(araçlar) **olarak söz edilir. Kısaca, kontrollerden söz etmek için üç değişik kelime kullanılır **: object(nesne), tool(araç) **ve en çok kullanılan olarak **control(kontrol)**.

VB4:

VB5, VB6:

Eğer toolbox(araç çubuğu) ekranda görünmüyorsa, ana menüden önce **View** daha sonra da **Toolbox **seçeneğini tıklayın. Birinci derste, **Sample** projesi ile tanımladığımız kontrolleri inceleyin.

## ***Properties(Özellikler) Penceresi*********

**Properties Penceresi, **kontroller için başlangıç özellik değerlerini vermek üzere kullanılır. Pencerenin en üstünde yer alan **drop-down box (çek kutu),** o anki form üzerinde bulunan bütün kontrolleri listeler. Bu kutu altında halihazır seçilmiş nesneye ait uygun özellikler mevcuttur.

VB4:

VB5, VB6:

** **İki şekilde görüntülenebilir : **Alphabetic (Alfabetik)** ve **Categorized (Sınıflandırılmış)**. Biz daima **Alfabetik** olanını kullanacağız.

Eğer ekranda **properties penceresi** görünmüyorsa :

** VB4**: Ana menü’den **View**, daha sonra da **Properties** seçeneğini tıklayın.

**VB5, VB6**: Ana menü’den **View, **daha sonra da **Properties Window **seçeneğini

## ** **tıklayın.** ******

Bir alternatif olarak, eğer **properties penceresi** ekranda görünmüyorsa, **F4** fonksiyon tuşuna basınız. Properties penceresi daima form ve onun kontrolleri ile birlikte göründüğünde ortaya çıkar.

## ***Proje Penceresi***

**Proje Penceresi** hangi formun projenizi oluşturduğunu gösterir. Daha tecrübeli bir Visual Basic programcısı olduğunuzda**, ****birden fazla sayıda form’dan oluşan projeleri** nasıl oluşturacağınızı öğreneceksiniz. Böylesi bir durum için projenizdeki bütün formlar bu pencerede listelenecektir. Aynı zamanda ekranda proje penceresinde görünen butonlardan birisini tıklayarak **Form Penceresi **veya **Code(Kod) Penceresi’**ni (gerçek BASIC

kodlamasının göründüğü pencere) göreceksiniz. Kod penceresini diğer derste göreceğiz.

VB4:

VB5, VB6:

Eğer ekranda **project (proje) penceresi** görünmüyorsa :

** VB4**: Ana menü’de **View**, daha sonra da **Project** seçeneğini tıklayın.

**VB5, VB6**: Ana menü’de **View** daha sonra da** Project Explorer **

seçeneğini tıklayın.** ******

**Bir alternatif olarak,** eğer **project (proje) penceresi** ekranda görünmüyorsa, <**Ctrl**> tuşunu basılı tutarken **R** tuşuna basınız.

Eğer bu pencerelerden herhangi birisi ekrana gelmezse; onların nerede olduğunu ve onları nasıl yerleştireceğinizi biliyor olmalısınız. Ayrıca, artık bu pencereleri de tanıyorsunuz. Bir sonraki seferde, birinci derste kullandığımız projeyi, burada işlediğimiz bazı konuları değerlendirmek üzere, tekrar ziyaret edeceğiz.

## ***Visual Basic İçinde Bir Tur***

## ***Proje Penceresi***

1. ders’te kullandığımız **Sample** adlı projeyi tekrar açın. **Project** penceresine gidin ve inceleyin.

VB4:

VB5, VB6:

Proje penceresi; **Sample.vbp** isimli bir proje dosyasının kaydedildiğini ve projenin bir adet **Sample.frm **adlı bir proje formuna sahip olduğunu göstermektedir.

Burada fark etmeniz gereken şey, formun **frmSample **adı ile anılmasıdır. **Properties** penceresini hatırladınız mı ? Bir kontrole atadığımız en önemli özelliklerden birisi, onun **Name(isim)**’inin**,** ‘**frmSample’**, yani formumuzun isim özelliğinin bu olmasıdır. Bizler kontrollere daima** isim özellikleri(property) **ile değiniriz.

Yani, **onlara nasıl bir isim verileceği konusu kritik bir konudur** (bu konuda, gelecek derste, birçok şeyden bahsedeceğiz). Proje penceresinde, listelenmiş isim vermek, son derece önemlidir.

## ***Properties(Özellikler) Penceresi***

Şimdi **Properties(Özellikler) **penceresine** **bakalım: Hatırlayın, bu sadece form görüntüye geldiğinde ortaya çıkar. Böylece, sizin ilk yapacağınız şey, öncelikle formun görüntüye geldiğinden emin olun. İstenilen pencereleri nasıl ekrana getireceğiniz konularını gözden geçiriniz.

VB4:

VB5, VB6:

**Properties(özellikler) Penceresi’**nin en üstünde bulunan çek kutusu **control** **list(kontrol listesi)** olarak adlandırılır. Projede kullanılan her kontrol tipinin ne olduğu kadar, ismini (isim özelliğini) de gösterir. Dikkat edin, şekilde göründüğü gibi, şu anki kontrol **Form** ‘dur ve ismi de **frmSample**’dır.

İlgili özelliklerin listesi bu kutunun altındadır. Bu listede**, seçilen kontrol için,** sıralanmış özellikleri kaydırarak (kaydırma çubuğunu kullanarak) inceleyebilir veya değiştirebilirsiniz. Özelliklerin isimleri listenin solunda yer alırken, şu anki geçerli özelliklerin değerleri ise sağ tarafında yer almaktadır. Form için sıralanan özellikleri kaydırarak inceleyin.

Gördünüz mü, kaç tane özellik var ?

Bunların birçoğunu derslere devam ettikçe öğreneceksiniz.

Kontrol listesindeki aşağı oku tıklayın(hatırlayın bu özellikler penceresinin en üstündeki çek-kutudur).

VB4:

VB5, VB6:

Form üzerinde bulunan bütün kontrollerin görünen listesini kaydırın. Bu kontrollerden pek çoğunu burada göreceksiniz. Bunlara atanan isimlere, kontrol tiplerine ve hangi isimlerin hangi kontrolleri tanımlamak için kullanıldığına dikkat edin. Örnek olarak **imgTrike** üç tekerlekli bir bisikletin resmini tutan bir **image control** ’ü olarak kullanılmıştır.

**Kontrollere uygun isim vermenin mantığı budur, yani bir kontrolü yalnızca isminden tanıma veya tanımlama mantığıdır.** Daha evvel sözünü ettiğimiz gibi, daha sonraki bölümlerde, kontrollere isim verme konusunda pek çok şeyden bahsedeceğiz.

Bir kontrol seçin ve bu **kontrol’ün property(özellikler)** bilgilerini gezinin. Değişik birkaç kontrol için, bunların özelliklerine bakın. Her kontrol başlı başına pek çok **property (özellik)**’e sahiptir. Pek çok **property(özellik)** değeri, **default(varsayılan)**

olarak, Visual Basic tarafından verilmiştir. Bizler bu varsayılan (default) değerleri, kendi kullanımımız için gerekli uygun değerler ile değiştireceğiz. Bu property (özellik)’lerini nasıl değiştireceğimiz konusuna üçüncü derste bakacağız.

## ***Kod Penceresi(Code Window)*********

Yeni pencereye bakalım. Tekrar hatırlayalım, Visual Basic **event-driven (olay- güdümlü)**’dür ve bir olay fark edildiğinde, **project(proje)** doğru **event** **procedure(olay prosedür)’**üne** **gider. **Olay Prosedürler**, Bilgisayara, bir **event(olay)**’a ne cevap vermesi gerektiğini söyler. Bunlar gerçek bilgisayar programlamasının (BASIC dili kullanılarak) olduğu yerlerde olur. **Code** **Window (Kod Penceresi)’**ndeki olay prosedürlerine bakalım. Kod penceresini göstermenin pek çok yolu vardır. Bir yolu, proje penceresinde bulunan uygun butonu bulmaktır. Bir diğeri ise Ana Menü’de bulunan **View** ve daha sonra **Code **seçeneklerini tıklamaktır. Veya bir alternatif olarak, **F7** fonksiyon tuşuna basınız. **Sample** projesi için kod penceresini bulunuz.

VB4:

VB5, VB6 :

Kod Penceresinin en üstünde iki tane yan yana kutu vardır, **object(nesne) (veya kontrol) listesi** ve **prosedür** **listesi**. Nesne listesi, özellikler(properties) penceresinde bulunan liste ile benzerdir. **Form üzerinde bulunan bütün nesneleri, isimleri ile listeler.**

Bir nesne veya kontrol için, listede bir isim seçilmişse, prosedür listesi bu kontrol için mümkün olan bütün **olay prosedür’leri(event procedures)**’leri** **gösterir. Görüldüğü gibi, kod penceresi, **Form** kontrolü için **Load** olay prosedürü göstermektedir. (Eğer nesne listesinde Form Kontrolü seçili değilse, aşağı-sürükle okunu tıklayarak **Form** kelimesi çıkana kadar kaydırın ve bunu seçin.).

Proje ilk olarak bilgisayara yüklendiğinde**, load(yükle)** **olayı** olur. Nesne ve prosedür liste kutuları altında bu olay prosedürü için gerçek BASIC kodları yer almaktadır.

Bu kod muhtemelen şimdi size bir yabancı dil gibi görünebilir fakat endişelenmeyin – anlayacaksınız ! Takip eden derslerde, BASIC öğrenmeye başlayacaksınız ve böylesi kodları okumak size çok kolay gelecek.

Prosedür liste kutusunun yanındaki aşağı-sürükle okunu tıklayın. Form kontrolü için bütün diğer olay prosedürlerine dikkat edin. Şanslıyız, çünkü bütün bu prosedürler için BASIC kodu yazmak zorunda değiliz. **Yalnızca projemiz çalışırken (run) olmasını beklediğimiz olaylar için kod yazacağız.**

Nesne listesinde aşağı-çek okunu tıklayın. **optBlue** ‘yu nesne olarak seçin.

VB4:

VB5, VB6:

** ****optBlue** isimli kontrol için olay prosedürü **Click ‘**dir. Eğer hiç BASIC bilmiyorsanız bile, burada neler olduğunu çıkartmaktasınız. Kontrollere isimler verirken dikkatli olduğumuzdan, fark etmeniz gerekir, bu kontrol bir option (seçenek) butonudur

(ufak daireli olan) ve onun yanında **Blue** kelimesi yer almaktadır (seçenek butonunun yanınadaki kelime onun **Caption(Başlık) **özelliğidir). Yani, bu olay prosedürü, biz ne zaman Blue seçenek buttonunu tıklarsak çalışır. Prosedür, yalnızca bir satırdan oluşan bir talimata sahiptir (ilk ve son satırları şimdilik bir kenara bırakın) :

## **frmSample.BackColor = vbBlue******

Bu BASIC kod’u satırı,** frmSample **adı verilen kontrolün **BackColor** **property (özellik)**’inin mavi renge ayarlanmasını söylemektedir (**vbBlue** kelimesi ile temsil edilen).

Kolay değil mi ? Gerçekten de, çoğunluk BASIC kodları kolay anlaşılır.

Nesne listesinden diğer nesneleri seçin ve karşılık gelen olaya, BASIC koduna bakın. Kodun en üst satırından başlayın (ve yine, en üstte yer alan başlık satırını göz önüne almayın) ve çalışın.

Hiç BASIC bilmemenize rağmen neler olup bittiğini anlayabiliyormusunuz ?

Düşüncem, sizin pek çok durumda yapabileceklerinizi, kendinizin bulacağı yönündedir. BASIC kodu yazmak, temelde, pek çok detaya dikkat etmektir. Pek çok kısmı için çok mantıklı ve açıktır. Ve, şimdi artık kendi kodunuzu yazmaya başlayabilirsiniz!

Özetle;

Bu ikinci derste, Visual Basic Ortamının parçalarını ve bu ortam içerisinde nasıl hareket edeceğimizi gördük. Aynı zamanda **properties (özellikler) **ve **event** **procedures (olay prosedürleri) **gibi bazı önemli terimleri öğrendik. Şimdi artık ilk Visual Basic projenizi yapılandırabilecek durumdasınız. Diğer derste, bir form üzerine kontrolleri nasıl yerleştireceğinizi, onlarla nasıl hareket edeceğinizi ve onların nasıl olmasını istiyorsanız, o şekilde hazırlamayı öğreneceksiniz. Event Procedure(Olay Prosedürler)’e nasıl BASIC kodları koyacağınızın bütün önemli adımlarını hep birlikte öğreneceğiz !

## ** PAGE 20**

## *** *****Herkes için ****VISUAL BASIC\_\_\_\_\_\_\_ **

## \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## ***VISUAL BASIC ******ORTAMI*** ** PAGE 20******

## PAGE 12 PAGE 7

## ***Olay İşlemcisi***

## ***Kontrol***

## ***Kontrol***

## ***Form***

## ***Kontrol***

## ***Kontrol***

## ***Proje***

## ***Olay**** ?*

## ***Olay***

## ***Prosedürü*********

## ***Olay Prosedürü***

## ***Olay***

## ***Prosedürü*********

***OLE ( Nesneyi Bağlantılama ve Dahil Etme )***

***Horizontal Scroll Bar ( Yatay Kaydırma Çubuğu)***

***Image( Görüntü )***

***Shape( Şekil)***

***Directory( Dizin)***

***Timer ( Zamanlayıcı)***

## ***Combo Box ( Birleşik Kutu)***

## *** Check Box ( Onay Kutusu)***

## ***Frame (Çerçeve)***

## ***Label (Etiket)***

## ***Pointer ( İşaretleyici)***

***Common Dialog Box (Ortak***

*** Diyalog ***

*** Kutusu)***

## ***Data Control (Veri Kontrol’ü)***

## ***Line (Çizgi)***

## ***Files (Dosya Liste Kutusu)***

***Drive (Sürücü Liste Kutusu)***

***Vertical Scroll Bar (Dikey Kaydırma Çubuğu)***

## ***List Box (Liste Kutusu)***

***Option Button (Seçenek Butonu)***

***Command Button (Komut Butonu)***

## ***Text Box (Metin Kutusu)***

## ***Picture Box (Resim Kutusu)***

***OLE ( Nesneyi Bağlantılama ve Dahil Etme )***

***Image( Görüntü*** )

***Shape( Şekil)***

***Frame (Çerçeve)***

***Combo Box ( Birleşik Kutu)***

***Timer ( Zamanlayıcı)***

***Horizontal Scroll Bar ( Yatay Kaydırma Çubuğu)***

***Check Box ( Onay Kutusu)***

***Pointer ( İşaretleyici)***

*** Label (Etiket)***

***Data Control (Veri Kontrol’ü)***

***Vertical Scroll Bar (Dikey Kaydırma Çubuğu)***

***List Box (Liste Kutusu)***

***Option Button (Seçenek Butonu)***

***Command Button (Komut Butonu)***

***Text Box (Metin Kutusu)***

***Picture Box (Resim Kutusu)***

***Drive (Sürücü Liste Kutusu)***

***Directory( Dizin)***

***Line (Çizgi)***

***Files (Dosya Liste Kutusu)***

***Çek liste ***

***kutusu ***

***Çek liste***

*** kutusu*********

## ***Kontrol listesi***

## Prosedür Listesi

## Nesne Listesi

## Nesne Listesi

## Prosedür Listesi

---
*Kaynak: `HERKES İÇİN VISUAL BASIC/BOLUM-2.DOC` — M. ŞAKİR UNUTUR — 2001*
