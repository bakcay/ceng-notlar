# Kim Korkar UNIX Ten

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 141

Kabuk Programlama Kabuk Programlama Kabuk Programlama Kabuk Programlama Shell Programming Shell Programming Shell Programming Shell Programming

İlginizi çekmiyorsa bu bölümü atlayabilirsiniz.

İlginizi çekmiyorsa bu bölümü atlayabilirsiniz.

İlginizi çekmiyorsa bu bölümü atlayabilirsiniz.

İlginizi çekmiyorsa bu bölümü atlayabilirsiniz.

Bu bölümdeki amacım, okuyuculara kabuk programlamayı öğretmek değil, sadece bu kavramın nasıl bir şey olduğu konusunda fikir vermek. Aslında oldukça karmaşık ve deneyim isteyen kabuk programlama, tipik UNIX kullanıcılarının pek ilgisini çekmez. Programcılık temeli olan okuyucularaysa oldukça ilginç gelebilir; ancak bu kitapta anlatılanlar kabuk programlamayı öğrenmek için kesinlikle yeterli değildir.

Güzel güzel kabuk programlarından bahsederken konuyu dağıtıp süreç kavramına ve onunla ilgili komutlara daldık. Aslında birbirleriyle yakın ilişkisi olan bu iki kavramı da başka nasıl anlatacağımı bilemedim. Neyse, kabuğumuza dönelim..

Kabuk programları, (sh sh sh sh, csh csh csh csh ve tsch tsch tsch tsch) aslında oldukça gelişmiş birer programlama dilini çözümleyebilecek yeteneğe sahiptir. Genel amaçlı işler için pek kullanışlı olmamakla birlikte ileri düzeydeki UNIX kullanıcıları ve sistem yöneticilerinin oldukça sık kullanılacakları özelliklere sahiptirler.

csh ve sh kabuk programlama dilleri birbirlerinden oldukça farklıdır. Bu kitapta

csh ve sh kabuk programlama dilleri birbirlerinden oldukça farklıdır. Bu kitapta

csh ve sh kabuk programlama dilleri birbirlerinden oldukça farklıdır. Bu kitapta

csh ve sh kabuk programlama dilleri birbirlerinden oldukça farklıdır. Bu kitapta

vereceğim örnekler genellikle csh kabuğuna göre olacaktır.

vereceğim örnekler genellikle csh kabuğuna göre olacaktır.

vereceğim örnekler genellikle csh kabuğuna göre olacaktır.

vereceğim örnekler genellikle csh kabuğuna göre olacaktır.

Kabuk programlama hakkında daha fazla ayrıntıya girmek isteyen okuyucular için The UNIX C Shell Field Guide The UNIX C Shell Field Guide The UNIX C Shell Field Guide The UNIX C Shell Field Guide UNIX POWER TOOLS UNIX POWER TOOLS UNIX POWER TOOLS UNIX POWER TOOLS Gail & Paul Anderson J. Peek, Tim O’Reilly & M. Loukides Prentice-Hall, 1986 O’Reilly & Associates, 1993 ISBN 0-13-937468-X 025 ISBN 0-553-35402-7 isimli kitapları hararetle tavsiye ederim.

MS-DOS’daki batch batch batch batch dosyalarını hatırlarsınız. Sık tekrarlanacak komut dizilerini, uzantısı BAT olan bir dosyaya yazıp, sanki bir programmış gibi sadece bu dosyanın adını vererek komut dizisini çalıştırırdık. (Nedense geçmiş zaman kullandım... UNIX işletim sisteminin tadını bir kez alan kullanıcılar için MS- DOS, gerçekten de gerilerde kalmış bir işletim sistemi gibi oluyor.) kabuk kabuk kabuk kabuk programlama programlama programlama programlama’nın mantığı da aynı batch batch batch batch dosyalar gibidir. Tek farkla ki; kabukların koşula bağlı komut çalıştırma, karşılaştırmalar, klavyeden kullanıcıların bilgi girme olanakları gibi özelliklerinin çok, ama gerçekten çok daha gelişmiş olmaları sayesinde karmaşık işlerin yapılmasına olanak sağlarlar.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 142

MS-DOS’ta, bilgisayar açıldığında otomatik olarak çalıştırılması gereken programlarla ilgili komut satırlarının yer aldığı AUTOEXEC.BAT diye bir dosya vardır. UNIX’de de aynı amaca yönelik; ama bu sefer, çok daha fazla sayıda dosya vardır.

Örneğin BSD UNIX’lerde, /etc /etc /etc /etc dizinin altında rc, rc.boot, rc.local rc, rc.boot, rc.local rc, rc.boot, rc.local rc, rc.boot, rc.local gibi isimleri olan dosyalar; sistem açılışının çeşitli aşamalarında otomatik olarak çalıştırılması istenen programlarla ilgili komut satırlarını içerirler. (System V UNIX’lerde bu dosyalar /etc/rc /etc/rc /etc/rc /etc/rc’nin altında yer alan dosyalardır.) Ancak, bu satırlar, basit birer komutlar dizisi yerine, sh sh sh sh veya csh csh csh csh kabuk kabuk kabuk kabuk programlarıdır programlarıdır. programlarıdır programlarıdır Aynı şekilde, kullanıcıların sisteme login login login login veya logout logout logout logout ettiklerinde otomatik olarak çalıştırılacak kabuk programları da her kullanıcının kendi home home home home dizininde, .login, .cshrc .login, .cshrc .login, .cshrc .login, .cshrc ve .logout .logout .logout .logout isimli dosyalarda yer alır. Şimdi isterseniz birkaç örnek kabuk programına göz atalım:

İ lk Kabuk Programımız

İ lk Kabuk Programımız

İ lk Kabuk Programımız

İ lk Kabuk Programımız

İlk örneğimiz, sistemde yaratmış olabileceğimiz bazı gereksiz dosyaları, arada sırada temizlemek için kullanacağımız bir kabuk programı yazmakla ilgili...

Öncelikle aşağıdaki UNIX komutlarını temizle temizle temizle temizle isimli bir dosyaya kaydediniz. Bu iş için vi vi vi vi komutunu kullanabilirsiniz.

```bash
df df df df cd ~ cd ~ cd ~ cd ~ /usr/bin/rm *tmp /usr/bin/rm *tmp /usr/bin/rm *tmp /usr/bin/rm *tmp cd proglar cd proglar cd proglar cd proglar /usr/bin/rm *.o /usr/bin/rm *.o /usr/bin/rm *.o /usr/bin/rm *.o cd .. cd .. cd .. cd ..
/usr/bin/rm core /usr/bin/rm core /usr/bin/rm core /usr/bin/rm core df df df df
```

Bir sonraki adımda, bu dosyanın bir program dosyası gibi çalıştırılacağını belirtmemiz gerekir. (Dosya erişim yetkilerini hatırlayınız...)

Bunu yapabilmek için

```bash
% chmod % chmod % chmod % chmod 755 temizle 755 temizle 755 temizle 755 temizle
```

komutunu veriniz. (rwxr-xr-x rwxr-xr-x rwxr-xr-x rwxr-xr-x yetki kalıbı).

Kabuk programımızdaki komutlara şimdi birer birer göz atalım:

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 143

df df df df cd ~ cd ~ cd ~ cd ~ Disklerin ne kadarının kullanıldığını gösteren bir UNIX komutudur. (Disk Free). Sistemdeki dosya sistemlerinin (disk bölümlerinin) toplam kapasitelerini ve ne kadarının kullanılmış olduğunu rapor eder. Bu komutu, disklerdeki temizlik öncesi boş yer durumunu görmek için koyduk.

Kullanıcının home home home home dizinine geçmek için. Zaten başkalarına ait dosyaları silemeyiz.

/usr/bin/rm \*tmp /usr/bin/rm \*tmp /usr/bin/rm \*tmp /usr/bin/rm \*tmp Adı tmp tmp tmp tmp ile biten dosyalarısilmek için. Bu komutta MS- DOS kullanıcılarına garip gelecek iki nokta var.

Birincisi \*.tmp \*.tmp \*.tmp \*.tmp yerine \*tmp \*tmp \*tmp \*tmp kullanılmış olması!

Biliyorsunuz, UNIX’de dosya uzantısı diye bir kavram yok ve noktanın da özel bir anlamı yok. O nedenle, nokta kullansaydık, sadece adının son 4 karakteri .tmp .tmp .tmp .tmp olan dosyaları silmiş olurduk. sirali-tmp sirali-tmp sirali-tmp sirali-tmp gibi bir ismi olan dosya silinmeden kalırdı.

İkincisi de, rm rm rm rm komutunun sadece rm rm rm rm şeklinde değil, /usr/bin/rm /usr/bin/rm /usr/bin/rm /usr/bin/rm şeklinde kullanılmış olması.

Silme komutunu sadece rm rm rm rm şeklinde kullanmış olsaydık, büyük olasılıkla, alias alias alias alias komutuyla "rm -i" "rm -i" "rm -i" "rm -i" olarak değiştirilmiş olan rm rm rm rm komutu çalışacak ve silinecek tüm dosyalar için birer kere "Emin misiniz?" "Emin misiniz?" "Emin misiniz?" "Emin misiniz?" anlamında "Are you sure?" "Are you sure?" "Are you sure?" "Are you sure?" sorusu ile karşılaşacaktık. cd proglar cd proglar cd proglar cd proglar proglar proglar proglar proglar alt dizinine geçmek ve adının sonu .o .o .o .o olan /usr/bin/rm \*.o /usr/bin/rm \*.o /usr/bin/rm \*.o /usr/bin/rm \*.o dosyaları silmek için. (Derleyicilerin ürettiği ‘object’ dosyalar) cd .. cd .. cd .. cd .. Bir üst düzeydeki dizine geçmek için (home home home home dizinimize geri dönüyoruz).

/usr/bin/rm core /usr/bin/rm core /usr/bin/rm core /usr/bin/rm core hatalı yazılmış programlar ya da doğru yazılmış programları hatalı kullanmamızdan dolayı oluşabilecek core core core core isimli dosyaları silmek için. du du du du Temizlik sonrası disk kullanım (disk usage) durumunu görmek için.

Aslında bütün bu silme işlerini tek bir rm rm rm rm komutuyla, yapabilirdik; ama o zaman kabuk programlamaya fazla kısa bir örnek vermiş olurduk (!).

```bash
/usr/bin/rm ~/*tmp ~/proglar/*.o ~/core /usr/bin/rm ~/*tmp ~/proglar/*.o ~/core /usr/bin/rm ~/*tmp ~/proglar/*.o ~/core /usr/bin/rm ~/*tmp ~/proglar/*.o ~/core
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 144

Şimdi biraz daha karmaşık bir kabuk programına göz atalım.

İ kinci Kabuk Programımız

İ kinci Kabuk Programımız

İ kinci Kabuk Programımız

İ kinci Kabuk Programımız

Bu csh csh csh csh kabuk programı (adı merhaba merhaba merhaba merhaba olabilir) çalıştırıldığında; parametresi olarak verilen kullanıcının sistemde olup olmadığına bakacak; kullanıcı sistemdeyse, talk talk talk talk programını başlatarak onunla doğrudan görüşmemizi sağlayacak; yok eğer o kullanıcı sistemde değilse, mail mail mail mail programını başlatıp ona bir elektronik mesaj göndermemizi sağlayacaktır.

```bash
#!/bin/csh #!/bin/csh #!/bin/csh #!/bin/csh
# Ornek bir csh kabuk programi # Ornek bir csh kabuk programi # Ornek bir csh kabuk programi # Ornek bir csh kabuk programi
# # # #
# # # # 9 Mayis 1995 - Ugur Ayfer 9 Mayis 1995 - Ugur Ayfer 9 Mayis 1995 - Ugur Ayfer 9 Mayis 1995 - Ugur Ayfer
# # # #
set w = (`who | grep $argv[1]` ) set w = (`who | grep $argv[1]` ) set w = (`who | grep $argv[1]` ) set w = (`who | grep $argv[1]` ) if ($#w == 0) then if ($#w == 0) then if ($#w == 0) then if ($#w == 0) then echo "$argv[1] sistemde degil... mektup gonderiniz..." echo "$argv[1] sistemde degil... mektup gonderiniz..." echo "$argv[1] sistemde degil... mektup gonderiniz..." echo "$argv[1] sistemde degil... mektup gonderiniz..." mail $argv[1] mail $argv[1] mail $argv[1] mail $argv[1] else else else else echo "$argv[ echo "$argv[ echo "$argv[ echo "$argv[1] sistemde... Gorusebilirsiniz...." 1] sistemde... Gorusebilirsiniz...." 1] sistemde... Gorusebilirsiniz...." 1] sistemde... Gorusebilirsiniz...." talk $argv[1] talk $argv[1] talk $argv[1] talk $argv[1]
endif endif endif endif
```

İşte bu kabuk programı biraz çetrefilli...

\# # # # ile başlayan satırlar kabuk tarafından dikkate alınmaz. O nedenle

programınız hakkında açıklamalar yapmak için kullanabilirsiniz.

İlk satırdaki #!/bin/csh #!/bin/csh #!/bin/csh #!/bin/csh özel bir kalıptır. Bu kalıp, kabuk programınının çalıştırılması sırasında csh csh csh csh kabuğunun kullanılması gerektiğini belirtir. Eğer bir başka kabuk çalışıyorsa; yeni bir csh csh csh csh kabuğu başlatılır ve program bitince bu yeni csh csh csh csh öldürülür. set w = (\`who | grep $argv\[1\]\` ) set w = (\`who | grep $argv\[1\]\` ) set w = (\`who | grep $argv\[1\]\` ) set w = (\`who | grep $argv\[1\]\` ) komutu biraz karışık.. Bu komut önce who who who who programını çalıştırıyor. Bu komutla, sistemde çalışan kullanıcıların listesi üretiliyor. Bu liste ekrana görüntülenmek yerine grep grep grep grep programına girdi olarak gönderiliyor (piping). Bir filtre olarak görev yapan grep grep grep grep programı, kendisine gönderilen satırlar arasında sadece içinde $argv\[1\]; (yani merhaba merhaba merhaba merhaba komutunu kullanırken vereceğimiz parametre) geçen satırları geçiriyor.

Bu liste (içinde ilgilendiğimiz kullanıcının adı geçen satırlar) w w w w isimli bir kabuk değişkene atanıyor.

Eğer bu listenin uzunluğu sıfırsa ( if ($#w == 0) then if ($#w == 0) then if ($#w == 0) then if ($#w == 0) then ) ) ) ) ; listede ilgilendiğimiz şahsın adı geçen bir satır yok demektir; yani aradığımız şahıs sistemde değildir. Bu durumda ekrana

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 145

..... sistemde degil... mektup gonderiniz... ..... sistemde degil... mektup gonderiniz... ..... sistemde degil... mektup gonderiniz... ..... sistemde degil... mektup gonderiniz... mesajını yazıp mail mail mail mail programını başlatacağız. Tahmin edeceğiniz gibi, echo echo echo echo komutu, parametresini standart çıktı birimine aynen tekrarlar.

Eğer, w listesinin uzunluğu sıfırdan büüyükse, ilgilendiğimiz kullanıcı en az bir iş yapıyor demektir. Bu durumda, ( else else else else ) ..... sistemde... ..... sistemde... ..... sistemde... ..... sistemde... Gorusebilirsiniz... Gorusebilirsiniz... Gorusebilirsiniz... Gorusebilirsiniz... mesajını yazıp talk talk talk talk programını başlatacağız. Yazdığımız bu merhaba programını kullanabilmek için bir kullanıcın adını parametre olarak vermeliyiz; örneğin :

```bash
% merhaba maslan merhaba maslan merhaba maslan merhaba maslan
maslan sistemde degil... mektup gonderiniz... mail programı başlatılır...
```

```bash
% merhaba reyyan merhaba reyyan merhaba reyyan merhaba reyyan
reyyan sistemde... Gorusebilirsiniz... talk programı başlatılır...
```

İşte şimdi UNIX’ce konuşmaya başladık...

İşte şimdi UNIX’ce konuşmaya başladık...

İşte şimdi UNIX’ce konuşmaya başladık...

İşte şimdi UNIX’ce konuşmaya başladık...

Sergio Aragones Daha önce find find find find komutundan bahsederken daha kolay kullanılan bir ff ff ff ff kabuk programından söz etmiş ve bu kabuk programının listesini vermiştim. Şimdi bu ff ff ff ff programını tekrar bir gözden geçirelim.

Önce problemi bir kez daha tanımlayalım : a) ff ff ff ff adlı bir kabuk programı yaratacağız. b) Bu program tek parametre ile kullanılırsa, çalışma dizinimizde ve alt dizinlerinde, parametrede verilen dosyayı arayan find find find find komutunu çalıştıracağız.. c) Eğer program iki parametre ile kullanılırsa, ikinci parametredeki dosyayı birinci parametredeki dizinden başlayarak arayacak bir find find find find komutu çalıştıracağız. d) Programın parametresiz ya da ikiden fazla parametre ile kullanılmasına izin vermeyeceğiz.

```bash
#!/bin/sh #!/bin/sh #!/bin/sh #!/bin/sh case $# in case $# in case $# in case $# in 1) find . -name "$1" -print;; 1) find . -name "$1" -print;; 1) find . -name "$1" -print;; 1) find . -name "$1" -print;; 2) find "$1" -name "$2" -print;; 2) find "$1" -name "$2" -print;; 2) find "$1" -name "$2" -print;; 2) find "$1" -name "$2" -print;; *) echo "Error. Usage: ff [path] name" *) echo "Error. Usage: ff [path] name" *) echo "Error. Usage: ff [path] name" *) echo "Error. Usage: ff [path] name" echo " ff [path] \"name*\"" echo " ff [path] \"name*\"" echo " ff [path] \"name*\"" echo " ff [path] \"name*\"" echo " ff [path] \"*name\"" echo " ff [path] \"*name\"" echo " ff [path] \"*name\"" echo " ff [path] \"*name\"" esac esac esac esac
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 146

Bu programın birinci satırındaki #!/bin/sh #!/bin/sh #!/bin/sh #!/bin/sh özel bir kalıptır. Bir kabuk programı bu kalıpla başladığı zaman; satırların yorumlanması sırasında mutlaka sh sh sh sh kabuk programının kullanılacağını belirtir. Kullanıcı csh csh csh csh kabuğunu kullanıyor olsa bile, bu satırı görünce UNIX, sh sh sh sh kabul programını başlatır, kabuk programı bitince de sh sh sh sh kabuğunu öldürür.

İkinci satır olan case $# in case $# in case $# in case $# in yapısal programlama dillerinin tamamında bulunan case case case case deyimlerinin aynısıdır. $# $# $# $# sembolu komut verildiğinde kullanılmış olan parametre sayısıdır.

1) find . -name "$1" –print;; 1) find . -name "$1" –print;; 1) find . -name "$1" –print;; 1) find . -name "$1" –print;; satırı, parametre sayısının 1 olması durumunda çalıştırılacak komutu tanımlamaktadır. Bu satırdaki "$1", "$1", birinci "$1", "$1", parametrenin aynen buraya yerleştirileceği anlamındadır. Örneğin programımızı ff aranan ff aranan ff aranan ff aranan şeklinde çalıştırmışsak, kabuk programımız bunun yerine, find . -name aranan -print find . -name aranan -print find . -name aranan -print find . -name aranan -print komutunu çalıştıracaktır 2) find "$1" -name "$2" –print;; 2) find "$1" -name "$2" –print;; 2) find "$1" -name "$2" –print;; 2) find "$1" -name "$2" –print;; satırı, parametre sayısının iki olması "$1" ve "$2" "$2" "$2" "$2" "$1" "$1" durumunda çalıştırılacak komutu tanımlamaktadır. Bu satırdaki "$1" birinci ve ikinci parametrelerin yerleştirileceği pozisyonları göstermektedir.

