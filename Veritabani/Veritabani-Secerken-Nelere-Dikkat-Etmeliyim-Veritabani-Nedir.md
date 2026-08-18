# Veritabani Seçerken Nelere Dikkat Etmeliyim Veritabani Nedir

Veritabanı seçerken nelere dikkat etmeliyim? Veritabanı nedir? Desktop database - Server database, esneklik,Güclü performans, Ölceklenebilirlik (Scalability), Özel bilgi/egitim gereklidir, pahalılık, zor kullanım gibi bazı kriterler.

**Database Secimi******

Öncelikle konuya tamamen yeni olanlara yönelik olarak „Database“ nedir sorusunun cevabini verelim:

Database (türkcesi Veritabani ama bundan böyle Database kelimesini kullanacagim):

Database, icerigi kolaylikla erisilebilir, yönetilebilir ve güncellenebilir sekilde düzenlenen bir data toplulugudur.En cok taninan Database tipi ise birkac farkli yoldan yeniden düzenlenebilen ve erisilebilen data olan „relational Databse“ yani Iliskisel Database’dir.

Burada karsimiza günümüzde cok kullanilan ve aslinda Database denilince aslinda „Relational Database“ kastedilen bir terim ortaya cikmaktadir :

Iliskisel bir Database, database tablolarini yeniden düzenlemeden birkac farkli yoldan erisilebilen ya da yeniden derlenen datayi teskil eden düzenli-tanimli tablolardan olusan bir data toplulugudur.Iliksisel Database 1970 yilinda E.F:Codd tarafindan gelistirilmistir.

Iliskisel Database’e olan standart kullanici ve uygulama programi arabirimi „Structured Query Language“ (Yapisal Sorgulama Dili, kisaca SQL).SQL ifadeleri hem interaktif sorgular (query) icin hem de raporlar icin data elde etmek icin kullanilir.

Buraya kadar kafalarda olusan mantiksal ve fiziksel kavramlari örneklerle aciklamaya calisalim :

Database tablolardan (table) olusur.Tablolar ise alanlardan (column) olusur.Temelde string ve sayi olma üzere degisik alan tipleri vardir.Bir Database’de birden fazla tablo olabildigi gibi bir tablonun da birden fazla alani olabilir.Bir sistemde ayni isimde bir Database, o Database’de ayni isimde bir tablo ve o tabloda ayni isimde bir alan olabilir.

Bu kavramlar asagidaki sekil üzerinde daha anlasilir olacaktir :

## **Desktop Database – Server Database******

Aslinda Database’leri genel olarak iki kisma ayirabiliriz.Birincisi „Desktop Database“ ve ikincisi „Server Database“.Desktop Database’lere örnek :

• Microsoft Access

• FoxPro

• FileMaker Pro

• Paradox

Desktop Database’lerin avantajlari :

• Desktop database’ler pahali degildirler

• Desktop database’ler kullanici dostudur (user-freindly).

• Desktop database‘ler web cözümlerini destekler.

Bunlari söyledikten sonra, „Server Database“ leri „kim kullanir ki o zaman?“ sorusuna Desktop Database’lerin dezavantajlarini siralayarak cevap verelim :

• **Desktop Database’ler genelde bir kullanici desteklerler.**Düreticilerin demeclerine ragmen genelde desktop databaseler ayni anda sadece bir kisinin database’i degistirmesine izin verirler.Cok kullanicili bir ortamda desktop Database’i kullanmak cok kötü sonuclar dogurabilir.Genel olarak söylenen eger Database’i birden fazla kisi kullanacaksa „Server Database“ kullanilmasi tercih edilmelidir.

• **Desktop Database’lerin güvenligi zayiftir.** Cogu desktop Database‘i basit bir sifre mekanizmasina sahiptir.Eger güvenlik ve log tutma özelliklerini istiyorsaniz kesinlikle „Server Database“ kullanmalisiniz.

