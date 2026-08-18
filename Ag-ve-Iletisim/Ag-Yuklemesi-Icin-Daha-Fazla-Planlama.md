# Ağ Yüklemesi İçin Daha Fazla Planlama

## **Ağ Yüklemesi için Daha Fazla Planlama **

Microsoft Windows NT Server sürüm 4 tarafından kullanılan veri yapıları, güvenlik açısından oldukça değerlidir, fakat aynı zamanda sistem bir kez yüklendikten sonra üzerinde bazı değişiklikler yapılmasını engelleyebilirler. Bu yüzden, sistemin ilk seferinde doğru yüklenebilmesi için dikkatli plan yapılması gerekir.

**Bir Dosya Sistemi Seçmek**** ******

Windows NT ağını yüklediğinizde FAT (file allocation table) ve NTFS (NT file system) olmak üzere iki ağ dosya sistemi seçeneğiniz vardır. Ağı FAT veya NTFS olarak önceden biçimlendirilmiş bir bölmeye yükleyebilirsiniz. Ayrıca sistemi yüklerkende bir bölmeyi FAT veya NTFS olarak biçimlendirebilirsiniz. Veya yükleme sırasında hiçbir veri kaybı olmadan, bir FAT bölmesini bir NTFS bölmesi olarak değiştirebilirsiniz.

NTFS'den daha düşük bir ek yükü olmasına rağmen FAT, sunucu için uygun bir seçim değildir. NTFS'in yerleşik güvenlik ve kurtulabilirlik özelliklerinden yoksundur. NTFS'in birçok özelliği onu Windows NT için yeğlenen dosya sistemi yapmaktadır:

• Korumalar ya dizinlere ya da kişisel dosyalara atanmaktadır. Dosyalar taşındıklarında bile izinlerini koruyabilirler.

• Hiç kimse bir disketten önyükleme yaparak NTFS sistemine yetkilendirilmemiş erişim kazanamaz.

• Çökme durumunda sistem kurtarılabilir; çünkü hareketler yürütülmeden önce bu hareketlerin günlük tutma işlemleri tamamlanmıştır. Disk onarım yardımcıları gerekli değildir.

• NTFS kendi disk alanlarını sürekli olarak gözler; eğer bir hasar bulursa, kötü alanı hizmet dışına çıkarır ve bu alandaki veriyi başka bir alana taşır. Bu sıcak düzenleme (hot fix) olarak adlandırılır ve çalışan herhangi bir uygulamada gözle görülmez.

RISC işlemcili makineler üzerinde bir FAT bölmesine ihtiyacınız olacak, ancak önyükleme amaçları için çok küçük bir tane de (min. 5 MB) yetecektir. Sabit diskin geri kalan kısmı NTFS olarak biçimlendirilmelidir.

Eğer güvenliğin değil de kullanışlığının önem taşıdığı bir ortamda iseniz, en azından bir küçük FAT bölmesini, Intel tabanlı sunucular üzerinde bile, kullanmayı düşünebilirsiniz. Çok güvenli ve sağlam bir yapılandırma olmadığı kesindir. Ancak sabit sürücünüzde küçük bir FAT bölmeniz varsa, EISA yapılandırma yardımcılarını çalıştırmak gibi sistem yönetiminin küçük işleriyle uğraşmak daha kolaydır. Tüm donanım yardımcılarını ona yükleyebilir ve sisteminiz çöktüğünde veya büyük sorunlar olduğunda bile bir disketten önyükleme yaparak yardımcılara gidebilirsiniz. Sabit diskin kendisi çöktüğünde bu kuşkusuz işe yaramayacaktır; dolayısıyla bu durumda güvenli, ancak erişebilir bir yerde disket sürümlerinizi tutmanız gerekecektir. Ancak küçük bir FAT bölmesine sahip olmak, bir çok durumda olayı kolaylaştırmaktadır.

Ancak güvenliğin ciddi önem taşıdığı bir ortamda FAT bölmesi kullanmayın. Bu durumda, tüm depolama sisteminizin NTFS için yapılandırılması iyi olur.

Yalnızca Windows NT ile çalışan bilgisayarların NTFS'i doğrudan kullanbilmelerine rağmen, ağ kullanıcıları hiçbir zorluk çekmeden NTFS bölmelerindeki dosyalara erişebilirler, MS,OS, OS/2, UNIX veya Microsoft Windows'un çeşitlemelerinden biriyle çalışıyor olsalar bile.

**Disk Bölmelerini Planlamak**** ******

Sunucunuzu kurduğunğzda, sunucunun kullanılabilir disk alanlarının bölümlemesine de karar vermeniz gerekecektir. Tek, büyük bölmeler ile çoklu, küçük bölmeler arasında dengelemeler yapılır.

Kavramsal olarak büyük, tek bölmelerle uğraşmak her zaman daha kolaydır, ancak büyük bölmeler kullanmak, sistem yapılandırılması için her zaman elverişli yol olmayabilir. Dikkate alınması gereken bir konu, sistemin genel kararlılığıdır. Eğer sisteminizin genel yapılandırılmasının, oldukça sabit bir uygulamalaru grubu ve istikrarlı bir kullanıcı nüfusuyla kararlı olması beklentiniz varsa, bu gereksinimlere karşılık verecek büyük bölmeler kullanmayı yeğleyebilirsiniz.

Eğer sunucunuz temelde bir veritabanı sunucusu işlevini görecekse, karar alma yönünde çok fazla şey yapmanız gerekmez. Veritabanınızın çekirdek program dosyalarını, mantıksal büyüme için yer ayırarak, tek bir bölme üzerine koymanız iyi olacaktır. Ancak hızı maksimumda tutmak için herşeyi bu bölme dışında tutmanız gerekeceğinden, bölmeyi buna uygun olarak boyutlandırın. Veri dosyalarının kendi başlarına nasıl düzenledikleri büyük ölçüde veritabanınıza bağlıdır, fakat dosyalar ya çoklu bölmeler ve çoklu sürücüler boyunca dağılacaklar ya da tümüyle veritabanı uygulamasının denetimi altında olan özel bir ham bölme üzerine depo edileceklerdir. Her durumda, veritabanının büyümesi için çok fazla alana gerek olduğunu fark edeceksiniz. Bir veritabanı sunucusu aynı zamanda, şeritleme (striping) veya diziler (array) kullanarak veritabanınızı çoklu sabit sürücüler boyunca yaymanıza izin veren bir RAID donanım veya yazılım çözümünün kullanılması için belirgin bir yerdir. Bu, sadece sınırsız bir büyümeye izin vermekle kalmaz, sabit disk boşluğunuzu ölçülü bir şekilde genişletebilme avantajını da sağlar; çünkü daha fazla dosya alanı gerektiğinde, bir ek sürücüyü basitçe dizinize ekleyebilirsiniz.
Diğer taraftan eğer işinizin doğası oldukça sık sistem değişiklikleri gerekiyorsa, daha küçük sabit disk bölmeleri kullanmayı daha anlamlı bulabilirsiniz; böylece özel bir proje için kolayca bir bölme yaratabilirsiniz. Proje tamamlandığında, gereken şey sadece veriyi arşivlemektir; bölme temizlenecek ve bir sonraki projeye hazır hale gelecektir.

NTFS'in bir büyük getirisi de, FAT kullanımındaki gibi büyük miktarlardaki alanlar harcamaksızın büyük ve tek bölmelere sahip olabilmenizdir. Sistem bölmesi yeterince büyük ve kararlı olacak ve birdenbire onu büyütmek derdine düşülmeyecektir. Tipik bir yükleme için, bugünlerde sabit sürücü alanının ucuz olduğunu varsayarsak, tipik bir sunucuya yaklaşık 500 MB yeter. Kuşkusuz kullanıcı ve uygulama bölmelerinin boyutu tümüyle sizin özel ortamınıza bağlı olacaktır. Ancak, onlara büyüme için fazla yer bırakmanız gerekmeyecektir, çünkü yeni kullanıcı ya da uygulama eklemeniz gerektiğinde, eski bölmelere dokunmadan basitçe bir başka sürücü ya da bölme eklenmelidir.

Disk bölmelerini planlarken dikkate almanız gereken bir şey de, eğer varsa, ne tür bir RAID ya da başka bir sürücü erişim yöntemi kullanacağınızdır. Eğer seçimşansınız varsa, bir özel RAID denetcisini veya bir RAID donanım çözümünü kullanmak gerekir. Yeterli bir RAID donanım çözümünü Windows NT Disk Administrator içinde yerleşik olarak bulabilirsiniz.

Bir disk dizisi veya ikizi oluşturmak için Disk Administrator'ın yerleşik araçlarını kullanmak kesinlikle avantajlıdır. Kuşkusuz, en önemlisi maliyettir, çünkü maliyet kayıp disk alanı ile sınırlıdır. Ancak, taşınabilirlik ve uyumluluk konusunda da üstünlükleri vardır. Disk Administrator, işletim sisteminin tümleşik bir bölümüdür; bu yüzden, Intel tabanlı veya RISC tabanlı bir sürücü için aynı biçimde kolayca yapılandırabilirsiniz. Bu bazı bilgisayarların gereksinimlerine bağlı olarak farklı işlemciler kullanıldığı çeşitlenmiş ağ boyunca, benzer bir yapılanmayı korumanıza izin verir. Ayrıca çözümü güç uyumluluk sorunları için endişe etmeniz gerekmez, çünkü Disk Administrator işletim sisteminin içinde tasarımlanmıştır.

Öte yandan, Disk Administrator kullanımında bazı kısıtlamalar vardır. Yalnızca üç temel RAID türünü destekler; İkizleme (RAID 1), şeritleme (RAID 0) ve eşlikli şeritleme (stripting with parity) (RAID 5). Bunlar en iyi bilinen ve en yaygın RAID türleri olsalar da, RAID seçenekleriniz neredeyse yalnız bunlarla sınırlrıdır ve sizin gereksinimlerinizi karşılamayabilir. Disk dizilerinizin kullanımını farklı bir donanım altsistemine taşımanın, hem hız hem de kararlılık açısından belirgin üstünlükleri olabilir. Öncelikle, RAID donanım çözümlerinin çoğu, sunucuyu tümüyle kapatmaksızın başarısız sabit sürücüleri kaldırmanıza (sıcak takas) izin verir; bu dabir üretim ortamında kesinlikle bir avantajdır.

**Ağ İletişim Kurallarını Seçmek**** ******

Windows NT Server geniş ölçüde iletişim kurallarında bağımsızdır. Standart iletişim kurallarından herhangi birini kullanarak işini görebilir ve tüm ana iletişim kurallarıyla boy ölçüşebilir.

• IPX/SPX : Novell NetWare ağlarının iletişim kuralı ve Windoe NT Server için varsayılan iletişim kuralı.

• TCP/IP : Internet'in iletişim kuralı ve geniş alanlı ağlar için yeğlenen iletişim kuralı.

• NetBEUI : Microsoft Lan Manager ağları ve Microsoft for Workgroups ağları tarafından kullanılan iletişim kuralı.

• AppleTalk : Macintosh bilgisayarlarının kullandığı iletişim kuralı.

• SNA DLC : Anasistem erişimi için iletişim kuralı.

Çok azımız bu iletişim kurallarının tümünü aynı anda desteklemeyi isteriz ve aslında buna gerek yoktur. Temel seçim iki tanedir: IPX/SPX veya TCP/IP.

IPX/SPX, NetWare ağlarında yıllardır başarıyla kullanılan hızlı ve esnek bir ağ iletişim kuralıdır; kurulumu ve yapılandırılması kolaydır. Bir yerel ağ için varsayılan iletişim kuralıdır ve bu düzeyin ötesinde bir bağlantı planlamıyorsanız, iyi bir seçimdir. Aynı zamanda NetWare sunucularla karışık bir ortama gireceğinizde de yeğlenen bir iletişim kuralıdır.

TCP/IP de hızlı ve esnek bir ağ iletişim kuralıdır. Esasen Internet için yaratılan TCP/IP, karşılaşabileceğiniz her türlü donanım veya işletim sistemi üzerinde çalışan ve yaygın kabul gören bir iletişim kuralıdır. Eğer geniş alanlı bir ağa ya da Internet'e bağlantı yapacaksanız, ağınız için yeğleyeceğiniz iletişim kuralı da TCP/IP olacaktır. TCP/IP, yapılandırılması ve sürdürülmesi zor bir iletişim kuralı olarak ün yapmıştır; ancak Windows NT Server'daki araçlarla TCP/IP'nin yapılandırılması ve sürdürülmesiişini geçmişte olduğundan daha kolay yapabilirsiniz.

NetBEUI yerel ağ yapılandırılmasının ilk zamanlarında geliştirilmiştir. Küçük ve bazı durumlarda nispeten hızlıdır ve Lan Manager ve Windows for Workgroups ağları için kullanılan bir iletişim kuralıdır. Bunula birlikte, günümüzün farklı ağ ortamında, sınırlamaları yararlarından daha ağır bastığından, ömrünün sonuna gelmiştir.

AppleTalk ve SNA DLC, sırasıyla Macintosh ve anasistem (mainframe) ortamlarına bağlantıyı kolaylaştırmak için, Windows NT Server'a katılmıştır. Eğer ağınız bu platformlardan birini içeriyorsa, uygun iletişim kuralını ekleme gereğiniz olacaktır. DLC, Hewlett-Packard yazıcılarla konuşmak için yararlı bir iletişim kuralıdır. Bunula birlikte, her iki durum için de TCP/IP'yi kullanabileceğinizi görebilirsiniz. Her iki ortam için de mükemmel TCP/IP çözümleri vardır ve her ikisinin de gelecekte TCP/IP'ye gittikçe daha fazla yönelmeleri olasıdır. Bununla birlikte, bir kalıt ortamı destekleme gereğiniz olabilir ve Windows NT Server bunun için gerek duyacağınız araçları içerir.

## **Güvenlik Planlaması **

Hemen hemen tüm ağ kullanıcıları, soyut konuşulduğunda güvenliğin iyi bir şey olduğunu kabul ederler. Ancak günün birinde, bir parolayı unuttukları, istedikleri bir belgeye ulaşamadıkları, en yakınlarındaki yazıcı dururken koridorun sonundaki yazıcıdan çıkış almak zorunda kaldıkları, Internet'ten aldıkları nefis bir programı yükleyemedikleri zaman bu durum değişir. Güvenlik yüzünden çalışmaz olduklarını söylerler. Öte yandan, erişilen, değiştirilen hatta tahrip edilen dosya kendilerinin ise, bu kez de güvenlik gevşek diye yakınırlar.

