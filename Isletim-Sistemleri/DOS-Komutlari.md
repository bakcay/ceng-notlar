# DOS Komutlari

Görme Engellilere göre uyarlanmış Dos İşletim sistemi ve komutları

Hazırlayan:

Ibrahim Elibal

ASİİ KODLARINA GÖRE KAREKTERLER:

! Ascii 33 ünlem

' Ascii 39 tek tırnak

+ Ascii 43 artı

% Ascii 37 yüzde

& Ascii 38 ve

/ Ascii 47 bölü

( Ascii 40 sol parantez

) Ascii 41 sağ parantez

= Ascii 61 eşittir

? Ascii 63 soru işareti

\* Ascii 42 yıldız

- Ascii 45 eksi, tire

\_ Ascii 95 alt çizgi

, Ascii 44 virgül

; Ascii 59 noktalı virgül

: Ascii 58 iki nokta üstüste

\\ Ascii 92 tersbölü

\# Ascii 35 rakam işareti

$ Ascii 36 dolar işareti

< Ascii 60 küçüktür

> Ascii 62 büyüktür

" Ascii 34 çift tırnak

@ Ascii 64 ed işareti

bibar Ascii 124 bibar işareti

~ Ascii 126 tilda işareti\_

DOS İŞLETİM SİSTEMİ HATA MESAJLARI

Bilgisayarla çalışırken onunla devamlı iletişim halinde olursunuz. Kullanıcı isteklerini komutlarla bildirirken bazı hatalar oluşur. Dos işletim sisteminde karşılaşılan hata mesajlarının anlamlarını bilmek, çözüm üretmekte zorlanmamak anlamına gelir. Sık karşılaşılan hata mesajları:

a) Bat command or file name ( Yanlış komut veya yanlışdosya adı) En çok karşılaşılan hata mesajıdır. Çünkükomut yazılırken yanlış harflere basılabilir. Olmayan programdosyalarıçalıştırmaya kalkışabiliriz. Bunedenle yazarken doğru komutları yani doğru harfleri kullanmalıyız.

b) Bad or missing command interpreter (Bozuk ya da eksik komut işlemcisi):

Msdos komutları çalışırken Command.com dosyası bozulduğunda

ya da yanlışlıkla silindiğinde bu hata mesajı görüntülenir. Hatayı

düzeltebilmek bir sistem disketiyle bilgisayarı yeniden başlatmak ve

Command.com adlı dosyayı ana dizine kopyalamak gerekir. c) Data error reading drive A: (A sürücüsünde veri okumahatası) Böyle bir

mesajla karşılaştığımızda büyükolasılıkla disket bozulmuştur. Msdos'un Scandisk programı çalıştırılarak disket kurtarılabilir. Eğer düzelme olmuyorsa disket yeniden formatlanmalıdır. Ç) Error in Exe file (Exe dosyasında hata) Çalıştırmak istenen uzantısı exe olan dosyaların bozuk olduğunda görüntülenir.

d) File not found (Dosya bulunamadı) Dos işletim sisteminde yaptığımız işlemlerde eğer yanlış dosya adı yazmışsak ya da o dosya gösterdiğimiz yerde bulunmuyorsa bu mesaj karşımıza çıkar.

e) Acces denied: (Erişim engellendi) Sadece okunabilir

niteliğe sahip bir dosya silinmek istendiğinde dosyanın silinemeyeceğini belirten bu mesaj ekrana gelir.

f) Batch file missing: Toplu işlem dosyasının bulunamadığı uyarısında bulunur.

g) Directory all ready exist: Disk-diskette bulunan

dizinleri aynı ortamda yeniden oluşturmak istediğimizde "Dizin zaten var" anlamında bu mesaj ekrana gelir.

h) Drive not ready error

Sürücüye disket takılı değilken bilgisayar açıldığında disket hazır değil

anlamında bu mesaj ekrana gelir.

i) File can not be copied on to itself:

Bir dosya yine aynı isimde aynı yere kopyalanmak istenildiğinde dosya kendi içerisine kopyalanamaz anlamında bu mesaj ekrana gelir.

j) General failure reading drive ... Abort, Retry, İgnore, Fail?

Sürücüde bulunan disket okunamıyor. Disketin bozuk ya da formatsız olması durumunda bu mesaj ekrana gelir.

Abort: Vazgeç, Retry: tekrar et, İgnore: Hatayı görme,Fail: Sürücü değiştir anlamlarına gelir.

k) İnsert system disk in drive A and press any key

Sürücüye bir sistem disketi takılması gerektiğini belirten bir mesajdır.

l) İnsufficent disk space 0 file(s) copied

Hedef diskette boş alan olmadığı için kopyalama yapılamayacağını belirten mesajdır.

m) İnvalid Command.com

Kullanılan Command.com dosyası geçersizdir mesajıdır.

n) Press any key to continue

Devam etmek için herhangi bir tuşa bas.

o) Program too big to fit in memory

Program bellek için çok büyük.

Ö) Terminate Batch Job?(Y/N)

Toplu işlem dosyası çalışırken Ctrl artı C tuşları seçilirse işlemin yarıda kesilip kesilmeyeceğini sorgulayan bu mesaj ekrana gelir.

p) Too many parameters

Bir komuta ait olmayan bir parametre kullanıldığında bu mesaj ekrana gelir.

r) Write protect error

Disketin yazmaya ve silmeye karşı korumalı olduğunu bildiren mesajdır.

Klavye kullanımı:

Bu bölümde klavye üzerinde bulunan tuşları ve genel olarak ne işe

yaradıklarını göreceğiz. Kullandığımız klavyeye göre tuşların aldığı özellikler farklılık göstermektedir. Ancak genel olarak her yerde kullanılan klavye türünün üstünde bulunan tuşları anlatacağız.

Klavyemizde grup olarak 5 tuş grupu bulunmaktadır. Bunlardan

en büyüğü olan yazılarımızı yazdığımız bölümdür. Bu tuş grubunda 62 adet tuş bulunmaktadır. Yazılarımızı yazdığımız ana bölümde 5 satır

bulunmaktadır. Bu satırların en üst satırında bulunan tuşlar soldan sağa doğru şöyledir:

Tırnak 1 2 3 4 5 6 7 8 9 0 \* - back-space

Üsten ikinci sırada bulunan tuşlar:

Tab Q W E R T Y U I O P Ğ Ü Enter tuşunun bir bölümü Üsten üçüncü sırada bulunan tuşlar: Büyük harf kilidi A S D F G H J K L Ş İ virgül Enter tuşunun bir bölümü

Yukarıdan aşağıya doğru dördüncü sırada bulunan tuşlar:

Shift Küçüktür-Büyüktür Z X C V B N M Ö Ç . Shift En alt satırda bulunan tuşlar ise:

Ctrl Windows Alt Space Alt indows1 Windows2 Ctrl

Bu tuşları sıralanışına göre sağ el sol el olarak iki şekilde kullanırız. Ellerimize göre tuşların ayrımını temel sırada

bulunan F J tuşlarının üstündeki kabartılmış bölümler ayırır. Sol elimizin işaret parmağı sol tarafta bulunan kabartılmış tuşun üstüne yani F tuşunun üstüne konur.

Diğer parmaklarımızı buna göre diğer tuşlara yerleştiririz. Yani sol el işaret parmağımız F tuşuna, Orta parmağımız D tuşuna, yüzük parmağımız S tuşuna, serçe parmağımız A tuşuna gelir. Buna göre temel sırada bulunan diğer tuşlarada J tuşunu başlangıç olarak aldığımızda parmaklarımızı yerleştiririz. Sağ el işaret parmak J tuşuna, orta parmak K tuşuna, yüzük parmak L tuşuna, serçe parmak Ş tuşuna konur. Temel sırada iki elin ortasında kalan tuşlar ise G H tuşlarıdır. Bu tuşlardan G harfine sol el işaret parmağı ile, H tuşuna sağ el işaret parmağı ile basılır. Temel sırada bulunan İ harfine de sağ el serçe parmakla basılır. Ayrıca temel sırada bulunan , (virgül) tuşuna da sağ el serçe parmakla basılır. Yine temel sırada bulunan büyük harf tuşu kilidine ise sol el serçe parmakla basılır. Temel sıranın sağ tarafında bulunan Enter tuşuna sağ elimizi biraz kaldırarak sağ serçe parmakla basarız. Harf tuşlarını öğrenmeyi sürdürelim. Sol elimizle, temel sıranın üstündeki tuşları şöyle

kullanacağız: Sol el işaret parmağımızla F tuşunun çok hafif solunda üstte bulunan R tuşuna basıyoruz. Orta parmak ile D tuşunun çok hafif

solunda üstte bulunan E tuşuna basıyoruz. Yüzük parmağımızla S tuşunun çok hafif solunda üstte bulunan W tuşuna basıyoruz. Serçe

parmağımızla A tuşunun çok hafif solunda üstte bulunan Q tuşuna basıyoruz. Bu sıranın solunda bulunan en son tuş ise Tab (sekme) tuşudur. Bu tuşa ise sol el serçe parmakla basıyoruz. Sağ elimizle temel sıranın üstündeki tuşların kullanımı ise şöyledir: Temel sırada sağ el işaret parmağımızla bastığımız J tuşunun çok hafif solda üstte bulunan tuş U tuşuna basıyoruz. Orta parmak ile K tuşunun çok hafif solda üstte I tuşuna basıyoruz. Yüzük parmağımızla L tuşunun çok hafif solda üstte O tuşuna basıyoruz. İşaret parmağımızla Ş tuşunun çok hafif solunda üstte P tuşuna basıyoruz. Sağ tarafta kalan Ğ Ü tuşlarına da sağ el serçe parmağımızla basıyoruz. Yine bu sıranın sağ tarafında uçta bulunan enter tuşuna da sağ el serçe parmakla basarız. (Enter tuşu hem temel sırada hem de üst sırada genişçe bulunan tek bir tuştur.) Bu sıranın

ortasında kalan T Y tuşlarından T tuşuna sol el işaret parmağımızla Y tuşuna sağ el işaret parmağımızla basıyoruz. Harflerin bulunduğu tuş grubunun en üst satırında bulunan tuşların ellerimize göre dağılımı ise şöyledir: Sol el işaret parmağımızla temel sırada F onun üstündeki

sırada R tuşlarına basıyorduk. R tuşunun çok hafif solunda bulunan tuş 4

tuşudur. Orta parmağımızla 3, yüzük parmağımızla 2, serçe parmağımızla 1 tuşlarına basarız. Yine sol el serçe parmağımızla en solda bulunan " (çift tırnak) tuşuna basarız. Ortada kalan 5 6 tuşlarından 5 rakamına sol el işaret parmağımızla, 6 rakamına sağ el işaret parmağımızla basarız. Sağ el temel sırada bastığımız tuş J onun üstünde bastığımız tuş U tuşu idi. U tuşunun çok hafif solda üstte bastığımız tuş 7 tuşudur. Orta parmak ile 8, yüzük parmak ile 9, serçe parmak ile 0 tuşlarına basarız. Bu sıranın en sağında bulunan \* - back-space (geriye doğru silme) tuşlarına da sağ el serçe parmakla basarız. Yazı yazdığımız bölümün temel sıranın altındaki

sırada bulunan tuşlar ise şöyle sıralanmaktadır: Temel sırada sol el işaret parmağımızla F tuşuna basıyorduk. Sol el işaret parmağımızla F tuşunun çok hafif sağ altta bulunan V tuşuna basıyoruz. Orta parmakla ile D tuşunun çok hafif sağında altta C tuşuna basıyoruz. Yüzük parmağımızla S tuşunun çok hafif sağında X tuşuna basıyoruz. Serçe parmağımızla A tuşunun çok hafif sağında altta Z tuşuna basıyoruz. Alt sıranın Z tuşunun solunda bulunan Büyüktür- küçüktür tuşuna ise sol el serçe parmakla basıyoruz. Sol el serçe parmağımızla alt sıranın en solunda bulunan

