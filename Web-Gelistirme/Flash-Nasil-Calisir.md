# Flash Nasil Calisir

FLASH NASIL ÇALIŞIR?

Flash içeriği iki dosya kullanılarak yaratılır ve dağıtılır:Bir **kaynak dosya** (bunda içeriği, animasyonu ve etkileşimi yaratacaksınız)ve daha çok **flash filmi** adıyla bilinen,bu dosyanın sıkıştırılmış ve optimize edilmiş bir versiyonu.

Kaynak dosya(.fla uzantısına sahiptir),daha sonra üzerinde uğraşmak üzere çalışmanızı kaydedeceğiniz yerdir:Bu, Flash açıkken üzerinde çalıştığınız dosyadır.son filminizde yer alacak tüm sesleri , bitmap’leri,çizimleri metni ve etkileşimi içerir.kaynak dosya,filminizin *optimizasyon öncesindeki *halidir; yani bu dosyanın boyu megabyte’larca bile olabilir.

Kaynak dosyanız,istediğiniz gibi göründüğünde ve çalıştığında, onu bir flash filmine dönüştürmenin zamanı gelir. Bu işleme **ihraç etme** (export) adı verilir.Kaynak dosyanızı bir filme (.swf dosya uzantısına sahiptir)ihraç ettiğinizde,flash onu sıkıştırır ve optimize eder;bu sayede Flash filminin boyu, orjinan kaynak dosyasına göre çok daha küçüktür(şekil2.1).Bu daha küçük olan dosyayı web sayfanıza koyar veya bir disket veya cd üzerinde dağıtırsınız. Çoğunlukla, ihraç edilen film düzenlenemez.filminizin içeriğini düzenlemek isterseniz,orijinal kaynak dosyayı tekrar açmalı, istediğiniz değişiklikleri yapmalı ve sonra kaynak dosyayı tekrar bir flash filmine ihraç etmelisiniz.

Flash filminizin boyunu etkileyen pek çok etken vardır ve bunların çoğunu kontrol edebilirsiniz son filmde en küçük dosya boyunu elde etmek,genellikle bir denge ve seçime bağlı bir fedakarlık meselesidir.İhraç edeceğiniz dosyanın boyunu küçültmek için, ne zaman ve nerede kaliteden ödün vereceğinize karar vermelisiniz(örneğin,sesin berraklığı veya resimlerin keskinliği gibi).Flash’ın araçlarını kullanarak makul bir dosya boyunu korurken en iyi kalitede son filmi nasıl elde edebileceğinizi göstereceğiz.

Kaynak dosyalarınızdan yaratabileceğiniz tek şey flash filmleri değildir; bu dosyaları Quick time filmleri,animated GIF’ler (hareketli GIF)ve durağan yada hareketsiz grafikler halinde de ihraç edebilirsiniz;Flash bunların tümünün aynı anda yarata bilir!Bu, kaynak dosyayı yarattıktan sonra ,onu çeşitli şekillerde dağıta bileceğiniz anlamına gelir(Flash filmi,Quick time filmi ,animated GIF,JPEG vb..)

**İçeriğin yaratılması ******

Flash projeleri sunular, öğreticiler,ürün demoları slayt gösterileri hatta oyunlar dahil olmak üzere pek çok farklı şekle bürünebilir.Bazı Flash projeleri etkileşimi kullanırken az miktarda animasyon kullanabilir,bazıları da hareketli grafikleri kullanırken az miktarda etkileşim içerebilir.

Projenizin alanı ne olursa olsun,çalışmanız tipik olarak şu şekilde ilerler:

1.Flash’ta grafikleri çizmek veya ithal etmek

2.Düğmeleri,bagımsız animasyonları ve tekrar kullanmak istediğiniz öğeleri semboller haline dönüştürmek.

3.film öğelerini Stage’e yerleştirmek(vektörler grafikler,bitmap’ler ve semboller dahil olmak üzere).

4.Etkileşimli hale getirmek için, timeline’de (zaman çizgisi) düğmelere film kliplerine (movie clip)ve karelere eylemler eklemek.

5.Stage’de bir kareyi,sembolü,dış hattı,dolguyu veya metin bloğunu seçerek,çeşitli panellerle özeliklerini ayarlamak.

Flash’ın çalışma şekli hakkında aklımızda tutmamız gereken birkaç şey var : Stge’de görmekte olduğumuz şey, Timeline’deki geçerli karenin içeriğini temsil eder. Oynatım kafasını farklı bir kareye götürdüğümüzde Stegedeki sahnede değişir.Animasyon,stagedeki içerik kareden kareye düzenleyerek yaratır ve kareler sıralı ardışık bir şekilde hızla gösterilir Timeline’ımızın içerdiği karelere de çalışmayı kolaylaştırmamız için Flash kaynak dosyayı **sahnelere** (scenes) ayırmanıza izin verir sahneleri her biri diğerlerinden tamamen farklı görünen kaynak dosyanızdaki sayfalar gibi düşüne bilirsiniz.Nir kaynak dosya istediğiniz sayıda sahne içere bilir; ancak bu sahnelerin tümü ihraç edilen bir tek filmin parçalarıdır. Sahneler,Timeline idare edebilir. Kısımlara ayırarak yaratım ortamında içeriğin oluşturmasını son derece basitleştirir.

**İçeriğin Dağıtılması**

Kaynak dosyada içeriğinizi yarattıktan sonra, onu bir flash filmi olarak ihraç etmeniz ve sonuçtaki optimize edilmiş,SWF dosyasıyla ne yapmak istediğinize karar vermeniz gerekir. Seçeneklerden biri,filminize bir Web sayfasına gömmektir;burada normal bir grafik gibi görünür,sadece etkileşimli ve hareketlidir.Aslında ,bir Web sitesinin tümünü tek bir flash filmiyle yaratmanızda mümkün.İzleyicilerinizin filminizi görmesini istediğiniz durum buysa.onu izleyebilmeleri için sistemlerinde Flash plug-in’inin kurulu olmasının gerektiğini unutmayın.

Flash filminiz Web üzerinde akar bu sayede filmin geri kalan kısmı arka planda yüklenirken,izleyicileriniz neredeyse anında filmi izlemeye başlaya bilir. Film oynatılırken ,Flas’a tarayıcı pencerelerini açmasını ve kapatmasını,kullanıcıdan bilgi almasını(bu bilgi bir CGI script’i tarafından işlenebilir ),sesleri çalmasını,kullanıcıyla etkileşmesini ve daha çok şeyi bildire bilirsiniz.

Flash filminizi sunmanın bir diğer popüler şekli, onu kendi başına çalışan bir uygulamaya dönüştüren bir **projektör **(projektör) veya bağımsız bir **oynatıcı** (player) haline getirmektir.Bu filminizi bir diskete veya CD’ye koyduğunuzda , sadece onu açarak herkesin anında filminizi izleyebileceği anlamına gelir.(Flash plug-in ‘ine sahip olmasalar bile).Flash’ın yeni script motoru ve Web sunucularıyla iletişim için desteği sayesinde,projektör dosyasıyla dağıtabileceğiniz eksiksiz ve güçlü Flash uygulamaları yaratabilirsiniz.işin aslı, Web sitenizin tümünü Flash’ta yaratarak,onu Web’e koyabilir ve müşterilerinize de disket veya CD-ROM’da verebilirsiniz.

Flash projenizi bir QuickTime filmine,bir Windows AVI dosyasına,hatta bir Real Player dosyasına dönüştürmeniz de mümkün. İhtiyaçlarınız ne olursa olsun, büyük ihtimalle Flash bu işi kolayca yapabilir.

**Flash 5‘te Neler Yeni?**

Macromedia,sadık Flash geliştiricileri topluluğuna gelecek kuşağın multi medya içeriğini yaratmalarını sağlayacak yeni bir araç sunmak için hiçbir şeyden kaçınmamış. Genel arabirimde bazı değişiklikler olurken (bunu yakında göreceksiniz),gelişmelerin çoğu yeni araçlar veya Flash’ın yeteneklerinin geliştirilmesi şeklinde.

Uzun süredir Flash kullanıyorsanız bile,bu son sürümü alışmak için kısa bir süreye ihtiyat duyabilirsiniz.Alıştıktan sonra ,işlerin çoğunu daha hızlı ve etkili bir şekilde yapabildiğinizi göreceksiniz.

Şimdi Flash 5’teki gelişmeleri ve ilaveleri özetleyeceğiz.(bunların tümü daha ileride ayrıntılı olarak açıklanacak):

**Genel Macromedia arabirimi: **Çeşitli üretim araçlarıyla çalışmayı daha kolay hale getirmek için,Macromedia Flash’ın arabirimini diğer geliştirme araçlarına (Dreamweaver,Fireworks vs.)benzeyecek şekilde değiştirildi.

