# İki Boyutlu Dizi

**İki Boyutlu Dizi.**

**Bir boyutlu dizilerin kullanılmaları problem çözerken oldukca yararlı olmuştur. Bir boyutlu dizilerin bazı problemlerin çözümünde yetersiz kalması iki boyutlu dizilerin kullanımlarını gündeme getirmiştir. **

**Matematik’te kullanılan Matrisler iki boyutlu diziye iyi bir örnek olarak verilebilir. İki boyutlu dizinin elemanlarına ulaşabilmek için iki tane farklı indis değerine gereksinim vardır. İki boyutlu diziyi matris gibi yorumlarsak indislerden birisi dizinin satır, diğeri dizinin sütun değerini gösterir. **

**Tanım.**

**Genel olarak iki boyutlu bir dizi **

**ve dizinin büyüklüğü=mxn şeklinde belirlenir.**

**İki boyutlu dizinin tanımı, bir boyutlu dizinin tanımından farklıdır. Çünkü tanımda dizinin ikinci boyutuda bulunur. Genel tanımı biraz daha açılırsa **

**Tanımı yapılan iki boyutlu dizinin elemanlarının açıklaması Şekil.2.5 de verilmiştir.**

**İki Boyutlu Dizinin Bellekte Gösterimi.**

**İki boyutlu dizinin belleğe yerleştirilmesinde izlenecek yol bir boyutlu dizideki gibi olmalıdır. O zaman iki boyutlu dizi ya Satır öncelikli veya Sutun Öncelikli olarak belleğe yerleştirilmelidir. Her elemanı bellekte bir kelimelik yer tutan bir boyutlu dizide, dizi elemanları belleğe yerleştirilirken ilk eleman, ‘α’ gibi bir adrese yerleştirildi. Sonra sırası ile diğer dizi elemanlarını ‘α+1’, ‘α+2’ ... ve ‘n’ inci eleman’da ‘α+n’ ninci bellek gözüne yerleştirildi. İki boyutlu dizide bu işlem Satır öncelikli veya Sutun Öncelikli yapılır. Yani iki boyutlu dizinin elemanlarını belleğe yerleştirmek için dizinin satırları tek tek alınıp, bir boyutlu dizide yapılan işlem uygulanır. Böylece iki boyutlu dizinin belleğe yerleştirilmesi gerçekleşir. Eğer sütun öncelikli yerleştirme düşünülürse bu sefer dizinin her sütunu tek tek alınarak bir boyutlu diziye uygulanan işlemin aynısı uygulanarak dizi belleğe yerleştirilir. İki boyutlu bir dizinin belleğe yerleştirilmesi aşağıdaki örneklerde gösterilmektedir.**

**Örnek dizinin adı dizi****1**** ve dizi 3****X****3 elemandan oluşsun. Dizinin tanımını **

**Tanımı yapılan bu dizinin satır elemanları indis halinde Şekil.2.6 deki gibi gösterilebilir.**

| **Dizi****1****\[1,1\] ** | **Dizi****1****\[2,1\] ** | **Dizi****1****\[3,1\] ** |
| --- | --- | --- |
| **Dizi****1****\[1,2\] ** | **Dizi****1****\[2,2\] ** | **Dizi****1****\[3,2\] ** |
| **Dizi****1****\[1,3\] ** | **Dizi****1****\[2,3\] ** | **Dizi****1****\[3,3\] ** |
| **Satir 1** | **Satir 2** | **Satir 3** |

**Şekil.2.6**

**İki boyutlu bu dizi matris gibi yazılırsa Şelil.2.7’daki matris elde edilir.**

**Şekil.2.7 deki dizinin sütün öncelikli ve satır öncelikli olarak belleğe yerleştirilmiş hali Şekil.2.8 de görülmektedir. Dizinin ilk elemanı bellekte ‘i’ gibi bir adrese yerleşir ve dizinin her elemanı bellekte bir kelimelik yer tutmaktadır. Diğer elemanlar takip eden adreslere yerleşir.**

