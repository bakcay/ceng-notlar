# Internet Adresleri Ve Ağ Siniflari

## **INTERNET ADRES SINIFLARI **

## **VE **

## **ALT AĞLAR**

Internet’e bağlı her sistemin kendisine ait özel bir adresi vardır.Bunlar IP adresi olarak adlandırılır ve bilgisayarlar arasında iletişim yapılırken veri paketlerinin adreslenmesinde kullanılırlar.Bir adres 32 bitlik bir sayıdır; dolayısıyla ağ üzerinde ,teorik olarak 232 tane,

Yani yaklaşık 4 milyar tane bilgisayar bağlanabilir. 32 bitlik IP adresleri gösterimi ve yazımı kolay olsun diye,aynı zamanda ağ yönetimi için sağladığı kolaylıklardan dolayı her biri noktalarla ayrılan 8 bitlik dört parçaya bölünmüştür; parçalar 162.72.155.27, 144.122.65.0 gibi birbirinden noktalar ile ayrılmıştır.Adreslemede hiyerarşik yapı kullanılmaktadır.

Yaklaşık 4 milyar tane IP adresi,ağa 4 milyar tane bilgisayar bağlanabileceğini gösterir;

pratikte bu sayının çok altında olacağı düşünülse de,aslında ağa bağlanabilecek bilgisayarların

sayısı çok daha fazla olacaktır.

İlk bakışta Internet’e bağlanacak bilgisayarların 4 milyarın altında olacağı düşünülü.

Çünkü IP adresleri yalnızca bilgisayarlara değil ağ içinde aktif görevi olan cihazlara da verilir.

Buna ek olarak üzerinde birden fazla arayüz bulunduran bir bilgisayar birden fazla IP adresine sahip olabilir.Örneğin iki LAN arasında bağlantı aygıtı görevini gören bir bilgisayarın iki tane arayüzü olur;iki tane de IP adresi olur.Sonuçta toplam IP adresi sayısı ağa bağlanacak toplam bilgisayar sayısını göstermez.Üstelik bir kısmının atıl durumda kaldığı (bir çok yer kendisine gerekenden fazla IP adresi alıp boş tutmaktadır),bir kısmının da ilerisi için saklı tutulduğu düşünülürse ,bu sayı 4 milyarın çok altında olacaktır.

Ancak Internet’e bağlanan bilgisayarların sayısı 4 milyarın çok çok üstünde olabilir.Çünkü bir servis sağlayıcı üzerinde *dial-up *bağlantı kullanan bilgisayara sabit bir IP adresi verilmez;verilen IP adresi dinamiktir ve oturum kurulması anında belirlenir.Oturum sonlandığında o IP adresi bir başkasına verilir.Böylece sınırlı sayıdaki IP adresi bir çok bilgisayar tarafından kullanılır.

## **Simgesel Adresler**

** **Kullanıcı düzeyinde,sayısal IP adresleriyle uğraşmak,onları akılda tutmak,yani gerektiği zamanlar kolayca hatırlamak güç olur.Bu nedenle, IP adreslerine simgesel isimler verme yoluna gidilmiştir.Örneğin 179.23.45.0 adresine simgesel olarak ‘istanbul.edu.tr’ verilirse ,

ikincisini anımsamak her zaman daha kolay olacaktır.Dolayısıyla bir IP adresi iki farklı şekilde verilebilir; biri sayısal olarak diğeri simgesel olarak;gerçekte her ikisi de aynı yeri

adresler.

## **Adres Sınıflaması**

** **Internet’e bağlı büyüklü küçüklü binlerce ağ vardır ve bu ağlar için gerekli IP adresleri sayısı birbirinden oldukça farklı olabilmektedir.Adres dağıtımını ve ağlara atanan adreslerin ağ aygıtlarına yerleştirimini kolaylaştırmak amacıyla IP adres alanı alt kümelere bölünmüştür;

yani sınıflanmıştır.Beş temel sınıflama vardır ve bunlar A,B,C,D ve E sınıfı adresler olarak adlandırılır.Bunların hangisinin gerektiğini, doğrudan, bu adreslerin kullanılacağı ağın büyüklüğü belirler.

