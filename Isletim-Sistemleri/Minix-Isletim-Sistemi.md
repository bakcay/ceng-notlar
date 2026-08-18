# Minix İşletim Sistemi

**MİNİX İŞLETİM SİSTEMİ**

“Küçük olan her şey güzeldir”

Minix , bütün kaynak kodları mevcut olan serbest bir unix clone’dur. İsminin açılımı mini-unix şeklindedir. Bütün kaynak kodları C diliyle yazılmış olup, içerisinde güçlü bir ANSI-C compiler bulundurur.

Minix ‘in yazılma amacı : Gerçek bir işletim sistemini parçalara ayırmak için kullanılan deneysel bir işletim sistemidir. Kullanıcıların kendi kişisel bilgisayarlarında Unix’in çalışma sistemini öğrenmelerini amaçlar.

Unix 6.0 AT&T lisansı altında – kaynak kodları açık bir şekilde – ve kolay bulunabiliyordu. Unix 7.0 piyasaya sürülmesi sırasında kaynak kodların açık bir şekilde olmasının ticari amaçlı kullanılabileceğini fark etti. Unix’in 7.0 dan itibaren açık kod sistemini terk etti. Fakat işletim sisteminin sadece teori üzerinde anlatılması , öğrencinin işletim sistemi hakkında yeterli bir bilgi kazanmasına engel oluyordu.

Mr. Tatenbaum öğrencilerin üzerinde değişiklik yapabilecekleri Unix 7.0 !a uyumlu bir işletim sistemi yazdı ve buna mini unix (minix) ismini verdi. Şimdi bu işletim sistemi 1984 den bu yana işletim sisteminin iç yapısını görmede kullanılıyor.

Minix çıkan versiyonları ve tarihleri;

1984 Minix

1987 Minix 1.0

1992 Minix 1.5 (intel,macintosh,amiga,atari,SPACH)

1996 Minix 1.7.2

1997 Minix 2.0.0 (intel )

1998 Minix 2.0.2

Ayrıca minix linux’ın temelini oluşturur. Linus torvalds minix’in daha gelişmiş bir modelini tasarlamaya karar vermiş ve bu da linux’ın doğuşu olmuştur. (25 Ağustos 2001)

Minix Yapısı : Minix Unix’e göre daha modüler yapıdadır. Kullanıcı görüşü açısından

Unix ile tam uyumlu olmasına karşın iç yapısı Unix den farklıdır. Örneğin Minix’in dosya sistemi tamamen işletim sisteminin bir parçası değildir. Fakat bir kullanıcı programı olarak çalışır. Bir çok yardımcı program cat,grep,ls,man,make... shell üzerinde bulunur ve bunlar Unix fonksiyonları ile aynı görevi görürler. Shell ise Bourne shell yapısındadır.Minix Unix kadar etkin değildir., çünkü okumak için tasarlanmıştır. Minix en büyük özelliğinden biriside çok az alan kapsamasıdır. İlk versiyonlarında 5mb yer kaplayan minix’in en son versiyonu 2.0 20mb yer kaplamaktadır.

Kullanıldığı platformlar; Kişisel bilgisayarlar (PC) geniş uygulama alanına sahip olduğundan ve geniş çapta kullanıldığı için minix ilk sürümünden itibaren kişisel bilgisayarları desteklemiştir. Minix’in 1.5 versiyonu atari,amiga,macintosh ve Sparch platformlarını da desteklemektedir. Ayrıca değişik enstitüler tarafından yürütülen projeler kapsamında Solaris-minix, mac-minix,palm-minix gibi minix yeni türevleri ortaya çıkarılmıştır.

Minix bir öok türewvi olmasına karşın resmi olarak www.minix.org adresi ile temsil edilmektedir. Ayrıca minix kullananlar kurdukları bir haber grubu ile sorunlarını ve çözüm yollarını paylaşmaktadırlar. 1987 den beri faaliyet gösteren haber grubu : comp.os.minix şu anda 40 bin üyeye sahiptir.

Minix 2.0 özellikleri ;

62000 satır kod

Multi programs

Protected çalışma modu 286,386,486 ve pentium için

RS-232 Com portu desteği

Üç veya daha fazla kullanıcının bir bilgisayarda çalışması

Tümü Kaynak kodlar C ‘de

Extended memory desteği

ANSI-C compiler içerir

Kabuğu Bourne shell’e benzer

TCP/IP desteği vardır

200 yardımcı program bulunur

Kütüphanesinde 300 fonksiyon bulunur

Beş tane kelime işlemci (emacs subset, vi clone, ex, ed, and simple screen editor)

40.000 kelime üzerinde yazım hatası tespiti yapabilme

Donanım Gereksinimi;

Minix 2.0 8088, 286, 386, 486, or Pentium CPU bulunan kişisel bilgisayarlarda sorunsuz çalışabilir. Ve bunlarda bulunan donanıma %100 destek verir. (i.e, EISA bus, IDE disk, etc.).

16 bitlik versiyonu 640Kb minimum, 32 bitlik versiyonu en az 2 Mb hafızaya ihtiyaç duyar. CGA,EGA,VGA monochrome veya Hercules ekran kartlarını da destekler. Ayrıca 5.25” ve 3.5” disketleri destekler. LPT portundan yazıcı çıkışı ile seri hattan terminal birimini de desteklemektedir. Bazı ethernet kartları ile mitsumi CD-ROM’ları da desteklemektedir.

Minix Simulatörleri ;

Minix2i kurmadan çalıştırmanın bir yolu da simule programlarıdır. Bunlardan en çok kullanılanı dosminix adlı programdır. Dosminix üzerinde boot.com, makefile.exe ve minix.mnx isimli 3 ayrı dosya bulunuyor. Minix.mnx açılacak olan dosyadır . Boot minix.mnx