İdeal bir güvenlik, hem kimsenin özel bir izni olmadan hiçbir şeye ulaşamayacağı kadar eksiksiz, hem de varlığını hiç kimsenin hissetmeyeceği kadar şeffaf olmalıdır.

**Ağ Yönetim Modelleri ve Güvenlik Sorunları**** ******

Ağınız için seçtiğiniz yöntem modeli, uygulamanız gerek güvenlik önlemi türlerini etkiler. Ağ yönetimi dört temel yapılandırmadan birinde organize edilebilir:

• Bir kuruluşun tümü için merkezden

• Bölüm veya grup temelinde yerel olarak (dağıtılmış yöntem)

• İşletim sistemi ile

• Yukarıdakilerden bazı bileşenleri ile

Yönetim modellerinin hem küçük hem de büyük ve karmaşık modeller için benzer olabilmesi şaşırtıcıdır. Bu modellerin ölçek ve derecesi farklılaşabildiği hakde, temel yaklaşım aynıdır. İncelenebilecek üç model vardır:

**Merkezden Yönetim **

Bir merkezden yönetim modelinde, örgütlenme içindek kaynakların, kullanıcıların ve ağların tümünü bir kişi, grup veya bölüm yönetir. Bu model, küçük ve orta ölçekli örgütlenmelerde iyi çalışır; büyük ya da coğrafi olarak dağınık olan örgütlenmelerde yavaş veya yetersiz kalabilir. Ancak, güvenlik açısından, merkezden yönetim en iyi modeldir. Sistem politika ve yordamların tüm örgütlenmede tek tip olmasını sağlar. Yöneticiler hem ağ içindeki kaynak ve kullanıcıların yeniden konumlandırılmasını, hem de kullanıcı profil ve erişimlerinde gerekli değişiklikleri hızla gerçekleştirebilir.

Merkezden yönetim modeli

**Dağıtılmış Yönetim **

Dağıtılmış yöntem modelinde ağ, bölüm ve çalışma grubu düzeyinde yönetilir. Bu yerel düzeydeki yönetim kullanıcı gereksinimlerine hızlı yanıt vermeyi kolaylaştırsa da, bu yanıt hızı çoğu zaman ağ güvenliği pahasına başarılabilmektedir. Bir ağ üzerinde çeşitli bölüm ve çalışma grubu düzeyi yönetici olduğunda, sistem politikaları ve yordamları bir çalışma grubundan diğerine değişmektedir. Bir sistemde ne kadar çok grup bulunursa, çoklu güven ilişkileride o kadar çok gerekecektir.

Dağıtılmış yönetim modeli

**Karışık Yönetim **
Karışık yöntem modeli hem merkezden, hem de dağıtılmış yönetim modellerinin özelliklerini taşır. Bölüm veya çalışma grubu düzeyindeki yöneticiler kullanıcıların günlük gereksinimleri ile ilgilenirken, merkezi yönetimdeki sistem politikalarının kuruluş çapında uygulanmasını sağlar. Bu, genellikle küçük örgütlenmelerin karşılabileceklerinden daha büyük bir personel yatırımı gerektirmektedir, dolayısıyla karışık yönetim modeli genellikle daha büyük organizasyonlarla sınırlandırılmıştır.

Karışık yönetim modeli

**Ağ Güvenlik Türleri**** ******

Ağ güvenliği için dört ana kategori vardır:

• Fizikselgüvenlik

• Kullanıcı güvenliği

• Dosya güvenliği

• Davetsize karşı güvenlik

Ağınızın büyüklüğü ne olursa olsun, bu kategorilerin hepsi hakkında bilgi sahibi olmanız gerekmektedir. Ancak bunlardan biri veya diğerinin göreli önemi, ağın boyutu değiştikçe değişecektir.

**Fiziksel Güvenlik **
İster ağ sunucusu, ister masaüstü iş istasyonu, isterse taşınabilir bilgisayar veya bir alışveriş merkezindeki ortak erişim terminali olsun, her bilgisayarın fiziksel olarak güvende olması gerekmektedir. Bilgisayarı fiziksel olarak alıp götürebilen biri, verinize erişim kazanabilir. Yine de bu, tüm bilgisayarlarınızı sürgülemeniz anlamına gelmez. Fakat, ağ sunucularının konumuna karar vermek, biraz daha fazla özeni gerektirmektedir. Çok fazla yürümemek için bu yerin yakın olması iyi olur. Kapısı kitlenen, iyi havalandırılmış, iyi aydınlatılmış bir oda bu iş için uygun olacaktır.

**Kullanıcı Güvenliği **
Kullanıcı güvenliğinin iki yönü vardır:

• Kullanıcıların gerek duydukları kaynaklara erişimini kolaylaştırmak.

• İşlerini yapmaları için gerekli olmayan kaynakları ise, kullanıcılardan uzak tutmak ve hatta gizlemek. Bu kaynaklar, hem işletmenin en gizli bilgilerini, hem de diğer kullanıcıların kişisel varlıklarını kapsar.

Mümkün olduğu kadar, ağa ve ağ kaynaklarına erişim için kullanıcıların sadece bir kez girmeleri gereken, tek bir parolayı anımsamaları iyi oluuur. Buna karşın, yüksek derecede hassas kaynaklara erişim için ikinci bir parola girme zorunluluğu, bu kaynakların gizlilik özelliğini pekiştirir. İnsanlar iki veya üç parolayı anımsamayabilirler. Fiziksel yerleşimle birlikte ağınızın mantıksal düzenini de planlamanız, daha sonra karşınıza çıkabilecek pek çok güvenlik ve yönetim sorunlarından sizi kurtaracaktır. Etki alanlarının, basit fiziksel yakınlık yerine kişi ve nesnelerin mantıksal gruplamalarını içereceği biçimde düzen planlanır.

**Dosya Güvenliği **
Dosya güvenliğini sağlamanın iki yolu vardır:

• Dosya erişimini denetlemek

• Dosya bütünlüğünü korumak

Hem veri hem de belge dosyaları yapılandırılmış biçimde veri içerir, ancak belge dosyaları genellikle insanlar tarafından okunabilirken, veri dosyaları bir program tarafından yorumlanmalıdır.

Microsoft Windows NT Server sürüm 4 hem klasör hem de dosya düzeyinde erişimi denetlemenize olanak sağlar. Böylece,bir klasöre tam erişimi olan biri, o klasördeki bir dosyaya erişemeyebilir veya bunun tam tersi. Ancak bu sadece, NTFS dosya sistemini seçmişseniz mümkün olabilr. Aslında,Windows NT'deki izinler, herhangi bir dosyaya atanabilen bileşimlerdir. Kişisel dosya özellikleri şunlardır:

• Read (R)

• Write (W)

• Execute (E)

• Delete (D)

• Change Permissions (P)

• Take Ownership (O)

Ayrıca, yetkilendirilmemiş erişim denemelerini önleyecek şekilde hassas ve gizli dosyaları denetlemek gerekir.

**Program dosyaları **
Program dosyaları ve onları içeren klasörler, hemen her zaman Read'e ayarlanmalıdır, çünkü kullanıcılar nadiren yazmaya gerek duyacaklardır. Ayrıca Read erişimi, kullanıcıların kasıtlıı veya kasıtsız olarak dosyaların silinmesi, üzerine yazmasını ya da virüs getirmesini önler. Bununla birlikte, bütün dosyaları Read'e ayarlamak da yeterli değildir, çünkü bir klasöre Change Permissions erişimi olan bir kullanıcı, klasördeki herhangi dosya için erişimi değiştirebilir.

**İyi Bir Parola Seçmenin Kuralları**** ******

İyi bir parola aşağıdaki özelliklere sahiptir:

• Oturum açma adındaki karakterlerin bir rotasyonu değildir.

• En azında iki alfebetik ve bir tane de alfebetik olmayan karakter içerir.

• En az altı karakter uzunluğundadır.

• Parola, kullanıcı adı ve başharfleri, çocuklarının veya diğer belirgin kişi adlarının baş harfleri veya bu tür verilerle kullanıcının doğum tarihi ve telefon numarası gibi verilerin bileşimide değildir.

## **Windows Nt de Donanımın Planlanması ve Yerleştirilmesi **

Ağ için donanım seçmek, tek bir iş istasyonu için donanım seçmekten daha özenle yapılmalıdır. İş istasyonları, genellikle kendi iç yapılandırılmaları dikkate alınmaksızın bir ağa bağlanabilir, ancak sunucu ve denetcilerin, en iyi başarımı elde etmek için, ağdaki rolleri düşünülerek tasarlanmaları gerekir. Her ne kadar kötü tasarlanmış ve yapılandırılmış bir iş istasyonu kendi kullanıcısını kızdırsa da, ağ üzerindeki rolü düşünülerek tasarlanıp yapılandırılmamış bir sunucu, ağ üzerindeki tüm kullanıcılar için sorun yaratacaktır.

İlk kural şudur: Microsoft Windows NT Server 4.0 Hardware Compatibility List'te olmayan bir sunucu veya denetçiyi kullanmayı düşünmeyin. Bunun iki nedeni vardır. Birincisi, ağınızdaki en önemli makinelerin hepsi resmen uyumluysa, herşeyin mükemmel çalışması şansına sahipsinizdir. İkisi, eğer bilgisayarlarla veya listedeki diğer gereçlerle herhangi bir sorununuz olursa, Microsoft'u arayabilirsiniz. Eğer, uyumlu olarak tanımlanmamış bir gereci kullanıyorsanız, kendinizle başbaşa kalırsınız. Sorununuzun donanımla ilgili olup olmaması, bu durumda önemli olmayacaktır. Dolayısıyla bileşenlerin, her zaman donanım uyumluluk listesinden seçtiğinizden emin olmak gerekir. Microsoft Windows NT, donanım konusunda Microsoft Windows'un Microsoft Windows 95 gibi diğer sürümlerinden çok daha titiz olsa da, uygun donanımların listesi her Windows NT sürümüyle biraz daha uzamaktadır. Seçimlerinizi donanım uyumluluk listesi ile sınırlamak sıkıntı yaratmayacaktır.

Eğer çok sayıda sistem yerleştirmeyi planlamış ve donanım uyumluluk listesinde bulunmayan bir donanım parçasını kullanmak zorunda kalmışsanınız, donanım sağlayıcınızın listeye katılması için bu öğeyi Microsoft'a bildirmesi, harcadığı zamana ve paraya değer.

**Sistemi Tasarlamak**** ******

Microsoft Windows NT Server sürüm 4 sistemini tasarladığınızda, karar alma sürecinizde dikkate alıp dengeleyeceğiniz üç etken vardır:

Ağınız için seçmiş olduğunuz etki alanı türü

Başlangıç boyutu ve sistemin beklenen gelişimi

Kaynakların örgütlenmedeki konumları

**Etki Alanı Modeli**** ******

Etki alanı modelinizin eninde sonunda neye benzeyeceğini düşünmeksizin, tek bir etki alanıyla başlayın ve gereksinimler sisteminizi aşıncaya kadar orada kalın. Bu, sizin Windows NT sunucu araçlarını tanımanıza, olası yükleme sorunlarını tanımlamanıza, donanım seçimlerinin akıllıca olduklarından emin olmanıza ve denetimli bir ortamda bile kaçınılmaz olarak beliren sistem hatalarını ve kullanıcı arabirimi sorunlarını incelemenize olanak verir. Test ortamında yakalamış olduğunuz sorunlar için endişelenmeniz gerekmeden, ağınızın ölçeğini büyüttüğünüzde yeteri kadar yenisiyle karşılaşabilirsiniz. Hızla ilerleme eğiliminde olsanız da, şimdi fazla zaman harcmak, sistemin yüklenme ve uygulaması sürecinin tamamını kolaylaştıracaktır.

Başlangıçtaki birincil etki alanı denetçinizi çalışır duruma getidikten sonra, örgütün etkili kullanıcılarını sürece katın. Bu kullanıcıları başlangıç işleminin bir parçası yapın ve etki alanları, yerel genel grup türleri ve uygulama teknikleri hakkındaki kararlara katılmalarına izin verin. Daha en başta bir anahtar kullanıcı grubu oluşturmak, tüm süreci benimseyen müttefikler yaratarak sistemin uygulayışını çok kolaylaştıracaktır. Bunlar sizin en iyi ve en etkili savunucularınız olabilir. Ve büyük bir ağ projesini uygulamış olan herkesin bildiği gibi, savunmaya ihtiyacınız olabilir.

Bu çekirdek grubun aynı ölçüde önemli bir başka önemli rolü daha vardır. Bunlar maden ocağınızın sirenleri olabilirler; yükleme sırasında sorunlar olduğunda bu grup, sorun kontrolden çıkmadan önce hızla tepki vererek erken uyarı sistemi olacaklardır. Bu kişiler test aşamasında sizinle yaptıları çalışmalar sayesinde, yeni ortamlarından ne bekleyeceklerini bilirler ve porjeniz ufak bie örnek çalışmadan tamamlanmış bir ortama dönüşünceye kadar, sistemde oluşabilcek tüm başarım azalmalarını ve gariplikleri derhal farkedeceklerdir.

**Başlangıç Boyutu ve Sistemin Beklenen Gelişimi**** ******

Başlangıçtaki ağ boyutunuz ile sisteminizin beklenen gelişimi arasındaki farkı dikkate almak önemlidir. Örneğin, büyük bir şirketin bir bölümünde bir ağ kurarken bu sistemin, şirketin geri kalan kısmını da içine alabilecek şekile gelişme olasılığını göz önünde bulunduruyor olabilirsiniz.

