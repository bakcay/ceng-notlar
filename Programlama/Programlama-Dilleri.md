# Programlama Dilleri

## **1. PROGRAMLAMA DILLERI**

Programlama dilleri iki ana bölümde toplanabilir:(a)Makineye yönelmiş diller ya da makine dilleri,(b)probleme yönelmiş diller ve bunlara ilişkin programlama sistemleri.

## **1.1. Makine Dili ile Kodlama**

Problem önce,bilgisayarın özellikleri ve mevcut komutlarla yapabileceği işlemler dizisi biçiminde ifade edilir;sonra programcı tarafından bu, bilgisayarın makine dilinde yazılır.Elde edilen makine dilindeki program gerekli veri ile birlikte,bilgisayarca doğrudan doğruya icra edilebilir ve aranan sonuçlar bulunur.Ancak makine dili ile programlamada bazı önemli güçlükler ortaya çıkar.Bütün komutların makine dili ile kodlanması; komutların makine tarafından icra olunacak sırada yazılması ve yanlışlıkla ya da başka bir nedenle bazı komutlar atlanmışsa, bundan sonraki bütün komutların araya eklenenler için ötelenmesi ve adreslemenin yenilenmesi zorunluluğu;bütün lojik ve program düzenlemenin programcı tarafından yapılması;programcının kullandığı bilgisayarı çok iyi anlamış olma gereği bu güçlüklere örneklerdir.

## **1.2. Programlama Sistemleri**

Programlama sistemleri genel olarak bir dil ve bir birleştirici ya da derleyici programdan oluşur.Programlama dili,programcı tarafından kolayca öğrenilebilecek ve yazılabilecek,bilgi işlem sisteminin yapım özellikleri ve yapılacak işlemler arasında uzlaşma sağlayabilecek bir biçimde olmalıdır.Bu dilin,diğer herhangi bir dildeki gibi, dilbilgisi,noktalama ve yazma kuralları olacağı acıktır.

Bir bilgisayarda programlama sistemlerinin bulunması makine dilinde programlamanın güçlüklerini önemli ölçüde azaltır.Birleştirici program ve derleyiciler,programların makine dili dışında probleme yönelmiş bir dilde hazırlanabilmesi olanağını sağlar.Programlama dilinde makine diline çeviriyi,birleştirici ya da derleyici aracılığı ile,bilgisayarın kendisi yapar. Programlama sisteminin dili makineye ya da programa yönelmiş olabilir.

## **1.3. Sembolik Programlama Sistemleri**

Sembolik programlama sistemleri,programcıyı makine dili ile kodlamanın güçlüklerinden büyük ölçüde kurtarır;fakat belli bir bilgisayara göre hazırlandıklarından ve sistemin programlama dilinin kısmen makineye yönelik olmasından dolayı makine dili düzeyinde çalışan ,öğrenilmeleri oldukça uzun suren sistemlerdir ve her bilgisayar için farklıdır,diğer bir deyişle makineye bağlıdır;her bilgisayarda ayni dil kullanılamaz.

## **1.4. Probleme Yönelmiş Diller ve Derleyiciler**

FORTRAN,COBOL,ALGOL, vb. bu tur programlama sistemlerine bazı örneklerdir.Bu tur programlama sistemleri ile çalışmada,temel programın derleyici program aracılığı ile bilgisayarca,belli kurallara uyarak makine dili programına çevrilmesine derleme denir.Derleme sırasında rastlanan dil kurallarına aykırı olan hatalar özel hata mesajları ile bilgisayarca programcıya bildirilir.

Probleme yönelmiş dillerin en önemlilerinden biri,bilimsel ve mühendislik araştırma ve uygulamaları için geliştirilen ve en yaygın olarak kullanılan FORTRAN dilidir.FORTRAN adi,formül çevirisi anlamındaki, İngilizce "FORmula TRANslation" kelimelerinin ilk hecelerinden oluşur.FORTRAN dili sayısal hesapla ilgili herhangi bir problemin kolaylıkla ifade edilebilmesini sağlayacak biçimde düşünülmüştür.Komutlar ya da deyimler herhangi bir güçlük olmaksızın anlaşılabilir ve yorumlanabilir.Bazı deyimler problemin matematiksel bağıntılarına çok benzer. FORTRAN programlama sistemi 1954 yılında J.W Backus tarafından önerilmiş ve ilk kez 1957 yılı baslarında IBM 704 Bilgi İşlem Sisteminde kullanılmıştır.1960 yılında BURROUGHS kendi bilgisayarları için bir FORTRAN derleyicisi hazırlamıştır.Günümüze kadar çeşitli FORTRAN programlama sistemleri geliştirilmiş ve kullanılmıştır.FORTRANII,FORTRANII-D,FORTRANIV bunların en önemlilerine örneklerdir.Genel olarak,bir sonraki işlemin bir öncekine göre daha gelişmiş olduğu ve programlamada daha geniş olanaklar sağladığı söylenebilir.

## **2. FORTRANA GİRİŞ******

## **2.1. GİRİŞ **

Program bir komutlar ( deyimler ) dizisidir ve herhangi bir problemin çözümü için kullanılan hesap düzenini tanımıdır . Çözümde bir bilgisayardan yararlanılacaksa , programın bilgisayar özellilerine uygun bir programlama dili ile yazılması gerekir . Bilgisayar , programdaki komutları aksi belirtilmedikçe , yazıldığı sırada yerine getirir . Gereğinde program bir komutlar kümesinin belli düzende tekrarlanmasını yada duruma göre belirli dallanmaları sağlayacak özel komutlarda içerebilir ; böylece programı kısaltmak mümkün olur .

FORTRAN programlama dili oldukça basittir ve normal matematik diline çok yakındır. FPRTRAN sistemi , FORTRAN dili ve FORTRAN derleyicisinden oluşur .

## **2.2. SAYILAR**

Bilimsel , mühendislik araştırmaları ve uygulamada yapılan hesapların çoğunda değişik büyüklükte sayılarla çalışılır . Güvenilir sonuçlar elde edilmesi için bu hesaplarda mümkün olduğu kadar çok anlamlı rakamı olan sayılarla çalışılması gerekir .

Sabit kelime uzunluklu ve değişken kelime uzunluklu bilgisayarda bir sayının gösterilmesi için bellekte sabit sayıda pozisyon ayrılır . Bu sabit pozisyon sayısına incelik ( prezisyon ) denir .

Sayılar ikiye ayrılır : tam sayılar , gerçel sayılar .

Tam sayılar desimal noktası olmayan sayılardır . Bunlarn büyüklük sınırlarıbilgisayar özelliklerine bağlıdır .

Gerçel sayılar desimal noktalı ondalık sayılardır . Gerçel sayıların bilgisayar belleğinde saklanmasından önce bilgisayarca sayı düzenlenir . Diğer bir deyişle desimal nokta sayının sıfırdan farklı en önemli rakamın soluna kaydırılır ve gerekli düzeltme 10 un üsleri şeklinde sayının yanına yazılır . Düzenlenmiş sayının kesirli kısmı mantis , desimal noktanın kaydırıldığı hane sayısına üs denir . Gerçel sayıların büyüklük sınırları da bilgisayar özelliklerine bağlıdır

## **2.3. Fortran Aritmetiği**

Bilgisayarla yapılan hesaplarda işleme giren büyüklüklerin tamsayı yada gerçel sayı olması , işlemlerin yapılışı ve sonuçlar yönünden büyük farklılıklar gösterir .

Tamsayı aritmetiği , tamsayılarla yapılan işlemler anlamındadır ; her işlemin sonucu da tamsayı olacak biçimde kesilir , yuvarlatma yapılmaz . Kesme işlemi öncelik sırasına göre yapılan bütün işlemler için söz konusudur . Bu nedenle bu tür aritmetik işlemlerin yapılış sırası ve parantezler çok önemlidir . Tamsayılar programlarda eleman numarası , indis, vb. amaçlar için kullanılır . Aritmetik işlemler çoğunlukla gerçel sayılarla yapıldığından tamsayı artimetiğinin bu özelliği bir sakınca değildir .

Gerçel sayı aritmetiği , gerçel sayılarla yapılan işlemler anlamındadır . Burada kesirler prezisyon hanesi kadar rakamla gösterilir ; diğer hanerler bilgisayar özellikerline göre ya kesilir , ya da yuvarlatılır . Kesme hataları ve diğer sayısal hesap yöntemleri konusudur .

## **2.4. Fortran Alfabesi**

FORTRAN alfabesi 10 nümerik , 26 alfabetik ve 13 özel karakterden oluşur .

## **2.5. Karakterler Simge/Anlam **

Nümerik 0 1 2 3 4 5 6 7 8 9

Alfabetik A B C D E F G H I J K L M N O P R S T U V W Y Z

Özel boşluk boşluk bırakma

= yerine koyma

+ artı

- eksi

\* çarpı

/ bölü

( aç parantez

) kapa parantez

. nokta

, virgül

' apotrof

" tırnak

& ve işareti

## **2.6. Fortran Deyimleri **

Bir FORTRAN temel programı bir takım deyimlerden oluşur . Deyimle programın hesap düzeni ile ilgili olarak , bilgisayara bilgi verilmesini , işlemlerin yapılmasını ve icrasını , gerekli kararların verilmesini , sonuçların dış ortama alınmasını sağlar

Deyimlerle bağlantı kurabilmek için , deyimler numaralanabilir . İcra sırası yönünden deyim numaralarının sırasının bir önemi yoktur . Deyi numaraları sadece hesap düzeninin gereği olarak bu deyimlerle dallanabilme olanağı sağlar ; iki deyime aynı numara verilemez .

## **2.7. Fortran İsimleri **

