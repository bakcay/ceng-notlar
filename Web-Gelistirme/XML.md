# XML

**BAŞLARKEN... **

XML dünyasına hoşgeldiniz.

Teknolojik gelişmelerin sürekli ve hızla devam ettiği bilişim dünyasında Internet,hiç kuşkusuz en önemli araç haline gelmiştir.Bu önemli aracın kullanmış olduğu dil olan HTML ise yapısındaki önemli bazı eksikliklerden dolayı yerini yeni bir dile bırakmaktadır:XML…

XML (Extensible Markup Language) artık çoğumuzun kulağına yabancı gelmeyen bir terim.W3C(World Wide Web Concortium) gibi bağımsız bir organizasyon tarafından geliştirilmiş olan XML, isminden de anlaşılacağı üzere son derece esnek bir yapıya sahiptir.İşte bu esneklik sayesinde XML, elektronik iş sistemleri, bankacılık, finans, sağlık, eğitim, ulaşım, otomotiv sektörleri gibi bir çok alanda,kısacası bilişim dünyasıyla ilgili olan her sektörde varlığını gün geçtikçe daha da hissettirmektedir.

Okumakta olduğunuz bu döküman sizlere XML ve ilişkili teknolojiler hakkında bilgiler vermek amacıyla hazırlanmıştır.Döküman temel olarak iki bölümden oluşmaktadır. Birinci bölümde XML ile yeni tanışan okuyucular düşünülerek temel sözdizimi(syntax) yapıları, terimler ve XML dilinin başlıca yapı birimlerinden bahsedilmiştir.İkinci bölümde ise daha da teknik detaya inilerek XML dilinin yapısındaki detaylar, programlama dilleriyle olan ilişkileri,veritabanı yönetim sistemlerindeki davranışları, gibi konular anlatılmaya çalışılmıştır.Bu bölümden programcılar,veritabanı yöneticileri,sistem uzmanları,web sayfası tasarımcıları öğrenciler gibi okuyucu gruplarının yararlanması düşünülmüştür.

Software AG / Türkiye olarak, hazırlamış olduğumuz bu dökümanın sizlere faydalı olmasını temenni etmekteyiz.Dökümanla ilgili eksik gördüğünüz yönleri, önerilerinizi, sorularınızı ve her türlü yorumlarınızı öğrenmekten memnunluk duyacağımızı belirtir çalışmalarınızda başarılar dileriz.

Saygılarımızla

**XML Nedir? **

XML(Extensible Markup Language) HTML ile pek çok açıdan benzerlik gösteren bir markup dilidir.Verinin tanımlanması ve tarif edilmesi için kulanılır.HTML'deki yapının aksine XML'de kullanılacak olan tag'ler önceden tanımlı değildir.Yani bir XML dökümanının yapısı tamamıyle kullanıcı tarafından oluşturulur.Verinin tarif edilmesi için DTD adı verilen yapılar kullanılmaktadır.XML ve DTD'nin birlikte kullanılması ile dökümanlar kendini tarif eden bir yapı halini alırlar.
XML ve HTML arasındaki en belirgin fark XML'in verinin kendisiyle ilgilenmesi HTML'in ise verinin sunumuyla ilgilenmesidir.Buna bağlı olarak HTML dökümanları veriye ilişkin şekillendirme bilgilerini içerirken XML dökümanları ise verinin tanım bilgilerini içermektedir. XML'in tasarım amaçlarından biri de verinin taşınmasıdır.
Bahsedilen bu özellikleri incelendiğinde XML'in pek çok önemli işlevi yerine getirdiği görülmektedir.
Şimdi çok basit bir XML dökümanını birlikte inceleyelim:

<not>
<kime>Mehmet</kime>
<kimden>Erdem</kimden>
<heading>Hatırlatma</heading>
<body>Kitapları Unutma!</body>
</not>

HTML dökümanlarına çok benzeyen bu yapıda ilk etapta göze çarpan nokta tag yapılarının bizim tarafımızdan tasarlanmış oluşudur.HTML'de kullanılan <p> ve <h1> gibi standart tag yapıları yukarıdaki XML dökümanında kullanılmamıştır.Bahsedilen bu özelliği nedeniyle XML dökümanları genişletilebilir(extensible) bir yapıya sahiptir.Dökümanın bu hali gerçek anlamda herhangi bir şey ifade etmez.Dökümanın iletimi(gönderim veya alım) ya da sunumu için başka şeylerin de yapılması gerekmektedir.
Burada önemli bir nokta olarak XML'i HTML'in yerine geçecek bir dil olarak düşünmek yerine HTML'in tamamlayıcısı olacak olan bir dil şeklinde düşünmek uygundur.
Günümüz bilişim dünyasına bakacak olduğumuzda XML'in her alanda karşımıza çıktığını görmekteyiz.Bu nedenle XML'I bir anlamda geleceğin web dili olarak tanımlamak mümkündür.

**XML Nasıl Kullanılabilir? **

