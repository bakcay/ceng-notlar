# Toolbox (VB Kontrol Elamanlari)

**10. BÖLÜM**

**TOOLBOX (VB KONTROL ELAMANLARI)**

Formlarda eklenebilecek her kontrol ToolBox penceresinde bir düğme ile temsil edilmektedir. Tasarım anında üzerinde çalıştığımız form veya projeye yeni bir kontrol elamanı eklemek istiyorsak ToolBox menüsü ekranda yoksa View menüzündeki ToolBox seçeneğinden yararlanarak bu pencereği çağırabiliriz.

ToolBox penceresinde seçebileceğimiz her kontrol için bir düğme bulunmaktadır. Üzerinde çalıştığımız forma hangi kontrolü eklemek istiyorsak fare ile ToolBox penceresinden o kontrolü temsil eden düğmeyi tıklayarak düğmeyi seçili duruma getirmeliyiz. Daha sonra formun istediğimiz yerin fare ile işaretlediğimizde kontrolü eklemiş oluruz.

Visual Basıc başlatıldığında TollBox penceresinde toplam 21 düğme bulunmaktadır. Bu 21 düğmeden ok işareti hariç hepsi bir kontrolü temsil etmektedir.

Şekil-10.1. ToolBox Penceresi

ToolBox penceresinde en çok kullanılan kontrollere ait düğmeler bulunmaktadır. Aslında kontrollerin sayısı gösterilenlerden fazladır. Başlangıçta ToolBox penceresinde bir düğme ile temsil edilmeyen kontrolleri kullanabilmek için söz konusu kontrole ait OCX uzantılı dosyanın çalışılan projenin üzerine dahil edilmesi gerekir. Üzerinde çalışılan projeye bir OCX dosyasını eklemek için Project menüsündeki Companets komutundan yararlanmamız gerekir.

Şekil-10.2. Companents Penceresi

Bu pencerede hangi özel kontrolü projeye dahil etmek istiyorsak o özel kontrole ait onay kutusunu seçili duruma getirmemiz gerekir.

Eğer Components diyalog kutusunda yalnızca o ana kadar projeye dahil etmiş olduğunuz OCX uzantılı özel kontrol dosyalarını ve diğer nesnelerin listelenmesini istiyorsanız Selectted Items Only onay kutusunu seçili duruma getirmeniz gerekir.

Bilgisayara kopyalamanıza rağmen Components diyalog kutusunda listelenmeyen özel kontroller varsa Browse düğmesiyle bunları ekleyebilirsiniz.

**10.1. Label Kontrolu (Mesaj Nesnesi)**

Label kontrolü, üzerinde çalışılan forma sabit bir bilgiyi yazmak için kullanılır. ToolBox menüsünden “A” harfi üzerine gelerek fare ile işaretlemelisiniz.

Şekil-10.3. ToolBox Penceresi (Label Kontrolü)

Label kontrol düğmesini seçtikten sonra çalışmakta olduğunuz formun üzerinde kontrolü yerleştireceğiniz alanı mouse ile işaretlediğinizde kontrolü eklemiş olursunuz.

Şekil-10.4. Form Penceresi

**10.1.1.Properties **

O anda seçilmiş olan elaman ait özelliklerin görüntülendiği pencereye Properties adı verilmektedir. Form üzerine alınan bir nesne VB’nin default olarak verdiği bir isimle yerleşir. Kullanıcı bu pencereyle kontrol elamanını kullanabileceği gibi istediği ismi verebilme hakkına sahiptir.

Şekil-10.5. Properties Penceresi

**Caption:**** **Nesnenin üzerindeki yazı bu özellikle belirlenir.

```vbnet
Label1.Caption= “Öğrencinin Adı”
```

** **Caption özelliğinde & karakterinin kullanılması bu karakterden sonraki karakteri kısa yol tuşu yapar.

```vbnet
Label1.Caption= “Öğrencinin &Adı :”
```

Yukarıdaki satır A harfini kısa yol tuşu yapar. Alt+A tuşlarına basılması durumunda klavye kontrolü Tab indexi bir büyük olan elamana bırakır.

**Autosize: **True ise nesnenin boyutları içeriğinin boyutlarına göre yeniden ayarlayacaktır. İçerik değiştiği anda kendiliğinden boyutlarda değişecektir.

**BlackStyle:** Bu özellik nesnenin üzerinde bulunduğu konuma uymasını sağlar. 0 ise üzerinde bulunduğu nesnenin görülmesini sağlar. Yani bir cam üzerine yazılmış yazı gibi davranır. 1 ise kendi zemin rengi üzerinde bulunur ve alttaki nesneyi göstermez.

**10.2. Textbox (Metin Kutusu)**

VB’de bilgi girişleri TextBox nesneleri aracılığı ile yapmaktadır. ToolBox penceresinde TextBox kontrolü işaretlenir.

Şekil-10.6. ToolBox Penceresi (Textbox Kontrolü)

Kontrol düğmesini seçtikten sonra çalışılan form üzerinde mouse ile yeri işaretlenerek kontrol eklenir.

Şekil-10.7. Form Penceresine

**10.2.1. Properties **

**Text :** Text kutusuna girilen metin nesnenin text parametresine atanır. Bu kullanılarak kullanıcının girdiği metin üzerinde işlem yapılır. Text kutusuna text verilmeden sadece ismi kullanılırsa text özelliği kullanılmış olur.

```vbnet
Text.Text= “Elektronik-Bilgisayar Bölümü”

Text1= “Elektronik-Bilgisayar Bölümü”
```

**MultiLine:** True ise text kutusuna birden fazla satır girilebileceğini gösterir. False ise tek satır girilebilir.

**Alignment:** Nesne içerisindeki yazının sola, sağa veya ortaya yazılmasını sağlar. 0 ise sola, 1 ise sağa, 2 ise yazıyı ortaya yaslar.

**ScollBars:** Multiline özelliğinin true olması durumunda etkili olan bu özellik text kutusu içerisinde bu özelliğin aşağı-yukarı sola-sağa kaydırmak için kaydırma çubuklarının eklenmesini sağlar. 0 ise yok, 1 ise yatay, 2 ise dikey ve 3 ise hem yatay hem de dikey.

**MaxLenght:** Text kutusuna girilebilecek maksimum karakter sayısını belirler. Buna 0 verilirse üst sınır 32 karakter olur.

