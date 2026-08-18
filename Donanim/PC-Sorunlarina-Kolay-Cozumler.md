# PC Sorunlarina Kolay Çözümler

## **PC SORUNLARINA KOLAY ÇÖZÜMLER.**

Donanım ve yazılımların birbirleri ile uyumsuz çalıştıkları, her donanımın her işletim sistemi ile aynı performansı sunmadığı günümüzde PC kullanıcılarının sıklıkla karşılaştığı bazı sorunlara ayrıntılı çözümler bulmaya çalıştım.

PC kullanımı, gelişen donanımlar ve işletim sistemleri ile her geçen gün daha da yaygınlaşırken beraberinde de yeni sorunları getiriyor. Her sorun ayrı bir bilgi birikimi ile çözüme ulaştırılabiliyor. Her PC kullanıcısı değişik konfigürasyonlarda farklı donanım problemleri ile karşılaşıyor. Donanım hakkında bilgi ve tecrübe ise bu problemleri çözmeye çalışırken ediniliyor. Birçok donanım problemi zor gözükse de en fazla birkaç dakika içinde kolaylıkla çözülebiliyor. Diğer yandan kullanıcılar PC performanslarının yanı sıra kullanım kolaylığı da arıyorlar. İşletim sistemleri kullanıcıya bu kolaylıkları sağlarken kullanıcının da bu kolaylıkları keşfetmesi gerekiyor.

Unutulmamalıdır ki işletim sistemleri göründüğünden çok daha fazla işlemi bir arada gerçekleştirirken kullanıcılarda bu işlemleri hızlandıracak yolları bulmalıdır

## **SABİT DİSKLER...**

SABİT DİSKLERDE DMA NEDİR? NASIL AÇABİLİRİM?

DMA (Direct Memory Acces) yada diger adıyla ‘bus mastering’ bir sabit diskin bilgiyi doğrudan RAM’e yani belleğe atarak bilgisayarın işlemcisini daha az kullanmasını sağlayan ve otomatik olarak bilgisayarı hızlandıran veri iletişim tekniğinin adıdır. Sabit diskinizin DMA özelliğini açmak için Windows ta bilgisayarım’ a sağ tıklayın ve özellikleri seçin. Aygıt yöneticisi bölümüne girin ve oradan disk sürücüleri bölümünü seçin DMA özelliğini açmak istediğiniz sabit diskinize çift tıklayın ve özellikler seçeneğine girip DMA yazan kutuyu işaretli değilse işaretleyin.

NİYE 2,1 GB BOYUTUNDAN DAHA BÜYÜK BİR PARTİTİON OLUŞTURAMIYORUM?

Windows 95 OSR2 sürümünden daha eski bir Windows kullanıyorsanız FAT 16 Sistemini kullanmak zorundasınız. Çünkü Windows’un eski sürümlerinde maxımum ‘partition’ boyutu 2.1 GB dir. Eğer sabit diskinizin boyutu 2.1 GB dan büyükse ve eski bir Windows sürümü kullanıyorsanız birden fazla partition yaparak sabit diskinizi bu şekilde kullanmak zorundasınız. Eğer Windows 95 OSR2 veya daha yeni bir Windows sürümü kullanıyorsanız ve yine 2.1 GB daha büyük bir partition oluşturamıyorsanız siz FAT 32 kullanmıyorsunuz demektir. Bu problemi çözmek için FDISK programını kullanmalı ve partition tanımlaması yapmadan önce ilk baştaki büyük disk deste ğini etkinleştirmek ister misiniz sorusuna evet cevabı vermeniz gerekiyor.

3) WİNDOWS DİSK BİRLEŞTİRİCİ KULLANIRKEN İŞLEM DURUYOR VE SÜRÜCÜNÜN İÇERİĞİ DEĞİŞTİ YENİDEN BAŞLATILIYOR HATA MESAJI ÇIKIYOR.

Bu durum genellikle sabit diskte bir problem varsa ortaya çıkıyor. DOS moduna geçerek SCANDİSK.EXE yazın ve ENTER tuşuna basın. ‘SCANDİSK’ işlemi yapılırken sabit diskinizde ‘bad sector’ bulunursa scandisk’in bu hatalı sectorleri işaretlemesine izin verin. Scandisk işlemi bittikten sonra Windows’u yeniden başlatın ve disk birleştirici programını tekrar başlatın

Disk birleştirici kullanırken herhangi başka bir programı çalıştırırsanız bu hata mesajı yine çıkar.

