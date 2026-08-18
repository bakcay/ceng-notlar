# Hedef Programlama

**1. ÇOK AMAÇLI KARAR VERME**

Karar problemlerinin çözümünde çoğunlukla optimal çözüm değeri elde edilmeye çalışılır. İşletmecilik problemlerinde kar maksimizasyonu optimal bir sonucu oluştururken, maliyet minimizasyonu da ayrı bir optimal sonuç oluşturmaktadır. Doğrusal Programlamada amaç kar maksimizasyonu ya da maliyet minimizasyonu olarak ifade edilmektedir. Oysa gerçek hayattaki karar problemlerinde tek bir amaç bulunmaz. Çünkü gerek kişiler gerekse kurumlar aynı anda birden çok amaca sahip olabilir. Örneğin fabrika yeri seçilirken, şüphesiz ki maliyet minimizasyonu önemli bir amaçtır. Fakat bu amacın yanında kar maksimizasyonu, işgücüne yakınlık,ulaşım kolaylığı, pazar ve enerji kaynaklarına yakınlık amaçları da vardır. Ancak bir çok açıdan çelişen hedefler içeren böyle bir problemin tüm kriterlerinin aynı anda gerçekleşmesi oldukça güçtür. Bu tür problemlerin çözümünde çok amaçlı karar verme teknikleri kullanılır. Bu yöntemlerden biri olan çok amaçlı hedef programlama aşağıda açıklanmıştır.

**2. HEDEF PROGRAMLAMA**

Uygulamada karşılaşılan sistemler birden çok amaca sahip olabilir. Tek amaç optimizasyonuna çalışan doğrusal programlamanın yetersiz kaldığı bu durumlarda, hedef programlama kullanılır. Hedef programlama hedef kısıtlarının yapısına göre lineer ve non-lineer olarak iki başlık altında incelenebilir. Bu projede sadece lineer hedef programlamaya değinilecektir.

Hedef programlamanın temel ilkesi şudur: Karar vericiden her bir amaç için ulaşılması istenen hedef değerler belirlenmesi istenir. Bu hedef değerlerden sapmaları minimize eden bir çözüm bulunur. Bu hedefler birbiriyle çelişebilir. Örneğin, hırslı politikacılar hem iç borcu azaltmayı, hem de gelir vergisi oranını azaltmayı hedefleyebilir. Böyle durumlarda, çelişen amaçları optimumu kılan tek bir çözüm bulmak olanaksız olabilir. Bunun yerine, her amacın önem derecesini temel alan uzlaşık çözümler bulunabilir.

Hedef programlama aşağıda yazılı olan özel terminolojiyi kullanır.

**Amaç:*** *Kullanıcı tarafından belirlenen genel nitelik (gelirin artırılması, pazar payını korunması gibi)

**Hırs seviyesi:** Karar veren kişinin ortaya koyduğu hedefin sayısal değeri (5000 dolar haftalık gider, % 15 Pazar payı)

**Sapma:**Çözümle sağlanan gerçek performans seviyesi ile modelde belirlenen amaç arasındaki fark.

**Öncelik:*** *Kullanıcı tarafından amaç fonksiyonları için belirlenen önem sırası

**Karar değişkenleri*****:**** *Karar vermek için araştırdığımız bilinmeyenler kümesi.

**Sağ taraf sabitleri:*** *Kaynak değerlerini ifade eden değerlerdir.

**Hedef:*** *Belirlenmiş bir hedef kısıtı içinde belirlenmiş sağ taraf sabiti değerinden sayısal sapmayı en küçükleme isteğidir.

**Öncelikli üstünlük faktörü:*** *Hedef programlama modelinde, hedeflerin düzenli bir şekilde yapılanmasını sağlayan bir sıralama sistemidir. (Pk ile gösterilir, k=1,2,.....K, K, modeldeki hedeflerin sayısıdır . ) Amaç fonksiyonunun oluşturulabilmesi için en önemliden daha az önemliye sıralanan hedefler,ilk önce birinci öncelikli hedefin karşılanmasını daha sonra sırayla diğer hedeflerin karşılanmasını gerektirir. Bu durum şu ilişki ile gösterilebilir:

(En önemli hedef) P1>>>P2>>> Pk (En az önemli hedef)

**Sapma değişkenleri:*** *Hedef kısıtının sağ taraf sabitlerinden pozitif veya negatif sapma olabilme imkanını ifade eden değişkenlerdir. i=l, 2,......1 için di- ve di+ ile gösterilirler. Bu değişkenler doğrusal programlama modelindeki aylak değişkenlerle aynı gibi düşünülebilir.

**Diferansiyel ağırlık:*** *k. seviyede i. hedeften oluşan sapmaya ilişkin matematiksel ağırlık olarak ifade edilir. Wki ile gösterilir.

**2.1. Hedef Programlamanın İlkeleri**

Hedef programlama her bir amaç bir hedef olarak kabul edilir.

Hedef programlamada hedeflerin gerçekleştirilmesinde öncelikler dikkate alınır. Önce birinci öncelik düzeyindeki hedefler daha sonra ikinci öncelik düzeyindeki hedefler gerçekleştirilir. Sıra atlamadan bütün hedefler tamamlanana kadar devam edilir.

di- i. hedefin altında kalınması durumunu, di+ hedefin aşılması durumunu gösterir.

Hedef düzeyleri dikkate alınarak hedeflerden toplam sapma minimize edilmeye çalışılır. Öncelikle birinci öncelikli hedefler için problemin çözümü belirlenir. Daha sonra bu çözümü ihmal etmeyen ikinci düzey hedeflere ait çözüm belirlenir. Aynı şekilde diğer hedefleri olabildiğince sağlayan ve önceki hedefleri ihmal etmeyen çözümler belirlenir.

**2.2. Hedef Programlamanın Formülasyonu**

Hedef programlamanın genel formülasyonu şu şekildedir.

Amaç Fonksiyonu:

Min \[ di-+di+)a\]1/a a=1

Kısıtlar:

gk(x)≤0, k=1,2,…,p

fi(x)+di--di+=bi, i=1,2,…,m

di-,di+≥0, i

di-,di+=0, i

Burada bi, i=1,2,…,m karar verici tarafından amaçlar için belirlenmiş hedef değerleridir. di- ve di+ ler i’ inci hedeften eksi(-) ve artı(+) sapmaları göstermektedir. Karar vericinin değer fonksiyonuna, D(x), bağlıdır.

Hedef programlama formülasyonunun en yaygın kullanılan şekli, karar vericinin, amaçlar için hedef değerler belirlemesine ilave olarak, amaçların önem derecelerine göre sıralanması ile ilgili sözlü bilgiyi verebileceğini de kabul etmektedir. Bu halde hedef programlama formülasyonu şu şekli almaktadır.

Min \[P1h1(d-,d+), P2h2(d-,d+),…Pjhj(d-,d+)\]

gk(x)≤0, k=1,2,…,p

fi(x)+di--di+=bi, i=1,2,…,m

di-,di+≥0, i

di-,di+=0, i

Burada hj (d-,d+) j=1,2,…, l sapma değişkenlerinin lineer fonksiyonları olup, başarma fonksiyonları adıyla anılırlar. Burada Pj’ler boş-gölge ağırlıklarıdır ve Pj>>>Pj+1 bunun anlamı, Pj, Pj+1 den çok daha büyük olup, W+Pj+1>Pj yapacak, hiçbir büyük W sayısının olmadığı kabul edilir.

**Örnek 2.1**

Ace Electorincs lcn. iki tip stereo teyp imal etmektedir. Bunlardan “Deluxe” tip modeli üretmek için montaj hattında 1 saat çalışılmakta, “Supreme” için ise iki saat çalışılmaktadır. Normal montaj hattı faaliyeti haftada 40 saat ile sınırlıdır. Pazarlama çalışmaları haftada 30 Deluxe ve 15 Supreme stereo teypten fazla üretilmemesi gerektiğini göstermiştir. Deluxe modelinin her biri için 8 pb, Supreme modelimin her biri için ise 12 pb net kar elde edilmektedir.

Şirket genel müdürü öncelikler için aşağıdaki amaçları belirlemiştir:

Toplam karı maksimize etmek.

Montaj hattındaki fazla mesai zamanını minimize etmek.

Mümkün olduğu kadar fazla stereo teyp satmak. (Bunun kar maksimizasyonu ile aynı olması gerekmez.)

**Çözüm:**

x1 = Her hafta üretilecek Deluxe sayısı,

x2 = Her hafta üretilecek Supreme sayısı,

Z max = 8x1 + 12x2

A.K.A.

x1 + 2x2 ≤ 40

x1 ≤ 30

x2 ≤ 15

Problemin hedef programlama şeklinde formülasyonu şu şekilde yapılır:

**Karlılık hedefi:** Şirket genel müdürü toplam karı maksimize etmek istemektedir. Bu değer keyfi olarak haftada 100 pb kabul edilmiştir.

G1: 8x1 + 12x2 + d1- - d1+ = 100

d1- \*d1+ = 0

1) d1- = d1+ = 0

2) d1- > 0, d1+ = 0

3) d1- = 0, d1+ > 0

Min G1 = d1-

Burada d1- hedefin altındaki sapma değeri, d1+ hedefin üstündeki sapma değeridir.

**Fazla mesai hedefi:**

G2: x1 + 2x2 + d2- - d2+ = 40

d2- \* d2+ = 0