• **Desktop databases are not designed for the Internet.** Eger basit olarak datanizi internete acmak istiyorsaniz bir desktop Database’i yeterli gelebilir.Fakat, internet kullanicilarinin datayi degistirebildigi ve yeni datanin girebildigi interaktif bir sistem olusturmak istiyorsaniz server tabanli bir Database kullanmaniz gerekmektedir.

Server Database’ler ise gercekten daha büyük imkanlar sunmaktadir.Baslica dünyada en cok kullanilan ve tanilan Server Database’ler sunlardir :

• Oracle

• Informix

• MS-SQLServer

• Sybase

• DB2

• MySQL

• Postgresql

Server Database’lerin genel olarak avantajlari ya da sagladiklari yararlar sunlardir :

• **Esneklik.** Desktop kuzenlerinin tam tersine, server tabali database’ler onlara yüklediginiz her data yönetim probleminin üstesinden gelebilirler.Programcilar cok severler cünkü Database merkezli özel uygulamalarin hizli gelisimini saglayan programci-dostu uygulama programci arabirimleri (Application Programmer Interface, yani API) vardir.Hatta Oracle, Informix, Sybase, DB2 gibi Database‘ler farkli platformlari (Isletim Sistemleri) destekjlemektedir.

• **Güclü performans.** Server tabanli Database’leristediginiz kadar güclü olabilirler.Önemli Database’ler sizin kurabileceginiz cok uygun donanimlarda cok verimli bir sekilde calisacaktir.Modern Database’ler birden fazla yüksek hizli islemcilerle, cluster sunucularla, yüksek bandgenisligine sahip aglarla ve hata toleransli depolama teknolojisiyle (fault tolerant storage technology )calisabilirler.

• **Ölceklenebilirlik (Scalability)**. Bu özellik öncekiyle cok yakindir.istenildigi sekilde gerekli donanimlari artirarak gerekli kullanici sayisi veya disk alani genisletilebilir.

Tabi hersey bir anda tozpembe degil, Server Database’lerin de dezavantajlari vardir :

• **Özel bilgi/egitim gereklidir.** Server tabanli Database’ler tabii ki oturdunuz yerden ögrenilecek birsey degildir.Donanim ve yazilima yatirima baslamadan önce gerekli özel egitimi almaniz tavsiye edilir.Bu egitim bu önemli yatirimda ihtiyaclari ortaya koyamada faydali olacaktir ve gerekli altyapiyla etkili bir büyüme ve gerceklestirme stratejisi saglayacaktir.

• **Pahalidir.** Server tabanli Database’le saglanan yararlar tabii ki size maddi maliyeti vardir.Öncelikle bircok Database’in bagli oldugu pahali yüksek performansli sistemleri satin almak icin önemli bir doananim yatirimi yapmaniz gerekecektir.Daha sonra , basit tek islemicili bir sistem icin 3000$ ile 15000$ arasinda lisans parasi ödemeye hazir olmaniz gerekir.

• **Son kullanicilar icin zordur.** Genel olarak , satin almadiginiz müddetce son kullanicilariniz kullanici dostu arabirimlere sahip olmayacaktir ve kullanicilariniz SQL ögrenmesi icin tabii ki sabir göstermeniz gerekir.Desktop Database’ler genelde server tabanli Database’ler icin iyi birer arabirimdir.Örnek olarak , bircok organizasyon server tabali Database’lere ulasmak icin bilinen kullanici dostu arabirim olan Microsoft Access’i kullanmaktadir.** ******

Simdi asil konumuza gelelim ve Database secerken gözönünde bulundurmamiz gereken noktalara deginelim. Diyelim ki siz bir Uygulama gelistireceksiniz , bu bir web uygulamasi, ögrenci isleri programi, taksitli satis programi ya da su faturasi tahsilat programi olabilir.Herseyden önce ihtiyaclarinizi ortaya koymaniz gerekir.Bu aslinda en zor olan kisimdir.Cünkü teorik olarak ihtiyaclarinizi belirledikten sonra bir de pratikte ortaya cikan ihtiyaclar bazen sizi zor durumda birakabilir.Bunun icin „en kötü durumda“ faktörü ve data’nin ve sistemin (kullanici acisindan) büyüme faktörü gözönünde buludurulmalidir.