**Pen aracı: **Artık Flash ile birlikte profesyonel vektörel çizim programlarında bulunan araca benzer bir Bezner **pen** aracı geliyor. **Pen** (kalem) aracı, kullanıcılara vektör el grafiklerin yaratılmasında ve düzenlenmesinden daha fazla hassaslık sağlıyor

**Paneller: **Genel arabirimdeki en büyük değişiklerden birini temsil eden paneller bir öğenin seçeneklerini ve parametrelerine hızlı erişimi sağlıyor. Pek cen sıkıcı iletişim kutusunun yerine geçen paneller iş akışını çok daha iyi bir hale getiriyor.

**Sürüklene bilir kılavuzlar:**Başka bir vektör el çizim programını kullanmış olsanız bile sayfa düzeninde nesneleri yerleştirmek ve düzenlemek için yerleştirebileceğiniz sürüklene bilir kılavuzlara aşık ola bilirsiniz. Bu sayfa düzeninin geliştirilmesi özellikle flash’ın animasyon ortamında son derece yararlı.

**Seçimlerin vurgulanması:**Grafiksel bir öğenin seçim kutusu, artık üzerinde bulunduğu katmanın rengini gösterebilir; bu seçilen bir öğenin hangi katman üzerinde bulunduğunu çabucak belirlemek için yararlıdır.

**Daha iyi renk desteği:** Flash artık renklerin seçimi ve mükemmel şekilde eşleşen renklerin yaratılması için profesyonel düzeyde bir **Eyebropper **(Damlalık) aracına sahip olduğundan renklerin ve gradyentlerin yaratılması ve düzenlenmesi artık çok daha kolay. Bunun yanı sıra başka gelişmiş renk araçları da var .

**Paylaşılan kütüphaneler:** Flash içeriği geliştiren bir çalışma grubundaysanız veya filminizin öğeleri üzerinde kolayca versiyon denetimi yapa bilmeyi istiyorsanız ihtiyacınız olan şey paylaşan kütüphaneler. Onlar film öğelerini merkezi bir kütüphaneye yerleştirmenizi izin verir, böylece herhangi bir flash projesinde onlara bağ kurabilirsiniz. Bir paylaşılan kütüphanenin içindeki bir öğeyi düzenlerseniz kütüphaneye bağ öğeleri içeren projelerde bu düzenlemeleri yansıtır.

**Font srmbolleri:** Font sembollerini kullanarak filminizdeki metin öğelerini yazı tipini değiştirmeniz kolaydır.bu bir HTML dokümanında Cascalding Style Sheets (CSS) ile sağlanan işlevselliğe benzer.

**Smart clip’ler:**Smart Clip’ler sayesinde (bunlar action script ile işlevsellik kazandırdığınız film klipleridir), menüler, liste kutuları ,vb. pek çok film öğesine kolayca yarata bilirsiniz .

**Macromedia Freehand ve Fireworks dosyalarıyla daha iyi entegrasyon: **Filminiz için vektörel içerik yartmakta Freehand ‘i ve ithal edilecek bitmap’leri yaratmakta fireworks’ü kullanıyorsanız , artık bu dosyaları doğrudan ithal edebilirsiniz; bu sayede katmanlar ve metin blokları korunur ve nesneler düzenlenebilir halde kalır.

**Özelleştirilebilir klavye kısayolları:** klavye kısayolları üzerinde tam kontrol istermisiniz? Flash 5 bunu size sağlar: çeşitli klavye kısayolu gruplarını kulanmamızaizin verirken (Fire works ve Photoshop’ın kısayolları gibi),kendi kısayol grubunuzu sıfırdan yaratmamıza da izin verir.

**MP3 ithali:**Flash 4,bizlere Flash projesinin seslerini MP3 forma tında ithal etme imkanını sağladı,ancak mp3 dosyalarını ithal etmemize izin vermedi artık mp3 dosyalarınıda ithal edebilirsiniz yani kaynak dosyalarınız çok daha küçük olabilir.

**HTML destekli metin blokları:** Flash da ki metin blokları artık HTML 1,0 biçimlendirmelerini koruyabiliyor;bu sayede metin bloklarını renklerle,farklı font boyutlarıyla,sitilleriyle ve hyprlinklerle biçimlendirebilirsiniz.

**Movie Explorer:** Bu yeni araç projenizin genel yapısını bir anda görmemizi sağlarken,öğeleri hızlıca bulup düzenlemeye ek olarak filminizi analiz etmenize de fırsat tanıyor.

**Yeniden yaratılan AsctionScript:**Flash geliştirme ekibi AsctionScript’i tümüyle dönüştürdü:artık javascript-benzeri söz dizimine ve eksiksiz bir matematiksel işlevler grubuna sahip.Artık ziyaretçilerimize filminizin öğeleri üzerinde daha fazla denetim sağlayabilirsiniz.

**XML Desteği:**Flas‘la uygulama geliştirmede ,karmaşık alış veriş kartları çok oyunculu oyunlar ve daha pek şey gibi yepyeni imkanlar sağlamak üzere,Flash yapılandırılmış verilerle çalışa biliyor ve işleye biliyor.

**Yazdırılabilen filmler:**İçeriğinizi dijital ortamın ötesine taşıya bilir ve ziyaretçilerinizin filminizdeki bir düğmeyi veya bir kare eylemini kullanarak bireysel kareleri ve tüm filmi yazdırmasını sağlayabilirsiniz.Yazdırılabilir filmler kuponların ,ürün bilgilerinin dağıtılmasında kullanılabilir.

**Hata ayıklayıcı: **Flash projelerinin giderek daha karmaşıklaşması yüzünden,bir flash tasarım ekibinin ActionScript’lerde ve bir film işlevlerindeki hataları ayıklamak için bir yol bulması gerekir.Yeni **Debugger **(hata ayıklayıcı ) aracı,bu işi mümkün olan en etkili şekilde yapmamıza izin verir.

**Arabirim**

Macromedia ,Flash 5’in yeni arabirimini daha kullanıcı dostu ve sezgisel hale getirmiş;Bu,daha kısa bir öğrenme eğrisiyle daha verimli iş akışı anlamına geliyor.diğer Macromedia ürünlerini kullandıysanız,programlar arasındaki benzerlikleri fark edeceksiniz: **Launcher **çubuğu,araç çubuğundaki araç ikonları , menü komutlarının yerleri ve projenizde çalışırken panellerin kullanımı gibi.

Flash 5’in arabirimi ile taşınarak,araç çubuklarının,menü çubuğunun, bağlam menülerini, panelleri,vs. nasıl özelleştirebileceğinizi öğrenmenin zamanı geldi**.**Her aanı daha yakından incelemeden önce, arabirime genel olarak bakacağız.Timeline ve katman arabirimi gibi bazı alanlar, animasyon ve katmanlarla ilgili bölümlerde daha ayrıntılı olarak ele alınacak.

**Araç Çubukları**

** **Flash’ın Macintosh versiyonun bir **Drawing **(çizim)** **araç çubuğu sunmasına karşı, windpws versiyonunda iki temel araç çubuğu vardır.** Standart ve drawing **araç çubuğu. Bu proğramın, iki işletim sisteminde gösterdiği az sayıdaki farklılıklardan biri budur.

**standart **araç çubuğu (sadece Windows’ta) , aksi halde sadece menüler den erişebilecek pek çok işleve hızlı erişim sağlar. Bunların arasında yeni proje yaratmak,açmak, kaydetmek, yazdırmak,kesmek,kopyalamak, yapıştırmak gibi sık kullanılan komutlar için düğmeler bulunur.** **

**Drawing** araç çubuğunda , flash’ın yaratım araçları seti eksiksiz olarak bulunur.

**Controller **filmimize yaratım ortamında oynatmak,durdurmak ,geri almak,ve hızlı ileri almak için vişdeo kumandasına benzeyen bir kontrol aracıdır.

Windows’da, **standart, drawing ve controller** araç çubukları ekranın bir kenarında sabitlene bilir veya kayan duruma getirilebilir. Macintosh bilgisayarlarda, araç çubukları ara birimde sabitlenemez herzaman kayan durumdadır.

**Hangi Araç Çubuklarının Görüneceğini Ayarlamak **

Bir araç çubuğunu görünür hale getirmek için menü çubuğundan window>toolbars’ı,sonra aşağıdaki seçeneklerden birini seçin.Görünür durumdaki araç çubuğun isminin yanında bir işaret görünür,görünmeyen araç çubuğunun yanında işaret bulunmaz.

**Main Standart **araç çubuğunu görmek için işaretleyin

**Status **Durum çubuğunu görmek için işaretleyin

**Controller controller’i **(kontrolcü) görmek için işaretleyin.

