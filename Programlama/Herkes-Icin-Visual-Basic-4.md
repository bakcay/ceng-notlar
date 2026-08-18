# Herkes İçin Visual Basic

## **Herkes İçin**

## **Visual Basic******

## 4. Proje (Tasarımı)Dizayn’ı, Formlar ve Komut Butonları

## ***Tekrar Gözden Geçirme ve Bir Önbakış***

Şimdiye kadar, bir Visual Basic projesinin parçalarını ve bir proje yapılandırılması ile ilgili şu üç adımı öğrendiniz:

Form üzerine kontrolleri yerleştirin.

Kontrol özelliklerini düzenleyin.

İstenilen olay prosedürünü yazın.

Visual Basic ile yapılandırmak istediğiniz projeler hakkında bir fikriniz var mı ? Eğer böyle ise, çok güzel ! Bu dersten başlayarak, kendi programlama becerinizi geliştirmeye başlayacaksınız. Geldiğimiz her yeni derste, Visual Basic ortamının bazı yeni özelliklerini öğreneceğiz. Birtakım yeni kontroller ve BASIC dilinin bazı yeni elemanları bunlardan bazılarıdır.

Bu derste, proje **dizayn(design)**’ı,** form**, **komut butonu kontrolleri** ve **komple bir projenin nasıl yapılandırıldığını** öğreneceksiniz.

## Proje Design(Dizayn-Tasarım)’ı

Şimdi, Visual Basic kullanarak projeler geliştirmeye başlamak üzeresiniz!

Size, yapılandırmanız için bazı projeler vereceğiz ve belki de sizin kendi projelerinizi oluşturmak için baz fikirleriniz olacak. Her ne şekilde olursa olsun, bilgisayar programları olarak sonuçlanan fikirleri görmek, hoş ve etkileyici olacak ! Fakat, bir projeye başlamadan evvel, ne yapmaya çalıştığınız konusunda biraz durup düşünmeniz iyi olacaktır. Uygun **proje** **dizayn’ı **size çok fazla zaman kazandıracak ve sonuçta, ileride daha iyi bir proje olarak sonuçlanacaktır!** ******

Uygun proje dizayn’ı gerçekten zor değildir ! Bir proje yaratmanın ana fikri; kullanımı kolay, kolay anlaşılır ve hatalardan arındırılmış bir proje yaratmaktır.

Anlamlı, değil mi? Projenizde yapmak istediğiniz herşey için bir süre durun ve düşünün ! Program ne türde bilgilere ihtiyaç duyuyor? Hangi bilgileri bilgisayar hesaplayacak? Bu bilgi topluluğunu sağlayın ve hangi kontrollere ihtiyaç duyacağınıza karar verin ! İyi bir

**user interface(kullanıcı arabirimi)** dizayn edin (arabirim, kontrollerin form üzerine yerleşimini de içine alır). Görünüm ve kullanım kolaylığını göz önüne alın. Eğer mümkünse, arabirimini, diğer Windows uygulamaları ile uyumlu olarak hazırlayın. Visual Basic kullanılarak hazırlanmış olanlar gibi, Windows tabanlı projelere aşinalık, herzaman iyidir.

Olay prosedürünüzü hazırlarken, BASIC kod’unuzu okunabilir ve kolay anlaşılabilir hazırlayın. Bu proje üzerinde daha sonra yapılacak değişiklikleri (veya sizin yapacağınız değişiklikleri) çok daha kolay hale getirir. Kabul edilen programlama kurallarına uyun - BASIC hakkında daha fazla şeyler öğrendikçe, bu kuralları da peyderpey öğreneceksiniz.

Projenizde hata bulunmadığından emin olun. Bu çok açık bir ifade gibi görünmesine rağmen, pekçok programlar hatasız değildir. Windows 95 içinde bile dolaşan birkaç yüz hata bulunmaktadır.

Proje dizaynı konusunda bu birkaç ifadenin önemi şimdilik pek anlaşılmasa da, ileride bunların önemi ortaya çıkacaktır. Amaç, basit bir fikir, faydalı, açık yazılmış, kolay kullanımı olan ve değiştirilmesi kolay, hatalardan arındırılmış projeler hazırlamaktır.

Dikkatli bir ileriye yönelik planlama, bu amaca ulaşmanızda yardımcı olacaktır.

Bu derste yapılandırılan her proje için, proje dizayn yöntemi’nin iç yapısına bir bakış vermeye çalışacağız. Bir projeyi yapılandırırken, daima neden yaptığımızı ve ne yaptığımızı anlatmayı deneyeceğiz. Göz önüne aldığımız her şeyin açıklamasını size vereceğiz.

## ** **Bir Visual Basic Projesini Kaydetmek(Save)

1.derste , daha önceden **kaydedilmiş(saklanmış)** bir Visual Basic projesini nasıl açacağınızı, çalıştıracağınızı ve kapatacağınızı öğrendiniz. Fakat şimdiye kadar, hiçbir yerde, bir projenin ileriki kullanımları için nasıl saklanılacağından bahsetmedik. Şimdi artık kendi projenizi yapılandırmaya başlıyorsunuz ve onları nasıl saklayacağınızı bilmeye ihtiyacınız var.

Bu gerçekten de çok kolaydır. Visual Basic ana penceresinde bulunan araç çubuğunu kullanacağız. Üzerinde bir disket resmi bulunan butona bakın. (Gittikçe kullanımı artan ve yazabilen CD sürücüleri ile, insanların daha ne kadar bir disketin nasıl göründüğünü hatırlayacaklarını düşünüyorsunuz ? – yeni Apple iMac’ın üzerinde bir disket sürücüsü bile yok !). Bu **Save** **Project(Projeyi Kaydet)** buton’udur:

Bu butonu tıklamak, onu ne zaman tıkladığınıza bağlı olarak, farklı sonuçlar veririr. Yeni bir proje üzerinde çalışıyorsanız ve daha evvel hiç saklamadıysanız, aşağıdaki pencere ortaya çıkacaktır:

Bu pencere, form’unuzu **nereye** kaydetmek istediğinizi ve ona **ne isim vermek** istediğinizi sormaktadır (tekrar hatırlayalım bu dosya **frm** uzantısına sahiptir). İstenen dizine gidin, form dosyasına istediğiniz bir isim verin (anlamlı bir isim) ve daha sonra **Save **tuşunu tıklayın.

Formunuzu kaydettikten sonra, aşağıdaki gibi başka bir pencere belirecektir :

Bu pencere proje dosyanızı, nereye ve hangi isimle kaydetmek istediğinizi sormaktadır(**vbp** uzantılı bir dosya ismi). Yine bir dizin seçin(genellikle form dosyasını kaydettiğiniz dizindir), bir proje ismi girin(yine bu isim anlamlı olsun) ve **Save’**i tıklayın.

Burada projeniz iki dosyada kaydedilmiştir: **form dosyası** ve **proje dosyası**.

