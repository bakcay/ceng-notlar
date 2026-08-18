# Basic Dili

İnsanların konuştuğu dillerin nasıl birer alfabesi varsa bilgisayar programlama dillerinin de alfabeleri vardır.bu alfabeler o dilde bir program yazabilmek için kullanılabilecek sembolleri ifade eder. BASIC öğrenilmesi çok kolay olan bir programlama dilidir.

İnsanların konuştuğu dillerin nasıl birer alfabesi varsa bilgisayar programlama dillerinin de alfabeleri vardır.bu alfabeler o dilde bir program yazabilmek için kullanılabilecek sembolleri ifade eder.

BASIC programının iki modda çalıştırılması mümkündür.
1.Dolaylı(indirect) Mod:Bu modda basıc dilinde yazılmış programın her satırına satır numarası denilen bir numara vermek zorunludur.satır numarası 0 ile 65529 arasında herhangi bir sayı olabilir.

```basic
10 PRINT 13+15
```
gibi.

2.Doğrudan(direct)Mod:Bu modda satır numarasına gerek yoktur.

**BASIC SABİTLERİ VE DEĞİŞKENLERİ****
****1.1 SABİTLER**
Programın çalışması esnasında değerleri değişmez.İki tip sabit vardır.
a) Karakter zinciri (strıng) sabiti:iki tane çift tırnak içine alınmış 255tane harf veya rakam olabilen karakter kümesidir.
''merhaba''
''12,000''
b)sayısal sabitler:5 gruba ayrılır;
b1) Tamsayı(ınteger)sabitler: -32768 ile +32767 aralığındaki tamsayıları ifade eder.
b2) Sabit noktalı sabitler : ondalık sayıların basıc'teki karşılığıdır.
b3) Kayan Noktalı Sabitler :Bir ondalık veya tamsayıyı üstel formda yazmak için kullanılır.

basıc kayan noktalı sabiti matemetiksel karşılığı
205.989E-2 2.05989
12E3 12000

c) Hekzadesimal(onaltılık)sabitler: &H ön eki kullanılır.

&H42 ondalık karşılığı 66'dır.

d) Oktal (sekizlik)sabitler : & veya &0 önekine sahip olan sabitlerdir.
&567 ondalık karşılığı 375'dir.

**1.2 DEĞİŞKENLER(VARIABLE)**
Değişken isimlerinde ilk 40 karakter anlamlıdır.Değişken isimlendirilirken harfler,rakamlar ve nokta sembolü kullanılır.ilk karakter alfabetik karakter (harf) olmalıdır.Değişken tipini belirlemek için özel tipte karakterler kullanılır. ($,!,%,ALFA$
MAKSİMUM!
GAMA
Bir değişken ismi ;
a)basıc deyimleri
b)basıc komutları
c)basıc fonksiyonlarının ismi
d)basıc oparatör isimleri ................... OLAMAZ.

Basıc değişkenleri iki gruba ayrılır:
a)sayısal değişkenler
b)karakter zinciri değişkenler . (değişkenin türünü belirlemek için iki yol vardır.)

1.özel tip bildiri karakterleri:
$ : değişkenin karakter zinciri değişkeni olduğunu bildirir.
! : değişkenin tek duyarlıklı olduğunu gösterir.(tek duyarlıklı değişkenler 7 ondalık hane kadar hassasiyetle depolanır.)
16 ondalık hane genişliğinde yer kaplar.)

2.basıc tip bilderi deyimleri:
DEFtip[harf1] , [harf2]....
tip 4 özel kelimeden biri olmalıdır.
INT :Tamsayı değişkeni
STR:karakter zincir değişkenleri için (strıng)
SNG:Tek duyarlıklı değişkenler için
DBL:çift duyarlıklı değişkenler için kullanılır.

örn. DEFINT A,X ( A ve X harfleri ile başlayan bütün değişkenler tamsayı değişken olarak tanımlanır.)

