# Bilgisayar Kontrollü Kayan Yazi Devresi

Metin Gunduz www.sautef.8m.com

BILGISAYAR KONTROLLU KAYAN YAZI DEVRESI 1.Her Satir Icin Olusturulacak Kaydedici Devresi :

5v 5v Clk Vcc Q7 Q6 Q5 Q4 MR’ CP 7 4 1 6 4 A B Q0 Q1 Q2 Q3 Gnd Led Gosterge (On Direnc eklenecek) BG: Bilgi Girisi 1kΩ Ω

BG

Sekil 1. Her satir icin olusturulacak kaydedici devresi 2.Kayan Yazi Devresinin Baglantisi :

1.Satir Clk

BG

2.Satir Clk

BG

3.Satir Clk

BG

4.Satir Clk

BG

5.Satir Clk

BG

6.Satir Clk

BG

7.Satir Clk

BG

DO

D1

D2

D3

D4

D5

D6

D7

Bilgisayar Portuna 1kΩ Sekil 2. Kayan yazi devresinin baglantisi 3.Kullanilan Malzemeler Tablo 1. Devrede kullanilan elemanlar Adet Eleman Açiklamasi 7x1 74164 entegresi 8 bit kaymali kaydedici içerir.

8x1 1 kΩ direnç Bilgi Girisinde kullanilir.(Biri CLK’ da) 7x8 Led diyot Bilginin gozukmesi için 7x8 220Ω direnç Ledler için akim sinirlama direnci 1 D25 erkek konnektor Bilgisayarin paralel portuna baglamak için

1

Metin Gunduz www.sautef.8m.com

Tablo2. 74164 8 bit kaymali kaydedici entegresinin bacak baglantisi Pin Sembolu Açiklamasi 1-2 A,B Bilgi girisleri 8 CP Clock girisi (yukselen kenar tetiklemeli) 9 MR’ Master reset (Aktif sifir) girisi 14 Vcc +Vcc 5v (%10) 7 Gnd Toprak hatti 3-6 Q0 Q1 Q2 Q3 Çikislar (High 10 U.L.)

10-13 Q4 Q5 Q6 Q7 Çikislar (High 10 U.L.)

4.Devrenin Çalismasi ve Bilgisayara Montaji Devre yedi ayri kaymali kaydediciden olusur. Bu kaydedicilerin tetikleme girisleri birlestirilir ve paralel portun D 0 hattina baglanilir. Diger her bir kaydedici çikisi yukaridan asagiya dogru paralel portun D1-D7 çikislarina baglanir. Bu çikislar asagidaki sekilde gosterilmistir.

Bilgi girislerindeki ve tetikleme girisindeki dirençler gerilim dusumu olusturmak için kullanilir. Ayrica devre için kullanilan guç kaynaginin sasesi bilgisayarin guç kaynaginin sasesi ile birlestirilmelidir. Bunun için paralel portun yuvasinin metal aksami veya paralel portun topraga bagli olan 18-25 arasi terminalleri de kullanilabilir. D7 D6 D5 D4 D3 D2 D1 D0

25

18

Sekil 3. D25 tipi disi konnektor 5. Devrenin Bilgisayar ile Kontrolu Devreyi bilgisayardan kontrol etmek için sirayla su islemler yapilir.

- Devrenin baglandigi port adresi ogrenilir
- Port adresine gonderilecek veriler kolaylik olmasi bakimindan bir diziye aktarilir
- Bir dongu açilir
- Belirlenen porta ilk veri gonderilir.
- Tetikleme islemi için veriye bir eklenerek tekrar porta gonderilir.
- Devre her ne kadar hizli olsa da herhangi bir atlamaya karsi bir milisaniye kadar bu deger portta tutulur.
- Ilk veri tekrar porta gonderilir(tetiklemeyi dusurmek için)
- Kaymanin gozle gozukmesi için bir sure bekletilir (200-300 mili saniye kadar). Yoksa yazi çok hizla kayacaktir.
- Dongu geri çagrilir ve yeni degere geçilir.

Bu soylediklerimizi akis diyagramina aktarirsak;

2

Metin Gunduz www.sautef.8m.com

Basla Port, veri N=veriuzunlugu Bekle i = 1,1,N Portaaktar(veri( i )) Dur Portaaktar(veri( i )+1) Portaaktar(veri( i )) Sekil 4. Veri aktarimi akis diyagrami 6. Porta Gonderilecek Verilerin Hesaplanmasi Porta gondermek istedigimiz yazilarin kodlarini çozeriz. Bu islemi bir ornekle açiklayalim. Ornegin kaydediciye A harfini gondermek istiyoruz

