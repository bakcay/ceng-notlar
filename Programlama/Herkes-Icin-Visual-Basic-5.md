# Herkes İçin Visual Basic

## **Herkes İçin**

## **Visual Basic******

## 5***. Etiketler (Labels), Metin Kutuları (Text Boxes), Değişkenler (Variables)***

## ***Tekrar Gözden Geçirme ve Bir Önbakış***

Bu derste Visual Basic ortamını, bazı yeni kontrolleri ve birtakım yeni BASIC bildirilerini görmeye devam edeceğiz. Bu derslere devam ettikçe, Visual Basic projesini yapılandırmanın daima üç adımı olduğunu unutmayın:

(1) form üzerine kontrolleri yerleştirin (2) kontrollere özellikler atayın (3) ilgili olay prosedürlerini yazın. Bu derste, **projelerinizdeki hatalarınızı nasıl bulup, bu hataları nasıl temizleyeceğinizi, label(etiket), text box controls(metin kutusu kontrolleri) ve BASIC variables(değişkenlerini)** öğreneceksiniz. Yine bu derste saklamayı planladığınız şeyleri saklamanıza yardımcı olacak bir proje yapılandıracaksınız.

## Bir Visual Basic Projesinin Hatalarını Ayıklamak

Projenizi ne kadar iyi planlarsanız planlayın, kontroller ve olay prosedürleri içine fikirlerinizi yerleştirirken ne kadar dikkatli olursanız olun, hatalar yapacaksınız !

Hatalar veya bilgisayar programcılarının söylediği şekilde **bugs (hatalar) **projelerinize sessizce sızacaklardır. Bir programcı olarak bu **bugs(hatalar)**’ı bulmak ve ayıklamak için bir takım stratejilere ihtiyaç duyacaksınız. Bir proje içindeki hataları bulup ayıklama metotlarına **debugging **adı veriyoruz. Ne yazık ki, bir program içindeki hataları bulmak için çok sayıda güçlü ve hızlı kurallar bulunmamaktadır.

Her programcının hatalara karşı geliştirdiği kendisine has bir yolu bulunmaktadır. Siz de kendi yollarınızı geliştireceksiniz. Bu derste size ancak bazı genel strateji ve düşünceler sağlayacağız.

Proje **hataları (veya bugs),** üç tipte sınıflandırılabilir:

**Syntax** errors **(sözdizimi hataları)******

**Run-time** errors **( çalışma süresi hataları)******

**Logic** errors **(mantıksal hatalar)******

**Syntax** **errors(sözdizimi hataları),** dizayn(design) modunda bir özelliğin değerini düzenlerken veya bir BASIC kodu satırı yazarken oluşur. Bir şey bozuk veya yanlış yazılmış olabilir veya orada bulunması gereken bir şey orada bulunmamaktadır. Eğer sözdizimi hataları varsa, projeniz çalışmayacaktır. **Run-time errors** **(çalışma süresi hataları)** projenizi çalıştırmaya kalkıştığınızda oluşur. Çalışması birdenbire durur, çünkü kontrolü arkasında bir şeyler olmuştur. **Logic errors(mantıksal hatalar)**’ı** **bulmak oldukça zorlayıcıdır. Projeniz güzel çalışır, fakat verdiği sonuçlar beklediğinizden farklıdır.

Hadi her hata tipi üzerine alıştırma yapalım ve muhtemel debugging metotlarını tespit edelim.

## ***Syntax Errors(Söz Dizimi Hataları)***

**Söz Dizimi Hataları(Syntax Errors)** tanımlanması ve ayıklanması en kolay olan hatalardır. Visual Basic Program’ı, **syntax error**’ları bulmak için en büyük yardımcıdır. Syntax error, en çok kontrol özelliklerine değer düzenlerken veya olay prosedürleri için BASIC kodu yazarken ortaya çıkar.

Visual Basic’te yeni bir projeye başlayın. Proje penceresine gidin ve formun **Left** özellik değeri kısmına **yelkenli **kelimesini yazın. Ne oldu** **? Aşağıdaki gibi küçük bir pencere göreceksiniz (bu bir **VB4** penceresidir, diğerleri ise benzerdir):

