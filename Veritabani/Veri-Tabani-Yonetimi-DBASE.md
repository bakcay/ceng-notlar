# Veri Tabani Yonetimi - DBASE

**VERİ TABANI YÖNETİMİ-DBASE******

***1-VERİ TABANI *********

**VERİ TABANI :** Belirli bir tarzda organize edilmiş bilgiler koleksiyonudur.

**VERİ TİPLERİ :**

**1-) Karaktersel (Alfasayısal)Veriler**

ASCII karakterlerini kapsar. 1 ile 254 arası sayıda karakterden oluşabilir.
(Bursa, Okul0115a ,#, s, “123”)

**2-) Sayısal (Numeric) Veriler**

Sayısal değerler, dört işlem yapabildiğimiz değerlerdir. Ondalık veya tamsayı olabilir.
(123, 845)

**3-) Tarih Tipi Veriler**

Tarih gösteren verilerdir.Otomatik olarak 8 karakter uzunluğundadır. Normalde gg/aa/yy
formatındadır. SET KONTROL komutları kullanılarak gg/aa/yy formatına dönüşüm yapılabilir.
(05/28/95)

gg aa yy
g- gün a-ay y-yıl

**4-) Memo Tipi Veriler**

Bu türden olan veriler herhangi bir metni yani text’ i içeren verilerdir. Bu tip verilere ait
sahalar diğer sahalardan farklı şekilde işlenir. Çalışılan dosya çağrıldığında bu sahaya
ilişkin bilgiler görünmez, özel olarak o sahaya girilerek içeriği görülebilir. Kısa not şeklinde
bir veri tipi olarak tanımlayabiliriz.

**5-) Logical (Mantıksal) Tip Veriler**

Mantıksal bir sahanın içeriği yalnızca doğru veya yanlış olabilir. Başka alternatif yoktur.
(Doğru veya Yanlış) (True veya False) ( Yes veya No)

**VERİ TABANI KÜTÜĞÜNÜN ANA PARÇALARI:**

**a-) Veri Alanları**

Bir veri alanı, veri tabanı kütüğünün içinde hep aynı tipte veri tutan depolama birimidir.

Örneğin öğrencilere ait sicil bilgilerinin saklandığı bir veri tabanı kütüğünde

Yalnızca Öğrenci No.larının saklandığı alan adı OGRNO alanı

Yalnızca İsimlerin saklandığı alan adı ADSOY alanı

Yalnızca Telefonların saklandığı alan adı TELNO alanı

Her bir alanda tek bir tipte veri depolanmaktadır. Bütün öğrenci numaraları tek bir alanda,
bütün isimler tek bir alanda ve yine bütün telefonlar da tek bir alanda saklanmakta ve
bu alanlara alanın içeriğine uygun olmayan veri girilmemektedir.

**b-) Veri Kayıtları**

Veri tabanı kütüğüne girilen bilgilerdir. Veri tabanı kütüğünde her kayıt tek bir kişiye veya
nesneye aittir. Örneğin dört adet ile ait bilgileri sakladığımız oldukça basit bir kütük olan

“il” kütüğünü ele alalım.

| Kayıt No | ILKOD | ILADI | NUFUSU |
| --- | --- | --- | --- |
| 1 | 01 | ADANA | 2100000 |
| 2 | 16 | BURSA | 2000000 |
| 3 | 34 | İSTANBUL | 8000000 |
| 4 | 67 | ZONGULDAK | 750000 |

Her bir kayıtta sadece tek bir kişi veya nesneye ait bilgilerin depolanacağı kuralına uygun
olarak, yukarıdaki örnekte birinci kaydın sadece ADANA iline , ikinci kaydın sadece BURSA
iline üçüncü kaydın sadece ISTANBUL iline ve yine dördüncü kaydın ise sadece
ZONGULDAK iline ait bilgileri içerdiğine dikkat edelim.

Yine yukarıdaki örnekte ILKOD, ILADI, NUFUSU başlıklarının her birisi ayrı birer VERİ ALANI
ve her bir ile ait bilgiler ise ayrı birer VERİ KAYDI’ dır. Başka bir deyişle yukarıdan aşağıya
her sütün birer VERİ ALANI iken, soldan sağa doğru her satır ise ayrı birer VERİ KAYDI’dır.

**VERİ TABANI KÜTÜĞÜNÜN YAPISI:**

Veri tabanı yapısı, bir veri kütüğünün içindeki her alanın ayrıntılı tarifini içerir. Veri tabanı
kütüğünün yapısı şu şekildedir:

a-) Field Name (Alan Adı)

b-) Type (Alan Tipi)

c-) Width (Alan Genişliği)