Sadece şu anki durumunuz değil, şirketinizin gelecek için planladığı koşullara uyan bir etki alanı modeli seçilmelidir. Başlangıçtaki tasarım şirketinizin gelecekteki gereksinimlerini dikkate almadan yapılmışsa, sonradan etki alanı modelinizi değiştirmek çok daha zor olacaktır. Örneğin, eğer örgütümüzün kuvvetli, merkezi bir bilişim sistemi varsa, etki alanı mimarinizi tam güven ilişkili bir model etrafında tasarlamayı istemezsiniz. Bu durumda temel etki alanı veya çoklu temel etki alanı daha uygun olacaktır. Öte yandan, örgütünüzdeki her bölüm veya departmanın genellikle kendi kaynaklarında sorumlu olduğu ve bilişim sistemleri departmanınızın esas olarak destekleyici bir rol üstlendiği bir durumda, çoklu temel etki alanı modeli çok daha anlamlı olacaktır. Ancak bu durumda bile, kuruluşunuzun tek bir yerleşim ve az sayıda departmanın ötesinde gelişeceğini düşünüyorsanız, temel veya çoklu temel etki alanı modelinin karmaşık güven ilişkilerini sürdürmek, bazı noktalarda çok büyük sıkıntılar yaratır.

Nispeten az sayıda sunucu her biri birden çok görevi gerçekleştirecek şekilde kullanmayı düşünüyorsanız, güçlü makinelere ihtiyacınız olacaktır. Kaynakları biraz daha dağıtılmış olduğu ve birkaç sunucunun etki alanı denetçilerine yardım ettiği bir yapıda, her makinenin çok güçlü olmasına gerek yoktur. Ancak, dağıtılmış kaynaklarınız olsa bile, kendinize ileriye yönelik büyüme için yer bırakın. Böylece kullanıcılarınıza bugün nitelikli hizmet vermeyi ve ileride giderek artan isteklere destek verebilmeyi sağlamış olursunuz. Potansiyel büyüme alanları olarak şu anahtar alanları aklınızda bulundurun:

Bellek

İşlem gücü

Sabit sürücü sığası, esnekliği ve hızı

Ağın bant genişliği

Bu alanların hepsi için, başlangıçtaki ağ kurulum aşamasında kendinize büyüme için yer bırakabilirsiniz.

**Bellek **
Her zaman belli bir bellek miktarı için mümkün olan en az sayıdaki yuvayı seçmektir. Örneğin, bir sunucuda 64 MB'lık RAM verebilmek için kolayca dört veya sekiz yuva kullanabilirsiniz. Ancak mümkün ise, bunu yapmamanız iyi olur. Daha ileri bir planlama yaparak, gelecekte kendinizi kısıtlamaktan kolayca kaçınabilirsiniz. İstediğiniz sonucu verecek olan maksimum bellek modül boyutunu seçin. Çoğu durumda yeni Pentium veya PentiumPro ana çevrim kartları için bu ölçü iki yuvadır, altı tane de gelecekteki bellek için bırakırsınız. 128 MB' tan fazlasını destekleyemeyecek bir ana çevrim kartı seçmeyin. Bu başlangıçta çok büyük bir bellek gibi gözükebilir ve fazlasıyla yeter. Ancak sonradan daha fazla belleğe ihtiyacınız olursa, yeni uygulamalarınız ve veritabanı sunucunuz 256 MB gerektirirse, eski RAM'inizi yeniden işleyip kullanılabilir duruma getirmek için bir yol aramak gerçekten sinir bozucu olmaktadır.

Bir Windows NT ağındaki tüm etki alanı denetçi ve sunucuları en az 32 MB RAM kullanımdan yarar görecektir. Tabii ki, bellek fiyatları böyle kalırsa, her makinede bu kadar RAM ayıramayabilirsiniz. Bir denetçi 16 MB RAM'le bile idare edebilir; ancak her dört MB'lık RAM bir fark yaratacaktır, dolayısıyla yapabildiğiniz sürece 20 veya 24 MB'a çıkın.

Ağ boyunca kaynakları dağıtmak, ancak RAM veya işlem gücü yetersizliği ile karşılaşmayacaksanız iyi bir fikir olabilir. Her biri, yönetebileceğiniz en çok RAM'e sahip olanaz sayıda sunucuya sahip olmak, daha az RAM'li çok sayıda makineye sahip olmaktan çok daha iyidir.

**İşlem gücü **Ek işlemcileri destekleyebilecek bir sunucuyla işe başladığınızı düşünün. Başlangıçtaki sisteminiz ekstra gücü gerektirmese bile, ek CPU'ları destekleyecek bir tasarım, gereksinimleriniz beklentilerinizin ötesinde arttığında sığayı hızla ve kolaylıkla yükseltmenize olanak tanıyacaktır. Birden fazla CPU'yu destekleyebilecek bir sunucu için yüksek bir para ödeyecek olsanızda, maliyet gerçekte çok fazla olmayacaktır. Birden fazla CPU'yu destekleyebilen bir sistem, diğer anahtar alanlarda da kolayca ölçeklenebilir biçimde tasarlanmıştır.

**Sabit sürücüler **Aynı düşünceler sabit sürücüler için de geçerlidir. Er ya da geç, sunucularınıza ek sabit sürücü sığası eklemeniz gerekeceğinizden emin olabilrsiniz. Depolama gereksiniminin varolan sığanızı her zaman aşması Murphy'nin değişmez kanunlarında biridir. Eğer, depolama alt sisteminizi çoklu sürücülerin çevresinde tasarlamısanız, kullanıcılarınızı ve yapılandırmanızı rahatsız etmeden yeni yer eklemek kolay olacaktır.

**Ağın bant genişliği **
Potansiyel sistem büyüme dar boğazı olarak aklınızda bulundurmanız gereken son alan ağ altsistemdir. Windows NT Server, NetBEUI, IPX/SPX, TCP/IP vediğer ağ iletişim kurallarını desteklemektedir, ancak mümkün olduğu sürece TCP/IP'yi kullanmak gerekeceği kesindir. NetBEUI, büyük ve yoğun bir ağın kullanımından sorumlu değildir. Ayrıca NetBEUI ile ağınızı parçalara da bölemezsiniz, çünkü dolaştırılamaz. Windows NT'nin önceki sürümlerine var sayılan iletişim kuralı , esas olarak Novell NetWare ağlarında kullanılan iletişim kuralı IPX/SPX'dir. Kurulumu ve yapılandırılması TCP/IP'den daha kolaydır, ancak ağ dünyasının gelecekteki hakimi TCP/IP olacaktır. TCP/IP'yi windows NT'deki araçlarla kurmayı, modası geçmiş yoldan şekillendirip tüm önemli ayrıntıları sapmaktan daha kolay bulabilirsiniz. Eğer Windows 95 veya Windows NT Workstation'a yükseltemeyeceğiniz kalıt MS-DOS ve Windows makineleriniz varsa, bu makineleri NetBEUI ile sunucuya bağlamaya seçebilirsiniz. Windows 95 makinelerinde zaten yerleşik mükemmel bir TCP/IP vardır ve TCP/IP'yi kolaylıkla Microsoft Windows for Workgroups 3.11 istemcilerine ekleyebilirsiniz.

Sabit sürücü ana adaptörünüz gibi, ağ kartlarınızın da sisteminizin en hızlı yolunda olmaları gerekmektedir. Buna ek olarak, sonradan yükseltmeye karar verirseniz, daha hızlı ağları kolayca destekleyebilecek bir ağ kartını seçmeniz de iyi olabilir.

**Kaynak Konumları **
Planlama sürecinde dikkatlice düşünmenizi gerektiren bir başka ağ özelliği de, ağ kaynaklarının belirlenmesi ve bu kaynakların ağ üzerindeki yerleşimidir. Ağınızın boyutuna ve temel işlevine dayalı olarak kaynaklarınızın çoğunu, her etki alanındaki bir veya iki sunucuda merkezleştirmek veya ağ üzerinde dağıtmak isteyebilirsiniz. Genellikle kaynaklarınızı mümkün olduğu kadar çok sayıda sunucuya yaymak yararlıdır. Örneğin, sunucularınızdan birini bir veritabanı sunucusu olarak kullanacaksanız, onu çok sayıda kullanıcı uygulamalarını da destekler durumda yüklemeyi istemezsiniz. Benzer şekilde, ana uygulama sunucunuz da yazdırma sunucunuz olmamalıdır. Bu işlevleri ağ üzerine yayarak her işlev için işlem gücünü ve bant genişliğini maksimuma çıkarabilirsiniz. Ancak bu, sözkonusu işlevler için önceden yapılandırılmış seçenekleri planlamak anlamına gelecektir. Örneğin, eğer yazdırma sunucunuzu geri almanız gerekiyorsa, ağınızın bütünün birden bire yazıcısız kalmasını istemezsiniz. Bu noktada yapılacak küçük bir planlama kullanıcıları daha mutlu kılacaktır.

**Uygun Donanımı Seçmek**** ******

Tahmin edebileceğiniz gibi, düşük bilgisayarların Windows NT Server ağında sunucular olarak yeterli br rolü olamaz. Bununla birlikte, bütçeyi her makine de aşmanın da gereği yoktur. Her makineyi, yapması gerekenler ve göreceli hızının ağın geri kalanı üzerindeki etkisi bakımında değerlendirmek lazımdır.

**Denetçiler için Donanım **
İster birincil ister yedek olsun, etki alanı denetçileri kendi rollerine uyan donanımı gerektirirler. Denetçiler, kullanıcılar için, oturum açma doğrulaması sağladıkları ve ayrıca dosya erişim isteklerini de onayladıkları için, bu işlemlerin hızlandırılması hızlı bir ağ kartı (PCI veya EISA) ve hızlı bir sabit sürücü gerektirebilir.

Denetçi, bir iş istasyonu olarak kullanılamayacağından, minimum VGA video kartından ve VGA uyumlu monitörden daha fazlasına gereksiniminiz olmaz. Bir süper işlemciye de gerek yoktur, çünkü çok fazla bir işlem yapılmaz. Bununla birlikte en az bir Pentium 90 veya 100 gereklidir. Yapılan işe göre RISC tabanlı makinelerden herhengi biri de olmalıdır.

Bir tane çok büyük disk kullanmak yerine çoklu küçük diskler kullanmak gibi bazı temel tasarım alternatiflerini düşünün ve ek sabit sürücüleri kolayca destekleyecek bir sunucu donanımını seçin. Windows NT Server EIDE sabit sürücülerini desteklese de, bu sabit sürücülerin sunucuda yerleri yoktur. Sabit disk isteklerinin olabildiğince fazlasını işleyecek bir SCSI yolu gerekir ki, hem yol hem de sabit sürücü birden fazla isteği ardarda karşılayabilsinler. SCSI ana adaptörü sisteminizin desteklediği (EISA veya PCI gibi) en hızlı yola yerleştirin, çünkü sistem başarımının potansiyel dar boğazı buradadır. Disk ikizi yaratma (mirrorring) ve RAID, düzgün çalışabilmek için SCSI disk altsistemlerini gerektirir. SCSI sistemlerini alırken, az bilinen bir kuruluşun kendini kanıtlamamış araç gereçleri ile tutumluluk yapmaya çalışmayın. Adaptec gibi iyi bilinen markalardan şaşmayın.

**Dosya Sunucuları için Donanım **
Dosya sunucularının istekleri almaları ve hzla yanıtlamaları gerekir. Bunun için, makul hızda bir işlemciye (Pentium 120 veya daha iyisi) ve hızlı bir ağ kartına (PCI veya EISA) sahip olmaları gerekir. İstekler sabit sürücüden dosya almak içindir; dolayısıyla hızlı sabit sürücüler ve hızlı sabit sürücü denetçileri zorunludur. Yoğun bir ağda tek bir bilgisayarın çoklu sabit sürücüleri ve sabit sürücü denetçileri olabilir.

**Uygulama Sunucuları için Donanım **
Uygulama sunucularının da hızlı hızlı sabit sürücüye ve PCI veya EISA gibi ağ kartlarına ihtiyacı vardır. Ek olarak, bir uygulama sunucusu elde edebileceğiniz (ve satın alabileceğiniz) en hızlı işlemciyi gerektirmektedir. Eğer uygulamalar bir sunucuda tutulacaksa, yavaş bir işlemci kullanıcılarınızın sabırlarını zorlayabilir.

**Uzaktan Erişim Sunucuları için Donanım **
Uzaktan erişim sunucusu olarak 80486 işlemli daha eski bir bilgisayar uygundur; böyle bir sunucu için ağ kartının pek de hızlı olması gerekmez.

Bir uzaktan erişim sunucusu için pahalı bir donanım ayırmanın anlamı yoktur, çünkü bilgisayar en yavaş bilgisayardan da yavaş olan çevirmeli bağlantıdan daha hızlı gidemez. Yalnızca RAS'ınız aynı anda birçok kullanıcı ile uğraşıyorsa, gereklerinizi o makine için gözden geçirmeniz gerekecektir.

**Yazdırma Sunucuları için Donanım **
Burası, donanım envanterinizdeki en yavaş bilgisayarları bulundurabileceğiniz yerdir. Yazdırma işleminin dar boğazı bilgisayar veya ağ kartı değil, yazıcının kendisidir. Yazıcılar (bilgisayarlara göre) yavaştırlar, dolayısıyla hemen hemen her bilgisayar yazdırma sunucusu olarak kendine bir yer bulabilir; burada ne RAM ne de hızlı sabit sürücüler önem taşır. Bununla birlikte, gereki kuyruk dosyaları için yeterli sabit sürücü alanınız olduğundan emin olmanız gerekebilir.

**İş İstasyonları için Donanın **
İş istasyonlarının yalnızca yapacakları işe uygun donanıma gereksinimleri vardır. Burası, kullanıcı yararına, iyi video kartları ve monitörlere para harcanacak yerdir. Yalnızca tüm iş istasyonu çalışmaları yerel olarak yapıldığında, hızlı ve büyük sabit sürücülere gerek olur. Eğer dosyalar ve uygulamalar ağda dışarıda ise yerel sabit sürücü yavaş olabilir, ancak ağ kartının hızlı ve verimli olması gerekir.

## **Etki Alanlari ve Güven Iliskileri **

Microsoft Windows NT Server sürüm 4 agindaki temel yapisal unsur olan etki alani (domain) kavrami ve karmasik bir Windows NT server agindaki etki alanlari arasi iliskilerin temeli olan güven kavrami, ag sistemlerine iliskin gittikçe karmasiklasan istemlerden dogmaktadir. Microsoft, ilk ag sunumlarinda, Microsoft Windows for Workgroups'ta çalisma grubu kavramini gelistirmistir. Çalisma grubu, bilgi gereksinimleri, çalismalari birbiriyle iliskili olan ve kendi dosya kaynaklarini digerleriyle paylasmak isteyen bilgisayar kullanicilarinin mantiksal bir gruplamasidir. Çalisma grubundaki tüm bilgisayarlar esittir; merkezi bir kaynagin bulunmasinin hiçbir yarari olmadigindan, kaynaklarin toplandigi bir merkezi bilgisayar da yoktur. Bu tür kurulumlarin es düzeyde aglar (peer to peer network) olarak adlandirilma nedeni de budur.