XML hakkında bilinmesi gereken en önemli nokta bu dilin veriyi taşımak amacıyla tasarlanmış oluşudur.
XML ile veriler yapı bakımından modülerlik kazanmaktadır.Yukarıda bahsettiğimiz gibi XML dökümanları verinin içeriğiyle ilgilenmektedirler.Bu sayede verilerin içerik,yapı ve sunum kısımları ayrı modüller halinde farklı XML dökümanlarında tutulmaktadır.
XML dökümanları Veri Adaları(Data Islands) adı verilen teknik sayesinde HTML sayfaları içerisinde de depolanabilmektedir.Bu teknik sayesinde verinizin sadece sunumuyla ilgilenilmektedir

XML ile verinin alışveriş işlemi gerçekleştirilir.XML,yapısının esnekliği sayesinde birbirine uyumlu olmayan sistemler arasında veri alış verişini rahatlıkla gerçekleştirmektedir.Günümüz bilişim dünyasında bilgisayar sistemleri ve veritabanlarının genellikle birbirine uyumsuz sistemler içerebildiklerini görmekteyiz.Bundan dolayı uygulama geliştiriciler Internet üzerinden bu tip uyumsuz verilerin alış veriş işlemini gerçekleştirmek zorundadırlar.
Verinin XML formatına çevrilmesi ile farklı sistemler ve uygulamalardaki verilerin karmaşıklık derecesi indirgenerek alış veriş işleminin kolaylaştırılması sağlanır.
XML ile finansal bilgilerin Internet üzerinden alış verişi sağlanmaktadır.Günümüzde artık hepimizin sıklıkla duyduğu elektronik iş kavramı açısından incelenecek olduğunda XML'in önemli fonksiyonları yerine getirdiği görülmektedir.Bahsedilen bu fonksiyonları ile XML geleceğin Elektronik İş dili olarak da yeni bir misyonu üstlenmektedir.
XML ile verinin paylaşımı kolaylaştırılır.
XML,veriyi düz metin (plain text) formatında saklamasından dolayı veriyi paylaştırma konusunda da hem yazılım hem de donanımdan bağımsız hareket edebilme imkanını sunmuştur.
Bu sayede farklı uygulamalarda hareket eden farklı veri tipleriyle çalışmak daha da kolaylaşır.Ayrıca işletim sistemlerinin yükseltgenmesi,sunucu,uygulama vb. dışsal faktörlerin yenilenmesi gibi dışsal faktörlerden de asgari ölçüde etkilenilmiş olunur.
XML ile verinin depolanması sağlanır.
XML, verinin dosyalarda veya veritabanlarında saklanması için de kullanılabilir.
XML,yazılım,donanım ve uygulamalardan bağımsız olduğu için verinin daha elverişli olarak kullanımını sağlamaktadır.Yani başka istemci(client) veya uygulamalar tıpkı veri kaynaklarına erişiyormuş gibi XML dosyalarına rahatlıkla erişebilirler.
XML,esnek yapısı nedeniyle başka dillerin de oluşturulabilmesine olanak tanır.Wireless Markup Language(WML) mobil cihazları için kullanılan WAP ortamlarının dilidir ve XML'in türevidir.

**XML Sözdizimi(XML Syntax) **

XML Syntax basit bir kaç kuraldan ibarettir.Bundan dolayı kullanımı ve öğrenimi oldukça kolaydır.

Bir XML döküman örneğini inceleyelim:

<?xml version="1.0"?>
<not>
<kime>Mehmet</kime>
<kimden>Erdem</kimden>
<heading>Hatırlatma</heading>
<body>Kitapları Unutma!</body>
</not>

XML dökümanları kendini tarif eden bir syntax'a sahiptir.
Dökümanın ilk satırı XML deklerasyonu(XML declaration) olarak isimlendirilir.Bu kısımda XML dökümanının versiyon bilgisi tanımlanır.Yukarıdaki örnekte XML dökümanımızın versiyonu 1.0 olarak belirtilmiştir.
Bir sonraki satırda dökümanın "root element" adı verilen kök elementi belirtilmiştir.Örneğimizde root element "not" tur.

<not>

Daha sonraki satırda 4 adet child element belirtilmiştir.(kimden,kime,heading ve body):

<kime>Mehmet</kime>
<kimden>Erdem</kimden>
<heading>Hatırlatma</heading>
<body>Kitapları Unutma!</body>

Son olarak root elementin bitişini gösteren tag bulunmaktadır:

</not>

Tüm XML elementleri bir kapanış tag'ine sahip olmalıdırlar.HTML'de ise bazı elementler bitiş tag'lerine sahip olmayabilir.Örneğin aşağıdaki kod parçası HTML için geçerli bir kod olmasına rağmen XML için geçerli değildir:

<p>Bu bir paragraftır
<p>Bu başka bir paragraftır

Yukarıdaki kod parçasını XML formatına uyarlayacak olduğumuzda

<p>Bu bir paragragftır</p>
<p>Bu başka bir paragraftır</p>

ªeklinde bir düzenleme yapmamız gerekecektir.
XML tag'ler için case-sensitive özellik gösterirler.HTML'de ise case-sensitive özellik yoktur.