**a-) Field Name (Alan Adı) :** Alfabetik (A-Z arası)bir değerle başlayıp sayısal bir değerle
devam edebilir. Karakterler arasında “ \_ “ sembolü ile ayırma yapılabilir. Bunların dışındaki
karakterler kabul edilmez. Aynı isim birden fazla alana verilemez. Aynı alan adı yazılırsa
uyarılarak bir süre bekletilir. Bir alan adı için kullanılabilecek toplam karakter uzunluğu
10 karakterdir. Bir alan adının uzunluğu 128 byte’ ı , bir kayıttaki alanların toplam uzunluğu
ise 4000 byte’ ı geçemez.

**b-) Type (Alan Tipi) :** Beş adet alan tipi vardır. Bunlar Character , Numeric, Date,
Logical, Memo alan tipleridir. Alan tiplerini seçmek için tiplerin ilk harfini yazmamız
veya ara çubuğuna (space bar) basmamız yeterlidir.

**c-) Width (Alan Genişliği) :**

Character 1-254 arası uzunlukta karakter alabilir

**N**umeric 1-19 arası uzunlukta karakter alabilir

**D**ate 8 karakter uzunluğunu otomatik olarak alır

**L**ogical 1 karakter uzunluğunu otomatik olarak alır

**M**emo 10 karakter uzunluğunu otomatik olarak alır

***2-DBASE KOMUTLARI ***

**1-) VERİ TABANI DOSYASI OLUŞTURMAK:**

DBASE ortamına girmek yani dbase’ i çalıştırmak için disk veya disketimizde aşağıdaki
dosyaların bulunması gerekmektedir:
DBASE.EXE
DBASE.MSG
DBASE.LD1
DBASE.OVL
DBASEINL.OVL
ASSIST.HLP
HELP.DBS

Yukarıdaki dosyalar disk veya disketimizde mevcut ise DBASE yazıp ENTER tuşuna
basarak Dbase ortamına girebiliriz.

CREATE komutunu kullanarak bir veri tabanı dosyası oluşturma işlemine
başlayabiliriz. Komutun Genel yazılımı şu şekildedir:

**CREATE dosya adı**

CREATE DENEME
CREATE KART
CREATE ORNEK

CREATE ORNEK yazıp ENTER tuşuna bastığımızda
karşımıza aşağıdaki türden bir ekran gelir:

Field Name “ISIM” yazıp ENTER tuşuna basınız. Type bölümünde yine ENTER tuşuna
basınız.Width için “ 10 ” yazıp ENTER tuşuna basınız. Yaptığımız bu işlemler ile ORNEK adlı
veri tabanı kütüğünde “ISIM” adında ve en fazla 10 karakter uzunluğunda bilgi girilebilecek
bir alan tanımlamış olduk. Böyle devam ederek aşağıdaki ekrana ulaşalım yani kütüğün
diğer alanlarını da aşağıdaki örneğe uygun olarak tanımlayalım.

Alan giriş tanımları sona erince CTRL+END tuşlarına basarız.

*Press ENTER to confirm. Any other key to resume.*

Mesajında ENTER tuşuna basarsanız oluşturduğunuz veri tabanı kütüğünü
(ORNEK.DBF adlı dosyayı) disk veya disketinize kaydetmiş olursunuz.
ENTER tuşundan başka herhangi bir tuşa basarsanız
kayıt yapılmaz. Kayıt işleminden sonra aşağıdaki mesaj ekranda görüntülenir.

*Input data records now? (Y/N)*

“Y” tuşuna basarsanız kütüğe bilgi girmeye başlarsınız. “N” tuşuna basarsanız
dbase nokta iletisine dönülür.

CREATE komutu ile bir dosya oluşturduğumuzda, daha önce aynı adla oluşturulmuş
bir dosya varsa o dosyanın içeriği sıfırlanır.

DBASE kullanarak oluşturduğumuz veri tabanı dosyalarının uzantısı “DBF” olur.

**
2- BİR DOSYAYI AÇMAK**

Önceden oluşturulmuş bir dosyayı içindeki bilgileri yok etmeden açmak için
USE komutunu kullanabiliriz. Komutun genel yazılımı şu şekildedir:**
USE dosya adı**
USE DENEME
USE KART
USE ORNEK

USE ORNEK yazıp ENTER tuşuna bastığımızda daha önceden CREATE komutunu
kullanarak oluşturup sakladığımız ORNEK.DBF adlı veri dosyasını ana bellekte aktif
hale getiririz,
yani açarız.

**3- DOSYAYA KAYIT İLAVE ETMEK:**

**APPEND **komutunu kullanarak dbase nokta iletisi konumundayken istenildiği anda,
ana bellekte o anda aktif olan yani açık olan kütüğe yeni bilgi ekleyebiliriz.

