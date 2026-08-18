# Kim Korkar UNIX Ten

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 94

Şimdi sıkı durun: UNIX kullanıcılarının, disklerin ne şekilde ayrılmış

Şimdi sıkı durun: UNIX kullanıcılarının, disklerin ne şekilde ayrılmış

Şimdi sıkı durun: UNIX kullanıcılarının, disklerin ne şekilde ayrılmış

Şimdi sıkı durun: UNIX kullanıcılarının, disklerin ne şekilde ayrılmış

olduğundan; hatta bilgisayarda kaç disk sürücü bulunduğundan haberi olması

olduğundan; hatta bilgisayarda kaç disk sürücü bulunduğundan haberi olması

olduğundan; hatta bilgisayarda kaç disk sürücü bulunduğundan haberi olması

olduğundan; hatta bilgisayarda kaç disk sürücü bulunduğundan haberi olması

bile gerekmemektedir. UNIX’de tüm diskler ve disk parçaları (

bile gerekmemektedir. UNIX’de tüm diskler ve disk parçaları (partition partition partition partition’lar), ’lar), ’lar), ’lar),

bile gerekmemektedir. UNIX’de tüm diskler ve disk parçaları (

bile gerekmemektedir. UNIX’de tüm diskler ve disk parçaları (

root ( / ) dizinin altında birer alt dizin olarak yer alacaktır.

root ( / ) dizinin altında birer alt dizin olarak yer alacaktır.

root ( / ) dizinin altında birer alt dizin olarak yer alacaktır.

root ( / ) dizinin altında birer alt dizin olarak yer alacaktır.

Şematik olarak göstermek gerekirse :

Her disk ve disk parçası üzerinde diğerlerinden bağımsız bir dosya dosya dosya dosya sistemi sistemi sistemi sistemi (file file file file system system system system) bulunmalıdır. Bu sistemler, diskler (ya da disk parçaları) üzerinde, formatlama işleminden sonra mkfs mkfs mkfs mkfs komutu ile yaratılmaktadır. (Merak etmeyin; bu işin yapılmasından siz değil; sistem yöneticiniz sorumludur.)

Genellikle, boot boot boot boot diskinizin (bilgisayar açıldığında UNIX işletim sisteminin yüklendiği disk) ilk parçası size root ( / / / / ) dizini olarak görünür. Diğer disk ve disk parçalarıysa bu dizinin altındaki alt dizinler olarak görünür. UNIX geleneğine göre boot boot boot boot diskleri an az 3 parçaya bölünür. İlk parça / / / /, ikinci parça /usr /usr /usr /usr, üçüncü parça ise /home /home /home /home dizini olarak isimlendirilir. Aslında pek yeri değil ama sanırım biraz daha ayrıntılı açıklama yararlı olacak.

/ / / / dizini, bilgisayarın açılabilmesi için gerekli olan dosyaların ve alt dizinlerin yer aldığı dizin; /usr /usr /usr /usr dizini, tüm kullanıcıların ortak olarak kullanacağı çeşitli derleyici ve servis programlarının yer aldığı dizin; /home /home /home /home diziniyse, adından da anlaşılacağı gibi kullanıcıların kendilerine özgü dosyalarını yerleştirecekleri home home home home dizinlerinin yer aldığı dizindir. Bu yerleştirme tarzı UNIX geleneğinin bir parçasıdır. Aynen uygulanması gerekmese de, genellikle tüm UNIX sistemlerinde diskler bu veya buna çok benzeyen bir şekilde düzenlenir. Bu düzenlemenin yararlarını daha ilerideki bölümlerde (özellikle sistem yöneticilerini ilgilendiren konulara gelince) anlatacağım.

Üzerinde bir dosya sistemi olan bir disk birimine veya parçasına, okuma veya yazma amacıyla ulaşabilmeniz için, o dosya yapısının, / / / / dosya yapınızda bir alt dizine mount mount mount mount edilmiş olması gerekmektedir. ( / / / / dizini, bilgisayarın açılması sırasında otomatik olarak mount mount mount mount edilmektedir. Eğer bu / / / / dizini, bilgisayarın açılması aşamasında mount mount mount mount edilemezse, o bilgisayar zaten açılamaz; bu durumda mutlaka teknik desteğe gereksiniminiz vardır. Diğer disk veya disk

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 95

parçalarının otomatik olarak mount mount mount mount edilmesi için gerekli işlemlerse, sistem yöneticiniz tarafından yapılmalıdır.

UNIX’deki dosya-dizin yapılarını ters duran bir ağaca benzetirsek, mount mount mount mount etme işlemini, bir ağacı, bir başka ağacın dallarından birine iliştirmek (monte etmek) gibi düşünebilirsiniz.

Şimdi isterseniz, kullandığınız bilgisayarda kaç disk ve/veya disk parçası olduğuna ve bunların hangi dizinlere mount mount mount mount edildiğine bir bakalım. Bu iş için lütfen terminalinizden şu komutu veriniz :

% mount mount mount mount

Tipik olarak şöyle bir liste almalısınız

% mount mount mount mount

/dev/sd0a on / rw 4.2 /dev/sd0g on /usr rw 4.2 /dev/sd0h on /home rw 4.2 % (Bu örnek, SUNOS 4.1 .3 UNIX i şletim sistemiyle çalı şan bir i ş istasyonundan alınmı ştır. Sizin kullandı ğ ınız bilgisayarda alacağ ınız liste bununla aynı olmayabilir).

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 96

Bu listeden, bilgisayarımızda sadece bir disk olduğunu (sadece /dev/sd0 /dev/sd0 /dev/sd0 /dev/sd0 serisi bulunduğundan anlaşılıyor) ve bu diskin en az üç parçaya ayrıldığını (parça isimleri a, g ve h) veya sadece üç parçasının o anda mount mount mount mount edilmiş durumda olduğunu ( a a a a parçası / / / / olarak, g g g g parçası /usr /usr /usr /usr dizini olarak ve nihayet h h h h parçası da /home /home /home /home dizini olarak) anlıyoruz. mount mount mount mount komutunun verdiği listedeki satırlarda yer alan rw rw rw rw harfleri, söz konusu disk parçalarının oku-yaz (read- read- read- read- write write write write) olarak kullanıma sunulduğunu (tabii ki, kullanıcıların yetkilerinin izin verdiği ölçüde) belirtmektedir. 4.2 sayısıysa, SUNOS 4.1.3 işletim sistemine özgü bir dosya sistemi sürüm kod numarasıdır (File System Version). mount mount mount mount komutu hakkında daha detaylı bilgiyi sistem yönetimi ile ilgili bölümlerde bulabilirsiniz. UNIX işletim sisteminin bir çok türevinde mount mount mount mount komutunu parametrelerle birlikte kullanabilmeniz için süper kullanıcı yetkilerine sahip olmanız gerekecektir; yani eğer süper kullanıcı (root root root root) değilseniz, zaten, mount mount mount mount komutunu yalnızca parametresiz olarak kullanmanıza izin verilecektir.

Bir UNIX bilgisayarı açıldığında, otomatik olarak mount mount mount mount edilmesi istenen diskler ve mount mount mount mount edilecekleri dizinler /etc/fstab /etc/fstab /etc/fstab /etc/fstab (BSD UNIX) veya /etc/vfstab /etc/vfstab /etc/vfstab /etc/vfstab (SVR4 UNIX) dosyalarında tanımlanır. Bu dosyalara sadece root root root root kullanıcının yazma yetkisi vardır; bu nedenle bu dosyalara korkmadan bakabilirsiniz. (more more more more /etc/fstab /etc/fstab /etc/fstab /etc/fstab gibi bir komut işe yarayabilir; ne dersiniz?)

Disket sürücüler ve CD-ROM sürücüleri de küçük birer disk sürücü olarak düşünülebilirler; bu nedenle kullanılabilmeleri için önce mount mount mount mount edilmeleri gerekir. Ancak; hem disketler, hem CD’ler, takılıp çıkarılabilir birimler olduklarından, bilgisayar açılırken otomatik olarak mount mount mount mount edilmezler. Normal olarak, bir disket veya CD’yi mount mount mount mount etmek için yeterli yetkiniz olmayacağından, bu tip birimlerin mount mount mount mount edilmesi konusunda sistem yöneticisinden yardım istemelisiniz. mount mount mount mount edilecek birimin, mount mount mount mount işleminden sonra hangi dizin altında görünmesi gerektiğine siz karar verebilir ve bu dizini siz yaratabilirsiniz. Bazı sistem yöneticileri, normal kullanıcılar tarafından çalıştırılabilen ve disket/CD mount mount mount mount işlemini yapan komutlar yaratırlar. Sizin çalıştığınız sistemde de böyle bir olanak olup olmadığını araştırınız. (Hayat Bilgisi kitabı gibi oldu, değil mi?)

İşi biten disket ve CD’ler unmount unmount unmount unmount edilmelidir; yani, bu birimlere takılı medyalar üzerindeki dosya sistemlerinin, root root root root dosya sistemiyle bağlantısı kesilmelidir. Aynı mount mount mount mount komutu gibi unmount unmount unmount unmount komutu için de yöneticinizin yardımına gereksiniminiz olabilir..

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 97

Haaaaa. Bu arada....

Haaaaa. Bu arada....

Haaaaa. Bu arada....

Haaaaa. Bu arada.... Sistem yöneticinizle iyi geçinin. Zaman zaman kendisinin ne kadar inanılmaz yeteneklerle donanmış olduğunu; bu kadar çok şeyi bilebildiğine göre dehşetli zeki olduğunu kendisine hatırlatmayı ihmal etmeyin. Aslında bu özelliklerini kendisi çok iyi biliyordur; ama gene de hatırlatılmasından hoşlanacaktır. Arada bir ona hediyeler alın; özellikle sizin için geç saatlere kadar çalışacaksa yemek zamanında onun için bir pizza ve büyük kola getirmeyi sakın ihmal etmeyin. Yalnız dikkatli olun; UNIX guruları, içinde yeşil malzeme olan pizza yemezler (UNIX geleneği)!

Süreçler Süreçler Süreçler Süreçler (Processes) UNIX işletim sisteminin çok kullanıcılı çok kullanıcılı ve çok işli çok kullanıcılı çok kullanıcılı çok işli bir işletim sistemi olduğunu çok işli çok işli şimdiye kadar bir kaç kez vurgulamıştım. Burada bir daha açıklamak gerekirse; UNIX işletim sisteminin denetimindeki bir bilgisayar hem aynı anda birden fazla kullanıcıya hizmet edebilir, hem de her kullanıcının aynı anda birden fazla işi yapmasına olanak sağlar. UNIX, kendi işlerini de bir sürü programı aynı anda çalıştırarak yapar. Örneğin, kullanılmayan terminallerin açılıp açılmadığını kontrol eden getty getty getty getty (bazı UNIX’lerde init init init init) programları, kullanıcıların birbirlerine gönderdikleri mesajları gözleyen ve gelen-giden mesajları uygun posta kutularına yönlendiren mail server mail server mail server mail server programı, bilgisayar ağı üzerinden gelen istekleri değerlendiren inetd inetd inetd inetd programı, belirli aralıklarla disklere yapılan kayıt işlemlerinin fiziksel olarak disklere kaydedilmesini (flushing disk buffers) sağlayan update update update update programı gibi... (Tipik bir UNIX bilgisayarında, kullanıcı programları dışında 30-40 sistem programı sürekli çalışıyor durumdadır.)

Bir UNIX bilgisayarında, belirli bir anda, merkezi işlem birimini (ya da birimlerini) ve belleği paylaşarak, birlikte çalışan programlara genel anlamda PROCESS PROCESS PROCESS PROCESS (süreç süreç süreç süreç) adı verilir. Süreçlerin Merkezi İşlem Birimi (MİB) zamanını paylaşmaları UNIX tarafından koordine edilir (İşletim Sistemlerine ilişkin İngilizce terminolojide : Process Scheduling işlevi). MİB paylaşımına ilişkin önemli bir terim de ‘zaman dilimi’ ‘zaman dilimi’ ‘zaman dilimi’ ‘zaman dilimi’ (time slice) kavramıdır. Her süreç, MİB’ni belirli ve kısa bir süre için (tipik olarak 10 - 100 milisaniye) sürekli olarak kullanabilir. Zaman dilimini dolduran süreçler beklemeye alınıp, MİB sırada bekleyen bir başka sürece tahsis edilir. Bu şekilde tüm süreçler aynı anda çalışıyormuş gibi bir etki elde edilir. Bu süreçlerin birden fazla kullanıcıya ait olmaları durumunda da, MİB kullanıcılar arasında paylaştırılmış olur. UNIX’in çok kullanıcılı olma özelliğinin altında yatan temel mekanizma budur

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 98

Herhangi bir anda, bilgisayarda çalışan süreçlerin neler olduğunu görmek isterseniz kullanacağınız komut

% ps -axl % ps -axl % ps -axl % ps -axl % ps -efl % ps -efl % ps -efl % ps -efl Berkeley UNIX için process status

SVR4 UNIX içinprocess status olacaktır. Aslında, bu komutun gerek BSD (Berkeley), gerekse SVR4 UNIX için daha bir çok parametresi olabilmektedir. Bu parametreleri merak eden kullanıcılar, man man man man komutu yardımıyla kullandıkları UNIX’in ps ps ps ps komutunun detaylarını öğrenebilirler.

Komutu parametresiz kullanırsanız, yanlızca kendinize ait süreçlerin bir listesini alırsınız. (Alacağınız bu liste BSD veya SVR4 UNIX’ler için biraz farklı olacaktır, fakat içerdikleri bilgi açısından eşdeğer sayılabilirler; bu nedenle sadece BSD UNIX’den örnekler vereceğim).

% ps ps ps ps

PID TT STAT TIME COMMAND

1210 co IW 0:01 sunview 1234 p0 S 0:43 shelltool 1226 p0 R 2:46 shelltool 1456 co R 0:04 ps 1605 co S 0:01 -bin/csh (csh) . . .

. . .

% Bu listedeki önemli bilgiler şunlardır:

PID TT STAT TIME (Process ID) UNIX’de, her sürecin birer tanıtım numarası vardır. Aynı numaraya sahip iki süreç olamaz.

(Teletype : Çok eskilerden kalan bir alışkanlık) Sürecin hangi terminalden başlatıldığı (genellikle co co co co : console, ttya ttya ttya ttya : a isimli seri arabirim, p0 p0 p0 p0 bilgisayar ağı üzerinden bağlanmış bir ekran). TT bilgisi kullandığınız donanımın özelliklerine göre değişebilir.

(Status) Sürecin bulunduğu duruma ilişkin bir kod.

R: Runnable : Çalışabilir durumda, sırasını bekliyor S: Sleeping : Uyuyor Z: Zombie : Bu süreç ile ilgili tüm diğer süreçler bitmiş veya ölmüş; bununda bitmiş olması gerekirdi ama bir nedenle ölememiş ölememiş. ps ps ps ps ölememiş ölememiş listesinde hala görünüyor olması zararsızdır.

Sürecin ne kadar zamandır çalıştığını gösterir COMMAND Süreci başlatan komut satırı

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 99

Süreçler hakkında daha detaylı bilgi isterseniz :

% ps -l % ps -l % ps -l % ps -l (process status -long list)

Sistemdeki tüm süreçler hakkında bilgi isterseniz :

% ps -ax % ps -ax % ps -ax % ps -ax (process status -all, extended)

% ps -ef % ps -ef % ps -ef % ps -ef

Sistemdeki tüm süreçler hakkında detaylı bilgi isterseniz :

% ps -axl % ps -axl % ps -axl % ps -axl (process status -all, extended, long)

% ps -efl % ps -efl % ps -efl % ps -efl

ps ps ps ps komutu, sistem yöneticileri için (sysad sysad sysad sysad, sysadmin sysadmin sysadmin sysadmin : system administrator) için çok önemlidir. Sistemde neler olup bittiğini, kullanıcıların ne gibi programlar kullanmakta olduklarını, sisteme kullanıcıların nerelerden eriştiğini, hep bu komut yardımı ile gözlerler. Ayrıca, sistemin çalışmasında bir gariplik olduğu zaman hemen bu komutla bilgisayarda çalışmakta olan süreçlerin bir listesini alırlar. ps ps ps ps komutu, zaman zaman normal kullanıcılar için de çok önemli olur. İşte size hemen bir senaryo...

Süreç Öldürme Süreç Öldürme Süreç Öldürme Süreç Öldürme (Killing Processes) Diyelim ki başlattığınız bir iş kontrolden çıktı ve istediğiniz ya da beklediğiniz gibi davranmıyor. Doğal olarak bu işi hemen kesmek istiyorsunuz. İlk denemeniz gereken Ctrl-C tuşu. Olmazsa Ctrl-D tuşu... (Fazladan basacağınız Ctrl-D logout logout logout logout edilmenize neden olabilir.) Gene olmadı diyelim.

BİLGİSAYARI ELEKTRİK ANAHTARINDAN KAPATMAYI VEYA RESET

BİLGİSAYARI ELEKTRİK ANAHTARINDAN KAPATMAYI VEYA RESET

BİLGİSAYARI ELEKTRİK ANAHTARINDAN KAPATMAYI VEYA RESET

BİLGİSAYARI ELEKTRİK ANAHTARINDAN KAPATMAYI VEYA RESET

DÜÐMES DÜÐMES DÜÐMES DÜÐMESİNE BASMAYI AKLINIZDAN DAHİ GEÇİRMEMELİSİNİZ!

İNE BASMAYI AKLINIZDAN DAHİ GEÇİRMEMELİSİNİZ!

İNE BASMAYI AKLINIZDAN DAHİ GEÇİRMEMELİSİNİZ!

İNE BASMAYI AKLINIZDAN DAHİ GEÇİRMEMELİSİNİZ!

Böyle bir durumda, eğer yapabiliyorsanız, ekranınızdaki başka bir pencereden veya bir başka kullanıcı terminalinden :

- Uygun bir ps ps ps ps komutuyla (ps ps ps ps veya ps -axl ps -axl ps -axl ps -axl veya ps -efl ps -efl ps -efl ps -efl) çalışmakta olan süreçlerin bir listesini alın.
- Bu listeye bakarak, sorun çıkaran sürecin numarasını öğrenin ve

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 100

% kill nnn % kill nnn % kill nnn % kill nnn (process kill)

(Burada nnn nnn nnn nnn, öldürülmek istenen sürecin numarasıdır).

- Eğer sorun yaratan süreci bu komutla öldüremezseniz

% kill -9 nnn % kill -9 nnn % kill -9 nnn % kill -9 nnn

komutunu deneyiniz. (-9 seçeneği ‘koşulsuz öldürme’ isteğinizi belirtir.)

% ps % ps % ps % ps

PID TT STAT TIME COMMAND

1234 p0 S 0:43 shelltool 1266 p0 R 2:46 problemli prog problemli prog problemli prog problemli prog 1456 co R 0:04 ps 1605 co S 0:01 -bin/csh (csh)

% kill 1266 % kill 1266 % kill 1266 % kill 1266 olmazsa

% kill -9 1266 % kill -9 1266 % kill -9 1266 % kill -9 1266

Süreci hala öldüremiyorsanız, kabuk programınızı öldürmeyi deneyiniz.

Hala direniyorsa sistemin USULÜNE UYGUN OLARAK USULÜNE UYGUN OLARAK USULÜNE UYGUN OLARAK USULÜNE UYGUN OLARAK kapatılmasını sağlayınız. Eğer root root root root yetkilerine sahip olabiliyorsanız, bu işi kendiniz de yapabilirsiniz; ancak sistemde başka kullanıcılar olabileceğini unutmayıp, bu kullanıcılara bir mesaj gönderip (write write write write ve wall wall wall wall komutları), onlara makul bir süre tanıyıp; ancak ondan sonra shutdown shutdown shutdown shutdown komutunu kullanarak sistemi kapatınız. Sistemleri kapatma yöntemlerini daha sonraki bölümlerde anlatacağım.

Link Kavramı ve ln Komutu

Link Kavramı ve ln Komutu

Link Kavramı ve ln Komutu

Link Kavramı ve ln Komutu

bazı

bazı

bazı

Şimdi biraz mistik bir konudan söz edeceğim. UNIX işletim sistemi altında bazı

dosyalar aslında bulundukları yerde olmayabilirler.

dosyalar aslında bulundukları yerde olmayabilirler. Evet, yanlış okumadınız!

dosyalar aslında bulundukları yerde olmayabilirler.

dosyalar aslında bulundukları yerde olmayabilirler.

Diskin üzerinde yer alan bazı dosyalar aslında orada olmayabilir; hatta bir dosyanın sistemde tek bir kopyası olmasına rağmen, bu dosya birden fazla dizinde; üstelik farklı isimlerle yer alabilir. Kavraması ve kullanması zor bir kavram fakat bir kez mecbur kalıp da kullandığınızda hoşunuza gideceğine emin olabilirsiniz.

Sanırım en iyisi bir örnekle anlatmak :

Farzedin ki bir UNIX sisteminin yöneticisisiniz. Sizden, bilgisayara matlab matlab matlab matlab isimli yeni bir uygulama programı yüklemenizi istediler.

Ancak, uygulama programının bir gereği olarak, program paketine ilişkin dosyaların /usr/local /usr/local /usr/local /usr/local dizininin altında açılacak bir dizinde yer alması gerekiyor. Eh! Olabilir. Ancak, bir sorun var! /usr /usr /usr /usr diskinde, yeni programa ilişkin dosyalar için yeterli boş yer yok; ve silebileceğiniz gereksiz dosyalar da yok!

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 101

Mistik ln ln ln ln kavramını kullanarak bu işi UNIX’in şanına yaraşır bir yöntemle çözebilirsiniz. Disklerin birinde; örneğin /home /home /home /home dizininin bulunduğu disk bölümünde (partition), yeni yükleyeceğiniz program için bir dizin yaratınız :

\# mkdir /home/matlab # mkdir /home/matlab # mkdir /home/matlab # mkdir /home/matlab

Sonra, bu dizini, /usr/local /usr/local /usr/local /usr/local altında yer alıyormuş gibi gösterebilmek için

\# ln -s /home/matlab /usr/ # ln -s /home/matlab /usr/ # ln -s /home/matlab /usr/ # ln -s /home/matlab /usr/local/matlab local/matlab local/matlab local/matlab

komutunu veriniz.

Böylece, gerçekte /home /home /home /home altında yer alan matlab matlab matlab matlab dizini, aynı zamanda /usr/local /usr/local /usr/local /usr/local altında da varmış gibi olacaktır. Bu dizini kullanırken isterseniz /home/matlab /home/matlab /home/matlab /home/matlab; isterseniz /usr/local/matlab /usr/local/matlab /usr/local/matlab /usr/local/matlab dizin adreslerini kullanabilirsiniz. Bir başka deyişle, dosyalarının /usr/local altında bulunmasını isteyen matlab yazılımını kandırmış olursunuz. link link link link kavramının çok işe yarayabileceği, bir öncekine benzeyen bir senaryo daha

mhsb1995

mhsb1995

anlatabilirim. Diyelim ki elinizde mhsb1995 mhsb1995 isimli bir dosya var ve muhasebe departmanının kullandığı muhasebe programı bu dosyayı mutlaka bu isimde görmek istiyor. Öte yandan yeni satın aldığınız bir mali analiz programı, aynı muhasebe verilerini acct95 acct95 acct95 acct95 adıyla görmek istiyor.

mhsb1995

mhsb1995

Söz konusu dosyanın adı mhsb1995 mhsb1995 olduğu zaman muhasebe departmanının sorunu yok ama siz mali analiz programını çalıştıramıyorsunuz. Analiz çalışmaları için dosyanın adını değiştirseniz, siz çalışabiliyorsunuz ama bu sefer muhasebe departmanındaki program kullanılamıyor. Dosyanın adını

mhsb1995

mhsb1995

mhsb1995

mhsb1995 olarak tutup, kendi analiz çalışmalarınız için acct95 acct95 acct95 acct95 adlı bir kopyasını çıkardığınızda ve siz bu kopya üzerinde çalıştığınızda problem kısmen çözülüyor ama çok kullanıcılı ortamda siz analizler üzerinde çalışırken öte taraftan muhasebe personeli yeni kayıtlar girip sizin analizlerinizin eskimiş kayıtlar üzerinde yapılmasına neden oluyorlar. İşte böyle bir durumda link link link link kullanımı sizi kurtaracaktır.

\# ln ./mhsb1995 ./acct95 # ln ./mhsb1995 ./acct95 # ln ./mhsb1995 ./acct95 # ln ./mhsb1995 ./acct95

Bu komutla mhsb1995

mhsb1995

mhsb1995

mhsb1995 dosyasını acct95 acct95 acct95 acct95 isimli bir dosyaya bağladığınızda

mhsb1995

mhsb1995

(aslında sadece tek bir asıl kopya var; o da mhsb1995 mhsb1995. acct95 acct95 acct95 acct95 isimli bir dosya

mhsb1995

mhsb1995

mhsb1995

aslında yok sadece diğer dosyanın bir başka adı. ) Bu sayede mhsb1995 dosyasında yapılan her değişiklik acct95 acct95 acct95 acct95 diye tanınan dosyada da aynen gözlenebilecektir. İşin bir başka yaralı tarafı da; acct95 acct95 acct95 acct95 isimli dosyanın diskte hiç yer kaplamayacak olmasıdır.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 102

Bu örnekler arasında, dikkatinizi çekmiş olduğunu umduğum bir fark var. İlk örnekte (matlab), ln ln ln ln komutunda -s -s -s -s diye bir parametre kullandım; oysa ikinci muhasebe örneğinde kullanmadım!

- Eğer, ln ln ln ln komutuyla birbirlerine bağlanacak olan dosya sistemi elemenları birer dizinse; -s -s -s -s parametresini kullanmak zorundasınız.
- Eğer, ln ln ln ln komutuyla birbirlerine bağlanacak olan dosya sistemi elemanları birer dosyaysa ve farklı disk parçalarında (bir başka deyişle; farklı dosya sistemleri altında) yer alıyorlarsa, gene -s -s -s -s parametresini kullanmak zorundasınız.
- ln ln ln ln komutuyla, bir dizini ve bir dosyayı birbirlerine bağlayamazsınız.

Bağlanacak olan elemanların ikisi de dizin; ya da ikiside dosya

olmalıdır.

Aynı dosya sisteminde yer alan ve birbirine bağlı olan dosyalardan birini silmeniz diğerini etkilemez. Asıl dosyayı silseniz bile, UNIX, bağlantıyı farkedip dosyayı diskten gerçekten silmeyecektir. UNIX, her dosya için bağlantıları sayar ve her silme işleminde bağlantı sayısını bir azaltır. Gerçek silme işi bu bağlantı sayısı sıfırlanınca yapılır.

Farklı dosya sistemlerinde yer alan bağlantılar için, bu bağlantı sayma işine güvenmeyiniz. Farklı dosya sisteminde bağlantısı olan bir dosyayı silerseniz başınız derde girer. Asıl dosya silinir ve diğer sistemde, gerçekte var olmayan bir dosyayı gösteren bir bağlantınız kalır.

Bir dosyanın gerçekten var olan bir dosya mı, yoksa sadece bir bağlantı mı (link link link link) olduğunu anlamak için ls ls ls ls komutunu -l -l -l -l seçeneği ile kullanmanız gerekir. İçinde bağlantılı dosyalar bulunan bir dizinde ls -l ls -l ls -l ls -l komutunu vererek, alacağınız listede bağlantılı dosyaları ve hangi dosyaya bağlantılı olduklarını açıkça görebilirsiniz.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 103

/home/ayfer % cd / cd / cd / cd / / % ls -l ls -l ls -l ls -l total 3166

lrwxrwxrwx 1 root 7 Jan 12 12:09 bin -> /usr/bin

-r--r--r-- 1 root 110912 Jan 12 12:11 boot

drwxr-sr-x 2 bin 7680 Jan 12 12:23 dev

drwxr-sr-x 7 bin 1536 Jan 15 08:45 etc

drwxr-sr-x 4 root 512 Feb 1 11:56 export

drwxr-xr-x 5 root 512 Mar 23 09:03 home

-rwxr-xr-x 1 root 239783 Feb 09 13:34 kadb

lrwxrwxrwx 1 root 7 Mar 01 18:23 lib -> /usr/lib

drwxr-xr-x 2 root 8192 Jun 15 23:09 lost+found

drwxr-sr-x 2 bin 512 Mar 01 20:09 mnt

drwxr-sr-x 2 bin 512 Mar 09 08:59 sbin

lrwxrwxrwx 1 root 13 Jan 24 07:45 sys -> /usr/kvm/sys

drwxrwsrwt 2 bin 512 Feb 24 09:56 tmp

drwxr-xr-x 20 root 512 Nov 23 16:08 usr

drwxr-xr-x 11 root 512 Nov 23 16:11 var

-rwxr-xr-x 1 root 1101191 Jan 11 09:35 vmunix

/ % Bu örnek listeye göre, aslında /bin /bin /bin /bin diye bir dizin bulunmamakta, bu isimde bir bağlantının /usr/bin /usr/bin /usr/bin /usr/bin dizinine yapılmış olduğu anlaşılmaktadır.

Dikkat ederseniz, ls -l ls -l ls -l ls -l komutunun verdiği listede, gerçek bir dosya (dizin) değil de, bağlantı olan dosyalara (dizinlere) ait satırların başında bir l l l l harfi bulunmaktadır.

İpin ucunu kaçırmayacağınıza eminseniz, bağlantılara bağlantı yapabilirsiniz.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 104

Önemli UNIX Komutları Önemli UNIX Komutları Önemli UNIX Komutları Önemli UNIX Komutları Günümüzün tipik UNIX bilgisayarlarında, GigaByte düzeyinde diskler bulunmaktadır. Bu kadar büyük disklerde de doğal olarak çok sayıda dizin ve binlerce dosya yer almaktadır. Zaman zaman adının bir kısmını hatırlayabildiğiniz; bulunduğu diziniyse bir türlü hatırlayamadığınız dosyalar olacaktır. Tek tek bütün dizinlere girip ls ls ls ls komutuyla bu dosya ya da dosyaları aramak pek akıllıca bir yöntem değildir. Böyle bir durumda kullanacağınız komut find find find find dır. find baslama-dizini kriter\[ler\] \[-exec komut ";"\] find baslama-dizini kriter\[ler\] \[-exec komut ";"\] find baslama-dizini kriter\[ler\] \[-exec komut ";"\] find baslama-dizini kriter\[ler\] \[-exec komut ";"\] find find find find komutuyla yapabileceğiniz aramalarda tek kriter dosya adı değildir. Bu komutla a) erişim yetkileri belirli bir kalıpta olan, b) belirli özelliklere sahip, c) belirli bir kullanıcıya ait, d) belirli bir boydan büyük ya da küçük, e) belirli bir tarihten veya saatten bu yana değişmemiş, erişilmemiş dosyaları veya dizinleri bulabilirsiniz.

