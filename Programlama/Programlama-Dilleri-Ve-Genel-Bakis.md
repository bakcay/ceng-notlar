# Programlama Dilleri Ve Genel Bakiş

1. AKIŞ ŞEMASI İŞARETLERİ

*1.1. GİRİŞ*

Bir problemin çözümünde izlenecek olan adımlara “algoritma” adı verilir. Algoritma, verilen herhangi bir problemin çözümüne ulaşmak için uygulanması gerekli adımların hiçbir yoruma yer verilmeksizin açık, düzenli ve sıralı bir şekilde söz ve yazı ile ifade edilmesidir. Akış Şemaları ise algoritmaların özel (geometrik) şekillerle gösterilmesidir. Yazılımı oluşturacak program parçalarını ve bu parçaların birbirleri ile olan ilişkilerini belirler.

Bilgisayar aracılığı ile bir problemin çözümünde yapılacak olan ilk ve temel iş, problemin çözüm algoritmasını hazırlamaktır. Algoritmayı oluşturan adımlar özellikle basit ve açık olarak sıralanmalıdır. Algoritma hazırlandıktan sonra, istenilen programlama dilinin komutları ile program yazılır. Bir problemin algoritması hazırlandıktan sonra bu problem bütün programlama dillerinde yazılabilir.

Program yazılırken aşağıdaki adımlar izlenmelidir.

Adım 1 : Programın algoritması hazırlanır ya da akış şeması çizilir.

Adım 2 : Hazırlanan algoritma ya da akış şeması istenilen programlama dili ile kodlanır.

Adım 3 : Program bilgisayarda çalıştırılır.

Adım 4 : Derleyici ya da yorumlayıcı yazım hatası veriyor ise bu hatalar düzeltilir.

Adım 5 : Program çalıştırıldığında çıkan sonuçlar istenilen gibi değilse Adım 1’e dönülüp algoritma kontrol edilir.

*1.2. BAŞLA VE DUR KUTULARI*

“Başla” ve “Dur” işlemleri, tüm akış şemalarında bulunan standart işlemlerdir. Akış şemaları “Başla” şekli ile başlar ve “Dur” şekli ile biter. Akış şemasında yer alan bütün işlemler, bu iki şekil arasında yer alırlar.

*1.3. OKLAR*

Akış şemalarında işlem akışının hangi yönde olduğu ok işaretleri ile gösterilir. Oklar, akış şemalarında şekiller arasında yer alıp bu şekilleri birbirine bağlarlar. İşlem akış yönüne uygun olan ok kullanılır. Oklar, bir şeklin ifade ettiği işlem tamamlandıktan sonra program akışının diğer şekilden devam edeceğini gösterirler.

*1.4. İŞLEM KUTUSU*

Programın işlenmesi sırasında yapılacak işlemleri göstermek için kullanılır. İçine formüller aynen yazılır. İşlem akışı, işlem kutusuna geldiğinde, kutunun içinde yazılı olan işlem gerçekleştirilir. Birden fazla işlem aynı kutunun içine aralarına virgül konularak ya da alt alta yazılarak gösterilebilir.

Değişkenler, herhangi bir değeri saklamak için kullanılırlar. Bir değişken aynı anda yalnızca bir değer saklayabilir. Değişkene yeni bir değer atandığında eski değer kaybolacaktır.

Atama işlemi ile eşitliğin sağ tarafındaki işlemin (işlem ne kadar basit ya da karmaşık olursa olsun) sonucu eşitliğin sol tarafındaki değişkene atanır. Eşitliğin sağ tarafında bir sabit, değişken ya da matematiksel bir işlem olabilir. Sol tarafında ise mutlaka bu değerlerin atanabileceği bir değişken olmalıdır.

*1.5. GİRİŞ KUTUSU*

Çevre aygıtlardan (klavye, disk vb.) değişkenler içerisine veri girmek amacı ile kullanılır. Giriş kutusu için aşağıdaki iki şekilden istenilen biri kullanılabilir.

Giriş kutuları içine birden fazla değişken yazılabilir. Bu durumda değişkenleri birbirinden ayırmak için virgül işareti kullanılır.

*1.6. ÇIKIŞ KUTUSU*

String ve sayısal sabit ya da değişkenlerin değerlerinin çevre aygıtlara (ekran, yazıcı disk vb.) yazdırmak amacı ile kullanılır. Yazdırılacak değişkenlerin adları olduğu gibi kullanılır. Herhangi bir sabit ifadeyi yazdırabilmek için ifade tırnak (‘) içine alınmalıdır. Birden fazla değişken ya da sabit ifade aynı çıkış kutusunda yazdırılabilir. Bu durumda söz konusu değişken ya da sabit ifadeler arasında virgül işareti konulur.

Şekil 7 :** Çıkış Kutusu**

*1.7. KARŞILAŞTIRMA KUTUSU*

Karşılaştırma kutuları, kontrol ifadeleri ile programın akışını kontrol ederler. Verilen koşulun doğru ya da yanlış olması durumlarına göre istenilen işlemleri gerçekleştirmek ve buna göre program akışını değiştirmek için kullanılır.

Şekil 8 : **Karşılaştırma Kutusu**

Karşılaştırma kutusu içinde bir koşul bulunur. Bu koşulun mantıksal olarak Doğru (True) ya da Yanlış (False) olması durumuna göre program akışı oklarla gösterilen yönde devam eder. Şekil.9’de görülen ‘a=b’ koşulu Doğru ise ‘komutlar1’, Yanlış ise ‘komutlar2’ komut grupları işlem görecek ve programın çalışması oklar yönünde devam edecektir. Karşılaştırma kutusu içindeki koşulun Doğru ya da Yanlış olması durumunda gerçekleştirilecek herhangi bir işlem yok ise söz konusu olan taraf boş bırakılabilir.

Tablo 1 : **Karşılaştırma Operatörleri**

| **PASCAL** | **C/C++** | **Anlamı** |
| --- | --- | --- |
| = | == | Eşit |
| < > | < > | Eşit değil |
| < | < | Küçük |
| <= | <= | Küçük eşit |
| > | > | Büyük |
| >= | >= | Büyük eşit |

Karşılaştırma operatörleri iki değeri birbiri ile kıyaslar. Kullanılan operatörün ifade ettiği koşula göre kontrol işlemi yapılır. Bu kontrol işlemi sonucunda Doğru (True) ya da Yanlış (False) diye iki mantıksal değerden biri üretilir. *{Örnekler} *

Tablo 2 : **Mantıksal İşlem Operatörleri**

| **PASCAL** | **C/C++** | **Anlamı** |
| --- | --- | --- |
| Not | ! | Değil |
| And | && | Ve |
| Or | \|\| | Veya |

Mantıksal işlem operatörleri ise herhangi bir karşılaştırma operatörü sonucu üretilen mantıksal değerler üzerinde işlem yaparlar. ‘And’ ve ‘Or’ iki mantıksal değeri bağlarken, ‘not’ bir mantıksal değerin önüne gelir. *{ örnekler}*

Tablo 3: ‘**And’ Mantıksal İşlem Operatörü**

| **P** | **q** | **p ve q** |
| --- | --- | --- |
| False | False | False |
| False | True | True |
| True | False | True |
| True | True | True |

Tablo 4 : ‘**Or’ Mantıksal İşlem Operatörü**

| **p** | **q** | **p ve q** |
| --- | --- | --- |
| False | False | False |
| False | True | False |
| True | False | False |
| True | True | True |

Tablo 5 : ‘**Not’ Mantıksal İşlem Operatörü**

| **p** | **not(p)** |
| --- | --- |
| False | True |
| True | False |

*1.8. DÖNGÜLER*

Döngü yapıları bir komut grubunun birden fazla işlenebilmesi için kullanılırlar. Belirli bir komut bloğunun belli koşullar gerçekleşinceye kadar defalarca çalışması gerekebilir. Böyle durumlarda döngüler kullanılır.

**1.8.1. TEKRARLI DÖNGÜLER**

Tekrar sayısının önceden bilindiği durumlarda tekrarlı döngüler kullanılır. Tekrarlı döngülerde genellikle bir sayaç kullanılır. Bu sayaç belli bir değere ulaşıncaya kadar artım miktarı kadar arttırılır. Bu tür döngü şeklinin içine; döngü değişkeni, döngü değişkeninin başlangıç ve bitiş değeri ve artım miktarı yazılır. Tekrarlı döngüler iki şekilde oluşturulabilir.

Artan Döngü : Başlangıç değeri, bitiş değerinden küçüktür. Artım değeri pozitiftir.

Azalan Döngü : Başlangıç değeri, bitiş değerinden büyüktür. Artım değeri negatiftir.

Şekil 9 : **Tekrarlı Döngüler**

İç içe birden fazla döngü kurulabilir. Döngüler kapatılırken, ilk önce en içteki döngünün kapatılması gerekir.

* {Şekil ... iç içe for .... }*

**1.8.2 . KOŞULLU DÖNGÜLER**

Koşullu döngüler, belirli bir koşul sağlandığı sürece döngü içindeki komutların tekrarlanmasını sağlamak amacı ile kullanılır.

Koşullu döngüler, koşulun döngüde bulunduğu yer göre ikiye ayrılır. Koşul ya döngünün başında ya da sonunda yer alır.

*{Şekil while}*

{Şekil repeat}

3. C PROGRAMLAMA DİLİ

*3.1. TEMEL KAVRAMLAR*

**3.1.1. C Programının Yapısı ve Progam Yazma Kuralları**

C Programlama dili, 1972 yılında Dennis RITCHIE tarafından tasarlanmıştır. C programlama dili, 1970’te Ken THOMPSON tarafından geliştirilen B programlama dili üzerine kurulmuştur. B programlama dilinin geliştirilmesinde, 1967 yılında Martin RICHARDS tarafından geliştirilen BCPL programlama dilinden esinlenilmiştir.

Genel amaçlı bir dil olan C dilinin yayılması ve gelişmesi, C programlam dili ile yazılmış olan UNIX işletim sisteminin tutulması önemli etken olmuştur. Günümüzde C programlama dili, hemen hemen her alanda kendisine yer edinmiştir.

**3.1.2. C Programında Kullanılan Karakterler**

C Programlama dilinde kullanılan karakterler aşağıda listelenmiştir.

A’dan Z’ye ve a’dan Z’ye İngiliz alfabesindeki harfler.

Boşluk (ara çubuğu) karakteri.

0’dan 9’a kadar rakamlar.

\\ karakteri

? işareti

\_ (alt çizgi – underline ) karakteri

( ) \[ \] { } karakterleri

+ - \* / karakterleri

| & ! ~ % karakterleri

< > = karakterleri

. (nokta) , (virgül) ; (noktalı virgül) ‘ (tırnak) “ (çift tırnak) işaretleri

**3.1.3. C Kelimeleri**

C Programlama dilinde kendi işlevleri dışında başka amaçlarla kullanılmayacak kelimeler vardır. Bu kelimeler, değişken, sabit, fonksiyon ismi gibi amaçlarla kullanılamazlar. Bu kelimeler “keyword” olarak adlandırılırlar.

Tablo 8 : **C Kelimeleri**

| asm | auto | break | case |
| --- | --- | --- | --- |
| cdecl | char | class |  |

**3.1.4. Tanıtıcı İsimler**

Tanıtıcı isimler terimi ile kastedilen kavram, “sabit”, “değişken” ya da “fonksiyon” tanımında C programının kullandığı adlardır. Bir C programında kullanılan sözcüklerin yazım kuralları aşağıda listelenmiştir.

Her sözcük bir harfle ya da ‘\_’ karakteri ile başlar.

Sözcüğün kalan bölümü harf, rakama ya da ‘\_’ işaretlerinden oluşabilir.

Boşluk karakteri kullanılamaz.

Sözcüğün uzunluğu istenildiği kadar olabilir ancak ilk 32 karakteri geçerli olacaktır.

Küçük harf, büyük harf ya da her ikisi de kullanılabilir. Ancak her biri farklı bir tanım olarak algılanacaktır. (ad, AD , Ad ve aD tanımlamaları farklıdır.)

Tanımlanmış olan C programlama dili sözcükleri başka bir kullanım için yeniden tanımlanamaz.

**3.1.5. Komutlar ve Komut Blokları **

Bütün C programları, bir dizi komuttan oluşur. Genellikle bir komut, tek bir eylem olarak düşünülebilir. C derleyicisi için bir zorunluluk olmamasına rağmen tek satıra tek komut yazılırsa, komutları birbirinden ayırmak daha kolay olacaktır.

Komutlar, blok adı verilen birimlerde biraraya toplanır. Bir blok herhangi bir komut ya da komut grubundan oluşabilir. Bloğun başlangıcını ve bitişini göstermek için oklu parantez “{“, “}” kullanılır.

*3.2. STANDART VERİ TİPLERİ*

**3.2.1. Tamsayı Veri Tipleri**

C programlama dilinde değişkenlerin tanımlanabileceği çeşitli tamsayı veri tipleri bulunmaktadır. Aşağıdaki tabloda kullanılabilecek tamsayı veri tipleri, her bir veri tipinin veri aralığı ve bellekte kapladığı alanlar gösterilmiştir.