**PaswordChar :**** **Text kutusuna şifre girmek için kullanılır. Yani kullanıcı girdiği karakterlerin ekranda görülmesini istemiyorsa bu özellikten yararlanır. **PasswordChar** özelliğine karakter girerek kullanıcının girdiği bütün karakterlerin bu karakterle görülmesini sağlar.

**Locked:** Text kutusunun bu özelliği True yapılırsa Text üzerinde hiçbir değişiklik yapılamaz.

Örnek olarak bir şifre programı yazalım.

```vbnet
Private Sub Form_Load()
If InputBox(“Şifreyi Giriniz”)<>”bahadır” Then
MsgBox(“Bilemediniz”)
Text1.Locked=True
End If
End Sub
```

**10.3. Command Button (Komut Düğmesi)******

Windows uyumlu programlarda karşımıza sık sık bazı uyarılar gelmektedir. Bu uyarılarla birlikte diyalog kutuları gelerek butonlarla senekler sunulmaktadır. Bu sunulan butonlara basıldığında üzerinde yazılan görevi yerine getirir. İşte VB’de böyle bir buton atamak için Command Button düğmesinden yararlanılır.

Şekil-10.8. ToolBox Penceresi (Command Kontrolü)

Toolbox penceresinde bu düğme işaretlendikten sonra, çalışılan form üzerinde konulacak yer işaretlendiğinde eklenmiş olur.

Şekil-10.9. Form Penceresi

**10.3.1. Properties **

**Caption :** Komut düğmesi üzerinde yazılacak mesajı içerir.

```vbnet
Command1.Caption= “Çıkış”
```

**Style:** Bu özellik komut düğmesinin yazılımının resimli olacağını belirtir. 0 ise komut düğmesi üzerinde Caption özelliği ile belirtilen yazı bulunur. 1 ise picture özelliği ile belirtilen resim bulunur.

**Picture, DisabledPicture, DownPicture:**** **Eğer komut düğmesinin Style özelliği 1 verilerek resimli bir komut düğmesi olacağı belirtilmişse bu üç özellikle komut düğmesinin üzerinde bulunacak resim belirlenebilir.

Picture özelliği ile belirlenen resim komut düğmesinin aktif (Enabled özelliği True)iken, DisabledPicture özelliği ile belirlenen resim komut düğmesinin pasif (Enabled özelliği False) iken, DownPicture özelliği ile de komut düğmesinin basılı iken gösterilecek resim belirlenir.

**Default:** Komut düğmesinin default özelliği True ise o düğmenin bulunduğu form üzerinde Enter’e basılması durumunda o düğme tıklanmış olur.

**Cancel:**** **Bu özellik de default özelliği gibidir ancak ESC tuşu ile aktif hale gelir.

**10.3.2. Events()**

Command Button’da click olayına boşluk tuşu, Enter, Kısayol tuşu ve mouse tıklaması meydana getirir. Düğmenin temsil ettiği işi yapmasını sağlayacak program bu alt programa yazılır.

**10.4. CheckBox (İşaret Kutusu)**

Kullanıcının belirli özelliği aktif veya pasif hale getirmesi için kullandığı kontroldür. ToolBox penceresinde bu kontrol işaretlenir.

Şekil-10.10. ToolBox Penceresi (CheckBox Kontrolü)

Komut düğmesi işaretlendikten sonra üzerinde çalışılan formun istenilen yerin işaretleyerek düğmeği ekleriz.

Şekil-10.11. Form Penceresi

**10.4.1. Properties**

**Alignment:** 0 ise işaret solda, 1 ise sağda görülür.

**Valume:** ikisi kullanıcı tarafından değiştirilebilen 3 değer atanabilir. 0 ise işaretsiz, 1 ise işaretli, 2 ise belirsiz.

**10.5. Horizontal Bar (Yatay Kaydırma Çubuğu)**

Belgenin sağına veya soluna gitmek için kullanılır. ToolBox penceresinden komut düğmesi işaretlenir.

Şekil-10.12. ToolBox Penceresi ( HorizontalBar Kontrolü)

Üzerinde çalışılan formun istenilen alanı işaretlenerek eklenir.

10.12. Form Penceresi

**10.5.1. Properties **

**Volue:** kaydırma çubuğunun temsil ettiği değeri gösterir. Bu değer maksimum ile minimum arasında bir sayıdır ve kaydırma çubuğu üzerinde değişik şekillerde değiştirilebilir.

Kaydırma çubuğunun uçlarındaki iki ok ile azaltılıp, çoğaltılabilir. Bu olay **smallchange **olarak adlandırılır.

Direkt kaydırma çubuğu üzerine mouse ile tıklanarak değer artırılıp, azaltılabilir. Bu olay **largechange** olarak adlandırılır.

Kaydırma çubuğunun üzerindeki kaydırma çubuğu üzerinde hareket eden kutucuk mouse ile istenen konuma getirilerek değer azaltılıp, çoğaltılabilir. Bu olaya da **scrollchange **olarak adlandırılabilir.

**Max-Min****:** Kaydırma çubuğunun alabileceği maksimum ve minimum değerdir.

**LargeChange:** Kaydırma çubuğu üzerine tıklanması durumunda **scroll.value**’nin ne kadar bir değişime tabi tutulacağını belirler.

**SmallChange:** Kaydırma çubuğunun iki kenarındaki oklarla **scroll.value**’nin ne kadar bir değişime tabi tutulacağını belirler.

**10.5.2. Events ()**

**Changer() :** Kaydırma çubuğunun Value’sini değişmesi change olayını meydana getirir. Max ve Min değerlerinin değişmesi normal de bu olayı meydana getirmez. Ancak Max ve Min değeri değiştirildiğinde Value bu sınırlar dışında kalıyorsa Value değeri kendiliğinden bu sınır içine alınacaktır. Dolayısıyla Change olayı meydana gelecektir.

**10.6. Vertical Scroll Bar (Düşey Kaydırma Çubuğu)******

Belgenin aşağısına veya yukarısına gitmek için kullanılır. Diğer özellikleri Horizontal Bar (Yatay Kaydırma Çubuğu) ile aynıdır.

**10.7. Timer Control (Zamanlayıcı)**

