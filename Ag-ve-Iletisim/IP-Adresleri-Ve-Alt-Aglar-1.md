# IP Adresleri Ve Alt Ağlar

**IP Adresleri ve Altağlar**

**IP Adresleri**

Network üzerindeki bilgisayarlar **Ethernet** kartları aracılığıyla bir biriyle iletişim kurarlar. Her bir Ethernet kartının fiziksel olarak bir MAC adresi vardır. Bu üretimi sırasında karta işlenir. TCP/IP bakımında ise bir network kartının iki adresi vardır:

IP adresi

Host adresi (ethernet adresi)

IP adresleri bir bilgisayarı adreslemeyi amaçlayan 32 bitlik bir bilgidir. Aynı cadde ve sokak adları gibi bölümlüdür ve tek bir kapı sadece tek bir IP adresi ile gösterilir. IP adresleri her biri onlu sayı 0 ila 255 arasında olan 4 gruptan oluşur. Bu gruplar w,x,y,z harfleriyle temsil edilir. Örneğin: 123.45.35.122. Dörtlü gruplardan her biri 8-bitlik bir Internet adresini belirtir.

**Desimal gösterim : **123. 45 . 35 .122

**İkili Gösterim : **11001010. 00101010 . 00100101 . 11010010

Sonuç olarak network içinde her bilgisayar bir network kartına sahiptir. Her network kartı da tanımlanmış bir adrese sahiptir. Network yöneticisi TCP/IP yazılımını yükleyerek her bir kartın IP adreslerini tanımlar.

Her IP adresi iki kısımdan oluşur.** Network ID **ve** Host ID.** Network ID değeri bilgisayarın bulunduğu network (segment) numarasını, Host ID ise bilgisayarın ya da diğer aygıtın numarasını gösterir. Yani mahalle içinde ev numaraları gibi. Bir şehirde 500 mahalle olabilir. Bu beş yüz tane network ID anlamına gelir. Her mahallede binlerce kapı numarası olabilir. Onlarda host ID anlamına gelir.

Bir IP adresi 32 bit uzunluğundadır; dolayısıyla ağ üzerine, teorik olarak 232 tane, yani yaklaşık 4 milyar tane bilgisayar bağlanabilir.32 bitlik IP adresleri gösterimi ve yazımı kolay olsun diye, aynı zamanda ağ yönetimi için sağladığı kolaylıklardan dolayı her biri noktalarla ayrılan 8 bitlik dört parçaya bölünmüştür; parçalar **162.72.155.27, 144.122.65.0** gibi birbirinden noktalar ile ayrılmıştır. Adreslemede hiyerarşik yapı kullanılmaktadır.

Bu 8-bitlik 4 kısmın her biri binary (ikili) olarak da ifade edileceğinden desimal olarak 0-255 arasında, ikili olarak da 0000000 ile 11111111 arasında değer alır.

| **32-Bit IP Adresi ****** |  |  |  |
| --- | --- | --- | --- |
| XXXXXXXX | XXXXXXXX | XXXXXXXX | XXXXXXXX |

Yaklaşık 4 milyar tane IP adresi, ağa 4 milyar tane bilgisayar bağlanabileceğini gösterir; pratikte bu sayının çok altında olacağı düşünülse de, aslında ağa bağlanabilecek bilgisayarların sayısı çok daha fazla olacaktır.

İlk bakışta internet’e bağlanacak bilgisayarların 4 milyarın altında olacağı düşünülür. Çünkü IP adresleri yalnızca bilgisayarlara değil ağ içinde aktif görevi olan cihazlara da verilir. Buna ek olarak üzerinde birden fazla arayüz bulunduran bir bilgisayar birden fazla IP adresine sahip olabilir. Örneğin iki LAN arasında bağlantı aygıtı görevini gören bir bilgisayarın iki tane arayüzü olur; iki tane de IP adresi olur. Sonuçta toplam IP adresi sayısı ağa bağlanacak olan toplam bilgisayar sayısını göstermez. Üstelik bir kısmının atıl durumda kaldığı (*birçok yer kendisine gerekenden fazla IP adresi alıp uzun süre boş tutmaktadır*), bir kısmının da ilerisi için saklı tutulduğu düşünülürse, bu sayı 4 milyarın çok altında olacaktır.