- A harfinin haç su tun seklinde ledlere aktaracagimizi buluruz ve buldugum adet sutunlu ve yedi satirli bir tablo çizeriz. A harfi için 4 sutun yeterlidir.
- Bu tablo uzerinde hangi ledlerin yanacagini karalariz.
- En sol sutuna yukaridan asagiya dogru 2,4,8,16,32,64,128 yazariz ve bu degerlere karsilik gelen karali hucrelere bu degeri yazariz. Ve her sutun için bu degerleri toplariz.

2 2 2

4 4 4

8 8 8

16 16 16

32 32 32 32 32

64 64 64

128 128 128

252 34 34 252 Topl am

- Porta sira ile gonderilecek veriler 252,34,34,252 ‘dir.

3

Metin Gunduz www.sautef.8m.com

DIKKAT:

¸ Programlarda degisken olarak girilen port adresi desimaldir. Bunu ya bir fonksiyonla hexadesimale çevirmeli yada kullaniciya seçim sunulmalidir. Ornegin port 378 isimle anilan adres esasinda hexadesimaldir. Bunun desimal karsiligi 888’dir ¸ Eger devrenin sasesi bilgisayarin sasesi ile birlestirilmezse devre çalismaz ¸ Devrede veya harici guç kaynaginda meydana gelebilecek arizalar bilgisayarin ana kartina zarar verebilir. Bu yuzden guç kaynagi ozenle seçilmelidir.

¸ Devrenin aynisindan clocklar ortak olarak seri eklenerek sutun sayisi sonsuza kadar uzatilabilir. Bu programi etkilemez.

7. Pascal Program Ornegi

```pascal
Program Kayan_Yazi_Devresi;
Uses Crt,Dos;
Const Veri:Array[0..124] of Integer=(68,138,146,162, 68, 0,252, 18, 18, 18, 252,0,254,16,40,68,130,0, 252,18,18,18,252,0,254,18,50,82,140,0,6,8,240,8,6,0, 252,18,18,18,252,0,0,0,0,0,0,126,128,128,128,126,0, 254,4,8,16,254,0,130,254,130,0,14,48,192,48,14,0,254,146,146,146,13 0,0,254,18,50,82,140,0,68,138,146,162,68,0,130,254,130,0,2,2,254,2, 2,0,254,146,146,146,130,0,68,138,146,162,68,0,130,254,130,0,0,0,0,0 ,0,0,0,0,0,0,0,0);
Var Portadr,N,Sayac:Integer;
Begin
Clrscr;Sayac:=-1;
Write('Port Adresini Giriniz(normalde 888): ');
Readln(Portadr);
Writeln('Islemi Durdurmak Icin Bir Tus...');
Repeat
Sayac:=(Sayac+1) Mod 125;
Port[Portadr]:=Veri[Sayac];Delay(1);
Port[Portadr]:=Veri[Sayac]+1;Delay(1);
Port[Portadr]:=Veri[Sayac];Delay(1);
Delay(200);
Until(keypressed);
End.
```

Programin çalistirilinca kullanicidan port adresini ister. Adres girildikten sonra herhangi bir tusa basilincaya kadar devreye ‘SAKARYA UNIVERSITESI ’ bilgisini gonderir. Bu program sadece kuçuk bir ornektir. Programi çok daha fazla gelistirmek sizin elinizdedir.

4

Metin Gunduz www.sautef.8m.com

8. Borland Delphi Gorsel Program Ornegi Bu programda metin kutusuna girilen yazi Basla butonuna basilinca kaydirma cubuguyla secilen hizla paralel porta aktarilir.Programi www.sautef.8m.com adresinden indirebilirsiniz. 8.1. Programin Gorünümü Program Calistirildiginde Program Calisirken 8.2. Programin Kaynak Kodu

```pascal
unit Unit1;
interface
uses Dialogs, Windows, Messages, SysUtils, Classes, Graphics, Controls, Forms, Buttons, StdCtrls, ExtCtrls;
type TForm1 = class(TForm)
Edit1: TEdit;
Button1: TButton;
Bevel1: TBevel;
Bevel2: TBevel;
Timer1: TTimer;
Bevel3: TBevel;
ScrollBar1: TScrollBar;
Button2: TButton;
procedure ScrollBar1Change(Sender: TObject);
procedure dizile;
procedure Button1Click(Sender: TObject);
procedure Timer1Timer(Sender: TObject);
procedure FormActivate(Sender: TObject);
procedure Button2Click(Sender: TObject);
private { Private declarations }
public { Public declarations }
end;
```