Konuyu daha fazla uzatmadan bir Database’e karar verebilmek icin gerekli olan sorular genel olarak sunlardir :

• Hangi platformlari (isletim Sistemlerini) destekliyor?

• Destekledigi arabirimler neler (odbc, jdbc, DBD, native)?

• Database ne derecede güvenli?

• Backup/Restore (Yedekleme/Yedek Dönme) imkani sunuyor mu?

• Lisans Stratejisi nedir?

• Warm Backup özelligi var mi?

• Transaction Destegi var mi?

• Trigger destegi var mi?

• Support (Destek)‘u var mi ve ne kadar güvenilebilir?

• Administration (Yönetim ve bakimi) kolay mi?

• Mirroring destegi var mi?

• Replication özelligi var mi?

• Parallel Server (Clustering) özelligi var mi?

• Lojiksel olarak limitleri nelerdir?

Bu sorulari cogaltmak tabii ki mümkün.

Bu sorularin detaylarina girmek sanirim yazinin genel amacina uygun olacaktir.

## **Hangi platformlari (isletim Sistemlerini) destekliyor?******

Aslinda öncelikle Database’imizi hangi Isletim Sistemi üzerinde calistirmak istedigimiz önemli.Diyelim ki Database Server’in Linux üzerinde calismasini istiyorsak ve bu tek secenegimiz ise, otomatik olarak MS-SQL Server’i elemis oluyoruz cünkü MS-Sqlserver sadece Windows platformunu desteklemektedir.Ayrica bazi Database’lerin belirli Isletim Sistemlerini desteklemedigini göz önünde bulundurmak gerekir.En cok kullanilan Isletim Sistemleri : HP-UX, AIX, Linux, Solaris, Windows NT, Windows 2000, Windows XP, Digital UNIX, Open BSD, FreeBSD vs.

## **Destekledigi arabirimler neler (odbc, jdbc, DBD, native)?******

Uygulamamizla dogrudan alakali olan bir nokta, cünkü kullandigimiz programlama dilinin destekledigi baglanti türlerini Database’imizin de desteklemesi gerekir.Örnegin bir Database’in ODBC sürücüsü yoksa o Database’le Herhangi bir Visual Basic-ODBC tabanli bir program yazamayiz.

Örnegin perl ile bir program yazacaksak mutlaka o Database’in DBD sürücülerinin üretici tarafindan saglanmasi gerekmektedir.Ayni sekilde java uygulamalari icin de bu durum gecerlidir.

## **Database’in güvenlik stratejileri?******

Düsünün ki bir bankacilik uygulamasi gelistiriyorsunuz , bu durumda Database’de tutulacak bilgilerin güvenligi ve gizliligi sizin icin cok önemlidir.Fakat bir web uygulamasinda cok da önemli olmayabilir.

Burada dikkat etmemiz gereken diger bir özellik ise Database’in kendi icinde saglamis oldugu güvenlik stratejisidir.Mesela tablo bazinda belirli kisilere yetkilendirme yapilabiliyor mu?

Buna informix’ten bir örnek verecek olursak :

grant select,update on table fatura to mehmet; mehmet kullanicisina fatura tablosu üzerinde select (okuma) ve update (kayit degistirme) yetkisi vermektedir.

Mesela Oracle’da yeni cikan bir özellik ise column (alan) bazinda belirli kullanicilara yetkiler verilebiliyor.

## **Backup/Restore (Yedekleme/Yedek Dönme) imkani sunuyor mu?******

