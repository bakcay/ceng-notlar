# ASP Üzerine

**Giriş**

ASP, Windows NT 4 işletim sisteminin kullandığı client/server mimarisine paralel olarak işleyen bir web sayfası/sitesi yazma ve geliştirme aracıdır. ASP sayesinde web geliştiricileri kolaylıkla web sayfalarını interactive ve dynamic olarak tasarlayabilirler. ASP için, geliştirilen tipik bir web uygulaması öncelikle bilinen geleneksel uygulama geliştirme araçları vasıtasıyla (örneğin C++ gibi) derlenmelidir. Uygulama derlendikten sonra, web server’daki CGI dizinine kopyalanır. Uygulamada yapılan en küçük bir değişiklikte bile uygulama tekrar derlendikten sonra aynı dizine yerleştirilir.

Visual Basic veya Jscript / JavaScript veya VBScript gibi bir web scripting dilinin bilinmesi daha öncden kullanılıyor olması ASP’nin kullanılışı sırasında bir avantaj olarak gelecektir. Çünkü ASP ile birlikte web ortamı içerisinde VBScript, Jscript/JavaScript veya Perl gibi scripting dilleride kullanılabilmektedir.

**Hafta 1**

**Bölüm 1**

**ASP’ye ve IIS (internet information server)’a Giriş**

ASP Microsoft’un en yeni web server teknolojilerinden birisidir ve web uygulamaları geliştirmeyi oldukça kolaylaştırmaktadır. ASP, JScript ve VBScript gibi scripting dillerine benzemekte fakat server tarafında çalışmaktadır. ASP’nin VBScript, Jscript, Perl veya diğer scripting dillerini desteklemesi nedeniyle web geliştiricileri daha başka scripting dillerini öğrenmek zorunda kalmazlar. Böylece ASP web geliştiricilerinin var olan bilgilerinden yararlanabilmelerini de sağlamaktadır.

| PRIVATE**NOT****** |
| --- |
| ASP direkt olarak VBScript, Jscript ve JavaScript scripting dillerini desteklemektedir. Ek scripting dilleri desteği (örneğin Perl) Bölüm 13’te (İleri Uygulamalar) anlatılacaktır. |

Bugün, ASP ile ilk tanışma yapılacak ve ASP’nin kendine has avantajları ve ASP ile yapılabilecekler ortaya konulacaktır. ASP interactive web uygulamaları geliştirmeyi kolaylaştıran bir teknolojidir. Bu notları okuduktan sonra, ASP’nin web uygulamaları için çok yararlı bir teknoloji olduğunu göreceksiniz. CGI ve ISAPI’nin de çok kullanışlı olmasına karşın, ASP kullanmanın getirdiği yararlar bölümünde ASP’nin farklı avantajları verilecektir.

**ASP Nedir ?**

ASP Microsoft’un temel internet stratejisi Active Platform’un önemli bir parçasıdır. Active Platform dillerin, standartların ve hem Active Desktop (client side, kullanıcı tarafı) hem de Active Server (server side, sunucu tarafı) uygulamaları için gereken servislerin ortak bir setidir. Active Platform yaklaşımı, ister kullanıcı tarafında ki , isterse de sunucu tarafında ki uygulamalar için oldukça geniş bir yelpazede avantajlar sunmaktadır. Ayrıca bu yaklaşım, desktop (masaüstü) uygulamalarının tamamen client/server taraflı uygulamalara dökümü işini de kolaylaştırır.

Aslında ASP web server üzerine yüklenmiş bir component’tir. Bu component uzantısı .asp olan dosyaları işler ve bu asp dosyalarının istemlerine cevap verir. Fakat bu durum ASP’nin ISAPI (internet server application programming interface) veya IDC (internet database connector) gibi render teknolojisi olduğu manasına gelmez. Daha doğrusu, ASP, IDC ve ISAPI uygulamaları için tamamlayıcı bir teknolojidir. Örneğin; eğer çoğu zaman sorgulamaya gerek kalmayan basit bir data kayıt uygulaması ortaya koymak istiyorsanız bu durumda basitce IDC teknolojisi kullanırsınız. Fakat eğer data sorgusu, transmisyonu (bazen replikasyonu) ve kompleks hesaplamalar içeren uygulamalar ortaya koyacaksınız tabii ki ASP daha uygun bir teknolojidir. Göreceğiniz gibi, geliştiricinin her bir teknoloji için farklı bir ortam kullanması gerekse bile, ASP diğer web teknolojilerini tamamlayan bir teknolojidir.

| PRIVATE**NOT****** |
| --- |
| Dosya uzantısı ile ASP tanımlayıcısı arasındaki tanımlama **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\W3SVC\\Parameters\\ScriptMap **registry anahtarı vasıtasıyla sağlanır. .asa ve .asp uzantılı dosyalar ise **...\\System32\\inetsrv\\ASP\\ASP.dll **dosyası ile ilişkilendirilmiştir. |