USE ORNEK yazıp dosyamızı açtıktan sonra, APPEND yazıp ENTER tuşuna basarak
daha önce oluşturduğumuz ORNEK adındaki dosyaya bilgi ilave edelim ve dosyamızın
içeriği aşağıdaki gibi olsun.

**4- KAYITLARI GÖRÜNTÜLEMEK:**

**DISPLAY (DISP) **komutunu kullanarak dbase nokta iletisi konumundayken istenildiği
anda, ana bellekte o anda aktif olan yani açık olan kütüğün kayıtları ekran yada yazıcıdan
görüntülenebilir.

**DISP** yazıp ENTER tuşuna bastığımızda açık olan kütüğün o anda üzerinde bulunulan
kaydı görüntülenir

**DISP record 3** yazıp ENTER tuşuna bastığımızda açık olan (aktif olan) kütüğün
3 numaralı kaydı görüntülenir

**DISP ALL** yazıp ENTER tuşuna bastığımızda açık olan (aktif olan) kütüğün bütün
kayıtları görüntülenir.

**DISP ALL ISIM,SOYAD,TELEFON** yazıp ENTER tuşuna bastığımızda açık olan
(aktif olan) kütüğün bütün kayıtlarının sadece, ISIM, SOYAD ve TELEFON bilgileri
görüntülenir.Kütüğün ISIM, SOYAD, TELEFON alanlarının dışında başka alanları varsa,
o alanlara ait bilgiler görüntülenmez.

**DISP record 3 ISIM,SOYAD,TELEFON** yazıp ENTER tuşuna bastığımızda açık
olan (aktif olan) kütüğün 3 nolu kaydının sadece, ISIM, SOYAD ve TELEFON bilgileri
görüntülenir.kütüğün ISIM, SOYAD, TELEFON alanlarının dışında başka alanları varsa,
o alanlara ait bilgiler görüntülenmez.
**
DISP ALL ISIM,SOYAD,TELEFON FOR “BAKIRKOY” $ ADRES**
yazıp ENTER tuşuna bastığımızda açık olan (aktif olan) kütüğün bütün kayıtları içinden
sadece ADRES alanında BAKIRKOY kelimesi geçen kayıtlara ait, ISIM, SOYAD ve TELEFON
bilgileri görüntülenir.kütüğün ISIM, SOYAD, TELEFON alanlarının dışında başka alanları
varsa, o alanlara ait bilgiler görüntülenmez.

**DISP ALL FOR SUBSTR(TELEFON,2,1)=”5”** yazıp ENTER tuşuna bastığımızda
açık olan kütüğün bütün kayıtları içinden sadece TELEFON alanının (telefon numaralarının)
ikinci karakteri 5 olan kayıtlara ait tüm bilgiler görüntülenir.

**DISP ALL ISIM,SOYAD,TELEFON FOR SUBSTR(TELEFON,2,1)=”5”**
yazıp ENTER tuşuna bastığımızda açık olan kütüğün bütün kayıtları içinden sadece
TELEFON alanının (telefon numaralarının) ikinci karakteri 5 olan kayıtların ISIM, SOYAD ve
TELEFON bilgileri görüntülenir.Kütüğün ISIM, SOYAD, TELEFON alanlarının dışında başka
alanları varsa,o alanlara ait bilgiler görüntülenmez.

**5- KAYITLARI LİSTELEMEK:**

**LIST **komutunu kullanarak dbase nokta iletisi konumundayken istenildiği anda, ana
bellekte o anda aktif olan yani açık olan kütüğün kayıtları ekran yada yazıcıdan
listelenebilir. **

LIST** yazıp ENTER tuşuna bastığımızda açık olan kütüğün bütün kayıtları listelenir.

**LIST ISIM,SOYAD,TELEFON** yazıp ENTER tuşuna bastığımızda açık
olan kütüğün bütün kayıtlarının sadece, ISIM, SOYAD ve TELEFON bilgileri listelenir.
Kütüğün ISIM, SOYAD, TELEFON alanlarının dışında başka alanları varsa, o alanlara
ait bilgiler listelenmez.

**6- KAYITLARI GÖRÜNTÜLEMEK ve DEĞİŞTİRMEK:**

**EDIT **komutunu kullanarak dbase nokta iletisi konumundayken istenildiği anda, ana
bellekte o anda aktif olan yani açık olan kütüğün kayıtlarını ekranda görüntüleyebilir
ve kayıtlar üzerinde değişiklikler yapabiliriz.

**EDIT** yazıp ENTER tuşuna bastığımızda açık olan kütüğün, o anda aktif olan kaydını
görüntüleyip üzerinde değişiklikler yapabiliriz. Yani kütüğün başındaysak ilk kaydı,
kütüğün sonundaysak ise son kaydı görüntüleyip değiştirebiliriz.

**EDIT record 3** yazıp ENTER tuşuna bastığımızda açık olan kütüğün, 3 nolu
kaydını görüntüleyip üzerinde değişiklikler yapabiliriz.

