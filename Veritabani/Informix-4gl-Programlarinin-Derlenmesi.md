# Informix - 4gl Programlarinin Derlenmesi

## **İÇİNDEKİLER :******

## **ÖNSÖZ ****2-10******

## **BÖLÜM 1 INFORMIX-4GL Programlarının ****11-16**** **

## **Derlenmesi **

## **BÖLÜM 2 Menü Oluşturma ****17-26******

## **BÖLÜM 3 Form Oluşturma ****27-32******

## **BÖLÜM 4 Database’e Veri Eklenmesi ****33-56******

## **BÖLÜM 5 Database’in Sorgulanması ****57-73******

## **BÖLÜM 6 Database’den Veri Silme Ve Güncelleme ****74-82******

## **BÖLÜM 7 Array Yapısı ****83-100******

## **BÖLÜM 8 Raporlar ****101-110******

## **ÖNSÖZ******

Bu iki bölümde INFORMIX-4GL e ait ve INFORMIX-4GL in 4. Kuşak dili olmasını sağlayan Menu ve Form oluşturulması incelenmiştir.

Bölüm 2 de aşağıdaki INFORMIX-4GL komutları ele alınmıştır.

Tanımlama Yapıları

FUNCTION

MAIN

Akış Yapıları

CALL

RUN

SLEEP

EXIT

Ekran Yapıları

MENU

ERROR

MESSAGE

PROMPT

OPTIONS

Utility

MKMESSAGE

Bölüm 3 te ise

Form oluşturma ve derleme özellikleri

Form4gl komutu

işlendi.

## **INFORMIX Mimarisi**

## ** Informix-SQL Informix-4GL Informix-ESQL**

** **ISQL-MENU Programmers’s environment

R A P

D C E ESQL

S E R 4GL Application

Q F Application Programs

L** **O Programs

** **** ** R

## ** ** M

SQL SQL SQL SQL LIBRARY SQL LIBRARY

Library Library Library

PARSER

OPTIMIZER

QUERY SQLEXEC

PROCESSOR

C-ISAM

DATABASE

## **INFORMIX-4GL in Özellikleri ve Avantajları**

Informix-4GL procedurel olmayan bir yapı kullanır.Bu programcıya istediği anda özel adımlar tanımlama fırsatı verir.Bu dilde özel komutlar vardır.Bunlar Menu ,Construct gibi komutlardır.Bu komutlar informix ‘i 4. Kuşak dili yapar ve informix’e özgü komutlardır.Bu sayede bazı işlemler birkaç satırda yapılabilir.3. kuşak dillerde ise bu yapılan işlemler bayağı uzun sürer.Böylelikle hata kontrolü ve program desteği oldukça basittir.

Informix 3. Kuşak dillerindeki komutlarıda destekler yani yapısında IF THEN, WHILE, FOR gibi.Böylece yapılan işler bu komutlar sayesinde koşul kazanabilir veya tekrarlanabilir.

Informıx-4GL UNIX,MS-DOS ve VMS işletim sistemlerine uyumludur.

Informix-4GL Informix-SQL ile bağlantılıdır.Yani SQL komutlarının tümünü kullanabilir.

## Informix-SQL ile Informix-4GL in Karşılaştırılması

Informix-SQL

RDSQL

sperform

User database

MENU sacago

Operating System

Commands

Informix-SQL de daha önceden sizin için database ‘e yazılmış veriye ulaşabilirsiniz.

Informix-4GL

DDL,DML,DCL

Data Entry Forms

User database

MENU Reports

Operating System

Commands

Informix-4GL database dizaynı ve database’e yazma işlemini programcı tarafından yapılmasına izin verir.

## **OVERVIEW******

**Program tanımlama yapıları******

MAIN

FUNCTION

REPORT

**Değişken tanımlama yapıları**

DEFINE

GLOBALS

**Program akış yapıları**

CALL EXIT RETURN SLEEP

CASE FOR RUN WHILE

CONTINUE IF

**Hata kontrolü yapıları**

DEFER

WHENEVER

**Ekran etkileşim yapıları**

OPEN WINDOW PROMPT DISPLAY MENU

OPEN FORM INPUT ERROR OPTION

CURRENT WINDOW CONSTRUCT MESSAGE

CLOSE CLEAR

**Değişken atama yapıları**

LET

INITIALIZE

**Rapor yapıları**

START REPORT

OUTPUT TO REPORT

FINISH REPORT

**Cursor yönetme yapıları**

DECLARE OPEN FOREACH

FETCH CLOSE

**Dinamik yapılar**

PREPARE

RDSQL yapıları aşağıdaki gibidir.

**Veri tanımlama yapıları**

CREATE DATABASE

CREATE TABLE

CREATE INDEX

DATABASE

**Veri yönetme yapıları**

INSERT

SELECT

DELETE

UPDATE

**Veri erişim yapıları**

GRANT

REVOKE

## **STORES DATABASE’I**

Burda RDSQL yapıları stores database’ini oluşturmak için kullanılmıştır.

MAIN

CREATE DATABASE stores

CREATE TABLE customer

(

cnum SERIAL(100),

fname CHAR(10),

lname CHAR(15),

company CHAR(20),

address1 CHAR(20),

address2 CHAR(20),

city CHAR(15),

state CHAR(2),

zip CHAR(5),

phone CHAR(12),

)

CREATE TABLE orders

(

ordno SERIAL(1000),

orddate DATE,

cnum INTEGER,

custpo CHAR(10),

shipdate DATE,

shipcharge MONEY,

datepaid DATE,

totalamt MONEY

)

CREATE TABLE items

(

ordno INTEGER,

itemno SMALLINT,

stockno SMALLINT,

mfcode CHAR(3),

qty INTEGER,

totalprice MONEY

)

CREATE TABLE stock

(

stockno SMALLINT,

mfcode CHAR(3),

description CHAR(15),

unitprice MONEY

)

CREATE TABLE manufacturer

(

mfcode CHAR(3),

mfname CHAR(15),

)

CREATE UNIQUE INDEX xc\_1 ON customer(cnum)

CREATE INDEX xc\_2 ON customer(lname)

CREATE INDEX xc\_3 ON customer(company)

CREATE UNIQUE INDEX xo\_1 ON customer(ordno)

CREATE INDEX xo\_2 ON customer(cnum)

CREATE INDEX xi\_1 ON items(mfcode)

CREATE INDEX xi\_2 ON items(stockno.mfcode)

CREATE UNIQUE INDEX xi\_3 ON items(ordno.itemno)

CREATE UNIQUE INDEX xs\_1 ON stock(stockno.mfcode)

CREATE INDEX xs\_2 ON stock(mfcode)

CREATE UNIQUE INDEX xm\_1 ON manufacturer(mfcode)

GRANT RESOURCE TO PUBLIC

END MAIN

## **Store database’inin veri yapısı**

**Customer******

cnum fname lname company address1 address2 city state phone

**Orders******

ordno orddate cnum custpo shipdate shipcharge datepaid totalamt

**Manufacturer******

mfcode mfname

**Stock**

** **stockno mfcode description unitprice

**Items******

ordno itemno stockno mfcode qty totalprice

index unique index

## **RDSQL DML(data management language) Yapısı**

** ** INSERT veriyi database e ekler.

DELETE veriyi database den siler.

SELECT databaseden veri getirir.

UPDATE veriyi günceller

INSERT

DELETE

SELECT database

UPDATE

## **INFORMIX’TE VERİ AKIŞI**

** **INPUT INSERT

## ** FORM 4GL DATABASE**

## ** **DISPLAY** PROGRAM **SELECT

## ** **UPDATE

## ** RAPORLAR**

## **BÖLÜM 1**

## **INFORMIX-4GL Programlarının**

## **Derlenmesi**

## **INFORMIX-4GL Programları**

Bir Informix-4GL programı bir veya birden fazla işletim sistemine ait dosya kullanabilir.Bu dosyalar module adı altında çağırılır.

Informix-4GL programları MAIN,FUNCTION ve REPORT routinelerini içerir. Module içinde bir veya daha fazla routine olabilir.Bu modüller ile birlikte routinlerde çalışabilecek olan bir programa link edilebilir.

Her Informix-4GL programı sadece bir tane MAIN routine’i içerebilir ve bu routine END MAIN ile bitmek zorundadır.

Uygulamanız dosyarla birlikte GLOBAL değişkenler ,FORM lar ve HELP mesajlarını kapsayabilir.

Informix-4GL Informix-ESQL e link edebilir.Buda c source kodundan oluşmaktadır. C kodu veya moduller assembly dilinde yazılmıştır.

## **INFORMIX-4GL Modülleri******

1.Bütün Informix-4GL modulleri .4gl uzantılı olmak zorundadır.

2.Informix-4GL programın format konusunda bir sınırlaması yoktur.Bu okumayı kolaylaştırır.

3.Informix-4GL case sensitive değildir.Yani büyük küçük harf ayrımı yoktur.

4.Informix-4GL programında yorumlar için ‘#’ veya ‘||’ kullanılır.

**Bir Modüllü INFORMIX-4GL Programı******

file.4gl

GLOBALS

...

END GLOBALS

MAIN

....

END MAIN

FUNCTION add\_cust()

....

END FUNCTION

**Bir Çok Modüllü INFORMIX-4GL Programı******

file1.4gl file2.4gl

GLOBAL GLOBALS

... ‘file1.4gl’

END GLOBALS

FUNCTION cust\_menu()

MAIN ....

... END FUNCTION

END MAIN

FUNCTION add\_cust()

...

END FUNCTION

REPORT labels()

...

END REPORT

## **INFORMIX-4GL Programı Nasıl Derlenir******

1.INFORMIX-4GL ilk olarak 4GL kodunu INFORMIX-ESQL C koduna dönüştürür ve bunun uzantısı .ec olur

2.INFORMIX-ESQL C kodu C koduna çevirir ve uzantısı .c olur.Bundan sonraki iki maddeyi tamamıyla C compiler yapar

3.C dili bir object dosyası oluşturur.Object dosyası .o ile biter.

4.Bundan sonra object dosyası INFORMIX-ESQL C kütüphanesi ve kendi kütüphanesi gibi çalışır bir program oluşturur.

**Tek Bir Modülü Derleme ve Bağlama******

file.4gl** **file.ec file.c file.o file.4ge

**Çok Modüllü Derleme ve Bağlama******

file1.4gl** **file1.ec file1.c file1.o file.4ge

file2.4gl** **file2.ec file2.c file2.o

**INFORMIX-4GL Modüllerinin Derlenmesi**

Informix-4GL modülleri direk olarak komut satırından veya 4GL menüsünden derlenebilir.

Komut satırından:

c4gl source.4gl -o outfile.4ge

Burdaki source modülününüzün ismi outfile ise çalışacak olan programın ismidir.Bu ismi kendiniz verebilirsiniz.

-e yi kullanarak .c uzantılı bir dosyayı derleyebilir ve link edebilirsiniz.

Eğer source.4gl de MAIN yoksa source.o derlenebilir fakat link edilemez.

Komut satırında size özel ESQL C source dosyası,object dosyası kullanabilirsiniz.

Syntax

c4gl source.4gl \[-e\] \[diğerargumanlar\] -o outfile

\[diğer.ec....\] \[diğer.c...\] \[diğer.o....\]

\[-l sizinkütüphaneniz....\]

Diğer argumanlar C compiler’ının içerdiği argumanlardır.

Not: Eğer özel bir output dosya ismi kullanılmamışsa default olarak output dosyası a.out olur.Informıx-4GL bunu uzantısı .4ge olan çalışır program haline getirir.

4GL Menüsünden:

Bu menuye girmek için i4gl in komut satırından girilip menu nün çıkması gerekiyor.

4GL TOP LEVEL Menu

INFORMIX-4GL : Module Form Program Query-Language Exit

Run,Modify,Create or Drop a module.

.................................................................Press CTRL-W for HELP......

Module menüsünde var olan bir modül değiştirilebilir,Yeni bir module oluşturulabilir,Module veya program derlenebilir,bir module çalıştırılabilir.

MODULE : Modify New Compile Program-Compile Run Exit

Modify a module

................................................................Press CTRL-W for HELP......

MODIFY MODULE : Object Runable Exit

Compile a module to object code

.................................................................Press CTRL-W for HELP........

COMPILE MODULE : Correct Exit

Correct a module

...................................................................Press CTRL-W for HELP

Komut satırına i4gl yazdıktan sonra ilk menu karşımıza çıkacaktır.Burdan Module seçeneğini seçtikten sonra karşımıza ikinci şekildeki menu çıkar burdanda Modify seçeneğini seçmemiz gerekir.Bu seçeneğide seçtikten sonra üçüncü şekildeki menu gelecektir.Buradaki Compile seçeneği bizim aradığımız seçenektir.Bu seçeneği seçtikten sonra bize programı object olarakmı yoksa çalışacak bir programmı olacağını gösteren iki tane seçenek vardır.Bunlardan Object olan .o uzantılı dosya üretir.Runnable ise sonu .4gi olan dosya üretir.Eğer kodda herhangi bir hata varsa karşımıza son şekildeki menu gelir ve Correct seçeneğini seçince programın kullandığı editordeki hatalı satıra gider ve hata kodunu yazar.Bu editor genellikle vi editorüdür.

## **BÖLÜM 2**

## **Menü Oluşturma**

**Menuler**

** **Informix-4GL de program yazmak istiyorsanız menü oluşturmanız gerekecektir.

Menu de yapısal olarak space bar veya hareket tuşları kullanarak menu seçeneklerine erişebilirsiniz.Eriştiğiniz seçeneğin üstünde enter tuşuna basarak o seçeneği aktif hale getirebilirsiniz.Bu işlemi seçeneğin ilk harfini klavyeden seçerekte yapabilirsiniz.

Örnek : menu1.4gl

MAIN

