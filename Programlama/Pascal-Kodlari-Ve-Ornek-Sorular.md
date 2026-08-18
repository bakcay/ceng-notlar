# Pascal Kodlari Ve Örnek Sorular

## EYLÜL 1

## 1. Temrin Konusu: KLAVYE KULLANIM TEKNİKLERİNİN UYGULANMASI

Örnek çalışma: İstiklâl Marşımızda kullanılacak tuşlar oklarla gösterilecek.

## İSTİKLÂL MARŞI

Korkma, sönmez bu şafaklarda yüzen al sancak;

Sönmeden yurdumun üstünde tüten en son ocak.

O benim milletimin yıldızıdır parlayacak;

O benimdir, o benim milletimindir ancak.

## Çatma kurban olayım, çehreni ey nazlı hilâl !

## Kahraman ırkıma bir gül! Ne bu şiddet bu celal?

## Sana olmaz dökülen kanlarımız sonra helâl…

## Hakkıdır, Hakk’a tapan milletimin istiklâl

Caps Lock: Büyük harf kilitleme tuşudur. Basıldığında büyük yazar.

Space Bar: boşluk tuşu.

Enter: O satırda yazılan bilginin bittiğini belirterek alt satıra geç.

Shift: Rakamlarda kullanıldığında üstte belirtilen fonksiyonları yazar.

Backspace: Geri tuşu işlevlidir. Ekleme noktasını geriye doğru siler.

Fonksiyon tuşları: Bu tuşlara atanmış görevleri yerine getirir.

## EYLÜL 2

## Temrin No 2: DOS komutları- Dizin işlemleri ile ilgili komutlar

Dizin: Dosyaların isimleri, uzantıları, boyutları, yaratıldığı ve son kullanıldığı tarihler hakkında bilgi içeren bölümlere denir.

Kullanıcı sistem üzerinde kendi amacı doğrultusunda dizinleri ve bu dizin içinde başka alt dizinleri yaratabilir. Bu ana dizin alt dizinleri ile birlikte gösterilebilir. Bu takdirde dizin isimlerinin birbirlerine “\\” işareti ile ayrılması gerekiyor.

Ör: ANA isimli bir dizinin DIZIN1 isimli bir alt dizini biçiminde dizin oluşturun.

MD: Dizinlerin yaratılması MKDIR veya MD komutu yardımıyla olur.

## Ör: C>MKDIR MUH

RD: Dizinleri yok etmek için kullanılır.

## Ör: C>RD \\uyg\\sto

Eğer dizin dolu ise aşağıdaki mesaj ile kullanıcı uyarılır.

## Ör: C>RD STO

## Invalid path, not directory or directory not empty

Deltree: Dizinin içerdiği dizin ve dosyaları tümüyle yok edilmesi için kullanılır.

## Ör: C>DELTREE UYG

## Delete directory UYG and all its sub directories?\[y,n\]\_

Sorulan soruya n yanıtı verilirse yok etme işlemi iptal edilir; y yanıtı verilirse silme işlemleri yapılır.

CD: Dizinler arasında hareket sağlar.

## Ör: C>CD

## \\

## C>

## Ör:C>CD UYG

## C>CD MUH

## (işlemleri kısaca aşağıdaki gibi yapılabilir.)

## C>CD \\uyg\\muh

DIR: Dizin içerisinin listelenmesi için kullanılır.

Dır komutu ile dosyalar belirli bir sıraya göre ekrana gelir.

## Ör :C:\\dos>DIR \*.SYS

Bu komut verildiğinde ekrana listelenen görüntüyü yazınız.

Ör: Bu komutu /W parametresi ile deneyiniz.

Eğer dizinlerin tüm alt dizinleri ve onlarında içerdiği dosyaların görüntülenmesi isteniyorsa /S parametresi kullanılır.

TREE: Mevcut tüm dizin ve alt dizinlerin görüntülenmesini sağlar.

Ör: C:\\>TREE komutu sonucunda görüntülenen ekranı yazınız.

XCOPY: Tüm alt dizinleri dosyalarıyla başka konuma kopyalanması işlevini yapar.

## Ör: c>XCOPY \*.\* A:/p

## EKİM 1

## Temrin No 3: DOS komutları- Dosya ve disk işlemleri ile ilgili komutlar

Dosya: Belirli özelliklere sahip bilgilerin bir araya toplanmış biçimi olarak değerlendirilebilir.

Ör:Bir dizinde yer alan ve MUH ile başlayan tüm dosyaları listeleyiniz.

TYPE: Dosya içeriklerini görüntülemek için kullanılır.

Ör: C>TYPE MEKTUP.TXT

Eğer dosya çok uzun ise, ekranın kaymasını engellemek üzere MORE süzgeciyle aşağıdaki gibi kullanılır.

C>TYPE MEKTUP.TXT | MORE

COPY: Dosyaların kopyalanması için kullanılır.

Ör: MUH1.dat isimli dosyayı disket üzerine kopyalamak için hangi komut kullanılır.

Eğer Satıs1 ve Satıs2 dosyalarının birleştirilerek SATIŞ isimli dosyanın yaratılması söz konusu ise bu amaca ulaşabilmek için aşağıdaki komut kullanılmalıdır.

C>COPY SATIS1+SATIS2 SATIS

Eğer disket üzerinde aynı dosya bulunursa aşağıdaki mesaj gelir.

C>COPY \*.\* A:

Overwrite DOSYA1.dat /YES/NO/ALL/?

SYS: Sistem dosyalarını kopyalamak için kullanılır.

Ör: C>SYS A:

DEL: Dosyaların tek tek silindiği gibi toplucada silinmesini sağlar.

Ör: A üzerindeki tüm dosyaları siliniz.

Bazen bu soyaların onaylatılarak silinmesi istenilebilir. Bu durumda ERASE komutu aşağıdaki gibi kullanılır.

C>ERASE A:\*.\* /P

UNDELETE: Silinen dosyaları tekrar kurtarmak için kullanılır.

C>UNDELETE

REN: Dosya isimlerinin değiştirilmesinde kullanılır.

Ör: TEST isimli dosyanın adını STOK1 olarak değiştiriniz.

MOVE: Dosyaların yer değiştirmesi için kullanılır.

Ör: \\USR\\MUH dizini içinde yer alan PROG1 isimli dosyayı \\USR\\TEST isimli dizin içine aynı isimle taşımak için aşağıdaki komut kullanılır. Bu komutu uygulayarak sonucunu yazınız.

