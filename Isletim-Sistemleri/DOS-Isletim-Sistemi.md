# DOS İşletim Sistemi

## **DOS İŞLETİM SİSTEMİ**

1980’li yıllarda IBM firmasının ilk kişisel bilgisayarları üretmesiyle birlikte kullanılmaya başlanan iletişim sistemidir.Günümüzde,Pckullanıcıları tarafından yaygın olarak kullanılmaktadır.

Çok kullanıcılı ortamlara uygun olamayan dos işletim sisteminin,bellek yönetimi ve grafik işlemlerde güçlü olmaması dezavantaçlarıdır.Bellekte az yer kaplaması,düşük donanıma sahip bilgisayarlarda kullanılabilmesi,diskte az yer kaplaması ise avantaçlarıdır.En önemli avantaçlarından biri de kolay öğrenilmesidir.

Dos işletim sistemi,” Disk Operating Systems”kelimelerinin kısaltılmış halidir.Bu sistem, bilgisayarın, yan üniteleri ile bağlantının düzenlenmesini, proğramların çalıştırılmasını ve veri giriş-çıkış işlemlerinin gerçekleştirilmesini sağlar.Bir başka ifade ile donanım arasındaki bağlantıyı sağlar.Yaygın kullanımı nedeniyle yeni işletim sistemlerinde de Dos işletim sistemine yer verilmiştir.

## İŞLETİM SİSTEMİNİN TEMEL KAVRAMLARI

Dos işletim sistemi,kendine bağlı birimleri belirli şekillerde ifade ederek tanımlar ve kullanır.

## 1.Sürücüleri Adlandırma

Dos işletim sisteminde, bilgisayarın üniteleri kendilerini temsil eden harf ve simgelerin önüne iki nokta üst üste”:” karakteri konularak gösterilir.Bilgisarayın yan ünitelerinin Dos tarafından ifade edilmesi aşağıda belirtilmiştir:

1.Disket Sürücü A:

2.Disket sürücü B:

Sabit Disk(Hard Disk) C:

Paralel Portlar LTP1:,LTP2:,LTP3,

Seri Portlar COM1:,COM2:,COM3:

Yazıcı PRN:

Seri Portlar AUX:

Boş Birim NULL

Ekran CON(Console)

***Örnek:***

Bilgisayarda, sabit disk, iki adet disket ve Cd-rom sürücüsü olduğunu farz edelim.Bu sürücüler, Dos tarafından aşağıda belirtildiği gibi adlandırılır.

1.disket sürücü A:

2.disket sürücü B:

Sabit Disk C:

Cd-Rom sürücü D: olarak ifade edilir.

2.Dizin Yolu İşareti(Komut göstergesi):

## Sistem İşareti

Bilgisayarlarda Dos işletim sistemi komutlarının yazılıp işlenebileceğini belirtmek amacıyla sürücü ismi ile birlikte gelen (>) işareti sergilenir.Bu işrete sistem işareti adı verilir.

***Örneğin:***

A sürücüsünde çalışıyorsa A>

B sürücüsünde çalışıyorsa B>

C sürücüsünde çalışıyorsa C > uyarıları ekrana görüntülenir.

## Dizin (Klasör)Yolu İşareti

Ters sılaç ( \\ )işareti, klasör yolunu göstermeyi sağlar.Bu işaret kullanılarak bilgisayarda çalışılmak istenilen klasör belirtilir.

***Örneğin:***

C:\\ C sürücüsünün ana klasörünü belirtir.

A:\\ A sürücüsünün ana klasörünü belirtir.

## 3.Dizin ve Alt Dizin(klasör- Directory)

Proğramların veya veri dosyalarının sembolik adların bulunduğu tabloya verilen isimdir.Klasörler iki ayrı şekilde ifade edilir.

## Ana Klasör(Root Directory)

Her disk ya da diskette mutlaka bulunur.Disk ya da disketler kullanılabilir hale getirildiğinde, bilgisayar tarafından otomatik olarak oluşturulur.Disk ya da disket üzerinde alt klasörler ve dosyalar, mutlaka bir ana klasöre bağlıdır. Ana klasör hiçbir zaman silinemez.Ana klasör, disk ya da disketlerin gövdesini oluşturur.

***Örneğin:***

A:\\ A sürücüsünde çalışıldığı ve A ana klasörde olunduğunu belirtir.

B:\\ B sürücüsünde çalışıldığı ve B ana klasörde olunduğunu belirtir.

C:\\ C sürücüsünde çalışıldığı ve C ana klasörde olunduğunu belirtir.