Komutu verildiğinde minix işletim sistemi çalıştırılacaktır.

Program start minix yazısı görüldüğünde ‘=’ tuşuna basılarak boot işlemi başlatlır. Buradan da görüldüğü gibi kernel windows altında çalışmamaktadır. Bu silmulatoru kullanmak için bilgisayarın “Güvenli Kip Komut İstemi” nde açılması sağlanmalıdır.

Minix 2.0 kurulumu:

Minix , ilk adım ve çok önemli adımı kurmadan önce , readme.txt okunmalıdır. Minix cd ile gelen txt dosyası kurulum için ihtiyaç duyan disklerin sayısını size söyleyecek . Aynı zamanda , o , minix için sistem gereksinimlerini belirtecektir. Esasen , aşağıdaki adımlar , minix kurulumu işlemi sırasında ne olduğunu kapsayacaktır.

minix/readme.txt dosyasını oku

Disketleri oluştur.

İnstall minix işlemine başlayınız

/usr: /dev/fd0c şeklinde sürücüyü göster

root olarak login ol ve start setup işlemi yap

F3 ile yazılım geçişi yapılabilir

Bir yanlışlık anaında Del ile işleme son verin

“halt” yazıp “boot hd1” “=” tuşuna basın

root olarak login olun

İç yapısı

Minix 2.0’da bulunan programların listesi ;

aal add\_route advent animals ar ascii ash at atrun autil backup badblocks banner basename bawk bc bin btoa byacc cal calendar cat cawf cd cdiff cdplay cgrep chmem chmod chown ci cksum clr cmp co comic comm compress cp crc cron cut date dd de decomp16 df dhrystone diff dirname dis88 diskcheck diskusage dosread du dw echo ed eject elle elvis expand expr factor fdisk fgrep file find finger flex fold format fortune fsck ftp gather getty gomoku grep head host hostaddr ic id ifconfig ifdef indent inodes install irdpd isoread join kermit kill last leave life loadfont loadkeys login look lpr ls m4 mail make man men mined mixer mkdir mkfifo mkfs mknod mkproto modem mount mref mt ncheck nm nonamed od part partition passwd paste patch pathchk ping playwave postmort pr prep pretty printenv printroot proto ps pwd rarpd rcp readall readclock readfs reboot recover recwave remsync repartition rev rlogin rmdir roff rsh screendump scripts sdump sed sh shar simple size sleep sort split strings strip stty su sum swapfs sync synctree tail tar tcpd tee telnet term termcap test time touch tr traverse treecmp tset tsort ttt tty umount uname unexpand uniq unshar update users uud uue vol wc whatsnew which who whoami width write xargs yap yes zmodem

Minix 2.0 da bulunan fonksiyonlar;

abort abs access alarm alloca asctime asin assert asynchio atan atan2 atexit atof atoi atol bcmp bcopy brk brksize bsearch bzero calloc ceil cfgetispeed cfgetospeed cfsetispeed cfsetospeed chartab chdir chmod chown chroot clearerr clock close closedir creat crypt ctermid ctime cuserid data difftime div doprnt doscan dup dup2 ecvt environ errlist errno ether\_line ethera2n ethere2a etherh2n ethern2h exec execl execle execlp execn execv execve exit exp ext\_comp fabs fclose fcntl fdopen feof ferror fflush ffs fgetc fgetpos fgets fileno fillbuf floor fltpr flushbuf fmod fopen fork fpathconf fprintf fputc fputs fread freopen frexp fscanf fseek fsetpos fslib fstat fsversion ftell fwrite getc getchar getcwd getdomain getegid getenv geteuid getgid getgrent getgroups gethnmadr gethostent gethostname getlogin getopt getpass getpid getppid getprocessor getproto getprotoent getpw getpwent gets getservent getsrvbyname getsrvbyport getuid getw gmtime gtty hton hugeval hypot icompute index inet\_addr inet\_ntoa ioctl iolib isalnum isalpha isascii isatty iscntrl isdigit isgraph islower isnan isprint ispunct isspace isupper isxdigit itoa kill labs ldexp ldiv link loadname localeconv localtime lock log log10 longjerr lrand lsearch lseek malloc mblen mbstowcs mbtowc memccpy memchr memcmp memcpy memcspn memmove memset misc mkdir mkfifo mknod mktemp mktime modf mount mtab nlist oneC\_sum open opendir pathconf pause peekpoke perror pipe popen pow printf printk ptrace putc putchar putenv puts putw qsort raise rand rcmd read readdir reboot regexp regsub remove rename res\_comp res\_init res\_mkquery res\_query res\_send rewind rewinddir rindex rmdir sbrk scanf seekdir sendrec setbuf setgid setjmp setlocale setuid setvbuf sigaction sigaddset sigdelset sigemptyset sigfillset sigismember sigmisc signal sigpending sigprocmask sigreturn sigset sigsetjmp sigsuspend sin sinh sleep sprintf sqrt sscanf stat stderr stime strcasecmp strcat strchr strcmp strcoll strcpy strcspn strerror strftime strlen strncat strncmp strncpy strnlen strpbrk strrchr strspn strstr strtod strtok strtol strxfrm stty swab sync syscall sysconf system tan tanh taskcall tcdrain tcflow tcflush tcsendbreak telldir termcap termios time times tmpfile tmpnam tolower toupper ttyname tzset umask umount uname ungetc unlink utime vfprintf vprintf vsprintf wait waitpid wcstombs wctomb write

---
*Kaynak: `MİNİX İŞLETİM SİSTEMİ/MİNİX İŞLETİM SİSTEMİ.doc` — M. Şakir Özkan — 2004*