Örneğin programımızı ff basla aranan ff basla aranan ff basla aranan ff basla aranan şeklinde çalıştırmışsak, kabuk programımız bunun yerine, find basla -name aranan -print find basla -name aranan -print find basla -name aranan -print find basla -name aranan -print komutunu çalıştıracaktır.

\*) echo "Error. Usage: ff \[path\] name" \*) echo "Error. Usage: ff \[path\] name" \*) echo "Error. Usage: ff \[path\] name" \*) echo "Error. Usage: ff \[path\] name" echo " ff \[path\] \\"name\*\\"" echo " ff \[path\] \\"name\*\\"" echo " ff \[path\] \\"name\*\\"" echo " ff \[path\] \\"name\*\\"" echo " ff \[path\] \\"\*name\\"" echo " ff \[path\] \\"\*name\\"" echo " ff \[path\] \\"\*name\\"" echo " ff \[path\] \\"\*name\\"" satırlarıysa, parametre sayısının 1 ve 2 dışında bir değerde olması durumunda çalıştırılacak komutları tanımlamaktadır. Böyle bir durumda ekrana Error. Usage: ff \[path\] name Error. Usage: ff \[path\] name Error. Usage: ff \[path\] name Error. Usage: ff \[path\] name ff \[path\] \\"name\*\\"" ff \[path\] \\"name\*\\"" ff \[path\] \\"name\*\\"" ff \[path\] \\"name\*\\"" ff \[path\] \\"\*name\\"" ff \[path\] \\"\*name\\"" ff \[path\] \\"\*name\\"" ff \[path\] \\"\*name\\"" mesajları verilecek ve kullanıcı; hatasından dolayı uyarılmasının yanısıra, UNIX geleneklerine uygun bir desende programın doğru kullanım kalıbı konusunda da aydınlatılacaktır.

En sondaki esac esac esac esac kelimesiyse, case case case case deyiminin sonunu belirlemektedir.

Kendi geliştirdiğimiz bu komutun kullanımına ilişkin birkaç örnek vermek gerekirse... ff kitaplar ff kitaplar ff kitaplar ff kitaplar Çalışma dizini ve altındaki dizinlerde kitaplar kitaplar kitaplar kitaplar adlı dosya veya dizini ara. ff /usr kitaplar ff /usr kitaplar ff /usr kitaplar ff /usr kitaplar /usr dizini ve altındaki dizinlerde kitaplar kitaplar kitaplar kitaplar adlı dosya veya dizini ara.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 147

ff "kitap\*" ff "kitap\*" ff "kitap\*" ff "kitap\*" Çalışma dizini ve altındaki dizinlerde, adı kitap kitap kitap kitap karakterleriyle başlayan dosya veya dizinleri ara. ff /etc "\*kitap\*" ff /etc "\*kitap\*" ff /etc "\*kitap\*" ff /etc "\*kitap\*" /etc dizini ve altındaki dizinlerde, adının içinde kitap kitap kitap kitap karakteri geçen dosya veya dizinleri ara.

Aynı işi yapmak üzere bir csh csh csh csh kabuk programı yazacak olsaydık

Aynı işi yapmak üzere bir

Aynı işi yapmak üzere bir

Aynı işi yapmak üzere bir

kabuk programı yazacak olsaydık

kabuk programı yazacak olsaydık

kabuk programı yazacak olsaydık

```bash
#!/bin/csh #!/bin/csh #!/bin/csh #!/bin/csh if ("$#argv" == 1) then if ("$#argv" == 1) then if ("$#argv" == 1) then if ("$#argv" == 1) then find . -name "$argv[1]" -print find . -name "$argv[1]" -print find . -name "$argv[1]" -print find . -name "$argv[1]" -print
endif endif endif endif
if ("$#argv" == 2) then if ("$#argv" == 2) then if ("$#argv" == 2) then if ("$#argv" == 2) then find "$argv[1]" -name "$argv[2]" -print find "$argv[1]" -name "$argv[2]" -print find "$argv[1]" -name "$argv[2]" -print find "$argv[1]" -name "$argv[2]" -print
endif endif endif endif
if ("$#argv" < 1 || "$#argv" > 2) then if ("$#argv" < 1 || "$#argv" > 2) then if ("$#argv" < 1 || "$#argv" > 2) then if ("$#argv" < 1 || "$#argv" > 2) then echo "Error. Usage: ff [path] name" echo "Error. Usage: ff [path] name" echo "Error. Usage: ff [path] name" echo "Error. Usage: ff [path] name" echo ' ff [path] "name*" ' echo ' ff [path] "name*" ' echo ' ff [path] "name*" ' echo ' ff [path] "name*" ' echo ' ff [path] "*name" ' echo ' ff [path] "*name" ' echo ' ff [path] "*name" ' echo ' ff [path] "*name" '
endif endif endif endif
```

Bu programı yazarken kullanıdığım bazı önemli kavramlar :

"$#argv" "$#argv" "$#argv" "$#argv" Komutu verirken kullanılan parametrelerin sayısı "$argv\[1\]" "$argv\[1\]" "$argv\[1\]" "$argv\[1\]" Komut satırındaki ilk parametre Sanırım kabuk programlama hakkında bu kadar tanıtma yeter.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 148

Çevreyi Tanı yalı m

Çevreyi Tanı yalı m

Çevreyi Tanı yalı m

Çevreyi Tanı yalı m

İyi bir bilgisayar kullanıcısı elinin altındaki kaynakları tanımalı, o kaynakların kuvvetli ve zayıf taraflarının yanısıra kullanım alanlarını iyi bilmelidir. UNIX için bu tanıma süreci, PC’lere göre oldukça uzun sürer. Sanıldığının aksine, bu gecikme UNIX’in zorluğundan değil, büyüklüğünden kaynaklanmaktadır. Ehhh, tabi, büyük olunca da biraz da karmaşık oluyor ama genede öğrenilemeyecek kadar değil.

Hangi UNIX bilgisayarında olursa olsun; bir terminalin başına geçip, login login login login etmeyi başarıp, ‘ne var, ne yok!’ ‘ne var, ne yok!’ ‘ne var, ne yok!’ ‘ne var, ne yok!’ anlamında bir "ls /" ls /" ls /" ls /" çektiğinizde aşağı yukarı aynı listeyle karşılaşırsınız.

```bash
abc:/home/ayfer> ls / ls / ls / ls / Mail/ etc/ lost+found/ sys/ bin@ export/ mnt/ tmp/ boot home/ pcfs/ usr/ cdrom/ kadb* quotas var/ dev/ lib@ sbin/ vmunix*
abc:/home/ayfer>
```

- Bu örnek liste, BSD UNIX (SUNOS 4.1.1) işletim sistemiyle çalışan, DTK marka bir SPARC iş istasyonundan alınmıştır.

Bu listedeki bir takım dizinler, kullanım amacı açısından tüm UNIX’lerde standarttır. Şimdi bu dizinlere teker teker bir göz atalım...

Dizin Dizin Dizin Dizin Kullanım Amacı

Kullanım Amacı

Kullanım Amacı

Kullanım Amacı

Mail/ Mail/ Mail/ Mail/ Kullanıcılara gelen elektronik posta mesajlarının toplandığı dizin. Normal olarak kullanıcıların bu dizine doğrudan hiç bir erişim hakkı bulunmaz.

Kullanıcılara gelen mesajların, mail yazılımı tarafından kendi home dizinlerine dağıtımı bu dizinden yapılır. bin@ bin@ bin@ bin@ UNIX komutlarının büyük bir çoğunluğunu oluşturan programların yer aldığı dizin. boot boot boot boot Pek standart bir dosya değil. Bu sisteme özgü olsa gerek.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 149

cdrom/ cdrom/ cdrom/ cdrom/ CD-ROM sürücüsü kullanıldığında, sürücüye takılı olan CD üzerindeki dosya sisteminin mount mount mount mount edileceği boş bir dizin. (mount point) (mount point) (mount point) (mount point) dev/ dev/ dev/ dev/ UNIX bilgisayarına bağlı olan ve bağlanabilecek tüm donanım unsurlarının işletim sisteminin çekirdek modülü (kernel kernel kernel kernel) ile bağlantısının kurulmasını sağlayan özel dosyamsı dosyamsı kayıtların yer aldığı dizin. dosyamsı dosyamsı (Bu dizinin altındakiler, ne birer dosya ne de birer dizindir, o yüzden “dosyamsı” sözcüğünü kullandım). etc/ etc/ etc/ etc/ Sistem yöneticisinin eli ayağı olan dosyaların bulunduğu dizindir. Kullanıcıların ve şifrelerinin tanıtıldığı dosya (passwd passwd passwd passwd), bilgisayar ağıyla ilgili tanıtım kayıtlarının bulunduğu dosyalar (hosts hosts hosts hosts, defaultdomain defaultdomain defaultdomain defaultdomain vs) sistemin açılışı sırasında çalıştırılacak olan kabuk programları (rc\* rc\* rc\* rc\*), yazıcı tanımları (printcap printcap printcap printcap), terminal bağlantıları ile ilgili kontrol dosyaları (termcap termcap termcap termcap, ttytab ttytab ttytab ttytab vs), sistemdeki disklerin mount mount mount mount edilmeleri ile ilgili tanıtım dosyası (fstab fstab fstab fstab), kullanıcılara yapılacak duyurunun yer aldığı dosya (motd motd motd motd) hep bu dizindedir. Bu dizinin başına bir kaza gelirse, o sistem bir daha kolay kolay ayağa kalkamaz. export/ export/ export/ export/ Bu bilgisayarın disklerinden yararlanarak işletim sistemini yükleyen başka disksiz bilgisayarlar bulunduğu durumlarda kullanılan disk sahalarıdır. home/ home/ home/ home/ Kullanıcıların home home home home dizinlerinin bulunduğu dizindir. kadb\* kadb\* kadb\* kadb\* “adb like standalone kernel debugger” “adb like standalone kernel debugger” “adb like standalone kernel debugger” “adb like standalone kernel debugger” (ne demekse...) lib@ lib@ lib@ lib@ Standart UNIX kütüphanelerinin bulunduğu dizine (/usr/lib /usr/lib /usr/lib /usr/lib) bir bağlantı (ln ln ln ln komutunu hatırlayınız).

(Bağlantı (link) olduğunu @ @ @ @ karakterinden anlıyoruz.)

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 150

lost+found/ lost+found/ lost+found/ lost+found/ Bilgisayarın kurallara uygun bir şekilde törenle (!) kapatılmadığı veya disklerde bir arıza olduğunda yapılan kontrollerde (fsck : file system check fsck : file system check fsck : file system check fsck : file system check) gerçek adı ve yeri bulunamayan dosya parçalarının toplandığı dizin. Buraya düşen dosyalar pek kolay kurtarılamazlar. (MS-DOS’daki FILE0001.CHK gibi). mnt/ mnt/ mnt/ mnt/ Çeşitli disk/disket/CDROM gibi çevre birimlerinin mount mount mount mount edilmesi için genel amaçlı bir boş dizin.

(mount point mount point mount point mount point) pcfs/ pcfs/ pcfs/ pcfs/ MS-DOS formatlı disketlerin mount mount mount mount edilmesi için boş bir dizin. quotas quotas quotas quotas Kullanıcıların disk kullanma kotalarının tanıtıldığı dosya. sbin/ sbin/ sbin/ sbin/ Marka ve donanıma bağımlı bazı sistem komutlarına ait dosyaların bulunduğu dizin. sys/ sys/ sys/ sys/ Marka ve donanıma bağımlı UNIX modüllerinde değişiklik yapmak gerektiğinde kullanılacak dosya ve dizinlerin bulunduğu dizin. tmp/ tmp/ tmp/ tmp/ Uygulama programları ve kullanıcılar tarafından yaratılan geçici dosyalar için ayrılmış bir dizin. Bu dizinin içindeki dosya ve alt dizinler, sistemin her açılışında otomatik olarak silinir. usr/ usr/ usr/ usr/ Uygulama programları, derleyiciler, standart yazılım kütüphaneleri gibi ortak kullanımda olan programların yerleştirildiği dizindir. var/ var/ var/ var/ Sistemde meydana gelen önemli olaylarla ilgili log log log log dosyalarının (syslog syslog syslog syslog, messages messages messages messages gibi) saklandığı dizin . vmunix\* vmunix\* vmunix\* vmunix\* UNIX işletim sisteminin çekirdek programı (kernel kernel kernel kernel).

Sistem açıldığında belleğe ilk olarak bu program yüklenir.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 151

/dev Dizini /dev Dizini /dev Dizini /dev Dizini Yukarıda listelenen dizinler arasında /dev /dev /dev /dev özel açıklamalar gerektirmektedir.

Bu dizinde yer alan dosyalar aslında tam anlamıyla birer dosya değildir. Dizin altında isimleri bulunmakla birlikte, diskte hiç yer harcamazlar hiç yer harcamazlar hiç yer harcamazlar hiç yer harcamazlar. Bu özelliklerinden dolayı /dev /dev /dev /dev dizini altında yer alan kayıtlara dosya değil; düğüm

düğüm

düğüm

düğüm

(node node node node) adı verilir.

Bu düğümlerin her birinin birer Major Major Major Major ve birer Minor Minor Minor Minor numaraları vardır. Bir UNIX komutu, ya da uygulama programı, /dev /dev /dev /dev dizininde yer alan bir isim aracılığıyla bir donanım unsuruna ulaşmak istediğinde (örneğin, teybe bir kayıt işlemi için /dev/rst0 /dev/rst0 /dev/rst0 /dev/rst0 düğümüne ulaştığında), UNIX, bu major-minor numaralar aracılığı ile çekirdek programın hangi modülünün harekete geçirileceğini anlayacak ve kontrolu, o donanım unsurunu tüm özellikleriyle tanıyıp denetleyebilen bir programa geçirecektir (device driver device driver device driver device driver).

Tipik bir UNIX bilgisayarının /dev /dev /dev /dev dizininde yüzlerce düğüm yer alır. Ben bu kitapta bunlardan sadece bir kaç tanesinden söz etmek istiyorum. Hem hepsini anlatmaya imkan ve gerek yok; hem de bu /dev /dev /dev /dev dizininin yapısı gerek kullanılan UNIX’in tipine, gerekse bilgisayarın üreticisinin tercihlerine bağlı olarak büyük farklılıklar göstermektedir; ancak kullanım mantığı temelde hepsinde aynıdır. /dev /dev /dev /dev dizininden söz ederken SUN Micro Systems firmasınca geliştirilen, BSD uyumlu SunOS 4.1.x UNIX’de kullanıldığı şekliyle söz edeceğim.

/dev Dizininde Yer Alan Bazı Dü ğ ümler

/dev Dizininde Yer Alan Bazı Dü ğ ümler

/dev Dizininde Yer Alan Bazı Dü ğ ümler

/dev Dizininde Yer Alan Bazı Dü ğ ümler

Düğüm Düğüm Düğüm Düğüm

Tanımladığı Donanım Unsuru

Tanımladığı Donanım Unsuru

Tanımladığı Donanım Unsuru

Tanımladığı Donanım Unsuru

/dev/console /dev/console /dev/console /dev/console Bilgisayarın ana ekranı (ya da ana terminali).

Sistemde ortaya çıkan donanım sorunları ve diğer önemli olaylara ilişkin mesajlar bu donanım birimine gönderilir.

/dev/mem /dev/mem /dev/mem /dev/mem Sistemin ana belleği /dev/kbd /dev/kbd /dev/kbd /dev/kbd Sistem konsolunun klavyesi /dev/mouse /dev/mouse /dev/mouse /dev/mouse Sistem konsolunun mouse mouse mouse mouse birimi

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 152

/dev/null /dev/null /dev/null /dev/null Hiç bir yere bağlı olmayan, “kara delik” gibi bir düğüm. Buraya her şeyi kopyalayabilirsiniz. Hiç bir zaman dolmaz; ama buraya kopyalananlar da hiç bir zaman geri gelmez. Bir programın çıktılarını merak etmiyor ve hiç bir şekilde gerek duymuyorsanız, programı çalıştırırken, standart çıktı birimini bu düğüme yönlendirebilirsiniz. komut > /dev/null komut > /dev/null komut > /dev/null komut > /dev/null gibi /dev/rst0 /dev/rst0 /dev/rst0 /dev/rst0 Sistemdeki ilk teyp birimi (işi bitince kaseti başa

işi bitince kaseti başa

işi bitince kaseti başa

işi bitince kaseti başa

saracak şekilde kullanım için) ( r r r r : rewind)

saracak şekilde kullanım için

saracak şekilde kullanım için

saracak şekilde kullanım için

/dev/rst1 /dev/rst1 /dev/rst1 /dev/rst1 Sistemdeki ikinci teyp birimi (işi bitince kaseti başa

işi bitince kaseti başa

işi bitince kaseti başa

işi bitince kaseti başa

saracak şekilde kullanım için)

saracak şekilde kullanım için

saracak şekilde kullanım için

saracak şekilde kullanım için

/dev/nrst0 /dev/nrst0 /dev/nrst0 /dev/nrst0 Gene sistemdeki ilk teyp birimi; ancak bu kez; işi bitince kaseti başa sarmayacak şekilde kullanılması söz konusu.