Bu nedenle disk birleştirici çalıştırırken başka bir program kullanmamaya dikkat edin. Aksi taktirde disk birleştirici durup en baştan başlayacaktır. Bu da zaman kaybetmenize neden olacaktır.

Disk birleştirici kullanmaya başlamadan önce açık olan tüm programları kapatmalısınız.

Arka planda yani görünmeden çalışan antivürüs programı gibi programları da kapatmak için \[CTRL\] + \[ALT\] + \[DEL\] tuşlarına basarak Task Manageri çalıştırın. Explorer ve Systray dışındaki tüm programların görevini sonlandırın ve disk birleştiriciyi yeniden başlatın.

BİLGİSAYARIMA YENİ BİR SABİT DİSK TAKTIM, ANAKARTIM SABİT DİSKİ TANIMADI VE ‘WİNDOWS KORUMA HATASI’ İLE KARŞILAŞIYORUM

Sabit diskinizin üzerinde yer alan ‘jumper’ ayarlarını doğru yapmadığınızda bu problemle karşılaşabilirsiniz. ‘jumper’ ayarlarında genellikle üç seçenek vardır. ‘Master, Slave ve Master with Slave present’ eğer bu harfler sabit diskin üzerinde belirtilmemişse yada sabit diskin yanında bir kullanım kılavuzu verilmediyse bu ayarları sabit diskinizin üreticisinin WEB sitesinde bulabilirsiniz.

YENİ BİR SABİT DİSK ALDIM VE ESKİ SABİT DİSKİMDEKİ TÜM DOSYALARI YENİ SABİT DİSKİME KOPYALAMAK İSTİYORUM.

Dosyalarınızı eski sabit diskinizden yeni sabit diskinize kopyalamak için Windows ile birlikte gelen Xcopy programını kullanabilirsiniz. Bilgisayarınızı tekrar başlatıp DOS moduna girin. C: konumuna geldikten sonra CD\\ yazıp \[Enter\] tuşuna basın. Daha sonra path=c:\\Windows\\command yazıp yine \[Enter\] tuşuna basın. Şimdi Xcopy programını xcopy/k/e/h c: \*.\* d:\\ yazarak çalıştırın. Bu şekilde bütün dosyalarınız eski sabit diskinizden (c:) yeni sabit diskinize (d) kopyalanacaktır. Disk sürücülerinizin başlangıç harfleri c ve d’den farklı ise bunları değiştirmeniz gerekebilir.

Bu işlem bittikten sonra bilgisayarınızı kapatın ve ‘Jumper” ayarlarınızı değiştirin ve yeni sabit diskinizi ‘master’ eski sabit diskinizi ise ‘slave’ yapın.

## **EKRAN KARTLARI...**

EKRAN ÇÖZÜNÜRLÜĞÜMDE 640X480 VE 256 RENKTEN BAŞKA SEÇENEK GÖREMİYORUM.

Windows ekran kartınızı tanımadığında ya da yanlış sürücü yüklendiğinde otomatik olarak varsayılan VGA sürücünü yükler ve size başka görüntü seçeneği sunmaz. Bu problemi çözmek için ekran kartınızın güncel sürücüsünü yüklemelisiniz. Masaüstüne sağ tıklayın ve Özelliklere girin Ayarlara sol tıklayıp ‘Gelişmiş’ seçeneğine tekrar sol tıklayın. Adapteri’ işaretleyip Değiştire sol tıklayın. Karşınıza çıkan ekranda Disketi Varı seçin. Daha sonra ‘Araştır’ diyerek Windows’a ekran kartının sürücüsünün olduğu yeri gösterin. Böylece ekran kartınız gerçek sürücüleri ile yüklenecek ve başka çözünürlük ve renk seçeneklerine sahip olacaksınız.

7) WİNDOWS AÇILDIĞINDA EKRANDA DİKEY VEYA YATAY ÇİZGİLER OLUŞUYOR VE HİÇ BİR ŞEY OKUNMUYOR YA DA GÖRÜLMÜYOR.

Ekran kartınızın ayarlarında monitörünüzün desteklediği maksimum tarama değeri (refresh rate) üzerinde bir seçenek işaretlenmiş. Düzeltmek için bilgisayarınızı yeniden başlatın ve Güvenli Kipte açın. Görüntü Seçeneklerinden Ayarlara oradan da Adapter’a girin. Ekran çözünürlüğünde 60 Hz’i seçin ve bilgisayarınızı yeniden başlatın. Windows doğru olarak açılacaktır. Eğer 60 Hz size yetmiyorsa veya daha yüksek bir çözünürlüğe çıkmak istiyorsanız bu ayarı daha sonra değiştirebilirsiniz

