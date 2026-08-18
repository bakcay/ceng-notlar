# Pascal Programlama Dersinden Geçme Klavuzu

## Pascal Programlama Dersi’nden Geçme Kılavuzu

## Hazırlayan: Nur Nedim Okatan

## Soru 01: N adet sayıyı küçükten büyüğe sıralayan program

```pascal
{N adet sayıyı küçükten büyüğe sıralayan program}
Program kucuk_buyuk;
uses crt;
var
n, i, j, yedek :integer;
matris :array[1..100] of integer;
begin
clrscr;
write('Sıralanacak sayı adedini giriniz :');
readln(N);
for i:=1 to n do
begin
write(i);
write('. sayıyı giriniz :');
readln(matris[i]);
end;
for i:=1 to n-1 do
for j:=i+1 to n do
begin
if matris[i]>matris[j] then
begin
yedek :=matris[i];
matris[i]:=matris[j];
matris[j]:=yedek;
end;
end;
clrscr;
writeln('Küçükten büyüğe sıralama :');
for i:=1 to n do
writeln(matris[i]);
readkey;
end.
```

## Soru 02: N adet sayıyı büyükten küçüğe sıralayan program

```pascal
{N adet sayıyı büyükten küçüğe sıralayan program}
Program buyuk_kucuk;
uses crt;
var
n, i, j, yedek :integer;
matris :array[1..100] of integer;
begin
clrscr;
write('Sıralanacak sayı adedini giriniz :');
readln(N);
for i:=1 to n do
begin
write(i);
write('. sayıyı giriniz :');
readln(matris[i]);
end;
for i:=1 to n-1 do
for j:=i+1 to n do
begin
if matris[i]<matris[j] then
begin
yedek :=matris[i];
matris[i]:=matris[j];
matris[j]:=yedek;
end;
end;
clrscr;
writeln('Büyükten küçüğe sıralama :');
for i:=1 to n do
writeln(matris[i]);
readkey;
end.
```

## Soru 03: Altı haneli polindromik sayıları bulan program

```pascal
{Altı haneli polindromik sayıları bulan program}
program d6polindromik;
uses crt;
var
i:longint;
istr, a,b,c,d,e,f :string;
begin
clrscr;
writeln('Altı haneli polindromik sayıların listesi :');
for i:=100000 to 999999 do
begin
Str(i,istr);
a:= copy(istr, 1, 1);
b:= copy(istr, 2, 1);
c:= copy(istr, 3, 1);
d:= copy(istr, 4, 1);
e:= copy(istr, 5, 1);
f:= copy(istr, 6, 1);
if (a=f) and (b=e) and (c=d) then
write(' '+istr+' ');
end;
readkey;
end.
```

## Soru 04: N adet ismi alfabetik sıralayan program

```pascal
{Girilen N adet ismi alfabedik sıralayan program}
Program alfabedik;
uses crt;
var
n, i, j :integer;
matris :array[1..100] of string;
yedek :string;
begin
clrscr;
write('Alfabedik sıralanacak isim adedini giriniz :');
readln(N);
for i:=1 to n do
begin
write(i);
write('. ismi giriniz :');
readln(matris[i]);
end;
for i:=1 to n-1 do
for j:=i+1 to n do
begin
if matris[i]>matris[j] then
begin
yedek :=matris[i];
matris[i]:=matris[j];
matris[j]:=yedek;
end;
end;
clrscr;
writeln('İsimlerin alfabedik sırası :');
for i:=1 to n do
writeln(matris[i]);
readkey;
end.
```

## Soru 05: N adet sayının tek-çift kontrolünü yapan program

```pascal
{Girilen N adet sayının çift-tek kontrolünü yapan program}
program cift_tek;
uses crt;
var
n, i, cift, tek :integer;
matris: array [1..100] of integer;
begin
clrscr;
write('Girilecek sayı adedini giriniz :');
readln(n);
for i:= 1 to n do
begin
write(i,'. sayıyı girin :');
readln(matris[i]);
if (matris[i]/2) = int(matris[i]/2) then cift:=cift+1
else tek :=tek +1
end;
writeln('Çift sayıların adedi :',cift);
writeln('Tek sayıların adedi :',tek);
readkey;
end.
```

## Soru 06: Girilen mesajı tersten yazan program

