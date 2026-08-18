# Bir Veri Tabaninin Oluşturulmasi

**BÖLÜM 1**

**BİR VERİ TABANININ OLUŞTURULMASI**

**1.1 Giriş**

SQL ile gerçekleştirilecek işlemlerde, üzerinde işlem yapılacak olan veri** **tabanı kütükleri ya da tablolar, bir veri tabanı içinde oluşturulur.Bu veri tabanını oluşturmak için,

```sql
CREATE DATABASE isim;
```

şeklindeki SQL komutunu kullanmak gerekir.Bu komut belirtilen isim’deki veri tabanını oluşturur.(Burada veri tabanı, içinde çok sayıda veri tabanı kütüğü ya da SQL terimleri ile tablo bulunan bir çevre bellek bölgesidir ya da bir alt dizin (subdirectory) adıdır.)

Veri tabanı içersinde, bir işletmenin çeşitli faaliyetleri ile ilişkili aşağıdaki tür de bilgiler yüklemek istediğimizi varsayalım:

Personel Tablosu:

Sicil NoSos. Güv. NoAdSoyadDoğum TarihiAdresCinsiyetMaaşBöl-NoYön. Sos. Güv. No

Bölüm Tablosu:

| Bölüm Adı | Bölüm No | Yönetici Sosy. Güvenlik No |
| --- | --- | --- |

Yer Tablosu:

| Bölüm No | Bulunduğu Yer |
| --- | --- |

```sql
Proje Tablosu:
```

| Proje Adı | Proje No | Yer | Bölüm No |
| --- | --- | --- | --- |

Çalışma Tablosu:

| Personel Sos. Güv. No | Proje No | Saat |
| --- | --- | --- |

Bağımlılık Tablosu:

| Personel Sos. Güv. No | Bağl. Old. İsim | Cinsiyet | Doğum Tarihi | İlişki |
| --- | --- | --- | --- | --- |

Parça Tablosu:

| Parça No | Parça Adı | Proje No | Fiyat | Ağırlık |
| --- | --- | --- | --- | --- |

Satıcı Tablosu:

| Satıcı No | Adı | Adres |
| --- | --- | --- |

Parça-Satıcı Tablosu:

| Satıcı No | Parça No | Miktar |
| --- | --- | --- |

Bu tabloların her sütunu, tabloda saklanan verilerle ilişkili bir özelliği (attribute) belirtmektedir. Her tablo satırı, birbiri ile ilişkili verileri saklamaktır. Tablolar arası ilişkiler ise, müşterek özellikler (sütunlar) sayesinde gerçekleştirilecektir. Örneğin, “İstanbul’da yürütülen projelerde çalışan kişileri listeleyiniz.” şeklindeki bir talep, Proje, Çalışma ve Personel tablolar arasıda ilişki kurulmasını gerektirecek ve örneğin, Proje tablosunda, Yer alanında İstanbul bulunan projelerin Proje No’ları ile Çalışma tablosundaki Proje No’ları mukayese edilecek, aynı olanları için; Çalışma tablosundan alınacak Personel Sos.Güv. No’ları ile Personel tablosunda arama yapılacak, bulunan kişilere ait bilgiler Personel tablosundan listelenecektir. Bu tür işlemlerle ilişkili SQL komutları ilerdeki bölümlerde verilecektir.

**1.2 Tabloların Yaratılması**

SQL ile giriş bölümünde verilen tabloların yaratılması için, CREATE TABLE komutunu uygun şekli ile kullanmak gerekir. Aşağıdaki, bu tabloları yaratacak SQL komutları verilmiştir.

```sql
CREATE TABLE tabloadı;
```

komutu ile tablolar oluşturulur.Bu komutu kullanırken SQL’in uygun veri tipleri kullanılır.

**ÖRNEK:**
```sql
CREATE TABLE Personel
(sicil INTEGER NOT NULL,
sosy_g_no CHAR(8) NOT NULL
ad CHAR(10) NOT NULL,
soyad CHAR(10) NOT NULL,
dog_tar DATE, adres CHAR(50),
cinsiyet LOGICAL, maas NUMERIC(13,2),
bol_no SMALLINT, yon_s_g_n CHAR(8));
```

Yukarıdaki örnekte Giriş kısmında verilen Personel Tablosunun nasıl oluşturulduğu verilmiştir. Diğer tablolarda aynı şekilde gerekli SQL veri tipleri kullanılarak yaratılır.

NOT NULL ifadesi söz konusu alan ile ilişkili olarak mutlaka veri yüklenmesi gerektiğini, ilgili alanın boş bırakılmayacağını anlatmaktadır.NOT NULL ifadesi yoksa, o alan NULL anlamındadır.Yani o alan ilişkili olarak veri yüklenmemesi durumuna da müsaade edilmektedir.

**1.3 SQL’de Veri Tipleri**

Tabloların oluşturulması için kullanılan CREATE TABLE komutu içersinde, tablonun her sütunu için kullanılan isimlerin her birinin farklı tiplerde tanımlandığını gözlediniz. Bu tanımları içinde CHAR, VARCHAR, INTEGER, SMALLINT, DATE, LOGICAL, NUMERIC(x,y) gibi ifadeler, SQL içinde tablodaki alanlara (sütun adı, attribute) yüklenebilecek veri tiplerini belirten sözcüklerdir. Tablo 1.1’de SQL’de mümkün veri tipleri ve özellikleri görülmektedir.

**Tablo 1.1 **SQL’de Veri Tipleri.

| **VERİ TİPİ** | **SQL KOMUTU** | **ÖZELLİĞİ** |
| --- | --- | --- |
| 1)Sabit uzunluklu karakter | CHAR(Uzunluk) ÖRNEK: CHAR(15) gibi. | Sayısal işleme sokulmayacak veriler için kullanılır.Adres,isim,açıklama v.b. Uzunluk sabit olarak belirlenir. Maksimum uzunluk 254 karakterdir. |
| 2)Değişken uzunluklu karakter | VARCHAR(Uzunluk) Buradaki uzunluk, maksimum uzunluktur.Veri daha kısa ise, uzunluğun gerektiği kadarı kullanılır. ÖRNEK: VARCHAR(23) gibi. | Karakter türündeki veriler gibidir. Tek fark, uzunluk değişkendir; yani verinin gerektirdiği uzunluk kullanılır.Bu veri tipi standart değildir.Her derleyicide bulunmaz. |
| 3)Nümerik tam sayı | INTEGER | -2147483648 ile +2147483647 arasındaki tam sayılar için kullanılır.Ondalıklı nokta kullanılamaz.Bellekte 4 byte’lik yer kaplar. |
| 4)Nümerik kısa tam sayı | SMALLINT | -32768 ile +32767 arasındaki tamsayılardır.Bu veri tipi standart değildir.Bazı derleyicilerde tanımlanmamıştır.Bu durumda veri tipi INTEGER’a çevrilir. |
| 5)Ondalık sayı | DECIMAL(x,y) REAL(x,y) ya da NUMERIC(x,y) şeklinde tanımlanabilir. | x sayısı maksimum hane (digit) sayısı, y ondalık noktadan sonraki hane sayısıdır. x en fazla 20 olabilir. y 0-18 arasındadır. Örnek: -10.22 veya 1056.82 gibi sayılar. |
| 6)Üstel sayı | FLOAT(x,y) | x sayısı toplam hane (digit) miktarıdır.Maksimum değer 20’dir. y ondalık noktadan sonraki hane sayısıdır. 0-18 arasındadır. 0.1 E-307 ile 0.9 E+308 arasındaki değerleri alabilir.Çok küçük ve çok büyük sayılar için uygun olan veri tipidir. |
| 7)Tarih türü veriler | DATE | Tarih türü bilgiler üzerinde işlem yapma imkanı sağlar.SQL için standart bir veri tipi değildir.Bir gerçekleştirimden diğerine farklı şekilde kullanımı mümkündür. |
| 8)Mantıksal veri | LOGICAL | Doğru (True, .T.) ya da yanlış (False, .F.) şeklinde değer alabilen veriler için kullanılır. |
| 9)Zaman türü veriler | TIME | ss:dd:snsn (saat, dakika, saniye) şeklinde veriler için kullanılır. Standart değildir. |
| 10)Tarih ve zaman türü veriler | TIMESTAMP | Tarih ve zaman türü verilerin bir karışık şeklinde kullanılan veriler içindir.Standart değildir. |
| 11)Grafik türü veriler | GRAPHIC(n) | n adet 16 bitlik karakterden oluşan bir sabit uzunluklu bilgi tanımlamak için kullanılır. (Karakter türü veri, 8 bitlik karakterden oluşmaktadır.) Standart değildir. |
| 12)Değişken uzunluklu grafik türü veri | VARGRAPHIC(n) | n adet 16 bitlik karakterden oluşan değişken uzunluklu (n maksimum uzunluktur.) bir bilgi tanımlamak için kullanılır. Standart değildir. |

SQL’de kabul edilen, zaman ve tarih formatları Tablo 1.2 ve Tablo 1.3’te verilmiştir.

**Tablo 1.2 **SQL’de Tarih Formatları.

| **STANDART ADI** | **TARİH FORMATI** | **ÖRNEK** |
| --- | --- | --- |
| Uluslararası Standartlar Organizasyonu (ISO) | yyyy-aa-gg y –yıl a –ay g –gün | 1992-11-29 |
| IBM ABD Standardı USA | aa/gg/yyyy | 11/29/1992 |
| IBM Avrupa Standardı EUR | gg.aa.yyyy | 29.11.1992 |
| Japon Endüstri Standardı JIS | yyyy-aa-gg | 1992-11-29 |

**Tablo 1.3 **SQL’de Zaman Formatları.

| **STANDART ADI** | **ZAMAN FORMATI** | **ÖRNEK** |
| --- | --- | --- |
| Uluslararası Standartlar Organizasyonu (ISO) | SS.dd.ss S –saat d -dakika s –saniye | 16.25.07 |
| IBM ABD Standardı USA | SS:dd AM veya PM | 16:25 PM |
| IBM Avrupa Standardı EUR | SS.dd.ss | 16.25.07 |
| Japon Endüstri Standardı JIS | SS:dd:ss | 16:25:07 |

**1.4 Tablolara Veri Yüklenmesi**

Bir tabloya veri girişi (veri yüklemesi) işlemi için;

```sql
INSERT INTO Tabloadı VALUES
```

komutu kullanılır.

**ÖRNEK:**
```sql
INSERT INTO Kimlik
VALUES (‘Ahmet’,’Yılmaz’,’25.12.1975’,’Trabzon’);
```

**1.5 Tablodaki Sutün İsimleri ve Tablo İsimleri İle İlişkili Kurallar**

İsim uzunlukları 18 karaktere kadar olabilir. (Bazı SQL uygulamalarında 8 karaktere kadar)

İlk karakter bir harf olmalıdır. Onu izleyen karakterler, harf, rakam ya da alt çizgi sembolü ( \_ ) olabilir.

**BÖLÜM 2**

**TEK TABLO İÇİNDE SORGULAMALAR**

**2.1 Giriş**

SQL içinde, tek bir tablo içinde çeşitli kriterlere göre bilgi sorgulama, bilgiyi sıralı olarak elde etme, bilgi özetleme, ortalama vb. gibi matematiksel işlemleri gerçekleştirmeyi sağlayan komut ve fonksiyonlar vardır. Ayrıca, doğal olarak, aynı tipte işlemleri birden çok tabloyu birlikte ele alarak gerçekleştirmekte mümkündür.

Bu bölümde öncelikle tek tablo ile ilişkili sorgulamalar ve gerekli SQL komutları incelenecektir.

**2.2 Temel SQL Sorgulamaları Select Komutu**

Tek tablodan gerekli bilgileri elde etmek için sorgulama yapabilecek SQL komutu olan SELECT’in en basit şekli aşağıdaki gibidir.

```sql
SELECT *
FROM Tabloadı;
```

Bu komut Tabloadı kısmında adı yazılı tablo içindeki bütün bilgileri koşulsuz olarak listeleyecektir. SELECT sözcüğünü izleyen kısımda \* sembolünün bulunması, ilgili tablodaki bütün sütun (kolon) isimlerinin ve ilgili bilgilerin listelenmesini sağlayacaktır. Burda istersek \* sembolü yerine bütün alanların adını veya işlem yapacağımız alan ya da alanların adını yazarız.

**ÖRNEK:**
```sql
SELECT *
FROM Kimlik;
```

**ÖRNEK:**
```sql
SELECT ad,soyad,dogumtar,dogumyer
FROM Kimlik;
```

Yukarıdaki iki örnekte Kimlik isimli tablodaki bütün alanları listeler. Eğer sadece ad alanının listelenmesini istersek;

```sql
SELECT ad
FROM Kimlik;
```

yazarız.

**2.3 Tekrarlı Satırların Ortadan Kaldırılması**

SQL dilindeki tablo yapısı, formal olarak tanımlanan ilişkisel veri tabanı tablo yapısından farklıdır. SQL de tablo içinde, birbirinin aynı data içeren satırlara müsaade edilir.(İlişkisel veri modelinde ise müsaade edilmez.)

Birbirinin aynı olan satırların, listeleme esnasında, bir kez yazılması için, SELECT komutuna DISTINCT sözcüğü eklenir.

```sql
SELECT DISTINCT Sat_no
FROM Par_sat;
```

Bu komut ile Par\_sat adlı tablodan Sat\_no‘lar tekrarsız olarak listelenecektir. Örneğin;

Par\_sat

| Sat\_no | Par\_no | Miktar |
| --- | --- | --- |
| S1 | P1 | 200 |
| S1 | P3 | 300 |
| S2 | P1 | 50 |
| S2 | P4 | 150 |
| ... | ... | ... |
| ... | ... | ... |

şeklinde bilgi içeriyorsa, komutun icrası sonucu

```sql
Sat_no
```

| S1 |
| --- |
| S2 |

listesi elde edilecektir.

**2.4 Tablo Bilgilerinin Sıralanmış Olarak Listelenmesi**

Tablodan listelenecek bilgilerin, belirli bir sütun adına göre (ad’a göre v.b.) sıralanmış olarak görüntülenmesi için, SELECT komutuna ORDER BY sözcüğü ilave edilir.

**ÖRNEK:** Personel isimli bir tabloda sicil, ad, soyad, maas sütunları olsun. Maaşa göre artan sırada (küçükten büyüğe doğru) sıralı olarak listeleyiniz.

| sicil | ad | soyad | maas |
| --- | --- | --- | --- |
| 2746 | Ali | Can | 7800000 |
| 1728 | Ayşe | Şener | 5600000 |
| 1116 | Mert | Okan | 8950000 |
| 1022 | Melih | Berkan | 7500000 |
| ... | ... | ... | ... |
| ... | ... | ... | ... |

```sql
SELECT sicil,ad,soyad,maas
FROM Personel
ORDER BY maas ASC;
```

**SONUÇ:**

| sicil | ad | soyad | maas |
| --- | --- | --- | --- |
| 1728 | Ayşe | Şener | 5600000 |
| 1022 | Melih | Berkan | 7500000 |
| 2746 | Ali | Can | 7800000 |
| 1116 | Mert | Okan | 8950000 |
| ... | ... | ... | ... |
| ... | ... | ... | ... |

ASC sözcüğü ascending** **(artan) anlamındadır. Veriler azalan sırada (büyükten küçüğe ya da alfabetik olarak Z’den A’ya doğru) sıralamak için ASC yerine DESC (descending) sözcüğü kullanılmalıdır.

**2.5 Birden Çok Alana Göre Sıralama**

Bir tablo içinde verilerin aynı anda birden çok sütun (alana) göre sıralamakta mümkündür. Örneğin Personel tablosunu ad ve maas alanlarına göre sıralamak isteyelim.

```sql
SELECT sicil,ad,soyad,maas
FROM Personel
ORDER BY ad,brüt;
```

Burada tablo öncelikle ad’a göre artan sırada (A’dan Z’ye doğru) sıralanacak, sadece aynı ad’a sahip olanlar kendi aralarında maas’a göre küçükten büyüğe (artan) sıralanacaktır.

| sicil | ad | soyad | maas |
| --- | --- | --- | --- |
| 1215 | Ali | Can | 2000000 |
| 3712 | Ali | Okan | 6000000 |
| 1152 | Ali | Mert | 8000000 |
| 3712 | Birol | Akın | 4000000 |
| 8145 | Birol | Çelen | 8500000 |
| 1248 | Birol | Okur | 11000000 |
| ... | ... | ... | ... |

**Şekil 2.1** Ad ve Maaş’a Göre Sıralama.

Burada, çok sayıda alana göre sıralama, farklı sıralama kriterlerine göre gerçekleştirilebilir. Örneğin aşağıdaki SELECT komutu ile ad** **alanına göre artan, soyad alanına göre azalan, maas alanına göre artan sıralanmış tablo elde edilmektedir.

```sql
SELECT sicil,ad,soyad,maas
FROM Personel
ORDER BY ad ASC,soyad DESC,maas ASC;
```

veya aynı komut için alternatif yazılış:

```sql
SELECT sicil,ad,soyad,maas
FROM Personel
ORDER BY ad,soyad DESC,maas;
```

şeklinde olacaktır. Örnek çıktı aşağıdaki gibidir.

| sicil | ad | soyad | maas |
| --- | --- | --- | --- |
| 2742 | Ahmet | Kaner | 8000000 |
| 1712 | Ahmet | Kaner | 16000000 |
| 3112 | Ahmet | Berk | 17000000 |
| 2712 | Melih | Caner | 12000000 |
| 1317 | Melih | Berat | 18000000 |
| 2718 | Zerhan | Şen | 7000000 |

**Şekil 2.2** Ad’a Göre Artan, Soyad’a Göre Azalan, Maaş’a Göre Artan Sıralama.

**2.6 Koşula Bağlı Olarak Listeleme**

SELECT komutu ile bir tablonun satırları içinde sadece verilen bir koşulu sağlayanlar da listelenebilir. Örneğin, maaşı 5000000 ‘dan fazla olan personel listelenmek istenirse, SELECT komutu aşağıdaki gibi yazılmalıdır:

```sql
SELECT *
FROM Personel
WHERE maas>5000000;
```

Burada WHERE sözcüğünü izleyen kısımda koşul belirtilmektedir. Koşul belirtilirken iki veri birbiri ile karşılaştırılmaktadır. SQL içinde, verileri çeşitli açılardan karşılaştırılmak için kullanılabilecek, karşılaştırma operatörleri Tablo 2.4’te verilmiştir.

Karşılaştırma ifadesinde karşılaştırılan verilerin türü aynı olmalıdır. Yani, bir karakter türü veri ile ancak karakter türünde başka bir veri, bir nümerik veri ile ancak nümerik olan başka bir veri karşılaştırılabilir.

**Tablo 2.4 **SQL’de Karşılaştırma Operatörleri.

| OPERATÖR | ANLAMI |
| --- | --- |
| < | Küçük |
| > | Büyük |
| = | Eşit |
| <= | Küçük veya eşit |
| >= | Büyük veya eşit |
| <> | Eşit değil |
| != | Eşit değil |
| Bazı SQL gerçekleştirimlerinde !< (den küçük değil) ve !> (den büyük değil) operatörleri de mevcuttur. |  |

**2.7 Çeşitli Veri Tipleri İçin Basit Sorgulamalar**

**Nümerik veri tipi**

Nümerik (sayıda) veri tipi, SMALLINT, INTEGER, DECIMAL, NUMERIC ya da FLOAT tipi bildiri sözcüklerinden biri ile tanımlanan, matematiksel işlemlere sokulabilen, özel semboller içine alınmayan (“ ” sembolleri gibi) verileri kapsar. Maaş, ürün miktarı vb. tipteki bilgiler bu türde olmalıdır.

**ÖRNEK:** Maaşı 8000000’dan fazla olmayan personeli listelemek.

```sql
SELECT *
FROM Personel
WHERE maas<=8000000;
```

**Karakter (char) veri tipi**

Karakter türündeki veriler, çift tırnak (“ “) veya tek tırnak (‘ ‘) sembolleri içine yazılır. Bu tip veriler, rakamdan oluşsa bile, matematiksel işlemler içinde kullanılamazlar. Örneğin “235”+2 işlemi geçersizdir.

**ÖRNEK:** Adı Ali olmayan personele ait kayıtları listelemek.

```sql
SELECT *
FROM Personel
WHERE ad<>”Ali”;
```

Veya

```sql
SELECT *
FROM Personel
WHERE ad !=”Ali”;
```

Bu komutlar sonucu aşağıdaki kayıtlar listelenebilir;

| sicil | ad | soyad | sos\_g\_no |
| --- | --- | --- | --- |
| 275 | Ahmet | Caner | 272534 |
| 117 | Melih | Akın | 387265 |
| 287 | ali | çokşen | 277421 |
| 444 | ali | cansu | 1722433 |

Adı’ı Ali** **olanları listelemek istememize rağmen, ali cansu ve ali çokşen listelenmiştir. Bunun sebebi, bilindiği gibi, bilgisayar açısından Ali karakter verisi ile ali karakter verisinin farklı veriler olmasıdır. Eğer ali cansu, Ali cansu şeklinde yazılmış olsa, listelemeyecekti. Bu özellik karakter türü verilerle işlem yaparken göz önünde bulundurulması gereken önemli bir noktadır.

**Tarih veri tipi**

Tarih tipi veriler, {} sembolleri içinde yazılmalıdır.

**ÖRNEK: **Hangi personelin, doğum tarihi 1960 yılından daha öncedir?

```sql
SELECT *
FROM Personel
WHERE dog_tar <={12/31/59};
```

Burada kullanılan SQL versiyonunda, tarih tipi verinin aa/gg/yy (ay/gün/yıl) formatında temsil edildiği varsayılmıştır.

SONUÇ:

| sicil | ad | soyad | dog\_tar |
| --- | --- | --- | --- |
| 2712 | Ali | Okan | 05/02/58 |
| 3718 | Hasan | Akın | 04/03/59 |

**Mantıksal (lojik) veri tipi**

Mantıksal veriler için mümkün olabilen sadece iki değer sözkonusudur.doğru (true, .T.) ile simgelenir, yanlış (false, .F.) ile simgelenir.

Personel tablosunda, personelin cinsiyetini belirleyen bir alanımız olsun. Cinsiyet adlı bu alanda cinsiyeti erkek olanlar true (.T.), kadın olanlar false(.F.) ile kodladığımızı kabul edersek, işletmede çalışan personel içinden erkek olanları listelemek için aşağıdaki gibi bir SQL kodu yazmak gerekecektir.

