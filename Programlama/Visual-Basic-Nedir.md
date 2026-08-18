# Visual Basic Nedir

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

VisualBasicNedir?

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Microsoft firması tarafından geliştirilen Visual Basic, atası olan QBASIC derleyicisinin geliştirilmiş ve Windows ortamına uyarlanmış olan sürümü olarak adlandırılabilir. Windows ortamına uyarlandığı için de Nesneye Yönelimli bir dildir. VBX kontrollerini destekleyen ilk dillerden biridir. VBasic'de, 1.0 sürümünden 6.0 sürümüne kadar bir çok yenilik ve değişiklik olmuştur. Bunlardan biri de, arayüzünün güçlü ve etkili bir görünüm kazanmasıdır. Visual Basic, devamlı geliştiği bu süre sonunda yüksek hızlı uygulamalar, OLE serverlar, ActiveX kontrolleri ve daha bir çok şey geliştirilebilecek hale gelmiştir.

Microsoft Windows için program geliştiren programcıların yüzde yirmibeşi Visual Basic'i tercih etmektedirler. Visual Basic'i en popüler programlama dillerinden biri yapan en önemli nedenlerden biri de büyük olasılıkla kolay olmasıdır. Visual Basic de program yazmak için çok fazla teknik bilgiye sahip olmak gerekmez. Sadece kontrolleri form üzerine yerleştirmek ve kodu yazmak yeterli. Kısaca Visual Basic, programcıyı, programın kullanıcıya yansıyan şekli için kod yazmak zorunda bırakmayan bir dildir.

Zamanla Microsoft dışındaki bazı şirketler tarafından benzer programlama dilleri geliştirildi. Muhtemelen bunların en popüleri Borland Delphi'dir.

İşte VBasic'in 5.0 sürümüne eklenen en önemli değişiklik ve yenilikler:

Derlenme işlemci tipine, hızına ve program büyüklüğüne göre optimize ediliyor.

Tekrar tasarlanmış form derleyici

3 Boyutlu grafik desteği

Visual C++’daki gibi sınıf, form ve kontrol "büyücüleri" (wizard)

Otomatik kod tamamlama

Birden çok veritabanı desteği

Animasyonlu GIF’leri destekleyen kontroller

Resim kontrolü JPEG formatını destekliyor

Birden çok kaynak dosyasını destekliyor.

Fonksiyon adresleme

Visual C++ ‘ın 4.x sürümündeki sürükle ve bırak destekli düzenlemeyi destekliyor.

Windows tabanlı ActiveX kontrollerini yaratmak için yeni derleyici

OCX kontrollerini yaratma imkanı !

Ağ üzerinde OLE

Yeni kullanıcı arabirimi ve ActiveX desteği

Birden çok projeyi kontrol edebilen proje penceresi

16 Bit uygulama yaratılamıyor...

Visual C++ Developer Studio tabanlı yeni arabirim

Visual Basic formlarını otomatik olarak HTML sayfasına çevirebilme imkanı

Internet üzerinde bulunabilen TCP/IP kontrollerini tanıyabiliyor

Kullanıcı arabiriminde projenin hiyerarşisini görüntüleyen bir pencere var

Yığın olarak güncellenen geliştirilmiş RDO (Remote Data Objects)

Yazım hatası yaptığınızda o komutu nasıl kullanacağınıza dair ipuçları veriliyor.

Yeni komutlar (Debug.Assert, AddressOf...) ve veri tipleri (Decimal Variant...)

Derleyici artık bir çok derleme opsiyonu sunuyor.

Çok hızlı ve küçük EXE’ler oluşturuluyor!

Degiskenlere Isim Verme Kurallari

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Visual Basic’de daha etkin bir programlama yapabilmek için kullanilan veri tiplerini ve veri yapilarini iyi bir sekilde bilmeliyiz. Burada önemli olan nerede hangi veri tipini kullanacak olusumuzdur. Veri tiplerini anlatmadan önce kullanacagimiz degiskenleri nasil isimlendirecegimizi görelim.

Degiskenleri isimlendirirken daha sonra bakdiginizda akilda kalabilecek ve anlamli bir isim veriniz

Asagida verilen kurallar dogrultusunda degiskenler tanimliyabilmemiz mümkün olmaktadir. Tanimlanacak degiskenlerin ilk karakteri mutlaka bir harf ile baslamalidir. Geri kalan karakterler ; harflerden , rakamlardan, alt çizgi karakterinden olusabilir. Degisken isimlerinde noktalama isaretlerini ,matematiksel ve mantiksal ve karsilastirma operatörleri kullanamayiz. Degisken isimleri 255 karaktere kadar uzunlukta olabilir. Asagida degisken tanimlamalari ile ilgili örnekler verilmistir.

Örnek :

```vbnet
Adi , soyadi , yasi , Maas98 , Dogum_Yeri , SANAT_DALI
```

Yukarida geçerli degisken isimlerine örnek verilmistir

Örnek :

```vbnet
2ADI , ad soyad , Mal+Bildirimi
```

Burada da geçersiz degisken isimlerine örnekler verilmistir.

2ADI : Çünki ilk karakter bir sayi ile baslamis.

Ad soyad : Degisken isminde bosluk kullanilmis

Mal+Bildirimi : Degisken isminde geçersiz bir karakter kullanilmis.

Zaten bu degiskenleri tanimlarken Visual Basic bizi hata mesaji ile uyaracaktir.

Visual Basic’de Degisken Tanimlama

Degisken tanimlarken Visual Basic’te Dim bildiri deyimini kullanabiliriz. Degiskenin tanimlanmasi hafizada ayrilacak hafiza miktarinin belirli olmasini saglar. Eger degiskenlerin tipini belirtmeden bir kullanim yaparsak bu degiskenlerin Variant tipinde oldugu kabul edilir.Bu da hafizada gereksiz yer kaybina sebep olur.Eger tanimlanan bütün degiskenlerin tiplerinin belli olmasini isterseniz kod penceresinin General,Declarations kismina

Option Explicit yazilir.

Ayrica degisken tanimlarken kullanilabilecek bir baska bildiri deyimide Def- bildiri deyimidir.Bu bildiri deyimi daha genel tanimlamalar yapmak için kullanilir..Def bildiri deyimleri asagida verilmistir.

Def bildiri deyimi projenin general,declarations bölümünde tanimlanmalidir

DefBool : Boolean tipinde degisken tanimlamak için kullaniriz.

DefByte : Byte tipinde degisken tanimlamak için kullaniriz.

DefInt : Integer tipinde degisken tanimlamak için kullaniriz.

DefLng : Long tipinde degisken tanimlamak için kullaniriz.

DefCur : Currency tipinde degisken tanimlamak için kullaniriz.

DefSng : Single tipinde degisken tanimlamak için kullaniriz.

DefDbl : Double tipinde degisken tanimlamak için kullaniriz.

DefDate : Date tipinde degisken tanimlamak için kullaniriz.

DefStr : String tipinde degisken tanimlamak için kullaniriz.

DefVar : Variant tipinde degisken tanimlamak için kullaniriz.

Örnek :

```vbnet
Private Sub Form_Load()
Dim Ad As String
Dim Maas As Currency
Dim D_tarihi As Date
Dim Adres As String
Dim Sira As Integer
End Sub
```

Burada görmüs oldugunuz gibi 5 adet degisken tanimlanmaktadir.Ad degiskeni string tipinde bir degiskendir.Maas degiskeni Currency tipinde bir degiskendir.D_tarihi degiskeni Date tipinde bir degiskendir.Adres degiskeni string tipinde bir degiskendir.Sira degiskeni integer tipinde bir degiskendir.

Asagidaki satirlari formun general,declarations bölümüne yazalim.

Örnek :

```vbnet
DefInt A-C
DefStr S
DefVar K
DefDate D
DefSng V
```

Bu örnekte

A , B, C ile baslayan bütün karakterler Integer türünde olmak zorundadir.

D ile baslayan bütün karakterler Date türünde olmak zorundadir.

V ile baslayan bütün karakterler Single türünde olmak zorundadir.

K ile baslayan bütün karakterler Variant türünde olmak zorundadir.

S ile baslayan bütün karakterler String türünde olmak zorundadir.

Def deyimi dim deyiminden farklidir. Def ile sadece bir harf yada harf araligi belirtilebilir.Burada belirtilen harf ile baslayan bütün degiskenler artik o bildiri deyimindeki tipdedir

Örnek :

```vbnet
Private Sub Form_Load()
Dim ad As String , soyad As String
Dim maas As Currency
End Sub
```

Bu örnektede ad ve soyad isimli iki degisken string türünde ve maas degiskeni ise Currency tipindedir.

Veri Tipleri

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Integer :

Visual Basic’te tam sayi degiskenleri tanimlamak için kullanilir. Hafizada 2 byte yer kaplarlar. Alabilecegi deger araligi -32768 ile +32767 arasindadir.DefInt bildiri deyimi ile tanimlanabilirler. Ayrica bir degiskenin sonunda % karakteri bulunuyorsa bu degisken integer tipindedir.

Örnek :

```vbnet
Private Sub Form_Load()
Dim Maas As Integer
DefInt A-C
Oran% = 100
A_sayi = 100
B_sayi = Oran*A_sayi
C_sayi = B_sayi + A_sayi - 1000
Maas= 32767
End Sub
```

Eger burada tanimlanan degiskenlere daha büyük sayilar atanirsa overflow olusur.

Long :

Daha büyük bir aralikta integer yani tamsayi tanimlamak için kullanabilecegimiz bir veri tipidir. Hafizada 4 byte yer kaplar. Kullanilabilecek uç degerler +2,147,483,647 ile -2,147,483,648 dir. Long tipinde bir degisken tanimlamak için DefLng bildirimini veya degisken sonunda & karakterini kullanabiliriz.

Örnek :

```vbnet
Private Sub Form_Load()
DefLng A-B
Bölüm=50000
cikan&=600000
Kalan& = (cikan / Bölüm ) * 10000
End Sub
```

