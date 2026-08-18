# SQL Notlar

## **Ders 1: Temel Konular**

**Select ** SQL dilinde bilgi gormek almak icin kullanilir

Bu komut herhangibir table olmadan da calisir. Herhangir degere veya global degere bu komut ile bakabiliriz.

Ornek 1: Select ‘merhaba ben cici’

Ornek 2: Select 10000 – 3849

Ornek 3: Select @@version

Tablolardan bilgi gormek icin en basit kullanim sekli asagidaki gibidir.

Select \* from tablo\_adi

“\*” tablodaki tum kolonlarin listelenmesini saglar

Belirli bir kolon gormek istersek o zaman gormek istedigimiz kolonlarin isimlerini yazmaliyiz. Kolon isimleri mutlaka , (virgul) ile ayraclanmalidir.

Select kolonadi1, kolonadi2 from tablo\_adi

Bir tablodan tum bilgileri degil bazi kurallara gore bilgi almak istiyor isek **where **komutunu kullanmaliyiz.

Select kolonadi1, kolonadi2 from tablo\_adi where kisitlamalar

Kisit olarak kullanilacak kosullar ise asagidakiler olabilir

Karsilastirma islemleri icin = > < >= <= <>

Belirli bir aralik icin between , not between

Bir Listeden bakmak icin in , not in

String karsilatimalari icin like , not like

Bilinmeyen degerler icin is null , is not null

Konbinasyonlar icin and , or

Olumsuz not

Ornek 1: Select sKodu from tbStok where sKodu = ‘010101’

Ornek 2: Select sKodu from tbStok where sKodu between ‘100001’ and ‘100001zzz’

Ornek 3: Select sKodu from tbStok where sKodu in ( ‘010101’ , ‘010102’ , ‘zzz’ , ‘0000’)

Ornek 4: Select sKodu from tbStok where sKodu like ‘01%’

Ornek 5: Select sKodu from tbStok where sKodu is not null

Ornek 6: Select sKodu from tbStok where sKodu = ‘010101’ or sKodu = ‘010102’

Kolonlarin adini daha okunabilir yapmak icin degistirbiliriz

Ornek: Select sKodu as \[Stok Kodu\] from tbStok veya Select ‘Stok Kodu’ = sKodu from tbStok

Gelen bilgi belli bir sirada gelmesi isteniyor ise **order by** ozelligi kullanilir.

Ornek: Select sKodu from tbStok order by sKodu

Order by ile siralama yapilirken default kucukten buyuge dogru siralamadir. Buyukten kucuge dogru siralama yapmak icin kolon adinin yanina **desc ** yazilir.

Ornek: Select sKodu from tbStok order by sKodu desc

Select ile raporladigimiz bilgiler uzerinde + , - , / , \* ve % seklinde aritmerik islemler kullanilabilir. ( ) ile de islem onceligi belirlenir.

Ornek : Select sFiyatTipi , lFiyat , (lFiyat \* 14000000) as TL

from tbStokFiyati

where sFiyatTipi = '$'

Select ile raporladigimiz **numerik** bilgilerde MATEMATIK fonksiyonlari kullanilabilir.

Bunlardan birkac tanesi ABS -> mutlak deger , Log -> logaritma , PI -> Pi sayisi vs.

Ornek: Select abs(lGirisMiktar1) from tbStokfisiDetayi

Bu ornekte lGirisMiktari – olsa bile sonucta – isareti kalkar.

Bu fonksiyonlardan en cok kullanilan ROUND fonksiyonudur. Numerik hesaplamalarda yuvarlama islemi yapar. Kullanim Sekli

**round(deger , yuvarlama\_degeri) ** seklindedir. Yuvarlama\_Degeri 0 , 1, 2…seklinde dir. 0 ise ondalik bolumu yuvarlar , 1 ise virgulden sonra 1.basamagi yuvarlar , 2 ise virgulden sonra 2.basamagi yuvarlar vs

Ornek: Select round(( lFiyat / 1.18 ), 0) from tbStokFiyati

Bu ornekte kdv dahil bir fiyattan %18 kdv yi cikartarak kdv haric fiyat bulduk ve virgulden sonraki rakamlari yuvarladik.

Select ile raporladigimiz **alfanumerik ** bilgilerde de bazi fonksiyonlari kullanilabilir. Bunlardan en cok kullanilanlar :

**Rtrim**  sagdaki bosluklari kaldirir

**Ltrim**  soldaki bosluklari kaldirir

**Str**  numerik alanlari alfanumerik olarak degistirir

**Lower ** karakterleri kucuk harfa cevirir

