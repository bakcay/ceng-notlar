# Linux Kurulumu Ve Baslangiç

## **LINUX KURULUMU VE BAŞLANGIÇ**

Linux hakkında ilk önemli dökümanlar yazıldığında, Linux çalıştırabilecek bilgisayarların özellikleri önemliydi. Linux 32 bitlik bir işletim sistemi olduğundan en az 80386SX işlemcilerle çalışmaktadır. 8086 ve 80286 işlemcili IBM-PC uyumlu kişisel bilgisayarlar Linux tarafından desteklenmemektedir. Hafıza olarak en az 4 Mbyte RAM ( yoğun işlemler için 12 veya 16) tavsiye edilmektedir. Teknik olarak 2 Mbyte ile de çalışması gerekir. Pratik olarak bugün piyasada bulunan hemen hemen her IBM-PC uyumlu kişisel bilgisayarda Linux çalışabilmektedir.

8 Mbyte RAM’a sahip herhangi bir 486 üzerinde hemen hemen her türlü uygulama rahatlıkla çalıştırılabilmektedir. Tabii ki daha fazla RAM ve daha hızlı işlemciler sistemin genel olarak daha hızlı çalışmasını sağlayacaktır.

Linux tarafından desteklenen donanımlar her geçen gün değişiyor. Bilgisayarınızda bulunan herhangi bir donanımın desteklenip desteklenmediğini *Hardware-HOWTO *dosyasından öğrenebilirsiniz.

Yine de daha önce yazılanları kısaca tekrar edersek,

Kişisel bilgisayarlarda INTEL, AMD, CYRIX şirketlerinin tüm 80386, 486, 586, 686, Pentium, PentiumPro işlemcileri

Tüm IDE, MFM, RLL sabit diskler

Çoğu SCSI sabit disk denetçileri

Çoğu Ethernet ve G/Ç kartları

Birçok VGA,SVGA,EGA,HERCULES görüntü kartları Linux tarafından desteklenmektedir.

Linux başka işletim sistemleri ile aynı sabit diskte bulunabilir. Makinanıza Linux yüklemek için mevcut işletim sisteminizi kaldırmak zorunda değilsiniz. Fakat yine de Linux yükleyebileceğiniz bir miktar alan ayırmak zorundasınız. Bir bilgisayara Linux yüklemek için bilgisayarınız üzerinde bir başka işletim sisteminin bulunmasına gerek yoktur, Linux tam anlamıyla kendi başına bir işletim sistemidir.

“Linux sabit disk üzerinde ne kadar yer kaplar?” sorusuna kesin bir cevap vermek oldukça zor, zira bu hangi yazılımları yükleyeceğinize ve ne kadar kullanıcı alanı istediğinize çok bağlıdır. Yine de kaba rakamlar vermek gerekirse, 40 Mbyte’lık bir alana çalıştırılabilir durumda ve işinizin çoğunu görebilecek bir Linux kurulabilir. Tüm paketleri yüklemeye kalktığınızda ise kabaca 250 Mbyte kadar yer kaplayacaktır.

Linux, çok çeşitli gruplar tarafından sürekli geliştirilen bir işletim sistemidir. Belirli kişiler ve topluluklar Linux için geliştirilen temel işletim sistemini ve uygulama yazılımlarını bir araya getirerek dağılımlar oluştururlar. Bir Linux dağılımı temel olarak bir makineye Linux kurmak ve o bilgisayar üzerinde Linux’la çalışmak için gerekecek tüm yazılımları ve paketleri içerir, bu yazılımların yüklenmesi için bir yükleme yazılımı sağlar.

Şu an mevcut çok çeşitli Linux dağılımları mevcuttur. Bu dağılımlar içerdikleri paketler ve yükleniş çeşitleri açısında bazı ufak tefek farklılıklar gösterseler de temelde aynı işletim sistemini yüklerler. Bir Linux dağılımı bir araya getirildiği zamandaki güncel işletim sistemini içermektedir. Örnek olarak Linux işletim sisteminin temeli olan çekirdek neredeyse her hafta yenilenerek geliştirilmektedir. Oysa dağılımlar senede ancak birkaç kere oluşturulurlar.

Linux dağılımları geleneksel olarak 3.5” lik disketler halinde hazırlanırlar. (her biri bir 3.5” lik diskete sığabilecek seri dizinler şeklinde). Her konu ile ilgili bir seri disket bulunur. (örnek olarak n serisi ağ uygulamaları için n1,n2,n3... şeklinde)

**2.2 Sabit Disk Üzerinde Linux İçin Yer Açmak**

Linux işletim sistemini yüklemek için sabit diskiniz üzerinde Linux için bir miktar yer ayırmak zorundasınız. Herhangi bir sabit disk bir işletim sisteminde kullanılabilmesi için ilk olarak bölümlere (partition) ayrılır. Daha sonra bu bölümler işletim sistemine uygun şekilde formatlanır. Linux işletim sistemi kendi disk formatını (ext2) kullanır. En yüksek verimi sabit disk üzerinde, kendi bölümünde, kendi disk formatı altında çalıştığı zaman verebilir. Eğer ayrı bir bölümlendirme yapılmıyorsa, tavsiye edilmese bile MS-DOS formatlı bir disk üzerinde de kurabilir (UMSDOS) ancak bu sistemin performansı diğerine göre oldukça düşük olacaktır. Bu dökümanın geriye kalan tüm kısımlarında bilgisayarınıza Linux yüklemek için sabit disk üzerinde Linux’a özgü bir bölüm ayrılacağı ve bu bölüme yükleyemeceği kabul edilecektir.

