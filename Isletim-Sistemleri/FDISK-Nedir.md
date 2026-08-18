# FDISK Nedir

## **FDISK Nedir?**

Bu ödevde ağırlıklı olarak, Windows 95, Windows OSR2 ve DOS için geliştirlimiş FDISK programının kullanımından bahsedeceğim. Bu program DOS/Windows 95 işletim sistemleri için, bir diski ilk kullanıma hazırlamak için kullanılır. FDISK’i dikkatli kullanmak gerekir. Yoksa bize pahalıya mal olabilir.

## **FDISK’in Tarihcesi**

Microsoft, ilk FDISK programını yazdığı zaman, 33 megabaytlık disk bölümlerini (partition) destekliyordu. Daha sonra 40 megabaytlık sabit diskler çıkmaya başladı. Microsoft’ da DOS 4.0 versiyonunu piyasaya sürdü. Artık yeni FDISK 2 gigabaytlık harddiskleri destekliyordu. Microsoft daha sonra Windows 95’ i piyasaya sürdü. Fakat Windows 95 ile beraber gelen FDISK 2 gigabaytın üzerini göremiyordu. Hal böyle olunca Microsoft Windows 95 OSR2 versiyonunu piyasaya sürdü. Windows OSR2 daha akıllı ve FAT32 desteği ile 2 terabayt disk alanlarını destekliyordu.

FDISK deyip Enter tuşuna basarsak karşımıza şöyle bir mesaj gelir :

Bilgisayarınızın 512 MB’den daha büyük bir diski var. Windows’un bu sürümü büyük diskler için geliştirilmiş destek içermektedir, böylelikle büyük sürücülerde diskin etkin kullanımını ve 2 GB’den büyük disklerin tek bir sürücü olarak biçimlendirilebilmesini sağlar.

ÖNEMLİ: Büyük disk desteğini etkinleştirir ve bu diskte herhangi yeni sürücü yaratırsanız, çalışan diğer sistemleri, Windows 95 ve Windows NT sürümlerini ve Windows ile MS-DOS ‘un önceki sürümleri gibi, kullanarak yeni sürücüye erişemezsiniz. Bunun yanı sıra, özel olarak FAT32 dosya sistemi için tasarlanmamış disk hizmet programları, bu diskle çalışamayacaktır.

Bu diske, diğer işletme sistemleriyle ya da daha eski disk hizmet programlarıyla erişmeniz gerekirse, büyük sürücü desteğini etkinleştirmeyin.

Büyük disk desteğini etkinleştirmek ister misiniz(E/H)..............?\[H\]

Burada “H” deyip enter’ a basarız. Şöyle bir menü gelir:

| **Microsoft Windows 95** **Sabit Disk Kurma Programı** **(C) Telif Hakkı Microsoft Corp. 1983 – 1995** **FDISK Seçenekleri** ** **Geçerli Sabit Disk Sürücüsü : 1 Aşağıdakilerden birini seçin: DOS bölümü veya Mantıksal Dos Sürücüsü yarat Etkin bölümü ata Bölüm veya Mantıksal DOS Sürücüsü sil Bölüm bilgisini göster Seçeneği girin : \[1\] FDISK’ ten çıkmak için Esc tuşuna basın |
| --- |

Burada 1. Seçeneği birinci ve uzatılmış DOS sürücüsü yaratmamızı sağlar. 2. Seçeneği yarattığımız 1.DOS bölümü veya uzatılmış DOS bölümünü etkin yapmamıza yani İşletim Sistemimizi hangi sürücüde bulunacağını belirlemek için kullanılır. 3. Seçeneği yarattığımız birinci DOS bölümü veya uzatılmış DOS bölümünü silmemize yarar. 4. Seçeneği ise yarattığımız bölümlemeleri gösterir. Şimdi sırayla bu seçenekleri açıklayalım.