AGP BİR EKRAN KARTI ALDIM ANCAK PCI SLOTUNA GİRMİYOR.

AGP ekran kartları sadece AGP ekran kartlarını destekleyen anakartlar da çalışır. Eğer ki AGP ekran kartı aldıysanız ve anakartınız eski ve AGP slotu yoksa çalıştırmak için anakartınızı da değiştirmeniz gerekecektir.

9) EKRAN KORUYUCUM DEVREYE GİRDİKTEN VE WİNDOWS BİLGİSAYARI ASKIYA ALDIKTAN SONRA FAREMİ HAREKET ETTİRİYORUM KLAVYEDE BİR TUŞA BASIYORUM AMA MAKİNEM AÇILMIYOR.

BIOS ayarlarında Power saving bölümünde Event Tımer seçeneği kapatılmışsa bilgisayar ‘Wake Up’ özelliğini gerçekleştiremez.Bunun düzelmesi için BIOS ta Event Tımer seçeneğini aktif hale getirin.

10) BİLGİSAYARIMI AÇARKEN ÜÇ KISA SİNYAL SESİ GELİYOR VE MONİTÖRÜME GÖRÜNTÜ GELMİYOR.

Bilgisayar açıldığında gelen üç kısa sinyal sesi ekran kartıyla ilgili bir problem olduğunu göstermektedir. Ekran kartını yerinden çıkarıp tekrar takın. Kart yerine oturmamış veya yerinden çıkmış olabilir. Ekran kartının anakarta giren ayakları kirlenmiş olabilir. Kuru bir bezle silin yine çalışmıyorsa ekran kartınızın yerine başka bir ekran kartı takın.

## **SES KARTLARI...**

11) BİLGİSAYARIMDAN ÇIKAN SESLER TİTRİYOR VEYA TEKRAR EDİYOR

Sık sık karşılaşılan ses kartları ile ilgili bu problem genellikle IRQ çakışması nedeniyle ortaya çıkıyor. Ses kartı ile aynı IRQ ‘yu kullanan anakarta bağlı başka bir kart bu probleme neden olabiliyor. Bir çok ses kartı IRQ7 ‘ i veya varsayılan olarak IRQ5 ‘i kullanmak isterken başka kartalar IRQ5’ i veya paralel porta atanmış olan IRQ7 ‘ yi kullanmak isterler. ‘Device Manager’ dan kaynak çakışması olup olmadığını kontrol edin. Varsa ses kartınıza boş bir IRQ bulun ve kendiniz bu IRQ yu ses kartına atayın.

Eğer probleminiz hala devam ediyorsa, bir başka neden de DMA çakışması olabilir yada ses kartınız 16 bit DMA modunu desteklemeyen eski bir kart olabilir. Bu problemi çözmek için denetim masasına gidin ve sistem ikonunu çift tıklayın ‘Device Manager’ kısmından ‘Sound’ , ‘Video and Game Controllers’ seçeneğine girin. Ses kartınıza çift tıklayın ve kaynaklar seçeneğine girin ‘Automatic Settings’ kutusunun işaretini kaldırın. Setting based on kutusunu seçin ve basic Configuration 7 yi seçin. Eğer Sound Blaster 16 plug and play kartı veya benzer uyumlu bir kart kullanıyorsanız basic configuration 0004’ ü seçin ve 8 bit DMA kullanın

12) HOPARLÖRLERDEN GÜRÜLTÜ GELİYOR.

Ses kartı, PC nizin güç kaynağından etkileniyor olabilir ses kartınızı başka bir slota takın başka bir nedende mikrofon olabilir. Mikrofonun sesini ses ayarlarından kapatın veya mikrofonu çıkartın eğer sorun hala devam ediyorsa ses kartını sabit disktende uzak bir yere takın sorunun devamı halinde CD sürücüsünden ses kartına giden kabloyuda kontrol edin kabloyu değiştirin yada yalıtım için etrafını bir bant ile sarın

13) MİDİ DOSYALARINI ÇALARKEN SES ÇIKIYOR AMA WAW VE MP3 DOSYALARINI ÇALARKEN SES ÇIKMIYOR.