On-line help için <**F1**> tuşuna basın ve problemin bir açıklamasını görün. Hatırlayın bu özellik değeri uygun tipte olmalıdır. Bir özelliğe uygun olmayan tipte bir atama yapmak bir **syntax** **error**’dur. Fakat, bakın Visual Basic bizim bu hatayı yapmamızı engelledi. **OK** tıklayın. **Left** değeri onu değiştirmek istediğinizden önceki durumuna dönecektir.

Kod yazarken eğer bir **syntax error** yaparsanız ne olur ? Deneyelim !

**Form\_Load** prosedürü için kod penceresini açalım. Başlık satırı altına, şu satırı yazın ve <**Enter**> tuşuna basın:

## **Form1.BackColor 0 vbRed**

Bir atama bildirisinde eğer **=** işareti yerine eğer yukarıdaki gibi **0** yazarsanız, aşağıdaki pencere görünür (yine bu bir **VB4** penceresidir):

## ***( Beklenen: Bildiri Sonu) ***

<**F1**> tuşuna basmak size bazı yardımlar sağlayacaktır. Visual Basic bu bildiride bir şey(ler)in yanlış olduğunun farkına vardı. Bunun ne olduğunu görebilmelisiniz.

Böylelikle eğer bir **syntax error** yaparsanız, Visual Basic genellikle yanlış bir şey yaptığınızın farkına varır ve hata yaptığınızın farkına varmanızı sağlar. **Syntax error**’larınızın ayıklanması için iyi bir kaynak **on-line help** sistemidir.

Şunu da belirtelim, **syntax error**’ler genellikle klavyeden hatalı yazı girilmesinden kaynaklanır. Bu ise klavyeden yazım becerinizi geliştirmeniz için diğer bir önemli nedendir.

## ***Run-Time Errors(Çalışma Süresi Hataları)***

Başarılı bir biçimde kontrol özelliklerini düzenleyip olay prosedürlerini yazınca ve bütün tanımlanan **syntax error**’lar da ayıklayınca, projenizi artık çalıştırmayı deneyeceksiniz. Eğer proje çalışırsa çok iyi ! Fakat pek çok kereler projeniz durup size bir hata bulduğunu söyleyebilir – bu bir **run-time error** **(Çalışma Süresi Hatası)**’dır. Neden durduğunu araştırıp problemi tespit etmeniz gerekmektedir. Yine, Visual Basic ve on-line help genellikle **run-time error**’ları ayıklamanız için yeterli bilgiyi sağlayacaktır.

Örneklere bakalım. Yukarıdaki aynı örnek ile çalışarak, **Form\_Load** prosedüründeki kod satırını aşağıdaki gibi değiştirin:

## **Form1.BackColor vbRed******

Buradaki örnekte formun background rengini düzenlerken **=** işaretini unutmuş gibi davranalım. Dikkat edin, Visual Basic size bu hatalı satırı yazmanız için izin verir. Visual Basic, dizayn modunda bütün syntax error’ları bulamaz. Projeyi çalıştırmayı deneyin (burada herhangibir dosyayı saklamanız gerekmiyor).

Araç çubuğu üzerinde bulunan **Start** buton’unu tıkladığınızda , aşağıdaki pencere görünmelidir (**VB4** sürümü gösterilmiştir):

## ***(Özelliğin Geçersiz Kullanımı)***

ve kod penceresinde bulunan **BackColor** kelimesi belirgin hale gelir. Visual Basic, bu belirli özelliği nasıl kullandığınız ile ilgili olarak size bir şeylerin yanlış olduğunu söylemektedir. Daha fazla bilgiye ihtiyaç duyarsanız <**F1**> tuşuna basın.

Visual Basic size hatalarınızı göstermesi açısından, yeteri kadar iyidir.

Varsayalım hatamızı bir **=** işareti koyarak düzelttik, fakat yanlışlıkla bu sefer de **BackColor** özellik ismi içindeki **k **harfini kaldırdık ve şu şekilde yazdık :

## **Form1.BacColor = vbRed******

Projeyi çalıştırmayı deneyin ve aşağıdaki pencereyi görün (**VB4** sürümü görünmektedir):

## ***(Metot veya veri elemanı bulunamadı)***

