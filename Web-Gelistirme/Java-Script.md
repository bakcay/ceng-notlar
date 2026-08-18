# Java Script

**Bir Web sayfasına Java Script Eklemek **

Bir Web sayfasında JScript ile kod yazabilmek için ilk önce tarayıcımıza kullanacağımız script dilini tanıtmamız gereklidir.

<script language="JavaScript>
...
JScript kodları
...
</script>

Burada;

<script language="JavaScript"> </script>

tag'leri tarayıcımıza komutların HTML değil JScript olduğunu gösterir.Bu satırları eklemememiz halinde tarayıcı komutları tanımayacağından JScript komutlarımız dökümanın bir parçası olarak algılanacak ve ekranda görünecektir.
Unutmamamız gereken noktalar tüm fonksiyonların ve blokların { ve } işaretleri arasında yazılması gerektiği ve her komut satırından sonra ; (noktalı virgül) işaretinin koyulması gerektiğidir.
Ayrıca JScript kodları her tarayıcının her sürümünde doğru olarak çalışmayacağı için özellikle eski tarayıcılarda hata verecektir. Bunu engellemek için

<script>
<!-- Hide script from older browsers
...
JScript kodları
...
// End hiding -->
</script>

**Sayfaya Yazı Yazdırmak **

Java Script kullanarak ekrana yazı yazdırmak document.write komutu ile yapılır. Kullanımı ise:

window.document.write("Merhaba Dünya !");

şeklindedir.
window.documen t kodu nesnemizin şu anda açık olan sayfamız olduğunu anlatır. Write komutu ait olduğu nesneye yazılmasını sağlar. Parametreleri ise parantezler arasına verilir. Eğer yazdırmak istediğimiz metni kodun içinde gireceksek metni "...." tırnak işaretlerini kullanarak girmemiz gereklidir. Ayrıca + işaretini kullanarak birden fazla giriş yapmak ta mümkündür.

window.document.write("Merhaba" + "Dünya");

veya isim, kullanıcının ismini taşıyan bir değişken olmak üzere

window.document.write("Merhaba" + isim);

yazmamız halinde bu ayrı metinler aralarında bir boşluk karakteri bırakılmak üzere ard arda yazılacaktır.
Ayrıca JScript'le yazdıracağımız metinleri HTML kodlarıyla şekillendirmemiz mümkündür.

window.document.write("<center><B>Merhaba Dünya</B></center>")

Her ne kadar linkleri HTML kullanarak yaratmak mümkünse de gelişmiş uygulamalarda gidilecek sayfalara parametre aktarımı yapabilmek için linki JScript'le oluşturmak gerekebilir. Bunun için JScript'te window.location.href komutu kullanılır.

Örnek olarak Java.htm isimli sayfaya gitmek için bu komutun kullanımı:

window.location.href="java.htm";

olacaktır. Tırnak işaretleri arasına URL girmek te mümkündür.

window.location.href="http://www.programlama.com";

**java Script' te Uyarı Mesajları **

JScript'te uyarı mesajları yazmak için alert komutu kullanılır. Örneğin

<script language="Javascript">
alert("Uyarı Mesajı");
</script>

scripti ekrana **Uyarı Mesajı **yazılı ve bir OK butonu bulunan bir mesaj kutusu getirir. OK butonuna basılınca Script, bir alt satırdan çalışmaya devam edecektir

**Java Script'te Fonksiyon Kullanımı **

JScript te C++ gibi nesneye yönelik bir dildir ve fonksiyonlar bu yapıda en önemli yeri alır. JScript fonksiyonları çağırıldıkları zaman işlemeye başlayan scriptlerdir. Aşağıdaki örnek, butona basıldığında "Merhaba Dünya" uyarı mesajı çıkartan fonksiyondur.

<script language="Javascript"<
function Deneme()
{
alert("Merhaba Dünya");
}
</script>

Şimdi düğmeye basıldığında bu fonksiyonu çağıran HTML kodunu yazalım

<form name="form1">
<input type="button" value="Buraya Bas" onclick="Deneme()">
</form>

JScript fonksiyonunda sadece alert("Merhaba Dünya") komutu var. HTML'de de üzerinde "Buraya Bas" yazılı bir buton var ve onclick olayı Deneme isimli fonksiyona yönlendirilmiş. Bu fonksiyona hiç bir parametre gelmiyor ve bir dönüş parametresi de yok. Aynı fonksiyon şu şekilde yazılısaydı:

<script language="Javascript">
function Deneme(param)
{
alert(param);
}
</script>

ve onu çağıran HTML satırında da fonksiyona "Merhaba Dünya" parametresini gönderseydik alınan sonuçta hiç bir değişiklik olmayacaktır.

<form name="form1">
<input type="button" value="Buraya Bas" onclick="Deneme('Merhaba Dünya')">
</form>

Burada dikkat edilmesi gereken nokta HTML'den parametreyi gönderirken fonksiyon adından sonra açılan parantezlere ' ve ' işaretleri arasına yazılması ve fonksiyon için param artık bir parametre olduğu için alert fonksiyonunda parantezlerin içinde tırnak içine alınmaması gereğidir.

JScript fonksiyonları hakkında bilinmesi gereken bir diğer nokta da fonksiyonlar tarayıcı tarafından işlendikten sonra HTML koduna dönüştürüleceğinden (C'deki precompiler mantığıyla) HTML'de yerine koyulacak bir değer de fonksiyonla verilebilir. Yani linker fonksiyonu yapılan bir seçime göre bir URL döndürüyorsa HTML'de <a href=linker(seçim)> yazımında hiç bir sakınca yoktur.

Fonksiyonların gerçekleşmesi için fonksiyonun çağırıldığı **olay **'ın alması gerekmektedir. Bu olaylardan bazıları:

Olay İsmi Ne Zaman Olur

**onClick : **Butona basıldığında

**onAbort : **Stop düğmesine veya bir linke basılarak yüklenme durdurulduğunda

**onChange : **Seçim yapıldığında veya metin değiştirildiğinde

**onError : **Resmin veya ekranın yüklenmesinde hata oluştuğu zamanlar

**onLoad : **Sayfa yüklenmesi tamamlandığında

**onMouseOut : **Mouse pointer bir alan veya linkten uzaklaştırıldığında

**onMouseOver : **Mouse pointer bir alan veya linkin üzerine geldiğinde

**onSelect : **Seçim için ayrılmış bir nesne seçildiğinde

**onSubmit : **Submit(gönder) butonu basıldığında

**onUnload : **Sayfa yüklenmesi bittiğinde(kullanıcı sayfadan çıktığında)

**Java Scrtipt'te Değer Girişi **

JScript'te alert komutunu bir çıkış komutu olarak düşünürsek bunun karşılığı olan giriş komutu prompt komutudur. Bu komut

adsoyad=prompt("Adınızı ve soyadınızı giriniz","");

şeklinde kullanılır ve kullanıcı tarafından girilen değer adsoyad isinmli değişkene atanır.

**Java Script'te Karşılaştırma İşlemi **

Conditional statement veya If statement olarak bilinen komut grubu yani IF-THEN-ELSE JScript'te de mevcuttur. Bu komut grubu bir değerle bir diğerini karşılaştırıp sonuca göre farklı işlemler yapmamızı sağlar. Şimdi az önceki örnekte olduğu gibi kullanıcıdan ismini girmesini isteyelim ve bir karşılaştırma yapalım. Dikkat etmemiz gereken nokta aynı C dilinde olduğu gibi then komutunu kullanmamamızdır.

adsoyad=prompt("Adınızı ve soyadınızı giriniz","");

if(adsoyad=="Serdar Kalaycı") alert("Hosgeldin Serdar");

else alert("Seni Tanımıyorum");

Burada bahsedilmesi gereken bir diğer konu da karşılaştırma operatörleri ve mantıksal operatörler. Karşılaştırma operatörleri:

Denk ==

Eşit değil !=

Küçük

< Büyük >

Küçük veya Eşit

<= Büyük veya Eşit >=

Mantıksal operatörler:

Ve &

Veya |

Değil !

XOR ^

Bir de birden fazla karşılaştırmayı birleştirmek için

Ve &&

Veya ||

Ayrıca ++ operatörü birer birer artırmak için ve – operatörü de birer birer azaltmak için kullanılır.

operatörlerini kullanabiliriz. Dikkat edilmesi gereken nokta bir adet = operatörünün eşitleme iki adet ==operatörünün karşılaştırma işleminde kullanılması gerektiği ve ! operatörünün her yerde değil anlamı taşıdığıdır. Yani ! operatörü diğer operatörlerle birlikte değil anlamı vermek üzere kullanılabilir

**Java Script'te Değişkenler **

JScript'te değişkenlere diğer diller gibi bir değişken tipi atamak zorunda değiliz. Daha sonra bu değişkeni eşitlediğiniz değere göre bir tip alacaktır.

JScript'te değişken tipleri olmadığı gibi bir dizi tanımı da yoktur. Bir dizi oluşturmak için basit bir foksksiyon yazmamız ve daha sonra kaç elemanlı dizi açmak istiyorsak bu fonksiyona onu parametre olarak göndermemiz gerekecektir. Bu fonksiyon şu şekilde olabilir:

function makearray(n)
{
this.lenght=n;
for( var i=1;i<=n;i++)
{
this\[i\]=0;
return this;
}
}

Daha sonra da dizimize vermek istediğimiz ismi ve uzunluğunu bu fonksiyona göndermemiz gerekecek. Yani

dizi= new makearray(20);

dediğimizde 20 elemanlı ve her elemanı 0 olan bir dizi oluşturalacaktır.

Tabi ki bu ilk değeri olmayan veya çok uzun bir dizi yaratmak için aksi halde Array komutuyla da bir dizi yaratılabilir. Şöyle ki:

dizi = Array("Ali","Ayse","Selim","Yahya","Kemal");

Burada dikkat edilmesi gereken nokta dizi elemanlarına ulaşırken diziadı\[indexno\] syntax'ı ve dizi index numaralarının( biz aksini belirtmedikçe) 0'dan başladığıdır. Bu arada bir değişkene string değer atandığı zaman o değişkenin otomatik olarak bir karakterler dizisi olarak algılanmayacağı da önemli bir özelliktir. Yani;

ad="Serdar";

şeklinde bir tanımlamada ad\[1\]=S , ad\[2\]=e ... olmayacaktır.

Bir stringin içinden bir harfi ya da harf grubunu almak istediğimizde kullanmamız gereken komut substring komutudur.

harf=ad.substring(0,1);

yazdığımızda harf değişkeni S harfini içerecektir. Buradaki parametrelerden 0, kaçıncı karakterden başlanacağını 1 ise kaçıncı karaktere kadar alınacağını gösterir.(1 hariç)

Yani harf=ad.substring(0,2) deseydik harf değişkeni "Se" değerini içerecekti.

Bu işlemin tam tersi de mümkündür. Yani girilen bir karakterin kaçıncı karakter olduğunu bulmak. Bunun için de indexOf komutunu kullanıyoruz.

sayi=ad.indexOf("e");

yazdığımızda sayi değişkenine 2 değeri atanır.

Ayrıca bu değişkenin uzunluğunu bulmak için lenght komutu kullanılır.

sayi=ad.lenght;

dediğimizde sayi değişkeninde 6 değeri bulunacaktır.

**Java Script'te Döngüler **

**For Döngüsü **

for (var i=0;i<10;i++)
{
window.write("Şu anda" + i + ". numaradasınız");
if (i==5) window.write("Yarısına geldiniz bile");
}

döngüsünde önce i değişkenine 0'dan başlaması gerektiğini, i 10'dan küçük olduğu sürece devam edeceğini ve i'nin birer birer artacağını söylüyoruz. Bu şartlarda ekrana "Şu anda 1. numaradasınız" , "Şu anda 2. numaradasınız" gibi mesajlar gelecek i, 5 olduğunda ise ayrıca "Yarısına geldiniz bile" mesajı gelecektir.

**While Döngüsü **

Bir döngüye ihtiyaç duyduğunuzda döngü içindeki işlemlerin kaç kere yapılması değil de bir durum gerçekleştiği sürece yapılması önemliyse while döngüsü kullanılır.

isim=array(""Ali","Ayse","Selim","Yahya","Kemal");
i=0;
j=0;
while(i != 1)
{
if isim\[j\]=="Yahya" i=1;
j++;
}

kodunda dizide "Yahya" ismini bulmak için bir döngü yarattık. Yahya ismini bulduktan sonra döngüde kalması programın yavaş çalışmasını sağlayacağından döngüyü 0'dan 4'e kadar for döngüsü yerine bir kontrol elemanının değerine bağladık. Yahya ismi bulununca kontrol değeri 1 yapıldı ve döngüden çıkıldı. J değeri ise Yahya isminin kaçıncı eleman olduğunu gösteren rakamın bir fazlasında kaldı.

**Break Komutu **

Herhangi bir şart gerçekleştiğine döngüden anında çıkmamız gerekiyorsa break komutunu kullanırız. Deminki örnekte Yahya ismini bulduğumuz halde kontrol döngünün başında olduğu için j bir kez daha artırıldı ve olmasını istediğimiz değerden bir fazla oldu. Oysa ki scripti şöyle yazsaydık:

isim=array(""Ali","Ayse","Selim","Yahya","Kemal");
i=0;
j=0;
while(i != 1)
{
if isim\[j\]=="Yahya"
{
i=1;
break;
}
j++;
}

Yahya ismi bulununca break komutuyla döngüden çıkacak ve j bir kez daha boşu boşuna artırılmamış olacaktı.

**Java Script'te Nesne Yaratmak **

Burada bahsedeceğimiz nesne birden fazla özelliği olan bir değişkendir. Bir insanın adı, soyadı, yaşı, kredi kart numarası gibi bilgileri tek bir değişken altında tutmak mümkündür. Bunun için de önce bunu yaratan bir fonksiyon yazıp sonra istediğimiz değişkeni gerekli parametrelerle bu fonksiyon cinsinden tanımlamalıyız.

function insan(ad,soyad,yas,kartno)
{
this.ad=ad;
this.soyad=soyad;
this.yas=yas;
this.kartno=kartno;
}
kisi\[1\]= new insan(Serdar,Kalaycı,22,1234567890123456)

Bu scriptte önce insan nesnesini yaratan fonksiyonu görüyoruz. Buradaki this keyword'ü bu nesneye ait olan özellikler için(sadece fonksiyonun içinde) kullanılır. Daha sonra kisi isimli dizinin birinci elemanını insan cinsinden yeni bir nesne olduğunu belirtmek için new keyword'ünü kullanarak ve gerekli parametreleri vererek fonksiyonu çağırıyoruz. Daha sonra gerekli özelliklere erişmek için kisi\[1\].ad , kisi\[1\].soyad ... yazılır.

**Özel Nesneler **

JScript'te bir önceki konuda anlattığımız gibi kendi tanımladığımız nesnelerin yanı sıra halihazırda var olan nesneler de vardır. Bizim için önemli olan document nesnesinin özelliklerini şöyle sıralayabiliriz.

window
parent,frame,self,\_top...
location
history
document
form
text field
text area
checkbox
radio
password
select
button
submit
reset
link
anchor

**Window Nesnesi **

Window nesnesi en üst düzeyli nesne olduğu için özellikleri ve metodların başlarına window. yazmaya gerek yoktur. Frame ve Status Bar window nesnesinin özellikleridir. Status Bar kontrolü

window.status="Merhaba Dünya";

gibi bir kodla kontrol edilebilir. Ayrıca window nesnesinin alert, prompt,confirm ve open gibi metodları vardır. Bunlardan alert ve prompt metodlarını daha önce gördük.

**Confirm Metodu: **

Confirm metodu kullanıcıdan onay almak için kullanılır. Kullanıcıya sorulan bir soruyu ve birer OK ve CANCEL butonu içerir.

**Java Script'te Form Nesneleri **

Nesneler JScript'te özel fonksiyonları bulunabilen birbirinden bağımsız elemanlardır. Text alanları, radio butonlar,check boxlar, butonlar ve drop-down menüler JScript nesneleridir.

Burada unutulmaması gereken durum nesnelerin bir form içinde olmaları yani <FORM> ve </FORM> HTML kodları arasında tanımlanmaları gerektiğidir. Tanımladığınız nesne içinde bulunduğu formun bir elemanıdır ve daha sonraulaşılması gerektiğinde form adıyla birlikte anılır.

<form name="form1">
<input type="button" name="but1" value="Buraya Basınız">
</form>

şeklinde tanıtılmış bir butona daha sonra erişmek istediğimizde form1.but1 yazmamız gerekecektir. Forma isim verilmediği durumlarda aynı butona form.but1 diye erişecektik ki aynı sayfada birden fazla form bulunması durumunda karışıklık çıkacaktı.

**Butonlar **

<form name="form1">
<input type="button" name="but1" value="Buraya Basınız">
</form>

Bu örnekte input type="button" giriş elemanının bir buton olduğunu, name="but1" programda bu butonu but1 olarak isimlendirdiğinizi value="Buraya Basınız" de butonun üzerinde Buraya Basınız metninin yazılacağını gösterir.

**Text Alanları **

<script language="Javascript">
function Goster (metin) {
alert(metin);
}

</script>
<form name="form1">
<input type="Text" name="text1" value="Buraya gireceğiniz yazı butona basınca alert olarak gelecektir.">
<input type="Button" name="buton1" value="Buraya Basın" onclick="Goster(form1.text1.value)">
</form>

Bu kodda Goster isimli bir fonksiyonumuz var ve metin ismiyle bir parametre alıyor.Daha sonra da bu parametreyi alert fonksiyonuyla gösteriyor. Bu parametreyi gönderen de butonun onclick olayı. Ve butonun gönderdiği parametre form1 formunun text1 nesnesinin değeri. Programda ilk olarak bu değeri Buraya gireceğiniz yazı butona basınca alert olarak gelecektir. vermiştik. Buradan da anlaşılacağı gibi bu değer text alanının içindeki metin. Yani text box'a birşey yazılmadığı durumda bu alanda Buraya gireceğiniz yazı butona basınca alert olarak gelecektir. yazacak ve butona basıldığında da uyarı kutusunda bu mesaj gelecektir.

Eğer çok satırlı bir text alanı yaratmak istiyorsak

<input type="Text" name="text1" value="Alanın içindeki yazı"> komutu yerine

<textarea name="TextBox" rows="10" cols="80">Alanın içindeki yazı</textarea>

Textarea tanımında rows alandaki satır sayısı, cols her bir satırın kaç karakter uzunluğunda olacağını belirten sayıdır.

**Radio Butonlar **

Radio Butonlar genellikle bir çok seçenekten sadece bir tanesinin seçilmesini istediğimiz durumlarda kullanılır. Radio butonların sadece bir tanesinin seçilmesini sağlamak için name özelliklerinin aynı olması gerekmektedir. Aşağıdaki örnekte bilgisayarınızın işlemcisinin markası sorulmaktadır:

<form name="form1">
<input type="radio" value="Intel" name="cpu" checked>
<input type="radio" value="Cyrix" name="cpu">
<input type="radio" value="AMD" name="cpu">
</form>

Değeri Intel olan radio butonda bulunan checked kodu sayfa açıldığına bu butonun işaretli olarak geleceğini belirtir. Radio butonların değerlerini alırken (örnekte üç tane olmasına rağmen) cpu adında tek bir nesnemiz varmış gibi form1.cpu.value dememiz gerekecektir. Seçili olan radio butonun değeri Intel, Cyrix veya AMD olarak gelecektir.

**Check Boxlar **

Check Boxlar da radio butonlar gibi iki durumlu giriş elemanlardır. Yalnız burada fark check boxların birden fazlasının da seçili olabilmesi durumudur. Her biri ayrı nesnedir ve her birinin seçili olma veay olmama durumu vardır. Durumunun anlaşılması ise checked komutu ile yapılmaktadır. Örneğin;

<input type="checkbox" name="chck1" value="1">

şeklinde tanımlanmış bir check box, daha sonra form.chck1.checked komutuyla kontrol edildiğinde seçili ise True seçili değilse False değeri getirecektir.

**Drop-Down Menüler **

Bu eleman birçok seçeneği açılan bir menü şeklinde sunar.

<script language="Javascript">
function goster(metin) {
alert(metin);
}
</script>
<select name="drp1" size="1"
onchange="goster (form.drp1.options\[drp1.selectedIndex\]value)">
<option value="Intel"<Intel</option>
<option value="Cyrix"<Cyrix</option>
<option value="AMD"<AMD</option>
</select>

Burada önemli olan bir özellik size özelliğidir. Kaç seçeneğin gösterilmesini istiyorsak size değerini o kadar artırmalıyız. Ayrıca bir çok eleman gibi onClick olayını değil onChange olayını kullanıyoruz. option value="Intel" seçildiğinde gönderilecek değeri, daha sonra yazdığımız isim de menüde gösterilecek yazıyı ifade eder.

<%@ language=JavaScript%>
<HTML>
<HEAD>
<SCRIPT>
</SCRIPT>
<TITLE>JavaScript Mesaj Denemeleri</TITLE>
</HEAD>
<BODY BGCOLOR=FFFFFF TEXT=000000>
<CENTER>
<FONT SIZE=+2>JavaScript Mesaj Denemeleri</FONT><BR>
</CENTER>
<HR>
<HR>
<FONT SIZE=+2>
<UL>
<LI><A HREF="INDEX1.HTML" OnClick="if(confirm('Emin misiniz!?')) alert('Emin oldugunuzu gormek guzel');else alert('Belki bir dahaki sefere');">Sana bir soru.</A>P>
<UL>
<LI>Status bar'a bak:
<A HREF="index.php3" onMouseOver="self.status='A secili';return true">A</A>
<A HREF="index.php3" onMouseOver="self.status='B secili';return true">B</A>
<A HREF="index.php3" onMouseOver="self.status='C secili';return true">C</A>
<A HREF="index.php3" onMouseOver="self.status='D secili';return true">D</A>
<A HREF="index.php3" onMouseOver="self.status='E secili';return true">E</A><P>
<UL>
<LI><A HREF=index.php3" onMouseOver="alert('Yaklaşma demiştim!')">Bana yaklaşma!</A><P>
</UL></UL></UL></UL>
</FONT><P><HR>
</BODY>
</HTML>

Bu örnekte kullanıcıya mesaj göndermenin değişik yolları gösterilmiştir. Confirm ve Alert komutlarının nasıl kullanıldığını görmüştük. İkinci satırda ise Status Bar'a mesaj yazdırmanın yolu görülüyor. Burada self.status denmesinin sebebi ise şu anda aktif olan nesnenin window nesnesi olasıdır. Bunun gibi herhangi bir nesne ile ilgili olarak yapacağımız işlemlerde **self **kullanacağız.

<HTML>
<HEAD>
<SCRIPT LANGUAGE=javascript>
<!--
function person(name,pass) {
this.name=name;
this.pass=pass;
}
function makearray(n) {
this.lenght=n;
for (var i=0;i<=n;i++) {
this\[i\]="";
return this;
}
}
function submit1\_onclick(form) {
var x=0;
pers= new makearray(3);
var isim;
var pas;
isim=text1.value;
pas=password1.value;
if(!isFieldBlank(isim)) alert('ID field cannot be blank');
else {
pers\[1\] =new person("serdar","");
pers\[2\] =new person("yucel","yucel");
pers\[3\] =new person("ali","veli");
for(i=1;i<4;i++) {
if(isim==pers\[i\].name) {
if(pas==pers\[i\].pass) x=1; }
}
if(x==1) document.write('You made a good job');
else alert('Password is invalid');
}
}
function isFieldBlank(ad) {
if(ad)
return true;
else
return false;
}
//-->
</SCRIPT>
</HEAD>
<BODY>
<P>
İsim:<BR>
<P><INPUT id=text1 name=text1 type=text></P>
<P> </P>
Şifre:<BR>
<INPUT id=password1 name=password1 type=password></P>
<P> </P>
<P><INPUT id=submit1 name=submit1 type=submit value=Gir onclick="submit1\_onclick()"></P> <P> </P>
</BODY>
</HTML>

Bu örneğimiz biraz karışık. Öncelikle iki tane form nesnemiz var. Biri text alanı diğeri ise password. Scriptimizde ise **person **isimli bir fonksiyonumuz var. Bu fonksiyondaki **this.name=name **komutu bu fonksiyonu çağıran değişkenin name özelliğinin name ismiyle aktarılan değişken olacağını gösterir. **pers\[3\] =new person("ali","veli"); **satırında olduğu gibi pers dizisinin 3. elemanı name özelliği ali, pass özelliği veli olan bir yapı olacak.

**isfieldblank **fonksiyonu parametre olarak aktarılan alanın boş olup olmadığını kontrol eden fonksiyonumuz. İsim alanı boş olamayacağından önce bunu kontrol edip eğer boşsa bir uyarı mesajı gönderiyoruz.

**makearray **fonksiyonu daha önce de bahsettiğim gibi dizi yaratmak için yazılmış bir fonksiyon. Aynı şekilde bu fonksiyonu çağıran değişkeni aktarılan parametre uzunluğunda bir dizi yapıyor. **pers **dizisi bu fonksiyonla yaratıldıktan sonra her bir elemanına **person **fonksiyonu tarafından name ve pass özellikleri atanıyor. Gerisi ise oldukça basit. Alanlara girilen değerler bir döngü içerisinde pers dizisinin elemanlarıyla karşılaştırılıyor.

**Java Script Kullanarak Yeni Bir Pencere Açmak **

Aşağıdaki scriptte butona tıklayarak yeni bir ekran açılması için bir örnek vardır.Burada kullanılan birtakım özellikler olacaktır.

window.close() komutunun özellikleri yoktur. Sadece o anda aktif olan pencereyi kapatır. window.open(özellikler) komutundaki özellikler ise:
"HTML" ; gösterilmesini istediğimiz sayfa
"window.name" ; istediğimiz bir başlık
"toolbar" ; toolbar'ın gösterilme özelliği (yes/no ya da 0/1 olarak belirtilir).
"status" ; statusbar'ın gösterilme özelliği (yes/no ya da 0/1 olarak belirtilir).
"menubar" ; menubar'ın gösterilme özelliği (yes/no ya da 0/1 olarak belirtilir).
"scrollbars" ; scrollbar denilen sayfayı aşağı-yukarı ve sağa-sola oynatmamızı sağlayan barların gösterilme özelliği (yes/no ya da 0/1 olarak belirtilir).
"resizable" ; açılacak olan ekranın boyutunun değiştirilebilir olup olmama özelliği (yes/no ya da 0/1 olarak belirtilir).
"width" ; genişlik (pixel olarak belilenir).
"height" ; yükseklik (pixel olarak belirlenir).

Gelelim scriptimize ve nasıl kullandığımıza:

<script language="Javascript">
function ekranac()
options='toolbar=0,status=0,menubar=0,scrollbars=0,resizable=0,width=300,height=200';
content=
'<body bgcolor="beige">'+
'<p align="left"><big><strong>Selam !</strong></big><br></p>'+
'<p align="left"><small>Buraya basarak ekranı kapatabilirsiniz</small></p>'+
'<form name="kapat"><input type="button" value="Ekranı Kapat !" onclick="window.close()">'+
'</form>';
acilan = window.open("","mywindow",options);
acilan.document.write(content)
</script>
<form name="ekrandeneme">
<input type="button" value="Ekran Aç !" onclick="ekranac()">
</form>

Script çok basit ve öğrenmesi kolay. Özellikleri biliyosanız window.open komutunu kullanmak zor olmayacaktır. Fakat Netscape Navigator'ın bazı bozuklukları sebebiyle bizim scriptimizde yaptığımız gibi bu özellikleri bir değişkene atayarak kullanmak yararlı olacaktır.

ekran = window.open("http://www.programlama.com","programlama",options)

gibi... Böylece ekrana da Javascript'in anlayabileceği bir isim vermiş oldunuz; "ekran". Bu ismi kullanarak açılan yeni ekrana istediğinizi yaptırabilirsiniz. Bu özelliği aklınızda tutun. Çünkü frame kontrolünde de bu özellik kullanılmaktadır.

ekran.document.write('Selam')

gibi pek çok komutu "ekran" isimli yeni açılan ekrana aktarabiliriz.
Aşağıdaki scripti kullanarak komutları ve özellikleri biraz daha rahat öğrenebilirsiniz. Her boşluğu doldurmak zorunda değilsiniz. Tek tek de denemeniz mümkün.

Bu komut Internet Explorer'ın bazı sürümlerinde çalışmamaktadır.

**Kullanıcının Tarayıcısını Kontrol Etmek **

Daha önce de gördüğümüz gibi Javascript komutları tarayıcılara göre değişiklik gösterebiliyor veya hiç çalışmıyor. Bu durumlarda kullanıcının kullandığı tarayıcıyı tespit etmek ve ona göre hareket etmek akıllıca olacaktır. Bunun için kullanılan fonksiyon:

navigator.appName

Tabi sadece tarayıcıyı tespit etmek yeterli olmayabilir. Tarayıcı tanımlama ile ilgili tüm komutlar :

navigator.appName
navigator.appVersion
navigator.CodeName
navigator.userAgent

Javascript ile kullanıcının bilgisayarından o anki tarihi ve saati almanız mümkün. Internet tüm dünyaya hitap ettiğinden sizin sayfanızın bulunduğu Web Server ile kullanıcının bilgisayarındaki saat ve tarih birbirine uymayabilir. Böyle bir durumda kullanıcının bilgisayarından saati ve tarihi almak faydalı olabilir.
Önce saatin ve tarihin atanacağı bir değişken ile new Date() fonksiyonu çağırılır.
zaman = new Date() Böylece zaman isimli değişkenin bir tarih değişkeni olduğunu belirttik. Fakat bu şekilde alınan tarih ve zaman bilgileri ekranda biraz düzensiz görülür. 14 Eylül 1998 tarihinde saat 22:10'da alınan bilgi ekranda şu şekilde görünecektir:
Fri Aug 14 22:10:54 UTC+0300 1998 Bunu daha anlaşılı bir şekle sokmak için JScript'in .toLocaleString() komutundan yararlanılır.
Deminki örneğimizde aldığımız zaman değişkenini zaman.toLocaleString() fonksiyonundan geçirdikten sonra alacağımız sonuç:

**08/14/1998 22:10:37 **şeklinde olur.

Aynı zamanda kullanacağımız şu zaman fonksiyonlarıyla alacağımız değerler de şöyle olur:

| **KOMUT ** | **YANIT ** | **AÇIKLAMA ** |
| --- | --- | --- |
| **zaman.getDay() ** | 5 | Haftanın günü (0 = Pazar) |
| **zaman.getMonth() ** | 7 | Ay (0 = Ocak , 0 - 11 arası) |
| **zaman.getDate() ** | 14 | 14 Ayın kaçıncı günü |
| **zaman.getYear() ** | 98 | Yıl |
| **zaman.getHours() ** | 22 | Saat |
| **zaman.getMinutes() ** | 10 | Dakika |
| **zaman.getSeconds() ** | 37 | Saniye |
| **zaman.getTime() ** | 903122773920 | "1 Ocak 1990 Geceyarısı" tarihinden itibaren geçen milisaniye |
| **zaman.getTimezoneOffset() ** | -180 | Greenwitch'e göre (GMT) dakika olarak saat farkı |

**Java Script'te Resim İşleme **

Aşağıdaki örnek Internet'te sıkça kullanılan ve Java Button diye anılan butonların nasıl çalıştığına bir örnektir. Bu butonlar mouse pointer üstlerine geldiği anda değişiyorlar ve pointer üstlerinden çekildiğinde eski hallerine dönüyorlar. Biz de bu işlemi yapan bir fonksiyon yazacağız ve butonun onMouseOver ve onMouseOut olaylarını bu fonksiyona göndererek resmi değiştireceğiz.

<html>
<head>
<script LANGUAGE="JavaScript">
{
res1 = new Image();
res1.src = "resim1.gif";
res2= new Image();
res2.src="resim2.gif";
}
function changeImage(imgDocId,imgObjName) {
document.images\[imgDocId\].src = eval(imgObjName + ".src");
}
// --></script>
</head>
<body>
<a href="http://www.programlama.com" onMouseOver="changeImage('buton','res1')"
onMouseOut="changeImage('buton','res2')">
<img src="resim1.gif" border="0" name="buton"></a><br>
</body>
</html>

Bir de Internet'te her gün rastladığımız linklere renk ve hareket getirecek bir script örneği verelim:

<HTML>
<HEAD>
<STYLE>
.on {
font-size:12;
text-decoration:underline;
color:red;
}
.off {
font-size:12;
color:black;
}
</STYLE>
</HEAD>
<BODY>
<A HREF="http://www.programlama.com" class="off" onMouseOver="this.className='on';" onMouseOut="this.className='off';">Gel Bakalim</A>
</BODY>
</HTML>
Burada STYLE tag'i içinde iki adet class tanımlıyoruz ve bunlara on ve off adlarını veriyoruz. Linkimize de başlangıç olarak off classını atıyoruz. onMouseOver olayında linkin classını on, onMouseOut olayında ise tekrar off yapıyoruz. Örnekte normalde siyah olan link, üzerine gelindiğinde kırmızı ve alt çizgili olmaktadır. Bu classların yapılarıyla oynayarak çok değişik linkler elde etmek mümkün

---
*Kaynak: `JAVA SCRİPT/ekitap-Anonim-Javascript_Eklemek/java script.htm`*
*Görseller: `Java-Script/gorseller/` (2 dosya)*