Burada d2+ fazla mesai süresini gösterirken d2- işçilik kapasitesinin altındaki kullanım miktarını yani gevşek zamanı gösterir. Amaç fazla mesaiyi minimize etmek olduğundan ikinci hedef şu şekilde ifade edilir.

Min G2 = d2+

**Pazarlama hedefi:** pazarlama departmanınca belirlenen talep miktarlarına ulaşılmaya çalışılır ve amacımız şu şekilde ifade edilir.

G3’ : x1 + d3- - d3+ = 30

G3” : x2 +d4- - d4+ = 15

d3- \* d3+ = 0

d4- \* d4+ = 0

Mümkün olduğu kadar çok stereo satmak istiyorsak d3-, d4- sapmalarının minimize edilmesi gerekir.

Min G3’ = d3-

Min G3” = d4-

**2.3. Hedef Programlama Algoritmaları**

Örnekte de olduğu gibi çelişen hedefler olabilir. Bu durumda uzlaşık bir çözüm aranır. Bu uzlaşık çözümü bulmada kullanılan iki değişik hedef programlama algoritması vardır. Her iki yöntem de çok sayıda amaç fonksiyonunun tek bir amaç fonksiyonu şeklinde ifade edilmesine dayanır. Birleştirilmiş bu amaç fonksiyonuna ise başarma fonksiyonu denir.

**2.3.1 Ağırlıklandırma Yöntemi **

Bu yöntemde belirlenen hedeflere önem düzeylerine göre ağırlık puanları atanarak hedefler tek bir amaç fonksiyonu olarak ifade edilir. n hedefli bir hedef programlama modelinin ağırlıklandırma yöntemi kullanılarak oluşturulmuş amaç fonksiyonu;

Min Z= w1G1+ w2G2+...+ wnGn

şeklinde tanımlanır. Burada wi, i=1,2...,n, her bir hedefe karar vericinin verdiği önemi yansıtan pozitif ağırlıklardır. wi değerleri çoğunlukla öznel yöntemlerle belirlenmektedir. Bu değerleri saptamakta kullanmak amacıyla geliştirilmiş analitik prosedürler de mevcut olup; bu prosedürlerde de öznel değerlendirmeler temel alınmıştır.

**Örnek 2.2 **** ******

Reklamevi, 10 çalışanı olan yeni bir reklam ajansıdır. Ajans yeni bir ürünün reklam kampanyasını üstlenmiştir. Ajans reklam kampanyasını radyo ve televizyon

aracılığıyla yapabilmektedir. Aşağıdaki tablo, her bir reklam türü (TV ya da radyo reklamı) ile ulaşılacak insan sayısını, ayrıca maliyeti ve işgücü gereksinimlerini göstermektedir.

** Tablo 2.1. Reklamevi verileri **

|  | Reklamın dakikası başına veri |  |
| --- | --- | --- |
| Radyo | TV |  |
| Ulaşılan kişi sayısı Maliyet (1000 pb) Gereken çalışan sayısı | 4 8 1 | 8 24 2 |

Reklamevi’nin firmayla yaptığı sözleşmede, radyo reklamının 6 dakikadan uzun olamayacağı şeklinde bir madde bulunmaktadır. Buna ek olarak, radyo ve televizyon reklamlarının en az 45 milyon kişiye ulaşması istenmektedir. Reklamevi bu kampanya için 100000 pb’lik bir bütçe ayırmıştır. Reklamevi radyo ve televizyonda kaçar dakikalık reklam yapmalıdır?

**Çözüm:**

Karar ortamından kaynaklanan kısıtların ifadesinde iki değişik uygulama vardır. Birincisi kısıtların direkt fonksiyonel kısıt olarak kabul edilmesi, ikincisi bu kısıtların mutlak hedef olarak kabul edilmesidir. Burada bu kısıtlar mutlak hedef olarak alınacaktır.

x1= Radyo reklamına ayrılan dakika

x2= Televizyon reklamına ayrılan dakika

G1: ulaşılmak istenen kişi sayısı şu şekilde ifade edilir:

G1: 4x1+8x2+d1--d1+= 45

Min G1= d1-

G2: Bütçe hedefinin ifadesi aşağıdaki gibidir.

G2: 8x1+24x2+d2--d2+= 100

Min G2= d2+

Karar ortamından kaynaklanan kısıtlar şunlardır:

x1+2x2≤ 10

x1 ≤ 6

x1, x2, d1-,d1+, d2 -, d2+≥ 0

Reklamevi yöneticileri ulaşılan kişi hedefini bütçe hedefinden iki kat daha önemli olduğunu düşünmektedir. Bu durumda başarma fonksiyonu şu şekilde ifade edilir.

Min a= {2G1+G2}={2d1-+ d2+}

A.K.A

4x1+ 8x2+d1--d1+ = 45

8x1+24x2+d2--d2+= 100

x1+2x2 ≤ 10

x1 ≤ 6

x1, x2, d1-,d1+, d2 -, d2+≥ 0

**Problemin grafik çözümü:**

4x1+ 8x2=45 (1) (0, 5,625),(11,25, 0)

8x1+24x2=100 (2) (0, 4,167),(12,5, 0)

x1+2x2 =10 (3) (0, 5),(10, 0 )

x1 =6 (4) (x1=6)

Şekil 2.1. Reklamevi grafiği

3 ve 4 numaralı karar ortamı kısıtlarından dolayı çözüm ACFG yamuk alanı dışında oluşamaz. Bu nedenle G1’ den mutlaka sapma olduğu görülmektedir. Fakat d2+ sıfır(0) değerini alabilir. Uzlaşık çözümümüz 2d1-+d2+ değerini minimize eden değerler kümesidir. Bu durumda d1- nin minimum değeri bulunur. Bu değer 1. amaç doğrusuna paralel olan DF doğru parçasının yine bu amaç fonksiyonuna olan uzaklığıdır.

D noktası 2 ve 3 denkleminin birlikte çözümünden (5,2.5) bulunur.

4x1+8x2+d1—d1+=45

d1- =5 d1+= 0

8x1+ 24x2+d2--d2+=100

d2- =0 d2+ =0

Min a = 2\*5+0 = 10

F noktası için denenirse;

x1+2x2=10

x1 =6

İki denklemin çözümünden F(6,2) bulunur.

4x1+8x2+d1--d1+=45

d1- =5 d1+ =0

8x1+24x2+d2--d2+=100

d2- =4 d2+=0

Min a= 2d1-+d2+=10

Görüldüğü gibi uzlaşık çözüm DF doğru parçasıdır. DF’ nin üzerine çıkılmasını kısıtlar engeller. Altına inildiğinde d1- değeri artmaktadır. Her iki durumda da uzlaşık çözüm dışına çıkılmaktadır.

**Simpleks Yöntemle Çözümü:******

Lineer hedef programlamanın çözümünde kullanılan simpleks yöntem, klasik lineer programlamada kullanılan simpleksin geliştirilmiş halidir. Bilindiği gibi simpleks yöntem iteratif bir süreç kullanarak optimum çözüme götüren algoritmik bir metottur.* ***

**Tablo 2.2. Reklamevi sonuç tablosu **

```text
Program: Goal Programming
Problem Title : Reklamevi

***** Input Data *****

Min Z = 2P1d-3 + 1P1d+4

Subject to

çalışan 1X1 + 2X2 <= 10
radyo 1X1 <= 6
u. kişi 4X1 + 8X2 + d-3 - d+3 = 45
bütçe 8X1 + 24X2 + d-4 - d+4 = 100

***** Program Output *****

Analysis of deviations
------------------------------------------------
Constraint RHS Value d+ d-
------------------------------------------------
çalışan 10.000 0.000 0.000
radyo 6.000 0.000 1.000
u. kişi 45.000 0.000 5.000
bütçe 100.000 0.000 0.000
-------------------------------------------------

Analysis of decision variables
------------------------------------
Variable Solution Value
------------------------------------
X1 5.000
X2 2.500
------------------------------------

Analysis of the objective function
----------------------------------
Priority Nonachievement
----------------------------------
P1 10.000
----------------------------------

***** End of Output *****
```

Simpleks yöntemle çözüm x1=5 ve x2=2.5 noktalarında gerçekleşmiştir. Bu çözüme göre ulaşılan kişi sayısı 40 milyondur. Hedeflenen değerden 5 milyon daha az kişiye ulaşılmıştır. Bütçe hedefinden ise sapma yoktur. Hedeflenen bütçenin tamamı kullanılmıştır.

Görüldüğü gibi grafik çözümde çözüm kümesi DF doğru parçası iken simpleks çözüm D noktasında gerçekleşmiştir. Çünkü simpleks yöntem noktasal bir çözüm verir. Yani uzlaşık çözüm noktalarından sadece birini alır.

Çözümlerden görüldüğü gibi ulaşılan kişi hedefinden mutlaka sapma vardır. Acaba 40 milyon kişiye daha az maliyetle ulaşılamaz mı? sorusuna cevap arandığında, grafik çözümde görülen F(6,2) noktasında maliyetin 96000 pb olduğu görülmektedir. Örnekten de anlaşıldığı gibi hedef programlama belirlenen hedeflere göre uzlaşık bir çözüm verir. Optimum çözüme ulaşmadaki bu yetersizliği, hedef programlamanın bir optimizasyon tekniği olarak uygulanabilirliği konusunda sorular uyandırmaktadır.