Tablo 9 : **C’ deki Tamsayı Veri Tipleri**

| **Tip** | **Veri Aralığı** | **Kapladığı Alan** |
| --- | --- | --- |
| char | -128 ... +127 | 1 byte |
| unsigned char | 0 ... 255 | 1 byte |
| short | -32768 ... 32767 | 2 byte |
| int | -32768 ... 32767 | 2 byte |
| unsigned int | 0 ... 65532 | 2 byte |
| long int | -2147483648 ... 2147483647 | 4 byte |
| unsigned long | 0 ... 4294967296 | 4 byte |

**3.2.2. Gerçel Sayı Veri Tipleri**

C programlama dilinde tamsayı verilerde olduğu gibi değişkenlerin tanımlanabileceği çeşitli gerçel sayı veri tipleri bulunmaktadır. Aşağıdaki tabloda kullanılabilecek gerçel sayı veri tipleri, her bir veri tipinin veri aralığı ve bellekte kapladığı alanlar gösterilmiştir.

Tablo 10 : **C’ deki Gerçel Sayı Veri Tipleri**

| **Tip** | **Veri Aralığı** | **Kapladığı Alan** |
| --- | --- | --- |
| float | 1.7x10-39 ... 1.7x10+38 | 4 byte |
| double | 1.7x10-308 ... 1.7x10+308 | 8 byte |
| long double | 1.7x10-4933 ... 1.7x10+4933 | 10 byte |

**3.2.3. Char Veri Tipi**

C programlama dilinde char veri tipinde tanımlanmış olan bir değişken bellekte 1 byte (1 byte = 8 bit) büyüklüğünde bir alan kaplamaktadır.

**3.2.4. String Veri Tipi**

C programlama dilinde stringler için özel bir veri tipi yoktur. String değişken bildirimi ve kullanımı diğer dillere göre farklıdır.

String bildirimi iki farklı yöntemle yapılabilir. Bu yöntemlerde biri tipi char olan ve NULL ile sonlandırılmış tek boyutlu karakter dizisi aracılığı ile; diğeri ise tipi yine char olan bir işaretçi (pointer) yolu aracılığı ile.

C programlama dilinde char sabitleri tek tırnak, string sabitler ise çift tırnak arasına alınarak tanımlanır. Char sabit ve değişkenleri operatörlerle karşılaştırma işlemlerinde kullanılabilir. Ancak, stringler üzerinde bu işlemler gerçekleştirilemez. Stringlerin karşılaştırılması ya da stringde karakter arama gibi işlemler fonksiyonlar aracılığıyla gerçekleştirilebilir.

**3.2.5. Diziler**

Veri yapısı, çok miktarda veri saklamak için kullanılan bir değişken grubudur. En basit veri yapısı dizidir. Dizi, aynı ad altında toplanmış ve aynı tipte olan değişkenler listesidir.

Bir bilgisayar belleği doğrudan adreslenebilen bir dizi hücreden oluşur. Bellekteki her hücreye erişebilmek için sayısal bir adres kullanılır. Bilgisayar belleğinin bu düzeni, dizilerin oluşturulmasında ve kullanılmasında programcılara kolaylık sağlar. Diziler, bellek tanımlamalarının kolaylığı nedeniyle programlama dillerinin temel taşları arasındadır. Bir dizinin elemanları fgiziksel ve mantıksal olarak birbirini izler. Örneğin bir dizinin i’inci elemanıın adresi (a) ise, (i+1)’inci elemanının adresi (a+1), (i+2)’inci elemanının adresi de (a+2) şeklinde olur.

C programlama dilinde diziler 0. adresten(indis) başlar. Diziler üzerinde işlemler yapılırken bu olguya dikkat etmek gerekir. Bu tür diziler tek boyutlu diziler olarak adlandırılır. Tek boyutlu diziler matematikte vektörler adı verilir. Tek boyutlu dizilerin yanında çok boyutlu (iki ya da daha çok boyutlu) dizi kullanma olnağı da vardır. En çok kullanılan çok boyutlu diziler matematikte matris adı verilen iki boyutlu dizilerdir. Satır ve sütunlardan oluşan tablolar bilgisayarda iki boyutlu dizilerle(matris) temsil edilir. Çok boyutlu dizi olarak üç ya da daha fazla boyutlu dizilerde kullanılabilir. Ancak karmaşıklığı dolayısıyla üçten fazla boyutlu diziler pek kullanılmaz.

YAPISAL VERİ TİPLERİ

3.4. DEĞİŞKEN VE SABİTLERİN TANIMLANMASI

**3.4.1. Yerel (Local) Tanımlama**

Yerel değişkenler kullanıldıkları fonksiyonların içinde tanımlanır ve yalnızca tanımlandıkları fonksiyon ya da bloğun içinde tanınır ve kullanılabilirler. Tanımlandıkları fonksiyon ya da bloğun dışında tanınmazlar. Yerel değişkenler tanımlandıkları fonksiyon ya da blok yürütüldüğü anda bellekteki veri alanında yer kaplarlar. Fonksiyon ya da bloğun çalışması sona erdiğinde de bu bellek alanları boşaltılır.

**Örnek :**

.....

{

int a;

.....

{

int b; b değişkeninin a değişkeninin

..... kullanım alanı kullanım alanı

}

.....

}

.....

**3.4.2. Genel (Global) Tanımlama**

Genel değişkenler bütün fonksiyonların dışında tanımlanırlar. Bir değişken bütün program boyunca kullanılıyorsa, genel olarak bildirilmelidir.

**Örnek :**

.....

int a;

.....

void main (void)

{

int b;

.....

..... b değişkeninin

..... kullanım alanı

.....

} a değişkeninin kullanım alanı

fonk1()

{

int c;

.... c değişkeninin

.... kullanım alanı

....

}

**3.3.3. Dışsal (Extern) Tanımlama**

Büyük programlar yazılırken program uygunparçalara bölünüp ayrı ayrı yazılır. Yazılan bu parçalar yine ayrı ayrı derlendikten sonra birbirleri ile bağlantıları (link) kurulabilir. Bu işlem, derleme süresini kısaltır. Çünkü, doğru olarak yazılmış bir fonksiyonbir kez derlendikten sonra, programın tamamında kullanılırken tekrar tekrar derlenmez, yalnızca bağlantı kurulur. Yalnızca o anda üzerinde değişiklik yapılan fonksiyonun bulunduğu dosya derlenir.

Bir C programında bir çok genel değişken olabilir. Program uygun parçalara bölünürken, kullanılacak olan genel değişkenler, bütün parçalarda aynı adla tanımlanırsa derleyici hata verir.

Aşağıdaki örnekte programın iki parçadan oluştuğu varsayılmıştır. A parçası x ve k genel (global) değişkenler olarak bildirilmiştir. Aynı değişkenler programın B parçasında da genel değişken olacaktır; eğer B, parçasında bildirimin önüne “extern” yazılmazsa derleme hatası oluşacaktır.

{Rıfat Çölkesen}

**Örnek:**

** A Parçası B Parçası**

** **int x; extern int x;

char k; extern char k;

void main(void) fonk2( )

{ {

int ... :

: x=x\*x;

: :

} }

fonk1( ) fonk3( )

{ {

: :

x=x\*6; k=’A’;

: :

} }

3.5. OPERATÖRLER

{ Rıfat Çölkesen}

3.6. ÖN İŞLEMCİ KOMUTLARI

**3.6.1. include**

Belirlenen kütüphane (dosya) içindeki makro komutları kullanabilmek için bildirim yapar. Örnek olarak standart giriş/çokoş komutları “stdio.h” doayasında bulunmaktadır. Bu komutları kullanabilmek için bu doayanın bildirilmiş olması gerekir.

#include<stdio.h>

Tablo 11 : **C/C++’da Kullanılan Bazı Kütüphaneler******

| Kütüphane | **İçeriği** |
| --- | --- |
| stdio.h | Standart giriş/çıkış fonksiyonları |
| conio.h | DOS destekli giriş/çıkış fonksiyonları |
| math.h | Matematiksel fonksiyonlar |
| stdlib.h | Dönüşüm, sıralama, arama vb. fonksiyonlar |
| graphics.h | Grafik fonksiyonları |
| dos.h | DOS fonksiyonları |
| ctype.h | Karakter dönüşüm ve sınıflandırma fonksiyonları |
| string.h | Alfasayısal ve bazı bellek yönetim fonksiyonları |

**3.6.2. define******

Programın her yerinde geçerli olan bir sembolik isim ve eşdeğeri tanımlanır.

#define pi 22/4

**3.6.3. pragma**

“pragma” direktifi iki şekilde kullanılır. Birinci kullanım olan ,

#pragma inline

direktifi derleyiciye program içinde Assembler dili kodlarının bulunduğunu bildirir. İkinci kullanımda ise,

#pragma warn \_uyariadi

direktifi, programın derlenmesi aşamasında adı verilen uyarıların dikkate alınmamasını sağlar. Uyarı adlarından bazılar ve anlamları aşağıda verilmiştir.

Tablo 12 : **pragma uyarıları**

| **Uyarı Adı****** | **Anlamı****** |
| --- | --- |
| big | çok büyük onaltılık ya da sekizlik sabit sayı |
| dup | adın tekrar tanımlanmasında farklılık |
| ret | hem ‘return’ komutu hem de bir değerin geri dönüşü var |
| str | verilen ad bir yapının parçası değil |
| stu | tanımlanmamış ad yapısı |
| sus | süpheli pointer dönüşümü |
| voi | “void” fonksiyonlar bir değer göndermez |
| zst | sıfır uzunluktaki yapı |
| aus | hiç kullanılmayan bir değer atandı |
| def | tanımlanmadan önce adın kullanımı mümkün değil |
| pff | etkisiz ifade |
| par | ilgili parametre hiçbir zaman kullanılamaz |
| pia | yanlış atama olasılığı |
| rch | ulaşılamayan kod |
| rvi | fonksiyonun bir değer göndermesi gerekir |
| amb | operatörler parantezlerle kullanılmazlar |
| nod | fonksiyon için bildiri yok |
| pro | protipsiz fonksiyon kullanımı |
| stv | yapısal değerin bir değer olarak geçişi |
| use | hiçbir zaman kullanılmayan bildiri |
| apt | uygunsuz pointer atanması |
| cln | çok büyük sabit değer |
| cpt | uygunsuz pointer karşılaştırması |
| rng | karşılaştırmada sabit aralığın dışında |
| sig | dönüşümde önemli basamaklar kaybolabilir |
| ucp | signed ce unsigned, char için karışık pointer |

**3.6.4. undef******

“#define” ile tanımlanan bir isim, orijinal tanımlamaları kaldırmaksızın farklı değerler için tekrar tanımlanamazlar.

Eğer “#define” ile tanımlanan ifade başka bir değer ile tekrar tanımlanmak istenirse, ya program içinden “#define” ile tanımlanan ifade kaldırılıp yerine yenisi yazılı ya da “#undef” direktifi ile önceki tanımlama iptal edildikten sonra “#define” ile yenisi tanımlanır.

**Örnek :******

#define X 1001

..........................

..........................

..........................

#undef X

#define X 1234

**3.6.5. if, elif, else, endif**

Makro düzeyde tanımlanan bu direktiflerin kullanımı aynı “if”, “else if” ve “else” ifadelerinin kullanımı gibidir. Bu macro kontrol ifadeleri donanıma ve işletim sistemine uygun olarak değişik makroların ya da ifadelerin geçerli olmasını sağlar.

Örnek :

#if ifade

tanımlama bloğu

#elif ifade

tanımlama bloğu

.............

.............

.............

#else ifade

tanımlama bloğu

#endif

Burada “#elif” makrosu “else if”e karşılık gelmekte ve “#endif” makrosu ise “#if”in sonunu göstermektedir.

**Örnek :**

#if (sizeof(int)= = 2)

#define MAKINE=“16 Bitlik İşletim Sistemi”

#else

#define MAKINE=“32 Bitlik İşletim Sistemi”

#endif

void main( )

{

printf(MAKINE);

}

**3.6.6. ifdef, ifndef**

** **“#ifdef” makrosu, bir ismin tanımlanmış olup olmadığının, “#ifndef” makrosu ise bir ismin tanımlanmamış olup olmadığının belirlenmesinde kullanılır.

**Örnek :******

#ifndef SIFRE

#define SIFRE “1342-485-32”

#endif

**3.6.7. ifdef, ifndef**

Bu direktif derleyicinin içte sakladığı satır numarası ve dosya adını işlenen satır numarası ve dosya adına çevirir. Derleyici satır numarası ve dosya adını, eğer bir hata varsa bu hatanın hangi dosyada ve kaçıncı satırda olduğunu göstermek için kullanır. Satır numarası, işlenen her satır sonunda bir artırılır. Bu direktifi genellikle derleyici kendisi kullanır.

**3.6.7. ifdef, ifndef**

