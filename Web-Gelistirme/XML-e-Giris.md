# XML ' e Giriş

XML'e Giriş**

**XML**(eXtensible Markup Language-Genişleyebilir Anlamlandırma Dili) hakkında birşeyler duymuşsunuzdur muhakkak; onun Web üzerinde veri alışveriş methodunu değiştireceğini, HTML’in bir nevi kardeşi olduğunu, ama tabi ki **SGML(Standard Generalized Markup Language)**’in bir alt kümesi olduğunu. XML üzerine uygulamalar geliştirmek onu kendi iş süreçlerinize dahil etmek istiyorsanız XML’i biraz daha geniş olarak inceleyen bu yazıyı okumanızı tavsiye ederim. **

İlk önce SGML’i incelemekte fayda görüyorum. Sonuçta bu bir giriş olduğuna göre temeli sağlam atmalıyız. SGML **International Standards Organization(ISO)** tarafından 1986 yılında kabul edilmiş ve onaylanmış bilgi-yönetimi standardıdır. SGML **platform-bağımsız** ve **uygulama-bağımsız** dökümanlar yaratmak sağlamak için oluşturulmuştur. Dilbilgisi gibi bir mekanizma kullanılarak dökümanların yapısını özel tanımlanmış tag’ler kullanarak yapısını tanımlamamıza yarar.

SGML bir **meta-dil**dir. Meta-dil demek dil yaratmaya yarayan dil demektir. (Yapay zeka’da metaknowledge’in knowledge about knowledge olduğu gibi.) Örneğin HTML, SGML’den türetilmiş bir anlamlandırma dilidir. Aynı şekilde XML’de temel olarak SGML’e dayanır. İlginç olan XML’in SGML gibi bir meta-dilden türemesine rağmen kendisi de bir meta-dil olmasıdır. Yani XML’den de yeni diller türetilebilir.

XML’i içeriğin nasıl görüneceğinden ziyade içeriğin yapısını tanımlamada kullanırız. Diğer taraftan HTML dökümanın nasıl gösterileceğini belirtir, dökümanın ne olduğundan hiç bahsetmez.

DTD**

Diğer önemli bir konu ise DTD’dir. HTML’de dikkat ettiyseniz ilk satır: **

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 FINAL //EN">

olarak görünür. Burada Web browser’a html’in hangi DTD’sini kullanacağı söylenir. **Burada DTD** Document Type Declaration’dır. Fakat kesinlikle bu XML’de ileride kullanacağımız **DTD yani Document Type Definiton ile ****karıştırılmamalıdır.** HTML’deki Document Type Declaration bize hangi tür bir dökümana sahip olduğumuzu söylerken , XML’de Document Type Definition ise dökümanın syntax’ının geçerli(valid) olduğu yerleri tanımlar. Aslında ileride DTD’yi geniş olarak ele alacağız ama kısaca açıklayacak olursak: DTD parser’ın izleyeceği kuralları belirler. Dökümanda ne gibi elemanların olduğunu ve bu elemanların neler yaptığını açıklar. Ayrıca DTD dökümanın tag yapısının ve içeriğindeki organizasyon hiyerarşisinin önceden tanımlanmış HTML kurallarına uyup uymadığını kontrol etmek için parser tarafından kullanılır. Şimdi aklınızdan geçenleri tahmin edebiliyorum, biraz karışık gibi görünüyor ama uygulama yapınca DTD’nin ne kadar kolay birşey olduğunu anlayacaksınız. Biraz daha sabır.

XML'in Gelişimi**

Internetin ilk yıllarında birkaç HTML tag’i kullanarak gri web sayfaları yapmak oldukça büyük bir işti. Ama zamanla insanlar bunun çok iyi bir reklam aracı olabileceğini farkedip, üzerinde çalışmaya başladılar. Birçok grafiksel öğe geldi, insanlar tasarım yapmaya başladılar. Bunu Html 2.0 ve 3.0 izledi. Gün geçtikçe internetin altyapısı da düzeldi. Türkiye’de inanılmaz bir ISS(Internet Servis Sağlayıcı) patlaması yaşandı. Paket fiyatları düştü düştü , firmalar bu rekabetten oldukça etkilendi ve geriye oldukça köklü firmalar kaldı. Internet 2. boyutunu yani insanlardan bilgi toplama yakalamıştı. Ve halen belki de bu boyuttayız. Asp bize sunucu taraflı uygulamalar geliştimeye olanak tanıdı hem de cgi, perl gibi dilleri bilmeden sadece Vbscript ile bunu yapmamızı sağladı. Artık web sayfaları dinamik içerik sağlıyordu, sizin kim olduğunuzu anlayıp size özel işlemler yapıyordu ki, veri transferinin önemi oldukça büyüdü. Artık herşey veriye bağlanmıştı. Bir web sitesinin arkasına SQL Server’lar, Oracle’lar SAP R/3 sistemleri durmaya başlamıştı. İşte XML bu veri değişimi işlemini kolaylaştırmak için doğdu. 3. kuşak internette de bu ve yeni teknolojiler kullanılarak insan faktörü ön plana çıkacak ve etkileşimli web siteleri yapılacak. B2B ve B2C’ler yerini Marketplace’lere bırakacak. Biz şu an 2. kuşağı yaşayan ama 3. kuşağa geçmeye hazırlanan bir ülkede bulunuyoruz. **

