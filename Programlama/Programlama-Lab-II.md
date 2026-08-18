# Programlama Lab II

## DERSİN ADI:PROGRAMLAMA LAB II

GELİŞTİRME ORTAMI:Windows işletim yüklü bir bilgisayarda pc de dos ortamında yazılmıştır.Programın kaynak kodu Turbo C’dir

ÇALIŞMA ŞEKLİ:202038.exe dosyasının tıklanmasıyla ekrana programın yapan kişinin bilgilerinin aktarılmasını ardından.Seçim yapmanız için 8 işlevin bulunduğu bir menü çıkıyor burdan 1 ile 8 arasında seçeceğiniz rakamlar sayesinde açıklaması solda bulunan açıklamaları gerçekleştiriliyor.1 kayıtlar için burda işçinin sicil numarasından ücretine kadar olan bilgilerin girilmesi isteniyor.2 istenilen bölümde ve isimde kayıt aranılması ve listelenmesi sağlanıyor.

3 tüm işçilerin şirkete alacakları maaşların toplamları gösteriliyor.4 işçiler arasından en yüksek maaşı alan kişiyi gösterir.5 silmek istediğiniz kişinin bilgilerini girilmesi sonucu silme işlemi gerçekleştiriliyor.6 isçi bilgilerinin isciler.txt adlı bir dosyaya kayıt ve eklenmesi sağlanıyor.7 isciler.txt dosyasındaki bilgilerin okunulması sağlanıyor.8 programdan çıkış sağlanıyor.

DEĞİŞKEN SABİT VE ALT PROGRAMLAR:

void kayit(void)//Dizi halinde kayit yapılıyor

{

int indis;

char cp;

char kr;

int saat;

unsigned long int brsaat;

do{

indis=ver();

(**dizinin hangi indisli elemanına kayıt yapılacağını veren ver() adlı fonksiyon çağrıldı)******

if(indis<0){

(**Eğer ver() adlı fonksiyon –1 değerini gönderirse ,dizide yer yok olarak değerlendirilir)**

printf("Liste dolu kayıt yapamam");

return;}

clrscr();

gotoxy(20,12);printf("İşçinin....:");

gotoxy(20,13);printf("Sicil Numarası:");

scanf("%lu",&calis\[indis\].sicil);

gotoxy(20,14);printf("Adı:");

scanf("%10s", &calis\[indis\].ad);

gotoxy(20,15);printf("Soyadı:");

scanf("%20s", &calis\[indis\].soyad);

gotoxy(20,16);printf("Çalıştığı");

gotoxy(20,17);printf("Bölümü:");

scanf("%10s",&calis\[indis\].bolumu);

gotoxy(20,18);printf("Ücreti:");

scanf("%lu",&calis\[indis\].ucret);

gotoxy(20,19);printf("Fazla mesai varmı?(E/H)");

cp=toupper(getch());

if(cp=='E') {

gotoxy(20,20);printf("Kaç saat?");

scanf("%d",&saat);

gotoxy(20,21);printf("Birim saat ucreti?");

scanf("%lu",&brsaat);

calis\[indis\].toplam=calis\[indis\].ucret+(saat\*brsaat);

gotoxy(20,22);printf("Başka kayit yapacak misin?(E/H)\\n");

kr=toupper(getch());

}

else{

calis\[indis\].toplam=calis\[indis\].ucret;

gotoxy(20,21);printf("Başka kayit yapacak misin?(E/H)\\n");

kr=toupper(getch());

}

}while(kr=='E');

}

int ver()**(anlamlı kayit olmayan dizi elemanın indisini verir)******

{

int erd;

for(erd=0; calis\[erd\].ad\[0\] && erd<MAX; erd++);

if(erd<MAX) return erd;

else return -1;

}

void goster(int vol)**(tek bir kayıtı ekrana yazdırır)**

{

clrscr();

gotoxy(20,12);printf("İşçinin...");

gotoxy(20,13);printf("Sicil:%lu",calis\[vol\].sicil);

gotoxy(20,14);printf("Adı:%s",calis\[vol\].ad);

gotoxy(20,15);printf("Soyadı:%s",calis\[vol\].soyad);

gotoxy(20,16);printf("Çalıştığı...");

gotoxy(20,17);printf("Bölümü:%s",calis\[vol\].bolumu);

gotoxy(20,18);printf("Ücret:%lu T.L.",calis\[vol\].toplam);

getch();

}

void arama(void)**(Bulunmak istenilen kişiyi arar)**

{

int k;

char ad\[10\];

char bolu\[10\];

clrscr();

gotoxy(20,14);printf("Hangi Bölüm:");

scanf("%9s",bolu);

gotoxy(20,15);printf("İsim:");

scanf("%9s",ad);

for(k=0; k<MAX; k++)

if (calis\[k\].ad\[0\]&&calis\[k\].bolumu\[0\])

if(!strcmp(calis\[k\].ad,ad)&&!strcmp(calis\[k\].bolumu,bolu)){

**(bulmak istenilen kişinin bilgilerinin kayıtlı listede olup olmadığına bakar varsa goster fonksiyonunu çağırır)**

goster(k);

}

else{

gotoxy(20,16);printf("Bulunamadı ");

YAZ;

}

}