<mektup>Bu syntax yanlıştır</MEKTUP>

<mektup>Doğru bir syntax örneği</mektup>

XML dökümanları içerisinde tüm elementler hiyerarşiye uymalıdırlar.HTML dökümanlarında bazı elementler düzgün bir içiçe olma yapısında olmayabilirler. Aşağıdaki örneği inceleyelim:

<b><i>Burada kullanılacak olan dökümanın formatı bold ve italic olacaktır</b></i>

XML syntax kurallarına gore yukarıdaki örneği düzenleyecek olursak:

<b><i>Burada kullanılacak olan dökümanın formatı bold ve italic olacaktır</i></b>

Görüleceği üzere elementler belirli bir düzen çerçevesinde içiçe geçmiş durumdadırlar.
XML syntax'ında tüm XML dökümanlarının bir root elementi olması gerekmektedir.XML dökümanları içerisinde ilk tag "root tag" olarak isimlendirilir:
Bahsedilen bu root elementin altındaki tüm elementler "child element" olarak adlandırılır.Bu child elementler ise daha önceden belirtilmiş olan synax'a uymak zorundadır.Yani elementlerin içiçe geçme durumları belirli bir hiyerarşiye gore olmaktadır.

<root>
<child>
<subchild>….</subchild>
</child>
…………
</root>

Attribute değerleri daima tırnak içine alınmalıdır.
XML elementleri attribute'lara sahip olabilirler ve bu attribute'lar ise tıpkı HTML'de olduğu gibi isim/değer(name/value) çiftlerini içerebilirler.Attibute değerlerinin nasıl kullanıldığını bir örnekle açıklayalım:

<?xml version="1.0"?>
<not date="12/10/99">
<kime>Mehmet</kime>
<kimden>Erdem</kimden>
<heading>Hatırlatma</heading>
<body>Kitapları Unutma</body>
</not>

Dikkat edilecek olursa "not" elementinin sahip olduğu "date" attribute değeri tırnak işareti içerisinde belirtilmiştir.
HTML'de white space adı verilen boşluk karakteri gözönüne alınmaz.Oysa XML dökümanlarında white space karakterler de değerlendirmeye alınır.Yani bir HTML sayfasında "Merhaba,benim adım Erdem" cümleciği sunum sırasında "Merhaba,benim adım Erdem" şeklinde görüntülenir.

**Elementler **

XML dökümanları daha fazla bilgiyi taşıyabilmek için genişletilebilirler.Aşağıdaki kod satırını incelyelim:

<not>
<kime>Mehmet</kime>
<kimden>Erdem</kimden>
<body>Kitapları Unutma!</body>
</not>

Şimdi yazmış olduğumuz bu kod satırının nasıl bir çıktı vereceğini inceleyelim:

Mesaj
kime:Mehmet
kimden:Erdem
Kitapları Unutma!

Şimdi dökümanımız içerisinde daha fazla bilgiyi sunmak istediğimizi varsayalım:

<not>
<tarih>199-03-01</tarih>
<kime>Mehmet</kime>
<kimden>Erdem</kimden>
<heading>Hatırlatma</heading>
<body>Kitapları Unutma</body>
</not>

Görüleceği gibi XML dökümanının yapısında herhangi bir değişiklik yapmaksızın daha fazla bikgiyi görüntüleme olanağını bulduk.Bu da bize XML dökümanlarının esnek yapısı hakkında bazı fikirler vermektedir.
XML elementleri birbirleriyle ilişki içindedir.Bu ilişki biçimi elementlerin parent ya da child oluşlarıyla belirlenmektedir.
XML elementlerinin parent/child ilişkilerini bir örnek üzerinde açıklayalım:

Kitap Başlığı:Software AG ve XML

Bölüm 1: XML'e giriş

· HTML ve XML'in karşılaştırılması· · · XML ve E-Ekonomi· · Bölüm 2: XML Syntax

· Elementler· · · Attribute'lar· ·

Çıktı düzeni verilmiş olan bu kitabı tanımlayacak XML dökümanını tasarlayalım:

<kitap>
<baslik>Software AG ve XML</baslik>
<urun id="12-112" media="paper"></urun>
<bolum>XML'e giris
<para> HTML ve XML'in karşılaştırılması</para>
<para> XML ve E-Ekonomi</para>
</bolum>
<bolum>XML'e giris
<para> Elementler</para>
<para>Attribute'lar</para>
</bolum>
</kitap>

Dökümanımızın root elementi "kitap" tır."kitap" elementi "baslik" ve "bolum" elementlerinin parent'i durumundadır."baslik" ve "bolum" elementleri ise aynı seviyede bulunan elementlerdir ve bunlar arasındaki iliºkiye sibling denir.
Elementler farklı içerik tiplerine sahip olabilirler.
Bir element diğer bir elementi içerebileceği gibi basit,sabit ya da boş(empty) içerkte de olabilir.Yukarıdaki örneği incelediğimizde "para" elementinin sadece metin(text) içerğinde olduğunu,"bolum" elementinin diğer elementleri içerebildiğini ve "urun" elementinin ise boş bir içerikte(empty)oldugunu görmekteyiz.