Eğer daha önceden **save(kaydet)**’ilmiş bir proje üzerinde çalışıyorsanız ve **Save** **Project** buton’unu tıklarsanız, Visual Basic otomatik olarak form dosyası ve proje dosyasını aynı isimle, herhangi bir soru sormadan kaydedecektir. Üzerinde çalıştığınız projeyi ara sıra kaydetmeniz tavsiye edilir. Daima projelerinizi çalıştırmadan evvel veya Visual Basic’ten çıkarken kaydedin. Kaydedilmiş bir projeyi açmak isterseniz sadece pencere üstünde bulunan araç çubuğu üzerinde bulunan **Open** **Project(Proje Aç)** buton’unu tıklayın.

İstediğiniz proje dosyasını seçin ve **Open(Aç)’**ı tıklayın. Proje dosyası ve bu proje ile ilgili form dosyası açılacak ve form ortaya çıkacaktır.

## ***On-Line Help (Çevrim-İçi Yardım)*********

Birçok kereler, Visual Basic ortamında çalışırken, herhangi birşey hakkında bir sorunuz olabilir. Belirli bir kontrol’ün ne yaptığı konusunda, belirli bir özelliğin ne için olduğu, bir kontrol’ün hangi olaylara sahip olduğunu veya belirli bir terim’in BASIC’te ne anlama geldiği konusunu merak edebilir veya şüpheye düşebilirsiniz. Böylesi askıda (havada) kalan durumlarda en iyi yol cevabını bilen birisine sormaktır. İnsanlar genellikle size yardımcı olmaktan mutlu olurlar-sizin öğrenmenize yardımcı olma fikrini severler.

Aynı zamanda cevabı bir kitapta bulmayı deneyebilirsiniz ve bu konuda bir sürü Visual Basic kitabı bulunmaktadır.

Veya, yardım almanın başka bir güzel bir yolu ise Visual Basic **On-Line** **Help** Sistem’ini kullanmaktır.

Visual Basic’in de içinde olduğu birçok Windows uygulaması, kullanılabilir durumda, yardım dosyalarına sahiptir.

Visual Basic Help Sistem’ine ulaşmak için, ana menü’de bulunan **Help(Yardım)** seçeneğini ve daha sonra da **Contents(İçerik)**’i tıklayın. Bu nokta’da ihtiyaç duyduğunuz yardıma ait başlığı araştırabilir veya bütün başlıkları kaydırma çubuğu ile gezinerek aradığınız yardımı bulabilirsiniz. Visual Basic Help Sistem’i diğer bütün Windows Help Sistem’leri gibidir.

Eğer daha evvel herhangi bir on-line help sistemi kullandıysanız, Visual Basic’deki on-line help sistemini kullanmanız kolay olacaktır. Eğer şimdiye kadar hiç bir on-line help sistemi kullanmadıysanız, yardım için birisine sorun. Kullanımı oldukça kolaydır. Veya, Windows task bar üzerindeki **Start’**ı tıklayın ve daha sonra da **Help’**i seçin. On-line Help Sistem’ini kullanarak, bir on-line Help Sistem’inin nasıl kullanıldığını öğrenebilirsiniz.

Visual Basic on-line help sistem’inin gerçekten müthiş bir özelliği vardır**; ‘context sensitive’ (bağlam duyarlı)**. Bu ne anlama geliyor?

Deneyelim !

Visual Basic’i çalıştırın ve yeni bir projeye başlayın. Özellikler penceresine gidin. Form özelliklerini gösteren pencere kenarındaki kaydırma çubuğunu kaydırarak, **BackColor **kelimesini tıklayalım. Kelime belirginleşir. <**F1**> tuşuna basın.

BackColor özelliği hakkında bir ekran dolusu bilgi görünür. Help sistem’i akıllıdır ! BackColor kelimesini belirginleştirdiğinizi ve daha sonra <**F1**> tuşuna basıldığını (<**F1**> daima yardım istendiğinde basılan bir tuştur) görünce, sizin BackColor hakkında yardım istediğinizi anlar.

Visual Basic çalışırken, ne zaman <**F1**> tuşuna basarsanız, program nerede çalıştığınıza bakarak, bağlam-duyarlı’lığınıza dayandırarak, ne hakkında yardım istediğinizi tespit etmeye çalışır. Bu özellikler penceresinde belirginleştirilmiş bir kelime veya kod penceresindeki imleç olabilir. Visual Basic ile çalıştıkça, ‘context-sensitive’ yardım’ı çok faydalı bulacaksınız. Sorularınıza, pek çok kereler, çabuk cevaplar alabilirsiniz. Yardım almak için, Visual Basic on-line help sistem’ine güvenmeyi bir alışkanlık haline getirin !

Visual Basic ortamı için, bu kadar yeni malzeme yeterli ! Şimdi detaylı olarak, iki önemli kontrol’e bakalım: **form’un kendisi** ve **komut butonu**. Daha sonra BASIC dili ve komple bir proje yapılandırılma çalışmasına başlayacağız.

## Form Kontrol olarak, Form

Bizler **form**’un, bir Visual Basic Projesinin geliştirilmesindeki temel kontrol olduğunu öğrendik. Form olmadan, proje olmaz! Form Kontrolü için bazı önemli özellikler ve olaylara bakalım. Yeni bir projeye başladığınızda form aşağıdaki gibi görünecektir:

## ***Özellikler ***

Bütün kontroller gibi, form da birçok (40’dan fazla) özelliğe sahiptir. Şanslıyız, yalnızca bunların bazılarını bilmek zorundayız. Göz önüne alacağımız özellikler :

## ***Özellik****** ******Açıklama****** *********

**Name**** **Form’u tanımlamak için kullanılan isim.** **Form isimleri için kullanılan üç harfli önek **frm’**dir.

**Caption **Form’un başlık çubuğu üzerinde görünen yazı** ******

**Icon **Form’un başlık çubuğu üzerinde görünen ikon(küçük şekil)’e referans** **(ikon yaratma’ya 7. derste bakacağız).

**Left** Form’un sol kenarından, ekranın sol kenarına kadar olan uzaklık

**Top** Bilgisayar ekranının üst kenarından, form’un üst kenarına kadar olan uzaklık

**Width** Twip birimi ile, form’un genişliği

**Height** Form’un twip birimi ile yüksekliği

**BackColor **Form’un **background(artalan)** rengi

**BorderStyle** Proje çalıştığında, form ya **boyutu değiştirilebilir (sizable)** veya **sabit tek(fixed single) ** boyutlardadır (boyut değiştirme, fare kullanılarak yapılır).

## ***Örnek*********