Proje çalışması sırasında bazı işlemlerin belirli zaman aralıklarında tekrarlanması gerekir. Bu gibi işlemlerde Timer denetiminden yararlanılır. ToolBox penceresinde Timer Butonu seçilir.

Şekil-10.13. ToolBox Penceresi (Timer Kontrolü)

Daha sonra çalışılan form üzerinde istenilen alan işaretlenerek nesne eklenir.

10.14. Form Penceresi

**10.7.1. Properties **

**Enabled:** False verilerek nesnenin çalışması durdurulur. Tekrar True yapılıncaya kadar Timer olayı meydana gelmez.

**Interval:** Timer olayının gerçekleşeceği milisaniye cinsinden zaman periyodudur. Alabileceği değerler 1-65535 arasıdır. 0 değeri Timer’i pasif hale getirir.

**10.7.2. Events**

**Timer ():**Timer kontrolünün interval özelliği ile belirtilen süre içinde periyodik olarak bu olay meydana gelir. Bu olay içerisinde yazılacak kodun hızlı olması gerekir. Bu olay periyodik olarak sürekli meydana geleceği için bu olay içerisine yazılan kodun uzun olması Windows altında çalışan diğer programlarında yavaşlamasına sebep olacaktır.

**Örnek 10.1 :**

```vbnet
Private Sub Timer1_Timer()
Form1.Caption= “Saat:” +Time
End Sub
```

**10.8. Frame Control (Çerçeve)******

Bazı kontrolleri gruplamak için kullanılan kontroldür. Bu çerçeveler içine konan çerçeveler, çerçeveye bağımlıdırlar. Konumları bu çerçeve dışına taşamaz. Özellikle birkaç kontrolü birden görünür veya görünmez yapmak için hepsinin Visible özelliğini tek tek değiştirmek yerine çerçeve içindeki tüm kontroller aynı anda görünmez yapılabilir. ToolBox penceresinden bu kontrol düğmesi işaretlenir.

Şekil-10.15. ToolBox Penceresi (Frame Kontrolü)

Toolbox penceresinden nesneyi seçtikten sonra çalışılan form üzerine gelinerek istenilen alan işaretlenerek nesne yerleştirilir.

Şekil-10.16. Form Penceresi

**10.9. Optional Button Control (Seçenek Düğmesi)******

Birkaç seçenekten birini seçmemizi yarayan bir kontroldür. Birkaç seçenekten birini seçme imkanı veren bir komut olduğu için en az iki tane birlikte kullanılmalıdır. Gruptaki Optional düğmelerinden biri seçildiğinde diğeri kendiliğinden seçilmiş özelliğini kaldırır. ToolBox penceresinden bu kontrol seçilir.

Şekil-10.17. ToolBox Penceresi (Optional Button Kontrolü)

Çalışma sayfasının istenilen alanı işaretlenerek yerleştirilir. Dikkat edilecek nokta, birden fazla kullanılmalıdır.

Şekil-10.18. Form Penceresi

**10.9.1. Properties **

**Value: **True olması optial butonunun seçilmiş olduğunu gösterir.

**10.10. Shape Control (Şekil Kontrol Elamanı)**

** **Bu grafiksel bir kontrol elamanıdır. Dikdörtgen, kare, elips, çember, oval ve oval dikdörtgen şekillerini oluşturmaya yarar. ToolBox penceresinden kontrol elamanı seçilir.

Şekil-10.19. ToolBox Penceresi (Shape Kontrolü)

Daha sonra çalışılan form üzerinde istenilen alan belirlenerek kontrol elamanı yerleştirilir.

Şekil-10.20. Form Penceresi

**10.10.1. Properties**

**BorderStyle:** Bu özellikle nesnenin çerçeve biçimini belirler.

**BorderWidth:** Bu özellik Line, Shape kontrol elamanlarının çerçeve kalınlığını ifade eder.

**Shape:** Shape kontrol elamanının çizeceği şekli belirler.

**10.11. Line (Çizgi Kontrol Elamanı)******

Bu kontrol elamanı form üzerine çizgi çizmek için kullanılır. Alınan bu çizgiyi yatay, dikey ve eğik bir biçimde göstermek mümkündür.

ToolBox penceresinden kontrol elamanı seçilir.

Şekil-10.21. ToolBox Penceresi (Line Kontrolü)

Kontrol elamanı seçildikten sonra çalışılan form üzerinde başlangıç noktası belirlenerek istenilen uzunlukta ve istenilen biçimde çizgi çizilir.

Şekil-10.22. Form Penceresi

**10.11.1. Properties**

**X1,X2,Y1,Y2****:** X1 ve Y1 noktaları çizgi kontrol elamanının başlangıç koordinatlarını, X2 ve Y2 ise bitiş koordinatları belirlenir. Yatay kontrolleri X1 ve X2, Dikey kontrolleri ise Y1 ve Y2 belirler.

**10.12. PitureBox (Resim Kutusu)**

Bu kontrol elamanı Bitmap, Icon, Metafile, Jpeg ve Gif gibi resimleri görüntülemek için kullanılır. Ayrıca metodlar kullanılarak PictureBox içine çizimlerde yapılabilmektedir. Bu kontrolün bir özelliği de Frame kontrolü gibi değer kontrolleri gruplayabilir. ToolBox penceresinde kontrol elamanı seçilir.

Şekil-10.23. ToolBox Penceresi (PictureBox Kontrolü)

Çalışılan form üzerinde resmin ekleneceği alan işaretlenir. Gerekli komut satırı yazılarak resim eklenir.

Şekil-10.24. Form Penceresi

**10.12.1. Properties**

**Picture:** Bu özellik kontrol içinde görüntülenecek icon, metafile ve bitmap tipi resimleri görüntülemeye yarar.

Nesneye bu özellik kullanarak resim yüklenmesi;

LoadPicture ile dosyadan

```vbnet
Picture1.Picture=LoadPicture(“\resimler\park.jpg”)
```

Başka bir nesnenin picture özelliğinden

```vbnet
Picture1.Picture=Picture2.Picture
```

Clipboard dan yapılabilir

```vbnet
Picture1.Picture=Clipboard.Getdata()
```

**Image:** Bu özellik sadece okunabilir bir özelliktir. Picture kontrolü içine methods’lar kullanılarak yapılan yazım ve çizimleri temsil eder.

