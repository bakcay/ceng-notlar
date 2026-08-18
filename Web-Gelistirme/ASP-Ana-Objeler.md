# ASP Ana Objeler

Dizinin 2 bölümünde : ana objeler, request, response, cookie, form, querystring, server variables konularından bahsediliyor.

**Ana Objeler ******

Active Server Pages ‘in beraberinde gelen bazı server ve uygulama geliştirme objeleri vardır. Bu objeler developerları clienttan gelen requestleri, application durumunun yonetimi,cookilerin kullanılması, istemciye verilcek cevabın duzenlenmesi gibi işlerin detayları için kod yazma zahmetinden kurtatır. Bu ana objeler şunlardır:

**1-Request and Response:**request objesi HTTP istemi ile scripte gonderilen tum bilgilere erişimi sağlar. Bu bilgiler cookieleri,formları,URL querylerini ve http headerlarını kapsar.

**Request objesine ait kolleksiyonlar:******

1-clientcertificate 2-cookie 3-form 4-querystring 5-servervaribles

eğer request.form veya request.querystring gibi ifadeler yerine dogrudan request(variable) denilirse web server kolleksiyonları şu sırada arar

1. querystring

2. form

3. cookies

4. clientcertificate

5. servervariables

Bunun için çoğunlukla

Request.(AUTH\_USER) yerine Request.ServerVariables(AUTH\_USER) kullanılır.

**1-ClientCertificate **:HTTP requesti icinde gonderilen X.509 standartındaki sertifikalara ait bilgilerdir.Eğer web browser SSL3.0/PCT1 Protocolu kullanıyorsa yani secure bir iletişim yapıyorsa web browsera sertifika yollayabilir.Eğer bir Sertifika gonderilmemişse ClientCertificate kolleksiyonundan EMPTY degeri doner.

Syntax

Request.ClientCertificate( Key\[SubField\] )

Bu kolleksiyona ait Keyler ise şunlardır:

| **Certificate****** | ASN.1 formatındaki tum sertifika içeriğinin binary stream'ini içeren bir string |
| --- | --- |
| **Flags****** | ek sertifika verileri sağlayan flaglerden oluşur. ceCertPresent—A client certificate is present. ceUnrecognizedIssuer—Bu zincirdeki son sertifikasyon bilinmyen bir user'a ait Not: flagleri kullanbilmeniz için Asp dosyanıza client sertifikasını include etmelisiniz.VBScript kullanıyorsanız cervbs.inc dosyasını Jscript kullnıyorsanız cerjavas.inc dosyasını include etmelisiniz.Bu dosyalar \\Inetpub\\ASPSamp\\Samples klasorune yuklenmiştir. |
| **Issuer****** | sertifikayı yayınlayan hakkındaki bilgileri kapsayan bazı subfield değerlerinden oluşan bir string dir.Eğer Sub fileld olmadan bu değer belirtilmişse ClientCertificate kolleksiyonu virgul ile ayrılmış SubFieldlar gonderir.Örneğin ,C=US, O=Verisign, vb... |
| **SerialNumber****** | Client sertifikası serial numerını ASCII tipinde ve tirelerle ayrılmış hxadecimal ifadeleri kapsayan bir stringdir.Örneğin, 04-67-F3-02. |
| **Subject****** | Bazı subfiled değerlerini tutan stringdir.Subfield değeri sertifikanın konusu hakkındaki bilgileri kapsar.Eğer bu değer subfieldsız belirtilmişse ClientCertificate kolleksiyonu virgul ile ayrılmış SubFieldlar gonderir. Örneğin, C=US, O=Msft, vb.. |
| **ValidFrom****** | sertifikanın hangi tarihten itibaren geçerli oldugunu bildiren tarih.Bu tarih VBScript formatındır ve uluslararası ayarlar ile değişir. Örneğin, U.S.'de, 9/26/96 11:59:59 PM. |
| **ValidUntil****** | sertifikanın hangi tarihe kadar geçerli oldugunu bildirir. |

SubField

| **C****** | şehir/kasaba adı |
| --- | --- |
| **CN****** | Skullanıcı adı (sadece Subject keyi ile kullnaılır.) |
| **GN****** | verilen ad |
| **I****** | ilk oncekileri belirtir |
| **L****** | Yöre |
| **O****** | şirket yada organizasyon adı |
| **OU****** | organizasyonel birimler |
| **S****** | Eyalet |
| **T****** | organizayon adı veya kişinin ünvanı |

Clientcertificate ile ilgili bazı ornek ASP kodları

<%

For Each strKey in Request.ClientCertificate

Response.Write strkey & " = " & Request.ClientCertificate(strkey) & "<BR>")

Next