MENU ‘TOP LEVEL’

COMMAND ‘Customer’ ‘Go to the CUSTOMER menu .’

CALL dummy()

COMMAND ‘Orders’ ‘Add a new order.’

CALL dummy()

COMMAND ‘Stock’ ‘Go to the STOCK menu .’

CALL dummy()

COMMAND ‘Reports’ ‘Go to the REPORTS menu .’

CALL dummy()

COMMAND ‘Exit’ ‘Return to operating system.’

CALL dummy()

END MENU

CLEAR SCREEN

END MAIN

FUNCTION dummy()

ERROR ‘Function not yet implemented’

SLEEP 3

CLEAR SCREEN

END FUNCTION

**Syntax**

** **MENU ‘menu\_name’

COMMAND ‘option’\[

KEY (key-list)\]

COMMAND KEY (key-list) ‘option’

\[‘Option’u tanımlayan yardım mesajı’\]

\[HELP help\_number\]

4GL command(s)

\[CONTINUE MENU\]

\[EXIT MENU\]

\[NEXT OPTION ‘option’\]

...

END MENU

\* Her menu en az iki komut içermelidir.

\* Menu’ye vereceğimiz isim menu Optionlarının isimlerinden farklı olması gerekmektedir.

\* Eğer aynı menudeki Option isimleri aynı harflerle başlıyorsa karışıklığı önlemek için bu değerleri sayı yapabiliriz.Bunu ancak bir KEY yardımıyla yapabiliriz .

\* COMMAND KEY ‘option’ isimsiz kullanılıyorsa bu kısım menüde hidden olacak yani gözükmeyecektir.

\* INFORMIX-4GL menu isminden sonra bir kolon ekler.Her optionun arasında iki boşluk olması gerekmektedir.

\* Yardım mesajları 80 karakteri yani bir satırı aşmamalıdır.

## ** ****Menu Syntaxları:******

**key-list **Menu şeçeneklerinde aynı harfle başlayan seçenekler varsa bunların başka harflerle girişini sağlamaya yarar.

**HELP help\_no **Help key yazıldığında ekrana ilgili helpi display eder yani gösterir.

**CONTINUE MENU** Herhangi bir menu işleminden sonra menuden çıkmaz tekrar menuye devam eder.

**NEXT OPTION **Bir sonraki Option’u highlight etmek için kullanılır. Bunun amacı Çok Option lu menulerde her seferinde başa dönmesini engellemek yada yakın bir optionla ilişkilendirmektir.

**EXIT MENU **Menu den çıkar.

## **OPTIONS**

** ****ERROR LINE **Bu option herhangi bir mesajı vermeye yarar.Bu mesaj sen son satırda görüntülenir.

**PROMPT LINE **Bu optionda ekrana bir mesaj çıkar ve bu mesajın cevabının alınması beklenir.Mesela ‘Devam İçin Bir Tuşa Basınız.’gibi.Bu mesaj ilk satırda display olur.

**MESSAGE LINE **Bu optionda ekranda göstermek istediğiniz mesajı gösterir.Bu genelde 2. Satırdır.

**COMMENT LINE **Bu option yorumları ekranda display eder.Bunun default’u ise son satır -1 dir.

**HELP FILE **Bu dosyaya mesajlar ve numaraları yazılır.Yardım dosyasına adını verir.

**HELP KEY **Yardımın hangi kısayol tuşuyla kullanılacağını belirtir.

MAIN

DEFINE answer CHAR(1)

OPTIONS

PROMPT LINE 22,

MESSAGE LINE LAST,

HELP KEY CONTROL-I,

HELP FILE ‘menuhelp.ex’

MESSAGE ‘Seçeneğin ilk harfini girin veya CTRL-I ya basın’

MENU ‘TOP LEVEL’

COMMAND ‘Customer’

‘Go to the CUSTOMER menu’

HELP 1

CALL cust\_menu()

COMMAND ‘Orders’

‘add a new order.’

PROMPT ‘Do you want to place an order for’,

’ a customer?(y/n)’ FOR answer

IF answer = ‘n’ THEN

CONTINUE MENU

END IF

CALL dummy()

...

COMMAND KEY (‘E’,’X’) ‘exit’

‘Exit Menu.’

EXIT PROGRAM

COMMAND KEY (‘!’)

CALL bang()

NEXT OPTION ‘Customer’

END MENU

END MAIN

Yukarıdaki örnek menüde syntax ve optionlar işlenmiştir.Optionlar ile ilgili tüm tanımlar OPTIONS seçeneğinin altında yapılmıştır.MENU de ise komutlar optionlara uygun kullanılmıştır.

## **MKMESSAGE **

** **BİR HELP MESAJI OLUŞTURMA:

\* Bir Help dosyası numaralandırılmış mesajlar içerir.Mesaj numarası mesajın üstündeki

satırda olur ve numaradan önce nokta içerir.

\* Help dosyasını derlerken aşağıdaki komut syntax’i kullanılır.

MKMESSAGE filename1 filename2

Burda filename1 help mesajlarını içeren dosya filename2 de derleme sonucunda oluşan ve INFORMIX-4GL in kullanacağı dosyadır.

ÖRNEK:

Aşağıda menuhelp dosyasının bir editor kullanılarak oluşturulması gözüküyor.

.1

To add a row the customer table.Type the information about the customer into spaces between brackets.

.2

To place an order enter the information between square brackets.

Mkmessage menuhelp menuhelp.ex

Diyerek INFORMIX-4GL in kullanacağı .ex uzantılı bir help dosyası yapmış oluruz.

## **INFORMIX-4GL Commands**

** ****ERROR**

** Syntax**

** **ERROR ‘display-list’ \[ATTRIBUTE (attribute-list)\]

Error komutu mesajı son satırda gösterir.İstenirse bu özellik OPTIONS tanımlamalarından değiştirilebilir.

Ekrana gösterilecek error mesajı 80 karakter uzunluğunu geçmeyecek şekilde ayarlanmalıdır.

Error mesajlarının default olarak özelliği beep sesi çıkarması ve background renginin farklı olmasıdır.Bu özellikler ATTRIBUTE kullanarak değiştirilebilinir.

**ATTRIBUTE’LER******

WHITE REVERSE

YELLOW BLINK

MAGENTA UNDERLINE

RED

CYAN

GREEN

BLUE

BLACK

ÖRNEK

ERROR ‘Function not yet implemented.’

**MESSAGE**

** Syntax**

** **MESSAGE ‘Display-list’ \[ATTRIBUTE (attribute-list)\]

Default olarak MESSAGE ın display edileceği satır 2. Satırdır.İstenildiği takdirde bu seçenek OPTIONS tanımlamalarından değiştirilebilir.

Ekrana gösterilecek error mesajı 80 karakter uzunluğunu geçmeyecek şekilde ayarlanmalıdır.

Mesajın görüntüsü ATTRIBUTE ‘lerinden değiştirilebilir.

ÖRNEK

MESSAGE ‘Type the first letter of the option’

‘you want or CTRL-I for instructions.’

**PROMPT YAPISI**

** **Prompt yapısında display edilen mesaja cevap beklenir.

**Syntax**

** **PROMPT ‘display-list’ FOR \[CHAR\] variable

\[HELP help-number\]

Default olarak PROMPT un display edileceği satır ilk satırdır.İstenildiği takdirde bu seçenek OPTIONS tanımlamalarından değiştirilebilir.

PROMPT mesajından alınacak cevap ya bir program değişkeni yada bir program sabiti olmalıdır.

Alınacak cevap 1 karakter olmalıdır.

ÖRNEK:

PROMPT ‘Do you want to place an order? (y/n)’

FOR answer

**Format******

CLIPPED

Program değişkeninin veya karakter kolonunun sağındaki boşlukları atmaya yarar.

KULLANILIŞI

Dates ve nümerik alanların formatı için kullanılır.

Value Format Result

999 ‘####’ 999

999 ‘<<<’ 999

9999 ‘SSS.SSS.&.&’ S9.999.00

99 ‘S###.&&’ S 99.00

01/19/1986 ‘mm/dd/yy’ 01/19/86

01/19/1986 ‘(ddd.) mmm,dd,yyyy’ (Tue.)JAN. 19. 1986

ÖRNEK:

PROMPT ‘Do you want to place an order for’,p\_lname CLIPPED

‘? (y/n) ‘ FOR answer

ÖRNEK :Menu2.4gl

MAIN

DEFINE answer CHAR(1)

OPTIONS

PROMPT LINE 22,

MESSAGE LINE LAST,

HELP KEY CONTROL-I,

HELP FILE ‘menuhelp.ex’

MESSAGE ‘Seçeneğin ilk harfini girin veya CTRL-I ya basın’

MENU ‘TOP LEVEL’

COMMAND ‘Customer’

‘Go to the CUSTOMER menu’

HELP 1

CALL cust\_menu()

COMMAND ‘Orders’

‘add a new order.’

HELP 2

PROMPT ‘Do you want to place an order for’,

’ a customer?(y/n)’ FOR answer

IF answer = ‘n’ THEN

CONTINUE MENU

END IF

CALL dummy()

COMMAND ‘Stock’

‘Go to the stock menu.’

HELP 3

CALL dummy()

COMMAND ‘Reports’

‘Go to the reports menu.’

CALL dummy()

COMMAND ‘Personnel’

‘Go to the personnel menu.’

CALL dummy()

COMMAND ‘Accounting’

‘Go to the accounting menu.’

CALL dummy()

COMMAND KEY (‘H’) ‘sHipping’

‘Go to the shipping menu.’

CALL dummy()

COMMAND KEY (‘X’,’E’) ‘eXit’

‘Exit menu and return to operating system’

EXIT MENU

COMMAND KEY (‘!’)

CALL bang()

NEXT OPTION ‘Customer’

END MENU

CLEAR SCREEN

END MAIN

FUNCTION cust\_menu()

MENU ‘CUSTOMER’

COMMAND ‘Add’

‘Add a new customer.’

CALL dummy()

COMMAND ‘Find’

‘Look for a customer’

CALL dummy()

COMMAND ‘Update’

‘Modify customer information.’

CALL dummy()

NEXT OPTION ‘Find’

COMMAND ‘Delete’

‘Delete a customer from the database’

CALL dummy()

NEXT OPTION ‘Find’

COMMAND ‘EXIT’

‘Return the main menu’

EXIT MENU

END MENU

END FUNCTION

FUNCTION bang()

DEFINE unixcmd CHAR(80),

x CHAR(1)

CLEAR SCREEN

LET x=’!’

WHILE x=’!’

PROMPT ‘!’ FOR unixcmd

RUN unixcmd

PROMPT ‘Press RETURN to the continue.’ FOR CHAR x

END WHILE

END FUNCTION

FUNCTION dummy()

ERROR ‘Function not yet implemented’

SLEEP 3

CLEAR SCREEN

END FUNCTION

## **BÖLÜM 3**

## **FORM OLUŞTURMA**

## **FORM OLUŞTURMA******

INFORMIX-4GL formları direk olarak komut satırından oluşturulabilinir. Bunun yanısıra INFORMIX-4GL programının menüsüde kullanılırak oluşturulanabilir.

INFORMIX-4GL Menüsü kullanarak oluşturma

Komut satırından i4gl yazılır ve INFORMIX-4GL menüsüne girilir.Burdan da form seçeneği seçilir.

Form Menüsü:

FORM : Modify Generate New Compile Exit

Modify a form

..............................................................Type control-W for help............

Modify seçeneği daha önce hazırlamış olduğunuz form u geliştirmek için kullanılır.INFORMIX-4GL in kullandığı editör genelde vi dır ve default olarak bu editor karşımıza çıkar.

Generate seçeneği 0 dan bir form oluşturmaya yarar.Bunun bir wizard’ı vardır ve seçtiğimiz tabloya göre bize bir form dizayn eder.

New seçeneğinde ise size direk olarak boş bir editor açar.

Compile seçeneği ise seçtiğiniz formu derler.

Komut satırını kullanarak form oluşturma:

1.Default olarak bir form yaratmak için

form4gl -d

Daha sonra size yaratacağınız formun ismini soracaktır ve INFORMIX-4GL bunun uzantısını .per yapacaktır.Daha sonrada hangi database den hangi tabloyu seçeceğinizi sorar.

2. Bir formu modify ederken iki adım vardır.Birincisi INFORMIX-4GL menusunden ikincisi ise direk formun yazıldığı editorden yapılabilir.

3.Dosya komut satırından derlenmek isteniyorsa

form4gl filename

veya

form4gl -v filename

v seçeneği ekranda bir satırda gözükecek olan karakter sayısını ayarlar.Komut satırından derlediğimizde hata oluşursa bunları filename.err diye hataların yazıldığı bir dosyada saklayacaktır.

Derleme işlemi başarıyla tamamlandıktan sonra bizim elimizde

filename.frm

diye bir form olacaktır.

Örnek: custform.Per

DATABASE stores

SCREEN

{

CUSTOMER FORM

Number : \[f000 \]

First Name : \[f001 \] Last Name : \[f002 \]

Company : \[f003 \]

Address : \[f004 \]

\[f005 \]

City : \[f006 \]

State : \[a0\] Zipcode : \[f007 \]

Telephone : \[f008 \]

}

END

TABLES

customer

ATTRIBUTES

f000 = customer.cnum.NOENTRY;

f001 = customer.fname;

f002 = customer.lname;

f003 = customer.company;

f004 = customer.address1;

f005 = customer.address2;

f006 = customer.city;

a0 = customer.state.UPSHIFT;

f007 = customer.zip;

f008 = customer.phone.PICTURE = ‘###-###-####’;

END

**ATTRIBUTE LER**

AUTONEXT Cursor’ın bulunduğu alan dolmuşsa otomatik olarak bir sonraki alana geçer.