Ancak internet’e bağlanan bilgisayarların sayısı 4 milyarın çok çok üstünde olabilir. Çünkü, bir servis sağlayıcı üzerinden dial-up bağlantıda kullanılan bilgisayara sabit bir IP adresi verilmez: verilen IP adresi dinamiktir ve oturum kurulması anında belirlenir. Oturum sonlandığında o IP adresi bir başkasına verilir. Böylece sınırlı sayıda IP adresi birçok bilgisayar tarafından kullanılır.

**Simgesel Adresler **

Kullanıcı düzeyinde, sayısal IP adresleriyle uğraşmak, onları akılda tutmak, yani gerektiği zamanlar kolayca hatırlamak güç olur. Bu nedenle, IP adreslerine simgesel isimler verme yoluna gidilmiştir. Örneğin 179.23.45.0 adresine simgesel olarak “deu.edu.tr” verilirse, ikincisini anımsamak her zaman daha kolay olacaktır. Dolayısıyla bir IP adresi iki farklı şekilde verilebilir: biri sayısal olarak, diğeri simgesel olarak. Gerçekte her ikisi de aynı yeri adresler, ancak simgesel adreslerin sayısal karşılıkları nasıl bulunur?

*** ******Adres Sınıflaması***

*** ***İnternet’e bağlı büyüklü küçüklü binlerce ağ vardır ve bu ağlar için gerekli IP adresleri sayısı birbirlerinden oldukça farklı olabilmektedir. Adres dağıtımını ve ağlara atanan adreslerin ağ aygıtlarına yerleştirimini kolaylaştırmak amacıyla IP adres alanı alt kümelere bölünmüştür; yani sınıflanmıştır. 5 temel sınıflama vardır. Bunlar: A,B,C,D ve E sınıfı adresler olarak adlandırılırlar. Bunlardan hangisinin gerektiğini, doğrudan, bu adreslerin kullanılacağı ağın büyüklüğü belirler.

IP adresleri 32 bit uzunluğundadır. Bu adresler temelde 2 parçaya ayrılır; parçanın biri ağı (*network ID*), diğeri ağ içindeki sistemleri (*hosts, network devices*) temsil eder. Adresin kaç bitinin ağı, kaç bitinin sistemleri göstereceği üzerine bir sınırlama yoktur. Ancak tanımlanan 5 tür sınıflama için bu bitlerin sayısı bellidir. Dolayısıyla bu sınıflar içinde en azla kaç tane ağ ve sistem olacağı önceden belirlenmiştir.

**A Sınıfı Adres (*****Class A*****)**

A sınıfı adres içinde ağlar (*netID*) 7 bit, ağ içindeki bilgisayarlar (*hostID*) ise 24 bit ile temsil edilir. Bu tür adres alanı çok büyük ağlar için kullanılır. Örneğin ARPANET,NSFNET gibi ağlar A sınıfı adres alanına sahiptir. Aşağıda bu tür adres alanının formatı görülmektedir; ilk biti 0 (*sıfır*)’dır. A sınıfı adresleme, her biri **16 777 214** tane bilgisayar içerebilen 126 tane altağa (***Subnet***) izin verir. **16 777 214 **sayısı (*2**24**-2*)’den hesaplanır; iki adres özel amaçlı kullanılır. h*ostID*’in tüm bitleri 1 olan adresler yayın (***broadcast***) ve 0 olanlar ise **ağ adresi** olarak kullanılır. 126 sayısı ise (27-2)’den hesaplanır. Görüldüğü gibi toplam sayıdan 2 çıkarılmıştır. Çünkü 0.0.0.0 ve 127.0.0.0 adresleri özel amaçlı kullanılmaktadır: **0.0.0.0** adresi ***default *****yönlendirme**, **127.0.0.0** adresi ise **yerel çevrim** için kullanılır.

*w.x.y.z *biçimindeki adresin w parçası ağı, x.y.z. kısmı sistemleri adresler. İlk parçası (w) 1 ile 126 arasında olan IP adresleri A sınıfındandır.

*** w x y z***

| 1 0 | netID | 7 bit | hostID | 24 bit |
| --- | --- | --- | --- | --- |

**B Sınıfı Adres***** (Class B)***

Bu tür adres alanı içinde ağlar 14 bit, ağ içindeki bilgisayarlar ise 16 bit ile temsil edilir; adres alanı her biri 65 534 bilgisayar içeren 16 382 tane altağa izin verir. Adres formatının ilk iki biti 1 0 şeklindedir. Bu tür adres alanı büyük veya orta büyüklükte ağlar için kullanılır. Birçok büyük üniversiteler ve ISS’ler bu tür adres alanına sahiptir. *w.x.y.z *biçimdeki adresi *w.x *kısmı ağı, *y.z *kısmı sistemleri adresler. İlk parçası (w) 128 ile 191 arasında olan IP adresleri B sınıfındandır.

