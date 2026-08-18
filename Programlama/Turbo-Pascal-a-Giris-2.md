# Turbo Pascal ' a Giriş 2

## **İÇİNDEKİLER**

**TURBO PASCAL’A GİRİŞ**

**EDİTÖR **...................................................................................................................8

Ana Menü ................................................................................................................ 8

Alt menüler ............................................................................................................. 8

Programın Yazımı (Edit) .................................. ........... .................................................. 11

Programın Saklanması (Save) ................................................ ....................................... 12

Programın Derlenmesi (Compile) .......................................................... ........................ 12

Programın Çalıştırılması (Run) ................................................................... ................... 12

EXE Uzantılı Dosya Oluşturma ....................................................................... .................13

PASCAL KAREKTER SETİ .............................................................................................. 13

Turbo Pascal ‘da Kullanılan Komut ve Kelimeler ......................................................... 14

PASCAL PROGRAMININ GENEL YAPISI ...................................................................... 16

Program Başlığı ..................................................................................................... 17

Tanımlama Bloğu .................................................................................................. 17

Uygulama Bloğu .................................................................................................... 20

**SABİTLER DEĞİŞKENLER VE OPERATÖRLER** .......................................................... 23

SABİTLER ....................................................................................................................... 23

Sabit (Constant) Tanımlama ....................................................................................... 23

**DEĞİŞKENLER ** ............................................................................................................... 23

Değiken (Variable) Tanımlama .............................................................................. 24

Değişken İsimleri ................................................................................................... 24

Değişken ve Sabit İsmi Seçilirken Dikkat Edilmesi Gereken Kurallar............................... 24

Değişken Tipleri ..................................................................................................... 25

Standart Değişken Tipleri ................................................................................................. 25

Tamsayı (Integer) Değişken Tipleri ................. ............. .................................................. 25

Gerçek (Real) Değişken Tipi ............................................................................................ 25

Karakter (character) Değişken Tipi .................................................................................. 25

String Değişken Tipi ......................................................................................................... 25

Boolean Değişken Tipi .................................................................................................... 26

Programcının Tanımladığı Değişken Tipleri ......................................................... 26

Tip Tanımlama ................................................................................................................. 26

Dizi Tipi Değişkenler .............................................................................................. 26

Dizi Tipi Değişkenlerin Tanımlanması .............................................................................. 26

Küme Tipi değişkenler ......................................................................................... 27

In operatörü ...................................................................................... ............................... 27

Küme Tipi Değişkenlerin Tanımlanması ................................................ ......................... 27

Küme Tipi Değişkenlere Değer Atama ............................................... ............................ 27

Küme İşlemleri ...................................................................................... .......................... 27

Sıralı Tip Değişkenler ............................................................................ ............... 27

Sıralı Tip Değişkenlerin Tanımlanması ................................................ ........... ............... 27

Sınırlı Tip Değişkenler............................................................................................. 27

Sınırlı Tip Değişkenlerin tanımlanması.................................................. ........................... 27

Sıralı Verilerin Yazdırılması.................................................................... .......................... 27

Sıralı Tip Veri Kullanmak Gerçekten Gerekli midir? ................................. ........................ 27

Record değişken Tipi............................................................................................... 28

Record Tipi Değişkenlerin Tanımlanması................................................. ........................ 28

Record Tipi Değişken Tanımlanması................................................................................. 28

Operatörler ............................................................................................................. 28

Aritmetik işlem Operatörleri................................................................................................ 28

İlişki Operatörleri................................................................................................................ 28

Mantıksal Operatörler........................................................................................................ 28

**TEMEL GİRİŞ / ÇIKIŞ KOMUTLARI**

WRITELN.......................................................................... .................................... 28

WRITE.................................................................................................................... 28

READLN................................................................................................................. 29

READ.......................................................................... .......................................... 29

FORMATLI ÇIKIŞ................................................................................................... 29

Integer Sayıların Formatlanması....................................................................................... 29

Real Sayıların Formatlanması.......................................................................................... 29

Char Tipi Verilerin Formatlanması.................................................................................... 29

String tipi Verileri Formatlamak......................................................................................... 30

Boolean Tipi Verilerin Formatlanması............................................................................... 30

VERİ KONTROLÜ (COMPILER BİLDİRİLERİ) ..................................................... 30

Compiler Bildirisi Tanımlamak.......................................................................................... 30

FORWARD bildirisi........................................................................................................... 30

R bildirisi.......................................................................... ................................................ 30

I bildirisi.......................................................................... .................................................. 30

I (INCLUDE DOSYA) Bildirisi............................................................................................ 30

**PROGRAM AKIŞININ KONTROLÜ**

DALLANMA DEYİMLERİ........................................................................................ 31

IF -THEN deyimi.............................................................................................................. 31

IF -THEN \_ELSE deyimi................................................................................................... 31

CASE -OF deyimi.............................................................................................................. 32

DÖNGÜLER........................................................................................................... ** **32

GOTO deyimi.......................................................................... ..................................... 32

FOR-DO deyimi............................................................................................................ 33

WHILE-DO deyimi.............................................................................................................. 34

REPEAT-UNTIL deyimi................................................................................................ 34

**İNDİSLİ DEĞİŞKENLER**

**İNDİSLİ DEĞİŞKENLERİN **TANIMI................................................................................................................... 36

TEK BOYUTLU DEĞİŞKENLER...................................................................................... 36

Sıralama (sort) işlemi ................................................................................................... 37

iKi BOYUTLU DEĞİŞKENLER..................................................................................... 37

**STANDART PROSEDÜR VE FONKSİYONLAR**

MKDIR prosedürü.................................................................................................. 38

PARAMCOUNT fonksiyonu.................................................................................... 38

PARAMSTR fonksiyonu......................................................................................... 39

GETDIR prosedürü; ............................................................................................... 39

CHDIR prosedürü................................................................................................... 39

IORESULT fonksiyonu........................................................................................... 40

RMDIR prosedürü.................................................................................................. 40

GETDATE prosedürü............................................................................................. 41

GETTIME prosedürü.............................................................................................. 41

SETDATE prosedürü.............................................................................................. 42

SETTIME prosedürü.............................................................................................. 42

CHR fonksiyonu..................................................................................................... 42

ORD fonksiyonu..................................................................................................... 43

PRED fonksiyonu................................................................................................... 43

SUCC fonksiyonu................................................................................................... 43

TEXTBACKGROUND prosedürü........................................................................... 43

TEXTCOLOR prosedürü......................................................................................... 43

LOWVIDEO prosedürü........................................................................................... 44

NORMVIDEO prosedürü........................................................................................ 44

READKEY fonksiyonu............................................................................................ 44

KEYPRESSED fonksiyonu...................................................................................... 44

GOTOXY prosedürü................................................................................................ 45

WINDOW prosedürü............................................................................................... 45

COPY fonksiyonu................................................................................................... 45

CONCAT fonksiyonu.............................................................................................. 45

LENGTH fonksiyonu............................................................................................... 46

POS fonksiyonu....................................................................................................... 46

DELETE prosedürü................................................................................................ 46

INSERT presedürü................................................................................................ 47

STR prosedürü....................................................................................................... 47

VAL prosedürü...................................................................................................... 47

EXIT prosedürü...................................................................................................... 47

HALT prosedürü...................................................................................................... 47

DELAY prosedürü.................................................................................................. 47

SOUND prosedürü................................................................................................. 48

NOSOUND prosedürü............................................................................................ 48

CLREOL prosedürü................................................................................................ 48

DELLINE prosedürü............................................................................................... 48

INSLINE prosedürü................................................................................................ 48

WHEREX fonksiyonu............................................................................................ 48

WHEREY fonksiyonu............................................................................................ 48

RANDOM fonksiyonu............................................................................................. 48

SIZE OF fonksiyonu............................................................................................... 48

UPCASE fonksiyonu.............................................................................................. 48

ABS fonksiyonu ..................................................................................................... 48

INT fonksiyonu....................................................................................................... 49

FRAC fonksiyonu................................................................................................... 49

TRUNC fonksiyonu................................................................................................. 49

ROUND fonksiyonu................................................................................................ 49

ODD fonksiyonu..................................................................................................... 49

SQR fonksiyonu.................................................................................................... 49

SQRT fonksiyonu................................................................................................... 49

SIN fonksiyyonu..................................................................................................... 49

COS fonksiyonu..................................................................................................... 49

ARCTAN fonksiyonu.............................................................................................. 50

EXP fonksiyonu...................................................................................................... 50

LN fonksiyonu......................................................................................................... 50

**ALT PROGRAMLAR**

**PROSEDÜR ALT **PROGRAMLARI..................................................................................................... 51

Prosedür Kuralları................................................................................................... 51

Prosedürlerde Değer Aktarımı................................................................................ 51

Değer Aktarmayan prosedürler (RAREMETRESİZ PROSEDÜRLER) ............................. 51

Değer Aktaran Prosedürler (PAREMETRELİ PROSEDÜRLER)....................................... 52

Tek Yönlü Değer Aktarımı................................................................................................. 52

Çift Yönlü Değer Aktarımı................................................................................................. 52

FONKS İYON ALT PROGRAMLARI...................................................................... 52

FONKSİYON Tanımlama................................................................................................... 52

Özyineleme (iç içe fonksiyon Kullanımı) .......................................................................... 53

Alt Programların Yan Etkileri.............................................................................................. 53

**BİRİMLER (UNITS)**** **.............................................................................. 53

Pascal Tarafından Desteklenmiş Unit’ler..................................................................... 53

Programcı tarafından Yazılan Unıt ‘ler.......................................................................... 53

**DOSYALAR**

DOSYA KAVRAMI ........................................................................................................... 54

TEXT DOSYALARI (SIRALI ERİŞİMLİ DOSYALAR) ...................................................... 54

Text dosyalarda kullanılan Standart Fonksiyonlar.................................................. 54

Dosya Yaratmak..................................................................................................... 54

Dosyaya Bilgi Yazmak ............................................................................................ 54

Dosyadan Bilgi Okumak.......................................................................................... 54

Dosyaya Bilgi Eklemek............................................................................................ 54

Dosyadan Bilgi Silmek............................................................................................. 56

Dosyadaki Bilgiyi Değiştirmek................................................................................. 56

RECORD TİPİ DOSYALAR (RASGELE ERİŞİMLİ DOSYALAR) .................................. 58

Dosya Yaratmak ..................................................................................................... 58

Dosyaya Bilgi Yazmak............................................................................................. 58

Dosyadan Bilgi okumak........................................................................................... 59

Dosyadan Bilgi Aramak........................................................................................... 59

Dosyadan Bilgi silmek............................................................................................. 59

**PORT‘ LARIN KULLANIMI**

PARALEL PORT’UN KULLANIMI......................................................................... 60

SERİ PORT’UN KULLANIMI......................................................................................... 67

**GRAFİK**

GRAFİK MOD KAVRAMI ..................................................................................... 70

EKRAN BOYUTLARI....................................................................................................... 70

GRAFİK DEYİMLERİ.................................................................................................... 71

**ÖRNEK PROJE PROGRAMLARI**

EDİTÖR PROGRAMLARI YAZMAK....................................................................... 71

Editör Zeminini ve Yazı Rengini Değiştirme...................................................................... 71

Editör Programlarında Bul-Değiştir İşlemleri..................................................................... 72

Fonksiyon Tuşlarında fonkiyonlar Atamak........................................................................ 72

Programlara Şifreli Ulaşma............................................................................................... 73

MOUSE PROGRAMLARI YAZMAK........................................................................ 73

Kursör Görüntüsünü Yok Etmek................................................................................... 74

Mouse Koordinatları Gösteren Program....................................................................... 74

ÇİZİM PROGRAMLARI YAZMAK.......................................................................... 75

PARALEL PORT’UN KULLANIMI..................................................................................... 75

Paralel Port’u Kullanarak Elektirikli Cihazlara Kumanda Eden Program....................... 76

TURBO VISION.................................................................................................... 78

**TURBO PASCAL HATA MESAJLARII**

COMPİLER HATA MESAJLARI............................................................................. 80

RUN-TIME HATA MESAJLARI ................................................................................. 83

**DİZİN**................................................................................................ 83** **** **

**1.BÖLÜM**

## ** TURBO PASCAL‘ A GİRİŞ**

## **EDİTÖR**

## ***Genel Bilgiler***

PASCAL yüksek seviyeli bir compiler dildir. Bu kompiler dilde kaynak programın tamamı

Önce makine diline çevrilir ve EXE uzantılı object program elde edilir. Daha sonra bu kaynak program DOS ortamında sadece ismi yazılarak çalıştırılır.

Pascal kaynak programını yazmak için bir text editörü kullanmak gerekir. Turbo pascal’ın enönemli özelliklerinden birisi de yazma işlemlerini kolaylaştıran özel editörünün bulunmasıdır.

## **Ana Menü**

Turbo pascal programlarınızı yazacağınız IDE ortamında kullanılan editör komutlarını içerir.

## **Alt Menüler**

## ***FILE menüsü***

**Open... F3** ** : **Daha önceden hazırlanmış olan programları ekrana getirir.

**New : **Yeni bir program yazmak gerektiğinde, yeni dosya açmak için kullanılır.

**Save F2 : **Editör içerisinde isim verilmiş bir program varsa , F2’ye basıldığında direkt olarak bu program sürücüye kaydedilir .

**Save as... : **Edit penceresindeki bir programı başka bir isimle kaydetmek istenildiğinde kullanılır.

**Save all : **Pascal editöründe birden fazla pencere açılarak programlar yazılmış ise hepsini birden kaydetmek için kullanılır.

**Change dir... : **Aktif sürücüyü değiştirmek için kullanılır.

**Print : **Aktif penceredeki programı yazıcıdan almak için kullanılır.

**Get info... : **Teknik bilgileri öğrenmek amacıyla kullanılır.

**Dos shell: **Geçici olarak dos ortamına geçmek için kullanılır.

**Exit Alt-x** ** :** Turbo pascal editöründen çıkmak için kullanılır.

## ***EDIT menüsü ***

**Restore Line : **Silinmiş olan en son satırı kursörün bulunduğu pozisyona tekrar getirmek için kullanılır.

**Cut shift-Del : **Seçilmiş bir text parçasını programdan silip, hafızaya alır.

## ***SEARCH menüsü***

**Find... : **Program içerisinde yazılmış olan harf veya kelimeyi bulmak için kullanılır.

**Replace... : ** Program içerisinde yazılmış olan kelimeyi değiştirir.

**Search again : **Replace veya find ile bulunan kelimeden sonra aynı kelimeden olup olmadığını arar.

**Go to line number... : **Kursörü program içerisinde istenilen bir satır numarasına komutlandırmak için kullanılır.

## ***RUN menüsü***

**Run Ctrl-F9 : **Programı derledikten sonra çalıştırmak için kullanılır.

**Program reset Ctrl-F2 : **işaretlenen yeri silmek , programı başlangıç durumuna getirmek amacıyla kullanılır.

**Go to cursor F4 :** Programı kursörün bulunduğu pozisyona kadar çalıştırır.

**Trace into F7 : **Programı satır satır çalıştırır.

**Step over F8 :** Trace into ile aynıdır.

## ***COMPILE menüsü***

**Compile Alt-F9 : **Aktif pencerede bulunan program veya unıt derlenir.

**Make F9 : ** Aktif programı değişen unıt’leriyle derlemek için kullanılır.

**Build :** Programı bütün unit ‘ leriyle yeniden derlemek için kullanılır.

**Destination Memory :** Programı belleğe veya diske derlemesiniseçmek için kullanılır.

## ***DEBUG menüsü***

**Watches : **Watches seçeneğinin bir alt menüsü olan “ edit watch “ ekrana gelir.

**Add Watch : **Program çalışırken değerleri istenen değişenleri eklemek için kullanılır.

**Edit Watch... : **Program çalışırken değerleri izlenecek olan değişken isimlerini yazmamak ve değiştirmek için kullanılır.

## ***OPTIONS menüsü***

**Compiler... : **Derleme seçeneklerini değiştirmek için kullanılır.

**Memory size... :** Bellek büyüklüğünü değiştirmek için kullanılır.

**Linker... :**Bu komut seçilince “ linker “ iletişim penceresi açılır.

**Debugger... :** Debug menüsündeki seçeneklerin özelliklerini değiştirmek için kullanılır.

**Directories... : **Turbo pascal dosyalarının bulunduğu yeri görmek ve bu yerleri değiştirmek için kullanılır.

**Environment : **Beş farklı iletişim kutusunun seçilebileceği bir pencere gelir.

## ***WINDOW menüsü***

**Size/ move Ctrl-F5 : **Aktif pencerenin ekranda kaydırılması için kullanılır.

