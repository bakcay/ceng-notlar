# Flash Nedir

**FLASH NEDİR?**
Flash vektörel grafiklerle animasyonlar hazırlayabileceğiniz, bu animasyonların birbirleriyle etkileşmesini sağlayabileceğiniz, ve en son sürümlerinin (flash 4 ve 5) özelliği olan veritabanları ile **asp**, **php** ve **cgi** gibi script dillerinin yardımıyla haberleşebileceğiniz bir web sayfası nesne geliştirme programıdır.

Önce bahsettiğimiz vektörel grafiği açıklayalım. Photoshop vb. programlarda grafikler hazırladığınızda bu grafikleri daha yakından görmek isterseniz görüntünün bozulduğunu resimde veya grafiğinizde kareleşmeler oluştuğunu, yani bazı yerlerin olması gerektiği gibi yuvarlakça görünmediğini fark edersiniz. Bunun sebebi grafik programlarının, daha doğrusu Windows'un grafikleri -veya resimleri de diyebilirsiniz- her noktası için ayrı tanımlama yaparak tanımasıdır. Yani her bir nokta tanınır ve yan yana getirilince grafik ortaya çıkar. Vektörel grafiklerde ise grafik bir başlangıç noktası, uzunluğu ve yönü vardır diyebilirsiniz.

Bu tanımlamayı direk vektör grafikler için yapamasak bile en azından vektörel büyüklüklerin genel tanımı olarak düşünürsek vektörel grafiklerin de bu çeşit grafikler olduğunu söyleyebiliriz. Yani vektörel grafikler için yapılan tanımlamada bu şekilde birkaç unsur vardır ve bu unsurları belirttiğinizde grafiği tanımlamış olursunuz. Bu da demektir ki kaba bir tabirle bilgisayarınız da vektörel grafikleri bu şekilde birkaç özelliğiyle tanıyabilecektir. Aynı zamanda bu da bilgisayarınızın daha az alanının işgal edilmesi demektir. Yani daha az dosya boyutu. Üstelik nesne noktasal olarak belirlenmediği için, photoshop gibi bir programdaki gibi zoom yaptığınızda görüntü bozulmayacaktır. Nesne büyütülse bile tanımlama olarak **başlangıç**, **son**, **uzunluk**, **yön**, **renk** vb değerler kullanıldığı için, cisim bozulmadan görüntülenir.

Flash'ı tanımladıktan sonra neler yapabildiğine de biraz değinelim. Hala kullanıldığını göz önüne alarak flash 4 ü de düşünelim ve direk onu anlatalım. Tabi flash 5 in birkaç artısı var. Flash ile animasyonlar hazırlayıp, bu animasyonların kendi içlerindeki kısımların birbirleriyle etkileşimli olmasını sağlayabilirsiniz. Yani bir buton hazırladığınızda bu butonun içerdeki bir animasyonu başlatmasını bitirmesini veya belli bir yerden devam ettirmesini sağlayabilirsiniz. Bunlar basit örnekler tabi.

Flash ile bir ziyaretçi defteri bile yapabilirsiniz örneğin. Nasıl mı? Uygun bir asp dosyası hazırlarsınız ve flash'ın içine bu asp dosyası ile haberleşmeyi sağlayacak action script kodlarını yerleştirirsiniz. Daha bir çok uygulama da yapılabilir. Yani flash ile database de kullanabilirsiniz. Geri veritabanınızdan bilgileri alacak bir asp, php, cgi dosyasına ihtiyacınız olur ama sonuçta siz flash üzerinde bu verileri görüntülersiniz. Şimdi açıklamamız gereken önemli bir şeyi geçmeyelim. Flash ile çalıştıktan sonra çalışmanızı uzantısı "fla" olan flash'a özel bir dosya türü şeklinde kaydedersiniz. Bundan sonra kullanma amacınıza göre değişik dosya türleri şeklinde bu animasyonu publish edersiniz yani bir nev'i yayınlarsınız, ilan edersiniz, gösteri şekline getirirsiniz, sunarsınız vs. flash çalışmalarında sonuç olarak bu şekilde hazırlayabileceğiniz birçok dosya formatı vardır. İlki uzantısı "swf" olan flash movieler.

Bunlar çalışması için bir Active X yüklenimine ihtiyaç duyulan özel bir formattır. Hep özel diyoruz ama aslında çok genel formatlar da dosyalar şeklinde publish edebilirsiniz çalışmalarınızı. Bunlardan bazılarını hiç açıklamadan direk yazıyorum. Html, gif, jpg, png, windows exe'si, macintosh exe'si ve quick time dosyası olarak yayınlayabilirsiniz. Tabi bunların kendi özelliklerine göre yayınlayabilirsiniz. Örneğin bir gif resminin içinde butonun çalışmasını bekleyemezsiniz. Diğerlerinde de böyle tabi ki, mesela bir quick time movie sinde de buton çalışmaz. Ama swf de html de ve exe de çalışır.

Flash kısaca bu şekilde tanımlanabilir ve tanıtılabilir. Bundan sonraki kısım flash'ın nasıl kullanıldığını öğrenmek olacaktır.

**FLASH PENCERESİNİN ÖĞELERİNİ TANIYALIM**
Flash ekranında standart olarak kullanacağınız 6 unsur vardır. İlk iki tanesi her sürükle bırak tekniğinin kullanıldığı programda veya her explorer penceresinde gördüğünüz dosya, düzen, görünüm, vs. menülerin bulunduğu kısım ve bunların butonlarla kısa yollarının bulunduğu bir bar. Üçüncüsü çalışma aletlerinin bulunduğu toolbar. Dördüncüsü movilerinizin doğru yürüyüp yürümediğini test edeceğiniz control barı. Son ikisi ise en önemli unsurlar olan çalışmalarınızı yapacağınız stage(sahne) ve her kareyi ayrı ayrı denetlemenizi sağlayan ve katmanları düzenlediğiniz timeline(zaman çizgisi)

**Stage** üzerinde gördüğünüz beyaz kısım movienizin alanı. Bu alanın dışındaki öğeler yayınladığınız movilerde görünmez. Bu grafiklerinizi çizip değerlendireceğiniz alan yani kısacası görsel olarak çalışacağınız alan.

**Timeline** şekilde stage'in tam üzerinde bulunan alan. Burada movienizin her bir karesini görüyorsunuz. Yani bu kareler ard arda görüntülendiğinde movieniz yürütülmüş oluyor. Bu alanın sağ tarafında bu frameler(yani filmin kareleri) sol tarfında ise layerlar(yani katmanlar bulunuyor. Layerlar ise hangi grafiğin hangisinin üzerinde bulunacağını belirlerler. Zaten adından da belli, bunlar katmanlar.

**Control** tuşları timeline nin sağ üst tarafında görünenler. Play, stop, rewind, forward vs.

**Standart bar** ımız timelinenin sol üst tarafında ve dediğimiz gibi normal kaydetme dosya açma kopyala yapıştır vb. işlevleri olan tuşlar içermekte.

**Toolbar** ise en solda. Toolbarın elemanları önemli olduğu için tek tek anlatalım.
**Arrow(ok): **Ok, herprogramda olduğu gibi tutup taşıma, nesne veya alan seçme gibi işlemleri gerçekleştirmek için.
**Lasso(kement):** Daha ince seçimler yapabilmek için.
**Line(çizgi)**: Çeşitli özelliklerde çizgiler çizebilmek için.
**Text tool(yazı aleti): **Yazı eklemek için.
**Oval(eliptik nesne aleti)**: Eliptik nesneler çizmek için. Bu aletin dolgu rengi ve çizgi renk ve stilleri düzenlenebilmektedir.
**Rectangle(dikdörtgen aleti):** Tabi ki bu da dikdörtgenimsi şekiller çizmek için ve bunun da dışçizgi, dolgu ve ayrıca köşe yumuşatma özellikleri düzenlenebiliyor.
**Pencil(kalem): **Rastgele çizgiler çizmek için. İstediğiniz gibi, sınır yok.
**Brush(fırça):** Değişik uç seçenekleriyle özelleştirebileceğiniz bir fırça.
**İnk bottle(çizgi renklerini düzenler):** Çizdiğiniz nesnelerin dış çizgi renklerini ve stillerini düzenler.
**Paint bucket(dolgu rengi):** Grafiklerinizin dolgu rengini düzenlemek için.
**Dropper(renk seçici): **Renk seçmek için.
**Eraser(silgi): **Adı üstünde
**Hand(el):** Sahneyi taşımak için.
**Magnifier(mercek):** Zoom için, büyüteç.

