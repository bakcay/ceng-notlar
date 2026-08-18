# Veri Tabani Sorulamalari

**INDEX******

**1. **TEK TABLODAN SORGULAMALAR
**---SELECT \* FROM Tablo
---SELECT \* DISTINCT FROM Tablo
**
**2. **TABLO BİLGİLERİNİN SIRALANMIŞ OLARAK LİSTELENMESİ**
---ORDER BY
---ORDER BY ASC DSC
**
**3. **BİRDEN ÇOK ALANA GÖRE SIRALAMA**
---SELECT alan1, alan2 FROM Tablo ORDER BY alan1
****
****--- **KOŞULA BAGLI OLARAK LISTELEME**
-----WHERE
****
****--- **KARŞILAŞTIRMA OPERATÖRLERi**
-----ÇEŞİTLİ VERİ TİPLERİ için BASİT SORGULAMALAR
---------1.NÜMERİK VERİ TİPLERİ
---------2.KARAKTER VERİ TİPLERİ (CHAR)
---------3.TARİH VERİ TİPİ (DATE)
---------4.MANTIKSAL VERİ TİPİ******

**4. **BİRDEN ÇOK KOŞULA DAYALI SORGULAMALAR (NOT / AND / OR)**
****
****--- **BİR VERİ KÜMESİNDE ARAMA -IN OPERATÖRÜ**
******

**--- **BETWEEN SORGULAMA SÖZCÜĞÜ**
******

**--- **KARAKTER TÜRÜ BİLGİ İÇİNDE ARAMA YAPMA -LIKE SÖZCÜĞÜ**
****
****5. **SQL’DE ARİTMETİKSEL İFADELER VE FONKSİYONLAR**
---SUM FONKSİYONU
---AVG FONKSİYONU
---MAX FONKSİYONU
---MIN FONKSİYONU
---COUNT FONKSİYONU
****
****6. **GRUPLANDIRARAK İŞLEM YAPMAK**
---GROUP BY
---HAVING
**

**--- **BİRDEN FAZLA TABLOYU İLİŞKİLENDİRMEK (JOIN)**
---SELF-JOIN
--- **NESTED SELECTS (İÇİÇE SEÇİMLER)**
******

**--- **UNION SÖZCÜĞÜ**
******

**----- **-KOŞULLAR **
---------ANY / ALL / EXISTS / NOT EXISTS
---------EXCEPT / INTERSECT / SAVE TO TEMP / KEEP

7. **TABLOLARDA DEĞİŞİKLİK YAPMAK**
--- **INSERT INTO tablo VALUES değerler**
******

**--- **DELETE FROM tablo WHERE alan = 1**
******

**--- **UPDATE tablo SET alan = alan \* 2**
******

**--- **CREATE INDEX ON tablo**
------ **TEK BİR ALANA GÖRE ARTAN SIRADA İNDEKSLEME **
******

**------ **TEK BİR ALANA GÖRE AZALAN SIRADA İNDEKSLEME**
******

**------ **BİRDEN FAZLA ALANA GÖRE İNDEKSLEME **
-----------UNİQUE SÖZCÜĞÜ
------MEVCUT BİR İNDEKSİN SİLİNMESİ
**

**--- **TABLONUN YAPISINDA DEĞİŞİKLİK YAPMAK**
------ALTER TABLE
-----------ADD KOMUTU (MEVCUT BİR TABLOYA ALAN (FIELD) EKLEMEK)
****-----------MODIFY KOMUTU (MEVCUT BİR TABLONUN ALANLARINDA DEĞİŞİKLİK YAPMAK)
****-----------DROP KOMUTU (MEVCUT BİR TABLODAN BİR ALAN SİLMEK)
-----------RENAME KOMUTU (MEVCUT BİR TABLONUN ADINI DEĞİŞTİRMEK)
-----------DROP TABLE (MEVCUT BİR TABLONUN TÜMÜYLE SİLİNMESİ)
******

**--- **CREATE VIEW (VERİ GÜVENLİĞİ)**
------WITH CHECK OPTION
------EKLEME
------DELETE
------UPDATE
------DROP
**

**8. **DAHA FAZLA ÖRNEK VE AÇIKLAMA

**1. TEK TABLODAN SORGULAMALAR:
**
**SELECT \* FROM** tablo

**ÖRNEK:** Bütün bilgileri personel tablosundan koşulsuz olarak listele.
**SELECT \* FROM personel **

**ÖRNEK**: Personel tablosundan SEÇ komutuyla istenen sütun adlarını belirt.
**SELECT sicil, sosy\_g\_no, ad, soyad, dog\_tar, sicil,sosy\_g\_no,ad,soyad,dog\_tar, adres, cins, brüt, böl\_no, yön\_s\_g\_n FROM personel; **

**ÖRNEK**: Personel tablosundan istenen sütün başlıklarını listele.
**SELECT sicil, ad, soyad, brüt FROM personel;
**
**DISTINCT (Tekrarsız)**

**TANIM**: SQL’de tablo içinde birbirinin aynı datalar bulunabilir. Aynı satırların listeleme esnasında bir kez yazılması için Distinct sözcüğünü kullan.

**ÖRNEK**: Par \_sat dosyasından sat\_no’lar tekrarsız olarak listelenecektir.
**SELECT DISTINCT sat\_no FROM par\_sat; ****
**
**2. TABLO BİLGİLERİNİN SIRALANMIŞ OLARAK LİSTELENMESİ:**

