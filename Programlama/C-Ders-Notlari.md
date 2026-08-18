# C Ders Notlari

## **C Ders Notları **

## **Mayıs 2001 **

## **Öğr. Gör. H. Turgut Uyar **

## **Önsöz**

Bu notlar henüz tamamlanmamıştır.

Notların hazırlanmasında anlatımı kolaylaştırması açısından C++ dilinin getirdiği bazı yeniliklerden yararlanılmıştır. Örnek programlar verildikleri şekliyle standart C derleyicileri tarafından derlenmeyebilirler; bu programların standart C dilinde yazılmış karşılıkları Ek E'de verilmiştir.

## **İçindekiler**

1 Programlamaya Giri s
1.1 Yap sal Programlama
1.2 Soyutlama
1.3 Program Geli stirme A samalar
1.4 Derleme / Yorumlama
1.5 Kitapl klar
1.6 Standartlar
1.7 Derleme A samalar
2 C Diline Giri s
2.1 Temel Özellikler
2.2 Degi skenler
2.3 Degi sken Tan mlama
2.4 Veri Tipleri
2.5 Giri s / Ç k s
2.6 Deyimler
2.7 Atama
2.8 Aritmetik İslemler
2.8.1 Tip Zorlama
2.8.2 İslemli Atama
2.8.3 Art rma / Azaltma
2.8.4 Öncelik S ras
2.9 Degi smezler
2.10 Makrolar
3 Ak s Denetimi
3.1 Rastgele Say lar
3.2 Ko sul Deyimleri
3.2.1 Kar s la st rma İslemleri
3.2.2 Mant ksal İslemler
3.3 Seçim
3.4 Sayaç Denetiminde Yineleme
3.5 Çoklu Kar s la st rma
3.6 Ko sul Denetiminde Yineleme
3.7 Ko sullu İsleç
3.8 Bo s Döngüler
3.9 Sonsuz Döngüler
3.10 \\.Içiçe Döngüler
4 Diziler
4.1 Tek Boyutlu Diziler
4.2 Çok Boyutlu Diziler
4.3 Ba svurular
5 Katarlar
6 Fonksiyonlar
6.1 Fonksiyonun Bildirimi
6.2 Fonksiyonun Tan m
6.3 Parametre Aktar m
6.4 Tan m Bölgesi
6.5 Seçerek S ralama
6.6 Aktar lan Parametrede Degi siklik
6.7 Dizilerin Fonksiyonlara Aktar m
6.8 Ana Fonksiyona Parametre Aktar m
6.8.1 Ç k s Parametreleri
6.8.2 Hata \\.Iletileri
6.8.3 Giri s Parametreleri
7 \\.Ileri Veri Tipleri
7.1 Tiplere Yeni \\.Isim Verme
7.2 Yap lar
7.3 Birlikler
7.4 Numaraland rma
8 İsaretçiler
8.1 İsaretçi Tipinden Degi skenler
8.2 Bellek Yönetimi
8.3 İsaretçi - Dizi \\.Ili skisi
8.4 Parametre Aktar m
9 Projeler
A C ile C++ Aras ndaki Farklar
B Ayr nt
C Kitapl klar
C.1 Matematik
C.2 Katar
D Uygulamalar
E Örnek Programlar n C Dili Kar s l klar
F Unix'de Program Geli stirme

**Chapter 1
Programlamaya Giriş**

Bir problemi bilgisayar yardımıyla çözmek için öncelikle problemi bilgisayarda işlemeyi sağlayan bir *model* kurulur. Daha sonra da bu model üzerinde çözüme adım adım hangi işlemlerin yapılmasıyla ulaşılacağı belirlenir. Bu işlem sırasına *algoritma* adı verilir. *Program* ise bu algoritmanın bir programlama dili kullanılarak gerçeklenmiş biçimidir. Yani algoritma dilden bağımsızdır, program ise dile bağımlıdır.

Algoritmaların iki temel özelliği vardır:

İyi tanımlanmışlardır: Her adımda ne yapılacağı bellidir. Böylelikle bilgisayar ile gerçeklenebilirler.

Sonludurlar: Sonlu sayıda adımda ya çözümü bulurlar ya da bulamadıklarını bildirirler, sonsuza kadar çalışmazlar.

**Örnek:**

Bir sayı dizisindeki en büyük elemanı (maksimumu) bulan algoritma.

Dizinin ilk elemanını maksimum olarak seç.

Dizide başka eleman varsa 3. adıma git, yoksa dur.

Bir sonraki eleman maksimumdan büyükse bu elemanı maksimum yap.

2. adıma dön.

Algoritmaları göstermek için sıkça kullanılan yöntemlerden biri akış çizenekleridir. Akış çizeneklerinde şu simgeler kullanılır:

Kutu: Bir işlemi gösterir. Kutunun içine işlemi anlatan bir deyim yazılır.

Ok: Akış yönünü belirtir. Algoritmanın bir sonraki adımının hangisi olduğunu gösterir.

Eşkenar dörtgen: Karar noktalarını gösterir. İçine yazılan sorunun yanıtının doğru ya da yanlış olmasına göre farklı bir yöne gidilmesini sağlar.