5

Metin Gunduz www.sautef.8m.com

```pascal
const kardizi:array[1..189]of integer= (4, 0, 0, 0, 0,0,0, {Boºluk 32} 6, 252, 18, 18, 18, 252, 0, {A 64} 6, 130, 254, 146, 146, 108, 0,{B} 6, 124, 130, 130, 130, 68, 0, {C} 6, 130, 254, 130, 130, 124, 0,{D} 6, 254, 146, 146, 146, 130, 0,{E} 6, 254, 18, 18, 18, 2, 0 , {F} 6, 124, 130, 146, 146, 114, 0,{G 71} 6, 254, 16, 16, 16, 254, 0, {H} 4, 130, 254, 130, 0,0,0, {I} 5, 64, 128, 128, 126, 0,0, {J} 6, 254, 16, 40, 68, 130, 0, {K} 5, 254, 128, 128, 128, 0,0, {L} 6, 254, 4, 24, 4, 254, 0 , {M 77} 6, 254, 4, 8, 16, 254, 0 , {N} 6, 124, 130, 130, 130, 124, 0,{O} 5, 254, 18, 18, 12, 0,0, {P} 6, 124, 130, 162, 66, 188, 0, {Q} 6, 254, 18, 50, 82, 140, 0, {R} 6, 68, 138, 146, 162, 68, 0, {S 83} 6, 2, 2, 254, 2, 2, 0, {T} 6, 126, 128, 128, 128, 126, 0,{U} 6, 14, 48, 192, 48, 14, 0, {V} 6, 127, 128, 112, 128, 127, 0,{W} 6, 198, 40, 16, 40, 198, 0, {X} 6, 6, 8, 240, 8, 6, 0, {Y} 6, 194, 162, 146, 138, 134, 0);{Z 90}
var Form1: TForm1;
porta:array[1..1000]of integer;
sira,sayac:integer;
implementation
{$R *.DFM}
procedure TForm1.Button1Click(Sender: TObject);{Basla Butonu}
begin
if Button1.Caption ='Basla' then begin Button1.Caption :='Dur'; Edit1.Enabled := false; dizile; timer1.Enabled :=true; end else begin Edit1.Enabled := true; Button1.Caption :='Basla'; timer1.Enabled :=false;
end;
end;
procedure TForm1.FormActivate(Sender: TObject); {Acilis proseduru}
begin
sayac:=1;
end;
```

6

Metin Gunduz www.sautef.8m.com

```pascal
procedure TForm1.ScrollBar1Change(Sender: TObject); {Hiz Ayari}
begin
Timer1.Interval :=ScrollBar1.Position ;
end;
procedure tform1.dizile; {Verinin Diziye Aktarilmasi}
label sona;
var i,j,karakter:integer;
function ascbul(giren:string):integer;
var i,sonuc:integer;
begin
sonuc:=0;
for i:=1 to 100 do if char(i)=giren then sonuc:=i;
ascbul:=sonuc;
end;
begin
form1.Edit1.text:=uppercase(form1.edit1.text);sira:=0;
for i:=1 to length(form1.edit1.text) do begin karakter:=ascbul(copy(form1.edit1.Text ,i,1)); if karakter=32 then karakter:=64; if not((karakter>63) and (karakter<91)) then goto sona; for j:=1 to kardizi[(karakter-64)*7+1] do begin sira:=sira+1; porta[sira]:=kardizi[(karakter-64)*7+1+j]; end;{j'nin endi} sona:end; {i'nin endi}
end;
procedure TForm1.Timer1Timer(Sender: TObject); {Sistem Saati}
var dat,datarti:byte;
begin
dat:=porta[sayac]; datarti:=porta[sayac]+1;
asm mov dx,888 mov al,dat
out dx,al
mov al,datarti
out dx,al
mov al,dat
out dx,al
end;
sayac:=sayac+1; if sayac>sira then sayac:=1;
end;
end.
```

Metin Gunduz Sakarya Üniversitesi Elektronik & Bilgisayar Egitimi Bolumu www.sautef.8m.com mtngndz@hotmail.com icq: 63 092 219

7

---
*Kaynak: `BİLGİSAYAR KONTROLLÜ KAYAN YAZI DEVRESİ/BİLGİSAYAR KONTROLLÜ KAYAN YAZI DEVRESİ.pdf`*