**7- KAYITLARI GÖRÜNTÜLEMEK ** **ve DEĞİŞTİRMEK:**

**BROWSE (BROWS) **komutunu kullanarak dbase nokta iletisi konumundayken
istenildiği anda, ana bellekte o anda aktif olan yani açık olan kütüğü, alanları yan yana
olarak ekranda listeleyip görüntüleyebilir ve kayıtlar üzerinde değişiklikler yapabilir yada
yeni kayıt girişi yapabiliriz.
BROWSE komutunu kullanabilmemiz için dosyada en azından bir adet kaydın mevcut
olması gerekmektedir. İstenilen alanda düzeltme yapmak için kursoru düzeltilecek alan
üzerine getirip değişiklik yapabilirsiniz.

**8- İSTENİLEN KAYDA GİTMEK:**

**GO **komutunu kullanarak dbase nokta iletisi konumundayken istenildiği anda, ana
bellekte o anda aktif olan yani açık olan kütüğün istediğimiz kaydına gidebiliriz.

**GO 3** yazıp ENTER tuşuna bastığımızda açık olan kütüğün, 3 nolu kaydına gideriz.

**GO TOP** yazıp ENTER tuşuna bastığımızda açık olan kütüğün, İLK kaydına
(yani kütüğün başına) gideriz.

**GO BOTTOM** yazıp ENTER tuşuna bastığımızda açık olan kütüğün, SON kaydına
(yani kütüğün sonuna) gideriz.

**SKIP **komutunu kullanarak dbase nokta iletisi konumundayken istenildiği anda,
ana bellekte o anda aktif olan yani açık olan kütüğün kayıtları arasında istediğimiz
sayıda İLERİ yada GERİ gidebiliriz.

**SKIP 3** yazıp ENTER tuşuna bastığımızda açık olan kütükte o anda bulunduğumuz
kayıttan 3 kayıt ileriye gideriz.

**SKIP -3** yazıp ENTER tuşuna bastığımızda açık olan kütükte o anda bulunduğumuz
kayıttan 3 kayıt geriye gideriz.

**9- KAYIT SİLMEK:**

**DELETED (DELE) **komutunu kullanarak dbase nokta iletisi konumundayken ,
ana bellekte o anda aktif olan yani açık olan kütüğün istediğimiz kaydını silinmek üzere
işaretleriz. Bunun anlamı silinen kaydın başına “ **\*** ” koymaktır.
DELE komutu ile silinmek üzere işaretlenen yani başına “ **\*** ” konulan kayıtlar istenilirse
dikkate alınır , istenilirse dikkate alınmaz.

**SET DELETED ON **yazılırsa, DELETED komutu kullanılarak silinmek üzere işaretlenmiş
olan kayıtlar işlemlerde dikkate alınır.
**
SET DELETED OFF** yazılırsa, DELETED komutu kullanılarak silinmek üzere işaretlenmiş
olan kayıtlar işlemlerde dikkate alınmaz.

**DELE RECORD 3** yazıp ENTER tuşuna bastığımızda açık olan kütüğün, 3 nolu kaydını
silinmek üzere işaretleriz.

**
****10- SİLİNEN KAYITLARI KURTARMAK:**

DELETED (DELE)** **komutu kullanılarak silinmek üzere işaretlenmiş kayıtları kurtarmak yani
kayıtların başındaki silinecek anlamına gelen “ **\*** ” işaretini kaldırmak için **RECALL **komutunu
kullanırız.

**RECALL RECORD 3** yazıp ENTER tuşuna bastığımızda açık olan kütüğün, daha önce
silinmek üzere DELE komutu ile işaretlenmiş 3 nolu kaydını eski haline getiririz yani
başındaki “ **\*** ” işaretini kaldırırız.

**10- SİLİNEN KAYITLARI TAMAMEN YOK ETMEK:**

DELETED (DELE)** **komutu kullanılarak silinmek üzere işaretlenmiş kayıtları yok etmek yani
RECALL komutu kullanılsa bile geri getirilemeyip dosyadan fiziksel olarak tamamen silinmesini
sağlamak için **PACK **komutunu kullanırız.

**PACK** yazıp ENTER tuşuna bastığımızda açık olan kütüğün, daha önce silinmek üzere DELE
komutu ile işaretlenmiş bütün kayıtlarını bir daha geri getirilemeyecek şekilde, tamamen
yok ederiz.

**11- BİR DOSYANIN TÜM KAYITLARINI YOK ETMEK:**

Bir veri tabanı dosyasında bulunan bütün kayıtları dosyadan fiziksel olarak tamamen silmek
yani dosyanın içindeki bütün kayıtları yok etmek için **ZAP **komutunu kullanırız. Bu komut
dosyanın içindeki bütün kayıtları yok edeceği için çok dikkatle kullanılmalıdır.**

