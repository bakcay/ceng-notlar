# XML Ve XML Uygulamalari

## **XML ve XML UYGULAMALARI**

**SEMİNER NOTU**

*Doç. Dr. Selim Akyokuş*

*Bilgisayar Mühendisliği Bölümü*

*Doğuş Üniversitesi*

sakyokus@dogus.edu.tr

**I. GİRİŞ**

XML açılımı Extensible Markup Language (Genişleyebilir İşaretleme Dili)’dir.

XML, elektronik ticaret, elektronik veri değişimi, terdarik zinciri bütünleştirmesi, veri yönetimi, akıllı arama makinaları gibi bir çok alanda stratejik bir araç olarak kullanılacak basit ve esnek metin biçimi teknolojisidir. XML’in özellikleri veri yapılarını, içeriklerini ve kavramlarını platform, şirket ve dilden bağımsız bir yapıda temsiline imkan vermektedir. XML uygulamalarımıza özel kendi işaretleme dilleri tanımlamamızı sağlayan bir meta dildir.

Bu seminer notunda işaretleme dilleri ve tarihçesi, HTML dili ve sınırlamaları, XML dili ve XML tabanlı teknolojiler ve uygulamalar, XML söz dizimi (syntax) kuralları, XML DTD belge tipi tanımlamaları, XML şemaları, CSS ve XSL ile XML belgelerinin biçimlendirilmesi, XML belgelerinin işlenmesi gibi XML temel konular örnekler verilerek açıklanmıştır.

**II. İŞARETLEME DİLLERİ VE TARİHÇESİ **

XML’in ne olduğunu tanımlayabilmemiz için önce Markup Language (İşaretleme Dili) ne anlama geldiğini açıklamakta fayda var. Basılı yayının gelişmesiyle yayıncıların yazılı metinlerin baskı makinalarında nasıl bir şekilde biçimde yayınlanması için hazırladıkları notlar ve özel sembolller *markup* olarak ifade edilmekteydi. Bu metinin belirli kısımlarının özel bir anlam kazandırmak üzere işaretlenmesi işlemidir. Bu amaçla kullanılan işaretler, kurallar ve gramer kümesi *markup language* (işaretleme dili) tanımlanır. Bu tip işaretleme yapılarını biz bir çok ortamda görebiliriz. Örneğin ASCII kodlama standardının içerdiği bir çok kontrol karakteri veri iletişimi için kullanmaktadır. Kelime işlem programları bir metin’nin içerdiği kısımları, yazı tiplerini, font ve stilleri ayırmak için metin içeririsine gömülü bir çok işaret’leri içermektedir. Programlama dilleri fonsiyonları, data yapılarını, verileri ayırmak için bir takım sembolller veya işaretler kullanmaktdadır. Bu tip bir standard ayıraç, işaret veya etiketler kümesi kullanmadan taşınabilir ve paylaşılabilir bir uygulama geliştirilebilmesi çok güçtür.

Metin ve belgelerin kolay bir şekilde taşınabilmesi, paylaşılabilmesi ve işlenebilmesi için ilk işaretleme dili GML (Generalized Markup Language) 1960 sonlarında IBM’de yapılan araştırma çalışmaları sonunda ortaya çıktı. GML daha sonra ANSI (American Natitional Stardard Institute) 1978 te oluştuturlan bir grup tarafından geliştirilerek SGML (Standardized Generalized Markup Language) adı altında 1986 yılında ISO (the International Organization for Standardization) kurumunca uluslararası bir standard olarak kabül edildi \[1\]. SGML bir metin veya belge kümesinde kullanılan dilin gramer ve sözlük yapısını belirtmek için kullanılan bir dildir. SGML Amerikan hükümeti kuruluşlarında, havacılık ve otomobil gibi büyük endüstri kuruluşları ve basın endüstrisinde bir belgeleme standardı olarak kullanılmaktadır. SGML çok güçlü bir dil olmasına rağmen son derece karmaşık yapısı ve yüksek uygulama geliştirme maliyeti bu dilin yaygın bir şekilde kullanımını engellemiştir.

Tim Berners-Lee ve Anders Berlung 1989 yılında internet ortamında belge paylaşımını kolaylaştırmak için Web uygulamalarının temel öğelerinden biri olan HTML (Hypertext Markup Language) dilini geliştirdiler. HTML bir SGML uygulaması olarak geliştirildi. Diğer bir deyişle HTML dilinin yapısı SGML dilinde tanımlandı. HTML dili çok basit yapısı ile son derece başarılı oldu. Albert Einstein’nin dediği gibi her şey daha basit olmamalı ama mümkün olduğunca basitleştirilmelidir\[2\]. HTML dili bir belgenin içerdiği başlık, font, resim ve tablo gibi bilgileri bilgisayar ortamında standard bir şekilde görüntülemek ve biçimlendirmek için geliştirilmiş bir dildir. Belgenin istenen formatta sunulması *tag *(etiket) olarak ifade edilen işaretler ile sağlanmaktadır. Bu dilin geliştirilmesindeki temel amaç belgenin standard bir formatta görüntülenerek sunulmasıdır. Bu dilin yalnızca web tarayıcıları için sunum amaçlı olarak geliştirilmesi bugunkü web uygulamalarının gerekirdiği daha sonra açıklayacağımız bir çok kısıtlamalar XML dilinin geliştirilmesine yol açtı.

