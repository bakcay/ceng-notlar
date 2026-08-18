# Windows NT Güvenliği

***İÇİNDEKİLER:***

***. *** ****** WİNDOWS NT GÜVENLİĞİ*** 1*********

**** YEREL KAYNAKLARIN KORUNMASI:** 2******

**** NTFS GÜVENLİK SİSTEMİ:** 2******

**** İzinler/işlemler** 3******

**** SAHİPLİK :** 3******

**** BİR DİZİNİ PAYLAŞTIRMA:** 3******

**** YÖNETİMSEL PAYLAŞIMLAR:** 4******

**** KULLANICI VE GRUP İZİNLERİ:** 4******

**** DENETİM (AUDITING ):** 4******

**** NT SERVER’DA VERİLERİN KORUNMASI:** 4******

**** SEKTÖRLERİN İDARESİ:** 4******

. ****** LINUX İŞLETİM SİSTEMİNDE GÜVENLİK*** 4*********

**** 1.KONSOL GÜVENLİĞİ:** 4******

**** 2. DOSYA GÜVENLİĞİ** 4******

**** 3.KULLANILMAYAN AÇIK PORTLARIN KAPATILMASI** 4******

**** 4.UZAKTAN ERİŞİMİ KAPATMAK ve GÜVENLİ KABUK SSH** 4******

KAYIT TUTULMASI 4

****** UNİX İŞLETİM SİSTEMİNDE GÜVENLİK*** 4*********

****** OS/2 WARP GÜVENLİK SEVİYESİ VE DESTEĞİ*** 4*********

**** Config.Sys Kütüğünün Kurtarılması** 4******

**** Kullanıcı INI Kütüğünün Kurtarılması** 4******

**** Bellek Durum Verisinin Kurtarılması** 4******

**WİNDOWS NT GÜVENLİĞİ******

**YEREL KAYNAKLARIN KORUNMASI: **

NT işletim sistemi düzenlediği sabit disk, sürücü, ve diğer birimlerin korunması için değişik güvenlik yöntemlerine sabittir. **NTFS **(NT File Sistem ) dosya sistemi, dosya ve dizilere kullanıcı bazında izinler verilerek NT sisteminin ana izin sistemini oluşturur. NTFS birimleri,dosyalara ve dizinlere erişim kontrol listesi (Access Control List-ACLs) uygulayabilir. Bu kontroller paylaşılmış dizinlerdeki izinlerle bağlantılı olarak görev yapıyorlar. Bir dosya yerleşim tablosu (File Alloction Table –FAT) birimi yalnızca son kısımları destekliyor ( güvenliğin paylaşım düzey şekli ). Emniyet açısından durum müsaitse çoklu korumaları kullanmak her zaman faydalıdır. Bu yüzden internet bağlantılı Windows NT makinelerde genelde NTFS kullanmak gereklidir.

Yerel (Lokal ) bilgisayarın sabit diski ve diğer birimlerinin korunmasının yanı sıra network üzerinden sisteme erişecek kullanıcıların da kontrol edilmesi NT koruma sisteminin bir bölümünü oluşturur. NT işletim sistemi bu işlemler için çok sayıda araca sahiptir:

**Yönetim Araçları:**

NT Explorer

My Computer

Server Maneger

Command Prompt ( komut yolu)

NT kaynaklarına başvuran biri için tesis edilen kontrol üç ayrı düzeyde düzenlenir:

Share-Level (paylaşım düzeyi )

Directory -level (dizin düzeyi )

File-level (dosya düzeni )

Paylaşım düzeyi paylaştırma uzak kullanıcılar için yapılır. Diğer paylaşım düzenlemeleri yerel kullanıcı içindir.

**Bir Uyarı: ** Eğer NTFS ACLs bir ağ kullanıcısına partition kısmı için tam ulaşım verir fakat paylaşım düzeyinde salt okunur erişim verilirse, etkili olan erişim yalnız okunurdur. Windows NT, NTFS ACLs ve paylaşım yetkilerinin arakesitini alıyor.

Peki umumi bir makinede paylaşımların bulunmasına izin verilmeli mi? Teorik olarak hayır. Pratikte ise, hizmet biriminizden dosyaları taşımanız için bazı yollara başvurmak gerekiyor. NTFS düzey güvenliği bu uygulamayı daha tehlikesizce gerçekleştirmeye yardımcı olabilir. Yeni paylaşımlar oluşturursak, NT tarafından koyulmuş varsayılan yetkileri değiştirmeye dikkat edin. Bunu yapmayı unutursak “Everyone” isimli grup paylaşım arasında gözükebilenlerin tümünün tam kontrolüne sahip olacaktır. Bu mesele NT’nin güvenlik piyasasında kötü bir darbe almasının sebeplerinden biridir. NT aşırı dikkatli olmaktan ziyade daha dostça konfigürasyon varsayımına yöneliyor. Bu felsefe bir LAN iş grubu için taktir edilebilir,fakat internet hizmet birimi için tam bir felaket.

**NTFS GÜVENLİK SİSTEMİ:******

NTFS bölümü kullanıcılara izin (hak ) vererek sabit diski yerel ve uzak (network ) bağlantılarına karşı korur. Bu nedenle izinleri dosyaların sahip oldukları özellikler olarak düşünmek gerekir. NTFS güvenlik sistemi içinde ayrıca disk üzerinde yapılan işlemler denetlenir (auditing ) ve sahiplikler düzenlenir.

İzinler (permissions ) dosyaların nasıl ve kim tarafından kullanılacağını belirler. NT’de beş temel izin vardır.

**NTFS’de İzinler********İzinler/işlemler**

| **Read** | **Execute** | **Write** | **Delete** | **Set Permission ** | **Take Ownership** |  |
| --- | --- | --- | --- | --- | --- | --- |
| No Access |  |  |  |  |  |  |
| Read | x | x |  |  |  |  |
| Change | x | x | x | x |  |  |
| Full Control | x | x | x | x | x | x |
| Special Access | x | x | x | x | x | x |

