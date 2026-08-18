# Assembler

Iste internette bircok sitede, formda gördügüm bu cümle. HAYIR Assembler ölmedi ve ölemezde! Assembler bugünde tipki yillar öncesindeki gibi önemli bir dil. Makine yakini hizli, kücük programlar üretmek icin en iyi dil. >> Neden Assembler? C/C++ da makine yakini, kücük ve gercekten hizli programlar üretebiliyor. << diyorsaniz ve eger yeni bir isletim sistemi veya sürücü yazmak istemiyorsaniz, hakli oldugunuzu itiraf etmeliyim. Ama bugun bile bazi yerlerde derleyicilerden daha iyi programlari optime etmek mümkün. Bunun disinda Assembler ile programlamak size bilgisayarla tam bir iletisim kurma imkani veriyor. Yani yazdiginiz her komut, bilgisayarin CPU(FPU komutlari haric) tarafindan direkt olarak calistiriliyor. Ilk bölümde daha önce Bilgisayar donanimi hakkinda yada CPU ve FPU hakkinda fazla bilgi sayibi olmayan insan lara bu donanim parcalari hakinda bilgi verecegim.

Her bilgisayar bir CPU ya sahiptir. CPU lar farkli bicimlerde olabilirler. Su an kullanilan CPU lar genelde iki bicimdelerdir. RISC ve CISC CPU lar. CISC 8086 tabanli islemcilerin kullandiklari komut modelidir. RISC komut destekli CPU lar ise genelde Server ve Workstation larda kullanilirlar. RISC az bir komut kapestesine ve az sapida adresleme modellerine sahiptir. Genelde her komut bir Takt da yapilir. Hatta bazi durumlarda bir Takt icinde bir kac islem yapmakta mümkündür. CISC CPU lar ise bir CPU ne kadar komut taniyorsa o kadar iyidir, felsefesi üzerine yapilirlar. Bazi komutlar 10 Takt bile gerektrebilirler. Ama yeni CISC CPU lari ile CISC ile RISC arasinda fazla bir fark kalmamistir. Cogu CISC CPU usu günümüzde CISC komutlarini kücük RISC komutlari haline getirip calistirabilme özelliginin yani sira 1 Takt da bir kac islem yapma özzelliginede sahiplerdir. Bunun disinda yeni bir islemci modeli olan EPIC (CISC ile RISC in karisimi) de intel tarafindan IA64 ile su anda pazara yerlestirilmeye calisiliyor. Ama genel bir CPU her sekilde registerlere, ve bir adresleme bicimine sahiptir.
CPU:
Datenbus

\----------------------------------
^....-REGISTERS-.-.............
|...............|..........-.................
|...............|.........-..................
|...............|........-...................
|...............|.......-....................
|...............|......-.....................
|...............|...- . . OP-Code.
---------ALU-------BR .. BZ
Flags...... |...........................
\----------------------------------
Adressbus

ALU bir islemcinin kalbidir denebilir. Islemler ALU icinde gerceklesir. Adressbus bize herhangibi bir alani adresleme olanagi verir. Datenbus üzerinden veri degis tokusu olur. Registerler bir islemcinin en önemli parcalaridirlar.Islemlerin yapilabilmesi icin ihtiyac duyulurlar, ve her hangibibir veri den cok daha hizli erisilebilirler. FPU ya gelince. FPU da CPU gibi kendi register lerini icerir ve kendi komut satiri vardir. Yüksek, komali vs. sayilarin hesaplanmasinda CPU dan cok daha hizlidir. 8486 dan beri FPU CPU un bir parcasi olarak bulunuyor. FPU ile programlamayi bu dökümanda ögrenmeyeceksiniz. Ama talep gelirse bu konu hakkindada bir döküman hazirlayabilirim.
Merhaba Dünya!

\--------------------------------------------------------------------------------
Bircok kitaptaki gibi bizde önce bir “Merhaba Dünya!” programiyla Assembler diline girelim. Derliyici olarak aksi söylenmedigi sürece TASM kullanilacaktir.(Zaten MASM ile TASM arasinda bir fark oldugu söylenemez)

.model small

.data
merhaba db ‘Merhaba Dunya!$’
.code

start:
mov ax, @data
mov ds, ax

mov ah, 0x09
lea dx, merhaba
int 0x021

mov ah, 0x04c
int 0x021

end start
ends

Aslinda ilk bakista fazla cana yakin bir dile benzemiyor Assembler, ama anlayinca gercektende kolay oldugunu anlayacaksiniz. Anlatmaya basliyorum;
Öncelikle “.model small” komutu ile programin programin bir CS(Code Segment) ve bir DS(Data Segment) e sahip olacagini söylüyoruz.SS(Stack Segment) ile DS ne yazikki ayni yeri paylasiyorlar. Daha sonra “.data” ile degiskenlerin saklanacaklari yeri belirliyoruz. DB(Define Byte) ile satirimizin Byte lar halinde saklanan bir degisken olmasini istedigimizi belirtiyoruz. “.code” ile CS e girdigimizi söylüyoruz. “mov ax, @data” ve “mov ds, ax” ile önce AX e DS nin baslangic adresini yükleyip sonrada DS in baslangic adresini AX den DS e yüklüyoruz. Bu cok önemli cünkü 8086 Segment ve Offset lerle adreslemeye izin veriyor. “mov ah, 0x09” ilea ax registerinin üst 8 Bittine 9 degerini yüklüyoruz. “int 0x21” ile bu DOS icin ds:dx adresindeki satiri yaz anlamina geliyor. Tabi adresin offset kismini dx e “lea” ile yüklüyoruz. Sonrada yine ah ye 0x04c yükleyerek int 0x21 i cagiriyoruz, buda DOS icin “Program bitti CIK!” demek oluyor. Simdi gelelim NE DEMEK Segment NE DEMEK Offset isine. 8086 islemcisi 20 Bitlik bir Adressbus a sayipti. Yani 1MB lik adresleme olanagina. Ama sadece 16 Bitlik registerleri vardi, bu yüzden INTEL aklina gelen süper(Ne kadar süper oldugu tartisilamaz tabi) bir fikri hayata sundu. Buna göre adresler söyle hesaplaniyordu: Adres= 16\*Segment+Offset Mesela havisada F6000 adresine ulasilmak istendiginde bu ister bu adresi F600:0000 olarak ister F000:6000 seklinde yazibilisiniz. Birinci kisimda Segment ikinci kisimda ise Offset in bulunmasi gerekiyor. Iste size 8086 nin registerleri:

8086:

ax ah al
bx bh bl
cx ch cl
dx dh dl

cs: ip
ds: di
es: si
fs
gs
ss: bp, sp

Flags