Üstelik verdiğiniz arama kriterlerine uyan dosyalar üzerinde uygulanacak UNIX komutlarını da find find find find komutuna parametre olarak verebilirsiniz.

başlama-dizini

başlama-dizini Arama işlemi, find find find find komutunun bu ilk

başlama-dizini

başlama-dizini

parametresinde belirtilen dizinden başlar ve varsa bu dizinin alt dizinleri de arama ağacına dahil edilir.

Eğer arama işleminin, bilgisayarınıza bağlı ve mount mount mount mount edilmiş tüm disklerinde yapılmasını istiyorsanız, bu ilk parametre olarak / / / / sembolünü kullanınız.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 105

Bilgisayarınızın CD-ROM sürücüsü varsa ve bu sürücüye bir CD takılıysa ve bu CD mount mount mount mount edilmiş durumdaysa ve arama, / / / / dizininin hiyerarşisi boyunca yapılırsa, CD-ROM sürücüsünü de kapsayacaktır. CD’lerin kapasitelerinin büyüklüğü ve erişim hızlarının düşüklüğünden dolayı bu arama uzun sürecektir. Aynı mantıkla, bilgisayar ağı üzerinden başka bilgisayarların diskleri de sizin dosya sisteminize mount mount mount mount edilmiş durumdaysa, o diskler de arama ağacına girecektir. Zaman kaybına yol açmamak için, gerekmedikçe aramayı / / / / dizininden başlatmamanızı öneririm. kriter\[ler\] kriter\[ler\] kriter\[ler\] kriter\[ler\] Aranan dosya ve dosyaların ortak özelliklerini tanımlayan kriterlerdir Bir kaç örnek vermek gerekirse :

-name isim -name isim -name isim -name isim adı "isim" olan dosyalar (farklı dizinlerde aynı isme sahip dosyalar olabilir) -name "abc\*" -name "abc\*" -name "abc\*" -name "abc\*" -name "a\*data" -name "a\*data" -name "a\*data" -name "a\*data" adı "abc" ile başlayan dosyalar adı "a" ile başlayan ve adının sonunda "data" olan dosyalar -name "\[a-k\]95" -name "\[a-k\]95" -name "\[a-k\]95" -name "\[a-k\]95" adı a95, b95, ..., j95 veya k95 olan

dosyalar

Dikkatinizi çektiyse, -name -name -name -name kriteri kullanıldığında, dosya adını verirken, dosya adını tam olarak yazıyorsak tırnak (" " " ") kullanmıyoruz; oysa \* \* \* \* karakterini içeren bir kalıp kullanıyorsak (wildcard wildcard wildcard wildcard) bu kalıbı tırnak (" " " ") içinde yazıyoruz.

Bunun nedeni şu :

Bir komut verdiğinizde, bu komut önce kabuk programınız tarafından irdelenir. Bu irdeleme sırasında rastlanan \* \* \* \* karakterleri dosya adı kalıpları olarak kabul edilip, bu kalıba uyan dosya isimleriyle değiştirilmeye çalışılır. Oysa, kalıplara uyan dosya isimlerinin kabuk programı tarafından değil, find find find find programı tarafından bulunması gerekmektedir. Kabuk programlarının irdeleme sırasında karşılaşacakları \* \* \* \* karakterlerine dokunmamaları için, kalıp tanımları tırnak içine alınır.

