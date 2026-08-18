# Personel Web Server

## **Personal Web Server**

Microsoft'un yeni teknolojisi olan Active Server Pages (ASP) teknigini kullanan dosyalari hazirlayip, çalistirabilmek için koca koca serverlara, ates pahasi yazilim ve isletim sistemlerine ihtiyaciniz yok. Windows 95/98 için gelistirilen ve Windows 95/98 CD-ROM'u içinde yer alan PWS, bu teknolojiyi masaüstü bilgisayarlarimiza tasiyor. PWS, Web sayfalarimizi kontrol etmek ve gelistirmek için kullanabilecegimiz bir masaüstü server (sunucu) yazilimidir.

Windows ortaminda Kisisel Web Sunucusu (Personal Web Server) CGI, Perl ve ASP dosyalarimizi Internet’e yerlestirmeden once sinayabilecegimiz mükemmel bir araçtir. Burada PWS’in kurulumunu ve hazirladigimiz ASP dosyalarini çalistirabilmek için gerekli bilgi ve ipuçlarini ele alacagiz.

Windows 98 Cd'si ile gelen PWS yazilimi neler içeriyor?

PWS bilgisayarinizda kurulu mu?

PWS'in kurulmasi

Kurulumda hata mesaji çikarsa

PWS hizmete hazir

Personal Web Manager'i taniyalim

Sanal dizin nedir?

Personal Web Server'imizi küçük bir ASP dosyasi ile sinayalim

Web Paylasimi

PWS'in kök dizinini degistirelim

## **Windows 98 Cd'si ile gelen PWS yazilimi neler içeriyor?**

Microsoft Personal Web Server 4.0

Microsoft Transaction Server 2.0

Data Access Components 1.5

Microsoft Message Queue (MSMQ) Server 1.0

Personal Web Manager

## **PWS bilgisayarinizda kurulu mu?**

Windows 98 bilgisayarinizda varsayilan (default) ayarlari ile kurulmussa PWS kurulu degil demektir. Yine de PWS'in kurulu olup olmadigini kontrol edebilirsiniz. PWS sisteminize yüklenmisse sistem tepsisinde (system tray) su üç simgeden birini göreceksiniz:

Ayni sekilde PWS'in sisteminizde kurulu olup olmadigini Baslat\*Ayarlar\*Denetim Masasi\*Program Ekle/Kaldir\*Windows Kur\*Internet Araçlari yolunu izleyerek Kisisel Web Sunucusu satirindan da kontrol edebilirsiniz

## **PWS'in kurulmasi******

PWS kurmak için Windows 98 CD-ROM'u gereklidir. Bu CD-ROM'u CD sürücüsüne yerlestirdikten sonra; CD-ROM'deki Add-ons klasörünün altinda bulunan **kur.exe** dosyasini çalistirin.

PWS "Normal" kurulumda yaklasik 26 mb disk alani gerektirmektedir. "Özel" kurulumu seçerek farkli bilesenler yükleyebilirsiniz. Veri-yönlendirmeli web uygulamalari üzerinde çalismak istiyorsaniz, "Microsoft Data Access Components" altinda bulunan "ActiveX Data Objects" bilesenini yükleyin.

Bir sonraki adimda "WWW Hizmeti" satirinda PWS'nin kök dizin olarak kullanacagi klasör görüntülenmektedir. Varsayilan (default) ayarlar ile bu klasör c:\\Inetpub\\wwwroot klasörüdür. "Gözat"i tiklayarak diskinizdeki istediginiz bir klasörü de kök dizin olarak seçebilirsiniz.

Daha sonraki adimda ise Transaction Server dosyalarinin kurulacagi dizin gösterilmektedir. Varsayilan ayarlar ile bu klasör "c:\\Program Files\\Mts" klasörüdür.

Kurulum bittikten sonra sistem tepsisinde PWS simgesi yerlesecek ve bilgisayari yeniden baslatmaniz istenecektir.

## **Kurulumda hata mesaji çikarsa**

Kurulum sirasinda Transaction Server sistem girdileri yapilirken bir hata mesaji alabilirsiniz.