Bu direktif makro komutların işleyişi sırasında bir uyuşmazlık olduğunda derleme aşamasına geçmesini engelleyerek, işlemi durdurur. Örneğin yazılan program 32 bit’lik bir işletim sistemi için (örneğin UNIX) dizayn edildi ise ve 16 bit’lik işletim sistemlerinde (örneğin MS-DOS) çalıştırılmaması gerekiyorsa, izleyen direktif program başına eklenebilir.

**Örnek :**

#if (sizeof(int)= = 2)

#error Bu program(16 bit’lik) bu işletim sisteminde çalışmaz.

#endif

3.7. GİRİŞ KOMUTLARI

**3.5.1. scanf( )**

scanf () fonksiyonu, klavyeden her türlü bilgi girişi yapabilmek için kullanılan genel amaçlı bir fonksiyondur. Bu fonksiyon karakterleri tek tek okur ve verilen formata göre düzenleyerek belirtilen değişkenlere aktarır. Bu fonksiyon ile herhangi bir değişkene bilgi girişi içini o değişkenin adresi kullanılır. Sayısal değişkenler için değişkenin adından önce “&” adres operatörü kullanılır. Alfasayısal değişkenler için ise adres operatörü kullanılmaz. Çünkü alfasayısal değişkene aktarılan değer bir alfasayısal bilgi değil, o bilginin ilk karakterinin bulunduğu adrestir.

scanf () fonksiyonu karakterleri tek tek okur ve verilen formata göre düzenleyerek belirtilen değişkenlere aktarır.

int scanf(format dizgisi,adres listesi);

Format Dizgisi : Girişin hangi formata göre olacağını gösterir.

Adres Listesi : Verilerin aktarılacağı değişkenlerin adreslerini gösterir.

Format Dizgisinin Genel Şekli

%

Bu formattaki karakterlerin anlamları şöyledir.

\* : Verildiği zaman değer okunur ama değişkene aktarılmaz.

n : Girilecek olan karakterlerin maksimum sayısını belirten pozitif bir tamsayıdır.

F : ‘far’ pointer olduğunu gösterir.

N : ‘near’ pointer olduğunu gösterir.

h : Sadece d,i,u,o,x ile kullanıldığında “short int” anlamını verir.

l : d,i,u,o,x ile kullanıldığında “long int”; e,f,g ile kullanıldığında ise “double” anlamı verir.

L : sadece e,f,g ile kullanıldığında “long double” anlamını verir.

d : 10 tabanında bir tamsayı (int) girilecek.

D : 10 tabanında bir tamsayı (long int) girilecek.

i : 10,8 ve 6 tabanında bir tamsayı (int) girilecek.

I : 10,8 ve 6 tabanında bir tamsayı (long int) girilecek.

u : İşaretsiz bir tamsayı (unsigned int) girilecek.

U : İşaretsiz bir tamsayı (unsigned int) girilecek.

o : 8 tabanında bir tamsayı (int) girilecek.

O : 8 tabanında bir tamsayı (long int) girilecek.

x : 16 tabanında bir tamsayı (int) girilecek.

X : 16 tabanında bir tamsayı (long int) girilecek.

e : Ondalıklı bir sayı (float) girilecek.

E : Ondalıklı bir sayı (float) girilecek.

g : Ondalıklı bir sayı (float) girilecek.

G : Ondalıklı bir sayı (float) girilecek.

f : Ondalıklı bir sayı (float) girilecek.

s : Alfasayısal bir bilgi (char \[ \] , char \* ) girilecek.

c : Bir karakter (char) girilecek.

% : ‘%’ karakteri girilecek.

**3.7.2. gets( ) **

Klavyeden ‘Enter’ tuşuna basılıncaya kadar alfasayısal (string) bir bilgi okunmasını sağlar. Alfasayısal bilgi okunduktan sonra bu bilginin sonuna ‘NULL’ karakteri eklenir.

gets(str1);

Enter tuşuna basılıncaya kadar klavyeden girilecek olan karakterler “str1” adındaki değişkene atanacaktır. Atama işlemi yapılırken klavyeden girilen son karakterin arkasına bir “NULL” karakteri atanır. Böylece string değişken sonlandırılmış olur.

**3.7.3. getch( ) **

Ekranda görüntülenmeden klavyeden tek bir karakterin girilmesini sağlar. Bilgi girişi için karakterden sonra ‘Enter’ tuşuna basmaya gerek yoktur.

Yazılımı : int getch(void);

ch=getch();

Komut satırı ile klavyeden bir karakter okunarak “ch” ile ifade edilen bir karakter değişkenine atanacaktır. Klavyeden girilen karakter ekranda görüntülenmeyecektir.

**3.7.4. getche( ) **

‘getch( )’ fonksiyonu ile aynı işlevi görür. Tek farkı klavyeden girilen karakterin ekranda görüntülenmesidir.

Yazılımı : int getche(void);

**3.7.5. getchar( ) **

Ekranda görüntülenmeden klavyeden tek bir karakterin girilmesini (okunmasını) sağlar. Bilgi girişi için karakterden sonra ‘Enter’ tuşuna basılmalıdır.

ch=getchar();

Komut satırı ile klavyeden bir karakter okunarak “ch” ile ifade edilen bir karakter değişkenine atanacaktır. Klavyeden girilen karakter ekranda görüntülenmeyecektir. Ama getch() fonksiyonundan farklı olarak bu işlemi yapmak için Enter tuşana basılması beklenecektir.

**3.7.6. cgetsr( ) **

Girilecek karakter sayısını kontrol ederek, string bilgi girişi yapmak için kullanılır.

char \*cgets(char \*str);

String değişkene bilgi okumadan önce ilgili değişkenin 0. byte’ına okunacak uzunluk değerinin girilmesi gerekir. Bu değer klavyeden okunacak karakter sayısını ayarlayacaktır. Daha fazla karakter girişine izin verilmeyecektir. Girilecek karakter sayısı bu değerin 1 eksiğidir. Bunun nedeni bir karakterin satır sonu (\\n) karakteri için ayrılmış olmasıdır.

**Örnek: **

#include <stdio.h>

#include <conio.h>

void main (void)

{

char isim\[30\];

char \*p;

isim\[0\]=10;

printf(“Ad Soyad Giriniz..:”);

p=cgets(isim);

printf(“\\n”);

printf(“Girilen Ad Soyad : %s\\n“, isim);

printf(“Fonksiyon Değeri : %d\\n”,p);

printf(“Karakter Sayısı : %d\\n”,isim\[0\]);

}

3.8. ÇIKIŞ KOMUTLARI

**3.8.1. printf() **

“printf()” fonksiyonu karakterlerin ve verilerin belli bir forma getirilerek ekranda görüntülenmesi için kullanılan bir fonksiyondur. “printf()” fonksiyonu çeşitli bilgilerin standart çıkış aygıtı üzerine yazdırılması amacıyla kullanılır. Standart çıkış aygıtı ekran olup, “stdout” değişkeni ile temsil edilmektedir. Yazdırılacak olan bilgilerin istenilen yazım formatına sahip olacak şekilde düzenlenmesi “printf()” fonksiyonunun ek bir işlevidir.

“printf()” fonksiyonunun ilk parametresi bir string bilgi olup sabit bilgileri, özel karakter notasyonları ve format dizgilerini içerir. Bu parametreyi izleyen, birbirlerinden virgül karakteri ile ayrılmış bir ya da daha fazla argüman seçimlik olarak kullanılabilir. Genel olarak; seçimlik olan bu argümanlar ekrana yazdırılacak bilgilere karşılık gelirler. Bu bilgilerin ekran üzerindeki yazılış şekilleri, format stringinin elemanları ile belirlenir. Ekrana yazdırılacak olan bilgiler, sabit, herhangi bir ifade ya da değişken olabilir.

Yazılımı : int printf(format dizgisi, değişken listesi);

printf() fonksiyonunun sonucu int tipinde bir bilgidir ve gönderilen karakter sayısını verir. Herhangi bir hata oluşması durumunda negatif bir değer gönderir.

Çift tırnak karakteri (“) ile başlayıp yine çift tırnak karakteri (“) ile sonlandırılan “format dizgisi” kısmı genel olarak üç kısımdan oluşur.

Açıklama Kısmı

Format Kısmı

Escape Düzeni Kısmı

**A. Açıklama Kısmı **

İki çift tırnak içinde yazdırılan bilgi doğrudan ekrana yazdırılır.

**Örnek Ekran Görüntüsü **

#include <stdio.h>

void main(void)

{

printf(“Yıldız Teknik Üniversitesi\\n”);

printf(“Meslek Yüksekokulu\\n”);

}

**B. Format Kısmı **

% karakteri arkasına getirilen bir ya da daha fazla karakterden oluşan ve çıkış biçimini belirlendiği kısımdır. Genel şekli aşağıdaki gibidir.

%

Flag Karakterleri

- : Değer sola dayalı olarak yazılır. Sağ taraf boşluklarla doldurulur.

+ : Değerin önüne, işareti (‘+’ ya da ‘–‘) konulur.

‘ ’ (Boşluk Karakteri) : Pozitif değerlerde ‘+’ işareti yerine boşluk karakteri konulur.

- : Değer sola dayalı olarak yazılır. Sağ taraf boşluklarla doldurulur.

\# : Bu karakterden sonra:

o : Değerin önüne ‘0’ ekler.

x,X : Değerin önüne ‘0x’ ya da ‘0X’ ekler.

e, E, f : Ondalıklı nokta daima bulunur.

g, G : Ondalıklı nokta daima bulunur ve izleyen sıfırlar atılmaz.

Genişlik Karakterleri

n : En az ‘n’ tane karakter yazdırılır. Çıkış değeri ‘n’ karakterden az ise boşluklarla doldurulur.

0n : En az ‘n’ tane karakter yazdırılır. Çıkış değeri ‘n’ karakterden az ise sağa dayalı olan sayının sol tarafı ‘0’ ile doldurulur.

\* : Genişlik için gerekli olan değer, değişken listesinden okunur.

Hassasiyet Karakterleri

.n : ‘n’ tane karakter yazdırılır.

.\* : Hassasiyet değeri değişken listesinden okunur.

Tip Tanımlama Karakterleri

F : Değer “far pointer” olarak okunur.

N : Değer “near pointer” olarak okunur.

h : d, i, o, u, x ve X önünde olduğunda “short int”; u önünde olduğunda ise “unsigned short int” olarak ele alınır.

l : d, i, o, u, x ve X önünde olduğunda “long int”; u önünde olduğunda “unsigned long int”; e, E, F, g ve G önünde olduğunda ise “double” olarak ele alınır.

L : e, E, F, g ve G önünde olduğunda “long double” olarak ele alınır.

Tip Karakterleri

d : 10 tabanında işaretli tamsayı.

i : 10 tabanında işaretli tamsayı.

o : 8 tabanında işaretli tamsayı.

u : 10 tabanında işaretsiz tamsayı.