COMMENTS Cursor mesajlanmış özel alana geldiği zaman yorum satırı olan 23. Satırda o alanla ilgili olan yorum çıkar.Comment satırı OPTIONS seçeneği yardımı ile değiştirilebilinir.

DEFAULT O alana default olarak bir değer atar.Bu alanları INPUT veya INPUT ARRAY komutları ile alırken karışıklık olmasın diye WITHOUT DEFAULTS cümleciğinide kullanabiliriz.TODAY sözcüğü ise içinde bulunduğumuz tarihi date field ının içine display eder.

INCLUDE O alana yazılabilecek değerleri gösterir.Bunlar spesifik değerler olabilir.Bunların Ascii karakterleri olması gerekir.

PICTURE Alanları dizayn etmeye yarar.Bunlar sosyal sigorta numarası telefon numarası gibi alanlar olabilir.Bu dizayn için 3 sembol kullanılır.

Bu semboller:

A Harfler için

\# Numaralar için

X Karakterler için

UPSHIFT Küçük harfleri büyük harfe çevirir.

DOWNSHIFT Büyük harfleri küçük harflere çevirir.

VERIFY Kullanıcının data iki kez girmesi gerekli olan önemli datanın saklandığı alanlarda kullanılır.Örnek olarak password yapısını verebiliriz.Burda yanlışlık olmasın diye password arka arkaya iki kez girilir.

REVERSE Alanı REVERSE modda gösterir.Bazı terminaller bunu desteklemez ve bunun yerine <> bu işaretler arasında gösterir.

FORMAT DECIMAL,SMALLFLOAT,FLOAT,DATE alanlarını formatlamak için kullanılır.

mm.dd.yy 09.15.85

mmm dd.yyyy Sep 15.1985

dd-mm-yy 15-09-85

(ddd.) mmm.dd.yyyy (Sat) Sep. 15. 1985

##.## 89.85

##.# 89.9

\## 90

NOENTRY Bu alana giriş yapılamaz.

REQUIRED Bu alanın INPUT veya OUTPUT ARRAY

kullanımında işlemi hızlandırır.

EKRAN KAYITLARI :

Ekran kayıtları alan veya alan gruplarını adreslemek için kullanılır.

Bir formda her tablonun içerdiği yanlızca bir tane SCREEN RECORD vardır.Bu formdaki tüm alanları içerir.

Custform

Number : \[ \]

First Name : \[ \] Last : \[ \]

Company : \[ \]

Address : \[ \]

\[ \]

City : \[ \]

State : \[ \] Zipcode : \[ \]

Telephone : \[ \]

customer

cnum

fname

lname

address1

address2

city

state

zip

phone

## **BÖLÜM 4******

## **DATABASE’E VERİ EKLEME******

**PROGRAM YAZARKEN FORM KULLANMA**

** **Form bir program yaratılmadan ve compile edilmeden önce oluşturulmalıdır.Form un 4GL programı içinde kullanımı şu şekildedir.

OPEN FORM form\_identifier FROM ‘form-file’

Form\_identifier INFORMIX-4GL programı tarafından refere edilen bir isimdir ve programın içinde formla ilgili işlemler yapılmak istenirse form bu isimle çağırılır.

Form dosyası derlenirken path inde uzantı olarak .frm yazılmaz.Bununla birlikte form programdan önce derlenmiş olmalıdır.

Form\_identifier alanı bir programda globaldir.

DISPLAY FORM form\_identifier

DISPLAY FORM komutu bir formu ekranda göstermek için kullanılır.

MAIN

OPEN FORM cust\_form FROM ‘custform’

DISPLAY FORM cust\_form

...

END MAIN

Not: Form\_identifier ve form-name in form-file ının tüm path ismini kullanmasına ihtiyaç duymazlar.Çünkü bunlar özel değildirler.

**EKRAN GÖRÜNTÜSÜ**

** ** Form 3. ve 22. Satırlar arasında terminal ekranında gözükecektir.Ekranın ilk satırı PROMPT lar için ayrılmıştır.İkinci satır ise mesajlara ayrılmıştır.Bunun yanısıra 23. Satır COMMENT lere ve 24. Satır da ERROR lara ayrılmıştır.

1 prompts lar bu satırda gösterilir.

2 4GL den alınan mesaj komutları bu satırda gözükür

3 Ekran formu bu satırdan itibaren gösterilir.

.

.

.

23 COMMENT ler bu satırda yazılır.

24 Hatalar burda gösterilir.

Not : Üstteki satırlar default satırlardır.Bunlar OPTIONS tan değiştirilebilir.

OPEN WINDOW

Syntax

OPEN WINDOW WİNDOW-NAME at row,column

WITH {integer ROWS, ,integer COLUMNS } FORM ‘form-file’

\[ATTRIBUTE (Attribute-list)\]

Bir FORM’un WINDOW ile Büyüklüğünün Ayarlanması

OPEN WINDOW w\_cust AT 3,3

WITH FORM ‘custform’

ATTRIBUTE (BORDER)

Eğer bir formun boyutunu ayarlıyorsanız aşağıdaki komutları kullanamazsınız:

OPEN FORM,DISPLAY FORM,CLOSE FORM.

Bir formun boyutu WINDOW ile ayarlanıyorsa WINDOW un boyutu form daki boşlukları içermelidir.

Bir WINDOW un büyüklüğü aşağıdaki gibi hesaplanır.Aşağıdaki örnekte 10 satırlık bir form düşünülmüştür.Burda default form satırı alınmıştır.Buda 3. Satırdır.

Formula Example

Length of the form 10

+1 Comment line +1

+Form satırının başlangıcı-1 +(3-1)

window uzunluğu 13

Bir WINDOW içinde FORM açmak

OPEN WINDOW w\_cust AT 3,3

WITH 11 ROWS,65 COLUMNS

ATTRIBUTE (BORDER)

OPEN FORM cust\_form FROM ‘custform’

DISPLAY FORM cust\_form

Burda önemli olan nokta ilk önce window’u açıp sonra Formu display etmektir.

Window’un başlangıcı (3,3) olacağından border’ın başlangıcı (2,2) olacaktır.

Eğer window boyutunuz form boyutuna göre kısa kalırsa veya window boyutu ekran boyutunu aşarsa run-time error larla karşılarsınız.

**WINDOW Özellikleri**

Window özellileri OPTIONS ta display edilecek satırları değiştirmek için kullanılır.

Attribute Default

BORDER no border

REVERSE no reverse

PROMPT LINE FIRST

MESSAGE LINE FIRST - 1

FORM LINE FIRST + 2

COMMENT LINE LAST

Not :Error mesajları daima ana ekranda yada bağlı olduğu ekranda çıkar window içinde çıkmaz.

CLEAR Komutları

CLEAR SCREEN

CLEAR komutu ekranı temizlemek için kullanılır.

CLEAR FORM

Burdaki CLEAR ise formu temizlemek için kullanılır.Burda form kalır ama formun içindeki bilgiler silinir.

CLEAR field-list

Burdaki CLEAR ise seçilen bir alanı silmeye yarar.Örneğin CLEAR adı\_soyadı dediğimizde ekrandaki tüm adı\_soyadı bölümleri silinir.

CLEAR WINDOW window-name

WINDOW alanını temizler fakat border kalır.

CLOSE Komutları

CLOSE FORM form-name

Bu komut form-name de verilen formu kapatır.

CLOSE WINDOW window-name

Bu komutta belirtilen window u kapatır.Ancak altındaki formu gösterir.

CURRENT WINDOW IS window-name

Hangi pencerenin öncelikle işlem yapacağını ön plana çıkacağını belirlememize yarar.

DATABASE’E VERİ EKLEYEN BİR POGRAM YAZMA

Form bir window içinde açık olmalı yada direk olarak ekranda görünmelidir.

Kullanıcı forma veri girmelidir.

Her alandaki data INPUT komutuyla program değişkenlerine atanmalıdır.

Veriler database’e eklenene kadar program değişkenleri olarak saklanmalıdır.

Enter data screen INPUT program INSERT

record variables database

**PROGRAM DEĞİŞKENLERİNİN TANIMLANMASI******

Program değişkenleri mutlaka ilk olarak tanımlanmalıdır.

DEFINE yapısı MAIN,FUNCTION veya GLOBALS yapılarından sonra gelmek zorundadır.

DEFINE yapısında birkaç tane değişken tanımlanabilir.

Değişken İsimlendirmedeki Kriterler

Değişken isminin uzunluğu 1 ile 18 karakter arasında olabilir.

Eğer 8 i geçerse ilk 8 karakteri aynı olmamalıdır.

Değişken isimleri karakterle başlamalıdır.Değişken isminde harf,numara,underscore lar bulunabilir.

Büyük ile küçük harf arasında ayırım yoktur.

Eğer değişken ismiyle database ismi ,tablo ismi veya kolon ismi aynı olursa program database i table i ve kolonu değişken gibi görecektir.Bu gibi durumlarda tablodan önce @ işareti koymak gerekmektedir.

Değişken Tipleri

Değişkenler kesin ve açık olmalıdır.

DEFINE answer CHAR (1)

Değişkenler bir database kolonunu işaret edebilirler bu gibi durumlarda DEFINE yapısı aşağıdaki gibi olur.

DEFINE p\_lname LIKE customer.lname,

p\_fname LIKE customer.fname

Database de bu kolonların ismi değiştiği zaman program yeniden derlenmelidir.

Değişkenler Kayıt yapısı şeklinde tanımlanabilirler.

DEFINE p\_customer RECORD LIKE customer.\*

DEFINE p\_name RECORD fname CHAR(10),

lname CHAR(20)

END RECORD

Değişkenler dizi şeklinde tanımlanabilirler.

DEFINE a\_customer ARRAY\[10\] OF RECORD

p\_lname LIKE customer.lname,

p\_fname LIKE customer.fname

END RECORD

Program Elemanlarının Alanları

Program Elemanları Alanları

Değişkenler GLOBAL Program

Local Function

Identifiers Forms Program

Windows Program

Değişken : Tanımlanır ve özel bir değerdir ve saklanır.

Identifier : Bir değişkene yada saklanan birşeye referans eder.Örneğin form bir dışsal dosya olarak tanımlanır.

GLOBALS YAPI

GLOBALS yapısı MAIN programın dışında olmalıdır.

Eğer bir database kolonunu global değişken olarak tanımlıyorsanız DATABASE yapısı GLOBALS in önünde tanımlanmalıdır.

GLOBALS yapı daha önceden başka dosyalarda tanımlanmış olan global değişkenlere referans oluşturmak için kullanılır.Bu dosayaların uzantısı .4gl olmalı ve compile edilmelidir.

GLOBAL Değişken Tanımlama :

DATABASE stores

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

GLOBAL Değişkene Referans Olma :

GLOBALS

‘global.4gl’

MAIN

...

END MAIN

FUNCTION add\_cust()

DEFINE flag CHAR (1)

...

END FUNCTION

Değişkenlerin Alanları :

Eğer global değişkenle local değişkene aynı isme sahipseler local değişken önceliği kendisine alır.

DATABASE STORES

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*,

switch CHAR(1)

END GLOBALS

MAIN

DEFINE answer CHAR(1)

.

.

.

END MAIN

FUNCTION add\_cust()

DEFINE flag CHAR(1)

switch CHAR(1)

.

.

.

END FUNCTION

DEFINE

yapılarının

yeri Değişken Tip Alan

MAIN answer local MAIN

FUNCTION flag local FUNCTION

GLOBALS p\_customer global MAIN

FUNCTION

FUNCTION switch local FUNCTION

GLOBAL switch global MAIN

**LET ve INITIALIZE YAPILARI**

LET yapısı bir değişkene bir değer atamak için kullanılır.

LET p\_lname = ‘Smith’

LET yapısında nümerik değerler,stringler veya boolean yapılar kullanabilirsiniz.

LET counter = 1

LET p\_lname = ‘Smith’

LET chosen = False

Değişkenler program tarafından oluşturulabilir.

LET cnt = 1

LET cnt = cnt+1

Değişkenler NULL değeri alabilir.

LET unitprice = NULL

INITIALIZE unitprice TO NULL

Eğer Null Değişken bir işlemde kullanılıyorsa işlemin sonucuda Null olur.

LET result = unitprice\*qty

Bir değişken listesi oluşturabilirsiniz.

INITIALIZE p\_customer.\* TO NULL

INITIALIZE p\_customer.\* LIKE customer.\*

Örnek :

DATABASE stores

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

...

OPEN WINDOW w\_cust AT 3,3

WITH FORM ‘custform’

ATTRIBUTE(BORDER)

MENU ‘CUSTOMER’

COMMAND ‘Add’

‘Add one new customer.’

CALL add\_cust()

COMMAND ‘EXIT’

CLEAR SCREEN

EXIT MENU

END MENU

CLEAR SCREEN

END MAIN

FUNCTION add\_cust()

...

LET p\_customer.cnum = 0

...

END FUNCTION

**INPUT YAPISI**

** **INPUT komutu ekrandaki bulunan formdaki değişkenlere program değişkenlerine atar.

Enter data screen INPUT program INSERT

record variables database

INPUT yapısı ekranda gösterilen bunlara default olarak alanlarda gösterilenlerde dahil, verilere değişkenlere atar değer olmayan alanlara karşılık gelen değerlerede null atar.

Kullanıcı Alanlar arasında ok tuşlarıyla veya enter tuşuyla dolaşırken her tuşa bastığında bir önceki alana yazdığı set edilir.

GENEL Syntax

INPUT variable-list FROM field-list

INPUT variable THRU variable FROM field-list

INPUT BY NAME variable THRU variable

INPUT BY NAME variable-list

INPUT Yapısına Örnekler

Örnek 1:

INPUT p\_customer.fname,

p\_customer.lname,

p\_customer.company,

p\_customer.address1,

p\_customer.address2,

p\_customer.city,

p\_customer.state,

p\_customer.zip,