Böyle bir durumla karsilasirsaniz kurulumdan çikarak, PWS'yi sisteminizden kaldirin (Denetim Masasi\*Program Ekle/Kaldir). CD-ROM'da bulunan add-ons\\PWS klasörünü diskinize kopyalayin ve <http://support.microsoft.com/support/kb/articles/q246/0/81.asp> adresinden mtssetup.exe dosyasini download edip çalistirin. Dosyalarin açilacagi yer olarak cd'den diskinize kopyaladiginiz PWS klasörünü gösterin. mtssetup.dll </download/download.asp?kategori=PWS&dosya=Mtssetup.exe> dosyasi üzerine yazilip yazilmayacagini soran ekranda "Yes"i tiklayin. Böylece hataya yol açan eski dosyanin yerine güncel dosya kopyalanacaktir.

Bu islemlerden sonra diske kopyaladiginiz klasörde bulunan kur.exe dosyasini çalistirin. Bu sefer PWS sisteminize hatasiz bir sekilde kurulacaktir.

## **PWS hizmete hazir**

Kurulum bitip bilgisayariniz tekrar açildiginda PWS artik hizmete hazirdir. Personal Web Manager'i çalistirmadan önce bilgisayariniza bir isim verebilirsiniz. Bunun için Denetim Masasi'ndaki Ag simgesini çift tiklayin ve açilan pencerede Tanimlama sekmesinde Bilgisayar Adi kismina dilediginiz bir isim verin.

Degisikliklerin geçerli olmasi için windows kapanip açildiginda artik Personal Web Manager'i çalistirabilirsiniz. Bunun için system tray'de bulunan ikonu veya masaüstündeki "Yayimla" kisayolunu çift tiklayin. Personal Web Manager, PWS'in site yönetim aracidir ve kullanimi kolay bir arayüzü vardir.

## **Personal Web Manager'i taniyalim**

Personal Web Manager'i çalistirdigimizda son derece sade bir arayüz ile karsilasiyoruz. "Ana" penceresinde iki kisim görülüyor. Üstte sunum hizmetini baslatip durdurmak için bir dügme vardir. (Ayrica sistem tepsisindeki PWS simgesini sag tiklayip Hizmeti Beklet seçenegini kullanarak PWS'i bekleme konumuna getirebilirsiniz). PWS Manager’da iki adres göreceksiniz: Baslat/Dur dügmesinin üstünde kisisel Web sunucusunun "sanal adresi," altinda ise bu adresin sabit diskinizdeki gerçek dizin adresi yer aliyor. Bilgisayariniza verdiginiz adin burada "sanal adres" sekilde göründügüne dikkat edin. PWS’in sanal adresini browser'da, URL adres kutusuna **http://<bilgisayar\_adi>** olarak yazacagiz; bu "adreste" yer almasini istedigimiz dosyalari ise burada gördügünüz gerçek dizine koyacagiz. PWS Manager’in alt kisimda ise ziyaretçi istatistiklerini görebilirsiniz. "Yayimla" ve "Web Bölgesi"nde bulunan iki adet sihirbaza ve "Gezinti" paneline hizlica bir göz attiktan sonra (bu sihirbazlari kisisel ana sayfa hazirlamak ve dosyalarinizi intranette paylasmak için kullanabilirsiniz) bizim için asil önemli olan "Gelismis" kismina gelelim.

Burada "Home" dizini altinda birtakim klasörler göreceksiniz. Isterseniz buraya sanal dizinler (virtual directory) ekleyebilir PWS'in diskinizin degisik klasörlerinde bulunan ASP dosyalarini çalistirmasini saglayabilirsiniz.

## **Sanal dizin nedir?**

Sanal dizin, fiziki olarak PWS klasörü altinda bulunmamasina ragmen bu klasöre sanal olarak ekleyebileceginiz klasörlerdir. Örnek olarak masaüstünde bulunan PWS klasörünü PWS’e sanal dizin olarak ekleyelim. Bunun için "Gelismis" panelinde bulunan "Ekle" dügmesini tikliyoruz (sanal dizini bir baska sanal dizin altina altdizin olarak eklememek için Home klasörünün seçili olmasina dikkat edin); ve açilan pencereden klasörün yerini gösteriyoruz. "Diger ad" (alias) kismina bir isim veriyoruz, örnegin pws. Daha sonra, Erisim kutusundaki Yürütme seçenegini isaretleyip Tamam dügmesini tikliyoruz.

