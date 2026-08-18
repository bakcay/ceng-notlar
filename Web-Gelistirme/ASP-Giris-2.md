# ASP Giriş 2

ASP sayfaları web sunucusu altında çalışan, içindeki scriptler sayesinde aktif olarak web sayfası oluşturan ve oluşturduğu sayfayı sunucuya bağlanmış olan internet browser' ına gönderen interaktif sayfalardır. Internet ortamında çalıştığı için herkesin aşina olduğu aşağıdaki temel elemanları kullanır:

ASP, 1996 yılının Kasım ayında Microsoft’un bir Active Platform dizaynını açıklaması ile doğdu. Active Platform, Microsoft’un bir masaüstü bilgisayar ile bir server bilgisayarın nasıl haberleşmesi gerektiği konusundaki fikirlerini yansıtmaktadır. Active Desktop ve Active Server olarak iki bölümden oluşur. Active Desktop client tarafını ya da HTML sayfalarının bir web browser üzerinde izlendiği kullanıcı tarafını temsil etmektedir. Active Server ise server tarafı componentini temsil etmektedir. Server tarafından işlenen sayfalar da Active Server Pages adını almaktadır.

Microsoft’un dökümanları ASP’yi “dinamik, interaktif, yüksek performanslı Web server uygulamalarını yaratıp çalıştırmak için kullanabileceğiniz bir server tarafı scripting ortamı” olarak tanımlamaktadır. ASP dosyaları sade HTML dosyalarının verebileceğinden çok daha yüksek seviyede interaktiflik sağlayabilmek için HTML’i, scriptleri ve ASP kodlarını birleştirmektedir. ASP ile Windows NT üzerinde çalışan programcılar dışarıdan gelen bilgileri temel alarak sayfalarının nasıl görüntüleneceğini düzenleyebilirler. Her hafta farklı bir resim veya kullanıcının yaşına göre bilgi gösterilebilir. *Durum dallanması* *(Condition Branching)* olarak adlandırılan bu işlem ASP’ye belirli durumlar karşısında ne göstereceğine karar verme olanağı sağlamaktadır.

Diğer yanda HTML’in bunu yapmak için hiç bir şansı yoktur. Çünkü HTML sadece gösterme amaçlı bir dildir. Gerçek hayatta genellikle kullanıcılarınızın tecrübelerine bağlı olarak farklı içeriklere sahip olan sayfalar sunmak isteyeceksiniz. Bunun için önce karar verme yeteneğine sahip olmanız lazım.

**DOSYALAR NASIL İŞLENİR?**

Normalde HTML dosyaları client tarafında (yani kullanıcının web browserında) işlenmekedir. Microsoft’un Active Server Platform’u sayesinde artık server tarafı da dosyaları işleyebilecektir. Burada server’ın işlemesinden kasıt bir dosyanın kullanıcının browser’ında gösterilmeden önce server tarafından bazı temel adımların tamamlanmasıdır:

|  | Dosyanın uzantısına bakar. Eğer dosya *.html* ya da .*htm* gibi standart bir uzantıya sahipse server dosyayı browser’a gönderir. Eğer dosya .*asp* (ya da .*asa*) gibi bir uzantıya sahipse server dosyayı açar ve içinde ASP kodunu belirten tag’ları aramaya başlar. ASP kodu özel tag’lar dahilinde yazılır; "<%" kodun başlangıcını," %>" ise kodun bitişini gösterir. |
| --- | --- |
|  | Server bu işaretlerin dahilindeki kodu işleme koyar ve onun yerine HTML kodu yazar. Bu HTML kodu kullanıcının ayarları ile bilgiye ya da client tarafındaki diğer durumlara dayanmaktadır. |
|  | Sonuç olarak kendi orijinal ve ayrıca ASP tarafından üretilen işaretleri taşıyan sayfa kullanıcının browser’ına gönderilir. |