**MOTİON TWEEN**
Flash'da animasyon hazırlamada en temel iki efektten biri motion tweendir. Buna efekt demek de doğru değil aslında. Flash'da hareket sağlamak için iki yöntemden biri de diyebiliriz.

Adından da anlaşılacağı gibi motion tween hareket kazandırma etkisidir. Sadece grafikler, grubu çözülmemiş yazılar, grubu çözülmemiş resimler gibi grupsal nesneler üzerine uygulanabilir. Yani oval aleti ile çizdiğiniz bir daireye hemen motion tween uygulayamazsınız. Önce bunu grafik haline getirmelisiniz. Yani ok ile işaretleyip insert>convert to symbol yapmalısınız.

Bir frame'e bir şekil çizip, bu şekli dediğimiz komutla grafik yapın. Sonra bu frame in aynısından ileriki (örneğin 15.) frame e sağ tıklayıp insert keyframe deyin. Yani oraya ilk frame deki içeriğin aynısını taşıyacak bir frame ekleyin. Şimdi bu son karemize kadar bu şekille doldurduk. Son frame de şeklin nerede olmasını istiyorsanız oraya taşıyın.

Sonra da ilk frame e çift tıklayarak tweening kısmını açıp motion tween i seçin. Kontrol tuşları ile movie nizi yürüttüğünüzde çizdiğiniz nesnenin her frame de aynı miktar yer değiştirerek ilk framedeki yerinden son framedeki yerine doğru hareket ettiğini göreceksiniz.

Motion Tween denilen şey, resimlerin, yazıların, şekillerin animasyonda yer değiştirmesidir. Yani bir dikdörtgeni sağdan sola hareketi Motion Tween ile gerçekleşir. Vektör tabanlı bir programla çalıştığınız için, Flash'ta yaptığınız animasyonlar, normal filimler gibi ardarda gösterilen resimler değildir.

Bir televizyon filminde, elma yere düşüyomuş gibi görmemizi sağlayan, düşme olayının ardarda hızlı bir şekilde gösterilen resimleridir. FLASH ta yaptığınız tüm animasyonlar ise aslında sadece komutlardan ibarettir.

Yani elmanın başlangıç noktasını , bitiş noktasını ve yerçekiminin ne kadar olacağını ( Bunun nasıl yapıldığını Easing Metodu adlı ders notumda bulabilirsiniz )programa belirtirsiniz, FLASH gerekli olan bütün matematiksel hesapları sizin için yapar ve ortaya animasyonunuzu çıkartır.

Bakın çok basit bir **Motion Tween **ile bunu açıklayalım:

FLASH ı açın, yeni bir dosya açılacaktır. Rectangle (R) düğmesine basın ve dosya içersinde dilediğiniz bir yere, fazla büyük olmayacak şekilde bir dikdörtgen çizin

Oluşturduğunuz bu dikdörtgen bir **Obje ( Shape )** dir. Motion Tween uygulayabilmeniz için bu objeyi bir **Sembol( Symbol )** haline getirmelisiniz.
Unutmayın, sadece sembolleri hareket ettirebilirsiniz. Örneğin bu bir dikdörtgen değil de yazı olsaydı, onu da ilk önce sembol haline getirecek ve sonrasında hareket ettirecektiniz.

Bu işlem için, dikdörtgeninizi seçili hale getirerek, **Insert \* Convert to Symbol (F8) **i seçmelisiniz. Karşınıza çıkan sorgu kutusunda, Name kısmına dikdörtgen yazın. Behavior da **Graphic** olarak kalsın. OK e basın.

Şimdi animasyonunuzun ilk karesi hazır. TimeLine a gelerek 15. frame e tıklayın ve **Insert \* Keyframe (F6) **seçin. Bu framede animasyonunuzun son karesi olacak. Şimdi dikdörtgeninize basılı tutarak onu filim içersinde istediğiniz bir yere sürükleyin ve bırakın.

TimeLine kısmında şu görüntüyü elde etmiş olmalısınız :

Şimdi 1. frame e sağ tıklayın. ( Dikkat edin 1. frame aynı zamanda bir **KeyFrame **dir. 15. Frame de öyle. TimeLine kısmında siyah bir noktayla belirtilirler. Şimdilik onlara başlangıç ve bitiş noktaları diyebiliriz.)

**Create Motion Tween **seçeneğini seçin. Şu görüntüyü elde etmiş olmalısınız:

Menülerden **Control \* Play **diyerek animasyonunuzu seyredin.

ZIPLAYAN TOP:

Öncelikle Oval aracı ile kendinize bir daire çizin. **Window>Panels>Mixer** işlemini yaparak, Mixer penceresini açıp topunuza bir renk belirleyin.

Topu Seçin ve **Modify>Group** işlemini yapın.

10. frameye sağ tuşla tıklayarak bir Keyframe ekleyin. 20. frameye de aynı işlemi uygulayın.

** -** 10. framede iken Shift ile topu aşağı doğru taşıyın.

** 5- **şimdi 11. frameye Keyframe ekleyin.

**6- **Tekrar 10. frameye tıklayarak **Modify>Transform>Scale** işlemini yaparak topa yukarıdan aşağıya doğru daraltın.
**7- **1. framede iken Frame penceresinden **Tweening>Motion **işlemini yapın. Scale'nin önündeki işareti kaldırın. Easing kısmı ndan dereceyi -100 (IN) yapyn.

** 8-** 11. framede iken Frame penceresinden **Tweening>Motion** işlemini yapın. Scale'nin önündeki işareti kaldırın. Easing kısmından dereceyi bu defa 100 (OUT) yapın.
**9- Control>Loop Playback** işlemini yapın .
**10-** Artyk animasyonumuz hazır.

**MOVİE KLİP, GRAFİK VE BUTTON**
Flash'da üç türlü grupsal nesne oluşturulabilir.(Dikkat edin dışardan alınan imageleri sesleri ve swf'leri saymıyorum.) Bunlara symbol denir. Bunlar grafikler, movie klipler ve butonlardır.

Grafikler bazı renk ve parlaklık ayarları yapılabilen nesnelerdir. Ayrıca kendi içlerinde animasyonlar da uygulayabilirsiniz.

Movie klipler flash'ın en önemli unsurlarıdır. Bunlar flash'ın içinde ayrı birer movie olarak kullanılması açısından ve dışardan yönetilebilmeleri açısından çok fazla kullanılırla. Neredeyse kendi başlarına birer flash movie'dirler. Ama bir ana flash movienin içindedirler. Yani bir flash filminizin içinde birden fazla ufak film kullanabilir ve bunların birbirlerini kontrollerini rahatça sağlayabilirsiniz.

Buttonlar ise flash da sanki bir visual basic programı butonu gibi işlevsel olabilirler. Butonun over halini, down halini ve buton olarak kabul edilmesi gereken alanı ayrı ayrı düzenleyebilirsiniz.

Şimdi bunları oluşturmanın yollarını öğrenelim:
Bu symbolleri oluşturmanın aslında aynı sonuca varan birkaç yolu vardır. Birincisi önce garfiğinizi hazırlayıp istediğiniz seçimi ok aleti ile yaparak Insert>Convert To Symbol komutu ile açılan pencerede bu çiziminizi üç çeşit symbolden birine dönüştürmek.

İkincisi Insert>New Symbol komutu bu üç çeşitden biri olan yeni bir symbol oluşturmak ve bu komuta okey dediğinizde karşınıza çıkacak o symbolün düzenleme ekranında istediğiniz bir grafiği çizmek.

Üçüncüsü ise Window>Library komutu ile açılacak pencerede yeni symbol düğmesine tıklayarak bu işlemi yapıp yeni bir symbol oluşturmak.