( n n n n : no rewind). Bir kasete peşpeşe dosyalar kaydedileceği zaman ya da bir kasette peşpeşe kayıtlı dosyalar okunacağı zaman bu düğüm kullanılmalıdır.

/dev/sd0a /dev/sd0a /dev/sd0a /dev/sd0a Sistemdeki ilk diskin a a a a adı verilmiş bölümü (a a a a

partition partition partition partition)

/dev/sd0b /dev/sd0b /dev/sd0b /dev/sd0b Sistemdeki ilk diskin b b b b adı verilmiş bölümü (b b b b

partition partition partition partition)

/dev/sd1h /dev/sd1h /dev/sd1h /dev/sd1h Sistemdeki ikinci ikinci ikinci ikinci diskin h h h h adı verilmiş bölümü (h h h h

partition partition partition partition)

/dev/sr0 /dev/sr0 /dev/sr0 /dev/sr0 Sistemdeki ilk CD-ROM sürücü okuyucusu /dev/fd0 /dev/fd0 /dev/fd0 /dev/fd0 Sistemdeki ilk disket sürücü birimi (üzerinde UNIX veya MSDOS formatlı disket takılıyken).

/dev/rfd0 /dev/rfd0 /dev/rfd0 /dev/rfd0 formatsız formatsız formatsız Sistemdeki ilk disket sürücü (üzerinde formatsız disket takılıyken) (r r r r : raw device ) /dev/ttya /dev/ttya /dev/ttya /dev/ttya Sistemdeki birinci seri arabirim (RS232) /dev/ttyb /dev/ttyb /dev/ttyb /dev/ttyb Sistemdeki ikinci seri arabirim (RS232) /dev/bpp0 /dev/bpp0 /dev/bpp0 /dev/bpp0 Sistemdeki ilk paralel yazıcı arabirimi (Centronics)

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 153

/dev/ttyp0 /dev/ttyp0 /dev/ttyp0 /dev/ttyp0 Ethernet üzerinden bağlanan terminal emülatörleri için sanal seri arabirimlerden ilki (pseudo tty port pseudo tty port pseudo tty port pseudo tty port).

/dev/ttyp1 /dev/ttyp1 /dev/ttyp1 /dev/ttyp1 Ethernet üzerinden bağlanan terminal emülatörleri için sanal seri arabirimlerden ikincisi ikincisi ikincisi ikincisi (pseudo tty port).

/dev/le0 /dev/le0 /dev/le0 /dev/le0 Sistemin ilk Ethernet Arabirimi /dev/le1 /dev/le1 /dev/le1 /dev/le1 Sistemin ikinci Ethernet Arabirimi Yukarıdaki /dev /dev /dev /dev düğümleri sadece birer örnektir. Her UNIX bilgisayarında aynen bulunmaları gerekmez. Örneğin, SVR4 UNIX’lerde diskleri tanımlayan düğümler /dev/dsk/c0t0d0s3 /dev/dsk/c0t0d0s3 /dev/dsk/c0t0d0s3 /dev/dsk/c0t0d0s3 gibi isimlerle anılırlar.

Gerek duydukça, sizin sisteminizde tanımlı olan /dev düğüm isimlerini ve nasıl kullanılacaklarını sistem yöneticinizden öğrenebilirsiniz. Eğer sistem yöneticisi sizseniz, bilgisayarınızın dökümantasyonunda yeterli açıklamaları bulacağınıza inanıyorum.

mount Komutu Üzerine Çeşitlemeler

mount Komutu Üzerine Çeşitlemeler

mount Komutu Üzerine Çeşitlemeler

mount Komutu Üzerine Çeşitlemeler

Aslında, mount mount mount mount, daha çok sistem yöneticilerinin kullandığı bir komut olmakla birlikte, normal kullanıcıları da yakından ilgilendirmektedir.

Şöyle kısa bir hatırlatma yapmak gerekirse; mount mount mount mount komutu, dosya sistemlerini (file systems) birbirlerine bağlamakta kullanılır. Örneğin, bir bilgisayardaki ikinci disk sürücüsünü / / / / altında bir dosya sistemine iliştirmek için; bir CD-ROM sürücüsüne takılı olan CD’yi okuyabilmek amacıyla /dev/sr0 /dev/sr0 /dev/sr0 /dev/sr0 düğümünü / / / / altında bir yerlere mount mount mount mount etmek için kullanılır. mount mount mount mount komutunu detaylı olarak açıklamaya başlamadan önce, SunOS 4.1.x UNIX işletim sisteminin bakış açısıyla disklerin yapılarından söz etmek istiyorum. Aslında tüm UNIX’ler diskleri SunOS’inkine benzer bir yapıda görmek isterler.

UNIX bilgisayarlarında kullanılan diskler genellikle SCSI SCSI SCSI SCSI (Small Computer Standard Interface) arabirimine sahiptir. Bu arabirimin bir özelliği olarak her diskin 0 ile 7 arasında bir adresi olmalıdır. (Sizin bilgisayarınızda bu 8 adresten hangilerinin diskler için kullanılabileceğini sistem dökümantasyonuna bakarak öğrenebilirsiniz.)

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 154

Birden fazla diski olan bilgisayarlarda, disklerden bir tanesi Sistem Diski Sistem Diski Sistem Diski Sistem Diski olarak tanımlanmalıdır. Sistem diski Sistem diski Sistem diski Sistem diski olarak seçilen disk, işletim sisteminizin özelliklerine bağlı olarak bir kaç bölüme (partition partition partition partition) ayrılmış olmalıdır. Örneğin

SunOS 4.1.1

SunOS 4.1.1

SunOS 4.1.1

SunOS 4.1.1 de, sistem diski en az 3, en fazla 7 bölüme ayrılabilir. Her bir bölümün bir bölüm adı (ya da numarası) olmalıdır. Varsa, diğer disklerin bölümlere ayrılıp ayrılmaması, sistem yöneticisinin tercihine bırakılmıştır.

Disklerdeki bu bölümlerin, üzerlerinde bulundukları disklerin SCSI adresleri ve bölüm numaralarına göre verilmiş birer ismi olmalıdır ve bu isimler /dev /dev /dev /dev dizininde birer düğüm düğüm (node) olarak yer almalıdır. Örneğin

düğüm

düğüm

BSD UNIX’de DİSK İSİMLENDİRME SİSTEMİ

BSD UNIX’de DİSK İSİMLENDİRME SİSTEMİ

BSD UNIX’de DİSK İSİMLENDİRME SİSTEMİ

BSD UNIX’de DİSK İSİMLENDİRME SİSTEMİ

/dev/sd0a /dev/sd0a /dev/sd0a /dev/sd0a SCSI adresi, sistemdeki sıfırıncı (ilk) diske karşılık gelen diskin a a a a isimli bölümü /dev/sd1c /dev/sd1c /dev/sd1c /dev/sd1c SCSI adresi, sistemdeki bir numaralı (ikinci) diske karşılık gelen diskin c c c c isimli bölümü /dev/sd3h /dev/sd3h /dev/sd3h /dev/sd3h SCSI adresi, sistemdeki 3 numaralı diske karşılık gelen diskin h h h h isimli bölümü

SVR4 UNIX’de DİSK İSİMLENDİRME SİSTEMİ

SVR4 UNIX’de DİSK İSİMLENDİRME SİSTEMİ

SVR4 UNIX’de DİSK İSİMLENDİRME SİSTEMİ

SVR4 UNIX’de DİSK İSİMLENDİRME SİSTEMİ

/dev/dsk/c0t0d0s0 /dev/dsk/c0t0d0s0 /dev/dsk/c0t0d0s0 /dev/dsk/c0t0d0s0 Sistemdeki ilk disk kontrol birimine bağlı olan (c0 c0 c0 c0), SCSI adresi 0 olan (t0 t0 t0 t0), bu adresteki ilk sürücü olan (d0 d0 d0 d0) diskin ilk bölümü (s0 s0 s0 s0). c : channel t : target d : drive s : slice /dev/dsk/c0t1d0s3 /dev/dsk/c0t1d0s3 /dev/dsk/c0t1d0s3 /dev/dsk/c0t1d0s3 Bu da günün bilmecesi...

Şimdi, bu disk yapılandırma mantığı çerçevesinde, bilgisayarımızda iki adet disk birimi olduğunu ve aşağıdaki şekilde bölümlendirildiklerini varsayalım :

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 155

Bu durumda, disk bölümlerini BSD UNIX altında, /dev /dev /dev /dev isimleri şöyle olur :

Sıfırıncı disk : /dev/sd0a /dev/sd0a /dev/sd0a /dev/sd0a Birinci disk :

/dev/sd1c /dev/sd1c /dev/sd1c /dev/sd1c /dev/sd0b /dev/sd0b /dev/sd0b /dev/sd0b /dev/sd0g /dev/sd0g /dev/sd0g /dev/sd0g /dev/sd0h /dev/sd0h /dev/sd0h /dev/sd0h Bu disk bölümlerinin UNIX altında kullanılabilmeleri için birer mount mount mount mount noktasına mount mount mount mount edilmeleri gerekir. Sistemin açılışı sırasında (/etc/fstab /etc/fstab /etc/fstab /etc/fstab) dosyasında belirtildiği şekilde mount mount mount mount işlemleri otomatik olarak yapılır. SunOS 4.1.1 altında, genellikle /dev/sd0a /dev/sd0a /dev/sd0a /dev/sd0a / / / / /dev/sd0g /dev/sd0g /dev/sd0g /dev/sd0g /usr /usr /usr /usr /dev/sd0h /dev/sd0h /dev/sd0h /dev/sd0h /home /home /home /home mount noktalarına mount mount mount mount edilirler. /dev/sd0b /dev/sd0b /dev/sd0b /dev/sd0b özel bir şekilde swap swap swap swap alanı olarak kullanılır; o nedenle mount mount mount mount edilmez. (swap alanı : ana belleğin yetmediği durumlarda, sistemi çok yavaşlatma pahasına da olsa; belleğin uzantısıymış gibi kullanılan disk alanı).

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 156

Şimdi, root root root root kullanıcının (mount mount mount mount komutunu sadece root root root root kullanıcı kullanabilir) bilgisayarımızın ikinci diskini de devreye sokabilmek için neler yapması gerektiğini bir gözden geçirelim.

İkinci diskimiz (sd1c sd1c sd1c sd1c) ayrı bir dosya sistemine (file system file system file system file system) sahip olmalı; yani UNIX kurallarına uygun olarak formatlanmış ve mkfs mkfs mkfs mkfs (make file system) veya newfs newfs newfs newfs (new file system) komutu kullanılarak üzerinde bir dosya sistemi yaratılmış olmalıdır. Bu formatlama ve dosya sistemi yaratma işi sadece bir sadece bir sadece bir sadece bir kez kez kez kez, diskin bilgisayara ilk takıldığı zaman yapılmalıdır. Her iki işlem de (format format format format ve mkfs mkfs mkfs mkfs) disk üzerindeki kayıtları tamamen silen işlemlerdir.

Eğer diskimiz hazırsa, root root root root kullanıcı, bu diski, / / / / dosya sisteminde hangi dizin altında görmek istediğine karar vermelidir. Örneğimizde bu dizin /disk2 /disk2 /disk2 /disk2 olsun.

(Pekala /usr/disk2 /usr/disk2 /usr/disk2 /usr/disk2 veya /home/ugur2 /home/ugur2 /home/ugur2 /home/ugur2 de olabilirdi...) Sonra, / / / / dizini (birinci diskin a bölümü : /dev/sd0a) altında disk2 disk2 disk2 disk2 isimli boş boş bir boş boş dizin bulunduğuna emin olmalıdır. Eğer bu isimde bir dizin yoksa, mkdir mkdir mkdir mkdir /disk2 /disk2 /disk2 /disk2 komutu iş görecektir. (Hatırlatayım; bu işleri ancak root root root root kullanıcı yapabilir).

Son olarak mount mount mount mount noktası (mount point)

```bash
# mount /dev/sd1c /disk2 # mount /dev/sd1c /disk2 # mount /dev/sd1c /disk2 # mount /dev/sd1c /disk2
```

komutuyla mount mount mount mount işlemini gerçekleştirir. Artık ikinci disk birimi bilgisayarın dosya yapısına entegre oldu ve tüm kullanıcılara / / / / dizininin altında disk2 disk2 disk2 disk2 isimli bir dizin olarak görünüyor. Normal koşullarda kullanıcıların, sistemde gördükleri dizinlerin birer disk birimi mi, yoksa disk bölümü mü, yoksa basit birer dizin mi olduklarını bilmeleri gerekmez. Ancak, sistem yöneticisinin tüm bu olup bitenlerden haberi olmalıdır.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 157

Eğer kullandığınız bilgisayardaki disklerin (veya disk bölümlerinin nasıl bir düzen içinde ve nerelere mount mount mount mount edildiklerini öğrenmek isterseniz, mount mount mount mount komutunu parametresiz olarak kullanabilirsiniz.

```bash
abc:/home/ayfer> mount mount mount mount /dev/sd0a on / type 4.2 (rw,quota) /dev/sd0g on /usr type 4.2 (rw) /dev/sd0h on /home type 4.2 (rw,quota)
abc:/home/ayfer>
```

Bu listeden öğrendiklerimiz şunlar : a) Sistemde sadece bir disk var ( ikinci disk varsa bile, mount mount mount mount edilmemiş).

Çünkü disk isimlerinin hepsi sd0 sd0 sd0 sd0 ile başlıyor. b) İlk diskin a a a a bölümü / / / / olarak, g g g g bölümü /usr /usr /usr /usr olarak, h h h h bölümüyse /home /home /home /home olarak mount mount mount mount edilmiş. c) Tüm disk bölümlerindeki dosya yapılarının tipi 4.2 imiş. (SunOS tarafından dosya yapısı sürüm numarasıyla (version) ilgili olarak kullanılan özel bir kod). d) Disk bölümlerinin hepsi okuma ve yazmaya açıkmış (rw rw rw rw). (Bu dosya sistemindeki dosya ve dizinlerin kullanıcı yetki kalıplarında belirtilen yetkiler saklı kalmak kaydıyla). e) / / / / ve /home /home /home /home dizinlerinin kullanımında kullanıcılara kota kota kota kota uygulanıyormuş. Yani, kullanıcılar kendilerine ayrılmış olan kotadan daha büyük disk alanı işgal edecek şekilde dosya açamayacaklar.

Bir bilgisayardaki disklerin ve disk bölümlerinin, sistemin açılışı sırasında otomatik olarak nerelere mount mount mount mount edileceğini sistem yöneticileri /etc/fstab /etc/fstab /etc/fstab /etc/fstab dosyasında belirtirler. Böylece sistemin her açılışında, dosya sistemlerini tek tek mount mount mount mount etmekten kurtulurlar.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 158

Tipik bir /etc/fstab /etc/fstab /etc/fstab /etc/fstab dosyasında

```bash
/dev/sd0a / 4.2 rw 1 1 /dev/sd0a / 4.2 rw 1 1 /dev/sd0a / 4.2 rw 1 1 /dev/sd0a / 4.2 rw 1 1 /dev/sd0h /home 4.2 rw 1 3 /dev/sd0h /home 4.2 rw 1 3 /dev/sd0h /home 4.2 rw 1 3 /dev/sd0h /home 4.2 rw 1 3 /dev/sd0g /usr 4.2 rw 1 2 /dev/sd0g /usr 4.2 rw 1 2 /dev/sd0g /usr 4.2 rw 1 2 /dev/sd0g /usr 4.2 rw 1 2
```

satırları bulunur.

BSD UNIX’lerdeki /etc/fstab /etc/fstab /etc/fstab /etc/fstab dosyasının görevini, SVR4 UNIX’lerde /etc/vfstab /etc/vfstab /etc/vfstab /etc/vfstab dosyası üstlenmiştir. /etc/vfstab /etc/vfstab /etc/vfstab /etc/vfstab dosyasındaki satır desenleri biraz farklı olmakla beraber, /etc/fstab /etc/fstab /etc/fstab /etc/fstab ile aynı mantıkta düzenlenmişlerdir.

Bu açıklamalardan sonra, günlük hayatta rastlanan mount mount mount mount uygulamalarına örnekler vermek istiyorum.

- Bir disk bölümünü salt oku salt oku salt oku salt oku (read only) olarak mount mount mount mount etmek için :

```bash
# mount -r /dev/sd1c /home/disk2 # mount -r /dev/sd1c /home/disk2 # mount -r /dev/sd1c /home/disk2 # mount -r /dev/sd1c /home/disk2
# mount -o ro /dev/dsk/c0t1d0s2 /home/disk2 # mount -o ro /dev/dsk/c0t1d0s2 /home/disk2 # mount -o ro /dev/dsk/c0t1d0s2 /home/disk2 # mount -o ro /dev/dsk/c0t1d0s2 /home/disk2
```

mount mount mount mount komutunu kullanabilmek için root root root root kullanıcı olmanız gerekir.

- xyz xyz xyz xyz isimli bir başka bilgisayarın (doğal olarak, bizim bilgisayarımızla aynı bilgisayar ağında bulunmak kaydıyla) bir dizinini, kendi bilgisayarımızdaki bir dizine mount mount mount mount etmek için :

```bash
# mount -t nfs xyz:/home /home2 # mount -t nfs xyz:/home /home2 # mount -t nfs xyz:/home /home2 # mount -t nfs xyz:/home /home2
# mount -F nfs xyx:/home /home2 # mount -F nfs xyx:/home /home2 # mount -F nfs xyx:/home /home2 # mount -F nfs xyx:/home /home2
```

- Üzerinde UNIX dosya sistemi olan bir disketi mount mount mount mount etmek için :

```bash
# mount /dev/fd0 /mnt # mount /dev/fd0 /mnt # mount /dev/fd0 /mnt # mount /dev/fd0 /mnt
# mount /dev/diskette /mnt # mount /dev/diskette /mnt # mount /dev/diskette /mnt # mount /dev/diskette /mnt
```

- Aynı disketin yazmaya karşı koruma deliği açıksa (disket yazmaya karşı korumalıysa) :