**2.3.2. Önceliği Koruma Yöntemi**

Hedeflerin karşılaştırılması sonunda göreceliği bir önem sırası ortaya çıktığında “Öncelikli Hedef Programlama” dan söz edilmektedir. Bu tür problemlerde hedefler karar vericinin değerlendirilmesine göre önem sırasına konur. i. hedefin (i+1). hedefe göre mutlak bir üstünlüğü vardır. Bu yöntemle problem çözümünde öncelikle 1. hedefin optimum çözümü bulunur. Daha sonra diğer hedeflerin optimum çözümü bulunur fakat bu çözümler bulunurken bir önceki hedefin çözümünün kötüleştirilmesine izin verilmez. n sayıdaki hedefin genel ifadesi şu şekilde tanımlanır.

Min G1=P1 (en yüksek öncelikli)

.

.

.

Min Gn=Pn (en düşük öncelik)

Pi>>>Pi+1

** Örnek 2.3. **(CP) firması CP 486 ve CP Pentium133 model bilgisayarlardan üretmektedir. Her iki bilgisayar için aynı tür kasa ve disket sürücülerden kullanılmaktadır. CP 486’da Harddisk’ in yanı sıra 3.5 inch’lik bir disket sürücü, CP Pentium133’te ise diğer modeldeki özelliklere ilave olarak bir de CD sürücü yer almaktadır. Kasa ve disket sürücüler ayrı firmalardan temin edilmektedir. CP firması, haftada 1000 adet disket sürücü, 500 adet Harddisk, 500 adet CD sürücü ve 600 kasa temin edebilmektedir CP 486’yı üretmek 1 saat alırken karlılığı 200 TL, buna karşılık CP Pentiuml33’ü üretmek 1.5 saat gerektirirken karlılığı 500 TL’ dir.

CP firması aşağıda belirtilen hedefleri tutturmaya çalışmaktadır.

P1: Haftada en az 200 adet CP 486 üretmek,

P2 : Haftada toplam en az 500 adet bilgisayar üretmek,

P3 : Haftada toplam en az 250.000 TL. kar sağlamak,

P4: Haftada 400 saat işgücünü aşmamak.

**Çözüm:**

x1: Haftada üretilen CP 486 adedi

x2: Haftada üretilen CP Pentium 133 adet

Fonksiyonel kısıtlar

x1+x2≤ 600 (kasa)

x1+x2≤ 500 (harddisk)

x2≤ 600 (CD sürücü)

x1+x2≤ 1000 (disket sürücü)

Hedefler

x1 ≥ 200 (CP 486)

x1+ x2≥ 500 (bilgisayar üretimi)

200x1+500x2≥ 250000 (karlılık)

x1+ 1,5x2≥ 400 (işgücü)

**Problemin hedef programlama modeli olarak ifadesi:**

G1: x1+d1--d1+ = 200

Min P1d1-

G2: x1+x2+d2--d2+ = 500

Min P1d1-, P2d2-

G3: 200x1+500x2+d3--d3+ = 250000

Min P1d1-, P2d2-, P3d3-

G4: x1+1,5x2+d4--d4+ = 400

Min P1d1-, P2d2-, P3d3-, P4d4+

**Başarma Fonksiyonu**

Min a= { P1d1-, P2d2-, P3d3-, P4d4+}

A.K.A.

x1+x2 ≤ 600

x1+x2 ≤ 500

x2 ≤ 600

x1+x2 ≤ 1000

x1 +d1--d1+ = 200

x1+x2 +d2--d2+ = 500

200x1+500x2 +d3--d3+ = 250000

x1+ 1,5x2 +d4--d4+ = 400

x1, x2, d1-, d1+, d2-, d2+, d3-, d3+, d4-,d4+ ≥0

Şekil 2.2. Bilgisayar probleminin grafik çözümü

karar ortamının kısıtlarından dolayı çözüm OAB üçgen alanı içinde olmak zorundadır. 1.öncelikli hedeften dolayı d1-‘yi minimize etmek zorunda olduğumuzdan çözüm d1-‘nin sıfır olduğu CEB alanı içindedir. 2. öncelikli hedef nedeniyle çözüm, d2-‘nin sıfır olduğu EB doğru parçası ile sınırlanır. 3. hedefin optimizasyonu için daha öncelikli hedeflerin çözümünü kötüleştirmeyecek ve d3-‘yi minimize edecek çözüm E(200, 300) noktasıdır. Bu noktada d2- değeri;

200x1+500x2+d3-- d3+= 250000

d3-= 60000

d3+= 0

olur. 4. hedefte pozitif sapma minimize edilmeye çalışılır. Daha öncelikli hedeflerin kötüleştirilmemesi için çözüm yine E noktasında kalır. Böylelikle 4. Hedeften sapma

x1+1,5x2+d4--d4+= 400

d4+= 250

olur. Yani 250 saat fazla mesai kullanılması gerekir.

**Problemin simpleks yöntemle çözümü **

Daha önce de belirtildiği gibi hedef programlamanın çözümünde geliştirilmiş simpleks yöntem kullanılır. Bu yöntem, sütün eleme kuralı denilen ve Gk+1 hedefi optimum kılınmadan önce Gk’nin optimum tablosundan Zj-Cj≠ 0 olan xj temel dışı değişkenini elemeyi gerektiren bir kural kullanır. Bu kural, izleyen hedeflerin optimizasyonunda sıfır(0) düzeyinin üzerine çıkıldığında yüksek öncelikli hedefin kalitesini kötüleştirebilecek (ama hiçbir zaman iyileştirmeyecek) bazı temel dışı değişkenleri saptar. Prosedür, simpleks tablonun modeldeki tüm hedeflere ait amaç fonksiyonlarını taşıyacak şekilde değiştirilmesini gerektirir.

Bu örnek 7 iterasyonda gerçekleştiğinden bilgisayar desteği alınmış, QM programı kullanılmıştır. Sütun eleme kuralının daha iyi anlaşılabilmesi için elle basit bir örnek çözülecektir.

**Tablo 2.3. Bilgisayar probleminin sonuç tablosu**

```text
Program: Goal Programming
Problem Title : bilgisayar

***** Input Data *****

Min Z = 1P1d-5 + 1P2d-6 + 1P3d-7 + 1P4d+8

Subject to

kasa 1X1 + 1X2 <= 600
harddisk 1X1 + 1X2 <= 500
cd surucu 1X2 <= 500
disket sur 1X1 + 1X2 <= 1000
cp 486 1X1 + d-5 - d+5 = 200
bilgisayar 1X1 + 1X2 + d-6 - d+6 = 500
karlilik 200X1 + 500X2 + d-7 - d+7 = 250000
isgucu 1X1 + 1.5X2 + d-8 - d+8 = 400

***** Program Output *****

Analysis of deviations
------------------------------------------------
Constraint RHS Value d+ d-
------------------------------------------------
kasa 600.000 0.000 100.000
harddisk 500.000 0.000 0.000
cd surucu 500.000 0.000 200.000
disket sur 1000.000 0.000 500.000
cp 486 200.000 0.000 0.000
bilgisayar 500.000 0.000 0.000
karlilik 250000.000 0.000 60000.000
isgucu 400.000 250.000 0.000
-------------------------------------------------

Analysis of decision variables
------------------------------------
Variable Solution Value
------------------------------------
X1 200.000
X2 300.000
------------------------------------

Analysis of the objective function
----------------------------------
Priority Nonachievement
----------------------------------
P1 0.000
P2 0.000
P3 60000.000
P4 250.000
----------------------------------

***** End of Output *****
```

Analiz tablolarında da görüldüğü gibi darboğaz oluşturan kısıt harddisk kısıtıdır. Temin edilen harddiskin tamamı bilgisayar üretiminde kullanılmaktadır. Bu durumda, harddisk kısıtı artırılamıyorsa kasadan 500 adet, CD sürücüden 300 adet, disket sürücüden 500 adet temin edilmesi yeterlidir. Kasa, CD sürücü ve disket sürücünün daha fazla temin edilmesi üretim kapasitesini artırmayacak ve hedeflerin tutturulmasına katkıda bulunmayacaktır.

Grafik çözümünden de bilindiği gibi çözüm x1=200, x2=300 noktasında oluşmuştur. Bu durumda 1. ve 2. hedef gerçekleştirilebilmiştir. 3. hedeften 60000 pb sapma olmuş, işletmenin bu durumda haftalık karı 190000 pb dir. İşgücü hedefinden ise haftalık 250 saat sapma vardır. Bu durumda işletme yeni işçi almalı veya fazla mesai kullanmalıdır.

Sütun eleme kuralının daha iyi anlaşılabilmesi için aşağıdaki örnek incelenmelidir.

**Örnek 2.4**

Küçük bir boya şirketi, iki tip dış cephe boyası üretiminde uzmanlaşmıştır. Bu boyalar lateks ve emay boyalarıdır. Lateks boyanın her 100 litresi 10 işçi-saat, emay boyanın her 100 litresi ise 15 işçi-saat çalışma gerekmektedir. Haftada yalnız 40 saat çalışıldığı ve dışarıdan işgücü kiralanmadığı veya fazla mesaiye başvurulmadığı varsayılmaktadır. Hem lateks hem de emay boyalarının her 100 litresinden 100 pb kar elde edilmektedir.

Şirket sahibi hedeflerini aşağıdaki gibi sıralamaktadır:

Fazla mesaiden kaçınmak,