x : 16 tabanında işaretsiz tamsayı (9’dan sonraki rakamlar küçük harflerle ‘a,b,c,d,e,f’ gösterilir.

X : 16 tabanında işaretsiz tamsayı (9’dan sonraki rakamlar küçük harflerle ‘A,B,CD,E,F’ gösterilir.

e : Üstel formda yazılan işaretli ondalıklı sayıyi ifade eder. (Üs belirteci olarak ‘e’ kullanılır.

E : Üstel formda yazılan işaretli ondalıklı sayıyi ifade eder. (Üs belirteci olarak ‘e’ kullanılır.

f : İşaretli ondalıklı sayı.

g : Belirtilen değer ve hassasiyete göre ‘e’ ya da ‘f’ formunda işaretli ondalıklı sayıdır.

G : Belirtilen değer ve hassasiyete göre ‘E’ ya da ‘F’ formunda işaretli ondalıklı sayıdır.

c : Tek karakteri ifade eder.

s : Alfasayısal bilgiyi ifade eder.

n : Near Pointer’ı ifade eder.

p : Pointer’ı ifade eder.

**A. Escape Düzeni Kısmı**

‘\\’ işareti ile başlayan bu karakterlerin anlamı aşağıda verilmiştir.

\\n : İmleci (cursor) bir alt satırın ilk sütununa (newline) konumlandırır.

\\r : İmleci bulunduğu satırın ilk sütununa (return) konumlandırır.

\\b : İmleci bir sütun geriye (Backspace) konumlandırır.

\\a : Zil (beep) sesi verir

\\t : Yatay tab işlemi gerçekleştirilir.

\\v : Düşey tab işlemi gerçekleştirilir. (Yazıcı için yeni satır başı işlemi gerçekleştirilir.)

\\f : Yazıcı için yeni sayfa başı işlemi gerçekleştirilir.

\\\\ : ‘\\’ işareti yazdırılır.

\\” : Çift tırnak (“) işareti yazdırılır.

\\’ : Tek tırnak (‘) işareti yazdırılır.

\\? : ‘?’ işareti yazdırılır.

\\ddd : 8 tabanındaki sayının ASCII karşılığı yazdırılır.

\\xddd : 16 tabanındaki sayının ASCII karşılığı yazdırılır.

\\0 : ‘NULL’ karakteri yazdırılır.

Örnek Ekran Görüntüsü

#include <stdio.h>

void main(void)

{

int a=65;

printf(“%d\\n”,65);

printf(“%d\\n”,60+5);

printf(“%d\\n”,a);

}

Örnekteki printf fonksiyonlarının tümünde “%d\\n” şeklindeki format stringi kullanılmıştır. Bu stringin “\\n” şeklindeki parçası özel bir karakter gösterimi olup, satır sonu karakterine karşılık gelmektedir. Bu karakterin ekrana yazdırılması ile imleç konumu değişecek ve bir sonraki satırın ilk sütununa geçilmiş olacaktır. Format stringinde yer alan “%d” şeklindeki diğer parça ise bir format dizgisidir. Argüman olarak verilen değerin desimal notasyon altında (‘d’ karakteri desimal’i belirtir) ve tamsayı formunda yazılacağını gösterir.

Format stringleri içinde birbirinden farklı format dizgileri kullanılarak aynı değerin değişik notasyonlar ile yazdırılması ya da değişik formlar altında yorumlanması sağlanabilir.

**Örnek:**

#include <stdio.h> **Ekran**

void main(void)

{

printf(“%c\\n”,65);

printf(“%d\\n”,65);

printf(“%o\\n”,65);

printf(“%x\\n”,65);

}

Yukarıdaki programda printf( ) fonksiyonu kullanılarak; 65 değerine karşılık gelen ASCII karakteri, desimal(on’lu) tamsayı, oktal(sekiz’li) tamsayı ve heksadesimal(onaltı’lık) tamsayı olarak ayrı ayrı yazdırılmıştır. Aşağıdaki tabloda değişkenler için kullanılabilecek olan tipler listelenmiştir.

Her format stringi içinde sabit bilgiler, format dizgileri ve özel karakter dizgileri yer alabilir. Format stringinin icra anındaki değerlendirilişi soldan sağa doğru olduğu için, bu stringi oluşturan bilgi ve dizgilerin (herhangi bir sırada ve istenildiği adet kullanılabilir) ekran üzerindeki görüntüleniş sıraları da soldan sağa doğru olacaktır.

Bir format stringi içinde birden fazla format dizgisinin yer alması durumunda format dizgileri sayısı ile, format dizgisini izleyen argüman sayısının birbirine eşit olması gerekir.

Bildirimden de anlaşılacağı gibi, printf( ) fonksiyonu yazım işleminin yanısıra bir dönüş değeri de üretmektedir. Fonksiyon tarafından üretilen değer, ekrana yazdırılan karakterlerin toplam sayısıdır.

**Örnek :** **Ekran**

#include <stdio.h>

void main(void)

{

int boy;

boy=printf(“Uzunluk“);

printf(“=%d’dir”,boy);

}

{Rıfat Çölkesen sizof örneği}

**3.6.2. putchar( ) **

int putchar( int ch);

Parametresi olan karakteri (ch) ekranda imlecin bulunduğu yere yazar.

...

char ch;

...

putchar(ch);

...

bu örnekte ‘ch’ değişkeninin değeri ekrana yazdırılır. “putchar(ch)” fonksiyonu, “printf(“%c”,ch)” ile aynı işleme sahiptir.

**3.8.3. putch( ) **

int putch( int ch);

Parametresi olan karakteri (ch) ekranda imlecin bulunduğu yere yazar.

**3.8.4. puts( ) **

int puts( const char \*s) ;

NULL ile sonlandırılmış karakter dizisini standart çıkışa yazmak için kullanılır.

**3.8.5. cprintf( ) **

‘printf()’ fonksiyonu ile aynı görevde olup renkli ya da belirtilen pencere içindeki çıktılarda kullanılır.

3.9. KARŞILAŞTIRMA KOMUTLARI

**3.9.1. if**

“if” deyimleri, farklı koşullar altında farklı komutların işletilmesini sağlarlar. “if” deyimi, ‘if ‘ anahtar sözcüğünün arkasına parantez içinde yazılmış bir karşılaştırma ifadesi ve peşinden gelen bir komut ya da komut bloğundan oluşur. Parantezler içine yazılmış olan ifade mantıksal olarak Doğru ise ‘if’ten sonra yazılan komut ya da komut bloğu işlem görecektir. İfadenin Yanlış olması durumunda ise ‘if’ten sonraki komut ya da komut bloğu atlanacak yani işlem görmeyecektir.

if (size>=100)

{

<komutlar>;

}

**3.9.2. if ... else**

if’ deyimi ile birlikte isteğe bağlı olarak bir ‘else’ anahtar sözcüğü kullanılabilir. Böyle bir kullanımda parantez içindeki karşılaştırma ifadesinin değeri Doğru ise ‘if’ten sonraki komut ya da komut bloğu, ‘if’ten sonraki karşılaştırma ifadesinin değeri Yanlış ise ‘else’ten sonraki komut ya da komut bloğu işlem görecektir.

İf (x>y)

{

printf(“%d”,x);

}

else

{

printf(“%d”,y);

}

**3.9.3. if ... else ... if **

‘if ... else’ deyimleri, art arda sıralanarak aşağıdaki gibi bir yapıda kullanılabilir.

if (koşul1)

<komutlar1>;

else if (koşul2)

<komutlar2>;

else if (koşul3)

<komutlar3>;

else if (koşul4)

<komutlar4>;
Koşulların yorumlanmasına ilk if deyiminden başlanır; koşul yanlışsa bir sonraki ‘else’e geçilir. Herhangi bir ‘if’ deyiminin koşulu ‘Doğru’ ise, o ‘if’ deyimini izleyen komutlar yürütülecek ve programın akışı, diğerleri (‘if’ ve ‘else’ deyimleri) atlanarak bir sonraki deyimden devam edecektir.

Eğer ‘if’ ve ‘else’ deyimlerinden sonra tek bir komut varsa, aç ve kapa küme karakterlerini kullanrak bir komut grubu oluşturmaya gerek yoktur. Aç ve kapa küme karakterleri birden fazla komut var ise komut grubu oluşturmak için kullanılır.

**3.9.4. switch( )**

‘switch’ deyimi birden çok seçenek arasından birinin seçilmesi için kullanılır.

** **Bir tamsayı ya da karakter(char) değişkenin kontrolu için kullanılır. “if” şart cümlesi gibi işlev görür. “case” ile kullanılır.

case 1 :

ifadesi, “switch” ile belirtilen değişkenin değeri 1 ise bundan sonraki komutları çalıştır anlamındadır.

Değişken ise “switch(a)” örneğinde (a) dır.

“switch”in genel formu

switch(a)

{

case 1 : komutlar;

break;

case 2 : komutlar;

break;

case 100: komutlar;

break;

default : komutlar;

}

şeklindedir.

“default” şartı, girilen bilginin hiçbir şarta uymadığı durumlarda yerine getirilir. “default” isteğe bağlı olarak kullanılır. Bütün şartlar kontrol edilmiş ancak uygun olan bulunamamışsa “default”un altındaki komutlar yerine getirilecektir. Eğer şartlardan herhangi biri gerçekleşmiş ise program “break” deyimini görene kadar sonraki komutları yerine getirir.

“switch” cümlesi için bilinmesi gereken 3 önemli nokta vardır.

1. “switch” cümlesi yalnızca eşitliklerde çalışır. (Büyükse, küçükse gibi durumlarda çalışmaz.)

2. Aynı “switch” döngüsü içinde aynı adı taşıyan birden fazla case bulunmaz. Ancak ikinci bir switch döngüsü içinde aynı adı taşıyan case kullanılabilir.

3. “switch” cümlesi içinde karakter sabiti kullanılacak olursa o karakter yerine otomatik olarak yazılacaktır.

Teknik olarak “break” komutu switch ifadesi içinde isteğe bağlı olarak kullanılır. Breakler “switch” ifadesi içine cümleyi sınırlamak, bitirmek için yerleştirilir. Eğer “case” “break”siz kullanıyorsa işlemler icra edilmeye devam edilir. Ta ki “break” deyimi ya da end “ } ” görünceye kadar; Sonraki “case”ler etiket gibi algılanırlar. Programın icrası bir etiketten başlayıp “break” ya da “end” görününceye kadar devam eder.

3.10. DÖNGÜ KOMUTLARI

Program içerisinde istenilen işlemlerin (komut ya da komut bloklarının) istenilen sayıda ya da belirtilen koşulun durumuna göre tekrarlanmasını sağlayan komutlardır.

**3.8.1. for döngüsü**

‘for’ döngüsü, bir komutu ya da komut bloğunu birçok kez tekrarlamak için kullanılır. ‘for’ döngüsü, ‘for’ anahtar sözcüğü, arkasında içinde iki noktalı virgülle ayrılmış üç ifade ve ondan sonra gelen bir deyimden oluşur. İfadelerden herhangi biri var olmayabilir ancak noktalı virgller mutlaka bulunmalıdır.

‘for’ döngüsü diğer döngülerden iki açıdan farklılık gösterir. İlki, döngü sayacını olması ve bu sayaca başlangıç değerinin verilmesi, ikincisi ise döngü sayacının her adım sonunda otomatikman arttırılabilme olanağıdır.

Genel Yazım Biçimi;

for (başlangıç;koşul;artım)

{

komutlar; // döngü bloğu

}

‘başlangıç’ döngü sayacına ilk değer atama deyimidir. ‘koşul’, doğru olduğu sürece çevrim yenilenir. ‘koşul’ kontrolü döngüye girmeden önce yapılır. ‘artım’ her çevrim sonunda döngü sayacının ne kadar artacağını belirler. Bu üç ifade birbirinden noktalı virgül ile ayrılır. Genelde, ‘başlangıç’ ve ‘artım’ bir atama deyimi, ‘koşul’ ise bir karşılaştırma işlemidir.

for(i=1;i<=10;i++)

{

printf(“%d”,i);

}

**3.10.2. while döngüsü**

Belirtilen koşul doğru olduğu sürece döngü içindeki işlemlerin tekrarlanmasını sağlar. Komutlar bölümünde istenildiği kadar komut bulunabilir. Eğer bu bölüm tek bir komut ya da bloktan oluşuyorsa blok başlangıcı ve sonu işaretleri "{" ve "}“ kullanılmayabilir.

“while” döngüsünün genel formu aşağıdaki gibidir.

while(koşul)

{

komutlar;

}

Döngü içindeki komutlar, koşul doğru olduğu sürece tekrarlanır. Koşul doğru olmadığında (“while” komut satırı icra ettirildiğinde şart doğru olmadığında) program akışı döngünün bir alt satırından devam eder.

“while” döngülerinde, “for” döngülerinde olduğu gibi koşulun doğru olup olmadığı döngünün başında kontrol edilir ki bu da bazı durumlarda döngünün içindeki komutların hiç çalıştırılmaması sonucunu doğurabilir.

#include <stdio.h>

void main (void)

{

int i=0;

while (i<10)

{

printf(“%d\\n”,i);

i++;

}

printf(“Döngü sonu …\\n”);

}

**3.10.3. do ... while döngüsü**

** **“for” ve “while” döngülerinden farklı olarak “do-while” döngüsünde, döngü koşulu döngünün sonunda kontrol edilir. Bunun anlamı da “do-while” döngüsünün içinde yer alan komutların en az bir defa çalıştırılacağıdır.

“do-while” döngüsünün genel formu aşağıdaki gibidir.

do

{

komutlar;

} while(koşul);

Aşağıdaki program bloğunda 1’den 100’e kadar olan sayılar görüntülenecektir.

a=0;

do

{

a++;

printf(“%4d”,a);

} while (a<100);

**3.10.4. break ve continue komutları**

Bir döngüye girildiğinde istenilen koşul sağlandıktan sonra döngü içerisindeki bloğun kalan kısım işlenmeden atlanarak döngüden çıkmak için “break” komutu kullanılır.

for(i=0;i<100;i++)

{

printf(“%d”,i);

if(i==10) break;

}

Yukarıdaki program parçası 0’dan 10’a kadar sayıları ekrana yazdırır.

Yine bir döngüye girildiğinde istenilen koşul sağlandıktan sonra döngü içinde bulunan bloğun geri kalan kısmını işlenmeden atlayarak döngünün tekrar başına dönmek için “continue” komutu kullanılır.

Aşağıdaki döngü yalnızca prozitif (+) sayıları gösterir.

do

{

scanf(“%d”,&x);

if(x<0) continue;

printf(“%d\\n”,x);

} while(x!=100);

**3.10.4. goto komutu**

Program akışını belirtilen program kesimine aktarmak için kullanılır. Ancak yapısal programlama dillerinde bu tür dallanmalar tercih edilmez. Daha doğrusu, komut yapılarından ve programlama yöntemlerinden dolayı kullanımına gerek kalmaz.

**Örnek :**

x=0;

t=0;

basla

x++;

t=t+x;

if (x<100) goto basla;

printf(“\\n Toplam=%d”,t);

3.11. FONKSİYON TANIMI VE KULLANIMI

İyi tasarlanmış bir program, büyük bir programı dahi küçük parçalara böler. C bunu, fonksiyon kullanımı ile sağlar. Fonksiyon(function), belli bir işi yapmak üzere tasarlanmış olan program parçasıdır. Fonksiyonlar, parametre (değer) kullanabilirler. Parametreler kullanılmışsa bunlar üzerinde bazı işlemler yapılabilir. Fonksiyonun işleyişi bittiği zaman, bir değer geri gönderebilir (return) ya da herhangi bir değer göndermeyebilir. İyi yazılmış bir fonksiyon, birçok program tarafından(yeniden yazılmadan) kullanılabilir.

Fonksiyonlardan sağlanan yararlar şöyle sıralanabilir :

Fonksiyonlar hem programın etkinliğini attrırı hem de yazılım esnasında büyük kolaylıklar sağlarlar.

Program içinde defalarca kullanılacak olan bir program parçasının yalnızca bir kez yazılması yeterli olacaktır. İstenilen program kesiminden bu fonksiyona erişim sağlanabilir.

Parametrilk olarak hazırlanan fonksiyonlar aynı amaçlarla başka programlarda da kullanılabilirler. Bu programcı için büyük zaman tasarrufu sağlar. Önceden hazırlanmış bir fonksiyon kolayca başka programlara aktarılabilir.

Programların daha az yer kaplamasının sağlar ve program üzerindeki değişiklikleri kolaylaştırır.

Bir C programı bir ya da birden çok fonksiyondan oluşur. “main( )” fonksiyonu mutlaka olmak zorundadır. Program bir tek fonksiyondan oluşuyorsa, bu fonksiyonun adı “main” olmalıdır. Programın çalışması daima “main( )” fonksiyonundan başlar. “main( )” fonksiyonun diğer fonksiyonlardan öne ya da sonra yazılmış olması önemli değildir.

Bir fonksiyonun genel yapısı aşağıdaki gibidir.

tip fonksiyon adı (parametre listesi)

{

yerel tanımlamalar;

<komutlar>;

}

**Örnek :**

#include <stdio.h>

void yaz (int a, int b)

{

printf(“%d %d\\n”,a,b);

}

void main(void)

{

int x=5,y=7;

yaz(x,y);

yaz(x+5,y+x);

}

Bir fonksiyon içende başka bir fonksiyon yazılamaz. Bir fonksiyonun yazılabilmesi için ondan önce yazılmış olan fonsiyonun yazımının bitmiş olması gerekir.

Her programda olduğu gibi her fonksiyonda da veriler verilir, işlenir ve bir sonuç elde edilir.

{özyenilemeli fonksiyonlar – Aksoy-Akgöbek 133}

3.12. İŞARETÇİ (POİNTER) TANIMI VE KULLANIMI

**3.12.1. İşaretçi Tanımlaması**

Tüm bilgisayar programlama dillerinin temelinde pointer veri tipleri bulunmaktadır. Fakat Fortran ve Basic gibi dillerde pointer’ların kullanımı programcıya ya sunulmamış ya da çok sınırlı olarak sunulmuştur. C programlama dilinde pointer’ların kullanımı en üst düzeydedir, hatta zorunludur.

Tipik olarak bir bilgisayar, ayrı ayrı ya da bitişik gruplar halinde idare edilebilen ardışık olarak sayısallaştırılmış ya da adreslenmiş bellek hücrelerinin bir dizisine sahiptir. Pointer değişken , bellekteki bir yerin adresini (byte sıra numarasını) içeren bir değişkendir.

İşaretçiler neden kullanılır : {Aksoy – Akgöbek - 137}

Bir pointer değişken izleyen şekilde tanımlanır;

tip\_adı \* değişken;

Bu tanımlamada değişken adının önüne ‘\*’ konulduğuna dikkat edin.

Pointer veri tipini kullanımını aşağıdaki örneklerle gösterelim;

char C=‘A’; /\* karakter tipinde veriyi gösteren pointer değişken \*/

Şimdi p değişkenine bir adres ataması yapalım (& sembolü bir değişkenin önüne yazıldığı vakit , o değişkenin bellekteki adresini gösterir).

P=&C;

Bu tanımlama ile C değişkeninin adresi P değişkenine atanır. Şu anda P pointeri C değişkenini göstermektedir. Bunu şematik olarak aşağıdaki gibi gösterebiliriz. (burada &C adres değeri sayısal olarak 100 ile gösterilmiştir).

&c &p

‘A’ 100

100

Burada dikkat ederseniz P’ye C’nin değeri değil C’nin adresi (100 degeri) atanmaktadır.

Pointer değişkeninin sahip olduğu adres değerini kullanarak bu adreste bulunan değere ulaşmak ve onu değiştirmek mümkündür.

printf (“%c”,\*p);

Burada \*p , p’nin gösterdiği adresteki bilgi anlamına gelmektedir. Adreste ne tip bir bilgi bulunduğu pointer değişkeninin tanımlanması sırasında verilmiş (char \*p). Yukarıdaki komutun icrası sırasında ekrana ‘A’ karakteri çıkacaktır.

Eğer adresteki değer değiştirilmek istenirse,

\*P=‘B’;

komutuyla yapılabilir. Bu durumda C’nin değeri ‘B’ karakteri olacaktır.

Bu iki olayı şematik olarak aşağıdaki gibi gösterebiliriz.

&c &p

\*p p

#include<stdio.h>

void main(void)

{

int degisken,\*isaretci;

degisken=55;

clrscr();

isaretci=&degisken;

printf("İşaretçinin Adresi..:%p\\n",isaretci);

printf("İşaretçinin Değeri..:%d\\n",\*isaretci);

printf("-------------------------\\n");

printf("Değişkeninin Adresi..:%p\\n",&degisken);

printf("Değişkeninin Değeri..:%d\\n",degisken);

}

**3.12.2. İşaretçi Aritmetiği**

İşaretçiler kullanılırken, bazen işaret ettiği adres taban olarak alınıp, o adresten daha ilerideki ya da gerideki adreslere erişilmek istenebilir; ya da işaret edilen bellek gözünün bir sonrasını işaret etmesi istenebilir. Bu ve benzeri durumlarda işaretçilerin aritmetik işlemlerde kullanılması gerekecektir. İşaretçiler ancak toplama (+,++) ve çıkarma (-,--) işlemlerinde operand olarak kullanılabilir.

4. ALGORİTMALAR

*4.1. MATEMATİKSEL İŞLEM İÇEREN ALGORİTMALAR*

4.1.1. Dışarıdan girilen bir N sayısına kadar olan sayıların toplamını bulan program.

4.1.1.1. Akış Şeması

4.1.1.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int i, n, toplam;

clrscr( );

printf (“N sayısını giriniz”);

scanf (“%d”,&n);

toplam=0;

for (i=1;i<=n; i++)

toplam=toplam+i;

printf(“Toplam=%d”,toplam);

}

4.1.2. Dışarıdan girilen bir N sayısına kadar olan tek sayıların toplamını bulan program.

4.1.2.1. Akış Şeması

4.1.2.3. C Program Kodu

#include <stdio.h>

void main (void)

{

int i, n, sonuc;

clrscr( );

printf(“N Sayısını Giriniz..:”);

scanf(“%d”,&n);

sonuc=0;

i=1;

while (i<=n)
{

sonuc=sonuc+i;

i=i+2;

}

printf(“N e kadar olan tek sayıların toplamı..:%d”,sonuc);

}

4.1.3. Yarıçapı dışarıdan girilen bir dairenin çevresini ve alanını bulan program.

4.1.3.1. Akış Şeması

4.1.3.3. C Program Kodu

#include <stdio.h>

#define pi 3.14

void main(void)

{

float r, cevre, alan;

clrscr( );

printf(“Yarıçap..:”);

scanf(“%f”,&r);

cevre=2\*pi\*r;

alan=pi\*r\*r;

printf(“Çevre..:%f\\n”,cevre);

printf(“Alan...:%f”,alan);

}

4.1.4. Katsayıları dışarıdan girilen ikinci dereceden bir denklemin çözüm kümesini bulan program.

ax2 + bx + c = 0 ikinci derece denkleminin köklerini bulmak için öncelikle Δ (delta)’nın bulunmadı gerekir.

Δ = b2 – 4ac

Δ bulunduktan sonra köklerin (çözüm kümesinin) incelenmesine geçilir.

d < 0 ise x = reel kök yok

d = 0 ise x = (-b)/2a

d > 0 ise x1= (-b -√ d ) / (2a) x1= (-b +√ d ) / (2a)

4.1.4.1. Akış Şeması

4.1.4.3. C Program Kodu

#include<stdio.h>

#include<math.h>

void main(void)

{

int a,b,c;

float x1,x2,d;

clrscr();

printf("a..:");scanf("%d",&a);

printf("b..:");scanf("%d",&b);

printf("c..:");scanf("%d",&c);

d=b\*b-4\*a\*c;

if(d==0)

{

x1=(-b)/(2\*a);

printf("x=%d",x1);

}

else

{

if(d>0)

{

x1=(-b-sqrt(d))/(2\*a);

x2=(-b+sqrt(d))/(2\*a);

printf("x1=%f\\n",x1);

printf("x2=%f",x2);

}

else

{

printf("Reel kök yoktur");

}

}

}

4.1.5. Kendisi hariç tam bölenlerinin toplamı kendisine eşit olan sayılara “mükemmel sayılar” denir. Dışarıdan girilen bir N sayısına kadar olan mükemmel sayıları listeleyen program.

4.1.5.1. Akış Şeması

4.1.5.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int i, j, n, s;

clrscr( );

printf(“Sayıyı Giriniz..:”);

scanf(“%d”,&n)

for(i=2;i<=n;i++)

{

s=1;

for(j=2;j<=(i/2);j++)

{

k=i/j;

k=k\*j;

if (k==i) s=s+j;

}

if (s==i) printf(“Mükemmel Sayı..:%d”,i);

}

}

4.1.6. Analog bir saatte akrep ile yelkovan arasındaki küçük açıyı bulan program.

4.1.6.1. Akış Şeması

4.1.6.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int saat, dakika;

float daci, saci, aci;

clrscr( );

printf(“Saat..:”); scanf(“%d”,&saat);

printf(“Dakika..:”); scanf(“%d”,&dakika);

daci=dakika\*6;

saci=saat\*30+dakika\*0.5;

if (daci>saci) aci=daci-saci;

else aci=saci-daci;

if (aci>180) aci=360-aci;

printf(“Aci=&f”,aci);

}