```bash
# mount -r /dev/fd0 /mnt # mount -r /dev/fd0 /mnt # mount -r /dev/fd0 /mnt # mount -r /dev/fd0 /mnt
# mount -o ro /dev/diskette /mnt # mount -o ro /dev/diskette /mnt # mount -o ro /dev/diskette /mnt # mount -o ro /dev/diskette /mnt
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 159

- MS-DOS formatlı bir disketi mount mount mount mount etmek için :

```bash
# mount -t pcfs /dev/fd0 /pcfs # mount -t pcfs /dev/fd0 /pcfs # mount -t pcfs /dev/fd0 /pcfs # mount -t pcfs /dev/fd0 /pcfs
# mount -F pcfs /dev/diskette /pcfs # mount -F pcfs /dev/diskette /pcfs # mount -F pcfs /dev/diskette /pcfs # mount -F pcfs /dev/diskette /pcfs
```

- MS-DOS formatlı ve yazmaya karşı korumalı bir disketi mount mount mount mount etmek için :

```bash
# mount -r -t pcfs /dev/fd0 /pcfs # mount -r -t pcfs /dev/fd0 /pcfs # mount -r -t pcfs /dev/fd0 /pcfs # mount -r -t pcfs /dev/fd0 /pcfs
# mount -F pcfs -o ro /dev/diskette /pcfs # mount -F pcfs -o ro /dev/diskette /pcfs # mount -F pcfs -o ro /dev/diskette /pcfs # mount -F pcfs -o ro /dev/diskette /pcfs
```

- ISO 9660 ISO 9660 ISO 9660 ISO 9660 standardında kaydedilmiş bir CD yi mount mount mount mount etmek için ( -r -r -r -r : CD ler her zaman yazmaya karşı korumalıdır) :

```bash
# mount -r /dev/sr0 /cdrom # mount -r /dev/sr0 /cdrom # mount -r /dev/sr0 /cdrom # mount -r /dev/sr0 /cdrom
# mount -o ro /dev/dsk/c0t6d0s2 /cdrom # mount -o ro /dev/dsk/c0t6d0s2 /cdrom # mount -o ro /dev/dsk/c0t6d0s2 /cdrom # mount -o ro /dev/dsk/c0t6d0s2 /cdrom
```

- High Sierra File System High Sierra File System High Sierra File System High Sierra File System standardında kaydedilmiş bir CD yi mount mount mount mount etmek için :

```bash
# mount -r -t hsfs /dev/sr0 /cdrom # mount -r -t hsfs /dev/sr0 /cdrom # mount -r -t hsfs /dev/sr0 /cdrom # mount -r -t hsfs /dev/sr0 /cdrom
# mount -F hsfs -r ro /dev/dsk/c0t6d0s2 /cdrom # mount -F hsfs -r ro /dev/dsk/c0t6d0s2 /cdrom # mount -F hsfs -r ro /dev/dsk/c0t6d0s2 /cdrom # mount -F hsfs -r ro /dev/dsk/c0t6d0s2 /cdrom
```

- xyz xyz xyz xyz isimli bir başka bilgisayarın (doğal olarak, bizim bilgisayarımızla aynı bilgisayar ağında bulunmak kaydıyla) /cdrom /cdrom /cdrom /cdrom dizinine mount mount mount mount edilmiş bir CD-ROM sürücüsünü, kendi bilgisayarımızdaki /cdrom /cdrom /cdrom /cdrom dizinine mount mount mount mount etmek için :

```bash
# mount -t nfs xyz:/cdrom /cdrom # mount -t nfs xyz:/cdrom /cdrom # mount -t nfs xyz:/cdrom /cdrom # mount -t nfs xyz:/cdrom /cdrom
# mount -F nfs xyz:/cdrom /cdrom # mount -F nfs xyz:/cdrom /cdrom # mount -F nfs xyz:/cdrom /cdrom # mount -F nfs xyz:/cdrom /cdrom
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 160

- mount mount mount mount edilmiş bir dosya sistemini, bilgisayarın / / / / dosya sisteminden ayırmak istediğinizde, (bu iş genellikle disket ve CD ler için anlamlıdır) :

```bash
# umount /dev/xxx # umount /dev/xxx # umount /dev/xxx # umount /dev/xxx unmount
```

veya

```bash
# umount /mmm # umount /mmm # umount /mmm # umount /mmm
```

komutu kullanılmalıdır. Burada xxx xxx xxx xxx sürücünün /dev dizinindeki adı; mmm mmm mmm mmm ise mount mount mount mount noktasının noktasının noktasının noktasının adıdır. Bir örnek vermek gerekirse, önceden

```bash
# mount -r -t hsfs /dev/sr0 /cdrom # mount -r -t hsfs /dev/sr0 /cdrom # mount -r -t hsfs /dev/sr0 /cdrom # mount -r -t hsfs /dev/sr0 /cdrom
```

komutuyla mount mount mount mount edilmiş bir CD yi umount umount umount umount etmek için

```bash
# umount /dev/sr0 # umount /dev/sr0 # umount /dev/sr0 # umount /dev/sr0 veya
# umount /cdrom # umount /cdrom # umount /cdrom # umount /cdrom
```

komutlarını kullanabilirsiniz.

mount/umount komutlarının kullanımında dikkat edilmesi

mount/umount komutlarının kullanımında dikkat edilmesi

mount/umount komutlarının kullanımında dikkat edilmesi

mount/umount komutlarının kullanımında dikkat edilmesi

gereken noktalar : gereken noktalar : gereken noktalar : gereken noktalar : mount mount mount mount ve umount umount umount umount komutlar , genellikle tüm UNIX’lerde sadece root root root root kullanıcı tarafından kullanılabilirler.

Bir donanım unsurunun mount mount mount mount edilebilmesi için, üzerinde geçerli bir dosya sistemi bulunmalıdır. Bu yüzden sadece

- formatlı diskler,
- CD’ler,
- formatlı disketler ve
- formatlı Magneto Optik diskler mount mount mount mount edilebilir.

Teyp birimlerinin kullanılmasında mount mount mount mount komutunun kullanılması söz konusu değildir; çünkü teyp kasetleri üzerinde dosya sistemi bulunmaz.

Çalışma diziniz bir mount mount mount mount noktasında, ya da onun altında bir yerlerdeyse; o mount mount mount mount noktasına bağlı sürücüyü umount umount umount umount edemezsiniz. Örneğin, bir CD’yi /cdrom /cdrom /cdrom /cdrom dizinine mount mount mount mount ettiyseniz ve bu CD üzerindeki işlerinizi daha kolay yapmak için cd /cdrom/xyz cd /cdrom/xyz cd /cdrom/xyz cd /cdrom/xyz komutunu verdiyseniz (çalışma dizininiz /cdrom/xyz /cdrom/xyz /cdrom/xyz /cdrom/xyz ise), umount /cdrom umount /cdrom umount /cdrom umount /cdrom komutunu kullanamazsınız. (Kullanmak

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 161

istediğinizde “Device Busy” “Device Busy” “Device Busy” “Device Busy” hata mesajıyla uyrarılırsınız; bindiğiniz dalı kesmenize izin verilmez.) mount mount mount mount edilmiş CD, disket gibi takılıp çıkarılabilen birimleri umount umount umount umount etmeden kesinlikle yuvalarından çıkarmayınız. Zaten bu yüzden, bir çok UNIX bilgisayarında CD ve disket sürücülerin üzerinde CD ve disketi çıkarmak için kullanılan düğme bulunmaz; bulunsa bile içinde mount mount mount mount edilmiş medya bulunuyorsa, düğme çalışmaz. Bu tip sürücülerin içindeki medyayı çıkarabilmek için

```bash
# eject cdrom # eject cdrom # eject cdrom # eject cdrom
# eject floppy # eject floppy # eject floppy # eject floppy
```

gibi komutlar kullanmanız gerekir. Bu komutlar, kullandığınız bilgisayara göre değişebilir.

Çalışan bir sistemde diskleri gerekmedikçe umount umount umount umount etmeyiniz.

Teypleri mount mount mount mount etmek gibi bir kavramın olmadığını aklınızdan çıkarmayınız. Elinde bir kasetle dolaşarak, , , , “Yahu bu teybi nasıl mount edeceğim?” diye soran cahil

“Yahu bu teybi nasıl mount edeceğim?”

“Yahu bu teybi nasıl mount edeceğim?”

“Yahu bu teybi nasıl mount edeceğim?”

bir UNIX kullanıcısı durumuna sakın düşmeyiniz. mount noktası olarak kullanırsanız mount noktası mount noktası İçinde dosya ve alt dizinler olan bir dizini, mount noktası (yani oraya CD, disket, disk gibi bir medya mount ederseniz), UNIX bu isteğinize karşı koymadan mount mount mount mount işlemini gerçekleştirecektir. Ama, medya mount mount mount mount edilmiş olarak kaldığı sürece, dizinin, eskiden altında bulunan dosya ve alt dizinlere ulaşamazsınız.

Senaryolar Senaryolar Senaryolar Senaryolar Şimdi isterseniz MS-DOS formatlı bir disketin içindeki , adı \*.DAT \*.DAT \*.DAT \*.DAT kalıbına uyan dosyaları, UNIX bilgisayarımızda /home/ayfer /home/ayfer /home/ayfer /home/ayfer dizinine kopyalamak için neler yapılması gerektiğine bir göz atalım. (Senaryolar SunOS 4.x.x SunOS 4.x.x SunOS 4.x.x SunOS 4.x.x sahnesinde oynanacak şekilde hazırlanmıştır.)

Öncelikle root root root root kullanıcı olmanız gerekir. Eğitim amaçlı bu senaryoya göre, root root root root şifresini bildiğinizi varsayalım.

Sonra, disketi nereye mount mount mount mount edeceğinize karar vermalisiniz. Bence /disket /disket /disket /disket dizini uygun.. Sonra /disket /disket /disket /disket diye bir dizininin (mount point) bulunup bulunmadığını kontrol etmelisiniz.

```bash
# ls /disket ls /disket ls /disket ls /disket
```

Olumsuz bir mesajla karşılaşmazsanız ve dizin boşsa devam edebilirsiniz. Eğer böyle bir dizin olmadığına ilişkin bir mesaj alırsanız

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 162

```bash
# mkdir /disket mkdir /disket mkdir /disket mkdir /disket
```

komutuyla, dizini yaratabilirsiniz.

Ardından

```bash
# mount -t pcfs /dev/fd0 /disket mount -t pcfs /dev/fd0 /disket mount -t pcfs /dev/fd0 /disket mount -t pcfs /dev/fd0 /disket
```

komutuyla disketi mount mount mount mount ediniz. Eğer disket yazmaya karşı korumalıysa, komutu

```bash
# mount -r -t pcfs /dev/fd0 /disket mount -r -t pcfs /dev/fd0 /disket mount -r -t pcfs /dev/fd0 /disket mount -r -t pcfs /dev/fd0 /disket
```

şeklinde vermelisiniz. mount mount mount mount işlemi başarılı olursa, herhangi bir mesaj almadan sistem hazır işaretini (prompt) görürsünüz.

Şimdi kopyalama işine başlayabilirsiniz.

```bash
# cp /disket/*.dat /home/ayfer cp /disket/*.dat /home/ayfer cp /disket/*.dat /home/ayfer cp /disket/*.dat /home/ayfer
```

Kopyalama bittiğinde,

```bash
# umount /disket umount /disket umount /disket umount /disket veya
# umount /dev/fd0 umount /dev/fd0 umount /dev/fd0 umount /dev/fd0
```

komutuyla disketi sistemden ayırıp,

```bash
# eject floppy eject floppy eject floppy eject floppy
```

komutuyla yuvasından çıkarmalısınız.

Bir de kısaca, CD kullanımına örnek vereyim. Bu örnekteki en önemli detay, CD kayıt tipiyle ilgili. Bir kaç paragraf önce ISO 9660 ISO 9660 ISO 9660 ISO 9660 ve High Sierra File System High Sierra File System High Sierra File System High Sierra File System adlı CD kayıt sistemlerinden söz ettim. Bir CD nin hangi sisteme göre kaydedildiğini her zaman kolayca anlayamazsınız Böyle durumlarda en kötü olasılıkla mount mount mount mount komutunun iki formunu da deneyerek işinizi görebilirsiniz.

```bash
# ls /cdrom ls /cdrom ls /cdrom ls /cdrom /cdrom dizini var mı?
```

```bash
# mount -r /dev/sr0 /cdrom mount -r /dev/sr0 /cdrom mount -r /dev/sr0 /cdrom mount -r /dev/sr0 /cdrom
```

```bash
# cd /cdrom cd /cdrom cd /cdrom cd /cdrom çalı şma dizinini
```

/cdrom yaptık.

```bash
# cp *.dat /home/ayfer cp *.dat /home/ayfer cp *.dat /home/ayfer cp *.dat /home/ayfer Kopyalama i şleri...
```

```bash
# umount /cdrom umount /cdrom umount /cdrom umount /cdrom CD’yi umount umount umount umount etmek
```

için...

Device Busy Bindi ğ iniz dalı kesemezsiniz..

Çalı şma dizinini değ i ştirdik

```bash
# cd /home/ayfer cd /home/ayfer cd /home/ayfer cd /home/ayfer # umount /cdrom umount /cdrom umount /cdrom umount /cdrom
```