Single :

Tam sayi olmayan küsüratli sayilar için kullanabilecegimiz bir veri tipidir. Kayan-noktali sayi olarak isimlendirilir. Single tipindeki veriler bellekte 4 byte yer kaplarlar. Nekatif sayilar için alabilecegi aralik -3.402823E38 ile -1.401298E-45 ,pozitif sayilar için alabilecegi aralik 1.401298E-45 ile 3.402823E38 arasindadir.Single tipinde veri tanimlamak için DefSgn bildirimi veya degisken sonuna ! karakteri konur. 7 haneye kadar hassastir.Daha sonrasi yuvarlatilir.

Örnek :

```vbnet
Private Sub Form_Load()
DefSgn A-B
Bölüm=50000
Cikan!=600000
End Sub
```

Double :

Visual Basic’te kullanilabilecek en büyük sayisal degerlerin veri tipidir. Hafizada 8 byte yer kaplarlar. 16 haneye kadar hassastirlar. Maximum alabilecegi degerler pozitif sayilar için 4.94065645841247E-324 ile 1.797693134862232E308 , nekatif sayilar için de -1.797693134862232E308 ile -4.94065645841247E-324 arasindadir. DefDbl bildirimi veya # sembölü ile double tipinde degiskenler tanimlanabilir

Örnek :

```vbnet
Private Sub Form_Load()
DefDbl A-K
Dari=50000
Bugday=600000
Arpa=340.56
End Sub
```

Currency :

Sayisal tipdeki veriler için tanimlanmis özel bir veri tipidir.Hafizada 8 byte yer kaplarlar. 4 hane ondalik kismi olmak üzere toplam 19 haneden olusur.(nokta hariç) Alabilecegi maximum degerler -922,337,203,685,477.5808 ile 922,337,203,685,477.5807 arasindadir. @ sembolü veya DefCur bildirimi ile Currency tipinde degisken’ler tanimlanabilirler.

Örnek :

```vbnet
Private Sub Form_Load()
Dim Maas As Currency , Borc As Currency
Maas = 500000000
Borc = 68000000
Zayi@ = 340000.56
End Sub
```

Date :

Tarih türündeki bilgileri kullanmak için olusturulmus bir veri tipidir. Hafizada 8 byte yer kaplarlar. 1 Ocak ile 31 Aralik 9999 arasindaki tarihleri kullanabilirsiniz. DefDate bildirisi ile tarih türünde degiskenler tanimlayabiliriz.

Örnek :

```vbnet
Private Sub Form_Load()
Dim Dogum_tarihi As Date , Evlenme_Tarihi As Date
Dogum_tarihi =#Dec,9,1977#
Evlenme_Tarihi=#May,15,1998#
End Sub
```

Boolean :

Mantiksal veri tipleri için kullanilir. Iki seçenekten birisini alabilir.Bunlar True veya False degerleridir. Bellekte 2 byte yer isgal ederler.Boolean tipindeki bir degiskeni tanimlamak için DefBool sözcügü kullanilir.

Örnek :

```vbnet
Private Sub Form_Load()
Dim Durum As Boolean , Duyum As Boolean
Durum = True
Duyum = False
End Sub
```

Byte :

O ile 255 arasindaki tamsayilari ifade etmek için kullanilabilecek veri tipidir.DefByte deyimi ile byte tipinde degiskenler tanimlanabilir.

Örnek :

```vbnet
Private Sub Form_Load()
Dim Durum As Byte , Duyum As Byte
Durum =23
Duyum = 143
End Sub
```

String :

Metin türü bilgileri saklamak için kullanilabilecek veri türüdür. 16 bitlik versiyonda 0 ile 65538 arasinda , 32 bitlik versiyonda ise 0 ile 2,000,000,000 arasinda karakter alabilir. String türünde degisken tanimlamak için Defstr veya $ sembolü kullanilir.

Örnek :

```vbnet
Private Sub Form_Load()
Dim Adi As String , Soyadi As String
Adi ="Kemal"
Soyadi = "Tas"
No$="1323970067"
End Sub
```

Variant :

Bu tipte tanimlanmis bir degiskene herhangi bir tip’te veri yüklenebilir.Yani ne tür bir veri girecegimizi bilmedigimiz degiskenleri Variant tipinde tanimlamaliyiz. Bu tür degiskenler hafizada 16 byte tan fazla yer kaplarlar. DefVar bildiri sözcügü ile Variant türünde degiskenler tanimliyabiliriz.

Variant türünde degiskenler tanimlamak fazla kullanisli degildir.Çünki hafizada fazla yer kaplarlar.

Örnek :

```vbnet
Private Sub Form_Load()
Dim Ad As Variant , Maas As Variant , Tel As Variant
Dim Dogum_tarihi As Variant
Ad="Aydin Kale"
Maas=200000
Tel="500-45-00"
Dogum_tarihi=#Apr,3,1970#
End Sub
```

Veri Yapıları

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Const :

Bunlar program içinde degeri degistirilemeyen sabitlerdir. Public ve Private tipinde sabitler tanimlanabiliilir. Public sabitlere tüm modüller içinden ulasilabilir.Private türündeki sabitler ise sadece tanimlandiklari modül içersinde geçerlidirler.Ayrica Visual Basic içinde tanimlanmis çok sayida sabit vardir. Bunlara CONSTANT.TXT dosyasini açarak inceleyebiliriz.

Örnek :

```vbnet
Const sehir="Istanbul"
Const Ulke="Turkey"
Const posta_kodu=34650
Const tek_kod=212
```

Type - End Type Yapisi :

Type yapisini kullanarak programici farkli veri tiplerini kullanarak kendi veri yapisini olusturabilir. Bu C deki Struct yapisina benzetilebilir. Bu yeni veri tipine record adi verilir. Herhangi bir modülün Declarations kisminda asagidaki gibi bir tanimlama yapabiliriz.

Örnek :

```vbnet
Type Ogrenci
Ad As String *10
Soyad As String *12
Not As Byte
Kredi As Integer
End Type

'Ogrenci veri tipi toplam hafizada 25 byte yer kaplamaktadir. Bu veri tipini kullanmak için 'Ogrenci tipinde degiskenler tanimlamak gerekmektedir.

Private Sub Form_Load()
Dim A As Ogrenci
Dim B As Ogrenci

'Bu degiskenlere bilgi atamak asagidaki sekildeki gibidir.

A.Ad="Ali"
A.Soyad ="Armer"
End Sub
```

String türü degiskenlere sabit bir uzunlukta yer ayirmak istersek asagidaki sekilde bir tanimlama yapmaliyiz.

```vbnet
Dim Name As String *12
Dim Address As String *50
```

Diziler

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Ayni tür bilgileri bellekte tutmak için kullanabilecegimiz listelere dizi adi verilir. Dizi kullamanin avantaji ayni tür bilgiler bir listede tutularak daha hizli islem yapilabilmesi saglanmis olacaktir.Visual Basic'de dizi su sekildedir

```vbnet
Dizi_adi(Indis)
```

olacaktir.

Örnek:

```vbnet
Private Sub Form_Load()
Dim ad(2) As String
Dim no(2) As Integer
ad(0) = "ali"
ad(1) = "ahmet"
ad(2) = "ebru"
no(0) = 133
no(1) = 56
no(2) = 67
End Sub
```

Bu örnek'te ad ve no olmak üzere iki adet dizi tanimlanmaktadir. ad dizisi string türünde bilgileri tutacak ve no dizisi ise integer türündeki bilgileri saklayacaktir. Görmüs olgunuz gibi dizilere bilgi atama sekli

```vbnet
dizi_adi(indis_sirasi)=atanacak_bilgi
```

seklindedir.

Eger diziyi sifirdan degilde bir den itibaren baslatmak istersek diziyi tanimlamadan önce Option Base 1 satirini eklemeliyiz.

Burada dizi indisleri sifirdan baslayarak tanimlama yaparken bizim belirtigimiz degere kadardir. Yani bizim bu dizilere atayabilecegim veri sayisi diziyi tanimlarken belirtdigimiz indis degerinden bir fazla olacaktir.

Eger deger atama yaparken belirttigimiz sinirlarin disina çikarsak hata olusur. Dizilere deger atarken dizi sinirlarini kontrol etmekle olasi bir hatayi önlemis oluruz.

Statik Diziler

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Bu tip dizilerde kullanilacak yer sayisi sabittir. Bu tip diziler sadece tanimlandiklari modül içersinde kullanilabilirler. Statik dizi su sekilde tanimlanabilir

```vbnet
Dim dizi_adi(sayi) As Veri_Tipi
```

Tüm proje içinde kullanilacak bir dizi tanimlanmak isterse standart modülün General,Declarations bölümünde yukaridaki sekildeki gibi tanimlanmalidir

Örnek :

```vbnet
Option Base 1
Dim a(5) As Integer

Private Sub Command1_Click()
Text1.Text = a(1) + a(2)
End Sub

Private Sub Form_Load()
a(1) = 10
a(2) = 20
End Sub
```

Bu örnekte görüldügü gibi projenin general,declarations kisminda a() dizisi tanimlaniyor.Bu dzi tanimlanmadan önce dizi indislerinin 1 den itibaren basliyacagini belirten Option Base1 satiri koda dahil edilmistir. Form1 yüklendiginde bu dizinin ilk elemaninna 10 sayisi ikinci elemanina 20 sayisi ataniyor. Eger kullanici Command1 isimli butona tiklarsa dizinin ilk ce ikinci elemanlari toplanarak Form üzerinde Text1 adli nesnenin Text özelligine ataniyor. Yani TextBox'in bu sayilarin toplamini göstermesi saglaniyor.

Dinamik Diziler

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Bu tip dizilerde kullanilacak yer sayisinda bir sinirlama yoktur. Bu tip diziler ilk basta sagidaki sekildeki gibi bir tanimlamaya ihtiyaç duyarlar.