ZAP** yazıp ENTER tuşuna bastığımızda açık olan kütüğün bütün kayıtlarını bir daha geri
getirilemeyecek şekilde, tamamen yok ederiz.

**12- BİR DOSYANIN YAPISINI GÖRMEK:**

Bir dosyanın kayıt yapısını görmek için **LIST STRU **veya **DISP STRU **komutunu
kullanırız.LIST STRU komutu ile DISP STRU komutu arasındaki fark çok sayıda alana sahip
dosyaların yapısını görüntülerken ortaya çıkar. DISP STRU komutu bir ekran dolduğu zaman
bir tuşa basmanız için beklerken, LIST STRU komutu beklemez ve dosyanın yapısını sonuna
kadar döker bu arada bilgi ekrandan hızla geçeceği için dosya yapısının tamamını sağlıklı
biçimde incelemekte zorlanabiliriz.

**DISP STRU** yada **LIST STRU** yazıp ENTER tuşuna bastığımızda açık olan kütüğün
kayıt yapısını görebiliriz. Yukarıdaki örnekte oluşturduğumuz ORNEK.DBF adlı dosyanın
içeriğini bu komutları kullanarak görmek istesek aşağıdaki gibi bir görüntü elde ederiz.

**13- BİR DOSYANIN YAPISINI DEĞİŞTİRMEK:**

Bir dosyanın yapısını daha önce girilen bilgilerimizi kaybetmeden değiştirebilmek için **
MODI STRU **komutunu kullanırız. Yukarıdaki örneği dikkate aldığımızda telefon numaralarını
girerken “9” karakter uzunluğunun yetmediğini (ülke ve şehir kodlarını da yazınca) daha
uzun telefon numaraları girmemiz gerektiğini düşünelim. Bu durumda TELEFON alanının
uzunluğunu örneğin 15 ‘e çıkarmak için MODI STRU komutunu kullanırız.

**14- TÜM KAYITLARDA BİR ALANIN YAPISINI DEĞİŞTİRMEK:**

Veri tabanı dosyasındaki herhangi bir alandaki bütün kayıtlara ait bilgileri değiştirmek için
**REPLACE **komutunu kullanırız. Komutun genel yazılımı :

REPLACE all DEĞİŞECEK ALAN ADI with NE ŞEKİLDE DEĞİŞECEĞİ

REPLACE all BUNU değiştir BU ŞEKİLDE

Yukarıdaki örneği dikkate aldığımızda telefon numaralarının tamamının başına örneğin “3”
getirmek için **REPLACE all TELEFON with “3” +TELEFON** yazıp ENTER tuşuna basmamız
yeterlidir.

**15- DOSYANIN BİR KOPYASINI ALMAK:**

Açık olan bir dosyanın başka bir isimle yeni bir kopyasını almak için **COPY TO **komutunu
kullanırız. Komutunu Genel Yazılımı şu şekildedir:

**COPY TO Yeni Dosya Adı**

**16- DOSYANIN YAPISINI BAŞKA BİR DOSYAYA KOPYALAMAK:**

Açık olan bir dosyanın içindeki kayıtlar( bilgiler) aktarılmadan, o dosyanın sadece yapısını
(sadece alanlarının adlarını, tiplerini ve uzunluklarını) başka bir dosyaya aktarmak için**
COPY STRUCTURE TO **komutunu kullanırız. Komutunu Genel Yazılımı şu şekildedir:

**COPY STRUCTURE TO Yeni Dosya Adı**

**17- AÇIK OLAN BÜTÜN DOSYALARI KAPATMAK:**

Açık olan bütün dosyaları kapatmak için **CLOSE ALL **komutunu kullanırız.

**18- EKRANI TEMİZLEMEK:**

Ekranı temizlemek için **CLEAR **komutunu kullanırız.

**19- DBASE ORTAMINDAN ÇIKMAK:**

Dbase ortamından çıkmak **QUIT **komutunu kullanırız.

***3-DBU PROGRAMININ TANITIMI*********

Database(veri) ve index dosyaları üzerinde işlem yapmamızı sağlayan çok kullanışlı bir yardımcı
programdır. Dbase nokta iletisinde komutlar kullanarak yapmak zorunda olduğumuz işlemlerin
hemen hemen tamamını bu programı kullanarak daha hızlı ve pratik yapma imkanımız vardır.
DBU yazıp ENTER tuşuna bastığımızda karşımıza aşağıdakine benzer bir ekran gelecektir.

**F1- Help :**Program ile ilgili yardım almak için kullanılır.

**F2- Open :****
Open-Database** : Önceden oluşturulmuş olan database kütüğünü (DBF) aktif hale
getiriyor, yani açıyor.**