**Zoom F5 : **Aktif pencerenin ekranda kapladığı alanı genişletmek için kullanılır.

**Tile : **Turbo editörde bulunan pencere birden fazla olduğunda, bu pencereleri daha küçük pencerelere bölerek hesini ekranda görmemizi sağlar.

**Cassade : **Ekrandaki birden fazla pencereyi üst üste getirme durumunu sağlar.

**Next F6 : **Üst üste duran pencerelerden bir sonrakini aktif hale getirir.

**Previous Shift-F6 : **Cassade durumundaki pencerelerden bir öncekini aktif hale getirir.

**Close Alt-F3 :**Aktif pencereyi hafızadan ve ekrandan silmek için kullanılır.

**Output : **Dos ortamındaki program çıktılarını görmek için kullanılır.

**User screen Alt-F5 : **Dos ortamındaki program çıktılarını** **ekranın tamamını kaplayacak şekilde görmemizi sağlar.

**List... Alt-0 : **Açık bulunan penceredeki program dosyalarının isimlerini listeler.

## ***HELP menüsü ***

**Contents : **Turbo pascal ‘daki bölüm başlıklarını ekrana getirerek, istenilen bölüm ile ilgili yardımı seçmek için kullanılır.

**İndex Shift- F1 : **Help dsyasında bulunan komutların tümünü alfabetik sırrayla listelemek için kullanılır.

**Topic search Ctrl-F1 : **Kursörün üzerinde bulunduğu Pascal komutu ile ilgili İngilizce açıklamaları ekrana getirir.

**Previous topic Alt-F1 : **Önceden seçilen help seçeneklerine, geriye doğru birer adım giderek yardımı ekrana getirir.

**Help on help :** Help ekranının kullanılışınıaçıklayan satırlar ekrana gelir.

## **Programın Yazımı (Edit )**

Bir Pascal programı yazmak için ilk önce editörde bulunan diğer programları silip, boş bir ekran oluşturmak gerekir.

** F10 **tuşuna basıp ** FİLE **seçeneğini ışıklandırırız. Sonra file menüsünün içinde bulunan **NEW **kelimesini seçip **Enter **tuşuna basarız. Böylece boş bir ekran açmış oluruz.

Gereksiz yere açılmış NONAME... dosyalarını silmek için;

**ALT+F3 **tuşlarına bir kaç defa basınız.

EDIT, PW editöründe bir satır aşağı inmek için satır sonlarında **enter **tuşuna , içeri doğru girintili yazmak için ise, **tab **tuşuna basılır.

**Pascal programı örneği :**

## **Programın Saklanması (Save)**

Programınızı yazdıktan sonra diskete kaydetmeniz gerekecektir.

**F10** tuşuna basınız, sonra da **F** tuşuna basınız. Aşağı ok tuşuna basarak **Save** seçeneğini ışıklandırıp **Enter** tuşuna basınız. Bu işlem için başka bir yöntemde direkt olarak **F2** tuşuna basmaktır.

## **Programın Derlenmesi (Compile)******

Yazılan bir programın çalıştırılabilmesi için tüm hatalardan arındırılmış olması gerekir. Turbo Pascal Compiler (TCP.EXE), kaynak program içerisinde bu gibi hataları bulur ve programcıya bildirir. Programcı bu hataları düzelttikten sonra tekrar derleme işlemini yapar. Compile komutunu çalıştırmak için, **Alt+C** tuşlarına basınız, Compile seçeneğini ışıklandırarak **Enter** tuşuna basınız. Bu işlem için başka bir yöntem ise **Alt+F9** tuşlarına birlikte basmaktır.

## **Programın Çalıştırılması (Run)******

**F10 **tuşuna sonrada **R** yazınız. Pencere içerisindeki ilk seçenek olan run seçeneği ilk anda ışıklı olduğundan Enter tuşuna basınız. Aynı işlem için daha kısa bir yöntem ise **CTRL+F9** tuşlarına basmaktır. Türbo Pascal sizin programınızı çalıştıracak ve ekranda program çıktısını çok kısa bir sürede görüntüleyecek ve tekrar paskal ana menüsüne geri dönecektir.

Program çıktısını görmek için **Alt+F5 **tuşlarına basınız. Program çıktısı siz herhangi bir tuşa dokununcaya kadar görüntülenecektir. Herhangi bir tuşa basınca tekrar ana menüye dönülür.

Program çıktısını yeniden görmek istediğiniz zaman tekrar** Alt+F5 **tuşlarına basınız.

## **EXE Uzantılı Dosya Oluşturma**

Pascal kaynak programları (programcının editörde yazdığı program) derlendiğinde makine diline çevrilir. Makine diline çevrilmiş olan dosyanın uzantısı EXE’dir. EXE uzantılı dosya olarak diske kaydetmek için, “Compile” Menüsünün altındaki “destination” seçeneğinin karşısındaki bilgiyi “disk” olarak değiştirmek gerekir. Bu bilgi “memory” olarak kalırsa, makine diline çevrilen kaynak program diske kaydedilmez.

Bazı uzun programların derlenmesi sırasında “out of memory” hatası ile karşılaşılabilir. Bu hatanın oluşmasını önlemek için “Option” menüsündeki “Linker Buffer” alanı “disk” olarak değiştirilir.

## **PASCAL KARAKTER SETİ**

Pascal programlarının yazılmasında üç tür karakter kümesi kullanılır. Bunlar sayısal, alfabetik ve özel işaret kümeleridir. Bu karakterler aşağıdaki tabloda verilmiştir.

| **Karakterler** | **Açıklamalar** |  |
| --- | --- | --- |
| **Sayılar** | 0’ dan 9’ a kadar olan rakamlar. |  |
| **Alfabetik Karakterler** | A’ dan Z’ ye İngiliz alfabesindeki büyük harfler. A’ dan Z’ ye İngiliz alfabesindeki küçük harfler. |  |
| Özel İşaretler | **+** | Toplama işlemi ve stringlerin birleştirilmesinde kullanılır. |
| **- / \*** | Aritmetik işlemlerde sırayla çıkarma, bölme ve çarpma işlemleri yapmak için kullanılır. |  |
| **< > =** | Karar işlemlerinde ilişkisel operatörler olarak kullanılırlar. |  |
| **# $** | Sayı yada karakterin başına getirildiğinde başka bir değeri göstermesini sağlar |  |
| **..** | Yanyana yazılan iki nokta, iki ayrı değeri ve bunlar arasında kalan tüm değerleri göstermek için kullanılır. |  |
| **\[ \]** | Bir dizinin indisini göstermek için kullanılır. |  |
| **(. .)** | Bir dizinin indisini göstermek için kullanılır. |  |
| **{ }** | Program içinde açıklama yapmak için kullanılır. |  |
| **(\* \*)** | Program içinde açıklama yapmak için kullanılır. |  |
| **:=** | Değişkenlere değer atamak için kullanılır. |  |
| **.** | Nokta, program sonunu belirtmek için ve sayıların ondalık kısmını yazarken virgül yerine kullanılır. |  |
| **,** | Virgül, listelenecek bir dizi sayı ve stringi birbirinden ayırmak için kullanılır. |  |
| **;** | Noktalı virgül, Pascal deyim veya komutlarını birbirinden ayırmak için kullanılır. |  |
| **‘** | Tek tırnak sembolü, karakter yada stringlerin başlangıç ve sonunu belirtmede kullanılır. |  |
| **:** | Bir değişkenin tipi tanımlanırken değişken listesinin sonunda kullanılır. |  |
| **( )** | Prosedür parametreleri parantez içinde yazılır. |  |
| **{$}** | Bu ikili karakter, derleyiciye yapılan bildiriler için kullanılır. |  |
| **\_** | Alt çizgi, derleyici tarafından karakter olarak kabul edilir ve genellikle değişken ismi tanımlanırken kullanılır. |  |

Yukarıdaki karakterler, açıklamalarda da belirtildiği gibi, derleyici için özel anlamları vardır. Bu nedenle amacı dışında kullanılmamalıdır. Kullanıldığında ise **syntax error (yazım kuralı hatası)** ile karşılaşılır.

## **Turbo Pascal’da Kullanılan**

## **Komut ve Kelimeler**

## ** Pascal’ın Ayrılmış Kelimeleri (Reserved Words)**

Pascal’da işlevleri dışında kullanılmayacak başka deyimlerde vardır. Pascal’da bunlara, **reserved word (ayrılmış kelimeler)** denir. Bunlar programcı tarafından tanımlanamazlar. Örneğin bir değişken adı olarak kullanılamazlar.

Reserved Word (Ayrılmış kelimeler) şunlardır ;

And Extended Not Type

Array File Of To

Begin Forward Or Until

Boolean For Procedure Unit

Byte Function Program Uses

Case Goto Real Var

Char If Record While

Const Implementation Repeat With

Div In Set Word

Do Integer Shortint Xor

Downto Interface Single

Double Label String

Else Longint Text

End Mod Then

## **Turbo Pascal Komutları**

Pascal’ da yine ayrılmış kelimelerden başka, özel özel işlevleri dışında kullanılamayacak standart procedure, function, deişken ve tipler vardır. Standart function ve procedure’ler Pascal derleyici içerisinde tanımlanmışlar. Zaten Pascal’da kullanılan ve çoğu zaman komut veya deyim adı verilen tüm kelimeler (örneğin; writeln, readln, lenght) birer procedure, yani alt programdır. Bunların hepsi Pascal derleyicide hazır olarak tanımlanmıştır. Türbo Pascal kütüphanesi içerisinde hazır bulunan ifadeler aşağıda görülmektedir.

Abs Erase Keypressed Randomize Str

Arctan Exit Lenght Read Succ

Append Exp Line Readln Sound

Assign False Ln Readkey Text

Bar Filepos Lowvideo Rectangle Textcolor

Bar3d Filesize Lst Rename Textbackground

Chr Frac Maxint Reset True

Circle Getdir Mkdir Rewrite Trunc

Close Getdate Normvideo Rmdir Truncate

Closegraph Getmaxx Nosound Round Upcase

Clrscr Getmaxy Odd Seek Val

Concat Getmaxcolor Ord Setdate Wherex

Copy Gettime Outtext Settime Wherey

Cos Gotoxy Outtextxy Setcolor Window

Delline Graphresult Paramcount Setfillstyle Write

Delay Halt Paramstr Setlinestyle Writeln

Delete Initgraph Pi Settextstyle

Detect Ioresult Pos Sin

Ellipse Insline Putpixel Sizeof

Eof Insert Pred Sqr

Eoln Int Random Sqrt

## **PASCAL PROGRAMININ GENEL YAPISI**

**ÖRNEK 1:** Klavyeden isminizi girdiğinizde ekrana bir mesaj yazdıran program.

Programı yazdıktan sonra, kaydedeceğiniz sürücüyü ve directory’ü belirlemek için **F10** tuşuna basıp sonrada **File** menüsünü seçiniz. **Change dir...** komutunu seçip **enter** tuşuna basınız. Şimdi ed programlarınızı kaydedeceğiniz sürücü ve directory için A:\\ yazıp **enter** tuşuna basınız. Bundan sonra saklama işlemi için sadece program adını yazmanız yeterli olacaktır. Çünkü directory bundan sonra A:\\ dır.

Örnek 1’deki programın genel yapısı üç kısımdan meydana gelir.

**Program başlığı**

**Tanımlama bloğu**

** begin**

** Ana program bloğu**

** End.**

## **Program Başlığı**

**Dizilim: PROGRAM **progismi;

**PROGRAM **progismi (Input, Output);

## **Dizilim diyagramı:**

**Örnek: **Program Merhaba;

Program Merhaba (Input, Output);

Bir program başlığı, program deyimi ve bir program isminin aralarına bir karakter boşluk bırakılarak aynı satırda yazılmasıyla oluşur. İkinci yazılış formu ise sadece standart Pascal’ da geçerlidir. Input kelimesi klavyeden data girileceğini, output kelimesi ise program çıktısının ekrana yazılacağını belirtir. Türbo Pascal’da program başlığı kullanmak isteğe bağlıdır. Kullanılmaması hataya neden olmaz.

## **Tanımlama Bloğu******

Tanımlama bloğunda, programın çalışması esnasında kullanılacak tüm isimlerin tanımlanması yapılır. Farklı amaçlar için kullanılan isimler, farklı tanımlama blokları içinde tanımlanırlar. Bu bloklar için başlık olarak kullanılan bildiri deyimleri aşağıda listelenmiştir.

Uses.................................... 1. Unit tanımlama bloğu

Label................................... 2. Etiket tanımlama bloğu

Const.................................. 3. Sabit tanımlama bloğu

Type.................................... 4. Tip tanımlama bloğu

Var...................................... 5. Değişken tanımlama bloğu

Procedure........................... 6. Prosedür tanımlama bloğu

Function.............................. 7. Fonksiyon tanımlama bloğu

## **Tanımlama Bloğunun Bazı Özellikleri******

**\* **Bir programda yukarıdaki tanımlama bloklarının tamamının kullanılması zorunlu değildir.

**\* **Tanımlama bloklarının program içerisindeki sırası da önemli olmadığı gibi, tanımlanan isimlerin program içinde kullanılmaları da zorunlu değildir.

**\* **Her bir tanımlama bloğu birden fazlada tekrarlanabilir.

## **USES bloğu******

**Amaç:** Turbo Pascal standart ünitesi altında tanımlanmış olan prosedür ve fonksiyonları program içerisinde kullanabilmek amacıyla kullanılır.

**Dizilim:** USES ünitlistesi;

**Örnek:** Uses

Crt, Dos, Printer, Verigir ;

Türbo Pascal’da bazı standart prosedürler (clrscr, gotoxy, gibi...) Unit denilen bir dosya adı altında toplanmışlardır. Bu prosedürleri kullanabilmek için hangi Unit altında bulunduğunu Uses tanımlama bloğu içerisinde yazmak gerekir.

## **LABEL bloğu******

**Amaç:** Pascal programlama dilinde satır numarası bulunmayışı nedeniyle, “goto” komutu kullanıldığında program akışının hangi komut grubuna geçeceğini etiketler ile belirtmek gerekir. Program içerisinde goto deyimi ile işlem görecek olan program satırını belirlemek amacı ile kullanılan etiketleri tanımlamak için kullanılır.

**Dizilim:** **LABEL** etiket\_listesi;

**Dizilim diyagramı:**

**Örnek:** Const

Birdol=8704.56;

İsim=’Onur’;

Const başlığı altında birden fazla sabit tanımlaması yapılabilir. Her sabit tanımlaması sonunda noktalı virgül ‘**;**’ kullanılır. Sabit değer olarak bir aritmetik işlem ifadesi yazılamaz.

## **TYPE bloğu**

**Amaç:** Programcı tarafından oluşturulan özel veri tiplerini tanımlamak amacıyla kullanılır.

**Dizilim:** **TYPE******

Tip\_ismi = tip\_tanımı;

**Örnek:** Type

Gunler=(Pazartesi, Sali, Carsamba, Persembe, Cuma, Cumartesi, pazar);

Notlar=0..100;

Sayi=set of 1..9;

Kucuk=’a’..’z’;

Tip tanımlama bloğu “Type” kelimesi ile başlar. Aynı blok içerisinde birden fazla faklı tip tanımlaması yapılabilir. Her tip tanımlaması birbirinden “;” ile ayrılmalıdır. Type bloğunda tanımlanan veri tipleri, “Var“ bloğunda bir değişkenin tipini Tanımlarken kullanılırlar.

## **VAR bloğu**

**Amaç:** Program içerisinde kullanılacak değişken isimlerini tanımlamak amacı ile kullanılırlar

**Dizilim:** **VAR** değişken\_listesi: tip;

**Dizilim diyagramı:**

**Örnek:** Var

İsim , soyad : string;

A, B : integer;

C, D, E : integer;

Değişken listesindeki herbir değişken için hafızada yer ayrılır. Değişkenin içerisine girilecek datanın tipi (string, integer....) iki nokta üst üste “:” ve noktalı virgül “;” arasına yazılarak belirtilir. Aynı tipteki değişkenler birden fazla listeyle Var başlığı altında tanımlanabilir. Programcı tanım bloğunda tanımlanan tipe sadık kalmalıdır.

## **Uygulama bloğu**

Uygulama bloğunda, program mantığı gereğince kullanılacak gerekli Pascal komutları yer alır. Turbo Pascal programında Basic dilinde olduğu gibi program satır numarası kavramı yoktur. Komut ve tanımlamaları birbirinden ayırmak için her komut sonuna “;” konulmuştur. Ana program bloğu “**begin**” kelimesiyle başlar ve “**end.**” Kelimesiyle biter.

