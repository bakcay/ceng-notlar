# Herkes İçin Visual Basic

## **Herkes İçin**

## **Visual Basic******

## 3***. İlk Visual Basic Projeniz*********

## ***Tekrar Gözden Geçirme ve Bir Önbakış***

İlk iki derste **forms(formlar)**, **controls(kontroller)**, **properties(özellikler)**, ve **event** **procedures(olay prosedürler)‘**i öğrendiniz.

Bu derste, şimdiye kadar öğrendiğiniz bütün bu bilgileri, ilk basit** Visual Basic Projenizi** oluşturmak üzere kullanacaksınız. Yine bu derste, bir proje yapılandırmanın adımlarını, form üzerine kontrolleri nasıl yerleştireceğinizi, bu kontroller için properties(özellikler)‘i nasıl düzenleyeceğinizi ve kendi olay prosedürlerinizi nasıl yazacağınızı (biraz BASIC kullanarak) öğreneceksiniz.

## Bir Visual Basic Projesi Yapılandırılmanın Adımları

Bir **Visual Basic Projesinin yapılandırılmasında**, üç temel adım bulunmaktadır:

Form üzerine **control(kontrol)** ‘leri yerleştirin (veya çizin).

Bu **control(kontrol)**‘lere **properties(özellikler) **atayın (değerler verin).

Bu kontroller için, **event** **procedure(olay prosedür)**’ler yazın.

Visual Basic’de, bu adımların her birisi, **design(dizayn)** mod’unda yapılmaktadır. Tekrar hatırlatalım, Visual Basic’de **mode(mod),** ana pencerenin başlık çubuğu üzerinde köşeli parantez içinde görünür.

Visual Basic’i çalıştırın. Çalıştığında ortaya çıkması gereken formu bulun. Formu tıklayın. Aşağıdaki gibi görünmelidir:

Projemizi yapılandırmadan evvel, birkaç **‘Windows’** tekniğini gözden geçirelim. Kontroller kullanarak, iki şey yapmanız gerekmektedir: **(move)taşımak** ve **(resize)yeniden boyutlandırmak** (form’un kendisinin de bir kontrol olduğunu hatırlayın!).

VB4:

Bir **VB4** projesinde form’u taşımak için, sol fare tuşu ile başlık çubuğu alanını tıklayın. Sol fare tuşunu basılı tutarak, form’u istenen yere **taşıyın(move)** (veya **sürükleyin (drag)**). Fare’nin tuşunu, formu istediğiniz yere taşıdıktan sonra bırakın. Proje başladığında, form’un ekranda alacağı pozisyon (yerleşim) budur.

**VB4**’de bir form’u **yeniden boyutlandırma(resize)** için, **fare işaretcisini **form’un bir kenar veya köşesine getirin. Küçük bir **‘double-arrow’ (iki yönlü ok)** göründüğünde tıklayın ve bu kenar veya köşeyi **sürükleyerek(drag)** istenen büyüklüğe getirin.

VB5, VB6:

Eğer **VB5** veya **VB6 **kullanıyorsanız,** **formun kendisini hareket ettiremezsiniz-kendi penceresinde sabit bir pozisyondadır (yerleşimdedir). Bu durumda pencerenin yerleştirilmesi **Form** **Layout** **Window (Form Yerleşim Penceresi) **kullanılarak yapılır:

Eğer ekranda **Form** **Layout** **Window (Form Yerleşim Penceresi) **görünmüyorsa,** **ana menü’den önce **View** seçeneğini daha sonra da **Form** **Layout** **Window‘**u tıklayın.

Şimdi, ufak ekranda form’u tıklayın ve istediğiniz yerleşim pozisyonuna sürükleyin.

Bu, bilgisayarınızda, **VB5** veya **VB6** uygulamaları başladığında formun yerleşimini oluşturur.

Dikkat edin,** VB5** veya **VB6’**da,** **form’u yeniden boyutlandırmak için, form’un her kenarında ve her köşesinde **‘sizing handles’ ( ‘boyutlandırma tutamaçları’)** bulunmaktadır.

Eğer fare işaretçisini bu tutamaçlardan birisinin üzerine doğru hareket ettirirseniz, küçük bir ‘**double-arrow’ (‘iki yönlü ok’)** belirecektir. Bu noktada, istediğiniz kenar ya da köşeyi, istediğiniz boyuta çekmek üzere tıklayarak sürükleyebilirsiniz.