Bu özelliklere aşinalık kazanmak için, Visual Basic’i çalıştırın ve yalnız tek bir form’u olan yeni bir projeye başlayın. Top, Left, Height ve Width özellik değerlerini ayarlayarak, form’un boyut ve ekran üzerindeki yerleşimindeki değişikliklerini gözlemleyin. Form’u yeniden boyutlandırın ve taşıyın. Özellikler penceresinde bu değerlerin nasıl değiştiğini gözlemleyin. Caption(Başlık) özelliğini ayarlayın. Yeni bir background rengini, 3. derste anlatılan teknikleri kullanarak değiştirin. **BorderStyle(Sınır Stili)** özelliğinin etkilerini görmek için, bir değer verin (ya **1-Fixed** **Single (sabit Tek)** veya **2-Sizable (Boyutu Değiştirilebilir**) kullanın). Bu derslerde, yalnızca bunları kullanacağız.

Projeyi çalıştırın. Evet, bir projeyi üzerinde sadece bir formla, formu kontrol olarak çalıştırabilirsiniz ! Her durumda form’u yeniden boyutlandırmayı deneyin. Fark’a dikkat edin. Bu örnek projeyi durdurun.

## ***Olaylar ***

Form; temelde, diğer kontroller için bir **konteyner(kap)** gibi davranır, fakat olayları destekler, yani bazı kullanıcı etkileşimlerine cevap verebilir. Bu derslerde yalnızca iki form olayı ile ilgileneceğiz:

## ***Olay****** ******Açıklama*********

**Click **Click(tıklama) olayı, sadece kullanıcı form’u fare ile tıklarsa, yerine getirilir.

**Load** Olay, form ilk olarak bilgisayarın hafızasına yüklenerek yerine getirilir. Değişik ilk değerler ve diğer proje değerlerini vermek için, iyi bir olaydır.

Eski derslerden hatırlayın, kontrol isimlerinin, olay prosedürlerinde kullanıldığını öğrendik. Bunlar, form’lar için doğru değildir. Bütün form olay prosedürleri aşağıdaki format’a sahiptir:

```vbnet
Form_EventName
```

Anlamı ise, form’a hangi **Name** özelliği verirseniz verin, olay prosedürleri **Form **kelimesi altında listelenirler. Böylelikle, kod penceresinde form olay prosedürlerine baktığınızda, **Object** **List**’esini **Form**’u bulana kadar, kaydırma çubuğu ile kaydırarak arayın. Şunu da belirtmek gerekir, eğer biz form’a **frmFirstCode** ismi verirsek, kod penceresi aşağıdaki şekilde görünecektir :

VB4:

VB5, VB6:

Dikkat edin, nesne listesinde **Form** kelimesi görünmektedir( **frmFirstCode **değil).

Form olay prosedürleri ile çalışırken, daima bu özelliğin farkında olmalıyız. Bütün diğer kontroller, kendilerine verilmiş isim özellikleri ile birlikte, nesne listesinde görüneceklerdir.

## Komut Butonu Kontrol’ü

**Command** **button(komut butonu) **en yaygın olarak kullanılan Visual Basic kontrollerinden birisidir. Komut butonları; başlatmak, durdurmak veya belirli yöntemleri bitirmek için kullanılır. Command button(komut butonu) araç kutusundan seçilir. Aşağıdaki şekilde görünür :

## ** *****Araç Kutusu İçinde Form Üzerinde default(varsayılan) ***

## *** özellikler:***

## ***Özellikler***

Komut butonu için birkaç faydalı özellik:

## ***Özellik ****** ******Açıklama ***

**Name **Komut butonunu tanımlamak için kullanılan isim. Komut butonları isimleri için kullanılan üç harflik önek **cmd **‘dir.

**Caption **Komut butonu üzerinde görünen yazı

**Font** Caption yazısı’nın **style(stil), size(boyut), **ve** (type)tip’**ini belirler.

**Left** Form’un sol kenarından komut butonunun sol kenarına olan uzaklıktır.

**Top** Form’un üst kenarından, komut buton’unun üst kenarına olan uzaklıktır.

**Width** Komut butonu’nun twip birimi ile genişliği.

**Height** Komut butonu’nun twip birimi ile yüksekliği

**Enabled** Komut Buton’unun kullanıcı olaylarına (run mod’unda) **karşılık (cevap)** verip, vermeyeceğini belirler.

**Visible** Komut Buton’unun form üzerinde (run mod’unda) görünür olup, olmayacağını belirler.

## ***Örnek ***

Visual Basic’e ve yeni bir projeye başlayın. Form üzerine bir komut butonu koyun. Butonu gezindirin, Top ve Left özelliklerindeki değişmeleri izleyin. Buton’u tekrar boyutlandırın ve Width ve Height değerlerinin nasıl değiştiğine dikkat edin. Caption özelliğini verin.

Komut butonuna ilaveten birçok kontrol bir **Font(yazı)** özelliğine sahiptir.

Şimdi bunun nasıl değişitirileceğini anlamak için bir bakalım. Font, Caption’ın nasıl görüneceğini belirler. Özellikler penceresinde Font’u tıklarsanız, **ellipsis** adı verilen ve aşağıda görünen bir buton, pencerenin sağ tarafında ortaya çıkar:

Bu buton’u tıklayın, **Font** **Window(Font Penceresi) **görünecektir.** **

Bu pencereden, bilginin üç temel parçasını seçebilirsiniz: **Font(Yazı)**, **Font** **Style(Font Stili)**, ve **Size(Boyut)**. Aynı zamanda altı çizili bir font’da seçebilirsiniz.

Bu pencere, bilgisayarınızda depolanmış bütün fontları listeler. Font özelliğini ayarlamak için, bu pencere içinde seçimlerinizi yaparak **OK’**i tıklayın. Farklı fontları, font stillerini ve font boyutlarını, komut butonunun Caption özelliğini değiştirmek üzere, deneyin.

Komut butonunda listelenen diğer iki özellik; **Enabled** ve **Visible’**dır. Bu özelliklerin her birisi, ya **True-Doğru (On) **ya da **False-Yanlış (Off)**’tur. Bir çok diğer kontrol de aynı zamanda bu özelliklere sahiptir.

Peki, neden bunlara ihtiyacınız var ?

Eğer bir kontrol’ün** Enabled özelliği False **ise, kullanıcı bu kontrole ulaşamayacaktır. Üzerinde **Start(Başlat)** ve **Stop(durdur) **butonları bulunan **Stopwach(Kronometre)** projemize bakalım:

Kullanıcının bu proje ile **Start** ve daha sonra **Stop** tuşlarını tıklamasını ve geçen sürenin bulunmasını istiyorsunuz. Kullanıcının Start buton’una tıklamadan, Stop buton’una **basamamasını** istiyorsunuz. Böylece başlangıç olarak **Start** buton’unun **Enabled** özelliğini **True**’ya ve **Stop** buton’unun **Enabled** özelliğini **False**’a ayarlamanız gerekmektedir. Bu yolla kullanıcı sadece **Start**’ı tıklayabilir. Bir kere kullanıcı Start’ı tıkladığında, özellik değerlerini değiş tokuş etmeniz gerekmektedir. Bu, Start buton’unun Enabled özelliğini False ve Stop button’unun Enabled özelliğini True yapmaktır. Kullanıcı ancak bu yolla Stop’u tıklayabilir.