**ÖRNEK 2:** Doları Türk Lirasına çeviren program.

Bu program klavyeden girilen dolar miktarının Türk parası karşılığını bulur. Görüldüğü gibi bir Pascal uygulama bloğu “**begin**”** ** kelimesi ile başlıyor, programın işlevlerini yerine getiren komutlar kurallarına göre yazıldıktan sonra”**end**” komutu ile bitiyor.

## **Atama İşlemi**

**Amaç:** Değişkenler içerisinde sabit değerleri yerleştirmek amacı ile uygulanır.

**Dizilim:** Sonuç\_değişkeni:=ifade;

**Dizilim Diyagramı:**

**Örnek:** x := y + z + 2 ;

x := 5 ;

y :=z ;

lira:= birdol \* dol ;

ad:=’Kemal’+’Atatürk’;

ifadeden elde edilen değer sonuç değişkenine atanır. Sonuç un önceki değeri bozulur ve yerine ifadenin değeri yerleşir. İfade tek bir değişken veya sabit olabildiği gibi örnekte de görüldüğü gibi her ikisi de olabilir. Bir atama işlemi ‘;’ ile biter. Bir değişken içerisine atama yapmak için kullanılan işaretin ‘=’ olmayıp ‘:=’ olmasına dikkat ediniz. ‘= ’ işareti sabit tanımlama ve karşılaştırma işlemlerinde kullanıldığını unutmayınız. Aritmetik atama işlemlerinde dikkat edilmesi gereken bir kuralda, sonuç olarak adlandırılan değişkenin tipi, aritmetik işlem sonucunda elde edilen ifadenin sonucuna uygun olmalıdır.

## **Pascal Programlarının Genel Yapısı**

| **Program **program\_ismi; |
| --- |
| **Const** ** **Sabitismi=sabitdeğer; “ “ Sabitismi=sabitdeğer; |
| **Var** ** **değişken\_listesi : tip; “ “ değişken\_listesi : tip; |
| **Begin****** deyim ; “ “ deyim ; |
| **End.** |

Program başlığı

Sabit

tanımlama

Taınlama bloğu

Değişken

tanımlama

Pascal deyimleri Uygulama bloğu

## **Pascal Programlarının Yazım Kuralları**

***Noktalama İşaretleri ve Tanımlama Kuralları ***

Programlar, program başlığı ile başlar. Ancak kullanımı zorunlu değildir.

Program içinde kullanılacak tüm isimler tanımlama bloğu içinde tanımlanmalıdır.

Bütün sabit tanımlamaları **const** kelimesinden sonra gelir.

Bütün değişken tanımlamaları **var** kelimesinden sonra gelir.

**Begin** kelimesi ana program bloğunun başladığını bildirir.

Ana program bloğu, makine diline çevrilip çalıştırılacak olan deyimlerden oluşmuştur.

Programın en son satırı “**end**” kelimesidir.

Her program bloğu birde fazla ‘end‘ deyimi içerebilir, ancak bu ‘end’ deyimleri program sonunu değil alt blokların sonunu gösterir ve sonlarında ‘;’ vardır.

Programın bloğu içindeki deyimler ’;’ ile birbirinden ayrılmalıdır.

‘;’ işareti ilk deyimden önce, ve son deyimden sonra konulması gerekmez.

‘**begin**’ kelimesinden sonra ‘;’ işareti konulması gerekmez.

**Büyük ve Küçük Harf Kullanımı**

Pascal’da, standart deyim veya kullanıcının belirlediği isimlerin büyük veya küçük harflerle yazılması tamamen serbesttir. Çünkü Pascal derleyicisi büyük ve küçük harfler arasında ayırım yapmaz.

**Deyimler Arasındaki Boşluklar ******

Pascal programlarında satır numarası olmadığından, programın okunabilirliğini arttırmak gerekir. Pascal programlarında satır numarası olmadığından, programın okunabilirliğini arttırmak gerekir. Pascal’da bu konuda büyük bir serbesti vardır. Derleyici, komut ve semboller arasına konulacak boşlukları dikkate almaz. Bu sizin programınızı daha iyi okunabilir duruma getirmeniz için önemli bir serbestliktir.

**Okunurluğu Kolaylaştıran Bazı Kurallar******

1.)Virgül ve aritmetik operatörlerden (\*,-,:=,/) önce ve sonra bir boşluk bırakınız.

Netmaas = brut \* vergi veya x := y \* z / 2 gibi.

2.) Begin, end, var, const kelimeleri dışında kalan diğer program satırlarını içeriye girintili olarak yazınız.

Var const

Netmaas : real ; veya mypi = 3.14; gibi..

3.) Bir atama deyimi gibi iki karakter birlikte kullanılan sembolleri birbirinden ayırmayınız.

A:=B\*C; ifadesini,

A : = B \* C ; şeklinde yazamadığımız gibi,

A :

= B

\* C ; şeklinde de yazamayız.

4.) Tanımlama isimleri arasında boşluk bırakılmaz. Ancak okunurluğunu arttırmak için aralarına “\_” konulabilir.

Net\_maas bir\_dol gibi.

**2. Bölüm**

## **SABİTLER DEĞİŞKENLER ve**

## **OPERATÖRLER**

## **SABİTLER******

Bir programın çalışması boyunca değişmeyen değerler “sabit” (constant) olarak adlandırılır. Sabitler const bloğu içerisinde tanımlanırlar. Turbo Pascal derleyicisi tarafından önceden tanımlı olan bazı sabit isimleri vardır. Bu sabit isimlerinin const bloğu içerisinde tekrar tanımlanmasına gerek yoktur.

Pi = 3.1415926536

False = False

True = True

Maxint = 32767

Minint = -32768 dir.

NOT:Falsenin türkçe anlamı yanlış demektir. Truenin ise doğru demektir.

**Sabit (Constant) Tanımlama**

**Dizilim: CONST **sabit\_ismi=sabit\_değer;

**Dizilim Diyagramı:******

ÖRNEK: Const

Birdol=588000.36 ;

İsim=’onur’ ;

Pascal programları içerisinde sabit kullanmak programın okunurluğunu arttırır. Const başlığı altında birden fazla sabit tanımlaması yapılabilir. Her sabit tanımlaması sonunda ‘;’ kullanılır.sabit değer olarak aritmetik işlem ifadesi yazılamaz.

**DEĞİŞKENLER**

Değişkenler verileri bellekte tutmak için kullanılırlar. Her tanımlanan değişken bellekte belirli bir yer ayrılmasına neden olur. Değişkenler içerisine programın akışı içerisinde farklı değerler atanabilir. İçerisinde değer bulunan bir değişkene yeni bir değer daha atandığında, bu değeri içinde barındırır. Bu nedenle değişken adını alırlar.

**Değişken (Variable) Tanımlama******

**Dizilim: VAR** değişken\_listesi : tip;

**Dizilim Diyagramı:**

**Örnek: Var**

** **İsim , soyad : string ;

A , B : integer ;

C , D , E : integer ;

Değişken listesindeki herbir değişken için hafızada yer ayrılır. Değişkenin içerisine girilecek datanın tipi “**:**” ve “**;**” arasına yazılarak belirtilir. Değişken listesindeki değişken isimleri birbirinden “**,**” ile ayrılır. Aynı tipteki değişkenler birden fala listeyle “var” başlığı altında tanımlanabilir. Programcı tanım bloğunda tanımlanan tipe sadık kalmalıdır. İnteger tipte tanımlanmış bir değişkene string tipte bir bilgi giremeyiz.

**Değişken İsimleri**

Bir değişkenin bellekte veri tutabilmesi için bellek hücresine bir isim verme zorunluluğu vardır. Anlamlı değişken adları oluşturmanız, hem program tasarımında hemde programlarınızın okunabilmesi açısından yarar getirir. Ancak isim verirken uyulması gereken bazı kurallar vardır. Bu kurallar, sabit, tip, değişken, procedure, function, etiket isimleri verirken de aynen geçerlidir.

**Değişken ve Sabit İsmi Seçilirken Dikkat Edilmesi**

**Gereken Kurallar**

**1.)** Daima bir harfle başlaması gerekir. Değişken isimleri rakamla başlayamaz.

**2.)** Pascal ayrılmış kelimesi veya pascal komutlarından oluşamaz.

**3.) **63 karakterden daha fazla olamaz. Eğer daha uzun bir isim verilirse ilk 63 karakter geçerli olur.

**4.) **Aritmetik işlem operatörlerini içeremezler.

**5.)** Değişken isimleri arasında boşluk bırakılmaz. Ancak okunurluğu arttırmak için ‘\_’ konulabilir.

**6.)** İçerisine atanacak değeri anımsatacak kısaltmalardan oluşmalıdır.

**7.)** Türkçe karakterleri içeremez.

**Geçerli Değişken Veya Sabit İsimlerine Örnekler**

Harf1, Cm, A, ad\_soyad, Lira, Sayilar, Isim, Adres1

**Geçersiz Değişken Veya Sabit İsimlerine Örnekler**

1Harf, Var, Const, Lira\*Dolar, Ahmet’in, Ad-Soyad, Ülker, Şeker

**Değişken Tipleri**

Pascal’da 15 ayrı değişken tipi vardır. Bu tiplere ek olarak kendi değişken tiplerinizi de tanımlayabilirsiniz. Her değişkenin bir tipi olmalıdır. Bir değişkenin tipi, o değişken için ayrılan bellek bölgesinde ne tür veriler tutabileceğini ifade eder.

**Standart Değişken Tipleri******

Standart veri tipleri Turbo Pascal tarafından belirlenen tipler vardır ki bunlara özel veri tipi denir. Standart veri tipleri aşağıda belirtilmiştir.

1) Integer tipi veriler

Shortint

Longint

Byte

Word

2) Real tipli veriler

Real

Single

Double

Extended

**Tamsayı (Integer) Değişken Tipleri**

Aritmetik işlemlerde kullanılan pozitif ve negatif tam sayılardır. Integer tipte sayıların ondalık hanesi bulunmaz.

**CLRSCR Prosedürü******

Turbo Pascal kütüphanesinde bulunan bu prosedür parametresiz olarak kullanılır. Ekranı silmeye ve kürsörü 1. satır 1. sütuna getirmeye yarar.

**Gerçek (Real) Değişken Tipi******

Ondalık nokta içeren ve üslü biçimde ifade edilen sayılara real tip sayılar denir. Pascalda 4 tip gerçek sayı vardır. (real, single, double, extended)

**Karakter (Char) Değişken tipi**

Char tipi veriler, 255 adet olan ASCII karakterlerin sadece bir tanesinden oluşurlar. Char tipi veriler tek tırnak ‘ ’ içerisine yazılmalıdırlar. Char tipi değişkenler hafızada 1 byte’lık yer işgal ederler.

**String Değişken Tipi******

String tipi veriler, tek tırnak ( ‘) içerisine alınan ve bilgisayar klavyesinden girilebilen karakter kümesinden oluşmuştur. Bir stringin hafızada kapladığı yer karakterlerin toplam sayısına eşittir. Bu sayı en fazla 255 olabilir. Tırnak içerisinde bulunan boşluk karakterleri de bu sayının içerisindedir. Bir string değişken tanımlanırken bu tipe ait verilerin uzunluklarının ne kadar olacağı köşeli parantezler “\[” ve “\]” içinde belirtilmelidir. Belirtilmediği takdirde uzunluk 255 olarak kabul edilir.

**Boolean Değişken Tipi******

Bir karşılaştırma sonucunda elde edilen değer eğer bir değişken içerisine atanmak isteniyorsa, bu değişken boolean tipi olarak var bloğu içerisinde tanımlanmalıdır. Tanımlanan değişken için bellekte bir byte’lık yer ayrılır. Boolean tipi bir değişken içerisine klavyeden ancak true veya false kelimeleri girilebilir.

**Programcının Tanımladığı Değişken Tipleri**

Pascal da tanımlı olmayan, programcı tarafından type tanımlama bloğunda yaratılan ve özel amaçlar için kullanılan veri tipleridir. Pascal’ın standart veri tipleri bir programda tanıma gerek duyulmaksızın kullanılabilir. Ancak bazı durumlarda verilerin işlenmesinde yetersiz kaldıkları görülür. Programcı tarafından yaratlabilecek olan 5 özel veri tipi vardır.

Küme veri tipi (set type)

Sıralı veri tipi (scalar type)

Sınırlı veri tipi (subrange type)

Record veri tipi (record type)

Dizi veri tipi (array type)

**Tip Tanımlama******

Tip tanımlama bloğu type kelimesiyle başlar. Aynı blok içerisinde birden fazla farklı tip tanımlaması yapılabilir. Her tip tanımlaması birbirinden ‘;’ ile ayrılmalıdır. Type bloğunda tanımlanan veri tipleri, Var bloğunda bir değişkenin tipini tanımlarken kullanılırlar.

**Dizi Tipi Değişkenler******

Aynı tipteki birden fazla bilginin tutulduğu değişkenlere (array) dizi tipi değişken denir. Program içerisinde aynı tür bilginin aynı anda saklanması durumu söz konusu olunca, dizi tipi değişkenlerden yararlanılır. Minindis değeri ‘0’, Maxindis değeri ‘32767’ olabilir. Köşeli parantez içerisine yazılan değerler boolean veya char tipi veri olabileceği gibi, sınırlı tip bir veri de olabilir.

**Küme Tipi Değişkenler******

Aynı tipte ve birbiriyle ilgili bilgilerden oluşan nesneler topluluğuna küme denir. Elemanı olmayan kümeye boş küme denir. Pascal daki kümelerde matematikteki tanımı gibidir.

Küme elemanları aynı tip olmalıdır.

Küme elemanları real sayılardan oluşmaz.

Kümeyi oluşturan elemanların arasına ‘,’ konularak “\[ \]” içerisine yazılırlar. Küme elemanları birbirini izleyen dizisel değerlerden oluşuyorsa en küçük ve en büyük değerlerin arasına iki nokta ‘:’ konulur.

**IN Operatörü******

IN operatörü, bir, elemanın bir küme içerisinde bulunup bulunmadığını test eder.

**Küme Tipi Değişkenlerin Tanımlanması ******

Değişken listesinde birden fazla değişken yazıldığında, değişkenler arasına “,” konulması gerekir. Küme tipi değişkenler direkt olarak “var” bloğunda tanımlandığı gibi, “type” bloğunda özel bir tip ismi yaratılarak ta tanımlanabilirler.

**Küme Tipi Değişkenlere Değer Atama******

Küme tipi değişkenlere aynen diğer değişkenlere atama yapılırken kullanılan “:=” atama sembolü kullanılır. Küme değeri olarak, o kümeye atanabilecek küme elemanları olabileceği gibi, sınırlandırılmış küme elemanları da olabilir. Bir küme tipi değişken ifadelerde kullanılmadan önce bir başlangıç değeri almalıdır.

**Küme İşlemleri******

Küme tipi verilerde, matematikte ifade edildiği gibi bileşim, kesişim ve fark kümesi olarak üç şekilde ifade edilir.

**Sıralı Tip Değişkenler ******

Pascal’da integer sayılar ve İngiliz alfabesindeki büyük ve küçük harfler sıralı tip verilerdir. Yani birbiri ardısıra gelen değerlerdir.Bazı programlarda bu sıralı tipler yeterli olmayabilir. Bu durumda programcı özel bir sıralı tip yaratmalıdır.

**Sıralı Tip Değişkenlerinin Tanımlanması******

Bir sıralı tip, o tipin alabileceği tüm değerleri gösteren değerleri içeren bir liste ile tanımlanır. Listedeki değerler birbirinden “,” ile ayrılır ve parantez içerisine alınırlar. Sıralı tip olarak tanımlanan değerler for do döngüsünde de kullanılabilir.

**Sınırlı Tip Değişkenler******

Çoğu programlarda değişkenler içerisine girilecek değerlerin alt ve üst sınırı bilinir.ancak program içerisinde biz bu sınırları tanımlarsak, compiler hatalı girilen bir veri olduğunda programı durdurur ve gerekli hata mesajını ekrana yazar.

**Sınırlı Tip Değişkenlerinin Tanımlanması******

Type bloğu içerisinde tanımlanan “sınırlı\_veri\_tipi\_ismi” yeni tanımlanan bir veridir. “alt sınır” bu veri tipine atanabilecek olan en küçük değer, “üst sınır” ise bu veri tipine atanabilecek en büyük değerdir. Alt sınır ve Üst sınır sıralı tip olmalıdır. Alt sınır her zaman üst sınırdan daha küçük olmalıdır.

**3.Bölüm**

## ** TEMEL GİRİŞ / ÇIKIŞ KOMUTLARI**