**ORDER BY **(Sırasıyla)
**TANIM**: Tablodaki sütunlardan ,belirli bir sütuna göre listelemek için SELECT komutuna , ORDER BY eklenir.
**ÖRNEK**: Personel dosyasından, sicil, ad, soyad, brüt sütunlarını seç ve brüt (maaşa) göre büyükten küçüğe sırala.

**SELECT sicil, ad, soyad, brüt FROM personel ORDER BY brüt ASC;
**
**DESC** : Küçükten büyüğe sırala (A-Z) **ASC **: Büyükten küçüğe sırala (Z-A)
DESC yazılmazsa ASC direct kabul edilir (DEFAULT)

**3. BİRDEN ÇOK ALANA GÖRE SIRALAMA:****
**
**TANIM**: Bir tablo içinde ,birden fazla sütundan aynı anda sıralamak için kullanılır.
**ÖRNEK**: Personel dosyasından seçilen sütunlarını aynı anda hem ad, hem de otomatik olarak sıralar.

**SELECT sicil, ad, soyad, brut FROM personel ORDER BY ad, brut;
**
**ÖRNEK **Personel tablosundan seçili sütunları öncelik adda olmak üzere (Z-A) adı bozmadan soyadı (A-Z) sıralı listeler.

**SELECT sicil, ad, soyad, brut FROM personel ORDER BY ad ASC, soyad DESC, brut ASC; **
veya;
**SELECT sicil, ad, soyad, brut FROM personel ORDER BY ad, soyad DESC, brut;
**

**KOŞULA BAGLI OLARAK LISTELEME:**
**WHERE ****
TANIM**: verilen koşulu sağlayanlar listelenir. İki veri birbiriyle karşılaştırılmaktadır. Karşılaştırılan verilerin türü aynı olmalıdır.

**SELECT \* FROM personel WHERE brüt > 5000000;

****KARŞILAŞTIRMA OPERATÖRLERI:****

****OPERATÖR ANLAMI :**

| < ...den daha küçük > ...den daha büyük = Eşit | <= Küçük veya eşit >= Büyük veya eşit <> Eşit değil | != Eşit değil !< ... den küçük değil !> ... den büyük değil |
| --- | --- | --- |

**
****ÇEŞİTLİ VERİ TİPLERİ İÇİN BASİT SORGULAMALAR:**
**1. NÜMERİK VERİ TİPLERİ:**

**ÖRNEK**: Maaşı 8000000TL’den fazla olmayan personeli listele.

**SELECT \* FROM personel WHERE brüt <= 8000000; **

**2. KARAKTER VERİ TİPLERİ (CHAR):**
Karakter çift veya tek tırnak ile gösterilir.

**ÖRNEK**: Adı Ali olmayan personele ait kayıtları listele.
**SELECT \* FROM personel WHERE ad <> “Ali”;
**
**3. TARİH VERİ TİPİ:**
Tarih VERİ TİPLERİ { } sembolleri içinde yazılır.
**ÖRNEK**: Hangi personelin doğum tarihi 1960 yılından daha öncedir?

**SELECT \* FROM personel WHERE dog\_tar <={12/31/59};
**
**4. MANTIKSAL (LOJİK) VERİ TİPİ:**

Mantıksal veriler için mümkün olabilen sadece iki değer söz konusudur. DOĞRU D (TRUE T), YANLIŞ Y (FALSE F) ile simgelenir.

**ÖRNEK:** Personel tablosunda personelin cinsiyetini belirten cins adlı alan mantıksal (logical) olarak tanımlanmıştır. Cinsiyeti erkek olanları D, kadın olanları y ile tanımlarsak erkek olanları listele.

**SELECT \* FROM personel WHERE cins = .T.; ****
**
**4. BİRDEN ÇOK KOŞULA DAYALI SORGULAMALAR: (NOT, AND, OR)**
**TANIM**: Mantıksal operatörlerin yardımı ile birden çok koşulun gerçekleştirmesine bağlı olarak ifade edilebilecek (karmaşık yada birleşik koşullu listelemeleri gerçekleştirilmektedir.)

**AND (VE)**
**ÖRNEK**: Maaşı 5000000’dan fazla olan ve cinsiyeti erkek olan personelin listelenmesi istenir yani iki koşul verilmektedir ve ikisinin de olması istenir.

**SELECT \* FROM personel WHERE brüt >5000000 AND cins =.T.;
**
**NOT (DEĞİL)
OR (VEYA**)

**ÖRNEKLER:**
1. Doğum tarihi 1960’dan önce olan maaşı 6000000 - 10000000 arasındaki bayan personelin listele.

**SELECT \* FROM dog\_tar < {01/01/60} AND brüt > = 6000000 AND brüt < =10000000
AND cins = .F.; **

2. Satış bölümüyle muhasebe bölümündekiler kimlerdir?
(Satış bölümünün böl\_no’sunun 1 ve muhasebe bölümünün böl\_no’sunun 2 olduğu varsayılmaktadır.)

**SELECT \* FROM personel WHERE bol\_no =1 OR bol\_no = 2;
**3. Bölümü Satış yada Muhasebe olamayan 1960’dan sonra doğmuş bayan personeli listele.

**1.YAZILIM:
****SELECT \* FROM personel WHERE NOT (böl\_no =1 OR böl\_no =2) AND dog\_tar > ={01/01/60}
AND cins =.F.; **
**2.YAZILIM:
****SELECT \* FROM personel WHERE böl\_no <> 1 AND böl\_no <> 2 AND dog\_tar > ={01/01/60}
AND cins =.F.;
**
**BİR VERİ KÜMESİNDE ARAMA -IN OPERATÖRÜ
**
**IN (içinde**)
“IN” operatörü NOT ile kullanılabilir.