```vbnet
Dim dizi_adi( ) As Veri_Tipi
```

Daha sonra bu dizi kullanilacak iken botunu belirtmek gerekir bunun içinde asagidaki gibi bir tanimlama yapilmalidir.

```vbnet
ReDim dizi_adi(boyut ) As Veri_Tipi
```

Artik bu veri dizisini projemiz içinde kullanabiliriz.

Örnek :

```vbnet
Option Base 1
Private Sub Form_Load()
Dim s() As String
End Sub

Private Sub Command1_Click()
ReDim s(10) As String
s(1) = "Selam "
s(2) = "Ayse"
Text1.Text = s(1) + s(2)
End Sub
```

Bu dizi tanimlanmadan önce dizi indislerinin 1 den itibaren basliyacagini belirten Option Base1 satiri koda dahil edilmistir. Form1 yüklendiginde s adli bir dinamik dizi tanimlanmaktadir. Kullanici Command1 isimli butuna tikladiginda s dizisinin boyutu belirtilerek yeniden tanimlanmistir. Bu dizinin ilk elemaninna "Selam " degeri ikinci elemanina "Ayse" degeri ataniyor. Dizinin ilk ve ikinci elemanlari toplanarak Form üzerinde Text1 adli nesnenin Text özelligine ataniyor. Yani TextBox'in bu degerlerin toplamini göstermesi saglaniyor.

Örnek :

```vbnet
Option Base 1
Private Sub Form_Load()
Dim s() As String
End Sub

Private Sub Command1_Click()
ReDim s(10) As String
s(1) = "selam"
s(2) = "fatih"
Text1.Text = s(1) + s(2)
End Sub

Private Sub Command2_Click()
ReDim s(5) As String
s(2) = "fatih"
Text1.Text = s(1) + s(2)
End Sub
```

Bu örnekte yukaridaki örnekten tek farkli yan olarak bir Command butonun arkasina yazilmis kod bulunuyor. Eger kullanici Command1 adli butondan sonra bu butona tiklarsa ne olacak ona bakalim. Command2 butonuna tiklanildiginda s() dizisi tekrardan boyutu 5 olrak tanimlaniyor. s() dizisine daha önce atamis bütün degerler siliniyor. Yani s() dizisi bir nevi bosaltiliyor ve yeniden boyutlandiriliyor. Eger s() dizisine daha önce atanmis degerler korunmak istenirse asagidaki sekildeki gibi bir tanimlama yapilmak zorundadir.

```vbnet
ReDim Preserve s(boyut) As Veri_tipi
```

Tip Dösümleri

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Visual Basic'de kullandigimiz sayisal degiskenleri diger veri tiplerine dönüstürebiliriz. Bu islemi yapan fonksiyonlara tip dönüsüm fonksiyonlari adi verilir. Tip dönüsüm fonksiyonlari asagida verilmistir.

Fonksiyon Geri Dönen Deger Yaptigi Islem

CBool(ifade) Boolean Matemetiksel ifadeyi Boolean türüne dönüstürür.

CByte(ifade) Byte Matemetiksel ifadeyi Byte türüne dönüstürür.

CCur(ifade) Currency Matemetiksel ifade Currency türüne dönüstürür.

CDate(ifade) Date Matemetiksel ifade Date türüne dönüstürür.

CDbl(ifade) Double Matemetiksel ifade Double türüne dönüstürür.

CDec(ifade) Decimal Matemetiksel ifadeDecimal sayiya dönüstürür.

CInt(ifade) Integer Matemetiksel ifade tam sayiya dönüstürür.

CLng(ifade) Long Matemetiksel ifade Long türüne dönüstürür.

CSng(ifade) Single Matemetiksel ifade Single türüne dönüstürür.

CVar(ifade) Variant Matemetiksel ifade Variant türüne dönüstürür.

CStr(ifade) String Matemetiksel ifade String türüne dönüstürür.

Asagida çesitli örneklerle tip dönüsümleri açiklanmaya çalisilmistir.

Örnek1:

```vbnet
A=10 , B=5 , C=10 , D=0
check = CBool(A < B) 'check=False
check = CBool(A > B) 'check=True
check = CBool(A = C) 'check=True
check = CBool(D) 'check=False
check = CBool(B) 'check=True
```

Örnek2 :

```vbnet
A=10 , B=5 , C=0
check = CBytel(A < B) 'check=0
check = CByte(A > B) 'check=1
check = CByte(A = C) 'check=0
```

Örnek3 :

```vbnet
A=1 , B=2 , C=36000 , D=36001
check = CDate(A) 'check=12/31/1899
check = CDate(B) 'check=1/1/1900
check = CDate(C) 'check=7/24/98
check = CDate(D) 'check=7/26/98
```

Örnek4 :

```vbnet
A=2.4 , B=2.5 , C=2.6 , D=3.5
check = CInt(AB) 'check=2
check = CInt(B) 'check=2
check = CInt(C) 'check=3
check = CInt(D) 'check=4
```

Aritmetiksel Operatorler

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

`+ , - , * , / , \ , ^ ,Mod , &`

Genel olarak matematiksel islemlerde kullanilan operatörlerdir. Bunlara kaynastirma "&" operatörünü de ilave edebiliriz. Simdi bu operatörleri açiklayalim.

+ Operatörü :

Bu operatör ile verilen iki veya daha fazla ifade toplanabilir.Genel yazilisi asagidaki sekilde gibidir.

```vbnet
Sonuc = Ifade1 + Ifade2
```

Burda Sonuc mutlaka sayisal bir degerdir.(Eger kaynastirma yapilmamis ise)

Ifade1 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Ifade2 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Eger Ifade1 ve Ifade2 string türünde veriler ise + operatörü kaynastirma yapar. Yani Ifade2 yi Ifade1’in sonuna ekler.Asagida Çesitli örnekler verilmistir.

Örnek :

```vbnet
Sonuc=13+45 'Sonuc=58
Sonuc=1378+56.78+435.908 'Sonuc=1870.688
A=89,B=3456
Deger=A+B ' Deger=3545
Ad="Ebru"
Soyad=" Kayaci"
Dim Name As String
Name=Ad+Soyad 'Name="Ebru Kayaci"
```

Operatörler :

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Matematik’de kullanilan çikartma opratörüdür. Birinci ifadede verilen degerden ikinci ifadeyi çikarir.

Genel yazilisi asagidaki sekildeki gibidir.

```vbnet
Sonuc=Ifade1 - Ifade2
```

Burda Sonuc mutlaka sayisal bir degerdir.

Ifade1 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Ifade2 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Asagida çesitli örneklerle - (çikarma )operatörü açiklanmaya çalisilmistir

Örnek :

```vbnet
Sonuc=3475.45-3445.90 'Sonuc = 29.55
Deger=45-788-23 'Deger = - 766
Son=190,Ara=47
Son1=Son-Ara ' Son = 143
```

\* Operatörü :

Matematikdeki çarpma operatörüdür. Verilen iki sayiyi çarpar. Genel yazim sekli asagidaki sekilideki gibidir

```vbnet
Sonuc=Sayi1 * Sayi2
```

Burda Sonuc mutlaka sayisal bir degerdir.

Sayi1 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Sayi2 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Asagida çesitli örneklerle çarpma operatörü açiklanmistir.

Örnek :

```vbnet
Sonuc=34 * 9 'Sonuc = 306
Deger = 87 * 12 'Deger = 1044
A=5,B= 56
C=A * B 'C = 280
```

/ Operatörü :

Matematikdeki bölme operatörüdür. Verilen ilk sayiyi ikinci sayiya böler. Genel yazim sekli asagidaki sekilideki gibidir.

```vbnet
Sonuc=Ifade11 /Ifade2
```

Burda Sonuc mutlaka sayisal bir degerdir.

Ifade1 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Ifade2 çesitli islemlerden olusmus bir ifade veya bir sayidir.Ifade2 sifirdan farkli bir deger olmalidir. Yoksa sifira bölme hatasi olusur.

Asagida çesitli örneklerle bölme operatörü açiklanmistir.

Örnek :

```vbnet
Sonuc=34 / 9 'Sonuc = 3.777778
Deger = 60 / 12 'Deger = 5
A=5,B= 56
C=B / A 'C = 11.2
```

Operatörler :

\ Operatörü :

Matematikdeki bölme operatörüdür. Verilen ilk sayiyi ikinci sayiya böler. Ancak sonuc mutlaka bir tam sayi degeridir. Bölüm küsüratli ise sayinin kusuratini atar.Genel yazim sekli asagidaki sekildeki gibidir.

```vbnet
Sonuc=Ifade1 \ Ifade2
```

Burda Sonuc mutlaka sayisal bir degerdir.

Ifade1 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Ifade2 çesitli islemlerden olusmus bir ifade veya bir sayidir.Ifade2 sifirdan farkli bir deger olmalidir. Yoksa sifira bölme hatasi olusur.

Asagida çesitli örneklerle tam bölme operatörü açiklanmistir

Örnek :

```vbnet
Sonuc=34 \ 9 'Sonuc = 3
Deger = 60 \ 12 'Deger = 5
A=5,B= 56
C=B \ A 'C = 11
```

^ Operatörü :

Matematikdeki üs operatörüdür. Verilen ilk sayinin ikinci sayi kadar kuvvetini (üssünü) alir. Genel yazim sekli asagidaki sekilideki gibidir.

```vbnet
Sonuc=Ifade1 ^ Ifade2
```

Burda Sonuc mutlaka sayisal bir degerdir.

Ifade1 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Ifade2 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Asagida çesitli örneklerle bölme operatörü açiklanmistir.

Örnek :

```vbnet
Sonuc=34 ^ 9 'Sonuc = 6.071699276646e+13
Deger = 60 ^ 2 'Deger = 3600
A=5,B= 5
C=B ^ A 'C = 3125
```

Mod Operatörü :

Matematikdeki mod alma operatörüdür. Verilen ilk sayinin modunu ikinci sayi göre alir. Genel yazim sekli asagidaki sekilideki gibidir.