Aslinda 8086 nin gercektende az registere sahip oldugunu söyleyebiliriz. Ax, bx, cx, dx genel amacli registerlerdir. Cs, ds, es, fs, gs, ss adreslemede Segment kisminda kullanilabilir ip, di, si, bp ve sp ise offset kisminda kullanilabilirler. Bunun disinda her register 16- Bit boyutunda ve ax, bx, cx, dx registerleri üst ve alt kisimlari seklindede kullanmak bümkün. H üst 8 Bit L ise alt 8Bit icindir. Bu sekilde mesela ax registerine hem 6 hemde 4 degerini tutacak sekilde verebiliriz. Örnek:
mov ah, 6
mov al, 4
; iki degerde ax registerinin icinde bulunuyor.
Programcilar icin bir diger önemli gelisme ise 8386 ile gerceklesti. Bu islemci ilk IA32 destekli islemci olmakla beraber, kendi 32-Bitlik registerlerini sunuyordu. Hemde bu islemci üzerinde her registeri her islem icin kullanmak mümkün. Tabi CS ile EIP disinda. Cünkü CS:EIP programin o anda bulundugu durumu, yani bir sonraki komutun adresini tutar. Iste 8386 nin registerleri:

8386:

eax ax ah al
ebx bx bh bl
ecx cx ch cl
edx dx dh dl
cs
ds
es
fs
gs
ss
eip ip
edi di
esi si
ebp bp
esp sp
eflags

Önünde e harfi olan registerler 32 Bitlikler. Ve 8386 sayesinde artik adreslemek icin Segment lere ihtiyacimiz yok, 20 Bitlik adres kapestesi yerine 32- Bitlik bir adres kapestesi var 8386 nin, ve bu adresler tam bir registere sigiyorlar, yani 1MB lik adres kapestesi 4GB seviyesinde artik!

Eski(8086):
Merhaba db ‚Merhaba Dunya!’
lds di, merhaba
; merhaba nin adresi= ds:di

Simdi(8386)
Merhaba db ‘Merhaba Dunya!’
lea edi, merhaba
; merhabanin adresi= edi

Simdilik öncelikle en önemli Assembler komutlarini burda kisaca bir aciklayayim:
“mov register/segment/degisken, register/segment/degisken” virgülden önceki kisma, virgülden sonraki kismi yükler. Önemli olan ve dikkat edilmesi gereken en az bir tane registerin verilmis olmasi. Daha sonraki en önemli komutlar ise Matamatik komutlari. “add” toplama, “sub” cikarma “mul” carpma ve “div” bölme icindir.
Mesela deger1= deger2\*16;
Assembler:
mov ax, deger2
shl ax, 4
mov deger1, ax
Burada dikkatinizi ceken komut “shl” olabilir. Shl belirtelen sekilde bitlerin sola kaydirir, fakat capma islemlerindede kullanilabilirler, üstelik mul dan 4-5 kat daha hizli calisirlar. 1 degerinde kaydirmak 2 ile capmak, 2 degerinde kaydirmak 4 ile carpmak , vs seklinde devam eder. Tabi matamatik komutlarini “lea” ile gerceklestirmekte mümkün, tabi 8386 dan itibaren, nasilmi? 8386 da her registerle adresleyebildigimizi söylemistim, artik cs, sp gibi registerleri kullanmak zorunda degiliz. Bu yüzden, simdik su komutun ne yaptigina bir bakalim:
lea eax, \[eax+eax\*4\]
Bu komut eax e eax+eax\*4 ün icerigini yüklüyor. Ama bu eax ile 5 in carpimindan baska bir sey degil!
mov ecx, eax
shl eax, 2
add eax, ecx
Burda “lea” ile sadece 3 satiri 1 satir haline getirmekle kalmiyoruz ayni zamanda bir registerin kullaniminida engellemis oluyoruz. Bu kadar derinlere girdikten sonra simdik kaldigimiz yerden devam edelim. Ilk programda “merhaba db ‘Merhaba Dunya!$” satirinda dikkatinizi ‘$’ cekmisdir herhalde. Bu isaret Dos icin cok önemli, satirin sonunu belirtiyor. Windows da 0 ile satir sonu belli edilebiliyor. Simdik en basta yazdigimiz “Merhaba Dünya!” programini birde Windows icin yazalim;

Includelib import32.lib ;
Windows fonksiyonlari icin

.386
; 8386 nin registerlerine ve
;komutlarina ihtiyacimiz var!
.model flat, stdcall
; 32- Bit adresleme(4GB!)

extrn MessageBoxA : Proc
extrn ExitProcess : Proc

.data
Caption db „Merhaba Dunya!“,0
Text db “MERHABA!”, 0
.code
start:
push 64
push Caption
push Text
push 0
call MessageBoxA ; MsgBox göster
call ExitProcess ; cik
end start
ends
Yukaridaki programda push ile fonksiyonlara verileri gönderdik. Normalde push ladiginiz herseyi pop lamalisinizda, ama bu örnekte ExitProcess zaten bir degisken beklemedigi icin bu bir sorun yaratmiyor, neyse bu tek Windows programiydi bu kitap icerisindeki, daha fazlasi icin Windows API isini ögrenmeniz gerekiyor. Bunun disinda diger DOS programlarinda kullandigimiz “mov ax, @data”, “mov ds, ax” satirlarinida kullanmamiz gerekmiyor, cünkü adresle tek bir registere sigdiklari icin Segment lere ihtiyacimiz olmuyor.
Programlamaya kaldigimiz yerden devam edelim,
Size bir kac Tipp vereyim;
Carpma ve bölme islemleri icin shl ve shr yi kullanin.
Bir sayi 0 a esit olup olmadigini kontrol ederken cmp ax, 0 yerine test ax, ax i kullanin.
CMOVcc ve SETcc yi programlarinizda kullanin.
Bir sayiya 0 yüklemek isterken mov ax, 0 yerine xor ax, ax i kullanin. Bir sayiya bir eklerken inc bir cikarirken dec i kullanin.

Bir kac altin tipten sonra simdikte iki sayiyi toplayan, basit bir program yazalim;

sayi\_bir equ 0x18 ; 24
sayi\_iki equ 0x5 ; 5
sonuc equ ax

.model small
.stack 0x100 ; 256 Bytes yeter
.code
start:

mov ax, sayi\_bir
add ax, sayi\_iki

mov ah, 0x9
int 0x21
end start
ends

Bu programda sayi\_bir, sayi\_iki ve sonuc birer degisken degil sadece equ ile isimlendirilmislerdir. Daha önce C ile programladiysaniz EQU nun #define ile ayni oldugunu size söyleyebilirim. Bir diger önemli komut ise CMP komutudur. Degerleri karsilastirir ama kaydetmez bunun yerine Flag lari degistirir. Cmp nin kullanim sekli söyledir;
Örnek:
cmp ax, 2
Bu komuttan sonra cmp önce ax 2 ye essitmi diye bakar., esitse zero-flag (zf) doldurur, sonra da kücük büyük denemesi yapar. Kücük ise SF=OF büyük ise SF!=OF degerlerini gönderir.
Örnek:

.model small
.code
start:

cmp ax, 4
jge kucuk
jl buyuk
je esit
jmp son

kucuk:
inc ax
jmp son

buyuk:
dec ax
jmp son

esit:
add ax, ax

son:
mov ah, 0x09
int 0x21
end start
ends

Böylece degerleri karsilastirabiliriz. Üstekki program 8086 icin yazildi. Pentium Pro icin optime edildiginde söyle bir kod cikacaktir:
.686
.model small
.code
start:
cmp ax, 4
cmovge cx, 1
cmovl cx, -1
cmove cx, ax
add ax, cx
mov ah, 0x09
int 0x21
end start
ends

seklinde cok daha kisa, ve performans bakimindan cok daha yüksek bir program elde edecegiz, iste bu tip Optime olaylari bize Assembler ile gerceklestirilirken bütün diger dillerden daha cok kolaylik sagliyor bize. VC++ 6.0 hayla cmove, csete gibi komutlari desteklemiyor, yukaridaki kodu bir VC++ 7.0(.Net) derliyicisiyle elde etmeniz mümkün.
Kaldigimiz yerden devam edelim yukaridaki kod ne anlama geliyor; iste C/C++ veya Java bilenler icin:
if(ax<4) ax++;
else if(ax>4) ax--;
else if(ax==4) ax = ax\*2;
Yada herkesin anliyacagi bir bicimde:
Eger(ax 4den kücükse) ax i bir degerinde arttir.
Eger(ax 4den büyükse) ax i bir degerinde azalt.
Eger(ax 4 e esitse) ax i 2 ile carp.
Bunun disinda ziplama komutlari dilin en önemli yapi taslarini olusturmaktadirlar. Hicbir Flag a bakmazsizin ziplama JMP komutu ile yapilir. Daha sonra Jcc(cc yerine herhangibi harfler gelebilirler) seklinde belli flaglar doldurulduklarinda yada silindiklerinde sadece ziplama yapan komutlar vardir. Bir ziplama komutunu ister bir label in adini ister bir adresi yazarak kullanabilirsiniz. Simdi buraya kadar gördügümüz ziplama komutlarina bakalim:
JE = Eger ZF dolu ise ziplar.
JLE= Eger SF OF den farkli ise ziplar.
JGE= Eger SF OF ye esitse ziplar.
Bunun disinda simdi yeni baslayanlara birkac Tipp daha vereyim:
Mümkün oldugunca az ziplama komutlarini kullanin. Mümkün oldugunca az sekilde registerlerin alt, ve üst kisimlariyla ayri seklide calisin. Mesela ah ye 2 ve al ye 4 degerini yüklemek istediginizde:
mov ah, 2
mov al, 4
Yerine;
mov ax, 0x0204
yazarak programinizin icindeki bir islemin hizini 2 Kat daha hizli halledebilirsiniz.
Eger 8086 icin programlamak zorunda degilseniz CMOVcc, SETcc ve MMX i kullanmaktan kacinmayin.Degerleri DX:AX icine saklamak yerine 32- Bitlik registerleri kullanin. FPU yu kullandiktan(dagittiktan) sonra tekrar toplamayi unutmayin. Bu size ve diger programcilara yardim eder. Eger 32- Bit programliyorsaniz her registeri her is icin kullanmaktan kacinmayin. Ama Windows icin programliyorsaniz EBX, EDI, ESI ve EBP nin degerlerini degistirmeden önce yedeklemeniz gerekmekte. Bunu su sekilde yapabilirsiniz:
push ebp
push edi
push esi
push ebx
; Burada registerleri kullanabilirsiniz.
; ….
pop ebx
pop esi
pop edi
pop ebp

Burda gördügünüz gibi PUSH stack’a(Yada havisaya) deger itmek icin kullanilirken, POP da deger cekmek icin kullanilir. Neden ilk ebp nin itilipte en son cekildigine gelince: Biz dokunmadan önce bos bir havisa rutini (Stack):

BP
SP

Simdi önce iki degeri push liyalim.

push 3
push ds

Su anda Stack söyle gözüküyor:

BP
3
DS
SP

Eger bir degeri pop larsak stack in en basindaki elemani cekiyoruz demektir. Yani:

pop ax ; ax= 3
pop es ; es=ds

Ve bu komuttan sonra Stack yine su sekilde gözüküyor:

BP
SP

Unutmayin SP herzaman Stackin sonunu BP ise basini tutar. Ayni zamanda BP fonksiyonlarda elemanlara erismek icinde kullanilir. Aslinda fonksiyonlar bir cok sekilde yaratilma imkani sunarlar ki bunlardan bazilari su sekildedirler:
topla proc near
push ebp
mov ebp, esp
mov eax, \[ebp+4\]
add eax, \[ebp+8\]
leave
ret
endp

yada;

topla:
push ebp
mov ebp, esp
mov eax, \[ebp+4\]
add eax, \[ebp+8\]
pop bp
ret

yada;

topla:
mov eax, \[esp+4\]
add eax, \[esp+8\]
ret

En alttaki sekil size biraz yabanci gelebilir, cünkü derliyiciler tarafindan fazla kullanilmaz. Bunun disinda ebp+4 ün ikinci ebp+8 ise birinci deger oldugunu unutmayin. Bunun sebebi Stackin yukaridan asagi dogru gitmasidir.Yani esp+8, esp+4 den daha önce push ile itilmistir. Bu yüzden birinci degerdir. Ama C/C++ da ikinci deger! Cünkü C/C++ Stack a biraz baska bir acidan bakar ve ilk push ile itilen degeri en son, en sonda push lanan degeri ise ilk deger olarak görür. Bunun disinda söyle bir fonksiyonun yapisina bakildiginda:

topla proc near
push ebp
mov ebp, esp
mov eax, \[ebp+8\]
add eax, \[ebp+12\]
pop ebp
ret

Bu yukardaki fonksiyon C/C++ de su sekilde yazilabilir:
int topla(int sayi1, int sayi2)
{
return sayi1+sayi2;
}

Ama eger size gelen verinin icerigini degistirmek istiyorsaniz,
Java da;

public static
void topla(int sayi1, int sayi2)
{
sayi1+=sayi2;
}

Ilk bakista bu koddan yola cikarak asagidaki kodu yazarsak gercekten bir yanlis yapmis oluruz;
void topla(int sayi1, int sayi2)
{
sayi1+=sayi2;
}
C/C++ ile programlayanlar yukardaki kodun, size hicbirsey kazandirmadigini bilirler, bu ayni sekilde Assembler dilindede böyledir, eger toplama islemini bu sekilde yapmak istiyorsaniz, iki yolunuz var:

void topla(int \*sayi1, int sayi2)
{
\*sayi1+= sayi2;
}

yada C++ da;

void topla(int &sayi1, int sayi2)
{
sayi1+=sayi2;
}

ikiside ayni Assembler Kodunu yaratirlar;