```bash
# eject cdrom eject cdrom eject cdrom eject cdrom CD’yi çıkarmak için
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 163

SunOS 5.x.x (SOLARIS 2.x) Kullanıcılarına...

SunOS 5.x.x (SOLARIS 2.x) Kullanıcılarına...

SunOS 5.x.x (SOLARIS 2.x) Kullanıcılarına...

SunOS 5.x.x (SOLARIS 2.x) Kullanıcılarına...

Eğer bir SUN iş istasyonu kullanıyorsanız ve işletim sistemi sürümünüz SunOS 5.x.x ise (nam-ı diğer SOLARIS 2), CD ve disket mount mount mount mount işlerinde hayat sizin daha kolay (bazı durumlarda da daha zor) demektir.

Eğer vold vold vold vold daemon’u (volume manager daemon volume manager daemon volume manager daemon volume manager daemon) çalışıyorsa ("ps -e" "ps -e" "ps -e" "ps -e" komutuyla çalışıp çalışmadığını öğrenebilirsiniz) CD veya disket mount mount mount mount etmek istediğinizde, CD veya disketi yuvasına takmanız yeterli olacaktır yuvasına takmanız yeterli olacaktır. Taktığınız yuvasına takmanız yeterli olacaktır yuvasına takmanız yeterli olacaktır medyanın formatı uygunsa otomatik olarak, önceden belirlenmiş mount mount mount mount noktalarından ilgili olanına mount mount mount mount edilecek ve kullanıma hazır olacaktır. İşi biten CD ve disketler için eject eject eject eject komutunu kullandığınızda, umount umount umount umount işi de otomatik olarak yapılacaktır. Ancak bu kolaylıkların kullanılabilmesi için vold vold vold vold programının arka planda çalışır durumda olması gerektiğini unutmayınız.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 164

Teyp Kullanı mı

Teyp Kullanı mı

Teyp Kullanı mı

Teyp Kullanı mı

UNIX dünyasının, disklerden sonraki en önemli manyetik çevre birimi teyp sürücüleridir. UNIX uygulamalarında, program ve veri dosyaları genellikle oldukça büyük olduğundan disket sürücüler pek kullanılmazlar. Hatta bir çok UNIX bilgisayarında disket sürücü bulunmaz bile.

Teyp sürücülerinin belli başlı üç kullanım alanı vardır. Doğal olarak ilk akla geleni yedekleme yedekleme yedekleme yedeklemedir. Kullandığınız bilgisayar ne olursa olsun, yedeklemenin çok önemli çok önemli çok önemli çok önemli olduğunu tekrarlamaya gerek yok sanırım.

İkinci önemli kullanım alanı, PC lerdeki disketler gibi yazılım ve veri dağıtım

veri dağıtım

veri dağıtım

veri dağıtım

ortamıdır. Örneğin bir UNIX program paketi satın aldığınızda genellikle size bir

ortamı

ortamı

ortamı

teyp kaseti gönderilir. (Son yıllarda yazılım dağıtımı amacıyla CD kullanımı hızla yaygınlaşmaktadır, ama QIC standardındaki teyp kasetleri hala çok önemli).

Üçüncü kullanım alanıysa, bilgisayarın sistem diskinde bir sorun olduğunda ve

bilgisayarı işletim sistemi dağıtım teybinden açmak

bilgisayarı işletim sistemi dağıtım teybinden açmak gerektiğinde görülür. UNIX

bilgisayarı işletim sistemi dağıtım teybinden açmak

bilgisayarı işletim sistemi dağıtım teybinden açmak

işletim sisteminin disketlere sığdırılması pek mümkün olmadığından, bilgisayarınızla birlikte ya bir teyp kaseti (UNIX Boot Tape), ya da bir CD (UNIX Boot CD) gelir. İşte işletim sistemi dağıtım teybiniz (ya da CD niz) budur; ÇOK İYİ KORUYUNUZ.

İçinde bulunduğumuz yıllarda (1995\* \* \* \*) UNIX dünyasında kullanılan teyp birimlerinin en yaygın tipleri QIC Teypler 8 mm EXABYTE 4 mm DAT teypler 150 - 525 Mega Byte 2.5 - 7 Giga Byte 2 - 16 Giga Byte olarak sıralanabilir.

- \* \* \* Bu kitabın uzun yıllar piyasada dolaşacağ ını umduğ um için tarih belirttim; bakarsınız umduğ um olur!

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 165

QIC teyp sürücüler QIC teyp sürücüler QIC teyp sürücüler QIC teyp sürücüler, yaklaşık VHS video kaset büyüklüğünde kasetler kullanırlar. Kaset kapasitelerinin mütevazi olması yanısıra; QIC en yaygın teyp standardıdır.

8 mm teyp sürücüleri 8 mm teyp sürücüleri 8 mm teyp sürücüleri 8 mm teyp sürücüleri, şekil olarak aynı 8 mm video kasetlerine benzeyen kasetler kullanırlar. Bazı 8 mm video kasetler bu sürücülerde kullanılabilmekle birlikte (daha ucuz olmalarından dolayı) bunu pek tavsiye etmem; veri kaydı için özel yapılmış kasetleri kullanmanız daha sağlıklı olacaktır.

4 mm 4 mm 4 mm 4 mm teyp teyp teyp teyplerin kullandığı kasetler neredeyse otellerde kullanılan küçücük kibrit kutularına benzer. Bu kasetleri görünce içine Giga Byte’larca kayıt sığdırılabildiğine inanmak oldukça güçtür. Kayıt teknolojisi açısından en sağlıklı ve güvenilir teypler olarak tanıtılmaktadırlar (ancak siz siz olun, bilgisayarlarla ilgili hiçbir konuda hiçbir şeye fazla güvenmeyin).

Hangi tipi kullanılırsa kullanılsın, UNIX açısından teyp teyptir. Hepsi için kullanılan komutlar aynıdır. (tar tar tar tar, cpio cpio cpio cpio, mt, mt, mt, mt, dump dump dump dump, ufsdump ufsdump ufsdump ufsdump gibi komutlar). MS-DOS teyp kullanıcılarını çatlatacak bir haberim var. UNIX’de formatlanması formatlanması kullanılacak teyplerin teyplerin teyplerin teyplerin formatlanması formatlanması gerekmemektedir gerekmemektedir gerekmemektedir gerekmemektedir.

UNIX tar Dosyaları UNIX tar Dosyaları UNIX tar Dosyaları UNIX tar Dosyaları (tape archive files) UNIX işletim sisteminde yedeklenecek veya teybe çekilip bir yerlere gönderilecek dosyalar genellikle önce bir tar tar tar tar dosyasına dönüştürülüp, sonra teybe çekilir. Bu işlem teybe dosya çekebilmek için uygulanması gereken bir kural değildir; sadece iyi yerleşmiş bir UNIX geleneğidir. tar tar tar tar dosyaları, birden fazla dosyanın peşpeşe eklenerek tek bir dosyaya kopyalanması yoluyla elde edilir.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 166

tar tar tar tar dosyalarının isimlerinin sonuna .tar .tar .tar .tar eklenmesi bir UNIX geleneğidir.

Böylece dosyayı alan kişi, o dosyanın bir tar tar tar tar paketi olduğunu; bir başka deyişle, tar tar tar tar formatı altında birleştirilmiş dosyalar içerdiğini anlayacaktır. tar Komutu tar Komutu tar Komutu tar Komutu tape archiver tape archiver tape archiver tape archiver Çok sık kullanılan, bu nedenle de iyi öğrenilmesi gereken bir komuttur.

Genel formu (basitçe) :

```bash
% tar [cxt][v]f tar-dosyas  [dosyalar] % tar [cxt][v]f tar-dosyas  [dosyalar] % tar [cxt][v]f tar-dosyas  [dosyalar] % tar [cxt][v]f tar-dosyas  [dosyalar]
```

Bu karmaşık genel formu çözmeye çalışmayın; çeşitli seçenekleri birer örnekle açıklamaya çalışacağım. Ancak; c c c c, x, x, x, x, t t t t ve v v v v harfleriyle belirtilen işlem kodlarını önce bir tanıyalım. c c c c tar tar tar tar dosyası yarat (create create create create) anlamında x x x x tar tar tar tar dosyasını aç (extract extract extract extract) anlamında t t t t tar tar tar tar dosyasının içindeki dosyaların isimlerini listele (table of contents table of contents table of contents table of contents) v v v v c, x c, x c, x c, x veya t t t t emrini yerine getirirken, olup biteni ekrana listele demektir (verbose verbose verbose verbose). Bu seçeneği kullanmazsanız tar tar tar tar komutu sessizce çalışır ve hangi dosyaları işlediğini ekrana listelemez. Bu seçeneği her zaman kullanmanızı öneririm.

Şimdi örneklere geçelim... Diyelim ki, home home home home dizinizde dosya1 dosya1 dosya1 dosya1 (10 KByte) dosya2 dosya2 dosya2 dosya2 (12 KByte) dosya3 dosya3 dosya3 dosya3 (20 Kbyte) isimli 3 dosya var.

```bash
% tar cvf dosyalar.tar dosya* % tar cvf dosyalar.tar dosya* % tar cvf dosyalar.tar dosya* % tar cvf dosyalar.tar dosya* create
% tar cvf dosyalar.tar dosya? % tar cvf dosyalar.tar dosya? % tar cvf dosyalar.tar dosya? % tar cvf dosyalar.tar dosya?
% tar cvf dosyalar.tar dosya1 dosya2 dosya3 % tar cvf dosyalar.tar dosya1 dosya2 dosya3 % tar cvf dosyalar.tar dosya1 dosya2 dosya3 % tar cvf dosyalar.tar dosya1 dosya2 dosya3
```

komutlarından herhangi biriyle bu üç dosyayı birleştirip dosyalar.tar dosyalar.tar dosyalar.tar dosyalar.tar isimli dördüncü bir dosya oluşturabilirsiniz.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 167

Yeni yaratılmış olan tar dosyası

```bash
abc:/home/ayfer> ls -l dos* ls -l dos* ls -l dos* ls -l dos*
-rw------- 1 ayfer 10240 May 12 16:53 dosya1
-rw------- 1 ayfer 12288 May 12 16:53 dosya2
-rw------- 1 ayfer 20480 May 12 16:53 dosya3
abc:/home/ayfer> tar cvf dosyalar.tar dosya* tar cvf dosyalar.tar dosya* tar cvf dosyalar.tar dosya* tar cvf dosyalar.tar dosya*
a dosya1 20 blocks
a dosya2 24 blocks
a dosya3 40 blocks
abc:/home/ayfer>
```

Bu komuttan sonra home home home home dizininizdeki adı dos dos dos dos ile başlayan dosyaları listelediğinizde

```bash
abc:/home/ayfer> ls -l dos* ls -l dos* ls -l dos* ls -l dos*
-rw------- 1 ayfer 10240 May 12 16:53 dosya1
-rw------- 1 ayfer 12288 May 12 16:53 dosya2
-rw------- 1 ayfer 20480 May 12 16:53 dosya3
-rw-r--r-- 1 ayfer 49152 May 12 16:53 dosyalar.tar
abc:/home/ayfer>
```

Diskinizde bulunan bir tar tar tar tar dosyasının içinde yer alan dosyaların isim listesini görmek istediğinizde

```bash
% tar tvf dosyalar.tar % tar tvf dosyalar.tar % tar tvf dosyalar.tar % tar tvf dosyalar.tar table of contents
```

komutunu vermeniz yeterlidir.

```bash
abc:/home/ayfer> tar tvf dosyalar.tar tar tvf dosyalar.tar tar tvf dosyalar.tar tar tvf dosyalar.tar
rw-------8700/33 10240 May 12 16:53 1995 dosya1
rw-------8700/33 12288 May 12 16:53 1995 dosya2
rw-------8700/33 20480 May 12 16:53 1995 dosya3
abc:/home/ayfer>
```

Bir tar tar tar tar dosyasını bir başka bilgisayara taşıyıp, orada yeniden açmak istediğinizdeyse

```bash
% tar xvf dosyalar.tar % tar xvf dosyalar.tar % tar xvf dosyalar.tar % tar xvf dosyalar.tar extract
```

komutunu kullanmalısınız.

Başka bilgisayar, başka dizin...

```bash
xyz:/home/hasan> tar xvf dosyalar.tar tar xvf dosyalar.tar tar xvf dosyalar.tar tar xvf dosyalar.tar
x dosya1, 10240 bytes, 20 tape blocks
x dosya2, 12288 bytes, 24 tape blocks
x dosya3, 20480 bytes, 40 tape blocks
xyz:/home/hasan> ls -l dos* ls -l dos* ls -l dos* ls -l dos*
-rw------- 1 ayfer 10240 May 12 16:53 dosya1
-rw------- 1 ayfer 12288 May 12 16:53 dosya2
-rw------- 1 ayfer 20480 May 12 16:53 dosya3
xyz:/home/hasan>
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 168

“Peki...Teyp bunun neresinde?” “Peki...Teyp bunun neresinde?” “Peki...Teyp bunun neresinde?” “Peki...Teyp bunun neresinde?” dediğinizi duyar gibi oluyorum. tar tar tar tar dosyası adı yerine bir teyp sürücüsünün /dev /dev /dev /dev dizinindeki adını verirseniz, tar tar tar tar komutu teyp üzerinde çalışacaktır.

Örneğin

```bash
% tar cvf /dev/rst0 dosya* % tar cvf /dev/rst0 dosya* % tar cvf /dev/rst0 dosya* % tar cvf /dev/rst0 dosya* create
```

komutunu verirseniz, dosya1 dosya1, dosya2 dosya2 dosya2 dosya2 ve dosya3 dosya3 dosya3 dosya3 dosyalarının birleştirilmesiyle

dosya1

dosya1

elde edilecek tar tar tar tar dosyası teybe kaydedilecektir. Dikkat ederseniz, bu durumda tar tar tar tar dosyasıyla ilgili bir isim vermiyoruz: dosyalar.tar dosyalar.tar dosyalar.tar dosyalar.tar veya benzeri bir isim vermedik. UNIX işletim sisteminde teypte yer alan tar dosyalarının isimleri

UNIX işletim sisteminde teypte yer alan tar dosyalarının isimleri

UNIX işletim sisteminde teypte yer alan tar dosyalarının isimleri

UNIX işletim sisteminde teypte yer alan tar dosyalarının isimleri

olmaz. olmaz. olmaz. olmaz. Teyp sürücüsünün adı ve teyp kasetinin okuyucu kafa karşısındaki pozisyonu teyp dosyalarını tanımlamak için yeterlidir.

Kasetinin başında bir tar tar tar tar dosyası bulunan teypden, bu tar tar tar tar dosyasının içindeki dosyaları çalışma dizininize indirmek istediğinizde

```bash
% tar xvf /dev/rst0 % tar xvf /dev/rst0 % tar xvf /dev/rst0 % tar xvf /dev/rst0 extract
```

komutunu kullanabilirsiniz.

Aynı mantıkla, teybin başındaki tar tar tar tar dosyasının içindekilerin listesini görmek istiyorsanız

```bash
% tar tvf /dev/rst0 % tar tvf /dev/rst0 % tar tvf /dev/rst0 % tar tvf /dev/rst0 table of contents
```

komutu işinizi görecektir.

Örnekler hep BSD UNIX için verilmiştir. SVR4 UNIX kullanılması durumunda değişecek tek şey, teyp sürücüsünün /dev /dev /dev /dev dizinindeki adı olacaktır.