## **1.DOS Bölümü veya Mantıksal DOS Sürücüsü Yarat**

Bu bölümde sabit sürücüyü bölümlere ayrıma, birinci DOS bölümü, mantıksal DOS sürücüsü, uzatılmış DOS bölümü yaratmak için kullanılır. Ana menüden “1” deyip Enter tuşuna basarsak karşımıza şöyle bir menü gelir:

| **DOS Bölümü veya Mantıksal DOS Sürücüsü Yarat** ** **Geçerli Sabit disk sürücüsü : 1 Aşağıdakilerden birini seçin: Birinci DOS bölümü oluştur Uzatılmış DOS Bölümü oluştur Uzatılmış DOS bölümü üzerinde Mantıksal DOS sürücüsü oluştur. Seçeneği Girin : \[1\] FDISK Seçeneklerine dönmek için ESC Tuşuna basınız. |
| --- |

Şimdi bu menüdeki seçeklerini tek tek kullanalım.

## **Birinci DOS Bölümü Yarat**

Burada 610 yazılıp Enter dersek şöyle bir açıklama menüsü gelir.

Burada ESC’ ye basarsak FDISK seçenekleri menüsü gelir. Bu menünün altında şöyle bir uyarı bulunur.

Bu uyarıyı şimdilik dikkate almıyoruz.

Şimdi sırada geride kalan Mbyt’ ı değerlendirmeye geldi. Bunu “Uzatılmış DOS bölümü yarat” seçeneği ile yapıyoruz. “DOS Bölümü veya Mantıksal Sürücü Yarat” menüsünden “2” yi “Uzatılmış DOS Bölümü Yarat” seçip enter’ a basarsak şöyle bir menü ile karşılarız.

## **DOS Bölümü Yarat**

Burada 608 birinci DOS bölümünden sonra kalan alanıdır. Bunu değiştirmezsek bir tane uzatılmış DOS bölümü yaratabiliriz. Eğer küçültürsek bir kaç tane yaratabiliriz. Biz sadece bir tane uzatılmış bölüm yaratacağımızdan 608 yazar Enter deriz. Karşımıza şöyle bir menü gelir.

ESC’ ye bastığımızda şöyle bir menü gelir.

## **Uzatılmış DOS Bölümü İçinde Mantıksal DOS Srücüsü yarat**

ESC’ ye basınca karşımıza şöyle bir açıklama menüsü gelir.

Buraya eğer mantıksal sürücü yaratmak istersek oraya 608 girersek bir mantıksal sürücü, daha küçük girersek birden fazla mantıksal sürücü yaratır. Eğer 608 dersek bilisayarımızı “D” sürüsünden açamıyoruz. Bu sürücüyü sadece bilgi depolamakta kullanabiliyoruz.

Ben 608 dedim mantıksal sürücüyü oluşturdum. Sonra ESC deyip FDISK seçeneklerine geldim.

## **Etkin Bölüm Ata**

Burada bir etkin bölüm atamamız gerekir. 2 seçeneğini “Etkin bölüm ata” seçip Enter’ a bastım. Karşıma şöyle bir menü geldi.

Burada “1” deyip Enter’ a basarsak “C” yi etkin yaparız. Eğer “2” deyip Enter tuşuna basarsak bilgisayar hata mesaji verir. Çünkü mantıksal sürücüyü etkin yapamayız.

Şimdi “3” seçeneğini seçtim “Bölüm veya Mantıksal DOS Sürücüsü” seçtim.

## **Bölüm Bilgisini Göster**

FDISK seçenekleri ana menüsüne gelip “4” seçeneği yani “Bölüm Bilgisi Göster” dedim. Şöyle bir açıklama menüsü ile karşılaştım.

Daha sonra deneme amacıyla oluşturduğum bölümleri silmek için FDISK seçenekleri ana menüsüne geldim ve “3” seçeneğini yani “Bölüm veya Mantıksal DOS Sürücüsü Sil” seçeneğini seçtim.

