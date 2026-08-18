# Visual Basic 'De Operatorler

**7. BÖLÜM**

**OPERATÖRLER**

** 7.1. Aritmetik Operatörler**

| **İşaret** | **Anlam** | **Örnek** |
| --- | --- | --- |
| **=** | Atama | a=10 |
| **+** | Toplama | MsgBox 30+12 ‘42 |
| **-** | Çıkarma | MsgBox 20-5 ‘15 |
| **\*** | Çarpma | MsgBox 4\*3 ‘12 |
| **/** | Bölme | MsgBox 7/2 ‘3.5 |
| **\\** | Tam Bölme | MsgBox 7\\2 ‘3 |
| & | String Toplama | MsgBox “Ela” & “zığ” ‘Elazığ |
| **^** | Üst | MsgBox 2^3 ‘8 |
| Mod | Bölmede Kalan | MsgBox 7 Mod 2 ‘1 |

Tablo-7.1. Aritmetik Operratörler

**7.2. Mantıksal Operatörler**

| **İşaret** | **Anlam** | **Örnek** |
| --- | --- | --- |
| And | Ve | MsgBox 7 And 2 ‘111 And 010= 010 |
| Or | Veya | MsgBox 5 Or 2 ‘101 And 010= 111 |
| Xor | Xor | MsgBox 7 And 2 ‘111 And 010= 101 |
| Not | Değil | MsgBox Not 6 ‘110=001 |

Tablo-7.2. Mantıksal Operatörler

**7.3. Karşılaştırma Operatörleri**

| **İşaret** | **Anlam** | **Örnek** |
| --- | --- | --- |
| = | Eşit | If x = 2 |
| <> | Farklı | If x <> 2 |
| < | Küçük | If x < 2 |
| > | Büyük | If x > 2 |
| <= | Küçük eşit | If x <= 2 |
| >= | Büyük eşit | If x >= 2 |

Tablo-7.3. Karşılaştırma Operatörleri

**7.4.. Like Operatörleri**

VB’de Like operatörü ile stringler üzerinde daha detaylı karşılaştırma işlemleri yapılabilmektedir. Like operatöründe tıpkı dosya isimlerinde olduğu gibi joker karakterler vererek karşılaştırma yapmak mümkündür.

Like operatöründe kullanılabilecek joker karakterler şunlardır.

| İşaret | Anlamı |
| --- | --- |
| ? | Herhangi bir karakter |
| \# | Herhangi bir rakam |
| \* | Bir veya daha fazla karakter |
| \[Aralık\] | Verilen aralıkta bir karakter |
| \[!Aralık\] | Verilen aralık dışında karakter |

Tablo-7.4. Like Operatörleri Joker karekterleri

If bolum Like “\*bilgisayar” Then

İfadesi ile bolum değişkeninin sonunda bilgisayar olup olmadığını kontrol eder.

If bolum Like “\*bilgisayar\*” Then

İfadesi ile bolum değişkeninin herhangi bir yerinde bilgisayar olup olmadığını kontrol eder.

If bolum Like “\*?ilgisayar\*” Then

İfadesi ile bolum değişkeninin ilk harfinin her hangi bir karakter ancak diğer karakterlerin ilgisayar olup olmadığını kontrol eder.

** 7.5. İşlem Önceliği**

| **Aritmetik** | **Karşılaştırma** | **Mantıksal** |
| --- | --- | --- |
| ^ Negatif İşareti (-) \*,/ \\ Mod +,- & | = <> < > <= >= Like Is | Not And Or Xor Eqv Imp |

Tablo-7.5. İşlem Önceliği

PAGE

PAGE 80

---
*Kaynak: `VISUAL BASIC 'de OPERATORLER/VB’DE OPERATÖRLER.doc` — BAHADIR İŞLEYEN — 2004*