```bash
% tar cvf /dev/rmt/0 dosya* % tar cvf /dev/rmt/0 dosya* % tar cvf /dev/rmt/0 dosya* % tar cvf /dev/rmt/0 dosya*
% tar tvf /dev/rmt/1 % tar tvf /dev/rmt/1 % tar tvf /dev/rmt/1 % tar tvf /dev/rmt/1 gibi...
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 169

Tahmin etmiş olacağınız gibi teyp kasetinin, okuyucu kafa karşısındaki pozisyonu son derece önemlidir. tar tar tar tar komutunda /dev /dev /dev /dev adı olarak

İşi bitince başa

İşi bitince başa saran saran saran saran teyp sürücüleri teyp sürücüleri teyp sürücüleri teyp sürücüleri

İşi bitince başa

İşi bitince başa

BSD BSD BSD BSD SVR4 SVR4 SVR4 SVR4 Sürücü Sürücü Sürücü Sürücü /dev/rst0 /dev/rmt/0 Birinci teyp sürücü /dev/rst1 /dev/rmt/1 İkinci teyp sürücü kullandığınız sürece, tar tar tar tar komutu işini bitirdiğinde, teyp sürücüsü otomatik olarak kasetin başına saracaktır. Kaseti teyp sürücüsünden çıkarıp geri takmanız, aynı şekilde kasetin başla sarılmasına neden olacaktır.

Kasetinizde ardarda birden fazla tar tar tar tar dosyası varsa ve siz bu iki kaydı da ayrı ayrı diskinize indirmek istiyorsanız, birinci tar tar tar tar komutunuzda kullanacağınız /dev /dev /dev /dev adında kasetin başa sarılmamasını istediğinizi belirtmek zorundasınız.

İşi bitince başa

İşi bitince başa

İşi bitince başa

İşi bitince başa sarmayan sarmayan sarmayan sarmayan teyp sürücüleri teyp sürücüleri teyp sürücüleri teyp sürücüleri BSD BSD BSD BSD SVR4 SVR4 SVR4 SVR4 Sürücü Sürücü Sürücü Sürücü /dev/nrst0 /dev/rmt/0n Birinci teyp sürücü /dev/nrst1 /dev/rmt/1n İkinci teyp sürücü

```bash
% tar xvf /dev/nrst0 % tar xvf /dev/nrst0 % tar xvf /dev/nrst0 % tar xvf /dev/nrst0 /dev /dev /dev /dev adındaki n n n n harfine dikkat!
```

komutunu kullandığınızda ( nrst0 : nrst0 : nrst0 : nrst0 : no rewind SCSI tape 0 no rewind SCSI tape 0 no rewind SCSI tape 0 no rewind SCSI tape 0 ), tar tar tar tar komutu işini bitirince, teyp kaseti başa sarılmayacaktır. Böylece ikinci tar tar tar tar dosyasını da diske indirmeniz mümkün olacaktır. Ancak, burada küçük bir sorun var. Teybin okuyucu kafası şu anda ikinci tar tar tar tar dosyasının başında değil de, iki tar tar tar tar dosyası arasındaki boşlukta duruyor. O nedenle ikinci tar tar tar tar dosyasını işlemek için vereceğiniz tar tar tar tar komutu bir hata mesajına neden olacaktır. tar: /dev/rst0: I/O error tar: /dev/rst0: I/O error tar: /dev/rst0: I/O error tar: /dev/rst0: I/O error Bu hata mesajını aldığınızda okuyucu kafa bu boşluğu atlamış olacağından son komutu tekrarlarsanız, ikinci tar tar tar tar dosyasını işlemeye başlamış olursunuz; tabii ikinci tar tar tar tar dosyası gerçekten varsa... Eğer tekrar aynı hata komutunu alırsanız, kasetin gerisi boş demektir. Daha fazla uğraşmanız anlamsızdır.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 170

Ş imdi bir kaç senaryo oynayalım:

Ş imdi bir kaç senaryo oynayalım:

Ş imdi bir kaç senaryo oynayalım:

Ş imdi bir kaç senaryo oynayalım:

1.

1.

1.

1. Teybinizin içinde 3 adet tar tar tar tar dosyası var ve siz sadece üçüncüyü üçüncüyü üçüncüyü üçüncüyü diske indirmek istiyorsunuz. Ne yapmalısınız?

. Ne yapmalısınız?

. Ne yapmalısınız?

. Ne yapmalısınız?

Teyp şeridi

Teyp şeridi

Teyp şeridi

Teyp şeridi

1. tar dosyası 2. tar dosyası 3. tar dosyası

İki dosya arası boşluk Teyp Sonu Kaseti teybe taktığınızda otomatik olarak başa sarıldığını dikkate alarak, önce ilk tar tar tar tar dosyasını atlamalısınız.

Dosya atlamanın en kolay yolu, tar tar tar tar komutunu t t t t seçeneği ile kullanmak olduğundan

```bash
% tar tvf /dev/nrst0 tar tvf /dev/nrst0 tar tvf /dev/nrst0 tar tvf /dev/nrst0
```

komutuyla ilk dosyanın içindekilerin listesini alınız. Bu liste anlamsız olmakla birlikte teybin çalıştığını göstermesi açısından yararlıdır. Bu tar tar tar tar komutunda boş bulunup /dev/rst0 /dev/rst0 /dev/rst0 /dev/rst0 kullanırsanız listeyi boşuna almış olursunuz. Çünkü tar tar tar tar komutu istediğiniz listeyi (t t t t seçeneği) verdikten sonra kaseti tekrar başa saracaktır.

Şimdi okuyucu kafa birinci ve ikinci dosyalar arasındaki boşlukta duruyor olmalı. Anlamsız da olsa bir tar tar tar tar komutuyla bu boşluğu atlamalısınız (biliyorsunuz, hata mesajı gelecek).

```bash
% tar tvf /dev/nrst0 tar tvf /dev/nrst0 tar tvf /dev/nrst0 tar tvf /dev/nrst0
```

tar: /dev/rst0: I/O error Şimdi teybin okuyucu kafası ikinci tar tar tar tar dosyasının başında... Bu dosyayı ve arkasındaki boşluğu da atlamak için

```bash
% !! !! !! !! % !! !! !! !! İkinci tar tar tar tar dosyasını atlamak için
```

İkinci ve üçüncü tar tar tar tar dosyalarının arasındaki boşluğu atlamak için komutlarını ardarda verebilirsiniz. (!! !! !! !! komutu ancak csh csh csh csh kabuk programını kullanıyorsanız ve history history history history değişkeninin bir değeri varsa anlamlıdır; eğer sh sh sh sh kabuğu kullanıyorsanız son komutu paşa paşa tekrar yazmak zorundasınız).

Şimdi kafa üçüncü tar tar tar tar dosyasının başına gelmiş olmalı. Artık normal tar tar tar tar komutunuzu (extract extract extract extract seçeneği ile ) verebilirsiniz.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 171

```bash
% tar xvf /dev/rst0 tar xvf /dev/rst0 tar xvf /dev/rst0 tar xvf /dev/rst0 tar tar tar tar komutu
```

bitti ğ inde i şimiz de bitmi ş olacağ ından, artık kaset başa sarılabilir.

2. 2. 2. 2. home home home home dizinizdeki adı a a a a ile başlayan dosyaları ilk tar tar tar tar dosyası olarak, adı b b b b ile başlayan dosyaları ikinci ve adı c c c c ile başlayan dosyaları da üçüncü tar tar tar tar dosyası olarak teybe kaydetmek istiyorsunuz. Ne yapmalısınız?

Ne yapmalısınız?

Ne yapmalısınız?

Ne yapmalısınız?

Teyp şeridi

Teyp şeridi

Teyp şeridi

Teyp şeridi

a a a a ile başlayan dosyaların tar tar tar tar dosyası b b b b ile başalayan

dosyalar

c c c c ile başlayan dosyaların tar tar tar tar dosyası İlk önce kasetin başına adı a a a a ile başlayan dosyaların tar tar tar tar dosyasını yaratmalısınız.

```bash
% tar cvf /dev/nrst0 a* tar cvf /dev/nrst0 a* tar cvf /dev/nrst0 a* tar cvf /dev/nrst0 a*
```

Hemen ardından ikinci ve üçüncü tar tar tar tar dosyalarını yaratabilirsiniz.. Dosyalar arasındaki boşlukların yaratılması sizin sorumluluğunuzda olmayacaktır.

```bash
% tar cvf /dev/nrst0 b* tar cvf /dev/nrst0 b* tar cvf /dev/nrst0 b* tar cvf /dev/nrst0 b*
% tar cvf /dev/nrst0 c* tar cvf /dev/nrst0 c* tar cvf /dev/nrst0 c* tar cvf /dev/nrst0 c*
```

3. 3. 3. 3. home home home home dizinizdeki adı a, b a, b a, b a, b ve c c c c ile başlayan dosyaları tek bir tar tar tar tar dosyası

Ne yapmalısınız?

olarak teybe kaydetmek istiyorsunuz. Ne yapmalısınız?

Ne yapmalısınız?

Ne yapmalısınız?

Teyp şeridi

Teyp şeridi

Teyp şeridi

Teyp şeridi

a, b ve c. ile başlayan

dosyalar

Bu işi tek komutta yapmalısınız. (Tek bir tar tar tar tar dosyası elde edebilmek için)..

```bash
% tar cvf /dev/nrst0 a* b* c* tar cvf /dev/nrst0 a* b* c* tar cvf /dev/nrst0 a* b* c* tar cvf /dev/nrst0 a* b* c*
```

4. 4. 4. 4. Kasetinizde adı a, b a, b a, b a, b ve c c c c ile başlayan dosyalardan oluşan tek bir tar tar tar tar

b1

b1

dosyası var. Bu dosyalar arasından sadece sadece sadece sadece adı b1 b1 ile başlayanları indirmek indirmek indirmek indirmek istiyorsunuz. Ne yapmalısınız?

Ne yapmalısınız?

Ne yapmalısınız?

Ne yapmalısınız?

Teyp şeridi

Teyp şeridi

Teyp şeridi

Teyp şeridi

a, b a, b a, b a, b ve c c c c ile başlayan

dosyalar

tar tar tar tar komutunu x x x x seçeneği ile kulllanacağınız kesin; ancak dosya adlarıyla ilgili tercihinizi belirtirken önemli bir püf noktasına dikkat etmelisiniz. İçgüdüleriniz

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 172

HATALI ! HATALI ! HATALI ! HATALI !

```bash
% tar xvf /dev/rst0 b1* tar xvf /dev/rst0 b1* tar xvf /dev/rst0 b1* tar xvf /dev/rst0 b1*
```

şeklinde bir komut yazmanızı söylüyor, değilmi?

Maalesef içgüdünüz sizi yanıltıyor ! Vermeniz gereken komut

Maalesef içgüdünüz sizi yanıltıyor !

Maalesef içgüdünüz sizi yanıltıyor !

Maalesef içgüdünüz sizi yanıltıyor !

```bash
% tar xvf /dev/rst0 "b1*" % tar xvf /dev/rst0 "b1*" % tar xvf /dev/rst0 "b1*" % tar xvf /dev/rst0 "b1*" DOÐRU ! DOÐRU ! DOÐRU ! DOÐRU !
```

Hatanın ne olduğunu ilk bakışta görememeniz oldukça normal.

Şimdi kabuklar hakkında öğrendiklerinizi bir tazeleyelim.

Kabuk programları, klavyeden girilen (ya da kabuk programlarından gelen) komut satırlarını irdeleyip, varsa parametreleri çözüp yerlerine yerleştirmeye çalışacaktır. Kabuk hatalı komuttaki b1\* hatalı hatalı programı hatalı

b1\*

b1\*

b1\* karakterlerini görünce, komutun verildiği andaki çalışma dizininde bulunan dosyalar arasında (Dikkat! Dikkat! Dikkat! Dikkat! teypteki değil, çalışma dizininde bulunan dosyalar

b1

b1

arasında) adı b1 b1 ile başlayanları bulup onların isimlerini komut satırında b1\*

b1\*

b1\*

b1\* in yerine yerleştirip, komutu öyle çalıştıracaktır.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 173

b1

b1

Eğer çalışma dizininde adı b1 b1 ile başlayan dosya yoksa, komut satırınız tar xvf /dev/rst0 tar xvf /dev/rst0 tar xvf /dev/rst0 tar xvf /dev/rst0 (dosya adına ilişkin bir parametre yok) olarak yazılmış kabul edilip tar tar tar tar komutu çalıştırılacak ve çok doğal olarak kasetteki tüm dosyaları indirecektir. b1\* karakterlerini

b1\*

b1\*

Bu sorunu halletmek için, kabuk programına b1\* çözümlememesi gerektiğini bildirmek gerekir. Bunun için tar tar tar tar komutunda b1\*

b1\*

b1\*

b1\* karakterlerini tırnak içine almalıyız. Böylece

"b1\*"

"b1\*"

"b1\*"

"b1\*" kalıbı kabuk programı tarafından değil, tar tar tar tar programı tarafından çözümlenecektir ve teypteki dosyalar arasında yanlızca adı bu kalıba uyan dosyalar diske indirilmiş olacaktır.

tar Komutunu kullanırken dikkat edilmesi gereken noktalar

tar Komutunu kullanırken dikkat edilmesi gereken noktalar

tar Komutunu kullanırken dikkat edilmesi gereken noktalar

tar Komutunu kullanırken dikkat edilmesi gereken noktalar

tar tar tar tar komutunu kullanırken çok tekrarlanan bazı hatalara dikkatinizi çekmek istiyorum.

1.

1.

1.

1. tar tar tar tar komutu, tar tar tar tar dosyası yaratırken dosya ve dizin ayırımı dosya ve dizin ayırımı yapmaz. dosya ve dizin ayırımı dosya ve dizin ayırımı Parametre olarak verilen dosya kalıbına uyan her şey tar tar tar tar dosyasının içine kopyalanır. Dizinler ve alt dizinleri buna dahildir.

2. 2. 2. 2. “tar cvf /dev/nrst0 \*” tar cvf /dev/nrst0 \*” tar cvf /dev/nrst0 \*” tar cvf /dev/nrst0 \*” komutu (çalışma dizinindeki her şeyi teybe tar tar tar tar dosyası olarak çek anlamında) aslında her şeyi çekmeyecektir. Komutun bu şekilde kullanılması durumunda adı . . . . (nokta) ile başlayan dosyalar tar tar tar tar dosyasına dahil edilmeyecektir. Adları noktayla başlayan dosyaları da kasete çekmek istiyorsanız; “tar cvf /dev/nrst0 .login .cshrc .X\* \*” “tar cvf /dev/nrst0 .login .cshrc .X\* \*” “tar cvf /dev/nrst0 .login .cshrc .X\* \*” “tar cvf /dev/nrst0 .login .cshrc .X\* \*” gibi bir komut kullanmanız gerekir.

“tar cvf /dev/nrst0 .\* \*” “tar cvf /dev/nrst0 .\* \*” “tar cvf /dev/nrst0 .\* \*” “tar cvf /dev/nrst0 .\* \*” şeklindeki bir komut tehlikeli olabilir. Bulunduğunuz dizinde, normal dosyalar ve dizinler yanısıra yer alan . . . . ve .. .. .. .. isimli iki özel dizin vardır. Bunlardan .. bir üst düzey dizini gösterdiği için; verdiğiniz komut, bir üst düsey dizini de teybe çekmek istediğiniz şeklinde yorumlanabilir.

3. 3. 3. 3. Bir çok UNIX kitabında açıklamasını göreceğiniz -r -r -r -r parametresi, ilk bakışta anlaşılacağı gibi teybin sonuna yeni bir tar tar tar tar dosyası eklemek için değil, teyp yazma kafasının üzerinde bulunduğu tar tar tar tar dosyasının sonuna eklemeler yapmak için kullanılır. Teyplerde bu parametrenin kullanılması, eğer varsa, söz konusu

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 174

tar tar tar tar dosyasının ardından gelen dosyaların tamamen kaybedilmeleriyle sonuçlanacaktır.

4. 4. 4. 4. Sık tekrarlanan bir başka hatayı ise bir örnekle açıklamak istiyorum.

Diyelim ki elimizde aşağıdaki şekilde kaydedilmiş bir teyp kaseti var :

1. tar dosyası 2. tar dosyası 3. tar dosyası

Kasetin sonuna ekleme yapmayı planlarken yanlışlıkla, tar cvf tar cvf tar cvf tar cvf komutunu kaset teybin başındayken verdiniz. Anında hatanızı farkettiniz ve hemen işinizi kestiniz. (Ctrl-C) ya da hemen teyp birimini kapattınız. Birinci tar tar tar tar dosyasının

kurtardığınızı

bozulduğuna hiç şüphe yok ama 2. ve 3. tar tar tar tar dosyalarını kurtardığınızı

kurtardığınızı

kurtardığınızı

sanıyorsanız YANILIYORSUNUZ YANILIYORSUNUZ YANILIYORSUNUZ YANILIYORSUNUZ. Yaptığınız hata kasetin tümündeki kayıtların

sanıyorsanız

sanıyorsanız

sanıyorsanız

kaybolmasına yol açtı.

Aynı mantıkla, birinci tar tar tar tar dosyasından daha kısa bile olsa, birinci dosya üzerine yapacağınız bir kayıt, kasetin bu kayıttan sonrasını kullanılamaz duruma getirecektir. Görsel olarak anlatmak gerekirse...

Kasetinizdeki kayıt yapısı

1. tar dosyası 2. tar dosyası 3. tar dosyası

Kayıt Sonu İşareti şeklindeyken, kısa bir tar tar tar tar dosyası oluşturmak için

```bash
% mt -f /dev/rst1 rewind mt -f /dev/rst1 rewind mt -f /dev/rst1 rewind mt -f /dev/rst1 rewind
% tar cvf /dev/nrst1 kisa-dosyalar tar cvf /dev/nrst1 kisa-dosyalar tar cvf /dev/nrst1 kisa-dosyalar tar cvf /dev/nrst1 kisa-dosyalar
```

komutlarını verirseniz yeni kaset yapınız Kısa tar tar tar tar dosyası şekline dönüşür. (Üzgünüm... Üzgünüm... Üzgünüm... Üzgünüm...)

5. 5. 5. 5. tar tar tar tar programı, daha önce bir tar tar tar tar dosyası içine paketlenmiş olan dosyaları geri çıkarırken (extract extract extract extract ederken) bu dosyaları alındıkları dizinlere yerleştirmeye çalışır. Örneğin

```bash
% tar cvf /dev/nrst1 /home/ayfer/* tar cvf /dev/nrst1 /home/ayfer/* tar cvf /dev/nrst1 /home/ayfer/* tar cvf /dev/nrst1 /home/ayfer/*
```

şeklinde bir komutla tar tar tar tar’lanmış dosyaları bir başka bilgisayarda

```bash
% tar xvf /dev/nrst0 tar xvf /dev/nrst0 tar xvf /dev/nrst0 tar xvf /dev/nrst0
```

komutuyla geri indirmek istediğinizde, dosyalar yeni bilgisayarda /home/ayfer /home/ayfer /home/ayfer /home/ayfer diye bir dizinin altına indirilecek; böyle bir dizin yoksa yaratılmaya çalışılacaktır. Bu tip sıkıntıları önlemek için tar tar tar tar programıyla dosya çekerken

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 175

```bash
% cd /home/ayfer cd /home/ayfer cd /home/ayfer cd /home/ayfer
% tar cvf /dev/nrst1 ./* tar cvf /dev/nrst1 ./* tar cvf /dev/nrst1 ./* tar cvf /dev/nrst1 ./*
```

şeklinde göreceli dizin tanımları kullanmanızı öneririm. ./\* ./\* ./\* ./\* kalıbı; “bulunduğum dizindeki herşey” anlamına gelmektedir.

6. 6. 6. 6. tar tar tar tar programı, dosya extract extract extract extract ederken diskte aynı isimde bir dosya olsa bile uyarmadan uyarmadan uyarmadan uyarmadan üzerine yeni dosyayı indirir.

7. 7. 7. 7. tar tar tar tar programı, tar tar tar tar dosyası yaratırken bağlantılı dosyaları (link link link link) kopyalamaz. Eğer bu tip dosyaların kopyalanmasını özellikle istiyorsanız, komutunuzda -h -h -h -h tar cvfh /dev/nrst1 ./\* tar cvfh /dev/nrst1 ./\* seçeneğini belirtmeniz gerekir. tar cvfh /dev/nrst1 ./\* tar cvfh /dev/nrst1 ./\* gibi... (SVR4 UNIX’de -L -L -L -L).

8. 8. 8. 8. tar tar tar tar programı, sadece teyp kullanımıyla sınırlı değildir; disketlerle birlikte de aynı rahatlıkla kullanılabilir. Ancak, normal tar tar tar tar programları medya dolduğunda (teyp ya da diskette boş yer kalmadığında) hata mesajı vererek dururlar (Abort Abort Abort Abort). Bir medya dolduğunda diğer bir boş medya isteyen tar tar tar tar programlarının adı genellikle bar bar bar bar’dır. SVR4 UNIX’lerde tar tar tar tar komutları birden fazla medya üzerine kayıt yapabilecek şekilde geliştirilmiştir. Sizin sisteminizde hangisini kullanacağınıza karar vermek için sistem yöneticinize danışınız.

9. 9. 9. 9. Bazı tar tar tar tar programları, tar tar tar tar dosyası yaratırken bir yandan da veri sıkıştırması yapabilirler. Bu özellik standart olmadığından, bir başka bilgisayara taşımak üzere tar tar tar tar dosyası (tar tar tar tar teybi) yaratırken tar tar tar tar programlarının bu sıkıştırma özelliğini kullanmayınız. Eğer mutlaka sıkıştırma yapmanız gerekiyorsa, dosyalarınızı önce diskte bir dosyaya tar tar tar tar’layın; sonra bu dosyayı standart UNIX compress compress compress compress komutuyla sıkıştırın, ondan sonra bu dosyayı tekrar tar tar tar tar komutuyla teybe (ya da diskete) kaydedin. Bu yöntemi kullandığınızı teyp ya da disketin etiketi üzerinde açıklayıcı bir not olarak iliştirip diğer bilgisayarda kullanılmak üzere yollayın. Örnek olarak :

```bash
% tar cvf dosyalar.tar dosya* tar cvf dosyalar.tar dosya* tar cvf dosyalar.tar dosya* tar cvf dosyalar.tar dosya*
% compress dosyalar.tar compress dosyalar.tar compress dosyalar.tar compress dosyalar.tar
% tar cvf /dev/fd0 dosyalar.tar.Z tar cvf /dev/fd0 dosyalar.tar.Z tar cvf /dev/fd0 dosyalar.tar.Z tar cvf /dev/fd0 dosyalar.tar.Z
```

compress programı sıkıştırdığı dosyanın adının sonuna .Z .Z .Z .Z ekler.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 176

Etkileyici Bir UNIX Gösterisi Etkileyici Bir UNIX Gösterisi Etkileyici Bir UNIX Gösterisi Etkileyici Bir UNIX Gösterisi Şimdi MS-DOS kullanıcılarını çatlatacak çatlatacak çatlatacak çatlatacak bir UNIX gösterisi yapmak; bir başka deyişle hava atmak hava atmak hava atmak hava atmak istiyorum. Gösterinin komutun nasıl çalıştığını anlamazsanız fazla dert etmeyin ama günün birinde bu komutun sırrını çözecek kadar UNIX öğrenmeye de azmedin lütfen. Aslında olay basit, ama komutu karmaşık. UNIX alışkanlığınız arttıkça bu tip komutları sizin de kullanacağınıza eminim.

Yapmak istediğimiz iş şu :

Bilgisayar ağı üzerindeki abc abc abc abc bilgisayarının önünde oturarak, dosyalarımızı xyz xyz xyz xyz makinasının üzerindeki rst1 rst1 rst1 rst1 teyp ünitesinde takılı olan kasete kopyalayacağız.

```bash
abc:/> tar cvfb - 20 dosya* | rsh xyz dd of=/dev/rst0 obs=20b abc:/> tar cvfb - 20 dosya* | rsh xyz dd of=/dev/rst0 obs=20b abc:/> tar cvfb - 20 dosya* | rsh xyz dd of=/dev/rst0 obs=20b abc:/> tar cvfb - 20 dosya* | rsh xyz dd of=/dev/rst0 obs=20b
```

Neler olup bittiğini merak ettiyseniz, açıklayayım: abc abc abc abc bilgisayarında tar tar tar tar programını başlatıyoruz, adı dosya\* dosya\* dosya\* dosya\* kalıbına uyan dosyaları bir tar tar tar tar dosyasına dönüştürüyoruz; ancak bu tar tar tar tar dosyasını fiziksel bir sürücü yerine standart çıktıya yönlendiriyoruz ( tar tar tar tar dosyası adı olarak - - - - işareti). Aynı anda; adı xyz xyz xyz xyz olan uzaktaki bilgisayarda dd dd dd dd ( device to device device to device device to device device to device copy copy copy copy) programını başlatıyoruz (rsh rsh rsh rsh : remote shell komutu). abc abc abc abc makinasının standart çıktısındaki kayıtları (tar tar tar tar dosyamızı), xyz xyz xyz xyz makinasında çalışmakta olan dd dd dd dd programına girdi olarak pipe pipe pipe pipe edip, dd dd dd dd programının çıktı dosyası olarak tanımlanmış olan /dev/rst0 /dev/rst0 /dev/rst0 /dev/rst0 sürücüsüne kaydedilmesini sağlıyoruz. Bu arada, bilgisayarlar arası transferi hızlandırmak amacıyla da kayıtlarımızı 20’şer 20’şer blokluyoruz. dd dd dd dd komutunu merak ettiyseniz, bir /dev /dev /dev /dev biriminden bir başka /dev /dev /dev /dev birimine veri kopyalamak için kullanılan programdır. Örneğin teypten teybe, disketten teybe kopyalamalarda kullanılabilir. Daha fazla bilgi almak için man dd man dd man dd man dd komutunu kullanınız. dump dump dump dump (BSD UNIX) ve ufsdump ufsdump ufsdump ufsdump (SVR4) genellikle sadece sistem yöneticilerini ilgilendiren ve diskleri teyplere yedeklemek için kullanılan komutlardır. Bu komutları kitabın “Sistem Yöneticine” başlıklı bölümlerinde anlatacağım.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 177

mt Komutu mt Komutu mt Komutu mt Komutu (magnetic tape controls) Teyp sürücülerindeki kasetlerin okuma/yazma kafası karşısındaki pozisyonunu ayarlamak için kullanılan bir komuttur.

```bash
% mt -f /dev/nrst0 hareket-kodu % mt -f /dev/nrst0 hareket-kodu % mt -f /dev/nrst0 hareket-kodu % mt -f /dev/nrst0 hareket-kodu
```

hareket-kodu hareket-kodu hareket-kodu hareket-kodu olarak rewind rewind rewind rewind (kısaca rew rew rew rew de kullanılabilir) (forward space file) fsf fsf fsf fsf fsf n fsf n fsf n fsf n eof eof eof eof retension retension retension retension (end of file) erase erase erase erase anahtar sözcükleri kullanılabilir. mt hareket-kodu mt hareket-kodu mt hareket-kodu mt hareket-kodu Görevi Görevi Görevi Görevi rewind rewind rewind rewind Kaseti başa sarar fsf fsf fsf fsf Kaseti bir dosya veya dosyalar arası boşluk kadar ileri sarar fsf n fsf n fsf n fsf n Kaseti n n n n tane dosya ve dosyalar arası boşluk kadar ileri sarar. (Örneğin, kasetinizi 3 dosya ileri atlatmak istiyorsanız fsf 6 fsf 6 fsf 6 fsf 6 kullanmalısınız.

(dosya+boşluk+dosya+boşluk+dosya+boşluk) eof eof eof eof Kasetin sonuna kadar ileri sarar. Kaset sonlarına dosya eklemek istediğinizde önce bu komutla kaseti sona sarmalısınız. retension retension retension retension Kaseti sona kadar ileri ve sonra tekrar başa sarar; böylece kasetin manyetik şeridinin gerginliği düzenlenmiş olur. erase erase erase erase Bir kasetin içindeki tüm kayıtları siler.

Eğer mt mt mt mt komutunu /dev/rst0 /dev/rst0 /dev/rst0 /dev/rst0 gibi “no rewind device (nrst0)” “no rewind device (nrst0)” “no rewind device (nrst0)” “no rewind device (nrst0)” belirtmeden kullanarak kaseti 4 dosya ileri ya da kaset sonuna sararsanız pek anlamlı bir iş yapmış sayılmazsınız. Çünkü, rst0 rst0 rst0 rst0 şeklinde verilen /dev /dev /dev /dev adları, teyp sürücüsünün işi bittiğinde (örneğin 4 dosya ileri sardıktan sonra) kaseti başa saracaktır.

Eğer kullanacağınız mt mt mt mt hareket-kodu rewind rewind rewind rewind, erase erase erase erase ya da retension retension retension retension ise sorun yok. İş bitince zaten kaset başa sarılı durumda kalacaktır.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 178

cpio Komutu cpio Komutu cpio Komutu cpio Komutu (copy input to output) tar tar tar tar kadar yaygın olarak kullanılmamakla birlikte, önemli teyp programlarındandır. Kullanılmaları tar tar tar tar’a göre daha fazla dikkat ve uzmanlık gerektirir. En önemli özelliği, teybe kopyalanacak dosya ve dizinlerin isimlerini standart giriş biriminden kabul etmesidir. Bu sayede, teybe kopyalanacak dosyaların isimleri başka programlar tarafından üretilen bir isim listesinden alınabilir. Çok karışık geldiyse bu komutla ilgili bölümü atlayabilirsiniz.

Meraklı okuyucularla devam edelim....

Aşağıdaki komut satırı, find find find find ve cpio cpio cpio cpio programlarını birlikte kullanarak son 10 gün içinde değişikliğe uğramış olan dosyaları teybe çekecektir. (İster inanın ister inanmayın).

```bash
% find . -type f -mtime -10 -p % find . -type f -mtime -10 -p % find . -type f -mtime -10 -p % find . -type f -mtime -10 -print | cpio -o > /dev/nrst0 rint | cpio -o > /dev/nrst0 rint | cpio -o > /dev/nrst0 rint | cpio -o > /dev/nrst0
```

Komut satırının mantığı şu :

. . . . (nokta) Aramaya, bulunduğum dizinden başla -type f -type f -type f -type f Tipi “dosya (file)” olan kayıtlarla ilgileniyorum (dizinleri dikkate alma) -mtime -10 -mtime -10 -mtime -10 -mtime -10 Son 10 gün içinde değişmiş olanları ayıkla -print -print -print -print Bulduklarının adlarını listele | cpio | cpio | cpio | cpio Bu listeyi ekrana değil de cpio cpio cpio cpio programına girdi olarak gönder (pipe kuruyoruz) -o /dev/nrst0 -o /dev/nrst0 -o /dev/nrst0 -o /dev/nrst0 cpio programı çıkışını nrst0 nrst0 nrst0 nrst0 teybine yazsın. cpio cpio cpio cpio programıyla elde edilen teyp kayıtları sadece cpio cpio cpio cpio programı ile geri yüklenebilirler.

Yukarıdaki komutla yedeklenmiş dosyaları teypden geri yüklemeniz gerekirse

```bash
% cpio -idmuv < /dev/rst0 cpio -idmuv < /dev/rst0 cpio -idmuv < /dev/rst0 cpio -idmuv < /dev/rst0
```

Eğer sadece bir dosyayı indirmek isterseniz (tabii ki daha önce cpio cpio cpio cpio ile teybe kaydedilmiş olmak şartıyla)

```bash
% cpio -idmuv istenen_dosya < /dev/rst0 cpio -idmuv istenen_dosya < /dev/rst0 cpio -idmuv istenen_dosya < /dev/rst0 cpio -idmuv istenen_dosya < /dev/rst0
```

cpio cpio cpio cpio komutuyla birlikte kullandığım garip idmuv idmuv idmuv idmuv seçeneklerinin ne olduğunu merak ettiyseniz man man man man komutu size yardımcı olabilir.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 179

Aman Ha! Sakın Ha!

Aman Ha! Sakın Ha!

Aman Ha! Sakın Ha!

Aman Ha! Sakın Ha! Elinizde bir teyp kasetiyle ortalıkta dolaşıp “Yahu! Bu kaseti nasıl mount mount mount mount edeceğim?” diye dolaşmayın. Rezil olursunuz! UNIX’de teypler “mount mount mount mount” edilmez! (Teyplerle ilgili olarak kullanılan “mt mt mt mt” komutu “mount” değil, “magnetic tape control” anlamındadır.)

UNIX’de bir çevre biriminin “mount” edilebilmesi için, çevre birimi üzerinde önceden bir dosya yapısı (file system) oluşturulmuş olması gerekir; bu da şimdilik yalnızca disk, disket, CDROM ve Magneto Optik diskler gibi doğrudan erişimli doğrudan erişimli çevre birimlerinde (Direct doğrudan erişimli doğrudan erişimli Access Storage Device) mümkündür. Teypler; şerit yapılarından dolayı sıradan erişimli çevre birimleridir (Sequential Access Storage Device).

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 180

Kullanı ş lı UNIX Komutları

Kullanı ş lı UNIX Komutları

Kullanı ş lı UNIX Komutları

Kullanı ş lı UNIX Komutları

UNIX işletim sisteminde, /bin /bin /bin /bin ve-veya /usr/bin /usr/bin /usr/bin /usr/bin, /usr/sbin /usr/sbin /usr/sbin /usr/sbin, /usr/5bin /usr/5bin /usr/5bin /usr/5bin gibi dizinlerinde yüzlerce program bulunur. Bunların önemli bir kısmının ne işe yaradığını bile anlamak meseledir. Ancak zamanla; çıraklık yapa yapa ve başınızı vura vura bu programlarının çoğunu anlayacak, öğrenecek ve kullanacaksınız. Başlangıçta bilmeniz gerekebilecek bazı komutları seçip açıklamak istiyorum. Bu seçimimde kullandığım kriter basit : seyrek de olsa kendi kullandığım komutlardan, herhangi bir sırayı dikkate almaksızın söz edeceğim. Bu arada, bazı tekrarlar olacak ama sizi rahatsız edeceğini sanmıyorum.

```bash
% cat % cat % cat % cat (catenate)
```

En temel kopyalama programı. Standart girişi standart çıkışa kopyalar.

Eğer parametresiz olarak başlatırsanız

Eğer parametresiz olarak başlatırsanız garip bir duruma düşersiniz. cat cat cat cat yazıp

Eğer parametresiz olarak başlatırsanız

Eğer parametresiz olarak başlatırsanız

Enter tuşuna basar basmaz imleç bir alt satıra iner ve oradan başlayarak klavyeden her yazdığınız satırı geri ekrana tekrarlar. Aslında program tanımına uygun davranıyor; yani standart girişi (klavyeyi) standart çıkışa (ekrana) kopyalıyor. Bu durum tamamen yararsız olduğundan, kurtulmak için, imleç satır başındayken Ctrl-D tuşuna basmanız gerekir. (Sadece bir kere; aksi takdirde, fazladan basacağınız Ctrl-D karakterleri kabuk programınız tarafından “dosya sonu” olarak yorumlanabilir ve daha fazla komut vermek istemediğiniz sonucuna varılarak kabuk programınız öldürülür; bir başka deyişle istemeden logout logout logout logout etmiş olursunuz.)

Parametreli olarak Parametreli olarak Parametreli olarak Parametreli olarak kullanıldığında, parametresinde verilen dosya (ya da dosyaları) standart çıkış birimi olan ekrana listeler. (MS-DOS’daki TYPE komutu gibi).

Buraya kadar olan kısmı zaten biliyordunuz. Peki aşağıdaki cat cat cat cat komutu formlarına ne dersiniz?

```bash
% cat dosya1 dosya2 dosya3 > genel_dosya cat dosya1 dosya2 dosya3 > genel_dosya cat dosya1 dosya2 dosya3 > genel_dosya cat dosya1 dosya2 dosya3 > genel_dosya
```

dosya1, dosya2 ve dosya3 dosyalarını bu sırayla peşpeşe ekleyip bir genel\_dosya dosyası oluşturur.

```bash
% cat dosya1 dosya2 dosya3 > genel_dosya & cat dosya1 dosya2 dosya3 > genel_dosya & cat dosya1 dosya2 dosya3 > genel_dosya & cat dosya1 dosya2 dosya3 > genel_dosya &
```

Aynı işi arka planda çalışarak yapar.

```bash
% cat buyuk_dosya > /dev/null cat buyuk_dosya > /dev/null cat buyuk_dosya > /dev/null cat buyuk_dosya > /dev/null
```

buyuk\_dosya buyuk\_dosya buyuk\_dosya buyuk\_dosya isimli dosyayı “kara deliğe” yani “hiç bir yere” kopyalar. Böyle bir komutla, dosyanın başından sonuna kadar okunabilir olup olmadığını denemiş olursunuz.

```bash
% cat liste > /dev/bpp0 cat liste > /dev/bpp0 cat liste > /dev/bpp0 cat liste > /dev/bpp0
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 181

liste isimli programı doğrudan yazıcı arabirimine kopyalar. Yazıcı ile ilgili daemon daemon daemon daemon’lar çalışmıyor olsa bile bu yöntemle yazıcıdan döküm alabilirsiniz. Ancak, root root root root kullanıcı olmanız gerekir.

```bash
% cat < /dev/ttyb cat < /dev/ttyb cat < /dev/ttyb cat < /dev/ttyb
```

İkinci seri arabirime bağlı olan terminalin klavyesinden yazılan her şeyi sizin ekranınıza kopyalar. Bu komut ancak mesai arkadaşlarını deli etmek isteyen root root root root kullanıcılar tarafından verilebilir.

```bash
% compress dosya_adi % compress dosya_adi % compress dosya_adi % compress dosya_adi
```

Kısa dönemde gerekli olmayacak ya da teybe çekilecek disk dosyalarının daha az yer işgal etmelerini sağlamak amacıyla kullanılan sıkıştırma programıdır.

```bash
% compress buyuk_dosya compress buyuk_dosya compress buyuk_dosya compress buyuk_dosya
```

komutunu verdiğinizde, buyuk\_dosya buyuk\_dosya buyuk\_dosya buyuk\_dosya isimli dosya sıkıştırılır ve buyuk\_dosya.Z buyuk\_dosya.Z buyuk\_dosya.Z buyuk\_dosya.Z isimli daha küçük bir dosyaya dönüştürülür. (MS-DOS dünyasındaki PKZIP gibi). Küçültmenin ne oranda olacağı tamamen dosyanın içeriğine bağlıdır.

ASCII text içeren dosyalarda sıkıştırma oranı oldukça yüksek olabilir. MS- DOS'daki PKZIP programından farklı olarak compress compress compress compress programı, dosyaları teker teker teker teker teker ve kendi üzerlerine teker ve kendi üzerlerine teker ve kendi üzerlerine teker ve kendi üzerlerine sıkıştırır.

```bash
% uncompress dosya_adi % uncompress dosya_adi % uncompress dosya_adi % uncompress dosya_adi
```

Daha önce sıkıştırılmış olan dosyaları geri açan programdır.

```bash
% uncompress buyuk_dosya.Z uncompress buyuk_dosya.Z uncompress buyuk_dosya.Z uncompress buyuk_dosya.Z
```

```bash
% tail [ -n ] dosya % tail [ -n ] dosya % tail [ -n ] dosya % tail [ -n ] dosya
```

Bir ASCII text dosyasının en son n n n n satırını listelemek için kullanılır. Eğer -n -n -n -n belirtilmemişse son 10 satır listelenir. tail tail tail tail komutunun çok hoş bir özelliği daha vardır. Eğer komutu -f -f -f -f parametresiyle kullanırsanız, ( tail -f uzayan\_dosya tail -f uzayan\_dosya tail -f uzayan\_dosya tail -f uzayan\_dosya ) dosyanın sonuna gelindiğinde program durmaz, eklenecek yeni kayıtları beklemeye başlar. Böylece, başka programlar tarafından sonuna devamlı kayıt eklenen dosyalara eklenen satırları ekranınızda sürekli olarak gözleyebilirsiniz. Gözleminiz sona erince, programı Ctrl-C ile durdurabilirsiniz.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 182

```bash
% head [ -n ] dosya % head [ -n ] dosya % head [ -n ] dosya % head [ -n ] dosya
```

Bir ASCII text dosyasının ilk n n n n satırını listelemek için kullanılır. Eğer -n -n -n -n belirtilmemişse ilk 10 satır listelenir.

```bash
% sort [ -d % sort [ -d % sort [ -d % sort [ -dbfru + bfru + bfru + bfru +f f f f - - - -g g g g ] dosya ] dosya ] dosya ] dosya
```

dosya dosya dosya dosya isimli dosyanın içindeki satırları alfabetik sıraya dizer, sıralı dosyayı standart çıktı birimine (ekrana) gönderir.

-d -d -d -d parametresi (dictionary sort) kullanılırsa, sıralama sözlük sırasında yapılır. (Yanlızca rakam, harf ve boşluklar dikkate alınır; noktalama işaretleri ve özel karakterler dikkate alınmaz) -b -b -b -b parametresi kullanılırsa satır başlarındaki boşluklar dikkate alınmaz.

-f -f -f -f parametresi kullanılırsa büyük harfler küçük harflere dönüştürülerek sıralama yapılır. Örneğin; Ayfer Ayfer Ayfer Ayfer ile ayfer ayfer ayfer ayfer eşdeğer kabul edilerek sıralama yapılır.

-r -r -r -r parametresi kullanılırsa, sıralama küçükten büyüğe değil, büyükten küçüğe doğru yapılır (reverse reverse reverse reverse order order order order) -u -u -u -u parametresi kullanılırsa birbirinin aynı olan satırlara rastlandığında sadece bir tanesi dikkate alınır. Bu parametreyi aşağıdaki örnekteki gibi kullanarak bir dosyadaki mükerrer kayıtları ayıklayabilirsiniz.

```bash
% sort -u dosya1 > dosya2 sort -u dosya1 > dosya2 sort -u dosya1 > dosya2 sort -u dosya1 > dosya2
```

+ + + +f f f f parametresi, sıralamada kullanılacak anahtar bilginin, satırın f f f f numaralı bilgi sahasında başladığını gösterir. (Dikkat Dikkat Dikkat Dikkat ! Bilgi saha sıra numaraları sıfırdan başlar) -g -g -g -g parametresi ise sıralamada kullanılacak anahtar bilginin, satırın g g g g numaralı sahasında sona erdiğini belirtir. (Dikkat ! Dikkat ! Dikkat ! Dikkat ! Saha sıra numaraları sıfırdan başlar) Satırlardaki sahalar boşluk karakterleri ve TAB karakterleriyle belirlenir.

Eğer boşluk ve TAB dışında bir ayırıcı karakter kullanmak isterseniz, bu karakteri -tx -tx -tx -tx parametresini kullanarak (ayırıcı karakter = x) belirtebilirsiniz. sort sort sort sort komutunun kullanımı üzerine bir dizi örnek vermek istiyorum. Bu örneklerin tümünde aşağıdaki sirasiz sirasiz sirasiz sirasiz isimli test veri dosyasının kullanıldığı varsayılmıştır.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 183

Dosyanın orijinal, sırasız sırasız hali sırasız sırasız sort sirasiz > sirali sort sirasiz > sirali sort sirasiz > sirali sort sirasiz > sirali komutundan sonra...

sarf kalem 200 sarf kalem 200 sarf kalem 200 sarf kalem 200

mobilya masa 12 mobilya masa 12 mobilya masa 12 mobilya masa 12

mobilya masa 12 mobilya masa 12 mobilya masa 12 mobilya masa 12

mobilya sandalye 8 mobilya sandalye 8 mobilya sandalye 8 mobilya sandalye 8

mutfak kahve 23 mutfak kahve 23 mutfak kahve 23 mutfak kahve 23

mobilya sehpa 4 mobilya sehpa 4 mobilya sehpa 4 mobilya sehpa 4

mobilya sandalye 8 mobilya sandalye 8 mobilya sandalye 8 mobilya sandalye 8

mutfak bardak 70 mutfak bardak 70 mutfak bardak 70 mutfak bardak 70

sarf silgi 123 sarf silgi 123 sarf silgi 123 sarf silgi 123

mutfak kahve 23 mutfak kahve 23 mutfak kahve 23 mutfak kahve 23

mutfak seker 340 mutfak seker 340 mutfak seker 340 mutfak seker 340

mutfak seker 340 mutfak seker 340 mutfak seker 340 mutfak seker 340

mobilya sehpa 4 mobilya sehpa 4 mobilya sehpa 4 mobilya sehpa 4

sarf kalem 200 sarf kalem 200 sarf kalem 200 sarf kalem 200

mutfak bardak 70 mutfak bardak 70 mutfak bardak 70 mutfak bardak 70

sarf silgi 123 sarf silgi 123 sarf silgi 123 sarf silgi 123

```bash
sort -r sirasiz > sirali sort -r sirasiz > sirali sort -r sirasiz > sirali sort -r sirasiz > sirali
```

```bash
sort +1 -2 sirasiz > sirali
sort +1 -2 sirasiz > sirali
sort +1 -2 sirasiz > sirali
sort +1 -2 sirasiz > sirali
```

komutundan sonra komutundan sonra

sarf silgi 123 sarf silgi 123 sarf silgi 123 sarf silgi 123

mutfak bardak 70 mutfak bardak 70 mutfak bardak 70 mutfak bardak 70

sarf kalem 200 sarf kalem 200 sarf kalem 200 sarf kalem 200

mutfak kahve 23 mutfak kahve 23 mutfak kahve 23 mutfak kahve 23

mutfak seker 340 mutfak seker 340 mutfak seker 340 mutfak seker 340

sarf kalem 200 sarf kalem 200 sarf kalem 200 sarf kalem 200

mutfak kahve 23 mutfak kahve 23 mutfak kahve 23 mutfak kahve 23

mobilya masa 12 mobilya masa 12 mobilya masa 12 mobilya masa 12

mutfak bardak 70 mutfak bardak 70 mutfak bardak 70 mutfak bardak 70

mobilya sandalye 8 mobilya sandalye 8 mobilya sandalye 8 mobilya sandalye 8

mobilya sehpa 4 mobilya sehpa 4 mobilya sehpa 4 mobilya sehpa 4

mobilya sehpa 4 mobilya sehpa 4 mobilya sehpa 4 mobilya sehpa 4

mobilya sandalye 8 mobilya sandalye 8 mobilya sandalye 8 mobilya sandalye 8

mutfak seker 340 mutfak seker 340 mutfak seker 340 mutfak seker 340

mobilya masa 12 mobilya masa 12 mobilya masa 12 mobilya masa 12

sarf silgi 123 sarf silgi 123 sarf silgi 123 sarf silgi 123

```bash
% cmp dosya1 dosya2 % cmp dosya1 dosya2 % cmp dosya1 dosya2 % cmp dosya1 dosya2 (compare files)
```

dosya1

dosya1 ve dosya2 dosya2 dosya2 dosya2 isimli dosyaları karşılaştırır; dosyalar arasında bir fark

dosya1

dosya1

varsa, bu farkların bulunduğu satır ve karakter numarasını verip durur.

Örneğin

dosya1

dosya1 dosya1 dosya1

dosya2 dosya2 dosya2 dosya2

Elma, insanlar tarafindan Elma, insanlar tarafindan Elma, insanlar tarafindan Elma, insanlar tarafindan Elma, insanlar tarafindan Elma, insanlar tarafindan Elma, insanlar tarafindan Elma, insanlar tarafindan cok sevilen bir meyvadir. cok sevilen bir meyvadir. cok sevilen bir meyvadir. cok sevilen bir meyvadir. cok sevilen bir meyvadir. cok sevilen bir meyvadir. cok sevilen bir meyvadir. cok sevilen bir meyvadir.

Uzun yillardir Uzun yillardir Uzun yillardir Uzun yillardir ben ben ben ben de de de de Uzun yillardir Uzun yillardir Uzun yillardir Uzun yillardir biz biz biz biz de de de de elma yemeyi bir elma yemeyi bir elma yemeyi bir elma yemeyi bir elma yemeyi bir elma yemeyi bir elma yemeyi bir elma yemeyi bir aliskanlik haline aliskanlik haline aliskanlik haline aliskanlik haline aliskanlik haline aliskanlik haline aliskanlik haline aliskanlik haline getirdik. getirdik. getirdik. getirdik. getirdik. getirdik. getirdik. getirdik. dosyalarına

```bash
% cmp dosya1 dosya2 cmp dosya1 dosya2 cmp dosya1 dosya2 cmp dosya1 dosya2
```

komutu uygulanırsa

```bash
dosya1 dosya2 differ: char 69, line 3 dosya1 dosya2 differ: char 69, line 3 dosya1 dosya2 differ: char 69, line 3 dosya1 dosya2 differ: char 69, line 3
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 184

yanıtını alırız. (Her satırın sonundaki satır başı karakterini de bir karakter saymayı unutmayın. cmp cmp cmp cmp komutundan daha yetenekli olan bir de diff diff diff diff komutu vardır. Bu diff diff diff diff komutunu öğrenmek de sizin ödeviniz olsun. Sınavda sorarım haaaa!

```bash
% crypt < normal_dosya > kriptolu_dosya % crypt < normal_dosya > kriptolu_dosya % crypt < normal_dosya > kriptolu_dosya % crypt < normal_dosya > kriptolu_dosya
```

Diskteki normal\_dosya normal\_dosya normal\_dosya normal\_dosya isimli dosyayı okur, klavyeden bir anahtar sözcük anahtar sözcük anahtar sözcük anahtar sözcük girmenizi ister ve bu anahtar sözcüğü kullanarak şifreli bir dosya olan kriptolu\_dosya kriptolu\_dosya kriptolu\_dosya kriptolu\_dosya dosyasını yaratır. Eğer normal\_dosya normal\_dosya normal\_dosya normal\_dosya isimli dosyayı silerseniz, geriye kalan şifreli dosyanın içeriğini sizden başka hiç kimse bir daha göremez. (root root root root kullanıcı dahi göremez). Ancak, programa verdiğiniz anahtar sözcüğü kesinlikle unutmamanız gerekir. Eğer bu sözcüğü bir unutursanız, dosyanızın şifresini çözebilmek için size hiç, ama hiç kimse yardım edemez.

```bash
% tr [-ds] [dizi_1] [dizi_2] < dosya1 > dosya2 % tr [-ds] [dizi_1] [dizi_2] < dosya1 > dosya2 % tr [-ds] [dizi_1] [dizi_2] < dosya1 > dosya2 % tr [-ds] [dizi_1] [dizi_2] < dosya1 > dosya2
```

translate dizi\_1 dizi\_1 Standart girişteki tüm karakterleri tarayarak dizi\_1 dizi\_1 kalıbına uyanları dizi\_2 dizi\_2 dizi\_2 dizi\_2 kalıbındakilerle değiştirir.

Örneğin

```bash
% tr 123 abc < dosya1 > dosya2 tr 123 abc < dosya1 > dosya2 tr 123 abc < dosya1 > dosya2 tr 123 abc < dosya1 > dosya2
```

komutu verildiğinde, dosya1 dosya1 dosyası taranarak, bu dosyada rastlanan tüm 1 1 1 1’ler

dosya1

dosya1

a a a a ile; tüm 2 2 2 2’ler b b b b ile ve tüm 3 3 3 3’ler c c c c ile değiştirilerek dosya2 dosya2 dosya2 dosya2 dosyası elde edilir.

Aynı komutu

```bash
% tr [1-3] [a-c] < dosya1 > dosya2 tr [1-3] [a-c] < dosya1 > dosya2 tr [1-3] [a-c] < dosya1 > dosya2 tr [1-3] [a-c] < dosya1 > dosya2
```

şeklinde de verebilirdik.

Komutun -s -s -s -s parametresi kullanılırsa, tekrar eden karakterden oluşan diziler tek karaktere dönüştürülür.

Örneğin, tekrarli tekrarli tekrarli tekrarli isimli dosyanın içinde "Imdaaaaaaaat!!!!!!" "Imdaaaaaaaat!!!!!!" "Imdaaaaaaaat!!!!!!" "Imdaaaaaaaat!!!!!!" dizisi varsa

```bash
% tr -s < tekrarli tr -s < tekrarli tr -s < tekrarli tr -s < tekrarli
```

komutu ekrana (standart çıktıya) "Imdat!" "Imdat!" "Imdat!" "Imdat!" sözcüğünü gönderir.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 185

```bash
% file dosya(lar) % file dosya(lar) % file dosya(lar) % file dosya(lar)
```

Parametresi olarak verilen dosyaların ne tip dosyalar olduğunu belirtir.

Acemi kullanıcılar sık sık bir dosyanın ne içerdiğini görmek için

```bash
% cat dosya_adi cat dosya_adi cat dosya_adi cat dosya_adi
```

komutunu verip, dosyayı ekrana listelemek isterler. Eğer söz konusu dosya bir ASCII text dosyası değilse, dosyanın içinde yer alan kod dizilerinden birinin terminali kilitleme olasılığı yüksektir.

Bu komutun önemi işte bu gibi durumlara düşmemek için, bir dosya ya da dosya grubunun ne tip kayıtlar içerdiğini anlamak için kullanılabilmesindedir.

Bu komutun ASCII ASCII ASCII ASCII ya da text text text text olarak nitelendirdiği dosyaların içine korkmadan cat cat cat cat, head head head head, tail tail tail tail veya more more more more komutlarıyla bakabilirsiniz.

Örneğin

```bash
% file a* b* file a* b* file a* b* file a* b*
```

komutu, adı a a a a veya b b b b harfiyle başlayan dosyaların tiplerini ekrana listeler.

```bash
abc:/home/ayfer> cd /etc cd /etc cd /etc cd /etc abc:/etc> file a* b* c* d* file a* b* c* d* file a* b* c* d* file a* b* c* d* adm: symbolic link to ../var/adm aliases: ascii text aliases.dir: empty aliases.pag: binary Computer Graphics Metafile arp: symbolic link to ../usr/etc/arp autoreply.data: c-shell commands cron: symbolic link to ../usr/etc/cron domainname: ascii text dp: directory dp.conf: English text dp.start: executable shell script dumpdates: ascii text abc:/etc>
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 186

```bash
% du [dizin adi] % du [dizin adi] % du [dizin adi] % du [dizin adi] (disk usage)
```

Parametresi olarak belirtilen dizinde (dizin belirtilmezse çalışma dizini kabul edilir) ve onun alt dizinlerinin diskte harcadıkları alanların büyüklükleri listelenir. Bu liste blok blok blok blok cinsinden verilir ve 1 blok = 512 Byte’ 1 blok = 512 Byte’dır.

1 blok = 512 Byte’ 1 blok = 512 Byte’

```bash
abc:/home/ayfer> du du du du 146 ./Mail 1 ./.elm 1086 ./burkey 1 ./.wastebasket 1473 ./docs 233 ./denemeler 91 ./kitap/bolumler 134 ./kitap 734 ./Humor 3899 .
abc:/home/ayfer>
```

Bu örneğe göre Mail Mail Mail Mail dizinindeki dosyaların toplam uzunluğu 73 Kbyte, burkey burkey burkey burkey dizini 543 Kbyte ve tüm dizinlerin toplamı da yaklaşık 1.95 Mbyte dır.

```bash
% df % df % df % df (disk free)
```

Komutun verildiği anda mount mount mount mount edilmiş olan tüm dosya sistemlerinin toplam kapasitelerini, ne kadarlarının kullanıldığını ve boş yer miktarını Kbyte Kbyte Kbyte Kbyte cinsinden listeler. SVR4 UNIX kullanıcıları, aşağıdakine benzer bir liste alabilmek için, komutu “df -k” “df -k” “df -k” “df -k” şeklinde kullanmak zorunda kalabilirler.

```bash
abc:/home/ayfer> df df df df Filesystem kbytes used avail capacity Mounted on /dev/sd0a 16327 12417 2278 84% / /dev/sd0g 413767 367489 4902 99% /usr /dev/sd0h 529020 419638 56480 88% /home
abc:/home/ayfer>
```

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 187

```bash
% tty % tty % tty % tty (teletype)
```

Terminalinizin sisteme hangi arabirimden bağlı olduğunu merak ederseniz kullanmanız gereken komuttur.

```bash
abc:/home/ayfer> tty tty tty tty /dev/ttya
abc:/home/ayfer>
```

```bash
% bc % bc % bc % bc (high Precision calculator)
```

Oldukça kullanışlı bir hesap makinası programıdır. Tipik kullanıma bir örnek

```bash
abc:/home/ayfer> bc bc bc bc 12+19 12+19 12+19 12+19
31
37 - 19 37 - 19 37 - 19 37 - 19
18
9 * 6 9 * 6 9 * 6 9 * 6
54
84/7 84/7 84/7 84/7
12
sqrt(64) sqrt(64) sqrt(64) sqrt(64)
8
quit quit quit quit
abc:/home/ayfer>
```

```bash
% split [ -n ] cok_buyuk_dosya % split [ -n ] cok_buyuk_dosya % split [ -n ] cok_buyuk_dosya % split [ -n ] cok_buyuk_dosya
```

Çok büyük dosyaları daha küçük parçalara ayırmak için kullanılır. Eğer -n -n -n -n parametresiyle bir sayı verilmezse çok-büyük-dosya çok-büyük-dosya çok-büyük-dosya çok-büyük-dosya 1000’er satırlık parçalara bölünecek ve xaa, xab, xac,...., xaz, xba, xbb, ..... xaa, xab, xac,...., xaz, xba, xbb, ..... xaa, xab, xac,...., xaz, xba, xbb, ..... xaa, xab, xac,...., xaz, xba, xbb, ..... diye isimler altında gereği kadar dosya yaratılacaktır. Satır başı karakterleri (CR : Carriage Return) ile ayrılmış bilgi grupları satır kabul edilecektir. Eğer dosyanın içinde hiç satır başı karakteri yoksa veya makul sıklıkta satır başı karakteri yoksa, parçalama pek başarılı olmayabilir.

Bir dosyayı 100’er satırlık parçalara bölmek isterseniz, kullanacağınız komut

```bash
% split -100 dosya split -100 dosya split -100 dosya split -100 dosya
```

olmalıdır.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 188

```bash
% join dosya1 dosya2 > yeni_dosya % join dosya1 dosya2 > yeni_dosya % join dosya1 dosya2 > yeni_dosya % join dosya1 dosya2 > yeni_dosya
```

İki dosyayı yanyana yanyana yanyana yanyana birleştirmek için kullanılır. Sanırım bir örnekle açıklaması çok daha kolay olacak :

dosya1

dosya1 dosya1

dosya1

dosya2 dosya2 dosya2 dosya2

isimler isimler isimler isimler telefonlar telefonlar telefonlar telefonlar ali ali ali ali

312-111 323 333 312-111 323 333 312-111 323 333 312-111 323 333

veli veli veli veli

212-777 666 666 212-777 666 666 212-777 666 666 212-777 666 666

selami selami selami selami

266-345 345 345 266-345 345 345 266-345 345 345 266-345 345 345

```bash
% join dosya1 dosya2 > dosya3 join dosya1 dosya2 > dosya3 join dosya1 dosya2 > dosya3 join dosya1 dosya2 > dosya3
```

komutundan sonra

dosya3 dosya3 dosya3 dosya3

isimler telefonlar isimler telefonlar isimler telefonlar isimler telefonlar ali 312-111 323 333 ali 312-111 323 333 ali 312-111 323 333 ali 312-111 323 333 veli 212-777 666 666 veli 212-777 666 666 veli 212-777 666 666 veli 212-777 666 666 selami 266-345 345 345 selami 266-345 345 345 selami 266-345 345 345 selami 266-345 345 345

```bash
% touch dosya % touch dosya % touch dosya % touch dosya
```

Bazen, içinde hiç bir şey olmayan boş bir dosya yaratmanız gerekebilir. Böyle bir durumda touch touch touch touch komutundan yararlanabilirsiniz.

Eğer parametre olarak verdiğiniz dosya, diskinizde zaten varsa diskinizde zaten varsa diskinizde zaten varsa diskinizde zaten varsa, o zaman bu dosyanın en son erişildiği tarih ve saat yenilenecektir. Böylece, dosyanızı sistem yöneticisinin “Son 10 gündür ellenmemiş dosyaları sil” “Son 10 gündür ellenmemiş dosyaları sil” şeklinde “Son 10 gündür ellenmemiş dosyaları sil” “Son 10 gündür ellenmemiş dosyaları sil” vereceği genel temizlik komutlarından kurtarmış olursunuz.

Eğer parametre olarak belirttiğiniz dosya yoksa, bu isimde bir boş dosya (sıfır byte uzunluğunda) yaratılır.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 189

X-Windows X-Windows X-Windows X-Windows X11 R5 & X11 R6

X11 R5 & X11 R6

X11 R5 & X11 R6

X11 R5 & X11 R6

Bilgisayar dünyasına ilk olarak Apple marka MacIntosh bilgisayarlarıyla kazandırılmış olan Grafik Kullanıcı Arabirimi (GUI : Graphical User Interface) kavramı MS-Windows ile kişisel bilgisayar (PC) dünyasına; X-Windows ile de UNIX dünyasına atladı.

Bir fare ve grafik bir ekranla bilgisayarların kullanımı çok kolaylaştı.

Bilgisayarda yapılması istenen işle ilgili olan ikonu gösterip tıklamak yeterli bir hale geldi.

X-Windows yazılım paketi MIT (Massachusetts Institute of Technology) tarafından geliştirilinceye kadar, UNIX bilgisayarlarının ekranları 24 satır ve her satırda 80 kolondan oluşan zavallı bir görünümün dışına çıkamıyorlardı.

X-Windows; X11R5 (X11 Release 5) sürümüyle birlikte grafik ekran sürebilen tüm UNIX bilgisayarlarında kullanılan bir Grafik Kullanıcı Arabirim standardına dönüştü. Bu standart etrafında çeşitli Pencere Yönetim (Window Manager) yazılımları üretildiyse de hepsinin temelinde X11 yazılımı yatmaktadır. Bu pencere yönetici yazılımlarına örnek olarak Openlook Openlook Openlook Openlook, Motif Motif Motif Motif, VUE VUE VUE VUE ve twm twm twm twm (tab window manager; X11R5 in standart pencere yöneticisi) gösterilebilir.

Eğer UNIX bilgisayarınızın grafik ekranı ve uygun bir X11 yazılım paketi varsa hayat sizin çok kolay ve zevkli bir hale gelecektir. Ekranınızda bir sürü pencere açıp, her pencerede farklı bir uygulama başlatıp, UNIX'in çok iş düzenini desteklemesi sayesinde bütün uygulamalarınızı aynı anda yürütebilirsiniz. Hele bilgisayarınız bir ağda yer alıyorsa, pencerelerinizden bir kaçında başka bilgisayarlara bağlantı kurarak (rlogin rlogin rlogin rlogin veya telnet telnet telnet telnet) bir kaç bilgisayarı aynı anda kullanabilirsiniz. (MS-Windows kullanıcılarının çatladığını duyar gibiyim...)

Bilgisayarınızdaki X olanakları hakkında sistem yönetinizden bilgi alabilirsiniz.

---
*Kaynak: `KİM KORKAR UNİX TEN/141-189.pdf`*
