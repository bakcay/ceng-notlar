# Delphi

Delphi 5 yazı dizisine Rifat'ın kaldığı yerden devam edeceğiz. İlk üç yazıda Delphi IDE ve Object Pascaldan bahsedilmişti. Bu yazımızda artık yavaş yavaş Delphi ile görsel programlamaya başlıyoruz. İlk önce Standart ve Additional bileşen paletlerindeki nesnelerimizi tanıdıktan sonra örneklerle öğrendiğimiz nesnelerin kullanımı pekiştirelim.

**STANDART BİLEŞEN PALETİNDEKİ NESNELER******

Öncelikle Standart bileşen paletindeki sık kullanılan nesneleri tanıyalım.

1-TMainMenu Bileşeni: Standart sayfasındaki ilk bileşenimizdir. Bu nesneyi form üzerine yerleştirdiğimizde diğer bileşenleri aksine hazır bir şekle rastlamayız. Zaten program çalıştığında da bu nesneden eser yoktur. Hani hemen her pencerenin en tepesinde Dosya, Düzen, Görünüm,.. diye menuler devam eder gider ya işte bu nesnede bunu yapmak için kullanılır. Bu nesnemizin göze batar özelliği **Items** özelliğidir. Object inspectorda items özelliğinden yada bu nesne üzerine çift tıklayarak menu tasarımcısını açalım. Açılan pencereden mavi zemin üzerine tıklayalım ve Dosya yazalım enter a basalım, daha sonra aynı şeyi Aç ve Kapat seçenekleri içinde yapalım...

Düzen menüsünü yapmak içinde Dosyanın yanındaki boşluğa tıklayıp ve yazmak istediklerimizi yazabiliriz.

2-TPopupMenu Bileşeni: Bu nesnemizin kullanımının tmainmenu nesnesinden pek farkı yoktur. Bu nesnemiz için mainmenu de olduğu gibi bir menü oluşturup tbutton, tedit, tlabel gibi nesnelerin PopupMenu özelliğinde bu nesnemizin adını görürüz. Programın çalışması esnasında bu nesnelerin herhangi biri üzerinde **sağ** tıkladığımız zaman oluşturduğumuz bu menüyü görürüz.

3-TLabel Bileşeni: Bu bileşenle form üzerine statik yazılar yazabiliriz. TLabel bileşeninin Caption özelliğine yazdığımız yazı form üzerinde görünür. Ancak programın çalışması esnasında kullanıcı bu bileşene bilgi girişi yapamazlar. Yazını rengini yada şeklini değiştirmek için bu nesnemizin font ve color özelliklerini kullanabiliriz.

4-TEdit Bileşeni: Bu bileşen sayesinde kullanıcılar form üzerinde bilgi girişi yapabilirler ve bu bilgiye ulaşabilmemiz için Edit1.Text gibi bir ifade kullanmamız gerekir. Sıkça kullanılan özellikleriyse CharCase ve PasswordChar özelliğidir. CharCase özelliği ile kullanıcının sadece küçük harf girmesi(ecLowerCase), sadece büyük harf girmesi(ecUpperCase) yada girilen harfin olduğu gibi kalmasını(ecNormal) sağlayabiliriz. PasswordChar özelliğinde ise, en basitinden e-postanıza bakmak için önce kullanıcı adını sonrada şifrenizi girersiniz. Siz şifrenizi girersiniz ama size gözüken \*\*\*\* karakterleridir. işte bunu sağlamak için bu özelliğe \* yazmamız yeterli olacaktır.

5-TMemo Bileşeni: Bu bileşen ekran üzerinde sınırları belirlenmiş bir alanda yazı yazılabilmesi ve yazılan yazıların değiştirilmesini sağlar. Lines adındaki özelliği ile tmemo nesnemizin içine birşeyler yazabiliriz, ve memonun içeriğini bir text dosyasına kaydedebilir yada bir text dosyasını açabiliriz.

Memo1.Lines.LoadFromFile('c:\\a.txt'); //c deki a.txt dosyasını memonun içine açar.
Memo1.Lines.SavetoFile('c:\\a.txt'); //c deki a.txt dosyasına memonun içeriğini kaydeder.

6-TButton Bileşeni: En çok kullanacağımız bileşenlerdendir. Butonun üzerine tıklandığında icra edilecek kodları Button1 'in OnClick(tıklandığında) olayına yazarız. Hemen basit bir örnek yapalım. Form üzerine bir tane button koyalım ve caption özelliğine birşey yazalım.Daha sonra Onclick olayı karşısında çift tıklayalım.Yada button üzerinde çift tıklaylım.

Karşımıza gelen kod editor penceresi gelecektir