Fortran dilinde dilinde indissiz ve indisli değişkenlere , FORTRAN arşiv fonksiyonların , aritmetik deyim fonksiyonlarına , FUNCTİON altprogramlama isimle verilir

FORTRAN isimleri birincisi nümerik olmayan 1 - 6 alfabetik ya da nümerik karakterden oluşur ; özel karakterler kullanılamaz . Aynı isim birkaç elemana verilemez . Komutlar için ayrılan özel kelimeler FORTRAN özel ismi olarak kullanılamaz

## ** ****3. ****DEYİMLER VE SAYISI GÖREVİ ADLARI**

Aritmetik deyimler yapılacak işlemleri denetler değişken = ifade

Giriş Çıkış deyimleri Dış ortamla bilgisayar arasında bilgi alışverişi sağlar READ

WRITE

FIND

FORMAT

REWİND

BACKSPACE

ENDFILE

REDREAD

NAMELIST

Yönetim deyimleri: Programdaki deyimlerin icra sırasını yönetir Şartsız GO

Hesaplanmış GO TO

Atanmış GO TO

Aritmetik IF

Mantıksal IF

DO

CONTINUE

pause

STOP

END

Bildiri deyimleri : Derleyiciye bilgi verir DIMMENSION

COMMON

EQUIVALANCE

IMPLICIT

Tip deyimi

EXTERNAL

DATA

Altprogram deyimleri: Alt programları tanımlamaya ve kullanmaya yarar FUNCTİON

SUBROUTİNE

CALL

RETURN

ENTRY

BLOCK DATA

## **3.1.Giriş Çıkış Deyimleri**

Giriş çıkış deyimleri bilgisayarlarla dış ortam arasındaki bilgi alışverişini ve çevre bellekte bilgi saklanması yada çevre bellekten bilgi alınması olanağını sağlar giriş çıkış ünitesini ve ortamını , bilginin giriş ortamında yerleşme ve çıkış ortamında yerleştirilme biçimini , bellekte bilgi alışverişi yapacak data alanlarını belirtir . Giriş çıkış deyimler ile ilgili yardımcı deyiler şunlardır:

READ deyimi

WRITE deyimi

FORMAT deyimi

REWİND deyim

BACKSPACE deyimi

ENDFILE deyimi

REDREAD deyimi

NAMELIST deyimi

Bu deyimler aşağıda sırasıyla incelenecektir

## **3.1.1. READ Deyimi **

READ deyim dış ortamdan ve çevre belleklerden bilgisayara bilgi aktarılması olanağını sağlar . Bu deyim bilgisayara bağlı giriş ünitesinden bilgi okunması durumunda

READ ( i, n, l,) liste

ve doğrudan ( rast gele ) erişimli disk kütüğünden bilgi okunması durumunda ise

READ ( i = r, n, l) liste

genel biçiminde yazılır . i, r, n, l, ve liste simgelerinin anlamları sırası ile şöyledir :

i giriş çıkış ünitesi numarasını belirten bir tam say sabit , yada kütük belirtici bir tamsayı sabit yada tamsayı değişkendir . B3700 sisteminde , i = 1,2...7 değerleri için giriş çıkış ortamı şu üniteleri gösterir

i ÜNİTE

1- Magnetik şerit ünitesi 1

2- Magnetik şerit ünitesi 2

2- Magnetik şerit ünitesi 2

2- Magnetik şerit ünitesi 2

5- Kart okuyucusu

6- Baskı makinesi

7- Kart delici

r bir doğrudan erişimli tutanak ( random record ) numarasıdır . Bir işaretsiz tamsayı değişken ya da pozitif tamsayı ifade olabilir " = " yerine " ' " işareti kullanılabilir .

n veri tipini ve dış ortamda yerleşme biçimini belirten ilgili FORMAT deyimimin numarasıdır . Giriş değişken uzunluklu bir şerit kütüğünden ya da bir disk kütüğünden olursa n yazılmayabilir . bu durumda giriş bilgilerinin okunacağı şerit yada disk kütüğü bir formatsız çıkış deyimi ile oluşturulmuş olmalıdır . Formatsız READ deyimi , girişin bir sıralı disk kütüğünden olması durumunda

READ ( i, l) liste

ve girişin bir doğrudan ( rast gele ) erişimli disk kütüğünden olması durumunda ise

READ ( i = r, L) liste

şeklinde yazılır. B3700 sisteminde doğrudan erişimli disk kütüğünden veri okuma durumunda bir FILE kartı kullanılmalıdır .

l giriş çıkış sırasında uygunluk hatası ( parity error ), yada kütük sonu ( End-of-Fıle )durumu ile karşılaşırsa yapılacak eylemi ve dallanılacak değimi belirtir ;n1 , n2 deyim numaraları olmak üzere

ERR = n1

END = n2

ERR = n1 , END = n2

END =n2 , ERR =n1

biçimlerinde yazılır . Veri okuma sırasında , sistemin bulup düzeltemediği bir uygunluk hatası ortaya çıkarsa kontrol n1 numaralı deyime ; kütük sonu durumu ile karşılaşırsa kontrol n2 numaralı deyime dallanır . Kütük sonu durumu ile , ( a ) 1. kolonda bir geçersiz karakter bulunan bir kart okuma ; ( b ) şerit yada diskte yazılı son kayıttan daha ötesini okuma çabası ; ( c ) diskin yazılı olmayan alanından bir kayıt okuma sırasında karşılaşılır . READ deyiminin yazılışında l kısmı bulunmayabilir . Bu durumda deyim

READ ( i, n,) liste

yada

READ ( i = r, n,) liste

biçiminde yazılır . Bu deyimlerin icrası uygunluk hatası ve kütün sonu durumları ile karşılaşıldığında icra durur

Liste indissiz yada indisli değişken ve dizi isimlerinden oluşur bunlar

d1, d2, ... , dn

şeklinde araları virgülle ayrılmış olarak sıra ile yazılır . Listedeki değişkenlere dış ortamdan okunan değerler atanır. Bu nedenle listedeki değişkenlerle dış ortamdan okunan değerler sıra , sayı ve mod bakımından uyuşmalıdır . Listedeki dizi imi indissiz yazılmışsa , bu dizinin tümü kolon düzeninde okunur .

## **3.1.2. WRITE Deyimi **

WRITE deyimi bilgisayar belleğinden dış ortama ve yardımcı bellek ünitelerine bilgi aktarma olanağı sağlar . Bu deyim bilgisayara bağlı bir çıkış aygıtından bilgi alınması durumunda