**ÖRNEK:** Bölümü 1,2,3 olmayan personel kimlerden oluşmaktadır?
**SELECT \* FROM personel WHERE bol\_no NOT IN (1,2,3); **

**ÖRNEK:** Böl\_no’su 1, 2 yada 3 olan personeli listele.
**SELECT \* FROM personel WHERE böl\_no = 1 OR böl\_no= 2 OR böl\_no = 3; **

Bu örneğin IN ile yapılmış şekli daha kısadır.

**SELECT \* FROM personel WHERE NOT böl\_no IN (1,2,3); **

**BETWEEN SORGULAMA SÖZCÜĞÜ:****
**
**BETWEEN (ARASINDA**)
**ÖRNEK**: Maaşı 5 - 10 milyon arasında olan personel kimlerdir?

**SELECT \* FROM personel WHERE brüt > =5000000 AND brüt < = 10000000; **

BETWEEN (ARASINDA) komutu ile daha kısa olacaktır.

**SELECT \* FROM personel WHERE brüt BETWEEN 5000000 AND 10000000; **

**KARAKTER TÜRÜ BİLGİ içinde ARAMA LIKE SÖZCÜĞÜ:**

**TANIM ÖRNEĞİ**: Adres sütunu içerisinde semt bölümüne ait ayrıca bir sütun olmadığını varsayarak semt adı adres sütunu içerisinde yer alır ve buradan da LIKE (BULUNAN) komutuyla adres sütunu içerisinde Taksim semtinde oturan personeli listele.

**SELECT \* FROM personel WHERE adres LIKE ‘% TAKSİM %’ ; **

Adres LIKE ‘%TAKSİM%’ ifadesi adres içinde her hangi bir yerde TAKSİM yazan yerde oturan personeli listeleyecektir.
LIKE sözcüğünü, alt çizgi (-) sembolü ile birlikte kullanmakta mümkündür.

**SELECT \* FROM personel WHERE ad LIKE ‘Mehmet -----‘; **

Şekildeki komut ile ad alanı “Mehmet “ ile başlayan ve ad alanı uzunluğu 10 karakter olan isimlere sahip personeli listeleyecektir.”Mehmet Ali”,”Mehmet Can”- “Mehmetcik” gibi isimler listeleyecektir. Anlaşılacağı gibi - sembolü, tek karakterlik bir bilgiyi temsil etmektedir.

**5. SQL’DE ARİTMETİKSEL İFADELER VE FONKSİYONLAR :**

**KÜME FONKSİYONLARI:
SUM FONKSİYONU:
****SUM (TOPLA)
**Fonksiyonun argümanı olarak belirtilen sütun ile ilişkili olana toplama işlemini gerçekleştirir.

**ÖRNEK**: İşletmedeki personelin brüt maaşlar toplamı ne kadardır?
**SELECT SUM (brüt) FROM personel;
****AVG FONKSİYONU:
****AVG (ORTALA**)
Aritmetiksel ortalama (average) hesaplamak için kullanılır.
**SELECT AVG(brüt) FROM personel; **

**MAX FONKSİYONU:
****MAX (EN ÜST)
**Tablo içinde ,belirtilen sütun (alan)içindeki en büyük değeri bulur.
**ÖRNEK**: İşletme içindeki en yüksek maaş ne kadardır?
**SELECT MAX (brüt) FROM personel;
**
**MIN FONKSİYONU:
****MIN (EN ALT**)
Tablo içinde, belirlenen sütun alan içindeki en küçük değeri bulur.
**ÖRNEK**: İşletme içinde 4 Mayıs 1970’den önce doğanlar için, asgari ücret nedir?
**SELECT MIN(brüt) FROM personel WHERE dog\_tar < {05/04/70};
**
**COUNT FONKSİYONU:
****COUNT (SAY)**
Tablo içinde, her hangi bir sayma işlemi gerçekleştirmek için kullanılır.
**ÖRNEK**: Ücreti 6000000’dan olan personel sayısı nedir?
**SELECT COUNT (\*) FROM personel WHERE brüt > 6000000;
**

COUNT (SAY) fonksiyonu DISTINCT (TEKRARSIZ) sözcüğü ile de kullanılır.
**ÖRNEK: **Personel tablosunda mevcut personelin işletme içinde kaç tane farklı bölümde çalıştığını bul.
**SELECT COUNT(DISTINCT böl\_no) FROM personel;
COUNT (böl\_no) **

**6. GRUPLANDIRARAK İŞLEM YAPMA:**

**GROUP BY (GRUPLA**)
**ÖRNEK**: Her bölümdeki ortalama maaş nedir?
**SELECT bol\_no, AVG (brut) FROM personel GOUP BY bol\_no;
**
** HAVING (SAHİP)**

Gruplandırarak kümeleme fonksiyonunu uygularken koşulda verilebilir.Bu durumda grup üzerindeki hesaplamalarla ilgili koşul belirtilirken **HAVING** (SAHİP) sözcüğü kullanılır.
**ÖRNEK**: En yüksek maaşın 9000000’dan fazla olduğu bölümlerdeki personele ait ortalama maaşları listele.

**SELECT böl\_no,AVG (brüt) FROM personel GROUP BY böl\_no HAVING AVG(brüt)> 9000000; **

HAVING sözcüğü SELECT konusunda GROUP BY bulunmadığı zaman geçersizdir. HAVING sözcüğünü izleyen ifade içinde SUM , COUNT(\*) ,AVG, MAX yada MIN fonksiyonlarından en az biri bulunmalıdır. HAVING sözcüğü sadece gruplanmış veriler üzerindeki işlemlerde geçerlidir. WHERE sözcüğü bir tablonun tek tek satırları üzerinde işlem yapan koşullar içinde geçerlidir.