```sql
SELECT *
FROM Personel
WHERE cinsiyet=.T.;
```

Bu komut aşağıdaki şekilde de kullanılabilir;

```sql
SELECT *
FROM Personel
WHERE cinsiyet;
```

Bu durumda cinsiyet alanı .T. olanlar (erkek olanlar) listelenir.

**2.8 Birden Çok Koşula Dayalı Sorgulamalar (Not, And, Or)**

NOT, OR ve AND mantıksal operatörleri yardımı ile birden çok koşulun gerçekleşmesine bağlı olarak ifade edilebilecek karmaşık ya da birleşik koşullu listelemeleri gerçekleştirmek mümkün olmaktadır.

**ÖRNEK:** Maaşı 5000000 TL’den fazla olan ve cinsiyeti erkek olan personelin listelenmesi gibi bir işlemde, söz konusu personel için iki koşul verilmekte ve ikisinin de gerçekleşmesi istenmektedir:

1.Koşul → Maaşın 5000000’dan fazla oluşu

2.Koşul → Cinsiyetin Erkek olması

Her iki koşulunda aynı anda gerçekleşmesi istendiği için, VE (AND) sözcüğü ile birbirlerine bağlanmıştır.

Bu işlemi gerçekleştiren SQL komutu aşağıdaki gibidir.

```sql
SELECT *
FROM Personel
WHERE maas>5000000 AND cinsiyet=.T.;
```

NOT, AND ve OR operatörlerinin etkileri aşağıdaki tablolarda (Tablo 2.5, 2.6, 2.7) verilmiştir.

**Tablo 2.5 **NOT Operatörü.

| Koşul | NOT koşul |
| --- | --- |
| .T. | .F. |
| .F. | .T. |

**Tablo 2.6 **AND Operatörü.

| 1. Koşul | 2. Koşul | 1. Koşul AND 2. Koşul |
| --- | --- | --- |
| .T. | .T. | .T. |
| .T. | .F. | .F. |
| .F. | .T. | .F. |
| .F. | .F. | .F. |

**Tablo 2.7 **OR Operatörü.

| 1. Koşul | 2. Koşul | 1. Koşul OR 2. Koşul |
| --- | --- | --- |
| .T. | .T. | .T. |
| .T. | .F. | .T. |
| .F. | .T. | .T. |
| .F. | .F. | .F. |

Aşağıdaki örnek sorularla, mantıksal işlem operatörlerinin kullanımı konusunda fikir verilmektedir.

**SORU:** Doğum tarihi 1960’tan önce olan, maaşı 6000000 – 10000000 arasında olan bayan personel kimlerdir.

```sql
SELECT *
FROM Personel
WHERE dog_tar<{01/01/60} AND
Maas>=6000000 AND maas<=10000000
AND cinsiyet=.F.;
```

**SORU:** Satış bölümü ile muhasebe bölümündekiler kimlerdir?

Satış bölümünün bölüm no’sunun (bol\_no) 1 ve muhasebe bölümünün bol no ‘sunun 2 olduğunu varsayalım.

```sql
SELECT *
FORM Personel
WHERE bol_no=1 OR bol_no=2;
```

şeklinde listeleme gerçekleştirilebilir.

**SORU:** Doğum tarihi 1960’tan önce olmayan, cinsiyeti erkek olan veya dağum tarihi 1965’ten önce olmayan ve cinsiyeti kadın olan personeli listeleyiniz.

```sql
SELECT *
FROM Personel
WHERE dog_tar>={01/01/60} AND
cinsiyet=.T. OR dog_tar>={01/01/65}
AND cinsiyet=.F.;
```

**SORU:** Bölümü satış veya muhasebe olan kadın personeli listeleyiniz.

```sql
SELECT *
FORM Personel
WHERE bol_no=1 OR bol_no=2
AND cinsiyet=.F.;
```

şeklindeki SELECT komutu doğru görünüyorsa da, dikkatle düşünüldüğünde istenileni vermeyeceği anlaşılabilir. AND ; OR ‘a göre öncelikli olduğu için, değerlendirme:

Satış bölümünde çalışan (cinsiyeti ne olursa olsun)

veya

muhasebe bölümündeki kadın personel; şeklinde listeleme yapılacaktır.

Doğru cevap ()’ler ile öncelikleri değiştirerek aşağıdaki ifade ile elde edilebilir.

**NOT:** AND operatörü OR operatörüne göre daha önceliklidir.

```sql
SELECT *
FROM Personel
WHERE (bol_no=1 OR bol_no=2) AND cinsiyet=.F.;
```

**SORU: **Bölümü satış ya da muhasebe olmayan, 1960’tan sonra doğmuş, bayan personeli listelemek.

```sql
SELECT *
FROM Personel
WHERE NOT (bol_no=1 OR bol_no=2)
AND dog_tar>={01/01/60}
AND cinsiyet=.F.;
```

Eşdeğer cevap:

```sql
SELECT *
FROM Personel
WHERE bol_no<>1 AND bol_no<>2
AND dog_tar>={01/01/60} AND cinsiyet=.F.;
```

**2.9 Bir Veri Kümesi İçinde Arama (In Operatörü)**

Aşağıdaki örnek sorunun cevabını, şu ana kadar öğrendiğimiz SQL komutları ile gerçekleştirebiliriz:

**SORU:** bol\_no’su 1,2 ya da 3 olan personeli listeleyiniz.

```sql
1-) SELECT *
FROM Personel
WHERE bol_no=1 OR bol_no=2 OR bol_no=3;
```

Fakat SQL’de bu işlemi gerçekleştirmenin daha kısa ve daha şık bir yolu vardır; IN sözcüğünü kullanarak bu işlemi yaparız.

```sql
2-) SELECT *
FROM Personel
WHERE bol_no IN(1,2,3);
```

Bu komut, OR ile düzenlenen 1. SELECT komut grubuna denktir. Fakat belirtildiği gibi daha kısa ve anlaşılır bir ifade oluşmaktadır.

IN operatörü NOT ile birlikte de kullanılabilir.Örneğin aşağıdaki soru ile ilişkili üç ayrı eşdeğer SELECT komutu verilmiştir.

**SORU:** Bölüm 1,2 ve 3 olmayan personel kimlerden oluşmaktadır.

**CEVAP 1:**
```sql
SELECT *
FROM Personel
WHERE NOT(bol_no=1) AND
NOT(bol_no=2) AND NOT(bol_no=3);
```

**CEVAP 2:**
```sql
SELECT *
FORM Personel
WHERE bol_no<>1 AND
bol_no<>2 AND bol_no=3;
```

**CEVAP 3:**
```sql
SELECT *
FORM Personel
WHERE bol_no NOT IN(1,2,3);
```

**2.10 Aralık Sorgulaması (Between Sözcüğü)**

**ÖRNEK:** Maaşı 5000000 – 10000000 arasında olan personel kimlerdir.

```sql
SELECT *
FORM Personel
WHERE maas>=5000000 AND
Maas<=10000000;
```

şeklindeki bir SELECT komutu ile bu işlem gerçekleştirilebilir. Aynı soruya daha kısa ve daha etkin cevap verebilecek bir SQL komutu ise BETWEEN sözcüğü ile aşağıdaki gibi düzenlenebilir.

```sql
SELECT *
FORM Personel
WHERE maas BETWEEN 5000000
AND 10000000;
```

**2.11 Karakter Türü Bilgi İçinde Arama Yapma (Like Sözcüğü)**

Personel tablosu içinde adres adlı 50 karakter uzunluğunda bir alanımız olsun. Adres bilgisinin aşağıdaki şekilde verildiğini varsayalım:

Cumhuriyet Cad. 46/9 Taksim/İSTANBUL

Burada, adres içinde, semtinde belirtildiğini ve bunun ayrı bir sütun (alan) olmadığına dikkat çekelim. Şimdi belirli bir semtte ikamet eden personeli listelemek istersek, semt adını, adres alanı içinde aramak gerekecektir. Bu işlemi gerçekleştirmek için SQL’de LIKE sözcüğü kullanılır. Aşağıdaki SELECT komutunu inceleyelim:

```sql
SELECT *
FROM Personel
WHERE adres LIKE ‘%Taksim%’;
```

Bu komut ile “Taksim” semtinde ikamet eden personel listelenmek istenmektedir. Bu komut gerçektende “Taksim” de oturan kişileri listeleyecektir. Ama bu arada

“Taksim Caddesi 22-7 Kadıköy - İST”

şeklindeki adresleri de listeleyecektir.

```sql
adres LIKE ‘%Taksim%’
```

ifadesi, adres içinde Taksim’i arayacaktır. Adres içinde, herhangi bir yerde, bulduğu takdirde, bu satırı (bu kayıt, personeli) listeleyecektir.

% sembolü, Taksim sözcüğünün öncesi ve sonrasındaki karakterler ne olursa olsun anlamındadır.

LIKE sözcüğünü, alt çizgi (-) sembolü ile birlikte kullanmak da mümkündür.

**ÖRNEK:**
```sql
SELECT *
FROM Personel
WHERE ad LIKE ‘Mehmet----’;
```

şeklindeki komut ile ad alanı “Mehmet” ile başlayan ve ad alanı uzunluğu 10 karakter olan isimlere sahip personeli listeleyecektir. ”Mehmet Ali”, “Mehmet Can”, “Mehmetcik” gibi isimler listelenecektir. Anlaşılacağı gibi - sembolü, tek karakterlik bir bilgiyi temsil etmektedir.

**BÖLÜM 3**

**SQL’DE ARİTMETİKSEL İFADELER ve FONKSİYONLAR**

**3.1 Aritmetiksel İfadeler**

** **SELECT komutu ile, veri tabanında mevcut tablolardan listeleme yaparken, tabloda ayrı bir sütun (alan) olarak yer almamışve ancak bir hesaplama sonucunda üretilebilecek bilgileri de liste içine katmak mümkündür.

Aşağıdaki SELECT komutu ile, personelin şu anda geçerli olan maaşı ile, bu maaşın %32 zamlı şekli listelenmektedir.

```sql
SELECT ad,soyad,maas,maas*1.32
FORM Personel;
```

Hesaplanmış alanları elde etmek için oluşturulacak aritmetiksel ifadelerde, Tablo 3.1’de belirtilen semboller kullanılabilir.

**Tablo 3.1 **SQL’de Aritmetiksel Semboller.

| OPERATÖR | İŞLEVİ |
| --- | --- |
| \*\* veya ^ | Üs alma |
| \* | Çarpma |
| / | Bölme |
| + | Toplama |
| - | Çıkarma |

Öncelikli sırası, matematikte ve diğer bilgisayar dillerinde olduğu gibidir. Üs alma, hepsinden öncedir. Sonra çarpma (\*) ve bölme (/) gelir. Toplama (+) ve çıkarma (-) en son önceliklidir.

Parantez kullanılarak öncelikler değiştirilebilir.

**3.2 Kümeleme Fonksiyonları**

SQL tablo içinden, çeşitli matematiksel işlemlerin sonucunu otomatik olarak üretmeyi sağlayan, fonksiyonlara sahiptir. Bu fonksiyonlar, örneklerle birlikte aşağıda verilmiştir:

**3.2.1 SUM fonksiyonu**

Fonksiyonun argümanı olarak belirtilen sütun ile ilişkiliolarak toplama işlemini gerçekleştirir.

**SORU: **İşletmedeki personelin maaşlar toplamı ne kadardır?

**ÇÖZÜM:**
```sql
SELECT SUM(maas)
FROM Personel;
```

**SORU:** Bilgi işlem bölümündekilerin maaşları toplamı ne kadardır?

**ÇÖZÜM:**
```sql
SELECT SUM(maas)
FROM Personel
WHERE bol_no=5;
```

ifadesi ile sonuç elde edilebilir. Sonuç, sadece bilgi işlem bölümdekilerin maaşları toplamı şeklinde olacaktır.

**SORU: **Satış, muhasebe ve bilgi işlem bölümündeki personelin maaşları toplamı nedir?

**ÇÖZÜM:** Satış bölümü için bol\_no 1, muhasebe için 2 ve bilgi işlem için bol\_no 5 olarak alınırsa

```sql
SELECT SUM(maas)
FROM Personel
WHERE bol_no IN(1,2,5);
```

**SORU:** Maaşları 5000000 TL’nin altında olan bayan personelin maaşları toplamı nedir?

**ÇÖZÜM:** Bayan personeli, daha önceden cinsiyet alanına .F. yerleştirerek kodlamış isek

```sql
SELECT SUM(maas)
FROM Personel
WHERE cinsiyet=.F. AND
maas<5000000;
```

ifadesi istenilen çözümü verecektir.

**3.2.2 AVG fonksiyonu**

Aritmetiksel ortalama (avarage) hesaplamak için kullanılır.

```sql
SELECT AVG(maas)
FROM Personel;
```

Komutu, işletmedeki ortalama maaşı hesaplayarak görüntüleyecektir. Bu fonksiyon ile de, koşula bağlı olarak hesaplatma yaptırılabilir.

**SORU:** Bilgi işlem bölümündekilerin maaş ortalaması ne kadardır?

**ÇÖZÜM:** Bilgi işlem bölümünün bol\_no’su 5 ise

```sql
SELECT AVG(maas)
FORM Personel
WHERE bol_no=5;
```

ifadesi istenilen çözümü verecektir.

**3.2.3 MAX fonksiyonu**

Tablo içinde, belirlenen sütun (alan) içindeki en büyük değeri bulur.

**SORU:** İşletme içindeki en yüksek maaş ne kadardaır?

**ÇÖZÜM:**
```sql
SELECT MAX(maas)
FORM Personel;
```

**SORU:** Bilgi işlem bölümündeki en yüksek maaş ne kadardır?

**ÇÖZÜM:** Bilgi işlem bölümünün 5 ile kodlandığı varsayımı ile

```sql
SELECT MAX(maas)
FROM Personel
WHERE bol_no=5;
```

**SORU:** Bayan personel içinde en yüksek maaş ne kadardır?

**ÇÖZÜM:**
```sql
SELECT MAX(maas)
FROM Personel
WHERE cinsiyet=.F.;
```

**3.2.4 MIN fonksiyonu**

Tablo içinde, belirlenen sütun (alan) içindeki en küçük değeri bulur.

**SORU:** İşletme içinde 4 Mayıs 1970’den önce doğanlar için, asgari ücret nedir?

**ÇÖZÜM:**
```sql
SELECT MIN(maas)
FROM Personel
WHERE dog_tar>{05/04/70};
```

**3.2.5 COUNT fonksiyonu**

** **Tablo içerisinde herhangi bir sayma işlemi gerçekleştirmek için kullanılır.

**SORU:** Personel tablosunda kaç satır vardır? (Bu, her satırda farklı bir personel bulunduğu düşünülürse, personel sayısı anlamına gelmektedir.)

**ÇÖZÜM:**
```sql
SELECT COUNT(*)
FROM Personel;
```

**SORU:** Maaşı 6000000’dan fazla olan personel sayısı nedir?

**ÇÖZÜM:**
```sql
SELECT COUNT(*)
FROM Personel
WHERE maas>6000000;
```

COUNT fonksiyonu, DISTINCT sözcüğü ile de kullanılabilir. Örneğin, personel tablosunda mevcut personelin, işletme içinde kaç tane farklı bölümde çalıştığı bulunmak istenirse aşağıdaki SELECT komutu kullanılabilir.

```sql
SELECT COUNT(DISTINCT bol_no)
FROM Personel;
```

COUNT komutunda, \* argümanının kullanılması, bütün sütunların (alanların) işleme sokulması, alan adının belirtilmesi ise (COUNT(bol\_no) gibi), sadece, belirtilen sütunun işleme sokulmasını sağlar.

**3.3** **Gruplandırarak İşlem Yapma******

SUM, AVG, MAX, MIN, COUNT fonksiyonları, tablodaki bilgileri, bazı özelliklere göre gruplandırarak bu gruplandırılmış veri üzerine de uygulamak mümkündür. Bu işlem, GROUP BY sözcükleri yardımı ile gerçekleştirilebilir. Örneğin, aşağıdaki soru bu konuda bir fikir verecektir:

**SORU:** Her bölümdeki ortalama maaş nedir?

Burada istene, bölümler bazında ortalama maaş olduğuna göre, personel tablosundaki satırlar, bölüm numaralarına göre (bol\_no) gruplandırarak, her bir grubun maaş ortalaması ayrı ayrı hesaplanarak listelenebilir. Aşağıdaki SELECT komutu bu işlemi gerçekleştirmektedir.

```sql
SELECT bol_no,AVG(maas)
FROM Personel
GROUP BY bol_no;
```

SONUÇ:

```sql
bol_no AVG(maas)
```

−−−−−−−−−−−−− −−−−−−−−−−−−−−−

1 2500000

2 6800000

3 7400000

4 12500000

Her bölümdeki en yüksek maaşı alan kişiler listelenmek istenirse, aşağıdaki

komut kullanılabilir:

```sql
SELECT bol_no,MAX(maas),ad,soyad
FROM Personel
GROUP BY bol_no;
```

Personel tablosundaki bilgiler

| maas | ad | soyad | bol\_no |
| --- | --- | --- | --- |
| 5000000 | Ali | Can | 1 |
| 3000000 | Ayşe | Okan | 1 |
| 8000000 | Akın | Oran | 2 |
| 10000000 | Yeşim | Şensoy | 2 |

şeklinde ise, yukarıdaki SELECT komutunun çıktısı;

| bol\_no | Max\_maas | ad | soyad |
| --- | --- | --- | --- |
| 1 | 5000000 | Ali | Can |
| 2 | 10000000 | Yeşim | Şensoy |

şeklinde olacaktır.

Gruplandırarak, kümeleme fonksiyonlarını uygularken, koşul da verilebilir. Bu durumda, grup üzerindeki hesaplamalarla ilişkili koşul belirtirken, HAVING sözcüğü kullanmak gerekir. Aşağıdaki örnek soru, bu konuda fikir vermektedir.

**SORU:** En yüksek maaşın, 9000000’dan fazla olduğu bölümlerdeki personele ait ortalama maaşları listeleyiniz.

**ÇÖZÜM:**
```sql
SELECT bol_no,AVG(maas)
FROM Personel
GROUP BY bol_no
HAVING AVG(maas)>9000000;
```

Personel tablosunda aşağıdaki veri mevcut olsun:

| .......... | bol\_no | ......... | maas |
| --- | --- | --- | --- |
|  | 1 |  | 6000000 |
|  | 1 |  | 17000000 |
|  | 2 |  | 7500000 |
|  | 2 |  | 8000000 |
|  | 3 |  | 12000000 |
|  | 3 |  | 11000000 |
|  | 1 |  | 14000000 |
|  | 1 |  | 18000000 |

Yukarıdaki SELECT komutu sonucunda

| bol\_no | AVG\_maas |
| --- | --- |
| 1 | 13750000 |
| 3 | 11500000 |

tablosu elde edilecektir.

HAVING** **sözcüğü, SELECT komutunda GROUP BY sözcükleri bulunmadığı zaman, geçersizdir. HAVING sözcüğünü izleyen ifade içinde, SUM, COUNT (\*), AVG, MAX ya da MIN gibi kümeleme fonksiyonlarından en az biri bulunmalıdır.

WHERE sözcüğü bir tablonun tek tek satırları üzerinde işlem yapan koşullar için geçerli iken, HAVING sözcüğü sadece, gruplanmış veriler üzerindeki işlemlerde geçerlidir.

Bazı durumlarda, HAVING ve WHERE sözcükleri birlikte, SELECT komutu içinde kullanılabilir.

**SORU:** Personel tablosu içinde, her bölümde, erkek personele ait maaşlar için, ortalamanın 9000000’den fazla olduğu bölümleri listeleyiniz.

**ÇÖZÜM:**
```sql
SELECT bol_no,AVG(maas)
FROM Personel
WHERE cinsiyet=.T.
GROUP BY bol_no
HAVING AVG(maas)>9000000;
```

Personel tablosunda aşağıdaki bilgiler olsun:

| ........ | bol\_no | maas | cinsiyet | ......... |
| --- | --- | --- | --- | --- |
|  | 1 | 6000000 | .T. |  |
|  | 1 | 17000000 | .F. |  |
|  | 2 | 7500000 | .F. |  |
|  | 2 | 8000000 | .F. |  |
|  | 3 | 12000000 | .T. |  |
|  | 3 | 11000000 | .F. |  |
|  | 1 | 14000000 | .T. |  |
|  | 1 | 18000000 | .T. |  |

Yukarıdaki uygulanan SELECT komutu, her bölümdeki erkek personele ait ortalama maaşı hesaplayacak (erkek personel .T. ile belirtilmiştir) ve erkek personel maaş ortalaması, 9000000’den olan bölümler listelenecektir. Komutun çıktısı, aşağıdaki gibidir.

| bol\_no | AVG\_maas |
| --- | --- |
| 1 | 12666666.67 |
| 3 | 12000000 |

**BÖLÜM 4**

**BİRDEN FAZLA TABLOYU İLİŞKİLENDİREREK SORGULAMAK**

**4.1 Giriş**

** **Bu bölüme kadar, SQL ile, sadece tek tablo üzerinde sorgulamalar gerçekleştirilmiştir. Fakat işletme uygulamalarında ya da gerçek veri tabanı uygulamalarında, bu işin elemanter bir yönüdür. Daha sık karşılaşılan ve güç olan sorgulamalar, birden çok tablonun bir biri ile ilişkilendirilmesini gerektiren sorgulamalardır.

SQL’in sorgulama gücü daha ziyade bu tip sorgulamalarda ortaya çıkmaktadır.

**4.2 Birleştirme (Join) İşlemi**

Birleştirme işlemini anlayabilmek için, örnek veri tabanımızdaki, Personel ve Bölüm tablolarını göz önüne alalım.

Personel

Sicil NoSos. Güv. NoAdSoyadDoğum TarihiAdresCinsiyetMaaşBöl-NoYön. Sos. Güv. No

Bölüm

| bölüm\_ad | bölüm\_no | y\_sos\_g\_n | y\_is\_bas\_tar |
| --- | --- | --- | --- |

Bu tablolar ile ilişkili olarak soruyu soralım:

Çalışan her personel ve bu personelin yöneticisi ile ilişkili bilgiler nelerdir?

Belirli bir personel ile ilişkili bilgiler, personel tablosunun o personele ait satırında mevcuttur. Ancak personelin yöneticisi ile ilişkili bilgilerin bir kısmına ise bölüm tablosunda erişilebilir. Bu durum zorunlu olarak personel ile bölüm tabloları arasında ilişki kurulmasını gerektirir. Bu ilişki, ancak müşterek bir alan yardımı ile kurulabilir.

