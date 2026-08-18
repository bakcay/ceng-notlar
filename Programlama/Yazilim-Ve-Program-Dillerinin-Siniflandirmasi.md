# Yazilim Ve Program Dillerinin Siniflandirmasi

YAZILIMIN SINIFLANDIRILMASI

-Bilimsel MühendislikYazılımlar

-Görüntüsel Yazılımlar

-Mesleki ve Ticari Yazlımlar

-Sistem Yazılımları

--İşletim Sistemleri

--Derleyiciler

--Editörler

--Debug programları

-Yapay Zeka Yazılımları

PROGRAMLAMA DİLLERİNİN SINIFLANDIRILMASI

-Seviyelerine göre

-Uygulama alanlarına göre

1)Seviyelerine Göre

Programlama dilinin insan anlayışına yakınlığı…

İnsana yakın

Çok yüksek programlama dilleri(Dbase,Clipper,Vbasic,Paradox,Access)

Yüksek seviyeli programlama dilleri(Fortran,Basic,Pascal,Cobol)

Orta seviyeli programlama dilleri( C )

Sembolik makina dilleri(Assembler)

Makinaya yakın

2)Uygulama Alanlarına Göre

-Bilimsel ve mühendislik dilleri(Fortran,C,Pascal)

-Sistem programlama dilleri(C,Assembler)

-Veri tabanı dilleri(Dbase,Clipper)

-Yapay zeka dilleri(Prolog,LISP)

-Genel amaçlı(C,Pascal,Basic)

Programlama Dillerinin Değerlendirilmesi

-Taşınabilirlik

-Verimlilik

-Veri yapıları ve türleri

-Alt programlama yeteneği:

--Avantajları:

---Kodu küçültür

---Algıyı kolaylaştıtır

---Test imkanını arttırır

---Yeniden kullanılabilirliliği arttırır

-Esneklik

-Yapısallık

-Nesne yönelimlilik

-Öğrenme kolaylığı

TEMEL KAVRAMLAR

-İşletim sistemi

-Derleyiciler

C kaynak kodu makina dili(0,1) [amac program]

Derleyici

Derleyicinin Hata Mesajları

1)Uyarılar(warning)

2)Gerçek hatalar(error)

3)Fatal error: Derleme işleminin bitirilmesini engelleyecek büyüklükteki hatalar.

Derleyici .OBJ Linker

.C .EXE

SAYI SİSTEMLERİ VE İKİLİK SİSTEM

İkilik sistemde yezılmış sayının her basamağına 1 bit denir.Bilgisayarda heseplamalar 2’lik sistemde yapılır ve öyle kaydedilir. 1 byte=8 bit 1 kilobyte=1024 byte

1 byte içerisindeki tüm dizilimlerin sayısı 2*2*2*2*2*2*2*2=256’dır.

00000000

………...

………...

11111111

Sayısal olarak 0-255 arası.

Bilgisayarda makina komutları da yazılar da sayılar da 1ve 0’lar olarak korunur…

Tamsayıların 2’lik Sistemde Tutulması

-İşaretsiz sistem

-İşaretli sistem

Tam sayılar işaretli veya işaretsiz sistemde tutulabilirler.İşaretsiz sistemde sayılar hep pozitif kabul edilirler..İşaretli sistem (genellikle bu kullanılır) pozitif ve negatif sayıların yazılabildiği sitemdir..

İşaretli Sistemde Sayıların Gösterimi

Negatif bir sayı bilgisayarda -1100 gibi tutulmaz.nagatiflik için de 1 ve 0’larla gösterilir.Bu konuda 3 sistem önerilmiştir..

1.Sistem

X0101101=> x=1 ise negatif x=0 ise pozitif

Bu sistemde yazılabilecek en büyük sayı 01111111=+127 en küçük sayı ise 11111111=-127.Bu sistemde iki tane 0 vardır.

00000000 ve 10000000

Toplamada da sorunları vardır..

+10= 00001010

10= 10001010

00001010 + 10001010 = 10010100 = -20

Bu sistemde +n ile –n toplandığında –2n yapar..

2.Sistem(1’e tümleme)

0=>+

1=>-

1’e tümleme sayı içindeki 1’lerin 0, 0’ların 1 yapılmasıdır.Pozitif ve negatif sayılar birbirlerinin 1’e tümleyenleridir..

+10=00001010

-10=11110101

Bu sistemde negatif bir sayı yazmamız istenirse önce sayının pazitifini yazar sonra !2 tümleriz.Bu sistemde yazılabilecek en büyük sayı 011111111, en küçük sayı 100000000.1.sistemde olduğu gibi 2 tane 0 var(00000000,111111111)

Toplama hatası yok.

3.Sistem(2’ye tümleme)

Sayının 1’e tümleyenine 1 eklenerek sayının 2’ye tümleyeni bulunmuş olur..

101011010101001001010011

Ya da sayının sağından soluna doğrı ilk 1’i görene kadar (ilk 1 dahil) aynısı ilk 1’den sonra 0’ları 1 1’leri 0 yapılabilir.

Bu sistemde de problemli bir sayı vardır.: 10000000Bu sayının 2’ye tümleyeni alınamaz.Problemli olan bu sayıya –128 değeri verilmiştir.

(C’de en büyük pozitif sayıya 1 eklenirse en küçük negatif tam sayı elde edilir.127+1=-128)

16’lık Sayı Sistemi(Hexadecimal)

0 0000 1A13=3+1*16+10*16*16+1*16*16*16

1 0001 16’lık sistemdeki herbir digite 4 bit karşılık düşer.16’lıktan ikiliğe

2 0010 dönüşüm kolaydır.

3 0011 FC18=1111 1100 0001 1000

4 0100

5 0101

6 0110

7 0111

8 1000

9 1001

A 1010

B 1011

C 1100

D 1101

E 1110

F 1111

8’lik Sistem

0 000

1 001

2 010

3 011

4 100

5 101

6 110

7 111

Yazıların Bellekte Tutulması

Her karakter ascii tablosunda 8 bitlik bir dizilim olaraka tutulmaktadır.Ascii tablusu 256 girişli bir tablodur.Yani karakterler 1 byte’lık sayılardır.C’de örneğin bir karakter aritmetik işlemlere sokulabilir. Bu durumda karakterin ascii numarası işleme sokulmaktadır.(‘A’+1=66)

C'NİN YAZIM KURALLARI

Boşluk Karakterleri

SPACE,TAB,ENTER

1)Atomlar arasında yazım kuralları

İstenildiği kadar boşluk bırakılabilir(#'li satırlar hariç)

ÖRNEK:

```c
#include <stdio.h>
main ( )
{
printf ( "merhaba c\n" )
;
}
```

2)Atomlar istenildiği kadar bileşik yazılabilir...

ÖRNEK:

```c
#include <stdio.h>
main(){printf("merhaba c\n");}
```

C'nin VERİ ve NESNE TÜRLERİ

Her değişken ve sabitin bir türü olmak zorundadır.Tür bilgisi ile derleyici 2 şeyi anlar:

1)O nesne için kaç byte ayıracaktır.

2)O nesne içindeki 1 ve 0'lar nasıl yorumlanacaktır(işaretli,işaretsiz,tam,reel)

BİLDİRİM ve TANIMLAMA

Programlama dillerinin çoğunda bir nesne kullanılmadan önce nesnenin özelliklerinin derleyiciye açıklanması gerekir.Bu işleme bildirim denir...

Nesne özellikleri:

-İsmi

-Türü

-Faaliyet alanı

-Ömrü

-Diğer

Bildirim İşleminin Genel Biçimi

<tür belirtne anahtar sözcük> <değişken ismi>

ÖRNEK:

```c
int a;
unsigned long b;
double weight;
int a,b;
```

Değişken İsimlendirme Kuralları

-Değişken ismi numerik bir karakterle başlayamaz...

-Değişken ismi boşluk içeremez...(Boşluk yerine "_" kullanılır)

-İsimlendirme karakteri olarak ingilizce karakterler kullanılabilir.(Türkçe karakterler kullanılamaz)

-Değişkenin karakter uzunluğu konusunda belirli bir standart yoktur ancak 32 sayısı kullanılmaktadır..

-Case sensitive'dir.Büyük küçük harf kullanımı değişkenleri farklılaştırır...C'nin bütün anahtar sözcükleri küçük harftir..

Bildirim İşlemi Nerede Yapılmalıdır?

1-Blokların başlarında

2-Tüm blokların dışında

3-Fonksiyon parametresi olarak parantezin içinde

1.a)Blokların başında yapılan bildirimler

Fonksiyon ana bloğu içerisinde istenildiği kadar iç içe ya da ayrık blok açılabilir.Tabi bloklar birbirini kesemez.Blok başı demekle küme parantezinin hemen sonrası denilmektedir..

