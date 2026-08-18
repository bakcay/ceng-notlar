# SQL Sorgulama Dili

## SQL Sorgulama Dili,Yerel SQL ve Dil Takımı

**SQL Sorgulama Dili** adı altında yeni bir makale dizisine başladık "SQL sorgulama dili" adlı makale dizimiz bittikten sonra "Veritabanı Uygulamaları Geliştirmek" adlı makale dizimize TQuery bileşeni ile devam edeceğiz. Makale dizimizin bu bölümünde SQL sorgulama dilinin Borland firması tarafından geliştirilen türevi Yerel SQL sorgulama dilini anlatacağız. Ayrıca Yerel SQL'in dil takımı üzerinde de duracağız.Yerel SQL dil takımında tablo isimlerinin, saha isimlerinin ve referansların, tarih ve zaman biçimlemelerinin, boolean ifadelerin kendine ait yazım kurallarını anlatacağız.SQL Sorgulama dilini bilen kişilerin bile bu makale dizisini dikkatle takip etmesini tavsiye ederim.

## Yerel SQL

**Yerel SQL Nedir?******

Yerel SQL dBASE, Paradox ve FoxPro tablolarına ulaşmak için kullanılan SQL-92 standartının bir alt türevidir. Yerel SQL ifadelerine uygulamalardan erişilirken, BDE bu ifadeleri BDE API fonksiyonlarına dönüştürür.

SQL ifadeleri iki katagoriye ayrılır: Veri İşletme Dili (DML) ve Veri Tanımlama Dili (DDL)
DML tablo verilerini taramak,eklemek,güncellemek, silmek için kullanılan SQL ifadeleri içerir. Örnek olarak SELECT bir DML ifadesidir.
DDL tabloları yaratmak, değiştirmek, ve silmek için kullanılan SQL ifadelerini içerir. Örnek olarak CREATE TABLE ve DROP INDEX DDL SQL ifadelerindendir.

**Yerel SQL Dil Takımı******

Bu makale dizisinde vereceğim örneklerin daha iyi anlaşılabilmesi için önce size SQL anlatım geleneklerini anlatmayı uygun gördüm.

vereceğim örneklerde tüm SQL örnekleri Courier New fontunda olacaktır. Ayrıca yerel SQL büyük küçük harf duyarlı olmasa da dil elemenlteri ile diğer elementleri kolayca ayırabilmeniz için tüm dil elementleri büyük harfle diğer elementler ise küçük harflae yazılmıştır.

Örneklerde kullanılma imkanı bulunan fakat kullanmak zorunda olmadığınız dil elementleri köşeli parantez ( \[ ve \] ) arasına alınacaktır. Örneğin aşağıdaki örnekte DISTINCT anahtar kelimesi seçimliktir.

SELECT \[DISTINCT\] \*

Örneklerde birden çok seçenekten birini seçmek söz konusu ise seçenekler dikey çubuk karakteri ayrılacaktır. Örneğin aşağıdaki gibi bir SQL ifadesinde bir saha referansı için ASC yada DESC ifadelerinden sadece biri kullanılabilir. Aynı zamanda bu ASC veDESC ifadeleri seçimliktir.

ORDER BY saha\_referansi \[ASC | DESC\]

**Not:** Kesinlikle tek dikey çubuk karakterini SQL dilinde kullanılan çift çubuk karakterleri ile karıştırmayın.( **| |** )

Yerel SQL kullanılırken bazı kurallara uyulması gerekir örneğin SQL ifadelerinden komutlarından yada fonksiyonlarıdan herhangi birini değişken, saha referansı,Parametre vb. olarak kullanamazsınız. Ayrıca tablo isimlerinin, saha isimlerinin ve referanslarıın, tarih ve zaman biçimlemelerinin, boolean ifadelerin kendine göre yazım kuralları vardır. Bu tanımlamalar aşağıda verilmiştir.

**Tablo İsimleri:******

ANSI-standard SQL'de, tablo isimleri Türkçe karakterler içermeyen tek bir kelimeden yada aralarında boşluk yerine "\_" karakteri içeren birden çok kelimeden oluşabilir. Fakat Yerel SQL birden çok kelime içeren tablo isimlerine izin verir.

Yerel SQL tam dosya adı ve yol tanımlamalarına izin verir. Tablo tek yada çift tırnak arasında bir dosya yolu yada dosya adı tanımlaması ile gösterilir.Örneğin:

SELECT \*
FROM 'parts.dbf'

SELECT \*
FROM "c:\\örnek\\parts.dbf"

Yerel SQL BDE alias tablo referanslarını da destekler. Örneğin:

SELECT \*
FROM ":pdox:table1"

Eğer dosya uzantısını ihmal etmek istiyorsanız, tablonun tipi BDE'de varsayılan tablo tipi olmalıdır. Yada SQL ifadenizde alias kullandığınız taktirde tablonun uzantısını yoksayabiliriz.

Son olarak eğer tablonuzun adı SQL ifadelerinden biri ise bunu tek yada çift tırnak arasına alarak kullanabiliriz. Örneğin:

SELECT passid
FROM "password"

**Saha adları ve referansları:******

ANSI-standard SQL'de, kolon isimleri ve referansları Türkçe karakterler içermeyen tek bir kelimeden yada aralarında boşluk yerine "\_" karakteri içeren birden çok kelimeden oluşabilir. Fakat Yerel SQL birden çok kelime içeren kolon isimlerine ve referanslarına izin verir.

Yerel SQL Paradox'un çok kelimeden oluşan saha isimlerini ve referanslarını destekler.

Eğer Paradox tablosunun bir sahası SQL ifadesiyle aynı adı taşıyorsa tek yada çift tırnakla çevrilerek kullanılır ve Önüne tablo adını yada tablo referansını alır.Tablo adı yada referansı saha adı yada referansından bir nokta ile ayrılır. Aşağıdaki örnekte saha adı iki kelimeden oluşmuştur:

SELECT E."Emp Id"
FROM employee E

Bir sonraki örnek DATE SQL anahtar kelimesini içeren bir saha adını nı nasıl tanımlandığını gösterir:

SELECT datelog."date"
FROM datelog

**Tarih Biçimleri:******

Yerel SQL tarih tanımlarını Amerikan tarih biçimine göre ayarlar. Diğer tarih biçimlerini desteklemez. Amerikan tarih biçimi AA/GG/YY yada AA/GG/YYYY olarak iki çeşittir. Tarih kullanımımnda bir hataya mahal vermemek için tarih değerleri tek yada çift tırnak içine alınırlar. Eğer tarih değerini tırnak içine almazsak örneğin 17/7/2000 tarihini 17 bölü 7 bölü 2000 olarak algılayacaktır.Aşağıda tarih değerinin SQL ifadelerinde nasıl kullanılacağına dair bir örnek verilmiştir.

SELECT \*
FROM orders
WHERE (saledate <= "1/23/1998")

Tek haneli günlerin yada ayların başlarına sıfır eklemek seçimliktir.

Eğer yüzyıl yıl içinde tanımlanmamışsa BDE ayarlarından FOURDIGITYEAR parametresi yüzyılı kontrol eder. Eğer FALSE ise yıllar sadece iki hane ile tanımlanır. Eğer rakam 0 ile 49 arasında ise 21'ci yüzyılı 50 ile 99 arasında ise 20'ci yüzyılı tanımlar. Örneğin 5/5/1998 tarihi 5/5/98 olarak tanımlanır. 17/7/2000 tarihi ise 17/7/00 olarak tanımlanır. Eğer TRUE ise 17/7/00 tarihi Milattan sonra 0'cı yıl olarak anlaşılır.

**Zaman Biçimleri:******

Yerel SQL saat biçimlerinin ss:dd:nn AM/PM (ss saat, dd dakika, nn saniye) olarak ayarlanmasını ister. zaman değeri ile birlikte yeni bir kayıt eklerken AM/PM kullanımı seçimliktir ve büyük küçük harf ayrımı yapılmaz (yani AM yerine am yazabilirsiniz.)Tanımlama tırnak işaretleri arasında olmalıdır.

INSERT INTO WorkOrder
(ID, StartTime)
VALUES ("B00120","10:30:00 PM")

Eğer AM yada PM etiketlerinden herhangi biri kullanılmışsa bu yarım gün uygulamasının kullanılacağı anlamına gelir ve saat 12 ile karşılaştırılır. Eğer saat 12den küçükse AM büyükse PM olur Saat sahsı AM/PM tasarımını değiştirebilir. Örneğin "15:03:22 AM" "3:03:22 PM" değerine çevrilir.

**Boolean ifadeler:******

Boolean ifadeler TRUE ve FALSE tırnak işaretleri ile çevrilerek yada çevrilmeden kullanılabilir.

SELECT \*
FROM transfers
WHERE (paid = TRUE) AND NOT (incomplete = "FALSE")

**Tablo Referans Adları:******