Cok önemli uygulamalarda yedek alma islemi cok önemlidir ve de online yani Database aktifken yapilabiliyor olmasi gerekir.Düsünün bir fabrikada 7/24 saat üretim yapiliyor ve database’in her an Online olmasi gerekiyor.Bu durumda sececeginiz Database‘in online backup alma özelligi mutlaka olmasi gerekir (warm backup).Diyelim ki Database online iken backup ya da dump özelligi var, peki alinan yedegin data tutarliligi bu durumda var mi?

Düsünün ki yedek basladiginda bir memur fatura tahsilati yapiyor ve islemin yarisindayken (yani bilgilerin bir kismi Database’e kaydedilmis durumda) yedek bitiyor.Herhangi bir crash (Sistemin ya da Database’in hata verip datalarin bozulmasi) durumunda o yedegi restore (yedegi dönme) ettik, bu durumda datalar tutarsiz olacaktir.

Diger önemli bir nokta ise aldiginiz backup’tan sadece bir tablo restore edilebiliyor mu?Bu durum da cok karsilasilan bir durumdur, mesela birisi sql le calisirken yanlislikla bir tablonun tamamini ya da belli bir kismini sildiginde tek care yedekten geri dönmektir.

## **Lisans Stratejisi nedir?******

Öncelikle open source olan Database’lerin ücretsiz oldugu herkes tarafindan bilinmektedir.Diger ücretli olan (commercial) Database’lerde ise herbirinin degisik lisans stratejileri vardir.Örnegin concurrent (ayni andaki kullanici sayisi) lisansi ya da named (yani toplam kullanici sayisi) lisanslar mevcuttur.Bir de cpu sayisina bagli olanlar da var.

Ortalama olarak her 6 ayda bir yeni sürüm ciktigini kabul edersek, versiyon güncellemelerinin ücretli olup olmadigi ve de güncellemenin ne kadar sürdügü de büyük önem kazanmaktadir.

## **Transaction Destegi var mi?******

Transaction, Database anlaminda begin ile commit arasinda yapilan islemin tamamina transaction denir.Transaction destegi temel olarak verilerin bütünlügü ve tutarliligi icin önemlidir.

Diyelim ki bir internet kullanicisi bir alisveris sitesinde ürünleri gezmektedir ve belirli ürünleri sepete eklemekte ya da sepetten cikarmaktadir.Zamanla bu bilgilerin bir kismi tablolara yazilmis olabilir.Diyelim ki kullanici alisverisi sonlandirmak icin devam etti ve kredi karti bilgilerini girdigi yerde alisveristen vazgecti ve baglantisini kopardi, iste bu durumda o ana kadar yaptigi bütün data hareketlerinin geri döndürülmesi (rollback) gerekir, bu da transaction destegi ile mümkündür.

Diger bir örnek de mesela Database’imiz aktifken birden elektrikler kesildi ve Server’i yeniden baslattik ve Database’i start ettik.Kesinti aninda yarim kalan bütün islemler o sekilde birakilmaz tabii ki, yarim kalan (Database dilinde commit olmamis ) bütün transaction’lar rollback edilir.Bu sekilde Database tutarli bir duruma geri döndürülmüs olur.

Transaction’in cok önemli olmasi sebebiyle artik cogu Database’in bu destegi vardir.Ancak cok kritik uygulamalarinizda bu konunun daha detayina inerek Database’i incelemekte fayda var.

## **Trigger destegi var mi?******

Trigger, bir Database’de belirli bir tablodaki bir satir degismesi gibi belirli bir islem gerceklestiginde otomatik olarak bir islemi baslatan bir dizi SQl ifadesidir.Bir trigger bir olaydan (insert, delete ya da update ifadelerin belirtilen tabloda olusmasi) ve bir hareketten (ilgili prosedür) olusur.Trigger’lar degisen ya da eklenilen bir datanin tutarliligi icin kullanilir.Mesela basit olarak sirket tablosuna yeni bir kayit eklendiginde (insert) git log tablosuna sirket nosunu ve o anki tarih ve zamani kaydet (insert).

## **Support (Destek)‘u var mi ve maliyeti nedir?******