Haftalık karı en az 1000 pb’de tutmak,

Her hafta en az 700 litre emay boya üretmek, eski bir müşterisinin talebini karşılamak.

**Çözüm:**

x1: Haftada üretilecek her 100 litre lateks boya

x2: Haftada üretilecek her 100 litre emay boya

**Modelin kurulması**

10x1+15x2≤ 40

100x1+100x2≥1000

x2≥7

x1, x2≥0

G1: 10x1+15x2+ d1--d1+= 40

Min P1d1+

G2: 100x1+100x2+ d2—d2+= 100

Min P1d1+, P2d2-

G3: x2+ d3—d3+= 7

Min P1d1+, P2d2-, P3d3-

**Başarma Fonksiyonu**

Min a= { P1d1+, P2d2-, P3d3-}

A.K.A

10x1+ 15x2+ d1--d1+= 40

100x1+100x2+ d2--d2+= 100

x3+ d3--d3+= 7

x1,x2, x3,d1-,d1+, d2-,d2+, d3-,d3+≥ 0

**Başlangıç tablosunun oluşturulması:**

Modelde üç öncelik seviyesi, iki karar değişkeni ve altı sapma değişkeni bulunmaktadır. Simpleks kriteri 3\*8’lik bir matris olacaktır. Başlangıç tablo x1= 0, x2= 0 noktasından başlar.

** Tablo 2.4. Başlangıç geliştirilmiş simpleks tablo **

| Pj Temel P2 P3 P1 değişken Miktar x1 x2 d1- d2- d3- d1+ d2+ d3+ |  |
| --- | --- |
| d1- 40 10 15 1 0 0 -1 0 0 4 \* P2 d2- 1000 100 100 0 1 0 0 -1 0 10 P3 d3- 7 0 1 0 0 1 0 0 -1 ∞ |  |
| P3 7P3 0 P3 0 0 0 0 0 -P3 Zj-Pj P2 1000P2 100P2 100P2 0 0 0 0 -P2 0 P1 0 0 0 0 0 0 -P1 0 0 \* |  |

Hedef programlama en yüksek öncelikli hedeften başlayıp sıra ile bütün hedefleri en iyileştirecek şekilde ilerler. Simpleks tabloda anahtar sütunun seçiminde en yüksek önceliğe sahip hedefe en büyük katkıyı sağlayacak değişken seçilir. Bir sonraki iterasyonda diğer hedefe geçilir. Bir önceki hedefi kötüleştirmeden bu hedefe en büyük katkıyı sağlayan değişken anahtar sütun seçilir. Bu işleme bütün hedefler sağlanıncaya kadar devam edilir. Bu nedenle tanımayı kolaylaştırmak amacıyla Zj-Pj satırları oluşturulurken hedefler aşağıdan yukarı sıralanır. Ayrıca tabloyu basitleştirmek için Zj matrisi gösterilmez. Zj-Pj değerleri klasik simpleks tablodakine benzer şekilde bulunur. Örneğin d1+ sütunu şu şekilde elde edilmiştir.

(0\*-1)+(P2\*0)+(P3\*0)-P1= -P1

Zj-Pj matrisinde bulunan miktar sütunu esasen Zj değerleri olup Zj matrisi yazılmadığı için burada gösterilmiştir. Bu değerler hedef denklemlerine, çözüme giren değişkenlerin yerleştirilmesiyle elde edilir.

Başlangıç tablosunda görüldüğü gibi 1. öncelikli hedefe ulaşılmıştır. Bu nedenle bu hedefin çözümünü iyileştirecek değişken yoktur. Anahtar sütunun seçiminde 2. öncelikli hedef dikkate alınır. 2. hedefe en çok katkıyı x1 ve x2 eşit miktarda yapmaktadır. Bu nedenle herhangi biri seçilebilir. x1 seçilerek, miktarlar x1 sütunundaki değerlere bölünür. En küçük sonucu veren satır bizim anahtar satırımızdır. Bu satırdaki değişken çözümden çıkarılarak yerine x1 çözüme sokulmuştur. Anahtar satır ve sütunun kesiştiği değer (10) pivot elemandır. Anahtar satır pivot elemana bölünerek çözüme giren değişkenin satır değerleri bulunur.

İkinci tablonun diğer satırları aşağıdaki formüle göre hesaplanır.

Yeni satır=(mevcut satır)-(mevcut satırın anahtar sütun elemanı)\*(yeni anahtar sayı)

Örneğin d2- satırının bazı yeni değerleri şunlardır;

1000-100\*4=600

100-100\*1=0

100-100\*1.5=-50

0-100\*0.1=-10

Bu işlemlere devam edildiğinde ikinci tablo aşağıdaki gibi elde edilmiştir.

Tablo 2.5. Optimal Değiştirilmiş Simpleks Tablo

| Pj Temel P2 P3 P1 değişken Miktar x1 x2 d1- d2- d3- d1+ d2+ d3+ |  |
| --- | --- |
| d1- 4 1 1.5 0.1 0 0 -0.1 0 0 P2 d2- 600 0 -50 -10 1 0 10 - 1 0 P3 d3- 7 0 1 0 0 1 0 0 -1 |  |
| P3 7P3 0 P3 0 0 0 0 0 -P3 Zj-Pj P2 600P2 0 -50P2 -10P2 0 0 10P2 -P2 0 P1 0 0 0 0 0 0 -P1 0 0 |  |

İkinci tablonun Zj-Pj satırları incelendiğinde optimal tablo olduğu anlaşılır. Çünkü P1 seviyesi gerçekleştirilmiştir. 2. düzeyi iyileştirebilecek d1+ sütunundaki 10P2 değeri P1 düzeyini kötüleştirdiği için çözüme alınamaz. Aynı şekilde P3 düzeyini iyileştirebilecek x2 sütunu da anahtar sütun olarak seçilemez. Çünkü P2 seviyesini kötüleştirir.

**2.3.3. İki Yöntemin Birlikte Kullanımı**

Hedefler arasında hissedilir derecede, mutlak, önem üstünlüğünün bulunduğu problemlerin çözümünde öncelikli (hiyerarşik) yöntem kullanılmakta; mutlak önceliklerden söz edilemeyen problemlerin çözümündeyse ağırlıklandırma yöntemi kullanılmaktadır. Her iki durumu aynı anda içeren problemler de vardır. Bu tür problemlerin çözümünde bahsedilen iki yöntem aynı anda kullanılır. Öncelikle hedefler değişik önem seviyelerinde toplanır daha sonra aynı önem seviyesine sahip hedefler kendi içinde ağırlıklandırılır.

**Örnek 2.5**** **

ABC Kumaş Fabrikası yünlü ve pamuklu olmak üzere iki tip elbiselik kumaş üretmektedir. Her iki tip için saatte üretilen miktar aynı olup 1000 metredir. Fabrikanın haftalık normal çalışma kapasitesi 40 saat olup, iki vardiya teşkil edilmesi halinde 80 saat olmaktadır.

Pazarlama bölümünün araştırma sonuçlarına göre haftalık en fazla satış miktarı yünlü için 60.000 metre, pamuklu için ise 45.000 metredir. Muhasebe bölümünden edinilen bilgiye göre yünlünün metresinden 250 para birimi(pb), pamuklu için ise 150 pb kar sağlanabilecektir.

Şirket yönetimi, kendi başarılarının iyi bir işçi-işveren ilişkisinin olmasına bağlı olduğunun bilincindedir. Bu nedenle, sendika ile iyi geçinmeyi istemekte, dengeli bir istihdam seviyesini gerçekleştirmeyi en önemli hedef saymaktadır. Normal üretim kapasitesini aşan talep olması halinde, yönetin üretim kapasitesini fazla mesai ile rahatlıkla arttırabilmektedir. Bu arada idare, fabrikanın 10 saatten fazla, fazla mesai yapması halinde masrafların daha çok arttığını bildiğinden bu sınırı aşmamaya çalışmaktadır. Yönetimin başlıca 4 amacı önem sırasına göre aşağıdaki şekildedir:

Üretim kapasitesinin herhangi bir şekilde altına düşülmemesi

Fabrikanın ihtiyaç duyacağı fazla mesainin 10 saati aşmaması

Yünlü ve pamuklu için tahmin edilen, 60.000 ve 45.000 metrelik satış hacimlerinin mümkün olduğu kadar altında kalınmaması.

Fabrikanın fazla mesai çalışma zamanının mümkün olduğu kadar az tutulması.

**Çözüm: **

Modelin kurulması

x1 : Yünlü kumaş üretimi için kullanılan süre(saat)

x2 : Pamuklu kumaş üretimi için kullanılan süre(saat)

**1.Üretim kapasitesi hedefi:** Fabrikanın kapasitesi günde iki vardiya çalışılması durumunda 80 saat/hafta ile sınırlıdır. Klasik lineer programlamada x1+x2≤ 80 şeklinde ifade edilen bu kısıt sapma değişkenleri eklenerek hedef denklemi olarak yazılır. Birinci önceliğe sahip bu hedef şu şekilde olacaktır. Amaç, kapasitenin altındaki kullanımdan kaçınmak olduğundan d1- minimize edilmelidir. Bilindiği gibi negatif sapma değişkenleri hedeflenen miktarın altındaki kullanımı göstermektedir.

G1: x1+x2+ d1--d1+= 80

Min P1d1-