**Hangi Araç Çubuklarının Görüneçeğini Ayarlamak (Macintosh)**

Menü çubuğundan **window>tools**’u seçerek **draving **araç çubuğunu,ya da **window>controller’i** seçrerek **controller’i** görünür(yanında işaret belirir) veya görünmez (yanında işaret yoktur)hale getirebilirsiniz.

**Menü Çubuğu**

Menüler pek çok flash komutunu erişim sağlar.Menüdeki bir seçeneğin sağ tarafındaki ok işareti,bir alt menüyü belirtir.Menü komutlarının klavye kısayolları,bazı komutların sağında gösterilir.**Flash projesi ve proje **terimleri,Flash kaynak dokümanlarını belirtmektedir:Yani muhtemelen bir Flash filmi olarak ihraç etmek üzere,içeriği yarattığınız yerdir.

**File Menüsü**

**File **menüsünü,dosyaları yaratmak,açmak ve kaydetmek için kuluanaçaksınız

**New:**Yeni bir Flash belgesini yaratır.

**Open:**Mevcut bir flash projesini açar.

**Open as library:**Başka bir Flash projesinin kütüphanesini açarak,öğelerinin açık olan geçerli projeye eklenmesini ve kullanmasını sağlar.

**Open as Shared** **library:**Paylaşılan bir kütüphaneyi açar,öğelerin o anda açık olan geçerli projede kullanmasını sağlar.

**Close:**Geçerli Flash projesini kapatır.

**Save:**Geçerli projeyi kaydeder.

**Save as:**Yeni bir projeye isim vermemizi veya mevcut projelerden birinin adını değiştirmemizi sağlar.

**Import:**Ses, bitmap,QucikTime videosu ve diğer dosyaları ithal eder.

**Export Movie:**Geçerli Flash projesini bir Flash filmine, QuickTime filmine,Animated GIF’ e veya bir hareketli diziye ihraç eder.

**Export İmage:**Stage’deki içeriği kullanarak durağan bir görüntü yaratır.

**Publish Settings:**Flash projemizi HTML’ye,QuickTime’a ve diğer fortmalara ihraç etmek için ayarları yapmamızı sağlar.

**Publis preview:Puplish Settings** seçeneğinde seçtiğiniz ayarlara göre,geçici bir ön izleme dosyası ve dosyaları yaratmanızı sağlar.

**Publis:Publish Settings** seçeneğinde seçtiğiniz ayarlara göre bir dosya yaratır.

**Page Setup:**Sayfa yapısı ayarlarını yapar.

**Print Preview:**Projenizin ön izlemesini **Page Setup **(sayfa düzeni).ayarlarıyla gösterir.

**Print:**Projenin karelerini yazdırır.

**Send**(Windows): Geçerli dokümanı bir e-posta mesajına ekler.

**Edit Menüsü:**

Edit menüsündeki seçenekler dosyaların üzerinde çalışmamızı kolaylaştırır(şekil 2.6)

**Undo:**son eylemimizi geri alır.

**Redo:**Geri aldığınız eylemi yeniden uygular.

**Cut:**Seçilen içeriği keserek panoya (clipboard) yerleştirir.

**Copy:**Seçilen içeriği kopyalayarak panoya yerleştirir.

**Paste:**Panodaki geçerli içeriği yapıştırır.

**Paste in Place:**Panodaki geçerli içeriği,Stagedeki kesildiği veya kopyalandığı izafı konuma yapıştırır.

**Paste Special:**Diğer programlarda içerik yapıştırır.

**Clear:**Stage ‘deki seçili durumdaki öğeleri siler.

**Duplicate:**stegedeki seçili durumdaki öğelerin kopyasını yaratır.

**Select All:**Stegedeki her şeyi seçer.

**Deselect All:** Stagedeki seçili olan her şeyi seçimden çıkarır.

**Cut Frames:**Timelinede seçilen kareleri keserek panoya (ClipBoard) yerleştirir.

**Copy Fremes:**Timelinede seçilen kareleri kopyalayarak panoya (clipboard) yerleştirir.

**Paste Frames:**Panodaki kareleri Timeline’ye yapıştırır.

**Edit Symbols:**En son düzenlenen sembolü stagede ve timelinede düzenleye bilmemiz için senbol düzenleme moduna sokar.(Bir sembolü düzenlerken,bu seçenek **Edit Movie** haline gelir)

**Edit Selected:**Seçilen bir sembolü,sembol düzenleme moduna geçirir.

**Edit All:** Tüm içeriği düzenlene bilir hale getirir.

**Preferences:**Flash’ın bazı özelliklerini özelleştirmemizi sağlar.

**Keyboard Shortcuts:**Klavye kısayollarını değiştirmekte,düzenlemekte veya kendi kısayollarınızı yaratmakta kullanabileceğiniz.Bir iletişim kutusunu açar.

**View Menüsü**

Bu menüdeki seçenekleri projenizin nasıl göründüğünü kontrol etmek için ve Flash’ın sunduğu çeşitli sayfa düzeni özellikleri için kullanacaksınız.

**Goto:**Filminizdeki sahneler veya kareler arasında dolaşmanızı sağlayan bir alt menüyü açar.

**Zoom In:**Stage’yi yakınlaştırır.

**Zoom Out:**Stage’yi uzaklaştırır.

**Magnification:**Stage’in büyütülme oranını seçebileceğiniz bir alt menüyü açar.

**Outlines:**Nesnelerin hızlı bir şekilde çizilmesi için stage’deki tüm nesneleri dolgusuz dış hatlar haline getirir.

**Fast:**Nesnelerin Hızlı çizilmesi için Antialiasing’i kapatır.

**Antialias:**Yazılar haricindeki tüm stage nesnelerinin kenarları yumuşatır.

**Antialias Text:**Yazı da dahil olmak üzere stage’deki tüm nesnelere Antialiasing uygular.

**Timeline:**Timelineyi(zaman çizgisi)güösterir veya gizler.

**Work Area:**Stage’in çevrisindeki çalışma alanını gösterir veya gizler.

**Rulers:**Yatay ve dikey cetvelleri gösterir veya gizler.

**Grid:**Çeşitli ızgara seçeneklerini ayarlayabilmemiz için bir alt menüyü açar.

**Guides:**Çeşitli klavuz seçeneklerini ayarlamanız için bir alt menüyü açar.

**Snap to Objects:**kenetlemeyi açar veya kapatır.

**Show Shhpe hints.**Bir shape tween’in parçası olan nesneler üzerinde şekil ipuçlarının yerlerini gösterir.

**Hide Edges:**Stage’deki seçili öğelerin çevresinde seçim kutusunu gösterir veya gizler.

**Hide Panels:**Panelleri gösterir veya gizler.

**Insert Menüsü **

**Insert** menüsü kareler ve katmanlar üzerinde kontrol sağlar.

**convert to symbol:** Stage’de seçilen tüm nesneleri sembolleri dönüştürür.

**New Symbol:**Yeni,boş bir sembol yaratır.

**Layer:**Timeline’da geçerli katmanın üzerinde,yeni,boş bir katman yaratır.

**Motion Guide:**Geçerli katmanı üzerinde yeni bir **Motion Guide**(hareket klavuzu) katmanı yaratır.

** Frame:**Seçilen karenin sağında yeni,boş bir kare yaratır.

**Remove Frames:**Timeline’da seçilen kareyi (kareleri) siler.

**Keyframe:**Timeline’da seçilen kareyi bir anahtar kareye dönüştürür; bu anahtar kare katmandaki son anahtar kareyle aynı içeriğe sahiptir

**Blank Keyframe:**Timeline’da seçilen kareyi boş bir anahtar kareye dönüştürür.

**Clear Keyframe:**Seçilen anahtar kareyi normal bir kare haline dönüştürür.

**Create Motion Tween:**Seçilen katman ve karedeki tüm nesneleri bir sembole dönüştürerek,**Motion Tween** uygulanabilmesini sağlar.

**Scene:**Flash projemize yeni bir sahne ekler.

**Remove Scene:**Geçerli sahneyi Flash projemizden kaldırır(Projemizde sadece bir tek sahne varsa,kullanılamaz).

**Modify Menüsü**

**Modify **menüsünü kullanarak,projemizdeki çeşitli öğeleri düzenyecek veya özelliklerini değiştireceksiniz.

**Instance:** Seçilen Örneğin özelliklerini ayarlayabileceğimi **Instance** panelini açar.

**Frame:**Seçilen karenin özelliklerini ayarlayabileceğiniz **frame** panelini açar.

**Layer:**Seçilen katmanın özelliklerini ayarlayabileceğiniz **Layer properties** iletişim kutusunu açar.

**Scene:**Geçerli sahnenin adını değiştire bileceğiniz **scene** panelini açar.