**Bu kitapdaki örneklerde iki boyutlu dizinin belleğe yerleştirilmesi satır öncelikli yapılacaktır.Verilen iki boyutlu dizinin bellekteki başlangıç adresi belli ise herhangi bir elemanın göreceli adresinin nerede olduğu bulunabilir. Dizi\[****X****,y\] nin bellekte bulunduğu adres (****X****-1)n+y+(i-1) ****\[F.2.4\]**** **

**formülü ile bulunur. Bu formülde yer alan elemanların özellikleri **

**L****1 ****≤ ****X**** ≤U****1**** **

**L****2 ****≤ y ≤U****2**** **

**Şeklinde olmalıdır.**

**X**** : Aranan elemanın satır indisi.**

**n : Bir satırdaki eleman sayısı.**

**y : Elemanın sütun indis değeri.**

**Verilen formülün (****X****-1)n+y lik bölümü aranan elemanın dizideki ilk elemana göre kaçıncı eleman olduğunu belirler. (i-1) ise bellek adresini verir.**

**İki boyutlu 4****X****3 elemandan oluşan ‘A’ isimli diziinin tanımı ve diziye eleman atanmış hali Şekil.2.9 da, dizinin bellek gösterimi ise şekil.2.10 da görülmektedir.**

**Şekil.2.9 ‘A’ isimli dizinin tanımı ve veri atanmış hali.**

**A dizisinde A\[3,4\] ün bellekteki yerinin bulunması:**

**A\[3,4\] demek : Ararnan eleman dizinin 3.satır, ile 4.sütununun kesim noktasındaki elemandır. **

**Bir başka deyişle 3 üncü satırdaki 4ncü elemandır. Çünki ****X****=3 y=4 dür.**

**Bu noktada yapılması gerekenler :**

**1. Önce aranan elemanın bulunduğu satırdan önce kaç tane satır olduğu hesaplanır. Bunun için aranan elemanın bulunduğu satırda 1 çıkarılır. Yani (x-1) formülü kullanılır. **

**Verilen örnekte x=3 dür. Ve aranan değer 3-1=2 dir. Yani 2 adet satır var.**

**2. Her satırda kaç eleman olduğu bulunur. Bu değer dizi tanımındaki ilk boyuttan alınır bu örnekte 4 dür.**

**3. 1nci ve 2nci adımlardaki bulunan değerler çarpılarak bir değer elde edilir. Bu değer aranan satıra kadarki satırlarda kaç eleman olduğunu gösterir bu örnekte bu değer 8 dir.**

**4. Son olarak A\[3,4\] deki 2nci rakam olan 4 değeri 3ncü adımda bulunan değere eklenir. Ve aranan elemanın bellekte başlangıç elemanına göre kaçıncı eleman olduğu bulunur. Bu örnekte 3ncü satırdaki 4ncü eleman aranmaktadır. Sonuç olarak A\[3,4\] elemanı bellekte (x-1)\*n+y =(3-1)\*4+4=12 bulunur. Bunun anlamı aranan eleman dizinin ilk elemanından itibaren bellekteki 12nci eleman dır. İlk eleman i gibi bir adreste olduğundan 12nci elemanda i+11 adresinde bulunur.**

**Formülde verilen ve bir satırdaki eleman sayısını veren ‘n’ değeri dizinin satırının boyutları cinsindende yazabiliriz. **

**U****1****-L****1****+1 : Alt ve üst sınırları verilmiş iki boyutlu bir dizinin satır öncelikli belleğe yerleşmesine gore herhangi bir elemanının bellek adresini veren formül.**

**İki Boyutlu Dizi ile ilgili işlemler.**

**Veri yapısı olarak tanımlanan dizilerle çok çeşitli işlemler yapılabilir. Bunlar diziye veri okuma, dizide bulunan verilerin değerlendirilmesi, dizideki verilerin güncelleştirilmesi ve dizideki verilerin silinmesi işlemleri olarak sayılabilir. Bu işlemlerin nasıl yapıldığı aşağıda tek tek ele alınmakta ve bir örnek üzerinde açıklanmaktadır. **

**İki Boyutlu Diziye veri Okuma.**

**Şekil 2.9 de tanımı yapılan ve değer atanan ‘A’ isimli dizinin algoritmasını yazalım ve bu işlemlerin nasıl yapıldığını açıklayalım.**