WRITE ( i, n, liste

genel biçiminde yazılır . Deyimin yazılışında n bulunmayabilir Formatsız Write deyimi , bir şerit ya da sıralı disk kütüğü çıkışında

WRITE ( i) liste

ve doğrudan ( rast gele ) erişimli disk kütüğü çıkışında ise

WRITE ( i = r) liste

biçiminde yazılır . Buradaki i , r , n ve liste simgelerinin anlamlar ve özellikleri READ deyiminde ayrıntıları ile açıklandığı gibidir .

## **3.1.3. FORMAT Deyimi **

Format deyimi bilgisayara bilgi giriş çıkışlarında data özelliklerini , yani verinin ne tipte ve ve ne uzunlukta olduğunu belirtir . Bir yada daha çok giriş çıkış deyimi ile ilişkili olan bu deyim

n FORMAT ( f1 , f2 , ..fn)

şeklinde yazılır . Buradan n giriş çıkış deyimlerinde belirtilen deyim numarası ve f1 , f2, .. , fn ise FORMAT deyimin bağlı olduğu giriş çıkış listesindeki değişkenlerin değerlerinin hangi formda dönüştürüleceğini gösteren alan bildirileridirler . Alan bildirileri ve giriş çıkış listesindeki değişkenle sayı , sıra ve mod bakımından uyuşmalıdırlar .

Format deyimi icra edilemez türde bir deyimdir ; fonksiyonu amaç programda bilgi iletimini istenen düzeyde gerçekleştirmekti . Bu nedenle Temel Programın içinde herhangi bir yerde bulunabilir ; yalnız DO çevrimi kapsamının son deyimi olamaz .

FORMAT deyimindeki alan bildirilerinin gösterdiği karakterlerin toplamı , bir satır için en çok bir kayıt birimi kadar olabilir . Kayıt birimi IBM kartı için 80 , daktilo kağıt şerit için 87 , B9247 baskı makinesi için ise 132 karakter olarak sınırlandırılmıştır .

Çeşitli alan bildirilerinin yazılışları , giriş ve çıkış için kullanıldıklarında dönüştürme özellikleri ve FORMAT deyimine ilişkin ayrıntılar aşağıda açıklanacaktır .

I tipi alan bildirisi

Tamsayı büyüklüklerin giriş çıkışında kullanılır ; W alan uzunluğunu göstermek üzere

Iw

şeklinde yazılır

GİRİŞ . Veri tamsayı sabit olmalıdır ve sayı ala içinde sağdan hizalanmalıdır . Sayının işareti de w içindedir . Tamsayı büyüklüğü alan uzunluğunu aşmamalıdır .

ÇIKIŞ . Çıkış listesindeki bu alan bildirisine ilişkin tamsayı değişkeninin değeri , dış ortamda belirtilen kayıt ortamındaki alan içine sağdan hizalanarak yazılır . Artı işareti basılmaz , eksi işareti ise basılır . Tamsayı büyüklüğünün değeri ( işareti ile birlikte ) w den büyük bir sayı ise basılmaz , alan \* işareti ile doldurulur .

F tipi alan bildirisi

Gerçel sayıların giriş çıkışı için kullanılır . w alan uzunluğu , d sağdan itibaren desimal noktanın yerini göstermek üzere

Fw.d

şeklinde yazılır . w alan uzunluğu seçilirken işaret ve desimal nokta için de birer yer düşünülmelidir ;bu nedenle w >= d + 2 olmalıdır .

Giriş . veri gerçel sayı olmalı ve sayı alan içinde sağdan hizalanmalıdır . Alan bildirisinde desimal sayını yeri belirtildiğinden , verilerde desimal nokta yazılmayabilir . Verideki desimal noktanın yeri alan bildirisinde gösterilene göre önceliklidir . Buna göre F10.0 alan bildirisi , herhangi bir üssüz gerçel sayının bilgisayara aktarılması olanağını sağlar .

E tipi alan bildirisi

Üslü gerçel sayıların giriş çıkışı için kullanılır ;

Ew.d

şeklinde yazılır . w alan uzunluğunu , d bu alanda E den itibaren desimal noktanın yerini belirtir .

GİRİŞ . Alan içinde desimal noktanın yeri bildirildiğinden veride desimal nokta yazılmayabilir . Verideki desimal noktanın yeri alan bildirisinde gösterilene göre önceliklidir . Buna göre E10.0 alan bildirisi , herhangi bir üslü gerçel sayının bilgisayara aktarılabilmesi olanağını sağlar . Üslü gösterim durumunda verinin alan içinde sağdan hizalanması gerekir .

ÇIKIŞ . Dış ortamda w sayıda yer ayrılır ; bunun içinde işaret ve desimal nokta için birere yer ve üs için dört yer olmak üzere toplam 6 yer vardır . w - d >= 6 olmalıdır ; bu kurala uyulmazsa çıkış alanı \* işaretleri ile doldurulur . Gerçel sayı prezisyonu f olduğuna göre , dil ortamda işaret ( pozitif ise basılmaz ) , desimal nokta ve üssü belirtmek için gerekli 6 karakterden başka , f > ( w - 6 ) ise f anlamlı hane , f >= ( w - 6 ) ise ( w - 6 ) anlamlı hane görünecektir . Alan bildirisinde bir n ölçek katsayısı kullanıldığında , bu sayı ile ile üs kısmı arasında bir desimal düzenleme yapma olanağı verir . n <= 0 ise , desimal noktanın solunda n anlamlı basamak konulur , bunu desimal noktanın solundaki ( d - n + 1 ) anlamlı basamak izler . Her iki durumda da üs uygun biçimde ayarlanır .

D tipi alan bildirisi

Çift incelikli gerçel sayıların giriş çıkışında kullanılır ;

Dw.d

Şeklinde yazılır . w alan uzunluğunu , d ise desimal noktanın yerini gösterir .

GİRİŞ . Çift incelikli gerçel sayı üslü yazılmışsa üs D harfi ile gösterilir . Giriş verisinin yazılış biçimine göre Fw.d ya da Ew.d dönüştürmeleri gibi çalışır

ÇIKIŞ . Çift incelikli sayıların dış ortama aktarılmasında kullanılmasının ve üssün D simgesi ile gösterilmesisin dışında Ew.d dönüştürülmesi gibi çalışır

L tipi alan bildirisi

Mantıksal büyüklüklerin giriş çıkışında kullanılır ;

Lw

şeklinde yazılır w alan uzunluğunu gösterir

GİRİŞ . w alan uzunluğu >= 1 olmalıdır ; başta boşluklar olabilir . Giriş alanındaki ilk karakter TRUE ( doğru ) için T ve FALSE ( yanlış ) için F olmalıdır . Bunları izleyen karakter göz önüne alınmaz . Giriş Alanında T ya da F yoksa bu bilgisayar belleğine FALSE olarak aktarılır .

G tipi alan bildirisi

Tamsayı , gerçel çift incelikli , kompleks ve mantıksal büyüklüklerin giriş çıkışında kullanılabilecek bir genel alan bildirisidir ;

GW.d

şeklinde yazılır . w alan uzunluğunu d desimal noktanın yerini belirler .

GİRİŞ . Giriş verisi I ya da L tipinde ise , Gw.dalan bildirisi Iw ya da Lw olarak çalışır .d kısmı göz önüne alınmaz ; F , E ya da D tipinde ise Fw.d , Ew.d ya da Dw.d biçiminde çalışır . Giriş değişkeni kompleks ise gerçek ve sanal kısımlar için iki ayarı G alan bildirisi gereklidir

ÇIKIŞ . I yada L tipi büyüklerin çıkışında Iw olarak çalışır gerçel sayılar durumunda çıkış biçimi sayıların büyüklüğüne bağlı olarak aşağıdaki gibi çalışır

Değişkenin büyüklüğü Eşdeğer dönüştürme

0,1 <= n < 1 F( w -4).d , 4X

1 <= n < 10 F( w -4).( d - 1 ) , 4X

... ...

... ...

... ...

10( d - 2 ) <= n < 10( d - 1 ) F( w -4).1 , 4X

10( d - 1 ) <= n < 10( d ) F( w -4).0 , 4X

diğer Ew.d

Çıkış değişkeni kompleks türde ise , gerçek ve sanal kısımlar için iki ayrı G alan bildirisi gereklidir.

Gerçel ve çift incelikli büyüklüklerin çıkışında w alan uzunluğu , üs desimal nokta ve işaret ( negatif ise ) için gerekli yerleri içermelidir . ( w - d ) >= 6 şartı sağlanmazsa , çıkış ortamı \* işaretleri ile doldurulur .

Z tipi alan bildirisi

Hekzadesimal büyüklüklerin giriş çıkışı için kullanılır ;

Zw

şeklinde yazılır . w alan uzunluğunu belirtir GİRİŞ . Veri hekzadesimal sabit olmalıdır . Giriş alanındaki boşluklar sıfır olarak yorumlanır . Veri sağdan hizalanmış olmalıdır . Giriş verisi uzunluğu >w ise fazla haneler kesilerek soldan kesilerek bilgi belleğe aktarılır .

ÇIKIŞ . Hekzadesimal değer çıkış ortamına sağdan hizalanmış yazılır ; kalan yerler varsa boş bırakılır . Değişkenin uzunluğu > w ise fazla haneler soldan kesilerek yazılır

A tipi alan bildirisi

Alfa nümerik büyüklüklerin giriş .çıkışı için kullanılır ;

Aw

şeklinde yazılır .w alan uzunluğunu gösterir .

GİRİŞ . Alfa nümerik bilgi bellekte karakter formunda saklanır ; bu nedenle hesaplamalarda kullanılamaz . Bilgi giriş alanında sağdan hizalanmış olmalıdır . w < b ise , alfa nümerik büyüklük soldan hizalanmış olarak bellekte değişken olarak saklanır ; b - w boş yer kalır .

ÇIKIŞ . Alfa nümerik bilgi çıkış ortamından sağdan hizalanarak yazılır . w > b değişken uzunluğu ( byte cinsinden ) ise , alfa nümerik karakter dizisi çıkış ortamına soldan hizalanarak konulur ve sağdan b - w karakter kesilir .

H tipi çıkış bildirisi

Bir karakter dizisini giriş çıkışı için kullanılır ;

wHs

şeklinde yazılır . w alan uzunluğunu , s karakter kümesini gösterir . Aynı işlem karakter dizisinin alan uzunluğunu belirtmeden 's' "s" şeklinde yazarak da gerçekleştirilebilir .

GİRİŞ . w sayıda karakter yerine s karakter kümesi geçer ; boşluk karakterleri de bunun içindedir .

ÇIKIŞ . Bildiriden sonra gelen w sayıda karakter , ya da bir giriş işlemi sonucu onun yerine geçirilmiş karakterler dış ortamda görünür .

X tipi alan bildirisi

Giriş çıkışta boşlukları göstermek için kullanılır ;

wX

şeklinde yazılır . w alan uzunluğunu gösterir . Girişte w karakterlik yerin atlanmasını , çıkışta ise w sayıda karakterlik boşluk bırakılmasını sağlanır .

T tipi alan bildirisi

Giriş çııl listelerindeki verilerin ilk karakterlerinin bulunduğu yeri belirlemekte kullanılır , n bu yeri göstermek üzere

Tn

şeklinde yazılır . Baskı makinesi ile çıkışta kullanıldığında veri gerçekte ( n - 1 ) karakter konumundan başlar ; çünkü kaydın ilk karakteri şaryo kontrolü için kullanılır .

Ölçek katsayısı :

F , E ve D tipi alan bildirileri ile birlikte , giriş çıkışta sayıları düzenlemekte kullanılır . Örneğin F tipi alan bildirisi ile , n ölçek katsayısı olduğuna göre ,

nPFW.d

şeklinde yazılır . Bu yazılım çıkışta kullanılmışsa

dış ortamdaki sayı = bellekteki değeri X 10n

olur . Ölçek katsayısı pozitif ya da negatif olabilir . Düşünce geneldir ; giriş ve çıkışta geçerlidir . Ancak çoğunlukla çıkışta kullanılır .

Ölçek katsayısı E tipi alan bildirisi ile kullanılırsa , girişte herhangi bir etkisi olmaz ; çıkışta mantis^n ile çarpılır , üs n kadar azaltılır

Alan bildirilerinin ve grupların tekrarı

Herhangi bir kayıt içinde n sayıda alanı aynı tipte yazmak için ilgili alan bildirisinin önüne n sayısına yazmak gerekir . n işaretsiz bir tamsayıdır . Eğer bir ölçek katsayısı da kullanılıyorsa , bu tekrar sayısının da önünde bulunur .

Alan bildiri gruplarının tekrarı ise bunu parantezler içine alarak önüne n tekrar sayısı yazmaklar sağlanır. Grup tekrar sayısı belirtilmemişse bu grup giriş çıkış bitinceye kadar tekrarlanır . Parantezler içine alarak gruplama dokuz düzeyde olabilir

alan tekrarı durumunun dışında FORMAT deyimi soldan sağa doğru yorumlanır . Giriş çıkış listesi bitmeden FORMAT deyiminin en sağındaki paranteze gelinmişse , diğer bir deyişle FORMAT deyimi bitmişse , denetim en son rastlana sol paranteze geri döner ; giriş çıkış listesi tamamlanıncaya kadar bu işlem tekrarlanır . Giriş çıkış listesi bitmesine rağmen FORMAT deyiminin en sağ parantezine , sonuna gelinmemiş olsa bile giriş çıkış deyiminin icrası tamamlanmış olur .

Çok kayıtlı alan bildirileri

FORMAT deyimi içindeki bir / işareti bir kayıtın bitip ikinci bir kayıta geçildiğini gösterir . Girişte / işaretinsen sonraki karakterler göz önüne alınmaz . Çıkışta ise / işaretine rastlandığında kayıt bitirilir ve kalan çıkış bilgileri bir sonraki kayıta konulur . Girişte kayıt atlamak ve çıkışta boş satır bırakmak için ardışık / işaretleri kullanılabilir . Genel olarak n+1 sayıdaki / işareti n sayıda boş satır bırakılmasını sağlar

İcra zamanında verilen format deyimi

Herhangi bir formatlı giriş çıkış deyiminde numarası bulunan ilgili format deyimi A tipi alan bildirisi ile yazılır ; böylece alan bildirilerini icra zamanında veri gibi okuma mümkün olur .

## **3.1.4. FIND Deyimi **

Bu deyim

FIND ( F = r )

şeklinde yazılır . Okuma zamanından önce bir tutanağın yüklenmesini sağlar . Tutanak tampon bellekte ( buffer ) değilse , Kullanılabilecek bir tampon bellek varsa , tutanağı içeren blokta okuma başlatılır ; yoksa FIND göz önüne alınmaz . Bir READ deyimi icra edildiğinde , okunacak bir tutanak olup olmadığını anlamak için tampon bellek kontrol edilir ; tutanak yoksa tutanağı içeren bloktaki READ başlatılır .

REWİND deyimi

Şerit ya da disk kütüphanelerinde kullanılan bir deyimdir ;

REWIND

şeklinde yazılır . Bu deyimin icrası kütüğünün başlangıç konumuna getirilmesini sağlar . Kütüğünün son referansı bir WRİTE deyimi ise , başlangıç konumuna dönülmeden önce , kütük kapatılır . REWIND deyimi şerit ya da disk kütüklerinden başka yerde tanımsızdır .

## **3.1.5. BACKSPACE Deyimi **

i kütüğünden gösterge m kaydında bulunuyorsa BACKSPACE deyiminin icrası kütük göstergesinin bir önceki ( m - 1 ) . kayda gelmesini sağlar . Bu deyim

BACKSPACE i

şeklinde yazılır ; yalnız magnetik şerit . disk yada kağıt şerit giriş kütükleri için tanımlanmıştır . i kütüğü başlangıç konumunda ise , bu deyimin icrasının hiçbir etkisi olmaz .

## **3.1.6. ENDFILE Deyimi **

Bu deyim kütüğün kapatılmasını sağlar ve

ENDFILE i

genel biçiminde yazılır . Yalnız şerit kütükleri için tanımlanmıştır . Bir i kütüğünde WRITE deyimini izleyen bir ENDFILE deyimi varsa , bir kütük sonu ( END - OF - FILE ) kaydı yazılır ve şerit bir sonra yazılacak kayıt , kütük sonu kaydını izleyecek biçimde konumlandırılır . i kütüğünde ENDFILE deyimi bir READ deyimini izlerse , bitiş etiketlerine rastlanmışsa , şerit bir sonraki kütük başlangıcına konumlandırılır ; bitiş etiketine rastlanmamışsa geri sarılır .

Kapatılmış bir kütükte BACKSPACE , ENDFILE , REWIND deyilerinden birinin icrası ile karşılaşırsa , bu deyim göz önüne alınmaz .

REREAD Deyimi

Bu deyim herhangi bir kütükte okunan en son kayda yeniden erişilmesini sağlar ;

REREAD

genel biçiminde yazılır . İcra edilecek bir sonraki READ deyimi ile ilişkilidir ; son kaydın kütükten okunmasını sağlar . REREAD deyiminden önce gelmelidir .

## **3.1.7. NAMELIST Deyimi **

NAMELIST deyimi değişken yada dizi isimleri kümesinin bir tek isimle belirlenmesini ve giriş çıkışta READ ya da WRTITE deyimi listesine gerek kalmaksızın giriş çıkış yapılabilmesini sağlar . Bu deyim

NAMELIST / ad /i1 ,i2..../ ad2/in

genel şeklinde yazılır . Burada her ad bir isim listesi tanıtıcısı , her biri değişken ve dizi isimlerinden oluşan bir listedir . Bir değişken ya da dizi ismi , birden çok adi ile ilişkili olabilir .

GİRİŞ . NAMELİST deyimini izleyen bir READ deyimi yazarak sağlanır . Veri kütüğünün her kaydının ilk karakteri göz önüne alınmaz ; ilk kayıtın ikinci karakteri ise & işareti olmalıdır . READ deyimini izleyen tanıtıcı ad , & işaretinden sonra gelir . Veri kütüğünde ikinci bir & işaretine rastlandığında ( bunu bir end deyimi izler ) okuma durur .

ÇKIŞ. f yerine daha önce bildirilmiş bir NAMELIST adı bulunan bir formatlı çıkış deyimi icra ederek çıkış yapılır.

## **3.2. FORTRAN-KONTROL Deyimleri**

1.CALL deyimi

2.CONTINUE deyimi

3.DO deyimi

4.END deyimi

5.GO TO deyimleri

6.IF deyimleri

7.PAUSE deyimi

8.RETURN deyimi

9.STOP deyimi

## **3.2.1. \*CALL Deyimi**

-Kontrolü bir subroutine alt programına aktarır,

-Gerçek argümanların ifadelerini değerlendirir,

-Gerçek argümanlarla yapay argümanları belirler.

Genel formatı:CALL ad \[(\[arg1\[,arg2\]\[,arg3\]....\])\]

Burada ad,bir subroutine alt programının veya bir ENTRY(giriş) noktasının adidir.Bu ad,FUNCTION,SUBROUTINE ve ENTRY deyimindeki yapma bir argümanın adi olabilir.

Arg, subroutine alt programı tarafından istenen gerçek bir argümanın adidir.Bu argüman bir değişken,bir sabite,dizi elemanı,dizi adi,aritmetik,lojik veya karakter ifade olabilir.Ayrıca bir FUNCTION, SUBROUTINE adi olabilir veya CALL deyiminin bulunduğu program biriminde bulunan ifade edilebilir bir deyimin deyim numarasının başına (\* ) gelerek bir argüman oluşturulabilir.Eğer gerçek argüman yoksa parantez kullanılmaz.CALL deyimi kontrolü subroutine alt programına aktarır ve CALL deyiminde bulunan gerçek argümanların değerleri yerine yapay değişkenleri getirir.

## **3.2.2. \*CONTINUE Deyimi**

Continue deyimi ifa edilebilir bir kontrol deyimidir,fakat ifanın sırasına etki etmez.Bu deyim DO döngüsünün sonunu belirlemek amacıyla veya programda bir etiket görevi için kullanılır.

Genel formati:CONTINUE

Continue deyimi ifanın sırasına etki etmediğinden kaynak programın herhangi bir yerinde kullanılabilir.Genellikle DO döngüsünün son deyimi,koşulsuz veya assign'e bağlı GO TO,blok IF, ELSE IF, ELSE , END IF, STOP, RETURN , END,aritmetik IF,başka bir DO deyimi veya lojik IF deyimi olamaz.Bundan kaçınmak için CONTINUE deyimi kullanılır.

Örnek:Aşağıdaki program parçasındaki ilk CONTINUE deyimi etiket amacıyla ,ikinci CONTINUE deyimi ise DO döngüsünün sonunu belirtmek için kullanılmıştır. IF (A-B)15,20,15

15 X=A+B\*\*2

20 CONTINUE

.

.

DO 40 I=1,K

KN(I)=X+I

40 CONTINUE

.

.

## **3.2.3. \*DO Deyimi**

DO deyimi kendisinden sonra gelen ve belirlenen bir deyime kadar olan tüm deyimleri tekrar tekrar ifa edilmesini sağlar.Bu deyimler <<DO döngüsü>>olarak

adlandırılır.Genel formati:Araligin sonu ffffDO değişkeni başlangıç degeri son değer Arg DO d1\[,\]= m2 \[,m3\]

Burada d1,DO deyiminin bulunduğu programda ve DO deyiminden sonra gelen ifa edilebilen bir deyimin numarasıdır.d1'den sonra gelen virgül seçimliktir.i, DO değişkeni olarak adlandırılan bu değişken ,bir tamsayı,gerçel veya çift duyarlıklı bir değişkendir (dizi elemanı olamaz)

m1,m2,m3 bir tamsayı,gerçel veya çift duyarlıklı aritmetik ifadedir.m1,m2 ve m3 ifadelerinin değerleri ,eğer gerekirse ,DO değişkenin tipine dönüştürülür.m3 seçimliktir ve hiçbir zaman sıfır olamaz.Eğer m3 belirtilmezse değeri 1 olarak alınır ve m3'den sonra virgül konmaz.

Aşağıdaki kuralların geçerli olması halinde DO döngüsü içindeki deyimler ifa edilir.

a)m1,m2'den küçük veya eşit ve m3 sıfırdan büyükse