ve **BacColor** kelimesi belirgin hale gelir. Yardıma ihtiyacınız varsa <**F1**> tuşuna basın. Visual Basic size bu belirli kontrol için bu özelliği bulamadığını söylemektedir. Hatalı yazımı farkedip düzeltmeniz gerekmektedir.

Şimdi, özellik ismini düzeltin fakat bu sefer **Form1 **yazacağınız yere **For1 **yazın:

## **For1.BackColor = vbRed******

Projeyi çalıştırın. Yeni bir pencere ortaya çıkacaktır:

## ***(Run-time error ’424’***

## ***Nesne gerekiyor)*********

Bu mesaj penceresi diğerleri kadar faydalı değildir. <**F1**> tuşuna basmak veya **Help**’i tıklamak hatayı açıklayacak, fakat hatanın nerede olduğunu söylemeyecektir. Buradaki anahtar mesaj kelime ‘**Object required’(Nesne gerekiyor)**’dur. Bu genellikle BASIC kodu içinde bir kontrolün ismini atarken yanlış girilmesi sonucu ortaya çıkan mesajdır. Visual Basic birşeye **dot notation (nokta notasyon)** kullanarak bir özellik atamaya çalışıyor :

## ** ControlName.PropertyName = Value**

Fakat, verilen isimde bir kontrol bulamamaktadır (örneğimizde **For1** ). Hatanın nerede olduğunu nasıl bulabiliriz ? **Bir ipucu;** bu pencerede **Debug** **buton**’u tıklanarak bulunabilir. Visual Basic durduğu kod satırını işaretler. Deneyin ve kötü kod satırını, bir kutucuk içine alınmış şekilde görün.Hatalı yazılmış form ismini sizin bulup çıkarmanız gerekmektedir - Visual Basic bunu sizin için yapamaz. **Debug** buton’unu tıkladığınızda, Visual Basic diğer mümkün olan başka bir moda sıçrar – **break(ara ver)** modu ( **design** ve **run** modlarını gördünüz). ** Break mod’**dan** **ayrılmak ve** design mod**’a** **dönmek için, yani kodunuzu düzeltmek için, projeyi durdurmanız gerekmektedir.

Burada sebep olduğumuz hatalar run-time error’lar içinde en genel olan üç tanesidir: **hatalı yazım ve bunu bir isim özelliğine atamak, bir özellik ismini hatalı yazmak, veya bir atama bildiriminde bir şeyi eksik bırakmak**.

Başkalarıda vardır ve başka projeleri yapılandırmaya başladıkça bunların pek çoğu ile karşılaşacaksınız. Fakat gördünüz. Visual Basic hatanın nerede olduğunu tespit ederken genellikle iyidir ve **on-line help** daima bunları açıklamak için kullanılabilir durumdadır. **Run-time error’lar hakkında son bir şey; **Visual Basic bütün hataların hepsini bir kerede bulamaz. Karşı karşıya kaldığı** ilk run-time error’**da durur.

Siz bu hatayı giderseniz bile, daha başka hatalar da bulunabilir.

**Run-time error**’ları, yalnızca, teker teker düzeltebilirsiniz.

## ***Logic Errors(Mantıksal Hatalar)***

Mantıksal hatalar bulunması ve ayıklanması en zor hatalardır. Bu tip hatalar projenizi çalışmaktan alıkoymazlar fakat doğru olmayan ve beklenmedik sonuçlar veren hatalardır. Bu noktada yapabileceğiniz tek şey, eğer mantıksal hataların varlığından şüpheleniyorsanız, projenize iyice dalmak (ilk olarak olay prosedürleri) ve her şeyin kesin olarak istediğiniz şekilde kodlandığından emin olmaktır. Mantıksal hatalar bir zaman tüketme sanatıdır, bir bilim değildir. **Mantıksal hatalar (logic errors)** bulmanın belirli kuralları yoktur. Her programcı, mantıksal hatalarını arayıp bulmak için, kendi yolunu bulup geliştirmelidir.

Kullandığımız örnek üzerinde bir mantıksal hata; kırmızı olmasını beklediğiniz halde form background rengini maviye ayarlamaktır. Buradan kodlara gidip neden öyle olduğuna bakabilirsiniz. İstenilen **vbRed** sembolik sabit yerine **vbBlue** sembolik sabitinin kullanıldığını görebilirsiniz. Değişikliğin yapılması mantıksal hatayı giderir ve form kırmızı olur.