**Algoritmanın açıklaması :**

**Adım.1 : Bu adımda algoritmada kullanılacak olan ****‘****A’ isimli iki boyutlu dizi tanımlanmakta ve sat indis değişkenine ilk değer atanmaktadır.**

**Adım.2 : Bu adımda algoritmanın satır indisi kontrol edilmekte eğer satır değeri 3 den büyükse işlem akışı adım.5 e yönlendirilmektedir. Bu adımda diğer indis değişkeni olan sutun değişkeninede ilk değer ataması yapılır.**

**Adım.3 : Bu adımda sutun değeri kontrol edilmekte. Eğer bir satır bitmiş ise bir sonraki satırın elemanlarının alınması için işlem akışı adım 2 ye yönlendirilir.**

**Adım.4 : Bu adımda diziye değer okunmakta ve yeni sutun değeri için işlem akışı adım.3 e yönlendirilmektedir.**

**Adım.5 : Bu adım algoritmanın son adımı olup bu adımın işlenmesi ile algoritma sonlandırılır.**

**İki boyutlu dizide herhangi bir dizi elemanı gösterilmek istenirse iki tane indis değeri kullanılır. Bunlar sırası ile dizinin elemanını belirten satır ve sütun değerleridir. Örnek Dizi****1****\[5,3\], Dizi****1****\[2,4\] gibi. **

| **Algoritma İkiBoyutluDiziyeVeriOku****** |  |  |
| --- | --- | --- |
| **//Bu algoritma 4****X****3 boyutunda iki boyutlu tamsayı tipinde ‘A’ isimli diziyi tanımlayarak dizinin eleman değerlerini veri ortamından okur. Algoritmada kullanaılan ‘sat’ ve ’sut’ değişkenleri, tamsayi değişkenler olup dizinin satir, sutun değerlerini tutmak için kullanılan indis değişkenlerdir. ‘sayi’ değişkeni tamsayi tipinde değişken olup veri ortamından değer okumakta kullanılır.//** |  |  |
| **1.** | **\[İlk İşlemler\]** |  |
|  | **A\[1:4,1:3\]Tamsayı; ** **sat←0****** |  |
| **2.** | **\[Dizinin Satır Boyutunu Kontrol Et\]** |  |
|  | **sat←sat+1; ** **sut←0;** **if sat>3 then adım 5 e git;** |  |
| **3.** | **\[Dizinin Sutun Boyutunu Kontrol Et\]** |  |
|  | **sut←sut+1;** **if sut>4 then adım 2’ye git;** |  |
| **4.** | **\[Dizi’ye Değer Oku\]** |  |
|  | **oku(sayı); ** **A\[sut,sat\]←sayı;** **Adım 3’e git** |  |
| **5.** | **\[İşlem Bitir\] ** |  |
|  | **Dur.** |  |
| **Algoritma.2.2** |  |  |

**İki Boyutlu Dizinin Günlenmsi.**

**Algoritma.2.2 ile Şekil.2.9 daki iki boyutlu dizi tanımlandı ve diziye değer okuma işlemi gerçekleştirildi. Şimdide dizide veri günleme işleminin nasıl yapıldığını Algoritma.2.3 ile açıklamaya çalışalım. **

**Algoritma.2.3, ‘A’ isimli dizinin elemanlarını tek tek ziyaret etmekte ve bu esnada sutun\_değeri≤satır\_değeri olan dizi elemanlarını sıfır yapmaktadır. Algoritmanın Açıklaması ve kendisi aşağıdadır.**

**Algoritmanın Açıklaması :**

**Adım.1 : Bu adımda 4X3 buytundaki iki boyutlu dizi tanımlanarak indis değişkenlerinden birisi olan sat değişkenine ilk değer atanır.**

**Adım.2 : Bu adımda algoritmanın sat indis değişkeni kontrol edilir. Sat değeri 3 den büyükse işlem tamamlanmıştır. Algoritmanın işlem akışı adım.5 e yönlendirilir ve algoritma sonlandırılır.**