```vbnet
Sonuc=Ifade1 Mod Ifade2
```

Burda Sonuc mutlaka sayisal bir degerdir.

Ifade1 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Ifade2 çesitli islemlerden olusmus bir ifade veya bir sayidir.

Asagida çesitli örneklerle Mod operatörü açiklanmistir.

Örnek :

```vbnet
Sonuc=34 Mod 9 'Sonuc = 7
Deger = 60 Mod 2 'Deger = 0
A=5.4,B= 57
C=B Mod A 'C = 2
D= 57 Mod 5.5 'D = 3
E=90.5 Mod 6 'E = 0
E=90.2 Mod 6 'E = 0
E=90.7 Mod 6 'E = 1
```

& Operatörü :

Bu operatör kaynastirma operatörüdür. String türü ifadelerle matematiksel ifadeleri kaynastirmada kullanilabilir. Genel yazim sekli asagidaki sekilideki gibidir.

```vbnet
Sonuc=Ifade1 & Ifade2 Burda Sonuc string veya variant türünde bir degerdir.
```

Ifade1 çesitli islemlerden olusmus bir ifade veya bir sayi veya bir metindir.

Ifade2 çesitli islemlerden olusmus bir ifade veya bir sayi veya bir metindir.

Asagida çesitli örneklerle kaynastirma operatörü açiklanmistir.

Örnek :

```vbnet
Sonuc=34 & 9 'Sonuc = 349
Deger = 60 & 2 'Deger = 602
A=5.4,B= 57
C=B&A 'C = 575.4
D= 57 & 5.5 'D = 575.5
E=90.5 & 6 'E = 90.56
E=9.2 &6 'E = 9.26
E=90.7 & 6.6 'Hata olusur
E="Hakan"&" Ayse" 'E = "Hakan Ayse"
```

Karsilastirma Operatörleri :

Bu operatörler ile verilen ifadeler arasinda karsilastirmalar yapilir. Genel karsilastirma operatörleri asagida verilmistir.

= operatörü :

Bu operatör verilen iki ifadenin esit olup olmadigini anlamak için kullanilir.Genel yazim sekli asagidaki sekildeki gibidir.

```vbnet
Sonuc=(Ifade11 = Ifade2)
```

Burda Sonuc Booean tipinde bir degerdir.

Ifade1 bir sayi veya bir metindir.

Ifade2 bir sayi veya bir metindir.

Asagida çesitli örneklerle kaynastirma operatörü açiklanmistir

Örnek :

```vbnet
Sonuc=(100=345) 'Sonuc=False
Sonuc=(100=100) 'Sonuc=True
A=12,B=45
Sonuc=(A=B) 'Sonuc=False
C=23,D=23
Sonuc=(A=D) 'Sonuc=True
```

<> operatörü :

Bu operatör verilen iki ifadenin farkli olup olmadigini anlamak için kullanilir.Genel yazim sekli asagidaki sekildeki gibidir.

```vbnet
Sonuc=(Ifade11 <>Ifade2)
```

Burada Sonuc Booean tipinde bir degerdir.

Ifade1 bir sayi veya bir metindir.

Ifade2 bir sayi veya bir metindir.

Asagida çesitli örneklerle kaynastirma operatörü açiklanmistir.

Örnek :

```vbnet
Sonuc=(100<>345) 'Sonuc=True
Sonuc=(100<>100) 'Sonuc=False
A=12,B=45
Sonuc=(A<>B) 'Sonuc=True
C=23,D=23
Sonuc=(A<>D) 'Sonuc=False
```

< operatörü :

Bu operatör verilen birinci ifadenin ikinci ifadeden küçük olup olmadigini anlamak için kullanilir.Genel yazim sekli asagidaki sekildeki gibidir.

```vbnet
Sonuc=(Ifade11 < Ifade2)
```

Burda Sonuc Booean tipinde bir degerdir.

Ifade1 bir sayi veya bir metindir.

Ifade2 bir sayi veya bir metindir.

Asagida çesitli örneklerle kaynastirma operatörü açiklanmistir.

Örnek :

```vbnet
Sonuc=(100<345) 'Sonuc=True
Sonuc=(100<100) 'Sonuc=False
Sonuc=(100<130) 'Sonuc=False
A=12,B=45
Sonuc=(A<B) 'Sonuc=True
C=23,D=23
Sonuc=(A<D) 'Sonuc=False
```

> operatörü :

Bu operatör verilen birinci ifadenin ikinci ifadeden büyük olup olmadigini anlamak için kullanilir.Genel yazim sekli asagidaki sekildeki gibidir.

```vbnet
Sonuc=(Ifade11 > Ifade2)
```

Burda Sonuc Booean tipinde bir degerdir.

Ifade1 bir sayi veya bir metindir.

Ifade2 bir sayi veya bir metindir.

Asagida çesitli örneklerle kaynastirma operatörü açiklanmistir.

Örnek :

```vbnet
Sonuc=(800>345) 'Sonuc=True
Sonuc=(100>100) 'Sonuc=False
Sonuc=(100>130) 'Sonuc=False
A=90,B=45
Sonuc=(A>B) 'Sonuc=True
C=23,D=23
Sonuc=(A>D) 'Sonuc=False
```

=> operatörü :

Bu operatör verilen birinci ifadenin ikinci ifadeden büyük veya esit olup olmadigini anlamak için kullanilir.Genel yazim sekli asagidaki sekildeki gibidir

```vbnet
Sonuac=(Ifade11 => Ifade2)
```

Burda Sonuc Booean tipinde bir degerdir.

Ifade1 bir sayi veya bir metindir.

Ifade2 bir sayi veya bir metindir.

Asagida çesitli örneklerle kaynastirma operatörü açiklanmistir.

Örnek :

```vbnet
Sonuc=(800=>345) 'Sonuc=True
Sonuc=(100=>100) 'Sonuc=True
Sonuc=(100=>130) 'Sonuc=False
A=90,B=45
Sonuc=(A=>B) 'Sonuc=True
C=23,D=23
Sonuc=(A=>D) 'Sonuc=True
```

<= operatörü :

Bu operatör verilen birinci ifadenin ikinci ifadeden büyük olup olmadigini anlamak için kullanilir.Genel yazim sekli asagidaki sekildeki gibidir.

```vbnet
Sonuc=(Ifade11 <= Ifade2)
```

Burda Sonuc Booean tipinde bir degerdir.

Ifade1 bir sayi veya bir metindir.

Ifade2 bir sayi veya bir metindir.

Asagida çesitli örneklerle kaynastirma operatörü açiklanmistir.

Örnek :

```vbnet
Sonuc=(800<=345) 'Sonuc=False
Sonuc=(100<=100) 'Sonuc=True
Sonuc=(100<=130) 'Sonuc=True
A=90,B=45
Sonuc=(A<=B) 'Sonuc=False
C=23,D=23
Sonuc=(A<=D) 'Sonuc=True
```

And Operatörü :

Lojik iki ifadenin karsilastirilmasi için kullanilir. Iki ifadenin'de dogru olmasi gereklidir. Genel yazim sekli asagidaki gibidir ;

```vbnet
Sonuc=Kosul1 And Kosul2
```

Burada Sonuc herhangi bir sayisal tipde degiskendir.

Kosul1 herhangi bir ifadedir.

Kosul2 herhangi bir ifadedir.

And operatörünün dogruluk tablosu asagidaki sekildeki gibidir.

Ifade1 Ifade2 Sonuc=Ifade1 And Ifade2

False False False

False True False

True False False

True True True

True Null Null

Null True Null

False Null False

Null False False

Null Null Null

And operatörü ayni zamanda bitwise comparison islemide yapilabilir.

Ifade1 Ifade2 Ifade1 And Ifade2

0 0 0

0 1 0

1 0 0

1 1 1

Örnek :

```vbnet
Sonuc = (False And False ) 'Sonuc=False
Sonuc = (Null And False ) 'Sonuc=False
A=True , B=True
Sonuc = (A And B ) ' Sonuc=True
A=1 ,B=0
Sonuc = (A And B ) ' Sonuc=0
A=1 ,B=1
Sonuc = (A And B ) ' Sonuc=1
A=1,B=4
Sonuc = (A And B ) ' Sonuc=0
A=1,B=3
Sonuc = (A And B ) ' Sonuc=1
A=1,B=5
Sonuc = (A And B ) ' Sonuc=1
A=1,B=8
Sonuc = (A And B ) ' Sonuc=0
```

Or Operatörü :

Lojik iki ifadenin karsilastirilmasi için kullanilir. Iki ifadeden yalnizca birinin dogru olmasi yeterlidir. Genel yazim sekli asagidaki gibidir :

```vbnet
Sonuc=Kosul1 Or Kosul2
```

Burada Sonuc hehangi bir sayisal tipde degiskendir.

Kosul1 herhangi bir ifadedir.

Kosul2 herhangi bir ifadedir.

Or operatörünün dogruluk tablosu asagidaki sekildeki gibidir ;

Ifade1 Ifade2 Sonuç=Ifade Or Ifade2

False False False

False True True

True False True

True True True

True Null True

Null True True

False Null Null

Null False Null

Null Null Null

Or operatörü ayni zamanda bitwise comparison islemide yapilabilir.

Ifade1 Ifade2 Sonuç=Ifade Or Ifade2

0 0 0

0 1 1

1 0 1

1 1 1

Örnek :

```vbnet
Sonuc = (False Or False ) ' Sonuc=False
Sonuc = (Null Or False ) 'Sonuc=Null
A=True , B=True
Sonuc = (A Or B ) 'Sonuc=True
A=1 ,B=0
Sonuc = (A Or B ) 'Sonuc=1
A=1 ,B=1
Sonuc = (A Or B ) 'Sonuc=1
A=1,B=4
Sonuc = (A Or B ) 'Sonuc=5
A=1,B=3
Sonuc = (A Or B ) 'Sonuc=3
A=1,B=5
Sonuc = (A Or B ) 'Sonuc=5
A=1,B=8
Sonuc = (A Or B ) 'Sonuc=9
A=10,B=8
Sonuc = (A Or B ) 'Sonuc=10
```

