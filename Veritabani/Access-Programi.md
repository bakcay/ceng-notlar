# Access Programi

## **1.**** ****GİRİŞ******

MS-Access 7.0 ya da kısaca Access, bir veritabanı oluşturma ve yönetim programıdır. Bu program kullanılarak, bilgiler düzenli bir şekilde depolanarak istenilen zamanda ve şekilde kullanılabilirler.

## **1.1**** ****Access Programının Başlatılması******

Access programı, arabiriminin genel görüntüsü açısından, diğer Windows ve özellikle de MS Office programlarına büyük benzerlik göstermektedir. Çalıştırılması da aynı diğer Windows programlarında olduğu gibidir. Elbette ki, en bilinen ve kullanılan yöntem, **Start** menüsünden **Programs** kısmındaki Access komutunun tıklanmasıdır. Diğer yöntemler arasında, eğer yüklenmişse MS Office Kısayol Çubuğu’ndaki Access düğmesinin tıklanması, eğer desktop’a (masaüstü) konmuşsa Access programının kısayol simgesine çift tıklanması ve Windows Explorer’da Access programının (msaccess.exe) dosyasının üzerinin çift tıklanması sayılabilir.

Access yüklendikten sonra, karşımıza aşağıdaki diyalog kutusu görüntülenir. Buradaki ilk iki seçenek, yeni bir veritabanı oluşturma ile ilgilidir. *Boş Veritabanı* seçeneği, içerisinde hiç bir bilgi içermeyen bir veritabanı oluşturur ve bu veritabanını bilgi girilmek üzere hazır durumda açar. *Veritabanı Sihirbazı* ise yine içerisinde hiç bir bilgi olmayan bir veritabanı oluşturur ancak, bu veri tabanı, kullanıcının Veritabanı Sihirbazına vermiş olduğu bilgiler kullanılarak hazırlanmış bir alt yapıyı da içermektedir. Bir önceki seçenekle oluşturulmuş olan veritabanında hiç bir alt yapı hazırlanmamaktadır. Alt yapıdan kastedilenilen, ileride daha detaylı olarak anlatılacak olan Tablo, Form ve Raporlardır.

Aynı diyalog kutusunda bulunan *Varolan Veritabanını Aç* seçeneği daha önceden oluşturulmuş olan bir veritabanını açmak için kullanılır.

Yukarıda açıklanan üç seçenekten birisi seçildikten sonra, *Tamam *düğmesi tıklanmalıdır. *İptal* düğmesinin tıklanması ile de herhangi bir veritabanı açılmaksızın ve oluşturulmaksızın, Access arabirimine ulaşılır.

## **1.2**** ****Access Arabirimi******

Ekranın en üst bölümünde, "Microsoft Access" başlığı görülür. Bu bölüm, başlık çubuğu olarak adlandırılır.

Başlık çubuğunun altında, menü seçeneklerinin yer aldığı menü çubuğu görülebilir. Buradaki menü seçenekleri, Access'in o anki moduna ve Access uygulamanızın özel bir menü sistemine sahip olup olmamasına göre değişiklik gösterecektir.

Menü çubuğunun hemen altında, araç çubuğu yer alır. Access'te çok sayıda değişik araç çubuğu bulunmaktadır. Kullanıcının kendi araç çubuklarını da oluşturması mümkündür. Araç çubukları, sık gerçekleştirilen işler için birer kestirme gibi düşünülebilirler.

Daha önce Access kullanmış olanlar için bile, araç çubuğundaki düğmelerin işlevlerini unutmak söz konusu olabilir. Araç çubuğundaki düğmelerden birinin üzerine mouse getirilip birkaç saniye beklenirse, küçük bir balon bu bileşenin işlevini açıklayıcı bilgi sunacaktır. Ayrıca en altta yer alan durum çubuğunun da kısa bir açıklama içerdiği görülebilir. Bu araç ipuçları kullanılarak her bir düğmenin ne işe yaradığı kısa sürede öğrenilebilir.

## **1.3**** ****Araç Çubuklarının Düzenlenmesi******

Access ilk açıldığında, araç çubuğu tek bir satırdan oluşmaktadır. Bu çoğu zaman işe yarasa da, zaman zaman farklı bir düzen gerekli olabilmektedir. Araç çubuklarını başka bir konuma taşımak için, mouse, araç çubuğunun boş bir bölümüne getirilip sol mouse tuşu ile sürükleme yapmak gerekmektedir. Araç çubukları ekranın dört kenarına yaslanacak şekilde yerleştirilebildiği gibi, aşağıdaki şekilde görüldüğü gibi, orta yerde seyyar olarak da kullanılabilirler. Bu durumda, araç çubuğunun üst kısmında bir başlık kısmı açılarak, araç çubuğunun ismi görüntülenir.

Başka araç çubuklarının görüntülenmesi ve araç çubukları ile ilgili değişik ayarlar yapabilmek için *Görünüm* menüsünden *Araç Çubukları *seçeneği seçilir. Aşağıdaki diyalog kutusunda, istenilen diğer araç çubuklarına ait kutuların işaretlenmesi ile başka başka araç çubukları da görüntülenebilir. Ancak bilinmelidir ki, Access programı, o anda yapılmakta olan işlem için gerekli olan araç çubuğunu otomatik olarak görüntüleyebilmektedir.

## **. Yeni Bir Veri Tabanının Hazırlanması******

Access’te yeni bir veritabanı oluşturulması, Msoffice paketinde bulunan Word ve Excel gibi diğer programlarda yeni doküman ya da kitap oluşturma işlemine benzerdir. Access’in ilk açılışında, görüntülenen diyalog kutusunda *Boş Veritabanı* seçeneği kullanılarak yeni bir veritabanı oluşturulabildiği gibi, daha sonra da araç çubuğundan *Yeni* düğmesi basılmak ya da *Dosya* menüsünden *Yeni Veritabanı* komutu seçilmek suretiyle de yapılabilir.

Hangi yöntem kullanılırsa kullanılsın, yeni bir veritabanı mutlaka bir şablon kullanılmak suretiyle oluşturulur. Herhangi bir şablon kullanılmak istenmiyorsa, bu durum da aslında yine bir şablon olan *Boş Veritabanı* şablonu seçilmelidir. Bu şablon dışında başka bir şablon kullanılmak isteniyorsa, aşağıdaki diyalog kutusunda olduğu gibi mevcut şablonlardan birisi seçilebilir. Bazı şablonlar, bir sihirbazı devreye sokarak, oluşturulacak yeni veritabanının yapısına ilişkin bazı bilgileri kullanıcıdan alırlar ve en son olarak da yeni veri tabanını oluştururlar.

• Access açılır.