Enabled özelliğinin False yapılmasının etkisi, sadece, Visual Basic run mod’unda iken kendisini gösterir. Bir komut butonu Enabled yapılmadığında (Enabled, False olarak verilirse), **‘silik’** olarak görünecektir ve kullanıcı bunu tıklayamayacaktır. Stop, Enabled yapılmazsa, kronometre aşağıdaki gibi görünecektir:

Böylelikle Enabled özelliğini, kontrol’ün, form üzerinde geçici olarak disabled (Etkinliğini Kaldırma) yapmak için kullanın. Daha evvel üzerinde konuştuğumuz gibi, bu, proje dizayn yönteminde bir karar verme durumudur.

**Visible(görünürlük)** özelliği, biraz daha zorlayıcıdır. Bir kontrol’ün Visible özelliği False olarak ayarlandı ise (varsayılan değerTrue’dır), kontrol form üzerinde bulunsa bile, proje çalıştırıldığında kontrol form üzerinde olmayacaktır!

Şimdi form üzerine yerleştirdiğimiz, özelliklerini ayarladığımız ve onun için olay prosedürleri yazdığımız bir kontrol’ün neden **invisible(görünmez)** olmasını isteyebiliriz? Cevap; Enabled özelliği ile benzerdir. Birçok kereler, bir proje içinde bir kontrol’ün geçici olarak ortadan kaybolmasını isteyebileceksiniz.

1. derste, **Sample** projesinde, oyuncakların görünüp görünmemesini sağlayan **check box(onay kutu)**’ları bulunmaktaydı. Oyuncakların görünmesi, image control’ünün Visible özelliğinin kontrolü ile gerçekleştirilmiştir. Veya, küçük kronometre örneğinde olduğu gibi, bir buton’un Enabled özelliğini False’a ayarlamak yerine, onu **unclickable**

**(tıklatılmaz)** yaparak, Visible özelliğini de False’a ayarlayarak, onun daima (sürekli) olarak görünmesini önledik. Her iki yolla da, aynı istenen sonucu elde edersiniz. Bu başka bir proje dizayn kararıdır. Enabled özelliği gibi,Visible’ın False yapılmasının etkileri yalnızca run mod’unda görülür. Bu anlamlıdır. Bir projeyi invisible control’lerle dizayn etmek zordur!

Şimdi, üzerinde çalıştığınız örnekte bulunan komut buton’unun Enabled ve Visible özellikleri ile oynayın. Bu özelliklerden birisine değer girdiğinizde, projeyi çalıştırın ve sonuçlarını görün. Dikkat edin, Enabled özelliği False olarak verilmiş butonu tıklayamazsınız. Yine dikkat edin,Visible özelliği False olarak verildiğinde, buton orada yerinde olmayacaktır. Daha sonra örnek projeyi durdurun.

## ***Olaylar***

İlgilendiğimiz yalnızca bir komut butonu olayı vardır, fakat bu çok önemli bir olaydır:

## ***Olay****** ******Açıklama *********

**Click **Kullanıcı fare ile komut butonunu tıkladığında, olay yerine getirilir.** ******

Her komut butonu, Clik Event(Tıklama Olay)’ına karşılık gelen bir olay prosedürüne sahiptir.

## ***BASIC – İlk Ders***

Uzun bir süre sonunda bir Visual Basic projesine giriş yapabilmeye artık

hazırız - **BASIC dili !** Bir Visual Basic Projesinde, olay prosedürlerin, kontrol olaylarını bilgisayar tarafından yerine getirilenlere bağlantılamak için kullanıldığını öğrendiniz.

Bu olay prosedürleri BASIC kullanılarak yazılır. Yani Visual Basic’ i bilmek için, BASIC bilmeniz gerekmektedir. Bu kitapta takip eden her derste, BASIC dili hakkında yeni yeni şeyler öğreneceksiniz.

## ***Event Procedure(Olay Prosedür) Yapısı ***

Biliyorsunuz, bu olay prosedürleri, şimdiye kadar Visual Basic Kod Penceresi’nde görünebiliyordu. Her olay prosedürü aynı genel yapıya sahiptir. İlkin, form’un bir **header(Başlık) **satırı vardır:

```vbnet
Private Sub ControlName_EventName()
```

Bu, **Private(Özel)** (yalnızca form’umuzdan ulaşılabilir), **Sub**routine’nin (bir olay prosedürü için başka bir isim) , **ControlName **kontrolü için, **EventName** olayı olduğunda yerine getirildiğini gösterir. Anlamlı, değil mi ?

**Event procedure(olay prosedür)**’ü, başlık satırından sonra başlar.

Olay prosedürü kodu, basit bir anlatımla bilgisayara ona ne yapması gerektiğini söyleyen,

satır-satır verilen talimatlar serisidir. Bilgisayar, ilk satırı işler, daha sonra ikincisini ve daha sonra bunları takip eden diğer satırları... Bilgisayar, olay prosedürünün **footer(taban) **satırına ulaşana kadar bu işlemleri yapar.** Footer(taban) **satırı:

```vbnet
End Sub
```

Olay prosedürü kod’u, BASIC dili ile yazılır. BASIC, bilgisayara belirli birtakım şeyleri yapmasını sağlayan anahtar kelime ve semboller set’inden oluşur. BASIC’in içeriği çok geniş ve zengindir ve bu kurs’ta bunlardan yapabildiğimiz kadarını inceleyeceğiz. Hemen bu noktada bir uyarı ! Daha önce söyledik, ama bir kere daha söyleyelim.

Bilgisayar Programlaması kesinlik gerektirir - hatalara izin vermez ! Özellikle olay prosedürleri yazarken, kesin olmalısınız ! Bilgisayar çağında iyi klavye kullanımı (yazım) tecrübesi bir gerekliliktir. Visual Basic Programlaması öğrendikçe, klavyeden yazım becerinizi geliştirebileceğiniz bu amaçla piyasada bulunan yazılımları, faydalı bulabilirsiniz.

Klavyeden daha iyi yazım tecrübesi, Visual Basic uygulamalarınızı yapılandırırken daha az hata yapacağınız anlamına gelir.

## ***Atama (Assignment) Bildirileri ***

BASIC’te en basit ve en fazla kullanılan **assignment statement (atama bildiri)**’ leridir. Aşağıdaki şekle sahiptir:

```vbnet
LeftSide = RightSide
```

‘ **=** ‘ sembolü **assignment** **operator(atama operatör)’**ü olarak adlandırılır.

Bu sembol’ün aritmetik’te eşittir anlamına gelen sembol olduğunu biliyorsunuz. Fakat Bilgisayar Programlanmasında eşittir olarak adlandırılmaz.

Neden böyle ?

Bir atama bidirisini, solda ne bulunmaktaysa, sağdakilerle değiştirilecektir şeklinde ifade ederiz. Atama bildirisinin sol tarafı bir kontrol özelliği gibi, yalnızca tek bir terim olabilir. Sağ taraf ise herhangibir kabul edilebilir BASIC ifadesi olabilir. Bazı matematiksel hesaplamalar veya hesaplanması gereken bazı şeyler gerekebilir. Eğer böylesi hesaplamalar varsa, atama yapılmadan evvel gerçekleştirilmelidir.