b)m1,m2'den büyük veya eşit ve m3 sıfırdan küçükse

Eğer m1,m2 ve m3 arasındaki ilişkilerden biri doğruysa ,ilk önce DO döngüsü içindeki ilk deyim ifa edilir.Bu anda i'nin baslangıç değeri m1' dır.Her bir ardışık iterasyonda i'nin değeri m3 kadar artırılır.Iterasyon sayısı MAX(INT((m2-m1+m3)/m3),0) oluncaya kadar döngü devam eder.

Örnek:DO 5 IX=1,12,4 deyimi ile döngü, (m2-m1+m3)/m3=(12-1+4)/4=15/4=3,75

INT(3,75)=3

MAX(3,0)=3 kez tekrarlanır.

Eğer ilk anda i'nin değeri m2'yi geçerse iterasyon durur ve kontrol d1'den sonraki deyime geçer.DO nun tamamlanmasından sonra DO değişkeni i'nin son degerim2'yi geçer.

Eğer (a) ve (b)'deki ilişkilerden biri doğru değilse kontrol doğrudan d1'den sonraki deyime geçer.

DO değişkeni DO döngüsü içinde yeniden tanımlanamaz.Bununla birlikte , m1,m2 veya m3'ün DO döngüsü içindeki değerleri ,iterasyon sayısını değiştirmeksizin yeniden tanımlanabilir.