Algoritmanın tamamı belirtilmişse akış çizeneği yuvarlak içinde bir \`\`start'' sözcüğüyle başlar ve yuvarlak içinde bir \`\`stop'' sözcüğüyle biter.

Yukarıda verilen algoritma örneğinin akış çizeneği Şekil 1.1'de görüldüğü gibidir.

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=maximum.png" |  |
| --- | --- | --- |

Şekil 1.1: Akış çizeneği örneği.

Bazen bir algoritmanın tamamı değil, yalnızca ilgilenilen bir parçası belirtilmek istenebilir. Bu durumda çizenek boş bir yuvarlak ile başlar ve boş bir yuvarlak ile sona erer. Akış çizeneğinin büyümesi ve topluca görülmesinin zorlaşması durumunda akış çizeneği parçalarının başındaki ve sonundaki yuvarlakların içine etiketler yazarak hangi parçanın hangi parçaya nereden bağlandığı belirtilebilir.

## **1.1 Yapısal Programlama**

Program tasarlamada nasıl bir yol izlemenin daha verimli olacağı konusundaki araştırmalar programcılığın ilk günlerinden beri sürmektedir. Küçük çaplı projelerde fazla sorun olmasa da, projenin çapı büyüdükçe ve programı geliştiren insanların sayısı arttıkça hem programın geliştirilmesi hem de geliştirilmiş bir programın bakımının yapılması (düzeltmeler, eklemeler, değişiklikler) zorlaşır. Yapısal programlama, program tasarımı üzerine geliştirilmiş yaklaşımlardan biridir. Programların yapıtaşlarını ve bunların birbirleriyle ilişkilerini düzenleyen kurallardan oluşur.

Yapısal programlamanın temel yapıtaşına *blok* adı verilir. Blok, birbiriyle ilişkili komutların oluşturduğu gruptur. Her program birbirlerine çeşitli şekillerde bağlanmış bloklardan oluşur. Blokları bağlamanın üç yolu vardır:

**Sıra**

Bu yapı, blokların yukarıdan aşağıya doğru yazıldıkları sırayla yürütülmeleri anlamına gelir. Sıra yapısının akışı Şekil 1.2'de çizildiği gibidir.

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=sequence.png" |  |
| --- | --- | --- |

Şekil 1.2: Sıra yapısının akış çizeneği.

**Seçim**

Bu yapı, bir koşulun doğru olup olmamasına göre yürütülecek bloğun seçilmesidir. Yani koşul doğruysa bir blok, yanlışsa başka bir blok yürütülür (Şekil 1.3). İki bloktan herhangi biri boş olabilir, yani sözgelimi \`\`koşul doğruysa şu bloğu yürüt, yanlışsa hiçbir şey yapma'' şeklinde bir yapı kurulabilir.

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=selection.png" |  |
| --- | --- | --- |

Şekil 1.3: Seçim yapısının akış çizeneği.

**Yineleme**

Bu yapı, belirli bir koşul sağlandığı sürece (ya da sağlanana kadar) bir bloğun yinelenmesidir. Akış çizeneğinde (Şekil 1.4) bu yapı için özel bir simge kullanılmayacak, koşul ve eylem simgeleri ile gösterilecektir1.

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=repetition.png" |  |
| --- | --- | --- |

Şekil 1.4: Yineleme yapısının akış çizeneği.

Bu yapıların ortak bir özelliği, hepsinin bir giriş ve bir çıkışlarının olmasıdır. Böylelikle bir bloğun çıkışı öbür bloğun girişine bağlanabilir; başka bir deyişle, bloklar ardarda eklenebilir. Ayrıca, bir bloğun içinde başka bir blok yer alabilir.

## **1.2 Soyutlama**

Yapısal programlamanın temel kavramlarından biri de *soyutlama* (abstraction) kavramıdır. Soyutlama, programın yapacağı işin daha küçük ve birbirinden olabildiğince bağımsız alt-işlere bölünmesidir. Alt-işler de, benzer şekilde, yapacaklarını alt-alt-işlere bölebilirler. Bu tip tasarıma *yukarıdan aşağıya* (top-down) tasarım adı verilir2.

Her iş bir *yordam* (C dilindeki adıyla *fonksiyon*) tarafından gerçeklenir. Ana-yordamın görevi, alt-işleri gerçekleyen yordamları başlatmak ve bunların arasındaki eşgüdümü sağlamaktır. Bir üst-yordam kullandığı alt-yordamların nasıl çalıştıklarıyla değil, yalnızca sonuçlarıyla ilgilenir.

Yordamlar olabildiğince genel amaçlı yazılmalıdır. Sözgelimi bir yordamın işi \`\`BİL102CE dersini alan öğrencilerin yılsonu sınav notlarının en büyüğünü bul'' şeklinde tanımlanabilir. Oysa işi \`\`herhangi bir dizinin en büyüğünü bulmak'' olarak tanımlanan bir yordam olsa ve bu yordam kullanılırken hangi dizinin en büyüğünün bulunmasının istendiği belirtilse daha yararlı olur. Bu durumda hangi dizi üzerinde işlem yapılacağı bilgisi yordamın *giriş parametresi* (ya da argümanı) olur. Yordam çalışması sonucu ürettiği değeri *çıkış parametresi* olarak döndürür. Örnekteki yordam kullanılırken giriş parametresi olarak \`\`BİL102CE dersini alan öğrencilerin yılsonu sınavı notları'' belirtilirse sınavda alınan en yüksek not, \`\`Los Angeles Lakers basketbol takımının oyuncularının boyları'' belirtilirse bu takımın en uzun boylu oyuncusunun boyu çıkış parametresi olur.

Soyutlamanın kazandırdıkları şöyle özetlenebilir:

Bir işi gerçekleyen yordam yazılırken, kullandığı alt-yordamların ayrıntılarıyla uğraşılmaz; alt-yordamın doğru çalıştığı varsayılarak yordamın kendi işine yoğunlaşılabilir. Böylelikle büyük ve çözülmesi zor olan bir sorunla uğraşmak yerine, her biri küçük ve çözülebilir sorunlarla uğraşılır ve bunlar daha sonra biraraya getirilir.

Programın bakımı kolaylaşır. Alt-yordamların çalışmaları birbirlerinden bağımsız olduğundan bir alt-yordamda bir değişiklik yapıldığında bunu kullanan üst-yordam (üst-yordamla olan etkileşim değişmediği sürece) değişiklikten etkilenmez.

## **Örnek**

İki sayının en küçük ortak katı bulunmak isteniyor olsun. Bu ana iş şu şekilde alt işlere bölünebilir:

Birinci sayıyı asal çarpanlarına ayır.

İkinci sayıyı asal çarpanlarına ayır.

Sayıların çarpanlarını kaynaştırarak en küçük ortak katın asal çarpanlarını bul.

Bir önceki adımda belirlediğin asal çarpanlardan en küçük ortak katı hesapla.

Sayıların 6468 ve 945 oldukları varsayılırsa:

6468=2\*2\*3\*7\*7\*11=22\*3\*72\*11

945=3\*3\*3\*5\*7=33\*5\*7

22\*33\*5\*72\*11

291060

1. ve 2. adımlar için herhangi bir sayıyı asal çarpanlarına ayıran bir yordam yazılabilir ve asal çarpanlarına ayrılacak sayı bu yordama parametre olarak yollanabilir. Herhangi bir sayının asal çarpanlarına ayrılması için kullanılabilecek bir algoritma Şekil 1.5'de verilmiştir. Bu algoritmada x asal çarpanlarına ayrılacak sayıyı, f ise çarpan olup olmadığı o anda sınanmakta olan asal sayıyı, p de sıradaki çarpanın kuvvetini gösterir. 945 sayısını örnek olarak alırsak:

Sınanacak ilk asal sayı 2 .

945 > 1 olduğu için 2a adımına git.

945 mod 2 ≠ 0 olduğu için ( 2 sayısı 945 sayısını bölmediği için) 2 bir çarpan değildir.

2 'den bir sonraki asal sayıyı bul ( 3 ).

945 > 1 olduğu için 3a adımına git.

945 mod 3=0 olduğu için 3 bir çarpandır. Kuvveti şimdilik 0 olsun.

945 mod 3=0 olduğu için 3 çarpanının kuvvetini 1 artır ( 1 oldu). Sayıyı 3 'e böl ( 315 oldu).

315 mod 3=0 olduğu için 3 çarpanının kuvvetini 1 artır ( 2 oldu). Sayıyı 3 'e böl ( 105 oldu).

105 mod 3=0 olduğu için 3 çarpanının kuvvetini 1 artır ( 3 oldu). Sayıyı 3 'e böl ( 35 oldu).

35 mod 3 ≠ 0 olduğu için daha fazla 3 çarpanı yoktur.

3 'den bir sonraki asal sayıyı bul ( 5 ).

35 > 1 olduğu için 4a adımına git.

35 mod 5=0 olduğu için 5 bir çarpandır. Kuvveti şimdilik 0 olsun.

35 mod 5=0 olduğu için 5 çarpanının kuvvetini 1 artır ( 1 oldu). Sayıyı 5 'e böl ( 7 oldu).

7 mod 5 ≠ 0 olduğu için daha fazla 5 çarpanı yoktur.

5 'den bir sonraki asal sayıyı bul ( 7 ).

7 > 1 olduğu için 5a adımına git.

7 mod 7=0 olduğu için 7 bir çarpandır. Kuvveti şimdilik 0 olsun.

7 mod 7=0 olduğu için 7 çarpanının kuvvetini 1 artır ( 1 oldu). Sayıyı 7 'ye böl ( 1 oldu).

1 mod 7 ≠ 0 olduğu için daha fazla 7 çarpanı yoktur.

7 'den bir sonraki asal sayıyı bul ( 11 ).

1 > 1 olmadığı için dur.

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=factorize.png" |  |
| --- | --- | --- |

Şekil 1.5: Bir sayıyı asal çarpanlarına ayırma algoritması.

Bu algoritmadaki bir sonraki asal sayıyı bulma işi de asal çarpanlarına ayırma işinin bir alt-işi olarak düşünülerek bir başka yordama bırakılabilir. Bu yordam kendisine parametre olarak gönderilen sayıdan bir sonraki asal sayıyı bularak sonucu geri yollayacaktır.

Ana işin 3. adımındaki kaynaştırma işini yapacak yordamın algoritması geliştirilirken, asal çarpanlarına ayırma yordamının çalışma şekli nedeniyle çarpanların küçükten büyüğe doğru sıralı oldukları varsayılabilir. Bu varsayım altında kaynaştırmayı yapacak algoritma Şekil 1.6'de verilmiştir.

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=merge.png" |  |
| --- | --- | --- |

Şekil 1.6: Asal çarpanlar dizilerini kaynaştırma algoritması.

Bu algoritma her iki çarpan sırasında da eleman bulunduğu sürece yapılacakları göstermektedir. Bir sayının çarpanları bittiğinde diğerinin çarpanları henüz bitmemişse o sayının kalan çarpanları da sonuç çarpanlarına eklenmelidir. Örneğimizden devam edersek:

Birinci dizi: 22\*3\*72\*11 , ikinci dizi: 33\*5\*7 .

22 ile 33 'ü karşılaştır. 2 daha küçük olduğu için 22 en küçük ortak katın bir çarpanıdır. Birinci dizinin sonraki elemanına geç ( 3 ).

3 ile 33 'ü karşılaştır. Tabanlar aynı oldukları için kuvveti daha büyük olanı seç. 33 en küçük ortak katın bir çarpanıdır. Her iki dizinin de sonraki elemanlarına geç.

72 ile 5 'i karşılaştır. 5 daha küçük olduğu için 5 en küçük ortak katın bir çarpanıdır. İkinci dizinin bir sonraki elemanına geç.

72 ile 7 'yi karşılaştır. Tabanlar aynı oldukları için kuvveti daha büyük olanı seç. 72 en küçük ortak katın bir çarpanıdır. Her iki dizinin de sonraki elemanlarına geç.

İkinci dizi bitmiş olduğu için birinci dizide kalan bütün elemanları kuvvetleriyle birlikte al.

## **Örnek**

İki sayının en küçük ortak katının alabileceği en küçük değer, bu iki sayıdan büyük olanıdır. Sözgelimi, 16 ile 64 'ün en küçük ortak katı 64 'tür. Alabileceği en büyük değer ise bu iki sayının çarpımıdır. Bunun için bu iki sayının aralarında asal olmaları, yani en büyük ortak bölenlerinin 1 olması gerekir. Sözgelimi, 21 ile 10 sayılarının en küçük ortak katı 210 'dur. Bu özellikler gözönüne alınarak iki sayının en küçük ortak katını bulmak üzere şöyle bir algoritma da geliştirilebilir:

İki sayıdan küçük olanına min , büyük olanına max adını ver.

Çarpana 1 değerini ver.

max\*carpan , min 'in bir tam katıysa 5. adıma, değilse 4. adıma git.

Çarpanı 1 artır ve 3. adıma git.

En küçük ortak kat max\*carpan sayısıdır.

Bu algoritma sayılardan birinin katlarını hesaplayıp bu değerin diğer sayının da katı olup olmadığının sınanmasına dayanmaktadır. Büyük olan sayının katlarının denenmesi, deneme sayısının azaltılmasını sağlayacağından daha etkin olur. 6468 ve 945 sayılarının en küçük ortak katını bulurken 6468 'in katları denenir: 6468,12936,19404,…,284592,291060 .

## **1.3 Program Geliştirme Aşamaları**

Bir programın geliştirilmesi çeşitli aşamalardan geçer:

**Tasarım**

Bu aşamada programcı, yazacağı programı kağıt üzerinde tasarlar. Yani programın algoritmasına, kullanıcıyla nasıl bilgi alışverişinde bulunacağına, hangi programlama tekniklerini kullanacağına, kısacası neyi nasıl yapacağına karar verir.

**Kodlama**

Bu aşamada programcı tasarım sırasında verdiği kararlara göre programı bir dil kullanarak oluşturur. Bu işlem için editör adı verilen yazılımlar kullanılır. Editörün görevi programcıya kaynak kodunu yazabileceği bir ortam hazırlamaktır. Windows işletim sistemindeki notepad, ya da Unix işletim sistemindeki pico gibi yazılımlar birer editör olmakla birlikte, programcılar genellikle programlamaya yönelik özel yetenekleri olan *programcı editörleri* kullanırlar.

**Sınama**

Bu aşamada program çalıştırılarak çeşitli senaryolar için doğru sonuçlar üretip üretmediğine, beklendiği gibi davranıp davranmadığına bakılır. Bu işlemin etkinliği gözönüne alınan senaryoların gerçekte oluşabilecek durumların ne kadarını örttüğüyle bağlantılıdır.

**Hata Ayıklama**

Bu aşamada sınama aşamasında bulunan hataların nedenleri belirtilerek gerekli düzeltmeler yapılır. Programların ilk yazıldıkları şekliyle doğru olmaları neredeyse tamamen olanaksızdır. Hatta üstüne çok çalışılmış, pek çok hatası bulunup düzeltilmiş programlarda bile bütün hataların bulunup düzeltilmiş olması son derece düşük bir olasılıktır. Ayrıca programlara yeni yetenekler eklendikçe yeni hatalar oluşacağından aşağı yukarı hiçbir program hiçbir zaman tam olarak hatasız olmayacaktır.

## **1.4 Derleme / Yorumlama**

Bilgisayarların çalıştıracakları programların belli bir biçimi olması zorunludur. Bu biçim, bilgisayardan bilgisayara ve işletim sisteminden işletim sistemine göre farklılıklar gösterir. Sözgelimi, bir kişisel bilgisayar üzerinde Windows işletim sisteminde çalışan bir program, Sun marka bir işistasyonunda Solaris işletim sisteminde çalışmaz. Hatta, yine aynı kişisel bilgisayar üzerinde Linux işletim sisteminde de çalışmaz. Programların bu çalıştırılabilir biçimine \`\`*makina kodu*'' (machine code) adı verilir. Makina kodu, insanların anlaması ve üzerinde çalışması son derece zor bir biçim olduğundan programcılar programları doğrudan bu kod ile yazmazlar. İnsanın anlaması daha kolay (insan diline daha yakın) \`\`yüksek düzeyli'' (high-level) bir dil ile yazıp yardımcı yazılımlar aracılığıyla makina koduna çevirir ve çalıştırırlar. Programcının yazdığı bu koda \`\`*kaynak kodu*'' (source code) denir.

Kaynak kodunun makina koduna çevrilmesi ve çalıştırılması işlemi üç farklı yaklaşımla gerçekleştirilebilir:

**Yorumlama**

Programın komutları bir yorumlayıcı (interpreter) tarafından *teker teker* okunur, makina koduna çevrilir ve çalıştırılır. Yani yorumlayıcı, önce birinci komutu okur, makina koduna çevirir ve çalıştırır. Sonra ikinci komutu alır ve aynı işlemleri yapar. Programın her çalışmasında çevirme işlemi yeniden yapılır. Herhangi bir komutta bir hatayla karşılaştığında bunu kullanıcıya bildirir ve çalışmayı durdurur. Basic, Perl, Python gibi diller genellikle yorumlayıcılar aracılığıyla kullanılırlar.

**Derleme**

Program bir derleyici (compiler) tarafından *bir bütün halinde* okunur, makina koduna çevrilir ve çalıştırılır. Çevirme işlemi sonucunda bir çalıştırılabilir dosya oluşur. Çevrilmiş olan program daha sonra çalıştırılır, yani çevirme işlemi yalnızca bir kere yapılır. Herhangi bir komutta bir hata varsa çevirme işlemi tamamlanmaz ve çalıştırılabilir kod oluşturulmaz. Fortran, Pascal, C gibi diller genelde derleyicilerle kullanılmakla birlikte bunları işleyen yorumlayıcılar da bulunabilmektedir.

**Karma**

Hem derleme hem de yorumlama tekniği kullanılır. Bu tip çalışmada kaynak kodu sanal bir bilgisayarın makina koduna (bytecode) çevrilir ve daha sonra bu sanal bilgisayarı gerçekleyen bir program yardımıyla yorumlanarak çalıştırılır. Örneğin Java dilinde yazılmış bir kaynak kodu önce Java derleyicisinden geçirilerek Java sanal makinasının (Java Virtual Machine - JVM) makina koduna dönüştürülür; sonra da bu sanal makinayı gerçekleyen bir Java çalışma ortamı (Java Runtime Environment - JRE) yardımıyla çalıştırılır.

Yorumlama yönteminde kodun okunması ve çevrilmesi programın çalışması sırasında yapıldığından hız düşüktür. Ayrıca yorumlayıcı yalnızca karşılaştığı ilk hatayı rapor edebilir. Bu hata düzeltildiğinde sonraki çalışmada da program ancak bir sonraki hataya kadar ilerleyebilir. Oysa derleyici kaynak kodundaki bütün hataları bulabilir.

Buna karşılık hata ayıklama -özellikle deneyimsiz programcılar için- yorumlayıcılarla daha kolaydır. Derleyicilerle gelen bazı sınırlamaların kalkması nedeniyle daha esnek bir çalışma ortamı sağlanır.

## **1.5 Kitaplıklar**

Bir programcıya gerekebilecek her şeyi programlama dilinin içine almak o dil için yazılan derleyicilerin hantallaşmalarına neden olur. C dili bu nedenle oldukça \`\`küçük'' bir dil olarak tasarlanmıştır. Örneğin basit aritmetik işlemlerin ötesindeki matematik işlemleri dilin tanımı içinde yer almaz. Yani sözgelimi karekök alma işlemi için bir C komutu yoktur.

Bununla birlikte, pek çok programcının bu tip işlemlere gereksinim duyacakları da açıktır. Böyle bir durumda programcı, isterse karekök alma işlemini yapacak kodu kendisi yazabilir. Ancak her programcının kendine gereken işlemler için kendi kodlarını yazmasının önemli sakıncaları vardır:

Programcının yazacağı kod hatalı olabilir. Karekök alma işlemi yapan kod yanlış sonuç üretebilir.

Programcının yazacağı kod yeterince etkin olmayabilir, yani işlemi yapmak için gereğinden fazla zaman ya da sistem kaynağı harcayabilir.

Çok sayıda programcının aynı işleri yapan kodlar yazmaları büyük bir zaman yitirilmesine yol açar.

Hem dilin tanımını küçük tutmak hem de bu sakıncaları giderebilmek için, çok sayıda programcıya gerekebilecek işlemler (yordamlar) *kitaplık* (library) adı verilen arşivlerde toplanmıştır. Bir sayının karekökünü almak isteyen bir programcı matematik kitaplığındaki sqrt yordamını kullanabilir. Kitaplığın kullanılması yukarıda sözü geçen sakıncaları giderir, yani programcıya zaman kazandırdığı gibi, doğru ve etkin çalıştığı sınanmış olduğundan dikkatini programın diğer kısımlarına yoğunlaştırma fırsatı verir.

## **1.6 Standartlar**

C dilinin geliştirilmesinde gözetilen ana hedeflerden biri *taşınabilirlik* (portability) sağlanmasıydı. Taşınabilirlik, bir ortamda (herhangi bir bilgisayar, herhangi bir işletim sistemi) yazılan bir kaynak kodunun başka bir ortamda da -üzerinde fazla değişiklik yapılması gerekmeden- derlenip çalıştırılabilmesidir. Bunun için değişik ortamlardaki derleyiciler arasında bir standart olması gerektiği açıktır. C dilinde yapılan standartlaşma çalışmaları sonucunda oluşan ANSI C standardı, hem C dilinin kurallarını belirler, hem de bir C derleyicisinin bulundurması zorunlu olan standart kitaplıkları ve bu kitaplıklarda yer alacak yordamları tanımlar.

Diğer önemli bir standart olan POSIX standardı ise programlama dili ile işletim sistemi arasındaki bağlantıları belirler. Örneğin dosya silmek, dosya adı değiştirmek, sistemdeki başka bir programla haberleşmek gibi işlemler için gereken yordamlar bu standartta yer alırlar.

Yine de sıkça gereksinim duyulan bütün işlemler için bütün kitaplıklarda bir standart henüz sağlanamamıştır. Örneğin grafik bir arayüze sahip uygulamalardaki grafik işlemlerini yapacak kitaplıklar standartlaştırılmamış olduğundan çeşitli firma ve kurumlar bu işlemleri yapan farklı kitaplıklar geliştirmişlerdir. Dolayısıyla bu kitaplıklar kullanılarak yazılan programlar tam anlamıyla taşınabilir olmamakta, yalnızca bu kitaplığın desteklediği ortamlara taşınabilmektedir.

## **1.7 Derleme Aşamaları**

Kaynak koddan üretilecek olan çalıştırılabilir makina kodunda hem programcının kendi yazdığı yordamların, hem de yararlandığı kitaplık yordamlarının makina koduna çevrilmiş hallerinin bulunması gerekir. Bu nedenle, kaynak kodunun makina koduna çevrilmesi iki aşamada gerçekleşir (Şekil 1.7):

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=compile.png" |  |
| --- | --- | --- |

Şekil 1.7: Derleme aşamaları.

**Derleme**

İlk aşamada kaynak kodu derlenerek bir ara koda dönüştürülür. Bu ara kod, kullanıcının yazdığı yordamların makina kodu karşılıklarını içeren bir dosyadır. Ancak, programcının kullanmış olduğu kitaplık yordamlarını içermediğinden henüz çalıştırılabilir bir kod değildir.

**Bağlama**

İkinci aşamada ise ara kod ile programcının kullandığı kitaplık yordamları arasında bağlantılar kurulur ve çalıştırılabilir dosya üretilir. Sözgelimi, programcı karekök alma için matematik kitaplığındaki bir yordamı kullandıysa, bağlayıcı (linker) ara kodda karekök yordamının kullanıldığı yerlerde gerekli düzenlemeleri yapar. Bu düzenlemeler iki şekilde yapılabilir:

Statik bağlantıda kitaplıktan ilgili yordamın makina koduna çevrilmiş biçimi alınarak ara kod ile birleştirilir ve böylece çalıştırılabilir dosyada gerekli bütün kodlar bulunur.

Dinamik bağlantıda ise yordamın makina kodu biçimi çalıştırılabilir koda eklenmez, yalnızca çalıştırılabilir kodda bu yordamın gerekli olduğuna ilişkin işaretler konur. Gerekli kitaplıkların yüklenmesi ve bağlantıların kurulması ise program çalıştırılmaya başlandığında yapılır.

Dinamik bağlantı yönteminde çalıştırılabilir dosya boyu daha küçük olduğundan ve kitaplıkların makina kodları gereksiz şekilde yinelenmediklerinden sistem kaynakları daha etkin kullanılır. Buna karşılık, programın çalışabilmesi için gereksinim duyduğu kitaplıkların sistemde bulunmaları zorunludur.

## **Sorular**

İki sayının en küçük ortak katını hesaplamak için verilen iki algoritmayı, basitlik ve etkinlik açılarından karşılaştırınız. İkiden fazla sayının en küçük ortak katlarını hesaplamak için bir algoritma geliştiriniz.

**Chapter 2
C Diline Giriş**

## **Örnek**

İlk örnek programımız (Örnek 1), ekrana Merhaba dünya! yazar. Bu örnekte bir C programının temel özellikleri ve ekrana nasıl yazı çıkartılacağı konuları işlenecektir.

```cpp
/* İlk C programım. *
* *
* Bu program ekrana "Merhaba dünya!" iletisini yazar. */
#include <iostream.h> // cout için
#include <stdlib.h> // EXIT_SUCCESS için
int main(void)
{
cout << "Merhaba dünya!" << endl;
return EXIT_SUCCESS;
}
```

#1 Ekrana bir satırlık ileti çıkaran program.

## **2.1 Temel Özellikler**

Örnek üzerinde bir C programının bazı temel özelliklerini görelim:

**Açıklamalar**

Yazdığınız bir kodu başka birinin okuduğunda anlayabilmesi ve hatta ileride kendiniz de anlayabilmeniz için kodun içinde gerekli yerlere açıklamalar yazmanızda büyük yarar vardır. Özellikle kolayca anlaşılmayacak programlama tekniklerinin kullanıldığı kod parçalarının açıklanması gerekir. Açıklamalar derleyici tarafından gözardı edilir, yani programın işleyişlerine hiçbir etkileri yoktur. Kodun içine açıklama iki şekilde yazılabilir3:

Birinci yöntemde, açıklamanın başına bölü-yıldız, sonuna yıldız-bölü simgeleri konur. Bu şekildeki açıklamalar birden fazla satır sürebilir. Örnekteki birinci açıklama birinci satırdaki \`\`İlk C programım'' sözcükleriyle başlar ve üçüncü satırdaki \`\`iletisini yazar.'' sözcükleriyle biter.

İkinci yöntemde ise açıklama çift bölü ile başlar ve satırın sonuna kadar sürer. Kısa açıklamalar için bu yöntem daha kullanışlıdır. Örnekteki ikinci açıklama beşinci satırdaki \`\`cout için'' sözcüklerinden oluşur. Üçüncü açıklama da altıncı satırdaki \`\`EXIT\_SUCCESS için'' sözcüklerini kapsar.

Birinci tipten açıklamalar içiçe yazılamaz, yani bir açıklamanın içine ikinci bir açıklama yazılamaz. İçiçe açıklamalar şu şekilde bir yapı oluşturur:

...a... /\* ...b... /\* ...c... \*/ ...d... \*/ ...e...

Bu yapıda birinci /\* ile açıklama başlar. Açıklamanın içinde görülen ikinci /\* gözardı edilir ve gelen ilk \*/ açıklamayı sona erdirir; yani açıklamayı b ve c bölgeleri oluşturur. Bundan sonra gelen bölüm (d bölgesi) normal C kodu gibi değerlendirileceğinden hataya yol açacaktır.

**Fonksiyonlar**

Yapısal programlamadaki yordamlar C dilinde fonksiyonlar ile gerçekleştirilir. Ana işi yapan fonksiyonun adı main olarak verilmelidir. Programın yürütülmesine ana işten başlanacağı için her programın bir ve yalnız bir main fonksiyonu bulunması zorunludur. Fonksiyonlarla ilgili bilgiler Bölüm 6'de verilecektir. Şimdilik main fonksiyonunun

```cpp
int main(void)
```

şeklinde başlayacağını bilmek yeterlidir.

**Bloklar**

C dili yapısal programlamadaki blok kavramı üzerine kuruludur (bkz. 1.1). Sıra, seçim ve yineleme yapılarının bloklarının yanısıra bir fonksiyonun içerdiği komutlar da bir blok olarak değerlendirilir. Bloklar aç-süslü-parantez ile başlar ve kapa-süslü-parantez ile sona erer. Bizim başlangıçtaki örneklerimizde main fonksiyonunun bloğu

```cpp
return EXIT_SUCCESS;
```

komutuyla sona erecektir. Bu komut programın başarıyla sonlandığını belirtir. Başarısızlık durumunda

```cpp
return EXIT_FAILURE;
```

komutu kullanılır.

**Komutlar**

C dilinde komutlar noktalı virgül ile sona erer. Birden fazla boşluk derleyici tarafından bir tek boşluk olarak değerlendirilir; dolayısıyla bir komutun bir satır içinde başlayıp sona ermesi gibi bir zorunluluk yoktur. Yani

```cpp
cout < < ``Merhaba dünya!'' < < endl;
```

komutu

```cpp
cout < <
``Merhaba dünya!'' < < endl;
```

biçiminde ya da

```cpp
cout < <
```

\`\`Merhaba dünya!''

```cpp
< < endl;
```

biçiminde yazılabilirdi.

**Çıkış**

Ekrana bir ileti yollamak istendiğinde bu ileti çift küçüktür ile cout birimine yönlendirilir. Örnekteki kullanımda ekrana

Merhaba, dünya!

yazılır. Sonda yer alan endl sözcüğü, ileti yazıldıktan sonra yeni satıra geçilmesini sağlar.4

**Katarlar**

Katarlar çift tırnak içinde yazılırlar. Katar içinde yazılan her boşluğun önemi vardır, yani sözgelimi peşpeşe 5 boşluk bırakıldığında bu 1 boşluk olarak değil, 5 boşluk olarak değerlendirilir. Örneğin

```cpp
cout < < ``Merhaba dünya!'' < < endl;
```

komutunda ekrandaki çıktıda Merhaba sözcüğü ile dünya! sözcüğü arasında 5 boşluk bulunacaktır. İngilizce harfler dışında harf kullanamama kısıtlaması da katarlar içinde geçerli değildir.

**Başlık Dosyaları**

Kitaplıklarda tanımlanmış olan fonksiyonlar, araçlar ya da büyüklükler kullanıldığı zaman derleyiciye bunlarla ilgili bilgileri nerede bulabileceğini söylemek gerekir. Bu bilgilerin yer aldığı başlık dosyaları (header files) program başında #include komutuyla belirtilir. Örneğin cout birimi iostream.h başlık dosyasında bulunduğundan örnek programda

```cpp
#include <iostream.h>
```

komutu yer almaktadır. Benzer şekilde, EXIT\_SUCCESS sözcüğünün kullanılabilmesi için stdlib.h dosyası içerilmelidir.

Bir kitaplıktan yararlanacağınız zaman gerekecek bilgilerin hangi başlık dosyasında yer aldığını belirlemeniz gerekir. Bunların büyük bir kısmı standartlarla belirlenmiş olmakla birlikte (bkz. Bölüm 1.6) standartlara girmemiş fonksiyonlar için kullandığınız derleyici ve kitaplıkların dokümantasyonuna bakmanız gerekecektir5.

C dilinde komutların noktalı virgül ile sona ermesi ve fazla boşluklar ile satır geçişlerinin öneminin olmaması nedeniyle komutlar satırlara istendiği şekilde yerleştirilebilir. Ancak bu konuda bir düzene uyulmazsa kodun okunması ve anlaşılması son derece zorlaşır. Okunabilirliği artırmak amacıyla alt-bloklar bir miktar içeriden başlatılırlar (*girintileme*). Böylece aynı düzeydeki (aynı bloğa ait) komutlar aynı hizadan başlarlar. Örnekte fonksiyon bloğundaki bütün komutlar satır başından 4 harf içeriden başlamaktadır. Özellikle içiçe yapıların kullanıldığı durumlarda (seçimin içindeki yinelemenin içindeki seçimin içindeki seçim gibi) blokları hiyerarşik bir şekilde girintilemek büyük önem taşır.

## **Örnek**

Bu bölümde kullanılacak program (Örnek 2) yarıçapını kullanıcıdan aldığı bir dairenin alanını hesaplayarak sonucu ekrana yazar. Bu örnek, geleneksel yöntemle çalışan (grafik bir arayüzü bulunmayan) programlara tipik bir örnektir. Programın işleyişi, kullanıcıdan verilerin alınması, işlenmesi ve sonuçların bildirilmesi şeklindedir.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS
#define PI 3.14
#define sqr(x) ((x) * (x))
int main(void)
{
float radius;
float circum, area;
cout << "Yarıçap: ";
cin >> radius;
circum = 2 * PI * radius;
area = PI * sqr(radius);
cout << "Çevre: " << circum << endl;
cout << "Alan: " << area << endl;
return EXIT_SUCCESS;
}
```

#1 Bir dairenin çevresini ve alanını hesaplayan program.

## **2.2 Değişkenler**

Değişkenler, programın işleyişi sırasında değişik değerler alabilen varlıklardır. Her değişken, değeri baştan belli olmayan ya da programın işleyişi sırasında değişebilecek bilgileri gösterirler. Örneğimizde radius dairenin yarıçapını, circum dairenin çevresini, area dairenin alanını gösteren değişkenlerdir.

Değişken adlarının uymaları gereken bazı kurallar vardır:

Adlar, İngilizce büyük ve küçük harfler, rakamlar ve altçizgi işaretinden oluşabilir. Bu kurala göre pi, weight, weight1 ve weight\_1 geçerli adlardır, ancak π, ağırlık ve weight-1 geçerli adlar değildir.

Adın ilk simgesi bir rakam olamaz. Bu kurala göre 2weight geçerli bir ad değildir.

Adın ilk 31 simgesi anlamlıdır. Başka bir deyişle, ilk 31 simgesi aynı olmayan iki adın farklı olacağı kesindir ancak daha uzun adlarda ilk 31 simge aynı ise çalıştığınız derleyici bu iki adın farklı olmadığına karar verebilir.

Adlarda büyük-küçük harf ayrımı vardır. Yani weight1, Weight1, WEIGHT1 ve wEiGHt1 adlarının hepsi geçerli olmakla birlikte hepsi birbirinden farklıdır.

C dilinin sözcükleri ad olarak seçilemez. Yani örneğin int, main, void, return geçerli adlar değildir.

Kesin kural olmamakla birlikte değişkenlere verilen adlarda çoğu programcının uyduğu bazı gelenekler de vardır:

Değişken adları küçük harflerle başlar. Başka bir deyişle, büyük harfler ya da altçizgi işaretiyle başlamaz.

Değişkenlere, gösterdikleri bilgiye uygun düşen, anlamlı bir ad verilir. Sözgelimi bir insanın ağırlığı bilgisini tutacak bir değişkene x4szb gibi anlamsız ya da height gibi yanıltıcı adlar verilmez.

Anlamlı adlar verilmek istendiğinde bazen değişken adının birden fazla sözcük içermesi gerekebilir. Bu durumda değişken adını oluşturan iki sözcük bir altçizgi işaretiyle birleştirilir (örneğin birth\_month) ya da ikinci sözcük büyük harfle başlar (örneğin birthMonth).

## **2.3 Değişken Tanımlama**

Bir değişkene bir değer vermeden ya da değerini bir hesapta kullanmadan önce değişkenin tanımlanması gerekir. Tanımlama işlemi, bellekte gerektiği kadar yerin bu değişken için ayrılmasını sağlar; böylece sistem, bellekte ayrılan bu yeri bu değişken için kullanır ve başka işlerde kullanmaz.

Tanımlama, değişkenin tipinin ve adının belirtilmesinden oluşur. Örnekte

```cpp
float radius;
```

tanımı derleyiciye radius adında bir değişken olduğunu ve bunun bir gerçel sayı olduğunu belirtmeye yarar.

Aynı tipten olan değişkenler aynı tanımın içinde yer alabilirler. Örnekteki

```cpp
float circum, area;
```

tanımı derleyiciye her ikisi de birer gerçel sayı olan, circum ve area adında iki değişken kullanacağımız anlamına gelir. Örnekteki tanımlar istenirse

```cpp
float radius;
float circum;
float area;
```

şeklinde ayrılarak ya da

```cpp
float radius, circum, area;
```

şeklinde birleştirilerek de yapılabilirdi.

Tanım sırasında istenirse değişkene başlangıç değeri de verilebilir.

```cpp
float radius, circum = 0.0, area = 0.0;
```

Bu durumda tanım sırasında circum ve area değişkenlerinin her ikisine de 0.0 değeri verilir, radius değişkenine bir başlangıç değeri verilmez.

Genelde bir blok içindeki değişken tanımları ile komutlar birbirlerinden ayrılır. Yani kullanılacak bütün değişkenlerin tanımları bittikten sonra komutlar başlar. Gelenek olarak tanımların sona erdiği ve komutların başladığı yerin kolayca görülmesini sağlamak amacıyla tanımlar ile komutlar arasında bir satır boşluk bırakılır.6

## **2.4 Veri Tipleri**

C dilinde değişkenlerin alabilecekleri temel veri tipleri şunlardır:

int: Tamsayı. Bu veri tipi short ve long niteleyicileriyle geliştirilerek kısa tamsayı (short int) ve uzun tamsayı (long int) tipleri oluşturulabilir. Aksi belirtilmedikçe tamsayı tiplerinin işaretli oldukları varsayılır, yani hem pozitif hem de negatif değerler alabilirler. Değişken yalnızca pozitif sayılardan (0 da olabilir) değer alacaksa işaretsiz olarak tanımlamak için unsigned sözcüğü kullanılabilir. Kısacası, 6 adet tamsayı tipi vardır: int, short int, long int, unsigned int, unsigned short int ve unsigned long int.