**Adım.3 :Bu adımda algoritmanaın ikinci indis değişkeni olan sut değişkeni kontrol edilir. Sut değeri 4 den büyükse bir satırdaki elemanlardan istenen şartı sağlayanlar günlenmiştir. Bir sonraki satırdaki elemanların günlenebilmesi için algoritmanın işlem akışı adım.2 ye yönlendirilir.**

**Adım.4 : Bu adımda algoritmada istenen işlem yapılır. Yani sutun değeri satırdan küçükse dizinin o elemanı sıfır yapılır. İşlem akışı adım.3 e yönlendirilir.**

| **Algoritma İkiBoyutluDiziGünle****** |  |  |
| --- | --- | --- |
| **//Bu algoritma 4****X****3 boyutunda iki boyutlu tamsayı tipinde ‘A’ isimli diziyi dolaşır. Bu esnada sutun indisi satır indisinden küçük veya satır indisine eşit olan dizi elemanlarının değerini sıfır yapar. //** |  |  |
| **1.** | **\[İlk İşlemler\]** |  |
|  | **A\[1:4,1:3\]Tamsayı; ** **sat←0****** |  |
| **2.** | **\[Dizinin Satır Boyutunu Kontrol Et\]** |  |
|  | **sat←sat+1; ** **sut←0;** **if sat>3 then adım 5 e git;** |  |
| **3.** | **\[Dizinin Sutun Boyutunu Kontrol Et\]** |  |
|  | **sut←sut+1;** **if sut>4 then adım 2’ye git;** |  |
| **4.** | **\[Veri Günle\]** |  |
|  | **If sut≤sat then A\[sut,sat\]←0;** **Adım 3’e git** |  |
| **5.** | **\[İşlem Bitir\] ** |  |
|  | **Dur.** |  |
| **Algoritma.2.3** |  |  |

**Bu algoritma ile iki boyutlu bir dizinin elemanlarının günlenmesi yapıldı. **

**İki Boyutlu Dizi Elemanlarının Değerlendirilmesi.**

**İki boyutlu dizi elemanlarının değerlendirilmesinin nasıl yapıldığını bir örnek üzerinde yazacağımız 2 algoritma ile gösterelim. Daha önce istanbulun bir gün boyunca her saat başı ölçülen sıcaklık değerini tutan örneği 30 günlük süre için yapacak olan algoritmayı ve günlük sıcsklık ortalaması ile aylık sıcaklık ortalamasını bulan 2 ayrı algoritma ile gösterelim. İlk olarak 30 gün boyunca her gün 24 adet sıcaklık değerini okuyup iki boyuıtlu dizide saklayan algoritmayı ve açıklamasını yazalım. **

| **Algoritma SıcaklıkOkuSakla****** |  |  |
| --- | --- | --- |
| **//Bu algoritma 24****X****30 boyutunda iki boyutlu tamsayı tipinde ‘Isı’ isimli diziyi tanımlayarak istanbulun 30 gün boyunca her gün her saat başı ölçülen sıcaklık değerini veri ortamından okuyup saklayan bir algoritmadır. Algoritmada kullanaılan ‘saat’ ve ‘Gün’ değişkenleri, tamsayi değişkenler olup dizinin indis değişkenleridir. ‘derece’ değişkeni tamsayi tipinde değişken olup veri ortamından sıcaklık değerini kumak için kullanılır.//** |  |  |
| **1.** | **\[İlk İşlemler\]** |  |
|  | **A\[1:24,1:30\]Tamsayı; ** **Gün←0****** |  |
| **2.** | **\[Dizinin Gün Boyutunu Kontrol Et\]** |  |
|  | **Gün←Gün+1; ** **saat←0;** **if gün>30 then adım 5 e git;** |  |
| **3.** | **\[Dizinin Saat Boyutunu Kontrol Et\]** |  |
|  | **Saat←saat+1;** **if saat>24 then adım 2’ye git;** |  |
| **4.** | **\[Dizi’ye Değer Oku\]** |  |
|  | **oku(derece); ** **Isı\[gün,saat\]←derece;** **Adım 3’e git** |  |
| **5.** | **\[İşlem Bitir\] ** |  |
|  | **Dur.** |  |
| **Algoritma.2.2** |  |  |

