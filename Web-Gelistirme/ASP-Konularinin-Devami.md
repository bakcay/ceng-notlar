# ASP Konularinin Devami

Yazı dizimize :Request objesinin Property leri ,RESPONSE OBJECT, Response objesinin Property leri, RESPONSE Objesinin Metodları konuları ile devam ediyoruz.

**Request objesinin Property leri**

**Totalbytes**:clientın gonderdigi istemin body kısmında gonderilen verilerin toplam uzunlugunu belirtir.

Syntax

Counter = Request.TotalBytes

**Request objesinin Metodları******

**Binaryread:**POST ile clienttan server’a gönderilmiş veri.Bu veriler SafeArray de tutulur.SafeArray de tutulan bilginin boyutlarıda tutulur.

Syntax

variant = Request.BinaryRead(count)

parametreler:

variant: VT\_ARRAY veya VT\_UI1 tipinde unsigned bitlerden oluşan bir dizi

count: client taraftn gelen bilginin okunabilen kısmının uzunlugunu belirtir.

Request.form ile Binaryread aynı sayfa uzerinde çağrılamaz.

**RESPONSE OBJECT******

Client tarafa çıktı göndermek için kullanılır.

**Response objesine ait kolleksiyonlar******

**Cookies:**cookielere değer atamak için kullanılır.Boyle bir cookie yoksa once oluşturulur.

Varsa yeni değer atanır.

Syntax

Response.Cookies(cookie)\[(key)|.attribute\] = value

Parametreler

cookie :cookie'nin adı

key :opsiyonel bir parametredir. key belirtilmişse , cookie bir dictionary'dir, ve key 'e değer atanır

attribute

cookie hakkındaki bilgileri tutar buna ait parametreler aşağıdakilerdir:

Domain :Write-only.eğer belirtilmişse cookie yalnızca bu parametre ile belirtilen değerdeki domainlere gonderilir.

Expires :Write-only. cookienin kullanımdan kalktığı tarih.bir değer belirtilmemişse cookie session sonuna kadar geçerli olur.

HasKeys :Read-only. cookienin key' e sahip olup olmadığını belirtir.

Path :Write-only. Belirtildiği takdirde cookie sadece bu pathdeki istemelre gonderilir. belirtilmemiş ise uygulama path 'i kullanılır.

Secure :Write-only. cookienin guvenli olup olmadıgını belirler.

Value :key yada attribute'a atanan değer

Şu şekilde bir cookie oluşturulursa

## <% Response.Cookies("mycookie")("type1") = "sugar"

## Response.Cookies("mycookie")("type2") = "ginger snap"

| %> |
| --- |

Headerda su bilgiler yer alır

| Set-Cookie:MYCOOKIE=TYPE1=sugar&TYPE2=ginger+snap |
| --- |

Ornekler

## <%

## For Each cookie in Response.Cookies

## Response.Cookie(cookie).ExpiresAbsolute = #July 4, 1997#

## Next

| %> |
| --- |

## <%

Response.Cookies("Type") = "Chocolate Chip"

Response.Cookies("Type").ExpiresAbsolute = "July 31, 2001"

Response.Cookies("Type").Path = "/"

| %> |
| --- |

**Response objesinin Property leri******

 Buffer

 CacheControl

 Charset

 ContentType

 Expires

 ExpiresAbsolute

 IsClientConnected

 Pics

 Status

**1-Buffer:**sayfanın tamponlanıp tamponlanmayacağını belirtir.Eğer sayfa tamponlanırsa server tum scriptlerin çalışması bitmeden yada flush yada end çağrılana kadar client tarafa veri gondermez.Buffer server clienta veri gonderdikten sonra atanmaz.Bu yuzden asp dosyasının ilk satırında belirtilmelidir.

Syntax

Response.Buffer \[= flag\]

Parametreler

flag :true yada false değerini alır.true ise tamponlama yapılır false ise yapılmaz.

**2-CacheControl******

CacheControl ozelliği Private default değeri dikkate almaz.Bu değeri Public yaptığınız zaman,proxy serverlar ASP tarafından olusturulan çıktıyı cache'e atabilirler

Syntax

Response.CacheControl \[= Cache Control Header \]

Parametreler:

**Cache Control Header :**public yada private değerlerini alabilir.

**3-Charset:**response objesindeki content-type headerına character setini (örneğin, ISO-LATIN-7) atar.

Syntax

Response.Charset(CharsetName)