p\_customer.phone,

FROM fname,

lname,

company,

address1,

address2,

city,

state,

zip,

phone

Örnek 2:

INPUT p\_customer.\* FROM customer.\*

Eğer program değişkeni ile ekran alanı aynı isimdeyseler INPUT BY NAME i kullanıp sadece değişken isimlerini kullanabilirsiniz.

Örnek 3:

INPUT BY NAME

p\_customer.fname THRU p\_customer.phone

Örnek 4:

INPUT BY NAME p\_customer.\*

INPUT Yapısından Çıkma :

INPUT yapısı kullanıcı son alanı doldurduktan sonra veya ESCAPE tuşuna bastığı zaman biter.

DEL tuşu ile anormal bitirme yapılır.Eğer özel olarak DEFER INTERRUPT varsa DEL tuşu INPUT işlemini sonlandıracaktır.

OPTIONS Taki INPUT Yapısı :

WRAP seçeneği alanlar bittikten sonra ENTER tuşuna basılınca cursor’u

ekranın tepesine götürür.Default olanı WRAP olmayandır.

ACCEPT KEY seçeneği özel olarak bir tuş kontrolü yada INPUT yapısını sonlandıran bir INTERRUPT gibi kullanılır.

OPTIONS

INPUT WRAP

ACCEPT KEY F1

Örnek :

DATABASE stores

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

...

OPTIONS

MESSAGE LINE LAST

INPUT WRAP

OPEN WINDOW w\_cust AT 3,3

WITH FORM ‘custform’

ATTRIBUTE (BORDER)

MENU ‘CUSTOMER’

COMMAND ‘Add’

‘Add one new customer.’

CALL add\_cust()

COMMAND ‘EXIT’

CLEAR SCREEN

EXIT MENU

END MENU

CLEAR SCREEN

END MAIN

FUNCTION add\_cust()

...

INPUT BY NAME p\_customer.fname THRU p\_customer.phone

LET p\_customer.cnum = 0

...

END FUNCTION

Bu özel alanların girişini kontrol etmemize izin verir.

Syntax

INPUT | BY NAME variable-list | variable list

FROM | field-list | screen-record \[\[n\]\].\* |

\[HELP help-number\]

\[{BEFORE FIELD field-list

| AFTER |FIELD field-list | INPUT |

|ON KEY (key-list) }

statement...

\[NEXT FIELD field-name\]

\[EXIT INPUT\]

...

END INPUT \]

INPUT Yapısındaki Opsiyonel Maddeler :

HELP Bu madde bir help mesajı kullanmak içindir.

BEFORE FIELD Herhangi bir alandan önce yapılması istenen işlemlerin yapılması için kullanılır.

AFTER FIELD Herhangi bir alandan sonra yapılması istenen işlemlerin yapılması için kullanılır.

AFTER INPUT Bu INPUT komutu sonlandıktan sonra datanın doğruluğunun kontrol edilmesi için kullanılır.

ON KEY Bu işlemde fonksiyon tuşları (F1-F36 arası) kontrol tuşları (CONTROL-B....) , ESCAPE tuşu veya INTERRUPT Tuşları kullanılabilinir. Bunlar bazı görevler için kullanılırlar.Bunun yanısıra aşağıdaki kontrol tuşları kullanılamaz:

CONTROL-A,CONTROL-D,CONTROL-H,CONTROL-J,CONTROL-L, CONTROL-M,CONTROL-Q,CONTROL-R,CONTROL-S,CONTROL-X.

Bu tuşlar editor tarafından ayırılmıştır.

NEXT FIELD Cursor’un hareketini kontrol altına almak için kullanılır.

END INPUT INPUT yapısına bitirmek için kullanılır.

DISPLAY

Syntax

DISPLAY ‘display-list’ \[AT row,column\] \[ATTRIBUTE (attribute-list)\]

DISPLAY variable-list TO field-list

DISPLAY BY NAME variable-list

DISPLAY yapısı stringleri ve program değişkenlerini yazmak için kullanılır.

DISPLAY ‘Updating Customer Record For ‘, v\_lname

AT maddesi yazıcağımız yerin ekrandaki adresini belirtmek için kullanılır.

DISPLAY v\_lname CLIPPED, ‘ record is being updated.’

AT 24,1

Bir satır silinmek isteniyorsa aşağıdaki komut kullanılır.

DISPLAY ‘ ‘ AT 1,1

DISPLAY yapısı program değişkenlerinden form alanlarına direk olarak yazma işleminide yapar.

DISPLAY p\_customer.fname,

p\_customer.lname,

TO customer.fname,

customer.lname

DISPLAY BY NAME Syntax’ı ise değişken değerlerini form alanları içinde gösterir.

DISPLAY BY NAME p\_customer.\*

INSERT Yapısı :

Syntax

INSERT INTO table-name \[(column-list)\]

| VALUES (value-list) | SELECT statement

Örnekler :

INSERT INTO customer

VALUES (p\_customer.\*)

INSERT INTO customer (fname,lname)

VALUES (p\_customer.fname,p\_customer.lname)

DATABASE stores

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

...

OPTIONS

MESSAGE LINE LAST

INPUT WRAP

OPEN WINDOW w\_cust AT 3,3

WITH FORM ‘custform’

ATTRIBUTE (BORDER)

MENU ‘CUSTOMER’

COMMAND ‘Add’

‘Add one new customer.’

CALL add\_cust()

COMMAND ‘EXIT’

CLEAR SCREEN

EXIT MENU

END MENU

CLEAR SCREEN

END MAIN

FUNCTION add\_cust()

...

INPUT BY NAME p\_customer.\*

ON KEY (CONTROL-E)

CLEAR FORM

INITIALIZE p\_customer.\* TO NULL

NEXT FIELD fname

END INPUT

LET p\_customer.cnum = 0

INSERT INTO customer VALUES (p\_customer.\*)

LET P\_CUSTOMER.CNUM = SQLCA.SQLERRD\[2\]

DISPLAY BY NAME p\_customer.cnum

END FUNCTION

Burdaki SQLCA.SQLEERD\[2\] başlı başına kullanılan bir yapıdır.Bu INFORMIX-4GL in SQLCA (SQL Communication Access) özelliğine aittir.SQLCA kayıtları şu şekildedir.

DEFINE SQLCA RECORD

SQLCODE INTEGER,

SQLERRD ARRAY \[6\] OF INTEGER,

SQLWARN CHAR(8)

END RECORD

SQLCODE global değişken olan STATUS a eşitlenir.Bunun sonucunda RDSQL yapısı çalıştırılır.Eğer STATUS değeri 0 ise RDSQL yapısı başarılmıştır.Eğer 0 dan küçükse başarılmamıştır.100 ise RDSQL yapısı bulunamamıştır.

Programda kullanılan SQLERRD\[2\] ise başarıyla database e eklenen son satır numarasını gösterir.

Add\_customer Fonksiyonunu tam anlamıyla yazarsak.

FUNCTION add\_cust ()

DISPLAY ‘ ‘ AT 1,1

DISPLAY ‘ ‘ AT 2,1

DISPLAY ‘Press ESC to enter data.CTRL-E to EXIT’

AT 1,1

DISPLAY ‘Press DEL to abort.’

AT 2,1

INPUT BY NAME p\_customer.fname THRU p\_customer.phone

ON KEY (CONTROL-E)

CLEAR FORM

INITIALIZE p\_customer.\* TO NULL

NEXT FIELD fname

END INPUT

LET p\_customer.cnum = 0

INSERT INTO customer VALUES (p\_customer.\*)

LET P\_CUSTOMER.CNUM = SQLCA.SQLERRD\[2\]

DISPLAY BY NAME p\_customer.cnum

MESSAGE ‘The customer has been added to database’

SLEEP 3

CLEAR FORM

END FUNCTION

WHENEVER Komutu :

Default Olarak Run-Time Hataları İçin :

Genellikle bizim yazdığımız program çeşitli şekillerde database e erişmek isteyecektir.Bu çeşitlilik yazdığımız kodla olur.INFORMIX-4GL derleyicisi bunu önceden derlerken kontrol etmiştir. Fakat program çalışması aşamasında bu erişimi RDSQL kontrol eder.Bu hata oluşuncada program kırılır.

İşte bu tip hataları kontrol altına almak için WHENEVER komutu kullanılır.

Syntax

WHENEVER ERROR

{ GOTO label |

CALL function-name |

CONTINUE

}

Burdaki syntaxta Call function-name de programın neresinde olursa olsun o fonksiyona gidiyor.Continue de ise hatayı dikkate almıyor.

WHENEVER ERROR STOP ise hata oluştuğunda programı durdur anlamına geliyor.Bu WHENEVER koşulu için Default değerdir.

Örnek 1:

Burda INSERT yapısı sırasında bir hata meydana gelirse program hatayı yoksayıp devam edecektir.Programda WHENEVER olmazsa program duracak ve IF STATUS bloğu asla işlemeyecektir.

WHENEVER ERROR CONTINUE

INSERT ...

IF STATUS < 0 THEN

ERROR ‘Error number’,

STATUS USING ‘####’,

‘has occured.’

RETURN

END IF

WHENEVER ERROR STOP

Örnek 2:

INSERT işlemi sırasında hata oluşursa db\_error fonksiyonu çağırılacaktır.

WHENEVER ERROR CALL db\_error

INSERT ....

WHENEVER ERROR STOP

FUNCTION db\_error()

ERROR ‘An error has occured.’

EXIT PROGRAM

END FUNCTION

Program Elemanları Alanları

Program Elemanları Alan

Değişkenler GLOBAL Program

Local Function

Identifiers Forms Program

Windows Program

Komutlar WHENEVER Module

**AKIŞ KONTROL YAPILARI:**

**IF THEN**

Syntax

IF Boolean-expr THEN

statement

\[ELSE

statement\]

END IF

**WHILE**

Syntax

WHILE Boolean-expr

statement

| EXIT WHILE

statement

| CONTINUE WHILE

statement

END WHILE

**RETURN**

RETURN komutu bulunduğu fonksiyonu terkederek genel programda kaldığı yere geri döner.

Örnek :

MAIN

...

CALL find\_cust()

... MAIN

END MAIN

FUNCTION find\_cust() CALL RETURN

...

RETURN

END FUNCTION find\_cust

**KULLANICI GİRİŞLERİNİ KESEN INTERRUPTLAR**

INFORMIX-4GL kullanıcı girişlerini interruptlarla kesmeye izin verir.Kesme tuşu DEL ve çıkma tuşu ise CONTROL-Q dur.

DEFER INTERRUPT Komutu :

Default olarak DELETE tuşuna basılınca program çalışma sırasında işletimini kesecektir.

Global değişken olan INT\_FLAG program kontrolüne izin verir.Yani burda DELETE tuşuna basılıp basılmadığını kontrol eder.

DEFER INTERRUPT komutu INT\_FLAG değişkenini otomatik olarak FALSE veya 0 yapıyor.

Program başlayınca INT\_FLAG default olarak 0 olur.Hata oluşunca INT\_FLAG = TRUE veya 1 olur.

INTERRUPT KEY aşağıdaki komutları sonlandırır:

INPUT,INPUT ARRAY,CONSTRUCT,PROMPT,DISPLAY ARRAY

DİAGRAM

DEFER INTERRUPT DEFER INTERRUPT

içermeyen çalışan bir program içeren çalışan bir program

DEFER

INTERRUPT

INT\_FLAG=FALSE

Operatör tipi Operatör tipi

DEL Tuşu DEL Tuşu

INT\_FLAG=TRUE

INPUT yapısı

kesildi

Program IF yapısı

Kesildi eylemi düzenledi

Program RESET lendi

INT\_FLAG = FALSE

Program Elemanları Alanları:

Program Elemanları Alanları

Değişkenler GLOBAL Program

Local Function

Identifiers Forms Program

Windows Program

Komutlar DEFER Program

WHENEVER Module

Örnek:

Aşağıdaki örnekte add\_cust() fonksiyonunda program kontrolü ile ilgili komutlar yer almaktadır.

FUNCTION add\_cust ()

DISPLAY ‘ ‘ AT 1,1

DISPLAY ‘ ‘ AT 2,1

DISPLAY ‘Press ESC to enter data.CTRL-E to EXIT’

AT 1,1

DISPLAY ‘Press DEL to abort.’

AT 2,1

INPUT BY NAME p\_customer.fname THRU p\_customer.phone

ON KEY (CONTROL-E)

CLEAR FORM

INITIALIZE p\_customer.\* TO NULL

NEXT FIELD fname

END INPUT

IF INT\_FLAG = TRUE THEN

LET INT\_FLAG = FALSE

ERROR ‘Data entry aborted’ü

CLEAR FORM

RETURN

END IF

LET p\_customer.cnum = 0

WHENEVER ERROR CONTINUE

INSERT INTO customer VALUES (p\_customer.\*)

IF STATUS < 0 THEN

ERROR ‘Error Number’,

STATUS USING ‘####’,

‘has occured.’

RETURN

END IF

WHENEVER ERROR STOP

LET P\_CUSTOMER.CNUM = SQLCA.SQLERRD\[2\]

DISPLAY BY NAME p\_customer.cnum

MESSAGE ‘The customer has been added to database’

SLEEP 3

CLEAR FORM

END FUNCTION

## **BÖLÜM 5**

## **DATABASE SORGULAMA******

TEK SATIRLI **SELECT **YAPISI

Program değişkenleri içnde saklanmış olan veriler SELECT ile geri dönerler.

Syntax

SELECT clause

\[INTO CLAUSE\]

FROM clause

\[WHERE clause\]

\[GROUP BY clause\]

\[HAVING clause\]

\[ORDER BY clause\]

\[INTO TEMP clause\]

Örnek : Select1.4gl

Aşağıdaki program yalnızca 1 satır geri döndürür.

DATABASE STORES

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