• Açılış diyalog kutusunda Cancel tıklanır.

• Araç çubuğundaki New Database düğmesi tıklanır. Access bir dizi şablon içerisinden yeni veri tabanı için seçim yapılmasına olanak tanır. Blank database şablonu bulunur ve vurgulanır.

• OK tıklanır ve uzantısı .mdb olan yeni bir veri tabanı hazırlanmış olur.

• Create tıklanarak Access’in veri tabanı hazırlama işlemini tamamlaması sağlanır.

## **2.1 Wizard’a Giriş******

Hazırlanan yeni veri tabanı çerçevesi, kullanılacak bütün nesneler için bir kap durumundadır. Bu pencere üst bölümünde sekmelere ve yan tarafında da bir kaç düğmeye yer verir.

2.1.1.Wizard Kullanılarak Yeni Bir Tablonun Hazırlanması

• Veri tabanı penceresinin sağ tarafındaki New düğmesi tıklanır. Bir sonraki diyalog kutusunda da Table Wizard tıklanır.

• OK tıklayın. Bir sonraki diyalog kutusunun sol alt bölümündeki Personal seçenek düğmesi tıklanır.

• Business ve Personal etiketli iki seçenek düğmesi, Wizard kullanılırken iki tablo tipi grubundan hangisinin kullanılacağını belirler. Sample Tables başlıklı liste kutusu, yeni tablo için şablon olarak kullanabilecek tabloları içerir. Sample Fields liste kutusu ise herbir örnek tabloda kullanabilecek alanları gösterir.

• Table Wizard'ı kullanırken istenene yakın alanları içeren örnek bir tablonun seçilmesi uygun olacaktır.

• Personal etiketli seçenek düğmesi tıklanarak kişisel örnek tablo kümesi görüntülenir. Farklı tabloların bir arada çalışabileceği unutulmamalıdır.

• Örnek bir tablo tıklandıktan sonra >> düğmesi tıklanırsa örnek tablodaki verinin tümü yeni tabloya taşınacaktır.

• Yeni tabloya örnek tablodan sadece bazı alanlar eklenecekse, bu alanlar vurgulanır ve > düğmesi tıklanır. Yeni tablodan alan çıkartmak içinse < ve << düğmeleri kullanılmalıdır.

• Fields in my new table liste kutusuna istenen bütün girişler yerleştirildikten sonra, Next> düğmesi tıklanarak tablo tasarımının bir sonraki aşamasına geçilir.

• Access tablo için Authors adını önerecektir,bu ad kabul edilir ya da başka bir ad kullanılır. Access ana anahtar (primary key) seçenek düğmesine geçerek kullanıcı için ana anahtarı hazırlayacaktır. Varsayılan bu durumun geçerliliği korunur ve Next> tıklanır.

• Access, Wizard işleminin tamamlanmak üzere olduğunu belirten bir ekran görüntüleyecektir. Bu noktada tablo tasarımını değiştirme, tabloyu veri girişine açma ya da form hazırlamak için başka bir Wizard’ı etkinleştirme seçenekleri sunulacaktır.

• "Enter data directly into the table"’ı ve Finish düğmesi tıklanır. Access yeni tabloyu hazırlayıp açacaktır.

• Şu andan sonra TAB ve ENTER tuşlarıyla alanlar arasında gezebilir ve veri girişi yapılabilir.

• İlk alana hiçbir bilgi girilemediğine dikkat edin. Bu alan Access'in alanları belirlemek için kullandığı ardışık numaralara ayrılmıştır.

Tablonun kullanımı sona erdiğinde kontrol menüsü ikonu çift tıklanarak ya da sağ üstte yer alan X düğmesi tıklanarak tablo kapatılabilir. Eğer alan genişlikleri değiştirildiyse bu değişikliklerin kaydedilmek istenip istenmediği sorulacaktır.

## **2.2 Yardım******

Bazı durumlarda ipucu kartları ve Wizard'Iarın sunduklarının ötesinde yardıma gereksinim duyulabilir. Bu tip durumlarda çevrimiçi Access yardım özelliği kullanılabilir.

## **2.3 Çevrimiçi Yardım Bileşenleri******

• Access başlatılır.

• Ana menü çubuğundan Help girişi tıklanır.

• Aşağı açılan menü listesinden Microsoft Access Help Topics tıklanır.

• Yardım penceresinin üstündeki Find sekmesi tıklanır. En üstteki seçenek düğmesi tıklanarak indeks boyutu en düşük düzeyde tutulur ve Next> düğmesi tıklanır. Finish tıklanarak yardım başlıklarına ait bir dizin listesinin görüntülenmesi sağlanır.

• İçlerinden seçim yapılabilecek 5600 konu başlığı bulunmaktadır.

• Hakkında yardım istenen deyim diyalog kutusunun üst kenarında bulunan boşluğa yazılır. Display düğmesini tıklanarak vurgulanan deyim ile eşleşme sağlayan yardım konusu görüntüye getirilir.

• Bunun sonucunda görüntülenecek help sayfası bir ipucu kartına yer yer verebilmektedir.

• İstenen konu başlığına ulaşıncaya kadar, tarama işlemi yinelenebilir.

• Index sekmesine girerek seçimin girilmesi de mümkündür. Access dizini en çok başvurulan konu başlıklarını içermesine karşın, Find dizinleri kadar kapsamlı değildir.

Find dizinlerinin kullanılmasının dezavantajlı yönü ise, zaman ve disk boşluğu harcamasıdır.

## **3. TABLOLARA VERİ GİRİLMESİ******

## **3.1 Veri Tabanı Projesi******

Proje dahilindeki örnek veri tabanında öğrencilerin istatistik bilgilerinin, aldığı derslerin ve öğretim ücreti ödeme durumlarının işlenmesi amaçlanmıştır. Etiketler değiştirilip birkaç düzenleme yapılarak aynı sistem tıp, ticaret ve personel yönetimi gibi alanlarda da kullanılabilir.

**3.1.1 Veri Tabanının Planlanması******

Access gibi ilişkisel bir veri tabanında, veriler mantıksal tablo gruplarına ayrılırlar. İlişkisel veri tabanı modelinin amacı, yüksek verimliliktir. İlişkisel olmayan düz kütük yönteminin bir öğrenciyle ilgili veriyi saklamak amacıyla kullanılması durumunda, öğrencinin aldığı her bir ders için ad, adres ve telefon biİgileri çoğaltılacaktır. Bu gereksiz fazlalık, önemli sayıda kayıtla uğraşan günümüz veri tabanları söz konusu olduğunda hem artan disk boşluğu ihtiyacı, hem de artan veri ulaşım zamanı gibi büyük sorunlara yol açacaktır.