Şimdi çok genel ifadelerle konuşuyoruz ve konuşmak zorundayız da ! Atama bildirileri fikri, daha fazla BASIC öğrendikçe, çok daha açık ve anlamlı olacaktır.

## ***Property(Özellik) Tipleri ***

Hatırlayın, bir özellik, bir kontrol hakkında birşeyi açıklar**: boyutlar(size), renk(color), appearance(görünüm), ....** Her **property(özellik),** belirli bir **tip(type)’**te,** ** temsil ettiği bilginin cinsine bağlı olarak, bir özelliği temsil eder.

Design(dizayn) mod’unda bir değer vermek için özellikler penceresini kullanırsak, Visual Basic otomatik olarak uygun olan tipi sağlayacaktır. BASIC atama bildirisi kullanarak, bir olay prosedüründe, eğer bir özelliği değiştirmek istiyorsak, özellik tipini bilmek zorundayız, zira ona uygun ve hatasız tipte bir değer girebilelim. Hatırlayın**; ‘dot notation’ (nokta notasyon)** adı verdiğimiz bir atama tipini, run mod’unda değiştirebilmemiz için kullanıyorduk :

```vbnet
ControlName.PropertyName = PropertyValue
```

ControlName , kontrole atanmış **Name(İsim)** özelliğidir. PropertyName özelliğin ismidir ve PropertyValue, PropertyName’ e atadığımız yeni bir değerdir.

Burada dört tipte özellik ile ilgileneceğiz:

Birinci özellik tipi, **integer(tamsayı)** tipidir. Bunlar tam, küsüratlı biçimde ifade edilmeyen, sayılardır. **Top**, **Left**, **Height**, ve **Width** gibi özellikler integer tipindedir. Yani, eğer integer tipte bir özelliğe bir değer atayacaksak, tamsayı kullanacağız. Bir örnek olarak, frmExample adını verdiğimiz bir form’un width özelliğini 4,000 twip’e ayarlayacaksak, BASIC’te şunları yazmalıyız:

```vbnet
frmExample.Width = 4000
```

Bu, geçerli form’un Width(genişliğini) yeni bir değer olan 4000 olarak atayacağımızı belirtmektedir. Dikkat edin, BASIC’te 4000 yerine, içinde virgül bulunan 4,000 şeklinde yazamayız.

İkinci bir özellik tipi **long** **integer(uzun tamsayı) **tipidir ve uzun tamsayı tipi, aynen isminin ifade ettiği gibidir. Integer tipte bir özellik en fazla 32,767 değerini alabilir. Bazen bu sayılardan daha büyük sayılara ihtiyaç duyabiliriz, bundan dolayı **long integer** tipi vardır. Bir long integer 2,147,483,647 sayısına kadar değer alabilir.

Yeteri kadar büyük değil mi?

Fakat Bill Gates, sahip olduğu serveti bu tipte bir özellikle yazamaz, çünkü yetersiz kalır. Belkide, Microsoft ‘dan birisinin kendisi için, **very** **long** **integer(çok uzun tamsayı)’**yı icat etmesi gerekebilir.

Uzun tamsayı’ları kullanan çok genel özellikler, **BackColor(arka-artalan rengi**) ve** ForeColor(ön kısım rengi)**’i ve bazı diğer kontroller için olanları göreceksiniz. Hatırlayın, önceki derslerimizde, gri renk için atanan özellik değeri bir uzun tamsayı için &H8000000F& şeklinde yazılmıştı-bu bir kısa **gösterim(notasyon)**’dur (bir heksadesimal sayı olarak adlandırılır). Renk özelliklerine değerler atarken, uzun tamsayı’ları kullanmalıyız.

Şanslıyız, Visual Basic renklere long integer sayılar vermek için, bir çok kolay yol sağlamaktadır. Böylelikle, long integer’lar ile çalışmayı kolay hale getirmiştir. Renkleri kullanmanın bir yolu, **symbolic** **constants(sembolik sabitler)**’dir. Sembolik sabitler, Visual Basic’de pek çok yerde kullanılmaktadır – bunlardan pek çoğunu bu dersler ilerledikçe göreceğiz. Bütün sembolik sabitler iki harf ile başlar; **vb** (Visual Basic).

Renkler için bazı sembolik sabitler aşağıdaki gibidir:

**vbBlack** - Siyah **vbRed** - Kırmızı

**vbGreen** - Yeşil **vbYellow** - Sarı

**vbBlue** - Mavi **vbMagenta** - Mor

**vbCyan** - Cyan (gök mavisi) **vbWhite** - Beyaz

Bu sabitlerin herbirisi, kendisine karşılık gelen, temsil ettiği renge ait long integer değerini **depolar(store).** Bizim örneğimizdeki formun BackColor özelliğini maviye çevirmek için, şu atama bildirisini kullanmalısınız:

```vbnet
frmExample.BackColor = vbBlue
```

İfade şu anlama gelir: Form’un **BackColor(artalan renk)**’i, **vbBlue** olarak adlandırılan sembolik sabit’in temsil ettiği long integer değeri ile değiştirirlir.

Bir diğer özellik(property) tipi ise **Boolean** tipidir. İsmini meşhur matematikçi Boole’dan almıştır. Yalnızca iki değere sahip olabilir: **True(Doğru)** veya **False(Yanlış). **

** **Daha evvel gördüğümüz gibi, komut butonu’nun Enabled ve Visible özellikleri Boolean değerlerine sahip olabilirler. Böylece, Boolean tipinde özelliklerle çalışırken, yalnızca** True **veya **False** değeri verdiğimizden emin olmalıyız. Örneğimizin formunu gözden kaybettirmek için (bunu yapmak iyi bir şey değil !), aşağıdaki atama bildirisini kullanmalıyız:

```vbnet
frmExample.Visible = False
```

Bu ifade, form’un geçerli Visible özelliğinin, Boolean değeri olan False ile değiştirileceğini söylemektedir. Tekrar eski haline döndürmek için:

```vbnet
frmExample.Visible = True
```

Belirtmemiz gereken son özellik tipi **string(dizilim)** tipidir. Bu tipte özellikler, basitçe, adının ifade ettiği gibidir - karakterlerin dizilimi. **Bir**** string;** **bir isim, bir sayı dizisi, bir cümle, bir paragraf veya herhangibir tipte karakterler dizisi** olabilir.

Birçok kereler, bir string hiçbir karakter içermez(bir boş string). Caption özelliği, string tipte bir özelliktir. Visual Basic’de, string’ler ile birçok çalışmalar yapacağız ve bu yüzden bununla aşina olmamız gerekmektedir.