**ASP Kullanmanın Getirdiği Yararlar**

ASP kullanmanın getirdiği birçok avantajlar vardır. Bu avantajlar sayesinde çok karmaşık uygulamalar dahi gerçekleştirilebilir.

ASP ile uygulama geliştirme kolay öğrenilebilir.

ASP ile uygulama geliştirme ortamı ortaya konulan bilgi birikiminin daha iyi kullanılmasını sağlar.

ASP ile uygulama geliştirme ortamı mevcut hünerlerin de daha iyi kullanılmasını sağlar.

ASP uygulamalarının derlenmesi zahmetsizdir.

ASP ortamı gelişmeye açık bir ortamdır.

ASP sahip olunan algoritmaların ve bilgilerin korunmasını sağlar.

**ASP ile uygulama geliştirme kolay öğrenilebilir**

ASP bir web sitesine farklı seviyelerde interaktivite ekleyebilir. ASP’nin sağlamış olduğu avantajlarda Visual Basic veya VBScript, JScript veya JavaScript gibi scripting dilleri ile beraberce kullanılabilmesinin de etkisi vardır. Çünkü VBScript, BASIC’e çoğu yönden benzer ve programlamaya yeni başlıyor olsanız bile öğrenilmesi kolaydır. Eğer C veya C++ kullanmışsanız, JScript ve JavaScript’tide öğrenmeniz oldukça kolay olacaktır.

**ASP ile uygulama geliştirme ortamı bilgi birikiminin daha iyi kullanılmasını sağlar**

Örneğin Microsoft Office ve benzer uygulamalar ile değişik projeler ve database uygulamaları oluşturmuş iseniz zaten belirli bir birikiminiz var demektir. ASP var olan bilgi birikiminizi internet için yönlendirmenizde oldukça kullanışlı bir yaklaşımdır. Örneğin, Gün 8 “ActiveX Data Objects (ADO) Kullanarak Web Ortamlı Database Programcılığına Giriş”’da ve Gün 9 “İleri Seviye Web Database Programlama”’da görüleceği gibi ASP’nin database özellikleri kullanılarak ODBC-yönelimli database uygulamaları web arayüzleriyle ortaya konulabilir.

**ASP ile uygulama geliştirme ortamı mevcut hünerlerin de daha iyi kullanılmasını sağlar**

ASP, VBScript, JScript/JavaScript veya Perl gibi benzer scripting dilleri kullanılarak web uygulamalarının ortaya konulmasını sağladığı işlevsellik ile basitleştirir. Ayrıntılı VBScript eki Ek-A, VBScript Okuma ekinde yer almaktadır.

**ASP uygulamalarının derlenmesi zahmetsizdir**

ASP’den önce, tipik bir interaktif web uygulaması için uygulama geleneksel yöntemler ile hazırlanır ve bir derleme ortamı vasıtasıyla derlenir (örneğin Visual C++), daha sonra da web server’in CGI dizinine kopyalanırdı. En ufak bir değişimde bile çalıştırılabilir uygulama tekrar derlenir ve tekrar CGI dizinine yerleştirilirdi. Bu özellik kullanışlılığı azaltan bir durumdur. ASP bu problemi ortadan kaldırmaktadır. Bir ASP uygulaması oluşturulduktan sonra uygulamanın derlenmesine gerek yoktur. Uygulama basitce .asp uzantılı olarak kaydedilir ve ASP DLL dosyası da kullanıcı istemi geldiğinde bu uygulamayı yürürlüğe koyar. Caching ASP’nin performansını artırmaktadır.

**ASP ortamı gelişmeye açık bir ortamdır**

ASP tamamen gelişmeye açık, esnek bir ortamdır. Örneğin gömülü (built-in) nesnelerle database erişimlerinin mümkün kılınması veya dönüşümlü reklam banner’larının oluşturulması uygulamaları gibi. Gömülü ASP komponentlerine ek olarak kullanıcı (programcı) kendi şahsi komponentlerini de oluşturabilir. Bu durum Gün 10’da “Özel ActiveX Komponentlerinin Oluşturulması” bölümünde verilecek ve bu komponentlerin yazımı için Visual Basic kullanılacaktır.

**ASP sahip olunan algoritmaların ve bilgilerin korunmasını sağlar**

