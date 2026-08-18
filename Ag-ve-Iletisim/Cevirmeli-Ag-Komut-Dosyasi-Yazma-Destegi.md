# Çevirmeli Ağ Komut Dosyası Yazma Desteği

## **Çevirmeli Ağ Komut Dosyası Yazma Desteği için**

## **Çevirmeli Erişim Komut Dosyası Yazma Komut Dili**

Telif Hakkı (c) 1995 Microsoft Corp.

**İçindekiler**

1.0 Giriş

2.0 Bir Komut Dosyasının Temel Yapısı

3.0 Değişkenler

3.1 Sistem Değişkenleri

4.0 Dizi Hazır Bilgileri

5.0 Deyimler

6.0 Açıklamalar

7.0 Anahtar Sözcükler

8.0 Komutlar

9.0 Ayrılmış Sözcükler

**1.0 ****Giriş******

Birçok Internet hizmet sağlayıcı ve çevrimiçi hizmetler bir bağlantı kurmak için, kullanıcı adınız ve parolanız gibi bilgileri girmenizi ister. Çevirmeli Ağ Erişimi için Komut Dosyası Yazma desteği ile bu işlemi otomatik hale getirecek bir komut dosyası yazabilirsiniz.

Bir komut dosyası, Internet hizmet sağlayıcısının ya da çevrimiçi hizmetinin bu bağlantıyı kurması ve bu hizmeti kullanması için gereken bir dizi komutu, parametreyi ve deyimi içeren bir metin dosyasıdır. Bir komut dosyası yaratmak için, Microsoft Not Defteri gibi herhangi bir düzenleyici kullanabilirsiniz. Komut dosyanızı bir defa yarattıktan sonra, Çevirmeli Erişim için Komut Dosyası Yazma Aracı'nı çalıştırarak bu dosyayı özel bir Çevirmeli Ağ bağlantısına atayabilirsiniz.

**2.0 ****Bir Komut Dosyasının Temel Yapısı**

Komut, komut yazma dosyasının içerdiği temel yönergedir. Bazı komutlar, komutun ne yapması gerektiğini tanımlayan parametrelere gereksinim duyarlar. Deyim, bir sonuç oluşturan bağımsız değişkenlerin ve işleçlerin birleşimidir. Deyimler, herhangi bir komutun içinde değer olarak kullanılabilirler. Deyimlere örnek olarak, aritmetik ve ilişkisel karşılaştırmalar ve dizi bitiştirmeler verilebilir.

Çevirmeli Ağ için komut dosyasının temel biçimi aşağıdaki gibidir:

;

; Açıklama, noktalı virgülle başlar ve satırın sonuna kadar

; gider.

;

proc main

; Bir komut dosyasında bulunabilecek değişken ve

; komut sayısının sınırı yoktur

*değişken bildirimleri*

*komut bloğu***

endproc

Bir komut dosyasının, **proc **anahtar sözcüğü ve bu sözcükle eşleşen ve yordamın sonunu gösteren **endproc **anahtar sözcüğü ile belirtilen bir ana yordamı mutlaka olmalıdır.

Değişken bildirimlerini, komutları eklemeden önce yapmalısınız. Önce ana yordamdaki ilk komut yürütülür ve sonra onu izleyen komutlar, komut dosyasında göründükleri sıra ile yürütülür. Ana yordamın sonuna gelindiğinde komut dosyası da biter.

**3.0 ****Değişkenler**

Komut dosyaları değişkenler içerebilir. Değişken adları bir harfle ya da bir altçizgi ('\_') ile başlar ve herhangi bir şekilde sıralanmış büyük ya da küçük harfler, sayılar ya da altçizgiler içerebilir. Ayrılmış bir sözcüğü bir değişken adı olarak kullanamazsınız. Daha fazla bilgi için, bu belgenin sonunda yer alan ayrılmış sözcükler listesine bakın.

Değişkenleri kullanmadan önce bildirimlerini yapmanız gerekir. Bir değişken bildirimi yaptığınızda, o değişkenin türünü de belirtmeniz gerekir. Belli bir türdeki değişken ancak yine bu türdeki değerleri içerebilir. Aşağıdaki üç değişken türü desteklenmektedir:

Tür Açıklama

integer Bir negatif ya da pozitif sayı, örneğin: 7, -12, ya da 5698.

