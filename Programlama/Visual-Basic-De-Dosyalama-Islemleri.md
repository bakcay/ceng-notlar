# Visual Basic 'De Dosyalama İşlemleri

**12. BÖLÜM**

**VB’DE DOSYALAMA İŞLEMLERİ**

Programda bilgilerin kalıcı olarak saklanabilmesi için diğer dillerde olduğu gibi VB’de de dosya oluşturma komutlarından yararlanılmaktadır. Dosyalar yapılan işe göre iki gruba ayrılırlar:

Rasgele Erişimli Dosyalar

Sıralı Erişimli Dosyalar

12.1. **Dosya Açmak **

```basic
Open “Dosya Adı” [For AçmaModu] [Access ErişimModu] As [#] dosya no[Len=Kayıtuzunluğu]
```

**Dosya Adı :** Açılacak veya oluşturulacak dosyanın adı.

**Açma Modu :** Dosyanın açma modunu belirler. Bu modlar;

**Random :** Dosyadaki her kayıt, kayıtuzunluğu belirlenen uzunluktaki alanlara yazılır. Dosyaya yazılan kayıtlar kayıt uzunluğu ile belirlenen sayıdan küçük de olsa kayıtuzunluğu kadar yer kaplar. Böylece dosyadaki her kaydın uzunluğu ile aynı olacağından dosyada istenen kayda numarası verilerek ulaşılır.

**Binary : **Dosya bu modda açılırsa dosya içerisindeki her karaktere, karakterin numarası verilerek ulaşılır.

**Input : ** Dosya okumak için sıralı erişimli açılır.

**Output : **Dosya okumak için sıralı erişimli okunur.

**Append : **Output ile aynı görevi görür. Ancak dosya göstericisi dosyanın sonunda duracaktır ve yazılan kayıtlar dosyanın sonuna eklenecektir.

Açılmak istenen dosya mevcut değilse Append, Binary, Output veya Random modlarında bu dosya oluşturulur. Yani bir dosyayı Input modunda açabilmek için o dosyanın var olması gerekir. Aksi takdirde hata oluşacaktır.

**ErişimModu:** Dosya açılırken dosyanın ne için açıldığı belirtilebilir. Bu parametre şu üç kelimeden biriyle kullanılır.

**Read : **Dosya sadece okumak için açılır.

**Write : **Dosya sadece okumak için açılır.

**Read Write:** Dosya hem okumak hem de yazmak için açılır.

**Lock: **Dosya açılırken istenilen diğer programların bu dosyaya erişimi engellenebilir.

**Shared:** Açılan dosyaya diğer uygulamalar tarafından okuma ve yazma yapılabilir.

**Read :** Okumaya karşı kilitler. Dosya açık olduğu sürece diğer programlar bu dosyadan okuma yapamazlar.

**Write** : Dosyayı yazmaya karşı kilitler.

**Read Write :** Dosyayı hem yazmaya hem de okumaya karşı kilitler.