String tipte özellikler atarken, tek bir sırrı(inceliği) vardır; bu da string değerini tırnak içine almaktır (“). Özellikler penceresi içinde string karakter tırnak içine alınmadığından, sizin tırnak içine alma zorunluluğunu, unutma eğiliminiz bulunmaktadır.

Örneğimizde **form caption(başlık)**’ı için şunu kullanabiliriz:

```vbnet
frmExample.Caption = “Bu tirnak içinde bir basliktir”
```

Bu atama bildirisi, form’un Caption özelliğinin, ifadenin sağ tarafındaki yazı ile değiştirilmesi bildirisini vermektedir. Şimdi, atama bildirilerinin nasıl olduğu hakkında fikir sahibi olmalısınız.

## ***Yorumlamalar ( Kodlama içine notlar düşme)***

Proje dizayn’ı konusunda bahsettiğimiz gibi, BASIC kod’u yazarken, uygun programlama kurallarını takip etmek zorundayız. Böyle bir kural, kod’unuzu uygun(düzgün) biçimde yorumlamanız ! Kodlarınızda, bilgisayar tarafından göz önüne alınmayan, çalıştırılmayan ve ne yaptığınızı açıklayan tanımlama yazıları koyabilirsiniz.

Bu **comments(yorumlamalar), **kod’unuzu** **anlamak için yardımcı olacaktır. Bunlar aynı zamanda ileride yapacağınız değişiklikleri çok daha kolay hale getirecektir.

Kod’unuzun içerisine bir yorumlama koymak için, bir kesme işareti (‘) koymanız gerekmektedir. Bu işaret 1 tuşunun sağ tarafında bulunan tuş **değil**, Ş tuşunun altında bulunup (AltGr) tuşu ile yazılır. Bu işaretten sonra yazılan her şey bilgisayar tarafından ihmal edilir. Komple bir BASIC kod satırını açıklayan, böyle bir yorum satırı, aşağıdaki gibidir:

```vbnet
‘Form’u maviye çevir
frmExample.BackColor = vbBlue
```

Veya, yorumunuzu aynı satırda atama bildirisinden sonra aşağıdaki gibi yazabilirsiniz:

```vbnet
frmExample.BackColor = vbBlue ‘Formu mavi yapar
```

Programcı olarak siz, kod’unuzu ne kadar yorumlayacağınıza karar vermelisiniz. Bu kursta size sunulan projelerde yeteri kadar yorumlama sağlayacağız. Şimdi ilk önce böyle bir projeye bakalım:

## ***Proje - Form Fun (Eğlenceli Form)***

## ***Proje Tasarımı *********

Bu projede, komut butonlarını kullanarak form özellikleri ile biraz eğlenelim.

Bir butonumuz form’u büyütecek, diğeri küçültecek ve diğer iki buton ise form’un rengini değiştirecektir. Bunlara ilaveten yine form üzerinde bulunan iki butondan birisi form’u gözden kayedecek, diğeri ise tekrar görüntüye getirecektir.

## ***Form üzerine kontrolleri yerleştirin: *********

Visual Basic’te yeni bir proje başlatın. Form’un büyüklüğünü, üzerine 6 tane buton sığacak şekilde ayarlayın. 6 tane komut butonunu form üzerine yerleştirin. Butonları aşağıda göründüğü şekilde yerleştirin :

Bir uyarı ! Eğer Windows uygulamalarını biraz kullandıysanız, **Copy(Kopyala)** ve **Paste(Yapıştır) **adını verdiğimiz edit özelliklerini de kullanmışsınızdır.

Bu, ikincisini çıkartacağınız**(bir tane daha yapacağınız)** bir şeyi kopyalamak, nereye kopyası çıkarılacaksa oraya gitmek ve buraya yapıştırmaktır. Bu kelime işlemcilerde daima kullanılır.

Keşfetmiş olabilirsiniz, Visual Basic ile çalışırken, kontrolleri kopyalayıp yapıştırabilirsiniz. Bunu, burada yapmayı da çok cazip bulabilirsiniz - yalnızca bir komut butonu oluşturup bunu kopyaladıktan sonra 5 kere daha yapıştırmak gibi kısa ve kolay bir yol varken, niçin 6 kere yeni komut butonu oluşturasınız? Evet, bunu yapabilirsiniz, fakat burada **yapmayın **!

Kontrolleri kopyalamak size farklı tipte bir kontrol verir – bunlardan bir tanesini daha ileri seviye Visual Basic derslerinde göreceksiniz. Bu derslerde ihtiyaç duyduğumuz her kontrolden sadece bir tane oluşturacağız (yani 6 ayrı kontrolü teker teker ve ayrı ayrı oluşturacağız). Daha sonra, daha iyi bir programcı haline geldikten sonra, kontrolleri kopyalayıp sonra yapıştırıldığında ne olduğuna bakacaksınız.

## ***Kontrol Özelliklerini Düzenleme ***

Kontrol özelliklerini, özellikler penceresini kullanarak düzenleyin. Hatırlayın, özellikler penceresinde seçilen bir kontrolü değiştirmek için, ya pencerenin en üstünde bulunan kontrol listesini kullanın veya sadece tercih ettiğiniz kontrolü tıklayın.

Proje kontrol özellikleri için, kontrolleri herzaman **varsayılan değerleri** ile listeleyeceğiz (kontrol, form üzerine yerleştirildiğinde Visual Basic tarafından atanan varsayılan(default) değerler).

**Form1** Form’u:

**Property Name(Özellik İsmi) Property Value(Özellik Değeri)**

Name frmFormFun

Caption Form Fun ***(Form Eğlencesi)*********

**Command1** Command Button(Komut Butonu):

**Property Name(Özellik İsmi) Property Value(Özellik Değeri)**

Name cmdShrink

Caption Shrink Form ***(Formu Küçült)*********

**Command2** Command Button(Komut Butonu):

**Property Name(Özellik İsmi) Property Value(Özellik Değeri)**

Name cmdGrow

Caption Grow Form ***(Formu Büyüt)*********

**Command3** Command Button:

**Property Name Property Value**

Name cmdHide

Caption Hide Buttons ***(Butonları Gizle)*********

**Command4** Command Button:

**Property Name Property Value**

Name cmdRed

Caption Red Form***(Kırmızı Form)*********

**Command5** Command Button:

**Property Name Property Value**

Name cmdBlue

Caption Blue Form***(Mavi Form)*********

**Command6** Command Button:

**Property Name Property Value**

Name cmdShow

Caption Show Buttons ***(Butonları Göster)*********

Visible False

Eğer isterseniz diğer özelliklerini de değiştirebilirsiniz – belki komut butonlarının Font özelliğini değiştirmek isteyebilirsiniz.

Özellikleri düzenledikten sonra, form’unuz aşağıdaki gibi görünmelidir:

Form üzerinde 6 buton bulunmaktadır; ikisi form’un boyutlarını ve diğer iki tanesi ise form’un rengini değiştirmek içindir. Bir tanesi form’u gözden kaybetmek, bir tanesi ise tekrar görünür hale getirmek içindir.