tablo referans adları tablo ile bir kolonu ilişkilendirmek için kullanılır. bu genellikle farklı tablolardan gelen adları aynı birden çok sahanın SQL ifadesi içinde kullanılırken çok büyük kolaylık sağlar. Bir tablo referans adı FROM ifadesinde tanımlanır.Bu tanımlayıcı yada tablo referans adıbir kolon adının ön eki olarak kullanılabilir.

Eğer tablo ismi tırnak işaretleri arasında değilse tablo adı varsayılan referans adı olarak kullanılır.

SELECT \*
FROM customer
LEFT OUTER JOIN orders
ON (customer.custno = orders.custno)

Eğer tablo ismi tırnak işaretli bir ifade ise aşağıdaki gibi tırnak işaretleri ile birlikte kullanabilirsiniz.

SELECT \*
FROM "customer.db"
LEFT OUTER JOIN "orders.db"
ON ("customer.db".custno = "orders.db".custno)

Eğer tırnak işaretinin arasındaki ifade çok uzunsa bu tanımlamayı FROM ifadesinden sonra başka bir ifadeye atayarak kullanabilirsiniz.

SELECT \*
FROM "customer.db" CUSTOMER
LEFT OUTER JOIN "orders.db" ORDERS
ON (CUSTOMER.custno = ORDERS.custno)

**Saha Refereansları:******

Saha referansları bir sahayı,hesaplanan saha değer kümesini yada bir SQL ifadesini ad olarak barındıran sahayı farklı bir adla tanımlamaya yarar. Saha referansları kesinlikle çift tırnak arasına alınamaz. Bir saha referansı tanımlamak için saha referansı tanımlanacak olan tanımlamadan sonra AS anahtar kelimesini kullanıp saha referans adını AS anahtar kelimesinden sonra yazmalıyız.Aşağıdaki ifade de Sub ve Word tanımlamaları saha referansıdır.

SELECT SUBSTRING(company FROM 1 FOR 1) AS sub, "Text" AS word
FROM customer

**Açıklama Tanımlamak:******

Eğer SQL ifadenizin daha anlaşılır olmasını istiyorsanız içine açıklama yazabilirsiniz. Açıklamanız /\* ile başlayıp \*/ ile sona ermelidir. başlangıç ve sondaki işaretler açıklama ile aynı satırda olmak zorunda değildir.

/\*
Merhaba Televole
\*/
SELECT SUBSTRING(company FROM 1 FOR 1) AS sub, "Text" AS word
FROM customer

Açıklamalar aynı zamanda SQL ifadeleri de içerebilirler İfadeleriniz eğer Açıklama içinde ise yoksayılacaklardır.Açıklamalar özellikle SQL ifadelerinizi test etmek istediğinizde çok işe yarat.Her satırı ayrı ayrı açıklama içine alarak hatanın nerede olduğunu bulabilirsiniz.

SELECT company
FROM customer
/\* WHERE (state = "TX") \*/
ORDER BY company

**SQL tanımlı kelimeler:******

SQL ifadeleri tanımlamak için bazı kelimeleri kullanmıştır. Biz sorgularımızda bu isimleri kullanamayız. Eğer kullanırsanız **Invalid use of keyword error** hata mesajını alırsınız.Aşağıda bahsettiğimiz ifadelerin alfabetik bir listesini görüyorsunuz.