*** w x y z***

| 1 0 | netID | (14 bit) | hostID | (16 bit) |
| --- | --- | --- | --- | --- |

**C sınıfı Adres***** (Class C)*********

C sınıfı adres içinde de ağlar 21 bit, ağ içindeki bilgisayarlar 8 bit ile temsil edilir. Dolayısıyla bu tür adres alanı her biri 254 tane bilgisayar içerebilen 2 097 152 altağa izin verir. *w.x.y.z *biçimindeki ağın *w.x.y *kısmı ağı, z* *kısmı sistemleri adresler. İlk parçası (w) 192 ile 223 arasında olan IP adresleri C sınıfındandır. Günümüzde kurumlara daha çok C sınıfı adres verilmektedir. Dolayısıyla yerel ağında az sayıda sistem bulunan kurumlarda birçok IP adresi boşa gitmektedir !

*** w x y z***

| 1 1 0 |  | netID | (21 bit) | HostID (8 bit) |
| --- | --- | --- | --- | --- |

| **Adres Sınıfı** | **İlk Parçanın Alabileceği Değerler** |
| --- | --- |
| A | 1-126 |
| B | 128-191 |
| C | 192-223 |

**\*127 adresi ağ içi test ve sistemin kendi işlemleri arasında iletişim için kullanılır; bu nedenle geçerli bir ağ adresi değildir!**

**ALTAĞLAR (SUBNETS)**

Ağ tasarımında, IP adresleri sistemlere dağıtılırken ağ daha küçük birimlere parçalanarak altağlar (*subnets*) oluşturulur. Bu Internet’in hiyerarşik adresleme yapısına uygun olduğu gibi, yönlendirme işinin başarılması için gerekli yapının kurulmasını da kolaylaştırır. Örneğin büyük bir üniversiteye B sınıfı bir adres alındığında, bu adreslerin bölümlerdeki bilgisayarlara, altağlar oluşturulmadan gelişigüzel verilmesi birçok sorunu da beraberinde getirir. Halbuki verilen B sınıf adres alanı daha küçük alanlardan oluşan alt alanlara bölünse ve bu alt alanların her biri bölümlerdeki LAN’lara atansa birçok kolaylık da beraberinde gelecektir. Adres yerleştirme işlemleri kolay olacak, hiyerarşik yapı korunacak, adrese bakılarak ilgili sistemin hangi altağda olduğu anlaşılacak vs. gibi getirileri olacaktır. Bu hiyerarşik adresleme yapısı, yerleşim alanlarının adreslenmesine benzer: önce mahallelere ayrılır, ardından caddelere ve sonra da sokaklara…Tam bir hiyerarşik yapı vardır: *Taksim , İstiklal Caddesi , Sinema Sokak* gibi.

Bir adres alanı altağlara bölünürken o adres sınıfının uç sistemlere ayrılan bitleri kullanılır. Örneğin alınan B sınıfı adresten 254 tane altağ oluşturulacaksa, sistemler için ayrılan 16 bitin 8 biti altağı, diğer 8 biti de sistemleri adreslemek için kullanılır.

| 1 0 | netID (14 bit) | hostID(16 bit) (8 bit) (8 bit) |
| --- | --- | --- |

SHAPE \\\* SHAPE \\\* SHAPE \\\*

**Altağ adresinde 000… ve 111… adresleri kullanılmaz. Bu durumda altağı sayısı, adresin ağ kısmı *****n ***** bit ise, 2****n****-2 olur.**

**Altağ Maskesi (*****Subnet Mask*****)**

** **Altağ için kullanılacak bit sayısında bir sınırlama yoktur. Ağ yöneticisi kendi sorumlu olduğu ağın adreslemesini istediği gibi düzenleyebilir. Altağın kaç bit kullanılarak temsil edildiğini belirlemek için altağ maskesi (*Subnet mask*) kullanılır. Altağ maskesi (*kısaca ağ maskesi*) genel olarak, bir IP adresinin ağ ve sistem için kullanılan bitlerini bulmak ve dolayısıyla ağ adresini belirlemek için kullanılır. Örneğin 192.120.55.129 adresinin kaç bitinin ağı, kaç bitinin uç sistemleri gösterdiğini belirlemek için ağ maskesine gerek vardır: ağ maskesi 255.255.255.0 ise 192.120.55.129 adresinin altağ parçası 192.120.55.0, uç sistem adresi 129 olur. Aynı adres için altağ maskesi 255.255.255.128 ise, bu sefer, altağ parçası 192.120.5.1 ve uç sistem adresi 1 olur.