4.1.7. Dışarıdan girilen bir sayının rakamları toplamını bulan program.

4.1.7.1. Akış Şeması

4.1.7.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int sayi, toplam, k,l;

clrscr( );

printf(“Sayıyı giriniz..:”);

scanf(“%d”,&sayi);

toplam=0;

while (sayi>9)

{

k= sayi / 10;

l=sayi/k\*10;

sayi=sayi/10;

toplam=toplam+k;

}

toplam=toplam+sayi;

printf(“Rakamları toplamı..:%d”,toplam);

}

4.1.8. Dışarıdan girilen bir sayının rakamlarını tersine çeviren program.

4.1.8.1. Akış Şeması

4.1.8.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int sayi, toplam, k, l;

clrscr( );

printf(“Sayıyı giriniz..:”);

scanf(“%d”,&sayi);

toplam=0;

while (sayi>9)

{

k=sayi/10;

l=sayi-k\*10;

sayi=sayi/10;

toplam=toplam\*10+k;

}

toplam=toplam\*10+sayi;

printf(“Ters..:%d”,toplam);

}

4.1.9. Dışarıdan girilen üç değişkenden en büyük olanı bulan program.

4.1.9.1. Akış Şeması

4.1.9.3. C Program Kodu

#include<stdio.h>

#include<math.h>

void main(void)

{

int x,y,z;

int enb;

clrscr();

printf("X=");scanf("%d",&x);

printf("Y=");scanf("%d",&y);

printf("Z=");scanf("%d",&z);

if(x>y)

{

if(x>y) enb=x;

else enb=y;

}

else

{

if(y>z) enb=y;

else enb=z;

}

printf("En büyük eleman ..:%d",enb);

}

4.1.10. Dışarıdan girilen bir N sayısına kadar olan sayıların karelerinin toplamını hesaplayan program.

4.1.10.1. Akış Şeması

4.1.10.3. C Program Kodu

#include<stdio.h>

void main (void)

{

int i,n;

float toplam;

clrscr( );

printf (“N sayısı ....: ”);

scanf (“%d”, &n);

toplam=0;

for(i=1;i<=n; i++)

toplam=toplam+i\*i;

printf(“N’e kadar olan sayıların kareleri toplamı ...: %f”,toplam);

}

4.1.11. Dışarıdan girilen herhangi bir ondalıklı sayıyı, tam ve ondalıklı kısımlarına ayıran program.

4.1.11.1. Akış Şeması

4.1.12. Dışarıdan girilen N sayının ortalamasını bulan program.

4.1.12.1. Akış Şeması

4.1.12.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,sayi,n;

int toplam;

float ortalama;

printf("Dizilerin eleman sayısını giriniz..:");

scanf("%d",&n);

toplam=0;

for(i=0;i<n;i++)

{

scanf("%d",&sayi);

toplam=toplam+sayi;

}

ortalama=toplam/n;

printf("Ortalama=%f",ortalama);

}

4.1.13. Aşağıdaki formu ekrana yazdıran program.