| %> |
| --- |

<%

If Len(Request.ClientCertificate("Subject")) = 0

Response.Write("No client certificate was presented")

End if

| %> |
| --- |

| <%= Request.ClientCertificate("IssuerCN") %> |
| --- |

<%

If (Request.ClientCertificate("Subject")="Msft")

Response.Write("Good Choice!")

End if

| %> |
| --- |

| <%= Request.ClientCertificate("ValidUntil") %> |
| --- |

<!--#include file="cervbs.inc" -->

<%

If Request.ClientCertificate("Flags") and ceUnrecognizedIssuer then

Response.Write "Unrecognized issuer"

End If

| %> |
| --- |

**2-COOKIE******

Syntax

Request.Cookies(cookie)\[(key)|.attribute\]

Örnekler

## <%

## For Each strKey In Request.Cookies

## Response.Write strKey & " = " & Request.Cookies(strKey) & "<BR>"

## If Request.Cookies(strKey).HasKeys Then

## For Each strSubKey In Request.Cookies(strKey)

## Response.Write "->" & strKey & "(" & strSubKey & ") = " & \_

## Request.Cookies(strKey)(strSubKey) & "<BR>"

## Next

## End If

## Next

| %> |
| --- |

| <%= Request.Cookies("myCookie") %> |
| --- |

**3-FORM******

HTTP requestinde POST ile gonderilen form verisi bilgilerini alır.

Syntax

Request.Form(element)\[(index)|.Count\]

Parametreler

element :form elemanının adı

index

bir parametrenin birden çok değerlerinden birine erişmenizi sağlayan opsiyonel bir değer Request.Form(parameter).Count. arasında değişen integer değerleri olabilir.

100 Kb dan buyuk veriler POST edilirken Request.form kullanılmaz bunun yerine request.binaryread kullanılır.

Örnekler

## <%

## For i = 1 To Request.Form("FavoriteFlavor").Count

## Response.Write Request.Form("FavoriteFlavor")(i) & "<BR>"

## Next

| %> |
| --- |

**4-QUERYSTRING******

HTTP içerisindeki query string dediğimiz link yaninda verilen ve ?(soru işareti) ile ayrilarak yazilan ifadelerdir.

Basit bir örnek verecek olursak

<a href=”queryornek.asp?msg=querystring\_metodu”>querystring ornegi</a>

Syntax

Request.QueryString(variable)\[(index)|.Count\]

Parametreler

variable

http içersinde gonderilen query string değişkeninin adı

index

değişkenin bir veya daha fazla değerini alabilmenizi sağlayan opsiyonel bir parametredir. 1 ile Request.QueryString(variable).Count arasında değişen bir integer değeri alabilir.

Request.querystring(parametre) QUERY\_STRING içinde bulunan bütün değişenleri tutan bir dizidir. Bu dizinin istediğiniz kaç elemanı oldugunu bulmak için Request.QueryString(parameter) .Count kullanılır.Eğer bir değişken gönderilmemişse bu değer 0 değerini alır.

Örnek

http://localhost/asp/names.asp?Q=Fred&Q=Sally

## ---NAMES.ASP---

## <%

## For Each item In Request.QueryString("Q")

## Response.Write Request.QueryString("Q")(item) & "<BR>"

## Next

| %> |
| --- |

Yada

## <%

## For i = 1 To Request.QueryString("Q").Count

## Response.Write Request.QueryString("Q")(i) & "<BR>"

## Next

| %> |
| --- |

Yazildiğinda ekran ciktisi su şekilde olacaktir.

**5-Server Variables:******

istemci tarafın tarayıcısı tarafından yollanan bir http başlık bilgisi bu kolleksiyonla kullanılabilir.

Syntax

Request.ServerVariables (server değişkenleri)

Server değişkenleri aşağıda verilmiştir:

**ALL\_HTTP :**client tarafından gonderilen bütün HTTP başlıkları

**ALL\_RAW :**tum HTTP değerlerini alır.ALL\_HTTP ile arasındaki fark ALL\_HTTP servera gelmeden once HTTP\_ prefix e gelir.Burada başlık adı büyük harfe çevrilir.ALL\_RAW da ise datalar buraya gelmediği için client taraftan gonderildigi gibi görünürler..

**APPL\_MD\_PATH :**ISAPI.DLL uygulamalarında kullanılmak uzere metabase'in path i

**APPL\_PHYSICAL\_PATH : **IIS APPL\_MD\_PATH 'i fiziksel path e çevirmiş halidir.

**AUTH\_PASSWORD: **client'ın authentication dialogunda belirttiği değerdir. Basic authentication kullanıldığı zaman geçerlidir