**2. Fazla mesai süresi:** Fabrikanın ihtiyaç duyacağı fazla mesainin 10 saati aşmaması istenmektedir. Fabrikada kullanılan fazla mesai süresini bir önceki hedef denklemindeki d1+ temsil etmektedir. Hedef denklemi şu şekilde yazılabilir.

G2: d1+ +d2--d2+= 10

Min P1d1-, P2d2+

Görüldüğü gibi bu denklem tamamen sapma değişkenlerinden oluşmuş olup karar değişkeni içermemektedir. Problemin çözümü sırasında oluşabilecek güçlüklerin önlenmesi için denklem, karar değişkenleri kullanılarak yazılır. Yeni denklem, üretim kapasitesi hedef denkleminde;

d1+= 10-d2-+d2+

eşitliği yerleştirilerek elde edilir. Yeni denklem şu şekildedir.

G1: x1+x2+ d2--d2+= 90

Min P1d1-, P2d2+

**3. Satış hedefleri:** Pazarlama departmanın verilerine göre yünlü ve pamuklu kumaşların talepleri sırayla 60000 metre ve 45000 metre olup bunların aşılması mümkün değildir. Burada taleplerin tam olarak karşılanması amaçlanmaktadır; yani talebin altında gerçekleşecek üretimden kaçınılmaktadır. Her iki üründen saatte 1000 metre üretildiği göz önünde bulundurulursa kısıtlar şu şekilde olur.

x1≤60

x2≤40

Burada aynı önem düzeyine sahip iki hedef bulunmaktadır. Birincisi 60000 metreden az yünlü kumaş üretmemek, ikincisi ise 45000 metreden az pamuklu kumaş üretmemektir. Bu hedefler önem derecelerini belirten ağırlık katsayıları belirlenmelidir. Yünlü kumaş 250 pb/m, pamuklu kumaş ise 150 pb/m kar sağlamaktadır. Bu nedenle yünlü kumaş hedefinin pamuklu kumaş hedefine göre 5/3 daha fazla öneme sahiptir. Bu durumda hedef denklemleri şu şekilde yazılır.

G3: x1+d3--d3+≤ 60

x2+d4--d4+≤ 45

Min P1d1-, P2d2+, 5P3d3-+3P3d4-

**4. Fabrikanın fazla mesaisinin minimize edilmesi:** Fabrika tarafından kullanılan işçilik birinci hedefte ifade edilmiştir. Bu denklemde d1+ fazla mesai süresini göstermektedir. Dördüncü hedefte fazla mesaiden kaçınılmak istenildiğine göre hedef denklemi şu şekilde yazılır:

G4: x1+x2+ d1--d1+= 80

Min P1d1-, P2d2+,5P3d3-+3P3d4-, P4d1+

**Başarma Fonksiyonu:**

Min a= { Min P1d1-, P2d2+, 5P3d3-+ 3P3d4-, P4d1+}

A.K.A

x1+x2+ d1--d1+= 80 (1)

x1+x2+ d2--d2+= 90 (2)

x1+d3--d3+≤ 60 (3)

x2+d4--d4+≤ 45 (4)

x1+x2+ d1--d1+= 80

x1, x2, d1-, d1+, d2-, d2+, d3-, d3+, d4-, d4+≥ 0

**Problemin grafik çözümü:**

Öncelikle hedef denklemleri çizilmiştir. Analize en yüksek önceliğe sahip üretim kapasitesi hedefinden başlanır. Bu hedefi birinci doğru temsil etmektedir. d1- değişkeninin minimize edilebilmesi için çözüm 1 doğrusu ve üzerinde kalan alan içinde olabilir.

Daha sonra ikinci hedefe geçilir. Bu hedef 2 doğrusuyla gösterilmiştir. d2+ en küçüklenmesi, mümkünse sıfır yapılması gerekir. Bu nedenle çözüm d2+ nın sıfır olduğu BCEF yamuğu içinde olmalıdır.

Üçüncü öncelikli hedef satış hacmiyle ilgilidir. İşletme en yüksek karı sağlayan satış hacmiyle çalışmak istemektedir. Yünlü kumaş daha fazla kar sağladığı için öncelikle bu ürünün satışının en yüksek olduğu çözüm kümesi aranır. Bu üründen satılabilecek en yüksek miktarın 60000 metre olduğu bilinmektedir. Daha öncelikli hedefleri kötüleştirmeden bu satış hacmini sağlayan çözüm EF doğru parçasıdır. Pamuklu kumaş için belirlenen 45000 metre hedefine geçilir. Bu hedefin gerçekleştirilebilmesi için çözümün 1 doğrusu üzerinde olması gereklidir. Özellikle D noktasında her iki ürün için en yüksek satış hacmi sağlanmış olur. Fakat bu nokta BCEF yamuğunun dışında kalmaktadır ve daha öncelikli hedeflerin çözümünü kötüleştirmektedir. Dolasıyla pamuklu kumaşın üretim miktarı öncelikli hedefleri kötüleştirmeden en yüksek karı sağlayan EF doğru parçası üzerinde aranmalıdır. E ve F noktaları denenir. E noktasında x1= 60000, x2= 30000 F noktasında ise x1= 60000, x2= 20000 dir. Daha yüksek satış hacmi sağlayan E noktası çözüm noktasıdır.

** Şekil 2.3. ABC Kumaş fabrikası probleminin grafik çözümü **

Yönetimin son amacı, fabrikanın toplam fazla mesai ile çalışma zamanını en küçüklemektir. Fabrikanın fazla mesai ile çalışma zamanı 10 saat ile kısıtlandığına göre bu amaç, gerçekte, optimumu değiştirmeyecektir. Şayet 10 saatlik fazla mesai ile çalışma zamanı ortadan kaldırılırsa bu amaç gerçekleşmiş olacaktır. Fakat buna karşılık, pamuklu kumaş imalatından 10000 metrelik bir fedakarlık yapılması gerekmektedir. Diğer bir deyimle E noktasından F noktasına gidilmelidir. Üçüncü amaç pahasına, dördüncü hedef değerine erişilmesi arzu edilmediğine göre problemin optimum çözümü E noktası olacaktır. Bu noktada, üretim, yünlü kumaşlardan x1=60000 m, pamuklulardan x2= 30.000 m; kar da 19.500.000 pb olacaktır.

**2.4. Hedef Programlamanın Uygulama Alanları**

Bu sahada son zamanlarda ilginin artması, çok değişik alanlarda ve çok sayıda aktüel uygulamalara yol açmıştır. Bu sahalardan küçük bir kısmı aşağıda sıralanmıştır:

Reklam Medyası Planlaması,

İşgücü Planlaması,

Program Seçimi,

Hastane Yönetimi,

Akademik Kaynak Ataması,

Belediyelerin Ekonomik Planlaması,

Nakliye Problemleri,

Enerji/Su Kaynakları,

Radar Sistemi ve Deniz Radarı Sistemi Projeleri,

Orman Ürünleri Planlaması,

Zaman Standartlarının Belirlenmesi,

Maliyet Tahmin Tekniklerinin Geliştirilmesi,

Şehir Abonelerinin (elektrik, su gibi) Yenileme Planları,

İşletme Birleşmeleri (merger) Stratejisi,

Çok amaçlı Tesislerin Yerleştirilmesi,

Güneş Enerjisiyle Isıtma/Soğutma.

**2.4.1. Hedef Programlamayla Doğru Uydurma **

Eldeki verileri en az sapmayla ifade edecek doğrunun bulunmasıdır. Bunun için genellikle lineer regresyon analizi kullanılmaktadır.

** Şekil 2.4. Regresyon analizi**

Doğru uydurmadaki amaç sapmaları minimize etmek olduğuna göre hedef programlama kullanılarak da eldeki verilere doğru uydurulabilir.

Model formu aşağıdaki gibi olduğu farz edilirse:

y=β0+β1x1+…+βnxn

y’ yi en küçük sapmayla veren βi değerleri bulunmaya çalışılır. Bu durumda hedef programlama modeli aşağıdaki gibidir.

A.K.A

y1-(β0+β1x11+β2x21+…+βnxn1)+d1--d1+=0

.

.

.

ym-(β0+β1x1m+β2x2m+…+βnxnm)+dm--dm+=0

di-,di+≥0, i=1,…,m

βi≥0, i=1,…,m

**2.5. Hedef Programlamanın Avantajları ve Dezavantajları******

**Avantajları******

Bu yöntemle iki ve daha çok amaca sahip karar problemlerinin çözümü yapılabilir.

Gevşek kısıtlara izin verir.

Hedef programlama, doğrusal programlamada “Uygun Çözümü Mevcut olmayan” (infeasible) problemlere uygun bir çözüm geliştirmede yardımcı teknik olarak da kullanılmaktadır.

**Dezavantajları **

Başarma fonksiyonu çok sayıda amaç fonksiyonunun birleştirilmesiyle oluşturulur. Bu nedenle karmaşık bir yapıya sahip olabilirler.

Hedef değerleri karar verici tarafından tespit edilmelidir.

Karar verici, hedeflerin ağırlıklarını ve öncelik seviyelerini belirlemelidir.

Bu değerleri bağdaşık hale getirecek bir yol bulunmalı.

**3. UYGULAMA**

**3.1. Şirket Tanıtımı**