-user ayfer -user ayfer -user ayfer -user ayfer sahibinin adı ayfer ayfer ayfer ayfer olan dosyalar -group yonetim -group yonetim -group yonetim -group yonetim sahibi yonetim yonetim yonetim yonetim grubuna dahil olan

dosyalar

-perm 755 -perm 755 -perm 755 -perm 755 erişim yetki düzeyi 755 755 755 755 olan dosyalar

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 106

-newer dosya1 -newer dosya1 -newer dosya1 -newer dosya1 dosya1 dosya1 isimli dosyadan daha sonraki bir

dosya1

dosya1

saat ya da tarihte değişikliğe uğramış

olan dosyalar

-size 10 -size 10 -size 10 -size 10 10 blok olan 10 blok 10 blok diskte kapladığı alan 10 blok dosyalar (1 blok = 512 Byte) -size +100 -size +100 -size +100 -size +100 diskte kapladığı alan 100 bloktan büyük

100 bloktan büyük

100 bloktan büyük

100 bloktan büyük

olan dosyalar (51 KByte’dan büyük dosyalar) -size -45 -size -45 -size -45 -size -45 diskte kapladığı alan 45 bloktan küçük 45 bloktan küçük 45 bloktan küçük 45 bloktan küçük

olan dosyalar

-ctime 3 -ctime 3 -ctime 3 -ctime 3 Tam 3 gün önce değişikliğe uğramış olan

dosyalar

-ctime +8 -ctime +8 -ctime +8 -ctime +8 8 günden daha uzun bir süre önce

değişikliğe uğramış olan dosyalar

-ctime -8 -ctime -8 -ctime -8 -ctime -8 8 günden daha kısa bir süre önce

değişikliğe uğramış olan dosyalar

-mtime 3 -mtime 3 -mtime 3 -mtime 3 Tam 3 gün önce değişikliğe uğramış

olan dosyalar

-mtime +8 -mtime +8 -mtime +8 -mtime +8 8 günden daha uzun bir süre önce

değişikliğe uğramış olan dosyalar

-mtime -8 -mtime -8 -mtime -8 -mtime -8 8 günden daha kısa bir süre önce

değişikliğe uğramış olan dosyalar

-atime -3 -atime -3 -atime -3 -atime -3 3 günden daha kısa bir süre içinde bir şekilde erişilmiş olan dosyalar -ctime -ctime -ctime -ctime ve -mtime -mtime -mtime -mtime parametrelerinin her ikisi de dosyanın değişikliğe uğramasıyla ilgili süreleri kontrol eder; ancak aralarında küçük bir fark vardır. -mtime -mtime -mtime -mtime, dosyanın içeriğinde bir değişiklik yapılıp yapılmadığına; -ctime -ctime -ctime -ctime ise dosyanın içeriği yanısıra özelliklerinin de değişip değişmediğini kontrol eder. Örneğin, sahibi değişen bir dosya -mtime -mtime -mtime -mtime tarafından farkedilmezken -ctime -ctime -ctime -ctime tarafından dikkate alınır.

-atime 3 -atime 3 -atime 3 -atime 3 Tam 3 gün önce bir şekilde erişilmiş

dosyalar

-atime +8 -atime +8 -atime +8 -atime +8 -atime -8 -atime -8 -atime -8 -atime -8 -type f -type f -type f -type f 8 günden daha uzun bir süre önce erişilmiş olan dosyalar 8 günden daha kısa bir süre önce erişilmiş olan dosyalar Basit birer ‘dosya’ olan dosyalar

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 107

-type d -type d -type d -type d Dizinler Bu arama kriterlerini bir arada kullanabilirsiniz; örneğin, sahibi hakman hakman hakman hakman adlı kullanıcı olan ve son 40 gündür kullanılmamış dosyaları bulmak isterseniz, kullanmanız gereken find find find find komutu

% find /home -user hakman -atime +40 -print find /home -user hakman -atime +40 -print find /home -user hakman -atime +40 -print find /home -user hakman -atime +40 -print

olmalıdır.

Komutun sonundaki -print -print -print -print parametresini kullanmayı unutursanız, find find find find programının verdiğiniz kriterlere uygun dosya bulup bulmadığını öğrenemezsiniz. Bulunan dosyaların isimlerinin listelenmesi için bu parametreyi kullanmak şarttır. İlk bakışta anlamsızmış gibi geldiğini biliyorum. Eğer bulunan dosyaların adını görmek istemiyorsanız, find find find find komutunu neden kullanasınız ki? Bu sorunun yanıtı şöyle : find find find find komutunu bir kabuk programı içinde çalıştırıyorsanız ve sizin için verdiğiniz kriterlere uygun dosya bulunup bulunmadığını bilmek yetiyorsa (hangi dosyalar olduğunu görmeniz gerekmiyorsa) aramanın başarılı olup olmadığını belirten bir sistem değişkeninin değerine bakmanız yeterli olacaktır.(condition code veya completion code).

Şimdi, sık kullanılan find find find find formları için bir kaç örnek vereyim :

% find /home/ayfer -name onemli.dosya -print find /home/ayfer -name onemli.dosya -print find /home/ayfer -name onemli.dosya -print find /home/ayfer -name onemli.dosya -print

/home/ayfer dizininden başlayarak bu dizinde ve alt dizinlerinde onemli.dosya onemli.dosya onemli.dosya onemli.dosya isimli dosyaları arar ve bulduklarının adını standart çıktıya (ekrana) listeler.

% find / -name core -exec /bin/rm {} ";" find / -name core -exec /bin/rm {} ";" find / -name core -exec /bin/rm {} ";" find / -name core -exec /bin/rm {} ";"

/ / / / dizininden başlayarak tüm disklerde core core core core isimli dosyaları arar ve bulduklarını siler. find find find find komutunu -exec -exec -exec -exec parametresiyle birlikte kullanırken sondaki ";" ";" ";" ";" parametresini UNUTMAMALISINIZ. Bu ";" ";" ";" ";" karakter dizisinin gerekliliği tamamen find find find find programının yazılışından kaynaklanmaktadır.

Bu komut, sistem yönetiminden sorumlu olanların oldukça sık kullanacakları bir komuttur. UNIX, çeşitli programların kullanımı sırasında bir sistem problemi olduğunda "core dumped core dumped core dumped core dumped" mesajıyla birlikte, belleği core core core core isimli bir dosyaya kopyalar. Bu core core core core dosyaları, problemin nedenini bulmasına yardımcı olmak amacıyla yaratılır. Bu dosyaları irdeleyerek problemin nedenini bulmak pek kolay

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 108

olmadığından, genellikle bu dosyalar içeriklerine bakılmaksızın silinebilirler. Zaman içinde biriken core core core core dosyaları diskte oldukça önemli yer harcadıklarından, rastladıkça bu dosyaları silmenizi öneririm.

% find /home -user hasan -exec /bin/rm {} ";" find /home -user hasan -exec /bin/rm {} ";" find /home -user hasan -exec /bin/rm {} ";" find /home -user hasan -exec /bin/rm {} ";"

/home /home /home /home dizininden başlayarak hasan hasan hasan hasan isimli kullanıcıya ait dosyaları arar ve bulduklarını siler.

Sisteme erişim hakları iptal edilen kullanıcılara ait dosyaları tek harekette silmek için kullanılabilir.

% find /home -name "\*.tmp" -exec /bin/rm {} ";" find /home -name "\*.tmp" -exec /bin/rm {} ";" find /home -name "\*.tmp" -exec /bin/rm {} ";" find /home -name "\*.tmp" -exec /bin/rm {} ";"

/home /home /home /home dizininden başlayarak adı \*.tmp \*.tmp \*.tmp \*.tmp kalıbına uyan dosyaları arar ve bulduklarını siler.

% find /home -type d -name \[tmp, temp\] -print find /home -type d -name \[tmp, temp\] -print find /home -type d -name \[tmp, temp\] -print find /home -type d -name \[tmp, temp\] -print

/home /home /home /home dizininden başlayarak adı tmp tmp tmp tmp veya temp temp temp temp olan dizinleri bulur ve listeler. find find find find komutuyla birlikte kullanılan kriterleri çeşitli mantık operatörleriyle birleştirebilirsiniz. Bunlar -a : -a : -a : -a : "ve ve ve ve" -o : -o : -o : -o : "veya veya veya veya" \\! : \\! : \\! : \\! :"de il de il de il de il" operatörleridir.

Örnekler :

% find /home -name "\*.tmp" -a -size +100 -print find /home -name "\*.tmp" -a -size +100 -print find /home -name "\*.tmp" -a -size +100 -print find /home -name "\*.tmp" -a -size +100 -print

adı \*.tmp \*.tmp \*.tmp \*.tmp kalıbına uyan ve ve ve ve büyüklüğü 100 bloktan fazla olan dosyaları bulur. (1 blok = 512 byte)

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 109

% find /home/ayfer \\! -user ayfer -print find /home/ayfer \\! -user ayfer -print find /home/ayfer \\! -user ayfer -print find /home/ayfer \\! -user ayfer -print

ayfer ayfer ayfer ayfer isimli kullanıcının home dizininde yer alan ama ayfer ayfer ayfer ayfer’e ait olmayan olmayan olmayan olmayan dosyaları bulur.

Bu örnekteki "değil değil" anlamında kullanılan \\! \\! \\! \\! operatöründeki \\ \\ \\ \\ işareti değil değil ardından gelen ! ! ! ! işaretinin özel bir anlamı olduğunu ve kabuk programı (sh veya csh) tarafından yorumlanmaya çalışılmaması gerektiğini belirtmek için kullanılmaktadır.

Hatırlarsanız, daha önceki bölümlerden birinde, UNIX işletim sisteminde kendi komutlarınızı yaratabileceğinizden bahsetmiştim. Sanırım bu uygulamaya bir örnek vermek için uygun bir noktadayız. find find find find komutu oldukça yetenekli ve seçenekli bir komut; ama bunun karşılığında da yazması oldukça uzun. Dosyaları sadece adlarıyla arayan daha kısa bir UNIX komutu yaratmaya ne dersiniz?

Önce vi vi vi vi editörünü kullanarak home dizininizde ff ff ff ff isimli ve içinde aşağıdaki satırlar bulunan bir dosya yaratınız. (% vi ~/ff) (% vi ~/ff) (% vi ~/ff) (% vi ~/ff) #!/bin/sh #!/bin/sh #!/bin/sh #!/bin/sh case $# in case $# in case $# in case $# in 1) find . -name "$1" -print;; 1) find . -name "$1" -print;; 1) find . -name "$1" -print;; 1) find . -name "$1" -print;; 2) find "$1" -name "$2" -print;; 2) find "$1" -name "$2" -print;; 2) find "$1" -name "$2" -print;; 2) find "$1" -name "$2" -print;; \*) echo "Error... Usage : ff \[path\] name" \*) echo "Error... Usage : ff \[path\] name" \*) echo "Error... Usage : ff \[path\] name" \*) echo "Error... Usage : ff \[path\] name" echo " ff \[path\] \\"name\*\\"" echo " ff \[path\] \\"name\*\\"" echo " ff \[path\] \\"name\*\\"" echo " ff \[path\] \\"name\*\\"" echo " ff \[path\] \\"\*name\\"" echo " ff \[path\] \\"\*name\\"" echo " ff \[path\] \\"\*name\\"" echo " ff \[path\] \\"\*name\\"" esac esac esac esac ff program dosyasını oluşturan bu satırların anlamları üzerinde şimdilik durmayınız.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 110

Daha sonra,

% chmod a+x ~/ff chmod a+x ~/ff chmod a+x ~/ff chmod a+x ~/ff

komutuyla, bu dosyanın erişim yetki kalıbını, tüm kullanıcılar tarafından çalıştırılabilen bir komut dosyası olacak şekilde değiştiriniz.

Bu komut, aksi belirtilmedikçe, aramalara bulunduğunuz dizinden başlar. Eğer tek parametreyle çalıştırılırsa, bu parametreyi bir dosya adı olarak kabul edip, bulunduğunuz dizinde ve alt dizinlerinde bu dosyayı arayacaktır. Eğer iki parametreyle başlatılırsa, birinci parametre aramanın başlayacağı dizin, ikinci parametreyse aranacak dosyanın adı kabul edilecektir. Eğer dosya adı içinde \* \* \* \* kullanmak istiyorsanız \*’ \*’ \*’ \*’li ifadeyi çift tırnak içine almayı unutmayınız.

Örnekler :

% ff aranan.veri.dosyasi ff aranan.veri.dosyasi ff aranan.veri.dosyasi ff aranan.veri.dosyasi

% ff /home/ugur prog.c ff /home/ugur prog.c ff /home/ugur prog.c ff /home/ugur prog.c

% ff ~ file001.dat ff ~ file001.dat ff ~ file001.dat ff ~ file001.dat

% ff "\*dat" ff "\*dat" ff "\*dat" ff "\*dat"

% ff /cdrom "openwin\*" ff /cdrom "openwin\*" ff /cdrom "openwin\*" ff /cdrom "openwin\*"

Yeni yarattığınız ff ff ff ff komutunu verdiğinizde, komut programının bulunamadığına ilişkin bir mesaj alıyorsanız, path path path path değişkeninizde home home home home dizininiz olmayabilir. Çalıştırmak istediğiniz programı oluşturan dosyanın çalışma dizininizde bulunması yetmez. Bir programın çalıştırılabilmesi için i) ya yeri tam olarak komutta belirtilmelidir (~/ff ~/ff ~/ff ~/ff gibi) ii) ya da program dosyasının bulunduğu dizin, path path path path değişkeninde tanımlanmış olmalıdır. path path path path ile ilgili bir sorun olmamasına rağman ‘komut bulunamadı’ ( ff : Command not found.) mesajını alıyorsanız; chmod chmod chmod chmod komutuyla, ff ff ff ff programının “çalıştırılabilir” (executable) bir dosya olduğunu belirtmeyi unutmuş olabilirsiniz.

“çalıştırılabilir”

“çalıştırılabilir”

“çalıştırılabilir”

Bir olasılık ta; ff ff ff ff komut dosyasını girerken bir hata yapmış olabileceğinizdir.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 111

Arama - Tarama Arama - Tarama Arama - Tarama Arama - Tarama find find find find komutuyla; dosyaları, adları ve sahipleri gibi özelliklerine göre taramayı öğrendiniz. Peki.... Dosyaların içinde kayıtlı verilere göre aramaları nasıl yapcaksınız? Örneğin, içerdiği kayıtlar arasında ayfer ayfer ayfer ayfer sözcüğü geçen dosyaları bulmak istediğinizde hangi komutu kullanmalısınız?

% grep \[-ilnc\] patern dosya(lar) % grep \[-ilnc\] patern dosya(lar) % grep \[-ilnc\] patern dosya(lar) % grep \[-ilnc\] patern dosya(lar) general purpose regular

expression search program Hemen bir kaç örnek...

İçinde yaklaşık 20,000 satır bulunan /etc/termcap /etc/termcap /etc/termcap /etc/termcap dosyasında (terminal karakteristikleri tanıtım dosyası) “wyse50 marka terminallerle ilgili bir tanım var mı?” diye merak ettiğinizde

% grep wyse50 /etc/termcap grep wyse50 /etc/termcap grep wyse50 /etc/termcap grep wyse50 /etc/termcap

komutunu kullanabilirsiniz. Eğer bu dosyanın içinde wyse50 wyse50 wyse50 wyse50 sözcüğü geçiyorsa, bu satırlar standart çıktı birimine (ekrana) listelenecektir. wyse50 wyse50 wyse50 wyse50 sözcüğünün büyük harflerle yazılmış olma olasılığı varsa

% grep -i wyse50 /etc/termcap grep -i wyse50 /etc/termcap grep -i wyse50 /etc/termcap grep -i wyse50 /etc/termcap

formunu denemelisiniz. ( -i -i -i -i : ignore case; büyük-küçük harf ayrımı yapılmasın) Bulunan satırların satır numaralarını da görmek isterseniz

% grep -ni wyse50 /etc/termcap grep -ni wyse50 /etc/termcap grep -ni wyse50 /etc/termcap grep -ni wyse50 /etc/termcap

formunu kullanabilirsiniz. ( -n : numbered) Bulunduğunuz dizinde, adı mektup mektup mektup mektup ile başlayan dosyalar arasında bir veya birkaç tanesinin içinde ayfer ayfer ayfer ayfer sözcüğünün bulunduğunu biliyorsunuz ama hangileri olduğunu hatırlayamıyorsunuz! İşte çözüm :

% grep ayfer mektup1 mektup2 mektup3 ... grep ayfer mektup1 mektup2 mektup3 ... grep ayfer mektup1 mektup2 mektup3 ... grep ayfer mektup1 mektup2 mektup3 ...

veya

% grep ayfer mektup\* grep ayfer mektup\* grep ayfer mektup\* grep ayfer mektup\*

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 112

