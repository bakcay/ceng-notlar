# CSharp Notlari

Bu makalemizde TCP protokolüyle basit bir Client/Server programı

yapacağız, C# ile socket programlama yapabilmek için System.Net.Sockets

isimalanı altında bulunan sınıfları kullanacağız. Yapacağımız programda

server bir console uygulaması, client ise windows formlarını kullanarak

yapacağımız windows uygulaması olacak.Amacımız basit bir Client/Server

çatisi kurmak olduğu için uygulamamız çok basit olacaktır. Siz yazının

tamamını dikkatlice incelediğinizde ve yaratıcılığınızı kullandığınızda

çok daha gelişmiş uygulamalar yapabilirsiniz. Belki bir sunucu tabanlı

script dili bile geliştirebilirsiniz :).

şimdi yazacağımız programda kullanıcı Windows uygulaması vasıtası ile

server olan programımıza bağlanacak. Form üzerinde bulunan butona

tıkladığımızda yine form üzerinde bulunan textbox girişindeki yazıyı server

programımız alacak ve yazıda kaç karakter olduğunu client programına

gönderecek.Client program ise bir mesaj kutusu ile kullanıcıya

bildirecek.Öncelikle client olan kullanıcıdan mesajın geldiğini düşünürek Server

programımızı yazalım. Server programımızı yazmaya başlamadan önce

programda Soket programlama için kullandığımız sınıflara ve onların üye

fonksiyonlarına kullandığımız kadarıyla bir göz atalım.

:::: TcpListener Sınıfı(System.Net.Sockets) ::::

TcpListener sınıfı TCP protokolü ile çalışan servislere bağlanmamızı

sağlar. Mesela HTTP ve FTP protokolleri TCP servislerini kullanırlar.

TcpListener sınıfının kurucu fonksiyonunu 3 değişik şekilde çağırabiliriz.

1- )IPEndPoint sınıfını kullanarak IP numarası ve port numarası içeren

bir bilgiyi kullanma yolu ile

2- )IP adresi ve port numarasını geçerek çağırma

3- )Sadece Port numarası ile çağırma.Bu durumda varsayılan ağ

arayüzünüz TCP servislerini sağlayacaktır.

Biz bu programda 3. şıktaki gibi bir kullanımı tercih ettik.

```csharp
public void Start();
```

TcpListener sınıfına ait bu metod network servislerinden ilgili port'u

dinleyerek verileri almaya başlamamızı sağlar.

```csharp
public Socket AcceptSocket();
```

TcpListener sınıfına ait bu metod veri transferi için geri dönüş değeri

olarak bir Socket nesnesi döndürür.Bu geri dönen socket ilgili

makinanın IP adresi ve port numarası ile kurulur.(kurucu işlev ile)

:::: Socket Sınıfı(System.Net.Sockets) ::::

Socket Sınıfı ile ilgili aşağıdaki örneği inceleyelim

```csharp
Socket s = new Socket(AddressFamily.InterNetwork,
SocketType.Stream,ProtocolType.Tcp );
```

Socket sınıfının bu kurucu işlevi parametre olarak AdressFamily

dedigimiz adresleme semasi Soket tipi ve kullanacagimiz protokol tipini alir.

Bu 3 paremtere de .NET Framework class kütüphanesinde Enum sabitleri

olarak tanimlanmistir.

Programimizda yazdigimiz "Socket IstemciSoketi =

TcpDinleyicisi.AcceptSocket();" satiri ile geri dönen soket nesnesinde bu 3 parametrede

tanimlanmistir.

```csharp
public bool Connected();
```

Bu metod ile Soketin baglanip baglanmadigini geri dönen bool degeri ile

anliyoruz.Eger soket hedef kaynaga bagliysa true degilse false degerine

geri döner.

:::: NetworkStream Sinifi(System.Net.Sockets) ::::

NetworkStream sinifi kurucularindan olan "void NetworkStream(Socket

x);" fonksiyonu ilgili kendisine gönderilen soket nesnesine ait datalari

NetworkStream türünden nesnede tutar.bu programda kullandigimiz soket

tipi stream oldugu için bu sinifi kullaniyoruz. NetworkStream sinifi

içinde islem yapabilmemeiz için ise System.IO isiamalaninda bulunan

StreamReader ve StreamWriter siniflarini kullanacagiz.

Ön bilgileri aldığımıza göre server programımızı yazalım. Aşağıdaki ilk

kaynak kod server.cs dir. Satır aralarına size yardımcı olabilecek

yorumlar ekledim.Kaynak dosyayı özellikle makaleme dosya olarak

eklemiyorumki siz aşağıdaki kodları tek tek yazıp daha iyi öğrenin.

:::: TcpClient Sinifi(System.Net.Sockets) ::::

Tcp servislerine bağlantı sağlamak için TcPClient sınıfı kullanılır.

Istemci programımızda TcpClient sınıfının <public TcpClient(string,

int);> kurucu işlevini kullanıyoruz. İlk parametre bilgisayar adı ikincisi

ise port numarasıdır.

```csharp
public NetworkStream GetStream();
```

Bu metod ile belirtilen port tan gelen veriler bir NetworkStream

nesnesine aktarılır. GetStream metodunun geri dönüş değeri NetworkStream

olduğu için atama işlemini NetworkStream türünden bir nesneye yapmamız

gerekir.

Not: Yeşil ile yazılan satırlar yorum satırlarıdır.Html formatında bir

alt satıra inmiş olan yorum satırlarını copy&paste ile programınıza

aktarırken o satırları tekrar tek satır haline getirmeyi unutmayın, aksi

halde programınız derlenemez.