**Smooth:**Stage’de seçilen çizgiyi (veya çizgileri)yumuşatır.

**Straighten:**Stage’de seçilen çizgiyi(veya çizgileri)düzleştirir.

**Optimize:**Seçilen bir Vektörel grafiğin(veya grafiklerin)üzerindeki gereksiz noktaları kaldırarak, onu dosya boyu açısından daha verimli hale getirmenizi sağlayan bir iletişim kutusunu açar.

**Shape:**Çizgi ve şekillerin düzenlenmesi için seçenekler içeren bir alt menüyü açar.

**Trace Bitmap:**Seçilen bitmap’i vektörel grafiğe dönüştürmek üzere ayarları yapabileceğiniz **Trace Bitmap** iletişim kutusunu açar.

**Transform:**Seçilen nesne veya şeklin dönüştürülmesi , düzenlenmesi ve şeklinin değiştirilmesi için seçenekler içeren bir alt menüyü açar.

**Arrange:**Nesnelerin** ***yığılma sırasını* değiştirmek,onları kilitlemek veya kilidini çözmek için seçenekler içeren bir alt menüyü açar.

**Group:**Seçilen nesneleri gruplar.

**Ungroup:**Seçilen nesne grubunun grubunu çözer.

**Break Apart:**Seçilen metni şekillere* *dönüştürür,seçilen sembolü onu oluşturan bireysel şekillere parçalar veya bir bitmap’i düzenlenebilen bir nesneye dönüştürür.

**Text Menüsü**

**Text **menüsü.seçili durumdaki yazının çeşitli seçeneklerini ayarlamamızı sağlar.

**Font: **Seçilen metnin yazı tipini değiştirmeniz için sistemde kurulu yazı tiplerinin listesini açar.

**Size:**Seçilen metnin boyunu değiştirmenizi sağlar.

**Style:**Seçilen metnin stil özelliklerini ayarlayabileceğiniz bir alt menüyü açar.

**Align:**Seçilen metnin hizalama özelliklerini ayarlayabileceğiniz bir alt menüyü açar.

**Tracking:**Seçilen metnin karakterlerinin aralığını ayarlayabileceğiniz bir alt menüyü açar.

**Character:**Seçilen yazının tüm karakter seçeneklerini hızlı düzenlemek için kullanılan **Character panelini gösterir veya gizler.******

**Paragraph:**Seçilen yazının tüm paragraf seçeneklerini hızlı düzenlemek için kullanılan **Paragraph** panelini gösterir veya gizler.

**Options:**Seçili durumdaki yazı bloğunun özelliklerini ayarlamakta kullanılan **Text Options** panelini gösterir veya gizler.

**Control Menüsü**

**Control **menüsü,filminizin nasıl çalışacağı,geliştirme ve test ortamında nasıl oynatılacağıyla ilgili çeşitli seçenekleri seçmenizi sağlar.

**Play:**Timeline’i geçerli konumdan itiberen oynatır.

**Rewind:**Timeline’i, geçerli sahnenin ilk karesine götürür.

**Step Forward:**Timeline’ı, geçerli konumuna göre bir kare ileri götürür.

**Step Back ward:** Timeline’ı, geçerli konumuna göre bir kare geri götürür.

**Test Movie:**Geçerli filmin geçici bir versiyonunu Flash’ın test ortamına ihraç eder.

**Debug Movie:**Hata ayıklama amacıyla, geçerli bir versiyonunu Flash’ın test ortamına ihraç eder.

**Test Scene:**Geçerli sahnenin geçici versiyonunu Flash’ın test ortamına gönderir.

**Loop Playback:**Geliştirme ortamında filminizi oynatırken,Timeline’ı son kareye ulaştığında Timeline’ı yeniden oynatır.

**Play All Scenes:**Geliştirme ortamında filminizi oynatırken,projedeki tüm sahneleri oynatır.Kapatıldığında,oynatım geçerli sahnenin karesinde son bulur.

**Enable Simble Buttons:**Düğmelerin,geliştirme ortamında imlece tepki olarak **Up,Over,Down **ve** Hit **durumlarını yansıtacak şekilde hareket etmesini ve düğme eylemlerinden bazılarını gerçekleştirmesini sağlar.

**Mute Sounds:**Tüm sesleri kapatır.

**Window Menüsü**

**Window** menüsü,Flash’ta çeşitli araç çubuklarına ve iletişim kutularına erişmenizi sağlar.

**New Window: **Geçerli sahneyi yeni bir pencerede açar.

**Toolbars:** (sadece Windows’ta):Hangi araç çubuklarını gösterip gizleyeceğimizi seçebileceğiniz bir alt menüyü açar.

**Tools:Draving**(çizim)araç çubuğunu gösterir veya gizler.

**Controller**(sadece Macintosh’ta):**Controller’i**(kontrolcü)gösterir veya gizler.

**Panels:**Hangi panellerin gösterileceğini veya gizleneceğini seçebileceğiniz bir alt menüyü açar.

**Panel sets.**Önceden kaydedilmiş bir panel düzenlenmesini seçebileceğiniz bir alt menüyü açar

**Save Panel Layout:**Geçerli panel düzenlenmesini daha sonra kullanım-lmak üzere kaydeder.

**Close All Panels:**Açık panellerin tümünü kapatır.

**Actions:**Actions panelini gösterir veya gizler.

**Movie Explorer**:Movie Explorer’ı gösterir veya gizler.

**Output**:Projenizdeki değişkenlerin değerlerini izlemenizi sağlayan **Output** penceresini gösterir veya gizler .

**Debugger:Debugger**(hata ayıklayıcı)aracını gösterir veya gizler.

**Library:**Filminizde tekrar kullanılabilen öğelerle çalışmanızı sağlayan **library **(kütüphane) penceresini gösterir veya gizler.

**Common libraries:**Genel kütüphanelerin listesini içeren bir alt menüyü açar.

**Generator Objects:**Bilgisayarınız da macromedia genarator kurulu olmadığı sürece bu seçenek gri renkte görülür.Generator kuruluysa, **Genarator Objects** (generator nesneleri)panelini gösterir veya gizler.

**Cascade:**Tüm açık pencereleri birbirinin üzerine yığmış görünecekleri şekilde basamaklar.

**Tile:**Tüm açık pencereleri yan yana döşer.

**Help Menüsü**

Yardım almak için Help menüsünü kullanın

**Using Flash:**Bir tarayıcı penceresinde Flash’ın online yardımını açar.

**ActionScript Reference:**Tafrayıcı penceresinde Flash online yardımının ActionScript kısmını açar.

**ActionScript Dictionary:**Tarayıcı penceresinde Flash online yardımının ActionScript sözlüğü kısmını açar.

**Macromedia Dashboard.**Flash’la ilgili son haberleri alabileceğiniz Flash tabanlı bir modülü açar.

**Bağlam Menüleri**

Flash’ta ana menü çubuğundan erişemeyeceğiniz pek çok menü daha vardır.***Bağlam menüleri*** olarak bilinen menüler, imlecin konumuna bağlı olarak komutlar sunar.Örneğin,imleciniz bir karenin üzerindeyken bir bağlam menüsünü açarsanız,o kareyle ilgili komutlara erişirsiniz Bu menüler fareyi fazla hareket ettirmede n uygun komutlara hızlıca erişmek için son derece yararlıdır.

**Bir Bağlam Menüsünü Açmak**

Bir araç,çubuğuna,Timeline’de bir kareye,stage’e veya Stage’deki bir nesneyle,panel ismlerine Flash’ın metin kabul edebildiği veya göstere bildiği her hangi bir alana,**Library** ön izleme penceresine,**library’deki Action** panelindeki veya **Movie Explorer** penceresindeki bir öğeye sağ tıklayın(Windows)veya **Control **tuşunu basılı tutarak tıklayın (Macintosh)

**Timeline- Zaman Çizgisi **

***Timeline***(zaman çizgisi),projenin içeriğini ve animasyonunu oluşturan kare ve katmanlarla çalıştığınız yerdir.Katmanlar,animasyonunuzdaki öğelerin yığılma sırasını temsil eder;Her katmanla ilişkili kare satırı da o katmanın öğelerinin zaman içinde nasıl hareket ettiğini temsil eder.Bir katmanı seçerek stage’de çizim yaptığınızda veya stage’e içerik ithal ettiğinizde bu içerik o katmanın bir parçası haline gelir.Hareket ve animasyonu yaratmak için,çeşitli karelerde katmanlar arasında içeriği taşır,içerik ekler,içerik üzerinde değişiklik yapar ve içeriği silersiniz.Timelinede yukarıdan aşağıya doğru sıralanmış çok sayıda katmanı kullanarak,animasyonunuzda derinlik yaratmak üzere farklı içerikleri farklı katmanlara yerleştire bilirsiniz(Örneğin,bir zemin üzerinde görülen nesneler gibi).

