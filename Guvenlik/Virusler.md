# Virüsler

## **VİRÜSLER**

Virüs, bilgisayar programlarını istem dışı olarak etkileyen ve programların yapması gereken asıl fonksiyonlarını hiç yaptırmayan, kısıtlayan veya yanlış işlemler yaptıran yazılımlardır. Özellikle internet kullanımının yaygınlaşması, bilgisayarlar arasında sürekli bir bağın olması (ağ) virüslerin yayılmasını hızlandırmıştır. Her gün yeni birtakım virüs ortaya çıkmakta ve hızla yayılmaktadır. Virüsler genellikle assembler programlama dili ile hazırlanmış ve kapasiteleri 1 byte ile 3 KB arasındadır.

Virüslerin aktif hale geçebilmeleri için çalıştırılabilen (EXE – COM uzantılı gibi) programlara bulaşması gerekir. Virüs bulaşan bir program çalıştırıldığında, virüs belleğe taşınır ve bellekte bulunan virüs bulunduğu sürece COMMAND.COM kütüğüne bulaşmayı ilk hedef olarak görür. Virüs bir kez bu kütüğe yerleştikten sonra sistemin her açılışında kendini belleğe yüklemekte ve çalıştırılan her programa bulaşmaktadır.

Virüsler, EXE, COM, SYS, PRG, OVL, OBJ, LIB uzantılı dosyalara ve boot sektöre bulaşabilir. Bomba kısmı ise çalışmak için uygun şartların çalışmasını bekler. Buradaki uygun şart herhangi bir şey olabilir. Zamana bağlı şartlar olabileceği gibi sistemde VGA monitörün bulunması, hard diskin kapasitesi, ülke kodu gibi çok değişik şartlarda gözlenebilir. Bu tamamen virüs yazarının isteğine kalmış bir olaydır. Uygun şartlar oluşmazsa virüs sadece yayılmaya devam eder. Uygun şartlar oluştuğunda ise bomba kısmı çalışmaya başlar. Bomba kısmı sisteme zarar verebileceği gibi ekrana basit bir mesaj yazabilir veya sadece kullanıcıya şaka yapmak amacı ile zararsız etkiler yapabilir.

Çoğu kişi sisteminde önemli şeyler barındırmaz, eğer sisteminizi ticari amaçlar dışında kullanıyorsanız virüs tüm hard diskinizi silmiş olsa bile fazla zarara uğramanız pek mümkün değildir. Büyük ihtimalle kaybettiğiniz programları çevrenizden bulmanız mümkündür. Fakat sisteminiz ticari amaçla kullanılıyorsa veya bir firmanın kullanımında ise maddi manevi zarar oldukça büyük olacaktır. Artı olarak bu tip bilgilerin yedeklenmediğini düşünün bu durumda problemin boyutları daha da büyüyecektir. Virüslerden korunmak için harcayacağınız emek ve zamanı bu kritere göre belirleyiniz.

Kendinizin ve diğer kullanıcıların teknik seviyesi ve tecrübesi ne kadardır? Bazı tecrübeli kullanıcılar yedek aldıktan sonra bir şeyden şüphelenmedikçe virüslere karşı tedbir mahiyetinde hiçbir korunma işlemi yapmaya gerek duymazlar. Gerektiğinde virüsü disassambly edip anti virüsünü yazacak kadar tecrübeli kullanıcılar bulunmaktadır. Buna karşılık oldukça tecrübesiz kullanıcılarda vardır.

Her ortamda virüs bulaşma ihtimali vardır. 1998 sensinde Novel firması 3800 adet virüslü disketi müşterilerine gönderdiyse, IBM ve NASA’nın bilgisayarları virüsten zarar gördüyse, 50 senelik tecrübeye sahip olsanız bile sisteminize virüs bulaşma ihtimali bulunmaktadır. PTT veya su idaresinin bilgisayarlarına girebilecek bir bilgisayar virüsünün aboneler ile ilgili kayıtları bozması sonucu 3-4 milyar telefon faturasını görerek hayatında bilgisayar kullanmamış olsa bile virüslerden zarar görmüş olur.

**VIRÜSLERIN YAPISI**

Virüslerin yapısı temel olarak 3 kısımda incelenir. Bunlar sırası ile kopya üreticisi, gizleyici ve bomba kısımlarıdır.

**Kopya üretici:** Bu bölüm virüsün yayılmasını,kendisini bir programdan diğerine kopyalamasını yani kısacası üremeyi sağlarlar. Virüslerin VİRÜS ismini alması temelde bu kısmın gerçekleştirmiş olduğu işlevden gelmektedir.

**Gizleyici:** Virüsün fark edilmemesi için gereken işlemleri yerine getirir. Bu bir tür savunma mekanizmasıdır. Virüs yazarlarının antivirüslere karşı geliştirdikleri teknikler sonucu ortaya çıkmıştır. Amacı antivirüslerin ve kullanıcıların kendilerini tespit etmesini, antivirüslerin bilgisayar üzerinde çalışır durumda iken etkisiz hale getirilmesini sağlamaktır.