## **WRITELN**

**Amaç:**String ve sayısal sabitleri yada değişken içerisindeki değerleri ekrana veya printere yazdırmak için kullanılır.çıkış listesine yazılanlar alt alta yazılır.

**ÖRNEK:3 **Writeln komutu ile yapılan sitringlerin ekrana yazdırılması.

```pascal
Uses crt; Begin Writeln(‘merhaba ‘); Writeln(‘dünya’) End.
```

Program çıktısı

| Merhaba Dünya |
| --- |

## **WRITE**

**Amaç:** String ve sayısal sabitleri yada değişken içerisindeki değerleri ekrana veya printere yazdırmak için kullanılır.çıkış listesine yazılanlar yan yana yazılır.

**Örnek 4:**

```pascal
Uses crt; Begin Write(‘ahmet’); Write(‘okula git’); Readln; End.
```

Program çıktısı

| Ahmet okula git |
| --- |

## **READLN**

**Amaç:**Çevre aygıtlardan(klavye,disk...),değişkenler içerisine veri girmek için kullanılır.

**ÖRNEK 5:**

```pascal
Uses crt; Var Ad,soy,no:string; Begin Write(‘adınızı giriniz’ :);readln(ad); Write(‘soyadınızı giriniz’ :);readln(soy); Write(‘numaranızı giriniz :’);readln(no); Clrscr; Write(ad); Write(soyad); Write(no); Readln; End.
```

Program çıktısı

| Adınızı giriniz : soyadınızı giriniz : numaranızı giriniz : |
| --- |

## **FORMATLI ÇIKIŞ**

**İnteger Sayıların Formatlanması**

**Örnek: **X:4 sayı:3

Örneğin,x:456 ise, writeln(x:8); deyimi ile sayının ekrana yazılışı şöyle olur.

|  |  |  |  |  | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |

**Real Sayıların Formatlanması**

**Örnek: ** X:4: ,Toplam:9:3

Örneğin,x:=34.56 ise, writeln(x:8:3); deyimi ile sayının ekrana yazılışı şöyle olur.

|  |  | 3 | 4 | : | 5 | 6 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- |

**Char Tipi Verilerin Formatlanması**

**Örnek: ** Writeln(c:6); Writeln( ‘a’:4’);

Örneğin, a:=’K’ ise, writeln(a:7) deyimi ile karekterin ekranda görünümü aşağıdaki gibi olur.

|  |  |  |  |  |  | K |
| --- | --- | --- | --- | --- | --- | --- |

**String Tipi Verilerin Formatlanması**

**Örnek: **Writeln(‘TÜRKİYE’:16);

TÜRKİYE

## **VERİ KONTROLÜ**

## **(COMPILER BİLDİRİLERİ)**

**Compiler Bildirisi Tanımlamak**

**Amaç:**Turbo Pascal derleyicisinin bazı özelliklerini, compıler bildirileri ile kontrol altında tutmak için kullanılır.

Örnek: {$B-}

{$R+}

{$ INCLUDE.PAS}

{$B- ,$R+, $I}

## **4.Bölüm**

## ** ****PROGRAM AKIŞININ KONTROLÜ**

## **DALLANMA DEYİMLERİ**

## **IF-THEN deyimi**

**Amaç: **Belli bir koşul oluştuğunda program akışını bir sonraki deyime geçirmek için kullanılır.

**ÖRNEK 6: **If-then deyiminin kullanılışı.Klavyeden 1 sayısı girildiğinde ekrana ’’kapalı’’ ve 0

Girildiğinde ‘’açık’’ mesajını veren program.

```pascal
Uses crt; Var A:integer; Begin Write(‘sayı giriniz(1veya0) : ‘);readln(a); İf a:=1 then Writeln(‘kapalı’); İf a:=0 then Writeln(‘açık’); Readln; End.
```

Program çıktısı

| Sayı giriniz (1veya 0) :0 Açık |
| --- |

## **IF-THEN\_ELSE deyimi**

**Amaç:**Belli bir koşul oluştuğunda program akışını bir sonraki deyime geçirmek için kullanılır.

**ÖRNEK 7:**

```pascal
Uses crt; Var A,b:integer; Begin Clrscr; Writeln(‘1.sayıyı gir’);readln(a); Writeln(‘2.sayıyı gir’);readln(b); If a>b then Writeln(‘1.sayı >2.sayı’); Else Writeln(‘2.sayı >1.sayı’); Readln; End.
```

Program çıktısı

| 1.sayıyı gir **10** 2.sayıyı gir **5** 1.sayı > 2.sayı |
| --- |

## **CASE-OF deyimi**

**Amaç:**bir değerin birden fazla değer ile karşılaştırmasını yaparak,bu eşitliğin bulunması durumunda belli program parçalarının işlenmesini sağlamak için kullanılır.

**ÖRNEK 8:**

```pascal
Uses crt; Var Harf:char; Begin Writeln(‘bir harf girin:’); readln(harf); Case harf of ‘A ‘............’Z’ :Writeln(‘büyük harf’); ‘A ‘............’Z’ :Writeln(‘küçük harf’); else Writeln(‘Bu harf değil’); Readln; End.
```

## **DÖNGÜLER**

GOTO,FOR-DO,REPEAT-UNTIL

## **GOTO DEYİMİ**

**Amaç: **Program akışının değiştirilmesi gereken yerlerde kullanılır.

**ÖRNEK 9: **1’den 5’e kadar olan sayıları ekrana yanyana yazdıran program.

```pascal
Uses crt; Var Sayac:integer; Label Tekrar; Begin Clrscr; Sayac:=0; Tekrar : Sayac:=sayac+1; Write(sayac,’ ‘); İf sayac<5 then goto tekrar; End.
```

## **FOR- DO deyimi**

**Amaç:**Belli bir program parçasını üst üste önceden belirlenen sayıda tekrarlamak için kullanılır.

**Örnek 10: **1’den 10’a kadar olan tam sayıları ekrana yan yana birer boşluk bırakarak yazdıran program.

```pascal
Uses crt; Var İ :integer; begin Clrscr; For i:=1 to 10 do write (i,’ ‘); End.
```

Program çıktısı

| 1 2 3 4 5 6 7 8 9 10 |
| --- |

** ÖRNEK 11**:Ekrana A’dan G’ye kadar olan harfleri,her defasında bir sonraki harfle birlikte yan yana yazdıran program.

```pascal
Uses crt ; Var Harfyaz,sonharf: char; Begin Clrscr; For sonharf:=’A’ to ‘G’ do Begin For harfyaz:=’A’ to sonharf do Write(harfyaz); Writeln; End; End.
```

Program çıktısı

| A AB ABC ABCD ABCDE ABCDEF ABCDEFG |
| --- |

## **WHILE-DO deyimi**

**Amaç:**Bir program bloğunun belli bir şart sağlanana kadar tekrar edilmesi için kullanılır.

**ÖRNEK 12: **Klavyeden girilen cümle içerisinde kaç adet sesli harf olduğunu bulan program.

```pascal
Uses crt; Ch:char; Say:integer; Begin Say:=0; Write(‘Bir cümle yazınız >’); While not eoln do Begin Read(ch); İf ch in [‘A’,’a’,’E’,’e’,’İ’,’i’,’I’,’ı’,’O’,’o’,’ö’,’ö’,’U’,’u’,’ü’,’ü’] then Begin Say:=say+1; End; Writeln(‘yazılan cümlede’,say,’tane sesli harf vardır.’) End.
```

## **REPEAT-UNTIL deyimi**

**Amaç: **Bir program bloğunun,belli bir şart sağlanana kadar ard arda işlenmesini sağlar.

**ÖRNEK 13: **Klavyeden girilen 10 sayıdan Tek ve Çift sayıların toplamını alt alta yazdıran program.

```pascal
Uses crt ; Var A:array[1..10] of integer; E:integer; T:longint; Begin Clrscr; For E:= 1to 10 do Begin Write (E,’.sayıyı gir......:’);readln(A[E]); End; T:=0; E:=0; Repeat E:= E+1; İf A[E] dıv 2<>A[E] / 2 then Begin T:=T+A[E]; End; Until 1=10; Writeln(‘tek sayıların toplamı :’,T); T:=0; 1:=0; Repeat E:=E+1; İf A[E} dıv 2= A[E] /2 then Begin T:=T+A[E]; End; Writeln(‘çift sayıların toplamı:’ ,T); Readln; end.
```

Program çıktısı

| 1.sayı gir........: 4 2. sayı gir........: 5 3. sayı gir........: 9 4. sayı gir........: 2 5. sayı gir........: 3 6. sayı gir........: 1 7. sayı gir........: 5 8. sayı gir........: 8 9. sayı gir........: 2 10. sayı gir.......:9 Tek sayıların toplamı =32 Çift sayıların toplamı=16 |
| --- |

**5.Bölüm**

## ** İNDİSLİ DEĞİŞKENLER**

## **TEK BOYUTLU DEĞİŞKENLER**

Aynı tipte olan verileri sıralı biçimde bellekte tutmak amacıyla tanımlanan değişkenlere dizi (array) tipi değişken denir.

**ÖRNEK 14: **Klavyeden girilen 5 sayının giriliş sırasının tersine yazdırılması.

```pascal
Uses crt ; Type İntarray =array [1..5] of integer ; Const N= 5; Var Sayı :intarray ; İ,j:integer; Begin Clrscr; For i :=1 to 10 do Begin Write (i,’.sayıyı gir>’); readln (sayı [i] ); End; For j :=n down to 1 do Writeln (j,’. Sayi =’,sayi [j] ); End.
```

Program çıktısı

| 1.sayı gir > 34 2. sayı gir >5 3. sayı gir >56 4. sayı gir >87 5. sayı gir >39 5. sayı=39 4. sayı=87 3. sayı=56 2. sayı=5 1. sayı=34 |
| --- |

**Sıralama (sort) İşlemi**

**ÖRNEK 15: **Klavyeden girilen 5 sayının sıralanıp ekrana yazdırılması (büyükten küçüğe).

```pascal
Uses crt; Var A: array [1..5] of integer; I ,k ,m:integer; Begin Clrscr; For I :=1to 5 do Begin Writeln (I,’.sayıyı gir :’); readln (a[I] ); End; For I := 1 to 4 do For k := I +1 to 5 do İf A [k] >A [I] then Begin M := A [ I ]; A : [ I ] := A[ k ]; A [k] :=m; End; For I := 1 to 500 Begin Writeln (A [ I ]); End; Readln; End.
```

Program çıktısı

| 1. sayı gir : 8 2. sayı gir : 6 3. sayı gir : 9 4. sayı gir : 5 5. sayı gir : 2 9 8 6 5 2 |
| --- |

**İKİ BOYUTLU DEĞİŞKENLER**

Tek boyutlu diziler için kullanılan değişkenler ,aynı cinsten verileri bellekte saklamak için kullanılır.

**6.Bölüm**

## ** ****STANDART PROSEDÜR VE FONKSİYONLAR**

## **MKDIR prosedürü**

**Amaç:**Pascal programlarında bir alt directory yaratmak için kullanılır.

**ÖRNEK 16 : **Aktif directory içerisine,klavyeden girilen bir string adıyla directory açan program.

```pascal
Uses crt ; Var Di:string; Begin Write (‘açmak istediğiniz directory ismi >’); readln(di); Mkdir (di); Mkdir (‘lotus’); Mkdir (‘lotus\müsteri’); End.
```

Program çıktısı

| Açmak istediğiniz directory ismi > BASIC |
| --- |

## **PARAMCOUNT fonksiyonu**

**Amaç:** Komut satırındaki paremetre sayısını verir.

**ÖRNEK 17: **Komut satırından paremetre girilip girilmediğini kontrol eden program.

```pascal
Uses crt; Begin İf paramCount < 1 then Writeln(‘Komut satırında paremetre yoktur’) Else Writeln(ParamCount,’paremetre vardır’); End.
```

Program çıktısı

| Komut satırında paremetre yoktur |
| --- |

## **PARAMSTR fonksiyonu**

**Amaç:** Komut satırındaki N inci paremetreyi veya N inci veriyi bir string olarak verir.

**ÖRNEK 18: **Komut satırından girilen paremetreleri okuyup ekrana yazdıran program.

```pascal
Uses crt; Var I :word; Begin For I:=1 to ParamCount do Writeln(paramstr( I ) ); End.
```

## **GETDIR prosedürü**

**Amaç:** Belirlenen sürücüdeki aktif directory ‘ü öğrenmek için kullanılır.

**ÖRNEK 19:** Aktif sürücüdeki aktif directory ismini ekrana yazdıran program.

```pascal
Uses crt; Var S:string; Begin Getdir(0,s); Writeln(‘ Aktif directory(‘,s,’) dır’); End.
```

Program çıktısı

| Aktif directory (A:\\) dır |
| --- |

## **CHDIR prosedürü**

**Amaç:** Pascal programı ile directory değiştirmek için kullanılır.

** ÖRNEK 20:** Önce aktif sürücüde PASCAL directory’si açıp daha sonra o directory içerisine girerek ekranda gösteren program.

```pascal
Uses crt; Var S:string;** ** Begin Mkdır(‘PASCAL’; Chdır(‘PASCAL’); Getdır(0,S); Writeln(‘şu anda (‘,S,’) directory sine geçtiniz’); End.
```

Program çıktısı

| Şu anda (A:\\ PASCAL) directory sine geçtiniz |
| --- |

## **IORESULT fonksiyonu**

**Amaç: **Pascal programları çalışırken oluşan run –time hata kod numarasının Pascal ortamına alınmasını sağlar.

**ÖRNEK 21: **Klavyeden yanlışlıkla integer yerine karekter girildiğinde,programın akışını kesmeden hatayı kullanıcıya düzelttiren program.

```pascal
Uses crt; Var Intsay : integer; Label Hata; Begin { $I-} hata: Write(‘bir sayı giriniz>’); readln(intsay); İf ioresult=106 then Begin Writeln(‘Tam sayı girişi yapmalısınız’); Goto hata; End; Writeln(‘Sayının karesi =’,intsay*intsay); End.
```

Program çıktısı

| Bir sayı giriniz >a Tam sayı girişi yapmalısınız Bir sayı giriniz >4 Sayının karesi =16 |
| --- |

## **RMDIR prosedürü**

**Amaç:**Alt directory’nin silinmesi için kullanılır.

**ÖRNEK 22: **Bir dos komutu gibi çalışan ve türkçe uyarı mesajı üreten directory silme programı.

```pascal
Uses crt; Begin { $I- } RmDir (paramStr(1); İf Ioresult<> 0 then Writeln (‘directory silinemez ‘); Else Writeln (‘directory silindi’); End.
```

## **GETDATE prosedürü**

**Amaç: **Bilgisayarın daha önceden kurulmuş olan tarihini okumak için kullanılır.

**ÖRNEK 23 :** Sistemin tarihini gün,ay,yıl ve haftanın hangi günü olduğunu gösteren program.

```pascal
Uses dos; Const Gunler:array [0..6] of String [9] = (‘Pazar’,’pazartesi’,’salı’,’çarşamba’, ’perşembe’,’cuma’,’cumartesi’); var y,a,g,hg:word; begin getdate (y,a,g,hg); Writeln(‘bugün ‘,g,’ / ‘,a,’ / ‘,y,’ ‘,günler [hg], ‘dir.’); End.
```

Program çıktısı

| Bugün 17/5/1997 Salı dir. |
| --- |

## **GETTİME** **prosedürü**

**Amaç: **Bilgisayarın daha önceden kurulmuş olan saatini okumak için kullanılır.

**ÖRNEK 23 :** Sistemin saatini ekranda gösteren program.

```pascal
Uses dos; Var Sa,da,sn,sl:word; Begin Gettime(sa,da,sn,sl); Writeln(‘saat=’ ,’sa, ’:’ ,da, ‘:’ ,sn, ‘.’ ,sl); End.
```

Program çıktısı

| Saat =3:48:20.80 |
| --- |

## **SETDATE prosedürü**

**Amaç: **Sistemin tarihini yeniden kurmak için kullanılır.

**ÖRNEK 24: **Sistemin tarihini klavyeden girilen sayılara göre kuran program.

```pascal
Uses dos; Var Yıl,ay,gun :word; Begin Write (‘yıl >’); readln(yıl); Write (‘ay >’); readln(ay); Write (‘gun >’); readln(gun); Setdate(yıl,ay,gun); End.
```

## **SETTİME prosedürü**

**Amaç: **Sistemin saatini yeniden kurmak için kullanılır.

**ÖRNEK 25: **Sistemin saatini klavyeden girilen sayılara göre kuran program.

