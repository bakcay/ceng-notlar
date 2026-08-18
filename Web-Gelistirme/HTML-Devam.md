# HTML - Devam

Sunuş.. 4

Dil Deyince:10

Bölüm I: Web’e Giriş. 11

Temel Bilgiler..... 11

HTML’e Genel Bakış12

HTTP ve TCP/IP14

Web Server17

Web Tarayıcıları.. 23

Microsoft Internet Explorer..... 24

Netscape Navigator.... 25

Diğerleri.... 25

Yaygınlık Oranları..... 27

Yardımcı Programlar ve Ek Birimler..... 27

Java, ActiveX..... 29

Bölüm II: HTML’in Temel Unsurları...... 30

Etiketler (Tag)..... 30

Düz Yazı Dosyası ve HTML. 31

HTML mi, HTM mi?32

Büyük Harf, Küçük Harf?. 34

HTML Dosyasının Bölümleri.... 35

Açtığınızı Kapatmayı Unutmamak İçin. 35

“Open” mı, “Browse” mı?36

HTML Editörleri. 38

Web Sayfasının Biçimlendirilmesi..... 39

Harf Genişliği. 40

Yerel Biçimlendirme43

Yeni Paragraf ile Yeni Satır’ın farkı.44

Internet’te Font meselesi46

SERIF-SANS SERIF Harfler:46

Metin Düzenleme Etiketleri... 48

Bölüm III: Tablo ve Çerçeveler ve Katmanlar...... 61

Bir Pixel Kaç Santim?61

Tablolar..... 63

Başlık, Satır ve Veri Etiketleri... 64

Açtığınızı Kapatın!66

Tablo Unsurlarının Kontrolü..... 66

İskelet Malzemesi Olarak Tablo69

Renk Şifresini Çözdünüz mü?72

Elinize geçeni sayfanıza koyabilir misiniz?74

Çerçeveler.... 80

Çerçevenin Unsurları: Sütunlar ve Sıralar..... 81

Eşit Sayıda Olmayan Sütun ve Sıralar..... 86

HTML’de Bağlantı’ya Giriş..... 89

Metinlere Bağlantı Kazandırmak89

HTML’de Bağlantı Türleri... 92

Sayfada Diğer Unsurlara Bağlantı Kazandırmak:94

Bağlantılı Çerçeve Uygulaması94

Ters Bölü İşaretine Ne Oldu?100

Bağlantıları Grafiklere Yerleştirmek: Düğmeler. 104

Katmanlar ve CSS Teknikleri: Dinamik HTML’e Giriş106

HTML’de Nesne Kavramı.... 109

Cascading Style Sheets (Yığılmalı Stil Kağıtları)110

Peki bir HTML sayfasına hem LINK, hem de EMBEDED stil sayfası verirsek, ne olur?113

Stil kurallarını Nesnelere Uygulamak... 114

Harf Seçiciler115

Sınıf Seçiciler115

Kimlikli Seçiciler116

Sınıfımsı Seçiciler117

Bağlamsal Seçiciler118

Denetlenebilir Özellikler.. 118

Font Özellikleri:.. 119

Renk ve Zemin Özellikleri:.. 121

Metin Özellikleri:.. 122

Konum (Pozisyon) Özellikleri124

Diğer Özellikler126

Bir Nesne Yapalım.... 127

Sabit Nesneler. 127

“Üst” mü, “Ust” mu?128

Rollover Etkileri. 131

Javascript ve VBScript132

Bölüm IV: HTML’de Form ve CGI.. 136

Formun Bölümleri.... 137

Action ve Method.... 138

Doldurulacak Boşluklar ve İşaretlemeler139

INPUT.. 139

SELECT.. 141

TEXTAREA. 142

Gönder ve Sil düğmeleri... 142

Örnek143

CGI. 149

# Sunuş

Bu kitapçıkta, Internet ve firmaların kendi yerel ağları içinde kuracakları dahilî Internet (intranet) için gerekli dosyaları oluşturma yollarından biri, HTML dilinin temel bilgileri yer alıyor. HTML için “dil” dedik; ama bu biraz açıklamaya muhtaç bir ifade.

Farklı bilgisayarlar ve kelime-işlem programları arasında, yazı dosyalarının biçimlendirilmesinde ortak bir yöntem bulma çabası, 1986’da, Dünya Standartlar Enstitüsü tarafından Standart Genelleştirilmiş İşaretleme Dili (Standart Generalized Markup Language, SGML) adıyla birleştirildi. Burada kullanılan dil, “program yazma dili” teriminde olduğundan pek de farklı değil. Fortran, Basic, Cobol gibi bir program yazma dili, bilgisayara, kendisine verilecek talimatların nasıl bir yöntemle verileceğini ve bu talimatlar üzerine ne yapması gerektiğini belirtir. SGML ile ondan türetilen HTML ve XML “dilleri” kullanılarak oluşturulan belgeler, programlama dillerinden farklı olarak doğrudan bilgisayarın işletim sistemine değilse bile bir yazılıma, örneğin kelime-işlemcisine ya da veri-işlemcisine “aşağıdaki veriyi ekranda şöyle göster, yazıcıdan da şöyle çıkart” anlamına gelen komutları da içerdiğine göre, bir anlamda “dil” sayılabilir.

Ne var ki, SGML ve ondan türetilen HTML ve XML’in bir uygulama programı tarafından anlaşılabilmesi için, bu yöntemle kendisine verilecek bilgileri nasıl işleyeceğine ilişkin bilgilerin önceden, programın içine işlenmiş olması gerekir. Yani, bir programın HTML’i anlayabilmesi için, içinde HTML’i anlama ve yorumlama komutlarının olması gerekir. Bu anlamda, işin program tarafı başka birisi tarafından yapılmış sayılabilir; bizim HTML ile yaptığımız sadece veri oluşturmak şeklinde yorumlanabilir. Bu açıdan SGML ve türevleri dil sayılamazlar.

Gerçek bilgisayar programcıları, HTML gibi, bilgisayara hem bilgileri, hem de bu bilgilerin nasıl işleneceğini gösteren “metinleri” dil saymazlar. İster “dil” sayılsın, ister sayılmasın, HTML, kısaca tanımlarsak, Netscape Navigator, Internet Explorer, Mosaic, Spry gibi, bilgisayar kullanıcısı, bilgisayar ve Internet arasında arabirim görevi yapan programların anladığı bir veri ve komut ulaştırma yöntemidir; diğer bilgisayar programlarından farklı olarak sabit disk veya disket gibi bilgisayar kayıt ortamlarına kaydedilirken, düz yazı olarak kaydedilir; herhangi bir düz yazı programı ile oluşturulabilir, okunabilir ve değiştirilebilir. Diğer bilgisayar programlarından farklı olarak, disk ve disketlere yazılırken Binary-İkili sistemle yazılmaz; içinde 16 Tabanlı-Hexadecimal komutlar yoktur; herşey standart düz yazı olarak yer alır. Buna karşılık herhangi bir düz yazı dosyasından farklı olarak “metnin” içinde “<” ve “>” işaretleri arasında yeralan Ingilizce bazı komut-kelimeleri vardır.

HTML, önceleri Macintosh ardından IBM uyumlu bilgisayarlarının yardım dosyalarının oluşturulmasında kullanılan bir yöntem olarak yaygın bir kullanım alanı buldu. Ancak, HTML kısaltmasının açık şekli olan Hypertext Markup Language’de geçen Hypertext terimi, 1950 yılında Ted Nelson adlı bir bilgisayar uzmanı tarafından içinde “hot,” yani başka bir metinle veya resimle ilintilendirilmiş noktalar bulunan metin anlamına kullanılmıştı. Apple firması, bu yöntemi ekranda gösterilen yardım metinlerinin içinde bir kelimeyi veya simgeyi tıklayarak ilgili başka bir başka metne veya simgeye gitme yöntemi olarak kullandı. Metinler böylece “hyper” hareketli hale geliyordu.

1989 yılında, Avrupa Parçacık Fiziği \[Atom\] Laboratuvarı CERN uzmanlarından Tim Berners-Lee, laboratuvar yönetimini ortak bir yazı biçimlendirme sistemine ikna edebilmek için, “Enformason Yönetimi: Bir Öneri” başlıklı bir rapor hazırladı. Bu raporda, daha sonra bugünkü Internet’in temeli olacak bilgisayar şebekeleri arası ağda bilgi alış verişi için Hypertext’in ortak yöntem olmasını önerdi. Ve bu öneri bugün dördüncü sürümüne ulaşmış olan HTML dilinin temeli oldu.

Bugünkü Internet’i Internet yapan iki unsur var. Birincisi bilgisayararası iletişimi gerçek zamanlı olmaktan çıkartan bağlantı protokolünün (HTTP) geliştirilmesi; diğeri ise HTML dilinin ortak dil olarak benimsenmesini mümkün kılacak basitlikte olmasına karşın, bir metnin biçimlendirilmesi ve resim, ses, video gibi diğer unsurlarla bütünleştirilmesini sağlayabilecek yeterlikte olması. Bunu biraz açalım:

Bugünkü Internet’in temeli olan üniversiteler ve araştırma kurumlarının bilgisayar ağlarını birbirine bağlayan ağlar 1980’lerin başlarında bağlantının gerçek zamanlı olmasını gerektiriyordu. Internet’in adı da ağlar-arası ağ anlamına gelen İngilizce “Inter-networks-network: Inter-net kısaltmasından doğuyor. Bir bilimadamı bir başka bilimadamının bilgisayarının bulunduğu ağa bağlandığı zaman, bu bağlantı, gerekli dosyanın bir bilgisayardan diğerine aktarılması süresince devam etmek zorunda idi. İki bilgisayar aralarında gidip-gelen bilginin hata kontrolünü ancak gerçek-zamanlı bağlantı olursa yapabiliyorlardı. HTTP (Hypertext Transmission Protocol-Hypertext Iletim Kuralları) ise iki bilgisayarın alış-verişin hatasız olduğunu denetlemek için, bilginin tümü alınıp-verilinceye kadar birbirine bağlı kalmaları zorunluğunu ortadan kaldırıyor. Bu zorunluğun ortadan kalkmasının önerimini bir örnekle anlatalım. Otomobille bir yerden diğerine gideceksiniz. Takip edeceğiniz yolda inşaat var, ve yol kapalı. Yolun kapalı kesimini atlamanız için gerekli servis yolunu da yok. Bu durumda yolculuğunuz ilk engelde sona ermiş demektir. Oysa daha dolambaçlı da olsa bir servis yolu olsaydı, yolunuza devam edebilirdiniz. Sözünü ettiğimiz kurallar demetini size sürekli bir servis yolu sağlamayı öngörüyor ve bu yolun hem gidişte, hem de gelişte izlenecek levhaları gibi, kıt’alar arası telefon bağlantılarının kesilmesi halinde, bilgisayarlararası iletişimin devamını sağlıyor.

HTTP’nin resmen standart olarak tanınması, 1990 yılında World Wide Web Konsorsiyomu’nun (W3C) kurulmasıyla mümkün olduğu için, bugünkü Internet’in de doğum tarihi 1990 yılı sayılabilir. Doğumundan bu güne 10 yıl bile geçmemiş olduğu halde, Internet’in hem HTTP, hem de HTML ilkeleri ihtiyaca yetmemeye başladı.

W3C, şu anda HTTPNG (Gelecek Kuşak) adını verdiği, standart üzerinde çalışıyor. Bu yeni kurallar demeti, HTTP’nin özellikle ses ve video gibi henüz ortak standarta kavuşturulmamış çoklu-ortam malzemelerinin alınıp-verilmesini kolaylaştırmayı öngörüyor. HTML’in önceden tanımlanmış komutlarını, Internet sayfası hazırlayanların kendi ihtiyaçlarına göre değiştirmesi sağlayan olan XML (Extensible Markup Language-Genişletilebilir İşaretleme Dili) ise bugün-yarın Netscape ve IE tarafından kabul edilir hale gelecek. Bu arada duragan bilgi kümesi alıp-verebilen HTML’e, dinamik-değişken özellikler kazandırmayı öngören ekler ortaya DHTML ilkelerini çıkarttı. Ne var ki DHTML diye adlandırıbalicek ortak bir standart olmaması, bunun, hiç değilse şimdilik, Internet ile bağlantı sağlayan programların sürümüne göre değişik anlamlar taşıması, Internet alanları için veri hazırlayanların (Web sayfası yapanların) çektiği sıkıntıyı artırıyor. XML ise ortak bir dinamik Web sayfası standardı getirmekten çok, ihtiyaca göre değiştirilebilir HTML oluşturmayı öngörüyor.

HTML’in belki Internet’teki pabucu tümüyle olmasa bile kısmen dama atılabilir. Ama firmaların kendi yerel ağ ortamlarında haberleşme ve bilgi alış-verişinde giderek daha sık uygulamaya başladıkları Intranet, Web gibi, giderek daha geniş kitlelerin ilgisini çekebilmesi için televizyon özelliklerine sahip olmak zorunda değil; HTML’in bugünkü haliyle izin verdiği çoklu-ortam uygulamaları, herhangi bir firmanın en ilgi çekici ve en etkili tarzda iç-iletişim yapmasına yeter. Başka bir deyişle, HTML, Internet’te ve intranet’lerde daha uzun süre yaşayacaktır.

Biz bu kitapçıkta daha çok Internet ve Internet’te yer alan sanal ortamlardan biri olan World Wide Web (Dünya Çapında Ağ) ortamından söz edeceğiz. Ancak bir çok yerde Internet sözünü kaldırıp, yerine intranet kelimesini koyarsanız, o bilgilerin Web kadar, bir firmanın yerel ağında oluşturacağı dahilî internet’e de uygulanabilir olduğunu göreceksiniz.

Klasik HTML’in temel ilkelerini biraraya getirmeyi öngören bu kitapçık, bugün olduğu gibi, ilerde de, Internet için olduğu kadar intranet için de Web sayfası hazırlamak isteyenlerin başvurabileceği bir kaynak olmak üzere kaleme alındı. Bu kitapçığın Internet protokolleri (iletim kuralları) ve Web tasarım ilkelerine ayrılan ilk iki bölümü, konuya aşina olmayanların temel bilgileri edinmeleri, konuya yabancı olmayanların ise bir çok yerde parça-parça duyduklarını bir arada görerek, bilgilerini tazelemelerini amaçlıyor. Daha sonraki bölümler ise ilerde, HTML kullanarak Web tasarımı yaptığınız zaman, örneğin bir komutun, bir etiketin kolay hatırlanmayan yüklemlyerini (parametrelerini) hatırlamak üzere başvurabileceğiniz bir rehber niteliğinde.

Konuya aşina olanların tümüyle atlayabilecekleri birinci bölümde, WWW, HTTP, TCP/IP ve HTML kısaltmalarının anlamını ve ne işe yaradığını en az birer paragrafta anlatabilecek kadar bu konunun içinde olmayanların yararlanabilecekleri bilgiler yer alıyor. Bir Web alanında, ya da daha teknik terimle HTML sayfasında, başlıca unsur metin olduğu için, kitapçığımızın ikinci bölümünü, HTML kodunun ana araçlarını tanıttıktan sonra metin girme ve metni biçimlendirme konusuna ayırdık. Ancak HTML’in metinle ilgili araçları, görsel açıdan etkili ve bir iskeleti olan sayfa inşasına izin vermediği için, bir anlamda metin sunma araçları olan tablo, çerçeve ve katman unsurlarından sayfa iskeleti oluşturmak için yararlanmak zorunda kalıyoruz. Bu üç unsura, üçüncü bölümde ayrıntılı olarak yer veriyoruz. Bu noktaya kadar değinmediğimiz fakat bugünkü Internet’i Internet yapan unsura, yani bir sayfadan diğerine, bir grafikten bir diğerine, bir kelimeden bir başka paragrafa, kısaca bir bağlantı noktasını tıklayarak, dünyanın öbür ucuna gitme imkanı veren bağlantı konusunu dördüncü bölümde ele alacağız. Bu noktada, duragan yani bağlantıları konulmuş ama kendiliğinden hiç bir şey yapmayan bir Web alanı oluşturmayı öğrenmiş olacaksınız. Fakat günümüzde Web alanları, ziyaretçinin kullandığı tarayıcının türünü ve hatta sürümünü belirleyip, ona göre içerik sunan, ziyaretçinin önceki ziyaretinde neler yaptığı, hangi sayfalarla ilgilendiğini hatırlayıp, bu kez ona uygun bağlantılar veren dinamik alanlar haline geldi. Bunu sağlayan Dinamik HTML (DHTML), beşinci bölümün konusunu oluşturacak. Altıncı bölüm ise, belli başlı HTML kodlarının (etiketlerin) tanımları, kullanıldığı yerler, alabilecekleri yüklemler (parametreler) ve örneklerine yer verdiğimiz Başvuru bölümü olacaktır.

HTML’e hayat veren, kişisel bilgisayarları Internet’e ve intranetlere bağlayan tarama programlarının bu dili nasıl ve ne ölçüde yorumladıklarıdır. Şu anda dördüncü sürümü yavaş yavaş uygulama bulan bir formüller topluluğu, gelişen bir organizma gibi. Bir süre sonra bu kitapçıkta yer almayan HTML etiketleri karşınıza çıkabilir, ve Web tasarımcısı olarak bu yeni komutları, kullanıldıkları yerleri ve işlevlerini, bu kitaptaki bilgilere eklemek zorunda kalabilirsiniz.

Hayat, zaten, baştan sona bir öğrenme süreci değil mi?

Dil Deyince:

HTML kısaltmasını bile Türkçe’ye çevirmediğimize bakarak, bu kitapçığın yarı İngilizce olduğunu düşünebilirsiniz. Fakat bu kitapçık bir dilin, geçmişi ile geleceği ile, bilim ve kültürün her alanında ifade imkanına sahip olması gerektiği inancıyla kaleme alındı. Türkçe’ye bu imkan, başka dillerden alınan kavramların öncelikle Türkçe ifade edilmesi ile kazandırılabilir. Bunu yaparken, bazı kelimelere yeni anlamlar yükleyerek görev alanlarını biraz uzatmak ve bunu önce ilgili topluluğun, sonra tüm toplumun onayına sunup beklemek gerekir. Ama Türkçe’nin kendi türetme kurallarını hiçe sayarak, ilgisiz fiillere hiç olmayacak ekler ekleyip, ortaya yeni isimler çıkartmak asla kabul edilebilir bir uygulama olamaz. Anlamını karşılayamadığımız, ya da mevcut kelimeleri biraz çekiştirerek uyduramadığımız İngilizce kelimeleri çevirmek için yeni kelime uydurmadık, öylece kullandık ve açıklamaya çalıştık. Elbette dil ve toplum bu kavramları karşılayacak kelimeler üzerinde anlaşacaktır.

# Bölüm I: Web’e Giriş

## Temel Bilgiler

Bu bölümde, HTML ile neler yapılabileceği ve neler yapılamayacağına bakacağız. Yine bu bölümde, tasarlayacağınız Web alanlarının, sizin (ya da sayfalarınıza ev sahipliği yapacak firmanın) bilgisayarlarından, ziyaretçinin bilgisayarına ulaştırılma yollarına değineceğiz. Sonuç itibariyle, Web alanı tasarlayan kişi, bu ulaşımın ucunda, ortasında ve sonunda da yer alan programlara, onların imkan ve sınırlamalarına bağımlı demektir. HTML’i kullanarak Web sayfası tasarlayacak kişinin bunu bir şekilde başkalarının hizmetine sunacağı varsayılır. Bu nedenle, HTML öğrenen kişinin sonunda bir Web alanına sahip olacağını düşünebiliriz. Dolayısıyla bu bölümde, kısaca, Web hizmeti sunmakta kullanılacak bilgisayarların sahip olmaları gereken donanım ve yazılım özelliklerinden de kısaca söz edeceğiz. Web Server’a koyacağınız HTML sayfaları ne kadar fiyakalı olsa da, HTML’in imkan ve yetenekleri, onu alan ve yorumlayan tarayıcı (browser) programının yetenekleri ile sınırlıdır. Bu nedenle Web tasarımcının, tarayıcı programları çok iyi tanıması gerekir. Bir tarayıcıda adeta televizyon filmi gibi gösterilebilen bir unsurun yerini, başka bir tarayıcıda gri zeminli boş bir kutu alabilir. Ya da aynı tarayıcıya sahip olan iki ziyaretçiden biri, sayfanıza girdiği anda en sıcak ve candan sesli hoşgeldiniz mesajınızı dinlerken, diğeri hiç bir şey duymayabilir. Tarayıcılar kadar, tarayıcıların özelleştirme yeteneklerini tanımak ve kullanıcıların genellikle ne gibi özelleştirmeler yapabildikleri hakkında fikriniz olması gerekir. Bu nedenle, bu bölümün sonunda mevcut en yaygın tarayıcıların ortak ve farklı önemli özelliklerine de bakacağız.

## HTML’e Genel Bakış

Programlama dili gibi görülse de, görülmese de, bugün Internet’in de intranet’lerin de ortak dili, HTML’dir. Bir Web sayfasında yer alan belgenin içindeki bazı kelimeler, simgeler, fotoğraflar, grafik unsurlar veya bunların parçaları bir başka sayfa ile hiper-link kurularak, ilentilendirilmiştir. Kullanıcı, hiç bir komut öğrenmek zorunda kalmadan, hiç bir bağlantının Internet’teki adresini bilmek zorunluğu olmadan bu sayfalardaki bağlantıları tıklayarak, yazıdan yazıya, şekilden şekilde, gidebilir. Ta ki, arzu ettiği bilgiyi bulup, okuyuncaya, kendi diskine veya disketine kopya edinceye veya yazıcısında basıncaya kadar. Aslında kullanıcı ya da ziyaretçinin bir HTML sayfasıyla ilişkisi burada da bitmemektedir. Çoğumuz ulaştığımız bir alanın adresini Web tarayıcı programında sık sık ziyaret etmek istediği yerlerin arasına koyabilir (bookmark) ve arzu ettiği zaman doğruca işaretlenmiş olan bu adreslere gidebilir.

HTML’in başlıca özelliklerini şöyle sıralayabiliriz:

1. Belge biçimlendirme: HTML, Wes tasarımcısına, belgelerini ziyaretçinin ekranında nasıl oluşmasını istiyorsa öyle şekillendirme imkanı verir. Bununla birlikte tarayıcı programlarının (Netscape Navigator veya Internet Explorer) HTML komutlarını yorumlayışlarında az da olsa fark vardır ve bu fark sayfalarınızın bir ziyaretçinin bilgisayarında başta, diğerinin bilgisayarında başka gösterilmesine yol açabilir. Ayrıca ziyaretçileriniz, tarayıcı programlara verdikleri komutlarla, aldıkları sayfalarda genel değişiklik veya kısıtlamalar yapabilirler. Siz sayfanızda ne tür harf türü (font) kullanmış olursanız olun, ziyaretçiniz tarayıcı programa “Sadece Times fontları kullan” demiş ise, sayfanız bu ziyaretçinin ekranında sizin istediğinizden farklı biçimde görülecektir. Ziyaretçi tarayıcı programına “Grafik unsurları gösterme!” demiş ise, sayfalarınız ve tabiî vermek istediğiniz görsel mesaj tamamen farklı bir nitelik kazanacaktır. Bu duruma rağmen, bugünkü şekliyle HTML, Web tasarımcısına adeta bir gazete ya da dergi sayfası tasarlarcasına, oluşturmak istediği görsel etkiyi sağlamasına yeterli tasarım araçları sunmaktadır.

2. Bugünkü imkanlarıyla HTML, Web sayfası terimine yeni bir anlam kazandırmış bulunuyor. “Web sayfası” terimi bile, eski, yani dört-beş yıl öncesinin Web sayfaları, içi bir örnek harflerden oluşan yazılarla dolu, duragan belgelerden ibaret bulunduğu için ortaya atılmıştı. Bugünkükü Web sayfalarının “sayfa” kavramı ile dahi ilgisi kalmadı. Bugün sadece HTML ögeleri kullanılarak, ziyaretçinin ekranında adeta bir televizyon programının grafik etkisini sağlamak mümkün. Bununla birlikte HTML, bir kelime işlem ya da masaüstü yayıncılık programının oluşturabileceği görsel özelliklere sahip sayfalar oluşturamaz. Bu kısıtlamalara, Internet’i tasarlayan uzmanların, platformlar (Windows 3.x, Windows 95/98, Windows NT, Unix, MacOS), donanımlar (Macintosh, PC, Sun) ve tarayıcı programlar arasındaki farkların, sunulacak malzemenin tasarımcının kastettiğinden tamamen farklı bir şekilde sunulmasına yol açmasını önleme arzusu neden oluyor. HTML, örneğin bir masaüstü yayın programı kadar hassas ölçmelere ve biçimlendirmelere izin verse idi, bu ancak belirli bir platformda, belirli bir program kullanmayı gerektirirdi. Oysa Internet’i Internet yapan unsurların başında, hemen herşeyin ekranda ve kağıt üzerinde, ortak denilebilecek şekilde oluşturulması geliyor.

3. HTML ile oluşturulacak statik alanların içine dinamik sonuçlar doğuracak programlar konulabilir. Bu programların oluşturulması için, ziyaretçinin Internet’e PC veya Macintosh ile bağlanmış olması, ya da bağlantı programının şu ya da bu firmaya ait bulunması gibi farklılıklardan etkilenmeyen, her türlü ortamda aynı sonucu veren ortak bir dil geliştirme çabası, ortaya Java adlı programlama dilini çıkartmış bulunuyor. Microsoft’un Visual Basic programlama dilinin bir türevi olan VBScript ve çeşitli firmaların ortaklaşa ürünü Javascript de bu tür çabaların sonuçlarıdır. Adı benzemekle birlikte, Javascript’in Java ile, VBScript’in de Visual Basic ile ilgileri yoktur. Internet tarayıcı programlarından Internet Explorer hem Javascript, hem de VBScript dillerini anlayabilir ve yorumlayabilir. Buna karşılık Netscape tarayıcı programı VBScript diliyle yazılmış bölümler içeren bir HTML metnini yorumlayarak, ekrana getiremez. Bugünkü şekliyle Java dili de, Javascript ve VBScript de, tarayıcı programların imkan ve kabiliyetleri ile sınırlıdır. Ancak her üç dili kullanarak, HTML sayfalarını duraganlıktan çıkartmak ve ziyaretçi ile etkileşen, ziyaretçinin arzu, beğeni ve özelliklerine göre içeriğini değiştirebilen Web alanları tasarlamak mümkündür

## HTTP ve TCP/IP

Web sayfası tasarlarken, dikkat edeceğiniz en önemli unsur, sayfalarınızın içeriğinin sunuluş biçiminin önemli ölçüde ziyaretçinin bilgisayarının türü (Mac, PC, Sun), ziyaretçinin işletme sistemi (Windows 3.x, 95/98, NT, MacOS, Unix) ve kullandığı tarayıcı yazılımı (IE, Netscape, Mosaic, vs.) tarafından belirleneceği olmalıdır.

Bir Web sayfasının ziyaretçinin ekranına kadar kat’ettiği yolda çeşitli protokoller (kurallar) var. Bunların başında bir bilgisayar ağı olan Internet’in iletim kuralları (HTTP) geliyor. Hypertext dosyalarını olduğu kadar çoklu ortam unsurlarını (ses, video ve diğer grafik ögelerden oluşan Multimedia dosyalarını) ve bilgisayar programlarını ağ içindeki bilgisayarlar arasında alıp-vermeye yarayan başka protokoller de vardır: FTP (File Transfer Protocol-Dosya Aktarma Kuralları) bunlardan biridir.

Internet bağlantısı, bir telin iki ucunda bulunan iki bilgisayar arasındaki ilişki olarak görebilirsiniz. Sizin Web sayfalarınızın durduğu bilgisayar Web ilişkisinde “Server” (Hizmet eden) diye adlandırılır. Ziyaretçinin Internet’e telefon bağlantısı ile bağlı bilgisayarı, ise sizin için Client-Müşteri sayılır. Hizmet veren bilgisayarla, bu hizmetin müşterisi olan bilgisayar (Server ile Client) arasındaki ilişkiyi düzenleyen kurallara TCP/IP adı verilir (Transmission Control Protocol/Internet Protocol-İletim Denetim Kuralları/Internet Kuralları). Gerek HTTP, gerekse FTP, müşterinin, sizin bilgisayarınızdan, yani Web Server olarak adlandırdığımız HTML sayfaların ve bu sayfaların içinde yer alan resimlerin, grafiklerin, ses ve video dosyalarının durduğu bilgisayardan bilgi isteme ve bu istediğine karşılık verildiğinde verilen karşılığın doğru gelip gelmediğini anlamasını sağlar. İki bilgisayarın üzerinde anlaştıkları bir tür konuşma adabı diyebileceğimiz bu kurallara uygun mesajlarını, kıt’adan kıt’aya, ülkeden ülkeye, kentten kente, yeraltı ve sualtı kabloları ile, uydularla iletirler. Tahmin edilebileceği gibi, müşteri bilgisayar ile servis sunan Web Server arasında oluşan bu bağlantı, bazen kesilebilir. Fizikî bağlantının kesilmesi, iletimin kesilmesi anlamına gelmemesi için, Internet Kuralları’nın IP bölümü, iki bilgisayar arasındaki bağlantının doğru kanallardan kurulmasını, kesildiğinde yeniden kurulmasını sağlar. Bunu yaparken, evrensel bir adres sisteminden yararlanır. Internet’te servis sunan bilgisayarlar, başka bir deyişle Web Server’lar kaynak sayıldığı için, IP, aradığı kaynağı Universal Resource Locator (URL) sistemini kullanarak bulur. Aynı kurallar demetinin TCP bölümü ise kurulan bağlantı sayesinde gelen bilginin doğru anlaşılmasını sağlar.

Aslında her bilgisayar, CPU ile ekran, CPU ile klavye, CPU ile CD-ROM sürücü arasında bir ağ demektir. Bir büro ortamında bir bilgisayar ile merkezdeki Server, bir ağın parçalarıdır. Bu ağların Internet denen dev ağdan farkı, sizin bilgisayarın CPU’su ile klavyesi, ekranı ve yazıcısı arasındaki bağ, yine bir büro ortamındaki bilgisayar ile merkez bilgisayar arasındaki ilişki, “sabit durum” ilişkisidir. Yani, bu ağlarda iki taraf birbirinin durumuna her an vakıftır; birbirlerinin ne durumda olduklarını her an bilirler. Oysa, iki kıt’a arasında kurulmuş bir Internet ilişkisinde, müşteri hizmet verenin, hizmet veren müşterinin durumunu, bağlantıdaki kesilmeler nedeniyle, bilemeyebilir. Bu nedenle TCP/IP, “durumun bilinmediği ilişki” esasına dayanır. Müşteri bilgisayar, servis sunucudan istediğini HTTP veya FTP kurallarına göre talep eder. Bunun için Web Server’ın kendisini bulup, bu talebi doğruca ona iletmesine gerek yoktur; bu talebini kendisine Internet bağlantısı sağlayan (ISP) firmanın bilgisayarına iletmesi yeterlidir. Bunu yaparken talep ettiği şeyin adını-sanını bildirdiği gibi bulunacağı kaynağı belirlemek için gerekli, adresi de (URL) bildirmek zorundadır. Internet hizmeti sağlayan firmanın bilgisayarı, bu talebi ve talebi karşılayacak kaynağın adresini, Internet’in omurgası olarak adlandırılan ana bağlantıyı kuran bakımını yapan ve ISP’lere hizmet sunan firmanın bilgisayarına iletir. Ana omurga firmasının bilgisayarlarında dünyadaki tüm Internet kaynaklarının listesi ve onlara ulaşmak için hangi omurgadan kime yol açılması gerektiğini gösteren bir liste bulunur. Ana omurga şirketinin bilgisayarı bu listeye göre, müşterinin talebini diğer bir ana omurga firmasına, o firma da bunu hedef Web Server’a ev sahipliği yapan (host) bilgisayara iletir. Bu talep, hedef Web Server’a talebin konusu ve talep edenin adresi ile birlikte bildirilir. Sizin müşteri olarak o sırada sadece kendi Internet hizmet sunucunuzla bağlantınız sürmektedir; yoksa sizin bilgisayarla hedef Web Server arasında doğrudan, bire-bir ilişki yoktur. Hedef Web Server, müşteri olarak sizin kim olduğunu ve size nasıl ulaşabileceğini, ancak kendisine gelen talebin altındaki adresten bilmektedir. Web Server, sizin o anda kendi Internet Hizmet Sunucu’nuzla arasındaki bağlantının devam edip etmediği ile hiç mi hiç ilgilenmez. Onun için önemli olan kendisine iletilen talebin karşılığını, talebin altındaki adrese iletmekten ibarettir. Aynı yol bu kez tersine kat’edilir; arzu ettiğiniz bilgi (sayfa, belge, video, ses, resim, fotoğraf, vs.) sizin ekranınıza ulaşır. Kısaca, ne talep sahibi müşteri bilgisayar, ne talebi karşılayan Server bilgisayar, bir diğerinin o anda nerede ve ne durumda olduğu ile ilgilenmez. Bu “durumdan haberdar olmama” hali ve etkilerine, ilerde Internet’te ticaret bahsinde geri döneceğiz.

## Web Server

HTTP ve FTP, müşteri bilgisayarla, servis sunan bilgisayarın üzerinde anlaştıkları bir dille (HTML) birbirine ilettikleri talep ve talebin karşılığı olan malzemenin alınıp verilmesinde TCP/IP denilen kurallardan yararlanılarak yapılan iletimi düzenleyen ilkelerdir. Bu ilkelere uygun olarak çıkartılan bir talep Web hizmeti sunan bilgisayar tarafından karşılanır ve karşılık olarak belirli bir bilgi kümesi müşteri bilgisayara iletilir.

Web server olarak tayin edilmiş bilgisayarda, kendisine gelecek HTTP ve FTP taleplerini anlamasına ve bu talepleri yerine getirmesine yarayan programlar (örneğin Apache Web Server, MS Internet Information Server veya Netscape Web Server) sürekli çalışır vaziyette olur. Bu programların, bilgi alıp-vermenin yanı sıra, elektronik posta alıp verme ve yönlendirme, veritabanlarına erişme ve içinden seçme yapma (Querry, SQL, vb. gibi), kendi sabit diskinde duran bir dosyayı alıp karşı tarafa aktarma (FTP, Gopher, WAIS) veya karşı tarafın vereceği dosyayı alıp kendi sabit diskine kaydetme yeteneği olur.