Bazı durumlarda HAVING ve WHERE sözcükleri ile birlikte SELECT komutu içinde kullanılabilir.

**ÖRNEK**: Personel tablosu içinde her bölümde erkek personele ait maaşlar için ortalamanın 9000000’dan fazla olduğu bölümleri listele.

**SELECT bol\_no, AVG (brut) FROM personel WHERE cins= .T. GROUP BY bol\_no HAVING AVG (brut) > 9000000; **

**BİRDEN FAZLA TABLOYU İLİŞKİLENDİRMEK:**

**JOIN (İLİŞKİLENDİR)**
**ÖRNEK:** Personel ve bölüm adlı 2 tablo bulunmaktadır.
Çalışan her personel ve personelin yöneticisi ile ilişkili bilgiler nelerdir?
**SELECT \* FROM personel,bölüm WHERE personel .böl\_no=bölüm.bölüm\_no ; ******

**ÖRNEK**: JOIN (İLİŞKİLENDİR) işleminde arzu edilen (sicil, ad, soyad, böl\_no, yön\_s\_g\_n) alanların listele.
**SELECT sicil,ad,soyad,bol\_no,yon\_s\_g\_n FROM personel, bolum WHERE personel .bol\_no = bolum .bolum\_no;
**
**SELF-JOIN: KENDİSİYLE -İLİŞKİLENDİR:
TANIM**: Bir tablonun kendisi ile birleştirilmesine “KENDISIYLE-İLİŞKİLENDİR” denir.(SELF-JOIN)

**SELECT A. sicil , A.ad , A.soyad, B .ad , B.soyad , B.dog\_tar FROM personel A , personel B
WHERE A. yon\_sos\_g\_n =B .sosy\_g\_no;
**

**NESTED SELECTS:**
**İÇİÇE SEÇİMLER**

**TANIM**: İç içe geçmiş SELECT komutlarından oluşur. İçteki Select komutunun bulduğu sonucu dış takı komutumuz işlevini yerine getirmesi için kullanılır.
**ÖRNEK: **Parça numarası 24 olan parçayı, projelerde kullanan çalışan personeli listele.
**SELECT \* FROM personel WHERE sosy\_g\_no IN(SELECT per\_s\_g\_no FROM parca, proje, calisma WHERE pr\_no = proj\_no AND proj\_no =proj\_no AND par\_no =24);
**
**ÖRNEK**: Fatih’te oturan personelin çalıştığı projelerin adlarını ve yerlerini listele.
**SELECT proj\_ad, yer FROM proje WHERE proj\_no IN (SELECT proje\_no FROM personel, calisma WHERE sosy\_g\_no = per\_s\_g\_no AND adres LIKE “% fatih %”); **

** UNION (BİRLEŞİM**)
**TANIM:** İki ayrı SEÇ komutunun sonucunda elde edilen tabloların birleşimi işlemini gerçekleştirir.

**ÖRNEK**: Adı Ahmet ve Soyadı Caner olan kişi yada kişileri işletmenin yürüttüğü projelerde çalışan bir kişi (sıradan bir personel yada bölüm yöneticisi)olarak bulunduran projelerin isimlerini ve projelerin yürütüldüğü yerleri listele.

**(SELECT proj\_ad,yer FROM proj,bölüm,personel WHERE bl\_no=bolum\_no AND
y\_sos gno = sosy\_g\_no AND ad =”Ahmet”AND soyad =”Caner”) UNION (SELECT proj\_ad,yer
FROM proje,çalışma,personel WHERE proj\_no = proje\_no AND Per\_s\_g\_no = sosy\_g\_no AND ad =”Ahmet” AND soyad =”Caner”) ******

**KOŞULLAR:
**UNION (BİRLEŞİM) sözcüğü ile, iki yada daha çok kişi SELECT ’in sonucu olan tabloların küme birleşimi işlemine tabi tutulması için 2 koşul gereklidir.

1) SELECT komutları sonucunda elde edilecek tablolar aynı sayıda kolon içermelidirler.
2) Sonuç tabloları karşılıklı olarak kolonların aynı veri tipi ve aynı genişlikte olmalıdır.
** ANY (HER HANGİ BİRİ****)**

**ÖRNEK**: Satış bölümünde çalışan personelin her hangi birinden daha düşük maaş alan ve mühendislik bölümündeki kişileri listele.

**SELECT \* FROM personel WHERE brüt < ANY (SELECT brut FROM personel WHERE bol\_no = 2) AND bol\_no =1;
**
Aynı ifade aşağıdaki gibi yazılabilir:
**SELECT \* FROM personel WHERE brut < (SELECT MAX (brut ) FROM personel
WHERE bol\_no = 2) AND bol\_no =1; **

**ALL (HEPSİ**)
**ÖRNEK**: Satış bölümünde çalışan ve mühendislik bölümündeki personelin hepsinden daha fazla maaş alan personeli listele.Bu örnekte satış bölümü kodu = 2 ve mühendislik bölümü kodu = 1 alınmıştır.
**YAPILIŞ YOLU:**
1) **SELECT \* FROM personel WHERE brut > ALL (SELECT brut FROM personel WHERE bol\_no = 1 AND bol\_no = 2;
**

2) **SELECT \* FROM personel WHERE brut > (SELECT MAX (brut) FROM personel
WHERE bol\_no = 1) AND bol\_no =2; **

