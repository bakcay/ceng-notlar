# Visual Basic ’De Değişken Tanimlama

**5. BÖLÜM**

**5. VB’DE DEĞİŞKEN TANIMLAMA**

GW ve Quick Basic’te programcı ne zaman bir değişkene gereksinim duyarsa her hangi bir bildiri değimini kullanmadan değişkeni tanımlayıp kullanabilir. Bu değişkene aktarılacak bilgiler, değişkenin adının son karakterine bağlı olarak değişiyordu.

VB’de ise değişken yapısı daha da gelişmiştir. Değişkenler için önemli durum, değişkenlerin karışıklığa meydan vermemesi için tanımlanması mecburiyeti olmasıdır. Daha önceki iki kuşak Basic’te bu mecburiyet yoktur ve değişkenleri benzerlikten dolayı her zaman karıştırmak mümkündür. VB’de değişkenleri kullanmadan önce tanımlama mecburiyeti programcının seçimine bırakılmıştır. Programcı isterse Tools-Options menüsü Require Variable Declaration seçeneğini işaretleyerek derleyicinin tanımlanmamış değişken kullanımda hata mesajı vermesini sağlayabiliriz.

Bir değişken tanımlanırken aşağıdaki kuralları göz önünde bulundurulması gerekir.

Değişken ismi bir harf ile başlamalıdır.

```basic
Ad1, Ad2
```

Değişken isminde boşluk bulunmaz. Bunun yerine alt çizgi karakteri kullanılabilir.

Değişken isminde sadece harfler, rakamlar ve alt çizgi karakterleri bulunabilir.

```basic
Adı_Soyadı, No1
```

Değişkene verilecek isim VB komutlarından oluşmamalıdır.

```basic
Not, Dim, Val ......vs
```

Değişken ismi 255 karakterden fazla olmamalıdır.

**5.1. VB’de Kullanılan Standart Veri Tipleri**

VB’de değişken tipleri Dim değimi ile tanımlanır. Bu değimin yazılımı;

```basic
Dim deg_adı [(Dizi boyutu)] As tipi
```

**deg \_adı :** Tanımlanacak değişkenin ismidir.

**Dizi boyutu :** Değişken dizi olarak tanımlanacaksa dizinin boyutu değişken isminden sonra parantez içine yazılır.

Dim x (5) tanımıyla 6 elemanlı dizi tanımlamış oluruz. Dizinin ilk

elemanı 0 son elemanı 5 dir.

Dim x (3 to 6) tanımıyla ilk elamanı x (3) ve son elamanı x (6)

olan bir dizi tanımlanmıştır.

**Tipi : **Tanımlanacak değişkenin tipi belirlenir. Bunlar ;

**Byte : **1 Baytlık tamsayı tipidir. 0 ile 255 arasında değer alabilir.

**Integer : **2 Baytlık işaretli tamsayı tipidir. –32768 ile 32767 arasında değer alabilir.

**Long : **4 Baytlık işaretli tamsayı tipidir. –2.147.483.648 ile 2. 147.483.647 arasında değer alabilir.

**Not:** Yukarıdaki değişken tiplerine ondalık sayı atanması durumunda sayı en yakın tamsayıya yuvarlatılacaktır. ( x=4,3 ise x= 4 atanır, y=3.6 ise y=4 atanır)

**Single : **4 Baytlık ondalık sayı tipidir. 3.402823 x 1038 ile 1.401298 x 10-45 arasında değer alabilir.

**Double :** 8 Baytlık ondalık sayı tipidir. 1.79769313486232 x 10308 ile 4.94065645841247 x 10-324 arasında değer alabilir.

**Currency :** 8 Baytlık ondalık sayı tipidir. Ancak sayının ondalık kısmı 4 basamaktan fazla olamaz. –92337203685477.5808 ile 922337203685477.5807 arasında değer alabilir.

**Decimal : **14 Baytlık bir sayı tipidir. Bu tipin en önemli özelliği sayıdaki bütün basamakların tutulmasıdır.

**Boolean : **2 Baytlık bir veri tipidir. Sadece True ve False değerleri alabilir.

```basic
Dim ogrenci As Boolen
Ogrenci=True
Ogernci=1 Bu atamaların hepsi aynı işi
Ogernci=100 görür.
```

**String : **Karakter sınırı verilmezse 2 milyar karaktere kadar atama yapılabilen sayısal veri tipidir. +10 bayt yer kaplar. Karakter sayısını sınırlamak için ;

```basic
Dim a As String * sınır yazılır.
Dim a String İstenildiği kadar karakter ataması yapılabilir.
Dim b String * 3 3 tane karakter ataması yapılabilir.
```

