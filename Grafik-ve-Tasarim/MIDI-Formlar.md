# MIDI Formlar

**13. BÖLÜM**

**MIDI FORMLAR**

Visal Basic uygulamaları dahilinde aynı anda birden fazla pencereyi açık tutma imkanı vardır. Bunun için MDI(Multiple Document Interface) adı verilen çoklu formlar kullanılır. Üzerinde çalıştığımız Projeye MDI özellikli bir form eklemek istiyorsak Project menüsündeki Add MDI Form seçeneğini seçmeliyiz.

Şekil-13.1. Project Penceresi

Bu seçenek seçildiğinde daha önce Form1 adında normal bir form içeren projeye “MDIForm1” adında MDI özellikli yeni bir form eklenir.

Şekil-13.2. MDI Form

MDI özellikli bir form projede tek başına yer alabileceği gibi çok sayıda alt form (Child) da içerebilir. Diğer taraftan bir projede yalnızca bir tek MDI özellikli form bulunabilir. Üzerinde çalıştığımız projeye MDI özellikli bir form dahil ettikten sonra Project menüsündeki Add MDI Form komutu kullanılamaz duruma gelir. Demek ki bir projede yalnızca bir MDI özellikli form bulunabilir.

Bir projeye MDI özellikli bir form eklendikten sonra istenildiği kadar alt form (Child) eklenebilir. Ayrıca projedeki normal formların sonradan Child özellikli form olmaları sağlanabilir. Bunun için formun Properties penceresindeki MDIChild adındaki özellikten yararlanılır. Bu özellik ilk olarak False değerine sahiptir. Projede MDI özellikli form yokken bu özellik True yapılırsa Form, MDI form özelliği kazanır.

Şekil-13.3. Properties Penceresi

Projedeki MDI özellikli forma alt fomlar dahil etmek için Project menüsünden Add Form komutu ile yeni form dahil edilip bu formun Properties penceresinden yararlanarak Child Form olması sağlanır.

Project penceresinden formların ikonlarına bakarak hangi formun normal, hangisinin MDI veya alt(Child) form olduğunu anlarız.

Şekil-13.4. Project Penceresi

MDI özellikli formlar ile normal formların özellikleri arasında bazı farklılıklar bulunmaktadır. Normal formların ekrandaki konumunu ve büyüklüklerini programcı tasarım veya çalışma anında belirleyebilir. Windows ve Windows uyumlu programların pencerelerine dahil edilen alt pencere veya bilgiler pencereye sığmıyorlarsa pencerenin sağ kenarına otomatik olarak düşey ve yatay kaydırma çubukları eklenir. Benzer durum MDI özellikli pencereler için geçerlidir. MDI özellikli pencereye dahil edilen pencerelerin (Child Form) boyutları çalışma anında değiştirilebilip, alt pencerelerden birinin pencereye sığmaması halinde, MDI özellikli form düşey kaydırma çubuğu otomatik olarak ekler. MDI özellikli formlara kaydırma özellikli formlara kaydırma çubuklarının gerektiğinde eklenmesi için MDI özellikli formun Properties penceresindeki ScrollBars seçeneğinin True olması gerekir.

Şekil-13.5. Properties Penceresi

MDI formların en önemli özelliği nesne dahil edilemiyor olmasıdır. MDI özellikli formlara, normal formlardaki gibi bit ToolBox nesnesi eklenemez.

Visual Basic’te MDI özellikli formlara araç çubuğu eklemek için kullanılan **Toolbar** adında özel bir kontrol bulunmaktadır. Ayrıca ToolBox penceresindeki **PictureBox** kontrolünden de yararlanabiliriz.

Tasarım anında MDI özellikli form aktif iken PictureBox kontrolünün işlevinde değişiklik olur. PictureBox kontrolünü temsil eden düğme seçili durumda iken fare ile formun herhangi bir yerine sürükle işlemi yapılırsa formun üzerine bir çubuk eklenir.

Şekil-13.6. MDI Form Penceresi

Programcının araç çubuğunu genişletme şansı yoktur. Ancak programcı Araç çubuğunun yüksekliğini istediği gibi ayarlayabilir. Üzerinde çalıştığımız MDI özellikli forma araç çubuğu olarak kullanmak üzere bir PictureBox nesnesi varken, forma ikinci bir araç çubuğu ekleyebiliriz.

MDI özellikli formun PictureBox nesnesi eklenen kısımlarına, normal formlarda olduğu gibi istediğimiz nesne veya kontrolü dahil edebiliriz. Buna göre MDI özellikli formun araç çubuğu olarak sınırlanan kısımları normal form alanı gibi kullanılabilir.

Şimdi aşağıdaki şeklide bir form hazırlayalım.

PictureBox dışındaki kontrollere resim eklae olanağımız olmadığı için yine yukarıdaki düğmeyi yerleştirirken PictureBox kontrolünden yararlanacağız. ToolBox penceresinden PictureBox kontrolünü seçtikten sonra MIDI özellikli forma eklemiş olduğumuz araç çubuğunun üzerine fare yardımıyla ikinci bir PictureBox kontrolü ekleyelim.

PictureBox kontrolünün üzerine yerleştirdiğimiz ikinci PicureBox nesnesine resim eklemek için PictureBox nesnesinin Picture özelliğinden yararlanılır.

Properties penceresinin Picture seçeneği üzerinde iken özelliğe ayrılan satırın sonunda üzerinde üç nokta olan bir düğme bulunmaktadır. Bu düğmede tıklama yaparsak resim veya ikon dosyası seçimi yapılan Load Picture diyalog kutusu ekrana gelir.

Bu pencerede istenilen resim dosyası seçilip Aç düğmesi tıklanarak resim yerleştirilir.

Çalışma anında bu düğmenin üzerine tıklama yapıldığı zaman yapılacak işlemleri belirlemek için aşağıdaki satırları yazalım.

Programı çalıştırıp MDI özellikli formu ekrana getirdikten sonra aarç çubuğuna eklediğimiz düğme tıklandığımız zaman, bu düğme için hazırladığımız tek satırlık programı çalıştırır.

PAGE 1

PAGE 170

---
*Kaynak: `MIDI FORMLAR/O-d-e-v-s-i-t-e-s-i-com-18988.doc` — BAHADIR İŞLEYEN — 1998*