1996 yılında Word Wide Consortium (W3C, http://www.w3.org)’u SGML güç ve esnekliğini içereçek basit bir işaretleme dili oluşturmak amaçıyla XML dilini tasarlamaya başladı. Şubat 1998’de XML 1.0 bir standard olarak W3C tarafından yayınlandı. XML dili SGML dilinin bir çok özelliğini içeren basitleştirilmiş dildir. SGML dilinin bir alt kümesidir. XML SGML gibi bir meta dildir. Yani başka dillerin yapısını tanımlamakta kullanılan bir dildir.

**III. HMTL : Biçimsel ve İçeriksiz**

HTML dili bir belgenin formatlanması amaçıyla daha önceden tanımlanmış bir etiket (tag) kümesine sahiptir. Her bir etiket özel bir formatlama anlamı içerir. Şekil 1’deki HTML örneğine bakalım. Burdaki <P> etiketi bir paragrafın başını göstermektekdir. </P> ise paragrafın bitiş etiketidir. Tarayıcı bu etiketlere bakarak bu başlangıç ve bitiş etiketleri arasındaki metini bir paragraf olarak yorumlayarak buna göre biçimlendirme işlemini gerçekleştirecektir. <b> ve </b> ekiteleri ise bu iki etiket arasındaki metinin bold (kalın) fontta basımı sağlayaktır. <br> etiketi ise yeni bir satır başına geçilmesini ifade eden satır atlama etiketidir.

Bu örnekte gördüğümüz gibi HTML dilindeki bir çok etiket yalnızca biçimlendirme ile ilgili tarayıcın kullandığı bir anlam ifade etmektedir. HTML’in bu yapısı esnek, güçlü ve çok amaçlı bilgi sistemlerinin geliştirilmesini engellemektedir. HTML’in bu anlamda getirdiği bu takım sınırlamalar şunlardır\[2|:

HTML genişleyebilir bir dil değildir. HTML daha öceden tanımlanmış sabit bir etiket kümesi içermektedir. Bu etiket kümesini uygulamara özgü kendimizin ekleyeceği yeni etketlerle genişletemeyiz.

HTML yalnızca sunum amaçlıdır. HTML etiketlerinin bir çoğu tarayıcının metni yalnızca nasıl biçimlendirmesi ile ilgili bilgi içermektedir. Veri kopyalama, paylaşımı, iletişimi ve uygulama bütünlenleştirmesi gibi diğer ağ uygulmalarının gereksinimlerine cevap vermemektedir.

HTML belgeleri genellikle direkt olarak yeniden kullanılamazlar. Örneğin, bir hava tahminleri hakkında bilgi veren bir sitedeki bir HTML belgesindeki sıcaklık, ve hava tahminleri ile ilgili bilgileri kendi uygulamamızda kullandığımızı düşünelim. Kendi uygulamamız bu sayfanın yapısını inceleyerek bu bilgileri istediğiz formata dönüştürsün. Hava tahmini sitesindeki en ufak bir değişiklik olması durumunda bizim uygulamamızı değiştirmemiz gerekeçektir. Bunun temel nedeni bir HMTL belgesi içindeki bilgi içeriğiyle sunum yapısının birbirinden ayrılmamasıdır.

HTML verilerinizin yalnızca bir "görüntüsü"nü sağlar. Kullanıcı isteklerine bağlı olarak bir HTML belgesindeki bilgilerin farklı formatlarda görüntülenmesini istersek bu işlem HTML ortamında çok zor olaçaktır. Bunun işlemi gerçekleştirmek için çok fazla script kodu yazmamız gerekçektir.

HTML verileri çok az veya hiçbir anlamsal yapı bilgisi içermezler. Örneğin yukarıda vermiş olduğumuz adres örneğinde metin içeriği hakkında ise hiç bir bilgi yoktur. Bu metne bakarak bir uygulamanın bu metindeki hangi verinin ad, soyad veya posta kodu olduğunu anlaması zordur.

**IV. XML NEDİR ?**

XML’de HTML gibi işaretleme etiketlerini kullanan dildir. HTML ve XML arasındaki temel fark XML işaretleme etiketlerinin bilginin içeriğini tanımlamak için kullanılmasıdır. XML bir meta dildir. Diğer bir deyişle diğer yeni işaretleme dillerini tanımlamak için kullanılan bir dildir. XML ile herhangi bir uygulama için bir XML belgesinin içinde bulunacak verinin içeriği ve içerdiği veri tiplerini tanımlayacak uygulamaya özel bir işaretleme dili tanımlayabilirsiniz. Meta veri (Metadata veya Metainformation) veri hakındaki bilgidir. XML etiketleri veri hakındaki meta bilgiyi tanımlamaktadır. Şekil 2’deki XML adres listesi belgesi örneğindeki etiketler adres içinde geçen veriler hakkında bilgi vermektedir. Başlagıç <contact> ve bitiş </contact> etiketleri arasındaki verilerin adres bilgisi olduğunu bildirmektedir. Bu belgenin içindeki başlagıç ve bitiş etiketlerine bakarak bir uygulama bu bilgilerin ne gibi bilgi içerdiklerini kolay bir şekilde çıkarabilir. Örneğin <city> başlangıç ve </city> arasındaki “New yok” verisinin şehir bilgisi olduğunu kolayca anlaşılabilir.

Bu belge örneğinde gördüğümüz gibi XML belge içindeki verinin içeriği tanımlayan

etiketler içermekdedir. Belgenin web tarayıcılarında nasıl formatlanacağı konusunda herhangi bir bilgi yoktur. Belgenin formatlanması daha sonra göreceğimiz CSS veya XSL teknolojileri yapılabilir.

Şu ana kadar bu örnekte belge içinde hangi etiketler hangi yapıda kullanılabilir belirmedik. Bir belge içerisinde her hangi bir etiket ismi verip bu etiketi belge içinde kullanabilirmiyiz? Elbeteki hayır. Bir uygulamadaki XML belgesinin yapısı ve içereçeği etiketler o uygulama için geliştirilmiş olan olan özel işaretleme dili ile tanımlanır. Bu işaretleme dilinin yapısı ise XML DTD (Document Type Definition) veya XML schema olarak adlandırılan belge tanımlama dosyalarında belirtilir. Şekil 3’te yukarıdaki adres listesi örneği için tanımlanmış bir DTD dosyasını göstermektedir. Bu dosyada bu DTD’ye göre oluşturulmuş bir adres listesinde hangi etiketlerin bulunabileçeğini, bu etiketlerin hangi etiketleri içerebileceği gibi bilgiler vermektedir. İlk satır <adressbook> etiketinin bir veya daha fazla <contact> etiketi içereceğini belirmektedir. İkinci satır ise bir <contact> etiketinin içinde geçecek elemanları belirlemektedir.

**V. XML TABANLI TEKNOLOJİLER VE UYGULAMALAR******

XML değişik veri, kavram ve içeriklerin tanımlanması ve temsil edilmesi için uygun bir ortam sunmaktadır. Bu nedenle XML farklı alanlarda uygulama verilerinin tanımlanması ve taşınması için üretici, dil, ve platformdan bağımsız stratejik bir araç olarak hızla yaygınlaşmaktadır. Aşağıda XML’in kullanıldığı ve kullanılaçağı bazı temel uygulama alanları tanıtılmıştır.

**Internet Arama Makinaları**

Internet çok büyük bir haçimdeki yapısal olmayan veri içermektedir. Bir arama makinasının (search engine) ingilizçe “chip” kelimesini aradğını düşünelim. Karşımıza “chip” kelimesini içeren binlerce doküman gelecektir. Bu dokümanlar patates “chip”leri, bilgisayar “chip”leri veya “chip” isimli kişiler hakında olabilir. Şu anda Internet belgeleri HTML ortamında saklandığından veri içeriği hakkında her hangi bilgi yoktur. XML yaygın bir şekilde Internet’te belge saklama ortamı olarak kullanıldığında, arama makinaları veriler hakında verilen bilgileri (metadata) kullanarak daha akıllı seçimler sunabilecektir.

**Aygıt ve Uygulamadan bağımsız Veri Erişimi**

Şu andaki Web ortamındaki HTML belgelerine masaüstü bilgisayarlardaki tarayıcı (browser) programları kullanarak erişilmektedir. Bu yapı değişmeye başlamıştır. Cep telefonları ve kişisel sayısal yardımcı PDA (Personel Digital Assistant) gibi araçlar ile bugün web erişimi hızla artmaktadır. Bu araçlardaki görüntü, band genişliği, bellek ve işlemçi sınırlamaları Web’te yeniden bir yapılanmayı gerektirmektedir.

HTML dili belgelerin Web tarayıcılarında gösterilmesi amaçı ile geliştirlmiştir. XML belge içeriğini belge sunumundan ayırmaktadır. XML ortamındaki belgeler aygıtın yapısına bağlı olarak istenilen şekilde formatlanarak sunulabilir. XML tabanlı bilgilere erişim cep telefonu gibi bir aygıtla erişileceği gibi bu iş amaçlı bir web uygulaması ilede olabilir. Bu uygulama XML ortamındaki bilgi içeriğini alarak istediği şekilde kullanabilir veya formatlayabilir. Örneğin aşağıda bir ürün hakındaki bilgiler XML formatında verilmiştir. Bu ürün hakkındaki bilgiler Şekil 4’te görüldüğü gibi XML işlemcisi tarafından farklı ortamlarda sunulabilir.

**Elektronik Veri Değişimi ve Elektronik Ticaret**

XML’in en fazla ilgi çeken tarafı e-ticaret, tedarik zinciri yönetimi ve iş akışı (workflow) yönetimi gibi elektronik iş web uygulamalarında bir veri değişim formatı olarak kullanılmasıdır. Bugünkü bilgisayar iletişimindeki çok büyük gelişimlere ve birikime rağmen, bilgisayar sistemlerindeki ve veritabanlarındaki farklı formatlardaki verilerin şirket içi ve şirketler arası taşınması ve işlenmesi en büyük problemlerden birisidir. Bu verilerin XML formatına dönüştürülerek taşınması bu problemin çözümünü kolaylaştırmaktadır.

**Basın ve Yayıncılık**

XML basın ve yayıncılık için geliştirilmiş olan SGML dilinin basitleştirilerek türetilmiş bir dil olduğundan bu konuda aynı amaçla kullanılabilir. XML formatında saklanan belgeler bir çok farklı ortama XML araçlarını kullarak dönüşürülebilir ve kullanılabilir. Klasik yayıncılığın yanı sıra XML yeni elektronik yayıncılıktada kullanılabilir. Elektronik yayın ortamındaki görüntü, video, ses ve diğer sayısal veri nesneleri XML ile formatlanarak saklanabilir, taranabilir ve sunulabilir.

**Şirket Uygulamarı Bütünleştirmesi**

Şirket Uygulamaları Bütünleştirilmesi kavramı farklı uygulamaların tek bir uygulama gibi davranması olarak ifade edilebilir. Bu işlem farklı sistemlerdeki veri kopyalarının ve dağıtık bir yapıdaki verilerin doğru zamanda ve doğru yerde bulunmasını gerektirir. Örneğin bir muhasebe sistemi ile satış sistemini birleştirmek için satış siparişi bilgilerinin faturaların oluşması için muhasebe sistemine aktarılması gerekebilir. Aynı şekilde fatura verilerininde muhasebe sistemine aktarılması gerekebilir. Bu aktarma işlemleri doğru bir şekilde yapıldığında her bir iş hareketi otomatik olarak gerekli uygulama sistemlerine işlenerek güncellecektir.

**Yazılım Geliştirme**

XML büyük çaplı uygulama gelişmede uygulama mimarilerinin paylaşımını kolaylaştıracaktır. OMG (Object Management Group) bir XML tabanlı bir uygulama olan XMI (XML Metadata Interchange) spesifikasyonunu kullanacağını belirmiştir. XMI, UML (Unified Modelling Language) kullanarak tasarlanmış olan uygulamaları tanımlamada kullanılan bir dildir. XMI, geliştirme ekibinin çok farklı uygulama geliştirme araçlarını kullanarak, tek bir UML modelinin paylaşımına imkan vermektedir. Bu yazılım geliştirme sürecinde geliştirme ekibi arasındaki iletişimi artırarak geliştirme sürecini kısaltmakta ve ekibi daha üretken kılmaktadır.

Yazılım geliştiricileri XML meta bir dil olduğundan uygulamalarının gerektirdiği yeni dilleri gelişitirebilir. Bu dillerde tanımlanmış olan verileri ve yapıları hazır olarak bulunan XML kütüpaneleri ve araçları ile kolaylıkla işleyebilir.

**VI. XML SÖZ DİZİMİ (SYNTAX)**

XML belgeleri işaretleme ifadeleri ve veri içeriğinden oluşan bir veri dosyası veya paketidir. İşaretleme ifadeleri elemanlar (elements), varlık referansları (entity refererences), açıklamalar (comments), işleme komutları (processing instructions), CDATA bölümleri ve veri tipi tanımlamalarından (document type declaretions) oluşur.

XML’de geçen temel işaretleme ifadelerini detaylı incelemeden önce aşağıdaki Şekil ‘teki örneği inceleyelim. Bu örnekte XML dilinde tanımlanmış basit bir elektronik posta verilmiştir. Belgenin ilk satırı <?xml ... ?> her zaman tanımlanması gereken XML işlem komutu deklarasyonudur. Bu belgenin bir XML belgesi olduğunu ve hangi versiyonu kullandığını belirmektedir. İkinci satır opsiyonel olarak tanımlanabilen belge tipi deklarasyonunudur. Bu belge için tanımlanmış olan DTD (Veri Tipi Tanımlama) dosyasının isminin e\_posta.dtd olduğunu ifade etmektedir. Bunların altındaki kısım XML belgesinin gövdesini oluşturmaktadır. XML belgesi gövdesi hiyerarşik bir ağaç yapısında oluşmuş belge elemanlarından oluşur. Her bir eleman bir başlangıç ve bitiş etiketi içerir. Örneğin aşağıdaki *tarih* elemanı *<tarih>* başlangıç etiketini, *7 Eylül 2000* karakter verisini ve *</tarih>* bitiş etiketindan oluşmaktadır. Elemanlar diğer elemanları veya karakter verileri içerebilir. Bu örnekte *e\_posta* elemanı *kime*, *kimden*, *tarih*, *konu*, ve *mesaj* elemanlarını içermektedir. Bir belgenin en üst seviyesinde bulunan eleman kök eleman olarak adlandırılır. Bu örnekte kök eleman *e\_posta*’dır.

**Elemanlar (Elements)**

Elemanlar XML dilinin en temel yapı taşlarıdır. Bir eleman veri içeriğini kapsayan bir kutudur. Karakter verileri, diğer elemanları veya diğer işaretleme yapılarını içerebilirler. Elemanlar etiketlerle ayrılırlar. Her bir etiket bir eleman tip ismi (element type name) içerir ve bir çift (“<>”) açı parantezle içe alınır. Eleman tip isimlerini oluşturmakta olan kurallar diğer programlama dillerindeki isim kurallarına benzemektedir. Her bir isim bir harfle veya alt çizgi (\_) başyababilir. Tire (-) veya sayı ile başlayan isimler kulanılamazlar.

Boş elemanlar (empty elements) haricindeki her bir elemanın bir başlagıç etiketi bir de bitiş etiketi bulunur.

**Başlangıç Etiketleri **

Bir elemanın başlama ayıraçı başlangıç etiketi (start-tag) olarak adlandırılır ve bir çift (“<>”) açı parateziyle kapatılır. Aşağıda bir bazı doğru başlangıç etiketleri verilmiştir.

Unutulmaması gereken bir diğer kural XML dili harflerin büyük veya küçük olmasına duyarlı (case sensitive) olduğudur. Örnekteki <Kitap> ve <kitap> etiketleri aynı değildirler.

**Bitiş etiketleri **

Bir elemanın bitiş ayıraçı bitiş etiketi (end-tag) olarak adlandırılır. Bitiş etiketi eleman tip ismi öcesinde bir bölü (“/”) karakteri içerir ve açı parantezleri ile kapatılır. Aşağıda bitiş etiketi örnekleri verilmiştir.

XML’de her bir başlangıç etketi bir bitiş etiketi ile mutlaka kapatılmalıdır. Başlangıç bitiş etiketi ile kapatılmış bir tam XML elemanı aşağıdaki gibidir.

**Boş Eleman Etiketleri **

Aşağıdaki örnekteki ilk satırda olduğu gibi boş elemanlar (empty elements) her hangi bir içerik içermezler. Boş etiketler istenirse etkiketin sonuna tek bir bolü (/) işareti eklenerek kısatılmış bir biçimde gösterilebilir. İkinci satırda bunun bir örneği verilmiştir.

**Belge Elemanı **

XML belgeleri mutlaka hiyerarşik etiket yapısında olmalıdır. Etiket hiyerarşisi içindeki en üst sevyideki etiket kök etiket (Root tag) veya belge kökü (Document root) olarak adlandırılır. Kök etiketin oluşturduğu eleman Belge elemanı (Document Element) olarak adlandırılır. Bu eleman belgenin ağaç yapısındaki diğer bütün elemanları içine alır ve diğer bir elemanın içinde bulunamaz. Örneğin Şekil 4’te verilen elektronik posta örneğinde belge kökü e\_posta’dır.

Elemanlar iç içe yuvalandığında yuvalama (nesting) kurallarına uymalıdırlar. Yoksa bu bir XML belgesinin hiyerarşik ağaç yapısını bozacaktır. Aşağıda bir yanlış yuvalama örneği verilmiştir.

Aşağıda doğru bir yuvalama örneği verilmiştir.

**Özellikler (Attributes)**

Elemanlara eklemek istediğimiz ek bilgiler özellikler olarak ifade edilir. Özelikler başlangıç etiketi içerisinde isim ve değer ikilileri olarak geçer. Aşağıda bir özellik örneği verilmiştir:

Buradaki kitap\_no kitabın bir özelliğidirr. Özellik değerleri mutlaka çift tırnak (“) veya tek tırnak (‘) içine alınmalıdır.

**Karakter Veri**

Bir elemanın başlangıç ve bitiş etiketleri içinde geçen metin içeriği karakter veri (character data) olarak adlandırılır. XML içinde özel amaçlı olarak kullanılan (&,<,>,”,’) karaterleri olduğu gibi bir karakater veri içerisinde geçemezler. Bu karakterler işaretleme etiketleri içinde özel amaçlarla kullanılan ayıraçlardır.

XML’de HTML’den farklı olarak etiketler içine yazılmış olan veri içerisinde geçen boşluklar (White Space) korunur ve uygulamalara iletilir. Etiket tanımları içerisinde veya özellik tanımı içerisinde geçen boşluklar ise HTML’de olduğu gibi parser tarafından yok edilir.

**Karakter ve Varlık referansları**

SGML ve HTML gibi ASCII karakter seti içinde karakterleri göstermek için XML iki yöntem kullanmaktadır. Birinici yöntem karater refereranslarıdır. Karater referansları gosterilecek karateri onluk bir sayının başına “&#”, onaltılık bir sayının başına ise “&#x” ekleyerek gösterme imkanı sağlar. Örneğin copyright karateri © ondalık olarak “&#169” veya onaltılık olarak “&#xA9” XML’de gösterlebilir.

Varlık referansları verilecek bir isim vasıtasıyla istenilen karaterleri göstermek için kullanılır. Varlık referansları bir amersend (&) karateri, bir isim ve noktalı virgülden (;) oluşur. Örneğin XML’de özel olarak kullanılan (&,<,>,’,”) karakterleri (&amp; &lt; &gt; &apos; &quot;) varlık referansları ile gösterilir. Bu referanslar XML de daha önce tanımlanmış standard referanslardır. Bu referanslar haricinde özel olarak kullanmak isteiğimiz varlık referansları DTD içinde tanımlanmalıdır.

**Açıklamalar (Comments)**

Açıklamalar HTML’de olduğu gibi “<!--“ ile başlar ve “-->” ile biter. Açıklamalar bir XML belgesinin herhangi bir kısmında geçebilir ve belgenin bir parçası sayılmazlar.

**İşlem Komutları (Processing Instructions)**

XML belgelerini kullanan uygulamalara her hangi bir komut geçilmesi istenildiğinde bu işlem komutları ile yapılır. İşlem komutları aşağdaki yapıya sahiptir:

İşlem komutları XML işlemiçisi tarafından uygulamaya iletilir. İşlem komutları açıklamalar gibi bir XML belgesinin parçası sayılmazlar.

**CDATA bölümleri (CDATA Sections)**

CDATA bölümleri XML’de kullanılan işaretleme ifadelerinin göz ardı edilmesi gereken metinleri yazmada kullanılır. XML parsır’ı bu bölümde metin içerisinde yer alan işaretleme ayıraçlarını ve etiketlerini normal karaterker olarak algılar. Bir CDATA bölümü şu yapıya sahiptir:

Bu yapıda “...” olarak ifade edilen kısım “\]\]” hariç herhangi bir metini içerebilir. Aşağıda bir CDATA bölümü örneği verilmiştir.