int varmi(char isim\[\],char soyisim\[\],char bol\[\] )

**(bir kayıtı dizide arar,varsa indisini gönderir)**

{

int k;

for(k=0;k<MAX;k++)

if(calis\[k\].ad\[0\])

if(!strcmp(calis\[k\].ad,isim)&&!strcmp(calis\[k\].soyad,soyisim)&&!strcmp(calis\[k\].bolumu,bol))

**(Girilen kişilerin listede istenilen kişinin olup olmadığını varsa indis numarasını yoksa **

**–1 gönderir)**

return k;

return -1;}

void maas(void)

{

int k;

unsigned long int masraf;

masraf=0;

for(k=0;k<MAX;k++)

masraf+=calis\[k\].toplam;

printf("Bu ay işçilere ödenen tutar:%lu",masraf);

getch();

}

void silme(void)/\*kayıt silmek için kullanılır\*/

{

int k,indis;

char ad\[11\],soyad\[21\],bolumu\[21\];

clrscr();

gotoxy(20,12);printf("Silmek istediğiniz işçinin :");

gotoxy(20,13);printf("Adı:");

scanf("%10s",ad);

gotoxy(20,14);printf("Soyad :");

scanf("%20s",soyad);

gotoxy(20,15);printf("Bölüm :");

scanf("%10s",bolumu);

indis=varmi(ad,soyad,bolumu);

if(indis==-1){

printf("Boyle biri yok!\\n Silinmedi.\\n");

getch();

return;

}

else

{

puts("Sildim...\\n");

getch();

calis\[indis\].ad\[0\]=NULL ;

}

}

void sakla(void)/\*diziyi diske/diskete yazar\*/

{

FILE \*di;

int k;

if((di=fopen("isciler.txt","a+"))==NULL) **(ekleme ve yazma modunda açılır)******

puts("dosya açılmadi...\\n");

return;

}

puts("saklıyorum\\n");

for(k=0;k<MAX;k++)

if(calis\[k\].ad\[0\])

fwrite(&calis\[k\],sizeof(KAYITP),1,di);

**(Burda dosyaya erişiliyor bilgiler yazılıyor)**

fclose(di);

**(dosya kapatılıyor)**

}

void yukle(void)/\*diskten/disketten kayıtları okur ve diziye ekler\*/

{FILE \*di;

unsigned int tane;

int k,i;

if((di=fopen("isciler.txt","r"))==NULL) **(okuma modunda açar)******

puts("dosya acilmadi\\n");

return;

}

fseek(di,0,2);

**(di ile belirtilen dosyanın kayıt işaretçisini istenilen yere konumlandırmak için öteler)**

tane=ftell(di)/sizeof(KAYITP);

fseek(di,0,0);(**kayıt işaretçisinin dosya başına göre (sekizli olarak) uzaklığını verir)**

puts("yukluyorum...\\n");

for(k=0;k<tane;k++){

i=ver();

if(i==-1){

printf("dizide yer kalmadi !\\n yukleyemem.");

break;

}

fread(&calis\[i\],sizeof(KAYITP),1,di);

}fclose(di);**(dosyadan toplu okuma yapmak içn kullanılır)**

}

PROGRAM MANTIĞI:Bir iş yerindeki çalışanların maaşlarını hesaplanması bunların istenildiğinde bulunması en yüksek maaşı alan kişinin belirlenmesi gibi fonksiyonları içeren bir program mantığı izlendi.

KARŞILAŞILAN ZORLUKLAR VE ÇÖZÜM AŞAMALARI:

Program yazılmadan önce bilgilerin hangi yöntemle kayıt edilmesi düşünüldü sonuç olarak diziler kullanılarak kayıt edilme karar verildi.Zorluklar arasında nasıl kayıt edileceği bunlar üzerinde nasıl işlem yapılacağı sorunu çıktı bu sorunu gidermek için kaynak kitap aranıldı sonuç olarak kaynak kitaptan faydalanarak sorun giderildi.

SONUÇ VE YORUM:Bu program diziler kullanarak kayıt nasıl yapılacağı bunları bilgisayara kayıt etme okuma işlemlerini nasıl gerçekleştirileceği öğrenildi.Program geliştirilmeye açık olup birkaç fonksiyon daha eklenebilir bunlar arasında düzeltme vs. fonksiyonlar olabilir.Kısacası dosyaların hangi mantık ve algoritma izlenerek kullanılacağı görüldü.

## KAYNAKLAR

\[1\] DR. RIFAT ÇÖLKESEN,”İŞTE C PROGRAMLAMA DİLİ”,Papatya Yay.,2001

---
*Kaynak: `PROGRAMLAMA LAB II/PROGRAMLAMA LAB II.doc` — volkan — 2004*