```pascal
Uses dos; Var Sa,da,sn,sl:word; Begin Write (‘saat >’); readln(sa); Write (‘dakika >’); readln(da); Write (‘saniye >’); readln(sn); ** **Sl :=0; Settime (sa,da,sn,sl); End.
```

## **CHR fonksiyonu**

**Amaç: **ASCII kod numarasının karşılığını verir.

**ÖRNEK 26:** ASCII kod numarası 14-25 arasında olan sayıların karakter karşılığını yanlarına numaraları ile birlikte yan yana yazdıran program.

```pascal
Uses crt; Var I :integer; Begin Clrscr; For I :=14 to 225 do Write (i :3,’=’,chr(I) ); Writeln; Writeln (‘ ‘’65’’ in ASCII karşılığı =’ ,#65,’ dir’); Writeln (#7); End.
```

## **ORD**** ****fonksiyonu**

**Amaç: **Bir elemanın tanımlı olduğu kümede kaçıncı sırada olduğunu bulmak için kullanılır.CHR fonksiyonunun tersine çalışır.

**ÖRNEK 27:** Bir elemanın tanımlı olduğu kümede kaçıncı sırada olduğunu ve ‘’A’’ harfinin ASCII kod numarasını bulan program.

```pascal
Uses crt; Type Renkler =(kırmızı,mavi,yeşil,sarı,siyah); Begin Writeln(‘Yeşil in sıralı veri tipindeki sırası =’,Ord(yeşil) ); Writeln(‘ ‘’A’’ harfinin ASCII kodu ‘,Ord (‘A’),’ dır’); End.
```

Program çıktısı

| Yeşil in sıralı veri tipindeki sırası =2 ‘’A’’ harfinin ASCII kodu 65 dir |
| --- |

## **PRED**** ****fonksiyonu**

**Amaç: **Bir elemanın tanımlı olduğu listede o elemandan önce gelen elemanı bulmak için kullanılır.

**ÖRNEK :** PRED (‘B’)----------- ‘A’

## **SUCC**** ****fonksiyonu**

**Amaç:** Bir elemanın tanımlı olduğu listede o elemandan sonra gelen elemanı bulmak için kullanılır

**ÖRNEK :** PRED (‘B’)----------- ‘C’

## **TEXTBACGROUND prosedürü**

**Amaç: **Text modunda zeminin rengini değiştirmek için kullanılır.

**ÖRNEK :** TEXTBACGROUND (7);---** **zeminin rengini beyaz yapar.

## **TEXTCOLOR prosedürü**

**Amaç: **Text modunda ekrandaki karakterin rengini değiştirmek için kullanılır.

**ÖRNEK : **TEXTCOLOR (1);-------** **karakterlerin rengini mavi yapar.

## **LOWVIDEO prosedürü**

**Amaç: **Ekrana yazılan karekterleri mat hale dönüştürmek için kullanılır.

**ÖRNEK 28 : **Lowvideo prosedürü ile karakter renklerini matlaştırma.

```pascal
Uses crt; Begin TextAttr :=White; Lowvideo; Writeln (‘Bu karakterler açık gridir’); TextAttr :=green; Lowvideo; Writeln (‘Bu karakterler mat yeşildir’); End.
```

## **NORMVIDEO prosedürü**

**Amaç:** Ekrana yazılan karekterleri parlak hale dönüştürmek için kullanılır.

## **READKEY fonksiyonu**

**Amaç:** Klavyeden sadece bir karakter okuyup char tipi bir değişkene aktarmak için kullanılır.

**ÖRNEK:** Ch :=readkey;

## **KEYPRESSED fonksiyonu**

**Amaç: **Programın çalışması esnasında klavyeden bir tuşa basılıp basılmadığını kontrol etmek için kullanılır.

**ÖRNEK 29 : **Klavyeden bir tuşa basılıncaya kadar ekranı çeşitli karakterlerle dolduran program.

```pascal
Uses crt; Begin Repeat Write (#176,#219,#178); Until Keypressed; End.
```

## **GOTOXY prosedürü**

**Amaç:** Kursör pozisyonunu istenilen ekranın istenilen koordinatlarına konumlandırmak için kullanılır.

**örnek: **GOTOXY (1,1);--------------Ekranın sol-üst köşesi

## **WINDOW prosedürü**

**Amaç: **Text modunda ekrana pencere açmak için kullanılır.

**Örnek : **Window (1,1,80,25);-------Normal pencere yaratır.

## **COPY fonksiyonu**

**Amaç: **Bir string ifadenin istenilen bir bölümünü elde etmek için kullanılır.

**ÖRNEK 30 : **Bir string içerisinde istenilen bir bölümü ekrana yazdıran program.

```pascal
Uses crt ; Var St1,st2:string; Begin St1 :=’BILGISAYAR’; St2 :=(copy(st1, 1,4) ); Writeln(st1);writeln(st2); End.
```

Program çıktısı

| BİLGİSAYAR BİLGİ |
| --- |

## **CONCAT fonksiyonu**

**Amaç: **Birden fazla stringi birleştirmek için kullanılır.

**ÖRNEK 31:**İki stringi ‘+’ ile birleştiren program.

```pascal
Uses crt; Var St1,st2:string; Begin St1:=Concat(‘Balık’,’esir’); St2:=’Balık’+’esir’; Writeln(st1); Writeln(st2); End.
```

Program çıktısı

| Balıkesir Balıkesir |
| --- |

## **LENGTH fonksiyonu**

**Amaç:** Bir stringin kaç karakterden oluştuğunu bulmak için kullanılır.

**ÖRNEK: **Length (‘Bilgisayar’);-------------10 tam sayı üretilir.

## **POS fonksiyonu**

**Amaç: **Bir string içerisinde başka bir stringin kaçıncı sırada olduğunu bulmak için kullanılır.

**ÖRNEK:**Pos(‘A’,’BİLGİSAYAR’);------------7

## **DELETE prosedürü**

**Amaç: **Bir stringin belirlenen sayıda karakterini silmek için kullanılır.

**ÖRNEK:** Delete(‘ABCDEF’,3,2)---------’ABEF’

**ÖRNEK 32 :**Bir stringden bir bölümünü çıkardıktan sonra geriye kalanın karakterlerini birer birer silerek ekrana yazan program.

```pascal
Uses crt ; Var St,st2:string; I :integer; Begin St :=’Uygulamalarla Temel Bilgisayar’; Delete (st); For I :=1 to length (st) do Begin Delete (st,length(st),1); Writeln(st);end; End.
```

Program çıktısı

| Uyar Uya Uy U |
| --- |

## **INSERT prosedürü**

**Amaç: **Bir stringin arasını açarak başka bir string yerleştirmek için kullanılır.

**ÖRNEK 33 : **‘’Mustafa Atatürk’’ içerisine Kemal stringi yerleştiren program.

```pascal
Uses crt; Var S:string; Begin S:=’Mustafa Atatürk’; Insert (‘Kemal ‘,S,9); Writeln(S); End.
```

Program çıktısı

| Mustafa Kemal Atatürk |
| --- |

## **STR prosedürü**

**Amaç: **İnteger veya Real tipteki verileri String tipine dönüştürmek için kullanılır.

**ÖRNEK: ** STR(235); st=’235’

## **VAL prosedürü**

**Amaç: **String tipindeki sayıları Real veya İnteger tipe dönüştürür.

**ÖRNEK: **VAL (‘723’ N,K); N=723 Kod=0

## **EXIT prosedürü **

**Amaç: **İşlenmekte olan program bloğundan direkt olarak çıkmak için kullanılır.

## **HALT prosedürü **

**Amaç: **İşlenmekte olan programı herhangi bir noktada sona erdirmek için kullanılır.

## **DELAY prosedürü**

**Amaç:** Çalışmakta olan bir programın işlenmesini belirlenen bir süre durdurur.

**ÖRNEK : **DELAY (100) ;

## **SOUND prosedürü**

**Amaç:**Bilgisayarın ses üreticisinden farklı sesler elde etmek için kullanılır.

**ÖRNEK : **SOUND (350);

## **NOSOUND prosedürü**

**Amaç: **Sound prosedürü ile üretilen sesi kesmek için kullanılır.

## **CLREOL prosedürü**

**Amaç: **Bir satırı sonuna kadar silmek için kullanılır.

## **DELLINE prosedürü**

**Amaç:**** **Kursörün bulunduğu satırı silmek için kullanılır**. **

## **INSLINE prosedürü**

**Amaç:** Kursörün bulunduğu satıra boş bir satır eklemek için kullanılır.

## **WHEREX prosedürü**

**Amaç:** Kursörün kaçıncı sütunda bulunduğunu öğrenmek için kullanılır.

## **WHEREY prosedürü**

**Amaç:** Kursörün kaçıncı satırda bulunduğunu öğrenmek için kullanılır.

## **RANDOM fonksiyonu**

**Amaç:** Rasgele sayı elde etmek için kullanılır.

## **SIZEOF fonksiyonu**

**Amaç:**** **Standart tip veya özel tip değişkenlerin bellekte kapladığı byte miktarını verir.

**ÖRNEK : **Sizeof (Integer) ; ----- sonuç 2 ‘dir.

## **UPCASE fonksiyonu**

**Amaç: **Küçük harfleri büyük harfe çevirmek için kullanılır.

## **ABS** **fonksiyonu**

**Amaç: **Bir sayının mutlak değerini almak için kullanılır.

**ÖRNEK: **Abs (34); -----------34 elde edilir.

## **INT fonksiyonu**

**Amaç:** Kesirli bir tamsayının ,tamsayı kısmını elde etmek için kullanılır.

**ÖRNEK: **Int (-18.58);------------18.0 elde edilir.

## **FRAC fonksiyonu**

**Amaç:** Kesirli bir sayının ,kesirli kısmını elde etmek için kullanılır.

**ÖRNEK:**Frac (-18.58); -------------0.58** **elde edilir.

## **TRUNC fonksiyonu**

**Amaç:** Kesirli bir sayının ,tamsayı kısmını elde etmek için kullanılır.

**ÖRNEK:**Trunc (-18.58); -------------18** **elde edilir.

## **Round fonksiyonu**

**Amaç:** Kesirli bir sayıyı yuvarlanmış olarak elde etmek için kullanılır.

**ÖRNEK: **Round (-18.58); -------------19** **elde edilir.

## **ODD fonksiyonu**

**Amaç:** Bir sayının tek veya çift olduğunu kontrol etmek için kullanılır.

**ÖRNEK :** Odd (3);-----faalse

## **SQR fonksiyonu**

**Amaç: **Bir sayının karesini alır.

**ÖRNEK : **Sqr(2);------- 4 elde edilir.

## **SQRT fonksiyonu**

**Amaç: **Bir sayının karekökünü alır.

**ÖRNEK : **Sqrt(5.76);------- 2.4 elde edilir

## **SIN fonksiyonu**

**Amaç: **Radyan cinsinden verilen bir açının sinüsünü elde etmek için kullanılır.

**ÖRNEK :** Sin(30\* pi/180) ;---------0.50000000000

## **COS fonksiyonu**

**Amaç: **Radyan cinsinden verilen bir açının kosinüsünü elde etmek için kullanılır.

**ÖRNEK :** Sin(30\* pi/180) ;---------0.86602540378

## **ARCTAN fonksiyonu**

**Amaç:** Tanjantı bilinen bir açının değerini radyan cinsinden elde etmek için kullanılır.

**ÖRNEK :** Arctan (1.000); --------0.78539816340 radyan

## **EXP fonksiyonu**

**Amaç:**Matematikteki e(2.71828183) sayısının N. kuvvetini elde etmek için kullanılır.

## **LN fonksiyonu**

**Amaç:** Bir sayının logaritmasını bulmak için kullanılır.

**7. Bölüm**

** ****ALT PROGRAMLAR**

## **PROSEDÜR ALT PROGRAMLARI**

Programlama dillerinde ,ana program bloğunu parçalara ayırarak, ayrı program blokları olarak ele alınmasını sağlayan ve ALT PRORAMLAR adı verilen birimler oluşturmak oldukça kolaylık sağlar. Pascal’da iki tür alt program vardır.

1 -) Prosedürler (Procedure)

2- ) Fonksiyonlar (Function)

**1 -) Prosedürler (Procedure)**

**ÖRNEK 34 : **Procedure komutu ile ses ver ve ses kes programı.** ******

```pascal
Uses crt ; Var A,b :integer ; C:char; Procedure ses ver; Begin Repeat A := A+100; Sound (A); Delay (100); Until A=1500; End; Procedure ses kes; Begin Nosound; End; Begin Clrscr; Repeat Writeln (‘1. ses ver:’); Writeln (‘2. ses kes:’); Write (‘seciminiz:’)readln(B); A:=0; Case B of 1:ses ver ; 2:ses kes; else write (‘Hatalı giriş yaptınız’); write (‘Ana menüye dönmek için 3’e basınız. Cıkmak için (h/H) basınız);readln; end; Untıl (C=’h’) or (C=’H’); End.
```

## **FONKSİYON ALT PROGRAMLARI**

Kullanıcı tarafından tanımlanan fonksiyonlar, standart fonksiyonlar gibi yalnızca bir değerin hesaplanmasında kullanılır.

**ÖRNEK 34 : **2 sayının 0 ‘dan 8’e kadar üslerini alan bir ana programda, us(x,y)adında bir fonksiyon fonksiyonunu kullanma.** ******

```pascal
Uses crt; Var J:integer; Function us (x: real ; n:integer) :real ; var Carpim:real; İ: integer; Begin Carpım:=1; For i:=1 to n do Carpım :=carpım *x; Us:=carpım; End; Begin Clrscr; For J:=0 to 8 do Writeln(‘2 nin ‘,j,’ nin ci kuvveti’, us(2,j): 5:0); End.
```

Program çıktısı

| 2 nin 0 nin ci kuvveti 1 2 nin 1 nin ci kuvveti 2 2 nin 2 nin ci kuvveti 3 2 nin 3 nin ci kuvveti 4 |
| --- |

**8. Bölüm**

## ** BİRİMLER (UNITS)**

## **Pascal Tarafından Desteklenmiş Unıt’ler**

**Ünite Kullanıldığı yerler**

**---------- --------------------------------------------------------------------------------------------------- **

**Crt ** Ekran,klavye ve ses kontrolünü sağlayan posedürlerin kullanılması gerektiğinde.

**Dos **Bir çok DOS fonksiyonunun kullanılmasını destekler**.**

**Graph **Grafik çizimi ile ilgili prosedürler kullanmak gerektiğinde.

**Printer **Printer kontrol prosedürleri kullanmak gerektiğinde.

**Turbo 3 **Prosedür veya fonksiyonları daha ileri versiyonda kullanılmak istenildiğinde.

## **Programcı Tarafından Yazılan Unıt’ler**

Kullanıcının kendi ihtiyacına göre hazırladığı ünitelere, **’’ kullanıcı üniteleri ‘’** denir.

## **UNIT Tanımlama**

**UNIT **ünite\_ismi;

**INTERFACE**

** **Global tanımlamalar

**IMPLEMENTATION**

** ** Lokal tanımlamalar

Global prosedür ve fonksiyonlar

**END.**

**ÖRNEK 35 : **Clrscr komutunu kullanarak ,türkçe isimli bir prosedürün tanımlandığı Unıt.

```pascal
Unıt ekran; Interface Uses crt; Procedüre sil; Implementation Procedüre sil; Begin Clrscr; End; End.
```

**9. Bölüm**

** ****DOSYALAR**

## **DOSYA KAVRAMI**

Dosyalar iki başlık altında yorumlanır.

**Program dosyası**

Şu ana kadar yaptığımız dosyaların hepsi program dosyasıdır.

**Data dosyası**

Bu tür dosyalar program dosyası tarafından oluşturulmuştur.erişim yine program dosyası tarafından gerçekleştirilir.İki tip Data dosyası vardır.

1-)Text dosyaları (sıralı erişimli data dosyası)

2-)Record tipi dosyalar (Rasgele erişimli data dosyaları)

## **TEXT DOSYALARI (SIRALI ERİŞİMLİ DOSYALAR)**

Text dosyaları karakter içeren satırlardan oluşur.Dosya içerisindeki her bir satır ,bu dosyanın bir kaydı olarak kabul edilir.

## **Text Dosyalarda Kullanılan Standart Fonksiyonlar**

## **EOLN Fonksiyonu**

**Amaç:** Okuyucu kafanın kayıt sonu işareti üzerinde olup olmadığını kontrol etmek için kullanılır.

**ÖRNEK : **Eoln (dosya );

Eoln(d);

## **Dosyaya bilgi yazmak,Dosyadan bilgi okumak,Dosyaya bilgi eklemek ve Dosyadan bilgi okumak.**