Müşterek alan, burada bölüm numarasıdır ve personel tablosunda bol\_no, bölüm tablosunda bölüm\_no adı ile yer almaktadır.

Müşterek alana göre, personel ve bölüm tablolarının birleştirilmesi (JOIN) demek, her iki tablodaki tüm sütunları içeren yeni bir tablo oluşturmak demektir. Yalnız bu tabloda sadece, her iki tabloda da mevcut olan bölüm numaraları ile ilişkili satırlar yer alacaktır.

Birleştirme (JOIN) işlemi ile listeleme aşağıdaki SQL komutu ile gerçekleştirilebilir.

```sql
SELECT *
FROM Personel,bölüm
WHERE Personel.bol_no=bölüm.bölüm_no;
```

ilişkilendirme, kolayca görüleceği gibi

```sql
WHERE Tabloadı.Kolonadı=Tabloadı.Kolonadı;
```

ifadesi ile sağlanmaktadır. Aşağıdaki örnek veri için bu JOIN işlemi sonucu Tablo 4.1’de görülmektedir. Örnek veri:

Personel

```sql
sicilsos_g_noadsoyaddog_taradrescinsiyetmaasbol_noyon_s_g_n11227641AliCan01/06/60Fatih.T.800000010371651753777654AyşeŞen04/07/65Kadıköy.F.70000001037165217176241AkınÖncel11/07/64Üsküdar.T.6000000227714351727615CanÖner05/08/65Fatih.T.4000000227714361857253BerilMeral08/07/62Pendik.F.37500002277143154044721AyşeCansu07/08/63Beşiktaş.F.48000003577211
```

Bölüm

| bölüm\_ad | bölüm\_no | y\_sos\_g\_n | y\_is\_b\_tar |
| --- | --- | --- | --- |
| Satış | 1 | 037165 | 01/07/89 |
| Muhasebe | 2 | 277143 | 01/08/91 |
| Üretim | 3 | 577211 | 04/06/92 |
| Eğitim | 4 | 443421 | 01/05/91 |
| Bilgi işlem | 5 | 288111 | 05/02/92 |

**Tablo 4.1 **Personel ve Bölüm Tablolarının, Müşterek Alan Olan Bölüm Numarası Üzerinde JOIN (Birleştirme) İşlemine Tabi Tutulması Sonucu Elde Edilen Bilgi.

```sql
sicilsos_g_noadsoyaddog_taradrescinsiyetmaasbol_noyon_s_g_nbölüm_adbölüm_ noy_sos_g_noy_is_b_tar11227641AliCan01/05/60Fatih.T.80000001037165Satış103716501/07/8917537654AyşeŞen04/07/65Kadıköy.F.70000001037165Satış103716501/07/89217176241AkınÖncel11/07/64Üsküdar.T.60000002277143Muhasebe227714302/08/9151727615CanÖner05/08/65Fatih.T.40000002277143Muhasebe227714302/08/9161857253BerilMeral08/07/62Pendik.F.37500002277143Muhasebe227714302/08/91154044721AyşeCansu07/08/63Beşiktaş.F.48000003577211Üretim357721104/06/92
```

Tablo 4.1’de görüleceği üzere, Personel ve bölüm tablolarında sadece her iki tabloda da aynı olan bölüm numaralarına ait satırlar alınarak birleştirilmiş ve listelenmiştir.

Listelenen birleştirilmiş tabloda, her iki tablodan da alındığı için tekrar eden bölüm numarası ve yönetici sosyal güvenlik numarası gibi sütun başlıklarının bir kez yazılması isteniyorsa, o takdirde SELECT komutunda \* sembolü yerine sadece, sonuçta yazılması istenen sütun başlıkları kullanılmalıdır:

Örneğin aşağıdaki SELECT komutu ile aşağıdaki tablodaki sonuçlar üretilecektir:

```sql
SELECT sicil,ad,soyad,bol_no,yon_s_g_no
FROM Personel,bölüm
WHERE Personel.bol_no=bölüm.bölüm_no;
```

**Tablo 4.2** Join İşleminde, Sadece Arzu Edilen Alanların Listelenmesi Sonucu Üretilen Bilgi.

| sicil | ad | soyad | bol\_no | yon\_s\_g\_no |
| --- | --- | --- | --- | --- |
| 112 | Ali | Can | 1 | 037165 |
| 175 | Ayşe | Şen | 1 | 037165 |
| 217 | Akın | Öncel | 2 | 277143 |
| 517 | Can | Öner | 2 | 277143 |
| 618 | Beril | Meral | 2 | 277143 |
| 1540 | Ayşe | Cansu | 3 | 577211 |

Personel ve bölüm tablolarından yararlanılarak aşağıdaki şekilde yazılacak bir SELECT komutu ise, ilgili sütun elemanları ile ilişkili kartezyen çarpımı işlemini gerçekleştirecektir.

```sql
SELECT sos_g_no,bölüm_ad
FROM Personel,bölüm;
```

**Tablo 4.3** Personel ve Bölüm Tabloları Üzerinde Kartezyen Çarpımı İşlemi.

| sosy\_g\_no | bölüm\_ad |
| --- | --- |
| 27615 | Satış |
| 27615 | Muhasebe |
| 27615 | Üretim |
| 27615 | Eğitim |
| 27615 | Bilgi işlem |
| 57253 | Satış |
| 57253 | Muhasebe |
| 57253 | Üretim |
| 57253 | Eğitim |
| 57253 | Bilgi işlem |
| ... | ... |
| ... | ... |
| ... | ... |
| ... | ... |
| 44721 | Satış |
| 44721 | Muhasebe |
| 44721 | Üretim |
| 44721 | Eğitim |
| 44721 | Bilgi işlem |

Burada Personel tablosundaki her sosyal güvenlik numarası, sıra ile, bölüm tablosundaki her bölüm adı ile eşlenerek listelenmiştir (6 personel ve 5 bölüm varsa, toplam 30 satır listelenecektir). Bu tür bir listelemenin pekçok durum için faydasız ve anlamsız olacağı açıktır.

**NOT: **A=(a,b,c,d) ve B=(x,y,z) kümelerinin kartezyen çarpımı

AxB=((a,x),(a,y),(a,z),(b,x),(b,y),(b,z),(c,x),(c,y),(c,z),(d,x),(d,y),(d,z))

şeklinde tanımlanır.

**4.3 Bir Tablonun Farklı İsimlerdeki Eşdeğerleri İle Sorgulama**

Daha önceden tanımlanmış bir tablonun, farklı isimli, bir eşdeğerini oluşturarak sorgulamalarda kullanmak mümkün olabilir. Örneğin, aşağıdaki sorgulamayı göz önüne alalım:

Her personel için, personel sicil numarası, ad ve soyadı ile bu personelin yöneticisinin ad, soyad ve doğum tarihini listeleyiniz: Bu isteğe cevap teşkil edebilecek SQL ifadelerinden bir tanesi, aşağıdaki gibi düzenlenebilir.

```sql
SELECT A.sicil,A.ad,A.soyad,B.ad,
B.soyad,B.dog_tar
FROM Personel A B
WHERE A.yon_s_g_n=B.sosy_g_no ;
```

Personel tablosu aşağıdaki gibi olsun:

| sicil | sosy\_g\_no | ad | soyad | dog\_tar | yon\_s\_g\_n |
| --- | --- | --- | --- | --- | --- |
| 117 | 276543 | Ali | Can | 01/05/67 | 37265 |
| 247 | 372651 | Can | Okan | 01/06/60 | 555115 |
| 348 | 572416 | Ayşe | Akın | 01/05/70 | 372651 |
| 447 | 443211 | Beril | Caner | 02/04/65 | 555115 |
| 542 | 555115 | Akın | Öner | 02/07/54 | 771727 |
| ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

Yukarıdaki SELECT komutunun çıktısı aşağıdaki tabloda verilmiştir.

**Tablo 4.4** Eşdeğer Tablo Yardımı İle Sorgulama Sonucu.

| sicil | ad\_a | soyad\_a | ad\_b | soyad\_b | dog\_tar |
| --- | --- | --- | --- | --- | --- |
| 117 | Ali | Can | Can | Okan | 01/06/60 |
| 348 | Ayşe | Akın | Can | Okan | 01/06/60 |
| 247 | Can | Okan | Akın | Öner | 02/07/54 |
| 447 | Beril | Caner | Akın | Öner | 02/07/54 |

Bu SELECT komutu ile, personel tablosunun A ve B isimli birer kopyası oluşturulur. Bu kopyalara personel kütüğünün eşdeğerleri ya da takma adlıları (aliases) adı verilir. SELECT komutu, personel tablosunun eşdeğeri olan ve yönetilenleri temsil eden B tablosundaki sosyal güvenlik numarasına eşit olan satırları kontrol ederek her personelin sicil no, ad, soyad bilgilerini ve bu personelin yöneticisinin ad, soyad ve doğum tarihini listeler (yukarıdaki tabloda verilmiştir). Buradaki yöntem ile bir tablonun kendisi ile birleştirilmesi işlemi kendi üzerinde birleştirme (self-join) adını almaktadır. Bazı SQL gerçekleştirimlerinde, bu SELECT komutunun,

```sql
SELECT A.sicil,A.ad,A.soyad,B.ad,B.soyad,B.dog_tar
FROM Personel A,Personel B
WHERE A.yon_s_g_n=B.sosy_g_no;
```

şeklinde yazılması gerekir.

Aşağıdaki örnek soru için, eşdeğer tablo oluşturma özelliğinden yararlanarak, benzer şekilde SELECT komutu düzenleyebiliriz:

**SORU:** Satış bölümünde çalışan tüm personelin ad, soyad ve adreslerini listeleyiniz.

**ÇÖZÜM: **
```sql
SELECT a.ad,a.soyad,a.adres
FROM Personel a,Personel b
WHERE b.bölüm_ad=”Satış” AND
a.bol_no=b.bölüm_no;
```

şeklinde olacak ve tablo aşağıdaki gibi olacaktır.

Personel tablosu

| sicil | ad | soyad | adres | bol\_no |
| --- | --- | --- | --- | --- |
| 117 | Ali | Can | Fatih | 1 |
| 247 | Selin | Akın | Bakırköy | 2 |
| 348 | Can | Seler | Üsküdar | 1 |
| 547 | Beril | Caner | Pendik | 1 |
| 648 | Akın | Çalışır | Kadıköy | 4 |

Bölüm tablosu

| bölüm\_ad | bölüm\_no | y\_sos\_g\_n | y\_is\_b\_tar |
| --- | --- | --- | --- |
| Satış | 1 | 276241 | 01/05/87 |
| Muhasebe | 2 | 372615 | 02/04/90 |
| Bilgi işlem | 3 | 44272 | 04/08/91 |

şeklinde ise Tablo 4.5’teki sonuç elde edilecektir.

**Tablo 4.5** Satış Bölümündekilerin Eşdeğer Tablo Oluşturma Yöntemi İle Listelenmesi Sonucu.

| ad | soyad | adres |
| --- | --- | --- |
| Ali | Can | Fatih |
| Can | Seler | Üsküdar |
| Beril | Caner | Pendik |

**4.4 İç İçe Select Komutları (Nested Selects)**

** **Bazı sorgulamalar, özelliği itibarı ile iç içe SELECT komutlarının kullanılmasını gerektirebilir. İçteki SELECT komutunun bulduğu sonuç, dıştaki SELECT komutunun işlevini yerine getirmesi için kullanılır. Örnek olarak, aşağıdaki soruyu göz önüne alalım:

**SORU:** Parça numarası 24 olan parçayı kullanan projelerde çalışan personeli listeleyiniz.

Örnek olarak aşağıdaki verileri göz önüne alalım:

Parça

| par\_no | par\_ad | pr\_no | fiyat | ağırlık |
| --- | --- | --- | --- | --- |
| 24 | Vida | 2 | 2000 | 500 |
| 24 | Vida | 4 | 2000 | 500 |
| 37 | Civata | 2 | 6000 | 800 |
| 87 | Conta | 2 | 7000 | 5000 |
| 112 | Pim | 5 | 6000 | 70 |

```sql
Proje
```

| proje\_ad | proj\_no | yer | bl\_no |
| --- | --- | --- | --- |
| 1 | 1 | İstanbul | 4 |
| 2 | 2 | İstanbul | 4 |
| 3 | 3 | Ankara | 5 |
| 4 | 4 | Ankara | 5 |
| 5 | 5 | İzmir | 4 |

Personel

| sicil | sosy\_g\_no | ad | soyad | dog\_tar | bol\_no | adres |
| --- | --- | --- | --- | --- | --- | --- |
| 117 | 274251 | Ali | Can | 05/01/60 | 4 | Akar sok. 2 Fatih |
| 247 | 527241 | Hasan | Okan | 04/07/62 | 4 | Merk cad. 3 Pendik |
| 348 | 5276672 | Ayşe | Pekcan | 04/08/65 | 5 | ...... |
| 548 | 443211 | Akın | Pekol | 07/02/70 | 4 | ...... |
| 1148 | 52625 | Mert | Caner | 04/08/70 | 5 | ....... |

Çalışma

| per\_s\_g\_no | proje\_no | saat |
| --- | --- | --- |
| 274251 | 1 | 250 |
| 527241 | 2 | 350 |
| 527672 | 3 | 400 |
| 443211 | 5 | 300 |
| 527625 | 4 | 250 |

Bu tablolardan yararlanarak aşağıdaki SELECT komutları ile arzu edilen işlem gerçekleştirilebilir:

```sql
SELECT *
FORM Personel
WHERE sosy_g_no
IN (SELECT Per_s_g_no
FROM Parça,Proje,Çalışma
WHERE pr_no=proj_no AND
proj_no=proje_no AND parça_no=24);
```

Buradaki içteki SELECT komutu parça, proje ve çalışma tablolarını proje numaraları üzerinde (proje numaraları bu tablolarda sıra ile pr\_no, proj\_no ve proje\_no adı ile yer almaktadır) birleştirerek elde edilen genişletilmiş tablodan sadece parça no’su 24 olan satırdaki personel sosyal güvenlik numaralarını (pers\_s\_g\_no) çıkarmakta ve sonuçta yukarıdaki örnek data için

| per\_s\_g\_no |
| --- |
| 527241 |
| 527625 |

değerlerini elde etmektedir.

Dış SELECT komutu ise, personel tablosundan bu sosyal güvenlik numaralarına sahip personel aşağıdaki tabloda görüldüğü gibi listelenecektir:

| sicil | sosy\_g\_no | ad | soyad | dog\_tar | bol\_no |
| --- | --- | --- | --- | --- | --- |
| 247 | 527241 | Hasan | Okan | 04/07/62 | 4 |
| 1148 | 527625 | Mert | Caner | 04/08/70 | 5 |

Benzer şekilde aşağıdaki sorunun çözümü de iç içe SELECT komutları ile gerçekleştirilebilir.

**SORU:** Fatih’te oturan personelin çalıştığı projelerin adları ve yerlerini listeleyiniz.

**ÇÖZÜM:**
```sql
SELECT proje_ad,yer
FROM Proje
WHERE proj_no IN(SELECT proje_no
FROM Personel,Çalışma
WHERE sosy_g_no=Per_s_g_no
AND adres LIKE ‘%Fatih%’);
```

SONUÇ:

| proj\_ad | yer |
| --- | --- |
| 1 | İstanbul |
| 3 | Ankara |

çıktısı elde edilecektir.

**4.5 UNION Sözcüğü**

UNION sözcüğü küme birleşimi işlemi görür. İki ayrı SELECT komutunun sonucunda elde edilen tabloların birleşimi işlemini gerçekleştirir. Aşağıdaki soru ve cevabı olan SELECT komutları bu konuda bir fikir vermektedir.

**SORU:** Adı Ahmet ve soyadı Caner olan kişi ya da kişileri, işletmenin yürüttüğü projelerde çalışan bir kişi (sıradan bir personel ya da bölüm yöneticisi) olarak bulunduran projelerin isimlerini ve projelerin yürütüldüğü yerleri listeleyiniz.

**ÇÖZÜM:**
```sql
(SELECT proj_no,yer
FROM Proje,bölüm,Personel
WHERE bl_no=böülm_no AND
y_sos_g_no=sosy_g_no AND
```

ad=”Ahmet” AND soyad=”Caner”)

```sql
UNION (SELECT proj_ad,yer
FROM Proje,Çalışma,Personel
WHERE proj_no=proje_no AND
per_s_g_no=sosy_g_no AND ad=”Ahmet” AND soyad=”Caner”);
```

UNION sözcüğü ile, iki ya da daha çok SELECT ‘in sonucu olan tabloların küme birleşimi işlemine tabi tutulması için iki koşul gereklidir.,

1-) SELECT komutları sonucunda elde edilecek tablolar aynı sayıda kolon içermelidirler.

```sql
1. SELECT 2. SELECT
```

Sonuç Tablosu Sonuç Tablosu

5 Kolon 5 Kolon

2-) Sonuç tabloların karşılıklı olarak kolonları ayrı veri tipi ve aynı genişlikte olmalıdır.

**4.6 ANY Sözcüğü**

** **Aşağıdaki örnek soru çerçevesinde bu sözcüğün SELECT komutu içindeki etkisini açıklayacağız.

**SORU:** Satış bölümünde çalışan personelin her hangi birinden daha düşük maaş alan ve mühendislik bölümünde çalışan kişileri listeleyiniz.

**ÇÖZÜM: **
```sql
SELECT *
FROM Personel
WHERE maas<ANY
( SELECT maas
FROM Personel
WHERE bol_no=2 ) AND
bol_no=1;
```

Bu çözümün eşdeğeri olan ifade ise şöyledir.

```sql
SELECT *
FROM Personel
WHERE maas<(SELECT MAX (maas)
FROM Personel
WHERE bol_no=2) AND bol_no=1;
```

Burada satış bölümü kodu 2 ve mühendislik bölümü kodu ise 1 olarak kabul edilmiştir. İkinci çözüm ifadesinden de kolayca anlaşılacağı gibi, iç içe SELECT ifadesinde, içteki SELECT sorgulaması sonucu, ikinci bölümde (Satış) çalışan personelin içinde en yüksek maaş alan kişinin maaşı bulunmakta, dıştaki SELECT ise, mühendislik bölümünde, bu maaştan düşük olan maaşa sahip kişileri listelemektedir.

Buradaki düşünce tarzı şöyledir:

Mühendislik bölümünde çalışan ve satış bölümündeki en yüksek maaştan düşük maaş alan kişi “SATIŞ BÖLÜMÜNDEKİ HER HANGİ BİR MAAŞ’TAN DÜŞÜK OLMA” koşulunu sağlayacaktır. Eğer mühendislik bölümündeki kişinin maaşı, satış bölümündeki en yüksek maaştan daha yüksek olsa (veya ona eşit olsa) doğal olarak bu koşul sağlanmayacaktı.

Personel tablosu aşağıdaki verileri içeriyorsa,

Personel

| sicil | ad | soyad | bol\_no | maas | ....... |
| --- | --- | --- | --- | --- | --- |
| 117 | Ali | Can | 1 | 7000000 | ....... |
| 247 | Hasan | Okan | 1 | 6000000 | ....... |
| 348 | Ayşe | Pekcan | 2 | 50000000 | ....... |
| 548 | Akın | Pekol | 1 | 4000000 | ....... |
| 1148 | Mert | Caner | 2 | 12000000 | ....... |
| 1215 | Beril | Şen | 2 | 5000000 | ....... |

Yukarıdaki SELECT komutları sonucu (ANY ile ya da eşdeğeri ile)

| sicil | ad | soyad | bol\_no | maas | ....... |
| --- | --- | --- | --- | --- | --- |
| 117 | Ali | Can | 1 | 7000000 | ....... |
| 247 | Hasan | Okan | 1 | 6000000 | ....... |
| 548 | Akın | Pekol | 1 | 4000000 | ....... |

tablosu elde edilecektir.

ANY (her hangi bir) sözcüğü yerine, tamamen eşdeğeri olan SOME sözcüğü de kullanılabilir.

**4.7 ALL Sözcüğü**

“Hepsi, tamamı” anlamındaki bu sözcük, SELECT komutu içerisinde belirli bir koşulu sağlayan bir grup datanın tamamınca sağlanan koşullarla ilişkili olarak kullanılır. Aşağıdaki soru konuda açıklayıcı olacaktır:

**SORU:** Satış bölümünde çalışan ve mühendislik bölümündeki personelin hepsinden daha fazla maaş alan personeli listeleyiniz. Bu örnekte de satış bölümü kodu 2 ve mühendislik bölümü kodu 1 olarak alınırsa aşağıdaki SELECT grupları çözüm teşkil edecektir.

**ÇÖZÜM:**

```sql
1. Alternatif 2. Alternatif
SELECT * SELECT *
FROM Personel FROM Personel
WHERE maas>ALL(SELECT maas WHERE maas>(SELECT MAX(maas)
FORM Personel FROM Personel
WHERE bol_no=1) WHERE bol_no=1)
AND bol_no=2; AND bol_no=2;
```

Personel tablosu aşağıdaki verileri içeriyorsa

Personel

| sicil | ad | soyad | bol\_no | maas |
| --- | --- | --- | --- | --- |
| 117 | Ali | Can | 1 | 7000000 |
| 247 | Hasan | Okan | 1 | 6000000 |
| 348 | Ayşe | Pekcan | 2 | 50000000 |
| 548 | Akın | Pekol | 1 | 4000000 |
| 1148 | Mert | Caner | 2 | 12000000 |
| 1215 | Beril | Şen | 2 | 5000000 |

Yukarıdaki 1. Alternatif ve 2. Alternatif olarak belirtilen, her iki SELECT komutları grubu da aşağıdaki sonucu verecektir.

SONUÇ:

| sicil | ad | soyad | bol\_no | maas |
| --- | --- | --- | --- | --- |
| 348 | Ayşe | Pekcan | 2 | 5000000 |
| 1148 | Mert | Caner | 2 | 12000000 |

**4.8 EXISTS Operatörü**

“Var, mevcuttur” anlamındaki bu sözcük, SQL’de boolean (lojik, mantıksal) operatördür. İçteki SELECT komutunun sorgulanması sonucunda, en az bir tablo satırı üretilmişse EXISTS operatörü TRUE (doğru) değerini, hiçbir tablo satırı üretilmemişse, EXISTS operatörü FALSE (yanlış) değerini üretir.