Xor Operatörü :

Lojik iki ifadenin karsilastirilmasi için kullanilir. Iki ifadeden yalnizca birinin dogru olmasi gereklidir. Eger ikiside dogru olursa sonuc yanlis olur. Genel yazim sekli asagidaki gibidir :

```vbnet
Sonuc=Kosul1 Xor Kosul2
```

Burada Sonuc hehangi bir sayisal tipde degiskendir.

Kosul1 herhengi bir ifadedir.

Kosul2 herhengi bir ifadedir.

Xor operatörünün dogruluk tablosu asagidaki sekildeki gibidir;

Ifade1 Ifade2 Sonuç=Ifade Xor Ifade2

False False False

False True True

True False True

True True False

Xor operatörü ayni zamanda bitwise comparison islemide yapilabilir.

Ifade1 Ifade2 Sonuç=Ifade Xor Ifade2

0 0 0

0 1 1

1 0 1

1 1 0

Örnek :

```vbnet
Sonuc = (False Xor False ) ' Sonuc=False
Sonuc = (True Xor False ) 'Sonuc=True
A=True , B=True
Sonuc = (A Xor B ) 'Sonuc=False
A=1 ,B=0
Sonuc = (A Xor B ) 'Sonuc=1
A=1 ,B=1
Sonuc = (A Xor B ) 'Sonuc=0
A=1,B=4
Sonuc = (A Xor B ) 'Sonuc=5
A=1,B=3
Sonuc = (A Xor B ) 'Sonuc=2
A=1,B=5
Sonuc = (A Xor B ) 'Sonuc=4
A=1,B=8
Sonuc = (A Xor B ) 'Sonuc=9
A=10,B=8
Sonuc = (A Xor B ) 'Sonuc=2
```

Eqv Operatörü :

Lojik iki ifadenin karsilastirilmasi için kullanilir. Iki ifadenin ikisininde dogru veya ikisininde yanlis olmasi durumunda dogru sonuc alir. Genel yazim sekli asagidaki gibidir

```vbnet
Sonuc=Kosul1 Eqv Kosul2
```

Burada Sonuc herhangi bir sayisal tipde degiskendir.

Kosul1 herhangi bir ifadedir.

Kosul2 herhangi bir ifadedir.

Eqv operatörünün dogruluk tablosu asagidaki sekildeki gibidir;

Ifade1 Ifade2 Sonuç=Ifade Eqv Ifade2

False False True

False True False

True False False

True True True

Eqv operatörü ayni zamanda bitwise comparison islemide yapilabilir.

Ifade1 Ifade2 Sonuç=Ifade Eqv Ifade2

0 0 1

0 1 0

1 0 0

1 1 1

Örnek :

```vbnet
Sonuc = (False Eqv False ) ' Sonuc=True
Sonuc = (True Eqv False ) 'Sonuc=False
A=True , B=True
Sonuc = (A Eqv B ) 'Sonuc=True
A=1 ,B=0
Sonuc = (A Eqv B ) 'Sonuc=0
A=1 ,B=1
Sonuc = (A Eqv B ) 'Sonuc=1
A=1,B=4
Sonuc = (A Eqv B ) 'Sonuc=-6
A=1,B=3
Sonuc = (A Eqv B ) 'Sonuc=-3
A=1,B=5
Sonuc = (A Eqv B ) 'Sonuc=-5
A=1,B=8
Sonuc = (A Eqv B ) 'Sonuc=-10
A=10,B=8
Sonuc = (A Eqv B ) 'Sonuc=-3
```

Imp Operatörü :

Lojik iki ifadenin karsilastirilmasi için kullanilir. Birincinin degili veya ikincidir. Genel yazim sekli asagidaki gibidir :

```vbnet
Sonuc=Kosul1 Imp Kosul2
```

Burada Sonuc hehangi bir sayisal tipde degiskendir.

Kosul1 herhangi bir ifadedir.

Kosul2 herhangi bir ifadedir.

Imp operatörünün dogruluk tablosu asagidaki sekildeki gibidir.

Ifade1 Ifade2 Sonuç=Ifade Imp Ifade2

False False True

False True True

True False False

True True True

True Null True

Null True True

False Null True

Null False Null

Null Null Null

Imp operatörü ayni zamanda bitwise comparison islemide yapilabilir.

Ifade1 Ifade2 Sonuç=Ifade Imp Ifade2

0 0 1

0 1 1

1 0 0

1 1 0

Örnek :

```vbnet
Sonuc = (False Imp False ) 'Sonuc=True
Sonuc = (Null Imp False ) 'Sonuc=True
A=True , B=True
Sonuc = (A Imp B ) 'Sonuc=True
A=1 ,B=0
Sonuc = (A Imp B ) 'Sonuc=0
A=1 ,B=1
Sonuc = (A Imp B ) 'Sonuc=1
A=1,B=4
Sonuc = (A Imp B ) 'Sonuc=-2
A=1,B=3
Sonuc = (A Imp B ) 'Sonuc=-1
A=1,B=5
Sonuc = (A Imp B ) 'Sonuc=-1
A=1,B=8
Sonuc = (A Imp B ) 'Sonuc=-2
A=10,B=8
Sonuc = (A Imp B ) 'Sonuc=-3
```

Not Operatörü :

Lojik bir ifadenin degilinin alinmasi için kullanilir. Genel yazim sekli asagidaki gibidir :

```vbnet
Sonuc=Not Kosul
```

Burada Sonuc herhangi bir sayisal tipde degiskendir.

Kosul herhangi bir ifadedir.

Not operatörünün dogruluk tablosu asagidaki sekildeki gibidir ;

Ifade Not Ifade

True False

False True

Not operatörü ayni zamanda bitwise comparison islemide yapilabilir.

Ifade Not Ifade

0 1

1 0

Örnek :

```vbnet
Sonuc=(Not True) 'Sonuc=False
Sonuc=(Not 1) 'Sonuc=False
A=4
Sonuc=(Not A) 'Sonuc=-5
A=45
Sonuc=(Not A) 'Sonuc=-46
Sonuc=(Not 10) 'Sonuc=-11
```

Visual Basic'de Kontrol Komutları

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Kontrol komutlari programcilar tarafindan sikca kullanilan belirli ifadeleri kontrol etmek veya bazi sartlarin gerçeklesip gerçeklesmedigini kontrol etmek amaciyla kullanilan komutlardir. Biz burada en çok kullanilan komutlarin üzerinde duracagiz.

If Kontrol Yapisi :

Genel olarak bu komut yapisi su sekilde yazilir.

```vbnet
If Kosul Then
Kosul dogru ise yapilmasi istenen islemler.
Endif
```

Kullandigimiz her If kontrolu için mutlaka bir Endif kullanmaliyiz. Bu kontrol yapisinin sonlandigini belirtir.

Örnek:

```vbnet
If ad="FATIH" Then
Maas=10000000
Endif
```

Eger kosul gerçeklesmemis ise yapilmasi istenen bazi islemler varsa o zaman su sekilde bir kontrol yapisini kullanabiliriz.

```vbnet
If Kosul Then
Kosul dogru ise yapilmasi istenen islemler.
Else
Kosul yanlis ise yapilmasi istenen islemler.
Endif
```

Ayni anda bir kaç kosul için karsilastirma yapilmak isternirse;

```vbnet
If Kosul Then
Kosul dogru ise yapilmasi istenen islemler.
Elseif Kosul1 Then
Kosul1 dogru ise yapilmasi istenen islemler.
Elseif Kosul2 Then
Kosul2 dogru ise yapilmasi istenen islemler.
Else
Bütün kosullar yanlis ise yapilmasi istenen islemler.
Endif
```

yapisi kullanilir. Bu yapida mutlaka Else blogunun bulunmasina gerek yoktur. Burada eger Kosul dogru ise ilk Then’den sonraki satirlar çalistirilarak Elseif ifadesine kadar icra edilirler. Daha sonra Endif ifadesinden sonraki satir icra edilir.Eger Kosul yanlis ise Kosul1 ifadesi kontrol edilir.Dogru ise buradaki then den sonraki satirlar çalistirilir. Yanlis ise Kosul2’ye bakilir. Eger bu kosulda yanlis ise Else ifadesinden sonraki satirlar çalistirilir.

Örnek :

```vbnet
If Isim="Ali" Then
Maas=Maas * 1.2
Elseif Isim="Murat" Then
Maas=Maas * 1.4
Elseif Isim="Kemal" Then
Maas=Maas * 1.1
Endif
```

Örnek :

```vbnet
If Bolen=0 Then
Msg.Text=" Bolen sayi sifir olamaz."
Else
Sonuc= Sayi / Bolen
Msg.Text = Sonuc
Endif
```

Ornek :

```vbnet
If name="Ali" AND no="1301920035"
Not=4
ElseIf name="Ahmet" AND no="1301940023" Then
Not=3
ElseIf name="Hakan" AND no="1301930045" Then
Not=2
ElseIf name="Hatice" AND no="1301940005" Then
Not=7
Endif
```

Select Case:

Bu kontrol yapisinda sadece bir degiskenin durum kontrolü yailir.Kontrolü yapilacak degiskenin genel olarak alabilecegi degerler belirli ise bu yapinin kukllanilmasi If yapisina göre daha avantajlidir. Yazilis biçimi genel olarak asagidaki sekildeki gibidir

```vbnet
Select Case Degisken
Case Deger1
Degisken=Deger1 oldugu durumda yapilmasi istenen islemler
Case Deger2
Degisken=Deger2 oldugu durumda yapilmasi istenen islemler
Case Else
Degisken yukaridaki degerler den hicbirine esit degil ise yapilacak islemler
End Select
```