Eğer son iki yöntem ile symbol oluşturduysanız; window>library komutu ile gelen pencerede symbolünüzün ismini tutup stage de istediğiniz bir yere sürüklemek olacaktır. Bu şekilde yapmazsanız hazırladığınız symbolü stage ye eklememiş olursunuz. Ama bu ilk seçenek için geçerli değil. İlk seçenekte zaten grafiğinizi başta oluşturup symbol'e çeviriyorsunuz.

BUTONLAR İLE ÇALIŞMAK

Flash'tadüğmelerin nasıl kullanıldığı konusunda bana birçok soru geliyor. Düğmeye nasıl ses eklenir. Düğmeye link nasıl verilir vs. Bu ders notunun bunun gibi birçok soruyu cevaplandıracağını düşünüyorum. Basit bir düğme çalışmasını yanda görebilirsiniz.
Düğmeye hiçbir komut eklenmediği için, üzerine tıkladığınızda bir şey olmayacaktır.

**File \* New** seçerek yeni bir film oluşturun. Daha sonra elinize sol taraftaki menüden Dikdörtgen çizmeye yarayan Rectangle aracını alın. Filmin içinde herhangi bir yere fazla büyük olmayan dikdörtgen çizin.

Farenizi herhangi bir köşeye getirin. Ve dikdörtgeni seçin. Bu işlemi yapmak için dikdörtgenin dışında bir bölgedeyken farenin sol tuşuna basılı tutup, dikdörtgenin tamamını seçmeye çalışın. Şu görüntüyü elde edeceksiniz:

**Insert \* Convert to Symbol **seçin. Hemen ardından açılan sorgu kutusunda **Button** seçeneğini seçin ve kutuya dugme yazın.

Artık bir düğmeye sahipsiniz. Şimdi sıra "düğmenin üstüne gidince ne olacak ?, tıklayınca ne olacak? " onları ayarlamaya geldi. Düğmenize sağ tıklayarak açılacak menüden **Edit** i seçin.

Bu ekranda TimeLine denilen kısımda sadece 4 tane frame göreceksiniz: Up ( Düğmenin Normal Hali ) , Over (Mouse düğmenin üzerine geldiği andaki hali ), Down ( Mouse ile üzerine tıklanıncaki hali ) ve Hit ( Düğmenin fareyi algılayacağı alan = özellikle yazıları düğme yaparken kullancağınız bu frame çok işe yarayacak ) .

**Over** yazan frame e tıklayarak **F6** ya basın. Böylece bir keyframe eklemiş olacaksınız.

Şimdi film alanındaki dikdörtgeninizden biraz daha büyük ve farklı renkte bir dikdörtgen daha çizin.

İsterseniz bu frame e herhangi bir library den ses dosyası ekleyebilirsiniz. Böylece fare düğmenin üstüne geldiğinde ses çıkacaktır. Benzer işlemleri **Down **keyframe'ine de zevkinize göre uygulayabilirsiniz. İşlemlerinizi bitirdiğinizde **Timeline** üzerindeki sekemlerden **Scene1** e tıklaya rak **Button Edit **modundan çıkıp, **Film Edit** moduna gelin.

Artık aktif bir butona sahipsiniz. Şimdi üzerine tıklayınca ne yapması gerektiğini ona anlatacak olan **Action Script** kodlarına geldi. İlerde bu kodları yazmayı öğreten bir yazı dizisi sunacağız. Ancak şu an için kendi çabalarınızla basit işlemleri yapmayı öğrenebilirsiniz.

Bu kodları girmek için. Düğmeye sağ tıklayıp **Properties **seçin (ya da çift tıklayın) Açılan menüden **Actions **sekmesine tıklayın. Üzerinde + yazan düğmeye basın ve istediğiniz komutu seçin.

Mesela Get URL komutunu seçip, sağ taraftaki gerekli ayarları yaptığınızda, düğmenize tıklayan kullanıcıyı belirli bir adrese yönlendirebilirsiniz.

ZIPLAYAN TOP2

Zıplayan bir top düşünelim. Yere yaklaştıkça yerçekiminin artmasıyla hızı artacak, yere çarptığı anda koruyabildiği momentum ile ters yönde zıplayacaktır. Yükseldikçe yavaşlayacak ve yerçekimine yenik düştüğü anda duracaktır.

Son derece basit bir ayarla sizde Flash animasyonlarınızda, nesneleri hızlandırabilir veya yavaşlatabilirsiniz.

Yeni bir film açın ( **File \* New veya Ctrl + N** )

Bir çember çizin, içini doldurun ( Eğer gerçek bir topa daha çok benzemesini istiyorsanız, Gradient Fill tekniği kullanarak içini doldurabilirsiniz. ) . Daha sonra dairenizi Symbol haline getirin. ( **Insert \* Convert To Symbol veya F8** )

Animasyonu gerçekleştireceğiniz Layer'ın ilk Frame 'inde olduğunuza emin olun. Topunuzu üst sol köşede bir yere oturtun.

Frame 10 a bir Key Frame Ekleyin. ( **F6 **) 10. Frame de iken topunuzu alın ve alt sol köşeye taşıyın. ( Bu sırada topun sağa sola sapmadan direk olarak aşşağı inmesini istiyorsanız taşıma sırasında SHIFT tuşuna basılı tutun.)

Daha sonra 1.ci Frame'e sağ tıklayarak, menuden **Create Motion Tween**'i seçin.

Tekrar sağ tıklayın ve **Properties**'i seçin. **Tweening** sekmesine tıklayın. **Tweening** ayarı **Motion** seçili olduğundan emin olun. **Easing **sürgüsünü sola doğru çekin. (In yazan kısıma) Yan kutudaki rakam - 100 oluncaya kadar bu işlemi yapın.

7.Şimdi topunuz yere düşmek için hazır. Ancak onu yukarı geri taşımak gerek. 1. Key Frame'i seçin ve kopyalayın. ( **Edit \* Copy Frames **). 20. Frame'i seçin ve kopyaladığınız Key Frame'i buraya yapıştırın. ( **Edit \* Paste Frames** )

8.10. ve 20. frameler arasında **Motion Tween** oluşturun. Nasıl yapıldığını unuttuysanız 5.aşamaya bakabilirsiniz. **Timeline **da şu görüntüyü elde etmiş olmalısınız.

9.10. Frame sağ tıklayarak **Properties** ı seçin ve 6. aşamada sürüklediğiniz Easing sürgüsünü **Out** yazan tarafa doğru çekin. Sağ taraftaki kutunun içinde 100 yazıncaya kadar bu işlemi yapın.

10.Artık zıplayan topunuz hazır ! Play tuşuna basarak animasyonunuzu test edin. **Control** menüsündeki **Loop Playback **seçeneği animasyonunuzu sürekli oynatmanızı sağlayacaktır.

Eğer daha fazla doğallık istiyorsanız. 11. **Frame **e bir **Key Frame **koyun ( **F6** ). ve 11.Key Framdeki topun boyutunu üstten biraz kısın. Böylece lastik bir top yere çarptıyormuş gibi görünecektir.

FLASH İLE FORM HAZIRLAMAK

**Giriş :**
Bu dersle Flash 5 ile nasıl form hazırlanacağını öğreneceğiz. Isim , WebSite, Mail, dusunceler adında text filed ve Gönder , Temizle adında form öğeleri oluşturalım.

**Text Fieldler
**Bir tex field yapmak için Toolbarda bulunan simgesine tıklayınız. Stage(Çalışma Alanında)'de istediğiniz yere tıklayınız. Bir text box içinde yanıp sönen bir imleç göreceksiniz. Daha sonra "Text Options" penceresinden "Input Text" i seçiniz.

Variable degerini Isım olarak değiştirin.

Aynı yöntemle WebSite, Mail, ve Dusunceler adında Input Box'lar olsuturun. Tum input boxlar bittiğinde çalışma alanında şöyle bir görüntü olmalı.

**MultineLine / Single Line / Password :**Single Line seçeneği tek satırlık girişler için kullanılır. Multiline ise birden fazla satır girişine izin verir. Multineline seçildiğinde Word wrap aktif olur. Bu seçenek seçili ise bir satıra sığmayan karakterler bir alt satıra aktarılır. Password ise girilen değerin ekranda gözükmesini önler.