Parametreler

CharsetName karakter setini bwlirleyen string

Örneğin;

the Response.Charset özelliği içermeyen bir asp sayfasındacontent-type su şekilde olacaktır:

content-type:text/html

su satır eklenirse

| <% Response.Charset= "ISO-LATIN-7" %> |
| --- |

content-type başlığı şu şekilde olacaktır:

content-type:text/html; charset=ISO-LATIN-7

**4-ContentType******

default değeri text/HTML.

Syntax

Response.ContentType \[= ContentType \]

Parameters

ContentType :type/subtype şeklinde belirtilir.

örnek

aşağıdaki örnek content type 'ı Channel Definition Format (CDF) formatına çevirir

| <% Response.ContentType = "application/x-cdf" %> |
| --- |

sık kullanılan diğer değerler

## <% Response.ContentType = "text/HTML" %>

## <% Response.ContentType = "image/GIF" %>

## <% Response.ContentType = "image/JPEG" %>

## <% Response.ContentType = "text/plain" %>

| <% Response.ContentType = "image/JPEG" %> |
| --- |

**5-Expires:******

sayfanın cache'e atılmadan ne kadar sure kalabileceğini belirtir.eğer bir sayfa expire olmadan kullanıcı aynı sayfaya donerse cache'e atılan sayfa gosterilir.

Syntax

Response.Expires \[= number\]

Parametreler

number :dakika

.asp dosyanız Response.Expires'ı cağırdığı zaman, IIS serverın saatini beliten bir HTTP başlığı oluşturur. client tarafın sistem saati server saatinden daha erken ise (farklı yerlerde olabileceklerinden) parametrenin değerin, 0 yapmak sayfanın expire olmasında hic bir etki göstermeyecektir. Response.ExpiresAbsolute'i kullanmalısınız.Ek olarak expires ozelliği için negatif bir sayı kullanabilirsiniz

| <%Response.Expires = -1 %> |
| --- |

response hemen expire olacaktır

eğer bir sayfa uzerinde birden çok response.expires kullaılmışsa server bunlardan en kısa zamana sahip olanı değerlendirecektir.

**6-ExpiresAbsolute******

ExpiresAbsolute ozelliği browserda cache'e atılan bir sayfanın ne zaman expireolacağı bilgisini saat ve zaman cinsinden belirtir.tarih belirtilmemişse sayfa scriptin çalıştığı günün gece yarısı expire olur.

Syntax

Response.ExpiresAbsolute \[= \[date\] \[time\]\]

Parameters

date :RFC-1123 formatında tarih bilgisi

saat:Expires başlığı gönderilmeden önce bu değer GMT ye çevrilir.

ExpiresAbsolute birden cok kez kullanılmışsa en erken tarih bilgisine sahip olanı server tarafından değerlendilir.

örnek

| <% Response.ExpiresAbsolute=#May 31,2001 13:30:15# %> |
| --- |

**7-IsClientConnected******

client'ın serverdan bağlantısını kesip kesmediği bilgisini tutar.

Syntax

Response.IsClientConnected ( )

Örnek

## <% If Not Response.IsClientConnected Then

## Shutdownid = Session.SessionID

## Shutdown(Shutdownid)

## End If

| %> |
| --- |

**8-PICS******

pics-label response header'ına değer ataması yapar.

Syntax

Response.PICS(PICSLabel)

Parameters

PICSLabel

Örnek

## <%

## Response.PICS("(PICS-1.1 <http://www.rsac.org/ratingv01.html>

labels on " & chr(34) & "1997.01.05T08:15-0500" & chr(34) & " until" & chr(34) & "1999.12.31T23:59-0000" & chr(34) &

## " ratings (v 0 s 0 l 0 n 0))")

| %> |
| --- |

satırını içeren asp dosyasına su header eklenmş olur