shift tuşuna da sol el serçe parmakla basıyoruz . Sağ elimizin işaret parmağıyla bastığımız tuş J tuşudur. Bu tuşun çok hafif sağında altta

bulunan tuş M tuşudur. Orta parmakla bastığımız K tuşunun çok

hafif sağında altta Ö tuşuna basıyoruz. Yüzük parmağımızla bastığımız L tuşunun çok hafif sağında altta Ç tuşuna basıyoruz. Serçe parmağımızla bastığımız Ş tuşunun çok hafif sağında . (nokta) tuşuna basıyoruz. Alt

sıranın en sağında bulunan shift tuşuna da sağ el serçe parmağımızla basıyoruz. Alt sıranın iki elin ortasında kalan B N tuşlarından B harfine sol el işaret parmağı ile N tuşuna sağ el işaret parmağıyla basarız. Yazı yazdığımız bölümün en altında bulunan tuşlar ise şöyledir: En alt

sıranın en solunda bulunan ctrl (control) tuşuna sol el serçe parmakla, bu

tuşun yanında bulunan windows (Bu tuş windows'da kullanılır) tuşuna kullanımı sizce rahat olan parmağınızla basınız. Bu tuşu izleyen sol alt

(alternatif) tuşuna sol el baş parmakla, ortada bulunan uzun tuşa sağ ya da sol el baş parmakla, bu tuşun sağında bulunan sağ alt (alternatif) tuşuna sağ el baş parmakla, sonraki windows (bu tuşlar windows'da kullanılır) tuşlarına (İki adet) kullanımı rahat olan parmakla ve en alt

sıranın en sağında bulunan sağ ctrl (control) tuşuna sağ

el serçe parmakla basarız. Yazıları yazdığımız klavyenin hemen sağ tarafında yani sağ ctrl tuşunun hemen sağında 4 adet tuş bulunmaktadır. Burada bulunan tuşlar yön tuşlarıdır. 3 adet tuş alt sırada ve 1 adet tuş ortada bulunmaktadır. Sağ elimizin işaret parmağını solda olan tuşun üstüne gelecek şekilde sağ el orta parmak ve yüzük parmaklarımızı tuşlara yerleştiririz. Böylece orta parmağımızla iki adet tuşu kontrol etmeye başlarız. Sağ el orta parmağımızla kontrol ettiğimiz tuşlardan yukarıda tek başına olan, yukarı yön tuşu, imleçimizi yukarıya doğru satır satır hareket ettirmeye yarar. Bu tuşun hemen altında bulunan, aşağı yön tuşu ise, imleçimizi aşağıya doğru satır satır hareket

ettirmek amaçıyla kullanılmaktadır. Sağ el yüzük parmağımızla kontrol

ettiğimiz tuş ile imleçimizi sağa doğru 1 karekter hareket ettirir. Sağ el işiaret parmağımızla kontrol ettiğimiz tuş ile imleçimizi sola doğru 1 karekter hareket ettirmekte kullanırız. Yön tuşlarının hemen üstünde bulunan bölümdeki tuş grubunda 6 adet tuş bulunmaktadır. Bu tuşların

yardımıyla imleçimizi hızlı hareket ettirebilmekteyiz. Kısaca ekran üzerinde yaptığımız tarama işlemlerinde bize hız kazandırmaktadır.

Bu tuşlar iki sıra halinde bulunmaktadır. 3 adet üst sırada,3 adet alt

sırada olmak üzere 6 adettir. Bu tuşların üst sırasında bulunan tuşlar soldan sağa doğru şöyledir: insert home page-up Bu bölümün alt sırasında soldan sağa doğru bulunan tuşlar: del end page-down Bu tuş grubunu da sağ elimizle kullanmaktayız. Soldan sağa doğru sağ elimizin işaret parmağı, orta parmağı ve yüzük parmağını bu tuşların alt sırasına yerleştirelim. Burada bulunan tuşların görevlerini genel özellikleriyle

görelim. Sağ el yüzük parmağımızın üzerinde bulunduğu tuş "page own" tuşudur. Bu tuşun yardımıyla o an çalıştığımız programın özelliklerine göre şu işlemleri yapabilmekteyiz:İmleçimizi, ekranın neresinde olursak

olalım, ekranın en alt satırına götürür. Diğer bir yaptığı görevse imleçimizi bir sayfa ya da bir ekran görüntüsü ileri götürür. Yine sağ el yüzük parmağımızla "page down" tuşunun hemen üstünde bulunan "page up" tuşunuda kontrol etmekteyiz. Bu tuşun görevi çalışılan programın özelliklerine göre farklılık kazanmaktadır. Çalışılan programa göre imleçimizi, ekranın neresinde olursak olalım, ekranın en üst satırına taşır. Diğer göreviyse imleçimizi bir sayfa öne ya da ekran görüntüsünü bir önceki görüntüye taşır. Sağ el orta parmakla kontrol ettiğimiz alt sıradaki tuş "end" tuşudur. Bu tuşun görevi çalışılan programa göre imleçimizi satırın sonuna ya da ekrandaki görüntünün en altına götürür.

Sağ el orta parmakla kontrol ettiğimiz diğer bir tuş "home" tuşudur. Bu tuşla çalışılan programa göre imleçimizi ya satırın başına ya da

ekrandaki görüntünün üst bölümüne taşır. Sağ el işaret parmağımızla alt sırada kontrol ettiğimiz tuş "del" tuşudur. Bu tuşla, çalışılan programa

veya işletim sistemine göre farklı işler yapmaktayız. Temel olarak silme

işlemini yapan bu tuş, Msdos'dayken üzerinde bulunduğumuz karekteri siler. Diğer kullanım alanları ise; bloklanmış ya da işaretlenmiş bölümleri siler. Sağ el işaret parmağımızla üst sırada kontrol ettiğimiz tuş "insert" tuşudur. Bu tuşla yaptığımız işler de çalışılan programa göre farklılık kazanmaktadır. Diğer göreceğimiz tuş grubu ise klavyemizin en üst bölümünde bulunan 16 adet tuş grubudur. Bu tuşlardan en soldaki tuş "esc" tuşudur. Bu tuşla çalıştığımız programa göre ya programdan çıkmaya yarar ya da ekran görüntüsünü değiştirmeye yarar. Bu tuştan sonra dört adetten oluşan 12 adet fonksiyon tuşları gelmektedir. Bu tuşların sabitleşmiş görevleri bulunmamaktadır. Çalışılan programa göre,

yapılan programla ilgili işlevleri aktif hale getirirler. F1-2-3-4....11-12 şeklinde isimlendirilirler. Bu tuşlardan sonra 3 adet tuş daha bulunmaktadır. Bu tuşları soldan sağa doğru sıralandığında: Print-screen (ekran görüntüsünü yazıcıdan almak), scro lock, pause tuşları yer alır. Klavyemizde bulunan 5'inci tuş grubumuz, rakamların

bulunduğu tuş grubudur. Bu tuşlar 17 adettir. Bu tuşların en üstte ve sol köşede bulunan tuşun on- off olma durumuna göre buradaki tuşlar görev

değiştirmektedir. Öncelikle Num-lock tuşunun on konumundayken

tuşların aldıkları görevleri görelim:

En üst sıra ve soldan sağa doğru: num-lock / \* -

Üstten ikinci sıra ve soldan sağa doğru: 7 8 9 +

Üstten üçüncü sıra ve soldan sağa doğru : 4 5 6 +

Üstten dört'üncü sıra ve soldan sağa doğru: 1 2 3 enter

Üsten beşinci sıra ve soldan sağa doğru: 0 . enter

Sizinde fark ettiğiniz gibi num-lock tuşu on konumundayken burada bulunan tuşlar, ilk halleriyle kullanılmaktadır. Şimdi bu tuşların num-lock off halindeyken aldıkları görevleri görelim:

/ (bölü), \* (yıldız), + (artı), Enter bu tuşlar ilk

hallerini korumaktadırlar. Ancak - (tire) tuşu kullanmış olduğumuz ekran okuma programının Review (gös gezdir-tarama) moduna geçmek için kullanılır. Diğer kalan tuşlardan 5 rakamını merkez aldığımızda 2 tuşu aşağı ok yön tuşuna, 8 tuşu yukarı ok yön tuşuna, 6 tuşu sağa ok

yön tuşuna, 4 tuşu sola ok yön tuşuna dönüşmektedir. Bunun yanı sıra 1 tuşu "end" tuşuna, 7 tuşu "home" tuşuna, 3 tuşu "page-down" tuşuna dönüşmektedir. Arta kalan 0 tuşu Msdos'da kullandığımız ekran okuma programının satır okuma tuşu, . tuşu sistem imleçimizin hangi satır ve kaçıncı karekterin üzerinde durduğunu söyleyen tuş görevini almaktadır. Hatırlayacaksınız bu bölümün başlarında bazı tuşlardan bahsettim. Nerede olduğunu öğrendiğiniz bu tuşların ne işe yaradıklarını görelim: ctrl (control) tuşları yazı yazma klavyesinin en alt satırının en solunda ve en sağında olmak üzere iki adettir. Bu tuşlarla birlikte başka tuşlar kullanılmaktadır. İşte birlikte kullanılan tuşlara bazı joker görevler verilmiştir. Ctrl tuşu ile birlikte joker görevi verilen tuşlar kullanıldığında

bu görevleri aktif hale gelir. örnek: ctrl artı s tuşuna bastığımızda işaretlenmiş ya da üzerinde çalışılan bölüm disk-diskette kayıt edilir. Örnek2: ctrl artı f tuşuna bastığımızda bir metin içerisinde bir kelimeyi arayabiliriz.

Alt (alternatif) tuşlar boşluk tuşunun sağ ve solunda olmak üzere iki adettir. Bu tuşların Msdos'da kullanım amaçları ctrl tuşlarıyla hemen hemen aynıdır. Klavyede bulunmayan bazı karekterleri ekranda görüntülenmesi için bu alt tuşlarından yararlanılır. Bunların yanı sıra ctrl tuşları gibi kendisiyle birlikte kullanılan tuşlara verilen joker tuş görevlerini aktif hale getirir. Örnek1: Vurguladığımız ilk durum için şöyle bir örnek inceleyelim: @ (ed) işaretinin klavyede belli bir tuşu bulunmamaktadır. Bu işareti ekranda görüntüleyebilmek için sağ tarafta bulunan alt tuşuyla birlikte q harfine basmamız gerekmektedir. Böyle @

işaretini elde ederiz. Örnek2: Klavyede bir çok işaretin tuşu bulunmamaktadır. Bu şekilleri ekranda görüntüleyebilmek için ascii kodlarından yararlanırız. Örneğin bibar işaretini eski klavyelerde ekranda görüntülemek için num-lock tuşunu on konumuna getiririz. Sol alt tuşunu basılı tutarak en sağda bulunan rakamların olduğu bölümden 124 tuşlarız. Böylece biber simgesini elde ederiz. Yazı yazdığımız ana bölümde en solda alttan dört'üncü tuş tab (sekme) tuşudur. Bu tuş farklı görevler almaktadır. Eğer yazı yazma ekranındaysak bu tuşa bastığımızda imleçimizi satır başından 5 karekter içeri taşır. Ya da çalıştığımız programımızın menüsündeyken menü içinde bulunan seçenekler arasında geçiş yapmamızı sağlar. Bu tuşa basarak istediğimiz seçeneğe geliriz. Tab tuşunun hemen altında bulunan yani en solda alttan

üçüncü tuş Büyük harf kilit tuşudur. Bu tuşun on-off kullanımları vardır. Eğer bu tuş on konumundaysa yazdığımız sadece harfler büyük yazılır. Sürekli büyük harfle yazma durumlarında bu tuşun on konumu kullanılır. Bu durumun dışında bu tuş off konumunda durmalıdır. Büyük harf kilit tuşunun hemen altında bulunan tuş shift tuşudur. Bu tuşu sadece ilk harfleri büyük yazılacak kelimeler için ve çift kullanımlı tuşların diğer özelliklerini elde etmek için kullanıyoruz. Bu tuştan iki

adet bulunmaktadır. Soldaki tuşla aynı hizada diğer uçta bulunmaktadır. Örnek: Ahmet yazmak istiyoruz.

Klavyede A harfi solda bulunuyor. Bu nedenle sağ elimizle sağ taraftaki shift tuşunu basılı tutarak A harfine sol elimizle basarız. Ekranda A harfini büyük olarak görüntüleriz. Dikkat: tuşlar oldukça duyarlı olduğundan istediğimiz karekteri hafif bir dokunmayla elde ederiz.

Shift tuşuyla birlikte kullanılan karekterler ve elde edilen karekterler:

Shift artı nokta birlikte kullanıldığında : işareti (iki nokta üst üste)

meydana gelir. shift artı virgül ; (noktalı virgül) elde edilir. Shift artı < (küçüktür) tuşlarının birlikte kullanımından > (büyüktür) işareti

elde edilir.

Shift artı 1 birlikte kullanımından ! (ünlem) elde edilir.

Shift artı 2 birlikte kullanımından ' (apostrof) elde edilir.

Shift artı 4 birlikte kullanımdan + (artı) elde edilir.

Shift artı 5 birlikte kullanımından % (yüzde) elde edilir.

Shift artı 6 birlikte kullanımından & (and ) elde edilir.

Shift artı 7 birlikte kullanımından / (bölü ) elde edilir.

Shift artı 8 birlikte kullanımından ( sol parantez elde edilir.

Shift artı 9 birlikte kullanımından ) sağ parantez elde edilir.

Shift artı 0 birlikte kullanımından = eşittir elde edilir.

Shift artı \* (yıldız) birlikte kullanımından ? (soru işareti) elde edilir.

Shift artı - (eksi) birlikte kullanımından \_ (altçizgi) elde edilmektedir.

Ters-bölü (back-slash) işaretini elde edebilmek için sağ alt tuşu ile birlikte yıldız tuşuna basmamız gerekmektedir. Back-space tuşu yazdığımız karekterleri bir geri olmak üzere siler. Yani imleçimizin üzerinde bulunduğu karekterden önceki bulunan karekteri siler. Msdos'da bazı dizinleri değiştirirken karşılaştığımız ~ (tilda- sonsuz) işaretinin klavyeden ascii kodlarını kullanarak çıkarabiliyoruz. Bunun için num-lock tuşunu on konumuna getiriyoruz. Sol alt tuşuna elimiz basılı iken rakamların bulunduğu en sağdaki tuş grubundan 126 tuşlamamız gerekmektedir.

İŞLETİM SİSTEMİ VE ÖNEMİ:

Bir çok parçadan meydana gelen bilgisayardan yararlanabilmemiz

için her şeyden önce bilgisayarımızın çalışıyor olması gerekir. Bilgisayarımızın çalışıyor olabilmesi için ve bizimle iletişim sağlayabilmesi için bir programa (yazılım) gereksinim duyulmaktadır. Bu yazılım sıradan bir yazılım değildir. Her program bilgisayarı çalıştıramaz. Bilgisayarları çalıştırabilecek yazılımlar farklılık arzeder. Örneğin bir oyun programı bilgisayarı çalıştıramaz. Bu oyun programını

bilgisayarda yüklü olan işletim sistemi tarafından çalıştırılır. Bilgisayarların çalışmalarını sağlayan disk yönetim sistemleri vardır. Bilgisayarı tanıyan tüm çalışmalarını kontrol altında tutarak bilgisayarı yöneten yazılımlara işletim sistemi denir. İşletim sistemi bilgisayarın tüm birimleri arasında iletişimi sağlar. İşletim sistemi yüklenmemiş bilgisayarları hiç bir kullanıcı kullanamaz. İşletim sistemleri bilgisayarın

açılması ve çalışması için olmazsa olmaz programlardır. İşletim sistemi, bilgisayar donamları arasında iletişimi sağlayarak, aygıtların etkin kılınmasını gerektiren yazılımları yükleyen, bu aygıtları kullanıcının kontrolüne sunulmasını sağlayan ve kullanıcıdan gelen komutlarla ilgili aygıtlara bildiren sistem yazılımlarıdır.

İşletim sistemlerinin işlevleri:

1) Kullanıcı ile merkezi işlem birimi arasında iletişim sağlar.

2) Giriş ve çıkış devreleri arasındaki veri akış yönünü ve işlemleri kontrol eder.