Open-Index** : Önceden oluşturulmuş olan index dosyasını (NTX veya NDX)
aktif hale getiriyor, yani açıyor.**

Open-View** : Önceden oluşturulmuş olan görüntüyü açıyor.

**F3- Create :**

**Create-Database** : Bir database (DBF) kütüğünü ilk defa oluşturabilir veya var olan bir
kütüğün alanlarının yapısını (kütük yapısını) değiştirebiliriz.

**Create-Index** : Yeni index dosyası oluşturabilir veya var olan indeksi değiştirebiliriz.

**F4- Save :**

**Save-View **: Görüntüyü saklamak için kullanırız.

**Save-Struct **: Kütük yapısını saklamak için kullanırız.

**F5- Browse :**

**Browse-Database** : Aktif olan kütüğün bütün kayıtlarını üzerinde işlem yapabilmemiz için
bize gösterir. Kayıtlar üzerinde istediğimiz değişiklikleri yapabildiğimiz gibi mevcut kayıtları
silinmek üzere işaretleyebilir ya da kütüğe yeni kayıt ekleyebiliriz.

**Browse-View **: Görüntüyü kullanarak değişiklikler yapabiliriz.

**F6- Utility :**

**Utility-Copy** : Bir kütüğün istediğimiz koşulu sağlayan kayıtlarını yeni bir kütüğe aktarmak
amacıyla kullanabiliriz.

**Utility-Apppend** : Çalıştığımız kütüğe başka bir kütükten kayıt ekleyebiliriz.

**Utility-Replace** : Kütüğün istediğimiz alanlarının içindeki bilgileri değiştirebiliriz.

**Utility-Pack : **Silinmek üzere işaretlenmiş kayıtları yok ederiz, tamamen sileriz.

**Utility-Zap **: Kütüğün tüm kayıtalarını sileriz yani içindeki bilgileri yok ederiz.

**Utility-Run** : Dos komutlarını DBU içindeyken çalıştırabiliriz.

**F7- Move :**

**Move-Seek** : İndeksi olan database dosyalarının kayıtları arasında arama yapabiliriz.

**Move-Goto** : İstenilen kayda, kaydın record nosunu vererek ulaşabiliriz.

**Move-Locate** : İndex kullanmadan belirli bir koşulu sağlayan kayıtlara ulaşmak için kullanırız

**Move-Skip** : Kayıt atlamamızı sağlar.

**F8- Set :**

**Set-Relation** : Birden fazla DBF dosyasında ortak alanları sayesinde aynı anda hareket
etmemizi sağlar.

**Set--Filter ** ** **: Filtre oluşturur.

**Set-Fields** : Kütüğün alanlarının sırasını (yerlerini) değiştirir.

***4-DBASE-CLIPPER PROGRAM KOMUTLARI*********

Örnek programlarda kullanacağımız veri tabanı kütüğü ORNEK.DBF aşağıda listelenmiştir.

| Field Name | Type | Width | Dec |
| --- | --- | --- | --- |
| ADSOY | C | 25 |  |
| MAAS | N | 10 | 0 |
| TARIH | D | 8 |  |
| BKOD | C | 1 |  |

**
DO WHILE......ENDDO DÖNGÜ YAPISI**

**DO WHILE **<koşul>

**<komutlar>**

**ENDDO**

**DO WHILE **<koşul>

<komutlar>

**LOOP******

<komutlar>

**ENDDO**

**DO WHILE **<koşul>

<komutlar>

**EXIT******

<komutlar>

**ENDDO**

**DO WHILE <**koşul>

**DO WHILE **<koşul>

**<komutlar>**

**ENDDO**

**ENDDO**

Koşul doğru olduğu sürece komutlar işleme

girer.

LOOP deyimi ile DO WHILE döngüsü içinde

Karşılaşılırsa, LOOP deyimi ile ENDDO

arasındaki komutlar işleme alınmaz ve

DO WHILE döngüsünün başına dönülür.

EXIT deyimi ile DO WHILE döngüsü içinde

Karşılaşılırsa, EXIT deyimi ile ENDDO

arasındaki komutlar işleme alınmaz ve

DO WHILE döngüsünün dışına çıkılır.

İçiçe DO WHILE döngüsü kullanıldığında

Birbirini kesme olmaması gerekir. İşleme

En içteki döngüden dışa doğru devam edilir.

ÖRNEK-1

İsim ve soyadınızı ekranda 9 kere tekrarlayan ve her defasında kaçıncı kez isminizi tekrarladığını gösteren programı yazınız.

**CLEAR**

**SET TALK OFF**

**X=1**

ADSOY=”ERDİNÇ KAHRAMAN”

Do WHILE x<=9

? adsoy,x

x=x+1

ENDDO

CLEAR : Ekranı temizler