XML ile veri değişiminin kolay hale gelmesi hedeflenmişti ve başarıldı. Artık sizin verilerinizi alacak sistemin ne olduğunu bilmeniz ve ona göre çıktı üretmeniz gibi birşey söz konusu değil. Siz bir XML paketi oluşturup karşı sisteme yolluyorsunuz. O da bu paketi açaral kendi sistemine dahil ediyor. Yani artık internet aracılığıyla farklı sistemler veri değişiminde aynı dili konuşuyor: XML.

ASP ve XML İlişkisi**

Peki ASP bunun neresinde diyeceksiniz, hatta daha komik birşey bir iş arkadaşıma SAP Türkiye’de XML dersi verirken sorulan bir soru: "Asp mi Xml’i kapsıyor, Xml’mi Asp’yi?". İki teknoloji de birbirinden bağımsız görünse de birbirine bağlı teknolojiler. Ama kimse kimseyi kapsamıyor. Asp bir teknoloji Xml de. Xml üretmek için illaki Asp’ye ihtiyaç yok, tam tersi Asp için Xml’e de. Ama bu iki teknoloji ortak kullanıldığında veri değişiminde oldukça kolay ve başarılı uygulamalar geliştirilebilir. XML bize karşı sistemin ne olduğunu bilmemize gerek kalmadan paket oluşturmamıza yararken, ASP de bu paketleri kullanılabilir halde oluşturmamıza yaratıyor. **

XML başlığı altında işleyeceğimiz diğer bir konu ise XSL yani eXtensible Stylesheet Language. Kısaca XSL , XML dökümanlarının biçimini belirleme ve değiştirmede kullanılır. XSL kullanarak XML dökümanlarını daha başka XML dökümanlarına dönüştürebilirsiniz. Şimdilik XSL’i kafanızda CSS olarak canlandırabilirsiniz, sanki XML verilerine şekil kazandırıyormuş gibi ama ileriki konularda XSL’in çok daha kapsamlı olduğunu göreceğiz.

## XML'in Tasarım Amaçları** **

**XML tasarlanırken düşünülen birçok düşünce var. W3C’nin birleşip ortaya çıkardığı 10 temel XML’in tasarım amacı şunlar:**

**1- XML internet üzerinde çalışabilmelidir. ******

2- XML neredeyse tüm uygulamalar tarafından desteklenmelidir.

3- XML SGML ile uyumlu olmalıdır.

4- XML üreten programlar oldukça kolay olmalıdır.

5- XML’de opsiyonel özellikler minumum olmalı veya hiç olmamalıdır.

6- XML dökümanları okunabilir ve açık olmalıdır.

7- XML tasarımı tek bir firma bu işi ele almadan acilen hazırlanmalıdır.

8- XML tasarımı biçimlendirilmiş ve kısa olmalıdır.

9- XML dökümanlarının yaratılması çok kolay olmalıdır.

10- XML dökümanlarında anlam belirsizlikleri olmamalıdır.

Kendini Tamamlayıcı Dökümanlar**

XML dökümanları verilen tag isimleri ile kendini tanımlayabilir olmalıdır. Örneğin: **

<okuladi>ODTU</okuladi>

Burada açık olarak anlaşılıyor ki ODTU bir okulun adıdır. Aslında işin temeline inmemizde ben yine yarar görüyorum. En başta dedim ya temel sağlam olmalı. XML dökümanları 2 kritere uymalıdır; **iyi-oluşturulmuş(well-formed)** ve** geçerli(valid)**.

**İyi-oluşturulmuş Döküman**:
Bir XML dökümanının iyi-oluşturulmuş olması için aşağıdaki temel kurallara uyması gereklidir:

1- HTML ve SGML gibi XML de büyüktür (>) ve küçüktür (<) karakterlerini ayrıraçlar olarak kullanır.
2- Bu karakterlerle tag dediğimiz yapılar oluşturulur ve bunlar açıldığı zaman kapatılmalıdır. Tek istisna boş elemandır(değeri olmayan eleman). Bu durumlarda açma ve kapama tag’i aynı olabilir. Örneğin: <okuladi/> dediğimizde okuladi diye bir tag açmış oluruz ama içinde herhangi bir değer bulunmaz.
3- Tag’lerin eklentileri çift-tırnak içine alınmalıdır. HTML bu açıdan esnektir fakat XML bunu yapmanıza izin vermez. Örneğin HTML’de <font size=3> diye bilirsiniz ama XML’de 3 kesinlikle çift-tırnaklar içine alınmalıdır.<font size=”3”>
4- Elemanlar aynı HTML’de olduğu gibi iç-içe düzgün bir şekilde tanımlanmalıdır. Her XML dökümanı bir kök elemanına sahiptir ve diğer tüm elemanlar onun çocukları olarak anılırlar. Hemen bir örnek verelim:

<universite>
<universiteadi>ODTU</universiteadi>
<universitesehiri>Ankara</universitesehiri>
</universite>

5- XML’deki elemanlar büyük-küçük harf ayırt eder. Yani <universite> ile <UNIVERSITE> iki ayri elemandır. Bu yönüyle de HTML’den farklıdır. Bu yüzden XML kodları yazarken ençok karşılaşılacak sorun bu olabilir.

**Geçerli Döküman: **
Geçerli bir döküman kendi DTDsi veya şemasında(**shema**) tanımlanmış kurallara uyan dökümandır. Aslında daha ikisini de incelemedik ama kısa bir bilgi vereyim: DTDler ve şemalar o XML dökümanının her elemanının neler kapsayabileceğini ve o dökümanın organizasyonel yapısını belirler. SQL Server veya Oracle ile uğraşmış olanlar bilirler , buradaki şema yapısı da veritabanı şeması belirleme ile aynıdır. En büyük fark ise XML’de elemanların eleman içermesidir. Bu konuya ileride oldukça geniş yer vereceğim çünkü oldukça önemli.

## XML Geliştirme Programları** **

Tabiki yine **Notepad**. Microsoftun en sorunsuz çalışan ürünü olsa gerek. Eğer ben iyi kod yazarım hata yapmam diyorsanız Notepad’i tavsiye ederim. Ama tabiki XML için de yazılımlar gün geçtikçe artıyor.

En çok kullanılanlardan biri Microsoftun **XML notepad**’i.(Notepad’e olan talebi görmüş olmalı ki.) Oldukça güzel bir arayüzü var. XML’de amaçlandığı gibi çok basit bir şekilde XML dökümanı yaratmanızı sağlıyor. Ayrıca ücretsiz.
**Download etmek için ****tıklayın...**

İlk Örnek**

Ve işte ilk örneğimiz: **

** ****<< Bakın burada yapılmışı var******

**
<?xml version="1.0"?>
<OGRENCI>
<ISIM>
<AD>SERAP</AD>
<SOYAD>BASARAN</SOYAD>
</ISIM>
<UNIVERSITE>
<BOLUM>GIDA MUH</BOLUM>
<YIL>1996</YIL>
</UNIVERSITE>
<ADRES>
<CADDE>YURTLAR CADDESI</CADDE>
<APARTMAN>UC APARTMANI</APARTMAN>
<NO>610</NO>
<ILCE>BABAESKI</ILCE>
<IL>KIRKLARELI</IL>
</ADRES>
</OGRENCI>**

Farzedelim ki bir vakıf kurduk ve bu bilgileri tutmak istiyoruz. Okulundan bir XML dökümanı istiyoruz ama yapısının bu şekilde olmasını istiyoruz. Onlar bize bu yapıda bir döküman yolluyorlar biz de bunu otomatik olarak çalışan sistemimize kaydediyoruz diyelim. Böylece okuldan biri mezun olduğunda mezunlar derneğimize katılması için mektup yollayableceğimiz bir adresi var. Sistem otomatik olarak güncelleniyor. Sizin büronuz Istanbul’da okul Ankara’da. Aslında çok basit bir örnek ama bu uygulamaları düşünmenin hayal sınırı yok. Veriyi oluşturmak için sisteminizi çalıştırmanız yeterli, diğer tarafta nasıl sisteme entegre olacağı sizi ilgilendirmiyor.

Web üzerinde kullanacağımız XML uygulamalarında XML dökümanını derleyen msxml.dll dosyasıdır. Eğer Internet Explorer 5.0 ve üzerini kullanıyorsanız XML dökümanlarını rahatça görüntüleyebilirsiniz.

Eğer yukarıdaki kodu düzgün kodladıysanız xml dosyasını kişisel sunucunuzda çalıştırdığınız da aşağıdaki görüntüyü elde edersiniz:

+ ve – ‘lere tıklayarak tag’leri açıp kapayabilirsiniz. Bu yapı size XML dökümanlarının eleman-çocuk ilişkisini anlamınıza yarayacaktır.

XML Hata Mesajları**

Eğer bir hata yaptıysanız ki neredeyse her zaman ilk yazılışta hata çıkar, Internet Explorer hata verecektir. Şimdi olası hataları değerlendirelim: **

1- Eğer üstteki hatayı görüyorsanız sizde anlayacaksınızdır ki, <IL> tagini kapatmayı unutmuşsunuzdur. XML dökümanı iyi-oluşturulmalıdır demiştik ya işte orada bundan söz etmiştik.

2- Eğer üstteki hatayı alıyorsanız çift-tırnak koymadığınızı anlayacaksınızdır. Bu da bir iyi-oluşturamama hatasıdır.

3- Eğer üstteki hatayı alıyorsanız, Büyük-küçük harfe dikkat etmemiş olduğunuzu göreceksiniz.

4- Eğer üstteki hatayı alıyorsanız, aynı tag’i birden fazla kullanmışsınızdır.

---
*Kaynak: `XML ' e GİRİŞ/XML 'e GİRİŞ.doc` — MEM — 2004*