## Alt (Sub) Klasör

Kullanıcı tarafından oluşturulur.Alt klasör oluşturulurken kullanıcının istegine bağlı olarak isim verilir.İsim vermede dosya adında uygulanan kurallara dikkat edilir.Genellikle alt klasörlere uzantı verilmez.Disk ya da disketlerde bulunan alt klasörlerin isminin yanında <DIR> işrareti bulunur.Her alt klasör,ana klasöre bağlıdır.Alt klasör içerisinde başka alt klasörler veya dosyalar da bulunabilir.Alt klasörler,dosyaları gruplandırmak amacıyla kullanılır.

## Dosya (File-Kütük)

Bilgisayar ortamında,verilerin bir arada toplandığı ortama dosya adı verilir.Örneğin; bilgisayar yardımıyla yazılmış olan bir ödev, disk veya diskete saklanması halinde dosya özelliği kazanır.

## 4.Dosya İsimlendirme Kuralları

Bilgisayar ortamında bilgilerin saklanabilmesi için dosyalara isim verilir.Dosya ismi yazılırken aşagıdaki kurallara uyulur:

Dosya ismi en az 8 karakter uzunluğunda olabilir.

Dosya ismi içerisinde ( “ \* ; + = / ? < > \[ \] ) gibi özel karakterler bulunamaz.

Dos için özel anlam taşıyan aşağıdaki ifadeler, dosya ismi olarak verilemez.

COM1, COM2, COM3, LTP1, LTP2, LTP3, LST, NUL, PRN, AUX, CLOCK$ gibi.

Dosya ismi içerisinde, boşluk karakteri yer alamaz. Dosya isimleri A’dan Z’ye İngiliz harflerinden;(0-9)arasındaki rakamlardan ve nokta karakterlerinden oluşturulur.

***Örnekler:***

KDV (Doğru) VERGI MUH (Yanlış)

COM1 (Yanlış) VERGI MUH (Doğru)

## 5.Dosya Uzantısı ve Tipleri

Uzantı,dosyanın içerisindeki bilginin türünü belirlemek amacıyla 3 karakter uzunluğunda verilebilir.

Bazı dosys tipleri şu şekilde sıralanabilir:

BAS \[Basic program dosyası\]

COM \[Makine diline dönüşmüş program dosyası\]

EXE \[Makine diline dönüşmüş program dosyası\]

DAT \[Veri dosyası\]

DOC \[Doküman veya yazım dosyası\]

TXT \[Doküman veya yazım dosyası\]

COB \[Cobol kaynak program dosyası\]

BAT \[Toplu işlem dosyası\]

SYS \[Sistem dosyası\]

PAS \[Pascal program dosyası\]

WK1 \[Wortstar yazım dosyası\]

DOC \[WORD yazım dosyası\]

XLS \[EXCEL çalışma tablosu\]

## 6.Çalışabilir Dosyalar

Uzantısı COM,EXE, ve BAT olan dosyalar hemen çalışabilir dosyalardır.Öncelik sırası COM,EXE ve BAT şeklindedir.

## D. DOS İŞLETİM SİSTEMİNİN AÇILIŞ AŞAMALARI

Bilgisayarlarda BIOS adı verilen ve içerisinde test programları, ekran,yazıcı,sürücü,klavye kontrol yazılımları ile yine sistem üzerindeki entegre devrelerin programlanması gibi verilerin bulunduğu ROM bellek vardır. Bilgisayar açıldığında BIOS içerisinde yer alan ve kısaca POST(Power On Self Test) denen kısım yardımıyla sistemin fonksiyonlarını yerine getirip getirmediği kontrol edilir,varsa sabit (Hard) disk belirlenir.

## Sistem Disketten Açılıyorsa

A sürücüsüne bakılır, varsa bu disketin ilk sektörü belleğe yüklenir. Kontrol, bu sektörde bulunan ve Boot Record adı ile anılan küçük bir yükleyici programa geçer.

## Sistem Diskten Açılıyorsa

Eğer A sürücüsünde disket yoksa ve hard disk olduğu belirlenmiş ise; hard diskin ilk sektörü olan Master Boot (MBR) yüklenir ve kontrol,küçük bir yükleyici programa aktarılır.MBR diskin üzerinde oluşturulmuş olan bölümlerden (partition) hangisinin sistemi açacağına karar verir.Daha sonra bu bölüm üzerindeki boot sektörü okur.

---
*Kaynak: `DOS İŞLETİM SİSTEMİ/DOS ISLETIM SISTEMI.doc` — OKTAY — 2004*
