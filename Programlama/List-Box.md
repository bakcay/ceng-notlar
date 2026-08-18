# List Box

## **LİST BOX (LİSTE KUTUSU)**

List Box elemanları listelemek, sıralamak gibi özellikler sunan genel amaçlı bir kontroldür. DirectoryListBox, DriveListBox, FileListBox gibi türevleri vardır. Component Palette araç çubuğunda bulunan List Box kontrolünü seçili duruma getirip formun üzerine tıklama yapılır ve formun üstüne “Liste Kutusu” nesnesi eklenmiş olur.

## **PROPERTIES**

## **ITEMS**

Liste kutusunda bulunması istenen elemanlar tasarım zamanı yükleneceği gibi çalışma zamanında da Items özelliğinin metotları ile yapılır.

Açılacak listede bulunması istenilen elemanları listeye tasarım anında eklenmesi Object Inspector penceresinden Items özelliğine çift tıklayarak gelen pencereden kolaylıkla yapılabilir.

**Items özelliğinin Önemli Alt Bölümleri:**

** Items.Add(eleman): **Bu özellik ile listenin sonuna yeni elemanlar eklenebilir.

ListBox1.Items.Add (‘istanbul’);

ListBox1.Items.Add (‘ankara’);

** Items.Insert(SatırNo,Eleman): **Add metodu verilen eleman sona eklenir. Araya eklemek için Insert yöntemi kullanılır. Örneğin; ikinci satıra ‘izmir’ elemanını eklemek için: ListBox1.Items.Insert(1,‘izmir’); İlk elemanın numarası 0 olduğu için bir eksiği kullanılır.

** Items.Count: **Listede kaç eleman olduğunu verir.

** **ListBox1.Items.Count;

** Items.Delete(Index): **Index numarası verilen elemanı listeden çıkarır.

ListBox1.Items.Delete(0);

** Items.Strings\[ElemanNo\]: **Listedeki ElemanNo numaralı elemanı öğrenmeye ve değiştirmeye yarar. İlk elemanın numarası 0’dır. Satır numarası verilen eleman yoksa işlem yapılmaz.

ListBox1.Items.Strings\[SatırNo\] satırı ve Listbox1.Items\[SatırNo\] satırı aynı işlemi yapar.

ListBox1.Items.Strings\[3\] := ’bursa’;

** Items.ExChange(Eleman1,Eleman2): **İki elemanın yerini değiştirir.

Örneğin; birinci ve ikinci elemanın yerini değiştirmek için:

ListBox1.Items.Exchange(0,1);

**Items.Move(Index,YeniIndex): **Index ile verilen elemanı YeniIndex ile verilen satıra taşır. Örneğin; ikinci elemanı beşinci satıra taşımak için:

ListBox1.Items.Move(1,4);

** Items.IndexOf(Eleman): **Verilen elemanın listede kaçıncı eleman olduğunu bulur. Verilen eleman yoksa geriye –1 döner. Bu özellik ile bir elemanın listede olup olmadığı kontrol edilebilir.

** Items.SaveToFile(dosyaadı): **Listedeki elemanları dosyaya satır-satır kaydeder.

ListBox1.Items.SaveToFile(‘okul.txt’);

** Items.LoadFromFile(dosyaadı): **verilen dosyadaki satırları listeye ekler.** ******

ListBox1.Items.LoadfromFile(‘okul.txt’);

## **TOPINDEX**

Bu özellik listenin o anda ekranda görülen kısmında en üstteki elemanın Indexini öğrenmeye ve değiştirmeye yarar.

## **SORTED**

Bu özellik True ise listedeki elemanlar alfabetik sıraya dizilir. Listeye eklenen elemanlar sona değil alfabetik sıraya göre dizilir. Ancak bu sıralama işlemi sayılar üzerinde doğru etkiyi göstermez. Çünkü alfabetik olarak 10 sayısı 2 sayısından önce gelir.

## **COLUMNS**

Bu özellik ile liste kutusu birkaç satır yapılabilir.

**0 ise:** Liste kutusu tek sütundur ve listenin ekranda görülen kısmının dolmasıyla listeye dikey scrollbar eklenir.

**0 değilse: **Listenin genişliği verilen sayıda bölünür ve bir sütunun dolmasıyla ikinci sütuna geçilir. Listenin görülen kısmındaki sütunların dolmasıyla listeye yatay scrollbar eklenir.

## **MULTISELECT**

Bu özellik True ise liste içinde birden fazla eleman seçilebilir.

## **SELCOUNT,SELECTED\[INDEX\]**

SelCount özelliği List Box içindeki seçili olan eleman sayısını verir. Selected özelliği de Index nolu elemanın seçili olup olmadığını bildirir.