| 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- |
| 3 | 5 | 7 | 9 | 11 |
| 4 | 7 | 10 | 13 | 16 |
| 5 | 9 | 13 | 17 | 21 |
| 6 | 11 | 16 | 21 | 26 |

4.1.13.1. Akış Şeması

4.1.13.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j;

clrscr();

for(i=1;i<=5;i++)

{

for(j=1;j<=5 ;j++)

printf("%3d",i\*j+1);

printf("\\n");

}

}

4.1.14. Aşağıdaki formu ekrana yazdıran program.

|  |  |  | \* |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | \* | \* | \* |  |  |
|  | \* | \* | \* | \* | \* |  |
| \* | \* | \* | \* | \* | \* | \* |

4.1.14.1. Akış Şeması

4.1.14.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n;

clrscr();

printf("Satır Sayısı..:");

scanf("%d",&n);

for(i=1;i<=n;i++)

{

for(j=1;j<=n-i;j++)

printf(" ");

for(j=1;j<=(i\*2-1);j++)

printf("\*");

printf("\\n");

}

}

4.1.15. Dışarıdan girilen iki sayının OKEK’ini bulan program.

4.1.15.1. Akış Şeması

4.1.15.3. C Program Kodu

4.1.16. 1’den 999’a kadar olan sayılar içerisinden basamaklarının küpleri toplamı kendisine eşit olan sayıları bulan program.

4.1.16.1. Akış Şeması

4.1.16.3. C Program Kodu

#include<stdio.h>

#include<dos.h>

void main(void)

{

int i,n;

int kuptoplam,bir,on,yuz;

clrscr();

for(i=1;i<=999;i++)

{

yuz=i/100;

on=(i-yuz\*100)/10;

bir=i-(yuz\*100+on\*10);

kuptoplam=bir\*bir\*bir+on\*on\*on+yuz\*yuz\*yuz;

if(i==kuptoplam) printf("%d\\n",i);

}

}

4.1.17. Dışarıdan girilen N sayısına kadar olan asal sayıları bulan program.

4.1.17.1. Akış Şeması

4.1.17.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n;

int dizi\[100\];

clrscr();

printf("N değeri..:");

scanf("%d",&n);

for(i=2;i<n;i++)

dizi\[i\]=1;

for(i=2;i\*i<n;i++)

{

if(dizi\[i\]==1)

{

j=i+i;

while(j<n)

{

dizi\[j\]=0;

j=j+i;

}

}

}

for(i=2;i<n;i++)

{

if(dizi\[i\]==1) printf("%d\\n",i);

}

}

4.1.18. Bazı sayılar sırası ile 2,3,4,5,6,7,8,9,10’a bölümdüklerinde yine sırası ile 1,2,3,4,5,6,7,8,9 kalanlarını vermektedir. Dışarıdan girilen N sayısına kadar olan sayılardan bu özelliği taşıyan sayıları listeleyen program. {Örnek 2519}

4.1.18.1. Akış Şeması

4.1.18.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n,kont;

clrscr();

printf("N değeri..:");

scanf("%d",&n);

for(i=1;i<=n;i++)

{

kont=1;

for(j=2;j<=10;j++)

if(!((i % j) == (j-1))) kont=0;

if(kont==1) printf("%d\\n",i);

}

}

4.1.19. İkilik tabanda verilen bir sayıyı onluk tabana çeviren program.

4.1.19.1. Akış Şeması

4.1.19.3. C Program Kodu

#include<stdio.h>

#include<string.h>

void main(void)

{

char iki\[100\];

int kat,s,i,on,kont;

clrscr();

printf("ikilik Sistemdeki Sayı..:");

scanf("%s",iki);

kat=1;

on=0;

i=strlen(iki)-1;

kont=1;

while((i>=0)&&(kont==1))

{

if(iki\[i\]=='1')

{

on=on+kat;

}

else

{

if(iki\[i\]!='0') kont=0;

}

kat=kat\*2;

i=i-1;

}

if(kont==1) printf("Onluk Sistemdeki Karşılığı..:%d",on);

else printf("SayЌ ikilik sistemde de§il");

}

4.1.21. Aşağıdaki formu ekrana yazdıran program.

| 1 |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2 | 3 |  |  |  |
| 4 | 5 | 6 |  |  |
| 7 | 8 | 9 | 10 |  |
| 11 | 12 | 13 | 14 | 15 |

4.1.21.1. Akış Şeması

4.1.21.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,s;

clrscr();

s=1;

for(i=1;i<=5;i++)

{

for(j=1;j<=i;j++)

{

printf("%3d",s);

s=s+1;

}

printf("\\n");

}

}

4.1.22. Çarpma işlemini kullanmadan dışarıdan girilen iki sayının çarpımını bulan program.

4.1.22.1. Akış Şeması

4.1.22.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,s;

int x,y;

clrscr();

s=0;

printf("X=");

scanf("%d",&x);

printf("Y=");

scanf("%d",&y);

for(i=1;i<=x;i++)

s=s+y;

printf("%dx%d=%d",x,y,s);

}

4.1.23. Dışarıdan üç kenarının uzunluğu girilen bir üçgenin ne çeşit bir üçgen olduğunu bulan program.

4.1.23.1. Akış Şeması

4.1.23.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int a,b,c;

int ucg;

clrscr();

printf("a..:");scanf("%d",&a);

printf("b..:");scanf("%d",&b);

printf("c..:");scanf("%d",&c);

if(a==b)

{

if(a==c) ucg=3;

else ucg=2;

}

else

{

if(a==c) ucg=2;

else

{

if(b==c) ucg=2;

else ucg=1;

}

}

switch(ucg)

{

case 1 : printf("Çeşit Kenar Üçgen"); break;

case 2 : printf("İkiz Kenar Üçgen"); break;

case 3 : printf("Eşkenar Üçgen"); break;

}

}

4.1.24. Dışarıdan girilen iki sayının OBEB’ini bulan program.

4.1.24.1. Akış Şeması

4.1.24.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int x,y,t;

int a,b;

clrscr();

printf("X=");scanf("%d",&x);

printf("Y=");scanf("%d",&y);

a=x;

b=y;

if((a>0) && (b>0))

{

do

{

if(a<b)

{

t=a;

a=b;

b=t;

}

a=a-b;

} while (a!=0);

printf("%d ile %d nin OBEB i %d",x,y,b);

}

}

4.1.25. Dışarıdan girilen bir tamsayının rakamları arasındaki en büyük sayıyı bulan program.

4.1.25.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int sayi,k,l;

int enb;

clrscr();

printf("Sayıyı Giriniz...:");

scanf("%d",&sayi);

enb=0;

while(sayi>9)

{

k=sayi/10;

l=sayi-k\*10;

sayi=k;

if(enb<l) enb=l;

}

if(enb<sayi) enb=sayi;

printf("Rakamlar arasındaki en büyük rakam..:%d",enb);

}

4.1.26. f(x) kesikli fonksiyonunun değeri X’in aldığı değere göre aşağıda verilmiştir. X’in değeri 0-10 arasında 0.5 aralıklarla arttığına göre her bir X değeri için f(x) fonksiyonunun değerini hesaplayan program.

0 ≤ x ≤ 2 => f(x) = x

2 < x ≤ 3 => f(x) = x3 – x2 - 2

3 < x ≤ 4 => f(x) = x2 – 2x + 13

4 < x => f(x) = x4 – 3x2 - 43

4.1.26.1. Akış Şeması

4.1.26.3. C Program Kodu

#include<stdio.h>

void main(void)

{

float x,f;

clrscr();

do

{

printf("N Değerini Giriniz..:");

scanf("%f",&x);

} while(x<0);

if(x<=2) f=x;

else

if(x<=3) f=x\*x\*x-x\*x-2;

else

if(x<=4) f=x\*x-2\*x+13;

else

f=x\*x\*x-3\*x\*x-43;

printf("%f",f);

}

4.1.27. “pi” sayısının formülü aşağıdaki gibi olduğuna göre serinin paydasındaki ifade dışarıdan girildiğinde “pi” sayısını hesaplayan program.

4.1.27.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int n,isaret;

float i,s;

clrscr();

printf("N sayısını Giriniz..:");

scanf("%d",&n);

i=3;

s=1.0;

isaret=-1;

do

{

s=s+isaret\*(1/i);

i=i+2;

isaret=isaret\*(-1);

} while(i<=n);

s=s\*4;

printf("pi=%f",s);

}

4.1.28. Dışarıdan girilen dört sayının en büyüğünü sayıyı bulan program.

4.1.28.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int a,b,c,d,enb;

printf(“1. Sayıyı Giriniz :”);scanf(“%d”,&a);

printf(“2 Sayıyı Giriniz :”);scanf(“%d”,&b);

printf(“3 Sayıyı Giriniz :”);scanf(“%d”,&c);

printf(“4 Sayıyı Giriniz :”);scanf(“%d”,&d);

if (a>b) enb=a; else enb=b;

if (c>enb) enb=c;

if (d>enb) enb=d;

printf(“En Büyük Sayı =%d\\n”,enb);

}

4.1.29. Aşağıdaki formu ekrana basan program.

1

2 1

3 2 1

4 3 2 1

5 4 3 2 1

**4.2. DİZİ ALGORİTMALARI **

4.2.1. N elemanlı bir dizideki elemanların toplamını bulan program.

4.2.1.1. Akış Şeması

4.2.1.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int i, n, toplam;

int dizi\[100\];

clrscr( );

printf (“N Sayısını Giriniz..:”);

scanf (“%d”,&n);

for (i=0;i<n; i++)

scanf (“%d”,&dizi\[i\]);

toplam=0;

for (i=0;i<n; i++)

toplam=toplam+dizi\[i\];

printf(“Toplam=%d”,toplam);

}

4.2.2. N elemanlı bir dizideki pozitif elemanların ortalamasını bulan program.

4.2.2.1. Akış Şeması

4.2.2.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int i, n, k;

int dizi\[100\];

float sonuc;

clrscr( );

printf (“N sayısını giriniz..:”);

scanf (“%d”,&n);

sonuc=0;

k=0;

for (i=0;i<n; i++)

scanf (“%d”,&dizi\[i\]);

for (i=0;i<n; i++)

{

if (dizi\[i\]>=0)

{

sonuc=sonuc+dizi\[i\];

k++;

}

}

sonuc=sonuc/k;

printf(“Ortalama=%f”,sonuc);

}

4.2.3. N elemanlı bir dizideki en küçük elemanı ve bu elemanın adresini bulan program.

4.2.3.1. Akış Şeması

4.2.3.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int i, n, yer, enk;

int dizi\[100\];

clrscr( );

printf (“N sayısını giriniz..:”);

scanf (“%d”,&n);

for (i=0;i<n; i++)

scanf (“%d”,&dizi\[i\]);

enk=dizi\[0\];

yer=0;

for (i=1;i<n; i++)

{

if(enk>dizi\[i\])

{

enk=dizi\[i\];

yer=i;

}

}

printf(“En Küçük Eleman=%d Yeri=%d”,dizi\[yer\],yer);

}

4.2.4. Dışarıdan girilen N elemanlı bir diziyi yedek dizi kullanmadan tersine çeviren program.

4.2.4.1. Akış Şeması

4.2.4.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int n,yedek;

int dizi\[100\];

clrscr( );

printf(“Dizinin Boyutunu giriniz...:”);

scanf(“%d”, &n);

for(i=1;i<=n;i++)

scanf(“%d”,&dizi\[i\]);

for(i=1;i<n/2;i++)

{

yedek=dizi\[i\];

dizi\[i\]=dizi\[n+1-i\];

dizi\[n+1-i\]=yedek;

}

for(i=1;i<=n;i++)

printf(“%d ”,dizi\[i\]);

}

4.2.5. N elemanlı bir dizideki tek elemanları dizinin başına çift elemanları dizinin sonuna taşıyan program.

4.2.5.1. Akış Şeması

4.2.5.3. C Program Kodu

#include <stdio.h>

void main (void)

{

int kont,i,n,bas,son,yedek;

int dizi\[100\];

clrscr( );

printf(“Dizinin Eleman Sayısını Giriniz..:”);

scanf(“%d”,&n);

for(i=1;i<=n;i++)

scanf(“%d”,&dizi\[i\]);

bas=1;

son=n;

while(bas<son)

{

kont=dizi\[bas\] / 2;

kont=kont\*2;

if(kont==dizi\[bas\])

{

yedek=dizi\[bas\];

dizi\[bas\]=dizi\[son\];

dizi\[son\]=yedek;

son=son-1;

}

else

bas=bas+1;

}

for(i=1;i<=n; i++)

printf(“%d ”,dizi\[i\]);

}

4.2.6. Fibbonacci Sayıları

Fib \[i\] = { 1, 1, 2, 3, 5, 8, 13, 21, ...}

4.2.6.1. Akış Şeması

4.2.6.3. C Program Kodu

#include <stdio.h>

void main (void)

{

int i,n;

int fib\[100\];

clrscr( );

printf(“N Sayısını Giriniz..:”);

scanf(“%d”,&n);

fib\[1\]=1;

fib\[2\]=1;

for (i=3;i<n;i++)

fib\[i\]=fib\[i-1\]+fib\[i-2\];

for (i=1; i<=n;i++)

printf (“%d”,fib\[i\]);

}