topla proc near
push ebp
mov ebp, esp
mov eax, \[ebp+8\]
mov edx, \[ebp+12\]
add \[eax\], edx
pop ebp
ret

Burada ilk dikkatinizi ceken “add \[eax\], ecx” kod parcasi olmali, bu kod C/C++ da “\*eax+=ecx” ile aynidir. Yani size gelen degeri degistirmek yerine, size gelen degeri tasiyan degiskeni degistiriyoruz burda. Yani eger bir deger, yada register parantez icinde ise, o registerin icindeki deger degil, gösterdigi adresdeki deger önemli demektir. Dikkat edin yukardaki fonksiyonu su sekilde cagiramazsiniz;
push 12
push 6
call topla
Böyle bir kodda siz eax in icine 0x06 adresini yüklersiniz, ve programiniz bu yüzden hata cikartir. Cünkü “topla” fonksiyonu 0x06 adresindeki veriyi degistirmeye calisir. Böyle bir fonksiyon su sekilde kullanilir;

lea eax, degisken
push 12
push eax
call topla

Bu durumda fonksiyona degiskenin adresi gönderilir(°isken) ve fonksiyonda bu degeri degistirmesi beklenir.Degisken icin tanimladigimiz bir degisken, yada Stack dan bir degisken koyabiliriz. Bunun disinda Assembler dilinde bir döngü yapmak icinde bir kac yöntem bulunmakta, iste iki temel döngü sekli:

dongu:
cmp ax, cx
je devam\_et
dec cx
jne dongu

devam\_et :
;...
Yukaridaki kod C/C+ da;
while(cx!=ax) cx--;
Seklinde yazilabilir. Bu cx, ax e esit olmadigi sürece cx den bir cikar anlamina geliyor. Ama bir dongunun cx sifir olana kadar devam etmesini isterseniz;
while(cx!=0) cx--;
Seklinde bir kod parcasina derleyici size baska bir kod parcasi gösterecektir;
dongu:
loop dongu
; …
Seklinde olacaktir kodunuz. „loop“ komuttu cx sifir oalana kadar donguyu devam ettirir, her seferinde cx den bir cikarir. Mesela;
while(cx!=0) { ax++; cx-- }
su sekilde derlenir;
dongu:
inc ax
loop dongu
; …
Tabikki derliyicinizin yukaridaki koddan daha degisik bir kod da vermesi dogal olacaktir, nede olsa C/C++ da registerlerle degil, degiskenlerle ugrasir programci, eger derleyici yeterli bir optime islemi yapmayi basarirsa elinize yukardaki kod gecer. Son olarakta SETcc hakkinda kücük bir kod örnegi yazayim ;
mov ax, 0x00FF
mov dx, 0xFF00
; dx :ax= 0xFF0000FF
add ax, 0xFF00
setc dl

Yukaridaki kod ne yapar? DX:AX in icine 32- Bitlik bir sayi yazar, daha sonra bu sayinin alt 16- Bittini 0xFF00 ile toplar. Eger sonuc sigmazsa dl nin icine 0x01 degerini yükler, böylece toplama islemi sorunsuzca gerceklesmis olur.
Not: Yukaridaki kod sonuc bilindigi icin yazildi, eger böyle bir koda programinizda ihtiyac duyuyorsaniz, asadaki sekilde yazin:
add ax, 0xFF00
adc dx, 0
Böylelikle isinizi riske atmamis olursunuz ;)

Tabikki Setcc nin gücünü gösteren Örnek bir kodda yazmak mümkün, mesela asadakki gibi cok fazla kosulun oldugu program parcasinda, C++:

if(r1==r2) r1++;
else if(r2==r1) r2++;
else r1=r2;
if(r1==r2) r1--;
if(r2==r1) r2--;
else if(r2==(r1-1)) r3=r2;
else r2=r3;

Assembler x86:
if0:
Cmp ax, bx
Jne else\_if0
Inc ax
Jmp if1
else\_if0:
Cmp bx, ax
Jne else0
Inc bx
Jmp if1
else0:
Mov ax, bx
if1:
Cmp r1, r2
Jne if2
Dec ax
if2:
Cmp bx, ax
Jne else\_if1
Dec bx
else\_if1:
Mov cx, bx
Dec cx
Cmp ax, cx
Jne else1
Mov cx, bx
Jmp cnt
else1:
Mov bx, cx
cnt:
;...

Burda Cmov ve Set komutlarini kullanarak yüksek bir seviyede performans elde ediyoruz, cünkü sadece 4 kere zipliyoruz. Yukarida ise 8 kere.

xor ecx, ecx

cmp eax, edx
jne else\_if1
inc eax
jmp if\_1
else\_if1:
cmp edx, eax
sete cl
cmovne eax, edx
add eax, ecx
if\_1:
cmp eax, edx
sete cl
sub eax, ecx
cmp edx, eax
jne else\_if2
dec edx
jmp end\_if
else\_if2:
mov ecx, eax
dec ecx
cmp edx, ecx
xor ecx, ecx
cmove ecx, edx
cmovne edx, ecx
end\_if:
Yukaridaki Cmov ve Set ile yazilmis olan kod x86 icin yazilmis koddan cok daha hizli(Tabikki Pentium Pro icin), ziplama komutlari kullanilmadigi icin, islemcinin bir sonraki komutu tespit etme imkani daha yüksek. Bunun disinda ziplama olmadigi icin koddaki CS:EIP register ciftlerinin icerigide degistirilmiyor. Unutmayin Set komutu 8386 dan Cmov komutu ise Pentium Pro dan itibaren gecirlidir.
Eger Assembler i ögrenmek istiyorsaniz, BIOS int. lerini ögrenmelisiniz. Ama eger Dos icin program yapmak(yazmak) istiyorsaniz Dos cagrilarini, Windows icin program yapmak(yazmak) istiyorsaniz Windows API isini ögrenmelisiniz. Ama BIOS int. lerini kesinlikle ögrenmeniz gerekmekte, bunlar size er yada gec lazim olacaktirlar.(Meselaa bir isletim sistemi yazmak istediginizde!)
Yüksek sayilarla calismak