string Çift tırnak işareti içine alınmış bir karakter dizisi; örneğin, "Merhaba!" ya da "Parolanızı girin:".

boolean Mantıksal bir boolean değeri, TRUE (DOĞRU) ya da FALSE (YANLIŞ).

Aşağıdaki atama ifadesi kullanılarak değişkenlere değerler atanır:

*değişken* **=** *deyim***

Değişken eşitlenen deyimi alır.

Örnekler:

integer count = 5

integer timeout = (4 \* 3)

integer i

boolean bDone = FALSE

string szIP = "getip 2"

set ipaddr szIP

3.1 Sistem Değişkenleri

Sistem değişkenleri komut dosyaları komutlarıyla ayarlanır ya da Çevirmeli Ağ bağlantısı kurarken verdiğiniz bilgiler tarafından belirlenir. Sistem değişkenleri salt okunurdur, bu da komut dosyası içinde değiştirilemeyecekleri anlamına gelir. Sistem değişkenleri şunlardır:

Ad Tür Açıklama

$USERID String Geçerli bağlantı için kullanıcı kimliği. Bu değişken,

Çevirmeli Ağ Bağlantı Yeri iletişim kutusunda belirtilmiş olan

kullanıcı adının değeridir.

$PASSWORD String Geçerli bağlantı için parola. Bu değişken, Çevirmeli Ağ

Bağlantı Yeri iletişim kutusunda belirtilmiş olan

kullanıcı parolasının değeridir.

$SUCCESS Boolean Bu değişken, komutun başarılı olup olmadığını belirtmek için bazı komutlar tarafından ayarlanır. Komut

dosyası, bu değişkenin değerine göre karar verebilir.

$FAILURE Boolean Bu değişken, komutun başarısız olup olmadığını

belirtmek için bazı komutlar tarafından ayarlanır. Komut

dosyası, bu değişkenin değerine göre karar verebilir.

Bu değişkenler, benzer türde bir deyimin kullanıldığı herhangi bir yerde kullanılabilir. Örneğin,

transmit $USERID

geçerli bir komuttur çünkü $USERID, "string" türünde bir değişkendir.

**4.0 ****Dizi Hazır Bilgileri******

Çevirmeli Ağ için Komut Dosyası Yazma, aşağıda açıklandığı gibi, kaçış tuşu dizisi ve kontrol dizisini destekler.

Dizi

Hazır Bilgileri Açıklama

**^***char* Kontrol dizisi

*char*, '@' ile '\_' arasında bir değerse karakter sırası, 0 ile 31 arasında olan bir

tek-bayt değere çevrilir. Örneğin, ^M bir satırbaşı değerine dönüştürülür.

*char*, a ile z arasında bir değerse karakter sırası, 1 ile 26 arasında olan bir

tek-bayt değere çevrilir.

*char* herhangi başka bir değerse, karakter sırasına özel bir işlem uygulanmaz.

**<cr>** Satırbaşı

**<lf>** Satır atlama

**\\"** Çift tırnak

**\\^** Tek kontrol dizisi

**\\<** Tek '<'

**\\\\** Ters eğik çizgi

Örnekler:

transmit "^M"

transmit "Gamze^M"

transmit "<cr><lf>"

waitfor "<cr><lf>"

**5.0 ****Deyimler******

Deyim, bir sonucun değerlendirilmesini sağlayan işleç ve bağımsız değişkenlerin birleşimidir. Deyimler, herhangi bir komut içinde değer olarak kullanılabilir.

Bir deyim, herhangi bir değişkeni ya da integer, string ya da boolean değerleri, aşağıdaki tablolarda görüleceği gibi herhangi birli ya da ikili işleç ile birleştirebilir. Tüm birli işleçler en yüksek önceliği alırlar. İkili işleçlerin önceliği tablodaki konumları ile belirtilmiştir.

Birli işleçler şunlardır:

** **İşleç İşlem Türü

- Birli eksi

! Bir'in tümleyeni

İkili işleçler öncelik sıralarına göre aşağıdaki tabloda listelenmiştir. Yüksek öncelikli işleçler listede önce yer alır:

İşleçler İşlem Türü Tür Sınırlamaları

\* / Çarpma Integers

+ - Toplama Integers, Strings (yalnız + )

< > <= >= İlişkisel Integers

