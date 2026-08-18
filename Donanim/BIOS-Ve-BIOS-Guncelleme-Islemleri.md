# BIOS Ve BIOS Güncelleme İşlemleri

## **BIOS ve BIOS GÜNCELLEME İŞLEMLERİ******

## ** ****1 - BIOS NEDİR ?******

*** ***BIOS adı “Basic Input / Output System” ( Temel Giriş / çıkış Sistemi) kelimelerinin baş harflerinin birleşmesiyle meydana gelmiştir. ROM adını verdiğimiz “Read Only Memory” (Sadece Okunabilir Bellek) bir çip içine depolanmıştır.En son çıkan anakartların çoğu şimdilerde kullanıcılar tarafından kolayca güncellenebilen Flash BIOS olarak da bilinen EEPROM “**E**lectrically **E**rasable **P**rogrammable **R**ead-**O**nly **M**emory” ( Elektrikle Silinebilir Programlanabilir Sadece Okunabilir Hafıza) kullanmaktadır. (Daha önceki BIOS ların çipleri güncellenebilmek için anakarttan fiziksel olarak çıkartılır ve daha yenisi ile değiştirilirdi) Bilgisayarı ilk açtığımızda çalıştırılan ilk program BIOS dur.İlk olarak bilgisayarın donanımını tarar ve test eder (Bu işlem Power On Self Test veya POST olarak adlandırılır ) Daha sonra BIOS işletim sistemini yükler. BIOS içindeki bilgiler bazı zamanlar CMOS diye de adlandırılan SETUP programı ile değiştirilebilir.Run Time Service olarak adlandırılan aynı zamanda BIOS ‘un bir fonksiyonu olan komut kümesi bilgisayarın donanımını kontrol etme işleminde işletim sistemine ve uygulama programlarına yardım eder. BIOS ,bilgisayarın donanımı hakkında tüm bilgiye sahip olur ve bu donanımların birbirleri ile haberleşmeleri işlemini BIOS üstlenir.Örneğin ses kartı, modem gibi parçaları üzerinde barındıran bir anakart aldığınızda, anakartınızın üzerine takılı olan aygıtların listesini işletim sisteminize BIOS verir. Anakart üzerinden desteklenen bir donanımı iptal ettiğimizde ise (örneğin, BIOS'dan anakartın ses özelliğini iptal ettik) işletim sisteminiz bu aygıtı artık görmeyecektir. Diğer taraftan, BIOS bir yazılım olduğundan, anakartın dengeli + performanslı çalışması için kullanıcılara ayar yapma olanağı sunuyor.
Bu paragraftan çıkartacağımız sonucu ise şöyle özetlersek daha kalıcı olabilir: "BIOS, anakartınızın özelliklerini ve üzerine takılı olan donanımların çalışması için gereken parametreleri, kullandığınız işletim sistemine aktaran, minik bir işletim sistemidir." çeşitli BIOS üreten firmalar vardır.Bunlar: AWARD, AMI ve Phoenix BIOS. Phoenix BIOS ile AWARD BIOS birleşerek, bazı anakartlarda ikisinin ortak ürünü olan BIOS'lardan kullanılmaya başlandı.

## P6-BXA Model Bir Anakart üzerindeki Bios

Güç Düğmesine bastıktan hemen sonra, BIOS devreye giriyor ve POST (Power On Self Test)denen kısa bir analiz-test yapıyor. Bu analiz ile birlikte, üzerine takılı olan PnP (Tak ve çalıştır) aygıtları tanımaya olanak sağlıyor. Bir aksilik olduğunda bunu size yazılı mesaj olarak ya da ses ile bildiriyor. Tahmin edeceğiniz üzere, BIOS, -diğer anlamda- PC'nin boot etmesi için gereken bir sistemdir.

## **2 - BIOS GÜNCELLEME NEDİR ? ******

Tıpkı işletim sistemlerinde olduğu gibi BIOS'lar da hata içerebilir. Eğer anakartınız bir donanım ile çalışmayı reddediyorsa, veya uyumsuzluk yapıyorsa, bu sorunları ve(ya) hataları BIOS güncellemeleri ile gidermek mümkün. Kısacası BIOS güncellemesi, anakartınızın üreticisinin çıkardığı daha yeni BIOS sürümünü, kullandığınız BIOS ile değiştirmektir. Ortada bir sorun yokken BIOS Güncellemek pek mantıklı değil. Ama yeni özellikler gelmiştir, kritik sorunlar giderilmiştir, o zaman BIOS’u güncelleriz. BIOS güncelleme sadece sorunları gidermek için yapılan bir işlem değil.. örneğin yeni bir işlemci çıktı, anakartımız teorik olarak bu işlemciyi destekliyor. Ama işlemciyi taktığımızda, işlemcinin yanlış algılandığını görüyoruz. Bu durumda BIOS ‘u güncelleriz ve yeni işlemcimizin tam olarak algılandığını görürüz. Bu güncelleme işini, BIOS yazılımının türüne göre veya anakart üreticisine göre farklı farklı yazılımlar ile yapabilmemiz mümkün. örneğin, AWARD BIOS kullanan bir kişi, BIOS güncelleme yaparken AWDFLASH programını kullanır. Anakart üreticine göre de değişir demiştik. Asus anakartlar AWARD BIOS kullanmasına rağmen, AFLASH adında kendilerine has bir program kullanırlar.

## **3 - BIOS GÜNCELLEME İŞLEMİ İÇİN NELER GEREKLİDİR? ******

** **BIOS güncelleme işlemi, eğer kurallara uyulmaz ise riskli bir iştir. Kurallara uyarsanız çok basit bir işlem. Eğer anakartınızın üreticisinin sayfasında yazılanlara harfiyen uymazsanız, BIOS yazılma işlemi başarısız olarak sisteminiz tekrar açılmayabilir. BIOS Güncelleme işlemlerine başlamadan önce, anakart üreticinizin yazdığı uyarılara tam olarak uyun.Gerekli olan ve bilmeniz gereken şeylere topluca bir göz atalım:

- Anakartınızın Markası & Modeli
- Anakartınızın üreticisinin Web Sitesi
- Anakartınız için gereken BIOS dosyaları ve sistem disketi

Anakart üreticilerini BIOS dosyaları için sunduğu direkt adresler ve programların adresleri:

ASUS : http://www.asus.com.tw/products/motherboard/bios.html
GigaByte: http://www.gigabyte.com.tw/support/mbbios\_index.htm
Abit : http://www.abit-usa.com/english/download/bios%20update/main.htm
MSI : http://www.msi.com.tw/support/bios/main.htm
Soyo : http://www.soyousa.com/686bios.html
INTEL : http://support.intel.com/support/motherboards/desktop/
IWILL : http://www.iwillusa.com/support/ProductSupport.asp?SupportID=8
FIC : http://www.fic.com.tw/techsupport/drivers/searchbios1.asp
SpaceWalker (Shuttle) : http://www.spacewalker.com/english/download.htm
Tyan : http://www.tyan.com/support/html/bios\_support.html

## **4 - ANAKARTIN MARKASINI VE MODELİNİ ÖĞRENME******

## **AWARD BIOS******

***(1)*** BIOS güncelleme işlemini anakartımızın markasına ve modeline göre yaparız. Bu sebeple anakartımızın markasını ve modelini öğrenmek durumundayız. Satın aldığımız sistemin özelliklerine bakarız ve hiçbir şeyin yazılı olmadığı görülür. Aslında en garantili ve kısa yol kasanızın içini açıp, anakartın üzerinde isim aramak olacaktır. Bazı üreticiler, anakartın üzerine marka yerine bazen model yazabiliyorlar. Dolayısıyla markayı anlamak güçleşiyor. Fakat bilgisayarın kasasını açmadan da anakartın markasını ve modelini öğrenebiliyoruz.
Anakart üreticilerini, kullandığı **AWARD **ve **AMI **BIOS'lar sayesinde anlıyoruz. PC'yi açtıktan sonra RAM'ın sayıldığı ekranda iken Pause tuşuna basarak ekrandakileri inceleyin. En altta, ilk bakışta vasıfsız gibi duran bir çok rakam ve harf bulunuyor. İşte her üreticinin kendine has bir id(kimlik) numarası bulunuyor. Her üreticinin kimlik numarası farklı ve bu numara aşağıda işlevsiz gibi duran bir dizi rakam ve harfin içerisine gizlenmiştir. Fakat günümüzde çıkan son model anakartlarda, bu işlemlere fazla gerek kalmıyor. Markalı bir anakart aldıysanız, POST ekranındayken, anakartınızın markası ve modeli çok açık bir şekilde görünmektedir.

***(4)*********

Fakat çoğu anakartta, kodlar yer alıyor. örneğin yukarıdaki resimde altı çizili ve işaretli yerlerde, marka ve model yerine, genelde kodlar yer alıyor ve biz bu kodları kullanarak anakartımızın markasını bulacağız.**CTBIOS** adlı bir program, eğer AWARD BIOS'lu bir anakarta sahipseniz, bu kodları kendisi analiz ederek, anakartınızın markasını sizlere söylüyor. Ama modelini söyleyemiyor. Her üreticinin sayfasında, anakartın modelini nasıl bulacağınız ile ilgili bilgiler yer almakta.

Bu programı, **www.hwstation.com/files/pcmag/ctbios.zip** adresinden çekebilirsin

Anakartımızın markasını nasıl bulacağımıza gelelim şimdi. Award BIOS'lar için, altını çizip B harfiyle işaretlenen yerde yazan yazıya bakın: **6A6S7M49C**. Buradaki ilk 5 karakter, yani **6A6S7 **anakartta kullanılan yongaseti hakkında bilgi verir. Bundan sonraki 6. ve 7. karakterler ise, yani **M4**, anakartınızın üreticisinin kod adını taşımaktadır. Son 2 karakter işimize yaramıyor. Bu kodlar her anakartın üreticine göre farklılık gösterir. Siz kendi anakartınızdaki kodları edindikten sonra **www.motherboards.org/moboidtools.html** adresine giderek, BIOS String ID bölümüne bu kodu yazacaksınız ve sonuca ulaşacaksınız.
Bazı anakartlarda, A harfiyle işaretlenen yerde, Kuzey ve Güney Köprüsü bilgileri yer almakta. Ama i815, i820 gibi hızlandırılmış mimariyi kullanan yongasetli anakartlarda yongasetinin ismi yer alır.

Yukarıda görülen ekran resminde,sol üst köşede altı çizili yere bakarsanız Anakart Modeli - BIOS versiyonunu göreceksiniz. örneğin, **W6167MS V 1. 3** şeklinde. **W6167MS **burada model, V 1. 3 ise kullanılan BIOS'un sürümünü belirtiyor.

## ** ****AMI BIOS******

***(5) ***· Sisteminizi kapatın

· Klavyenizi kasanızdan çıkartın veya tuşlardan birini basılı tutun.

· Sitemi açın ( klavye hatası ile karşılaşmanız gerekiyor)

· Ekranın sol alt köşesindeki harf ve sayılardan oluşmuş uzun diziye dikkat edin.

Bu dizi BIOS tanımlama dizisidir. Bu dizi aşağıdaki gibi görünür.

**51-0102-005123-00111111-101094-AMIS123-P ******

Bu dizi 1991 ‘den günümüze olan bir anakartı işaret etmektedir. Bu BIOS tanımlama dizisi için BIOS tanımlama numarası 3. dizi bölümünde koyu olarak yer alan **005123** ‘dür.

**DINT-1123-04990-K8 ******

Bu dizi 1986’dan 1991 ‘e kadar olan BIOS ları işaret etmektedir..Bu BIOS tanımlama dizisi için BIOS tanımlama numarası 2. dizi bölümünde koyu olarak yer alan **1123**’dür.

Eğer ikinci dizi kümesinin koyu renkli ilk numarası;

1, 2, 8, veya bir harf ise-bu NON-AMI Taiwan üretimi bir anakarttır.

3, 4, veya 5 ise- bu TRUE AMI anakarttır.

50 veya 6 ise - bu NON-AMI US yapımı anakarttır.

9 ise –bu Taiwan üretimi değerlendirme anakartıdır.

**Not :** Eğer tanımlama numarası NON-AMI bir anakartı işaret ediyorsa bu durumda anakartı size satan kişi veya kuruluşlarla temasa geçmeniz gerekmektedir.

***(1)*** Son olarak, anakartınızın markasını ve modelini öğrendikten sonra yapacağınız işlem artık çok basit. Yukarıda verilen adresten ID Stirng'e göre sonuçları aldığınızda, size bu markanın Web sitesi adresi verilecektir. Anakartınızın üreticisinin Web adresine gidip, ürünler bölümünden sizin anakartınız ile ilgili olan sayfaya gidecek ve BIOS sayfalarından, anakartınız için olan BIOS dosyalarına ulaşacaksınız.

**
5 - AWARD BIOS GÜNCELLEME İŞLEMLERİ ******

***(1) ***önce sistemi boot edebilecek bir disket hazırlamanız gerekiyor. Bunun için Win9x veya Windows Me kullanıyorsanız, disket sürücünüze boş bir disket koyup, **Başlat-Ayarlar-Denetim Masası-Program Ekle/Kaldır-Başlangıç Disketi ** yolunu izleyip, bir açılış disketi oluşturun.

PC'yi bu disket ile açmanız gerektiğinden, BIOS'a girip **ADVANCED BIOS FEATURES** menüsünden, boot sırasında birinciliği disket sürücüsüne verin. Böylece sistemi disketten boot edebileceksiniz.

Anakartın modeline göre, kutucukta belirtilen BIOS dosyalarının adresine gidip, sizin anakartınız için en güncel olan BIOS dosyasını çekin. Ayrıca, **AWDFLASH** programını çekin ve diskete kopyalayın.

Daha sonra BIOS'a girerek, önemli ayarları bir kenara not edin.Bilgisayarı disketten açtıktan sonra komut satırına **awdflash.exe** yazıp entere basın.Karşımıza aşağıdaki gibi bir ekran çıkacaktır.

**File Name to Program** kısmına anakartınızın üreticisinin web sitesinden indirmiş olduğunuz yeni bios bilgilerini içeren **.BIN** uzantılı dosyanın diskinizdeki tam yolunu yazın.Bu işlemi yaptıktan sonra anakartınızın **Flash tipi** okunacak ve ekranda görülecektir.Aşağıda görüldüğü gibi Flash tipi **“Winbond 29C020 / 5V “** olarak ekrana gelmiştir.Daha sonra en alt kısımda size **"Do You Want To Save BIOS? "** şu anda kullandığınız BIOS'u kayıt edip etmeyeceğinizi sorulur. **"Y"** tuşuna basarak bunu kabul edin.

Daha sonra sizden şu anki bios dosyanızı biryere yedeklemeniz için bir dizin ve dosya ismi girmeniz istenecektir. örneğin dosya ismi olarak ESKIBIOS.BIN verebilirsiniz.

Bu işlemi yaptıktan sonra entere bastığımızda karşımıza **“Now Backup System Bios to a file “** uyarı yazısı gelecektir.

Bu işlem bittikten sonra alt bölümde ikinci bir soru belirecek: **“Are you sure to program?”** BIOS’u güncellemek istediğinize emin olup olmadığınız sorusuna **“Y”** tuşuna basıp devam edin.BIOS güncellenecek ve bilgisayarınız otomatik olarak tekrardan başlayacaktır.Post ekranında iken DEL tuşuna basarak BIOS'a girin ve LOAD SETUP DEFAULTS seçeneğini uygulayın. Değiştirmek istediğiniz ayarları değiştirip, kayıt edip çıkın.Açılışta POST ekranında sağ üst köşede göreceksiniz ki BIOS ‘un versiyonu değişmiştir. Böylece BIOS ‘u sağlıklı bir şekilde güncelleyebildiğinizi anlayabilirsiniz.

## **6 - AMI BIOS GÜNCELLEME İŞLEMLERİ ******

***(1) ***Bir sistem disketi oluşturun . İnternetten çekeceğiniz **ROM** uzantılı dosyayı diskete kopyalayın. Aynı diskete yine internetten **Ami703e.com** dosyasını kopyalayın.ROM uzantılı bu dosyanın bir kopyasını acil durumlarda kullanabilmek için başka bir diskette saklayın ve dosya ismini **AMIBOOT.ROM** olarak değiştirin.Sistem disketi ile sistemi açın ve şunları yazın:

## **AMI703E xxxxxx.ROM ******

**xxxxxx** olan yere BIOS dosyasının ismini yazacaksınız.

**"Y"** tuşuna bastığınızda, güncelleme işlemi başlayacaktır. Programlama işlemi başarılı olursa, **"Flash EEPROM Program Successful"** mesajı görünecektir. Bir tuşa bastığınızda sistem yeniden başlayacaktır.

## **7 - BAZI ANAKART İÇİN GÜNCELLEME İŞLEMLERİ******

## ** a - ASUS ANAKARTLAR ve BIOS GÜNCELLEMESİ******

***(******1)*** ASUS Anakartlarda, genelde **AWARD BIOS** kullanılıyor. Sadece, şu an için eski bir kart sayılan **ASUS K7M’**de **AMI BIOS** kullanılmıştı. Onun haricinde, AWARD BIOS kullanılıyor. Fakat ASUS P3B-F dahil olmak üzere ondan sonra ASUS un çıkan tüm anakartlarında, alışık olduğumuz AWARD Moduler BIOS’un aksine, AWARD Medallion BIOS kullanılmıştır.

Award Medallion BIOS

ASUS anakartların BIOS’unu güncellemek için, ASUS’a özel olan **AFLASH** programını kullanmak gerekiyor. K7M serisi için ise, Flash822.exe dosyasını kullanmak gerekiyor.
Genel olarak bakıldığında, Asus anakartların BIOS’unu güncellemek için iki adet dosyaya ihtiyacımız var. AFLASH.exe ve güncel BIOS dosyası.

## ***(7) ***** Güncelleme İşlemleri :**

Bir açılış disketi oluşturun.

AFLASH.EXE programını oluşturduğunuz diskete kopyalayın

Aflash.exe programını disketten çalıştırın ve **“1.Save Current Bios to File”** seçe seçin.

ASUS BIOS dosyasını ASUS ‘un web sitesinden daha önceden oluşturmuş olduğunuz diskete indirin.

Ssistem disketti ile açılış yapın.

Sistem A sürücüsünde iken **Aflash.exe** yazıp enter tuşuna basın.

Ana Menü’de iken **2** numaralı seçeneği girin ve enter tuşuna basın.

**“ Are you sure ?”** sorusuna **“Y”** tuşuna basarak evet deyin.

Yeni BIOS bilgisi programlanmaya başlanır. Programlama işlemi bittikten sonra **“Flashed Succesfully”** yazısı görünür.

Karşımıza son gelen ekrandaki talimatları takip ederek BIOS güncelleme işlemini bitiririz.

**Talimatlar:** EPROM ‘u güncellediniz;Sistemi yeniden başlatıp sisteme girmeniz ve yeni BIOS ile güncellenmiş CMOS ‘u görmek için Load Setup Defaults seçeneğini seçmeniz tavsiye olunur.

## b - GIGABYTE ANAKARTLAR ve BIOS GÜNCELLEMESİ

## ***(6)***** Güncelleme İşlemleri :******

· Bir sistem disketi hazırlayın..

**Not:**
A.Bu işlem disket sürücünüzdeki bütün bilgileri kaybetmenize sebep olacaktır.Bu sebeple dikkatli olunuz.

B. Tipik olarak 4 dosya disketinize transfer edilecek fakat bunlardan sadece command.com görünebilir olacaktır.

C. Son olarak disketinizdeki bu dosyaların güvenliği için yazmaya karşı koruma tırnağını açın.

· BIOS güncelleme dosyasını ve sıkıştırılmış haldeki **awdflash.exe** programını Gigabyte sitesinden indirin.

· Sıkıştırılmış awdflash.exe dosyasını pkunzip veya winzip gibi programlarla 1. adımda hazırlamış olduğunuz diskete açın.Daha sonra yine indirmiş olduğunuz yeni BIOS dosyasını da diskete kopyalayın.

** Not:
** Bu iki programı da aşağıda görmüş olduğunuz adresten bulabilirsiniz.
www.shareware.com
· Yeni hazırlamış olduğunuz disketi kullanmak için sisteminizi tekrardan başlatın.Sisteminiz disketten açılış yapsın.

· DOS komut satırında iken **awdflash.exe dosya\_adı.xxx** komutunu yazın ve enter tuşuna basın. **Dosya\_adı.xxx** dosyası sizin Gigabyte sitesinden indirmiş olduğunuz ve diskete kopyaladığınız bios güncelleme dosyasıdır.

· Sıradaki ilk seçeneğiniz, eski BIOS’u kaydetmek olacaktır.. Bu işlemi yapmanız tavsiye olunur. BIOS’u güncelledikten sonra yeni özelliklerden memnun olmayabilirsiniz.
A. Eski BIOS’u kaydetmeye karar verirseniz, yeni BIOS’un adıyla kaydetmediğinizden emin olun.Eğer eski bios’a yeni bios dosyası ile aynı ismi verirseniz eski bios bilgileri yeni bios dosyasının üzerine hiçbir uyarı olmadan yazılacaktır. En basit isim verme şekli ESKIBIOS.BIN şeklinde olabilir.

B. Eğer eski bios dosyanızı biryere kaydetmek istemiyorsanız en azından eski bios’ un versiyon numarasını biryerlere not alın. Hayır demek için ‘N’ tuşuna basarak bir sonraki adıma geçin.

· Eski BIOS’u kaydetmek için evet anlamında ‘Y’ tuşuna basın.
· Eski bios için bir isim verin ve enter tuşuna basın.
· Sıradaki ikinci seçeneğiniz BIOS’u güncellemek isteyip istemediğiniz olacaktır.

Evet demek için ‘Y’ tuşuna basın.

** Not:**
Bu adım çok kritiktir.Flash işlemi sürmekte iken kesinlikle klavyeye,reset tuşuna veya açma kapama butonuna dokunmayın.

· BIOS güncelleme işlemi tamamlandıktan sonra disketinizi disket sürücüden çıkartın ve sisteminizi tekrar başlatın. Açılışta POST ekranındayken BIOS versiyonunun değişmiş olduğunu göreceksiniz. Artık işlem tamamlanmıştır.

## **c - ABIT ANAKARTLAR ve BIOS GÜNCELLEMESİ******

***(1) ***ABIT Anakartların hemen hepsi AWARD BIOS kullanıyor. Abit’in sitesi Türkçe olarak hizmet veriyor.

Abit’in Türkçe sayfalarına http://www.abit.com.tw/turkish/index.htm adresinden ulaşabilirsiniz. önceden, Abit anakartların BIOS’unu update etmek için 3 adet dosya gerekiyordu; ama şimdi o sistem yok. İki dosyaya ihtiyaç duyacaksınız. Birincisi AWDFLASH programı, ikincisi ise BIOS güncellemede kullanacağımız BIN uzantılı yeni BIOS dosyası.

## **Güncelleme İşlemleri (örnek Anakart: ABIT SE6)******

· önce sistemi boot edebilecek bir disket hazırlamamız gerekiyor. Bunun için Win9x veya Windows Me kullanıyorsanız, disket sürücünüze boş bir disket koyup, **Başlat-Ayarlar-Denetim Masası-Program Ekle/Kaldır-Başlangıç Disketi ** yolunu izleyip, bir açılış disketi oluşturun. PC’yi bu disket ile açmanız gerektiğinden, BIOS’a girip **ADVANCED BIOS FEATURES** menüsünden, boot sırasında birinciliği disket sürücünüze verin. Böylece sistemi disketten boot edebileceksiniz.

· Anakartınızın modeline göre, kutucukta belirtilen BIOS dosyalarının adresine gidip, sizin anakartınız için en güncel olan BIOS dosyasını çekin. Ayrıca, AWDFLASH programını çekmeniz gerekiyor. Daha sonra BIOS’a girerek, önemli ayarları bir kenara not edin.

· Bilgisayarı disketten açtıktan sonra, komut satırına:* ***awdflash dosya\_adı.xxx **
yazıp Enter tuşuna basın. **Dosya\_adı.xxx** yerine, anakartımız için İnternetten çektiğiniz BIOS dosyasının ismini yazacaksınız. örneğin:

**awdflash SE6\_SW.BIN ******

· AWDFLASH programına girdiğinizde, size alt bölümde bir soru sorulacak : **“Do You Want To Save Bios?” **Şu anda kullandığınız BIOS’u kayıt edip etmeyeceğiniz sorusunu **“Y”** tuşuna basarak bunu kabul edin ve kayıt edilmesi için bir dosya adı girin . örneğin: **eskibios.bin******

· Bu işlem bittikten sonra, alt bölümde ikinci bir soru belirecek:

**“Are you sure to program ” **BIOS’u güncellemek istediğinizden emin olup olmadığınız sorusuna. **“Y”** tuşuna basıp devam ediyoruz.

· İşlem bittiğinde, bilgisayarınızı yeniden başlatarak BIOS’a girin ve LOAD SETUP DEFAULTS seçeneğini uygulayın. Değiştirmek istediğiniz ayarları değiştirip, kayıt edip çıkın. Abit, bu işi otomatikleştirmek için birkaç komut daha yazmanızı daha mantıklı buluyor. Bilgisayarınızı hazırladığınız sistem disketiyle açtıktan sonra komut satırına aşağıdakileri yazmak olacak :

**awdflash SE6\_SW.BIN /cc /cd /cp /py /sn /cks /r
**Buradaki harflerin anlamları :

**cc **: Güncelleme işlemi bittikten sonra CMOS bilgilerini sil

**cd **: Güncelleme işlemi bittikten sonra DMI bilgilerini sil

**cp **: Güncelleme işlemi bittikten sonra PnP bilgilerini sil

**py **:BIOS’u Güncelle

**sn **: BIOS yedeği alma

**cks **:** **Güncelleşmiş dosyayı eskisi ile karılaştır

**r ** : Güncelleme işlemi bittikten sonra sistemi yeniden başlat.

## **d - MSI ANAKARTLAR ve BIOS GüNCELLEMESİ******

***(1) ***MSI, anakartlarının bir çoğunda AWARD BIOS kullanılıyor. Fakat AMI BIOS kullanan bazı modelleri de bulunmaktadır.

**Award BIOS Kullanan MSI Anakartlar İçin Güncelleme İşlemleri :**
MSI, BIOS güncelleme işini kolaylaştırmak için, bütün dosyaları aynı dosya içinde sıkıştırıp sitesine koymuş. Anakartınızın modeline uygun dosyayı indirdikten sonra, bunu bir klasöre açın. Bu klasörün içine baktığınızda, Autoexec.bat dosyası göreceksiniz.Bunun anlamı güncelleme işleminin otomatik olacağıdır. Sistem disketinize, klasörünüzde yer alan tüm dosyaları kopyalayın, ve sistemi yeniden başlatın. İşlem bittiğinde bilgisayarınız yeniden başlayacaktır.Eğer otomatik olark değilde klasik yöntemle BIOS’u güncellemek istiyorsanız ve eğer AWARD BIOS’lu MSI anakarta sahipseniz, GigaByte anakartlar için anlatılan prosedürün aynısını MSI anakartlarda da uygulayabilirsiniz.

**Ami BIOS Kullanan MSI Anakartlar İçin Güncelleme İşlemleri :**
MSI’nin AMI BIOS kullanan anakartları da var. Bunlar için Güncelleme işlemlerine bakacak olursak :

· Bir sistem disketi oluşturun. İnternetten çekeceğiniz dosyayı diskete kopyalayın. Aynı diskete yine MSI’nin sitesinden çekeceğiniz **AMIFL634.EXE** dosyasını kopyalayın.

· Yeni BIOS dosyasının adı şu şekilde olmalı : **A54MS10.ROM ** Bu dosyanın bir kopyasını başka bir diskette acil durumlarda kullanmak üzere saklayın ve dosya ismini **AMIBOOT.ROM** olarak değiştirin.

· Sistem disketi ile sistemi açın ve şunları yazın: **AMIFL634 xxxxxx.rom
**
**xxxxx.rom** olan yere BIOS dosyasının ismini yazacaksınız.

·** “Y”** tuşuna bastığınızda, güncelleme işlemi başlayacaktır. Programlama işlemi başarılı olursa, **“Flash EEPROM Program Successful”** mesajı görünecektir. Bir tuşa bastığınızda sistem yeniden başlayacaktır.

## **e - INTEL ANAKARTLAR ve BIOS GÜNCELLEMESİ******

***(1)*** Intel, hemen hemen tüm yeni anakartlarında **Phoenix BIOS** kullanıyor. Phoenix BIOS genelde markalı PC’lerde kullanılan bir BIOS markası. Ve Phoenix BIOS, anakartınızın markasını belirleyebileceğiniz kod numaraları da sunmuyor. Ama, eğer INTEL marka anakarta sahipseniz, açılışta INTEL anakarta sahip olduğunuzu gösteren bir logo ile karşılaşacaksınız. Modelini ise “CTRL+ALT+ESC” tuş kombinasyonunu kullanarak POST ekranına geçtiğinizde en üstte göreceksiniz.

**Güncelleme İşlemleri :******

· önce sistemi boot edebilecek bir disket hazırlamamız gerekiyor.Bunun için Win9x veya Windows Me kullanıyorsanız, disket sürücünüze boş bir disket koyup, **Başlat-Ayarlar-Denetim Masası-Program Ekle/Kaldır-Başlangıç Disketi ** yolunu izleyip, bir açılış disketi oluşturun.PC’yi bu disket ile açmanız gerektiğinden, BIOS’a girip BOOT menüsünden, boot sırasında birinciliği disket sürücünüze verin. Böylece sistemi disketten boot edebileceksiniz.

· Intel’in Web sitesinden BIOS dosyalarını indirin ve bu dosyayı sabit diskinizde ayrı bir dizine koyduktan sonra, üzerine çift tıklayın. çift tıkladıktan sonra “Bios.exe” ve “Mk\_bootz.exe” adında iki dosya çıkacak.

· “Bios.exe” dosyasına çift tıklayın.Açılan dosyaları diskete kopyalayın.

· Yeni disketimiz ile sistemi açmadan önce, BIOS’a girip tüm ayarları bir kenara not etmenizde fayda var.

· Intel BIOS güncelleme için farklı bir açılış disketi hazırlamış; ekrana gelen menü de Enter tuşuna basın.

· **“Update Flash Memory From a File”** seçeneğini seçin.

· **“Update System BIOS”** seçeneğini seçin.

· Yeni BIOS dosyanızın ismi sorulacak. Buraya güncellenecek BIOS dosyasının ismini yazın. İşlem bitene dek bekleyin ve işlem bittiğinde disket sürücüden disketi çıkartarak yeniden bilgisayarı başlatın ve BIOS’a girin. Not aldığınız ayarları tekrar düzenleyin.

## **8 - CANLI BIOS GÜNCELLEME******

***(1)*** Şu an için Asus, GigaByte ve MSI, bazı anakart modelleri için, Canlı BIOS Güncelleme olayını sunuyor. BIOS Güncellemenin artık son zamanlarda bir gereklilik olduğu bir dönemdeyken Asus, GigaByte, MSI gibi firmalar BIOS güncelleme konusunda kullanıcılarına daha kolay bir ortam hazırlamak için özel programcıkları kullanıcılara sunmakta. Bu firmaların yazdığı özel programcıklar sayesinde anakartınızın BIOS’unu fazla uğraşmadan, ve teknik bir bilgiye sahip olmadan güncelleyebiliyorsunuz. Firmaların kendi anakartları için hazırladıkları programlar farklılık gösteriyor ama genelde mantık aynı: Anakartın modelini otomatik olarak algılayıp (veya siz göstereceksiniz), Internetten uygun yeni BIOS dosyasını çekip, güncellemeyi yapmak. Bu programların Win9x /Nt4,0/WinME ve Win2000 altında çalışabiliyor olması kullanıcılara kolaylık sağlıyor.

Asus ve GigaByte’ın programları benzer mantıkta. 2 farklı şekilde BIOS’unuz güncelleyebiliyorsunuz. Eğer daha önceden yeni BIOS’u Internetten çekmediyseniz, bu programlar aracılığı ile, Internetten uygun BIOS dosyasını çekebiliyorsunuz. Dolayısı ile anakartınızın üreticisinin WEB sayfasına gidip, BIOS dosyası aramaktan kurtulursunuz. Bu programlar, anakartınızın modelini otomatik olarak belirliyor. Fakat her anakart “Canlı” BIOS Güncelleme olayını desteklemiyor.

İkinci yöntem ise, dosyayı ayrıca çekmek ve daha sonra güncelleme programında yeni bios dosyasının diskinizdeki yerini belirtmek. Eklenmesi gereken bir ayrıntıda şu ki Asus’un programı olan “Asus Update” programı, GigaByte’ın “@BIOS” programından daha başarılı ve kullanıcı arabirimi çok daha güzel.

MSI’nin Live BIOS programını Internetten yüklüyoruz

MSI ise kısmen farklı bir yol izlemiş. MSI bu işi programla yapıyor ama web üzerinden. Programı web üzerinden yüklüyorsunuz, ve anakartınızın modeli program üzerinde değil de, web üzerinde tanınıyor ve ona göre BIOS dosyası çekiliyor. Geri kalan işlemler ise benzer.
Asus UPDATE: http://www.cizgi.com.tr/sss/sssliveupd-1.htm

GigaByte @BIOS: http://www.gigabyte.com.tw/home/a\_bios.htm

MSI Live BIOS: http://www.msi.com.tw/support/feature/livebios/livebios.htm

## **9 - BIOS KURTARMA İŞLEMLERİ******

## **a - Intel Flash ROM ‘lu Anakartlar İçin BIOS Kurtarma******

***(1)*** Eğer Intel marka bir anakarta sahipseniz diğer anakart kullanıcılarına göre şanslısınız. Zira, INTEL FLASH ROM’un **Boot Block** denilen bölgesi için yazma korumasına sahip. Boot Block, BIOS çipinde çok ufak bir yer kaplayan ,bilgisayarın açılabilmesi için bir takım algoritmalara sahip sistemciktir. Dolayısı ile aslında bu bölümün güncellenmesi gerekmiyor. INTEL, kendi ürettiği FLASH ROM ( BIOS çipi )’ larda bu boot block koruma özelliğini koymuş ve bu FLASH ROM’u kullanan anakartlarda, BIOS Güncellemesi sonucunda sorun yaşama ihtimalinin yok denecek kadar az. BIOS Güncelleme esnasında elektrikler kesilse bile BIOS’unuzun Boot Block bölümü hasar görmediğinden, bilgisayarınız yine açılacaktır ve Güncelleme işlemini tekrardan yapmanız istenecektir. çünkü, BIOS Güncelleme olayının ilk bölümünde, BIOS çipindeki bilgiler silinir, ikinci adımda ise bilgiler tekrar yazılır. Yani yarıda kalan işlem sonucunda tekrar BIOS Güncelleme yapmalısınız. İntel marka anakartlarda herhangi bir sorunla karşılaşıldığında uygulanması gereken yöntem şudur :

1. INTEL anakartların üzerindeki “flash recovery” olarak tanımlanan jumper’ı bulun ve kurtarma (recovery) pozisyonuna getirin.

2. Daha önce , INTEL anakartlar için hazırladığınız disket ile sistemi açın.

3. Görüntü alamayacaksınız,fakat bu sorun değil çünkü işlemleri bip sesleriyle yapacaksınız. Bip sesi duyduğunuz anda Disket Sürücünüzün ışığı yanıyor ise, işlem başlamıştır demektir. Floppy ışığı söndüğünde işlem bitmiştir.

4. Sistemi kapatın ve jumper’ı eski konumuna getirin.

5. Sisteminizi tekrar açın ve güncelleme işlemine başlayın.

## ***b - Award BIOS Kullanan Anakartlar İçin BIOS Kurtarma*********

Şimdi anlatılacak çözüm ise, AWARD BIOS kullanan bir çok anakart kullanıcıları için geçerli olacak bir çözüm (ASUS hariç). AWARD BIOS’a sahip anakartlarda işe yarayan bir kurtarma olayı otomatikleştirilmiş bir olay. örneğin BIOS Güncelleme sırasında, elektrik kesilmesi gibi bir sorun oluştu ve bilgisayarınız açılmaz hale geldi. Panik yapmadan hemen İnternet erişimi olan başka bir bilgisayar bulun ve işlemlere başlayın .

1. İlk olarak bir sistem disketi oluşturun : format a:/q/s

2. Anakartınızın üreticisinin WEB adresine gidin ve kendi anakartınız için olan yeni BIOS dosyasını indirin. AWDFLASH programını da indirin. AWDFLASH programını ve BIOS dosyasını diskete kopyalayın. Ve sisteminizdeki Autoexec.bat dosyasını da diskete kopyalayın. Şimdi Disket Sürücünün içindeyken, Autoexec.bat dosyasına sağ tuş tıklayıp düzenle deyin. Autoexec.bat içerisindeki tüm satırları silin. Ve şunları yazın:

## ***A:\\AWDFLASH dosya\_adı.xxx /SN /PY /CP /CD /CC ***

örneğin:

## ***A:\\AWDFLASH W6334VMS.bin /SN /PY /CP /CD /CC***

Bu arada yukarıda AWRDFLASH programının AWDFLASH.EXE şeklinde bulunacağı varsayılarak, AWDFLASH yazıldı. Ama aynı program AWDFL770 gibi isimlerle de bulunabilir. çektiğiniz AWARD BIOS Güncelleme programının ismine göre, verdiğimiz komut satırını değiştirmemiz gerekiyor.

örneğin :

## ***A:\\AWDFL770 w6334VMS.bin /SN /PY /CP /CD /CC***

Autoexec.bat dosyası içindeki değişiklikleri yaptıktan sonra, bunu kayıt edin.

3. Bu disket ile, sistemi açın. Ekrana görüntü gelmeyecektir. Bip sesiyle beraber, Disket Sürücü ışığının yanmasıyla işlem başlayacaktır. 1,5 – 2 dakika arası sürecek bir işlemden sonra, disket sürücünün ışığı sönecektir. Ve sistemi artık başlatabilirsiniz! Fakat bu yöntem her anakartta çalışmıyor.

## **c - Award BIOS’ lu *****ASUS***** Anakartlar İçin BIOS Kurtarma ******

Daha önce belirtildiği gibi, ASUS, kendi anakartlarındaki BIOS Güncelleme işlemini yapabilmeniz için AFLASH programını sizlere sunuyor. Kilit nokta şu: AFLASH programını çalıştırdığınızda, karşınızda duran ikinci seçenek şudur : **“Update BIOS Including Boot Block and ESCD” **(“ Boot Block ve ESCD dahil BIOS’u güncelle”) . BU demektir ki Asus Anakartların BIOS’unu güncellerken bir sorun çıkarsa, Boot Block’un zarar görmüş olması ihtimaller arasında. O zaman sisteminiz açılmayacak anlamına gelir. Tabii her zaman böyle olacak diye bir kaide yok. Boot Block gerekli olduğu vakitlerde güncelleniyor.

## **d – Ami BIOS Kullanan Anakartlar İçin BIOS Kurtarma******

AMI BIOS’lar için genelde ortak bir kurtarma yöntemi var.

1.AMI BIOS’u olan anakartınızın markasına ve modeline göre, anakartınızın üreticinizin adresinden yeni BIOS dosyasını çekin. Bu dosyanın ismi şuna benzer bir şey olur : A54MS10.ROM

2. Bu dosyanın ismini, AMIBOOT.ROM olarak değiştirin. Sonra bunu boş bir diskete kopyalayın.

3. Diskete sistem dosyalarını transfer ETMEYİN. Diskette sadece ve sadece AMIBOOT.ROM dosyası olacak. Açılmayan sisteme bu disketi koyduktan sonra, CTRL ve HOME tuşlarını nasılı tutarken sistemi açın. Disket Sürücünün ışığı yandıktan sonra elinizi bu tuşlardan çekin.

4. Sistem, BIOS Güncelleme olayını yaklaşık 35-40 saniye içinde bitirecek. İşlem bittiğinde birkaç bip sesi çıkacaktır. Daha sonra sisteminizi açabilirsiniz!

---
*Kaynak: `BIOS VE BIOS GÜNCELLEME İŞLEMLERİ/BIOS VE BIOS GÜNCELLEME İŞLEMLERİ.doc` — YUSUF — 2004*