DEFINE p\_count INTEGER

OPEN FORM f\_cust FROM ‘custform’

DISPLAY FORM f\_cust

PROMPT ‘Enter customer number : ‘ FOR p\_customer.cnum

SELECT \* INTO p\_customer.\*

FROM customer

WHERE cnum = p\_customer.cnum

SELECT count (\*) INTO p\_count

FROM orders

WHERE orders.cnum = p\_customer.cnum

DISPLAY BY NAME p\_customer.\*

DISPLAY ‘Number of orders : ‘,p\_count AT 16,1

END MAIN

ÇOK SATIRLI **SELECT **YAPISI

SELECT yapısı çalıştığı zaman arama kriterimize göre tüm satırları getirmesini isteriz.

Problem :

RDSQL sadece bir zamanda sadece bir tane satır getirme yetkisine sahiptir.Biz nasıl bir operasyon ile birden fazla satır gelmesini sağlamalıyız.

Çözüm :

Burda bizim satırlara geri dönmemizi sağlayacak bir pointer’a ihtiyacımız vardır.Bu metod CURSOR diye adlandırılır.CURSOR o andaki işaret edilen satırı getirir.

Cursor

NOT FOUND

DECLARE YAPISI

DECLARE YAPISI bir CURSOR ile çalışabilir durumdaki RDSQL yapısını bir araya getirir.

Syntax

DECLARE cursor\_name CURSOR FOR sql-statement

Program Elemanları Alanları:

Program Elemanları Alanları

Değişkenler GLOBAL Program

Local Function

Identifiers Forms Program

Windows Program

Cursors Module

Komutlar DEFER Program

WHENEVER Module

OPEN YAPISI

OPEN yapısı herhangi bir cursor u select işlemi için aktif hale getirir.

Syntax

OPEN cursor-name \[USING variable-list\]

USING in anlamı cursor u herhangi bir program değişkenine atamak içindir.

FETCH YAPISI

FETCH yapısı aktif hale getirdiğimiz verileri okumak için kullanılır.

Syntax

FETCH cursor-name \[INTO variable-list\]

Son satıra gelince global değişken olan STATUS 100 değerini işaret eder ve buda NOTFOUND anlamına gelir.

CLOSE YAPISI

Bu aktif olan cursor setini kapatır.

Syntax

CLOSE cursor-name

AKTİF HALE GELEN BİR CURSOR SETİNİN HAREKETİ

DECLARE cursor

OPEN cursor

FETCH cursor

FETCH cursor

FETCH cursor

FETCH cursor

NOT FOUND

CLOSE cursor

Her fetch bir kayıt okur.Kayıt kalmadığı zaman Status değişkeni NOT FOUND anlamına gelen 100 değerini alır.Close cursor komutu ilede cursor seti kapatılır.

Örnek :

DATABASE STORES

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

DEFINE answer CHAR(1)

OPEN FORM f\_cust FROM ‘custform’

DISPLAY FORM f\_cust

DECLARE pointer1 CURSOR FOR

SELECT \*

FROM customer

ORDER BY lname

OPEN pointer1

WHILE TRUE

FETCH pointer1 INTO p\_customer.\*

IF STATUS = NOTFOUND THEN

EXIT WHILE

END IF

DISPLAY BY NAME p\_customer.\*

PROMPT ‘Type carriage RETURN to continue’

FOR CHAR answer

END WHILE

CLOSE pointer1

CLEAR SCREEN

END MAIN

FOREACH DÖNGÜSÜ

FOREACH sorgu için yazılmış yapıyı sırayla her satıra uygular ve sonuca geri döndürür.

FOREACH OPEN,FETCH,CLOSE komutlarının birleşimidir diyebiliriz.

Syntax

FOREACH cursor-name \[INTO program-variable\]

DISPLAY program-variable TO screen-record

END FOREACH

Örnek :

DATABASE STORES

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

DEFINE answer CHAR(1)

OPEN FORM f\_cust FROM ‘custform’

DISPLAY FORM f\_cust

DECLARE pointer1 CURSOR FOR

SELECT \*

FROM customer

ORDER BY lname

FOREACH pointer1 INTO p\_customer.\*

DISPLAY BY NAME p\_customer.\*

PROMPT ‘Type carriage RETURN to continue.’

FOR CHAR answer

END FOREACH

CLEAR SCREEN

END MAIN

SCROLLING CURSOR

Syntax

DECLARE cursor\_name SCROLL CURSOR FOR select-stmt

FETCH NEXT

PREVIOUS | PRIOR

FIRST

LAST

RELATIVE m

ABSOLUTE m

cursor-name INTO variable-list

NEXT : Bir sonraki kaydı getir anlamında kullanılır.

PREVIOUS,PRIOR : Bir önceki kaydı getir anlamında kullanılır.

FIRST : İlk kayda gider.

LAST : Son kayda gider.

RELATIVE m : Bulunulan pozisyondan m kayıt kadar ileri gider.

ABSOLUTE m : İlk kayıttan m kadar ileri gider.

FETCH in default olarak değeri NEXT tir.

Tüm SCROLL fonksiyonları SCROLLing CURSOR olarak tanımlanmalıdır.Tanımlanmazsa bu fonksiyonlar kullanılamaz.

SCROLLing CURSOR u Databasedeki veriyi güncelleştirme veya silme için kullanamayız.

Örnek :

FUNCTION find\_init ()

DECLARE pointer1 SCROLL CURSOR FOR

SELECT \* FROM customer

ORDER BY lname

OPEN pointer1

END FUNCTION

FUNCTION first\_cust ()

FETCH FIRST pointer1 INTO p\_customer.\*

CALL display\_cust()

END FUNCTION

Örnek :

DATABASE stores

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

DEFER INTERRUPT

CALL find\_cust()

CALL cust\_menu()

END MAIN

FUNCTION find\_cust ()

DECLARE pointer1 SCROLL CURSOR FOR

SELECT \* FROM customer

ORDER BY lname

OPEN pointer1

END FUNCTION

FUNCTION cust\_menu()

OPEN FORM f\_cust FROM ‘custform’

DISPLAY FORM f\_cust

MENU ‘CUSTOMER’

COMMAND ‘Find’

‘Look for a specific customer.’

CALL find\_menu()

COMMAND ‘EXIT’

‘EXIT menu’

EXIT MENU

END MENU

CLEAR SCREEN

END FUNCTION

FUNCTION find\_menu ()

MENU ‘FIND’

COMMAND ‘First’

‘Find first customer’

CALL first\_cust()

COMMAND ‘Next’

‘Find next customer’

CALL next\_cust()

COMMAND ‘Previous’

‘Find previous customer’

CALL prev\_cust()

COMMAND ‘Last’

‘Find Last customer’

CALL last\_cust()

COMMAND ‘Exit’

‘Exit Menu’

EXIT MENU

END MENU

END FUNCTION

FUNCTION first\_cust()

FETCH FIRST pointer1 INTO p\_customer.\*

IF STATUS = NOTFOUND THEN

ERROR ‘There are no customers.’

ELSE

CALL display\_cust()

END IF

END FUNCTION

FUNCTION next\_cust()

FETCH NEXT pointer1 INTO p\_customer.\*

IF STATUS = NOTFOUND THEN

ERROR ‘You are at the end of list’

ELSE

CALL display\_cust()

END IF

END FUNCTION

FUNCTION prev\_cust()

FETCH PRIOR pointer1 INTO p\_customer.\*

IF STATUS = NOTFOUND THEN

ERROR ‘You are at the beginning of the list ’

ELSE

CALL display\_cust()

END IF

END FUNCTION

FUNCTION last\_cust()

FETCH LAST pointer1 INTO p\_customer.\*

IF STATUS = NOTFOUND THEN

ERROR ‘There are no customers.’

ELSE

CALL display\_cust()

END IF

END FUNCTION

FUNCTION display\_cust()

DISPLAY AT 1,1

DISPLAY AT 2,1

DISPLAY BY NAME p\_customer.\*

END FUNCTION

ARAMA KRİTERLERİ

Bir database de bir kayıt araken belli kriteler olmalıdır ve bu kriterler WHERE ile birlikte yazılır.Bu kriterler aşağıdaki gibidir.

= Eşitlik.NULL değerlerini aramak gibi kullanılabilir.

> Büyüktür.

< Küçüktür.

>= Büyük eşit

<= Küçük eşit

\* CHAR veri tipinde arama yaparken kullanılır.Örnek olarak kullanıcı yerine kul\* diye yazabiliriz.

? Bu işaretinde kullanımı benzerdir.Bu arayacağımız karakter dizisindeki bir tane karakteri hatırlıyamıyorsak kullanılır. Kul?lanıcı

: Sınır aranacak değerlerin sınırıdır.Örnek 1:100 gibi.

| Alternatif değerdir.Örnek Brown|Smith gibi.

CONSTRUCT YAPISI

CONSTRUCT yapısı forden verileri alır ve SELECT yapısında kullanılmak üzere boolean bir değişken oluşturur.

Diagram

CUSTOMER FORM

Number : \[ \]

First Name : \[ \] Last Name : \[ \]

Company : \[ \]

Address : \[ \]

\[ \]

City : \[Menlo Park \]

State : \[ \] Zipcode : \[ \]

Telephone : \[ \]

Kullanıcı arama kriterini Forma girer.Burda arama kriteri City olan ‘Menlo Park’ tır.

Daha sonra kullanıcı ESCAPE tuşuna basar.

CONSTRUCT yapısıda aşağıdaki string’ i oluşturur:

customer.city = ‘Menlo Park’

Syntax

CONSTRUCT variable ON column-list

FROM form-field-list

CONSTRUCT BY NAME variable ON column-list

CONSTRUCT yapısı kullanıcının bir veya daha fazla alana veri girmesini bekler.

ESCAPE veya DEL tuşuna basılınc veri girme işlemi sonlanır.Buna bağlı olarakta CONSTRUCT işlemide sona erer.

CONSTRUCT işleminin sonunda bir string değişken oluşur.Bu string arama için kullanılır.

Örnek :

FUNCTION find\_cust ()

DEFINE where\_clause CHAR (200)

...

CONSTRUCT where\_clause

ON cnum,fname,lname,company,

address1,address2,phone

FROM cnum,fname,lname,company,

address1,address2,phone

...

END FUNCTION

SELECT YAPISINI OLUŞTURMAK

SELECT yapısı LET kullanılarak oluşturulur.

SELECT için kullanılacak bir değişken mutlaka CHAR tipinde ve syntax’ı düzgün olmalıdır.

Örnek :

FUNCTION find\_cust ()

DEFINE where\_clause CHAR (200)

DEFINE sql\_stmt1 CHAR(250)

...

CONSTRUCT BY NAME where\_clause ON customer.\*

...

LET sql\_stmt1 = ‘SELECT \* FROM customer WHERE ‘,

where\_clause CLIPPED

...

END FUNCTION

PREPARE YAPISI

PREPARE yapısı çalışabilir bir RDSQL yapısı oluşturur.

Syntax

PREPARE statement-name FROM variable

Statement-name PREPARE kullanılmadan önce tanımlanmak zorunda değildir.

PREPARE değişkeninin alanı module lerin içndedir.

PREPARE yapısı SELECT te olduğu gibi INTO clause sini içermez.

Örnek :

FUNCTION find\_cust ()

DEFINE where\_clause CHAR (200)

DEFINE sql\_stmt1 CHAR(250)

...

CONSTRUCT BY NAME where\_clause ON customer.\*

LET sql\_stmt1 = ‘SELECT \* FROM customer WHERE ‘,

where\_clause CLIPPED

PREPARE ex\_stmt1 FROM sql\_stmt1

...

END FUNCTION

Program Elemanları Alanları :

Program Elemanları Alanları

Değişkenler GLOBAL Program

Local Function

Identifiers Forms Program

Windows Program

Cursors Module

Prepared Statements Module

Komutlar DEFER Program

WHENEVER Module

Örnek :

DATABASE stores

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

DEFER INTERRUPT

OPTIONS

MESSAGE line 24

CALL cust\_menu()

END MAIN

FUNCTION cust\_menu()

WHENEVER ERROR CALL cursor\_err

OPEN FORM cust\_form FROM ‘custform’

DISPLAY FORM cust\_form

MENU ‘CUSTOMER’

COMMAND ‘Find’

‘look for a specific customer’

CALL find\_cust()

COMMAND ‘Next’

‘Find next Customer’

CALL next\_cust()

COMMAND ‘Previous’

‘Find previous customer.’

CALL prev\_cust()

COMMAND ‘Exit’

‘Exit Menu’

EXIT MENU

END MENU

CLEAR SCREEN

END FUNCTION

FUNCTION find\_cust()

DEFINE where\_clause CHAR (200)

sql\_stmt1 CHAR (250)

answer CHAR (1)

DISPLAY ‘ ‘ AT 1,1

DISPLAY ‘ ‘ AT 2,1

DISPLAY ‘ ‘ AT 19,1

DISPLAY ‘ ‘ AT 20,1

DISPLAY ‘Enter the search criteria for customer’,

‘selection ,then press ESC ‘ AT 1,1

CONSTRUCT BY NAME where\_clause ON customer.\*

IF INT\_FLAG THEN

LET INT\_FLAG = FALSE

ERROR ‘Customer Query Aborted.’

RETURN

END IF

LET sql\_stmt1 = ‘SELECT \* FROM customer WHERE ‘,

where\_clause CLIPPED

DISPLAY where\_clause CLIPPED AT 19,1

DISPLAY sql\_stmt1 CLIPPED AT 20,1

PROMPT ‘Press any key to continue... ‘ FOR CHAR answer

PREPARE ex\_stmt1 FROM sql\_stmt1

DECLARE pointer1 SCROLL CURSOR FOR ex\_stmt1

OPEN pointer1

CALL first\_cust()

END FUNCTION

