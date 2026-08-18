# API Nedir

**API Nedir? ******

İşletim sistemlerine duyulan ihtiyaçlardan biri standart olarak her program tarafından yapılması gereken şeyleri ortak bir çatı altında toplamak ve programları sistemde belirli kurallar altında çalışmasını sağlamaktır. İşletim sistemlerinin değerini anlamak için işletim sistemi olmayan bir bilgisayar düşünün.

Yaptığınız programları diske kaydetme ihtiyacınız var. İşletim sisteminiz yoksa programlarınızı diske yazacak ve okuyacak assembly kodları sizin yazmanız gerekecektir. Ve her program diske yazma ve okuma kodlarını içinde bulundurmak zorunda olacaktır. Ayrıca diske yazacağınız programı diskin neresine yazacaksınız. Tabi ki herkes kendi programının başa yazılmasını isteyecektir. Bu da diski paylaşım sorununu çıkaracaktır. Ayrıca yazıcı için de problem vardır. Her yazıcı aynı sistemle çalışmayacağı için programınızda yazdırma işlemleri de varsa belli başlı yazıcı tipleri için gerekli kodları yazmanız gerekecektir. Bu örnekler çoğaltılabilir.

İşte PC'ler ilk çıktığında disk işlemlerini kolaylaştırmak için DOS ta piyasaya çıktı. DOS disk işlemlerini yapmak için yazılım interruptlarını programcıların hizmetine sunmuştu. Diskle ilgili bir işleminiz için INT X'in Y numaralı servisini çağırıyordunuz ve bu işlemleri sizin yerinize DOS yapıyordu. Sistemler geliştikçe bilgisayar değişik alanlara da hitap etmeye başlayınca çok değişik arabirimler de çıktı. DOS'a grafik, yazıcı işlemleri gibi standart işlemler de eklendi ve sistemde bulunan standart donanımların hemen hemen hepsine DOS veya BIOS interruptlarıyla erişebiliyordunuz. Ayrıca DOS programların belleği nasıl kullanacağını da belirliyordu. DOS işletim sistemi olarak kullanıcıya herhangi bir standart arabirim sunmamıştır. Sadece programların sistemdeki standart donanımlara ulaşabilecekleri kodları kullanıcıya sunmuştur. DOS'ta yapılan programların hiçbiri bir birine benzemez. Her program kendi kullanıcı arayüzünü belirlemek zorundadır ve bunun için gerekli kodu kendisi yazmak zorundadır. DOS'ta yapılan programların kullanım ve programlanmasının zorluğu da bir ölçüde buradan kaynaklanır.

DOS'un programlara standart bir arabirim sunmaması, bellek sınırlarının olması gibi sebeplerden dolayı çok çok geç kalmış olsada Windows çıktı. Windows DOS'un sağladığı standart donanıma ulaşma haricinde Ses kartları, Gelişmiş yazıcılar, Scanner'ler gibi donanımların kullanımını da programların kullanımına sunar. Ayrıca programlara standart arabirimleri (Diyalog kutuları, Formlar, Kontroller gibi) kullanma imkanı da sunmuştur. DOS kendi servislerini yazılım interruptlarıyla sunarken Windows API'lerle sunar.

Şimdi şöyle bir şey düşünülebilir. DOS'ta çok program yaptım ama diske birşey yazdırmak için DOS'un interruptlarını kullanmaya hiç ihtiyaç duymadım. Evet eğer assembly program yazmadıysanız bunlara da ihtiyacınız yoktur. Çünkü kullandığınız programlama dili bu işi sizin yerinize yapıyordu. Bu VB'de yaptığınız programlarda da böyledir. API kullanacaksınız diye bir şart yok VB bunları sizin yerinize kullanır. Ancak DOS'taki programlama dillerinde olduğu gibi VB'de de programlama dilinin sunduğu işlemler her zaman işinizi görmeyebilir, bu durumda Windows API'lerini kullanma ihtiyacı duyarsınız.

Basic herhalde bütün zamanların en yavaş programlar üreten dili olma özelliğini kimseye kaptırmak istemiyor. Quick Basicte yaptığınız bir program, aynı işi yapan C ile yapılmış programdan en az 5 kat daha yavaş çalışacaktır. Bu fark GWBasic'te daha da büyüktür. VB'de de durumun iç açıcı olduğunu iddia etmek çok güç. Programlarınızda API kullanmanız bu hız barajlarını aşmanızı sağlayacaktır. Ayrıca VB'nin sunmadığı bazı işlemler için de API kullanmak gerekir. Örneğin sistemdeki boş bellek miktarını verecek herhangi bir komut VB'de bulunmaz bunu da yine API kullanarak öğrenmek zorundasınız.

Windows'un sunduğu bu API'ler gruplandırılarak bir çok DLL ve EXE dosyasına konmuştur. VB'de kullanılan OCX dosyalarında da API'ler bulunabilir. Bu API'lerden birini kullandığınızda API'nin bulunduğu DLL sisteme daha önce yüklenmemişse önce bu DLL yüklenir ve API çalıştırılır.