Bir alışveriş kartı örneğini ele alalım. Bir müşterinin mağazanın kataloğundan 5 tane malzemeyi seçtiğini farzedelim. Bu seçimler satır sütunları olan bir tablo içeren bir alışveriş kartı sayfasında listelenecektir. Her sütunun en üstünde örneğin miktar, stok numarası ya da fiyat gibi bir başlık olacaktır. İçeriği müşterinin ne seçtiğine bağlı olarak değişen bu sayfayı nasıl dizayn etmeyi düşünürdünüz?

Sütun başlıkları değişmeyeceği için onlar orijinal HTML kodunun içine yerleştirilebilir. Tablonun pozisyonu da büyük ihtimalle değişmeyeceği için o da HTML dosyasına dahil edilebilir. Sayfaya ne kadar geri dönüp tekrar izlesenizde bunlar değişmeyecek olan değerlerdir.

Ancak tablonun içi alışveriş için kullanıcının ne seçtiğine bağlı olarak değişecektir. Siteye giren herkes değişik malzemeler seçebilir. Bunu gösterebilmek için ASP bilgileri bir database’den çeker ve kullanıcaya gönderilmeden önce bunları HTML kodunun içine gömer. Programcılar bu tür sayfaları “*on the fly*” olarak tanımlıyorlar çünkü gerçekte böyle bir sayfa yok. Bunun yerine gerektiğinde istek üzerine (on the fly) oluşturuluyor. ASP scripti statik sayfa elemanları ile database’den seçilen bilgileri birleştirerek safyanın tamamını oluşturur.

**ASP’ Yİ GENİŞLETMEK İÇİN SCRIPT KULLANMAK**

VBScript, JavaScript ve JScript bir HTML dosyasına eklendiğinde görüntü üzerinde değişikliklere olanak sağlayan scripting dilleridir. Bu diller genellikle client tarafında çalıştırılırlar yani başka bir deyişle kullanıcının browser’ı tarafından işletilirler.

Ancak bazı ciddi dezavantajları mevcuttur:

- Browser’a özeldirler. Yani aynı kod browser’a bağlı olarak farklı çalıştırılabilirler.

- Bir database ile ilişki (ürün kataloğu gibi) kuramazlar ve bilgi saklayamazlar.

Bu dezavantajlarına rağmen scripting dilleri kullanışlı olabilirler. Muhtmelen en iyi kullanılabilecekleri alan bilgi onaylamaktır (*data validation*). Mesela server’ a işleme konması için gönderilmeden önce bir giriş formu üzeinde eksik alan olup olmadığının kontrol edilmesi gibi. Bu gönder düğmesine basıldığı zaman çalışan bir script sayesinde gerçekleştirebilir. Fonksiyon formun bütün alanlarını kontrol edecek ve eğer bir alan boş bırakılmışsa kullanıcıyı bilgilendirecek şekilde bir hata mesajı gönderecektir.

Scriptler server tarafında da kullanılabilir ama genellile kullanıcı tarafında kullanılırlar. SCRIPT tag’ının bir özelliği sayesinde programcı kodun nerede çalışacağını tayin edebilir. Default olarak kod client tarafında işleme konur ancak bunu değiştirmek programcının elindedir.

**COMPONENTLER VE OBJECTLER (BİLEŞENLER VE NESNELER)**

Componentler ve objectler server’ın ortamı ve sistemi ile haberleşmek için kullanılan araçlardır. Bir component bir ya da birden fazla object’i içerebilir. Ve bir object de bir ya da daha fazla metod ve bir ya da daha fazla özellik (properties) içerebilir. (Metodları dilbilgisindeki fiiller özelikleri de sıfatlar olarak düşünebilirsiniz). Bir object’in bir örneğini (instance) yaratarak görevleri yapmak için metodlarını kullanabilirsiniz. Bir object’in özelliklerini değiştirmek metodlarının görevleri farklı icra etmesine sebep olur.

