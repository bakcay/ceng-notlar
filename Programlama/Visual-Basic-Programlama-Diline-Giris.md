# Visual Basic Programlama Diline Giriş

**3. BÖLÜM**

**3. VISUAL BASIC PROGRAMLAMA DİLİNE GİRİŞ**

**3.1. Visual Basic Ana Formu**

VB ilk çalıştırıldığı zaman VB’in kendine ait olan aşağıdaki form ekrana gelir.

Şekil-3.1.1. Visual Basic Ana Formu

**Araç Çubukları **

VB penceresinde çok sayıda düğme içeren araç çubukları bulunmaktadır. Araç çubuklarını ekrandan kaldırmak veya eklemek için View menüsünün Toolbars seçeneğinden faydalanılır. Bu araç çubukları Debug, Edit, Form Editör, Standart olmak üzere dört tanedirler. Bu araç çubuklarıyla yeni proje açma, projeyi kaydetme gibi işlemler menülerle uğraşmaya gerek duymadan kısa yoldan yapılırlar.

Şekil-3.1.2. Araç Çubukları

**Programcı Formu **

** **Bu form programa ait kullanıcı arabiriminin oluşturulduğu yerdir. Burada oluşturduğumuz formun görüntüsü program çalıştığı zaman aynen gözükür. Bu VB en önemli özelliğidir. Diğer dillerde programın ekran görüntüsü programın çalışması esnasında oluşturulurken VB’de bu iş tasarım sıkıcı kodları kullanmadan ve görerek yapabilmekteyiz. Programda birden fazla formda bulunabilir.

Şekil-3.1.3. Programcı Formu

**ToolBox Menüsü**

** **Form üzerine yerleştirilecek kontrollerin tamamı Toolbox penceresinde yer alır. Bu pencereye yeni kontrol elamanı eklemek, silmek veya adını değiştirmek işlemleri yapılabilir. Bu konuyu ileride ayrıntılı olarak anlatacağız.

Şekil 3.1.4. ToolBox menüsü

** 3.1.4. Properties (Özellikler) Penceresi **

** **Bu pencere seçili durumda olan nesnenin özellikleri gösterir. Başlangıçta VB projelerinde yalnızca “Form1” adında form ya da nesne olduğu için properties penceresinde Form’in özellikleri listelenmektedir.

Şekil-3.1.5. Properties Penceresi

Bu pencerenin alt kısmında üzerinde bulunulan özellikler hakkında bilgi verilmektedir. Eğer bu pencerenin alt kısmında üzerinde bulunduğu özellik hakkında açıklayıcı bilginin verilmesini istemiyorsak farenin sağ tuşunu tıklayıp açılan pencereden Description komutunu vermemiz gerekmektedir.

**3.1.6. Project Penceresi **

Bu pencere üzerinde çalışılan programa dahil edilen form, modül vb. elemanların listesini verir. Bu pencere aracılığı ile istenilen bir forma geçiş yapmak modülü forma dahil etmek mümkündür.

**NOT:** Modül, VB projelerinde formlardan başka birde BAS uzantılı Basic program kodunu içeren dosyalar bulunabilir. BAS uzantılı program kodu dosyalarına MODULE adı verilir.

Şekil-3.1.6. Project Penceresi

**3.1.7. Kod Penceresi **

Visual diller programcının kendi kodunu yazacağı bir editör sunarlar. Önceki VB versiyonlarında her elemanın kullandığı olaya ait bir kod penceresi karşımıza çıkarken 4.0 versiyonundan sonra ise tüm elamanlar aynı kod penceresinden çıkmakta ve elamanlara ait olay prosedürleri bir ayırma çizgisi ile ayırmaktadır. Üzerinde çalışılan form veya kontrol elamanı çift tıklatıldığında bu pencere karşımıza gelir.

Şekil-3.1.7. Kod Penceresi

** 3.1.8. Pencere Organizasyonu (Form Layout)**

Visual Basic penceresi içinde üzerinde çalışılan proje ile ilgili çok sayıda alt pencere açılmaktadır. Bu alt pencereler Visual Basic penceresi içinde nasıl organize edildiğini görmek için bu pencereden yararlanılır.

Şekil-3.1.8. Form Loyout Penceresi

**Örnek 3.1 :** Şimdi bu konuyu iyi kavrayabilmemiz için aşağıdaki formu oluşturalım.

Şimdi Labe1 bölümüne Adı kelimesini yazdıralım. Label1’i seçtikten sonra properties penceresinden Caption seçeneğini seçelim. Caption’daki Label yerine Adı kelimesini yazalım. Aynı şekilde Label2’ye Soyadı, Label3’e telefonu Label’de adresi, Command1’e Ekle, ommand2’ye Sil, Comman3’e Çıkış kelimelerini yazalım.

Şimdi Çıkış işleminden başlayarak işlemlerimizi yapalım. Çıkış butonunun üzerine gelip çift tıkladığımızda kod penceresi gelmektedir. Bu pencerede Sub ile End Sub arasına çıkmak için gerekli olan END komutunu yazalım.

Programı F5 tuşu ile Run ettiğimizde düğmelerde birinin üzerine düşen görevi yaptığını göreceğiz.

Şimdi ise Ekle düğmesi seçildiğinde girilen ismi listeye eklemek için gerekli kodu yazalım. Üzerine ekle yazdığımız komut düğmesinin üzerini çift tıklayın. Girilen ismi listeye eklemek için List kutusunun AddItem özelliğinden yararlanacağız. Şimdi kod penceresine List1.AddItem Text1.Tex yazalım.

Son olarak da Sil düğmesi ile listeden seçileni silmeye çalışalım. Bunun için Liste kutusunun RemoveItem özelliğinden yararlanalım. List1.RemoveItem List1.ListIndex satırını komut penceresine yazalım.

Artık programımızı F5 tuşu ile çalıştırarak işlemleri gerçekleştirebiliriz.

PAGE

PAGE 10

Standart

Debug

Editör

Form Editör

---
*Kaynak: `VISUAL BASIC PROGRAMLAMA DİLİNE GİRİŞ/VISUAL BASIC PROGRAMLAMA DİLİNE GİRİŞ.doc` — BAHADIR — 2004*