**Elementlerin İsimlendirilmesi **
Elementlerin isimlendirilmelerinde bazı kurallar geçerlidir:

- İsimler harf,sayı ya da diğer karakterleri içerebilir.
- İsimler bir sayı veya \_ (underscore) karakteri ile başlamamalıdır.
- İsimler "xml"(ya da XML veya Xml) şeklinde başlamamalıdır
- İsimler boşluk içermemelidir.

**Attribute'lar **

Elementler attribute değerlerine sahip olabilirler.Attribute'lar elementler için ek bilgilerin tanımlanmasına olanak veren yapı birimleridir:
Bir HTML sayfasında tanımlanmış olan
<IMG SRC="edi1.gif">
kod parçasında SRC attribute değeri IMG elementi için ek bilgiler tanımlamamıza olanak sağlamaktadır.XML dökümanları için de durum aynıdır.
Veri bir XML dökümanında element veya attribute'lar içerisinde saklanır.Aşağıdaki örnekleri inceleyelim:

<kisi cinsiyet="bayan">
<ad>Zeynep</ad>
<soyad>Temel</soyad>
</kisi>

<kisi>
<cinsiyet>bayan</cinsiyet>
<ad>Zeynep</ad>
<soyad>Temel</soyad>
</kisi>

İki örneği karşılaştıracak olduğumuzda "cinsiyet" değerinin birinci örnekte bir attribute ikinci örnekte ise bir element halinde oldugu anlaşılacaktır.Ancak her iki örnekte de ortak olan özellik hem element hem de attribute şeklinde de "cinsiyet" değerinin bilgi depolaması oldugudur.
Hangi durumlarda attribute'ların hangi durumlarda elementlerin kullanılacağına ilişkin kesin bir tanımlama yoktur.Aşağıdaki üç örneği incelediğimizde tümünün aynı bilgiyi içerdiği açıkça görülecektir:

Programlama veya web tasarımı gibi konulara yakınlığı olan okuyucularımız yukarıdaki üç örnekten sonuncusunun syntax bakımından daha avantajlı olduğunu fark edeceklerdir.

**XML Dökümanlarının Geçerliliği **

**Well-Formed XML Dökümanları **Bir well-formed XML dökümanı doğru XML syntax'ında olan döküman demektir.

**Valid XML Dökümanları **
Valid bir XML dökümanı doğru XML syntax'ında olan(yani aynı zamanda well-formed yapıda olan) ve yapı bilgilerini aldığı DTD'ye uyumluluk gösteren döküman demektir.

Aşağıdaki örnekleri inceleyelim:

**DTD Nedir? **
DTD'leri, XML dökümanlarının yapı bilgilerini tutan modüller olarak tanımlamak mümkündür.Döküman içinde kullanılacak olan tüm varlıklar daha önceden DTD içerisinde tanımlanmalıdır.

**XML Schema **XML Schema'lar da DTD'ler gibi XML dökümanlarının yapı bilgilerini tutarlar.Ancak DTD'lere gore daha kullanışlıdır ve en önemli özelliği XML syntax'ında olmalarıdır.

Not: DTD ve Schema kavramları daha sonraki bölümlerde detaylı olarak incelenecektir.Bu aşamada sadece tanımların öğrenilmesi yeterlidir.

**Hata(Error) ve Hata Kontrolü **XML dökümanları içerisinde yapacağımız bir syntax error veya geçerlilik kontrolü hatası(validation error) durumunda program XML dökümanını işleme işine devam etmez ve durur.HTML'de ise yapılabilecek bir hata da(örneğin bitiş tag'i yazmayı unuttuğumuzda) program çalışmaya devam eder.

**XML Dökümanlarının Görüntülenmesi Stylesheet Kavramı **