Dikkat edin **Show** **Buttons(Butonları Göster) **komut butonu False değerine sahip bir Visible özelliğine sahiptir. Onun orada form üzerinde ilk olmasını istemiyoruz. Çünkü butonlar halihazırda orada bulunacaklardır. **Hide** **Buttons(Butonları Gizle)** kontrol’ünü tıkladığımızda (onların Visible özelliğini değiştirerek) butonların kaybolmasını ve **Show** **Buttons(Butonları Göster**) butonunu görünür hale getiririz.

Anlamlı, değil mi ?

Fakat , **Show** **Buttons** buton’unun Visible özelliğini False yapmamıza rağmen hala neden orada ? Hatırlayın, False olan Visible özelliği sadece **run** modunda ortaya çıkar.

## ***Olay Prosedürleri Yazmak *********

Form’umuzun üzerinde 6 komut butonu bulunmaktadır. Bu butonlardan herbirisine ait **Click** olay prosedürü için kod yazmamız gerekmektedir. Aynı zamanda form için de bir **Click** olay prosedürü yazmak istiyoruz - neden olduğunu açıklayacağız. Form üzerinde bulunan ve form’u ufaltan bir butonumuz var. Formu o kadar çok ufaltırsak sonuçta yine büyültmek için gerekli butonu bulup tıklayamayız. Bunu önlemek için formu tıklayarak büyütme imkanı veririz. Bu ‘ileride ne olacağını düşünme’ örneği, daha önce hakkında konuştuğumuz proje dizayn kavramlarından birisidir.

Her olay prosedürü için kod penceresini kullanacaksınız. Nesne listesinden kontrolü ve prosedür listesinden olayı seçin. Başlık satırı ve taban satırı arasındaki alanı tıklayın ve kodu yazmaya başlayın. Bu kadar kolay ! Fakat tekrar ediyoruz, her şeyi bu kitapta tarif edildiği gibi yazdığınızdan emin olun, kesin olmak zorundasınız !

İlk olarak, **cmdShrink\_Click** olay prosedürünü yazalım. Bu prosedürde , form yüksekliğini 100 ve form genişliğini de 100 twip azaltacağız :

```vbnet
Private Sub cmdShrink_Click()
'Formu ufalt.
'Formun yüksekligini 100 twip azalt.
frmFormFun.Height = frmFormFun.Height - 100
'Formun genisligini 100 twip azalt.
frmFormFun.Width = frmFormFun.Width - 100
End Sub
```

Diğer olay prosedürlerine geçmeden, bu noktaya biraz daha yakından bakalım. Çünkü üzerinde iyice durmadığımız birkaç fikir kullanılmaktadır. Üzerinde **Shrink** **Form **yazılı olan butonu tıkladığımızda, yerine getirilen olay prosedürü budur. Bu yorum bildirilerinin kolaylıkla farkına varacaksınız. Yorum olmayan bildiriler form yüksekliğini ve genişliğini değiştirir. Height(yükseklik) değerini değiştiren aşağıdaki bildiriye bakın:

```vbnet
frmFormFun.Height = frmFormFun.Height - 100
```

Hatırlayın, atama operatörü nasıl çalışıyor (=) . Sağ taraf önce değerlendirilir. Daha sonra 100 ( - işareti kullanılarak) halihazır form yüksekliğinden çıkarılır. Bu değer ifadenin sol tarafına atanır ( frmFormFun.Height). Sonuç, form Height özelliği, Height değeri eksi 100 twip’dir. Bu kod satırından sonra, Height özelliği 100 azaltılır ve form ekranda daha ufak görünür.

Bu ifade aynı zamanda buna niçin atama operatörü (=) deyip, eşittir işareti demediğimizi de anlatmaktadır. Herhangi bir kimse ifadenin sol tarafını, ifadenin sağ tarafına eşit olamayacağını görebilir. FormFun.Height değeri ne olursa olsun, sağ taraf daima sol taraftan 100 birim daha ufaktır.

Fakat, bu bir eşitlik olmamasına rağmen, doğru olmadığını bile bile, programcıların çoğunlukla bu bildiriyi, “frmFormFun.Height eşittir frmFormFun.Height eksi 100,” şeklinde okuduğunu işitirsiniz ! Kendi programlarınızı yazmaya başlarken, atama bildirilerinin nasıl çalıştığını hatırlayın.

Şimdi, diğer olay prosedürlerine bakalım. **cmdGrow\_Click** prosedürü, form yüksekliğini 100 ve form genişliğini 100 twip arttırır:

```vbnet
Private Sub cmdGrow_Click()
'Formu büyüt
'Form yüksekligini100 twip arttir
frmFormFun.Height = frmFormFun.Height + 100
'Form genisligini 100 twip arttir
frmFormFun.Width = frmFormFun.Width + 100
End Sub
```

**cmdRed\_Click** olay prosedürü form background rengini kırmızıya çevirir:

```vbnet
Private Sub cmdRed_Click()
 'Formu kirmizi yap 
frmFormFun.BackColor = vbRed
End Sub
```

**cmdBlue\_Click** olay prosedürü form background rengini maviye çevirir:

```vbnet
Private Sub cmdBlue_Click()
'Formu mavi yap
frmFormFun.BackColor = vbBlue
End Sub
```

**cmdHide\_Click** olay prosedürü, bütün komut butonlarını gizlemek için kullanılır (**Visible** özelliğini **False **olarak verin) – **cmdShow **istisnadır ve **Visible **olarak ayarlanır:

```vbnet
Private Sub cmdHide_Click()
'cmdShow haricinde butonlari gizle
cmdGrow.Visible = False
cmdShrink.Visible = False
cmdHide.Visible = False
cmdRed.Visible = False
cmdBlue.Visible = False
'cmdShow butonunu göster
cmdShow.Visible = True
End Sub
```

ve **cmdShow\_Click** olayı, bu etkileri tersine çevirmek için kullanılır:

```vbnet
Private Sub cmdShow_Click()
'cmdShow butonu hariç butonlari göster
cmdGrow.Visible = True
cmdShrink.Visible = True
cmdHide.Visible = True
cmdRed.Visible = True
cmdBlue.Visible = True
'cmdShow butonunu gizle
cmdShow.Visible = False
End Sub
```

Son olarak, **Form\_Click** olay prosedürü de aynı zamanda form’u **‘grow’ (büyütmek)** için kullanılır ve bu yüzden **cmdGrow\_Click **ile aynı koda sahiptir:

```vbnet
Private Sub Form_Click()
'formu büyüt
'form yüksekligini 100 twip arttir
frmFormFun.Height = frmFormFun.Height + 100
'Form genisligini 100 twip arttir
frmFormFun.Width = frmFormFun.Width + 100
End Sub
```

Buradaki prosedürün doğru bir prosedür olduğundan emin olun. **Form** kontrolünü seçtiğinizde, görünecek prosedür **Load **olacaktır. Prosedür listesini kullanarak, **Click** olay prosedürüne bakınız. Yeni bir projeyi **saklamak(kaydetmek)** için daha önce anlatılan teknikleri gözden geçirin. Projenizi kaydedin.