EXISTS operatörü, AND, OR ve NOT gibi diğer mantıksal operatörlerle birlikte kullanılabilir. Aşağıdaki soru ve çözümü bu mantıksal operatörle ilişkili bir fikir vermektedir:

**SORU:** Numarası 27 olan parçayı satan satıcılarla ilişkili tüm bilgileri listeleyiniz.

Gerekli SELECT komularını yazabilmek için, sistemde satıcı adlı tabloda ve par\_sat (parça ve satıcısı ile ilişkili bilgileri içeriyor) adlı tabloda aşağıdaki kolon ve verilerin bulunduğunu varsayalım:

Satıcı Par\_sat

| satıcı\_n | adı | adres |  | sat\_no | parca\_n | miktar |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ali Akın | İstanbul |  | 1 | 1 | 200 |
| 2 | Ayşe Can | İstanbul |  | 1 | 27 | 300 |
| 3 | Akın Peker | Ankara |  | 2 | 27 | 250 |
| 4 | Can Ozan | İzmir |  | 2 | 42 | 115 |
| 5 | Mert Ak | Antalya |  | 3 | 1 | 500 |
|  |  |  |  | 3 | 2 | 56 |
|  |  |  |  | 4 | 15 | 800 |
|  |  |  |  | 5 | 18 | 900 |

**ÇÖZÜM:**
```sql
SELECT *
FROM Satıcı
WHERE EXISTS (SELECT *
FROM Par_sat
WHERE sat_no=satıcı_n AND parca_n=27);
```

Aşağıdaki sonuç elde edilir:

| satıcı\_n | adı | adres |
| --- | --- | --- |
| 1 | Ali Akın | İstanbul |
| 2 | Ayşe Can | İstanbul |

Yukarıda da belirtildiği gibi, iç SELECT’te WHERE’i izleyen koşulu sağlayan satırlar, Par\_sat içinde bulundukça (mevcut iseler), EXISTS operatörü TRUE (doğru) değeri verecek bu durumda dış SELECT’in WHERE koşul kısmı doğru olacağı için, o satıcı ile ilişkili bilgiler, satıcı tablosunda listelenecektir.

**4.9 NOT EXISTS İfadesi**

EXISTS’te belirtildiği gibi, EXISTS mantıksal operatörü, NOT, AND ve OR mantıksal operatörleri ile birlikte de kullanılır.

NOT EXISTS şeklinde kullanılması, EXISTS’te açıklanan yapının tamamen tersi bir etki yaratır; yani SELECT komutunun sorgulanması sonucu koşulu sağlayan hiçbir tablo satırı** **bulunamazsa, dıştaki SELECT için WHERE’i izleyen koşul kısmı TRUE (doğru) olarak kabul edilir ve SELECT icra edilir.

**SORU:** Numarası 27 olan parçayı satmayan satıcılar kimlerdir? (EXISTS operatöründe kullanılan Satıcı ve Par\_sat tablolarındaki verilerin aynen geçerli olduğunu varsayalım)

**ÇÖZÜM:**
```sql
SELECT *
FROM Satıcı
WHERE NOT EXISTS (SELECT *
FROM Par_sat
WHERE sat_no=satıcı_n
AND parca_n=27);
```

SONUÇ:

| satıcı\_n | adı | adres |
| --- | --- | --- |
| 3 | Akın Peker | Ankara |
| 4 | Can Ozan | İzmir |
| 5 | Mert Ak | Antalya |

NOT EXISTS ifadesinin kullanımı ile ilişkili olarak diğer bir örnek de aşağıdaki soru ile ilişkili olarak verilmiştir:

**SORU:** İşeltmenin yönettiği projelerde kullanılan parçalardan, tümünü de bulunduran ve İstanbul’da faaliyet gösteren satıcılarla ilişkili bütün bilgileri listeleyiniz.

**ÇÖZÜM:**
```sql
SELECT *
FROM Satıcı
WHERE NOT EXISTS (SELECT *
FROM Parça
WHERE NOT EXISTS
(SELECT *
FROM Par_sat
WHERE sat_no=satıcı_n AND
parca_n=par_no ))
AND ADRES LIKE ‘%İstanbul%’;
```

Bu ifade şu şekilde yorumlanabilir.

İstanbul’daki satıcılar içinde, satmadıkları bir parça mevcut olmayan satıcıları listele!

**4.10 Select Komutu İçinde Except Sözcüğü**

EXCEPT sözcüğü, iki tablo arasında küme farkı (difference) işlemini gerçekleştirir. Tablo 1 ve Tablo 2 aşağıdaki gibi olsun.

Tablo 1 Tablo 2

| Sütun 1 |  | Sütun1 |
| --- | --- | --- |
| a |  | a |
| b |  | b |
| c |  | c |
| d |  |  |

```sql
Tablo 1 EXCEPT
```

Tablo 2

Tablo 1 ile Tablo 2’de yukarıdaki işleme göre (Tablo 1 EXCEPT,Tablo2) işlem sonucu elde edilecek tabloda, Tablo 1’de bulunup Tablo 2’de bulunmayan veriler mevcut olacaktır. Bu işlem SQL’de

Tablo 1 EXCEPT Tablo 2 şeklinde ifade edilir ve sonuçta elde edilen fark tablosu aşağıdadır:

```sql
Tablo 1 EXCEPT Tablo 2
```

| Sütun 1 |
| --- |
| d |

Aşağıdaki soru ve çözümü bu sözcüğün kullanımı konusunda daha iyi fikir verecektir:

**SORU:** Satış bölümündeki personel adlarından, mühendislik bölümünde bulunmayanları listeleyiniz:

(Satış için bol\_no 1, mühendislik için bol\_no 2 olduğunu varsayalım.)

**ÇÖZÜM:**
```sql
SELECT * FROM
(SELECT ad FROM Personel
WHERE bol_no=1
EXCEPT
SELECT ad FROM Personel
WHERE bol_no=2);
```

**4.11 Select Komutu İçinde Intersect Sözcüğü**

İki tablo arasında küme kesişimi (intersection) işlemini gerçekleştirir.

Tablo 1 Tablo 2

| Sütun 1 |  | Sütun1 |
| --- | --- | --- |
| x |  | p |
| y |  | q |
| z |  | x |
|  |  | y |

şeklinde ise;

```sql
TABLO 1 INTERSECT TABLO 2 işlemi sonucunda
```

| Sütun 1 |
| --- |
| x |
| y |

tablosu elde edilecektir. (Küme kesişimi işleminde, her iki kümede mevcut olan müşterek elemanlar alınır.)

**SORU:** Hem Ankara’daki hem de İstanbul’daki projelerde görev alan bölümleri listeleyiniz.

**ÇÖZÜM:**
```sql
SELECT * FROM
(SELECT bl_no FROM Proje
WHERE yer LIKE ‘%Ankara%’
INTERSECT
SELECT bl_no FROM Proje
WHERE yer LIKE ‘%İstanbul%’);
```

Proje tablosundaki bilgi aşağıdaki gibi olsun:

| proj\_ad | proj\_no | yer | bl\_no |
| --- | --- | --- | --- |
| otoyol-1 | 2 | Ankara-Türkiye | 1 |
| ekspers-2 | 4 | İstanbul-Türkiye | 1 |
| subway-2 | 16 | Bakü-Azerbeycan | 2 |
| otoyol-16 | 17 | Ankara-Türkiye | 4 |
| köprü-5 | 21 | İstanbul-Türkiye | 4 |
| köprü-17 | 13 | Roma-İtalya | 1 |
| geçit-5 | 18 | İstanbul-Türkiye | 7 |

Yukarıdaki SELECT komutu sonucunda bulunan tablolar ile son adımda

| bl\_no |  | bl\_no |
| --- | --- | --- |
| 1 |  | 1 |
| 4 |  | 4 |
|  |  | 7 |

işlemi sonucunda

| bl\_no |
| --- |
| 1 |
| 4 |

tablosu elde edilecektir.

**4.12 Bir Select Komutunun Sonucunu Ayrı Bir Tablo Olarak Saklamak**

Bir SELECT komutunun sonucu olarak elde edilecek bilgileri, geçici bir tablo olarak saklamak mümkündür. Bunu gerçekleştirebilmek için, SELECT komutunun sonuna SAVE TO TEMP Tabloadı şeklinde bir ifade eklemek gerekmektedir.

**SORU:** Bayan personeli Bayan adlı bir tablo içinde saklayınız.

**ÇÖZÜM:**
```sql
SELECT *
FROM Personel
WHERE cinsiyet=.F. SAVE TO TEMP Bayan;
```

cinsiyeti belirleyen cinsiyet alanında .F. simgesinin bayanları temsil ettiği varsayımı ile, personel adlı tablodaki bayan personel bayan adlı tabloya geçici olarak saklanacaktır.

Bayan adlı tabloya, SELECT komutu, bütün şekilleri ile uygulanabilir. Örneğin, bayanlar içinde maaşı 10000000 TL’den fazla olanlar listelenmek istenirse

```sql
SELECT *
FROM Bayan
WHERE maas>10000000;
```

ifadesi kullanılır.

Burada üretilen tablonun geçici değil kalıcı olması istenirse KEEP sözcüğü eklenmelidir:

```sql
SELECT *
FROM Personel
WHERE cinsiyet=.F.
SAVE TO TEMP Bayan KEEP;
```

**BÖLÜM 5**

**VIEW (BAKIŞ) OLUŞTURMAK**

**5.1 Temel Tablo (Base Table) ve Bakış (View) Kavramı**

** **Bu bölüme kadar oluşturulan ve kullanılan tablolar, veri tabanı ya da SQL açısından temel tablolar (base tables) adını alırlar. Bu tablolar fiziksel olarak veri tabanı ortamında mevcut olan tablolardır.

Veri tabanı kavramı içinde teorik olarak mevcut olan view (bakış) terimi, farklı kullanıcıların veri tabanına nasıl baktıklarını ya da bakış açılarını anlatan bir terimdir. Bu anlamda bir kullanıcı, fiziksel olarak mevcut olan tabloların sadece bir kısmı ile ilgilenebilir.

Temel tabloların tamamı ya da bir kısmı kullanılarak elde edilen ve fiziksel olarak veri tabanında mevcut olmayan sadece nasıl elde edilebileceğine dair bilginin saklandığı tablolara bakış (view) adı verilir. Bunlar için virtüel tablo terimide kullanılır.

SQL, bu tip tabloların oluşturulma ve kullanılmasına da olanak sağlayan komutlara sahiptir.

Şekil 5.1’de kavramsal olarak bir view’in nasıl oluşturulacağı gösterilmektedir.

**Şekil 5.1 **Kullanıcılar, Temel Tablolar ve View Oluşturma.

Örneğin, 1. Kullanıcı, Personel adlı tablonun sadece bayan personeli ile ilgilenmektedir. Bu nedenle, X adlı, sadece bayan personeli içeren bir view tablosu, personel adlı temel tablodan elde edilebilir.

2. Kullanıcı ise, örneğin 3. Bölümün yönettiği projelerde çalışan personel listesi ile ilgilenmektedir. O nedenle personel, proje ve bölüm adlı temel tabloları kullanarak, Y adlı bir view oluşturulabilir.

View oluşturmanın, veri tabanı ortamında aşağıda belirtilen faydaları vardır.

**5.2 View Oluşturmanın Yararları**

**5.2.1 Veri güvenliği**

** **Veri tabanı içinde bulunan tablolardakibazı sütunlarda bulunan bilgilerin, herkes tarafından görülmesi istenmeyebilir.

Örneğin, personelin maaşlarının herkes tarafından listelenebilir olması mahsurlu olabilir. Bu durumda, Personel adlı temel (base) tablodan, persview adlı bir view oluşturulabilir.

```sql
CREATE VIEW persview
AS SELECT sicil,sos_g_no,ad,soyad,dog_tar,adres,cinsiyet,bol_no,yon_s_g_n
FROM Personel;
```

persview adlı view, herkesin kullanımına açık, Personel adlı temel (base) tablo ise, yetkili kişiler dışındakilere, erişilemez hale getirilirse, maaşların herkes tarafından erişilebilir bilgi olması önlenmiş olur.

Bir view’den bilgi listelenmesi temel tablodan bilgi listelenmesinden farklı değildir.

```sql
SELECT *
FROM persview;
```

persview’den maaşlar hariç, tüm personel bilgileri listelenecektir.

Bir temel tablodan bir view oluşturulurken, temel tablodaki aynı sütun (alan) isimlerini kullanmak zorunda değildir. Örneğin, Parça adlı ve par\_no, par\_ad, pr\_no, fiyat ve ağırlık adlı sütun (alan) isimlerini içeren tablo kullanılarak oluşturulan parview içinde, par\_no yerine parc\_no, fiyat yerine fiy ve ağırlık yerine ağır isimleri kullanılmıştır:

```sql
CREATE VIEW
Parview(parc_no,fiy,ağır)
AS SELECT par_no,fiyat,ağırlık
FROM Parça;
```

**5.2.2 Sorgulamanın daha basit hale gelmesi**

Karmaşık sorgulamalarda, bazı SELECT komutlarının sonuçları diğer SELECT komutlarınca kullanıldığında, sorgulamanın düzenlenmesinde yanlışlıklar yapma olasılığı artar.

Karmaşık sorgulamalar, VIEW özelliği kullanılarak daha basit hale getirilebilir. Burada temel fikir şudur: Madem ki bir view, bir sorgulama sonucu elde edilen bilgiyi (tabloyu) isimlendirerek elde edilen bir virtüel tablodur; o halde karmaşık SELECT komutu içinde, sonucu kullanılacak başka bir SELECT komutu kullanmak yerine, bu sonucu bir view olarak isimlendirerek, view adını kullanmak. Bazı durumlarda ise, işletmenin veri tabanı uygulamasında çok sık olarak sorulan karmaşık soruları bir view yapısı içinde saklayarak, daha sonra aynı tip sorgulamalar için bu view yapısını kullanarak daha basit ifadeler kullanmakta olasıdır.

**SORU:** Satış bölümünde çalışan personelin herhangi birinden daha düşük maaş alan ve mühendislik bölümünde çalışan kişileri listeleyiniz.

**ÇÖZÜM:**
```sql
SELECT *
FROM Personel
WHERE maas<ANY(SELECT maas
FROM Personel
WHERE bol_no=2) AND
bol_no=1;
```

(Satış bölümü kodu 2 ve mühendislik bölümü kodu ise 1 kabul ediliyor.)

Şimdi bu sorunun cevabı olan tablo bir view olarak saklanırsa:

```sql
CREATE VIEW S1view
AS SELECT *
FROM Personel
WHERE maas<ANY(SELECT maas
FROM Personel
WHERE bol_no=2) AND
bol_no=1;
```

bundan sonra aynı tip sorgulama için sadece

```sql
SELECT *
FROM S1view;
```

yazmak yeterli olcaktır.

**5.2.3 Sadece view kullanılarak gerçekleşebilen sorgulamalar**

Bir tablodan elde edilecek bilgiler için, iki kademeli işlem gerektiren sorgulamalarda, ilk adımda bir view oluşturup ikinci adımda esas sorgulamayı bu view yardımı ile gerçekleştirmek, çoğu kez kaçınılmaz bir durumdur.

Aşağıdaki soru ve bunun çözümü olan SQL ifadeleri bu konuda bir fikir verecektir:

**SORU:** Her bölümde, o bölümdeki ortalama maaştan daha yüksek maaş alanları listeleyiniz.

**ÇÖZÜM:** Bu sorunun cevaplandırılması için önce her bölümdeki ortalama maaşların bulunması gereklidir.

```sql
CREATE VIEW BOL_OR_VIEW(bol_no,ort,maas)
AS SELECT bol_no,AVG(maas)
FROM Personel
GROUP BY bol_no;
```

Daha sonra, yaratılan BOL\_OR\_VIEW yardımı ile (bu view, bölüm no’ları ve bölüm ortalama maaşlarını saklamaktadır) sorulan sorunun cevabı elde edilebilir:

```sql
SELECT *
FROM Personel
WHERE bol_no=BOL_OR_VIEW.bol_no
. AND.maas>ort_maas;
```

(Bu sorunun cevabını, şu ana kadar anlatılan diğer bilgilerle bulmaya çalışınız.)

**5.2.4 Veri bütünlüğünün sağlanması**

View oluşturma esnasında CHECK sözcüğünün kullanılması ile, o view’i oluştururken sağlanması gereken koşulların, daha sonra view içine veri ekleme ya da değişiklik işlemlerinde de ihmal edilmesi engellenmiş olur.

Örneğin aşağıdaki gibi bir VIEW oluşturulsun:

```sql
CREATE VIEW UST_PER_VIEW
AS SELECT FROM Personel
WHERE maas>25000000,
WITH CHECK OPTION;
```

Burada,maaşı 25000000’un üstünde olan personelden oluşan bir UST\_PEVIEW adlı view oluşturulmuştur. Daha sonra bu view içine

```sql
INSERT INTO UST_PER_VIEW
VALUES(27521,’27865427’,’Ayşe’
‘Okan’,{01/05/62},’Cumh. Cad. 46-Taksim’,
.F.,13000000,1,’27651112’);
```

komutu ile maaşı 13000000 olan bir personel eklenmek istendiği zaman şu hata mesajı alınacaktır.

```sql
Error: not enough non-null values
```

Eğer CHECK opsiyonu kullanılmasaydı hata mesajı alınmadan bu veri view içine yüklenecekti. Bir tablo ya da view üzerinde veri ekleme, güncelleme ve silme işlemleri bir sonraki bölümde incelenecektir.

**BÖLÜM 6**

**TABLOLARDA DEĞİŞİKLİK YAPMAK**

**6.1 Tabloya Veri Ekleme**

SQL’de, mevcut bir tabloya veri eklemek için kullanılacak olan komut INSERT komutudur.

Standart SQL’de, oluşturulan bir tabloya veri yüklemek için tek imkan INSERT komutudur. INSERT komutu ile, tabloya, belli bir anda, tek bir satır eklemek imkanı vardır. INSERT komutunun yazılış biçimi aşağıdaki gibidir.

```sql
INSERT INTO Tabloadı
(Sütunadı1,Sütunadı2,........,Sütunadı n)
VALUES (değer1,değer2,....,değer n);
```

Örneğin, Personel tablosuna, sicil no’su 275 olan personel ile ilişkili bilgiler aşağıdaki gibi bir INSERT komutu ile yüklenebilir:

```sql
INSERT INTO Personel(sicil,sosy_g_no,ad,soyad,
dog_tar,adres,cins,maas,bol_no,yon_s_g_n)
VALUES (‘275’,’27652418’,’Ali’,’Caner’,{01/05/62},’Fatih-İstanbul’,.T.,27000000,2,’876215342’);
```

Karakter türü verilerin ‘ ‘ sembolleri arasında yüklendiğine diğer veriler içinse buna gerek olmadığına dikkat ediniz. Burada, tabloya tüm kolonlarla ilgili veri yüklendiği için, istenirse kolon isimleri ihmal edilebilir.

Standart SQL’deki INSERT komutunun, belli bir anda, tabloya, tek bir satırı yüklemesine karşılık, birçok SQL gerçekleştiriminde, yığın halinde veri yükleyen hizmet programlarından (utility) faydalanmak imkanı da vardır.

Ayrıca, INSERT komutunun bu şekli ile tabloya veri yüklemek pratikte tercih edilebilecek bir şekil değildir. (Her tablo satırı için bir INSERT komutu kullanılıyor.) Daha kullanışlı olan yol,verilerin kullanıcının zorlanmayacağı bir ekran düzeni ile klavyeden yüklenmesi daha sonra bunların INSERT ile tabloya yerleştirilmesidir.

SQL’de ekrandan interactive bilgi girişi ve ekran tasarımı sağlayacak komutlar yoktur. Fakat SQL’in bir veri tabanı yönetim yazılımının (dbase, Foxpro, Oracle) ya da daha üst düzey dilinin (C, Pascal, Cobol v.b) interactive bilgi girişine uygun komutları kullanarak bu işlemi arzu edilen kalitede gerçekleştirmesi mümkündür. SQL’in diğer dillerle etkileşimi bir sonraki bölümde incelenmiştir.

**6.2 Tablo Satırlarını Silme**

Bir tablonun satırlarını silmek için gerekli komut DELETE komutudur. Satır silme koşullu ya da koşulsuz olarak gerçekleştirilebilir.

```sql
DELETE FROM Tabloadı;
```

**ÖRNEK:**
```sql
DELETE FROM Personel;
25 Rows Deleted
```

Bu komut ile Personel tablosundaki tüm satırlar silinecektir. 25 Rows Deleted mesajı ile, o anda tabloda bulunan 25 satırın silindiği bildirilmektedir.

Koşula bağlı olarak satır silmeyi gerçekleştirmek için, DELETE komutuna WHERE sözcüğü eklenmeli ve bunu izleyen ifade koşulu göstermelidir.

**ÖRNEK:**
```sql
DELETED FROM Personel
WHERE bol_no=2;
5 Rows Deleted
```

Bu komut ile, 2 numaralı bölümdeki personelin tümü tablodan silinecektir. 5 Rows** **Deleted mesajı ile de, o anda 2 numaralı bölümde çalışan 5 personele ait satırların silindiğini belirtmektedir.

Aşağıdaki örnekte ise maaş alanı boş olmayan tüm personel silinecektir.

```sql
DELETE FROM Personel
WHERE maas IS NOT NULL;
25 Rows Deleted
```

**6.3 Tablo Satırlarındaki Verilerde Değişiklik Yapma-Güncelleme İşlemi**

Tablo satırlarında güncelleme yapmak için SQL’de UPDATE komutu kullanılır. DELETE komutunda olduğu gibi, UPDATE komutunu da koşullu ya da koşulsuz olarak kullanmak mümkündür. Koşul belirtilmemişse, belirtilen değişiklik tüm tablo satırları üzerinde gerçekleştirilir. Koşul belirtildiği takdirde, sadece koşulu sağlayan satırlar üzerinde değişiklik gerçekleştirilir. UPDATE komutunun yazılış biçimi aşağıdaki gibidir.

Koşulsuz ise,

```sql
UPDATE Tabloadı
SET Kolonadı1=değer1,Kolonadı2=değer2,.....,Kolonadı n=değer n;
Koşullu olduğu takdirde,
UPDATE Tabloadı
SET Kolonadı1=değer1,Kolonadı2=değer2,.....,Kolonadı n=değer n
WHERE Koşul;
```

Aşağıdaki UPDATE komutunun kullanılışı ile ilgili örnekler verilmiştir.