Gelistirdiginiz uygulamalariniz ne kadar kaliteli olursa olsun, kullandiginiz Database’in destegi yoksa ya da cok zayifsa bu pek iyi bir durum degildir.Örnegin uygulamanizin cok spesifik bir ayrintisinda eger Database’de bir bug ortaya ciktiysa ve siz yeni bir versiyon ya da gecici bir cözüm bulamiyorsaniz sistem kullanilamaz haldedir ve proje „basarisizdir“!!

Oracle’dan bir örnek vereyim , 1 yillik destek anlasmasi lisans ücretinin %20 sidir ve genelde Database’inizin down oldugu durumlarda birkac saat icinde bir cozüm sunarlar.Informix’te de bu durum asagi yukari aynidir.

Postgresql ve MYSQL’de ise commercial support veren kurumlar disinda newsgroup’lara baglisiniz ve cogunlukla soru ya da sorunlariniza cok hizli cevaplar alabilirsiniz, fakat hicbir zaman size garanti yoktur.Sanssiz bir sekilde bir bug ortaya cikmis ise bir sonraki versiyonu beklemeniz gerekir ya da o bug’in olmadigi bir diger versiyona gecmeniz gerekir ki bu da zaman ve ugrasi demektir.

## **Administration (Yönetim ve bakimi) kolay mi?******

Aslinda en iyi Database bir anlamda isteklerinize %100 cevap veren ama ayni zamanda administration yani yönetimi ya da bakimi olan Database’dir.

Diger önemli bir nokta ise yönetimi ve bakimi icin gerekli altyapi ve egitim ve bütün bunlarin maliyetidir.Örnegin Oracle’in yönetimi belki de en zor olanidir , bu sebepten dolayi da egitimleri cok pahali ve de fazladir.

Informix’in administation’u ise daha kolaydir fakat görsel yönetim programlari o kadar iyi degildir.Postgresql ve MySql’in ise dökümanlari bol olmasina ragmen egitimleri cok fazla yaygin degildir.Görsel yönetim programlari da her ikisi icin de mevcuttur.Örnegin MySQL icin MySQL Control Center ve Postgresql icin pgadmin, tora gibi.

## **Mirroring destegi var mi?******

Mirroring aynalama demektir ve güvenlik stratejisinin bir parcasi olabilir.Database’in mirror destegi olmasi bir avantajdir ve datalarinizin Disk üzerinde 2 kez kaydedilmesi demektir ve birisinin bozulmasi halinde diger kopyasindan online devam edebilmektedir.Güvenligin yani sira performans acisindan da faydalidir, cünkü bir read (okuma) isleminde paralel yani her iki kopaydan ayni anda okuyabilmektedir , bu da hiz demektir.

Bildigim kadariyla Postgresql ve MySQL’de mirroring özelligi kendi bünyesinde yoktur..

## **Replication özelligi var mi?******

Replication , Database server bazinda kopyalama demektir.Örnegin 1000 tane subesi olan bir banka düsünün ve her subede 50 kullanici olsa toplam 50000 kullanici demektir ve ayni saatler icerisinde sadece bir Server‘a erismeleri biraz garip olurdu sanirim (böyle bir durumu düsünemiyorum bilen varsa lütfen mail atsin).Bunun icin en azindan birden fazla Database farkli yerlerde fakat merkezi bir Database’de olusan bir degisim diger bütün databaselere zamanla iletilir.

Bir hesaba bütün diger subelerden erisilebildigine göre Database’deki kayitlarin bir kere ayni olmasi gerekmektedir.Bu durumda farkli sehirlerde replike edilen birden fazla server dusunursek ve her birinin üzerinde bir Database calisirsa ve bütün bunlar replike edilirse yükler dagilmis ve performans artmis olur.Özet olarak bir Database’in replike edilmesi demek o Database’deki degisiklikler birebir diger Database’lere aktarilmasi demektir.

Replication’un sagladigi bir avantaj da bir Database’in ariza görmesi halinde (down) diger Database’in durumu idare edebilmesidir.