## **EXTENDEDSELECT**

MultiSelect özelliği True ise listeden birden fazla eleman seçilebilir.

True ise: Windows’un Dosya yöneticisi – Explorer programındaki gibi değişik şekillerde listeden eleman seçilebilir. (Shift + yön tuşları ile veya Ctrl + click v.b.)

## **STYLE**

Bu özellik List Box kontrolünün verileri nasıl göstereceğini belirtir. Şu değerleri alabilir;

IbStandard: Bütün veriler string ve aynı yükseklikte olur.

IbOwnerDrawFixed: List Box’taki verilerin yüksekliği aynı olmak şartıyla ItemHeight özelliğiyle ayarlanır.

IbOwnerDrawVarible: List Box’taki verilerin yüksekliği birbirinden farklı olarak ayarlanabilir.

## **METHODS**

## **CLEAR**

Listedeki tüm elemanları bir kerede silmek için bu metot kullanılır.

## **COMBO BOX (AÇILAN LİSTE KUTUSU)**

Aşağı doğru açılabilen bir liste kontrolüdür. Component palette araç çubuğunda bulunan Combo Box kontrolünü seçili duruma getirip formun üzerine tıklama yapılır ve formun üstüne “Açılan Liste Kutusu” nesnesi eklenmiş olur. Combo Box normalde ekrana tek satır halinde gelir. Genellikle, değerleri daha önceden belli olan elemanların seçimi için kullanılırlar. Liste kutusuna benzer fakat listedeki elemanlardan sadece seçileni ekranda görüntüler. Combo box başlangıçta herhangi bir eleman içermez.

## **Combo Box Kontrolüne Eleman Ekleme:**

** **Çalışma anında combo box’ta listelenmesi istenilen bilgiler **Object Inspector** penceresinde **Items** özelliğinden yaralanılarak belirlenir. Items özelliğine ait metin kutusunun sonuna eklenilen düğmede tıklama yapılırsa, ekrana String List Editör diyalog kutusu aracılığı ile listelenecek seçeneklerin girişi yapılır.

**Items.Add(eleman)******

** **Bu özelliği kullanarakta listenin sonuna yeni eleman ekleyebiliriz.

ComboBox1.Items.Add (‘İSTANBUL’);

ComboBox1.Items.Add (‘İZMİR’); gibi.

## **Combo Box Kontrolünden Eleman Silme:**

**Items.Delete(Index)**

** **Index numarası verilen elemanı listeden çıkarır.

ComboBox1.Items.Delete(0); // Listedeki ilk elemanı sil.

ComboBox1.Items.Delete(ComboBox1.ItemIndex); // Seçili elemanı sil

## **PROPERTIES**

**Style**

Aşağıdaki değerlerden birini alarak Combo Box’ın stilini belirler.

**csDropDown: **Aşağıya doğru açılabilen bir Combo Box oluşturur. Kullanıcı bilgi girişi yapabilir. Kutudaki tüm veriler aynı yüksekliktedir.

**csDropDownList: **Aşağıya doğru açılabilen bir Combo Box oluşturur. Kullanıcı bilgi girişi yapamaz. Kutudaki tüm veriler aynı yüksekliktedir.

**csSimple: **Aşağıya doğru açılmayan bir Combo Box oluşturulur. Kullanıcı bilgi girişi yapabilir. Aşağıya doğru açılmadığı için kullanıcı yukarı ve aşağı tuşları ile bir seçim yapabilir.

**csOwnerDrawFixed: **Aşağıya doğru açılabilen bir Combo Box oluşturulur. Kullanıcı bilgi girişi yapamaz. Kutudaki verilerin yükseklikleri ItemHeight özelliğiyle değiştirilebilir. Bu tipteki Combo Box’lar grafik nesnelerde içerebilir. DriveComboBox kontrolü bu tip Combo Box’a örnek olarak verilebilir.

**csOwnerdrawVariable: **Aşağıya doğru açılabilen bir Combo Box oluşturulur. Kullanıcı bilgi girişi yapamaz. Kutudaki verilerin yükseklikleri farklı olabilir. Bu tipteki Combo Box’lar grafik nesnelerde içerebilir.

**DropDownCount: **Bu özellik Combo Box aşağıya doğru açılırken gösterilecek olan eleman sayısını belirtir. Eğer herhangi bir değer belirtilmezse varsayılan değer 8’dir.

**MaxLength:** csDropDown, csSimple tipindeki Combo Box’lara kullanıcı bilgi girişi yapabilmekteydi. Bu özellikle, istenirse kullanıcının giriş yapabileceği karakter sayısı sınırlandırılabilir yada 0 verilerek sınır kaldırılır.