.

Begin ve end arasına showmessage('Merhaba!'); yazalım. En son olarak ise programı çalıştıralım..

6-TCheckBox Bileşeni: Bu bileşen daha çok Evet/Hayır, Var/Yok, Kadın/Erkek gibi cevabı iki seçenekten birisi olan soruların cevaplanmasında kullanılır. Bu nesnemizin Checked özelliğine bakarak bu nesnenin işaretlenip yada işaretlenmediğini anlayabiliriz. Hemen bir uygulama yapalım. Form üzerine bir tane button ve checkbox koyalım. Checkbox1 nesnemizin Caption özelliğine Öğrenci yazalım. Daha sonra Button'un OnClick olayına giderek begin end bloğu arasında şu kodları yazalım.

if (checkbox1.checked=true) then Showmessage('Öğrenci') else ('Öğrenci Değil');

Bu kodu yazıp butona tıklayınca şöyle bir çıktı alırız

.

7-TRadioButton Bileşeni: Bu bileşen tek başına çok fazla kullanışlı olmadığı için bunu TRadioGroup bileşeninde anlatacağım.

8-TListBox Bileşeni: Form üstünde kullanıcılara herhangi bir listenin gösterimesi yada listeden herhangi bir elemanın seçilmesi için kullanılır.Listbox içinde görünmesini istediğimiz elemanları **items** isimli özelliğine yazabiliriz. Bu özelliğin yanındaki üç düğmeye tıklayıp istediğimiz elemanları buraya yazabiliriz. Seçilmiş elemana ulaşmak için listbox1.items\[listbox1.itemindex\] ifadesiniz kullanırız.Yada listbox taki 3. elemana konumlanacağız listbox1.items\[2\] ifadesini kullanırız.(eleman numaraları 0 dan başlar.) ListBox a yeni bir eleman eklemek için listbox1.items.add(edit1.text); ifadesini kullanırız.(editin textindeki ifadeyi listbox a ekler.) Şimdi yine bu nesnemizle bir örnek yapalım. Items özelliğine giderek aşağıdakileri yazalım.

Bu elemanları yazdıktan sonra form üzerine üç tane tbutton bir tane tedit iki tane label koyalım ve özelliklerini şöyle değiştirelim.

Label1...Caption : Meyveler
Label2...Caption : Eklenecek Meyve
Button1...Caption : Ekle , OnClick :Button1.Click

Button2...Caption :Eleman Sayisi, OnClick :Button2.Click
Button3...Caption :Seçili Eleman, OnClick :Button3.Click

Bir sonraki adımda ise Button nesnelerimizin OnClick olaylarına şu şekilde tamamlayalım.

Programımızın Son Hali

9-TCombobox Bileşeni : Bu bileşen aslında TListBox bileşenine çok benzer ve daha cok yerden kazanmak için kullanılır. Listboxtaki komutların hemen hemen aynısı ComboBox içinde geçerlidir. Listbox tan farklı olarak seçili elemana combobox1.items\[combobox1.itemindex\] ifadesiyle ulaşabileceğimiz gibi combobox1.text ifadesiyle de ulaşabiliriz . ComboBox a örnek olarak Listbox ta yaptığımız örneğin aynısını yapabilirmisiniz :)

10-TRadioGroup Bileşeni : RadioButton bileşenlerinin biraraya gelmesiyle oluşur ve bu bileşenlerin yine items adında bir özelliği vardır. Hangi elemanın seçili olduğunu itemindex özelliği ile anlayabiliriz. Şimdi bir örnek yapalım. Üç tane tlabel, iki tane tedit ve bir tanede TRadioGrup bileşenini form üzerine koyalım. Özelliklerini ise şöyle değiştirelim.

label1...Caption: Birinci sayıyı giriniz.
label2...Caption: İkinci sayıyı giriniz.
label3...Caption: Boş bırakın
Edit1, Edit2 ...Text : Boş bırakalım., OnKeyPress : Kodda oldugu gibi tamamlayalım. (Edit1 için kodu tamamlayalım. Edit2 için KeyPress olayına gidip yanındaki ok işaretine tıklayıp Edit.KeyPress i seçelim.)
TRadioGrup..items : Şekildeki gibi tamamlayalım , OnClick : Koddaki gibi tamamlayalım.

Bu makalede Delphi 5 ile görsel programlamaya bir giriş yaptık ve Standart bileşen paletindeki sık kullanılan bileşenleri inceledik... Sonra ki makalemizde Delphi 5 Additional bileşen paletinde ki sık kullanılan bileşenleri inceleyeceğiz...

---
*Kaynak: `DELPHI/DELPHI.doc` — ekim kaya — 2004*