IP adresleri 32 bit uzunluğundadır ve bu adresler temelde 2 parçaya ayrılır; parçanın biri ağı (network ID) ,diğeri ağ içindeki sistemleri (hosts,network devices) temsil eder.Adresin kaç bitinin ağı ,kaç bitinin sistemleri göstereceği üzerinde bir sınırlama yoktur.Ancak tanımlanan 5 tür sınıflama için bu bitlerin sayısı bellidir.Dolayısıyla bu sınıflar içinde en fazla kaç tane ağ ve sistem olacağı önceden belirlenmiştir.

## **A Sınıfı Adres (Class A)**

A sınıfı adres alanı içinde ağlar(netID) 7 bit, ağ içindeki bilgisayarlar (hostID) ise 24 bit ile temsil edilir.Bu tür adres alanı çok büyük ağlar için kullanılır.Örneğin ARPANET,NSFNET gibi ağlar A sınıfı adres alnına sahiptir.

| 0 | (a) netID 7 bit | (b) | (c) hostID 24 bit | (d) |
| --- | --- | --- | --- | --- |

Yukarıda bu tür adres alnının formatı görülmektedir;ilk biti 0 dır.A sınıfı adresleme ,her biri 16 777 214 tane bilgisayar içerebilen 126 tane altağa (subnet) izin verir.16 777 214 sayısı

(224 -2 )’den hesaplanır; 2 adres özel amaçlı kullanılır:*hostid’*nin tüm bitleri 1 olan adresler yayın(broadcast) ve 0 olanlar ise ağ adresi olarak kullanılır.126 sayısı ise(27-2) den hesaplanır;görüldüğü gibi toplam sayıdan 2 çıkarılmıştır.Çünkü 0.0.0.0 ve 127.0.0.0 adresleri özel amaçlı kullanılmaktadır:0.0.0.0 adresi default yönlendirme, 127.0.0.0 adresi ise yerel çevrim için kullanılır.a.b.c.d biçimindeki adresin a parçası ağı,b.c.d kısmı sistemleri adresler.

## **B Sınıfı Adres (Class B)**

Bu tür adres alanı içinde ağlar 14 bit ,ağ içindeki bilgisayarlar ise 16 bit ile temsil edilir;adres alanı her biri 65 534 bilgisayar içeren 16 384 tane alt ağa izin verir.Adres formatının ilk biti 1 0 şeklindedir.Bu tür adres alanı büyük veya orta büyüklükteki ağlar için kullanılır.Bir çok büyük üniversiteler ve ISP ler bu tür adres alanına sahiptir.

| 1 0 | (a) netID | (b) 14 bit | (c) hostID | (d) 16 bit |
| --- | --- | --- | --- | --- |

a.b.c.d biçimindeki adresin a.b kısmı ağı,c.d kısmı sistemleri adresler.İlk parçası (a) 128 ile 191 arasında olan IP adresleri B sınıfındandır.

## **C Sınıfı Adres(Class C)**

C sınıfı adres alanı içinde ağlar 21 bit, ağ içindeki bilgisayarlar 8 bit ile temsil edilir.

Dolayısıyla bu tür adres alanı her biri 254 tane bilgisayar içerebilen 2 097 152 alt ağa izin verir.

| 1 1 0 | (a) | (b) hostID | (c) 21 bit | (d) hostID 8 bit |
| --- | --- | --- | --- | --- |

** **a.b.c.d biçimindeki ağın a.b.c kısmı ağı c kısmı sistemleri adresler.Günümüzde kurumlara daha çok C sınıfı adres verilmektedir.Dolayısıyla yerel ağında az sayıda sistem bulunan kurumlarda bir çok IP adresi boşa gitmektedir!

## **D ve E sınıfı Adres (Class D and Class E)**

D sınıfı adreslerin ilk 4 biti 1110 şeklindedir.Bu adres sınıfı tek bir datagram’ın bir çok sisteme dağıtılması (multicast) için kullanılır.