1937 yılında tamamı yerli sermaye ile kurulan HAYAT KİMYA SANAYİ A.Ş., KASTAMONU AĞAÇ SANAYİ A.Ş., YONGAPAN ORMAN ÜRÜNLERİ A.Ş. den oluşan KİĞILI ŞİRKETLER GURUBU'nun bir üyesidir. Bingo, Test, Bingosil, Nit, ve Hass markalı toz, krem ve sıvı deterjanları; kozmetik pazarında da Nel ve Goll markalı şampuanları üreten kuruluş, kendi sektörünün en önemli şirketlerinden biridir. Hayat Kimya'nın Avrupa standartlarındaki üretim seksiyonlarında, sürekli sülfonasyon (SO3), nötralizasyon, sürekli slurry hazırlık, atomizasyon kulesi ve nihai toz üretim üniteleri bulunmaktadır.

**3.2. Problemin Tanımı**

Bingo sıvı dolum ünitesinde aşağıdaki ürünler doldurulmaktadır. Firma bütün talebi karşılamak istemektedir. Talep mevsimsel olarak değişmektedir ve her yıl değişik oranlarda artmaktadır. Firma ileriki yıllara ait talep tahminleri yapmakta ve bu tahminlere uygun olarak makine ve işgücü kapasitelerini planlamak istemektedir. Mevcut kapasite değerleri aşağıdaki tabloda gösterilmiştir.

**Tablo 3.1. Sıvı dolum ünitesine ait veriler**

| mak | makine adı | ürün | çalışan | dev/ | koli | maksaat/ | adamsaat/ | talep |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no |  |  |  | dak | adet | koli | koli | (koli) |
| 1 | 6'lı döner dolum mak | 1 kg çamaşır suyu | 7 | 26 | 18 | 0,012 | 0,081 | 18000 |
| 2 | 6'lı döner dolum mak | 1 kg çamaşır suyu | 7 | 26 | 18 | 0,012 | 0,081 |  |
|  |  | 2.5 kg çamaşır suyu | 7 | 13 | 6 | 0,008 | 0,054 | 5000 |
|  |  | 4 kg çamaşır suyu | 7 | 6 | 4 | 0,011 | 0,078 | 5000 |
| 3 | 6'lı likit jel dolum mak | 275 gr likit jel |  |  |  |  |  |  |
|  |  | 500 gr likit jel | 5 | 22 | 16 | 0,012 | 0,061 | 2500 |
| 4 | 6'lı bingola dolum mak | 500 gr bingola |  |  |  |  |  |  |
|  |  | 1000 gr bingola | 5 | 20 | 12 | 0,010 | 0,050 | 3500 |
|  |  | 2500 gr bingola | 5 | 10 | 6 | 0,010 | 0,050 | 500 |
| 5 | el dolum | 1 kg wocox | 5 | 12 | 12 | 0,017 | 0,083 | 3000 |
|  |  | 1kg joli banyo | 5 | 12 | 12 | 0,017 | 0,083 | 500 |
|  |  | 1 kg b.sil mutfak | 5 | 10 | 12 | 0,020 | 0,100 | 600 |
|  |  | 1 kg b.sil kireç sök. | 5 | 10 | 12 | 0,020 | 0,100 | 1000 |
| 6 | el dolum | 1 kg ultra çamaşır suyu | 5 | 10 | 12 | 0,020 | 0,100 | 1750 |
| 7 | el dolum | 6 kg çamaşır suyu | 4 | 3 | 6 | 0,033 | 0,133 | 1000 |
| 8 | el dolum | 20 kg çamaşır suyu | 1 | 1 | 1 | 0,017 | 0,017 | 125 |

Firma tarafından belirlenen hedefler aşağıda sıralanmıştır:

Firma gelen bütün talebi karşılamak istemektedir.

Makine kapasitelerinin üzerine çıkılamamaktadır. Ayrıca teknik zorunluluktan dolayı Wocox’ tan 475 koli/vardiya’ dan fazla üretememektir. Diğer ürünler için böyle bir kısıt yoktur.

Sahip olduğu işgücü kapasitesini tam olarak kullanmak istemektedir.

Firma fazla mesaiden kaçınmaktadır.

Karlılığı maksimize etmek istemektedir.

Firma bütün talepleri karşılamak istediğine göre diğer hedefler nasıl değişir?

**Çözüm:**

**Modelin kurulması **

x1: 1 kg çamaşır suyundan doldurulacak toplam koli miktarı

x1a: 1 kg çamaşır suyundan 1. makinede doldurulacak miktar

x1b: 1 kg çamaşır suyundan 2. makinede doldurulacak miktar

x2: 2.5 kg çamaşır suyundan doldurulacak koli miktarı

x3: 4 kg çamaşır suyundan doldurulacak koli miktarı

x4: 500 gr Likit Jel’ den doldurulacak koli miktarı

x5: 1000 gr Bingola’ dan doldurulacak koli miktarı

x6: 2500 gr Bingola’ dan doldurulacak koli miktarı

x7: 1 kg Wocox’ tan oldurulacak koli miktarı

x8: 1 kg Joli Banyo’ dan doldurulacak koli miktarı

x9: 1 kg B. Sil Mutfak’ tan doldurulacak koli miktarı

x10: 1 kg B. Sil Kireç Sökücü’ den doldurulacak koli miktarı

x11: 1 kg Ultra Çamaşır Suyun’ dan doldurulacak koli miktarı

x12: 6 kg Çamaşır Suyun’ dan doldurulacak koli miktarı

x13: 20 kg Çamaşır Suyun’ dan doldurulacak koli miktarı

**Talep hedefleri:**Daha önce de belirtildiği gibi firmanın öncelikli hedefi her üründen en az talep miktarları kadar üretim yapmaktır.

G1: x1a+x1b+d1--d1+=18000

x2+d2--d2+=5000

x3+d3--d3+=5000

x4+d4--d4+=2500

x5+d5--d5+=3500

x6+d6--d6+=500

x7+d7--d7+=3000

x8+d8--d8+=500

x9+d9--d9+=600

x10+d10--d10+=1000

x11+d11--d11+=1750

x12+d12--d12+=1000

x13+d13--d13+=25

Min P1(d1-+d2-+d3-+d4-+d5-+d6-+d7-+d8-+d9-+d10-+d11-+d12-+d13-)

**Makine ve teknik kapasite kısıtı: **İşletmenin dolum ünitesi günde 8 saatten tek vardiya olarak üretimine devam etmektedir. İşletmenin geçmiş deneyimlerine dayanarak işçilerin dinlenme ve makine arızalı olma sürelerini çıkarttıktan sonra makinelerin günde 7 saat etkin olarak çalıştığı kabul edilmiştir. Ayda 24 işgünü çalışılmaktadır. Yukarıdaki bilgilere göre aylık kullanılabilecek makine saatleri şu şekilde hesaplanır.

Maksimum makine saati= Vardiya sayısı\*Günlük çalışma süresi\*Aylık işgünü

Maksimum makine saati= 1\*7\*24=168

Tabloda da görüldüğü gibi makineler, değişik ürünler için programlanabilmekte fakat aynı anda sadece bir ürünün dolumunu yapabilmektedir.

G2: Makine 1: 0.012x1a + d14- - d14+ =168

Makine 2: 0.012x1b + 0.008x2 + 0.011x3 + d 15- - d15+ = 168

Makine 3: 0.012x4 + d 16- - d16 + = 168

Makine 4: 0.010x5 + 0.010x6 + d 17- - d17+ = 168

Makine 5: 0.017x7 + 0.017x8 + 0.020x9 + 0.020x10 + d 18 -- d18+ = 168

Makine 6: 0.020x11 + d 19- - d19 + = 168

Makine 7: 0.033x12 + d 20- - d20+ = 168

Makine 8: 0.017x13 + d 21- - d21+ = 168

**Teknik hedef: **Üretim tanklarının kapasitesi ve kimyasal özelliği nedeniyle Wocox ürününden bir vardiyada 475 koliden daha fazla üretilememektedir. Bu da ayda (1\*24\*475) 11400 koli demektir.

x7 + d22- – d22+ =11400

Yukarıdaki kapasite sınırlarının, yeni yatırım veya iyileştirme yapılmadan aşılması mümkün değildir. Bu nedenle pozitif sapmalar minimize edilmiştir.

Min P1(d1-+d2-+d3-+d4-+d5-+d6-+d7-+d8-+d9-+d10-+d11-+d12-+d13-), P2(d14+ + d15+ + d16++ d17+ + d18+ + d19+ + d20+ + d21+ + d22+ )

**İşçilik hedefi: **Dolum ünitesindeki makinelerde, tam kapasite çalışma durumunda aynı anda 39 işçi çalışabilmektedir. Daha fazla işçi yüklenmesi durumunda atıl işçilik oluşmaktadır; çünkü her makinede çalışacak işçi sayısı belirlidir. (M1=7, M2=7, M3=5, M4=5, M5=5, M6=5 M7=4, M8=1) fakat mevcut talepler tam kapasiteyi gerektirmediği için; işletme yöneticileri tek vardiya üzerinden 17 işçiyle çalışmayı amaçlamaktadır. Bu durumda aylık işçilik hedefi (1\*24\*17) 2856 adamsaat olarak belirlenmiştir.

G3: 0.081x1a + 0. 081x1b + 0.054x2 + 0.078x3 + 0,061x4 + 0,0520x5 + 0.050x6 + 0.083x7 + 0.083x8 + 0.100x9 + 0.100x10 + 0.100x11 + 0.133x12 + 0.017x13 + d 23- - d23+=2856