**Max Char :** Seçili alana en fazla kaç karakter girileceğini bu alandan belirtebiliriz. 0 değeri sonsuz girişe izin verir.
**
Embed Fonts :** TextField ile gömülecek karakterleri ayarlamamızı sağlar.
**
HTML :** Eğer bu alan seçili ise textfield içinde HTML kodlarının aktif olacağını belitir . Böylece textfield içinde <a href>, <b> gibi HTML kodlar kullanılabilir.

| **Butonları Hazırlama : **İki tane buton yapıyoruz . Biri gönder ve diğeri temizle butonu. Bu butonları formumuza yerleştiriyoruz. Gönder butonu için şu action kodları ekliyoruz : on (release) { loadVariablesNum ("http://www.server.com/MailGonder.asp", 0, "POST"); } Bu action ile serverımızda bulunan MailGonder.asp isimli ASP dosyasına Flash içindeki Isim,Mail,WebSite ve Dusunceler değişkenlerini post ediyoruz. Temizle butonu için ise şu action'ları ekliyoruz. on (release) { Isim = ""; Mail = ""; WebSite = ""; Dusunceler = ""; } Temizle butonuna basıldığında tüm değişkenlerin değeri boşaltıldığından Input boxlara girilen tüm değerler silinecektir. |
| --- |

## FLASH İLE CHECKBOX KUTULARI OLUŞTURMA

**SWF Dosya**
"Bir onay kutusu nasıl yapılır?" sorusu çok sorulduğu için anlatılması gereken bir konu.Sizde Flash ile onay kutularını ve butonlarını kolaylıkla yapabilirsiniz.Onsuz bir interaktiv site olmaz.

**Düğmeleri Oluşturma**
Herhangi bir çeşit onay kutusu yada butonu oluşturmak için,iki karelik movie clip yapmamız gerek.Bunu yapmak için Insert> New Symbol tıklayın.Bir isim vererek Movie Clip Hareketi seçin.Şimdi Movie Clip düzenleme ekranı belirecek.Burada layer üzerinde iki boş keyframe ekleyin,movie cliplerin biri ilk framede diğeri ikinci framede olacak.Şimdi herbir karede durumu göstermek için bir buton oluşturun.Örnekte,ON butonu için yeşil,OFF butonu için kırmızı kullandım.Buton için grafik kullanmıyorum çünkü kullanışlılığı azalıyor.Buton ise mouse ile etkileşime geçiyor.

Butonu seçin ve Modify> Instance tıklayın.Actions sekmesine geçin,butona aşağıdaki actionları verin.
**
Birinci Kare:**
On (Release)
Go to and Play (2)
// on mouse click turn switch on
End On

**Ikinci Kare: **
On (Release)
Go to and Play (1)
// on mouse click turn switch off
End On

**Sonuç**
Şimdi movie'ye bazı şeyleri öğretmemiz lazım.Mesela her bir durumda durup butonun gerçek zamanlı doğal halini göstermsi için değeri "boxStatus" olarak ayarlamasını ve bir sonraki tıklama için beklemesini.Yeni bir layer oluşturun (Actionları Movie Clip timeline'ında tutması için)

Keyframe'I seçin ve Modify> Frame tıklayın.Sonra actions sekmesine geçin.Kullandığım actionlar bunlar:
**
Birinci Kare: **
Set Variable: "boxStatus" = "0"
Stop
**
Ikinci Kare: **
Set Variable: "boxStatus" = "1"
Stop

Movie'miz tamamen bitti.Şimdi tek yapmanız gereken şey yaptığımız Movie Clip'I sahneye taşımak ve projenizi geliştirmeye evam etmek.

TEXT DOSYASINDAN VERİ YÜKLEMEK

Flash 4 ilk elime geçtiği zaman, orasını burasını kurcalarken ilk farkettiğim değişikliklerden bir tanesi de , **Load Movie **eylem komutuna **Load Variables from File **eklenmiş olmasıydı. Nasıl çalıştığını anladığım zaman gözlerime inanamamıştım. SWF dosyalarını hiç bir Generatore gerek kalmadan dışarıdan bir tek dosyayı değiştirerek güncelleyebiliyordum artık !

Bu ders notunda, herhangi bir Text dosyasından veri alabilen SWF dosyaları oluşturmayı öğreneceğiz ! Bu sayede FLA dosyasını açmaya gerek kalmadan filimlerimizi güncelleştirebileceğiz !
**
Text Dosyasını hazırlayalım**
**
Load Variables into location **eylem komutu HTTP satır formatındaki verileri okuyabilir. Mesela, selam=deneme&test=345 gibi.

Bu yüzden notepad'i açın vetext.txt adında bir text dosyası yaratıp içine,

text=Bu Flashe aktarilmis herhangi bir yazidir.

ve dosyayı kaydedin.

**SWF Dosyasını Oluşturalım******

Flash'ı açın ve yeni bir film oluşturun.

İlk Frame'in **Properties'**ini açın ve **Load Movie** eylem komutunu ekleyin. Sağdaki menüden **Load variables into location**'ı seçin, **URL **kısmına ./text.txt yazın ve **Level** değerini 0 yapın. Bu işlem ile text.txt dosyasındaki metini ana filime aktarmış olduk.

3.Frame 2'ye boş bir **Keyframe **ekleyin.

4.Bu frame'in **Properties'**ini açın ve **Label** kısmına YUKLENIYOR yazın. Actions sekemsine tıklayın ve **If **komutu ekleyin. **Condition **ksımına text ne "" yazın. Sonra da **Goto** eylemi ekleyin ve TAMAM label'ına sahip frame gitmesini söyleyin.

5.Frame 3'e boş bir **Keyframe **ekleyin. Bu frame'in **Properties'**ini açın ve Acitons sekmesine tıklayarak **Goto and play** komutunu ekleyin. LOADING label'ına sahip keyframe gitmesini sağlayın.

6.Son olarak Frame 4'e de boş bir **Keyframe **ekleyin. Bu frame'in **Properties'**ini açın ve **Label **kısmına TAMAM yazın. Sonra da **Stop **eylemini ekleyin.

7.Artık herşey hazır, **Text Tool'**u seçin ve **Text Field **butonuna basın. Sahne içersinde istediğiniz bir yere, istediğiniz boyutlarda bir text filed çizin. Text Field'a sağ tıklayın ve **Properties**'i seçin. Variable olarak text yazın. *Draw Border and Background* seçeneğini iptal edin. *Word Wrap*, *MultiLine*, *Disable Editing* and *Disable Selection* seçeneklerini aktif hale getirin.

**Nasıl Çalışıyor ?**

İlk frame text dosyasından verileri yüklüyor. Sonraki iki frame de tüm veriler yuklenene kadar bekliyor. Bu örnek için aslında gerekli bişey değildi. Ancak uzun metinlerde bazı sorunlarla karşılaşmamanız için bu önlemi aldık. Son Frame ise alınan veriyi bir Text Fİeld içersinde gösteriyor.

**SES**

Flash 4'de ses kontrolü hiç kolay olmamıştı.Flash 5'de gelişmiş bir action script ile bu çok kolay hale geldi.Bu derste sesi kontrol etmenin ne kadar kolay olduğunu göreceğiz.

Bu ders 4 bölüm halinde.
· Sesi import etme
· Movie symbol'ü oluşturma
· Düğmeler oluşturma
· Action'ı ekleme

**Sesi import etme**
Flash'ın güncelleştirilmiş bu yeni versiyonunda wav dosyalarının haricinde mp3 dosyalarını da import edebilirsiniz.
Bir ses dosyası import etmek için File>Import tıklayın yada CTRL+R tuş kombinasyonunu kullanın.import etmek istediğiniz ses dosyasını seçin ve OK tıklayın.
Ses dosyasını movie'e import etmiş oldunuz.

**Movie Symbol'ü oluşturma**
Verilen fla dosyasında music ismi verilen bir movie symbol kullandım ve bunun içinde bir ses içeriyor.
Bir movie symbol oluşturmak için Insert>New Symbol tıklayın yada CTRL+F8 kısayolunu kullanın. Şimdi Symbol özellikleri diyalog kutusunu göreceksiniz.symbol için isim alanına bir isim girin ve symbol için uygulamak istediğiniz behaviour'u seçin.
Symbol'ü oluşturdukran sonra Lıbrary'i açın.(Windows/library yada CTRL+L) Burada symbol'ü göreceksiniz.(Örnekte music isimli bir symbol)
Şimdi scene'de symbol'ü yerleştirin ve istediğiniz bir isim verin.(Windows/Panel/Instance tıklayın)
Şimdi diyalog kutusunda movie clip için isim verin.