| ACTIVE ADD ALL AFTER ALTER AND ANY AS ASC ASCENDING AT AUTO AUTOINC AVG BASE\_NAME BEFORE BEGIN BETWEEN BLOB BOOLEAN BOTH BY BYTES CACHE CAST CHAR CHARACTER CHECK CHECK\_POINT\_LENGTH COLLATE COLUMN COMMIT COMMITTED COMPUTED CONDITIONAL CONSTRAINT CONTAINING COUNT CREATE CSTRING CURRENT CURSOR DATABASE DATE DAY DEBUG DEC DECIMAL DECLARE DEFAULT DELETE DESC DESCENDING DISTINCT | DO DOMAIN DOUBLE DROP ELSE END ENTRY\_POINT ESCAPE EXCEPTION EXECUTE EXISTS EXIT EXTERNAL EXTRACT FILE FILTER FLOAT FOR FOREIGN FROM FULL FUNCTION GDSCODE GENERATOR GEN\_ID GRANT GROUP GROUP\_COMMIT\_WAIT\_TIME HAVING HOUR IF IN INT INACTIVE INDEX INNER INPUT\_TYPE INSERT INTEGER INTO IS ISOLATION JOIN KEY LONG LENGTH LOGFILE LOWER LEADING LEFT LEVEL LIKE LOG\_BUFFER\_SIZE | MANUAL MAX MAXIMUM\_SEGMENT MERGE MESSAGE MIN MINUTE MODULE\_NAME MONEY MONTH NAMES NATIONAL NATURAL NCHAR NO NOT NULL NUM\_LOG\_BUFFERS NUMERIC OF ON ONLY OPTION OR ORDER OUTER OUTPUT\_TYPE OVERFLOW PAGE\_SIZE PAGE PAGES PARAMETER PASSWORD PLAN POSITION POST\_EVENT PRECISION PROCEDURE PROTECTED PRIMARY PRIVILEGES RAW\_PARTITIONS RDB$DB\_KEY READ REAL RECORD\_VERSION REFERENCES RESERV RESERVING RETAIN RETURNING\_VALUES RETURNS REVOKE RIGHT | ROLLBACK SECOND SEGMENT SELECT SET SHARED SHADOW SCHEMA SINGULAR SIZE SMALLINT SNAPSHOT SOME SORT SQLCODE STABILITY STARTING STARTS STATISTICS SUB\_TYPE SUBSTRING SUM SUSPEND TABLE THEN TIME TIMESTAMP TIMEZONE\_HOUR TIMEZONE\_MINUTE TO TRAILING TRANSACTION TRIGGER TRIM UNCOMMITTED UNION UNIQUE UPDATE UPPER USER VALUE VALUES VARCHAR VARIABLE VARYING VIEW WAIT WHEN WHERE WHILE WITH WORK WRITE YEAR |
| --- | --- | --- | --- |

AşağıdaYerel SQL'de bulunan operatörlerleri görüyorsunuz.Bu operatörler kesinlikle hiç bir referansın yada ismin içinde kullanılamazlar.

| **\| \|****-****\*****/****<>****<****>****,****** |
| --- |

| **=****<=****>=****~=****!=****^=****(****)****** |
| --- |

**Yerel SQL'in Desteklemediği Elementler:******

Aşağıdaki SQL-92 elementleri Yerel SQL'de kullanılamazlar.

| ALLOCATE CURSOR (Komut) ALLOCATE DESCRIPTOR (Komut) ALTER DOMAIN (Komut) CASE (Deyim) CHECK (Sabit) CLOSE (Komut) COALESCE (Deyim) COMMIT (Komut) CONNECT (Komut) CONVERT (Fonksiyon) CORRESPONDING BY (Deyim) CREATE ASSERTION (Komut) CREATE CHARACTER SET (Komut) CREATE COLLATION (Komut) CREATE DOMAIN (Komut) CREATE SCHEMA (Komut) CREATE TRANSLATION (Komut) CREATE VIEW (Komut) CROSS JOIN (İlişki Operatörü) CURRENT\_DATE (Fonksiyon) CURRENT\_TIME (Fonksiyon) CURRENT\_TIMESTAMP (Fonksiyon) DEALLOCATE DESCRIPTOR (Komut) DEALLOCATE PREPARE (Komut) DECLARE CURSOR (Komut) DECLARE LOCAL TEMPORARY TABLE (Komut) DESCRIBE (Komut) DISCONNECT (Komut) DROP ASSERTION (Komut) DROP CHARACTER SET (Komut) DROP COLLATION (Komut) DROP DOMAIN (Komut) DROP SCHEMA (Komut) | DROP TRANSLATION (Komut) DROP VIEW (Komut) EXCEPT (İlişki Operatörü) EXECUTE (Komut) EXECUTE IMMEDIATE (Komut) FETCH (Komut) FOREIGN KEY (Sabit) GET DESCRIPTOR (Komut) GET DIAGNOSTICS (Komut) GRANT (Komut) INTERSECT (İlişki Operatörü) MATCH (Yüklem) NATURAL (İlişki Operatörü) NULLIF (Deyim) OPEN (Komut) OVERLAPS (Yüklem) PREPARE (Komut) REFERENCES (Sabit) REVOKE (Komut) ROLLBACK (Komut) Row value constructorsSET CATALOG (Komut) SET CONNECTION (Komut) SET CONSTRAINTS MODE (Komut) SET DESCRIPTOR (Komut) SET NAMES (Komut) SET SCHEMA (Komut) SET SESSION AUTHORIZATION (Komut) SET TIME ZONE (Komut) SET TRANSACTION (Komut) TRANSLATE (Fonksiyon) UNIQUE (Yüklem) USING (İlişki Operatörü) |
| --- | --- |

---
*Kaynak: `SQL SORGULAMA DİLİ/ekitap-Anonim-SQL_Sorgulama_Dili_Yerel_SQL_ve_Dil_Takimi.doc` — Dinamit — 2001*