**Bomba:** Bu bölüm virüs içerisinde yazarın istekleri doğrultusunda şartlar gerçekleştiğinde yapılması gereken olayı icra eden kısımdır. Virüs yazarının durumuna göre basit bir şaka veya korkunç bir HDD formatı olabilir.

**Virüslerin yazılma metodları**

Virüsler tip ayrımının yanı sıra, iki farklı metodla yazılabilir.

1. Nonresident virüsler (Run - time virüsler)

2. Resident virüsler

bütün virüsler temelde iki farklı şekilde çalışırlar. Bu ayırım virüslerin kendisinden değil DOS ortamında çalışan programlara sağlamış olduğu imkanlardan kaynaklanır. İyi bir virüsün yazılabilmesi ancak resident biçimi ile mümkündür. Bu gruptaki virüsler ileri teknikler kullanırlar.

**Nonresident virüsler**

Nonresident virüsler ister DOSYA virüsü olsun ister BOOT sektör virüsü olsun bulaşma işini, kendileri aktif oldukları anda ilk buldukları diğer hedef bulaşma alanlarına kendilerini bir veya birden fazla kopyalayıp daha sonra kontrolü ana programa, boot sektör virüsü ise işletim sistemine bırakan virüslerdir. Bu tip virüsler için bir sonraki bulaşma işlemini, aynı şekilde yani tekrar çalıştıklarında gerçekleştirirler. Kısacası bu virüslerin yayılabilmesi için muhakkak bulaşılmış bir dosyanın çalıştırılması gerekmektedir. Aynı durum boot sektör virüsleri de geçerlidir. Nonresident virüsler zor fark edilirler çünkü sadece program çalıştırıldığında aktif hale gelip, yapmaları gerekeni yaptıktan sonra kontrolü ana programa vererek devre dışı kalırlar. Hafıza haritalarında gözükmezler. Bu nedenle fark edilmeleri oldukça zordur.

**Resident Virüsler**

Resident virüslerin nonresident virüslerden tek farkı adından da anlaşılacağı gibi hafızada sürekli çalışır durumda olmalarıdır Bu tip virüsler hafızada aktif halde bekleyerek kesmeler vasıtası ile bulaşma işlemini gerçekleştirirler.

**VIRÜS TIPLERI**

Virüsler üzerinde yazılmış oldukları bilgisayar sitemlerine göre şekil alırlar. Üzerinde çalışılan donanım ve sistem programı virüslerin tipleri üzerinde belirleyici olarak etkin rol oynarlar.

**Worms (Solucanlar):** Adını aldıkları canlılara benzeyen bu virüsler, girdikleri bilgisayar sistemimde birtakım 'delikler' açar. Kendilerini kopyalama özelliğine sahiptirler. İnternet yada yerel ağ üzerinde bilgisayardan bilgisayara yayılırlar. Bazıları zararsızdır ancak sistemde yer kaplar ve bilgisayarı yavaşlatırlar. Bazıları ise zararlıdır ve bilgisayara zarar verir.

**Trojan Virüsleri:** Bu virüsler kendilerini kopyalayıp çoğalmazlar. Bilgisayara girdiklerinde kendisini özellikle gönderen kişinin buyruğuna girer ve ona hizmet ederler. Eğer bu hizmet kötü niyetli bir kişiye yapılıyorsa bu kişinin keyfiyetine bağlı olarak bilgisayarınızdaki bilgileri kaybedebilir, istemediğiniz bilgilerin bilgisayarınıza girmesini sağlayabilir, gizli dosyalarınıza ulaşabilir,modem yada hard diskiniz bozulabilir.

**Makro Virüsleri:** Word Excel gibi makro kullanımına olanak sağlayan programların dosyalarına bulaşan virüslerdir. Bunlar Word yada Excel kullanarak hazırladığınız belgeye yerleşir ve bu belgeye her girişte aktif hale geçer.

**Boot Virüsleri:** Disketlerin 'boot sector' veya sabit disklerin 'master boot sector' diye isimlendirilen ilk sektörlerine sıçrarlar ve çoğalarak diğer bilgisayarlara disketler, e.mail gibi yöntemlerle bulaşır ve yayılırlar. Bulunması ve temizlenmesi en kolay virüslerdir çünkü yerleri bellidir.

**Dosya Virüsleri:** Com, Exe gibi çalışabilir dosyalara bulaşırlar ve bu dosyalardan diğer dosyalara sıçrarlar. Ne kadar dosyaya sıçradıklarına bağlı olarak dosyanın boyutunu arttırırlar. Dosyaya bulaşan virüs yazılımı dosyanın sonunda bazende ortasında olabilir. Bu virüsler hafızada kalabilme özelliğine sahiptirler.

**Polimorfik Virüsler:** Sürekli olarak kendini değiştiren virüslerdir. Bulunması ve temizlenmesi farklı teknoloji gerektiren bir virüs türüdür.