\--------------------------------------------------------------------------------
Bir cok dilde 64-Bitlik veri tiplerine raslamak dogal, oysa x86 islemcilerinin 64 Bitlik registerleri bulunmuyor, peki nasil oluyor bu? Öncelikle ilk akla gelen cevap 64-Bit lik bir sayinin 32 Bitinin bir resistere, diger 32 Bittin baska baska bir resistere yüklenmesi. Bu VC++ deki \_\_int64 ile tanimlanabilen veri türü ile ayni islemin yapilmasi anlamina geliyor. Mesela:
mov eax, 0x00ffff00
mov edx, 0x000000ff
Seklinde 0x000000ff00ffff00
(1095233437440) sayisini eax:edx in icine kaydediyoruz. Mesela basit bir toplama islemini su sekilde yapiyoruz,
add eax, eax
adc edx, edx
Burda 1095233437440 sayisini kendisi ile topladik(yada iki ile carptik). Adc komutu add dan farkli olarak önce sayiyi topluyor sonrada üstüne CF in degerini ekliyor. Akla gelen ikinci yöntem ise FPU, bu sayede C/C++ da double adi verilen sayilarla carisma olanagimiz oluyor. 3 üncü ve en iyi tekniklerden biride MMX. MMX 8 tane 64-Bitlik register le geliyor.(MM0…MM7) Ama bu registerler yeni degiller, aksine eski 80-Bitlik FPU registerlerini(ST0…ST7) kullaniyorlar. Ama yaninda bu sayilari islemek icin bircok yeni komutla beraber geliyor MMX, ve bu sekilde sadece bir register icinde bir sayi ile calismak zorunda degiliz. Herhangibir registerin icine 8 tane sayi koyup, 8 ile ayni anda calismamiz bile mümkün. Ama yinede MMX inde eksikleri var, ama bunlar 3Dnow! SSE ve SSE2 ile ortadan kalkmis durumdalar. Yinede size su anda MMX ile calismanizi tavsiye ederim, cünkü hem 3DNow, hem SSE hemde SSE2 MMX i destekliyorlar. Ama su anda SSE2 sadece Pentium 4 tarafindan destekleniyor. TIP: Sayilarin hesaplanmasinda Windows un hesap makinesi, gelismis bölümünü kullanabilirsiniz. Gercektende cok faydali, hem hex, hem binary hemde normal sayilarin hesaplanmasinda.
DOS ve Windows
Ilk programlamaya basliyanlar icin kusursuz bir ögrenim ortami olusturan DOS ayni zamanda bazi isleri gercektende zorlastiriyor. Mesela dosda sayilari ekrana yazmak icin ASCII formatina cevirmeniz gerekiyor ki, bu bir sayinin her basamaginin tek tek cevrilmesi anlamina geliyor. DOS icat edildigi siralarda 8086 bulundugundan dolayi sadece 1MB lik adresleme kapastesine sahip DOS, ve bu DOS un en son sürümü 6.0 ile bile bugün öyle. Bunun disinda Windows 3.x de 16-Bitlik bir isletim sistemi ama 16MB lik adresleme destegi var. Yani Windows 3.x de adresler 8286 ya göre hesaplaniyorlar:
DOS(8086)
adreslemesi=16\*Segment+Offset
Windows 3x(8286)
adreslemesi=256\*Segment+Offset
Bunun disinda Windows 3.x su anki Windows versiyonlarina göre cok daha farkli bir coklu-kanal programlama teknigi kullaniyor. Buna göre sadece o an secili olan program calisiyor, diger kanallar arkada beklemede kaliyorlar. TSS 16-Bitlik ve cok kanalli programlama mantigi cok basit bir sekilde calisiyor Windows 3.x de. Buna göre TSS 44 Bytes büyüklügünde. Windows 95 ile gelen coklu kanal sisteminde ise her program belli bir aralikla calistiriliyor. Kanallar degistirilirken(Yani sira diger programa geldiginde) TSS(Task Switch Segment) ye programin her registeri ve Flaglari yüklüyor. 32-Bit TSS 104 Bytes büyüklügünde. Windows EDI, ESI, EBX ve EBP registerlerini kullaniyor ve bu degerleri degistirmemenizi bekliyor. Bu yüzden bu registerler kullanilmadan önce yedeklemeniz gerekiyor, aksi halde sistemi cöktürebilirsiniz. Hernekadar 8386 da 4GB gibi bir bellek alani gösterilebilsede, Windows altinda bu sadece 2GB büyüklügünde. Geri kalan 2GB Windows tarafindan ayrilmis, ve kullanimi yasak olarak duruyor. Coklu kanallilik olunca her programin adresleme kismida Windows a yükleniyor. Yani programlarin biribirlerinin degiskenlerini göstermemeleri, vs. Kisimlarida Windows hallediyor. Windows XP ise gercek bir 32-Bit isletim sistemi olma özelligi ile geliyor. Bundan önceki Windows serisi Dos üzerinde aciliyordu, ve daha sonra 32-Bit moda geciyorlardi. Bu yüzden aslinda Windows 9x serisininde 16/32-Bit bir isletim sistemi oldugu söylenebilir. 32-Bit Moda sizde programlariniz icinde DOS dan gecebilirsiniz, bunun icin programiniza su kücük satiri eklemeniz yeterli:
push cr0
; Daha sonra Real-Mode geri dönmek icin.
smsw ax
or ax,0x01 ; Protected –Mode
lmsw ax
; ...
pop cr0
; Geri Real-Mode dayiz simdik

Her ne kadar bir programin icinde Mode degistirmek fazla gerekli bir durum olmasada, burda kisa bir aciklamada bulunayim dedim. SMSW ile CR0 registerinin ilk 16-Bit tini ax e kaydedip, 1 inci biti degistererek Protected mode girmek icin gerekli degeri ax e yüklüyoruz. Daha sonrada LMSW ile ax i CR0 registerine yazarak Protected Mode geciyoruz.
Protected Mode: Windows 9x ve yeni sürümlerinin kullandigi, isletim sistemi Mode u. Bu mod un özelligi degisik programlarin birbirilerine zarar vermelerini engelleyebilmesi. Real- Mode: 8086 ile beraber gelen isletim sistemi Mode u. Pogramlamayi ögrenmek icin kusursuz bir ortam bence. Virtual 8086 Mode: Protected Mode altinda baslatilan fakat 8086 icin yazilmis programlarin calistiklari Mode.

CPUID

Pentium ile birlikte, programinizin üstünde calistigi islemci hakkinda bilgi alabilecegi bir komut geldi, CPUID. CPUID eax registerinin icinde bir fonksiyon numarasi bekler, böylelikle hangi bilgileri göndermesi gerektigini anlar. Bu bilgiler EDX icinde geri dönerler. Daha sonra TEST komutu ile geri dönen bilgilerde istenilen özelligin olup olmadigi anlasilabilir.
Mesela:
mov eax, 0x01
cpuid eax
test edx, 0x0800000
;(23 uncu bit dolu ise MMX vardir.) jnz mmx\_var

EKLER
ADC
\----------------------------------------
add with carry
ADC O1, O2

ADC iki elemani(O1 ve O2) toplar ve bu sonuca Carry Flags sida ekler.

Örnek:
stc
mov al, 3
mov ah, 2
adc al, ah ; al= ah+al+cf=6

ADD
\--------------------------------------
ADD O1, O2
ADD O1 ile O2 yi toplayip O1 in icine yazar.
Tip:
Eger bir registere 1 eklemek
istiyorsaniz INC i kullanin.
DIV
\----------------------------------------
division
DIV O1
Bu komut bölme icindir. Eger O1 8 Bit ise AX deki sayi bölünür, kalan AH nin icine ve sonuc AL nin icine yazilir.