**Dosyano:** Dosya açılırken o dosyaya 1 ile 255 arasında bir numara verilir. Bu dosyada yapılan işlemlerde bu numaralar kullanılır. (Get #1 gibi).

**Kayıtuzunluğu:** Dosyanın açım moduna göre bu parametrenin iki farklı anlamı vardır ve 32767 den büyük olamaz. Binary modunda açılan dosyalarda bu parametrenin anlamı yoktur.

Dosya Random modu ile açılmışsa bu sayı her kaydın uzunluğunu belirler. Verilmezse 128 karakter kabul edilir.

Dosya Random modundan farklı bir modda açılmışsa bu sayı karakter harflerinin boyutunu belirler. Verilmezse 512 karakter olarak kabul edilir.

**12.2. Rasgele Erişimli Dosyaya Yazma ve Okuma**

Random ve Binary modu ile açılan dosyalara kayıtlar Put komutu ile yazılır ve Get komutu ile okunur.

**Yazılım:**

```basic
Put [#] dosyano, [kayıtno], değişken
Get [#] dosyano, [kayıtno], değişken
```

**Değişken:** İçeriği yazılacak değişken** .**

**Dosyano:** Yazılacak veya okunacak dosyanın numarası

**Kayıtno:** Yazılacak veya okunacak değişkenin dosya içindeki kayıt numarası.

12.3. **Sıralı Erişimli Dosyaya Yazma ve Okuma**

Output ve Append modu ile açılan dosyalara Write veya Print komutu ile yazma yapışır.

**Write:**

**Yazılım :******

```basic
Write # dosyano [, değişkenler]
```

**Dosyano:** Yazılacak dosyanın numarasıdır. Bu komut Open komutu ile belirlenen dosya numarasıdır.

**Değişkenler:** Dosyaya yazılacak olan değişken listesi araya virgüller konarak yazılır.

**Örnek 12.1 :**

```basic
Dim adi, tel, adres
Open “deneme” For Output As # 1
adi = “Bahadır Işleyen”
tel = “3456432”
adres = “Elektronik-Bilgisayar Bölümü”
Write #1, adi, tel, adres
Close #1
```

**Print: **

**Yazılım:**

```basic
Print # dosyano [, değişken formatı]
```

**Dosyan : **Yazılacak dosyanın numarasıdır. ** **

**Değişken formatı:** Print komutunun dosyaya yazan bu formatı ekrana çıkış yapan Print gibidir.

**Örnek 12.2 :**

```basic
Dim adi, tel, adres
Open “deneme” For Output As # 1
adi = “Bahadır Işleyen”
tel = “3456432”
adres = “Elektronik-Bilgisayar Bölümü”
Print #1, adi, tel, adres
Close #1
```

**Input:**

**Yazılım:******

```basic
Input # dosyano, değişkenlistesi
```

**Dosyano:** Okunacak dosyanın numarasıdır.

**Değişkenlistesi:**Dosyadan okunacak kayıtların atandıkları değişkenlerdir.

**Örnek 12.3 :**

```basic
Dim adi, tel, adres
Open “deneme” For Output As # 1
Input #1, adi, tel, adres
Print “ad=”; adi
Print “telefon=”; tel
Print “adres=”; adres
Close #1
```

**Line Input:**

**Yazılım:**

```basic
Line Input #dosyano, değişken
```

**Dosyano:** Okunacak dosyanın numarası

**Değişken:** Dosyadan Okunacak kaydın aktarılacağı değişken. Bu komut Input komutundan farklı olarak satır sonu karakterlerine kadar olan karakterleri bir kayıt kabul eder ve bu karakterleri değişkene aktarır.

**Örnek 12.4:******

```basic
Dim adi, tel, adres
Open “deneme” For Output As # 1
Line Input #1, adi
Line Input #1, tel
Line Input #1, adres
Print “ad=”; adi
Print “telefon=”; tel
Print “adres=”; adres
Close #1
```

12.4. **Dosyaları Kapatmak **

Hangi modda açılırsa açılsın dosya Close komutu ile numarası verilerek kapatılır.

**Yazılım:**

```basic
Close # dosyano
```

**Not :** Açılacak bütün dosyaları kapatmak için Reset komutu kullanılabilir.

12.5. **Dosya Sonu Kontrolü (EOF)**

Numarası verilen dosyanın sonuna gelinip gelinmediğini kontrol eder.

**Yazılım******

```basic
EOF (dosyano)
```

12.6. **Dosya Boyu Kontrolü (LOF) ******

Numarası verilen dosyanın byte olarak uzunluğunu verir.

**Yazılım**

```basic
LOF(dosyano)
```

12.7. Aktif Kaydı Değiştirmek (Seek)

Dosya içerisinde aktif kaydı veya karakteri gösteren bir gösterici vardır. Kayıt numarası verilmeden yapılan yazma ve okuma işlemleri bu göstergecin bulunduğu yerden yapılır. Yapılan yazma ve okuma işlemleri de göstericiyi okunan veya yazılan kaydın sonuna taşır.

Dosya Random modla açılmışsa bu gösterici kayıt numarasıdır, diğer modlarda açılmış ise bu gösterici dosya içindeki karakterin konumudur.

**Yazılım **

```basic
Seek (doyano)
```

Dosya numarası ile verilen dosyadaki göstericinin konumu öğrenilebilir.

PAGE

PAGE 163

---
*Kaynak: `VİSUAL BASİC 'de DOSYALAMA İŞLEMLERİ/O-d-e-v-s-i-t-e-s-i-com-18966.doc` — BAHADIR ISLEYEN — 1999*