**Upper ** karakterleri buyuk harfe cevirir

**Substring ** secilen alan uzerinden istenilen bir parcayi ayirmak icin kullanilir

**Patindex ** secilen alan uzrinde arana sozcugun baslangic posizyonunu verir

**Space **  istenilen uzunlukta bosluk gonderir.

Ornek1: select Rtrim(sAciklama) from tbStokfisiDetayi

Ornek2: select Ltrim(sAciklama) from tbStokfisiDetayi

Ornek3: select str(lCikisMiktar1) from tbStokfisiDetayi

Ornek4: select lower (sEvIl) from tbMusteri

Ornek5: select upper (sIsIl) from tbMusteri

Ornek6: select substring (sAciklama , 10 , 5) from tbStok

Ornek7: select substring (sAciklama , Patindex(‘%cigdem%’ , sAciklama) , 15 ) from tbStok

Ornek8: select substring(sAdi, 1 , 1) + ‘.’ + space(2) + sSoyadi from tbPersonel

Tarih ve saat icin kullanilan fonksiyonlar da vardir.

**Dateadd (tarihparcasi , sayi , tarih)**  bir tarihe gun, ay, yil vs ekleyerek tarih bulma

**Datediff (tarihparcasi , tarih1, tarih2)**  Iki tarih arasindaki farki bulma

**Datename(tarihparcasi, tarih)**  month secildiginde aylarin isimleri ile gorulebilmesini saglar, digerlerinde degerini getirir

**Datepart(tarihparcasi, tarih)**  Verilen tarihteki secilen alanin degerini verir

**Getdate()** O andaki gecerli tarih ve saati verir

Tarihparcasi neler olabiliyor:

Year

Quarter

Month

Day of year

Day

Week

Weekday

Hour

Minute

Second

Milisecond

Ornek : select dteIslemTarihi , Dateadd(day , 38 , dteIslemTarihi) from tbStokFisidetayi

Ornek : select dteIslemTarihi , dteFisTarihi , DateDiff(day , dteFisTarihi , dteIslemTarihi) from tbStokFisidetayi where sFistipi = ‘FS’

Ornek : select datename(month , dteIslemTarihi ) from tbStokFisidetayi

Ornek : select datepart(week , dteIslemTarihi ) from tbStokFisidetayi

Bir data tipinden baska bir data tipine cevirme yapilmak isteniyor ise convert fonksiyonu kullanilir. Formul asagidaki gibidir :

Convert (datatype\[(uzunluk)\], deger , \[stil\])

Convert islemi tarih sahalarini okunabilir hale getirmek icin cok kullanislidir. Ornegin select dteIslemTarihi from tbStokFisidetayi yazdigimizda gelen cevapta tarih 2002-01-01 00:00:00 formatinda gelecektir. Ama biz 01/01/2002 seklinde gormek istiyor isek :

select convert(char(10), dteIslemTarihi , 103) from tbStokFisidetayi

yazmaliyiz

buradaki 103 ingiliz/fransiz standartidir. Yani bizimde kullandigimiz standart. Burada kullanilabilecek stil numaralari sql help te yazilmistir.

Parasal alanlari virgul ile ayirmak istiyorsa yine convert fonksiyonunu kullanmaliyiz.

Ornek : select convert(char(20), convert(money, lBrutFiyat , 1), 1) from tbStokFisidetayi

**Convert** fonksiyonu gibi calisan baska bir fonksiyonda **cast **fonsiyonudur. Kullanim sekli **cast ( deger as datatype\[(uzunluk)\])** seklindedir. Yukarida yazdigimiz selectin cast ile yazilimi

select convert(char(20), cast(lBrutFiyat as money), 1) from tbStokFisidetayi

Ayni sonucu verir. Cast fonsiyonunda stil yoktur. Stil kullanilacak ise convert kullanmak gerekir.

Bir numerik alan ile bir alfanumerik alani birlestirip bir sonuc elde etmek istiyorsak numerik alani alfanumerik alana convert etmek gerekir.

Ornek : Select 'Stok Adi :' + sAciklama + space(2)+ convert (char(20), lAsgariMiktar) + space(2) + sBirimcinsi1 from tbstok

Tekrarlayan satirlarin birlestirilmesi icin **distinct** kullanilir

Ornek : Select distinct sModel from tbstok

Sadece ilk n satiri listelemek icin **top **kullanilir

Ornek : Select top 20 \* from tbstok

---
*Kaynak: `SQL NOTLAR/Odevsitesi_com_31963.doc` — Cigdem Hiz — 2002*