Doğru DO deyimleri:

DO 50,INT=1,5,2

DO 60X=BAS,BIT,ART

DO 3,A=20,3,-3

DATA deyiminde üstü kapalı belirtilen DO:

Bir data deyimindeki üstü kapalı belirtilen DO listesinin genel formati: (dliste,i=m1,m2\[,m3\])

Burada d liste, dizi eleman adlarının ve üstü kapalı belirtilen DO'ların listesidir.i,bir tamsayı değişken adi olup üstü kapalı belirtilen DO değişkeni olarak adlandırılır.m1,m2 ve m3 değerlerinin her biri bir tamsayı sabite veya bir tamsayı sabitenin adidir.Ayrıca tamsayı sabite adları veya tamsayı sabitelerden oluşan bir ifade olabilir.m3 seçimliktir,eğer kullanılmazsa 1 olarak kabul edilir ve m3'den önceki virgül kullanılmaz.

Üstü kapalı belirtilen DO döngüsünün tamamlanmasından sonra DO değişkeni tanımsızdır ve bir DATA deyiminde ,atama deyiminde veya READ deyiminde değeri belirtilinceye kadar kullanılmaz.

Örnek:15 boyutlu bir matrisin oluşturulması

DIMENSION A(15,15)

DATA ((A(I,J),J=1,15), I=1,15)/225\*0./

DATA (A(I,I),I=1,15)/15\*1./

Bir Giriş Çıkış deyimindeki üstü kapalı belirtilen DO:

Bir giriş çıkış deyimindeki listede üstü kapalı belirtilen DO döngüsü kullanılıyorsa, bu döngü ile belirlenen değerler bir dış ortamdan belleğe veya bellekten bir dış ortama aktarılacaktır.

Giriş/çıkış deyimindeki üstü kapalı belirtilen DO deyiminin genel formati:

(dliste,i=m1,m2\[,m3\])

Burada dliste, bir giriş/çıkış listesidir. i, tamsayı,gerçel veya çift duyarlıklı değişken adi olup DO değişkeni olarak adlandırılır.m1,m2 ve m3 tamsayı, gerçel veya çift duyarlıklı aritmetik ifadedir. m1,m2 ve m3 ifadelerinin değerleri DO değişkeni i'nin tipine dönüştürülür.m3 seçimliktir ve sıfır değerini alamaz,kullanılmazsa 1 olarak kabul edilir ve m3'den önceki virgül de yazılmaz.

Örnek: Farz edelim ki A bir değişken, B,C ve D ise tek boyutlu diziler olsun. B,C ve D'nin 20 elemanlı olduğunu kabul edersek,

READ(UNIT=5)A,B,(C(I),I=1,4),D(4) deyimi ile ilk değer A'ya,sonraki 20 değer B'ye ,daha sonraki dört değer C'nin ilk dört değeri olarak C'ye ve son değer de D'nin 4'üncü elemanına okunur veya WRITE(UNIT=9)A,B,(C(I),I=1,4),D(4) deyimi ile önce A'nin değeri,sonra B'nin 20 değeri,daha sonra C'nin ilk dört değeri ve son olarak da D'nin 4'üncü degeri yazılır.

Eğer gerekiyorsa üstü kapalı belirtilen DO'lar bir arada kullanılabilir.Mesela 10\*20'lik bir A dizisi ile 10 boyutlu bir B dizisini göz önüne alalım.A'nin her bir satiri okunduktan sonra ,B'nin bir elemanını okutmak istiyorsak,aşağıdaki deyimi kullanabiliriz:

READ(UNIT=5) ((A(I,J), J=1,20), B(I), I=1,10)

Benzer şekilde A'nın her bir satirini yazdıktan sonra B'nin bir elemanını yazdırmak için aşağıdaki deyimi kullanırız:

WRITE(UNIT=9) ((A(I,J), J=1,20), B(I), I=1,10)

## **3.2.3.1 DO Deyimine İliskin Kurallar:**

1.DO döngüsü içinde herhangi bir fortran deyimi kullanılabilir.Fakat döngünün son deyimi koşulsuz veya assign'e bağlı GO TO, blok IF, ELSE IF, ELSE, END IF,STOP,RETURN ,END ,aritmetik IF,lojik IF veya bir başka DO deyimi olamaz.Bundan kaçınmak için genelde DO döngüsünün son deyimi olarak CONTINUE deyimi kullanılır.

2.Bir DO alanı içinde başka DO döngüleri olabilir.Ancak içteki DO alanının tamamı dıştaki DO alanın içinde kalmalıdır. İçteki DO ile dıştaki DO alanlarının bitişi ayni deyime rastlayabilir.

DO 10ffI = 1,N DO 100 K = 1,N,2

DO 15 hJ = 1,M DO 105 L = 1,M,3

....... ...... ........... .........

....... ...... ........... ..........

15 CONTINUE ..........................................100 CONTINUE

10 CONTINUE ...........................................105 CONTINUE

doğru olduğu halde ...................................... yanlıştır.

3.DO alanı içinde DO nun indisleyici parametreleri olan i , m1 , m2 ve m3 ü değiştiren, yeniden tanımlayan bir deyim kullanılamaz.Mesela aşağıdaki program birimindeki M = I + 1 deyimi hatalıdır.

........ .........

M = 2

DO 5. I = M,5

M = I + 1

X = A(I)\*B(M)

5 CONTINUE

........ ............

4.DO alanı içinden bu alanın disina atlamak mümkündür. Sapma anında DO değişkeninin değeri son aldığı değerde kalır.Fakat DO alanı içine bu alanın dışından girmek mümkün değildir.Çünkü bu durumda DO değişkeninin değeri belirlenemez.

## **3.2.4. \*END Deyimi**

Bir programın sonunu tanımlayan END deyimi anaprogramın veya function, subroutine veya blok data alt programlarının ifasını durdurur.

Genel formati: END

END deyimine numara verilebilir.Bu deyim bir program biriminin son deyimi olup, programdaki herhangi bir deyimden önce gelemez.Eğer ana programda ise,ana programın ifasını durdurur, altprogramda ise RETURN deyimi gibi işlem görür.

END deyimi ifa edildiği anda ,altprogramdaki yapma argümanlar ile gerçek argümanlar arasındaki bağlantı kesilir.Altprogramdaki tüm birimler aşağıdakiler hariç olmak üzere tanımsız olur. -SAVE deyiminde tanımlanan birimler,

-Etiketsiz COMMON'daki birimler,

-Başlangıçta tanımlanan birimlerden yeniden değer almamış veya tanımsız olmamış olanlar,

-Hiç olmazsa başka bir program biriminde de görünen bir altprogramdaki etiketli COMMON bloklar.

Function alt programındaki END deyimi:

Tüm function alt programları END deyimi ile bitmelidir.Ayrıca bu altprogramlarda RETURN deyimi de bulunabilir.END deyimi fiziksel olarak altprogramı n sonunu belirler.

Subroutine alt programındaki END deyimi:

Tüm subroutine alt programları END deyimi ile bitmelidir.Ayrıca RETURN deyimleri de bulunabilir(altprogramin farklı yerlerinde).END deyimi altprogramın fiziksel olarak bittiğini belirler.Eğer bir subroutine alt programın ifası esnasında END deyimine ulaşılırsa ,bu deyim RETURN deyimi gibi ifa edilir.

## **3.2.5. \*GO TO Deyimleri**

GO TO deyimleri kontrolü programdaki ifa edilebilen bir deyime aktarır.Üç tür GO TO deyimi vardır:

-Assign'a bağlı GO TO deyimi,

-Hesaplanış GO TO deyimi,

-Koşulsuz GO TO deyimi.

Assign'a bağlı GO TO deyimini görmeden , bir atama deyimi olan ASSIGN deyimini inceleyelim.

Assign deyimi: ASSIGN deyimi tamsayı bir değişkene bir sayı atar.

Genel formatı: ASSIGN d TO i

Burada d, ASSIGN deyimini içinde bulunduran bir program birimindeki ifa edilebilen bir deyimin veya bir FORMAT deyiminin numarasıdır.