İlk Web Server programı, yukarıda, HTML dilinin geliştirilmesindeki öncü konumu nedeniyle sözünü ettiğimiz, İsviçre’deki CERN kurumu tarafından geliştirildi; ama kısa zamanda UNIX platformunda, anonim bir tarzda ve ücret ödemeden kullanılabilen bir şekil aldı. NCSA Server, National Center for Supercomputing Applications-Superbilgiişlem Uygulamaları Ulusal Merkezi adlı, şimdi kapanmış olan kurum tarafından UNIX işletme sistemi için geliştirilmişti. NCSA Server’ın geliştirilmiş şekli olan Apache Server ise uzun süre ücretsiz dağıtıldıktan sonra günümüzde ticarî olarak geliştiriliyor ve satılıyor. Bugün halâ NCSA Server veya Apache’nin ücretsiz sürümlerine dayalı Web alanları bulunmakla birlikte, Sun Solaris, IBM AIX ve diğer UNIX sistemleri için geliştirilmiş çok sayıda Web Server hizmete girmiş durumda. Kişisel bilgisayarların UNIX gerektiren bilgisayarlara oranla daha ucuz olması, Microsoft’un NT, IBM’in OS/2 işletme sistemlerinin UNIX’e ciddî rakip haline gelmiş bulunmaları nedeniyle, bu sistemlere dayalı Web Server programları da hızla artıyor. Apache Web Server’ın bile NT sürümü piyasaya çıktı.

NT Workstation ve Windows 95/98, aslında Kişisel Web Server adı verilen, Internet’e 24 saat bağlı olmadan, başka bir firmanın ev sahipliği yaptığı Web alanlarına hizmet sağlayabilir. Hatta NT Workstation, aynı anda 10’u geçmemek üzere, 24 saat süreyle ınternet’e bağlanabilecek ve müşteri taleplerini karşılayabilecek yetenektedir. Aynı anda daha fazla Internet bağlantısını kaldırmak istiyorsanız, NT’nin Server sürümünü edinmeniz gerekli. IBM’in OS/2 işletim sistemi ise, Internet Connection Server adlı paket kurulduğu zaman, bir PC’nin fiziksel olarak kaldırabileceği kadar Internet bağlantısına cevap vermesini sağlamaktadır. Macintosh bilgisayarları için Starnine firmasının MacHTTPd programı gibi, ücretsiz edinilebilecek http4Mac ve EasyServe adlı programlarla, Internet servisi sağlamak mümkün.

Ayrıca, bugün PC’lerde de UNIX işletme sistemi kurmak hem kolay, hem ucuz hale gelmiş bulunuyor. Solaris, BSDI, Esix, SCO UNIX bu alandaki ticarî programlar. Ayrıca Linux ve FreeBSD adlı, ücretsiz dağıtılan UNIX işletme sistemleri de, ticarî olanları aratmayacak niteliklere sahip. Ayrıca bu tür ücretsiz programlar, Apache Web Server’ın ücretsiz sürümünü de içeriyorlar.

Bir PC ile Web Server hizmeti yapacaksanız, önünüzdeki bir çok seçeneğe rağmen, başarınızın PC’nin gerçekten sabit disk alanı ve belleği bol olmasına bağlı bulunduğunu hatırlamalısınız. PC’lerin, Internet’in gerektirdiği en önemli özellik olan aynı anda birden çok iş yapabilme becerisi, işletim sistemi kadar, donanım kaynaklarının genişliğine bağlı olduğunu unutmamalısınız.

Bir Web Server yazılım paketi seçerken dikkat edilmesi gereken bir kaç ilkeyi sıralayalım:

1. Yazılım paketi yeterli güvenliği sağlayacak özelliklere sahip olmalıdır. Binalarda bir odadaki yangının yandaki odaya sıçramasını önleyen ateşe dayanıklı duvarlardan (Firewall) esinlenerek adlandırılan bir dizi program, Web Server yazılımının bulunduğu bilgisayarın, kötü niyetli kişiler tarafından bozulmasına engel oluyor. Ancak Web Server’ın kendi içinde mevcut güvenlik önlemlerinin neler olduğunu dikkatle araştırmanız gerekir. UNIX işletme sistemi ve ona bağlı çalışan Web Server programlarının daha güvenli olduğuna ilişkin, kimi zaman Web tasarımcısını ve Internet hizmet sunucusunu rahatlatan, yaygın bir söylenti vardır. Bu doğru değil. Ne türü olursa olsun, UNIX de bir işletme sistemidir ve el elden üstündür. Kötü niyetli bir kişi Windows NT sistemine verebileceği zararı, aynı rahatlıkla UNIX’e de verebilir. Bir diğer yaygın ve aynı ölçüde yanlış inanç ise NT’nin güvenli olmadığıdır. Microsoft firmasının NT’nin 4’ncü sürümünü güncelleştirmek için dağıttığı SP3 adlı tamir programının yerleştirilmesinden sonra, NT sistemleri güvenlik açısından herhangi bir başka işletme sistemiyle boy ölçüşebilir hale geldi. Burada önemli olan, Internet’e açılmanın, iyi niyetli-kötü niyetli herkese açılmak olduğunu unutmamaktır. Özellikle form denilen, HTML’in ziyaretçi bilgisayarın evsahibi bilgisayara talepten başka şeyler göndermesine imkan veren etiketlerini ve ona bağlı CGI (Common Gateway Interface-Ortak Geçit Arabirimi) adı verilen ziyaretçinin ev sahibi bilgisayardaki programları harekete geçirebildiği buluşma noktasında yer alacak programları tasarlarken, daima kötüniyetli kişileri dikkate alarak hareket etmek gerekir. Internet’te güvenliğin ne kadar kolay sarsılabildiğine ve ne kadar kolay önlem alınabileceğini bir örnek verelim. Sayfanızda, ziyaretçinin doldurması gereken “Elektronik Posta Adresiniz:” diye bir metin kutusu bulunduğunu düşünün. Bu kutuya bütün ziyaretçilerin elektronik posta adreslerini yazacaklarını düşünüyor ve bu bilgiyi işleyecek CGI programında, ziyaretçinin bu kutuya yazacağı bilgiyi, alıp doğruca Web Server’ın “Mail” programına veriyorsunuz. Peki, ya kullanıcı adres yerine “herkimse@herneredeyse.com; mail haydut@soygun.com</etc/passwd” yazarsa? Bu basit elektronik posta adresi, sizin Mail Server’ınızın bilgisayar sisteminizdeki bütün password-parola dosyaları Soygun.com’daki “Haydut” isimli arkadaşa postalamasını sağlayacaktır. Oysa, CGI programını yazan kişi, elektronik posta adresini Mail programına gönderirken “unless ($mail\_to = ~/^\[\\w-.\]+\\@\[\\w-.\]+$)” şeklinde bir satırla, Web ve Mair Server’larla işletme sisteminin “metakarakter” denilen ve bir isim veya adreste değil de sadece komutlarda yer alabilecek karakterlerin bulunup-bulunmadığını denetlerse, sorun kökünden halledilebilecektir.

2. Mahremiyetin Korunması ve Doğrulatma: Web hizmeti sunan kişi, sadece başkalarının kendi bilgisayar sisteminde arzu edilmeyen şeyler yapmalarını önlemekten değil, aynı zamanda kendisine tevdi edilen başkalarına ait bilgileri de saklamak ve başkalarından korumak zorundadır. Bu bilgiler, ziyaretçinin adı, elektronik adresi, hatta kredi kartı numarası olabilir. Bunlar, sizin Internet’te çizdiğiniz portreye güvenilerek size verilmiş mahrem bilgilerdir. Ziyaretçi bu bilgileri size, kötüye kullanılmayacağı güvencesiyle vermektedir. Bu bilgilerin korunması, sizin birinci derecede sorumluluğunuzdadır. Aynı bağlamda, Web hizmeti sunan kişi olarak, sizin de bu bilgilerin kolayca ve başkalarına açık hale getirilmeden doğrulatılmasına ihtiyacınız olacaktır. Web Server programınız, örneğin kredi kartı numarasını, yeni programlar edinmeye ihtiyaç kalmadan doğrulatabiliyor mu? Yeni bir kredi kartı firmasının çıkartacağı elektronik alış-veriş yöntemi, sizin Web Server’ınıza kolaylıkla uyarlanabilir mi? Microsoft gibi, IBM gibi firmaların paket program olarak sundukları Web Server’lar, çoğu zaman bu firmaların protokollerini tanıyan her türlü ek programı kabul ederler. Oysa Internet’ten ücretsiz olarak edinilebilecek bir Web Server programı, belki maliyet açısından çok daha uygun görülebilir, ama daha sonraki ekleri kabul edemez.

3. Web Server, sizin Internet sayfalarınızı ziyaret edecek kişilerin bilgisini doğru tutuyor mu? Web hizmeti sunan kişi olarak, kimin hangi sayfadan sizin sayfasına atladığını bilmek, kendi sayfanızın reklamını bu sayfalarda daha çok yapmanıza imkan verir. Özellikle elektronik ticarete dayalı veya mesajını daha çok sayıda kişiye iletmek amacıyla hazırlanan Web alanlarını işletenlerin, sayfalarının varlığını duyurmak için, mümkün olan her yoldan yararlanmaları gerekir. Web Server, size bu kolaylıkları sağlamalıdır. Web Server, kimin hangi tür bilgileri edinmek istediğine ilişkin rapor tutmalıdır. Bu raporu incelemekle, Web alanınızda hiç talep edilmeyen bilgilerden çok, talep edilen alanlarda daha çok bilgi sunabilirsiniz.

4. Web Server programıyla ilgili teknik destek ve sorun çözme hizmeti alıp almamak, programın seçiminde belki de en önemli unsur sayılabilir. Özellikle başlıca işi bilgisayar mühendisliği olmayan bir hizmet sunucu, yazılımın donanımla uyumunu sağlamada karşılaşabileceği güçlükleri, ancak yazılımı piyasaya süren firmanın teknik servisinden veya o yazılımla ilgili uzmanlığı olan danışmanlardan sağlayabilir. Piyasada hiç tanınmayan veya Internet’ten ücretsiz olarak edinilebilen--dolayısıyla belirli bir firmanın malı olmayan—Server programları, çoğu zaman gerekli teknik destekten de mahrumdur. Buna karşılık büyük yazılım firmalarının programları, firmanın kendi mühendis ve uzman kadrosu, ve buna ek olarak bu programlara destek sağlayarak hayatını kazanan kişiler tarafından en ince ayrıntılarına kadar bilinmektedir. Bir gece yarısı çöken Web Server’ı yeniden çalıştıramamanın bedeli, o programın ilk maliyetinden çok daha yüksek olabilir.

## Web Tarayıcıları

Web tasarımcısının, HTML komutları kadar, hatta onlardan da çok iyi bilmesi gereken, tarayıcıların HTML’i nasıl yorumladığıdır. Bu nedenle bir Web tasarımcısının bilgisayarında, Web server yazılımı bulunmayabilir (sayfalarına başka bir Internet Web Server hizmeti veren kişi veya firma evsahipliği yapıyor olabilir), ama mutlaka piyasaya mevcut Web tarayıcılarının hemen bütün geçerli sürümleri bulunmalıdır. Netscape firmasının Navigator ve Communicator adıyla piyasaya sürdüğü farklı sürümleri ayrı ayrı dizinlerde durmak şartıyla aynı bilgisayarda çalışabilir. Anacak Microsoft firmasının Internet Explorer adlı programının farklı sürümleri aynı Windows ortamında birarada bulunamazlar. Bunun için iddialı bir Web tasarımcısının, bu programın farklı sürümleri için birden fazla bilgisayar bulundurması gerekebilir.

Neden değişik tarayıcıların değişik sürümlerine ihtiyacınız var? Bu sorunun cevabı, HTML’in ınternet’in ortak dili olduğu gerçeğine bir ölçüde gölge düşürecektir. Çünkü ortak bir HTML dili bulunmasına rağmen, tarayıcıların ve aynı tarayıcının farklı sürümlerinin HTML’i yorumlayışı farklıdır. HTML, Uluslararası Web Konsorsiyomu adlı kuruluşun çıkarttığı, adı “tavsiye” olmakla birlikte kendisi standart sayılan dördüncü sürümüne ulaşmış bulunuyor. Böyle bir standartlaşmaya rağmen, Netscape ve Microsoft firmaları, bilgisayar kullanıcılarının rağbet ettiği tek tarayıcı programın kendi programları olmasını sağlamak üzere giriştikleri rekabet çerçevesinde, programlarını sadece HTML’i aynı şekilde yorumlayan ve dolayısıyla birbirinden farksız sonuçlar veren programlar olmaktan çıkartmak istediler. Bunun sonucu ise, Web tasarımcısının, kimi zaman Netscape’in anladığı ama IE’nın anlamadığı, kimi zaman IE’in becerebildiği, buna karşılık Netscape’in henüz programına koyamadığı HTML özelliklerinden hangisini kullanacağına bir türlü karar veremez duruma düşmesi oldu.

HTML’i kullanarak, ticarî amaçlı Web tasarımı yapan kişi, Internet ile bağlantılı bilgisayar kullanıcılarının (Internet kullanıcılarının) hepsinin ekranında aynı şekilde gösterilecek sayfalar yapmaya mecburdur. Buna karşılık bir firmanın intranet ortamı için Web tasarımı yapan kişi, HTML’in sadece kendi firmasının standart olarak benimsediği tarayıcının anlayabileceği özelliklerinden yararlanması mümkündür.

### Microsoft Internet Explorer

Windows ortamında tarayıcı piyasasına, diğer tarayıcılardan sonra girmesine rağmen, Microsoft’un Web tarayıcı programı, piyasa payındaki artış hızı bakımından da, HTML’in tanıdığı özellikleri ve HTML’e ilave ettiği diğer görsel kabiliyetler bakımından da, diğer programları geride bırakmış bulunuyor. 1997 sonbaharında 4’ncü sürümü piyasaya çıkan IE, giderek Windows ortamının masaüstü ile bütünleşiyor. IE artık sadece bilgisayar kullanıcısının Internet ile bağlantı kurmasını ve Internet’ten alacağı HTML sayfalarını ekrarında canlandırmasını sağlamakla kalmıyor, aynı zamanda bilgisayarın disklerinin taranması ve dosya yönetimi gibi işleri de yapıyor. Windows 98’in ve NT’nin hazırlanmakta olan beşinci sürümünün yardım dosyaları da IE vasıtasıyla okunuyor. IE’nin, sürümleri daha geriden gelmekle birlikte Macintosh uyumlu sürümü de bulunmaktadır. IE’nin UNIX sürümü, 1998 yaz sonu piyasaya sürülmek üzere hazırlanmaktadır. IE, Microsoft’un Internet alanından ücretsiz indirilebilir veya sadece CD masrafı ödenerek, firmadan posta ile de istenebilir.

### Netscape Navigator

Netscape Communications Corporation’ın (NCC) piyasaya sürdüğü NN, IE’ın hızlı yükselişine rağmen, kurulduğu bilgisayar sayısı bakımından piyasanın en yaygın tarayıcısıdır. NN, sadece Windows ve Macintosh ortamlarında değil, fakat aynı zamanda UNIX işletme sisteminde de işleyebilmektedir. NCC, yakın zamana kadar, hem tarayıcı, hem de Web Server programları alanında Internet’te öncü konumda idi. Internet’in bugün sahip olduğu bir çok özellik, HTTP ve FTP ilkelerinin çoğu, bu firmanın tasarımı sonucudur. Eğitim kurumları ve kâr amacı gütmeyen kuruluşların mensupları ile programdan kişisel amaçlarla yararlanmak isteyenler, NN’i ücretsiz olarak kullanabilirler. Ticaret amaçlı kullanım ise ücrete tabidir.

### Diğerleri

Web tarayıcı piyasasını NCC ve MS firmalarının egemenliklerine almış olmaları nedeniyle, piyasada başka tarayıcı bulunmadığını sananların sayısı az değil. Oysa piyasada, çoğu ücretsiz veya sınayıp da beğenenlerin yazarına az bir ücret ödedikleri paylaşım yazılımı türünden, 50’den fazla tarayıcı programı bulunmaktadır. Bu programların en yaygını, tarayıcı programının ilk mucidi NCSA’e ait Mosaic’tir. Spyglass firmasının Mosaic’i esas alan programı, halâ yaygın olarak kullanılmaktadır.

Web tasarımcısının NN ve IE’ın 3 ve 4’ncü sürümlerini bilgisayarlarında mutlaka bulundurması gerekir. Hazırlayacağınız bir HTML dosyasının, bu iki program ve onların farklı sürümleri tarafından nasıl yorumlandığını ve bu yorumun sizin oluşturmak istediğiniz görsel etkiye uygun olup olmadığını, sayfalarınız Internet’e veya intranet’e çıkmadan mutlaka incelemelisiniz. HTML’in 4’ncü sürümünde yer alan komut listesinin tümü halâ NN tarafından tanınmamaktadır. Böyle bir komuta sayfanızda yer vermeniz halinde, sayfanızı NN ile tarayacak ziyaretçilerin ekranlarında, sayfanız sizin istediğiniz biçimde yansıtılamaz.