**Çalışma Grupları ile Windows NT Server Ağları Karşılaştırması**** ******

Çalisma grubu aglarinin çekiciligi, kurulup sürdürülmelerinin kolayligindan gelir. Birbirinden bagimsiz kullanicilar, neyin paylasilacagini ve kimin erisecegini belirleyerek kaynak paylasimini yönetirler. Bir kullanici diger kullanicilarin bir yaziciyi, bir CD-ROM sürücüsünü, bir sabit sürücüyü veya yalnizca belirli dosya ve dizinleri paylasmalarina izin verebilir. Zorluklar, ag çok genislediginde veya her kullanici ya da kullanici grubu için kaynaklara erisim düzeyinin farklilastirilmasi gerektiginde ortaya çikar.

Tek basina boyut, bir çalisma grubunun etkisini sinirlayabilir. Birçok kullanici varsa ve kaynaklarin sayisida buna bagli bir arti olmussa, kullanicilar kaynaklari bulmakta zorlanabilir. Çalisma gruplarinin formel olmayan yapisi, hiçbir merkezi yönetim ve denetim olmadigi anlamina gelir. Büyük bir grupta, sistemi yönetmek ve sürdürmek için gereken zaman ve çaba yildirici olabilir, çünkü her bilgisayar tek tek yapilandirilmak zorundadir.

Kullanicilar arasinda bir ayrim (yani, belli kaynak için farkli düzeylerde kullanici erisimine izin verilmesi) gerektiginde, erisimi sinirlandirmak için parolalar gerekebilir ve yapilir da. Fakat, es düzeyde aglar büyüdükçe parolalar artar ve sistem giderek karmasiklasir. Sistemin farkli parçalarina erisim için farkli parolalari olmasi gereken bir çok kullanici, ayni parolayi tekrar tekrar kullanmaya ya da animsanmasi, dolayisiyla da tahmin edilmesi kolay parolalar seçmeye baslar. Güvenlik zayiflar. Ayrica, sistemin çevirmeli baglantilari varsa ve birisi kurulusun en büyük rakibine çalismak için isi birakmissa, tüm parolalarin degistirilmesi ve çalisma grubundaki kullanicilarin yeni parolalar konusunda bilgilendirilmesi gerekir; sistem yöneticisi ve kullanicisi için yine yildirici bir manzara söz konusudur.
Bütün bu nedenlerden dolayi es düzeydeki aglar, özellikle büyük veya merkezlesmis denetim gerektiren aglar için yeterli degildir. Windows NT Server'daki yerlesik etki alani yapisi, daha büyük bir esnekligin yani sira, büyük ve karmasik sistemlerde iyi çalisan basitlestirilmis bir yönetim tarzi sunmaktadir.

**Agi Planlamak**** ******

Her proje planlamayla baslar. Baslamadan önce neyi basarmak istediginizi kesin ve ayrintili olarak bilmiyorsaniz, çok hata olacak ve çok zaman yitirilecektir. Olmak isteyeceginiz en son yer, hosnutsuz kullanicilarin olusturdugu bir agin ortasidir; en iyisi, makineye kabloyu baglamadan önce, her seyi düsünmektir.

**Etki Alanlarini (Domain) Tanimlamak**** ******

Windows NT Server'in temel birimi olan etki alani, bir veritabanini paylasan ve ortak bir güvenlik politikasi olan bilgisayarlar grubudur. Etki alani, birincil etki alani denetcisi (primary domain controller-PCD) olarak islev gören bir bilgisayar, yedek etki alani denetcisi (backup domain controller-BDC) olarak islev gören en az bir bilgisayar ve en az bir is istasyonu içerir. Ek is istasyonlari olabilecegi gibi, ek yedek etki alani denetçileri ve sunucularida olabilir.

Etki alaninin, sunucu içeren bir tür çalisma grubu oldugu söylenebilir. Bilgisayarlar arasinda kablolardan daha fazla baglanti olan, baska bir deyisle, ortak bilgi gereksinimleri ve çalismalari olan kullanicilarin mantiksal bir gruplamasidir. Amaç hâlâ, kullanicilarin kendi gruplari içinde kaynaklari paylasmalarina izin vermek, böylece grup üyelerinin birlikte ve verimli çalismalarini kolaylastirmaktir. Bir etki alanindaki temel fark, agin tek bir noktasinda yönetime ve denetime izin veren bir sunucunun varligidir.

Bir Windows NT Server agi, tek bir etki alanini veya birbiriyle baglantili birçok etki alanini içerebilir. Ikinci durumda, birbirinde bagimsiz is istasyonlari, belirli erisim gerekleriyle, belirli etki alanlarinda gruplandirilmislardir. Etki alani kavraminin gerçek güzelligi, tayfin her iki ucundaki etki alani modellerini ve aradaki bilesen ve degiskenleri destekleyecek sekilde kolayca büyüyüp küçülebilmesidir.

**Windows NT Etki Alani Modelinin Üstünlükleri**** ******

Windows NT agi etki alani modelinin üstünlükleri sunlardir:

• Esnek tasarim yapilandirmasi

• Merkezilesmis ag yönetimi

• Yeni kullanici eklenmesinde ve erisim kisitlamalarinin degistirilmesinde esneklik

• Kullanici hesaplari için tek bir veritabani

• Tüm bir etki alani için tek bir birlesik güvenlik sistemi

• Dosya ve dizinlerin istege bagli erisim denetlemesi

Es düzeydeki agi sürdürmek için gereken makine temelinde yönetim, bir çalisma grubunun verimli olarak ulasabilecegi en büyük boyutu ciddi bir biçimde sinirlamaktadir. Windows NT Server sisteminde ise sinirlamalar, yalnizca isinizde hangi bölümlemelerin anlam tasidigina baglidir. Tüm bir sirket, tek bir Windows NT Server etki alani olarak yönetilebilir. Sirketinizin tüm kullanicilari tek bir çati altinda olsa ve erisebilecekleri kaynaklara göre kullanicilari gruplamak gerekmese de, aginizda istediginiz kadar bilgisayar ve buna karsilik tek bir yönrtsel denetim noktasi olabilir. Ayrica, tüm kullanicilar, en yenisi bile, kendi etki alani üzerindeki herhangi bir bilgisayardan erisebilir. Dosya ve dizinler için erisim izni, her bir kullaniciya verilmistir, tek tek bilgisayarlara degil.

Etki alani yapilandirilmali bir agda sistem yöneticisi olarak siz, agdaki herhangi bir bilgisayardan sistem degisikliklerini yapabilirsiniz. Basitçe, etki alanindaki herhangi bir Windows veya Windows NT Server bilgisarinda oturum açabilir ve amaçlanan degisiklikleri yapabilirsiniz. Hatta bu yolla kullanicilar ekleyip, silebilir veya erisim sinirlamalarini degistirebilirsiniz. Tüm degisiklikler tek bir yönetsel denetim noktasina yapilir ve daha sonra tüm etki alaninda hizla yerine getirilir, çünkü Windows NT Server, kullanici hesaplari veritabanini tüm etki alani boyunca otomatik olarak uyarlar. Bu, veritabanini makine makine yenilemek zorunda kalmayan sistem yöneticisinin basagrilarini büyük ölçüde azaltir.

Windows for Workgroups aginda, çalisma grubundaki diger üyelere bir bilgisayarin kaynaklarini açabilmek için yapabileceginiz seçimler sinirlidir. En basit düzeyde, is istasyonundaki bir kullanici, bilgisayarin kaynaklarini digerleriyle ya paylasacak ya da paylasmayacaktir. Bir sonraki düzeyde, söz konusu bilgisayara erisim saglayan bir parola atayabilirsiniz. Bu, belirli makinelere kullanicilarin bireysel erisimini denetlemek için sinirli bir olanak saglar. Yine de parolasi olmayan herhangi biri tarafindan bir bilgisayarin kaynaklarina fiziksel anlamda erisilemeyecegi anlamina gelir. Ayrica, her kullanicinin kendi dosyalarina erisim için bir parola gereksinmesi durumunda, bazi kullanicilarin birkaç farkli parolayi hatirlamalari gerekecektir.

Windows NT Server, istege bagli erisim denetimi olarak bilinen denetimi saglamak için ag sisteminin esnekligini arttirmistir. Bu sistemde, her kullanicinin diger bir kullanicinin kaynaklarina yapacagi erisim düzeyi kesin sekilde belirlenebilir. Tek bir dosya, bir dizin içindeki dosyalar veya bir dizinin tümü için kullanici erisimi saptayabilirsiniz. Windows NT Server, mümkün olan en ayrintili ve genis seçimleri yapabilmenizi saglar. Her kullanici için yalnizca bir parola gerektirir. Kullanici erisim denetimine sahip Windows NT Server sisteminin bir örnegi, bazi kullanicilarin varolan bir belgede degisiklik yapabildikleri, bazilarinin yalnizca belgeyi okuyabildikleri, diger kullanicilarin ise belgeyi bile göremedikleri bir etki alanidir.

**Etki Alani Bilesenleri**** ******

Normal bir etki yapilandirilmasi, isletim sistemleri, sunucular ve is istasyonlari bir araya geldigi bir yapi olabilir.

Bir ağ etki alanı örneği

**Birincil EtkiAlanı Denetçisi**** ******

Birinciletki alanı denetçisi (primary domain controller), bir etki alanındaki en önemli bilgisayardır. Etki alanı için güvenlik politikalarını uygular ve hesap veritabanı için de ana depodur. Aynı zamanda etki alanının paylaşılan kaynakları için birincil tutucu da olabilir; ancak, birincil etki alanı denetcisinin bu işlevi yerine getirmesi için gerekli değildir, hatta istenmiyen bir durum olabilir.

Kullanıcı hesabı veritabanındaki değişiklikler yalnızca birincil etki alanı denetçisinde yapılabilir, daha sonra bu değişiklikler, veritabanının salt okunur kopyalarının tutulduğu yedek etki alanı denetçilerine otomatik olarak yayılır. Yönetici olarak oturum açtığınızda birincil etki alanı denetçisinde çalışıp çalışmadığınıza bakılmaksızın, tüm değişiklikleriniz birincil etki alanı denetçisinin veritabanına yapılır. Kullanıcı hesaplarını yönetmek için kullandığınız araç User Manager for Domains'dir. User Manager for Domains'i çalıştırdığınızda hangi sunucuya oturum açacağınızı seçmezsiniz, sadece yönetmek istediğiniz etki alanını seçersiniz.

Birincil etki alanı denetcisi ağ üzerinde olmasa bile, bir veya daha fazla yedek etki alanı denetcileri yaratmışsanız ve bunlardan en az biri ağ üzerindeyse, kullanıcılar ağa oturum açmaya devam edebilirler. Bununla birlikte, birincil etki alanı denetcisi ağa dönmediği veya yedek etki alanı denetçilerinden birini birincil etki alanı denetçisine dönüştürmediğiniz sürece, etki alanında kullanıcı veya grup hesaplarını değiştiremez veya etki alanından kullanıcı ve grupları kaldıramazsınız.

User Manager for Domains

**Yedek Etki Alanı Denetçisi**** ******

Windows NT Server etki alanının, bir veya daha fazla yedek etki alanı denetçileri olabilir ve birçok durumda olmalıdır da. Her yedek etki alanı denetçisi, hesap veritabanının bir kopyasını içerir; kullanıcılar sisteme oturum açtıklarında onları onaylayabilir ve kaynaklara kullanıcı erişimini yetkilendirebilir. Bu, birincil etki alanı denetcisinin çökmesi olasılığına karşı sistemdeki paylaşılan önemli kaynakların artıklığını (redundancy) sağlar. Yedek etki alanı denetçilerinden bir tanesi birinci etki alanı denetçisi olarak değiştirilebilir ve ağ, normal olarak işlemeye devam eder. Sınırlı sayıda kullanıcının yer aldığı küçük bir etki alanında, yedek etki alanı denetcisinin bulunması şart olmasa da, iyi olabilir. Ağda, yalnızca birincil etki alanı denetcisi bulunuyorsa ve o sunucuda kullanılabilir değilse, tüm ağ devredışı kalacaktır. Windows NT Server ile çalışan bir bilgisayar, birincil ve yedek etki alanı denetçisi olabilir ya da ikisi de olmayabilir. İş istasyonu olarak işlev görecek bir bilgisayar için Windows Nt Server yerine başka bir işletim sistemi kullanmak daha iyidir. İş istasyonunun kullanımı, daha kolay ve hızlı olur.

**İş İstasyonu ******

İş istasyonları, MS-DOS, OS/2, Microsoft Windows 3.x, Windows for Workgroups, Microsoft Windows 95, Microsoft Windows NT Workstation ve Macintosh OS ile çalışabilirler. MS-DOS, OS/2, Macintosh OS, ve Windows 3.x ile çalışmak için istemci yazılımlarına ihtiyaç vardır. Diğerleri gerekli ağ yazılımlarını, temel işletim sisteminin bir parçası olarak içermektedirler.

**
Güven İlişkileri**** ******

İki veya daha fazla etki alanını içeren bir ağda, her etki alanı kendi hesap veritabanıyla ayrı bir ağ gibi hareket eder. En katı biçimde katmanlara ayrılmış bir örgütlenmede bile, bir etki alanındaki bazı kullanıcıların başka bir etki alanındaki kaynakların hepsini veya bir kısmını kullanma gereksinimleri olabilir. Etki alanları arasında kullanıcı erişim düzeylerini yapılandırmanın olağan çözümü güven ilişkisi olarak adlandırılır. Windows NT Server, bir yandan kullanıcıları ayrıntılı yordamlar ve çoklu parolalarla uğraşma yükünden kurtarırken, bir yandan da hassas kaynak alanını koruyan etki alanı denetçileri arasında güven ilişkileri olan bir çoklu etki alanlı ağı kurmak için gereken araçların tümünü sağlar.

**Etki Alanı Modelleri**** ******

Windows NT Server'ın dört tane etki alanı güven ilişkisi modeli vardır. Seçenekler dikkatlice düşünülür ve ağ stratejisi ona göre planlanır. Bu, ağ büyüdükçe, onu sürdürme ve genişletme kolaylığını sağlar.