## **EVENTS**

** OnClick (Sender:TObject): **Kullanıcının kutudan bir eleman seçmesi ile bu olay meydana gelir.

** OnChange (Sender:TObject):** Kullanıcının kutudan bir eleman seçmesi veya kutuya bir şey yazması ile bu olay meydana gelir.

## **CHECK BOX (İŞARET KUTUSU)**

Kullanıcının bir seçeneği aktif veya pasif duruma getirmesi için kullanılan bir kontroldür.

Bu kontrol üç durumdan birinde bulunabilir:

**Checked: **İşaretli

**UnChecked: **İşaretsiz

**Grayed:** Bu durum temsil ettiği şeyin belirsizliğini gösterir.

## **PROPERTİES **

## **CHECKED**

Bu özellik CheckBox kontrolünün işaretli mi, işaretsiz mi olduğunu öğrenmeye ve değiştirmeye yarar.

Seçili ise: CheckBox 1.Checked:= true;

Seçili değil ise: CheckBox 1.Checked:= false;

Grayed durumu içinde State özelliği kullanılır.

## **STATE**

Checked özelliği gibi CheckBox’ın durumunu öğrenmeye yarar. Tek farkı Grayed durumuna da getirilebilir.

CheckBox 1.State:= cbChecked;

CheckBox 1.State:= cbUnChecked;

CheckBox 1.State:= cbGrayed;

## **ALIGNMENT**

Bu özellik caption özelliği ile belirlenen yazının, işaretin sağına mı soluna mı yazılacağını belirler.

CheckBox 1.Alignment:= taLeftJustify;

CheckBox 1.Alignment:= taRightJustify;

## **RADIO BUTTON (SEÇENEK KUTUSU)**

Radio Button kontrolü Check Box’tan farklı olarak birkaç seçenekten birini seçme imkanı veren bir kontroldür.

## **PROPERTİES **

## **CHECKED**

Checked özelliğinin True olması Radio Button düğmesinin seçili olması demektir.

## **RADIO GROUP**

Bu kontrol Radio düğmelerini gruplamak için değil istenen sayıda Radio düğmesini çalışma zamanı oluşturmak için kullanılır.

## **PROPERTİES **

## **ITEMS**

Bu özellik ile yeni düğmeler eklenebilir. List Box’ın Items özelliğiyle aynıdır.

## **ITEMINDEX**

Seçili olan elemanın numarası bu özellikle öğrenilebilir.

## **COLUMNS**

Bu özellik düğmelerin kaç sütunda gösterileceğini belirler.

## ** EVENTS**

**OnClick (Sender:TObject): **Radio Group nesnesinin Click olayı çerçevenin tıklanması ile değil içindeki bir düğmenin tıklanmasıyla meydana gelir. Hangi düğmenin tıklandığı ise ItemIndex özelliği ile öğrenilebilir.

## **PANEL KONTROL ELEMANI**

Bu kontrol elemanı içerisine kontrol elemanları yerleştirilebilir. Yani Group Box gibi diğer kontrolleri gruplamak için kullanılabilir. Farklı ise üç boyutlu görünümü ayarlanabilen bir kontroldür. Genelde Toolbar gibi kontrolleri gruplamak için kullanılır.

## **PROPERTİES******

## **BEVELINNER, BEVELOUTER**

İç ve dış çerçevelerin üç boyutlu görünümü bu iki özellikle belirlenir.

## **BEVELWIDTH, BORDERWIDTH******

Bu iki özellikle üç boyut efekti sağlayan çerçevelerin genişlikleri belirlenir.

## **CAPTION******

Panelin içindeki yazı bu özellikle belirlenir.

## **GROUP BOX (GRUPLAMA KUTUSU)**

Bu kontrol tek başına değil diğer kontrolleri gruplamak için kullanılır. Bu çerçeveler içine konan kontroller, çerçeveye bağımlıdırlar ve konumları bu çerçeve dışına taşamaz. Örneğin; birkaç kontrolü birden görünür veya görünmez yapmak için hepsinin Visible özelliğini tek tek değiştirmek yerine çerçevenin Visible özelliği değiştirilerek sorun halledilir. Kontrolün tek başına kullanılması anlamsızdır. Birkaç seçenekten birini seçme imkanı veren bir kontrol oluğu için en az iki tane birlikte kullanılmalıdır. Gruptaki Radio düğmelerinden biri seçildiğinde diğeri pasif olur. Aynı anda bir grupta iki tane işaretli düğme bulunmaz.

## **ALEV PARLAR**

## ** 11/A 49**

PAGE

PAGE 1

---
*Kaynak: `LIST BOX/LIST BOX.doc` — ALEV — 2004*