3) Donanım aygıtlarını yönetir.

4) Programların çalışmasını kontrol eder.

5) Veri ve dosya saklama işlemlerini yapar.

6) Sistemin etkin bir şekilde işlemesi için güvenlik ve kontrol sağlar.

İşletim sisteminin yukarıda sayılan işlevlerine dikkat edildiğinde,

bir yöneticiden beklenen tüm sorumlulukları ve yetkileri bulunmaktadır.

İŞLETİM SİSTEMİ ÇEŞİTLERİ:

Günümüzde en çok yararlanılan ve kullanılan işletim sistemleri şunlardır: 1- Windows 95-98: Bu program etkileşimli ara bir programdır.

Bilgisayarın ara birimleri arasında kolay, düzenli ve güvenli iletişimi sağlayan işletim sistemidir.

2- CPM: (Control program for micro computer) Micro bilgisayarlar için kontrol programı. Bu işletim sistemi 8 bit'lik mikro bilgisayarlar için hazırlanmıştır. Bu programın özelliği; kendi yapısındaki donanım içinde bios'ta toplanmıştır. Programın küçük bir yerinde yapılabilecek bir değişikle diğer bilgisayarları da çalıştırması sağlanmaktadır. Günümüzde pek kullanılmayan bir işletim sistemidir.

3- Os2: İşletim sistemi 2 olarak da söylenmektedir. Bu sistem MSdos işletim sistemindeki bazı sınırlamaları ortadan kaldırmak için geliştirilmiştir. Msdos işletim sistemindeki sınırlamalar; kullanım zorluğu, tekli programlama sağlaması ve sadece 610 kb'lik bellek kullanabilmesidir. Bu da büyük bilgisayarla da bilgi alış-verişini zorlaştırmaktadır. Bu sınırlamaları ortadan kaldırabilmek için Os2 işletim sistemi geliştirilmiştir.

4- Unix: Çok kullanıcılı, taşınabilir ve çoklu programlama olanağı veren bir işletim sistemidir. İlk olarak 1971 yılında AT&T firmasında yazıldı. Daha sonra bu program geliştirilerek taşınabilirlik özelliği kazandı. Günümüzde yaygın olarak kullanılmaktadır. 5- Dos: (Disk Operating System) Tek kullanıcılı olan bu işletim sistemi, çoklu programlama olanağı ortamı sağlayamadığından kişisel bilgisayarlarda kullanılmaktadır. Çok kullanıcılı ortamlarda tercih edilmemektedir. 6- Mos: (Macintosh Operating System) Macintosh bilgisayarlar için geliştirilen işletim sistemi İBM uyumlu bilgisayarlarda kullanılamaz. Daha çok masa üstü yayıncılık alanlarında tercih edilen ve başarılı olan bir işletim sistemidir. Dosya yönetim ve programlama dillerinin uygulamalarına yanıt vermeyen bir işletim sistemidir.

DOS İŞLETİM SİSTEMİ (Disk Operating system)

Bilgisayarın kullanıcı ve kendi birimleri ile iletişimi sağlayan, programların çalışmalarını denetleyen yazılım olan Dos işletim sistemi olmadan bilgisayarın kullanıcı komutlarına yanıt vermesi olanaksızdır. Bilgisayarı kullanıcının kullanımına hazır duruma getiren sistemdir. Bilgisayarın çalışmasıyla yüklenir. Bu işleme yükleme denir. 1)Dos işletim sistemi yüklü bir bilgisayarın açılması: Dos işletim sisteminin yüklenmesi işlemini gerçekleştirebilmek için öncelikle İBM uyumlu en az 512 kb. Rem belleğe sahip bir bilgisayar sisteminin ve Dos işletim sisteminin dosyalarının yer aldığı bir disket veya sabit diske gereksinim vardır.

2) a) Disketle Dos işletim sisteminin bilgisayara yüklenerek açılması:

1) Disket sürücüsüne, dos işletim sistem dosyalarının bulunduğu disketi takmadan önce bilgisayarın elektrik düğmesi açılır.

2) Disketin hareketli kısmı sola doğru çekilebilir konumdayken ya da disket üstünde bulunan yuvarlak bölümün alta gelecek şekilde ve hareketli kısım karşımıza bakacak şekilde disket sürücüsüne takılır.

3) Kısa bir süre sonra işletim sisteminin belleğe yüklenmesi başlar.

4) Yükleme sırasında sürücüden tıkırtıyı andıran sesler gelecektir.

Ayrıca yükleme sırasında sürücü ışığı yanacaktır.

5) Dos işletim sisteminin yükleme işlemi tamamlandığında bilgisayar bizden yeni tarih girmemizi ya da geçerli olan tarihin onaylanmasını isteyecektir.

6) Ekrana A:\\> komut kabul ifadesi gelecektir. A:\\> ifadesinde geçen karekterlerin anlamları şöyledir: A Disket sürücü adı. : Bu karekteri komutlarımızı yazarken yönlendirme karekteri olarak kullanıyoruz. \\ Bu karekteri ise; sürücü ile dizin adı arasında veya dizin ile dizin arasında ya da dizin ile dosya arasında ayıraç olarak kullanmaktayız. > Bu işaret büyüktür anlamına gelmektedir.

7) Komut kabul ifadesi belirdiğinde dos işletim sistemi yüklenmiş, bilgisayarın birimleriyle iletişim sağlanmış, komutları kabul edilebilir hale gelmiş ve kullanıcıyla bağlantı sağlanmaya hazır demektir. b) Dos işletim sisteminin sabit diskten yüklenmesi: Bilgisayar sabit diskten başlatılacaksa gerekli sistem dosyaları sabit diskte yer aldığında yapılacak tek şey bilgisayarın elektrik düğmesini

açarak işletim sisteminin yüklenmesini beklemektir. Çünkü sabit disketten yükleme yapılıyorsa bilgisayar bizden tarih ve zaman bilgilerini istemeyecektir. Bunun için gerekli toplu işlem dosyaları oluşturulmuş olarak bilgisayarın sabit diskinde vardır. Yükleme işlemi tamamlandıktan sonra C:\\> komut kabul ifadesi belirecektir. Buda bilgisayarımızın kullanıma hazır olduğu anlamına gelir.

KÖK DİZİN:

Bir disket ya da sabit diskte en az bir dizin bulunur. Bunun adı kök dizindir. \\ (ters bölü) işaretiyle gösterilir. Dikkat edilmesi gereken bir

nokta disket ya da sabit diskte bir tane kök dizininin olduğudur. Kök dizininin silinmesi veya açılması mümkün değildir. Bilgisayar açıldığında ana dizin ekrana gelir.

Dizin ya da alt dizin:

Bilgisayar çalışırken, bilgisayar, çalışılan sabit disk veya disketleri bölümlere ayırma işlemlerini yapar. Disk-disketleri bölümlere ayırıp, bu

bölümlere isim verip saklama işlerine dizin oluşturma denir. Oluşturulan

bu alanlar birer kayıt ortamıdır. Bu ortamlara aynı gruplara ait bilgi ve

programları yerleştirmede kullanırız.

Alt Dizin:

Alt dizin, kök dizininde açılan dizin içinde kullanıcı tarafından açılan

dizinlerdir. Ana dizinin altında bulunan tüm dizinler alt dizin olarak

adlandırıldığı gibi, alt dizinler içinde açılan dizinlere de alt dizin denir.

Dosya isimlendirme kuralları:

Dosya aynı özelliklere sahip veri gruplarının yer aldığı ve belleklerde

saklanabilen bilgilere denir. Dosyaya, Dos işletim sisteminde

kütük de denilmektedir. Dos işletim sisteminde dosya (file) olarak yer

alır.

Dosyaları isimlendirme kuralları şunlardır:

1) Dosya adı en fazla 8 en az 1 karekter olabilir.

2) Dosya adından sonra nokta konarak dosyanın niteliğine göre

uzantı konmalıdır. Uzantı konurken, dosya uzantısının en fazla 3 karekteri aşmaması gerekmektedir.

3) Dosya adı verilirken: Nokta, apostrof, ters-bölü, bölü, noktalı virgül, artı, eşittir, parantez, büyüktür-küçüktür işareti, virgül, soru işareti, yıldız gibi karekterler kullanılmaz.

4) Dosya adı verilirken karekterler arasında boşluk bırakılmaz.

5) Dosya adı ile uzantı arasındaki nokta işareti yazılırken boşluk bırakılmaz.

6) Dosya adı verilirken tire işareti, dosya adının başında ve sonunda

kullanılmaz. (Tire işareti, dosya isminin ortasında kullanılabilir.)

7) Dosya adı verilirken harf ve rakam karekterler birlikte kullanılabileceği gibi sadece harf, sadece rakam karekterlerinden dosya adları oluşabilir.

Dosya Uzantısı ve Tipleri:

Dosya uzantılarına göre dosyaların özellikleri anlaşılabilir. Dosya uzantısı dos işletim sisteminde en fazla 3 karekter olarak verilir. Dosyalar uzantılarına göre şöyledir:

Hemen çalışabilir dosyalar. Bunların uzantısı com, exe, bat olabilir. Veri dosyaları, bilgi dosyaları, yardım dosyaları gibi farklı dosyalar vardır. Dosya uzantıları hem alfabetik karekter hem de sayısal

karekterler veya bunların karmasından oluşabilir.

Uzantılarına göre dosya tipleri:

--.bat Toplu işlem dosyası. Komutlardan oluşmaktadır.

--.bak Yedeklenmiş dosyadır.

--.pas Paskal programlama dili ile yazılmış kaynak dosya.

--.dat Bu tür dosyalar veri dosyalarıdır.

--.com Bu tür uzantısı olan dosyalar çalıştırılabilir dosyalardır.

--.exe Bu tür dosyalar çalıştırılabilir dosyalardır.

--.sys Bu dosyalar işletim sisteminin kaynak dosyalarıdır.

Çalışabilir Dosyalar:

Çalışabilir dosyalar uzantılarından anlaşılan dosyalardır. Bu dosyalar belirli bir programın çalışmasını sağlayan ve genellikle program ismiyle anılan dosyalardır. Örneğin, Pw programını çalıştıran çalışabilir dosya pw.com dosyasıdır. Bu dosyalar hemen çalışan dosyalardır. Bunlar bat, exe, com uzantılı dosyalardır. Bu dosyaların çalışabilmesi için sadece isimlerini yazmak yeterli olacaktır.

DOS İŞLETİM SİSTEMİNİN AÇILIŞ AŞAMALARI:

Dos işletim sisteminin bilgisayara yüklenmesi (boot) olarak tanımlanır. Bilgisayar açıldığında aşağıdaki işlemler gerçekleşir:

a) İlk olarak rom'da bulunan bios programı çalışır. Bu program bilgisayarın parçalarını kontrol eder. Çalışmayan veya eksik olan parçalar varsa, bunları çeşitli şekillerde uyarı mesajı ile kullanıcıya bildirir.

b) Bilgisayar, disket sürücüsünde disket olup olmadığını araştırır. Eğer

varsa 2 sistem dosyasını İo.sys ve Dos.sys dosyalarını yükler. Eğer disket sürücüsünde disket yoksa aynı işlemleri sabit diskten tekrarlar.

c) Yukarıda yüklenen dosyalar çalıştıktan sonra Command.com adlı

dosyayı bularak çalıştırır. Bu dosyada işletim sisteminin içsel komutları vardır. Bu dosyanın çalışmasıyla işletim sisteminin bir kopyası Ram'e yüklenmiş olur.

Ç) Io.sys, Dos.sys ve Command.com dosyaları belleğe yüklendikten

sonra bilgisayarın açılışta yapması gerekli düzenlemeler için config.sys

ve bazı programları açılışta yükleyen Autoexec.bat toplu işlem dosyası

çalıştırılır.

d) Dos işletim sistemi yüklenmiştir.

e) Ekranda C:\\> komut kabul ifadesi görüntülenir. Eğer bilgisayar disketten açılış yapılmışsa A:\\> komut kabul ifadesi ekranda görülür.

DOS İŞLETİM SİSTEMİ SİSTEM DOSYALARI:

Dos işletim sistemini sabit diskten veya disketten başlatabilmek için sistem dosyalarına gereksinim duyulur.

Bu dosyalar: İo.sys, dos.sys, command.com dosyalarıdır.

Bu dosyalar bulunması gereken dosyalardır. Bunların dışında programın diğer üniteleriyle ilgili tanımlar içeren config.sys ve autoexec.bat dosyalarıdır.

a)Io.sys: Sistem dosyasıdır. Bilgisayarın ilk açılışında belleğe yüklenir ve sistemi yönetmeye başlar. Bu dosya bilgisayar açık kaldığı sürece bellekte kalır. İo.sys sistem dosyası Copy komutuyla kopyalanamaz. Del komutuyla silinemez. İo.sys dosyası disk veya diskette formatlama sırasında /s parametresi kullanılarak veya sys komutu kullanılarak transfer edilir. Bu dosya eksik olduğunda işletim sistemi yüklenemez. Sabit diske yüklü ve yalnız okunabilir olarak yüklenir. b)Dos.sys: Sistem dosyasıdır. Bilgisayar açılışında belleğe yüklenir. İo.sys ile birlikte sistemi yönetir. Bu dosyada bellek açık kaldıkça bellekte kalır. İo.sys dosyası için geçerli kurallar dos.sys dosyası içinde geçerlidir.

c)Command.com: Msdos'a ait bir sistem dosyasıdır.

Bilgisayarın açılışında İo.sys, Dos.sys ve command.com dosyaları belleğe yüklenerek sistemi yönetmeye başlar. Command.com komut yorumlayıcı

bir dosyadır. İşletim sisteminin komutları bu dosyanın içindedir. Bu dosya bilgisayar için zorunlu dosyalardan biridir.

Ç) Autoexec.bat: Bilgisayar açılırken disket veya diskten İo.sys ve

Dos.sys dosyalarını belleğe okur. Daha sonra açma programlarının

bulunduğu disket ve diskin ana-dizininde config.sys dosyaları araştırılır.

Config.sys dosyası ana-dizininde varsa bu dosyada yazılı olan bir takım

ayarlamaları yapar. Daha sonra command.com dosyasını belleğe yükler.

Bu dosyanın yüklenmesiyle birlikte bilgisayar denetimi command.com

dosyasına geçer. Command.com ilk olarak bilgisayarın ilk açıldığı

ortamda autoexec.bat dosyasını arar. Bu dosya bulunursa bu dosyada yer

alan gerekli işlemleri yapar. Eğer dosya bulunmazsa bilgisayar günün

tarih ve saat bilgilerini ister. Autoexec.bat dosyasının önemi bilgisayar

her açıldığında yapılması gereken tanımlar ve değişiklikleri uygulamasıdır. Autoexec.bat dosyası bulunduğu dizinin kök dizininde

bulunmalıdır. Çünkü bu dosya özel bir toplu işlem dosyasıdır. Bilgisayar

açılış sırasında bu dosyayı kök dizininde arar.

d) Config.sys: Bu dosya sistemin donanım özelliklerini değiştirmemize

olanak verir. Özel komutlar kullanarak, sisteme kurulacak sürücüleri

ilave eder. Bu dosyanın sürücünün ana dizininde bulunması gerekir.

Dosya bilgisayarın açılışı esnasında 3 aşamada okunur. Dosya üzerindeki değişiklikler bilgisayar açılırken sistem tarafından yerine getirilecektir.

İÇsel VE Dışsal KOMUT KAVRAMLARI:

Dos işletim sistemi komutları, kullanıcı ile bilgisayar arasında iletişim sağlar. Bu iletişimde rol oynayan unsur, kullanıcının bilgisayarın anlayacağı dilden komutlar vermesidir. Bilgisayarın dos'u yüklemesiyle otomatik olarak belleğe yerleşen komutlara iç komutlar denir. Bunlar bilgisayar açıldıktan sonra kullanıcı tarafından kullanılabilmektedir. Bellekte fazla yer kaplamadıklarından ayrıca bir dosya halinde saklanmamışlardır. Bellekte fazla yer kapladıklarından belleğe yüklenmeyen komutlara dışsal komutlar denir. Bunlar kendi adlarıyla anılır ve hemen çalışabilir dosyalar halindedirler. Dışsal komutların çalıştırılabilmesi için bu komut dosyalarının çalışılan ortamda veya her taraftan çalışabilmeleri için yol tanımları yapılmış olmalıdır.

Joker ve yönlendirme karekterleri:

Dos işletim sistemi dosya adlarının aranması ve belirtilmesi sırasında bazı karekterlerin joker olarak kullanılmasına izin vermektedir. Bu karekterlerin sayesinde dosya isimlerinden hatırlayamadığımız karetkerlerin yerine joker karekterler yazılır. Dos işletim sisteminde kullanılan joker karekterler:

1- ? (soru işareti),

2- \* (yıldız) karekterleridir.

a) ? (soru işareti): Dosya isminde yer alan tek bir karekter yerine geçer. Örneğin: İlk karekterini hatırlayamadığımız bir dosya adını şu şekilde yazabiliriz: ?ıldırım.txt Dos işletim sistemi ilk karekter ne olursa olsun diğer karekterleri aynı olan dosyaları dikkate alacaktır.

b) \* (yıldız): Dosya isminde belirtilmeyen birden fazla karekteri temsil eder. Örneğin: ilk karekterini hatırlayamadığımız veya ismin bütün karekterlerini hatırlayamadığımız zamanlarda ve uzantısı txt (metin dosyası) olan bir dosyayı aradığımızda joker karekterin kullanımı şöyledir: \*.txt ya da ilk karekteri r olan bir txt dosyasını aradığımızda kullanımı şöyledir: r\*.txt Böyle bir durumda dos işletim sistemi uzantısı txt olan bütün dosyaları dikkate alarak bize mevcut olan bütün txt uzantılı dosyaları listeleyecektir.

c) Yönlendirme : (iki nokta üst üste) karekteridir. İki nokta üstÜste karekteri çalışılan ortamların değiştirilmesine veya seçilmesi işleminde sürücü harfinden sonra yazılarak işlemleri o sürücüye yönlendirir. Örneğin: A:\\> sürücüsünden C sürücüsüne geçmekiçin C: yazılarak enter (giriş ya da onay) tuşuna bastığımızda çalışılan sürücü değişecektir. Komut kabul ifadesi C:\\> olarak değişecektir.

İŞLETİM SİSTEMİ KOMUTLARI:

İçsel Komutlar: (İnternal)

Cls: (Ekran temizleme)

Dos ekranında çalışırken daha önceki yazılan komutların ekrandan silinmesi için kullanılan komutur. Dos komutlarının tam olarak uygulanabilmesi için komut kabul satırının temiz olması yani yanlış yazılmış karekterlerin temizlenmiş ya da silinmiş olmalıdır. Cls komutunun kullanımı şu şekildedir: C:\\> Cls enter bas. Dir: (Dizin ve dosya adlarını görüntüleme) Çalışılan disk veya diskette kayıtlı bulunan dizin ve dosyaların ad, uzantı, kapladıkları alan, oluşturuldukları tarih, oluşturuldukları saat bilgilerini isteyen komuttur. Yalnız başına kullanıldığında çalışılan disk veya diskette kayıtlı bulunan dizin ve dosyaların ad, uzantı, kapladıkları alan, oluşturuldukları tarih, oluşturuldukları saat bilgilerini listeler. Ayrıca sürücünün adını, seri numarasını ve çalışılan dizinin adını ekranda görüntüler.

