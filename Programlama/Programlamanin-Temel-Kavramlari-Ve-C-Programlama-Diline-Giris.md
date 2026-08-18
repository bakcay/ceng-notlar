# Programlamanin Temel Kavramlari Ve C Programlama Diline Giriş

## **part 3**

## PROGRAMLAMANIN TEMEL KAVRAMLARI VE "C" PROGRAMLAMA DİLİNE GİRİŞ

BAZI TERİMLER;

Atom;Anlam taşıyan en küçük birim

## **Bölümleri**

## **1.Anahtar Sözcükler;******

Değişken olarak kullanımı yasaklanmış olan sözcüklerdir.

--- int,include,for...vs---

**Not**;C de tüm anahtar sözcükler küçük harften oluşur.

## **2. Değişkenler;******

Önceden belirlenmiş kurallara göre bellekte yer ayıran atomlardır.

---a,d,ch,...vs..---

## **3.Operatörler;******

Önceden tanımlanmış işlemleri yapan özel atomlar.

--- + toplama,- çıkarma , ++ arttırma, vs..---

## **4.Sabitler**

Doğrudan işleme sokulurlar ve bilgi içermezler..

---- c=a+10 bu ifadede c ile a değişken 10 ise sabitir.---

## **5.Stringler(String literal)******

İki tırnak içerisine alınmış ifadelerdir..genelde atom olarak yorumlanırlar.bölünemezler.

--- "lütfen birsayı giriniz","/n" vs..---

## **6.Ayraçlar******

Deyimleri birbirinden ayırırlar

--- {,;,}---

## 3.3 NESNE KAVRAMI

**Tanım**;Bellekte yer kaplayan ve içlerine erişilebilen alanlardır.

a=b+c de bu değişkenlerin her biri aynı zaman da birer nesnedir.

## **NESNE ÖZELLİKLERİ;******

## **İsmi(name);******

Nesneyi temsil eden karakterdir.Belirli kuralları vardır.Her değişken bir nesnedir.

## **Değer(value);******

Nesnelerin içlerinde tutukları değerlerdir. Değiştirilebilirler veya birdefaya mahsus değiştirilebilireler.

**Tür(type);******

Nesnenin işleme sokulduğunda derleyici tarafından nasıl işleme sokulacağını belirten belirteçtir.

---char karakter,integer tamsayı,float or real gerçek sayı---

ayrıca birnesnenin türü onun bellekte nekadar yerkapladığınıda bilmemizi sağlar

Faaliyet eaalanı ve ömrü(scopeand duration);

----------------------------------

Not buradaki "nesne" kavramını nesne yönelimli prohgramlama diliyle hiç bir ilgisi yoktur.

İFADE;

değişken ve operatörlerin kombinasyonundan oluşur.

## SOL TARAF DEĞERİ-Left value-

Atama operatörünün solundaki ifadelerdir.

a=b+c de .. a sol taraf değeri b ise sağtaraf değerini oluşturur.

## MERHABA "C"

## #include <stdio.h>

## main()

## {

## printf("Merhaba C\\n")

## }

işte size basit bir c programı işlevi ekrana

## **Merhaba C ******

yazısını basmak şimdi bu programı irdeliyelim;

#include <stdio.h> ----->Bu satır hazır kütüphane satırı derlemeye dahil.

main() -----> main fonksiyonu çağrılmış "()" ise fonksiyon operatörü

{ ----->Blok başlangıcı

printf("Merhaba C\\n"); ----->printf fonkisonu ve içinde string ifadesi ve ekrana basılacak kısım

} ------>Blok bitişi

Burada main tanımlanmış printf ise bloğun içinde çağrılmıştır.bunu **;** den anlarız.

## FONKSİYONLARIN ÇAĞRILMASI VE TANIMLANMASI

Tanımlanmış fonksiyonlar bizim tarafımızdan yazılmışlardır.Çağrılmaları ise onların icraya davet edilmesi anlamına gelir.Bir fonksiyonun çağrılması için tanımlanması gerekir.

---Fonksiyonlar herzaman tanımlanmış fonksiyonların içerisinde çağrılabilirler---

Yukarıdaki programda main fonksiyonunu tanımladık .. Bu fonksiyonnun faaliyet alanı iki blok arasındadır."main" fonksiyonu işlevi gereğince printf fonksiyonu çağrılmış ve printf fonksiyonunun gereğincede paramatre değeri içersindeki string değerindede ekrana basılmıştır.

## **part 4 **

## **part 5 **

## **part 6 **

## **part 7 **

## **part 8 **

## **part 9 **

## OPERATÖRLER

Kavramlar;

Bu bölümde öğrenilmesi gereken kavramlardan bazıları şunlardır;

1.Operatörler ve operandlar

2.Önek-prefix- Araek-infix- Sonek -posfix-

3. Öncelik sırası

Not: C de "kavramlar" arası ilişkiler operatörlerle sağlanır.Bu özellikte C yi anlama babında operatörlerin önemini arttırmaktadır.Türkçesi C yi iyice bellemek için operatörler konusunu iyice kavramalısınız.