**Variant : **VB’de değişken tanımlanırken tip ismi verilmemişse bu tip Variant olarak ele alınır ve değişkenin tipi atanacak değere göre değişir. Variant tipler yukarıdaki tiplerden herhangi biri gibi işleme girebilir ve programın çalışması esnasında değişebilir.

**Date : **8 Baytlık yer kaplayan bu değişken tipi 1/1/100 ile 31/12/9999 arasındaki tarih ve 0:00:00 ile 23:59:59 arasında saat atamaları yapılabilir.

**Object :** 4 Baytlık bir veri tipidir. OLE işlemlerinde kullanılmak amacıyla tasarlanmıştır. Bu tipte değişkenlere atama yapılırken Set operatörü kullanılır.

**5.2. Kullanıcı Tarafından Yeni Tip Tanımlanması******

```basic
Type tip_adı
Deg_adı As tipi
Deg_adı As tipi
.........................
.........................
.........................
End Type
```

Bu sekil de tanımlanan tipte bir değişken tanımlamak için de;

```basic
Dim deg_adı As tip_ismi olarak tanımlanabilir.
```

Tip tanımı bir form içerisinde ancak Private olarak tanımlanabilir. Yani tanımlanan tip sadece o formda kullanılır. Genel yani Public bir tip ise ancak bir modül içerisinde kullanılabilir.

Bir formda tip;

```basic
Private Type Ad
..............
End Type şeklinde tanımlanır.
```

**Örnek 5.1:**

```basic
Type Rehber
Ad As String
Soyadı As String
Tel As Integer
Adres As String
End Type
```

Burada Rehber değişkenini değil Rehber tipini tanımladık. Artık Rehber yapısındaki değişkenleri tanımlayabiliriz.

```basic
Dim adı As Rehber şeklinde tanımlayabiliriz.
```

Bu değişkene değer atamak için “.” operatörünü kullanalım ;

```basic
Adı.Ad = “Bahadır”
```

**5.2.1. Enum**

```basic
Enum Tip İsmi
Elemen1=Sayı1
Eleman2=Sayı2
........................
Eleman3=SayıN
End Enum
```

Bu tip her bölüme bir numara verir. VB bu bölümü bir sayı olarak kullanmasına rağmen bunu bir string gibi kullanma imkanı verir.

**Örnek 5.2:**

```basic
Enum bolum
Bilgisayar=1
Elektronik=2
Makine=3
Metal=4
Yapı=5
YapıRes=6
End Enum
```

Tanımını yaptıktan sonra bolum tipinde değişkenler tanımlayarak bu değişkenlere değer atamak mümkündür.

```basic
Dim eğitim As bolum
Bolum=Bilgisayar
```

Satırı ile bolum değişkenine Bilgisayar atamaktayız. Bu işlem eğitim=1 satırı ile aynı işi yapmasına karşın anlaşılması daha kolaydır.

**5.3. Dinamik Dizi Tanımlama**

** **Programda tanımlanacak dizinin boyutu her zaman belli olmayabilir. Bu durumda diziyi dinamik olarak tanımlamamız gerekir. Diziyi dinamik olarak tanımlayabilmek için ReDim değimi kullanılır. Diziyi dinamik olarak tanımlamak demek dizinin boyunun ihtiyaç olduğunda artırılması veya azaltılması demektir. Üstelik dizinin eski halini koruyarak.

```basic
ReDim [Preserve] deg_adı (dizi boyutu] As tipi
```

ReDim ile dizin ilk defa tanımlanacağı gibi yine ReDim’le tanımlanmış dizinin boyutunu değiştirmek için de kullanılabilir. Burada Dim’den farklı olarak Preserve parametresi vardır.

Preserve, dizinin yeniden boyutlandırılması durumunda dizide bulunan elaman içeriklerini yeni dizide de bulunmasını sağlar.

Tanımlanacak dizi local bir dizi olmayacaksa dizi öncelikle Dim veya Global değimiyle aşağıdaki gibi tanımlanmalıdır.

```basic
Dim deg_adı () As tipi
```

Görüldüğü dizi tanımlanırken parantez içerisinde dizi boyutu verilmemiştir. Bu VB’ye dizinin dinamik olarak tanımlanacağını belirtecektir. Daha sonra dizinin elaman sayısı ReDim değimi kullanılarak belirlenir.

```basic
Private Type takip
Ad As String * 25
Soyad As String * 25
Sınıfı As String * 2
No As String *6
End Type

Dim Ogr () As takip “Diziyi dinamik olarak tanımla
Dim dizi_boyu As Integer ‘En son tanımlanan dizinin boyutu
Dim eleman_say As Integer ‘Dizideki son eleman indeksi
```

**5.4. Global ve Local Değişkenler **

** **Global değişkenler programın bütün fonksiyonları kullanılabilen değişkenlerdir. Local değişkenler ise sadece tanımlandıkları fonksiyonda kullanılabilirler.