**XML Veri Tipi Tanımlamaları (DTD)**

**Belge Tipi Deklarasyonu (Document Type Declaration)**

Belge tipi deklarasyonları bir XML belgesinin giriş kısmında tanımlanan belgenin gramer tanım kurallarını belirleyen hangi harici ve dahili DTD (Document Type Definiton)’yi kullandığını belirtir. Bu kısım varlık referansı tanımlamaları gibi ek bilgilerde içerebilir. Harici belge tipi deklarasyonları şu formatta olabilir:

Bu tanımdaki kök\_eleman\_ismi belge DTD’sinde en üst seviyede tanımlanan kök elemanı belirtir. Sistem\_tanımlayıcısı ise harici olarak kullanılan DTD’ye URI (Uniform Resource Idenifier) bir referansı içerir. İkinci satırdaki formatta XML parser’ı ilk önce public\_tanımlayıcısı’nı kullarak bir URI referansı oluşturmaya çalışır. Eğer bu mümkün olmazsa sistem\_tanımlayıcısı’ndaki referansı kullanır. Aşağıdaki Şekil 2’de verilen adres belgesinin belge tipi deklarasyonu kısmı gösterilmiştir:

İlk satır adres belgesindeki kök elemanın adressbook olduğunu belirtmektedir. Belgenin DTD’si **http://xyz.com/AddressBook.dtd** dosyasında saklanır. Bunun haricinde köşeli parantez içinde tanımlanan kısım ise varlık referanslarını tanımlamaktadır. Bu kısımda istenirse dahili belge tipi tanımlamalarıda bulunabilir.

**İyi Oluşmuş (Well-formed) ve Doğru (Valid) Belgeler**

XML söz dizimi (syntax) kurallarına uyan XML belgeler iyi-oluşmuş (Well-formed) belgeler olarak adlandırılır. Eğer belge için tanımlanmış olan DTD’de geçen gramer kurallarına uyuyorsa bu durumdaki belgelerde doğru (Valid) belgeler olarak adlandırılır.

**VII. DTD (DOCUMENT TYPE DEFINITION) BELGE TİPİ TANIMLAMALARI **

DTD’ler bir belgenin yapısını belirlerler. XML’in ilk harfinde geçen genişleyebilir kelimesinin (Extensible - X) anlamını ifade eden yeni yapılar tanımlamamıza imkan verir. Herhangi bir alandaki uygulamalarda kullanılacak yeni işaretleme dillerini (markup languages) DTD’ler ile geliştirebiliriz. Bu amaçla geliştirilmekte şu anda onlarca XML işaretleme dili vardır. Bu diller XML uygulaması (application) veya XML sözlüğü (vocabulary) olarak anılmaktadır. XML sözlükleri bir alandaki bilgi değişimi ortamını sağlamak için tanımlanmış işaretleme dilleridir. Bazı XML sözlükleri örnekleri aşağıda verilmiştir:

Synchonized Multimedia Integreration Language (SMIL)

Chemical Markup Language (CML)

Bioinformatic Sequence Markup Language (BSML)

Common Business Library (CBL)

Bu yeni diller için tanımlanan DTD’ler bu dilin hangi etiketleri içerbileceği, etiketlerin sahip olabileceği özellikleri, hangi elemanların diğer hangi elemanları içerebileceği gibi dil yapısı bilgilerini (gramer) içerir.

Bilgisayar ortamında dillerin gramer’leri genellikle EBNF (Extended Backus-Naur Form)’da tanımlanır. XML belirtimide (XML Specification) original olarak EBNF notasyonunda belirtilmiştir. XML 1.0 belirtimi http://www.w3.org/TR/REC-xml adresinden elde edilebilir. EBNF dili yapı kurallarını içerir. Her bir yapı kuralının sol tarafı yapının ismini sağ tarafı ise yapıyı tanımlar. Bir kişinin bir isminin şart olmasının gerektiğini ve opsiyonel olarak telefon numaralarının bulunabileceğini EBNF’de şu şekilde ifade edebiliriz.

Aynı yapı DTD’de şu şekilde tanımlanabilir.

Bir XML belgesinin yapısı DTD’de aşağıda verilan dört çeşit işaretleme ifadesi ile tanımlanır.

| DTD ifadesi | Anlamı |
| --- | --- |
| ELEMENT ATTLIST ENTITY NOTATION | Bir XML elemanı tanımlar. Bir eleman tipinin alabileceği özellikleri tanımlar. Belli bir içeriğin bir isme bağlanarak o isimle ilişkilendirilmesini sağlar. XML hariçi içeriğin tanımlanmasını sağlar. Bu tanımlaran içerik XML belgesinin bir parçası olarak parse edilmez. |

**Elemanlar**

Elemanlar bir XML belgesinin en temel yapılarıdır ve ELEMENT etiketi ile tanımlanırlar. Dört çeşit eleman tipi vardır:

Empty (Boş) : Eleman herhangi bir içerik içermez. Elemanın özellikleri olabilir.

Element Only (Yalnızca Eleman) : Eleman yalnızca alt seviye (child) elemanları içerebilir.

Mixed (Karışık) : Eleman alt seviye elemanlar ve karakter veri karışımını içerebilir.

Any : Eleman DTD’in izin verdiği içeriği içerebilir.

**Boş (Empty) Elemanlar**

Boş elemanlar aşağıdaki formatta tanımlanır.

Örneğin

Boş eleman XML belgesi içerisinde daha önce açıklandığı gibi eğer bir özelliği yoksa

aşağıdaki ilk iki satırdaki gibi geçecektir:

Yukarıdaki örnekte alttaki iki satırda *img* elemanı *src* adlı bir özellik içermektedir.

**Yalnızca Eleman İçeren (Element Only) Elemanlar **