```pascal
{Girilen mesajı tersten yazan program}
program ters_yazi;
uses crt;
var
mesaj, tersmesaj:string;
i, l:integer;
begin
clrscr;
write('Tersten yazılacak yazıyı giriniz :');
readln(mesaj);
l:=length(mesaj);
for i:= l downto 1 do
tersmesaj:=tersmesaj+copy(mesaj, i, 1);
writeln('Girilen yazının tersten yazılışı :');
write(tersmesaj);
readkey;
end.
```

## Soru 07: N adet öğrencinin kız-erkek kontrolünü yapan program

```pascal
{Girilen N adet öğrenciden kız ve erkek olanların sayısını bulan
program kiz_erkek_sayi;
uses crt;
label soru;
var
n, i, erkek, kiz:integer;
cinsiyet:char;
begin
clrscr;
write('Öğrenci sayısını giriniz :');
readln(n);
for i:=1 to n do
begin
soru: write(i,'. öğrencinin cinsiyeti (E/K) :');
cinsiyet:=readkey;
writeln(cinsiyet);
if (cinsiyet='E') or (cinsiyet='e') then erkek:=erkek+1;
if (cinsiyet='K') or (cinsiyet='k') then kiz :=kiz +1;
if (cinsiyet<>'K') and (cinsiyet<>'k') and
(cinsiyet<>'E') and (cinsiyet<>'e') then goto soru;
end;
writeln('Erkek öğrenci sayısı :',erkek);
write('Kız öğrenci sayısı :',kiz);
readkey;
end.
```

## Soru 08: Birden yüze kadar tek ve çift sayıların toplamlarını bulan program

```pascal
{1-100 arasındaki çift ve tek sayıların toplamlarını bulan program}
program te_cift_toplam;
uses crt;
var
i, cift, tek:integer;
begin
clrscr;
for i:=1 to 100 do
if (i/2)=int(i/2) then cift:=cift+i
else tek :=tek +i;
writeln('1-100 arası tek sayılar toplamı : ',tek);
writeln('1-100 arası çift sayılar toplamı: ',cift);
readkey;
end.
```

## Soru 09: N adet işçinin maaşlarının ortalamasını bulan program

```pascal
{N sayıda işçinin ücretlerini okuyup ortalamasını bulan program}
program isci_ortalama;
uses crt;
var
i, n :integer;
maas : array [1..100] of longint;
toplam :longint;
ortalama :real;
begin
clrscr;
write('İşçi sayısını giriniz :');
readln(n);
for i:=1 to n do
begin
write(i,'. işçinin ücretini giriniz :');
readln(maas[i]);
toplam:=toplam+maas[i];
end;
ortalama:=toplam/n;
write('İşçilerin maaş ortalaması :',ortalama:9:2);
readkey;
end.
```

## Soru 10: N adet işçinin net maaşlarını hesaplayan program

```pascal
{İşçilerin net ücretlerini hesaplayan program}
program net_ucret;
uses crt;
var
n, i:integer;
saatucreti :longint;
iscimesai, iscimaas:array [1..100] of real;
begin
clrscr;
write('İşçi sayısını giriniz :');
readln(n);
write('Saat ücretini giriniz :');
readln(saatucreti);
for i:=1 to n do
begin
write(i,'. işçinin mesai saatini giriniz :');
readln(iscimesai[i]);
iscimaas[i]:=iscimesai[i]*saatucreti;
iscimaas[i]:=iscimaas[i]-(iscimaas[i]*0.14);
iscimaas[i]:=iscimaas[i]-(iscimaas[i]*0.3);
end;
for i:=1 to n do
writeln(i,'. işçinin net ücreti :',iscimaas[i]:15:2);
readkey;
end.
```

## Soru 11: Üç yüz adet öğrencinin not ortalamasını bulan program

```pascal
{300 öğrencinin sınav ortalamasını bulan program}
program sinav_ortalama;
uses crt;
var
sinavnotu:array[1..300] of integer;
i:integer;
toplam:longint;
ortalama:real;
begin
clrscr;
for i:=1 to 300 do
begin
write(i,'. öğrencinin sınav notunu giriniz :');
readln(sinavnotu[i]);
toplam:=toplam+sinavnotu[i];
end;
ortalama:=toplam/300;
writeln('Öğrencilerin sınav ortalaması :',ortalama:3:2);
readkey;
end.
```

## Soru 12: Sigara anketi sonuç rapor programı