• Tek etki alanı (single domain)

• Tek temel etki alnı (single-master domain)

• Çoklu temel etki alanları (Multiple-master domains)

• Tam-güven ilişkili etki alanları (fully trusted domains)

Ağınız sonuçta bu modellerden tıpkısı, biraz farklılaşmışı veya ağın farklı bölgelerindekileri iki veya daha çok modelin bir karışımı olabilir. Fakat temel yapı taşları aynı kalacaktır.

**Kullanıcı Hesaplarının Temelleri ******

Windows NT Server ağı kullanan herkesin, etki alanlarından biri üzerinde kullanıcı hesabının olması gerekir. Eğer kullanıcının hesabı, oturum açmak istediği etki alanında değilse, o etki alanına erişimine, sadece o etki alanı ile kullanıcı hesabının (user account) depolandığı etki alanı arasında güven ilişkisi varsa izin verilir. Bir kullanıcı hesabı, bir ad, bir parola ve kullanıcının ağı nasıl kullanacağını belirleyen sınırları içerir. Hesap, aslında, tüm ağ boyunca tek olan gizli bir güvenlik tanımlayıcısıyla (SID-security identifier) yaratılır; Windows NT Server, bir kullanıcıyı tanımlamak için kullanıcı adını değil, SID'i kullanır.

Kullanıcılar, benzer erişim hak ve izin dizilerine sahip yerel ve genel gruplar olarak gruplandırılırlar. Kullanıcı gruplar biçiminde organize etmek, bir işlemle tüm grubun hak ve izinlerini değiştirmenize olanak tanır.

**Kullanıcıların Gruplar Biçiminde Yönetimi ******

Windows NT Server, ağınızdaki kullanıcıları yönetmek için harika bir başlangıç noktası oluşturan bir dizi yerleşik yerel ve genel grupla birlikte gelir. Bu kullanıcı grubu özelliğinde yararlanarak çok sayıda kullanıcıyı bir defada kolayca yönetebilirsiniz. Aslında iki tür kullanıcı grubu vardır, yerel gruplar (local group) ve genel gruplar (global group). Bir yerel grup, sadece yaratıldığı etki alanı içinde yer alıp izinleri bulundurabilir; bir genel grup ise, yine bir etki alanında yer alır, ancak izinlerini tüm güven etki alanları boyunca koruyabilir. Kendi istediğiniz ve gerek duyduğunuz izinler dizisini içeren özelleşmiş yerel ve genel grupları kolaylıkla yaratabilirsiniz.

Bir grubu ve onun için gerekli izinleri birkez kurduğunuzda, yeni kullanıcıları hızla ekleyebilir veya grup için izinleri ayarlayabilirsiniz. Örneğin, maaş veritabanını kullanan ve bordroların yazımını üstlenen bir kullanıcı grubu yaratıyorsanız, yeni bir yazmanı gruba kolaylıkla ekleyebilirsiniz; yazman, gerekli tüm izinlere ve kaynakların konumlandırıldığı etki alan(lar)ı için erişime otomatik olarak sahip olacaktır.

İyi düşünülmüş bir grup yapısı, istenmeyen erişimi engellediği gibi, yönetim için harcanan zamanı da azaltır. Yerleşik gruplar, size önceden tanımlanmış bir grup yapısı sağlar.

## **DHCP (Dynamic Host Configuration Protokol=Dinamik Bilgisayar Konfigurasyon Protokolü) ******

TCP/IP protokolünü kullanan aglarda ikisi gerekli olmak üzere bes adet parametre kullanilir.. Bunlar IP, Subnet Mask, Gateway, DNS ve WINS dir. Bunlardan IP ve Subnet'in degerinin mutlaka girilmesi gerekir.

Ancak bir network üzerinde makine sayisinin artmasi sonucu bu degerlerin girilmesi hem zorlasir hemde hatali girilmesi sonucu makinelerin baglanti sorunlariyla karsilasiriz. Bu sorunu çözmek için olusturulan bir server üzerine DHPC (Dynamic Host Configuration Protokol=Dinamik Bilgisayar Konfigurasyon Protokolü) adi verilen bir servisin kurulmasi sonucu gerekli olan bütün konfigurasyon degerlerinin diger makinelere otomatik olarak baglanmasini saglamis oluruz. Bunun için networke bagli statik IP(Internete çikista kullanacagi legal IP degeri) ve gerekli degerleri dogru girilimis bir makine üzerine DHPC Prokolünü kurduktan sonra networkte bulunan diger client makineler IP degerleri bos birakilip bu degerleri DHPC üzerinden isterler. Client bu istegi verdikten sonra DHCP IP araligindan seçilen bir IP degeri belirli bir zaman araliginda bu clienta kiralar. Ve en son olarak client aldigi IP numarasini onayladiktan sonra o tarih araliginda client'a o IP atanir ve süre sonunda IP numarasi geri alinir.Ve ondan sonra istenirse tekrar bir IP verilir. DHPC server'in genel çalisma prensibi bu sekildedir.

Her hangi bir client'in aldigi IP adresini komut satirinda

C:\\ipconfig

Komutunu yazarak IP adresini, Subnet Maskini ve Default Gateway'ini ögrenebiliriz.Daha ayrintili bilgi istersek yani kartin MAC adresini, Host ismini (makine adi), DNS ayarlari gibi bu sefer ise

C:\\ipconfig /all yazmamiz yeterlidir.

DHPC 'den eger bir client bir IP numarasi aldiysa

C:\\ipconfig /release komutuyla aldigi bilgileri birakmasini saglayabilir
C:\\ipconfig /renew yazarsak tekrar yeni bir deger almasini saglayabiliriz..

**DHCP SERVER KURULUMU VE KONFIGURASYONU ******

DHCP servisinin kurulmasi için statik IP'si olan ve bir NT Server makine üzerine Control Panel içindeki Network Objesi altindan Services tabindan Add.. Buttonuna basarak yeni bir servis olarak DHCP Servisini ekleriz.Ve makine restart edilir. DHCP Servisi kurulmus olur daha sonra konfigurasyonuna geçelim. Istemcilere verecegimiz IP adres havuzunu tanimlamaliyiz. Daha sonra istemcilerin kullanacagi subnet mask degerini girmemiz gerekir. Ama bazi durumlarda server gibi kullanilan makinelerin kendine ozgu IP degerleri olabilecegi için onlarin adreslerini statik olarak vermek ve IP havuzundan çikarmamiz gerekir. Bazi makinelerinde hep ayni IP'yi almalarini istersek kendilerine ozgu IP degerlerini rezerve ederiz. DHPC server servisini konfigure etmek için Administrator Tools menüsü altinda DHPC Manager menusu kullanilir.

DHCP sunucu hizmetinin konfigurasyonu için ilk olarak bir scope tanimlanir. Scope DHCP'nin degitacagi IP degerlerinin araligidir. Eger ag birbirlerine router dedigimiz yönlendiricilerle birbirine bagliysa bu durumda scope sayisi birden fazla olabilir.

Simdi artik DHCP konfigurasyonuna geçebiliriz. Ilk olarak Administrator Tools arltindan DHCP Manager çalistirilir. Local Machine üzerine tiklanarak Scope menusunden Create diyerek yeni bir scope olusturalim. Daha sonra Start Adress olarak istemcilere verecegimiz IP'lerin ilk degerini ve End Adress kisminda verilecek son IP degerinin yazalim.Subnet mask için ag üzerinde kullandigimiz subnet mask degeri girilir. Excluded Adresses kisminda, verdigimiz IP araligi içindeki bir grup IP degerini çikarmak için kullanilir. (Bu degerler statik olarak kullanildigi için bunlari hariç tutmamiz gerekir ) Lease Durationda ise client"a verilen IP degerinin ne kadar sonra geri alinacagi degeri girilir. Bu degeri çok degisen IP degerlerine göre 3-5 gün arasinda vermek uygun olur. Name kisminda scope'un ismi Comment 'te ise ilgili yorum bulunur.
Bu degerleri girdikten sonra OK 'e basildiktan sonra sonra bu scope'u aktif edip edilmeyecegi sorulur. Buna Yes dersek scope aktif hale gelmis olur. Manager 'da aktif olan scopelar yaninda sari lambayla ifade edilir. Aktif olmayanlarin yaninda lamba bulunmaz.
Scope tanimlandiktan sonra IP ve subnet maske bilgilerini direk olarak clientlara yollamis olduk bundan sonra diger bilgileri yani default gateway, WINS ve DNS server IP Bilgilerinide DHCP tarafindan yollayabiliriz. Bunun için DHCP Manager'dan DHCP Option'I seçiyoruz. Burada yapilan konfigurasyonlar bütün scopelari yada seçili bir scope'u etkileyebilir.DHCP üzerinden bir scope seçildikten sonra DHCP Options menüsünden Global veya Scope seçilir. Burada Unused Options kisminda daha önce tanimlamadiginiz ve tanimlaya bileceginiz degerlerin listesidir. Bunlardan en çok kullanilanlari asagida verilmistir.

| 003 | Router | Router'ın adresi yani default gateway değeri |
| --- | --- | --- |
| 006 | DNS Servers | DNS Server adresi girişi |
| 044 | WINS/NBNS | WINS Sunucunun adresi |
| 046 | WINS/NBT node type | NETBIOS isim çözümlemesinin tipi girilir. |
| 047 | NetBIOS Scope ID | NetBIOS Scope ID'si tanımlanır. |

## **Windows NT'ye Genel Bakış ******

Microsoft NT işletim sistemi, Windows NT 3.1 adıyla sunulan 1993'teki sürümünden bu yana, ağ işletim sistemleri için standart belirleyici olmayı vadetmiştir. İlk sürümünün kullanışsızlığına karşın, bu işletim sisteminin özellikleri ve işlevselliği daha sonra sürekli olarak gelimiştir. Büyük reklam kampanyaları Microsoft'un gündemdeki işletim sistemi Windows 95 ile ilgilenirken, Windows NT'ye bir takım yeni özellikler ve işlevler, gürültülü olmasa bile düzenli olarak eklenmiştir. Ağ yazılım uzmanları bu ilerlemeyi ve her yeni ilerlemeyle birlikte gelen kazanımları da farketmişler, ancak hiçbir zaman Windows NT'yi ağ işletim sistemleri içinde bir lider olarak ilan etmeye hazır olmamışlardır. Windows NT sürüm 4'ün gelişmesiyle bu durum değişmiştir.

Windows NT'nin 4. Sürümü, Windows 95'den gelen kullanımı kolay grafik arabirimleri kendisiyle bütünleştirmesi, hem de farklı coğrafi konumlardaki kullanıcılarla kurulacak bağlantı sorunlarına getirdiği çözümler açısından, ağ işletim sistemleri içinde oldukça büyük bir gelişimi temsil etmektedir. Tüm kullanıcıların bağlantılarını yaptıktan sonra da, bilginin paylaşımı için insanların çalışma biçimlerinde kökten değişiklikler yapacak olan, yeni ve güçlü birtakım araçlar da sağlamaktadır.

Dahası, teknolojik mekanizmanın tümü, daha önce olduğundan çok daha kolay bir biçimde denetlenmekte ve yapılandırılmaktadır. Windows NT Server'ın 4. Sürümü zahmetsiz bir yönetime doğru adımdır.

**Sunucu ve İstemci İşletim Sistemleri ******

Windows NT ağı, genellikle istemci/sunucu mimarisi olarak adlandırılan merkezleşmiş bir ağ işletim sistemini kullanır. Ağ işletim sisteminin büyük bölümünün çalıştırıldığı merkezi bilgisayar, sunucu (server) olarak adlandırılır. Sunucu tarafından yönetilen kaynakları kullanan bilgisayara ise istemci (client) denir. Böylece bir ağdaki tüm bilgisayarlar, sunucu ya da istemci olarak görevlendirilmişlerdir; sunucular hizmet sağlar, istemciler de bu hizmetleri kullanırlar.

Her bilgisayar, bir işletim sistemi gerektirir. Ancak, bir ağ sunucusu ile bir ağ istemcisinin gereksinimleri genellikle çok farklı olmaktadır. Bir sunucu, bir kişisel PC işletim sistemi tarafından normal olarak kullanılan işlevlere ek olarak, şu işlemleri de yönetmelidir:

• Uzak dosya sistemleri

• Paylaşılan uygulamaların çalıştırılması

• Paylaşılan ağ aygıtları için girdi ve çıktı

• Ağ bağlantılı işlemlerin CPU zamanlaması

• Ağ güvenliği

Ağ sunucusu, sunucuya özgü ek ağ işlevleri için tasarlanan bir işletim sistemini kullanır. Bir sunucu düzinelerce ve hatta yüzlerce kullanıcı için yazdırma, dosya ve diğer hizmetleri sağlamak zorunda olduğundan, bir ağ işletim sistemi güçlendirilmiş ve sağlam olmak zorundadır. Birçok kullanıcı, işlerinin yapılması için sunucuya güvenir, bu nedenle sık yinelenen sistem hatalarını ve hatta reboot yapmak zorunda kalmak istemez.

Bir ağ istemcisi, iş istasyonu işletim sistemini kullanır, çünkü istemci işletim sistemi, sunucu işletim sistemi kadar dayanıklı olmak zorunda değildir. Bir iş istasyonunun yeniden önyüklemesi, kullanıcı için sıkıntı yaratabilir ama bir başkasının çalışmasını aksatmaz. Bir istemci için yerleşik bir güvenlik sistemi de gerekmez, çünkü istemcinin güvenliği ağ işletim sistemi tarafından sağlanmaktadır. Bir Windows NT Server ağındaki istemciler, MS-DOS, Microsoft Windows 3.1, Windows 95, Windows NT Workstation, UNIX, Macintosh OS ve OS/2 gibi herhangi bir işletim sisteminde olduğu gibi çalışırlar. Bununla birlikte, bir istemci işletim sistemi ne kadar gelişmiş olursa, güvenlik ve bilgi paylaşımı alanlarında ağ işletim sistemiyle işbirliği de o kadar iyi olur.

**Windows NT Sürüm 4'ün Özellikleri ******

Windows NT sürüm 4'ün görünüşü tümüyle yeni, yetenekleri de büyük ölçüde geliştirilmiş olsa da, sıfırdan başlamaz. Yeni görünümü ve yeni yetenekleri, Windows işletim sistemlerinin daha önce sürümlerinde oluşturulmuş özelliklerin temeli üzerine yapılandırılmıştır.