float: Gerçel (kesirli) sayı.

double: Çifte duyarlılıklı gerçel sayı. Bu veri tipi de long niteleyicisiyle geliştirilerek uzun çifte duyarlılıklı gerçel sayı (long double) veri tipi oluşturulabilir.

char: Simge. Simge tipinden değerler tek tırnak işaretleri arasında gösterilirler: 'a', 'M', '5' ya da '?' gibi. '5' ile 5 aynı şey değil. ASCII tablosu.

bool: Mantıksal. Bu tipten değişkenler true (doğru) ya da false (yanlış) değerlerini alabilirler.

Bir değişkenin tanımlanacağı veri tipi, o değişkenin alabileceği değer aralığını belirlediğinden son derece önemlidir. Bu nedenle bir değişkenin veri tipine karar verirken o veri tipinin izin verdiği değer aralığına dikkat etmek gerekir. Sözgelimi short int veri tipi yalnızca \[−32768,+32767\] değer aralığındaki sayıların gösterilebilmesine olanak veriyorsa ve sizin tanımlayacağınız değişkenin 45000 değerini alması sözkonusu olabilecekse değişkeninizi bu tipten tanımlamamalısınız.

Bir veri tipinin boyu sizeof işlemi yardımıyla belirlenebilir. Her değişken bellekte bu boy kadar yer kaplar (sekizli cinsinden). Aşağıdaki komutlar çalıştığınız sistemde tamsayı tabanlı veri tiplerinin öğrenilmesi için kullanılabilir:

```cpp
cout < < ``int tipinin boyu: '' < < sizeof(int) < < endl;
cout < < ``short int tipinin boyu: '' < < sizeof(short int) < < endl;
cout < < ``long int tipinin boyu: '' < < sizeof(long int) < < endl;
```

Kısa tamsayı veri tipinin boyunun 2 sekizli yani 16 bit olduğunu varsayalım. Bu değer hem işaretli hem de işaretsiz kısa tamsayılar için geçerlidir. Bu durumda işaretsiz kısa tamsayı cinsinden tanımlanan bir değişkenin alabileceği en küçük değer 0 , en büyük değer ise 216−1 olacaktır.

## **2.5 Giriş / Çıkış**

İlk örnek programda kullanıcı, programın işleyişi üzerinde herhangi bir etki yaratamıyordu; bu örnekteyse toplanacak sayıları kendisi belirleyebiliyor. Bunun yapılabilmesi için kullanıcının yazdığı sayıların ilgili değişkenlere aktarılması gerekir. cout biriminin çıkış için kullanımının çok benzerini cin birimi giriş için sağlar. Örnekteki

```cpp
cin > > radius;
```

komutu sonucunda radius değişkeni kullanıcının yazdığı sayının değerini alır.

Birden fazla değişken birlikte okunmak isteniyorsa bunlar birbiri ardına > > işaretleriyle belirtilebilirler. Sözgelimi, iki tane yarıçap değeri okunacak ve radius1 değişkeni kullanıcının yazdığı birinci sayının, radius2 değişkeni de kullanıcının yazdığı ikinci sayının değerini alacaksa:

```cpp
cout < < ``Yarıçapları yazın: ``;
cin > > radius1 > > radius2;
```

Bu örnekte kullanıcının sayıları yazarken aralarında bir boşluk bırakması gerekir.

Yine ilk örnekte çıkış da hep aynı katarın ekrana aktarılmasına dayanıyordu. İkinci örneğimizde ise çıkış programın her çalışmasında farklı olacaktır. cout birimine aktarım yapılırken çift tırnak içine yazılmayan bölümler değişken değerleri olarak yorumlanır. Örnekteki

```cpp
cout < < ``Çevre: `` < < circum < < endl;
```

komutu ekrana önce \`\`Çevre'' katarını yazar, daha sonra circum değişkeninin değerini yazar ve yeni satıra geçer.

## **2.6 Deyimler**

Deyimler bir hesabı ifade eden cümle parçalarıdır. Sayılar, değişkenler ve işlemlerden oluşurlar. Bir deyim yalnızca bir sayı ya da yalnızca bir değişken olabileceği gibi, bunların işlemler ile çeşitli şekillerde birleştirilmelerinden de oluşabilir. Örnekler:

2

radius

2 \* radius

radius \* radius

Deyimleri yazarken tamsayıların ve gerçel sayıların çeşitli gösterilim biçimleri kullanılabilir:

Tamsayıların olağan gösterilimleri onlu düzendedir, ancak istenirse sekizli ya da onaltılı düzende de gösterilebilirler. 0 rakamı ile başlayan sayıların sekizli, 0x ile başlayanların onaltılı düzende oldukları varsayılır. Buna göre, 38 sayısı sekizli düzende 046, onaltılı düzende 0x26 olarak yazılır.

Gerçel sayıların olağan gösterilimi noktalı gösterilimdir, ancak istenirse bilimsel gösterilim ( mantis\*10us ) de kullanılabilir. Sayının yazılışında E simgesi geçiyorsa bu simgenin öncesi mantis, sonrası üs olarak değerlendirilir. Buna göre, 0.01 sayısı bilimsel gösterilimde 1E-2 olarak yazılır.

## **2.7 Atama**

Örnekteki

```cpp
circum = 2 * PI * radius;
```

komutu bir atama komutudur. Atama, bir değişkene bir değer verilmesi işlemidir (simgesel olarak circum← 2\*PI\*radius şeklinde de gösterilir). Atama işlemi eşit işaretiyle yapılır ve işaretin sol tarafına bir değişken adı, sağ tarafına ise bir deyim yazılır. Sağ tarafta yer alan deyim hesaplanarak sonucu sol tarafta belirtilen değişkene atanır.7

Atama işlemi bir matematiksel eşitlik *DEĞİLDİR*. Öyle olsaydı

```cpp
2 * PI * radius = circum;
```

şeklinde bir komut geçerli olurdu. Oysa bu komut C dilinde hatalı bir komuttur, çünkü eşit işaretinin sol tarafına bir deyim yazılamaz. İşlem sonucunun sol tarafa yazılan değişkene atanacağı gözönüne alınırsa bu yazımın neden yanlış olduğu da görülebilir; sol tarafta sonucun atanabileceği bir varlık yer almamaktadır.

Atama işleminin bir matematiksel eşitlik olmadığına ilişkin diğer bir örnek de şu komuttur:

```cpp
a = a + 17;
```

Matematiksel açıdan bakıldığında bu yazılan yanlıştır ( 0=17 ). Oysa bu komutun anlamı \`\`a değişkeninin değeri ile 17 sayısını topla ve sonucu yeniden a değişkenine yaz'' cümlesiyle açıklanabilir.

Komutların okunurluğunu artırmak amacıyla C programcılarının uydukları geleneklerden biri de, eşit işaretinin öncesinde ve sonrasında birer boşluk bırakmaktır. Benzer şekilde, deyimlerde yer alan işlem simgelerinin (örnekte + simgesi) önce ve sonralarında da birer boşluk bırakılır.

## **2.8 Aritmetik İşlemler**

Aritmetik deyimlerde kullanılabilecek aritmetik işlemler şunlardır:

Toplama: + işleciyle gerçeklenir.

Çıkartma: - işleciyle gerçeklenir.

Çarpma: \* işleciyle gerçeklenir.

Bölme: / işleciyle gerçeklenir.

Kalan (modulo): % işleciyle gerçeklenir. Yalnızca iki tamsayı arasında yapılabilir, gerçel sayılara uygulanamaz.

İşleme giren sayıların her ikisi de tamsayı ise sonuç da tamsayı olur. Sayılardan herhangi birinin gerçel sayı olması durumunda sonuç da gerçel sayı olacaktır. Bu durum bölme işleminde dikkat edilmesi gereğini doğurur. Bölme işlemine giren her iki sayı da tamsayı ise sonuç da tamsayı olacaktır, yani sonucun varsa kesir kısmı atılacaktır. Örneğin 14 / 4 deyiminin sonucu 3.5 değil 3 olacaktır. İşleme giren her iki sayı da tamsayı ise ve sonucun kesir kısmının yitirilmemesi isteniyorsa sayılardan birinin gerçel sayı olmasını sağlamak gerekir. Yukarıdaki örnek için çözüm

14.0 / 4

14 / 4.0

14.0 / 4.0

gibi yazılışlarla sağlanabilir.

## **2.8.1 Tip Zorlama**

Bir bölme işlemine giren iki değişkenin ikisinin de tamsayı tipinden olması durumunda sonuç yine tamsayı olacaktır. Örneğin

```cpp
int num1 = 14, num2 = 4;
float quotient;
quotient = num1 / num2;
```

işlemleri sonucu quotient değişkeni 3.0 değerini alır. Son bölme deyiminde hiçbir sayı yer almadığı için bunların noktalı şekilde yazılmalarına da olanak yoktur. İşlemin doğru olarak yapılmasını sağlamak için num1 ve num2 değişkenlerinden en az birinin gerçel sayı tipine çevrilmesi gerekir. Bu işleme *tip zorlama* (type casting) adı verilir. Tip zorlama, bir deyimin başına parantez içinde deyimin sonucunun alması istenen tipin adının yazılmasıyla yapılır. Yukarıdaki örneğin doğru çalışması için

```cpp
quotient = (float) num1 / num2;
quotient = num1 / (float) num2;
quotient = (float) num1 / (float) num2;
```

komutlarından herhangi biri kullanılabilir.

```cpp
quotient = (float) (num1 / num2);
```

komutu ise önce bölmeyi sonra tip zorlamasını yapacağından yine quotient değişkenine 3.0 değerini atayacaktır.

Genel olarak, bir işleme giren sayılar farklı tiptense, bunların ortak bir tipe çevrilmeleri gerekir. Dar tipten geniş tipe geçiş işlemleri derleyici tarafından otomatik olarak yapılır. Örneğin, bir toplama işleminin bir operandı tamsayı bir operandı gerçel sayı ise tamsayı olanı gerçel sayıya çevrilir ve toplama yapılır. Geniş tipten dar tipe geçişler ise bilgi yitirilmesine neden olabilirler. Örneğin gerçel sayı tipinden bir değişkenin tamsayı tipinden bir değişkene atanması sırasında sayının kesir kısmı yitirilebilir. Derleyicilerin bu gibi durumlarda hata ya da uyarı üretmeleri zorunlu değildir.

## **2.8.2 İşlemli Atama**

Atamanın sağ tarafındaki deyim, atamanın sol tarafındaki değişken ile bir deyimi içeren bir işlemse, yani

```cpp
değişken = değişken ° deyim;
```

( ° herhangi bir işlem simgesi olabilir) şeklindeyse bu komut

```cpp
değişken °= deyim;
```

şeklinde kısaltılabilir. Örnekler:

```cpp
a += 5; // a = a + 5;
a -= b; // a = a - b;
a *= c + d; // a = a * (c + d);
a /= 2; // a = a / 2;
a %= 4; // a = a % 4;
```

## **2.8.3 Artırma / Azaltma**

Bir değişkenin değeri

```cpp
a = a + 1;
a += 1;
```

gibi komutlarla artırılabilir. Azaltma için de benzer komutlar düşünülebilir. Ancak artırma ve azaltma işlemleri programlarda sıkça gereksinim duyulan işlemlerden olduklarından C'de bunlar için özel işleçler tanımlanmıştır. ++ işleci, önüne ya da arkasına yazıldığı değişkenin değerini 1 artırır; - işleciyse önüne ya da arkasına yazıldığı işlecin değerini 1 azaltır. Her iki işleç de yalnızca tamsayı veri tipleri ile çalışırlar.

Örnekler:

```cpp
a++;
a--;
++a;
--a;
```

Basit kullanımlarında işleçlerin değişkenin önüne mi arkasına mı yazıldıklarının önemi yoktur.8

## **2.8.4 Öncelik Sırası**

C'de deyimlerin hesaplanmasında izlenen öncelik sırası, matematikten alışık olunan sıradır. Yüksek öncelikliden alçak öncelikliye doğru öncelik grupları şöyledir:

Parantez içindeki deyimler

Sayı işareti belirten + ve - işlemleri, artırma, azaltma

Çarpma, bölme, kalan

Toplama, çıkarma

Eşit öncelik grupları kendi içlerinde soldan sağa doğru değerlendirilirler.

**Örnek 1**

| PRIVATE | a+b+c+d+e 5 |  |  |
| --- | --- | --- | --- |

aritmetik deyimi C'de

(a + b + c + d + e) / 5

şeklinde yazılmalıdır. Parantezler kullanılmazsa ortaya çıkan

a + b + c + d + e / 5

C deyimi

| PRIVATEa+b+c+d+ | e 5 |  |  |
| --- | --- | --- | --- |

aritmetik deyimine karşı düşer.

**Örnek 2**

p \* r % q + w / x - y

deyimindeki işleçlerin işleniş sırası \* % / + - şeklindedir.

## **2.9 Değişmezler**

Programda kullanılan bazı bilgiler de programın farklı çalışmaları arasında değer değiştirmezler. Örnekteki PI sayısı ve dairenin çevresinin hesaplanmasında kullanılan 2 sayısı bu tipten büyüklüklerdir. Değişmezlerin bazılarına isim vermek birtakım kolaylıklar sağlar:

Anlaşılırlığı artırır. Programın içinde 3.14 yazmak yerine PI yazmak programı okuyan birinin bu sayının neye karşı düştüğünü daha kolay anlamasını sağlar.

Değiştirmek kolay olur. Diyelim programın geliştirilmesinin ileri aşamalarında 3.14 değerinin yetersiz kaldığına ve 3.141592 değerinin daha uygun olduğuna karar verirsek kod içinde tek bir noktada değiştirmek yeterli olur. Öbür türlü, kodun içindeki bütün 3.14 sayılarının yerine 3.141592 yazmamız gerekir. Daha da kötüsü, kodun içindeki rastlantısal olarak başka 3.14 değerlerinin de geçmesi olasılığıdır. Bu durumda bütün 3.14 değerlerini tek tek inceleyerek değiştirilip değiştirilmeyeceğine karar vermek gerekir.

Değişmezler iki şekilde tanımlanabilirler:

#define bildirimiyle tanımlama. Bu yöntem bir değere mantıksal bir isim vermekte kullanılır. Örnekte yapılan 3.14 sayısına PI adını vermektir. Bu bildirimin sonucu, programcının kod içinde PI geçen her yere kendisi 3.14 değerini yazmış olmasıyla aynıdır. Bu şekilde tanıtılan değişkenlere gelenek olarak tamamı büyük harflerden oluşan adlar verilir.

Bu bildirim yönteminde değişmezlerin tipleri ayrıca belirtilmez. Tamsayı değişmezler int tipine sığmıyorlarsa long int varsayılırlar. Değerlerinin sonuna l ya da L harfleri eklenirse long, u ya da U eklenirse unsigned niteleyicileri seçilmiş olur.

```cpp
#define MAXSHORT 0x7FFF
#define MAXUSHORT 65535U
```

Gerçel değişmezlerin değerlerinin sonuna f ya da F eklenmemişse double tipinden oldukları varsayılır. l ya da L eklenirse long double tipinden olurlar.

```cpp
#define EULER 2.81782F
#define PERCENT 1E-2
```

Değişken bildirimine benzer şekilde ancak bildirim sırasında veri tipinin önüne const niteleyicisi koyarak tanımlama. Böylece değeri değiştirilemeyen bir değişken tanımlanmış olur. Bu şekilde tanımlanan değişmezlere büyük harflerden oluşan adlar verilmez. Örnekteki PI değişmezinin bu yöntemle tanımı şöyle olurdu:

```cpp
const float pi = 3.14;
```

Her iki tanımda da değişmez olarak bildirilmiş bir büyüklüğe değer atanmaya çalışırsa derleyici hata verir9.

## **2.10 Makrolar**

Programın içinde sıkça yinelenmesi gerekebilecek küçük kod parçaları makrolar yardımıyla gerçeklenebilir. Örnekte kare alma işlemini yapmak üzere bir makro yazılmıştır. Makrolar da değişmez tanımlarına benzer şekilde #define sözcüğüyle yapılırlar. İşleyişleri de yine değişmez tanımlarına benzer şekilde olur, yani makronun adının geçtiği yere açılımı konur. Örnekteki

```cpp
area = PI * sqr(radius);
```

komutu görülünce makro tanımında x yerine radius sözcüğü konarak kod

```cpp
area = PI * ((radius) * (radius));
```

şekline getirilir (programcı kendisi bu şekilde yazmış gibi).

Bu işlem bir sözcük ya da sözcük grubunun yerine başka bir sözcük ya da sözcük grubunun yerleştirilmesi şeklinde yürüdüğünden kullanımına dikkat etmek gerekir. Örnekteki makro

```cpp
#define sqr(x) x * x
```

şeklinde tanımlansa ve programda

sqr(radius + 1)

şeklinde kullanılsaydı yerine geçecek (yanlış) kod şu şekilde olurdu:

radius + 1 \* radius + 1

## **Sorular**

Çalıştığınız geliştirme ortamında int tabanlı veri tiplerinin değer aralıklarını belirleyin ve bu aralıklar dışında bir değer atandığında nasıl bir sonuç elde edildiğini gözleyin.

Aşağıdaki deyimlerin sonuçlarını bulun:

8 + 17 % 3 \* 5

45 / (4 + 7) - 5.0 / 2

Aşağıdaki aritmetik deyimleri gerçekleyen C deyimlerini yazın:

| PRIVATEk← | PRIVATE1 2ab | −cd | ef−g h |  |  |
| --- | --- | --- | --- | --- | --- |
| x(y+z) |  |  |  |  |  |

Aşağıdaki C deyimlerinin gerçeklediği aritmetik deyimleri yazın:

```cpp
a + 3 * b - (c + d) / 2 * y;
```

Kullanıcının Fahrenheit biriminde verdiği bir sıcaklık değerini aşağıdaki formüle göre Celcius birimine çevirerek, bu sıcaklıkta suyun halini (0'dan küçük ise katı, 100'den büyük ise gaz, diğer durumlarda sıvı) ekrana çıkartan bir program yazın.

| PRIVATEC= | 5 9 | (F−32) |  |
| --- | --- | --- | --- |

İkinci dereceden ( ax2+bx+c=0 şeklinde) bir denklemin köklerinin yerleri belirlenmek isteniyor. Diskriminantın

| PRIVATE | √ | b2−4ac |  |
| --- | --- | --- | --- |

şeklinde tanımlandığını ve köklerin

| PRIVATEx1,2= | PRIVATE−b± | √ | b2−4ac |  |  |
| --- | --- | --- | --- | --- | --- |
| 2a |  |  |  |  |  |

formülüne göre hesaplanacağını gözönünde bulundurarak, denklemin katsayılarını kullanıcıdan aldıktan sonra aşağıdaki işlemleri gerçekleştiren bir program yazın. (Not: Kök alma işlemi için sqrt kitaplık fonksiyonunu kullanabilirsiniz.)

Denklemin iki farklı gerçel kökü varsa (diskriminant pozitif ise) bunlar hesaplanarak ekrana çıkartılacaktır.

Denklemin kökleri çakışıksa (diskriminant 0 ise) bu durumu kök değeriyle birlikte kullanıcıya bildirecektir.

Denklemin gerçel kökü yoksa (diskriminant negatif ise) bu durum kullanıcıya bildirilecektir.

**Chapter 3
Akış Denetimi**

## **Örnek**

Bu bölümde üzerinde çalışılacak program, kullanıcının verdiği sayı kadar yazı tura atarak yazı ve turaların kaçar kere geldiğini sayar ve sonuçları ekrana çıkartır. Bu programa ilişkin akış çizeneği Şekil 3.1'de, kod Örnek 3'de verilmiştir.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS,srand,rand,RAND_MAX
#include <time.h> // time
int main(void)
{
int count, i;
float number;
int heads = 0, tails = 0;
cout << "Kaç kez atılacak? "; cin >> count;
srand(time(NULL));
for (i = 1; i <= count; i++)
{
number = (float) rand() / RAND_MAX;
if (number < 0.5)
{
cout << "Yazı" << endl;
tails++;
}
else
{
cout << "Tura" << endl;
heads++;
}
}
cout << " Yazı sayısı: " << tails
<< ", Yüzdesi: %" << 100.0 * tails / count << endl;
cout << " Tura sayısı: " << heads
<< ", Yüzdesi: %" << 100.0 * heads / count << endl;
return EXIT_SUCCESS;
}
```

#1 Yinelemeli yazı-tura atışı simülasyonu yapan program.

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=random.png" |  |
| --- | --- | --- |

Şekil 3.1: Yinelemeli yazı-tura atışının simülasyonu.

## **3.1 Rastgele Sayılar**

Yazı-tura atışını simüle etmek için en kolay yol 0 ile 1 arasında bir rastgele sayı üretmek ve bu sayının 0.5'den küçük olması durumunu bir sonuca (diyelim tura), eşit ya da büyük olmasını da diğer sonuca (bu durumda yazı) atamaktır.

C standart kitaplığındaki rand fonksiyonu 0 ile RAND\_MAX arasında bir rastgele tamsayı üretir. RAND\_MAX standart kitaplıkta tanımlanmış bir değerdir ve sistemden sisteme farklılık gösterebilir. rand fonksiyonundan gelen sayı RAND\_MAX değerine bölünürse 0 ile 1 arasında bir rastgele gerçel sayı elde edilir.