Bazı objectler ASP, bazıları VBScript ve bazıları da server sisteminin içine gömülmüştür. Bir uygulamayı daha rahat geliştirmek için başka componentler de yaratılabilir.

| **Ortak Componentler ve Objeler****** |  |  |
| --- | --- | --- |
| **Object / Component****** | **Fonksiyonu****** | **Kaynak****** |
| Request Object | Browser’dan gelen istekleri düzenler | ASP içine gömülmüş |
| Response | Browser’a gönderilen bilgiyi düzenler | ASP içine gömülmüş |
| Server Object | Bazı temel server servislerine erişimi sağlar | ASP içine gömülmüş |
| Application Object | Bir uygulamanın yaşamı için bilgileri düzenler | ASP içine gömülmüş |
| Session Object | Bir session’ın yaşamı için bilgileri düzenler | ASP içine gömülmüş |
| Text Object | Text dosyalarını kullanır | VBScript scripting object |
| Error Object | Hata analizi sağlar | VBScript scripting object |
| Dictionary Object | Lookup referans oluşturur | VBScript scripting object |
| File System Object | Dosya sistemlerine erişim sağlar | VBScript scripting object |
| Content Linking | Sitedeki sayfalara bir düzen verir | Server Component |
| Browser Capabilities | Browser’ının ne yapabileceğini belirler | Server Component |
| Ad Rotator | Sayfa üzerinde bir noktada reklamları döndürür | Server Component |
| Voting | Kullanıcı havuzundan bilgi toplar | Server Component |
| Active Database | Bir database ile iletişim kurar | Server Component |

**MUHTEMEL DEZAVANTAJLAR**

ASP dinamik web içeriği için kuvvetli bir araç olmakla beraber diğer çözümler gibi onun da bazı dezavantajları mevcuttur. ASP sadece Windows NT ve 95 içinde çalışır. ASP kullanmak için bir Microsoft web server’ına (genellikle Internet Information Server) ihtiyaç duyulur. Diğer sunumcularda ASP için Chili!ASP adlı ürünü kullanmak gerekir. Ayrıca ASP cookie kullanmaktadır. Bu da Lynx kullanan kullanıcıların sayfalara erişememesi demektir. Gerçi günümüzde Lynx kullanan kullanıcıların sayısı oldukça az ve hedef kitlenin büyük bir kesimine hitap etmemektedir.

Durumunuza ve ihtiyaçlarınıza bağlı olarak ASP sizin için en iyi çözüm olabilir. ASP’nin piyasada şu an rekabet halinde bulunduğu diğer rakibinin adı Cold Fusion’dır. Allaire Grubu tarafından yaratılan Cold Fusion da sizin Access ve SQL Server gibi database’lere erişmenize olanak vermektedir. Bunun yanında Cold Fusion’ın tagları biraz kafa karıştırıcı ve hata ayıklaması biraz daha zor olabilir ve bazı kullanıcılar bellek problemleri ile karşılaşmışlardır

**Mevcut teknolojiler**

Başlangıçtan beri web sayfalarından veritabanına erişim için çeşitli standartlar ortaya çıkmıştır. Bu teknolojiler gün geçtikçe ilerlemekte ve daha kapasiteli hale gelmektedir. Yapısal olarak iki sınıfa ayırabiliriz.

*1. Push Web Page Teknolojisi:***

Statik web sayfaları kullanıcının etkileşimi ile değişmezler. Statik web sayfaları push teknolojisi olarak bilinen bir teknoloji ile oluşturulur. Push web page teknolojisinde önce sayfalarınızı yaratırsınız. Daha sonra bunu webserver üzerindeki bir dizine yüklersiniz. Daha sonra web server bunları Statik web sayfası haline getirir. Eskiden beri birçok site bu yöntemle yaratılmıştır. Bu siteler dataya dinamik olarak erişime izin vermezler. Push teknolojisi yaygın olmasına rağmen hızla gelişen Pull teknolojisi yavaş yavaş onun yerini almaktadır.

