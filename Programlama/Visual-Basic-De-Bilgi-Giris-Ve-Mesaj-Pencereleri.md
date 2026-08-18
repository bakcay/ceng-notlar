# Visual Basic 'De Bilgi Giriş Ve Mesaj Pencereleri

**6.BÖLÜM**

**BİLGİ GİRİŞ VE MESAJ PENCERELERİ**

**6.1. MSGBOX(Mesaj Kutuları)**

** **Bütün Windows uyumlu programlarda kullanıcıya program akışı sırasında bilgi vermek ve onaylamak için diyalog kutuları içinde mesaj verilir. Visual Basic programları dahilinde ekrana bir diyalog kutusu içinde mesaj vermek için MSGBOX değimi kullanılır. MSGBOX değiminin iki kullanım şekli vardır.

1-Sadece kullanıcıya mesaj vermek için kullanılır.

**Örnek 6.1: **Program çalışmaya başladığında “Elektronik-Bilgisayar Bölümü” yazan komut satırını yazalım.

**Çözüm : ** Bu işlemi yapabilmek için Formun komut penceresine form açılırken meydana gelen Load olayına MsgBox fonksiyonu ile beraber bu mesaj satırını yazmamız gerekir.

Bu programı çalıştırdığımızda çıktısı aşağıdaki şekilde olur.

**Örnek 6.2 : **Şimdide program kapanırken “Visual Basic 5.0” mesajını yazan komut satırını yazalım.

**Çözüm :** Bu sefer komut penceresinde Unload olayına bu mesajı yazmamız gerekir.

Programı çalıştırıp form penceresini kapadığımızda aşağıdaki şekilde ekrana mesaj gelir.

2- Mesaj kutuları kullanıcıdan onay almak için de kullanılabilir.

Kullanıcıların mesaj kutularında verebileceği cevaplar için uygun düğmeleri belirlemek ve verilen cevabı öğrenebilmek için MsgBox fonksiyonunu aşağıdaki formata göre yazmalıyız.

**Cevap=MsgBox (mesaj, \[tip\],\[pencere başlığı\]\[,helpfile,context\])**

**Mesaj:** Kutu içerisine yazılmasını istediğimiz mesaj

**Pencere Başlığı:** Pencerenin başlığına yazılacak metin

**HelpFile, Context:** Bu iki özellikle bir yardım dosyası ismi ve bir konu numarası belirlenebilir.

**Tip:** Pencerenin içine konacak seçenekler, iconlar, pencerenin önceliğini ve varsayılan seçenekleri belirten bir sayıdır. Tip parametresini şu şekilde formülize edersek;

**Tip=seçenek+icon+varsayılan+öncelik**

**Seçenek:** Mesaj kutusunun tipini belirler. Bu pencerede mesaj kutusunda hangi düğmelerin bulunacağı belirlenir.

| **Sembolik** | **Sayısal** | **Anlamı** |
| --- | --- | --- |
| VbOKOnly | 0 | Tamam |
| VbOKCancel | 1 | Tamam İptal |
| VbAbortReryIgnore | 2 | Durdur Yeniden Dene Yoksay |
| VbYesNoCancel | 3 | Evet Hayır İptal |
| VbYesNo | 4 | Evet Hayır |
| VbRetryCancel | 5 | Yeniden Dene İptal |

Tablo-6.1. Seçenekler

**İcon : **Kullanıcının dikkatini çekebilmek için mesaja uygun bir resmin gösterilmesinde kullanılır.

| **Sembolik** | **Sayısal** | **Anlamı** |
| --- | --- | --- |
| VbCritical | 16 |  |
| VbQuestion | 32 |  |
| VbExclamation | 48 |  |
| VbInformation | 64 |  |

Tablo-6.2. İconlar

**Varsayılan : **Açılan pencerede kullanıcıya hangi düğmenin aktif olduğunu belirtir.

| **Sembolik** | **Sayısal** | **Anlamı** |
| --- | --- | --- |
| VbDefaultButton1 | 0 | Birinci Düğme |
| VbDefaultButton2 | 256 | İkinci Düğme |
| VbDefaoltButton3 | 512 | Üçüncü Düğme |

Tablo-6.3. Varsayılanlar

**Öncelik : **Bu parametrenin 4096 olması durumunda mesaj kutusunda her hangi bir seçim yapılmadan diğer uygulamalara geçiş yapılamaz. Cevap verilmesinin sistem için gerekli olduğu durumlarda kullanılır.

| **Sembolik** | **Sayısal** | **Anlamı** |
| --- | --- | --- |
| VbApplicationModal | 4096 | System Modal |
| VbSystemModa | 0 | Normal |

Tablo-6.4. Öncelik Verme

Seçilen fonksiyona göre MsgBox fonksiyonu geriye değerler gönderir. Bu değerler aşağıdaki tabloda verilmiştir.

| Sembolik | Sayısal | Anlamı |
| --- | --- | --- |
| VbOk | 1 | Tamam düğmesi seçildi |
| VbCancel | 2 | İptal düğmesi seçildi |
| VbAbort | 3 | İşlemi Durdur düğmesi seçildi |
| VbRetry | 4 | Tekrar Dene düğmesi seçildi |
| VbIgnore | 5 | Gözardı Et düğmesi seçildi |
| VbYes | 6 | Evet Düğmesi seçildi |
| VbNo | 7 | Hayır Düğmesi seçildi |

Tablo-6.5. Geri Dönen Değerler

**Örnek 6.3 : ******

Programın çıktısı aşağıdaki şekilde olur.

Bu örnekte 4 değeri ile Evet, Hayır düğmesini, 32 ile ? iconunu aktif hale getirdik.

**6.2. INPUTBOX(Bilgi Giriş Kutusu)**

Kullanıcının gereken değeri girebilmesi için Visual Basic’de InputBox fonksiyonu kullanılmaktadır. Bu fonksiyon standart olarak OK ve Cancel düğmeleri bulunan bir pencere açar ve değer giriş bu pencereden yapılır.

**InputBox (mesaj \[, başlık\]\[,varsayılan değer\]\[,x\]\[y\]\[,helpfile,context\]**

**Mesaj :** Girilmesi istenen değer için açıklama veya soru.

**Başlık :** Açılacak pencerenin başlığı.

**Varsayılan Değer :** Değer giriş kutusunda bulunması istenen metin.

**x,y :** Pencerenin sol üst köşesinin x ve y koordinatları.

Fonksiyondan dönen değer kullanıcının yazdığı metindir. Kullanıcı Cancel düğmesini seçmişse boş değer döner.

**Örnek 6. 4:**

Programın çıktısı aşağıdaki gibidir.

PAGE

PAGE 73

---
*Kaynak: `VISUAL BASIC 'DE BİLGİ GİRİŞ VE MESAJ PENCERELERİ/BİLGİ GİRİŞ VE MESAJ PENCERELERİ.doc` — BAHADIR — 2004*
