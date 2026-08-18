# Bir Text Dosyasi Oluşturmak

## **Bir Text Dosyası oluşturmak**

Sunucunun herhangi bir dizininde bir text dosyasını, ASP komutları ile oluşturmak istersek, *CreateTextFile* nesnesini kullanmamız gerekir.

Bu komutun kullanımı şöyledir.

**Set dosya\_nesnesi = CreateObject("Scripting.FileSystemObject")**

**Set dosya\_degiskeni =dosya\_nesnesi.CreateTextFile**

**("c:\\dosya\_degiskenii\_deneme.txt",false)**

## **Bir Text dosyası oluşturmak ve yazdırmak**

ASP sayfamız üzerinde bir text dosyası oluşturduktan sonra sıra geldi bu dosyamızın içine yazı yazmaya bunu ***Write & WriteLine***** **komutları ile yapacağız.

**<HTML>**

**<BODY>**

**<%**

**Set dosya\_nesnesi = CreateObject("Scripting.FileSystemObject")**

**Set dosya\_degiskeni = dosya\_nesnesi.CreateTextFile**

**("c:\\yazi\_deneme.txt",false)**

**dosya\_degiskeni.WriteLine("Bu bir denemedir.")**

**dosya\_degiskeni.Close**

**%>**

**</BODY>**

**</HTML>**

## **Bir Text Dosyasından Okumak**

Metin yazdırma işlerinde sık sık uygulayacağımız bir senaryo, mevcut bir metin dosyasına ek yapmak olacaktır. Örneğin bütün ziyaretçilerimizin sitemizdeki konuk defterine yazdıklarını, bir metin dosyasında toplamak isteyebiliriz.

Bunu OpenTextFile metodu ile yapacağız. Bu metod, tahmin edeceğiniz gibi, açılacak dosyanın yolunu ve adını isteyecektir. Örneğin, ilgili satır şöyle olacak:

**Set dosya\_degiskeni = Dosya\_degiskeni.OpenTextFile ("c:\\inetpub\\wwwroot\\yazi\_deneme.txt",8,0)**

veya **Set dosya\_degiskeni = Dosya\_degiskeni.OpenTextFile ("server.MapPath(“yazi\_deneme.txt"),8,0)**

Burada dosya yolunu ve adını veren birinci argümana ek olarak iki yeni argüman görüyorsunuz: “8,0” şeklinde. Bunlardan birinicisi girdi/çıktı durumu (I/O Mode), ikincisi ise biçim (Format) ile ilgilidir. I/O Mode parametreleri şunlardır:

1: okumak için aç

2: yazmak için aç

8: eklemek için aç

Açılacak dosyanın biçimini belirttiğimiz son argüman ise şu değerlerden birini alabilir:

0: ASCII dosyası olarak aç

-1: Unicode dosyası olarak aç (Örneğin içinde Türkçe karakterler varsa)

-2: Sistemin varsayılan dosya türü olarak aç

Buna göre, bir dosyayı salt okumak için açmak amacıyla “1,0” argümanlarını kullanmamız

Yararlanabileceğimiz diğer metodlar ise şunlardır:

**Read**** (oku):** Bir sayı örgümanı ile çalışır ve verdiğiniz sayı kadar karakter okur.

**ReadLine**** (satır oku):** Bir satır okur ve String olarak verir.

**ReadAll**** (tümünü oku):** Bütün satırları okur ve tek String olarak verir.

**Skip**** (atla):** Bir sayı argümanı ile çalışır ve verdiğiniz sayı kadar karakteri atlar.

**SkipLine**** (satır atla):** Bir sonraki satıra atlar.

Bu metodlarla sağladığımız okuma işinin kontrolü amacıyla şu özellikleri de kullanabiliriz:

**AtEndOfStream**** (akımın sonunda):** Okutulan dosyanın sonuna gelinmesi halinde True (doğru) olur.

**AtEndOfLine**** (satırın sonunda):** Okutulan satırın sonuna gelinmesi halinde True (doğru) olur.

## **Text Dosyasının Başından Belirli Sayıda Karakter Okutmak**

Read metodunun bir özelliği ile text dosyamızın başlangıç karakterinden itibaren kaç karakteri okuyacağımızı sunucuya bildirebiliriz.

Kullanımı:

response.write(dosya\_degiskeni.read(10))

## **Text Dosyasının Başından Belirli Sayıda Karakter Atlamak**

Yukarıdaki işlemlerin tam tersidir. Bu yöntemle text dosyamızın başından, belirttiğimiz adette karakter atlanır.

Kullanımı:

Dosya\_degiskeni.skip(*sayı*)

response.write(dosya\_degiskeni.readAll)

## **Text Dosyasından Satır Okumak**

Dilersek oluşturduğumuz text dosyasından satır okutabiliriz. Bunun komutu ***Response.Write(dosya\_degiskeni.ReadLine) ***‘dır. *** ***

## **Text Dosyasından Bütün Satırları Okumak**

Text dosyalarındaki tüm satırları okumak için ***Response.Write(dosya\_degiskeni.ReadLine) ***komutunu kullanırız.