Ne yazık ki, mantıksal hataları ayıklamak bu örnekte olduğu kadar kolay değildir. Fakat bir yardım bulunmaktadır. Visual Basic, **debugger** adı verilen bir araca sahiptir ve mantıksal hataları tanımlamaya bu yolla yardımcı olur.

Debugger kullanarak (daha evvel gördüğümüz gibi **break** modunda çalışır), özellikleri yazıcıda bastırılabilir, kodlarınızı nerede ve ne zaman isterseniz durdurabilir ve projenizi satır-satır çalıştırabilirsiniz. Debugger’ın kullanımı, bir ileri seviye başlık olup bu derste anlatılmayacaktır. Eğer Visual Basic becerilerinizi arttırmak istiyorsanız, aynı zamanda debugger’ın nasıl kullanılacağını da öğrenmeniz gerekmektedir.

Şimdi Visual Basic ile ilgili becerilerimizi arttıralım. Yeni iki kontrole bakacağız:

**Label(etiket)** ve **text** **box(metin kutusu)**.

## Label(Etiket) Kontrolü

Bir **label(etiket),** kullanıcının direk kontrol edemeyeceği bilgiyi gösterir.

Bu genellikle diğer kontrollere başlıklar sağlamak üzere kullanılır. Veya , bazı bilgisayar işlemlerinin sonuçlarını göstermek üzere kullanılır. Label kontrolü araç kutusu içerisinden seçilir. Şu şekilde görünür:

** ****Araç Kutusunda : ** **Form Üzerinde (varsayılan **

** (default) özellikler) **:

## ***Özellikler***

Etiketler için birkaç faydalı özellik aşağıdaki gibidir:

**Özellik**** ****Açıklama**

**Name**** **label(etiket)’i tanımlamak üzere verilen **isim**. Etiket isimleri için kullanılan ve üç harften oluşan önek ** lbl’**dir.

**Caption**** **Metin (**string tipte**) ve etiket içinde görünür.

**Font** Caption metninin **stil, boyut ve tipini** düzenler.

**Alignment** Caption metninin sola yaslı, sağa yaslı veya ortada olmasını belirleyen özelliktir **(hizalama)****.******

**BackColor** Etiket’in **background(artalan)** rengini düzenler.

**ForeColor** Caption metninin rengini düzenler.

**BorderStyle** Label sınırlarının stilini(tipini) düzenler.

**Left** Formun sol kenarından, etiketin sol kenarına kadar olan uzaklık.

**Top** Formun üst noktasından etiketin üst noktasına kadar olan uzaklık.

**Width** Twip birimi ile etiketin **genişliği******

**Height** Twip birimi ile etiketin **yüksekliği******

**Visible** (run modunda) etiketin form üzerinde görünüp görünmemesini belirler

## ***Örnek***

Visual Basic’i çalıştırın. Yeni bir projeye başlayın. Form üzerine bir label koyun. İsterseniz bunu yeniden boyutlandırıp hareket ettirin. Caption özelliğini düzenleyin. Değişik fontları deneyin....................................

..................................

.......................

.............

.......

....

...

..

.

## **------------------------------------------------**

## **HERKES İÇİN VISUAL BASIC **

## **KİTABIMIZI SİPARİŞ EDEREK TÜM KİTABIN BÜTÜN SAYFALARINA SAHİP OLABİLİRSİNİZ.**

## **TEŞEKKÜRLER**

## **ARTER YAYINCILIK, MÜHENDİSLİK, DANIŞMANLIK******

## ------------------------------------------------------------------------------------------

## ** PAGE 12**

## *** ****** *****Herkes için ****VISUAL BASIC\_\_\_\_\_\_ **

## \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## *** ETİKETLER, METİN KUTULARI ve DEĞİŞKENLER ***** PAGE 12******

## PAGE 12 PAGE 7

---
*Kaynak: `HERKES İÇİN VISUAL BASIC/BOLUM-5.DOC` — M. ŞAKİR UNUTUR — 2001*