```vbnet
Picture1.Circle(0,0),150
Picture2.Picture=Picture1.Image
```

Yukarıdaki satırlarla, Picture1 ile bir daire çizilmiş ve picture2 ile nesne üzerinde gösterilmesi sağlanmıştır.

**AutoRedraw:** Bu özellik aldığı True veya False değerleri ile nesnenin kendini otomatik olarak yenilemesini ya da yenilememesini sağlar.

**10.13. Image (Resim Gösterme Kontrolü)******

Bu kontrol grafiksel bir kontrol olup resimleri görüntülemek, boyutlandırmak ve taşımak için kullanılır. Bu kontrol elamanı PictureBoxtan farklı olarak gruplandırma yapamaz ve metodları kullanarak yazım ve çizim yapamaz.

**10.14. ComboBox (Açılan Liste)**

** **Aşağı doğru açılan bir liste kontrolüdür. Genellikle değerleri daha önce belli olan elamanların seçimi için kullanılır. Listele işlemi ilk olarak kapalı bir şekilde gelir. Yan taraftaki ok işaretine basılarak diğer listelenen seçenekler görülebilir. Bu kontrolü eklemek için ilk önce ToolBox penceresinden kontrol işaretlenir.

Şekil-10.25. ToolBox Penceresi (PictureBox Kontrolü)

Formun üzerinde istenilen alan mouse ile işaretlenerek kontrol yerleştirilir.

Şekil-10.26. Form Penceresi

**10.14.1. Properties**

**Style:** ComboBox kontrolünün tipini belirler. 0,1,2 değerlerinden birini alır. 0 değeri alırsa aşağı doğru açılan ve içeriği kullanıcı tarafından değiştirilebilen, 1 değerini alırsa aşağı doğru açılmayan fakat kullanıcı tarafından içeriği değiştirilebilen 2 değerini alırsa aşağı doğru açılan fakat kullanıcı tarafından giriş yapılamayan ComboBox oluşturur.

**Text:** ComboBox kutusunda aktif olan yazıyı gösterir.

Örnek olarak içerisinde beş tane ismin bulunduğu bir ComboBox nesnesi oluşturalım.

İlk önce ToolBox penceresinde kontrolü işaretleyip formun üzerine ComboBox nesnesini yerleştirelim. Daha sonra ComboBox nesnesinin üzerini mouse ile çift tıklayarak komut penceresine aşağıdaki satırları yazalım.

```vbnet
Private Sub Combo1_Change()
Combo1.AddItem "Bahadır"
Combo1.AddItem "Metin"
Combo1.AddItem "Musa"
Combo1.AddItem "Dinçer"
Combo1.AddItem "Ümit"
End Sub
```

Programın çalıştırdığımızda çıktısı aşağıdaki gibi olur.

**10.15. Drive List Box (Sürücü Listeleme Kutusu)**

Sistemde bulunan sürücüleri listelemeye yarar. Bu kontrol elamanı sürücüğe geçişi sağlayamaz. ToolBox penceresinden kontrol elamanı mouse yardımıyla seçilir.

Şekil-10.27. ToolBox Penceresi (Drive List Box Kontrolü)

Formda istenilen yer işaretlenerek kontrol eklenir.

Şekil-10.28. Form Pencerei

**10.15.1 Properties**

**Drive:** Kontrolün gösterdiği aktif sürücü öğrenilebilir veya değiştirilebilir.

**10.15.2. Events()**

**Change(**)**: **Kontrolden bir sürücü seçilmişse bu olay meydana gelir.

```vbnet
Sub Drive1_Change()
Dir1.Path=Drive1.Drive
ChDrive Drive1.Drive
End Sub
```

**10.16. Directory List Box (Dizin Listeleme Kutusu)**

Bilgisayarsa bulunan sürücülerdeki dizinleri listelemeye yarayan kontroldür. Bu kontrol elamanı vasıtasıyla Path özelliği ile seçilmiş sürücüdeki dizinler seçilebilir. ToolBox menüsünden Mouse yardımıyla kontrol seçilir.

Şekil-10.29. ToolBox Penceresi (Directory List Box Kontrolü)

Çalışılan formun üzerinde istenilen alan işaretlenerek kontrol forma dahil edilir.

Şekil-10.30. Form Penceresi

Dizini seçme işlemi aktif dizinin değişmesine sebep olmaz. Bu işi ChDir gibi bir komutla yapılası gerekir.

**10.16.1. Properties**

**Path:** Bu özellik kullanılarak kontrol ile seçilmiş olan dizin öğrenilebilir ve değiştirilebilir. Bu kontrolden dönen değer sürücü ismi dahil tam yoldur.

**10.16.2. Events ()**

**Change():** Listeden bir dizin seçilmesiyle bu olay meydana gelir. Dizin seçimi yapıldığında yazılması gereken kod buraya yazılmalıdır.

```vbnet
Sub Dir_Change()
File1.Path=Dir1.Path
ChDir Dir1.Path
End Sub
```

**10.17. FileList Box (Dizin Listeleme)**

Herhangi bir dizindeki dosyaları listelemeye yarayan kontrol elamanıdır. Bu kontrol elamanı vasıtasıyla path özelliği ile belirlenmiş dizindeki dosyalar listelenir. ToolBox penceresinden kontrol seçilir.

Şekil-10.31. ToolBox Penceresi (PictureBox Kontrolü)

Çalışılan formun üzerinde istenilen alan seçilerek kontrol elamanı forma dahil edilir.

Şekil-10.32. Form Penceresi

**10.17.1. Properties**

**FileName:** Bu özellik ile seçili dosyanın ismi öğrenilebilir.

**Archive,Hidden,Normal,ReadOnly,System:** Bu özellik kullanılarak dosya listeleme kutusundaki Arşiv, Saklı, Sadece Okunu, Normal ve system özelliklerine sahip dosyaların görüntülenmesini sağlar. Bu özelliklerden herhangi birine True değeri o özelliğe sahip dosyalar listelenir.

**Pattern:** Bu özellikle listelenmek istenen dosyalar filtrelenir. Bu işlem (*,?) gibi joker karakterlerle yapılır.

```vbnet
File1.Patern=”*.EXE”
```

**10.17.2. Events ()**