(C++'da yerel değişkenler bloğun her yerinde tanımlanabilir)

Tanımlama Kavramı

Bir bildirimde belekte yer ayrılıyorsa tanımlamadır..Özellikle belirtilmediyse her bildirim işlemi de tanımlama işlemidir.

ÖRNEK:

```c
#include <stdio.h>
main ()
{
int x;
x=10;
}
```

Sabitler

Doğrudan yazılmış sayılara sabit denir. C'de sabitlerin de türleri vardır. Bir sabitin türü nitelikle ya da sayının sonuna getirilen eklerle belirtilir..

-Signed Int Sabitler

İşaretli int sınırları içerisinde kalan ve sonuna ek almamış sayılar otomatik olarak signed int sabiti olarak belirlenirler

-40000 =>Dos'ta int değil ama unix'te int

-Signed Long Int Sabitler

1- 10L =>Signed long int olarak belirtilmiştir.

2- Int sınırını aşmış sayılar otomatik olarak sonunda L veya l olsun olmasın long sabiti olarak kabul edilirler..

(0 (sıfır) C'de her tür sabit anlamına gelmektedir ve istisnadır)

ÖNCEDEN TANIMLANMIŞ KARAKTER SABİTLERİ

'\a' => 7 nolu ASCII çan sesi çıkarır

'\b' => 8 nolu ASCII backspace

'\f' => feedform

'\r' => enter

'\n' => line feed

'\t' => 9 nolu ASCII tab karakteri

'\0' => 0 nolu ASCII null karakter

HEX SİSTEMDE YAZILMIŞİ KARAKTER SABİTLERİ

'\xhh' , '\x13' ,'\x1' ...

Önce bir \ sonra x sonra da iki haneli bir hex sayı yazılırsa o hex sayıya karsılık gelen karakter sabiti elde edilmiş olunur.

'\x61' = 'a'

OKTAL SİSTEMDE YAZILMIŞ KARAKTER SABİTLERİ

'\0ooo' , '\0117' , '\010' ...

Uyarı '\' geçersiz bir karakter sabitidir..ekrana \ basılmak isteniyorsa '\\' karakter sabiti uygulanmalıdır.

SIGNED SHORT SABİTLER

C'de short türünden bir sabit yoktur.

FLOAT SABİTLER

c'de bir sayı nokta içerirse ve sonunda "f" varsa bu sabit float olarak nitelendiririlir.

DOUBLE SABİTLER

Bir sayı nokta içeriyorsa ve sonunda f veya F yoksa double olarak düşünülür.

LONG DOUBLE SABİTLER

Sayı nokta içeriyorsa ve sonuna l veya L içeriyorsa long double düşünülür.

İŞARETSİZTAMSAYI SABİTLER

Sayının sonuna u veya U getirilirse sayı aynı türün unsigned'ı olarak anlaşılır.

10u => unsigned integer

100L => long intereger

100LU =>unsigned long integer (bunun yerine 100UL de aynı anlama gelirdi..)

C'de unsigned tipinde bir sabit yoktur.

C'de sağ taraf ve sol taraf değerleri farklı türlerden olabilir.

printf FONKSİYONUNUN KULLANIMI

printf fonksiyonu ile değişkenlerin içindeki değerler ekrana yazdırılabilir.

printf(.....);

```c
#include <stdio.h>
main()
{
int a;
a = 10;
printf("a=%d\n",a); /* burada %d ",'den sonraki a deişkeninin sayısal */ /*değerinin ekrana yazılacağını gösteriyor*/
}
```

FORMAT KARAKTERLERİ

%d => int türünü 10'luk sistemde

%x => int türünü 16'lık sistemde

%l => long türünü 10'luk sistemde

%lx => long türünü 16'lık sistemde

%f => float ve double türünü

%lf => double türünü

%c => karakter görüntüsünü

%s => string görüntüsünü

yazdırmaya yarar.

TANIMLAMA SIRASINDA DEĞİŞKENLERE İLK DEĞER VERİLMESİ

```c
int i = 200;
int a, b = 10, c;
```

TAMSAYI SABİTLERİNİN 10'LUK 16'LIK VE 8'LİK SİSTEMLERDE GÖSTERİLİŞİ

a = 123; 10'luk

a = 0x123; 16'lık

a = 0123; 8'lik sistemde....

Hexadesimal sistemde yazılmış bir sayının işareti (-,+'lığı) bitleriyle zaten bellidir.

0xFF13 = (1111 1111 0001 0021) en baştaki 1 zaten negatif olduğunu anlatıyor.

Bu sabitin kaçlık sistemde yazıldığıyla hangi türden olduğu arasında bir ilişki yoktur. Belirtilmesi gerekliyse yukarıda anlatıldığı gibi davranılmalıdır.

0xFF13L => long int

gibi..

GERÇEK SAYI SABİTLERİNİN ÜSTEL BİÇİMDE GÖSTERİMİ

3.2E+23 => 3.2*10^23

1.2e-17 => 1.2*10^-17

Üstel formda yazılan sayı ya float ya da double olmalıdır.

FONKSİYONLAR

[geri dönüş değeri] <fonksiyon ismi>([paramatre])

{

ANABLOK

}

Her fonksiyon ard arda tanımlanır.İç içe fonksiyon tanımlanamaz...

Yanlış fonksiyon kullanımına örnek:

```c
main()
{
fonk()
{
}
}
```

Olması gereken:

```c
main()
{
}
fonk()
{
}
```

Hiçbir fonksiyon 1'den fazla tanımlanamaz.En azından aynı isme sahip olmaz.

Fonksiyonlara örnek:

```c
#include <stdio.h>
main()
{
printf("Ben main'im\n");
fonk1();
fonk2();
}
fonk1()
{
printf("Ben 1.fonksiyonum\n");
}
fonk2()
{
printf("Ben 2. fonksiyonum\n");
fonk3();
}
fonk3()
{
printf("Ben 3. fonksiyonum\n");
}
```

FONKSİYONLARIN GERİ DÖNÜŞ DEĞERLERİ(RETURN VALUE)

```c
int x;
x = fonk();
```

Bir fonksiyonun çalışması bittikten sonra onu çağıran fonksiyona gönderdii değere geri dönüş değeri denir.

Fonksiyonların geri dönüş değerleri aritmetik işlemlere sokulabilir.

```c
x = fonk() + a;
```

gibi..

GERİ DÖNÜŞ DEĞERİ OLUŞTURULMASI VE return ANAHTAR SÖZCÜĞÜ

```c
fonk()
{
printf("Ben fonk'um\");
return 100;
}
main()
{
int a;
a = fonk();
printf("fonk'un geri dönüş değeri=%d\n",a);
}
```

return anahtar sözcüğünün iki işlevi vardır:

1-Fonksiyonun çalışmasını bitirir.Bu durumda akış, onu çalıştıran fonksiyonda devam edecektir.

2-Geri dönüş değeri oluşturur.

Kullanım biçimi => return [ifade]

return İFADESİ NASIL OLUŞTURULUR?

return'ün yanındaki ifade önce derleyici yarafından programcının erişemediği geçici bir bölgeye alınır,oradan kullanılır.Örneğin a = fonk(); işleminde şunlar yapılır:

```c
temp = fonk();
a = temp; Bu işlem bize aksettirilmez.
```

Fonksiyonun geri dönüş türü aslında geçici bölgenin türünü gösterir.return ifadesinin oluşturulması da geçici bölgeye yapılan gizli bir atamadır.

```c
long fonk()
{
printf("Ben fonk'um\");
return 123000L;
}
main()
{
long a;
a = fonk();
printf("%ld\n",a);
}
```

return anahtar sözcüğü kullnılmışsa fonksiyon ana bloğu bittiğinde sonlanır.Fonksiyonda return ile belirli bir değer veilmemişse rastgele bir geri dönüş değeri verilecektir.

Bir fonksiyonun geri dönüş değerine sahip olması kullanılmasını gerektirmez.

Fonksiyon başında void yazılırsa foksiyonun geri dönüş değerinin olmadığı analtılır.

```c
void fonk()
{
}
```

Böyle fonksiyonlarda return anahtar sözcüğü fonksiyonu sonlandırmak için kullanılır.void bir fonksiyonun geri dönüş değeri olmadığı için geri dönüş değeri kullanımaya çalışılmamalıdır.

```c
void fonk()
{
printf("selam\n");
return;
}
main()
{
int a;
a = fonk();/*bu kullanım tamamen yanlış*/
printf("%d\n",a);/*bu kullanım tamamen yanlış*/
}
```

void FONKSİYONA NEDEN İHTİYAÇ VARDIR?

1-void anahtar sözcüğü okunabilirliği arttırır.

2-Geri dönüş değerine sahip olmayan fonksiyonları void olarak tanımlarsak yeni derleyiclerin vereceği uyarılardan kurtuluruz.

Parametre yerine void koyarsak fonksiyonun parametre almadığını gösteririz.

main fonksiyonunun da bir geri dönüş değeri vardır.main'e geri dönüş değeri çıkş kodu olarak(exit code) gönderilir.Bu değer işletim sisteminden daha sonra istenebilir.Ancak böyle bir bilgiye seyrek olarak ihtiyaç duyulur.

KLAVYEDEN KARAKTER ALAN STANDART C FONKSİYONLARI

1-getchar fonksiyonu

```c
#include <stdio.h>
void main(void)
{
char ch;
ch = getchar();
printf("%d %c\n", a, a);
}
```

Bu fonksiyon bir tuşa ve ardından enter'a basılana kadar bekler. Basılan tuşun ASCII sıra numarasıyla geri döner.

2-getche fonksiyonu

Enter'a gereksinim duymaz.Bir tuşa basıldığı anda görüntülenme sağlanabilir.

```c
#include <stdio.h>
void main(void)
{
char ch;
ch = getche();
printf("%d %c\n", ch, ch);
}
```

3-getch fonksiyonu

Bu fonksiyon da tuşa basar basmaz alır ama basılan tuşu göstermez.Basılan tuşu görmek için printf ile yazırmak gerekir.

Bu fonksiyon daha çok programın bir tuş alınana kadar bekletilmesini sağlamak için kullanılır.

KLAVYEDEN HER TÜRLÜ BİLGİ ALAN FONKSİYON(scanf)

scanf fonksiyonu printf fonksiyonu gibi format karakterleri alır. Ancak bu karakterler klavyeden yapılan girişi belirlemekte kullanılır.

```c
#include <stdio.h>
void main(void)
{
int a;
printf("sayı=");
scanf("%d", &a);
printf("%d", a);
}
```

scanf fonksiyonunun string kısmında format karakterleri dışında hiçbirşey konulmamalıdır.Buraya konulacak boşluk bile farklı anlama gelir. scanf fonksiyonunun diğer parametrelerinin önünde ampersan(&) operatörü bulunur.

scanf ile birden fazla değişken girişi yapılabilir.

```c
#include <stdio.h>
void main(void)
{
int a;
long b;
printf("sayılar=");
scanf("%d %ld", &a, &b);
printf("%d %ld\n", a, b);
}
```

NESNELERİN FAALİYET ALANLARI VE ÖMÜRLERİ

Faaliyet alanları:

Bir nesnenin derleyici tarafından tanınabildiği program aralığını gösterir.3 tür faaliyet alanı vardı.

1-Blok faaliyet alanı:Yalnızca bir blokta tanınır.

2-Fonksiyon faaliyet alanı:Bir fonksiyonun her yerinde tanınır.

3-Dosya faaliyet alanı:Programın her tarafında tanınır.

NESNELERİN FAALİYET ALANLARINA GÖRE SINIFLANDIRILMASI

1-Yerel değişkenler:

Blokların başlarında tanımlanmış değişkenler yerel değişkenlerdir. Bunlar tanımlandıkları blokta kullanılırlar.(blok faaliyet alanı)

```c
void main(void)
{
int a;
{
int b;
}
}
```

Burda a main fonksiyonunun tamamında b ise sadeec içteki blok'ta geçerlidir.Farklı faaliyet alanlarına sahip değişkenler aynı ada sahip olabilir.

```c
main()
{
int a = 10;
{
int a = 20;
}
}
```

Farklı faaliyet alanlarına ilişkin aynı isimli nesneler için farklı yerler ayrılır.Bir blok içierisinde aynı isimli birden fazla değişken faaliyet gösteriyorsa, o blok içerisinde değişken kullanıldığında dar faaliyet alanı olan kullanılır.

2-Global değişkenler

Tüm blokların dışında tanımlanan değişkenlere global değişkenler denir.Dosya faaliyet alanı kuralına uyar.Kaynak kodun her yerinde tanınır.

```c
#include <stdio.h>
int a;
void fonk(void)
{
a = 20;
}
void main(void)
{
a = 10;
fonk();
printf("%d\n", a);/*ekrana 20 değeri basılır*/
}
```

```c
#include <stdio.h>
int a;/*global*/
void fonk(void)
{
a = 20;/*global a'ya atanan değer*/
}
void main(void)
{
int a;/*yerel*/
a = 10;/*yerel a'ya atanan değer*/
printf("%d\n", a);/*ekrana 10 değeri basılır*/
}
```

Global değişkenler herhangi bir yerde tanımlanabilir,ancak tanımlandıkları yerden daha yukarda derleyici tarafından etspit edilemezler.Bu durumda global değişkenler için en iyi tanımlama yeri programın tepesidir.yani include dosyalarının hemen altıdır.

3-Parametre değişkenleri

Bir fonksiyon parametre alabilir.Bunun için parametre değişkenlerinin tanımlanması gerekir.İki ayrı yöntemel parametre bildirimi yapılır.

a.Eski biçim:

```c
void fonk(a,b)
int a;
long b;
{
}
```

b.Yeni biçim

```c
void fonk(int a,long b)
{
}
```

Bu biçimde parametre değişkenlerş aralarına virgül konularak tanımlanır.

```c
void fonk(int a,b)/*YANLIŞ TANIMLAMA*/
```

Bu değişkenler fonksiyon faaliyet alanı kuralına uyarlar.Parametre değişkenine sahip bir fonksiyon aynı sayıda değişkenle çağırılmalıdır.

PARAMETRE AKTARIM KURALI

Parametreli bir fonksiyon çağırıldığında derleyici önce parametrelerden parametre değerlerine karşılık atama yapar, daha sonra programın akışı fonksiyona geçirilir.

```c
#include <stdio.h>
int add(int a, ,int b)
{
return a + b;
}
void main(void)
{
int x = 10, y = 20, z;
z = add(x, y);
printf("%d\n", z);
}
```

Fonksiyonlar sabitlerle de çağırılabilrler.

```c
fonk(10, 20); gibi..
```

BAZI MATEMATİK FONKSİYONLAR

```c
#include <stdio.h>
#include <math.h>
```

sqrt fonksiyonu double olarak aldığı bir sayıyı kare kökü olarak geri döndürür.

sin, cos, tan, atan hepsinin parametresi ve geri dönüş değeri double

```c
#include <stdio.h>
int kare(int x);
{
return x * x;
}
void main(void)
{
printf("%d\n", kare(10));
}
```

Bir fonksiyonun parametresi bir diğerinin geri dönüş değeri olabilir.

NESNELERİN ÖMÜRLERİ

Ömür:Nesnenin bellekte yer kapladığı zaman aralığına ömür denir. Nesnelerin ömürleri 2 gruba ayrılır.

1-Statik ömürlü nesneler:Bu nesneler programın belleğe yüklenmesiyle yaratılırlar.Program bitince hafızadan atılır.

2-Dinamik ömürli nesneler:Programın belli bir aşamasında yaratılırlar, belirli bir süre faaliyet gösterdiktensonra kaybedilirler.

YEREL DEĞİŞKENLERİN ÖMÜRLERİ

Dinamik ömürlüdürler.Programın akışı bloğa girdiğinde yaratılırlar, bloğun çalışması bittiğinde bellekten çıkarılırlar.

GLOBAL DEĞİŞKENLERİN ÖMÜRLERİ

Statik ömürlüdürler.Programın başından sonuna kadar bellekta kalırlar.

PARAMETRE DEĞİŞKENLERİNİN ÖMÜRLERİ

Dinamik ömürlüdürler.Fonksiyon çağırıldığında yaratılırlar, fonksiyon çalışması bittiğinde bellekten silinirler.Parametreli bir fonksiyonun çağırılmasında şunlar olmaktadır.

1-Parametre değişkeni yaratılır.

2-Değer ataması yapılır

3-Programın akışı fonksiyona yönledirilir.

Ömürle faaliyet alanı arasındaki ilişki programın faaliyet alanına girdiğinde değişken yaratılır, faaliyet alanından çıktığında değişken sonlandırılır.

İçerisine değer verilmemiş yerel değişkenlerin içinde rastgele değerler vardır.Bir değer atanmamış global değişkenlerin içerisinde ise 0 değeri vardır.Parametre değişkenlerine değer atanmaması söz konusu değildir.

OPERATÖRLER

Bir işleme yol açan, işlem sonucunda belirli bir değer üretilmesini sağlayan atomlara operatör denir.

OPERATÖRLERİN SINIFLANDIRILMASI

1-İşlevlerine göre

a.Aritmetik operatörler(+,*,/...)

b.İlişkisel operatörler(<,<,<=,...)

c.Mantıksal operatörler(AND,OR,NOT,XOR,..)

d.Bit operaörleri(belli bir sayının kaçıncı bitinin kaç olduğu hakkında bilgi verir)

e.Gösterici operatörleri

f.Özel amaçlı operatörler

2-Operand sayılarına göre

a.İki operand alanlar (binary)

b.tek operand alanlar (unary)

c.Üç opernd alanlar (ternary)

3-Operatörün konumuna göre yapılan sınıflandırma

a.Ara ek operatörler (infix)

b.Ön ek operatörle (prefix)

c.Son ek operatörleri (postfix)

C'nin bütün iki operand alan operatörleri infix'tir.Bir operatörün teknik olarak tanımlanması için bütün bu gruplardaki yerinin belirtilmesi gerekir.Örneğin 4 binary infix aritmetik operatördür.

OPERATÖRLER ARASI ÖNCELİK İLİŞKİSİ

Bir operatörün diğerinegöre bir öncelil sırası vardır.Bu sıra operatörlerin öncelik tablosu denilen bir tabloyla belirtilir.

Tabloda üstteki satrda bulunanlar attakilerden daha önceliklidir. Aynı satırda bulunanlar eşit önceliklidir.Aynı öncelikli operatörlerle soldan sağa ya da sağdan sola işlem yapılır.

ARİTMETİK OPEARATÖRLER

+, -, *, / binary, infix

% OPEARÖRÜ

Binary infix bir operatördür.Bölüm işlemideki kalanı hesaplar.

++ VE -- OPERATÖRLERİ

++ arttırma -- eksiltme operatörüdür.

İkisi de unary operatörlerdir.Postfix ve prefix olarak kullanılabilir. Postfix ve prefiz kullanımda fark vardır. ++a => a = a + 1;

Bu operatörler başka hiçbir operatör olmadan tek başlarına kullanılmışsa aralarında fark olmaz.

```c
void main(void)
{
int a = 10;
++a;
printf("%d\n", a);/*11*/
--a;
printf("%d\n", a);/*10*/
a++;
printf("%d\n", a);/*11*/
a--;
printf("%d\n", a);/*10*/
}
```

Eğer başka operatörlerle beraber kullanılıyorlarsa prefix durumda tabloda belirtilen öncelikle işlemler yapılır.Eğer postfix durumda kullanılmışsa bütün işlemler yapıldıktan sonra yani ifadenin son işlemi olacak biçimde arttırma ya da eksiltme yapılır.

```c
void main(void)
{
int b, a = 10;
b = ++a;
printf("a=%d b=%d", a, b);/*a=11 b=11*/
b = a++;
printf("a=%d b=%D", a, b);/*a=12 b=11*/
}
```

```c
void main(void)
{
int a = 10, b = 20, c;
c = a++ * b++;
printf("c=%d b=%d a=%d", c, b, a);/*c=30 b=21 a=11*/
}
```

ŞÜPHELİ KODLAR

++ veya -- operatörlerinin bilinçsizce ve kötü kullanımları derleyiciler arasında yorum farklııklarına yol açarak taşınabilirliği bozar.Böyle kolardan kaçınmk gerekir.

1-Üç tane + operatörü boşluk olmaksızın yanyana getirilmemelidir.(+++)

2-Bir değişken ++ veya -- ile kullanılmışsa bir daha aynı ifade içerisinde ++ veya -- operatörleriyle gözükmemelidir.(hata: b = ++a + ++a;)

3-

```c
int multiply(int a, int b)
{
return a * b;
}
void main(void)
{
int a, b = 10;
a = multiply(b, ++b);/*hata:derleyicinin parametreleri ne sırayla*/ /*aktardığı derleyiciye göre değişir.*/
printf("%d\n", a);
}
```

Bir fonksiyon çağırılırken parametrelerden birinde ++ veya -- kullanılmışsa diğer parametrelerde aynı değişken kullanılmamalı, çünkü parametre aktarım sayısı her sistemde aynı olmayabilir.

```c
fonk(++a);/*Doğru:önce a arttırılır sonra yeni a değeriyle fonk çağırılır*/
fonk(a++);/*Doğru:önce fonk çagırılır sonra a arttırılır*/
```

İLİŞKİSEL OPERATÖRLER

< > <= >=

== !=

C'de 6 ilişkisel operatör vardır.Hepsi binary infix operatörlerdir. Aritmetik operatörlerden daha düşük önceliklilerdir.

İlişkisel operatörlerin ürettiği değer önerme doğruysa 1 yanlışsa 0'dır

```c
void main(void)
{
int a;
a =10 > 5;
printf("a=%d\n", a);/*a=1*/
}
```

Bu operatörlerden elde edilen değerler başka operatörlerle işleme sokulabilir.

MANTIKSAL OPERATÖRLER(&&)

C'de 3 tane mantıksal operatör vardır.

AND &&

OR ||

NOT !

AND OPERATÖRÜ

A | B | A&&B

0 | 0 | 0

1 | 0 | 0

0 | 1 | 0

1 | 1 | 1

Mantıksal operatörlerin hepsi önce operandlarını doğru ya da yanlış olarak yorumlar, eğer sonuç doğruysa 1, yanlışsa 0 sayısal değerini üretir. Yorumlamada kural:eğer operand 0 dışı bir değerse doğru olarak, 0 ise yanlış olarak yorumlanır.Uygulama da ilişkisel operatörlerle birlikte kullanılırlar.

&& operatörünün önce sol tarafı tam olarak bitirilir.Daha sonra sağ tarafı yapılır ve bitirilir.Eğer sol tarafın sayısal değeri 0 ise sağ tarafın yapılmasına gerek kalmaz.

Örneğin x > 10 && fonk() burada x 10'dan küçükse fonk hiç çağırılmayacaktır.

OR OPERATÖRÜ(||)

OR işlemi iki operand da yanlışsa yanlış,operandlardan en az birisi doğruysa doğru sonucunu üretir.

a | b | a||b

0 | 0 | 0

0 | 1 | 1

1 | 0 | 1

1 | 1 | 1

Bu operatör de 1 ya da 0 tamsayı değerini üretir.

```c
void main(void)
{
int x,y;
scanf("%d",&y);
x = y < 10 || y > 50;
printf("%d\n",x);/*girilen y değeri 10'dan küçük veya 50'den*/ /*büyükse ekrana 1 değeri basılacaktır.*/
}
```

OR operatörünün önce sol tarafı yapılır.Eğer sol taraf değeri 0 dışı bir değerse sağ tarafın yapılmasına gerek kalmaz.

NOT OPERATÖR(!)

Bu operatör unary prefixtir.Zaten öncelik tablosunun ikinci düzeyi tamamen unary operatörlere ayrılmıştır.

a | !a

0 | 1

1 | 0

Yani bu operatör operand 0 ise 1 , 0 dışı herhangibir değerse 0 yapar.

```c
void main(void)
{
int x,a = 10;
x = !!a;
printf("%d\n", x);/*a = 10, !a = 0, !(!a) = 1, ekrana 1 basılır*/
}
```

ATAMA OPERATÖRÜ(=)

Bu operatçr binary, infix bir operatördür.Atama operatörünün sol tarafındaki operandın nesne olması gerekir.

Buradan hareketle ++ ve -- operatörlerinin operandlarının da nesne olması gerekir.

Atama operatöründe elde edilen değer sağ taraftaki operandın sayısal değeridir.

```c
void fonk(int n)
{
printf("%d\n", n);
}
void main (void)
{
int x = 10, y;
fonk(y = x);
}
```

```c
z = y = x = 10; ifadesi doğru olduğu gibi,
z = (y = 10) + 2; ifadesi de doğru ve geçerlidir.
```

İŞLEMLİ ATAMAM OPERATÖRLERİ(+=, -=, *=, /=)

Öncelik sırasında atama operatörüylesağdan sola eşit öncelik sırasında bulunurlar.

```c
void main (void)
{
int x = 12;
x += 5;/*x=x+5(sonuc 17)*/
x -= 5;/*x=x-5(sonuç 17)*/
x /= 3;/*x=x/3(sonuç 4)*/
}
```

Bu operatörlerin de sol tarafındaki operandları nesne olmalıdır.

VİRGÜL OPERATÖRÜ(,)

Binary, infiz bir operatördür ve en düşük önceliğe sahiptir.İki ifadeyi birleştirir.Önce sol taraf yapılır sonra sağındaki ifade yapılır.

```c
void main(void)
{
int x,y;
x = 10, y = 20;
printf("%d %d\n", x, y);/*x=10 y=20*/
}
```

, operatörü sağ tarafındaki ifadenin sayısal değerini üretir.

İstenilen operatörler parantez kullanılarak virgül dışına çıkarılabilirler.

```c
z = (x = 3,y = 4) + 2;/*iş1:x=3, iş2:y=4,iş3: ,=4 ,iş4:4+2=6, iş5:z=6*/
```

Her virgül virgül operatörü değildir.Örneğim fonk(a, b); buradaki virgül fonksiyon parametre ayıracıdır.

```c
fonk((a, b));buradaki , ise virgül operatörüdür.
```

NOKTALI VİRGÜLÜN İŞLEVİ

```c
a = b + c;/*iş1=b+c, iş2=a=iş1*/
```

; bir işlemin sonlandırıldığını anlatmak için kullanılır.Yani iki ; arasındaki kısım bağımsız olarak işlem sırasına göre yapılacaktır.Eğer ; unutulursa derleyici iki ifadeyi tek bir ifade zanneder.Bu da bir syntax error oluşmasına neden olur.(Error:Statement missing ; in function...)

```c
#include <stdio.h>
void main(void)
{
int x, y = 10;
x = y +2 =>Statement missing ; in funciton main
z = 10 + x;
printf("%d %d\n", x, y);
}
```

OKUNABİLİRLİĞE İLİŞKİN KURALLAR

1-İki space üst üste kullanılmaz,bir space'in yetmediği yerde bir tab kullanılır.Tab ayarının 4 yapılması uygundur.

2-Bütün fonksiyonlar ilk sütuna dayalı olarak yazılır.Fonksiyonlar arasında bir satır boşluk bırakılır.include satırlarından sonra da bir boşluk bırakılır.

3-Her bloğun için bir tab içeriden yazılır.

4-Binary operatörlerle operandlar arasında boşluk bırakılır(a = b). Bildirimden sonra bir satır boşluk bırakılır.

```c
int a;
a = 10;
```

5-Unary operatörlerle operandlar arasında boşluk bırakılmaz.

6-Mümkün olduğunca her satıra bir ifade yazılır.

7-Virgülden sonra bir boşluk bırakılır(önce değil).

8-Parantezlerden önce ya da sonra boşluk bırakılmaz.

9-Noktalı virgül bitişik yazılır

IF DEYİMİ

Bir ifadenin sonuna noktalı virgül konursa, buna deyim denir. Deyimler gruplara ayrılabilir.

1-Yalın deyimler:

ifade; biçimindekiler..

2-Birleşik deyimler:

```c
{
ifade1;
ifade2;
}
```

Bir bloğun içerisinde 1 ya da birden fazla deyim varsa ona bileşik deyim denir.

3-Bildirim deyimleri

4-Kontrol deyimleri

```c
if (...) {
}
```

Program akışı üzerinde etkili olan if gibi for, while gibi deyimlerdir.

5-Boş deyimler

Solunda ifade olmadan konulan ;'e boş deyim denir.

x = 10; ; ; son iki noktalı virgül boş deyimdir.

Boş deyim görüldüğünde derleyici hiçbir şey yapmaz.

IF DEYİMİNİN GENEL BİÇİMİ

1-

```c
if (ifade)
ifade;
else
ifade;
```

2-

```c
if (ifade) {
ifade1;
ifade2;
}
else {
ifade3;
ifade4;
}
```

If Nasıl Çalışır?

Derleyici if deyimindeki ifadenin sayısal değerini hesaplar.Bu değer 0 dışı bir değer ise if kısmı,ifadenin değeri 0 ise ifadenin else kısmı yapılır.

```c
void main(void)
{
int a;
printf("Sayı=");
scanf("%d", &a);
if (a >= 10 && a <=20)
printf("%d sayısı 10 ile 20 arasındadır\n", a);
else
printf("değildir\n");
}
```

Örnek:Klavyeden alınan iki sayının toplamının 100'den küçük olup olmadığını test eden programın yazılması:

```c
void main(void)
{
int a, b, c;
printf("İki sayı giriniz:");
scanf("%d %d", &a, &b);
c = a + b;
if (c < 100)
printf("%d 100'den küçüktür\n", c);
else
printf("%d 100'den büyüktür"\n", c);
}
```

KARAKTER TEST FONKSİYONLARI

C'de ismi "isxxxx" ile başlayan, geri dönüş değeri int, parametresi char olan bir grup fonksiyon vardır.

```c
x = isalpha('a');/*isalpha=alfanumerik mi?*//*x<>0*/
x = isupper('a');/*isupper=büyük harf mi?*//*x=0*/
```

Bu fonksiyonlar parametresiyle girilen karakterleri test ederler.Test olumluysa 0 dışı herhangi bir sayı ile geri dönerler, olumsuzsa 0 değerine geri dönerler.

Bu fonksiyonları kullanabilmek için ctype.h'ın include edilmesi gerekir.(#include <ctype.h>)

```c
#include <stdio.h>
#include <ctype.h>
void main(void)
{
char ch;
ch = getchar();
if (isupper(ch))
printf("%c büyük harf\n", ch);
else
printf("%c küçük harf\n", ch);
}
```

Örnek:isupper fonksiyonunun Türkçe veriyonunun istrkupper biçiminde yazılması.

```c
#include <stdio.h>
#include <ctype.h>
int istrkupper(char ch)/*baştaki int geri dönüş değerini gösteriyor*/
{
if (ch == 'Ç' || ch == 'Ş' || ch == 'İ' ||
ch == 'Ö' || ch == 'Ü' || ch == 'Ğ')
return 1;
else
return isupper(ch);
}
void main(void)
{
char ch;
ch = getchar();
if (istrkupper(ch))
printf("%c büyük harf", c);
else
printf"%c küçük harf", c);
}
```

Else kısmı olmayan if deyimi

```c
if (ifade) {
İfade1;
İfade2;
}
ifade3;
```

if’i yanlışlıkla boş deyimle kapatmak sıkça yapılan bir hatadır. Boş deyimle kapatılan if’ten sonraki deyim dolayısıyla if’in dışında düşünülür.

İç İçe if deyimler

Bir if’in doğruysa ya da yanlışsa kısmında başka bir if bulunabilir. Bir if doğruysa ya da yanlışsa kısmıyla birlikte dışarıdan bakıldığında tek bir deyim olarak ele alınır.

```c
if(ifade1){
if(ifade2){
ifade3;
ifade4;
}
else
ifade5;
ifade6;
}
else
ifade7;
ifade8;
```

İki if’den sonra gelen else içteki if’e aittir.

```c
if(ifade1)
if(ifade2)
ifade3;
else
ifade4;
ifade5;
```

Eğer bu else’in dıştaki if’in olması isteniyorsa bilinçli blok açılmalıdır.

```c
if(ifade1){
if(ifade2)
ifade3;
}
else
ifade5;
ifade5;
```

Else-if durumları

| if(ch == ’a’) printf(“a\n”); if(ch == ‘b’) printf(“b\n”); | if(ch == ‘a’) printf(“a\n”); else if(ch == ‘b’) printf(“b\n”); |
| --- | --- |

Else if durumları özellikle bir olasılık gerçekleştiğinde başka bir olasılığın gerçekleşme olasılığı mümkün olmadığı durumlarda karşılaştırma sayısını azaltmak için kullanılır.

İF DEYİMİNDE BOŞ DEYİMİN KULLANILMASI:

If deyiminin sonuna ; konulursa buradaki ; boş deyim demektir ve bütün if deyiminin biçimi değişebilir.

BÜYÜK KÜÇÜK HARF DEĞİŞTİRMESİ YAPAN FONKSİYONLAR:

```c
char toupper(chr chr)
```

toupper fonksiyonu parametresi ile belirtilen karakter küçük harf ise onun büyük harf karşılığı ile geri döner ; değil ise değişiklik yapmadan aynısı ile döner.Bu fonksyon kullanılırken "#include <ctype.h>" yapılmalıdır.

tolower parametresi ile belirtilen karakter büyük harf ise geri dönüş olarak onun küçük harf karşılığını verir. Değilse aynı karakter ile geri döner.

putchar FONKSİYONU:

Bu fonksiyon parametresi ile belirtilen fonksiyonun görüntüsünü ekrana basar.

eşdeğeri :

printf("%c",ch) dır.

DÖNGÜLER

Döngü bir programın belirli bir kısmının yinelemeli olarak çalıştırılmasını sağlayan kontrol deyimlerine döngü denir.

C'de döngüler ikiye ayrılır:

1--> while döngüleri

1-a-> kontrolun başta yapıldığı while döngüleri

1-b-> kontrolun sonda yapıldığı whilw döngüleri

2--> for döngüleri

Kontrolun başta yapıldığı while döngüleri:

"genel biçim"

```c
1> while (ifade)
ifade1;

2> while (ifade) {
ifade1;
ifade2;
}
```

while döngüsünün çalışma biçimi:

Derleyici while paranteszi içindeki ifadenin sayısal değerini hesaplar eğer bu nonzero ise döngünün devamına karar verilir ve döngü deyimleri çalıştırılır.

eğer ifadenin sayısal değeri 0 ise döngini çalışması sonlandırılır, programın çalışması döngü dışındaki ilk deyimle devam eder. eğer while parantezinden sonra bloklama yapılmış ise tüm blok döngü içindedir yapılmamış ise yanlızca ilk deyim döngü içindedir.

Sınıf çalışması:

Birden 100'e kadar (100 dahil) sayılarının toplamını döngü yoluyla hesaplayan bir program yazınız.

while döngüsü içinde virgül operatörüde sıklıkla kullanılır.

Bazı döngülerden while ifadesi ile çıkış mümkün olmayabilir. Bunlara "infinite loop" denir.

BREAK anahtar sözcüğü:

Kullanımı: break;

Programın akışı brewak anahtar sözcüğünü gördüğünde döngü kırılarak akış döngü dışındaki ilk deyimle devam eder.

Break anahtar sözüğü için bir döngünün içinde olmak gerekir dışarıda kullanılamaz.

While para bntezi içinde postpix bi işlem varsa arttırım(aynı şekilde eksiltim) önce döngünün devam etme veya etmeme kararı verilir sonra arttırım veya azaltım yapılır.

Kontrolun sonda yapıldığı :

```c
1--> do
ifade1;
while (ifade2);

2--> do {
ifade1;
ifade2;
.....
} while (ifade);
```

Bu tür while döngülerine ender olarak rastlanır.kontrol yapılana kadar döngü deyimleri en az bir kere çalıştırılır.

While döngülerinde boş deyimlerin kullanılması:

genellikle while döngüleri yanlışlıkla boş deyimle kapatılır.

while (++i<10); <-- hatalı

bazen while döngüsü bilinçli olarak boş deyimle kapatılabilir, bu durumda ; bir tab içeriden yazılmalıdır

FOR DÖNGÜLERİ:

Genel Biçim:

```c
1-->for (ifade1; ifade2; ifade3)
ifade4;

2-->for (ifade1; ifade2; ifade3;) {
ifade4;
ifade5;
....
}
```

Derleyicinin for anahtar sözcüğünden sonra bir parantez açılmasını ve parantez içerisinde iki noktalı virgül bulunmasını bekler. Bu iki ; for deyimini 3'e ayırır. Bu kısımlar ifade1 , ifade2 , ifade3 ile gösterilir.

For parantezinden sonra blok varsa bloğun içindekiler yoksa ilk deyim döngü içerisindedir.

For döngüsünün ilk kısmı döngüye ilk girişte bir defa yapılır, bir daha işlem görmez. İkinci kısmı ilk girişte ve her yinelemede döngünün devam edip etmeyeceğine karar verir. For döngüleri ikinci kısmın değeri 0 dışı bir değer olduğu sürece devam eder. Üçüncü kısım döngü deyimleri çalıştırıldıktan sonra dönüşte çalıştırılır.

```c
for(ilk değer; koşul; işlem) {
….
….
.…
}
```

Örnek:0’dan 99’a kadar olan sayıların görüntülenmesi.

```c
void main(void)
{
int i;
for(i = 0; i < 100; ++i)
printf(“%d\n”, i); /*99’a kadar olan sayıları basar*/
printf(“Son değere=%d\n”, i);/*100 değerini ekrana basacak*/
}
```

Örnek:1’den 100’e kadar olan sayıların toplamı.

```c
void main(void)
{
int i, total = 0;
for (i = 0; i < 100; ++i)
total = total + i;
printf(“Toplam=%d”, total);
}
```

Örnek:

```c
void main(void)
{
double i;
for(i = 0; i < 6.28; i = i + 0.01)
printf(“%lf\n”, i);
}
```

Örnek:

```c
void main(void)
{
char ch;
for(ch = getch(); ch != ‘q’; ch = getch())
putchar(ch);
}
```

Örnek:

```c
void main(void)
{
for(printf(“Birinci kısım\n”); printf(İkinci kısım\n”), getch !=’q’; printf(“üçüncü kısım\n”));
}
```

Sınıf çalışması:Birden 100’e kadar olan tek ve çift sayıların toplamını bulduracak program.

```c
void main(void)
{
int i, odd_sum = 0, even_sum = 0;
for(i = 1; i < 100; ++i)
if ((i % 2) == 0)
even_sum += i;
else
odd_sum += i;
printf("Tek sayılar=%d\n", odd_sum);
printf("Çift sayılar=%d\n", even_sum);
}
```

```c
i = 1;
for( ; i <100; ++i){ /*ifadesi tamamen geçerlidir*/
}

for(;;){ /*sonsuz döngü*/
}
```

İÇ İÇE DÖNGÜLER

```c
void main(void)
{
int i, k;
for(k = 0; k < 10; ++k)
for(i = 0; i < 10; ++i)
printf(“%d %d\n”, i, k);
}
```

SWITCH DEYİMİ:

bu deyim bir ifadenin çeşitli sayısal değerlerine karşı farklı işlemlerin yapılabilmesi için kullanılır.

Genel biçim:

```c
switch (ifade) {
case <s1>:
case <s2>:
case <s3>:
......
[default:]
}
```

switch deyiminin çalışma biçimi şöyledir:derleyici switch parantezi içindeki ifadenin sayısal değerini hesaplar, eğer bu sayısal değere uygun bir case ifadesi varsa program akışı oraya yönlendirilir, yoksa default (varsa şart değil) yönlendirilir. Eğer yoksa programın akıoşıo switch dışındaki ilk deyimle devam eder.

SABİT İFADESİ(CONSTANT EXPERSSİON)

Yanlızca sabitlerden ve operatörlerden oluşan ifadelere denir, yani değişken yoktur.

6

6/3

7+2

3+x(bu değil)

sabit ifadelerinin sayısal değeri derleme aşamasında belirlenir ve programın çalışması ile değişmez. C'de pek çok yerde ve durumda sabit ifadesine gereksinim duyulur. Örneğin "case" ifadeleri sabit ifadeleri olmak durumundadır.

case x+2 "olmaz"

case 3+5 "olur"

case 3/8 "olur"

BREAK anahtar sözcüğünün switch içindeki kullanımı:

Break anahtar sözcüğü switch içindede kullanılabilir bu durumda programın akışı switch dışındaki ilk deyime atlar.

her case ifadesi break ile sonlandırılırsa her durumda yalnızca bir case yapılmış olur.

case ifadelerinin okunabilir yazımı şöyledir eğer ifade çok küçük ise hepsi aynı satıra yazılabilir değil ise aşağıdaki satırdan ve bir tab içeriden yazılır.

Switch deyimi olmasa idi aynı şey en ekonomik else iflerle yapılabilirdi.

Ancak tipik switch kullanımlarını kaçırmamak gerekir. Case ifadelerin sırlaı gitmesi yada defaultun sonda olması zorunlu değil ama hoca sonda olsa iyi olur diyoo.case ifadeleri tam sayı türünden olmak zorundadır gerçek sayı türleri olmuyooo.çünkü yuvarlama hatasına göre iki sayı birbirine çok yakın olabilir ama eşit değildir bu durum programlamacıyı şaşırtabilir

Bir switch ifadesinde bir başka switch olabilir.

KOŞUL OPERATÖRÜ (CONDİTİONAL OPERATOR)

Koşul operatörü if deyimi gibi çalışan bir operatördür. İki sembolden oluşur ?: (C'deki tek üç değişken alan operatör) bu operatör şöyle çalışır....

1-->önce soru işaretinin solundaki ifade tam olarak yapılırburadan bir sayısal değer hesaplanır bu değer 0 dışı ise ? ile : arasındaki ifade değilse : dan sonraki ifade yapılır.

Koşul operatörü bir operatör oldğu için bir değer üretir. Ürettiği değer başka bir değişkene atanabilir yada işlemlerde kullanılabilir. bu operatörün ürettiği değer koşul ifadesinin durumuna göre ? : arasındaki ifade yada : dan sonraki ifadenin sayısal değeridir.(koşul operatörü ile yapılan herşey if deyimi ile de yapılabilir.)

Bu operatör öncelik tablosunda atama operatörünün hemen yukarısında bulunur.

derleyiciye göre koşul operatörünün tamamı tek operatördür. aşağıdaki ifadede iki operatör vardır.

b= a>0 ? 10+20 : 20+50

KOŞUL OPERATRÖRÜNÜN OPERANTLARININ AYRIŞTIRILMASI

derleyici ? dan sola doğru koşul operatöründen daha düşük öncelikli operatör görene kadar ilerler (bu operatör ya atamadır yada işlemlisidir atama operatörünün) o kısma kadarki ifade 1. operandı oluşturur. ? ile : arasındaki ifade 2. operant olarak ele alınır. derleyici : dan sağa doğru koşul operatöründen daha düşük öncelikli operatörü görene kadar ilerler o kısım 3. kısımdı

b= a>0 ? x : y =z

burada 3 operatör var

iki tane atama ve birdane de koşul

ancak parantez kullnılarak operantlar bilinçli olarak ayrıştırılabilir.

koşul operatörü ile yapılan herşey if deyimi ile karşılanabilir.

koşul operatörü üzellikle bir ifadenin sayısal değerinin karşılaştırma sonunda bir değişkene atanması gerektiği durumlarda okunabilirlik açısından tercih edilmelidir.Koşul operatörünün kullanılmasının tavsiye edildiği 3 durum vardır

1--> bir karşılaştırmanın sonucunun bir değişkene atandığı durumlar

b= a>10 ? 20 : 30

if eşdeğeri

```c
if (a>10)
b=20
else
b=30
```

2--> koşul operatörü return ile beraber kullanılabilir

return (a%3==0)? 1:0;

3--> bir fonksyon çağırılırken parametre yerinekoşul operatörüde konulabilir.

fonk (a%3==0 ? 10 : 20)

GOTO DEYİMİ

goto kullanım biçimi:

```c
goto <etiket>
.
.
etiket
```

goto özellikle karmaşık ifadeleri basitleştirmek için kullanılır. en tipik kullanımı içiçe döngülerden çıkmak yada döngü içinde switch varsa hem switch hem döngüden çıkmak için kullanılır.

Örnek:

```c
void main(void)
{
char ch;
for(;;){
ch = getch();
switch(ch){
case ‘x’: putchar(‘?’);break;
case ‘q’: goro EXIT;
default:
}
}
EXIT: printf(“Program sonu..\n”);
}
```

FONKSİYON PROTOTİPLERİ

C’de bir fonksiyonun çağırıldığını gören derleyici, çağırılma noktasına gelene kadar o fonksiyonun geri dönüş değerini tespit etmelidir. Çağırılma noktasına kadar geri dönüş değeri tespit edilmemişse C derleyicileri bu fonksiyonun geri dönüş değerinin int türünden olduğunu varsayarlar. Eğer çağrılan fonksiyon çağıran fonksiyonun daha yukarısında tanımlanmışsa derleyici derleme yönüne göre önce çağırılanı göreceği için çağırılma noktasına gelindiğinde çağırılan fonksiyonun geri dönüş değerini tespit etmiş olacaktır. Eğer çağırılan çağıranın daha altında tanımlanmış ise ve çağırılan fonksiyonun geri dönüş değeri int dışında bir değerse derleyici error verecektir.

```c
void main(void)
{
long x;
x = fonk();
printf("%ld", x);
}
long fonk(void)
{
return 100000; /*derleyici “type mismatch in redeclaration in fonk” error mesajını verir*/
}
```

Bir fonksiyonun geri dönüş değerini derleyiciye bildirim yolu fonksiyon prototipleridir. Fonksiyon prototipleri bir bildirim işlemidir. Yani derleyiciye bilgi verilmiş olur. Tanım yapılmamıştır henüz.

[geri dönüş değeri] <fonksiyon ismi> ([parametreler]);

Prototipler için en iyi bildirim yeri include satırlarının sonrasıdır. Bir önceki örnekteki hatanın düzeltilmesi:

```c
#include <stdio.h>
long fonk(void); /*fonk fonksiyonun prototipi*/
void main(void)
{
long x;
x = fonk();
printf("%ld", x);
}
long fonk(void)
{
return 100000;
}
```

STANDART C FONKSİYONLARININ PROTOTİPLERİ

Standart C fonksiyonlarının prototiplerinin mutlaka bildirilmeleri gerekir. Yoksa derleyici geri dönüş değerini int varsayar ve hata verir. Standart C fonksiyonlarını prototiplerini yazmak yerine o fonksiyonların prototiplerini bulunduran dosyaların include edilmesi yeterli olur.

stdio.h

conio.h

math.h

stdlib.h

TÜR DÖNÜŞTÜRMELERİ:

Farklı türlerin birbirine atanması:

bu konu 4 başlıkta incelenebilir:

1-->Büyük tamsayı türünün küçük tamsayı türüne atanması

2-->Küçük tamsayının büyuük tam sayı türüne atanması

3-->Gerçek sayıdan tam sayı türlerine yapıolan atamalar

4-->Tamsayı türlerinden gerçek sayı türlerine atamalar.

Büyük tamsayı türlerinden küçük tamsayı türlerine atamalar:

int=long

chr=int gibi durumlar incelenecektir.

büyük tür küçük tüğre atanırken sayının yüksek anlamlı byte değerleri atılır, düşük anlamlısı atanır yani bilgi kaybı sözkonusudur.(uyarı gerektirmez normal işlem olarak görülür.) Sayının yüksek anlamlı byte'ları kaybedildiği zaman sayı ilki ile ilgisiz hatta işaret değiştirmiş bile olabilir.

Küçük tamsayı türünün büyük tamsayı türüne atanması:

long =int

int=char gibi durumlar

Böyle bir atamada bilgi kaybı sözkonusu olmaz. Ancak tabi sayının işareti korunarak atanmaktadır. Eksi atıyorsak yüksek anlamlı bytelar ffff ile doldurulur. Pozitif atanıyor ise büyük türün yüksek anlamlı byteları 0000 ile doldurulur.

Gerçek sayı türlerinden tam sayı türlerine yapılan atamalar:

int=float

long double

Sayının noktadan sonraki kısmı atılır geri kalanı atanır.

gerçek sayıu nokta kısmı atıldıktan sonra atanankısma yine sığmıyorsa bir dönüştürme daha yapılır.(örneğin 116517.3)

Tam sayı türlerinden gerçek sayı türlerine yapılan atamalar:

float=long

Bu durumda sayı .0 biçiminde atanır.

İŞLEM ÖNCESİ OTOMATİK TÜR DÖNÜŞTÜRMELERİ:(acaip önemli imiş)

C derleyicileri bir operatör ile karşılaştığında önce operantların türlerini araştırır, eğer ikiside aynı ise işlem doğrudan yapılır; eğer farklı türlerden ise önce operantlar aynı türe dönüştürülür sonra işlem yapılır. Özet olarak küçük tür büyük türe dönüştürülür. Küçük türün büyük türe dönüşümünde yukarıdaki kural uygulanır, yani bilgi kaybı yoktur ve işareti korunur.

c de iki operantda tam sayı türlerine ilişkin ise bölmenin sonucu tam sayı çıkar.

at5 te bilgi kaybı var. işlemin sonucu negatif çıkıyor çünkü long int'e atanıyor .

İşlem öncesi tür dönüştürmeleri yalnızca aritmetik operatörlerle değil ilişkisel operatörlerlede yapılmaktadır.

at4 de FC yi inte dönüştürürken fffc olarak dönüşütürülür.ama unsignedchar olarak dönüşütürürsek 00fc olarak dönüşür.

TÜR DÖNÜŞTÜRME OPERATÖRÜ:

Unary prefix bir operatördür ve aşağıdaki gibi kullanılır.

(tür) operant

Bu operatör öncelik tabvlosund ikinci düzeyde sağdan sola bulunur

Dönüştürme işlemi bir işlemlik yapılıyordur.

(long)(a*b)--> burada a*b ddönüşütürülüyor.

Küçük türün büyük türe dönüştürülme olayının istisnaları:

1--> Integral promotion:

Char ve/veya short işlemlerinde heriki operantta int'e dönüşütürülür. sonuç int türünden çıkar.

char + char --->int oluyor

(char) char+char ---> char'a bilinçli dönüştürülüyor.

2-->

Aynı türün işaretli ve işaretsiz versiyonların işleme sokulur ise sonuç işaretsiz çıkar(bilgi kaybı oluşmaması için).

int + unsigned int --> unsigned int olur

unsigned int + long---> long olur.

3-->

Float ve long arasındaki işlemlerde floata doğru dönüşütürme yapılır.

4-->

İşaretli bir tür işaretsiz bir türe dönüştürülürse sayının bit durumları değişmez. En yüksek anlamlı bit işaret biti olmaktan çıkar ve sayıyı oluşturan bir bit haline gelir. Benzer biçimde işaretsiz bir tür işaretli bir türe dönüştürülürse en yüksek anlamlı bit işaret biti olarak yorumlanır.

5-->

İşaret dönüştürmek için kullanılan + - ler unary prefix operatördürler.

- operatörü -1 ile çarpılıyormuş gibi bir etki yaratır.

ÖNİŞLEMCİ KAVRAMI VE SEMBOLİK SABİTLER:

Derleyiciler iki modülden oluşur;Önişlemci modülü ve derleme modülü;

Derleme işleminin tüm işlemleri derleme modülü tarafından yapılır.

Önişlemci kaynak kodu üzewrinde çeşitli değişiklikler ve düzenlemeler yapan derleyicinin ön bir modülüdür.

C'de # ile başlayan satırlar önişlemciye aittir yani Öİ sadece # ile başlayan saturlarla ilgilenir.# den sonra bir Öİ komutu bulunur. bu komut Öİ ye yapması gerekenleri anlatır.(#include ve #define ele alınacaktır)

#INCLUDE komutu:

komutun yanında açısal parantez yada ""içinde bir dosya ismi vardır.Öİ ilgili dosyayı diskte bulur komutun yazılı olduğu yere kopyalar, program derleme modülüne geldiğinde burada artık o dosya vardır.

bu komut kaynak kodun herhangi bir yerine yerleştirilebilir nereye yerleştirilirse oraya açılır.Dosya açısal parantezler içinde ise ilgili dosya yalnızca derleyici tarafından belirlenen dizinde aranır orada yoksa yoktur bu dizin pek çok compilerde değiştirilebilir

options\directories\include directories de bulunur.

C standart başlık dosyaları açısal parantezler ile ifade edilirler.

eğer uyguın dosya yoksa ön işlemci bunu error mesajı ile bildirir.

Eğer dosya ismi iki tırnak ile belirtilmiş ise Öİ önce dosyayı bulunulan dizinde arar burada bulamazsa bu kezde derleyici tarafından belirlenen dizinde bakar.

geleneksel olarak programcının yarattığı dosyalar "" içerisinde belirtilirler.

Bir dosyanıın include olması için h uzantılı olması gerekmez.

Öİ açtığı dosyadan hareket ederek oradaki Öİ komutlarını da yapar.

```c
/*--x1.c--*/
#include <stdio.h>
#include "X2.c"
void main(void)
{
clrscr();
printf("%d\n",add(10,20));
printf("%d\n",multiply(10,20));
}
/*----*/
```

```c
/*--x2.c--*/
#include "X3.c"
int add(int a,int b)
{
return a + b;
}
/*-----*/
```

#define KOMUTU

#define str1 str2

Bu komut tıpkı text editörlerdeki bul ve değiştir özelliğinde olduğu gibi bir yazıyı başka bir yazı ile yerdeğiştirir. Hesaplama yapmaz. Öİ define anahtar sözcüğünden sonraki ilk boşluksuz karakter kümesini alır, buna str1 diyelim, daha sonra satır sonuna kadarki tyüm karakterlerin kümesini alır , buna str2 diyelim, kaynak kodda str1 gördüğü yere str2 yazısını yerleştirir.

Bir yazıya karşılık bir sayı getirilmesi durumuna sembolik sabit tanımlama denir. define edilmiş bir sembolik sabit başka define ifadelerinde kullanılabilir. #define ile operatör vs. değiştirilemez yalnızca anahtar sözcükler ve değişkenler değiştirilebilir

#define + - ERROR

#define 300 200 ERROR

değiştirme işleminde büyük küçük harf duyarlılığı vardır. Sembolik sabitler genellikle büyük harflerle yazılırlar bu durum onların program içinde kolay farkedilmesini sağlar. #define komutu include dosyaların içinde de bulunabilir.

Okunabilir formu:

define dan sonra boşluk ve sonrada yeterince tab

sembolik sabitin yazılmış olması kullanımını zorunlu kılmaz.

bazı standart sembolik sabitler belirtilmişrtir

örneğin math.h içinde pek çok matematiksel sabit vardır tabi bu sabitlerin kullanımı için math.h ın include edilmesi gerekir.

En ünlü sembolik sabit #define NULL 0 dır(stdio.h içinde).

2. string yazılmamış ise bu durum birincisinin silineceği(yerine boşluk atar) anlamına gelir.

Sembolik sabitler neden kullanılır:

1--> Okunabilirlik arttırmak için

sayılar yerine onları anlatan yazıların kullanılması kodun daha iyi anlamlandırılmasını sağlar.

2--> Bir sabit programın pek çok yerinde kullanılıyorsa sabitin değiştirilmesi tek yerden yapılabilir.

!!!!!! DİZİLER !!!!!!

ADRES KAVRAMI:

Bellek byteların peşisıra dizilmesinde oluşur. Donanımsal olarak her byte ın bir fiziksel adres numarası vardır.En tepedeki byte 0 olmak üzere her byte ın artan sırada bir adres numarası vardır. Fiziksel adres numaraları 16'lık sisitemde belirtilirler.

Yazılımsal olarak adres bilgisinin bileşenleri:

1-->(Fiziksel adres numarası) sayısal bileşen

2-->Tür bileşeni

Sayısal bileşen ilgili bölgenin fiziksel adres numarasını belirtir.

Tür bileşeni sayısal bileşnle belirtilen bellek bölgesindeki bilginin hangi türden yorumlanacağını anlatır. Örneğin sayısal bileşeşn 1FC0 tür bileşeni char ise burada şu anlaşılır:

1FC0 fiziksel adres numarasındaki bilgi karakter olarak yorumlanacaktır.

Adres bilgisi c'de ayrı bir veri türüdür. bu durumda c'deki veri türleri 3'e ayrılır.

1--> tam sayı türleri

2--> gerçek sayı türleri

3--> adres bilgisi

C'de her değişkenin bir adresi söz konusudur.

Bir byte tan uzun olan değişkenlerinin adreslerinin sayısal bileşenleri onları düşük anlamlı byte'larının fiziksel adres numarası ile belirtilir.

ADRES SABİTLERİ:

Adres türünden sabitler yazılabilir

genel biçim :

(int *) 0x1FC0

DİZİLER

Elemanları aynı türden olan bellekte ardaşıl bir biçimde bulunan veri yapılarına dizi denir.

Dizi bildiriminin yapılması:

genel biçim:

<tür>dizi ismi [uzunluk];

chr s[10]; s 10 elemanlı bir karakter dizisidir.

int sample[24];

float t[40]; t 40 elemanlı bir float dizisidir.

dizinin istenen elemanına ulaşmak için "dizi ismi[index]"

Bir dizi bildirimi ile karşılaşan derleyici dizinin tüm elemanlarını tutacak uzunlukta bellekte yer ayırır. Dizinin her elemanı diğerlerinden bağımsız bir nesne imiş gibi kullanılabilir. İndex ifade tanımına uyan herşey olabilir.dizinin ilk elemanın indisi 0 dır.

Bir dizinin en önemli kullanım gerekçesi bir indşis yardımı ile bir döngü içerisine dizinin tüm elemanlarının taranmasıdır.

Eger yerel bi dizinin içerisine değerler atanmamış ise o dizinin içerisinde rastgele değerler bulunur.

Dizilere ilk değer verilmesi:

int a[10]={1,2,3,4,5,80,90,100,4,7}; şeklinde verilebilir

tür dizi ismi[uzunluk]={0,2,.....};

dizi elemanlarına ilk değer küme parantezleri içerisinde elemanlar arasına , konularak verilir bu durumda derleyici küme parantezi içerisindeki sayıları sırası ile dizi elemanları içine yerleştiriler.

bir dizinin az sayıda elemanına ilk değer verilebilir bu durumda diğğer elemanlar dizi yerelse rastgele global ise 0 alırlar.

bir diziye uzunluk belirtmeden ilk değer verilebilir bu durumda derleyici verilen ilk değerlerin sayısını bulur ve dizinin o uzunlukta açılmış olduğunu varsayar.

int a[]={1,5,45,96}

derleyici bir dizinin uzunluğunu o dizi için kaç byte yer ayıracağını tespit etmek için derleme sırasında bilmek zorundadır. o nedenle c de dizi uzunlukları sabit ifadesi biçiminde verilmek zorundadır.

Bir dizinin en büyük ve en küçük elemanının bulunması:

Bu işlem için önce dizinin ilk elemanı en büyük yada en küçük kabul edilip değişken içerisinde sakalnır. sonra dizinin tüm elemanları bir döngü içerisinde taranır. daha büyük veya daha küçük görüldükçe bu değişkenin içerisindeki değer değiştirilir.

Dizilerin sıraya dizilmesi:(sortinng)

Dizilerin sıraya dizilmesinde pek çok algoritmik yöntem vardır. hız ve performans dizinin dağılımı ile ilişkilidir ancak rastsal bir dağılım sözkonusu ise en iyi performansı quick sort yönteminin gösterdiği söylenebilir.

Bubble Sort:

bu algoritmada yanyana iki eleman karşılaştırılır eğer koşul sağlanıyor ise yerdeğiştirilir. bubble sort algoritması içiçe n-1 defa dönen döngü biçiminde tasarlayabiliriz

```c
#include<stdio.h>
#define SIZE 10
void main (void)
{
int a[SIZE] = {3, 8, 6, 41, 16, -7, 25, 63, 57, 45};
int temp,i,k;
clrscr();
for (i = 0;i < SIZE -1;++i)
for (k = 0;k < SIZE - 1 - i;++k)
if (a[ k] > a[k + 1]) {
temp = a[k];
a[k] = a[k + 1];
a[k+1] = temp;
}
for (i = 0;i < SIZE;i++)
printf("%d\n", a[i]);
}
```

Selection Sort:

bu yöntemde duruma göre en büyük yada en küçük eleman bulunur bu eleman ilk elemanla yerdeğiştirilir bu işlem dizi daraltılarak yinelenir.

```c
#include <stdio.h>
#define SIZE 10
void main (void)
{
int a[SIZE] = {3, 8, 6, 41, 16, -7, 25, 63, 57, 45};
int min,indis,i,k;
clrscr();
for (i = 0;i < SIZE - 1;++i) {
min = a[i];
indis = i;
for (k = i + 1;k < SIZE;++k)
if (a[ k] < min) {
min = a[k];
indis = k;
}
a[indis] = a[i];
a[i] = min;
}
for (i = 0;i < SIZE;++i)
printf("%d\n", a[i]);
}
```

sınıf çalışması :

klavyeden bir sayı isteyen bu sayıyı 10 elemanlık bir int dizi içerisinde arayan bulursa bulduğu yerin indisini yazdıran bulamazsa bulamadığını belirten bir program yazınız.

```c
#include <stdio.h>
#define SIZE 10
void main (void)
{
int a[10] = { 3,8,6,41,25,18,-7,65,57,45};
int i,k;
clrscr();
printf("bir sayi giriniz:=>");
scanf("%d",&k);
for(i = 0;i<SIZE;++i)
if (k == a[i]) {
printf("%d sayisini %d numarali indiste yani %d . eleman olarak buldum",k,i,i+1);
return;
}
printf("bi daha dene.. ");
}
```

C'de bir dizi bildirirken sabit ifadesi ile bildirmek gerekir. Derleme aşamasında dizinin uzunluğunun ne kadar olduğunun bilinmesi gerekir. Dizi uzunluğuna göre derleyici yer ayırmalıdır.

Karakter Dizileri

Her elemanı karakter olan dizilerdir(NULL karakteri = '\0'). Karakter dizileri sayısal ya da yazısal amaçlarla kullanılabilir. Eğer yazısal amaçla kullanılacaksa dizinin her elemanına yazının bir karakteri yerleştirilir. Böylece karakter dizisi bir yazıyı tutar hale gelir. Ancak dizi içerisindeki yazının da nerede sonlandığı belirlenmelidir. Bunun için C'de yazının sonuna NULL karakteri yerleştirilir. NULL karakteri ASCII tablosunun sıfırıncı elemanıdır ve değeri sıfırdır. Bu durumda C'de n elemanlı bir dizinin içerisine sonuna NULL karaktre konulması gerektiği için en fazla (n-1) eleman yerleştirilebilir.

Karakter Dizilerine İlk Değer Verilmesi

char s[50] = {'A', 'n', 'k', 'a', 'r', 'a', '\0'};

İlk değer verirken mutlaka en son karakter NULL karakter olmalıdır.

char s[5] = "Ankara";

Bu durumda derleyici çift tırmak içerisindeki karaktreleri sırasıyla dizi içerisine yerleştirir ve sonuna NULL karakter koyar.

char s[] = "Van";

Bu durumda derleyici 4 elemanlı bir dizi açar.

char s[5] = "İstanbul"; /* Derleyici hata verir. */

Dizinin eleman sayısı atanan değeri eleman sayısından küçük ise hata oluşur. Ama eşit olursa hata vermez.

char s[3] = "Van";

Bu durumda, yani sayılar eşit olduğunda dizinin sonuna NULL karakteri konmaz ve derleyici uyarı vermez.

Klavyeden Bir Karakter Dizisinin Okunması

gets(dizi_ismi);

Bu fonksiyon enter tuşuna basılana kadar girilen tüm karakterleri sırasıyla diziye yerleşirir ve sonuna NULL karakterini yerleştirir. get fonksiyonunun kullanışında okutulan n elemanlı dizi için (n-1) eleman girilmelidir. Çünkü gets fonksiyonu yazının sonuna NULL karakteri koyacaktır. Okutulan n elemanlı dizi için (n-1)'den fazla eleman girilirse oluşacal duruma dizi taşması denir.

Karakter Dizilerinin Ekrana Yazılması

puts(dizi_ismi);

Bu fonksiyon karakter dizisini ekrana NULL karakter görene kadar yazar, NULL karakterini görünce durur. Eğer NULL karakter bir şekilde ezilmiş ise puts istenilen yerde durmaz. Bu fonksiyonun işi printf fonksiyonu %s parametresiye çağırılarak da yapılabilir. Tek farkı puts farklı cursor'ı alt satıra geçirir.

DİZİ İSİMLERİ

(CHAR *) 0X1FC0

Dizi elemanları bellekte ardaşıl bir biçimde bulunurlar yani iki eleman arasında hiç boşluk yoktur. dizi isimleri nesne değil ADRES SABİTİ belirtir. Bir dizi ismi yazıldığında derleyici sayısal bileşeni dizininn bellekteki başlangıç adresi olan tür bileşeni ise dizinin türü ile aynı olan bir adres sabiti yazar. Yani dizi isimleri derleyici tarafından adres sabitlerine dönüştürülür.

Bir adresin sayısal bileşeni printf fonksyonu ile " %p "formatında yazdırılır.

POINTERS (GÖSTERİCİLER)

10 --> int a;

20L --> long b;

3.2 --> double c;

(char*)0x1FC0

İçlerine adres bilgilerinin yerleştirildiği değişkenlere "gösterici" denir.

:Gösterici bildirimlerinin genel biçimi:

<tür>*<gösterici ismi>;

örnekler

int *p; ----> p int türünden bir göstericidir.

float *abc; ----> abc float türünden bir göstericidir.

....

okunabilir formu * ile gösterici isminin birleşik yazılmasıdır.

int *p,a,*c ----> aynı satırda birden çok bildirim yapılabilir.

int *p

p=(int*)0x1BC3 doğru:: gösterim.

char *p;

p=(int*)0x1A13; hata:: gösterici ile adres bilgisi farklı türlerden.

char *p;

p=0x1234; hata:: adres ataması bile yapılmamış.

Bir göstericiye aynı türden bir adres bilgisi konulmalıdır. Bir göstericiye adres bilgisi atandığında göstericiye adresein yalnızca sayısal bileşeni yerleştirilir.

Bir dizinin ismi aynı türden bir göstericiye atanabilir. Çünkü dizi isimleri aynı türden bir adres sabiti belirtmektedir.

char *p;

char s[100];

p=s; s yerine (char*)0x1A00

char *p;

p=(char*)0x1F10;

*p='a'

bir gösterici * operatörü ile kullanılabilir.*p ='a' gibi bir işlemde *p ifadesi p'yi değil p göstericisinin içerisindeki adresteki bilgiyi temsil eder. * unary prefix bir gösterici operatörüdür.

p bir gösterici olmak üzere *p bir nesnedir. her nesnenin bir türü vardır. *p nesnesinin türü bildirimde açıkça belirtilmiştir.

Aşağıdaki gibi bir gösterici bildiriminden iki şey anlaşılır:

1--> p karakter türünden bir göstericidir.

2--> p göstericisinin * operatörü ile kullanımında "*p" karakter türündendir.

gösterici içerisine bir adres yerleştirilirse belleğin istediğimiz bir yerindeki bilgiye erişip okuyabiliriz.

GÖSTERİCİ OPERATÖRLERİ:

c'de adresler üzerine işlem yapan operatörlere gösterici operatörü denir.

c'de 3 tane gösterici operatör vardır.

* --> indirection

& --> address of

[n] --> index

* OPERATÖRÜ

unary prefix bir operatördür. operantının mutlaka ve mutlaka adres bilgisi olması gerekir. Yani * operatörü :

1--> Doğrudan adre

....

*p * 10

* gösterici operatörünün operantı c nin normal türlerine ilişkin bir bilgi olmaz adres bilgisi olmak zorundadır.

& OPERATÖRÜ

BU operatörde unary prefix bir operatördür.bir değişkenin bellekteki yerleşim adresini elde etmek için kullanılır. BU operatör ile elde edilen adresin sayısal bileşeni operant olarak alınan adresin fiziksel adres numarası tür bileşeni ise nesnenin türü ile aynı olan türdür.Bir nesnenin adresi bu operatör ile alınıp bir göstericiye konulursa daha sonra bu gösterici * operatörü ile kullanıldığında daha sonra bu nesneye erişilmiş olur.

[] INDEX OPERATÖRÜ

Unary postfix bir operatördür. Öncelik tablosunun en üst düzeyindedir.

Kullanımı:

köşeli parantez içindeki ifade int türüne dönüştürülür otomatik olarak. Bu operatörün operantının bir adres bilgisi olması gerekir. yani operant

1- >bir gösterici olabilir.

2- >dizi ismi olabilir.

3- >adres sabiti olabilir.

*(p+n)=p[n] ile tamamen eşdeğerdir.

bu operatör bir adresten n ilerinin içeriğini almakta kullanılır.

FONKSYON PARAMETRESİ OLARAK GÖSTERİCİLERİN KULLANIMI:

bir fonksyonun parametre değişkeni gösterici türünden olabilir.böyle fonksyonlar birer adres bilgisi ile çağırılmalıdır. Bu durumda derleyici fonksyon çağırıldığında adres bilgisini otomatik olarak göstercinin içine yerleştirir. C'de bir yerel değişkenin içeriğinin başka bir fonk tarafından değiştirilebilmesi ancak şöyle mümkündür:

Fonk yerel değişken adresi ile çağırılır, fonk parametre değişkeni aynı türden bir göstericidir. bu gösterici * ile kullanılırsa yerel değişkene erişilmiş olur.

[ Bir göstericinin içerisine aynı türden bir adres bilgisi konulabilir bunun tersi de doğrudur yani bir adres bilgisinin atanacağı değişken aynı türden gösterici olmak zorundadır.]

DİZİLERİN FONKSYONLARA PARAMETRE OLARAK GEÇİRİLMESİ

diziler bellekte sürekli ardaşıl bir biçiimde bulunduklarına göre onların başlangıç adreslerini geçirerek bir fonk diziye erişmesini sağlayabiliriz. karakter dizilerinin başlangıç adresi yeterlidir. çünkü dizinin başlangıç adresini alan fonksyon null karakter görene kadar ilerlerse dizi içindeki yazının hepsine erişebilir. karakter dışındaki türlere ilişkin dizilerin başlangıç adreslerinin yanısıra birde uzunluklarının geçirilmesi gerekir. örneğin puts fonksyonu aslında dizinin başlangıç adresini parametre olarak almaktadır bu durumda puts fonk parametre değişkeni karakter türünden gösterici olmak zorundadır. bu durumda fonksyon dizinin başlangıç adresi ile yani dizinin ismi ile çağrılır. fonk parametre değişkeni aynı türden bir gösterici olmalıdır.

ADRESLERİN ARTTIRILMASI VE EKSİLTİLMESİ:

bir adres bilgisini bir artırdığımızda adresin sayısal bileşeni adresin türünün uzunluğu kadar artar. yani int bir göstericiyi 1 artırdığımızda dos'ta adresin sayısal değeri 2 artacaktır. bir adres bilgisine int türden bir sayı ile toplarsakda elde edilen adresin sayısal bileşeni adresin türünün uzunluğu kadar artacaktır. örneğin p[n] ifadesi p adresinden n byte ilerinin içeriği değil "p adresinden n*p'nin türünün uzunluğu kadar ilerinin içeriği anlamına gelir."

```c
#include <stdio.h>
void main(void)
{
int a[5] = {100, 200, 300, 400, 500};
int *p;
clrscr();
p=a;
printf("%d\n", p[2]);
}
```

GÖSTERİCİLER VE DİZİLERİN BENZERLİKLERİ VE FARKLILIKLARI

1--> Göstericide dizi ismide adres bilgisidir. gösterici kullanıldığında göstericinin içerisindeki adres kullanılır dizi ismi kullanıldığında dizinin başlangıç adresi sabit olarak kullanılır.

2--> Gösterici bir nesnedir yani içerisine bir bilgi atanabilir oysa dizi ismi dizinin başlangıç adresine ait bir sabittir.yani diiznin ismi diiznin ilk elemanının adresi gibi bir anlamdadır.

3--> bir gösterici tanımlandığında yalnızca kendisi için yer ayrılır. ayrılan alan dosta 2 veya 4 byte; unix ve win32 de her zaman 4 byte yer ayrılmaktadır. bir gösterici için ayrılan alanın göstericinin tür ile hiç bir ilgisi yoktur. göstericinin türü göstericinin gösterdiği yer ile ilgilidir.

ÖRNEK:Bir int dizinin başlangıc adresinmi ve uzunluğunu alarak dizinin en büyük elemanına geri dönen bir fonksyonun tasarımı:

```c
#include <stdio.h>
int c=0;
int MaxVal(int *p, int n)
{
int max = p[0];
int i;
for (i = 1; i < n; ++i)
if (max < p[i]) {
max = p[i];
c=i;
}
return max;
}
void main(void)
{
int a[]={10,20,30,40,50,60,70,80,90,50};
int m;
clrscr();
m = MaxVal(a,10);
printf("%d %d\n",m,c);
}
```

ÖRNEK:n elemanlı bir int diziyi sıraya sokan sort isimli bir fonksiyon yazınız...prototipi sort(a,10); a = dizi ismi

10 = uzunluk

```c
void sort(int *p,int n)
{
int deis,i,j;
for (i = 0; i < n - 1; ++i)
for (j = 0; j < n - 1; ++j)
if (p[j] > p[j + 1]) {
deis = p[j];
p[j] = p[j + 1];
p[j + 1] = deis;
}
}
void main (void)
{
int a[]={1, 8, 9, 17, 6, 4, 41, -7, 20, 40};
int k;
clrscr();
sort(a,10);
for (k = 0; k < 10; ++k)
printf("%d\n",a[k]);
}
```

:String Fonksyonları:

standart c de başı str ile başlayan bir karakter dizisinin başlangıç adresini parametre alarak dizi içerisindeki yazı üzerinde çeşitlli işlemler yapan bir grup fonksyon vardır. bunlara string fonksyonları denir ve prototoipleri string.h içerisindedir.

strlen fonksyonu:

int strlen (char *str);

bu fonksyon parametre olarak aldığı adresten başlayarak null karakter görene kadar yazı içerisinde kaç karakter bulunduğunu hesaplar ve bu değerle geri döner.

```c
int mystrlen(char *str)
{
int i = 0;
while (*str != '\0') {
++str;
++i;
}
return i;
}
```

```c
int mystrlen(char *str)
{
int i = 0;
while (str[i] != '\0')
++i;
return i;
}
```

```c
int mystrlen(char *str)
{
int i;
for (i = 0;str[i] != '\0';++i)
;
return i;
}
```

Geri dönüş değeri adres olan fonksyonlar:

bir fonksyon herhangi türden bir adrese geri dönebilir. böyle fonksyonlar tanımlanırken geri dönüş değeri türü yerine <tür>* yazılmalıdır.

int *fonk(void)

yıldız olmasa int anlaşılacaktu ama * varken int türünden adres sabiti.

okuynablirlik gereği *ile fonksyon bitişik yazılır. böyle fonksyonların geri dönüş değerleri aynı türden bir göstericiye atanmalıdır.

STRCHR fonksyonu: bu fonksyon bir yazı içerisinde bir karakteri aramakta kullanılır. prototipi: char *strchr(char *str,char ch)

fonksyonun birinci parametresi aramanın yapılacağı yazının başlangıç adresine yönelik göstericidir. ikinci parametre aranacak karakteri belirtir. C'DE 0 ADRESİ GEÇERLİ BİR ADRES DEĞERİ DEĞİLDİR. Bu fonksyon karakteri yazı içerisinde bulursa bulduğu yerin adresi ile bulamazsa 0 ile geri döner. Bu bir başarısızlık işaretidir . 0 adresine null gösterici denilmektedir.

SINIF ÇALIŞMASI:Bir yazı içerisindeki belli bir karakterli başka bir karakterle değiştiren replace fonksiyonunu yazınız.

prototipi:=> void replace(char *str,char a,char b)

Bu fonksiyon strchr fonksiyonu yardımıyla yazılacaktır.

```c
#include <stdio.h>
#include <string.h>

/* Başka bir replace */
/*void replace(char *str,char a,char b) */
/*{ */
/* int c,i; */
/* */
/* c = strlen(str); */
/* for (i = 0;i < c;++i) */
/* *strchr(str,a) = b; */
/*} */
/* */
/* Başka bir replace */
/*void replace(char *str,char a,char b) */
/*{ */
/* for (;;) { */
/* str=strchr(str,a); */
/* if (str == NULL) */
/* break; */
/* *str = b; */
/* } */
/* ++str; */
/*} */
/* */

void replace(char *str,char a,char b)
{
int c,i;
while (strchr(str,a) != NULL)
*strchr(str,a) = b;
}
void main (void)
{
char s[] = "Bu bir denemedir";
clrscr();
replace(s,'e','x');
puts(s);
}
```

STRCPY fonksiyonu:

Bu fonksiyon bir karakter dizisi içindeki yazıyı başka bir karakter dizisine kopyalamak için kullanılmaktadır.

Prototipi:=> char *strcpy(char dest,char source);

İkinci parametresinden başlayarak null karaktere kadar (null karakter dahil) olan tüm karakterleri ilk parametredeki adresten başlayarak yerleştirir.

Fonksiyon birinci parametresiyle belirtilen yani kopyalamanın yapıldığı adresin kendisine geri döner.Geri dönüş değeri nadiren kullanılır.Bunun amacı: printf("%s\n",strcpy(d,s)); şeklinde kullanılsın..

STRRCHR fonksiyonu:

Prototip:=>char *strrchar(char *str,char ch);

Bu fonksiyon yazı içerisinde karakteri ararken son bulduğu yerin adresiyle geri döner.Oysa strchr ilk bulduğu adresle geri dönmektedir.strchr ve strrchr fonksiyonları ile NULL krakterin kendisi de aranabilir. p=strchr(s,'\0');

p karakter türünden bir gösterici olmak üzere p'nin null karaktere ötelenmesi aşşağıdaki 3 biçimde yapılabilir.

```c
1-while(*p !='\0')
++p;

2-p += strlen(p);

3-p = strchr(p,'\0');
```

1 ve 3 iyi 1 hızlı...

STRCAT FONKSYONU:

Bu fonksyon bir ayzının sonuna başka bir yazıyı eklemek amacı ile kullanılır.

char *strcat(char *dest, char *source)

bu fonksyon ikinci parametresinde belirtilen adresyen başlayarak null karakter görene kadar (dahil) tüm karakterleri birinci parametresinde belirtilen yazının sonuna kopyalar. Kopyalamanın yapıldığı yani birnci parametresi ile belirtilen adresin kendisine geri döner ancak geri dönüş değeri nadiren kullanılır.

```c
#include <stdio.h>
#include <string.h>
void main (void)
{
char s[50] = "ankara";
char d[50] = "istanbul";
strcat(d, s);
printf("%s\n", d);
}
```

```c
char *mystrcat (char *dest, char *source)
{
char *temp;
temp=dest;
while(*dest != '\0')
++dest;
strcpy(dest,source);
return(temp);
}
```

STRCMP FONKSYONU:

bu fonksyon iki yazıyı karşılaştırmakta kullanılır.

int strcmp(char *s1, char *s2);

bu fonksyon iki yazının da başlangıç adreslerinin kopyalandığı iki gösterici parametresi alır birincisi büyükse pozitif küçükse negatif herhangi bir değere eşitse 0 a geri döner.

```c
#include <stdio.h>
#include <string.h>
void main (void)
{
int result;
char passwrd[] = "mavi ay";
char s[50];
printf("enter password:");
gets(s);
if (!strcmp(s, passwrd))
printf("OK....\n");
else printf("invalid password...\n");
}
```

SINIF ÇALIŞMASI: kullanıcıdan en fazla 3 kere password isteyen 3ündede yanlışsa invalid password yazan doğru girilmişse OK yazısını çıkartan programı yazınız. her hatalı girişte password doesnot match enter password yazısı tekrar çıkacak.

```c
#include <stdio.h>
#include <string.h>
#define TRYNUM 3
void main (void)
{
int i, j = 0;
char password[] = "mavi ay";
char s[50];
clrscr();
for(i = 0; i < TRYNUM; ++i){
if (j == -1)
printf("Password does not match\n");
else if(j == 1)
break;
printf("Enter password:");
gets(s);
if (!strcmp(s, password))
j = 1;
else
j = -1;
}
if (j == 1)
printf("OK..\n");
else
printf("Invalid password\n");
}
```

standart olmamakla birlikte library içinde stricmp isminde büyük küçük harf duyarlılığı olmadan karşılaştırma yapan bir fonksyon da vardır bu fonksyon derleyicilerin çoğu tarafında destekler.

STRUPR ve STRLWR FONKSYONLARI:

char *strupr(char *str);

char *strlwr(char *lwr);

bu iki fonksyon null karakter görene kadar bir yazı içindeki tüm karakterleri büyük yada küçük harfe çevirir.

```c
#include <stdio.h>
#include <string.h>
void main (void)
{
char s[50];
gets(s);
strlwr(s);
puts(s);
strupr(s);
puts(s);
}
```

STRNCPY FONKSYONU:

char *strncpy(char *dest,char *source, int n);

bu fonksyon ikinci parametresi ile belirtilen adresten başlayaral birinci parametresinde belirtilen adrese doğru 3. parametresi işle belirtilen sayıda karakteri kopyalar.geri dönüş değeri 1. parametresi ile belirtilen adresin aynısıdır. bu fonksyon normal olarak null karakteri kopyalamazbir ayzının belli bir kısmını başka bir yazı ile değiştirmek amacı ile kullanılır. eğer n sayısı kopyalaacak yazının uzunluğundan daha büyük ise null karakterde kopyalanır ve işlem sonlandırılır.

```c
#include <stdio.h>
#include <string.h>
void main (void)
{
char d[50]="Eskişehir";
char s[50]="yenisahra";
clrscr();
strncpy(d,s,4);
printf("%s\n",d);
}
```

STRNCAT FONKSYONU

bu fonksyon bir yazının ilk n karakterini başka bir dizinin sonuna eklemeye yarar. null karakter her zaman yazının sonuna kopyalanır.

```c
#include <stdio.h>
#include <string.h>
void main (void)
{
char d[50]="Eskişehir";
char s[50]="yenisahra";
clrscr();
strncat(d,s,4);
printf("%s\n",d);
}
```

STRNCMP FONKSYONU:

int strncmp(char *s1,char *s2, int n);

iki yazının ilk n karakterini karşılaştırır. fonksyon n sayısı yaızlardan birinin uzunluğundan daha büyükse null karakteri görünce işlemini bitirir.

```c
#include <stdio.h>
#include <string.h>
void main (void)
{
char d[100] = "eskişehir";
char s[100] = "eskihisar";
if (!strncmp(d, s, 4))
printf("evet\n");
else
printf("hayır\n");
}
```

ALFABETİK SAYISAL DÖNÜŞÜM YAPAN FONKSYONLAR:

stdlip.h içerisinde çok kullanılan karma fonksyonların prototipleri bulunur.

ATOI (alfabetic to integer) FONKSYONU:

int atoi( char *str);

bu fonksyon ascii karakterleri ile oluşturulmuş yani bir yazı biçiminde bulunan sayısal bilginin başlangıç adresini bir parametre olarak alır. Onu int türüne dönüştürerek geri dönüş değeri olarak verir.

```c
#include <stdio.h>
#include <stdlib.h>
void main (void)
{
char s[] = "1234";
int n;
n = atoi(s);
printf("%d\n",n);
}
```

ilk sayısal olmayan yada null karakteri gördüğünde işlemi sonlandırır.

SAYISAL ALFABETİK DÖNÜŞÜM YAPAN FONKSYONLAR

ITOA FONKSYONU:

char *itoa(int n, char *str, int base);

1. parametre yerleştirlecek sayıyı belirtir

2. parametre yerleştirilmenin yapılcağı adrestir

3. parametre kaçlık sistemde yerleştirileceği

bu 2. parametredeki değerine geri döner

LTOA FONKSYONU:

itoa fonksiyonunun long türü için olanıdır.

ATOF FONKSİYONU:alfabetic to float

```c
#include <stdio.h>
#include <stdlib.h>
void main (void)
{
char s[]="127.560";
printf("%lf\n",atof(s));
}
```

SPRINTF FONKSİYONU:

Bu fonksiyon her turlu bilgiyi karakter biçimine dönüştüren genel amaçlı bir fonksiyondur.Kullanımı printf fonksiyonunun aynısıdır.Ancak ilk parametresi karakter türünden bir göstericidir.

sprintf(char *str,.......);

Bu fonksiyon sonuçları ekran yerine birinci parametresiyle belirtilmiş olan adrese yazar ve sonun null karakteri ekler.

```c
#include <stdio.h>
#include <stdlib.h>
void main(void)
{
char s[500];
int a=123;
long b=5000000;
sprintf(s, "a=%d b=%ld", a, b)
puts(s);
}
```

```c
sprintf(s,"%lf",x);
```

GÖSTERİCİLERE İLK DEĞER VERİLMESİ:

char *p=(char *)0X1FC0;

Bir göstericiye tanımlar tanımlamaz ilk değer verilebilir.

**GÖSTERİCİ HATALARI**

Derleyicinin hafızada bizim kullanımımız için ayırdığı bölgelere güvenli bölge denir.Bir gösterici kullanılarak bellekte istenilen bir bölgeye erişilebilir.Ancak herhangi bir bölgeye gösterici yoluyla veri aktarmak orada çalışan programların bütünlüğünü bozacağı için beklenmeyen sonuçların çıkmasına neden olabilir.Bellekte kimin tarafından kullanıldığı belli olmayan bölgelere veri aktarılması gösterici hatasıdır.İçeriği programcı tarafından bilinmeyen bölgelere güvenli olmayan bölge denir.Gösterici hatası derleme sırasında değil run time sırasında etkisini gösterir.Böyle hataları derleyici anlayamaz.Göstericilerle ancak tanımlama yoluyla tahsis edilmiş olan alanlara veri aktarılabilir.

GÖSTERİCİ HATALARININ ORTAYA ÇIKIŞ BİÇİMLERİ

1-ilk değer verilmemiş göstericilerin yol açtığı hatalar

Bir pointer rast gele bir adresi ifade ederken onun içine değer verilmesi hatadır.

```c
void main(void)
{
char *p;
*p='a';
}
```

```c
void main(void)
{
char *p;
gets(p);
}
```

```c
void main(void)
{
char *p;
char s[]="ali";
strcpy(p,s);
}
```

```c
p=strchr(s,'a');
*p='b'; eger a karakteri bulunmazsa strchr NULL adrei ile geri döner.Bu durumda b karakteri NULL adresine konulmaya çalışılır ki,tanımsız bir adrestir.
```

2-Dizi taşmalarında kaynaklanan gösterici hataları

```c
{
int a[10];
int i;
for (i=0;i<=10;++i) /* a<10 olmalı yoksa dizi taşması...*/
a[i]=0;
}
```

```c
{
char s[10];
gets(s); /*burada ancak 9 karakter girilebilir.yoksa null karakter */
/*11. karakter olarak konulabilir... */
```

```c
{
char d[]="ali"; /*tanımlamada d'ye daha büyük bir aralık verilmeli */
char s[]="veli"; /*d[50] gibi */
strcpy(d,s);
}
```

```c
{
char d[10]="adana";
char s[10]="istanbul";
strcat(d,s); /*strcat d'nin sonuna s'yi eklediği için taşma olur*/
}
```

```c
{
char d[10];
char s[10]="ali";
char t[]="veli";
strcat(d,s); /*d'nin içinde rastgele değerler olduğu için ilk önce */
strcat(d,t); /*strcpy(d,s) yapılması daha doğru olur */
}
```

Çok işlemli işletim sistemlerinde bir programcının yaptığı gösterici hatalarından başka bir programcı etkilenebilir.Ancak böyle birşeyin güvenlik açısından engellenmesi gerekir.Böyle sistemlerde kullanılan mikro işlemcilerin koruma mekanizmaları vardır.Böyle sistemlerde bir program kendi alanı dışına eriştiğinde bu durum işlemci tarafından tespit edilir,işlemci bu durumu işletim sistemine bildirir,işletim sistemi de programı sonlandırır.

RASTGELE SAYI TÜRETME

RASTGELE(random):

Sayıların rastgeleliği istatistik hesaplamalarla bulunabilir.Her sayının gelme olasılığının eşit olduğu sisteme düzgün dağılmış rastgele sistem denir. Borland ve microsoft derleyicilerinde rastgele sayı üretilmesini sağlayan fonksiyonlar bölümden elde edilen kalan sistemini kullanırlar.Bu sisteme göre bir sayının bir sayıya bölümünden kalan rastgeledir.Ritchie'nin "The C Programming Language" kitabında bu tür fonksiyonların tasarımı açıklanmıştır. C'nin srand ve rand isimli rastgele sayı üretilmesini sağlayan iki türlü fonksiyonu vardır.İkisi de stdlib.h'ta bulunur.

rand fonksiyonu 0-32765 arası bir tam sayı verir[prototipi=>int rans(void);]

```c
#include <stdio.h>
#include <stdlib.h>
void main(void)
{
int i;
for (i=0;i<10;++i)
printf("%d\n",rand());
}
```

Bu fonksiyon her defasında aynı sayıları üretir.Bu fonksiyon ile herhangi bir aralıkta rastgele sayı üretilebilir.=> rand()%n+k [:=>k ile n arası]

0-1 arasında noktalı rastgele sayı üretimi için stdlib.h içerisinde RAND_MAX isimli bir sembolik sabit de vardır.

rand fonksiyonunun algoritması :

```c
unsigned long int next=1;
int rand(void)
{
next=next * 1103515245 + 12345;
return (next / 65536) % 32767;
}
```

Burada next global değişkeni sabit olduğuna göre program her çalıştığında bir dizi aynı rastgele sayılar elde edilir.

srand standart olarak next global değişkenine bir değer yüklemek için kullanılır.

```c
void srand(unsigned int seed)
{
next=seed;
}
```

Programın her çalışmasında farklı bir dizilimin elde edilmesi isteniyorsa srand fonksiyonunun parametresinin de rastgele bir değer alınması gerekir. Prototipi time.h içerisinde tanımlanmış olan time fonksiyonu kullanılır.time fonksiyonu 1-1-1970 'ten kullanıldığı ana kadar geçmiş saniye sayısını bulur.Parametre için 0 girilmelidir.Yani programın başında srand(time(0)); çağırması yapılırsa her seferinde farklı sayılar bulunur.Borland derleyicilerinde stdlib.h dosyası içerisinde aynı çağrmayı yapan bir #define vardır..

```c
/* #define randomize() srand(time(0)) */
```

void Göstericiler

Bir göstericinin türü void olabilir. Böyle göstericilerin içieriisnde bulunan adresi türü belli değildir. Void gösterici arttırılamaz ve azaltılamaz. Void göstericiler * veya [] operatörleriyle de kullanılamaz. Böyle göstericiler adres bilgilerinin geçici olarak tutulmasında kullanılırlar.

Bir Göstericiye Farklı Türden Bir Adresin Atanması

```c
void main(void)
{
int *p;
char s[10];
p = s; /*warning:suspicious pointer conversion*/
}
```

C'de bir göstericiye farklı türden bir adres bilgisi atanırsa bir uyarı söz konusu olur. Çünkü derleyici bu işlemin yanlışlıkla yapıldığını düşünür. Bu uyarıya karşın adresin sayısal bileşeni göstericiye atanmaktadır.

```c
void main(void)
{
int *p;
char s[10];
p = (int *)s; /*Bilinçli tür dönüştürme yapıldığında warning olmaz*/
}
```

Bir Göstericiye Adres Olmayan Bilginin Atanması

```c
void main(void)
{
int *p;
p = 0x1FC0; /*warning non-portable pointer assignment...*/
}
```

Bir göstericiye adres olmayan bir bilgi atanırsa derleyici bunu da programcının yanlış yaptığı bi4r işlem olarak alır ve uyarı verir. Bu durumda da uyarıyı kesmek için bilinçli tür dönüşümü yapmak gerekir. Bu yapılırsa zaten ifade adres sabitine dönüşür.

```c
void main(void)
{
int *p;
p = (int *)0x1FC0;
}
```

Bu atama işlemleri fonksiyon çağırılması sırasında gizli bir biçimde de yapılır.

```c
void fonk(int *p)
{
*p = 10;
}
void main(void)
{
char s[] = "Ankara";
fonk(s);
}
```

Standart C fonksiyonlarının kendileri kütüphane dosyalarında, prototipleri başlık dosyalarında olduğuna göre parametresi gösterici olan standart C fonksiyonlarındaki uyuşmazlıklar da tespit edilir.

```c
void main(void)
{
int p[] = {1, 2, 3};
puts(p); /*warning:suspicious pointer assignment..*/
}
```

Normal Bir Türe Adres Bilgisinin Atanması Durumu

```c
void main(void)
{
int a;
char s[] = "Ankara";
a = s; /*warning Non-portable pointer assignment in function ... */
}
```

Bir adres bilgisi C'nin normal bir türüne atanmaya çalışılırs, derleyici bunu da şüpheyle karşılar ve uyarı verir. Bu uyarıdan kurtulmak için normal türe bilinçli dönüştürme yapılabilir.

```c
void main(void)
{
int a;
char s[] = "ankara";
a = (int ) s;
}
```

Genel Sonuçlar

1. Bir göstericiye aynı türden bir adres bilgisi atanmalıdır ve bir adres bilgisi de ancak aynı türden bir göstericiye atanabilir. Bu kurala uyulmazsa C derleyicileri uyarı verir.

2. Uyumsuzluk nedeniyle ortaya çıkan uyarılar bilinçli tür dönüşümüyle giderilebilir.

Void Göstericilerle İlgili Atama İşlemleri

void göstericiye hangi türden adres atarsak atayalım bir uyarı söz konusu olmaz. Ancak void bir adres herhangi bir türden göstericiye atanırsa bu durum eski dereiyicilerde bir probleme yol açmasa da yeni derleyicilerde uyarı olarak ele alınır.

void * = int * ; /*warning yok*/

int * = void * ; /*warning var*/

void adresin bir göstericiye atanması gerektiği durumlarda bilinçli tür dönüştürmesi uygulanırsa hiçbir derleyicide problem ortaya çıkmaz.

```c
{
char *p;
int *t;
p = (char *) t; /*warning yok*/
}
```

void Göstericilerin Kullanım Amacı

void göstericiler türden bağımsız işlemlerin yapılması için genellikle fonksiyon parametresi kullanırlar.

memcpy isimli fonksiyon bir adresten bir adrese koşulsuz n byte kopyalar. Bu fonksiyon herhangi bir türden dizinin içeriğinin kopyalanması amacıyla kullanılır. Bu işlem strncpy fonksiyonu ile yapılamaz bu fonksiyon 0 sayısını gördüğü anda bunu NULL karakter zanneder ve işlemi sonlandırır. Bu fonksiyonun ilk parametresi kopyalamanın yapılacağı adres, ikinci parametresi kopyalanacak adres, üçüncü parametresi ise kopyalanacak byte sayısıdır. Bu fonksiyonun prototipi string.h içerisindedir.

memcpy(dest, source, n);

memcpy fonksiyonu madem her türden adres bilgisiyle çağırılmaktadır o halde bu fonksiyonun ilk iki parametresi void türden gösterici olmalıdır.

memcpy(void *dest, void *source, int n);

void Gösterici Parametresine Sahip Olan Fonksiyonların Yazımı

void göstericiler * ve [] ile kullanılamadığına ve arttırılıp azaltılamadığına göre hemen blok girişinde tür dönüşümü yapılarak türü belirli bir göstericiye atanmalıdır.

```c
void mymemcpy(void *dest, void *source, int n)
{
char *d = (char *) dest;
char *s = (char *) source;
int i;
for (i = 0; i < n; ++i)
d[i] = s[i];
}
```

memset Fonskiyonu

void memset(void *p, char ch,int n);

Bu fonksiyon bir adresten başlayarak n tane byte'ı belirle bir değerle doldurmak için kullanılır. Bu fonksiyon örneğin bir diziyi 0'lamak için kullanılabilir.

```c
#nclude <stdio.h>
#include <string.h>
void main(void)
{
char s[50];
memset(s, 'x', 20);
s[20] = '\0';
puts(s);
}
```

```c
void main(void)
{
char a[] = "Ali";
char b[50];
memcpy(b, a, strlen(a) + 1);
puts(b);
}
```

Bir fonksiyon void bir adresle geri dönebilir. Böyle bir fonksiyonun geri dönüş değeri tür dönüştürmesi yapılarak herhangi bir türden göstericiye atanmalıdır.

Stringler

C'de çift tırnak içerisine yazılan ifadelere çift tırnak ile beraber string denir. Derleyici bir stringle karşılaştığında önce string içerisindeki karakterler belleğin güvenli bir bölgesine yerleştirir. Sonuna NULL karakteri ekler. String yerine yerleştirildiği yerin adresini koyar. Yani stringler karakter türünden adres sabiti gibi işlem görürler.

```c
void main(void)
{
char *p;
p = "Ankara";
puts(p);
}
```

| p=> | 1A00 |
| --- | --- |

| A | 1A00 |
| --- | --- |
| n | 1A01 |
| k | 1A02 |
| a | 1A03 |
| r | 1A04 |
| a | 1A05 |
| '\0' | 1A06 |

Stringler karakter türünden bir göstericiye atanabilirler. Bir diziye ilk değer verirken kullanılan çift tırnak içerisindeki deyim string değildir. Yani derleyici oradaki çift tırnak yerine bir adres yerleştirmez.

char s[100] = "Ali"; /*string değil*/

Bu işlem çift tırnak içerisindeki karakterlerin dizi içerisine tek tek yerleştirilmesi anlamındadır.

```c
{
char s[100];
s = "Ali"; /*error: Lvalue required in function...*/
}
```

Bir karakter dizisinin içerisine bir yazı 3 şekilde yerleştirilebilir.

1. İlk değer verilerek:

char s[] = "Ali";

2. Tek tek değer verme:

```c
char s[10];
s[0] = 'A';
s[1] = 'l';
s[2] = 'i';
s[3] = '\0';
```

3. strcpy fonksiyonu kullanılarak:

```c
char s[10];
strcpy(s, "Ali");
```

(12-9-1998)

PAGE 1

PAGE 71

---
*Kaynak: `YAZILIM VE PROGRAM DİLLERİNİN SINIFLANDIRMASI/YAZILIM VE PROGRAM DİLLERİNİN SINIFLANDIRMASI.doc` — serkan — 2004*