Bir XML dökümanının sunumu sırasında izlenen yollar yukarıdaki şekilde belirtildiği şekilde gerçekleşir.XML dökümanları,yapı bilgilerinin geçerlilik kontrolleri (DTD'ye bakılarak) yapıldıktan sonra XML Parser adı verilen yazılıma giderler.XML parser bu yapı bilgilerinden yararlanarak dökümanın parçalanma ağç yapısını yani Parse Tree'sini oluşturur.Parse Tree'si oluşturulmuş olan döküman "Stylesheet" adı verilen işlem kullanılarak sunuma hazır hale getirilir. Daha sonra stylesheet işleminin uygulandığı sunum kısmından(rendering agent) alınan XML dökümanı görüntüleme cihazına aktarılır.
Temel olarak kullanılan iki stylesheet tekniği bulunmaktadır:CSS ve XSL
CSS(Cascaded StyleSheets) ve XSL(Extensible StyleSheets) tekniklerinin her ikisi de XML dökümanlarının şekillendirilmesi amacıyla kullanılır.Amacı aynı olmasına rağmen XSL'in CSS'e gore daha esnek ve daha avantajlı olduğunu görmekteyiz.
Aşağıdaki XSL örneğini inceleyelim:

<?xml version="1.0"?>
<?xml:stylesheet type="text/xsl" href="ornek.xsl"?>
<kahvalti-menu>
<yemek>
<ad>Tulum Peynir</ad>
<fiyat>125</fiyat>
<tarif>Taze Tulum Peyniri</tarif>
<kalori>1200</kalori>
<yemek>
</kahvalti-menu>

Dikkat edilecek olursa XML dökümanının şekil bilgisi "ornek.xsl" adı verilen ayrı bir yapı biriminde tutulmaktadır."ornek.xsl" yapı birimi xsl uzantısından anlaşılacağı gibi XML dökümanımız üzerinde xsl tekniğini kullanarak stylesheet işlemini uygulamıştır.

**ELEMENT'LER İLE ÇALIŞMAK **

Elementler DTD içinde element bildirimleri yapılarak tanımlanırlar.Bu tanımlama şu şekilde yapılır:

< !ELEMENT ElementName Type >

ElementName, element ismini belirten bir markup değeridir ve DTD içerisinde tek(unique) olmalıdır.Elementin tip değeri "Type" olarak belirtilmiştir.Bu değer ayrıca elementin içerik değeri olarak da bilinir.

XML dört tipteki element değerini destekler:

- Empty:Herhangi bir içeriği olmayan fakat attribute içerebilen element
- Element Only:Sadece child element içeren element
- Mixed:child element ve karakter verisinin kombinasyonunu içeren element
- Any:DTD tarafından müsaade edilen herhangi bir içeriği içeren element

Şimdi biraz daha detaya girelim:

**Empty Element **

Adından da anlaşılacağı gibi bu tür elementler herhangi bir içerik içermezler.Empty elementler şu şekilde deklare edilirler:

< !ELEMENT ElementName EMPTY >

aşağıda bir empty element deklare ediliş örneği görülmektedir

< !ELEMENT img EMPTY>

Bir empty element döküman içerisinde şu iki yoldan birisi ile tanımlanır:

- bir start/end tag çifti
- bir empty(boş) tag

Şimdi start/end tag ile yapılan bir emty tag örneği verelim:

<img src="Baslik.gif" < > /img>

Dikkat edilirse tag ler arasında herhangi bir içerik değeri yoktur.
Empty element tanımı için şimdi Empty tag kullanımına örnek verelim:

<img src="Baslik.gif" / >

Görüleceği gibi empty tag aslında bir çeşit start/end tag olarak düşünülebilir.

**Element-Only Element **

Child elementleri dışında herhangi birşey içermeyen elementlerdir.Bu tip bir element, elementin içerik modelini belirterek yapılır yani element deklarasyonu içerisinde child elementleri içeren genel bir listenin oluşturulması sayesinde yapılır.

Bir elementin içerik modeli şu şekilde oluşturulur:

< !ELEMENT ElementName ContentModel >

İçerik modelinin kendisi de özel sembol ve child element isimlerinin kombinasyonu sonucu oluşur.Bir elementin içerik modelinin oluşturulması için şu semboller kullanılır:

- Parantez(( )) child elemente ait bir grup ve diziyi bitirmek için kullanılır
- Virgül(,) dizideki başlıkları ayırmak için kullanılır
- Pipe(|) seçimsel gruplar arasındaki başlıkları ayırmak için kullanılır
- Sembol yoksa bir child element in mutlaka birkez görüneceği anlamı çıkar
- Soru işareti(?) child elementin ya bir kez görüneceğini yada hiç görünmeyeceğini belirtmek için kullanılır
- Asterisk(\*) Bir child elementin birden fazla sayıda görülebileceğini belirtir
- Artı işareti(+) Child elementin en az bir kere görüleceğini belirtir

Bahsedilen bu sembolleri anlamanın en güzel yolu elbette örneklere gözatmak olacaktır.

Aşağıdaki örnekte resume elementine ait içerik modelin oluşturulmasına gözatalım

< ELEMENT genel (bilgi,(egitim | deneyim+)+,hobi?,referanslar\*) >

**Mixed Elements **

Mixed elementler hem karakter tipindeki veriyi hem de child elementleri içerebilirler.En basit mixed element sadece karakter verisi içeren olacaktır.Bu tipteki bir element bazen text-only element olarak da adlandırılır.Text-only elementler şu şekilde tanımlanır:

< !ELEMENT ElementName (#PCDATA) >

Text-only elementler için yapılan içerik modeli tanımlamalarında (#PCDATA) terimi kullanılır ve bu terim elementin parse edilmiş karakter verisi içerdiğini bildirir.

Örneğin:

< !ELEMENT band (#PCDATA) >

Bu element XML dökümanı içindeki cd koleksiyonuna ait olan bir bandın ismini markup etmek için kullanılmış olabilir.Aşağıdaki örnekte döküman içerisinde bu band elementinin nasıl tanımlandığı görülüyor:

<band> Candan Ercetin </band>

Aşağıdaki örnekte bir film koleksiyon bildirim kodunun oluşturulması görülmektedir:

<!ELEMENT filmler (film)+>

<!ELEMENT film (baslik,yazar+,produktor+,yonetmen+,aktor\*,yorumlar?)>

<!ELEMENT baslik (#PCDATA)>

<!ELEMENT yazar (#PCDATA)>

<!ELEMENT produktor (#PCDATA)>

<!ELEMENT yonetmen (#PCDATA)>

<!ELEMENT aktor (#PCDATA)>

<!ELEMENT yorumlar (#PCDATA)>

Bu DTD nin yapısını biraz daha inceleyelim:

Film elementinin içinde bulunan baslik elementi sadece bir kez görünmelidir.Yazar,produktor ve yonetmen elementleri de en azından bir kez görünmelidir,ancak bu elementler daha fazla seferde görünebilirler.aktor elementi herhangi bir sayıda döküman içinde görünebilmektedir.film ‘in içerik modelindeki son eleman olan yorumlar elementi film hakkında ki yorumları içeren bir liste elde etmemizi sağlamaktadır.

Burda akılda tutmamız gereken şey mixed yapıdaki bir elementin child elementler içermeyeceğidir.

İşin detayına indiğimizde mixed elementlerin deklare edilişinin element-only elementlerin deklare edilişine çok benzerlik gösterdiğini görmekteyiz.Mixed bir elementin içerik modeli tekrarlanan bir seçim listesi içerir ve yazılımı şöyledir:

<!ELEMENT ElementName (#PCDATA | ElementList)>

Buradan da görüleceği üzere #PCDATA mixed elementin karakter verisini de içerebileceğini gösterir.Seçim listesinden arda kalan şey child elementleri ve element-only elemente benzeyen düzenli elementleri içerir.Daha sonra tekrar #PCDATA kullanılması durumunda child elementlerde de karakter verisinin kullanılabileceği anlamına gelir.Dikkat edilirse asterisk(\*) içerik modelin en sonunda göze çarpar ve bu da tüm seçim listesinin opsiyonel bir yapıda olduğunu belirtir.Aşağıda #PCDATA ile seçim listesinin nasıl kullanılabileceği gösterilmiştir.

<!ELEMENT hatirlatma (#PCDATA | baslik | konu)\*>

Not

Bir mixed elementin içerik modelinde,karakter verisi (#PCDATA) mutlaka ilk olarak seçim listesinin içinde belirtilmesi gerekir ve seçim listesinin kendisi de asterisk(\*) izlemelidir

**ANY Elementler **

XML tarafından desteklenen en son element türüdür ve ANY sembolü ile deklare edilirler.Bu element türü hemen hemen belirgin bir yapısı olmamasına karşın karakter verisi,deklare edilmiş element tiplerini veya bunların karışımını içerebilir.Bu element türünü geniş kapsamlı açık bir içerik modeli olarak düşünebiliriz.Şu şekilde yazımları vardır:

<!ELEMENT ElementName ANY>

**ATTRIBUTE'LER İLE ÇALIŞMAK **

Attribute’ler attribute deklerasyon listesi denilen bir liste içinde aşağıda belirtilen şekilde tanımlanırlar:

<!ATTLIST ElementName AttrName AttrType Default>

Görüleceği gibi bir attribute isim(AttrName) ve tip(AttrType) ve default olmak üzere üç bileşenden oluşmaktadır.Bir attribute deklerasyonu sırasında kullanılabilecek olan dört default değeri vardır:

- #REQUIRED
- #IMPLIED
- #FIXED
- default

#REQUIRED değeri attribute’ın element için mutlaka gerekli olduğunu belirtir. #IMPLIED değeri attribute ‘ın seçimsel olduğunu ve element için kullanımının zorunlu olmadığını belirtir. #FIXED değeri attribute’a atanacak değerin sabit olacağını ve bunun da attribute’u bir bilginin sabit bir parçası durumuna getireceğini belirtir.

XML 10 tane farklı attribute tipini desteklemektedir:

- CDATA :Parse edlmemiş karakter verisi
- Enumerated :Bir dizi string değeri
- NOTATION :DTD içinde herhangi bir yerde tanımlanmış olan notasyon
- ENTITY: Dışsal bir binary entity
- ENTITIES Birden fazla dışsal binary entity ler
- ID :Unique bir tanımlayıcı
- IDREF: DTD içinde tanımlanmış olan bir ID ye refere edilen değer
- IDREFS: DTD içinde birden fazla ID lere refere edilen değerler
- NMTOKEN: XML token değerlerini içeren isim
- NMTOKENS:XML tone karakterlerini içeren isim boşlukları

**String Attribute’leri **
String attribute ler CDATA tarafından gösterilen ve en çok kullanılan attribute tipidir.CDATA tipi attribute’ın bir metin stringini içereceğini belirtir.Aşağıdaki örnekte CDATA tipi ile beraber oyuncu elementinin kullanılışı gösterilmiştir:

<!ATTLIST oyuncu takim CDATA #REQUIRED>

Bu örnekte oyuncu ‘nun ait olduğu takim’in oyuncu elementi için gerekli olan bir karakter verisi attribute dur.Bu takim attribute’ını seçimsel duruma getirmek isteseydik:

<!ATTLIST oyuncu takim CDATA #IMPLIED>

şeklinde kullanmamız gerekirdi.

Burada karşımıza önemli bir soru çıkmaktadır:XML parser acaba string attribute tipini diğerlerinden nasıl ayırdedebilmektedir?

Bir XML parser CDATA attribute değerinin işleme konması sırasında boşlukların tümünü reserve eder.Satır sonlarının whitespace boşluklarına dönüştürülme işlemi string attribute değerinin normalizasyonu olarak adlandırılır.

**Enumerated Attribute’ler **
Bu tür attribute ler daha önceden tanımlanmış bir metin dizisinin listesini içerirler.Enumerated tipi CDATA tipine benzemektedir ancak bu veri tipinde kabul edilebilir attribute değerleri attribute listesi deklerasyonu içinde sağlanmaktadır.Daha önce vermiş olduğumuz örneği biraz daha geliştirelim.oyuncu elementine enumerated bir attribute değeri olan pozisyon bilgisini de ekleyelim

<!ATLIST oyuncu pozisyon (ortasaha | forvet | savunma | kaleci ) "ortasaha">

Bu örnekte pozisyon değerinden birini seçebilmekteyiz.Eğer hiçbir şey seçmezsek default değer olan "ortasaha" devreye girmiştir.

**Notasyon Attribute’ler **
Enumeration attribute’ın özel bir kullanımı da notasyon attribute leridir.Notasyonlar DTD içinde biryerlerde tanımlanmış olan bir liste olarak düşünülebilir.Bu deklerasyonu DTD içerisinde NOTATION anahtarsözcüğünü kullanarak şu şekilde yazabiliriz:

<!ATTLIST image format NOTATION (gif | jpeg) #REQUIRED)>

Dikkat edilirse #REQUIRED sembolü attribute’un gerekli olduğunu belirtmeye yarıyordu.Enumerated attribute değerleri opsiyonel de olabilir.Bunun için #IMPLIED terimini kullanmamız gerekir.

**Tokenize Attribute’ler **
XML tarafından desteklenen son attribute tipi tokenize attribute’lerdir.Bunlar XML parser tarafından attribute’ların token larına ayrıştırılması işlemini yaparlar.XML parser bu token’larına ayrıştırma işlemi sonucunda tüm boşluk ve tek karakter sembollerini eleme işlemine tabi tutar. ENTITY,ENTITIES,ID,IDREF,IDREFS,NMTOKEN ve NMTOKENS tokenized attribute tipleridir.

ENTITY ve ENTITIES tipleri entity lere refere olmak için kullanılır.Örneğin image’ler tipik olarak binary entity’ler şeklinde refere olurlar.ENTITIES tipi ENTITY e benzemektedir ve bir entity listesi oluşturmamıza yararlar.Aşağıda ENTITY attribute tipinin reference işleminin oluşturulması gösterilmiştir.

<!ATTLIST bolum id ID #REQUIRED>

IDREF ve IDREFS tipleri ID lere yapılacak olan reference’leri belirtmek için kullanılır.Bu tipler ID tipine benzerler ancak burada akılda tutulması gereken şey bunların kendilerinin de unique yapıda olmalarıdır.

NMTOKEN ve NMTOKENS attribute tipleri token isim değerlerini içerirler.Bir isim token, string yapıda olan bir metin değeridir.Genelde isim token değeri sadece tek bir ismi içerir ve boşluk içermez.

**Birden Fazla Attribute Deklerasyonu **
Buraya kadar olan bölümde ayrı attribute’lerin örneklerini gördük.Elbette elementler birden fazla attribute içerebilirler.Bir elementin tüm attribute değerlerini tek bir attribute list’te tutmak elbette en mantıklı çözümdür.Aşağıda buna ilişkin bir örnek görülmektedir:

**DTD'NİN DETAYLARI **

**Entity’ler ve döküman yapısı **

Bir XML dökümanı entity adı verilen depolama birimlerine bölünmüştür ve bu bölümler ise unique isimler alırlar.Bu entity lerden birisi document entity olarak isimlendirilir ve dökümanın en üstünde yeralır.Document entity aslında dökümanın tümünü içerir diyebiliriz.

Entity ler dökümanın fiziksel yapısını tarif ederler.Bundan dolayı çoğu zaman dosyalara birleşik olarak bulunurlar.Gerçekte,entity lerin çoğu sistem üzerinde kayıtlı dosyalara karşılık gelmektedirler.Biraz daha detaya inecek olursak bu entity ler bir veritabanı kaydı veya belleğin herhangi bir kısmıyla birleşebilirler.Burada akılda tutulması gereken en önemli nokta entity kavramının daima depolamayla ilgili oluşudur.

Daha önce verilen bir örneği tekrar gözden geçirelim:

<?xml version="1.0" standalone="no">

<!DOCTYPE filmler SYSTEM "filmler.dtd">

<filmler>

...

</filmler>

Burdan görüleceği gibi document type decleration filmler root elementi ve filmler.dtd dışsal altkümesi olmak üzere iki entity den bahseder."filmler.dtd " dışsal alt kümesini yerini değiştirerek entity olarak değerlendirilmemesini sağlamak da mümkündür.Burada anahtar nokta dışsal bir DTD alt kümesinin depolanış şekline dikkat etmek olacaktır.
**Karakterler ve entity’ler **

Entity lerin deklerasyonu ve referans işlemlerinin detaylarında girmeden önce karakterlerin entity’ler içerisinde nasıl kullanıldığını anlamak çok önemlidir.Çünkü XML karakterlerin encoding işlemi sırasında değişik standartlar kullanır ve bu da ona büyük bir esneklik sağlar.XML karakter encoding işleminin temelinde ISO/IEC 10646 Unicode standardı kullanılmaktadır.Bu standart karakter kullanımında inanılmaz bir esneklik sağlar.

Bu standarda ek olarak ISO 8859 veya JIS X-0208-1997 standardı da kullanılabilmektedir.Bu standart terimler size karışık geliyorsa Unicode seçeneğini kullanmak uygun olacaktır.

Karakter encoding deklerasyonu dökümanın başlangıcında karakter encoding decleration denilen kısımda yapılır.Bu deklerasyon kısmı XML attribute deklerasyonuna benzer.

<?xml version="1.0" encoding="UTF-8"?>

Burada UTF-8 değeri yukarıda bahsedilmiş olan ISO/EIC 10646 standardını bir altkümesi olarak düşünülebilir.UTF-8 ve UTF-16 karakter encoding işlemlerinde en sık kullanılan standartlardır ve bu iki encoding standardı hemen hemen tüm XML processor’lar tarafından desteklenmektedir.

Aşağıda karakter encoding işlemlerini içeren bir liste görülmektedir.

- UTF-8(Unicode)
- UTF-16(Unicode)
- ISO-10646-UCS-2(Unicode)
- ISO-10646-UCS-4(Unicode)
- ISO-8559-1 (ISO-8559-9 üzerinden)
- ISO-2022-JP(JIS X-0208-1997)
- EUC-JP(JIS X-0208-1997)
- Shift\_JIS(JIS X-0208-1997)

XML, karakter referans için iki tekniği destekler:

- decimal referans(base 10)
- hexadecimal referans(base 16)

Decimal character referans karakterin, sayısal olarak 10 tabanına gore refere edilmesi ilkesine dayanır.Decimal referans işlemi (&#) işaretini takiben karakter numarasının yazılması ve sona semicolon(;) konulması sonucu elde edilir. Genel yazımı:

&#Num;

şeklindedir.

&#169;

örneğinde bu karakter referans işleminde desimal olarak 169 değerine karşılık gelen karakter değeri(bu copright işaretine karşılık gelir.)

Şimdi copright işaretine karşılık gelen bu karakter değerinin refere edilme işlemine bir gözatalım:

&#169;1999 Emre Ultav

Refere etme işlemi sırasında kullanılan diğer bir teknikde base-16 tekniği yani hexadecimal tekniktir.Bunun genel yazılımı ise

&#xNum;

şeklindedir.

Tekniğin temel işleyişi aynıdır.

Decimal olarak 169 değerine sahip olan karakter hexadecimal olarak refere edileceğinde:

&#xA9;

şeklinde refere edilecektir.

**Entity’ler ile Çalışmak **

Bir XML dökümanı en az bir tane entity içerir.İçerilen bu entity, "document entity" olarak isimlendirilir ve bir XML processor yapacağı işlemlere document entity’den başlar.Çünkü document entity döküman hiyerarşisini şekillendirir.

XML dökümanı içerisinde yer alacak olan entity’ler kullanılmadan önce deklare edilmek zorundadırlar.Bir entity deklerasyonu unique bir entity ismi ve bu isme eklenmiş olan bir veri parçasını içerir.Belirtilen bu unique isim değerine aşağıdakilerden birini ekleyebiliriz:

- bir metin dizisi
- bir DTD bölümü
- XML metini içere bir dışsal referans(External referans)
- Binary veri içeren bir dışsal referans(External referans)

Görüleceği gibi entity’ler depolayacağı veriler incelendiğinde son derece esnek bir yapıda oldukları anlaşılmaktadır. Ancak genel hatları ile incelendiğinde entity’ler XML dökümanı içerisinde iki şekilde kullanılırlar:

- parsed entity’ler
- unparsed entity’ler.

Parsed entity’ler XML parser tarafından parse edilmiş veriyi depolarlar.Yani sadece metin(text) içerebilirler.Diğer yandan unparsed entity’lerde ise veri parse edilmemiştir ve dolayısıyla bir metin veya binary veri depolanabilir.

Parse edilmiş entity’ler döküman açısından biraz daha değişik anlamda incelenirler.Bu tür entity ler iki ana gruba ayrılırlar:

- Genel entity’ler-döküman içeriğinde kullanılan entityler
- Parameter entity’ler-sadece DTD içinde kullanılan entity’ler

---
*Kaynak: `XML/ekitap-Anonim-XML/XML.HTM`*
*Görseller: `XML/gorseller/` (5 dosya)*