C> MOVE \\USR\\MUH\\PROG1 \\USR\\TEST

PRİNT: Yazıcıdan dökümlerin alınması için kullanılır.

Ör: C>PRINT RAPOR

DOSYA NİTELİKLERİ

Dosyalara bazı özellikler kazandırılabilir. Bu özellikleri kazanan dosyalar:

- Sadece okunabilen dosyalar

- Arşiv dosyaları

- Sistem dosyaları

-Gizli dosyalar

ör: çalışmakta olan ana dizindeki dosyaların niteliklerini görüntüleyip yazınız.

C:\\ATTRIB

Ör: TEST isimli dosyaya sadece okunabilir niteliği verin ve kaldırın.

## EKİM 2

## Temrin No 4: T.Pascal editörünün incelenmesi, karakter seti, sabitler, değişkenler, operatörler

Turbo Pascal editörünün genel görünümünü çiziniz.

## Sabitler

Ör:

## const

Ad=’Ali’;

Soyad=’GEZER’;

No=’20’;

Pi=3.14;

Aldıgı\_maas=integer;

Net=integer;

Brüt=integer;

## Değişkenler

Ör:

Uses crt;

## Var

a,b,c:integer;

## Begin

a:=5;

b:=7;

c:=9;

write(a);

write(3\*b);

write(a\*b+c+5);

end.

Karakter seti çiziniz.

Ör:

Uses crt;

Var a,b,c:integer;

c1,c2,c3:char;

## Begin

Writeln(‘Üç tamsayı girin’);read(a,b,c);

Writeln(‘Üç harf girin’);

Readln;

end.

Ör: matematik notunun 4 katı, fizik, biyoloji, kimya notunun 3 katı, bilgisayar notunu 2 katı ve 6 dersin toplanıp ortalaması alınınca öğrencinin ortalaması bulunmaktadır. Ders notlarını ekrandan girip toplam ders ortalamasını ekrana yazan programı yazınız.

## EKİM 3

## Temrin No 5: T.Pascal temel giriş çıkış komutları, program akışının kontrolü

## WRİTE-WRİTELN

Ör: Ekrana ‘GAZİ TEKNİK LİSESİ’ yazan programı yazınız.

Aşağıdaki programların ekran çıktısını inceleyiniz ve yazınız.

1. Uses crt;

Begin

Writeln(‘Turbo Pascal’);

Write(‘Programlama’);

Write(‘dili’);

Readln;

End.

2. uses crt;

var

a,b:integer;

begin

a:=40;

b:=30;

writeln(‘a=’,a);

writeln(‘b=’,b);

writeln(‘a+b’,a+b);

writeln(‘a-b’,a-b);

readln;

end.

Ör: Kendi isim, yaş, kilo, boy bilgilerinizi programı yazarken girip ekrana görüntüleyen programı yazınız.

Ör: Aşağıdaki formatlı yazım örneklerini ve çıktılarını yazınız.

1. Uses crt;

Begin

Clrscr;

Writeln(123456);

Writeln(1:6);

Writeln(12:6);

Writeln(123:6);

Writeln(1234:6);

Writeln(12345:6);

Wrtieln(123456:6);

Readln;

End.

2. uses crt;

var

x:real;

begin

clrscr;

x:=469.2763;

writeln(x);

writeln(x:10);

writeln(x:10:4);

writeln(x:10:3);

writeln(x:10:2);

writeln(x:10:1);

writeln(x:10:0);

readln;

end.

Ör: Klavyeden girilen tuşun hangi tuş olduğunu ekrana yazan programı ve çıktısını yazınız.

Ör: Klavyeden a harfi girilirse ‘Ahmet’, b girilirse ‘Burak’, c girilirse ‘Canan’ yazan programı yazınız.

## 1

## Temrin No 6: T.Pascal döngü komutları ve diziler EKİM 4

## IF THEN

Ör: Klavyeden girilen bir sayı 5veya 5’den büyükse ‘5 veya 5’den büyük bir sayı girdiniz’; 5’den küçük sayı girmişse ‘5’den küçük sayı girdiniz yazan programı ekran görünümü RAM ve CPU değişimlerini yazınız.

Ör: klavyeden girilen sayının 0 ile 10 11 ile 100 ve 100’den büyük olma durumunu ekrana yansıtan programı yazınız.

Ör: Aşağıdaki programı uygulayınız ve sonucu yazınız.

Uses crt;

Var

A:byte;

Begin

Write(‘klavyeden bir sayı giriniz\[1/2/3\]’); readln(a);

İf (a=1) or (a=2) or (a=3) then

Begin

Write(‘1,2,3 sayılarından…’);

Writeln(‘birini girdiniz’)

End;

Readln;

End.

Uses crt;

Var

A:byte;

Begin

Write(‘klavyeden bir sayı giriniz\[1/2/3\]’); readln(a);

İf (a=1) or (a=2) or (a=3) then

Begin

Write(‘1,2,3 sayılarından…’);

Writeln(‘birini girdiniz’)

End

ELSE

Writeln(‘1,2,3 dışında bir sayı girdiniz’);

Readln;

End.

NOT: İf bloğunda şart sağlanınca uyulacak komutlar 1 komuttan fazla ise bu komutların başına ve sonuna begin end eklenir. Ve bu end’den önce ; konulmaz.

Soru: klavyeden girilen not 50’den büyükse ve eşitse ‘GEÇTİNİZ’, değilse ‘KALDINIZ’ yazan programı yazınız.

Soru: Çalışılan saate göre maaş hesaplanan bir kurumda işçi 8 saat ve daha az saat çalışmışsa bu saati 50000TL ile çarpılıp maaşı hesaplanıyor. 8 saatten fazla çalışmışsa saat başı 80000 TL’den hesaplanıyor. Klavyeden girilen saate göre işçinin aldığı maaşı ekrana yazan programı yazınız.

Soru: Klavyeden maaş ve fatura toplamı girilip, bu fatura toplamıyla vergi iadesi hesaplanmaktadır

1)Eğer fatura toplamı alınan maaşa eşit ise vergi iadesi fatura toplamın aynı oluyor.

2) Eğer fatura toplamı 60000TL’dan daha az ve eşitse vergi iadesi fatura toplamının 1/10’u ladar.