Eger O1 16 Bit ise DX:AX icindeki sayi bölünür, kalan DX in icne sonuc AX in icine yazilir. Eger O1 32- Bit ise EDX:EAX deki sayi bölünür, kalan EDX e sonuc EAX e yazilir.
Tip:
Eger bir sayiyi 2 nin katlarina bölmek istiyorsaniz;
SHR komutunu kullanabilirsiniz.
mov ax, 24
mov bl, 8
div bl
yerine;
mov ax, 24
shr ax, 3 (2 üstü 3)
yazarsaniz kodun boyu ve hizi degisecektir.

IDIV
\---------------------------------------
interger division
IDIV O1
Bo komut DIV ile hemen hemen aynidir, fark olarak isaretli sayilarlada islem yapabilir.
IMUL
\---------------------------------------
interger multiply
IMUL O1, \[O2, \[O3\]\]
IMUL iki virgüllü sayiyi carpar.
Ilk olarak eger iki tane adress yada register le kullanirsaniz;
Örnek:
IMUL ax, dx
sonuc ax= ax\*dx
Eger ama 3 tane adress yada register kullanirsaniz; Örnek: IMUL ax, dx, cx O zaman ax= dx\*cx seklindedir.

MUL
\---------------------------------------
multiply
MUL O1
MUL O1 i Akkumulator(AH, AL, AX, EAX) ile carpar.
Tip:
Eger bir sayiyi 2 nin katlariyla carpacaksaniz:
mov al, 5
mov bl, 4
mul bl
yerine;
mov al, 5
shl al, 2
seklinde yazarsaniz programinizin boyutunu ve hizini degistirmis olursunuz.

SBB
\---------------------------------------
subtraction with borrow SBB O1, O2 SBB O2 ile Carry- Flag i toplayip sonuctan O1 i cikarir.

SUB
\---------------------------------------
subtract
SUB O1, O2
O2 yi O1 den cikarir ve sonucu O1 e yazar.
Tip:
Bir sayidan 1 cikarmak istiyorsaniz,
Örnek:
sub ax, 1
yerine:
dec ax
yazmaniz kodunuzun boyunu ve hizini degisterecektir.

XADD
\---------------------------------------
exchange and add
XADD O1, O2
XADD iki elemanin önce iceriklerini degistirir sonrada ADD komutunun yaptigini yapar.
Örnek:
mov al, 3
mob bl, 5
xadd al, bl ; Al= 8, Bl=3

KARSILASTIRMA KOMUTLARI

CMP
Compare
CMP birinci ile ikinci girilen degerleri karsilastirir ve sonucu FLAG lara yazar.
Örnek:
mov ax, 2
cmp ax, 2 ; ZF=1
CMPXCHG
Compare and exchange
Cmpxchg komutu kendisine gelen ilk degeri al, ax veya eax ile(Kendisine gelen ilk degeri boyutuna göre) karsilastirir. Eger degerler esitseler kendisine gelen ilk degere ikinci degeri yükler ve ZF ki doldurur. Örnek:
mov eax, 3
mov edx, 3
lea ecx, \[eax+edx\*8\]
cmpxchg edx, ecx ; edx= ecx
Bunun disinda cmpxchg8b ile 64-Bit lik sayilar üstündede bu islemi yapabilirsiniz. Yalniz cmpxchg8b biraz daha degisik calisiyor, sadece bir tane adres gelmesini bekliyor kendisine, daha sonrada bu adresteki degeri EDX:EAX icindeki deger ile karsilastiriyor. Eger esitlerse ECX:EBX icindeki degeri bu adrese yaziyor.
Örnek:
Cmpxchg8b qword ptr\[ebp\]
TEST
Test
Test kendisine gelen degeri, ile kendisine gelen ikinci deger arasinda bir “and” islemi yapar. Ama sonucu and komuttundaki gibi kaydetmek yerine sadece FLAG lari degistirir.
FONKSIYON KOMUTLARI:

CALL
Call bir fonksiyonu cagirmak icin kullanilir. Eger bir near-call yapilirsa sadece o anki programin eip(ip) registeri yedeklenir, böylece fonksiyon bittikten sonra programda kalinan yerden devam edilebilir. Eger bir far call yapilirsa hem cs hemde eip(ip) yedeklenir.
INT
Interrupt
Int kendisine gelen 8-Bitlik(0 ile 255 arasinda sayilar) adresdeki aliciyi cagirir.
Örnek:
int 0x21 ; Dos interrupt unu cagirma.
Bunun disinda birde into vardir. Bu komut ise eger OF=1 ise bir int islemi gerceklestirir. Ama bir deger göndermeniz gerekmemektedir, otomatik olarak interrupt 0x04 ü cagirir.
RET
Ret Call ile cagrilan bir fonksiyondan tekrar dönmek icin kullanilir. Eger bir near call yapilmissa eip yi tekrar eski haline getirir. Eger bir far call yapilmissa hem cs yi hemde eip yi eski haline getirir.

MANTIKSAL OPERATORLER

Assembler
C/C++/Java

And
&&

Not !

Or
||

Xor
^

Shl
<<

Shr
>>

REGISTER KOMUTLARI

BSWAP
\---------------------------------------
byte swap
BSWAP O1
BSWAP O1 yerinde 32 Bit lik bir register bekler. 0 .ile 4. üncü byte'i ve 2. ile 3. yü degistirir. Örnek:
mov eax, 11223344h
BSWAP EAX ; EAX= 44332211h

CBW
\---------------------------------------
convert byte to word CBW AL- registeri icinde bulunan seyi, bir Word seklinde AX e yazar.

CDQ
\---------------------------------------
convert word to quadword CDQ EAX icindeki doubleword 'u EDX:EAX icine quadword olarak yazar.

CWD
\---------------------------------------
convert word to doubleword CWD AX icinde bulunan word' u DX:AX e doubleword olarak yazar.

CWDE
\---------------------------------------
convert word to doubleword extended CWDE AX icindeki word'u EAX 'E doubleword olarak yazar.
LEA
\---------------------------------------
load effective address
LEA O1, O2
LEA O2 nin adresini O1 e yazar. O1 16 yada 32 Bit lik bir register olabilir. Örnek:
lea dx, deger
mov dx, offset deger
; Bu ikisi ayni isi yapar
LMSW
\---------------------------------------
load machine status word
LMSW O1
O1 e CR0 registerinin ilk 16 bitini yazar(32 Protected Mode gecmeye yariyon kisimda ordadir) Ne yazikki real mode da bu gecirli degil, o yüzden mov O1, cr0 yazmaniz gerekebilir.
Bu komut aslinda isletim sistemi icindir, ve normal bir programda kullanilmasi gerekli degildir.