Min P1(d1-+d2-+d3-+d4-+d5-+d6-+d7-+d8-+d9-+d10-+d11-+d12-+d13-), P2(d14+ + d15+ + d16++ d17+ + d18+ + d19+ + d20+ + d21+ + d22+ ), P3 d 23-

**Fazla mesai hedefi: **Maliyetleri yükselttiği için fazla mesai istenilmemektedir. Bu nedenle modelde pozitif sapmadan kaçınılmıştır.

G4: 0.081x1a + 0. 081x2a + 0.054x2 + 0.078x3 + 0,061x4 + 0,0520x5 + 0.050x6

+ 0.083x7 + 0.083x8 + 0.100x9 + 0.100x10 + 0.100x11 + 0.133x12 + 0.017x13 + d 23-- d23+=2856

Min P1(d1-+d2-+d3-+d4-+d5-+d6-+d7-+d8-+d9-+d10-+d11-+d12-+d13-), P2(d14+ + d15+

+ d16++ d17+ + d18+ + d19+ + d20+ + d21+ + d22+), P3d 23- , P4d23+

**Karlılık hedefi:**İşletme yöneticileri karı maksimize etmek istedikleri için kar sağ taraf değeri 100000 pb gibi oldukça büyük bir değer alındı.

G5: x1a + x1b + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13 +d24--

d24+=100000

Min P1(d1-+d2-+d3-+d4-+d5-+d6-+d7-+d8-+d9-+d10-+d11-+d12-+d13-), P2(d14+ + d15+ + d16++ d17+ + d18+ + d19+ + d20+ + d21+ + d22+), P3d23-, P4d23+, P5 d24-

**Başarma Fonksiyonu**

Min a={ P1(d1-+d2-+d3-+d4-+d5-+d6-+d7-+d8-+d9-+d10-+d11-+d12-+d13-), P2(d14+ + d15+ + d16++ d17+ + d18+ + d19+ + d20+ + d21+ + d22+), P3d23-, P4d23+, P5 d24-}

A.K.A

x1a+x1b+d1--d1+=18000

x2+d2--d2+=5000

x3+d3--d3+=5000

x4+d4--d4+=2500

x5+d5--d5+=3500

x6+d6--d6+=500

x7+d7--d7+=3000

x8+d8--d8+=500

x9+d9--d9+=600

x10+d10--d10+=1000

x11+d11--d11+=1750

x12+d12--d12+=1000

x13+d13--d13+=25

0.012x1a + d14- - d14+ =168

0.012x1b + 0.008x2 + 0.011x3 + d 15- - d15+ = 168

0.012x4 + d 16- - d16 + = 168

0.010x5 + 0.010x6 + d 17- - d17+ = 168

0.017x7 + 0.017x8 + 0.020x9 + 0.020x10 + d 18 -- d18+ = 168

0.020x11 + d 19- - d19 + = 168

0.033x12 + d 20- - d20+ = 168

0.017x13 + d 21- - d21+ = 168

x7 + d22- – d22+ =11400

0.081x1a + 0. 081x1b + 0.054x2 + 0.078x3 + 0,061x4 + 0,0520x5 + 0.050x6 + 0.083x7 + 0.083x8 + 0.100x9 + 0.100x10 + 0.100x11 + 0.133x12 + 0.017x13 + d 23- - d23+=2856

x1a + x1b + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13 +d24-- d24+=100000

x1a, x1b, xi≥0 (i=2,…,13)

di-, di+≥0 (i=1,…,24)

**Tablo 3.2. Birinci planlama dönemi sonuç tablosu**

```text
Program: Goal Programming
Problem Title : birinci planlama dönemi

***** Input Data *****

Min Z = 1P1d-1 + 1P1d-2 + 1P1d-3 + 1P1d-4 + 1P1d-5
+ 1P1d-6 + 1P1d-7 + 1P1d-8 + 1P1d-9 + 1P1d-10
+ 1P1d-11 + 1P1d-12 + 1P1d-13 + 1P2d+14 + 1P2d+15
+ 1P2d+16 + 1P2d+17 + 1P2d+18 + 1P2d+19 + 1P2d+20
+ 1P2d+21 + 1P2d+22 + 1P4d+23 + 1P3d-23 + 1P5d-24

Subject to

talep1 1X1a + 1X1b + d-1 - d+1 = 18000
talep2 1X2 + d-2 - d+2 = 5000
talep3 1X3 + d-3 - d+3 = 5000
talep4 1X4 + d-4 - d+4 = 2500
talep5 1X5 + d-5 - d+5 = 3500
talep6 1X6 + d-6 - d+6 = 500
talep7 1X7 + d-7 - d+7 = 3000
talep8 1X8 + d-8 - d+8 = 500
talep9 1X9 + d-9 - d+9 = 600
talep10 1X10 + d-10 - d+10 = 1000
talep11 1X11 + d-11 - d+11 = 1750
talep12 1X12 + d-12 - d+12 = 1000
talep13 1X13 + d-13 - d+13 = 125
m1 0.012X1a + d-14 - d+14 = 168
m2 0.012X1b + 0.008X2 + 0.011X3 + d-15 - d+15 = 168
m3 0.012X4 + d-16 - d+16 = 168
m4 0.010X5 + 0.010X6 + d-17 - d+17 = 168
m5 0.017X7 + 0.017X8 + 0.020X9 + 0.020X10 + d-18 - d+18 =
168
m6 0.020X11 + d-19 - d+19 = 168
m7 0.033X12 + d-20 - d+20 = 168
m8 0.017X13 + d-21 - d+21 = 168
W 1X7 + d-22 - d+22 = 11400
is 0.081X1a + 0.081X1b + 0.054X2 + 0.078X3 + 0.061X4 + 0.050X5
+ 0.050X6 + 0.083X7 + 0.083X8 + 0.100X9 + 0.100X10 + 0.100X11
+ 0.133X12 + 0.017X13 + d-23 - d+23 = 2856
kar 1X1a + 1X1b + 1X2 + 1X3 + 1X4 + 1X5 + 1X6 + 1X7 + 1X8 + 1X9
+ 1X10 + 1X11 + 1X12 + 1X13 + d-24 - d+24 = 100000

***** Program Output *****

Analysis of deviations
------------------------------------------------
Constraint RHS Value d+ d-
------------------------------------------------
talep1 18000.000 0.000 0.000
talep2 5000.000 0.000 0.000
talep3 5000.000 0.000 0.000
talep4 2500.000 0.000 0.000
talep5 3500.000 0.000 0.000
talep6 500.000 0.000 0.000
talep7 3000.000 0.000 0.000
talep8 500.000 0.000 0.000
talep9 600.000 0.000 0.000
talep10 1000.000 0.000 0.000
talep11 1750.000 0.000 0.000
talep12 1000.000 0.000 0.000
talep13 125.000 0.000 0.000
m1 168.000 0.000 0.000
m2 168.000 0.000 25.000
m3 168.000 0.000 138.000
m4 168.000 0.000 128.000
m5 168.000 0.000 76.500
m6 168.000 0.000 133.000
m7 168.000 0.000 135.000
m8 168.000 0.000 165.875
Wocox 11400.000 0.000 8400.000
işçilik 2856.000 375.125 0.000
kar 100000.000 0.000 57525.000
-------------------------------------------------

Analysis of decision variables
------------------------------------
Variable Solution Value
------------------------------------
X1a 14000.000
X1b 4000.000
X2 5000.000
X3 5000.000
X4 2500.000
X5 3500.000
X6 500.000
X7 3000.000
X8 500.000
X9 600.000
X10 1000.000
X11 1750.000
X12 1000.000
X13 125.000
------------------------------------

Analysis of the objective function
----------------------------------
Priority Nonachievement
----------------------------------
P1 0.000
P2 0.000
P3 0.000
P4 375.125
P5 57525.000
----------------------------------

***** End of Output *****
```

QM çözümünde de görüldüğü gibi mutlak hedef olan talepler gerçekleştirilmiştir. 1 kg çamaşır suyu 1. ve 2. makinelerde doldurulabilmektedir. İşletme hazırlık sürelerini en aza indirmek için öncelikle makine 1’i bu ürün için programlamaktadır. Fakat bu makinede aylık 14000 koliden fazla üretilememektedir. Bu nedenle makine 2, 4000 koli 1 kg çamaşır suyu doldurulacak şekilde programlanacaktır. Böylelikle ürünün 18000 olan talebi gerçekleştirilmiştir.

Makine 1 ve makine 2 hariç diğer makinelerde aşırı bir kapasite fazlalığı görülmektedir. Bu nedenle bu makinelerde doldurulan ürünlerin talebi artsa bile bu makineler kısıt oluşturmayacaktır.

Yukarda da açıklandığı gibi makine kapasitenin üzerine çıkılmamıştır. Yani 2. hedefimizden sapma yoktur.

İşletme 375.125 saat fazla mesai kullanılmıştır. Bu nedenle işgücünü tam kullanma hedefi gerçekleştirilmiştir. 4. hedeften 375.125 saat sapma olmuştur.

İşletmenin şuan ki karı 100.000-57525=42475 pb dir.

Yukarda birinci planlama dönemine değinildi. İkinci planlama döneminde ürün taleplerinde beklenen yüzde artışlar şu şekildedir. 1 kg Çamaşır Suyunda % 10, 500 gr Likit Jelde % 100, 1 kg B.sil Kireç Sökücüde % 40 ve diğer ürünlerde % 20 talep artışı olacağı tahmin edilmektedir.