**EXISTS (MEVCUT)
**VE, VEYA, DEĞİL operatörleri ile kullanılabilir.
**ÖRNEK**: 27 no’lu parçayı satan satıcılarla ilişkili tüm bilgileri listele.

**SELECT \* FROM satıcı WHERE EXISTS (SELECT \* FROM par\_sat WHERE sat\_no = satici\_n
AND parça\_n =27); **

**NOT EXISTS (MEVCUT DEĞİL)
**VE, VEYA, DEĞİL operatörleri ile kullanılabilir.
**ÖRNEK**: 27 no’lu parçayı satmayan satıcılar kimlerdir?

**SELECT \* FROM satıcı WHERE NOT EXISTS (SELECT \* FROM par\_sat WHERE sat\_no = satıcı\_n AND parça\_n =27);
**
**EXCEPT (FARKLI)**
Tablo-1 - Tablo-2 işlemi sonuç (iki kümenin farkı) elde edilecek tabloda,Tablo-1’de bulunup, Tablo-2’de bulunmayan veriler mevcut olacaktır.
**ÖRNEK**: Satış bölümündeki personel adlarından,mühendislik bölümünde bulunmayanları listele.

**SELECT \* FROM (SELECT ad FROM personel WHERE bol\_no=1 EXCEPT SELECT ad FROM personel WHERE bol\_no =2); **

**INTERSECT (KESİŞİM)
****ÖRNEK**: Hem Ankara’da,hem de İstanbul’daki projelerde görev alan bölümleri listele.

**SELECT \* FROM (SELECT bl\_no FROM proje WHERE yer LIKE “%Ankara%” INTERSECT
SELECT bl\_no FROM proje WHERE yer LIKE “%İstanbul%”);
**
**SAVE TO TEMP (SAKLA)
****ÖRNEK**: Bayan personeli,bayan adlı bir tablo içinde sakla.
**SAVE TO TEMP (SAKLA)
****SELECT \* FROM personel WHERE cins =.F. SAVE TO TEMP bayan;
**
**KEEP:**
**KEEP (KALICI**)

**ÖRNEK**:
**SELECT \* FROM personel WHERE cins = .F. SAVE TO TEMP bayan KEEP;
**
**7. TABLOLARDA DEĞİŞİKLİK YAPMAK:**

**INSERT (EKLE)
INTO (içinE)
VALUES (DEĞERLER**)

**ÖRNEK**: Bir personel tablosuna sicil\_no’su 275 olan personel ile ilişkili bilgileri ekle.