| 1 1 1 0 | Multicast 28 bit |
| --- | --- |

| 1 1 1 1 | Saklı tutulmuş 28 bit |
| --- | --- |

E sınıfı adreslerin ilk 4 biti ise 1111 dir.Bu adresler Internet’in ilerideki uygulamalarına olanak vermek amacıyla saklı tutulmuştur.

Bir adresin ilk parçası onun hangi sınıfa ait olduğunu gösterir.Aşağıda bütün adres sınıfları için ilk parçanın (a) alabileceği değerler gösterilmektedir.

| Adres sınıfı | İlk parçanın alabileceği değer |
| --- | --- |
| A | 1-126 |
| B | 128-191 |
| C | 192-223 |
| D | 224-239 |
| E | 240-247 |

\*127 adresi ağ içi test ve sistemin kendi prosesleri arasında iletişim için kullanılır,dolayısıyla geçerli bir ağ adresi değildir.

## **Altağlar (Subnets)**

Ağ tasarımında, IP adresleri sistemlere dağıtılırken ağ daha küçük birimlere parçalanarak altağlar (subnets) oluşturulur.Bu Internet’in hiyerarşik adresleme yapısına uygun olduğu gibi,

yönlendirme işleminin sağlanması için gerekli yapının kurulmasını da kolaylaştırır.Örneğin büyük bir üniversiteye B sınıfı bir adres alındığında ,bu adreslerin bölümlerdeki bilgisayarlara

altağlar oluşturmadan gelişigüzel verilmesi bir çok sorunu da beraberinde getirir.Halbuki, verilen B sınıfı adres alanı daha küçük alanlardan oluşan alt alanlara bölünse ve bu alt alanların her biri bölümlerdeki LAN‘lara atansa bir çok kolaylık ta beraberinde gelecektir; adres yerleştirimleri kolay olacak ,hiyerarşik yapı korunacak ,adrese bakılarak ilgili sistemin hangi altağda olduğu anlaşılacak vs gibi getirileri olacaktır.Bu hiyerarşik adresleme yapısı

yerleşim alanlarının adreslenmesine benzer;önce mahallelere ayrılır,ardından caddelere ve sonra da sokaklara…Tam bir hiyerarşik yapı vardır;*taksim.istiklal caddesi.sinema sokak *gibi.

Bir adres alanı alt ağlara bölünürken o adres sınıfının uç sistemlere ayrılan bitleri kullanılır

Örneğin alınana B sınıfı adresten 254 tane altağ oluşturulacaksa ,sistemler için ayrılan 16 bitin

8 biti altağı ,diğer 8 biti de sistemleri adreslemek için kullanılır.

## Ağ kısmı Sistem Kısmı

| **1 0** | netID (14 bit) | hostID (16 bit) |
| --- | --- | --- |

Burası alt ağları Ağa bağlı olan

Adreslemek Sistemleri adreslemek

için kullanılır İçin kullanılır

Altağ adresinde 000… ve 111… adresleri kullanılmaz.Bu durumda altağ sayısı ,adresin ağ kısmı n bit ise 2n -2 olur.

## **Altağ Maskesi (Subnet Mask)**

** **Altağ için kullanılacak bit sayısında bir sınırlama yoktur.Ağ yöneticisi kendi sorumlu olduğu ağın adreslemesini istediği gibi düzenleyebilir.Altağın kaç bit kullanılarak temsil edildiğini belirlemek için altağ maskesi(subnet mask) kullanılır.Altağ maskesi (kısaca ağ maskesi), genel olarak, bir IP adresinin ağ ve sistem için kullanılan bitlerini bulmak ve dolayısıyla ağ adresini belirlemek için kullanılır.Örneğin 192.120.55.129 adresinin kaç bitinin

ağı ,kaç bitinin uç sistemleri gösterdiğini belirlemek için ağ maskesine gerek vardır:ağ maskesi 255.255.255.0 ise 192.120.55.129 adresinin altağ parçası 192.120.55.0, uç sistemi