**SORU:** Tüm personelin maaşlarına %12 zam yapma işlemini gerçekleştiriniz.

**ÇÖZÜM:**
```sql
UPDATE Personel
SET maas=maas*1.12;
```

**SORU: **5 inci bölümde çalışan kişilerin maaşlarına %35 zam yapan UPDATE komutunu yazınız.

**ÇÖZÜM:**
```sql
UPDATE Personel
SET maas?maas*1.35
WHERE bol_no=5;
```

**SORU:** 2 inci bölümün yürüttüğü projelerde kullanılan tüm parçaların fiyatlarına %7 zam yapan UPDATE komutunu yazınız.

**ÇÖZÜM:**
```sql
UPDATE Parça
SET fiyat=fiyat*1.07
WHERE pr_no IN (SELECT proj_no
FROM Proje
WHERE bl_no=2);
```

**SORU:** Sicil numarası 27265421 olan personelin bölüm numarasını 5 olarak değiştiren ve maaşına %14 zam yapan UPDATE komutunu yazınız.

**ÇÖZÜM:**
```sql
UPDATE Personel
SET bol_no=5,maas=maas*1.14
WHERE sicil=’27265421’;
```

**6.4 Tablonun Yapısında Değişiklik Yapma (Alter Table Komutu)**

ALTER TABLE komutu ile bir tablonun yapısında değişiklik yapmak mümkündür. Standart SQL’de bu değişiklikler, tabloya yeni bir kolon ekleme (ADD sözcüğü yardımı ile) ve mevcut bir kolonunözelliklerini değiştirme (MODIFY komutu ile kolon genişliğini değiştirme ya da kolondaki verinin NULL ya da NOT NULL özelliğini değiştirme) şeklindedir.

Standart dışına çıkan bir çok SQL gerçekleştiriminde ise ayrıca tablodan bir kolon silme (DROP), mevcut bir kolonun adını değiştirme (RENAME) ya da tablonun adını değiştirme (RENAME TABLE) özellikleri de, ALTER TABLE komutu içinde mevcuttur.

**6.4.1 Mevcut bir tabloya bir kolon ekleme**

ALTER TABLE komutu içinde ADD sözcüğü kullanılarak, mevcut tabloya bir satır eklenebilir.

Mevcut bir tabloya, yeni bir kolon eklenirken, o kolon içindeki verinin türü, uzunluğu ve bu kolondaki verinin boş bırakılıp bırakılmayacağı (NULL veya NOT NULL) özellikleri de belirtilir.

**SORU:** Personel tablosuna, işe başlama tarihini belirten yeni bir kolon ekleyiniz.

**ÇÖZÜM:**
```sql
ALTER TABLE Personel
ADD is_bas_tar DATE;
```

Yeni eklediğimiz is\_bas\_tar alanı içinde veri yüklü olmayacağı için boş olacak yani NULL değerler taşıyacaktır. Eğer ADD is\_bas\_tar DATE NOT NULL; şeklini kullansaydık, bu kolon satırları gene boş olacaktı; fakat bu kolon ile ilişkili yeni boş değerler eklenmek istendiğinde, buna müsaade etmeyecekti (INSERT komutu ile). ADD sözcüğü ile aynı anda birden çok kolon eklenebilir.

**6.4.2 Mevcut bir tablonun kolonlarında değişiklik yapma (modify**

**komutu)**

Mevcut bir kolon üzerinde değişiklik yapma, değişken uzunluklu bir veri tipine sahip olan kolonun genişliğini arttırma ile sınırlıdır. Bu anlamda, kolon genişliğini azaltma ya da veri tipini değiştirme mümkün değildir.

Bu işlem için MODIFY sözcüğü ALTER TABLE komutu içinde kullanılır.

**SORU:** Daha önce Proje adlı tabloda VARCHAR(15) olarak tanımlanmış olan yer adlı alanı, 25 olarak genişleten SQL komutunu yazınız.

**ÇÖZÜM:**
```sql
ALTER TABLE Proje
MODIFY yer VARCHAR(25);
```

Aynı anda birden çok kolon üzerinde değişiklik yapılabilir. Yukarıda belirtildiği gibi, tabloda daha önce tanımlanmış bir tür (type) başka bir türe çevrilmez. Örneğin DATE’i MODIFY komutu ile CHAR, ya da INT olan bir alanı VARCHAR şekline dönüştürmek mümkün değildir.

**6.4.3 Mevcut bir tablodan bir kolon silme (drop komutu)**

Mevcut bir tablodan, bir kolon silmek için, ALTER TABLE komutu içine DROP sözcüğü eklemek gerekecektir. Örneğin, Personel tablosundan, is\_bas\_tar kolonunu silmek için

```sql
ALTER TABLE Personel
DROP is_bas_tar;
```

komutunu kullanmak gerekir.

Aynı anda birden çok kolon silinebilir. Bu durumda, DROP komutu içinde bunları virgüllerle ayırmak gerekir.

```sql
ALTER TABLE Personel
DROP is_bas_tar,yon_s_g_n;
```

Personel tablosundan işe başlama tarihi ve yönetici sosyal güvenlik numarası alanları silinmiştir.

Bir tablodan bir kolon silindiği takdirde, bu tablo kullanılarak üretilmiş VIEW’lerdeki ilgili kolonlar da otomatik olarak silinir. İndeks alanı olarak tanımlanmış alanların tablodan silinmesi, sistem tarafından kabul edilmez; önce indeks özelliğinin iptal edilmesi gerekecektir.

**6.5 Bir Tablonun Adını Değiştirme **−** Rename Table Komutu**

Mevcut bir tablonun adını değiştirmek için, ALTER TABLE komutu içinde RENAME TABLE ifadesi kullanılmalıdır. Örneğin Personel tablosunun adını elemanlar olarak değiştirmek istersek aşağıdaki komutu kullanmak gerekecektir.

```sql
ALTER TABLE Personel
RENAME TABLE elemanlar;
```

**6.6 Mevcut Bir Tablonun Bir Kolonunun Adını Değiştirme **−** Rename Komutu**

Mevcut bir tablonun, bir kolonunun adını değiştirmek için, ALTER TABLE

komutu içinde RENAME sözcüğü kullanılmalıdır. Örneğin, Personel tablosunda maas alanını, br\_maas olarak değiştirmek için aşağıdaki komutu kullanmak gerekir.

```sql
ALTER TABLE Personel
RENAME maas br_maas;
```

**6.7 Mevcut Bir Tablonun Tümüyle Silinmesi **−** Drop Table Komutu**

Bir tablonun tümünü silmek için DROP TABLE komutu kullanılmalıdır. Örneğin, Proje adlı tablonun silinmesi için aşağıdaki komut gereklidir:

```sql
DROP TABLE Proje;
```

Veri tabanından bir tablo, DROP TABLE komutu ile silindiği takdirde, bu tablodan üretilmiş bütün VIEW’ler, bu tablodan üretilmiş eş tablolar, tablo üzerindeki indeksler ve tablo için konulmuş bütün öncelikler de sistemden silinir.

**6.8 Bir Tabloda Yapılan Değişikliklerin İptali **− **Rollback ve Commit Komutları**

ROLLBACK komutu ile, veri tabanında, kullanıcının veri tabanında çalışmaya başlamasından itibaren yaptığı tüm değişiklikleri ya da en son kullanılan COMMIT komutundan sonra yapılan tüm değişiklikleri iptal etmek mümkündür.

```sql
ROLLBACK;
```

Komutu girildikten sonra, tablodan kolon silme, kolon güncelleme, tablonun tümünü silme, view silme gibi değişiklik işlemlerinin tümü iptal edilerek önceki duruma dönülecektir.

COMMIT komutu ise, kullanıcının veri tabanına bağlandığı andan itibaren ya da kullanılan en son COMMIT komutundan sonraki yukarıda bahsedilen türde bütün değişikliklerin kalıcı olarak veri tabanına aksettirilmesini ve saklanmasını sağlar.

```sql
COMMIT;
```

komutu ile o ana kadar gerçekleştirilen bütün değişiklikler sistemde kalıcı olarak yerleşecektir. Bu konuda ayrıntılı bilgi için hareket yönetimi bölümüne bakınız.

**6.9 View’ler Üzerinde Ekleme, Silme, Değişiklik İşlemleri**

VIEW’ler üzerindeki ekleme, silme ve değişiklik işlemleri esas itibarı ile tablolar üzerinde yapılan benzer işlemlerden çok farklı değildir. Fakat VIEW’ler üzerinde bu tip işlemlerin gerçekleştirilmesinde bazı kısıtlamalarda mevcuttur. Aşağıdaki hususların belirtilmesinde fayda vardır:

Bir view’in güncellenebilir nitelikte olması için, bir birleştirme (join) işlemi sonucunda üretilmemiş olması gerekir. Başka bir deyişle, CREATE VIEW komutunda FROM sözcüğünü izleyen kısımda sadece tablo adı bulunmalıdır.

View içindeki hiçbir kolon bileşik (aggregate) fonksiyonlarca üretilmiş olmamalıdır. (MAX, SUM v.b) View’in üretildiği SELECT komutunda DISTINCT, GROUP BY ya da HAVING sözcüklerini içeren parçaların yerine getirilmiş olmamalıdır.

Bu koşulları sağlamayan view’ler sadece okunabilir (Readonly) özellikteki view’lerdir ve üzerlerinde herhangi bir değişiklik yapılamaz.

**6.9.1 View içine satır ekleme**

Daha önceden oluşturulmuş Px adlı view, ad, soyad ve maas alanlarını içermiş olsun. Bu view, güncellenebilir nitelikte ise, aşağıdaki INSERT komutu ile, aynen tablolarda olduğu gibi kendisine bir satır eklemek mümkün olacaktır:

```sql
INSERT INTO Px
VALUES (‘Ali’,’Çakır’,12000000);
```

Daha önceden, VIEW oluşturulurken, CHECK OPTION alternatifi kullanılmışsa, bu takdirde, ekleme esnasında, VIEW’i oluşturan koşul ihlal ediliyorsa, sistem eklemeye müsaade etmeyecek ve hata mesajı verecektir.

**SORU:** Personel adlı tablodan, maaşı 20000000 TL’yi aşan personeli alarak, UST\_PER\_VIEW adlı bir view oluşturunuz.

**ÇÖZÜM:**
```sql
CREATE VIEW UST_PER_VIEW
AS SELECT FROM Personel
WHERE maas>20000000
WITH CHECK OPTION;
Şimdi UST_PER_VIEW içine
INSERT INTO UST_PER_VIEW
VALUES (37261,’34268152’,’Beril’,
’Caner’,{01/04/64},’Kadıköy’,.F.,
14000000,2,’37624158’);
```

komutu ile maaşı 14000000 olan bir kişi eklenmek istendiğinde, bu komut kabul edilmeyecek ve aşağıdaki hata mesajı alınacaktır:

```sql
Error:Not enough non-null values
```

Eğer CHECK opsiyonu kullanılmasaydı, hata mesajı verilmeksizin bu satır, view içine eklenecekti.

**6.9.2 View içinden satır silme**

Güncellenebilir bir view içinde satır silme işlemi, tablolardan satır silme işlemi ile aynı şekilde gerçekleştirilir. Örneğin 6.9.2’de oluşturulan UST\_PER\_VIEW içinden, maaşı 2500000’den az olan kişiler silinmek istenirse

```sql
DELETE FROM UST_PER_VIEW
WHERE maas<2500000;
```

komutunu kullanmak yeterli olacaktır.

**6.9.3 View satırları üzerinde güncelleme işlemi**

Güncellenebilir view’lerde güncelleme işlemi tablolardakinin aynıdır. Örneğin UST\_PER\_VIEW adlı view’de sicili 27251 olan kişinin maaşının 37000000 olarak değiştirmek için

```sql
UPDATE UST_PER_VIEW
SET maas=37000000
WHERE sicil=27251;
```

komutunu kullanmak uygun olacaktır.

**6.9.4 Bir view’i silmek**

Tabloların silinmesine benzer şekilde, sistemde oluşturulan bir view, DROP VIEW komutu ile silinebilir.

```sql
DROP VIEW UST_PER_VIEW;
```

Bir view’in silinmesi ile, o view’e bağlı olarak oluşturulmuş diğer bütün view’ler ve bu view ile ilişkili önceliklerin de tümü silinmiş olacaktır.

**BÖLÜM 7**

**İNDEKS OLUŞTURMA ve KULLANMA**

**7.1 İndeks Oluşturmanın Amacı**

Bir indeks, veri tabanı ortamında bir tablo ya da bir view gibi bir nesnedir ve ilişkili olarak kullanıldığı tablo ya da view’deki satırların, indeksleme alanı (key field (anahtar alan)) olarak kullanılan kolondaki verilere göre sıralanmış biçimde işleme sokulmasını (listeleme ya da arama işlemi) sağlar.

Bir tablo, indekslenmiş ise, bu tablo içinde gerçekleştirilecek bir arama (search) ya da koşullu listeleme (SELECT komutu ile) işlemi çok daha hızlı biçimde gerçekleştirilebilecektir.

**7.2 İndeks Yaratma**

** **SQL’de bir tablo ile ilşkili olarak indeks yaratmak için gerekli komut CREATE INDEX komutudur. Komutun yazılış biçimi aşağıdaki gibidir:

```sql
CREATE INDEX indeks adı
ON tabloadı (kolonadı 1,kolonadı 2,....,kolonadı n );
```

İndeksleme artan (ascending) ya da azalan (decending) şeklinde olabilir. Artan, alfabetik olarak A’dan Z’ye nümerik olarak küçükten büyüğe şeklindedir. Azalan ise bunun tersidir. Hiçbir özel sözcük kullanılmazsa indeksleme artan sayılır ya da alan adının yanında bir boşluktan sonra ASC sözcüğü kullanılırsa bu alana göre artan sıralama yapılacak demektir.

Herhangi bir alanın adının yanında DESC sözcüğünün kullanılması ise indekslemenin azalan olacağını gösterir. Komutun yazılış biçiminden anlaşılacağı gibi, aynı anda, birden çok alana göre indeksleme de yapılabilir.

**7.2.1 Tek bir alana göre artan sırada indeksleme**

İşletmede çalışan personeli maaşlarına göre artan sırada listelemek istersek, maas alanına göre bir indeks oluşturmalıyız.

```sql
CREATE INDEX pers_maas
ON Personel (maas);
Index created 127 Rows
```

127 satırlık personel tablosu ile ilişkili olarak maas alanına indeks anahtarı olarak kullanılan pers\_maas adlı indeks oluşturulmuştur. Bu durumda

```sql
SELECT *
FROM Personel;
```

şeklindeki listeleme komutu sonucunda, personel tablosundaki tüm personel, maaşlarına göre sıralı olarak listelenecektir.

**7.2.2 Tek bir alana göre azalan sırada indeksleme**

İşletmede çalışan personeli maaşlarına göre azalan sırada (yüksek maaştan düşük maaşa doğru) listelemek istersek, maas alanına göre aşağıdaki şekilde oluşturmak gerekir.

```sql
CREATE INDEX pers_maas
ON Personel (maas DESC);
```

**7.2.3 Birden fazla alana göre indeksleme**

İşletmedeki personelin öncelikle adlarına göre, aynı ad da olanların soyadlarına göre, hem adı hem soyadı aynı olanların maaşlarına göre sıralanmış olarak listelenmesi istenirse aşağıdaki komut kullanılmalıdır:

```sql
CREATE INDEX p_ad_soy_m
ON Personel (ad,soyad,maas);
```

Bu durumda

```sql
SELECT *
FROM Personel;
```

komutu sonucunda, aşağıdaki şekilde sıralanmış tablo görüntülenecektir.

sicil ad soyad maas

11117 Ahmet Caner 15000000 .......

247 Ahmet Deniz 27000000 .......

645 Ahmet Zoran 12000000 .......

3871 Ali Cenker 26000000 .......

15372 Ali Cenker 34000000 .......

4246 Ali Cenker 65000000 .......

16656 Ali Şener 12000000 .......

7216 Beril Arkan 18000000 .......

....... ....... ....... .......

Burada, kolayca görüleceği gibi personel öncelikle adı alanına göre sıralanmış (Ahmet, Ali, Beril) aynı ada sahip olanlar soyadlarına göre sıralanmış (Ahmet ismindeki kişilerin soyadları olan Caner, Deniz, Zoran sıralaması gibi), hem ad hem de soyadları aynı olanların sıralanmasında ise maas alanı dikkate alınmıştır.

İndeks komutu

```sql
CREATE INDEX p_ad_soy_m
ON Personel (ad,soyad,maas DESC);
```

şeklinde yazılsa idi, tablodaki değerler

sicil ad soyad maas

11117 Ahmet Caner 15000000 .......

247 Ahmet Deniz 27000000 .......

645 Ahmet Zoran 12000000 .......

3871 Ali Cenker 65000000 .......

15372 Ali Cenker 34000000 .......

4246 Ali Cenker 26000000 .......

16656 Ali Şener 12000000 .......

7216 Beril Arkan 18000000 .......

....... ....... ....... .......

şeklinde sıralanırdı. Bu durumda farklı olan ad ve soyad alanı aynı olan kişilerin maaşlarına göre, yüksek maaştan düşük maaşa göre sıralanmış olmasıdır. (maas DESC ifadesinden ötürü)

**7.2.4 Unique sözcüğü**

Bir tablo, seçilen bir sütuna (alana) göre indekslenirken, indeksleme alanı olarak seçilen sütundaki verilerin tekrarlanmasına müsaade edilmesi isteniyorsa, indeksleme yapılırken, CREATE INDEX komutu içinde UNIQUE sözcüğü kullanılmalıdır:

```sql
CREATE UNIQUE INDEX pers_sicil
ON Personel (sicil);
```

UNIQUE sözcüğünün etkisi, bu komuttan sonra, tabloda, aynı sicilden birden fazla tekrar olmasını engellemesidir.

Personel tablosunu

```sql
INSERT INTO Personel
VALUES(53768,’27241685’,’Ayşe’,’Şen’,{01/04/63},’Kadıköy’,
.F.,27000000,2,’34261578’);
```

komutu ile sicil 53768 olan kişi eklenmek istendiği zaman, bu sicilden daha önce o tabloda mevcutsa, ekleme kabul edilmeyecek ve

-Error- data is not unique

-Hata- veri tekrarsız (tek) değildir.

şeklinde bir hata mesajı alınacaktır.

**7.3 Mevcut Bir İndeksin Silinmesi**

Bir tablo üzerinde tanımlanmış herhangi bir indeks, o tablonun veri tabanından silinmesi ile otomatik olarak silinecektir.

Tablo silinmeksizin, o tablo üzerinde oluşturulan indeksin silinmesi içinse, DROP INDEX komutu kullanılmalıdır.

```sql
DROP INDEX pers_in;
```

komutu ile

```sql
INDEX DROPPED
(İndeks Silindi)
```

mesajı alınacaktır. Böylece, Personel tablosu üzerinde oluşturulmuş pers\_in adlı indeks, personel tablosu veri tabanında kaldığı halde silinecektir.

**BÖLÜM 8**

**SQL’İN DİĞER BİLGİSAYAR DİLLERİNE ve YAZILIMLARINA**

**KATILIMI (EMBEDDED SQL)**

**8.1 SQL Katılımının Amacı**

SQL için iki çalışma modu mevcuttur.

Etkileşimli SQL modu (interactive SQL mode)

Katılımlı SQL modu (embedded SQL mode)

Bu bölüme kadar, SQL’in etkileşimli modu ile ilişkili uygulama ve komutlar ele alınmıştır. Bu modda, her komut, sisteme gönderilmekte ve sistem cevabı olarak bir sonuç ya da bir hata mesajı karşılığı alınmaktadır.

Etkileşimli modda aşağıda belirtilen üç noktada önemli güçlükler vardır:

Tablolara bilgi girişi: Her tablo satırı girişi için ayrı bir INSERT komutuna gerek vardır. Bu oldukça önemli güçlük oluşturur. Ayrıca, kullanıcı için kolaylık sağlayan bilgi giriş ekranlarını, etkileşimli modda ve SQL komutları ile gerçekleştirmek olanaksızdır.

Bilgi işleme: Etkileşimli moddaki SQL belli bir anda tek bir komut icra edilebilir ve aynı zamanda, bir komutu otomatik olarak, tekrar takrar icra edebilme yeteneğine sahip değildir. Başka bir deyişle ve bilgisayar yazılımı terimleri ile çevrim (döngü-loop) yapılarından yoksundur.

Ayrıca etkileşimli SQL modunda IF...THEN...ELSE....END IF şeklinde ki kontrol yapılarını kullanma imkanı yoktur.

Bilgi çıkışı: Etkileşimli SQL modu ile, gerçekleştirilen bir sorgulama sonucunu, kullanıcının arzu edeceği düzen ve esneklikle ekrana aktarma imkanı yoktur. Başka bir deyişle, etkileşimli SQL modunda, istenilen tarzda rapor hazırlamayı gerçekleştirebilecek esneklikte bilgi çıkış komutları mevcut değildir.

SQL, tanım olarak veri tabanı alt dilidir. Yani bir bilgisayar dilinin gerek

gösterdiği tüm yapılara sahip değildir.

SQL’in sahip olduğu özellikler bu noktaya kadar görüldüğü gibi,veri tanımlama, bütünlük kontrolü, veriye erişim ve sorgulama, veriyi güncelleme ile ilişkili komut yapılarıdır. Dolayısı ile eksik olan dil yapıları (bilgi giriş/çıkış, ekran tasarımı, döngü (loop)) ile ilişkili programa gereksinimleri, SQL’in başka bir dil veya veri tabanı yazılımı ile etkileşimi ile (C, Pascal v.b.) sağlanacaktır.

Öte yandan SQL, sorgulama dili olarak bir standart haline gelmiştir. İlişkisel veri tabanı sistemlerindeki sorgulama işlemleri, hangi veri tabanı yazılımı ya da bilgisayar dili kullanılırsa kullanılsın SQL ile yapılmaktadır.

Yeni geliştirilen bilgisayar dilleri ve yazılımları da tümü ile SQL kullanımını desteklemektedir (Visual Basic, Visual C++, Foxpro v.b.).

SQL dili yordamsal bir dil değilidir. Tam tersine küme esaslı bir dildir. Bunun anlamı şudur: SQL dili ile örneğin bir sorgulama esnasında, SELECT komutu ile belirli bir koşulu sağlayan tablo satırlarının tümü birden elde edilir. Bu satırları tek tek alarak üzerinde işlem yapma imkanı yoktur. Oysa yordamsal diller, bir tablo üzerinde satır satır ya da kütük üzerinde kayıt kayıt işlem yapma imkanına sahiptirler.