Problem Windows’ un ses kartı için yaptığı otomatik ayarlar ile ilgili olabilir. Kartınızı başka bir PCI slota takın.

14) TASK BARDA SES ÖZELLİKLERİ İÇİN KULLANDIGIM İKON ÇIKMIYOR

Başlangıç menüsünden ayarlara gidin, oradanda denetim masasına girin ‘Multimedia’ ikonuna çift tıklayın. ‘show volume control on the task bar’ kutusunu işaretleyin uygulaya tıklayın ve OK diyerek bu pencereden böylece task bardaki hoparlör ikonuna çift tıklayarak ses özelliklerine girip istediğiniz ayarları yapabilirsiniz.

15) SES KARTIMIN SES KAYIT ÖZELLİĞİNİ KULLANABİLİYORUM AMA MİKROFON KULLANARAK SES KAYIT YAPMAK İSTEDİĞİMDE MIXER’DE SES DALGASINI GÖRMEME RAĞMEN SES ÇIKMIYOR.

Taskbar’daki ‘Ses Özellikleri’ ikonunu çift tıklayın ve Seçeneklerden Properties’e girin. Mikrofon’un olduğu kutunun işaretli olup olmadığını kontrol edin ve değilse kutuyu işaretleyin.

16) BİLGİSAYARIMA YENİ BİR CD SÜRÜCÜ EKLEDİM AMA WİNDOWS CD SÜRÜCÜMÜ TANIMADI.

Özellikle BIOS’un CD sürücünüzü tanıyıp tanımadığını kontrol edin. Eğer tanımıyorsa CD sürücü IDE kablosunu kontrol edin. Ayrıca güç kaynağından elektrik alıp almadığına da bakın.

Eğer BIOS CD sürücünüzü tanırsa Windows’ta Denetim Masası’na girip Sistemden CD sürücünüzü kaldırın ve Windows’u yeniden başlatın.

Yeni bir CD sürücü eklerken ‘Jumper’ ayarlarının doğru olup olmadığını kontrol edin. Eğer IDE bağlantınızda çift sürücü varsa bunlardan birinin ‘Master’ diğerinin ‘Slave’ olmasını sağlayın. Eğer ikisi de ‘Master’ veya ‘Slave’ ise Windows sürücünüzü tanımayabilir.

17) CD SÜRÜCÜMÜN HARFİ F AMA SÜREKLİ KAYBOLUP BİR AĞ SÜRÜCÜSÜ GİBİ GÖZÜKÜYOR.

Bu problemin genel sebebi Netware ağ ayarlarıdır. Eğer CD sürücüsünün adı ile Birincil Ağ sürücüsünün adı aynı olursa bu problem ortaya çıkıyor. Eğer ‘Map’ edilmiş bir ağ sürücünüz varsa ve aynı adı taşıyan bir CD sürücü tanımlı ise Ağ Sürücüsü CD sürücünün yerine çalışır ve CD sürücü çalışamaz hale gelir.

Bu problemi çözmek için, Ağ Ayarları’nda Netware özelliklerinde ‘Birincil Ağ Sürücüsü’ adını, F’ten başka bir harf olarak tanımlayın.

18) CD SÜRÜCÜMÜN HARF ADINI NASIL DEĞİŞTİREBİLİRİM?

Başlangıç Menü’sünden ‘Ayarlar’ a oradan da ‘Denetim Masası’ na girin ve ‘Sistem’ ikonunu çift tıklayın. ‘Device Manager’ kısmında adını değiştirmek istediğiniz CD Sürücü’nün ikonunu çift tıklayın. Ayarlar kısmında tanımlanmış başlangıç ve bitiş harflerinin her ikisini birden değiştirin ve Denetim Masası’na geri dönün. Bu değişikliklerden sonra bilgisayarınızı yeniden başlatmanız gerekebilir.

19) CD SÜRÜCÜM DOS MODUNDA ÇALIŞMIYOR

Bu problemi çözmek için CD sürücünüzün DOS sürücülerine ihtiyacınız olacak. Donanımınızı alırken size verilen DOS sürücülerini yüklemelisiniz. Ayrıca sisteminizde yer alan ‘autoexec.bat’ dosyanıza şu satırı eklemelisiniz:

C:\\windows\\command\\mscdex.exe/d:mscd000

Ayrıca ‘config.sys’ dosyasına da şu satırı eklemeniz gerekmekte:

Device=C:\\path\\cdrom.sysy/D:mscd000