i, 4 bayt uzunluğunda olan bir tamsayı değişkenin (bir dizi elemanı olamaz) adidir. Bu değişken deyim numarası d'ye atanmaktadır.Deyim numarası ASSIGN deyiminin bulunduğu program birimindeki bir deyimin numarası olmalıdır.ASSIGN deyiminin ifa sı , bir değişkenin bir deyim numarası tarafından tanımlanması ile olur.Bu değişken ,Assign'a bağlı GO TO deyiminde veya bir giriş/çıkış deyiminde belirlenen bir format deyiminde verilen deyim numarası ile tanımlanabilmelidir.Bir deyim numarası ile tanımlanan bu tamsayı değişken ,ayni veya farklı deyim numaraları ile veya bir tamsayı değer ile yeniden tanımlanabilmelidir. Eğer d ifa edilebilen bir deyim numarası ise i değişkeni Assign'a bağlı bir GO TO deyiminde kullanılabilir.Eğer d bir FORMAT deyiminin numarası ise i değişkeni format kontrolü bir, READ, WRITE veya PRINT deyimindeki format tanımlayıcısı olarak kullanılmalıdır.

## **3.2.5.1. Assign'a bağlı GO TO Deyimi:**

Assign'a bağlı GO TO deyimi , i nın o andaki değerine bağlı olarak kontrolü d1 , d2 , d3 ,..... ile numaralandırılmış deyime saptırır.Örneğin i nin değeri d2 ise GO TO ... deyimi ile d2 no lu deyime sapılır.

Genel formatı:

GO TO i \[ \[, \](d1 \[ , d2\]\[ , d3 \]...) \]

Burada i , bir ASSIGN deyimi ile bir deyim numarası atanan 4 bayt uzunluğundaki bir tamsayı değişkendir(bir dizi lemanı olamaz).d assign'a bağlı GO TO deyimini içinde bulunduran program birimindeki ifa edilebilen bir deyimin numarasıdır.( d1 , d2 , ....) ile gösterilen numaraları listesini kullanmak zorunlu değildir.Eğer bu liste kullanılmazsa i den sonra gelen virgül de kullanılmaz.Ayrıca bu liste kullanılsa da i den sonraki virgül kullanılmayabilir.Assign'a bağlı GO TO deyiminin kullanıldığı program biriminde bulunan ve i değişkenine atanan

deyim numarası listedeki deyim numaralarından biri olmalıdır.Deyim numarası listede birden çok görülebilir.Yani , d1 = dj = .... olabilir.

Mesela, GO TO I , (10,25,50) deyiminde :Eğer tamsayı değişken I'ya o anda t atanan değer deyim numarası 50 ise GO TO.... deyiminden sonra 50 nolu deyime sapılır; Eğer I'ya atanan değer deyim numarası 10 ise bir sonraki adımda 10 nolu deyime sapılır.Mesela,

ASSIGN 10 TO KOD

GO TO KOD , (10 , 20 ,30)

.............

10.. A = B

............

20.. A = C

...........

30.. A = D

.............

program biriminde GO TO deyiminden sonra 10 nolu deyime sapılır ve B' nin değeri A' ya taşınır.

## **3.2.5.2 Hesaplanmış ( Computed ) GO TO Deyimi :**

Hesaplanmış GO TO deyimi , m nin o andaki değeri 1,2,3,.... değerlerine bağlı olarak kontrolü d1 , d2 , d3 ,.... numaralı deyimlerden birine aktarır.

Genel formatı: GO TO ( d1 , \[ , d2\] \[ ,d3 \]...) \[ , \] m

Burada d , hesaplanmış GO TO deyiminin içinde bulunduğu programdaki ifa edilebilen bir deyimin numarasıdır. Ayni deyim numarası parantez içinde birden fazla kullanılabilir. m , tamsayı bir ifadedir. m den önceki virgül seçimliktir.Eğer m nin değeri , n parantez içindeki deyim numaralarının sayısı olmak üzere , 1 < m < n aralığının dışına ise hesaplanmış GO TO deyiminden sonraki deyim ifa edilir.

Örnek :

5 .GO TO ( 1,2,3,2 ) , IX

1. A = A + 1.0

...GO TO 3

2 .A = A + 2.0

3 .CONTINUE

## **3.2.5.3 Koşulsuz GO TO Deyimi :**

Koşulsuz GO TO deyimi kontrolü deyim numarası belirlenen deyime aktarır. Bu GO TO deyiminin her ifa edilişinde kontrol ayni deyime aktarılır.

Genel formatı: GO TO d

Burada d , koşulsuz GO TO deyiminin içinde bulunduğu programdaki ifa edilebilen bir deyimin numarasıdır.Bu deyimden sonra gelen ifa edilebilir herhangi bir deyimin , bir deyim numarası olması gerekir, aksi halde bu deyim isleme konmaz veya ifa edilemez.

Örnek :

........

....GO TO 1

2. B = A \* 200.0

..........

1. A = B + 10.0

...........

## **3.2.6. \* IF Deyimleri**

IF deyimleri verilen koşula bağlı olarak ortaya çıkan farklı durumlarda yapılacak işlemi belirler.Üç tür IF deyimi vardır :

-Aritmetik IF

-Blok IF ; END IF , ELSE , ELSE IF

-Lojik IF

## **3.2.6.1 Aritmetik IF Deyimi :**

Aritmetik IF deyimi , aritmetik ifade ( m ) nin değeri sıfırdan küçük, sıfıra eşit veya sıfırdan büyük olduğu zaman kontrolü d1 , d2 veya d3 numaralı deyimlere aktarır. Ayni IF deyiminde bir deyim numarası birden çok kullanılabilir.

Genel formatı: IF ( m ) d1, d2 , d3

Burada m, kompleks tipte olmayan herhangi bir aritmetik ifadedir. d1 , d2 ve d3 ; IF deyiminin de içinde bulunduğu programdaki ifa edilebilen bir deyimin numarasıdır.Bu deyimden sonra gelen ifa edilebilir herhangi bir deyimin bir deyim numarası olması gerekir; aksi halde bu deyim asla isleme konmaz veya ifa edilemez.

## **3.2.6.2 : ****Blok IF Deyimi:******

Blok IF deyimi END IF deyimi ile birlikte kullanılır ve gerektiğinde ELSE IF ve ELSE deyimleri ile de kullanılabilir.

Genel formatı: IF ( m ) THEN

Burada m, herhangi bir lojik ifadedir. Blok IF deyimi ile ilgili olan iki terim vardır .Bunlar IF-level ve IF-block terimleridir.

## **3.2.6.3. IF-Level :**** **

Bir programdaki IF-level'lerin sayısı blok IF deyimi ile END IF'den oluşan deyimlerin sayısı ile hesaplanır.

## **3.2.6.4. IF-Block :**** **

Bir IF-block, blok IF deyiminden sonraki ilk deyim ile baslar son ELSE IF, ELSE veya END IF deyiminden önceki deyimde biter.Eğer IF-block'un içinde ifa edilebilen bir deyim yok ise IF block bostur denir.

Kontrol bir IF bloğunun içinden başka bir IF bloğunun içine aktarılamaz.Bir blok IF deyiminin ifasında önce m ifadesi değerlendirilir. Eğer m nin değeri doğru(true) ise IF-block'undaki ilk deyimden başlayarak sırasıyla deyimler ifa edilir.Eğer m nin doğru ve IF-block bos ise kontrol bir sonraki END IF deyimine(ayni IF-level'inda olan) aktarılır.Eğer m nin değeri yanlış(false) ise kontrol ayni IF-level'inde olan bir sonraki ELSE IF, ELSE veya END IF deyimlerine aktarılır.Bir blok IF deyimi DO döngüsü ile kesilemez, yani iç içe giremez.

## **3.2.6.5. END IF Deyimi :**

END IF deyimi bir IF-block'unu bitirir .İfa sırasını değiştirmez.

Genel formatı: END IF

Her bir blok IF deyimi için ayni programda bir END IF deyimi bulunmalıdır. Bu END IF deyimi blok IF deyiminin son deyimidir ve ifa sırasına etki etmez.END IF deyimi DO döngüsü içinde olmamalıdır.

Örnek :

IF ( A . GT . B ) THEN

...........

END IF

## **3.2.6.6 ELSE Deyimi :**

Eğer bir önceki blok IF veya ELSE IF koşulu yanlış olarak değerlendirildi ise ELSE deyimi ifa edilir.Normal ifa sırasını değiştirmez.

Genel formatı: ELSE

Bir ELSE-block ayni IF-level'indeki son END IF deyimi ile ELSE deyimi arsındaki ifa edilebilir deyimlerden oluşur.Burada ELSE deyimi ile END IF deyimi ELSE-block'a dahil değildir.Bir ELSE-block bos olabilir.Bir IF-block'unda yalnız bir ELSE olabilir. Bir ELSE block'unun içinden bir başka ELSE block'unun içine geçilemez.ELSE deyimi DO döngüsü içinde kullanılamaz.

Örnek:

IF ( A . EQ . B ) THEN

...........

ELSE

...........

END IF

ELSE IF deyimi :

Eğer bir önceki blok IF koşulu yanlış olarak değerlendiriliyor ise ELSE IF deyimi ifa edilir.

Genel formatı: ELSE IF ( m ) THEN

Burada m, herhangi bir lojik ifadedir. Bir ELSE IF-block ayni IF-level'indeki son ELSE IF , ELSE veya END IF deyimi ile ELSE IF deyimi arasındaki ifa edilebilir deyimlerden oluşur. Burada ELSE IF deyimi değimi block'a dahil degildir.ELSE IF-block'u bos olabilir. Eğer lojik ifade m nin değeri doğru ise ELSE IF-block'unun ilk deyimi ile normal ifa işlemleri gerçekleştirilir. Eğer lojik ifade m doğru ve ELSE IF-block bos ise kontrol ayni IF-level'indeki son END IF deyimine aktarılır. Eğer lojik ifade m yanlış ise kontrol ayni IF-level'indeki son ELSE IF, ELSE veya END IF deyimine aktarılır.