Bundan sonraki lat bölümde, set oriented SQL dili ile yordamsal bir yaklaşım ile nasıl işlem yapılabileceği anlatılacaktır.

**8.2 Kürsör Kullanımı**

SQL’deki anlamı ile kürsör, SELECT komutu ile seçilmiş tablo satırları arasından, belirli bir satırı işaret eden gösterge demektir. Belli bir anda kürsörün işaret ettiği tablo satırı üzerinde (sadece o satırda) güncelleme ya da satır silme işlemi yapılabilecektir.

Kürsör özelliği, SQL’in küme esaslı yapısı ile diğer dillerin yordamsal yapısı arasında bir köprü görevi görür. Kürsör, aynen SELECT komutunun yaptığı gibi, belirli bir koşulu sağlayan tablo satırları kümesini elde eder; fakat SELECT'’en farklı olarak ve SELECT’in yapamadığı işlemi yaparak bu küme içindeki tablo satırlarını tek tek işleme sokabilir. Kürsör özelliğini kullanmaksızın, bu tür bir işlem yapma olanağı yoktur.

Bir SELECT işlemi ile ilişkili olarak bir kürsör tanımlama iki aşamalı bir süreçtir.

DECLARE CURSOR komutu ile kürsör için bildiride bulunulur.

OPEN komutu ile de kürsör açılır. (aktif hale getirilir.)

Kürsör açıldığı zaman, veriye erişmek için, FETCH deyimi kullanılmalıdır. Kürsör ile ilişkili işlemler

Bitince, CLOSE deyimi ile kürsör kapatılır.

Bir kürsörün kapatıldıktan sonra yeniden açılması gerektiğinde, yeniden bildiride bulunmaya (DECLARE CURSOR) gerek yoktur. Aynı anda bir tablo ile ilişkili olarak birden çok kürsör bildirisinde bulunulabilir. Bir yordam içinde kullanılabilecek kürsör sayısı bakımından da bir limit yoktur. Fakat bir kürsör, sadece tanımlandığı yordam içinde kullanılabilir.

**8.3 Kürsör Komutları**

**8.3.1 Declare cursor komutu**

Bir kürsör ismini, SELECT komutu ile ilişkili hale getirir.

```sql
DECLARE Kürsöradı CURSOR
FOR SELECT−Komut [FOR READ[ONLY] ]
```

şeklindedir. Burada kürsör adı, SQL isim verme kurallarına uygun olarak verilmiş isimlerdir.

SELECT komutu, daha önce görüldüğü şekilde olup WHERE, GROUP BY, HAVING ya da ORDER BY sözcüklerini de içerebilir. Ayrıca istenirse içinde alt SELECT komutları, bileşik fonksiyonlar ve diğer SELECT ile kullanılabilen yapılar bulunabilir. SELECT komutu, kürsör açıldığı zaman erişilebilecek tablo satırları kümesini belirler.

FOR READ ONLY parçası ile kullanılırsa, seçilen satırlar sadece okunabilir; seçilen satırlar üzerinde güncelleme ya da satır silme işlemleri gerçekleştirilemez.

DECLARE CURSOR komutu, kürsör açılmadan ya da kürsöre herhangi bir yerde referans verilmeden, icra edilmelidir. Kürsör, bir yordam içinde birçok kez kapanıp açılsa da, DECLARE CURSOR komutu sadece bir kez görünmelidir.

**ÖRNEK:**
```sql
DECLARE kürsör1 CURSOR FOR
SELECT sicil,ad,soyad,maas
FROM Personel
WHERE bol_no=2;
```

SELECT komutu, WHERE cümleciği içinde, SQL’in içinde kullanıldığı dile ya da yazılıma ait (C, Pascal, Foxpro v.b.) bir değişkene referans verebilir. Kullanılan dile ait değişken, kürsör açıldığı zaman işleme sokulur.

Aşağıdaki örnek SQL’in içinde kullanıldığı dil değişkenine nasıl referans verildiği ile ilişkindir:

**ÖRNEK: **DEFINE VARIABLE ysg\_n

```sql
AS CHARACTER INITIAL “25724711”;
DECLARE kürsör2 CURSOR FOR
SELECT ad,soyad,y_sos_g_n
FROM Personel
WHERE y_sos_g_n=ysg_n
ORDER BY ad,soyad;
```

Burada ysg\_n adlı, SQL’in içinde kullanıldığı dile ait değişken DEFINE VARIABLE komutu ile tanımlanmış ve bu değişkene 25724711 başlangıç değeri atanmıştır.

**8.3.2 Open komutu**

Yazılış biçimi:

```sql
OPEN kürsöradı
```

şeklindedir.

OPEN komutu, DECLARE CURSOR komutundaki SELECT deyiminin icra edilmesi ile elde edilen tablo satırları kümesi içinden erişim yapılabilmesi işlemini başlatır. OPEN komutu sonucunda, kürsör, SELECT ile elde edilecek tablo satırları kümesinden oluşan erişim satinin ilk satırına konumlanacaktır.

```sql
OPEN kürsör1
```

komutu ile kürsör1 adlı kürsör açılmaktadır. Bir kürsör, tanımlandıktan sonra çeşitli kereler açılır ve kapatılabilir. Kürsörün her açılışı esnasında, SELECT komutu yeniden icra edilir. O nedenle kürsörü, bir kez bildirel yeterlidir. Her yeni icra sonucu erişim seti farklı olabilir.

**8.3.3 Fetch komutu**

Bu komut yardımı ile, açılan erişim seti içindeki tablo sütunlarındaki verielr, SQL’in içinde kullanıldığı program içindeki değişkenlere aktarılabilir.

Kullanış biçimi:

```sql
FETCH kürsöradı INTO değişken listesi
```

şeklindedir.

FETCH komutuna ait değişken listesinde bulunan değişkenler, DECLARE CURSOR komutu içindeki SELECT komutu içinde bulunan tablo sütun adları ile sayı, sıra ve tür bakımından uyuşmalıdır.

**ÖRNEK:**
```sql
DECLARE kürsör3 CURSOR
FOR SELECT ad,soyad,y_sos_g_n,maas
FROM Personel;
```

Şeklinde tanımlanmış kürsör3 ile erişilebilecek veri kümesi, ad, soyad, y\_sos\_g\_n ve maas adlı tablo sütunları ile saklanan verilerden oluşmaktadır. Bununla ilişkili olarak

```sql
FETCH kürsör3 INTO a,s,ysgn,b_maas
```

şeklindeki komut ile, erişim setinde o esnada aktif olan tablo satırındaki verilerden

ad ⎯→ a

soyad ⎯→ s

```sql
y_sos_g_n ⎯→ ysgn
maas ⎯→ b_maas
```

adlı değişkenlere aktarılacaktır.

SELECT’teki sütun adları ile dil değişkenleri aynı isimden olmamalıdır. FETCH belli bir anda bir tablo satırına erişilir. Her yeni FETCH, yeni bir satıra erişecektir. Bir erişim setindeki bütün satırlara erişmek için, FETCH komutu, SQL’in içine katıldığı dildeki bir çevrim (loop) yapısı içinde kullanılmalıdır. (SQL’de Loop komutları olmadığını hatırlayınız.)

**8.3.4 Konumlandırılmış güncelleme işlemi**

Güncelleme işlemini gerçekleştiren UPDATE komutunun, o esnada kürsörün işaretlediği tablo satırı üzerinde işlem yapan, konumlandırılmış şekli, açılan bir kürsör ile birlikte kullanılır. Bir tablo satırındaki veriye erişimi sağlayan FETCH komutunun icrasından sonra, erişilen tablo satırı üzerindeki her kolon için güncelleme işlemi gerçekleştirilebilir.

Konumlandırılmış UPDATE komutunun yazılış biçimi aşağıdaki gibidir:

```sql
UPDATE Tabloadı
SET sütun(kolon)adı=ifade
WHERE CURRENT OF kürsör
```

Burada kullanılacak tablo adı, DECLARE CURSOR komutundaki tablo adının aynısı olmalıdır.

İçindeki SELECT komutunda DISTINCT sözcüğü, birleştirme işlemi (JOIN), bir matematiksel ifade ya da sabit , bir alt SELECT,GROUP BY ya da HAVING cümleciği, güncellenemez bir VIEW için referans mevcut olan kürsör işlemlerinde güncelleme işlemi yapılamaz.

Konumlandırılmış güncelleme ile ilişkili aşağıdaki örneği inceleyiniz:

```sql
DEFINE VARIABLE bmaas LIKE
```

Personel.maas

```sql
DECLARE kürsör4 CURSOR FOR
SELECT maas
FROM Personel
OPEN kürsör4
```

REPEAT:

```sql
FETCH kürsör4 INTO bmaas
UPDATE Personel
SET maas=bmaas+2500000
WHERE CURRENT OF kürsör4
END
CLOSE kürsör4
```

Bu örnekte, DECLARE CURSOR komutu ile personel tablosundaki maas brüt maaşlar kümesi elde edilmiş ve OPEN komutu ile bu kümenin ilk satırı erişilebilir hale getirilmiştir.

|  | BRÜT |
| --- | --- |
| ⎯⎯→ | 37000000 |
|  | 12000000 |
|  | 13000000 |
|  | ....... |
|  | 47000000 |

FETCH komutu ile personel’deki ilk satıra ait maaş, bmaas isimli, SQL’in içinde kullanıldığı dile ait değişkene yüklenmiştir.

UPDATE komutu ile ilk satıra ait maaş, bmaas+2500000 ifadesi ile 2500000 TL arttırılarak güncellenmiştir. Bir sonraki işlemde FETCH komutu bir sonraki satırı işleme sokacaktır. Satırlar arasında dolaşarak, tüm erişim kümesi üzerinde işlem yapma ise, bu örnekte, PROGRESS veri tabanı yazılım sistemine ait REPEAT:END çevrim (loop(döngü)) yapısı ile gerçekleştirilmektedir.

**8.3.5 Konumlandırılmış Delete komutu**

Konumlandırılmış UPDATE komutuna benzer şekilde çalışır. Açık bulunan kürsörün o esnada işaret ettiği satırı siler. Satır silindikten sonra, kürsör bir sonraki satırın başına gelir.

**ÖRNEK:**
```sql
DELETE FROM Personel
WHERE CURRENT OF kürsör4
```

Bu komut ile, kürsör4’ün o esnada işaret ettiği tablo satırı, Personel tablosundan silinecektir.

**8.3.6 Kürsörün kapatılaması**

Bir kürsör ile oluşturulan erişim kümesi ile bağlantıyı kesmek başka bir deyişle erişim kümesini erişilemez hale getirmek için CLOSE komutu kullanılır. Komut,

```sql
CLOSE kürsöradı
```

şeklinde kullanılır. CLOSE komutundan sonra OPEN ile yeniden açılmadıkça, kürsörün oluşturduğu erişim kümesine yeniden erişmek mümkün değildir.

**8.4 Bir SQL Tablosundan Tek Bir Satır Seçme (Select Into Komutu)**

SELECT INTO komutu, tablo içinden sadece tek bir satıra erişir. Amaç, tablo içindeki bütün satırları ya da belli koşulları sağlayan satırları taramak olmayıp sadece belirli bir satıra erişmekse , kürsör tanımlayıp, FETCH komutu kullanmak yerine sadece SELECT INTO komutu kullanılabilir.

SELECT INTO komutu, WHERE kısmında belirtilen koşulun sadece bir satır üreteceği varsayımı ile çalışır. Aksi durumda hata mesajı alınacaktır.

**ÖRNEK:**
```sql
DEFINE scl LIKE Personel.sicil
DEFINE bmaas LIKE Personel.maas
SELECT sicil,maas INTO scl,bmaas
FROM Personel
WHERE sicil=’2715213’;
```

**8.5 SQL’in Destek Sağladığı Diller**

SQL’in içinde kullanılabildiği diller yedi tanedir. Bu diller:

C

COBOL

FORTRAN

MUMPS

PASCAL

ADA

PL/I

dilleridir. SQL komut ve bildirileri, kullanıldığı üst dil ya da esas dil içinde iki ayraç başlangıç ve bitiş ayraçları içine alınır. Bu ayraçlar yukarıda belirtilen diller için Tablo 8.1’deki gibidir.

**Tablo 8.1** Üst Diller İçinde SQL Ayraçları.

| DİL | BAŞLANGIÇ | BİTİŞ |
| --- | --- | --- |
| ADA | EXEC SQL | ; |
| C | EXEC SQL | ; |
| COBOL | EXEC SQL | END-EXEC |
| FORTRAN | EXEC SQL | YOK |
| MUMPS | &SQL( | ) |
| PASCAL | EXEC SQL | ; |
| PL/I | EXEC SQL | ; |

**8.6 Cobol İle SQL Kullanımı**

Bir COBOL programı içinde, SQL kullanımı için aşağıdaki işlemlerin gerçekleştirilmesi gerekir:

Üst dil (COBOL) içinde SQL ile bağlantılı olarak kullanılacak değişkenler tanımlanın (WORKING STORAGE SECTION’da) SQL ile haberleşmeyi sağlayacak olan SQLCA sisteme ilave edilir. (SQLCA →SQL Communication Area anlamındadır.) Bunun için COBOL içinde

```cobol
EXEC SQL INCLUDE SQLCA
END−EXEC
```

komutu, COBOL’un WORKING−STORAGE SECTION kesimine yerleştirilir. PROCEDURE DIVISION’da, gerekli SQL komutları, COBOL’un

```sql
EXEC SQL
```

SQL Komutları

```sql
END−EXEC
```

ayraçları içine yazılır.

**ÖRNEK:** Sicil’i 27562 olan kişi ile ilişkili ad, soyad, maas ve bölüm bilgilerini görüntüleyen programı yazınız.

```cobol
INDENTIFICATION DIVISION.
ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING−STORAGE SECTION
EXEC SQL BEGIN DECLARE SECION END−EXEC.
01 USICIL PIC 9 (5).
01 UAD PIC A (10)
01 USOYAD PIC A (10)
01 UMAAS PIC 9 (13) V 9 (2).
EXEC SQL END DECLARE SECTION END−EXEC.
01 B-MAAS PIC 9 (13). 9 (2).
EXEC SQL INCULEDE SQLCA
END−EXEC.
PROCEDURE DIVISION.
EXEC SQL SELECT sicil,ad,soyad,maas
INTO :USICIL,: UAD,: USOYAD,: UMAAS
FROM Personel
WHERE sicil=27562
END−EXEC.
DISPLAY “Sicili 27562 Olan kişi”
DISPLAY “Ad Soyad Maaş”
IF SQLCODE=O
MOVE UMAAS TO B-MAAS
DISPLAY UAD,” ”,USOYAD,” ”,B-MAAS
ELSE
DISPLAY “Hata kodu ........”, SQLCODE
STOP RUN.
```

Yukarıdaki programda iki noktanın açıklığa kavuşturulması gerekmektedir.

Birincisi, SQL komutları içinde üst dile ait değişkenler: sembolü ile başlamaktadır.

İkinci nokta ise, SQLCODE değişkenidir. Bu değişken, SQL haberleşme alanı (SQLCA) içinde tanımlanmış bir nümerik değişken olup, değerinin kontrol edilmesi ile, hata olup olmadığı, tablonun sonuna gelinip gelinmediği anlaşılır. SQLCODE için aşağıdaki değerlerin kontrolü sözkonusudur.

FETCH işelemi başarılmış ise, yani SELECT komutu tablo değerleri üst dilin değişkenlerine başarı ile aktarılmış ise, SQLCODE değişkeninin değeri ∅’dir. Tablodan erişilecek satır yoksa ya da tablonun sonuna gelinmiş ise SQLCODE’un değeri 100’dür. Herhangi bir hatadan dolayı FETCH işlemi başarılamamışsa, SQLCODE’un değeri negatiftir. (Bazı gerçekleştirimlerde –1’dir.)

```cobol
INDENTIFICATION DIVISION.
EVIRONMENT DIVISION.
DATA DIVISION.
WORKING−STORAGE SECTION
01 TO-MAAS PIC 9 (15). 9 (2).
01 T-MAAS PIC 9 (15) V 9 (2).
01 O-MAAS PIC 9 (13) V 9 (2).
01 OO-MAAS PIC 9 (13). 9 (2).
01 SAY PIC 9 (4).
EXEC SQL BEGIN DECLARE
SECTION END−EXEC
01 UMAAS PIC 9 (13) V 9 (2).
EXEC SQL END DECLARE SECTION
END−EXEC.
EXEC SQL INCULEDE SQLCA END−EXEC.
PROCEDURE DIVISION.
EXEC SQL WHENEVER SQLWARNING
CONTINUE END−EXEC.
PERFROM P1.
PERFROM P2 UNTIL SQLCODE IS
```

NOT EQUALS TO ZERO.

```cobol
PERFROM P3.
STOP RUN.
P1.EXEC SQL DECLARE kürsör1
FOR SELECT maas
FROM Personel END−EXEC.
MOVE ∅ TO T-MAAS.
MOVE ∅ TO O-MAAS
MOVE ∅ TO SAY.
EXEC SQL OPEN kürsör1 END−EXEC.
P2.EXEC SQL FETCH kürsör1
INTO:UMAAS END−EXEC
IF SQLCODE THEN
MOVE UMAAS TO T-MAAS
ADD 1 TO SAY
P3.IF SQLCODE=100
COMPUTE O-MAAS=T-MAAS / SAY
MOVE T-MAAS TO TO-MAAS
MOVE O-MAAS TO OO-MAAS
DISPLAY “Maaş Toplamı....”,TO-MAAS
DISPLAY “Ortalama maaş...”,OO-MAAS
ELSE
DISPLAY “Hata Kodu.....”,SQLCODE.
EXEC SQL CLOSE kürsör1 END−EXEC.
```

**8.7 Whenever Komutu ve SQLState Parametresi**

** **WHENEVER komutu da, SQLCA’yı kullanarak üç sonuçtan birinin meydana gelip gelmediğini kontrol eder. Kontrol edilen koşul oluşmadı ise, program devam eder. Şayet kontrol edilen koşul oluşmuşsa, bu durmda program işaret edilen noktaya dallanır ya da belirtilen işlemi yapar.

WHENEVER ile kontrol edilecek üç sonuç sunlardır:

NOT FOUND

SQLERROR

```sql
SQLWARNING
```

Bu sonuçlardan her biri, SQLCA içinde tanımlanan değişkenlere ait belirli bir değeri yansıtmaktadır. SQL komutu sonucu, kontrol edilen koşulu sağlayan hiçbir tablo satırı elde edilmemişse, NOT FOUND sonucu oluşur. SQL komutu sonucu, bir hata oluşmuşsa, SQLERROR değeri elde edilir.SQL komutunun icrası sırasında bir uyarı durumu oluşursa da SQLWARNING sonucu elde edilecektir.

Aşağıdaki program parçasında, erişilecek tablo satırı bulunmadığı zaman ne yapılacağı belirtilmektedir:

```sql
EXEC SQL
WHENEVER NOT FOUND
```

GO TO P1

```sql
END−EXEC.
```

Aşağıdaki program parçasında ise, bir uyarı durumu oluşursa, programın icrasına devam edilmesi gereği belirtilmektedir.

```sql
EXEC SQL
WHENEVER SQLWARNING
```

CONTINUE

```sql
END−EXEC.
```

SQL içinde kullanılan SQLCODE parametresi, SQL standardında halen mevcut ve kullanılabilir durumda olmasına rağmen, standart komitesince “eskimiş özellik” listesine konulmuştur. Bunun anlamı bir sonraki standart düzenlemesinde SQL standardından çıkarılacağıdır.

SQLCODE’un sağladığı kontrolün daha kapsamlısını sağlayan SQLSTATE parametresi kullanmak bu durumda daha modern bir yaklaşımdır.

SQLSTATE 5 karakter uzunluğunda ve iki kısımdan oluşan bir değişkendir. İlk iki karakter sınıf, onu izleyen üç karakter ise alt sınıf adını alır.

Bazı önemli SQLSTATE değerleri aşağıdaki tabloda verilmiştir:

```sql
**Tablo 8.2** SQLSTATE Parametre Değerleri.
```

| Sınf | Alt Sınıf | Anlamı |
| --- | --- | --- |
| 00 | 000 | FETCH işlemi başarı ile tamamlandı. |
| 00 | 100 | Tabloda erişilecek satır kalmadı. |
| 23 | 000 | Bütünlük (integrity) kısıtlı ihlal ediliyor. |
| 34 | 000 | Geçersiz kürsör adı |
| 2A | 000 | İnteraktif SQL komutunda yazılış ya da erişim hatası |
| 37 | 000 | Dinamik SQL komutunda yazılış ya da erişim hatası |
| 01 | 000 | Uyarı |
| 24 | 000 | Geçersiz kürsör durumu |
| 42 | 000 | Yazılış hatası ya da erişim kuralını ihlal etme |

**ÖRNEK:** **.**

** .**

```sql
** **EXEC SQL
```

-

-

```sql
IF SQLSTATE =’∅∅1∅∅’ GO TO P1.
```

-

-

```sql
IF SQLSTATE=’ ∅∅1∅∅’ GO TO SON.
```

-

-

```sql
END−EXEC.
```

**8.8 C Dili İçinde SQL Kullanımı**

** **C dili içinde SQL kullanımı esas itibarı ile COBOL içindeki kullanımdan farklı değildir. Sadece, SQL ayraçları olarak

```sql
EXEC SQL BEGIN DECLARE SECTION;
```

ve

```sql
EXEC SQL END DECLARE SECTION;
```

yapısı kullanılır.

```c
EXEC SQL BEGIN DECLARE SECTION;
Char Parcano[15];
Sqlind Parcanolnd;
Char Parcano3[15];
Char Parcano5[15];
Char Parcano7[15];
Char Parcano9[15];
Char Ustkomp[15];
Sqlind Partnolnd;
Char Partname[31];
Sqlind Partnamelnd;
Char Partname[31];
Sqlind Partname5lnd;
Char Parcaadi[31];
Sqlind Parcaadilnd;
Char Parcaadi5[31];
Sqlind Parcaadi5lnd;
Char resimno4[16];
EXEC SQL END DECLARE SECTION;
```

**8.9 dBase IV İçinde SQL Kullanımı**