Bu tipteki elemanlar aşağıdaki formattadır.

Bu yapıda İçerik-Modeli yalnızca bu elemanın altında kalacak alt elemanları içerebilir.

Örneğin Şekil 4’te verilen elektronik posta kök elemanı e-posta’nın tanımı aşağıdaki gibidir.

Bu örnek e-posta elemanı *kime*, *kimden* ve *mesaj* alt elemanlarını mutlaka gösterilen sırada XML belgesi içinde geçmesi gerektiğini göstermektedir*. Tarih* ve *konu* elemanları ise opsiyoneldir. Bu elemanların opsiyonal olduğunu (?) sembolü göstermekdedir. XML’de çeşitli amaçlarla kullanılan sembollerin anlamları aşağıda listelenmiştir:

| **Eleman** **Tanımı** | **Anlamı** |
| --- | --- |
| **A?** **A+** **A\*** **A,B** **A \| B** ( ) | Opsiyonel; A alt elemanı bir defa veya hiç gözükmeyebilir. A alt eleman mutlaka bir defa veya daha fazla gözükür. A alt eleman sıfır veya daha fazla gözükebilir. B elemanı A’dan sonra gözükmelidir. A veya B’den bir tanesi gözkebilir. Paratez içinde geçecek elemanları guruplar. Örneğin (A,B)+ ifadesi A ve B’nin ardışık olarak bir veya daha fazla geçeceğini götermektedir. |

Aşağıdaki bu sembolleri kullanan bir özgeçmiş elemanı örneği verilmiştir:

**Karışık (Mixed) Elemanlar**

Karışık elemanlar hem karakter veri hemde alt elemanları içerebilirler. Karakter veri **#PCDATA** terimi ile gösterilir ve parsed karakter veri anlamındadır. Aşağıda Karışık eleman örnekleri verilmiştir:

İlk satırdaki ifade *konu* elemanının yalnızca karakter veri içereçeğini göstermektedir. Bu tip yalnızca veri içeren eleman tanımlarında #PCDATA parantez içine alınmalıdır.

İkinci satırdaki karmaşık *not *elemanın karakter veri, tarih veya konu elemanlarından oluşabileceğini göstermektedir. Aşağıda buna bir örnek verilmiştir.

**ANY elemanları**

ANY tanımının formatı aşağıdaki şekildedir.

ANY elemanları herhangi bir yapıya sahip değildir. ANY elemanı karakter veri, tanımlanmış elemanlar veya bunların bir karışımını içerebilir. ANY elemanları her hangi bir yapı belirtmediği için kullanılması tavsiye edilmez.

**Özellikler (Attributes)**

Daha öncede belirtildiği gibi özellikler elemanlar hakında ek bilgi tanımlamak için kullanılır. Bir eleman hakkındaki özellik bilgileri aşağıdaki formatta tanımlanır.

Bir özellik bir isim ve tip bilgisini içerir. *Default *bir değer olabilir veya özellik kullanımı hakkında bilgi verir. Dört çeşit default değer tipi aşağıda verilmiştir.

| Default | Anlamı |
| --- | --- |
| **#REQUIRED** **#IMPLIED** **#FIXED ***Değer* *Değer* | Özellik her zaman tanımlanmalıdır. Özellik opsiyoneldir. Özellik sabit bir *Değer’*e sahiptir. Özellik eleman içinde tanımlı olmazsa, parser bu sabit *değer*’in olduğunu varsayar. Özellik eleman içinde tanımlı olmazsa, parser bu *değer*’in olduğunu varsayar. Eğer tanımlı ise özellik farklı bir değer içerebilir. |

Örneğin aşağıdaki örnekte Kitap elemanının BasımTarihi diye bir özelliğinin olduğu ve bu özelliğin karater veri olduğu (CDATA) belirtilmektedir.

Bu özellik bir XML belgesi içinde şu şekilde geçebilir:

Aşağıdaki örnek kitap *Basım-Sayısı* özelliğinin opsiyonel olduğunu göstermektedir.

Aşağıdaki örnek *deniz* elemanının *renk* özelliğin sabit olarak mavi değerine sahip olduğunu göstermektedir.

Aşağıdaki örnek *elma* elemanının *renk* özelliğinin default olarak *kırmızı* olduğunu göstermektedir.

XML 10 değişik özellik tipini destekler. Bu özellik tipleri şunlardır.

| **Özellik Tipi** | **Anlamı** |
| --- | --- |
| **CDATA** **Enumarated** **NOTATION** **ENITITY** **ENTITIES** **ID** **IDREF** **IDREFS** **NMTOKEN** **NMTOKENS** | Karakter veri (Unparsed) Özelliğin sahip olabileçeği değerler kümesi DTD’de tanımlanmış herhangi bir notation. Harici bir varlık. Bir den fazla boşlukla (white space) ayrılmış varlıklar. Bir belge içerisinde geçebilecek tek tanımlayıcı bir değer (unique identifier). DTD’te tanımlanmış olan bir ID’ye olan referans. Boşlukla (white space) ayrılmış ID’ler serisine referans. XML token karaklerlerinden (harf, sayı, nokta, tire, iki nokta, alt cizgi) oluşan bir isim. XML token karakterlerinden oluşan boşlukla ayrılmış bir çok isim. |

Enumerated özellikler bir dizi değer kümesi içerir. Özellik bunlardan bir değeri alabilir:

Aşağıdaki örnek *kalem* elemanının renk özeliğininin *mavi, kırmızı*, *yeşil* veya *beyaz* olabileceğini göstermektedir. Eğer bir renk seçilmezse default olarak *kırmızı *renk alınır.

Aşağıdaki örnek DTD’de tanımlanmış olan notation’ları özellik olarak kullanmaktadır.

Notation XML harici veri tiplerini tanımlamakta kullanılır. Bu örnek resim formatının *gif *veya *jpeg* olabileceğini belirtmektedir.

ID tipindeki özellikler değerleri bir belge içerisinde yalnızça bir defa geçebilir. Bu bize bir elemanı unique olarak tanımlamamızı sağlar. Örnegin personel diye bir elemanımız olsun. Her personel personel-no adlı bir özellik içersin. Her personelin numarası farklı olacağından bu özellik ID olarak tanımlanır.

IDREF, ID tipindeki elemanlara referans vermemizi sağlar. Örneğin mühendis adlı bir elemanımız olsun. Mühendis ile personel arasındaki bire bir ilişkiyi IDREF ile belirtebiliriz.

Bu bize mühendisin personel bilgilerini personel elemanından elde etmemizi sağlar. Aşağıda bir XML belgesi örneği verilmiştir.

IDREFS iki eleman arasındaki bire çoklu ilişkileri göstermekte kullanılabilir.

Örneğin proje-gurubu adlı bir elemanımız olsun. Bir proje gurubu bir çok personel içerecektir. Bu ilişkiyi şu şekilde belirtebiliriz:

Bu yapıdaki bir XML belgesi aşağıda verilmiştir. Bu belge 12345, 67891, 23456 nolu personelin proje gurubunda yer aldığını belirtmektedir.

Özellik değerlerininin token olarak varsayılması gereken durumlarda NMTOKEN veya NMTOKENS tipini kullanılır. Token boşluk içermeyen bir değerdir. XML parser’ı bir özelliği token olarak işlemesi durumumda aradaki boşlukları (white space) tek boşluğa indirger ve baş ve sondaki boşlukları siler. Bu işlem özellik değeri normalizasyonu (attribute value normalization) olarak adlandırılır. Aşağıda bir çok token içeren bir NMTOKENS özellik tipi tanımı ve XML ifadesi verilmiştir.

**Varlıklar (Entities)**

Varlıklar herhangi bir veri parçasına bir isim vererek bu veri parçalarına referrans vermemizi sağlar. Bunu C dilindeki DEFINE fonksiyonu gibi düşünebiliriz. Varlık tanımlamaları bir defa tanıladığımız bir değeri bir çok yerde ismi ile refereans vererek tekrar kullanabiliriz. Üç çeşit varlık tanımlaması vardır:

Genel Varlıklar (General Entities)

Parametre Varlıklar (Parameter Entities)

Karakter Varlıklar (Character Entities)

**Genel Varlıklar**

Genel varlıklar bir metin parçasına bir isim vererek bu isimle metini kullanmamızı sağlar.

Örneğin aşağıda bir şirket ismi için yapılmış tanımlama gösterilmiştir.

Tanımlamayı aşağıdaki gibi ismin başına (&) harfi ve sonunna (;) ekleyerek kullanabiliriz.

Bu ifadedeki &şirket referansı tanımlamadaki metinle yer değiştirecektir.

Genel varlık tanımlamalarını harici bir dosyaya ulaşmak içinde kullanabiliriz. Örneğin aşağıdaki tanımlaman *readme.txt* dosyasına referans tanımlamaktadır.

SYSTEM ve URL dosyanın bulunduğu yeri belirtmektedir.

**Parametre Varlıklar (Parameter Entities)**

Genel varlık tanımlamaları XML belgesi içinde bir metin için tanımladığımız isimle belgenin içinde yer almasını sağlar. Parametre varlık tanımlamaları aynı işlevi bize DTD’nin içinde yapmamızı sağlar. Parametre varlık tanımlamaları aşağıdaki formattadır:

Aşağıdaki örnekte boyut isimli bir parametre tanımı yapılmıştır.

Parametre varlıkları varlık ismi başına (%) sonuna (;) konarak DTD içinde referans edilir. Aşağıda boyut’a yapılmış olan referansları görmekteyiz.

Her üç eleaman tanımındada *%boyut;* isminin geçtiği yerlerde (*uzunluk genişlik yükseklik*) metni yer alaçaktır.

**Karakter Varlıklar (Character Entities)**

Karakter varlık referansları verilecek bir isim vasıtasıyla istenilen karaterleri göstermek için kullanılır. Karakter varlık referans tanımlamaları aşağıdaki örnekte olduğu gibi yapılır:

Bu tanımlamada ASCII kodlamada 169 copyright karakterini (©) belirtmektedir. Karakter varlık referansları bir amersend (&) karakteri, bir isim ve noktalı virgülden (;) oluşur. XML metninde *&copyright;* yazdığımız yerler © sembolü ile yer değiştirecektir.

**Notation (Gösterim)**

Notation tanımlamaları XML harici verinin ve bu harici ile ilişkindirilecek bir yardımcı uygulamanın (helper application) tanımlanmasını sağlar. XML parser XML verisi üzerinde parse işlemini yapar. XML harici verilerin işlenmesi, örneğin *gif* formatında tanımlanmış bir resim verisini, ancak bu veri formatları ile ilişkilendirilecek bir uygulama ile yapabilir. Aşağıdaki örnekte *jpg* ve *gif * formatındaki tanımlanmış verileri ilgili uygulamalarla ilişkilendirmektedir.