*2. Pull Web Page Teknolojisi:***

Pull teknolojileri SQL server’a yapılan bir query’nin karşılığı olarak dinamik olarak web sayfalarının inşa edilmesini sağlar. Bu query bir sorguyu oluşturan opsiyon kümesinden veya datayı güncelleyen standart Transact-SQL ifadeleri şeklinde olabilir. Bu erişim değişik teknikler sayesinde olur.

Microsoft Internet Database Connector (IDC) dosyaları

ActiveX Data Object (ADO)’lu Microsoft Active Server Pages (ASP)

Microsoft Remote Data Services (RDS) (eski Advanced Data Connector-ADC)

*3. SQL Server’a Diğer Erişim Metodları:***

Microsoft’un şu anki yaklaşımına göre en iyi erişim metodu ADO’dur. ADO, OLE-DB uyumlu veritabanlarını sorgulamak için kullanılan erişim metodur. Siz Active Server Pages (ASP) scriptlerinizi yazarsınız, bunlar Internet Information Server (IIS) 3.0 ve daha yukarısı versiyonlarında işlenir ve kullanıcının web browser’ına gönderilir. ADO’ya yapılan çağrılar Microsoft’un VBScript programlama dili gibi server-side script ile yazılır. Sonuç olarak kullanıcıya gönderilen normal HTML kodu olduğundan karşı tarafta herhangi bir web client kullanılabilir.

Veritabanlarına ADO ile erişim, IDC dosyaları kullanarak erişime oranla çok daha kuvvetlidir ancak bunun yanında bir o kadar daha kompleksdir. ADO database erişiminiz için kodlamayı ASP dosyaları içinde yapabilir veya SQL Server' a çağrıda bulunan ayrı DLL’ler ve çalışabilir programlar şeklinde ActiveX kontrolleri yaratabilirsiniz. Bu ActiveX kontrolleri Microsoft Transaction Server’ın bir parçası olarak da çağırılabilir. Bütün bu teknolojileri ve beraber nasıl çalıştıklarını anlamak biraz zaman alabilir.

Son olarak; Microsoft Remote Data Services (RDS) olarak adlandırılan bir teknolojiye sahiptir. Bu teknoloji daha önce Advanced Data Connector (ADC) olarak biliniyordu. Bu teknoloji de veritabanlarını sorgulamak için ADO’yu kullanmaktadır ancak ActiveX kontrollerini kullanarak sizin client Web browserınız üzerinde çalışır. Bu yüzden Web browserınız ActiveX kontrollerini desteklemelidir.

**Uygulama Ortamları ve Alternatifler**

Web sayfanızı veritabanı ile ilişkilendirmek için bir çok alternatif vardır. Bunlar çok güçlü olmayan basit çözümlerden kullanılması güç olan çok kuvvetli araçlara kadar olan geniş bir yelpazeye sahiptir.

**Şekil 2.1.** Alternatiflerin karşılaştırılması

Yukarıdaki şekil iki koordinattan oluşmaktadır. Yatay eksen araçların özelliklerinin yeteneklerini alçaktan-yükseğe olacak şekilde derecelendirerek ölçmektedir. Dikey eksen kullanım kolaylığını gösterir ve alçaktan - yükseğe olacak şekilde derecelendirilmiştir. Her aracın matrixdeki pozisyonunu bulmak için iki eksende de karşılaştırılması yaparak değerlendirilmiştir. (Kaynak: Morrison M. “Special Edition Using Microsoft Visual Interdev” Macmillan Publishing, USA \[1997\])** **Karşılaştırmadan da görebileceğiniz Visual Interdev .ok güçlü ve kullanımı kolay bir araçtır. Java programları ve appletleri platformlar arasında geçiş yapabilme özelliklerinden dolayı yetenek ekseninde Visual Interdev’den daha yüksek bir dereceye sahiptirler. Fakat aynı araçlar kullanım kolaylığı ekseninde ise Java programlama dilinin doğasından ötürü daha düşük değerler almaktadır.