Kontrol bir ELSE IF-block'unden başka ELSE IF-block'una aktarılamaz. ELSE IF deyiminin deyim numarası ile bir başka deyime geçilemez. Bir END IF deyimi DO döngüsü içinde kullanılamaz.

Örnek 1 :

IF ( I . LT . J ) THEN

........

ELSE IF ( I . GT . J ) THEN

..........

END IF

Örnek 2 :

IF ( I . LT . J ) THEN

..........

ELSE IF ( I . GT . J ) THEN

...........

ELSE

END IF

Örnek 3 : Aşağıdaki program sayısal notları alfabetik notlara dönüştürmek için hazırlanmış basit bir uygulamadır. Blok IF deyimi kullanılarak hazırlanan bu program başka şekillerde de yazılabilir.

.....CHARACTER\*1 N1/'A' / , N2/'B' /, N3/ 'C'/ ,N4/ 'D'/

1.. READ ( 5,5,END = 90 ) NO, NOT

5.. FORMAT ( I5,35X,I3 )

.....IF ( NOT.LE.25 ) THEN

.....WRITE ( 6,30 )NO , N4

.....ELSE IF ( NOT . LE .50 ) THEN

.....WRITE ( 6,30 )NO , N3

......ELSE IF ( NOT.LE.75 ) THEN

......WRITE ( 6,30 )NO , N2

......ELSE

......WRITE ( 6,30 )NO , N1

.....END IF

30 .FORMAT ( 5X,I5, 'NOT = ' , A1)

......GO TO 1

90 . STOP

...... END

## **3.2.6.7 Lojik IF Deyimi :**

Lojik IF deyimi bir lojik ifadeyi değerlendirir ve ifadenin değerinin doğru veya yanlış olmasına göre ya bir deyimi ifa eder veya lojik IF deyiminin altındaki ifadeyi gerçekleştirir.

Genel formatı: IF ( m ) d

Burada m , herhangi bir lojik ifadedir. d , ifa edilebilir herhangi bir deyimdir. Bu deyim DO deyimi , başka bir lojik IF deyimi, END deyimi , blok IF , ELSE IF , ELSE veya END IF deyimi ve ayrıca TRACE ON, TRACE OFF, INCLUDE veya DISPLAY deyimi olamaz. d bir deyim numarası olamaz , ama içinde deyim numarası bulundurulabilir( GO TO 50 gibi ).

Örnek :

IF ( A . LE .0 .) GO TO 50

............X = Y + Z

............IF ( A . EQ . B ) X = 2.0\*Y/Z

...50.....T = U\*\*2

...........................

## **3.2.7. \*PAUSE Deyimi**

PAUSE deyimi amaç programın ifasını geçici olarak keser ve bir mesajın görünmesini sağlar.

Genel formatı: PAUSE \[ n \] ,

........................PAUSE \[ 'mesaj ' \]

Burada n , 1-5 basamaklı bir sayı , 'mesaj' , tırnaklarla kapanan bir karakter sabitedir.Bu sabite alfa nümerik veya özel karakterlerden oluşur. Bu literal sabite içinde tırnak kullanılacaksa bu çift tırnakla belirtilmelidir.

Eğer n veya ' mesaj ' kullanılıyorsa kesilme anında operatöre gerekli talimat verilir.Bu duraklama esnasında operatör gerekli işlemleri yaparak kontrolü programa geçirir ve PAUSE deyiminden sonra gelen deyim veya DO döngüsünün son iterasyonu ifa edilir.

## **3.2.8. \*RETURN Deyimi **

RETURN deyimi kontrolü çağıran programa aktarır. Eğer RETURN deyimi ana programda kullanılıyorsa STOP deyiminin yaptığı isi yapar. Bu deyim ya bir function veya subroutine alt programında kullanılmalıdır.

Function alt programındaki RETURN deyimi :

Function alt programları RETURN deyimini bulundurmalıdır.Bu RETURN deyimi lojik olarak hesaplama sonucunu belirler ve hesaplanan fonksiyon değerinin çağrılan programa geri dönmesini sağlar.

Genel formatı: RETURN

RETURN deyiminin ifası ile altprogramdaki yapma argümanlar ile gerçek argümanlar arasındaki ilişki kesilir.Altprograma giren argümanların tümü , aşağıdakiler hariç tanımsız olur.

-SAVE deyiminde belirlenen argümanlar,

-DATA ve açık tip bildirme deyiminde kullanılan argümanlar,

-Etiketsiz COMMON deyimindeki argümanlar .

Subroutine alt programındaki RETURN deyimi :

Subroutine alt programları da RETURN deyimi bulundurmalıdır. Bu RETURN deyimi lojik olarak hesaplama sonucunu belirler ve kontrolü çağıran programa aktarır.

Genel formatı: RETURN ( m )

Burada m , bir tamsayı ifadedir. RETURN deyiminde m kullanılmazsa veya m nin değeri birden küçük ise veya SUBROUTINE deyiminde belirlenen ( \* ) asterikslerin sayısından fazla ise kontrol CALL deyiminden sonraki deyime aktarılır. Böylece CALL deyiminin ifası tamamlanır.Eğer , n SUBROUTINE deyimindeki asterikslerin sayısı olmak üzere 1<=m<=n ise m nin değeri yapma argüman listesindeki m inci asteriksi belirler. CALL deyimindeki geri dönüş belirleyicileri ile SUBROUTINE deyimindeki asteriksler arasında birebir bir ilişki olmalıdır. Bu ilişkiye göre herhangi bir asterikse karşılık gelen bir geri dönüş belirleyicisi bulunur ve RETURN deyiminin ifası ile bu deyime sapılır.RETURN deyimi ifa edildiğinde altprogramdaki yapma argümanlar ile gerçek argümanlar arasındaki ilişki kesilir.Altprograma giren argümanların tümü, yukarıda belirlenen üç gruptaki argümanlar hariç olmak üzere tanımsız olur.

RETURN m ile birlikte kullanılan bir CALL deyiminin daha iyi anlaşılması için hesaplanmış, GO TO deyimlerinden oluşan deyim grubunun incelenmesi gerekir.Mesela aşağıdaki CALL deyimi :

CALL SUB ( X , \* 10 , Y , \* 20 , Z , \* 30 ) aşağıdaki deyimlere denktir:

CALL SUB ( X , Y , Z , I )

GO TO ( 10 , 20 , 30 ) , I

Buradaki I çağrılan altprogramda 1, 2 veya 3 değerlerini alan bir değişkendir.Yukarıdaki CALL deyiminde de m nin 1 olması halinde 10 nolu deyime , 2 olması halinde 20 nolu deyime , 3 olması halinde 30 nolu deyime sapılır.

## **3.2.9. \*STOP Deyimi**

STOP deyimi amaç programın ifasını durdurur ve istenirse amaç programın ifası sonunda bir mesajın yazılmasını sağlar.

Genel formatı: STOP \[ n \]

........................STOP \[' mesaj '\]

Burada n, 1-5 basamaklı bir sayıdır. mesaj, iki tırnak arasına yazılan ve alfa nümerik veya özel karakterlerden oluşan bir karakter sabitedir. Literal olması halinde bu literal içindeki bir tırnak peş peşe gelen iki tırnakla belirtilir.Eğer STOP'tan sonra n veya ' mesaj ' kullanılırsa , STOP ile birlikte gerekli bilgi operatöre iletilir.

## **4. DIZILER VE DIZI ELEMANLARI**