Bu notation jpg dosyalarını jpgviewer.exe, gif dosyalarının gifviewer.exe uygulaması ile işlenmesi gerektiğini belirtmektedir.

**VIII. XML ŞEMALARI (XML SCHEMAS)**

XML şemaları XML belgelerinin yapısını DTD’te olduğu gibi tanımlada kullanılan yeni bir yöntemdir. World Wide Web Konsonsiyumu (W3C) DTD’nin bazı sınırlamaları nedeniyle yeni bir alternative olarak 1998 yılında XML-Data **note** yayınladı. XML-Data note’u belge yapılarının bir XML sözlüğü olarak tanımlanmasını önermiştir. Bu yeni belge yapısı tanımlama yöntemi XML şema (XML Schema) olarak adlandırılmakta ve Microsoft tarafından desteklenmektedir.

XML şemaları ilgili iki tane Working Draft yayınlanmıştır. Bunlar şunlardır:

XML Schema Part 1 : Structures (http://www.w3.org/TR/xmlschema-1/)

XML Schema Part 2 : Datatypes (http://www.w3.org/TR/xmlschema-2/)

XML şemaları bir XML sözlüğü olarak tanımlandığından normal bir XML belgesi olarak işlenebilir ve parse edilebilir. Bunun yanında bir çok veri tipini desteklemesi, açık bir model olarak genişleyebilmesi, katılım (inheritance) ilişkilerini desteklemesi gibi avantajları vardır. Bu yöntem gelişme aşamasında olması nedeniyle henüz son şeklini (**recommendation**) alamamıştır.

Şekil 5 bir adres listesi belge yapısını tanımlayan DTD’yi ve bunun altında aynı amaçla geliştirilmiş olan bir XML şemasını vermektedir.

**IX. CSS ve XSL ile XML sunumu**

Daha önce bahs ettiğimiz gibi XML belge içeriği ve sunumu birbirinden ayırmıştır. XML belgelerinin görsel olarak biçimlenlendirilerek sunumu CSS (Cascading Style Sheets) veya XSL (eXtensible Style Language) kullanılarak gerçekleştirilir.

**CSS (Cascading Style Sheets)**

CSS HTML ve XML belgelerini görüntüleme amaçıyla kullanılan bir biçimleme dilidir. CSS biçim sayfaları (sytle sheets) belge elemanlarına uygulanacak olan bir kurallar kümesi içerir. Her bir kural elemanların nasıl biçimlendirleceğini belirler. Biçim kuralları aşağıdaki yapıya sahiptir:

Özellikler (properties) seçicinin (selector) belirtiği elemanların nasıl formatlanaçağı konusunda biçimleme ifadeleri içerir. Aşağıdaki HTML paragrafının mavi renkte, Arial fontunda 14pt büyüklükte göstermek istediğimizi varsayalım.

Bu pararafı istediğimiz şekilde formatlayacak bir CSS kuralı örneği verilmiştir:

HTML elemanlarının nasıl biçimlendirileceğini CSS kuralları kullanarak belirtiğimiz gibi, XML belgelerindeki elemanlarıda CSS kuralları kullanarak biçimlendiredirebiliriz.

Örneğin <isim> Selim Akyokuş </isim> elemanını kalın, 16pt ve Times font’unda biçimlendirmek için aşağıdaki CSS kuralını kullanabiliriz.

XML belgelerini CSS kurallarını içeren CSS biçim dosyasına ilişkilendirmek için xml-stylesheet işlem komutu kullanılır. Örneğin aşağıdaki işlem komutu Şekil 4’te verilen *adressbook.xml* XML belgesini *adressbook.css* CSS kural dosyası ile ilişkilendirmektedir.

Bu işlem komutunun *adresbook.xml* belgesini *adressbook.css* teki kurallara göre biçimlendirilmesi için belgenin başlangıcına konulması gerekmektedir. Şekil 4’de verilen adressbook.xml belgesini biçimlendirmek için oluşturulan *adressbook.css* CSS biçim dosyası aşağıda Şekil 6’de verilmiştir.

Şekil 4’teki XML belgesinin *adressbook.css *dosyasındaki kurallara göre Internet Explorer 5.0’daki görüntüsü Şekil 7’de verilmiştir.

CSS basit biçimlendirme işlemleri için iyi bir yöntemdir. Karmaşık biçimlendirme işlemleri için XSL dili tercih edilir.

**XSL (eXtensible Style Language)**

XSL, XML belgelerinin biçimlendirilmesi tasarlanmış bir biçimleme dilidir. CSS’den çok daha güçlü bir yapıya sahip olmasına rağmen XSL yeni bir teknoloji olduğundan çok fazla yaygın değildir ve konudaki standardlaştırma çalışmaları henüz tamamlanamamıştır. XSL dili W3C’nin aşağıdaki spesifikayonlarını kullanır:

XSLT – http://www.w3.org/TR/xslt

Xpath – http://www.w3.org/TR/xpath

XSLF – http://www.w3.org/TR/xsl

XSLT (XSLT Trasformations), XML belgelerinin bir dönüşümü için kullanılır. XSLT bir yapıdaki XML belgesini, XSL biçim dosyasındaki tanımlamalara göre başka bir yapıya dönüştür. XSLT, XML belgesini HTML diline, diğer bir XML belgesine veya XSLF formatlama nesnelerine dönüştürebilir. Bugün XSLT en yaygın olarak XML belgelerinin HTML belgelerine dönüşümünde kullanılır. Dönüşüm sonuçunda elde edilen HTML belgesi tarayıcılar ile görsel olarak gösterilebilir.

XSLT, bir XML belgesinin dönüşümü için ilk önce belgeyi parse ederek bir ağaç yapısı oluşturur. Oluşan ağaç yapısın kök elemanından başlıyarak ağaçı tarar ve XSL biçimleme dosyasında tanımlanan kalıplara göre dönüşüm işlemini gerçekleştirir. XSLT ağaç yapısını tararken Xpath ifadelerini kullarak ağaçın değişik kesimlerine erişir.

Xpath spesifikasyonu oluşan bir XML ağaçının içindeki düğümleri adreslemek için kullanılır ve ağaçın belirli kısımlarını adresleyerek ağaç içinde dolaşmamızı sağlar.

XSLT bir XML belgesini başka bir XML belgesinede dönüştürebilir. Örneğin cep telefonlarındaki WAP uygulamalarında kullanılan WML (Wireless Markup Language) cep telefonlarındaki kısıtlamalar düşünürüklerek XML dilinde tanımlanmış bir işaretleme dilidir. XML belgeleri XSLT kullanarak WML’e dönüştürülerek cep telefonlarında görüntülenmesi sağlanabilir.

XSLF (XSL Formating), XSL teknolojisinin biçimleme kısmını içerir. XSLT , XML belgelerini XSLF biçimlendirme nesnelerine dönüştür. Biçimleme nesneleri belgelerin görsel olarak sunumu sağlar. Biçimleme nesnelerinin görüntülenmesi için tarayıcıların XSLF biçimleme yapısını desteklemesi gerekir. XSLF spesifikasyonu henüz geliştirme aşamasında olduğundan bu yapıyı destekleyen bir tarayıcı yoktur.

**XML’den HTML’e dönüşüm**

Şu anda XML belgelerinin görüntülenmesi için en yaygın yöntem XML belgesinin HTML biçimleme diline dönüştütlmesidir. Dönüştürme işlemi XSL biçimleme sayfaları (style sheets) içinde tanımlamış dönüşüm kuralları ile gerçekleştirilir. Bu kurallar şablon (template) olarak adlandırılır. Şablonlar XML belgesi içindeki eleman ve özellikleri kalıplar (pattern) ile karşılaştırarak eşleştirilir. Kalıplar Xpath spesifikasyonuna göre XML belgesinin istediğimiz kısımlarına erişmemizi sağlar. Örneğin “/” kök kalıbı bütün belgeyi adresler. “isim” kalıbı XML belgesi içinde geçen bütün isim elemanlarını ifade eder. “*adressbook/contact*” kalıbı *adressbook* elemanı altındaki *contact *elemanını adresler. Eşleştirilen kalıplara şablonlar uygulanarak dönüştürme işlemi gerçekleşir. Örneğin aşağıdaki XML elemanına bakalım:

İsim elemanını aşağıdaki HTML ifadesine dönüştürmek isteyelim.

Bu dönüştürme işlemi için aşağıdaki XSLT şablonunu kullabiliriz.

Bu ifade bir XML belgesi içinde geçen isim elemanlarını bularak elemanın içindeki değeri <xsl:value-of/> ifadesi ile alır ve H2 etiketi içerisinde yazar.

Aşağıda sık olarak kullanılan XSLT diğer bazı şablon yapıları verilmiştir:

Xsl:if

Xsl:apply-templates

Xsl:for-each

Xsl:if ifadesi şartlı eşleme işlemleri gerçekleştirilir. Örneğin aşağıdali ifade fiyat özelliği (attribute) 1000 olan ürünler için *urun* sablonunu uygulayacaktır.

Xsl:apply-templates XSL biçim sayfası içinde tanımlanmış şablonları uygulamamızı sağlar.

Xsl:for-each ifadesi bir XML belgesi içindeki elemanlara bir döngü içerisinde erişmemizi sağlar. Örneğin aşağıdaki ifade *vehicles* elemanı içindeki *vehicle* elemanlarına *price *elemanına göre sıralayarak erişmemizi sağlar.

Şekil 4’te verilen *adressbook.xml* belgesini Internet Explorer 5.0’da Şekil 8’deki gibi görüntülenmesini sağlayan bir XSL biçimleme sayfası Şekil 9’de gösterilmiştir.

Adressbook.xsl biçimleme sayfasına göre *adressbook.xml *belgesini biçimlendirmek için aşağıdaki işlem komutunun XML belgesinin başlagıçına konulması gerekir. Internet Explorer 5.0 bu komutu kullanarak belge ile biçimleme sayfasını eşleştirir ve XML belgesinin HTML formatına dönüşümünü sağlar.

XML belgelerinin XSL biçimleme sayfaları ile HTML’e dönüşüm işlemi isternirse *Javascript* kullanılarakta yapılabilir. Dönüştürme işlemi XMLDOM COM nesnesi ile yapılır. Şekil 10’da *Addressbook.xml* belgesini *Addressbook.xsl *biçimleme sayfasını kullarak HTML’e dönşümünü sağlayan *Javascript* kodu verilmiştir.

XML belgelerinin HTML’e dönüştürme işlemi isternirse Web sunucusu makinasınada yapılabilir. Bu yapıda sunucu tarafında XML belgeleri HTML’e dönüştürülerek tarayıcılara gönrilir. Böylece XSL’i desteklemeyen tarayıcılardada XML belgelerinin görüntülenmesi sağlanır. Şekil 11’da *Addressbook.xml* belgesini *Addressbook.xsl *biçimleme sayfasını kullarak HTML’e Web sunucusunda dönüşümünü sağlayan *ASP* kodu verilmiştir.

**X. XML BELGELERİNİN İŞLENMESİ**

XML belgelerinin uygulama yazılımları işlenmesi için bir çok yazılım paketi geliştirilmiştir. Bu yazılımlar XML processor veya XML parser olarak adlandırılmaktadır. Değişik firmalarca geliştirilen XML parser yazılımlarından bazıları şunlardır:

Sun X package

IBM XML4J package

Oracle XML package

Microsoft MSXML parser

Open/XML parser

Lark/Larval XML parser

XML parser’ları veya işlemcileri üç değişik model üzerine inşa edilmiştir. Bunlar şunlardır:

Bildiri-tabanlı İşlem modeli (Declaretive processing model)

Olay-tabanlı İşlem Modeli (Event-Based Processing model)

Ağaç-tabanlı İşlem Modeli (Tree-based processing model

Bildiri-tabanlı işlem modelinde hangi işlemlerin gerçekleştirileçeğini belirtiriz. İşlemin nasıl gerçekleştileceğini sistem belirler. Örneğin ilişkisel veritabanlarında kullanılan SQL sorgulamama dili bildiri-tabanlı işlem modeline dayanan bir dildir. Bir SQL sorgu ifadesi hangi sonuçların elde edileceğini tanımlanır. İşlemin nasıl gerçekleşeceğini belirtilmez. XML için geliştirilen XQL gibi sorgulama dilleri ve XSLT bildiri-tabanlı işlem modeline dayanır. Bir önceki bölümde gördümüz XSLT dönüşüm örneklerinde dönüşüm işlemi XSL biçimleme dosyasında tanımlanmış olan kurallara gerçekleştirilir. Bu kuralların nasıl geçekleşeğini XML işlemcisi belirler. XSLT bildiri-tabanlı işlem modelinde oluşturulmuş bir yapıdır.

Olay-tabanlı işlem modelinde XML parser’ı XML belgesini okur iken bulmuş olduğu nesneleri uygulama programına olay (event) olarak bildirir. Örneğin bir başlangıç etiketi, karaketer veri veya bitiş etiketi okuduğunda bunu bir olay olarak uygulama programına iletir. Örneğin aşağıdaki XML belgesinin okunduğunu varsayalım:

XML parser’ı okuma işlemi esnasında aşağıdaki olayları türetir.

Uygulama programı XML parser’nın bildirdiği olay tiplerine göre XML belgesini işler ve uygulama amaçına göre bir çıktı üretir. Bu amaçla geliştirilmiş olan yaygın yazılım standardı SAX (Simple API for XML) arayüzüdür. SAX arayüzü basit uygulamalar için geliştirilmiştir. SAX arayüzünü bir çok XML parser paketi desteklemektedir.

Ağaç-tabanlı işlem modelinde XML parser ilk önce XML belgesini okuyarak belge yapısına göre sistem belleğinde bir ağaç oluşturur. Uygulama progamı bu ağaç yapısı içinde dolaşarak gerekli işlemleri yapar. Ağaç-tabanlı işlem modeli için kullanılan model

DOM (Document Object Model) dir. DOM , XML ve HTML belgerinin işlemesi için W3C konsorsiyumu tarafından geliştirilmiştir. Hiyerarşik bir yapıda olan XML belgeleri DOM modelinde bir ağaç yapısında temsil edilir. Örneğin aşağıda bir yazarlar XML belgesi verilmiştir:

Bu belge aşağıdaki ağaç yapısında temsil edilir.

**DOM (Document Object Model) API**

Ağaç-tabanlı işlem modeli için gelişirilmiş olan arayüz DOM (Document Object Model) API (Application Programming Interface) olarak adladırılır. DOM API dil ve platformdan bağımsız W3C’nin önerdiği bir arayüz spesifikasyonudur. Geliştirilen XML parser’larının büyük çoğunluğu bu arayüz spesifikasyonuna göre inşa edilmiştir. Bu kısımda Microsoft MSXML parser kullarak bazı örnekler vereceğiz. MSXML parser bir COM nesnesi olarak yazıldığından hem istemci tarayıcı tarafında hemde sunucu makinalarda çalışabilmektedir.

Ağaç yapısındaki XML belgelerini işlemek için DOM API bir çok nesne, yöntem ve özellik içerir. Aşağıda DOM’da kullanılan önemli nesneler listelenmiştir.

| Nesne | Tanım |
| --- | --- |
| Document Element Attribute veya Attr Node NodeList Text Comment ProcessingInstruction | XML belgesinin kök nesnesi XML Elemanı XML özelliği XML ağaçındaki bir düğüm Düğümler Kümesi Bir eleman veya özellik içindeki metin XML açıklaması XML işlem komutu |

MSXML parser’nın *Document* nesnesinin önemli olan özellik ve method’ları aşağıda verilmiştir.

| Özellik/Method | Tanım |
| --- | --- |
| Doctype DocumentElement ChildNodes FirstChild LastChild Text Async ValidateOnParse Load() LoadXML() GetElementsByTagName() | Document DTD Kök eleman Alt düğüm listesi İlk düğüm Son Düğüm Belgede geçen tüm metinler False ise belge tamamen yüklediğin de cağıran method’a kontrolu devr eder. True ise yükleme esnasında devr eder. Beglenin DTD göre doğrulanması Bir XML belgesinin URL’le belirtiği dosyadan yükler XML belgesini direct metinden yükler Belirli bir tipteki elemanlar kümesini getirir |

Aşağıda MSXML parser’nın *Node* nesnesinin önemli olan özellik ve methodları verilmiştir.

| Özellik/Method | Tanım |
| --- | --- |
| ChildNodes FirstChild LastChild ParentNode previousSibling nextSibling NodeName NodeValue TransformNode() | Alt düğüm listesi İlk düğüm Son düğüm Üst seviye düğüm Aynı seviye önceki düğüm Aynı seviye sonraki düğüm Düğüm ismi Düğüm değeri Belirtilen XSL dosyasına göre dönüşüm yapar |

Aşağıda MSXML parser’nın *NodeList* nesnesinin önemli olan methodları verilmiştir.

| Method | Tanım |
| --- | --- |
| item() nextNode() reset() | Düğüm listesinden istenilen düğümü getirir. Düğüm listesinden istenilen bir sonraki düğümü getirir. Liste imini başa döndürür. |

Şekil 12’de bu kısımdaki MSXML parser örneklerinde kullanağımız *movies.xml* belgesi verilmiştir. *Movies.xml* dosyası bir film hakındaki film tipini, adını, yazarlarını, aktör gibi bilgileri içerir. Şekil 13 ve Şekil 15’te Internet Explorer 5.0 ile çalışan MSXML parser örneklerinin kodu listelenmiştir. Bu örneklerde Javascript kullanılmıştır.

Şekil 13’teki XML parser uygulaması Şekil 14’te görülen film adı ve açıklamalarını listeler. Bu uygulamada *LoadDoc()* fonksiyonu XML belgesini yükleyerek belgeyi ağaç yapısında bellekte oluşturur. Bu örnekteki aşağıdaki satır bir COM nesnesi olan MSXML parser’nı çağırır.

Aşağıdaki satır Movies.xml dosyasını yükler ve XML ağaçını oluşturur.

Aşağıdaki satır belgenin kök elemanına erişir.

Aşağıdaki ifade kök elemanın altında bulunan elemanların adeti kadar bir döngü oluşturur. Bu döngü içinde alt elemanlara erişiriz.

Aşağıdaki kod kök elemanın (*movies*) altındaki *movie* elemanının ilk elemanının (*title*) içeriğini getirir. *ChildNodes.Item(i)* alt düğümlerdeki her hangi bir eleman indeks’le ulaşmamızı sağlar.

Aşağıdaki kod kök elemanın (*movies*) altındaki *movie* elemanının son elemanının (*comments*) içeriğini getirir.

Şekil 15’te görülen XML parser uygulaması *movies.xml* dosyasında bulunan filimlerdeki aktorleri listeler. Programın üretiği çıktı Şekil 16’da listelenmiştir. Bu programdaki aşağıda verilen kod belge içinde geçen bütün *actor* elemanların bir listesini oluşturur. Oluşan aktörler listesindeki elemanlar bir döngü içerisinde taranarak aktör isimleri *actors(i).text *ifadesi ile listelenir.

**XI. SONUÇ**

Önümündeki aylar ve yıllar XML ve XML’in bir çok alandaki uygulamaları hakkında yapılan daha çok araştırma, geliştirme, yazılım ve yayın çalışmalarına sahne olacak. Şu anda olduğu gibi XML hakında daha çok işteceğiz. Bir çok araştırmacı ve yazılım geliştiricisi XML’in yazılım endüstirisinde radikal değişiklilere sebeb olacağına inanmakta ve XML’i elektronik veri değişiminin yeni ASCII standardı olarak kabül etmektedir. Microsoft, IBM, Sun ve Oracle gibi birçok teknoloji lideri firma XML ve XML uygulamala standardlarını desteklemekte ve XML tabanlı yeni ürünlerini bilgi teknolojisi uygulamalarının kullanımına sunmaktadır.

Bu yazıdada gördümüz gibi XML dili, XML söz dizimi kuralları, XML DTD, XML Schema, XML Namespaces, Xpath, Xpointer, XSL, XSLT, XSLF, SAX ve DOM gibi bir çok belirtim ve teknolojinin birleşiminden oluşmaktadır. Bu yazıda yalnızca temel XML teknolojilerini tanıtmaya çalıştık.

Bunların yanında XML’in veri tabanı sistemlerinde kullanımı; bir çok alandaki bilgi paylaşımını kolaylaştıracak XML sözlükleri (vocabularies); bu sözlüklerin standard bir şekilde tasarlanması, kayıt ve saklanması için Microsoft firmasının desteklediği BizTalk Framework’u; XML-RPC ve SOAP gibi XML mesaj protokolleri; elektronik ticaret alanında kullanılacak olan birlemiş milletler destekli ebXML çalışmaları; elektronik veri değişimi standardı XML/EDI gibi daha bir çok XML ile ilgili konu vardır. Bu konularda bilgi almak isteyenler aşağıda verdiğimiz kaynaklardan ve internetteki diğer kaynaklardan yaralanabilirler. Bu kaynaklardan özellikle http://www.oasis-open.org/cover/ sitesindeki *XML cover pages *XML konusunda geniş bir yayın listesi içermektedir.

**KAYNAKLAR:**

A Brief History of the Development of SGML, http://www.sgmlsource.com/history/sgmlhist.htm

Mark Johnson, XML for the absolute beginner, http://www.javaworld.com/javaworld/jw-04-1999/jw-04-xml.html

Ralf I. Pfeiffer, Tutorial 1: Overview of XML, http://www4.ibm.com/software/developer/education/tutorial-prog/overview.html

Micheal Morrison et al.,*XML Unleashed*, Sams Publishing, 1999.

Richard Anderson et al., *Professional XML,* Wrox Press Ltd., 2000.

Portable Data/Portable Code: XML & Java Technologies, http://java.sun.com/xml/ncfocus.html

Alex Homer et al, *Active Server Pages 3.0*, Wrox Press Ltd., 2000.

Danny Ayers et al, *Professinal Java Server Programming*, Wrox Press Ltd., 2000.

http://www.ibm.com/developer/xml/

http://msdn.microsoft.com/xml/default.asp

http://www.oracle.com/xml/

http://www.oasis-open.org/cover/

http://www.xml.org/

http://www.xml101.com

http://www.sun.com/software/xml/

http://ebxml.org

http://www.w3.org/XML/

http://www.xml.com/

http://www.xml.org/

http://www.xmlinfo.com/

http://www.geocities.com/SiliconValley/Peaks/5957/xml.html

PAGE

PAGE 10

## **Biçimle******

## ** TARAYICI******

Şekil 1 – Tarayıcıda Biçimlendirilmiş HTML Belgesi

Şekil 2 – Adres XML Belgesi \[4\]

## **HTML******

**Sn. Selim Akyokuş**

Barboros Cad. No: 11

Yildiz 80750 İSTANBUL

**<P> **

**<b> Sn. Selim Akyokuş </b>**

**<br>**

**Barboros Cad. No: 11 **

**<br>**

**Yıldız 80750, İSTANBUL**

**</p>**

**<?xml version="1.0"?>**

**<!DOCTYPE addressbook SYSTEM "AddressBook.dtd" \[**

**<!ENTITY amp "&#38;#38;">**

**<!ENTITY apos "&#39;">**

**\]>**

**<addressbook>**

** <!-- This is my good friend Frank. -->**

** <contact>**

** <name>Frank Rizzo</name>**

** <address>1212 W 304th Street</address>**

** <city>New York</city>**

** <state>New York</state>**

** <zip>10011</zip>**

** <phone>**

** <voice>212-555-1212</voice>**

** <fax>212-555-1213</fax>**

** </phone>**

** <email>frizzo@fruity.com</email>**

** <web>http://www.fruity.com/rizzo</web>**

** <company>Frank&apos;s Ratchet Service</company>**

** </contact>**

** <!-- This is my old college roommate Sol. -->**

** <contact>**

** <name>Sol Rosenberg</name>**

** <address>1162 E 412th Street</address>**

** <city>New York</city>**

** <state>New York</state>**

** <zip>10011</zip>**

** <phone>**

** <voice>212-555-1818</voice>**

** <fax>212-555-1819</fax>**

** </phone>**

** <email>srosenberg@fruity.com</email>**

** <web>http://www.fruity.com/rosenberg</web>**

** <company>Rosenberg&apos;s Shoes &amp; Glasses</company>**

** </contact>**

**</addressbook>**

**<!ELEMENT addressbook (contact)+>**

**<!ELEMENT contact (name, address+, city, state, zip, phone, email, web, company)>**

**<!ELEMENT name (#PCDATA)>**

**<!ELEMENT address (#PCDATA)>**

**<!ELEMENT city (#PCDATA)>**

**<!ELEMENT state (#PCDATA)>**

**<!ELEMENT zip (#PCDATA)>**

**<!ELEMENT phone (voice, fax?)>**

**<!ELEMENT voice (#PCDATA)>**

**<!ELEMENT fax (#PCDATA)>**

**<!ELEMENT email (#PCDATA)>**

**<!ELEMENT web (#PCDATA)>**

**<!ELEMENT company (#PCDATA)>**

Şekil 3 – Adres XML DTD Dosyası \[4\]

<?xml version="1.0" ?>

<!DOCTYPE e\_posta SYSTEM "e-posta.dtd">

<e\_posta>

<kime>Herkese</kime>

<kimden> Selim Akyokuş</kimden>

<tarih> 7 Eylül 2000</tarih>

<konu>XML ve XML Uygulamaları</konu>

<mesaj> XML HTML gibi etiket tabanlı bir dildir</mesaj>

</e\_posta>

<kime>

<kimden>

<Kitap>

<kitap>

</kime>

</kimden>

</Kitap>

</kitap>

</kitap> XML Unleashed </kitap>

Şekil 4 – Elektronik posta XML belgesi

</br></br>

<br/>

HTML allows <B>

<I> improper nesting <B>

<I>

XML requires <B>

<I> improper nesting <I>

<B>

<kitap kitap\_no=”123456”>

<?hedef ...komutlar ... ?>

<!\[CDATA\[ ... \]\]>

<!\[CDATA\[

\*P = &A

C = (i <= 5) ;

\]\]>

**<!DOCTYPE kök\_eleman\_ismi SYSTEM "sistem\_tanımlayıcısı"> **

**<!DOCTYPE kök\_eleman\_ismi PUBLIC **

** "public\_tanımlayıcısı""sistem\_tanımlayıcısı"> **

**<?xml version="1.0"?>**

**<!DOCTYPE addressbook SYSTEM "http://xyz.com/AddressBook.dtd" \[**

**<!ENTITY amp "&#38;#38;">**

**<!ENTITY apos "&#39;">**

**\]>**

**Kişi ::= (isim telefon-no\*) **

**<!ELEMENT kişi (isim telefon-no\*)> **

**<!ELEMENT Elemanİsmi EMPTY> **

**<!ELEMENT img EMPTY)> **

**<img/>**

**<img></img>**

**<img src=”resim.gif”/>**

**<img src=”resim.gif”/><img>**

**<!ELEMENT Elemanİsmi İçerik-Modeli> **

**<!ELEMENT e-posta kime kimden tarih? konu? mesaj> **

**<!ELEMENT özgeçmiş (giriş, (eğitim | deneyim+)+, hobiler?, referanslar\*> **

**<!ELEMENT konu (#PCDATA)>**

**<!ELEMENT not (#PCDATA | tarih | konu)\*>**

**<not>**

** <tarih> 1 Ekim 2000 </tarih>**

** Okul kayıtları başlayacak.**

**</not>**

**<!ELEMENT Elemanİsmi ANY> **

**<!ATTLIST Elemanİsmi Özellikİsmi ÖzellikTipi *****Default*****> **

**<!ATTLIST Kitap BasımTarihi CDATA #REQUIRED> **

**<Kitap BasımTarihi=”1.1.2000”> ...... </Kitap>**

**<!ATTLIST Kitap Basım-Sayısı CDATA #IMPLIED> **

**<!ATTLIST deniz renk #FIXED “mavi”> **

**<!ATTLIST elma renk “kırmızı”> **

**<!ATTLIST kalem renk (mavi | kırmızı | yeşil | beyaz) “kırmızı”> **

**<!ATTLIST resim format NOTATION (gif | jpeg) #REQUIRED> **

**<!ATTLIST personel personel-no ID #REQUIRED> **

**<!ELEMENT mühendis EMPTY>**

**<!ATTLIST mühendis per-no IDREF #REQUIRED> **

**<personel personel-no=”12345”>**

** <isim> Ali Veli </isim>**

** ..... **

**</personel>**

** .....**

**<mühendis per-no=”12345”/> **

**<!ELEMENT proje-gurubu EMPTY>**

**<!ATTLIST proje-gurubu per-no IDREFS #REQUIRED> **

**<proje-gurubu per-no=”12345 67891 23456”**

**<!ATTLIST personel eğitim NMTOKENS #IMPLIED> **

**<personel eğitim=”ilkokul ortaokul lise ”**

**<!ENTITY şirket “XYZ Bilgisayar Limited Şirketi A.Ş.”>******

**<reklam> Firmamız &şirket; internet danışmanlığı hizmeti sunar. </reklam>******

**<!ENTITY aciklama SYSTEM “http://www.xyz.com/readme.txt”>******

**<!ENTITY % Varlıkİsmi VarlıkTanımı>******

**<!ENTITY % boyut “uzunluk genişlik yükseklik”>******

**<!ELEMENT tavan (%boyut;)>**

**<!ELEMENT çatı (%boyut;)>******

**<!ELEMENT duvar (%boyut;)>******

**<!ENTITY copyright **“&#169”** >******

**<!NOTATION jpg SYSTEM “jpgviewer.exe”>******

**<!NOTATION gif SYSTEM “gifviewer.exe”>******

**W3C standardlaştırma çalışmaları aşamalarında farklı seviyelerde standard spesifikasyonları yayınlamaktadır. Bunlar şunlardır:**

***Note***** **: **Bir fikir veya açıklamayı içeren en aşağı seviyedeki spesifikasyon**

***Working Draft***** : Standardlaştırma çalışmalarının devam ettiğini sürede yayınlanan spesifikasyonlar.**

***Recommendation***** : Working Draft aşaması sonucu elde edilen en son seviye standard specifikasyonu.**

** ****ADRESBOOK DTD**

**<!ELEMENT addressbook (contact)+>**

**<!ELEMENT contact (name, address+, city, state, zip, phone, email, web, company)>**

**<!ELEMENT name (#PCDATA)>**

**<!ELEMENT address (#PCDATA)>**

**<!ELEMENT city (#PCDATA)>**

**<!ELEMENT state (#PCDATA)>**

**<!ELEMENT zip (#PCDATA)>**

**<!ELEMENT phone (voice, fax?)>**

**<!ELEMENT voice (#PCDATA)>**

**<!ELEMENT fax (#PCDATA)>**

**<!ELEMENT email (#PCDATA)>**

**<!ELEMENT web (#PCDATA)>**

**<!ELEMENT company (#PCDATA)>**

** ****ADRESBOOK XML ŞEMASI**

**<?xml version="1.0"?>**

**<Schema name="AddressBookSchema"**

** xmlns="urn:schemas-microsoft-com:xml-data"**

** xmlns:dt="urn:schemas-microsoft-com:datatypes">**

** <ElementType name="name" content="textOnly"/>**

** <ElementType name="address" content="textOnly"/>**

** <ElementType name="city" content="textOnly"/>**

** <ElementType name="state" content="textOnly"/>**

** <ElementType name="zip" content="textOnly" dt:type="int"/>**

** <ElementType name="voice" content="textOnly" dt:type="int"/>**

** <ElementType name="fax" content="textOnly" dt:type="int"/>**

** <ElementType name="phone" content="eltOnly">**

** <element type="voice" minOccurs="1" maxOccurs="1"/>**

** <element type="fax" minOccurs="0" maxOccurs="1"/>**

** </ElementType>**

** <ElementType name="email" content="textOnly"/>**

** <ElementType name="web" content="textOnly"/>**

** <ElementType name="company" content="textOnly"/>**

** <ElementType name="contact" content="eltOnly">**

** <element type="name" minOccurs="1" maxOccurs="1"/>**

** <element type="address" minOccurs="1" maxOccurs="2"/>**

** <element type="city" minOccurs="1" maxOccurs="1"/>**

** <element type="state" minOccurs="1" maxOccurs="1"/>**

** <element type="zip" minOccurs="1" maxOccurs="1"/>**

** <element type="phone" minOccurs="1" maxOccurs="1"/>**

** <element type="email" minOccurs="0" maxOccurs="1"/>**

** <element type="web" minOccurs="0" maxOccurs="1"/>**

** <element type="company" minOccurs="0" maxOccurs="1"/>**

** </ElementType>**

** <ElementType name="addressbook" content="eltOnly">**

** <element type="contact" minOccurs="1"/>**

** </ElementType>**

**</Schema>******

<product>

<id>12345678-Q</id>

<description>Thinkpad 2000D</description>

<price>$999.99</price>

</product>

Şekil 4 – XML belgeleri farklı ortamlarda erişilebilir \[3\].

p { display : block;

color: blue;

font-family : Arial;

font-size: 14pt;

}

**Seçiçi {özellik1: değer1;**

** özellik2: değer2;**

** ......**

**}******

isim { display : block;

font-family : Times, serif;

font-size: 16pt;

font-weight : bold;

}

<p> CSS basit bir biçimleler için kullanılır </p>

contact {

display: block;

width: 350px;

padding: 10px;

margin-bottom: 10px;

border: 4px double black;

background-color: silver;

color: blue;

text-align: center;

}

name {

display: block;

font-family: Times, serif;

font-size: 16pt;

font-weight: bold;

}

address {

display: block;

font-family: Times, serif;

font-size: 14pt;

}

city, state, zip {

display: inline;

font-family: Times, serif;

font-size: 14pt;

}

phone, email, web, company {

display: none;

}

<?xml-stylesheet type=”text/css” href=”Adressbook.css”>

Şekil 5 – Adressbook DTD ve XML şeması \[4\]

Şekil 6 – Adresbook.css biçimleme dosyası \[4\]

Şekil 7 – Adressbook XML belgesinin Adressbok.css dosyasındaki biçimleme kuralları ile oluşmuş görüntüsü

<isim> Selim Akyokuş </isim>

<H2> Selim Akyokuş </H2>

<xsl:template match=”isim”>

<H2> <xsl:value-of/> </H2>

</xsl:template>

<xsl:template match=”@fiyat=1000”>

<xsl:apply-templates select=”urun” />

</xsl:template>

<xsl:for-each order-by="+ price" select="vehicles/vehicle">

<tr>

<td><xsl:value-of select="@year"/></td>

<td><xsl:value-of select="@make"/></td>

<td><xsl:value-of select="@model"/></td>

<td><xsl:value-of select="mileage"/></td>

<td><xsl:value-of select="color"/></td>

<td><xsl:value-of select="price"/></td>

</tr>

</xsl:for-each>

**ADRESBOOK.XSL BİÇİMLEME SAYFASI**

**<?xml version="1.0"?>**

**<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl">**

** <xsl:template match="/">**

** <html><head><title>Address Book XML Example</title></head>**

** <body bgcolor="#FFFFFF">**

** <xsl:for-each select="addressbook/contact">**

** <xsl:apply-templates select="name"/>**

** <xsl:apply-templates select="address"/>**

** <xsl:apply-templates select="city"/>**

** <xsl:apply-templates select="state"/>**

** <xsl:apply-templates select="zip"/>**

** </xsl:for-each>**

** </body>**

** </html>**

** </xsl:template>**

** <xsl:template match="name">**

** <h2><xsl:value-of/></h2>**

** </xsl:template>**

** <xsl:template match="address">**

** <xsl:value-of/><br/>**

** </xsl:template>**

** <xsl:template match="city">**

** <xsl:value-of/>, **

** </xsl:template>**

** <xsl:template match="state">**

** <xsl:value-of/>**

** </xsl:template>**

** <xsl:template match="zip">**

** <xsl:value-of/><br/>**

** </xsl:template>**

**</xsl:stylesheet>******

<?xml-stylesheet href="AddressBook.xsl" type="text/xsl"?>

Şekil 9 – Adressbook.xsl biçimleme sayfası (style sheet) \[4\]

Şekil 8 – Adressbook.xsl biçimleme sayfasıdaki (style sheet) şablonlara göre Internet Explorer 5.0’da oluşan görüntü

**<html>**

**<body>**

**<script language="javascript">**

**// Load XML **

**var xml = new ActiveXObject("Microsoft.XMLDOM")**

**xml.async = false**

**xml.load("Addressbook.xml")**

**// Load the XSL**

**var xsl = new ActiveXObject("Microsoft.XMLDOM")**

**xsl.async = false**

**xsl.load("Addressbook.xsl")**

**// Transform**

**document.write(xml.transformNode(xsl))**

**</script>**

**</body>**

**</html>******

Şekil 10 – *Addressbook.xml* belgesini *Addressbook.xsl *biçimleme sayfasını kullarak HTML’e dönşümünü sağlayan *Javascript* kodu

<example>

<line>&quo;Hello,

world!&quo;</line>

</example>

Şekil 11 – *Addressbook.xml* belgesini *Addressbook.xsl *biçimleme sayfasını kullarak HTML’e Web sunucusunda dönşümünü sağlayan *ASP* kodu

**<%**

**'Load the XML**

**set xml = Server.CreateObject("Microsoft.XMLDOM")**

**xml.async = false**

**xml.load(Server.MapPath("Addressbook.xml"))**

**'Load the XSL**

**set xsl = Server.CreateObject("Microsoft.XMLDOM")**

**xsl.async = false**

**xsl.load(Server.MapPath("Addressbook.xsl "))**

**Response.Write(xml.transformNode(xsl))**

**%>**

start document

start element: example

start element: line

text: “Hello, World!”

end element: line

end element: example

end document

<?xml version=”1.0”>

<!—Parse ağaçı örneği -->

<yazarlar>

<yazar>

<ad> Ali </ad>

<soyad> Demir </ad>

</yazar>

</ornek>

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">

<html>

<head>

<title>List Movies 2 Example HTML Document</title>

<script language="JavaScript">

var xmldoc;

function LoadDoc() {

xmldoc = new ActiveXObject("microsoft.xmldom");

xmldoc.load("Movies.xml");

}

function ListMovies() {

LoadDoc();

root = xmldoc.documentElement;

for (i = 0; i < root.childNodes.length; i++) {

DOCCONTENT.innerHTML += "<b>" +

root.childNodes.item(i).firstChild.text + "</b><br>";

DOCCONTENT.innerHTML += root.childNodes.item(i).lastChild.text +

"<br><br>";

}

}

</script>

</head>

<body>

Click the button to list the movies in the Movies XML document.

<br>

<input type="button" value="List Movies" onclick="ListMovies()">

<div id="DOCCONTENT"></div>

</body>

</html>

<?xml version="1.0" standalone="no"?>

<!DOCTYPE movies SYSTEM "Movies.dtd">

<movies>

<movie type="comedy" rating="PG-13" review="5" year="1987">

<title>Raising Arizona</title>

<writer>Ethan Coen</writer>

<writer>Joel Coen</writer>

<producer>Ethan Coen</producer>

<director>Joel Coen</director>

<actor>Nicolas Cage</actor>

<actor>Holly Hunter</actor>

<actor>John Goodman</actor>

<comments>A classic one-of-a-kind screwball love story.</comments>

</movie>

<movie type="comedy" rating="R" review="5" year="1988">

<title>Midnight Run</title>

<writer>George Gallo</writer>

<producer>Martin Brest</producer>

<director>Martin Brest</director>

<actor>Robert De Niro</actor>

<actor>Charles Grodin</actor>

<comments>The quintessential road comedy.</comments>

</movie>

<movie type="mystery" rating="R" review="5" year="1995">

<title>The Usual Suspects</title>

<writer>Christopher McQuarrie</writer>

<producer>Bryan Singer</producer>

<producer>Michael McDonnell</producer>

<director>Bryan Singer</director>

<actor>Stephen Baldwin</actor>

<actor>Gabriel Byrne</actor>

<actor>Benicio Del Toro</actor>

<actor>Chazz Palminteri</actor>

<actor>Kevin Pollak</actor>

<actor>Kevin Spacey</actor>

<comments>A crime mystery with incredibly intricate plot twists.</comments>

</movie>

<movie type="sci-fi" rating="PG-13" review="4" year="1989">

<title>The Abyss</title>

<writer>James Cameron</writer>

<producer>Gale Anne Hurd</producer>

<director>James Cameron</director>

<actor>Ed Harris</actor>

<actor>Mary Elizabeth Mastrantonio</actor>

<comments>A very engaging underwater odyssey.</comments>

</movie>

</movies>

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">

<html>

<head>

<title>List Actors Example HTML Document</title>

<script language="JavaScript">

var xmldoc;

function LoadDoc() {

xmldoc = new ActiveXObject("microsoft.xmldom");

xmldoc.load("Movies.xml");

}

function ListActors() {

LoadDoc();

actors = xmldoc.getElementsByTagName("actor");

for (i = 0; i < actors.length; i++) {

DOCCONTENT.innerHTML += actors(i).text + "<br>";

}

}

</script>

</head>

<body>

Click the button to list the actors in the Movies XML document.

<br>

<input type="button" value="List Actors" onclick="ListActors()">

<div id="DOCCONTENT"></div>

</body>

</html>

Şekil 13 – *Movies.xml* belgesindeki film ve film açılamalarını listeleyen Javascript kodu \[4\]

Şekil 12 – *Movies.xml* XML belgesi \[4\]

Şekil 15 – *Movies.xml* belgesindeki aktör isimlerini listeleyen Javascript kodu \[4\]

Şekil 14 – Şekil 13’teki kodun üretiği Internet Explorer 5.0 görüntüsü

xmldoc = new ActiveXObject("microsoft.xmldom");

xmldoc.load("Movies.xml");

root = xmldoc.documentElement;

for (i = 0; i < root.childNodes.length; i++)

root.childNodes.item(i).firstChild.text

root.childNodes.item(i).lastChild.text

Şekil 16 – Şekil 15’teki kodun üretiği Internet Explorer 5.0 görüntüsü

actors = xmldoc.getElementsByTagName("actor");

---
*Kaynak: `XML ve XML UYGULAMALARI/XML ve XML UYGULAMALARI.doc` — adminIA — 2004*