Form’u **taşımak** ve **yeniden boyutlandırmak** için alıştırmalar yapın.

Bu alıştırmalar, aynı zamanda form üzerine kontrolleri yerleştirmek istediğimizde de gerekli olacaktır.

## ***Control(Kontrol)’lerin Form Üzerine Yerleştirilmesi ***

Bir Visual Basic Projesinin yapılandırılmasındaki ilk adım, kontrollerin form üzerinde istenilen yerlere yerleştirilmesidir. Şimdi, bu noktada, projenizi yapılandırmanız için hangi kontrollerin gerekli olacağına karar vermeniz gerekmektedir.

Birçok kez, zaman tüketen bir çalışmadır. Size garanti ederim, kafanızdakini birçok kez değiştireceksiniz! Şimdilik, yalnızca, form üzerine kontrolleri nasıl koyacağımızın alıştırmalarını yapıyoruz.

Kontroller, Visual Basic’in **Toolbox** **(Araç Kutusu)**‘ndan seçilir.

**Bir form üzerine bir kontrol yerleştirmenin iki yolu vardır: **

**Toolbox Window (Araç Kutusu Penceresi)** içinden, istenen kontrolü **doble-click(çift-tıkla)**’yın. Kontrol **default(varsayılan)** boyutlarda oluşturulacak ve formun ortasına yerleştirilecektir.

İstediğiniz kontrol’ü, **Toolbox window **içinde tek sefer tıklayın. Şimdi, fare işaretçisini form üzerinde hareket ettirin. Dikkat edin, işaretçi bir (+) işaretine dönüştü. Kontrolünüzü nereye koymak istiyorsanız, bu işaret yani (+)’yı kontrolünüzün sol üst köşesi olacak şekilde yerleştirin. Sol fare tuşunu tıklayın ve basılı tutun. Şimdi fare işaretçisini istediğiniz kontrolün sağ alt köşesine gelecek şekilde sürükleyin. Dikdörtgen biçiminde bir dış hat ekrana gelecektir. Bu dikdörtgen şeklindeki dış hat, eğer sizin istediğiniz kontrolün boyutunu temsil ediyorsa fare tuşunu bırakın. Kontrol ortaya çıkacaktır.

Kontrol, bir kere form üzerinde yer alınca, oraya nasıl yerleştirdiğiniz fark etmez.

Yine yeniden boyutlandırır ve taşıyabilirsiniz. Bir kontrolü **move(taşımak) **için, kontrolü seçmek üzere fare sol tuşunu tıklayın (boyutlandırma tutamaçlarını yeniden ortaya çıkacaktır). Onu yeni yerleşim yerine sürükleyin ve fare tuşunu bırakın.

**Resize(yeniden boyutlandırma) **için sol fare tuşunu tıklayarak kontrolü seçin. Eğer fare işaretçisini bu boyutlandırma tutamaçlarından birisinin üstüne getirirseniz, küçük bir **‘double-arrow’ (iki yönlü ok)** görünecektir. Bu noktada, karşılık gelen kenar veya köşeyi tıklayıp sürüklerseniz, seçilen kenar veya köşeyi istenen yere kadar getirebilirsiniz.

## ***Örnek***