Java, C++ benzeri bir dildir ve Visual Interdev ile karşılaştırıldığında çok kompleks kalmaktadır. Ayrıca Visual Interdev’de görsel olarak SQL sorgulamalarınızı oluşturabileceğinizden Visual Interdev’deki veritabanı araçlarının kullanımı çok kolaydır.

Visual Interdev hem web sayfası hemde uygulamalarımız için database çağrılarını oluşturmak amacıyla tek ortam sağlaması yeteneğiyle yüksek not almakatdır. IDC (Internet Database Connector) gibi daha önceki database çözümlerinde; SQL bilgilerinizi ve çağrılarınızı idare etmek için bir dosya ve HTML sayfası işlemek için ayrı bir dosya yaratmak gerekiyordu.

API, programlama yetenek ekseninde yüksek skorlar elde etmektedir ancak kullanılması diğer çözümlerden daha zordur. CGI sevenler ise karşılaştırma matrixinde CGI’ın derecesini görünce üzüleceklerdir. CGI veritabanı ilişkilendirme çözümü olarak kullanılmaya devam edecek ancak server bağlantılarının performansını arttıran API’lerin geliştirilmesi ve veritabanı uygulamamızı geliştirmek için harcadığımız süreye görsel araçların getirdiği kolaylıkların eklenmesinden sonra, CGI artık eski bir teknoloji sayılacaktır.

**VISUAL INTERDEV**

Visual Interdev’i diğer database bağlantı araçları ile karşılaştırdıktan sonra şimdi de Visual Interdev’in içerdiği bazı spesifik özelliklerden bahsedelim. Uygulamınızı geliştirmek için tam bir geliştirme ortamına sahip olmanın getirdiği avantajlar küçümsenemez. Yukarıda web-database bağlantı karşılaştırma matrixinde belirtilen bazı araçlara tanıdık olabilirsiniz. Bu çözümlerin bir çoğunda database bağlantısı sağlamak için ayrı geliştirme ortamı ve araçları kullanmak zorunda kalırsınız. Visual Interdev aşağıdaki özellikleri ve avantajları içeren tam bir geliştirme ortamı sunmaktadır :

*Kullanım Kolaylığı*** ******

Visual Interdev bir çok veritabanı aracını bütünleşik bir çatı altında toplayan benzersiz bir ortam sunmaktadır. Bundan dolayı Visual Interdev’in kullanımı çok kolaydır. Veritabanı bağlantınızı SQL çağrılarınızı ve HTML web sayfalarınızı oluşturmak için farklı araçlar ve ortamlar arasında geçiş yapmanız gerekmemektedir. Ayrıca Visual Interdev web sayfalarınıza database fonksiyonelliği ekleme süreci esnasında size toolbar' lar ve menu optionlarla rehberlik etmektedir.

*Görsel Ortam*** ******

Adından da anlaşılacağı gibi Visual Interdev uygulamalarınızı oluşturmak için size görsel bir ortam sağlar. Bu görsel ortam Visual Data Tool’ larını içermektedir. Bu araçlar SQL ifadelerinizi görsel olarak oluşturmanıza ve anında test etmenize imkan tanımaktadır. Sorgulamanızı oluşturabilmek için SQL detaylarını bilmenize hiç gerek yoktur. Kuvvetli SQL programcıları içinse araçların doğal görsel ortamı onların rutin sorgulamaları yazarken kaybettikleri zamandan tasarruf edip bu kazanılan zamanı daha kompleks SQL sorgusu yazarken harcamaya fırsat tanıyacaktır.

*RAD (Rapid Application Development)*** ******