**INSERT INTO personel(sicil, sosy\_g\_no,ad,soyad,doğ\_tar adres,cins,brüt,böl\_no,yön\_s\_g\_no
VALUES(‘275’,’27652418’,’Ali’,’Caner’, {10/05/1962},’Merkez caddesi 46 -Fatih-İstanbul’,
.T.,27000000,2,’876215342’);
**
**DELETE (SİL)
****ÖRNEK**: 2 no’lu bölümdeki personelin tümü tablodan sil.

**DELETE FROM personel WHERE böl\_no = 2; **

5 ROWS DELETED 5 SATIR SİLİNDİ
**ÖRNEK**:Brüt maaş alanı boş olmayan tüm personeli sil.

**DELETE FROM personel WHERE brüt IS NOT NULL;
**25 ROWS DELETED 25 SATIR SİLİNDİ

**UPDATE (GÜNCELLE)
SET (YAP**)

**ÖRNEK:**2’inci bölümün yürüttüğü projelerde kullanılan tüm parçaların fiyatlarını % 7 zam yap.

**UPDATE parça SET fiyat = fiyat \*1,07 WHERE pr\_no IN (SELECT proj\_no
FROM proje WHERE bl\_no = 2; **

**CREATE INDEX (INDEKS YARAT **)
**ON (Hangi Tablo İçin)
**
**CREATE INDEX ındeks adı ON tablo adı(kolon adı 1,kolon adı 2,.,.kolon adı n); ******

**TEK BİR ALANA GÖRE ARTAN SIRADA İNDEKSLEME :**

**ÖRNEK**:İşletmede çalışan personeli brüt maaşlarına göre artan sırada listele.(Brüt alana göre bir indeks oluşturmalıyız)
**CREATE INDEX pers\_maas ON personel(brüt);
**INDEX CREATED 127 ROWS İNDEKS YARATILDI 127 SATIR
127 satırlık personel tablosu ile ilişkili olarak brüt kolonu indeks anahtarı olarak kullanan pers\_maas adlı indeks oluşturulmuştur. Bu durumda;
**SELECT \* FROM personel;**

Şeklinde listeleme komutu sonucunda personel tablosundaki tüm personel, brüt maaşlarina göre sirali olarak listelenecektir.

**TEK BİR ALANA GÖRE AZALAN SIRADA İNDEKSLEME :
****DESC Küçükten büyüğe (K-B)**

**ÖRNEK**: İşletmede çalışan personeli brüt maaşlarına göre azalan sırada (yüksek maaştan düşük maaşa doğru) listelemek istersek, brüt alanına göre aşağıdaki şekilde oluşturmak gerekir.

**CREATE INDEX ****
****ON personel (brüt DESC); **
**BİRDEN FAZLA ALANA GÖRE İNDEKSLEME :****
****ÖRNEK**:İşletmedeki personelin öncelikle adlarına göre,aynı adda olanların soyadlarına göre, hem adı hemde soyadı aynı olanların maaşlarına göre sıralanmış olarak listele.

**CREATE INDEX p\_ad\_soy\_m ON personel (ad,soyad,brüt); **

Bu durumda;

**SELECT \* FROM personel;
**

**UNIQUE (TEK****)**

Bir tablo, seçilen bir sütuna (alana) göre indekslenirken, indeksleme alanı olarak seçilen sütundaki verilerin tekrarlanmasına müsaade edilmesi istenmiyorsa, indeksleme yapılırken, CREATE, INDEX komutu içinde UNIQUE sözcüğü kullanılmalıdır.

**CREATE UNIQUE INDEX pers\_sicil ON personel (sicil); **

EKLEME için:

**Personel tablosuna INSERT INTO Personel VALUES(53768 ,’27241685’,’ayşe’,
‘şen’{01/04/63},’Merkez cad. 82 - Kadıköy’.F. ,27000000 ,2, ‘34261578’); **

**MEVCUT BİR İNDEKSİN SİLİNMESİ:
DROP IPTAL**

**DROP INDEX pers\_in; **
Komutu ile
INDEX DROPPED (İNDEKS SİLİNDİ)

**TABLONUN YAPISINDA DEĞİŞİKLİK YAPMAK:
****ALTER TABLE (TABLO DEĞİŞTİR)
**
**MEVCUT BİR TABLOYA KOLON EKLEMEK:
****ADD (EKLE**)
ALTER TABLE (TABLO DEĞİŞTİR) komutu içinde ADD (EKLE) ile satır ekle.

**ÖRNEK: **Personel tablosuna ,işe başlama tarihini belirten bir kolon ekle
**ALTER TABLE personel ADD iş\_baş\_tar DATE; **

ADD (EKLE) iş\_baş\_tar DATE NOT NULL (TARIH DEĞERSIZ) bu şekilde kullanılsaydı bu kolon satırı gene boş kalırdı; fakat bu kolon ile ilişkili yeni boş değerler eklemek istendiğinde buna müsaade edilmeyecekti.

**MEVCUT BİR TABLONUN ALANLARINDA DEĞİŞİKLİK YAPMAK :
****MODIFY (DEĞİŞTİR)
**
**MEVCUT BİR TABLODAN BİR KOLON SİLMEK: **
** DROP (İPTAL)
**
**ÖRNEK**: Personel tablosundan iş\_baş\_tar kolonunu sil.
**ALTER TABLE personel DROP iş\_baş\_tar ;
**Birden fazla kolonda silinebilir. Birden fazla kolon silmek için virgülle ayrılarak silinir.

**BİR TABLONUN ADINI DEĞİŞTİRMEK:**
**RENAME (TABLO YENİ AD**)
ALTER TABLE personel Personel tablosunda değişiklik yap RENAME TABLE elemanlar; elemanlar tablosunun adını değiştir

**MEVCUT BİR TABLONUN BİR KOLONUNUN ADININ DEĞİŞTİRİLMESİ:**
**RENAME YENİ AD
****ALTER TABLE personel RENAME brut br-maas;**

**MEVCUT BİR TABLONUN TÜMÜYLE SİLİNMESİ**
**DROP TABLE (TABLO İPTAL**)
**ÖRNEK**:Proje tablosunu sil.
**DROP TABLE proje; **

**VERİ GÜVENLİĞİ:
CREATE VIEW GÖRÜŞ ALANI YARAT
ÖRNEK**: Personel adlı temel tablodan persview adlı bir view oluştur.
**CREATE VIEW perswiew AS SELECT sicil,sos\_g\_no, ad, soyad, dog\_tar, adres, cins, bol\_no, yon\_s\_g\_no FROM personel; **

**VERİ BÜTÜNLÜĞÜNÜN SAĞLANMASI:**
**WITH CHECK OPTİON KONTROLLÜ
**
**CREATE VIEW UST\_PER\_ VIEW ****'Önce bir view oluşturulsun****
AS SELECT FROM personel WHERE brut >25000000 WITH CHECK OPTION;**

Burada, maaşı 25000000’ün üzerinde olan personelden oluşan bir UST\_PER\_VIEW adli view oluşturulmuştur.Bu view’a brüt maaşı 13000000 olan bir personel eklemek istediği zaman hata mesaji verecektir.

CHECK opsiyonu kullanılmasaydı hata mesajı alınmadan bu veri VİEW içine yükleyecekti.

**EKLEME **
**INSERT INTO UST\_PER\_VIEW VALUES (27521 ,’27865427’,’ayşe’, ‘okan’ ,{01/05/1962}’Cumh. Cad. 46 - Taksim’, .F.,13000000 ,1 ,’27651112’);
**
**VIEW İÇİNDE SATIR SİLME:
ÖRNEK**:UST\_PER\_VIEW içinden, maaşı 2500000’den az olan kişileri sil.

**DELETE FROM UST\_PER\_VIEW WHERE brut < 25000000; **
**VIEW SATIRLARI ÜZERİNDE GÜNCELLEME :
ÖRNEK**: UST\_PER\_VIEW adlı view’de sicili 27251 olan kişinin maaşını 37000000 olarak değiştir.

**UPDATE UST\_PER\_VIEW SET brüt = 37000000 WHERE sicil = 27251; **

**BİR VIEW’U SİLMEK:
****DROP VIEW (GÖRÜŞ ALANI IPTALI**)
**DROP VIEW UST\_PER\_VIEW; GÖRÜŞ ALANI IPTALI UST\_PER\_VIEW;**

**Açıklamalı Örnekler******

| **SQL Sorgu****Açıklama****** |  |
| --- | --- |
| "Select \* From Employees" | Employees tablosundan tüm alanları seç. En BASİT SQL sorgusu budur. |
| "Select \* From Title Where \[Year Published\] < 1889" | Title tablosundan \[Year Published\] alanı değeri 1889'dan küçük olan tüm kayıtları seç. Not: \* işareti tüm alanların seçileceğini gösterir. \[ \] "Köseli ayraç ise alan adi bir kelimeden fazla ise kullanılmalıdır. Yani yukarıdaki alan adı sadece "Year" olsaydı köseli ayraç kullanmaya gerek kalmayacaktı. |
| "Delete From Titles Where \[Year Published\] < #1/1/1889#" | Titles tablosundan \[Year Published\] alanı değeri 1/1/1889'dan küçük olanların tümünü sil |
| "Select Name, Picture From Authors Where Date\_of\_Birth = #2/1/1947#" | Authors tablosundan Date\_of\_Birth = 2/1/1947 denkliği olan kayıtlardan Name ve Picture alanlarını seç Dikkat ederseniz tüm sorgularda sabit bir SELECT ... WHERE .... yapisi var. Select seçimin nereden yapılacağını Where ise eşleşme kriterlerini göstermektedir. Bu örnekte \* işareti kullanılmamış ve sadece iki alan seçilmiştir: "name" ve "picture" Tarih ifadeleri ise # işaretleri arasında yazılmalıdır. |
| "Select \[First Name\], \[Last Name\] From Employees" | Employees tablosundan sadece First Name ve Last Name alanlarını seç |
| "Select Employees, Department, SupvName From Supervisors, Employees Where Employees.Department = Supervisors.Department" | Bu biraz daha karışık. Burada iki tablo var: Supervisors ve Employees. Bu iki tablodan üç adet alan seçilecek: 1.Employees, 2.Department, 3.SupvName. Bu iki tabloda da Department adlı birer alan var. İşte bu alanların denkliği ile seçim yapılıyor. Yani Employees tablosunun Department alanı ile Supervisor tablosunun Department alanı eşit ise seçim yapılıyor. |
| "Select Distinct \[Last Name\] From Employees" | Employees tablosundan Last Name değeri aynı olan kayıtlardan sadece birini al. Distinct anahtarı birden fazla aynı değer var ise sadece ilkini alır. |
| "Select \[Last Name\], Salary From Employees Where Salary > 2100" | Salary değeri 2100'den küçük olan Employees tablosu kayıtlarından yalnızca Last Name alanlarını seç. |
| "Select \* From Orders Where \[Shipped Date\] = #5/12/93#" | Orders tablosundan Shipped Date değeri 5/12/93'e eşit olan kayıtların tüm alanlarını seç. |
| "Select \[Product Name\], Sum (\[Units in Stock\]) From Products Group By \[Product Name\]" | Products tablosundan Product Name ve Unit in Stocks alanlarını al. Ancak burada dikkat edilmesi gereken Sum() fonksiyonudur. Bu fonksiyon her alan değerini birbiri üzerine toplar. Seçilen alanların tabloya yerleştirilmesi ise Product Name alan değerinin alfabetik sırasına göre A-Z olarak yapılır. |
| "Select \* From Employees Order By \[Last Name\], Asc" | Employees tablosundaki tüm alanları Last Name alan değerine göre Z-A sıralamasına göre seç Yani tablodan tüm kayıtlar alınacaktır, çünkü kriter olarak kullanılan WHERE sözcüğü yoktur. Ancak alınan tüm kayıtlar Last Name alan değerinin Z-A alfabetik sırasına göre (ters sıra) sıralanır. Soyadı Zahit olan kişi soyadı Orhun olan kişiden önce gösterilir. Sorgunun sonunda kullanılan ASC anahtarı seçimliktir (optional). Herhangi bir şey yazılmazsa, bu anahtar değerinin DESC (A-Z) olduğu kabul edilir. |
| "Select \[Last Name\], Salary From Employees Order By Salary, Desc, \[Last Name\] Last Name Salary Filiz 300.000.000 Kara 275.000.000 Akin 250.000.000 Bahçe 250.000.000 Celep 250.000.000 | Veritabanından alınan kayıtların listelemesi işlemi burada iki kritere göre yapılmakta. Önce kişilerin maaşları (Salary), sonra da soyadları (Last Name) dikkate alınmakta. Şöyle düşünün; Bir şirkette aynı maaşı alan 3 kişi var. Bu kişilerin soyadları Akın, Bahçe ve Celep olsun... Bu sorgu sonucu şirkette çalışan herkes listelenecektir. Ancak bizim bu üç kişi peş peşe listelenecek ve sıralama Akın-Bahçe-Celep seklinde olacaktır. Yandaki örneğe bakınız: |
| Dim dbNoro as Database Dim recLab2 as Recordset Set dbNoro = OpenDatabase("Noroloji.mdb", dbOpenSnapshot) Set recLab2 = dbNoro.OpenRecordset ("SELECT \* FROM LAB2 " & "WHERE ID = " & longID & " ;") | Yukarıdaki örneklerde sorgulara değişmezler girdik. ancak programcılıkta her zaman iş bu kadar kolay değildir. Sizin kullanıcıdan girdi almanız ve bunu run-time program içinde sorguya katmanız gerekir. Bu örnekte ise, dbNoro adlı Database nesnesini ve recLab2 adlı bir recordset nesnesini ilk önce Dim ile programa tanıtıyoruz. Sonra SET komutu ile önce dbNoro database nesnesine OpenDatabase metodu ile açmak istediğimiz veritabanını açıyoruz, sonra OpenRecorset Metodu ile bu veritabanı (yani dbNoro) içinde kayıt arayacak SQL sorgusunu çalıştırıyoruz. SQL sorgularının " " çift tırnak içine yazıldığını gördünüz. Bu değişmez bir kural. Bir de her sorgunun sonuna bir " ;" eklemeyi de unutmayın. Bu sorguda görülen longID ise kullanıcının klavyeden girdiği bir değerdir. Bu değer ile veritabanının LAB2 adli tablosunda bulunan ID adli alanının değeri eşit olursa o zaman arama olumlu sonuç verir ve recLab2 nesnesi içine bulunan değerler girilir, yada şöyle diyelim bulunan kayıtların temsilcisi recLab2 adli recordset nesnesi olur. Bu recordset nesnesini bir DBGrid nesnesine bağlarsanız, otomatik olarak bulunan tüm kayıtların gridlerde gösterildiğini görürsünüz. |
| Dim dbs As Database, rst As Recordset Set dbs = OpenDatabase ("Northwind.mdb") Set rst = dbs.OpenRecordset ("SELECT" & " Sum(UnitPrice\*Quantity)" & " AS \[Total UK Sales\] FROM Orders" & " INNER JOIN \[Order Details\] ON" & " Orders.OrderID = \[Order Details\].OrderID" & " WHERE (ShipCountry = 'UK');") | Dim ile Database ve Recordset nesnelerini tanımla. dbs nesnesini OpenDatabase metodu ile Northwind.mdb'ye bagla (aç). Bu açılan database'in OpenRecordset metodu ile SQL sorgu yap. Bu diğerlerine göre oldukça karışık bir sorgu. Bunun içinde INNER JOIN bağlantısı var. Bu bağlantı iki ayrı tabloyu ortak bir alan ile birbirine bağlar. Burada Orders ile Order Details tabloları inner join ile bağlanıyor, ve bağlantı kriteri ise; her iki tabloda da bulunan OrderID adlı alan. Her iki tabloda da OrderID alan değeri eşit olan ve ShipCountry değeri UK olan kayıtlardan Orders tablosunda bulunanların Unit Price ve Quantity alan değerleri çarpılarak üst üste toplanıyor ve bu toplama Total UK Sales adi veriliyor. Yani bu yeni bir sütun başlığı oluyor. |
| Sub Ad\_Ara(mode As String) Dim hasta As String hasta = InputBox("Aradiginiz hastanin " + mode + "i:") If hasta = "" Then Exit Sub Hastalar\_Ac Set recHastalar = \_ dbNoro.OpenRecordset("SELECT \* FROM " \_ & "HASTALAR WHERE " & mode & " = '" \_ & hasta & "' ") If recHastalar.AbsolutePosition = -1 Then MsgBox hasta + " " + mode + "ında kayıtlı hasta yok!", 48 Exit Sub End If recHastalar.MoveLast recHastalar.MoveFirst End Sub | Ad\_Ara adli bu sub benim NoroPlus programında veritabanından hasta aramakta kullanılıyor. Bu sub "mode" adlı bir string değişken ister. Kullanıcı bu sub'dan önce bir seçim yapmıştır. Ayni hastayı neye göre arayacaktır. Menüden adına göre aramayı seçerse bu "mode" değişkeni "ad" olacaktır, soyadına göre aramayı tercih ederse mode değişkeni "soyad" olacaktır. Bu mode değişkeni değerleri aynı zamanda Hastalar tablosundaki alan adlarıyla aynıdır. Yani Hastalar tablosunda da ad, soyad vs alanları vardır. Kullanıcı menüden adına göre aramayı seçince, karşısına inputbox çıkacak seçimine göre bilgi girmesini isteyecektir. Herhangi bit bilgi girilmezse sub'dan çıkılır. Girilen değer hasta adlı local bir string değişkeni içine kaydedilir. Sonra veritabanı içinden OpenRecordset metodu ile parantez içindeki sorgu çalıştırılır ve sonuç rechastalar adlı recordset nesnesi içinde tutulur. Eğer Recordset nesnesinin AbsolutePosition değeri = -1 ise bu yapılan sorguda kriterlere uyan kayıt bulunmadı demektir. O zaman msgbox bir hata mesajı ile bunu kullanıcıya duyurur ve sub'dan çıkar. Tersi olur da kayıt bulunursa MoveLast ile bulunan kayıtların sonuna gider ve tekrar MoveFirst ile başa gelerek kaç adet kayıt bulunduğunu öğreniriz. Gelelim sorguya: Hastalar tablosundan tüm bilgileri almak istiyoruz, bu yüzden "\*" yıldız kullandık: "SELECT \* FROM HASTALAR" devamında ise koşul cümlesi var: "WHERE " & mode & " = ' " & hasta & " ' " Bu kosul tablodaki "mode" adli alan değeri input ile girilen değer ile aynı ise doğru sonuç verecektir ve Select ifadesi çalışacaktır. Diyelim ki soyadı Kara olan hastaları arattınız. Bu soyada sahip 10 hasta çıkmış olsun. Bu rakamı da Recordset nesnesinin RecordCount özelliği ile bulursunuz. Daha sonra bulduğunuz hastalar arasında Move metodları yardımıyla dolaşabilirsiniz: MoveFirst, MoveNext, Move Previous, MoveLast. Bu is çok kolaydır. Birden fazla sayıda kayıda ulaştığınızda görünür hale getireceğiniz, aksi taktirde görünmeyen command butonlari ile ileri geri hareketleri sağlayabilirsiniz. |

## PAGE

## PAGE 1

---
*Kaynak: `VERİ TABANI SORULAMALARI/VERİ TABANI SORULAMALARI.doc` — Bim — 2004*