Eğer satır satır okutmak istiyorsak döngü içine şu komutları kullanmamız gerekir.

**do while dosya\_degiskeni.AtEndOfStream=false**

**Response.Write(dosya\_degiskeni.ReadLine) **

**Response.Write(“<br>”)**

**loop**

## **Text Dosyasındaki Belirli Bir Satırı Okumak**

Diyeli ki 3. satırı okumak istiyoruz bunun için if karar yapısından yardım almalıyız

Kullanımı :

do while dosya\_degiskeni.AtAndOfStream =False

okunan\_satir = dosya\_degiskeni.ReadLine

if 3=dosya\_degiskeni.line then

response.write okunan\_satır

end if

## **Text Dosyasından Satır Atlamak**

Text dosyasından satır atlamak ***SkipLine*** Komutuyla yapılır

Kullanımı :

***Dosya\_degiskeni.SkipLine ***

Diyeli ki 3. satırı atlamak ve diğer tüm satırları yzdırmak istiyoruz. Bunun için *if then else* karar yapısını kullanacağız.

Örnek :

do while dosya\_degiskeni.AtAndOfStream =False

if 3=dosya\_degiskeni.line then

dosya\_degiskeni.SkipLine

else

Response.Write(dosya\_degiskeni.ReadLine)

end if

## **ÖNSÖZ**

ASP veya Active Server Pages (Etkin Sunucu Sayfaları) tekniği, sayfalarınızı canlandıracak bir tekniktir. Bu teknik, bir kaç sayfa sonra göreceksiniz ki, sil baştan bir bilgisayar programlama dili öğrenmeye gerek olmadan uygulanabilir. Bu kitapçığı yazarken sizinle yolun başından beri beraber olduğumuzu, yani HTML bildiğinizi varsayıyorum. Ayrıca Web’in nasıl çalıştığını, Server (Sunucu) ve Client (İstemci) ilişkisinin nasıl yürüdüğünü de biliyor olmalısınız.

ASP teknolojisinden yararlanmak istediğinizde Web sitesine evsahipliği yapan bilgisayarda çalışmakta olan Web Server’ın ASP teknolojisini tanıması ve sitenize bu hizmeti vermesi gerekir. ASP, bir zamanlar sadece Microsoft’un NT ve daha sonra Windows 2000 işletim sistemine dayanan MS-IIS (Internet Information Server) programında işleyebilirdi. Fakat şimdi artık NT-tabanlı diğer Web Server programları gibi Unix-tabanlı Web Server programları da ASP anlar ve işletir hale gelmiş bulunuyor. Fakat ASP sayfalarınızı gerçek Internet ortamında ziyaretçilerinizin hizmetine sunmadan önce, kendi bilgisayarınızda sınamanız gerekir. Bunun için bilgisayarınızın işletim sistemi Windows 95/98 ise Kişisel Web Server (PWS), NT 4.0 ise IIS kurulmuş olmalıdır. Sisteminiz Windows 2000 ise, IIS 5.0 kendiliğinden kurulmuş demektir.

Şimdi biraz ASP’den söz edelim. Bu kısaltmayı, “a..se..pe” veya “ey-es-pi” diye harf-harf okuyanlar olduğu gibi, “eyspi” diye bir kelime halinde okuyanlar da vardır; ve bana sorarsanız, hepsi de doğrudur. Internet programcıları, bütün görevi bir sabit diskteki HTML dosyalarını alıp, ziyaretçinin Browser’ına göndermekten ibaret olan Web Server programını yeniden tasarlamaya başladıklarında, Server’ın sadece durağan sayfaları göndermesi yerine, ziyaretçiden de veri kabul etmesinin uygun olacağını düşündüler. Bu amaçla Internet istemcisi ile sunucusunun buluştuğu noktada, yani Common Gateway Interface (Ortak Geçit Arayüzü) katmanında Web Server programının, istemci programdan (browser) kendisine bilgi ve komutlar gönderilmesini sağladılar. Örneğin bir Form’daki bilgilerin alınıp, bir dosyaya kaydedilmesi için vereceğimiz komut, sitemizin bulunduğu bilgisayarın işletim sisteminde CGI katmanı tarafından icra ettirilir. Bu manada CGI, Web Server’ın Internet ziyaretçisinin Browser’ın gelen bilgi ve komutları işlediği veya kendi işletim sistemine aktardığı noktadır. Bu gelişmenin sonucu olarak ortaya CGI programı dediğimiz şeyler çıktı. Perl, C/C++, Delphi, Visual Basic ile yazılan bu programlar Web Server tarafından çalıştırılır, ve vereceği komutlar işletim sistemine iletilir.

CGI programları ile çok şey yapılabilir; fakat Web Server’a aynı anda birden fazla kişi erişir ve aynı CGI programını çalıştırırsa, (yani aynı anda aynı formun “Gönder” düğmesini tıklarlarsa), CGI programının birden fazla “kopyası” çalışmaya başlar. Aynı anda aynı forma ulaşan kişi sayısı 4-5 ise bu belki sorun oluşturmaz; ama bu sayı arttıkça Web Server da adeta yerlerde sürünmeye başlar! Özetle CGI programları Web Server’ı yavaşlatır.