Dir komutunun Anahtarları:

a) / (bölü) P

Bu anahtar dir/p şeklinde kullanılır. Bu anahtarın görevi, bulunduğumuz sürücü veya dizin içindeki dosya ve dizin isimlerini sayfa sayfa olarak göstermektir. Dosya ve dizin isimleri ekrana sığmadığı aman sayfa sayfa olarak gösterilir. Sayfa sayfa gösterim esnasında kran durur ve bir sonraki sayfaya geçmeniz için herhangi bir tuşa basmanızı bekler.

b) /w Bu anahtar dosya ve dizin isimlerini sütunlar halinde ekrana listeler. Ekrana sığmadığında yukarı doğru kaydırarak diğer dizin ve dosya isimlerini sütunlayarak listelemeye devam eder. c) /a Bu anahtar dosya ve dizinlerin niteliklerini gösterir. Görmek istediğimiz niteliğe göre a harfinin yanına bazı harfler gelmektedir. Bunlar şöyledir: Gizli dosyalar için dir/ah, sistem dosyaları için dir/as, dizinler için dir/ad, sadece okunabilir dosyaları görebilmek için dir/ar, arşiv dosyalarını göstermesi için dir/aa, gizli özelliği olmayan dosyaları gösteren dir/a-h, sadece dosya isimlerini görüntüleyebilmek için dir/a-d, arşiv özelliği olmayan dosyaları görüntüleyebilmek için dir/a-a, hem okunur hem de yazılabilir dosyaları görüntüleyebilmek için dir/a-r, sistem dosyası özelliği olmayan dosyaları görüntüleyebilmek için dir/a-s. ç) /o Bu anahtar dosya veya dizin isimlerini sıralamada kullanılır.

1- /on: Dosyaları adına göre A'dan Z'ye doğru sıralar.

2- /oe: Dosyaları uzantılarına göre A'dan Z'ye doğru sıralar.

3- /os: Dosyaları kapladıklara alanlara göre küçükten büyüğe doğru sıralar.

4- /od: Dosyaları bilgisayara kayıt tarihlerine göre küçükten büyüğe doğru sıralar.

d) /s Bu anahtar bulunduğumuz sürücü veya dizin içindeki diğer alt

dizin ve dosyaları görüntülemeye yarar. Nerede bulunuyorsak oradan itibaren bütün dizin ve dosyaları görüntüler. e) /b Bu anahtar sadece dosya ve dizin isimlerini görüntüler. Dosya ve dizinlere ait olan diğer bilgileri göstermez. f) /l Bu anahtar dosya ve dizin isimlerini ekrana küçük harflerle yazarak listeler.

Verify:

Yan bellek birimi üzerine yazılacak bilgilerin doğru olarak kayıt edilip edilmediğini kontrol eder. Bu komut bir anahtar komuttur. Eğer komutla birlikle On ifadesi kullanılırsa komutun işlevi aktif, Off ifadesi kullanılırsa komut işlevini pasif duruma getirir. Kullanımı: Verify on veya off enter

Copy:

Bir veya birden fazla dosyayı belirtilen yani gösterilen adrese kopyalar.

Bu işlemin yapılması anında kopyalama yapılan ortamda aynı isimden

dosya varsa yeni dosyanın burada bulunan dosyanın üzerine yazılıp yazılmayacağını uyaran bir mesaj alınır. Eğer bu mesaja olumlu yanıt verirsek yeni dosya burada bulunan dosyanın üzerine kopyalanır. Yanıtımız olumsuz olursa kopyalama işlemi iptal olur. Kullanımı:

1- Öncelikle komutumuzu yazarız ve boşluk tuşuna basarız.

2- Copy Kopyası çıkarılacak dosyanın dizinin bağlı olduğu sürücü adı ve yönlendirme karekteri iki nokta üstüste ve ayıraç karekteri ters-bölü karekterini koyarız.

3- Dosyanın bağlı olduğu dizin adı.

4- Kopyası alınacak dosya adı ve uzantısı,

5- Dosyanın kopyalanacağı hedef sürücü adı,

6- Hedef dizin adı.

Bu komutu uygularken pratik bir anımsama ise şöyledir: neyi nereye kopyalayacağımdır. Bu durumu ayrıntılı bir örnekle şöyle gösterelim: Kök dizininde bulunan yunus adlı dizinindeki Emre.txt dosyasını A sürücüsündeki bahar dizinine kopyalayalım. İzleyeceğimiz yol ise şöyledir: Copy C:\\yunus\\emre.txt A:\\bahar\\emre.txt enter Eğer dosya ismini aynen koruyacaksak yeniden emre.txt yazmaya gerek yoktur. ancak dosya ismini değiştireceksek A:\\bahar\\ bölümünü yazdıktan sonra yeni isim ve uzantıyı doğru olarak yazarak enter tuşuna basmalıyız. Bu işlem doğru olarak yapıldıktan sonra bir dosya kopyalandı diye bir mesaj

alacağızdır. (1 File(s) copied.)

Copy komutuyla aynı sürücü veya aynı dizin içinde bulunan bir dosyanın ismini değiştirerek niteliği aynı bir ikinci dosyayı oluşturabiliriz. Bunun için yapacağımız işlem şudur:

1- Komut yazılır: Copy 2- Örneği çıkarılacak dosyanın adı: Aziz.txt 3- Dosyanın yeni adı: Emre.txt enter tuşuna basılır. Başka bir değişle C sürücüsünde bulunan Okul adlı dizinin içinde bulunan Aziz .txt dosyasından bir adet daha çıkartmamız gerekiyor. Bunu şu işlemle de yapabiliriz: Copy C:\\okul\\aziz.txt C:\\okul\\emre.txt enter tuşuna bas. Bu işlem bittikten sonra 1 file(s) copied. (1 dosya kopyalandı) şeklinde bir mesaj verecektir. Copy komutuyla yapabildiğimiz diğer bir işlem ise 2 veya daha fazla dosyayı birleştirerek yeni bir dosya oluşturmaktır. Bu işlemle genel olarak metin dosyalarını birleştirme yapabiliriz. Uzantısı bat, txt olan dosyaları birleştirebiliriz. Bu işlemi yaparken hangi dosyaya ek yapılacaksa o dosya sıralamada önce yazılır. Örneğin, Murat ve Mesut bir ödev üstünde çalışsın. Bu ödevin ilk 5 başlığının konularını Murat, diğer 5 başlığa ait konuları da Mesut yazsın. Yazma işlemi bittikten sonra dosyaları birleştirmek için şu işlemi uygulayacağız: Biz okul adlı dizin içinde bulunalım. Copy C:\\okul\\murat.txt+mesut.txt odev.txt enter tuşuna bas. Burada önce yazının ilk kısmını yazan Murat.txt önce yazıldı ve + (+ Bu işaret artı karekteridir.) işareti koyduk. Daha sonra Mesut.txt dosyasını hiç aralık vermeden artı işaretinden sonra yazdık. Boşluk tuşuna bastıktan sonra bu iki dosyanın birleşiminden ortaya çıkacak olan yeni dosyanın adını ve uzantısını yazdık. Bu işlemleri yaptıktan sonra elimizde yeni bir dosya oluşmuş olur.

Copy con:

Bu komutun yardımıyla bir satır editörü oluşturabiliyoruz. Bu satır editörüyle kısa metin dosyaları elde edebiliyoruz. Ancak ciddi yazılarımızı burada yazmak çok zor olmaktadır. Bu programda hareket olanağı çok iyi değildir. Bu komuttan daha çok toplu işlem dosyaları gibi kısa mesajlar içeren txt veya bat uzantılı dosyalar elde ederiz.

Kullanımı:

1- Öncelikle komutu yazarak boşluk tuşuna basarız: Copy con

2- Hangi sürücüde dosya oluşturacaksak o sürücünün adını, yönlendirme karekterini, ayıraç karekterini yazarız.

3- Hiç aralık vermeden dizin adını yazarız.

4- Hiç aralık vermeden ayıraç karekterini yazarız.

5- Yeni oluşacak dosya adı ve uzantısını yazarız. 6- son olarak enter tuşuna basarız. 7- Yazı yazma işlemimiz sona erdikten sonra F6 tuşuna basarız. Biz dosya adını daha önceden yazdığımız için sadece enter tuşuna basarız.

Örnek: C sürücüsünde bulunan belgeler adlı dizinde kullanım.txt adında bir programın hızlı kullanımını anlatan bir metin dosyası oluşturalım. Bunun için izleyeceğimiz yol şöyledir:

Copy con C:\\belgeler\\kullanım.txt enter Bu komutu yazdıktan sonra kullandığımız ekran okuma programından herhangi bir geri bildirim alamayız. Ancak ekran okuma programının satır okutma tuşuna bastığımızda blank (boşluk) diyecektir. Artık satır editörü açılmış olur. Metinimizi yazarken satırın sonuna kadar beklenmez. Kısa satırlardan oluşan yazımızı yazma işlemi bittikten sonra bu dosyamızı disk-diskete kayıtetmemiz gerekmektedir. Bunun için öncelikle fonksiyontuşlarından f6 tuşuna basarız. Program burada bizden dosya ismini girmemizi beklemektedir. Ancak biz dosya ismini komutu ilk çalıştırdığımız anda verdiğimiz için bu bölümü enter tuşuna basarak geçeriz. Enter tuşuna bastıktan sonra "1 file(s) copied" şeklinde bir mesaj gelecektir. Böylece dosyamız kopyalanmış olacaktır.

Del Silmek (delete):

Bu komutu kullanarak disketten veya diskten istenen dosya veya dosyaları silebiliriz. Bu komutla dosyalar tam anlamıyla disk ve disketten silinmiş olmazlar. Dosya veya dosyaların kayıtlı oldukları alanların serbestçe kullanılabileceği anlamına gelir. Ancak yeni bir dosya yazıldığında ilk olarak serbest kalan bu alanlar üzerine yazılır. Böylece önceden Del komutuyla sildiğimiz dosyalar tam olarak silinir. Eğer sildiğimiz dosyaları kurtarmak istiyorsak bu bölümde yeni dosya yazdırmamış olmamız gerekiyor. Diğer önemli bir kuralda sildiğimiz dosyaların bağlı oldukları dizinin silinmemiş olması gerekiyor ya da dizinle birlikte dosyaların silinmemiş olması gerekiyor. Bu komutun kullanımı: Del sürücü adı, dizin adı, dosya adı ve uzantısı enter. Eğer silmek istediğimiz dosya ve dosyaların bizim onayımızı aldıktan sonra silinmesini istiyorsak: Del sürücü adı, dizin adı, dosya adı ve uzantısı /p enter.

Örnek: A sürücüsünde bulunan Davullar.txt dosyasını silmek istiyoruz.

Bunun için şu yolu izleyeceğiz: Del A:\\davullar.txt enter tuşuna bas. Ya da bu silme işlemini yaparken kullanıcının onayını aldıktan sonra yapsın.