Programınızda API kullanmak için Declare deyimiyle API'yi tanımlamanız gerekir. Bu tanımdan sonra tanımladığınız API'ye bir fonksiyon veya bir altprogram gibi ulaşabilirsiniz.

**VB'de API Tanımı ******

VB'de API'ler iki şekilde tanımlanabilir. Fonksiyon veya altprogram olarak. Fonksiyon olarak tanımlanan API'lerden geriye bir değer dönerken, altprogram olarak tanımlananlardan bir değer geri dönmez.

Alt program olarak API tanımı:

Private/Public Declare Sub isim Lib "libname" \[(\[parametreler\])\]

Fonksiyon program olarak API tanımı:

Private/Public Declare Function isim Lib libname \[(\[parametreler\])\] \[As tip\]

Burada isim fonksiyonun ismidir ve programda API bu isimle çağrılır. Libname kullanılan kütüphanenin ismi, parametreler; fonksiyona giren parametreler, As tip; fonksiyondan dönen değerin tipidir.

API'nin tanımlanacağı yer formun veya modülün General-Declerations kısmıdır. API'yi bir formun decleration kısmında tanımlarsanız API'yi yalnız o formun altprogramlarından çağırabilirsiniz. Bir modülde tanımlarsanız programınızın her yerinde kullanabilirsiniz.

API'yi doğru olarak tanımladığınız halde VB, ilgili dosyada böyle bir API bulunmadığını söylüyorsa veya API ile aynı isme sahip bir VB komutu var ise bu durumda Alias isimleri kullanmanız gerekir.

Private/Public Declare Function/Sub isim Lib libname Alias "isim" \[(\[parametreler\])\] \[As tip\]

API'yi doğru olarak tanımladığınız halde VB, ilgili dosyada böyle bir API bulunmadığını söylüyorsa API isminin sonuna A ekleyerek Alias ismi olarak vermeniz gerekir. Bunun sebebi Windows işletim sisitemi farklı dilleri desteklemektedir. ANSI karakter setini destekleyen ülkler için sonuna A harfi, UniCode veya iki karekter genişliğini kullanan ülke seti için ise sonuna W harfi eklemeniz gerekir.

API tanımı yaparken kullanacağınız tiplerin isimlerini ise C'den VB'ye çevirmeniz gerekir. Genel olarak tip karşılıkları şöyledir.

| PRIVATE | **C ****** | **Visual Basic ****** |
| --- | --- | --- |
|  | atom | ByVal değişken AS integer |
|  | bool | ByVal değişken As Long |
|  | byte | ByVal değişken As Byte |
|  | char | ByVal değişken As Byte |
|  | colorref | ByVal değişken As Long |
|  | dword | ByVal değişken As Long |
|  | hwnd,hdc,hmenu vb | ByVal değişken As Long |
|  | int,uint | ByVal değişken As Long |
|  | long | ByVal değişken As Long |
|  | lparam | ByVal değişken As Long |
|  | lpdword | değişken As Long |
|  | lpint,lpuint | değişken As Long |
|  | Iprect | değişken As type |
|  | Ipstr,Ipcstr | ByVal değişken As String |
|  | Ipvoid | değişken As Any |
|  | lpword | değişken As Integer |
|  | lresult | ByVal değişken As Long |
|  | null | değişken As Any veya ByVal değişken As Long |
|  | short | ByVal değişken As Integer |
|  | void | Sub procedure |
|  | word | ByVal değişken As Integer |
|  | wparam | ByVal değişken As Long |
|  | 16 bit | ByVal değişken As Integer |
|  | 32 bit | ByVal değişken As Long |
|  | float | ByVal değişken As Single |
|  | double | ByVal değişken As Double |

Parametrelerden biri iki farklı tipte değer alabiliyorsa bunu As Any olarak tanımlamanız gerekir. Hangi parametrenin Any olarak tanımlanması gerektiğine ancak dosyadaki bilgileri okuyarak anlayabilirsiniz. Örneğin bir parametre hem string içerebiliyor ve hemde Null içerebiliyorsa bu parametre Any olarak tanımlanmalıdır.

Yaptıkları işlere göre API'lerin bulundukları dosyalar ise şunlardır :

| PRIVATE | **DLL ****** | **Fonksiyonları ****** |
| --- | --- | --- |
|  | Advapi32.dll | Şifre ve Kayıt dosyası işlemleri gibi gelişmiş bir çok API'ler |
|  | Comdlg32.dll | Diyalog pencereleri ile ilgili API'ler |
|  | Gdi32.dll | Grafik API'leri |
|  | Kernel32.dll | Çekirdek Windows API'leri |
|  | Lz32.dll | 32 bit skıştırma API'leri |
|  | Mpr.dll | Multiple Provider Router API'leri |
|  | Netapi32.dll | 32-bit Network API'leri |
|  | Shell32.dll | 32-bit Shell API'leri |
|  | User32.dll | Kullanıcı arabirimi API'leri |
|  | Version.dll | Versiyon işlemleri API'leri |
|  | Winmm.dll | Multimedia API'leri |
|  | Winspool.drv | Print spooler API'leri |

---
*Kaynak: `API NEDIR/API NEDIR.doc` — q — 2004*