adresi 129 olur; aynı adres için altağ maskesi 255.255.255.128 ise ,bu sefer, altağ parçası 192.120.55.1 ve uç sistem adresi 1 olur.

Eğer adresin bulunduğu sınıf altağlara ayrılmamışsa ,bu C sınıfı bir adres olduğundan ilk 24 biti ağı,kalan 8 biti de sistemleri destekler.Fakat, altağlara ayrılmışsa ağ maskesi olmadan

Bulmak mümkün değildir.

Aslında bütün sınıflar tüm adres alanı içinde altağları gösterir.Ağ maskesi, ağı gösteren bitler 1,sistemi gösteren bitler 0 yapılarak bulunabilir.

**Adres sınıfı Ağ maskesi Maskelerin bitleri**

A 255.0.0.0 11111111-00000000-00000000-00000000

B 255.255.0.0 11111111-11111111-00000000-00000000

C 255.255.255.0 11111111-11111111-11111111-00000000

Örneğin B sınıfı adreste ilk 16 bit 1,kalan 16 bitte 0 yapılırsa ,B sınıfı adresin maskesi 255.255.0.0 olur.Buna ek olarak B sınıfı adres kendi içinde yukarıdaki şekilde olduğu gibi 8 biti altağ ,8 biti de uç sistemler için olacak şekilde altağlara bölünürse ,yeni altağların maskeleri 255.255.255.0 olur.Böylelikle B sınıfı adres alanı içinde 28 tane C sınıfı altağ elde edilmiş olur

## **Yayın Adresi**

** **Yayın adresi ,ağ adresi dışında kalan bitlerin 1 yapılmasıyla elde edilir.Amacı altağ içerisindeki tüm sistemleri aynı anda adresleyebilmektir.Bir paketin alıcı adres kısmında yayın adresi bulunuyorsa,altağ içindeki tüm sistemler ilgili paketi alır ve işler.

Örneğin 137.36.12.3 adresinin altağ maskesi 255.255.0.0(B sınıfı) ise ilgili altağ için yayın adresi 137.36.255.255 olur.

***Örnek Adresleme:***

Bünyesinde birbirine bağlı birçok LAN bulunduran bir araştırma kurumu,aldığı B sınıfı adresi 254 ağa bölüp ,kurum içindeki bölümlere dağıtmak istemektedir.Adresi 164.55.0.0 olduğu varsayılırsa ,ağın genel maskesi,altağların adresleri ve maskesi ne olur?Bu altağ için yayın adresi nasıl bulunur?

***Çözüm***

B sınıfı adresin ,254 altağa ayrılması için sistemlere ait 16 bitlik kısmın 8 biti kullanılır.

Böylece 28 -2 hesaplamasında 254 tane altağ elde edilir.Diğer 8 bit ise altağlar içindeki uç sistemler için kullanılır.Buna göre 24 bit altağları, kalan 8 bit ise altağlar içindeki sistemleri adresler.

B sınıfı adres 164.55.1.0 Maskesi 255.255.0.0

Altağların adresleri

1.altağ 164.55.1.0 Maskesi 255.255.255.0

2.altağ 164.55.2.0 Maskesi 255.255.255.0

3.altağ 164.55.3.0 Maskesi 255.255.255.0

…

253.altağ 164.55.253.0 Maskesi 255.255.255.0

254.altağ 164.55.254.0 Maskesi 255.255.255.0

Bir altağ içindeki sistemlerin adresleri de, altağ adreslerinin son parçalarının birer arttırılmasıyla bulunur.Örneğin 164.55.254.0 altağı için IP adresleri aşağıdaki gibidir.

164.55.254.1 164.55.254.2 164.55.254.3 …

Altağ yayın adresleri ise,son 8 bitin 1 yapılmasıyla elde edilir.Örneğin 164.55.1.0, 164.55.2.0 altağlarının yayın adresleri aşağıdaki gibi olur:

164.55.1.255 164.55.2.255 ……..255

---
*Kaynak: `INTERNET ADRESLERİ VE AĞ  SINIFLARI/Odevsitesi_com_32630.doc` — ibrahim f doğan — 2003*