**PathChange():** Bu özellik Path özelliğinin değiştirilmesi sonucu meydana gelir. Yani FileBox farklı bir yeri göstermeye başladığında meydana gelir.

**PatternChange(): **Bu olay Pattern özelliğinin değiştirilmesinde meydana gelir.

**10.18. Common Dialog (Diyalog Penceresi)**

Windpws tarafından sağlanan standart diyalog kutularını kullanımını sağlayan kontroldür. Bu kutular “Aç”, “yeni Adla Kaydet”, “Renk”, “Help”, “Yazdır” ve “Font” dur. ToolBox penceresinden ilgili kontrol seçilir.

Şekil-10.33. ToolBox Penceresi (PictureBox Kontrolü)

Formda istenilen alan seçilerek kontrol eklenir.

Şekil-10.34. Form Penceresi

Form üzerinde kontrolleri istediğim büyüklükte ayarlayabiliyorduk. Bu kontrolde böyle bir imkan yoktur. Büyüklüğü sahiptir. Çalışma anında Common Dialog kutusu formun üzerinde görünmez.

**10.18.1. Properties**

**Action:** 1 ile 6 arası değer verilerek ilgili diyalog kutusu açılır.

1: Aç

```vbnet
CommonDialog1.Action=1
```

veya

```vbnet
CommonDialog1.ShowOpen

Private Sub Form_Click()
CommonDialog1.ShowOpen
End Sub
```

2: Yeni Adla Kaydet

```vbnet
CommonDialog1.Action=2
```

veya

```vbnet
CommonDialog1.ShowSave
```

3: Renk

```vbnet
CommonDialog1.Action=3
```

veya

```vbnet
CommonDialog1.ShowColor
```

4: Font

```vbnet
CommonDialog1.Action=4
```

veya

```vbnet
CommonDialog1.ShowFont
```

5: Yazdır

```vbnet
CommonDialog1.Action=5
```

veya

```vbnet
CommonDialog1.ShowPrint
```

6:Windows Help programını çalıştır.

```vbnet
CommonDialog1.Action=6
```

veya

```vbnet
CommonDialog1.ShowHelp
```

**CancelError:** Diyalog pencerelerinde “İptal” düğmesinin seçilmesi halinde yakalanabilir bir hata oluşturup oluşturmayacağı bu özellikle belirlenir. Değer True ise “İptal” düğmesi seçildiğinde hata oluşturur, False ise oluşturmaz.

**Dialog Title**: Açılacak pencerenin başlığında yazılması istenen metni belirler.

**10.19. Film Klib Kontrolü**

Visual basic projeleri dahilinde Multimedia kontrolü sayesinde müzik CD’lerini, MID ve WAV uzantılıses dosyalarını çalabilir, AVI formatındaki video görüntü dosyalarını oynatabilirsiniz. Visual Basic projeleri dahilinde Windows ile birlikte verilen Medya Player programından yararlanabilirsiniz.

AVI uzantılı dosyalarla çalıştırabilmek için Film Klibi kontrolünü ToolBox penceresine atalım. Companents diyalog kutusundaki Insert Object sekmesinde Visual basic projeleri dahilinde kullanabileceğimiz nesneler bulunmaktaydı. Bu pencereden Film Klibi kontrolünü işaretleyip Toolbox penceresine dahil edelim.

Şekil-10.35. ToolBox Penceresi (Film Klibi Kontrolü)

Şimdi form üzerine bu kontrolü mouse yardımıyla yerleştirelim.

Şekil-10.36. Film Klibi Kontrolünün Forma Eklenmesi

Yukarıdaki şekilde de görüldüğü gibi kontrol yerleştirildiği an Ortam Yürütücü programını çalıştırmış gibi ekrana direkt gelmektedir. Bu arada forma yerleştirdiğiniz Film Klibi nesnesinin boyutunu değiştiremezsiniz. Forma yerleştirmiş olduğumuz Film Klibi kontrolüyle çalıştıracağımız AVI uzantılı dosya belli ise Ortam Yürütücüsü penceresinin dosya menüsünden Aç komutunu verip dosya seçimi yapılabilir. Aç komutunu verirsek ekrana dosya isimlerini gösteren Aç diyalog kutusu gelir.

10.37. Aç Diyalog Penceresi

Aç diyalog kutusundan dosya seçimi yapıp Aç düğmesine tıklama yaparak kapatınca masaüstü ve Form aşağıda verilen şekildeki gibi ekrana gelir.

Şekil-10.38. AVI Dosyasının Oynatılması

Ortam Yürütücüsünden yararlanarak seçtiğimiz video dosyasını oynatabiliriz. Ayrıca program çalıştırdıktan sonra kontrolün üzerini çift tıklayarak AVI uzantılı dosya çalıştırılabilir.

**10.20. MultiMedia Kontrolü**

VB projeleri dahilinde Windows ile birlikte verilen Ortam yürütücüsü uygulamasından yararlanmadan (10.19) da örnek olması için anlattığımız işlemleri **MultiMedia** kontrolünden yararlanarak gerçekleştirebiliriz. Multimedia kontrolü ToolBox penceresinde bir düğme ile temsil edilmediği için Components diyalog penceresinden eklememiz gerekmektedir.

Components diyalog kutusunda Multimedia Control onay kutusunu seçip Tamam düğmesini tıklayınca Multimedia kontrolünü temsil eden ToolBox penceresine dahil edelim.

Şekil-10.40. ToolBox Penceresi (Multimedia Kontrolü)

Multimedia kontrolü seçiliyken mouse ile formun üzerine yarleştirelim.

Şekil-10.41. Form Penceresi

Multimedia nesnesinden hangi amaçla yararlanılacağı MultiMedia nesnesine ait Properties penceresindeki Device Type özelliği ile belirlenmektedir. Şimdi müzik CD’si çalmaya çalışalım.

Şekil-10.42. Properties Penceresi

Forma eklediğimiz Multimedia nesnesinden müzik CD’lerini çalmak için Command özelliğinden de yararlanmak gerekir. Command özelliğine o işlemle ilgili komutu aktarmamız gerekir. Command özelliğine Open komutunu aktaracak olursak forma eklemiş olduğumuz Muldimedia nesnesi aktive edilir.

```vbnet
Private Sub Form_Load()
MMControl1.Command= “Open”
End Sub
```

Bu satırı ekledikten sonra programı çalıştıralım.