**NOT :**Dosyaya bilgi yazmak,Dosyadan bilgi okumak, Dosyaya bilgi eklemek ve Dosyadan bilgi okumak konularının birleştirilerek yapıldığı bir örnektir.

**ÖRNEK 36: **Text dosyasının içinde ‘’10-A sınıfının listesini yazan program.

```pascal
Uses crt ;
Var
Ad : array [1..27 ] of string;
No :array [1.. 27 ] of string;
I,A:integer ;
dd:text;
C: char;
Procedüre kayıt_gir;
Begin
Clrscr;
Assing (dd,’m.m’);
Rewrite(dd);
Writeln(dd,’10-avSınıf listesi ‘);
Writeln (dd,’numarası ‘,adı ve soyadı ‘);
For i := 1 to 27 do
Begin
Write (I,’.öğrencinin numarasını giriniz:’); readln(no [ I ] );
Write (I,’. öğrencinin adını ve soyadını giriniz:’); readln(ad [ I ] );
Writeln (dd,no [ I ],ad [ ı ] );
End;
Close (dd);
Readln;
End;
Procedüre kayıt_ekle;
Begin
Clrscr;
Assing (dd,’ m.m ‘);
Append(dd);
For I :=1 to 27 do
Begin
Write (I,’.öğrencinin numarasını giriniz:’); readln(no [ I ] );
Write (I,’. öğrencinin adını ve soyadını giriniz:’); readln(ad [ I ] );
Writeln (dd,no [ I ],ad [ ı ] );
End;
Close (dd);
Readln;
End;
Procedüre kayıt_oku;
Begin
Clrscr;
Assing (dd,’ m.m ‘);
Reset (dd);
Clrscr;
While not eof (dd) do
Begin
Readln(dd,no [ 20 ],ad [ 20 ] );
Writeln (no [ 20 ],ad [20 ] );
End;
Close (dd);
Readln;
End;
Begin
Repeat
Clrscr;
Writeln(‘1. kayıt girmek ‘);
Writeln(‘2.kayıt ekleme2);
Writeln(‘3.kayıt okuma’);
Writeln(‘seçiminiz:’);readln (a);
Case a of
1: Kayıt_gir;
2: Kayıt_ekle;
3: kayıt_oku;
Else
Writeln (‘hatalı giriş yaptınız’);
Writeln (‘çıkmak için ( H/ h) basınız’); readln©;
End;
Untıl (c= ‘h’) or (c=’H’);
End.
```

## **Dosyadan bilgi silmek,Dosyadan bilgi aramak ve dosyadaki bilgiyi listeleme.**

**NOT :**Dosyadan bilgi silmek,Dosyadan bilgi aramak ve Dosyadaki bilgiyi listelemek , konularının birleştirilerek yapıldığı bir örnektir.

**ÖRNEK 37: **Text tipi dosyalarda, bilgi giriş ,arama,silme,listeleme ile ilgili program.

```pascal
Uses crt;
Var
Uz,x,i,no,not1,not2,not3 :integer;
Ad,soy,ara :string;
Y,ort :real;
Dd:text;
Dev,w,e :char;
Bay :integer;
Procedüre Bilgi_gir;
Begin
{ $I- }
window (40,1,80,13 );textbackround(4);clrscr;
assing (dd,’m.s’);
append (dd);
writeln(dd,’no adı soyadı 1.Not 2.Not 3.Not Ort );
(Write (‘öğrencinin Numarasını giriniz :’); readln (no);
(Write (‘öğrencinin adnı giriniz :’); readln (ad);
(Write (‘öğrencinin soyadını giriniz :’); readln (soy);
(Write (‘öğrencinin 1.Notunu giriniz :’); readln(1.not);
(Write (‘öğrencinin 2.Notunu giriniz :’); readln (2.not);
(Write (‘öğrencinin 3.Notunu giriniz :’); readln (3.not);
if ioresult <> 0 then
Write (‘tekrar giriniz’);
Delay (500);
i := not1+not2+not3;
y:=i/3;
Writeln (dd,no:1,ad:15,soy:12,not1:10,not2:10,not3:10, ‘ ‘,y:5:0);
Close(dd);
End;
Procedüre arama;
Begin
Clrscr;
Assing(dd,’m.s’);
Repeat
Reset(dd);
Write (‘aradığınız öğrencinin adı....’);readln(ara);
Uz:= lenght (ara);
Bay:=0;
Clrscr;
Writeln(’No Adı Soyadı 1.Not 2.Not 3.Not Ort );
While Not eof (dd) do
Begin
Readln (dd,ad,soyad);
if ara =copy(dd,1,uz)then
Begin
Writeln (ad,soy,ort;9,2);bay:=1;
End;
End;
if bay =0 then writeln (‘aradığınız öğrenci listede yok ! ‘);
write (devam için <enter> son(h/H)....’);
dev:=readkey;
Writeln;
Until dev in [ ‘H’,’h’];
Close(dd);
Writeln;
End;
Procedüre liste;
Assing(dd,ad,soy);
Write(ad:17,soy:11);
End;
Close(dd);
Readln;
End;
Begin
Clrscr;
Repeat
Writeln(‘1.Bilgi Girişi’);
Writeln(‘2.Bilgi Ekleme’);
Writeln(‘3.Bilgi Arama’);
Writeln(‘4.Bilgi Listeleme’);
Writeln(‘5.Çıkış’);
Write(‘seçiminiz’);readln(x);
Case X of
1: Bilgi_gir;
2: Bilgi_ekle;
3: Bilgi_arama;
4:Liste;
5:EXIT;
Else
Writeln(‘Hatalı giriş yaptınız’);
Writeln(‘Ana menüye dönmek için bir Tuşa basınız:’);
Write(‘çıkmak için (H/h)basınız:’);readln(W);
End;
Until W in [‘H’,’h’];
End.
```

## **RECORD TİPİ DOSYALAR**

## **(RASGELE ERİŞİMLİ DOSYALAR)**

**NOT:**Dosya yaratmak,Dosyaya bilgi ekleme,ve Dosyadan bilgi okumak konularının birleştirilerek yapıldığı bir örnektir.

**ÖRNEK 38 : **Record Tipi dosyalar ile ilgili program.

```pascal
Uses crt; Label Git; Type ** **Kayit=record; No:integer; Ad:string[10]; Soy[10]; End; Var A,sil: string; Sec,ara:integer; ögrenci:kayit; cev,dev:char; dosya:file of kayit; procedüre kayit_ekle; begin assing(dosya,’nurdan.dat’); repeat rewrite(dosya); write(‘no ‘yu giriniz:’);readln(ögrenci.no); write(‘adı giriniz:’);readln(ögrenci.ad); write(‘soyadı giriniz:’);readln(ögrenci.soy); seek(ögrencino); Write(dosya,ögrenci); Writeln(‘devam etmek istiyormusunuz (‘E/H’); Cev :=readkey; Until cev in [‘H’,’h’]; Close (dosya); End, Procedüre liste; Begin Assing(dosya,’nurdan.dat’);reset(dosya); Writeln(‘No Ad Soyad’); Writeln(‘----------------------‘); Begin Seek (dosya,’ara’); Read(dosya,ögrenci); With ögrenci do Begin Writeln(No,ad:10,soy:10); End; End.
```

## **10.Bölüm**

## **PORT’LARIN KULLANIMI**

## **PARALEL PORT’UN KULANIMI**

Sistem ünitenizin arka tarafında 25 uçlu (pin), D tipi konnektöre paralel port denir.

Bu port kullanarak sisteminizden dışarıya sinyal gönderebilir (Output) ya da dışarı -

dan gelen bir sinyali bilgisayarınıza girerek (Input) bilgisayarınızda işleyebilirsiniz.

Bu portta bağlanan cihazlara gönderilen veya alınan sinyallerin seviyesi standart

TTL seviyesindedir, yani 5 V’tur.Portun adından da anlaşıldığı gibi veri alış verişi 8 bit’lik

bir veri seti ile paralel olarak yapılır.Sistem ünitenize bağlı birden fazla paralel port buluna -

bilir. Paralel portlara LPT1, LPT2, LPT3 ... gibi isimler verilir.IBM uyumlu bilgisayarlarda

bulunan 25-pin’li D-tipi konnektörün uç bağlantı numaraları aşağıda görülmektedir.

**PORT REGİSTERLERİ** Bir paralel porta bağlanan cihazdan veri alış/verişi yere kaydedilmesi gerekir.İşte veri kaydı yapılan bu geçici belleğe register denilir.Her registerin hexadesimal olrak ifada edilen bir adresi vardır.Bu register adresleri 378H, 37AH, 379H’dir.

Şimdi bu port registerlerinin kullanılışına, bir paralel printerin kontrolünü örnek olarak

verelim.

**Data Latch, 378 H:**Bu adrese yazılan data, printer buffer’ına ( tampon belleğine ) gönderi

lir ve burada saklanır.Yeni bir daha gönderilene kadar buradaki data sabit kalır.Bu adresteki da -

talar okununca printer buffer’i içerisinde bulunan veri elde edilir.

**Printer Controls, 37A H:**Paralel port kontrol sinyalleri bu port aracılığı ile yapılır.Ayrıca bu adresteki datalar mikroişlemci tarafından okunabilir.Bu adrese gönderilen datalar ile printerin

seçimi, çalışmaya başlatılması, otomatik satır ilerlemesi gibi işlemleri yaptırır.

**Printer Status, 379 H:**** **Paralel printerin durumu ( status ) hakkındaki datalar mikroprose -sörün okuması için bu adreste saklanır.Bu adresteki datalar, printerin meşgul olması, sayfa sonu -

na gelinmesi, printerde hata oluşması gibi priterin durumu ile ilgili bilgileri ifade eder.

Aşağıdaki tipik bir printerin giriş/çıkış sinyalleri gösterilmiştir.Bu tabloda “I” harfi Input,

“O” harfi Output’u “N/A” kullanılmayan ucu gösterir.

| PİN | I/O DURUMU | SİNYAL ADI | PİN | I/O DURUMU | SİNYAL ADI |
| --- | --- | --- | --- | --- | --- |
| 1 | O | Strobe | 14 | O | Auto Feed XT |
| 2 | I/O | D0 | 15 | I | Error |
| 3 | I/O | D1 | 16 | O | Initialize |
| 4 | I/O | D2 | 17 | O | Select Input |
| 5 | I/O | D3 | 18 | N/A | Ground |
| 6 | I/O | D4 | 19 | N/A | Ground |
| 7 | I/O | D5 | 20 | N/A | Ground |
| 8 | I/O | D6 | 21 | N/A | Ground |
| 9 | I/O | D7 | 22 | N/A | Ground |
| 10 | I | ACK | 23 | N/A | Ground |
| 11 | I | Busy | 24 | N/A | Ground |
| 12 | I | Printer Enable | 25 | N/A | Ground |
| 13 | I | Select |  |  |  |

Tablodan da anlaşılacağı gibi **2, 3, 4, 5, 6, 7, 8, 9 **numaralı uçlar data uçlarıdır.Bu uçlar

dan hem data çıkışı ( Output ) hem de data girişi ( Input ) yapılır.

Sadece sinyal giriş yapılabilecek uçlar **10, 11, 12, 15 **numaraları uçlar,sadece sinyal çı-

kışı yapılabilecek uçlar ise **1, 14, 16, 17 **numaraları uçlardır.

**2-9 **numaralı data uçlarına sinyal göndermek için **378** adresi ile belirlenen register kul -lanılır.Diğer uçları kullanabilmek için de **37A** ve **379 **adreslerinin kullanıldığını printer kontro -

lü için verdiğimiz örneklerde açıkladık.

## **Paralel Port Test Cihazının Yapımı**

*** ***Paralel porta veri gönderen programların çalışıp çalışmadığını görebilmeniz amacıyla

basit bir devre kuralım.Bu devreyi kurmak için aşağıdaki malzemelere ihtiyacınız olacak **:**

** 1 Adet Printer Konnektörü **

** 1 Adet Segmet Display**

**7 Adet 330 Ohm Direnç **

**1 Metre 8’li Data Kablosu**

Portlara gönderilen sinyalin seviyesini görmek için en basit devre **2-9 **uçlarından her

birine LED bağlamaktır.Aşağıda gördüğünüz devreyi bir delikli pertinax üzerine kurduktan

sonra uygun bir kutu içerisine yerleştirirseniz, port kontrolü için yapacağınız programların çık-

tısını görmeniz mümkün olacaktır.Aksi halde bizim bu kitapta verdiğimiz örnek programların

çıktılarını da görmeniz mümkün değildir.

## **PORT Komutu **

**Amaç :**Bilgisayarın bir paralel port register’ine veri yazmak veya registerden veri okumak amacıyla kullanılır.

**Dizilim : PORT \[$**Register\_adresi **\]:=**veri;  veri göndermek için

Integer\_değişken**:=PORT \[$**Register\_adresi**\]; **** **veri okumak için

**Örnek :** **Port \[$378\]:=5;**

** i:=port\[$378\];**

Port komutu ile bir paralel port registerine veri göndermenizde o veri **2-9** numaralı uçlar arasında görülür.Bir uca veri göndermek, o uçtaki gerilimin **5 V** olması demektir.Yukarıda veri –len ilk örnekte **378 **adresine **5** verisi gönderildiğinde paralel portun **2** ve **4** numaraları uçlarında

**5 V**’luk gerilim görülür.İkinci örnekte adresi **378** olan port registerleri içerisindeki bilgi okunarak

**“i”** değişkeni içerisine atanır**.”i”** değişkeninin tipi integer olmalıdır.

## ***Port Registeri İçerisine Yazılacak Verinin Tespit Edilmesi***

Paralel portun data giriş ve çıkış uçları **2-9** olduğuna göre bu uçlara gönderilecek olan veri **8 bit** olmalıdır.Gönderilecek verinin binary karşılığı bulunduktan sonra bu sayı desimale dönüştü- rülmelidir.Örneğin paralel portun **2** ve **4** numaralı uçlarını **5 V’**luk gerilim gönderelim.Bunun için **2-9** sırasındaki uçları aşağıdaki gibi gösterebiliriz.

| Pin Numarası | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Data Numarası | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 |
| Display Segmenti |  | g | f | e | d | c | b | a |
| Basamak Değeri | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 5 V. Gönderilecek Olan Uçlar |  |  |  |  |  | 1 |  | 1 |
| Desimal Karşılığı |  |  |  |  |  | 4 |  | 1 |

Yukarıdaki tablodan registere **5** sayısının gönderilmesi gerektiğini buluruz.Veriyi göndermek için program içinde **“port\[$378\]:=5” ** yazmak yeterlidir.Tabloya dikkat edilecek olursanız paralel port test cihazında **a** ve **c** segmentlerinin yanacağını anlayacaksınız.

**Örnek 39 :7** segment displayın tüm **LED’**lerini belirli sürelerde yakıp söndüren program.

```pascal
Program Port 1; Uses Dos,Crt; Var I : integer; Begin Repeat Port [$378]:=127; Delay (3000); Port [$378]:=0; Delay (3000); Until Keypressed; End.
```

**Örnek 40 : 7** segment displayın **LED’**lerini a’dan g’ye doğru belirli aralıklara yakan ve herhangi bir tuşa basınca duran program.

```pascal
Program Port 2; Uses Dos,Crt; Var I , J :integer; Begin Repeat For J:=0 to 7 do Begin Delay (4000); Port [$378]:=Trunc(Exp (J*Ln (2))); I:=Port [$378]; Writeln( I ); End; Until Keypressed; End.
```

** 7 **segment displayın **LED’**lerini sırayla yakmak için **378** adresine **1, 2, 4, 8, 16, 32, 64** sayılarını sırasıyla göndermek gerekir. **“Trunc (Exp (J\* Ln (2)))”** ifadesi bu sayıları üretmek için kullanılmıştır.

**“I:=Port \[$378\]”** ifadesiyle **378 **adresinden okunan veri **“I” **değişkeni içerisine atanmış ve **“Writeln” **komutu ile ekrana yazdırılmıştır.Daha önce de belirtildiği ** **gibi **378** adresindeki **“Data Latch” **registerine yazılan veri, yeni bir veri gönderilinceye kadar paralel port uçlarında aynen tutulur.Bu nedenle **378** adresindeki veri bir önceki komutla gönderilen veridir.

**Örnek 41 : 7** segmentli displayın **LED’**lerini önce a’dan f’ye daha sonra f’den a’ya doğru yakan, bu işleme herhangi bir tuşa basıncaya kadar devam eden program.