İlişkisel modelde ise, veri iki tabloya ayrılacaktır. Birinci tablo kimlik, sigorta numarası ve adres gibi kişisel öğrenci bilgilerini içerecektir. İkinci tablo ise bu bilgileri çoğaltmak yerine ders bilgisine ve öğrenci kimlik bilgisine yer verir. Öğrenci kimlik bilgisi, Access'in öğrenciyi aldığı derslerle eşlemede kullandığı bağlantı alanı durumundadır.

**3.1.2 İlk Tablodan Önce******

Okullarda kullanılan veri tabanları, öğrencilere ilişkin kişisel bilgiyi içerecek bir tabloyu gerektirir.

**3.1.3 Yeni Bir Veri Tabanının Hazırlanması******

• Access açılır. En üstteki seçenek düğmesi kullanılarak boş veri tabanı hazırlanır.

• Eğer Access zaten açık durumdaysa, kapatılıp açılarak yada New Database düğmesi tıklanarak ilgili diyalog kutusunun görüntülenmesi sağlanır.

• OK tıklanarak yeni diyalog kutusuna geçilir.

• Access yeni veri tabanını adlandırmanızı isteyecektir. Access'irı önerdiği ad yerine, uygun görülen bir deyim girilir. Veri tabanı adlarında, .mdb uzantısı kullanılacaktır.

• Access yeni bir veri tabanı hazırlayacaktır.

**3.1.4 İlk Tablo******

Örnek uygulamada, Öğrenci Bilgi tablosuna Öğrenci sigorta no, ad (ilk ad orta ad ve soyad), adres, telefon, acil durum erişimi ve/veya anne-babası, elektronik posta adresi, takip konusu ve notlar gibi alanlara yer verilecektir.

**3.1.5 Öğrenci Bilgi Tablosunun Hazırlanması******

• Table sekmesinin seçildiğinden emin olunur.

• Database kutusu içindeki New düğmesi tıklanır.

• Access bazı seçenekleri sunacaktır. Bunlardan ilk ikisi olan Datasheet View ve Design View, elle tablo hazırlama seçenekleridir. Son iki seçenek olan Import Table Wizard ve Link Table Wizard varolan tabloların veri tabanına bağlanmasını ya da aktarılmasını sağlar. Table Wizard seçilir ve OK tıklanır.

• Sol alt köşedeki Business seçenek düğmesinin işaretli olmasına dikkat edilmelidir. Mouse'la Sample Tables listesi gerekirse kaydırılır ve Öğrenciler tablosu bulunur ve tıklanır.

• Access kullanıcı için işleri kolaylaştıracaktır. Sample Fields liste kutusu incelenirse, istenen alanların hemen hemen tümünün İngilizce olarak içerildiği görülecektir.

• Sample Fields liste kutusunun hemen sağındaki > > düğmesi tıklanarak örnek alanların hepsinin tabloya aktarılması sağlanır. Öğrencilerin hepsi Türkiye’de olacağı için, PostaICode alanı ve Rename tıklanıp alan PostaKod olarak adlandırılabilir. OK tıklanarak yeni ad kabul edilir. StateOrProvince alanı da aynı şekilde Ûlke olarak değiştirilebilir. Rename seçeneği kullanılarak bütün alanlar Türkçeleştirilebilir.

• Table Wizard'ın sağ alt bölümünde yer alan Next> düğmesi tıklanır. Access tablo için Students adını önerecektir, ancak bunun yerine ÖğrenciBilgi adı kullanılır.

• Wizard diyalog kutusunun ortasına geçilir ve No, set the Primary Key seçilir. Next> tıklanarak sıradaki diyalog kutusuna geçilir.

• Kimlik olarak öğrenci sigorta numarası kullanılacağından her bir kayıt için ayrı bir öğrenci kimliği söz konusu olacaktır. Access'in her bir kayıt için ayrı bir öğrenci kimliği kullanma konusundaki önerisine uyun. Öte yandan ortadaki diyalog kutusunda en alt seçenek kullanılarak, ana anahtar alanda hem harf hem de rakamların kullanılabilmesi mümkün kılınır.

• Next> düğmesi tıklanır. Access kullanıcıya son olarak üç seçenek daha sunacak ve Wizard'ın sonunda olduğunu belirtecektir. Eğer seçili değilse, en üstteki seçenek tıklanarak Access'e son olarak tablo tasarımı üzerinde oynamak istendiği bildirilir. Finish tıklanır. Access yeni tabloyu hazırlayacak ve kullanıcıyı Design View görüntüsünde bırakacaktır.

**3.1.6 Alan Tipleri Ve Özellikleri******

Tablo tasarım penceresinin en üst bölümü, alan adları ve veri tiplerine ilişkin bir liste içermektedir. Pencerenin altında, General ve Lookup adlı iki sekmeye yer veren Field Properties adlı bir bölüm bulunmaktadır. Access tablosundaki her bir alan, üç bileşene sahiptir: Alan adı (kimlik gibi), alan tipi (Text gibi) ve özellikler. Veri tabanındaki her bir alanın uygun bir alan tipine ayarlanması önemlidir.

**3.1.7 Veri Tipleri******

Access, şu veri tiplerini desteklemektedir.

• Metin (text): Alphanumeric olarak da bilinir. Normal karakterleri kabul eder. Alan uzunluğu 255 karakterle sınırlıdır.

• Sayı (number): Bu veri tipi sayıları kabul eder. Alanlar üzerinde matematik işlemler yapılması planlanıyorsa, bu veri tipi kullanılmalıdır.

• Tarih/saat (date/time): Number veri tipinin özel bir biçimi olan Date/Time, tarih ya da saat bilgisinin girilmesi için kullanılır. Bu tip veriye sahip alanlarda da matematik işlemleri yapılabilir.

• Para (currency): Para bilgisinin girilmesini sağlayan bu veri tipi de, Number'ın değişik bir uyarlamasıdır.

• Otomatik numaralama (autonumber): Bir alandaki verinin tipi Autonumber yapıldığında, Field Property New Number'ın Increment olarak ayarlanması durumunda Access kayıtlara ardışık sayılar uygulayacaktır. Random'a ayarlandıysa, Access her bir yeni kayıt için gelişigüzel sayılar üretecektir. Increment olarak ayarlandığında Access numara vermeye 1'den başlar. Increment ya da Random seçenekleri, ana anahtar alanlar için kullanılır, çünkü Access bir tablodaki kayıtlardan birine atanmış bir sayıyı bir daha kullanmayacaktır. Bu tip alanların gereksiz kullanımı veri tabanını gereksiz bilgilerle doldurarak ilişkisel teoriye ters düşecektir.