Tanım 9.1 Operatör

Nesneler ve Sabitler üzerinde önceden tanımlanmış tanımlı işleri CPU katkısıyla faaliyete neden olan - assembly dilinde birden fazla komuta karşılık gelen - C deki atomlardır.

Not: C de her ifadede en az bir operatör bulunur.

Tanım 9.2 Operand

Operatörlerin işleme soktuğu nesneler yada sabitlerdir.

c=a+b bu ifadede c,a ve b operand, = ve + ise operatördür.

++a ifadesinde ise ++ bir operatör, a ise operandır

-----Operandlar operatörlerin faaliyet alanlarıdır----

## OPERATÖRLER ARASI ÖNCELİK İLİŞKİSİ

-- 4 İşlem önceliği buraradada geçerlidir.

-- !! Aynı önceliğe sahip 2 operatörlü bir ifadede, eşit önceliğe sahip operatörlerden önce soldaki operatörün işlemi yapılır sonrada sağdakinin ve sonrada diğerlerin.

!!!!Aynı önceliğe sahip iki operatör arasındaki öncelik soldan sağa doğrudur.!!!

a=b-x/2\*c ----> bu ifadede;

## I1: x/2

## I2: I1\*c

## I3:b-I2

## I4: a=I3

C de "=" operatörü soldan sağa önceliklidir.

Parantez içindeki "()" işlemler en çok önceliklidir.

Bir operatör birden fazla operandla çalışabilir. Buna çoklu operand desteği denir.

## OPERANDLARIN SINIFLANDIRILMASI

İşlevlerine;

Operand sayılarına

Operatörlerin konumlarına göre

OPERATÖRLERİN İŞLEVLERİNE GÖRE SINIFLANDIRILMASI;

Aritmetik op. -arithmetic op-

Mantıksal op. -Logical-

Gösterici op. -Pointer-

İlşkisel op. -Relational-

Bit op. -Bitwise-

Özel amaçlı op. -Special purpose-

İlk 3 operatör türü dillerin hepsinde vardır fakat bit op ile gösterici op. ler çoğu dilde bulunmaz.Fakat dillerin çoğunda özel amaçlı operatörler mevcuttur.

Aritmetik operatörler -arithmetic-

4 işlemle ilgili ..

\* Çarpma,

/ Bölme,

% Mod alma -kalan bulma-,

+ Toplama,

- Çıkarma,

İlişkisel operatörler -Relational-

İki değer arasındaki ilişkiyi sorgularlar.

> Büyüktür,

< Küçüktür,

>= Büyük yada eşittir,

<= Küçük yada eşitir,

== Eşittir,

!= Eşit değil,

Mantıksal -Logical-

Mantıksal işlemleri yaparlar.

! Değil

&& ve -and-

|| veya -or-

Bit -Bitwise-

~ Değil -Bitwise not-

<< Sola kaydırma -left shift-

>> Sağa kaydırma -right shift-

& Ve Bitwise and

^ özel veya -Bitwise exor-

| Özel ve -Bitwise or-

Gösterici oeperatörler -Pointer-

Adres işleminde kullanılan operatörlerdir.

\* İçerik alma -indirection-

& adres alma -adress of-

\[\] İndex -index -

-> Yapı gösterici -arrow-

Özel amaçlı operatörlerdir. -special purpose-

özel amaçlı operatörler..

() Fonksiyon çağırma ve öncelik değiştirme

. Yapı elamanına erişme

(tür) Tür dönüştürme

sizeof Uzunluk

?: Koşul

= Atama

+=,\*=, /0,......., İşlemli atama

OPERATÖRLAERİN OPERAND SAYILARINA GÖRE SINIFLANDIRILMASI

1 Operandlı operatörler (Unary op.)

2 Operandlı operatörler ( Binary op.)

3 Operandlı operatörler (Ternary op.)

Bir operatör aynı anda 3 operandı işleme sokabilir.Genelde operatöerler 2 operandla çalışır 3 nadirdir tek operandlı olanlarıda vardır.Koşul operatörü 3 operandlıdır.

OPERANDLARIN KONUMLARINA GÖRE SINIRLANDIRILMASI

Önek -prefix- operatörü,, tek operandlı operatörlerde operatörün konumu.

Araek -infix- operatörü,, iki " " " " .

Sonek -posfix- operatörü,, tek " " " "

ARİTMETİK OPERATÖRLER;

Klasik 4 işlem operatörleridir.Dört işlem önceliği buradada aynen geçerlidir.Bu operratörlerin operandları mutlaka char, int,short veya long türünden olmalıdırlar.Hepsi araek -prefix- konumunda işleme alınırlar.

Öncelik sırası gözetilerek aritmetik operatörler,

\* , / ve % eşit öncelikli

+ ve - de eşit önceliklidir.

BU iki grup arasında ise yukardaki daha önceliklidir.

\* Çarpma,

/ Bölme,

% Mod alma -kalan bulma-,

+ Toplama,

- Çıkarma,

ARTTIRMA VE EKSİLTME OPERATÖRLERİ

Çok kullanılırlar,önek -prefix- veya sonek -posfix- durumunda kullanılıarlar.