Dim değimi ile yapılan tanımlamalar yerine Global ve Local’dır. Dim ile tanımlana değişkenler;

General-Declarations kısmında tanımlanmışsa modül veya form içerisinde Global’dır. Buna VB’de Modüle Level denir.

Bir fonksiyon veya alt programda tanımlanmışsa Local’dır. Sadece o prosedür tarafından kullanılabilir.

Bir formun General Declarations kısmında Public değimi ile tanımlanmışsa diğer modüller ve formlarda bu değişkeni kullanabilirler. Ancak değişkenin isminden önce modülün/formun ismini vermesi gerekir.

```basic
Form1 . x = 4
```

Bir değişkeni programın her tarafında kullanılacak şekilde tam olarak global tanımlamak için o değişkeni bir modülün General-Declaration kısmında Public değimi ile tanımlamak gerekir.

```basic
Public x
```

Local değişkenlerin önemli bir avantajı bellekte fazladan yer işgal

etmemeleridir (Static olarak kullanılmamışlarsa). Global değişkenler program çalıştığı sürece bellekte tutulmalarına rağmen local değişkenler, değişkenin bulunduğu fonksiyona girince değişken belleğe alınır ve fonksiyonun çalışması bitince bellekten atılır.

**5.5. Static Değişkenler**

Local olarak tanımlanan bir değişken tanımlandığı alt program veya fonksiyonun çalışması bittikten sonra bellekten atılır. İlgili prosedür ikinci kez çalıştırıldığında Local değişkenler eski değerlerinden değil baştan başlarlar.(string ise “ ”, sayı ise 0 )

Local olarak tanımlanan bir değişkenin değerinin tanımlandığı alt program veya fonksiyonun çalışması bittikten sonra da değerinin korunması isteniyorsa Dim yerne Static değimiyle tanımlama yapılır. Static değimi bir alt program veya fonksiyon altında tanımlanabilir:

```basic
Static deg_adı [(dizi boyutu)] As tipi
```

**5.6. Sabit Tanımlama******

Programda değerlerinin değişmesi istenmeyen değerler sabit olarak tanımlanır. VB sabit tanımlama;

```basic
Cost Sabit ismi=Değeri
```

**Örnek 5.3:**

```basic
Cost PI=3.1415
```

**5.7. Değişkenlere İlk Değer Ataması**

Local değişkenlere ilk değer ataması şu şekildedir.

Dim değimiyle ile tip ismi kullanılmadan yapılan tanımlamalarda ilk değer ataması direk olarak tanımın yapıldığı satırda yapılabilir.

```basic
Dim x=5, y=10
```

Tip ismi kullanılarak yapılan tanımlamalarda ise ikinci bir satırda ilk değer ataması yapılır.

```basic
Dim x As Integer
x=5
```

Global olarak tanımlanan değişkene ilk değer ataması Declarations kısmında yapılır ve burası bir alt program değildir. Dolayısıyla Global olarak tanımladığımız değişkenlerimize ilk değer atamasını Form\_Load veya projenin çalışmaya başladığı alt program altında yapmalıyız.

Static değişkenlere de ilk değer ataması IsEmpty () fonksiyonu ile yapılır. Bu fonksiyon bir değişkene değer atanıp atanmadığını kontrol eder. Verilen değişkene değer ataması yapılmamışsa fonksiyondan geri dönen değer TRUE’dir. Fonksiyonun bu özelliğinden yararlanarak static olarak tanımlanan değişkene daha önce değer atanıp atanmadığını yani ilk defamı kullanıldığını öğrenebiliriz.

```basic
Static i;
If IsEmpty(i) then i=5
```

Böylece alt program ilk defa çalıştığında i’ye her hangi bir değer ataması olmadığı için şartımız çalışacak ve ilk değer atanacaktır. Alt programın sonraki seferlerde çalışması durumunda ise i’nin static olmasından dolayı atanmış bir değer olacak ve şartımız çalışmayacaktır. Böylece sadece alt program ilk defa çalıştığında ilk değerimizi atamış olacağız.

VB’de bir diziye değer ataması da değişkeni Variant olarak tanımladıktan sonra Array fonksiyonu ile o değişkenin bir dizi olduğunu belirtmek ve ilk değer atamak mümkündür.

```basic
Dim Dizi [As Variant]
Dizi=Arrray(eleman)
```

**Örnek5.4:**

```basic
Dim gün
Gün= Array(“Pazar”, “Pazartesi”, “Salı”, “Çarşamba”, “Perşembe”, “Cuma”, “Cumartesi”)
```

**5.8.Kullanılan Değişkenlerin Tipini Belirlemek**