Bunun için izleyeceğimiz yol: Del A:\\davullar.txt /p enter'a bas. Bu komutu girdikten sonra ekranda davullar.txt dosyasını silmek istiyormusunuz şeklinde bir mesaj belirecektir. Sizden Evet ya da hayır tuşuna basmanızı yani evet için Eğer kullandığınız Dos işletim sistemi Türkçe ise E tuşu, Eğer İngilizce ise Y tuşuna basılır. Hayır seçeneğini seçecekseniz Türkçe için H tuşu, İngilizce ise N tuşuna basılır. Del komutuyla birlikte joker karekterler kullanılabilir. Eğer Del \*.\* komutu verilirse çalışılan dizindeki tüm dosyaların silineceğini belirten bir uyarı mesajı belirir. Size uygun seçenek seçildikten sonra işlem tamamlanır. Dikkat: Bu komutu kullanırken çok dikkatli olunması gerekmektedir. Özellikle joker karekterler kullanarak dosyaları toplu silebiliriz. Bu karekterleri kullanırken çok dikkatli olmamız gerekmektedir. Ren: (Dosyaları yeniden adlandırma. ) Dosya adlarını değiştirmekte kullandığımız komuttur. Rename (yeniden adlandırma) anlamına gelir. Kullanımı:

1- Öncelikle komut yazılır:

2- Ren boşluk verilir,

3- Adı değişecek dosya adı ve uzantısı yazılır, 4- Boşluk tuşuna basılır, 5- Dosyanın yeni adı ve uzantısı yazılır, 6- enter tuşuna basılır. Örnek: Ren

Salih.txt Veli.txt enter. Eğer bilgisayardan herhangi bir hata mesajı

almadıysak yaptığımız işlem doğru olmuştur anlamına gelir. Ancak eğer değiştirme işlemi sırasında dosya adı ve uzantısını yanlış olarak yazmış olsak dahi bu işlem gerçekleşir. Çünkü bu komut yazdığınız ad veuzantının ne olduğuna bakmaz sadece yaptığınız işlemin kurallarına uygun olup olmadığına bakar.

Md: (Make Directory)

Çalışan sürücü veya belirtilen sürücüde dizin oluşturan komuttur. Kullanımı: Md Sürücü adı, dizin adı enter. Eğer sürücü adı vermeden yani yol tanımı yapmadan bu komut uygulanırsa çalışılan sürücü veya dizine verilen adla yeni bir dizin oluşturulur. Dizinler oluşturulurken dikkat edilmesi gereken kurallar dosyalara isim verirken geçerli olan kurallarla aynıdır. Dizinler bulundukları dizinlerin alt dizinleri olarak açılır. Aynı dizin içine birden fazla dizin açabileceğimiz gibi alt dizinler içinde de dizinler açabiliriz. Örnekler: Çalıştığımız sürücü C olsun. Md C:\\okul enter. Bu dizin C sürücüsünde oluşur. Bu dizin içinde sınıf adında bir dizin daha oluşturabiliriz. Bunun içinde: Md C:\\okul\\sınıf enter. Sınıf dizinimiz C sürücüsündeki okul dizininin içinde oluşmuş olacaktır. Eğer istersek okul dizininin içindeki sınıf dizininin içine de bir veya birden fazla dizin oluşturabiliriz. Bunun içinde: Md C:\\okul\\sınıf\\ders enter. Böylece C sürücüsünde bulunan okul dizininin içindeki sınıf dizinine ders adında bir dizin daha oluşturmuş oluruz.

Dizin oluştururken dizin oluşturacağımız sürücü veya dizin içinde olmamız gerekmiyor. Eğer yol tanımını doğru olarak yaparsak istediğimiz sürücü veya dizin içine yeni dizin veya dizinler oluşturabiliriz. Örnek: Biz C sürücüsünde ve okul adlı dizin içindeyiz. A sürücüsünde yeni bir dizin oluşturacağız. Bunun için izleyeceğimiz yol: Md A:\\dernek enter. Böylece biz C sürücüsündeyken A sürücüsünde bir dizin oluşturmuş oluruz. Aynı yolla oluşturduğumuz dizinin içine alt dizinlerde oluşturabiliriz.

Cd: (Change Directory)

Bu komut var olan dizinler içine girmeyi ve dizinler arasında hareket

etmeyi sağlar. Kullanımı: Cd sürücü adı hedef dizin adı enter. Bu komutu kullanabilmek için yazdığımız dizinin bilgisayarımızda oluşturulmuş olması gerekiyor. Eğer dizin adını yanlış yazmışsak ya da o dizin bilgisayarda bulunmuyorsa bize "geçersiz dizin" şeklinde bir mesaj gelecektir. Eğer komutu doğru olarak uygularsak: Cd C:\\okul enter. Doğru olarak işlemi gerçekleştirdiğimizde C:\\okul> şeklinde komut kabul ifadesi ekranda görülecektir. Okul adlı dizinin içindeyizdir anlamına gelir. Eğer sınıf adındaki dizinin içine girmek istiyorsak: Cd sınıf enter. İşlemin doğru olup olmadığı bilgisayarın bize vereceği mesaj veya komut kabul ifadesinden anlaşılır. Eğer dizinden çıkmak istiyorsak cd.. şeklinde komut kullanılır. Bu işlemi yaptığımızda bulunduğumuz dizinden bir önceki dizine geliriz. Örneğin biz C:\\okul\\sınıf\\ders dizinleri içinde bulunalım. Bu komutu kullandığımızda yani cd.. enter Bulunduğumuz ders dizininden sınıf dizinine geliriz. Eğer bulunduğumuz alt dizinlerden veya dizinden doğrudan kök dizine dönmek istiyorsak bu kez cd\\ komutunu kullanırız. ( \\ işareti ters bölü yani back slash anlamına gelmektedir.)

Rd: (Remove Directory)

Bir dizini veya alt dizini silmek için kullanılır. Bu komut ile içi boş olan

ve içinde olmadığımız dizinler silinir. Bu komutla sadece dizinler silinir. Dikkat edilmesi gereken silinecek dizinin içerisinde herhangi bir dosya ve dizin olmaması gerekir. Ayrıca sileceğimiz dizinin içinde olmamamız gerekmektedir. Kullanımı: Rd sürücü adı dizin adı enter. Örnek: Rd C:\\okul\\sınıf enter. Burada okul dizini içinde bulunan sınıf dizinini silmiş

oluyoruz. Diğer dos komutlarında olduğu gibi işlemlerimizi yaparken yol

tanımına çok dikkat etmemiz gerekir. Eğer Rd komutu kullanılarak bir izin silinmek isteniyor ancak bize hata mesajı veriyorsa yapmamız gereken şey, dizinin içerisini kontrol etmek veya dizin ismini doğru olarak yazıp yazmadığımızı kontrol etmektir.

Ver: (Versiyon)

Kullandığımız Msdos işletim sisteminin uyarlama numarasını görüntüler. Amaç işletim sisteminin versiyon numarasını öğrenmektir.

Kullanımı: Ver enter Örnek: Ver enter Görüntü: Msdos version 6.22.

Type:

Dosyaların içeriğini görüntülemeye sahiptir. Bu komut yardımıyla ascii

içerikli dosyaların içeriğini görüntüleyebiliriz. Eğer ascii kotlarıyla kotlanmamış dosyaların içeriklerini görüntülemeye çalışırsak ekrana okunamayacak karekterler şeklinde gelir.

Kullanımı:

1- Komut adı: Type 2- Boşluktan sonra sürücü adı, yönlendirme karekteri, ayıraç karekteri,

3- Hiç aralık vermeden Dizin Adı 4- Hiç aralık vermeden Dosya adı ve uzantısı 5- Hiç aralık vermeden enter tuşuna bas. Örnek: Type C:\\okul\\odev.txt enter

Böylece odev adlı dosyanın içerisindeki yazıların ne olduğunu okuyabiliriz. Burada unutulmaması gereken, bu komutla sadece dosyaların içeriğini görüntüleyebiliriz, herhangi bir şekilde dosyanın içeriğine müdahale edemeyiz. Örneğin hayat.txt dosyasının içeriğini görelim: Type hayat.txt enter. Bu işlemi yaptıktan sonra Ascii kodlarıyla

yazılmış dosyamızın içeriği karşımıza gelir: "Hayat bir çok zorluklarla doludur. Bu zorluklarla kimimiz mücadele eder, kimimiz de mücadeleden kaçarız. Ya da bazılarının yaptıkları gibi kendi beynimizi tatile gönderir başkalarının beyni ile yaşamayı tercih ederiz. Burada önemli olan birisinin veya birilerinin dayattıkları değil biz ne istiyoruz olmalıdır...."

More:

Type komutuyla dosyaların içeriklerini görüntüleme esnasında eğer azı

ekranı taşıyorsa More komutunu Type komutuyla birlikte kullanırız. More komutu görüntülenen dosyayı ekran ekran bize gösterecektir. Yani

eğer dosyamız dos işletim sisteminin bize tanıdığı ekran boşluğunu dolduruyor ve taşıyorsa More komutunun yardımıyla dosyayı bölüm bölüm ekranda görüntüleyebiliriz. Kullanımı: Type hayat.txt bibar işareti more enter Bu komutu kullanırken more yazmadan önce bibar olarak söylenen işaret konur. Bu işareti iki yolla elde edebiliriz. Birincisi sağ tarafta bulunan alt tuşuna basarak büyüktür-küçüktür işaretini çıkarttığımız tuşlara birlikte basarak elde edebiliriz. İkincisi ise Ascii kodunu yazarak elde edebiliriz. Bunun için numlock tuşunun on konumunda olması gerekmektedir. Daha sonra sol tarafta bulunan alt tuşuna elimiz basılıyken numaratörden yararlanarak 124 yazmamız gerekecektir. Böylece bu işareti elde etmiş oluruz.

Path:

Bilindiği gibi çalışabilir dosyalarımız vardı. Bu çalışabilir dosyaların arama yolunu tanımlamakta Path komutu kullanılmaktadır. Amaç: hangi ortam ve dizin olursak olalım istenilen çalışabilir dosyayı çalıştırmaktır. Kullanımı: Path sürücü adı, dizin adı, enter Örnek: Path C:\\Pw enter Sonuç: C sürücüsünde bulunan Pw adlı dizinde bulunan (com, bat, exe) hemen çalışabilir dosyalar kök dizininde adları yazıldığında çalışırlar. Path komutu satırı olmadığında adı geçen dizinlerde bulunan hemen çalışabilir dosyaları çalıştırmak için ilgili dizine girmek ve sonrada dosya adını yazmak gerekecektir. Yol tanımı (path) yapmak her zaman bize zaman kazandıracak ve işlemleri daha çabuk yapabileceğiz. Hemen çalışabilir dosyalara kök dizininden ulaşmak için bu komut genellikle Autoexec.bat toplu işlem dosyasına yazılır. Böylece bilgisayar her açıldığında otomatik olarak komut belleğe yüklenir. Çalışılan sürücüdeki yol tanımını görmek için Path enter komutu uygulanır. Böylece bellekteki yol tanımı ekrana gelir.

Prompt:

Ekranda görülen komut kabul ifadesini değiştiren komuttur. Amaç:

Komut kabul ifadesinde istediğimiz ve gerekli gördüğümüz karekterlerin

görüntülenmesini sağlamaktır. Kullanımı: Prompt yeni ifade dolar işareti. Komuttan sonra yazılan ifade ne olursa olsun ekranda komut kabul ifadesi olarak görülecektir. Değiştirilmediği sürece belleğe yerleşir. Bilgisayar kapanana kadar bellekte yüklü kalır ve etkinliğini korur. Örnek: Prompt Sevgi enter Böylece komut kabul ifadesi değişir.

Sevgi yazısı sürekli ekranda görüntülen C:\\> ifadesinin yerini alır. Değiştirmek için de aynı komut aynı şekilde kullanılır. Yeniden eski görüntüyü elde etmek için Prompt $p$g yazarak enter tuşuna basınız. (Burada $ karekteri Dolar işareti olarak kullanılmıştır.) Görüntü tekrardan C:\\> şekline dönüşecektir.

Prompt komutuyla kullanılabilen karekterler:

a) Ekranda sistem saatinin görüntülenebilmesi için $t şeklinde kullanılır.

b) Günün tarihini görüntüleyebilmek için $d şeklinde kullanılır.

c) Çalışılan sürücü dizini için $p şeklinde kullanılır.

ç) Versiyon numarasını görüntülemek için $v şeklinde kullanılır.