```csharp
//Server.cs
using System; // bunu her zaman eklememiz lazim
using System.IO ; //StreamReader ve StreamWriter siniflari için
using System.Net.Sockets; // Socket, TcpListener ve NetworkStrem
siniflari için
public class Server
{
public static void Main()
{
//Bilgi alisverisi için bilgi almak istedigimiz port numarasini
TcpListener sinifi ile gerçeklestiriyoruz
TcpListener TcpDinleyicisi = new TcpListener(1234);
TcpDinleyicisi.Start();
Console.WriteLine("Sunucu baslatildi...") ;
//Soket baglantimizi yapiyoruz.Bunu TcpListener sinifinin
AcceptSocket metodu ile yaptigimiza dikkat edin
Socket IstemciSoketi = TcpDinleyicisi.AcceptSocket();
// Baglantının olup olmadığını kontrol ediyoruz
if (!IstemciSoketi.Connected)
{
Console.WriteLine("Sunucu baslatilamiyor...") ;
}
else
{
//Sonsuz döngü sayesinde AgAkimini sürekli okuyoruz
while(true)
{
Console.WriteLine("Istemci baglantisi saglandi...");
//IstemciSoketi verilerini NetworkStream sinifi türünden
nesneye aktariyoruz.
NetworkStream AgAkimi = new NetworkStream(IstemciSoketi);
//Soketteki bilgilerle islem yapabilmek için StreamReader ve
StreamWriter siniflarini kullaniyoruz
StreamWriter AkimYazici = new StreamWriter(AgAkimi);
StreamReader AkimOkuyucu = new StreamReader(AgAkimi);
//StreamReader ile String veri tipine aktarma islemi önceden
bir hata olursa bunu handle etmek gerek
try
{
string IstemciString = AkimOkuyucu.ReadLine();
Console.WriteLine("Gelen Bilgi:" + IstemciString);
//Istemciden gelen bilginin uzunlugu hesaplaniyor
int uzunluk = IstemciString.Length;
//AgAkimina, AkimYazını ile IstemciString inin uzunluğunu
yazıyoruz
AkimYazici.WriteLine(uzunluk.ToString());
AkimYazici.Flush() ;
}
catch
{
Console.WriteLine("Sunucu kapatiliyor...");
return ;
}
}
}
IstemciSoketi.Close();
Console.WriteLine("Sunucu Kapatiliyor...");
}
}
```

İşte buda Istemci programımız. Öncelikle şunu belirtiyimki aşağıdaki

kodların çoğunu Visual C# kendiliğinden hazırladı, o yüzden size Tavsiyem

Visual C# kullanmanız. Öncelikle aşağıdaki şekilde gördüğünüz form

yapısını benzer bir form hazırlayın.Sonra da buton_click metodunu

form_kapatma metodunu ve using ifadelerini ekleyin. Yada zamanınız çoksa

aşağıdaki kodları teker teker yazın. (İsteyene kaynak kodu da gönderebilirim)

```csharp
//client.cs
using System;
using System.Net.Sockets;
using System.IO ;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
public class Form1 : System.Windows.Forms.Form
{
//Burda server da tanımladıklarımızdan farklı olarak TcpClient sınıfı
ile serverdan gelen bilgileri alıyoruz
public TcpClient Istemci;
private NetworkStream AgAkimi;
private StreamReader AkimOkuyucu;
private StreamWriter AkimYazici;
private System.Windows.Forms.Button buton;
private System.Windows.Forms.TextBox textbox;
private System.ComponentModel.Container components = null;
public Form1()
{
InitializeComponent();
}
protected override void Dispose( bool disposing )
{
if( disposing )
{
if (components != null)
{
components.Dispose();
}
}
base.Dispose( disposing );
}
private void InitializeComponent()
{
//Bu satırları Visual C# oluşturdu.
this.buton = new System.Windows.Forms.Button();
this.textbox = new System.Windows.Forms.TextBox();
this.SuspendLayout();
this.buton.Location = new System.Drawing.Point(8, 40);
this.buton.Name = "buton";
this.buton.Size = new System.Drawing.Size(248, 23);
this.buton.TabIndex = 0;
this.buton.Text = "Sunucuya Baglan";
this.buton.Click += new System.EventHandler(this.buton_Click);
this.textbox.Location = new System.Drawing.Point(8, 8);
this.textbox.Name = "textbox";
this.textbox.Size = new System.Drawing.Size(248, 20);
this.textbox.TabIndex = 1;
this.textbox.Text = "Buraya Sunucuya göndereceginiz yaziyi yazin";
this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
this.ClientSize = new System.Drawing.Size(264, 69);
this.Controls.AddRange(new System.Windows.Forms.Control[] {
this.textbox,
this.buton});
this.MaximizeBox = false;
this.Name = "Form1";
this.Text = "C#nedir?com";
this.Closing += new
System.ComponentModel.CancelEventHandler(this.form1_kapatma);
this.Load += new System.EventHandler(this.Form1_Load);
this.ResumeLayout(false);
}
//giriş noktamız olan mainde yeni bir form1 nesnesini çalıştırıyoruz
static void Main()
{
Application.Run(new Form1());
}
//From1 yüklendiğinde TcpClient nesnesi oluşturup
AgAkımından(NetworkStream) verileri okuyoruz
private void Form1_Load(object sender, System.EventArgs e)
{
try
{
Istemci = new TcpClient("localhost", 1234);
}
catch
{
Console.WriteLine("Baglanamadi");
return;
}
//Server programında yaptıklarımızı burda da yapıyoruz.
AgAkimi = Istemci.GetStream();
AkimOkuyucu = new StreamReader(AgAkimi);
AkimYazici = new StreamWriter(AgAkimi);
}
}
private void buton_Click(object sender, System.EventArgs e)
{
//Kullanıcı butona her tıkladığında textbox'ta yazı yoksa uyarı
veriyoruz
//Sonra AkimYazici vasıtası ile AgAkımına veriyi gönderip sunucudan
gelen
//cevabı AkimOkuyucu ile alıp Mesaj la kullanıcıya gösteriyoruz
//Tabi olası hatalara karşı, Sunucuya bağlanmada hata oluştu mesajı
veriyoruz.
try
{
if (textbox.Text=="")
{
MessageBox.Show("Lütfen bir yazi giriniz","Uyari");
textbox.Focus();
return ;
}
string yazi;
AkimYazici.WriteLine(textbox.Text);
AkimYazici.Flush();
yazi = AkimOkuyucu.ReadLine();
MessageBox.Show(yazi,"Sunucudan Mesaj var");
}
catch
{
MessageBox.Show("Sunucuya baglanmada hata oldu...");
}
}
//TVe bütün oluşturduğumuz nesneleri form kapatıldığında kapatıyoruz.
public void form1_kapatma(object o , CancelEventArgs ec)
{
try
{
AkimYazici.Close();
AkimOkuyucu.Close();
AgAkimi.Close();
}
catch
{
MessageBox.Show("Düzgün kapatilamiyor");
}
}
```

-------------------------------------------------------------------------------------------

NOT DEFTERİ

Ben bu resime kullandığım kontrollerin isimlerini de yazdım ki kodları