SET TALK OFF : Dbase yorumlayıcısında kullanılan komut ve deyimlerin sonuçlarını saklar.

? : Değişkeni ekranda yazdırır.

ÖRNEK-2

ORNEK.DBF kütüğündeki kayıtları “kütük başından sonuna doğru” , kayıt numaralarıyla beraber ekranda sıralayan programı yazınız. (Sadece adsoy alanını görüntüleyin).

**CLEAR**

**SET TALK OFF**

**USE ORNEK**

**GO TOP**

**Do WHILE .NOT. EOF( )**

**? adsoy , RECNO( )**

**SKIP**

**ENDDO**

**RETURN**

USE ORNEK : ORNEK.DBF adlı dosyayı çağırır( Ana bellkte aktif hale getirir)

GO TOP : Kütüğün en başına gider.

SKIP : Bir kayıt ileriye doğru atlatır.

RETURN : Programı sonuna geldiğini ve artık çalışabileceğini gösterir.

ÖRNEK-3

ORNEK.DBF kütüğündeki kayıtları “kütük sonundan başına doğru” , kayıt numaralarıyla beraber ekranda sıralayan programı yazınız. (Sadece adsoy alanını görüntüleyin).

**CLEAR**

**SET TALK OFF**

**USE ORNEK**

**GO BOTTOM**

**Do WHILE .NOT. BOF( )**

**? adsoy , RECNO( )**

**SKIP -1**

**ENDDO**

**RETURN**

GO BOTTOM : Kütüğün en sonuna gider.

SKIP -1 : Bir kayıt geriye doğru atlatır.

BOF ( ) : Kütük Başı

ÖRNEK-4

1 1

1 2

1 3

2 1

2 2

2 3

3 1

3 2

3 3

Yukarıdaki matrisi içiçe döngü kullanarak döken programı yazınız.

**CLEAR**

**SET TALK OFF**

**x=1**

**y=1**

**Do WHILE x<=3**

**Do WHILE y<=3******

**? x , y**

**y=y+1**

**ENDDO**

**y=1******

**x=x+1**

**ENDDO**

**RETURN**

IF.......ELSE........ENDIF KOŞUL YAPISI

**IF **<koşul>

**<komutlar>**

**ENDIF**

**IF **<koşul>

**<komutlar1>**

**ELSE**

**<komutlar2>**

**ENDIF**

Koşul doğruysa komutlar işleme girer, yanlışsa

İşleme girmez.

Koşul doğruysa <komutlar1> işleme girer ve

ENDIF deyimi ile bloktan çıkılır.

Koşul yanlışsa <komutlar2> işleme girer ve

bloktan çıkılır.

**ÖRNEK-1**

ORNEK.DBF kütüğündeki bkod=1 olan kayıtları , kayıt numaralarıyla beraber ekrana döken programı yazınız. (Sadece adsoy ve bkod alanlarını görüntüleyin).

**CLEAR**

**SET TALK OFF**

**USE ORNEK**

**GO TOP**

**Do WHILE .NOT. EOF( )**

**IF BKOD=”1”**

**? adsoy , bkod, RECNO( )**

**ENDIF**

**SKIP**

**ENDDO**

**RETURN**

ÖRNEK-2

ORNEK.DBF kütüğündeki maaşı 300.000.000 dan küçük olan kayıtları , kayıt numaralarıyla beraber ekrana döken programı yazınız. (Sadece adsoy ve maas alanlarını görüntüleyin).

**CLEAR**

**SET TALK OFF**

**USE ORNEK**

**GO TOP**

**Do WHILE .NOT. EOF( )**

**IF MAAS<300000000**

**? adsoy , maas, RECNO( )**

**ENDIF**

**SKIP**

**ENDDO**

**RETURN**

ÖRNEK-3

ORNEK.DBF kütüğündeki maaşı 300.000.000 dan küçük ve bkod=1 olan kayıtları , kayıt numaralarıyla beraber ekrana döken programı yazınız. (Sadece adsoy , bkod ve maas alanlarını görüntüleyin).

**CLEAR**

**SET TALK OFF**

**USE ORNEK**

**GO TOP**

**Do WHILE .NOT. EOF( )**

**IF MAAS<300000000**

**IF BKOD=”1”**

**? adsoy , bkod, maas, RECNO( )******

**ENDIF**

**ENDIF******

**SKIP**

**ENDDO**

**RETURN**

ÖRNEK-4

ORNEK.DBF kütüğünde kişinin maaşı 150.000.000 dan küçük veya 150.000.000 a eşitse kişinin adını soyadını ve maaşını görüntüleyip yanına “AZ KAZANIYOR” , ve kişinin maaşı 150.000.000 ‘dan büyük ise kişinin adını soyadını ve maaşını görüntüleyip yanına “İYİ KAZANIYOR” yazan programı yazınız. (Sadece adsoy ve maas alanlarını görüntüleyin).