Öncelik; Tüm aritmetik operatörlerden yükssek önceliğe sahiptirler.

++ Arttırma op.

-- Eksiltme op.

Kullanım;

1.Yalın olarak diğer operatörlerle ilişkisiz;

++x ve x++ aynı anlama yani ++x=x++=x+1,, x'İ 1 arttır .

--x ve x-- aynı anlama yani --x=x--=x-1,, x'İ 1 eksilt anlamındadır

2. Diğer operatörlerle beraber kullanıldığında, örneğin atama operatörüyle önek veya sonek olarark kullanıldığında farklı anlamalara gelir.

--> Önek durumunda kullanılıyorsa;diğer aritmetik ooperatöerlerden yüksek önceliklidir.

x=10;

y=++x; /\* x'i 1 arttır ve oluşan değeri y'ye ata sonuç: y=11 , x=11 \*/

-->atama operatörüyle son ek durumunda kullanılıyorsa

x=10; /\*x değerini y'ye ata ve işlem sonunda x'i 1 arttır. y=10 , x=11 Burada ;arttırım ifadenin ilk işlemi y=x++ olacak şekilde değil ifadenin enson işlemi olacak şekilde en sonda yapılır.\*/

NOT; Arttırma ve eksiltme operatörlerinin operandları sabit olamazlar çunku sabitlerin içlerine erişilemezler,dolayısıyla mutlaka operandlar nesne olmalıdır.

NOT;Şüpheli kodlar:

a=10; /\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

b=20 1.a++ +b ; a ile b yi toplayıp c ye atarız sonundada a yı 1 arttırırız ve ya a+ ++b şeklinde

c=a+++b; düşünüp b yi bir arttırıp aile toplayıp c ye atarız .Acaba derleyici ne yapar??

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

bu tip şüpheli kodlardan kaçınmalıyız.

2. İLİŞKİSEL OPERATÖRLER;

İki değer arasında karşılaştırma yaparlar;koşul sağlanırsa "1" sağlanmıyorsa "0" değerini üretirler.

öncelik sırasına göre ;

> Büyüktür, < Küçüktür, >= Büyük yada eşittir, <= Küçük yada eşitir, kendi aralarında eşit önceliğe sahiptirler.

== Eşittir, != Eşit değil, kendi aralarında eşit önceliğe sahiptirler.

Not: C de mantıksal dveri türü yerine int türü küllanılır.Buda C ye esneklik katar bunun nasıl bişi olduğu ilerki bölümlerde anlatılacak. Sabırsızlanmamayın please..

Not: Arada mantıksal operatör olmaksızın ardarda ilişkisel operatörler kullanılamazlar.

Kullanım;

a=5>2; /\* a=1 koşul sağlandı.\*/

c= 5 <= 1 ; /\* işlem soldan sağa yürür .1. koşul sağlanmadığı için sonuç 0 ve c=0 dır \*/

3. MANTIKSAL OPERATÖRLER;

Öncelik sırasına göre:

! Değil -not-

&& ve -and- || veya -or- eşit öncelikli..aralarında

Not: ! not, tek operandlı ve herzaman önek durumundadır.

C de Mantıksal "doğru" ve "yalnış" değerleri

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ilşkisel operatörler tarafından üretilen değerler 1 yada 0 dır Fakat bir sayı mantıksal olarak yorumlanacağı zaman;

sayı--operand değeri- 0 ise -0- yalnış;

sayı--operand değeri- 0 dan farklı bir değerse sonuç "doğru" -1- dur denir.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

örnekler;

-11 doğru,

0 yanlış ;

10 doğru,

---->İlişkisel operatörler tarafından üretilen 1 ve 0 değerleri mantıksal operatörler tarafındsan doğru veya yalnış olarak yorumlanırlar.Mantıksal operatörlerde de ilişkiselde olduğu gibi üretilen değerlr int türünden 1 yada 0 değerleridir.

Not: önemli... C de mantıksal veri değerleri yoktur bunun yerine int türünden değerler kullanılır buda C nin esnekliğini arttırır.

! Değil (not) işlemi ;

Tek operandlıdır,

Her zaman önek durumundadır.

Doğru değeri yalnışa , yalnış değeri doğruya çevirir."a" nın değeri doğruysa onun değili yalnıştır.

"a" nın değeri yalnışsa onun değili doğrudur.

Burdaki doğru ve yalnış değerleri mantıksal olarak ele alınmalıdır.

Mantık

a=!4; /\* 4 doğru bir değerdir.. o dışı bunun değili ise yalnış olarak yorumlanır.\*/

a=10

b=!++a > 10 !=5;

b=0 > 10 !=5

b= 0 !=5

b=1

& Ve and operatörü ve işlevi;

---
*Kaynak: `PROGRAMLAMANIN TEMEL KAVRAMLARI VE C PROGRAMLAMA DİLİNE GİRİŞ/PROGRAMLAMANIN TEMEL KAVRAMLARI VE -  C -  PROGRAMLAMA DİLİNE GİRİŞ.doc` — skeser — 2004*