**2.2.BASIC'TE İNDİSLİ DEĞİŞKENLER**:Diziler( arrays)
DIM: Diziler kullanılacağı zaman DIM deyimi kullanılır.Bu deyim dizinin yapısını ve boyutunu bildirir.
DIM M(1,2) Bu deyim ile bilgisayarda 1 satır ve 2 sütun açılır.

**3.İFADELER VE ATAMA DEYİMLERİ**
basic sayısal operatörleri"ni 3 guruba ayırırız
1)aritmetiksel operatörler 2)ilişkisel operatörler 3)mantıksal operatörler

**3.1 ARİTMETİK OPERATÖRLER : **toplama,çıkarma,çarpma,üs alma gibi işlemleri gerçekleştirir.
^ : üs alma + :toplama
* :çarpma - :çıkarma

aritmatiksel operatörlerde işlem sırası ; varsa parentez içindeki ifade,üs alma,çarpma veya bölme,modüler aritmetik işlemi,toplama veya çıkarma.
İki operatörün birbirini izlemesi gerekiyorsa ,bunlar parentezle ayrılmalıdır. A/(-B) gibi.

matematiksel ifade basıc karşılığı
5 üssü 6 5^6 'dır.
x'in karesi + Y/(3.Z) X^2 +Y/(3*Z)

**3.1.1 Tamsayı Bölme:**
'' \'' sembolü tamsayı bölmeyi simgeler. 5 \ 2 =2'dir. eğer bölünen ve bölen ondalık sayılarsa önce yuvarlatma yapılır ve sonra işlem yapılır.
3.1.2 Modüler Aritmetik :
Mod operatörü yardımıyla gerçekleştirilir.8 Mod 3 ifadesi 8'in 3 ile bölümünden kalanı ifade eder.
8MOD 3=2'dir.

**3.2 İLİŞKİSEL OPERATÖRLER**: Bu operatörler iki değeri birbiri ile karşılaştırırlar.karşılaştırmanın değeri doğru ise -1 sayısal değeri görülür,yanlış ise 0 değeri görülür.
Operatör Kontrol ettiği eşitlik
= eşitlik
<> veya >< eşitsizlik
< den daha küçük
> den daha büyük
=< veya <= den daha küçük veya eşit
=> veya >= den daha büyük veya eşit

**3.3- OPERATÖRLERİN ÖNCELİK SIRASI**: Sayısal ,mantıksal ve ilişkisel opreratörler ve basıc fonksiyonlarının bulunduğu
bir ifadede öncellik sırası şu şekildedir:
1.Fonksiyon alma
2.Aritmetiksel işlemler
a.^ üs almak
b.*, /
c.\
d.MOD
e.+ , -
3.İlişkisel operatör işlemleri
4.Mantıksal işlemler,aşağıdaki önceliklerle:
a. NOT
b.AND
c.OR
d.XOR
e.EQV
f.IMP

örnek: sın(3,14159/2)^2*2-3<2 AND5/2*3>1
öncesın(3,14159/2)=1 olarak hesaplanır (basıc fonksiyonları için 10.bölüme bakın)

1^2*2-3<2 AND 5/2*3>1
sonra üs almak hesaplanır.
1*2-3<2 AND 5/2*3>1
sonra çarpma ve bölmeler yazılış sırasına göre yapılır:
2-3<2 AND 2,5x3>1
2-3<2 AND 7,5>1
sonra toplama ve çıkartma yapılır :
-1<2 AND 7,5>1
ilişkisel işlemler gerçekleştirilir:
-1<2 soncu Doğru (-1) ve 7,5>1 sonucu Doğrudur(-1).

Doğru AND Doğru sonucu olarak da Doğru (-1) sonucu hesaplanabilir

**4.0- ATAMA DEYİMİ (Assignment Statement)-LET DEYİMİ: **Basıc dilinde bir değişkene değer atama,aşağıda
yazılış biçimi verilen bir atama deyimi ile gerçekleşir
[LET] değişkeni ismi = ifade