Stage ve çalışma alanına ayrılmış ekran alanını genişletip daraltarak ,Timeline’nin boyuna daha fazla veya daha az katmanı gösterecek şekilde ayarlaya bilirsiniz.Ayrıca Timeline’yi geliştirme ortamını üs tarafındaki varsayılan komutlardan ekranın her hangi bir kenarına sürükleyebilirsiniz.Yaptığınız işe baglı olarak yerini değiştirerek Timeline’de daha fazla kare veya daha fazla katman görebilirsiniz.

Timline’ın Boyunu Değiştirmek

1-İmlecinizi Timeline’yi stage’den ayıran çizginin üzerine getirin;İmleç çift başlıklı ok şeklini alır

**2-**Ayrıca ayırıcı çizgiye tıklayıp yeni konumuna sürükleyin ve farenin tuşuna bırakın.

Timeline’ı Ekranın Başka Bir Kenarına Taşımak

**1-**İmleci zaman cetveli üstündeki alana getirin ve tıklayarak sürükleyin siz sürüklerken,Timelinenin dış hattı belirir

**2-**Ekranın kenarına ulaştığınızda farenin tuşuna bırakın Timeline orada sabitlenir.

**Stage **

Stage, çizim yaptığınız ve filminizin içeriğini yerleştirdiğiniz dikdörtgen şeklindeki alandır.Sadece bu alanın içine yerleştirilen içerik ihraç edilir ve son filmde görünür halde olur.Belirli bir anda Stage’de gördüğünüz şeyler,geçerli karenin içeriğini temsil eder.

Stage,filminiz için arka plan vazifesi görür(varsayılan rengi beyazdır),Bu arka plan,filminizin son durumunda herhangi bir nesne tarafından kapatılmayan alanlarda görülür.Bir bitmap’i Flash’a ithal ederek,bir sahnenin en altdaki katmanına yerleştirebilirsiniz;böylece bitmap Stage’i kaplar ve bir arka plan haline gelir.

Stage’in Arka Plan Rengini Değiştirmek

1-**Modify **menüsünden **Movie**’yi seçerek **Movie Properties** iletişim kutusunu açın.

**2-Background Color** düğmesini tıklayın.

**3-Eyedropper**(Damlalık)aracını kullanarak,paletteki veya Flash geliştirmeortamındaki herhangi bir renge tıklayın, sonra **OK**’etıklayın.Stage’in rengi seçtiğiniz renge ayarlanır.

Çalışma Alanı (Work Area)

*Work area* (çalışma alanı),Stage’i temsil eden dikdörtgeni çevreleyen gri renkli alandır.Bu alna deneme amaçlı öğeler çizebilir ve ithal edebilirsiniz,bu öğeler son filmde görünmez.Çalışma alanı,bir nesnenin kayarak bir filme girdiği veya çıktığıu bir animasyonda,genellikle bir başlangıç veya bitiş noktası olarak kullanılır.

Kütüphane (Library)

Library (kütüphane),Flash projesindeki varlıkları organize etmemize yardımcı olur.

Paneller

Flash eskiden iletişim kutularını kullanarak yaptığınız işleri gerçekleştirmenizi sağlayan çeşitli paneller sunar.Paneller,projenizi geliştirirken ayarlamamız gereken ayar ve parametrelere hızlı erişim sağlayarak iş akışını iyileştirir.Onları filminizdeki kareler,metin blokları,semboller,örnekler ve diğer öğeler üzerinde değişiklik yapmak için kullanın;çalışmanızı en verimli kılacak tarzda onları keyfinize göre düzeltmekte,yerleştirmekte veya boylarını değiştirmekte kendinizi özgür hissedin.Bu bölümde daha ileride panelleri daha ayrıntılı şekilde ele alacağız. Ancak önce kendisiyle çalışacağınız panelleri tekrar görelim

**İnfo Paneli**

**Info **(bilgi)paneli,seçili haldeki nesnenin yatay ve dikey ebatlarını stage’in üst ve sol yanlarına göre konumunu gösterir metin kutularına yeni değerler girebilir ve **Enter/Return **basarak seçtiğiniz nesnelerin boyunu veya konumunu değiştire bilirsiniz.İnfo panelinin sağ üst köşesi stagede çeşitli durumlardaki nesnenin bir şekil,grafik sembolü örneği,düğme,film klibi(Movieclip)sembolü veya metin olduğunu belirtir.

İmleci,Stage’deki bir grubun veya sembolün bir parçası olmayan bir dış hattın veya dolgunun üzerine yerleştirirseniz,renk ve Alpha değerleri gösterilir.

**İnfo **paneli,her zaman farenin geçerli konumunu stage’in sol üst köşesine göre belirtir.

**FİLL Paneli **

**Fill** (dolgu)paneli;**oval,Rectangle,Brush **veya **Paint Bucket **araçlarını kullanarak dolgu yaratırken,düzenlenirken veya Stage’de seçili durumdaki şekillerin dolgu özelliklerini ayarlarken,dolgu nitelikleri ayrlamanızı saglar.Biraçılır liste,arsından seçim yapılabileçeğiniz çeşitli dolgu tipleri sunar.**None**(yok)**,solid**(katı),**dient**8radyal Gradyat)ve Bitmap.Bu paneli gradyent yaratmak ve düzenlemek için kullanacaksınız. (Bu paneli nasıl kullanacağınız hakkında daha fazla bilgi için 3.bölme bakınız. )

**Stroke Paneli**

**Stroke** (Dış hat)paneli;**Line,Pen ,Pencil **veya**Ink Bottle** araçlarını kullanarak dış hat yaratırken. Ya da Stage’de seçili durumdaki şekillerin dış hat özelliklerini nitelikleri ayarlamanızı sağlar.Bir açılır liste,dış hatta uygulayabileceğiniz çeşitli stilleri sunar.Bu paneli bir dış hattın rengini ve kalınlığını ayarlamak içinde kullanabilirsiniz.

**Transform Paneli**

**Transform**(Dönüşüm)paneli;ilgili metin kutusuna gireceğiniz değerlerle,seçtiğiniz öğeleri belirli bir miktarda ölçeklemenizi,döndürmenizi veya eğmenizi sağlar.Stage’de bir öğe seçtiğinizde,**Transform** panelinde ilk kez görünen değerler o öğenin ilk durumuna göre ne kadar dönüştürüldüğünü yansıtır.

**Align Paneli**

**Align**(Hizalama)paneli seçilmiş çok sayıda öğenin birbirine göre hizalanması,dağıtılması,boyunun ve boşluklarının değiştirilmesi için seçenekler sunar

**Mixer Paneli**

**Mixer**(Karıştırma)paneli,yeni renkleri üç farklı moda göre tanımlamanıza izin verir:RGB,HSB veya Hex(onaltılık).(Bu paneli nasıl kullanacağınız hakkında daha fazla bilgi için 3.bölme bakınız).

**Swatches Paneli**

**Swatches**(Palet)paneli,önceden tanımlanmış ve yarattığınız ya da ithal ettiğiniz özel paletlerden renk seçmenize izin verir. Bu paneli nasıl kullanacağınız hakkında daha fazla bilgi için 3.bölme bakınız.

**Character Paneli**

**Character**(Karekter)paneli,yazı yaratırken veya düzenlerken,yazı tipi,yazı stili,rengi ve daha başka seçenekler dahil olmak üzere çeşitli nitelikleri ayarlamanıza izin verir.

**Paragraph Paneli**

**Paragraph **(Paragraf) paneli,metin yaratırken veya bir metin bloğunun içindeki seçilen paragrafları düzenlerken,kenar boşlukları,hizalama seçenekleri ve satır aralıkları dahil olmak üzere çeşitli niteliklere ayarlamanızı sağlar.** **

**Text Options**

**Text Options**(Metin seçenekleri)paneli,metin blokları yaratırken veya düzenlerken çeşitli niteliklere ayarlamanızı sağlar;Buna metin kutusunun tipi,HTML becerili olup olmadığı ve diğer ayarlar dahildir.Bu panelde yapılan ayarlar,sadece netin bloğunda seçilen yazıyı değil,Tüm metin bloğunu etkiler.

**İnstance Paneli**

**İnstance**(Örnek)paneli,stage’de seçilen birf sembol örneğinin çeşitli niteliklerini ayarlamanızı sağlar.Bu paneldeki seçenekler seçilen örnek tipine göre değişiklik gösterir.Yani grafik,düğme ve film klibi tipinde olmasına göre.Bu panelin son üst köşesindeki grafik,seçilen sembolün tipini belirtir.

**Effect Paneli**

