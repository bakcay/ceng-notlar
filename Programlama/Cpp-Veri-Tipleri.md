# Cpp Veri Tipleri

**Temel Veri Tipleri : **bool true ve false değerlerini alır. true = 1, false = 0 gibi düşünelebilir. Derleyicisine göre Bool şeklindede tanimlanıyor olabilir.

| char | ASCII karakterleri ve çok küçük sayılar için kullanılır. |
| --- | --- |
| enum | Sıralanmış değerleri tutar. |
| int | Sayma sayıları. |
| long | Sayma sayıları. |
| float | Ondalıklı sayılar. |
| double | Ondalıklı sayılar. |
| long | double Ondalıklı sayılar. |
| void | Değersiz - boş. |

## C++ VERİ TİPLERİ

**Temel Veri Tiplerinin Uzunlukları ******

Not : Bu değerler 32 bit uygulama geliştirme ortamındaki platformlara özeldir. Platformdan platforma değişebilir.

| bool | 0--1 |
| --- | --- |
| char | -128 -- 127 |
| enum | int ile aynı değerde |
| int | –2,147,483,648 -- 2,147,483,647 |
| long | –2,147,483,648 -- 2,147,483,647 |
| float | 3.4E +/- 38 |
| double | 1.7E +/- 308 |
| long double | 1.2E +/- 4932 |

**unsigned : **
unsigned belli veri tiplerinin işaretsiz değerler almasını sağlar.
Örneğin; unsigned char 0 - 255 arasında değer alır. Dikkat edilecek olunursa negatif kısım atılmış ve burada ki değer uzunluğu pozitif kısıma eklenmiş.
unsigned char;int ve long türlerine uygulanabilir.

**typdef - Türleri kendinize göre adlandırın : **
typdef kullanarak tanımlanmış türleri kendinize göre adlandırabilirsiniz..Dikkat ediniz ki bu şekilde yeni bir tür yaratmıyorsunuz. Ayrıca bu isimlendirmenizi diğer tiplerle birlikte kullanamazsınız.

Örneğin:
typdef double FINANSAL
artık double yerine FINANSAL kullanabilirsiniz.
long FINANSAL şeklinde bir kullanım hatalıdır.

## **Değişkenler ******

**Değişken Nedir? **
Değişken belli bit türe ait verileri saklayan veri deposudur. Aksi belirtilmedikçe içerikleri değiştirilebilir.

**Değişken Nasıl Tanımlanır? **
Değişkenleri tanımlamak için aşağıdaki notasyon kullanılır.

Veri Tipi\] \[Değişken Adı\];

Örneğin içinde sayı tutacak bir değişken şu şekilde tanımlanabilir

int sayi;

Benzer olarak aşağıdaki tanımlamalarda doğudur

char c;
int i;
float f;
double d;
unsigned int ui;

**Değişken isimlerini tanımlarken dikkate alınacak noktalar : **
C++ dilinde de C dilinde ki gibi büyük ve küçük harfler farklı verileri temsil eder

Örneğin;
char c;
char C;
int sayi;
int Sayi;
c ve C hafızada farklı yerleri gösterirler. sayi ve Sayi'da farklıdır.

Değişkenler harflerle yada \_ başlar.

İçlerinde boşluk yoktur.

Değişkenler istenildekleri yerde tanımlanabilirler. Ancak burada dikkate alınması gereken noktalar vardır. Lütfen bölüm sonundaki örneklere göz atınız.

**Değişkenlere değer atanması ** Bir değişkene değer atamak için = operatörü kullanılır. Değişkene değer atama tanımlandığı zaman yapılabildiği gibi daha sonradanda yapılabilir.

Örneğin;
Tanımlama sırasında değer atama:
char c = 'c';
int sayi = 100;
Daha sonradan değer atama:
char c;
int sayi;
c = 'c ';
sayi = 100;

Aynı anda birden fazla değişken tanımlanabilir, ve aynı anda birden fazla değişkene değer atanabilir;

int i , j , k;
i = j = k = 100;
i,j,k'nın değeri 100 oldu.

## **Programlara Açıklama Eklenmesi ******

**Açıklama Nedir? **
Değişkenleri tanımlarken dikkat ettiyseniz her C++ komutu ; (noktalı virgül) ile bitiyor. Bu derleyiciye komut yazımının bittiğini belitmek için kullanılıyor.
Programlar uzadıkça ve karmaşıklaştıkça programımıza bir daha ki bakışımızda neyi neden yaptığımızı unutabiliriz. Yada yazılmış olan programı bizden başka kişilerde kullanacak olabilir. Bundan dolayı ne yaptığımıza dair açıklamaları kodun içine serpiştirmeliyiz.
Yazdığınız komutlar basit fonksiyonları içersede detaylı şekilde açıklama eklemenizi öneririm. Böylecene aylar sonra kodunuza tekrar baktığınızda ne yaptığınızı kolayca hatırlayabilirsiniz. Başkası sizin kodunuza baktığında öğrenmesi çok hızlanacaktır.

**Açıklamaları C++'ta nasıl tanımlayacaksınız ? **
C++ program içerisine iki şekilde açıklama eklemenize izin veriyor.Biri C'nin açıklama ekleme şekli olan // kullanılması. C++ derleyicisi // 'den sonra satır boyunca yazılanların tümünü yok sayar.

Örneğin:
// Bu satır derleyici tarafından umursanmaz
// Ve ben satırın başına // yazarak bu satırın açıklama olduğunu belirtiyorum
// Aşağıda da örnek bir değişken tanımlanmıştır.
long ornek;

C++'ın C'den farklı olarak birden fazla satıra açıklama yazmayı sağlayan bir yapı daha vardır. Bu yapı /\* ile başlar \*/ ile biter. Yukarıdaki örneği bu yapı ile aşağıdaki gibi tanımlayabiliriz.

/\* Bu satır derleyici tarafından umursanmaz
Ve ben satırın başına // yazarak bu satırın açıklama olduğunu belirtiyorum
Aşağıda da örnek bir değişken tanımlanmıştır.\*/
long ornek;

---
*Kaynak: `C++ VERİ TİPLERİ/C++ VERI TIPLERI.doc` — anka — 2004*