Kişisel bilgisayar için geliştirilmiş en önemli veri tabanı yönetim yazılımlarından biri olan dBASE Iviçinde veri tabanı sorgulamalarını gerçekleştirecek, bu tür yazılımlara özgü XBASE komutları sınıfından komutlar mevcuttur. Örneğin sorgulama için DISPLAY FOR komutu kullanılabilir. Ayrıca veri tabanları üzerinde güncelleme, silme gibi işlemler için de REPLACE, DELETE gibi XBASE komutlarından yararlanmak mümkündür.

Fakat ilişkisel modele dayalı veri tabanlarındaki sorgulama işlemlerinde, özellikle birden çok tabloyu bir arada işleme sokmayı gerektiren sorgulamalarla, SQL komutlarının kullanımı programcıya aşağıdaki gibi yararlar sağlayacaktır:

SQL sorgulama komutları, aynı karmaşıklıktaki işlemler için kullanılabilecek XBASE komutları grubuna göre daha kısa ve anlaşılır yapıdadır.

SQL veri tabanı yönetim yazılımlarının standart bir sorgulama dili olduğu için dBASE IV dışındaki veri tabanı yazılımlarına geçişte kolaylık sağlayacaktır. Özellikle mainframe bilgisayarlar için geliştirilen ORACLE ve PROGRESS gibi veri tabanı yönetim yazılımlarında SQL, sorgulama için kullanılabilecek tek araçtır.

Bir dBASE programcısı, bu bölümün başlarında belirtilen nedenlerle, programdaki bilgi giriş, ekran tasarımı, rapor dökümü gibi işlemleri XBASE komutları ile yapacaktır. Çünkü konularda SQL’in etkileşimli komutları yoktur ya da yetersizdir. Fakat sorgulama işlemleri içinse, SQL’in gücünden yararlanacaktır.

Ayrıca, SQL’den bağımsız olarak, SQL ile oluşturulmuş veri tabanı tabloları, dBASE IV’ün etkileşimli komutları (BROWSE, EDIT, APPEND, CREATE) ile de işlenebilir.

DBASE IV içinde SQL’in iki şekilde kullanılması mümkündür. Etkileşimli modda (SQL . modu) komut kütüğü içerisinde dBASE IV’te nokta modunda iken

```sql
SET SQL ON ↵
```

komutu girilirse SQL’in nokta moduna geçilir ve

SQL

mesajı gelir. Bu andan itibaren SQL komutları etkileşimli olarak kullanılabilirler.

DBASE IV’ün help olanığı kullanılırsa (F1 tuşu ile), burada dBASE IV’te geçerli olan SQL komutlarının bir listesi ve syntax kuralları da elde edilebilir.

SQL komutları bir dBASE IV program kütüğü (.PRS uzantılı) içinde, dBASE IV (ya da XBASE) komutları ile birlikte de kullanılabilir.

Aşağıdaki verilen tabloda program listesi bu konuda faydalı bir fikir verecektir.

\*Personel tablosu içinde kısmi

\*Sorgulama, güncelleme, silme

\*İşlemlerini gerçekleştiren menülü

\*Bir Program−PROG.PRS

```dbase
SET TALK OFF
SET ECHO OFF
START DATABASE ISLETME;
DO WHILE .T.
CLEAR
@ 5, 10 SAY ‘Personel Bilgi Sistemi’
@ 6, 10 SAY ‘S−Sorgulama’
@ 7, 10 SAY ‘G−Güncelleme’
@ 8, 10 SAY ‘D−Silme’
@ 9, 10 SAY ‘C−Programdan Çıkış’
?
?
WAIT “Seçiminiz........” TO SEC
DO CASE
CASE UPPER(SEC)=”S”
DO SOR
CASE UPPER(SEC)=”G”
DO GUNCEL
CASE UPPER(SEC)=”D”
DO SIL
CASE UPPER(SEC)=”C”
RETURN
OTHERWISE
```

? “Hatalı Seçim”

```dbase
END CASE
WAIT “Devam için Return” TO XX
END DO
RETURN
PROCEDURE SOR
CLEAR
SELECT * FROM Personel
ORDER BY sicil;
WAIT “Devam için Return” TO XX
RETURN
PROCEDURE GUNCEL
CLEAR
@ 10, 10 SAY “Bölüm No......” GET b_no
READ
DECLARE kürsör CURSOR
FOR SELECT ad,soyad,adres,maas
WHERE bol_no=b_no;
FOR UPDATE OF ad,soyad,adres,maas;
OPEN kürsör;
IF SQLCNT=0
WAIT “Bu bölümde kayıtlı personel yok, Devam etmek için Return”
CLOSE kürsör;
RETURN
END IF
DO WHILE .T.
FETCH kürsör
INTO xad,xsoyad,xadres,xmaas;
INTO SQLCODE<>∅
WAIT “Devam için Return”
RETURN
ELSE
CLEAR
@ 10, 10 SAY “ad........” GET xad
@ 11, 10 SAY “soyad........” GET xsoyad
@ 12, 10 SAY “adres........” GET xadres
@ 13, 10 SAY “maas........” GET xmaas
UPDATE Personel
SET ad=xad,soyad=xsoyad,adres=xadres,maas=xmaas
WHERE CURRENT OF kürsör;
END IF
END DO
CLOSE kürsör;
RETURN
PROCEDURE SIL
CLEAR
@ 10, 10 SAY “Bölüm No........” GET b_no
READ
DECLARE kürsör CURSOR
FOR SELECT ad,soyad;
WHERE bol_no=b_no
FOR UPDATE OF ad,soyad;
OPEN kürsör;
IF SQLCNT=0
WAIT “Bölümde kayıtlı personel yok, Devam için Return”
CLOSE kürsör;
RETURN
END IF
DO WHILE .T.
FETCH kürsör
INTO xad,xsoyad;
IF SQLCNT<>0
WAIT “Devam için Return”
RETURN
ELSE
CLEAR
@ 10, 10 SAY “ad........” GET xad
@ 10, 10 SAY “soyad........” GET xsoyad
WAIT “Bu personel silinsinmi E/H” TO T
IF UPPER(T)=”E”
DELETE FROM Personel
WHERE CURRENT OF kürsör;
END IF
END IF
END DO
CLOSE kürsör
RETURN
```

Yukarıdaki programla ilişkili olarak aşağıdaki noktaların açıklanması gerekir:

SQLCNT, SQLCA (SQL Communication Area − SQL haberleşme ve alanı) içinde yer alan bir değişkendir ve tablo içinde bulunan satırların sayısını elde eder. Bu değişkenin ∅ olması durumunda tabloda satır olmadığı (oluşturulan kürsör yapısı ile seçilen erişim kümesinin boş olduğu) sonucu ortaya çıkar.

Önemli diğer bir nokta ise;

```sql
SART DATABASE ISLETME;
```

komutudur.

SQL açısından bir veri tabanı, bir ya da daha çok tablodan oluşan ilişkili bilgiler topluluğudur; DOS ortamından ise bir SQL veri tabanı, bir DOS alt dizinidir. Bu alt dizinin adı, veri tabanının adı ile aynıdır.

Veri tabanı (DOS alt dizini) içindeki her tablo ise ayrı bir veri kütüğüdür, dBASE IV(FOXPRO) ortamında bu tabloların ya d veri tabanı kütüklerinin uzantısı \*.DBF (data base file) şeklindedir.

Bu anlamda START DATABASE ISLETME; komutu, ISLETME adlı veri tabanını kullanma imkanı sağlayan (ISLETME adlı DOS alt dizini içine girişi sağlayan) bir SQL komutudur.

Bu anlamda, programda kullanılan tüm tabloların (Personel v.b.) bu veri tabanı (alt dizin) içinde mevcut olduğu varsayılmaktadır. Bir SQL veri tabanını (DOS içinde bir alt dizin olarak) oluşturmak için SQL’de

```sql
CREATE DATABASE veritabanı adı;
```

komutunu kullanmak gerekir. Mevcut bir SQL veri tabanını silmek içinse

```sql
DROP DATABASE veritabanı adı;
```

şeklinde SQL komutu kullanmak gerekir. Sistemde mevcut olan veri tabanlarının adını görmek içinse

```sql
SHOW DATABASE;
```

SQL komutu kullanılır. Aktif bir veri tabanını iptal etmek içinse

```sql
STOP DATABASE;
```

SQL komutunu kullanmak gerekecektir. Bir veri tabanı içinde bir tabloyu, SQL komutu olan CREATE TABLE yerine XBASE komutu olan CREATE ile oluşturduğunuz takdirde, SQL’in bu \*.DBF’i bir SQL tablosu olarak algılaması için

```sql
DBDEFINE dbf adı;
```

şeklinde SQL komutu kullanmalısınız.

**8.10 Foxpro İçinde SQL Kullanımı**

FOXPRO For Windows 2.5 versiyonu içinde, SQL’in CREATE CURSOR, CREATE TABLE, INSERT ve SELECT komutları yer almaktadır. SELECT ile kullanılabilecek bileşik fonksiyonlar da aynen uygulanır (AVG, COUNT, MAX, MIN, SUM).

dBASE IV’ten farklı olarak, FOXPRO içinde, SQL için ayrı bir modda (SQL .) geçme zorunluluğu yoktur. SQL komutları, diğer FOXPRO komutları gibi hem etkileşimli modda hem de program içinde kullanılabilir.

FOXPRO içinde SQL tablosu ile FOXPRO dbf’i aynı anlamdadır. Gerçekten de

menüsü seçildiği zaman, yeni oluşturulacak kütük seçenekleri içinde, veri tabanı kütüğü (dbf) seçeneği

File Type

Table / DBF

.....

.....

şeklinde yer alır.

FOXPRO’nun etkileşimli modu olan ve dBASE IV’ün . moduna karşı gelen Command penceresinde, daha önceden oluşturulmuş personel.dbf ile ilişkili olarak yazılacak SELECT komutu ile aşağıdaki şekilde bir çıktı elde edilecektir:

Command

```sql
USE Personel
SELECT * FROM Personel;
```

SONUÇ:

Query

Sicil sos\_g\_no ad soyad dog\_tar

117 274521 Ali Can 04/01/62

... ... ... ... ...

FOXPRO’nun program kütükleri için de, SQL komutları, diğer FOXPRO komutları gibi kullanılabilecektir.

**8.11 Microsoft Access İçinde SQL Kullanımı**

Access veri tabanı yönetim yazılımı içinde, veri tabanına erişim amacı ile yapılacak işlemler ve sorgulamalar, sistemde SQL’e dönüştürülür ve uygulanır. Dolayısı ile ACCESS, sorgulama dili olarak tamamen SQL’i kullanır.

Kullanıcı kendi tasarladığı SQL ifadelerini uygulayabilmesi için, ACCESS menüsü içinde View SQL alternatifini seçmesi gerekir. Karşısına çıkacak olan SQL penceresi içinde, SQL komutlarını kullanabilir (Şekil 8.1).

SQL

SQL−Text:

```sql
SELECT * ↑
FROM Personel
WHERE bol_no=2;
```

↓

**Şekil 8.1** ACCESS İçinde SQL Penceresi.

**8.12 Visual Basic’te SQL Kullanımı**

İlişkisel veri tabanlarının sorgulanması, güncellenmesi vb. işlemleri Visual Basic ortamı içinde SQL ile gerçekleştirmek mümkündür. Visual Basic içindeki SQL komutları ve bu komutların yazılış biçimleri Microsoft Access’teki SQL’in aynısıdır. Ayrıca Visual Basic içinde, ODBC yazılımı kullanmakta mümkündür. Visual Basic’te kullanılabilecek SQL sözcükleri (komutları) şunlardır:

ALL LEFT

```sql
DELETE OPTION
DISTINCT ORDER BY
DISTINCTROW OWNERACCESS
FROM PARAMETERS
GROUP BY PROCEDURE
HAVING RIGTH
IN SELECT
INNER TRANSFORM
INSERT UPDATE
INTO WHERE
```

JOIN WITH

Bu listede, daha önce incelenmiş olan sözcükler dışındakiler hakkındaki açıklamalar aşağıda verilmiştir.

**8.12.1 Distinctrow**

SELECT komutu ile elde edilecek çıkışta, tekrar eden hiçbir satır bulunması istenmiyorsa bu sözcük kullanılır.

**ÖRNEK:**
```sql
SELECT DISTINCTROW *
FROM Proje;
```

Euroway 2 ist 2

Euroway 2 ist 2

şeklinde iki aynı satır varsa sadece biri listelenecektir.

**8.12.2 Inner**

İki tabloyu birleştirerek yeni bir tablo elde etmek için kullanılacak birleştirme (join) işleminin bir türünü anlatmak üzere kullanılır. INNER JOIN sözcüklerinin kullanılması, birleştirilecek tablolar içinde birleştirme alanı için sadece ortak veriye sahip olan satırların birleştirilmesini sağlayacaktır.

**ÖRNEK:**

| sicil | ad | soyad | bol\_no |  | bölüm\_ad | bölüm\_no | y\_sos\_g\_n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 257 | Ahmet | Okan | 1 |  | Satış | 1 | 27152 |
| 387 | Veli | Şen | 2 |  | Muhasebe | 2 | 34325 |
| 1117 | Akın | Mert | 1 |  | Teknik | 3 | 72651 |
| 2742 | Ayşe | Meral | 3 |  | Ambar | 4 | 15264 |
| 5574 | Akın | Caner | 2 |  |  |  |  |

şeklinde ise

```sql
SELECT *
FROM Personel,Bölüm
```

Personel INNER JOIN Bölüm

```sql
ON Personel.bol_no=Bölüm.bölüm_no;
```

ifadesi sonucu aşağıdaki sonuç elde edilecektir:

| sicil | ad | soyad | bol\_no | bölüm\_ad | bölüm\_no | y\_sos\_g\_n |
| --- | --- | --- | --- | --- | --- | --- |
| 257 | Ahmet | Okan | 1 | Satış | 1 | 27152 |
| 387 | Veli | Şen | 2 | Muhasebe | 2 | 34325 |
| 1117 | Akın | Mert | 1 | Satış | 1 | 27152 |
| 2742 | Ayşe | Meral | 3 | Teknik | 3 | 72651 |
| 5574 | Akın | Caner | 2 | Muhasebe | 2 | 34325 |

**8.12.3 Left ve Right**

Birleştirme (JOIN) işleminde LEFT sözcüğü kullanılırsa, soldaki tabloda bütün satırlar, sağdaki tabloda müşterek alanla ilişkili hiçbir veri bulunmasa dahi, birleşim tablosuna katılır. RIGHT sözcüğü kullanıldığı takdirde ise, aynı işlem sağdaki tablo için söz konusu olacaktır.

**ÖRNEK:**
```sql
SELECT *
FROM Personel,Bölüm
```

Personel LEFT JOIN Bölüm ON

```sql
Personel.bol_no=Bölüm.bölüm_no;
```

**SONUÇ:** INNER JOIN’deki tablonun aynısıdır

**ÖRNEK:**
```sql
SELECT *
FROM Personel,Bölüm
```

Personel RIGHT JOIN Bölüm

```sql
ON Personel.bol_no=Bölüm.bölüm_no;
```

**SONUÇ:**

| sicil | ad | soyad | bol\_no | bölüm\_ad | bölüm\_no | y\_sos\_g\_n |
| --- | --- | --- | --- | --- | --- | --- |
| 257 | Ahmet | Okan | 1 | Satış | 1 | 27152 |
| 387 | Veli | Şen | 2 | Muhasebe | 2 | 34325 |
| 1117 | Akın | Mert | 1 | Satış | 1 | 27152 |
| 2742 | Ayşe | Meral | 3 | Teknik | 3 | 72651 |
| 5574 | Caner | Caner | 2 | Muhasebe | 2 | 34325 |
|  |  |  |  | Ambar | 4 | 152264 |

**8.12.4 Owneraccess**

Güvenli bir çok kullanıcılı sistemde, WITH OWNERACCESS OPTION sözcükleri, kullanıcıya belirli tablolara erişmek için izin verilmemiş olsa dahi, o tablolardan sorgulama yaparak bilgi edinme imkanı sağlar.

**ÖRNEK:**
```sql
SELECT ad,soyad,maas
FROM Personel
ORDER BY soyad
WITH OWNERACCESS OPTION;
```

Kullanıcıya Personel’e erişim yasaklanmış olsa bile, bu seçenek ile personele ait maaş bilgilerine erişebilir.

**8.12.5 Visual Basic’te Execute Özelliği**

SQL içinde, tablo satırları (ya da veri tabanı kayıtları) üretmeyen SQL komutlarının VISUAL BASIC içinde icra edilmesi için kullanılabilecek bir yöntemdir. Belirtilen SQL komutunu, belirten veri tabanı üzerinde icra eder. Bu anlamda SELECT komutu için geçerli değilidir.

Yazılış Biçimi

```sql
Satırlar = Veritabanı.Execute (SQL deyimi)
```

Satırlar, sayısal bir veri tipi olupdeğeri SQL komutunun etkilediği tablo satırları sayısıdır. Veri tabanı, Visual Basic’te bir veri kontrolünün veri tabanı özelliğidir. Komutlar etkilenecek veri tabanını belirler.

SQL deyimi, veri tabanı üzerinde icra edilecek SQL komutudur.

**ÖRNEK: **
```vbnet
Dim db as Database
Set db=OpenDatabase (“isletme.mdb”)
db.Execute (‘Select * From Personel’)
```

Yukarıdaki örnekte db database olarak tanımlanmış değişkendir. Set ile database’i açma ve db değişkenine database adını atama işlemi yapılır. Execute içersinde yazılan SQL deyimi bu satıra gelindiğinde icra edilir (çalıştırılır).

**8.12.6 Visual Basic’te Database, Dynaset ve Field Nesneleri**

Visual Basic profesyonel yazılımda, DIM ve SET deyimleri kullanılarak herhangi bir nesne türü için, nesne değişkenleri yaratılabilir. Örneğin aşağıdaki program parçası Database, Dynaset ve Field adlı Visual Basic nesneleri için nesne değişkenleri yaratmaktadır. Bu kod içinde SQL’in kullanılışına dikkat ediniz:

```vbnet
Dim VT As Database, Dina As Dynaset, Ala As Field
SET VT=OpenDatabase(“kitap.mdb”)
SET Dina=VT.CreateDynaset(“SELECT * FROM kitaplar”)
SET Ala=Dina.Fields(“Yaz_ID”)
```

**8.12.7 Visual Basic’te Recordset Nesnesi**

Visual Basic’te form üzerine data nesnesi yerleştirilmesi durumunda database ve recordset nesneleri otomatik olarak hazırlanmaktadır. Recordset kayıt seti manasına gelmektedir. Bu kayıt seti kullanılara 1. Bölümden itibaren gördüğümüz SQL komutlarını rahat bir şekilde uygulayabiliriz. Recordset nesnesinin kullanımı konusunda aşağıdaki örnek bizi daha çok aydınlatacaktır.

**ÖRNEK:** Personel tablosunda bulunan ve bölüm numarası 3 olan personeli listeleyiniz (sadece ad, soyad ve bölüm no’su listelenecek).

İsletme.mdb veri tabanı dosyası Microsoft Access’te hazırlanmış olduğunu varsalım.

```vbnet
Dim db as Database
Dim rs as Recordset
Private Sub Command1_Click()
Set db=OpenDatabase(“isletme.mdb”)
Set rs=db.OpenRecordset(“Select * From Personel Where bol_no=2;”)
Text1.text=rs.Fields(“ad”)
Text2.text=rs.Fields(“soyad”)
Text3.text=rs.Fields (“bol_no”)
End sub
```

Yukarıdaki örnektede görüldüğü gibi rs değişkeni db (database) değişkeninin OpenRecordset (kayıt setini aç) özelliğinden yararlanılarak açılır. Bu deyimden sonra gelen SQL sorgusuna eşit olan bütün kayıtlar bu kayıt setine atılır ve bu kayıtların kontrolü burdan yapılır. Text alanlarına ad, soyad ve bol\_no yazılır. Fakat birden çok kayıtın bulunduğu takdirde en son kayıt görüntülenir. Bunu engellemek için recordset nesnesinin MoveNext, MoveLast, MovePrevious, MoveFirst gibi bir çok nesnesinden yararlanarak bu kayıtlar görüntülenir. Recordset nesnesinin bir çok özelliği ve SQL sorgulamaları ile veri tabanı işlemleri çok basite indirgenmiş olur.

Eğer veri tabanındaki tablomuzda herhangi bir alana veri yüklemek içinde recordset nesnesi kullanılabilir.

**ÖRNEK:**
```vbnet
Set rs=db.OpenRecordset (“Select * From Personel”)
rs.Fields (“ad”)=text1.text
rs.Fields (“soyad”)=text2.text
rs.Fields (“bol_no”)=Val(text3.text)
```

Yukarıdaki örnekte ad, soyad ve bol\_no alanlarına text alanlarındaki bilgiler aktarılır. Val komutu Visual Basic’e ait bir fonksiyondur.

**NOT:** SQL deyimi yazılan kısımda Visual Basic ve SQL konusunda var olan bütün komutlar veya deyimler kullanılır.

**NOT: **Set deyimi kendisinden sonra gelen değişkene değer aktarır (= işaretinden sonraki deyimi).

**BÖLÜM 9**

**ERİŞİM KONTROLÜ ve SİSTEM GÜVENLİĞİ**

**9.1 Giriş**

Veri tabanına erişim kontrolü ve sistem güvenliğinin sağlanması, en önemli konulardan biridir.

Kim hangi bilgilere erişebilecektir; ne kadarına erişebilecektir?

Kim, hangi bilgiler üzerinde değişiklik yapma ve bilgileri silme hakkına sahiptir?

Veri tabanlarına çok sayıda kullanıcı tarafından erişilebilen ortamlarda, bu erişimin kontrolü son derece önemlidir.

Bu bölümde konu ile ilişkili temel kavramlar anlatılacak ve SQL’de gerekli komutlar ve kullanılış biçimleri örneklerle verilecektir.

**9.2 Veri Tabanı Nesnelerinin Güvenliğinin Sağlanması**

Bu bölümde veri tabanı ortamında, değişik tipteki kullanıcılar, ORACLE terminolojisi ile anlatılacaktır. Fakat buradaki prensipler hemen hemen bütün sistemlerde benzer şekilde uygulanmaktadır.

ORACLE veri tabanı yönetim sisteminin kontrol ettiği veri tabanı ortamında, dört farklı türde kullanıcı vardır.