```pascal
Program kara_simsek; Uses Dos,Crt; Var I, J :integer; Begin Repeat For J:=0 to 5 do Begin Delay(4000); Port [$378]:=Trunc(Exp (J*Ln(2))); I:=Port[$378]; Writeln( I ); End; For J:=5 downto 0 do Begin Delay(4000); Port [$378]:=Trunc(Exp (J*Ln(2))); I:=Port[$378]; Writeln( I ); End; Until Keypressed; End;
```

**Örnek 42 : **Klavyeden girilen **0-9 **arasındaki sayıları **7 **segment displayda gösteriri program.

```pascal
Uses Dos,Crt; Var I, J:integer; Begin Repeat Clrscr; Writeln(‘ 0-9 Arasında Bir Sayı Giriniz ’); Write(‘ 99 Sayısı Girince İşlem Sona Erer : ‘);Readln( J ); Case J of 1: Port [$378]:=6; 2: Port [$378]:=91; 3: Port [$378]:=79; 4: Port [$378]:=102; 5: Port [$378]:=109; 6: Port [$378]:=124; 7: Port [$378]:=7; 8: Port [$378]:=127; 9: Port [$378]:=103; 0: Port [$378]:=63; End; I:=Port[$378]; Writeln( I ); Until J=99; End.
```

**Örnek 43 : 0-9 **arasındaki sayıları sıra ile **7** segment displayda gösteren program.”Delay” komutu ile verilen süreyi değiştirilerek bir kronometre gibi kullanılabilir.

```pascal
Uses Dos,Crt; Var I, J:integer; Begin Repeat For J:= 0 to 9 do Begin Delay(4000); Case J of 1: Port [$378]:=6; 2: Port [$378]:=91; 3: Port [$378]:=79; 4: Port [$378]:=102; 5: Port [$378]:=109; 6: Port [$378]:=124; 7: Port [$378]:=7; 8: Port [$378]:=127; 9: Port [$378]:=103; 0: Port [$378]:=63; End; I:=Port[$378]; Writeln( I ); End; Until Keypressed; End.
```

**4. **ve **5. **Programlarda portlara gönderilecek verinin tespiti aşağıdaki gibi yapılmıştır.Örneğin **7** segment displayda **3** sayısının görülmesi için **a, b, c, d, g **segmentlerinin yanması gerektiği bu- lunur.Daha sonra bu segmentlerin yanması için porta gönderilmesi gereken desimal sayı hesap edilir.

| **Port Numarası** | **9** | **8** | **7** | **6** | **5** | **4** | **3** | **2** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Data Numarası** | **D7** | **D6** | **D5** | **D4** | **D3** | **D2** | **D1** | **D0** |
| **Display Segmenti** |  | **g** | **f** | **e** | **d** | **c** | **b** | **A** |
| **Basamak Değeri** | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
| **5 V Gönderilecek Olan Uçlar** |  | **1** |  |  | **1** | **1** | **1** | **1** |
| **Desimal Karşılığı** |  | **64** |  |  | **8** | **4** | **2** | **1** |

Yukarıdaki tabloda göre basamak değerlerinin desimal karşılığı toplanacak (**64+8+4+2+1=79) **olursa **3** sayısını displayda göstermek için parelel porta **79** sayısının gönderilmesi gerektiği bulunur.

**Örnek 44 :** 7 segment display’ın tüm LED’lerini belirli sürelerle yakıp söndüren program.

```pascal
Uses Dos,Crt; Var I, J:integer; Begin Repeat Writeln(‘1.Fırını Çalıştır ‘); Writeln(‘2.Kapıyı Aç ‘); Writeln(‘3.Televizyonu Aç‘); Writeln(‘4.Müzik Setini Aç‘); Writeln(‘5.Salon Işığını Aç ‘); Writeln(‘6.Programdan Çıkış ‘); Write(‘Seçiminiz -------->‘);Readln( J ); Case J of 1:Port [$378]:=1; 2:Port [$378]:=2; 3:Port [$378]:=4; 4:Port [$378]:=8; 5:Port [$378]:=16; 6:Exit; End; I:=Port[$378]; Writeln ( I ); Until J = 99 ; End.
```

** 1 13**

** 25 14**

## **Şekil 1-1:Paralel Port’un Pin’lerinin Yerleşimi **

## **Şekil 1-2 :Paralel Port Test Cihazı******

## **SERİ PORT’UN KULLANIMI**

Sistem ünitesinin arkasında 25 pinli ve D tipindeki konnektörlerden biriside seri port’tur.Bo seri port’a RS-232 port’u da denir.Pin sayısı ve görünüş olarak paralel port’a çok benzer, ancak pin numaraları farklıdır.

** 13 1 ******

**25**

Seri iletişim için bir tek kablo yeterlidir.Ancak gönderilen veri bit’lerinin karşı taraftan doğru algılanabilmesi için zamanlamada yanlışlık olmaması gerekir.Yani bir birim ne zaman başlar, ne kadar sürer gibi problemlerin aşılması gerekir.Bunun için yapılacak iki şey vardır.Birincisi; veri kablosunun yanına bir adet clock palsi kablosu ilave edilir ve bu kablo üzerinden peryodik palsler uygulanır.Her pals’in boyu bir birimin iletim süresi olarak kabul edilir.İkinci yol ise; sadece veri kablosu olur.Veriler gönderildikten daha önceden alıcı tarafla anlaşılmış bir protokole uyulur.İkinci yönteme eşzamansız seri iletişim denilir.Bu tür iletişimde gönderilen her birime ayrılan süre, birimlerinin birbirini nasıl takip edeceği önceden belirlenmiştir.

| PİN | I/O DURUMU | SİNYAL ADI | PİN | I/O DURUMU | SİNYAL ADI |
| --- | --- | --- | --- | --- | --- |
| 1 | N/A | Bağlı değil | 14 | N/A | Bağlı değil |
| 2 | O | Data gönderme | 15 | N/A | Bağlı değil |
| 3 | I | Data alma | 16 | N/A | Bağlı değil |
| 4 | O | Gönderme isteği | 17 | N/A | Bağlı değil |
| 5 | I | Göndermek için sil | 18 | N/A | Bağlı** **değil |
| 6 | I | Data seti hazır | 19 | N/A | Bağlı değil |
| 7 | N/A | Bağlı değil | 20 | O | Data transfere hazır |
| 8 | I | RLDS | 21 | N/A | Bağlı değil |
| 9 | N/A | Bağlı değil | 22 | I | Ring indicate |
| 10 | N/A | Bağlı değil | 23 | N/A | Bağlı değil |
| 11 | N/A | 20. pin’e bağlı | 24 | N/A | Bağlı değil |
| 12 | N/A | Bağlı değil | 25 | N/A | Bağlı değil |
| 13 | N/A | Bağlı değil |  |  |  |

**PC’LERDELİ PORT ADRESLERİ**

** Adresi Register Adı Açıklama**

03F8 Transmitter Holding Gönderilecek verinin yazıldığı register

03F8 Receiver Buffer Karşı taraftan alınan verinin yazıldığı register

03F8 Divisor Latch, Low Byte İletişim hızının yazıldığı register

03F9 Divisor Latch, High Byte İletişim hızının yazıldığı register

03F9 Interrupt Enable Register Veri iletişiminin hangi koşullar altında kesme

üreteceğini belirleyen register

03FA Interrupt Idendification Kesme olmuşsa, bu kesmenin hangi sebeple

oluştuğu bilgisini içeren register

03FB Line Control Register İletişin parametrelerini belirleyen register

03FC Modem Control Register Port uçlarındaki işaretlerin değerlerini belirleyen reg.

03FD Line Status Register İletişimde bir hata oluşup oluşmadığını bilgisini

içeren register

03FE Modem Status Register Port uçlarına karşı taraftan verilen işaretlerin

durumunu içeren register

## **11.Bölüm**

## **GRAFİK**

## **GRAFİK MOD KAVRAMI**

Çoğu programlama dillerinde olduğu gibi Turbo Pascal’da da PC’lerin ekran modlarını kontrol eden çok güçlü prosedür ve fonksiyonlarına sahiptir.Şimdiye kadar yapılan programlar 25x80 boyutlarındaki text modunda yapıldı.Bu bölümde Turbo Pascal’ın en sık kullanılan grafik fonksiyon prosedürlerini kullanmasını öğreneceksiniz.

Sisteminizin grafik sürücüsünü belirleyen “ \*.BGI “ dosyaları da yine sisteminizin ulaşabileceği bir disket veya hard diske kayıtlı olması gerekir.

Grafik ortamında yazılan yazıların istenilen fontta olmasını sağlayan “ \*.CHR “ dosyaları da yine sisteminizle ulaşabileceğiniz bir sürücüde hazır bulunması gerekir.

## **EKRAN BOYUTLARI**

Aşağıda, pek çok kullanılan HERCULES ve VGA grafik kartlarında kullanabilecek pixel sayılarını vermemize rağmen, kitapta verilen programlar her tür PC’de çalışacak şekilde hazırlanmıştır.Ancak, bizim burada verdiğimiz grafik kartından farklı bir grafik kartına sahip olan bilgisayar kullanıyorsanız, ekranda herhangi bir noktayı doğru olarak tanımlayabilmemiz için grafik kartınızın pixel sayısını bilmeniz gerekir.Bu grafik elemanının X ve Y eksenlerinde tanımlanabile- cek nokta sayısına **çözünürlük **denir.

Y Y

X X

VGA ekran pixel sayıları HERCULES ekran pixel sayıları

**Bazı Sürücüler ve Çözünürlükleri**

**Ekran Kartı Çözünürlük**

CGACO 320x200

CGAHi 640x200

MCGACO 320x200

MCGAMed 640x200

MCGAHi 640x480

EGALo 640x200

EGAHi 640x350

HercMonoHi 720x348

ATT400CO 320x200

ATT400Med 640x200

AT400Hi 640x480

PC3270Hi 720x350

IBM8514Lo 640x480

IBM8514Hi 1024x768

## **Grafik Ekranına Geçmek**

** **Grafik komutlarının kullanıldığı bir Pascal programı çalıştırabilmek için ekranı grafik moduna geçirmek gerekir.Pascal’da bu işi gerçekleştiren prosedürleri aşağıda inceleyeceğiz.

***Detect fonksiyonu***

**Amaç : **Default grafik sürücüyü arayıp sisteme otomatik olarak dahil etmek için kullanılır.

**Dizilim : **int\_değişken :=** DETECT ******

**Örnek : **Grsur : Detect;

***DETECTGRAPH**** **** Prosedürü*********

**Amaç : **Sistemin grafik sürücüsünü ve grafik modunu otomatik olarak bulur.

**Dizilim : DETECTGRAPH **(Grsürücü,Grmodu) ;

**Örnek 45 : **Sistemin sürücü kod numarasını ve grafik modunu bulup ekrana yazdıran program.

```pascal
Program Grsur_GR_mod_Bul; Uses Graph ; Var Gs, Gm :Integer; Begin Detectgraph(Gs,Gm) ; Writeln (‘ Sisteminizin Grafik Sürücü Numarası =’,Gs) ; Writeln (‘ Sisteminizin Grafik Modu Numarası = ’,Gm); End.
```

***INITGRAPH Prosedürü***

**Amaç : **Sistemi text modundan grafik moduna geçirmek için kullanılır.

**Dizilim : INITGRAPH (**Grsürücü, Grmodu, GrsürücüPath) ;

**Not : **“ GrsürücüPath “ parametresinin değeri ‘ ‘ olarak verilirse, grafik sürücü dosyasının

aranacağı yer aktif sürücü olduğu varsayılmış olur.

***CLOSEGRAPH Prosedürü***

**Amaç : **Grafik modunu kapatıp tekrar text moduna geçmek için kullanılır.

**Dizilim : CLOSEGRAPH ;**

Her grafik moduna geçtikten sonra, genellikle program sonunda kullanılır.Kullanıldığında ekranı siler.

***GRAPHRESULT Fonksiyonu***

**Amaç : **Grafik komutlarının kullanılması esnasında oluşan hataları kontrol etmek için amacıyla kullanılır.

**Dizilim : **Hatakodu **:= GRAPHRESULT ;**

***SETCOLOR Prosedürü***

**Amaç : **Ekrana çizilecek çizgi rengini belirlemek için kullanılır.

**Dizilim : SETCOLOR (**Renk\_kodu **);**

***GETMAXCOLOR Fonksiyonu ***

**Amaç : **Kullanılan bilgisayarda kullanılabilecek en büyük renk kodu numarasını elde etmek için kullanılır.

**Dizilim : GETMAXCOLOR ;**

***LINE Prosedürü (Ekrana Çizgi Çizmek) ***

**Amaç : **Ekrana belirlenen iki koordinatı arasına çizgi çizmek için kullanılır.

**Dizilim : LINE ( **X1, Y1, X2, Y2 **) ;******

**Örnek 46 : **Ekranın sol-üst köşesindeki belirlenen bölgeye rasgele renkte ve boyutta çizgiler çizdiren program.

```pascal
Program line_ciz ; Uses Crt, Graph ; Var Gs, Gm:Integer ; Begin Detectgraph(Gs,Gm) ; Initgraph (Gs, Gm, ‘ ‘) ; If GraphResult <> 0 then Halt (1) ; Randomize ; Repeat Setcolor ( random (getmaxcolor+1)) ; Line (Random (200) , Random (200),Random (200), Random (200)) ; Delay (100) ; Until Keypressed ; Readln ; Closegraph ; End.
```

***GETMAXX ve GETMAXY Fonksiyonları***

**Amaç : **Ekranda kullanılabilecek maximum X ve Y koordinatlarını bulmak için kullanılır.

**Dizilim : **int\_değ :=** GETMAXX ;**

** **int\_değ := **GETMAXY ;**

***RECTANGLE Prosedürü ( Dikdörtgen Çizmek )***

**Amaç : **Ekrana iki köşe koordinatı belirlenen bir dikdörtgen çizmek için kullanılır.

**Dizilim : RECTANGLE (**X1, Y1, X2, Y2 **) ;**

**Örnek 47 : **Ekranın kullanılabilecek alanını sınırlayan bir dikdörtgen çizen program.

```pascal
Program rectangle_ciz ; Uses Graph ; Var Gs, Gm :Integer ; Begin Detectgraph (Gs, Gm) ; Initgraph (Gs, Gm, ‘ ‘ ) ; If GraphResult <> 0 then Halt (1) ; Rectangle (0, 0, GetMaxX,GetMaxY) ; Readln ; CloseGraph ; End.
```

***CIRCLE Prosedürü ( Daire Çizmek )***

**Amaç :** Koordinatları ve yarıçapı belirlenen bir daireyi ekrana çizmek için kullanılır.

**Dizilim : CIRCLE (** X, Y, YARIÇAP **) ;**

**Örnek 48 : **Ekrana değişik renklerde iç içe daireler çizdiren program.

```pascal
Program circle_ciz ; Uses Crt, Graph ; Var Gs, Gm : Integer ; Yaricap : Integer ; Ch : char ; Begin Gs :=Detect ; Initgraph (Gs, Gm, ‘ ’) ; if GraphResult <> 0 then Halt (1); Randomize ; Repeat For yaricap := 1 to 5 do Begin Setcolor (Random (GetMaxcolor+1 )) ; 0 Circle (100, 100, yaricap*10) ; Delay (100) ; End ; Ch := Readkey ; Until ch = # 27 ; End.
```

***ELLIPSE Prosedürü ***

**Amaç : **Ekrana koordinatları belirlenen bir yere elips çizmek için kullanılır.

**Dizilim : ELLIPSE ( **X, Y, Baş\_açı, Bit\_açı, Xyarıçap, Yyarıçap ) ;

**Örnek 49 : **Ekranın** **belirlenen koordinatlarına bir tam, bir de yarım elips çizen program.

```pascal
Program elips_ciz ; Uses Graph ; Var Gs, Gm :Integer ; Begin Gs := Detect ; Initgraph (Gs, Gm, ‘ ‘) ; if GraphResult <> 0 then Halt (1) ; Ellipse (100, 100, 0, 360, 30, 50) ; Ellipse (100, 100, 0, 180, 50, 30) ; Readln ; CloseGraph ; End.
```

***PUTPIXEL Prosedürü (Nokta Koymak)***

**Amaç : **Ekranın belirlenen koordinatlarına belirlenen renkte nokta koymak için kullanılır.

**Dizilim : PUTPIXEL (**X, Y, Renk\_kodu **) ;**

**Örnek 50 : **Ekranın sol-üst köşesinde belirlenen bir alana içerisindeki rasgele yerlere rasgele renklerde nokta çizen program.