FUNCTION first\_cust()

FETCH FIRST pointer1 INTO p\_customer.\*

IF STATUS = NOTFOUND THEN

ERROR ‘No records found.’

ELSE

CALL display\_cust()

END IF

END FUNCTION

FUNCTION next\_cust()

FETCH NEXT pointer1 INTO p\_customer.\*

IF STATUS = NOTFOUND THEN

ERROR ‘You are at the end of the list.’

ELSE

CALL display\_cust()

END IF

END FUNCTION

FUNCTION prev\_cust()

FETCH PRIOR pointer1 INTO p\_customer.\*

IF STATUS = NOTFOUND THEN

ERROR ‘You are at the beginning of the list.’

ELSE

CALL display\_cust()

END IF

END FUNCTION

FUNCTION display\_cust()

DISPLAY ‘ ‘ AT 1,1

DISPLAY ‘ ‘ AT 2,1

DISPLAY ‘ ‘ AT 19,1

DISPLAY ‘ ‘ AT 20,1

DISPLAY BY NAME p\_customer.\*

END FUNCTION

FUNCTION cursor\_err()

DEFINE sc INTEGER

message CHAR(70)

LET sc = STATUS

CASE sc

WHEN -239

LET msg = ‘ : Insert failed.’,

‘duplicate value in unique index.’

WHEN -329

LET msg =’ : Database not found .’,

‘or no system permission.’

WHEN -387

LET msg = ‘: No connect permission’,

‘for database’

OTHERWISE

LET msg =’ ‘

END CASE

ERROR ‘Error ‘, sc USING ‘-<<<<’, msg CLIPPED

INITIALIZE p\_customer.\* TO NULL

CLEAR FORM

LET STATUS = sc

END FUNCTION

## **BÖLÜM 6******

## **DATABASE’DEN VERİ SİLME******

## **VE DATABASE’İ GÜNCELLEME******

Bu bölümde INFORMIX-4GL in özelliği olan çok mödüllü programların derlenmesini ve link edilmesini biraz hatırlamalıyız.

DERLEMENİN VE LINK ETMENİN KOMUT SATIRINDAN YAPILMASI

Aşağıdaki komut iki modülü link edip birlikte çalışan customer.4ge isimli bir program yapar.

c4gl module1.4gl module2.4gl -o customer.4ge

DERLEMENİN VE LINK ETMENİN INFORMIX-4GL EDİTÖRÜNDEN YAPILMASI

Bunun için komut satırından i4gl yazılır ve INFORMIX-4GL editörüne girilir.Burdan sonra karşımıza çıkacak New yada Modify seçeneklerinden ya programda kullanacağımız yeni bir dosya oluşturabiliriz.Ya da kullandığımız bir dosyayı değiştirebiliriz.Bu dosyalar bir programa bağlı olduklarından program derlendiği zaman hepsi derlenirler.Çoklu dosya kullanan bir programda dosyalar

syspgm4gl Form adlı dosyada tutulur.

Program İsmi

\[customer \]

4GL source u 4GL path’i

\[module1 \] \[ \]

\[module2 \] \[ \]

\[ \] \[ \]

\[ \] \[ \]

Diğer source lar ext source path’i

\[ \] \[ \] \[ \]

\[ \] \[ \] \[ \]

\[ \] \[ \] \[ \]

Kütüphaneler derleme seçenekleri

\[ \] \[ \]

\[ \] \[ \]

DELETE YAPISI

Bu komut verilen tablodan where ile yazılmış koşulu sağlayan kayıdı siler.

Syntax

DELETE FROM table-name

WHERE condition

Örnek

DELETE FROM customer

WHERE cnum = p\_customer.cnum

UPDATE YAPISI

WHERE koşulunda yazılan kayıdı SET koşulunda verilen değerle değiştirip UPDATE satırında verilen tabloyu günceller.

Syntax

UPDATE table-name

SET column-name = expr

WHERE condition

UPDATE table-name

SET (column-list) = (expr-list)

WHERE condition

UPDATE table-name

SET table-name.\* = (expr-list)

WHERE condition

Örnek :

UPDATE customer

SET customer.\* = (p\_customer.\*)

WHERE cnum = p\_customer.cnum

INPUT WITHOUT DEFAULTS YAPISI

INPUT yapısı ekrandaki bilgileri gruplandırarak program değişkenlerine atıyordu. WITHOUT DEFAULTS durumu ise değerleri update etmek için kullanılır.

Örnek :

INPUT BY NAME p\_customer.\* WITHOUT DEFAULTS

INPUT ‘a gelene kadar en son değer kalıyor ve kullanıcı değiştirebiliyor.

WITHOUT DEFAULTS INPUT’a ne gibi bir etki yapar:

cust\_form

DATABASE stores

SCREEN

{

First Name : \[a \]

Last Name : \[b \]

State : \[c \]

}

END

TABLES

customer

ATTRIBUTES

a = fname :

b = lname :

c = state.DEFAULT = ‘CA’ :

END

INPUT BY NAME p\_customer.\*

p\_customer

fname

lname

state CA

INPUT BY NAME p\_customer.\* WITHOUT DEFAULTS

p\_customer

fname George

lname Watson

state WA

Örnek :

Beşinci bölümde yazdığımız Örnek arama işlemi yapıyordu.Şimdi aşağıdaki örnekte arama ve silme işlemini ve arama güncelleme işlemini birleştireceğiz.Bunun için del\_stock ve update\_stock fonksiyonlarını ekleyeceğiz.

Customer

Dosya :module1.4gl

DATABASE stores

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

DEFER INTERRUPT

OPTIONS

MESSAGE LINE 24

CALL cust\_menu()

END MAIN

Dosya : Module2.4gl

GLOBALS

‘module1.4gl’

FUNCTION cust\_menu()

WHENEVER ERROR CALL cursor\_err

OPEN FORM cust\_form FROM ‘custform’

DISPLAY FORM cust\_form

CALL reset()

MENU ‘CUSTOMER’

COMMAND ‘Add’

‘Add one new customer.’

CALL add\_cust()

COMMAND ‘Find’

‘look for a specific customer’

CALL build\_select()

NEXT OPTION ‘Next’

COMMAND ‘Next’

‘Find next Customer’

CALL next\_cust()

COMMAND ‘Update’

‘Modify existing customer information’

CALL update\_cust()

NEXT OPTION ‘Find’

COMMAND ‘Delete’

‘Delete an existing customer information’

CALL delete\_cust()

NEXT OPTION ‘Find’

COMMAND ‘Exit’

‘Exit Menu’

EXIT MENU

END MENU

CLEAR SCREEN

END FUNCTION

FUNCTION reset()

LET INT\_FLAG = FALSE

INITIALIZE p\_customer.\* TO NULL

CLEAR FORM

END FUNCTION

FUNCTION add\_cust()

DISPLAY ‘ ‘ AT 1,1

DISPLAY ‘ ‘ AT 2,1

DISPLAY ‘Press ESC to enter data.CTRL -Z to clear’

AT 1,1

DISPLAY ‘Press DEL to abort.CTRL-I for instruction’

AT 2,1

CALL reset()

INPUT BY NAME p\_customer.fname THRU p\_customer.cnum

ON KEY (CONTROL-Z)

CALL reset()

NEXT FIELD fname

END INPUT

IF INT\_FLAG = FALSE THEN

LET p\_customer.cnum = 0

INSERT INTO customer VALUES (p\_customer.\*)

LET p\_customer.cnum = SQLCA.SQLERRD\[2\]

DISPLAY BY NAME p\_customer.cnum

MESSAGE ‘The customer has been added to the database’

ELSE

ERROR ‘Data entry aborted.’

CALL reset()

END IF

END FUNCTION

FUNCTION build\_select()

DEFINE where\_clause CHAR (200)

sql\_stmt1 CHAR (250)

DISPLAY ‘ ‘ AT 1,1

DISPLAY ‘ ‘ AT 2,1

DISPLAY ‘Enter the search criteria for customer ‘,

‘selection then Press ESC ‘ AT 1,1

CONSTRUCT BY NAME where\_clause ON customer.\*

IF INT\_FLAG THEN

ERROR ‘Customer query aborted.’

CALL reset()

RETURN

END IF

LET sql\_stmt1 = ‘SELECT \* FROM customer WHERE ‘,

where\_clause CLIPPED

PREPARE ex\_stmt1 FROM sql\_stmt1

DECLARE pointer1 CURSOR FOR ex\_stmt1

OPEN pointer1

CALL get\_cust()

END FUNCTION

FUNCTION get\_cust()

FETCH pointer1 INTO p\_customer.\*

IF STATUS = NOTFOUND THEN

ERROR ‘No records found.’

ELSE

CALL display\_cust()

END IF

END FUNCTION

FUNCTION next\_cust()

FETCH pointer1 INTO p\_customer.\*

IF STATUS = NOTFOUND THEN

ERROR ‘You are at the end of the file.’

ELSE

CALL display\_cust()

END IF

END FUNCTION

FUNCTION display\_cust()

DISPLAY ‘ ‘ AT 1,1

DISPLAY ‘ ‘ AT 2,1

IF INT\_FLAG = TRUE THEN

ERROR ‘Query Aborted’

CALL reset()

ELSE

CALL display\_cust()

END IF

DISPLAY BY NAME p\_customer.\*

END FUNCTION

FUNCTION delete\_cust()

DEFINE p\_count INTEGER

DEFINE answer CHAR (3)

IF p\_customer.cnum IS NULL THEN

ERROR ‘No record selected.’

RETURN

END IF

DISPLAY ‘ ‘ AT 1,1

DISPLAY ‘ ‘ AT 2,1

LET p\_count = 0

SELECT count (\*) INTO p\_count

FROM orders

WHERE orders.cnum = p\_customer.cnum

CASE

WHEN p\_count > 0

ERROR ‘This customer has placed’,p\_count USING ‘<<’,

‘order(s) and cannot be deleted.’

RETURN

OTHERWISE

PROMPT ‘Are you sure you want to delete’,

’this customer? (y/n) ‘ FOR answer

END CASE

IF answer MATCHES ‘\[yY\]\*’ THEN

DELETE FROM customer

WHERE cnum = p\_customer.cnum

MESSAGE ‘The information for customer’,

p\_customer.fname CLIPPED, ‘ ‘,

p\_customer.lname CLIPPED,

‘Has been deleted.’

CALL reset()

ELSE

ERROR ‘This record will not be deleted’

END IF

END FUNCTION

FUNCTION cursor\_err()

IF STATUS = -400 THEN

ERROR ‘There are no rows in the current list’,

‘see error number’,STATUS USING ‘-###’

ELSE

ERROR STATUS USING ‘-###’

END IF

CALL reset()

END FUNCTION

## **BÖLÜM 7**

## **ARRAY’LER******

ARRAY Nedir?

Bir array tekrarlanan alanları druplandırır.

Array sayesinde database’e aynı anda birden fazla veri eklenmesi mümkündür.

Her tekrarlanan satır bir elemana karşılık gelir.

Diagram

Stock

Number Code Description Price

\[7 \] \[HRQ \] \[basketball \] \[$35.00\]

\[8 \] \[ANZ \] \[volleyball \] \[$84.00\]

\[2 \] \[HRO \] \[baseball \] \[$12.60\]

\[1 \] \[HRO \] \[baseball glove \] \[$35.00\]

\[3 \] \[HSK \] \[baseball bat \] \[$24.00\]

Yukarıdaki diagramda 5 tane array’a ait eleman vardır.

FORM içeren bir ARRAY oluşturma

Örnek : stk\_arr.per

DATABASE stores

SCREEN

{

STOCK FORM

Stock

Number Code Description Price

\[f000 \] \[a0 \] \[f001 \] \[f002 \]

\[f000 \] \[a0 \] \[f001 \] \[f002 \]

\[f000 \] \[a0 \] \[f001 \] \[f002 \]

\[f000 \] \[a0 \] \[f001 \] \[f002 \]

\[f000 \] \[a0 \] \[f001 \] \[f002 \]

}

END

TABLES

stock

ATTRIBUTES

f000 = stock.stockno;

a0 = stock.mfcode,UPSHIFT;

f001 = stock.description,DOWNSHIFT;

f002 = stock.unitprice;

INSTRUCTIONS

SCREEN RECORD s\_stock \[5\]

(stockno,

mfcode,

description,

unitprice)

END

SCREEN RECORD YAPISI

SCREEN RECORD form üzerindeki bir alana referans olmanın bir yoludur.

Bir form içindeki her table default olarak SCREEN RECORD yapısına sahiptir.Programcının bu yapıyı ayrıca tanımlamasına gerek yoktur.

SCREEN RECORD form yapısı oluşturulurken instructions kısmında tanımlanır.

SCREEN RECORD bir array’in formda ship olduğu eleman sayısını tanımlamaya yarar.

SCREEN RECORD’a Örnekler :

SCREEN RECORD cust\_id (cnum,fname,lname,company)

SCREEN RECORD cust\_id (cnum THRU company )

SCREEN RECORD s\_items \[4\] (stock.stockno,

stock.mfcode,

manufacturer.mfname,

stock.description,

stock.unitprice)

SCREEN RECORD s\_stock \[5\] (stockno,

mfcode,

description,

unitprice)

ARRAY KULLANARAK BİR INFORMIX-4GL PROGRAMI YAZMAK

Screen Array Program Array

s\_stock1 p\_stock1

s\_stock2 INPUT ARRAY p\_stock2 INSERT

s\_stock3 p\_stock3 database

s\_stock4 DISPLAY ARRAY p\_stock4 SELECT

s\_stock5 p\_stock5

p\_stock6

p\_stock7

p\_stock8

p\_stock9

p\_stock10

stk\_arr.per Örneğindeki SCREEN RECORD tanımlaması

Bu yapı ekran içindir.