Kullandigimiz her Select ifadesi için bir End Select kullanmaliyiz.

Örnek :

```vbnet
Select Case No
Case 1304
Name="Murat Tuna"
Case 1306
Name="Ayse Sinem"
Case 1307
Name="Hakan Kaya"
Case 1312
Name="Abdullah Kahyali"
Case 1324
Name="Hatice Uygun"
End Select
```

Örnek :

```vbnet
Select Case Ay
Case 1
Max_date=31
Case 2
Dim Artik as Integer
Artik = Yil Mod 4
If Artik=0 Then
Max_date=29
Else
Max_date=28
Endif
Case 3
Max_date=31
Case 12
Max_date=31
Case Else
Mesaj="Error : Bir yilda 12 ay vardir."
End Select
```

Visual Basic'te Döngü Komutlari

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Bu komutlar belirli islemleri belirli sayida veya herhangi bir sart saglanana kadar tekrarlamak amaci ile kullanilirlar. Bu komutlar asagida verilmistir.

For ….. Next Döngüsü

Do While …. Loop Döngüsü

Do Until ……Loop Döngüsü

Do …… Loop While Döngüsü

Do …… Loop Until Döngüsü

Asagidada bu döngülerin nasil kullanildiklari açiklanmis ve örneklerle pekistirilmistir.

For Next Döngüsü :

Bütün dillerde bulunan döngü yapisidir. Genel yazim sekli asagidaki sekildeki gibidir.

```vbnet
For sayac=baslangiç To bitis Step artim
Arada isletilecek komutlar
Next sayac
```

Bu döngü sayac baslangic degerinden bitis degerine kadar çalistirilir. Sayaç baslangic degerinde iken döngü içindeki komutlar isletilir. Next ifadesine gelindiginde tekrar For satirina gelinir. Sayac degeri artim kadar artirilir. Eger Sayac degeri Bitis degerini geçmis ise Next adimindan sonraki adim isletilir. Burada step degerine pozitif veya nekatif bir deger versilebilir. Eger nekatif deger verilirse sayac her seferinde 1 azaltilir.Step adimini vermezsek bu pozitif 1 (+1) anlamindadir ve her adimda sayac bir artirilacaktir.Biz içiçe For Next döngüleride kurabiliriz. Ancak burada suda dikkat edilmelidir. En son baslatilan For döngüsü ilk önce bitirilmelidir.

```vbnet
For sayac1=basla1 To son1
Komutlar
For sayac2=basla2 To son2
Komutlar
Next sayac2
Next sayac1
```

Biz buradaki sayiyi daha da artirabiliriz.

Asagidaki sekideki gibi bir kullanim hatalidir

```vbnet
For sayac1=basla1 To son1
Komutlar
For sayac2=basla2 To son2
Komutlar
Next sayac1
Next sayac2 Burada For döngüsü isletilirken hata olusacaktir
```

Örnek :

```vbnet
Factöriyel=1
For I=1 To Sayi
Factöriyel= Factöriyel * I
Next I
```

Bu örnekte girmis oldugunuz pozitif sayinin faktoriyeli hesaplanmaktadir.

Do While Döngüsü :

Bu dögünün genel yazim sekli asagidaki sekildeki gibidir.

```vbnet
Do While Kosul
Komutlar
Loop
```

Burada önce Kosula bakilir. Eger kosul dogru ise aradaki satirlar çalistirilir taki Loop satirina kadar. Loop satirinda tekrar While satirina dönülür. Kosul tekrar kontrol edilir. Eger dogru ise ara satirlar tekrar çalistirilir. Kosul yanlis ise Loop ‘tan sonraki ilk satirdan program çalismaya devam eder. Içiçe Do While döngüleride kurabiliriz.

```vbnet
Do While Kosul1
….
Do While Kosul2
…
Komutlar
Loop
…..
Loop
```

Her Do While için mutlaka bir Loop yerlestirmeliyiz.

Örnek :

```vbnet
Fact=1 I=2
Do While I<=Sayi
Fact=Fact * I
I=I+1
Loop
```

Buradaki örnekte te faktöriyel hesabini Do While döngüsü ile yapiyoruz. Burada sayac olarak I degeri kullaniliyor. Eger faktöriyeli hesaplanacak deger 2 den kücükse (1 veya 0 ise) döngü içine girilmemektedir. Döngü içinde sayac artimini kendimiz veriyoruz. Sayac sayi degerine esit iken döngü son kez çalitiriliyor.

Do ….. Loop While Döngüsü :

Bu döngü yapisinin genels yazim sekli asagida verilmistir.

```vbnet
Do
…..
Komutlar
…..
Loop While Kosul
```

Bu ifade de döngü içinde komutlar mutlaka bir defe icra edilir. Daha sonra Kosul kontrol edilir. Eger kosul dogru ise tekrar Do satirina dallanilir ve aradaki komutlar tekrar icra edilir. Yanlis ise döngüden çikilir.Bu yapiyida içiçe kullanmamiz mümkündür.

Örnek :

```vbnet
Fact =1 I=1
Do
Fact=Fact *I
I=I+1
Loop While I<=Sayi
```

Faktöriyel hesapini yapan bir baska örnek verilmistir.

Do Until Döngüsü:

Bu döngünün genel yazim sekli asagidaki sekildeki gibidir.

```vbnet
Do Until Kosul
Komutlar
Loop
```

Burada önce Kosula bakilir. Eger kosul yanlis ise aradaki satirlar çalistirilir'taki Loop satirina kadar. Loop satirinda tekrar While satirina dönülür. Kosul tekrar kontrol edilir. Eger yanlis ise ara satirlar tekrar çalistirilir. Kosul dogru ise Loop‘tan sonraki ilk satirdan program çalismaya devam eder. Içiçe Do Until döngüleride kurabiliriz. Do While döngüsünden tek farki kosul yanlis iken çalistirilir.

```vbnet
Do Until Kosul1
…
Do Until Kosul2
…
Komutlar
Loop
…..
Loop
```

Her Do Until için mutlaka bir Loop yerlestirmeliyiz.

Örnek :

```vbnet
Fact=1 I=Sayi
Do Until I<=1
Fact=Fact * I
I=I-1
Loop
```

Buradaki örnekte'de faktöriyel hesabini Do Until döngüsü ile yapiyoruz. Burada sayac olarak I degeri kullaniliyor. Eger faktöriyeli hesaplanacak deger 2 den küçükse (1 veya 0 ise) döngü içine girilmemektedir.Döngü içinde sayac azaltimini kendimiz veriyoruz. Sayac 2 degerine esit iken döngü son kez çalistiriliyor

Do … Loop Until Döngüsü :

Bu döngü yapisinin genel yazim sekli asagida verilmistir.

```vbnet
Do
…
Komutlar
…
Loop Until Kosul
```

Bu ifade de döngü içinde komutlar mutlaka bir defa icra edilir. Daha sonra Kosul kontrol edilir. Eger kosul yanlis ise tekrar Do satirina dallanilir ve aradaki komutlar tekrar icra edilir. Kosul dogru ise döngüden çikilir.Bu yapiyida içiçe kullanmamiz mümkündür

Örnek :

```vbnet
Fact =1 I=1
Do
Fact=Fact *I
I=I+1
Loop While I>Sayi
```

Faktöriyel hesapini yapan bir baska örnek verilmistir

Kes, Kopyala, Yapıştır

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Bir TextBox'ta Kes, Kopyala, Yapıştır, Geri Al işlemlerinin yapılması için iki tane çok kolay yol mevcut. Aşağıdaki örnekler SendKeys methodunu kullanıyor.

İşte birinci örnek:

```vbnet
Sub DoEditThing(whatThing As String, onWhat As Object)
Select Case whatThing
Case "Copy"
onWhat.SetFocus
SendKeys "^C"
Case "Cut"
onWhat.SetFocus
SendKeys "^X"
Case "Paste"
onWhat.SetFocus
SendKeys "^V"
Case "Undo"
onWhat.SetFocus
SendKeys "^Z"
End Select
End Sub
```

Aşağıdaki kod aynı işi yapan ikinci örnek:

```vbnet
Sub DoEditThing(whatThing As String, onWhat As Object)
Dim Send$
Select Case whatThing
Case "Copy"
Send = "^C"
Case "Cut"
Send = "^X"
Case "Paste"
Send = "^V"
Case "Undo"
Send = "^Z"
End Select
If Len(Send) Then
onWhat.SetFocus
SendKeys Send
End If
End Sub
```

Şimdi, yukarıdaki iki örnekten birini formunuza ekledikten sonra aşağıdaki kod satırıyla istediğiniz işlemi yapabilirsiniz.

```vbnet
DoEditThing Copy|Cut|Paste|Undo*, On_Which_Object**
```

\* - Bir tanesini seçin; Copy, Cut, Paste veya Undo

\*\* - TextBox'ı seçin; (ör. Text1)

System Dizinini Bulmak

Örneğin INI dosyalarını kullanan bir uygulama yazdığınızda, çoğunlukla \System dizinine ihtiyaç duyarsınız. Genellikle bu dizinin yolu "C:\Windows\System\" şeklindedir.

Fakat bazı kullanıcılar windows'u farklı sürücü veya dizine kurabilirler. Ve işte bu sorunu çözmek için kullanacağınız kod aşağıda.

Bu kodu bir Module'nin declarations section kısmına kopyalayın:

```vbnet
Declare Function GetSystemDirectory Lib "Kernel32" Alias "GetSystemDirectoryA" (ByVal lpBuffer As String, ByVal nSize As Long) As Long

Function VBSysDir() As String
Dim Gwdvar As String, Gwdvar_Length As Integer
Gwdvar = Space(255)
Gwdvar_Length = GetSystemDirectory(Gwdvar, 255)
VBSysDir = Left(Gwdvar, Gwdvar_Length)
End Function
```

Daha sonra aşağıdaki kodu kullanarak \System dizininin yolunu bulabilirsiniz:

```vbnet
MsgBox VBSysDir & " is the System Directory", vbInformation, "System Directory"
```

Hızlı Form

Move methodunun, Left ve Top ayarlarından %45 daha hızlı çalıştığını biliyormuydunuz? Özellikle yavaş sistemlerde çok işe yarıyor.

Move methodu için kullanacağınız kod aşağıda:

```vbnet
Sub ...
Form.Move x, y
End Sub...
```

Bu kadar kolay.

Tüm Formlar Kapansın

Çok sayıda açık form içeren uygulamalardaki tüm formları bir kerede kapatmak mı istiyorsunuz. İşte aşağıda bu işi yapan kod parçası.

```vbnet
Public Sub UnloadAllForms(sFormName As String)
Dim Form As Form
For Each Form In Forms
If Form.Name <> sFormName Then
Unload Form
Set Form = Nothing
End If
Next Form
End Sub
```

Aşağıdaki kodu Ana formunuzun Form_Unload olayına yerleştirin.

```vbnet
Call UnloadAllForms Me.Name
```

Tüm TextBox'lar Temizlensin

Bazen bir form üzerindeki tüm textboxları temizlemek zorunda kalırsınız. İşte aşağıda bunu yapmak için kullanacağınız kod.

```vbnet
Sub ClearAllTextBoxes(frmTarget As Form)
For i = 0 To (frmTarget.Controls.Count - 1)
Set ctrlTarget = frmTarget.Controls(i)
'If it's a textbox, clear it
If TypeOf ctrlTarget Is TextBox Then
ctrlTarget.Text = ""
End If
Next i
End Sub
```

Aşağıdaki kodu da örneğin bir komut butonunun Click olayına yerleştirerek textboxları temizleyebilirsiniz.

```vbnet
ClearAllTextBoxes FormName
```

Dosya Kopyalamak

Aşağıdaki kod parçası da yüzde ölçüsünü kullanarak dosya kopyalamaya yarıyor. Göze güzel görünen uygulamalar yapmak için iyi bir şey.

```vbnet
Function CopyFile (src As String, dst As String) As Single
'L. Serflaten 1996
Static Buf$
Dim BTest!, FSize!
Dim Chunk%, F1%, F2%
Const BUFSIZE = 1024
'This routine will copy a file while providing a means
'to support a percent gauge. Ex. your display routine
'is called "PercentDone" and accepts the values 0-100.
'Error support is provided.
'
'A larger BUFSIZE is best, but do not attempt to exceed
'64 K (60000 would be fine)
'
'The size of the copied file is returned on success
'0 is returned on failure
If Dir(src) = "" Then MsgBox "File not found": Exit Function
If Len(Dir(dst)) Then
If MsgBox(UCase(dst) & Chr(13) & Chr(10) & "File exists. Overwrite?", 4) <> 6 Then Exit Function
Kill dst
End If
On Error GoTo FileCopyError
F1 = FreeFile
Open src For Binary As F1
F2 = FreeFile
Open dst For Binary As F2
FSize = LOF(F1)
BTest = FSize - LOF(F2)
Do
If BTest < BUFSIZE Then
Chunk = BTest
Else
Chunk = BUFSIZE
End If
Buf = String(Chunk, " ")
Get F1, , Buf
Put F2, , Buf
BTest = FSize - LOF(F2)
' __Call percent display here__
'PercentDone ( 100 - Int(100 * BTest/FSize) )
Loop Until BTest = 0
Close F1
Close F2
CopyFile = FSize
Exit Function
FileCopyError:
MsgBox "Copy Error!"
Close F1
Close F2
Exit Function
End Function
```

Önce formunuza bir ProgressBar kontrolü ekleyip ardından aşağıdaki kodu kullanarak dosya kopyalayabilirsiniz.

```vbnet
ProgressBar1.Value = CopyFile (Which_File*, To_Where**)
```

\* = Kopyalanacak dosya

\*\* = Kopyalanacağı yer

Dosya Adını Çıkarmak

Bazen full path'i olan bir dosyanın (ör: C:\windows\hello.txt) sadece dosya adı (hello.txt) gerekebilir. İşte onu aradan çıkarmak için aşağıdaki kodu kullanabilirsiniz.

```vbnet
Function StripPath(T$) As String
Dim x%, ct%
StripPath$ = T$
x% = InStr(T$, "\")
Do While x%
ct% = x%
x% = InStr(ct% + 1, T$, "\")
Loop
If ct% > 0 Then StripPath$ = Mid$(T$, ct% + 1)
End Function
```

Aşağıdaki kodu kullanarakta dosya adını File değişkenine aktarabilirsiniz.

```vbnet
File = StripPath("c:\windows\hello.txt")
```

NotePad'ı Çalıştırmak

Bazen yazdığınız uygulamanın Readme dosyasını görüntülemek için Not defterini çalıştırmak kullanışlı olur.

1. Formun üzerine bir CommandButton yerleştirin.

2. Aşağıdaki kodu formun Declarations Section bölümüne kopyalayın.

```vbnet
Private Declare Function CreateProcess Lib "kernel32" Alias "CreateProcessA" (ByVal lpApplicationName As String, ByVal lpCommandLine As String,
lpProcessAttributes As Any, lpThreadAttributes As Any, ByVal bInheritHandles As Long, ByVal dwCreationFlags As Long, lpEnvironment As Any, ByVal lpCurrentDriectory As String,
lpStartupInfo As STARTUPINFO, lpProcessInformation As PROCESS_INFORMATION) As Long
Private Declare Function OpenProcess Lib "kernel32.dll" (ByVal dwAccess As Long, ByVal fInherit As Integer, ByVal hObject As Long) As Long
Private Declare Function TerminateProcess Lib "kernel32" (ByVal hProcess As Long, ByVal uExitCode As Long) As Long
Private Declare Function CloseHandle Lib "kernel32" (ByVal hObject As Long) As Long
Const SYNCHRONIZE = 1048576
Const NORMAL_PRIORITY_CLASS = &H20&
Private Type PROCESS_INFORMATION
hProcess As Long
hThread As Long
dwProcessId As Long
dwThreadId As Long
End Type
Private Type STARTUPINFO
cb As Long
lpReserved As String
lpDesktop As String
lpTitle As String
dwX As Long
dwY As Long
dwXSize As Long
dwYSize As Long
dwXCountChars As Long
dwYCountChars As Long
dwFillAttribute As Long
dwFlags As Long
wShowWindow As Integer
cbReserved2 As Integer
lpReserved2 As Long
hStdInput As Long
hStdOutput As Long
hStdError As Long
End Type
```

3. Şimdi, aşağıdaki kodu da Command1_Click olayına kopyalayın:

```vbnet
Dim pInfo As PROCESS_INFORMATION
Dim sInfo As STARTUPINFO
Dim sNull As String
sInfo.cb = Len(sInfo)
success& = CreateProcess(sNull, "notepad.exe e:\anexis\vbpage\vbisland.html", ByVal 0&, ByVal 0&, 1&, NORMAL_PRIORITY_CLASS, ByVal 0&, sNull, sInfo, pInfo)
MsgBox "Notepad has been started. Click OK to end it."
ret& = TerminateProcess(pInfo.hProcess, 0&)
ret& = CloseHandle(pInfo.hThread)
ret& = CloseHandle(pInfo.hProcess)
MsgBox "Notepad has been shut down.
```

4. F5 basarak uygulamayı çalıştırın.

Windows Kapansın

Bu kod setup programlarında sistemi resetlemek istediğiniz zaman kullanışlı olur. İşte aşağıdaki kodu kullanarak bu işi kolaylıkla yapabilirsiniz.

1. Aşağıdaki kodu bir formun Declarations section bölümüne kopyalayın:

```vbnet
Const EWX_LogOff As Long = 0
Declare Function ExitWindows Lib "User32" Alias "ExitWindowsEx" (ByVal dwOptions As Long, ByVal dwReserved As Long) As Long
```

2. Aşağıdaki kodu da bir nesnenin olayına kopyalayın (ör: Command1_Click):

```vbnet
ExitWindows EWX_LogOff, &HFFFFFFFF
```

Not: Bu kod sadece Exe dosyasından çalışır. Eğer VBasic içinden çalıştırırsanız tüm programlarınızı kapatın.

Ses Kartı Var mı?

Şimdi bir çok programda bir olay gerçekleştiğinde küçük sesler duyuluyor. Eğer sizde böyle bir şey yapmak için sisteminizde ses kartı olup olmadığını öğrenmek istiyorsanız aşağıdaki kodu kullanabilirsiniz.

Denemek için aşağıdaki kodu bir Modulenin içine kopyalayın.:

```vbnet
Declare Function waveOutGetNumDevs Lib "winmm.dll" Alias "waveOutGetNumDevs" () As Long
```

Bu kodu da formunuzun Form_Load olayı altına kopyalayın:

```vbnet
Dim i As Integer
i = waveOutGetNumDevs()
If i > 0 Then
MsgBox "Your system supports a sound card.", vbInformation, "Sound Test"
Else
MsgBox "Your system cannot play Sound Blaster Files.", vbInformation, "Sound Test"
End If
```

Şimdi F5 tuşuna basarak kodu deneyebilirsiniz.

Textbox Popup Menüleri Çıkmasın

Bildiğiniz gibi textboxların üzerinde sağ tuşa bastığınızda bir Popup Menu çıkar. Bunun çıkmasını istemiyorsanız aşağıdaki kodu kullanabilirsiniz.

Kodu formun General Declarations bölümüne kopyalayın:

```vbnet
Sub Text1_MouseDown
if button=2 then
text1.enabled=false
popupmenu <MENUNAME>
text1.enabled=true
text1.setfocus
end if
End Sub
```

Dosya Uzantısını Bulmak

Aşağıdaki fonksiyon bir dosyanın uzantısını döndürüyor.