Burada ‘path’ yazan yere CD sürücünüzün harf adını ve ‘cdrom’ yazan yere de CD sürücünüzün adını yazmalısınız.

20) GÜVENLİ KİP’TE CD SÜRÜCÜMÜ NASIL ÇALIŞTIRABİLİRİM?

Daha önceki problemde belirtildiği gibi DOS sürücülerin yüklenmiş olması gerekiyor.

Bilgisayarınızı yeniden başlattıktan sonra ‘Windows 95 başlıyor’ yazısını gördüğünüz sırada \[F8\] tuşuna basın ya da Windows 98’de PC açılırken \[CTRL\] tuşuna basın. Komut İşlemcisi’nde win/d:m satırını yazın ve \[Enter\] tuşuna basın. Böylece Windows güvenli kipte açılacak ve CD veya DVD sürücünüz varsa güvenli kipte kullanabileceksiniz.

21) CD SÜRÜCÜME YENİ BİR CD YERLEŞTİRDİĞİMDE OTOMATİK OLARAK BAŞLAMIYOR.

‘Başlat’ menüsünden ‘Ayarlar’, oradan da ‘Denetim Masası’ na gidin. ‘Sistem’ ikonunu çift tıklayın. ‘Device Manager’ kısmından CD sürücünüzün üzerine çift tıklayın ve ‘Auto Insert Notification’ kutusunu işaretleyin ve Denetim Masası’na geri dönün.

Başka bir çözüm de profesyonel kullanıcılar için. ‘Başlat’ menüsünden ‘Çalıştır’ a girin ve ‘regedit’ yazarak \[Enter\] tuşuna basın. ‘Registry Editör’ e girdiniz. HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\CDRom anahtarına bir bakın. Eğer ‘Autorun‘ yoksa ‘Autorun’ adında yeni bir anahtar yaratın ve anahtarın değerini ‘1’ yapın. ‘Autorun’ özelliğini kapatmak isterseniz bu değeri ‘0’ yapın.

22) CD SÜRÜCÜM UZUN DOSYA İSİMLERİNİ OKUYAMIYOR.

‘Real Mode’ kullanıyorsanız ya da DOS sürücüleri düzgün yüklenmediyse bu problem yaşanabilir. Sürücülerinizi güncelleyin ve sürücünün eski satırlarını ‘autoexec.bat’ ve ‘config.sys’ dosyalarından silin. Problem çözülecektir.

23) CD SÜRÜCÜME TAKTIĞIM MÜZİK CD’SİNİ DİNLEYEMİYPRUM

Cd sürücünüzün ses kartınıza bağlanmış olması gereken ses kablosunu kontrol edin, çıkartıp tekrar takın. Ses kartının üzerinde ‘CD-in’ yazan yere takılı olup olmadığını kontrol edin. Ayrıca windows saatinin yanındaki ses kontrol ikonuna tıklayın. Ses kontrolünde CD sürücünün sesini açın.

24) BİLGİSAYAR AÇILIRKEN ‘MEMORY’ HATASI VERİYOR VE RAM BOYUTU DOĞRU OLARAK GÖSTERİLMİYOR.

Bu problem, RAM’lerin slotlara doğru oturmamış olmasından, slota değen ayakların kirli olmasından ya da RAM’lerin arızalı olmasından dolayı olabilir. RAM’leri slottan çıkartıp yeniden yerleştirin. RAM’leri takarken ayakları yumuşak silgi ile silin.

RAM’leri teker teker takarak çalıştırın. Böylece arızalı bir RAM varsa farkedebilirsiniz. Eğer SIMM RAM kullanıyorsanız aynı boyutta olan RAM’leri takmalısınız. Yani bir 32 MB RAM ile bir 64 RAM beraber çalışmayabilir. Bu arada RAM lerin çalışma hızları da aynı olmalı. 60ns bir RAM ile sadece 60ns bir RAM bir arada çalışabilir. Eğer DIMM RAM kullanıyorsanız daha yavaş olan RAM’I birinci slota takın. Slot numaraları anakart üzerinde gösterilmiyorsa anakartın kullanım kılavuzuna bakın. RAM’lerin slotlara düzgün bir şekilde takıldığından emin olun.

25) BİLGİSAYARIM AÇILIRKEN ‘BOOTABLE DRİVE NOT FOUND’ VEYA ‘OPERATİNG SYSTEM NOT FOUND’ HATA MESAJLARI ÇIKIYOR.