SCREEN RECORD s\_stock \[10\] (stockno,

mfcode,

description,

unitprice)

global.4gl için Record Array yapısı

Bu yapı veri tabanı içindir.

DEFINE p\_stock ARRAY\[20\] of RECORD

stockno LIKE stock.stockno,

mfcode LIKE stock.mfcode,

description LIKE stock.description,

unitprice LIKE stock.unitprice

END RECORD

Diagram

Stock

Number Code Description Price

\[4 \] \[HSK \] \[football \] \[$96.00\]

\[7 \] \[HRO \] \[basketball \] \[$35.00\]

\[8 \] \[ANZ \] \[volleyball \] \[$84.00\]

\[2 \] \[HRO \] \[baseball \] \[$12.60\]

\[1 \] \[HRO \] \[baseball glove \] \[$35.00\]

\[3 \] \[HSK \] \[baseball bat \] \[$24.00\]

\[4 \] \[HRO \] \[football \] \[$48.00\]

\[ \] \[ \] \[ \] \[ \]

\[ \] \[ \] \[ \] \[ \]

\[ \] \[ \] \[ \] \[ \]

Program array’indeki eleman sayısı ile SCREEN RECORD taki eleman sayısı aynı olmak zorunda değildir.

INPUT ARRAY YAPISI

INPUT ARRAY yapısı screen arraylerini girdiğiniz verileri program array’i şeklinde saklar.

Syntax

INPUT ARRAY program-array FROM screen-array

Örnek :

INPUT ARRAY p\_stock FROM s\_stock.\*

Hareket tuşları bir array çevresinde dolaşmak için kullanılır.

ESCAPE VE DEL tuşları INPUT ARRAY’i kesmek için kullanılır.

Fonksiyon tuşları array’a edit etmek için kullanılır.

Eğer array aşılırsa otomatik olarak beep sesi verilir.

OPTIONS

ESCAPE tuşu INPUT ARRAY den çıkar.

F1 tuşu array’e boş bir satır ekler.

F2 tuşu arrayden bir satır siler.

F3 tuşu array penceresinden sonraki sayfaya geçer.

F4 tuşu ise bir önceki sayfaya gider.

Bu tuşlar default tuşlardır.İstenildiği takdirde OPTIONS bölümünden değiştirilebilir.

Örnek

OPTIONS

ACCEPT KEY F1,

INSERT KEY CONTROL-I,

DELETE KEY CONTROL-E,

NEXT KEY CONTROL-N,

PREVIOUS KEY CONTROL-P

ARRAY FONKSİYONLARI

SCR\_LINE () Bu bize ekranda kaçıncı satırda olduğumuzun değerini geri yollar.

ARR\_CURR() Bu bize program dizisinin kaçıncı satırında olduğumuzu geri yollar.

ARR\_COUNT() Program dizisinde kaç kayıt olduğunun değerini verir.

SET\_COUNT(expr) Programdan kaç kayıt okuduğumuzun değerini geri gönderir.Bunu DISPLAY ARRAY yapısından önce kullanmalıyız.Bütün kayıtların okunduğunu anlamak için bu değeri ARR\_COUNT() ile karşılaştırabiliriz.

Program array

p\_stock

stockno mfcode description unitprice

4 HSK football $96.00

7 HRO basketball $35.00

+ 8 ANZ volleyball $84.00

2 HRO baseball $12.60

1 HRO baseball glove $35.00

3 HSK baseball bat $24.00

4 HRO football $48.00

screen array

s\_stock

stockno mfcode description unitprice

7 HRO basketball $35.00

+ 8 ANZ volleyball $84.00

2 HRO baseball $12.60

1 HRO baseball glove $35.00

3 HSK baseball bat $24.00

Burda ANZ mfcode una ilişkin değerlere bakalım

s = SCR\_LINE() = 2

p = ARR\_CURR () = 3

c = ARR\_COUNT() = 7

ARRAY Değerlerini Database Tablolarına Ekleme

FOR yapısı sayesinde sıralı bir şekilde değişkenleri database tablolarına atarız.

FOR un Syntax’i

FOR integer-var = integer-var TO integer-expr

Örnek

FUNCTION add\_cust()

DEFINE i smallint

...

FOR i = 1 TO ARR\_COUNT ()

INSERT INTO customer

VALUES (p\_customer \[i\].\*)

END FOR

INPUT ARRAY IN DESTEKLEDİĞİ SEÇENEKLER

BEFORE ROW Cursor yeni bir satıra gelmiş ve önceki data da girilmişse kullanılır.

BEFORE INSERT Yeni bir satır açıp F1 tuşuna basıldığında yeni bir satır açmadan önceki yapılacak işlemleri yapmamızı sağlar.

BEFORE DELETE Bir satır silmeden önce yapılacak işlemleri yapmamızı sağlar.

BEFORE FIELD Bazı özel durumlarda cursor field-listesine bir field girerken kullanılır.

ON KEY Bu bazı işlemleri özel tuşlarla yapmamızı sağlar.

AFTER FIELD Cursor’un field-listesindeki bir alanı terk ettiği zaman bazı işlemler yapmak için kullanılır.

AFTER INSERT Tamamlanmış bir array’in içine yeni bir satır eklemek için kullanılır.

AFTER DELETE Bir array’den bir eleman silinince yapılacak işlemler için kullanılır.

AFTER ROW Cursor’ın satırdan ayrılması sırasında gerek duyulur.

AFTER INPUT ESCAPE tuşuna basıldıktan sonra programcının INPUT ARRAY yapısının doğruluğunu kontrol etmesi gerekir.

BİR EXPRESSION İÇİNDE FONKSİYON ÇAĞIRMA

Biz bir expression içinde bize değer gönderen bir fonksiyonu kullanabiliriz.

Örnek :

IF no\_manufact() THEN

...

END IF

Bu şuna eşittir:

DEFINE a SMALLINT

CALL no\_manufact()

RETURNING a

IF a=TRUE THEN

...

END IF

Tabii fonksiyonun göndereceği değere göre expression içinde kullanmalıyız.Aksi takdirde hata oluşur.

no\_manufact() :

FUNCTION no\_manufact()

IF ...

RETURN TRUE

ELSE

RETURN FALSE

END IF

Aşağıdaki örnekte kullanıcı p\_stock.mfcode a değer girecek no\_manufact() fonksiyonu ise mfcode u database içerisinde arayacak.Eğer daha önceden bu değer varsa fonksiyon TRUE değerini gönderir.

FUNCTION add\_stock()

...

INPUT ARRAY p\_stock FROM s\_stock.\*

AFTER FIELD mfcode

IF no\_manufact() THEN

NEXT FIELD mfcode

END IF

END INPUT

...

END FUNCTION

FUNCTION no\_manufact()

DEFINE p INTEGER

LET p= ARR\_CURR()

SELECT mfcode

FROM manufacturer

WHERE mfcode = p\_stock\[p\].mfcode

IF STATUS = NOTFOUND THEN

ERROR ‘This is not a valid mfcode.’

RETURN TRUE

ELSE

RETURN FALSE

END IF

END FUNCTION

ÖRNEK : stk\_arr2.4gl

DATABASE stores

GLOBALS

DEFINE p\_stock ARRAY \[20\] OF RCORD LIKE stock.\*

END GLOBALS

MAIN

OPTIONS

INSERT KEY CONTROL-I,

DELETE KEY CONTROL-E,

NEXT KEY CONTROL-N,

PREVIOUS KEY CONTROL-P

OPEN FORM stockform FROM ‘stk\_arr’

DISPLAY FORM stockform

MENU ‘STOCK FORM’

COMMAND ‘Add’

‘Add stock items.’

CALL add\_stock()

COMMAND ‘Exit’

‘Exit program.’

EXIT MENU

END MENU

CLEAR SCREEN

END MAIN

FUNCTION add\_stock()

DEFINE i SMALLINT

DISPLAY ‘ESC add CTRL-N next page CTRL-E erase row ‘

AT 1,1

DISPLAY ‘DEL abort CTRL-P previous page CTRL-I insert row’

AT 2,1

INPUT ARRAY p\_stock FROM s\_stock.\*

AFTER FIELD mfcode

IF no\_manufact() THEN

NEXT FIELD mfcode

END IF

END INPUT

FOR i=1 TO ARR\_COUNT()

INSERT INTO stock

VALUES (p\_stock\[i\].\*)

END FOR

CLEAR FORM

END FUNCTION

FUNCTION no\_manufact()

DEFINE p INTEGER

LET p= ARR\_CURR()

SELECT mfcode

FROM manufacturer

WHERE mfcode = p\_stock\[p\].mfcode

IF STATUS = NOTFOUND THEN

ERROR ‘This is not a valid mfcode.’

RETURN TRUE

ELSE

RETURN FALSE

END IF

DISPLAY ARRAY YAPISI

Bir ARRAY ‘i display etmek için şunları yapmalısınız :

Database den veri seçmek

Seçilen veriyi ekranda göstermek.

INFORMIX-4GL

Program

p\_stock

Screen DISPLAY stockno mfcode description unitprice SELECT database

Örnek : Bu örnek stock tablosundan değerleri seçiyor ve onları p\_stock adlı arrayde saklıyor.Biz array in boyutunu test etmeliyiz.

GLOBALS

DEFINE p\_stock ARRAY \[10\] OF RECORD

LIKE stock.\*

END GLOBALS

MAIN

...

END MAIN

FUNCTION stkblock()

DEFINE counter, i INTEGER

DECLARE pointer CURSOR FOR

SELECT \* FROM stock

ORDER BY description

LET counter = 1

OPEN pointer

WHILE STATUS != 100

WHILE COUNTER <= 10

FETCH pointer INTO p\_stock\[counter\].\*

LET counter = counter+1

END WHILE

...

END FUNCTION

PROGRAM ARRAYİNDEKİ DEĞERLERİN SCREEN ARRAYA DISPLAY EDİLMESİ

Syntax

DISPLAY ARRAY program-array TO screen-array.\*

\[ATTRIBUTE (attribute-list)\]

DISPLAY ARRAY program-array TO screen-array.\*

\[ON KEY (key-list)

statement

| EXIT DISPLAY \]

END DISPLAY

Burda SET\_COUNT(expr) fonksiyonunu çağırmalısınız.

ESCAPE tuşu veya OPTION kısmı içerisinde belirtilen ACCEPT KEY DISPLAY ARRAY den çıkar.

Ok tuşları ve OPTIONS içerisinde belirtilen NEXT ve PREVIOUS tuşları hareket etmek için kullanılır.

Aşağıdaki örnek program array i olan p\_stock tan screen array i olan s\_stock a değer display eder.

Örnek :

GLOBALS

DEFINE p\_stock ARRAY\[10\] OF RECORD

LIKE stock.\*

END GLOBALS

FUNCTION stkblock()

DEFINE counter,i INTEGER

LET counter = 1

OPEN pointer

WHILE STATUS != 100

WHILE counter <=10

FETCH pointer INTO p\_stock\[counter\].\*

LET counter = counter+1

END WHILE

CALL SET\_COUNT(counter-1)

DISPLAY ARRAY p\_stock TO s\_stock.\*

LET counter = 1

CLEAR FORM

FOR i =1 to ARR\_COUNT()

INITIALIZE p\_stock \[i\].\* to NULL

END FOR

...

END FUNCTION

Örnek : stk\_blok.4gl

DATABASE stores

GLOBALS

DEFINE p\_stock ARRAY \[10\] OF RECORD LIKE stock.\*

END GLOBALS

MAIN

DEFER INTERRUPT

OPEN FORM stock FROM ‘stk\_blok’

DISPLAY FORM stock

MENU ‘STOCK’

COMMAND ‘Start’

CALL stkblock()

COMMAND ‘Exit’

Exit Menu

END MENU

END MAIN

FUNCTION stkblock()

DEFINE counter,i INTEGER

DISPLAY ‘Press ESC to continue or DEL to EXIT.’ AT 1,1

DECLARE pointer CURSOR FOR

SELECT \* FROM stock

ORDER BY description

LET counter = 1

OPEN pointer

WHILE STATUS != 100

WHILE counter <=10

FETCH pointer INTO p\_stock\[counter\].\*

LET counter = counter+1

END WHILE

CALL SET\_COUNT(counter-1)

DISPLAY ARRAY p\_stock TO s\_stock.\*

LET counter = 1

CLEAR FORM

FOR i =1 to ARR\_COUNT()

INITIALIZE p\_stock \[i\].\* to NULL

END FOR

IF INT\_FLAG = TRUE THEN

LET INT\_FLAG = FALSE

EXIT WHILE

END IF

END WHILE

RETURN

END FUNCTION

Örnek : stk\_arr3.4gl

DATABASE stores

GLOBALS

DEFINE p\_stock ARRAY \[20\] OF RCORD LIKE stock.\*

DEFINE p\_manufact ARRAY \[10\] OF RECORD LIKE manufact.\*

DEFINE p\_manufact\_size SMALLINT

DEFINE p\_manufact\_cnt SMALLINT

END GLOBALS

MAIN

DEFER INTERRUPT

LET p\_manufact\_size = 10

CALL pop\_manufact()

OPTIONS

INSERT KEY CONTROL-I,

DELETE KEY CONTROL-E,

NEXT KEY CONTROL-N,

PREVIOUS KEY CONTROL-P

MESSAGE LINE 24

OPEN FORM stockform FROM ‘stk\_arr’

DISPLAY FORM stockform

MENU ‘STOCK FORM’

COMMAND ‘Add’

‘Add stock items.’

CALL add\_stock()

COMMAND ‘Exit’

‘Exit program.’

EXIT MENU

END MENU

CLEAR SCREEN

END MAIN

FUNCTION add\_stock()

DEFINE i , p , s SMALLINT

DISPLAY ‘ESC add CTRL-N next page CTRL-E erase row ‘

AT 1,1