4.2.7. Bir dizideki en büyük eleman ile en küçük eleman arasındaki farkı (rank) bulan program.

4.2.7.1. Akış Şeması

4.2.7.3. C Program Kodu

#include <stdio.h>

void main (void)

{

int i,n,enk,enb,rank;

int dizi\[100\];

clrscr( );

printf(“Dizinin Eleman Sayısını giriniz ...:”);

scanf(“%d”,&n);

for (i=0;i<n;i++)

scanf(“%d”,&dizi\[i\]);

enk=dizi\[0\];

enb=dizi\[0\];

for(i=1;i<n;i++)

{

if (enk>dizi\[i\]) enk=dizi\[i\];

else if (enb<dizi\[i\]) enb=dizi\[i\];

}

rank=enb-enk;

printf(“Rank=%d”,rank);

}

4.2.8. Dışarıdan girilen N boyutlu A ve B vektörlerinin skaler çarpımını hesaplayan program.

A= (a1,a2,a3,....,an)

B=(b1,b2,b3,....,bn)

SC=A.B=(a1.b1+a2.b2+a3.b3+....+ an.bn)

4.2.8.1. Akış Şeması

4.2.8.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,n;

int a\[100\],b\[100\];

float sc;

clrscr();

printf("Dizilerin eleman sayısını giriniz..:");

scanf("%d",&n);

printf(“A dizisini giriniz\\n”);

for(i=0;i<n;i++)

scanf("%d",&a\[i\]);

printf(“B dizisini giriniz\\n”);

for(i=0;i<n;i++)

scanf("%d",&b\[i\]);

sc=0;

for(i=0;i<n;i++)

sc=sc+a\[i\]\*b\[i\];

printf("Toplam=%f",sc);

}

4.2.9. Dışarıdan girilen N elemanlı bir dizide 3 ya da 5’e tam bölünebilen elemanları ve bu elamanların sayısını bulan program.

4.2.9.1. Akış Şeması

4.2.9.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,n;

int dizi\[100\];

int sayac;

clrscr();

sayac=0;

printf("Dizinin eleman sayısını giriniz..:");

scanf("%d",&n);

for(i=0;i<n;i++)

scanf("%d",&dizi\[i\]);

for(i=0;i<n;i++)

{

if(!((dizi\[i\]%3)||(dizi\[i\]%5)))

{

sayac++;

printf("%d ",dizi\[i\]);

}

}

printf("Toplam=%d",sayac);

}

4.2.10. Dışarıdan girilen N elemanlı bir dizinin aritmetik, geometrik ve harmonik ortalamasını hesaplayan program.

Ortalamalar :

Aritmetik => AO =

Geometrik => GO =

Harmonik => HO =

4.2.10.1. Akış Şeması

4.2.10.3. C Program Kodu

#include<stdio.h>

#include<math.h>

void main(void)

{

int i,n;

int dizi\[100\];

float ariort,geoort,harort;

clrscr();

ariort=0;

geoort=1;

harort=0.0;

printf("Dizinin eleman sayısını giriniz..:");

scanf("%d",&n);

for(i=0;i<n;i++)

scanf("%d",&dizi\[i\]);

for(i=0;i<n;i++)

{

ariort=ariort+dizi\[i\];

geoort=geoort\*dizi\[i\];

harort=harort+1.0/dizi\[i\];

}

ariort=ariort/n;

geoort=pow(geoort,(1/n));

harort=n/harort;

printf("Aritmetik Ortalama=%f\\n",ariort);

printf("Geometrik Ortalama=%f\\n",geoort);

printf("Harmonik Ortalama =%f\\n",harort);

}

4.2.11. Varyans, bir serideki birim değerlerin aritmetik ortalamadan farklarının toplamının birim sayısına bölümüdür. Standart sapma ise varyansın kareköküdür. Bir dizideki elemanların standart sapmasını ve varyansını bulan program.

4.2.11.1. Akış Şeması

4.2.11.3. C Program Kodu

#include<stdio.h>

#include<math.h>

void main(void)

{

int i,n;

int dizi\[100\];

float ariort,stsapma,varyans;

clrscr();

ariort=0;

varyans=0;

printf("Dizinin eleman sayısını giriniz..:");

scanf("%d",&n);

for(i=0;i<n;i++)

scanf("%d",&dizi\[i\]);

for(i=0;i<n;i++)

ariort=ariort+dizi\[i\];

ariort=ariort/n;

for(i=0;i<n;i++)

varyans=varyans+(dizi\[i\]-ariort)\*(dizi\[i\]-ariort);

varyans=varyans/n;

stsapma=sqrt(varyans);

printf(“Aritmetik Ortalama=%f”,ariort);

printf("Varyans =%f\\n",varyans);

printf("Standart Sapma =%f\\n",stsapma);

}

4.2.12. Bir dizinin elemanlarını dişarıdan girilen bir X sayısına göre küçükleri dizinin baş tarafına, büyükleri ise son tarafına yerleştiren program.

4.2.12.1. Akış Şeması

4.2.12.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,n,x,yedek;

int dizi\[100\];

int bas,son;

clrscr();

printf("Dizinin Eleman Sayısı=");

scanf("%d",&n);

for(i=0;i<n;i++)

scanf("%d",&dizi\[i\]);

printf("X=");

scanf("%d",&x);

bas=0;

son=n-1;

while(bas<son)

{

if(dizi\[bas\]>x)

{

yedek=dizi\[bas\];

dizi\[bas\]=dizi\[son\];

dizi\[son\]=yedek;

son--;

}

else

{

bas++;

}

}

for(i=0;i<n;i++)

printf("%d ",dizi\[i\]);

}

4.2.13. Dışarıdan girilen n elemanlı bir dizideki tek ve çift elemanların ortalamasını bulan program.

4.2.13.1. Akış Şeması

4.2.13.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,n;

int dizi\[100\];

int tektop,cifttop,tekadet,ciftadet;

float tekort,ciftort;

clrscr();

printf("Dizinin Eleman Sayısı=");

scanf("%d",&n);

for(i=0;i<n;i++)

scanf("%d",&dizi\[i\]);

tektop=cifttop=0;

tekadet=ciftadet=0;

for(i=0;i<n;i++)

{

if((dizi\[i\] % 2)==1)

{

tektop=tektop+dizi\[i\];

tekadet++;

}

else

{

cifttop=cifttop+dizi\[i\];

ciftadet++;

}

}

tekort=tektop/tekadet;

ciftort=cifttop/ciftadet;

printf("Tek elemanların toplamı=%d\\n",tektop);

printf("Tek elemanların ortalaması=%f\\n",tekort);

printf("Çift elemanların toplamı=%d\\n",cifttop);

printf("Çift elemanların ortalaması=%f\\n",ciftort);

}

4.2.14. Dışarıdan girilen N elemanlı bir dizideki tek indisli elemanlarının başka bir diziye atayan program.

4.2.14.1. Akış Şeması

4.2.14.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,n,sayac;

int dizi\[100\],tek\[50\];

clrscr();

printf("Dizinin Eleman Sayısını Giriniz..:");

scanf("%d",&n);

for(i=1;i<=n;i++)

scanf("%d",&dizi\[i\]);

i=1;

sayac=1;

while(i<=n)

{

tek\[sayac\]=dizi\[i\];

i=i+2;

sayac=sayac+1;

}

for(i=1;i<=sayac-1;i++)

printf("%d ",tek\[i\]);

}

4.2.15. Dışarıdan girilen N elemanlı bir dizinin en büyük ve ikinci en büyük elemanlarını bulan program.

4.2.16. Dışarıdan girilen bir X değerinini yine dışarıdan girilen N elemanlı bir dizideki elemanlardan hangisine en yakın olduğunu bulan program.

4.2.16.1. Akış Şeması

4.2.16.3. C Program Kodu

#include<stdio.h>

#include<math.h>

void main(void)

{

int i,j;

int n,x,enk,s;

int dizi\[10\];

clrscr();

printf("Dizinin Eleman Sayısı..:");

scanf("%d",&n);

for(i=1;i<=n;i++)

scanf("%d",&dizi\[i\]);

printf("X..:");

scanf("%d",&x);

enk=abs(dizi\[1\]-x);

s=dizi\[1\];

for(i=2;i<=n;i++)

{

if(enk>abs(dizi\[i\]-x))

{

enk=abs(dizi\[i\]-x);

s=dizi\[i\];

}

}

printf("En Yakın Eleman..:%d",s);

}

4.3. MATRİS ALGORİTMALARI

4.3.1. NxM boyutlu bir matristeki en büyük elemanı ve bu elemanın satır ve sütun adresini bulan program.

4.3.1.1. Akış Şeması

4.3.1.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n,m;

int sat,sut,enb;

int mat\[10\]\[10\];

clrscr();

printf("Satır Sayısı ..:");

scanf("%d",&n);

printf("Sütun Sayısı ..:");

scanf("%d",&m);

for(i=1;i<=n;i++)

for(j=1;j<=m;j++)

scanf("%d",&mat\[i\]\[j\]);

enb=mat\[1\]\[1\];

sat=1;

sut=1;

for(i=1;i<=n;i++)

for(j=1;j<=m;j++)

{

if(enb<mat\[i\]\[j\])

{

enb=mat\[i\]\[j\];

sat=i;

sut=j;

}

}

printf("En Büyük Sayı = %d\\n",enb);

printf("Satır = %d\\n",sat);

printf("Sütun = %d",sut);

}

4.3.2. NxN boyutlu bir matrisin esas köşegenin elemanlarının toplamını bulan program.

4.3.2.1. Akış Şeması

4.3.2.3. C Program Kodu

#include <stdio.h>

void main (void)

{

int n, i, j, toplam;

int mat\[10\]\[10\];

clrscr( );

printf(“Matrisin boyutunu giriniz...”);

scanf(“%d”,&n);

for(i=0;i<n;i++)

toplam=toplam+mat\[i\]\[i\];

printf(“Toplam=&d”,toplam);

}

4.3.3. NxM boyutlu iki matrisin toplamını bulan program.

4.3.3.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int i,j,n,m;

int mata\[10\]\[10\], matb\[10\]\[10\], matc\[10\]\[10\];

clrscr( );

for(i=0;i<n;i++)

for(j=0;j<m;j++)

scanf(“%d”,mata\[i\]\[j\]);

for(i=0;i<n;i++)

for(j=0;j<m;j++)

scanf(“%d”,matb\[i\]\[j\]);

for(i=0;i<n;i++)

{

for(j=0;j<m;j++)

{

matc\[i,j\]:=mata\[i\]\[j\]+matb\[i,j\];

printf(“%d”,matc\[i,j\]);

}

printf(“\\n”);

}

}

4.3.5. NxN boyutlu bir matrisin alt üçgen matrisindeki en küçük elemanı bulan program.

4.3.5.1. Akış Şeması

4.3.5.3. C Program Kodu

#include <stdio.h>

void main (void)

{

int i,j,enk,n;

int matris\[10,10\];

clrscr( );

printf(“Kare Matrisin Boyutunu Giriniz..:”);

scanf(“%d”,&n);

for(i=0;i<n;i++)

for(j=0;j<n;j++)

scanf(“%d”,&matris\[i\]\[j\]);

enk=matris\[0\]\[0\];

for (i=1;i<n;i++)

for(j=0;j<n;j++)

if (enk>matris\[i\]\[j\]) enk=matris\[i\]\[j\];

printf(“En küçük eleman = %d”,enk)

}

4.3.6. NxN boyutlu bir matrisin esas ve ters köşegenleri üzerindeki elemanların yerlerini değiştiren program.

4.3.6.1. Akış Şeması

4.3.6.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n,yedek;

int mat\[10\]\[10\];

clrscr();

printf("Kare Matrisin Boyutunu Giriniz ..:");

scanf("%d",&n);

for(i=1;i<=n;i++)

for(j=1;j<=n;j++)

scanf("%d",&mat\[i\]\[j\]);

for(i=1;i<=n;i++)

{

yedek=mat\[i\]\[i\];

mat\[i\]\[i\]=mat\[i\]\[n-i+1\];

mat\[i\]\[n-i+1\]=yedek;

}

for(i=1;i<=n;i++)

{

for(j=1;j<=n;j++)

printf("%3d",mat\[i\]\[j\]);

printf("\\n");

}

}

4.3.7. NxN boyutlu bir matrisin sütunları toplamını başka bir diziye atayan program.

4.3.7.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n;

int mat\[10\]\[10\];

int dizi\[10\];

clrscr();

printf("Kare Matrisin Boyutu ..:");

scanf("%d",&n);

for(i=1;i<=n;i++)

for(j=1;j<=n;j++)

scanf("%d",&mat\[i\]\[j\]);

for(i=1;i<=n;i++)

dizi\[i\]=0;

for(i=1;i<=n;i++)

for(j=1;j<=n;j++)

dizi\[j\]=dizi\[j\]+mat\[i\]\[j\];

for(i=1;i<=n;i++)