**Hoaxlar:** Hoaxlar virüs olduğu söylenen fakat aslında virüs olmayan aldatmacalardır. Bunlar sadece kullanıcılarda panik yaratmak için hazırlanmış olabileceği gibi daha sonradan yazılacak bir virüsün etkisini artırmak amacıyla da hazırlanmış olabilir.

**ANTIVIRÜS PROGRAMLARI**

Antivirüs programlarının işleyişini genel olarak 3 ana gruba ayırmak mümkündür. Bunları tespit etme, tanımlama ve temizlemedir.

Her virüs belli bir uzunlukta makine kodu yığınından oluşur. Bu kodlar her virüs için değişiktir ve virüsler bir dosyaya bulaştıklarında bu kodlar bulaşılan dosya üzerine yazılmış olur. Antivirüs programlarının ise virüslerin %95 oranındaki büyük bir bölümü için kullandığı teknik son derece basittir. Virüs üzerinde yapılan inceleme sonucu virüsün her kopyasında sabit kalan mümkün olduğunca uzun(yanlış alarma düşme ihtimalini azaltmak için) kod dizimini aramaktır. Bu şekilde binlerce virüsün imzası bir dosyada toplanır. Daha sonra virüs taraması yapılacak her dosyada bu binlerce imzanın her biri aranır. İmza bulunduğu takdirde dosyaya virüs bulaşmış demektir. Bunlardan sonraki aşama temizleme kısmıdır. Bilinen klasik tarzda yazılmış virüslerin hepsi bu metotla temizlenebilmektedir. Bu metodun dezavantajı yeni çıkan virüslere karşı etkisiz olmasıdır. Bundan dolayı antivirüs programlarının sık sık update edilmesi gerekir.

Başka bir antivirüs tekniğinde aşılama tekniğidir. Bu teknik virüslerin çalışabilir dosyalara bulaşmak için kullandığı tekniği kullanır. Fakat bu defa bulaşan virüs değil virüsün bulaştığını fark edebilecek bir kod bölümünü programa eklemekten ibarettir. Eklenen bu kod, program her çalıştığında kendi kendisini kontrol etmesini ve temizlemesini sağlar. Aşılama tekniğinde çalışabilir her dosyaya bu program parçasının bulaşması sağlanır.

**Virüsün Bulaştığına Dair Şüphe Edilecek Durumlar:**

Bazı virüsler bilgisayar üstünde bulunan tüm sürücüleri bulaşılacak dosya bulmak için tarar. Örneğin disketten çalıştırdığınız bir program harddisk üzerinde hiçbir işlem yapılmasına gerek yokken , harddisk’e erişim gerçekleştiriyorsa bunu büyük ihtimalle virüs yapmaktadır.

Antivirüs programları veya kontrol dosyaları siliniyorsa , yanlışlıkla kendiniz silmediyseniz bunu yapan büyük ihtimalle virüstür.

RAM belleğinizin miktarı belirgin olmayan bir şekilde azalmış ise hafızada bir virüs aktif halde olabilir.

Harddisk’inizin çalışma hızının sebepsiz yere düşmesinde virüslerden kaynaklanıyor olabilir.

Eğer bilgisayarınızın ve programlarınızın çalışma hızı beklenmedik bir şekilde düştü ise resident bir virüsün hafızada aktif olması ihtimali oldukça yüksektir.

**Virüsün Bilgisayara Bulaşabilme Yolları: **

Temiz olduğuna emin olamadığınız disketlerden

Bir program yüklemek amacı ile kullandığınız CD’lerden.

E-maillerden ve e-mail yolu ile alınmış dosyalardan.

Çeşitli karşılıklı görüşme programları (Mirc, Icq) ve bunlar aracılığı ile alınan dosyalardan.

Ağ komşularından bağlı olduğunuz virüslü bir bilgisayardan (ağ paylaşımı açık olduğu durumlarda)

**Virüslerden Korunma yolları**

İyi bir antivirüs programı yüklenmesi ve bunun düzenli bir şekilde update edilmesi.

Kullandığımız bilgisayarlarda gelişigüzel her disketin kullanılmaması.

İşimize yaracağını kesin olarak bilmediğimiz, güvenilir olmayan kişilerden alınan cd’lerin kullanılmaması ve bunlardaki programların yüklenmemesi.

Tanımadığımız kişilerden gelen e-mailleri gerekirse hiç açmamak, özellikle sonu exe olan dosyalar karşı temkinli davranmak.

Ağ paylaşımlarına hiçbir zaman tam paylaşım vermemek, paylaşım verilmesi gerekiyorsa parolaya bağlı paylaşıma verilmesi.

**Notlar:**

Virüsler kendiliğinden oluşmaz. Bir programcı tarafından yazılması gerekir.

İyi niyetli virüslerde vardır.

Virüsler, bir disket yada program makinede çalıştırılmadığı sürece bulaşmaz.

Disketten bilgi okunması virüs bulaştırmaz.

Protect (koruma) yuvası kapalı olan disketin virüs bulaştırma olasılığı daha azdır.

Virüsler, veri (data) dosyalarına bulaşmazlar.

---
*Kaynak: `VİRÜSLER/VİRÜSLER.doc` — Innkeeper — 2004*