**AUTH\_TYPE :**korumalı bir scripte erişmek isteyen userları değerlendirmak için serverin kullandığı authentication metodudur.

**AUTH\_USER :**doğrulanmış ancak işlenmemiş kullanıcı adı.

**CERT\_COOKIE :**client sertifika'e ait Unique ID

**CERT\_FLAGS :**client sertifika sı varsa 1 değeri ni alır yoksa 0 değerini alır.

**CERT\_ISSUER :**client sertifika yayınlayıcısına ait bilgiler(O=MS, OU=IAS, CN=user name, C=USA).

**CERT\_KEYSIZE :**SSL bağlantısının kaç bit üzerinden yapılığını belirtir.

**CERT\_SECRETKEYSIZE : **server certificate private key'indeki bit sayısı. 1024 gibi

**CERT\_SERIALNUMBER:**client sertifika 'sının seri numarası

**CERT\_SERVER\_ISSUER :**server sertifika'sının yayınlayıcısı

**CERT\_SERVER\_SUBJECT : **server sertifika sının konusu

**CERT\_SUBJECT :**client sertifika sının konusu

**CONTENT\_LENGTH:**client taraftan gelen toplam bilginin uzunluğu

**CONTENT\_TYPE :**client tan gelen verilerin gonderiliş şekli örneğin GEt,POST veya PUT gibi

**GATEWAY\_INTERFACE:**serverin kullandığı CGI sartnamesi. CGI/revision formatındadır

**HTTP\_<HeaderName> :**HeaderName de saklanan başlık değeri.Başlık oluşturulurken kullanılan \_(alt çizgi) server tarafından -(tire) olarak algılanır.

**HTTP\_ACCEPT :**Accept başlığı

**HTTP\_ACCEPT\_LANGUAGE: **contenti yani clienttan gelen veriyi gösterebilmek için kullanılan dili ifade eden string bir değer

**HTTP\_USER\_AGENT :**istemde bulunan browserı belirten bir string değerdir.

**HTTP\_COOKIE :**istemle birlikte gelen bir cookie stringi.

**HTTP\_REFERER :**bir yonlendirme olduğu zaman esas isteme ait url yi tutan bir string değeri

**HTTPS :**ON ise SSL aglantısı uzerinden istemler gerçekleşiyor dur OFF ise non-secure bir iletişim yapılıyor demektir.

**HTTPS\_KEYSIZE :**SSL bağlantısının kaç bit üzerinden yapıldığını belirtir.

**HTTPS\_SECRETKEYSIZE: **server certificate private key deki bit sayısı

**HTTPS\_SERVER\_ISSUER :**server sertifika'sının yayınlayıcısı

**HTTPS\_SERVER\_SUBJECT :**server sertifika sının konusu

**INSTANCE\_ID :**IIS icin kullanılan bir ID

**INSTANCE\_META\_PATH:**istemden sorumlu ISS icin metabase path'i

**LOCAL\_ADDR :**istemi cevaplandıracak serverin adresi.

**LOGON\_USER :**userin hangi Windows accountunu kullandığını belirtir.

**PATH\_INFO :**PATH\_INFO ve Virtual pathi kullanarak scriptlere erişebilirsiniz.Bu bilgi bir URL ile gelirse CGI script ine gonderilmeden once server tarafından desifre edilir.

**PATH\_TRANSLATED :** PATH\_INFO nun pathi alıp virtualdan fiziksel yola cevirilme işlemlerinin yapılmış hali olan dir..

**QUERY\_STRING :**HTTP isteminde ? den sonra gelen değişkendir.

**REMOTE\_ADDR :**istemi yapan makinanın adresi

**REMOTE\_HOST :**istemi yapan host makina

**REMOTE\_USER :**istemi yapan makinaya login olmuş kullanıcının accountundaki username

**REQUEST\_METHOD: **istem yapılırken kullanılan metod. GET, HEAD, POST gibi.

**SCRIPT\_NAME :**calışan scriptin virtual pathi

**SERVER\_NAME :**The serverin host name, DNS alias veya IP address

**SERVER\_PORT :**istemin yapıldığı port numarası

**SERVER\_PORT\_SECURE :**Secure bağlantı varsa 1 yoksa 0 değerini alır

**SERVER\_PROTOCOL :**The name and revision of the request information protocol. The format is protocol/revision.

**SERVER\_SOFTWARE: **istemlere cevapveren ve gatewayin uzerinde bulunduğu serverin adı ve kullandıgı sunucu yazılımı.name/version formatındadır.

**URL :**URL adresi

Bahriye BAŞTÜRK , ASP

---
*Kaynak: `ASP ANA OBJELER/ASP ANA OBJELER.doc` — ekim kaya — 2004*