Visual Interdev uygulamanızda hızlıca database ilişkisi oluşturmanızı sağlayan görsel bir ortam sağlar. Modern çağın gereksinimi olarak her zaman anında bilgiye ihtiyaç duyulmaktadır. Visual Interdev hem PC masaüstü hemde server databaselerinin her ikisini de destekleyerek RAD’ın arkasındaki teoriyi desteklemektedir. Database araçları uygulamanızı MS SQL Server gibi daha güçlü database programlarına geçirirken de kullanabileceğiniz ODBC uyumlu SQL çağrıları oluşturmanıza olanak verir.

*Etkinlik*

Buraya kadar Visual Interdev’in sağladığı kolaylıklardan bahsettik. Bazıları bu kadar kolaylık sağlayan bir uygulamanın çok kuvvetli olamayacağını düşünebilir. Ancak Visual Interdev dünyanın en iyi kolaylık ve kuvvetlilik desteğini vermektedir. Visual Interdev ortamında kompleks SQL programlayabilirsiniz. Visual Interdev, Microsoft SQL Server, Oracle, Sybase, Informix, IBM DB/2, Microsoft Access, FoxPro, Paradox gibi ODBC uyumlu bütün veritabanlarını desteklemektir.

**ACTIVEX DATA OBJECT (ADO)**

ADO bütün Visual Interdev araçları için veritabanı erişimi sağlar. Web sayfalarınızla database ilişkisi kurmak için ADO temel modeli oluşturmaktadır. ADO web sayfalarınız ile herhangi bir ODBC uyumlu database arasında bağlantıyı sağlar. ADO modelinin ana faydası düşük memory overheadi ve yüksek sürattir ki bu da Web temelli uygulamalar için idealdir.

ADO, veri kaynağına erişimi sağlamayabilmeniz için ActiveX script kullanmanıza izin verir. Ayrıca ActiveX scripti bir ADO’nun özelliklerini ve metodlarını değiştirmek içinde kullanabilirsiniz. ADO, resimleri ve büyük binary nesneleri (BLOB) de içeren değişik veri tiplerini desteklemektedir. ADO transactionları, cursorları, hata yönetimini ve veritabanı içinde oluşturulmuş *Stored Procedure*' lerin kullanımını destekler.

Microsoft, ADO’yu web sayfalarınızdan bir veritabanına erişmek için dilden bağımsız objeler olması için yarattı. ADO, Microsoft’un OLE database modelinin üzerine inşa edildi. DAO (Data Access Object) ve RDO (Remote Data Objects)’ya aşikar olan Visual Basic programcıları Microsoft’un kısaltmaları birleştirip harflerle oynadıgını düşünebilir. ADO hem RDO’dan hem de DAO’dan daha üstündür. ADO daha önceki veri erişim metodlarını nesneye yönelik bir standartla birleştirirken RDO ve DAO’nun özelliklerini de içermekte ve OLE modelini kullanarak İnternet için veri erişimi sağlama yeteneğini arttırmaktadır.

DAO (Data Access Object) ilk olarak Microsoft Visual Basic ve Microsoft Access’in önceki versiyolarında bulunuyordu. DAO bir objenin kapsamı içerisinde database fonksiyonlarını ve işlemlerini birleştirmek için geliştirildi. DAO ODBC-uyumlu databaselere erişimi sağlamaktadır.

RDO ise DAO’dan daha üstündü ve Visual Basic 4’ün içine koyulmuştu. RDO ODBC-uyumlu databaselere erişim için daha iyi bir çözümdü ve bu objelerin server’a olan erişimlerini arttırmıştı. Bu iki metodun üzerine ADO’nun avantajı bağımsız olarak objeleri yaratabilmenizdir. Hem RDO hem de DAO’da objeler için bir hiyerarşi yaratmak zorundaydınız. Ayrıca ADO bu metodlara oranla daha hızlı ve daha etkindir.

OLE DB’nin arkasındaki fikir remote objectleri sanki local’miş gibi gösteren bir nesne temelli arayüz sağlamaktır. Amaç uzaktaki server makinada ya da kendi makinanızda bulunan yardımcı objeler sayesinde database erişiminizi sağlayabilmenizdir.