• Evet/Hayır (yes/no): Yalnızca iki değer kabul eder: Yes ya da No.

• Arama Wizard'ı (lookup wizard): Diğer veri tabanı nesnelerine önceden girilmiş olan değerleri arar.

• OLE nesnesi (OLE Object): OLE'yi destekleyen başka bir programda hazırlanmış bir nesnenin yerleştirilmesini ya da nesneye bağlanılmasını mümkün kılar. Access 95, yalnızca bir OLE müşterisi durumunda olduğu için, OLE'yi destekleyen diğer programlara yerleştirilebilen nesneler hazırlayamaz.

• Not (memo): Bir kayda not eklenmesini sağlayan bir alandır.29

## **4. TABLO ALANLARININ ÖZELLİKLERİ******

## **4.1 Bir Tablonun Düzenlenmesi******

Access'de bir tablonun hemen hemen bütün özellikleri değiştirilebilir. Aynı amaçla bir wizard da kullanılabilir. Çoğu zaman tablo tasarlandıktan sonra belirli bir alandaki veri tipinin yanlış olduğu ya da bir alanın eklenmesi veya çıkarılması gerektiği farkedilecektir. Örnek tabloda da etkin kökeni belirten bir alan eklenmesi ve fazlalık StudentNumber alanının çıkarılması gerekmekte. Uygun tablo tasarım alanını tıklayıp istene değişiklikler şu şekilde yapılmalıdır.

• Access, Okul veri tabanı, yada Öğrenci bilgi tablosu kapalıysa yeniden açılmalıdır. Öğrenci bilgi tablosu vurgulanmış durumdayken, veri tabanı penceresindeki Design düğmesi tıklanır.

• StudentNumber alanı bulunur. Mouse, alan adının hemen solundaki gri bölüme getirilir ve göstergenin sağ yönü gösteren bir oka dönüştüğü gözlemlenir. Sol mouse düğmesi tıklanarak alanın tamamı vurgulanır

• Del tuşuna basılır. StudentNumber alanı silinecektir.

## **4.2 Alan Ekleme******

Access veri tabanlarına kolaylıkla yeni alanlar eklenebilir.

**4.2.1 Bir Tabloya Alan Eklenmesi******

• FieldName alanı kaydırılarak Takip Konusu başlığı bulunur. Mouse Field Name sütununun sol kenarına taşınır. Gösterge, sağ yönü gösteren bir oka dönüşecektir. Sol mouse düğmesi tıklanır.

• Access satırın tamamını vurgulayacaktır. Tıklarken, mouse göstergesinin Takip Konusu alanının hemen solundaki gri bölümün dışına çıkmamasına dikkat edilmelidir.

• Takip Konusu satırı tümüyle vurgulanmış durumdayken, Insert tuşuna basılır. Access yeni ve boş bir satır yerleştirecek ve takip Konusu alanını bir satır aşağı kaydıracaktır.

• Vurgulanan satırın Field Name sütunu bir kez tıklanır. Satırın vurgusu kaybolacak ve gösterge Field Name sütununun en solunda yer alacaktır. Şimdi Köken sözcüğü girilir.

• Tab tuşuna basılarak gösterge Data Type sütununa taşınır. Access Text veri tipini önerecek ve ayrıca Data Type alanının sağında bir sekme sunacaktır. Sekmeyi tıklanarak liste açılır.

• Text, Köken alanı için doğru veri tipidir. Ancak diğer seçenekleri görmek için aşağı ok düğmesi tıklanabilir.

• Böylece ÖgrenciBilgi tablosuna yeni bir alan eklenmiş olur. Kontrol menü ikonu çift tıklanarak ya da X düğmesi kullanılarak ÖgrenciBilgi tablosu kapatılır. Access tabloda yapılan değişikliklerin kaydedilmesinin istenip istenmediğini sorunca, OK tıklanır.

## **4.3 Wızard'sız Tablo Hazırlama******

Wizard'ın örnekleri istenen tabloya yakın özellikler sunmuyorsa, kullanıcı kendi tablosunu hazırlamalıdır.

Örneğin, öğrenci kimliği ile ilgili alan sayesinde ÖgrenciBilgi tablosuyla bağlantı kuran ve öğrencilerin ders kayıtlarıyla ilgili bir tablo kurulacaksa ve bağımsız tabloda karşılık gelen bir kayıt yoksa, bağımlı tabloya bilgi eklenemez. İki tablo bağladıktan sonra, ÖgrenciBilgi tablosuna öğrenciyle ilgili bilgi girilmediği sürece, bir derse yeni bir öğrenci kaydedilemeyecektir. Yeni tablo ders kodu, öğrencinin dersi bitirip bitirmediğine ilişkin bir gösterge ve öğrencinin notu için de alanlara gereksinim duyacaktır ve her sömestr bu tablo başka bir tabloya veri sağlayarak öğrencinin karnesinin hazırlanmasını sağlayacaktır.

**4.3.1 Tablonun Hazırlanması******

ÖgrenciBilgi tablosunu kapandıktan sonra, Tables sekmesinde veri tabanı penceresine dönmüş olunur.

**4.3.2 Wızard Kullanmadan...******

• New düğmesi tıklanarak tablo hazırlama işlemine başlanır. Design View seçilir ve OK tıklanır. Access boş bir tablo tasarım bölümü açacaktır.

• Işıklı gösterge, tasarım alanının en solundaki sütunun ilk satırında yer alacaktır. İşlem sırasında sağ alt bölümde ve durum çubuğunda görüntülenen açıklamalar kullanıcıya yardımcı olacaktır.

• İlk alan adına IndeksNo deyimi girilir. Tab’a basarak Data Type alanına geçilir. Access Text veri tipini önerecektir. Yandaki sekmeyle açılacak listeden, Autonumber veri tipi bulunur ve tıklanır. IndeksNo alanı, bu tablo için anahtar alan olma işlevini üstlenecektir. Autonumber veri tipinin kullanılması sayesinde, Access bu tabloda hazırlanacak her bir kayıt için bu alana diğerlerinden farklı bir sayı girecektir. Ekranın alt bölümünde New Values alanının, Increment olarak ayarlandığına dikkat edilmelidir.

• İkinci alan, ÖgrenciBilgi tablosuyla bağlantıyı sağlayacak olan Ögrenci Sigorta No alanıdır. İki kez Tab’a basılarak Field Name sütununun ikinci satırına geçilir.

• Ögrenci Sigorta No deyimi girilir. Data Type alanına geçilir. Access'in sunduğu varsayılan ayarlar kabul edilir ve iki kez Tab'e basılarak bir sonraki satıra geçilir. ÖgrenciBilgi tablosunda Text veri tipine sahip olan Ögrenci Sigorta No alanının, yeni tabloda da Text veri tipine sahip olduğu gözlenmelidir.