Tipi belirtilmeyen Variant tipi değişkenlere programın işletimi sırasında istenen tipteki bilgi aktarılabilir. VarType fonksiyonu ile Variant bir değişkenin hangi tipte bilgi içerdiği öğrenilebilir.

```basic
VarType (Variant Değişken Adı)
```

Yazılımında da görüldüğü gibi bu fonksiyon dışarıdan içerdiği bilginin tipi öğrenilmek istenen değişkenin adını almaktadır. Geriye ise değişkenin içerdiği bilginin tipini temsil eden sayısal bir değeri döndürmektedir. Eğer Variant değişken karaktersel bilgi içeriyorsa VarType() fonksiyonu geriye 8 sayısal değerini döndürür. VarType fonksiyonu ile döndürülecek sayısal değer ve bu değerlerin temsil ettikleri veri tipleri aşağıdaki tabloda verilmiştir.

| Veri Tipi | Sayısal Değer |
| --- | --- |
| Boş-Empty | 0 |
| Null | 1 |
| Integer | 2 |
| Long | 3 |
| Single | 4 |
| Double | 5 |
| Currency | 6 |
| Date | 7 |
| String | 8 |
| Object | 9 |
| Error | 10 |
| Boolen | 11 |
| Variant | 12 |
| Data Object | 13 |

Tablo-5.1. Veri Tipleri

**5.9. Tip Değiştirme İşlemleri**

**Ccur(ifade): **Parantez içinde verilen ifadeyi Currency tipine dönüştürür.

**CDbl(ifade):** Parantez içinde verilen ifadeyi Double tipine dönüştürür.

**CInt(ifade):** Parantez içinde verilen ifadeyi Integer tipine dönüştürür.

**CLng(ifade): **Parantez içinde verilen ifadeyi Long tipine dönüştürür.

**CSng(ifade):** Parantez içinde verilen ifadeyi Single tipine dönüştürür.

**CVar(ifade):** Parantez içinde verilen ifadeyi Variant tipine dönüştürür.

**CBool(ifade):** Parantez içinde verilen ifadeyi Boolen tipine dönüştürür.

**CByte(ifade): **Parantez içinde verilen ifadeyi Byte tipine dönüştürür.

**CDec(ifade):** Parantez içinde verilen ifadeyi Decimal tipine dönüştürür.

**CDate(ifade): **Parantez içinde verilen ifadeyi Date tipine dönüştürür. İki tarih arasında işlem yapabilmek için bu dönüşüm kullanılır.

**5.10. Değişkenlerle İlgili Komutlar**

**5.10.1. IsDate **

** **Değişkenin içeriği geçerli bir tarih ise geri dönen tarih True, değilse False’dir kabul edilen tarih formatı Windows’da tanımlanan formattır.

```basic
IsDate (değişken)
```

**Örnek 5.4:**

```basic
Dim a
a=IsDate(“30/02/1999”) ‘ Verilen tarih geçerli değildir. A=True (Şubat ayı 29 gündür.
a=IsDate(“13bfg”) ‘Verilen tarih geçerli değildir. A=False
```

**5.10.2. IsNumeric **

** **Verilen değişkenin içeriğinin bir sayı olup olmadığını kontrol eder. Değişkenin içeriği sayı ise geri dönen değer True değilse False’dir.

```basic
IsNumeric(değişken)
```

**5.10.3. IsArray**

** **Girilen değişken bir dizi ise True değilse falese üretir. Yani bir değişkenin dizi olup olamadığını öğrenmek için kullanılır.

```basic
IsArray(değişken)
```

**5.10.4. IsEmpty**

Tanımlanmış bir değişkene henüz bir değer atanmamışsa o değişken Empty’dir. Bir değişkene değer atanıp atanmadığını öğrenmek için kullanılır. Dönen değer False ise değişkene bir atama yapılmıştır.

```basic
IsEmpty (Değişken)
```

**5.10.5. IsMissing **

** **VB’de fonksiyon veya alt programlara giriş parametresi olarak Optional değimi kullanılırsa o parametre kullanılmadan da o fonksiyon çağrılabilir. IsMissing fonksiyonu bu tip parametrelerin verilip verilmediğini kontrol etmek için kullanılır.

```basic
IsMissing (Değişken)
```

**5.10.6. IsObject **

** **Verilen değişkenin tipi Object tipinde ise fonksiyondan geriye True değeri döner.

```basic
IsObject (Değişken)
```

**5.10.7. Erase **

İsmi verilen diziyi siler.

```basic
Erase Diziismi
```

PAGE 10

PAGE 72

---
*Kaynak: `VISUAL BASİC ’DE DEĞİŞKEN TANIMLAMA/VB’DE DEĞİŞKEN TANIMLAMA.doc` — BAHADIR — 2004*