```vbnet
Function GetExtension(Filename As String)
Dim PthPos, ExtPos As Integer
For i = Len(Filename) To 1 Step -1 ' Go from the Length of the filename, to the first character by 1.
If Mid(Filename, i, 1) = "." Then ' If the current position is '.' then...
ExtPos = i ' ...Change the ExtPos to the number.
For j = Len(Filename) To 1 Step -1 ' Do the Same...
If Mid(Filename, j, 1) = "\" Then ' ...but for '\'.
PthPos = j ' Change the PthPos to the number.
Exit For ' Since we found it, don't search any more.
End If
Next j
Exit For ' Since we found it, don't search any more.
End If
Next i
If PthPos > ExtPos Then
Exit Function ' No extension.
Else
If ExtPos = 0 Then Exit Function ' If there is not extension, then exit sub.
GetExtension = Mid(Filename, ExtPos + 1, Len(Filename) - ExtPos) 'Messagebox the Extension
End If
End Function
```

Fonksiyonu aşağıdaki gibi çağırabilirsiniz.

```vbnet
FileExt = GetExtension("c:\windows\vb\vb.exe")
```

Dosya Taşımak

Bazı kişiler dosyayı taşımanın kopyalamaktan daha kolay olduğunu düşünürler. E gerçektende öyle ama bu yaptığımız işe bağlı. Neyse aşağıdaki kodu kullanarak dosya taşıyabilirsiniz.

```vbnet
Name "File to move" As "Filename To move it as"
```

Task Bar'ı Gizlemek

Windows95 Taskbarı saklayıp, geri getirmek için bir çözüm yolu var. Aşağıdaki kodu kullanarak bu işi kolaylıkla yapabilirsiniz.

Önce, aşağıdaki kodu formun General Declarations bölümüne kopyalayın:

```vbnet
Dim hWnd1 As Long
Private Declare Function FindWindow Lib "user32" Alias "FindWindowA" (ByVal lpClassName As String, ByVal lpWindowName As String) As Long
Private Declare Function SetWindowPos Lib "user32"
(ByVal hwnd As Long, ByVal hWndInsertAfter As Long, ByVal x As Long, ByVal y As Long, ByVal cx As Long, ByVal cy As Long, ByVal wFlags As Long) As Long
Const SWP_HIDEWINDOW = &H80
Const SWP_SHOWWINDOW = &H40
```

Saklamak için aşağıdaki kodu kullanın:

```vbnet
hWnd1 = FindWindow("Shell_traywnd", "")
Call SetWindowPos(hwnd1, 0, 0, 0, 0, 0, SWP_HIDEWINDOW)
```

ve görüntülemek içinde aşağıdakini kullanın:

```vbnet
Call SetWindowPos(hwnd1, 0, 0, 0, 0, 0, SWP_SHOWWINDOW)
```

Masaüstü İkonlarını Dizmek

Aşağıdaki kod aktiv desktop ta bulunan ikonları düzenliyor.

Önce, Bu kodu bir formun General Declarations bölümüne kopyalayın:

```vbnet
Private Declare Function GetWindow Lib "user32" (ByVal hwnd As Long, ByVal wCmd As Long) As Long
Private Declare Function SendMessage Lib "user32" Alias "SendMessageA" (ByVal hwnd As Long, ByVal wMsg As Long, ByVal wParam As Long, lParam As Long) As Long
Private Declare Function FindWindow Lib "user32" Alias "FindWindowA" (ByVal lpClassName As String, ByVal lpWindowName As String) As Long
Private Const GW_CHILD = 5
Private Const LVA_ALIGNLEFT = &H1
Private Const LVM_ARRANGE = &H1016
```

İkonları düzenlemek için de aşağıdaki kodu kullanın:

```vbnet
Dim hWnd1 As Long
Dim hWnd2 As Long
Dim Ret As Long
hWnd1 = FindWindow("Progman", vbNullString)
hWnd2 = GetWindow(hWnd1, GW_CHILD)
hWnd1 = GetWindow(hWnd2, GW_CHILD)
Ret = SendMessage(hWnd1, LVM_ARRANGE, LVA_ALIGNLEFT, 0)
```

API ile Disket Formatlamak

API kullanarak bir diskete format atmak için aşağıdaki kodu kullanabilirsiniz.

Not: Bu kod harddiske format atabilir, bu nedenle dikkatli olmalısınız.

Önce, Bu kodu bir formun General Declarations bölümüne kopyalayın:

```vbnet
Private Declare Function SHFormatDrive Lib "shell32" _
(ByVal hwnd As Long, ByVal Drive As Long, ByVal fmtID As Long, _
ByVal options As Long) As Long
Private Declare Function GetDriveType Lib "kernel32" Alias _
"GetDriveTypeA" (ByVal nDrive As String) As Long
```

Forma iki CommandButtons ekleyin:

Birincinin adı: "cmdFormatDrive"

İkincinin adı: "cmdDiskCopy"

```vbnet
Private Sub cmdFormatDrive_Click()
Dim DriveLetter$, DriveNumber&, DriveType&
Dim RetVal&, RetFromMsg%
DriveLetter = UCase(Drive1.Drive)
DriveNumber = (Asc(DriveLetter) - 65) ' Change letter to Number: A=0
DriveType = GetDriveType(DriveLetter)
If DriveType = 2 Then 'Floppies, etc
RetVal = SHFormatDrive(Me.hwnd, DriveNumber, 0&, 0&)
Else
RetFromMsg = MsgBox("This drive is NOT a removeable" & vbCrLf & _
"drive! Format this drive?", 276, "SHFormatDrive Example")
Select Case RetFromMsg
Case 6 'Yes
' UnComment to do it...
'RetVal = SHFormatDrive(Me.hwnd, DriveNumber, 0&, 0&)
Case 7 'No
' Do nothing
End Select
End If
End Sub

Private Sub cmdDiskCopy_Click()
' DiskCopyRunDll takes two parameters- From and To
Dim DriveLetter$, DriveNumber&, DriveType&
Dim RetVal&, RetFromMsg&
DriveLetter = UCase(Drive1.Drive)
DriveNumber = (Asc(DriveLetter) - 65)
DriveType = GetDriveType(DriveLetter)
If DriveType = 2 Then 'Floppies, etc
RetVal = Shell("rundll32.exe diskcopy.dll,DiskCopyRunDll " _
& DriveNumber & "," & DriveNumber, 1) 'Notice space after
Else ' Just in case 'DiskCopyRunDll
RetFromMsg = MsgBox("Only floppies can" & vbCrLf & _
"be diskcopied!", 64, "DiskCopy Example")
End If
End Sub
```

Forma birde Drive1 adlı ListDrive ekleyin:

```vbnet
Private Sub Drive1_Change()
Dim DriveLetter$, DriveNumber&, DriveType&
DriveLetter = UCase(Drive1.Drive)
DriveNumber = (Asc(DriveLetter) - 65)
DriveType = GetDriveType(DriveLetter)
If DriveType <> 2 Then 'Floppies, etc
cmdDiskCopy.Enabled = False
Else
cmdDiskCopy.Enabled = True
End If
End Sub
```

Office 97 Araç Çubuğu Yaratmak

Office 97 ile gelen araç çubuğu uygulamaya güzel bir görünüm katıyor. Aslında bunu VBasic ile yapmak içi bir kontrol gelmiyor.

Fakat API fonksiyonlarını ve eski Common Controls ToolBar'ı kullanarak bu tür araç çubukları oluşturmak mümkün.

1. Önce yeni bir proje hazırlayın ve Common Controls ActiveX kontrolünü ekleyin.

2. Bir formun üzerine ToolBar kontrolünü yerleştirin ve butonları oluşturun.

3. Şimdi projeye bir Module yerleştirin ve aşağıdaki kodu modülün General Declarations kısmına yerleştirin:

```vbnet
Public Declare Function FindWindowEx Lib "user32" Alias "FindWindowExA" (ByVal hWnd1 As Long, ByVal hWnd2 As Long, ByVal lpsz1 As String, ByVal lpsz2 As String) As Long
Public Declare Function SendTBMessage Lib "user32" Alias "SendMessageA" (ByVal hwnd As Long, ByVal wMsg As Long, ByVal wParam As Integer, ByVal lParam As Any) As Long
Public Const WM_USER = &H400
Public Const TBSTYLE_FLAT = &H800
Public Const TBSTYLE_TRANSPARENT = &H8000
Public Const TB_SETSTYLE = (WM_USER + 56)
Public Const TB_GETSTYLE = (WM_USER + 57)
Public Sub MakeToolbarFlat(theToolbar As Control)
Dim Res As Long
Dim Style As Long
Style = SendTBMessage(FindWindowEx(theToolbar.hwnd, 0&, "ToolbarWindow32", vbNullString), TB_GETSTYLE, 0&, 0&)
Style = Style Or TBSTYLE_FLAT Or TBSTYLE_TRANSPARENT
Res = SendTBMessage(FindWindowEx(theToolbar.hwnd, 0&, "ToolbarWindow32", vbNullString), TB_SETSTYLE, 0, Style)
theToolbar.Refresh
End Sub
```

4. Aşağıdaki kodları da formun Form_Load olayına kopyalayın:

```vbnet
Call MakeToolbarFlat(Toolbar1)
```

Toolbar1, tabiki ToolBar kontrolünün adı.

Web Sayfası İçin Kısayol Yaratmak

Çoğu kişi bunun nasıl yapılacağını bilmek istiyor. Aslında çok kolay. Aşağıdaki kod varsayılan tarayıcınızı açarak yazmış olduğunuz adresi getirmeye başlar.

Aşağıdaki kodu bir modulenin içine kopyalayın:

```vbnet
Declare Function ShellExecute Lib "shell32.dll" Alias "ShellExecuteA"
(ByVal hwnd As Long, ByVal lpOperation As String, ByVal lpFile As String, ByVal lpParameters As String, ByVal lpDirectory As String, ByVal nShowCmd As Long) As Long
```

---
*Kaynak: `VİSUAL BASİC NEDİR/VİSUAL BASİC NEDİR.txt`*