Eğer adresin bulunduğu sınıf altağlara ayrılmamışsa, bu C sınıfı bir adres olduğundan ilk 24 biti ağı, kalan 8 biti de sistemleri adresler. Fakat, altağlara ayrılmışsa ağ maskesi olmadan bulmak mümkün değildir.

Aslında bütün sınıflar tüm adres alanı içinde altağları gösterir. Ağ maskesi, ağı gösteren bitler 1, sistemi gösteren bitler 0 yapılarak bulunabilir.

**Adres Sınıfı Ağ maskesi Maskelerin Bitleri**

**A** 255.0.0.0 11111111-00000000-00000000-00000000

**B** 255.255.0.0 11111111-11111111-00000000-00000000

**C** 255.255.255.0 11111111-11111111-11111111-00000000

Örneğin B sınıfı adreste ilk 16 bit 1, kalan 16 bit de 0 yapılırsa (11111111-11111111-00000000-00000000), B sınıfı adres kendi içinde yukarıdaki şekilde olduğu gibi 8 biti altağ, 8 biti de uç sistemler için olacak şekilde altağlara bölünürse, yeni altağların maskeleri 255.255.255.0 olur. Böylelikle B sınıfı adres alanı içinde 28 tane C sınıfı altağ elde edilmiş olur.

Network ID ve Host ID değerlerinden oluşan IP adreslerinde özel subnet masklar yaratılarak networklerin bölümlenmesi ve daha etkin çalışması sağlanır. Peki bu durumda networkü kısımlara ayırmak için özel subnet masklar nasıl yaratılacak?

Öncelikle network üzerinde kaç tane subnet yaratılacak ona karar verilir. Örneğin şirket networkü üzerinde 3 ya da 5 subnet yaratılacaktır.

Network (subnet) sayısı: 6

Binary değeri: 00000110

Yukarıdaki binary (ikili) değer 00000110 üç bit uzunluğundadır (110). Bu durumda gereken sayı sol baştan üç bitin oluşturduğu iki değerdir.

**Sonuç: 11100000**

Bu ikili değerin desimal karşılığı ise 224 dür. Böylece B sınıfı bir adresi için özel subnet mask değeri 255.255.255.224 olarak hesaplanır. Bu durumda temel subnet yaratma tablosu şu şeklinde olacaktır:

**Tablo: **A sınıf adresler için özel subnet masklar:

| Subnet Sayısı | Bit Sayısı | Subnet Mask | Her Subnetteki Host Sayısı |
| --- | --- | --- | --- |
| **0** | 1 | Yok | **Yok** |
| **2** | 2 | 255.192.0.0 | **4,194,302** |
| **6** | 3 | 255.224.0.0 | **2,097,150** |
| **14** | 4 | 255.240.0.0 | **1,048,574** |
| **30** | 5 | 255.248.0.0 | **524,286** |
| **62** | 6 | 255.252.0.0 | **262,142** |
| **126** | 7 | 255.254.0.0 | **131,070** |
| **254** | **8** | **255.255.0.0** | **65,534** |

**Tablo: **B sınıf adresler için özel subnet masklar:

| **Subnet sayısı****** | **Bit sayısı****** | **Subnet Mask****** | **Her Subnetteki host sayısı****** |
| --- | --- | --- | --- |
| 0 | 1 | Yok | Yok |
| 2 | 2 | 255.255.192.0 | 16,382 |
| 6 | 3 | 255. 255.224.0 | 8,190 |
| 14 | 4 | 255. 255.240.0 | 4,094 |
| 30 | 5 | 255. 255.248.0 | 2,046 |
| 62 | 6 | 255. 255.252.0 | 1,022 |
| 126 | 7 | 255. 255.254.0 | 510 |
| 254 | 8 | 255. 255.255.0 | 254 |

**Tablo:** C sınıf adresler için özel subnet masklar:

| **Subnet sayısı****** | **Bit sayısı****** | **Subnet Mask****** | **Her Subnetteki host sayısı****** |
| --- | --- | --- | --- |
| 0 | 1 | Yok | Yok |
| 1-2 | 2 | 255. 255. 255.192 | 62 |
| 3-6 | 3 | 255. 255. 255.224 | 30 |
| 7-14 | 4 | 255. 255. 255.240 | 14 |
| 15-30 | 5 | 255. 255. 255.248 | 6 |
| 31-62 | 6 | 255. 255. 255.252 | 2 |
| Yok | 7 | Yok | Yok |
| Yok | 8 | Yok | Yok |