**Şimdi Günlük ve aylık sıcaklık ortalamasını bulacak olan algoritmayı yazalım ve işlem adımlarının açıklamasını yapalım. Adı geçen algoritmanın açıklaması ve algoritmanın kendisi aşağıdadır.**

**Adım.1 : Bu adımda ilk işlemler olarak Dizi tanımlanır ve değişkenlere ilk değerler verilir.**

**Adım.2 : Bu adımda dizinin gün boyutu kontrol edilir. Eğer 30 gün dolmuş ise aylık ortalama hesaplanarak yazdırılır ve işlemin tamamlanması için işlem akışı algoritmanın son komutuna yönlendirilri.**

**Adım.3 :Bu adımda dizinin saat boyutu kontrol edilir. Eğer saat 24 den büyükse günlük sıcaklık ortalaması hesaplanır ve yazdırılır. Günlük sıcaklık ortalaması sonra kullanılmak üzere aylık sıcaklık ortalamasını bulunması için ona eklenir. Günlük sıcaklık ortalaması yazdırılarak işlem akışı adım.2 ye yönlendirilir.**

**Adım. 4: Bu adımda Günlük ortalamanın hesaplanması için günlük sıcaklık değerleri toplanır.**

**Adım.5 : Bu adım algoritmanın son adımı olup bu adımda işlem sonlandırılır.**

| **Algoritma İkiBoyutluDiziDeğerlendir.****** |  |  |
| --- | --- | --- |
| **//Bu algoritma 24****X****30 boyutunda iki boyutlu tamsayı tipinde ‘Isı’ isimli dizide bulunan istanbulun hergün 24 saat boyunca saat başında ölçülmüş olan bir aylı sıcaklık değerlerini kullanarak istanbulun günlük ve aylık sıcaklık ortalamasını hesaplar. Algoritmada kullanaılan ‘saat’ ve ‘Gün’ değişkenleri, tamsayi değişkenler olup dizinin indis değişkenleridir. ‘Gort’ değişkeni günlük sıcaklık ortalamasını, ‘Aort’ değişkeni ise aylık sıcaklık ortalamasını tutan değişkendir.//** |  |  |
| **1.** | **\[İlk İşlemler\]** |  |
|  | **A\[1:24,1:30\]Tamsayı; ** **Gün←0** **Gort←0** **Aort←0****** |  |
| **2.** | **\[Dizinin Gün Boyutunu Kontrol Et\]** |  |
|  | **Gün←Gün+1; ** **saat←0;** **if gün>30 then adım begin** ** Aort←Aort/30** ** Yaz(Aort);** ** Adım 5 e git;** ** End;** |  |
| **3.** | **\[Dizinin Saat Boyutunu Kontrol Et\]** |  |
|  | **Saat←saat+1;** **if saat>24 then begin** ** Gort←Gort/24;** ** Yaz(Gort);** ** Aort←Aort+Gort;** ** Gort←0;** ** adım 2’ye git;** ** dur;** |  |
| **4.** | **\[Günlük ısı topla\]** |  |
|  | **Gort← Gort+\[gün,saat\];** **Adım 3’e git** |  |
| **5.** | **\[İşlem Bitir\] ** |  |
|  | **Dur.** |  |
| **Algoritma.2.2** |  |  |

**Heriki algoritmanın yaptıklarını yapan pascal programı aşağıdadır.**

|  | **Program ısı;** **Var ** **D\[1..30,1..24\] of integer;** **Procedure ısıal;** **Begin** **For gun:=1 to 30 do** ** For saat:=1 to 24 do read(d(saat,gun));** **End;****** |
| --- | --- |
|  | **Procedure ısıdeğerlendir;** **Begin** **Orta:=0;** **For gun:=1 to 30 do Begin** ** Ortg:=0;** ** For saat:=1 to 24 do ** **ortg:=ortg+d\[saat,gun\];** ** Write(‘Günlük Ortalama ısı =’,ortg/24);** ** Orta:=orta+ortg; ** ** End;** **Write(‘Aylık Ortalama =’,orta/30);** **End;****** |
|  | **Begin** **Isıal;** **Isıdeğerlendir;** **End.****** |