**Şekil 2.2** SQL Server veritabanına erişim

Yukarıdaki şekilde ADO ve OLE-DB' nin birlikte Microsoft SQL Server database’ine erişim sağlamak için nasıl çalıştıklarını görüyoruz. ADO web server üzerinde ASP içinde yer alır. Browser database bilgisi için istek gönderdiğinde ASP çağrılır ve ADO OLE DB aracılığıyla isteği database server’a gönderir. MSDA SQL spesifik bir SQL dilidir ve Microsoft Access ve Microsoft SQL Server kendi veri kaynakları ile haberleşmede kullanımı desteklemektedir. ODBC sürücüsü her database için MSDA SQL’i spesifik bir dile çevirir. Daha sonra bu bilgi bu hat boyunca ilerler. ASP ve ADO sonuçları düzenleyip browser’a geri göndermek için beraber çalışırlar.

ADO’nun nesne-temelli bir çözüm olduğundan bahsetmiştik. ADO modelinde 7 ana nesne mevcuttur :

- Connection Object

- Command Object

- Recordset Object

- Field Object

- Parameter Object

- Property Object

- Error Object

Bu modelde *Connection* objectinin temel object olduğunu görüyoruz. Modeldeki diğer bütün objectler *Connection* objectine bağlıdır. Veritabanına bir bağlantı olmadan diğer nesneler varolamayacağından bu hiyerarşi önemlidir. Oluşturulan yeni bir *Recordset'i* mutlaka daha önce tanımlanmış bir *Connection* objesinin altına koymak yerine, yeni bir Connection yaratarak onun altında oluşturmak mümkündür. ADO modelinin bu yapısal doğası kodun daha düzenli olmasına katkıda bulunur.

**Connection Object**

Database ile olan bağlantınızı kontrol eder. Bağlantı ile ilgili bütün bilgiler bu object sayesinde sağlanır. *Connection* Objectinin timeout gibi özelliklerini değiştirebilirsiniz. Database ile olan bağlantıyı açıp kapatabilir ve transaction özelliklerini düzenleyebilir.

**Command Object**

*Command* objecti database üzerinde çalıştıracağınız spesifik bir komutu tanımlamanızı sağlar. Mesela *Command* objesini bir stored procedure’ü çağırmak için kullanabilirsiniz. Command Objectini daha önce yaratılmış bir connection objesi ile ilişki kurarak oluşturmak zorunda değilsiniz. Bu ADO’nun diğer database iletişim metodlarından farkıdır. Komutlarınız için object hiyerarşisini kullanmak zorunda değilsiniz.Yine de aynı database bağlantısı üzerinde bir çok komut çalıltıracaksanız, objelerinizi bir hiyerarşi altında düzenlemek daha doğru olur.

**Recordset Object******

Bu object sayesinde kayıtları ya da database tablosundaki satırları düzenleyebilirsiniz. Bir recordset bir temel tablodaki bütün satırları tutabilir veya bir sorgulamanın sonuç kümesinden de oluşabilir. *Recordset* objecti hem anında hem de toptan güncellemeleri destekler.

Recordset objecti veritabanının desteklediği değişik tipte *cursor*ler kullanmanıza izin verir. *Cursor* veritabanında nerede olduğunuzu ve nereye gideceğinizi belirtir. Bazı cursorler:

|  | *Dynamic *: Diğer kullanıcılar tarafından yapılan silme, değişiklik ve eklemeleri gösterir. |
| --- | --- |
|  | *Keyset *: Değişiklikleri gösterir ama eklemeleri ve silmeleri göstermez. |
|  | *Static *: Datanın bir kopyasını gösterir. Değişiklikleri, silmeleri ve eklemeleri göremezsiniz. |
|  | *Forward-only*: Static ile aynı tablo içinde sadece ileri doğru ilerleyebilirsiniz. |