Bu prosedürlerin her birisinde neler olduğunu kolaylıkla görebilmelisiniz.

**cmdHide** ve **cmdShow** butonlarının click olaylarında, Visible özelliğinin nasıl kullanıldığına özellikle dikkat edin. Dikkat etmeniz gereken bir başka nokta ise, pek çok olay prosedürünün, bunların kodlamalarına olan sıkı benzerliğidir.

Örnek, **Form\_Click** olayı, **cmdGrow\_Click** olayı ile birebir eşdeğerdir. Bu Visual Basic projelerinde çok rastlanan bir durumdur. Kontrolün yerleştirilmesinden farklı olarak, kod yazarken, **Copy ve Paste** gibi editör özelliklerinin kullanılmasını özellikle tavsiye ediyoruz ! Bir şeyi kopyalamak için; fareyi kullanarak, istenilen yazıyı işaretleyin - aynı şeyi bir kelime işlemcide yapıyorsunuz. Daha sonra, Visual Basic ana menüsünden, **Edit**’i daha sonra da **Copy** ‘yi seçin. Nereye yapıştırmak istiyorsanız,** imleç’i (cursor)**’u oraya götürün.

Diğer olay prosedürlerini de taşıyabilirsiniz. **Edit**’i daha sonra da **Paste**’i seçin.

O da ne ? Kopya göründü. Yapıştırılan yazının bir miktar düzeltilmeye ihtiyacı var. Fakat güzel tarafı, **copy **ve** paste** fonksiyonu kod yazarken çok zaman kazandıracaktır. Bu ise yapmak istediğiniz şeydir. Çünkü, belki farketmişsinizdir, programlama yaparken, böylesi basit bir projede bile, belirli bir miktarda yazıyı klavyeden girme gereği vardır.

Bir diğer faydalı özellik ise **Find(Bul) **ve **Replace(Değiştir) **özelliğidir. Gerektiği zaman bu özelliği de kullanın.

** VB5** ve **VB6** yazı yazma yükünü hafifletecek ve yapabileceğiniz hataları azaltmanız için başka bir yol daha sunar. Eğer Visual Basic ana menüsünde** Tools**, ve daha sonra da

** Options**’ı seçer ve daha sonra burada bulunan **Editor**’ü tıklarsanız burada bulunan **Auto** **List** **Members **adı verilen bir seçeneği görürsünüz. Bu seçenek, eğer kod penceresinde BASIC yazarken seçili ise, belirli bazı noktalarda **ufak kutucuklar aniden ortaya çıkacaktır(pop-up).** Bunlar, üzerinde çalıştığınız bildiriyi mantıksal olarak tamamlayan (bitiren) bilgileri gösterir.

Böylelikle, bundan sonrası için, eksik olan tamamlama bilgisini yazmak yerine kalan kısmı buradan seçebilirsiniz. **VB5** veya **VB6 **kullanıyorsanız, **Auto List Members Option**’ları denemek isteyebilirsiniz. Kullanımı ile ilgili daha fazla bilgiye erişmek için, **on-line help** kullanın.

## ***Projeyi Çalıştırın***

Devam edin ! Projenizi çalıştırın(Run) - Visual Basic toolbar üzerinde bulunan **Start(Başlat) **butonunu tıklayın. Eğer doğru biçimde çalışmıyorsa, bu aşamada tavsiye edilebilecek tek şey, projeyi durdurmak, yazılı olanı tekrar kontrol etmek ve yeniden denemektir. **‘debugging’(hata ayıklama)** tekniklerini diğer derste öğreneceğiz.

Bütün komut butonlarını deneyin. Form’u büyütün, küçültün, form rengini değiştirin, butonları gizleyin, butonları tekrar görünür hale getirin. Bütün butonları denediğinizden ve istediğiniz her türlü çalışmayı yaptığınızdan emin olun. Gerekli yerleri tıklayarak, istediğiniz sonuçları aldığınızdan emin olun. Bu yapılması çok açık ve görünür bir şey gibi gelebilir fakat büyük projelerde, yazdığınız bazı kodlar olacaktır ki bu kodlar asla yerine getirilmeyecektir-çalıştırılmayacaktır(execute) ve hiçbir yolla bu belirli prosedürün doğru çalışıp çalışmayacağını tespit edemeyeceksiniz. Düzgün proje tasarımında başka bir adım, projenizi tam olarak test etmenizdir. Çalıştığınız her olayın hedeflediğiniz gibi çalıştığından emin olun. Projenizi durdurun( Visual Basic toolbar içinden Stop butonunu tıklayın). Eğer bir değişiklik yaptı iseniz, projenizi (Save) saklayın.

## ***Denemeniz Gereken Diğer Bazı Şeyler*********

Bu derslerdeki her proje için, bazı denemeler yapabilmeniz için birtakım değişiklikler konusunda tavsiyelerde bulunacağız. **Shrink** **Form** ve **Grow** **Form** butonlarını, formu ekran etrafında hareket ettirmek üzere değiştirin (Left ve Top özelliklerini kullanın).Daha fazla sayıda kullanılabilir renkleri, formlara uygulamak üzere daha evvel tanımladığımız sembolik sabitlerden yararlanarak kullanın.

**Hide** **Buttons** butonunu öylesine ayarlayın ki, o sadece komut butonlarının

’ Enabled özelliğini False’a çevirsin ( Visible(görünürlük) özelliği değil).

Benzer şekilde **Show** **Buttons** butonunu da modifiye edin (değiştirin).

Özetle,

**Tebrikler!** Şimdi daha karmaşık bir Visual Basic projesini tamamladınız

(en azından birden fazla kontrol vardı). Proje dizaynı hakkında bilgiler edindiniz, projeleri saklamayı, komut butonu kontrollerini, formların detaylarını ve komple bir projenin nasıl yapılandırılacağını artık öğrendiniz.

Şimdi bir proje yapılandırmanın üç adımı ile ilgili olarak artık rahat olmalısınız:

**Kontrollerin yerleşimi, özelliklerin (property) düzenlenmesi ve olay prosedürlerin yazılması.**** **

** ** Bu adımları, ilerleyen derslerimizde, yeni kontroller ve daha fazla BASIC dili kullanarak, diğer projeleri yapılandırmada kullanmaya devam edeceğiz.

## ** PAGE 33**

## *** ****** *****Herkes için ****VISUAL BASIC\_\_\_\_\_\_ **

## \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## *** PROJE DİZAYN’I, FORMLAR ve KOMUT BUTONLARI ***** PAGE 33******

## PAGE 12 PAGE 7

## cmdGrow

## cmdShrink

## cmdHide

## cmdRed

## cmdBlue

## cmdShow

## frmFormFun

Caption

İkon

---
*Kaynak: `HERKES İÇİN VISUAL BASIC/BOLUM-4.DOC` — M. ŞAKİR UNUTUR — 2001*