## **Bölüm veya Mantıksal DOS Sürücüsü Sil**

Bu seçenek yarattığımız bölüm veya mantıksal DOS sürücülerini silmeye yarar. FDISK ana menüsünde “3” deyip Enter’ a basarsak karşımıza şöyle bir menü gelir.

Burada ilk önce eğer mantıksal sürücü yaratıysak “3” seçeneğini kullanarak Mantıksal Sürücüyü silmemiz gerekir. Ben mantıksal sürücü oluşturduğum için ilk önce bu menüyü kullanacağım.

## **Uzatılmış DOS Bölümü İçindeki Mantıksal DOS Sürücüsünü Sil**

Mantıksal sürücüyü oluşturduğum zaman “Birim adını” **Remote**\* olarak verdi. Sonra o mantıksal sürücüyü silmek istedim. Birim adını Girin seçeneğine ne girersem gireyim “Birim adı Uyuşmuyor” diye bir hata mesajı verdi. DOS’ a çıkıp “D” sürücüsüne format atamak istedim. Format atmak istememde ki amaç birim adını değiştirmekti. Format atarkende bir sorun verdi. Hata mesajı olarak “Bir ağ sürücüsü biçimlendirilemez” yazdı. Bende bilgisayarı kapattım. Sonra BIOS Setup ayarlarından harddiske “HDD Low Level Format” attım. Sonra bilgisayarı sistem disketiyle tekrar açıp “D” sürücüsüne format atıp birim adını değiştirdim. FDISK’ e girip uzatılmış bölüm içindeki mantıksal sürücüyü sildim. FDISK seçenekleri ana menüsünden çıkıp “Bölüm bilgisini göster” dedim ama hala “D” yi görüyordu. Bu problemi gidermek için “Uzatılmış DOS Bölümünü” silmem gerekiyordu.

## **3.2. Uzatılmış DOS Bölümünü Sil**

DOS Bölümünü veya Mantıksal DOS Sürücüsünü Sil menüsünden “2” yi yani “Uzatılmış DOS Bölümünü Sil” seçeneğini seçip Enter’ a bastım. Karşıma şöyle bir ekran geldi.

Burada “E” dedim ve Enter’ a bastım. Şöyle bir mesaj geldi.

## **Birinci DOS Bölümünü Sil**

Sıra “Birinci DOS bölümünü” silmeye geldi. “1” yani “Birinci DOS Bölümünü Sil” deyip Enter’ a bastığımda şöyle bir menü ile karşılaştım.

Buraya genelde “1” yazarız. Eğer birden fazla harddiskimiz varsa başka rakam girebiliriz. “1” deyip Enter dersek şöyle bir mesaj ile karşılaşırız.

Böylece Birinci DOS bölümünüde silmiş olduk. Yani harddiskimiz şu anda kullanılamaz.

Daha sonra FDISK seçenekleri ana menüsünden “1” yani “DOS Bölümü veya Mantıksal DOS Sürücüsü Yarat” seçeneğini oradan da tekrar “1” ‘i yani “Birinici DOS Bölümü Yarat” seçeneğini seçtim ve harddiskimin tümünü yani “1219” Megabayt’ ı tek bir bir bölüm halinde oluşturdum. Daha sonra FDISK seçenekleri ana menüsünden “2” yani “Etkin Bölüm Ata” seçeneğini seçtim ve oluşturduğum Birinci DOS bölümünü etkin yaptım.

## **FDISK Sonrası Yapılanlar**

Daha sonra DOS’ a çıkıp bilgisayarımı reset ettim ve sistem disketinden bilgisayarı açtım. “C” sürücüsüne format atttım. Ve İşletim sistemini kurdum.

PAGE

PAGE 1

---
*Kaynak: `FDISK NEDIR/FDİSK NEDİR.doc` — ogr — 2004*