Rastgele sayıların kullanımında daha çok 1 ile bir üst sınır arasında değer alacak bir rastgele tamsayıya gereksinim duyulur. Bu üst sınır max ile gösterilirse

1 + rand() % max

deyimi istenen türden bir sayı üretir (Neden?).

Rastgele sayılar, bir seri olarak üretilirler; yani her rastgele sayı seride bir önceki rastgele sayıdan üretilir. Bu serinin başlayabilmesi için ilk sayıyı üretmekte kullanılacak bir başlangıç değeri (*tohum*) verilmesi gerekir. srand fonksiyonu bu tohumun belirtilmesini sağlar. Aynı tohumla başlanırsa aynı seri üretilir. Her serinin programın çalışmasındaki bir senaryoya karşılık düştüğü düşünülürse istendiği zaman aynı senaryoyu üretebilmek programın hatalarının ayıklanması açısından yararlıdır.

Her defasında farklı bir tohumla başlamak için tohumun da her defasında farklı verilmesi gerekir. Standart kitaplıktaki time fonksiyonu, 1 Ocak 1970 tarihinden o ana kadar geçen saniyelerin sayısını verdiğinden her çağrılışında farklı bir tohum üretebilir. Bu fonksiyona NULL giriş parametresini göndermek yeterlidir.

## **3.2 Koşul Deyimleri**

Yapısal programlamadaki seçim ve yineleme yapılarında bir koşula göre bir karar verilmesini sağlayan yapılar gerektiği görülmüştü (bkz. Bölüm 1.1). Koşullar, koşul deyimleriyle gösterilirler. C dilinde bir koşul deyimi, iki sayısal büyüklüğün (aritmetik deyimin) karşılaştırılması ile oluşturulur ve mantıksal bir değer (doğru ya da yanlış) üretir. Örnekteki

number < 0.5

deyimi bir koşul deyimidir ve number değişkeninin o anki değerine göre doğru ya da yanlış değerini alır.10

## **3.2.1 Karşılaştırma İşlemleri**

İki sayı değeri arasında şu karşılaştırma işlemleri yapılabilir:

Eşitlik: == işleciyle gerçeklenir. İşlecin solundaki değerle sağındaki değer aynıysa doğru, farklıysa yanlış sonucunu üretir.

Farklılık: != işleciyle gerçeklenir. Eşitlik karşılaştırmasının tersidir. İşlecin solundaki değerle sağındaki değer farklıysa doğru, aynıysa yanlış sonucunu üretir.

Küçüklük: < işleciyle gerçeklenir. İşlecin solundaki değer sağındaki değerden küçükse doğru, küçük değilse yanlış sonucunu üretir.

Büyüklük: > işleciyle gerçeklenir. İşlecin solundaki değer sağındaki değerden büyükse doğru, büyük değilse yanlış sonucunu üretir.

Küçüklük veya eşitlik: <= işleciyle gerçeklenir. Büyüklük karşılaştırmasının tersidir. İşlecin solundaki değer sağındaki değerden küçük veya eşitse doğru, büyükse yanlış sonucunu üretir.

Büyüklük veya eşitlik: >= işleciyle gerçeklenir. Küçüklük karşılaştırmasının tersidir. İşlecin solundaki değer sağındaki değerden büyük veya eşitse doğru, küçükse yanlış sonucunu üretir.

**Örnekler ******

Yıl 4'e kalansız bölünebiliyor mu?

(year % 4) == 0

Yaş 18'den büyük ya da eşit mi?

age >= 18

## **3.2.2 Mantıksal İşlemler**

Bazı durumlarda tek bir karşılaştırma işlemi bütün koşul deyimini oluşturmak için yeterli değildir. Örneğin bir insanın yaşının 18 ile 65 arasında olup olmadığını sınamak istiyorsanız, bunu tek bir karşılaştırma işlemiyle yapamazsınız. Böyle durumlarda, karşılaştırma işlemleri mantıksal işlemlerle bağlanarak karmaşık koşul deyimleri üretilebilir. Üç tane mantıksal işlem vardır:

DEĞİL işlemi: ! işleciyle gerçeklenir. Önüne yazıldığı koşul deyimini değiller, yani doğruysa yanlış, yanlışsa doğru değerini üretir (bkz. Tablo 3.1).

| PRIVATEcond!(cond) |  |
| --- | --- |
| doğru | yanlış |
| yanlış | doğru |

Tablo 3.1: Değil işlemi doğruluk tablosu.

**Örnek**

Yaş 18'den küçük değil:

!(age < 18)

VE işlemi: && işleciyle gerçeklenir. Bağladığı koşulların hepsi doğruysa doğru, en az biri yanlışsa yanlış değerini üretir (bkz. Tablo 3.2).

| PRIVATEcond1cond2(cond1) && (cond2) |  |  |
| --- | --- | --- |
| doğru | doğru | doğru |
| doğru | yanlış | yanlış |
| yanlış | doğru | yanlış |
| yanlış | yanlış | yanlış |

Tablo 3.2: VE işleminin doğruluk tablosu.

**Örnek**

Yaş 18'den büyük veya eşit ve 65'den küçük veya eşit:

(age >= 18) && (age <= 65)

VEYA işlemi: || işleciyle gerçeklenir. Bağladığı koşulların hepsi yanlışsa yanlış, en az biri doğruysa doğru değerini üretir(bkz. Tablo 3.3).

| PRIVATEcond1cond2(cond1) \|\| (cond2) |  |  |
| --- | --- | --- |
| doğru | doğru | doğru |
| doğru | yanlış | doğru |
| yanlış | doğru | doğru |
| yanlış | yanlış | yanlış |

Tablo 3.3: VEYA işleminin doğruluk tablosu.

**Örnek**

Yaş 18'den küçük veya 65'den büyük:

(age < 18) || (age > 65)

**Örnek**

Bir yılın artık yıl olup olmadığını belirleyen koşul deyimi. Sonu 00 ile biten yıllar dışındaki yıllar 4 sayısına kalansız bölünüyorlarsa artık yıl olurlar. Sonu 00 ile bitenler ise 400 sayısına kalansız bölünüyorlarsa artık yıldırlar. Bunların dışında kalan yıllar artık yıl değildir. Sözgelimi, 1996, 2000, 2004 ve 2400 yılları artık yıldır ama 1997, 2001, 1900 ve 2100 yılları artık yıl değildir.