3) Eğer fatura toplamı 60000TL’den büyük 120000TL’den küçük veya eşit ise vergi iadesi

6000+((fatura toplamı-60000)\*02) kadar;

4) Eğer fatura toplamı 120000TL’den fazla ve200000TL’ye eşit veya daha az ise vergi iadesi

1800+((fatura toplamı-120000)\*0.12)

5) Eğer fatura toplamı 200000TL’den büyükse vergi iadesi 27600+((fatura toplamı-200000)\*0.05) kadardır.

Girilen değerlere göre vergi iadesini yazan programı yazınız.

IF THEN- ELSE

Aşağıdaki programı inceleyiniz ve sonucunu yazınız.

Bu programda hava sıcaklığına göre bir insanın hangi işleri yapabileceği söylenmektedir.

Uses crt;

Var

İsi:integer;

begin

write(‘Hava sıcaklığını giriniz’);

readln(isi);

writeln;

write(‘Tavsiye edilen faaliyet:’)

IF isi>30 then writeln(‘Yüzme iyi gelir’);

ELSE IF isi>20 then writeln(‘Tenis iyi gelir’);

ELSE IF isi>10 then writeln(‘Basketbol’a ne dersin’);

ELSE IF isi>0 then writeln(‘Sinema sıcaktır üşümezsin’);

ELSE writeln(‘Kartopu oynayalım’);

End.

2

Soru: Bir işçinin günde çalıştığı saat 8 veya daha az ise saat başına 50.000 TL, 8 saatten fazla çalışıyor ise saati 80.000TL den maaşı hesaplanmaktadır. Bu işçinin 30 günde kazandığı maaşı hesaplayan programı yazınız.

Aşağıdaki programı inceleyiniz ve sonucunu yazınız.

Uses crt;

Var

ch1,ch2:char;

h:boolean;

begin

b:=FALSE;

write(‘Klavyede bir tuşa basınız:’);

ch1:=readkey;

writeln;

if ch1=#0 then begin

b:=TRUE;

ch2:=readkey;

end;

IF B THEN begin {b doğru olduğunda}

Writeln(‘İki kodlu tuşa bastınız’);

Wrtieln(‘Basılan tuş:’,ch2’);

End

Else begin

Wrteln(‘Tek kodlu tuşa bastınız’);

Writeln(‘Basılan tuş:’ch1);

End;

Readln;

End.

Bu program çalıştırıldığında yukarı ok tuşuna basıldığını kabul edelim. Bu tuş özel tuş olduğu için iki karakter kodu üretir ve birinci karakteri #0’dır. Bu durumda b boolean değişkenine TRUE değeri aktarılır ve klavye belleğindeki 2. karakter yeni bir readkey komutu ile okunur. B değişkeninde TRUE değeri bulunduğu için IF B THEN yapısından sonraki begin-end bloğundaki komutlar çalışır. Ve ikinci karakter kodunu görüntüler. Yukarı ok tuşunun üretiiği ikinci karakter H harfidir.

Soru: yaşı, boyu,cinsiyeti verilen bir insanın ideal kilosunu hesaplayan programı yapınız.

Formül: bayan ise katsayı 0.8 erkek ise katsayı 0.9 ve ideal kilo=((boy-100)+(yas/10))\*katsayı

CASE –OF

CASE değişken veya ifade OF

Etiket1:komut veya komutlar;

Etiket2:komut veya komutlar;

Etiket n:komut veya komutlar;

\[ELSE komut veya komutlar\]

End;

\* İf ile yaptığınız soruları case of yapısı ile yazınız.

\* Klavyeden girilen yüzlük sistemde bir not için 85-100 arasında ise 5, 70-84 arasında ise 4, 55-69 arasında ise 3, 45-54 arasında ise 2, 25-44 arasında ise 1,değilse 0 yazan programı en kısa biçimde yapınız.

Aşağıdaki programı inceleyiniz ve sonucunu yazınız.

Program karakter\_tespiti;

var ch:char;

begin

write(‘Bir tuşa basınız:’); ch:=Upcase(readkey); {girilen karakteri büyük harfe çevirir}

write(‘girilen karakter:’);

case ch of {1. case yapısı}

‘A’..’Z’: CASE ch OF {2. case yapısı}

‘A’,’E’,’I’,’O’,’U’:writeln(‘Sesli harf’);

else writeln(‘Sessiz harf’); {2. casenin elsesi}

end; {2. case yapısının bitimi}

‘0’..’9’:writeln(‘rakam’);

else {1. casenin elsesi}

writeln(‘Sembol’); {harfde rakamda değilse semboldür}

end; {1. case yapısının bitimi}

readln;

end.

3

FOR-DO

FOR değişken := ilkdeğer TO sondeğer DO

DOWN TO

\[begin\] Komut veya komutlar; \[end\]

Örnekleri inceleyip ekran çıktılarını yazınız.:

Uses crt;

Var

İ:byte;

Begin

Clrscr;

For i:=1 to 10 do

Write(‘T10’);

Readln;

End.

Uses crt;

var

i:byte;

begin

clrscr;

for i:=1 to 10 do

write(i:2);

readln;

end.

Uses crt;

var

i:byte;

begin

clrscr;

for i:=1 DOWNTO 10 do

write(i:2);

readln;

end.Soru: 1’den 10’a kadar olan sayıları ve bu sayıların karelerini yan yana yazan (5 25 gibi) programı yazınız.

Soru: klavyeden girilen 5 sayının ortalamasını bulan programı yazınız.

WHİLE –DO

WHİLE şart DO

While döngüsünde bir şart ifadesi, döngünün hemen başında test edilir. Şart ifadesindeki önerme DOĞRU (TRUE) ise program kontrolü döngüye girer ve şart önermesi DOĞRU OLDUĞU MÜDDETÇE döngüdeki komut veya komutlar tekrarlanır. Şart önermesi yanlışsa döngüden çıkar. Burada sayaç kullanılıyorsa bu sayacı (sayac:=sayac+1 gibi) teker tker programcı kodu ile arttırmak gerekir.

Örnekleri inceleyip ekran çıktılarını yazınız.:

Örnek:

Uses crt;

Var

İ:byte;

Begin

İ:=0; Clrscr;

While i<=10 do

Begin

Writeln(i);

İ:=i+2;

End;

Readln;

End.