Client-side scripting dillerini kullanmanın bir dezavantajı kullanıcı müdahalesine açık olmasıdır. Örneğin, satıcı, yılın belirli günlerinde, belirli ürünlerin fiyatlarında indirime gidiyor olsun (Aralık 20 ve Ocak 1 arasında % 20). Bu aslında satıcının müşterilerini haberdar kılmak istediği öncelikli bir durum değildir fakat yinede müşteriler bu durumdan haberdar olabilirler ve webdeki uygulama bir client-side scripting dili ile, örneğin VBScipt, hazırlanmış ise müdahaleye direkt açık olabilir ve sayfanın kaynak kodu kolayca değiştirilebilir. Fakat ASP kullanımı durumunda böyle bir olayla karşılaşılmayacaktır. Çünkü ASP, sunucu taraflı (server-side) çalışan bir web uygulama dilidir.

**ASP Uygulamaları Geliştirmek İçin Microsoft Visual Interdev Kullanmalımıyım ?**

Microsoft Visual Interdev ASP uygulamaları için hızlı bir uygulama geliştirme aracıdır (RAD, rapid application development). Fakat mutlaka olması, bulunması gerekmez. ASP teknolojisi IIS 3.0 tarafından içerilmektedir. Bununla beraber komplike ASP uygulamaları Microsoft Visual Interdev ile rahatlıkla geliştirilebilir. Bu durumda, ASP uygulamaları geliştirmek için Microsoft Visual Interdev’in bir kopyasının edinilmesi bir öneri olarak sunulabilir. ASP database uygulamalarının kolayca gerçekleştirilebilmesi Microsoft Visual Interdev’in en dikkat çekici özelliklerinden birisidir.

**ASP Uygulamaları Geliştirmek İçin Gereksinimler**

ASP uygulamaları geliştirmek için gerekenler iki farklı grupta toplanabilirler:

yazılım/donanım gereksinimleri

teknik gereksinimler

Minimum yazılım ve donanım gereksinimleri:

pentium tabanlı bir bilgisayar

32 MB Ram

100 MB civarı boş sabit disk alanı

TCP/IP protokolü kurulmuş ve konfigüre edilmiş bir Windows NT Server 4.0 sunucu

| PRIVATE**NOT****** |
| --- |
| Windows 95/98 de ASP uygulamaları geliştirmek için kullanılabilsede tavsiyemiz Windows NT 4.0 işletim sisteminin kullanılmasıdır. Bunun sebebi Windows NT 4.0’ın dikkate değer güvenlik, performans ve uygulama-bütünlüğü yetenekleridir. Ayrıntılı bilgi için bu bölümdeki “Gerçekten Windows NT Server 4.0’a İhtiyacım Var mı ?” bloğuna bakınız. |

IIS 3.0 veya daha üstü Windows NT Server 4.0 kullanılıyor ise gereklidir. PWS (personal web server) ise Windows 95/98 kullanılıyor ise, Microsoft Peer Web Services ise Windows NT WorkStation kullanılıyor ise gereklidir. Aslında ASP’nin bir ISAPI uygulaması olması nedeniyle, IIS 3.0 veya daha üst versiyonunun ASP komponentinin download edilmesi ve kurulması ile ISAPI uygulamalarının gerçekleştirilmesine yetkin bir web server elde edilmesi sayesinde çeşitli database uygulamaları ortaya konulabilirler. Bununla beraber, en iyi ASP integrasyonu, IIS ve PWS/Peer Web Services ile sağlanabilir.

ODBC desteği veren bir database ve sürücüsü (Microsot Access veya Microsoft SQL server gibi)

Microsoft Visual Interdev önerilir fakat mutlaka kullanılıyor olması gerekmez

ASP uygulamaları geliştirimi için teknik gereksinimler

Microsoft NT Server 4.0 yatkınlığı

Microsoft NT Server 4.0 güvenliği ve NTFS (NT File System) dosya sistemi izinleri hakkında temel bilgi

Visual Basic veya VBScript, JScript/JavaScript gibi scripting dilleri hakkında temel bilgi

**Niçin Windows NT ve IIS/ASP Seçilmelidir ?**

ASP uygulamaları geliştirmeden önce, Windows NT Server 4.0 ve IIS/ASP’nin niçin seçildiklerinin anlaşılması çok önemlidir. Eğer Windows NT veya Unix gibi serverları web yayımlamak için kullanıyorsanız, özellikle Windows NT Server 4.0’ın unique (kendine has) özellikleri ve bunlardan nasıl yararlanılabileceği öğrenilmelidir. Internet üzerinden yayımcılık sırasında Windows NT ve IIS’ın seçilmesinin birçok avantajı (yararı) vardır. Windows NT temelde mission-critical uygulamalar için seçilen bir işletim sistemidir (güvenlik gerektiren, mission critical). Windows NT takımı üst yöneticilerinden Dave Cutler, VMS işletim sisteminin tasarımcısıdır. NT geliştirme takımı çalışmalarında Mach Microkernel’i (Carnegie-Mellon Üniversitesi’nde geliştirilen Unix’in bir benzeri) ve VMS’yi, NT’nin ortaya çıkarılmasında kullanmıştır. Unix’ten ayrık olarak, Windows NT’nin başlangıç masrafı düşüktür. PC sistemlerine rahatça kurulabilir ve yönetim kolayca icra edilebilir.