MOV
\---------------------------------------
move
MOV O1, O2
Assembler dilinin en önemli komutudur. O1 e O2 yi tasir, önemli olan her iki Ox nun esit olmasidir. Ikinci kural ise ikisininde Segmentregister olmamasidir. 16 bitlik bir registeri 32 bit lik bir registerin icine kopyaladiginiz zaman Pentium Pro dan itibaren 0 ile diger bitler doldurulur. Önceki islemcilerde karisik bitlerle dolduruluyorlardi. Tip: xor ax, ax ; mov ax, 0 push ds ; mov ax, ds pop es ; mov es, ax

MOVSX
\---------------------------------------
move with sign- extension MOVSX O1, O2 MOVSX o1 in icine o2 yi kopyalar, burdaki fark ise o1 in 16 yada 32 bit olup o2 nin 8 veya 16 bit olabilmesidir. Örnek: mov ax, 0 mov bl, -5 movsx ax, bl

MOVZX
\---------------------------------------
move with zero- extend
MOVZX O1, O2

POP
\---------------------------------------
POP O1
Stak(daha önce PUSH lanmis seyler) tan O1 icine cekmeye yarar. Stak n son karakterini ceker. Eger O1 16-Bit ise SP = SP+ 2 eger O1 32-Bit ise SP= SP+4 olur.

POPA
\---------------------------------------
pop all
POPA bütün registerleri kullanmak icindir. Registerler siradaki gibi kullanilmis olurlar;
DI, SI, BP, BX, DX, CX, AX
POPAD
\-------------------------------------
pop all doubleword
Baknz: POPA

POPAW
\-------------------------------------
pop all word
Baknz: POPA

PUSH
\--------------------------------------
PUSH O1
Stak 'a eleman göndermeye yarar, ama o1 8- Bitlik bir eleman olamaz. Eger O1 16-Bit ise SP = SP- 2 eger O1 32-Bit ise SP= SP- 4 olur.

PUSHA
\--------------------------------------
push all
16 bitlik bütün registerleri su sirada pushlar;
AX, CX, DX, BX, SP, BP, SI, DI.

PUSHAD
\------------------------------------
push all doubleword
baknz: PUSA

PUSHAW
\--------------------------------------
push all word
baknz: PUSHA

SMSW ---------------------------------------
store machine status word
SMSW O1
SMSW CR0 in ilk 16 bitini O1 e kaydeder. Aslinda isletim sisteminin ihtiyac duydugu, bir komuttur ve bir uygulamada kullanilmasi gerekli degildir.

MSRs
-------------------------------------- 80 nin üzerinde MSR vardir, ama her islemcide degisik olabilirler. Bu yüzden Pogramlamada fazla kullanilmamaktadirlar, WRMSR ile EDX: EAX icindeki eleman yazilir, RDMSR ile okunurlar. Tip: Hayla merak ediyorsaniz Döküman Nr. 245472 de Pentium4 ün MSRs hakkinda bilgi bulabilirsiniz, developer.intel.com da.

XCHG --------------------------------------
exchange
XCHG O1, O2
Iki elemanin iceriklerini degistirir. XLAT
\---------------------------------------
translate
XLAT \[O1\]
XLAT DS:(E)BX adresindeki degeri AL ye kopyalar. Önceden AL de hangi Byte istendigi yazilmalidir.
Örnek:
var db "ABCDE"
...
lea bx, var
mov al, 3 ;Dördüncü eleman
XLAT ; AL=D
...
XLAT ES: O1

EK B: NASILSINIZ?

; 2003 Anil Öner
.model small
.data

msg db "Iyimisiniz?(\[E\]vet/\[H\]ayir)$"
msg2 db 0Ah, "Iyi. :)$"
msg3 db 0Ah, "Kotu. :($"
.code
start:
mov ax, @data ; ds = data
mov ds, ax
mov ah, 09h
lea dx, msg ; Ekrana msg yi yaz.
int 21h
mov ah, 07h
int 21h
cmp al, 'e'
je sec\_1
cmp al, 'E'
je sec\_1 ; e yada E ise sec\_1 e git.
mov ah, 09h
lea dx, msg3 ; degilse msg3 u ekrana yaz
int 21h
sec\_1: ; iyi ise
mov ah, 09h
lea dx, msg2
int 21h
son:
mov ah, 04ch ; cikis
int 21h
end start
ends

EK C: AMD vs Intel(I64 vs X86-64)

Bu yazimda size bir kac yeni teknolojiden söz edecegim. Eminim ki aranizda Ia64 ve x86-64 ü duymus olanlar vardir.
Bu iki teknolojide 64- Bitlik sistemler.
Ia64
\----------------------------------------------------------------------------
Intelin CISC tabanli islemcileriyle Hp nin RISC tabanli islemcilerinin komutlarinin birlestirilmesiyle olusmus EPIC teknolojisine dayaniyor. Ilk EPIC islemci Itanium' du. Itanium Server ler icin gelistirilmis bir islemciydi, bu yüzden pahali. IA64 gercekten cok fazla registere sahip. Bu yüzden ziplama orani düsürülebiliyor. Buda gercekten cok iyi bir performans demek oluyor. Tabiki EPIC in gercek ten zor oldugunu söylemem gerek. Bunun disinda derleyicilerde EPIC icin cok optimize edilmis kod yaratamiyorlar.
Iste örnek bir kod:
Mantik
Eger p1=p2
r2=r3+r4
Yoksa
r7=r6-r5
EPIC:
cmp.eq p1, p2 = r1, r0
(p2) br.cond else\_clause
add r2 = r3, r4
br.endif
else\_clause:
sub r7 = r6, r5
endif:
....

Tabiki yukaridaki kod daha optimize edilmeden x86 gözüyle bakilarak yazildi, yani ziplama komutlariyla. Ayni Kodun optimize edilmis hali:
EPIC:
cmp.eq p1, p2 = r1, r0
(p1) add r2 = r3, r4
(p2) sub r7 = r6, r5
...
x86-64
\----------------------------------------------------------------------------
Simdide x86-64 sistemine bakalim. Ia64 ün aksine x86-64 Ia32 programlarini da 64- Bitlik programlarla ayni hizda calistirabiliyor. Eski x86 komut satirini kullaniyor, ama tabiki bircok yeni gelismeyle, bulardan en önemlileri:
-Eski registerlerin 64- Bitlik leri ve 8 yeni 64- Bit register.
-Daha temiz ve kullanisli bir FPU
-Gercek 64 Bitli adresleme
x86-64 de Intelin 16- Bit den 32- Bit e gecerken yaptigi straji kullaniliyor. Ilk x86-64 islemci AMD denin Hammer adli islemcisi.
Gcc de derlenmis örnek bir kod su sekilde gözüküyor:
Hammer: gcc
\-------------------------------------------------------------------------------
C:
int bar(int a,int b,int c) { return foo(a,b,c,0); }
bar\_x86: bar\_hammer:
pushl %ebp xorl %ecx, %ecx
movl %esp, %ebp jmp foo
pushl $0
pushl 16(%ebp)
pushl 12(%ebp)
pushl 8(%ebp)
call foo
addl $16, %esp
leave
ret
...