```pascal
{Sigara anketi sonuç programı}
program sigara_anket;
uses crt;
label
start;
var
isim :array [1..100] of string[20];
cinsiyet :array [1..100] of string[5];
yas :array [1..100] of string[2];
tercih :array [1..100] of char;
i, ii, ksayi :integer;
begin
clrscr;
write('Ankete katılan kişi sayısını giriniz :');
readln(ksayi);
clrscr;
for i:=1 to ksayi do
begin
writeln('Sıra No :',i);
write('Adı Soyadı :');
readln(isim[i]);
write('Cinsiyeti :');
readln(cinsiyet[i]);
write('Yaşı :');
readln(yas[i]);
write('Sigara Tercihi (0/1/2) :');
start:tercih[i]:=readkey;
if tercih[i]='0' then
writeln(' ',tercih[i],'- içmiyor ');
if tercih[i]='1' then
writeln(' ',tercih[i],'- az içiyor');
if tercih[i]='2' then
writeln(' ',tercih[i],'- tiryaki ');
if (tercih[i]<>'0') and (tercih[i]<>'1') and
(tercih[i]<>'2') then goto start;
writeln('-------------------------------------');
end;
clrscr;
for i:=1 to ksayi do
begin
gotoxy(1,1); write('Sıra No');
gotoxy(13,1); write('Adı Soyadı');
gotoxy(35,1); write('Cinsiyeti');
gotoxy(50,1); write('Yaşı');
gotoxy(60,1); write('Sigara Tercihi');
for ii:=1 to 70 do
begin
gotoxy(ii,2);
write('-');
end;
gotoxy(3 ,i+2); write(i);
gotoxy(13,i+2); write(isim[i]);
gotoxy(37,i+2); write(cinsiyet[i]);
gotoxy(51,i+2); write(yas[i]);
if tercih[i]='0' then
begin
gotoxy(59,i+2);
write(' ',tercih[i],'-İçmiyor');
end;
if tercih[i]='1' then
begin
gotoxy(59,i+2);
write(' ',tercih[i],'-Az İçiyor');
end;
if tercih[i]='2' then
begin
gotoxy(59,i+2);
write(' ',tercih[i],'-Tiryaki');
end;
end;
readkey;
end.
```

Soru 13 Hatalı satırı bulma sorusu olduğu için yazılmadı.

## Soru 14: Üç basamaklı ve rakamlarının küplerinin toplamı kendine eşit olan sayıları bulan program

```pascal
{Üç basamaklı ve rakamlarının küpleri toplamı kendine eşit} {olan sayıları bulan program}
program kuptop;
uses crt;
var
istr:string;
i, a, b, c, code, toplam:integer;
begin
clrscr;
for i:=100 to 999 do
begin
str(i,istr);
val(copy(istr,1,1),a,code);
val(copy(istr,2,1),b,code);
val(copy(istr,3,1),c,code);
toplam:= (a*a*a)+(b*b*b)+(c*c*c);
if toplam=i then writeln('Sayı bulundu: ',i);
end;
readkey;
end.
```

## Soru 15: Girilen sayının faktoriyelini alan program

```pascal
{Sayının faktöriyelini alan program}
program faktoriyelbul;
uses crt;
var
i, sayi:integer;
faktoriyel:real;
begin
clrscr;
write('Faktoriyeli alınacak sayıyı giriniz :');
readln(sayi);
faktoriyel:=1;
for i:=1 to sayi do faktoriyel:=faktoriyel*i;
write(sayi,' sayısının faktoriyeli:',faktoriyel:42:0);
readkey;
end.
```

## Soru 16: N adet sayıdan en büyüğünü bulan program

```pascal
{N adet sayının maksimumunu bulan program}
program maksbul;
uses crt;
var
matris:array [1..100] of integer;
n, i, j, yedek:integer;
begin
clrscr;
write('Girilecek sayı adedini giriniz :');
readln(n);
for i:=1 to n do
begin
write(i,'. sayıyı giriniz :');
readln(matris[i]);
end;
for i:=1 to n-1 do
for j:=i+1 to n do
begin
if matris[i]<matris[j] then
begin
yedek :=matris[i];
matris[i]:=matris[j];
matris[j]:=yedek;
end;
end;
write('Girilen sayıların en büyüğü :',matris[1]);
readkey;
end.
```

Soru 17: N adet sayıdan en küçüğünü bulan program,