PICS-label:(PICS-1.1 <http://www.rsac.org/ratingv01.html> labels on "1997.01.05T08:15-0500" until "1999.12.31T23:59-0000" ratings (v 0 s 0 l 0 n 0))

**9-Status******

Status property serverden gelen status line değeridir. Status değerleri HTTP olarak tanımlanırlar.

Syntax

Response.Status = StatusDescription

Parameters

StatusDescription :3 dijitlik status kodunu ve bu koda ati kısa bir açıklamayı içeren bir string değerdir.örneğin 310 Move Permanently.

Örnek:

| <% Response.Status = "401 Unauthorized" %> |
| --- |

RESPONSE Objesinin Metodları

**1-AddHeader******

AddHeader metodu bir HTML başlığı ekler.Bu metod her zaman yeni bir başlık ekler yani olan bir başlık ile yer değiştirmez. Eklenen bir başlık bir daha kaldırılamaz

Syntax

Response.AddHeader name, value

Parameters

name :yeni başlık değişkenin adı.

value :başlıkta tutulan değer

Bir ad karmaşasını engellemek icin name parametresi altçizgi ( \_ ) içermemelidir. Server.varibles kolleksiyonu başlıklar içinde bu karakteri tire ( - ) olarak algılar.

| <% Request.ServerVariables("HTTP\_MY\_HEADER") %> |
| --- |

Scripti ile server MY-HEADER isimli bir başlık arar.

HTML ifadelerde başlıklar içerikten once yer alması gerktiğinden addheader content gonderilmeden once yani .asp dosyanız bir çıktı uretmeden once yer almalıdır.Bunun için flush metodu kullanılabilir.

## <HTML>

Here's some text on your Web page.

<% Response.AddHeader "WARNING", "Error Message Text" %> Here's some more interesting and illuminating text.

## <% Response.Flush %>

## <% Response.Write("some string") %>

| </HTML> |
| --- |

Örnek

| <% Response.Addheader "WWW-Authenticate", "BASIC" %> |
| --- |

**2-AppendToLog******

web serverinizin loglarına yeni bir string ekler.sayfanız icinde bir cok kez cağiridiginizda her seferinde yeni bir string ekleyecektir.

Syntax

Response.AppendToLog string

Parametreler:

string :Eklenecek text.loglarda ifadeler ( , )(virgul)lerle ayrıldıgından text parametresi virgul içermemelidir.

Örnek

| <% Response.AddToLog "My custom log message" %> |
| --- |

**3-BinaryWrite******

karakter donuşümü yapılmaksızın bilgileri HTTP çıktısına yazar.belli uygulamalarda kullanılmak uzere binary data gibi non-string ifadelerle çalışıyorsanız yaralı bir metod olabilir.

Syntax

Response.BinaryWrite data

Parameters

data:HTTP çıktısına yazılacak olan data.bu veri VT\_ARRAY yada VT\_UI1 tipinde olabilir.

Örnek

## <%

## Set objBinaryGen = Server.CreateObject("MyComponents.BinaryGenerator")

## vntPicture = objBinaryGen.MakePicture

## Response.BinaryWrite vntPicture

| %> |
| --- |

**4-Clear******

tamponlanmış tüm HTML çıktılarını siler.Bu method sadece body kısmını silebilir headerları silemez.Response.buffer özelliği true ise bu methodun kullanılması run-time error oluşturur.

Syntax

Response.Clear

**5-End******

web serverin scripti çalıştırmasını dururur ve o zamana kadar uretilen sonuçları client taraf gonderir.

Syntax

Response.End

eğer Response.Buffer özelliği TRUE yapılmışsa , Response.End 'in kullanılması tamponlanmış veriyi gonderir. eğer kullanıcıya veri gitmesini istemiyorsanız,önce Response.Clear metodunu kullanmalısınız

## <%

## Response.Clear

## Response.End

| %> |
| --- |

**6-Flush:******

tamponlanmış veriyi hemen kullanıcıya gonderir.Eğer Response.buffer ozelliği TRUE ise hata oluşur

Syntax

Response.flush

**7-Redirect******

browseri baska bir url ye gonderir

Syntax

Response.Redirect URL

Parametreler

URL :(Uniform Resource Locator) yonlendirilen yer

Redirect metodu kullanıldığı zaman şu başlık eklenir:

## HTTP 1.0 302 Object Moved

## Location URL

| <% Response.Redirect "http://www.microsoft.com" %> |
| --- |

**8-Write******

belirtilen yazıyı HTTP çıktısına ekler

Syntax

Response.Write variant

Parametreler

variant :yazılacak veri. Asp tagi yazmak için "%\\>" yazılmalıdır.

Ornekler

## I just want to say <% Response.Write "Hello World." %>

| Your name is: <% Response.Write Request.Form("name") %> |
| --- |

| <% Response.Write "<TABLE WIDTH = 100%\\>" %> |
| --- |

---
*Kaynak: `ASP KONULARININ DEVAMI/ASP KONULARININ DEVAMI.doc` — ekim kaya — 2004*