10 Let A=A+1 veya let deyimi kullanılmadan 10 A=A+1 şeklinde atama yazılır.

**4.1 -PRINT DEYİMİ** : Ekrana bilgi yazdırmak için kullanılır.
**LPPRINT** : yazıcıdan çıkış alınmak isteğinde kullanılır.

Örnek;

```basic
10 X$="ESRAGÜL"
20 Y$="KOYUNCU"
30 LPPRINT X$;
40 LPPRINT Y$
```

Sonuç: **ESRAGÜL KOYUNCU****
**

**4.2 TAB Fonksiyonları :**Yazdırılacak değerlerin, n ile belirtilen pozisiyondan itibaren yazılmasını sağlayan 1 ile 255 arasında bir sayıdır.
TAB (n)
Örnek;

```basic
10 LPPRINT "ESRAGÜL"TAB(9) "KOYUNCU"
```
Sonuç: E S R A G Ü L K O Y U N C U
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

**4.3 SPC Fonksiyonu** : Yazdırılacak iki değer arasında n ile belirtilen miktarda boşluk bırakır.
**
****5.0 WRITE DEYİMİ**
Ekrana bilgi yazdırmak için kullanılır.
WRITE ve PRINT arasındakı farklar;
1)WRITE komutu elemanlar arasına yazılan virgülleri de ekrana aktarır.PRINT virgülleri aktarmaz.
2)WRITE komutu pozitif sayıların sol tarafında boşluk bırakmadan yazdırır.PRINT boşluk bırakır.
Örnek;

```basic
10 X=15 : Y=9 Z$="ESRAGÜL"
20 WRITE X,Y,Z$
```
Sonuç : 15,9,"ESRAGÜL"

**5.1 LOCATE komutu** : LOCATE X,Y şeklindedir.
Kursörün konumu X'ıncı satır Y'inci sütundur.

**5.2 READ/DATA deyimleri** :READ deyime değişkenlere değer okur.Bu değerlerin okunduğu yer DATA deyimidir.
Örnek;1

```basic
10 READ a,b,c
20 DATA 1,2,3
```
Sonuç : a=1, b=2, c=3 şeklinde görülür.

Örnek;2

```basic
10 READ X,Y,Z
20 DATA 1,2,3
30 SUM=X+Y+Z
40 PRINT "X=";X. "Y=";Y, "Z=";Z, "SUM=";SUM
50 END
```

Sonuç : X=1 Y=2 Z=3
SUM =6

Örnek;3

```basic
10 PRINT A
20 READ A
30 DATA 12
40 END
```
Sonuç: Ekranda sıfır değeri görülür.Çünkü A ya değer atanmadan önce programda 10 numaralı deyimle yazdırılmaktadır.

**5.3 RESTORE deyimi** : DATA deyimin dan okunan değerlerin programın daha sonraki bir kısmında tekrar okunması gerekebilir.Bu kısaca RESTORE deyimi ile sağlanır.