Artık müzik CD’sini çalmaya başlayabiliriz.

**10.20.1.Ses Dosyalarını Seslendirmek**

Programcı hazırladığı program hakkında yardım dosyası hazırlamanın yanında programını konuşarak anlatır ve WAV uzantılı bir ses dosyasına kaydedebilir.

Şimdi bu işlemin nasıl yapılacağı hakkında bilgi verelim. Üzerine çalıştığımız projenin formuna bir Multimedia kontrolü ekleyelim. Daha sonra forma yerleştirdiğimiz Multimedia kontrolünün bütün düğmelerini properties penceresinden yararlanarak formun üzerinde görünmelerini engelleyelim. Bunun için properties penceresinden BlackVisible,Enabled Visible, Next Visible, Pause Visible, Play Visible, Prev Visible, Recad Visible, Stop Visible, Eject Visible değerlerine FALSE yapalım.

Forma Anlat isminde iki tane Command Butonu atayalım. Bu buton bir bizim ses dosyamızın çalışmasını sağlayacaktır. Diğeri bu işlemi sonlandıracak.

Forma yerleştirdiğimiz MultiMedia DeviceType özelliğine WaveAudio bilgisini aktarmak ve Formdaki düğmeye (Anlat) tıklama yapıldığında seslendirilecek WaV uzantılı ses dosyasının adını FileName özelliğini aktarmak aşağıdaki progman satırlarını yazalım.

```vbnet
Private Sub Command1_Click()
MMControl1.DeviceType = “WaveAudio”
MMControl1.filename= “c:\Windows\media\ctmelody.Wav”
MMControl1.Command = “Open”
MMControl1.Command = “Play”
End Sub
```

İkinci (Durdur) kontrolüne de aşağıdaki satırı yazalım

```vbnet
Private Sub Command2_Click()
MMControl1.Command = “close”
End Sub
```

Artık Programımızı çalıştırabiliriz.

**10.21. Formlar**

Windows arabiriminin en temel kontrolü formlaradır. Windows’ta hemen hemen her program formlar üzerinde çalışır. Boyutlandırılabilir özelliği sayesinde aynı anda ekranda tek bir program olmak zorunda değildir.

Formun Propertieslerini formun alt programlarında yazarken formun ismi yazılmak zorunda değildir. Direkt olarak Properties ismini vermemiz yeterlidir (Captionform1).

**10.21.1. Properties**

**Caption :** Formun başlığında yazılacak yazıyı belirler.

**Icon :** Formu tanıtacak iconu belirler. Bu ikon form minimize edildiğinde veya Alt+tab geçişlerinde formu temsil eder.

**BorderStyle :** Formun çerçeve şeklini belirleyen bu özellik formun boyutlarının değiştirilmesini veya kapatılabilmesini vereceğimiz değerlerle engelleyebilir. Bu değerler şunlardır:

**0:vbBSNone:** Çerçevesi, başlığı, kontrol kutusu, ekranı kapla, simge durumunu küçült düğmeleri olmayan bir form oluşturur.

**1:vbFixedSingle: ** Boyutları değiştirilmeyen, fakat konumu kullanıcı tarafından değiştirilebilen bir form oluşturur.

**2:vbSizable:** Formun bütün özelliklerini sunabilir.

**3:vbFixedDouble:** Form kullanıcı tarafından boyutlandırılamaz.

**4:vbFixedToolWindow :** Normal forma göre başlığı daha küçük olan, kontrol menüsü olmayan ve boyutlandırılamayan bir form oluşturur.

**5:vbSizable ToolWindow:** 4 değerindeki gibi bir form oluşturulur. Farklı olarak bu pencerenin boyutları değiştirilebilir.

**MaxButton, MinButton:** Formun sağ üst köşesindeki maksimize veya minimize düğmelerinin görüntülenmesini veya görüntülenmemesini sağlar.

**ControlBox:** Formun sol üst köşesindeki kontrol kutusunun görüntülenmesini veya görüntülenmemesini sağlar.

**WhatsThisButton:** Form üzerinde ? düğmesinin bulunmasını sağlar. Form üzerinde bu düğmenin bulunabilmesi için;

ControlBox özelliği Ture

BorderStyle özelliği Fixed Single, Sizable veya Fixed Dialog

MinButton ve MaxButton özellikleri False

**Moveable:** Bu özellik formun kullanıcı tarafından taşınıp taşınamayacağını belirler.

**ShowInTaskbar: **Bu özellik formun Windows görev çubuğunda yer alıp almayacağını belirler.

**AutoRedraw:** Bu özellik False ise form üzerinde başka bir form geldiğinde veya form boyutlandırıldığında form üzerine yapılan yazım ve çizimler yenilenmeyecektir. True ise form boyutlandırılırken veya üzerine kapatılırken formun içeriyi kaydedilerek formun içeriğinin kaybolmasını önleyecektir.

**FillColor, FillStyle:** Circle ve Line metodu ile form üzerine çizilen çember ve kutuların iç boyama rengini ve desenini belirler.

**FontTransparent:** True ise form üzerine Print komutu ile yaılacak yazıların zemin rengi yoktur. Dolayısıyla yazı altında resim veya başka bir yazı varsa bunu gösterecektir.

**WindowState:** Formun çalışması üç şekilde olur. Bu7 durumlar WindowState özelliği ile belirlenir.

**0:vbNormal: **Normal, ekranın herhangi bir kısmında pencere içinde.

** 1:vbMininized:** Simge durumunda.

** 2:vbMaximized: **Ekranın tamamını kaplayacak şekilde.

**StartupPosition:** Form yüklenirken ekrandaki koordinatlarının neye göre belirleneceğini bu özellik etkiler.

0: Form tasarlanırken bulunduğu koordinatlarda açılır.

1: Form içinde bulunduğu formun ortasında açılır.(MDI Child

formlar için)

2: Form ekranın ortasında açılır.

3: Formun koordinatları Windows tarafından belirlenir.

**KeyPriew:** Form aktifken basılan tuşlardan formun haberdar edilip edilmeyeceğini belirler.

**False :** Herhangi bir kontrol üzerinde iken basılan tuşlar yalnız o kontrolün KeyPress, KeyDown, KeyUp olaylarını meydana getirir.