Ve Gelecek
\----------------------------------------------------------------------------
Peki ya gelecek, acaba Intel IA64 üylemi yeni nesil islemci modelini belirleyecek, yada AMD x86-64 üylemi.
Nasil olursa olsun 64- Bit lik islemcilerin kapida oldugunu görmemek olagan degil. Intel Serverler icin 64- Bitlik islemci yaratmaya calisirken, AMD Desktop Pc ler icin bunun aynisi yapmaya calisiyor. Peki ya gercektende Desktop Pclerin buna ihtiyaclari varmi? Gercektende gelecekte 16TByte lik Ram lar kullanmamiz gerekecekmi? Iste bu tip sorularin cevabini vu yilin sonuna dogru Amd nin Hammer islemcisi cikinca alacagimizi düsünüyorum. Eger AMD Hammer tutarsa büyük ihtimalle Intel 32- Bitlik Pentium 5 in tasarimini 64- Bitlik EPIC tasarimiyla zenginlestirip, masaüstüne sunmaya calisacaktir. Ama su anda x86-64 daha parlak bir gelecege sahip benziyor, cünkü 32Bitlik programlar cok fazla. Ve Intelin EPIC seti 32 Bitlik islemcileri gercekten yavas calistiriyor.
Yani su birkac yil bilgisayarlar icin cok önemli,
Iyi calismalar...
Kaynaklar:
\-----------------------------------
www.intel.com
www.amd.com
AMD Athon 64
IA64 Assembler
IA64 vs X86-64 was soll ein Hacker darüber wissen?
Itanium Sowftware Developer's Manual Volume 1,2,3

EK C: Küyük bir isletim sistemi YAZMAK!

Hangi Dil?
\----------------------------------------------------------------------------
Isletim sistemini aslinda C/C++ da yapmak isterim, ama mesela ekrana girdi vermek istedigimde bunun icin gerekli olan "printf" komutunu cagirmam gerektigini varsayalim. O zaman adindaki baslik dosyasini kullanmam gerekmekte.Ama sorun her basligin C/C++ derliyicileri tarafindan belli isletim sistemler(yada belli sistemler) icin tasarlandigi icin ne yazikki C/C++ dillerini cekirdegi yazarken kullanmayacagim fakat sonradan isletim sisteminin devamini C/C++ ile yazabilirsiniz.
Söyle düsük seviyede Assembler bilginiz olmasi sizin cekirdegi daha iyi anlamanizi saglayacaktir...
Gerekenler
\---------------------------------------------------------------------------
1.Netwide Assembler (NASM)
2.RaWrite yada Diskete Imageleri yazacak baska bir program.
3.Bos bir disket.
Buraya Dikkat!
\----------------------------------------------------------------------------
Size söylemem gerekirki Assembler ile cok sey yapilabilir(yada cok sey yanlis yapilabilir).Bu bilgisayariniza gelebilecek herhangibir zarar benim degil, sizin sucunuzdur!
Basliyoruz
\----------------------------------------------------------------------------
Bir isletim sisteminin nasil calistigini anlamak icin, önce bir bilgisayarin nasil calistigini iyi anlamak gerekir. Burada kisaca söylüyorum ki, önce bilgisayar acilir, hemen BIOS devreye girer ve denetimler yaptiktan sonra isletim sistemini cagirir. BIOS hangi sürücünün önce "BOOT" lanacagini belirler. Isletim sistemini önce yerel sürücüde arar. Biz isletim sistemimizi diskete yazacagiz.
Simdik kodlari yazmaya basliyalim;
\----------------------------------------------------------------------------
Ilk Kernel:
Tabiki bir Kernel sadece bir mesaj ekrana yazip sistemi yeniden baslatmak la kalmaz ama böyle bir kod yapiyi anlamak icin kolaydir:
\--------------------------------------------------------
mov ax, 1000h
mov ds, ax
mov es, ax
start: ; Burda gercek anlamda isletim
; sistemimize basliyoruz.
mov si, msg ; hemen bir string gösteriyoruz
call put
call read ; "oku" bir tusa basilana kadar bekler
jmp reset
msg db "Yeniden baslatmak icin bir tusa"
db "basin!",13,10,0
put:
lodsb
or al, al
jz short put\_d
mov ah, 0x0E
mov bx, 0x0007
int 0x10
jmp put

put\_d:
retn

read:
mov ah, 0
int 016h
ret

reset:
db 0Eah
dw 0000h
dw 0FFFFh
\---------------------------------------------------------
Dosyayi kernel.asm diye kaydettikten sonra;
nasm –f bin –o kernel.bin kernel.asm
seklinde derlenmelidir.

Bir BOOTMANAGER
\----------------------------------------------------------------------------

BIOS ilk acildiginda 512Bytes boyutunda bir OP-Code arar ve BIOS bu dosyayi 0x7C00 adresine yükler.
-----------------------BOOT.ASM--------------------------
org 0x7C00 ; Öncelikle dosyanin adresini ayaliyoruz.

start:
cli ; Interrupts kullanma!
mov ax, 0x9000 ; Stack adresini kayit etme
mov ss, ax
mov sp, 0 ; Stackpointer' 0 lamak
sti

mov \[bootdriv\], dl
call load ; Kernel i yükleme

mov ax, 0x1000 ; 0x1000 Shell' in adresi
mov es, ax
mov ds, ax
push ax
mov ax, 0
push ax
retf

bootdriv db 0
loadmsg db "Sistem Yükleniyor...",13,10,0

putstr:
lodsb
or al,al
jz short putstrd
mov ah,0x0E
mov bx,0x0007
int 0x10
jmp putstr
putstrd:
retn

load:
push ds
mov ax, 0
mov dl, \[bootdriv\]
int 13h
pop ds
jc load

load1:
mov ax,0x1000
mov es,ax
mov bx, 0
mov ah, 2
mov al, 5
mov cx, 2
mov dx, 0
int 13h
jc load1
mov si,loadmsg
call putstr
retn

;Programin 512 Bytes dan büyük olmamasi icin...
times 512-($-$$)-2 db 0
dw 0AA55h ; Bu da BIOS sa bitis talimatini verir
\----------------------------------------------------
nasm –f bin –o boot.bin boot.asm seklinde de dosya derlenmelidir.

Simdide isletim sistemimizi Diskete yükleyip calistirmak icin;

copy boot.bin+kernel.bin vitaxia.img
Seklinde iki dosyayi birlestiriyoruz.
Son olarak da RaWrite programi ile bu img dosyasini diske yaziyoruz. Disketi sokup bilgisayari yeniden baslattigimizda isletim sistemimiz calisacaktir.
Son olarak tabi ki bunu hepsi sadece bir örnek, nasil bir isletim sistemi yapabilecegimize dahil.
Herkese iyi calismalar...

- The END -

---
*Kaynak: `ASSEMBLER/ASSEMBLER.doc` — ogrenci — 2004*