== != Eşitlik Integers, strings, booleans

and Mantıksal VE Booleans

or Mantıksal VEYA Booleans

Örnekler:

count = 3 + 5 \* 40

transmit "Merhaba" + " dünya"

delay 24 / (7 - 1)

**6.0 ****Açıklamalar******

Noktalı virgülü izleyen tüm satır yoksayılır.

Örnekler:

; bu bir açıklamadır

transmit "merhaba" ; string "merhaba" aktarımı

**7.0 ****Anahtar Sözcükler**

Anahtar sözcükler komut dosyasının yapısını belirler. Komutların aksine, bir eylem gerçekleştirmezler. Anahtar sözcükler aşağıda listelenmiştir.

**proc** *ad*

Yordamın başlangıcını belirtir. Tüm komut dosyalarının bir ana yordamı olması gerekir (**proc **ana). Komut dosyasının yürütülmesi ana yordamdan başlar ve ana yordamın bitiminde sona erer.

**endproc**

Yordamın sonunu belirtir. Komut dosyası ana yordamın **endproc **ifadesine kadar yürütüldüğünde, Çevirmeli Ağ PPP ya da SLIP'e başlayacaktır.

**integer ***ad *\[ **=** *değer* \]

Integer türünde bir değişken bildirimi yapar. Değişkenin ilk değeri için herhangi bir sayısal deyim ya da değişken kullanabilirsiniz.

**string ***ad *\[ **=** *değer *\]

String türünde bir değişken bildirimi yapar. Değişkenin ilk değeri için herhangi bir dizi hazır bilgisi ya da değişken kullanabilirsiniz.

**boolean ***ad *\[ **=** *değer *\]

Boolean türünde bir değişken bildirimi yapar. Değişkenin ilk değeri için herhangi bir boolean deyimi ya da değişken kullanabilirsiniz.

**8.0 ****Komutlar**

Tüm komutlar ayrılmış sözcüklerdir, bundan ötürü komutlarla aynı ada sahip değişken bildirimi yapamazsınız. Komutlar aşağıda listelenmiştir:

**delay** *nSaniye***

Komut dosyasındaki bir sonraki komutu yürütmeden önce *nSaniye *ile belirtilen saniye kadar duraklar.

Örnekler:

delay 2 ; 2 saniye duraklar

delay x \* 3 ; x \* 3 saniye duraklar

**getip** *değer*

Uzak bilgisayardan alınacak IP adresini bekler. Internet hizmet sağlayıcınız bir dize içinde birden fazla IP adresi döndürüyorsa, komut dosyasının kullanması gereken IP adresini belirtmek için* değer *parametresini kullanın.

Örnekler:

; ikinci IP adresini alır

set ipaddr getip 2

; ilk alınan IP adresini bir değişkene atar

szAddress = getip

**goto ***etiket***

Komut dosyasında *etiket* ile belirtilen konuma atlar ve onu izleyen komutları yürütmeye devam eder.

Örnekler:

waitfor "Prompt>" until 10

if !$SUCCESS then

goto BailOut ; BailOut'a atlar ve onu izleyen komutları

; yürütmeye başlar

endif

transmit "bbs^M"

goto End

BailOut:

transmit "^M"

**halt******

Komut dosyasını durdurur. Bu komut uçbirim iletişim penceresini kaldırmaz. Bağlantıyı kurmak için Devam'ı tıklatmanız gerekir. Komut dosyasını yeniden başlatamazsınız.

**if ***durum ***then******

*komutlar***

**endif******

Eğer *durum *DOĞRU* *ise bir *komutlar* serisi yürütür.

Örnek:

if $USERID == "John" then

transmit "Johnny^M"

endif

*etiket* **:******

Komut dosyasında atlanılacak yeri belirtir. Etiketin benzersiz bir adı olmalı ve değişkenlerin adlandırılma düzenlerine de uygun olmalıdır.

**set port databits **5 | 6 | 7 | 8

Bir oturum sırasında gönderilen ve alınan baytların içindeki bit sayısını değiştirir. Bit sayısı 5 ve 8 arasında olabilir. Komut dosyasında bu komutu kullanmadıysanız Çevirmeli Ağ, bağlantı için özellikler ayarlarını kullanacaktır.

Örnek:

set port databits 7

**set port parity **none | odd | even | mark | space