**Varsayım İzinler: **bir disk bölümü NTFS ile formatlandığında **Everyone **grubuna Full Control Olarak açılır. Bunun anlamı yeni yaratılan bir NTFS disk bölümünün yerel bir FAT ya da HPFS bölümü gibi kullanılmasıdır.

**SAHİPLİK :**

Bir dosya ya da dizinin sahibi ( owner/yaratan) onun izinlerini değiştirme hakkına sahiptir. Başka bir deyişle sahiplik izni değiştirme hakkıdır. Temelde Adminstrator sahiplikleri düzenler ve istediği sahipliği de elde eder. Bunun dışında bir sahip, kendi izin ya da dosyası üzerinde istediği kullanıcıya istediği hakkı verebilir.

*Sahiplik konusunda genel esaslar şunlardır :*

Yaratıcı (sahip ) kullanıcı başka bir gruba ya da kullanıcıya sahiplik hakkı verebilir.

Adminastrators bir dosya ya da dizinin sahipliğini alabilir.

*Adminastrators *grubundan birisi sahiplik alırsa Adminastrators grubu sahip olur. Buna karşın Adminastrators grubunda olmayan bir kullanıcı sahiplik alırsa o zaman sadece kendisi sahip olur.

Bir dosyanın sahibi olmak ya da *Adminastrator *olmak dosyanın bütün izinlerine sahip anlamına gelmeyebilir. Ancak bir sahip o dosyanın izinlerini değiştirerek istediği izinleri elde eder.

**BİR DİZİNİ PAYLAŞTIRMA: **

Çalışan bir NT Server üzerindeki dosya ve dizinlere izini olmayan kullanıcılar ulaşamazlar. NT Server üzerindeki dosya ve dizinlere ulaşmak için paylaştırılması gerekir. Bir dizini paylaştırmak için ***Adminastrators**** *grubunda ya da ***Server Operators*** grubunda olmak gerekir.

Bir dizin yerel (bulunulan makine) yada uzaktan paylaştırılabilir. Yerel yönetim için **NT Server’a** giriş yapılmalıdır. Uzaktan paylaşım yapmak için **Server Maneger **programı çalıştırılmalıdır. NT’de paylaşımları kısıtlamak mümkündür.

Paylaşıma açılan bir dizine (kaynağa ) bir ad verilir. Bu ad varsayım olarak dizinin adıdır. Bunun dışında kullanıcı istediği bir paylaşım adını dizine verebilir. **Paylaşımları gizlemek için paylaşım adlarının sonuna $ işareti konur.**

Uzaktaki bir bilgisayar üzerindeki paylaşımın yönetimi için** Server Maneger **programı kullanılır.uzaktan paylaşımları gören sistem yöneticisi isterse paylaşımdan yaralanan kullanıcıların paylaşımlarını keser.

**YÖNETİMSEL PAYLAŞIMLAR:**

NT Server ve Workstation işletim sisteminde server servisinin çalışmasıyla birlikte bazı gizli yönetimsel (administrative ) paylaşımlar oluşturulur. Bu paylaşımlar şunlardır:

ADMIN$ (NT programlarının bulunduğu dizin

IPC$ ( SİSTEM İÇİ İLETİŞİM )

C$ (her bir disk partitionu)

D$ “

E$ “

**KULLANICI VE GRUP İZİNLERİ:**

Dizine ve dosyaya diğer bilgisayarlardan (network’ten) erişim için verilen izinlerin yanısıra yerel bilgisayar için (logon )edilen dizinler ve dosyalar üzerinde istenilen dizinler güvenlik amaçlı olarak düzenlenebilir.

**DENETİM (AUDITING ): **

Bir bilgisayar için, dosya ve dizinler üzerinde belli kullanıcı ya da gruplar tarafından yapılacak belli işlemlerin takip edilmesini sağlar. Denetim özellikleri başarılı ya da başarısız olarak yapılan girişimleri (işlemleri )takip etmeyi sağlar. Denetim sadece NTFS dosya sisteminde sağlanır. Denetim düzenlemeleri sadece **Adminastrators **tarafından sağlanır.

**NT SERVER’DA VERİLERİN KORUNMASI: **

NT Server’da verilerin (sabit diskin ) korunması için özel özellikler vardır.sistemlerin çökmesi işletmeleri büyük kayıplara uğratabilir. DFT ( Disk Fault Tolerance/disk hata toleransı , sistem çökmelerine karşı önlem alınmasını ve veri saklama ortamlarının güvenliğini sağlar. Windows NT’de yazılım temelli üç tür hata toleransı sistemi vardır.

Disk mirroring

Disk striping with partys

Sector sparing (sektör idaresi)

Disk hata toleransı sistemleri RAID (Redundant Arrays Of Inexpensive Disks) olarak adlandırılır ve altı düzeye ayrılır. Bu düzeyler farklı bileşimlerde güven,performans ve maliyete sahiptirler.

Veri güvenliğinde diğer bir konu da verilerin yedeklerinin alınmasıdır. Çeşitli risklere karşı yedekleme yapmak gerekir. NT işletim sistemi **Tape Backup **birimi aracılığıyla yedekleme almayı sağlayan bir grafik programa sahiptir. Y eklenen dosyalar aynı bilgisayara ya da başka bir bilgisayara geri yüklenebilir.

**SEKTÖRLERİN İDARESİ: **

RAID sistemi ile getirilen güvenlik yöntemlerinin yanı sıra Windows NT sektörleri koruyarak güvenliği artırır. Disk üzerindeki bütün sektörler formatlanırken hatalı sektörler diğerlerinden ayrılır. Okuma/yazma işlemlerinde karşılaşılan hatalar sonucunda önce kötü sektör saptanır. Ardından bu bilgiler yeni sektöre taşınır. Bu düzenlemenin ardından disk alanı için yeni bir driver map (sürücü hatası )düzenlenir. Bu işlemler disk işlemlerinde bir hata mesajının verilmemesini sağlar.

**SONUÇ OLARAK: **

**Aşağıdaki dört nokta NT’nin en önemli güvenlik konseptleridir. **

Güvenlik sistem girişi : Bir kullanıcı sistemde çalışmadan önce geçerli bir kullanıcı adı ve şifre ile kendini sisteme tanıtmak zorundadır.

Erişim kontrolü :** **Bir kaynağın sahibi ,dosya, bellek alanı veya başka bir nesne olsun, kimin hangi şekilde bu kaynağa erişebileceğini belirler. Objenin sahibi bunun için kullanıcı ve kullanıcı gruplarına erişim hakları verebilir.

Gözetleme fonksiyonları :** **NT güvenlik için önemli olayları belirleyebilir ve bunları bir günlük dosyasında tutabilir. Aynı şey sistem kaynakları oluşturma, bunlara erişme ve silme teşebbüslerinde de geçerlidir.

NT kullanıcı yönetimi sayesinde bu tip bir olayın hangi kullanıcı tarafından gerçekleştiğini tespit edebilir.

Bellek koruması: programlar ayrılmış bellek alanlarında çalışırlar.bu yüzden bir program gerekli yetkiye sahip değilse başka bir programın kullanıldığı belirli** **bellek alanlarına erişemez. NT bu bağlamda bir programın kullandıktan sonra yeniden işletim sistemine ger verdiği belleğin içeriğini siler, böylece başka yazılımlarla bu bellek alnındaki okunması imkansız kılınmış olur.

**LINUX İŞLETİM SİSTEMİNDE GÜVENLİK**

Linux\`un gün geçtikçe yaygınlaşmasının en başta gelen sebeplerinden biri de kararlı ve güvenilir bir işletim sistemi olmasıdır. Bu, bir çok sistem yöneticisinin bilgilerini Linux altında tutması,linux a güvenmesinin yanı sıra sistem kırıcı olarak nitelendirilebilecek \`cracker\`lar içinde bir nevi kendini kanıtlama fırsatı fikrini de beraberinde getirir.

**(Cracker:**Aslında bu terimin iki anlamı var fakat bizim konumuzla ilgili olan anlamı: Sistemlere güvenlik amacıyla konulan şifrelerin çözme tekniklerini iyi bilen,şifre kırıcı olarak ta adlandırabileceğimiz kişilerdir.Kesinlikle sisteme sızdıkları zaman zarar verirler hatta kullanılmaz hale getirebilirler. )

**1.KONSOL GÜVENLİĞİ:**

İç güvenlik olarak ta nitelendirilebilecek konsol güvenliği tamamen kurduğunuz sisteme bağlıdır.Eğer normal bir kullanıcı olarak Linux'u yüklediyseniz bu kısımda anlatılacak önlemlerin hepsini uygulamak zorunda değilsiniz. Fakat bir sistem yöneticisi iseniz biraz daha dikkatli olmanız gerekir. Bu kısımda anlatılanlar bizzat bilgisayarın başında yapabileceğiniz güvenlik önlemleridir.

Linux a sistem yöneticisi (root) olarak girdiyseniz, makinenin başından ayrılırken mutlaka şifreli bir ekran koruyucusu devreye sokun. Aksi halde siz yokken birileri hoş olmayan sürprizlerde bulunabilir. Linux'u konsoldan kullanıyorsanız \`vlock \` komutunu, X-windows altında ise herhangi bir şifreli ekran koruyucuyu çalıştırmanızı tavsiye ederim.

Çok gerekmedikçe sisteminize yeni kullanıcı eklemeyin.

Kullanıcılar için şifre belirledikten sonra kullanıcı bu şifreyle ilk kez sisteme girdiğinde mutlaka şifresini değiştirmesini sağlayın.

Kullanıcı şifrelerinin zayıflığı da çok önemlidir. Cracker'lerin genelde kullandığı şifre kırıcı programlar basit, tek kelimelik şifreleri kısa bir zamanda çözer.Bunun için sizde Cd'de gelen john the cracker programını kullanarak kullanıcılarınızın şifrelerinin ne denli zayıf olduğunu öğrenebilir ve değiştirmeleri için uyarıda bulanabilirsiniz.

Root kullanıcısının şifresini ayda bir mutlaka değiştirin.

Şifre seçerken isim, eşya adı kullanmak yerine iki bağımsız sözcüğü bir rakamla ya da sembolle birleştirmek crackerin işini bir hayli zorlaştırır.Örnek vermek gerekirse; saat5okul ya da kime5$verdin. Bunun gibi şifreleri kullanmak sisteminizi daha güvenli hale getirir. Önemli olan Crackerin şifreyi çözerek sisteme girmesi ihtimalini ortadan kaldırmaktır. Eğer sisteme giriş yaparsa bir de root yetkisini elde etmek için uğraşacaktır. Bunun için ilk güvenlik önlemi olan şifreleme çok önemlidir. Zaten hangi hırsız kapıyı açmadan kasadaki parayı götürebilir ki?

**Şifreler ve Şifre Seçimi:** Çok kullanıcılı işletim sistemlerinde kullanıcının kimliğinin belirlenmesi büyük önem taşır. Hem sistemi kullanmaya yetkisi olmayan kişilerin sisteme girmelerinin engellenmesi, hem de sistemdeki kullanıcıların birbirlerinden ayırt edilebilmeleri için, her kullanıcıya bir şifre verilir ve sisteme giriş başta olmak üzere tüm kritik işlemlerde kullanıcıya şifresi sorulur. Şifreler, diğer kullanıcı bilgileriyle birlikte, ***/etc/passwd*** veya ***/etc/shadow*** dosyasında tutulur.

Bazı uygulamaların şifre dosyasının bazı alanlarına erişmeleri gerektiğinden şifre dosyası, sistemdeki bütün kullanıcılar tarafından okunabilecek bir dosya olmalıdır. Bu nedenle şifreler bu dosyaya açık halde değil, şifrelenerek yazılırlar.

**Gölgeli Şifreler (Shadow Pasword Suite)**

Redhat 6.0 dan önceki tüm linux dağıtımlarında ön tanımlı olarak normal bir şifreleme metodu kullanılıyordu. Bu şifreleme metodu ise şifrelerinizi ayrı bir biçimde tekrar şifreleyerek (crypt) */etc/passwd* altında saklar çünkü bazı programlar bu dosyayı kullanarak çalışır. Kötü yanı ise sistemdeki tüm kullanıcıların yetkisi ne kadar düşük de olsa bu dosyayı okuma hakkı olmasıdır. Her kullanıcının okuma hakkı olduğu zaman bu dosyayı kopyalayarak, içinde bulunan şifrelerin çözülmesi çok kolaydır. Bu sorunu ortadan kaldırmak için sadece sistem yöneticisinin ve gerektiğinde sistemin bu dosyayı okuyabilme hakkı olması gerekliliği ortaya çıkmıştır. Gölge şifreler yani Shadow Password bu fikirden doğmuş bir metottur. Şifreler gene şifrelenerek */etc/shadow* içinde adeta hapsedilir ve */etc/passwd* dosyası altında şifre bırakılmaz. Böylece daha güvenli bir yapı kurmuş olursunuz. Redhat 6.0 bu desteği kurulum aşamasında sizden onay alarak kullanıma açabiliyor. Eğer kurulum sırasında *\`use shadow passwords\`*'u seçmişseniz sorun yok; fakat, \`bu da ne yahu?\` diyerek bu opsiyonu es geçmişseniz çok geç değil.
Komut istemine *"pwconv"* komutunu yazmanızla gölgeli şifreleme yöntemini kullanmanız mümkün. Bu özelliği kaldırmak içinse *\`pwunconv\`* komutunu vermeniz yeterli. Bu komutları aklınızda tutmaktansa RedHat'ın bu avantajından hala faydalanabiliriz. Komut isteminde *\`setup\`* yazarak kurulum ve yönetim programına girip *\`Authentication configuration\`* seçeneğini seçerek karşınıza çıkan menüden \`Use Shadow password’u seçerek de gölgeli şifreleme yöntemine geçebilirsiniz. Bu aşamada gözünüze bir şey daha takılacak *"MD5 passwords"*. **
**

**Nedir bu MD5 şifrelemesi ? **

Linux ta açılan kullanıcılar için verilecek şifrenin uzunluğu en fazla 8 karakter olabilir. Daha uzun yazsanız bile Linux sadece ilk 8 karakteri şifre olarak kabul edecektir.Bu da demek oluyor ki şifre en fazla 8 karakter olabiliyor ve şifrelerimizi çözmek isteyen biri için bu bir başlangıç noktası, ipucu niteliği taşıyor. Bu ipucunu yok etmenin de bir yolu var tabi ki. Çözüm az önce merak ettiğimiz MD5 şifrelemesi. MD5 şifrelemesi sayesinde şifre uzunluğu 8 karakterden 256 karaktere kadar çıkarabiliyor. Bu da crackerin ömrünün bilgisayar başında geçirerek şifreyi kırmaya çalışacağı anlamına geliyor. Sistem şifrelerini korumak amacıyla mutlaka gölgeli şifreleme ve MD5 şifrelemesini Kullanın!!

**
2. ****DOSYA GÜVENLİĞİ**

Her dosyanın bir sahibi, bir de grubu vardır. Dosya üzerinde kimin hangi işlemleri yapabileceğine dosyanın sahibi olan kullanıcı karar verir. Erişim hakları, dosyanın sahibi, grubu ve diğerleri için ayrı ayrı belirtilir.

*-rwxr-x--- 1 uyar users 4030 Dec 4 15:30 dene*

Dizinler için de aynı erişim hakları modeli geçerlidir. Bir dizin üzerindeki okuma izni, dizin altındaki programların listesinin alınıp alınamayacağını, yazma izni dizinde yeni bir dosya yaratılıp yaratılamayacağını, çalıştırma izni de o dizine geçilip geçilemeyeceğini belirler. Yetkili kullanıcının (root) bütün dosyalar ve dizinler üzerinde (birkaç sistem dosyası ve dizini haricinde) bütün işlemleri yapma yetkisi vardır.

**Tehlikeler:** İşletim sisteminde ya da uygulama programlarında bir hata olmadığı sürece erişim izni olmayanlar dosyayı zaten okuyamayacaklardır. Asıl tehlike, yetkili kullanıcının yetkisini kötüye kullanarak kullanıcıların kişisel dosyalarını ve mektuplarını okumasıdır. Her şeye yetkisi olan bir kullanıcı, sistemin kararlılığını korumak için gerekli olmakla birlikte, güvenliği ve özel bilgilerin gizliliğini bir kişinin ahlakına bırakması açısından Linux (ve Unix) işletim sisteminin güvenliğinin en zayıf noktalarından biri olarak değerlendirilmektedir.

Saldırgan, sisteme girince, hem sonraki girişlerini kolaylaştırmak, hem de daha rahat çalışabilmek için bazı sistem dosyalarını ya da programlarını değiştirebilir. Örneğin, şifre dosyasına bir kayıt ekleyerek kendine yetkili bir kullanıcı yaratabilir. Kullanıcıların şifrelerini öğrenmek için login, passwd gibi programları değiştirebilir.

**Önlemler: **Şifre güvenliği sağlandığı sürece dosya erişimlerinde fazla bir güvenlik sorunu olmayacaktır. Bu konuda sistem sorumlusuna düşen, kullanıcılarını erişim haklarını nasıl düzenleyecekleri konusunda bilgilendirmektir.

Şifre dosyası gibi metin dosyalarında değişiklik olup olmadığı gözle inceleme yaparak ya da basit komut satırı programları kullanarak bulunabilir. Çalıştırılabilir dosyalar gözle kontrol edilemeyeceğinden en uygun yöntem, dosya imzaları oluşturarak sağlam olduğu bilinen imzalarla yeni hesaplanan imzaları karşılaştırmaktır. *Tripwire* paketi, dosyalarda yapılan değişiklikleri fark etmekte sistem sorumlusuna ve kullanıcılara yardımcı olur. Önce sağlam olduğu bilinen dosyaların dosya imzaları oluşturularak bir yerde saklanır. Sonraki çalıştırmalarda imzalar yeniden hesaplanarak eskileriyle karşılaştırılır ve farklı olanlar varsa bildirilir. Düzgün çalışma için özgün imzaların iyi korunması, mümkünse, üstüne yazılamayan bir ortamda saklanması gerekir.

**
3.KULLANILMAYAN AÇIK PORTLARIN KAPATILMASI
**

Bilgisayarınızın aslında internete açılmak ve çeşitli internet uygulamalarını (ftp,telnet,irc , .. vs ) çalıştırmak için bu işlemlere karşılık gelen portları kullandığını biliyor muydunuz? Portlar herhangi bir internet uygulamasının haberleşme için kullandığı sanal çıkış noktalarıdır.Her uygulamaya özgü bir port vardır ve diğer hiçbir uygulama başka uygulamaya ait porttan bilgi giriş ve çıkışı yapamaz. Bir an için portların gerçekten bilgisayarın içinde olduğu düşünecek olursak, üzerinde bir çok farklı boyutlarda açılmış delik bulunan bir tabla hayal edelim. Bu delikler portlarımız olsun. Her biri farklı boyutlarda olduğu için birine ait bir çomak diğerine asla tam olarak yerleşemez; ya dar gelir ya da bol.portların mantığı da aynen bu örnekteki gibidir.

Ayrıca sisteminizin verdiği servisler doğrultusunda kullandığı portları dinleyerek açık olup olmadığını tespit eden programlar vardır. Bu programlar sayesinde sisteminiz hakkında bilgi edinen bir hackerin içeri giriş noktalarını kapatmak en akıllıca çözüm olur.
RedHat'ı eğer sunucu olarak kurduysak açılışta , önceden seçilmiş servisleri çalıştırır (web sunucusu, dns sunucusu gibi). Bu sunucularında tabi ki belli portları vardır fakat artık bir sunucunun görevine son vermek istiyorsak bunu nasıl yaparız? Önceki bölümlerde anlatılan \`SETUP\` uygulaması bize yine bu aşamada da yardımcı oluyor. Setup komutunu vererek bu uygulamayı başlatıp "services" seçeneğine girersek bazı servisleri için başlatma/kapatma seçimini rahatlıkla yapabiliriz. Peki telnet ya da ftp servislerini kapatmak için ne yaparız? Linux tüm internet uygulamalarına ait görevi inetd'ye yani internet deamon denilen "internet canavarına" vermiştir. Bu canavar */etc/inetd.conf* adlı konfig dosyasında belirtilen tüm portları dinleyerek, gelen istemlere karşılık gelen servisi yerine getirir. İşte bu konfig dosyasını değiştirerek sürdürülen servisleri kapatmak mümkün. Örnekte bu dosyadan alınan bir kısım görülüyor.

*ftp stream tcp nowait root /usr/sbin/tcpd in.ftpd -l -a

telnet stream tcp nowait root /usr/sbin/tcpd in.telnetd *

Buradan ftp ve telnet hizmetlerinin verildiğini anlıyoruz. Eğer bu hizmetleri kapatmak istersek, istenmeyen hizmetin yazdığı satırın başına \`#\` işaretini koymamız yeterli olur. Bu işaret aslında bu satırın yorum satırı olduğunu belirterek inetd'nin bu işlemleri görmesini engeller.

*#ftp stream tcp nowait root /usr/sbin/tcpd in.ftpd -l -a

#telnet stream tcp nowait root /usr/sbin/tcpd in.telnetd *

Artık size telnet'le ulaşmaya çalışan istemciye bu servisin verilmediği ve bağlantının kesildiği bildirilir. Kullanmadığınız servisleri bu şekilde kapatmanız sizi daha güvenli bir sisteme götürür. Eğer verilen servislerin hangi portlardan gerçekleştiğini görmek ve kapatmak istiyorsanız aynı yöntemle */etc/services* dosyasıyla da oynayabilirsiniz. Kapatılan servislerin tekrar açılması için satır başlarına konan \`#\` işaretlerinin kaldırılması ve inetd'nin kapatılarak tekrar çalıştırılması gerekir. Bunun için yazılacak komut aşağıda belirtilmiştir.

***#killall -HUP inetd***

**4.UZAKTAN ERİŞİMİ KAPATMAK ve GÜVENLİ KABUK SSH
**

Bildiğiniz gibi linux ile beraber gelen telnet desteği oldukça çok kullanılan bir uygulamadır. Telnet sayesinde karşı uzak sisteme eğer kullanıcı hesabınız varsa bağlanıp bu sistemi aynı kendi bilgisayarınız gibi kullanabilirsiniz. Tabi bu erişim biraz daha yavaş bir şekilde gerçekleşecektir. Telnet servisini çalıştırıyorsanız ve kullanıcılarınız varsa aynı mekanizma sizin sisteminiz içinde geçerli olur. Ne yazık ki telnet uygulaması sanıldığı kadar güvenli değildir. Karşılıklı yapılan şifre alışverişlerinde bir şifreleme, gizleme yapılmadığı için bilgiler istenmeyen kişilerin eline geçebilir, ve daha önemlisi hackerların sisteme sızmak için deneyeceği ilk port telnetin portudur. Bunu engellemek ve maksimum derecede güvenli bir bağlantı sağlamak için yeni bir kabuk geliştirilmiştir ve bu kabuğun şu ana kadar bilinen hiç bir açığı yoktur! Bu kabuğun adı SSH yani güvenli kabuk anlamına gelen \`secure shell\` dir. Eğer bu kabuğu kullanacaksanız öncelikle telnet'i bir önceki maddede anlatılan biçimde servis dışı bırakmanız daha doğru olur. SSH i Cd de güvenlik dizini altında bulabilirsiniz. Kurulum ve verimli bir SSH için belirtilen tüm paketlerin kurulması gerekmektedir.

*ssh-1.2.26.-4i.i386.rpm
ssh-clients-1.2.26.-4i.i386.rpm
ssh-server-1.2.26.-4i.i386.rpm
ssh-extras-1.2.26.-4i.i386.rpm
*

Eğer sisteminize bağlanan kullanıcılarınız başka bir işletim sistemini kullanıyorlarsa, bu onların artık bağlanamayacağı anlamına gelmez. Telnet istemcisi gibi bir de SHH istemcisini internetten temin edebilirler. http://hp.vector.co.jp/authors/VA002416/teraterm.html

**5.BELİRLİ IP ADRESLERİNE İZİN VERİLMESİ **

Kullanıcılarınız tarafından herhangi bir makineden Linux\`unuza yapılan bağlantıları denetlemek, gerekli zamanlarda kısıtlamak ve böylece davetsiz misafirleri ileride engellemek amacıyla; /etc dizini altında bulunan iki konfigürasyon dosyası vardır.

*/etc/hosts.deny DOSYASI*

Bu konfig dosyası sayesinde Linux'unuz tarafından verilen servislere alan kısıtlaması getirilebilir. Yani bu servislerin bir ya da birkaçını istediğiniz güvenilir bir ağa ya da bir tek IP adresine izin vererek, bu adresler dışındaki makineler bu servisleri kullanamaz. Adından da anlaşılacağı üzere host.deny(makine.reddi) dosyası kabul etmediğiniz makine ip adreslerini yazabileceğiniz bir dosya. Örnek bir */etc/host.deny* üzerinde yorum yapalım:

*#/etc/hosts.deny
in.telnetd : ALL except localhost
in.ftpd : ALL except localhost

*Burada belirtilen in.telnetd, verilen servisin adıdır. ALL seçeneğini ile tüm uzak erişime bu servis kapatılır; ancak bu servisten bizde mahrum kalırız. Bunun için \`except\` yani hariç parametresinden sonra kendimizi ekleriz ki bu servis bize açık olsun.

*#/etc/hosts.deny ornek 2
in.telnetd : ALL *

Bir önceki örnekten farklı olarak bu örnekte telnet servisi tüm makinelere kapatılmıştır. Bu servisin hizmet vermeyeceği makineler arasında kendi makinemiz de var, farkı yalnızca bu. Size bir başlangıç fikri vermek gerekirse öncelikle /etc/host.deny \`da bütün servisleri dışarıdan erişime kapamanız ve bir sonraki başlıkta incelenecek /etc/host.allow dan istediğiniz belli ip adreslerine ya da ağlara izin vermenizin daha güvenli olacağı doğrultusundadır. Aşağıda belirtilen biçimi host.deny için kullanabilirsiniz.

*#/etc/host.deny ornek 3
ALL : ALL except localhost
/etc/hosts.allow DOSYASI *

Yukarıda anlatılan ve kapatılan bir ya da tüm servisleri /etc/host.allow konfig dosyasını kullanarak belirli ya da güvenli ip adreslerine ya da ağlara açalım.

*#/etc/hosts.allow ornek1
in.telnetd: .gelecek.com.tr
wu.ftpd : 195.34.34.0 *

Az önce hatırlarsanız tüm servisleri host.deny dosyasından kapatmıştık. Ancak bir servis her iki dosyada da geçtiği için Linux direkt olarak host.allow dosyasını göz önünde bulundurur. Bu örnekte de her makineye ve ağa kapalı olan telneti gelecek.com.tr domain ismi altındaki her makineye açık tutuyoruz. Ayrıca kapalı olan ftp servisini 195.34.34.0 olarak tanımlı tüm ağa açmış durumdayız. Buda 195.34.34.1 - 195.34.34.254 arasında bir ip adresine sahip tüm makinelerin bu servisi kullanması anlamını taşır.Bu şekilde servisleri belli bir ağa verebileceğimiz gibi sadece belli bir ip adresine de bu servisleri açabiliriz. Örnek 2'yi inceleyiniz.

*#/etc/hosts.allow ornek2
in.telnetd: 195.56.57.3
wu.ftpd : 195.98.97.9 *

**6.UZAKTAN YAPILAN SALDIRILAR**

İşletim sistemlerine bağlı olarak sistemleri bir müddet için dondurmaya, devre dışı bırakmaya, hatta internetten bağlantısını kopartmaya kadar zarar verici ve uzaktan (remote) yapılabilecek saldırılar son bir kaç yıldır gündemde. Bunlara verilen genel ad \`Denial of Service\` yani service dışı bırakma \`dır. Bunlara örnek olarak teardrop, newtear, nestea, smurf, land, lattierra, ssping verilebilir. Bu saldırıların bir çoğu linux üzerinde etkisizdir. Sadece tear-drop ve yeni versiyonu olan new-tear ile nestea ayrıca broadcast (yayın ) haberleşmesi üzerinde gerçeklenen smurf Linux'u etkileyebiliyordu. Etkileyebiliyordu diyorum çünkü bu saldırılar çıktıktan hemen sonra Linux için bir üst sürüm kernel yazılmış ve bu açık giderilmişti. Kernel\`in 2.0.34 sürümünden beri Linux'a karşı bu saldırılar etkisizdir. Düşünün ki RedHat Linux 6.0 in çekirdeği 2.2.5. Ancak Unix ve unix türevleri dışında diğer işletim sistemlerinin çoğu bu saldırılardan hala etkileniyor. Bu konuda Linux'unuza güveniniz tam olsun! Son zamanlarda iyice "moda" olan DDoS (distrubuted denial of service) saldırıları ise her işletim sistemini etkiler. Ancak sistemi ping e kapatırsanız güvende olma şansınız bire iki oranında artar. Sizin yaşamadığınızı düşünün biri size ateş etmez değil mi?

**KAYIT TUTULMASI **

Güvenliğin en önemli parçalarından biri, sistemin sürekli izlenerek, güvenliğe aykırı durumlar oluşup oluşmadığının, oluştuysa bunların sorumlularının kimler olduğunun belirlenmesidir. Bunun için, güvenliği ilgilendirebilecek her türlü olayın kaydı tutulmalıdır. Şu tip bilgiler, güvenlik açısından değer taşırlar:

Başarısız veya başarılı olmuş sisteme giriş denemeleri

Nerelerden, hangi hizmetler için bağlantı istekleri geldiği

Hizmetler sırasında gerçekleşen dosya aktarımları

Linux'ta kayıt tutulması işini *syslogd* süreci görür. Hangi tür mesajların hangi dosyaya yazılacağı konfigürasyon dosyasında (/etc/syslog.conf) belirtilir. Genellikle makine ilk açıldığı zaman */var/adm/messages* dizini altındaki *messages*, *xferlog*, *syslog* gibi dosyalara yazılan bu bilgileri isteğinize göre daha sistematik bir yapıda saklamak da mümkündür. Ağ ile ilgili hizmetleri denetleyen süreçler (*tcpwrapper*, *xinetd* gibi paketler) kayıt dosyalarına girmesini istedikleri bilgileri syslogd sürecine bildirirler.

**UNİX İŞLETİM SİSTEMİNDE GÜVENLİK**

Güvenlik, UNİX işletim sistemin en kuvvetli aynı zamanda da en zayıf olduğu konulardan birisidir. En kuvvetli çünkü işletim sistemi kendisini ve kullanıcılarının sahip oldukları dosyaları çok iyi bir şekilde koruyabilmektedir. En zayıf çünkü bir kez kötü niyetli birisi root şifresini ele geçirirse sisteminizi çok kolayca mahvedebilir. UNİX altında her türlü erişim, kullanıcı tanıtım kodları ve şifreleri konusunda yeteri kadar hassas davranmıyorlarsa sisteminizde güvenlik yok demektir.

**Sistemin Güvenliği İçin Uyarılar:** Güvenlikte root şifresi son derece önemlidir. Kullanıcı psikolojisi olsa gerek, insanlar root yetkileriyle çalışmaktan hoşlanıyorlar. Bu nedenle de, eğer şifreyi biliyorlarsa gerekmese bile root kullanıcı olarak login etmeyi tercih ediyorlar. Bu nedenle:

Root şifresini iyi koruyunuz. Yetkili olmayan kimselere vermeyiniz.

Şifreyi sık sık değiştiriniz.

Kullanıcılarınızı şifre kullanmaya zorlayınız. Şifrelerini birbirlerine vermemeleri konusunda uyarınız.

Bu sistemin yürümesi için her kullanıcıya farklı bir hesap açmaya üşenmeyiniz.

Kullanıcılarınızı kolay tahmin edilebilecek şifreler seçmemeleri konusunda uyarınız.

İşten ayrılan ya da görev yeri değişen kullanıcıların hesaplarını hemen erişilmez hale getiriniz. Bunun en kolay yolu, ilgili kullanıcının **/etc/passwd ** dosyasındaki kaydında şifre bölümünün ilk karakteri olarak bir \*eklemektir. Bir nedenle kullanıcı hesabını tekrar açmanız gerekirse bu \*işareti kaldırırsanız olur biter.

Sisteminizin **/var/adm/mesages** veya benzer dosyalarına sık sık bakınız. Sistemde meydana gelen loginler ve su komutuyla root olan kullanıcılarla ilgili kayıtlar bu dosyalarda arşivlenmektedir. Bu dosyadaki kayıtlar isteminize girmeye çalışan kimseler olup olmadığı konusunda fikir verecektir.

Terminal başlı seri arabirimlerden ve bilgisayar ağı üzerinden gelen **telnet, rlogin** gibi bağlantılarda root olarak login edilmesini önleyiniz. Bu önleme işini BDS UNIX’lerde **/etc/ttyab** dosyasında, SVR4 UNIX’lerde /**etc/defaults/login** dosyalarında gerekli değişiklikleri yaparak halledebilirsiniz.

**SUID PROGRAMLAR: **En tehlikeli güvenlik gedikleridir. SUID özelliğine sahip programlar hangi kullanıcı tarafından kullanılırsa kullanılsın, çalıştıkları sürece root yetkilerine sahiptirler. Eğer bir SUID program, bir şekilde bir kabuk programına çıkış veriyorsa bunu keşfeden bir kullanıcı şifre vermeden root oldu demektir. Ne isterse yapar.

Sistem ilk kurulduğunda SUID programlatın bir listesini alın ve bu listeyi iyi saklayın zaman zaman sistemdeki SUID programların bir listesini alıp, elinizdeki ilk listeyle karşılaştırın. SUID programların bir listesini almak için şu komutu kullanabilirsiniz.

**#find/-user roor-perm-4000-execls-I{}\\;**

**ÖNERİ : **İnternet bağlantısında güvenli çalışmak için “firewall” yöntemlerini kullanınız. Bu yöntemde, sizin bilgisayar ağınızla internet arasına bir bilgisayar eklemeniz gerekecektir. Bunu göze alabiliyorsanız, “firewall” sistemi sorununuzu çözecektir**.******

**OS/2 WARP GÜVENLİK SEVİYESİ VE DESTEĞİ**

**Config.Sys Kütüğünün Kurtarılması**

CONFIG.SYS kütüğü, başlangıç sırasında sisteminizin konfigürasyonunu tanımlamak içi kullanılan komut deyimlerini içerir. Kütük yanlış değiştirilirse, sistemi başlatmayabilir ya da kütüğü düzenleyemeyebilirsiniz. (Örneğin bazı programlar kuruldukları zaman CONFIG.SYS kütüğüne bilgiler yazar. Bazı durumlarda, bu bilgiler CONFIG.SYS kütüğünün kullanılmamasına neden olur.) Özgün CONFIG.SYS kütüğü uyarlamasını (OS/2 kurulduğunda yaratıldığı şekliyle) kurtarmak için aşağıdaki yordamı kullanabilirsiniz:

Bilgisayarı açın. Bilgisayar açıksa yeniden başlatın.

Ekranınızın sol üst köşesinde küçük beyaz bir kutu görüldüğünde, **Alt+F1 **tuşlarına basın. ** ******

Kurtarma seçenekleri ekranı göründüğünde **C ** tuşuna basın.

**C: **yazın ve Enter tuşuna basın (burada C, işletim sisteminizin bulunduğu sürücüyü gösterir.)

Zarar gören CONFIG.SYS kütüğünü yeniden adlandırın. Örneğin, aşağıdaki komutu yazın:

** REN CONFIG.SYS CONFIG.BAD**

Enter tuşuna basın.

CONFIG.SYS kütüğünün yedek uyarlamasını işletim sisteminizin bulunduğu sürücünün kök dizinine kopyalayın. (CONFIG.SYS yedek kütüğü OS/2 kuruluşu sırasında yaratılmıştır.) Aşağıdaki komutu yazın.

**COPY C:\\OS/2\\INSTALL\\ CONFIG.SYS C:\\ CONFIG.SYS**

Enter tuşuna basın.

Diskette 1’i A sürücüsünden çıkarın.

Sisteminizi yeniden başlatmak için, Ctrl+Alt+Del tuşlarına basın.

**Kullanıcı INI Kütüğünün Kurtarılması**

Kullanıcı INI kütüğü olarak da anılan OS/2.INI kütüğü, program varsayılan değerleri, görüntü seçenekleri ve kütük seçenekleri gibi sistem ayarlarını içeren bir işletim sistemi başlatma kütüğüdür. Sistem INI kütüğü olarak da anılan OS2SYS.INI kütüğü, yazı tipleri ve yazıcı sürücüleri ile ilgili bilgileri içeren bir işletim sistemi kütüğüdür. OS/2.INI kütüğünün “bozulduğunu” belirten bir ileti alırsanız, sabit diskinizdeki hem OS2.INI kütüğünü, hem de OS2SYS.INI kütüğünü değiştirin.

Bu kütüğü varsayılan değerleri içeren uyarlamalarla değiştirmek için aşağıdaki yordamı kullanın:

Bilgisayarı açın. Bilgisayar açıksa, yeniden başlatın.

Ekranınızın sol üst köşesinde küçük beyaz bir kutu göründüğünde, ALT+F1 tuşlarına basın.

Kurtarma seçenekleri ekranı göründüğünde C tuşuna basın.

C: yazın ve Enter tuşuna basın (burada C, işletim sisteminizin bulunduğu sürücüyü gösterir.)

CD/OS2 yazın ve Enter tuşuna basın.

ATTRIB –s –h –r OS2.INI yazın ve Enter tuşuna basın.

REN OS2.INI OS2.OLD yazın ve Enter tuşuna basın.

MAKEINI OS2.INI INI.RC yazın ve Enter tuşuna basın.

REN OS2SYS.INI OS2SYS.OLD yazın ve Enter tuşuna basın.

MAKEINI OS2SYS.INI INISYS.RC yazın ve Enter tuşuna basın.

Diskette 1’i A sürücüsünden çıkarın.

Sisteminizi yeniden başlatmak için, Ctrl+Alt+Del tuşlarına basın.

Sisteminizi her başlatışınızda INI kütüklerin otomatik olarak yedeklenmesini sağlayarak bu kütüklerinizi koruyabilirsiniz. Örneğin aşağıdaki deyimi CONFIG.SYS kütüğüne eklerseniz o andaki INI kütükleriniz ve bu kütüklerin önceki sistem başlangıcındaki şeklinin bir kopyasını oluşturur. (bu örnekte OS2’ nin C sürücüsüne kurulduğu varsayılmıştır. OS/2 ‘ yi kurduğunuz sürücünün harfini kullanın.)

CALL=C:\\OS2\\XCOPY.EXE C:\\OS2\\\*.INX C:\\OS2\\\*.INY

CALL=C:\\OS2\\XCOPY.EXE C:\\OS2\\\*.INI C:\\OS2\\\*.INX

INI kütüklerini bu yolla kopyalayarak, kullanıcı INI kütükleri zarar gördüğünde, bu kütüklerin en son uyarlamasını kurtarabilirsiniz.

**Bellek Durum Verisinin Kurtarılması **

Bir arıza olduğunda bellek durumunu kurtarmak için OS/2 ‘ nin kullanıldığı yordam bellek dökümü olarak adlandırılır. Bellek dökümü, bir sorunun yeniden üretilmesinin zor olduğu ya da diğer sorun saptama yöntemlerinin sorunu tanımlayamadığı zamanlarda gerçekleştirilir. Bellek dökümü bilgileri daha sonra teknik uzmanlar tarafından incelenerek sorunun nedeni saptanabilir.

** Önemli: **Hizmet ve destek grubunuz bu işlemi önermedikçe bellek dökümünü gerçekleştirmeyin.

**İki tip bellek dökümü vardır:**

El ile bellek dökümü( sistemin durmasına neden olan sistem askı ve tuzakları için kullanılır.)

Otomatik bellek dökümü (uygulama programları, sistem tuzakları ve iç işletim hataları için kullanılır.)

Bir bellek dökümü FAT sabit disk bölümüne ya da biçimlenmiş disketlere yerleştirilebilir.

**KAYNAKÇA**

Çubukçu Faruk, Her Yönüyle Windows NT Workstation/Server, ALFA,Şubat, 1997

Chip Dergisi,Nisan, 1999

BYTE dergisi, Nisan, 1997

http://linux.gov.tr

Çubukçu Faruk, OS/2 İşletim Sistemi, 1995

Linux işletim sistemi,Sistem yayıncılık

PAGE

PAGE 3

Yönetimsel paylaşımlar durdurulabilir. Ancak sistemin yeniden açılmasıyla yeniden yaratılır. Bu durumda sistem yöneticisinin dikkatli olması gerekir. Aksi taktirde uzaktan kullanıcının NT Server’a girebilmesi ( NET USE ) ile ) mümkündür.

---
*Kaynak: `WİNDOWS NT GÜVENLİĞİ/O-d-e-v-s-i-t-e-s-i-com-19030.doc` — pınar — 2001*