MS-DOS formatlı bir disk hiyerarşisi altına Linux kurmak için *USMDOS-HOWTO* dökümanından yararlanabilirisiniz. Eğer bilgisayarınızı bir süredir kullanıyorsanız, büyük bir ihtimalle sabit diskinizin tümünü kullandığınız işletim sistemi için ayırmış durumdasınız.

MS-DOS kullanıyorsanız diskinizin bir (sadece C veya birden fazla (C: D:..) bölüme ayrılmış durumda olabilir. MS-DOS altında bir disk üzerinde en fazla 4 bölüm olabilir. (primary partition). Eğer daha fazla bölüme ihtiyaç varsa temel bölümlerden biri genişletilmiş bir bölüm olarak ayrılır (extended partition) ve bu bölüm üzerinde mantıksal bölümler ayrılır(logical partitions).

Bilgisayarınızda birden fazla bölüm varsa bir bölümü boşaltıp bu bölümü Linux için ayırabilirsiniz. Eğer tek bölümünüz varsa, veya mevcut bölümlerinizden birini tümüyle harcamak istemiyorsanız diskinizi yeniden bölümlemeniz gerekecektir. Klasik olarak bu durumda bölmek istediğiniz bölümdeki yazılımların yedeğini almanız, daha sonra MS-DOS altında *fdisk* yazılımı yardımı ile söz konusu bölümü silmeniz, yeni boyutu ile yeniden yaratmanız, bu bölümü format komutu ile formatlandırmanız ve yedeğini aldığınız yazılımları yeniden yerleştirmeniz gerekecektir.

Bazı yazılımlar mevcut bölümünüzü iki parçaya ayırabilirler. Örnek olarak *fips* bu amaçla kullanılan bir yazılımdır. (Diskinizin üzerinde işlem yapan her yazılım az da olsa disk üzerindeki bilgilere zarar verme riski taşır. Bu tür yazılımlar ile çalışmadan önce önemli olduğunu düşündüğünüz bilgilerin yedeğini almaya özen gösterin). Ftips, defrag programı kullandıktan sonra bölümünüzü sizin belirleyeceğiniz boyutlarda 2 bölüme ayırabilir.

Eğer bilgisayarınızı yeni alıyorsanız veya yeni bir disk alıyorsanız, bu diskin tamamını veya bir bölümünü Linux için kullanabilirsiniz. Bu amaçla diskinizde sadece Linux kullanmak istemediğiniz bölümleri ayırmanız (ve gerisini boş bırakmanız) yeterlidir. Linux bölümlerinin Linux altından formatlanması gerekecektir.

Yoğun olarak Linux kullanan yerler için standart olarak dağıtımdan gelen işletim sistemini ayrı bir bölüme yüklemeleri kullanıcı alanları (/home) ve sonradan yüklenen yazılımlar (/usr/local) için ayrı bir alan ayırmaları tavsiye edilebilir. Bu sayede, işletim sistemi güncellemek son derece kolaylaşır, yeni işletim sistemi yüklerken sadece işletim sisteminin bulunduğu bölüm üzerinde işlem yapılır ve bu sayede kullanıcı alanlarının veya sonradan (dağıtım dışı) yüklenen yazılımların zarar görmeleri engellenebilir.

Her bir bölüm için ne kadar yer ayrılacağı hakkında çok şey yazılmıştır. Ne var ki yazılanların birçoğu sabit disklerin nadiren 200 Mbyte sınırını geçtiği günlerden kalmaktadır. Linux’un kaplayacağı alan, hangi paketleri kullanacağınıza çok bağlıdır. Kabaca bir disketin 2-3 Mbyte arasında yer kaplayacağını düşünerek, yüklemek istediğiniz disketleri hesaplayarak kaba bir tablo çıkartabilirsiniz. Tecrübeli bir Linux kullanıcısı hangi yazılımları kullanıp hangilerini kullanmadığını daha iyi belirleyecek durumda olacaktır. Dolayısı ile yeni bir kullanıcı ortalama olarak 200-300 Mbyte kadar bir yer ayırmak isteyecektir. Bu, günümüzün disk kapasiteleri düşünülünce o kadar büyük bir alan değildir.

Takas alanı konusunda da çok şey yazılmıştır. Birçok kaynak takas bölümü için ayırması gereken alanın gerçek hafızanın 2 katının biraz fazlası olarak kabul edilmektedir. Pratikte 10-60 Mbyte arasında bir alan fazlasıyla yeterli kalmaktadır. Ancak takas bölmeleri 128 megabytedan daha büyük olamaz. Eğer 128 megabytedan daha büyük takas alanı gerekiyorsa birden fazla takas bölmesi ayartmalısınız. Toplam 16 tane takas bölmeniz olabilir.

Takas alanı kullanırken, bir seferde daha fazla uygulama çalıştırmanızı sağlayacak şekilde Linux kullanılmayan sayfaları hafızadan diske taşır. Ancak, takas işlemi genelde yavaş olduğundan gerçek fiziksel hafızanın yerini dolduramaz. Ama çok fazla hafıza isteyen uygulamalar (X Window System gibi) eğer yeteri kadar fiziksel hafızanız yoksa takas alanına bel bağlar.

Tercih olarak 1.2 Gbyte’lık bir disk üzerinde;

**Linux nedir denemek isteyen bir kişi için**

Bölüm 1: DOS 1000 Mbyte

Bölüm 2: Linux 180-200 Mbyte

Bölüm 3: Linux “swap” bölümü 10-20 Mbyte

**İşinde arada sırada Linux kullanan birisi için**

Bölüm 1: DOS 400 Mbyte

Bölüm 2: Linux 400 Mbyte

Bölüm 3: Linux takas bölümü 32 Mbyte

Bölüm 4: DOS( DOS altında D: olarak gözükecek) 400 Mbyte

**İnternet üzerinde sadece Linux kullanan bir bilgisayar için**

Bölüm 1: Linux 100 Mbyte

Bölüm 2: Linux takas bölümü 60 Mbyte

Bölüm 3: Linux /usr 400 Mbyte

Bölüm 4: Linux /home 600 Mbyte

**2.3 Bilgisayarın Linux ile Açılması**

Bilgisayarın sabit diski üzerinde yer ayırdıktan, bir Linux dağıtımı bulduktan sonra artık Linux yüklemek için yapılması gereken, yükleme yapmanıza yardımcı olmaya yetecek şekilde bilgisayarınızı Linux altında çalıştırmaktır. Bu amaçla *boot *ve *root disketi* adı verilen iki disket kullanılması yeterlidir. Bu disketlerden boot disketi bilgisayarınız üzerindeki donanıma uygun bir Linux çekirdeği (kernel) içerir ve bilgisayarın Linux ile açılmasını sağlar, root disketi adı verilen diğeri ise makinanız Linux olarak açıldığı zaman çalıştıracağı yazılımları içeren ve Linux’un çalışması için gereken sistem programlarını içerir . Bu iki disketi,

MS-DOS altındaki sistem disketine benzetmek mümkündür.

Boot ve root disketleri, Linux dağılımı ile birlikte gelirler. Eğer bir CD-ROM dağıtımı kullanıyorsanız, büyük ihtimal disketler CD-ROM ile beraber geleceklerdir. Eğer dağıtımı Internet’ten alıyorsanız bu disketler bir disket görüntüsü olarak bulunacaklardır. Yapmanız gerek bu disket görüntülerini normal disketlere bu amaç için yazılmış bir yazılımla aktarmak ve açılış disketlerini oluşturmaktır. Bunun için RAWRITE.EXE programını kullanabilirsiniz.

Root disketi için genelde bir veya iki seçenek bulunmaktadır. Genelde kullanılan disket color.gz adını alır.

Boot disketi için aynı şeyi söylemek mümkün değildir. Zira boot disketi Linux çekirdeğini içermektedir. Her işletim sistemi, o işletim sistemi altında çalışacak olan bilgisayar üzerindeki donanıma erişebilmek için bazı destekler içerir. Ne var ki her donanım kendisine göre bir takım farklılıklar gösterir. Linux bilgisayarınız üzerinde bulunan birçok donanım için destek verebilir, ne var ki tüm donanım desteğini tek bir çekirdekte toplamak çekirdeğin gereksiz yere büyümesine ve hantallaşmasına neden olacaktı( Bilgisayarınızda ses kartı donanımı yoksa çekirdeğin ses kart desteğine ihtiyacınız olmayacaktır, yapılan sadece gereken destekleri ekleyerek çekirdeğin verimini artırmak demektir.)

Linux çekirdeği gerektiğinde destek verdiği donanımları destekleyecek şekilde güncellenebilir. Ancak Linux yükleyebilmek için, seçeceğiniz yükleme yöntemine göre bazı donanımlara destek vermesi gerekmektedir. Örnek vermek gerekirse, NFS üzerinden Linux yüklemek için çekirdek içerisinde mutlaka ağ (network) desteğinin olması gerekmektedir ama ses kartı desteğinin olmasına gerek yoktur. Linux yükledikten sonra derleyeceğiniz bir çekirdeğe ses kartı desteği vermesini sağlayabilirsiniz.

Bir işletim sisteminin sabit diske yüklenme aşamasında kullanıcıya sağlayacağı en büyük kolaylık, deneyimli kullanıcılar için tüm paketleri kurmadan önce sormak, Linux’u bilmeyen ve sabit diskine Linux kurmak isteyen yeni kullanıcılar için ise kurulum aşamasını mümkün olan en az soru ile bitirip daha önceden belirlenmiş birtakım paketleri otomatik olarak yüklemektir.

Çok farklı donanımların olması Linux yükleyebilmek için bir dizi boot disketinin oluşmasına neden olmuştur. Güncel bir Linux dağıtımında hangi boot disketlerinin hangi donanımlara destek verebildiğini görebilmek için ilgili dağıtımla gelen README dosyalarına bakmak gerekecektir. Şu anki Slackware dağıtımı ile gelen boot disketlerinden bazıları ;

**Bare.i** IDE sabit disklere, sabit disk veya IDE/ATAPI CD-ROM’lardan yükleme yapmak için

**Net.i** IDE sabit disklere, NFS üzerinden yükleme yapmak için.

**Scsinet.s** SCSI sabit disklere, NFS üzerinden yükleme yapmak için. Buna ek olarak değişik SCSI denetçileri için 25 kadar değişik boot disketi bulunmaktadır.

**Xt.i** Bu açılış disketinde sadece IDE ve XT sabit disk sürücüleri vardır.

Boot ve root disketlerinizi de elde ettikten sonra artık bilgisayar ilk defa Linux altında çalışmak için hazırdır. Boot disketini takarak sistemi açın, (PC’nin açılma sırasının A:,C: olmasına dikkat ediniz). Disket açılır açılmaz yaklaşık bir sayfalık bir mesaj verecek ve kullanıcıdan ek bir parametre isteyip istemediğini soracaktır.

Bu noktada çalışacak olan yeteneğe birçok ek parametre verilebilir. Eğer herşey yolunda giderse bu noktada özel bir parametre belirtmeye gerek kalmayacaktır. Boot disketi parametreleri hakkında *BootPrompt-HOWTO* içerisinde detaylı bilgi bulabilirsiniz. Bu aşamayı geçtikten sonra çekirdek yüklenmeye başlayacak ve bir dizi mesaj geçecektir. Bu mesajlar çekirdeğinizin bilgisayar üzerindeki donanımları tanıması ve çeşitli hizmetleri çalıştırması ile ilgili mesajlardır. Çekirdeğin donanımınızı ne şekilde tanıdığı bu mesajlardan anlaşılır. Yükleme yapabilmek için çekirdeğin sabit diskinizi ve ağ bağlantısı kullanacaksınız Ethernet kartınızı doğru olarak tanımış olması gerekecektir.

Daha sonra kullanıcıdan root disketini yüklemesi için bir mesaj çıkacaktır. Bu aşamada boot disketi yerine root disketi takılmalıdır. Kısa bir yüklemeden sonra bir mesaj çıkacak ve ardından

login:

mesajı ile karşılaşılacaktır. Tebrikler!. Artık Linux altında çalışmaya başlayabilirsiniz. Bilgisayarınız şu anda sizden bir kullanıcı ismi beklemektedir. “root” yazarak sisteme girin.

**2.3.1 Ön Hazırlık**

Yüklenmenin her aşaması setup yazılımı tarafından yürütülür. Ancak ilk olarak disk alanlarının tanımlanması gerekmektedir.Bu amaçla setup programı kullanılır.

Linux altında bir bilgisayara bağlı her cihaza bir dosya gibi erişilebilir. Her cihaza karşılık gelen bir sistem dosyası mevcuttur.cihazlarla ilgili dosyalar /dev dizini altında yer alır. IDE sabit diskler “hd”, SCSI sabit diskler “sd” olarak adlandırılır. Aynı anda bir bilgisayara birden fazla disk bağlanmış olabilir. Diskler sırasıyla a b c d olarak adlandırılır. Her disk üzerinde birden fazla bölüm olabilir. Bu bölümler 1 2 3 4 olarak numaralandırılır. Örnek:

/dev/hda, bir numaralı IDE (Primary Master) diski

/dev/hda1, bir numaralı IDE diskin ilk bölümü (DOS altında c:)

/dev/hda2, bir numaralı IDE diskin ikinci bölümü

/dev/hdb, iki numaralı IDE (Primary Slave) diski

/dev/hdc, üç numaralı IDE (Secondry Master) disk

/dev/hdd, dört numaralı IDE (Secondry Slave) disk

/dev/sdb3, ikinci SCSI sabit diskin üçüncü bölümü

göstermektedir.

**2.3.2 FDISK**

Birden fazla sabit disk varsa hangisi ile ilgilenecek belirtilmelidir. Fdisk’i kullanırken dikkat edilmelidir. Her an yanlış bir diski formatlama yapabilirsiniz.

Fdisk komutu hardisk bölümlerinin düzenlenmesi için kullanılır. Eğer komut satırında parametre verilmezse fdisk ilk bulduğu disk üzerinde işlem yapacaktır. Komut satırında istenilen disk belirtilmelidir.

Fdisk paremetreleri:

/fdisk –v: Fdisk programının sürümünü ekrana getirir.

Fdisk –l: /dev/hda, /dev/hdb, /dev/sda, /dev/sdb, /dev/sdc, /dev/sdd, /dev/sde, /dev/sdf, /dev/sdg ve /dev/sdh disklerinin (varsa) bölümlendirme tablosunu ekrana yazar ve çıkar.

Fdisk –s <disk-bölümü>: Eğer bir DOS bölümü değilse (bölüm numarası 10’dan büyük), sözkonusu disk bölümünün büyüklüğü bayt cinsinden ekrana yazılır.

**2.3.3 Setup Programı**

Setup Linux yüklemek için gereken temel birçok işlemi yapabilir. Ok tuşları yardımıyla menüler arasında gezerek işlemleri tamamlayabilirsiniz.ekrana gelen menüler aşağıdadır.(Linux sürekli gelime halinda olduğu için zamanla değişiklikler olabilir.)

Hint: If you have trouble using the arrow keys on your keybord,

You can use “+”, “-“ and TAB instead. Which option would you like?

HELP Read the Slackware setup HELP file

KEYMAP Remap your keyboard

MAKE TAGS Tagfile customization program

TARGET Select target directory \[now:/\]

SOURCE Select source media

DISK SETS Decide which disk sets you wish to install

INSTALL Install selected disk sets

CONFIGURE Reconfigure your Linux system

PKGTOOL Install or remove packages with Pkgtool

EXIT Exit Slackware Linux Setup

< OK > <Cancel>

**HELP Menüsü: **Setup programı hakkında bazı ipuçları verecektir.

**KEYMAP Memüsü: **Bu menü ile Amerikan klavye dışında bir klavye tanımlamak mümkün olacaktır.

**MAKE TAGS Menüsü: **Bu menü yardımı ile dağıtım disketlerinde özel uzantılı dosyalar hazırlayarak hangi paketlerin yükleneceğini otomatik olarak belirlemek mümkündür. Bu sayede eğer benzer makineler yüklenecekse yüklenecek paketler bir kere belirlenir ve bir daha menülerden ekstradan paketlerin seçilmesine gerek kalmaz. Büyük ihtimalle buraya kadar henüz bir takas alanı tanımlamamışsınızdır. Setup yazılımı bu durumu anlar ise bir takas bölmesi oluşturulması için aşağıdaki menüyü ekrana getirecektir.

**ADDSWAP Menüsü: **fdisk ile ayırdığınız takas bölümünü uygun şekilde formatlar ve bu bölümü kullanıma açar. Setup yazılımı hangi disk bölümünün takas bölümü olarak ayrıldığını otomatik olarak bulacaktır. Daha sonra söz konusu alanları form atlayacak ve bu takas alanını sistem belleğine ekleyecektir. (Her adımda bir onay isteyecektir.)

**TARGET Menüsü: **Linux’un hangi bölüme yükleneceğini belirler. Bu menüye girildiği zaman Linux’un disk formatına (ext2) sahip (sabit disk bölümü numarası 83 olan) tüm disk bölümleri gösterilecek ve içerlerinden hangisine Linux kurulması istenileceği sorulacaktır. Bu aşamadan sonra o disk bölümü kullanıcı isterse formatlanacaktır. Burada iki format seçeneği vardır. Bu seçeneklerin ikincisinde disk önce hatalar için taranacak daha sonra formatlanacaktır. Eğer Linux disk formatında başka bölümler varsa bu bölümlerin kullanılmasının istenip istenmediği sorulacaktır. Bu sayede disk hiyerarşisinin herhangi bir kısmını bu ek disk bölümleri üzerine kurmak mümkündür. Son olarak Linux tarafından desteklenen başka disk bölümleri varsa (Örneğin DOS) bu bölümlere Linux altından erişim yapılmasının istenip istenmediği sorulacak ve bu bölümler için hiyerarşi içerisinde bir dizin atanması istenecektir.

**SOURCE Menüsü: **bu menü Linux dağıtımının nerede aranması gerektiğini belirler. Buradaki seçenekler

SOURCE MEDIA SELECTION

Where do you plan to install slackware Linux from?

1 Install from a hard drive partition

2 Install from floppy disks

3 Install via NFS

4 Install from a pre-mounted directory

5 Install from CD-ROM

1 Numaralı seçenek, Linux dağıtımını bir sabit disk bölümünde aramak için kullanılacaktır. Bu seçenekle örnek olarak DOS kısmında bulunan dağıtım disketlerinden yükleme yapılabilir.

2 Numaralı seçenek, disketlerden yükleme yapılmaktadır. Çalışır bir sistemi birkaç disketle oluşturmak mümkündür. Ancak günümüzde tercih edilmemektedir.

3 Numaralı seçenek, NFS üzerinden yükleme yapmak için kullanılmaktadır. Burada bilgisayar ağına bağlı olması, bu bilgisayar ağı üzerindeki bir sunucu üzerinde erişim izni bulunan bir dizin altında dağıtım disketlerinin bulunması gerekmektedir. Bu seçenekle yükleme yapmak için boot disketi içerisinde yer alan diskette ağ desteğinin bulunması gerekmektedir. Bu seçeneğin ardından bilgisayarın (geçici) IP numarası varsa ağ üzerindeki yönlendiricinin (router-getway) IP numarası, ağ maskesi (subnet mask), NFS sunucu IP numarası ve sunucu üstünde dağıtım disketlerinin bulunduğu hiyerarşi gibi ağ ile ilgili parametreler sorulacaktır. Bu soruların cevabını sistem yetkilisinden öğrenmeniz ve onun onayını almanız gerekecektir.

4 Numaralı seçenek, aslında 1 numaralı seçeneğe çok benzemektedir. Aradaki fark bu durumda sistem hiyerarşisine bağlanmış (mounted) bir dizin içerisinde dağıtım disketlerinin bulunmasıdır.

5 Numaralı seçenek ise CD-ROM’dan yükleme yapmak içindir.

**DİSKSETS Menüsü ******

CUS Also prompt for CUSTOM disk sets

A Base Linux system

AP Various Applications that do not need X

D Program Development (C, C++, Lisp, Perl etc.)

E GNU Emacs

F FAQ lists, HOWTO documentation

K Linux kernel source

N Networking (TCP/IP, UUCP, Mail, News)

T TeX typesetting sftware

TCL Tcl/Tk script languages

X Xfree86 X Window System

XAP X Aplications

XD X Server Development kit

XV Xview (Openlook Window Manager, apps)

Y Games (tahat do not require X)

**A Serisi (8 disket)**: Temel işletim sistemi bu disketlerde yer alır. Temel disk hiyerarşisi yaratılır, sistemin çalışması için hayati olan yazılımlar, terminal yazılımları, kabuklar (shell), disk düzenleme yazılımları, kütüphaneler, Linux çalıştırmak için LILO ve LOADLIN bu disketlerdedir.

**AP Serisi (5 disket): **X Window ortamı gerektirmeyen uygulama yazılımlar. Metin editörleri, ghostscript, man sayfaları, midnight commander (Norton Commander benzeri bir yazılım) bu disketlerde yer alır.

**D Serisi (13 disket): **Tüm programlama dilleri ve destek yazılımları bu disketlerde yer alır. Eğer kendinize yeni bir Linux Çekirdeği derlemeyi düşünüyorsanız bu seriye ihtiyacınız var.

**E Serisi (8 disket): ** EMACS editörü.

**F Serisi (2 disket): **Linux hakkında birçok doküman ve açıklama bu disketlerde yer alır. Yeni başlayan birisi bu disketleri mutlaka yüklemesi gerekir. Söz konusu dokümanlar sıkıştırılmış halde

/usr/doc

/usr/doc/faq

/usr/doc/faq/HOWTO

dizinlerine yüklenecektir. Dokümanlar sıkıştırılmış olduğundan zless gibi sıkıştırılmış dosyaları destekleyen bir yazılımla okunmaları gerekir.

**K Serisi (6 disket): **Çekirdeğin kaynak kodu burada bulunur. Eğer kendi donanımınıza uygun bir çekirdek derlemek istiyorsanız bu seriye ihtiyacınız var. FTP arşivlerinden kaynak kodu olarak bulacağınız bazı yazılımlar da bu hiyerarşi altında yer alan bazı dosyalara ihtiyaç duyacaklardır.

**N Serisi (6 disket) :** Ağ desteği bu diskler ile sağlanmaktadır. E-posta okuma yazılımları, lynx, www sunucusu, haber grubu okuma yazılımları bu disketlerin içerisinde yer alan yazılımlardır.

**T Serisi (9 disket):** TeX. TeX yüklerken üç temel seçenekle karşılaşacaksınız. İlk seçenek hangi TeX yardımcı paketlerini isteyeceğinizi sorar. İkinci seçenek hangi dil için makro tanımları istediğinizi sorar. Son seçenek yazı tipleri hakkında tercihlerinizi sorar.

**TCL Serisi (2 disket):** X Window altında kullanımı basit bir programlama dili ve bu dili ile yazılmış bazı uygulama yazılımları (tkdesk).

**X Serisi (16 disket): **X Window desteği. Bu disketlerin büyük kısmı değişik grafik kartları için X window sunucuları ve yazı karakterlerinden oluşmaktadır. Linux yüklediğiniz bilgisyar üzerindeki grafik kartını bilmeniz ve buna uygun bir sunucu seçmeniz gerekmektedir.

**XAP Serisi (4 disket): **X Window altında çeşitli uygulamalar: santranç, gnuplot, xv, xfileman, windows95 benzeri X Window arayüzü bu seriler içerisinde yer almaktadır.

**XD Serisi (3 disket):** Xserver geliştirmek için kütüphane ve uygulama yazılımları.

**XV Serisi (3 disket):** OpenLook desteği veren yazılımlar. Bu sayede X Window altında Sun bilgisayarlarda yer alan Open Windows benzeri bir ortam kullanılabilir.

**Y Serisi (1 disket):** Minik birkaç oyun.

**INSTALL Menüsü: **Seçtiğiniz disk serilerini belirlediğiniz kaynaktan, belirtilen hedef disk bölümüne aktarır. Disk serileri içerisinde yer alan paketleri ne şekilde yüklemek istediğiniz konusunda birtakım seçenekler olacaktır. Bunlar:

NORMAL Use the default tagfiles for verbose prompting

MENU Choose package subsystems from interactive menus

CUSTOM Use custom tagfiles in the package directories

PATH Use tagfiles in the subdirectories of a custom path

EXPERT Cgoose individual packages from interactive menus

NONE Use no tagfiles-install everything

**NORMAL**: Bu seçenek ile gerekli paketler yüklenir, diğer paketler için kısa bir açıklama yazılır ve kullanıcının fikri sorulur.

**MENU ve EXPERT:** Bu seçeneklerde her disk serisi yüklenmeye başlanırken o seride yer alan tüm paketler bir menü içerisinde yer alır. Kullanıcı istediği paketleri işaretler ve bunların yüklenmesini sağlar.

**CUSTOM ve PATH:** Daha önce belirtilen TAGFILE dosyaları yardımıyla yükleme yapmak için kullanılır. Bu durmda belirli bir uzantıya sahip dosyalar içerisinde (TAGFILE) yüklenmesi gereken yazılımlar belirtilir. Bu seçenek ile TAGFILE’ların uzantısı belirtilir ve o uzantılı dosyalarda bulunan paketler yüklenir.

**NONE:** Herşeyi kuracaktır. Sadece belirli paketler için anlamlıdır.

**2.3.4 Sistem Tanıtımları (Konfigürasyon)******

Yükleme bittikten sonra yapılacak iş artık sistemimizin tanıtımlarını yapmaktır. İlk aşama sistemi açacak bir çekirdek belirlemektir. Bu konuda üç seçenek var:

Bootdisk Use the kernel from the installation bootdisk

Cdrom Use a kernel from the Slackware CD

Floppy Install a zimage or bzimage file from a DOS floppy

**Bootdisk:** Bu seçenekte kullandığınız çekirdek boot disketinden kopyalanacaktır.

**CD-ROOM:** Slackware CD-ROOM’unda bulunan önceden derlenmiş çekirdeklerden herhangi birisini seçebilirsiniz.

**Floppy:** Herhengi bir DOS disketinde yer alan çekirdeği yüklemenizi sağlar.

Daha sonra sisteminiz için bir boot disketi yaratmak isteyip istemediğinizi soracaktır. Ne olursa olsun, elinizin altında root ve boot disketleri bulundurmak zorundasınız. Bir sorun olduğunda sisteminizi açmak için bir boot disketi bulmanız gerekecektir.

Ardından setup size modem, mouse, CD-ROM, bulunduğunuz zaman dilimini soracak ve liloconfig yazılımı çalışacaktır. ;LILO, Linux Loader (Linux yükleyicisi) kelimelerinden meydana gelir. LILO Linuz yüklemek için kullanılan çok pratik ve etkili bir yazılımdır. Bilgisayar açılır açılmaz, boot eden ilk sabit diskin üzerinde (boot partition) kendini yazar, bilgisyar açılır açılmaz, birden fazla işletim sistemi için seçenek sunulur. Konfigürasyon sırasında LILO kendisinin nereye yazılacağını sorar, bu seçenekler arasında

The Master Boot Record of your first hard drive

The superblock of your root Linux partition

A formatted floppy disk

yer alır.

**1 numaralı seçenek, **birçok uygulamada kullanılacak olan seçenektir. MBR bir bilgisayar açarken ilk bakılacak yerdir.

**2 numaralı seçenek**, MBR’yi kullanmamaktır. Bunun sebebi, MBR üzerinde bir başka işletim sisteminin benzer bir yazılımın bulunması olabilir. (örneğin OS/2 Bootmanager).

**3 numaralı seçenek,** LILO kendisini bir diskete yükleyecektir. Bu disketten açıldığı zaman menü ortaya çıkacaktır.

Daha sonra boot işlemi sırasında çekirdeğe gönderilecek ekstra parametreler belirtilebilir. Birçok sistem için bu parametre gereksizdir. Bu parametre boot diski ile açıldığı zaman sorulan parametrenin aynısıdır. Sonraki seçenek LOLO’nun yükleme sırasındaki davranışını belirler. LILO konfigürasyonu sırasında birden fazla boot edilebilecek sabit disk bölümü tanımlanabilir. Shift tuşuna basıldığı zaman LILO mevcut bölümler için bir liste çıkaracaktır. LILO için tanımlı dört davranış vardır:

None, don’t wait at all – boot straight into the first OS

5 seconds

30 seconds

Present a prompt and wait until a choice is made without timing out

**1 numaralı seçenek,** hiç beklenmeden doğrudan listede belirtilen ilk işletim sistemini yükleyecektir. Sadece Linux bulunan bilgisayarlar için kullanılan seçenel budur.

**2 ve 3 numaralı seçenek,** sırasıyla 5 ve 30 saniye beklerler, eğer bu süre içerisinde Shift tuşuna basılmazsa ilk sırada yer alan işletim sistemi yüklenir.

**4 numaralı seçenek,** bir işletim sistemi seçilene kadar bekler.

Daha sonra sırasıyla yüklenmesini tercih ettiğiniz disk bölümlerini tanıtabilirsiniz. LILO her bölüm için sizden ayıredici bir kelime isteyecektir. LILO yükleme anında sizden komut beklerken bu kelimeye göre işletim sistemini yükleyecektir.

**2.4 Makineyi Açmak******

Linux yükleme işlemi sona erdi. Sıra makinenizi Linux çalışacak şekilde çalışmasını sağlamaktır. Bunun için temel olarak iki değişik yöntem mevcuttur.

**LILO:** En çok kullanılan en pratik açılış şeklidir. Burada bilgisayar açıldığı zaman isteğe göre bir süre bekler ve bu esnada shift, tab veya control tuşuna basılırsa birden fazla işletim sistemi ile çalıştırma seçeneği sunar.

**LOADLIN: **DOS altında çalışan bir yazılımdır. DOS altında çalışırken Linux Yüklemenize yarar. Eğer kurulum aşamasında LOADLIN paketini (A serisi disketler içinde ) seçmişseniz bu paket /root dizini altında LOADLIN.ZIP ismi ile kaydedilmiş olacaktır. Yapmanız gereken bu yazılımı ve mevcut çekirdeğinizi (/vmlinux) DOS kısmını aktarmaktır. (son yıllarda pek kullanılmaktadır.)

Bütün bu adımlardan sonra artık elinizde çalışmaya hazır bir linux makine vardır. Makineyi kapatıp tekrar açın . ekranda çekirdek mesajları geçtikten sonra:

Login:

Belirecektir. Buraya root yazın ve sisteme girin. İlk deneme için

\# shutdown –rf now

yazabilirsiniz. Linux bir makine çalıştığı sürece hafıza içerisinde birçok tampon beelek açar. Mümkün olduğu kadar makineyi kapama tuşuna basarak kapatmayın. Shutdown komutu işletim sisteminin tampon belleklerde tuttuğu bilgileri güncellemesini sağlayacaktır. –r paremetresi sitemin reboot etmesini sağlayacaktır. Bilgisayarı kapatmak için

\# shutdown –hf now

komutu kullanabilirsiniz. Burada yer aln h paremetresi sistemin “halt” edeceğini (tamamen kilitleme) ve bir daha açılmayacağını belirtir.

Sistemde çalışmaya başlamak üzere ilk iş olarak kendinize çalışmak amacıyla bir kullanıcı tanımlayın. Sistemde başka kullanıcı olacaksa, onlar için de hesap açacaksınız. Kullanıcı hesabı açmak için

\# adduser

komutu kullanılır. adduser (veya useadd) komutu, kullanıcı ismi, isim ve soyad, GID (grup kimliği), UID (kullanıcı kimliği) gibi birtakım sorular sorulacaktır. Bu komut hakkında detaylı bilgiyi Sistem Yönetimi bölümü altında bulabilirsiniz. root kullanıcısı sistem üzerinde sınırsız yetkiye sahip olduğundan sistem dosyalarını kazara değiştirmenize veya silmenize sebep olabilir.

Şimdi yeni hesabınızla sisteme girebilirsiniz. ALT F1’den ALT F6’ya kadar olan tuşlarla birden çok ekranda (sanal akranlar) aynı anda çalışabilirsiniz.

Bu noktadan sonra bazı uygulamaların ayarlamalarını yapmanız gerekecek.

Açılış esnasında makinanızın ismi /etc/rc.d/rc.M dosyasında belirlenir. Bu dosyayı uygun şekilde değiştirerek makinanızın ismini de yeniden tanımlayabilirsiniz. Makinenizin ilk ismi darkstar olacaktır. Eğer TCP/IP ağ üzerinde çalışıyorsanız, /etc/HOSTNAME dosyasının içeriğini değiştirerek veya hostname komutu kullanılarak makine ismi de değiştirilebilir.

**2.4.1 Başlangıçta**

Önceki bölümde sisteme girmek için şifresi olmayan “root” kullanıcıyı kullanmıştık. Bu kullanıcı sistemde en fazla yetkiye sahip kullanıcı olup sistem görevlisi (sorumlusu) adını alır. Eğer root dışında bir kullanıcı hesabı tanımlanmışsa onu kullanın. Şifre yazıldıktan sonra komut istemcisine, yani kısaca kabuk dediğimiz programa gelir. Şifre yazılırken, başkalarının görmemesi için ekrana basılmaz, imleç sabit kalır.

Kullanıcı isimleri veya şifrelerde büyük ve küçük harfler arasında fark vardır. Root, root, RooT farklı kullanıcıları işaret eder. Sisteme ilk girişte aşağıdaki gibi bir satırla karşılaşacaksınız.

Welcome to Linux 1.2.13.

Linux login: root

Pasword:

Last login: Thu Feb 13 12:46:35 on tty 1

Linux 1.2.13.

You have mail.

Linux: ~#

Genellikle komut istemcisinin sonundaki karekter, root kullanıcısı için #, diğer kullanıcılar için $ olur. Bu karekterlerden önce de makine ismi yeralır. MS-DOS’ta olduğu gibi burada UNIX komutlarını girebileceğiniz kabuk (shell) üzerindesiniz.

Şifreyi değiştirmek için kullanılan komut *passwd’*dir. Bir kullanıcı sadece kendi şifresini değiştirirken root!a herkesin şifresini değiştirme yetkisi verilmiştir. Herhangi bir sistemde hesap şifrenizi unutursanız, bunu sadece root değiştirebilir. root iken passwd yazın ve enter tuşuna basın.

linux:~# passwd

Changing password for root

Enter new password:

Re-type new password:

Password changed.

linux:~#

şifrenizi iyi saklayın. root şifresini ele geçiren birisi sistemde istediği değişiklikleri yapabilir. Şifre seçimi için *Linux İşletim Sisteminde Güvenlik* konusuna bakın.

Linux komutları hakkında bilgi almak için *man* komutu kullanılır. Eğer kurulum aşamasında man dosyalarının kopyalanması sorusuna olumlu yanıt verilmişse bunlar /usr/man dizini altında bulunur. Örneğin passwd komutu hakkında detaylı bilgi almak için

$ man passwd

yazılır. Tüm man dosyaları /usr/man dizini altında 8 ayrı dizinde saklanır (man1...man8). bazı komutların man dosyaları birden fazla dizin altında bulanabilir. Bir dosya komut hakkında bilgi verirken diğeri sistem programcılarına yönelik olabilir. Örnek olarak mount komutu, hem 2 hem de 8 numaralı man dosyalarıyla birlikte arşivlenmiştir. C programlayıcısı, mount komutuna ulaşmak için

$ man 2 mount

yazarken, normal kullanıcı,

$ man 8 mount

yazmalıdır. Bunun yanında başlığında belirli bir anahtar sözcüğü içeren tüm man dosyalarını araştırmak için apropos komutu kullanılır.her komut, bir veya birden çok parametre alabilir. Örnek olarak,

find .-name “\*.txt” –print

komutu, bulunduğunuz yerden itibaren tüm dosyaları araştıracak ve bunların arasından sonu .txt ile bitenleri ekrana basacaktır. Parametreler genel olarak “-“ işaretleri ve bu işaretten gelen parametre ismi ile belirtilirler.

**2.4.2 Sorun Çıktığında******

Çıkabilecek en önemli sorun bilgisayarın açılmamasıdır. Bunun birçok sebebi olabilir. Açılış esnasında ilk olarak LILO çalışır. Çekirdek yüklenir. Hizmet veren yazılımlar teker teker çalışmaya başlar.

Her aşmada birçok satırda durumunu belirtecektir. Çalışan yazılımlar veya yazılım parçalarının her biri birbirinden bağımsız olduğu için açılış sırasında geldiğiniz nokta çok önemlidir. LILO çalışmadığında veya çekirdek yüklenirken takılırsa boot disketi ile rahatlıkla sistemi açabilirsiniz. Örnek olarak Linux yüklü disk bölümünüzün /dev/hda2 olduğunu varsayalım. Boot disketi parametre isteğinde

mount root = /dev/hda2

yazmanız yeterli olacaktır. Bu durumda boot disketinde yer alan çekirdek ile belirttiğiniz bölümde yer alan Linux hiyerarşisi açılacaktır. Çalışan bu sisteminiz içerisinde artık hatanın kaynağı daha rahat bulabilirsiniz.

Çekirdeğin yükleme esnasında takılması büyük ölçüde çekirdeğin donanımı doğru belirleyememesinden çıkar. Örneğin ethernet kartınızı yanlış tanımış olabilir. Bunu çözmenin temel yöntemi çekirdek içerisinde kullanmayacağınız donanımlara ilişkin destekleri kaldırmak veya çekirdeğe yardımcı olabilecek açılış parametreleri vermek.

Çalışan sisteminizde bir arıza meydana gelip de makine aniden çalışmamaya başlarsa en son yaptığınız değişiklikleri gözden geçirin.

Sisteminizin çalışması her zaman Linux’dan kaynaklanmayabilir, donanım ile ilgili sorunlar da yaşayabilirsiniz. Rastgele davranışlar, durup dururken çakılmalar, panik mesajları altında, bozuk sabit diskler, normalden yüksek frekansta çalıştırılan işlemciler ve sistem saatine göre yavaş kaçan veya bozuk RAM’ler yatabilir.

---
*Kaynak: `LINUX KURULUMU VE BASLANGIÇ/LINUX KURULUMU VE BAŞLANGICI.doc` — Murat Arslan — 2004*