Sayı 10’dan küçük ve 10’a eşit olduğu sürece döngü çalışacaktır.çalıştırılması istenen komutlar birden fazla olduğu için begin-end yapısı kullanılmıştır.i:=i+2 komutu ile i sayacının değeri her seferinde 2 arttırılmıştır. Sayı 10 değerini aştığı anda döngüden çıkılır.

Örnek:

Uses crt;

Var i:byte; sa,top:integer; ort:real; ch:char

Begin i:=0; sa:=0; top:=0; ort:=0; ch:=’E’;

WHİLE ch=’E’ DO

Begin

İ:=SUCC(i); (değişkenin değerini 1 arttırır)

Write(‘Bir sayı giriniz=!); readln(sa);

top:=top+sa;

writeln; write(‘Devam etmek istiyormusunuz(e/h):’);ch:=readkey;ch:=upcase(ch);writeln;

end;

ort:=top/i; writeln; writeln(‘toplam=’,top); writeln(‘ortalama=’,ort:6:2);

readln;

end.

4

REPEAT UNTİL

Repeat döngüsü, belirli bir şart YANLIŞ (FALSE) oldukça devam eder. Bu niteliğiyle diğer döngülerden ayrılmaktadır. REPEAT döngüsünün WHİLE döngüsünden farkı şudur: WHİLE döngüsünde şart önermesi döngünün başında, REPEAT döngüsünde ise şart önermesi döngünü sonunda TESTedilir. Bu nedenle REPEAT DÖNGÜSÜ EN AZ BİR KERE ÇALIŞIR. Bu özelliğiyle repeat döngüsü menü programları için ideal bir yapıdır.

REPEAT

Komut ve komutlar;

UNTİL şart;

Örnek:

uses crt;

var i,j:integer;

begin i:=0; j:=0; clrscr;

Repeat

İ:=i+1; j:=j+i;

Until i=10;

Writeln(‘Toplam=’,j);

Readln;

End.

Soru while –do döngü örneklerinden birinci örneği repeat until döngüsü kullanarak yazınız.

Örnek:

Uses crt;

Var a,r,sina,cosa:real; ch:char;

Begin

Ch:=’E’;

Clrscr;

Repeat

Write(‘Açının değerini giriniz=’);readln(a);

r:=a\*(pi/180); (\* Açı radyana çevriliyor\*)

sina:=sin(r); (\*Açının sinüsü bulunuyor\*)

cosa:=cos(r); (\*Açının kosünüsü bulunuyor\*)

writeln;

writeln(‘Girilen açının sinüsü=’,sina);

writeln(‘Girilen açının kosinüsü=’,cosa);

writeln;

write(‘Devam etmek istiyormusunuz(e/h) : ‘);

readln(ch);

UNTİL ch=’H’;

End.

EKİM 5, KASIM 1, KASIM 2

Temrin No 7,8,9: T.Pascal standart procedure ve function uygulamaları

Ör: Aşağıdaki örneği inceleyerek Ram ve ekran görüntüsünü örnekle birlikte defterinize yazınız.

Uses crt;

Var

Sa:array\[1..10\] of integer;

İ:byte;

Begin

Clrscr;

For i:=1 to 5 do begin

Write(i,’. Sayıyı giriniz:’);

Readln(sa\[i\]);

End;

Writeln;