• Bir sonraki satıra geçtikten sonra, DersKod deyimi girilir. Yine Data Type sütununa geçilir, Access'in varsayılan ayarlamaları kabul edilir ve iki kez Tab'e basılarak Field Name alanındaki dördüncü satıra geçilir.

• Yeni alanın adı Bitirdi olarak girilir ve veri tipi olarak Yes/No seçilir. Bir sonraki Field Name satırına geçilir.

• Son alan için Not deyimi girilerek alanlara ad verme işlemi tamamlanır. Son alanın veri tipi Text olarak bırakılır.

• Bir not Access'in alan boyutu için sunduğu 50 boşluğu tamamıyla kaplamayacaksa, Field Properties bölümündeki Field Size satırı tıklanarak varsayılan değer düşürülür.

• Access'e IndeksNo alanının, anahtar alan olarak istendiği belirtilir.

• Tablo tasarım bölümündeki ilk sütunun ilk satırı (IndeksNo alanı) tıklanır. Araç çubuğunda küçük bir anahtarla temsil edilen düğme bulunur. Bu düğme tıklanır. IndeksNo alan adının hemen solunda küçük bir anahtar görüntülenecek böylece IndeksNo'nun anahtar alan olarak ayarlandığını gösterecektir.

• Bu tabloya bir ad verip kaydetmek gerektiğinde, File menü maddesi tıklanır ve Close seçilir. Access yapılan değişikliklerin kaydedilmek istenip istenmediğini soracaktır. Yes tıklanır. Ad sorulduğunda, ÖgrenciVeDers deyimi girilir. OK tıklanır. Access tabloyu kaydedecektir.

## **4.4 Neden İlişkisel?******

ÖgrenciVeDers tablosunda öğrenci olmayanlara ilişkin hiçbir giriş istenmeyecek ve ayrıca alınan dersleri öğrencilerle gerektiği gibi eşleme gereksinimi duyulacaktır. Access gibi ilişkisel bir veri tabanında, bağlar bu iki işlevi de yerine getirmektedir.

ÖgrenciBilgi ve ÖgrenciVeDers tabloları arasında bağlarıtı kurulmasının doğrulama ve eşleme olmak üzere iki nedeni vardır. Doğrulama, ÖgrenciVeDers tablosunda hatalı veri bulunmamasını sağlar. Amaç, bir öğrenci için ÖgrenciVeDers tablosuna bir giriş yapmadan önce, bu öğrenciyle ilgili kayda ÖgrenciBilgi tablosunda da yer verildiğinden emin olmaktır.

Ayrıca tek bir öğrenci için ÖgrenciVeDers tablosuna birden fazla kayıt girilebileceğinden de emin olmak istenecektir. Çünkü öğrenciler sömestr boyunca çok sayıda ders alabilir. Tek bir kaydın çok sayıda kayda bağlandığı ilişkiler bire-çok ilişki diye adlandırılırlar.

re-çok" ilişki biçiminde adlandırılır. Diğer tarafa "çok' sayıda giriş yapmadan önce "bir" olan tarafta ilgili kaydın varolmasını garantiye almak başvuru tümleşikliği (referential integrity) olarak adlandırılır. Eşleme, ÖgrenciBilgi ve ÖğrenciVeDers tablolarında yer alan bilgiler arasında uygun eşlemenin sağlanmak istendiği anlamına gelir. Bağ, Access'e iki tablodaki alanlardan hangilerinin birbiriyle eşlendiğini söyler.

## **4.5 Bağ Ya Da İlişkinin Kurulması******

Ekran veri tabanı penceresini gösteriyor durumda olmalıdır.

**4.5.1 Bire-Çok Bağın Oluşturulması******

• Önce Tools menü maddesi, sonra da aşağı açılan listenin ortasında yer alan Relationships tıklanır.

• Sırayla her biri vurgulanır ve Add düğmesi tıklanarak tablolar Relationship penceresine eklenir.

• Add Table diyalog kutusunda Close düğmesi tıklanır.

• ÖgrenciVeDers tablosunda IndeksNo ve ÖgrenciBilgi tablosunda da Öğrenci SigortaNo alanlarının koyu olduğuna dikkat edilir. Bu alanlar, kendi tablolarının anahtarı durumundadırlar.

• Mouse göstergesi, ÖgrenciBilgi liste kutusundaki Ögrenci SigortaNo girişine getirilir. Sol mouse düğmesi basılı tutularak mouse ÖğrenciVeDers liste kutusuna sürüklenir. Mouse düğmesi bırakılmadan gösterge ikinci liste kutusundaki ÖgrenciSigortaNo alanına taşınır ve mouse düğmesi bırakılır. Access bir diyalog kutusuyla karşılık verecektir.

• Enforce Referential Integrity seçim kutusu işaretlenir. Böylece Ögrenci Bilgi'de ilgili giriş olmadığı sürece, ÖgrenciVeDers'e giriş yapılması önlenecektir.

• File/Cİose seçilir. Access ilişki değişikliklerinin kaydetmek istenip istenmediğini sorduğunda, Yes tıklanır. Böylece veri tabanı penceresine geri dönülür.

**4.5.2 Table Analyzer******

Microsoft’un ilişkisel teorinin gerçek hayattaki sorunlara uygulanması konusunda yardımcı olarak sunduğu Table Analyzer wizard sayesinde Access, tabloları inceleyebilir ve ilişkisel teoriye daha uygun olacak şekilde yeniden yapılandırabilir. Bu wizard, ilişkisel teoriyi kavrama konusunda da çok yardımcı olabilmektedir.

## **5. TABLOYA VERİ GİRİLMESİ******

Tablonun tasarımının ardından tabloya veri girilebilir. Veri girişi için tablonun veritablosu (datasheet) görünümü kullanılır. Tablolar veri girişi için kontrollar ve görünüm bakımından daha zor olduğundan genellikle veri girişi formlardan da yapılır.

• Bu işlem için veritablosu düğmesine basılır.

• Kullanıcı birinci alandan başlayarak veri girişini hücrelere yapar.

• Bir hücreye girilen verinin ardından TAB tuşuna basılarak yandaki bir hücreye geçilir.

• Ayrıca ok tuşları kullanılarak tablo satırları ve alanları arasında hareket edilir.

Tablo alanlarına veri girişi yapılırken alan tiplerine uygun veri girilmelidir. Tarih alanına tarih, sayısal alana sayısal veri girilmelidir. Bunun dışında indeks ve ana anahtar alanlarına da uygun veriler girilmelidir. Örneğin ana anahtar olan alana birinci kayıtta olan bir bilgi ikinci kaydına da girilmemelidir. Tablo alanına yanlış tipte veri girilmesinde ise hata mesajları ekrana çıkacaktır. Bu durumda yapılan değişiklikler ya da eklenen yeni satır tabloya eklenmez.