**Effect**(Efekt) paneli,stage’de seçilen bir örneğe renk ve Alpha efektleri uygulamamızı sağlar.Seçilen örneğe önceden bir efekt uygulanmışsa,bu önceki ayar otomatik olarak gösterilir

**Clip Parameters** **Paneli**

**Clip Parameters**(Klip Parametreleri) paneli,stage’de seçili durumdaki bir smart clip’in parametrelerini ayarlamanızı sağlar.

**Frame Paneli**

**Frame **(kare) paneli,kareye bir etiket veya bir komut grubu atamanıza izin vermenin yanında,ara doldurma(tweeening) seçenekleri de içerir

**Sound Paneli**

**Sound **(Ses) paneli,Timelinedeki ses eklemenizi veya bu karelere eklenmiş sesleri düzenlenmemizi sağlar.Bu panelde Flash’ın ses düzenleme araçlarını açarak bir sesin uzunluğunu,şiddetini ve pan ayarlarını yapmanızda mümkün

**Scene Paneli **

**Scene**(Sahne)paneli,projenizdeki sahnelerle çalışmanıza ve onları organize etmenize yardımcı olur,sahne yaratmanızı,silmenizi,sırasını değiştirmenizi,ve sahneler arasında geçiş yapmanızı sağlar.

**Generator Paneli**

**Generator **Paneli,MacroMedia Genarator ile ilgili içerikle çalışmak için kullanılır.Bilgisayarınızda Generator kurulu olmadığı sürece bu panel işlevsel değildir.

**Actions Paneli**

**Action **(Eylemler) panelini, filminizde etkileşim yaratmak için kullanacaksınız. Bir kareye,düğmeye veya filmin klibine tıklamanız,Actions panelindeki seçenekleri kullanabilir hale getirir.Bu panelin size en uygun şekilde çalışmasını sağlamanız içinde pek çok seçeneğe sahiptir.

**Panellerle Çalışmak**

Nasıl çalıştığınıza ve kullanılabilir ekran alanı miktarına bağlı olarak çeşitli panelleri özelleştirerek verimliliğinizi büyük ölçüde artıra bilirsiniz.

**Panelleri Bireysel Glarak Göstermek ve Gizlemek**

**Window>panel’**i seçin.beliren alt menüden göstermek istediğiniz paneli seçin.Bir panel zaten görünür halde ise,aynı adımı izleyerek paneli gizleyin.

Panelin sol üst köşesinde(Macintosh)veya sağ üst köşesinde yer alan kapama kutusunu tıklayın

**Launcher **çubuğu,**Library **ve** Movie Explorer’**ın yanı sıra,çeşitli panelleri de hızlıca göstermenizi ve gizlemenizi sağlar.**Launcher**’daki düğmelere tıklyarak o ara birim öğesinin geçerli durumuna bağlı olarak onu gösterir veya gizlersiniz

**Tüm Panelleri Göstermek,Gizlemek veya kapatmak**

**Tab **tuşuna basın.Bu,geçerli durumlarına bağlı olarak o anda aktif olan panellerin tümünü gösteren veya gizleyen bir geçiş komutudur.Bu komuta **View>Hide All Panels**’i seçerek de ulaşabilirsiniz.

**Window>Close All Panels**’i seçin.Bu eylem o anda açık olan panellerin tümünü kapatır.

Panelleri gruplayarak,benzer işlevlere sahip panelleri bir araya toplaya bilirsiniz..Böylece film öğeleri üzerinde çeşitli düzenleme işlevleri yaparken fareyi daha az hareket ettirmek zoruda kalırsınız.

**Panelleri Gruplamak**

Panelin adına tıklayın,onu başka bir panelin üzerine sürükleyin,sonra farenin tuşunu bırakın.

Sürüklediğiniz panel ve üzerine sürüklediğiniz panel artık gruplanmıştır.İstediğiniz sayıda paneli bir grup halinde bir araya getirebilirsiniz.

**Panellerin Grubunu Çözmek**

Grubunu çözmek istediğiniz panelin altına tıklayın,gruptan uzağa sürükleyin ve farenin tuşunu bırakın.Sürüklediğiniz panel gruptan ayrılır.

Özel grup lamalarınızı daha sonra kullanmak üzere bir tek fare tıklamasıyla kaydedebilirsiniz.***Panel grupları***(panel set)adı verilen bu özel gruplar,belirli işleri yapmak için mükemmeldir.

**Bir Panel Grubunu Kaydetmek**

**Window>save panel Layout**’u seçerek **save panel Layout**(panel düzenini kaydet)iletişim kutusunu açın. Panel grubunuza bir isim verin **OK**’i tıklayın.

**Önceden Kaydedilmiş Bir Panel Grubunu Kullanmak **

**Window>panel seti**’i seçerek var sayılan panel düzeni ile birlikte yarattığınız özel panel düzenlerini içeren bir liste alt menüsünü açın.

**Önceden Kaydedilmiş Bir Panel Grubunu Silmek**

Bir panel grubunu silmek için,Flash 5 /panel sets klasöründe paneli bulun ve silin Flash,o panel grubunu seçenek grubundan kaldırır.

**Movie Explorer**

**Movie Explorer**,yapısı ve içerdiği öğelerde dahil olmak üzere,tüm Flash projenizin genel görünümünü sağlar.**Launcher **çubuğunda **Movie Explorer **düğmesine tıklayarak bunu gösterebilir veya gizleyebilirsiniz.

**Izgara, Cetveller ve klavuzlar**

Flash,projenizi geliştirirken öğeleri stage’e hassas bir şekilde yerleştirebilmeniz için çok sayıda araç sunar;bunların arasında bir ızgara (Mili metrik kağıdın dijital dünyadaki karşılığı),cetveller ve kılavuzlar vardır.Bu araçları verimli bir şekilde kullanmayı öğrendiğinizde,tasarımınızı oluştururken işinizi son derece kısalta bilirsiniz.

**Scene ve Symbols Liste Düğmeleri**

**Scene **ve** Symbol **düğmeleri projenizdeki sahneler ve semboller arasında hızlı geçiş yapmanızı ve onları düzenlemenizi sağlayan menüleri açar.

**Seçenekler ve Ayarlar**

İki farklı kişinin çalışma tarzları da farklıdır. Kullanıcının tanımlayabildiği ayarların varlık nedeni de budur:Bir programın geçerli ayarlarlarıyla çok yavaş çalıştığını düşünebilir,eski sürümünün özelliklerini daha çok beğeniyor olabilir veya yardıma her an olaşabilmeği isteyebilissiniz.hangi durumda olursanız olun,Flash 5’i kendinize göre ayarlamanız kolaydır.

**Preferences (Tercihler) iletişim kutusu**

**Edit>preferences**’i seçerek **preferences **iletişim kutusunu açarsınız.Bu iletişim kutusu,genel (**General**),düzenleme (**Editing)** ve pano (**Clip Board**)tercihlerinin ayarlamamızı sağlayan üç sekmeye sahiptir.Şimdi her ayar grubuna tekrar bakalım

**General (Genel)Sekmesi**

**Undo leves:**Bu ayar, Flash’ta kullanılan geri alma /yineleme düzeylerini sayısını ayarlamamızı sağlar.Bu değer ne kadar yüksek olursa o kadar fazla bellek gerekir ve bu yüzden bilgisayarınızın performansını o kadar düşürebilir.Maksimum değer 200 olabilir.Denemeler yaparken daha rahat etmek için daha yüksek bir değere ayarlamak isterseniz,bol miktarda belleğe sahip olmalısınız.Aksi halde var sayılan ayarı kullanmanız,genellikle daha makuldür.

**Printing Options-Disable Postscript**(sadece Windows da ):Bu seçenek,bir PostScript yazıcıya yazdırılırken PostScript çıktıyı etkinleştirir veya kapatır.

**Section Options-Shift Select:** :Bu seçenek ,Stage’deki ve çalışma alanındaki öğeleri nasıl seçeceğimizi ayarlar.İşaretli ise,bir öğeyi seçmemiz diğer öğeleri seçimden çıkarır ve çok sayıda nesneyi seçmek için Shift tuşuna basılı tutmanızı gerektirir.İşaretli değilse her hangi bir öğeye bir kez tıklayarak onu geçerli seçimi dahil edebilirsiniz

**Selecttion Options-Show Tooltips:**Bu seçeneği seçmeniz fare arabiriminin çeşitli kısımlarının üzerinde durdurulduğunda araç ip uçlarının gösterilmesine neden olur .Bu araç ip uçları,farenin durduğu öğeyle ilgili bilgi içerir.Onları can sıkıcı buluyorsanız bu seçenekteki işareti kaldırın.