**Niçin Windows NT Seçilmelidir ?**

IIS ve ASP ile bütünleşmiş bir Windows NT, web uygulamaları geliştirme ve yürürlüğe koyma açısından çok kuvvetli bir platform teşkil etmektedir.

**Gerçekten Windows NT Server 4.0’a İhtiyacım Var mı ?**

ASP uygulamaları Windows NT 4.0 WorkStation veya Windows 95/98 kullanılarakta geliştirilebilirler. Bununla birlikte, aşağıdaki nedenlerden dolayı ASP uygulamalarının yürürlüğe geçirilmesinde Windows NT Server kullanılmalıdır:

Windows NT Server en iyi performansı sağlayacaktır

Windows NT Server çok daha güvenlidir

Windows NT Server enterprise-seviye’li uygulamalarla (örneğin Microsoft SQL Server) daha tümleşiktir.

**Windows NT Server en iyi performansı sağlayacaktır**

Windows NT Server, yoğun ağ ortamlarında ki sunucu uygulamaları için en iyi başarımı verecek tarzda optimize edilmiştir. Diğer taraftan, Windows 95/98 ve Windows NT WorkStation ise en iyi verimliliği sağlayacak tarzda optimize edilmişlerdir. Bu nedenle, ASP uygulamaları devreye girdiğinde tabii ki en iyi performans Windows NT Server’dan alınacaktır.

**Windows NT Server çok daha güvenlidir**

Internet Information Server 3.0 Windows NT Server 4.0 altında NTFS güvenliğini kullandığı için, Microsoft NT Server, ASP uygulamaları için çok güvenli bir platform olmaktadır. Windows 95/98, Microsoft Personal Web Server (Internet Information Server’in güvenlik seviyesi düşük bir versiyonu) kullandığı için, Windows NT ve NTFS dosya sisteminin sağladığı güvenlik seviyesine erişemeyecektir.

**Windows NT Server Enterprise-Seviyeli Uygulamalar İle Daha Tümleşiktir**

Enterprise-seviye’li uygulamalar, Microsoft BackOffice ile beraber gelen uygulamalar (Microsoft SQL Server, Microsoft Exchange Server vs...), Windows NT Server’a gereksinim duyarlar. Bu nedenle eğer ASP uygulamalarınız BackOffice uygulamaları ile paralel çalışacak ise Windows NT Server sorun çıkartmayacak aksine güçlü bir platform oluşturacaktır.

**ASP Client-Side Scripting’i Nasıl Tamamlar**

ASP uygulamaları client-side scripting dillerinin yerini alamaz. Fakat, web sitesi geliştiricilerine client-side scripting dilleri ile daha interaktif web sitelerinin oluşturulması hususunda tamamlayıcılık arz eder. Gün 2 “ASP Uygulamaları Geliştirmenin Temelleri” bölümünde, client-side scripting’in server-side scripting ile nasıl tamamlandığını ve nasıl daha zengin interaktif içeriklerin oluşturulacağını öğreneceksiniz.

Ek-A’da görüleceği gibi, bir web sitesine client-side scripting ile değişik seviyelerde interaktif özellikler ekleyebilirsiniz. Örneğin, web sayfasındaki bir formun işlenmesi sırasında, form henüz web server’a gönderilmeden önce eğer varsa formdaki bilgi eksiklikleri veya hataları bir VBScript ile kullanıcıya bildirilir ve düzelttirilebilir. Bununla beraber bazı web browser’ları client-side scripting’i desteklemeyebilir. Böyle bir durumda, server-side scripting devreye girer ve daha zengin ve daha interactive web denetimleri sağlanır. Gün 5 “ActiveX Komponentlerinin Kullanılışı” bölümünde görüleceği gibi browser yeterlilikleri client-side scripting ile anlaşılabilecektir.

**ASP Uygulamalarının Yayımı İçin IIS’ın Kullanılması**

Bu bölüm, ASP uygulamalarının yayımı için IIS’in nasıl kurulacağını, nasıl konfigüre edileceğini ve nasıl yönetileceğini kapsamaktadır. IIS, ASP’nin temelidir. Bu yüzden IIS’in nasıl kurulacağının, konfigüre edilmesinin ve yayımın nasıl yapıldığının anlaşılmasının önemi büyüktür.

---
*Kaynak: `ASP ÜZERİNE/ASP ÜZERİNE.doc` — Alper Basturk — 2004*