{

for(j=1;j<=n;j++)

printf("%5d",mat\[i\]\[j\]);

printf("\\n");

}

printf("\\n");

for(i=1;i<=n;i++)

printf("%5d",dizi\[i\]);

}

4.3.8. NxN boyutlu ve satır ve sütunları kendi içinde sıralı bir matriste, dışarıdan girilen bir X değerini arayan program.

4.3.8.1. Akış Şeması

4.3.8.3. C Program Kodu

4.3.9. Dışarıdan girilen NxN boyutlu bir matrisin her sütununu o sütundaki köşegen elemanına bölen program.

4.3.9.1. Akış Şeması

4.3.9.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n,payda;

float mat\[10\]\[10\];

float sayi;

clrscr();

printf("Kare Matrisin Boyutu ..:");

scanf("%d",&n);

for(i=1;i<=n;i++)

for(j=1;j<=n;j++)

{

scanf("%f",&sayi);

mat\[i\]\[j\]=sayi;

}

for(i=1;i<=n;i++)

{

payda=mat\[i\]\[i\];

for(j=1;j<=n;j++)

mat\[i\]\[j\]=mat\[i\]\[j\]/payda;

}

for(i=1;i<=n;i++)

{

for(j=1;j<=n;j++)

printf("%6.2f",mat\[i\]\[j\]);

printf("\\n");

}

}

4.3.10. Dışarıdan girilen NxN boyutlu bir matrisin her satırındaki en küçük elemanı o satırın ilk gözüne yerleştiren program.

4.3.10.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n;

int yer,enk,yedek;

int mat\[10\]\[10\];

clrscr();

printf("Kare Matrisin Boyutunu Giriniz ..:");

scanf("%d",&n);

for(i=1;i<=n;i++)

for(j=1;j<=n;j++)

scanf("%d",&mat\[i\]\[j\]);

for(i=1;i<=n;i++)

{

for(j=1;j<=n;j++)

printf("%5d",mat\[i\]\[j\]);

printf("\\n");

}

for(i=1;i<=n;i++)

{

enk=mat\[i\]\[1\];

yer=1;

for(j=2;j<=n;j++)

{

if(enk>mat\[i\]\[j\])

{

enk=mat\[i\]\[j\];

yer=j;

}

}

yedek=mat\[i\]\[1\];

mat\[i\]\[1\]=mat\[i\]\[yer\];

mat\[i\]\[yer\]=yedek;

}

for(i=1;i<=n;i++)

{

for(j=1;j<=n;j++)

printf("%5d",mat\[i\]\[j\]);

printf("\\n");

}

}

4.3.11. Dışarıdan girilen NxM boyutlu bir matriste 16 değişik renk kullanılmıştır. Her renkten kaç adet kullanıldığını bulan program.

4.3.11.1. Akış Şeması

4.3.11.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n,m;

int mat\[10\]\[10\],renk\[16\];

clrscr();

printf("Satır Sayısı=");

scanf("%d",&n);

printf("Sütun Sayısı=");

scanf("%d",&m);

for(i=0;i<n;i++)

for(j=0;j<m;j++)

scanf("%d",&mat\[i\]\[j\]);

for(i=0;i<16;i++)

renk\[i\]=0;

for(i=0;i<n;i++)

for(j=0;j<m;j++)

renk\[mat\[i\]\[j\]\]++;

for(i=0;i<16;i++)

printf("%d=%d\\n",i,renk\[i\]);

}

4.3.12. Dışarıdan girilen NxN boyutlu bir matriste bazı hatalar oluşmuştur. Bu hatalar sıfır ile gösterilmiştir. Her satırda kaç tane hata olduğunu bulan program.

4.3.12.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n;

int mat\[10\]\[10\],hata\[16\];

clrscr();

printf("Satır Sütun Sayısı=");

scanf("%d",&n);

for(i=0;i<n;i++)

for(j=0;j<n;j++)

scanf("%d",&mat\[i\]\[j\]);

for(i=0;i<n;i++)

hata\[i\]=0;

for(i=0;i<n;i++)

for(j=0;j<n;j++)

if(mat\[i\]\[j\]==0) hata\[i\]++;

for(i=0;i<n;i++)

printf("%d.sütundaki hata sayısı=%d\\n",i,hata\[i\]);

}

4.3.13. Dışarıdan girilen NxN boyutlu bir matrisin ters köşegeni üzerindeki elemanların toplamını ve çarpımını bulan program.

4.3.13.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j;

int n,toplam,carpim;

int mat\[4\]\[4\];

clrscr();

printf("Satır Sütun Sayısı=");

scanf("%d",&n);

for(i=0;i<n;i++)

for(j=0;j<n;j++)

scanf("%d",&mat\[i\]\[j\]);

toplam=0;

carpim=1;

for(i=0;i<n;i++)

{

toplam=toplam+mat\[i\]\[n-(i+1)\];

carpim=carpim\*mat\[i\]\[n-(i+1)\];

}

printf("Toplam=%d\\n",toplam);

printf("Çarpım=%d\\n",carpim);

}

4.3.14. Dışarıdan girilen NxN boyutlu bir kare matrisin simetrik olup olmadığını bulan program.

4.3.14.1. Akış Şeması

4.3.14.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n;

int yedek,kontrol;

int mat\[10\]\[10\];

clrscr();

printf("Kare Matrisin Boyutunu Giriniz..:");

scanf("%d",&n);

for(i=1;i<=n;i++)

for(j=1;j<=n;j++)

scanf("%d",&mat\[i\]\[j\]);

kontrol=1;

for(i=2;i<=n;i++)

for(j=1;j<=i-1;j++)

{

if(mat\[i\]\[j\]!=mat\[j\]\[i\])

kontrol=0;

}

for(i=1;i<=n;i++)

{

for(j=1;j<=n;j++)

printf("%5d",mat\[i\]\[j\]);

printf("\\n");

}

if(kontrol==1) printf("Matris Simetriktir");

else printf("Matris Simetrik Değildir");

}

4.3.15 Dışarıdan girilen NxN boyutlu bir kare matrisin transpozesini bulan program.

4.3.15.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n;

int yedek;

int mat\[10\]\[10\];

clrscr();

printf("Kare Matrisin Boyutunu Giriniz...:”);

scanf("%d",&n);

for(i=1;i<=n;i++)

for(j=1;j<=n;j++)

scanf("%d",&mat\[i\]\[j\]);

for(i=1;i<=n;i++)

{

for(j=1;j<=n;j++)

printf("%5d",mat\[i\]\[j\]);

printf("\\n");

}

for(i=2;i<=n;i++)

for(j=1;j<=i-1;j++)

{

yedek=mat\[i\]\[j\];

mat\[i\]\[j\]=mat\[j\]\[i\];

mat\[j\]\[i\]=yedek;

}

for(i=1;i<=n;i++)

{

for(j=1;j<=n;j++)

printf("%5d",mat\[i\]\[j\]);

printf("\\n");

}

}

4.3.16. Ana köşegen üzerindeki elemanları “1” , diğer bütün elemanları “0” olan matrise “birim matris” denir. Dışarıdan girilen N sayısına göre NxN tipinde birim matris oluşturan program.

4.3.16.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,n;

int mat\[10\]\[10\];

clrscr();

printf("Kare Matrisin Boyutunu Giriniz..:");

scanf("%d",&n);

for(i=0;i<n;i++)

for(j=0;j<n;j++)

if (i==j) mat\[i\]\[j\]=1;

else mat\[i\]\[j\]=0;

for(i=0;i<n;i++)

{

for(j=0;j<n;j++)

printf("%3d",mat\[i\]\[j\]);

printf("\\n");

}

}

4.4. STRING ALGORİTMALARI

4.4.1. Dışarıdan girilen bir string’i tersten yazdıran program.

4.4.1.1. Akış Şeması

#include<stdio.h>

void main(void)

{

int i;

char cumle\[100\];

clrscr();

printf("Cümleyi Giriniz..: ");

gets(cumle);

printf("Cümlenin Tersi...: ");

for(i=strlen(cumle)-1;i>=0;i--)

printf("%c",cumle\[i\]);

}

4.4.2. Dışarıdan girilen bir string’de her harften kaçar tane olduğunu bulan program.

4.4.2.1. Akış Şeması

4.4.2.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i;

char cumle\[100\];

int harfler\[26\];

clrscr();

printf("Cümleyi Giriniz..: ");

gets(cumle);

for(i=0;i<26;i++)

harfler\[i\]=0;

for(i=0;i<strlen(cumle);i++)

harfler\[cumle\[i\]-'a'\]++;

for(i=0;i<26;i++)

printf("%c=%d ",i+'a',harfler\[i\]);

}

4.4.3. Dışarıdan girilen bir cümlede kaç kelime olduğunu bulan program.

4.4.3.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i, sayac;

char cumle\[100\];

clrscr();

printf("Cümleyi Giriniz..:");

gets(cumle);

sayac=1;

for(i=0;i<strlen(cumle);i++)

{

if(cumle\[i\]==' ')

sayac=sayac+1;

}

printf("Kelime sayısı..:%d",sayac);

}

4.4.5. Dışarıdan girilen bir string’deki en uzun kelimenin uzunluğunu bulan program.

4.4.5.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i;

int sayac,enb;

char cumle\[100\];

clrscr();

printf("Cümleyi Giriniz..:");

gets(cumle);

sayac=0;

enb=0;

for(i=0;i<strlen(cumle);i++)

{

if(cumle\[i\]==' ')

{

if(enb<sayac) enb=sayac;

sayac=0;

}

else

sayac=sayac+1;

}

if(enb<sayac) enb=sayac;

printf("%d",enb);

}

4.5.2. Bubble Sort (Kabarcık Sıralaması). Bu sıralama algoritmasında, sıralanacak olan dizinin elemanları üzerinden tekrar tekrar geçilir ve her geçişte yalnızca yan yana bulunan iki eleman arasında sıralama yapılır. Bu işlem tüm elemanlar sıralanıncaya kadar tekrarlanır. Dizinin başından sonuna kadar bütün elemanlar bir kere bu işlemden geçirildiğinde dizinin en büyük elemanı dizinin en son adresine taşınmış olacaktır. İç döngüde yer alan işlem (yan yana bulunan iki eleman karşılaştırılıp gerekli yer değiştirme işlemi) ile en büyük eleman dizinin hangi adresinde olursa olsun, en sağa kaydırılır. Bir sonraki tarama ise en sağdaki eleman tarama dışı bırakılarak gerçekleştirilir. En sağdaki elemanın dışarıda bırakılması için dış döngünün döngü değişkeni bir azaltılır. Bu işlemler dış döngünün döngü değişkeni 0 (sıfır) olana kadar tekrarlanarak sıralama işlemi tamamlanır.

Eğer herhangi bir tarama işlemi sırasında iç döngüde hiçbr değiştirme işlemi gerçekleştirilmemişse dizi sıralanmış demektir ve kontrol değişkeni sayesinde sonraki aşamalar gerçekleştirilmeden döngüden çıkılır.

4.5.2.3. C Program Kodu

#include <stdio.h>

void main(void)

{

int yer, i, n, kontrol;

int dizi\[100\];

clrscr();

printf(“Dizinin Eleman Sayısını Giriniz”);

scanf(“%d”,&n);

for (i=0;i<n;i++)

scanf(“%d”, &dizi\[i\]);

kontrol=1;

yer=0;

while ((yer<=n-2) && (kontrol==1)) do

{

kontrol:=0;

for (i=0;i<(n-yer);i++)

{

kontrol=0;

yedek=dizi\[i\];

dizi\[i\]=dizi\[i+1\];

dizi\[i+1\]=dizi\[i\];

}

}

for (i=0;i<n; i++)

scanf(“%d”,&n);

}

4.5.3. Shell Sort(Kabuk Sıralaması). {Aksoy Akgöbek -238{

4.5.3.3. C Program Kodu

#include<stdio.h>

void main(void)

{

int i,j,v,n,h;

int dizi\[100\];

clrscr();

printf("Dizinin Eleman Sayısı=");

scanf("%d",&n);

for(i=1;i<=n;i++)

scanf("%d",&dizi\[i\]);

h=1;

while(h<n)

h=3\*h+1;

while(h!=1)

{

h=h/3;

for(i=h+1;i<=n;i++)

{

v=dizi\[i\];

j=i;

while((dizi\[j-h\]>v))

{

dizi\[j\]=dizi\[j-h\];

j=j-h;

if (j<=h) break;

}

dizi\[j\]=v;

}

}

for(i=1;i<=n;i++)

printf("%d ",dizi\[i\]);

}

PAGE

PAGE 1

d D

i I

u U

o O

x X

e E

g G

f

s

c

%

n

p

F

N

h

l

L

n

\*

Yıldız Teknik Üniversitesi

Meslek Yüksekokulu

d i

o

u

x

X

e

E

f

g

G

c

s

n

p

F

N

h

l

L

n

0n

\*

-

+

\#

‘ ’

.n

.\*

65

65

65

A

65

101

41

Uzunluk=7’dir

---
*Kaynak: `PROGRAMLAMA DİLLERİ VE GENEL BAKIŞ/cıktı.doc` — Ugur — 2002*