grep grep grep grep komutu, arama işini birden fazla dosya üzerinde yaptığı zaman, kullanıcıya kolaylık olması için; bulunan satırları ekrana listelerken, her satırın başına, satırın bulunduğu dosyanın adını ekler.

Eğer, bulunan satırlar için yalnızca dosya adlarını görmek istiyorsanız,

% grep -l ayfer mektup\* grep -l ayfer mektup\* grep -l ayfer mektup\* grep -l ayfer mektup\*

formunu kullanmalısınız.

Adı mektup mektup mektup mektup’la başlayan dosyalarda ayfer ayfer ayfer ayfer sözcüğünün kaç defa geçtiğini öğrenmek isterseniz

% grep -c ayfer mektup\* grep -c ayfer mektup\* grep -c ayfer mektup\* grep -c ayfer mektup\*

komutunu kullanılabilirsiniz. grep grep grep grep komutu ( ve onun biraz geliştirilmişleri olan egrep egrep egrep egrep ve fgrep fgrep fgrep fgrep), UNIX işletim sisteminin en çok kullanılan komutlarındandır. Bu komutun daha yararlı kullanımlarına ilişkin örneklere devam etmeden önce çok önemli bir UNIX kavramından daha söz etmek istiyorum: PIPE PIPE PIPE PIPE. pipe pipe pipe pipe kavramını anlatırken kullanacağım örnekler arasında grep grep grep grep komutuyla ilgili olanları dikkatle incelerseniz yukarıda verilen örneklerden daha yararlı kullanımlarını öğrenmiş olacaksınız.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 113

UNIX kullanıcılarının günlük hayatta karşılaşacağı tipik bir sorun ve bu sorunun çözümünden söz etmek istiyorum : Sorun (ya da soru) şu : home home home home dizinimin altında yer alan bir takım dizinlerde bir takım dosyaların içinde “piper” sözcüğü geçiyor. Bu dosyaların hangileri olduğunu grep piper \* grep piper \* grep piper \* grep piper \* komutuyla bulabileceğimi biliyorum; ama home dizinimin altında o kadar çok alt-dizin var ki! Her birine teker teker geçip aynı grep komutunu tekrarlamak istemiyorum. Bu arama işini hem home dizinimde, hem de onun alt dizinlerinde tek komutla yapabilir miyim?

Elbette yapabilirsiniz! UNIX’de, sadece standart UNIX komutları kullanarak, hiç program yazmadan, veri tabanı sistemi bile geliştirebilirsiniz!