```pascal
Program put_pixel_ciz ; Uses Crt, Graph ; Var Gs, Gm :Integer ; Renk : Word ; Begin Gs := Detect ; Initgraph (Gs, Gm, ‘ ‘) ; if GraphResulr <> 0 then Halt (1) ; Randomize ; Repeat Renk := Random (100) ,Random (100), Renk ) ; Delay (10) ; Until KeyPressed ; Readln ; CloseGraph; End.
```

*** ******SETLINESTYLE Prosedürü***

**Amaç : **Ekrana çizilecek olan çizginin tipini belirlemek amacıyla kullanılır.

**Dizilim : SETLINESTYLE ( **Çizgi\_stili, Pattern, Çizgi\_kalınlığı ) ;

**Örnek 51 : **Ekrana değişik çizgi stilinde ve kalınlıkta çizgi ve dikdörtgen çizen program.

```pascal
Program ciz_stili ; Uses Graph ; Var Gs, Gm : Integer ; Begin Gs := Detect ; Initgraph (Gs, Gm, ‘ ‘) ; if GraphResulr <> 0 then Halt (1) ; Line (0, 0, 100, 0, ) ; SetLineStyle (DottedLn, 0, ThickWidth ) ; Line ( 0, 10, 100, 10 ) ; SetLineStyle (DashedLn, 0, NormWidth ) ; Rectangle (0, 20, 100,40 ) ; Readln ; CloseGraph ; End.
```

***SETFILLSTYLE Prosedürü***

**Amaç : **Sütun grafiği çizilirken, sütunları birbirinden ayırt etmek için içerisine çizilen çeşitli paternleri seçmek için kullanılır.

**Dizilim : SETFILLSTYLE ( **Pattern, renk **) ;**

***BAR Prosedürü (Sütun Grafiği Çizmek)***

**Amaç : ** Ekrana boyutları ve renkleri belirlenmiş sütun grafiği çizmek için kullanılır.

**Dizilim : BAR (**X1, Y1, X2, Y2 **); **

**Örnek 52 : **Ekrana rasgele renklerde ve rasgele patternlerle doldurulmuş sütun grafikleri çizen program.

```pascal
Program bar_ciz ; Uses Crt, Graph ; Var Gd, Gm, I, Gen : Integer ; Ch :char ; Begin Gs := Detect ; Initgraph (Gs, Gm, ‘ ‘) ; if GraphResulr <> 0 then Halt (1) ; Gen := 20 ; Randomize ; Repeat For I := 1 to 5 do Begin SetFillStyle (Random (12), Random (GetMaxcolor)) ; Bar ( I* Gen, I*10, Succ ( I ) *Gen, 300 ) ; End ; Ch :Readkey ; Until ch = # 27 ; CloseGraph ; End.
```

***BAR3D Prosedürü ( 3 Boyutlu Sütun Grafiği Çizmek )***

**Amaç : **Ekrana üç boyutlu sütun grafiği çizmek için kullanılır.

**Dizilim : BAR3D ( **X1, Y1, X2, Y2, Derinlik, Üst **) ;**

**Örnek 53 :** Ekrana değişik boy ve renkte 3 boyutlu sütun grafiği çizen program.

```pascal
Program bar_boy3 ;İ Uses Crt, Graph ; Var Gs, Gm, I, Width :Integer ; Ch : Char ; Begin Gs := Detect ; Initgraph (Gs, Gm, ‘ ‘) ; if GraphResulr <> 0 then Halt (1) ; Width := 20 ; Randomize ; Repeat i := 5 ; While I < 20 do Begin SetFillStyle ( Random (12), Random (GetMaxcolor)) ; Bar3d (I*Width, I*10, Succ ( I )*Width, 300, 20, true ) ; İ := i+3 ; End ; Ch := Readkey ; Until Ch = # 27 ; CloseGraph ; End.
```

***OUTTEXT ve OUTTEXTXY Prosedürleri***

**Amaç : **Grafik ortamında ekrana yazı yazmak için kullanılır.

**Dizilim : OUTTEXT ( ‘** String **‘) ;**

** OUTTEXTXY (‘ **String **‘) ;**

**Örnek 54 : **Grafik ortamında default karakter stilinde Yazı yazdıran program.

```pascal
Program out_text_ciz ; Uses Graph ; Var Gs, Gm :Integer ; Begin Gs := Detect ; Initgraph (Gs, Gm, ‘ ‘) ; if GraphResulr <> 0 then Halt (1) ; Outtext (‘ Outtext komutu ile yazılıdı ‘) ; Outtext (‘ Karakterler Default Stildedir. ‘) ; OuttextXY (‘ 100, 100, ‘OuttextXY Komutu İle Yazılmıştır. ‘) ; Readln; CloseGraph ; End.
```

***SETTEXSTYLE Prosedürü***

**Amaç : **Grafik modunda ekrana yazılacak yazı tipini belirtmek amacıyla kullanılır.

**Dizilim : SETTEXTSTYLE (** Font, Doğrultu, Genişlik **) ;**

**Örnek 55 : **Grafik ortamında ekrana çeşitli font, doğrultu ve büyüklüklerde yazı yazdıran program.

```pascal
Program Set_text_style ; Uses Graph ; Var Gs, Gm : Integer ; Begin Gs := Detect ; Initgraph (Gs, Gm, ‘ ‘) ; if GraphResulr <> 0 then Halt (1) ; SetTextStyle (TriplexFont, Horizdir, 1 ); OuttextXY (0, 1, ‘ Yatay TriplexFont ‘) ; SetTextStyle (GothicFont, Horizdir, 2 ); OuttextXY (0, 20, ‘ Yatay GothicFont ‘) ; SetTextStyle (3, Horizdir, 9 ); OuttextXY (0, 40, ‘ SansSerifFont ‘) ; SetTextStyle (3, VertDir, 4 ); OuttextXY (200, 100, ‘ Dikey SmallFont ‘) ; Readln ; CloseGraph; End.
```

## **12.Bölüm**

## **TURBO PASCAL HATA MESAJLARI**

## **COMPİLER HATA MESAJLARI**

## **Hata Kodu Mesaj Açıklama**

1 Out of memory Sistemin hafızası yetersiz veya program

çok büyük, CONFIG.SYS’den geçersiz

sürücüleri çıkarınız.FILES=20,

BUFFER=20 yapınız.

2 Idenfiler expected Bir pascal reserved kelimesinin tanımla-

ma bloğunda kullanılıyor.

3 Unkown idenfiler Var bloğunda tanımlanmamış bir

değişken programda kullanılıyor.

4 Duplicate idenfiler Bir değişken veya sabit aynı

tanımlamama bloğunda iki defa

tanımlanıyor.

5 Synaxt error Program içerisinde geçersiz bir

karakter kullanılıyor.

6 Error in real constant Sabit real tanımlamada hata var.

7 Error in integer constant Sabit integer tanımlamada hata var.

8 String constant String sabitlerinin sonundaki tırnak

unutulmuş veya fazladan tırnak

konulmuş.

10 Unexpected end of file Bir program bloğu sonuna end

yazılmamış veya “.” unutulmuş.

11 Line too long Bir satıra 126 karakterden daha

fazla yazılmış.

12 Type idenfiler expected Type tanımlayıcı bekleniyor.

13 Too many open files Aynı anda açık olan dosya sayısı

çok fazla CONFIG.SYS deki

FILES=20 olmalı.

14 Invalid file name Dosya ismi geçersiz ya da

belirtilen path yanlış.

15 File not found Belirtilen dosya aktif directory

içerisinde bulunamıyor.

16 Disk full Disket veya harddisk dolu.

17 Invalid compiler directive Geçersiz Compiler bildirisi.

18 Too many files Aynı anda açılmış çı-ok sayıda

dosya var.Gereksiz dosyaları

kapatınız.

19 Undefined type in pointer Pointer tanımında bilinmeyen tip.

Defination

20 Veriable idenfiler expected Değişken tanımlayıcısı

bekleniyor.

21 Error in type Bu sembol ile tip tanımlamasına

başlanamaz.Tip hatası var.

26 Type mismatch Bir atama deyiminde değişken

içine atanan değer ile değişken

tipi arasında uyuşmazlık var.

28 Lower bound greater than Sınırlı tip veri tanımında

upper bound alt sınır, üst sınırdan fazla.

Örneğin “type a=3..1”

29 Ordinal type expected Real, string veya sınırlı tip

veri burada kullanılamaz.

30 Integer constant expected Sadece integer sabit

kullanılabilir.

31 Constant expected Burada sadece sabit kullanılır.

32 Integer or real constant Sadece sayısal sabit kullanılabilir.

33 Type idenfiler expected Tip tanımı gerekiyor.Tipinin

tanımlanması gerekli olan bir

değişkenin tipi tanımlanmamış.

34 Invalid function result type Geçerli olan fonksiyon tipi

sadece standart veri tipleri ve

string tiptir.

36 BEGIN expected Begin kelimesi unutulmuş.

37 END expected End kelimesi unutulmuş.

38 Integer expression expected İfade integer tipte olmalı.

39 Ordinal expression expected İfade sıralı (ordinal) tip olmalı.

40 Boolean expression expected İfade boolean olmalı.

41 Operand type does not match Aritmetik operatör bu tip

operator veriler için uygun değil.

Örneğin (‘A’ div ‘2’)

42 Error in expression Bir ifade içersinde operatör

yazmak unutulmuş.Örneğin

“ a:=5\* ”

50 DO expected DO yazılmamış.

54 OF expected OFF yazılmamış.

55 INTERFACE expected INTERFACE yazılmamış.

57 THEN expected THEN yazılmamış.

58 TO or DOWNTO expected DO veya DOWNTO yazılmamış.

62 Division by zero /, div veya mod operatörü ile

bir sayının sıfıra bölümü

oluşuyor.

63 Invalid file type Readln komutu record tip

dosyada veya Seek komutu text

tipi dosyada kullanılmış.

64 Cannot read or write Bu tip veri read veya write

variables of this type komutu ile kullanılmaz.

66 String variable expected Bu değişken string tip olmalı.

67 String expression expected İfade string tipte olmamlı.

73 Implementation expected Implementotion yazılmamış.

74 Constant and case type Case deyiminin seçici değişkeni

do not match ile etiket tipleri arasında

uyumsuzluk var.

75 Record variable expected Bu değişken record tip olmalı.

76 Constant out of range Sınır dışında kalan bir sabit

değer, değişkene atanmış.

79 Integer or Real expected İfade integer veya real tipte

olmalı.

84 UNIT expected Unit yazılması gerekir.

85 “;” expected “;” yazılması gerekir.

86 “:” expected “:” yazılması gerekir.

87 “,” expected “,” yazılması gerekir.

88 “(“ expected “(“ yazılması gerekir.

89 “)” expected “)” yazılması gerekir.

90 “=” expected “=” yazılması gerekir.

91 “:=” expected “:=” yazılması gerekir.

92 “\[“ or “(.” Expected “\[“ veya “(.” yazılması gerekir.

93 “\]” or “.)” expected “\]” veya “.)” yazılması gerekir.

94 “.” Expected “.” yazılması gerekir.

95 “..” expected “..” yazılması gerekir.

97 Invalid FOR control For deyimi içerisindeki kontrol

variable değişkeni imteger

tipte olmalı.

98 Integer variable expected Integer değişken kullanılmalı.

102 String constant expected String sabit kullanılmalı.

113 Error in statement Bu sembol ile bir deyim yazmaya

başlanamaz.

116 Must be in 8087 mode to Bu ifadenin derlenmesi için

compile this compiler 8087 modunda olmalı.

121 Invailed qualifier Array olarak tanımlanmamış bir

değişken indexli olarak

kullanılmaya çalışıyor.

132 Critical disk error Kritilk bir disk hatası var.

Örneğin sürücüde disket yok.

133 Cannot evaluate this Bu ifade DEBUG fonksiyonu ile

expected değerlendirilemez.Örneğin Sin

fonksiyonu veya bir sabit watch

penceresinde yazılmış.

## **RUN-TIME HATA MESAJLARI**

## **Hata Kodu Mesaj Açıklama**

1 Invalid function number Geçersiz fonksiyon numarası.

Mevcut olmayan DOS

Fonksiyonu çağrılıyor.

2 File not found Reset,Append,Rename veya

Erase komutlarıyla belirlenen

dosya bulunamıyor.

3 Path not found Reset, Rewritre, Append,

Rename, Erase, Chdir, Mkdir

Veya Rmdir komutlatıyla

Belirtilen path bulunamıyor.

4 Too many open file Aynı anda açılan dosya sayısı

çok fazla FILES=20 olmalı.

5 File access errror Reset, Append, Rewrite, rename

Erase, Rmdir komutları

kullanıldığında ortaya çıkar.

6 Invalid file handle Geçersiz bir dosya isteği DOS

sistemine letilmiş.

12 Invalid file access code Geçersiz dosya erişim kodu.

15 Invalid drive number Getdir komutu ile geçersiz bir

sürücü numarası kullanılmış.

16 Connat remove accross Rmdir komutu ile aktif directory

directory silinmeye çalışıyor.

17 Connat rename accross Rename komutu ile aynı

drivers sürücüdeki dosyaların ismi

değiştirilmeye çalışılıyor.

100 Disk read error Read komutu ile EOF

karakterinden sonraki bir kayıt

okunmaya çalışıyor.

101 Disk write error Close, write, writeln komutları ile

dolu bir diskete işlem yapılıyor.

102 File not assigned Assign komutu ile dosya bir

temsilci değişkene atanmamış.

103 File not open Açılmamış bir dosya üzerinde

işlem yapılıyor.

104 File not open for input Text dosyası giriş için açık değil.

105 File not open for output Text dosyası çıkış için açık değil.

106 Invalid numeric format Text dosyasından read veya

readln komutu ile sayısal bir veri

okunurken uygun olamayan bir

sayısal değer ile karşılaşıldı.

150 Disk is write protected Disket yazmaya karşı korumalı.

151 Unknown unit Tanımsız ünite.

152 Drive not ready Disket sürücüye takılmamış veya

sürücü kolu kapatılmamış.

154 CRC error in data Diskete kaydedilmiş datada hata var.

156 Disk seek error Disktekten data okunurken hataya

rastlandı.

157 Unknown media type Disket DOS tarafından tanınmıyor.

158 Sector not found Disket bozuk olduğundan data

bulunamıyor.

159 Printer out of paper Printer’e kağıt takılmamış.

160 Device write fault Hardware hatası nedeniyle disket

veya harddisk’e kayıt

yapılamıyor.

161 Device read fault Hardware hatası nedeniyle disket

veya harddisk’ten data okunamıyor.

162 Hardwae failure I/O portunda arıza tespit edildi.

200 Division by zero /, div ceya mod operatörleriyle

yapılan bölme işleminde sayının

sıfıra bölümü oluşmakta.

201 Range check error {$R+} compiler bildirisi

kullanıldığında bir değişkene

sınırları dışında veri

girilmekte veya bir dizi

değişkenin boyutları sınır dışında

kalıyor.

205 Floating point overflow Tanımlanmamış bir real değişkene

sınırları dışında veri atanmaya

çalışılıyor.

PAGE 1

```pascal
Program Merhaba ;
begin
Writeln(‘Merhaba’)
Writeln(‘Turbo Pascal Dünyasına Hoş geldiniz’);
Writeln(‘Güle güle’);
end.
```

```pascal
Program merhaba;
var
isim : string ;
begin
Writeln(‘isminizi Yazıp Enter Tuşuna Basınız >’);
Readln(isim);
Writeln(‘merhaba ‘,isim,’.’);
Writeln(‘Umarım Pascal öğrenmekten hoşlanırsın !’);
End.
```

program

Program ismi

**;**

const

Sabit ismi

=

Sabit değer

**;******

Var

Değişken ismi

**:******

Tip

**;******

**,******

```pascal
Program dolardan_liraya;
Const
Birdol=585800.25;
Var
dol; lira : real;
begin
Writeln(‘Kaç dolarınız var >’);
Readln(dol);
Lira:=birdol * dol ;
Writeln(dol,‘ABD doları’,lira,’TL. eder.’);
End.
```

Sonuç değişkeni

:=

İfade

;

const

Sabit ismi

=

Sabit değer

;

var

Değişken

ismi

**:**

Tip

**;**

**,**

3) Char tipi veriler

4) String tipi veriler

5) Boolean tipi veriler

6) Array tipi veriler

7) File tipi veriler

8) Text tipi veriler

type

Sınırlı tip

Değişken ismi

=

Alt sınır

..

;

üst sınır

**7x330ohm**

**4+1=5**

0,0

0,0

639,479

719,347

---
*Kaynak: `TURBO PASCAL ' a GİRİŞ 2/TURBO PASCAL ' a GİRİŞ 2.doc` — ÖMER KIROĞLU — 2004*