**True: **Her hangi bir kontrol üzerinde basılan tuşlar önce Form’un daha sonra o kontrolün KeyPress, KeyDown, KeyUp olaylarını da meydana getirir.

Örneğin ESC tuşuna basıldığında programın kapanmasını istiyorsak bu özelliği True yapıp Formun Keypress olayına aşağıdaki komut satırını yazmamız gerekir.

```vbnet
if KeyAcii=27 Then End
```

**Count:** Formun içindeki menüler dahil kontrol sayısını verir.

**ActiveControl:** Form üzerinde aktif kontrolün ismi gibi davranır.

**Örnek 10.1: **

```vbnet
form1.ActiveControl.Left=0
```

satırı form üzerindeki aktif kontrolü sağlar.

Burada aktif kontrol TexBox ise bu satır;

```vbnet
form1.TextBox.Left=0
```

ListBox ise;

```vbnet
Form1.ListBox.Left=0
```

**Picture:** Form üzerinde gösterilecek resmi belirler. Formun properties penceresinde Picture seçeneği işaretlendiğinde, bu seçeneğin karşısında üç nokta çıkar.

Şekil-10.43. Properties Penceresi

Bu üç nokta tıklandığında Load Picture penceresi açılır.

Şekil-10.44. Load Picture Penceresi

Bu pencerede istenilen resim dosyası işaretlenerek “Aç” düğmesi mouse ile tıklanarak dosya forma yerleştirilir.

**Image:** Formun AutoRedraw özelliği True ise form üzerine yapılan yazım ve çizimlerin kaybolmadığından bahsetmiştik. Formun AutoRedraw özelliği True ise form üzerine yapılan çizim ve yazımlar Formun Image özelliğine kaydedilebilir. Bu özellik yalınız okunabilir bir özelliktir. Eğer form üzeri kaydetmek, panoya kopyalamak veya başka bir kontrol için göstermek istiyorsak bu özellik kullanılır.

**MDIChild:** Windows’un formlara verilebildiği diğer bir özellik de form içinde form oluşturulabilmesidir. Programımızda bir MDI form varsa diğer formların MDIChild özelliğini True yaparak Child formlar oluşturulur.

**hDC:** Windows altında oluşturulan kontrollerin birer handle numarası vardır. Windows kontrollere bu numarayla ulaşır. Visula Basic’te bu numaralar hWnd özelliği ile öğrenilebilir. hDC numarası da bir handle numarasıdır. Fakat özel bir numaradır. Bu numarada Windows uygulamaları ile Device Driver (birim sürücüleri) arasında bir bağlantı kurar. bU numarada hWnd özelliği gibi API’lerle kullanılır.

**CurrentX, CurrentY:** Form üzerine yazılan başlangıç noktası olmayan çizim ve yazımlar aktif pixelin bulunduğu bölgeden başlar. Bu aktif pixelin x ve y koordinatlarını CurrentX ve CurrentY özellikleriyle belirlenir. Özellikle form üzerine yazdığımız Print modu ile yazılarda bu özellik yazının koordinatlarını belirler.

**Örnek** **10.2**:

```vbnet
Pirvate Sub Form_Load()
Show
Dim a,b
a= “Elektronik-Bilgisayar Bölümü”
FontName= “Arial”
For b=1 To 10
Fonsize=b*3
CurrentX=(ScaleWidth-TextWidth(a)/2
Print a
Next
End Sub
```

Programın çıktısı.

**10.21.2. Events**

**Loda()**: Form ilk defa belleğe yüklenirken bu olay meydana gelir. Formun Visible özelliği ile gizlenip tekrar gösterilmesi bu olayı meydana getirmez. Çünkü form bellektedir. Programımızda birden çok form varsa program çalışmaya başladığında sadece ana form belleğe yüklenir. Diğer formları yazacağımız kodlarla bizim yüklememiz gerekmektedir. Formlar aşağıdaki şekilde belleğe yüklenir ve Load olayları meydana gelir.

Load Formismi ile form direk olarak belleğe yüklenir. Ancak kontrolü ele almaz.

Formadı.Show ile form belleğe yüklenir ve görüntülenir.

O anda bellekte olmayan formla ilgili bir koda rastlandığında o form belleğe yüklenir ve daha sonra işlem görür.

**Örnek 10.3:**

```vbnet
Form2.Text1.Text= “12”
```

Yukarıdaki satırla Form2’nin yüklenmesini, dolayısıyla Form2’nin Load olayının çalışmasını ve Text1 kontrolüne “12” atamasının yapılaması sağlanacaktır.

**Activate(), Deactivate ():** Programımızda birden fazla form varsa, aynı anda sadece biri aktiftir. Aktivitenin programdaki formlardan diğerine geçmesi durumunda aktiviteyi kaybeden formun, Deactivate olayı, aktif olan formun da Activate olayı meydana gelir.

**Unload (Cancel As Integer): ** Form herhangi bir şekilde kapanırken bu olay meydana gelir. Bu olaya yazacağımız kodla form kapanmadan önce yapılması gereken işleri yapabiliriz. Ayrıca Cancel=True yazarsak formun kapatılmasını önleyebiliriz. Formun Unload olayı şu hallerde meydana gelir.

Formun sol üst köşesindeki kontrol kutusunda “kapat” seçildiğinde,

Windows görev yöneticisinden “Göreve son ver” düğmesi seçilmesiyle,

Windows’tan çıkılmaya başlandığında,

Form bir MDIChild ve MDI formun kapatılmasıyla.

Programın herhangi bir yerinde End komutu ile sonlandırılması durumunda Unload olayı gerçekleşmez. Bu yüzden Unload olayına kod yazdığınız programlarınızda End komutu ile Programı sona erdirmemeliyiz.

**QueryUnload (Cancel As Integer, UnloadMode As Integer):** Unload olayıyla aynı işi yapar ancak formun kimin tarafından kapatılmaya çalışıldığım da öğrenebilirsiniz. Ayrıca bu olay Unload olayından önce meydana gelir ve burada Cancel = True ile kapatma olayı iptal edilirse Unload olayı meydana gelmez.

Unload olayında bir formun 5 değişik şekilde kapanacağını belirtmiştik. QueryUnload olayındaki UnloadMode parametresiyle formun hangi şekilde kapatılmaya çalışıldığını öğrenebiliriz. Bu parametrenin alacağı değerler şöyledir.