Bu küçük problemin çözümü şu iki komut : cd /home/ayfer cd /home/ayfer cd /home/ayfer cd /home/ayfer grep piper grep piper grep piper grep piper \`find . -print\` \`find . -print\` \`find . -print\` \`find . -print\` tırnak işaretlerine dikkat! ASCII kodu desimal 96 olan tırnak işaretidir. Burada ' veya “ kullanamazsınız.

Komutun çalışma sistemi aslında basit. Kabuk programınız, komut satırında \` işaretleri arasında bir başka komut görünce önce onu çalıştıracaktır (find . - find . - find . - find . - print print print print komutu). Bu programın standart çıktıya gönderdiği listeyi de grep grep grep grep komutunun sonuna ekleyecek; grep grep grep grep komutunu ondan sonra çalıştıracaktır. Bir başka deyişle, grep grep grep grep komutuna, içinde piper piper piper piper sözcüğü aranacak dosyaların listesini klavyeden yazmak yerine, bu işi find find find find komutuna yaptırmış olacaksınız. Zarif, değil mi?

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 114

UNIX PIPE Kavramı UNIX PIPE Kavramı UNIX PIPE Kavramı UNIX PIPE Kavramı pipe pipe pipe pipe (boru) kavramı, daha önce açıklamış olduğum ‘Giriş/Çıkış Yönlendirme’ kavramıyla kolayca karıştırılan, bu yüzden dikkatle ele alınması gerek bir kavramdır. Kısaca bir tekrarlamak gerekirse; ‘çıkış yönlendirme ( çıkış yönlendirme ( > ) > ) > ) > )’, çalıştırılan çıkış yönlendirme ( çıkış yönlendirme ( bir programın, standart çıktı birimine yazacağı satırların bir dosyaya yönlendirme işlemidir. Aynı mantıkla, verilerini standart giriş biriminden okuyan programlar için ‘giriş yönlendirme ( giriş yönlendirme ( giriş yönlendirme ( < ) < ) < ) < )’; verilerin bir dosyadan okunmasını sağlayan giriş yönlendirme ( işlemdir.

Piping işlemiyse, gene bir çeşit yönlendirmedir; ancak şu farkla ki, bir programın standart çıktısı, bir başka programa standart girdi olarak yönlendirilir.

Pipe kurmak için, aynı komut satırında en az iki program birden başlatmalı ve bu iki programa ilişkin komutların arasına karakterini yerleştirmeniz gerekir.

Şimdi grep grep grep grep komutu ve pipe pipe pipe pipe kavramının birlikte kullanımına bir kaç örnek vereyim :

% grep ayfer mektup\* | more grep ayfer mektup\* | more grep ayfer mektup\* | more grep ayfer mektup\* | more

Bu komut, daha doğrusu komut ikilisinin anlamı şu : grep grep grep grep ve more more more more programlarını aynı anda başlat.

Adı ‘mektup mektup mektup mektup’la başlayan dosyalar içinde ayfer ayfer ayfer ayfer sözcüğünü ara, bulduğun satırları more more more more programına gönder, more more more more programı bu satırları alsın ve kendi görev tanımı doğrultusunda işlesin. (Yani sayfa sayfa listelesin).

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 115

% ps -ax | grep in.named ps -ax | grep in.named ps -ax | grep in.named ps -ax | grep in.named

ps ps ps ps ve grep grep grep grep programlarını aynı anda başlat.. ps ps ps ps programının oldukça uzun olabilecek çıktısını grep grep grep grep programına girdi olarak gönder. grep grep grep grep kendisine gönderilen satırlar arasında, içinde in.named n.named n.named n.named sözcüğü geçenleri bulsun ve sadece ilgilendiğimiz bu satırları listelesin. Böylece grep grep grep grep programı bir filtre gibi kullanılmış olacaktır. sıkı sıkı Şimdide sıkı sıkı bir pipe örneği...

  tuşunun solundaki tırnak işareti...

% echo Sistemde \`who | wc -l\` kullan c  var echo Sistemde \`who | wc -l\` kullan c  var echo Sistemde \`who | wc -l\` kullan c  var echo Sistemde \`who | wc -l\` kullan c  var

Bu komut satırında bir kaç kademeli bir işlem istenmektedir.

İlk olarak who who who who programı çalıştırılacaktır. Aynı anda wc wc wc wc programı da çalıştırılacak ve who who who who programının çıktısı standart girişindeki satır, kelime ve karakterleri sayan wc wc wc wc (-l seçeneği yanlızca satırların sayılmasını sağlıyor) programına gönderilecektir. wc wc wc wc programının çıktısıysa (who who who who komutunun listelediği satırların sayısı) tırnaklar arasına yerleştirilerek elde edilen; örneğin üç kullanıcı Sistemde 3 kullanıcı var’ dizisi de echo echo echo echo Sistemde 3 kullanıcı var Sistemde 3 kullanıcı var varsa, ‘Sistemde 3 kullanıcı var programına girdi olarak transfer edilir. echo echo echo echo programıysa parametrelerini aynen ekrana gönderir. Bu örnekteki komutu, home home home home dizinizdeki .login .login .login .login veya .cshrc .cshrc .cshrc .cshrc dosyasına eklerseniz, sisteme her login login login login edişinizde, sistemde siz dahil, kaç kişinin çalıştığını öğrenmiş olursunuz.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 116

Yazı cı Kullanı mı

Yazı cı Kullanı mı

Yazı cı Kullanı mı

Yazı cı Kullanı mı

MS-DOS işletim sistemi ile çalışan kişisel bilgisayarlarda yazıcı kullanımı oldukça kolaydır. Bilgisayarı yalnızca siz kullandığınız için, diğer tüm kaynaklar gibi yazıcı da sadece sizin kullanımınıza tahsis edilmiş durumdadır.

Canınız istediği zaman programınıza ‘yaz’ komutunu verir ve yazıcının başına geçip, çıktılarınızın kağıda aktarılmasını beklersiniz.

UNIX dünyasında durum farklı... Kullanıcılar, bilgisayarın tüm kaynakları gibi yazıcısını da başkalarıyla paylaşmak zorundalar. Yazıcıya gönderilen her döküm, MS-DOS’da olduğu gibi anında basılmaya başlamayabilir; çünkü o anda yazıcı bir başka kullanıcının bir çıktısını döküyor olabilir. Kağıda bir kaç satır bir kullanıcıdan, bir kaç satır da başka kullanıcıdan döküm yapmak pek sağlıklı olmayacağı için, tüm çok kullanıcılı işletim sistemlerinde olduğu gibi, UNIX’te de; yazıcı dökümlerinin sıraya konmasını sağlayan SPOOLING SPOOLING SPOOLING SPOOLING (Shared (Shared (Shared (Shared Peripheral Operation Online) Peripheral Operation Online) Peripheral Operation Online) Peripheral Operation Online) işlemi uygulanmaktadır. UNIX’de, kullanıcı programlarından gelen ‘yazıcıya yazıcıya yolla’ yolla’ yolla’ yolla’ emirleri sanki yerine yazıcıya yazıcıya getirilmişcesine olumlu karşılanır; ancak yazıcıya gönderilmesi istenen bilgiler diskte önceden belirlenmiş bir alana kaydedilir (spool spool spool spool area). Zaman içinde kullanıcılardan gelen döküm istekleri UNIX spooler spooler spooler spooler programı tarafından sıraya konur ve yazıcı boş kaldığında, diskte saklanan dökümler kağıda aktarılmak üzere sırayla yazıcıya veya yazıcılara gönderilir.

Bir başka deyişle, uygulamanız, kağıda bir döküm almanızı gerektiriyorsa ve siz bu doğrultuda yazdırma komutu verdiyseniz; isteğiniz hemen yerine getirilemeyebilir (yazıcı meşgul olabilir veya hazır olmayabilir). Ancak, bu durum size yansıtılmaz ve kağıda dökülmesini istediğiniz her şey, spooler spooler spooler spooler tarafında diske kaydedilerek sıraya sokulur ve ilk fırsatta yazıcıya gönderilir.

UNIX altında çalışan bilgisayarlar genellikle büyükçe sistemler olduğundan, birden fazla yazıcıya sahip olabilirler. Özellikle bilgisayar ağlarında bu durumla daha da sık karşılaşılır. Bir döküm almak istediğinizde, yazıcı seçme şansınızın da olabileceğini unutmayınız.

BSD ve SVR4 UNIX türevlerinde yazıcı kullanma komutları oldukça farklı olduğundan, bu iki tip UNIX için ayrı ayrı bölümler hazırladım. Genel kültür açısından her iki bölümü de okumanızı öneririm.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 117

BSD UNIX’de Yazıcı Kullanımı

BSD UNIX’de Yazıcı Kullanımı

BSD UNIX’de Yazıcı Kullanımı

BSD UNIX’de Yazıcı Kullanımı

Herhangi bir dosyayı yazıcıya göndermek istediğinizde kullanabile-ceğiniz en basit komut formu şudur :

% lpr dosya\_adi % lpr dosya\_adi % lpr dosya\_adi % lpr dosya\_adi (line printer)

Bu komutu verdiğinizde, dosya\_adı dosya\_adı isimli dosya, adı lp lp lp lp olan yazıcının (veya

dosya\_adı

dosya\_adı

PRINTER PRINTER PRINTER PRINTER isimli kabuk değişkeninde belirtilmiş olan isme sahip yazıcının) sırasına sokulur. Sisteminizde adı lp lp lp lp olan bir yazıcı bulunmasını sağlamak, sistem yöneticisinin görevidir.

Eğer, dosyanızı, özel bir yazıcıya göndermeniz söz konusuysa kullanacağınız komut

% lpr -Pyaz % lpr -Pyaz % lpr -Pyaz % lpr -Pyazici\_adi dosya\_adi ici\_adi dosya\_adi ici\_adi dosya\_adi ici\_adi dosya\_adi

Bu komutta P P P P harfinin büyük P olduğuna ve yazıcı adının bu P P P P harfine bitişik olarak yazıldığına dikkatinizi çekerim. (Bazı UNIX’ler P P P P harfiyle yazıcı adı arasında boşluk kullanılmasına izin verir.)

% lpq \[-Pyazici\_adi\] % lpq \[-Pyazici\_adi\] % lpq \[-Pyazici\_adi\] % lpq \[-Pyazici\_adi\] (line printer queue)

Yazıcı için sıra bekleyen işler hakkında bilgi verir. Sıra bekleyen her dökümün bir tanıtma numarası vardır.

% lprm \[ nnn \[mmm ...\] \] % lprm \[ nnn \[mmm ...\] \] % lprm \[ nnn \[mmm ...\] \] % lprm \[ nnn \[mmm ...\] \] (line printer remove)

Sıra bekleyen dökümler arasında tanıtma numarası nnn nnn nnn nnn (ve mmm mmm mmm mmm vs) olan işleri iptal eder. nnn nnn nnn nnn verilmezse, komutu veren kullanıcıya ait olan ve o sırada dökülmekte olan ya da sıradaki ilk işi iptal edilir.

% lprm kullanici\_adi % lprm kullanici\_adi % lprm kullanici\_adi % lprm kullanici\_adi (line printer remove)

Sıra bekleyen işler arasında sahibi kullanici\_adi kullanici\_adi kullanici\_adi kullanici\_adi olan dökümleri iptal eder. nnn nnn nnn nnn (ve mmm mmm mmm mmm vs)

% lpstat \[-Pyazici\_adi\] % lpstat \[-Pyazici\_adi\] % lpstat \[-Pyazici\_adi\] % lpstat \[-Pyazici\_adi\] (line printer status)

Yazıcının durumunu gösterir. (Hazır olup olmadığını vs.)

% lpr -#n % lpr -#n % lpr -#n % lpr -#n -Plazer dosya\_adi -Plazer dosya\_adi -Plazer dosya\_adi -Plazer dosya\_adi

dosya\_adı isimli dosyanın, lazer lazer lazer lazer isimli yazıcıdan n n n n kopyasının basılmasını

dosya\_adı

dosya\_adı

dosya\_adı

sağlar.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 118

% lpr - % lpr - % lpr - % lpr -m m m m onemli onemli onemli onemli

onemli onemli onemli onemli isimli dosyanın, basılmak üzere lp lp lp lp isimli yazıcıya gönderilmesini ve basım tamamlandığında, komutu veren kullanıcıya bir mesaj (mail) gönderilmesini sağlar.

% lpr -r % lpr -r % lpr -r % lpr -r onemsiz onemsiz onemsiz onemsiz

onemsiz onemsiz onemsiz onemsiz isimli dosyanın, basılmak üzere lp lp lp lp isimli yazıcıya gönderilmesini ve dosyanın, ilgili yazıcının sırasına alınmasından hemen sonra diskten silinmesini

sağlar.

% lpr dosya1 dosya2 ... % lpr dosya1 dosya2 ... % lpr dosya1 dosya2 ... % lpr dosya1 dosya2 ...

Birden fazla dosyanın tek komutla yazıcı sırasına gönderilmesini sağlar.

% sort < sirasiz | lpr % sort < sirasiz | lpr % sort < sirasiz | lpr % sort < sirasiz | lpr

lpr lpr lpr lpr komutu ve pipe pipe pipe pipe kavramının birlikte kullanılışına bir örnek... Bu örnekte, sirasiz sirasiz sirasiz sirasiz isimli dosya sort sort sort sort programıyla sıraya dizilmekte ve sıralanmış hali doğrudan yazıcıya gönderilmektedir.

Örneklerini verdiğim çeşitli lpr lpr lpr lpr seçeneklerini birleştirebileceğinizi ayrıca belirtmeme sanırım gerek yok. Örneğin;

% lpr -rmPepson onemsiz % lpr -rmPepson onemsiz % lpr -rmPepson onemsiz % lpr -rmPepson onemsiz

Kullanıcısı olduğunuz bilgisayar sistemine bağlı olan yazıcıların özelliklerini ve isimlerini sistem yöneticisinden öğrenebilirsiniz.

SVR4 UNIX’de Yazıcı Kullanımı

SVR4 UNIX’de Yazıcı Kullanımı

SVR4 UNIX’de Yazıcı Kullanımı

SVR4 UNIX’de Yazıcı Kullanımı

Herhangi bir dosyayı yazıcıya göndermek istediğinizde kullanabileceğiniz en basit komut formu şudur :

% lp dosya\_adi % lp dosya\_adi % lp dosya\_adi % lp dosya\_adi (line printer)

Bu komutu verdiğinizde, dosya\_adı dosya\_adı isimli dosya, adı lp lp lp lp olan yazıcının (veya

dosya\_adı

dosya\_adı

PRINTER PRINTER PRINTER PRINTER isimli kabuk değişkeninde belirtilmiş olan isme sahip yazıcının) sırasına sokulur. Sisteminizde adı lp lp lp lp olan bir yazıcı bulunmasını sağlamak, sistem yöneticisinin görevidir.

Eğer, dosyanızı, özel bir yazıcıya göndermeniz söz konusuysa kullanacağınız komut

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 119

% lp -dyazici\_adi dosya\_adi % lp -dyazici\_adi dosya\_adi % lp -dyazici\_adi dosya\_adi % lp -dyazici\_adi dosya\_adi

Bu komutta d d d d harfinin küçük d olduğuna ve yazıcı adının bu d d d d harfine bitişik olarak yazıldığına dikkatinizi çekerim.

% lpstat \[-a\] % lpstat \[-a\] % lpstat \[-a\] % lpstat \[-a\] line printer status

Yazıcının durumunu gösterir. (Hazır olup olmadığını vs.) -a -a -a -a seçeneği tüm yazıcıların durumunu gösterir. Durum raporlarında, yazıcılar için sıra bekleyen işler ve tanıtım numaraları da listelenir.

% cancel nnn \[mmm ...\] % cancel nnn \[mmm ...\] % cancel nnn \[mmm ...\] % cancel nnn \[mmm ...\]

Sıra bekleyen dökümler arasında tanıtma numarası nnn nnn nnn nnn (ve mmm mmm mmm mmm vs) olan işleri iptal eder.

% cancel -u ugur % cancel -u ugur % cancel -u ugur % cancel -u ugur

Sıra bekleyen dökümler arasında ugur ugur ugur ugur isimli kullanıcıya ait olan döküm işlerini iptal eder.

% lp -nk -dlazer dosya\_adi % lp -nk -dlazer dosya\_adi % lp -nk -dlazer dosya\_adi % lp -nk -dlazer dosya\_adi

dosya\_adı isimli dosyanın, lazer lazer lazer lazer isimli yazıcıdan k k k k kopyasının basılmasını

dosya\_adı

dosya\_adı

dosya\_adı

sağlar.

% lp -m % lp -m % lp -m % lp -m onemli onemli onemli onemli

onemli onemli onemli onemli isimli dosyanın, basılmak üzere lp lp lp lp isimli yazıcıya gönderilmesini ve basım tamamlandığında, komutu veren kullanıcıya bir mesaj (mail) gönderilmesini sağlar.

% lp dosya1 dosya2 ... % lp dosya1 dosya2 ... % lp dosya1 dosya2 ... % lp dosya1 dosya2 ...

Birden fazla dosyanın tek komutla yazıcı sırasına gönderilmesini sağlar.

% sort < sirasiz | lp % sort < sirasiz | lp % sort < sirasiz | lp % sort < sirasiz | lp

lp lp lp lp komutu ve pipe pipe pipe pipe kavramının birlikte kullanılışına bir örnek... Bu örnekte, sirasiz sirasiz sirasiz sirasiz isimli dosya sort sort sort sort programıyla sıraya dizilmekte ve sıralanmış hali doğrudan yazıcıya gönderilmektedir.

Örneklerini verdiğim çeşitli lp lp lp lp seçeneklerini birleştirebileceğinizi ayrıca belirtmeme sanırım gerek yok. Örneğin;

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 120

% lp -mdepson onemsiz % lp -mdepson onemsiz % lp -mdepson onemsiz % lp -mdepson onemsiz

Kullanıcısı olduğunuz bilgisayar sistemine bağlı olan yazıcıların özelliklerini ve isimlerini sistem yöneticisinden öğrenebilirsiniz.

SVR4 UNIX’lerde yazıcı yönetimi ile ilgili olan bir kaç komut daha vardır. Bu komutların görev ve yetenekleri kitabın sınırlarını çok aştığı için; sadece meraklı kullanıcılar için bu komutların isimlerini verip geçeceğim. Bu komutlar hakkında daha fazla bilgi almak için man man man man komutunu kullanabilir veya UNIX dökumantas-yonuna başvurabilirsiniz. Yazıcı yönetimine ilişkin diğer SVR4 UNIX komutları : accept, lpadmin, disable, enable, accept, lpadmin, disable, enable, accept, lpadmin, disable, enable, accept, lpadmin, disable, enable, lpmove, pr, reject, lpsched lpmove, pr, reject, lpsched lpmove, pr, reject, lpsched lpmove, pr, reject, lpsched

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 121

Kabuklar - C Shell ve Shell Kabuklar - C Shell ve Shell Kabuklar - C Shell ve Shell Kabuklar - C Shell ve Shell

Komut Satırının Yorumlanması ve Parametreler

Komut Satırının Yorumlanması ve Parametreler

Komut Satırının Yorumlanması ve Parametreler

Komut Satırının Yorumlanması ve Parametreler

UNIX İşletim sistemi, kullanıcıların verdikleri komutları çözümlemek ve bu komutları yerine getirecek programları başlatmak için kabuk (shell) programlarını kullanır. Bir başka deyişle, kabuk programları, kullanıcılarla bilgisayar arasındaki yazılım arabirimidir. Aslında, bu tip komut yorumlayıcıları (command interpreter), tüm işletim sistemlerinde kullanılmaktadır; örneğin MS-DOS işletim sisteminde bu görevi COMMAND.COM üstlenmiş durumdadır.

UNIX işletim sisteminde, kullanıcıların birden fazla kabuk programı arasından seçim yapma ve beğendikleri komut yorumlayıcısını kullanma hakları vardır.

Hatta, aynı anda birden fazla kabuk programı bile kullanılabilirler. Daha fazla detaya girmeden, genel olarak bir kabuk programının ne işler yaptığını bir örnekle açıklamaya çalışacağım. Bu örneğimizle ilgili bir kaç tane de varsayımımız olacak; şöyleki :

- Kullanıcı C-Shell kabuk programını kullanıyor olsun,
- Kullanıcının adı ayfer ayfer ayfer ayfer ve komutu verdiği anda kendi çalışma
- dizini /home/ayfer /home/ayfer /home/ayfer /home/ayfer olsun, Başarılı bir login login login login’den sonra, UNIX, komut beklediğini, abc:/home/ayfer % \_ abc:/home/ayfer % \_ abc:/home/ayfer % \_ abc:/home/ayfer % \_ veya sadece % \_ % \_ % \_ % \_ hazır işaretiyle (prompt) belli edecektir. (Eğer C-shell yerine sh sh sh sh kabuk programı kullanılıyor olsaydı, % % % % işareti yerine $ $ $ $ işareti görünüyordü).

Kullanıcı klavyesinden; örneğin; cp eski-dosya yeni-dosy cp eski-dosya yeni-dosy cp eski-dosya yeni-dosy cp eski-dosya yeni-dosya a a a komutunu verdiğinde, kabuk programı, cp cp cp cp harflerini kullanıcının çalıştırmak istediği programın adı olarak; eski-dosya eski-dosya eski-dosya eski-dosya ve yeni-dosya yeni-dosya yeni-dosya yeni-dosya kelimeleriniyse bu cp cp cp cp programının iki parametresi olarak kabul edecektir. cp cp cp cp eski-dosya eski-dosya eski-dosya eski-dosya yeni-dosya yeni-dosya yeni-dosya yeni-dosya (Komut) (1. parametre) (2. parametre) Bir sonraki iş, kullanıcının çalıştırmak istediği bu cp cp cp cp programının saklandığı disk dosyasını bulmak olacaktır. Bu arama işinin temelinde, kullanıcımız için

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 122

tanımlanmış olan PATH PATH PATH PATH ve/veya path path path path kabuk değişkeninin o andaki değeri yatmaktadır. Bu değişkenlerin değerleri PATH = /bin:/usr/bin:/usr/local/bin:~ayfer/bin:. PATH = /bin:/usr/bin:/usr/local/bin:~ayfer/bin:. PATH = /bin:/usr/bin:/usr/local/bin:~ayfer/bin:. PATH = /bin:/usr/bin:/usr/local/bin:~ayfer/bin:.

veya

path= ( /bin /usr/bin /usr/local/bin ~ayfer/bin .) path= ( /bin /usr/bin /usr/local/bin ~ayfer/bin .) path= ( /bin /usr/bin /usr/local/bin ~ayfer/bin .) path= ( /bin /usr/bin /usr/local/bin ~ayfer/bin .) benzeri bir karakter dizisi olacaktır ve bu değerler, kullanıcının home home home home dizininde yer alan .cshrc .cshrc .cshrc .cshrc ve/veya .login .login .login .login dosyalarında tanımlanmış olmalıdır. Şimdilik, bu dosyaların, sizin için, sistem yönetici tarafından hazırlanmış olduğunu kabul edebilirsiniz. csh csh csh csh programı, “: : : :” işaretleriyle (ya da boşluk karakterleriyle) birbirlerinden ayrılmış olan dizinlerde; cp cp cp cp isimli bir dosya arayacaktır. Arama, dizin isimlerinin veriliş sırasına göre yapılacaktır. Örneğimize göre, csh csh csh csh programı, cp cp cp cp isimli dosyayı önce /bin /bin /bin /bin dizininde; orada bulamazsa /usr/bin /usr/bin /usr/bin /usr/bin dizininde; orada da bulamazsa /usr/local/bin /usr/local/bin /usr/local/bin /usr/local/bin; olmazsa ayfer ayfer ayfer ayfer adlı kullanıcının home home home home dizininin altındaki bin bin bin bin dizininde (~ayfer/bin ~ayfer/bin ~ayfer/bin ~ayfer/bin); o da olmazsa o andaki çalışma dizininde ( . . . . ) arayacaktır. Söz konusu dosyayı bu dizinlerden hiç birinde bulamazsa cp : Command not found. cp : Command not found. cp : Command not found. cp : Command not found. diye, komutu tanıyamadığına ilişkin bir hata mesajı vererek yeniden komut bekleme durumuna dönecektir.

Eğer, cp cp cp cp program dosyası, bu dizinlerden birinde bulunursa, bu dosyanın erişim yetkileri kontrol edilir; ayfer ayfer ayfer ayfer’in bu programı çalıştırmaya yetkisi varsa (execute yetkisi) cp cp cp cp programı kabuk tarafından belleğe yüklenir ve çalıştırılır.

Komut satırında verilen parametrelerse, gerekirse çözümlenip, cp cp cp cp programına aktarılır.

Artık kontrol, cp cp cp cp programına geçmiştir. Bu programın mantığına göre son parametre, kopyalamanın yapılacağı dosya ya da dizin adını, önceki parametrelerse buraya kopyalanacak dosyaların isimleri olmalıdır. Bir başka deyişle, cp cp cp cp komutunun en az iki parametresi bulunmalıdır. kabuk programı bu detayları bilemeyeceği için, bu tip mantık kontrolleri komut programı tarafından yapılmalıdır. Parametrelerin doğru sırada ve sayıda verilip verilmediğini her program kendisi kontrol eder ve gerekirse uygun hata veya uyarı mesajları üreterek, kullanıcıyı uyarır.

Şimdi ortalığı biraz karıştıralım....

Şimdi ortalığı biraz karıştıralım....

Şimdi ortalığı biraz karıştıralım....

Şimdi ortalığı biraz karıştıralım....

Kullanıcımız cp \* /disk2/home2/ayfer cp \* /disk2/home2/ayfer cp \* /disk2/home2/ayfer cp \* /disk2/home2/ayfer komutunu vermiş olsun. Bu komutla kullanıcının yapmak istediği iş, çalışma dizinindeki tüm dosyaları ( \* \* \* \* ), /disk2/home2/ayfer /disk2/home2/ayfer /disk2/home2/ayfer /disk2/home2/ayfer dizinine kopyalamak... Bu komutu gören csh csh csh csh, komut adı olan cp cp cp cp sözcüğünü bulduktan sonra, bu komutun parametrelerini bulup çıkarmaya çalışacaktır. Komut satırını tararken

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 123

(parsing) \* \* \* \* karakterine rastlayınca, csh csh csh csh, “tüm dosyalar” anlamına gelen \* \* \* \* yerine, çalışma dizininde yer alan dosyaların isimlerini yanyana gelecek şekilde yerleştirecektir.

Yani, komut satırı cp abc dosya1 dosya2 xyz x123 muhasebe.dat /disk2/home/ayfer cp abc dosya1 dosya2 xyz x123 muhasebe.dat /disk2/home/ayfer cp abc dosya1 dosya2 xyz x123 muhasebe.dat /disk2/home/ayfer cp abc dosya1 dosya2 xyz x123 muhasebe.dat /disk2/home/ayfer şekline dönüştürülecektir (çalışma dizininde sadece abc abc abc abc, dosya1 dosya1, dosya2 dosya2 dosya2 dosya2, xyz xyz xyz xyz,

dosya1

dosya1

x123

x123

x123

x123 ve muhasebe.dat muhasebe.dat muhasebe.dat muhasebe.dat dosyalarının yer aldığı varsayımıyla). Bu dönüşümü ekranda gözleyemezsiniz; ancak bu tip dönüşümlerin olduğunu bilmeniz ve komutları verirken bu dönüşümleri dikkate almanız çok önemlidir.

Bazı komutların doğru çalışması için, komut satırlarının, kabuk programları tarafından dönüştürülmeden komut programlarına aktarılması gerekmektedir.

Bu gerekliliği açıklayan en iyi örnek find find find find komutudur.

Hatırlarsanız, find find find find komutuna ilişkin verdiğim örneklerden biri, adı \*.tmp \*.tmp \*.tmp \*.tmp kalıbına uyan ve büyüklüğü 100 bloktan fazla (51200 byte’dan fazla) olan dosyaları bulup listelemeye yönelikti. find /home -name "\*.tmp" -a -size +100 -print find /home -name "\*.tmp" -a -size +100 -print find /home -name "\*.tmp" -a -size +100 -print find /home -name "\*.tmp" -a -size +100 -print Bu örnekte "\*.tmp" "\*.tmp" "\*.tmp" "\*.tmp" yazarken kullanılan " " " " işaretleri çok çok önemlidir çok çok önemlidir çok çok önemlidir çok çok önemlidir. Kabuk programı, tırnak içinde yer alan komut bölümlerini çözümlemeye çalışmayacaktır. Komut satırında tırnak içinde yer alan bölümler, hiç bir değişikliğe uğramadan, ilgili programa parametre olarak iletilecektir. Şimdi, yukarıdaki find find find find örneğindeki komutu tırnak işaretlerini kullanmadan yazdığımızı farzedelim.... hatalı hatalı hatalı hatalı find /home -name \*.tmp -a -size +100 -print find /home -name \*.tmp -a -size +100 -print find /home -name \*.tmp -a -size +100 -print find /home -name \*.tmp -a -size +100 -print Bu komutu gören kabuk programı, find find find find sözcüğünü program adı olarak değerlendirip, bu programın parametrelerini saptamak amacıyla satırı taramaya devam edecektir. /home /home /home /home birinci; -name -name -name -name ise ikinci parametre olarak çözümlenecektir. Buraya kadar sorun yok.... Ancak \*.tmp \*.tmp \*.tmp \*.tmp kalıbına rastlandığında, çalışma dizininde yer alan ve adı bu kalıba uyan dosyaların isimleri komut satırına üçüncü, dördüncü, beşinci vs parametre olarak yerleştirilecektir (tabii çalışma dizininde adı bu kalıba uyan dosyalar varsa).

Diyelimki, bu komutu verdiğimizde, çalışma dizinimizde şu dosyalar bulunmaktaydı : a a a a dosya1 dosya1 dosya1 dosya1 dosya2 dosya2 dosya2 dosya2 a.tmp a.tmp a.tmp a.tmp dosya1.tmp dosya1.tmp dosya1.tmp dosya1.tmp dosya3 dosya3 dosya3 dosya3 kabuk programı tarafından çözümlenen ve dönüştürülen komut satırı find /home -name a.tmp dosya1.tmp -a -size +100 -print find /home -name a.tmp dosya1.tmp -a -size +100 -print find /home -name a.tmp dosya1.tmp -a -size +100 -print find /home -name a.tmp dosya1.tmp -a -size +100 -print olacaktır.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 124

BU ŞEKİLDE ÇÖZÜMLENMİŞ KOMUT BİRKAÇ NEDENLE HATALIDIR.

BU ŞEKİLDE ÇÖZÜMLENMİŞ KOMUT BİRKAÇ NEDENLE HATALIDIR.

BU ŞEKİLDE ÇÖZÜMLENMİŞ KOMUT BİRKAÇ NEDENLE HATALIDIR.

BU ŞEKİLDE ÇÖZÜMLENMİŞ KOMUT BİRKAÇ NEDENLE HATALIDIR.

Birincisi; find find find find komutunun mantığına göre arama sadece adı a.tmp a.tmp a.tmp a.tmp olan dosyalar için yapılacaktır; oysa biz adı \*.tmp \*.tmp \*.tmp \*.tmp kalıbına uyan tüm dosyaları aramak istiyoruz.

İkincisi; dosya1.tmp parametresi tanımlayıcı işaretsiz (-name, -size gibi) kalmıştır. (Nitekim, komutu verdiğinizde find : missing conjunction find : missing conjunction find : missing conjunction find : missing conjunction mesajı alırsınız).

Bu hataların olmaması için, kabuk programının, komut satırımızla oynamamasını ve \*.tmp \*.tmp \*.tmp \*.tmp parametresini, find find find find programına AYNEN göndermesini sağlamamız gerekmektedir. İşte, “ tırnak karakterleri burada işe yaramaktadır.

KABUK PROGRAMLARI, “ TIRNAK KARAKTERLERİ ARASINDA YER ALAN KOMUT

KABUK PROGRAMLARI, “ TIRNAK KARAKTERLERİ ARASINDA YER ALAN KOMUT

KABUK PROGRAMLARI, “ TIRNAK KARAKTERLERİ ARASINDA YER ALAN KOMUT

KABUK PROGRAMLARI, “ TIRNAK KARAKTERLERİ ARASINDA YER ALAN KOMUT

İBİ İLETİR:

İBİ İLETİR:

İBİ İLETİR:

PARÇALARINI ÇÖZÜMLEMEYE ÇALIŞMAZ VE PROGRAMA OLDUÐU G ÐU G ÐU G ÐU GİBİ İLETİR:

PARÇALARINI ÇÖZÜMLEMEYE ÇALIŞMAZ VE PROGRAMA OLDU

PARÇALARINI ÇÖZÜMLEMEYE ÇALIŞMAZ VE PROGRAMA OLDU

PARÇALARINI ÇÖZÜMLEMEYE ÇALIŞMAZ VE PROGRAMA OLDU

Komutumuzu

doğ ru

doğ ru

doğ ru

doğ ru

find /home -name "\*.tmp" -a -size +100 -print find /home -name "\*.tmp" -a -size +100 -print find /home -name "\*.tmp" -a -size +100 -print find /home -name "\*.tmp" -a -size +100 -print olarak verince, find find find find komutunun birinci parametresi /home /home /home /home, ikinci parametresi -name -name -name -name, üçüncüsü \*.tmp \*.tmp \*.tmp \*.tmp, dördüncüsü -a -a -a -a, beşincisi -size -size -size -size, vs. olarak kabul edilecek ve find find find find programı bu parametre yapısıyla çalıştırılacaktı. Yani, \*.tmp \*.tmp \*.tmp \*.tmp kalıbı kabuk tarafından değil, find find find find programı tarafından yorumlanacak ve komut istediğimiz şekilde çalışacaktır.

Eğer, kabuk programının irdelemeden komuta aktarmasını istediğiniz özel karakter tek bir karakterden oluşuyorsa, o karakteri tırnak içine almak yerine, önüne bir \\ \\ \\ \\ (back slash) yerleştirebilirsiniz. Bir başka deyişle "\*.tmp" "\*.tmp" "\*.tmp" "\*.tmp" ile \\\*.tmp \\\*.tmp \\\*.tmp \\\*.tmp ve \\! \\! \\! \\! ile "!" "!" "!" "!" eşdeğerdir.

sıfırıncı parametrelerinin

Bu arada, kabuk tarafından çalıştırılan programların sıfırıncı parametrelerinin

sıfırıncı parametrelerinin

sıfırıncı parametrelerinin

de bulunduğunu söylemeden geçemeyeceğim. Bir program çalıştırıldığında, sıfırıncı parametresi, programın kendi adıdır. Böylece, her program, hangi isimle kullanıldığını bilebilmektedir. Bu özelliğe tipik örnek compress compress compress compress ve uncompress uncompress uncompress uncompress komutlarıdır. Bu iki komut aslında tek bir program dosyasıdır. compress compress compress compress isimli dosya gerçekten bu isimle diskte yer alırken, uncompress uncompress uncompress uncompress sadece bu dosyaya bir bağlantıdır (link).

% which compress which compress which compress which compress

/usr/ucb/compress

% ls -lF /usr/ucb/compress /usr/ucb/uncompress ls -lF /usr/ucb/compress /usr/ucb/uncompress ls -lF /usr/ucb/compress /usr/ucb/uncompress ls -lF /usr/ucb/compress /usr/ucb/uncompress

-rwxr-xr-x 1 root 23783 ... compress\*

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 125

lrwxr-xr-x 1 root 23783 ... uncompress --> ./compress

which which which which komutu da nereden çıktı diyorsunuz... Çok önemli bir komut değil... Parametresi olarak belirtilen komut verilmiş olsaydı, hangi dosyanın çalıştırılacağını bildirir. Bir diğer deyişle, parametresi olan komutu PATH PATH PATH PATH ve/veya path path path path değişkenlerine göre disk(ler)de arar ve ilk bulduğunun (bulursa) yerini bildirir.

Kabuk Değ i şkenleri

Kabuk Değ i şkenleri

Kabuk Değ i şkenleri

Kabuk Değ i şkenleri

compress compress compress compress program dosyasını compress compress compress compress adıyla kullanırsanız, dosya sıkıştırma işlemi; uncompress uncompress uncompress uncompress adıyla çalıştırırsanız, daha önce sıkıştırılmış olan bir dosyayı açma işlemi yapılmasını sağlarsınız.

Kullandığınız kabuk programı içinde çeşitli değişkenler tanımlamanız mümkündür; hatta bazı standart değişkenler zaten tanımlıdır. Kabuk değişkenleri arasında en önemlileri Bourne Shell Bourne Shell Bourne Shell Bourne Shell C Shell C Shell C Shell C Shell Görevi Görevi Görevi Görevi (sh) (sh) (sh) (sh) (csh) (csh) (csh) (csh) PATH PATH PATH PATH path path path path Bir komut verildiğinde, komut programını oluşturan dosyanın aranacağı dizinler listesini belirleyen değişken.

HOME HOME HOME HOME HOME HOME HOME HOME Kullanıcının home home home home dizinin adını içeren değişken. login login login login ettiğinizde kabuk programı tarafından otomatik olarak yaratılır.

MAIL MAIL MAIL MAIL mail mail mail mail Size elektronik posta (e-mail) gelip gelmediğini anlamak için kontrol edilecek dosyaların listesi.

PS1 PS1 PS1 PS1 Tanımlanmazsa $ $ $ $ kabul edilir prompt prompt prompt prompt Tanımlanmazsa

% % % % kabul edilir

Sistem hazır işaretini tanımlayan değişken.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 126

TERM TERM TERM TERM TERM TERM TERM TERM Kullandığınız terminalin tipini belirleyen değişkendir. Eğer vi vi vi vi editörünü kullanmak istediğinizde ekranınıza garip işaretler yanısıra satırlar da garip bir düzensizlik içinde çıkıyorsa, büyük olasılıkla TERM TERM TERM TERM değişkeniniz hatalı bir değere sahiptir ya da hiç tanımlı değildir.

Bu değişkenin kullanımı, /etc/termcap /etc/termcap /etc/termcap /etc/termcap dosyasındaki binlerce değişik terminal tipinin tanımlarıyla yakından ilgilidir. TERM TERM TERM TERM değişkeninize vermeniz gereken değer için sistem yöneticinize danışınız. history history history history Sadece csh csh csh csh kabuğunda anlamlıdır. Bu değişkenin değeri, klavyeden gireceğiniz komutlardan son kaç tanesinin saklanacağını ve ! ! ! ! ile birlikte tekrar kullanılabileceğini belirtir. Tipik değeri 30-50 arasındadır.

Örnekler Örnekler Örnekler Örnekler Bourne Shell (sh) Bourne Shell (sh) Bourne Shell (sh) Bourne Shell (sh) C Shell (csh) C Shell (csh) C Shell (csh) C Shell (csh) PATH=/bin:/usr/local/bin:. PATH=/bin:/usr/local/bin:. PATH=/bin:/usr/local/bin:. PATH=/bin:/usr/local/bin:. set path=( /bin /usr/local/bin . ) set path=( /bin /usr/local/bin . ) set path=( /bin /usr/local/bin . ) set path=( /bin /usr/local/bin . )

veya

setenv PATH /bin:/usr/local/bin:. setenv PATH /bin:/usr/local/bin:. setenv PATH /bin:/usr/local/bin:. setenv PATH /bin:/usr/local/bin:. MAIL=/usr/mail/ayfer MAIL=/usr/mail/ayfer MAIL=/usr/mail/ayfer MAIL=/usr/mail/ayfer setenv mail /usr/mail/ayfer setenv mail /usr/mail/ayfer setenv mail /usr/mail/ayfer setenv mail /usr/mail/ayfer PS1="ayfer@abc $ " PS1="ayfer@abc $ " PS1="ayfer@abc $ " PS1="ayfer@abc $ " set prompt="ayfer@abc % " set prompt="ayfer@abc % " set prompt="ayfer@abc % " set prompt="ayfer@abc % " TERM=vt100 TERM=vt100 TERM=vt100 TERM=vt100 setenv TERM vt100 setenv TERM vt100 setenv TERM vt100 setenv TERM vt100 setenv history 100 setenv history 100 setenv history 100 setenv history 100

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 127

Bazı UNIX’lerdeki sh sh sh sh uyarlamalarında, bir kabuk değişkenine değer verdikten sonra değişkeni export export export export komutu ile geçerli kılmanız gerekebilir. Şöyle ki :

PATH=/bin:/usr/local/bin:. PATH=/bin:/usr/local/bin:. PATH=/bin:/usr/local/bin:. PATH=/bin:/usr/local/bin:. komutundan hemen sonra export PATH export PATH export PATH export PATH komutunu vermeniz gerekebilir.

Herhangi bir anda, tanımlı olan kabuk değişkenlerini ve/veya değerlerinin ne olduğunu merak ederseniz

% set % set % set % set % env % env % env % env % setenv % setenv % setenv % setenv sh ve csh için

sh için csh için komutlarını kullanabilirsiniz Kabuk değişkenleri, standart isimli bir takım değişkenlerle sınırlı değildir.

Kullandığınız uygulama programları, çalışma ortamını tanımlamak için bir takım değişkenlerin tanımlanmasını ve özel değerler verilmesini gerektirebilir.

Örneğin X Windows uygulamaları, kullanılacak ekranın bağlı bulunduğu bilgisayarın adının DISPLAY DISPLAY DISPLAY DISPLAY isimli bir değişkende tanıtılmasını gerektirecektir. C Shell’e Özgü Özellikler C Shell’e Özgü Özellikler C Shell’e Özgü Özellikler C Shell’e Özgü Özellikler UNIX dünyasında kabuk programı olarak csh csh csh csh kullanımı gittikçe yaygınlaşmaktadır. Bu nedenle kitabın bundan sonraki kısımlarında kullanıcıların kabuk programı olarak C Shell kullandıklarını varsayacağım. Eğer bu kitapta bundan sonra anlatılacak konulardaki örnekleri denemek istiyorsanız, csh csh csh csh kabuk programını kullanıyor olmalısınız. Hangi kabuk programını kullandığınızı bilmiyorsanız, sisteme login ettiğinizde sizin için başlatılacak olan kabuk programınızı değiştirmeniz gerekiyorsa sistem yöneticinizden yardım isteyiniz. Kullandığınız kabuk tcsh tcsh tcsh tcsh ise bir değişiklik yapmanız gerekmeyecektir. csh csh csh csh’in bazı önemli özelliklerini örneklerle açıklamak istiyorum :

Hatalı Komutları Düzeltme

Hatalı Komutları Düzeltme

Hatalı Komutları Düzeltme

Hatalı Komutları Düzeltme

Diyelimki uzun bir UNIX komutunu yanlış yazdınız.... cp /home/hakman/.Xdesksetdefualts /home/ayfer cp /home/hakman/.Xdesksetdefualts /home/ayfer cp /home/hakman/.Xdesksetdefualts /home/ayfer cp /home/hakman/.Xdesksetdefualts /home/ayfer (.Xdesksetdef .Xdesksetdef .Xdesksetdef .Xdesksetdefau au au aults lts lts lts olmalı ydı...) ve doğal olarak .Xsetdefualts .Xsetdefualts .Xsetdefualts .Xsetdefualts diye bir dosya bulunamadığına dair bir hata mesajı aldınız. Eğer csh csh csh csh kullanıyorsanız, bu karışık satırı baştan bir kez daha yazmak yerine

% ^fual^faul^ % ^fual^faul^ % ^fual^faul^ % ^fual^faul^

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 128

yazıp ENTER tuşuna basmanız yeterli olacaktır. (“Bir önceki komuttaki fual fual fual fual karakter dizisini faul faul faul faul karakter dizisi ile değiştir ve komutu tekrarla” anlamında...)

Son Komutu Tekrarlama Son Komutu Tekrarlama Son Komutu Tekrarlama Son Komutu Tekrarlama Diyelimki MS-DOS işletim sisteminden alışkanlıkla

% cp /home/hakman/.Xdesksetdefaults % cp /home/hakman/.Xdesksetdefaults % cp /home/hakman/.Xdesksetdefaults % cp /home/hakman/.Xdesksetdefaults

yazdınız. UNIX kurallarına göre kopyalamanın nereye yapılacağını da belirtmiş olmanız gerekirdi. csh csh csh csh kullanıyorsanız, böyle bir durumda, tüm komutu tekrarlamak yerine

% !! /home/ayfer % !! /home/ayfer % !! /home/ayfer % !! /home/ayfer

yazmanız yeterli olacaktır. Böylece; bir önceki komutunuz aynen tekrarlanacaktır; ancak sonuna /home/ayfer /home/ayfer /home/ayfer /home/ayfer eklenmiş olarak...

Eski Bir Komutu Tekrarlama Eski Bir Komutu Tekrarlama Eski Bir Komutu Tekrarlama Eski Bir Komutu Tekrarlama Eğer history history history history isimli kabuk değişkeniniz tanımlıysa, bu değişkenin değeri kadar sayıda UNIX komutu kabuk tarafından bir ara bellekte saklanacaktır. Her hangi bir anda, eski komutlarınızı

% history % history % history % history

komutuyla listeyebilirsiniz.

% history history history history

.....

7 23:12 ls -l 8 23:13 cat /etc/printcap 9 23:13 cp /usr/bin/.... .....

Bu eski komutlardan birini tekrar çalıştırmak isterseniz, bir ünlem işaretinin ardından o komutun listedeki sıra numarasını girmeniz yeterli olacaktır.

% !8 % !8 % !8 % !8 8 numaralı komutu tekrarlama

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 129

İ lk Birkaç Harfini Hatırladı ğ ınız Eski Bir Komutu Tekrarlama

İ lk Birkaç Harfini Hatırladı ğ ınız Eski Bir Komutu Tekrarlama

İ lk Birkaç Harfini Hatırladı ğ ınız Eski Bir Komutu Tekrarlama

İ lk Birkaç Harfini Hatırladı ğ ınız Eski Bir Komutu Tekrarlama

Her hangi bir anda, ilk harfini (ya da birkaç harfini) hatırladığınız eski bir komutu tekrarlamak isterseniz

% !c % !c % !c % !c % !ca % !ca % !ca % !ca c c c c harfiyle başlayan son komutu tekrarla

ca ca ca ca harfleriyle başlayan son komutu tekrarla Kendi Gereksinimlerinize Göre Özel Komut Yaratma Kendi Gereksinimlerinize Göre Özel Komut Yaratma Kendi Gereksinimlerinize Göre Özel Komut Yaratma Kendi Gereksinimlerinize Göre Özel Komut Yaratma UNIX kullanıcılarının çok sık tekrarladıkları bazı uzun komutları, daha kısa ve kolay yazılan komutlarla değiştirmeleri mümkündür. Bu iş csh csh csh csh’in alias alias alias alias komutu ile yapılır.

Örneğin, history history history history komutunu her seferinde uzun uzun yazmaktansa,

% alias h history % alias h history % alias h history % alias h history artık history history history history yerine h h h h

kullanabilirsiniz ls ls ls ls listelerinde isimlerin çalıştırılabilir program olup olmadığını \* \* \* \* işaretiyle, dizinlerinse / / / / işaretiyle belirlenmesi için kullanılan -F -F -F -F seçeneğinin standart hale getirilmesi için :

% alias ls "ls -F" % alias ls "ls -F" % alias ls "ls -F" % alias ls "ls -F" yeni tanımda birden fazla sözcük

olduğ u için tırnak kullanmak gerekir Eğer more more more more komutunu sık sık hatalı yazıyorsanız :

% alias mroe more % alias mroe more % alias mroe more % alias mroe more

MS-DOS alışkanlıklarınızdan vaz geçemiyorsanız :

% alias dir "ls -F" % alias dir "ls -F" % alias dir "ls -F" % alias dir "ls -F"

% alias copy "cp -i" % alias copy "cp -i" % alias copy "cp -i" % alias copy "cp -i"

% alias del "rm -i" % alias del "rm -i" % alias del "rm -i" % alias del "rm -i"

% alias ren mv % alias ren mv % alias ren mv % alias ren mv

% alia % alia % alia % alias edit vi s edit vi s edit vi s edit vi

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 130

Herhangi bir anda geçerli olan alias alias alias alias’ları listelemek için

% alias % alias % alias % alias

Hazır işaretinizin her zaman çalışma dizininizi göstermesi için

% alias cd ‘cd \\!\*;set prompt="\`hostname\`:$cwd> "‘ % alias cd ‘cd \\!\*;set prompt="\`hostname\`:$cwd> "‘ % alias cd ‘cd \\!\*;set prompt="\`hostname\`:$cwd> "‘ % alias cd ‘cd \\!\*;set prompt="\`hostname\`:$cwd> "‘

biraz çetrefilli ama çalı şır... Bana güvenin..

Programları Arka Planda Çalı ştırma

Programları Arka Planda Çalı ştırma

Programları Arka Planda Çalı ştırma

Programları Arka Planda Çalı ştırma

Diyelim ki, çok büyük bir disk dosyasındaki (söz gelimi 42 Mbyte) müşteri kayıtlarını alfabetik sıraya dizmek istiyorsunuz. Bu iş için kullandığınız bilgisayar sisteminde yarım saat süreceğini varsayalım. Eğer tek iş düzeninde çalışan bir işletim sistemi kullanıyor olsaydınız (MS-DOS gibi), sıralama komutunu verdikten sonra ( sort sort sort sort ) yemeğe çıkabilir veya köpeğinizi dolaştırmaya götürebilirdiniz; çünkü sıralama bitinceye kadar bilgisayarınızdan bir başka amaçla yararlanmanız söz konusu olamazdı. Oysa, UNIX işletim sisteminde, sıralamayı arka planda arka planda arka planda arka planda bir iş olarak başlattıktan sonra, ön planda başka işler yapmanız mümkündür. Bunu yapabilmek için tek yapmanız gereken, arka planda yapılmasını istediğiniz işi başlatan komutun sonuna bir & & & & işareti eklemekten ibarettir.

% sort musteri-dosyasi & % sort musteri-dosyasi & % sort musteri-dosyasi & % sort musteri-dosyasi & &, &, &, &, i şi arka planda

yürütmek istediğ inizi belirtiyor Elbetteki her iş bu şekilde arka planda çalıştırılmaya uygun değildir. Örneğin, bir muhasebe fiş giriş programı gibi; kullanıcının sürekli olarak klavyeden bilgi girmesini gerektiren programlar arka planda çalıştırılsa bile, sürekli ilgi istedikleri için bu tip bir çalışma rahat olmaz. Oysa, yukarıdaki sıralama örneğimizde, sıralama süresince kullanıcıdan herhangi bir bilgi istenmeyecektir. Sıralama programı arka planda sessizce çalışıp işini bitirecektir.

Bazı programlar, kulanıcıdan bir bilgi istememekle birlikte, sürekli olarak ekrana, yaptıkları işin gelişmesini açıklayan bilgiler dökerler. Bu tip bir programı arka planda çalışmak üzere başlattığınızda; sürekli olarak ekrana gelen bilgiler yüzünden ön planda başka bir iş yapmanıza pek olanak kalmaz.

Örneğin, genellikle teybe yedekleme yapmak için kullanılan tar tar tar tar komutunu

% tar -cvf /dev/rst1 /home/ayfer & tar -cvf /dev/rst1 /home/ayfer & tar -cvf /dev/rst1 /home/ayfer & tar -cvf /dev/rst1 /home/ayfer &

şeklinde verirseniz (bu komutla ilgili detaylı bilgiyi daha ileride vereceğim; şimdilik komutun ne yaptığı ve parametrelerinin ne olduğu üzerinde durmayınız), program arka planda teybe yedekleme yapacaktır, ama bir

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 131

yandan da kopyalamayı tamamladığı bütün dosyaların isimlerini ekrana listeleyecektir. Böyle her saniye yeni bir satır gelen ekranda başka bir iş yapmak pek kolay olmayacaktır.

Ancak aynı komutu

% tar -cvf /dev/rst1 /home/ayfer > tarmesajlari & % tar -cvf /dev/rst1 /home/ayfer > tarmesajlari & % tar -cvf /dev/rst1 /home/ayfer > tarmesajlari & % tar -cvf /dev/rst1 /home/ayfer > tarmesajlari &

şeklinde verirseniz ekrana gelmesi gereken tüm mesajlar, çalışma dizininizde tarmesajlari tarmesajlari tarmesajlari tarmesajlari isimli bir dosyaya yönlendirilmiş olur. İş bittikten sonra tarmesajlari tarmesajlari tarmesajlari tarmesajlari dosyasına bakarak teybe kopyalama işinin başarıyla bitip bitmediğini ve kopyalanan dosyaların listesini görebilirsiniz.

Ön Planda Çalı şan Programları Arka Plana Atma

Ön Planda Çalı şan Programları Arka Plana Atma

Ön Planda Çalı şan Programları Arka Plana Atma

Ön Planda Çalı şan Programları Arka Plana Atma

Sadece C Shell’de geçerlidir Bazı durumlarda, başlattığınız bir programın ne kadar süreyle çalışacağını önceden kestiremezsiniz. İşin uzun süreceğini ve sessiz çalışan bir iş olduğunu sonradan farkedersiniz; ya da işin bu özelliklerini bilseniz bile, boş bulunup komut satırının sonuna & & & & koymadan Enter tuşuna basıverirsiniz. Örneğin, bir dizindeki tüm dosyaları bir başka diske ya da dizine çekme komutunu cp -r /home/ayfer /disk2/home2 cp -r /home/ayfer /disk2/home2 cp -r /home/ayfer /disk2/home2 cp -r /home/ayfer /disk2/home2 şeklinde verdiğinizi ve programı ön planda çalıştırdığınızı varsayalım.

Başlattıktan bir kaç saniye (ya da birkaç dakika) sonra işin uzun süreceğini farkettiniz ve ‘’Tüh! Keşke arka planda başlatsaydım!!’’

’Tüh! Keşke arka planda başlatsaydım!!’’ dediniz. Eğer kabuk ’Tüh! Keşke arka planda başlatsaydım!!’’

’Tüh! Keşke arka planda başlatsaydım!!’’ programı olarak csh csh csh csh kullanıyorsanız sorun değil...

Klavyenizden ^Z ^Z ^Z ^Z tuşuna basarsanız (Control tuşu basılıyken Z tuşuna da basarsanız) ekranda Suspended. Suspended. Suspended. Suspended. mesajını görürsünüz. Bu mesaj, o sırada ön planda çalışan işinizin geçici olarak askıya alındığını göstermektedir; ancak, buradaki durdurma durdurma durdurma durdurma kelimesi, işinizin tamamlanmadan kesildiği anlamında kullanılmamaktadır. Buradaki durdurma durdurma durdurma durdurma, müzik kaseti çalan teyplerdeki PAUSE düğmesinin görevine benzeyen bir durdurmadır. İşiniz çalışmaya ara vermiş ve devam edebilmek için sizden bir komut bekler durumdadır.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 132

Bu noktada

% bg % bg % bg % bg Background

komutu verirseniz işniz arka planda çalışmaya devam edecektir. Ancak, o anda ekranda bir de \[1\] cp ... & \[1\] cp ... & \[1\] cp ... & \[1\] cp ... & mesajı görünecektir. Bu mesajın kısaca anlamı şudur :

Programınız (komutunuz) arka planda çalı şır duruma alındı...

Bu şekilde arka plana atılan i şler arasında sıra numarası 1 oldu.

Bu işi tekrar ön plana almak isterseniz

% fg %1 % fg %1 % fg %1 % fg %1 Foreground

komutunu verebilirsiniz. (Eğer birden fazla arka plana atılmış işiniz varsa, % % % % işaretinden sonra o işin numarasını yazmayı unutmamalısınız.)

Arka planda çalışmak üzere başlatılacak; ya da sonradan arka plana atılacak işlerin sayısı ile ilgili herhangi bir sınırlama yoktur. Ancak arka plan ya da ön plan olsun, çalışan her işin bilgisayarın performansından bir pay alacağını unutmamalısınız.

Bazan, arka planda başlattığınız ya da sonradan arka plana attığınız işlerin hesabını şaşırabilirsiniz. Böyle bir durumda

% jobs % jobs % jobs % jobs

komutunu verirseniz, arka plana atılmış işlerin bir listesini alırsınız.

Benzeri bir listeyi

% ps % ps % ps % ps process status

komutuyla da alırsınız. Ancak ps ps ps ps komutunun görevleri biraz daha farklı olabilmektedir. ps ps ps ps komutu, parametresiz olarak verildiğinde, kullanıcı olarak sizinle ilgili olarak başlatılmış olan işlerin listesini verir. UNIX işletim sisteminde, siz tek bir iş yaparken (hatta hiç program çalıştırmazken bile) sizinle ilgili birkaç iş, UNIX kabuk kabuk kabuk kabuk programı tarafından çalıştırılmaktadır (bu arada kabuk programının kendisi de çalışmaya devam etmektedir.) Hele X Windows, Motif, OpenWindows gibi grafik kullanıcı arabirimleri (GUI :

Graphical User Interface) kullanıyorsanız; sizinle ilgili olarak onlarca iş başlatılmış olduğunu göreceksiniz. jobs jobs jobs jobs komutu sizin tarafınızdan arka plana atılmış işleri; ps ps ps ps komutuysa, daha geniş kapsamlı olarak sistemdeki işleri ve bu işlerle ilgili çalışma istatistiklerini listeler.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 133

UNIX’de SÜREÇ (process) Kavramı - Tekrar Bir Göz Atı ş

UNIX’de SÜREÇ (process) Kavramı - Tekrar Bir Göz Atı ş

UNIX’de SÜREÇ (process) Kavramı - Tekrar Bir Göz Atı ş

UNIX’de SÜREÇ (process) Kavramı - Tekrar Bir Göz Atı ş

Süreçler, UNIX işletim sisteminde çok iyi anlaşılması gereken bir

Süreçler, UNIX işletim sisteminde çok iyi anlaşılması gereken bir

Süreçler, UNIX işletim sisteminde çok iyi anlaşılması gereken bir

Süreçler, UNIX işletim sisteminde çok iyi anlaşılması gereken bir

kavramdır. Bu nedenle, bu konuyu bir kez daha tekrarlamak

kavramdır. Bu nedenle, bu konuyu bir kez daha tekrarlamak

kavramdır. Bu nedenle, bu konuyu bir kez daha tekrarlamak

kavramdır. Bu nedenle, bu konuyu bir kez daha tekrarlamak

istiyorum. Okuyucunun eski bir bölümü tekrar okumasını

istiyorum. Okuyucunun eski bir bölümü tekrar okumasını

istiyorum. Okuyucunun eski bir bölümü tekrar okumasını

istiyorum. Okuyucunun eski bir bölümü tekrar okumasını

istemektense, burada tekrarlamanın daha sempatik ve yararlı

istemektense, burada tekrarlamanın daha sempatik ve yararlı

istemektense, burada tekrarlamanın daha sempatik ve yararlı

istemektense, burada tekrarlamanın daha sempatik ve yararlı

olduğunu düşünüyorum. Üstelik, okuyucunun UNIX’e daha yatkın bir

olduğunu düşünüyorum. Üstelik, okuyucunun UNIX’e daha yatkın bir

olduğunu düşünüyorum. Üstelik, okuyucunun UNIX’e daha yatkın bir

olduğunu düşünüyorum. Üstelik, okuyucunun UNIX’e daha yatkın bir

duruma geldiğini dikkate alarak biraz daha ayrıntılı olarak anlatma

duruma geldiğini dikkate alarak biraz daha ayrıntılı olarak anlatma

duruma geldiğini dikkate alarak biraz daha ayrıntılı olarak anlatma

duruma geldiğini dikkate alarak biraz daha ayrıntılı olarak anlatma

ve örnekleme olanağı bulmuş olacağım. Tekrarlamaya gerek

ve örnekleme olanağı bulmuş olacağım. Tekrarlamaya gerek

ve örnekleme olanağı bulmuş olacağım. Tekrarlamaya gerek

ve örnekleme olanağı bulmuş olacağım. Tekrarlamaya gerek

görmeyen okuyucular bu bölümü atlayabilirler. görmeyen okuyucular bu bölümü atlayabilirler. görmeyen okuyucular bu bölümü atlayabilirler. görmeyen okuyucular bu bölümü atlayabilirler. UNIX, tasarımından kaynaklanan nedenlerle, çeşitli problemlerin çözümü için yazılan programların, problemi parçalayıp, her bir parçanın ayrı bir (ya da birkaç) programdan oluşacak şekilde yazılmasına olanak sağlamaktadır . Pek açık olmadı, farkındayım. İsterseniz örneklerle biraz daha açmaya çalışayım.

UNIX’i yazan insanların bakış açısıyla düşünelim... İşletim sistemi aynı anda şu temel işlerle ilgilenmek zorunda : (bu temel işler herhangi bir sıraya göre verilmemiştir) 1) Kullanıcı programlarının veya bu programları oluşturan süreçlerin bir seferinde ve kesintisiz olarak 200 milisaniyeden fazla MİB kullanmalarını önlemek için işletim sisteminin bir modülü sürekli olarak zamanı izlemeli.

2) Hangi kullanıcının hangi terminalden ne zaman sisteme gireceği belli olmadığından, işletim sisteminin bir modülü, devamlı olarak terminallerin bağlandığı arabirimleri gözlemeli, sisteme login login login login etmek isteyen kimse varsa, ona hizmet edecek programları başlatmalı.

3) Hangi kullanıcının ne zaman hangi yazıcıya bir şeyler göndereceği bilinemediğinden ve ayrıca yazıcıların herhangi bir anda, ne durumda olacakları kestirilemeyeceğinden dolayı bir (ya da birkaç) program sürekli olarak yazıcılarla ilgilenmeli.

4) Elektronik posta (mail) keza...

5) Hele hele bilgisayar bir bilgisayar ağına bağlıysa durum daha da yürekler acısı... İzlenmesi gereken çevre birimleri yetmezmiş gibi bir de sağdan soldan gelen erişim isteklerine yanıt vermek gereklidir.

6) vs. vs.

UNIX işletim sistemini tasarlayanlar, bu problemlerin çözümüne doğru önemli bir kavram geliştirmişler : SÜREÇ SÜREÇ SÜREÇ SÜREÇ (PROCESS ).

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 134

Bu tasarıma göre, yapılması gerek tüm işler için ayrı ve bağımsız çalışabilen programlar yazılır, bu bağımsız programlar gerektiğinde birbirleriyle mesaj alışverişinde bulunabilirler ve sıradan kullanıcı programları gibi bilgisayarların MİB, bellek gibi kaynaklarını paylaşırlar.

Bazı süreçlere daemon daemon daemon daemon (sözlük anlamıyla : kötü ruh, iblis, iblisin uşağı) adı verilir. Neden bu adın seçildiğini bilmiyorum ama bu tip süreçlerin ortak özellikleri şunlar:

♦ Arka planda tamamen sessizce çalışırlar, ♦ Hata mesajları olsa bile bunu genellikle ekrana değil, kendilerine ait bir disk dosyasına yazarlar (Log File), ♦ Klavyeden müdahale gerektirmezler, ♦ İsimleri genellikle d d d d harfiyle biter.

Her hangi bir anda sistemde çalışmakta olan süreçlerin listesini almak için ps ps ps ps komutu kullanılır. BSD veya System V UNIX için küçük farklar gösteren bu komutun en çok kullanılan kalıpları ve bu kalıplar için örnekleri izleyen sayfalarda bulacaksınız.

BERKELEY UNIX (BSD) BERKELEY UNIX (BSD) BERKELEY UNIX (BSD) BERKELEY UNIX (BSD) ps ps ps ps ps -a ps -a ps -a ps -a ps -ax ps -ax ps -ax ps -ax Kullanıcı yla ilgili süreçleri listeler Tüm kullanıcılarla ilgili süreçleri listeler Tüm kullanıcılar ve sistemle ilgili süreçleri listeler ps -axl ps -axl ps -axl ps -axl l (le harfi) seçeneğ i ayrıntılı liste verilmesini sağ lar AT&T UNIX (System V) AT&T UNIX (System V) AT&T UNIX (System V) AT&T UNIX (System V) ps ps ps ps ps -a ps -a ps -a ps -a ps -ae ps -ae ps -ae ps -ae Kullanıcı yla ilgili süreçleri listeler Tüm kullanıcılarla ilgili süreçleri listeler Tüm kullanıcılar ve sistemle ilgili süreçleri listeler ps -ael ps -ael ps -ael ps -ael l (le harfi) seçeneğ i ayrıntılı liste verilmesini sağ lar

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 135

BSD UNIX’de ps komutu kullanımına bir kaç örnek....

BSD UNIX’de ps komutu kullanımına bir kaç örnek....

BSD UNIX’de ps komutu kullanımına bir kaç örnek....

BSD UNIX’de ps komutu kullanımına bir kaç örnek....

abc:/home/ayfer> ps abc:/home/ayfer> ps abc:/home/ayfer> ps abc:/home/ayfer> ps

PID TT STAT TIME COMMAND

29011 a R 0:00 ps abc:/home/ayfer> abc:/home/ayfer> ps -x abc:/home/ayfer> ps -x abc:/home/ayfer> ps -x abc:/home/ayfer> ps -x

PID TT STAT TIME COMMAND

28731 a S 0:00 -tcsh (tcsh) 29010 a R 0:00 ps -x abc:/home/ayfer> ps -axl abc:/home/ayfer> ps -axl abc:/home/ayfer> ps -axl abc:/home/ayfer> ps -axl F UID PID PPID CP PRI NI SZ RSS WCHAN STAT TT TIME COMMAND 80003 0 0 0 0 -25 0 0 0 runout D ? 1:20 swapper 20088000 0 1 0 0 5 0 52 0 child IW ? 0:08 /sbin/init - 80003 0 2 0 0 -24 0 0 0 child D ? 0:04 pagedaemon 88000 0 58 1 0 1 0 68 0 select IW ? 0:58 portmap 88000 0 63 1 0 1 0 224 0 select IW ? 14:39 ypserv 88000 3 65 1 0 1 0 36 0 select IW ? 0:01 ypbind 88000 0 67 1 1 1 0 40 0 select IW ? 0:00 rpc.ypupdate 88000 0 69 1 0 1 0 40 0 select IW ? 0:00 keyserv 88001 0 114 1 0 1 0 40 64 select I ? 1:09 in.routed 88000 0 117 1 0 1 0 324 0 select IW ? 2:02 in.named 88001 0 120 1 0 1 0 16 0 nfs\_dnlc I ? 0:00 (biod) 88000 0 134 1 0 1 0 60 0 select IW ? 0:16 syslogd 88000 0 148 1 0 1 0 108 0 select IW ? 1:09 rpc.mountd - 88000 0 153 1 1 1 0 52 0 select IW ? 0:00 rpc.statd 88001 0 154 149 0 1 0 28 0 socket I ? 23:57 (nfsd) 88000 0 161 1 0 1 0 84 0 select IW ? 0:00 rpc.lockd 88000 0 167 1 0 1 0 80 0 select IW ? 0:06 /usr/etc/rpc 80201 0 182 1 0 15 0 12 4 kernelma S ? 109:22 update 488000 0 185 1 0 1 0 56 0 Heapbase IW ? 0:00 cron 88000 0 191 1 0 1 0 48 0 select IW ? 0:47 inetd 88000 0 194 1 0 1 0 52 0 select IW ? 0:00 /usr/lib/lpd 20488020 560 4969 1 0 1 0 132 0 socket IW ? 0:04 ncftp ramiga 88401 0 24725 167 0 25 0 0 0 Z ? 0:00 <defunct> 20088000 0 27454 1 0 3 0 40 0 Heapbase IW co 0:00 - cons8 cons 204882018700 28731 1 0 15 0 216 700 kernelma S a 0:00 -tcsh (tcsh) 200000018700 29007 28731 24 31 0 216 468 R a 0:00 ps -axl abc:/home/ayfer>

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 136

abc:/home/ayfer> ps -ax abc:/home/ayfer> ps -ax abc:/home/ayfer> ps -ax abc:/home/ayfer> ps -ax

PID TT STAT TIME COMMAND

0 ? D 1:20 swapper 1 ? IW 0:08 /sbin/init - 2 ? D 0:04 pagedaemon 58 ? IW 0:58 portmap 63 ? IW 14:39 ypserv 67 ? IW 0:00 rpc.ypupdated 69 ? IW 0:00 keyserv 114 ? I 1:09 in.routed 117 ? IW 2:02 in.named 120 ? I 0:00 (biod) 134 ? IW 0:16 syslogd 142 ? IW 0:05 /usr/lib/sendmail -bd -q1h 148 ? IW 1:09 rpc.mountd -n 149 ? I 24:20 (nfsd) ...

Meraklı olan okuyucular için yukarıdaki örneklerde adı geçen bazı süreçlerin açıklamalarını yapmak istiyorum. Ancak bunların sadece birer örnek olduğunu, gerçek süreç listelerinin daha uzun ve/veya daha farklı olacağını unutmamalısınız.

Süreç Süreç Süreç Süreç Görevi Görevi Görevi Görevi lpd lpd lpd lpd Line printer daemon. Yazıcılarla ilgilenir. Yazıcı(lar)dan dökülmek üzere gönderilen bilgilerin sıraya konmasından ve yazıcıların yönetiminden sorumludur. kill kill kill kill komutunu kullanarak bu süreci öldürürseniz artık kimse yazıcılardan döküm alamaz. inetd inetd inetd inetd Internetworking daemon. Bilgisayar ağı üzerinden gelip giden servis istekleriyle ilgilenir. cron cron cron cron Günün, haftanın, ayın belirli zamanlarında çalıştırılması gereken programları izler; zamanı gelen programı başlatır. update update update update Disk tampon bellek alanlarının belirli aralıklarla disklere kaydedilmesini sağlar(flush); böylece bir arıza ya da enerji kesintisi durumunda ortaya çıkabilecek bilgi kaybını en aza indirir.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 137

syslogd syslogd syslogd syslogd Sistemde meydana gelen önemli olayları uygun log log log log dosyalarına kaydeder. (Sisteme giren/çıkan kullanıcıları, root root root root kullanıcı kimliğini alan kullanıcıları, donanımla ilgili sorunları vs. kaydeder.) swapper swapper swapper swapper Ana belleğin yetmediği durumlarda diskte ayrılmış olan swap swap swap swap alanının sanki ana belleğin bir uzantısıymış gibi kullanılmasını sağlar. init init init init Kullanıcı terminallerini dinler. Sisteme girmek üzere terminalini açan bir kullanıcıya rastlarsa, onun sisteme login login login login edebilmesi için gerekli hazırlıkları yapar. in.routed in.routed in.routed in.routed Bilgisayar ağı üzerinde, çeşitli mesajların doğru bilgisayarlara ulaşmasından sorumludur. in.named in.named in.named in.named Bilgisayar ağı üzerinde, adresi bilinmeyen bilgisayarların yer ve adreslerinin bulunabilmesi ile ilgili protokolleri yürütmekle görevlidir.

-tcsh -tcsh -tcsh -tcsh İlgili olduğu kullanıcı terminali için çalışan bir kabuk programıdır.

Önceki sayfalardaki ps ps ps ps komutlarının çıktılarının oldukça karmaşık bir görünümde olduklarını kabul etmek lazım. Ancak, gözünüzü, sürecin adının gösterildiği son kolonla PID PID PID PID kolonlarına alıştırırsanız, tipik bir UNIX kullanıcısının gerek duyabileceği tüm bilgileri almış olursunuz. Aradığınız sürecin adı bu listede varsa, programınız çalışıyor demektir (aslında çalışmaktan çalışmaya fark var... UNIX açısından çalışıyor, fakat sizin istediğiniz işleri yapmıyor olabilir; o başka mesele). PID PID PID PID kolonundaki numaraysa UNIX’in sizin programınızı izlemek ve denetlemek için kullandığı

süreç tanıtım numarasıdır

süreç tanıtım numarasıdır (PROCESS ID). UNIX altında çalışan programların

süreç tanıtım numarasıdır

süreç tanıtım numarasıdır

herbirinin özgün (unique) bir PID PID PID PID numarası vardır. Bu numaranın büyüklüğü veya küçüklüğü bir anlam taşımaz. Nitekim, UNIX, programlara verdiği PID numarası 65535 e ulaşınca, tekrar birden başlatmakta bir sakınca görmez. (PID numaraları her UNIX’de 65535 le sınırlı değildir; bazı uyarlamalarda bu sayı daha da büyüyebilir; ancak bunun kullanıcılar için pek önemi yoktur.)

Eğer bir süreç (ya da program) çakılıp kaldıysa; ya da sizin istediğiniz gibi ÖLDÜREBİLİRSİNİZ.

ÖLDÜREBİLİRSİNİZ. davranmıyorsa o süreci ÖLDÜREBİLİRSİNİZ.

ÖLDÜREBİLİRSİNİZ. Deyim çok tatmin edici; değil mi?

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 138

% kill nnn % kill nnn % kill nnn % kill nnn (kill process )

Bu komut, tanıtım numarası (PID PID PID PID) olan süreci öldürmek için kullanılır. Tek bir komutla birden fazla süreci beraber öldürebilirsiniz. kill 154 185 117 kill 154 185 117 kill 154 185 117 kill 154 185 117 gibi...

Eğer öldürmek istediğiniz süreç ölmemek için direniyorsa,

% kill -9 nnn % kill -9 nnn % kill -9 nnn % kill -9 nnn şartsız öldürme

formunu deneyiniz. Eğer süreç gene ölmezse daha fazla uğraşmayınız. Bazı süreçler ölemezler. Bu tip süreçlere zombie zombie zombie zombie adı verilir. (Hoş... Değil mi ?)

Zombie Zombie Zombie Zombie süreçler genellikle pek sistem zamanı ya da bellek harcamazlar. Bu tip süreçlerin sistemde çalışır durumda olması genellikle zararsızdır.

Öldürülen bir süreç, daha önce başka süreçler yarattıysa; yani eğer bir ebeveyn süreçse (parent process parent process parent process parent process), büyük olasılıkla o yavru süreçler de (child child child child process process process process) ölecektir. Bu nedenle mecbur olmadıkça süreçleri sona erdirmek için bu öldürme yöntemini kullanmayınız. kill kill kill kill komutu ile sadece kendinize ait süreçleri öldürebilirsiniz. Sisteme, ya da başka kullanıcılara ait süreçleri öldürme yetkisi sadece root root root root kullanıcıya aittir.

Zaman zaman klavyenizin kilitlendiği ve sistemin hiç bir komuta tepki göstermediği durumlarla karşılaşacaksınız. Böyle bir durumda, Böyle bir durumda, Böyle bir durumda, Böyle bir durumda,

bilgisayarı kapatıp açmayı aklınızdan bile geçirmemelisiniz.

bilgisayarı kapatıp açmayı aklınızdan bile geçirmemelisiniz.

bilgisayarı kapatıp açmayı aklınızdan bile geçirmemelisiniz.

bilgisayarı kapatıp açmayı aklınızdan bile geçirmemelisiniz.

- Eğer UNIX bilgisayarını bir terminalden kullanıyorsanız, terminalinizi açıp kapatmayı bir denemenizde sistem açısından herhangi bir tehlike yoktur.
- Eğer bilgisayarı sistem konsolundan kullanıyorsanız (iş istasyonlarında olduğu gibi) ekranı kapatıp açmak bir yarar sağlamaz. Bilgisayarı kapatmayı düşünmemelisiniz dahi.. Peki ne yapılmalı?

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 139

- İlk denemeniz gereken Ctrl-Q tuşu. Daha önce yanlışlıkla Ctrl-S tuşuna basmış olabilirsiniz. Ctrl-S tuşu, ekrana gelen dökümleri durdurmak için kullanılan bir komuttur. (Ctrl-Q ise ‘devam et’ ‘devam et’ ‘devam et’ ‘devam et’ anlamındadır). (XON/XOFF XON/XOFF XON/XOFF XON/XOFF seri haberleşme protokolu).
- Olmazsa Ctrl-C tuşu ile çalışan işi kesmeyi deneyin. Gene olmuyorsa Ctrl-Z tuşuyla çalışan işi askıya almayı denemelisiniz.

sistem hazır

sistem hazır

sistem hazır

Her iki durumda da denemeniz başarılıysa ekranınızda sistem hazır

işaretini (prompt) göreceksiniz.

işaretini (prompt) göreceksiniz. Hemen ps ps ps ps komutuyla çalışan

işaretini (prompt) göreceksiniz.

işaretini (prompt) göreceksiniz.

işlerin bir listesini alın. Sorun yaratan sürecin numarasını (PID) öğrenip onu öldürmeyi deneyin. Ölmüyorsa çok ısrar etmeyin.

Gerek duyarsanız, sistem yöneticisinden yardım isteyin.

- Eğer klavyeniz kilitlenmişse; sisteme bir başka terminal veya varsa, bilgisayar ağındaki bir başka bilgisayar üzerinden login login login login etmeyi deneyin (telnet telnet telnet telnet veya rlogin rlogin rlogin rlogin komutları). Bunu başarabiliyorsanız hemen ps ps ps ps komutuyla çalışan işlerin bir listesini alın. Sorun yaratan sürecin numarasını (PID) öğrenip onu öldürmeyi deneyin. Ölmüyorsa çok ısrar etmeyin. Gerek duyarsanız sistem yöneticisinden yardım isteyin.
- Hiç bir çareniz kalmadıysa en az 5 dakika bilgisayara dokunmadan bekleyin (eğer çalışıyorsa update update update update daemon’u tampon belleği boşaltsın diye) sonra bilgisayarı kapatın. Tüm bilgisayarlarda olduğu gibi en az 30 saniye kadar bekleyip tekrar açın. Bu tip Bu tip Bu tip Bu tip

zoraki işlemlerden sonra disk kayıtlarınızda büyük çaplı kayıplara

zoraki işlemlerden sonra disk kayıtlarınızda büyük çaplı kayıplara

zoraki işlemlerden sonra disk kayıtlarınızda büyük çaplı kayıplara

zoraki işlemlerden sonra disk kayıtlarınızda büyük çaplı kayıplara

hazırlıklı olmalısınız.

hazırlıklı olmalısınız.

hazırlıklı olmalısınız.

hazırlıklı olmalısınız.

% nohup % nohup % nohup % nohup no hangup

Bir UNIX bilgisayarına ulaşmak için kullandığınız terminali ya da terminal gibi davranan bir PC’yi (Terminal Emulation yazılımı çalışan bir PC) kapatırsanız veya logout logout logout logout komutu ile sistem bağlantınızı keserseniz, o terminal bağlantısıyla ilgili tüm süreçler (hem ön, hem arka plandaki süreçler) UNIX tarafından öldürülür.

Ender de olsa, bazı durumlarda sistemden çıkmanıza rağmen, başlatmış olduğunuz bir işin kesilmeden devam ettirilmesini isteyebilirsiniz. Örneğin, Internet Internet Internet Internet üzerinden çok uzun bir dosya çekiyor ve bu kopyalama işinin siz eve gittiğinizde de devam etmesini istiyor olabilirsiniz. Böyle bir durumda ilk akla gelen ‘’logout ’logout ’logout ’logout etmeden’’ terminali açık bırakarak eve gitme çözümü pek iyi bir çözüm değildir. Sizin yokluğunuzda, açık bırakmış olduğunuz terminalin başına oturan birisi, sizin kimliğinizle hoşlanmayacağınız işler yapabilir.

Kim Korkar UNIX’ten? - Can Uğur Ayfer - PUSULA YAYINCILIK 140

İşte böyle durumlarda nohup nohup nohup nohup komutu kullanılır. logout logout logout logout ettiğinizde kesilmesini istemediğiniz bir programı başlatırken kullanmanız gereken komut satırı

% nohup komut \[varsa parametreleri\] & % nohup komut \[varsa parametreleri\] & % nohup komut \[varsa parametreleri\] & % nohup komut \[varsa parametreleri\] &

olmalıdır.

% tcsh % tcsh % tcsh % tcsh t c-shell

tcsh tcsh tcsh tcsh, csh csh csh csh’e göre oldukça üstün özelllikleri olan bir kabuk programıdır; ancak, şimdilik hiç bir UNIX uyarlamasında standart olarak bulunmamaktadır. Sistem yöneticinize bir danışınız; eğer sisteminizde varsa, sizin için login login login login kabuğu olarak tcsh tcsh tcsh tcsh çalıştırılmasını sağlamasını isteyiniz. (Sistem yöneticileri; kola, kahve, piza gibi rüşvetleri kabul ederler. Para falan teklif etmeyiniz. Paranın ne olduğunu bilseler, UNIX sistem yöneticisi olmazlardı...) tcsh tcsh tcsh tcsh’in belki de en iyi iki özelliği, aynı MS-DOS’daki DOSKEY yardımıyla olduğu gibi, yukarı aşağı tuşlarla eski komutlar arasında dolaşmanızı sağlaması ve dosya adlarının tamamını yazmadan komut yazmanıza olanak sağlamasıdır. tcsh tcsh tcsh tcsh hakkında daha fazla reklama gerek yok. Sisteminizde varsa nasıl olsa öğrenirsiniz; yoksa, zaten özelliklerini öğrenip gıpta etmenin bir anlamı yok.

‘’tcsh ‘’tcsh ‘’tcsh ‘’tcsh’i nereden bulurum ?’’ diyenlere ise cevabım ‘’Internet‘den’’ ‘’Internet‘den’’ ‘’Internet‘den’’ ‘’Internet‘den’’ olacaktır. Birçok üniversitenin bilgisayarında, herkese açık alanlarda tcsh tcsh tcsh tcsh ve daha bir sürü ilginç program bulabilirsiniz. ’’Internet’de neyin nesi ?’’ . ’’Internet’de neyin nesi ?’’ . ’’Internet’de neyin nesi ?’’ . ’’Internet’de neyin nesi ?’’ diyorsanız, bu kitabı okumakla daha fazla vakit kaybetmemenizi öneririm.

---
*Kaynak: `KİM KORKAR UNİX TEN/94-140.pdf`*