Writeln((‘1. girilen sayı=’,sa\[1\]);

Writeln((‘2. girilen sayı=’,sa\[2\]);

Writeln((‘5. girilen sayı=’,sa\[5\]);

Writeln;

For i:=5 to 10 do

Writeln(i’. Sayı=’,sa\[i\]);

End;

Ör: Aşağıdaki program ilk ölnce bir diziye klavyeden girilen değerleri aktarır. Daha sonrada bu değerleri ikinci iç içe for döngüleri ile küçükten büyüğe sıralar.

Bu örneği önce Step Over komutu ile pascalda çalıştırınız.

Trace yaparak RAM ve ekran görüntüsünü temrin defterinize çiziniz. Sayıları kendiniz belirleyiniz.

Uses crt;

Var

İ,j:byte;

A:array\[1..10\] of integer;

Gec:integer;

Begin

Clrscr;

For i:=1 to 10 do (\*sayıların girildiği bölüm \*)

Begin

Write(i,’.sayıyı giriniz:’);

Readln(a\[i\]);

End;

(\*sıralamanın yapıldığı bölüm. 9 sayısı

eleman sayısı –1 dir. 10 ise eleman sayısıdır \*)

For i:=1 to *9** *do

For j:=i+1 to *10 *do

İf a\[j\] > a\[i\] then begin

Gec:=a\[i\];

A\[i\]:=a\[j\];

A\[j\]:=gec;

Writeln;

For i:= 1 to 10 do

Writeln(a\[i\]);

End.

STRİNGLERİ SIRALAMA

Bu program kalvyeden girilen isimleri a’dan z’ye sıralar

Uses crt;

Var ad:array\[1..100\] of string\[20\]; gec:string\[20\]; i,j,n:byte;

Begin

Clrscr; write(‘Sıralanacak isim sayısı=’);readln(n);

Writeln;

For i:= 1 to n do (\*isimlerin girildiği bölüm\*)

Begin

Write(i,’.adı giriniz=’);readln(ad\[i\]);

End;

Writeln;

For i:=1 to n-1 do

For j:= 1 to 10 do

İf ad\[i\] > ad\[j\] then begin

Gec:=ad\[j\];

Ad\[j\]:=ad\[i\];

Ad\[i\]:=gec;

End;

Writeln;

For i:=1 to n do

Writeln(i,’.isim=’,ad\[i\]);

End.

FONKSİYONLAR VE PROSEDÜRLER

Pascal’da kullandığımız komutlar gerçekte birer prosedür ve fonksiyondur. Örneğin sqrt bir fonksiyondur.

Bu prosedür ve fonksiyonlar pascal tarafından tanımlanmış prosedürlerdir. Bunlara STANDART prosedür ve fonksiyonlar denir. Ayrıca bir de programcı tarafından tanımlanan prosedür ve fonksiyonlar vardır.

FONKSİYONLAR

Genel olarak bir hesap işlemi yaparak bir sayı üretmekte kullanılırlar.

SQRT(değişken adı): bu fonksiyon gönderilen değişken adının değerinin karesini geriye döndür.

Fonksiyonlarda belirleyici özellik şudur :bir veya birden fazla değişken fonksiyona gönderilir. Fonksiyon bu değişken veya değişkenleri kullanarak bir değer üretir.

Ör:

Var

A,sonuc:byte;

Begin

A:=5;

Sonuc:=SQRT(A); (\*sqrt fonksiyonu a değişkeninin içindeki değeri aldı yorumladı sonucu sonuc değişkenine aktardı.\*)

Writeln(‘5in karesi=’,sonuc);

Readln;

End.

Yukarıdaki örnekte sqrt fonksiyonu bir standart fonksiyondur fakat bu fonksiyonu açık bir biçimde yazarsak şudur:

Function sqrt (x:integer): integer;

begin

sqrt:=x\*x; (\*buradaki sqrt fonksiyonun adıdır ve geriye bu isim değer gönderir\*)

End;

Ör: bu programda fonksiyon tanımlanmış ve ana program içinde kullanılmıştır.

Uses crt;

Var

Large,a,b:real;

Function max (bir, iki:real) : real; (\*Fonksiyon\*)

Begin (\*yukarıdaki satırda ilk real iki ve bir değişken isimlerini tanımlar, ikinci real ise fonksiyonun döndüreceği değerin tipini tanımlar.

İf bir > iki then

Max:=bir

Else

Max:=iki;

End;

Begin (\*Ana program\*)

Write(‘Birinci sayıyı giriniz=’); readln(a);

Write(‘İkinci sayıyı giriniz=’); readln(b);

Large:= max(a,b); (\*Fonksiyon çağrılıp a ve b değişkenleri fonksiyona gönderilip, sonuç maz ismi ile geri dönüyor ve sonuç large değişkenine aktarılıyor\*)

Writeln;

Writeln(‘Büyük sayı=’,large:8:3);

Readln;

End.

Yukarıdaki programda max fonksiyonu REAL tipi ile tanımlanmıştır. Ana programda a ve b değişkenlerine aktarılan sayılar, fonksiyonun bir ve iki parametrelerine aktarılır. Fonksiyonda bu iki sayının büyük olanı bulunur ve sonuç max fonksiyonuna atanır. Max fonksiyonundaki sonuçda ana programdaki large değişkenine gönderilir.

PROSEDÜRLER

Prosedürler fonksiyonlardan daha geniş kapsamlıdır. Bazı prosedürler ana programla hiç değer alışverişinde bulunmazlar, bazıları ana programdan değer alır fakat ana programa değer aktarmaz, bazıları ise birden fazla değer aktarırlar.

Fonksiyonlar programda kullanılmak üzere bir değer üretirler. Prosedürler ise bir veya birden fazla işlemi gerçekleştirerek program tarafından yapılan işin bir kısmını gerçekleştirirler. Bu şekilde çok çok uzun olacak programlar daha kısa hale gelmiş olur.

Bütün bunların dışında birde UNİT dediğimiz harici prosedürler vardır. Unit yazılarak ana program sayfası dışında bir kod sayfası yazılarak kütüphane oluşturulur ve bu unitleri biz her çeşit programda çalıştırabiliriz.

Ana program ile aynı metin içerisinde olan prosedürlere DAHİLİ PROSEDÜR, ana programın yazıldığı metinde yer almayıp, bağımsız olarak derlenerek, ana programda uses komutuyla programa dahil edilen prosedürlere ise HARİCİ PROSEDÜRLER denir. Unitler harici prosedürlerdir.

PROSEDÜR KURALLARI

Ana programda tanımlanan değişkenler, hem ana program tarafından hem de prosedürler tarafından kullanılabilirler.

prosedür içinde tanımlanan değişkenler sadece tanımlı olduğu prosedürlerde kullanılabilirler. Bu tür değişkenlere LOCAL değişkenler denir.

DAHİLİ PROSEDÜRLER

ÖR: Aşağıdaki programda toplama işlemi “topla” isimli bir dahili prosedürde yapılmaktadır. Bu programı önce Step over komutu ile çalıştırınız. Daha sonra defterinizde trace ediniz.

Uses crt;

Var

A,b,c:integer;

Procedure topla; (\* toplama yapan prosedür \*)

Begin

c:=a+b;

End;

Begin (\*Ana program \*)

Clrscr;

A:=5;

B:=3;

Topla;

Writeln(‘Birinci sayı=’,a);

Writeln(‘İkinci sayı =’, b);

Writeln(‘Toplam=’,c);

Readln;

End.

Bu programda a,b ve c değişkenleri her yerde kullanılabilir. Prosedür içinde de kullanılabilir. Çünkü ana programda tanımlanmıştır, böylelikle globaldir. “Topla;” komutu ile prosedür çalıştırılır. A ile b toplanır, c’ye aktarılır. Ve bu c sonucu ana programda kullanılır.

Ör: Bu programda iki prosedür kullanılmıştır. İkisinin işlevi de farklıdır.

Uses crt;

Var ch:char;

Procedure mesaj; (\* Ekrana mesaj yazan prosedür\*)

Begin

Clrscr;

Gotoxy(24,10); Write(‘AFYON GAZİ EML’);

Gotoxy(25,11);write(‘BİLGİSAYAR BÖLÜMÜ’);

Gotoxy(15,20);

write(‘Devam etmek için herhangi bir tuşa basınız…’);

ch:=readkey;

end;

Procedur fark; (\* Çıkarma işlemi yapan prosedür\*)

Var

A,b,c: integer;

Begin

Write(‘Birinci sayıyı giriniz=’);readln(a);

Write(‘İkinci syıyı giriniz=’);readln(b);

c.=a-b;

writeln(‘Bu sayıların farkı=’,c);

end;

Begin (\*Ana program \*)

Mesaj;

Clrscr;

Fark;

End.

Bu programda fark prosedüründeki a,b,c değişkenleri LOCAL değişkenlerdir ve sadece prosedüre aittirler. Prosedür dışında kullanılamazlar. Mesaj adlı prosedür bilgisayara bir tanıtım mesajı yazmakta, fark adlı prosedür ise çıkarma işlemi yapmaktadır. Prosedür isimleri ana program içinde komut gibi kullanılarak prosedürler çağrılmaktadır.

Ör: Aşağıdaki programın ekran çıktısını, RAM görüntüsünü yazınız.

Uses crt;

Var

Ad: string;

Procedure isimgir;

Begin

Write(‘İsminizi giriniz’);

Readln(ad);

End;

Procedure ekranayaz;

Begin

Write(‘Merhaba, benim adım ‘);

writeln(ad);

readln;

End;

Begin

İsimgir;

Ekranayaz;

End.

Ör: Aşağıdaki program klavyeden girilen kalp atış sayısına göre saatteki atış hızını bulur.

Uses crt;

Const

Dakika=60;

Var

Ats, toplam: integer;

Procedure giris;

Begin

Write(‘kalbinizin dakika atış sayısını giriniz=’);

Readln(ats);

End;

Procedure hesapla;

Begin

Toplam:=ats+dakika;

End;

Procedure ekrana yaz;

Begin

Writeln(‘Kalbinizin saatteki atış sayısı’,toplam);

End;

Begin

Giris;

Hesapla;

Ekranayaz;

End.

Aşağıdaki programda ana programdan gönderilen değerler, prosedür isminin yanındaki parantez içinde yer alan parametreler aracılığıyla prosedüre aktarılır.

Uses crt;

var

a,b:integer; (\*global değişkenler\*)

procedure toplam (x,y:integer);

var

z:integer;(\*local değişken\*)

begin

z:=x+y;

writeln(‘Toplam=’,z);

end;

begin (\*Ana program\*)

clrscr;

write(‘Birinci sayı=’);readln(a);

write(‘İkinci sayı=’);readln(b);

toplama(a,b);

end.

Bu programı step over komutu ile inceleyiniz. Tracesini yazınız.

Bu programda ana programdan girilen değerler prosedür isminin yanındaki parantez içindeki x ve y parametreleri aracılığıyla prosedüre aktarılır.ana programdan prosedüre aktarılan değerlerin aktarılmasına aracı olan parametrelere FORMAL parametreler denir (Geçici). Yukarıdaki programda prosedürün tanımlanması sırasında prosedür isminin yanındaki parantez içinde yer alan x ve y FORMAL parametrelerdir. Z ise prosedürün içinde tanımlandığı için sadece o prosedüre aittir ve LOCAL’dir.

Şu ana kadarincelediğimiz prosedürlere sadece ana programdan değer aktarımı oluyor ve işlemlerin hepsi prosedürde tamamlanıyordu. Bundan sonraki örneklerde prosedürden ana programa değer aktarımı yapan örnekleri inceleyeceksiniz.

Aşağıdaki programda prosedürde klavyeden sayıların girilmesi ve çarpılması sağlanıyor. Sonuç ise ana programa aktarılıyor.

Uses crt;

var

c: integer; ( \*Ana program tarafından kullanılan değişken\*)

procedure carp( var z: integer);

var

x,y:integer;

begin

write(‘Birinci sayıyı giriniz=’);readln(x);

write(‘İkinci sayıyı giriniz=’);readln(y);

z:=x\*y;

end;

begin

clrscr;

carp( c );

writeln(‘Bu sayıların çarpımı=’,c);

end.

Ör: Aşağıdaki programda prosedür tarafından üretilen string tipi bilgi ana programa aktarılmaktadır. Karşılıklı değer aktarımında kullanılan değişkenler aynı tipte olmalıdır. Bu programda ana program ile prosedür arasındaki değer aktarımında kullanılan değişkenler aynı tipte olmalıdır. Bu programda , ana program ile prosedür arasındaki değer aktarımında kullanılan ad ve dd değişkenlerinin her ikisi de string tipinde tanımlanmıştır. RAM , ekran çıktısı ve tacesi yapılacak.

Uses crt;

Var

Ad:string;

Procedure bilgi ( var dd:string);

Begin

dd:=’BİLGİSAYAR’;

end;

begin

ad:=’TUZLA’;

writeln(ad);

bilgi(ad);

writeln(ad);

end.

ARALIK 2

Temrin No 12: T. Pascal’da unit kavramı ve programcı tarafından unit oluşturulması

HARİCİ PROSEDÜRLER

Harici prosedürler, ana program ile aynı metinde yer almazlar. Bu prosedürler ayrı bir dosya olarak yazılır ve derlenirler. Harici prosedürlerin derlenmesi sonucunda diskette TPU uzantılı bir dosya oluşur. Harici prosedürler UNİT olarak da adlandırılırlar. Harici prosedürler herhangi bir programda kullanılmadan önce USES komutuyla programa dahil edilirler.programa dahil edilen harici prosedür, programın herhangi bir yerinde komut gibi kullanılabilirler. Harici prosedürlerde bilgi aktarımı yönünden tek yönlü ya da çift yönlü olabilirler.

Ör:

Unit toplam;

İnterface

Procedure topla (x, y :integer; var z:integer);

İmplementation

Procedure topla( x, y: integer; var z: integer);

Begin

Z:=x+y;

End;

Begin

End.

Bu prosedür, turbo editörde TOPLAM .PAS adı altında yapılır, diskete kaydedildikten sonra da derlenir. Derleme işleminden sonra diskte TOPLAM.TPU dosyası oluşur. Bu dosya herhangi bir programda USES bölümünde tanımlanarak programa dahil edilebilir. Daha

KASIM 3, ARALIK 1

Temrin No 10,11:T. Pascal programcı tanımlı procedure ve function uygulamaları

ARALIK 3

Temrin No 13: T. Pascal’da text tipli dosya uygulamaları

DOSYALAR

Diskette ya da hard diskte saklanan bilgisayar programlarının kaydedildiği dosyalara PROGRAM DOSYASI, programlar tarafından üretilen ve yine programlar tarafından kullanılan bilgilerin kaydedildiği dosyalara ise VERİ DOSYASI denir. Turbo Pascal’da 2 tip veri dosyası vardır. TEXT dosyalar ve RECORD tipi dosyalar.

TEXT DOSYALAR

Text dosyalarda bilgiler diskete sırayla kaydedilir ve yine sırayla okunur.

Text dosyaları ilk defa oluştururken REWRİTE modunda

Bilgi ekleme amacıyla önceden oluşturulmuş bir text dosyayı açarken APPEND(türkçesi ekle) modunda

Önceden oluşturulmuş text dosyayı bilgi okumak amacıyla açarken RESET modunda açılır.

*REWRİTE modu*

Bu mod kullanıldığında veri dosyası diskte ilk defa oluşturulur ve yazıcı kafa dosyanın en başına konumlanır. Daha önceden diskte oluşturulmuş bir dosyayı REWRİTE modunda açmaya kalkarsak yazıcı kafa bu dosyanın başına konumlanıp yeni bilgiler girildiğinde önceki bilgilerin üstüne yenileri yazılır, eski bilgiler silinir.

Dosyalar, üzerinde işlem yapıldıktan sonra kapatılırken dosyanın sonuna dosya sonu işareti konulur. Dosya sonu işaretini bir komut koyar. Dosya sonu işareti ekranda yazdırılamayan bir işarettir. Bu işaret EOF(End of File) değişkenine atanan boolean tipi bir bilgi ile kontrol edilir. Eğer dosya sonuna gelinmişse EOF değişkeni TRUE, dosya sonuna gelinmemişse FALSE değerini alır.

Text dosyalara kaydedilen bilgiler dosyalara ASCII karakterlerle kaydedilir. Bu nedenle TYPE isimli DOS komutunu kullanarak text dosyanın içindeki bilgiler görüntülenebilir. Text dosyalara bilgi yazarken veya bu dosyalardan bilgi okurken WRİTE,WRİTELN,READ,READLN komutları kullanılır.Text dosya isimlerinin uzantıları genelde DAT olur.

Text dosyalar RAM’de temsil edilmelidir. Text tipinde bir isim var bloğunda tanımlanır ve bu text dosyayı temsil eder.

Ör: aşağıdaki programda “ikirakam” isimli dosya Rewrite modunda açılıp, biri formatlı diğeri ise formatsız 565.5 sayısı kaydedilir.

Uses crt;

Var

dosya:Text;

{text tipinde “dosya” isminde dosyayı temsil eden bir değişken oluşturuldu ve ramde yer ayrıldı}

Begin

ASSIGN(dosya,’ikirakam’);

{“ikirakam” ismi dosya değişkenine atandı.”ikirakam” veri dosyasının diskteki ismidir.bu dosya programda “dosya” ismiyle temsil edilecektir.}

REWRİTE(dosya);

{dosya oluşturuluyor ve açılıyor}

WRİTELN(dosya, 565.5);

{bilgiler dosyaya yazılıyor}

WRİTELN(dosya, 565.5:10:0);

CLOSE(dosya)

{dosya kapanıyor}

WRİTELN(‘işlem tamam’);

Readln;

End.

Bu programı yazdıktan sonra DOS ortamında “ikirakam” isimli dosyanın oluştuğunu DIR komutu ile görün. “TYPE ikirakam” komutuyla da bu dosyanın içindeki bilgileri görün.

Soru : Klavyeden girilen 10 sayıyı RAKAM.DAT isimli, text tipli, yeni oluşturulacak veri dosyasına kaydeden ve bu dosya RAM’de dd değişken adıyla temsil eden programı yazınız.

*APPEND modu*

Dosya append modunda açıldığında yazıcı kafa dosyanın mevcut olan bilgilerin en altına konumlanır ve yeni bilgileri o noktadan itibaren yazmaya başlar. Böylece eski bilgilerde silinmemiş olur.

Ör: TELNO.DAT ismindeki veri dosyasına yeni bilgiler eklenen program

Uses crt;

Var

tn: Text;

ad: string\[10\];

soyad\[10\];

no:longint;

ch:char;

begin

ASSIGN(tn,’TELNO.DAT’);

APPEND(tn);

{dosya bilgi ekleme modunda açılıyor}

Clrscr;

Ch:=’e’;

While ch=’e’ do

Begin

Writeln;

write(‘ADI :’); readln(ad);

write(‘Soyadı :’);readln(soyad);

write(‘Telefonu :’);readln(no);

writeln(tn, ad,soyad,no);

{dosyaya yazıldı);

writeln;

write(‘Devammı?’);readln(ch);

end;

CLOSE(tn);

End.

Soru :Yukarıdaki programda bu dosyayı yeni oluşturacak olsaydınız hangi komutu nasıl değiştirirdiniz?

*RESET modu*

Bilgilerin okunması amacıyla dosya RESET modunda açılır.

Ör: bu program bir önceki örnekte oluşturulan TELNO.DAT isimli dosyadaki bilgileri listeler.

Uses crt;

Var

tn: Text;

ad: string\[10\];

soyad\[10\];

no:longint;

i:integer;

begin

ASSIGN(tn,’TELNO.DAT’);

RESET(tn); {dosya okuma modunda açılıyor}

Clrscr;

Writeln;

Writeln (‘ADI‘,’SOYADI‘,’TELEFONU ‘);

writeln(‘====’,’======’,’===========’);

while not EOF(tn) do

{dosya sonuna gelinmediği sürece döngüyü yap}

begin

readln(tn, ad, soyad, no);

{dosyadaki bilgiler okunuyor}

writeln(ad, soyad,no);

{okunan bilgiler ekrana yazılıyor}

end;

CLOSE(tn);

End.

---------------------------------------------------------------------------------------------------------------------

ARALIK4, ARALIK 5

Temrin No 14,15: T. Pascal’da record tipli dosya uygulamaları

RECORD TİPLİ DOSYALAR

Text tipi dosyalarda bir kayıta ulaşmak için ilk kayıttan itibaren istenilen kayda ulaşıncaya kadar bütün kayıtlar taranır. Bu olay uzun veri dosyaları için zaman kaybıdır. Record tipi dosyalarda ise her kaydın bir kayıt numarası bulunur. Bu kayıt numarası kullanılarak istenilen kayda doğrudan ulaşılabilir.

RECORD tipli dosyalarda, bir kaydı oluşturan bilgiler ortak bir kayıt değişkeni altında programın başlangıç bölümünde TYPE başlığı altında tanımlanır. TYPE başlığı altında programcı tarafından veri tipleri tanımlaması yapılır.

TYPE

Gunler=(Pazartesi,Salı,Çarşamba);

VAR

A:gunler;

Yukarıdaki tanımlamada önce “gunler” adlı veri tipi tanımlanmış ve Pazartesi, Salı, Çarşamba verileri aktarılmıştır. Daha sonrada VAR başlığı altında a değişkeni gunler tipinde tanımlanmış ve bu veriler a değişkenine aktarılmıştır.

Veri dosyalarına genellikle kişilere veya nesnelere ait bilgileri kaydederiz. Bu bilgiler bir bütün olarak düşünülmelidir. Örneğin bir kişinin adresi aşağıdaki elemanlardan oluşmaktadır:

Ev numarası

Sokak adı

Semt adı

Şehir adı

Record tipli dosyalarda bu mantıkla hareket edilerek bir kaydı oluşturan bilgiler, kayıt değişkeninin alt elemanları olarak tanımlanır. Tanımlama TYPE başlığı altında yapılır.

TYPE

Adres=record

Evno : integer;

Sokak : string;

Semt : string\[10\];

Şehir : string\[10\];

End;

Aynı gruptaki bir grup değişken bu şekilde ayrı ayrı tanımlandıktan sonra adres adlı yeni bir tip oluşur. Daha sonra, var bölümünde bir kayıt değişkeni bu yeni oluşturulan veri tipinde tanımlanır.

Var

Kay : Adres;

Dd: File of Adres;

Kay adlı kayıt değişkeni adres tipinde, “dd” adlı dosya değişkeni ise adres tipinde tanımlanmış olan bilgileri kaydedecek bir RECORD tipi dosya olarak tanımlandı.

RECORD tipli dosyalar ilk defa diskette oluşturulurken REWRİTE modunda açılır. Tekrar bilgi yazma ve okuma amacıyla RESET modunda açılır ve aynı modda değiştirilme yapılabilir. Record tipi dosyalarda kayıtlar disket üzerine 0’dan başlayan kayıt alanlarına yapılır.

Record tipi dosyalar yazma ya da bilgi okuma amacıyla açıldığında SEEK komutu kullanarak yazıcı veya okuyucu kafa istenilen kayıt alanına konumlandırılır.bundan sonra WRİTE ya da READ komutu kullanılabilir.

Ör: İSİM,ŞEHİR,NUMARA KAYIT PROGRAMI

Uses crt;

Type

Bilgi=record

No : integer;

Ad : string\[10\];

Soyad : string\[10\];

Sehir : string\[10\];

End;

Var

Ch: char;

Deg : bilgi;

Dosya File of bilgi;

Begin

ASSIGN(dosya,’OKUL.DAT’);

REWRİTE(dosya);

Ch:=’e’;

While ch<>’h’ do

Begin

Writeln;

Write(‘Numara =’); readln(deg.no);

Write(‘İsim=’);readln(deg.ad);

Write(‘Soyad=’);readln(deg.soyad);

Write(‘Şehir=’);readln(deg.sehir);

SEEK(dosya, deg.no); {yazıcı kafa kayıt alanına konumlanır}

Write(dosya, deg); {deg kayıtları dosyaya yazıldı}

Writeln;

Write(‘Devam etmek istiyormusunuz?’); readln(ch);

End;

Writeln;

Close(dosya);

End.

-----------------------------------------------------------------------------------------------------------------------------

OCAK 1

Temrin No 16: T. Pascal’da port kullanımı ve grafik programları uygulamaları

Temrin No 17: T. Pascal’da grafik programı uygulamaları

PORT KULLANIMI

Seri portlar COM1, COM2, COM3... olarak adlandırılır. Seri portlarda bilgi alışverişi bilgilerin peş peşe gönderilmesi suretiyle (yani seri olarak) yapılır. Yüksek hız gerektirmeyen uygulamalarda seri port kullanılır.

Paralel portlar ise LPT1, LPT2, LPT3... olarak adlandırılır. Paralel portlarda 1 byte’lık (yani 8 bit) bilgi aynı anda ayrı ayrı iletkenler aracılığıyla gönderilir. Yüksek hız gerektiren uygulamalarda paralel portlar kullanılır. Ayrıca paralel portun kullanımı daha pratiktir.

Bir bilgisayarda en az 1 seri 1 paralel port bulunur. Seri port en fazla 4, paralel port en fazla 3 tane olabilir.

LPT1 adlı paralel portun 25 ucu vardır. Bu pinlerin birer numarası vardır. 2,3,4,5,6,7,8,9 numaralı olanlar 8 bitlik bilgi alışverişinde kullanılırlar ve adresi 378’dir. Pascal programlama dilinde $378 olarak geçer

Ör:

Uses crt;

Var sayi: byte;

Procedure porta\_yolla;

Begin

ASM

MOV AB,sayi

MOV DX, 378H

OUT DX, AL

End;

Begin

Clrscr;

Write(‘Porta aktarılacak sayıyı giriniz: (0-255)’); readln(sayi);

Porta\_yolla;

Write(‘Şu anda paralel porta ‘, sayi, ‘değerini görmekteyiz’);

Readln;

End.

LINE KOMUTU

Line (x1,y1,x2,y2)

Ör: bu program ekrana çeşitli renklerde çizgiler çizer.

Uses crt, graph;

Var i,j:integer;

Begin

İ:=DETECT;

Clrscr;

İnitgraph(i,j,’ ’); {grafik moduna geçiliyor}

Setcolor (BLUE); {çizgi rengi tanımlanıyor}

Line(2,2,100,2);

Setcolor(GREEN);

Line(2,20,200,20);

Setcolor(RED);

Line(2,40,100,40);

Readln;

Closegraph;

End.

Aynı mantıkla RECTANGLE(x1,y1,x2,y2) komutu ekrana dikdörtgen çizer; CIRCLE( x, y, r) çember çizer, ELLIPSE(.x1,y1, başlangıç, bitiş, r1, r2) elips çizer.

Temrin No 18,19: T. Pascal’da proje çalışmaları

--------

Temrin No 20: Hesaplama tablosunun elemanları

Temrin No 21: Hesaplama tablosu uygulamaları

Temrin No 22, 23: Birbirine bağlı tablo-dosya uygulamaları

Temrin No 24: Birbirine bağlı tablo-dosya uygulamaları

Temrin No 25,26,27,28: Grafik Chart Window uygulamaları

Temrin No 29:Database uygulamaları

Temrin No 30,31: Database tablo uygulamaları

Temrin No 32: Database form dizaynı uygulamaları

Temrin No 33: Database sorgu uygulamaları

Temrin No 34: Database print uygulamaları

Temrin No 35,36,37: Database kullanarak proje çalışması uygulaması

x1,y1

x2, y2

---
*Kaynak: `PASCAL KODLARI VE ÖRNEK SORULAR/Odevsitesi_com_32608.doc` — MUJDEHANAIM — 2003*