Visual Basic’in çalıştığından, ekranda bir form olduğu kadar, **Toolbox(Araç Kutusu)’ **nun da yerinde olduğundan emin olun (Eğer yerinde yoksa Ana Menü’de

önce **View** daha sonra **Toolbox** seçeneğini tıklayın. Araç kutusuna gidin ve

**command** **button(komut butonu) ** kontrolünü bulun. Aşağıdaki gibi görünecektir:

Kontrolü **çift-tıkla’**yın**(double-click).** Form’un ortasında, ekrana gelmelidir:

Dikkat edin, boyutlandırma tutamaçları, buton etrafındadır. Bu, onun **active(aktif)** kontrol olduğunu göstermektedir. Formu tıklayın. Bu tutamaçlar gözden kaybolacaktır. Bu ise butonun artık aktif kontrol olmadığını göstermektedir.

Komut butonununu tekrar aktif yapmak için yeniden tıklayın. Komut butonunu değişik yerlere taşıyın ve onu yeniden boyutlandırmayı deneyin.

Gerçek bir büyük buton, gerçek bir küçük buton, gerçek bir geniş buton ve gerçek bir kısa buton oluşturun. Komut butonunu form üzerinde değişik yerlere taşımayı deneyin.

İkinci bir yerleşim metodunu kullanarak, başka bir komut butonunu form üzerine koyalım. Tekrar geriye araç kutusuna gidin ve komut butonu kontrolüne tek tıklama yapın. İşaretciyi form üzerinde hareket ettirin. Bir (+) işareti göreceksiniz. İkinci metodu kullanarak, form üzerinde komut butonunu çizin: (+) işareti üst sol köşede iken fare sol tuşunu tıklayın ve istenen boyuta ulaşana kadar fare tuşunu basılı tutarak işareti sürükleyin. Fare tuşunu bırakın. Dikkat edin, hala siz bu ikinci komut butonunu taşıyabilir ve yeniden boyutlandırabilirsiniz.

Form üzerine kontrol yerleştirme ile ilgili bu iki yola da alışkın olmalısınız. Zamanla bir metodu diğer metottan daha kolay bulup, onu tercih eder hale geleceksiniz. Fakat daima, her ikisinin de nasıl kullanılması gerektiğini bilin. Bazı durumlarda; bu metotlardan yalnızca birisini kullanabileceksiniz. Kontrolleri form üzerine yerleştirme konusunda biraz zaman harcayın ve alıştırma yapın.

Etiketler, metin kutuları, seçenek butonları gibi diğer kontrolleri de kullanın. Form içinde bunları dolaştırın ve yeniden boyutlandırın.

Kontrollerinizi iyi sıralanmış gruplar halinde organize edin. Bu tecrübeler, Visual Basic projelerimizi yapılandırırken bize gerekecektir.

Bunlara ilaveten, form üzerinden bir kontrolü nasıl kaldırabileceğinizi de bilmeniz gerekmektedir. Kolay bir işlemdir! Kaldırmak istediğiniz kontrolü tıklayın, aktif kontrol haline gelecektir. Klavyeden **Del (delete-sil)** tuşuna basın. Kontrol kalkacaktır.

**Bir kontrolü silmeden önce, onu gerçekten silmek istediğinizden emin olun! **

## Control Properties(Kontrol Özellikleri)’ni Düzenlemek

## (Design Mode-Dizayn Mod’u)

İstediğiniz kontrolleri form üzerine yerleştirdiğinizde, bu sefer de bu kontrollere **properties(özellikler)** **atamak,** **(değerler vermek)** isteyeceksiniz. Hatırlayın! **Properties(özellikler),** bir kontrolün, form üzerinde nasıl görüneceğini belirler.

Özellikler, kontrolün boyutları,rengi, bir kontrolün “**ne söylediği**”, form üzerindeki pozisyonu gibi şeyleri oluştururlar.

Bir kontrolü form üzerine yerleştirdiğinizde, bu kontrol Visual Basic tarafından verilen birtakım değerler alır. Form üzerinde kontrolü yerleştirip boyutlandırdığınızda, özellikle geometrik özellikler (boyutlarını ve yerleşimini içine alacak şekilde) düzenlenir.

Fakat birçok kereler, Visual Basic tarafından verilen bu **varsayılan değerler** kabul edilebilir değildirler ve onları değiştirmek isteyeceksiniz. Bu **Properties** **Window(Özellikler Penceresi) **yolu ile yapılır.

Eğer bilgisayarınızda Visual Basic çalışmıyorsa, şimdi başlatın. Eğer çalışıyorsa, **File’ **ı daha sonra da **New** **Project** ‘i tıklayın (eğer halihazır form ve projenin kaydedilip edilmeyeceği sorulursa cevap **No(Hayır)**’dır).

**VB5** veya **VB6’ **da ise ne çeşit bir projeye başlayacağınız sorulur: **Standard EXE **olarak cevap verin. Ekranda boş bir form bulunmalıdır. **Properties** **Window** ‘u bulun (eğer yoksa <**F4**> ‘e basın):

VB4:

VB5, VB6:

Eğer **Categorized** seçili görülüyor ise, **Alphabetic** olanını seçin.

Hatırlayalım, **Properties Window**’un üzerinde **control** **list(kontrol listesi) ** bulunmaktadır. Bu ise bize, form üzerinde hangi kontrollerin bulunduğunu söylemektedir. Burada listede ise, yalnızca bir kontrol vardır ve bu da formun kendisidir.

## ***Haydi, form özelliklerinin bazılarına bakalım:***

İlkin, form ne büyüklükte ? Bütün kontroller dikdörtgen şekildedir ve dört özellik bu dikdörtgenin boyutlarını belirler. Özellikler listesini kaydırma çubuğu ile kaydırın ve **Height(yükseklik) **özelliğini bulun. Bu özellik formun yüksekliğidir ve **twip **adı verilen bir birim ile değer bulur.** **Bir **cm** içerisinde 567 twip bulunmaktadır. Yani yüksekliği (**Height)** 567 ‘ye bölerek, formun yüksekliğinin **cm** olarak ne kadar olduğunu hesaplayabilirsiniz. Benzer şekilde **Width(Genişlik)** özelliği, formun genişliğini twip birimi ile verir. Formun boyutlarını değiştirin ve buna bağlı olarak yükseklik ve genişlik değerlerinin nasıl değiştiğine dikkat edin.

**Left(Sol) **özelliği, formunuzun sol kenarının monitör ekranının sol kenarından ne kadar uzakta olduğunu söyler. **Top(üst)** özelliği, formunuzun üst kenarının monitör ekranının üst kenarından ne kadar aşağıda olduğunu söyler.

Formunuzu hareket ettirin ve bu özelliklerdeki değişmeleri izleyin (**VB5** ve

**VB6‘ **da ise** **formu, **Form Layout Window (Form Yerleşim Penceresi)** üstünde hareket ettirmelisiniz). Veya **Left** veya **Top** özelliklerini tıklayarak, buralara yeni değerler verebilirsiniz. Bundan sonra da formun ekran üzerinde nasıl hareket ettiğini izleyin. Böylece dört özellik**, Left, Top, Width, ve Height **formun bilgisayar üzerinde tümü ile yerleşim ve boyutlarını tanımlar.

Kaydırma çubuğu ile **BackColor(Arka Renk) **özelliği üzerine gelin. Burada gördüğünüz değer, formun **background(artalan)** renk değerini göstermektedir.

Bu özellik için listelenen değer muhtemelen **&H000000F&** ‘dir. Belki farkında değilsiniz, fakat bilgisayar dili ile bu **gri** bir renktir. İleri derslerde renkleri düzenlemenin diğer yollarını da inceleyeceğiz. BackColor özelliğini şimdi değiştirmek için, **BackColor **’u tıklayın ve daha sonra aşağı açılan liste okunu tıklayın (Eğer **VB5** veya **VB6** kullanıyorsanız, **Palette** **Tab**’ını tıklayın.) Çeşitli renklerin bulunduğu bir **renk paleti** ortaya çıkacaktır. Yeni bir renk seçin ve sonucunu izleyin.

Kaydırma çubuğunu **Caption(Başlık) **özelliği üzerine getirin. Bu özellik, formun **başlık çubuğu üzerinde ne yazısı** bulunduğunu belirler. **Caption(Başlık)**’ı tıklayın ve daha sonra özellik penceresinden bu satırın sağ tarafına bir şeyler yazın. Dikkat edin yeni **Caption(Başlık),** form’un başlık çubuğu üzerinde de görünmektedir.

Property(özellik)’lerin kontrollerini ayarlamak, işte budur !

İlkin kontrol listesinden ilgilendiğiniz kontrolü seçin. Daha sonra kaydırma çubuğu ile kaydırarak özellikler boyunca gezinin ve değiştirmek istediğiniz özelliği bulun. Bu özelliği tıklayın. Özellik yeni bir değer girilerek değiştirilebilir (geometrik değerleri veya başlık özelliği gibi) veya önceden tanımlanmış bir listeden seçim yaparak gerçekleştirilebilir

(renk değerleri gibi aşağı ok vasıtası ile açılan liste gibi).

## ***Örnek *********

Yeni bir Visual Basic Projesine başlayalım. Bir form görünecektir. İstenilen yerleşim ve boyutlara getirmek üzere, formu hareket ettirin ve yeniden boyutlandırın.

**Left**, **Top**, **Width **ve** Height** özelliklerini kontrol edin. **BackColor** özelliğini ayarlayın. **Caption** özelliğini ayarlayın. Form üzerine bir komut butonu koyun. Komut butonunu ölçülendirin ve yerleşimini ayarlayın.

Komut butonu özelliklerine bakalım. Özellikler penceresinin kontrol listesinden **command button**’u seçin. Form gibi komut butonu da dikdörtgendir. **Width** özelliği twip birimi ile genişlik değerini, **Height** özelliği ise twip birimi ile yükseklik değerini verir. Formlar dışındaki kontroller için **Left(Sol)** ve **Top(Üst) **özellikleri biraz farklıdır. Form olmayan bir kontrol için, **Left** değeri kontrolün sol kenarının, formun **(****ekranın değil****)** sol kenarına olan uzaklığını verir. Yani, twip birimi ile form üzerinde kontrol pozisyonunu verir. Benzer şekilde **Top** değeri, kontrolün üst kenarının pozisyonunun twip birimi ile formun **(****ekranın değil****)** form’un üst kenarına (form’un üst kenarı başlık çubuğunun alt tabanı olarak tanımlanır) olan uzaklığını verir.

Tek bir komut butonu için, bu özellikler aşağıdaki gibidir:

Komut butonu için diğer önemli bir özellik ise **Caption(Başlık)** özelliğidir.

Buton üzerinde görünen yazı **Caption**’dır. Bu yazı, bu buton tıklandığında ne olacağını ifade etmelidir. Komut butonunun **Caption** özelliğini değiştirin. Komut butonu için bir **BackColor** özelliği listelenmiş olsa bile, bu değiştirilemez.

Form üzerine birkaç tane daha komut butonu koyun. Bunları taşıyın ve yeniden boyutlandırın. Bunların Caption özelliklerini değiştirin.

**Properties Window(Özellikler Penceresi) **‘nde, bir kontrolden diğerine geçiş yapmasını öğrendik. Kontrol listesinden aşağı oku tıklayabilir ve listeden seçtiğimiz değeri alabiliriz. İstenilen bir kontrole, listelenen özellikler içerisinde, geçmenin **kısa(kestirme) **

**bir yolu,** form üzerindeki kontrolü basitçe tıklamak ve onu **active(aktif) ** kontrol yapmaktır. Komut butonlarından birisini tıklayın. Dikkat edin özellikler penceresindeki seçilmiş kontrol, bu seçtiğimiz yeni kontrole geçti. Başka bir butonu tıklayın, değişmeye dikkat edin. Formu tıklayın. Seçilen kontrol form oldu. Kendi Visual Basic projelerinizi hazırlarken, bu kestirme metodu; bir kontrolden diğerine kolayca geçişi, çok faydalı bulacaksınız !

## ***Kontrolleri İsimlendirme (İsim Verme) ***

Herhangi bir kontrol için en önemli özellik, onun **Name(İsim)’ **idir. Öneminden dolayı bu kısmı ayrıca ele alacağız. Bir kontrole isim verirken, iki parça bilgi tanımlamak isteyeceğiz: kontrol’ün **type(tip)’ **i ve kontrol’ün **purpose(amacı). ** Böyle isimlendirmeler programlama çalışmalarımızı çok daha kolaylaştıracaktır.

Visual Basic Programcı Topluluğunda kontrolleri isimlendirmek için bir kural geliştirilmiştir. Kontrol isminin üç harfi (**prefix – önek **olarak adlandırılır) kontrol tipini belirler. Bazı **önekler** aşağıdadır (daha fazlasını, ilerleyen dersler boyunca göreceğiz):

**Kontrol**** ****Prefix(Önek)******

Form **frm******

Command Button(Komut Butonu) **cmd******

Label(Etiket) **lbl******

Text Box (Metin Kutusu) **txt******

Check Box (Onay Kutusu) **chk******

Option Button (Seçenek Butonu) **opt**

Kontrol ismi önekinden sonra, kontrolün ne yaptığını belirten bir isim seçeriz

(bu; önekin sona erdiğini göstermek üzere, genellikle büyük harfle başlar). Komple bir kontrol ismi 40 karaktere kadar uzunluğa sahiptir. İsim bir harf ile başlamalıdır ( bu kullanılan önek dikkate alınarak yapılır) ve yalnızca büyük ya da küçük olmak üzere harfler, sayılar ve (\_) karakterlerini içerir. 40 karaktere kadar uzunlukta kontrol isimleri oluşturma hakkınız olsa bile, isimleri mümkün olduğunca, anlamlarını da kaybetmesine izin vermeden kısa tutun. Bu, sizi, klavyeden uzun uzun isim yazma zahmetinden kurtarır.

Size bir fikir vermek üzere, isimlerin nasıl seçileceği konusunda bazı örnek kontrol isimlerine göz atalım. Bu isimler, birinci ve ikinci derslerde baktığımız **Sample** projesinde kullanılan isimlerdir.

## ***Örnekler:***

***frmSample*** - Sample projesi için **form******

***cmdBeep ***– Bip(beep) sesi verdiren **komut butonu(Command button)******

***lblPick*** – Seçilen sayıyı gösteren **etiket(Label)******

***optBlue *** – **Background(artalan)** rengini maviye çeviren** Option button **

** (Seçenek Buton)**’u

***chkTop*** – Oyuncak top’u gösteren veya gizleyen **Onay Kutusu(Check box)**

Bunlar, size, kontrol isimlerinin nasıl seçileceği konusunda bir fikir vermelidir. Bir programcı olarak çalışmanızı çok daha kolay gerçekleştirmenizi sağlayacaktır.

## ***Run Mod’unda, Properties(Özellikler)’i Düzenlemek *********

Uygun kontrol isimleri kullanmanın önemini belirtmek için, Visual Basic’te ortak bir amaca bakalım. Bir Visual Basic Projesini geliştirme adımlarından birisinin Design(dizayn) mod’unda kontrol özelliklerini oluşturmak olduğunu gördük. Siz aynı zamanda, projeniz **run(çalışma) **mod’unda iken **properties(özellikler)**’ini değiştirebilir veya oluşturabilirsiniz. Örneğin, **Sample** projesinde, bir **option button(seçenek buton)**’una tıkladığınızda, formun **BackColor** özelliği değişecektir. **Run(çalışma)** modunda bir özelliği(property) değiştirmek için, bir satır BASIC kodu kullanmamız gerekmektedir. ( İlk BASIC satırını öğrenmek üzeresiniz !). Bu kod için **format (yapı -şekil)** aşağıdaki gibidir:

## **ControlName.PropertyName = PropertyValue******

Kontrolün ismi, bir nokta (küsurat-ondalık noktası gibi), değiştirdiğimiz özelliğin ismi, (özellikler penceresi içinde bulunur), bir eşittir işareti (bir atama işlemcisi olarak adlandırılır) ve yeni bir değer yazdık. Böylesi bir format **dot** **notation-Nokta Notasyon **olarak adlandırılır.

Sample Projesi Form’unun artalan rengini maviye dönüştüren kod:

## **frmSample.BackColor = vbBlue******

Dikkat edin, hiç BASIC bilmemenize rağmen, uygun isim kullanılması, bu kod satırını çok anlaşılabilir bir hale getirmiştir. Sample form’un **artalan(background)** rengini maviye ayarlanmasını söylemektedir.

## ***Olay Prosedürlerinde Kontrol İsimleri Nasıl Kullanılır***

Uygun kontrol ismi vermenin önemi bir kez daha event procedures ( olay prosedürleri) yazarken ortaya çıkar (diğer derslerde ele alınacaktır). Bir form üzerine bir kontrol koyduğunuzda, kontrol yapan olay prosedürlerinin tümü, projenize eklenecektir. Bu **event procedures(olay prosedürleri)**’ni, **code window (kod penceresi)**’nde göreceğiz. Bu olay prosedürleri için yapı:

## Başlık satırı : **Private Sub ControlName\_EventName()******

\[BASIC kodu buradan devam eder\]

Alt(taban) satırı : **End Sub******

Başlık satırının kontrol ismi kullandığına dikkat edin. Böylece, uygun isimlendirme ile bizler kolaylıkla her olay prosedürünü tanımlayabiliriz

Bir örnek olarak, yine **Sample** programını kullanarak, **optBlue** kontrolü için **Click** olay prosedürü:

## **Private Sub optBlue\_Click()**

## **frmSample.BackColor = vbBlue**

## **End Sub**

Fark etmemiz gereken şey, kullanıcının **optBlue** option buttonunu çalıştıracak kod budur.

Uygun isim verme, olay prosedürlerin çok kolaylıkla tanımlanmasını ve okunmasını sağlar. Yine, bu, sizin bir programcı olarak, işinizi çok daha kolay yapmanızı sağlar. Şimdi, ilk **event procedure(olay prosedür)**’ümüzü yazalım.

## Olay Prosedürü (Event Procedure) Yazmak

Bir Visual Basic Uygulaması yapılandırırken üçüncü adım, form üzerinde bulunan kontroller için **event procedures(olay prosedür)**’leri yazmaktır. Bir olay prosedürü yazmak için, **code window(kod penceresi)’**ni kullanırız.

Kod penceresini projenizde ekrana getirmek için gerekli yolları gözden geçirelim. Bu adım, gerçek ten BASIC kodları yazmamız gerektiğinde veya bilgisayar programlaması yaparken gerekmektedir. Şimdiye kadar pek BASIC öğrenmediniz fakat, olay prosedürlerini bulma ve kod yazmanın prosesini öğrendiniz.

Henüz şimdi belirttiğimiz gibi, bir form üzerine bir kontrol yerleştirdiğimizde bu kontrol ile ilintilendirilmiş(bağlantılanmış) olay prosedürleri, projenin bir parçası haline gelecek ve bunlara **code** **window(kod penceresi) **vasıtası ile ulaşılabilecektir.

Her kontrol birçok olay prosedürüne sahiptir. Her prosedür için BASIC kodu yazmak zorunda değilsiniz-**yalnızca bilgisayarın cevap(karşılık) vermesini istedikleriniz için** yazmalısınız. Bir kere bir olayın **‘kodlanması’** gerektiğine karar verirseniz, bu olay prosedüründe ne gerçekleşmesi gerektiğine karar verin ve bu isteklerinizi gerçek BASIC kod satırlarına çevirin. Daha evvel görüldüğü gibi, her olay prosedürü için **format(yapı-şekil) **aşağıdaki gibidir:

## Başlık Satırı : **Private Sub ControlName\_EventName()******

\[BASIC kodu buradan devam ediyor\]

Alt(taban) satırı: **End Sub******

‘**Private Sub’** kelimeleri , bunun bir **Subroutine** (prosedür için başka bir kelime) ve bunun yalnızca forma **Private(Özel) **olduğunu belirtmektedir (yalnızca bu form tarafından kullanılabilir – şimdilik bunun ne anlama geldiği konusunu dert etmeyin!).

BASIC kodu geliştirme, bir Visual Basic Uygulamasının yaratıcı kısmıdır ve aynı zamanda, nerede ihtiyaç duyarsanız çok kesin olmak zorundadır. Yanlış heceleme ve yazım, işaretlemelerdeki hatalar ve işlemcilerin yanlış veya eksik olması programınızı çalıştırılmaz hale getirir.

Bir bilgisayar programı yazmanın **kesinlik** gerektirdiğini göreceksiniz.

Olay prosedürleri yazmanın yöntemleri şunlardır:

Hangi olaylara bilgisayar tarafından karşılık verilmesi istediğinize karar verin.

Bu karşılığın ne olacağı konusunda karar verin.

Bu karşılığı BASIC koduna çevirin.

Kod penceresindeki olay prosedürünü bulun.

BASIC kodunu yazın.

Ve, bu en iyi şekilde örnekle anlatılacak bir yöntemdir:

## ***Örnek***

Eğer Visual Basic bilgisayarınızda çalışmıyorsa , çalıştırın ve yeni bir projeye başlayın.

Form üzerine tek bir komut butonu yerleştirin.

Formun **Name** **property(özelliğini)** **frmFirstCode **olarak verin.

**Caption** **property(özelliğini**) **My** **First** **Code(Benim İlk Kodum) **olarak verin.

Komut butonunun **Name** özelliğini **cmdBeep **olarak verin.

Komut butonunun **Caption** özelliğini **Beep! **Olarak verin.

Bu noktada , dizayn prosesinde, form’unuz şu şekilde görünmelidir:

Tek bir olay prosedürü yazmak istiyoruz - prosedür, komut butonunun **Click(tıklama)** olayına karşılık vermesini, bu butonu tıkladığımızda, bilgisayarın beep(bip) sesi vermesini istiyoruz.

Kod pencersini ekrana getirin ( <**F7**> ‘ye basmak yollardan birisidir):

VB4:

VB5, VB6:

Sizin kod pencereniz bu şekilde görünmeyebilir. Visual Basic ortamında

**full-module** adı verilen bir **display(görünme)** seçeneği vardır. Bu seçenekte; olay prosedürleri burada göründüğü gibi ayrı ayrı değil, biri diğerinin arkasından listelenmiştir.

Eğer Visual Basic **ortamınız(environment)** full-module view ’ de ise değiştirmeniz gerekmektedir, çünkü bu kitapta onu kullanmayacağız. Full-module view’den çıkmak için, **Tools’**ı ve daha sonra **Options’**u tıklayın. Çıkan pencerede **Editor’**ü tıklayın ve **Full-Module View** seçeneğinin yanındaki kutuda onay işareti bulunmadığından emin olun. Eğer varsa , kutuyu tıklayarak işareti kaldırın.

Eğer **cmdBeep** nesnesi, **Object(Nesne) **listesinde görünmüyorsa, bu listede bulunan aşağı ok ile açılan listeyi tıklayın ve **cmdBeep** (komut buton)’unu seçin.

Kod penceresi şimdi aşağıdaki gibi görünmelidir:

VB4:

VB5, VB6:

Dikkat edin, **cmdBeep** buton’u için **Click** prosedürü şimdi ekrana geldi. Birçok kereler istediğiniz prosedürü bulmak için **Procedures** listesini kullanacaksınız-bu sefer yalnızca bir tanesi ekrana geldi (prosedürler alfabetik olarak listelenmiştir). Burası bizim bilgisayara **‘bip’** sesi verdireceğimiz kodları yazacağımız yerdir.

Kod penceresi bir kelime işlemcisi gibi davranır. Pencere içine metin yazılabilir, pek çok normal düzenleme özellikleri kullanabilir. Örnek kes, yapıştır, kopyala, bul ve değiştir gibi. Daha tecrübeli bir programcı olmaya başladığınızda, kod penceresini kullanırken daha rahat olacaksınız. Başlık ve dip satırları arasındaki alanı tıklayın.

Tek bir satır yazın:

## ** Beep**

Bu bir BASIC talimatı olup, bilgisayara** bip** sesi vermesini söylemektedir.

Şimdi ilk BASIC kod satırını yazmış bulunuyorsunuz !

Projeniz şimdi artık çalıştırılmaya hazırdır**(run).** Projeyi **Run(çalıştır)’**ın

(araç çubuğu üzerindeki **Start** butonunu tıklayın veya <**F5**>’e basın). Size bazı dosyaları saklayıp saklamayacağınız sorulabilir: Şimdilik **No(Hayır) **ile cevap verin veya **Cancel(iptal)**’i tıklayın.

Form şu şekilde belirecektir:

Üzerinde ‘Beep!’ yazan komut butonunu tıklayın. Bilgisayar **bip** sesi vermelidir. **cmdBeep** kontrol’ü üzerinde bir **Click** **event(olay)**’ına sebep oldunuz. Bilgisayar bunu fark edecek ve **cmdBeep\_Click** olay prosedürüne gidecektir.

Buradaki kod satırı(Beep) yorumlanacak ve bilgisayar bip sesi verecektir. Projenizi durdurun. Kod penceresine gidin ve **cmdBeep\_Click** olayını bulun. **Beep** satırından sonra, şu satırı ekleyin:

## **frmFirstCode.BackColor = vbBlue******

Aynen yukarıda yazıldığı gibi yazdığınızdan emin olun. Hatırlayın**, bilgisayar programları kesin olmalıdır**. Projeyi yeniden çalıştırın(Run). Komut butonunu tıklayın. Kontrol, olay prosedürü ve BASIC kodu ile olan ilişkisini açıklayın. Projenizi durdurun.

Özetle;

Şimdi ilk ve komple bir Visual Basic projesini tamamladınız. Bir uygulamayı yapılandırırken şu üç adımı takip ettiniz:

Form üzerine kontrolleri yerleştirin.

Kontrol özelliklerini atayın(verin).

Kontrol olay prosedürleri yazın.

Aynı adımları, ister buradaki gibi çok basit, isterse de çok karmaşık bir projeyi yapılandırırken aynen takip edeceksiniz.

Şimdi, bu adımları bilerek, Visual Basic Toolbox(araç kutusu) üzerinden çalışmaya her kontrolün ne yaptığını öğrenmeye hazırsınız. Programlarınızı yazarken, size yardımcı olması için, BASIC dilinin elemanlarını öğrenmeye başlayabilirsiniz. Proje geliştirmenize yardımcı olmak için, Visual Basic Ortamının yeni özelliklerini öğrenmeye başlayabilirsiniz. Her bir sonraki derste bazı yeni kontroller, bir miktar daha BASIC ve Visual Basic hakkında daha fazla yeni şeyler öğreneceğiz.

## ** PAGE 23**

## *** ****** *****Herkes için ****VISUAL BASIC\_\_\_\_\_\_ **

## \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## *** İLK*** ***VISUAL BASIC PROJENİZ *** ** PAGE 23******

## PAGE 12 PAGE 7

## **Left**

## **Top**

## **Height**

## **Width**

---
*Kaynak: `HERKES İÇİN VISUAL BASIC/BOLUM-3.DOC` — M. ŞAKİR UNUTUR — 2001*
