# PHP 2

[](http://www.e-dersane.com)

[](javascript:history.go(-1))

[](PHP-2-13.md)

[](PHP-2-10.md)

**
Windows 95/98 Altında POP3/SMTP Sunucu Kurulumu**

PHP ile tanıştıktan kısa bir süre sonra, hepimizin öğrendiği ilk konulardan biri, PHP ile e- posta gönderimidir. Sitemizdeki formlar aracılığıyla kullanıcılardan aldığımız bilgileri her zaman veritabanında saklama imkanımız olmayabilir, ya da form her doldurulup gönderildiğinde haberdar edilmek istiyor olabiliriz. Sonuç olarak, internetteki bir numaralı haberleşme aracı olan e-postayı, programlarımızda er ya da geç bir şekilde mutlaka kullanmak durumunda kalıyoruz.

Windows altında çalışan programcıların sorunları da bu aşamada başlıyor: Linux sistemlerin aksine, Windows 95/98 sistemlerde hazır bir POP3/SMTP sunucu programı yok. Bu yüzden, Windows 95/98 altında kurdugunuz PHP, sizden e-posta yollayabilmesi için ayrıca kurmanız gereken bir POP3/SMTP sunucusu talep eder. Bu talebi karşılayacak bir program kullanmadığınız sürece, internete baglı olmadığınız zamanlarda yazdığınız kodları deneme imkanınız olmaz. Internet'e saatlerce baglı kalmanın maliyetini de düşünecek olursanız, Windows 95/98 kullanıcıları için yapılacak en mantıklı iş, bu talebi internetle hiç uğraşmadan kendi bilgisayarınızda karşılamaktır.

Öncelikle bu iş için kullanacağımız programın adresini verelim, aşağıdaki linkten aslında komple bir internet sunucusu (POP3/SMTP disinda HTTP, FTP, IMAP ve NNTP protokollerini de destekliyor) olan Infradig programının ücretsiz Personal Edition sürümünü indirebilirsiniz:

[http://www.infradig.com/downloads/inframail.exe](http://www.infradig.com/downloads/inframail.exe)

Programın bir diğer özelliği de ayarları tarayıcınız üzerinden web tabanlı yapabiliyor olmanız.

Kuruluma geçmeden önce, POP3 ve SMTP sunucularının işleyiş mantığından bahsetmek istiyorum.

Internet üzerinde, e-posta alışverişi, SMTP sunucular üzerinden sağlanır. Bütün e-posta hizmeti veren yerlerin bir de SMTP adresi vardır: smtp.ixir.com gibi. SMTP sunucuların yerine göre üstlendikleri iki farklı rol vardır: Posta yollarken gönderen (sender), posta alırken alan (receiver). Örneğin siz Ixir'deki posta hesabınızdan Superonline'daki arkadaşınıza posta göndermek istediğinizde, postanız önce smtp.ixir.com a gider, buradan smtp.ixir.com -> mail.superonline.com ile bağlantı kurar ve postanızı mail.superonline.com a gönderir. İşin geri kalan bölümü, artık mail.superonline.com u ilgilendirir. Onun da görevi, aldığı postayı, postayı saklayacak olan programa (büyük çoğunlukla POP3 sunucu) iletmektir.

SMTP sunucular genellikle 25 numaralı porttan, POP3 sunucular da 110 numaralı porttan iletişim kurarlar. "Port" kavramına yabancıysanız gözünüzde şu şekilde canlandırabilirsiniz :

Bir sokaktaki binaların hepsinin kendine ait bir numarası var. Bunların kimisi boş, kimisi şahıslara ait, kimisi de devlet binası. 25 numaralı bina, bir devlet binası, önceden belirlenmiş şekilde posta gönderme hizmeti veriliyor. Siz mektubunuzu yazıp bu binaya gidiyorsunuz, mektubunuzu görevliye teslim edip çıkıyorsunuz. Postanızı 24 numaralı binadan yollayamazsınız, çünkü burası ya özel bir binadir, içeri alınmazsınız, ya da boştur, kapı kilitli olmasa ve içeri girebilseniz dahi, postanızı teslim edebileceğiniz bir görevli yoktur. Aynı şey 110 numaralı posta alma hizmeti verilen bina için de geçerlidir, postalarınızı sadece bu binadan ve size özel kutudan alabilirsiniz.

Programımızı kurup işler hale getirdikten sonra bu konuya tekrar döneceğiz.

**İnfradig Kurulumu**

Verdiğim adresten indirdiğiniz dosya, kendiliğinden çalıştırılabilir haldedir. Üzerine çift tıklayarak kurulumu başlatabilirsiniz. Bundan sonra yapacaklarınızı adım adım anlatacağım :

Dosyaya çift tıkladıktan sonra karşınıza sürüm bilgileri gelecektir, Tamam deyip geçebilirsiniz.

Kurulumu hangi klasöre yapmak istediğiniz sorulacak. Öntanımlı klasörü kullanmanızı tavsiye ederim, yine de kendi isteğinize göre değiştirebilirsiniz tabii. Diğer seçenekleri oldukları gibi bırakıp, Unzip seçeneğine tıklayın.

Kurulum ZIP ile işini bitirdikten sonra otomatik olarak SETUP programını çalıştıracaktır. Burada herhangi bir müdahalede bulunmanıza gerek yok, otomatik olarak gerekli dosyalar ayarlanacaktır.

Herşey sona erdiğinde karşınıza Notepad'de ufak bir not çıkacaktır. Aynı zamanda program otomatik olarak başlayacaktır.

Not defterini kapatalım. Şu anda sistem çubuğunda sarı-siyah baklava şeklindeki infradig ikonunu görüyor olmalısınız. Üzerine sağ tıklayın ve "Administration" seçeneğini seçin. Tarayıcınız otomatik olarak açılacak ve karşınıza yönetim ekranı gelecektir.

Çok güzel! Şimdi sıra yeni bir posta hesabı açmaya geldi. Adım adım ilerleyelim :

Üst bölümden "Accounts" linkine tıklayın. Burada karşınıza mevcut posta hesapları gelecek. Şimdilik sadece programın öntanımlı olarak yarattığı "root" kullanıcısı var. Bir tane de biz yaratalım.

Sağ taraftan "Create" butonunun üstüne tıklayın. Karşınıza hesap yaratma ekranı çıkacak. Burada girmeniz gereken bilgiler oldukça basit, isim, kullanıcı adı, şifre, ve tekrar şifre bilgilerini giriyorsunuz. Bir uyarı, burada gireceğiniz kullanıcı adını daha sonra kullanıcıadı@localhost biçiminde kullanacağız. Biz deneme olarak şöyle yazalım:
Name: Deneme
Userid: deneme
Password: 1234

"Create" butonuna bastıktan sonra, hesabımızın yaratıldığını ve "Enabled" yani aktif olduğunu görüyoruz. Şimdi üstteki seçeneklerden "Domains" linkine tıklayın.

Buradaki bilgileri:
Local domain: 127.0.0.1
Default domain: 127.0.0.1
Hosted domains: localhost
olacak şekilde değiştirin. Her satırı değiştirdikten sonra sağ tarafındakı Update butonuna basmanız gerekiyor, her seferde tek bir satırı değiştirebildiğinize dikkat edin.

Ayarlarımız tamam! Program ilk açıldığında kendiliğinden POP3/SMTP sunucu çalışır halde oluyor, bu ayarları programı daha sonra kendiniz kurcalayıp "Mail" bölümünden değiştirebilirsiniz, bizim istediğimiz zaten bir POP3/SMTP sunucu olduğu için bir sonraki aşamaya geçiyoruz.

**Telnet İle Ssunuculara Erişim**

Şimdi sıra yaptıklarımızın çalışıp çalışmadığını kontrol etmeye geldi. Daha sonra Outlook Express ile bir deneme yapacağız ama daha önce kullanımı oldukça kolay ve her Windows kullanıcısının bilgisayarında bulunan Telnet programı ile bir giriş yapalım :

Başlat -> Çalıştır seçeneklerini seçin.

Kutuya -> telnet localhost 110 yazip Enter tuşuna basın.

Telnet programı çalışacak ve karşınıza şuna benzer bir mesaj gelecek :

+OK POP3 Infradig-MAIL 181.965744246@localhost

Başka bir komut girmeden önce, Telnet'in menülerinden Uçbirim -> Tercihler seçeneklerine tıklayın ve burada "yerel yankı" seçeneğinin seçili olduğundan emin olun, aksi takdirde yazdıklarınızı göremezsiniz.

Şimdi aşağıdaki komutu yazın :

User deneme

Şu cevabı alacaksınız :

+OK enter password

Sonra aşağıdaki komutu yazın :

Pass 1234

Ve aldığınız cevap :

+OK logged in 'deneme'

Bütün herşey yolunda gittiyse, şu anda deneme kullanıcısı ile POP3 sunucusuna login oldunuz, mükemmel! Outlook, Messenger gibi programlar da, sizin bu yaptığınızdan farklı bir iş yapmıyorlar, bunu size çaktırmadan yapıyorlar o kadar! :)

Bundan sonra biraz POP3 komutlarıyla oynayabilirsiniz, örneğin STAT, size aşağıdaki çıktıyı verir :

+OK 0 0

İlk sıfır posta kutunuzda kaç mesaj oldugunu, ikincisi de bu mesajlarının boyutunun toplam kaç octet olduğunu gösterir.

Daha fazla kafa karıştırmayalım ve QUIT yazarak bağlantımızı keselim.

Bir sonraki aşama, Outlook Express'e bu posta hesabını nasıl tanıtacağımız.

**Outlook Express Ayarları**

Outlook ile yapmanız gereken ayarlar normal e-postanız için yaptığınız ayarlardan farklı değil. Adım adım anlatalım :

Araçlar-> Hesaplar menülerini seçin.

Sağ bölümde "Ekle" butonuna basın ve Posta seçenegini seçin.

Çıkan ekranda posta yollarken görünmesini istediğiniz ismi yazın ve İleri deyin.

E-posta adresi bölümüne "deneme@localhost" yazın.

Sonraki ekrandaki iki kutucuğa da localhost yazın.

Son ekranda da, kullanıcı adı : deneme, şifre: 1234 olacak şekilde belirtip hesabı yaratın.

Artık Outlook ile hesabımızı denetleyebileceğiz. Önce ufak bir test postası hazırlayıp Kime bölümüne "deneme@localhost" yazıp gönderin. Daha sonra posta hesabınızı kontrol edin. Kendinize attığınız postayı alabildiyseniz, bütün ayarlar tamam demektir!

Bu ayarlardan sonra geriye yapmanız gereken tek birşey kaldı, eğer daha önceden php3.ini veya php.ini dosyasında, SMTP değerinin karsılığını değiştirdiyseniz, tekrar php3.ini veya php.ini dosyasını düzenleyip SMTP'nin karşısına "localhost" yazmalısınız.

Bütün bu adımları uyguladıktan sonra, tamamen kendi başına çalışan bir POP3/SMTP sunucusuna kavuşmuş olacaksınız, bundan böyle her posta alıp gönderen programınızı test etmek için internet'e bağlı olmak zorunda değilsiniz, kendi bilgisayarınızda yerel olarak çok daha hızlı biçimde çalışabileceksiniz.

Son bir hatırlatma, programı kapattıktan sonra bir daha yeniden çalıştırmak istediğinizde ;

C:\\infradig-servers\\server\\ifmailtray.exe veya
C:\\programi\_kurdugunuz\_klasor\\server\\ifmailtray.exe

dosyasını çalıştırmanız yeterli.

Bu yazıyla ilgili phptr posta listesinden destek alabilirsiniz.

[](javascript:history.go(-1))

[](PHP-2-13.md)

[](PHP-2-10.md)

[ ](javascript:window.external.AddFavorite('http://www.e-dersane.com','E-DERSANE.com - Internetle Yasamayi Ogretir!'))

Copyright © 2001- **[www](http://www.e-dersane.com)**[.**E-Dersane.com**](http://www.e-dersane.com)** - Offline Dersler**. All Rights Reserved.
**[](http://www.e-dersane.com)****[](http://www.php.org.tr)****PhP Offline Dersleri **bolumunde yayinlanan bütün metin ve makaleler GPL lisansli olup ayrintili bilgi için [GNU.org](http://www.gnu.org) adresine bakiniz.

---
*Kaynak: `PHP 2/ekitap-Anonim-PHP_Offline/ders6.htm`*
*Görseller: `PHP-2/gorseller/` (1 dosya)*