**Tablo:** Özet olarak subnet tablosu:

| **Bit** | **Maskeli** | **Subnet** | **Subnet Mask** | **C sınıfı** **host** **sayısı** | **B sınıfı** **host** **sayısı** | **A sınıfı** **host** **sayısı** |
| --- | --- | --- | --- | --- | --- | --- |
| 11000000 | 2 | 2 | 192 | 62 | 16,382 | 4,194,302 |
| 11100000 | 3 | 6 | 224 | 30 | 8,190 | 2,097,150 |
| 11110000 | 4 | 14 | 240 | 14 | 4,094 | 1,048,574 |
| 11111000 | 5 | 30 | 248 | 6 | 2,046 | 524,286 |
| 11111100 | 6 | 62 | 252 | 2 | 1,022 | 262,142 |
| 11111110 | 7 | 126 | 254 | 0 | 510 | 131,070 |

**Network Adresinin Bitlerinden Ödünç Almak**

Subnetting sırasında bir networkün alt networklere bölünmesi için adresleme sisteminde özel gösterimler yapmak gerekir. Örneğin bir C sınıfı adreslemede her networkün içinde 255 tane host tanımlanabilmektedir.

Örneğin bir C sınıf IP networkünün adresi: 192.168.1

Bu network içinde 255 tane host tanımlanır: 1-255 arasında.

Ancak 192.168.1 networkü içinde alt networtler (subnwetworkler) yaratmak isterseniz, network adresinden belli sayıda bit ödünç alınır.

**Normal C sınıfı adresleme: **

| Network Adresi | Yerel Host Adresi |
| --- | --- |

**Network adresinin bitlerinden ödünç alma: ******

| Network Adresi | Ödünç Alınan Adresleri | Yerel Host Adresi |
| --- | --- | --- |

**AND İşlemi**

Bir kaynak IP ve hedef IP adresleri gönderilmeden önce subnet masklarıyla AND işlemine tabi tutulurlar. Eğer sonuç aynı ise o zaman paketin lokal subnet içinde olduğu anlaşılır. AND işleminde sadece 1 AND 1 işleminin sonucu 1 dir. Diğer bileşimlerin hepsinin sonucu 0 dır.

**Örnek: **Subnet mask hesaplama

**IP adresi: 192.168.2.1**

İkili değer: 11000000 10101001 00000010 00000001

Subnet Mask: 11111111 11111111 11111111 00000000

**AND işlemi**

Sonuç: 11000000 10101001 00000010 00000000

**İkinci IP adresi:192.168.2.2**

İkili değer: 11000000 10101001 00000010 00000010

Subnet Mask: 11111111 11111111 11111111 00000000

**AND işlemi**

Sonuç: 11000000 10101001 00000010 00000000

**Sonuçlar aynıdır !:**

Sonuç: 11000000 10101001 00000010 00000000

Sonuç: 11000000 10101001 00000010 00000000

Bu durumda iki host da aynı subnet içindedir.

**Yayın Adresi (Broadcast)**

Yayın adresi, ağ adresi dışında kalan bitlerin 1 yapılmasıyla elde edilir. Amacı altağ içindeki tüm sistemleri aynı anda adresleyebilmektir. Bir paketin alıcı adres kısmında yayın adresi bulunuyorsa, altağ içerisindeki tüm sistemler ile ilgili paketi alır ve işlerler.

Örneğin 137.36.12.3 adresinin altağ maskesi 255.255.0.0 (B sınıfı) ise, ilgili altağ için yayın adresi 137.36.255.255 olur.

**Örnek adresleme 1:**

Bünyesinde birbirine başlı birçok LAN bulunduran bir araştırma kurumu, aldığı B sınıfı adresi 254 altağa bölüp, kurum içindeki bölümlere dağıtmak istemektedir. Adresi 164.55.0.0 olduğu varsayılırsa, ağın genel maskesi, altağların adresleri ve maskesi ne olur? Bir altağ için yayın adresi nasıl bulunur?

**Çözüm 1:**