**Önceki Windows NT Sürümlerinden Gelme Özellikler **
Windows NT sürüm 4, Windows NT'nin önceki sürümlerinde geliştirilen özellikler temelinde yükselmektedir: Donanım bağımsızlığı, çoklu işlemciler için destek, çokgörevlilik, çoklu çalışma, güvenlik, RAID desteği ve NT dosya sistemi gibi.

**Dosya bağımsızlığı **
Taşınabilirlik veya mimari bağımsızlık olarak da bilinen donanım bağımsızlığı, Windows NT'nin yalnızca bir işlemci türü için tasarlanmadığı anlamına gelir. Gerçekte, ilk gerçekleştirilişi, bir Reduced Instruction Set Computing –RISC yongası (chip) olan MIPS R4000 üzerinedir. Windows NT Server'ın veya Windows NT Workstation'ın 4. Sürümünü şu işlemcilere yüklenebilir:

• Intel 80486, Pentium, Pentium Pro

• DEC Alpha RISC

• MIPS RISC

• Power PC

Windows NT'nin belirli bir işlemci için yazılan parçaları, hardware absraction layer HAL (donanım soyutlama katmanı) denilen, yazılımın küçük bir kısmına yalıtılmıştır. Microsoft'ta çalışan mühendisler, işletim sistemini yeni bir yongaya taşımak için; C kodunu yeniden derlemişler ve yeni bir HAL yazmışlardır. Bu, göründüğü kadar kolay değilse de, çok zor olduğu da söylenemez. Sonuç, maliyet ile başarım arasında, özel durumunuza en uygun dengeyi kuracak bir donanımı seçebilmektir.

**Çoklu işlemciler için destek **
Windows NT Server, simetrik çoklu işlemcili bilgisayarlarıda desteklemektedir; dört işlemcili bir bilgisayara yükenebilir. Windows NT Workstation ikiden fazla işlemcisi olmayan makinelerle sınırlanmıştır.

**Çokgörevlilik ve çoklu çalışma **
Çokgörevlilik, sizi birçok şeyin aynı anda olduğuna inandıran bir yanılsamadır. Gerçekte olan, işlemcinin birçok görev arasında hızla geçiş yapmasıdır. Çokgörevlilik, hızlı bir bilgisayarda ve onu iyi kullanan (Windows 95) bir işletim sisteminde, birçok şeyin aynı anda olduğu izlenimini veren oldukça inandırıcı bir yanılmasa yaratmaktadır. Windows NT, çokgörevliliği çok iyi kullanmakta ve her görevi diğerlerinden özenle ayırmaktadır. Bu, aksayan bir programın tüm sistemi bozmasını önlemek için gereklidir. Çökmüş bir uygulama, diğer görevleri veya sistemin kendisini etkilemeden kapatılabilir.

Bununla birlikte Windows NT, çoklu çalımayı gerçekleştiren uygulamalardan da yararlanabilir. Çoklu çalışma, bir uygulamanın çok sayıda yürütme yolunu -iş parçacığı (thread) kullanabildiği bir işlemdir. Çok işlemcili bir bilgisayarla işlem yaparken, iki iş parçacığı aynı anda çalışabilir. Başka bir deyişle çoklu çalışma, çok görevliliğin yapar gibi göründüğü şeyi gerçekte yapmaktatır.

**Güvenlik **
Windows NT server, yönetici tarafından herhangi bir ağ türü için yapılandırılabilen birçok güvenlik özelliği içerir. Ağ üzerindeki bilgi değerlidir ve korunması gereklidir. Ağ ne kadar büyük olursa, güvenlik de o denli önemli olur; sistem hataları ve kullanıcı sorunları üreyebilir. Ağ, her kullanıcının verisini donanım ve yazılım hatalarından korumalı, yetkisiz kullanıcıları dışarıda bırakıp yetkili kullanıcıları da yapmamaları gereken şeylerden uzak tutmalıdır.

**RAID desteği **
Redundant Array of Inexpensive Disks-RAID teknolojisi, sabit sürücülerin hata toleransını geliştirmektedir. Birçok durumda RAID olanağından yalnızca belirli bir donanımı satın alarak yararlanabilirsiniz. Windows NT Server yalnızca SCSI donanımı ve standart sabit sürücüler gerektiren bir RAID yazılım desteği sağlamaktadır.

**NT dosya sistemi **
NT File System (NTFS), Windows NT Server ve Windows NT Workstation ile kullanılabilmesi için tasarlanmıştır. Söz konusu dosya sistemi, daha önceden çalışmış olabileceğiniz File Allocation Table ( FAT) veya VFAT sistemlerinden oldukça farklıdır ve bir ağ ortamına çok daha iyi uyar. NTFS şu özellikleri içerir:

• Boşluklar dahil 255 karaktere kadar dosya adları ve çoklu uzantılar için destek.

• Kısa MS-DOS uyumlu dosya adlarının otomatik oluşumu.

• Sıcak düzenleme özelliği. Kötü disk bölümündeki veri otomatik olarak iyi bir bölüme taşınır ve kötü olan, hizmetten kaldırılır.

• Dosya ve klasörler için izinler belirlemenizi sağlayan yerleşik güvenlik.

• Disk hatası durumunda dosyaları geri yüklemek için kullanılabilecek günlük dosyası biçimindeki hata toleransı.

**Windows NT Sürüm 4'te Yeni Olan Özellikler ******

Windows NT'nin 4. sürümü, öncekilerde olmayan çeşitli özelliklere sahiptir. Bazıları tümüyle yenidir, bazıları ise Windows 95'ten alınmıştır.

**Microsoft Windows 95 kullanıcı arabirimi **
Windows NT'nin 4.sürümündeki en belirgin ve önemli değişiklik, Windows 95 kullanıcı arabiriminin uyarlanmasıdır. Yeni arabirim, program açmayı ve dosya bulmayı eskisinden çok daha kolaylaştırılmıştır. Yönetimle ilgili birçok araç ve yardımcı da, kullanımlarını kolaylaştıran yeni görünümler edinmiştir.

**Microsoft Internet Explorer Sürüm 3 **
Internet Explorer'ın en son ve en usta işi sürümü Windows NT'ye yerleştirilmiştir. Internet Explorer, işletim sistemiyle tümüyle bütünleştirilmiş basit ve hızlı bir Internet tarayıcısıdır.

**Microsoft Internet Information Server **
Windows NT Server sürüm 4'ün ayrılmaz parçası olan Internet Information Server (IIS), World Wide Web, ftp ve Gopher hizmetlerini kurup yönetmenize izin verir. IIS, Windows NT Workstation sürüm 4'teki yeni Peer Web Service ile birlikte çalışır ve kullanıların kendi kişisel Internet sunucularını yaratmalarına izin verir.

**Microsoft Exchange **
Microsoft Exchange, Internet postası ve Microsoft Mail'i uzlaştıran yerleşik bir ileti merkezidir. İletilere katıştırılmış biçimde dosya gönderip alınabilir. Ağa Exchange Server'ı ekleyerek, yerel ve dünya çapındaki ağlarla tam bir ileti ve bilgi paylaşım sistemi yaratılabilir..

**Telephony API **
Yeni Telephony API (TAPI) teknolojisi, Windows iletileme altsistemi (Exchange E-Mail Client), faks uygulamaları ve Internet Explorer tarafından kullanılmaktadır.

**İletişim kurallarındaki gelişmeler **
Windows NT Server'ın 4. Sürümünde bulunan Microsoft Point-to-Point Tuneling Protocol , uzaktaki kullanıcıların Internet üzerinden ağlarına güvenli erişimlerini sağlayan yeni bir teknolojidir. BOOTP iletisi içeren geliştirilmiş TCP/IP özelliklerini de bulunabilir. Bir diğer yeni özellik ise, DHCP (Dynamic Host Configuration Protocol) ve BOOTP'nin dolaştırılmasını geliştiren DHCP Relay Agent'tır.

**Ve daha fazla özellik... **
Bunlarda Windows NT sürüm 4'te bulunabilecek diğer yeni özelliklerdir:

• **DNS Name Server **
Windows NT Server, Domain Name System (DNS) ad sunucusu olabilir. Bu onun, ana bilgisayar adının çözümlenmesinde WINS'i kullanmak için yapılandırılabileceği anlamına gelir. Evrensel adlandırma anlaşması Universal Naming Convention (UNC), şimdilerde DNS adlarını desteklemektedir.

• **Multiprotocol Routing **
Windows NT Server 3.51 hizmet paketinin bir parçası olan çoklu iletişim kuralı dolaştırması (Multiprotocol routing-MPR) artık 4. Sürümle birleştirilmiştir.

• **DirectX **
Windows NT, DirectDraw sürüm 2, DirectSound sürüm 1 ve DirectPlay sürüm 1 için tam bir API desteği sağlamaktadır.

• **Windows 95 Masaüstlerinin Uzaktan Önyüklemesi **
Uzaktan önyükleme hizmeti "disksiz" Windows 95 masaüstlerinin kullanımını basitleştirmektedir.

• **Uzaktan Yönetim **
Uzaktan yönetim, yönetim görevlerinin Windows 95 masaüstünden yerine getirilmesi için bir dizi yeni araçtır.

• **Novell Netware ile Bağlantı **
Windows NT kullanıcıları NetWare Directory Services'ı (NDS) çalıştırarak Novell NetWare 4.x sunucularına erişebilirler. NetWare sunucusundaki paylaşılan nesneler, kullanımı oldukça kolay olan hiyerarşik bir sırada düzenlenmişlerdir.

**Windows NT Server İçin Donanım Gerekleri ******

Windows NT Server sürüm 4 güçlü bir işletim sistemi olduğu için, doğal olarak güçlü bir bilgisayarı gerektirir. Kimi sunucular daha fazla, kimileri ise daha az güçlü donanımlar gerektirmektedir.

Aşağıdakiler, bir sununcu için temel donanım gerekleridir:

• Bir Intel 80486/66 veya daha yükseği, bir Intel Pentium, Power PC, Digital Alpha AXP veya MIPS R4x00 gibi bir desteklenmiş RISK işlemcisi. Windows NT Server bilgisayarları en fazla 4 mikroişlemciye kadar destekler. Windows NT server ile çalışan bir işlemci için en küçük değer 80486/25 olsa da, etki alanı denetcisi veya dosya sunucusu rolündeki bir bilgisayarın en az bir Pentium mikroişlemcisi olmalıdır. 80486/66, NT Server ile çalışan diğer herhangi bir bilgisayar için en gerçekçi minimum değerdir.

• Windows NT Server sistem dosyalarının bulunucağı bölmede en az 123 MB sabit disk alanı. RISC tabanlı bilgisayarlar için, sabit sürücü bölmesi üzerinde en az159 MB sabit disk alanı olmalıdır.

• VGA ya da daha iyi bir ekran.

• Ağ üzerinde yükleme yapmayan herhangi bir bilgisayar için, desteklenmiş bir CD-ROM sürücü. Intel x86 tabanlı bir bilgisayar için, desteklenmiş CD-ROM sürücüsüne ek olarak bir 3.5 inç yüksek yoğunluklu disket sürücü.

• x86 tabanlı bilgisayarlar için en az 12 MB RAM; 16 Mb önerilen, 32MB ise en iyi olandır. RISC tabanlı bilgisayarlar için en az 16 MB RAM; 32 MB yeğlenmelidir.

• Fare veya başka bir imleme aygıtı.

• Desteklenmiş bir ağ kartı.

## **POP ve SMTP protokolleri nedir, nasıl çalışır ? ******

O karmaşık e-posta haberleşmesinin nasıl çalıştığını hiç düşündünüz mü? Üstten bakışla ne kadar karmaşık görünüyor değil mi. Oysa, gerçekte, hiç te o kadar zor sayılmaz. Öncelikle sistemin nasıl çalıştığını bilmek gerekir.

E-posta sistemi 2 bölümden oluşur

1-Post office protokol(POP3): POP3 bizim posta kutumuza gelen mesajları oradan almamız için e-posta programımızla (Netscape Messenger veya Outlook Express gibi.) abonesi olduğumuz POP3 server'i arasında geçen konuşup anlaşma protokulüdür. Bu protokolün nasıl işlediğini kendimiz de, e-posta programı kullanmadan TELNET vasıtasıyla görerek deneyebiliriz. Ayrıca bu bize başka yararlar da sağlayacaktır. Örneğin e-mail programıyla alamadığımız bazı postaları hiç almadan posta kutusundan silmemiz mümkün olacaktır. Ya da kendi SMTP server'imizi hiç kullanmadan istediğimiz birisinin posta kutusuna kısa mesajlar bırakabiliriz.

POP3 protokolü sırasında e-mail programı bazı standart komutlar kullanmak zorundadır. Bunlar:

**USER <KullanıcıAdı> : **Bunu yazarak POP3 server'e hangi kullanıcı olarak bağlandığımızı belirtmiş oluruz. Örneğin