incelerken zorluk çıkmasın. Yalnız burada görünmeyen 2 kontrol daha

var. Biri SaveFileDialog (objSave), diğeri OpenFileDialog (objOpen). Bu

kontrolleri de ekleyip adlarını parantez içlerindeki gibi yaparsanız

sorun çıkmaz…

Şimdi kodlarımıza geçebiliriz. Bu bölümde adım adım ilerleyeceğiz.

Menülerdeki tüm başlıkların olaylarını yazacağız.

1)Genel değişkenimizi tanımlama

Bu programda Degisim adında, “bool” yani sadece true ve false değerleri

alabilen bir değişken tanımladım. Bu değişken sayesinde kullanıcıyı

metinin değişip değişmediği konusunda uyaracağız, böylece isterse değişen

metni kayıt imkanı vereceğiz…

```csharp
private bool Degisim;
```

2)Form1’in onLoad Olayı

Bu olay programımızın açılışında yürütülen olaydır. Burada objSave ve

objOpen için bazı ayarlar yapıyoruz ve göstermesini istediğimiz

dosyaların uzantılarını giriyoruz.

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
objOpen.Filter = "Text Dosyaları(*.txt)|*.txt|Tüm
Dosylar(*.*)|*.*" ;
objOpen.FilterIndex = 1 ;
objSave.Filter = "Text Dosyaları(*.txt)|*.txt|Tüm
Dosyalar(*.*)|*.*" ;
objSave.FilterIndex = 1 ;
}
```

3)Kullanılacak metotların tanımlanması…

Ben bu programda sadece 2 tane metot tanımladım. Bunlardan birincisi

KayitMekanizmasi, diğeri DegisimUyari . KayitMekanizmasi adı üstünde

yazdıklarımızı kaydedecek olan mekanizma, DegisimUyari ise objText içindeki

metnin değişimi durumda programı kapatırken falan bize haber verecek

olan kod.

```csharp
public void KayitMekanizmasi(string strVeri)
{
if (objSave.ShowDialog() == DialogResult.OK)
{
StreamWriter Kayitci = new
StreamWriter(Environment.GetEnvironmentVariable("mydocuments")+objSave.FileName.ToString(),false,System.Text.Encoding.Unicode);
Kayitci.Write(strVeri);
Kayitci.Close();
Degisim = false;
}
}
```

Önce yukarıdaki kodu biraz inceleyelim. Burada önce bi if kontrolü

görüyorsunuz. Bu kontrolün amacı, Kayıt ekranı açıldığı zaman kullanıcı

“OK” düğmesine tıklayıp tıklamadığını kontrol etmek. Eğer “OK”e tıkladı

ise programımız bir adet StreamWriter oluşturuyor. Kayitci adındaki bu

Writer Environment.GetEnvironmentVariable("mydocuments”) bu kod ile

ayarlı olan Belgelerim klasörüne gidiyor otomatik olarak. objSave.FileName

ise bizim Kayıt Ekranın da dosyaya verdiğimiz ismi bize döndürüyor. Son

olarak ise bu satırda Unicode bir kodlama yaptığımız gösteriyoruz. Bunu

yazmazsanız Türkçe karakterlerinizin yerinde yeller estiğini

görürsünüz.

Kayitci.Write(strVeri) satırı ile gelen veriyi kaydediyor ve

StreamWriter nesnesini kapatıyor. Degisim değerini ise true olarak atıyor. Bunun

nedeni değişim oldu ve ben bunu gördüm demek. Kullanıcıya haber vermeye

gerek yok anlamına gelecek.

Şimdi devam edelim.

```csharp
public bool DegisimUyari()
{
if (MessageBox.Show("Dosyanızda bir değişiklik oldu kaydetmek
ister misiniz?","Değişiklik
Var",MessageBoxButtons.YesNo,MessageBoxIcon.Exclamation) == DialogResult.Yes)
{
return true;
}
else
{
Degisim = false;
return false;
}
}
```

Yukarıdaki kodda ise tipik bir MessageBox kullanımı görüyorsunuz.

Buradaki metodumuz birde değer döndürüyor.Bir bool değeri döndürüyor. Bu

dönen değer ile biz az sonra kullanıcının çıkan mesaj kutusunda dosyayı

kaydetmek isteyip istemediğini anlayacağız.

```csharp
MessageBox.Show("Dosyanızda bir değişiklik oldu kaydetmek ister
misiniz?","Değişiklik Var",MessageBoxButtons.YesNo,MessageBoxIcon.Exclamation)
== DialogResult.Yes)
```

Bu satırı biraz incelemek lazım. Burada ilk overload (Overload

metodlara parantezler içinde yollanan veri demek.) mesaj kutusunda görünecek

olan yazı, ikinicisi bu mesaj kutusunun başlığı, üçüncüsü mesaj kutusu

üzerinde ki “Evet”, “Hayır” düğmeleri ve son olarak mesaj kutusundaki

simge. Ancak kodlara bakmaya devam ettiğimizde bir karşılaştırma görüyoruz

(“==” ifadesi) DialogResult.Yes , aslında açıklamaya bile gerek yok.

Eğer kullanıcı “Evet”e tıkladı ise demek. Asıl kodlarda bu durumda bir

“true” ifadesi döndürüldüğünü görebilirsiniz. Biz daha sonra bunu kontrol

ederek KayitMekanizmasi metodumuzu çağıracağız.

4) Yeni düğmesi

Menümüzdeki “Yeni” düğmesine tıkladığımızda olacak olayları gireceğiz.

Bunun için bu düğmeye Designer’dan çift tıklayınız.

```csharp
private void menuItem2_Click(object sender, System.EventArgs e)
{
if (Degisim == false)
{
objText.Clear();
}
else
{
if (DegisimUyari())
{
KayitMekanizmasi(objText.Text);
objText.Clear();
Degisim = false;
}
else
{
objText.Clear();
Degisim = false;
}
}
}
```

Burada önce Degisim değerini kontrol ediyoruz. Eğer değer “false” ise

yani değişim yoksa ya bu dosya önceden kaydedilmiştir ya da yeni

açılmıştır. O zaman içeriğinin temizlenmesinde bir sorun yok.

Eğer değer “true” ise biraz karışıyor ortalık. Önce kullanıcıyı uyarmak

için DegisimUyari() çalıştırılıyor. Eğer kullanıcı kayıt etmek

istiyorsa, KayitMekanizmasi() çalıştırılıyor, ekran temizleniyor ve Degisim

değeri false oluyor.Eğer kullanıcı kayıt etmek istemiyorsa içerik

temizleniyor ve Degisim değeri yine false oluyor. Böylece yeni bir dosya açma

işlemlerini hallettik.

5) Varolan dosyayı açma

Metin editörünüz ile daha önce var olan bir dosyayı açmak istersiniz

diye böyle bir özellik ekledik birde. Menümüzde “Aç”a çift tıklayın ve

tıklama olayına aşağıdaki kodları girin.

```csharp
private void menuItem3_Click(object sender, System.EventArgs e)
{
if (Degisim == true)
{
if (DegisimUyari())
{
KayitMekanizmasi(objText.Text);
}
}
if (objOpen.ShowDialog() == DialogResult.OK)
{
FileInfo strKaynak = new
FileInfo(Environment.GetEnvironmentVariable("mydocuments")+objOpen.FileName.ToString());
StreamReader Okuyucu = strKaynak.OpenText();
objText.Text = Okuyucu.ReadToEnd();
Degisim = false;
Okuyucu.Close();
}
}
```

Bu kodlarda da önce değişim var mı diye bakıyoruz. Yani amacımız

kullanıcının yazdığı metni yanlışlıkla bastığı bir düğme yüzünden

kaybetmesini engellemek. Eğer değişim varsa ve uyarıdan “true” değeri dönerse

kaydediyoruz, aksi halde herhangi bir şey yapmıyoruz.

Bundan sonra yukarıda SaveFileDialog için yaptığımız benzer şeyleri

yapıyoruz. Yani .ShowDialog() metodunu çağırıyoruz. Kullanıcı OK’e

tıklayınca kodlarımız devam ediyor. Ancak burada yukarıdakinden farklı kodlar

var. Dosya okumak için çok farklı yöntemler var. Yazmak içinde tabi ki.

Mesela StreamWriter’ın StreamReader’ı da var ve ben burada bunu

kullandım. Eğer kodları incelerseniz biraz farklı olduğunu göreceksiniz. Çünkü

burada FileInfo diye de bir şey var. FileInfo bu tür dosya

işlemcilerine yardımcı olur. strKaynak değişkenine atadığımız nesnemizde

StreamWriter daki gibi path gösterip dosyamızı açıyoruz. Burada

objOpen.FileName’den gelen veri, kullanıcının açmak istediği dosya.

StreamReader nesnesini de oluşturup strKaynak.OpenText() ile metin

dosyamızı açıyoruz. Yalnız burada bir noktaya dikkat çekmek istiyorum. Ben

burada açılacak dosyanın bir .txt dosyası olduğunu bildiğim için

.OpenText’i kullandım. Yoksa başka versiyonları da mevcut. Bu nesneyi de

oluşturduktan sonra objText’e Okuyucu.ReadToEnd ile baştan sonra tüm veriyi

okuyup aktarıyoruz. Değişimden haberimiz olduğunu programa bildirip,

nesnelerimizi kapatıyoruz…

6) Kaydet düğmesi

Kullanıcı çalışmasını kaydetmek istediği zaman bu düğmeye tıklayabilir.

Çok kısa bir kodu var. Zaten asıl işi yapan KayitMekanizmasi(), biz

sadece onu çağıracağız şimdi.

```csharp
private void menuItem4_Click(object sender, System.EventArgs e)
{
KayitMekanizmasi(objText.Text);
Degisim = false;
}
```

Burada açıklanacak bir kod yok. Gördüğünüz gibi …

7) Kapat Düğmesi

Kullanıcı programı kapatmak isteyebilir ve bunun için Dosya menüsündeki

Kapat düğmesini kullanabilir. O zaman bu düğmeye de bir olay atamamız

lazım. Şimdi çift tıklayın ve aşağıdaki kodları yazın.

```csharp
private void menuItem6_Click(object sender, System.EventArgs e)
{
Close();
}
```

Bu kod çok basit. Sadece Close() metodunu çağırıyor. Bu özel tanımlı

bir metodur ve o form penceresinin kapanmasını sağlar. Şimdi aklınıza

gelebilir ya içeride kaydedilmemiş veri varsa hiç kontrol etmedik. O zaman

biraz sabır, ona da bakacağız…

8) Kapanmadan önce kontrol

Kullanıcımız programı çok farklı şekillerde kapatabilir. Alt + F4

kombinasyonu, köşedeki X ile kapatabilir ya da Kapat düğmemize tıklar;ancak

az önce de dediğimiz gibi ya içeride veri varsa. O zaman bu veri için

bi kontrol yapmamız lazım. Form’ların “Closing” adında olayları vardır.

Bu form kapatılmadan hemen önce yapılacakları belirler. Biz buna bazı

olaylar atıyoruz şimdi.

```csharp
private void Form1_Closing(object sender,
System.ComponentModel.CancelEventArgs e)
{
if (Degisim == true)
{
if (DegisimUyari())
{
KayitMekanizmasi(objText.Text);
Close();
}
}
else
{
Close();
}
}
```

Burada yapılanlardan farklı olan hiç bir şey yok. Degisim değerini

kontrol ediyoruz ve ona göre işlem yapıyoruz..

9) Son bir metod…

Asıl en önemli şeyi yapmadık sanıyorum. Örneğin kullanıcı programa bir

veri girdiğinde yani herhangi bi yazı yazdığında Degisim değeri

değişmedi. O zaman bunu halledelim. objText’in TextChanged adında bir olayı

var. Şimdi o olay kodları içine aşağıdaki tek satırlık kodu yazıyoruz.

```csharp
private void objText_TextChanged(object sender, System.EventArgs e)
{
Degisim = true;
}
```

Evet, böylece olayın iş yapan kısmı bitti..

Ancak menülerimiz arasında hiç ilgilenmediğimiz bir düğme var.

Hakkında. Bu aslında en gereksiz şey belki ama bir programcının en çok

önemsediği bölüm :). Bunun için basit bir form yaratınız. Ben aşağıdaki formu

oluşturdum ve adını “hakkinda” yaptım.

Burada altta iki tane de link var. Biri MaxiASP.Com ‘a biri

MaxiASP.Net’e yönlenmiş durumda. Bunlara tıklandığında tarayıcımızın açılıp

sitelere gitmemizi sağlayacak kodlarda aşağıda.

```csharp
private void linkLabel1_LinkClicked(object sender,
System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
System.Diagnostics.Process.Start("http://www.maxiasp.com");
}
private void linkLabel2_LinkClicked(object sender,
System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
System.Diagnostics.Process.Start("http://www.maxiasp.net");
}
```

--------------------------------------------------------------------------------------------

```csharp
using System;
namespace StructSample1
{
struct Zaman
{
private int saat,dakika,saniye;
private string kosucuAdi;
public string Kosucu
{
get
{
return kosucuAdi;
}
set
{
kosucuAdi =value;
}
}
public int Saat
{
get
{
return saat;
}
set
{
saat =value;
}
}
public int Dakika
{
get
{
return dakika;
}
set
{
dakika =value;
}
}
public int Saniye
{
get
{
return saniye;
}
set
{
saniye =value;
} } }
class Class1 {
static void Main (string[] args)
{ Zaman z;
Console.WriteLine ("Koşucu:"+z.Kosucu);
Console.WriteLine ("Saat:"+z.Saat.ToString());
Console.WriteLine ("Dakika:"+z.Dakika.ToString());
Console.WriteLine ("Saniye:"+z.Saniye.ToString());
} }}
```

------------------------------------------------------------------------------------------

Dolayısıyla bizde yazdığımız sınıflara ait constructorları overload edebiliriz. Şimdi dilerseniz overload ile ilgili olaraktan kısa bir uygulama geliştirelim. Bu uygulamada yazdığımız bir sınıfa ait constructor metodları overload ederek değişik tipte fonksiyonellikler edinmeye çalışacağız.

Bu uygulamada KolayVeri isminde bir sınıfımız olucak. Bu sınıfın üç adet yapıcısı olucak. Yani iki adet overload constructor yazıcaz. İki tane diyorum çünkü C# zaten default constructoru biz yazmasak bile uygulamaya ekliyor. Bu default constructorlar parametre almayan constructorlardır. Overload ettiğimiz constructor metodlardan birisi ile, seçtiğimiz bir veritabanına bağlanıyoruz. Diğer overload metod ise, parametre olarak veritabanı adından başka, veritabanına bağlanmak için kullanıcı adı ve parola parametrelerinide alıyor. Nitekim çoğu zaman veritabanlarımızda yer alan bazı tablolara erişim yetkisi sınırlamaları ile karşılaşabiliriz. Bu durumda bu tablolara bağlantı açabilmek için yetkili kullanıcı adı ve parolayı kullanmamız gerekir. Böyle bir olayı canlandırmaya çalıştım. Elbetteki asıl amacımız overload constructor metodların nasıl yazıldığını, nasıl kullanıldığını göstermek. Örnek gelişmeye çok, hemde çok açık. Şimdi uygulamamızın bu ilk kısmına bir gözatalım. Aşğıdakine benzer bir form tasarım yapalım.

Şimdi sıra geldi kodlarımızı yazmaya. Öncelikle uygulamamıza KolayVeri adında bir class ekliyoruz. Bu class’ın kodları aşağıdaki gibidir. Aslında uygulamaya bu aşamada baktığımızda SqlConnection nesnemizin bir bağlantı oluşturmasını özelleştirmiş gibi oluyoruz. Gerçekten de aynı işlemleri zaten SqlConnection nesnesini overload constructor’lari ile yapabiliyoruz. Ancak temel amacımız aşiri yüklemeyi anlamak olduğu için programın çalışma amacının çok önemli olmadığı düşüncesindeyim. Umuyorum ki sizlere aşırı yükleme hakkında bilgi verebiliyor ve vizyonunuzu geliştirebiliyorumdur.

```csharp
using System;
using System.Data.SqlClient;
namespace Overloading
{
public class KolayVeri
{
/* Connection'in durumunu tutacak ve sadece bu class içinde geçerli olan bir string değişken tanımladık. private anahtar kelimesi değişkenin sadece bu class içerisinde yaşayabilceğini belirtir. Yazmayabiliriz de, nitekim C# default olarak değişkenleri private kabul eder.*/
private string baglantiDurumu;
/* Yukarıda belirttiğimiz baglantiDurumu isimli değişkenin sahip olduğu değeri, bu class'a ait nesne örneklerini kullandiğımız yerde görebilmek için sadece okunabilir olan (readonly), bu sebeplede sadece Get bloğuna sahip olan bir özellik tanımlıyoruz.*/
public string BaglantiDurumu
{
get
{
/* Bu özelliğe eriştiğimizde baglantiDurumu değişkeninin o anki değeri geri döndürülecek. Yani özelliğin çagırıldığı yere döndürülücek.*/
return baglantiDurumu;
}
}
/* Iste C# derleyicisinin otomatik olarak eklediği parametresiz yapıcı metod. Biz bu yapıcıya tek satırlık bir kod ekliyoruz. Eğer nesne örneği parametresiz bir Constructor ile yapılırsa bu durumda bağlantının kapalı olduğunu belirtmek için baglantiDurumu değişkenine bir değer atıyoruz. Bu durumda uygulamamızda bu nesne örneğinin BaglantiDurumu özelliğine eristiğimizde BAĞLANAMADIK değerini elde edeceğiz.*/
public KolayVeri()
{
baglantiDurumu="BAĞLANAMADIK";
}
/* Bizim yazdığımızı aşırı yüklenmiş ilk yapıcı metoda gelince. Burada yapıcımız, parametre olarak bir string alıyor. Bu string veritabanının adını barındırıcak ve SqlConnection nesnemiz için gerekli baglantı stringine bu veritabanının adını geçiricek.*/
public KolayVeri(string veritabaniAdi)
{
string connectionString="initial catalog="+veritabaniAdi+";data source=localhost;integrated security=sspi";
/* SqlConnection baglantımız yaratılıyor.*/
SqlConnection con=new SqlConnection(connectionString);
/* Baglantı işlemini bir try bloğunda yapıyoruz ki, herhangi bir nedenle Sql sunucusuna bağlantı sağlanamazsa (örnegin hatalı veritabanı adı nedeni ile) catch bloğunda baglantiDurumu değişkenine BAĞLANAMADIK değerini atıyoruz. Bu durumda program içinde KolayVeri sınıfından örnek nesnenin BaglantiDurumu özelliğinin değerine baktığımızda BAĞLANAMADIK değerini alıyoruz böylece bağlantının saglanamadığına kanaat getiriyoruz. Kanaat dedikte aklima Üsküdarda ki Kanaat lokantasi geldi :) Yemekleri çok güzeldir. Sanirim karnımız acıktı... Neyse kaldığımız yerden devam edelim.*/
try
{
con.Open(); // Bağlantımız açılıyor.
/* BaglantiDurumu özelliğimiz (Property), baglantiDurumu değişkeni sayesinde BAĞLANDIK değerini alıyor.*/
baglantiDurumu="BAGLANDIK";
}
/* Eğer bir hata olursa baglantiDurumu değiskenine BAĞLANAMADIK değerini atıyoruz.*/
catch(Exception hata)
{
baglantiDurumu="BAGLANAMADIK";
}
}
/* Sıra geldi ikinci overload constructor metoda. Bu metod ekstradan iki parametre daha alıyor. Bir tanesi user id'ye tekabül edicek olan kullaniciAdi, diğeri ise bu kullanıcı için password'e tekabül edecek olan parola. Bunları SqlConnection'in connection stringine alarak , veritabanına belirtilen kullanıcı ile giriş yapmış oluyoruz. Kodların işleyişi bir önceki metodumuz ile aynı.*/
public KolayVeri(string veritabaniAdi,string kullaniciAdi,string parola)
{
string connectionString="initial catalog="+veritabaniAdi+";data source=localhost;user id="+kullaniciAdi+";password="+parola;
SqlConnection con=new SqlConnection(connectionString);
try
{
con.Open();
baglantiDurumu="BAGLANDIK";
}
catch(Exception hata)
{
baglantiDurumu="BAGLANAMADIK";
}
}
}
}
```

Şimdi sıra geldi, formumuz üzerindeki kodları yazmaya.

```csharp
string veritabaniAdi;
private void lstDatabase_SelectedIndexChanged(object sender, System.EventArgs e)
{
veritabaniAdi=lstDatabase.SelectedItem.ToString();
/* Burada kv adında bir KolayVeri sınıfından nesne örneği (object instance) yaratılıyor. Dikkat edicek olursanız burada yazdığımı ikinci overload constructor'u kullandık.*/
KolayVeri kv=new KolayVeri(veritabaniAdi);
/* Burada KolayVeri( dediğimizde .NET bize kullanabileceğimiz aşırı yüklenmiş constructorları aşagıdaki şekilde olduğu gibi hatırlatacaktır. IntelliSence’in gözünü seveyim.*/
```

Sekil 4. 2nci yapıcı

```csharp
stbDurumBilgisi.Text=lstDatabase.SelectedItem.ToString()+" "+kv.BaglantiDurumu;
}
private void btnOzelBaglan_Click(object sender, System.EventArgs e)
{
string kullanici,sifre;
kullanici=txtKullaniciAdi.Text;
sifre=txtParola.Text;
veritabaniAdi=lstDatabase.SelectedItem.ToString();
KolayVeri kvOzel=new KolayVeri(veritabaniAdi,kullanici,sifre);
/* Burada ise diğer aşırı yüklenmiş yapıcımızı kullanarak bir KolayVeri nesne örneği oluşturuyoruz.*/
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

C - 9 : enum türlerinin kullanımına bir örnek :

```csharp
namespace Foo
{
enum Colors
{
BLUE,
GREEN
}
class Bar
{
Colors color;
Bar() { color = Colors.GREEN;}
public static void Main() {}
}
}
```

--------------------------------------------------------------------------

S - 10 : Geri dönüş değeri olmayan bir metot bildirimi yaptığımda neden (CS1006) hatası almaktayım?

C - 10 : Bir metodun geri dönüş değerini yazmadan bildirirseniz derleyici onu sanki bir yapıcı metot bildiriyormuşsunuz gibi davranır. O halde geri dönüş değeri olmayan bir metot bildirimi için void anahtar sözcüğünü kullanın. Aşağıda bu iki kullanıma örnek verilmiştir.

```csharp
// Bu bildirim CS1006 hatası verir.
public static staticMethod (mainStatic obj)
// Bu metot ise istenildiği gibi çalışır.
public static void staticMethod (mainStatic obj
```

-------------------------------------------------------------------------------------------------------------------------

C - 22 : C# özellikleri destekler ancak Item özelliğinin sınıflar için özel anlamı vardır. Item özelliği aslında varsayılan indeskleyici olarak yer alır. Bu imkanı C# ta elde etmek için Item sözcüğünü atmak yeterlidir. Aşağıda örnek program gösterilmiştir.

```csharp
using System;
using System.Collections;
class Test
{
public static void Main()
{
ArrayList al = new ArrayList();
al.Add( new Test() );
al.Add( new Test() );
Console.WriteLine("First Element is {0}", al[0]);
}
}
```

-------------------------------------------------------------------------------------------

S - 39 : C#'ta string türünden bir değişkeni int türüne nasıl dönüştürebilirim?

C - 39 : Aşağıda bu duruma bir örnek verilmiştir.

```csharp
using System;
class StringToInt
{
public static void Main()
{
String s = "105";
int x = Convert.ToInt32(s);
Console.WriteLine(x);
}
}
```

--------------------------------------------------------------------------------------------

```csharp
using System;
public class TryTest
{
static void Main()
{
try
{
Console.WriteLine("In Try block");
throw new ArgumentException();
}
catch(ArgumentException n1)
{
Console.WriteLine("Catch Block");
}
finally
{
Console.WriteLine("Finally Block");
}
}
}
```

-------------------------------------------------------------------------------

C#'ta göstericilerin kullanımı ile ilgili yazı dizisinin son bölümü olan bu yazıda gösericiler ile dizi islemlerinin nasıl yapıldıgi, stackalloc ıle dinamik bellek tahsısatının yapılmasını ve son olarak yapı(struct) göstericilerinin kullanılışını inceleyeceğiz.

Göstericiler ile Dizi İşlemleri

C#'ta tanımladıgımız diziler System.Array sınıfi türündendir. Yani bütün diziler managed type kapsamına girerler. Bu yüzden tanımladıgımız bir dizinin herhangi bir elemanının adresini fixed bloğu kullanmadan bir göstericiye atayamayız. Bu yüzden göstericiler ile dizi islemleri yaparken ya fixed bloklari kullanıp gereksiz nesne toplayıcısını uyarmalıyız yada stackalloc anahtar sözcüğünü kullanarak kendimiz unmanaged type(yönetilemeyen tip) dizileri olusturmalıyız. Her iki durumuda birazdan inceleyeceğiz.

Bildiğiniz gibi dizi elemanları bellekte ardışıl bulunur. O halde bir dizinin elemanlarını elde etmek için dizinin ilk elemanının adresini ve dizinin boyutunu bilmemiz yeterlidir. System.Array sınıfı dizilerinin elemanlarina göstericiler yardimiyla rahatlıkla ulasabiliriz. Bunun için ilk olarak fixed ile isaretlenmis bir blok içerisinde dizinin ilk elemanının adresini bir göstericiye atamalıyız. Ardından göstericinin degerini bir döngü içerisinde birer birer artırdıgımızda her döngüde dizinin bir sonraki elemanina ulaşmış oluruz. Dizilere bu sekilde erisebilmemizi sağlayan ise gösterici aritmetiğidir. Tabi dizilerin elemanlarının bellekte ardışıl bulunması da bu işlemi bu şekilde yapmamızı sağlayan ilk etkendir.

Şimdi yönetilen türden(managed) bir dizinin elemanlarına nasıl eriştiğimizi bir örnek üzerinde inceleyelim.

```csharp
using System;
class Gosterici
{
unsafe static void Main()
{
int[] a = {1,2,3,4};
fixed(int* ptr = &a[0])
{
for(int i=0; i<a.Length; ++i)
Console.WriteLine(*(ptr+i));
}
}
}
```

Programı derlediğinizde dizinin elemanlarının

1

2

3

4

seklinde ekrana yazdırıldığını görürsünüz. (programı derlerken /unsafe argümanını kullanmayı unutmayın). Programın kritik noktası

```csharp
fixed(int* ptr = &a[0])
```

satırı ile dizinin ilk elemanının adresinin elde edilmesidir. Zira dizinin diğer elemanlarıda sırayla ilk elemandan itibaren her eleman için adres değeri 4 byte artacak şeklindedir. Diger önemli nokta ise for döngüsü içindeki

```csharp
*(ptr+i)
```

ifadesidir. Bu ifade her döngüde ptr göstericisinin adres bileşeni, döngü degişkeni kadar artırılıyor, sözgelimi döngü degişkeni 1 ise ptr'nin adres bileşeni 4 artırılıyor. Bu da dizinin ikinci elemanının bellekte bulunduğu adrestir. İçerik operatörü ile bu adrese erişildiğinde ise dizinin elemanı elde edilmis olur.

Gösterici dizileri ile ilgili diğer önemli nokta göstericilerin indeksleyici gibi kullanılabilmesidir. Örneğin yukarıdaki örnekte bulunan

```csharp
*(ptr+i)
```

ifadesini

```csharp
ptr[i]
```

şeklinde degiştirebiliriz. Burdan aşağıdaki eşitlikleri çıkarabiliriz.

```csharp
*(ptr+0) == ptr[0]
*(ptr+1) == ptr[1]
*(ptr+2) == ptr[2]
*(ptr+3) == ptr[3]
```

Dikkat: ptr[i] bir nesne belirtirken (ptr+i) bir adres belirtir.

Dizilerin isimleri aslinda dizilerin ilk elemanının adresini temsil etmektedir. Örneğin aşagıdaki programda bir dizinin ilk elemanının adresi ile dizinin ismi int türden bir göstericiye atanıyor. Bu iki göstericinin adres bileşenleri yazdırıldıgında sonucun aynı olduğu görülmektedir.

```csharp
using System;
class Gosterici
{
unsafe static void Main()
{
int[] a = {1,2,3,4};
fixed(int* ptr1 = a, ptr2 = &a[0])
{
Console.WriteLine((uint)ptr1);
Console.WriteLine((uint)ptr2);
}
}
}
```

Programı derleyip çalıştırdığınızda ekrana alt alta iki tane aynı sayının yazıldığını görürsünüz.

Yönetilen(managed) tiplerle çalışmak her ne kadar kolay olsa da bazı performans eksiklikleri vardır. Örneğin bir System.Array dizisinin bir elemanına erişmek ile stack bölgesinde olusturacagımız bir dizinin elemanına ulaşmamız arasında zaman açısından büyük bir fark vardır. Bu yüzden yüksek performanslı dizilerle çalışmak için System.Array sınıfının dışında stack tabanlı diziler oluşturmamız gerekir. Stack tabanlı diziler yönetilemeyen dizilerdir. Bu yüzden bu tür dizileri kullanırken dikkatli olmalıyız. Çünkü her an bize tahsis edilmeyen bir bellek alanı üzerinde islem yapiyor olabiliriz. Ancak yönetilen dizilerde dizinin sınırlarını aşmak mümkün degildir. Hatırlarsanız bir dizinin sınırları aşılınca çalışma zamanında IndexOutOfRangeException istisnai durumu meydana geliyordu. Oysa stack tabanlı dizilerde dizinin sınırları belirli degildir ve tabiki dizinin sınırlarını aşmak kısıtlanmamıştır. Eğer dizinin sınırları aşılmışsa muhtemelen bu işlem bir hata sonucu yapılmıştır. Hiçbir programcı kendisine ait olmayan bir bellek alanında islem yapmamalıdır. Aksi halde sonuçlarına katlanması gerekir.

Stack tabanlı diziler stackalloc anahtar sözcüğü ile yapılır. stackalloc bize istediğimiz miktarda stack bellek bölgesinden alan tahsis eder. Ve tahsis edilen bu alanın başlangıç adresini geri döndürür. Dolayısıyla elimizde olan bu baslangıç adresi ile stackalloc ile bize ayrılmış olan bütün bellek bölgelerine erişebiliriz. stackalloc anahtar sözcüğünün kullanımı aşağıdaki gibidir.

```csharp
int * dizi = stackalloc int[10];
```

Bu deyim ile stack bellek bölgesinde 10*sizeof(int) = 40 byte'lık bir alan programcının kullanmasi için tahsis edilir. Bu alan, dizinin faaliyet alanı bitinceye kadar bizim emrimizdedir. Tahsis edilen bu 40 byte büyüklüğündeki bellek alanının ilk byte'ının adresi ise int türden gösterici olan dizi elemanına aktarılır. Dolayısyla dizi göstericisi ile içerik operatörünü kullandığımızda bize ayrılan 10 int'lik alanın ilk elemanına erişmiş oluruz.

! stackalloc ile tahsis edilen bellek alanlarının ardışıl olması garanti altına alınmıştır.

stackalloc ile alan tahsisatı yapılır. Ancak alan tahsisatı yapılan bellek bölgesi ile ilgili hiçbir islem yapılmaz. Yani yukaridaki deyim ile, içinde tamamen rastgele değerlerin bulundugu 40 byte'lık bir alanımız olur. Bu alandaki değerlerin rastgele degerler olduğunu görmek için asagidaki programı yazın.

```csharp
using System;
class Gosterici
{
unsafe static void Main()
{
int * dizi = stackalloc int[10];
for(int i=0; i<10;++i)
Console.WriteLine("*(dizi+{0}) = {1}",i,dizi[i]); }
}
}
```

---------------------------------------------------------------------------------------------------

Bu makalede nesne yönelimli programlama tekniğine kadar kullanılan yazılım geliştirmedeki yaklaşımlara göz atacağız. Daha sonra nesne yönelimli programlamanın temel kavramları ve neden böyle bir tekniğin kullanıldığı üzerinde duracağız.

Yazılım Geliştirme ve Bu Alandaki Yaklaşımlar

Kimilerine göre geçtiğimiz yüzyılın en önemli buluşu olarak kabul edilen bilgisayar teknolojisi, baş döndürücü bir hızla gelişmektedir. Bilişim sektöründeki değişimler bazen varolan teknolojilere yenilerinin eklenmesi şeklinde olabilir. Diğer taraftan bir kısım yenilikler vardır ki bu alanda büyük değişimlere ve evrimlere yolaçar. Mesela; kişisel bilgisayarların kullanılmaya başlanması veya internetin belli başlı akademik kurumların ve askeri organizasyonların tekelinden alınıp tüm insanlığın hizmetine sunulması gibi.

Hepimizin bildiği gibi bir bilgisayar sistemi iki ana parçadan oluşur. Bunlar donanım(hardware) ve yazılım(software). Donanımın yazılım ile uyumlu çalişması sonucunda sistemlerimiz sorunsuz bir şekilde bizlere hizmet verirler. Ayrıca donanımın amacımimza uygun hizmet vermesi uygun yazılımın geliştirilip kullanılmasına baglıdır.

Yazılım sektöründe program geliştirme konusunda günümüze kadar bir çok yaklaşim denenmiştir. Bunların ilki programın baştan aşağıya sırası ile yazılıp çalıştırılmasıdır. Bu yaklaşımla BASIC dili kullanılarak bir çok program yazıldığını biliyoruz. Burda sorun programın akışı sırasında değişik kısımlara goto deyimi ile atlanmasıdır. Program kodu bir kaç bin satır olunca, kodu okumak ve yönetmek gerçekten çok büyük sorun oluyordu.

ıkinci yaklaşım ise prosedürel yaklaşımdır. Programlarda bir çok işin tekrar tekrar farklı değerleri kullanılarak yapıldığı farkedildi. Mesela herhangi bir programda iki tarih arasında ne kadar gün olduğunu bulmak birçok kez gerek olabilir. Bu durumda başlangıç ve bitiş tarihlerini alıp aradaki gün sayısını veren bir fonksiyon yazılabilir ve bu fonksiyon ihtiyaç duyulduğu yerde uygun parametrelerle çağrılıp istenen sonuç elde edilebilir. Prosedürel yaklaşım Pascal ve C dillerinde uzun yıllar başari ile kullanılmıştır.

Ama her geçen gün programların daha karmaşık bir hal alması, program kodunun kurumsal uygulama projelerinde onbinlerce satırı bulması ve yazılım geliştirme maliyetinin çok arttiğını gören bilim adamları, programcılara yeni bir yaklaşımın kullanılabilineceğini öğrettiler. Bu yakaşımın ismi Nesne Yönelimli Programlama(Object Oriented Programlama)dır.

Nesne yönelimli programlama tekniği, diger yaklaşımlara nazaran, yazılım geliştiren insanlara büyük avantajlar sağlamaktadır. Birincisi karmaşık yazılım projelerinin üretilmesini ve bakımını kolaylaştırıyor olmasıdır. Diğeri ise program kodunun tekrar kullanılabilmesine (code-reusability) olanak sağlamasıdır. Bu noktada program kodunun tekrar kullanılabilmesi profesyonel yazılım şirketlerinin maliyetlerini azaltmıştır. Dolayısi ile programların lisans ücretleri düşmüş ve sektörün sürekli olarak canlı kalmasına ve rekabet içinde gelişmesine yardımcı olmuştur.

Nesne Yönelimli Programlama Nedir?

Nesne yönelimli programlamada esas olan, gerçek hayatta varolan olguların programlamaya aktarılmasındaki yeni yaklaşımdır. Prosedürel programlamada verilerimiz ve fonksiyonlarımız vardı. Yani veri ve bu veriyi işleyen metodlar etrafinda dönüyordu herşey.

Aslında nesne yönelimli programlamada da iki önemli birim veri ve veriyi işleyip mantıklı sonuçlar üreten metodlar bulunur. Ama burdaki fark gerçek hayattaki olguların da daha iyi gözlenip programlama dünyasına aktarılmasındadır.

Mesela elimizde bir ütümüz olsun. Ütünün markası, modeli, rengi, çalıstığı elektrik voltajı, ne tür kumaşları ütüleyebildiği bu ütüye ait özelliklerdir (veri). Aynı zamanda ütümüzü ısıtabiliriz, ütüleme işinde kullanabiliriz ve soğumaya bırakabiliriz. Bunlar ise ütünün fonksiyonalarıdır(metod). Eğer ütü ile ilgili bir program yapmış olsak ve nesne yönelimli programlama tekniğini kullansak hemen bir ütü sınıfı(class) oluştururduk. Bu sınıfta ütüye ait bilgiler (veriler) ve ütü ile yapabileceğimiz işler(metod) bulunurdu. O zaman nesne yönelimli programlama da bir sınıfta, sınıfa ait veriler ve bu verileri işleyip bir takiı faydalı sonuçlar üreten fonksiyonlar/metodlar bulunur.

Dahası, biz birtane ütü sinifi tasarlarsak bu sınıftan istediğimiz sayıda değişik ütüler(object veya instance) yapabiliriz. Ağagidaki şekilde ütü sınıfı ve bu sınıftan oluşturduğumuz neslerin görsel olarak anlatımı bulunmaktadır.

---
*Kaynak: `C# NOTLARI/Odevsitesi_com_32585.txt`*