Tablonun içindeki verilerin görülmesi için tablo tasarım durumunda Datasheet view (Veritablosu Görünümü) düğmesine basılabileceği gibi Veritabanı Penceresinden de tablo seçilerek open (Aç) düğmesine basılır. Bir tablo tasarımında diğer önemli bir konu da alanların özelliklerinin düzenlenmesidir. özellikler tasarım sırasında ya da tasarımdan sonra düzenlenebilir. Özellikler, tablonun daha etkin olarak kullanımı sağlanır. Veri girişinde yapılan hatalar önlenir, varsayılan değerler düzenlenerek otomatik olarak tabloya eklenmeleri sağlanır, verilerin biçimi (formatı) düzenlenir, indeksler düzenlenerek arama ve sıralama işlemleri yapılır.

Alanların özelliklerinin düzenlenmesi için tablo tasarım penceresinde herbir alanın üzerine gelindiğinde alt tarafta oluşan özellikler bilgilerinin satırları kullanılır. Alan özelliklerinin bazıları varsayım olarak verilmiştir. Bu nedenle özelliklerin bir kısmının düzenlenmesine gerek duyulmaz.

## **5.1 Alan Özelliklerinin Düzenlenmesi******

Field Size, Text ve number (sayısal veri) için alan genişliğini belirler. Text (alfabetik bilgi) alanların uzunluğu 1 ile 255 arasında düzenlenebilir. Text alan alfabetik ve rakam karakterlerden oluşabilir. Ancak bu alanlar üzerinde aritmetik işlem yapılmaz. Text alanın varsayım genişliği 50'dir. Herbir karaktere karşılık bir değerini alan alan genişliği, alana girilecek veriye göre ayarlanır. Alan genişliği özelliği sayısal olarak da verileri en etkin biçimde temsil etmek için ayarlanır. Varsayım olarak sayısal bilgileri Long Integer olarak temsil eder. Ancak bazı durumlarda daha az yer kaplaması için daha düşük özelliklerdeki sayısal özelliklere sahip alan ayarlaması yapılır.

Double -1.797X10 309 ile 1.797X10309

Single -3.4X1038 ile 3.4X1038

Long Integer -2,147,483,648 ile 2,147,483,647

Integer -32,768 ile 32,767

Byte 0 ile 255

Yukarıdaki tabloda da görüldüğü gibi kuruşlu ve büyük sayılarla işlem yapılacaksa alan özelliği olarak single ya da Double seçilmelidir. Bunun dışında küçük sayılar için daha geniş özellikte bir alan tipi seçmek gereksiz yer harcamak olacaktır. Sayısal alanların alan özelliklerinin değiştirilmesi sayıların değişmesine neden olabilir. Single ya da Double bir alan Integer olarak değişirse içindeki değer de yuvarlanır ya da değer kayıp olur. Alan tipi Number olarak seçilen alanların Field size (Alan Genişliği) özelliği Access’de Long Integer dır.

**5.1.1 Format******

Format özelliği, metin, sayısal verilerin, tarih ve zaman verilerinin görünümünü etkiler. Format özelliği ile kazanılan biçimleriyle veriler daha iyi bir şekilde görülürler.

**5.1.2 Format Özelliği******

Standard Sayısal bilgiler için

Short Date Kısa tarih biçimi

Long Date Uzun tarih biçimi

Short Time Kısa zaman biçimi

**5.1.3 Sayısal Alan Biçimleri******

General Number 4567.8 4567.8

Currency 4567.8 4,567.80 TL

Fixed 4567.8 4567

Standard 4567.8 4,567.80

= Percent 0.25 25%

Scientific 4567.8 4.56E+03

Sayısal bilgilerin biçimlenmesinde kullanılan diğer bir özellik de Decimal Places'dir. Decimal Places (Onlu hane) sayısal bilgide bulunacak olan onlu haneyi (kuruş) sayısını düzenler.

**5.1.4 Tarih Bilgileri******

General Date 11.05.95 3:21:01 PM

Long Date Thursday, May 11,1995

Medium Date 11-May-95

Short Date 5/11/95

Long Time 3:21:01 PM

Medium Time 03:21 pm

Short Time 15:21

**5.1.5 Caption******

Caption (Başlık) özelliği alanın adının dışında giriş ve görünümde kullanılmak üzere bir başlık düzenlenmesini sağlar.

**5.1.6 Default Value******

Default value (Varsayım Değer, Hazır Değer) özelliği bir alanda sürekli kullanılan bir değeri belirtir. Daha sonra giriş, görünümde ve formlarda bu alanın değeri otomatik olarak yer alır. Varsayılan değer alanda hazır olarak bulunur. Ancak kullanıcı bunu değiştirebilir. Amaç alanın içinde genellikle bulunacak bu değeri alanın içinde hazır olarak tutmak ve veri girişinde zaman kazanmaktır.

**5.1.7 Validation Rule, Validation Text******

Access, alanlara girilen değerleri alanın özelliklerine (tipine) göre kontrol eder. Örneğin, sayısal (number) özelliğine sahip bir alana Text (alfabetik) bilgi girilemez. validation Rule (Sağlama Kuralı) ve validation Text (Sağlama Metni) alana girilecek verinin belli bir kurala uymasını zorunlu kılar. Sağlama Kuralı verinin özelliklerini belirlerken, Sağlama Metni ise girilen verinin kuralı sağlamaması durumunda verilecek mesajı içerir. Örneğin alana 0'dan büyük bir değer girilmesi, alana 10'dan küçük bir değer girilmesi, alana "EGE", "MARMARA", "AKDENİZ" değerlerinden birisinin girilmesi gibi kurallar konulabilir. Eğer mevcut (içinde değer olan) bir tablonun bir alanına Sağlama Kuralı konmaya kalkılırsa o zaman tablo kayıtlarının tamamı okunacak ve kurala uymayanlar bulunarak mesaj verilecektir.

**5.1.8 Required******

Bir alanın her kayıtta mutlaka bir değere sahip olması isteniyorsa alanın Required özelliği Yes yapılır. Normalde bu özellik No durumundadır. Herhangi bir alanın Required özelliği Yes olarak düzenlendikten sonra bu alan Null değerini kabul etmez. Diğer bir deyişle alana mutlaka bir değer girilmelidir.

**5.1.9 Allow Zero Length******