Boot drive’ınız aktif hale getirilmediyse bu problem ortaya çıkar. Yani işletim sisteminin yüklü olduğu sürücünün ‘partition’ ının aktif hale getirilmesi gerekmektedir. Bunu Fdisk.exe ile düzeltin.

‘Operating system not found’ hata mesajı bir virüs ya da herhangi bir başka nedenle Master Boot Record’un silinmesi ya da zarar görmesinden dolayı ortaya çıkar.

Bir başlangıç disketi ile c: sürücüsünde iken fdisk /mbr yazarak Master Boot Record’u düzeltebilirsiniz.

26) SABİT DİSK SÜRÜCÜMÜN BAŞLANGIÇ HARFLERİ DEĞİŞTİ.

Sabit disk’inize yeni bir ‘partition’ eklediyseniz veya varolan bir ‘partition’ ı sildiyseniz başlangıç harfleri değişebilir. Yeni bir logical drive yaratarak yeni bir başlangıç harfi ekleyebilirsiniz. Eğer bir ‘partition’ sildiyseniz, ‘partition’ ın temsil ettiği başlangıç harfi silinir. Yeni bir ‘partition’ ismi CD sürücü ya da çıkarılabilir başka bir sürücünün adını alır ve diğer sürücülerin adlarını alfabetik sırada iteler.

27) FLOPPY DİSK SÜRÜCÜSÜ’NÜN IŞIĞI SÜREKLİ YANIYOR VE DİSKETLERİ OKUYAMIYOR.

Floppy Sürücüsü’nün kablosu ters takılmış. Kabloyu yerinden çıkarıp doğru olarak takın.

28) BIOS ŞİFREMİ KAYBETTİM VE PC’Mİ AÇAMIYORUM.

PC’nizin güç kaynağının elektrik kablosunu çıkarın ve anakart üzerinde CMOS’u silmeye yarayan ‘Jumper’ ı bulun. Jumper’ı ayarlayın ve 30 saniye bekleyin. Daha sonra ‘Jumper’ ı eski haline getirin ve PC’nizi açın. Anakartınızın BIOS’u resetlemiş ve bütün şifreler kaldırılmış hale gelir.

29) INTELLIMOUSE KULLANIYORUM AMA FARE EKRANDA İSTEDİĞİM YERE GİTMİYOR YA DA KENDİ KENDİNE HAREKET EDİYOR.

Intellipoint sürücülerinde sıkça yaşanan bir problem. Çözmek için sürücüleri kaldırın, Device Manager’da tekrar aktif hele getirin ve sürücüleri tekrar yükleyin.

30) USB FARE KULLANIYORUM AMA SABİT DİSK SÜRÜCÜ VEYA CD SÜRÜCÜ AKTİF HALDEYKEN FAREM TAKILIYOR.

Genellikle PC’niz Sabit disk, Floppy Disk Sürücü veya CD sürücüsü’nden okurken USB donanımlarınız takılabilir ya da düzgün çalışmayabilir. Bunu düzeltmek için Denetim Masası’ndan Device Manager’a girin ve Sabit Disk ve CD sürücülerin DMA özelliğini açın.

31) PC’Mİ GÜVENLİ KİP’TE AÇTIĞIMDA WİNDOWS PS/2 FARE OLMADIĞI UYARISINI YAPIYOR.

PS/2 Port’unun BIOS’ta doğru olarak kurulduğunu kontrol edin. Intel Triton Chipset kullanan anakartlarda PS/2 farelerin kullanılması için BIOS güncellemesi yapılması gerekebilir.

32) FAREMİN İŞARETİ DONUYOR VE TİTRİYOR.

Bu problemin nedeni Grafik Hızlandırıcı ayarının çok yükseğe getirilmiş olmasıdır. Sistem Özellikleri’nde performans’a gelin ve grafik hızlandırma ayarını biraz düşürün.

33) KLAVYEMDE BAZI TUŞLAR İSTEDİĞİM KARAKTERLERİ BASMIYOR. (@) İŞARETİ YERİNE (‘) ÇIKIYOR.

Windows’ta klavye ayarlarınız yanlış dile getirilmiş. Denetim Masası’nda Klavye’yi seçin ve Bölgesel Ayarlar’da kullanmak istediğiniz dili seçin.

PAGE 1

PAGE 1

---
*Kaynak: `PC SORUNLARINA KOLAY ÇÖZÜMLER/PC SORUNLARINA KOLAY ÇÖZÜMLER.doc` — Fatih Yılmaz — 2004*