DISPLAY ‘DEL abort CTRL-P previous page CTRL-I insert row’

AT 2,1

INPUT ARRAY p\_stock FROM s\_stock.\*

AFTER FIELD mfcode

IF no\_manufact() THEN

LET p = ARR\_CURR()

LET s = SCR\_LINE()

CALL sel\_manufact (p,s)

END IF

END INPUT

IF INT\_FLAG = TRUE THEN

LET INT\_FLAG = FALSE

ERROR ‘This entry has been aborted.’

CLEAR FORM

RETURN

END IF

WHENEVER ERROR CONTINUE

FOR i=1 TO ARR\_COUNT()

INSERT INTO stock

VALUES (p\_stock\[i\].\*)

IF STATUS = 0 THEN

MESSAGE ‘The stock item has been added’

SLEEP 3

MESSAGE ‘ ‘

ELSE

ERROR ‘Stock item’,

p\_stock\[i\].stockno USING ‘##’,

‘/’,

p\_stock\[i\].mfcode,

‘was not added to the database.’

END IF

END FOR

WHENEVER ERRRO STOP

CLEAR FORM

END FUNCTION

FUNCTION no\_manufact()

DEFINE p,s INTEGER

LET p = ARR\_CURR()

LET s = SCR\_LINE()

SELECT mfcode

FROM manufacturer

WHERE mfcode = p\_stock\[p\].mfcode

IF STATUS = NOTFOUND THEN

RETURN TRUE

ELSE

RETURN FALSE

END IF

END FUNCTION

FUNCTION pop\_manufact()

LET p\_manufact\_cnt = 1

DECLARE pointer1 CURSOR FOR

SELECT mfcode,mfname

FROM manufacturer

ORDER BY mfname

FOREACH pointer1 INTO p\_manufact \[p\_manufact\_cnt\].\*

LET p\_manufact\_cnt = p\_manufact\_cnt+1

IF p\_manufact\_cnt = (p\_manufact\_size+1)

EXIT FOREACH

END IF

END FOREACH

END FUNCTION

FUNCTION sel\_manufact (p,s)

DEFINE p2 , p, s SMALLINT

OPEN WINDOW w\_manufact AT 15,5

WITH FORM ‘manufact’

ATTRIBUTES (BORDER,MESSAGE LINE FIRST)

MESSAGE ‘Press ESC to select’

CALL SET\_COUNT (p\_maufact\_cnt-1)

DISPLAY ARRAY p\_manufact TO s\_manufact.\*

LET p2= ARR\_CURR ()

LET p\_stock\[p\].mfcode = p\_manufact\[p2\].mfcode

CLOSE WINDOW w\_manufact

DISPLAY p\_stock\[p\].mfcode TO s\_stock\[s\].mfcode

END FUNCTION

## **BÖLÜM 8**

## **RAPORLAMA******

RAPORLAMA

1.Veriler INFORMIX-4GL programı içerisinde program değişkenleri olarak gruplandırılırlar.

Database den program değişkenleri için veri seç

Seçilen veriyi ekranda göster.

2.INFORMIX-4GL rapor rutinine gruplandırılmış verileri satır satır gönderir.

3.Rapor rutini gelen veriyi belli bir formata sokar.

INFORMIX-4GL DE VERİ AKIŞI

INPUT INSERT

form 4GL DELETE

DISPLAY Program SELECT database

UPDATE

Reports

Raporlama kaybolan linki anlaşılabilir bir formatta database dışına göndermeyi destekler.

INFORMIX-SQL ACE RAPORLARI

Ace raporları INFORMIX-SQL kullanılarak yazılmıştır.Bu raporlamalar program tarafından RUN komutu ile çalıştırılırlar.

Örnek :

DATABASE stores

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

CLEAR SCREEN

CALL labels()

END MAIN

FUNCTION labels ()

DEFINE print\_option CHAR(1)

DECLARE pointer1 CURSOR FOR

SELECT \* FROM customer

START REPORT labels\_rep TO ‘labels\_rep.out’

FOREACH pointer1 INTO p\_customer.\*

OUTPUT TO REPORT labels\_rep (p\_customer.\*)

END FOREACH

FINISH REPORT labels\_rep

END FUNCTION

REPORT labels\_rep( c )

DEFINE

c RECORD LIKE customer.\*

FORMAT

EVERY ROW

END REPORT

LABEL FONKSİYONLARI

1.START REPORT yapısı raporlama işini başlatır.Bu sayfa başlarını oluşturur.TO labels\_rep.out clause u ise çıkışın hedefidir.Rapor bir program yada printer a pipe olabilir bunun için TO PIPE komutu kullanılır.TO PIPE ‘program ‘ veya TO PRINTER.

2.OUTPUT REPORT yapısı SELECT yapısı sonucunda oluşan her satırı REPORT rutinine gönderir.Bu genelde FOREACH ve WHILE döngülerinin içinde bulunur.

3.FINISH REPORT yapısı ise o anda yazılmakta olan bilgileri handle eder ve raporlama işlemini yok eder.

REPORT rutini MAIN in dışarısında olmalıdır.

RAPORLAR

Rapor ismi özel bir REPORT rutini için kullanılır.Bunu argument-list izler.

Argument-listesinin içinde basit değişkenler kullanabilirsiniz.

p\_customer , cnum , lname

Bu değişkenler geçerli değildir.

p\_customer.\*

p\_customer.fname THRU p\_customer.zip

Argument-listesi REPORT rutininin DEFINE kısmında tanımlanması gerekir.

Örnek :

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

FUNCTION labels()

...

FOREACH pointer1 INTO p\_customer.\*

OUTPUT TO REPORT labels\_rep(p\_customer.\*)

END FOREACH

...

END FUNCTION

REPORT labels\_rep( c )

DEFINE

c RECORD LIKE customer.\*

...

END REPORT

OUTPUT BÖLÜMÜ

OUTPUT raporu değişik yerlere yollamak için kullanılır.Bunların arasında printer,dosya,pipe,terminal ekranı yeralır.OUTPUT hedefi START REPORT komutu içerisinde kullanılır.

Syntax

OUTPUT

REPORT TO filename | PIPE program | prınter {screen}

REPORT TO filename | PRINTER {screen}

LEFT MARGIN x {5}

RIGHT MARGIN x {132}

TOP MARGIN x {3}

BOTTOM MARGIN x {3}

PAGE LENGTH x {66}

END

Örnek :

OUTPUT

LEFT MARGIN 0

PAGE LENGTH 24

ORDER BY BÖLÜMÜ

Çıktıyı sıralamak için kullanılır.

Örnek :

ORDER BY lname,fname

FORMAT BÖLÜMÜ

Raporlamanın FORMAT kısmında basit komutlar vardır:

Sayfa başlıkları yazar.

Sayfa numaraları yazar.

Verileri gruplandırır.

Gruplanmış verilerde işlemler yapar.(MIN,MAX,TOTAL,AVG,PERCENT,COUNT)

Kolon başlıklarına göre verileri sıraya dizer.

Numaraları ve tarihleri düzenler.

Sayısal hesaplamalar yapar.

KONTROL BLOKLARI

EVERY ROW = Her gelen kaydın formatlanması yapılır.

PAGE HEADER =Başlık için

PAGE TRAILER =Sayfa sonunda herhangi bir işlem yapmaya yarar.

FIRST PAGE HEADER

ON EVERY ROW

ON LAST ROW

BEFORE GROUP OF variable

AFTER GROUP OF variable

FORMAT KEYWORDS

NEED expr LINES O anki sayfada yeterince satır yoksa kullanılır.

PAUSE \[string\] Terminali durdurur ve mesaj verir.Bu işlem enter tuşuna basıldıktan sonra biter.

PRINT expr-list string kolon yada değişkenleri yazdırmak için kullanılır.

PRINT FILE filename Özel bir file ın içindekileri yazdırma işlemini gerçekleştirir.

SKIP expr LINES Raporda satır atlamak için kullanılır.

SKIP TO TOP OF PAGE Yeni bir sayfaya başlarken kullanılır.Bir counter yazılan satır sayısını tutar ve bu fonksiyon sayesinde sayfa uzunluğundan satır sayısı çıkartılır.

ASCII expr Özel ASCII karakterlerini yazdırmak için kullanılır.

Char-expr CLIPPED Değişkenin veya stringin sağındaki boşlukları atar.

COLUMN expr Print edilmiş kolon numarasını verir.

Expr SPACES Verilen değer kadar boşluk yazar.

Expr USING Nümerik değişkenleri tarih ve saat değişkenlerini düzenlememizi sağlar.

Sembol Print

\# boşluk yazar

& yazılmışsa 0 değeri verir.

$ dolar işareti yazar.

< Numaraları sola dayalı yazar.

TARİH FONKSİYONLARI

TODAY Sistem tarihini verir.

DATE(date-expr)

DAY(date-expr)

MONTH(date-expr)

YEAR(date-expr)

MDY(date-expr)

WEEKDAY(date-expr)

AGGREGATES

Aggregate \[WHERE expression\]

COUNT

PERCENT

AVERAGE expression

MIN expression

MAX expression

Syntax

GROUP aggregate \[WHERE expression\]

Örnek :

DATABASE stores

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

CLEAR SCREEN

CALL labels()

END MAIN

FUNCTION labels()

DEFINE print\_option CHAR (1)

LET print\_option = ‘ ‘

DECLARE pointer1 CURSOR FOR

SELECT \* from customer

WHILE print\_option NOT MATCHES ‘\[sSfF\]’

PROMPT ‘Do you want the labels to go to a ‘,

‘Screen or file (s-f)? ‘ FOR CHAR print\_option

CASE

WHEN print\_option MATCHES ‘\[sS\]’

START REPORT labels\_rep

WHEN print\_option MATCHES ‘\[Ff\]’

START REPORT labels\_rep TO ‘labels\_rep.out’

OTHERWISE

ERROR print\_option, ‘is not valid character’

END CASE

END WHILE

MESSAGE ‘PreparingLabels please wait...’

FOREACH pointer1 INTO p\_customer.\*

OUTPUT TO REPORT labels\_rep(p\_customer.\*)

END FOREACH

FINISH REPORT labels\_rep

END FUNCTION

REPORT labels\_rep ( c )

DEFINE

c RECORD LIKE customer.\*

OUTPUT

TOP MARGIN 0

BOTTOM MARGIN 0

PAGE LENGTH 7

FORMAT

ON EVERY ROW

PRINT c.fname CLIPPED, ‘ ‘,c.lname CLIPPED

PRINT c.company

PRINT c.address1

IF c.address2 <> ‘ ‘ THEN

PRINT c.address2

END IF

PRINT c.city CLIPPED,’ ‘,c.state,’ ‘,c.zip

SKIP TO TOP OF PAGE

END REPORT

Örnek : Labels2.4gl

DATABASE stores

GLOBALS

DEFINE p\_customer RECORD LIKE customer.\*

END GLOBALS

MAIN

DEFER INTERRUPT

OPTIONS

MESSAGE LINE 24

OPEN FORM f\_cust FROM ‘custform’

DISPLAY FORM f\_cust

MENU ‘REPORTS’

COMMAND ‘Labels’

‘Print labels for customers.’

CALL labels()

COMMAND ‘Exit’

‘Exit menu.’

CLEAR SCREEN

EXIT MENU

END MENU

END MAIN

FUNCTION find\_cust()

DISPLAY ‘ ‘ AT 1,1

DISPLAY ‘ ‘ AT 2,1

DISPLAY ‘Enter the search criteria for customer’,’selection then press ESC ‘

AT 1,1

CALL build\_select()

END FUNCTION

FUNCTION build\_select ()

DEFINE where-clause CHAR(200)

sql-stmt1 CHAR(250)

CONSTRUCT BY NAME where\_clause ON customer.\*

IF INT\_FLAG THEN

LET INT\_FLAG = FALSE

ERROR ‘Customer query aborted.’

RETURN

END IF

LET sql\_stmt1 = ‘SELECT \* FROM customer WHERE ‘,

where\_clause CLIPPED

PREPARE ex\_stmt1 FROM sql\_stmt1

DECLARE pointer1 SCROLL CURSOR FOR ex\_stmt1

END FUNCTION

FUNCTION labels()

DEFINE print\_option CHAR (1)

LET print\_option = NULL

CALL find\_cust()

WHILE print\_option NOT MATCHES ‘\[sSfF\]’

PROMPT ‘Do you want the invoice to go to a ‘,

‘Screen or file (s-f)? ‘ FOR CHAR print\_option

CASE

WHEN print\_option MATCHES ‘\[sS\]’

START REPORT labels\_rep

WHEN print\_option MATCHES ‘\[Ff\]’

START REPORT labels\_rep TO ‘labels\_rep.out’

OTHERWISE

ERROR print\_option, ‘is not valid character’

END CASE

END WHILE

CLEAR SCREEN

MESSAGE ‘PreparingLabels please wait...’

FOREACH pointer1 INTO p\_customer.\*

OUTPUT TO REPORT labels\_rep(p\_customer.\*)

END FOREACH

FINISH REPORT labels\_rep

END FUNCTION

REPORT labels\_rep ( c )

DEFINE

c RECORD LIKE customer.\*

FORMAT

ON EVERY ROW

PRINT c.fname CLIPPED, ‘ ‘,c.lname CLIPPED

PRINT c.company

PRINT c.address1

IF c.address2 <> ‘ ‘ THEN

PRINT c.address2

END IF

PRINT c.city CLIPPED,’ ‘,c.state,’ ‘,c.zip

SKIP 2 LINES

END REPORT

**INFORMIX-4GL**

PAGE\\# "'Sayfa: '#'
'" |

---
*Kaynak: `INFORMIX - 4GL PROGRAMLARININ DERLENMESİ/INFORMIX - 4GL PROGRAMLARININ DERLENMESİ.doc` — OĞUZHAN YILMAZ — 2004*