RESTORE [satır no'su]; eğer satır no su yazılmadıysa bir sonraki READ deyimi, programdaki ilk DATA deyimindeki değeri alır.
Örnek;

```basic
10 READ A,B,C,D
20 RESTORE
30 READ X,Y,Z,Q
40 DATA 1,2,3,4
50 LPPRINT A;B;C;D;X;Y;Z;Q
60 END
```

Sonuç : 1 2 3 4 1 2 3 4 bu şekilde görülür.

**5.4 INPUT deyimi :** Girilen karakterlere klavyeden değer atanmasını sağlar.

Örnek;

```basic
10 INPUT "EN VE BOY NEDİR?";A,B
20 ALAN=A*B
30 LPPRINT "DIKDÖRTGENIN ALANI" ALAN "DÜR"
40 END
```

Sonuç : Önce ekranda EN VE BOY NEDİR? görülür.Klavyeden değer girilir,mesela 20,5 değerleri girilir ve Enter'a basılırsa DIKDÖRTGENIN ALANI 100 DÜR ifadesi ekranda görülür.

**6.0 GOTO deyimi : **Herhangi bir koşul olmadan programın kontrolünü belirlenen satıra göndermek için kullanılır.

Soru: Verilen sayıların toplamını bulan ve sayıların kaçtane olduğunu hesaplayan program;

```basic
10 TANE=0: TOPLAM=0
20 READ A
30 TANE=TANE+1
40 TOPLAM=TOPLAM+A
50 PRINT "TANE", "SAYI", "TOPLAM"
60 PRINT TANE, A, TOPLAM
70 GOTO 20
80 DATA 20, 30, 40, 50
90 END
```

Sonuç : TANE SAYI TOPLAM
1 20 20
TANE SAYI TOPLAM
2 30 50
TANE SAYI TOPLAM
3 40 90
TANE SAYI TOPLAM
4 50 140

**6.1 IF deyimi :** Bir ifade doğruysa THEN'i izleyen deyimler yapılır.Eğer ifade yanlışsa ELSE'i izleyen deyimler yapılır.
IF...THEN... ELSE

Örnek1;

```basic
10 LET X=2: LET Y=3
20 IF X<=Y THEN A=X+Y ELSE A=X*Y
30 PRINT A
40 END
```

Sonuç : A= 5 Ekranda görülür.

Örnek2;

```basic
10 INPUT A,B
20 LPPRINT "a=";A, "b=";B
30 IF A > B THEN LPPRINT "a,b den büyüktür" ELSE IF B>A THEN LPPRINT "a,b den küçüktür"
ELSE LPPRINT "a,b ye eşittir"
```

Sonuç : a=12 b=45
a,b den küçüktür ifadesi Ekranda görülür.

Örnek3;

```basic
5 INPUT A,B
10 IF A<>B GOTO 5 ELSE PRINT "A,B ye eşittir"
20 PRINT "A=";A, "B=";B
25 GOTO 5
30 END
```

Sonuç : Eğer A,B ye eşit değilse 5 numaralı deyime gidilir .Eşitse ELSE'i izleyen deyim yapılır.Bundan sonra GOTO deyimi ile yeni bir A,B değere okunmak üzere 5 numaralı deyime gidilir.

**7.0 FOR ve NEXT deyimleri :** Bu deyim sayaç görevi görür.

Örnek1;

```basic
10 FOR X=1 TO 5 STEP 2
20 PRINT "X=",X
30 NEXT X
```

Sonuç : X'ın başlangıç değeri 1 son değeri 5 tir.X herdefasında ikişer artar.Sonuç olarak X=5 ise Ekrana 5 değeri yazılır.

Örnek2;

```basic
10 INPUT N
20 FAKT=1
30 FOR I=2 TO N
40 FAKT=FAKT*I
50 NEXT I
60 LPPRINT "n!=1*2*3*4......";N;"=";FAKT
70 END
```

Sonuç : Önce I =2 için 40 nolu deyimde FAKT=1*2=2 görülür.Sonra I birer birer artar ve N değerine ulaşınca 1*2*3...N =N! sonucu görülür.

Örnek3;

```basic
10 FOR I=1 TO 2
20 FOR X=1 TO 3
30 PRINT "I=";I, "X=";X
40 NEXT X,I
```

Sonuç : I=1 X=1
I=1 X=2
I=1 X=3
I=2 X=1
I=2 X=2
I=2 X=3 Şeklinde iç içe döngü görülür.

**7.1 WHILE/WEND deyimi: **Ifade doğru olduğu sürece WHILE ve WEND arasındaki deyimler işlenir. WEND'e gelince program WHILE deyimine döner.Ifade yanlış olursa WEND'den sonraki deyimler işlenir.

Örnek;

```basic
10 X= -1
20 Y= 0
30 WHILE X
40 Y=Y+1
50 IF Y>6 THEN X=0
60 WEND
70 LPPRINT "X=";X,"Y=";Y
80 END
```

S onuç : Y değeri 6'dan küçük olduğu sürece Y'ye 1 eklenmektedir.50 deyimi ile Y'nın değeri 6'dan büyük olduğu anda X'e 0 atanır.60 deyimi ile 30 deyimine gelince,X=0 olduğu için program 70 deyimine geçer ve X=0,Y=7 Ekrana yazılır.

**8.2 ALT PROGRAMLAR -GOSUB VE RETURN DEYİMLERİ**

Program içinde aynı türden bir işlem bir çok kez tekrarlanıyorsa basic deyimlerine her seferinde tekraryazmak yerine bu işlemi alt program halinde tanımlayarak daha kısa sürede işlemi bitirebiliriz.
GOSUB (satır no su) şeklinde ifade edilir.

Örnek;

```basic
10 GOSUB 40
20 LPPRINT "ESRAGÜL KOYUNCU"
30 END
40 LPPRINT "ASAAD";
50 LPPRINT "MOHAMED"
60 RETURN
```

Sonuç : 10 GOSUB 40 deymi ile program 40 deymine gelir.Bu deyimle ASAAD MOHAMED yazılır.60 RETURN deyimine gelince program 20 LPPRINT deyimine gelir ve ESRAGÜL KOYUNCU yazar.
ASAAD MOHAMED
ESRAGÜL KOYUNCU

**9.1 BASIC'te MATRİS DEYİMLERİ**

DIM : Bütün Matrislerin boyutları bu deyimle gösterilir.DIM A (1,20) ifadesi Matrisin bir satır ve 20 sütün dan oluştuğunu gösterir.
MAT : Bütün Matris deyimleri bu ifadeyle başlar.
Örnek;

```basic
10 DIM A (2,3 )
20 MAT READ A
30 DATA 1,2,3,6,11,13
40 MAT PRINT A
50 END
```
Sonuç :
1 2 3
6 11 13

MATRIS'te TOPLAMA ve ÇIKARMA
MAT A = B+C MAT A= A-B Şeklinde yazılır.

MAT A= B+C+D Şeklinde yazılmaz dığrusu MAT E= C+D
MAT A= B+E Şeklinde yazılır.
matrısın transpozu MAT B=TRN(A)
matrısın tersı MAT A= INV(B) Şeklindedir.

Örnek;

```basic
10 DIM A(2,6)
20 MAT READ A
30 DATA 1,2,3,4,5,6,7,8,9,10,11,12
40 MAT PRINT A,
```
Sonuç: 1 2 3 4 5
6
7 8 9 10 11
12

NOT: Eğer MAT PRINT deyimindan sonra virgül kullanılırsa her eleman arasına büyük boşluk bırakır.Eğer noktalı virgül kullanılırsa hiç boşluk bırakmaz.

Örnek;

```basic
10 DIM A(2,4),B(2,4),C(4,2),P(3,3),Q(3,3)
20 MAT READ A
30 DATA 1,2,3,4,5,6,7,8
40 PRINT "ESRA FORMU"
50 MAT PRINT A,
60 PRINT "GÜL FORMU"
70 MAT PRINT A;
80 MAT C = TRN(A)
90 PRINT "TRANSPOZE",
100 MAT PRINT C;
110 MAT E=CON
120 MAT A=A-B
130 MAT PRINT A;B;
140 MAT P=IDN
150 MAT Q=ZER
160 MAT P=P+P
170 MAT PRINT P;Q;
180 END
```

Sonuç: ESRA FORMU
1 2 3 4
5 6 7 8

GÜL FORMU
1 2 3 4
5 6 7 8

TRANSPOZE
1 5
2 6
3 7
4 8
0 1 2 3
4 5 6 7
1 1 1 1
1 1 1 1
2 0 0
0 2 0
0 0 2
0 0 0
0 0 0
0 0 0

Esragül KOYUNCU

---
*Kaynak: `BASIC DILI/BASIC DILI.doc` — ekim kaya — 2004*