Sistem kullanıcısı (System User) tüm veri tabanı ortamına hükmedebilen kullanıcıdır. Veri tabanı yöneticisinin (DBA-Data Base Administrator) üstündedir. Sisteme, yeni kullanıcıları dahil edebilir; bir veya daha fazla kullanıcıya veri tabanı yöneticisi yetkisi verebilir. Kullanıcıların parolalarını değiştirebilir. Sistem kullanıcısı ayrıca, ORACLE veri tabanı sözcüğünü değiştirebilir.

Veri tabanı yöneticisi yetkisine sahip olan kullanıcılar, yeni kullanıcıların sistemde çalışmaya başlamaları için gerekli koşulları ve yeni kullanıcıların ayrıcalıklarını belirleme, kullanıcıların çalışmalarına son verme ve ORACLE veri sözcüğü yetkilerine sahiptir.

CONNECT ve RESOURCE ayrıcalıkları verilen kullanıcıları, veri tabanına bağlanabilirler, yeni tablolar ve indeksler yaratabilirler.

Sadece CONNECT ayrıcalığına sahip olan kullanıcılar, sadece mevcut tablolara erişebilirler fakat kendi tablolarını yaratamazlar.

**9.3 Yeni Kullanıcılar Yaratma ve Kullanıcılara Ayrıcalık Verme**

ORACLE ilk yüklendiği (install) zaman SYSTEM/MANAGER statülü kullanıcı otomatik olarak yaratılır. İlk olarak, sistem kullanıcısı default parolayı değiştirmelidir. Daha sonra sistem kullanıcısı tarafından diğer kullanıcılara ayrıcalıkları ve kullanıcı tipleri aşağıdaki komutlarla verilir:

```sql
GRANT DBA to Mert
GRANT DBA to Mitat
GRANT RESOURCE, CONNECT to Beril
GRANT CONNECT to Mehmet
GRANT CONNECT to Ali
GRANT CONNECT to Cem
```

Mert ve Mitat adlı kullanıcılar veri tabanı yöneticisi, Beril adlı kullanıcı CONNECT ve RESOURCE ayrıcalıklı, Mehmet, Ali ve Cem ise CONNECT ayrıcalıklı olarak tanımlanmaktadır.

Verilen bir ayrıcalığı iptal etmek içinse REVOKE komutu kullanılır.

REVOKE CONNECT to Ali komutu ile Ali’ye daha önceden verilen veri tabanına bağlanma (CONNECT) ayrıcalığı iptal edilmektedir.

Bir tabloyu yaratan kişi o tablonun sahibi (owner) olarak kabul edilir. Eğer tablonun sahibi tarafından yetki verilmemişse, tabloya başka hiç kimse erişemez. Tablo sahibi tarafından, tabloya erişim, tabloda değişiklik yapma gibi değişik ayrıcalıklar, GRANT komutu ile diğer kullanıcılara verilebilir. Örneğin aşağıdaki komut, bütün kullanıcılara personel adlı tabloya erişip bilgi dökme (SELECT), satır ekleme (INSERT), tabloda değişiklik yapma (UPDATE), satır silme (DELETE), tablonun yapısında değişiklik yapma (ALTER), indeksleme (INDEX) ve kümeleme (CLUSTER) yetkilerini vermektedir.

```sql
GRANT SELECT, INSERT, UPDATE
DELETE, ALTER, INDEX, CLUSTER
ON Personel
TO PUBLIC;
```

Bu komutu daha kısa şekilde aşağıdaki gibi yazmak mümkündür:

```sql
GRANT ALL
ON Personel
TO PUBLIC;
```

Ahmet isimli kullanıcıya personel ve proje tabloları üzerinde sadece SELECT yetkisi verilmek istenirse, aşağıdaki GRANT komutunu yazmak gerekecektir:

```sql
GRANT SELECT
ON Personel, Proje
TO Ahmet;
```

**9.4 View’lerle İlişkili Güvenlik İşlemleri**

** **GRANT komutu, tabloların kullanımı ile ilişkili kısıtlamalar getirmektedir. View’ler, tabloların belirli sütunları ile oluşturulabildiği için, view oluşturma sayesinde, tablonun sütunları (alanları) bazında da kullanım kısıtlaması dolayısıyla güvenlik önlemi getirilebilir.

Örneğin, personel ilişkili tüm bilgilerin saklandığı Personel tablosunda, maaşlarda bulunduğu için yönetim açısından bu tabloyu tüm kullanıcıların erişmesine olanaklı kılmak mahsurludur. Öte yandan, çalışan personel ile ilişkili diğer bilgiler, işletmenin her bölümünde pek çok çalışan tarafından çeşitli zamanlarda ihtiyaç duyulabilir.

Bu durumda en uygun yol, personelle ilişkili, maaşlar hariç tüm bilgilerin bulunduğu bir View oluşturmak ve bunun bütün kullanıcıların erişimine açmaktır. Aşağıdaki komutlarla bu işlem yapılmaktadır:

```sql
CREATE VIEW genpers
AS
SELECT sicil,sosy_g_no,ad,soyad,
```

dogum\_tar,adres,cinsiyet,bol\_no,yon\_s\_g\_n

```sql
FROM Personel;
GRANT SELECT
ON genpers
TO PUBLIC;
```

Böylece, genpers adlı VIEW herkesin erişimine açılarak, personel tablosu ise sadece belirli kişilerin kullanımına açık tutularak, fiilen, personel tablosunun maas alanı üzerinde bir işlem yasağı oluşturulmuştur.

Pratikte bir işletmede, her bölümün yöneticisine, sadece o bölümdeki maaşları bilme ve gerekirse maaşlarda değişiklik yapabilme yetkisinin verilmesi gerekir.

Bunun sağlanması için, personel tablosundan her bölümle ilişkili olarak bir view oluşturmak ve bu viewler üzerinde yöneticiye inceleme yapmak ve maaş üzerinde değişiklik yapmak yetkisinin verilmesi uygun bir çözüm olacaktır. Örneğin, mühendislik bölüm numarası 2 ise

```sql
CREATE VIEW mühendis
AS
SELECT *
FORM Personel
WHERE bol_no=2;
GRANT SELECT, UPDATE (maas)
ON mühendis
TO müh_yönet;
```

Mühendislik bölümü yöneticisinin sistemdeki kullanıcı adı (user\_id) müh\_yönet ise, bu yöneticiye, mühendis adlı, sadece mühendislik bölümündeki personeli içeren view üzerinde, inceleme yapma ve maas alanında değişiklik yapma imkanı verilmektedir.

Her kullanıcıya, sadece kendi bilgilerini inceleyip diğerlerini inceleyememesi şeklinde bir kısıt konulmak istenirse aşağıdaki yol izlenebilir:

```sql
CREATE VIEW özel
AS
SELECT Personel
WHERE sicil=USER;
GRANT SELECT
ON özel
TO PUBLIC;
```

Burada, o andaki kullanıcının kullanıcı isminin sicil ile belirlendiği varsayılıyor. USER bir ORACLE sistem değişkenidir; o esnada sistemde bulunan (logon yapmış) kullanıcının, user\_id’sini (kullanıcı belirleyicisi) saklamaktadır.

**9.5 Veri Tabanı Ortamındaki İşlemlerin İzlenmesi**

ORACLE veri tabanı yönetim yazılımı, diğer pekçok benzer yazılım gibi, tablo sahibi kullanıcılar, tablolarına erişim teşebbüsleri ile ilgili ve tablolar üzerinde gerçekleştirilen işlemlerle ilgili döküm ve bu işlemleri izleme imkanı verir. Ayrıca, veri tabanı yöneticisine ise, tüm sistem için, aynı olanak verilmiştir; ayrıca veri tabanı yöneticisi sisteme girme (log on) teşebbüsleri ile ilgili bilgileride izleyebilir.

Örneğin veri tabanı yöneticisinin personel tablosu üzerinde tablodaki verileri ya da tablonun yapısını değiştirmekle ilgili teşebbüsleri incelemek istediğini düşünelim. Bunu gerçekleştirmek için AUDIT komutunu aşağıdaki gibi kullanmak durumundadır:

```sql
AUDIT INSERT, UPDATE, DELETE, ALTER
ON Personel
BY ACCESS;
```

izleme işlemini sona erdirmek içinse NOAUDIT komutu kullanılır:

```sql
NOAUDIT INSERT, UPDATE, DELETE, ALTER
ON Personel
BY ACCESS;
```

ORACLE, veri tabanı yöneticilerine, denetim imkanlarını genişletmek için aşağıdaki yetkileride vermiştir:

CONNECT ORACLE veri tabanı sistemine log on teşebbüslerini görüntüler.

DBA Sistem çapındaki GRANT, REVOKE, AUDIT ve NOAUDIT deyimlerini ve ayrıca CREATE/ALTER PARTITION, CREATE/DROP PUBLIC SYNONIM deyimleri izler.

NOT EXISTS Tablolara erişim esnasında does not exists (mevcut değil) hata mesajı alınan erişimleri görüntüler.

RESOURCE CREATE/DROP TABLE, VIEW, SPACE, SYNONIM deyimlerini, CREATE/ALTER/DROP CLUSTER deyimlerini izleme imkanı sağlar.

**ÖRNEK:**
```sql
AUDIT DBA
ON DEFAULT
BY ACCESS;
```

**ÖRNEK:**
```sql
AUDIT NOT EXISTS
ON Personel
BY ACCESS;
```

**BÖLÜM 10**

**HAREKET YÖNETİMİ**

**10.1 Temel Kavramlar**

Hareket yönetimi (transaction management) bir veri tabanı yönetim sistemindeki en önemli işlemlerden biridir. Hareket yönetiminin SQL komutları ile nasıl gerçekleştirilebileceği bu bölümün konusunu teşkil edecektir.

**Hareket (transaction)**

SQL’de bir hareket, ‘veri tabanı üzerinde çeşitli fonksiyonları gerçekleştiren bir işlemler dizisi’ olarak tanımlanır. Bu tanım çerçevesinde, işlemler dizisi, çok sayıda birbirini izleyen SQL komutlarından ya da SQL’in katılımlı kullanılması durumda üst dil komutlarından oluşur.

Veri tabanında mevcut olan par\_sat adlı tabloda, satıcı numarası (sat\_no), parça numarası (parca\_n) ve miktar (miktar) sütunları mevcuttur. Şimdi S1 satıcısından P1 parçasından 500 tane talep edilmiş olsun. Stoktan talep etme hareketi olarak nitelendirebileceğimiz bu hareket için aşağıdaki işlemlerin gerçekleştirilmesi gerekecektir:

S1 satıcısının P1 parçasını satıp satmadığını kontrol etmek.

S1 satıcısı P1 parçasını satıyorsa, talep edilen miktarı, tablodaki miktarla mukayese ederek talebi karşılayıp karşılamadığını kontrol etmek.

Talep karşılanabiliyorsa, par\_sat üzerinde S1 satıcısının P1 parçasının miktar alanından 500 eksilterek güncelleme yapmak.

Stok talebi hareketini aşağıdaki gibi bir akış diyagramı ile ifade etmek mümkündür:

Hayır Hayır **Şekil 10.1** Hareket Akış Diyagramı.

Hareket başarılı ise (istenilen değişiklikler yapılmış ise) veri tabanının yeni durumu hareketten önceki durumundan farklı olacaktır. Bunu aşağıdaki diyagram ile daha açık görmek mümkündür:

Evet Hayır

**Şekil 10.2** Hareket ve Veri Tabanı Durumu İlişkisi.

**Eski duruma dönme (recovery)**

** **Bir hareket içinde herhangi bir işlem başarısızlıkla sonuçlanmışsa, o hareket içindeki işlemlerden bazıları tarafından veri tabanı üzerinde gerçekleştirlmiş değişiklikler iptal edilmeli ve veri tabanı hareketin başlamasından önceki duruma dönmelidir.

**Aynı zamanda çok sayıda işleme (eşzamanlılık-concurrency)**

Aynı zamanda birden çok hareket aktif halde olabilir. bu hareketlerden bazıları aynı anda veri tabanı üzerindeki aynı alanlara erişip değişiklik yapmak isteyebilir. Veri tabanı yönetim sisteminin bu durumu kontrol etmesi zorunludur.

**10.2 Hareket Yönetiminin Gerçekleştirilmesi**

Bir işlemler dizisinden oluşan bir hareketle, işlemlerin tümü başarılı ise veri tabanının durum değişikliğinin kalıcı hale getirilmesi, işlemlerden biri bile başarısız ise değişikliklerin reddedilerek veri tabanının hareketten önceki durumuna dönüştürülmesi şeklindeki hareket yönetimini gerçekleştirmek için iki yaklaşım vardır:

Standart olmayan yöntem

Bu yöntemde, hareketi oluşturan işlemlerle ilişkili komutlar BEGIN ve END

TRANSACTION komutları arasına alınır.

```sql
BEGIN TRANSACTION;
komut 1;
komut 2;
```

- Hareketi oluşturan komutlar

-

```sql
komut n;
END TRANSACTION;
```

ANSI standardı

Buna göre aşağıdaki yapı kullanılacaktır:

```sql
komut 1;
komut 2;
```

- Hareketi oluşturan komutlar

-

```sql
komut n;
COMMIT
```

Standart metod kullanıldığına göre, bir hareket, ilk rastlanılan SQL komutu

ile başlar ve aşağıdaki komut ya da olaylardan biri ile karşılaşınca sona erer:

```sql
COMMIT
ROLLBACK
```

Herhangi bir veri tanımlama dili

```sql
(Data Definition Language-DDL)
```

komutu

Hata koşulu

Sistemden çıkılması (logoff)

Sistemden normal olmayan çıkış

Bir işlemler dizisinden oluşan hareket sona erince, bir sonraki SQL komutu otomatik olarak devreye girer.

**10.3 Commit ve Rollback Komutları**

Bir hareketi oluşturan komutların sonunda COMMIT komutu kullanılmışsa, bu hareketin veri tabanı üzerinde oluşturduğu değişiklikler sistem tarafından kalıcı hale getirilir.

Hareketi oluşturan komutlar sonunda ROLLBACK komutu kullanılmışsa, gerçekleştirilen değişikliklerin tümü iptal edilecek ve veri tabanı, hareketten önceki durumuna dönecektir.

**ÖRNEK:**
```sql
UPDATE Personel
SET maas=27000000
WHERE sicil=27115;
INSERT INTO Bölüm (bölüm_ad,
```

bölüm\_no,y\_sos\_g\_n,y\_is\_b\_tar)

```sql
VALUES (‘halkla ilişkiler’,7,’27141527’,{01/05/93});
COMMIT
```

Bu örnekte, personel tablosunda sicili 27115 olan kişinin maaşı 27000000 yapılmakta ve bölüm adlı tabloya ise, halkla ilişkiler adlı yeni bir bölüm, bölüm numarası, yöneticinin sosyal güvenlik numarası ve yöneticisinin işe başlama tarihi yeni bir satır olarak yüklenmektedir.

Yukarıda açıklandığı gibi, COMMIT komutuna kadar görülen SQL komutları ANSI standart yönetimine göre bir hareket kabul edilecekler COMMIT ile bu komutlarca veri tabanında gerçekleştirilen değişiklikler kalıcı hale getirilecektir.

COMMIT yerine ROLLBACK kullanılsa idi, o takdirde yapılan değişiklikler iptal edilecek ve veri tabanında bu hareketten dolayı bir değişme görülmeyecekti.

**10.4 Eşzamanlı Erişimler İçin Kilitleme Yöntemi – Lock Table Komutu**

Farklı veri tabanı yönetim sistemleri dolayısıyla bunlar içindeki SQL gerçekleştirimleri, veri tabanı içindeki tablo sütunlarına aynı zamanda erişim ve güncelleme taleplerini farklı şekilde kontrol etmektedirler. Pekçok SQL gerçekleştiriminde mevcut olan LOCK TABLE adlı SQL komutu, kullanıcıya, kısıtlı bir zaman dilimi içinde bir veya daha fazla tabloyu tek başına, özel olarak kullanma imkanı vermektedir. Bu komutun yazılış biçimi aşağıdaki gibidir:

LOCK TABLE tablo ya da view adı IN

```sql
SHARE | EXCLUSIVE MODE
```

SHARE MODE seçeneği kullanılırsa, diğer kullanıcılar tablo ya da view üzerinde sadece okuma işlemi (SELECT) yapabilirler; silme ya da güncelleme yapamazlar.

SHARE ile kilitlenmiş bir tabloyu aynı anda çok sayıda kişi kullanabilir. (Bir kullanıcı her türlü hakka sahip olabilir; diğerleri sadece okuma yapabilir.(Şekil 10.3))

Sadece okuma

Tabloyu SHARE yapabilen diğer

Mode’da kullanıcılar

kilitleyen kullanıcı

```sql
Güncelleme (Update)
Silme (Delete) yapabilir.
```

**Şekil 10.3** LOCK TABLE (Tablo Kilitleme) Komutunun SHARE MODE (paylaşımlı mod) da Kullanımı.

LOCK TABLE komutu, EXCLUSIVE MODE’da kullanılırsa, diğer kullanıcılar gene tabloda herhangi bir değişiklik yapamazlar; tabloda sorgulama yapabilirler fakat tablo üzerinde herhangi bir kilitleme (LOCK TABLE) işlemine girişmelerine müsaade edilmezler. (SHARE MODE ile aradaki en önemli fark budur (Şekil 10.4))

Sadece okuma yapabilen diğer

```sql
Tabloyu EXCLUSIVE kullanıcılar.
```

MODE’da Bunlar tablo

kilitleyen kullanıcı üzerinde kilitleme - Güncelleme (Update) işlemine de teşeb-

```sql
- Silme (Delete) yapabilir. büs edemezler.
**Şekil 10.4** LOCK TABLE (Tablo Kilitleme) Komutunun EXCLUSIVE MODE
```

(Özel Mod) da kullanımı.

Her iki tür kilitleme komutunun da, tablo üzerindeki kilitleme etkisi, tabloyu kilitleyen kullanıcının bir COMMIT ya da ROLLBACK komutunu kullanması ile sona erer.

Sistem bir tabloyu kilitlemeye teşebbüs etmeden önce, o tablo üzerinde herhangi bir kullanıcının EXCLUSIVE MODE’da bir LOCK TABLE işlemi uygulayıp uygulamadığını kontrol eder.

**10.5 Kilitleme Yönteminin Sakıncaları**

Tablolar üzerinde kilitleme yönteminin uygulanmasının çeşitli sakıncaları olabilir.

Bunlardan ilk başta geleni, sistemdeki bazı kullanıcıların bir veya daha fazla tablo üzerinde uzun süre kilitleme işlemi uygulayarak tabloları tekeline alması ve dolayısıyla sistemin genel performansını düşürmesidir.

İkinci ve çok daha ciddi olan sakınca ise çıkmaza girme (deadlock) olayının meydana gelmesidir.

Çıkmaza girme aşağıdaki şekilde oluşur:

A kullanıcısı X tablosunu EXCLUSIVE olarak kilitlemiştir. Bir sonraki işlem adımında ise Y tablosuna erişmek istemektedir. Aynı anda ise, B kullanıcısı Y tablosu üzerinde Y tablosu üzerinde EXCLUSIVE kilitleme yapmıştır ve X tablosuna erişmek istemektedir. (Şekil 10.5)

A, X’i B, Y’yi

```sql
EXCLUSIVE EXCLUSIVE
```

olarak olarak

kilitlenmiştir. kilitlemiştir.

** Şekil 10.5** Çıkmaza Girme (Deadlock) Durumunun Oluşması.

Çıkmaza girme durumu, herhangi bir müdahale olmazsa, sonsuza kadar bekleme ile sonuçlanacaktır.

Sistem tarafından, çıkmaza girme durumu, kullanıcılardan birini bir anlamda feda ederek ortadan kaldırılabilir.

ORACLE veri tabanı yönetim sisteminde, çıkmaza girme durumu sistem tarafından otomatik olarak tespit edilir ve sistem tarafından ortadan kaldırılır.

Ortadan kaldırma şu şekilde olur: Sistem, çıkmazı oluşturan komutları analiz ederek bunlardan birine ROLLBACK işlemi uygulayarak, o komutu kullanan kullanıcının yarattığı kilitlenmeyi ortadan kaldırır.

**10.6 Otomatik Kilitleme**

Bazı veri tabanı yönetim sistemleri, tablonun değişimine sebebiyet verecek herhangi bir komut (INSERT, UPDATE, DELETE) uygulandığı zaman, o tablo üzerinde otomatik olarak EXCLUSIVE kilitleme oluşturur. Bu kilitleme herhangi bir COMMIT ya da ROLLBACK komutu ile ortadan kalkacaktır.

**ÖRNEKLER:**

```sql
LOCK TABLE X IN SHARE MODE;
```

X tablosu SHARE MODE’da kilitleniyor. Diğer kullanıcılar sadece okuma yapabilir.

```sql
LOCK TABLE Y IN EXCLUSIVE MODE;
```

Y tablosu EXCLUSIVE MODE’da kilitleniyor. Diğer kullanıcılar sadece okuma yapabilir ve Y tablosu üzerinde kilitleme yapamazlar.

**KAYNAKLAR**

SQL, The Standart Handbook, Stephan Cannon, Gerard Otten, Mc Graw Hill Book Comp., 1993

Introduction to Oracle, M. Bronzite, Mc Graw Hill Book Comp., 1993

```sql
An Introduction to Database System, Volume I, C. J. Date, 1990
```

Visual Basic für DOS, Peter Manodjemi, Addison-Weley, 1993

DBase III-IV Programlama, Mithat Uysal, Murat Tunç, Beta Yay., 1994

Foxpro für Windows, W. Schottler, Addison Wesley, 1993

Das Microsoft Access, R. Albrecht, N. Nicol, Addison Wesley, 1993

SQL Veri Tabanı Sorgulama Dili, Mithat Uysal, Beta Yay., 2000

PAGE 1

PAGE 50

File

Ne

Hareket Başlat

S1 satıcısı

P1 parçası satıyor mu?

P1’in miktarı 500 ya da daha fazla mı?

Hareket sonu

Veri tabanı

t anı

Veri tabanı

t+∆t anı

Hareket Başarılı

```sql
Tablo veya view
Tablo veya view
```

X

Tablosu

Y

Tablosu

1. Kullanıcı

2. Kullanıcı

```sql
View X
View Y
```

Temel Tablo

Personel

Temel Tablo

```sql
Proje
```

Temel Tablo

Bölüm

---
*Kaynak: `BİR VERİ TABANININ OLUŞTURULMASI/BİR VERİ TABANININ OLUŞTURULMASI.doc` — ertuğrul — 2004*