**Butonları Oluşturma**
Eğer buton oluşturmaya alışkın iseniz bu bölümü atlayabilirsiniz.
Insert > Symbol seçin.
Symbol için bir isim verin ve symbol özellikleri diyalog kutusunda butonları seçin.Şimdi Button symbol düzenleme alanını göreceksiniz.
Bu arada not edin movie'miz için 4 buton oluşturmamız gerek.

**Sesi Ayarlama**
Timeline'da şu scripti ekleyin.

music1=new Sound(music);
music1.setVolume(50);
music1=new Sound(music);

music1 ses için olan isim.

| music1.setvolume(50); Volume 50'ye ayarlı (Buna 0 ile 100 arasında değer verebilirsiniz.). |
| --- |

/** Volume'ü yükseltmek**
"+" volume'ü yükseltmek için kullanılır.Bu action script'i eklememiz lazım:

on (release) {
tellTarget ("/") {
vol = music1.getVolume();
}
music1.setVolume(music1.getVolume()+5);
if (music1.getVolume()>=100) {
;
music1.setVolume(100);
}
}

| **Sesi right-left aktarmak** Bu script de sesi sağdan sola aktarmak için. on (release) { tellTarget ("/") { pan = music1.getPan(); } music1.setPan(music1.getPan()-5); if (music1.getPan()<=-100) { ; music1.setPan(-100); } } Mouse ortaya çıkınca music1.setPan(music1.getPan()+5); sesi sağdan sola aktaracak |
| --- |

**Sesi left-right'a aktarmak**
Sesi soldan sağa çevirmek için:

on (release) {
tellTarget ("/") {
pan = music1.getPan();
}
music1.setPan(music1.getPan()+5);
if (music1.getPan()>=100) {
;
music1.setPan(100);
}
}

Mouse ortaya çıkınca
music1.setPan(music1.getPan()+5);
sesi soldan sağa aktaracak

Flash ile bir site yaptınız. Ziyaretçilerinize birde güzelinden loop diye çağrılan şirin müziklerden dinletmek istiyorsunuz. En fazla 8 - 10 saniye ( en azından böyle olması gerekir. Kimileri 45 - 30 saniyelik şeylere loop diyor, hayret vallaha! )süren bu müzik tekrar tekrar çalarak siteye canlılık verir.

İnat ya, bir ziyaretçi beğenmedi kapatmak istedi arkada zangur zungur çalan bu müziği. Durun hemen kızmayın ! Belki hoparlörleri çok kötüdür veya loop artık çekilmez bir hal almıştır. Mesela bizim sitede arkada sürekli çıın çıın şeklinde öten müzik çok eleştiri aldı. Biliyorum beyninizi tırmalıyor, açma kapama tuşu koymadık bir türlü ! Bakın daha iyi işte.. koymuyoruz, size nasıl yapılacağını öğretiyoruz !

Bu ders notuna devam edebilmek için **Action Script kodlarının **nasıl girildiğini, düğmelerin nasıl yapıldığını bilmeniz ve en azından Tell Taget komutu hakkında bilgi sahibi olmanız gerekmektedir.

Yeni bir film dosyası açın. **Insert \* New Symbol **seçin. Loop adını verin ve **Movie Clip **seçeneğini seçin.

Timeline kısmındaki ilk key frame'e çift tıklayın ve açılan menüde **Actions **kısmına **Stop** komutunu ekleyin.

İkinci frame'e tıklayıp **F6 **ya basın ve keyframe ekleyin. Şimdi **File \* Import **seçin. Import etmek istediğiniz **.wav **uzantılı ses dosyasını seçin ve import edin. Bu dosyanın bir loop dosyası olduğuna emin olun. Yani ardarda çalındığında sürekli devam eden bir müzikmiş gibi duyulması gerekiyor. Bu gibi ses dosyaları internette çok sayıda mevcut. Nerelerden bulacağınıza gelince, bizim linkler sayfasında çok sayıda site var.

CTRL+L ye basın ve **Library** nizin açılmasını sağlayın. Listedeki ses dosyasını film alanına sürükleyin. Bu işlemi yaparken 2.frame de olduğunuzdan emin olun.

Keyframe'e çift tıklayın ve açılan menüden **Sound **sekmesine tıklayın. **Loops **yerine 999 değerini yazın. (1000 yazında Flashın sapıttığından bahsediyorlar. )

6.

Şimdi **Edit \* Edit Moive **seçerek film alanına gelin. Açık olan Library'den loop isimli sembolü film alanına sürükleyin. Beliren + şekline çift tıklayarak bu loop adındaki sembolün **Instance Properties**'ine ulaşın. **Instance Name** yerine loop yazın. Ok diyip çıkın.

Bir düğme yapın. Düğmenin **Acitons** kısmına geline ve şu kodları girin :

On (Release)
If (a=1)
Begin Tell Target ("/loop")
Stop All Sounds
Go to and Stop (1)
End Tell Target
Set Variable: "a" = "0"
Else
Begin Tell Target ("/loop")
Go to and Play (2)
End Tell Target
Set Variable: "a" = "1"
End If
End On

**İşin mantığına gelince:**

Bir **Movie Clip **dosyamız var ve ilk frame'de müzik yok. İkinci frame'de ise 999 kere tekrar edecek bir animasyon var. ( 999 kere dinleyecek kadar sitenizde birisi kalmışsa helal olsun size )

Bir de düğme yaptık durup dururken. Bu düğmeye dedik ki :

1- a denen değişkenin değeri 1 ise "loop" adındaki filme git. Tüm sesleri durdur, ayrıca bu filmin 1. karesine git dur. Bunun yanında a değerini 0 yap dedik. Böylece bir daha tuşa bastığımızda a değeri 1 değilde 0 olacak.

2- Yok eğer a değeri 0 ise "loop" adındaki filme git ve 2. karesini oynat. 2.karede ne var ? 999 kere çalacak bir müzik ! Ayrıca bununla da yetinme a nın değerini 1 yap ki bu tuşa bir daha bastığımda değeri 0 değilde 1 olsun.

**Ses Kaydedici**
İlk önce Ses Kaydediciyi açın.(**Start>Programs>Accessories>Entertaiinment>Sond Recorder**)

Eğer ses kaydediciniz yoksa COOL edıt gibi bir program da kullanabilirsiniz.

**Sesi kaydetme
**Kaydetmek istediğiniz sesi bulun.Sesi çalmaya başlayın ve hemen ses kaydedici ekranına gidip kırmızı düğmeye basın.Sadece 7 saniye kaydetmenizi öneririm.Şimdi de DURDUR düğmesine basın ve **FILE>Save AS** tıklayın.İstediğiniz br yere kaydedin.
Wav dosyanızı kaydettikten sonra Ses kaydediciye geri dönün.**FILE >NEW** tıklayın. Tekrar **FILE > OPEN** tıklayın.Sonra wav dosyasını bulun ve tıklayın.
Properties menüsüne gidin.(Fıle>Properties) Bir form çıkacak ekrana.ALL FORMATS seçip **Convert Now**'a tıklayın.Yeni bir form çıkacak.Formatı **GSM 6.10 **seçin ve OK'e tıklayın.Bu dosyanın boyutunu küçültecek.Diğer formatları da kullanabilirsiniz.**FILE >Save As** tıklayın ve aynı yere kaydedin.

**Flash'a import etme**
Flash'ı açın, Yeni bir keyframe oluşturun sesi eklemek için. **CTRL+R **basın ve kaydettiğiniz sesi bulup açın. Flash ekranına geri dönünce **Windows >Library **seçin.Sesi tutup Scene'ye bırakın.Böylece ses Flash movie'mize eklenmiş oldu.

**"BASIC ACTIONS"**

Adında da anlaşılacağı gibi hemen hemen her Flash Movie'de kullanılan basit seviye action'lar bu kategoride bulunur.

**
Go To : **Bu action ile, aktif scene ve aktif frame'den, belirtilen scene'deki , frame numarasına ya da daha önce label(etiket)'ı tanımlanmış frame'e yönlendirebilirsiniz. "Go To" action'ı ile kullanabileceğiniz paramatreler şunlardır.

Scene : Scene'nin ne olduğunu biliyorsunuz sanırım. Bir movie'de isteğinize göre birden fazla scene(sahne) bulunabilir. Ve "Go To" action'ın scene parametresi ile istediğiniz scene seçimini buradan yapabilirsiniz. Buraya tıkladığınızda açılan listede nextScene(sonraki sahne), previousScene(önceki sahne) ve varolan scene'lerinizin listesi çıkar. nextScene ya da previousScene seçeneklerini seçmeniz durumunda frame numarası ya da etiketi belirtemezsiniz. Bunlardan birini seçmeniz durumunda previousScene için önceki , nextScene için sonraki scene'nin ilk frame'ine gider. Eğer bir seçenek belirtmezsek geçerli değer, o anda içinde bulunduğumuz scene(current scene)'dir.
Type :** **Frame alanında verilen frame bilgisinin türünü buradan belirleyebilirsiniz. Bu parametre ile 5 seçenek mevcuttur.
Frame Number :** **Frame alanında verilen frame bilgisinin frame numarası olduğunu belirtir. Timeline aracılığı ile frame numarasını alabilirsiniz.
Frame Label **:** Label verdiğiniz bir frame'e yönlendirme istiyorsanız , bu seçeneği seçmeniz gerek. Bir frame'e nasıl label verilecegini ve label'ın faydalarına değinelim. "Go To" action'ını kullanırken frame numarası yerine frame label vermek daha avantajlıdır. Mesela 200 frame'lik movie'miz de "Go To" action'ı için frame number kullandıysak ve ileride bu frame'ler arasına yeni bir frame eklemek gerekirse , tüm "Go To" action'larımızı yeniden düzenlememiz gerekir ki , Çin işkencesini aratmayacak bir durumla karşı karşıya kalırız.O halde ne yapıyoruz, "Go To" action'ını çok fazla kullanıyorsak veya frame sayımız yüksekse frame label kullanıyoruz. Bir frame'e label vermek için ise Window > Panels altında bulunan Frame'e(CTRL+F) tıklıyoruz. Açılan pencede label alanına yazdığımız değer, seçili keyframe'in label değeri oluyor. Zaten label'ı girip enter'a bastıktan sonra , label verdiğimiz keyframe'de kırmızı bir bayrak görüntüsü ve verdiğimiz label'ın değeri gözükecektir.
Expression : Bu seçeneğe ileride değineceğiz. Ama kısaca bilginiz olması açısından, frame alanındaki değerin bir değişken , ifade yani kısaca başka bir fonksiyon yada matematiksel ifadeden dönen sonuç olduğunu belirtir.
Next Frame : Aktif frame'den, bir sonraki frame'e gitmemizi sağlar. Bu seçenek seçildiğinde bir ipte iki canbaz oynayamayacağı için, doğal olarak "Frame" alanı deaktif olur.
Previous Frame : Aktif frame'den bir önceki frame'e gitmemizi sağlar.Yine nextFrame'de olduğu gibi bu seçenek de seçildiğinde "Frame" alanı deaktif olur.
Frame : Yukarıda anlattığımız "Type" bilgisine göre bu alana frame numarası, frame label, expression türünden bir değer girilir.
Altta bulunan, "Go to and Play" seçeneği ile, belirtilen scene' deki, frame 'e gittikten sonra animasyonun devam edip edilmeyeceği içindir. Yanında bulunan kutu işaretli ise belirtilen frame'e gittikten sonra , o frame'den sonra oynamaya(play) devam eder, kutu işaretli değil ise belirtilen frame'e gittikten sonra bekler(stop).Eğer kutudaki işaret kaldırılırsa "gotoAndPlay" şeklinde gözüken action "gotoAndStop" şeklini alır.
Bir örnek vermek gerekirse, Scene2'deki 15. frame'e gitmek istersek :
gotoAndPlay ("Scene 2", 15); gibi bir action yazmamız gerekir.

/
**Play :** Şimdi bu action'ın neyini anlatacaksın dediğinizi duyar gibiyim. Her teypde bir tane var, basıyoruz kaset kaldığı yerden devam ediyor işte!.. Haklısınız, bu action'da her teypde bulunan "Play" tuşuyla aynı işleve sahiptir. Bu action komut kullanıldığında, animasyonbulunduğu frame'den itibaren oynamaya devam eder. Hiç bir parametresi yoktur.

**Stop : **Gene, "Play" action'ında oldğu gibi gürültü patırtı çıkartmayın. Ben görevimi yapıyorum ve anlatıyorum. Bu action'ın verildiği keyframe'de animasyon durdurulur.Hiç bir parametresi yoktur.

**Toggle High Quality : **Bu action komut ile Flash movie'nizin kalitesini ayarlarlayabilirsiniz. Ve her kullanıldığında , bir önceki değere göre kalite düşük veya yüksek olur. Hiç bir paramteresi yoktur.
**
Stop All Sounds :** Movie'nizde çalan bütün sesleri durdurmaya yarar. Hiç bir parametresi yoktur.

**Get URL : **Flash içinden, herhangi bir Web sitesine ya da bir Web sayfasına link vermek veya Flash içindeki değişkenleri Web sayfasına göndermek için kullanılır. Bu action ile kullanabileceğiniz parametreler aşağıdaki gibidir.
URL : Buraya, yönlendireceğiniz Web sitesinin ya da Web sayfasının adresini girebilirsiniz.Eğer bir URL giriyorsanız "http://" ifadelerini girmeniz şart. Aksi halde, girdiğiniz URL sizin sitenizin altında bir sayfa/dizin gibi aranır ve dolaysıyla ulaşılamaz.

Window : Bu parametre ile, "URL" alanına girdiğimiz adresin hangi tarayıcı penceresinde açılacağını belirleriz. Hiç bir değer girilmezse geçerli değer "\_self" seçeneğidir.

\_self : Bu seçenek ile, "URL" alanında belirtilen adres ,movie'nin bulunduğu pencere içinde açılır. Eğer HTML belgede frame varsa , verilen URL , movie'nin bulunduğu frame içinde açlır.
\_blank : "URL" alanında girilen adres, yeni bir tarayıcı penceresinde açılır,
parent : HTML belgede, Flash movie'nin bulunduğu frameset'i kaldırır ve URL alanında verilen adresi yükler. Eğer frameset kullanılmamışsa "\_top" seçeneği ile aynı işlevi görür.

\_top : Eğer HTML frame kullandıysanız, bu seçenek ile, aynı tarayıcı penceresi içinde, tüm HTML frame'ler kaldırılır ve "URL" alanına girilen adres aynı penrece içinde açılır.
Yukarıdaki "Window" seçeneklerine ek olarak, kendimizin tanımladığı bir tarayıcı penceresinede girilen URL'yi yönlendirebiliriz.HTML frame'lerden oluşmuş bir Web sayfası gibi.

Variables : URL alanında belirttiğimiz Web sayfasına , Flash içindeki değişkenlerin gönderilip gönderilmeyeceğini, eğer gönderiyorsak , gönderme için kullanacağımız metodu belirlememizi sağlar.
Don't Send(Gönderme) : Flash içinde bulunan hiç bir değişkeni URL ile birlikte, belirtilen adrese göndermez.
Send Using GET(GET metodu ile gönder) : Bu metod ile, Flash içinde kullanılan değişkenler, URL sonuna eklenerek gönderilir.Girilen URL'den sonra "?" karakteri , daha sonra değişkenler ve değerleri yer alır. Gönderilen her değişken "&" karakteri ile birbirinden ayrılır.
Send Using POST(POST metodu ile gönder) : Bu yöntem ile Flash içinde kullanılan değişkenler HTTP Header'lar ile birlikte gönderilir. Yani kullanıcı değişkenleri GET metodunda olduğu gibi göremez.Eğer değişkenleriniz çok veya değerleri uzun ise , kullanıcı adı ve şifre gibi bilgileri Flash formunuzdan gönderiyorsanız bu metodu tercih etmelisiniz.

Bir yanlış anlamayı ortadan kaldırmak için hemen belirteyim ki, Flash ile ziyaretçi defteri, anket, mail formları gibi tam Flash uygulamalar yukarıda bahsettiğimiz "Get URL" ile yapılmaz.Bu action ile Flash'da bulunan değişkenler "Window" parametresinde açılmak üzere verilen URL'ye, yönlendirilir. Tam Flash uygulamalar için, "Load Variables" action'ı kullanılır ve bu action'ı önümüzdeki aylarda öğreneceğiz.
"Get URL" action'ı ile bir mail adresine link vermek istersek "URL" parametresine, "mailto:" ifadesinden sonra E-Mail adresimizi girebiliriz."mailto:" kullanıldığında diğer parameterlerin bir önemi kalmaz. Eğer HTML belgemizin içindeki bir JavaScript fonksiyonunu çağırmak istiyorsak, "JavaScript:" ifadesinden sonra fonksiyonumuzun adını yazabiliriz. "JavaScript:" ifadesini kullanırsanız dikkat etmeniz gereken nokta; "Window" parametresidir. Zira Flash verilen "Window" isminde JavaScript' i calıştırır.Genelde, JavaScript'imizde aynı HTML belgede olduğuna göre "\_self" seçeneği kullanılmalıdır.
"Window " ve "URL" parametrelerinin yanlarında bulunan "Expression" kutucuklarını ilerleyen derslerde öğreneceğiz. Şimdilik en iyisi bunlara dokunmayın.Yok eğer dokunursanızda, evin önünde bir ambulans bekletin.Zira hata ararken sinir krizleri geçirebilirsiniz.

**FS Command : **Bu action ile StandAlone Player(Flash Player) için kullanabileceğimiz komutların yanı sıra, Flash movie'mizin HTML belge içinde bulunan JavaScript fonksiyonlarıyla haberleşmesini sağlayabiliriz.JavaScript kısmını daha başlangıç seviyesinde olduğumuz için bir kenara bırakalım ve StandAlone Player komutlarını inceleyelim. Ne de olsa hepiniz player ile movie'nizin nasıl tam ekran yapılacağını merak ediyorsunuz.Aşağıda açıklayacağımız komutları "Command" parametresine girebileceğiniz gibi, "Commands for standalone player" parametresinden de bu komutları listeleyebilirsiniz.

fullscreen : StandAlone Player ile açılan movie'nin kendi boyutlarında veya tam ekran olup olmayacağını belirler."Arguments" parametresine "true" verilmesi ile tam ekran , "false" verilmesi durumunda ise movie orjinal boyutlarına döner.
allowscale :StandAlone Player'ın boyutunun değiştirilmesi halinde oynayan movie'nin player'ın boyutlarına göre değişip değişmeyeceğini bu komut ile ayarlayabiliriz."Argumets" değerinin "true" olması durumunda Player'ın boyutu ile orantılı olarak movie'ninde boyutu değişir."Arguments" değerinin "false" olması durumunda ise Player'ın boyutuna bakılmaksızın movie orjinal boyutlarında kalır ve boyutu değişmez.
showmenu : StandAlone Player'da izlenen movie'ye sağ tıklanılması durumunda açılan menünün ve yukarıda bulunan "File, View, Control, Help" menüsünün gösterilip gösterilmeyeceğini belirler."Arguments" parametresinin "true" olması durumunda movie'ye sağ tıklanıldığında zoom ayarları, kalite ayarları ve kontroller menüsü ile yukarıdaki menüler gösterilir, "false" olması durumunda ise bu menüler gösterilmez.
trapallkeys : Bu komut ile, flash movie'niz için klavye tuşlarının aktif olup olmayacağını ayarlayabilirsiniz.
exec: StandAlonePlayer'da, movie'nin bulunduğu dizinde olmak şartıyla, "Arguments" alanına girilen programı çalıştırılı.
quit : StandAlone Player'ı kapatır.

Bir kere daha belirtmekte fayda görüyorum.Bu komutlar sadece StandAlone Player içindir.Yani HTML belge içine embed edilen movie için "fullscreen" komutunu verip neden tam ekran olmuyor diye bunalıma girmeyin.

**Load Movie **: Aktif movie'nizin içine, dışarıdan bir movie yüklemek için kullanılır. Bu action ile HTML belgenin yeniden yüklenmesine gerek kalmadan herhangi bir SWF dosyasını yükleyebiliriz.

**URL :** Yüklenilecek SWF dosyanın adresi buradan verilir.
Location : Burada bulunan listede iki seçenek mevcuttur. "Level" ve "Target".
Level(Seviye) : Level, kullandığımız Layer'lar gibi birer katmandır. Her Level "\_level" ifadesinden sonra kullanılan bir rakamla belirlenir.Bir movie içinde sonsuz Level olabilir. Hazırladığımız movie, "\_level0" da bulunur. Dolayısıyla "Load Movie" action'ı ile "\_level0" a bir SWF yüklersek ana movie'miz yerine yüklediğimiz SWF gösterilir. "\_level1" gibi farklı Level'lara SWF yüklediğimizde "\_level0" da bulunan movie üstüne yüklenir.Tabi yüklediğimiz SWF içindeki değişkenlerde yüklenilen "\_level" a ait olur."Level" a yüklediğimiz bir SWF 'nin özelliklerini ayarlamayı ilerleyen derslerimizde öğreneceğiz.Sonuç olarak SWF dosyasını bir "\_level"a yükelemek istersek "Level" seçeneğini seçer ve karşısındaki alana "\_level" değerini sayı olarak gireriz.
Target(Hedef) : İşte Action paneli anlatırken es geçtiğimiz meşhur target. Flash'da target, bir Movie Clip'e verilen "Instance Name" adı ya da yukarıda bahsettiğimiz "\_level" dır.Bir Movie Clip'e "Instance Name" verebilmek için Window>Panels menüsünden(CTRL+I) "Instance" penceresini açmanız gerekir. "Instance Name" vereceğiniz Movie Clip'i seçtikten sonra, Name alanına vereceğiniz ismi girebilirsiniz.Bu ismi gerekli action'larda target alanında kullanacağız. Elbette, çalışma alanında bulunmayan ve seçili olmayan bir Movie Clip'e "Instance Name" veremeyiz.
Eğer bir SWF dosyasını bir Movie Clip içine yüklemek istiyorsak target seçeneğini seçerek, Movie Clip'e verdiğimiz "Instance Name"i karşısında bulunan alana gireriz. Eğer target alanında belirttiğimiz "Instance Name"e sahip bir Movie Clip yok ise yüklemeye calıştığınız SWF dosya gözükmez. Niye gözükmüyor diye, saçınızı başınızı yolmadan önce target'ın, verdiğiniz "Instance Name" ile aynı olup olmadığını kontrol edin.
Variables : Bu parametre ile yükleyeceğimiz SWF dosyasına değişken(ler) gönderilip gönderilmeyeceğini, eğer gönderiyorsak ,gönderme için kullanacağımız metodu belirlememizi sağlar. "Get URL" action'ında "Variables" parametresinde bahsettiğimiz işleve sahiptir.Bu parametre, aslında interaktif animasyonlar ve uygulamalar hazırlamak için kullanacağımız en önemli parametrelerden.

**Unload Movie : **"Load Movie" action'ı ile, belirtilen "\_level" ya da target'a daha önce yüklenen movie'yi kaldırır.Hiç bir paramteresi yoktur.
**
Tell Target : **"Instance Name" verilmiş bir Movie Clip'i çağırmak için kullanılır."Tell Target" ile daha önce "Instance Name" verdiğimiz bir Movie Clip'i, target alanına Movie Clip'in "Instance Name"ini yazmak şartıyla çağırabiliriz. Çağırıpta ne yapacağız Movie Clip'i, dertsiz başımıza dert almayalım demeyin. Çağırıdıktan sonra action kodlar ile bu Movie Clip'i kontrol edebiliriz.

**Genel Kullanımı :**
tellTarget ("Hedef") {
Yapılacak İşler;
}

bir örnek vermek gerekirse , "test" "Instance Name"ine sahip bir Movie Clip'i çağıralım ve 6.frame'ine gidelim.

tellTarget ("text") {
gotoAndPlay (6);
}

Görüldüğü gibi "tellTarget" ifadesinden sonra parantez ve tırnak içinde hedef olarak verdiğimiz Movie Clip'in "Instance Name"ini ve süslü parantezler içinde de çağırdğımız Movie Clip için "Go To" action'ını kullandık. Süslü parantez, tırnak ve parantez gibi karakterlerin ne amlama geldiğine önümüzdeki ay değineceğiz.

**If Frame Is Loaded : **Bu action ile belirtilen Scene'deki belirtilen frame yüklendiğinde istenilen action'ların çalıştırılması sağlanır. Flash movie'niz için önyükleme bu action ile yapılır.

**Secene : **"curent scene" ile içinde bulunduğunuz scene seçilebilir ya da buraya tıkladığınızda açılan listeden kullandığınız scene'lerden birini seçebilirsiniz.
**Type :** Frame number ile, "Frame" alanına girilen değerin frame numarası oluduğu, Frame Label ile "Frame" alanına girilen değerin frame etiketi olduğu ve son olarak da "Expression" ile "Frame" alanının bir değişken ya da script ifadesi olduğu belirtilir.
**Frame :** Yukarıdaki seçilen seçeneğe göre buraya frame numarası , frame etiketi ,bir değişken adı veya script ifadesi girilir.

Flash 5 ile önemini yitirmiş bir action' dır.

**On Mouse Event :** Bu action eğer bir buton seçili ise aktif hale gelir.Butona yapılacak eylemlerin türünü belirlememize olanak sağlar.Eylemler diyorum, çünkü burada birden fazla seçenek seçebiliriz.Verilen eylem(ler) gerçekleştiğinde "On Mouse Event" içindeki action'lar calıştırılır.Bir butona verebileceğimiz 8 değişik eylem bulunur.

Press : Butona tıklanması durumunda eylem gerçekleşmiş sayılır. Eylemin gerçekleşmesi için tıklandıktan sonra butonun serbest bırakılması gerekmez.
Release : Butona tıklanılıp, buton serbest kaldıktan sonra eylem gerçekleşmiş sayılır.
Release Outside :Butona tıklanılıp, buton alanından çıktıktan sonra serbest bırakılmasıyla eylem gerçekleşmiş sayılır.
Roll Over : Mouse işaretçisi butonun üstündeyken eylem gerçekleşmiş sayılır.Bir kere mouse işaretçisinin üstüne gelmesiyle action kodlar bir kere calıştırılır.
Roll Out : Mouse işaretçisi butonun üstüne getirilip, buton alanından dışarı çıktığında eylem gerçekleşmiş sayılır.
Drag Over : Butona tıklandıktan sonra, yine basılı durumda, mouse işaretçisinin buton alanından dışarı çıkıp , tekrar buton alanına girmesiyle eylem gerçekleşmiş sayılır.
Drag Out : Butona tıklandıktan sonra, yine basılı durumda, mouse işaretçisinin buton alanından çıkmasıyla eylem gerçekleşmiş sayılır.
Key Press : Bu seçenek seçildiğinde karşısındaki kutu aktif hale gelir.Buraya klavyede bulunan Fn (F1,…,F12), Print Screen, Scroll Lock, Pause, Ctrl, Alt, Shift, Caps Lock, Num Lock ve Windows tuşları hariç, herhangi bir tuş ismi girebilirsiniz. Sizin istediğiniz tuşa basmanız halinde tuş ismi bu kutuda yazacaktır. Oyun yaparken ya da butonlara kısayol vermek için bu seçenek ileride işimizi görecek.
**
Örnek : **
Klavyeden "P" karakterine basıldığında veya butona tıklanılıp, buton serbest kaldığında sayfamızı http://www.pcmagazine.com.tr adresine yönlendirelim.
on (release, keyPress "P") {
getURL ("http://www.pcmagazine.com.tr", "\_blank");
}

BAŞLANGIÇ SAYFASI YAPIMI

Bağlantı hızının oldukça düşük olduğu ülkemizde Flash animasyonlarını download ile eş zamanlı olarak seyretmek oldukça güç oluyor. Animasyonun ara ara takılması, tüm çalışmamızı alt üst ediyor.

Buna çözüm olarak animasyonunuzun başına bir Yükleniyor ibaresi koyabilir, asıl animasyon tam olarak yüklendiği anda animasyonu başlatabilirsiniz.

Çok değişik yollara başvurarak bu işlemi gerçekleştirebilirsiniz. Anlatacağım yöntemi ilk Flash kullandığım zamanlarda kendim bulmuştum. Hala daha ufak geliştirmeler yaparak aynı tekniği kullanmaktayım.

Yeni bir Scene yaratın. Bu Sceneyi **Başlangıç Scene**'si olarak ayarlamayı unutmayın. Bunun için **Window \* Inspectors \* Scene **menüsünü kullanın.

10. Frame e bir **Key Frame **ekleyin. ( **F6** )

İlk frame ile 10. frame arasında kısa bir animasyon yaratın. Yanıp sönen bir "Yükleniyor" yazısı olablir mesela...

11. Frame'e bir **Key Frame **ekleyin. ( **F6 **). **Timeline **kısmında şöyle bir görüntü elde etmiş olmalısınız:

11. Key Frame çift tıklayın yada sağ tıklayarak **Properties **i seçin. Açılan kutuda **Actions **sekmesine tıklayın. Üzerinde + yazan düğmeye tıklayarak **Go To **seçeneğini seçin. Sağ alt köşedeki **Control : Goto and Play **yazan kutuyu seçili hale getirin. **Scene **yazan açılır menüden de yüklenme animasyonu yaptığımız yani üzerinde çalıştığımız Sceneyi seçin. Benim çalışmamda Scene 1 olduğu için ben Scene1 i seçtim. Actions kutusunda şöyle bir görüntü elde etmiş olmalısınız

Şimdi asıl animasyonun olduğu Scene ye gidin. ( Sağ üst taraftaki iki düğmeden solda olan düğme ile Sceneler arası gezebilirsiniz. ) Animasyonunuz Scene 2 de olduğunu ve 200. framde son bulduğunu varsayalım. 200. **Key Frame**'e çift tıklayarak, **Label **sekmesine tıklayın ve bu keyframe bir ad verin.

Tekrar Yükleniyor animasyonunun olduğu Sceneye dönün. ( Biz Scene 1'e dönüyoruz.) 10. **Key Frame'**e çift tıklayın yada sağ tıklayarak **Properties**'i seçin. **Actions **sekmesine tıklayın. + yazan düğmeye basarak **If Frame is Loaded **seçeneğini seçin. Sağ tarafta **Scene **menüsünden Scene 2 yi (Asıl animasyonun olduğu Scene yani..) seçin. **Frame **menüsünden **Label'ı **seçin ve açılır menüden **Son Frame**'i seçin. ( 6. aşamada verdiğiniz isim.)

Tekrar + tuşuna basarak **Go To **seçin. Sağ alt kısımın **Go To and Play **olarak seçilmiş olduğuna dikkat edin. **Scene **açılır menüsünden **Scene 2 **yi seçin. Şu görüntüyü elde etmiş olmalısınız:

İşte oldu ! Hata yapmadan bu aşamaya kadar geldiyseniz artık bir loading scene sine sahipsiniz. Denemek istiyorsanız eğer, dosyayı publish ettikten sonra Flash'te .SWF dosyasını açın. Control menüsünden **Show Streaming i **seçin. Daha sonra bağlantı hızını aynı menüden istediğiniz gibi ayarlayabilirsiniz.

**Nasıl Çalışıyor ?

**İlk Scenede 10. Frame'e geldiği zaman Scene 2 nin son Frame'i yüklenmiş mi diye kontrol ediyoruz. Eğer yüklenmemişse hiç bir şey yapmadan yolumuza devam ediyoruz. Karşımıza çıkan 11. Frame bizi 1.Frame e tekrar geri yollluyor. Bu şekilde sürekli 10. Frame de kontrol yapıyoruz. 10. Frame'e geldiğimizde eğer Son Frame de yüklenmişse direk olarak Scene2 nin ilk Frame ine atlıyoruz ve animasyonumuz başlıyor.

---
*Kaynak: `FLASH NEDİR/FLASH NEDIR.doc` — xx — 2004*