Oturum sırasında bağlantı noktası için parite şemasını değiştirir. Komut dosyasında bu komutu kullanmadıysanız Çevirmeli Ağ, bağlantı için özellikler ayarlarını kullanacaktır.

Örnek:

set port parity even

**set port stopbits **1 | 2

Oturum sırasında bağlantı noktası için dur biti sayısını değiştirir. Bu sayı 1 ya da 2 olabilir. Komut dosyasında bu komutu kullanmadıysanız Çevirmeli Ağ, bağlantı için özellikler ayarlarını kullanacaktır.

Örnek:

set port stopbits 2

**set screen keyboard ** on | off

Komut dosyası yazma uçbirim terminalinden yapılacak klavye girdisini etkinleştirir ya da etkinliğini kaldırır.

Örnek:

set screen keyboard on

**set ipaddr ***dize***

Oturum için iş istasyonunun IP adresini belirtir. *Dize* IP adresi biçiminde olmalıdır.

Örnekler:

szIPAddress = "11.543.23.13"

set ipaddr szIPAddress

set ipaddr "11.543.23.13"

set ipaddr getip

**transmit ***dize *\[ **, raw **\]

Uzak bilgisayara *dize* ile belirtilen karakterler gönderir.

Komut içinde **raw **parametresini kullanmadığınız sürece, uzak bilgisayar kaçış tuşu dizisi ve kontrol dizisini algılayacaktır. $USERID ve $PASSWORD sistem değişkenleri aktarıldığında kullanıcı adı ya da parola karakter sıraları içeriyorsa, **raw **parametresini kullanmak yararlıdır, **raw **parametresi yoksa, kaçış tuşu dizisi ya da kontrol dizisi olarak algılanabilecektir.

Örnekler:

transmit "slip" + "^M"

transmit $USERID, raw

**waitfor ***dize *\[ **,** **matchcase **\] \[ **then ***etiket ***

{ **,** *dize *\[ **,** **matchcase **\] **then ***etiket *} \]

\[ **until ***zaman *\]

Bilgisayarınız, uzak bilgisayardan belirtilmiş olan dizelerden bir ya da daha fazlasını alana kadar bekler. **matchcase** parametresi kullanılmazsa, *dize* parametresi küçük ve büyük harf duyarlıdır.

Eşleşen bir dize alınırsa ve **then ***etiket *parametresi kullanılırsa, bu komut, komut dosyasında *etiket *ile belirtilen yere atlayacaktır.

Seçime bağlı **until ***zaman *parametresi, bilgisayarınızın bir sonraki komutu yürütmeden önce, dizeyi almak için bekleyeceği saniye sayısının üst sınırını belirtir. Bu parametre yoksa, bilgisayar sonsuza kadar bekleyecektir.

Bilgisayarınız, belirtilmiş dizelerden birini alırsa, $SUCCESS sistem değişkeni TRUE'ya (DOĞRU) eşitlenir. Aksi takdirde, *zaman *ile belirtilen saniye sayısı dize alınmadan önce aşılmışsa, FALSE!a (YANLIŞ) eşitlenir.

Örnekler:

waitfor "Login:"

waitfor "Password?", matchcase

waitfor "prompt>" until 10

waitfor

"Login:" then DoLogin,

"Password:" then DoPassword,

"BBS:" then DoBBS,

"Other:" then DoOther

until 10

**while ***durum ***do******

*komutlar***

**endwhile******

*durum *YANLIŞ olana kadar *komutlar* serisini yürütür.

Örnek:

integer count = 0

while count < 4 do

transmit "^M"

waitfor "Login:" until 10

if $SUCCESS then

goto DoLogin

endif

count = count + 1

endwhile

...

**9.0 ****Ayrılmış Sözcükler******

Aşağıdaki sözcükler ayrılmış sözcüklerdir ve değişken adı olarak kullanılamazlar.

and boolean databits delay

do endif endproc endwhile

even FALSE getip goto

halt if integer ipaddr

keyboard mark matchcase none

odd off on or

parity port proc raw

screen set space stopbits

string then transmit TRUE

until waitfor while

---
*Kaynak: `Çevirmeli Ağ Komut Dosyası Yazma Desteği/Çevirmeli Ağ Komut Dosyası Yazma Desteği.doc` — serkan — 2004*