0: vbFornıControlMenu (Kontrol kutusunda “kapat” seçildi)

1: vbFormCode (Programda Unload komutu kullanıldı)

2: vbAppWindows (Windows’tan çıkılmaya çalışıldı)

3: vbA TaskManager (Task Managerden “Göreve Son Ver”)

4: vbFormMDIForm ( MDI form kapatıldığında)

Örnek olarak doğru şifre girilmediği sürece Windows’'tan çıkışı önleyecek bir program yapalım.

Windows’u kapatmak istediğinizde, Windows açık olan bütün uygulamalara kendini kapatmalarını bildirir. Yani programların QueryUnload ve Unload olayları aktif hale getirilir. O halde biz Windows’tan çıkılacağını anlayabilmek için yazacağımız programın QueryUnload olayına gerekli kodu yazmamız gerekir. Windows kapatılmak istendiğinde programımız o anda bellekte ise QueryUnload olayı aktif hale gelecek ve doğru şifre girilmezse Windows kapatılmayacaktır. Programı sürekli bellekte tutmak içinde “Başlangıçta” grubuna koymamız gerekir. Ayrıca programın ekranda görülmemesi içinde formu gizlemeliyiz.

**10.21.3. Resize()**

Formun boyutlarının değişmesi halinde bu olay meydana gelir. Formun genişliğinin veya yüksekliğinin değişmesi ayrıca formun minimize edilmesi bu olayı meydana getirir.

**10.21.4. Methods**

**Line:**Bu komutla çizgi veya dikdörtgen çizilebilir.

```vbnet
Line (x1,yl)-(x2,y2),[renk]
```

x 1,y1 koordinatlarında x2,y2 koordinatlarına verilen renk ile bir çizgi çizer.

```vbnet
Liııe -(x2,y2),(renk~
```

şeklinde kullanılarak en son kalınan noktadan x2,y2 noktasına çizim yapılabilir.

```vbnet
Line (xl,y1)-(x2,y2),[renk],B
```

şeklinde kullanılırsa xl,yl köşesinden x2,y2 köşesine bir dikdörtgen çizer.

```vbnet
Line (xl,y1)-(x2,y2),[renk],BF
```

F parametresi ile kullanıldığında ise dikdörtgenin içi renk parametresi ile belirlenen renkle boyanır. F parametresi olmaksızın kullanıldığında ise dikdörtgenin için FilIColor ve FillStyle özellikleri ile belirlenen modda boyanır.

**Circle:** Çember, Elips ve yay çizmek için kullanılır.

```vbnet
Circle (mx,my),r,renk
```

mx,my merkezli r yarıçaplı çemberi verilen renkte çizer.

```vbnet
Circle (mx,my),r,renk,a,b
```

mx, my merkezli r yarıçaplı yayı a açısından b açısına verilen renkte çizer.

**Pset:** Verilen koordinatlar arasına nokta koyarak şekil çizer.

```vbnet
Pset 8x,y),renk
```

**Point:** Verilen koordinatların rengini belirler.

```vbnet
Renk=Point (x,y)
```

**Print: **Form üzerine kontrolden bağımsız olarak yazı yazmak için kullanılır.

Yazının;

Koordinatları CurrentX, CurrentY özellikleri ile

Biçimi FontName, FontSize, FontBold, FontItalic, FontUnderLine, FontStrikeThru özellikleriyle

Boyu FontSize özelliği ile

Rengi ForeColor özelliği ile

Zemin renginin olup olmayacağı FontTransparent özelliği ile

belirlenebilir.

Print metodunda birden fazla değişken araya noktalı virgül koyularak yan yana, virgül koyularak bir tab mesafesinde aralıklı olarak yazdırılabilir.

**Örnek 10.4:**

```vbnet
Dim x,y,z
Show
x=5 :y=10: z=20
Print x,y,z
Print x;y;z
```

**Cls:** Form üzerine yukarıdaki yöntemlerle yazılmış yazı ve çizimleri siler. Forn üzerindeki kontrollerde bir değişiklik olmaz.

**TextHeight (Metin), TextWidth(Metin):** Bu özellikler, Metin parametresiyle verilen yazının formu, picturebox veya yazıcıya print metoduyla yazılması durumunda yazının yüksekliğini ve genişliğini nesnenin ScaleMode özelliğiyle belirlenen birim cinsinden verir. Bu değerlere nesnenin FontName, Fontsize, FontItalic, FontBold gibi fon özellikleri etki eder.

Bu özellikleri, özellikle yazıcıda tablo gibi aynı hizada bulunması gereken çıktılarda kullanmak gerekli olabilir.

**Move sol, üst, genişlik, yükseklik:** Formun veya herhangi bir kontrolün konumunu ve boyutlarını tek sefere değiştirir.

**Scale (x1,y1,x2,y2):** Bu özellikte kontrolün kullanacağı koordinat sistemi yeniden tanımlanabilir. Örneğin matematiksel grafikler için bilgisayarda kullanılan koordinat sistemi uygun değildir. Scale metodu ile bu koordinat sistemini yeniden belirleyebiliriz.

Örneğin formun ortasını orijin, sol üst köşeyi -10,10 ve sağ alt köşeyi de 10,10 kabul edecek yeni bir koordinat sistemi oluşturmak için

```vbnet
Form1.Scale (-10,10,10,-10)
```

şeklinde kullanılabilir. Bu işlemden sonra uygulayacağınız yazım ve çizim metodları bu koordinat sistemi referans alınarak yapılacaktır.

**Hide:** Formun Visible özelliğinin False yapılmasını yani formun ekrnda görülmemsini sağlar.

**Show\[stil\]:** Formun Visible özelliğinin False yapılması gibidir. Parametre ile kullanılırsa formun gösterim şeklini de etkiler.

Burada stil kullanılmazsa veya sıfır kullanılırsa Visible=True ile aynı işi yapar.

Sitil değeri 1 ise form Modal olarak gösterir. Form modal ise, form gizlenmeden veya kapatılmadan program içindeki diğer formlara ulaşım engellenir.

PAGE 21

PAGE 95

---
*Kaynak: `TOOLBOX (VB KONTROL ELAMANLARI)/O-d-e-v-s-i-t-e-s-i-com-18916.doc` — BAHADIR ISLEYEN — 1998*