((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)

Parantezler kullanılmadığında mantıksal işleçlerin öncelikleri yüksek öncelikliden başlayarak DEĞİL, VE, VEYA sırasıyladır. Buna göre yukarıdaki örnek

(year % 4 == 0) && !(year % 100 == 0) || (year % 400 == 0)

ya da

(year % 400 == 0) || (year % 4 == 0) && !(year % 100 == 0)

biçiminde de yazılabilirdi.

## **3.3 Seçim**

if/else yapısı, bir koşulun sağlanıp sağlanmamasına göre iki bloktan hangisinin yürütüleceğine karar verir. Örnekteki

```cpp
if (number < 0.5)
{
cout < < ``Yazı'' < < endl;
tails++;
}
else
{
cout < < ``Tura'' < < endl;
heads++;
}
```

yapısında number değişkeninin değeri 0.5'den küçükse yazı geldiğine karar verilir ve tails değişkeninin, 0.5'e eşit ya da daha büyükse tura geldiğine karar verilir heads değişkeninin değeri 1 artırılacaktır.

Bir blok tek bir komuttan oluşuyorsa bloğun süslü parantezler ile sınırlanması zorunlu değildir11. Örnekte yazı mı tura mı geldiğinin her seferinde bildirilmesi istenmiyor ve yalnızca sayılarının bulunması isteniyor olsaydı if / else yapısı şöyle olurdu:

```cpp
if (number < 0.5)
{
tails++;
}
else
{
heads++;
}
```

Bu yapı, süslü parantezler kullanılmayarak şu şekilde de yazılabilirdi:

```cpp
if (number < 0.5)
tails++;
else
heads++;
```

Gelenek olarak tek komutlu bloklarda süslü parantezler kullanılmaz, yani yukarıdaki örneklerin ikinci yazılış şekline uyulur.

Her if yapısında bir else bloğu bulunması zorunlu değildir. Bu şekliyle kullanımda if, bir koşulun sağlanıp sağlanmamasına göre bir bloğun yürütülüp yürütülmeyeceğine karar verir. Yine her atışın sonucunun tek tek bildirilmediği durum gözönüne alınırsa yazı ve turaları ayrı ayrı saymaya gerek olmayacağı, birini saymanın yeteceği görülebilir. O halde program şu şekilde değiştirilebilir:

```cpp
for (i = 1; i <= count; i++)
{
number = (float) rand() / RAND_MAX;
if (number < 0.5)
tails++;
}
heads = count - tails;
```

Döngü içindeki if yapısında koşul sağlanıyorsa tails değişkeninin değeri artırılır, sağlanmıyorsa hiçbir şey yapılmaz.

## **3.4 Sayaç Denetiminde Yineleme**

Örnekte yazı-tura simülasyonunun kullanıcının belirteceği sayıda yinelenmesi isteniyor. Bir bloğun belli sayıda yinelenmesi istendiğinde kullanılabilecek en uygun yapı for yapısıdır. Bir sayacın denetiminde yineleme yapmak için şunların belirtilmesi gerekir:

Sayacın başlangıç değeri: Örnekte bu değer 1'dir.

Kaça kadar sayılacağı: Örnekte bu değer kullanıcıdan alınan sayının tutulduğu count değişkeniyle belirlenir.

Kaçar kaçar sayılacağı: Örnekte sayacın birer birer artırılacağı belirtilmiştir.

for yapısı bu üç belirtimin aynı anda yapılmasına olanak sağlar. Parantez içinde önce başlangıç değeri ataması, ikinci olarak hangi koşul sağlandığı sürece devam edileceği ve son olarak da sayacın nasıl artırılacağı belirtilir.

```cpp
for (i = 1; i <= count; i++)
```

komutu şöyle okunabilir:

i değişkenine 1 değerini ver ve bu değişkenin değeri count değişkeninin değerinden küçük veya eşit olduğu sürece bloğu her yürütüşünden sonra i değişkeninin değerini 1 artır.

Bu yapıyla ilgili olarak bazı noktalara dikkat etmek gerekir:

Döngü, belirtilen koşul sağlanmadığı zaman sonlanır ve programın yürütülmesi döngünün arkasından gelen komutla sürdürülür. Örnekte i değişkeninin değeri count değişkeninin değerinden büyük olduğu zaman döngü sona erer.

Artırma işlemi döngü gövdesi yürütüldükten sonra yapılır. Örnekte döngünün gövdesi i değişkeninin 1, 2, ..., count değerleri için yinelenir, 1 değeri atlanmaz.

Verilen başlangıç değeri döngü koşulunu sağlamıyorsa döngünün gövdesi hiç yürütülmez. Örneğin

```cpp
for (i = 1; i == 10; i++)
```

döngüsünde başlangıç değeri sürme koşulunu sağlamadığından (1 == 10 olmadığından) döngüye hiç girilmez.

Artım miktarı için artırma işleci kullanılması zorunlu değildir, herhangi bir C deyimi kullanılabilir.

```cpp
for (i = 1; i < count; i += 3)
```

döngüsü 1, 4, 7, 10, 13, ... şeklinde sayarken

```cpp
for (i = 1; i < count; i *= 2)
```

döngüsü 1, 2, 4, 8, 16, ... şeklinde sayar.

## **Örnek**

Bu bölümde üzerinde çalışılacak program (Örnek 4), operandlarını ve operatörünü kullanıcının belirttiği işlemi yaparak sonucu ekrana yazar.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS,exit
int main(void)
{
int num1, num2, result;
char op;
cout << "İşlemi yazın: "; cin >> num1 >> op >> num2;
switch (op)
{
case '+': result = num1 + num2;
break;
case '-': result = num1 - num2;
break;
case '*': result = num1 * num2;
break;
case '/': result = num1 / num2;
break;
case '%': result = num1 % num2;
break;
default: cout << "Böyle bir işlem yok." << endl;
exit(EXIT_FAILURE);
}
cout << num1 << op << num2
<< " işleminin sonucu: " << result << endl;
return EXIT_SUCCESS;
}
```

#1 Kullanıcının belirttiği işlemi yapan program.

## **3.5 Çoklu Karşılaştırma**

Bir deyimin çok sayıda değer içinden hangisini almış olduğunu sınamak istiyorsak yazacağımız if kodu uzun ve çirkin bir görünüm alacaktır. Örneğimizde yapılacak işlemin hangisi olduğunu anlamak için yazılacak if kodu şu tip bir şey olurdu:

```cpp
if (op == '+')
```

...

```cpp
else
{
if (op == '-')
```

...

```cpp
else
{
if (op == '*')
```

...

switch komutu bu tip karşılaştırmalar için daha düzgün bir yapı sunar. Bu komutun akış çizeneği Şekil 3.2'de görüldüğü gibidir. Önce birinci karşılaştırma yapılır ve koşul doğru sonucunu üretirse buna ilişkin blok yürütülür ve break komutuyla switch yapısının dışına çıkılır. Birinci karşılaştırma yanlış sonucunu üretirse ikinci karşılaştırma denenir. Herhangi bir karşılaştırma doğru sonucunu ürettiğinde yapıdan çıkılır. Karşılaştırmaların hiçbiri doğru değilse default bloğu yürütülür ve switch sona erer. Her switch yapısında bir default bloğu bulunması zorunlu değildir.

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=switch1.png" |  |
| --- | --- | --- |

Şekil 3.2: switch komutunun akış çizeneği.

C programlarında sıkça yapılan hatalardan biri bloklardaki break komutlarının unutulmasıdır. Böyle bir durumda switch komutu Şekil 3.3'de görüldüğü gibi çalışır. Örnekte birinci bloğun sonuna konması gereken break komutu yoktur. Bu durumda birinci karşılaştırma işlemi başarısız olursa bir sorun çıkmayacak ama başarılı olursa block 1 yürütüldükten sonra block 2 de yürütülecektir ve break ile switch sonlanacaktır. Yani, başarılı olan ilk karşılaştırmadan başlanarak break komutu görülene kadar gelen bütün bloklar yürütülecektir.12

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=switch2.png" |  |
| --- | --- | --- |

Şekil 3.3: switch komutunda break kullanılmazsa oluşan akış çizeneği.

Örnek programda break komutları yazılmazsa işlemin toplama olduğu durumda önce toplama, sonra çıkartma, sonra çarpma ve son olarak da bölme yapılacak (yani yalnızca bölme işlemi geçerli olacak), ayrıca da \`\`Böyle bir işlem yok.'' denilerek herhangi bir sonuç görüntülenmeden programdan çıkılacaktır. İşlem çıkartma olduğunda toplama kısmı atlanacak, gerisi deminki gibi devam edecektir.

## **Örnek**

Bu bölümde iki sayının en büyük ortak bölenini Euclid algoritmasını kullanarak bulan bir program yazılacaktır. Bu algoritmaya ilişkin akış çizeneği Şekil 3.4'de, bu akış çizeneğini gerçekleyen program Örnek 5'de verilmiştir.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS
int main(void)
{
int num1, num2, tmp;
cout << "Sayıları yazın: "; cin >> num1 >> num2;
while (num1 > 0)
{
if (num1 < num2)
{
tmp = num1;
num1 = num2;
num2 = tmp;
}
num1 = num1 - num2;
}
cout << "En büyük ortak bölen: " << num2 << endl;
return EXIT_SUCCESS;
}
```

#1 İki sayının en büyük ortak bölenini bulan program.

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=gcd.png" |  |
| --- | --- | --- |

Şekil 3.4: İki sayının en büyük ortak bölenini hesaplayan program.

## **3.6 Koşul Denetiminde Yineleme**

Örnekte programda döngünün kaç kere yineleneceği belli değildir; bir koşul sağlandığı sürece yinelenmesi istenmektedir. Böyle durumlarda while yapısı kullanılır. Örnekteki while bloğu num1 değişkeninin değeri pozitif olduğu sürece yinelenecek, sıfıra eşit ya da negatif olduğu zaman sona erecektir.

```cpp
for döngüleri while döngüleri şeklinde de yazılabilirler:
for (başlangıç ataması; sürme koşulu; artırma komutu)
{
blok;
}
```

döngüsü

```cpp
başlangıç ataması;
while (sürme koşulu)
{
blok;
artırma komutu;
}
```

döngüsüne eşdeğerlidir. Yine de sayaç denetiminde yinelemeler için for, koşul denetiminde yinelemeler için while kullanmak anlaşılırlık açısından daha iyidir.

## **Örnek**

Bu bölümdeki programda (Örnek 6), giriş bölümünde anlatılan ikinci algoritma kullanılarak iki sayının en küçük ortak katı bulunacaktır.

```cpp
#include <iostream.h> // oout,cin
#include <stdlib.h> // EXIT_SUCCESS
int main(void)
{
int number1, number2;
int max, min, i;
long int lcm;
cout << "1. Sayı: "; cin >> number1;
cout << "2. Sayı: "; cin >> number2;
max = number1 > number2 ? number1 : number2;
min = number1 < number2 ? number1 : number2;
for (i = 1; (max * i) % min != 0; i++)
;
lcm = max * i;
cout << "En küçük ortak kat: " << lcm << endl;
return EXIT_SUCCESS;
}
```

#1 İki sayının en küçük ortak katını bulan program.

## **3.7 Koşullu İşleç**

Koşullu işleç, bir koşulun gerçekleşip gerçekleşmemesine göre iki deyimden birini seçer.

*deyim1* ? *deyim2* : *deyim3*

Burada öncelikle deyim1 değerlendirilir. Sonuç doğruysa deyim2, yanlışsa deyim3 seçilir. Örnekteki

```cpp
max = (number1 > number2) ? number1 : number2;
```

komutu şu şekilde yorumlanabilir:

```cpp
if (number1 > number2)
max = number1;
else
max = number2;
```

## **3.8 Boş Döngüler**

Bazı durumlarda bir döngünün bloğu boş olabilir, yani herhangi bir komut içermeyebilir. Örnekte, en küçük ortak katı bulunacak iki sayıdan büyük olanın katları taranarak bunların herhangi birinin küçük olan sayıya da bölünüp bölünmediğini sınayan for döngüsünün bloğu boştur çünkü bu döngüde döngü sayacını artırmaktan başka yapılacak işlem yoktur. Aynı döngü while ile şu şekilde yazılabilirdi:

```cpp
i = 1;
while ((max * i) % min != 0)
i++;
```

## **Örnek**

Bu bölümdeki programda (Örnek 7), ex fonksiyonun hesaplanması için aşağıdaki seri toplamından yararlanılacaktır:

```cpp
PRIVATEf(x)=∞
∑
i=0
xi
```

i!
=1+x+x2

2!
+x3

3!
+x4

4!
+…Bu programda içiçe iki döngü bulunacak ve bu döngülerden biri uygun koşul sağlandığında çıkılan bir sonsuz döngü şeklinde gerçeklenecektir. Dış döngünün her yinelenişinde serinin o anki terimi hesaplanarak toplama eklenecektir. Hesaplanan terim kullanıcının belirttiği hatadan küçük olduğunda değerin istenen duyarlılıkta hesaplandığına karar verilerek sonuç ekrana çıkartılacaktır.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS
#include <math.h> // pow
int main(void)
{
float x, error, term, result = 1.0;
int i = 1, f;
float fact;
cout << "x: "; cin >> x;
cout << "Hata: "; cin >> error;
while (true)
{
fact = 1.0;
for (f = 2; f <= i; f++)
fact *= f;
term = pow(x, i) / fact;
result += term;
if (term < error)
break;
i++;
}
cout << "Sonuç: " << result << endl;
return EXIT_SUCCESS;
}
```

#1 ex\\protect deyimini genel terimden giderek hesaplayan program.

## **3.9 Sonsuz Döngüler**

Örnekte görüldüğü gibi, dış döngü

```cpp
while (true)
```

şeklinde başlamaktadır. Bu yapıda koşul doğru olduğu sürece blok yineleneceğinden ve koşul her zaman doğru olduğundan bu bir sonsuz döngüdür, yani blok içinde önlem alınmazsa döngü sonlanmaz.

Döngünün sonlanması için blok içinde bloktan çıkılması için gerekli koşul uygun noktalarda sınanır ve sağlandığı zaman break komutuyla döngünün dışına çıkılır. Örnekte hesaplanan terim kullanıcının belirttiği hata değerinden küçük olduğunda döngüden çıkılması istenmektedir.

## **3.10 İçiçe Döngüler**

## **Sorular**

Aşağıdaki seri toplamı hesaplanmak isteniyor:

```cpp
PRIVATEn
∑
i=0
(−1)ixi
```

(2i)!
=x0

0!
−x1

2!
+x2

4!
−x3

6!
+x4

8!
−x5

10!
+…Bu serinin i . elemanı ai ise, ai+1/ai oranı nedir?

Bu bilgiyi kullanarak, serinin toplamını hesaplayan bir program yazın. x ve n sayıları kullanıcıdan alınacaktır.

**Chapter 4
Diziler**

## **Örnek**

Bu bölümde üzerinde çalışılacak program (Örnek 8), kullanıcıdan aldığı sayı kadar öğrencisi bulunan bir sınıfta yine kullanıcıdan aldığı öğrenci notlarının ortalamasını, varyansını ve standart sapmasını hesaplar. Öğrenci sayısı n , i . öğrencinin notu gi , ortalama m , varyans v , standart sapma s ile gösterilirse:

| PRIVATEm | PRIVATE= | PRIVATE | PRIVATEn ∑ i=1 | gi |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| n |  |  |  |  |  |  |  |
| PRIVATEv | PRIVATE= | PRIVATE | n ∑ i=1 | (gi−m)2 |  |  |  |
| PRIVATEs | PRIVATE= | PRIVATE | √v n−1 |  |  |  |  |

Yalnızca ortalama hesaplanacak olsaydı tek bir döngü kullanmak yeterli olurdu. Döngünün her bir yinelenişinde kullanıcıdan sıradaki öğrencinin notu alınır ve o ana kadarki toplama eklenirdi. Döngü sona erdiğinde bulunan toplam, eleman sayısına bölünerek ortalama elde edilirdi. Ancak varyansın hesaplanabilmesi için her bir notun ortalamayla farkına gereksinim vardır. Ortalama ise ancak birinci döngünün sonunda elde edilebildiğinden varyansı hesaplamak için ikinci bir döngü gerekir. Ayrıca bu ikinci döngüde yine öğrenci notlarına gereksinim olduğundan kullanıcının girmiş olduğu notlar da unutulmamalıdır.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS
#include <math.h> // sqrt
#define MAXSTUDENTS 100
#define sqr(x) ((x) * (x))
int main(void)
{
int grades[MAXSTUDENTS];
int nstudents, i;
float mean, variance = 0.0, deviation;
int total = 0;
cout << "Öğrenci sayısı: "; cin >> nstudents;
for (i = 0; i < nstudents; i++)
{
cout << i + 1 << ". öğrencinin notu: "; cin >> grades[i];
total += grades[i];
}
mean = (float) total / nstudents;
for (i = 0; i < nstudents; i++)
variance += sqr(grades[i] - mean);
deviation = sqrt(variance / (nstudents - 1));
cout << "Ortalama: " << mean << endl;
cout << "Varyans: " << variance << endl;
cout << "Standart Sapma: " << deviation << endl;
return EXIT_SUCCESS;
}
```

#1 Ortalama, varyans ve standart sapma hesaplayan program.

## **4.1 Tek Boyutlu Diziler**

Aynı tipten ve birbirleriyle ilişkili değerler bir dizi altında birleştirilebilirler. Örneğimizde öğrenci notları bir dizi olarak temsil edilmeye uygundur. C dilinde diziler -birden çok eleman içerseler de- tek bir değişken olarak değerlendirilirler; yani grades değişkeni sınıftaki bütün öğrenci notlarının tutulduğu tek bir değişkendir.

Diğer değişkenlerde olduğu gibi, dizilerin de kullanılmadan önce tanımlanmaları gerekir. Dizi tanımında dizinin eleman tipi, adı ve boyu belirtilir. Örnekte

```cpp
int grades[MAXSTUDENTS];
```

tanımı, her biri tamsayı tipinden MAXSTUDENTS elemanlı ve grades adında bir dizi tanımlar. Bu dizi için bellekte MAXSTUDENTS \* sizeof(int) kadar yer ayrılır.

Yine diğer değişkenlerde olduğu gibi, dizilere de tanım sırasında başlangıç değeri verilebilir. Örneğin:

```cpp
int grades[4] = { 85, 73, 91, 66 };
```

tanımı 4 elemanlı bir dizi tanımlar ve elemanlara sırasıyla 85, 73, 91 ve 66 değerlerini verir. Özel bir durum olarak, bütün diziye 0 başlangıç değeri verilmek isteniyorsa şu komut kullanılabilir:

```cpp
int grades[50] = { 0 };
```

Diziye başlangıç değeri verilirse eleman sayısını belirtmek zorunluluğu yoktur, yani

```cpp
int grades[] = { 85, 73, 91, 66 };
```

tanımı da yukarıdakiyle aynı işi yapar. Bu durumda derleyici başlangıç değeri olarak verilen dizideki eleman sayısını sayarak boyu kendisi belirler.

Derleyicinin dizi için bellekte ne kadar yer ayrılacağını bilmesi gerektiğinden dizi tanımında boy olarak sabit bir değer vermek zorunludur. Örnekte sınıftaki öğrenci sayısı nstudents değişkeniyle gösterilmektedir, yani dizinin nstudents elemanı olması gerekli ve yeterlidir. Ancak nstudents değişkeninin değerinin ne olacağını programın çalışması sırasında kullanıcı belirlediğinden derleyici bu değeri dizi boyu olarak kullanamaz, yani

```cpp
int grades[nstudents];
```

şeklinde bir dizi tanımı yapamaz. Başka bir deyişle, dizi boyu için yazılacak deyimde yalnızca sayılar ve değişmezler yer alabilir, değişkenler yer alamaz. Bu durumda, dizinin kaç elemanı olacağı baştan bilinmiyorsa gerekebilecek en büyük eleman sayısı boy olarak belirtilmelidir. Örnekteki MAXSTUDENTS değişmezi bu işlevi görmektedir. Burada belirtilen sayı, bir yandan gereksiz bellek kullanımına yol açabilir, diğer yandan da programın bir kısıtlaması haline gelir. Örnek programın yaptığı işin açıklamasını şu şekilde düzeltmek gerekir:

Bu program, en fazla 100 öğrencili bir sınıfta, öğrenci notlarının ortalamasını, varyansını ve standart sapmasını hesaplar.

Dizi her ne kadar bir elemanlar topluluğu olsa da işlem yapılacağı zaman dizinin bir elemanına erişmek gerekecektir. Bir dizinin bir elemanı üzerinde işlem yapmak için o elemanın kaçıncı eleman olduğunu belirtmek gerekir. C dilinde dizilerin ilk elemanının sıra numarası 0 olarak belirlenir; yani ilk elemanın sıra numarası 0, ikinci elemanın sıra numarası 1 şeklinde ilerler. Bu durumda n elemanlı bir dizinin son elemanının sıra numarası n−1 olur. Bu özellik nedeniyle n elemanlı bir dizi üzerinde işlem yapacak tipik bir C döngüsü

```cpp
for (i = 0; i < n; i++)
```

şeklinde başlar. İlk elemanın sıra numarası 0 olduğundan for bloğuna ilk girişte dizinin ilk elemanı ile işlem yapılır. Son işlem de n−1 sıra numaralı elemanla yapılacak, döngü sayacı n değerini alır almaz döngüden çıkılacaktır.

Derleyici dizilerin elemanlarına erişimde dizi sınırlarının denetimini yapmaz; yani n elemanlı bir dizinin n. ya da daha sonraki elemanlarına erişilmeye kalkılırsa bir hata vermez. Böyle bir erişim yapıldığında ilk elemandan başlanarak n eleman kadar ilerleyip orada ne değer bulunursa o değerle işlem yapılmaya çalışılır. Erişilmek istenen bellek bölgesi kullanıcının izni olan bölgeler dışında bir yere düşerse çalışma anında bir *bellek hatası* oluşur. Dizi sınırlarından taşmamak programcının sorumluluğundadır.

## **Örnek**

Bu bölümde üzerinde çalışılacak program (Örnek 9), boyutları ve elemanları kullanıcıdan alınan iki matrisi çarparak sonucu ekrana çıkartır. Bu örnekte, çok boyutlu diziler üzerinde nasıl işlem yapılacağı üzerinde durulacaktır.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS
int main(void)
{
int m1[30][20];
int m2[20][30];
int pr[30][30] = { 0 };
int r1, c1, c2;
int &r2 = c1;
int i, j, k;
cout << "Sol matrisin satır sayısı: "; cin >> r1;
cout << "Sol matrisin sütun sayısı: "; cin >> c1;
cout << "Sağ matrisin sütun sayısı: "; cin >> c2;
cout << "Sol matris: " << endl;
for (i = 0; i < r1; i++)
for (j = 0; j < c1; j++)
{
cout << " [" << i + 1 << "," << j + 1<< "]: ";
cin >> m1[i][j];
}
cout << "Sağ matris: " << endl;
for (j = 0; j < r2; j++)
for (k = 0; k < c2; k++)
{
cout << " [" << j + 1 << "," << k + 1 << "]: ";
cin >> m2[j][k];
}
for (i = 0; i < r1; i++)
for (j = 0; j < c2; j++)
for (k = 0; k < c1; k++)
pr[i][j] += m1[i][k] * m2[k][j];
cout << "Sonuç:" << endl;
for (i = 0; i < r1; i++)
{
for (k = 0; k < c2; k++)
cout << " " << pr[i][k] << " ";
cout << endl;
}
return EXIT_SUCCESS;
}
```

#1 İki matrisi çarpan program.

## **4.2 Çok Boyutlu Diziler**

Çok boyutlu bir dizi tanımlanmasında her boyut ayrı bir köşeli parantez çifti içinde belirtilir. Örnekteki

```cpp
int m1[30][20];
```

komutu, 30 satırlı ve 20 sütunlu bir matris tanımlar. Bu matrisin, her biri birer tamsayı olan, 30\*20=600 elemanı olacaktır, yani bellekte 600 tamsayı tutacak kadar yer ayrılmasına neden olur. Daha çok boyutu olan bir dizi tanımlanmak istenseydi boyutlar yanyana sürdürülebilirdi:

```cpp
int n[30][20][7][12];
```

Bu işlem sonucunda da bellekte 30\*20\*7\*12=50400 tamsayı tutacak kadar yer ayrılır.

Tek boyutlu dizilerde olduğu gibi, çok boyutlu dizilerde de başlangıç değeri verilebilir. Bunun için her bir boyutun kendi içinde süslü parantezler içine alınması gerekir:

```cpp
int p[2][3] = { { 1, 2, 1 }, { 3, 5, 1 } };
```

tanımı

| PRIVATEp= | ⎡ ⎢ ⎣ | PRIVATE1 | PRIVATE2 | PRIVATE1 | ⎤ ⎥ ⎦ |  |
| --- | --- | --- | --- | --- | --- | --- |
| PRIVATE3 | PRIVATE5 | PRIVATE1 |  |  |  |  |

matrisini oluşturur. Tek boyutlu dizilerdekine benzer şekilde { 0 } başlangıç değeri bütün elemanlara 0 başlangıç değerini atar.

## **4.3 Başvurular**

Başvurular, aynı değişkene ikinci bir isim verilmesini sağlarlar. Örnekte sol matrisin satır sayısı ile sağ matrisin sütun sayılarının aynı olması zorunluluğu nedeniyle bu bilgiyi tek bir değişkenle temsil etmek yeterli görülmüş ve c1 değişkeni tanımlanmıştır. Ancak döngülerde anlaşılırlığı artırmak amacıyla r2 değişkeninin de tanımlanmasının yararlı olacağı düşünülerek r2 değişkeninin c1 değişkenine başvurması sağlanmıştır. Bu iki değişken bellekte aynı gözde bulunurlar ve dolayısıyla birinde yapılan değişiklik doğrudan doğruya diğerini etkiler.

Örnekte r2 değişkeni başvuru olmak yerine ikinci bir değişken olarak da tanımlanabilirdi. Bu durumda c1 değişkeni kullanıcıdan okunduktan sonra r2 = c1 şeklinde bir atamayla işlem sürdürülebilirdi. Bu yaklaşımda, iki değişken birbirinden ayrılmış olacağı için birindeki değişiklik diğerini etkilemezdi, ancak programda boyut değişkenleri üzerinde bir değişiklik olmadığı için bir sorun çıkmazdı. Tek ayrım, gereksiz yere ikinci bir değişken tanımlanmış olması olurdu.

## **Ödevler**

Kullanıcıdan alınan iki tarih arasında geçen gün sayısını hesaplayan bir program yazın.

**Chapter 5
Katarlar**

## **Örnek**

Bu bölümde üzerinde çalışılacak program (Örnek 10), kullanıcının girdiği sözcüğü tersine çevirerek ekrana yazar. Bu programın yeniliği sayılar üzerinde değil sözcükler üzerinde işlem yapmasıdır.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS
#include <string.h> // strlen
int main(void)
{
char word[30];
int len, i;
char tmp;
cout << "Sözcük: "; cin >> word;
len = strlen(word);
for (i = 0; i < len / 2; i++)
{
tmp = word[i];
word[i] = word[len - 1 - i];
word[len - 1 - i] = tmp;
}
cout << "Tersi: " << word << endl;
return EXIT_SUCCESS;
}
```

#1 Sözcüğü tersine çeviren program.

Programlamada üzerinde işlem yapılan temel veri tiplerinden biri de katarlardır. Katarlar, sözcük, tümce, ileti gibi bilgi tiplerini temsil ederler. Örnek programda kullanıcının girdiği sözcük bir katar olacaktır. Çoğu programlama dilinin katarlar için özel bir veri tipi olmasına karşın C'de böyle bir özel tip tanımlanmamıştır. Katarlar bir simge dizisi olarak değerlendirilirler. Diğer dizilerden tek farkları eleman sayısının (katarın içerdiği simge sayısının) tutacak bir değişkene gereksinim duyulmamasıdır. Katarlar sonlarına konan '0' simgesiyle sonlandırılırlar. Bu nedenle katar için bellekte ayrılması gereken yer, katarın içerdiği simge sayısının bir fazlasıdır. Örnekteki

```cpp
char word[30];
```

tanımı, her biri simge tipinden, 30 elemanlı, word adında bir katar oluşturur. Bu elemanlardan biri '0' simgesi için kullanılacağından kullanıcının gireceği sözcük en fazla 29 simge uzunluğunda olabilir.

Katar tipinden bir değişkenin tanımlanması sırasında başlangıç değeri çift tırnak içinde belirtilebilir. Tanımlanan boyun katar için gerektiği kadar yeri ayırmasına dikkat edilmelidir. İstenirse boyut belirtilmeyebilir; bu durumda derleyici gerekli yeri kendisi ayırır. Aşağıdaki iki tanım aynı işi görürler:

```cpp
char word[7] = ``Sözcük'';
char word[] = ``Sözcük'';
```

Tam gerektiği kadar yer ayırmak riskli bir davranıştır. Programın içinde katarın uzaması sözkonusu olabilecekse gerekebilecek maksimum alan gözönüne alınmalı ve tanım sırasında bu boy belirtilmelidir.

Katarlar birer dizi olduklarından elemanlarına teker teker erişilebilir.

Katar kitaplığı

## **Ödevler**

Kullanıcıdan alınan bir sayıyı yazı olarak ekrana çıkartan bir program yazın. Örneğin kullanıcı 21355 sayısını girerse program ekrana \`\`Yirmibirbinüçyüzellibeş'' yazacaktır.

**Chapter 6
Fonksiyonlar**

## **Örnek**

Bu bölümde üzerinde çalışılacak program (Örnek 11), kullanıcının girdiği bir sayının asal çarpanlarını ekrana dökecektir. Bu programda bir sayının asal olup olmadığının sınanmasına ve asal sayıların bulunmasına gerek duyulacaktır. Soyutlama ilkesine göre bu işlemler fonksiyonlarla gerçekleştirilecek, ana fonksiyon asal sayıları bulan fonksiyondan sırayla aldığı asal sayıların kullanıcının verdiği sayıyı bölüp bölmediklerini sınayacaktır. Örnekte is\_prime fonksiyonu kendisine gönderilen bir sayının asal olup olmadığını belirleyerek geriye asalsa doğru, değilse yanlış mantıksal değerini yollar. next\_prime fonksiyonu ise kendisine gönderilen asal sayıdan bir sonraki asal sayıyı bularak kendisini çağıran fonksiyona geri yollar.

```cpp
#include <iostream.h> // oout,cin
#include <stdlib.h> // EXIT_SUCCESS
#include <math.h> // sqrt
int next_prime(int prime);
int main(void)
{
int number, factor;
cout << "Sayı: "; cin >> number;
factor = 2;
while (number > 1)
{
while (number % factor == 0)
{
cout << factor << " ";
number /= factor;
}
factor = next_prime(factor);
}
cout << endl;
return EXIT_SUCCESS;
}
bool is_prime(int cand)
{
int count;
if (cand == 2)
return true;
if (cand % 2 == 0)
return false;
for (count = 3; count <= sqrt(cand); count += 2)
{
if (cand % count == 0)
return false;
}
return true;
}
int next_prime(int prime)
{
int cand = (prime % 2 == 0) ? prime + 1 : prime + 2;
while (!is_prime(cand))
cand += 2;
return cand;
}
```

#1 Bir sayıyı asal çarpanlarına ayıran program.

Bir fonksiyon iki bileşenden oluşur:

Fonksiyonun başlığı, fonksiyonun adını ve giriş/çıkış parametrelerini belirtmeye yarar. Soyutlamadaki karşılığıyla fonksiyonun NE yaptığını anlatır.

Fonksiyonun gövdesi, fonksiyonun yapacağı işleri belirten bloktan oluşur, yani fonksiyonun işini NASIL yaptığını anlatır.

## **6.1 Fonksiyonun Bildirimi**

Fonksiyon başlığının belirtilmesi işlemine fonksiyonun bildirimi denir ve başlığın sonuna bir noktalı virgül konarak yapılır. Örnekte next\_prime fonksiyonu için bir bildirim yapılmıştır. Bu bildirim, derleyiciye next\_prime adında bir fonksiyon olduğunu, tamsayı tipinden bir giriş parametresi aldığını ve yine tamsayı tipinden bir değeri geriye döndürdüğünü bildirir. Böylelikle derleyici bu fonksiyon çağrısını gördüğü yerde parametrelerin uyumlu olup olmadıklarını denetleyebilir. Çalışma anında fonksiyon çağrısına gelindiğinde uygun yere gidilmesini sağlayacak bağlantıları kurmak derleyicinin değil bağlayıcının görevidir.

## **6.2 Fonksiyonun Tanımı**

Bir fonksiyonun bütününün, yani giriş/çıkış parametrelerinin yanısıra gövdesinin de belirtildiği yere fonksiyonun *tanımı* denir. Örnekte is\_prime fonksiyonu, main fonksiyonunun bitiminden sonra, next\_prime fonksiyonu da is\_prime fonksiyonunun bitiminden sonra tanımlanmıştır.

Bir fonksiyonun diğer bir fonksiyon tarafından çağırılabilmesi için ya bildirimi ya da tanımı çağıran fonksiyondan önce yapılmalıdır. Örnekte main fonksiyonu next\_prime fonksiyonunu, next\_prime fonksiyonu da is\_prime fonksiyonunu çağırmaktadır. Birinci çağrı, next\_prime fonksiyonunun bildirimi main fonksiyonunun tanımı başlamadan yapıldığından başarılı olur. İkinci çağrı is\_prime fonksiyonu next\_prime fonksiyonundan önce tanımlandığından başarılı olur. Ancak örneğin main fonksiyonu is\_prime fonksiyonunu çağıramaz çünkü öncesinde is\_prime fonksiyonunun ne tanımı ne de bildirimi vardır.

## **6.3 Parametre Aktarımı**

Bir parametre aktarımı sırasında çağıran fonksiyondaki değer, çağırılan fonksiyonun ilgili değişkenine atanır. Örnekteki birinci fonksiyon çağrısında:

```cpp
factor = next_prime(factor);
```

main fonksiyonundaki factor değişkeninin değeri next\_prime fonksiyonunun giriş parametresi olan prime değişkenine atanır. Dönüşte de next\_prime fonksiyonunun return komutuyla geri yolladığı cand değişkeninin değeri main fonksiyonundaki factor değişkenine atanır. Fonksiyonun bir döngü içinde çağrıldığı gözönüne alınarak, parametre olarak ilk çağrıda 2, ikinci çağrıda 3, ileriki çağrılarda 5, 7, 11, ... değerlerinin aktarılacağı görülebilir.

main fonksiyonundaki factor değişkeni ile next\_prime fonksiyonundaki prime değişkeni farklı değişkenlerdir, bellekte farklı yerlerde bulunurlar. Dolayısıyla, birinde yapılan değişiklik diğerini etkilemez.

Benzer şekilde, ikinci fonksiyon çağrısında:

is\_prime(cand)

next\_prime fonksiyonundaki cand değişkeninin değeri is\_prime fonksiyonunun giriş parametresi olan cand değişkenine atanır. Adları aynı olsa da next\_prime fonksiyonunun cand değişkeniyle is\_prime fonksiyonunun cand değişkeni yine farklı değişkenlerdir.

Tipi uygun olduğu sürece parametre olarak herhangi bir deyim belirtilebilir. Sözgelimi aşağıdaki çağrılar geçerlidir:

is\_prime(13)

is\_prime(cand + 1)

Benzer şekilde, geri döndürülen değer de uyumlu tipten bir deyim olabilir:

```cpp
return (cand + 2);
```

Çağrılan fonksiyonun geri yolladığı değer değişik şekillerde kullanılabilir:

Değişkene atama: Örnekteki

```cpp
factor = next_prime(factor);
```

çağrısında olduğu gibi dönen değer çağıran fonksiyondaki bir değişkene atanabilir.

Deyimde kullanma: Örnekteki

```cpp
while (!is_prime(cand))
```

çağrısında olduğu gibi uygun tipten bir deyimde yer alabilir.

Başka bir fonksiyona aktarma: Dönen değer başka bir fonksiyona giriş parametresi olarak yollanabilir:

```cpp
if (!is_prime(next_prime(factor))
cout < < ``next_prime düzgün çalışmıyor.'' < < endl;
```

Bu çağrının başarılı olmasının nedeni, next\_prime fonksiyonunun döndürdüğü değerin tipi ile is\_prime fonksiyonunun giriş parametresinin tipinin uyumlu olmalarıdır.

## **6.4 Tanım Bölgesi**

Her değişken yalnızca tanımlandığı fonksiyon içinde geçerlidir. Fonksiyon içinde tanımlanan değişkenlere *yerel* (local) değişken adı verilir ve bunların *tanım bölgesi* (scope) içinde tanımlandıkları fonksiyonla sınırlanır. Bir fonksiyonun giriş parametreleri de fonksiyonun yerel değişkenlerinden sayılır. Örnekteki bütün fonksiyonların ikişer (main: number ve factor, is\_prime: cand ve count, next\_prime: prime ve cand) yerel değişkeni vardır.

Değişkenlere tanım bölgeleri dışında erişilemez. Yani sözgelimi main fonksiyonu number ve factor dışında kalan değişkenleri kullanamaz. Bazı durumlarda birden fazla fonksiyonun aynı değişkeni kullanabilmeleri istenir. Bu tip değişkenlere *genel* (global) değişken adı verilir ve tanım bölgeleri bütün fonksiyonlar olarak belirlenir. Genel değişkenler bütün fonksiyonların tanımlarından önce tanımlanırlar. Örnek programda şöyle bir değişiklik düşünelim:

...

```cpp
#include <math.h>
int xyz;
int next_prime(int prime);
```

...

Bu şekilde tanımlanan xyz değişkeni örnekteki üç fonksiyon tarafından da kullanılabilir. Tek değişken olduğu için bir fonksiyonun yaptığı değişikliği diğer fonksiyonlar da görür.

Genel değişkenler parametre aktarımı yerine kullanılabilecek bir yöntem olmakla birlikte programın anlaşılırlığını azalttıkları ve fonksiyonları birbirlerine bağımlı kıldıkları için gerekmedikçe kullanılmaması önerilen bir tekniktir.

## **Örnek**

Bu bölümde üzerinde çalışılacak program (Örnek 12), kullanıcıdan aldığı sayı kadar öğrencisi olan bir sınıfta kullanıcının girdiği öğrenci notlarının ortadeğerini bulur. Bir dizinin ortadeğeri, dizi sıralandığında dizinin ortasında yer alan değerdir. Çift sayıda elemanı olan dizilerde dizinin ortasında bir eleman olmadığından ortadaki iki elemanın ortalaması ortadeğer kabul edilir.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS
#define MAXSTUDENTS 50
void selsort(int arr[], int size);
void swap(int &x, int &y);
int main(void)
{
int grades[MAXSTUDENTS];
int nstudents, i;
float median;
cout << "Öğrenci sayısı (en fazla 50 olabilir: "; cin >> nstudents;
for (i = 0; i < nstudents; i++)
{
cout << i + 1 << ". öğrencinin notu: "; cin >> grades[i];
}
selsort(grades, nstudents);
median = (nstudents % 2 == 1) ? grades[nstudents/2] :
(grades[nstudents/2] + grades[nstudents/2-1]) / 2.0;
cout << "Ortadeğer: " << median << endl;
return EXIT_SUCCESS;
}
void selsort(int arr[], int size)
{
int round, max, i;
for (round = 0; round < size - 1; round++)
{
max = 0;
for (i = 1; i < size - round; i++)
if (arr[max] < arr[i])
max = i;
swap(arr[max], arr[size-1-round]);
}
}
void swap(int &x, int &y)
{
int tmp = x;
x = y;
y = tmp;
}
```

#1 Öğrenci notlarının ortadeğerini bulan program.

## **6.5 Seçerek Sıralama**

Dizinin ortadeğerini bulmak için öncelikle diziyi sıralamak gerekir. Sıralama, programcılıkta en çok gereksinim duyulan işlemlerden biridir ve bu işlemin hızlı bir şekilde yapılması amacıyla pek çok algoritma geliştirilmiştir. Seçerek sıralama, en basit sıralama algoritmalarından biridir.

Küçükten büyüğe doğru sıralama yapılacağı varsayımıyla, bu algoritmanın her adımında dizinin en büyük elemanı bulunur ve sondaki elemanla yeri karşılıklı değiştirilir. Böylece en büyük eleman en sona alınır ve dizinin boyu bir azaltılarak işleme devam edilir. n elemanlı bir dizide sözügeçen işlem n−1 kere yinelenecektir. Örnek bir dizi üzerinde seçerek sıralama algoritmasının çalışması Şekil 6.1'de verilmiştir.

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=selsort.png" |  |
| --- | --- | --- |

Şekil 6.1: Seçerek sıralama örneği.

## **6.6 Aktarılan Parametrede Değişiklik**

Örnekteki swap fonksiyonu, kendisine gönderilen iki değişkenin değerlerini karşılıklı olarak değiştirir. Seçerek sıralamanın doğru çalışabilmesi için bu değişikliğin yalnızca swap fonksiyonunda etkili olması yeterli değildir, değişen değerlerin selsort fonksiyonunda da görülebilir olması gerekir. Oysa şimdiye kadar kullandığımız parametre aktarımlarında çağırılan fonksiyondaki giriş parametresinin değerinin değiştirilmesi çağıran fonksiyondaki ilgili değişkeni etkilemiyordu.

Çağırılan fonksiyondaki bir giriş parametresinde yapılan değişikliğin çağıran fonksiyondaki değişkeni etkilemesi isteniyorsa bu giriş parametresi başvuru tipinden tanımlanır (bkz. Bölüm 4.3). Örnekte swap fonksiyonu çağrıldığında yaratılan x değişkeni çalışma anında selsort fonksiyonunun o anki arr\[max\] değişkenine başvurur. x üzerinde yapılan değişiklik doğrudan doğruya arr\[max\] değişkenini etkiler.

Benzer bir sorun, fonksiyonun birden fazla değer geri döndürmesi gerektiğinde de karşımıza çıkar.

## **6.7 Dizilerin Fonksiyonlara Aktarımı**

Diğer değişken tiplerinden farklı olarak, bir dizi bir fonksiyona parametre olarak aktarıldığında dizinin bütün elemanlarının birer kopyası çıkartılarak fonksiyona yollanmaz, yani yeni bir dizi oluşturulmaz. İşlemler asıl dizinin üzerinde yapılır; çağırılan fonksiyon elemanlardan birinin değerini değiştirirse bu değişiklik çağıran fonksiyondaki dizide de görülebilir. Örnekte main fonksiyonundaki grades dizisi ile selsort fonksiyonundaki arr dizisi aynı dizidir; zaten bu iki dizi farklı diziler olsaydı sıralama işlemi yeni oluşturulan arr dizisi üzerinde yapılır ve main fonksiyonundaki grades dizisi bundan etkilenmeyeceğinden program doğru çalışamazdı.

## **Örnek**

Bu bölümde üzerinde çalışılacak program (Örnek 13), yarıçapı komut satırından verilen bir dairenin çevresini ve alanını hesaplayarak ekrana yazar. Örnek 2'den en önemli farkı, kullanıcının yarıçap değerini program başladıktan sonra değil, programı başlatırken belirlemesidir. Sözgelimi bu programın yazılı olduğu dosya maincirc.cc ise ve derleme ve bağlama sonucu oluşan çalıştırılabilir dosyanın adı maincirc olursa program

maincirc 2.4

gibi bir komutla çağırılmalıdır. Program çalıştırılırken bir yarıçap değeri belirtilmezse ya da birden fazla komut satırı parametresi belirtilirse program hata verecektir. Bu örneğin bir yeni tarafı da hata mesajlarını normal çıktıdan ayırması ve hata birimine yollamasıdır.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS,atof
#define PI 3.14
#define sqr(x) ((x) * (x))
int main(int argc, char *argv[])
{
float radius;
float circum, area;
if (argc == 1)
{
cerr << "Komut satırında bir yarıçap belirtmelisiniz." << endl;
return EXIT_FAILURE;
}
else if (argc > 2)
{
cerr << "Komut satırında fazla parametre var." << endl;
return EXIT_FAILURE;
}
radius = atof(argv[1]);
circum = 2 * PI * radius;
area = PI * sqr(radius);
cout << "Çevre: " << circum << endl;
cout << "Alan: " << area << endl;
return EXIT_SUCCESS;
}
```

#1 Yarıçapı komut satırından belirtilen dairenin çevre ve alanını hesaplayan program.

## **6.8 Ana Fonksiyona Parametre Aktarımı**

Ana fonksiyon da diğer fonksiyonlar gibi bir fonksiyon olmakla birlikte giriş ve çıkış parametrelerinin aktarımı bakımından farklılık gösterir. Bir fonksiyonun giriş parametreleri alması ve çıkış parametresi döndürmesi, o fonksiyonun çağırılabilmesi anlamına gelir. Oysa ana fonksiyon çalışmanın başladığı fonksiyon olduğundan diğer fonksiyonlarca çağırılan değil, diğer fonksiyonları çağıran konumundadır. Ana fonksiyonu çağıran işletim sistemidir, yani ana fonksiyonun çağırılması programın işletim sistemince yürütülmeye başlanmasına karşı düşer. Bu durumda ana fonksiyon giriş parametrelerini işletim sisteminden alır, çıkış parametresini de işletim sistemine döndürür.

Program çalışması sırasında kullanıcıyla giriş - çıkış işlemlerini kendisi yapar. Dolayısıyla kullanıcıdan alınan değerler ve ekrana yazılan değerler ana fonksiyonun giriş - çıkış parametreleri değildir.

## **6.8.1 Çıkış Parametreleri**

Çıkış parametresi, programın çalışması sonucu oluşan durumun işletim sistemine bildirilmesi anlamını taşır. Örnekteki

```cpp
return EXIT_SUCCESS;
```

komutu, işletim sistemine programın başarıyla sonlandığını belirtir. Benzer şekilde,

```cpp
return EXIT_FAILURE;
```

komutu bir hata durumu olduğunu belirtir. İşletim sistemlerinde bu bilgiler genellikle kabuk programlama (shell scripting) uygulamalarında kullanılır.

## **6.8.2 Hata İletileri**

Bir C programının içinde çalıştığı ortamda üç adet giriş - çıkış birimi vardır:

Standart giriş: Programın giriş işlemlerini yaptığı birim. Örneklerimizde bu birim olarak cin'i kullanıyoruz. Aksi belirtilmedikçe bu birim kullanıcının kullandığı tuştakımıdır.

Standart çıkış: Programın çıkış iletilerini yolladığı birim. Örneklerimizde bu birim olarak cout'u kullanıyoruz. Aksi belirtilmedikçe bu birim kullanıcının kullandığı ekrandır.

Standart hata: Programın hata iletilerini yolladığı birim. Genellikle hata iletilerinin diğer iletilerden ayrılmaları istenir. Bu amaçla normal iletiler standart çıkışa, hata iletileri de standart hata birimine yollanır. Böylece programın çalışması sırasında oluşabilecek aykırı durumların daha kolay farkedilmeleri sağlanır. Örneklerimizde bu birim olarak cerr'i kullanacağız. Aksi belirtilmedikçe bu birim -standart çıkışta olduğu gibi- kullanıcının kullandığı ekrandır.

Program çalıştırılırken bu üç birim başka yerlere *yönlendirilebilir*. Sözgelimi, giriş bilgileri bir dosyadan okunabilir ya da çıkış bilgileri doğrudan yazıcıya yollanabilir. Yönlendirme işleminin nasıl yapılacağı kullanılan işletim sistemine bağlıdır.

## **6.8.3 Giriş Parametreleri**

Ana fonksiyonun giriş parametreleri kullanıcının programı çalıştırırken belirttiği parametrelerdir. Bunlara *komut satırı* (command line) parametreleri de denir. Giriş parametrelerinin okunabilmesi için ana fonksiyonun giriş parametresi listesi

```cpp
int argc, char *argv[]
```

şeklinde belirtilir. Burada argc parametre sayısını (argument count), argv ise parametre değerlerini (argument vector) gösterir.

Programın adı da parametreler arasında sayıldığından parametre sayısı en az 1 olabilir. Yani örnek program yalnızca maincirc komutuyla çağırılırsa argc değişkeni 1 değerini alır. maincirc 2.4 şeklinde çağırmada argc değişkeni 2 değerini alacaktır.

Parametre değerleri de argv dizisinin elemanlarını oluştururlar. Yine son örnek üzerinden gidersek

argv\[0\] = \`\`maincirc''

argv\[1\] = \`\`2.4''

olur. Dikkat edilecek bir nokta bütün parametrelerin birer katar olarak değerlendirildikleridir. Örnekte yarıçapı gösteren radius değişkeni gerçel bir sayıdır ve gerçel bir değer alması gerekir, oysa komut satırından gelen parametre \`\`2.4'' katarıdır. Sayı olarak kullanılabilmesi için atof kitaplık fonksiyonuyla sayıya çevrilmesi gerekir.

## **Sorular**

Kusursuz bir sayı, kendisinden küçük bütün çarpanlarının toplamına eşit olan sayıdır. Örnek: 28=1+2+4+7+14 . Buna göre:

Kendisine gönderilen sayının kusursuz sayı olup olmadığını belirleyen bir fonksiyon yazınız.

Bu fonksiyonu kullanarak, ilk 10000 sayı içindeki kusursuz sayıları ekrana döken bir ana fonksiyon yazınız.

Kendisine gönderilen katardaki sözcük sayısını döndüren bir fonksiyon yazınız. Katar başında, sonunda ve sözcükler arasında bir ya da birden fazla boşluk bulunabilir. Katarda tab simgesi ya da noktalama işaretleri bulunmadığı varsayılabilir. Sözgelimi, giriş katarı

\`\` the world is not enough ''

ise, fonksiyon 5 değerini döndürmelidir.

Kendisine parametre olarak gönderilen bir katarda, yine kendisine parametre olarak gönderilen bir simgenin ilk ve son pozisyonları arasında kaç simge olduğunu bularak sonucu döndüren bir fonksiyon yazınız. Sözgelimi, giriş katarı

\`\`the world is not enough''

ve giriş simgesi 'o' ise, fonksiyon 13 değerini döndürmelidir (\`\`rld is not en'').

İki tamsayı dizisindeki ortak elemanların sayısı bulunmak isteniyor. Örneğin birinci dizi \`\`21 10 9 13 15'', ikinci dizi \`\`10 7 1 13 15 8'' ise ortak elemanların sayısı 3'tür (10, 13, 15). Örnekten de görülebileceği gibi, dizilerin aynı sayıda elemanları bulunması zorunlu değildir. Bunun için:

Bir sayının bir dizide bulunup bulunmadığını sınayan bir fonksiyon yazınız. Fonksiyonun giriş parametreleri dizi, dizinin boyu ve aranan sayı olmalıdır. Geriye sayı dizide varsa 1, yoksa 0 değeri döndürülmelidir.

Yukarıda yazdığınız fonksiyonu kullanarak, iki dizideki ortak elemanların sayısını belirleyen bir fonksiyon yazınız. Fonksiyonun giriş parametreleri her iki dizinin kendileri ve boyları olmalıdır. Fonksiyon geriye ortak elemanların sayısını döndürmelidir.

Yukarıda yazdığınız fonksiyonları kullanarak, boyunu ve elemanlarını kullanıcıdan aldığı iki dizinin ortak eleman sayısını bularak ekrana çıkartan bir ana fonksiyon (main) yazınız.

Bir dizinin kipi, dizide en çok yinelenen elemandır. Sözgelimi

75 32 45 43 75 66 43 88 66 92 66 27

dizisinin kipi 66'dır. Buna göre, bir sınavdaki öğrenci notlarının kipi bulunmak isteniyor.

Bir dizinin en büyük elemanının dizideki sırasını döndüren bir fonksiyon yazınız.

Yukarıda yazdığınız fonksiyonu kullanarak bir dizinin kipini döndüren bir fonksiyon yazınız. (Yol gösterme: Elemanları ilgili notun kaç kere geçtiğini gösteren 101 elemanlı bir tamsayı dizisi kullanın. Örneğin counts\[55\], 55 notunun kaç kere alındığını göstersin.)

Yukarıda yazdığınız fonksiyonları kullanarak, öğrenci sayısını ve notlarını kullanıcıdan alarak notların kipini bulan ve ekrana çıkartan bir ana fonksiyon (main) yazınız.

**Chapter 7
İleri Veri Tipleri**

Bir programlama dili, tamsayı, gerçel sayı, katar gibi desteklediği temel veri tiplerinin yanısıra, programcıya kendi veri tiplerini oluşturma olanağı sunmalıdır. Bir veri tipinin temsil ettiği bilgiyi olabildiğince doğru bir şekilde modellemesi gerekir.

Sözgelimi, programda bir tarih dizisi tutulmak isteniyor olsun. C'de tarih için özel bir veri tipi olmadığından bir tarih bilgisinin tutulması için biri günü, biri ayı biri de yılı belirleyen üç tamsayı gerekir. Tarih dizisi içinse benzer şekilde üç tamsayı dizisi gerekecektir. Böyle bir veri modellemesinde, günler, aylar ve yıllar dizilerinin aynı indisli elemanlarının birleşerek bir tarih oluşturdukları programcının aklında bulunması gereken bir bağlantıdır. Oysa üç tamsayıyı birleştirerek bir tarih veri tipi oluşturulur ve elemanları bu tipten bir dizi tanımlanırsa modellenen bilgiye daha iyi uyan bir yapı kurulmuş olur.

C dili de programcıya kendi veri tiplerini yaratmak için bazı olanaklar sağlar. Bu bölümde bunlar anlatılacaktır.

## **7.1 Tiplere Yeni İsim Verme**

C dilinin programcıya kendi veri tiplerini tanımlayabilmesi için sunduğu temel olanak var olan veri tiplerine yeni isimler verilebilmesidir. Sözgelimi bir sınavdaki öğrenci notları için bir dizi tanımlanmak isteniyor olsun. Öğrenci notlarının 0 ile 100 arasında birer tamsayı olacağı varsayımıyla öğrenci notu tipinden bilgileri temsil etmek üzere bir veri tipi tanımlanabilir:

```cpp
typedef int grade_t;
```

Burada typedef saklı sözcüğünden sonra yazılan ilk veri tipi asıl tipin ismi, ikincisi de bu asıl tipe verilen yeni isimdir. Yani örnekte int veri tipine grade\_t diye yeni bir isim verilmiştir. Daha sonra bu tipten bir dizi tanımlamak için

```cpp
grade_t grades[MAXSTUDENTS];
```

komutu yazılabilir.

Bir veri tipine yeni bir isim vermenin yararları şöyle açıklanabilir:

Anlaşılırlık artar: Programın kodunu okuyan kişi bu veri tipinin temsil ettiği bilgiyle ilgili daha iyi bir fikir edinebilir.

Değiştirmek kolay olur: Program geliştirmenin ileri aşamalarında öğrenci notlarının kesirli olabileceği durumu ortaya çıkarsa yalnızca veri tipine isim verme komutunun

```cpp
typedef float grade_t;
```

biçiminde değiştirilmesi yeterli olur. Veri tipi tanımı yoksa bütün kodun taranarak öğrenci notuna karşılık gelen int veri tiplerini bulup değiştirmek gerekir. Bu da bazı int sözcüklerinin değişmesi, bazılarının değişmemesi anlamına gelir ve programın boyutlarına göre büyük zorluklar çıkarabilir.

## **Örnek**

Bu bölümde üzerinde çalışılacak program (Örnek 14), kullanıcıdan aldığı iki karmaşık sayıyı toplayarak sonucu ekrana çıkartır. Bu programda, programcının var olan veri tiplerini birleştirerek kendisinin bir veri tipi oluşturması incelenecektir.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS
struct complex_s
{
float re;
float im;
};
typedef struct complex_s complex_t;
complex_t add_complex(complex_t c1, complex_t c2);
int main(void)
{
complex_t n1, n2, n3;
cout << "Birinci sayıyı yazın: "; cin >> n1.re >> n1.im;
cout << "İkinci sayıyı yazın: "; cin >> n2.re >> n2.im;
n3 = add_complex(n1, n2);
cout << "Toplam: " << n3.re << " + " << n3.im << "i" << endl;
return EXIT_SUCCESS;
}
```

complex\_t add\_complex(complex\_t c1, complex\_t c2)

```cpp
{
complex_t c3;
c3.re = c1.re + c2.re;
c3.im = c1.im + c2.im;
return c3;
}
```

#1 Karmaşık sayılar üzerinde işlem yapan program.

## **7.2 Yapılar**

Çoğu dilde *kayıt* adı verilen, başka veri tiplerini birleştirerek oluşturulan veri tiplerinin C dilindeki adı *yapı*dır. Yapılar, her biri kendi bir veri tipinden olan alanlardan oluşur. Örnekte karmaşık sayıları göstermek üzere bir yapı kullanılmıştır. Bu yapının iki alanı vardır: birincisi sayının gerçel kısmını gösteren re alanı, ikincisi de sayının sanal kısmını gösteren im alanıdır. Her iki alan da gerçel sayı tipindendir.

Yapı tanımının sonucunda yeni bir veri tipi oluşur. Örnekteki tip tanımı sonucunda artık

```cpp
struct complex_s
```

adında bir veri tipi oluşmuştur. Programcının yeni veri tipi için belirttiği sözcük (örnekte complex\_s) yeni veri tipinin *künyesi* olarak adlandırılır. Örnek programda kullanım kolaylığı açısından bu veri tipine typedef komutuyla yeni bir isim verilmiştir13.

Tip tanımı bir değişken tanımı olmadığı için bellekte yer ayrılmasına neden *OLMAZ*. Bir yapının kullanılması için bu yapının tipinden değişken tanımlamak gerekir. Bu tanımlama da, diğer veri tiplerinde olduğu gibi yapılır. Burada yapının tipi olarak istenirse asıl verilen isim, istenirse typedef ile verilen yeni isim kullanılabilir:

```cpp
complex_t n1, n2, n3;
struct complex_s n1, n2, n3;
```

Her iki komut da aynı işi yaparlar, yani n1, n2 ve n3 isimlerinde, birer karmaşık sayı yapısında olan üç adet değişken tanımlarlar (Şekil 7.1).

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=struct1.png" |  |
| --- | --- | --- |

Şekil 7.1: Yapı tipinden değişken tanımlama.

Bu değişkenlerin her biri, yapıda belirtilen alanlara sahiptir. Alanlar üzerinde işlem yapmak için *noktalı gösterilim* kullanılır, yani değişkenin adından sonra nokta işareti ve alanın adı belirtilerek işlem yapılabilir. Yani birinci sayının gerçel kısmıyla bir işlem yapılacaksa n1.re yazılır.

Aynı yapı tipinden değişkenler arasında atama işlemi yapılması, birinin bütün alan değerlerinin diğerine olduğu gibi kopyalanması anlamına gelir. Yani, örnekte main fonksiyonundaki n1 değişkeni add\_complex fonksiyonunun c1 değişkenine aktarılırken n1'in re alanının değeri c1'in re alanına, n1'in im alanının değeri de c1'in im alanına atanır. n2 değişkeninin c2 değişkenine atanması ve geri dönüşte result değişkeninin n3 değişkenine atanması da aynı şekilde değerlendirilebilir.

Yapının bir alanının bir dizi olması durumunda atama işlemlerinde dikkatli olmak gerekir:

```cpp
struct person_s
{
char name[50];
int birth_year;
};
struct person_s person1, person2;
```

tanımları yapıldıysa

```cpp
person1.name = ``Dennis M. Ritchie'';
person1.birth_year = 1941;
person2 = person1;
```

işlemleri sonucunda Şekil 7.2'deki durum oluşur. Şekilden görülebileceği gibi, person1 değişkeninin name alanında yer alan katar işaretçisi değeri, person2 değişkeninin name alanına atanacağından iki değişkenin name alanları aynı katarı işaret eder hale geleceklerdir; yani katarın bir kopyası çıkarılmayacak, olan tek katar iki değişken tarafından paylaşılacaktır. Çoğu zaman istenen bu değildir ve bu örnekte kopyalamanın doğru yapılması için aşağıdaki komutlar kullanılmalıdır:

```cpp
strcpy(person2.name, person1.name);
person2.birth_year = person1.birth_year;
```

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=struct2.png" |  |
| --- | --- | --- |

Şekil 7.2: Yapıların birbirine atanması.

Bir yapının bir alanı başka bir yapı tipinden olabilir.

```cpp
struct date_s
{
int day, month, year;
};
struct person_s
{
char name[50];
struct date_s birth_date;
};
```

tanımları Şekil 7.3'de görülen yapıyı oluşturur. Alanlara erişim yine noktalı gösterilimle sağlanır:

```cpp
struct person_s person[30];
person[5].name = ``Dennis M. Ritchie'';
person[5].birth_date.year = 1941;
```

| PRIVATE | PRIVATEPRIVATE "TYPE=PICT;ALT=struct3.png" |  |
| --- | --- | --- |

Şekil 7.3: Yapı içinde yapı kullanma.

## **7.3 Birlikler**

## **7.4 Numaralandırma**

**Chapter 8
İşaretçiler**

Şu ana kadar yapılan örneklerde değişkenlerin bellekte kaplayacakları yer baştan belliydi. Sözgelimi, 100 elemanlı bir tamsayı dizisi tanımlanırsa bu diziye bellekte 100 adet tamsayıyı tutacak kadar yer ayrılacağı derleme aşamasında bellidir. Bu tip değişkenlere *statik değişken* adı verilir. Statik bir değişkenin yeri program çalışmaya başladığında ayrılır ve programın sonuna kadar bırakılmaz. Bu durumun iki sakıncası vardır:

Değişkenin kullandığı yerin programın bütün işleyişi boyunca tutulması gerekli olmayabilir. Örneğin değişken belli bir noktada kullanılmaya başlayacak ve bir noktadan sonra da kullanılmayacak olabilir. Değişkenin bu \`\`gerekli olduğu'' bölge dışında yer kaplamaya devam etmesi belleğin etkin kullanılmasını engeller.

Tutulacak değişkenin boyu derleme aşamasında belli değilse gerekebilecek en büyük miktarda yer ayrılmak zorunda kalınır. Örneğin, değişik sınıflardaki öğrencilerin notlarını tutmak üzere bir tamsayı dizisi tanımlanacak olsun. Bu durumda bir sınıftaki maksimum öğrenci sayısı konusunda bir varsayım yapıp (diyelim 100) dizi bu boyutta açılmalıdır. Verilen bu boyut hem programın bir sınırlaması olacak, hem de öğrenci sayısı bunun altında kaldığı zamanlarda gereksiz bellek harcanmasına yol açacaktır.

Bu sorunları çözmek için tasarlanan *işaretçiler*, bellekte kaplanacak yerin derleme sırasında değil çalışma sırasında belirlenmesini sağlarlar. Böylelikle gerektiği zaman gerektiği kadar yer almak ve gerek kalmadığı zaman da geri vermek olanaklı hale gelir. Buna karşılık, dinamik olarak kullanılan bu alanların düzgün yönetimi programcıya bırakılmış olduğundan programların en sık hata yapılan bölümlerindendir.

## **8.1 İşaretçi Tipinden Değişkenler**

İşaretçi tipinden bir değişken, bir bellek gözünün adresini taşır; başka bir deyişle, bir bellek gözüne \`\`işaret eder''.

İşaretçi tipinden bir değişken tanımlamak için yıldız (\*) simgesi kullanılır. Bütün işaretçiler birer adres olmakla (dolayısıyla boyları aynı olmakla) birlikte, tanımlarında ne türden bir değişkene işaret ettikleri belirtilmelidir. Örnek:

```cpp
int *i;
```

Yukarıdaki tanımın anlamı i değişkeninin bir tamsayı işaretçisi olduğudur. Yani, i'nin gösterdiği bellek gözünde yer alan bilgi bir tamsayı olarak yorumlanacak demektir.

İşaretçi tipinden bir değişken tanımlandığı zaman bellekte bir adres tutacak kadar yer ayrılır (işaretçinin kendi değerini tutmak üzere). İşaretçinin göstereceği bellek gözü içinse çalışma anında yer ayırmak gerekir.

Alınacak yerin boyu çalışma sırasında belirlenebilir, yani alınacak yerin boyunu belirten ifadede değişkenler bulunabilir. Ayrıca, statik değişkenlerin aksine, işaretçiler yardımıyla bildirilen değişkenler için alınan yer, değişkenin işi sona erince geri verilebilir. İşaretçilere yer almak ve bu yeri geri vermek için kitaplık fonksiyonları tanımlanmıştır.

Boş işaretçi NULL saklı sözcüğüyle belirtilir. İşaretçilere çoğu zaman başlangıç değeri olarak NULL atanır.

```cpp
int *a = NULL;
```

İşaretçi Operatörü (\*): Bir işaretçinin işaret ettiği bellek gözünün içeriğini öğrenmekte kullanılır. Yukarıdaki örnekteki atamadan sonra

```cpp
*b = a
```

olur.

## **8.2 Bellek Yönetimi**

new delete

## **8.3 İşaretçi - Dizi İlişkisi**

C'de statik tanımlanmış diziler ile işaretçiler yardımıyla oluşturulan diziler tamamen aynı şekilde değerlendirilirler.

```cpp
int dizi[4];
int i;
i = dizi[3];
```

program parçası ile

```c
int *dizi;
int i;
dizi = (int *) malloc(4 * sizeof(int));
i = dizi[3];
```

program parçası aynı işi görürler. Bu işlev, iki kural sayesinde geçerli olur:

İşaretçi, dizinin ilk elemanının adresini tutar.

```cpp
int *p;
int dizi[10];
```

tanımları yapıldıysa

```cpp
p = &dizi[0];
```

ile

```cpp
p = dizi;
```

aynı anlama gelir.

İşaretçi değerlerine bir tamsayı eklenebilir ya da çıkartılabilir. İşaretçinin değeri bir sayıyla toplanırsa, işaretçi o sayı ile işaret ettiği tipin boyunun çarpımı kadar ilerler. Benzer şekilde, çıkartma işleminde bu miktar kadar geriler. Sözgelimi, p bir tamsayı işaretçisi ise:

p+1=p+sizeof(int)

p−1=p−sizeof(int)

p+n=p+n\*sizeof(int)

p−n=p−n\*sizeof(int)

p\[n\] deyimi derleyici tarafından \*(p + n) şeklinde değerlendirilir. p + n, p adresinden başlayarak, her biri p'nin işaret ettiği veri tipinden olmak üzere, n eleman ilerlenerek bulunduğundan, p bir dizi, p\[n\] de p dizisinin n. elemanı olarak görülebilir.

İşaretçilerle işlem yaparken, işaretçinin kendisiyle mi, yoksa işaret ettiği alanla mı işlem yapıldığına dikkat edilmelidir. Örneğin, p bir işaretçi ise

```cpp
p++;
```

komutu yürütüldükten sonra p işaretçisi değer değiştirir. Oysa p'nin işaret ettiği alandaki verinin artması isteniyorsa

```cpp
(*p)++;
```

komutu yürütülmelidir.

## **8.4 Parametre Aktarımı**

Çağırılan fonksiyondaki giriş parametresinde yapılan değişikliğin çağıran fonksiyondaki değişkeni etkilemesini sağlamanın ikinci bir yolu da çağırılan fonksiyona değişkenin adresini yollamaktır. Çağırılan fonksiyon bu adresi işaretçi tipinden bir değişkene alır ve bu işaretçinin gösterdiği yerde değişikliği yapar. Böylece değişiklik çağıran fonksiyondaki değişkeni doğrudan etkiler.

Adres işleci (&), başına eklendiği değişkenin adresinin elde edilmesini sağlar. Buna göre, örnekteki swap fonksiyonu şu şekilde de yazılabilirdi:

```cpp
void swap(int *x, int *y)
{
int tmp = *x;
*x = *y;
*y = tmp;
}
```

Bu swap fonksiyonunu kullanan selsort fnnksiyonunda çağrının yapılışı şu şekilde olurdu:

```cpp
swap(&arr[max], &arr[size-1-round]);
```

Bu örnekte x değişkeni tamsayıya işaretçi (yani adres) tipinden bir değişken olurdu ve değeri arr\[max\] değişkeninin adresi olurdu. Yani x işaretçisinin gösterdiği yere yazılan değer arr\[max\] değişkenine yazılmış olurdu.

Yapılara işaretçiler ->

**Chapter 9
Projeler**

Yazılan programın kapsamı büyüdükçe bütün kaynak kodunun tek bir dosyada toplanması zorlaşmaya başlar.

**Appendix A
C ile C++ Arasındaki Farklar**

**Açıklamalar ******

Çift bölüden başlayıp satır sonuna kadar giden kısmın açıklama olarak değerlendirilmesi C++ ile getirilmiş bir yeniliktir, C dilinde geçerli değildir. C'de tek açıklama yöntemi açıklama metninin yıldız-bölü ve bölü-yıldız arasına alınmasıdır.

**Giriş/Çıkış ******

C dilinde cout ve cin birimleri yoktur. Çıkış işlemleri printf, giriş işlemleri de scanf kitaplık fonksiyonları aracılığıyla gerçekleştirilir.

**Değişken Bildirimleri ******

C++ dilinde bildirimler komutlar başladıktan sonra da yapılabilir. Örnek 14, şu şekilde de yazılabilirdi:

```cpp
float radius;
cout < < ``Yarıçap: ``;
cin > > radius;
float circum = 2 * PI * radius;
float area = PI * sqr(radius);
```

C dilindeyse komutlar başladıktan sonra artık değişken bildirimi yapılmasına izin verilmez, yani yukarıdaki örnek C dilinde derlenmez.

**Mantıksal Veri Tipi ******

C dilinde mantıksal verileri temsil edecek bir veri tipi yoktur, bu yöntem C++ dilinde getirilmiştir; yani bool, true ve false sözcükleri geçerli C sözcükleri değildir. C mantıksal değerleri sayı olarak gördüğünden her aritmetik deyim aynı zamanda bir mantıksal deyim olarak değerlendirilebilir. Bir aritmetik deyimin değeri 0 ise yanlış bir koşulu, 0'dan farklı ise doğru bir koşulu temsil ettiği varsayılır.

Doğru ve yanlış büyüklükleri programlarda sıkça gereksinim duyulan değerler olduklarından genellikle bunlar genellikle programın başında değişmez olarak tanımlanırlar.

```cpp
#define TRUE 1
#define FALSE 0
```

Daha sık kullanılan bir yöntemse bunları bir numaralandırma içinde tanımlayarak oluşacak veri tipine yeni bir isim vermektir.

```cpp
typedef enum { FALSE, TRUE } bool;
```

Böylelikle C++ dilinde olduğu gibi mantıksal bir veri tipi tanımlanmış olur ve bu tipten değişkenler kullanılabilir.

C dilinde 0 değerine sahip deyimlerin yanlış, diğerlerinin doğru kabul edilmesi eşitlik karşılaştırmalarında hataya yol açabilir. En sık yapılan C hatalarından biri bir eşitlik karşılaştırmasında == yerine = işareti kullanılmasıdır.

```cpp
age = 12;
```

...

...

```cpp
if (age = 18)
block1;
else
block2;
```

Yukarıdaki programda koşulun sınanması sırasında eşitlik işlemi değil atama işlemi belirtildiğinden age değişkenine 18 atanır, deyimin değeri 18 olarak bulunur ve 0'dan farklı olduğu için doğru sayılarak block1 yürütülür. Oysa == simgesi kullanılsaydı age değişkeninin değeri değişmeyecek ve block2 yürütülecekti.

**Değişmezler ******

C dili const ile tanımlanmış değişmezlerin değerlerinin değiştirilebilmesine izin verir. Bu tipten bir değişkene atama yapılmak istendiğinde derleyici hata değil, yalnızca bir uyarı üretecektir.

**Başvurular ******

**Bellek Yönetimi ******

C standardında çalışma anında yer ayırmak ve geri vermek için üç fonksiyon tanımlanmıştır.

```c
void *malloc(size_t size);
```

Bu fonksiyon bellekte birbirini izleyecek şekilde size boyunda yer ayırır ve ayırdığı yerin başlangıç adresini geri döndürür. Alan boyu sekizli cinsinden belirtilir. Geri gönderdiği bilgi herhangi bir tipe işaret etmeyen bir adres bilgisidir, programcının bunu istediği tipe zorlaması gerekir. Bu fonksiyon çağrısı, başlangıç değeri ifadesinde de yer alabilir. Yer alma girişimi başarısızlıkla sonuçlanırsa, örneğin bellekte yer kalmadıysa, geriye NULL döndürür.

```c
int *a = NULL, *b = NULL;
float *c = (float *) malloc(20 * sizeof (float));
a = (int *) malloc(sizeof(int));
b = (int *) malloc(10 * sizeof(int));
```

Örnekte b, malloc işleminden sonra 10 elemanlı bir tamsayı dizisinin ilk elemanının adresini içerir.

```c
void *calloc(size_t nitems, size_t size);
```

Bu fonksiyon bellekte her biri size uzunluğunda olmak üzere nitems adet byte yer ayırır ve ayırdığı alanı 0 ile doldurur.

```c
b = (int *) calloc(10,sizeof (int));
void free(void *block);
```

Bu fonksiyon block işaretçisinin kapladığı alanı geri verir. çağırılmasından sonra artık işaretçinin gösterdiği alana erişilemez.

**Appendix B
Ayrıntı**

**Çoklu Atama ******

C dilinde aynı anda birden çok değişkene birden aynı değer atanabilir. Örneğin

```cpp
a = b = c = 24;
```

komutu a, b ve c değişkenlerinin üçüne de 24 değerini atar. Bu işlem sağdan sola doğru gerçekleştirilen peşpeşe atamalar şeklinde düşünülebilir:

```cpp
c = 24;
b = c;
a = b;
```

**İşlemli Artırma/Azaltma ******

Artırma ve azaltma işlemleri başka işlemlerle birlikte kullanılabilir. Sözgelimi bir artırma işlemiyle bir atama işlemi aynı komut içerisinde yapılabilir. Böyle durumlarda artırma/azaltma işlecinin değişken adının önüne ya da arkasına yazılması önem kazanır. Önüne yazıldığında önce artırma, sonra atama yapılacaktır. Arkasına yazıldığındaysa önce atama, sonra artırma yapılır. Yani

```cpp
y = ++x;
```

komutu

```cpp
x++;
y = x;
```

koduna karşı düşerken

```cpp
y = x++;
```

komutu

```cpp
y = x;
x++;
```

koduna karşı düşer.

Bu tip kısaltmalar kodun anlaşılırlığını azalttıklarından kullanımları özendirilmez.

**Tek Komutlu Bloklar ******

Seçim ya da yineleme yapıları bir bütün olarak tek bir komut olarak görülürler:

```cpp
if (ph > 7)
cout < < ``Asit'' < < endl;
else
if (ph < 7)
cout < < ``Baz'' < < endl;
else
cout < < ``Nötr'' < < endl;
```

Süslü parantezler kullanılmadığında if / else yapılarında belirsizlikler oluşabilir. Örneğin

```cpp
if (x > 5)
if (x < 8)
/* a bölgesi */
else
/* b bölgesi */
```

kodunda a bölgesine gelmek için x değişkeninin değerinin 5'den büyük 8'den küçük olması gerektiği açıktır ancak b bölgesine gelmek için ne olması gerektiği açık değildir. else kısmı üstteki if ile ilişkilendirilirse x değişkeninin değeri 5'den büyük değilse bu bölgeye gelinir, yani girintileme ile gösterilirse şu şekilde yorumlanır:

```cpp
if (x > 5)
if (x < 8)
```

a bölgesi

```cpp
else
```

b bölgesi

Alttakiyle ilişkilendirilirse x 5'den büyükse ve 8'den küçük değilse b bölgesine gelinir, yani girintileme ile gösterilirse şu şekilde yorumlanır.

```cpp
if (x > 5)
if (x < 8)
```

a bölgesi

```cpp
else
```

b bölgesi

Örneğin 4 değeri için birincide b bölgesine girilirken ikincide bütün if yapısı atlanır. 9 değeri içinse birincide bütün iki bölgeye de girilmezken ikincide b bölgesine girilir.

Bu belirsizliği önlemek için C dilinin getirdiği kural, her else'in kendisinden önce gelen en son if ile ilişkilendirileceğidir, yani yukarıdaki yorumların ikincisi geçerli sayılır.

Bu tip karışıklıklara fırsat vermemek amacıyla blok başlangıç ve bitişlerini her zaman süslü parantezlerle işaretlemek daha doğrudur.

**Bildirilmeyen Fonksiyonlar ******

Bildirimi yapılmadan kullanılan fonksiyonların değişken sayıda parametre alabildikleri ve int tipinden değer döndürdükleri kabul edilir. Genelde C fonksiyonları, çıkış parametrelerini yaptıkları işle ilgili olarak oluşan hata durumlarını çağıran fonksiyona iletmek için kullanırlar. çoğu zaman, -1 ya da başka bir negatif değer, işlemin başarıyla tamamlanamadığını belirtir.

**İleri Tip Tanımlama ******

Tipin tanımlanması ve yeni isim verilmesi işlemleri istenirse tek komutta birleştirilebilir:

```cpp
typedef struct complex_s
{
float re, im;
} complex_t;
```

Birleştirilmiş tanımlamada istenirse tipin künyesi de belirtilmeyebilir, yani yukarıdaki örnekte complex\_s sözcüğü yazılmasa da olurdu. Yine de çoğunlukla önerilen yöntem, belirtilmeleri zorunlu olmasa da künyeleri yazmaktır.

**Appendix C
Kitaplıklar**

## **C.1 Matematik**

## **C.2 Katar**

**Appendix D
Uygulamalar**

## **Çoklu Karşılaştırma**

Barbut oyununun kuralları şöyledir:

Oyuncu bir çift zar atar.

Attığı zarların toplamı 7 ya da 11 ise oyuncu kazanır.

Attığı zarların toplamı 2, 3 ya da 12 ise oyuncu kaybeder.

Diğer durumlarda attığı zarların toplamı oyuncunun sayısı olur.

Oyuncu aynı toplamı veren zarları bir daha atana kadar ya da attığı zarların toplamı 7 olana kadar zar atmaya devam eder.

Aynı toplamı bir daha atarsa oyuncu kazanır.

Attığı zarların toplamı 7 olursa oyuncu kaybeder.

Örnek 15 bu oyunu simüle eden bir programdır. Bu örneğin ilginç bir yönü switch yapısının bazı durumlarında kasıtlı olarak break kullanılmamasıdır (fall-through case). Böylelikle durumlar gruplanarak her bir grup için yapılacak işlemlerin bir kere belirtilmesi sağlanmıştır.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS,srand,rand,RAND_MAX
#include <time.h> // time
int main(void)
{
int game_status, point;
int die1, die2, sum;
srand(time(NULL));
die1 = 1 + rand() % 6;
die2 = 1 + rand() % 6;
sum = die1 + die2;
cout << "Gelen: " << die1 << " + " << die2 << " = " << sum << endl;
switch (sum)
{
case 7:
case 11:
game_status = 1; break;
case 2:
case 3:
case 12:
game_status = 2; break;
default:
game_status = 0;
point = sum;
cout << "Sayı: " << sum << endl;
break;
}
while (game_status == 0)
{
die1 = 1 + rand() % 6;
die2 = 1 + rand() % 6;
sum = die1 + die2;
cout << "Gelen: " << die1 << " + " << die2 << " = " << sum << endl;
if (sum == point)
game_status = 1;
else
{
if (sum == 7)
game_status = 2;
}
}
if (game_status == 1)
cout << "Oyuncu kazanır." << endl;
else
cout << "Oyuncu kaybeder." << endl;
return EXIT_SUCCESS;
}
```

#1 Barbut oyununu simüle eden program.

## **Bir Önceki Terimden Giderek Seri Toplamı Hesaplama**

Bu programda (Örnek 16), Örnek 7'de yazılan programın nasıl daha etkin şekilde yazılabileceği incelenecektir. Serinin genel teriminin

| PRIVATEai= | xi i! |  |
| --- | --- | --- |

olduğu gözönüne alındığında dizide bir elemanın kendisinden önceki elemana bölümü

| PRIVATE | ai ai−1 | = | x i |  |
| --- | --- | --- | --- | --- |

olarak hesaplanabilir. Yani her terim, kendisinden önceki terimin x ile çarpılıp i 'ye bölünmesiyle bulunabilir. Böylece her adımda üs alma ve faktöryel hesaplama işlemlerine gerek kalmayacak ve seri toplamı çok daha hızlı bulunabilecektir.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS
int main(void)
{
float x, error, term, result = 1.0;
int i = 2;
cout << "x: "; cin >> x;
cout << "Hata: "; cin >> error;
term = x;
while (true)
{
result += term;
term = term * x / i;
if (term < error)
break;
i++;
}
cout << "Sonuç: " << result << endl;
return EXIT_SUCCESS;
}
```

#1 ex\\protect deyimini bir önceki terimden giderek hesaplayan program.

## **Newton-Raphson Yöntemiyle Polinom Kökü Bulunması**

Bir f(x) fonksiyonunun kökü, f(x)=0 koşulunu sağlayan x değeridir. Bu değere

| PRIVATE | x |  |
| --- | --- | --- |

dersek f(x) fonksiyonunun

| PRIVATE | x |  |
| --- | --- | --- |

civarında Taylor açılımının ilk iki terimi şöyle yazılabilir

| PRIVATEf( | x | )=f(xi)+( | x | −xi)f′(xi) |  |
| --- | --- | --- | --- | --- | --- |

Bu değer 0 olması gerektiğinden denklem

| PRIVATEf(xi)+( | x | −xi)f′(xi)=0 |  |
| --- | --- | --- | --- |

ve buradan da

| PRIVATE | x | =xi− | f(xi) f′(xi) |  |  |
| --- | --- | --- | --- | --- | --- |

yazılabilir. Bu formülde

| PRIVATE | x |  |
| --- | --- | --- |

yerine xi+1 konursa, fonksiyonun kökü ardışıl yerine koyma yöntemiyle hesaplanabilir. Yani her adımda o adımdaki x değeri formüldeki xi değerinin yerine konarak bir sonraki adımda kullanılacak x değeri hesaplanır.

Bu yöntemin p(x)=anxn+an−1xn−1+…+a1x+a0 şeklinde n. dereceden bir polinoma uygulandığını varsayalım. O halde yineleme formülü

| PRIVATExi+1=xi− | p(xi) p′(xi) |  |  |
| --- | --- | --- | --- |

olacaktır. Bu formüldeki p(xi) değerinin hesaplanması için

| PRIVATE | n(n+1) 2 |  |
| --- | --- | --- |

adet çarpma ve n adet toplama işlemi gerecektir14. İçiçe çarpma ve toplama yöntemiyle bu sayı azaltılabilir:

Bir b dizisinin elemanları şu şekilde hesaplansın:

| PRIVATEbn | PRIVATE= | PRIVATEan |  |
| --- | --- | --- | --- |
| PRIVATEbn−1 | PRIVATE= | PRIVATEbnxi+an−1 |  |
| PRIVATEbn−k | PRIVATE= | PRIVATEbn−k+1xi+an−k |  |

Böyle gidilerek yapılan hesaplama sonucunda elde edilecek b0 değeri hesaplanmak istenen p(xi) değeri olacaktır (Neden?). Yapılması gereken işlem sayısı da n çarpma ve n toplamaya iner.

Benzer bir hesap da p′(xi) değerinin bulunmasında kullanılabilir.

| PRIVATEp′(x)=bnxn−1+bn−1xn−2+…+b2x+b1 |
| --- |

şeklinde yazılabilir (Neden?). O halde:

| PRIVATEcn | PRIVATE= | PRIVATEbn |  |
| --- | --- | --- | --- |
| PRIVATEcn−1 | PRIVATE= | PRIVATEcnxi+bn−1 |  |
| PRIVATEc1 | PRIVATE= | PRIVATEc2xi+b1 |  |

Bu yöntemi kullanarak katsayılarını kullanıcının girdiği bir polinomun köklerini hesaplayan program Örnek 17'de verilmiştir.

```cpp
#include <iostream.h> // cout,cin
#include <stdlib.h> // EXIT_SUCCESS
#include <math.h> // fabs
float newton_raphson(float x, const float a[], int n);
int main(void)
{
float *a;
int n, i;
float xi, xj, error;
cout << "Polinomun derecesi: "; cin >> n;
a = new(float[n+1]);
for (i = n; i >= 0; i--)
{
cout << "a" << i << ": ";
cin >> a[i];
}
cout << "Hata: "; cin >> error;
cout << "x0: "; cin >> xi;
while (true)
{
xj = newton_raphson(xi, a, n);
if (fabs(xj - xi) < error)
break;
xi = xj;
}
cout << "Kök: " << xj << endl;
delete a;
return EXIT_SUCCESS;
}
float newton_raphson(float x, const float a[], int n)
{
float *b, *c;
float xn;
int i;
b = new(float[n+1]);
c = new(float[n+1]);
b[n] = a[n];
c[n] = b[n];
for (i = n - 1; i > 0; i--)
{
b[i] = b[i+1] * x + a[i];
c[i] = c[i+1] * x + b[i];
}
b[0] = b[1] * x + a[0];
xn = x - b[0] / c[1];
delete b;
delete c;
return xn;
}
```

#1 Polinom kökü hesaplayan fonksiyon.

**Appendix E
Örnek Programların C Dili Karşılıkları**

```c
/* İlk C programım. *
* *
* Bu program ekrana "Merhaba dünya!" iletisini yazar. */
#include <stdio.h> /* printf için */
#include <stdlib.h> /* EXIT_SUCCESS */
int main(void)
{
printf("Merhaba dünya!\n");
return EXIT_SUCCESS;
}
```

#1Ekrana bir satırlık ileti çıkaran program (Örnek 1).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS */
#define PI 3.14
#define sqr(x) ((x) * (x))
int main(void)
{
float radius;
float circum, area;
printf("Dairenin yarıçapını yazın: ");
scanf("%f", &radius);
circum = 2 * PI * radius;
area = PI * sqr(radius);
printf("Çevre: %f\n", circum);
printf("Alan: %f\n", area);
return EXIT_SUCCESS;
}
```

#1Bir dairenin çevresini ve alanını hesaplayan program (Örnek 2).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS,srand,rand,RAND_MAX */
#include <time.h> /* time */
int main(void)
{
int count, i;
float number;
int heads = 0, tails = 0;
printf("Kaç kez atılacak? "); scanf("%d", &count);
srand(time(NULL));
for (i = 1; i <= count; i++)
{
number = (float) rand() / RAND_MAX;
if (number < 0.5)
{
heads++;
}
else
{
tails++;
}
}
printf("Yazı sayısı: %d\n", tails);
printf("Tura sayısı: %d\n", heads);
return EXIT_SUCCESS;
}
```

#1Yinelemeli yazı-tura atışı simülasyonu yapan program (Örnek 3).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS,exit */
int main(void)
{
int num1, num2, result;
char op;
printf("İşlemi yazın: "); scanf("%d %c %d", &num1, &op, &num2);
switch (op)
{
case '+': result = num1 + num2;
break;
case '-': result = num1 - num2;
break;
case '*': result = num1 * num2;
break;
case '/': result = num1 / num2;
break;
case '%': result = num1 % num2;
break;
default: printf("Böyle bir işlem yok.\n");
exit(EXIT_FAILURE);
}
printf("%d %c %d işleminin sonucu: %d\n", num1, op, num2, result);
return EXIT_SUCCESS;
}
```

#1Kullanıcının belirttiği işlemi yapan program (Örnek 4).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS */
int main(void)
{
int num1, num2, tmp;
printf("Sayıları yazın: "); scanf("%d %d", &num1, &num2);
while (num1 > 0)
{
if (num1 < num2)
{
tmp = num1;
num1 = num2;
num2 = tmp;
}
num1 = num1 - num2;
}
printf("En büyük ortak bölen: %d\n", num2);
return EXIT_SUCCESS;
}
```

#1İki sayının en büyük ortak bölenini bulan program (Örnek 5).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS */
int main(void)
{
int number1, number2;
int max, min, i;
long int lcm;
printf("1. Sayı: "); scanf("%d", &number1);
printf("2. Sayı: "); scanf("%d", &number2);
max = number1 > number2 ? number1 : number2;
min = number1 < number2 ? number1 : number2;
for (i = 1; (max * i) % min != 0; i++)
;
lcm = max * i;
printf("En küçük ortak kat: %ld\n", lcm);
return EXIT_SUCCESS;
}
```

#1İki sayının en küçük ortak katını bulan program (Örnek 6).

```cpp
#include <stdio.h> /* cout,cin */
#include <stdlib.h> /* EXIT_SUCCESS */
#include <math.h> /* pow */
#define TRUE 1
int main(void)
{
float x, error, term, result = 1.0;
int i = 1, f;
float fact;
printf("x: "); scanf("%f", &x);
printf("Hata: "); scanf("%f", &error);
while (TRUE)
{
fact = 1.0;
for (f = 2; f <= i; f++)
fact *= f;
term = pow(x, i) / fact;
result += term;
if (term < error)
break;
i++;
}
printf("Sonuç: %f\n", result);
return EXIT_SUCCESS;
}
```

#1 ex\\protect deyimini genel terimden giderek hesaplayan program (Örnek 7).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS */
#include <math.h> /* sqrt */
#define MAXSTUDENTS 100
#define sqr(x) ((x) * (x))
int main(void)
{
int grades[MAXSTUDENTS];
int nstudents, i;
float mean, variance = 0.0, deviation;
int total = 0;
printf("Öğrenci sayısı: "); scanf("%d", &nstudents);
for (i = 0; i < nstudents; i++)
{
printf("%d. öğrencinin notu: ", i + 1); scanf("%d", grades[i]);
total += grades[i];
}
mean = (float) total / nstudents;
for (i = 0; i < nstudents; i++)
variance += sqr(grades[i] - mean);
deviation = sqrt(variance / (nstudents - 1));
printf("Ortalama: %f\n", mean);
printf("Varyans: %f\n", variance);
printf("Standart Sapma: %f\n", deviation);
return EXIT_SUCCESS;
}
```

#1Ortalama, varyans ve standart sapma hesaplayan program (Örnek 8).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS */
#include <string.h> /* strlen */
int main(void)
{
char word[30];
int len, i;
char tmp;
printf("Sözcük: "); scanf("%s", word);
len = strlen(word);
for (i = 0; i < len / 2; i++)
{
tmp = word[i];
word[i] = word[len - 1 - i];
word[len - 1 - i] = tmp;
}
printf("Tersi: %s\n", word);
return EXIT_SUCCESS;
}
```

#1Sözcüğü tersine çeviren program (Örnek 10).

```cpp
#include <stdio.h> /* cout,cin */
#include <stdlib.h> /* EXIT_SUCCESS */
int main(void)
{
int m1[30][20];
int m2[20][30];
int pr[30][30] = { 0 };
int r1, c1, r2, c2;
int i, j, k;
printf("Sol matrisin satır sayısı: "); scanf("%d", &r1);
printf("Sol matrisin sütun sayısı: "); scanf("%d", &c1);
printf("Sağ matrisin sütun sayısı: "); scanf("%d", &c2);
r2 = c1;
printf("Sol matris:\n");
for (i = 0; i < r1; i++)
for (j = 0; j < c1; j++)
{
printf(" [%d,%d]: ", i + 1, j + 1);
scanf("%d", &m1[i][j]);
}
printf("Sağ matris:\n");
for (j = 0; j < r2; j++)
for (k = 0; k < c2; k++)
{
printf(" [%d,%d]: ", j + 1, k + 1);
scanf("%d", &m2[j][k]);
}
for (i = 0; i < r1; i++)
for (j = 0; j < c2; j++)
for (k = 0; k < c1; k++)
pr[i][j] += m1[i][k] * m2[k][j];
printf("Sonuç:\n");
for (i = 0; i < r1; i++)
{
for (k = 0; k < c2; k++)
printf(" %d ", pr[i][k]);
printf("\n");
}
return EXIT_SUCCESS;
}
```

#1İki matrisi çarpan program (Örnek 9).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS */
#include <math.h> /* sqrt */
typedef enum { FALSE, TRUE } bool;
int next_prime(int prime);
int main(void)
{
int number, factor;
printf("Sayı: "); scanf("%d", &number);
factor = 2;
while (number > 1)
{
while (number % factor == 0)
{
printf("%d ", factor);
number /= factor;
}
factor = next_prime(factor);
}
printf("\n");
return EXIT_SUCCESS;
}
bool is_prime(int cand)
{
int count;
if (cand == 2)
return TRUE;
if (cand % 2 == 0)
return FALSE;
for (count = 3; count <= sqrt(cand); count += 2)
{
if (cand % count == 0)
return FALSE;
}
return TRUE;
}
int next_prime(int prime)
{
int cand = (prime % 2 == 0) ? prime + 1 : prime + 2;
while (!is_prime(cand))
cand += 2;
return cand;
}
```

#1Bir sayıyı asal çarpanlarına ayıran program (Örnek 11).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS,malloc,free */
#define MAXSTUDENTS 50
void selsort(int arr[], int size);
void swap(int *x, int *y);
int main(void)
{
int grades[MAXSTUDENTS];
int nstudents, i;
float median;
printf("Öğrenci sayısı: "); scanf("%d", &nstudents);
for (i = 0; i < nstudents; i++)
{
printf("%d. öğrencinin notu: ", i + 1); scanf("%d", &grades[i]);
}
selsort(grades, nstudents);
median = (nstudents % 2 == 1) ?
```

grades\[nstudents/2\] :

```c
(grades[nstudents/2] + grades[nstudents/2-1]) / 2.0;
printf("Ortadeğer: %f\n", median);
free(grades);
return EXIT_SUCCESS;
}
void selsort(int arr[], int size)
{
int round, max, i;
for (round = 0; round < size - 1; round++)
{
max = 0;
for (i = 1; i < size - round; i++)
if (arr[max] < arr[i])
max = i;
swap(&arr[max], &arr[size-1-round]);
}
}
void swap(int *x, int *y)
{
int tmp = *x;
*x = *y;
*y = tmp;
}
```

#1Öğrenci notlarının ortadeğerini bulan program (Örnek 12).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS,atof */
#define PI 3.14
#define sqr(x) ((x) * (x))
int main(int argc, char *argv[])
{
float radius;
float circum, area;
if (argc == 1)
{
fprintf(stderr, "Komut satırında bir yarıçap belirtmelisiniz.\n");
return EXIT_FAILURE;
}
else if (argc > 2)
{
fprintf(stderr, "Komut satırında fazla parametre var.\n");
return EXIT_FAILURE;
}
radius = atof(argv[1]);
circum = 2 * PI * radius;
area = PI * sqr(radius);
printf("Çevre: %f\n", circum);
printf("Alan: %f\n", area);
return EXIT_SUCCESS;
}
```

#1Öğrenci notlarının ortadeğerini bulan program (Örnek 13).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS */
struct complex_s
{
float re;
float im;
};
typedef struct complex_s complex_t;
complex_t add_complex(complex_t c1, complex_t c2);
int main(void)
{
complex_t n1, n2, n3;
printf("Birinci sayıyı yazın: "); scanf("%f %f", &n1.re, &n1.im);
printf("İkinci sayıyı yazın: "); scanf("%f %f", &n2.re, &n2.im);
n3 = add_complex(n1, n2);
printf("Toplam: %f + %fi\n", n3.re, n3.im);
return EXIT_SUCCESS;
}
struct complex_s add_complex(struct complex_s c1, struct complex_s c2)
{
complex_t c3;
c3.re = c1.re + c2.re;
c3.im = c1.im + c2.im;
return c3;
}
```

#1Karmaşık sayılar üzerinde işlem yapan program (Örnek 14).

```cpp
#include <stdio.h> /* cout,cin *
#include <stdlib.h> /* EXIT_SUCCESS *
#define TRUE 1
int main(void)
{
float x, error, term, result = 1.0;
int i = 2;
printf("x: "); scanf("%f", &x);
printf("Hata: "); scanf("%f", &error);
term = x;
while (TRUE)
{
result += term;
term = term * x / i;
if (term < error)
break;
i++;
}
printf("Sonuç: %f\n", result);
return EXIT_SUCCESS;
}
```

#1 ex\\protect deyimini bir önceki terimden giderek hesaplayan program (Örnek 16).

```cpp
#include <stdio.h> /* cout,cin */
#include <stdlib.h> /* EXIT_SUCCESS,srand,rand,RAND_MAX */
#include <time.h> /* time */
int main(void)
{
int game_status, point;
int die1, die2, sum;
srand(time(NULL));
die1 = 1 + rand() % 6;
die2 = 1 + rand() % 6;
sum = die1 + die2;
printf("Gelen: %d + %d = %d\n", die1, die2, sum);
switch (sum)
{
case 7:
case 11:
game_status = 1; break;
case 2:
case 3:
case 12:
game_status = 2; break;
default:
game_status = 0;
point = sum;
printf("Sayı: %d\n", sum);
break;
}
while (game_status == 0)
{
die1 = 1 + rand() % 6;
die2 = 1 + rand() % 6;
sum = die1 + die2;
printf("Gelen: %d + %d = %d\n", die1, die2, sum);
if (sum == point)
game_status = 1;
else
{
if (sum == 7)
game_status = 2;
}
}
if (game_status == 1)
printf("Oyuncu kazanır.\n");
else
printf("Oyuncu kaybeder.\n");
return EXIT_SUCCESS;
}
```

#1Barbut oyununu simüle eden program (Örnek 15).

```c
#include <stdio.h> /* printf,scanf */
#include <stdlib.h> /* EXIT_SUCCESS,malloc,free */
#include <math.h> /* fabs */
#define TRUE 1
float newton_raphson(float x, const float a[], int n);
int main(void)
{
float *a;
int n, i;
float xi, xj, error;
printf("Polinomun derecesi: "); scanf("%d", &n);
a = (float *) malloc((n+1) * sizeof(float));
for (i = n; i >= 0; i--)
{
printf("a%d: ", i); scanf("%f", &a[i]);
}
printf("Hata: "); scanf("%f", &error);
printf("x0: "); scanf("%f", &xi);
while (TRUE)
{
xj = newton_raphson(xi, a, n);
if (fabs(xj - xi) < error)
break;
xi = xj;
}
printf("Kök: %f\n", xj);
free(a);
return EXIT_SUCCESS;
}
float newton_raphson(float x, const float a[], int n)
{
float *b, *c;
float xn;
int i;
b = (float *) malloc((n+1) * sizeof(float));
c = (float *) malloc((n+1) * sizeof(float));
b[n] = a[n];
c[n] = b[n];
for (i = n - 1; i > 0; i--)
{
b[i] = b[i+1] * x + a[i];
c[i] = c[i+1] * x + b[i];
}
b[0] = b[1] * x + a[0];
xn = x - b[0] / c[1];
free(b);
free(c);
return xn;
}
```

#1Polinom kökü hesaplayan fonksiyon (Örnek 17).

**Appendix F
Unix'de Program Geliştirme**

**Yardımcı Belgeler ******

Unix işletim sistemlerinde çoğu zaman man *fonksiyon* komutuyla o fonksiyonla ilgili bilgi alabilirsiniz. Bu komut fonksiyonun ne iş yaptığını ve hangi başlık dosyasında yer aldığını söyleyecektir. Örnek: man printf.

info

## **Footnotes:**

1Bu yapı, bloğun işlenmesi bittikten sonra koşulun sınandığı noktaya geri dönmeyi sağlayan bir goto komutu gerektiriyor gibi görünmekle birlikte, yapısal programlamada yineleme için özel yapılar vardır ve goto komutunun kullanılmaması özendirilir. Bu konuyla ilgili olarak, Edsger W. Dijkstra'nın \`\`Go To Statement Considered Harmful'' başlıklı klasik makalesini "http://www.acm.org/classics/oct95/"adresinde bulabilirsiniz.

2Niklaus Wirth'ün bu konuda yazmış olduğu \`\`Program Development by Stepwise Refinement'' başlıklı klasik makalesini "http://www.acm.org/classics/dec95/" adresinde bulabilirsiniz.

3bkz. Ek .

4bkz. Ek .

5bkz. Ek .

6bkz. Ek .

7bkz Ek

8bkz. Ek .

9bkz. Ek .

10bkz. Ek

11bkz. Ek .

12bkz. Ek

13bkz. Ek .

14 p′(xi) için kaçar tane çarpma ve toplama gerekir?

File translated from TEX by TTH, version 2.92.
On 1 Jun 2001, 20:35.

---
*Kaynak: `C DERS NOTLARI/C DERS NOTLARI.doc` — Ahmet Can Kutlu — 2004*