|  | **# include <iostream.h>** |
| --- | --- |
|  | **void ısıal(){** |
|  | **int deger;** |
|  | **for (** |
|  | **int i=1;i<30;i++){** |
|  | ** for (int j=1,j<24;i++){** |
|  | ** cin>>deger;** |
|  | ** D\[i\]\[j\]::deger;** |
|  | ** }** |
|  | ** }** |
|  | **void ısıdegerlendir(){** |
|  | **int orta(0);** |
|  | **for (int gun=1;gun<30;gun++){** |
|  | ** int ortg(0);** |
|  | ** for (int saat=1;saat<24,saat++){** |
|  | ** ortg=ortg+d\[saat,gun\];** |
|  | ** cout<<”Günlük Ortalama ısı=”<<ortg/24;** |
|  | ** orta=orta+ortg;** |
|  | ** cout<<”Aylık Ortalama ısı=”<<orta/30;** |
|  | ** }** |
|  | ** }** |
|  | **int main(){** |
|  | ** ısıal();** |
|  | **ısıdegerlendir();** |
|  | **return 0;** |
|  | **}** |

** DiziÖrnek\[1:m,1:n\]Dizi Tipi**

**şeklinde tanımlanır **

**DiziAdı****\[L****1****:U****1****, L****2****:U****2****\] ****\[T.2.2\]******

**tanımını elde edilir.******

**Şekil.2.5 Bir dizinin tanımı ve değer atanmış hali**

**ÖrnekDizi\[****L****1****:U****1****, L****2****:U****2****\]tamsayı.**

**Dizi tipi**

**2.Boyutun Üst Sınırı**

**2.Boyutun Alt sınırı**

**Dizi Adı**

**1. Boyutun Üst Sınırı**

**1. Boyutun Alt sınırı**

** Dizi****1****\[1:3,1:3\] DiziTipi **

**Şeklinde yapılır. ******

**Şekil.2.7 Dizi****1**** in matris şeklinde gösterimi**

**Satırlar**

**sütunlar******

| **i** | **1,1** |
| --- | --- |
| **i+1** | **2,1** |
| **i+2** | **3,1** |
| **i+3** | **1,2** |
| **i+4** | **2,2** |
| **i+5** | **3,2** |
| **i+6** | **1,3** |
| **i+7** | **2,3** |
| **i+8** | **3,3** |

**Sütun Öncelikli**

| **i** | **1,1** |
| --- | --- |
| **i+1** | **1,2** |
| **i+2** | **1,3** |
| **i+3** | **2,1** |
| **i+4** | **2,2** |
| **i+5** | **2,3** |
| **i+6** | **3,1** |
| **i+7** | **3,2** |
| **i+8** | **3,3** |

**Satır Öncelikli**

**Sutun.1**

**Sutun.2**

**Sutun.3**

**Satır.1**

**Satır.2**

**Satır.3**

**Şekil.2.8.**

**Şekil.2.10 ‘A’ İsimli Dizinin Satır Öncelikli Olarak Belleğe Yerleşimi**

| **Adres** | **İndis** | **Satır** | **Değer** |
| --- | --- | --- | --- |
| **i** | **1,1** | **1.satır** | **3** |
| **i+1** | **1,2** | **6** |  |
| **i+2** | **1,3** | **9** |  |
| **i+3** | **1,4** | **8** |  |
| **i+4** | **2,1** | **2.satır** | **4** |
| **i+5** | **2,2** | **5** |  |
| **i+6** | **2,3** | **2** |  |
| **i+7** | **2,4** | **1** |  |
| **i+8** | **3,1** | **3.satır** | **0** |
| **i+9** | **3,2** | **6** |  |
| **i+10** | **3,3** | **9** |  |
| **i+11** | **3,4** | **7** |  |

**A =**

**(X****1****-1)(U****1****-L****1****+1)+Y **

**koordinati verilen satırdaki kolondeğeri**

**Bir satırdaki eleman sayısı**

**koordinatı verilen satırdan 1 eksik satır miktarını verir**

**Dizinin ilk Hali**

**Algoritma uygulandıktan sonra günlenmiş dizi**

---
*Kaynak: `İKİ BOYUTLU DİZİ/İKİ BOTUTLU DİZİ.doc` — Sefer kurnaz — 2004*