**Timeline Options-Disable Timeline Docking:**Bu seçeneği işaretlediğinizde,Timeline flash arabiriminden ayrılır ve serbest,kayan halde kalır(Macintosh versiyonunda zaten böyledir).Timeline’yi bol bol taşıyorsanız ve normalde olduğu gibi ekranın üst kısmında sabitlenmesini istemiyorsanız,bu özelliği faydalı bulacaksınız.

**Timeline Options-Flash 4 Selection Style:**kare seçimi bu Flash sürümünde biraz farklıdır.Flash 4’ün tarzını tercih ediyorsanız,bu seçeneği işaretleyin

** Timeline Options-Show Blank Keyframes:** Flash 4’te Timeline’deki boş bir anahtar kareyi içi boş,küçük bir çember belirtirdi.Flash 5’te artık içi boş çember kullanılmıyor.Bu seçeneği seçmeniz,küçük çemberi geri getirir ve boş anahtar karelerde görünmesini sağlar.

**Highlight Color:**Gruplar yazı ve semboller gibi Stage öğelerini seçtiğinizde,seçili olduklarını belirtmek için bunların çevresinde renkli bir kutu belirir.**Highlight color **kısmından**Use This Color’ı **işaretler seçerseniz,tüm katmanlarda seçilen öğeri tanımlamak için burada seçtiğiniz renk kullanılır.Bunun yerine ** Use Layer Color’**ı seçerseniz,bir öğenin seçim kurusunun rengi hangi katman da durduğunu belirten renk olacaktır.İkinci seçeneği seçerek,seçtiğiniz bir öğenin hangi katman da durduğunu hemen anlayabilirsiniz.

**Action Panel Mode:Action **paneli iki modda çalışabilir:**Normal **ve **Expert**(Uzman).Bu seçenek yeni eylemler yaratırken Action panelinin kullanacağı varsayılan modu kullanmamızı sağlar.

**Clipboard(Pano)Sekmesi******

(Sadece Windows için)Bir Grafiği kestiğinizde veya kopyaladığınızda Flash aslında oraya iki versiyonu yerleştirir:Versiyonlardan biri ***metafile ***bilgisine dayanır(başka bir vektörel programa yapıştırmak için faydalıdır),diğeri bitmap programlara yapıştırmak için bir bitmap versiyonudur.

Panodaki bitmapler için Windows ayarları(**Bitmaps on Clip board):**

**Color Depth:** Renk derinliğini ayarlar bu değer ne kadar yükse, panoya yerleştirdiğinde grafik dosyanın boyu da o kadar büyük olacaktır** 32-Bit Color W/Alpha **seçeneğini,panoya yerleştirdiğiniz öğelerin şeffaflıklarını korumak için seçmelisiniz.

**Resolution:**Bitmap’ın çözünürlüğünü ayarlar çözünürlük ne kadar büyük ise dosya boyuda o kadar artar.

**Size Limit:**Bitmap’ın panoya yerleştirilmesi için ayırmak istediğiniz maksimum RAM miktarını ayarlamanızı sağlar daha yüksek çözünürlük,daha fazla RAM gerektirir.Bilgisayarınız az miktarda belleğe sahipse **None **ayarlayın,çünkü bu seçenek belirtilen miktarda belleğin kullanımından bağımsız olarak ayrılır.

**Smooth:**Panoya yerleştirildiğinde bitmap’e Antialiasing uygular veya yumuşatır.

**Gradients:**Bu seçenek,nesnelerin panoya kopyalanması ile dosyalarda yaratılan gradyentlerin kalitesini ayarlar.Sadece Flash’ın içinde kopyalama ve yapıştırma yapacaksınız,bu ayar için **None’**u seçin bu karmaşık ve gradyentli çizimlerin kopyalanması için gereken zamanı azaltır.

**FreeHand Text:**Bir MacroMedia FreeHand dokümanından metin blokları yapıştırıyorsanız, Flash’da düzenlene bilir halde olmaları için bu seçeneği işaretleyin

Panodaki bitmap’ler için Mac ayarları:

**Type:**Flash’da kestiğiniz veya kopyaladığınız nesneleri panoya yerleştirirken,bir bitmap yaratmak veya onları vektörel olarak bırakmak arasında seçim yapmanızı sağlar.

**Resolution:**Bitmap’ın çözünürlüğünü ayarlar daha yüksek çözünürlük daha büyük dosya boyuna neden olur.

**Including PostScript:**Bir PICT dosyasın bir nesne veya vektör-tabanlı olarak ihraç ediyorsanız bu seçenek grafiği post Script yazdırma için optimize eder.

**Gradients:**Nesnelerin panoya kopyalanmasında yaratılan PICT dosyalrındaki grandyentlerin kalitesini ayarlar kopyalama ve yapıştırma işlerini Flash’ın içinde yapacaksınız,bu ayarda **None’**u seçmelisiniz.Bu karmaşık gradyentli çizimlerin kopyalanması için gereken zamanı azaltır.

**Görünüm Seçenekleri**

Herkes iki işlemcili Macintosh G4’lerde çalışmıyor.Öyle olsaydı,hem dünya daha mutlu yer olurdu,hem de bu kısım büyük olanda gereksiz olurdu.İşin doğrusu bazılarınız halen işlemci engelli.Çok sayıda vektörel grafik içeren projelerde çalışırken,her grafik çizilişinizde ekranın tazelenmesini beklemek,yaratıcıların önünde büyük bir engel oluşturabilir.

Flash,öğelerin geliştirme ortamında nasıl gösterileceği için seçenekler sunarak bu problemi hallediyor.Bu seçenekleri kullanmak için **View **menüsünden aşağıdaki seçeneklerden birini seçin

**Outlines:**Bu seçeneği seçerseniz dolgular kaldırılır ve tüm öğeler sadece dış hatları ile (Vektörel grafikler) veya sınırlayıcı kutularıyla (Bitmap’ler) gösterilir.Bu sayede karmaşık şekilleri gösterimi hızlandırılır.

**Fast:**Bu seçeneği seçerseniz,bir grafiğin tüm özellikleri gösterilir,ancak yumuşatma (Antialiasing) kapatılır.

**Antialias:**Yazılar haricindeki tüm stage nesnelerini kenarlarını yumuşatır.Bunun nedeni,çok küçük yazılara Antialiasing uygulandığında okunmalarının son derece güçleşmesidir.

**Antialias Text.**Yazı da dahil olmak üzere her şeyi yumuşatır.Bu işlemciye en çok yüklenen seçenektir,buna karşı geliştiricilerin en çok tercih ettiği seçeneklerden biridir.

**İzleme Seçenekleri**

Flash’ta çalışmanızı daha ayrıntılı şekilde görmek için stage’e ve çalışma alanına yaklaşa bilir veya sayfa düzeninin genel halini görmek için uzaklaştırabilirsiniz.**View** menüsünü kullanarak yaklaşma ve uzaklaşma işlemlerini kontrol edebilirsiniz. Stage’i büyütmek veya küçültmek bu menüden bir yüzde seçin.**Show Frame** seçeneği stage’in tümünü görür hale getirir ve **Show All** seçeneği stagedeki tüm nesnelerin ve çalışma alanını görünür hale getirir.Diğer seçeneklerin tümü stage’in ve çalışma alanının büyültme yüzdesini bir yüzdeye göre ayarlar.

**Hand Araçı **

**Hand** (El) araçı bir tek işe yarar:Sayfanıza yaklaştığınızda ve onda görünümde olmayan bir alana geçmek istediğinizde,stage’de /Çalışma alanında hareket etmenizi sağlar(aynı işi kaydırma çubuklarını kullanarak ta yapabilirsiniz,ancak bu kadar kullanışlı olmayacaktır).

**1-Hand**(el)aracının düğmesini tıklayın veya klavyeden H tuşuna basın.İmleç küçük bir el halini alır

**2-**İmleci stage’de veya çalışma alanında her hangi bir yere yerleştirin sonra tıklayıp sürükleyerek hareket edin.

**Magnifier Aracı******

**Magnifier**(Büyüteç)aracı,çiziminize yaklaşıp uzaklaşarak ince ayrıntılar üzerinde çalışmanızı veya genel görünümü görmenizi sağlar.

**Magnifier **aracı iki değiştiriciye veya seçeneğe sahiptir:

**Enlarge:**Stage’e veya çalışma alanına tıklayarak,çiziniz %200 büyüterek yaklaşmanızı sağlar

**Reduce:**Stage’e veya çalışma alanına tıklayarak çiziminizi geçerli büyüt oranını %50 ‘sine düşürerek uzaklaşmanızı sağlar.

**Klavye Kısayolları**

