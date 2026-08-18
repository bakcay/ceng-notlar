# Kullanilan Deyim Ve Fonksiyonlar

KULLANILAN DEYİM VE FONKSİYONLAR

.OPEN DEYİMİ

Open deyimi erişimli veri dosyalarında olduğu gibi dosyanınn açılmasını sağlar.ancak mod olarak RANDOM parametresi kullanılmalıdır.

RANDOM ifadesi dosyanın rastgele erişimli veri dosyası olduğunu belirtir. Ancak kullanımı zorunlu değildir. Kullanılmadığında varsayılan değer 128 byte’dır.

LEN parametresi ile belirlenen toplam kayıt uzunluğu , FIELD deyimi ile değişkenlere atanacak veri alanlarına bölünerek kullanılır. Toplam alan Len ile verilen uzunluğu geçemez.

Rastgele erşimli veri dosyalarında , sıralı erişimli veri dosyalarındaki gibi veri yazmak , veri okumak, veya veri eklemek için ayrı ayrı modlar yoktur. Tüm bu işlemler RANDOM parametresi ile açılan rastgele erişimli veri dosyası üzerinde uygulanabilir. Rastgele erişimli veri dosyaları ile işlem yaparken kayıt numaraları kullanılır. Her birinin veri numarası vardır ve verilere erşim doğrudan bu numaralarla yapılır. Sıralı erişimli veri dosyalarını kullanırken, istediğimiz veriye ulaşmak için program oluşturacak kadar kod yazmak zorunda kaldığımızı hatırlayınız.

.FIELD# DEYİMİ

FIELD# deyimi buffer alanının düzenlenmesinde kullanılır. Buffer daha öncede açıkladığımız gibi veri dosyası ile program arasındaki özel bellek alanıdır. Veriler dosya yada programa aktarılmadan önce buffer alanına alınır ve veriler üzerindeki işlem burada yapılır. Daha sonra programa yada diskete aktarılır. FIELD# deyimi ile, buffer üzerinde gerekli veriler için alan oluşturulur.

.LSET VE RSET DEYİMLERİ

FIELD# deyimi ile, buffer üzerinde değişkenlerin yerleştirilmeleri için alan oluşturulur. LSET ve RSET deyimleri ilede bu alanlara veri yerleştirilir. LSET deyimi ile, veriler buffer alanına sola yanaşık olarak, RSET deyimi ile sağa yanaşık olarak yazılır.

.PUT DEYİMİ

PUT deyimi dosyaya veri yerleştirmek için kullanılır. Diğer bir deyişle, sıralı erişimli veri dosyalarında WRITE# deyiminin yaptığı işi yapar. PUT deyimi ile birlikte dosya numarası ile kayıt numarası da belirtilir.Deyim ile istenilirse # karakteri de kullanılabilir.

.GET DEYİMİ

GET deymi, veri dosyasından programa veri okumak için kullanılır.okunacak verinin kayıt numarası bu deyim ile belirtilir. Deyim ile birlikte istenirse # karakteri kullanılabilir.

.MKI$, MKL$, MKS$, VE MKD$ FONKSİYONLARI

Bu fonksiyonların sayısal değerleri, string değerlere çevirmek için kullanılır.

MKI$ : Tam sayı değerleri string değerlere çevirmek için kullanılır.

MKL$ : Uzun tam sayı değerleri string değerlere çevirmek için kullanılır.

MKS$ : Tek incelikli sayısal değerleri string değerlere çevirmek için kullanılır.

MKD$ : Çift incelikli sayısal değerleri string değerlere çevirmek için kullanılır.

.CVI, CVL, CVS VE CVD FONKSİYONLARI

Bu fonksiyonlar, buffer alanında string olarak kayıt edilen ifadeleri sayısal değerlere dönüştürür.Böylece buffere string sabit olarak yerleştirilen sayısal ifadeler, program içerisinde kullanılırken tekrar sayısal değere dönüştürülür.

CVI : String ifadenin tam sayıya çevrilmesinde kullanılır.

CVL: String ifadenin uzun tam sayıya çevrilmesi için kullanılır.

CVS : String ifadenin tek incelikli sayıya çevrilmesi için kullanılır.

CVD :String ifadenin çift incelikli sayıya çevrilmesi için kullanılır.

.EOF FONKSİYONU

Sıralı erişimli veri dosyalarında kullanılan EOF fonksiyonundan farklı değildir. Dosya sonunun belirlenmesinde kullanılır.

.CLOSE # DEYİMİ

Open deyimi ile açılan dosyanın kapatılmasında kullanılır. Kulanımı zorunlu değildir, ancak prensip olarak açılan tüm dosyalar program sonunda CLOSE# deyimi ile kapatılır.

ÖRNEK:

CLS

OPEN “c:/ rndpers.dat”RANDOM AS #1 LEN = 40

FIELD #1,2 AS Bfno$,9 AS Bfisim$,12 AS Bfsoy$,2 AS Bfyaş$, 15 AS Bfbol$

| EKRAN ÇIKTISI: Kimlik numarası : 1 Çalışanın ismi : erdem Soyismi : tulunay Yaşı : 21 Bölümü: teknikservis Devam (d) bitir (b) ? d Kimlik numarası:2 Çalışanın ismi:kenan Soyismi:avci Yaşı:52 Bölümü:ulaşım Devam (d) bitir (b) ? d Kimlik numarası :3 Çalışanın ismi :sinem Soyismi:er Yaşı:27 Bölümü:pazarlama Devam (d) bitir (b) ? b Kayıt işlemi sona erdi |
| --- |

DO

INPUT”kimlik numrası:”,no$

LSET Bfno$ = no$

INPUT”çalışanın ismi: “,isim$

LSET Bfisim$ = isim$

INPUT”soyismi: “, soy$

LSET Bfsoy$ = soy$

INPUT”yaşı: “,yas

Yas$ = MKI$ (yas)

LSET Bfyas$ = yas$

INPUT”bölümü: “, bol$

PUT 1, VAL (no$)

PRINT

INPUT “ devam (d) / bitir (b) “; secim$

PRINT

LOOP WHILE UCASE$(secim$) = “D”

CLOSE #1

PRINT

PRINT “ kayıt işlemi sona erdi”

END

---
*Kaynak: `KULLANILAN DEYİM VE FONKSİYONLAR/KULLANILAN DEYİM VE FONKSİYONLAR.doc` — wizard — 2004*