d) Versiyon ve sürücü görüntülemek için $n şeklinde kullanılır.

e) Büyüktür karekterini görüntülemek için $g şeklinde kullanılır.

f) Küçüktür karekterini görüntülemek için $l şeklinde kullanılır.

g) Eşittir karekterini görüntüleyebilmek için $q şeklinde kullanılır.

Vol: (Volume)

Diskete verilen etiket ismini ve format esnasında verilen numarayı ekranda görüntüler. Kullanımı: Vol sürücü adı enter

Date: (Tarih)

Sistem tarihini verir ve değiştirmemizi sağlar. Kullanımı: Date enter

Bu komuttan sonra ekranda şunlar yazacaktır:

Current Date Is Son 14/02/1999

Enter New Date ../../....

Önce gün sonra ay ve yıl yazıldıktan sonra enter tuşuna basarak yeni

tarihi onaylamış oluruz.

Time: (Zaman)

Bu komutu yazarak enter tuşuna bastıktan sonra önce sistem saatini

bize verir. Sonrasında yeni saati girmemizi ister. Kullanımı: Time

Saat:dakika:saniye,silisiye enter

Örnek: Time enter

Current Time Is 10:01:21,56

Enter New Time ..:..:..,..

Bu komutu kullanırken öncelikle 24 saat üzerinden yeni saat bilgisini, 60 dakika üzerinden yeni dakika bilgisini, 60 saniye üzerinden yeni saniye bilgisini ve salisiye bilgisini girdikten sonra enter tuşuna basarız.

Dşsal Komutlar: (External)

Tree:

Bu komutla, sürücüdeki, diskteki, disketteki dizin ve alt dizinler bir ağaç şeması halinde ekranda görülür. Amaç: Belirtilen sürücüdeki dizinleri ve içindeki dosyaları şematik olarak görüntülemektir. Kullanımı: Tree sürücü adı\\dizin adı\\dosya adı/f/a Burada F anahtarı her dizindeki dosyaların isimlerini verir. A anahtarı hızlı bir yazılım sağlayarak kod sayfalarında bulunan grafik karekterlerin kullanılmasını sağlar. Tree komutu yalnız kullanıldığında sadece dizinlerin şemasını görüntüler. Örnek: Tree enter yapıldığında sadece dizinlerin şemasını gösterir.

Deltree:

Bu komut belirtilen dizini ve dizinin içindeki tüm dizinleri silen komuttur. Del komutu yalnızca dosyaları silmekte kullanılırken, deltree komutu ile dizinleri ve dosyaları silebiliriz. Amaç: Dizin ve içindeki dizin ve dosyaları topluca silmektir. Kullanımı: Deltree sürücü adı, dizin adı enter Deltree komutu uygulandığında ekrana silinecek dizin ile ilgili kullanıcıdan onay ister. Çünkü silme işlemi ne olursa olsun her zaman tehlikelidir. Deltree komutu ile dizin ve dizin içinde silinen dosyalar tekrardan kurtarılması mümkün değildir. Örnek: Deltree Yeni enter Bu komutu uyguladıktan sonra ekrana Yeni dizini ve tüm alt dizinleri silinsinmi (E/H) şeklinde bir görüntü gelir. Dizinin silinmesi isteniyorsa E

istenmiyorsa H tuşuna basılarak işlem sonuçlandırılır.

Undelete:

Bu komut, del komutuyla veya deltree komutuyla silinen dosyayı (disk- disketten) yeniden kurtarmaya yarar. Uyarı: Deltree komutuyla eğer dosyayı dizinle birlikte silmiş iseniz kurtarmanız mümkün değildir. Kullanımı: Undelete sürücü adı, dizin adı, dosya adı enter Bir dosya silindiğinde hiç bir yazma veya sürücüden okuma işlemi yapmadan hemen undelete komutu kullanılmalıdır. Aksi taktirde dosyanın tam olarak kurtarılması mümkün olmayabilir. Örnek: Undelete C:\\okul\\yazı.txt enter Bu dizindeki daha önce silinmiş dosya varsa arayarak bunlar kurtarılacaktır. Del komutuyla silme işleminde

dosyaların adının yalnızca ilk karekterleri silinir. Undelete bu dosyaları bularak kurtarır. Komut verildikten sonra ekranda silinen dosyanın ilk karekterinin yerine ? (soru işareti) karekteri gelerek dosyanın geri kalan

kısmı görüntülenir. Daha sonra bu dosyayı kurtarmak isteyip istemediğimiz sorulur. Kurtarılacak bir dosya ise Y (yes) değilse N (no) seçeneği girilir. Y seçeneği girildiğinde bizden kurtarılacak dosyanın ilk karekterini yazmamız istenmektedir. İlk karekteri yazdıktan sonra "dosya kurtarma işlemi başarıyla tamamlandı." Şeklinde bir mesaj gelecektir. Eğer undelete komutunu bütün dosyaları kurtarmak için kullanmışsak dosyalar teker teker kurtarılacak ve her dosyanın kurtarılması esnasında kullanıcıdan onay istenecektir. Tercih edilen (Yes ya

da No) seçeneğe göre işlem yapılır.

Sys: (System)

Msdos işletim sistemi sürekli geliştirilmekte ve yenilenmektedir. Kullanılan Dos işletim sisteminin eskimesi nedeniyle yenileşmek, güncelleşmek isteyebiliriz. Yeni versiyon işletim sisteminin dosyalarını bilgisayara yüklenmesini sağlayan komuttur. Kullanımı: Sys sürücü adı enter Bu komutla Sys uzantılı sistem dosyaları ve command.com dosyaları bilgisayara yüklenir. Sistem dosyaları özel dosyalar olduklarından kopyalama komutlarıyla bilgisayara yüklenmezler. Sys komutuyla sistem disketleri oluşturulabilir.

Diskcopy:

Bir diskette bulunan dosyaların tamamı başka bir diskete kopyalamak için kullanılır. Diskcopy yapılacak disketlerin kapasiteleri aynı olmalıdır. Eğer diskcopy yapacağımız disket formatlı değilse diskcopy komutu bu

işlemide yaparak disketi kopyalama işlemini tamamlar. Amaç: Disketleri bire bir kopyalamaktır. Kısacası disketin fotokopisini çıkarmaktır. Kullanımı: Diskcopy sürücü adı sürücü adı enter Burada dikkat edilmesi gereken durum, eğer bilgisayarınızda ikinci disket sürücünüz yoksa komuttan sonra sürücü adları yerine A: A: ifadeleri gelmelidir. İkinci sürücünüz varsa bukez komuttan sonra A: B: ifadeleri yazılır. Ancak artık ikinci disket sürücü kullanılmamakta olduğundan biz komuttan sonra A: A: yazarak enter tuşuna basacağız. Bu komut sadece disketleri bire bir kopyalamaya yarar. Sabit diskler disketlere kopyalanamaz.

Bir program ya da metin disketinin bir örneğini çıkartmak istediğimizde şu yolu izleyeceğiz: Öncelikle program disketini disket sürücüye yerleştireceğiz. Daha sonra Diskcopy A: A: yazarak enter tuşuna basacağız.

"Kaynak disketi yerleştirin devam etmek için bir tuşa basın" şeklinde mesaj gelecektir. Kaynak disketi sürücüye yerleştirdikten sonra herhangi bir tuşa basılır. Bilgisayar tarafından disket okunarak belleğe alınır. Okuma işleminden sonra ekrana aşağıdaki mesaj gelir. "A sürücüsüne hedef disketi yerleştirin. Devam etmek için bir tuşa basın. "Kaynak disketi çıkararak, boş disketimizi A sürücüsüne yerleştirdikten sonra herhangi bir tuşa basarız. Belleğe okunan bilgiler diskete yazılmaya başlayacaktır. Bu işlem bittikten sonra "kopyalanma bitti. Başka kopyalanacak disket var mı (E/N) " şeklinde mesaj gelecektir. Tercih ettiğimiz seçeneğe göre disket kopyalama işlemi tamamlanmış olacaktır.

Xcopy:

Bir disketten bir diskete veya bir diskten bir diske dosya veya dosyaları,

alt dizinleri, bunların içinde bulunan alt dizin ve dosya veya dosyalarla kopyalayan komuttur. Amaç: İstenen sürücüden belirtilen dizin ve alt dizinleri ya da dosya-dosyaları başka bir sürücüye kopyalamaktır. Kullanımı: Xcopy sürücü adı dizin adı dosya adı daha sonra gidecek hedef sürücü dizin ve dosya adı enter Bu komutla en çok kullanılan anahtar /s olmaktadır. Belirtilen dizini tüm alt dizinleriyle ve dosya-dosyalarıyla birlikte kopyalamak için kullanılır. Örnek: Xcopy/s C:\\okul\\\*.\* A:\\okul enter Böylece C:\\okul dizininde bulunan tüm dosya ve alt dizinleri A:\\okul dizininin içine kopyalar.

1- /v: Kopyalama işleminin doğru olup olmadığını kontrol eder.

2- /a: Arşiv nitelikli dosyaları kopyalamakta kullanılır.

3- /e: Boş olan alt dizinlerinde kopyalanmasını sağlar. Dikkat: /e anahtarı /s anahtarı ile kullanılmaz.

4- /p: Kopyalanacak her bir dosya için onay ister.

5- /w: Xcopy kopyalama işlemine başlamadan,

"Press eny key when ready to start copying files" şeklinde bir mesaj gelir. Bu mesajda Kopyalama işlemini hazır olduğunuzda bir tuşa basarak başlatınız demektedir. Herhangi bir tuşa basmanız durumunda kopyalama işlemi başlayacaktır.

Move:

Bu komuttan, dizinlerin adlarını değiştirmek ve dosyaları bir ortamdan

başka bir ortama taşımak için yararlanmaktayız. Move kelime olarak taşıma anlamına gelir. Dosya taşıma amaçlı kullanımı: Move sürücü adı dizin adı dosya adı bunları yazdıktan sonra gidecek hedef adresin tanımı

yapılarak yani sürücü adı dizin adı dosya adı enter tuşuna bas. Örnek: A sürücüsünde bulunan deneme adlı dizindeki oku.txt adlı dosyayı C sürücüsündeki belgeler adlı dizine taşıyalım. Bunun için şu yolu izlememiz gerekecektir: Move A:\\deneme\\oku.txt

C:\\belgeler\\oku.txt enter bas.

Böylece komut uygulandıktan sonra parantez içinde O.K) yani tamam seçeneği çıkacaktır. Eğer işlem yanlış olmuşsa hata mesajı ekranda belirecektir. Sonuç olarak A sürücüsünde bulunan oku.txt dosyası oradan alınarak C sürücüsündeki belgeler adlı dizine konmuş olur. Move komutuyla dizinlerin adlarını değiştirebilmekteyiz. Kullanımı: Move sürücü adı dizin adı, sürücü adı dizin adı enter bas. Örnek: C sürücüsünde bulunan okul dizininin adını değiştirmek istiyoruz. Bunun için şu yolu izleyeceğiz: Move C:\\okul C:\\dernek enter bas. Böylece okul dizininin adı dernek olarak değişmiştir.

Mem: (Memory)

Bilgisayarın kullanılan ve kullanılmayan boş hafıza miktarının yanısıra, program yerleştirilen ve yerleştirilmeyen yerleri gösterir. Mem komutuyla birlikte /c anahtarı kullanıldığında bellekte yüklü olan programların listesini ve bellekte ne kadar yer kapladıklarını gösterir. Kullanımı: mem enter diğer kullanımı Mem/c enter

Format: (Biçimlendirme)

Yeni alınmış ya da eski bir disketi Dos işletim sisteminde kullanabilmek

için biçimlendirilmesini sağlayan komuttur. Formatlama işlemleriyle disk veya disketler yeniden kullanılabilir hale getirilebilmektedir. Disk-disket