Required özelliginin yanısıra, Text ve Memo tipli alanlar için allow zero length özelliği vardır. Bu özellik alanın sıfır uzunluğunda bir karakter bilgi (zero-length string) içerip içermeyeceğine izin verir. Normalde bir Text ya da Null alana herhangi bir değer girilmezse (boş geçilirse) o zaman alanın içine Null degeri girilmiş sayılır. Bir alana (açık biçimde) bir sıfır uzunluklu karakter bilgi girilecekse o zaman bu bilgi iki tırnak ile belirtilir. Aralarında boşluk olmayan iki tırnak sıfır uzunluklu bir karakter bilgiyi belirtir.

Zero-Length string (Sıfır-Uzunluklu Karakter bilgi). Text ya da Memo bir alan boş bırakıldığında içi değersiz (Null) olması isteniyorsa o zaman Required ve allow zero Lengt özellikleri Yes yapılarak bu alana sıfır uzunluklu bir karakterin girilmesi sağlanır.

**5.1.10 Indexed******

Çok sayıda kayda erişmek için belli anahtar alanlar gerekir. Örneğin bin kişilik bir personel listesinden işe giriş tarihleri 1/1/1990 ile 1/31/1990 arasında (bir ay) olanların bulunması gerekirse kayıtlar birer birer taranacak ve ilgili kayıtlar bulunacaktır. İşte indeksleme böyle bir durumda arama işlemini kolaylaştıracak bir düzenlemedir. Tablonun işe giriş tarihi alanı indeks alanı olarak düzenlenir. Ardından yapılacak arama işleminde kayıtlar işe giriş tarihine göre sıralı olarak okunacağı için arama işlemi daha hızlı olacaktır. Indexed (İndeksli) özelliği bir alanın indekslenerek tablodaki kayıtların o alana üzerinden daha hızlı bulunmasını sağlar.

İndeksleri Görme ve Değiştirme

Bir tablonun indeks alanlarını görmek için view (Görünüm) menüsünden indexes (İndeksler) komutu seçilir ya da Indexes düğmesine basılır. Tablonun indeks alanlarının yanısıra varsa ana anahtar alanı da İndeksler listesinde yer alır.

İndeksler penceresinde herhangi bir indeks satırı seçilerek DEL tuşuna basılarak silinebilir. Ascending (Artan) ve Descending (Azalan) sıralamanın tipidir. Artan sıralama A'dan Z'ye ya da küçükten büyüğe anlamındadır. Azalan sıralama ise bunun tam tersidir.

Çok-Alanlı Bir İndeks Yaratma

• İndeksler penceresinde çok alanlı (multiple-field) bir indeks yaratılacaksa önce yeni bir satır açılır.

• Bu işlem için seçilen bir satırın üzerine ekleme (insert) işlemi yapılır.

• Bu işlemi yapmak için önce üzerine satır eklenecek satır seçilir.

• Farenin sağ tuşuna basılarak kısayol menüsü elde edilir.

• Insert Row (araya satır ekle) komutu seçilerek indeksler listesinde araya yeni bir satır eklenir.

• Yeni yaratılacak bir indeks bir ya da daha çok alana (multiple-field) dayalı olabilir. Bu durumda indekse bir grup adı verilir.

• Alanlar birer birer seçilir.

Lookup

Tablo alanlarının tasarımında düzenlenen diğer bir özellik de alanlara arama (look up) özelliğinin verilmesidir. Arama özelliği verilen alan tablonun veritablosu görünümünde ve form görünümünde Combo Box ya da List Box olarak yer alır ve kullanıcının değerleri seçerek kolayca girebilmesini sağlar.

Alana arama özelliği düzenlemek için alan tasarımında özellikler alanında Lookup tabı seçilir ve alanın arama ile ilgili seçenekleri düzenlenir.

## **6. Sorgu Yaratmak******

Bir sorgu yaratmak için New query düğmesine basılır. Bir tablo seçildikten sonra yeni nesne (new object) düğmesinden yeni sorgu seçilerek bir sorgu yaratıIır. Bir sorgu yaratmak için önce Database penceresinden Query seçilir. New (Yeni) düğmesine basılır.

Bir sorgu yaratmak için değişik yollar vardır.

Design view Sorgu Tasarım Görünümü

Simple Query Sihirbazı Basit Sorgu

Crosstab Query Wizard Çapraz-tablo Sorgu Sihirbazı

Find Duplicates Query Wizard Tekrarları Bul Sorgu Shirbaıı

Find Unmatched Query Wizard Eşleşmeyenleri Bul Sorgu Sihirbazı

## **6.1 Design View******

Design view düğmesine basılarak yeni bir sorguya başlandığında önce hangi tablo ve sorguların bu yeni sorguda kullanılacağı sorulur. Kullanıcı iletişim kutusundan yeni sorguda kullanılacak olan tablo ve sorguları seçer.

Veritabanı penceresinden sorgular (Queries) ve new (Yeni) düğmesine basılır. Ardından sorguda kullanılacak tablolar seçilir. Seçimde, CTRL tuşu ile çoklu seçim ya da SHIFT tuşu ile de ardışık seçim yapılabilir. Sorguya katılacak nesneler, Tables (Tablolar), Queries (Sorgular) ya da ikisi birden (Both) tabı ile seçilir.

Seçilen elemanların ardından Add (Ekle) düğmesine basılarak sorgu penceresine geçilir. Sorgu penceresinde, seçilen tablolar arasında bir ilişki varsa o da otomatik olarak görülür. Başta seçilip sorgu penceresine eklenen tablolardan başka tabloların da sorguya katılması için Query (sorgu) menüsünden Show Table (Tablo Göster) komutu kullanılır ya da Add Table düğmesine basılır.

Sorgu penceresinde, yeni bir tablo eklemek ya da çıkarmak için farenin sağ tuşu da kullanılır. Seçilen bir tablo üzerinde ya da tablolar alanında boş bir yere fare ile tıklanarak tablo ekleme (Show Table) ya da tablo çıkarma (Remove Table) işlemi sağlanır. Aynı şekilde sorgu penceresinde seçilen tablonun üzerinde farenin sağ tuşuna basılarak elde edilen kısayol menüsünden remove Table (Tablo Çıkar) komutu seçilir.

Sorgu penceresinde, tablolar yerleştirildikten sonra gereksinim durulan alanlar seçilir ve sorgu penceresinin alt tarafına alınır. Ardından alanlar üzerinde gereken düzenlemeler (kriter vb) yapıldıktan sonra sorgunun çalıştırılmasına geçilir.

Yeni bir sorguya başlandığında ekrana sorgu penceresi (query window) gelir. Üzerinde sorgulama işlemlerinin yapıldığı grafik ortam olan sorgu penceresine Örneklerle Sorgu (Query by Example) QBE denir.