Menüleri,arac çubuklarını ve düğmelerin Flash ‘la çalışmayı kolaylaştırmasına karşın,bezen bir işi yapmak için bir veya iki düğmeye basmaktan daha hızlı bir yol yoktur.Flash ile kesmek ,kopyalamak,silmek,sahne eklemek ve kaldırmaktan,kare eklemeye ve silmeye,kareleri gösterme ve gizlemeye kadar her tür işi klavye kısayollarını kullanarak yapabilirsiniz.

Flash artık kullanıcılara kendi klavye kısayollarını yaratmak veya atama imkanı sağlayarak klavye kısayollarını yeni bir düzeye taşıyor:İstediğiniz satırda özel kısayolu ayarlayabilir ve bunları özel bir klavye kısayolu grubu halinde kaydedebilirsiniz.Aslında,Flash yüklenmiş durumda çok sayıda hazır grupla gelir;Bunların arasında var sayılan klavye kısayolları ve PhotoShop,Fireworks.Freehand 9 ve Illustrator gibi değer program tarafından kullanılan kısayol grupları da vardır.

Klavye kısayollarının taratılması ve düzenlenmesi **KeyBoard Shortcuts **(klavye kısayolları)iletişim kutusundan yapılır.

**Keyboard Shortcuts İletişim Kutusunu Açmak**

**Edit> Keyboard Shortcuts’ı **seçin.önce arabirimi inceleyelim,sonra bir klavye kısayolu grubunun nasıl yaratıldığını göreceğiz .

**Current Set**(geçerli grup)**: Keyboard Shortcuts **iletişim kutusunu açtığınızda,bu açılır listede kullanılmakta olan klavye kısayollarının listesi görünür.Buna ek olarak,bu kutuyu başka bir kısayol grubunu seçmek için kullanırsınız.

**Duplicate Set**(Grubu çoğalt)düğmesi:Seçili haldeki geçerli grupla aynı kısayollarla sahip bir kısayol grubu kopyası yaratır.Bu sayede,özel bir grup yaratmak için bir başlangıç noktası sağlar

**Rename Set**(Grubun adını değiştir) düğmesi:Seçtiğiniz kısayol grubunun adını değiştirmekte kullanacağınız **Rename** iletişim kutusunu açar.Bu eylemi var sayılan Flash 5 kısayolları üzerinde yapamazsınız.

**Delete set**(Grubulu sil) Düğmesi:Seçili haledeki klavye kısayolları grubunu siler.Bu eylemi var sayılan Flash 5 kısayolları grubu özerinde yapamazsınız.

**Commands**(Komutalar):Üç kısayol komutları kategorisi vardır:**Draving Menu Commands**(çizim menüsü komutları),**Draving Tools**(çizim araçları)** Test Movie Menu Commands**(Film testi menüsü komutları).Bu açılır listeden bir kategori seçmeniz,o kategori için ayarlanabilecek tüm komutları gösterir.**Commands **açılır listenin altındaki **commands** kutusu,seçilen kategorideki komutların hiyerarşik listesini gösterir.

**Commands List(**komut listesi):Bu,seçilen komut kategorisine dayanan hiyerarşik bir listedir(yukarı bakın);klavye kısayoluna sahip olabilecek tüm komutları gösterir.

**Description(**açıklama);**Commands** penceresinde bir menü komutu seçildiğinde,bu alanda seçilen komuta dahil kısa bir açıklama ğörünür.

**Add/Delete Shortcut**(kısayol ekle/sil) düğmeleri **+ ve –**düğmeleri belirli komutlarla ilişkili kısayolları eklemenize ve silmenizi sağlar.**Shortcut** penceresi **commands** penceresinde seçili haldeki komutlar ilşkili kısayolların listesini gösterir.

**Shortcuts List**(kısayol listesi) **Commands **penceresinde seçili komutla ilişkili tüm klavye kısayollarını gösterir.

**Pres Key**(tuşa bas):Seçili haldeki kısayol için tuş kombinasyonunu (**Shortcuts **pencerisinde göründüğü gibi) veya belirli bir kısayol için sizin girdiğiniz yeni tuş kombinasyonunu gösterir.

**Change**(Değiştir)**düğmesi:Press Key** kutusunda görünen tuş kombinasyonunu,**Shortcut** pencereinde seçili durumdaki kısayolla ilişkilendirir.

Artık arabirimi tanıdığınıza göre,bir özel klavye kısayolu grubunun yaratılmasındaki işlemleri görelim.

**Özel Bir Klavye Kısayolları Grubunun Yaratılması**

**1.Key board Shortcut** iletişim kutusu açıkken **Current Set **açılır listesinden mevcut bir gurubu seçin

**2.Duplicate** düğmesine tıklayın.Açılan **Dublu cate** iletişim kutusunda bir isim verin ve **OK’**e tıklayın

**3.Commands **açılır listesinden bir komut kategorisi seçin **Commands** listesinde o kategorideki komutların Hiyerarşik listesi belirir.

**4.Commands** listesinden bir komut seçin.İletişim kutusunun **Description** alanında komutun bir açıklaması görülür.

**5.**seçili haldeki komutla bir tuş kombinasyonunu ilişkilendirmek için,**Add(+)** düğmesine tıklayın.Tuş kombinasynonunu değiştirmek için, **Shortcuts** düz yazı listesinden seçin.

**6.Press Key** metin kutusunu seçin,sonra seçili haldeki komutla ilişkilendirmek istediğiniz tuş kombinasyonunu seçin

**7.Change** düğmesine tıklayın .

**8.**komutlarla ilişkili kısayollar eklemek veya düzenlemek için bu adımları tekrarlayın.

**9.OK** düğmesine tıklayarak iletişim kutusunu kapatın ve yeni kısayolunuzu etkinleştirin.

**Özel Bir Klavye Kısayolu Grubunu Silmek**

**1.Keyboard Shortcuts ** iletişim kutusu açıkken **Delete Set** düğmesine tıklayın.

**2.**Açılan **Delete Set **iletişim kutusunda,silmek istediğiniz grubunu seçin ve **OK**’e tıklayın.

**Bir Özel Klavye Kısayolu Grubunu Adını Değiştirmek**

**1.Key board Shortcuts **iletişim kutusu açıkken,**Rename Set** düğmesine tıklayın.

**2.**Açılan **Rename **iletişim kutusundan yeni bir isim girin** ve OK**’e tıklayın.

**Film Özelliklerini Ayarlamak **

Flash projenize başlamak için,saniyede onaylatılmasını istediğiniz kare sayısıyla (oynatım hızı),filmin yatay ve dikey boyunu ayarlamanız gerekir .Bunların ne olması gerektiği hakkında en başından net bir fikrimiz olmalı çünkü bu ayarları projenin ortasında değiştirmeniz yarattığınız her şeyi olumsuz yönde etkileye bilir.Örneğin,Stage’e nesneler yerleştirilmiş ve onları tam olarak 12 kare /saniye(Frames per second,Fps)hızında 4gösterilmek üzere ayarlanmış olabilirsiniz.Bu durumda Fps ayarını değiştirmeniz,tüm animasyonunun oynatım hızını etkiler ve filminiziz başta düşündüğünüzden farklı görünmesine neden olur.Tabi ki bunu dengelemek üzere ayarlamalar yapabilirsiniz,ancak bu önemli miktarda zaman kaybetmeniz anlamına gelir.Her şeyi başta doğru planlamak en iyisidir.

**Filmin Özelliklerini Ayarlamak**

**1.**Modify menüsünden** Movie’i **seçerek ** Movie Properties **iletişim kutusunu açın.

**2.Frame Rate** kutusuna,filminizin oynatılmasını istediğiniz saniyedeki kare sayısı cinsinden değeri yazın.Var sayılan ayar olan 12,pek çok proje için yeterlidir.İsterseniz daha büyük bir değerde seçebilirsiniz.Ancak bu değer ne kadar yükselirse yavaş makinelerin filminizi oynatmasını da o kadar güçleşeceğini unutmayın.

**3**.**Dimension **kutularına filminiz genişliği(**Width)** ve yüksekliği** (Height)**için değer girin.Minimum genişlik veya yükseklik 18 piksel;maksimum değeri ise 2880 piksel’dir.

**4**.**Background Color** kontrolünü kullanarak bir arka plan rengini seçin arka plan rengini ***stage’in rengi’***de denir.

**5**.**Ruler Units** çekme menüsünden ölçü birimi seçin.burada seçtiğiniz ölçü birimi,ölçülerle ilgili kullanıldığında programın tüm alanlarını etkileyecektir.(Örneğin,ızgara ayarları **Info** panelindeki değerler vb.).

Projenizi bir film halinde ihraç ettiğiniz,filminiz etkileyen daha pek çok ayar vardır.

---
*Kaynak: `FLASH NASIL CALISIR/FLASH NASIL CALISIR.doc` — serdal — 2004*