```pascal
{N adet sayının minumumunu bulan program}
program minbul;
uses crt;
var
matris:array [1..100] of integer;
n, i, j, yedek:integer;
begin
clrscr;
write('Girilecek sayı adedini giriniz :');
readln(n);
for i:=1 to n do
begin
write(i,'. sayıyı giriniz :');
readln(matris[i]);
end;
for i:=1 to n-1 do
for j:=i+1 to n do
begin
if matris[i]>matris[j] then
begin
yedek :=matris[i];
matris[i]:=matris[j];
matris[j]:=yedek;
end;
end;
write('Girilen sayıların en küçüğü :',matris[1]);
readkey;
end.
```

## Soru 18: Döviz kurunu Türk Lira’sına çeviren program

```pascal
{Döviz kurunu TL'ye çeviren program}
program dovizcev;
uses crt;
var
kur,miktar,tl:longint;
begin
clrscr;
write('Döviz kurunu giriniz :');
readln(kur);
write('Döviz miktarını giriniz :');
readln(miktar);
tl:=kur*miktar;
write(miktar,' birim döviz karşılığı Türk Lirası :',tl);
readkey;
end.
```

## Soru 19: Birden ona kadar sayıların çarpım tablosunu üreten program

```pascal
{1den 10a kadar sayıların çarpım tablosu}
program carpim;
uses crt;
var
i,j:integer;
begin
clrscr;
for i:=1 to 10 do
begin
for j:=1 to 10 do writeln(i,'x',j,'=',i*j);
writeln('Devam etmek için Enter''a basın');
readkey;
end;
end.
```

## Soru 20: Girilen sayının asal olup olmadığını kontrol eden program

```pascal
{Girilen sayının asal olup olmadığını kontrol eden program}
program asalmi;
uses crt;
var
sayi,i,tam,onda:integer;
begin
clrscr;
write('Kontrol edilecek sayıyı giriniz :');
readln(sayi);
for i:=1 to sayi do
if (sayi/i)=int(sayi/i) then tam:=tam+1
else onda:=onda+1;
if tam>2 then writeln('Sayı asal değildir')
else writeln('Sayı asaldır');
readkey;
end.
```

## Soru 21: İki matrisi toplayan program

```pascal
{Girilen NxM ve ZxK matrislerini toplayan program}
program mat_top;
uses crt;
var
matris1,matris2,toplamatris:array[1..10,1..10] of integer;
x,y,i,j:integer;
begin
clrscr;
write('Toplanacak matrislerin boyutlarını giriniz(X,Y)');
readln(x,y);
for i:=1 to x do
for j:=1 to y do
begin
write('Birinci matrisin ',i,'-',j,' nolu hücresine
sayı girin :');
readln(matris1[i,j]);
end;
for i:=1 to x do
for j:=1 to y do
begin
write('İkinci matrisin ',i,'-',j,' nolu hücresine sayı
girin :');
readln(matris2[i,j]);
end;
for i:=1 to x do
for j:=1 to y do
begin
toplamatris[i,j]:=matris1[i,j]+matris2[i,j];
writeln('Toplam matris :', i, '-', j,
'. eleman :', toplamatris[i,j]);
end;
readkey;
end.
```

## “Soru 22: Matrislerin çarpımı” sorusu geçen sene çözülmediği için yazılmadı

## Soru 23: Beş adet vize ve finalin ortalamasını bulan program

```pascal
{Beş adet vize ve bir adet final notunun ortalamasını alan program}
program vize_final;
uses crt;
var
vize: array [1..5] of integer;
i,toplam,final:integer;
ortalama,toplam2,ortalama2:real;
begin
clrscr;
for i:=1 to 5 do
begin
write(I,'. vize notunu giriniz :');
readln(vize[i]);
toplam:=toplam+vize[i];
end;
ortalama:=toplam/5;
writeln('Vize ortalaması :',ortalama:3:2);
write('Final notunu giriniz :');
readln(final);
toplam2:=ortalama+final;
ortalama2:=toplam2/2;
write('Başarı notu :',ortalama2:3:2);
readkey;
end.
```

## Soru 24: Vergi iadesi hesaplayan program

```pascal
{Bir işçinin vergi iadesini hesaplayan program}
program vergi_iade;
uses crt;
var
maas,toplamfatura:longint;
iade:real;
begin
clrscr;
write('İşçinin maaşı :');
readln(maas);
write('Fatura toplamı :');
readln(toplamfatura);
if toplamfatura>maas then toplamfatura:=maas;
if (toplamfatura>0) and (toplamfatura<=30000) then
iade:=toplamfatura*0.2;
if (toplamfatura>30000) and (toplamfatura<=60000) then
iade:=30000*0.2+(toplamfatura-30000)*0.15;
if (toplamfatura>60000) and (toplamfatura<=100000) then
iade:=30000*0.2+30000*0.15+(toplamfatura-40000)*0.1;
if (toplamfatura>100000) then
iade:=30000*0.2+30000*0.15+40000*0.1+
(toplamfatura-10000)*0.05;
writeln('Toplam iade :',iade:12:2);
readkey;
end.
```