**Field Object **

*Field* objecti recordset içerisindeki özel bir sütun ile ilgilidir.

**Parameter Object **

*Paramater* objectini bir veritabanına karşı komut işletirken parametre tanımlamak maksadı ile kullanabiliriz. Mesela bu objeyi database üzerindeki bir stored procedure’e geçirilen parametrelerin değerlerini ayarlamak için kullanabiliriz. Bu object genelde *Command Object* ile beraber kullanılır.

**Property Object **

*Property* objecti dataya erişimi ve sorgulamayı sağlayan özel servisleri gerçekleştiren ve servis sağlayıcı tarafından belirlenen spesifik özellikleri yakalar. OLE DB servis sağlayıcılarını, *ActiveX Data Object*’e ek karakteristikler ve özellikler sunmak üzere ayarlayabilir, daha sonra bu özellikleri uygulamanızın kapasitesini arttırmak için kullanabilirsiniz. Örneğin *Property* Objectini bir servis sağlayıcısının transactionları destekleyip desteklemediğini anlamak için kullanabilirsiniz.

**Error Object ******

Error objecti veritabanı tarafından üretilen hata mesajlarını toplar. Bir veritabanı fonksiyonunu gerçekleştirmeye çalışırken oluşan herhangi bir hata bu object içinde tutulur.

**ODBC Data Source Name (DSN)**

Open Database Connectivity yani ODBC veritabanına erişimi sağlayan bir standarttır. Oracle, SQL Server, Sybase, Interbase, Paradox gibi bir çok veritabanı sistemine erişimi sağlar. NT işletim sisteminde DSN tanımlayarak veritabanlarına ulaşılabilir. Bu Delphi' de Borland Database Engine için *Alias* tanımlamaya benzer.

**File Data Source ******

Bir File DSN belirli bir bilgisayar dahilinde dosya temelli bir bağlantı kurulmasını sağlar. Ve bu bağlantı bir çok kullanıcı tarafından paylaşılabilir. Dosya temelli bağlantıdan kastedilen bir veritabanına bağlanırken gerekli olan bilgilerin bir *.dsn* dosyasında saklanıyor olmasıdır. Bu bilgisayarda veritabanına bağlanabilmek için ODBC driver yüklemiş olmanız gerekmektedir. Uygulama için veritabanı bağlantısı gerçekleştirildiğinde *.dsn *dosyasındaki bilgi *global.asa* dosyasındaki bağlantı stringinin içine eklenir.

File DSN bazen DSN-less bağlantı olarak adlandırılır çünkü bağlantı bilgisi başka herhangi bir yerde değil projenizin içinde saklıdır. File DSN taşınabilirlik özelliğinden dolayı tercih edilmektedir. Uygulamanızı taşıdığınızda ek olarak bir DSN dosyası da kopyalamak ya da yaratmak zorunda değilsiniz.

**Machine Data Source:**

İki tip *Machine Data Source* oluşturulabilir. Birincisi User DSN olarak adlandırılır. Bu tip DSN’ler sadece belirtilen kullanıcılar tarafından kullanılabilir ve makineye özeldir. System DSN ise diğer Machine Datasource tipidir. Bir System DSN’i de makineye özeldir ancak bir çok kullanıcı tarafından kullanılabilir, yani kullanıcıya özel değildir. Bu bilgiler Windows Registry’sinde saklanır ve eğer uygulama başka bir makineye taşınacaksa bu bilgilerde geçirilmelidir. Genellikle File DSN tercih edilir çünkü her kullanıcı için ayrı bir dsn kurulmak zorunda değildir. Machine Datasource makineye özel tanımlandığından uygulama başka bir platforma taşındığı için yeniden tanımlanmak zorundadır

---
*Kaynak: `ASP GİRİŞ 2/ASP GİRİŞ 2.doc` — OBILGIC — 2004*