**CLEAR**

**SET TALK OFF**

**USE ORNEK**

**GO TOP**

**Do WHILE .NOT. EOF( )**

**IF MAAS=<150000000**

**? adsoy , maas, “AZ KAZANIYOR”**

**ELSE**

? adsoy , maas, “İYİ KAZANIYOR”

ENDIF

SKIP

ENDDO

RETURN

ÖRNEK-5

ORNEK.DBF kütüğünde **sadece bkod=1 olan kayıtlar**** için kişinin maaşı 150.000.000 dan küçük veya 150.000.000 a eşitse kişinin adını soyadını ve maaşını görüntüleyip yanına “AZ KAZANIYOR” , ve kişinin maaşı 150.000.000 ‘dan büyük ise kişinin adını soyadını ve maaşını görüntüleyip yanına “İYİ KAZANIYOR” yazan ve programı yazınız. (Sadece adsoy ve maas alanlarını görüntüleyin).**

**CLEAR**

**SET TALK OFF**

**USE ORNEK**

**GO TOP**

**Do WHILE .NOT. EOF( )**

**IF BKOD=”1”**

**IF MAAS=<150000000**

**? adsoy , maas, “AZ KAZANIYOR”**

**ELSE**

**? adsoy , maas,** “İYİ KAZANIYOR”

ENDIF

ENDIF

SKIP

ENDDO

RETURN

ÖRNEK-6

ORNEK.DBF kütüğünde **sadece bkod=1 olan kayıtlar** için kişinin maaşı 150.000.000 dan küçük veya 150.000.000 a eşitse kişinin adını soyadını ve maaşını görüntüleyip yanına “AZ KAZANIYOR” , ve kişinin maaşı 150.000.000 ‘dan büyük ise kişinin adını soyadını ve maaşını görüntüleyip yanına “İYİ KAZANIYOR” yazan ve **bkod=1’den farklı olan kayıtlar için ise **kişinin adını soyadını görüntüleyip yanına “BKODU 1’DEN FARKLI” ifadesini yazan programı yazınız. (Sadece adsoy ve maas alanlarını görüntüleyin).

**CLEAR**

**SET TALK OFF**

**USE ORNEK**

**GO TOP**

**Do WHILE .NOT. EOF( )**

**IF BKOD=”1”**

**IF MAAS=<150000000**

**? adsoy , maas, “AZ KAZANIYOR”**

**ELSE**

**? adsoy , maas, “İYİ KAZANIYOR”**

**ENDIF**

**ELSE**

**? adsoy , maas, “BKODU 1’DEN FARKLI”**

**ENDIF**

**SKIP**

**ENDDO**

**RETURN**

**DO CASE......CASE........ENDCASE**

İçiçe IF deyimleri ile birden fazla koşulu kontrol edebildiğimiz gibi, aynı işlemi DO CASE.....ENDCASE blokları ile de yapabiliriz. DO CASE bloklarında tanımlanan koşullardan sadece birisi doğruysa, onunla ilgili deyimler işleme girer. Kullanılması içiçe IF deyimlerinden daha kolaydır. Program işlemesi sırasında da daha hızlı çalışır.

**DO CASE**

**CASE** <koşul-1>

<komutlar-1>

**CASE** <koşul-2>

<komutlar-2>

**..................................**

**..................................**

**..................................**

**CASE** <koşul-n>

<komutlar-n>

\[**OTHERWISE**\]

<komutlar-x>

**ENDCASE**

Koşul-1 doğruysa komutlar-1

Koşul-2 doğruysa komutlar-2

Koşul-n doğruysa komutlar-n işleme girer.

OTHERWISE hiçbir koşulun sağlanamaması durumunda işleme girer ve komutlar-x çalışır.

ÖRNEK-1

ORNEK.DBF kütüğünde **bkod** alanını kullanarak kişilerin adlarını soyadlarını ve unvanlarını döken programı yazınız.

bkod =1 ise ünvanı MÜDÜR bkod =2 ise ünvanı ŞEF bkod =3 ise ünvanı MEMUR

**CLEAR**

**SET TALK OFF**

**USE ORNEK**

**GO TOP**

**Do WHILE .NOT. EOF( )**

**DO CASE**

**CASE bkod=”1”**

**YAZ=”MÜDÜR”**

**CASE bkod=”2”**

**YAZ=”ŞEF”**

**CASE bkod=”3”**

**YAZ=”MEMUR”**

**ENDCASE**

**? adsoy , YAZ******

**SKIP**

**ENDDO**

**RETURN**

---
*Kaynak: `VERI TABANI YONETIMI - DBASE/VERI TABANI YONETIMI - DBASE.doc` — OBILGIC — 2004*
