# ASP Giriş

Editörlerimizden Bahriye Baştürk tarafından derlenen bu yazı ASP konusunda size detaylı bir kaynak olacağına inanıyoruz. Yazının ilk bölümünde genel olarak asp ye giriş yapılıyor ve activex server bileşenlerinden bahsediliyor

Organizasyonlar İnternetiverimi artırmak, maliyeti azaltmak ve varolan bilgi ve veriye yeni dinamik ve interaktif yollardan erişimi sağlamak amacıyla kullanıyorlar.Bir işyeri için internet uzerinden yapılabilecek uygulamalardan sadece bir kaçı örneklenecek olursa;

\# İşçi kayıtlarının çıktısını almak yerine online olarak yayınlayabilirsiniz. Böylece işçilerin girip kendilerine ait kayıtları guncellemeleri ilede idari masrafları azaltmış olursunuz.

\# Envanter veritabanlarınızı online store’a bağlayabilirsiniz ve processing sistemi düzenleyebilirsiniz.

\# Sitenize giren her ziyaretcinin ilgilendigi alanları belirleyerek bu alanlarda son ziyaretlerinden itibaren olan gelişmeleri duyurabilirsiniz.

Microsoft internet information server(IIS) ASP ile internet ve tumleşik intranet uygulamaları gelistirmek icin tasarlanmış guclu bir platformdur. Webmasterlar ActiveX scriptlerini ve server tabanlı çözümler uretmek icin yaratılmış, serverda çalışan activeX server bilesenlerini kombine edebilirler.

**ACTIVE SERVER PAGES:**ASP sayfaları HTML icine gomulmus scriptler seklinde yazilirlar.bu scriptler database’e ve uygulamalara erişim için ve veri işlemek için local server veya baska bir serverda calisan componentlere basvururlar.Bir browser ASP dosyasını cagiridigi zaman server bu sayfada bulunan kodları işler ve client tarafa standart HTML kodları gönderilir.

**AÇIKLIK**:IIS kullanıldıgında web uygulamaları geliştirmek için belli bir dil bilmek zorunda degilsiniz.Active server pages activeX scripting dillerinin tumu ile uyumludur.

Active server Pages default olarak Visual Basic scripting language(VBScript) ve Jscript destekler.plug-inler sayesinde REXX ,Perl ve Tcl gibi dilleride IIS ye veya web server’a bilesenlerinde eklenmesi ile destekleyecektir.Birden cok scripting dili tek asp sayfası içinde kullanılabilir.ActiveX server Bilesenleri hemen hemen butun dillerde yazilabilir.Bunlar c++,Java,visual Basic cobol ve dahasıdır.

ASP ile Web Uygulamaları geliştirmek kolaydır:HTML yazarlarına serverdaki web sayfalarına canlılık getirmeyi kolay kılar.özellştirilmiş sayfalar basit uygulamalar çok çabuk bir şekilde geliştirilebilir. Her kullnaıcı icin farklı bir içerik sunan dinamik sayfalar olusturmak için perl ve c gibi dillerde karmasık CGI kodları yazmaktansa web developerlar butun bu işleri ASP ile çok kolay bir şekilde yapabilirler.Aşagidaki örnekte o kullanıcının ip adresi o anki zaman ve client tarfın kullandıgı browserin tipi kullnıcıya yansıtan VBScript ile yazilmis ASP kodlarını görmektesiniz.