>USER aguler /Bizim yazdığımız
Bu kullanıcı server'de tanımlıysa Server'in yanıtı,
<+OK welcome aguler
eğer bu kullanıcı olmasaydı
<-ERR …
şeklinde olacaktır. (Bazı server'ler kullanıcı yoksa hatayı PASS komutundan sonra verirler.)

**PASS <Parola> : **Bunu yazarak bağlanılan kullanıcının parolasını veririz. Eğer parola yanlışsa bağlanamayız. Örneğin

>PASS ozelbisiy
doğruysa
<+OK …
yanlışsa
<-ERR invalid password (veya –ERR …)
şeklinde yanıt verecektir.

**STAT : **Posta kutumuzun durumunu almak için kullanılan komuttur. Yani posta kutusunda kaç mesaj var ve toplam büyüklüğü nedir, sorularının yanıtını bu komutla alırız.

>STAT
<+OK 0 0 Posta kutusunda hiç mesaj yokmuş
veya
<+OK 6 15978 Posta kutusunda 6 adet mesaj varmış ve toplam büyüklüğü 15978 (byte|octet)
miş

**LIST \[MsgNo\] : **Mesajların listesini ve her birinin büyüklüğünü verir. Eğer MsgNo yazılırsa aynı işlemi sadece o nolu mesaj için yapar.
Mesaj nosu yazmadan komutu verirsek

>list
<+OK 11 messages (218146 octets)
<1 940
<2 7044
<3 165064
<4 863
<5 1907
<6 907
<7 2500
<8 2091
<9 4445
<10 1223
<11 31162
<.

Şeklinde bir liste verir bize ve en sonunda da bittiğini göstermek için sadece ilk kolonunda . (nokta) olan bir satır gönderir. Böylece biz (e-mail programı anlar ki tüm mesajlar bunlarmış.)
Mesaj nosu yazarak (1 nolu mesaj) komutu verirsek

>list 1
<+OK 1 940

**UIDL \[MsgNo\] : **Her mesajın, başka bir mesajda aynısı olayan (benzersiz, unique) bir kodu vardır. Bu komut bize o kodu verir. Özellikle e-mail programlarında (örneğin Outlook Express 5'te Tools|Accounts|<xx internet account> Properties menüsünde Advanced sayfasındaki
Leave a copy of messages on server işaretlendiğinde aldığın mesajları posta kutusundan silme, kalsın anlamına gelir. Dolayısıyla tekrar bağlanılıp mesajlar alınırken Outlook Express 5 daha önce aldığı mesajları işte bu mesaj ID'si yardımıyla tesbit ederek onları birdaha tekrar almaz. Eğer mesajlar Outlook Express Inbox'tan ve Deleted Items'dan silinirse aynı mesajları tekrar alacaktır. Eğer Leave a copy of messages on server İşaretli değilse Outlook Express bu kontrolu yapmaz, dolayısıyla herhangi bir nedenle bağlantı kesilirse daha sonra mesajları tekrar çekmeye kalktığımızda aynı mesajları tekrar alacaktır.
Komutlar Telnetten yazılırsa

>uidl
<+OK
<1 4cf6ef281a0eaae6f906669ad5d097e9
<2 49ba75aeb7a13ad9925979c91b8b67fe
<3 74af7f5470ec50e639c5c0e750b99e99
<4 c335fced9d3004aa794e636646ed84c9
<5 B0003006265.MSG
<6 <001201bedd74$05a07820$3c14a8c0@veronique.gozenair.com>
<7 84fe916939f91687ad3487c45237cfce
<8 2691d46fc915d63f488e797fb860ba7e
<9 B0003018571.MSG
<10 <000c01bedda9$93690f20$3c14a8c0@veronique.gozenair.com>
<11 B0003020608.MSG
<.
>uidl 1
<+OK 1 4cf6ef281a0eaae6f906669ad5d097e9

şeklinde sonuçlar alınacaktır.

**TOP <MsgNo> <SatırNo> : **Belirtilen numaralı mesajın satır nosu olarak verilen en üstten (mesaj gövdesi başladıktan itibaren) o kadar satırı server'den okumak için kullanılır. Server en sonunda ilk kolonunda nokta olan bir satır gönderir. Böylece gönderimin bittiği anlaşılır.

>TOP 5 1
<……
<…..
<…..
<.

**RETR <MsgNo> : **Belirtilen numaralı mesajın tümünü almak için bu komut verilir. Server mesajın sonunda, ilk kolonunda nokta olan bir satır gönderir. Böylece mesajın bittiği anlaşılır.

>RETR 5
<……
<……
<……
<.

**DELE <MsgNo> : **Belirtilen mesajı sil komutudur. Örneğin 5 nolu mesajı silmek için

>DELE 5

yazdığımızda

<+OK
yanıtını veren server 5 nolu mesajı sildiğini bu şekilde belirtecektir.

**QUIT : **Server'le bağlantının kesileceği komutunu verir. Bu komut verilir verilmez Server posta kutusundaki güncellemeleri yaparak bağlantıyı keser. Bağlantı başka şekillerde (örneğin Telnet penceresini kapatarak veya menüden Disconnect'e basarak) kesilirse çoğu server'de posta kutusu güncellenmez, dolayısıyla QUIT komutuyla çıkmaya dikkat etmek gerekir.

>QUIT
<+OK ………
ve bağlantı kesilir, Telnet penceresi boşalır.

**LAST : **Son mesaja konumlanmayı sağlar. Çok kullanılmayan bir komuttur.

**RSET : **Bir server'den bağlantıyı kesmeden başka bir kullanıcı ile login olmayı sağlar. Örneğin

>USER agil
<+OK …..
>PASS ghtj
<+OK
>LIST
<+OK 0 messages (0 octets)
<.
>RSET
<+OK
>USER ggg
<+OK …..
>PASS hhhh
<+OK ….
>LIST
<+OK 0 messages (0 octets)
<.
gibi.

**NOOP : **İşlem yapma demek. Ne için kullanıldığını bilmiyorum. Bir işe yarıyordur mutlaka ama önemli olduğunu sanmıyorum. Belki yeni serverler buna hata mesajı veriyor olabilirler. Bunun için ilgili RFC'ye bakmak lazım. Uzun iş…

Tabii bunların sonucunda şu soru sorulabilir.
"Biz tüm bunları yapıyoruz ama bunların hepsi Text formatında ve şifrelenmemiş yazılar tarzında, bu hacker'lar için bir ziyafet değil mi ?"
Ne yazık ki bu doğru! Adamcağızlar uğraşmış didinmişler ve son derece esnek (bana göre) harika bir sistem kurmuşlar. Şimdi hacker'lar yüzünden bunu değiştirecek miyiz. Bence gerek yok. Onlara karşı en iyi korunma mesajların ulaşılmaz derecede çok olması olacaktır. İnternette o kadar çok mesaj dolaşıyor ki garipler hangi birini inceleyecekler.

## **PRIMARY DOMAIN SERVER KURULUMU: ******

## **Nt Server Yüklenmesi : ******

**Sistem Gereksinimleri **
Windows Nt yüklenecek bilgisayarlarda minumum bulunmasi gereken donanimlar asagida çikarilmistir. Bunlar Nt yüklenebilecek minumum gereksinimlerdir. Daha güçlü özelliklere sahip makinalarin üzerine kurulmasi önerilir.

| CPU | 32 bit Intel x86 tabanli (80486/33 veya daha yüksek) |
| --- | --- |
| RAM | Nt server için 16 Mb RAM |
| Harddisk | 16Kb cluster kullanan harddisklerde 120 Mb civarinda bos alan 32Kb cluster kullanan harddisklerde 200 Mb civarinda bos bir alan gerekmektedir. |
| Display | VGA |

**Nt Server Yüklenmesi : **

Kurdugumuz makinanin üzerinde su konfigurasyon bulunmaktaydi.

| CPU | Intel Pentium II-350 Islemci |
| --- | --- |
| RAM | 64 Mb RAM |
| HDD | 8 GB Quantum Harddisk |

Isletim sistemini 2 MB harddisk üzerine kuracagiz. Geriye kalan 6 GB üzerinde FTP ve WWW servislerinin bulunacagini varsaydik.

Windows Nt Server kurulumuna başlamadan önce asağıdaki kontrol listesini doldurmanız Windows Nt kurulumu sırasında size büyük kolaylıklar sağlayacaktır.

**Windows NT Server Kurulum Kontrol Listesi ******

| 1.Bilgisayarinizin Adi | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| --- | --- |
| 2.Yazicinizin Adi | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 3.Yazicinin Modeli | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 4.Network Kartinizin Tipi | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| IRQ Seviyesi | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Memory Base Address | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| I/O Port Address | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 5.Domain Adi | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 6.Administrator Account Setup | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| User Name | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Password | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 7.Zaman Dilimi | :\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

\[ \] Otomatik olarak günisigindan yararlanma zamani geçisi
\[ \] Sadece standart zaman
\[ \] Sadece günisigi tasarrufu zamani

Bunlara ek olarak asagidaki disketlere ihtiyaciniz vardir :
\[ \] Windows NT Setup Disketleri
\[ \] Windows NT CD-ROM Dagitim Diski
\[ \] "Emergency Repair Disk" diye etiketlenmis kurulum sirasinda yaratilacak yazilabilir bos bir floppy disk

Asagidaki adimlari izleyerek isletim sistemini yükledik:

1- Makinayi MS-DOS disketi ile A sürücüsünden açtik.
2- FDISK programini çalistirdik.
3- Ilk basta 2 GB'lik kismini FAT16 olarak primary disk yarattik.
4- Makinayi tekrar Reboot ettik.
5- Format c: diyerek birinci hardisk'imizi formatladik.
6- Makinayi tekrar reboot ediyoruz.
7- A sürücüsünden MS-DOS 6-22'yi install ettik.
8- Bu sefer makinayi reboot ederek harddisk'ten açtik.
9- CD-ROM sürücüsünün disketini A:'ya takarak setup dosyasini çalistirdik.
10- CD-ROM install ettikten sonra makinayi tekrar reboot ettik.
11- NT Server CD-ROM'unu CD'ye yerlestirdik.
12- CD'deki winnt dizinine geçtim.
13- I386 dizinini Harddisk'e kopyaladik.
14- Xcopy i386 c:\\\\i386 /s
15- Daha sonra Harddisk de I386 dizinine girdik.
16- Winnt /b komutunu vererek Nt server yüklemeye basladik.
17- Default path olarak burayi kabul ettik.
18- Daha sonra karsimiza gelen son kullanici anlasmasini pagedown tusuna basarak geçtim.
19- F8 tusuna basarak anlasmayi kabul ettim.
20- Enter tusuna basarak sistem üzerinde bulunan aygitlari onayladim.
21- C sürücünün üzerine yükleyecegimizi belirttik.
22- File sistemi degistirmeyecegimizi belirten seçenegi seçtik ve enter tusuna basarak bir sonraki adima geçtik.
23- Nt Server c:\\winnt dizinine yükleyecegimizi belirttik.
24- Enter tusuna bastik ve Setup HDD'yi test etti. Ve gerekli dosyalari HDD'ye kopyaladi.
25- Daha sonra gelen pencere A sürücüsünde eger disket varsa bunlari çikarmamizi ve makinayi tekrar baslatacagini bildirdi .Bizde Enter tusuna basarak islemi onayladik.
26- Windows NT Server yüklenmesinin 2. Adimi basladi.
27- Setup options penceresinden custom seçenegini seçtim.
28- Daha sonra gelen pencere kullanici ve organizasyon isimleri isteniyordu. Bu opsiyonlari doldurduktan sonra next tusuna bastik.
29- Daha sonra gelen pencerede NT key numarasini girdik.
30- Gelen pencereden PerServer opsiyonunu seçtik ve ayni anda 150 connections a izin verebilmesi için buradaki kutuya 150 degerini girdik.
31- Daha sonra gelen pencerede bu makinanin daha dogrusu server'in isminin ne olacagini yazmamiz gereken bir kutu vardi. Bu kutuya DOMAIN\_SRV ismini verdim. Next tusu ile bir sonraki adima geçtim.
32- Bu adimda Server'in tipini belirtmemiz isteniyordu. Burada üç seçenek bulunmaktaydi.

Birinci seçenek : Primary Domain Controller :

Domain üzerinde en yetkili ana makina olmasi seçenegi

Ikinci Seçenek : Backup Domain Controller :
Domain üzerinde bulunan Primary Domain Controller'in bir yedegi olacakti. Birinci makina üzerinde tutulan bütün kullanici ve sistem dosyalarinin bir yedegi alinmakta ve eger birinci server çökerse bu devreye girerek onun görevini yapacaktir.

Üçüncü Opsiyon : Stand-Alone Server :

Bu makina domain olarak yaratilmayacak. Yalniz basina çalisan bir server olacakti.
Biz bir Primary domain kuracagimiz için birinci opsiyonu seçtik.
33- Daha sonra karsimiza gelen pencere Administrator user için password girmemizi istiyordu. Bu user sistemdeki en güçlü kullanici olacak ve birçok islem bu kisi tarafindan yapilacakti. Password olarak girdigimiz ifadeyi ikinci kutuyada girdik.
34- Daha sonra önümüze gelen pencerede kurtarma disketi yaratip yaratmiyacagimiz soruldu. No seçenegini seçip disket yaratmayacagimizi belirttim.
35- Daha sonra karsimiza gelen pencereden yüklemek istedigimiz component'leri seçerek yükledik.
36- Next tusuna basarak Network islemlerine geçtik.
37- Karsimiza gelen pencereden Wired Network seçenegi seçili idi. Bu seçenek bu makinanin Network karti üzerinden sisteme baglanagini belirtiyordu.
38- Remote Access to the Network seçenegini seçmedik. Bu seçenek bu makinaya telefonla disardan baglanti yapilmasina izin veren bir opsiyondu. Next tusuna basarak bir sonraki adima geçtim.
39- Internet Information Server seçenegini seçmedim. Çünku biz bu serverdan disariya FTP ve HTTP seçeneklerini firewall ile kapattigimiz için IIS server installasyonunu geçtim.Gerekirse IIS 3.0 Server kurarak FTP ve WWW yükleyebilirdik.
40- Bu adimda Server üzerinde bulunan Network kartlarini tanitmamiz isteniyordu. Start Search buttonuna basarak bilgisayarin Network kartini aramasini baslattik. Makina Network kartini buldu. Next tusuna basarak bir sonraki adima geçtik.
41- Burada Network kartinin özelliklerini degistirebilecegimiz bir pencere idi. Ancak biz burada bir degisiklik yapmayarak Nt'nin detect ettigi gibi biraktik ve next tusuna basarak bir sonraki adima geçtik.
42- Bu pencere kullanacagimiz Network protokolerini seçmemiz isteniyordu. Buradan bütün protokoleri seçtim. Bu protokolerden TCP/IP internet protokolu IPX/SPX Novell tarafindan kullanilan protokol ve NetBEUI ise Microsoft tarafindan kullanilan bir protokoldür. Next buttonuna basarak bir sonraki adima geçtim.
43- IP adreslerini Subnet ve Gateway degerlerini girdik
44- Bu pencere makinaya yüklenecek servisleri seçmemiz gerekmektedir. Bunlarin hepsi seçili idi. Biz bunlari uncheck etmeden bir sonraki adima geçmek için next tusuna bastik.
45- Burada seçili component'leri yükleyecegini belirten bir bilgi veriliyordu. Yükleme islemini baslatmak için Next buttonuna bastik.
46- Daha sonra bir next buttonuna basarak seçilmis network componentlerini enable ettik.
47- Daha sonra gelen pencereden Domain adi olarak DOMAIN\_TEST ismini verdik.
48- Finish butonu ile NT yükleme islemlerini basari ile tamamladik.
49- Makina tekrar reboot ettikken sonra Time Zone listesinden Istanbul olarak seçtik Next buttonuna bastik.
50- Tarih ve zaman ayarlarini ayarladik. Close buttonu ile pencereyi kapattik.
51- Daha sonra gelen pencereden Display özelliklerini ayarladik. OK buttonuna
bastiktan sonra NT kurulumunu tamamladik.
52- Makinayi tekrar reboot ettik.
53- Makine açildiktan sonra 2 GB FAT ve geri kalan 6 GB\`i userlar tutulacagi için NTFS'e cevirdik.

## **Microsoft Exchange Server 5.0 ******

Kullanıcıların Netwok üzerinde ve tüm Internet kullanıcıları ile haberleşebilmelerini gerçekleştirmek amacıyla Microsoft Exchange Server 5.0'ın bilgisayara yüklenmesi ve kullanıcı mailbox'larının yaratılması , adres listeleri oluşturulması ,genel kullanıcı kısıtlamaları nın nasıl yapılacağını burada anlatmaya çalışacağız.

**Exchange Server Kurulumu : ******

1- Exchange Server Cd-ROM'nun CD'ye taktık.
2- E sürüsücüde geçtik. "E:"
3- Exchange dizini altındaki I386 dizinine girdik.
4- Buradan Setup.exe dosyasını çalıştırdık.
Karşımıza Exchange setup penceresi geldi.

5- OK butonuna basarak devam ettik.
6-Daha sonra karşımıza Exchange Server nasıl yüklemek istediğimize dair bir pencere çıktı. Bu pencere aşağıda da görülmektedir.

7-Burada change directory butonuna basarak programı yüklemek istedigimiz sürücüyü seçtik.
8-Daha sonra Custom/Complete butonuna basarak özel kurulum yapacağımızı belirttik

9- Karşımıza gelen pencerede hangi programları yüklememiz gerekecegini seçecegiz.
10- Biz buradan Active Server Components uncheck ettik.
11- Continue butonuna basarak devam ettik.
12- Daha sonra CD-KEY degerini girdik.
13- Üstede görüldügü üzere karşımıza gelen pencereden Server tipini ve license sayısını girmemiz isteniyordu.
14- Buradaki Add License butonuna basarak exchange server'dan hizmet alabilecek kullanıcı sayısını tanımladık.
15- Quantity alanına 5000 girdik. OK butonuna bastım.
16- Karşımıza License anlaşmasını kabul edip etmedigimize dair bir pencere geldi. Anlaşmayı kabul ettik.
17- Continue butonuna bastık.

19- Biz yeni bir site yaratacaktık. Onun için ikinci seçenegi seçtik.
20-Karşımıza gelen pencere organization ve site adı sorulmaktaydı. Bunlara değerlerini girdik

21- OK butonuna bastık ve yeni bir site yarattık.
22- Site server'ının yöneticisi olarak şu anda bu programı yüklemekte olan kullanıcı olarak girdik.
23-Karşımıza gelen pencereden bu kullanıcı için password girdik.

24- Artık Exchange server gerekli dosyaları harddisk'e kopyalamay başladı.
25- Dosyaların yüklenmesi bitince karşımıza gelen pencereden Run Optimizer butonuna tıklayarak Exchange optimizer'ını çalıştırdık.
26-Buradan karşımıza yeni bir pencere geldi. Bu pencere optimizer hakkında bilgi vermekteydi
27-Buradan Next butonuna basarak bir sonraki adıma geçtik.
28-Bu adımda bu server'dan nasıl hizmet alınabilecegini belirten seçenekleri girmemizi istiyordu.
29- Users on This Server bölümünde bu server'dan aynı anda hizmet alabilecek kullanıcı sayısını belirtmek için seçenekler bulunmaktadır.
30- Biz bu seçeneklerden 101 ila 250 kullanıcıya kadar hizmet verebilecegini belirttik.

31-Server tipi olarak bazı seçenekler sunulmaktaydı. Biz bunlardan Private ve public depolama ortamı olmasını ve aynı zamanda Multiserver olması seçeneklerini seçtik.
32- Üçünçü bölümde ise kaç kullanıcının bu organizasyonda bulundugunu girmemizi isteyen bir seçenek vardı. Biz buraya 1000 ile 9999 olarak girdik.
33- Next butonuna basarak bir sonraki adıma geçtik.
34-Disk analizleri işlemleri bitti. Next butonuna basarak bir sonraki adıma geçtim.

35- Bu adımda bizden bilgilerin tutulacağı ve kullancı loglarının tutulacağı dizinleri girmemizi istedi. Bu alanlara gerekli dizin isimlerini yazdıktan sonra Next butonuna basarak bir sonraki adıma geçtik.
36- Karşımıza gelen pencereden dizinlerin otomatik olarak yeni dizinlere taşınıp taşınmıyacağını sordu. Otomatik olarak taşıma seçeneğini seçerek OK butonuna bastık.
37- Daha sonra gelen pencereden Finish butonuna basarak Exchange Server Service'lerinin çalıştırılmasını sağladık.
38- Böylece Exchange server kurulumunu tamamladık.

## **Kullanıcı MailBox'larının ve Adres Listerinin Oluşturulması: ******

Exchange Server makinanın açılışıyla beraber gerekli olan service'leri otomatik olarak çalıştırır. Bu servisler aşağıda verilmiştir.

| Microsoft Exchange Directory |
| --- |
| Microsoft Exchange Information Store |
| Microsoft Exchange Message Transfer Agent |
| Microsoft Exchange System Attendant |

Biz Exchange administrator programını çalıştırarak Exchange üzerinde işlemler yapabiliriz. Bunun için
1- Start butonuna basın
2- Programs sekmesini seçin
3- Microsoft Exchange bölümünü seçin
4- Microsoft Exchange Administrator programını çalıştırın.
5- Exchange programını ilk defa yüklediğimiz için Internet Mail Service'ini yüklememiz gerekiyor.
6- Bunun için File menüsünden New Other seçeneginden en alttaki Internet Mail Service seçiyoruz.

7- İlk gelen pencere kısaca bu işlemin hangi adımlardan oluştuğunu anlatıyor. Bu pencereyi Next butonuna basarak geçiyoruz.
8- Yeni gelen pencere ise daha detaylı bir açıklama sunuyor. DNS manager'dan Exchange Server için A mail MX recordları yaratılıyor. Bu recordlara göre Exchange Server servisleri çalışacaktır.
9- Next butonuna basarak bir sonraki adıma geçiyoruz.
10- Bu adım da hangi Domain'in bu mail server'dan yararlanabileceğini belirtmemiz isteniyor. Okul için buraya CSCIENCE giriyoruz.
11- Daha sonra Next butonuna basarak bir sonraki adıma geçiyoruz.
Bu adımda Mail'ler gönderilirken nasıl bir yol izlenecegini belirtmemiz gerekiyor.

12- Biz burada DNS kullanacagımız belirtiyoruz. Next butonuna basarak bir sonraki adıma geçiyoruz.
13- Bu adımda hangi mail'lerin gönderilmesine izin verileceğini belirtiyordu.
14 Biz burada ki ilk seçenegi seçerek bütün mail'lerin gönderilmesine izin verdik.
15- Next butonuna basarak bir sonraki adıma geçtik. Bu adımda mail sitesi olarak ne kullanılacagını girmemiz isteniyor.

16- Buraya yazılacak deger dışardan mail gönderilirken @ işaretinden sonra hangi adres yazılması gerektigini belirtiyor.
17- Biz bu alana @cs.istanbul.edu.tr girdik.
18- Artık yarattıgımız mail box 'lara mail görelilirken kullanılacak adres = kullanıcının\_mailbox@cs.istanbul.edu.tr olacaktır.
19- Next butonuna basarak bir sonraki adıma geçtim.

## 20-Bu adımda Excahnge administrator olan kullanıcı için mailbox belirtmemizi istedi

21-İlk seçenek seçilirse yeni bir mailbox yaratılmaktadır.
22-Eger ikinci seçenek seçilirse bir mailbox seçilmektedir.
23-Next butonuna basarak bir sonraki adıma geçtim. Bu adımda yaratılan mailbox için bir şifre girmemizi söyledi.

24-Şifremizi girdikten sonra bir sonraki adıma geçmek için Next butonuna bastım.
25-Artık Internet Mail Service kurulumunu tamamladık.
26-Artık CS domaini ile ilgili kullanıcı ve grub tanımlamaları yapabilmemiz mümkün olacaktır.
27-Yeni bir kullanıcı mailbox'ı yaratmak için File menüsünden New Mailbox sekmesi seçilebilir yada toolbardan New Mailbox butonuna tıklanarak yeni bir mailbox yaratılabilir.

28-Karşımıza gelen pencereden boş olan alanları doldururuz.
29-Burada First alanına isim gireriz.
30-Last alanına soyisim girilir.
31-Display alanına Exchange Server listesinden görülmesini istedigimiz degeri gireriz.
32-Alias alanına ise kullanıcı mailbox'ını girmelyiz. Biz burada 9406035 girdik bu kullanıcıya dışardan mail gönderilmek istenirse adres 9406035@cs.istanbul.edu.tr olarak bu değer girilmelidir.
33-Diger bilgileride doldurdıktan sonra eger bu kullanıcının Domain'dede username'I varsa Primary Windows NT Account seçenegine basılarak NT'deki şifrenin geçerli olması sağlanır.

34-Phone/Notes sekmesine tıklanılarak kullanıcı telefon numaraları girilebilir.
35-Distribution Lists sekmesine tıklayarak kullanıcıyı belirli mail grublarına dahil edebilriz.
36-Karşımıza gelen pencereden Modify butonuna basarak kullanıcıyı dahil edecegimiz listelerin görülmesini sağlarız.

37-Burada da görmüş oldugunuz gibi sol tarafta listeler gözükmektedir. Bunlar seçilerek Add butonuna basılırsa kullanıcıyı bu listelere eklemiş oluruz.
38-Kullanıcının mailbox'ına bazı sınırlamalar getirmek istersek Advanced butonuna basarak karşımıza gelen pencereden sınırlamalrı girebiliriz.

39-Burda da görmüş oldugumuz üzere kullanıcı mesaj büyüklüklerini sınırlıyabiliyoruz.
40-Gelen mesaj boyutunun MAX degerini Incoming alanına giriyoruz. (Kilobyte)
41-Giden mesaj boyutunun MAX degerini Outgoing alanına giriyoruz. (Kilobyte)
42-Eger kullanıcının mailbox'ında belirli bir degerden sonra mail'leri sınırlandırılmak istenirse bu alltaki bölümden sağlıyabiliyoruz.
43-Issua warning alanına girdigimiz değerden (büyüklük bakımından) çok mail varsa kullanıcıya uyarı verilmesi sağlanıyor.
44-Prohibit send alanına girilen degerden çok fazla mail varsa artık kullanıcı bu mail'lerini silmeden mail gönderemez.
45-Delivery Restriction alanında ise kullanıcının gelen ve giden mesajlarına sınırlamalar getirebiliyoruz. Burada bu mail adına gelen mesajların hangilerinin kabul hangilerinin kabul edilmiyecegini belirtebiliyoruz. Buraya girdigimiz kişilerden gelen mesajların kabul edilip edilmiyecegini belirtiyoruz.

46-Yeni bir mesaj grubu yaratılmak istenirse File menüsünden New Distribution Lists seçilir.
47-Karşımıza yeni grup tanımlamaları yapacağımız aşağıdaki pencere gelir.

48-Bu pencereden display alanına Exchange programında bu grup için görülecek isim girilir.
49-Alias name alanına ise dışardan bu gruba gönderilecek mail'lerin ön eki yazılır.
50-Owner alanına bu adres grubunun sahibi girilir. Bunu yapmak için Modify butonuna tıklanırsa karşımıza Exchange server'da mail'leri bulunan kullanıcılar gelecektir.
51-Buradan sahip seçildikten sonra OK butonuna basılarak işlem tamamlanır.

52-Bu listeye mailbox eklemek istersek Members frame altında yer alan Modify butonuna tıklanır.
53-Aşağıdaki gibi gelen pencereden son tarafdaki kullanıcılar seçilerek Add butonuna basılarak bu gruba dahil edilirler.

52-Eğer bu listeye bir mesaj gelirse artik bu mesaj bu listedeki bütün kullanıcılara gönderilecektir.
53-Eğer bu liste içine başka bir listeye gelen mesajlarıda eklemek istersek en üste Distribution List sekmesine tıklanır. Burada da modify butonuna basılarak gerekli listeler ilave edilebilir.
54-E-mail adres sekmesine tıklarsak artık bu grubun e-mail adresinin birler@cs.istanbul.edu.tr olarak yer aldığını görürüz.
55-Eğer bu listeye bazı ileri seviyede özellikler eklemek istersek Advanced butonuna tıklarız.

56-Eğer bu gruba gelen mesajlara boyut sınırlaması getirmek istersek Message size Max alanına kilobyte olarak mesaj boyutunu girmeliyiz.
57-Aşağıda da bu liste ile ilgili seçenekler verilmektedir.
58-Birinci seçenek seçilirse liste hakkında bu listenin sahibine rapor verilir.
59-İkinci seçenek seçilirse listenin yaratıcısına mesaj geçilir
60-Üçünücü seçenek seçilirse listenin yaratıcısına offline mesajları geçer.
61-Dördüncü seçenek seçilirse adres defterini kullanıcılardan gizler.
62-Beşinci seçenek seçilirse liste üyelerinin adres defterleri gizlenir.
63-Eğer sekmeler Delivery Restriction seçilirse gelen ve giden mesajlar için kısıtlamalar getirilir.
64-Bu kısıtlamalar bazı kullanıcılardan gelen mesajları alma ve bazılarına göndermedir.
65-OK butonuna basılırsa artık grubumuz yaratılır. Aşağıda grubun nasıl göründüğünü gösteren bir resim görülmüştür.birinci\_sinif adlı grubumuz yaratılmıştır.

## 66-Exchange Server üzerinde daha bir çok kontrol getirebilmektedir

## PAGE

## PAGE 16

---
*Kaynak: `AĞ YÜKLEMESİ İÇİN DAHA FAZLA PLANLAMA/ekitap-Anonim-Ag_Y³klemesi_I_in_Daha_Fazla_Planlama.doc` — SONTAY — 2001*