Artik bu klasördeki dosyalari çalistirabiliriz. Sanal klasörleri Personal Web Manager'a ekledikten sonra browser'da görüntülemek için adres satirina URL'i su sekilde yaziyoruz:

**http://<bilgisayar\_adi>/<sanal\_dizin\_adi>**

Bizim örnegimize göre adres su sekilde olacak:

**http://kara-murat/pws**

## **Personal Web Server'imizi küçük bir ASP dosyasi ile sinayalim******

Simdi ASP çalismalarimiz için bir klasör olusturup bunu Personal Web Manager'a sanal dizin olarak ekleyecegiz ve küçük bir ASP dosyasi olusturup PWS'i sinayacagiz. Önce yeni bir klasör olusturalim. Bu, örnegin c:\\Belgelerim altina ASP\_deneme klasörü olsun

Sonra yukarida anlattigimiz sekilde bu klasörü sanal dizin olarak gösterelim ve denemek için bir minik ASP dosya olusturalim. Kodlar su sekilde;

<html>

<head>

<title>Deneme ASP Sayfasi</title>

</head>

<body>

<h3>Personal Web Server'a Hosgeldiniz</h3>

Su anda saat: <% =time() %>

</body>

</html>

Bu dosyayi ASP\_deneme klasörü içerisine default.asp ismi ile kaydedelim. Personal Web Manager'da olusturdugumuz sanal dizini bulup üzerine sag tiklayip Gözat'i seçtigimizde browser açilacak ve ASP dosyamiz görüntülenecektir. Browser'in Refresh/Reload/Yenile tusu ile sayfayi her yüklediginizde saatin degistigini görebilirsiniz. Eger Yenile simgesini her tikladiginizda saat degisiyorsa, PWS çalisiyor, demektir. TEBRIKLER

Dosyaya **default.asp** ismini vermemizin nedeni PWS'in varsayilan olarak bu dosyayi görüntülemek istemesinden kaynaklaniyor. Böyle bir dosya bulunamadigi taktirde browser meshur 404 kod numarali sayfa bulunamadi hatasi verecektir. Bu durumu degistirmek için Personal Web Manager'da "Gelismis" panelinde bulunan ayarlari kullanabiliriz. "Varsayilan Belgeler" satirina varsayilan ana sayfa olarak kullanmak istediginiz dosya isimlerini yazin. PWS çalistirildiginda sirayla dosyalari kontrol edecek ve buldugu dosyayi çalistiracaktir.

Eger klasörde bu dosyalardan hiçbiri bulunmuyorsa ve hata mesaji ile karsilasmak istemiyorsaniz bir alt satirda bulunan "Dizinde Gözatmaya Izin Ver" seçenegini isaretleyin. Böylece örnegin yalnizca grafik dosyalarinizin bulundugu bir klasörü de PWS ile açabilir, dosyalari görebilirsiniz.

## **Web Paylasimi**

PWS'in getirdigi bir baska yenilik de klasör özelliklerine ekledigi Web Paylasimi seçenegidir. Klasörleri sag tiklayip Özellikler'den Web Paylasimi sekmesine girdigimizde klasörün PWS’e sanal dizin olarak eklenip eklenmedigini kontrol edebilir, eklenmisse özelliklerini degistirebilir, paylasimi kaldirabiliriz.

## **PWS'in kök dizinini degistirelim**

Isterseniz PWS'in default olarak kullandigi C:\\Inetpub\\wwwroot kök dizini degistirebilirsiniz. Bunun için Personal Web Manager'da "Gelismis" panelinde sanal dizinler penceresindeki "Home" dizinini seçip Özellikleri Düzenle dügmesini tiklayin ve kök dizin yapmak istediginiz klasörü gösterin. Hepsi bu kadar.

Simdi sizi PWS ve ASP dosyalari ile basbasa birakiyoruz. Kolay gelsin...

**NOT: Burada kullanilan ekran görüntüleri Internet Exporer'a aittir. Fakat varsayilan browser'iniz Netscape Navigator ise PWS NN ile de sorunsuz olarak çalisabilmektedir. ASP sayfalarinizi her iki browser'da da görüntüleyebilmek için adres satirlarina gerekli adresi yazmaniz yeterli olacaktir. ******

---
*Kaynak: `PERSONEL WEB SERVER/PERSONEL WEB SERVER.doc` — serkan — 2004*