Bir Web tasarımcısının mutlaka aşina olması gereken bir tarayıcı, HTTP, FTP ve HTML gibi Web’in protokol ve dillerini belirleyen, Evrensel Kaynak Belirleyici (URL) sistemini işleten, yani tüm dünyadaki Web adreslerini sağlayan ve bu listeyi üstlenici firmalar aracılığıyla hergün tüm dünyadaki Internet omurga işletmecilerine ulaştıran uluslararası kurum olan W3C’nin kendi tarayıcı programı olan Amaya’dır. Bu program, sadece Internet tarayıcı değil, aynı anda HTML sayfaları oluşturmakta da kullanabileceğiniz bir HTML editörüdür. Birden fazla HTML sayfasını açabilen, Internet’e bağlı iken bir yandan da sayfa tasarımına olanak veren Amaya, HTML’i, olduğu gibi anlayıp, ekranda gösteren tek tarayıcı programıdır. NN ve IE, HTML’e kendi yorumlarını katarken, Amaya, sayfalarınızın gerçek HTML değerlerini ekrana getirecektir. Bu program ücretsiz olarak [http://www.w3C.org](http://www.w3c.org/) adresinden indirilebilir. Bu programı edinmek, ve tasarlayacağınız Web sayfalarını bu programla sınamak, tasarımcı olarak sizi diğer tarayıcıların sayfanızı nasıl göstereceğini belirleme zorunluğundan kurtarmaz. Amaya, bir HTML sayfasının sınanacağı ilk tarayıcı olmalıdır. Ama tasarımcı olarak, sayfanızın NN veya IE’de “nasıl durduğunu” belirlemek zorundasınız. Ayrıca Amaya, HTML standardının parçası olmayan, NCC ve MS tarafından kendi tarayıcı programlarının bir ilave niteliği olarak ortaya attıkları Java, Javascript, VBScript gibi programları tanımamaktadır. HTML editörü olarak Amaya, bu alana yeni atılan bir tasarımcının HTML’i öğrenmesine ve uygulamasına olanak sağlamakla birlikte, çok yetenekli ve scripting pogramları oluşturabilen diğer editing programlarına oranla basit kalabilir.

### Yaygınlık Oranları

Internet’te [http://browserwatch.internet.com](http://browserwatch.internet.com/) adresinde bulabileceğiniz istatistikler, size tarayıcılar arasında hangi programın ne oranda rağbet gördüğünü söyleyecektir. Genel olarak ifade edersek, Netscape Navigator halâ tüm bilgisayarlarda (PC, UNIX bilgisayarları ve Macintosh) yarının biraz üzerinde bir paya sahip bulunuyor. IE ise, üçret bir sınırını aşmış durumda. Listenin geri kalan bölümünü, en genişi yüzde 2’lik bir pay olmak üzere, şu programlar paylaşıyorlar: Cyberdog, IBrowse, Opera-3.0, Lynx, Echo, CacheFlow-Cache, IBM WebExplorer, Opera-3.0, ve MacWeb.

### Yardımcı Programlar ve Ek Birimler

Internet tarayıcıları, sadece HTML kodları ile yazılmış metinleri okuyup anladıkları günleri çoktan geride bıraktılar. NN ve IE, artık bir çok grafik dosyasını okuyup, ekranda resmedebiliyorlar. Bu gelişmeye rağmen, Internet tarayıcının başlıca işi, hergün yeni bir türü ortaya çıkan ses, video ve diğer çoklu ortam dosyalarının, veritabanı veya muhasebe tablolarının hızlı gelişimine ayak uydurup, onları ekranda canlandırmak olmadığı için, tarayıcı programını yazan uzmanlar, bu gibi programlarının dışardan çalıştırılmasına olanak sağlarlar. Kullanıcı isterse tarayıcısına, Internet’te adının uzatması “.xls” olan bir dosya ile karşılaşınca, bunu ekranda göstermek için Microsoft Excel programını çalıştırmasını bildirebilir. Yardımcı programlara ve bunların gerektiği verileri sayfanıza koyarken, Internet tarayıcısına nasıl bildirimde bulunacağınıza ilerde döneceğiz.

Plug-In denilen ek birimler ise, tarayıcıya tamamen farklı bir programı açmak yerine, belirli bir tür dosya türünü ekranda canlandırabilme yeteneği kazandıran eklerdir. Tarayıcı program bilgisayara kurulurken bu ek birimler olmaksızın (ya da çok yaygın olanları ile) yüklenir. Internet’te yeni bir tür dosya türü oluşturmak isteyen, ya da mevcut türlerin Internet servisi sunan bilgisayardan (Server) müşteri bilgisayara aktarılmasında yeni bir yöntem geliştiren kişi veya firma, bu yeni dosya türünün tarayıcı tarafından bilgisayarda oluşturulabilmesi için bir de “plug-in” oluşturur ve bunu genellikle ücretsiz dağıtır.

Diyelim ki, bir firma, Internet’te ses naklini çok daha hızlı ve kolay hale getirdiğini düşündüğü yeni bir biçim geliştirdi. Bu biçimin Internet hizmeti verenler tarafından benimsenmesi ve yaygın olarak kullanılması, tarayıcı programların bu biçimi tanımasına, bu da firmanın yeni ses nakil yönteminin gerektirdiği plug-in programcıklarını etkin şekilde dağıtmasına bağlıdır. Kimi zaman bir yöntem o kadar beğenilir ve Internet hizmeti verenler tarafından tutulur ki, plug-in tarayıcı kullananların satın almak isteyecekleri bir program haline gelir. Çoğu zaman, tarayıcı için gerekli plug-in kullanıcılara ücretsiz ulaştırılırken, yeni yöntemi kullanarak Internet alanında sundukları içeriği daha etkin hale getirmek isteyenler için gerekli oluşturma programı parayla satılır. Bunun bir örneği Internet’te gerçek zamanlı ses aktarmakta kullanılan RealAudio ses kayıt ve saklama yöntemidir. Firma, ses dosyalarını bu yöntemle sıkıştırıp hızlı bir şekilde ulaştırmak isteyenlere kodlama ve bunu Server’a yerleştirerek, isteyen tarayıcıya aktaracak programı satarken, kendi tarayıcılarına RealAudio dosyalarını okuyarak, bilgisayarın ses kartını ve hoparlorunu kullanarak bu dosyayı sese çevirecek ek birimi ücretsiz dağıtmaktadır.

Web tasarımcısı, özellikle ses, video ve diğer grafik unsurların Server’dan müşteriye aktarılmasında ne gibi yöntemler olduğunu ve gelişmeleri izlemek zorundadır. HTML sayfanıza bir ses unsuru koymaya karar verdiğiniz zaman NN veya IE kullanan bir kişinin bunu bilgisayarında dinleyip-dinleyemeyeceğini de hesaba katmak zorundasınız. İlerde, Web tasarımında çoklu ortam unsurlarından söz ettiğimiz zaman, plug-in’lere döneceğiz.

### Java, ActiveX

Bu bölümü bitirmeden, HTML sayfalarınıza koyabileceğiniz ve HTML’i duraganlıktan kurtarıp, hareket ve hatta kullanıcı ile etkileşmeli hale getiren unsurlardan da kısaca söz edelim.

Java dili ile yazılmış programlar veya programcılar (Applet) ve Microsoft firmasının Windows ortamı için geliştirdiği ama zamanla diğer işletme sistemlerine de yayılan ActiveX Kontrolleri, tarayıcı programın yanı sıra, ama ondan bağımsız olarak, çalışan ve ortaya çıkarttıkları sonucu, programcığı veya Kontrol’ü yazan kişinin amacına bağlı olarak, ya tarayıcı içinde, ya da tarayıcı dışında ekrana getiren veya yapan unsurlardır. Hareketli Web sayfalarından ve Dinamik HTML’den söz ettiğimiz zaman bu iki unsuru daha geniş ele alacağız.

# Bölüm II: HTML’in Temel Unsurları

HTML sayfanın temel taşı nedir, diye sorarlarsa, çekinmeden “Metinlerdir,” diye cevap verebilirsiniz. Günümüzde birçok Internet alanında sayfalarında hiç yazı bulunmasa, sayfanın bütün içeriği sadece grafikten ibaret olsa ve HTML’den sadece grafik unsurları bir arada tutmak ve ziyaretçinin bilgisayarına aktarmak için yararlanılsa da, bütün grafik unsurların ziyaretçiyi götürüp bırakacağı son nokta, bir bilgi kümesidir, metindir. Bu bölümde HTML’in temel yapı unsuru olan metne nasıl yer verileceğini ve metnin nasıl biçimlendirileceğini ele alacağız. Bunu yapmak için de bir HTML sayfası oluşturacağız ve bunu beğendiğimiz bir tarayıcı ile açıp, bakacağız. Bu suretle Web tasarımının metinle ilgili araçlarını, metin şekillendirmek etiketlerini tanımış olacağız. Daha sonra HTML sayfa tasarımında kullanacağımız elemanları, stil sayfaları, tablo, ve çerçeve, grafik ve çoklu-ortam (multimedya) unsurlarını tanıyacağız.

### Etiketler (Tag)

HTML komutları içeren ve tayarıcıların tanıyabildiği dosya, aslında içinde ASCII karakterlerden başka unsur olmayan, düz yazı dosyalarıdır. Tarayıcıya, sayfayı ekranda oluştururken vermesini istediğimiz biçimle ilgili komutları bir dizi özel işaretleme etiketlerini kullanarak veririz. Başka bir deyişle, tarayıcı bir paragrafın, cümlenin, satırın, kelimenin ya da harfin önünde, onun ekranda nasıl gösterileceğine ilişkin etiketi görür ve bu etiketin gerektiği işlemi icra eder.

Siz, Web sayfasının mimarı olarak, Server’a koyacağınız HTML metninin içinde, bir anlamda, “Netscape veya Internet Explorer: Buraya bir etiket koyuyorum. Bu etiket, büyük başlık etiketidir. Ben sana bu etiketin kapsadığı kelimelerin bittiğini söyleyinceye kadar, vereceğim bütün kelimeleri büyük başlık olarak sun!” demiş oluyorsunuz. Dolayısyla, HTML’de ilke, önünde etiketi olmayan herhangi metne yer vermemektir. Önünde etiketi olmayan herhangi bir metin parçası, tarayıcı tarafından temel paragraf olarak nitelenir.

HTML, içinde kontrol kodu olmayan metin dosyasıdır. Bu, söz gelimi WordPerfect veya Microsoft Word ile yazdığınız ve uzatması “.wp” veya “.doc” olan bir isimle ve WordPerfect veya Word biçiminde kaydettirdiğiniz bir belge, HTML etiketleri içerse bile, HTML dosyası sayılamaz. Çünkü kelime-işlem programınız, bu dosyanın içinde kendi kontrol kodlarını koymuştur. Böyle bir dosyanın adındaki uzantıyı silerek, yerine “.htm” uzantısını verin ve tarayıcınıza açtırmaya kalkın!

/////////////KUTU///////////////////////

Düz Yazı Dosyası ve HTML

Düz yazı biçiminde kaydedilmemiş bir metni tarayıcıya açtırma denemesini, burada birlikte yapalım. Yandaki paragrafı içeren bir metni, örneğin HTML.DOC adıyla, Word dosyası olarak kaydedelim ve sabit diskte bu dosyayı bulup, adını “HTML.HTM” olarak değiştirilim. Bilgisayarlarımızda, “.htm” uzatması ile bağlantılı tarayıcı Netscape Navigator veya Internet Explorer olarak. Adını değiştirdiğimiz bu dosyayı iki kere tıkladığımızda, sistemin varsaydığı tarayıcı açılacak ve karşımıza şuna benzer bir tablo çıkacaktır:

\[reh000.tif\]

Bu kargaşanın nedeni, tarayıcı programın, uzantısı “.htm” veya “.html” olan bir dosyayı, içinde kontrol kodu olmayan, düz yazı dosyası sanması ve Word belgesindeki kontrol kodlarını da metin olarak ekranda göstermesidir. Belgemizin içinde hiç bir HTML etiketi yer almadığı için de, tarayıcımız bu yazıyı, düz paragram olarak gösteriyor. Aynı yazıyı, bu kez Word programına düz yazı olarak kaydettirelim. Word bu dosyaya, “HTML.txt” adını verecektir. Şimdi de bu dosyanın adını “HTML.htm” olarak değiştirelim ve iki kere tıklayalım. Tarayıcıda karşımıza şöyle bir görüntü çıkacaktır:

\[reh001.tif\]

Bu dosyanın içinde kelime işlemcinin kontrol kodları bulunmadığı ve dosyada metnin dışında başka bir unsur olmadığı için, tarayıcı metni yorumlamakta güçlük çekmeyecektir. Ne var ki, kelime-işlemci metni ASCII olarak kaydederken, metnin Türkçe karakterlerini en yakın ASCII koduna çevirdiği için, yazıdaki Türkçe harfleri kaybetmiş olduk.

Aynı paragrafı HTML dosyası olarak (ilerde değineceğimiz bir programın yardımıyla) ve sayfanın kodlama dili olarak Türkçe’yi seçerek kaydettiğimiz zaman, tarayıcımız, sayfayı hem kolayca açıp ekranda gösterebiliyor; hem de Türkçe karakterlerin kodları, tarayıcı tarafından tanınabiliyor:

\[html rehberi003.tif\]

////////////////////////////////////////////////////////

HTML düz yazı olduğuna göre, bir HTML dosyası oluşturmak için, tabii HTML kodlarını kendiniz yazacaksanız, herhangi bir kelime-işlem yazılımını kullanabilirsiniz, ama kaydettirirken “Sadece metin olarak,” “Text only,” “ASCII dosyası,” “ANSI Dosyası” gibi, programın kendi kontrol kodlarını koymayacağı bir biçim seçmek zorundasınız.

///////////////NOT/////////////////////////////

HTML mi, HTM mi?

Windows ortamında HTML etiketlerini kendiniz vererek HTML dosyası oluşturmak ya da bir HTML dosyasında değişiklikler ve düzeltmeler yapmak istiyorsanız, kullanabileceğiniz en uygun program Not Defteri‘dir (NotePad). DOS ortamında Edlin veya Edit, Macintosh’da ise SimpleText’i kullanabilirsiniz. HTML kodunuzu Microsoft Word, Corel WordPerfect veya beğendiğiniz herhangi bir kelime işlemcisi ile oluşturduğunuz taktirde, Dosya menüsünden Adıyla Kaydet maddesini seçin ve Biçim olarak Düz Yazı Olarak, ASCII Metin gibi bir biçimi seçin. HTML dosyalarının adlarının uzantısı, “.htm” veya “.html” olabilir. İşletme sisteminiz üç harften fazla uzatmaya izin vermiyorsa (DOS veya Windows 3.x gibi) “.htm”i tercih edin.

//////////////////////////////////////////////

İlerde, yaygın kelime işlem programlarının HTML yeteneklerinden ve yapacağınız sayfaların HTML kodunu otomatik olarak oluşturacak programlardan sözedeceğiz. Ama şimdi, herhangi bir kelime işlem programını açın ve aşağıdaki örneği birlikte yapalım:

HTML için markup (işaretleme) dili dediğimizi hatırlıyor olmalısınız. Yani, bir HTML dosyasında, Internet alanımızı ziyaret edecek kişinin bilgisayar ekranında belirlemesini istediğimiz metinlerimiz, grafik unsurlarımız ve diğerleri ile bunların nasıl belirmesini istiyorsak onu belirten **işaretlerimiz**. Bu işaretlere, **HTML etiketi **dediğimizi de hatırlıyor olmalısınız. HTML dosyası oluştururken, aslında yaptığımız iş, belirli metnin önüne, o metnin tarayıcı tarafından tanınacak ve gereği yapılacak bir etiket koymaktan ibaret. Tarayıcıya, etiketle, gerçek metni birbirinden ayırt etmesi için etiketlerimizi ‘küçüktür’ (<) ve ‘büyüktür’ (>) dediğimiz iki işaretin arasına alırız. Bu işaretlere, kimi İngilizce kaynaklardan doğrudan çevirerek ‘köşeli parantez’ dendiğine de tanık oluyoruz. Oysa köşeli parantez adını ‘\[‘ ve ‘\]’ işaretleri için kullanmak daha doğrudur. Sadece Web tarayıcınız değil, HTML dilini anlayan her program, bu işaretlerin arasındaki kelime veya kelimelerin ekranda gösterilmek üzere değil, gereği icra edilmek üzere verildiğini anlayacaktır. HTML’i geliştiren uzmanların etiket olarak üzerinde anlaştıkları kelimelerin büyük harfle veya küçük harfle yazılması arasında fark yoktur. Bir etiket kelimeyi büyük harfle de yazsanız, küçük harfle de yazsanız, hatta büyük harflerle küçük harfleri gelişi-güzel bile kullansanız, tarayıcı tarafından anlaşılacaktır. Bir başka deyişle, tarayıcı için “OKU” ile “Oku,” “oKu,” “okU” ve “oku” aynı emirlerdir.

Bir kaç istisnası dışında, bütün HTML etiketlerinin kapsadığı alanın bittiği aynı kelimenin önüne bölü işareti (/) konularak oluşturulan ikinci etiketle belirtilir. Yani, diyelim ki <Oku> komutuyla başlattığınız işi, </Oku> komutuyla bitirirsiniz.

/////////////////////////NOT////////////////////

Büyük Harf, Küçük Harf?

Oluşturacağınız Web sayfaları, ilerde bu görevi devralacak başkaları tarafından düzeltilebilir, değiştirilebilir, kısmen kullanılabilir. İyi bir mimarın planlarının başka bütün mimarlar tarafından hiç tereddütsüz anlaşılabileceği gibi, sizin sayfalarınızın da başka Web alan yöneticileri ya da sayfa tasarımcıları tarafından kolaylıkla **okunabilmesi** şarttır. Nasıl bir yöntem izlerseniz izleyin; ama bir alanda yer alan bütün sayfalarınızda aynı yöntemi izleyin: kodlarınız ya tümüyle büyük harf olsun, ya da tümüyle küçük harf. HTML tarayıcıların okuduğu ama gereğini yerine getirmediği yorum/açıklama tarzındaki etiketleri kullanarak, sayfalarınızın bölümlerinin insan gözüyle okunulup anlaşılabilmesini sağlayın.

/////////////////////////////////////////////////////////

### HTML Dosyasının Bölümleri

HTML dosyasının bir tarayıcı tarafından tanınması, yorumlanması ve gereğinin ekranda yapılabilmesi için, belgenin bir HTML belgesi olduğunun bildirilmesi şarttır. Bu bildirimi dosyanın tümünün etiketi anlamına gelen <HTML> etiketi, bir HTML belgesinin ilk kelimesi olarak yazılır. Tarayıcıya, HTML dosyasının bittiği de </HTML> etiketiyle bildirilir.

/////////////////////////////////////////NOT//////////

Açtığınızı Kapatmayı Unutmamak İçin

İyi bir tasarımcı olarak, HTML belgesini oluştururken, yazdığınız her etiketi bitiş etiketi ile birlikte yazın: <HTML></HTML> gibi. Sonra, iki etiketin arasına ilgili komutları ya da metinleri koyun.

//////////////////////////////////////////////////////////////

HTML belgesi, iki bölüme ayrılır: Baş taraf (başlangıç) (<HEAD>) ve gövde (<Body>) bölümleri. Web tarayıcılar, bir belgeyi sizin arzu ettiğiniz tarzda yorumlayabilmek için, HTML etiketini gördükten sonra derhal HEAD ve BODY etiketlerini arar ve ekrandaki sayfayı buna göre biçimlendirirler. Sayfanın “baş tarafı” sayfanın en üstünde, örneğin bir gazetenin başlığı gibi gösterilen bir metin olmayıp, ilerde ele alacağımız belge hakkında genel bilgileri kapsayan bölümdür. Burada yer alabilecek genel etiketleri (meta tag) ayrıntıları ile inceleyinceye ve ne işe yaradıklarını görünceye kadar, şimdilik örnek sayfalarımızda baş tarafı başlatan ve bitiren etiketleri koyup, aralarına, HTML sayfalarının İngilizce metinlerden oluştuğunu varsayan tarayıcıya, sayfamızın Türkçe olduğunu bildirmek için—şimdilik anlamının üzerinde durmadan—bir genel etiket koyacağız. Şimdi herhangi bir kelime işlemcisinde, örneğin Windows ortamında Not Defteri’nde, Macintosh’ta SimpleText’te şu örneği aynen yazın ve dosyayı düz yazı dosyası olarak kaydedin.

<HTML>

<HEAD>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</HEAD>

<BODY>

Web Tasarım Rehberi’ne Hoş Geldiniz!

</BODY>

</HTML>

Gördüğünüz gibi ilk HTML sayfamız, tarayıcıya bu dosyanın bir HTML dosyası olduğu beyanıyla başlıyor. İlerde anlamını öğrenmek üzere baş taraf etiketlerinin arasına sayfamızın Türkçe olduğunu belirten genel etiketi koyuyoruz; ve gövde bölümünde, ziyaretçilerimize hoşgeldiniz, diyoruz. Bu dosyayı, örneğin “hosgeld.htm” adıyla kaydedin. Kelime işlemcinizi kapatmayın; bir kenarda dursun. Kaydettiğiniz dosyanın simgesini bulunduğu yerde iki kere tıklayın; “.htm” uzantısı ile bağlantılı tarayıcınız hangisi ise, o açılarak, sayfayı yükleyecektir.

reh004.tif

//////////////////////NOT////////////////////

“Open” mı, “Browse” mı?

Internet Explorer’ın 4’ncü sürümünde programı başlattıktan sonra, Dosya (File) menüsünden Aç (Open) maddesini seçerek, ve açılacak diyalog kutusunda Araştır (Browse) düğmesine basarak oluşturduğunuz dosyayı bulabilirsiniz. Netscape Navigator’da ise yine File (Dosya) menüsünden Open Page (Sayfa Aç) maddesini seçerek, ve gelecek dilayog kutusunda Choose File (Dosya Seç) kutusunu tıklayarak oluşturduğunuz dosyayı arayabilir ve yükleyebilirsiniz. İşini kolaylaştırmak için, “.htm” ve “.html” uzantılarını en beğendiğiniz tarayıcı ile ilişkilendirirseniz, herhangi bir HTML dosyasını iki kere (Internet Explorer 4.x’ün masaüstü unsurlarını koymuş iseniz, bir kere) tıklayınca, tercih ettiğiniz tarayıcı dosyayı otomatik olarak açacaktır.

//////////////////////////////////////////////////////////

İlk HTML sayfanız şimdi karşınızda. HTML etiketleri arasına yazdığınız mesaj ekranda, tarayıcının varsayılan fontu ile ve yine varsayılan büyüklükte, gösteriliyor.

Şimdi, tarayıcının program adının yazılı olduğu üst çerçeveye dikkat edin: “F:\\hosgeld.htm – Microsoft Internet Explorer” ya da sadece “Netscape” kelimelerini göreceksiniz.

Şimdi, hala açıksa, “hosgeld.htm” dosyasını yazdığınız kelime işlemcisini ön plana getirin ve üçüncü satıra “<Web Tasarım Rehberi</TITLE>” kelimelerini yazın. Dosyanızın tümü şu şekli almış olacaktır:

<HTML>

<HEAD>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</HEAD>

<TITLE>Web Tasarım Rehberi</TITLE>

<BODY>

Web Tasarım Rehberi’ne Hoş Geldiniz!

</BODY>

</HTML>

Burada yaptığımız, sayfamıza bir başlık vermekten ibarettir. Title/Başlık etiketi, tarayıcıya, bu etiketin, programın adıyla birlikte, çerçevede gösterilmesi talimatını verecektir.

Şimdi bu sayfayı aynı isimle bir kere daha kaydedin; ve oluşan dosyayı iki kere tıklayın. Açılan tarayıcıya, en üstteki çerçevenin üzerindeki başlığı okuyun:

reh005.tif

Title/Başlık komutu, IE’de, dosya adı yerine sayfanıza verdiğiniz Benim Sayfam başlığının tarıyıcı programının adıyla birlikte, programın çerçevesinde gösterilmesini sağladı. Netscape de şimdi program başlığında sadece kendi adını değil, bizim sayfamızın başlığını da göstermektedir. Yani, Title komutu ile, HTML sayfamızın içinde bir iş yapmış olmuyoruz, sadece tarayıcıya, kendi başlık alanında sayfamızı bilgisayar kullanıcısına hangi başlıkla sunmasını istediğimi söylemiş oluyoruz.

////////////////////////////////////////NOT//////////

HTML Editörleri

HTML kodunu kendisi oluşturan ve tasarımcıya görsel araçlar kullanma imkanı veren bir çok program çıktı. Kısaca HTML editörü denen bu programların bir özelliği WYSIWYG imkanına sahip olmalarıdır. İngilizce “Ne Görüyorsan, Onu Alırsın” kelimelerinin başharflerinden oluşan bu terim, yaptığınız tasarımın ekranda nasıl görülüyorsa aynen o şekilde HTML dosyasına haline dönüştürüleceğini ifade ediyor. Bu tür programların bir özelliği, oluşturduğunuz sayfaya hemen “Untitled” (Başlıksız) başlığını vermektir. Sayfalarınızı böyle bir program yardımıyla oluşturuyorsanız, ilk işiniz sayfa özellikleri (Page Properties) kutusunu açıp, sayfanın başlığını vermek olmalıdır.

//////////////////////////////////////////////////////////

İlk HTML sayfamızı yazmış ve incelemiş olduk. Bundan sonrası, sayfalarımıza daha çok içerik koymak ve onları biçimlendirmekten ibaret. Bunun için ilk adım olarak Style Sheet (Stil Sayfaları) denilen, tarayıcıya toplu biçimlendirme komutları veren etiketleri inceleyeceğiz.

## Web Sayfasının Biçimlendirilmesi

Bir anlamda, HTML etiketlerinin yarısından fazlası metin biçimlerdirme komutlarıdır. Ama bu komutlar, HTML etiketlerini geliştirenlerle, ürettikleri tarayıcı programların bunları nasıl yorumlayacağına karar veren uzmanların belirlediği biçimlerden ibarettir. Örneğin, HTML, temel metin unsuru oharak paragraf (<p>..</p>) ve altı ayrı büyüklükte başlık (Heading) kodu içerir (H1, H2, H3, H4, H5, ve H6). Ne var ki, temel metin harfleri ile başlıkların gerçekten ne kadar büyük olacağına, tarayıcı program karar verir. Bir programda H1, 16 punto olabilir; bir diğerinde 14. Ayrıca kullanıcı, kendi tarayıcısında bazı seçenekleri değiştirmiş, varsayılan metin yazısı ölçüsünü azaltmış ya da arttırmış olabilir. Bu durumda, ölçüsünü göreceli olarak normal paragraf harfi büyüklüğünden alan diğer bütün başlıkların da ölçüsü değişecektir. Bu değişiklik, sizin sayfalarınızın kullanıcının ekranında arzu ettiğiniz görsel etkiyi oluşturacak şekilde canlandırılmasını önleyebilir. Ayrıca HTML etiketlerini benimseyip, kullanmak, tarayıcı programlarını üreten firmalara kalmış bir tutum olduğuna göre, bütün HTML etiketlerinden yazı biçimlendirmede yararlanamayabilirsiniz. Örneğin, metin biçimlendirmede kullanılan bir diğer, alıntıları belirten Q (quotation) etiketidir. Netscape, bu etiketi taşıyan metni sabit genişlikteki fonta çevirirken, Internet Explorer, bu etiketin sonucu olarak metinde hiç bir biçim değişikliği yapmayacaktır.

////////////////////////////////NOT////////////////////////////

Harf Genişliği

Eski daktilolarda, kağıdı hareket ettiren mekanizma, her harfin genişliğine göre farklı hareket edemediği için “i” harfi gibi sadece bir çizgiden olan harf de, içine üç adet “i” harfi alabilecek olan “m” harfi de aynı genişlikte bir alana yazılırdı. Zamanla dizgi makinalarının “akıllı” hale gelmeleri ile, her harf, “m” harfinin kaçta kaçı kadar bir alan kapladığına bakarak, farklı yere yazılır hale geldi. Harfleri büyüklüklerine göre göreli genişlikte olan fontlarla bütün harfleri aynı genişlikte olan fontların farkı buradan kaynaklanır. Günümüzde, eski daktilo metinlerin sağladığı görsel etkiyi sağlamak üzere, bilgisayar fontları arasında da her harfinin alanı eşit, fontlar var.

/////////////////////////////////////////////////////////

Ne var ki, HTML 4 ile, etkisi duragan ve niteliği bir anlamda kullanıyıca bağlı olan bu etiketleri kullanma yerine, artık her paragrafı, hen cümleyi, hatta her harfi arzu ettiğiniz gibi biçimlendirebilirsiniz. Artık duragan etiketleri de, tarayıcının değil, kendi ettiğiniz biçimde kullanma imkanınız var. Dahası, bir tek dosyada bir tek kelimeyi değiştirerek, yüzlerce sayfadan oluşan bir Internet alanınında söz gelimi bütün başlıkları maviden turuncuya çevirebilir; bütün alıntıları italikten siyah harfe, Times’dan Arial’a çevirebilirsiniz.

HTML sayfada metin stili dediğimiz zaman, metnin Internet alanımızı ziyaret eden kişinin bilgisayar ekranında hangi tür harfle (Arial, Times, Verdana, Helvetica, vd.), bu harfin normal türüyle mi, ya da siyah (bold) veya italik tarzıyla mı, hangi büyüklükte (12 punto, 18 punto, 24 punto), ve ne renk gösterileceğini, sayfanın ya da içinde bulunduğu tablo hücresinin sağına mı, soluna mı, ortasına mı bloklanacağını kasdediyoruz. HTML 4’de, metin stil unsurları arasında, geri plan rengi gibi, daha başka unsurlar da vardır. Bunları, daha sonra ele alacağız. Şimdi sadece sayfa tasarımında kullanabileceğimiz unsurlardan biri olarak, stillerin HTML sayfasında nasıl yer aldığına bakalım.

HTML 4, üç ayrı stil imkanına sahiptir. Bir paragrafın (paragraf, bir kelime, hatta bir harf bile olabilir), ya da bir paragrafın bir bölümünün stili, hemen önüne konulacak bir stil komutu ile belirlenebilir. Buna in-line (aynı satırda) biçimlendirme komutları denilir. Burada bu tür biçimlendirmeyi biraz ayrıntılı ele alacağız ve bir iki örnekle nasıl kullanıldığına değineceğiz. Diğer iki biçimlendirme yöntemi olan HTML sayfasının başlangıç bölümüne gömülmüş ve gövde bölümünden buraya atıf yapılan “Embedded” stil etiketleri ile HTML dosyasının tamamen dışında, dosya adı uzantısı “.css,” içeriği düz yazı dosyası biçiminde olan Cascading Style Sheets (Yığılma Stil Sayfaları) tarzındaki stil olanaklarını Dinamik HTML bölümünde ayrıntılı ele alacağız. Burada kısaca söz etmek gerekirse, Gömülmüş (Embedded) stil bölümü, biraz sonra ayrıntılı olarak ele alacağımız yerel biçimlerdirme kodlarını HTML dosyasının başlangıç bölümüne toplu halde koymaktan ibarettir. Böylece dosyanın gövde bölümünden toplu stil kodlarıyla tanımlanmış etiketleri kullanarak her seferinde yerel biçimlendirme kodları girmekten kurtulmuş oluruz, Ancak bu yöntemi uygulamak için, Internet alanınızdaki her sayfanın baş tarafına bu kodları girmek zorundasınız. Oysa toplu biçimlendirme kodlarınızı ayrı bir düz yazı dosyası halinde saklamanız ve Internet alanınızda yer vereceğiniz bütün sayfaları bu stil dosyası ile bağlantılandırmanız mümkündür. Buna bağlı (linked) stil dosyası denir. Bu yöntem, tasarımcıya bu dosyada yapacağı değişiklikle, bütün sayfalarda değişiklik yapma imkanı verir.

HTML 4’ün tanıdığı bu üç stil yöntemini kullanarak Web alanındaki bütün sayfalar baştan sona tutarlı bir görünüme kavuşabilir. Web tasarımcıları, stil belgeleri sayesinde, adeta gazete, dergi ve diğer basılı yayınları hazırlamakta kullanılar masaüstü yayıncılık programlarını kullananlara yakın bir tasarım esnekliği ve kalite düzeyine ulaşmış bulunuyorlar. HTML ile henüz herhangi bir masaüstü yayıncılık programında yapılan bütün tasarım incelikleri uygulanamaz; ama stil belgelerinin dikkatli ve titiz şekilde kullanan ve bu alandaki gelişmeleri takip eden bir tasarımcı, herhangi bir gazete sayfası tasarımcısını bile kıskandıracak sayfalar hazırlayabilir.

Stil etiketlerini yorumlama ve özellikle yukarıda değindiğimiz son iki yöntemin kullanılma açısından bütün tarayıcıların eşit düzeyde olmadığını söylememiz gerekir. Internet Explorer’ın 4’ncü sürümü HTML 4’ün bütün etiketlerini tanırken, Netscape’in 4’ncü sürümü HTML 3.2’nin etiketlerinin tümünü, HTML 4’ün de bir kısmını tanıyor. Web sayfasını tasarımcısı olarak, tarayıcıların hangi stil etiketlerini tanıdıklarını, hangisini tanımadıklarını izlemeniz ve sayfalarınızın bütün kullanıcıların bilgisayarında hemen hemen aynı tarzda gösterilmesini sağlamak için bunlardan hangisini kullanacağınıza, hangisini kullanmayacağınıza karar vermeniz gerekir. Başvuru bölümünde bazı etiketlerin tarayıcıların hangi sürümü tarafından tanındığına bakabilirsiniz.

Şimdi yerel biçimlendirme yöntemine ayrıntılı olarak bakalım.

### Yerel Biçimlendirme

Diyelim ki, Web’de sayfa tasarımı konularını bir araya getiren, karşınıza çıktığında beğendiğiniz sayfaların adreslerini, bir yerlerde okuduğunuz bir makalenin ana mesajını aktaran ve Web tasarımcılarının birbirleriyle fikir alışverişi yaptıkları bir Internet alanı oluşturmak istiyorsunuz. Sayfanıza şu metni koymak istiyorsunuz:

“Bizler, inandığımız için ve bilinçli olarak harf tasarımcısıyız, harf dökümcüsüyüz, sayfa dizgicisiyiz.. **Yoksa, yeteneğimiz daha yüksek şeyler için elverişsiz olduğu için değil**. Biz inanıyoruz ki, en yüksek düzeyde beceri gerektiren şey, bizim sanatımıza en yakın olanıdır.

Rudolf Koch - *Alman harf dökümcüsü, kaligraf*

Dikkat ederseniz, metinde bir cümle siyah harflerle dizilmiş ve kaynak italik harflerle gösterilmiş bulunuyor. Şimdi bu paragrafı, biraz önce oluşturduğumuz Hoşgeldiniz sayfasına alalım ve siyah harflerle italikleri oluşturmaya çalışalım. Yukarıdaki örnekte kaydettiğiniz HTML dosyasını açın ve “Benim Web Sayfama hoş geldiniz!” kelimelerini silip, yerine yukarıdaki paragrafı yazın:

Bitirdiğinizde ekranınızdaki HTML kodu şöyle olmalıdır:

<HTML>

<HEAD>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</HEAD>

<TITLE>Web Tasarım Rehberi</TITLE>

<BODY>

<p>“Bizler, inandığımız için ve bilinçli olarak harf tasarımcısıyız, harf dökümcüsüyüz, sayfa dizgicisiyiz.. <b>Yoksa, yeteneğimiz daha yüksek şeyler için elverişsiz olduğu için değil.</b> Biz inanıyoruz ki, en yüksek düzeyde beceri gerektiren şey, bizim sanatımıza en yakın olanıdır.</p>

<p>Rudolf Koch - <i>Alman harf dökümcüsü, kaligraf</i></p>

</BODY>

</HTML>

Burada paragraf etiketini kullandığımıza dikkat edin. <p>..</p> etiketleri, tarayıcıya, ana metin unsurunu verir. Tarayıcı bu etiketi gördüğü anda, takibeden unsuru (bu bir başka metin olabileceği gibi, bir grafik öge, veya tablo da olabilir) bir satır aşağıya ve yeni satırın en başına alır.

/////////////////////////////////NOT///////////////

Yeni Paragraf ile Yeni Satır’ın farkı.

</p> etiketi, tarayıcıya, yeni bir paragraf başlatmasını söyler. Buna karşılık, bir metinde bir satır, nerede bitiyorsa orada bitsin, takibeden satır yeni bir paragraf yapmadan, alttaki satırın başına gitsin isteyebilirsiniz. Bu iki durumun, yani yeni paragraf ile paragraf başlatmadan yeni satıra gitmenin farkı da mekanik daktilodan geliyor. Daktilo yazma kurallarından biri, yeni paragraf başlatırken, iki paragrafın arasında normal satır aralarına verdiğiniz boşluktan daha fazla boşluk vermekti. Diyelim satırlarınız tek aralıkla yazılıyorsa, paragraflarınızın arasında en az bir buçuk aralık olması gerekirdi. Ayrıca her yeni paragraf bir miktar içerden başlardı. Elektrikli daktiloların icadıyla, yazana kolaylık olması için mühendisler, yeni paragraf yapmayı ve sadece satır atlatmayı ayrı ayrı tuşlarla yapılır hale getirdiler. Bugün ENTER veya RETURN tuşu, kelime işlem programınızın varsayılan ayarlarına bağlı olarak, iki parafraf arasında arzu ettiğini bir miktar boşluk bırakır ve yeni paragrafı biraz içerden başlatır. Yeni paragrafın normal satır aralığından daha fazla boşluk bırakmadan ve birinci satırı içeri girmeden yazılmasını istiyorsanız, yine programına bağlı olarak, örneğin ENTER veya RETURN tuşuna basarken, CONTROL tuşunu da tutmanız gerekir. Internet’in ilk günlerinde, yazıların ekranda mümkün olduğunca kelime işlem programlarına benzer şekilde oluşturulması amacıyla </p> etiketine yeni paragraf başlatma, buna karşılık <BR> (line break) etiketine de sadece satır atlatma görevi verilmişti.

/////////////////////////////////////////

Paragraf etiketinin nasıl bloklanacağını ALIGN yüklemi belirlersiniz. Örneğin paragraf etiketini <p align=center> şeklinde kullanırsanız, </p> etiketine kadar gireceğiniz bütün metin, bulunduğu yerde ortalanacaktır. Paragraf etiketinin çeşitli kullanım özelliklerine aşağıda döneceğiz, Ama şimdi bu HTML sayfasını farklı bir isimle kaydedin ve kaydettiğiniz dosyayı tarayıcınızda açın. Bu paragraf, herhangi bir tarayıcının ekranında, şöyle gösterilecektir:

reh007.tif

Bu görünümü sağlayan HTML komutları, koyu renkli (matbaacılıktan kalma deyimle siyah harfler) için <B> (ve tabiî, bu etiketin etki alanının bittiğini belirten eşi </B>), italik için <I> (ve </I>) etiketleridir.

Aynı şekilde istersek. bir paragrafın veya bir bölümünün harf ailesini (fontunu) da değiştirebiliriz. Yukarıdaki örnekte, metnimizin tarayıcının ekranında nasıl gösterileceğini bilgisayar kullanıcısının seçtiği varsayılan fonta bırakıyoruz. Başka bir deyişle, sayfamızın tarayıcıda hangi temel harfle gösterileceğini biz tayin etmiyoruz, işi bir bakıma şansa bırakıyoruz. Oysa oluşturduğumuz Internet alanı edebiyatla ilgili olduğuna göre, harf ailesini, sanata biraz daha önem verecek şekilde biz seçebiliriz.

/////////////////////////////NOT////////////////////////

Internet’te Font meselesi

HTML sayfanızı tasarlarken, kendi bilgisayarınızda mevcut fontların, Internet alanınızı ziyaret edecek herhangi bir kişinin bilgisayarında mevcut olacağını varsaymanız hata olur. Bunun için hemen hemen bütün Windows ve Macintosh ortamlarında mevcut harf ailelelerinden ayrılmamanız gerekir. Netscape ve Internet Explorer programlarının yeni sürümleri, kurulurken, kullanıcının bilgisayarına Internet’in klasik fontları olmaya başlayan bazı harf ailelerini yüklüyorlar. İşletme sistemlerinin temel harfleri ile tarayıcıların eklediği harfler arasında seçim yaparak da görsel etkisi arzu ettiğinize yakın sayfalar tasarlamanız mümkün. Bir başlıkta, ya da bütün sayfalarınızda ortak bir logo’da mutlaka arzu ettiğiniz bir fontu kullanmak istiyorsanız, bu başlık ya da logoyu, grafik haline getirebileceğinizi unutmayın. Ama grafiklerin de sayfanızın ziyaretçinin bilgisayarına aktarılması süresini uzatacağını akıldan çıkartmayın. Metinlerinizi, sırf görsel etki için grafik halinde sunarsanız, bir süre sonra ziyaretçilerinizin beklemekten bıkıp, başka sayfalara gidebileceğini hatırlayın.

////////////////////////////////////////////////////////

/////////////////////NOT/////////////////////////

SERIF-SANS SERIF Harfler:

Latin alfabesine bugünkü biçimini veren eski Romalılardır. Harflerin kol ve bacaklarının ucunda, ana çizgiye dik gelecek kısa sonlardırma çizgisi olan serif’in ilk kez kağıt üzerinde mi, yoksa harfleri anıtlara oyan yontma ustalarının keskilerinden mi doğduğu bugün bile tartışmalıdır. Serif, daha sonra matbaacılıkta da çok iyşe yaramıştır. İlk yıllarda kağıt üzerinde harf şeklinde iz bırakan harf kalıpları çoğu zaman şimşir tahtasından oyularak yapılırdı. Bu kalıplara mürekkep sürülür ve üzerine konan kağıda basılırdı. Tıpkı lastik damga gibi! Ama tahta harf kalıplarının uçları çok çabuk aşınırdı. Aşınmanın uzun zaman alması için, zamanla harflerin kol ve bacaklarının çıkıntılı, yani serif yapılması gelenek oldu. Daha sonra, kurşun ve tunç gibi dayanıklı malzemeden harf kalıpları üretildiği zaman, çıkıntıları olmayan, sans-serif (serif’siz) harfler yaygınlaştı. Günümüzde de bilgisayar fontları, serif, sans serif ve dekoratif diye üçe ayrılıyor. Basılı eserlerde görsel etki, zıtlıklardan yararlanrak sağlanır. Bir sayfada yer alacak iki yazı unsuruna gerekli dikkati çekebilmek için bunlardan birinin serif, diğerinin sans serif harfle verilmesi yaygın bir uygulamadır. Ekranda zıtlıklar yoluyla dikkat çekebilmek için harf türünden başka şeyler, örneğin renk ve hareket unsuru da kullanabiliriz. Fakat matbaacılıktan kalma bir gelenekle, HTML tasarımcıları arasında başlıkla metni birbirinden serif-sans serif harflerle ayırmak giderek yaygınlaşıyor. Ekranda okuma kolaylığı açısından sans serif harfleri tercih edin. Özellikle küçük puntolu serif harflerin okunması çok zor olabilir.

//////////////////////////////////////////////////////////

Sayfamızda metinlerimizi Arial veya Helvetica; başlık ve kaynakları kaynağı da Times veya Times Roman ile gösterelim. Bunun için, HTML kodumuzda bir değişiklik yapmak zorundayız. Dosyamızın baş tarafına dokunmadan, paragrafın başladığı yere FONT etiketi koyalım. Bu etiketin parametreleri, başka bir ifadeyle, bu etikete niteliğini veren yüklemler, “face,” (font ailesinin adı), “size” (harfin büyüklüğü) ve “color” (harfin rengi) olarak sıralanır. Bu yüklemlerin nasıl kullanıldığını daha yakından görmek için, Başvuru bölümüne bakabilirsiniz. Biz burada sadece harfin türünü belirlemek istiyoruz; onun için sadece “face” yüklemini kullanacağız. HTML sayfasında paragraf etiketinden sonra <font face="Arial"> yazınız. Tabiî, bu etiketi sonlandıran, bitiren eşini ihmal etmeden! Kaynak cümlesi için aynı ifadeyi bu kez fontun adını değiştirerek yazacağız. Bitirdiğinizde, HTML kodunuzun paragraf bölümü şöyle olmalıdır:

<p><font face="Arial"> “Bizler, inandığımız için ve bilinçli olarak harf tasarımcısıyız, harf dökümcüsüyüz, sayfa dizgicisiyiz.. <b>Yoksa, yeteneğimiz daha yüksek şeyler için elverişsiz olduğu için değil.</b> Biz inanıyoruz ki, en yüksek düzeyde beceri gerektiren şey, bizim sanatımıza en yakın olanıdır..”</font></p><p><font face="Times New Roman">Rudolf Koch - <i>Alman harf dökümcüsü, kaligraf</i></font></p>

Bu sayfayı kaydedin ve kaydettiğiniz dosyayı, tarayıcınıza açtırın. Herşeyi doğru girdi iseniz, sayfanız şu sayfaya benzeyecektir:

reh008.tif

### Metin Düzenleme Etiketleri

Bu örneklerde HTML’in temel unsuru olan paragraf (<p>..</p>) etiketini kullandık ve çeşitli şekillerde biçimlendirdik. Ancak HTML paragraftan başka metin unsurlarını da tanır. Bu bölümde bu etiketleri ele alacağız.

HTML’in paragraftan sonra metne ilişkin en önemli yapı taşı, başlık etiketleridir. nitekim bizim yaptığımız örnek sayfanın da eksiği başlığının olmaması. Sayfamıza başlık koyşmadan önce HTML’in başlık etiketlerini daha yakından tanıyalım.

HTML bize H1, birinci yani en büyük, H6 sonuncu, yani en küçük olmak üzere altı ayrı büyüklükte başlık kullanma imkanı veriyor. Farklı başlık büyüklüklerini daha yakından tanımak için, şu sayfayı yazarak, örneğin baslik.htm adıyla kaydedin:

<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

<title>Başlıklar</title>

</head>

<body>

<p><font face="Arial">

<h1>H1: Bir numaralı başlık<h1>

<h2>H2: İki numaralı başlık<h2>

<h3>H3: Üç numaralı başlık<h3>

<h4>H4: Dört numaralı başlık<h4>

<h5>H5: Beş numaralı başlık<h5>

<h6>H6: Altı numaralı başlık<h6>

Normal Metin

</font> </p>

</body>

Bu dosyayı tarayıcınızda açın. Tarayıcınızın temel font ölçüsünü ortalamada tutuyorsanız, şuna benzer büyüklükler verir:

reh009.tif

Şimdi bu bilgiyle, örnek sayfamıza başlık verebiliriz. Bunun için, paragrafın hemen üstüne,

<h1>Tasarımcı kimdir?</h1>

<h2>Tasarım nedir? </h2>

satırlarını yazın ve sayfanızı kaydedin. Tarayıcıda açtığınız zaman sayfamızda iki başlık göreceksiniz.

reh010.tif

Paragraf etiketi gibi, başlık etiketinin de arkasına koyabileceğiniz tek özellik ALIGN’dır ve bununla başlığın sola, sağa, ortaya bloklanmasını veya sağ sol marjların aynı anda bloklanmasını sağlayabilirsiniz.

Yerel biçimlendirmede kullanabileceğimiz stil unsurları paragraf, başlık ve bunların <B>, <I> ve FONT etiketleri ile biçimlenmesinden ibaret değildir. Diğer temel biçimlendirme etiketlerini kısaca sıralayalım:

<BASEFONT>: Temel font etiketi, bir sayfadaki bütün metinlerin temel fontunu, tarayıcının varsayılan fontu ne olursa olsun, istediğiniz font ailesine (Helvetica, Times gibi) veya font türüne (serif, sans serif gibi) çevirmenizi ya da büyüklüğünü belirlemenizi sağlar. (Bu etiketin sonlandırıcı eşi, yani </BASEFONT> etiketi yoktur.)

<BIG>...</BIG>: İşaretlediği metnin temel fonttan bir ölçü büyük olmasını sağlar. Bu etiketi, aynı etiketin içinde tekrar kullanırsanız, en içerdeki font, temel fonttan iki ölçü büyük olacaktır.

Örnek: <p><font face="Times New Roman"><big>Rudolf Koch</big> - <i>Alman harf dökümcüsü, kaligraf</i></font></p

reh011.tif

<SMALL>...</SMALL>: İşaretlediği metnin temel fonttan bir ölçü küçük olmasını sağlar. Bu etiketi, aynı etiketin içinde tekrar kullanırsanız, en içerdeki font, temel fonttan iki ölçü küçük olacaktır.

Örnek: <p><font face="Times New Roman">Rudolf Koch - <small><i>Alman harf dökümcüsü, kaligraf</i></small></font></p>

reh013.tif

<CENTER>..</CENTER>: Ortalama etiketi, işaretlediği metnin, içinde bulunduğu kutuda (bu bir tablonun hücresi olabileceği gibi, sayfanın kendisi de olabilir) yatay olarak ortalanmasını sağlar.

Örnek: <p><center><font face="Times New Roman">Rudolf Koch - <i>Alman harf dökümcüsü, kaligraf</i></font></center></p>

reh014.tif

<S>..</S>: Ortasından Çizgi Çek (Strikethrough) etiketi, işaretlediği metnin ortasından çizgi çekilmesini sağlar. Bu etkiyi, bir metinden çıkartılmış yerleri göstermek için kullanabilirsiniz.

Örnek: <s> Biz inanıyoruz ki,</s> en yüksek düzeyde beceri gerektiren şey, bizim sanatımıza en yakın olanıdır..”

reh015.tif

<TT>..</TT>: Teleks Metni (Teletype Text) etiketi, işaretlediği metnin eşit genişlikte fontlarla (Courier gibi) gösterilmesini sağlar. Bu etkiyi, bir metinde örneğin bilgisayar kullanıcısının kendi yazması gereken bölümleri göstermekte kullanabilirsiniz.

Örnek: <p><font face="Arial">Programın <tt>kullanıcının adını</tt> soran diyalog kutusuna adınızı yazınız</font> </p>

reh016.tif

<U>..</U>: Altını Çiz (Underline) etiketi, işaretlediği metnin altına çizgi çekilmesini sağlar. Bu etkiyi, bir metinde vurgulamak istediğiniz bölümü göstermekte kullanabilirsiniz.

Örnek: <u>Biz inanıyoruz ki,</u> en yüksek düzeyde beceri gerektiren şey, bizim sanatımıza en yakın olanıdır..”

reh017.tif

<HR>: Yatay Çizgi (horizontal rule) etiketi, bulunduğu yerde, vereceğiniz yüklemlere göre yatay bir çizgi çizilmesini sağlar. Bu etiketin etkisinin bittiği yeri belirten eşi yoktur. Yatay çizginin yüklemleri arasında sağa, sola veya ortaya bloklanacağını gösteren ALIGN, gölgesiz olmasını sağlayan NOSHADE, pixel veya yüzde olarak kalınlığını belirleyen WIDTH vardır. Doğrudan betin biçimlendirmeye yaramamakla birlikte bu etiket, metnin bölümlerini ayırmakta kullanılabilir.

Örnek: <<HR><p><font face="Times New Roman">Rudolf Koch - <i>Alman harf dökümcüsü, kaligraf</i></font></p>

reh018.tif

HTML’in metin biçimlendirmekten çok metnin bölümlerini tanımlamakta kullanılan ve özellikle Internet’in metin ağırlıklı olduğu ilk dönemlerinden kalma, ACRONYM, BLOCKQUOTE, CITE, CODE, DEL, DFN, EM, INS, KBD, PRE, Q, SAMP, STRONG, SUB, SUP, VAR etiketlerini ve kullanıldıkları yerleri Başvuru bölümünde bulabilirsiniz.

Fakat burada kısaca da olsa, Internet giderek daha çok bilgi sunma ve bu bilgilerin bulunduğu yerleri gösteren bağlantıların listesi haline döndüğüne göre, listelerden söz etmek yerinde olacaktır. HTML bize birçok liste türü kullanma imkanı veriyor. Bunları sırayla inceleyelim ve uygulayalım.

Sıralı Listeler

<OL>..</OL>: Sıralı (Ordered) listeler, liste unsurlarının başına, tasarımcının arzusuna göre, ya rakam, ya harf koyarak, sıralanmış listelerdir. Listenin başladığını ve bittiğini belirten bu iki etiketin arasına liste unsurları (list item) <LI> etiketi ile yazılır. (Bu etiketin bittiğini gösteren eşi yoktur.) Etiketi biçimlendiren TYPE (1, rakamla; A, büyük harfle; a, küçük harfle; i küçük Romen rakamları ile; ve I, büyük Romen rakamları ile sıralanmayı sağlar), COMPACT, (listenin mümkün olduğu kadar az satır aralığı ile verilmesine yarar) ve START (listenin harfi harf veya rakamdan başlayacağını belirtir) şeklinde üç yüklemi olabilir.

Örnek sayfamıza, Web’de hemen herkesin tarayıcısının gösterebileceği güvenli renklere ilişkin bir sayfa koyalım. Akılda kolay kalması için kaç adet renk olduğunu belirtmek üzere, listemizde yer alacak unsurların rakamla veya harfle sıralanması uygun olur. Web Tasarım Rehberi sayfasının HTML kodunu açın ve mevcut paragrafı şöyle değiştirin:

<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

<title>Web Tasarım Rehberi - Renkler</title>

</head>

<body>

<p><font face="Arial">

<h1>HTML Sayfada Güvenli Renkler</h1>

<ol type=1 compact>

<li>#000000=black (Siyah)

<li>#000080=navy (Lacivert)

<li>#0000FF=blue (Mavi)

<li>#008000=green (Yeşil)

<li>#008080=teal (Koyu Yeşil)

<li>#00FF00=lime (Parlak Yeşil)

<li>#00FFFF=aqua (Turkuaz)

<li>#800000=maroon (Vişne çürüğü)

<li>#800080=purple (mor)

<li>#808000=olive (Zeytunî yeşil)

<li>#808080=gray (Gri)

<li>#C0C0C0=silver (Gümüşî gri)

<li>#FF0000=red (kırmızı)

<li>#FF00FF=fuchsia (Parlak pembe)

<li>#FFFF00=yellow (Sarı)

<li>#FFFFFF=white (Beyaz)

</ol>

</font> </p>

</body>

</html>

Herşeyi yolunda gitti ise, tarayıcınızda şu sayfa karşınıza çıkacaktır:

reh019.tif

Denemiş olmak için, liste etiketinde, TYPE yüklemini “1” değil, “a” olarak verin. Sayfadaki listeniz, bu kez rakamla değil, küçük harflerle sıralanmış olacaktır:

reh020.tif

(Bu liste “ç” ve “ı” gibi Türkçe harflerin olmadığını görüyorsunuz. Peki, listemiz çok unsur içerse, “z” harfinden sonra ne olur? İşte size güzel bir ev ödevi konusu!)

Sırasız Listeler

Sayfamızı tarayıcıda inceledikten sonra, aslında bu listenin rakam veya harfle sıralanmış olmasının istediğimiz görsel etkiyi yapmadığına karar verdik, diyelim. İstiyoruz ki listemizde, unsurların başına siyah, yuvarlak bir nokta gelsin. Bunun için, HTML’in sağladığı sıralanmamış liste etiketini kullanmak zorundayız.

<UL>..</UL>: Sırasız (Ordered) listeler, liste unsurlarının başına, tasarımcının arzusuna göre, ya içi dolu ya da içi boş bir yuvarlak, veya dört köşe nokta konularak sunulan listelerdir. Listenin başladığını ve bittiğini belirten bu iki etiketin arasına liste unsurları (list item) <LI> etiketi ile yazılır. (Bu etiketin bittiğini gösteren eşi yoktur.) Etiketi biçimlendiren TYPE (DISC, içi dolu daire; CIRCLE, içi boş daire; SQUARE dörtköşe nokta ile sıralanmayı sağlar) ve COMPACT, (listenin mümkün olduğu kadar az satır aralığı ile verilmesine yarar) şeklinde iki yüklemi olabilir.

Şimdi HTML kodumuzda gerekli değişikliği yapalım. Yani liste etiketini <UL></UL> olarak değiştirelim, TYPE yüklemini de DISC yapalım:

<ul type=disc compact>

Listemiz, tarayıcıda değişik bir görünüm alacaktır:

reh021.tif

Liste türünü diğer iki unsuru deneyerek, değiştirebilirsiniz.

Tanımlama Listeleri

HTML’in, Internet’in daha çok bilimadamlarının bilimsel rapor alışveriş alanı olduğu günlerde, sayfa tasarımcılarına kolaylık sağlamak üzere geliştirilmiş tanımlama listeleri üç gruba ayrılabilir.

<DL>..</DL>: Tanımlama (definition) listesi etiketinin içinde, tanımlamalara (<DD>), tanımlama terimlerine (<DT>) veya her ikisine birden yer verilir. DL etiketine sadece COMPACT yüklemi verilebilir. DD ve DT’nin sonlandıran eşi yoktur. Bu etiketlerle oluşturulacak listeleri de birer örnekle inceleyelim:

Diyelim ki Web tasarımını ciddî bir şekilde meslek olarak edinmek isteyenler için Web Tasarım rehberi sayfamızda bazı HTML işlemcilerin ve grafik programlarının tanıtımını yapalım. Tabiî önce bu programları gruplara ayıracağız. Dolayısıyla önce sayfamızı ziyaret edenlere, bu gruplarda ne tür programların yer aldığını anlatmak zorundayız. Başka bir deyişle tanımlama listemiz üç tanımlama terimi (<DT>) ve bunlara ait üç tanımlama (<DD>) içerecek. Buna göre, HTML kodumuzun liste bölümü şöyle olabilir:

<h1>Web Tasarımcısının Alet Çantası</h1>

<dl compact>

<dt>HTML İşlemciler

<dd>Tasarımcıya, program ekranında Web sayfasını bir kelime işlem veya masaüstü yayıncılık programı gibi hazırlama imkanı veren ve ortaya çıkan sayfayı HTML kodlarını koyarak kaydeden yazılımlar.

<dt>Grafik Programları

<dd>Mevcut grafik programlarından farklı olarak, Web için güvenli renklerle çalışan ve oluşturulan grafiği tarayıcıların tanıyabileceği biçimlerde kaydeden programlar.

<dt>Web Alanı Yönetim Programları

<dd>Web yöneticisinin kendi bilgisayarındaki sabit diskte oluşturacağı sayfaları, Internet Hizmet Sunucu firmanın bilgisayarına aktarma ve güncelleştirme imkanı veren programlar

</dl>

Bu kodun oluşturduğu tarayıcı sayfası ise şöyle görünecektir:

reh023.tif

Menüler

<MENU>..</MENU>: Tabiî burada kastedilen bir lokantanın menüsünden çok, tek kelime veya bir satıra sığabilecek uzunlukta, kısa ve çok az yer kaplayan listeler. Menü listeleri, diğer listelerden çok daha az satır yüksekliğine ve satır aralığına sahiptir.

Web tasarımcısının alet çantasında yer alması gereken programları kısa bir menü listesi olarak vermek istersek, HTML kodumuzun liste bölümününde şu değişikliği yapmak zorundayız:

<menu compact>

<li> HTML İşlemciler

<li> Grafik Programları

<li> Grafik Programları

</menu>

Bu şekilde değiştirdiğimiz sayfamız ise tarayıcıda şöyle görünecektir:

reh024.tif

Bu listenin kapladığı dikey alanın, aynı unsurları içeren sıralı ve sırasız listelere göre daha az, ya da daha çok yer kapladığını kolayca bulabilirsiniz. Ve bunu yaparken, listeler konusunu bir kere daha gözden geçirmiş olursunuz!

Liste etiketleri türlerini sayarken, özellikle dosya adı gibi bir dizin içindeki unsurların adını sıralayan <DIR>..</DIR> etiketinden de söz edelim. Bu etiketin içine de liste unsurlarını <LI> etiketi ile yazarız. Ortaya çıkacak liste, Menü ya da unsurları noktalı sırasız listeden farklı olmayacaktır.

Listelerden, yukarıda verdiğimiz örneklerde olduğu gibi bilgi sıralama amacının yanı sıra, liste başlıklarına veya unsurlarına başka sayfalarla bağlantı yaptırarak, çeşitli şekillerde yararlanabilirsiniz. Bağlantılar’ı ilerde ele alacağız.

Listeleri, madde başlarında kendi oluşturacağınız veya başka bir kaynaktan sağlayacağınız grafik unsurları kullanarak, güzelleştirebilirsiniz. Aşağıdaki örnekte, açık yeşil renkli küçük bir dikdörtgen nokta olan dot.jpg grafiğini kullanarak, program tanım listesini görsel açıdan zenginleştirelim. Bunun için, HTML kodumuzun liste bölümünde şu değişikliği yapacağız:

<dt><img src="dot.jpg">HTML İşlemciler

.......

<dt><img src="dot.jpg"> Grafik Programları

.......

<dt><img src="dot.jpg"> Grafik Programları

.......

Burada yaptığımız şey, <dt> etiketinden sonra bir grafik kaynağı (image source) etiketi koymak ve kaynak olarak sabit diskimizdeki grafik dosyasının adını vermekten ibaret. Siz kendi örneğinizde uygun bir başka grafik dosyasının adını verebilirsiniz. HTML sayfada grafik unsurlara nasıl yer verildiğini ve kurallarını ilerde ayrıntılı olarak ele alacağız. Bu noktada dikkat edeceğiniz tek şey, grafik dosyasının HTML dosyası ile aynı dizide durmasıdır. Daha sonra başka dizinlerdeki grafikleri sayfalarımıza alma yollarını gözden geçireceğiz. Bu kodun oluşturduğu sayfa ise tarayıcıda şöyle görünüyor:

reh025.tif

Listeler konusunu kapatırken, liste etiketlerini iç-içe kullanarak, farklı görsel etkiler oluşturabileceğimizi belirtelim. Örneğin, sırasız bir liste etiketinin içinde herhangi bir maddenin alt-maddelerini belirmek amacıyla, başka bir sırasız liste etiketi kullanabilirsiniz. Örneğin şöyle bir liste sunmak istiyorsunuz:

Madde 1

Madde 2

Madde 3

Madde 3-Paragraf A

Madde 3-Paragraf B

Madde 4

Madde 5

Madde 6

Bu etkiyi sağlayabilmek için, <UL>..</UL> etiketinin arasını şöyle doldurmanız gerekiyor:

<ul><li>Madde 1</li>

<li>Madde 2</li>

<li>Madde 3</li>

<ul><li>Madde 3 Paragraf A</li>

<li>Madde 3 Paragraf B</li></ul>

<li>Madde 4</li>

<li>Madde 5</li>

<li>Madde 6</li>

</ul>

Bu kod, tarayıcıda, şöyle görünüyor:

reh026.tif

Burada dikkat edeceğiniz nokta, iç içe açılan etiketlerin sıralı şekilde kapanması olmalıdır. Tabiî, bir süre sonra başınız dönmezse!

# Bölüm III: Tablo ve Çerçeveler ve Katmanlar

HTML sayfanın metinden sonra en önemli yapı taşları, tablolar ve çerçeveler olsa gerek. Bir HTML sayfasında hiç metne yer vermeyebilirsiniz. Tablolarınızda, çerçevelerinde ya da katmanlarınızda da yazı bulunmayabilir. Ama bu unsurlar, HTML’e henüz sahip olmadığı (örneğin, bir sayfanın sütunlara bölünmesi, yazı ya da grafik unsurların yer aldığı kutuların bir sayfada arzu ettiğiniz koordinatlarda sabit durması gibi) bazı sayfa tasarım araçlarını kazandırır. Tablo çerçevere ve katmanı, bir sayfanın iskeleti, ya da boş bir duvara yerleştirilen kitap raflarına benzetebilirsiniz. Kitaplarınızı kolayca alabileceğiniz bir düzende tutabilmek için, duvarın önüne raflar koymak, bu rafları bölmelere ayırmak gerekir. Aynı şekilde bir Web alanı da tarayıcı tarafından sol üst köşesinden başlanıp, sağ alt köşesine kadar doldurulması gereken bir sayfa gibi görülür. “Web sayfası,” “Ana sayfa” ya da “Home Page” gibi terimlerin kaynağı da, Internet’te alınıp-verilen “şey”in “sayfa” sayılmasıdır. Bu sayfa, yukarıdan aşağı doldurulması gereken bir alandır. Başka bir deyişle, bir unsur, bir diğer unsuru izleyerek sayfada yer alır. Bir duvarın tuğlayla örülmesi gibi. Ama bu duvar, sol üst köşeden, sağ alt köşeye doğru örülüyor! Ve tuğlaların arasında boşluk olamaz!

////////////////////////////////////NOT://///////////////////////

Bir Pixel Kaç Santim?

HTML sayfasının boyutları, sayfayı izleyen kişinin tarayıcısının ekrandaki penceresine bağımlıdır. Siz, sayfanızı kendi ekranınızda istediğiniz kadar geniş, istediğiniz kadar dar oluşturun: sayfanızın alacağı nihai ölçü, izleyen kişinin ekranının kaç inçlik olduğu, ve tarayıcısına ekranında ne kadar genişlikte bir pencere verdiği olacaktır. Windows ortamında buna bir de ekran-grafik kartı kombinasyonunun sisteme verdiği çözünürlük ölçüsü eklenecektir. Ekran ve kullanıcının tarayıcısının penceresine verdiği yer ne kadar büyükse, Web sayfasına o kadar çok unsur sığacaktır. Ancak ekranın çözünürlük oranı bu dengesi değiştirebilir. Grafik kartının çözünürlük oranı ne kadar yüksekse, ekrana o kadar çok şey sığar, ve sığan şeyler o kadar küçük görünür. Bu değişkenler yüzünden herrhangi bir kullanıcının ekranında sizin sayfanızın ne ölçüde gösterileceğini hiç bir zaman bilemezseniz. Bu nedenle, Web tasarımında standart, sayfanın 14 inçlik ekranda, 640’a 480 pixel (pixel=ekranda oluşan görüntünün bir hücresi, görüntünün bir noktası) çözünürlükte bir kart kullanan kişinin tarayıcısına azani genişliğine çıkartığı varsayılarak ve bundan tarayıcı programın kendi çerçevesi, menü alanı, simgeleri gibi sabit unsurlarının kapladığı alan düşülerek bulunan 600’e 350 pixellik alandır. Sayfanızı sadece ekranda izlenmek üzere tasarlıyorsanız, sayfa genişliğiniz eni 600, yüksekliği 350 pixel olmalıdır. Sayfanızı basılmak üzere tasarlıyorsanız, sayfanızın eni 569, boyu 672 pixel olmalıdır. Bu standartın belirlenmesinde ilke, hiç bir ziyaretçinin sayfanızın sağını veya solunu görebilmek için tarayıcı ekranında fareyle kaydırma çubuklarına basmak zorunda kalmasını ve bir sayfayı yazıcıya gönderdiği zaman bir satırın yarısının ya da bir grafik unsurun bir bölümünün ikinci sayfaya basılmasını önlemektir.

//////////////////////////////////////////////////////////

O halde HTML sayfasını, sol üst köşede (sayfa koordinatı olarak ifade edersek, 0,0 pixel noktasında) başlayan ve sağ alt köşede (600,350 pixel noktasında) sona eren bir duvar gibi düşmek zorundayız. Diyelim ki, ikinci bölümde yaptığınız ilk HTML sayfasına koyduğunuz, “Benim Web sayfama hoş geldiniz!” yazısının, sayfanın tam orta yerinde, 300,175px noktasına ortalanarak, yer almasını. Bunu sağlayabilmek için, “Benim” kelimesinin önünde aşağı yukarı, 640 adet aralık ya da Web diliyle “&nbsp;” (non-breaking space) kodu girmeniz gerekir. Üstelik, elde ettiğiniz sayfada başlık kullanıcının tarayıcısına verdiği alana göre, ya ortaya gelebilir, veya gelmeyebilir.

elle verilmiş boşluk örneği .. uygun : reh027.tif

elle verilmiş boşluk örneği .. bozuk: reh028.tif

Oysa, tablo, çerçeve veya katman unsurlarından birini kullanarak, ve aralık vermek gibi zahmetli ve bir anlamda amatörce yöntemlere başvurmadan bu başlığın, tarayıcının ekranı ne boyutta olursa olsun sayfanın tam ortasında gösterilmesini sağlamak elinizdedir.

mükemmel örnek: reh029.tif

Bu üç yapı taşının, sayfa biçimlerdirmeden başka işlevleri de vardır. Tablo, adı üstünde, bilginin sınıflandırılarak ve kolay anlaşılır tarzda sunulmasını sağlar. Çerçeveler, ziyaretçiye sunacağınız unsurların belirli bir tertip içinde sunulmasını, ziyaretçilerin alanınızda istediği yerlere zahmetsizce girmesine imkan veren bir tasarım ögesidir. Katman (layer) ise, duragan HTML’i, dinamik HTML haline getiren en kullanışlı unsurdur.

Bu bölümde, sırasıyla bu üç unsuru kullanmayı öğreneceğiz.

## Tablolar

Tablolar, Web sayfalarında verilerin sınıflandırılmış ve sıralanmış olarak sunulmasını sağlayan sütunlar ve sıralardan ibarettir. HTML’de dil olarak sağlanan gelişmeye rağmen, bütün ziyaretçilerin tarayıcıların en son ve en gelişmiş sürümlerini kullanmadıklarını, eski sürüm tarayıcıların ise HTML’in metinlerin sabit yerlere konulmasına imkan veren etiketlerini anlamamaları sonucu, sayfalarınız bir ekranda başka, bir diğerinde daha başka gösterilebilir. Bunu önlemek ve sayfalarınızı tarayıcıdan tarayıcıya değişmeyecek bir isketelete kavuşturmak için, tablolardan yararlanabilirsiniz. Bu imkan, tabloların verileri sütunlar ve sıralar halinde sunmaktan çok yapısal unsur olarak kullanılmasına yol açtı.

Yine de önce tabloların veri sunmakta kullanılmasını dikkate alarak, tablo kurallarından kısaca söz edelim. Tablolar, satırlardan ve sütunlardan oluşur. Satırlar, genellikle hakkında bilgi verilen unsurları (birimleri, bireyleri) içerir; sütunlarda ise bu birimlerin çeşitli değişkenlere göre hangi değeri aldığı gösterilir. Her tablonun genel bir başlığı olduğu gibi, her sütunun hangi bilgileri içerdiğini gösteren kendi başlıkları bulunur. Tablonun, üstte başlığın altında veya son sıradan ve varsa tablo çerçevesinden sonra bir açıklama yazısı (Caption) bulunabilir. Tablonun birden fazla sayfaya bölünmesi halinde, başlığın ve sütun başlıklarının tablonun devam bölümünün de üstünde bulunması gerekir. Tablonun devam bölümlerinin açıklama yazısında bir tablonun devamı olduğu belirtilir.

### Başlık, Satır ve Veri Etiketleri

HTML’de bir tablonun başlangıcı ve bitişi <TABLE>..</TABLE> etiketiyle işaretlenir. Tablonun sütun başlıkları <TH>..</TH>; gövdesi <TBODY>..</TBODY> etiketiyle belirtilir. Sütun başlıkları veya gövde etiketinin hemen altında tarayıcıya bir tablo satırı başladığını söylemeniz gerekir. Bunu <TR>..</TR> etiketiyle yaparız. Bu iki etiketin arasında Tablonun değerleri, yani içinde bilgiler bulunan hücreleri oluşturan etiket, <TD>..</TD> yer alır. Bu iki etiketin arasında tablonuzun ilgili hücresinde yer alacak bilgi bulunur.

Bu bilgileri hemen bir tabloya uygulayalım. En beğendiğiniz düz yazı dosyasını açın ve şu kodları girin:

<HTML>

<HEAD>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</HEAD>

<TITLE>Tablonun Esaslari</TITLE>

<BODY>

<p><font face="Arial">

<h1><center>HTML'de Tablo</center></h1>

<table align=center border=3 width=70%>

<caption align=bottom>Bu tablomuzun Alt-yazısı (caption)</caption>

<thead align=center>Bu tablomuzun Başlığı (thead)</thead>

<thead><tr><th>Birinci sütun başlığı (th)</th><th>İkinci sütun başlığı(th)</th><th>Üçüncü sütun başlığı(th)</th><th>Dördüncü sütun başlığı(th)</th><th>

<tbody>

<tr><td>Satır 1 Sütun 1</td><td>Satır 1 Sütun 2</td><td>Satır 1 Sütun 3</td><td>Satır 1 Sütun 4</td></tr>

<tr><td>Satır 2 Sütun 1</td><td>Satır 2 Sütun 2</td><td>Satır 2 Sütun 3</td><td>Satır 2 Sütun 4</td></tr>

<tr><td>Satır 3 Sütun 1</td><td>Satır 3 Sütun 2</td><td>Satır 3 Sütun 3</td><td>Satır 3 Sütun 4</td></tr>

<tr><td>Satır 4 Sütun 1</td><td>Satır 4 Sütun 2</td><td>Satır 4 Sütun 3</td><td>Satır 4 Sütun 4</td></tr>

</tbody>

</table>

</body>

</html>

Bu kod, tarayıcınızda, şöyle bir tablo oluşturacaktır:

reh030.tif

/////////////////////////////////////NOT//////////////

Açtığınızı Kapatın!

Düz yazı programlarıyla HTML kodu yazmak zevkli, fakat biraz dikkat isteyen bir iştir. Özellikle kapatan eşi olan etiketlerle eşsiz etiketleri öğrenmek kolay değil. Ama bunu kolaylaştıracak bir ilke var: İlk açılan son kapanır! Diyelim önce bir TR, onun içinde de içinde bir TD etiketi açtınız; TD’yi kapatmadan TR’yi kapatmayın. Daha kestirme bir yol, biraz önce oluştrduğunuz Tablo kodunu, daha sonra uygun yerde kullanmak üzere bir yerde saklayın. İhtiyacınız olmayan TR’leri ve tabiî içindeki TD’leri atarak veya ihtiyacınız olan TR’leri ekleyerek, yazacağınız HTML dosyalarının içine kopya edebilirsiniz!

/////////////////////////////////////////////////////////

### Tablo Unsurlarının Kontrolü

Bloklama: HTML’de tablonun kendisi ve içindeki bir çok unsur, (örneğin TH etiketiyle verdiğiniz sütun başlıkları, TD ile verdiğiniz hücrelerde yer alacak değerler ve CAPTION ile verdiğiniz tabloyu açıklayan alt-yazı) bulundukları yerde sola, ortaya veya sağa bloklanabilirler. Bunun için etiketten sonra “ALIGN=xx” yazmanız gerekir. “xx” yerine sağ için RIGHT, sol için LEFT, orta için CENTER, iki tarafının da bloklanması için JUSTIFY, veya herhangi bir karakterin ortalama unsuru olması için o karakteri yazmanız gerekir. Bu sonuncu olanaktan, tabloda rakam yer alacaksa ve bütün rakamlar nokta veya virgülleri altalta gelecek şekilde sıralansın istiyorsanız, yararlanabilirsiniz. Alt-yazı diye adlandırmış olmamıza rağmen CAPTION sadece bulunduğu yerde bloklanmakla kalmaz, istenirse tablonun üstüne veya altına alınabilir (ALIGN=LEFT/RIGHT/TOP/BOTTOM).

Sütun ve Satır Birleştirme: Bir tablonun başlığında ve gövdesinde yer alan hücreler yatak ve dikey olarak komşuları ile birleştirilebilirler. Bunun için COLSPAN ve ROWSPAN etiketlerini kullanırız. Bu olanaktan, sadece veri sunmak için oluşturacağınız tablolarda gruplanabilir sütunları en üstteki başlık hücrelerini birleştirerek, görsel bir birlik sağlamak için yararlanabilirsiniz. Fakat bu iki etiket, HTML’i, masaüstü yayıncılık programları ile yarışabilir yapısal özelliklere sahip sayfalar oluşturmakta yararlanacağımız iki ana araçtır. Aşağıda, tablolardan yapısal unsur olarak yararlanma yollarını ele aldığımızda bu iki etiket üzerinde çok duracağız.

Zemin: Bir tablonun, her bir satırın, her bir sütunun ve her bir hücrenin ortak veya ayrı zemini olabilir. Bu zemin düz renk olabileceği gibi bir grafik unsur da olabilir. Bu olanaktan, uzun ve çoğu zaman gözle takibi zor rakamlar içeren tablolar oluşturduğunuz zaman, satırlara biri açık, diğeri renkli zemin vererek, izleme kolaylığı sağlamak için yararlanabilirsiniz. Fakat bu etiketi de, sayfalarda içerik aracı olmaktan çok yapısal unsur olarak kullanacağız.

Tablonun genişliği: Bir tablo, tarayıcının tüm sayfasına yayılabileceği gibi, tasarımcının arzu ettiği bir yüzdesinde veya belirli ölçülerde de oluşturulabilir. Bunun için tabloyu başlattığınız yerde TABLE etiketine ölçü birimi ve miktarını eklemeniz gerekir. Örneğin, <TABLE WIDTH=70%> etiketi, tablonun eninin kullanıcının tarayıcı penceresinin yüzde 70’i kadar olmasını sağlar. Yüzde yerine pixel olarak mutlak ölçü de verebilirsiniz: WIDTH=200px gibi.

Tablonun Çerçevesi: Bir tablonun bütün sütun ve satırları içine alan en dış çerçevesinin kalınlığını belirlemek tasarımcının elindedir. Bunun için TABLE etiketi ile birlikte BORDER=xx (xx, pixel cinsinden çerçeve kalınlığı) yazacaksınız. “FRAME=x” ile tablonun dış ve hücreler arası çerçeve çizgilerini kontrol edebilirsiniz. “x” yerine VOID yazarak bütün dış çerçeveyi kaldırabilirsiniz; ABOVE sadece tablonun üst tarafına; BELOW sadece alt tarafına; HSIDES sadece alt ve üst taraflara; LHS sadece sol tarafa, RHS sadece sağ tarafa, VSIDES sadece sağ ve sol taraflara çerçeveye konulmasını sağlar. RULES=x ile iç çerçeveleri kontrol edebilirsiniz. x yerine NONE yazarak bütün iç çerçeveleri kaldırabileceğiniz gibi, GROUPS yazarak sadece başlık ve gövde grupları arasına, COLS yazarak sadece sütunların arasında, ROWS yazarak sadece satırların arasına çerçevere koyabilirsiniz. Bir tablonun hücreleri arasındaki mesafe CELLSPACING=x olarak verilebilir. burada x yerine pixel cinsinden mesafe ölçüsünü yazacaksınız. Hücrelerin içindeki yazı veya grafik gibi unsurların hücrenin iç çizgisine ne kadar yaklaşacağı, ya da başka bir deyişle, hücre içi marj, CELLPADDING=x ile verilebilir. yine, x yerine, pixel olarak arzu ettiğiniz ölçüyü verebilirsiniz.

Diğer tablo kontrol araçları: HTML 4 ile, tablolara, bilgisayarda görme özürlüler için ekrandaki unsurları okuyarak sese çeviren program varsa, tablonun yatay ve dikey unsur başlıklarını seslendirmeye yarayan AXIS ve AXES etiketlerinden tutun, sütunları veya satırları gruplayama, her bir gruba diğerinden farklı özellikler vermeye yarayan yeni yeni özellikler kazandırılmış bulunuyor. Bu özellikleri Başvuru bölümünde okuyarak ve ayrıntılarını uygulayarak bulabilirsiniz.

Şimdi tablodan sayfaya şekil kazandırma unsuru olarak nasıl yararlanacağımıza dönelim.

### İskelet Malzemesi Olarak Tablo

Önce bu sayfaya bir bakın ve bu sayfanın temel ögesinin ne olduğunu anlamaya çalışın:

reh031.tif (veya reh031bw.tif)

Tahmin ettiğiniz gibi, sayfanın temeli, bir tablodan ibaret.

Tablodan sayfanızın iskeleti olarak yararlanmak istediğiniz zaman, kurguya, en içerden başlamanız yararlı olur: Boş bir kağıda yan yana gelecek kutuları çizin; bu kutuların hepsi aynı sırada ve aynı sütunda olması gerekmez; tersine, sayfanın temeli olan kutuların mümkün olduğunda “kaybolması” için bazı tablo hücrelerinin sağlarında, sollarında, altlarında ve üstlerindeki hücrelerle birleşmesi gerekir. Bunu yapabilmek için tablonun temel kuralını hatırlayarak işe başlayalım:

TABLE etiketi ve ilgili yüklemlerinden sonra:

Önce tablonun birinci sırasını başlatın: <TR>

Sonra bu satıra kaç hücre koyacaksanız o kadar hücre koyun. Diyelim ki üç hücre koyacağız: <TD>&nbsp;</TD><TD>&nbsp;</TD><TD>&nbsp;</TD>. (Burada “&nbsp;” şeklinde gösterdiğimiz bir harflik aralık, hücrenin içine hiç bir şey konmadan da tarayıcı tarafından görülmesini sağlamak içindir. Bazı tarayıcılar içinde hiç bir şey olmayan hücreleri görmezler! sonra bunları silip, yerlerine hücrenin asıl malzemesini koyacağız. Bunu silmeyi unutsanız bile, tablonuza zarar vermeyecektir.) Sonra satırı kapatın: </TR>

İkinci sırada, diyelim ki iki hücre olacak. Birinci ve ikinci hücreler birleşecek; üçüncü hücre yerinde duracak. Sırayı başlatalım: <TR>. Birleşik birinci ve ikinci hücreleri açalım: <TD COLSPAN=2>&nbsp;</TD>. Üçüncü hücreyi koyalım: <TD>&nbsp;</TD>. Ve bu sırayı da kapatalım: </TR>

Diyelim ki üçüncü sıranın birinci hücresi ile dördüncü sıranın birinci hücresini birleştireceğiz. İkinci ve üçüncü hücreler ayrı ayrı kalacaklar:

<TR><TD ROWSPAN=2>&nbsp;</TD><TD>&nbsp;</TD><TD>&nbsp;</TD></TR>.

Üçüncü ve son sıranın birinci hücresini, bir üstündeki hücre aldığına göre, bu sıraya kaç hücre koymamız gerek? Evet, bu sıraya 2 hücre koyacağız. Ama istiyoruz ki bu iki hücre de birbiriyle birleşsin: <TR><TD COLSPAN=2></TD></TR>

Bu kadar! Şimdi bu dosyayı saklayalım ve tarayıcıda bir bakalım. Bu arada daha sonra kullanım kolaylığı için aralıkların yerine hücrelerin adını yazabiliriz. Tabloyla ilgili HTML kodlarımız toplu olarak şöyle:

<table border="1" width="75%">

<tr>

<td>Kutu 1</td>

<td>Kutu 2</td>

<td>Kutu 3</td>

</tr>

<tr>

<td colspan="2">Kutu 4</td>

<td>Kutu 5</td>

</tr>

<tr>

<td rowspan="2">Kutu 6</td>

<td>Kutu 7</td>

<td>Kutu 8</td>

</tr>

<tr>

<td colspan="2">Kutu 9</td>

</tr>

</table>

Bu kodun oluşturduğu içi boş tablo ise şöyle görünüyor:

reh034.tif

Şimdi burada ilkemizi bir kere daha tekrarlayalım: Tablo, içindeki satır ve sütunların kesişmesi demek olan hücrelerden oluşur. Hücreleri yukarıdan aşağıya, soldan sağa doğru birleştirebilirsiniz. Bir tablonun doğru oluşması için, birleştirdiğiniz ve birleştirmediğiniz bütün hücrelerin sayısının, tabloda olması gereken hücre sayısını tutması gerek. Tutmazsa ne olur? Tabloda kullanılabilecek bir hücreden mahrum olursunuz! Tabiatıyla, dünyaya hiç bir şey olmaz!

Peki, bu tablocuk, bizim sayfamıza nasıl iskelet olacak? İçi doldurularak! Bu hücreleri, bir gazete veya dergi sayfasının sütunları gibi düşünün. Kimi kutuya grafik unsur koyacağız; kimine metin. Hatta, bir tablonun bir hücresine, ikinci bir tablo bile konabilir! Birinci tabloyu sayfanızın ana iskeleti olarak düşünürseniz, bu iskeletin bir yerinde, içine çeşitli verileri koyduğunuz bir tablo bulunabilir.

Şimdi, küçük tablomuzu renklendirerek işe başlayalım:

Kutu 1’i oluşturan TD’nin zemin rengini bir tür yeşile çevirin:

<td bgcolor="#CC9999>Kutu 1</td>

Aynı şekilde, Kutu 2’yi, #FFCC99; Kutu 3’ü #CCCCCC; Kutu 4’ü #FF9966 yapın. Diğer kutulara da kendiniz renk verin. Bu arada ilk liste örneğimizi hatırlıyor musunuz?

////////////////////////////NOT///////////////////

Renk Şifresini Çözdünüz mü?

Web tarayıcılar renk komutunu, ya İngilizce kelime olarak ya da kod olarak kabul ederler. Bu karışık gibi görünün renk kodu, aslında, 16 tabancı sayı sistemiyle, yani Hexadecimal sistemle (Sayı sistemini 1’den 10’a kadar ondalık sistem olarak değil, 1’den 16’ya kadar 16’lık bir sistem olarak; 0’dan sonraki altı sayıyı da A, B, C, D, E, F olarak ifade ettiğimizi düşünün. Yani “11” yerine “1A” yazacaksınız. Tabiî, bu sistemde bir rakamı yazmak için iki basamağa ihtiyacınız var) Kırmızı, Yeşil ve Mavi renklerin ifadesinden ibarettir. Bilgisayar ekranı, bir katod tüpü olduğuna göre, renk sistemi, tıpkı televizyon ekranları gibi RGB (Kırmızı-YeşilMavi) renklerin üstüste düşürülerek diğer renklerin elde edilmesine dayanır. Altı haneli renk kodu, bilgisayar ekranına arzu ettiğimiz rengin kırmızı, yeşil ve mavi renklerin ne oranda karıştırılarak elde edileceğini söylemektedir. İki haneli renk oranları ise bilgisayara, “00” ise o renkten yüzde sıfır oranında, “FF” ise yüzde 100 oranında karıştırılmasını söylüyor. Bilgisayar ve televizyon ekranında beyaz renk, her üç rengin de yüzde yüz oranında olması halinde, siyah ise her üç rengin de yüzde sıfır oranında olmasıyla sağlandığına göre #000000 Siyah, #FFFFFF ise Beyaz anlamına geliyor. Web tarayıcıları her rengi göstermezler; her türlü tasarım projesinde olduğu gibi, Web tasarımında da renk en önemli yapı taşlarından biridir. Bunun nedenle grafik tasarımcılar için renklerin etkileri ve kullanma kuralları ile ilgili kaynaklara bakmanız yerinde olur. Web’de güvenli renk konusunda iyi bir kaynak, http://www.slip.net/~kiss/software/html\_colors adresinde bulunabilir.

//////////////////////////////////////////////////

Kutularımızı renklendirdiğimize göre, şimdi de içine koyacağımız yazıların bloklanma durumlarını farklı hale getirelim. Soldaki kutulara koyacağımız yazılar sola, ortadaki kutularda ortaya, sağdaki kutularda sağa bloklarsak, görsel etki açısından kutularımız bir ölçüde gazete-dergi sütunu görünümü kazanabilir. Ama tabiî bu, tamamen sizin kendi tasarım zevkinize bağlı. Kutuların içeriğini istediğiniz tarafa bloklayabilirsiniz. Önemli olan bunu bir kere denemiş olmak.

Bu noktada, kısaca tartışmamız gereken bir görsel unsur, hücrelerin ve tablonun tümünün çerçeveleri olup-olmamasıdır. Kimi tasarımcı bu çizgilerin tablo ile elde edilmek istenen etkiyi yok ettiğini düşünür; kimi, gerektiği yerde sütunların arasındaki çizgi gibi, tablonun bazı çerçevelerini korumak gerektiğini. Bu da, tasarımcı olarak tamamen sizin sanat anlayışınıza ve zevkinize kalmış bir şey. Çerçeveleri kaldırmak istiyorsanız, TABLE etiketinin BORDER= yüklemini 0 yapacaksınız. Peki, diğer çizgiler nasıl kontrol ediliyordu?

Kutulara yazı girmek kolay. TD etiketi ve yüklemleri kendisine vereceğiniz yazıyı bekliyor. Fakat Internet’i ilginç hale getiren, içeriğin sadece yazı olmaktan kurtulması oldu. Bu nedenle biz de kutularımıza, desen, ActiveX, Java, hareketli GIF dosyası, JPEG fotoğraf, ya da süslü harflerle yazılmış ve grafik dosyası haline getirilmiş başlıklar koyabiliriz. Bunların örneklerini çeşitli yerlerde bulabilirsiniz. Byte-Türkiye’nin CD Magazin’leri bunların örnekleri ile dolu.

/////////////////////////////////NOT//////////////////////

Elinize geçeni sayfanıza koyabilir misiniz?

Hayır!. Hem de kocaman bir hayır! Sözünü ettiğimiz bütün multimedya (çoklu ortam) unsurları, sanat eseridir; ve her sanat eserinin bir telif hakkı sahibi vardır. Telif hakkı size ait olmayan veya sahibi tarafından size kullanma hakkı verilmemiş bir sanat eserini yayınlayamazsınız. Bir sanat eserini Web sayfanıza koymak ve kamuoyunun ulaşabileceği Internet gibi herkese açık bir ortama yerleştirmek, yasaların “yayın” saydığı bir fiildir. İzinsiz sanat eseri yayınlamak ise, Türk Ceza Yasası’na göre ağır hapis cezasıyla cezalandırılan bir suçtur. Ceza yasalarını bir kenara bırakalım. Bu eserlere vücut veren, göznuru döken kişilerin, iznini almadan eserini yayınlamakla, bu kişiyi en tabiî haklarından birinden, mülkiyet hakkından mahrum etmiş olmuyor musunuz? Ve unutmayın; hoşunuza giden bir sanat eserinin yayın hakkını sahibinden satın alabilirsiniz. Bu çoğu zaman hiç de beklemediğiniz kadar kolay ve ucuz olabilir!

/////////////////////////////////////////////////////

Tablonuza çoklu-ortam ürünleri koymakla yazı koymak arasında kodlama bakımından biraz fark var. <TD>..</TD> etiketlerinin arasına istediğinizi yazın; tabloda denk geldiği yerde bu yazıyı görebilirsiniz. Ama iş grafik unsurlara gelince tarayıcıya bu dosyanın nerede olduğunu söylemeniz gerekir. Tablonun hücrelerine koyduğunuz yazı, HTML dosyasının bir parçası haline geldiği halde, diğer unsurlar, HTML’in içine girmezler; sadece nerede bulunduklarına dair bilgi, yani URL adresi, HTML’in içine yazılır ve HTML ile birlikte, Internet Server programı tarafından, ziyaretçinin bilgisayarına aktarılır. Bir tablonun hücrelerinde yer alan gönderme (referans) bilgisine göre ziyaretçiye aktaracağınız dosya, tarayıcı program tarafından tanınan bir biçimde olmalıdır. Tarayıcılar, sabit grafik alanında JPG, GIF, PNG; hareketli grafik alanında GIF, ses alanında AU, AIFF, RA, Video alanında AVI, MOV, gibi dosyaları yardımcı programlar olmaksızın, tanıyıp, ya kendi başlarına ya da gerekli plug-in ek parçaları kullanarak bilgisayar ekranında canlandırabiliyor ve gerekli sesi ses kartı varsa, bağlı hoparlorlerde elde edebiliyorlar. Tabloların hücrelerine, CGI programları (Tarayıcıdan gelecek komutla, Web Server’da çalıştırılan programlar), veritabanı uygulamaları, ActiveX ve Java programları da koyabilirsiniz.

Burada, son sakladığımız tablonun HTML dosyasını açın; oluşturduğumuz tabloya bazı çoklu-ortam unsurları koyacağız. Bu alıştırma için, benzeri türde arzu ettiğiniz unsurları kullanabilirsiniz.

Şimdi; önce tablomuzu görsel olarak biraz daha etkili hale getirelim. Bunun için tabloyu tanımladığımız etikette, çerçeve çizgilerini kaldılarım, hücreler arasındaki boşluğu arttıralım ve hücre içlerine marj koyalım:

<table border=0 cellspacing=5 cellpadding=5 width=600">

Bu noktada, tasarımcıların tablo etiketini sayfa iskeleti için kullanırken çerçevere olmamasında anlaştıklarını, ama hücreler arasında boşluk bırakıp bırakmamakta anlaşamadıklarını belirtmemiz gerekir. Bu, herhangi bir grafik tasarımda olduğu gibi, sadece bir zevk meselesi değil. Grafik tasarım bir bilim dalıdır ve temel ilkeleri vardır. Bu ilkelerden biri, bir tasarımda ögelerin birbirine karışmamasıdır. Bu nedenle bir kutuya koyduğunuz grafik ile yanındaki kutuda yer alacak bir diğer unsurun birbirine "dokunmaması" gerekir. Fakat farklı zemin renklerine sahip hücrelerin tümü birden, sayfanın zemini gibi ele alınabilir ve içlerindeki unsurlar izleyicinin dikkatini çekmek için birbirleriyle yarışmadıkları sürece aralarında boşluk bırakılmayabilir. Bu nedenle, tablomuzu tanımladığınız kodu önce “cellpadding=5”, sonra “cellpadding=0” olarak deneyin; en beğendiğinizde kalın.

Sonra birinci kutuyu oluşturan TD etiketinin yerine, bu etiketin oluşturduğu kutunun yeni özelliklerini belirleyecek ve içeriğini tayin edecek şekilde, şunları yazın: (Burada dosya adı olarak istediğiniz, ealinizde olan bir dosya adı verebilirsiniz; örnek dosya, ekrana DÜŞÜN yazan anime bir bir daktilo tuşunu gösteren GIF dosyasıdır.)

<td align="right" bgcolor="#C0C0C0"><img src="dusani.gif" width="250" height="180"></td>

İkinci kutuya ise başlığımızı koyacağız. Bunun için, bir grafik programında “Web Tasarımında Temel İlkeler” yazın, basit bir gölge verin ve dosyanızı GIF olarak kaydedin. Bizim örneğimizde bu dosyanın adı “tab06tit.gif”:

<td align="right" colspan=2 bgcolor="#CC9999"><img src="tab06tit.gif" width="346" height="180"></td>

İkinci kutuya yaptığımız işlemi farkettiniz mi? Ku kutu artık iki hücreyi kapsıyor; dolayısıyla üçüncü kutuya gerek kalmadı. Bu satırı kapatabiliriz: </tr>.

Şimdi sıra ikinci satıra geldi. İlk yazdığımız şekliyle, ikinci satırın birinci ve ikinci hücresi birleşmiş bulunuyorlar. Bu kutu, oluşturmakta olduğumuz Web alanının genel bir “İçindekiler” listesini tutabilir; yani buraya ziyaretçinin bizim sayfalarımızda neler bulacağını gösteren listemizi koyabiliriz. Diyelim ki, alanımızda şu bölümler bulanacak: Grafik İlkeler, İçerikle İlgili İlkeler, Davranış Kuralları. Şimdi bunu ikinci satırın birinci kutusuna girecek şekilde kodlayalım:

<td align= left bgcolor=”#FFCC99” colspan="2"><p><b><font size=”+3”>Web Tasarımında Gözetilecek İlkeler: </font></b></p>Grafikle İlgili İlkeler,<br>İçerikle İlgili İlkeler<br>Davranış Kuralları</td>

Dikkat ettiyseniz, burada listenin başlığını “<p>...</p>” etiketine aldığımız halde, listenin maddelerini <BR> ile ayırdık. Bunun nedeni, maddelerimizin arasında fazla geniş boşluklar koymamak içindir. Listenin başlığında font büyüklüğünü değişik bir ifadeyle tayin ettik. “+3” ifadesiyle, tarayıcıya, “Bu fontu normalden üç kere daha büyük göster!” demiş oluyoruz.

Eski sırasıyla beşinci kutuya, bizim ilkelerimizi gözeten, tasarımı başarılı, içeriği mükemmel Web alanlarından örnekler koymaya ne dersiniz? Peki, o zaman bu kutuyu da şöyle yeniden yazabiliriz:

<td align="center" bgcolor="”#FFFFCC”"><b><font size="+2" color="navy">Güzel Web Örnekleri</font></b><p><font size="+1">Web Tasarımcıları Derneği,<br>Tasarımcı Gençler Birliği<br>Gönüllü Web Ustaları</font></td>

Son iki satıra ve içindeki kutulara bu sayfada ihtiyacımız yok. Onun için, bu iki satırı ve hücrelerini oluşturan kodları yazmıyoruz ve kodumuzun tümü, yaptığımız bir iki ek değişikle, şöyle oluyor:

<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

<title>Tablonun Esaslari</title>

<meta name="Microsoft Theme" content="none">

</head>

<body topmargin="0" leftmargin="0">

<font face="Arial">

<table border="0" cellspacing="5" cellpadding="10" width="600">

<tr>

<td align="right" bgcolor="#C0C0C0"><img src="dusani.gif" width="250" height="180"></td>

<td align="right" colspan="2" bgcolor="#CC9999"><img src="tab06tit.gif" width="346"

height="180"></td>

</tr>

<tr>

<td align= left bgcolor=”#FFCC99” colspan="2"><p><b><font size=”+3”>Web Tasarımında Gözetilecek İlkeler: </font></b></p>Grafikle İlgili İlkeler,<br>İçerikle İlgili İlkeler<br>Davranış Kuralları</td>

<td align="center" bgcolor="”#FFFFCC”"><b><font size="+2" color="navy">Güzel Web Örnekleri</font></b><p><font size="+1">Web Tasarımcıları Derneği,<br>Tasarımcı Gençler Birliği<br>Gönüllü Web UstalarıGönüllü<br>Web Ustaları</font></td>

</tr>

</table>

</font>

</body>

</html>

Bu dosyayı, öncekinden farklı bir isimle kaydedin ve en beğendiğiniz tarayıcıda sınayın. Karşınıza şuna benzer bir görünüm çıkmış olmalı:

reh036.tif

Şimdi burada büyükçe bir parantez açalım ve sayfamızda olmayan bir şeyden söz edelim:

Sayfamızda henüz “Web’i Web yapan asıl unsur yok! Web’e bugünkü kimliğini veren unsurun, metinlerin, birbiri ile ilintilendirilmesi olduğunu hatırlıyorsunuz. Yani, bir kelimeye, cümleye hatta harfe veya rakama, bir başka metnin, paragrafın, harfin, sayfanın, grafiğin, hatta tamamen başka bir Web alanının adresini kodlayabilirsiniz. Internet’te bir şeyleri tıklayarak bir yerlere gitmemizi sağlayan bu kodlardır. Oysa bizim ana sayfamızda bir taraftan kendi alanızda, diğer taraftan başkalarının alanlarında olan bazı unsurları sıralayan iki liste var; ama bu listeler, bizim ziyaretçilerimizi hiç bir yere götürmüyorlar. Oysa ziyaretçilerimiz güzel Web örneklerinden birini görmek veya bizim Web ilkeleri ile verdiğimiz geniş bilgiyi okumak isteyebilirler. Bu durumda ne yapacaklar?

Bu sorunun cevabı bizi HTML’in adındaki birinci kelimeye “hyper” sıfatına götürüyor. Bir sayfanın gerçekten HTML ve oluşturduğu alanın gerçekten Web (ağ) olabilmesi için, unsurları ile başka unsurlar arasında link (ilinti, bağlantı) kurulması gerekli. Siz, bu ilintinin adresini belirtmekle görevlisiniz; kullanıcının bilgisayarındaki tarayıcı ise bu link’i izleyerek, sözkonusu içeriği kullanıcıya göstermek yükümlü. Tabiî, link’in işaret ettiği içerik unsuru (sayfa, grafik, ses, film, Internet alanı) oluşturulmuş ve Internet’e yüklenmiş olmalı. Sizin sabit diskinizde duran bir unsura link verirseniz, sabit diskiniz Internet’e açık değilse, kullanıcı bu malzemeye nasıl ulaşacak?

Link bilgisinin nasıl verileceğini, başka bir deyişle, Anchor (<A>..</A>) (bağlantı noktası) etiketinin nasıl yazılacağını, Çerçeve (Frame) etiketini incelerken ele alalım. Çünkü link’siz tablo olur da, Çerçeve olamaz!

## Çerçeveler

HTML’in yaygın olarak kullanılmaya başladığında içinde olmayan bir unsur çerçeve idi. Daha sonraki HTML standartlarında, çerçeve teknolojisi önerildiğinde, HTML’i ilk günlerinden beri kullananlar, sanki sözleşmiş gibi çerçeveden nefret ettiler. O kadar ki, hem Netscape, hem Internet Explorer’ı tasarlayan program mühendisleri, programlarına “çerçeveyi kapatma kolaylığı” bile getirdiler. Bugün bile bir çok Internet alanında, ziyaretçilere sayfaların çerçeveli ve çerçevesiz türleri öneriliyor. Çerçeve düşmanlığı, mantıksız olduğu kadar, teknik açıdan haklı! Internet’i salt bilgi (ya da düz yazı) alışverişi için kullanmak isteyenler, Çerçevelerin getirdiği ek indirme ve sayfa çizme yükü ile çerçevelerin ekran alanından “çaldığı” yerden kurtulmak stiyorlar. Ama Web sayfa tasarımcısı olarak bizleri düz yazıdan ibaret sayfadan kurtaran, tablodan bile güçlü sayfa iskeleti unsuru, çerçevedir.

Önce çerçevenin aldığı alan sorununa bakalım. Bugün, ortalama bilgisayar kullanıcısının ekranı, çaprazlama 15 ile 17 inç arasında değişmektedir. 17, 21 hatta 25 inçlik ekranların fiyatlarındaki hızlı düşüşe rağmen, ortalama ev bilgisayarının ekranını 15 inç olarak varsaymak zorundayız. Bu size eni 640 yüksekliği 480 pixel olan bir alan bırakıyor. Web tarayıcı programların ekranın sağ ve solunda 5 ile 15 pixel, üstünde 25 ile 150 pixel, altında yaklaşık 25 pixel’i zaten kendi penceresi için aldığını düşünürsek, kullanıcıya temiz Web alanı olarak en iyi ihtimalle 630’a 430, en kötü ihtimalle 610’a 305 pixellik bir pencere kalıyor. Bu alana, 5’er pixellik çizgileri olan dört çerçeve yerleştirdiğiniz zaman, aralardaki üç çizgi 15 pixellik bir alanı götürecektir.

Netscape 3 ile “çerçevesiz çerçeve” yönteminin gelmesi, çerçeveye karşı olan grubu biraz sakinleştirdi. Şimdi artık hem çerçevenin getirdiği imkanlardan yararlanabiliriz, hem de çerçevenin çizgilerinin aldığı yeri kazanmış olabiliriz. Çerçeve, bu anlamda, bilginin sistemli sunuluş aracı olmaktan çıkabilir, sayfa tasarım unsuru olabilir. Tablodan farklı olarak çerçeve teknolojisi, bize sayfamızın bir tarafı sabit kalırken, diğer tarafının içeriğini, kullanıcının tercihine göre değiştirme imkanı verir.

Çerçevenin de, tablo gibi, yapısal unsurları vardır: Sütunlar ve satırlar. Tablonun sütun ve satırları ile vücud bulan hücreleri ancak yanlarındaki hücreleri de kapsatarak genişletebilirken, çerçevelerin enini ve boyunu, kullanıcının ekran alanı ile sınırlanacak şekilde ayarlayabiliriz. Söz gelimi bir tabloyu, ekranı en dar kullanıcıyı gözönünde tutarak toplam 600 pixel yapabiliriz; ekranı 800 veya 1200 pixel olan kullanıcı için bu yarısı boş bir Web sayfası anlamına gelir. Oysa çerçeve teknolojisi sayesinde, sayfalarımızı tüm kullanıcıların ekran alanlarına uygun yapma imkanımız vardır.

### Çerçevenin Unsurları: Sütunlar ve Sıralar

Çerçeveli bir HTML sayfası oluşturmak, aslında, çerçeve sayısı kadar HTML sayfası oluşturmak demektir. Tablodan çerçeveyi ayıran en önemli unsur bu olsa gerek: Çerçeveli bir HTML sayfası saytınız ve, diyelim ki, dosyasını da “cerceve1.htm” adıyla kaydettiniz. Bu sayfa tarayıcıdan sadece hata mesajı alacaktır! Çünkü, çerçeveli sayfanıza, biraz sonra öğreneceğimiz usulle, koyduğunuz çerçevelerin “çağırdığı” sayfaları yapmadınız!

Bu karmaşık ifadeyi, uygulayarak, yakından inceleyelim:

Yine en beğendiğiniz düz yazı programını açın, en üste, artık klasik hale gelen kodları yazın:

<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

<title>Çerçeve Teknolojisi</title>

</head>

Çerçeve oluşturma kodu olan <frameset cols="">...</frameset> kodlarını girin. İçini birazdan dolduracağız. Bu kodla, tarayıcıya, gerçekte “Şimdi şu kadar ve şu ölçülerde çerçeve aç ve içlerine şu HTML sayfalarını koy!” demiş oluyorsunuz. Burada çerçeve sayısını “cols=” ifadesinden sonra vereceğiz ve buraya sayfamızda kaç çerçeve olsun istiyorsak o kadar ölçü yazacağız. Yani bir taşla iki kuş vuruyoruz: Ölçünü vererek, çerçeve sayısını söylemiş oluyoruz. Şimdi, elimizi alıştırmak için enleri birbirine eşit dört dikey çerçeve oluşturalım ve içlerine farklı zemin renkleri verelim, ve çerçeve sayısını yazalım. Bu dört çerçeveyi “çağıran” ifade, şöyle olacak:

<frameset cols="25%,25%,25%,25%">

Şimdi burada “col” ifadesiyle dikey çerçeve oluşturuyoruz. Birazdan “rows” ifadesiyle yatay çerçeve de oluşturacağız. Tarayıcıya herbir çerçevenin eninin kendi penceresinin dörtte biri kadar olması talimatını veriyoruz; virgül ile birbirinden ayrılmış dört ölçü yazmakla, tarayıcıya dört çerçeve oluşturmasını bildiriyoruz. Peki, bu çerçevelere ne konulacak?

Bunu, FRAMESET etiketinin içine yazacağımız kaynak gösteren satırlarla bildireceğiz; kaynaklarımız bu çerçevelerde yer alacak müstakil HTML sayfalarına işaret edecek.

Şimdi bunları yazalım. </frame> kodunun önüne şunları yazın:

<frame name="col" src="cer01.htm" marginheight="5" marginwidth="5" noresize scrolling="no">

<frame name="co2" src="cer02.htm" marginheight="5" marginwidth="5" noresize scrolling="no">

<frame name="co3" src="cer03.htm" marginheight="5" marginwidth="5" noresize scrolling="no">

<frame name="co4" src="cer04.htm" marginheight="5" marginwidth="5" noresize scrolling="no">

HTML’in klasik kapanış kodlarını da girelim:

<noframes>

<body>

</body>

</noframes>

</frameset>

</html>

Burada <noframes>..</noframes> kodu dikkatinizi çekmiş olmalı. Bu, başta belirttiğimiz, çerçeveden hoşlanmayan Internet meraklıları veya çerçeve teknolojisini beceremeyen tarayıcı kullananlar için, çerçevelerin içine yazdığınız unsurları buraya yazarak, çerçeveden hoşlanmayanların Web sayfanızdan eli boş çevirmemeyi sğlayan güvenlik önlemi. Şimdilik aynen yazın. Sonra isterseniz içini doldurursunuz.

Şimdi bu HTML’i “cerceve1.htm” adıyla saklayın. Tarayıcınıza bu sayfayı açtırın. Sonuç, herhalde şöyle bir mesaj olsa gerek:

reh037.tif

Tarayıcınız açılınca, karşınıza da şöyle bir tablo çıkacaktır:

reh038.tif

Neden? Çerçevelerinizin çağırdığı HTML sayfalarını yapmadınız da onun için! Şimdi, düz yazı programınızda, şu sayfayı oluşturun:

<html>

<head>

<title>Çerçeve 1</title>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</head>

<body bgcolor="#C0C0C0">

<p align="center"><big><big><big><strong>Çerçeve: 1</strong></big></big></big></p>

</body>

</html>

Bu sayfayı, “cer01.htm” adıyla saklayın. Başlıktaki 1’i 2; zemin rengini "#00FFFF"; paragraftaki “Çerçeve: 1” yazısını “Çerçeve: 2” yaparak ve dosya adını “cer02.htm” diye değiştirerek sayfayı yeniden kaydedin. Aynı değişiklikleri 3 ve 4’ncü sayfa için de yapın. Üçüncü sayfa için zemin rengini "#FF0000," dördüncü sayfanın zemin rengini ise "#00FF00" yapabilirsiniz. Bu dört dosyayı, “cerceve1.htm” dosyasının bulunduğu klasöre koymayı unutmayın.

Tarayıcınızı şimdi açın. Karşınıza şu görünümün çıkması gerek:

reh039.tif

Hızımızı almışken; “cerceve1.htm” dosyasını düz yazı programında açın, FRAMESET etiketinin önündeki “cols” ifadesini “rows” olarak değiştirin. Başka hiç bir şeyi değiştirmeden, dosyayı, “cerceve2.htm” adıyla kaydedin ve oluşturduğunuz HTML dosyasını tarayıcınızda açıp bakın. Biraz önceki dik sütunlar halindeki çerçeveleriniz, yatay hale geldi mi?

reh040.tif

Şimdi, FRAMESET sayfamıza, iki dikey, iki de yatay çerçeve koyalım. Yine “cerceve1.htm” dosyasını düz yazı programında açın, FRAMESET etiketinin önündeki “cols” ifadesini (cols="50%,50%"), “rows” ifadesini ise (rows="50%,50%") olarak değiştirin; başka hiç bir şeye dokunmayın ve dosyanızı “cerceve3.htm” adıyla saklayın. Şimdi bu sayfayı tarayıcıda açıp, bakalım:

reh041.tif

Harika! Şimdi eni, boyu birbirine eşit dört çerçevemiz oldu. Alıştırma olarak, “cerceve1.htm”, “cerceve2.htm” ve “cerceve3.htm” deki sütun ve sıra yüzdelerini değiştirin; yüzdeleri kaldırıp, yerlerine pixel cinsinden mutlak ölçüler verin. İşte size bir ev ödevi:

Sütun veya sıra ölçüsünü, örneğin (cols="100,\*") veya (rows="100,\*") yaparsanız, nasıl bir sonuç alırsınız. İpucu: Tabloda olmayan ama çerçeve teknolojisinde, sayfamızı ve sayfamızın bölümleri olan çerçevelerimizi kullanıcının tarayıcı ekranının tümünü kapsayacak kadar genişletebiliriz, demiştik. Bir ipucu daha: Asterisk, dosya adında “ne olursa olsun” demek olduğuna göre, acaba burada “Birinci sütun (veya sıra) 100 pixel olsun, ikincisi ne olursa olsun!” anlamına mı geliyor?

### Eşit Sayıda Olmayan Sütun ve Sıralar

Buraya kadar ya eşit sayıda sütun ve sıra, ya da eşit sayıda sütun veya sıra içeren çerçeveli sayfa yapmayı ele almış olduk. Açaba, sütun ve sıra sayıları eşit olmayabilir mi? Yani, tabloların hücrelerini alt ve ya yandaki hücrelerle birleştirdiğimiz gibi, çerçeveleri de yanlarında ve altlarındaki çerçevelerle birleştirebilir miyiz? Hayır, bunu yapamayız. Çerçeveleri birbirleriyle birleştiremeyiz, ama aynı görüntüyü elde edebiliriz. Sadece kodlamamız biraz farklı olur. Şimdi, şu örnekteki biçimde çerçeveler elde edelim:

cerorn.TIF

Dikkat etti iseniz, HTML’de çerçeveyi oluşturan FRAMESET komutunda ne kadar çerçeve alanı ayırırsanız ayırın, aynı etiketin içinde bu çerçevelerin kaynağını “<FRAME SRC="...." .....> ifadesiyle belirtmezseniz, tarayıcı, FRAMESET komutunda işaret edilen sıranın kaynağından önce yeni bir FRAMESET komutu ile bu kez sütun oluşturur ve onun kaynaklarını bildirirseniz, birinci FRAMESET’in diğer sıralarından önce, ikinci FRAMESET’in sütunlarını çizecektir. İşte eşit olmayan sayıda sütun ve sıra içeren çerçeveli sayfaları bu durumdan yararlanarak yazabilirsiniz. Önce, yukarıdaki şemada gösterilen birinci örneği yapalım. Birinci sütun tek sıralı, ikinci sütun iki sıralı bir çerçeve sayfası için kodumuz şöyle olmalıdır:

<FRAMESET COLS="25%,75%">

<FRAME SRC="cer01.htm" NORESIZE SCROLLING="auto">

<FRAMESET ROWS="20%,80%">

<FRAME SRC="cer02.htm" NORESIZE SCROLLING="auto">

<FRAME SRC="cer03.htm" NORESIZE SCROLLING="auto">

</FRAMESET>

Burada, önce iki sütunluk bir çerçeve alanı açıyoruz, birinci sütun tek sıralı olacağı için sadece bir kaynak gösteriyoruz; ikinci sütunu iki sıralı yapacağımız için önce bu sütuna sıralar oluşkuruyoruz; ve bu sıraların kaynaklarını gösteriyoruz. Bu kodun oluşturduğu sayfa, şöyle görünüyor:

reh042.tif

Örnekler şemamızdaki ikinci sayfada ise yanyana iki sütunun altında tek bir sıra var. Bunu gerçekleştirmek için, tarayıcıya iki ayrı FRAMESET komutu vereceğiz. İlk komut sayfada iki sıralı bir çerçeve oluşturacak; bu çerçevelerin kaynaklarını belirtemeye geçmeden hemen ayrı bir FRAMESET komutu ile iki sütun oluşturacağız. Bu sütunların içeğinin kaynaklarını belirttikten sonra, sütunları açan FRAMESET’i kapatacağız, alttaki sıranın kaynağını belirteceğiz. Kodumuz şöyle olacak:

<FRAMESET ROWS="50%,50%" frameborder="NO">

<FRAMESET COLS="50%,50%">

<FRAME SRC="cer01.htm" NAME="cer1" frameborder="NO" NORESIZE SCROLLING="NO">

<FRAME SRC="cer02.htm" NAME="cer2" frameborder="NO" NORESIZE SCROLLING="NO">

</FRAMESET>

<FRAME SRC="cer03.htm" NAME="cer3" frameborder="NO" NORESIZE SCROLLING="NO">

</FRAMESET>

Bu kodun yaptığı sayfa ise tarayıcıda şöyle görünecektir:

reh043.tif

Üstte bir, ortada, iki altta çerçeveden oluşan sayfaya gelince: Burada, deminki sayfanın mantığı ile, sıraları oluşturduktan ve birinci sıranın kaynagını verdikten sonra hemen ikinci bir FRAMESET komutu ile iki sütun oluşturacağız ve onların kaynaklarını bildireceğiz. Sütunları açan FRAMESET’i kapattıktan sonra alttaki sıranın kaynağını verelim ve birinci FRAMESET komutunu kapatalım. Kodumuz şöyle olacaktır:

<FRAMESET ROWS="20%,60%,20%">

<FRAME SRC="cer01.htm" NORESIZE SCROLLING="no" NAME="cer01" MARGINWIDTH="0" MARGINHEIGHT="0">

<FRAMESET COLS="20%,80%">

<FRAME SRC="cer02.htm" NORESIZE SCROLLING="auto" NAME="cer02" MARGINWIDTH="0" MARGINHEIGHT="0">

<FRAME SRC="cer03.htm" NORESIZE SCROLLING="auto" NAME="cer03" MARGINWIDTH="0" MARGINHEIGHT="0">

</FRAMESET>

<FRAME SRC="cer04.htm" NORESIZE SCROLLING="auto" NAME="cer04" MARGINWIDTH="0" MARGINHEIGHT="0">

</FRAMESET>

Bu kodun oluşturduğu sayfa ise tarayıcıda şöyle görünecektir:

reh044.tif

Bu bölümü kapatırken, ilkemizi özetleyelim: Önce bir FRAMESET komutu ile en üstte en soldaki unsur yanında başka sütun olmayan bir sütun ise sütunları; değilse sıraları oluşturun. Bu sütunda diğer sütunda olmayan sıralar varsa, o sıraları oluşturun. İlk oluşturulacak sıra veya sütunların kaynaklarını verin; ikinci ve üçüncü oluşturulacak sıraların kaynaklarını verin. Ve temel ilkeyi unutmayın, “önce açılan etiket sonra kapanır.

Şimdi bir ev ödevi. Şu sayfayı oluşturacak kodu nasıl yazarsınız:

reh045.tif

Bir iki ipucu verelim: Önce sütunları oluştaracaksınız; ama sütun kaynaklarını vermeden, hemen sıraları oluşturacaksınız.

## HTML’de Bağlantı’ya Giriş

Bu noktada duralım ve kodun içindeki <A>..</A> etiketini ele alalım. HTML’e hareket kazandıran bu etikettir. HTML etiketleri arasında Anchor (A) etiketinin yanı sıra, <BASE> ve <LINK> etiketleri de, bir noktadan bir diğerine gitmemizi sağlar. HTML sayfada metinlere ve diğer unsurlara bağlantı kazandırabilirsiniz. <A>..</A> etiketiyle metinlere kazandıracağımız bu ilişkinin temel kurallarını burada ele aldıktan sonra, diğer unsurları özellikle “olaylara” bağlantı kazandırma konusu, aşağıda Katmanlar konusunu işlerken göreceğiz.

#### Metinlere Bağlantı Kazandırmak

Anchor, İngilizce’de gemilerin demirine verilen isimdir. Gemi demirinin, gemiyi bir yere bağlaması gibi, bu etiketle sayfamızdaki bir unsuru, yukarıdaki örnekte “Grafikle İlgili İlkeler” ve diğer iki liste unsurunu, başka bir yere bağlamış oluyoruz.

<A>..</A> etiketine özellik kazandıran yüklemleri şöyle sıralayalabiliriz:

ACCESSKEY=”metin”: Bu yüklemle, bağlantının fare ile tıklamak yerine, klavyede bir veya birden fazla tuşa basarak yapılymasını sağlayabilirsiniz. “Metin” kelimesinin yerine yazacağınız karakterler, klavye kestirmesi olur.

CHARSET=”metin”: Bağlantı sağlanan Web kaynağının, tarayıcıda hangi dil kodlamasıyla gösterileceğini belirler. Bu yüklemi koymazsanız, kullanıcının tarayıcı programı ISO-8859-1 olan ASICII kodunu seçer. (Tarayıcılar açısından Türkçe kodlama ve yorumlama kodu, “charset=windows-1254" şeklindedir.)

COORDS=”X1, Y1, X2, Y2... Xn, Yn”: Bu yüklem, bağlantının metinde değil, bir grafik üzerinde oluşturulması halinde, resmin hangi koordinatları arası tıklanırsa, bağlantının sağlanacağını gösterir. Bu etiket, SHAPE yüklemi ile birlikte kullanılır.

HREF=”url”: URL, (Uniform Recourse Locator) Internet’te adres demektir. Bu adres, kendi sabit diskinizde bir klasör (ve alt-klasörler) içindeki bir dosyanın adı olabileceği gibi, HTTP, FTP veya elektronik posta yoluyla ulaşılabilecek bir Web alanı ve o alanın içindeki bir dosya olabilir. Ulaşılacak dosya, HTML dosyası olabileceği gibi, grafik, ses, video veya herhangi bir başka çoklu-ortam ögesi, program (“.bat,” “.exe” veya “.com”) ya da sıkıştırılmış ZIP dosyası olabilir. Önemli olan önce Web Server programının, sonra da tarayıcıların bu dosyayı ne yapacağını bilmesidir. Normal bir bilgisayar ortamında bulunabilecek bütün dosya türleri Server’lara tanıtıldığına, ve Netscape ve Internet Explorer gibi tarayıcı programlar herhangi bir dosyayı kendileri alıp gösteremezlerse, yardımcı bir program veya plug-in dediğimiz eklerin yardımı ile tanıdıklarına göre, bu noktada fazla sorun olamaz. Tarayıcılar genellikle, bir bağlantı ile kendisine gelen dosyayı ne yapacağını bilemezse, kullanıcıya bu dosyayı yerel sabit diske kaydetmeyi önerirler.

NAME=”metin”: Anchor’a isim vererek, daha sonra bu noktaya atıfta bulunma imkanı kazandırır. Bunu, bir sayfanın kendi içinde, belirli yerleri, örneğin baştarafı, belirlemek için kullanabilirsiniz. Çok uzun bir sayfanın baştarafına <a name="ust"> şeklinde bir “isimlendirilmiş Anchor” noktası koyarsanız ve aşağıda baştarafa dönüşü kolaylaştırmak için şöyle bir bağlantı yapabilirsiniz: <A HREF="ust”>Baştarafa dönmek için burayı tıklayınız</A>

REL=”metin”: Kurulacak ilişkinin niteliğini belirtir. Tarayıcılar, çoğu zaman bu ifadeye bakarak, bağlantı kurulunca ne yapabileceklerini bilirler. Örneğin “metin” yerine “stylesheet” yazarak, tarayıcıya alacağı dosyanın, daha sonra metinleri biçimlendirmekte kullanılacağını söyleyebiliriz.

SHAPE=(RECT/CIRCLE/POLY/DEFAULT): Bu yüklem ve karşısına yazacağınız ifade ile, tarayıcıya bir grafik unsurun üzerine konmuş bağlantı noktasının biçimini tanımlarsınız. Rect şeklin dörtgen, circle daire, poly çok kenarlı ve default ise arayıcının varsayılan bağlantı şekli olduğunu ifade eder. Bu yüklemi COORDS yüklemi ile birlikte kullanırsınız. Bu durumda COORDS’ün önüne yazacağınız “X1, Y1, X2, Y2, Xn, Yn” şeklindeki koordinatların da anlamı farklı olur. SHAPE’i “rect” olarak bildirirseniz, X1 ve Y1 şekin sol üst köşesinin, tarayıcı penceresinin sol üst köşesinden itibaren kaç pixel sağa ve aşağı konulacağını; X2 ve Y2 ise şeklin sağ alt köşesinin koordinatlarını gösterir (Örnek: SHAPE=rect, COORDS=”0,0,9,9”). SHAPE’i “circle” olarak tanımlarsanız, koordinatlar dairenin merkezini ve çapını gösterir (Örnek: SHAPE=circle COORDS=”10,10,5). Çok kenarlı bir şekil tanımlamanız halinde, her bir koordinat diğerine, son koordinat da birinciye bağlanır (Örnek SHAPE=poly COORDS=”10,50,25,20,20,50”). Şeklinde DEFALUT olarak bırakılması ise kullanılmamaktadır.

TARGET=”pencere”: Bu bağlantı sağlandığı zaman alınacak HTML sayfasının nerede kullanıcağını gösterir. FRAMESET etiketi bulunan bir sayfada kullanılması halinde, alınacak sayfanın hangi çerçeveye konulacağını gösterir. Burada “pencere” kelimesinin yerine şu değerler yazılabilir:

“çerçeve adı”: Oluşturulan çerçevelere önceden isim verilmiş ise, o isimler buraya yazılmak suretiyle, alınacak HTML sayfasının hangi çerçeveye yerleştirileceği belirtilebilir. Çerçeve isimleri mutlaka rakam veya harfla başlamalıdır.

\_blank: Alınacak sayfa veya unsur için yeni bir tarayıcı penceresi açılır.

\_parent: Alınacak unsur, o anda açık sayfayı oluşturmuş bir ana sayfa varsa, onun yerine konulur.

\_self: Alınacak sayfa mevcut sayfanın bulunduğu tarayıcı perceresine konulur.

\_top: Alınacak sayfa mevcut pencereye en üstten itibaren konulur.

#### HTML’de Bağlantı Türleri

Bu noktada, mevcut diğer HREF türlerini de belirtelim:

HTTP bağlantıları: Bağlantı, tarayıcının HTTP protokolünü kullanarak ulaşabileceği bir alanda ise, bunun gönderme ifadesi, <A HREF="http://www.bizimweb.com.tr/ogut2.htm" TARGET="ogut">İçerikle İlgili İlkeler</A> şeklinde yazılır. Başka bir Web alanında belirli dosyaya değil de, alanın birinci sayfasına (home page, index page, vs.) bağlantı veriyorsak, bağlantıyı <A HREF="http://www.bizimweb.com.tr/"> olarak bırakmalısınız. Buradaki son düz bölü işareti, tarayıcıya gittiği yerin bir sayfa değil, dizin olduğunu bildirecektir.

FTP bağlantıları: Kimi zaman verdiğimiz bağlantı, kullanıcının bir dosya aktarma alanından, HTTP protolünü değil de FTP (File Transfer Protocol) yöntemini kullanarak, bir dosyayı kendi bilgisayarına indirmesini sağlayabilir. Bunun için bağlantı ifademiz, örneğin şöyle olur: <A HREF="ftp://software.com/pub/">Bedava Yazılımlar</A>

Haber Grupları: Internet’in belki de en çok kullanılan haberleşme, görüş ve bilgi alışverişi yapılan, tartışma gruplarına yer verilen Usenet servisine yapılacak göndermede, protokol zikredilmez. Ayrıca bu göndermede düz bölü işareti de bulunmaz, Usenet’te, örneğin HTML program yazıcıların haberleşme grubuna bağlantı vermek için şu HREF ifadesini yazabiliriz: <A HREF="news:comp.infosystems.www.authoring.html">Web Program Yazıcıları Haberleşme Grubu</A>

Elektronik Posta Bağlantısı: Sayfanıza koyacağınız bir bağlantı, kullanıcının tarayıcısına, bir başka yere atlamayı veya bir dosya almayı değil de, varsayılan elektronik posta programını açarak, bir elektronik mektup göndermeye hazır hale gelmesini bildirebilir. Bunun için gönderme ifadesi içinde, tarayıcı programın “mailto” bölümüne atıf yapılır: <A HREF="mailto:webmaster@bizimweb.com.tr”>Sayfamız hakkında düşündüklerinizi bize bildirin</A>

Dosya Bağlantıları: Diyelim ki yaptığınız HTML dosyaları genel Internet’te değil de kendi okulunuzun yerel ağında veya firmanızın dahili Internet alanında (intranet) yer alacak. Bu durumda göndermeleriniz doğruca belirli bir sabit diskin bir klasöründe, bir dosyaya olabilir. Bu durumda dosya göndermesi ifadelerini kullanmanız gerekir. Bunu, örneğin, <A HREF="file://edebiyat/maaksoy/imarsı.htm">Mehmet Akif’in Eserleri: İstiklal Marşı</A> şeklinde yazarsınız.

Diğer bağlantılar: Internet’in ilk günlerin sık kullanılan Gopher, ve çok geniş bir alana yayılmış ağlarda veri tabanı araştırması yapmaya imkan weren WAIS, çok yaygın olmamakla birlikte, HREF ifadesi olarak kullanılabilir. Bu ve diğer bağlantı türleri hakkında son bilgiyi [http://www.w3.org/addressing/schemes.html](http://www.w3.org/addressing/schemes.html) adresinde bulabilirsiniz.

#### Sayfada Diğer Unsurlara Bağlantı Kazandırmak:

HTML sayfalarda, sadece belirli metinler veya metin parçalarına bağlantı sağlanmaz; aynı zamanda grafik unsurlara ve hatta ilerde göreceğimiz şekilde belirli olaylara, örneğin kullanıcının fare simgesini sayfada belirli bir unsurun üzerine getirmesine, belirli ses dosyasının çalınıp bitmesine, vs., de bağlantı kazandırılabilir. Ama bunun ayrıntılarını, Dinamik HTML ile ilgili bölümde ele alacağız. Burada sadece bunun mümkün olduğuna işaret edip geçelim; çünkü birazdan Webcilere Öğütler sayfamızda bu imkandan sayfalarımıza geriye dönüş imkanı kazandırmak için yararlanacağız. Şimdi çerçeveli sayfa alıştırmamıza geri dönelim.

#### Bağlantılı Çerçeve Uygulaması

Şimdi son iki bölümde öğrendiklerimizi, Tablolar konusunu ele alırken oluşturduğumuz örnek sayfamıza uygulayalım; ziyaretçilerimize verdiğimiz sayfalarda biraz değişiklik yapalım. Bu kez ziyaretçilerimize bir sayfada dört çerçeve vermek istiyoruz. Sol üst çerçeveye, tasarımcı-programcının birinci ilkesi olan “Düşün” tavsiyesini konu alan anime GIF dosyamızı koyalım. Üst sağ çerçeveye sayfamızın başlığını yerleştirelim. Sol alt sütunda, sayfamızı ziyaret edecek Web tasarımcılarına vereceğimiz öğütlerin başlıkları olsun; ve nihayet sağ alt kutuda, öğütlerimizi sunalım. Bu son çerçevenin içeriği, sayfamız açıldığında sayfamızın bir tür rasat kılavuzu, hareket rehberi olsun; ziyaretçilere nereyi tıklarlarsa nereye gidebileceklerini söyleyelim. “Gitmek” diyerek, sayfamızda bazı unsurları henüz gösterilmeyen sayfalarla ilişkilendireceğimizi, yani Web diliyle link kuracağımızı belirtmiş oluyoruz.

Stratejisini belirttiğimiz sayfanın temel malzemesi, (1) anime GIF dosyası, (2) başlık için GIF veya JPG grafik dosyası; (4) sayfa kılavuzunun içine koyacağımız öğütler listesini içeren HTML dosyası ve (4) bu listede yer alan her öğüt için bir HTML dosyasından ibarettir.

Web tasarımcılara vereceğimiz öğütleri nasıl grupladığımız hatırlıyor musunuz:

“Web Tasarımında Gözetilecek İlkeler: Grafikle İlgili İlkeler, İçerikle İlgili İlkeler, Davranış Kuralları”

Çerçeveli sayfalarımızı içerden dışarı ya da aşağıdan yukarı doğru oluşturacağız. Yani önce en dışarıdaki ya da en üstteki sayfaların çağıracağı içerdeki veya alttaki sayfaları yapacağız; sonra dışarıdaki sayfaları ve en son, en üstteki FRAMESET sayfasını yazacağız.

En içerde, ya da en altta, üç adet öğüt sayfamız var. Öğütlerin içeriği ile uğraşmamak için, bir çok masaüstü yayıncılık programı ile verilen ve içeriği hiç bir anlam ifade etmeyen, ala alıştırmalarda metin yazısı olarak kullanılan bir yazı dosyasını, ya da beğendiğiniz (!) bir Benioku.txt dosyasını, sabit diskinizde alıştırma yeri olarak tayin ettiğiniz klasöre kopya edin. Bu amaçla kullanılabilecek uygun dosyalardan biri, Adobe firmasının hemen her programı ile verdiği yazı örneği dosyasıdır. Büyük bir olasılıkla, “lorem ipsum..” diye başlayan ve içi tümüyle anlamsız kelimelerle dolu bu metni daha önce görmüş bulunuyorsunuz.

Örnek yazı dosyanızı açın, ve baştarafına şu kodları yazın

HTML>

<HEAD>

<TITLE>Ogut 1</TITLE>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</HEAD>

<BODY BGCOLOR="#80FFFF">

Sonra iki üç paragraf metin alın ve sonuna şu kodları koyun:

</BODY>

</HTML>

Özetle, ortaya şöyle bir dosya çıkartın:

<HTML>

<HEAD>

<TITLE>Ogut 1</TITLE>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</HEAD>

<BODY BGCOLOR="#80FFFF">

<P>Lorem ipsum,</P>

<P>Dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.</P>

<P>Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</P>

<P>Ut wisi enim,</P>

<P>Ad Minim Veniam</P>

</BODY>

</HTML>

Şimdi, bu dosyayı, “ogut1.htm” adıyla kaydedin. Sonra, başlıktaki Ogut 1’i Ogut 2 yapın, zemin rengini değiştirin (Renk kodlarını hatırlıyorsunuz, değil mi?) ve “ogut2.htm” adıyla bir daha kaydedin. Sonra, tahmin ettiğiniz gibi, sayfa başlığını Ogut 3 yapıp, zemin rengini değiştirip, “ogut3.htm” olarak bir daha kaydedin. Bu üç dosya, stratejimize göre, sağ alt çerçevenin içinde, ziyaretçinin tercihine göre, değişecek olan sayfalarımızı oluşturacaklar.

Şimdi, düz yazı editöründe, şu dosyayı (tabiî içeriğini arzu ettiğiniz gibi değiştererek, yazıp, “temp4.htm” adıyla kaydedin:

<HTML>

<HEAD>

<TITLE>Geçici Dördüncü Çerçeve</TITLE>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</HEAD>

<BODY>

<P><FONT FACE="Arial" SIZE="7">Sevgili Web tasarımcısı kardeş:</FONT></P>

<P><FONT SIZE="4"><B>Yan tarafta size sunacağımız öğütlerimizin bir listesini görüyorsunuz. Bu listede arzu ettiğiniz bir maddeyi tıklarsanız, bu kutunun içinde o konudaki öğütlerimizi bulacaksınız. İşlerinizde başarılar dileriz.</B></FONT></P>

<P><FONT SIZE="4"><B>Kolay gelsin..</B></FONT></P>

</BODY>

</HTML>

Bu dosya da, sayfamız açıldığında, öğütler çerçevisinin içinde ziyaretçilerimize “hoşgeldiniz!” diyecek olan sayfayı oluşturacak.

İçteki veya en alttaki dört sayfayı yaptık. Şimdi sıra bir üstteki sayfayı yapmaka geldi. Bu sayfaya, Web dilinde Navigation sayfası, çerçevesi veya bölümü denir. Kullanıcı, buraya koyacağımız bağlantı kelimelerini (ya da, grafik koyarsak, düğmeleri) kullanarak, sunduğumuz bağlantı noktalarına gidecektir.

“Web Tasarımında Gözetilecek İlkeler: Grafikle İlgili İlkeler, İçerikle İlgili İlkeler, Davranış Kuralları” şeklindeki sayfa planımızı, bağlantıları koyarak, Navigation sayfası haline getirelim. Sonra bu sayfayı sol alt çerçevenin içine yerleştireceğiz. Düz yazı programında “liste.htm” adını vererek, şu dosyayı oluşturun:

<HTML>

<HEAD>

<TITLE></TITLE>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</HEAD>

<BODY BGCOLOR="#808000">

<P ALIGN="left"><B><FONT COLOR="Red" SIZE="6">Web Tasarımında Gözetilecek İlkeler:</FONT></B></P>

<P><B><FONT SIZE="5" COLOR="Red"><A HREF="ogut1.htm" TARGET="ogut">Grafikle İlgili İlkeler</A></FONT></B></P>

<P><FONT SIZE="5" COLOR="Red"><B><A HREF="ogut2.htm" TARGET="ogut">İçerikle İlgili İlkeler</A></B></FONT></P>

<P><FONT SIZE="5" COLOR="Red"><B><A HREF="ogut3.htm" TARGET="ogut">Davranışla İlgili Kurallar</A></B></FONT></P>

</BODY>

</HTML>

Herhalde, yukarıdaki bölümde bağlantılarla ilgili bilgiler ışığında burada yapmak istediğimiz bağlantıyı görebiliyorsunuz. Birinci satırda, ziyaretçimizin tarayıcısına, kullanıcı “Grafikle İlgili İlkeler” kelimelerini tıkladığı taktirde, Web Server’dan “ogut1.htm” adlı dosyayı istemesini ve bunu, “ogut” adlı çerçeve içinde göstermesini söylüyoruz. Unutmayın, henüz FRAMESET sayfamızı yapmadığımız için ortada böyle bir çerçeve yok.

Çok sayfalı Web alanı inşa etmeye en içerden, en alttan başlamanın yararı budur: nereye, ne koyacağını tayin ederek geldiğiniz için, ilerde hangi dosyaya, hangi çerçeveye ne ad verdiğinizi unutmazsınız. Örneğin, işe bu sayfadan başlamış olsaydık, bu bağlantıya vereceğimiz dosya adını buraya yazmak zorunda olduğumuz için, bir isim uyduracaktık. Daha doğrusu üç isim... Sonra, her bir öğüt sayfasını yapıp sabit diske kaydederken, bu dosyalara ne isim vermemiz gerektiğini, gelip, Navigation sayfasını açarak yeniden öğrenmek zorunda kalacaktık. Bu boşuna zaman kaybını önlemiş olduk. Şimdi biliyoruz ki, FRAMESET sayfasını, ya da çerçeveli ana sayfayı yaparken, sağ alt köşedeki çerçeveye “ogut” adını vereceğiz.

/////////////////////////////NOT///////////////////

Ters Bölü İşaretine Ne Oldu?

HREF yükleminin önünde düz bölü işareti kullanılır. Sayganızı PC’de çalışan bir Web Server’a bile koyacak olsanız, kendi alanınızdaki klasörlere yaptığınız bütün URL referanslarınız ters bölü işareti (\\) değil, düz bölü işareti (/) olmalıdır. Diyelim ki, kendi sabit diskinizde bir dosyaya göndermede bulunuyorsunuz. Dosyanın, “C:\\belgeler\\html\\ornek.htm” olan “adresi,” HREF ifadesi olarak yazılırken, “C:/belgeler/htm/ornek.htm” olarak yazılmalıdır.

////////////////////////////////////////////////////////////

Şimdi sıra, FRAMESET sayfasını yapmaya geldi. Bu sayfa, aslında sadece çerçeveleri oluşturacak ve kaynaklarını gösterecek son derece basit bir dosya olacak. Sayfanın baştarafını yazalım:

<HTML>

<HEAD>

<TITLE>Ogutler</TITLE>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</HEAD>

<FRAMESET BORDER="0" COLS="240,\*">

<FRAMESET ROWS="180,\*">

<FRAME SRC="anim.htm" NAME="anim" NORESIZE SCROLLING="no" MARGINHEIGHT="0" MARGINWIDTH="0">

<FRAME SRC="liste.htm" NORESIZE SCROLLING="no" NAME="liste" MARGINWIDTH="10" MARGINHEIGHT="10">

</FRAMESET>

<FRAMESET ROWS="271,61%">

<FRAME SRC="baslik.htm" NORESIZE SCROLLING="no" NAME="baslik" MARGINWIDTH="10" MARGINHEIGHT="10">

<FRAME SRC="temp4.htm" NORESIZE SCROLLING="auto" NAME="ogut" MARGINWIDTH="10" MARGINHEIGHT="1">

</FRAMESET>

</FRAMESET>

FRAMESET etiketinin çerçeve çizgilerine ilişkin BORDER yüklemine istediğiniz değeri verebilirsiniz. Ama daha önce de belirttiğimiz gibi bu sadece bir görsel ilke veya zevk meselesi değil. Kimi kullanıcılar, çerçevelerin aldığı yeri kayıp sayarlar. Çerçevelere çizgi koymayarak bu endişenin önüne geçebiliriz. Bir de, sütun ve sıra boyutlarını belirlediğimiz ifadelere dikkat edin. COLS=”240,\*” ve ROWS=”1800,\*” ifadeleriyle, sadece sol üst kutunun boyutlarını belirliyoruz, geri kalan kutular için tarayıcıya “Geriye ne kaldı ise o kadar yer ayır!” demiş oluyoruz. Bu iki ölçü, sol üst kutuya koymaya niyet ettiğimiz anime grafiğin boyutlarıdır. Böylece, kullanıcının programı, bu kutuyu grafiğin alması gereken yere dokunmayacaktır. Dokunursa ne olur? Büyük bir olasılıkla, grafiğin iki tarafında anlamsız boşluklar kalacak ve ortaya görsel açıdan çirkin bir tablo çıkacaktır. Grafiklerin ve İçindekiler listemizin yer alacağı çerçevelerin altında ve sağında kaydırma çubukları olması da gerekmiyor. Ayrıca bu üç çerçevenin kullanıcı tarafından içindekileri daha rahat görmek için eninin boyunun genişletilmesine de gerek yok. Fakat değişken içeriğin yera lacağı sağ alttaki çerçevenin, içine girecek yazının boyuna göre, otomatik olarak, ihtiyaç varsa kaydırma çubuklarıyla, ihtiyaç yoksa çubuklar olmaksızın gösterilmesi gerekiyor. Bu nedenle oluşturduğumuz dört çerçeveden üçü ölçüsünün değiştirilmesi imkanı kapatılarak (NORESIZE) ve kaydırma çubukları olmaksızın (SCROLLING="no") ifadeleri ile oluşturulurken, dördüncü (SCROLLING="auto") ifadesiyle oluşturuluyor. Bu arada her dört çerçeveye de isim verdiğimizi farketmiş olmalısınız. Çerçeveleri isimlendirmek, o andaki tasarım stratejisi gerektirmese de ilerde yararlı olabilir. Ayrıca biz dördüncü çerçeveye isim vermek zorundayız; çünkü İçindekiler listesinde kullanıcının yapacağı tercihe göre çağrılacak öğüt sayfası, bu çerçeveyi adıyla arayıp, bulacak.

Şimdi, dosyanın son bölümünü yazalım:

<NOFRAMES>

<BODY>

<P>Maalesef sizin Web Browser programınız biraz antika! Bu sayfayı çerçeveli olarak göremiyorsunuz. Onun için size düz bir liste veriyoruz:</P><P><B><FONT SIZE="5" COLOR="Red"><A HREF="ogut1.htm">Grafikle İlgili İlkeler</A></FONT></B></P><P><FONT SIZE="5" COLOR="Red"><B><A HREF="ogut2.htm">İçerikle İlgili İlkeler</A></B></FONT></P><P><FONT SIZE="5" COLOR="Red"><B><A HREF="ogut3.htm">Davranışla İlgili Kurallar</A></B></FONT></P>

</BODY>

</NOFRAMES>

</HTML>

Baştan beri örnek çerçeve dosyalarımızda içini boş bıraktığımız <NOFRAMES>..</NOFRAMES> içini bu kez dolduruyoruz. Tarayıcıların çerçeve teknolojisinden önceki sürümlerini halâ kullanan ziyaretçilerimize, ekranlarında bomboş bir sayfa görmemeleri için, kibarca programlarını güncelleştirmeleri zamanı geldiğini hatırlatarak, sayfamızın sadece metin içeren sürümünü sunuyoruz. Bu kişiler de, diğerleri gibi öğüt seçeneklerimizi görecekler ve herhangi birini tıkladıkları taktirde, ilgili öğüt sayfamıza gideceklerdir.

Şimdi bu dosyayı “ogutler.htm” adıyla saklayın; tarayıcınızda açıp bakın. Karşınıza şu tablo çıkmalıdır:

reh047.tif

Şimdi burada hemen dikkat etmeniz gereken bir önemli unsur var. Bir başka unsurla arasında bağlantı kurduğunuz kelime, cümle veya paragrafın, tarayıcı ekranında gösterilirken, (tabiî kullanıcı olarak tarayıcının varsayılan tercihlerini değiştirmemişseniz) altının bir çizgiyle çizildiğini ve metin renginin koyu mavi olduğunu farketmiş olmalısınız. Bu, artık Internet’te bağlantının klasik görünümü halini aldı. Bu Internet’e önce Macintosh ardından Windows işletim sistemlerinin Yardım dosyalarındaki Hyperlink’lerin gösterilme tarzından miras kalmış bulunuyor.

#### Bağlantıları Grafiklere Yerleştirmek: Düğmeler

Şimdi, İçindekiler sayfamızda küçük bir değişiklik yapacağız. Bu sayfadaki bağlantı gösteren kelimelerin yanına birer düğme koyacağız ve kullanıcının bu düğmeyi tıklaması halinde, ilgili öğüt sayfasına gitmesini sağlayacağız.

Bunun için bize bir düğme grafiği gerekiyor. Internet adeta böyle düğmelerle kaynıyor. Fakat karşınıza çıkan ilk sayfada, hoşuna giden ilk düğme grafiğini farenin sağ düğmesi ile tıklayıp, açılacak listeden “Save Picture as” maddesini seçerek ve sabit diske yazılacak grafiği istediğiniz yerde kullanamazsınız. Gerçi “kim görevek?” diye düşünebilirsiniz, ama böyle bir davranış yasal olmadığı kadar, ahlaka da aykırı olur. Tasarımcı, yani ortaya kendi fikir ve sanat eserini çıkartacak bir kişi olarak, herkesden önce bizim böyle bir şey yapmaya hakkımız olamaz. Kendi grafiklerinizi kendiniz yapmayacaksanız, en iyisi, “Bu grafikleri alıp, kullanabilirsiniz,” diyen bir Internet alanından beğendiğiniz grafikleri almak olabilir. Grafik programlarının CD-ROM’ları da on binlerce Internet’te kullanma izni olan grafikle dolu!

Diyelim ki, kullanılmasında sakınca olmayan böyle bir dosyamız var, ve adı da “dugme.gif”. Şimdi, Navigation amacıyla yazdığımız “liste.htm” adlı dosyayı açalım; ve içindoe bir iki değişiklik yapalım. Yapmak istediğimiz şey; liste maddelerimize dokunmadan, önlerine içinde “tıklayınız” yazan düğme grafiklerini koymak ve bağlantıyı yazıdan alıp, bu düğmeye vermek. Bunun için <BODY>...</BODY> etiketinin içine şu kodu yazacağız:

<p align="center"><b><font color="Red" size="6">Web Tasarımında Gözetilecek İlkeler:</font></b></p>

<p><b><font size="5" color="Red"><a href="ogut1.htm" target="ogut"><img src="dugme.gif" width="50" height="28" border="0" alt="Dugme" align="middle"></a><font color="#6600CC">Grafikle İlgili İlkeler</font></font></b></p>

<p><font size="5" color="Red"><b><font size="5" color="Red"><a href="ogut2.htm" target="ogut"><img src="dugme.gif" width="50" height="28" border="0" alt="Dugme" align="middle"></a></font><font color="#6600CC">İçerikle İlgili İlkeler</font></b></font></p>

<p><font size="5" color="Red"><b><font size="5" color="Red"><a href="ogut3.htm" target="ogut"><img src="dugme.gif" width="50" height="28" border="0" alt="Dugme" align="middle"></a></font><font color="#3300CC">Davranışla İlgili Kurallar</font></b></font></p>

Bu dosyayı, “yeniliste.htm” adıyla kaydedin ve neler yaptığımıza bir bakalım. Bir kere, metinlerimizi <A>...</A> etiketinin içinden çıkarttık, yerine bir grafik kaynağı yazdık:

<img src="dugme.gif" width="150" height="58" border="0" alt="Dugme" align="middle">

Bu kaynak adresinde sadece grafik dosyamızın adı değil, fakat onunla birlikte daha bir çok bilgiler var. Bu grafiğin ekranda ne büyüklükte gösterileceği, eni (width) ve yüksekliği (height) pixel olarak belirtiliyor; graifin içinde yer alacağı kutunun çerçevesi olmaması isteniyor (border=”0”); grafik ziyaretçinin bilgisayarına yükleninceye kadar ve gönderilemez onun yerine alternatif olarak ekranda “dugme” kelimesinin görünmesi bildiriliyor (alt=”dugme”); ve nihayet, grafik kutusunun yarındaki nesneye (bu durumda yazı) ortalanması isteniyor (align=”middle”). dikkat ettiyseniz, <A> etiketinin içeriğinde bir değişiklik yok; bu düğme tıklanırsa, “ogut1.htm” (veya ogut2, ogut2) dosyayı, adı “ogut” olan çerçevenin içine yerleştirilecek.

Şimdi bir de “ogutler.htm” adlı FRAMESET dosyasında, sol alt kutuya, “liste.htm” değil de yeni oluşturduğumuz “yeniliste.htm” dosyasının konulmasını sağlayalım. Bunun için “ogutler.htm” dosyasının içinde, birinci sütunda ikinci sırayı tanımlayan ifadenin içindeki “liste.htm” adını “yeniliste.htm” yapıyoruz ve bu satır şöyle oluyor:

<FRAME SRC="yeniliste.htm" NORESIZE SCROLLING="no" NAME="liste" MARGINWIDTH="10" MARGINHEIGHT="10">

Bu dosyayı “ogutle2.htm” adıyla kaydediyoruz; tarayıcıda açıp bakıyoruz:

reh061.tif

Düğmeleri sınıyoruz. Bütün bağlantılar doğru çalışıyor mu? Öğüt sayfaları açılmaları gerektiği gibi, sağ alt köşedeki kutuda açılıyor mu? Evet, her şey mükemmel çalışıyorsa, oluşturduğumuz bu sayfayla Web Tasarımı Şampiyonası’nda dereceye giremeyiz, ama çerçeve teknolojisini öğrendik demektir!

## Katmanlar ve CSS Teknikleri: Dinamik HTML’e Giriş

“HTML’de, tarayıcıların kalıplarına uymak zorundayız. Sayfaya koyacağımız bir başlık bir diğerinden daha büyük dursun istiyorsak, birini H3, diğerini H2 yaparız; sorun çözülür.”

Bu “Eski Web”in bir kuralıydı; şimdi, yukarıda Metin Düzenleme Etiketleri’ne ele aldığımız bölümde, Yerel Biçimlendirme kavramından söz ederek, ”Yeni Web”in eskinin kurallarını kıran imkanlarına kısaca değinmiştik.

Bununla birlikte sayfalarımızın çatısını, ya da Pagemaker, Quark Express, Corel Ventura gibi masaüstü yayıncılık programlarının ustalarının diliyle, sayfa iskeletini kurarken, yine de HTML’in bize verdiği iki imkanı, tablo ve çerçeve araçlarını, biraz varoluş amaçlarının dışına çıkarak kullanmaktan başka çaremiz olmadığını gördük.

Peki, şimdi şu sayfaya bir bakın:

reh062.tif

Bu sayfada bir tek tablo, bir tek çerçeve olmadığını, grafik unsur olarak sadece yayının başlığı olan “Gazete” kelimesinin bulunduğunu söylersek, “Yeni Web” teknolojisinin ya da bu bölümde ele alacağımız Katman ve Cascading Style Sheets (Yığılmalı Stil Sayfaları) yöntemlerinin Web sayfası tasarımına kazandırdığı imkanların boyutu hakkında bir fikir vermiş oluruz.

Bir de, bir HTML sayfasının değişik anlardaki ekran görünümlerine bakın:

reh064.tif

reh065.tif

reh066.tif

Buradaki sayfada görülen grafik kendi içinde hareketli, yani anime GIF dosyası olmakla birlikte, dosyanın içeriğini içine koyduğumuz unsur sayfada hareket etmektedir!

Oysa baştan beri görüyoruz ki, ne tabloların hücreleri, ne de çerçeveler sayfada konuldukları yerde sabit durmakta, ancak içlerinde bulunan hareketli GIF dosyalarındaki unsurlar, kendilerine ne gibi bir hareket kazandırılmış o harekete yapmaktadırlar. Buradaki lama, ayaklarını kaldırıp indirerek ve başını sallayarak yürüyormuş izlenimini veren bir animasyon örneğidir. Fakat lama resmini içinde bulunduran unsuru, sayfa içinde hareket ettirmek, şu ana kadar ele aldığımız tekniklerle mümkün olamaz.

Bunu sağlayan Katman veya Layer teknolojisi, HTML’in bu tarihe kadar kazandığı en büyük imkan olabilecekken, ne yazık ki, tarayıcı firmaları arasında, bilgisayar ekranlarına egemenlik sağlama savaşında, Dinamik HTML’in tanımındaki farklılık ve nedeniyle, henüz gelebileceği yere gelememiş bulunuyor. CSS ise, katman tekniğinden daha şanslı bir uygulama alanı buldu; ama yine de tarayıcı alanında Netscape firmasının uygulamaları ile Microsoft firmasının uygulamaları arasında fark var.

Bu iki tekniğin getirdiği olağanüstü kolaylıklardan yararlanmak, fakat bu arada, Internet müdavimlerinin en az üçte ikisini elden kaçırmak istemiyorsanız, sayfalarınızda Katman ve CSS yöntemlerini her iki tarayıcının asgari ortak noktalarına hitabeden tarzda kullanmanız gerekir. Bu nedenle, günümüzde bir çok Internet alanı, kendisini ziyaret eden kişinin, önce kullandığı tarayıcının adına ve sürümüne bakıyor; ardından bu iki bilgiye uygun bir içerik sunuyor.

Katman ve CSS teknolojileri adeta içiçe kullanıldığı için, bu noktadan itibaren aralarında ayrım yapmayacağız; arzu ettiğimiz bir iki etki türünü oluştururken bu tekniklerin hangisinden nasıl yararlanacağızı göreceğiz. Ve tabiî bu arada ele aldığımız konuya uygun olduğu ölçüde iki tarayıcı arasındaki uygulama ve yorumlama farklarına değineceğiz.

Önce Dinamik HTML veya DHTML nedir sorununa cevap arayalım. DHTML, Web tarayıcısına indirildikten sonra ekranda yer alan unsurları değişen HTML demektir. Bu değişim, bir grafiğin hareket kazanması veya şekil değiştirmesi; bir grafiğin yerini başka bir grafiğin alması; belirli bir zaman geçince sayfanın yeniden indirilmesi veya belirli bir bölümünün yenilenmesi; kullanıcının belirli hareketleri, örneğin fareyi oynatması veya bir yeri tıklaması sonucu sayfanın içeriğinde değişiklikler olması, olabilir. Yukarıda ilk bağlantı örneğimizde bir başka unsurla arasında bağlantı kurduğumuz kelimelerin, tarayıcı ekranında gösterilirken, (tabiî kullanıcı tarayıcının varsayılan tercihlerini değiştirmemişse) altının bir çizgiyle çizildiğini ve metin renginin koyu mavi olduğunu farketmiştik. Internet’te bağlantının klasik görünümü halini almiş olan bu durumu değiştirip, kullanıcı fare simgesini herhangi bir bağlantı unsurunun üzerine getirecek olursa, bağlantı unsuru kelime ise başka renk almasını, grafik ise başka bir grafikle yer değiştirmesini sağlayabiliriz.

Bu “değişim” örnekleri, içeriği kullanıcının tercihlerine (sözgelimi, bizim sayfalarımızda daha önce neler yaptığının tarihçesine), veya kullanıcının bulunduğu yerde saatin kaç olduğuna bakarak tümüyle farklı vermek gibi dinamik uygulamalarla kıyaslandığında biraz statik görünebilir. Fakat, bu örneklerde de HTML, daha önceki sayfalarımıza göre oldukça hareketli sayılabilir. Şimdi bu hareketi sayfalarımıza kazandıracak etiketlerle tanışalım. Daha önce yaptığımız gibi, yine bunu örnekle yapalım.

### HTML’de Nesne Kavramı

DHTML’i bir teknikler demeti olarak ele alırsak, ilk tekniğimiz, sayfamıza ne metin, ne grafik, ne tablo ve ne de çerçeve sayılmayan, ama içinde bunların tümüne de yer verebileceğiniz nesne (object) kavramına dayanıyor. Bu sağlayan etiketin adı Bölüm/Division’dır (<DIV>..</DIV>).

Bölüm ve ilerde değineceğimiz diğer Katman (Layer) etiketlerini, teknik ressamların kullandığı ince şeffat kağıtlara benzetebiliriz. Bir dekoratörün ev planının üzerine, masaların, sandalyelerin, dolapların nasıl yerleştirileceğini gösteren parşömen kağıdına yaptığı çizimi gözününüzün önüne getirin. Bu parşömen, alttaki asıl plan üzerinde istenilen yere kaydırılarak, eşyaların nasıl yerleştirilmesinin daha uygun olacağı araştırılabilir. Sonunda parşömenin belirli bir yere yerleştirilmesi ile iç düzenleme planı elde edilir. <DIV>..</DIV> etiketleri arasında yer alan her şey, yani yazılar, resimler, grafikler, tablolar, video, ses ve benzeri çoklu-ortam unsurları, bu etikete vereceğiniz yerleştirme ve değişme özelliklerine uygun hareket ederler.

#### Cascading Style Sheets (Yığılmalı Stil Kağıtları)

Bu kadar teori yeter; şimdi uygulamaya geçelim. Ama önce biçimlerdirme ile ilgili bir hatırlatma yapalım. Web sayfalarını biçimlendirme konusunu ilk ele aldığımızda yerel biçimlendirme yoluna gitmiş ve neyi biçimlendireceksek o unsurun önünde biçim komutları vermiştik. Ancak yerel biçimlendirme dediğimiz bu yöntemi ele alırken, HTML’de çok daha kullanışlı, bir sayfanın bütün unsurları ve bir Web alanının bütün sayfaları arasında görsel birlik sağlamamıza yarayacak iki ayrı biçimlendirme yöntemi bulunduğunu da söylemiş ve geçmiştik.

Şimdi bu iki yöntemi ele alalım; çünkü Web sayfasınhda “nesne” oluşturmak için önce bu nesnelerin alacağı şekli belirlememiz gerekiyor. Bu iki yeni biçimlendirme yöntemine Cascading Style Sheets (Yığılmalı Stil Kağıtları) adı veriliyor. Yığılmalı: çünkü HTML vereceğiniz bütün stil komutlarını bilgisayarın belleğinde bir yere yığıcak ve en üstteki kullanacaktır. Kağıt: çünkü adını eskiden bir matbaaya iş verirken, içerik malzemesinin üzerine eklenen ve kapağın nasıl olacağını, metnin çeşitli bölümlerinin hangi harflerle ve ne büyüklükte basılacağını ve genel sayfa düzeninin nasıl yapılacağını belirten bir sayfalık stil kağıdından alıyor. CSS standartlarına göre, yerel olmayan biçimlerdirme (1) biçim komutlarını toplu olarak HTML dosyasının HEAD bölümüne koyarak ve aşağıda gövde bölümünde nerede ihtiyaç olursa oradan yukarıya stil göndermesi yaparak, ya da (2) bu komutların tümünü HTML dosyasının dışında oluşturduğumuz ve HTML dosyasına “Link” etiketiyle bağladığımız ayrı dosya yoluyla yapılır.

Şimdi düz yazı programınızı açın ve başlayın yazmaya:

<style>

<!-

body {background-color: #ffe4b5; background-ımage: none; background-repeat: repeat; color: #000000; margın-left: 1cm; margın-rıght: 1cm; margın-top: 1cm; posıtıon: relative}

p { color: black; font-famıly: 12pt; text-ındent: 1cm}

h1 { color: #008080; font-famıly: 30 pt arial, helvetica, sans-serif}

h2{ color: #008000; font-famıly: 18 pt arial, helvetica, sans-serif}

h3{ color: #ff0000; font-famıly: 14 pt arial black, helvetica black, sans-serif; margın-left: 3cm; margın-rıght: 2cm; margın-top: 2cm}

a { color: aqua; font-famıly: arial; margın-left: 3cm; margın-rıght: 2cm; margın-top: 2cm}

-->

</style>

Parantezlerin düz köşeli değil, kıvrık parantez olduğuna dikkat edir ve bu dosyayı, “ilkstil.css” adıyla kaydedin; ama dosyayı kapatmayın.

Tebrikler, ilk CSS dosyasını oluşturdunuz. Şimdi bunu, bir HTML sayfasına LINK edelim. İlk yaptığımız hoşgeldin sayfalarından birini açabilir ve içinde değişiklik yapabilirsiniz. Şöyle bir HTML oluşturmak istiyoruz:

<html>

<head>

<title>HTML ve Web</title>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

<link rel="stylesheet" href="ilkstil.CSS"></head>

<h1>Tasarımcı kimdir?</h1>

<h2>Tasarım nedir?</h2>

<p>“Bizler, inandığımız için ve bilinçli olarak harf tasarımcısıyız, harf dökümcüsüyüz, sayfa dizgicisiyiz.. <b>Yoksa, yeteneğimiz daha yüksek şeyler için elverişsiz olduğu için değil.</b> Biz inanıyoruz ki, en yüksek düzeyde beceri gerektiren şey, bizim sanatımıza en yakın olanıdır..”</p>

<h3><center>Rudolf Koch - <i>Alman harf dökümcüsü, kaligraf</i></center></h3>

</body>

</html>

Bu sayfayı “ilkstil.htm” adıyla kaydedin, fakat dosyayı da kapatmayın. “Ilkstil.htm” dosyasını tarayıcınızda açın. Karşınıza şöyle bir görünüm çıkacaktır:

reh071.tif

Şimdi, açık olan CSS dosyasında H1 türü başlıklarla ilgili stil satırında font ailesi bölümünü değiştirin. Satır şöyle olsun:

H1 { COLOR: #008080; FONT-FAMILY: 26 pt serif}

CSS dosyasını aynı adla saklayın ve tarayıcınız hala açıksa “Reload” düşmesine basın; kapalıysa “ilkstil.htm” sayfasını tekrar açın. İki sayfadaki büyük başlığı karşılaştırın:

reh072.tif

HTML dosyasına elinizi sürmediğiniz halde, sayfadaki bir unsurun stili değişmiş oldu. Neden? Çünkü HTML sayfanız, bütün stil bilgisini “ilkstil.css” dosyasından alıyor; CSS dosyasındaki her değişiklik, bu dosya ile LINK halindeki bütün Web sayfalarına yansıyacaktır.

Çok güzel. Şimdi, CSS dosyasındaki herşeyi aynen HTML dosyasına <LINK...> satırının yerine aktarın (CSS dosyasının açık olduğu düz yazı programındaki tüm yazıları seçip, kopyaladıktan sonra “ilkstil.htm” dosyasında LINK satırının yerine yapıştırabilirsiniz). Bu dosyayı, “ilkstil2.htm” adıyla kaydedin ve tarayıcıda bakın. Biraz önceki sayfadan hiç farkı yok. Çünkü, önceki sayfanın stil bilgisi dışarıdaki bir dosyadan geliyordu; bu kez stil bilgisini HTML’in içine gömdük. Buna da Embeded” (Gömülü) stil sayfası denir.

///////////////NOT/////////////////////

Peki bir HTML sayfasına hem LINK, hem de EMBEDED stil sayfası verirsek, ne olur?

Uluslararası Web Konsorsiyom’unun (W3C), Web sayfalarına stil verme tekniğine birbiri üstüne yığılma, deste gibi dizilme anlamına gelen “Cascading” kelimesini ad olarak seçmelerinin nedeni, HTML’e birden fazla yöntemle stil komutu verilmesi halinde, bunları iskambil kağıdını gibi üstüste dizmesi ve uygulamaya en üstten başlamasıdır. Bir HTML sayfaya iki LINK komutu ile ardarda iki ayrı CSS dosyası bağlarsanız, ikisinde de aynı unsurlara farklı biçimler veriliyorsa, ikincisindeki, yani destenin en üstüne gelendeki komutlar geçerli olur. Bir HTML’e biri LINK, diğeri ayrı stil bilgisi verilirse ve ikisinde de aynı unsurlar için farklı komutlar varsa, ikincisi, yani HTML’in içinde geçerli olur; çünkü HTML önce dış dosyayı okuyacak, onun üstüne kendi içindeki stilleri koyacaktır. Ve son olarak, bir sayfada hem LINK, hem bağlantısı olsa ve diyelim ki bir HTML unsurunun önünde onu biçimlendiren bir yerel stil komutu (INLINE stil) bulunsa, en son okunan yerel stil komutu olacağı için, tarayıcı ilk iki stili bir kenara bırakıp, INLINE stili uygulayacaktır. Bir Web alanının bütün ortak özellikleri, örneğin sayfaların zemin rengi, metin ve başlıkların rengi, sağ ve sol marjları LINK CSS ile verilebilir; bu alandaki herhangi bir HTML sayfasını bu temel kurallardan ayrı biçimlerdirme zorunluğu varsa, sadece o sayfada yoluyla değişiklik yapılabilir. Bu durumda bile herhangi bir paragrafın veya bir grafiğin hem tüm alandan, hem de içinde bulunduğu sayfadan farklı bir stile ihtiyacı bulunuyorsa, o zaman bunu INLINE stil ile yapabilirsiniz. Böylece Internet alanınızın tümü ve herbir sayfanın içindeki bütün unsurlar hem belirli bir standarda kolayca uyabilirler; hem de özel durumlarının gerektirdiği değişiklik anında yapılabilir.

////////////////////////

### Stil kurallarını Nesnelere Uygulamak

Stil bilgilerini nereye koyacağımızı, veya dışarıdaki dosyaları nasıl bağlayacağımızı gördük; ama hangi unsurların hangi özelliklerini stil yoluyla kontrol edebileceğimizden söz etmedik. DIV ve SPAN etiketleri yardımıyla Nesne oluşturmak ve stil komutları ile bunları biçimlendirmeye ve sayfada istediğimiz yere yerleştirmeye geçmeden önce neleri, ve hangi özelliklerini kontrol edebileceğimizden kısaca söz etmemiz yerinde olur.

W3C’nin CSS standardı, bize dört ayrı unsur seçme imkanı veriyor. HTML’in hangi unsurunu seçip biçimlendirdiğimizi tarayıcıya bildiren ifadelere Seçici (Selector) denir. Yani CSS’de dört ayrı Seçici türü vardır.

#### Harf Seçiciler

Bir bakıma bütün HTML unsurları Seçici sayılabilir. Yukarıdaki alıştırmada, HTML’in BODY, H1, H2, H2, P ve A etiketlerini seçici olarak kullandık ve biçimlendirdik. Bunun gibi HTML’in metin biçimlendiren unsurlarına stil komutları sağlayan Seçicilere, Harf Seçici (Type Selectors) denir. Bu Seçiciler için kullanabileceğiniz özellikleri veren yüklemler (örneğin, unsurun hangi harfle veya harf ailesiyle gösterilmesini belirleyen FONT-FAMILY yüklemi gibi) başka unsurlar için de kullanılabilir. Bu nedenle bu seçicilerle neleri kontrol edebileceğinizi bütün seçicileri gördükten sonra ele alacağızb

#### Sınıf Seçiciler

İkinci grup Seçici’ye Sınıf Seçiciler (Class Selectors) denir. Hayalgücünüzün imkan verdiği kadar Sınıf Seçici oluşturabilirsiniz. Örneğin “kırmızı” diye bir sınıf oluşturup, bu sınıfın font rengini kırmızı yapıp, dikkat çekmek istediğiniz kelimeyi, cümleyi veya paragrafın etiketini bu sınıfa bağlayabilirsiniz. Bu stilin komutu şöyle yazılır:

.kirmizi { COLOR: red }

“Kirmizi” kelimesinin başındaki nokta’ya dikkat edin. HTML sayfanızda diyelim ki bir başlığı kırmızı yapmak istiyorsunuz:

<h1 class=”kirmizi”>Bu başlık kırmızı olacak</h1>

Ya da bir paragrafın tümünü kırmızı renkle göstermek istiyorsunuz:

<P class=.kirmizi>Bu paragrafın tümü kırmızı gösterilerek, dikkati hemen çekecektir.</p>

Sınıf Seçicileri, CSS dosyasında veya HTML’in içindeki STYLE bölümünde müstakil olarak oluşturabileceğiniz gibi, bir etikete bağlı olarak da oluşturabilirsiniz:

h1.kirmizi { COLOR: red }

Fakat bu durumda “kırmızı” sınıfını sadece H1 etiketi ile kullanabilirsiniz.

#### Kimlikli Seçiciler

Üçüncü grup seçici ID Selectors (Kimlik Kazandırılmış Seçiciler) adını alır ve yine hayalgücünüzle sınırlı olarak istediğiniz kadar ID Selector oluşturabilirsiniz. Örneğin:

#mavi { COLOR: blue }

#icerden { text-indent: 2cm }

kimlikli seçicilerdir. Başlarındaki “#” işaretine dikkat ediniz. (Bu işaretten sonraki isim bölümü mutlaka harfle başlamalıdır; ama içinde rakam ve kesme çizgisi kullanılabilir.) Bu seçicilerden HTML’de yararlanmak için, adlarıyla hitabedilmesi gerekir:

<P ID=icerden>Bu paragraf diğerlerine oranla 2 sm içerden başlar<-p>

<P ID=mavi>Bu paragraf mavi olarak gösterilir</p>

Bu seçiciyi kullanırken, aynı etikete iki ayrı kimlik veremeyeceğinizi unutmayın.

#### Sınıfımsı Seçiciler

Üçüncü grup seçicilere Sınıfımsı Seçiciler (Pseudo-classes) adı verilir; çünkü kendi başlarına sınıf gibi göründükleri halde ancak bir etiketin belirli durumlarına uygulanabilirler. Bu seçici grubu şimdilik sadece iki etikete uygulanabilir:

A etikeninin üç durumu olabalir ve bunları sınıfımsı seçicilere konu yapabiliriz. Hatırlıyorsunuz, A etiketi (Anchor) sayfalarımızı, paragraflarımızı, cümle veya kelimelerimizi ya da grafiklerimizi bir yerlere bağlamakta kullanılırdı. Bu bağın üç durumu olabilir: Link (henüz gerçekleşmemiş) Visited (daha önce bağ kurulmuş) ve Active (üzeri tıklandığı anda). Şimdi bu durumlara uygun üç CSS etiketi yazalım:

A:link { COLOR: green }

A:active { COLOR: red }

A:visited { COLOR: blue }

Bu durumda ziyaretçinin ekranında A etiketlerimiz yeşil olarak gösterilecek, kullanıcı herhangi bir bağlantıyı tıkladığında bağlantı unsuru (kelimesi veya kelimeleri) kırmızıya dönecek; daha sonra sayfamıza geri geldiğinde bu kelimeler mavi olarak gösterilecektir.

Sınıfımsı etiketin kullanılabileceği şimdilik bir diğer durum ise başlık veya metin gibi bir etiketin ilk satırı veya ilk kelimesinin özelliklerini kontrol eden seçicidir. Örneğin:

P:first-line { font-variant: small-caps; font-weight: bold }

P:first-letter { font-size: 300%; float: left }

Bu seçicilerle oluşturulan etiketlere HTML’in içinde şöyle gönderme yapılır:

<P><P:first-line><P:first-letter>B</P:first-letter>izler, inandığımız için ve bilinçli olarak harf</P:first-line> tasarımcısıyız..... </P>

CSS’in ikinci sürüm standartları ile yeni yeni “durumlar, sınıfımsı oluşturmaya müsait sayılmaya başlamış bulunuyor. Bunun için [WWW.W2C.ORG](http://www.w2c.org/) adresini ziyaret ederek, gelişmeleri öğrenebilirsiniz.

#### Bağlamsal Seçiciler

Dördüncü son grup seçiciler, bir HTML etiketinin her zaman değil de belirli bir bağlamda belirli stiller almasını istediğimizde kullandığımız Contextual Selectors (bağlamsal Seçiciler) grubudur. EM (Emphasis) etiketi, uygulandığı başlık veya paragraf gibi bir etiketi italik yaparak belirginleştirir. Fakat diyelim ki bu etiketi paragraf etiketi ile birlikte (paragraf bağlamında) kullandığımızda işaretlenen yerin mavi, başlık bağlamında kullandığımızda yeşil yapmasını istiyoruz. Bunun için CSS bölümünde bu etiketi P ve H1 bağlamlarında tanımlarız:

P { COLOR: black; FONT-FAMILY: 12pt; TEXT-INDENT: 1cm}

P EM { COLOR: blue}

H1 { COLOR: #008080; FONT-FAMILY: 26 pt serif}

H1 EM { COLOR: red}

Sonra, metinde H1 etiketi içinde EM etiketi kullanırsanız. işaretlenen kelimeler kırmızı, paragraf etiketi içinde EM kullanırsanız işaretlenen kelimeler mavi olacaktır.

### Denetlenebilir Özellikler

HTML’de unsurların stil özelliklerini nasıl ve ne gibi bir yöntemle belirleyeceğimizi gördük. Bu arada verdiğimiz örneklerle, “font-family,” “margin-left,” “color” gibi, hangi özellikleri belirleyebileceğimiz hakkında da bir fikrimiz oldu. Fakat denetlenebilir özellikleri toplu halde ele alalım:

#### Font Özellikleri:

Harf ailesi: “FONT-FAMILY:” şeklinde kullanılan bu yüklemle, uyguladığınız stilin harf ailesini seçebilirsiniz. İfadenin karşısına font ailesinin adını yazabileceğiniz gibi, “serif” (ör. Times), “sans-serif” (ör. Arial), “cursive” (ör. Zapf-Chancery), “fantasy” (ör. Western), “monospace” (ör. Courier) de yazabilirsiniz. Bu satırda birdenf azla unsur, virgülle ayrılarak yaçzılabilir. İyi bir uygulama, önce tercih ettiğiniz belirli bir fontun, ardından bu font ailesinin adını ve nihayet türü yazmaktır. Örnek:

P { FONT-FAMILY: “New Century School Book”, Times, serif }

P { FONT-FAMILY: “Arial Black”, Helvetica, sans-serif }

Harf stili: “FONT-STYLE:” şeklinde kullanılan bu yüklemle, harfin normal, italik veya yatık olmasını sağlayabilirsiniz. (İtalik harflerin mutlaka öne yatık olması gerekmez! Ama çoğu italik harf, öne yatıktır.) Örnek:

H1 { FONT-STYLE: normal }

H2 { FONT-STYLE: italic }

H3 { FONT-STYLE: oblique }

Harf türü: “FONT-VARIANT:” şeklinde kullanılan bu yüklemle, harfin normal veya küçük harf boyunda ama büyük harf biçiminde olması sağlanabilir:

H1 { FONT-VARIANT: normal }

H2 { FONT-VARIANT: small-caps }

Harf ağırlığı: “FONT-WEIGHT:” şeklinde kullanılan bu yüklemle, fontun normal, siyah, koyu, daha koyu, dana açık olması sağlanabilir. Verilebilecek değerler, “normal,” “bold,” “bolder,” “lighter” olabileceği gibi, 100, 200, 300, 400, 500, 600, 700, 800 veya 900 olabilir. Burada 100-300 ince çizgili harf, 400-500 kalın çizgili harf, 600-900 çok kalın çizgili harf sayılır. Örnek:

H1 { FONT-WEIGHT: normal }

H2 { FONT-WEIGHT: bold }

Harf ölçüsü: “FONT-SIZE:” şeklinde kullanılan bu yüklemle, fontun büyüklüğünü belirleyebilirsiniz. Bu, ya mutlak veya göreli olabilir. Mutlak büyüklüklür ya punto, santimetre veya inç cinsinden belirli bir rakam (ör. 12 pt, 1cm) veya en küçükten en büyüğe doğru olmak üzere, “xx-small,” “x-small,” “small,” “medium,” “large,” “x-large,” “xx-large” olabilir. Göreli büyüklükler ise bir önceki fonta göre daha büyük anlamına “larger” veya daha küçük anlamına “smaller” olabileceği gibi, bir önceki harf büyüklüğünün yüzdesi olarak verilebilir. Tarayıcı programların harf ölçüsü konusunda ya arızalarla donanmış bulunuyor; ya da ölçüleri yorumlamaları birbirinden farklıdır. Bu nedenle, en emin yol harf ölçüsü olarak punto kullanmaktır. Örnek:

H1 { FONT-SIZE: 12pt }

H2 { FONT-SIZE: 90% }

(Yüzde işaretinin rakamın önünde değil, arkasında olduğuna dikkat ediniz.)

Harf: “FONT:” şeklindeki bu yüklemle bir çok font özelliği birden verilebilir. Bu ifadenin karşısına harf stili, türü, ağırlığı, ölçüsü ve ailesi ile bu harfin kullanıldığı satırın satır yüksekliği toplu olarak belirtilebilir. Örnek:

P { FONT: italic bold 12pt/14pt Times, serif }

#### Renk ve Zemin Özellikleri:

Renk: “COLOR:” şeklindeki bu yüklemle herhangi bir unsurun renk özelliğini belirleyebilirsiniz. Renk adları veya kodlarını daha önce ele almıştık. Örnek:

H1 { COLOR: blue }

H2 { COLOR: #000080 }

Zemin Rengi: “BACKGROUND-COLOR:” şeklindeki bu yüklemle herhangi bir unsurun arkasındaki zemin rengini belirleyebilirsiniz. Unsurun kendi rengi ile zemin renginin farkını görebilmek için daima COLOR yükleminden sonra kullanılması iyi bir uygulama olur. Örnek:

H1 { BACKGROUND-COLOR: blue }

Zemin grafiği: “BACKGROUND-IMAGE:” şeklindeki bu yüklemle herhangi bir unsurun arkasındaki zemine koymak istediğiniz görüntüyü belirleyebilirsiniz. Unsurun kendi zemin rengi ile zemine konacak görüntünün birbirini örtmemesi için ardarda kullanılması doğru olur. Zemin görüntüsünün yerini belirten ifade için “url...” ifadesi kullanılır. Bu ifadenin farklı türleri için örneğe dikkat ediniz:

H1 { BACKGROUND-IMAGE: url(/images/grafik1.gif }

P { BACKGROUND-IMAGE: url([http://www.benimsite.com/](http://www.benimsite.com/)zemin.gif }

Zemin: Zemin rengi ve zemin görüntüsü komutları, çeşitli tarayıcılar tarafından farklı yorumlandığı ve bu nedenle her zaman aynı sonucu alamayacağınızı dikkate alarak, hepsinin aynı şekilde yorumladığı ve “BACKGROUND:” şeklinde yüklem daha kullanışlı olabilir. Bu ifadenin karşısına renk, grafik, tekrar etme oranı, zemini oluşturduğu nesneye bağlı olup olması ve pozisyonu belirten değerler yazılır. Tekrar oranı, (background-repeat) sayfanızın bütün ebadından küçük bir grafiği zemin yapmaya kalktığınız zaman bu grafiğin sayfanın tümünü doldurabilmek için ne kadar tekrar edilmesini istediğini belirter. Bu değeri kullanarak, sayfanın bir kısmının zeminini boş bırakabilirsiniz. zeminin üzerindeki unsurlara bağlanmasını veya bağlanmamasını sağlayan (background-attachment:) zeminin üzerinde unsurla birlikte sayfada aşağı yukarı oynamasını veya oynamamasını belirler. Paragraf, başlık ve ölçüsü belli unsurların (örneğin, IMG, INPUT, TEXTAREA, SELECT gibi) zemini olacak görüntülerin alanın neresine ne de ölçüde konacağını zeminin pozisyon (background-position:) yüklemi belirleyebilirsiniz. Bu yüklemlerin yazılış biçimi ve değerler için örneklere bakınız:

BODY { BACKGROUND: white url(/images/grafik1.gif }

P { BACKGROUND: bule url(/images/grafik1.gif no-repeat bottom right}

Pozisyon değerleri, üstte solda (left top), üstte ortada (top center), üstte sağda (top right) olabileceği gibi, ortada ortalanmış (center center), ortada sağda (center right) veya ortada solda (center left), ya da altta solda (bottom left), altta ortada (bottom center) ve altta sağda (bottom right) olabilir.

#### Metin Özellikleri:

Kelime aralıkları: “WORD-SPACING:” yüklemi ile kelimelerinin arasına konulmasını istediğiniz ilave boşlukları belirtebilirsiniz. Burada kullanılan ölçü kullanılan fontun en geniş hargi olan “m” harfinin ondalık bölümüdür. Örnek:

P { WORD-SPACING: normal }

H1 { WORD-SPACING: 0.2em }

H2 { WORD-SPACING: -0.4em }

Harf aralıkları: “LETTER-SPACING:” yüklemi ile harflerin arasına konulmasını istediğiniz ilave boşlukları belirtebilirsiniz. Burada kullanılan ölçü de “m” harfinin ondalık bölümüdür. Örnek:

P { LETTER-SPACING: normal }

H1 { LETTER-SPACING: 0.2em }

H2 { LETTER-SPACING: -0.3EM }

Metin süsleme: “TEXT-DECORATION” yüklemi ile bir metnin altını çizdirebilir (underline), üstünü çizdirebilir (overline), veya ortasına çizgi koydurabilirsiniz (line-through), veya bir görünüp, bir kaybolmasını sağlayabilirsiniz (blink). Bunu, altı normal olarak çizilen A (Anchor) etiketiyle verdiğiniz bağlantı kelimelerinin altının çizilmemesi için de kullanabilirsiniz. Örnek:

H3 { TEXT-DECORATION: blink }

A:link, A:visited, A:active { TEXT-DECORATION: none }

Metnin bloklanması: “TEXT-ALIGN” yüklemi ile bir metni sağa (right), sola (left) veya ortaya (center) bloklayabilirsiniz. Örnek:

H3 { TEXT-ALIGN: left }

H1 { TEXT-ALIGN: center }

Birinci satırın içerden başlaması: “TEXT-INDENT” yüklemi ile bir metnin birinci satırını vereceğiniz ölçüde içerden başlatabilirsiniz. Örnek:

H3 { TEXT-INDENT: 1cm }

Satır Yüksekliği: “LINE-HEIGHT” yüklemi ile bir metnin satırları arasına konacak boşluğu vereceğiniz yüzde ölçüsü ile normal satır yüksekliğine göre belirleyebilirsiniz. Örnek:

H3 { LINE-HEIGHT: 200% }

H1 { LINE-HEIGHT: 350% }

(Bu ölçü yüzde 100’ün altına düşerse, satırlar birbirinin üzerine bineceği için okunamaz hale gelir.)

#### Konum (Pozisyon) Özellikleri

CSS kurallarının içinde yer almakla birlikte HTML unsurlarının tarayıcının ekranında, konumunu, nereye konulacağını, yani pozisyonunu ve ilk konumun daha sonraki değişme tarzını belirleyen yüklemler, son zamanlarda CSS-P (Cascading Style Sheets-Positioning) şeklinde kendi adıyla anılmaya başladı. Bu grupta yer alan ve unsurlarınızın tarayıcı ekranında yer alacağı konum kontrol yüklemlerini tek tek ele alalım:

Konum: “POSITION:” yüklemiyle belirlenen konum, sabit (static) olabileceği gibi mutlak (absolute) veya göreli (relative) olabilir. Mutlak (absolute) konum verilmiş bir unsur, HTML’in diğer içeriği nedeniyle asla yer değiştirmez; kendisine verilen üst (top) ve sol (left) değerlere göre mutlak bir yerde kalır. Buradaki ölçü pixel cinsinden, tarayıcının HTML sayfasını gösterdiği alanın sol üst köşesi 0-0 kabul edilerek verilir. Örneğin “top: 10 px; left: 20px” şeklindeki bir ölçü, bu unsurun tarayıcının HTML alanının sol üst köşesinden 10 pixel aşağı ve sol kenarından 20 pixel sağa doğru yerleşmesini sağlar. Sabit (Static) konum, yeri belirlenmek istenen unsurun, HTML’in diğer içeriğine göre, nereye geliyorsa, oraya yerleşmesini sağlar. Göreli (Relative) konum ise verilecek ölçülere göre belirlenecek yer, bir önceki unsurun konumunun bittiği yerden itibaren hesaplanır. Örnek:

<SPAN STYLE="position:static; background-color:#90EE90">Yeşil bir satır. Konumu: sabit</SPAN>

<DIV STYLE="position:absolute; top:60px; left:60px; background-color:#ADD8E6">Mavi bir satır. Konumu: mutlak. Üstü 60, sol kenarı 60 santim içerden.</SPAN>

Görünürlük: CSS-P, “VISIBILITY:” yüklemi ile, biçimlendiren unsurun gizlenmiş (hidden), veya görünür (visible) olmasını sağglayabilir veya görünürlüğü içinde bulunduğu nesneden miras almasını (inherit) sağlayabilir. Yani ana unsur görünüyorsa içinde yer alan bu unsur da görünür, ana unsur görünmüyorsa bu unsur da görünmez. Örnek

<div id="Yazi01" style="position:absolute; left:68px; top:60px; width:147px; height:164px; z-index:1; visibility: visible; background-color: #FFCCFF">Bu Mutlak konuma sahip, zemini pembe bir yazıdır. Adı “Yazi1” olan bu kutu her durumda görülür</div>

Katman Enhdeksi: CSS-P, “Z-INDEX:” yüklemi ile bir unsurun tarayıcı tarafından hangi katmanda gösterilmesini tayin etme olanağı sağlar. Bir sayfada, DIV veya SPAN etiketi ile oluşturulmuş nesne varsa, onların katman endeksine bakarak, hepsini belirli bir kata koyar. Yanyana gelen nesnelerin kaçıncı katta olduğu önemli olmayabilir; ancak nesneler üst üste geliyorlarsa, hangisinin hangi altta, hangisinin ortada, hangisinin üstte duracağı önem taşıyabilir. Verilecek değer 1, 2, 3 şeklinde bir sıra numarasıdır. 1, en alttaki katmandır; diğerleri sırayla onun üzerindeki katları gösterir. Örnek

<div id="Yazi01" style="position:absolute; left:68px; top:60px; width:147px; height:164px; z-index:1; visibility: visible; background-color: #FFCCFF">Pembe kutudaki bu yazı altta..</div>

<div id="Yazi2" style="position:absolute; left:132px; top:120px; width:208px; height:206px; z-index:2; background-color: #FF3300">Kırmızı kutudaki bu yazı üstte</div>

Konum belirleyen yüklemler arasında eni boyu belirlenmiş bir nesneye koyduğunuz metnin taşması halinde taşan yazının gösterilip gösterilmeyeceği, veya bir nesnenin içine konulan unsurun hangi bölümlerinin gösterilip, hangi bölümlerinin kesileceğini belirleyen diğer iki kontrol ögesi daha vardır. Bunların tarayıcı yorumları sürümden sürüme değiştiği için ayrıntılarını W3C Internet alanında bulabilirsiniz.

#### Diğer Özellikler

Stil sayfalarını veya HTML’in baştarafına koyacağınız stil bölümleri ile CSS’in diğer bazı biçimlendirme imkanlarını da kullanabilirsiniz. Bir metnin veya diğer unsurun içinde yer aldığı varsayılan kutunun etrafına çerçeve koymak ve bu çerçevenin rengini, çizgi kalınlığını, çizgilerin içinde ve dışında bırakılacak marjları, bu kutuların zeminini, zemine konacak grafiği belirlemek, kutuların ekrandaki yerini tayin etmek mümkündür. Giderek sayıları artan bu yüklemleri toplu olarak W3C’nin Internet alanında heran bulabilirsiniz. Bunların arasında sık sık kullanılan yüklemleri sıralayalım.

Marjlar: Bir HTML unsurunun üstünde (MARGIN-TOP), sağında (MARGIN-RIGHT), solunda (MARGIN-LEFT) ve altında (MARGIN-BOTTOM) bırakılacak marj boşlukları ya ayrı ayrı ya da toplu olarak belirlenebilir. Toplu belirleyecekseniz, değerlerin sırası üst, sağ, sol, ve alt olarak okunacaktır. Örnek:

P { MARGIN-TOP: 1cm }

P { MARGIN-RIGHT: 2cm }

P { MARGIN-LEFT: 2cm }

P { MARGIN-BOTTOM: 1cm }

P { MARGIN: 1cm 2cm 2 cm 1 cm }

### Bir Nesne Yapalım

#### Sabit Nesneler

Evet bu kadar bilgiden sonra sıra yine uygulamaya geldi. Önce yapacağımız işin stratejisini belirleyelim: Bir sayfada iki katman oluşturacağız; alt ve üst katlara farklı grafikler koyacağız.

Şimdi iki grafik yapalım; birinci içinde “Alt Grafik” diğerinde “Üst Grafik” yazısı bulunsun. Eğer grafikle uğraşmak istemiyorsanız, 100’e 40 pixel civarında birbirinden ayırt edebileceğiniz iki küçük grafik dosyası da işimizi görür. Şimdi bunları HTML sayfasına öyle bir şekilde koyacağız ki, sayfanın stil etiketiyle oynayarak grafiklerin yerlerini değiştireceğiz. Ve böylece HTML’de katman kavramını kullanmış olacağız.

Düz yazı programınızı açın ve başlayın yazmaya:

<html>

<head>

<title>Dinamik HTML</title>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

<style type="text/css">

<!--

#alt {position:absolute; top: 135px; left: 90px; width: 102px;}

#ust {position:absolute; top: 110px; left: 60px; width: 102px;}

-->

</style>

</head>

Şimdilik burada duralım. Farkettiğiniz gibi biraz önce öğrendiğimiz <STYLE> etiketine yer veriyoruz. STYLE etiketinin içinde iki stil türü oluşturuyoruz: Alt ve üst.

////////////////////////////////////////////////////NOT///////

“Üst” mü, “Ust” mu?

Stilleri oluştururken, aslında “alt” değil “#alt” ve “üst” değil “#ust” kelimelerini kullandığımız dikkatinizi çekmiş olmalı. Sayfalarınızın Türkçe’yi destekleyen işletme sistemi olmayan, örneğin Türkiye kullanıcıların bilgisayarlarında acaip sonuçlar vermemesi için, sistem değişkeni olarak tarayıcı ve dolayısıyla MacOS, Windows veya Unix gibi işletme sistemi tarafından kullanılacak isimlerin içinde Türkçe karakter kullanmaktan kaçınmak iyi bir programlama terbiyesidir. İçerik bölümünde tarayıcıların desteklemesi şartıyla istediğiniz dili, istediğiniz karakteri kullanabilirsiniz. Bunun için tek zorunluk, içerikte kullandığınız dili HTML’in başlangıç bölümünde bir META etiketle belirtmektir. Örneğin,

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

böyle bir bildirimdir ve tarayıcıya, bu dosyadaki bilgilerin Türkçe kodlama sistemiyle yorumlanması talimatını vermektedir.

///////////////////////////////////////////////////////

////////////////////////////////////////////////////NOT///////

“<!—“ ve “-->”

Bir etiketin içinde yer alabilecek “<!—“ ve “-->” şeklindeki etiketler HTML dilinin yorum etiketleridir; bu etiketlerin arasındaki şeyler, tarayıcıların eski sürümleri tarafından dikkate alınmaz. Bu önlemi almazsanız, örneğin Netscape veya IE’ın eski sürümleri, stil komutlarını içerik gibi ekranda gösterecektir. Bu nedenle <STYLE> etiketini yazar yazmaz, “<!—“ ve “-->” ile </STYLE>’ı yazmayı unutmayın.

///////////////////////////////////////////////////////

Burada iki stil oluşturuyoruz: birine “alt” diğerine “Üst” adını veriyoruz. Kimliklendirilmiş seçiciler kullandığımıza dikkat edin. Daha sonra oluşturacağımız iki nesneyi bu stillere bağlayacağız ve bu stillere adlarıyla gönderme yapacağız. Oluşturacağımız iki nesnenin ekranda mutlak bir yere konulmasını istiyoruz; Onun içinde her iki stile de mutlak bir konum veriyoruz ve yerlerini, pixel ölçüler vererek belirliyoruz.

Nesnelerimiz vücut bulduğu zaman alacakları şekilleri böylece belirledikten sonra sıra nesneleri oluşturmaya geldi. Düz yazı programınızda devam edin yazmaya:

<body bgcolor="#FFFFFF">

<h1>Dinamik HTML--Katman Örneği</h1>

<div id="alt"><img src="alt.gif"></div>

<div id="ust"><img src="ust.gif"></div>

</body>

</html>

Dosyanın tümünü “div01.htm” adıyla kaydedin ama programı kapatmayın; kaydettiğiniz dosyayı tarayıcınızda açıp bakın. Karşınızda şuna benzer bir görünüm olacaktır:

reh073.tif

Düz yazı programınızda kimlendirilmiş seçicilerin kimliklerine yer değiştirin; yani STYLE etiketi içinde “#ust” kelimesini “#alt”, “#alt” kelimesini de “#ust” yapın; dosyayı “div02.htm” adıyla yeniden kaydedin ve bu kez bu dosyayı açıp bakın. Farkı görebiliyor musunuz?

reh074.tif

Aynı sonucu, aşağıda nesneleri oluşturduğunuz bölümde, nesnelerin kimliğini değiştirerek de elde edebilirsiniz. Bunun içinde ilgili bölüm şöyle olacak:

<div id="ust"><img src="alt.gif"></div>

<div id="alt"><img src="ust.gif"></div>

İki nesnemizin ekrandaki yerini istediğimiz gibi değiştirebiliyoruz. Peki içinde Üst yazılı grafiği alta, Alt yazılı grafiği de üste getirebilir misiniz? Tabiî. Bunun için Katman endekslerini vermemiz yeter. Nesnelerin stillerini tanımladığımız iki satıra endeks sayılarını ekleyelim:

#ust {position:absolute; top: 135px; left: 90px; width: 102px; z-index:1 }

#alt {position:absolute; top: 110px; left: 60px; width: 102px; z-index:2 }

Dosyayı “div3.html” adıyla kaydedelim. Tarayıcıda bakalım. İşte görünüm:

reh075.tif

“Ust” stilinin endeksini 2, Alt stilinin endeksini 1 yaparsanız, Alt isimli nesneniz, altta mı kalır, üstte mi?

Bu ev ödevi ile, HTML’de katman kavramına giriş yapmış ve bunu sayfada uygulamış bulunuyoruz. Stil kağıdını değiştirerek, nesnelerimizi hareket ettirmeyi de öğrendik.

Burada nesnelerimizi, DIV (Division) etiketi ile oluşturduk. Ama aynı işi SPAN etiketi ile de yapabiliriz. İkisinin arasındaki başlıca fark, DIV etiketinin içine koyacağınız herşey, sayfada kendi başına bir blok oluşturmak zorundadır. Oysa SPAN etiketi ile oluşturacağınız bir nesne, sıradan bir paragrafın içinde olabilir ve paragrafı bölmeden kalabilir.

Şimdi, bir iki nesneyi, Javascript dilini kullanarak, sayfamızın görünümünü ziyaretçinin faresini hareket ettiriş tarzına göre değiştirmeye çalışalım.

#### Rollover Etkileri

Peşinde olduğumuz etkiye, Webcilerin dilinde Rollover Etkisi deniliyor. Yani bir unsur, bir yazı, bir stil, bir grafik siliniyor, yerini başka bir unsur, başka bir yazı, başka bir stil, başka bir grafik alıyor; biri dönüp, gidiyor (roll-over) yerini başka biri alıyor. Bu hareketliliği başlatan şey, ya da hareketin tetiği, ziyaretçinin fare simgesini ekranda belirli bir yere getirmesi; sayfanın değişmesi, ziyaretçinin klavyesinde bir tuşa basması, sayfaya yerleştirdiğimiz bir müzik dosyasının çalınmasının tamamlanması, vs. olabilir.

Konu, HTML’den çok, daha geniş boyutlu DHTML ilkelerine girdiği için, burada Rollover etkisini kullanarak, örneğin ziyaretçinin bulunduğu yerde saatin kaç olduğuna bakarak, sayfamızın içeriğini bu bilgi ışığında belirlemek gibi, Visual Basic Script (VBScript) veya Javascript dilinin ayrıntılarına giremeyiz. Ama bu dillere başvurmadan, Netscape Navigator ve Internet Explorer’ın dördüncü sürümlerinin bazı becerilerinden yararlanarak basit bir etki oluşturmayı öğrenebiliriz.

////////////////////////////////////NOT//////////////////////

Javascript ve VBScript

Etkili Web sayfaları yapmak istiyorsanız, Dinamik HTML’in ana dili haline gelen bu iki dili öğrenmek zorundasınız. Java dili ile hiç ilgisi olmayan ama benzer bir isim taşıyan Javascript dili, Netscape firması tarafından Web sayfalarının bilgisayar programı dillerindeki “Eğer .... ise ... şunu yap! Değilse bunu yap!” şeklindeki karar yeteneğini kazanması için geliştirildi ve derhal Microsoft firması tarafından Internet Explorer’a uygulandı. Bu dil, Netscape’in iddiasına göre, Macintosh, Windows ve Unix işletim sistemlerinde çalışabilecekti. Ancak Microsoft Windows ortamının doğal imkanlarını kullanan Visual Basic dili ile bir Windows programının daha çok yetenek kazanabileceğini gözönünde tutarak, bu dilin Web sürümünü yaptı ve VBScript adını verdi. Netscape firmasının tarayıcı programı, şu ana kadar bu dili tanımaktan mahrum bulunuyor. Bu nedenle Web tasarımcısı olarak, DHTML özellikleri taşıyan Web sayfaları yaptığınız zaman, bu sayfaların hem Netscape, hem de Internet Explorer programları tarafından aynı şekilde tanınmasını istiyorsanız, Javascript dili ile sınırlı olduğunu bilmelisiniz.

/////////////////////////////////////////////////////////

Şimdi, bir sayfa yapalım; sayfaya koyacağımız Link unsurları, kullanıcı fare simgesini bağlantı kelimelerinin üzerine getirdiği anda, hem biraz büyük fontla gösterilsin, hem de renk değiştirsinler. Yapacağımız sayfaya koyacağımız bu etki, Netscape’in hiç bir sürümünde görülemez. Bu nedenle aşağıdaki örneği Internet Explorer ile sınamanız gerekir.

Önce sayfamıza, giriş ve STYLE bölümlerini yazalım:

<HTML>

<HEAD>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</HEAD>

<TITLE>Dinamik HTML</TITLE>

<style type="text/css">

<!--

P {font-family: Arial, Verdana, Helvetica; font-size: 12pt; line-height:13pt}

H1 {font-family: arial, helvetica; font-size: 16pt; color: #578D99; line-height:18pt}

H2 {font-family: arial, helvetica; font-size: 14pt; color: red; line-height:16pt}

H3 {font-family: arial, helvetica; font-size: 24pt; color: red; line-height:28pt}

A {text-decoration:none; font-weight: bold}

.yeni {color:red; font-weight:bold; font-size:120%; letter-spacing:0px; text-transform: none}

.normal {color:#578D99}

-->

</style>

</HEAD>

Farketmiş olacağınız gibi, burada STYLE bölümünde HTML’in temel etiketlerinin varsayılan özelliklerini değiştiriyoruz ve iki yeni “Sınıf” seçicisi oluşturuyoruz: “.yeni” ve “.normal.” (HTML’in stille ilgili komutlarını, özellikle seçici isimleri büyük harf-küçük harf bakımından hassas olduğu için burada yazdığınız sınıf isimlerini aşağıda aynen kullanmak zorundasınız.)

Şimdi HTML’in geri kalan bölümünü yazalım:

<BODY TEXT="#000000" BGCOLOR="#CCFFFF" LINK="#578D99" VLINK="#999999" ALINK="#FFFFFF">

<h1>Web Tasarımında Gözetilecek İlkeler:</h1>

<p><a href="ogut1.htm"><SPAN onmouseover = "this.className = 'yeni'" onmouseout = "this.className='normal'" class=normal>Grafikle İlgili İlkeler</span></a></p>

<p><a href="ogut2.htm"><SPAN onmouseover = "this.className = 'yeni'" onmouseout = "this.className='normal'" class=normal>İçerikle İlgili İlkeler</span></a></p>

<p><a href="ogut3.htm"><SPAN onmouseover = "this.className = 'yeni'" onmouseout = "this.className='normal'" class=normal>Davranış Kuralları</span></a></p>

</BODY>

</HTML>

Burada ise Javascript dışında şimdilik sadece IE4’ün anladığı bir komut olan “onmouseover” (Fare üzerine geldiğinde) ve “onmouseout” (Fare üzerinden gittiğinde) komutlarını kullanarak, A etiketlerinin üzerine fare simgesi geldiğinde “yeni” sınıfının özelliklerini almasını, fare simgesi üzerinden çekildiği anda “normal” sınıfına geçmesini bildiriyoruz. A etiketlerimizi STYLE bölümünde “normal” sıfınının özelliklerine kavuşturduğumuz farketmiş olmalısınız. Bu sayede A etiketi ile işaretlenen metin, tarayıcının varsayılan stili olan altı çizgili mavi metne dönmeyecektir.

Bir unsurun HTML’in tanıdığı “Nesne” halini alabilmesi için ya DIV ya da SPAN etiketleri içine alınması gerektiğini söylemiştik. SPAN etiteki, DIV’den farklı olarak, içine aldığı ve Nesne yaptığı unsuru sayfada yeni bir paragraf haline getirmez, demiştik. Nitekim, deremiş olmak için, A etiketlerinden önceki <p> ve </p> etiketlerini kaldırır, yerine bir aralık koyarsanız, SPAN ile oluşturduğunuz unsurların yanyana dizildiklerini göreceksiniz.

Hazır deneme yapmaya başlamışken, bir de STYLE bölümünde, “.yeni” sınıfının “font-size:120%” şeklindeki font ölçüsü komutu ile oynayıp, yüzde 120’yi, örneğin yüzde 160 yapın!

Buradaki şekliyle bu sayfa ve oluşturduğumuz etki, IE ekranında şöyle görünüyor:

reh076.tif

reh077.tif

Bu kitapçığın kapsamı, dinamik HTML’in diğer imkan ve yeteneklerini ele almaya elverişli değil. Ama, Internet DHTML kılavuzları ile dolu. Ayrıca, WYSIWYG (Ekranda ne görürsen o sonucu veren) HTML editörleri de Dinamik HTML’in yeteneklerinden Javascript öğrenmeden yararlanma imkanı veriyor.

# Bölüm IV: HTML’de Form ve CGI

Internet, bilimadamlarının birbirlerine araştırmalarıyla ilgili rapor vermelerini sağlayan bir Ağlar-arası Ağ olarak başlamış ise de, bugün hemen herkesin, yararlı olsun, olmasın, her türlü bilgiyi alıp-verdiği başlıca alan haline gelmiş bulunuyor. Kimine göre, Internet, duragan bilgisayar ekrarınını televizyon ekranına çevirdiği için bu kadar cazip hale geldi. Kimine göre, Internet’in sırrı ulaşım ve talep etme kolaylığı getirmesinde. Her türlü mal ve hizmet, artık Internet’te yapazarlanıyor ve Internet yardımıyla edinilebiliyor. Ödemelerinizi Internet’te yapabilirsiniz. Bu grup, Güvenli HTML (SHTML) denen yeni bir protokolün yaygınlaşmasıyla, Internet’te elektronik ticaretin de artacağı kanısında.

Internet’in bu ikinci işlevi, yani Internet’in sadece Web sayfası sahibinin sunduğu bilgilerin ziyaretçi tarafından alınmasına yarayan tek yönlü bir yol değil de, ziyaretçinin de Web sayfası sahibine birşeyler gönderebilmesi, HTML’in Form başlığı altında toplanan imkan ve yetenekleri sayesinde mümkün oldu. Elektronik ticaret de, HTML’in FORM etiketinin kullanımından başka bir şey değil.

FORM, sizin Web tasarımcısı olarak sayfanıza koyacağınız ve içinde ziyaretçinin dolduracağı boşluklar veya ziyaretçinin yapacağı tercihleri belirteceği kutular bulunan ve en sonunda bu bilgileri size göndereceği bir düğme bulunan bir Web sayfasıdır. FORM, bir sayfanın içinde bir bölüm olabileceği gibi, başlıbaşına bir sayfa da olabilir. FORM, ziyaretçiye “girdi” yapma imkanı verebilir; vermeyebilir. FORM düz bir metin olabilir; resimlerle süslenmiş olabilir. Ne kadar işlenmiş olursa olsun, bütün HTML etiketleri gibi formlar da bir etiketle başlar ve biter. Şimdi bu bölümde <FORM>..</FORM> etiketinin arasını doldurmayı öğrenelim.

Bu arada bir uyarı notu: Oluşturacağınız form, ekranda çizilecek ve size başarılı bir form yapıp, yapmadığını görme imkanı verecektir. Ama formun gerçekten yapmasını istediğiniz işleri yapıp, yapmadığını sınamak için, örneğin altına koyacağınız Gönder düğmesine basmanızın bir faydası olmayacaktır. Çünkü HTML’de form, karşısında o formdaki bilgileri alıp bir şeyler yapacak bir program olsun ister. Bu programlar, genellikle Web Server dediğimiz, ziyaretçilere Web sayfalarındaki bilgileri sunan programların bir bölümüdür. En yaygın Web Server programları (Unix ortamında Apache, Windows ortamında Microsoft Internet Information Server, ziyaretçiden gelen form bilgisini alacak ve işleyecek “Web Server’a ortak Giriş Kapısı” diye adlandırabileceğimiz CGI (Commen Gateway Interface) oluştururlar ve burada ziyaretçilerden gelen formları işleyecek programlara yer verirler. Bu programlar genellikle CGI programı adıyla bilinir. Bu tür programları, Internet hizmeti yapmadan sadece formlarınızı sınamak amacıyla PC veya Macintosh bilgisayarlara koymak da mümkündür. Ancak bilgisayarınıza böyle bir CGI programı kurduğunuz taktirde formlarınızı bu programa “göndererek” sınayabilirsiniz.

## Formun Bölümleri

HTML formunun üç bölümü vardır. Bunlar, Web tasarımcısının formdan beklediği eylemin (Action) ne olduğunu gösteren ve ziyaretçinin tarayıcısına hitabeden bölümü; ziyaretçinin doldurması gereken boşluklar veya tercih etmesi gereken seçenekler; ve ziyaretçiye bu formun eylem komutunu harekete geçirme veya vaz geçme imkanı veren komut düğmeleri.

### Action ve Method

Web alanınızda bir form oluşturmak için kullanacağınız <FORM> etiketi, kullanıcının tarayıcı programına bu formdaki bilgileri ne yapması gerektiğine ilişkin talimatı da içerir. Bunun için FORM etiketinin içinde, tarayıcıya ACTION yüklemiyle bu formun doldurularak gönderilmesi halinde içindeki bilgilerin nerede, hangi adreste, hangi programa teslim edileceğini söylersiniz. HTTP protokolü Web Server ile ziyaretçinin bilgisayarı arasında iki tür iletişime imkan verdiği için bu bölümde tarayıcıya hangi yöntemi seçmesi gerektiğini de METHOD yüklemiyle bildirmeniz gerekir.

Dolayısıyla Form etiketinin yazılış kuralı şöyle olacaktır:

<FORM ACTION=”url” METHOD=POST veya GET>

Burada url harfleri yerine bu form ile gelecek bilgiyi işleyecek programın adresi bulunacaktır. Örneğin: “/cgi-bin/siparis.cgi”

CGI programları için aşağıda daha geniş bilgi bulacaksınız.

METHOD hanesine ya GET ya da POST yazabilirsiniz. Get ve Post, ziyaretçinin bilgisayarı ile Web Server arasında kurulacak HTTP prorotokolüne dayanan bağlantı, ziyaretçinin Server’a bu iki yöntemden birisiyle bilgi göndermesini sağlar. Aralarındaki fark, Get yönteminde bilgiler Web Server’da “querry\_string” denen değişkenin içine yazılırken, Post yönteminde bu bilgiler “stdin” değişkenine yerleştirilir. Server’larda ikinci değişken birincisinden çok yer tutar; yani Post yöntemiyle daha çok bilgi gönderilebilir. Web alanı işletmecileri giderek daha yüksek oranda Post yöntemini tercih ediyorlar. Gerçek bir form yaptığınız ve Web alanınıza koyacağınız zaman, Web alanınıza ev sahipliği yapan firmanın teknik yetkililerine, formlarınızda ACTION ve METHOD yüklemlerinin karşısına ne yazacağınızı sormanız gerekir.

Form etiketinin önüne form bilgisi ziyaretçinin bilgisayarından sizin Web Server’ınıza nasıl bir şifreleme yöntemi ile gelsin istiyorsanız, onu da yazabilirsiniz. Fakat bu bilgi Web Server programlarına göre değiştiği için burada böyle bir imkanın varlığını belirtmekle yetineceğiz. “ENCTYPE=”.....” şeklinde yazılan bu bölümü doldurmazsanız, varsayılan şifreleme yöntemi, HTTP’nin standart kodlama yöntemi olan MIME olacaktır.

### Doldurulacak Boşluklar ve İşaretlemeler

<FORM>...</FORM> etiktenin arasını ya kullanıcının dolduracağı boşluklar, ya da tercih yapmasına imkan veren listeler ve düğmelerle doldurmanız gerek. Bunu sağlayan başlıca kontrol elemanlarınız INPUT , SELECT ve TEXTAREA etiketidir. Şimdi bunları sırasıyla inceleyelim:

#### INPUT

INPUT etiketi ile ziyaretçiye, forma klavyesinden veya fare ile işaretlemek suretiyle bilgi girmesi imkanı veririz. Bu etiketi kullanmanın genel biçimi şöyledir:

<INPUT TYPE=”...” NAME=”...” VALUE=”...” SIZE=”...” MAXLENGTH=”...” SCR=”...” CHECKED”....”>

Şimdi bu etiketin kullanım ilkelerini kullanıcının yapabileceği işlere göre ayırarak inceleyelim:

· **Kullanıcının klavyesi ile bir metin girmesi için: **

TYPE=TEXT NAME=”...” VALUE=”...” SIZE=”...” MAXLENGTH=”...”

“Size” hanesi bu kutunun kullanıcının ekranında gösterileceği genişliği karakter olarak belirler; “Maxlenghth” hanesi ise kullanıcının girebileceği metnin uzunluğunu karakter olarak belirler. Bu haneyi koymaz ve bir değer vermezseniz, tarayıcı azami metin uzunluğunu 21 karakter olarak varsayar. Bu kutu ekranda gösterildiğinde içinde bir yazı olsun istiyorsanız, bunu “Value=...” hanesine tırnak içinde yazın. Daha sonra CGI programı düzeyinde bu bilgiyi bir veri bankasına işlemek, bir elektronik mektup içinde veya herhangi bir başka tarzda kullanmak istiyorsanız, bu alana “Name=...” hanesinin içine yazmak suretiyle isim vermeniz gerekir.

· **Kullanıcının parola girmesi için: **

TYPE=PASSWORD NAME=”...” VALUE=”...” SIZE=”...” MAXLENGTH=”...”

Metin girme kutusu ile aynı özelliklere sahiptir; fakat bu kutunun içine kullanıcının gireceği bilgiler ekranda gösterilmez yerine yıldız simgesi gösterilir.

· **Kullanıcının bir kutuya işaret koyması: **

TYPE=CHECKBOX NAME=”...” VALUE=”...” \[CHECKED\]

Ziyaretçi, bu komutla oluşturacağınız işaret kutusunun içine fare ile tıklamak veya klavyede aralık tuşuna basmak suretiyle bir çarpı işareti girer veya otomatik olarak konan işareti kaldırabilir. Bu kutuda işaret varsa, tarayıcı “Value=” hanesine yazacağınız bilgiler ve kutunun adını bir çift olarak Server’a gönderir. Kutuda işaret yoksa kutunun adı ve değeri Server’a gönderilmez. Bu kutuyu oluştururken mutlaka Name hanesine tırnak içinde bir isim girmeniz gerekir; yoksa gelecek bilgi hiç bir işinize yaramayabilir. Kutunun otomatik ohardak işaretlenmesini istiyorsanız, CHECKED kelimesine yer verin; istemiyorsanız, bu kelimeyi yazmayın. Bu suretle oluşturulacak kutunun ekranda otomatik şekilde bir yaftası olmayacaktır. Bu nedenle bu kutuyu oluşturmadan önce veya sonra bu kutunun ne işe yaradığını yazın.

· **Kullanıcının yuvarlak bir boşluğun içine siyah bir nokta koyması (Radyo düğmesi): **

TYPE=RADIO NAME=”...” VALUE=”...” \[CHECKED\]

İşaretlenecek yerin kare kutu değil de bir daire olması dışında bu unsurun bütün özellikleri ve ilkeleri CHECKBOX gibidir.

INPUT etiketi ile forma grafik veya gizli metin koymak da mümkündür. HTML 4 ile gelen ekranda kullanıcının fare simgesi ile tıklayabileceği düğme oluşturan BUTTON etiketi yerine, örneğin Gir ve Sil gibi kullanıcının bilgileri Server’a göndermesini veya doldurduğu bilgileri tümüyle silmesini sağlayan işlemler de bu etiketle yapılabilir.

#### SELECT

Bu etiketi kullanarak, formda bir kutu ve yanında bir aşağı ok oluşturabilirsiniz; kullanıcı aşağı oku tıklamak suretiyle açacağı listeden bir unsuru seçerek, kutunun içine yazılmasını sağlayabilir. Arzu ederseniz, bu unsurlardan birisi otomatik olarak seçilmiş olarak da gösterilebilir. Bu etiketin kullanım şekli şöyledir:

<SELECT NAME=”....” SIZE=”...” \[MULTIPLE\]>.....</SELECT>

Size hanesine 1, 2, veya 3 vs.. yazarak, ekrandaki kutunun kaç seçenek göstereceğini belirleyebilirsiniz. Bu hane konulmazsa, otomatik 1 seçenek varsayılır. Bu kutuda gösterilecek seçenekler, <SELECT....>..</SELECT> etiketlerinin arasına <OPTION> etiketiyle yazılır. (<OPTION> etiketi kapatılmaz.) Herhangi bir seçeneğin otomatik olarak seçilmesi için önündeki <OPTION> etiketinin içine SELECTED kelimesi konulur. Örnek:

<select name="Temas" size="1"><option selected>Lütfen bir tercih yapınız<option value="Telefon">Telefon<option value="EPosta">E Posta<option value="Gel">Şahsi Görüşme</select></p>

#### TEXTAREA

Metin kutusu, ziyaretçiye, Web Server’a uzun metin gönderme imkanı sağlar. bu etiketin kullanım şekli şöyledir:

<TEXTAREA NAME="..." rows=.. cols=..>Kutunun içine otomatik yazılması istenen metin buraya yazılır </TEXTAREA>

“Name=....” yüklemi ile metin kutusuna Server’a gelecek metnin işlenmesi ve kullanılması için gerekli ad verilebilir. “rows=” ve “cols=” yüklemlerinin karşısına verilecek rakamlarla bu kutunun formda kaç satır yüksekliğinde ve kaç harf genişliğinde bir yer alacağı belirtilir. Bu iki ölçünün kutuya girilecek metnin uzunluğu ile ilgisi yoktur.

### Gönder ve Sil düğmeleri

Formun mantıksal olarak sonuna, kullanıcının dolduğu bilgileri ve yaptığı tercihleri formu sunan Internet alanına göndermesini sağlayan bir Gönder, veya forma yazdığı bilgileri ve yaptığı tercihleri değiştirmek isteyenlerin tümüyle silebilmesi için bir Sil düğmesi konması gerekir. HTML 4 standartları ile Form’lara düğme (BUTTON) etiketi koymak mümkün oldu. Bundan önce formların, ziyaretçinin bilgisayarı tarafından Server’a gönderilmesi veya o ana kadar yazdıklarını tümüyle silmesi, INPUT etiketinin SUBMIT ve RESET yüklemleriyle kullanılması ile mümkündü.

Bunun için INPUT etiketi şöyle kullanılır:

<INPUT TYPE=SUBMIT NAME=Gonder VALUE="Gönder">

<INPUT TYPE=RESET NAME=Sil VALUE="Sil">

HTML 4 sayesinde tarayıcının otomatik düğme şekli yerine kendi rdüğme grafiklerimizi kullanabileceğimiz gibi sayfaya birden fazla ve değişik maksatlarla düğme koyabiliriz. Ancak her düğmenin ayrı ismi ve ayrı değeri olması gerekir. Bu kodu şöyle yazabiliriz:

<BUTTON TYPE=SUBMIT NAME=Gonder VALUE="Gönder"><IMG SRC=”gonder.gif></BUTTON>

<BUTTON TYPE=RESET NAME=Sil VALUE="Sil"><IMG SRC=”sil.gif></BUTTON>

### Örnek

Formlarla ilgili bu temel bilgileri sıraladıktan sonra, basit bir form örneği yapalım. Herzaman olduğu gibi, önce yapacağımız şeyin (formun ) stratejisini belirleyelim. Bu bir kitabevinin kitap sipariş formu olacak. Köşesine logomuzu koyacağız; ziyaretçinin adını soyadını, e-posta adresini ve adresini isteyeceğiz. Formda, ziyaretçinin ne tür kitaplarla ilgilendiğini belirtmesi için bir çok seçenekli liste sunabiliriz. Sonra ziyaretçiden bazı kutuları ve seçenekleri tıklayarak, bize kendisi hakkında bilgi vermesini isteyeceğiz. En sonunda da bu formu göndermesini veya tümünü silmesini sağlayan iki düğme sunacağız. Formumuz bir Web alanının parçası olacağı için, ziyaretçinin geri dönmesini ve ilk sayfamıza gitmesini sağlayan iki yol gösterme düğmesi koyabiliriz.

Bir formda form unsurları ile unsurların yanında yer alan ve neye ilişkin olduklarını belirten metinleri hizalamak oldukça zordur. Kutuların altalta gelmesi için, aralıktan yararlanmak ise hemen hemen imkansız denilecek kadar zordur. Bu nedenle mimari ilkemiz, formun içine bir tablo yerleştirmek ve form unsurlarını tablonun hücrelerine koymak olacak. Örnek form için, bir logo grafiğine ihtiyacınız olabilir. Bu grafik, görsel olarak alanınızdaki bütün sayfalar arasında birlik sağlayabilir ve form sayfasının hangi alana ait olduğunu gösterebilir. Örnek bir sayfa için şu kodu kullanabilirsiniz:

<html>

<head>

<title>Sizinle nasıl temas kuralım</title>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">

</head>

<body bgcolor="#FF8040">

<div align="center"><center>

<table border="0" width="100%">

<tr>

<td width="13%"><img src="Logo.gif" width="92" height="125" alt="Logo.gif (15642 bytes)"></td>

<td width="54%"><h1><font face="Arial" color="#804040">Sizinle nasıl temas kuralım?</font></h1>

</td>

<td width="33%"></td>

</tr>

<tr>

<td width="13%"></td>

<td width="54%"><form method="POST" name="temasform" action="Post">

<div align="center"><center><table border="0" width="103%" height="448">

<tr>

<td width="42%" height="23"><div align="right"><p>Adınız</td>

<td width="61%" height="23"><input type="text" name="Adınız" size="37" tabindex="1"

maxlength="25"></td>

</tr>

<tr>

<td width="42%" height="23"><div align="right"><p>Adresiniz</td>

<td width="61%" height="23"><input type="text" name="Adresiniz" size="37" tabindex="2"></td>

</tr>

<tr>

<td width="42%" height="23"><div align="right"><p>Posta Kodu</td>

<td width="61%" height="23"><input type="text" name="Kod" size="37" tabindex="3"

maxlength="5"></td>

</tr>

<tr>

<td width="42%" height="23"><div align="right"><p>E Posta</td>

<td width="61%" height="23"><input type="text" name="eposta" size="37" tabindex="4"></td>

</tr>

<tr>

<td width="103%" height="44" colspan="2"><font face="Arial"><strong><big>Sizi tanıyabilir

mıyız?</big></strong></font></td>

</tr>

<tr>

<td width="42%" height="19"><div align="right"><p><font face="Arial">Eğitim düzeyim:</font></td>

<td width="61%" height="19"><input type="checkbox" name="ilkokul" value="ON" tabindex="5">Ilk<input

type="checkbox" name="Orta" value="ON" tabindex="6">Orta<input type="checkbox" name="yuksek"

value="ON" tabindex="6">Yüksek</td>

</tr>

<tr>

<td width="42%" height="31"><div align="right"><p><font face="Arial">Merak Alanım</font></td>

<td width="61%" height="31"><select name="Merak" size="1" tabindex="7" style="font-family: sans-serif">

<option selected value="Bir alan seçiniz">Bir alan seçiniz</option>

<option value="Polisiye">Polisiye</option>

<option value="Siir">Şiir</option>

<option value="Tarih">Tarih</option>

<option value="Siyaset">Siyaset</option>

</select></td>

</tr>

<tr>

<td width="103%" height="36" colspan="2"><div align="left"><p><font face="Arial"><strong>Bize

iletmek istediğiniz bir mesaj var mı?</strong></font></td>

</tr>

<tr>

<td width="42%" height="117"></td>

<td width="61%" height="117"><textarea rows="5" name="mesaj" cols="33" tabindex="9">Mesajınınızı buraya yazınız</textarea></td>

</tr>

<tr>

<td width="42%" height="25"></td>

<td width="61%" height="25"><input type="submit" value="Gönder" name="Gonder"

tabindex="10"

style="font-family: sans-serif; font-size: 14pt; background-color: rgb(128,128,0); color: rgb(255,255,255)">

&nbsp; <input type="reset" value="Sil" name="Sil" tabindex="11"

style="font-family: sans-serif; font-size: 14pt; background-color: rgb(128,128,0); color: rgb(255,255,255); text-align: center"></td>

</tr>

<tr>

<td width="42%" height="18"></td>

<td width="61%" height="18"><div align="right"><p><a href="#">Geri dön</a>

&nbsp;&nbsp;&nbsp; <a href="#">İlk Sayfaya git</a></td>

</tr>

</table>

</center></div>

</form>

</td>

<td width="33%"></td>

</tr>

</table>

</center></div>

</body>

</html>

Bu HTML dosyasının oluşturduğu form ise ekranda şöyle görünüyor:

reh078.tif

Burada, Form etiketine daha önce belirttiğimiz özelliklerini veren yüklemlerden farklı olarak, fodrma bir isim verdiğimiz dikkatinizi çekmiş olmalı. Ayrıca kullanıcıya kutudan kutuya, klavyede TAB (Sekme) tuşuna basarak ilerleme imkanı veren ve tarayıcının formda kutulara hangi sırayla gideceğini gösteren “tabindex=..” yüklemine dikkat ediniz. Bu yüklemi bütün form elemanları için kullanabilirsiniz. Formu içine koyduğumuz tabloya çerçeve çizgisi vermemekle, formun “form gibi” görünmesini sağladık. Tablonun hücrelerinin enini (width) mutlak sayı ile değil de yüzde kullanarak sınırladığımız için, formumuz ziyaretçinin ekranında sağda solda boşluk bırakmadan, büyüyüp, küçülebilecektir.

## CGI

Forma ilgili bütün bu çaba, bir tek karşılık için, ziyaretçinin bize bilgi veya sipariş vermesi, başka bir deyişle ziyaretçinin formu doldurarak, “Gönder” düğmesinin tıklaması içindir. Fakat bu düğmenin tıklanması, bizim formdan beklediğimizin gerçekleşmesine yetmez. Ziyaretçinin tarayıcı programının Server’a ileteceği bilgi ile Server’da “bir şey yapılması” gerekir. Bunu yapacak olan da ziyaretçilerle Server arasındaki arabirim olan CGI (Common Gateway Interface) programlarıdır.

Microsoft’un NT işletim sisteminin, Ağ (Network) işletim sistemi olarak Unix sisteminin yerine ciddi bir aday olduğunu ilan ettiği iki üç yıl öncesine kadar, ağ dendiği zaman otomatik olarak akla Unix işletim sistemi gelirdi. Bu sistemin Internet uzantısını sağlayan programlar ise Unix ortamı için geliştirilmiş diller ve programlar kullanırlardı. “Perl” ve “tcl” bu dillerin en yaygınlarıdır. Bu diller o denli yayıldı ve klasik hale geldi ki, NT ortamı için Perl çeviriciler geliştirildi. Bir Web Server’ın DOS ortamında işletilmesi halinde, CGI programları sdandart DOS “batch programları” bile olabilir. Ancak NT sistemleri için kendi doğal dillerini ve programlarını kullanmak yerinde olur. Nitekim günümüzde Perl’ün yerini hızla Visual Basic ile yazılmış Active Server Page denen arabirimler alıyor. Ayrıca C ve C++ dilleri ile yazılmış arabirimler, örneğin formunuzu alıp, ona uygun arabirim işlemcisi yazan programlar edinebilirsiniz. Macintosh ortamında ise en uygun dil olarak, Applescript sayılabilir.

CGI arabierimi ve programları, bu kitapçığın kapsamı dışında kalıyor. Ama, Qeb tasarımcısı olarak neye ihtiyacınız bulunduğunu bilmeniz için, ziyaretçi “Gönder” tuşuna bastığı zaman, ziyaretçinin bilgisayarı ile sizin Web Server’ınız arasında olup biteni kısaca özetlemekte yarar var.

FORM etiketine koyduğunuz ACTION ve bu eylemin yöntemine ilişkin METHOD yüklemleri doğrultusunda, Web sayfalarınızın bulunduğu Servar’a, formun içerdiği bilgiler toplu halde gönderilir.

ser\_cli.TIF

Server bu bilgileri, METHOD olarak GET veya POST yöntemlerinden hangisini seçtiğinize bakarak, bu bilgileri CGI programına aktarır. CGI programınız, türüne göre, bu bilgileri önce formdaki değişkenlere verdiğiniz isimlere ve değerlere göre ayırır ve bir liste yapar. Bu listedeki veriler, yine CGI programınızın yapmasını istediğiniz işlemde kullanılır. Çoğunlukla bu bilgilerin (1) bir veri tabanına işlenmesini, (2) ziyaretçiye gönderdiği bilgilerin alındığına ilişkin olarak ya tarayıcısına bir HTML sayfa göndererek, veya elektronik posta ile bir mesaj yollayarak bir karşılık verilmesini, ve (3) Web yöneticisine forma bir ziyaretçinin daha karşılık verdiğine ilişkin bir uyarı mesajı gönderilmesini isteriz. CGI programı bu üç işi birden yapar ve devreden çıkar. Oluşturulacak veritabanı daha sonra çeşitli programlar yardımıyla kullanılabilir.

SONUÇ

Bu kitapçıkta, HTML’in temel etiketlerini ele almış olmamıza rağmen, adını bile etmediğimiz etiketler bulunduğunu bilmeniz gerekir. Aynı şekilde, Web sayfalarının Dinamik HTML genel başlığı altında toplanan imkan ve yeteneklerinden de hiç söz etmediklerimiz var. Ancak burada ayrıntılarını ele aldığımız etiketler ve yöntemler, bugün Internet’te gördüğünüz bir çok sayfadan çok daha iyisini yapmanıza yetecek düzeydedir.

CGI programları ise, HTML’den çok daha kapsamlı, içinde yer alacağı Internet Server programının, hatta ondan da öte, yerleştirileceği bilgisayar işletim sisteminin özellikleri dikkate alınarak yazılması gereken programlardır. Perl, bu işi en basite indiren dillerden biridir. Ama Visual Basic ve microsoft’un Visual Interdev adıyla topladığı HTML ve Server programları yazmayı son derece kolaylaştıran programları, programlama dili bilmeden program yazmaya imkan veriyor.

HTML’in ve CGI programlarının teknik detaylarını öğrenmek giderek kolaylaşıyor. Bu ise size, işin teknik yanından çok içeriğe ve bu içeriğin sunuluşundaki kalite eğilme imkanı veriyor.

---
*Kaynak: `HTML - DEVAM/ekitap-Hakki_Ícal-Kitapcik_HTML_Rehberi.html`*