## Soru 25: İkinci dereceden denklemin köklerini bulan program

```pascal
{Ikinci dereceden denklemin köklerini bulan program}
program poli_kok;
uses crt;
var
a,b,c,delta:real;
begin
clrscr;
writeln('Denklemin katsayılarını giriniz ax² + bx + c = 0');
write('a = ');
readln(a);
write('b = ');
readln(b);
write('c = ');
readln(c);
delta:=((b*b)-(4*a*c));
if delta<0 then
write('Bu denklemin gerçek kökü yoktur.');
if delta=0 then
write('Bu denklemin bir adet gerçek kökü vardır :',
-B/(2*A));
if delta>0 then
begin
writeln('Bu denklemin iki adet gerçek kökü vardır :');
write(((-b+sqr(delta))/(2*a)):12:2,' ve ',((-b-
sqr(delta))/(2*A)):12:2);
end;
readkey;
end.
```

## Soru 26: Girilen cümledeki kelime sayısını culan program

```pascal
{Bir cümlede kaç adet kelime olduğunu bulan program}
program kelimesay;
uses crt;
var
cumle:string;
uzunluk,i,kelimesayi:integer;
begin
clrscr;
write('Cümleyi giriniz :');
readln(cumle);
uzunluk:=length(cumle);
for i:=1 to uzunluk do
if (cumle[i]=' ')and(cumle[i+1]<>' ') then
kelimesayi:=kelimesayi+1;
write('Cümledeki kelime sayısı :',kelimesayi+1);
readkey;
end.
```

## Soru 27: Girilen kelimede kaç adet “a” harfi olduğunu bulan program

```pascal
{Bir kelimede kaç "a" harfi olduğunu bulan program}
program asayisi;
uses crt;
var
kelime:string;
uzunluk,i,asayi:integer;
begin
clrscr;
write('Kelimeyi giriniz :');
readln(kelime);
uzunluk:=length(kelime);
for i:=1 to uzunluk do
if (kelime[i]='A')or(kelime[i]='a') then
asayi:=asayi+1;
write('Kelimedeki a harfi adedi :',asayi);
readkey;
end.
```

## Soru 28: N adet sayı içinde negatif, pozitif ve sıfırların sayısını bulan program

```pascal
{Girilen N sayi içinde pozitif negatif ve sıfır adedini bulan program}
program npsbul;
uses crt;
var
sayilar:array[1..100] of integer;
n,i,poz,neg,sif:integer;
begin
clrscr;
write('Girilecek sayı adedini giriniz :');
readln(n);
for i:=1 to n do
begin
write(I,'. Sayıyı giriniz :');
readln(sayilar[i]);
if sayilar[i] > 0 then poz:=poz+1;
if sayilar[i] = 0 then sif:=sif+1;
if sayilar[i] < 0 then neg:=neg+1;
end;
writeln('Pozitif sayı adedi :',poz);
writeln('Negatif sayı adedi :',neg);
writeln('Sıfır adedi :',sif);
readkey;
end.
```

## Soru 29: Kürenin hacmini bulan program

```pascal
{Kürenin hacmini bulan program}
program kup_hacim;
uses crt;
var
r:real;
begin
clrscr;
write('Kürenin yarıçapını giriniz :');
readln(r);
hacim:=4/3*pi*r*r*r;
writeln(r,'Yarıçaplı kürenin hacmi ',hacim,' dır.');
readln
end.
```

## Soru 30: Kürenin alanını bulan program

```pascal
{Kürenin alanını bulan program}
program kure_alan;
uses crt;
var
r,alan:real;
begin
clrscr;
write('Kürenin yarıçapını giriniz :');
readln(r);
alan:=4*((22 / 7)*(r*r));
write(r:12:4,' yarıçaplı kürenin alanı ',alan:12:4,' dır.');
readkey;
end.
```

---
*Kaynak: `PASCAL PROGRAMLAMA DERSİNDEN GEÇME KLAVUZU/PASCAL PROGRAMLAMA DERSİNDEN GEÇME KLAVUZU.doc` — OEM — 2004*