| <HTML> <HEAD> <TITLE>Deneme</TITLE> </HEAD> <BODY> <P> Merhaba <%= Request.ServerVariables(“REMOTE\_ADDR><br> Şu an saat <%= now %><br> Kullandıgınız browser <% =Request.ServerVariables(“http\_user\_agent”) %> </BODY> </HTML> |
| --- |

Bu kodların çıktısı aşağıdaki gibi olacaktır:

Mantık ve lojiği presentasyondan ayırır:Web işi grafik,Html,programcılık,yayınlama gibi bir cok işi bir arada toplar.Asıl zor olan bunlarin birara verimli bir şekilde çalışmasına sağlamak ve biribirinin işini aksatmayacak şekilde değişiklikler yapmak.bugun dinamik bir içerikte olması gerekenler tasarım, lojik ve içeriktir.Perl ve C kodlarında değişiklik yapmak uygulamayı zorlastıracaktır ve yanlışlıkla yapılacak bir değişiklik programı veya HTML formatını tamamıyle bozabilir.

Scripting ve bilesenlerin kullanılması sayesinde asp veritabanındaki verilere erişim için yazılmış bir programı ve uygulamayı tasarımdan ve web sayfasınıın diger içeriklerinden ayırır.

Bu, uygulama geliştiricilerin business lojiklerini istemci tarafa yansır endisesi tasimadan html kodlarının icine yazabilmelerini saglar.tasarımcılar sayfalarını deidikleri şekilde tasarlamakta ozgurdurler.scripting program ile HTML birleştiren bir kopru gorevi ustlenmiştir.

Aşağıdaki örnekte bir form ile gonderilen URL aracılığı ile alınan ticker symbol degişkeni ASP dosyasına gonderiliyor.ASP Dosyasının ilk kısmında stok fiat serverI ile bağlantı kuracak component çağırılıyor.bu nesnenin fiatı acma kapama gibi özellikleri HTML icine kolayca yazılabilir.Programcı istedigi dilde calişabilir.Endişe edilecek tek nokta stok fiar server’i ile nasıl haberleşileceğidir.HTML yazıcısınında bilmesi gereken tek sey componenti nasil yazacagidir,stok fiat server inin nasil calisacagi onu ilgilendirmez.

| <HTML> <% TSym=Request.QueryString("TickerSymbol") Set NObj=Server.CreateObject("NASDAQ.TickerObj") if NObj.GetCompany(TSym)=False then Server.Redirect("ticker/entryform.htm") %> <H1>Gunluk satış raporu<%=NObj.CompanyName%> </H1> <TABLE> <TR><TD>Open</TD><TD>Close</TD><TD>Volume</TD></TR> <TR><TD><%=NObj.Open%></TD> <TD><%=NObj.Close%></TD> <TD><%=NObj.Volume%></TD></TR> </TABLE> <H2>rapor zamanı<%=time()%><%=date()%></H2> </HTML> |
| --- |

Manul Derleme yoktur:kodlarda bir değişik oldugu zaman programı tekrar derlemek yerine ASP dosyalarında bir sonraki request yani istem yapıldığı zaman server yeni ASP kodlarını derler ve serverin cache in yukler istemci tarafada yeni sonuclar gitmiş olur. Sitenizi yaparken ASP dosyalarınızsa değişklik olduğu zaman sadece refresh etmeniz yeterli olacaktır.

Browserdan Bağımsızdır:ASP uygulamaya browser açısından tarafsız bir yaklaşım sağlar. Dinamik bir içerik sağlamak için oluşturulan uygulama mantığının tümü server uzerinde çalıştığı için uygulama geliştiricileri web sitelerinin hangi browser tarafından görüntülendigi konusunda endişelendirmez. Browserlar sadece ASP dosyasının işlenmesi sonucu oluşan çıktıyı yansıtırlar scriptler serverda çalışır.

**SCRIPTING ve ACTIVE SERVER PAGES: **Active Server Pages dinamik,interaktif yuksek performanslı web server uygulamaları oluşturmak ve çalıştırmak server taraflı bir scripting ortamı sağlar. Server taraflı scripting web serverinizin ozelleştirimiş HTML sayfalrı olusturmada gerekli bir işi yapmasını sağlar. Örneğin usera gore userin browserinin tipine veya ozelliklerine gore sitenize nerden bağlandıklarına gore yada bir alisveris siteniz varsa musterinizin daha once aldigi urunlere gore farklı sayfalar gelmesini sağlayabilirsiniz.

Scripting dilleri C,C++,ve visual Basic gibi programlama dilleri ve HTML arasında bir basamaktır. HTML genel olarak format berlemede kullanılırken programlama dilleride bilgisayarlar karmaşık komutlar vermek için kullanılır.scripting dilleri ise bircok masaustu uygulamasındaki macro dilleri gibi bunlar arasında bir yere sahiptir.

Active server Pages scripting enginelerin kullanımı ile tum ActiveX scriptinng dillerini desteklerler. Scripting engineler Component Object Model(COM) denilen scriptleri işleyen nesnelerdir.IIS VBScript ve Jscript dillerini desteklemektedirler ve REXX,Perl,Tcl ve diger scripting dilleri içinde plug-in ler mevcuttur.

Active Server Pages web uygulaması geliştiricilerinin değişik scripting dilleri kullanmalarını mumkun kılar.Bunun nedeni scriptlerin client taraflı scriptingin tersine server tarafında işleniyor olmasıdır.Aslında tek ASP sayfasında birkaç scripting dili kullanılabilir.Bu bir tagin icinde script dilinin belirtilmesi ile yapılır.Örneğin aşağıdaki scriptte Active server Pages tarafında işlenecek olan jScript ve ardındanda Vbscript kodlarının hangi script diline ait oldugu onceden belirtiliyor.

| <html> <script language=”jscript” RUNAT=Server> <Jscript kodları bu kısma yazılır> <script language=”VBScript” RUNAT=Server> <VBscript kodları bu kısma yazılır> </html> |
| --- |

**ACTIVEX Server Bileşenleri:**IIS nin bir avantantajı ActiveX Server Componentleri’ne destek veren web çözümleri için component tabanlı uygulama gelişimini sağlamasıdır.Active Server Pages C++,Visual Basic,Java yada Cobol gibi herhangi bir dilde yazilmis ActiveX Server Componentlerini çalıştırmanıza olanak sağlar.IIS filtreler ve ozel web uygulamaları icin CGI ve ISAPI pprogramlarını desteklemeye devam ettiği sürece ,Active Server Componentleri uygulama geliştirmeleri için güçlü,component tabanlı bir yaklaşım sunar

**ACTIVEX Server Bileşenlerinin Yararları:**ActiveX server componentleri(bileşenleri) daha onceki bilinen adıyla OLE otomasyon Serverları web uygulamalrının bir parçası olarak web server uzerinde çalışmak uzere tasarlandılar.Bu componentler scriptinizin fonksiyonelliğini artırabilirler.Bu birçok programcının component ve bu componentleri olusturmada kulanılan cogu geliştime aracını geliştirmeyle yakından ilgili olmasını kesinleştirir. Dahası bircok ActiveX componenti zaten hazır olarak bulunmakta ve web uygulamalrı geliştirmek için hazır bloklar halinde kullanıma hazır haldedirler.

Yazılış şekillerine bağlı olaraktan ,ActiveX server componentleri bir web brpwser uzerinde de çalışabilirler ve geleneksel client-server uygulamaları ve uygulama plug-inleri gibi web server dışındaki ortamlardada kullanılabilirler.

---
*Kaynak: `ASP GİRİŞ/ASP GİRİŞ.doc` — ekim kaya — 2004*