B sınıfı adresin, 254 altağa ayrılması için sistemlere ait 16 bitlik kısmın 8 biti kullanılır. Böylece 28-2 hesaplamasında 254 tane alt ağ elde edilir. Diğer 8 bit ise altağlar içindeki uç sistemler için kullanılır. Buna göre 24 bit (3 sekizli) altağları, kalan 8 bit ise altağlar içindeki sistemleri adresler.

B sınıfı adres  164.55.0.0 maskesi  255.255.0.0

Altağların Adresleri

1. Altağ  164.55.1.0 maskesi  255.255.255.0

2. Altağ  164.55.2.0 maskesi  *aynı*

3. Altağ  164.55.3.0 maskesi  *aynı*

...

253. Altağ  164.55.253.0 maskesi  *aynı*

254. Altağ  164.55.254.0 maskesi  *aynı*

Altağların, hepsinin maskesi 255.255.255.0 olur. Altağ adresleri ise,

164.55.1.0

164.55.2.0

164.55.3.0

…

olarak sıralanır. Bir altağ içindeki sistemlerin adresleri de, altağ adreslerinin son parçalarının birer arttırılmasıyla bulunur. Örneğin 164.55.254.0 altağı için IP adresleri aşağıdaki gibi olur:

164.55.254.1

164.55.254.2

164.55.254.3

…

Altağ yayın adresleri ise, son 8 bitin 1 yapılmasıyla elde edilir. Örneğin 164.55.1.0, 164.55.2.0 altağlarının yayın adresleri aşağıdaki gibi olur:

164.55.1.255

164.55.2.255

………………255

**Örnek Adresleme 2:**

Bir kurumun internete bağlantısı için C sınıfı bir adres (194.240.120.0) alınmış olsun. Ağ yöneticisi bu adres alanını kurumda bulunan LAN’lara bölerek hiyerarşik yapıda dağıtmak istemektedir; 6 tane LAN olduğuna göre bu altağların adresleri, maskeleri ve yayın adresleri ne olur?

**Çözüm 2:**

C sınıfı adres maskesi 255.255.255.0’dır. 6 altağ elde etmek için sistem için ayrılan bitlerden 3 bit (23=8) ödünç alınır ve burası altağ adreslemesi için kullanılır. Dolayısıyla bir C sınıfı adreste 24 bit olan ağ adres kısmı 3 bit daha eklenerek 27 bite çıkmış olur. Buna göre;

C sınıfı adres  194.240.120.0 maskesi  255.255.255.224

Altağların adresleri

Altağ  194.240.120.0 maskesi  255.255.255.**224******

1. Altağ  194.240.120.**32** maskesi  255.255.255.**224******

2. Altağ  194.240.120.**64** maskesi  *aynı*

3. Altağ  194.240.120.**96** maskesi  *aynı*

4. Altağ  194.240.120.**128** maskesi  *aynı*

5. Altağ  194.240.120.**160** maskesi  *aynı*

6. Altağ  194.240.120.**192** maskesi  *aynı*

Altağ  194.240.120.**224** maskesi  *aynı*

Daha sonra altağ içerisindeki sistemlere adres atamsı yapılır. Örneğin 194.240.120.**32 **adresine sahip altağ içindeki 1,2 ve 3. sistemin adresleri sırasıyla

194.240.120.33,

194.240.120.34 ve

194.240.120.35

olur. Benzer şekilde 194.240.120.**64** adresine sahip ikinci altağ içindeki sistemlere de sırasıyla 194.240.120.**65, …66, …67 **verilebilir.

Altağlara ait yayın adresleri, altağ içerisindeki sistemleri adresleyen 5 bitin hepsinin 1 yapılmasıyla bulunur. Örneğin 194.240.120.32 altağı için yayın adresi şöyle hesaplanır:

Ağ adresi ** 194.240.120.32**

32 sayısı ** 0 0 1 ****0 0 0 0 0**** **** 0 0 1 ****1 1 1 1 1******

194.240.20.32 altağ yayın adresi 194.240.20.63 olarak bulunur.

194.240.20.64 altağı için yayın adresi 194.240.20.95’dir.

Internet Servis Sağlayıcı: modem ile çevrimli erişim veya kurumsal Internet bağlantı hizmeti veren şirketler.

## IP Adresleri ve Altağlar

## PAGE 9

## Altağları adreslemek için kullanılır

## Ağa bağlı olan sistemleri adreslemek için kullanılır

---
*Kaynak: `IP ADRESLERİ VE ALT AĞLAR/IP ADRESLERİ VE ALT AĞLAR.doc` — ZAFER KANBUR — 2004*