**Tablo 3.3. İkinci planlama dönemi sonuç tabloları**

```text
Program: Goal Programming
Problem Title : ikinci planlama dönemi

***** Input Data *****

Min Z = 1P1d-1 + 1P1d-2 + 1P1d-3 + 1P1d-4 + 1P1d-5
+ 1P1d-6 + 1P1d-7 + 1P1d-8 + 1P1d-9 + 1P1d-10
+ 1P1d-11 + 1P1d-12 + 1P1d-13 + 1P2d+14 + 1P2d+15
+ 1P2d+16 + 1P2d+17 + 1P2d+18 + 1P2d+19 + 1P2d+20
+ 1P2d+21 + 1P2d+22 + 1P4d+23 + 1P3d-23 + 1P5d-24

Subject to

talep1 1X1a + 1X1b + d-1 - d+1 = 19800
talep2 1X2 + d-2 - d+2 = 6000
talep3 1X3 + d-3 - d+3 = 6000
talep4 1X4 + d-4 - d+4 = 5000
talep5 1X5 + d-5 - d+5 = 4200
talep6 1X6 + d-6 - d+6 = 600
talep7 1X7 + d-7 - d+7 = 3600
talep8 1X8 + d-8 - d+8 = 600
talep9 1X9 + d-9 - d+9 = 720
talep10 1X10 + d-10 - d+10 = 1400
talep11 1X11 + d-11 - d+11 = 2100
talep12 1X12 + d-12 - d+12 = 1200
talep13 1X13 + d-13 - d+13 = 150
m1 0.012X1a + d-14 - d+14 = 168
m2 0.012X1b + 0.008X2 + 0.011X3 + d-15 - d+15 = 168
m3 0.012X4 + d-16 - d+16 = 168
m4 0.010X5 + 0.010X6 + d-17 - d+17 = 168
m5 0.017X7 + 0.017X8 + 0.020X9 + 0.020X10 + d-18 - d+18 = 168
m6 0.020X11 + d-19 - d+19 = 168
m7 0.033X12 + d-20 - d+20 = 168
m8 0.017X13 + d-21 - d+21 = 168
W 1X7 + d-22 - d+22 = 11400
is 0.081X1a + 0.081X1b + 0.054X2 + 0.078X3 + 0.061X4 + 0.050X5
+ 0.050X6 + 0.083X7 + 0.083X8 + 0.100X9 + 0.100X10 + 0.100X11
+ 0.133X12 + 0.017X13 + d-23 - d+23 = 2856
kar 1X1a + 1X1b + 1X2 + 1X3 + 1X4 + 1X5 + 1X6 + 1X7 + 1X8 + 1X9
+ 1X10 + 1X11 + 1X12 + 1X13 + d-24 - d+24 = 100000

***** Program Output *****

Analysis of deviations
------------------------------------------------
Constraint RHS Value d+ d-
------------------------------------------------
talep1 19800.000 0.000 0.000
talep2 6000.000 0.000 0.000
talep3 6000.000 0.000 0.000
talep4 5000.000 0.000 0.000
talep5 4200.000 0.000 0.000
talep6 600.000 0.000 0.000
talep7 3600.000 0.000 0.000
talep8 600.000 0.000 0.000
talep9 720.000 0.000 0.000
talep10 1400.000 0.000 0.000
talep11 2100.000 0.000 0.000
talep12 1200.000 0.000 0.000
talep13 150.000 0.000 0.000
m1 168.000 15.600 0.000
m2 168.000 0.000 0.000
m3 168.000 0.000 108.000
m4 168.000 0.000 120.000
m5 168.000 0.000 54.200
m6 168.000 0.000 126.000
m7 168.000 0.000 128.400
m8 168.000 0.000 165.450
W 11400.000 0.000 7800.000
is 2856.000 1017.550 0.000
kar 100000.000 0.000 48630.000
-------------------------------------------------

Analysis of decision variables
------------------------------------
Variable Solution Value
------------------------------------
X1a 15300.000
X1b 4500.000
X2 6000.000
X3 6000.000
X4 5000.000
X5 4200.000
X6 600.000
X7 3600.000
X8 600.000
X9 720.000
X10 1400.000
X11 2100.000
X12 1200.000
X13 150.000
------------------------------------

Analysis of the objective function
----------------------------------
Priority Nonachievement
----------------------------------
P1 0.000
P2 15.600
P3 0.000
P4 1017.550
P5 48630.000
----------------------------------

***** End of Output *****
```

Birinci hedef gerçekleşmiş ikinci hedeften 15.6 makinesaat/ay pozitif sapma vardır. Bu sapma birinci makineden dolayı oluşmuştur. Yani işletme talepleri tam olarak karşılayabilmek için birinci makineyi ayda 16 saat daha çalıştırmalıdır. Bu da fazla mesai ile mümkündür.

Dördüncü hedefe baktığımızda 1017.550 adamsaat/ay sapma vardır. Yani ayda 1018 saat ek işçiliğe ihtiyaç vardır. İşletme bu işçilik farkını mevcut işçilerine her gün 2.5 saat fazla mesai yaptırarak karşılayacağı gibi 3 adet yeni işçi alarak da karşılayabilir.

İşletmenin bu dönemdeki tahmini aylık karı (100000-48630) 51370 pb dir.

Yeni talep değerleri girilerek model işletildiğinde istenilen planlama dönemi için gerekli olan değerler, yukarıda ki planlama dönemlerinde olduğu gibi elde edilebilir.

**KAYNAKÇA**

Aladağ, Zerrin. Yöneylem Araştırması II Ders Notları. Kocaeli Üniversitesi Endüstri Mühendisliği Bölümü. 2003 Bahar Yarı Yılı.

Aslan, Yakup ve Öztürk**, **Şenol. “Hedef Programlama,” Tarih yok. www.ozyazilim.com, 15 Mart 2003.

Evren, Ramazan ve Ülengin Füsun. Yönetimde Çok Amaçlı Karar Verme. İstanbul, İTÜ Yayınları, 1992.

Kırlıoğlu, Hilmi. (1987), “Amaç Programlama,” Sanayi Mühendisliği Dergisi, Cilt II, Sayı 22, s. 8-13

Kongar, Elif ve Gupta, Surenda M. “Goal Programming” Tarih yok. www.coe.neu.edu, 15 Mart 2003.

Taha, Hamdy A. Yöneylem Araştırması. Çeviren Ş. Alp Baray ve Şakir Esnaf. 6 Baskı, İstanbul, Literatür Yayıncılık.

Timor, Mehpare. Yöneylem Araştırması ve İşletmecilik Uygulamaları. İstanbul, İstanbul Üniversitesi Yayınları, 2002.

**İÇİNDEKİLER**

**İÇİNDEKİLER ……………………………………………………………………...I**

**TABLO LİSTESİ …………………………………………………………………..II**

**ŞEKİL LİSTESİ ……………………………………………………………..……III**

*** *** **** 1. ÇOK AMAÇLI KARAR VERME** 1******

**** 2. HEDEF PROGRAMLAMA** 1******

**** 2.1. Hedef Programlamanın İlkeleri** 3******

**** 2.2. Hedef Programlamanın Formülasyonu** 4******

**** 2.3. Hedef Programlama Algoritmaları** 7******

**2.3.1 Ağırlıklandırma Yöntemi** 7

**2.3.2. Önceliği Koruma Yöntemi** 13

**2.3.3. İki Yöntemin Birlikte Kullanımı** 23

**** 2.4. Hedef Programlamanın Uygulama Alanları** 29******

**2.4.1. Hedef Programlamayla Doğru Uydurma** 29

**** 2.5. Hedef Programlamanın Avantajları ve Dezavantajları** 31******

**** 3. UYGULAMA** 32******

**** 3.1. Şirket Tanıtımı** 32******

**** 3.2. Problemin Tanımı** 32******

**** KAYNAKÇA** 45******

Yakup Aslan ve Şenol Öztürk. ”Hedef programlama”, tarih yok, www.ozyazilim.com.tr ,15/03/ 2003

Ramazan Evren ve Füsun Ülengin. Yonetimde Çok Amaçlı Karar Verme, İst. İTÜ ya.1992,s. 54

Hilmi Kırlıoğlu,”Amaç Programlama,” Sanayi Müh. Dergisi(Nisan 1987)çilt 2,sayı 22.s 10

Hamdy A. Taha. Yöneylem Araştırması, çev. Ş.Alp Baray ve Şakir Esnaf, İstanbul:Literatür yayıncılık,2000, s. 348

Taha, s.349

Taha, s. 349

Evren ve Ülengin, s. 77

Mehpare Timor, Yöneylem Araştırması ve İşletmecilik Uygulamaları, İst, İstanbul Ün. 2001, s.199

Taha, s. 352

Timor, s. 201

Taha, s. 352

Zerrin Aladağ, Yön. Araş. II, Ders Notları, Kocaeli Üniversitesi, 2003(bahar yarı yılı)

Taha, s. 78

Evren ve Ülengin, s. 64

Kırlıoğlu, s. 8

Elif Kongar ve Surenda M. Gupta. tarih yok, www.coe.neu.edu , 15 Mart 2003

Kongar ve Gupta

timor, s.196

PAGE

PAGE 44

---
*Kaynak: `HEDEF PROGRAMLAMA/26/düzgün.doc` — tour guide — 2003*