## **Parallel Server (Clustering) özelligi var mi?******

Bu özellik daha cok büyük Database’ler icin gecerlidir.Bir Server düsünün o anki teknolojiyle donanim olarak maximum seviyede donatilmis fakat toplam kullanici sayisini kaldiramiyor, ya da basit olarak bir Database’i 2 server üzerinde calistirmak istiyorum ya da bir Database’de bir ariza olustugunda otomatik olarak diger Database durumu idare etsin istiyorsam Database’in Parallel Server özelligi olmasi gerekir.

Oracle, Informix , DB2 ve MS-Sqlserver in parallel özellikleri var fakat normal Database lisansindan ayri bir fiyatla satilmaktadir.Postgresql ve MySql in ise böyle bir özelligi yoktur.

## **Lojiksel olarak limitleri nelerdir?******

Her Database’in kendi mimarisi vardir ve buna bagli olarak da bazen teorik de olsa limitleri vardir.Bir tablodaki column (alan) sayisi, bir tablonun maximum alacagi satir sayisi, bir Database’in maximum kullanabildigi alan, bir alanin maximum büyüklügü gibi faktörler büyük Database (>100Gb)’ler icin önemlidir.

Simdi birkac Database’in limitlerini vermeye calisalim:

## PostgreSQL

Asagidaki bilgiler aynen http://www.ca.postgresql.org/users-lounge/limitations.html adresinden alinmistir.

Bir Database’in maximum büyüklügü sinirsiz(60GB databaseler mevcut)

Bir tablonun maximum büyüklügü 64 TB bütün Isletim Sistemlerinde

Bir satirin maximum büyüklügü sinirsiz 7.1 ve sonrasi versiyonlarda

Bir alan icin maximum büyüklük 1GB 7.1 ve sonrasi versiyonlarda

Bir tablodaki maximum satir sayisi sinirsiz

Bir tablodaki maximum alan sayisi 1600

Bir tablodaki maximum index sayisi sinirsiz

Tabii ki bunlar sinirsiz degildirler, fakat eldeki disk alanina ve hafiza/swap alanina bagimlidir.Bu degerler normalin disinda büyük olursa performans sorunu yasanabilir.

## Oracle

Bir tablodaki maxiumum index sayisi sinirsiz

Maximum icice altsorgu (nested queries) sayisi 255

Maximum Database user’i 65525

Bir tablodaki maximum alan sayisi 1000

Bir tablodaki maximum satir sayisi sinirsiz

Maximum Tablespace sayisi 64K

Maximum block sayisi 16Kb

Kaynak : http://download-uk.oracle.com/docs/html/A97297\_01/ch1\_admin.htm#i92495

## Informix

Maximum Database büyüklügü 2 Terabyte

Maximum alan sayisi 32000

Maximum tablo sayisi 2^31-1

## MySQL

http://www.mysql.com/doc/en/Features.html :

Büyük Database’ler olusturmak mümkündür.50 milyon kayit iceren bazi Database’ler kullaniyoruz ve 60000 tablo ve yaklasik 5 milyar satir sayisi olan kullanicilar biliyoruz.Bir tabloda maxiumum 32 index kullanilabilir.Her bir index 1 ile 16 arasinda alandan olusabilir.Maximum index genisligi ise 500 byte’dir(bu MySQL Server’i derlemekle degistirilebilir).Bir indexi CHAR ya da VARCHAR olarak kullanabilirsiniz.

Maxiumum tablo büyüklügü 4Gb (3.22) 3.23 versiyonuyla birlikte myIsam tablo tipinde 8 milyon Tb yani 2^63 büyüklügünde bir tablo mümkündür.

Maximum alan büyüklügü 4Gb (long text ya da long blob)

---
*Kaynak: `VERİTABANI SEÇERKEN NELERE DİKKAT ETMELİYİM VERİTABANI NEDİR/O_d_e_v_18539.doc` — ekim kaya — 2003*