Microsoft programcıları biraz geriden gelmekle birlikte Server işine el attıklarında, istemci ile sunucunun etkileşmesini, bütün sistemi yavaşlatan “haricî” programlar yerine, işletim sisteminin bir işlevi haline getirebileceklerini düşündüler. Bunun yolu ise işletim sisteminin Uygulama Programı Arayüzü (API, Application Programming Interface) denen unsurlarını kullanmaktı. Nitekim Microsoft, oturup bir dizi Internet Server API (veya kısaca ISAPI) tasarladı. ISAPI, tıpkı CGI gibi, Web Server programının bulunduğu bilgisayardaki diğer programlarla alışverişini sağlar. Ne var ki ISAPI’den yararlanan programlar üreterek bunları Web Server’ın emrine vermek oldukça pahalı bir yol. Başka bir deyişle, bir formda Gönder düğmesinin çalışabilmesi için sözgelimi Excel ayarında bir program yazdırtmak pek akıl kârı olmasa gerek.

Bu noktada çeşitli firmalar ISAPI benzeri “yorumlayıcılar” geliştirerek, düz yazı bir Script yazmakla ve bu Script’in içindeki komutları Server programına icra ettirmekle, Web tasarımcısının hayatını çok kolaylaştırabileceklerini gördüler. Microsoft’un bu noktadaki çözümü ASP oldu. Yani bir bakıma “Server’a Aktif Sayfalar sunma” teknolojisi! NetObjects firması kendi Server Extension’larını geliştirdi. Linux-Unix dünyasında bir başka grup PHP dilinden yararlanarak PHP Sayfaları sistemini geliştirdi. Bunlardan sadece MS’un ASP teknolojisi birden fazla dil ile Script kabul edebilen teknoloji olarak, diğerlerinden ayrıldı. Bu noktaya birazdan geleceğiz; ama önce “ASP nasıl çalışır?” sorusunun üzerinde duralım.

Ama önce biraz başa dönelim: Siz Web ziyaretçisi olarak Browser’ınızın URL hanesine bir HTML sayfasının Internet yolunu ve adını yazıp (örneğin, http://www.pclife.com.tr/index.htm) Git düğmesini tıkladığınızda veya klavyede Enter/Return tuşuna bastığınız zaman ne olur? Web Server, Internet’in bulutları arasından geçip kendisine gelen bu istem üzerine, index.htm’i bulur ve yine aynı bulutların arasından sizin blgisayarınıza kadar gönderir. ASP teknoloji ile üreteceğiniz sayfanın adının uzatması ise .asp şeklinde olur. Siz bu kez URL hanesine bu dosyanın adını (örneğin http://www.pclife.com.tr/index.asp) yazarsınız. Bu durumda Web Server, bu sayfayı alıp, doğruca size göndermez: önce içindeki kodları icra eder. Sonra bu kodları ayıklar ve geriye saf ve temiz HTML kalır. Ve bu sayfa, bizim Browser’ımıza gönderilir.

Yukarıdaki son üç cümleyi lütfen yeniden okur musunuz? Nelere dikkat ettiniz:

1. ASP sayfasının içinde kod vardır.

2. ASP sayfasının kodları Web Server tarafından icra edilir.

3. ASP sayfası, Browser’a salt HTML olarak gelir.

Şimdi burada ASP ile Javascript’in farkını görebiliyor musunuz? Javascript, HTML’in içine konuluyor; ama Server’da değil, Browser’da çalışıyor. Peki CGI/Perl programı ile ASP’nin farkını görebiliyor musunuz? HTML sayfasını Perl ile yazdığınız program üretiyor (print “<HTML>\\n”; kodunu hatırlıyor musunuz?); oysa ASP’de ziyaretçiye gidecek HTML’i Server ve tasarımcı birlikte üretiyorsunuz. Bu bakımdan, Javascript “istemci-tarafında” çalışırken, ASP, CGI programları gibi, “sunucu-tarafında” çalışır. Bunun sonucu ise ASP ile yazacağınız sayfaların, ziyaretçinin bilgisayarında kurulu Browser programı ne olursa olsun (Netscape Navigator, Opera, Amaya, Internet Explorer), mutlaka görüntülenecek olmasıdır. ASP sayfalarınıza koyacağınız VBScript kodları Server’da icra edileceği için, ziyaretçinin Browser’ının örneğin VBScript’i tanımayan Netscape olması, sizi hiç etkilemeyecek. Bununla birlikte ASP yoluyla üreteceğiniz sayfalarda yer alacak dinamik HTML kodlarının, her Browser’da mutlaka arzu ettiğiniz gibi yorumlanmayacağını unutmamalısınız.

PAGE

PAGE 1

---
*Kaynak: `BİR TEXT DOSYASI OLUŞTURMAK/BİR TEXT DOSYASI OLUŞTURMAK.doc` — ilhan Alphan — 2004*