**6.1.1 Qbe (Query By Example)******

QBE (Query By Example), değişik sorgulama dillerinin bir uzantısıdır. QBE'nin amacı kullanıcının profesyonelce bir sorgulama dili kullanmadan grafik bir ortamda kullanıcının sorgulamasını geliştirmesidir.

Diğer bir deyişle QBE bir sorgulama tekniğidir. Bir sorgulama dili değildir. QBE, kullanıcının sorulara yanıt vererek karmaşık bir sorguyu geliştirmesini sağlar.

QBE önce veritabanından ilgili tabloların seçilmesiyle başlar. Ardından sorgulamanın yapılacağı kolonlar belirlenir. Örneğin: Müşterinin Adı QBE satırlarında eşittir, eşit değildir, büyüktür vb. ifadeler kullanılır. Bunun dışında QBE satırlarında SQL komutları da kullanılabilir.

**6.1.2 Sorgu Penceresi******

Sorgu penceresinde üç ayrı görünüm sağlanabilir.

• Design View Design View (Tasarım Görünümü)

• Datasheet View (Veritablosu Görünümü) sı

• SQL View (SQL Görünümü)

Tasarım görünümü sorgu penceresinin normal kullanımıdır. Kullanıcı bu ekranı kullanarak sorgusunu tasarlar.

Veritablosu görünümünde; sorgunun sonucunda oluşan veri alt seti (Dynaset) görünür. Diğer bir deyişle sorgu sonucunda elde edilen kayıtlar (çıktı) alınır.

SQL Görünümünde, sorguyu oluşturacak SQL deyimlerinin yazılacağı (ya da oluşturulan sorgunun SQL karşılığı) pencere ekrana gelir.

Bir sorgu yaratırken önce sorg uya konu olacak ya da sorguda alanlarına gereksinim duyulacak olan tablolar seçilir. Ardından tablo alanları sorgu içine dahil edilir. Bir tablonun herhangi bir alanını sorgu alan bölümündeki kolonlara yerleştirmek için alan fare ile istenilen kolonun üzerine bırakılır. Tablolardan birden çok alanın seçilmesi için CTRL ve SHIFT tuşları kullanılır. SHIFT tuşu ile ardışık alanlar bir seferde seçilir. CTRL ile ardışık olmayan çok sayıda alan seçilir.

Bir tablodan bir alan sorgu alanına alındıktan sonra, o kolona ait olan alan listesi açılarak istenilen alan seçilerek alanın değiştirilmesi sağlanır. Alan listesi açılarak istenilen alan seçilir ve alan eski alanın yerine getirilir.

Bir tablonun tüm alanları sorguya katılacaksa o zaman tablo alanlarının üzerinde yer alan yıldız (\*) karakteri kullanılır. Yıldız karakteri fare ile seçilerek sorgu alanına (ilk kolona) bırakılır. Yıldız karakterinin bir kolaylığı da ileride tabloda yapılacak alan değiştirme (ekleme/çıkarma) işlemlerinin sorguya otomatik olarak yansımasıdır.

Sorgu alanına tablonun tüm alanlarını eklemenin diğer bir yöntemi de tablo başlığında çift tıklayarak tablonun tüm alanlarının seçilmesi ve daha sonra seçilmiş alan grubunun bir seferde sorgu alanına eklenmesidir.

Şu andan sonra sorgunun işletilmesi gerekecektir. Bu işlem için Veritablosu görünümü (datasheet view) ya da Çalıştırma (Run) düğmesi kullanılır. Çalışmakta olan (sonuçları üretmekte olan) sorgunun kesilmesi (durdurulması) için CTRL+BREAK tuşları kullanılır.

## **6.2 Simple Query Wizard******

Basit sorgu sihirbazı (simple query wizard) ile yaratılan sorgular, bir tablodan belli alanların seçilmesini sağlarlar. Bu sorgularda kriterler ve diğer işlemler bulunmaz.

• Veritabanı penceresinden sorgu (Queries) seçilir.

• New (Yeni) düğmesine basılır.

• Sorgulanacak tablo ve alanların seçildiği iletişim kutusu ekrana gelir. Ardından sorgunun adı yazılır.

• Daha sonra yaratılan sorgu veritabanında oluşturulur.

• Basit sorgular bir ya da daha çok tablodan belli alanların (kolonların) seçilerek listelenmesini sağlar.

• Yaratılan sorguda daha sonra istenirse tasarım görünümüne geçilerek sorgu için kriterler tasarlanabilir.

## **6.3 Crosstab Query Wizard******

Crosstab (çapraz) sorgular çalışma tablosu biçiminde bir tablonun elde edilmesini sağlar.

• Veritabanı penceresinden sorgu (Queries) seçilir.

• New (Yeni) düğmesine basılır.

• Üzerine çapraz sorgu kurulacak olan tablo seçilir.

• Tablodan sorguya eklenecek alanlar seçilir. (Önce satırları oluşturacak alan seçilir)

• Tablonun ortasında hesaplanacak alan seçilir. (Örneğin tutar, miktar vb.)

• Tablonun kolonlarının başlığını oluşturacak alan seçilir.

• Sorgunun adı verilir.

## **6.4 Find Duplicates Query Wizard******

Tekrar sorgusunda (Duplicates Query) tablonun belli bir alanında bulunan tekrar eden bilgiler bulunur.

• Veritabanı penceresinden sorgu (Queries) seçilir.

• New (Yeni) düğmesine basılır.

• Tablo seçilir.

• Tekrar bilgisi aranacak olan alan seçilir.

• Tekrar bilgisi olan alanın yanısıra ek diğer bazı alanlar da listelenebilir.

• Sorgunun adı verilir.

## **6.5 Find Unmatched Query Wizard******

Eşleşmeyenler (uymayanlar) sorgusu iki tabloyu karşılaştırır. Bir tabloda bulunup da diğer tabloda olmayan kayıtların istenilen alanlarını listeler. Pratikte bir tabloda olan kayıtların belli bir alan üzerinden diğer bir tabloda olup olmadığı karşılaştırılır.

• Veritabanı penceresinden sorgu (Queries) seçilir.

• New (Yeni) düğmesine basılır.

• Ana tablo seçilir. Örneğin satışları olmayan (satış tablosunda kaydı olmayan) müşteriler sorgulanacaksa o zaman müşteriler tablosu ana tablo olarak seçilir.

• Daha sonra sorgunun adı verilir.

• Yardımcı tablo seçilir.

• İki tablo arasındaki ilişki hangi alan üzerinden kurulacaksa o seçilir.

---
*Kaynak: `ACCESS PROGRAMI/ACCESS PROGRAMI.doc` — MEB — 2004*