formatlanırken eski bilgiler silinir. Bu nedenle disk-disketleri formatlarken iyi kontrol ettikten sonra komutu uygulamak gerekir. Kullanımı: Format sürücü adı /s/b/v/q/u/c/f: disket kapasite enter

a) /s: Formatlanan diskete Dos işletim sisteminin sistem dosyalarını yükler.

b) /b: Dos sistem dosyalarının daha sonradan yüklenebilmesi için disk-

diskette yer ayırır.

c) /q: Formatlama işlemini hızlı olmasını sağlar.

Ç) /f: Formatlanan disketin kapasitesini bilgisayara girmeye yarar. Eğer formatladığımız disketimiz 720 kb'lık disket ise /f:720 şeklinde yazarız.

Eğer 1.44'lük disketse /f:1440 yazarız.

d) /u: Disketteki tüm bilgilerin silinmesini sağlar. Bilgilerin kurtulması

mümkün değildir.

e) /c: Disket üzerindeki bozuk alanların düzeltilerek formatlanmasını sağlar.

f) /v: Disk veya diskete hacim etiketi verilmesini sağlar.

Formatlama işlemi:

Formatlanacak disket hazırlanır. Format A: yazılır ve enter tuşuna basılır.

Ekrana aşağıdaki mesaj gelecektir: A

sürücüsüne yeni disket yerleştirin ve devam etmek için enter tuşuna basın. Bu mesajdan sonra disket sürücüye yerleştirilir ve enter tuşuna basılır. Formatlama işlemi tamamlandıktan sonra bilgisayar diskete isim vermemizi bekler. (En az 0 en fazla 11 karekter olmalı.) Daha sonra ekrana disketle ilgili bilgiler gelmektedir. Burada disketin kapasitesiyle ilgili bilgilerin yanısıra diskette eğer bozuk alanlar varsa bunlarla ilgili bilgiler de verir. Sonrasında başka formatlanacak disket var mı yok mu şeklinde bir soru ekranda belirir. Tercih edeceğimiz seçeneğe göre işlemimizi sonuçlandırırız. Dikkat: /s ve /b parametreleri birlikte kullanılmaz. Diğer paremetreleri birlikte kullanabilirsiniz.

Unformat:

Önceden biçimlendirilmiş disketin eski haline getirilmesi yani format işleminin geri alınması işlemini gerçekleştirir. Dikkat: Eğer formatlama

işlemi esnasında /u anahtarı kullanılmışsa formatı geri alma işlemi gerçekleşmez. Kullanımı: Unformat sürücü adı /j /u /test/p a) /j: Unformat komutuyla tek başına kullanılır.

b) /u: Miror dosyasını kullanmadan disketi kurtarır.

c) /test: Bilgilerin nasıl kurtarılacağını ve düzenleneceğini gösterir.

Ç) /p: Ekrana gelen mesajları yazıcıdan alır.

Komut uygulandıktan sonra bilgisayar bizden kurtarma işlemini gerçekleştirmek için disketi sürücüye yerleştirmemizi ister ve hazır olduğunuzda enter tuşuna basınız der. Sonrasında çıkacak olan mesajlara Y (yes) seçeneğiyle yanıt verdiğinizde biçimlendirdiğiniz disketteki bilgiler kurtarılacaktır.

Chkdsk: )Disk Kontrol)

Disk ya da disketimizi kontrol etmemizi sağlayan komuttur. Okunmaz ve yazılmaz alanları tespit ederek kullanılır hale getirmeye çalışır. Kullanımı:

Chkdsk Sürücü adı dizin adı, dosya adı /f /v enter /f anahtarı disketteki hatalı alanları belirleyerek temizler ve kullanılabilir hale getirmeye çalışır. /v disketteki hatalı dizin ve dosyaları tesbit eder ve bunlarla ilgili bilgi verir.

Scandisk:

Bu komutun çalıştırdığı program disk-disket analizi yapar ve kontrol eder.

Bozuk alanları bulur ve düzeltilebilecek tüm alanları onarır. Chkdsk komutunun başaramadığı problemlerde kullanılır. Chkdsk komutunu kullandığınızda son kısmında verilen mesajda Scandisk yapmanız önerilmektedir. Kullanımı: Scandisk sürücü adı /all/autofix/surface

a) /all: Gösterdiğimiz sürücüde kurulu tüm dizinleri kontrol eder.

b) /autofix: Tesbit ettiği hataları otomatik olarak onarır.

a) /surface: Yüzey taraması yapar.

Attrib:

Dosyalara özellik veren veya özelliklerini kaldıran komuttur. Aynı zamanda dosyaların özelliklerini görüntülemeye yarar.

Kullanımı: 1- Komut yazılır, boşluğa basılır: Attrib 2- Dosyaya verilecek niteliğe göre eksi veya artı karekterleri yazılır 3- Hiç aralık vermeden eksi-artı karekterinden sonra özellik simgeleri 4- Sürücü adı, yönlendirme karekteri, ayıraç karekteri, 5- Hiç aralık vermeden Dizin adı, ayıraç karekteri, 6- dosya adı ve uzantısı enter

a) +r: Tanımlanan dosyayı yalnız okunabilir özelliği verir. Bu özellik dosyaya verildiğinde dosya ile ilgili işlemlerin yapılması engellenmektedir. Yani disya silinemez, dosya verileri içine herhangi bir veri eklenemez ya da çıkarılamaz.

b) -r: Dosyalara sadece okunabilir özelliğini kaldırmak için kullanılır. c) +a: Dosyaya arşiv özelliği verir. Dosya bu şekildeyken okunabilir, yazılabilir ve silinebilirdir.

Ç) -a: Dosyanın arşiv özelliğini kaldırır.

d) +s: Dosyaya sistem dosyası özelliği verir.

e) -s: dosyanın sistem dosyası özelliğini kaldırır.

f) +h: Dosyayı bulunduğu dizin içerisinde gizler. Normal listeleme

esnasında görülmez. g) -h: Dosyanın gizlilik özelliğini kaldırır.

Ğ) /s: Bu anahtarın kullanılmasıyla alt dizinlerdeki dosyalarıda işleme tutar.

Örnek1: Attrib +r C:\\okul\\\*.txt enter Okul dizini içinde bulunan txt

uzantılı dosyaları sadece okunur

hale dönüştürür. (R harfinden önce kullanılan + karekteri artı karekteridir.)

Örnek2: Attrib +h C:\\sınıf\\B\*.txt enter Burada komut, Sınıf dizini içinde

bulunan B harfi ile başlayan bütün txt

dosyalarını gizler. (B harfinden sonra kullanılan karekter \* yıldız karekteridir.)

Örnek3: Attrib -r -s -h -a C:\\okul\\\*.\* enter Burada komut okul dizini içinde bulunan tüm dosyalara daha önceden verilmiş özellikleri iptal etmektedir.

Label: (Etiketleme)

Disk veya disketin etiket ismini değiştirir ya da oluşturur. Kullanımı:

Label sürücü adı etiket adı enter Burada disket veya disk adı en fazla 11 en az 0 karekter olabilir. Örnek: A sürücüsündeki disketimizin adı yedek 1 olsun. Bunu değiştirmek istediğimizde şu yolu izleyeceğiz: Label A: enter bas. Bu işlemi yaptıktan sonra bilgisayar bize önce eski isimi okuyacaktır. Daha sonra değiştirmek istiyorsak en fazla 11 karekterden oluşan yeni isimi girmemizi ister ya da enter tuşuna tekrar basarak herhangi bir değişiklik yapmadan işlemi sonlandırmamızı ister. Eğer isimi değiştireceksek en fazla 11 karekterden oluşan isimi yazarak enter tuşuna basarız. Bu işlemi şu şekilde de yapabiliriz: Label A: Salih enter bas.

Toplu İşlem Dosyaları: (Batch file)

Çok sık olarak kullanılan komutların biraraya getirilmesiyle oluşturulan dosyaya Toplu İşlem Dosyası denir. Toplu işlem dosyalarının uzantıları Bat olmak zorundadır. Toplu işlem dosyaları Autoexec.bat ve diğerleri olmak üzere ikiye ayrılır. Autoexec.bat dosyası içerisindeki komutlar, bilgisayar açıldığında kendiliğinden uygulanır. Diğer toplu işlem dosyaları ise, isimleri ile çağırılır ve ancak isimleri yazıldığında çalışırlar. Toplu işlem dosyalarının içerisinde Dos komutlarının yanı sıra toplu İşlem Dosyası özel Toplu işlem komutları kullanılır. Toplu işlem dosyalarında kullanılan komutlar ise şunlardır:

1- Echo: Ekrana mesaj gönderir. Kullanımı: Toplu işlem dosyası oluştururken ekranda istediğiniz mesajın görüntülenmesini istediğinizde bu komut kullanılır:

2- Örnek: echo "Program kuruldu"

Echo off: Dosya içerisinde yazdığımız komut satırlarının ekranda görüntülenmesini engeller.

Kullanımı: Görüntülenmesini istemediğimiz komut satırından önceki satırda @ (ed) işaretini satırın başına yazarak hiç aralık vermeden echo off yazarak bir sonraki satıra geçeriz. 3- Echo on: Dosyamızda echo on komutunu kullandığımızda bundan sonraki komut satırları ekranda görüntülenecektir.

4- Pause: Toplu işlem dosyası pause komut satırına geldiğinde klavyeden bir tuşa basana kadar yaptığı işlemi durdurur. Herhangi bir tuşa basmamız halinde işlemine kaldığı yerden devam eder. Şimdi bir toplu işlem dosyası örneği yazalım:

@echo off

cd\\

C:

cd C:\\tiny

ttalk.exe

ttconf load merhaba

cd\\

echo on

"TİNY PROGRAMINIZ HAZIRLANDI"

Yukarıda okuduğunuz toplu işlem dosyasında öncelikle komut satırlarının ekranda görüntülenmemesi için ilk satırı yazdık. Daha sonra kök dizine döndük. Bulunduğumuz kök dizin çalıştırmak istediğimiz kök dizin olmaması olasılığını düşünerek C sürücüsüne bilgisayarı yönlendirdik. Bundan sonra C sürücüsünde bulunan Tiny dizinine gittik. Tiny dizinine girdikten sonra bu programı çalıştıracak olan exe dosyasını çalıştırdık. Arkasından bu programın sağlıklı çalışması için programa ait olan configrasyon dosyasının yüklenmesini sağladık. Program çalıştıktan sonra Tiny dizinini terk ettik ve ekrana programın hazır olduğunu bildiren bir mesaj gönderildi. Sizlerde çok sık kullandığınız komutlardan oluşan toplu işlem dosyaları üreterek zamandan kazanabilirsiniz.

PW PROGRAMI F2 F3 F4 TUŞLARININ ALDIKLARI GÖREVLER (6 . VERİSİYONA AİT TUŞLAR )

F2 ' YE AİT TUŞLAT :

1 : Dosya yükleme ctrl + G

2 : Dosya sakla ctrl + S

3 : Dosya sil

4 : Araya ekle

5 : Yazıcı

6 : Ekranı boşaltma

7 : Tuş tanımlama

F3 2' e AİT TUŞLAR

1 : Satır Ekleme ctrl + I

2 : Kelime Silme ctrl + W

3 : Satır silme ctrl + L

4 : Bloklama ctrl + T

5 : Paste - Yapıştırma ctrl + P

6 : Koyu kelime ctrl + B

7 : Kelime alt çizgi ctrl + U

8 : Çizim

9 : Bul ctlr + F

F4 'e AİT TUŞLAR

1 : Marj ayarı

2 : Üst ve alt yazı

3 : Tab ayarı

4 : Ekran bölme ctrl + N

5 : Çift satır ctrl + D

6 : Satır ortalama ctrl + X

7 : Sola yasla

8 : Sağa yasla

---
*Kaynak: `DOS KOMUTLARI/ekitap-Ibrahim_Elibal-Dos_Komutlari_Isletim_Sistemleri.txt`*