Küme aralarında ortak bir ilişki bulunan nesneler topluluğudur.(Örneğin bir sınıftaki öğrenciler ,bir ülkenin kentleri veya bir polinomun katsayıları gibi)Eleman kümeyi oluşturan nesnelere denir.Dizi elemanlar küme içinde belli bir sıra içinde ise kümenin aldığı addır. Küme ve dizi arasındaki fark aşağıda gösterilmiştir;İndis elemanın dizi içindeki yerini belirleyen bilgiye denir.(Örneğin yukarıdaki dizide üçüncü elemanın adi Can'dır demek indise bir örnektir.).Diziler tek boyutta tanımlanabileceği gibi iki boyutta da tanımlanırlar.Aşağıdaki örneği inceleyiniz;

dizi kullanmak ilk etapta getirdiği ifade kolaylıkları ile göze çarpmaktadır.Örnek olarak aşağıda polinomun değişik şekillerdeki yazılımlarını ve en sonda da dizi olarak bir tanımı verilmiştir.anlayacağınız üzere dizi kullanmak hem sadeleşme hem de güncelleme sağlamıstır.güncelleme diyoruz çünkü ifadede tek bir rakamı değiştirmek ,ki bu sayı 5'tir,ifadenin uzunluğu değiştirmeden ifade avantajı sağlıyor.konumuz ile alakalı olarak verilebilecek önemli bir örnek tipi ise sıralama algoritmasıdır.

Tanım: Üzerinde toplama,çarpma ,çarpma ve bölme işlemlerinin özel olarak tanımlandığı bir ve iki boyutlu dizilere cebirde vektör ve matris adi verilir.Bu tanıma ilişkin,matris ve vektör kullanımına bir örnek alalım;normalde seklinde yazılan bir üç bilinmeyenli bir denklem takımı,

katsayılar matrisi A ;

bilinmeyenler vektorü x ;

ve sabitler dizisi b ; kullanarak

A . x = b

seklinde yazılabilir.Burada seklinde tanımlanmış diziler olup , çarpım işlemi özel kurallara göre yapılır.Bu şekilde yapıldığı zaman denklem takımlarının algoritmik yolla ,başka bir değişle programlama ve çözümü daha kolay ifade edilebilir.Dizi kullanımının programcıya (algoritma tasarımcısına) getirdiği anlatım kolaylıkları,tüm programlama dillerinde diziler ve diziler üzerinde işlemleri kolaylaştıran deyimlere yer verilmesine yol açmıştır. Küme aralarında ortak bir ilişki bulunan nesneler topluluğudur.(Örneğin bir sınıftaki öğrenciler ,bir ülkenin kentleri veya bir polinomun katsayıları gibi).Eleman kümeyi oluşturan nesnelere denir.Dizi elemanlar küme içinde belli bir sıra içinde ise kümenin aldığı addır. Küme ve dizi arasındaki fark aşağıda gösterilmiştir;

İndis elemanın dizi içindeki yerini belirleyen bilgiye denir.(Örneğin yukarıdaki dizide üçüncü elemanın adi Çan’dır demek indise bir örnektir.).Diziler tek boyutta tanımlanabileceği gibi iki boyutta da tanımlanırlar.Aşağıdaki örneği inceleyiniz;dizi kullanmak ilk etapta getirdiği ifade kolaylıkları ile göze çarpmaktadır.Örnek olarak aşağıdaki polinomun değişik şekillerdeki yazılımlarını ve en sonda da dizi olarak bir tanımı verilmiştir.anlayacağınız üzere dizi kullanmak hem sadeleşme hem de güncelleme sağlamıştır.Güncelleme diyoruz çünkü ifadede tek bir rakamı değiştirmek ,ki bu sayı 5'tir,ifadenin uzunluğu değiştirmeden ifade avantajı sağlıyor.

konumuz ile alakalı olarak verilebilecek önemli bir örnek tipi ise sıralama algoritmasıdır.

Tanım: Üzerinde toplama,çıkarma ,çarpma ve bölme işlemle işlemlerinin özel olarak tanımlandığı bir ve iki boyutlu dizilere cebirde vektör ve matris adi verilir.Bu tanıma ilişkin,matris ve vektör kullanımına bir örnek alalım;normalde seklinde yazılan bir üç bilinmeyenli bir denklem takımı,

katsayılar matrisi A ;

bilinmeyenler vektörü x ;

ve sabitler dizisi b ; kullanarak

A . x = b

seklinde yazılabilir.Burada seklinde tanımlanmış diziler olup , çarpım işlemi özel kurallara göre yapılır.Bu şekilde yapıldığı zaman denklem takımlarının algoritmik yolla ,başka bir değişle programlama ve çözümü daha kolay ifade edilebilir.

Dizi kullanımının programcıya (algoritma tasarımcısına) getirdiği anlatım kolaylıkları,tüm programlama dillerinde diziler ve diziler üzerinde işlemleri kolaylaştıran deyimlere yer verilmesine yol açmıştır. Al gol programlama dilinde "while ...do", Basic prog. dilinde "for ...next", FORTRAN prog. dilinde "Do" çevirimleri bu amaca yöneliktir.

## **5.YAN BELLEK(KÜTÜK) KULLANIMI **

## **5.1. Kütük Açma**

Fortran 77'de kütük yaratma ya da yaratılan kütüğü açma işlemi OPEN deyimi kullanılarak yapılır. Deyimin genel yazılışı:

OPEN (UNIT =nuf, FILE ='fna', STATUS ='st', ACCESS ='ac', FORM ='ft, RECL =rl)

biçimindedir. Burada:

nuf : Yaratılacak ya da açılacak kütüğün numarasıdır. Bulunması zorunludur.

fna : Yaratılacak ya da açılan kütük adıdır. Değişken kurallarına uyar.

st : Herhangi bir kütük daha önce yaratılmış ya da ilk defa yaratılacak olabilir. Eğer OPEN deyiminde st yerine NEW yazılırsa kütüğün yaratılmakta olduğu, OLD yazılırsa daha önce yaratılan bir kütüğün açılmakta olduğu anlaşılır.

ac : Kütüğe erişim sıralı ya da doğrudan olabilir. Belirtilmezse sıralı erişim vardır.

ft : Kütük ile ilgili yapılacak okuma ya da yazma işlemlerinde format kullanılıp kullanılmayacağı belirtilir. Belirtilmezse sıralı erişim durumunda formatsız, dolaylı erişim durumunda formatlı olarak yapılır.

rl : Kayıtların uzunluklarını tanımlamakta kullanılır. En uzun kayıt uzunluğu alınır.

OPEN(13, STATUS='NEW', ACCESS='SEQUENTIAL', FORM='FORMATTED', RECL=15)

## **5.2. Kütük Kapama **

Açılan kütüklerin kapanması işlemi CLOSE deyimi kullanılarak gerçekleştirilir. Genel yazılışı:

CLOSE (UNIT =nuf, STATUS ='st')

biçimindedir. Burada:

st : Kütük kapatma türünü gösterir. Delete ve Keep durumları söz konusudur. Delete silmek, Keep saklamak için yazılır.

CLOSE(13, STATUS='KEEP')

## **5.3. Kütükten Okuma **

Kütükten okuma yapılması işlemi READ deyimi ile olur. Genel yazılışı:

READ (UNIT =nuf, fs, END =sst, ERR =hst, REC =m)dl

biçimindedir. Burada:

nuf : Okuma yapılacak kütüğün numarasını

fs : Okuma için kullanılan formatın deyim numarasını

sst : Okuma işlemi bittiğinde ya da kütük sonunda devam edilecek kütük numarasını

hst : Okuma sırasında ortaya çıkabilecek hatalar durumunda devam edilecek deyim numarasını

m : Kütükte okutma yapılan kaydın numarasını

dl : Birbirinden virgülle ayrılmış değerleri okutulacak değişkenleri gösterir.

READ(1,10,END = 20)GR,LR,NRM

## **5.4. Kütüğe Yazma **

Herhangi bir kütüğe veri girilmek ya da yazılmak istendiğinde WRITE değimi kullanılır. Genel yazılışı:

WRITE (UNIT = nuf, fs, ERR = sst, REC = m)dl

biçimindedir. Burada:

sst : Yazma hataları durumunda devam edilecek deyim numarasını gösterir

WRITE(1,10, ERR = 100, REC=5)D,E,F

## **5.5. ENDFILE Deyimi **

Okuma işlemi sırasında sıralı bir kütükte kütük sonuna gidilmesini sağlar. Genel yazılışı:

ENDFILE (nuf)

biçimindedir. Burada nuf kütük numarasını gösterir.

ENDFILE(2)

## **5.6. REWIND Deyimi **

Kütüğün herhangi bir yerinden ilk tutanağa dönülmesini sağlar. Genel yazılışı:

REWIND(nuf)

biçimindedir. Burada nuf kütük numarasını gösterir.

READ(2)

## **5.7. BACKSPACE Deyimi **

Kütükte, bulunan tutanaktan bir önceki tutanağa geçilmesini sağlar. Genel yazılışı:

BACKSPACE(nuf)

biçimindedir. Burada nuf kütük numarasını gösterir.

BACKSPACE(2)

## **5.8. Bazı Örnek Programlar**

1)Aşağıdaki program sıralı bir kütük yaratır, bu kütüğe bilgileri yazar, kütüğü kilitler ve kapatır. Daha sonra kütüğü açar ve kütükteki bilgileri okuyup ekrana yazar.

Dimension A(9,9)

Open (Unit=5, File='Ver',Status='New')

Read (\*,\*)A

Write (5,\*)A

Close (5,Status='Keep')

Open (5,File='Ver',Status='Old')

Read (5,\*,End=77)A

Write (\*,\*)A

Goto 130

Close (5)

Stop

End

2)Öğrenci notlarını bulunduğu sıralı kütükten okuyan ve ortalamaları yazan bir program ise:

Dimension Onot (1500)

Open (5, File='Onot')

Do 50 I-1, 1500

Read (5,\*,End=100) Onot (I)

Tnot=Tnot+Onot(I)

K=K+1

50 Continue

100 Ornot=Tnot/K

Write (\*,\*)Ornot

Stop

End

## **6. ÖRNEK PROGRAMLAR**

! Write the values of "pi" and "e."

program A01 ! (specification statement)

program A01 ! (specification statement)

implicit none ! (specification statement)

implicit none ! (specification statement)

! start program A01

! start program A01

write (unit = \*, fmt = \*) atan2( 0.0, -1.0 ), exp( 1.0 ) ! (instruction)

write (unit = \*, fmt = \*) atan2( 0.0, -1.0 ), exp( 1.0 ) ! (instruction)

stop ! (instruction)

stop ! (instruction)

end program A01 ! (specification statement)

end program A01 ! (specification statement)

! Write the values of "pi" and "e."

! Write the values of "pi" and "e."

program A01 ! (specification statement)

program A01 ! (specification statement)

implicit none ! (specification statement)

implicit none ! (specification statement)

! start program A01

! start program A01

write (unit = \*, fmt = \*) atan2( 0.0, -1.0 ), exp( 1.0 ) ! (instruction)

write (unit = \*, fmt = \*) atan2( 0.0, -1.0 ), exp( 1.0 ) ! (instruction)

stop ! (instruction)

stop ! (instruction)

end program A01 ! (specification statement)

end program A01 ! (specification statement)

proram ex511

use triangle

real::a,b,c

logical::triangle,isosceles,equilateral

call find (a,b,c,triangle,isosceles,equilateral)

print\*,"This program decides the type of a triangle"

print\*,"Given with the side lenghts :"

print\*,""

do

print\*,"Enter the side lenghts!"

print\*,""

read::a,b,c

if (isosceles) then

print\*,"The triangle is an isosceles"

else

if (equilateral) then

print\*,"The triangle is equilateral"

else

print\*,"The triangle is a scalane"

endif

endif

end do

end program ex511

aca yoneliktir. . Çıkışta liste belirtilmez .

PAGE

PAGE 1

---
*Kaynak: `PROGRAMLAMA DİLLERİ/PROGRAMLAMA DİLLERİ.doc` — x — 2004*
