# Internet, Web Server Ve Web Tarayicilari

## **BÖLÜM 1**

## **INTERNET, WEB SERVER ve WEB TARAYICILARI**

## **1.1. INTERNET **

HTML dilini öğrenmenin amacı, ya bir web sayfası ya da bir web sitesi oluşturmaktır. Bir web sayfası ya da bir web sitesi oluşturmak için de bilmek gereken bir çok kural vardır. Bu kurallar ise Internet’ in çalışma tarzından ve protokollerinden doğan kurallardır.

**Internet’ in Tarihçesi**

Internet, 1970’ lerde Amerika Savunma Bakanlığının çeşitli araştırma projelerinde çalışan bilim adamları, üniversiteler ve araştırma kurumları arasında bilgi alışverişini sağlamak için oluşturulmuştur. Amerika Genelkurmay Başkanlığının Savunma Araştırmaları Proje Dairesi (DARPA) tarafından, hangi bilgisayarın, hangi bilgisayara günün hangi saatinde bağlanacağını ve aralarında bilgilerin hangi ilkelere göre alınıp verileceğini belirleyen bu sistem (ARPANET), bilim adamları arasında haberleşmeyi ve çok büyük bilgisayar dosyalarını alıp-vermeyi o kadar kolaylaştırdı ki, bir süre sonra sistem askeri nitelik taşımayan ve fonu Savunma Bakanlığı tarafından sağlanmamış projelerle ilgili bilgi aktarımında da kullanılmaya başlandı. Üniversiteler, özel firmalara ARPANET sisteminden (ve bu ağ üzerinde oluşturulan USENET sistemi) yararlanma hakkı satmaya başladılar. 1979 yılında Amerika Savunma Bakanlığı, üniversitelerarası haberleşme sisteminin bütün masrafını savunma bütçesinden karşılamanın haksızlık olduğunu belirterek, ARPANET sisteminden desteğini çekeceğini açıkladı.

1980’ lerin başlarında Amerikan Ulusal Bilim Vakfı (NSF), sadece ARPANET sistemine bağlı bilgisayarları değil fakat bazı üniversitelerdeki süper bilgisayarları birbirine bağlamaya karar vermiş ve bu amaçla Cornell Üniversitesi Teori Merkezi (Kısaca, NY), Illionis Üniversitesi Ulusal Süper Bilgiişlem Uygulamaları (NCSA, Urbana, Champaign), Pittsburgh Üniversitesi Süper Bilgiişlem Merkezi (Pennsylvania), California Üniversitesi San Diego Süper Bilgiişlem Merkezi (California) ve Princeton Üniversitesi John Von Neumann Merkezi (New Jersey) arasında TCP/IP standardı ile çalışacak bir bağlantı için harekete geçmişti. Amaç, bu süper bilgisayarları Amerika ye Kanada’ daki bütün bilim adamlarının hizmetine sunabilmekti. NSF, *5 *merkez arasında *56 *Kbps bir ağ için gerekli parayı sağladı ye bu merkezlerin çevresindeki bütün üniversitelere, fiziken bu ağa ulaşabiliyorsa, bağlanabileceklerini bildirdi. Bu dev bilgisayarlardan yararlanmak isteyen çok sayıda üniversite daveti kabul etti ve Internet’ in çekirdeği toprağa atılmış oldu.

Bir süre sonra kullanıcılar, bu ağın, sadece beş büyük süper bilgisayardan yararlanmaya değil, ağa dahil bilim adamı meslektaşlarına elektronik posta göndermeye, dosya aktarmaya ve haber grupları oluşturmaya yaradığını gördüler. Böylece ağın trafiği birden arttı. Kasım 1987’ de, NSF, Michigan Üniversitesi Bilgisayar Merkezi, Merit şirketine IBM, MCI ve Michigan eyalet hükümetleriyle ortaklaşa, mevcut 56Kbps’ lik ağı 1,544Mbps (ki bu bağlantıya daha sonra T1 adı verilecekti) hızına çıkartma işini ihale etti. Yeni ağ, ilk beş merkez ile Kolorado eyaletinin Boulder kentindeki Ulusal Atmosfer Araştırmaları Merkezi’ ni ve Michigan Üniversitesi’ ni de kapsayacaktı. İhaleden sekiz ay sonra 1 Temmuz 1988’ de T1 omurgası hizmete girmiş ve ilk ay içinde 152* *milyon “data paketi” aktarılmıştı. Projenin ortaklarından MCI telefon şirketi Michigan eyaletinin Ann Arbor kentinde Merit binasında 24 saat görev yapacak modern bin ağ denetim merkezi kurmuş ve omurgaya bağlı 13 yerde 170 yerel ağı izleme imkânı sağlamıştı. NSFNET, 24Temmuz 1988 günü 56 Kbps’ lık eski omurgayı kapattı.

Bu tarihte Amerika ve dünyanın çok yerinde üniversiteler ve özel sektör birçok “Bölgesel Internet” kurmuş bulunuyordu, ve bu bağlantı üyeleri, NSFNET’ e girmek için NSF şirketine baskı yapmaya başlamışlardı. Örneğin; Türkiye Üniversiteler ve Araştırma Kurumları Ağı (TÜVAKA) 1986’ da birçok Üniversite ve TÜBİTAK’ a bağlı araştırma merkezini birbirine bağlamış ve bu bağlantıyı, Amerika’ da EARN/BITNET ağı vasıtasıyla, dünyaya açmıştı. 1991-92’ de Orta Doğu Teknik Üniversitesi ve TÜBİTAK, bu bağlantıya RIPE adlı ağı ekleyerek network protokolü olarak IP kullanmaya başlamıştı. Bağlantı noktası olarak Fransa yerine Almanya’ nın tercih edilmesi ile 1994’ te Türkiye’nin dış bağlantı hızı 64 Kbps’ a çıkmıştı. Daha sonraki yıllarda, X.25* *ağı, kiralık hatlarla hızla gelişecekti.

Amerika içinde ve dışındaki bu baskılar sonucu, Ocak 1989’ da Merit-IBM-MCI ortaklığı, NSF şirketine, ağ hızını arttıracak ve giderek artan yükü kaldıracak bir güncelleştirme programı önerdi. Bu sırada IBM 45 Mbps (buna da T3 bağlantı hızı adı verilecekti) hızda çalışan ilk Router (ağ yönlendirme bilgisayarı) cihazını imal etmeyi başarmıştı. Vakfın verdiği 4 milyon dolar ile, Kasım 1991’ de omurga T1’ den T3’ e çıkartıldı, merkez sayısı 16’ ya, merkeze bağlı ağ sayısı ise 3500’ e çıkartıldı. İşte bu omurga, bugün Internet denilen mucizedir.

Bu tarihten sonra Internet günlük yaşantıya giren bir kelime oldu. Trafik, bir taraftan ticari nitelik kazanırken, diğer taraftan tek omurganın kaldıramayacağı kadar artmıştı. California eyaletinde Santa Clara kentinde Willtel telefon şirketi kendi routerını devreye sokarak, özel şirketlere NFSNET bağlantısı satmaya başladı. Aynı şeyi Federal Hükümet, Washington’ da yapıyordu. Bu gelişmeler üzerine NSF, 1993’ te, Network Access Pornts* *(NAP, Ağ Erişim Noktaları) adını verdiği dört nokta oluşturacağını ve arzu eden firmanın omurga kurarak, omurgasını bu noktada Internet’ e bağlayabileceğini duyurdu. Açılan ihalenin sonuçlarına göre, bu dört noktadan birincisi San Francisco’ da Bell telefon şirketi, ikincisi Chicago’ da Bell-Ameritech ortaklığı, üçüncüsü New York’ ta Sprint, dördüncüsü New Jersey’ de Pennsauken kentinde Metropoliten Fiber Systems tarafından işletilecekti. Bu noktalardan Sprint şirketine ait olan, Amerika dışı bağlantıları da sağlanacaktı. 30 Nisan 1995’ te, NFSNET resmen kapatılmış oldu. Bu ilk NAP bağlantılarına yeni omurgalar bağlandıktan sonra fiilen bağlantıları bağlama (enterkonnekte) merkezi doğmuş oldu. Fakat zamanla bu da önemini yitirdi, omurga işleticisi firmalar resmi bağlantı yerlerinin dışında da özel bağlantı merkezleri kurdular.

***Omurga Nedir?***

Bilgisayarlar arası bağlantı şebekesi (ağ, network) genel olarak router denen cihazlarla birbirine bağlanır. Bu cihazlara, yol bulan, yol veren anlamına gelen bu kelimenin verilmesi, cihazın kendisine ulaşan bir veri paketini okuyup, paketi üzerindeki “adrese yollamasından” kaynaklanmaktadır. Internet, birbirine bağlanmış routerlar zinciridir.

Routerlar arası en etkili iletişim yer kabloları ile bağlandığı için günümüzde routerların çoğu telefon sistemi ile birbirine bağlıdır. Telefon teli** **ile yapılabilecek bir iletişimin hızı ise azami 53 Kbps olabilir. Daha fazla hız için, routerların kiralık daimi bir hat ile birbirine bağlamak gereklidir. Kiralanacak hatların ise taşıyabilecekleri bilgi miktarı (hattın aktardığı elektrik sinyalinin frekansı) kullanılan telden tele ve mesafeye göre değişir. DS-0 (Data Service -0) adı verilen en basit hat, 56Kbps hıza sahiptir. DS-1 hattı kiralanırsa, bu hız 1544* *Mbps’ a çıkar. O zaman bu bağlantıya T1 bağlantısı denilir. 45* *Kbps hıza sahip hatta DS-2, kurulan bağlantıya T3 adı verilir. Kiralanan hattın optik olmasını arzu edilirse, OC-3 hattı kiralanabilir ve router 155* *Mbps ile bilgi alışverişi yapar. OC- 12 hat kiralanacak olursa kapasite 622 Mbps’ a çıkar. Omurga denilen şey, bir telefon firmasının veya benzeri bir başka iletişim şirketinin, routerları arasında kurduğu ana hattır.

“Ulusal Internet Omurga Sağlayıcı” firmalar, birbirleriyle NAP ağında bağlanırlar. Dolayısıyla aslında birden fazla olan omurgalar, Internet kullanıcısına bir tek “bilgi süper otoyolu” gibi görünür. Aslında bu süper otoyolunda, birincisi “Ulusal Internet Omurga Sağlayıcı” şirketler,..., dördüncüsü bizim abonesi olduğumuz IS Sağlayıcıları olmak üzere dört hız seviyesi vardır. Fakat bunu kesin bir kural olarak algılamamak gerekir. Zincirde dördüncü halka olan bir IS Sağlayıcıların, ikinci halkaya bağı T3 bile olabilir. Bu, IS Sağlayıcıların ödemek istediği kiraya bağlıdır. Internet kullanıcısı bir firma, isterse kendi IS Sağlayıcısına kiralık T1 hattı ile bağlanabilir. Ama IS Sağlayıcısına, üçüncü seviye bağlantı noktasına 56 Kbps bir hat ile bağlı ise, bu firma parasını çöpe atmış olur; çünkü binlerce dolar vereceği kablodan, herhangi bir Internet abonesi gibi azami 53 Kbps (56K bile değil) hızında iletişim sağlayacaktır (1).

## **2. Internet Nedir, Nasıl Çalışır?**

Internet bir demiryolu şebekesine benzetilebilir. Yüzlerce lokomotif ve binlerce vagondan oluşan bir sistemin, sonuç itibariyle aynı raylar üzerinde, belirli bir sisteme göre hareket etmesi gibi, Internet’ te yüzlerce omurga, binlerce omurgalar arası bağ, on binlerce hizmet sağlayıcıdan oluşan bir sistemle, milyonlarca kişiye hizmet sunuyor.

Internet, bilgisayar ağları arası ağ demektir. İki veya daha fazla bilgisayar arasında iletişim kurmak, bir başka deyişle bağımsız bilgisayarları bir ağ halinde birbirine bağlamak için her şeyden önce bu bilgisayarları bir suretle birbirine bağlamak gerektiği gibi bilgisayar ağlarını da birbiriyle alışveriş yapabilir hale getirmek için önce birbiriyle irtibatlandırmak gerekir.

Bu bağ oluşturulduğu zaman, karşımıza bir bilgisayarın birbirine bilgi aktarmalarını ve aktarılan bilginin doğru anlaşılmasını sağlayacak ilkeler üzerinde de anlaşmalarını sağlama sorunu çıkar. Aralarında alış veriş sağlayabilmek için, bilgisayarları ortak bir dil konuşur hale getirmek gerekir. Bilgisayar ağı ve Internet uzmanları, ortak iletişim diline “dil” yerine “protokol” demeyi tercih eder. Bir protokol ise sistemdeki bütün birimlerin birbirine nasıl ve hangi sırayla hitap edeceklerini gösteren ilkeler listesidir.

## **1.1.3. Internet’ te Kullanılan Protokoller**

Bir Web sayfasının ziyaretçinin ekranına kadar kat ettiği yolda, çeşitli protokoller (kurallar) ona eşlik eder. Bunların başında bir bilgisayar ağı olan Internet’in Hypertext dosyalarını ulaştırma kuralları (HTTP) geliyor.

Hypertext dosyalarını olduğu kadar çoklu ortam unsurlarını (ses, video ve diğer grafik unsurlarından oluşan Multimedya dosyalarını) ve bilgisayar programlarını, ağ içindeki bilgisayarlar arasında alıp-vermeye yarayan başka protokoller de vardır.

FTP** **(File Transfer Protocol - Dosya Aktarma Kuralları) bunlardan biridir. FTP, Internet’ te iki bilgisayar arasında dosya aktarmakta kullanılır. Bu dosyalar herhangi bir veri veya yazılım dosyası olabilir. FTP yönteminden, browser programın serverdan alıp ziyaretçinin ekranında oluşturması uzun zaman alabilecek dosyaların aktarılmasında yararlanılır.

Internet bağlantısını, bir telin iki ucunda bulunan iki bilgisayar arasındaki ilişki olarak görülebilir. Web sayfalarını içeren bilgisayar, Web ilişkisinde “SERVER” (Hizmet eden) diye adlandırılır. Ziyaretçinin bilgisayarı Internet’ e telefon bağlantısı ile bağlı ise “CLIENT” (Müşteri) sayılır. Hizmet veren bilgisayarla, bu hizmetin müşterisi olan bilgisayar (Server ile Client) arasındaki ilişkiyi düzenleyen kurallara TCP/IP (Transmission Control Protocol/ Internet Protocol- Aktarma Denetim kuralları-Internet Kuralları) adı verilir. Gerek HTTP gerekse FTP, müşterinin, sizin bilgisayarınızdan, Web Server olarak adlandırdığımız HTML sayfalarını ve bu sayfaların içinde yer alan resimlerin, grafiklerin, ses ve video dosyalarının durduğu bilgisayardan bilgi isteme ve bu isteğe karşılık verildiğinde verilen karşılığın doğru gelip gelmediğini anlamasını sağlar. Yani, gönderilecek bilginin küçük parçalara ayrılmasını ve karşı tarafta düzgün bir şekilde birleştirilmesini sağlar.

Müşteri bilgisayar ile servis sunan Web Server arasında oluşan bağlantı bazen kesilebilir. Fiziki bağlantının kesilmesi, aktarma işinin tümüyle kesilmesi, sona ermesi anlamına gelmemesi için, Internet Kurallarının IP bölümü, TCP’ ye göre paketlere bölünen bilginin fiziksel olarak bir cihazdan çıkıp diğerine en uygun yoldan gitmesini sağlar. Yani, iki bilgisayar arasındaki bağlantının doğru kanallardan kurulmasını sağlar. Ağları birbirine bağlayan sistemde, Gateway ve Router denen, ana geçitler ve yönlendiriciler vardır. Aslında bu cihazlar kendi başına birer bilgisayardan ibarettir. Router cihazları, kendilerine gelen bilgi paketinin üzerindeki adrese göre doğru yönde ilerlemesini sağlar. Bu işlemi yaparken, evrensel bir adres sisteminden yararlanır. Internet’ te servis sunan bilgisayarlar, başka bir deyişle Web Server, kaynak sayıldığı için, IP, aradığı kaynağı Universal Resource Locator (URL) denilen (Evrensel Kaynak Belirleyici) adres sistemini kullanarak bulur. Aynı kurallar demetinin TCP bölümü ise kurulan bağlantı sayesinde gelen bilgini doğru anlaşılmasını sağlar.

Birden fazla bilgisayar birbirine bağlandığında birbirlerine mesaj gönderme imkanları da vardır. Bu mesaja Elektronik Posta (E-Mail) deniliyor. E-Mail göndermek için de günümüzde Internet’ te iki protokol kullanılıyor. Simple Message Protocol (SMTP, Basit Mesaj Aktarma Protokolü), elektronik mesajların Internet’ te bir server bilgisayardan alınıp, adreste belirtilen server bilgisayarına aktarılmasını sağlayan kuralları içerir. Bu protokole uygun gönderilen elektronik mesaj demeti, en uygun, en elverişli yoldan gönderilir. Post Office Protocol (POP, Posta Dairesi Protokolü) ise server bilgisayarına ulaşan mesajların müşteriye (client) aktarılmasını sağlar. Internet server programlarının her iki protokole uygun elektronik mesaj hizmetleri vardır (1).

## **1.1.4. Internet ve Web İlişkisi**

Aslında her bilgisayar, Merkezi İşlem Birimi (CPU) ile ekran, klavye, CD-ROM sürücü, vb. arasında bir ağ demektir. Böyle bir ağın Internet’ ten farkı iki taraf birbirinin durumuna her an vakıftır; birbirlerinin ne durumda olduklarını her an bilirler. Oysa iki kıta arasında kurulmuş bir Internet ilişkisinde, müşteri hizmet verenin, hizmet veren müşterinin durumunu, bağlantıdaki kesilmeler nedeniyle, bilemeyebilir. TCP/IP, “durumun bilinmediği ilişki” esasına dayanır.

Müşteri bilgisayar servis sunucudan istediğini HTTP veya FTP kurallarına göre talep eder. Bunun için Web Serverın kendisini bulup bu talebi doğruca ona iletmesine gerek yoktur; bu talebi kendisine Internet bağlantısı sağlayan (ISP) firmanın bilgisayarına iletmesi yeterlidir. Bunu yaparken talep ettiği şeyin adını bildirdiği gibi, bulunacağı kaynağı belirlemek için gerekli adresi de (URL) bildirmek zorundadır. Internet hizmeti sağlayan firmanın bilgisayarı, bu talebi ve talebi karşılayacak kaynağın adresini, Internet’ in omurgası olan ana bağlantıyı kuran, bakımını yapan ve ISP firmalarına hizmet sunan firmanın bilgisayarına iletir. Ana omurga firmasının bilgisayarında dünyadaki tüm Internet kaynaklarının listesi ve onlara ulaşmak için hangi omurgadan, kime yol açılması gerektiğini gösteren bir liste bulunur. Ana omurga şirketinin bilgisayarı bu listeye göre, müşterinin talebini diğer bir ana omurga firmasına, o firma da bunu hedef Web Server a ev sahipliği yapan (host) bilgisayara iletir. Bu talep, hedef Web Server a talebin konusu ve talep edenin adresi ile birlikte bildirilir. Sizin müşteri olarak o sırada sadece kendi Internet hizmet sunucunuzla bağlantınız sürmektedir, yoksa sizin bilgisayarla hedef Web Server arasında doğrudan, birebir bir ilişki yoktur. Hedef Web Server, müşteri olarak sizin kim olduğunuzu ve size nasıl ulaşabileceğini, ancak kendisine gelen talebin altındaki adresten bilmektedir. Web Server sizin o anda kendi Internet Hizmet Sunucunuzla arasındaki bağlantının devam edip etmediği ile ilgilenmez. Onun için önemli olan kendisine iletilen talebin karşılığını, talebin altındaki adrese iletmekten ibarettir. Aynı yol bu kez tersine kat edilir; arzu ettiğiniz bilgi sizin ekranınıza ulaşır. Kısaca ne talep sahibi müşteri bilgisayar, ne talebi karşılayan Server bilgisayar, bir diğerinin o anda nerede ve ne durumda olduğu ile ilgilenmez. Bu “durumdan haberdar olmama” hali özellikle Internet’ te ticaret bahsinde çok önem taşır (1).

## **1.2. WEB SERVER YAZILIMLARI**

HTTP ve FTP, müşteri bilgisayarla, servis sunan bilgisayarın üzerinde anlaştıkları bir dille (HTML) birbirine ilettikleri talep ve talebin karşılandığı olan malzemenin alınıp verilmesinde TCP/IP denilen kurallardan yararlanılarak yapılan iletişimi düzenleyen ilkelerdir. Bu ilkelere uygun olarak çıkartılan bir talep Web hizmetini sunan bilgisayar tarafından karşılanır ve karşılık olarak belirli bir bilgi kümesi müşteri bilgisayara iletilir. Web Server olarak tayin edilmiş bilgisayarda, kendisine gelecek HTTP ve FTP taleplerini anlaması ve bu talepleri yerine getirmesine yarayan programlar (örneğin Apache Web Server, MS Internet Information Server veya Netscape Web Server) sürekli çalışır vaziyette olur. Bu programların, bilgi- alıp vermenin yanı sıra, elektronik posta alıp verme ve yönlendirme, veri tabanlarına erişme ve içinden seçme yapma (Querry, SQL, vb. gibi), kendi sabit diskinde duran bir dosyayı alıp karşı tarafa aktarma (FTP, Gopher, WAIS) veya karşı tarafın vereceği dosyayı alıp kendi sabit diskine kaydetme yeteneği olur.

İlk Web Server programı, HTML dilinin geliştirilmesindeki öncü konumu sebebi ile İsviçre’ deki CERN kurumu tarafından geliştirildi, ama kısa zamanda UNIX platformunda, anonim bir tarzda ve ücret ödemeden kullanılabilen bir şekil aldı. NCSA Server, National Center for Supercomputing Applications – Super bilgiişlem Uygulamaları Ulusal Merkezi adlı, şimdi kapanmış olan kurum tarafından UNIX işletim sistemi için geliştirilmişti. NCSA Server in geliştirilmiş olduğu Apache Server ise uzun süre ücretsiz dağıtıldıktan sonra günümüzde ticari olarak geliştiriliyor ve satılıyor. Bugün hala NCSA Server veya Apache’ nin ücretsiz sürümlerini dayalı Web alanları bulunmakla birlikte, Sun Solaris, IBM AIX ve diğer Unix sistemleri için geliştirilmiş çok sayıda Web Server hizmete girmiş durumda. Kişisel bilgisayarların Unix gerektiren bilgisayarlara oranla daha ucuz olması, Microsoft’ un NT, IBM şirketinin OS/2 işletim sistemlerinin Unix ile ciddi bir rakip haline gelmiş bulunmaları sebebiyle, bu sistemlere dayalı Web Server programları da hızla artıyor.

NT Workstation ve Windows 95/98, aslında kişisel Web Server adı verilen, Internet’ e 24 saat bağlı olmadan, başka bir firmanın ev sahipliği yaptığı Web alanlarına hizmet sağlayabilir. Hatta NT Workstation, aynı anda 10 u geçmemek üzere, 24 saat süre ile Internet’ e bağlanabilecek ve müşteri taleplerini karşılayabilecek yetenektedir. IBM şirketinin OS/2 işletim sistemi ise, Internet Connection Server adlı paket kurulduğu zaman, bir PC’ nin fiziksel olarak kaldırılabileceği kadar Internet bağlantısına cevap vermesini sağlamaktadır. Macintosh bilgisayarları için. Star Nine firmasının MacHTTPd programı ile, ücretsiz edinilebilecek http4Mac ve EasyServe adlı programlarla, Internet servisi sağlamak mümkün.

Ayrıca, bugün PC’ lerde de UNIX işletim sistemi kurmak hem kolay, hem ucuz hale gelmiş bulunuyor. Solaris, BSDI, Esix, SCO UNIX bu alandaki ticari programlar. Bunun yanında Linux ve FreeBSD adlı, ücretsiz dağıtılan UNIX işletim sistemleri de, ticari olanları aratmayacak niteliklere sahip. Bu tür ücretsiz programlar, Apache Web Server’ in ücretsiz sürümünü de içeriyorlar.

Yalnız PC’ lerin, Internet’ in gerektirdiği en önemli özellik olan aynı anda bir çok iş yapabilme becerisinin, işletim sistemi kadar, donanım kaynaklarının genişliğine bağlı olduğunu unutmamalıdır.

Bir Web Server yazılım paketi seçerken dikkat edilmesi gerekenler; Yazılım paketi yeterli güvenliği sağlayacak özelliklere sahip olmalıdır. Binalarda bir odadaki yangını yandaki odaya sıçramasını önleyen ateşe dayanıklı duvarlardan (friwall) esinlenerek adlandırılan bir dizi program, Web Server yazılımının bulunduğu bilgisayarın, kötü niyetli kişiler tarafından bozulmasını engel oluyor. Ancak Web Server’ in kendi içinde mevcut güvenlik önlemlerinin neler olduğunu dikkatle araştırmak gerekir. UNIX işletim sistemi ve ona bağlı çalışan Web Server programlarının daha güvenli olduğuna ilişkin, kimi zaman Web tasarımcısını ve Internet hizmet sunucusunu rahatlatan, yaygın bir söylenti vardır bu doğru değil. Kötü niyetli bir kişi Windows NT sistemine verebileceği zararı, aynı rahatlıkta UNIX sistemine verebilir. Bir diğer yaygın ve aynı ölçüde yanlış inanç ise NT sisteminin güvenli olmadığıdır. Microsoft firmasının NT sisteminin 4. Sürümünü güncelleştirmek için dağıttığı SP3 adlı tamir programının yerleştirilmesinden sonra, NT sistemleri güvenlik açısından herhangi bir başka işletim sistemi ile boy ölçüşebilir hale geldi (5.0 sürümüyle de daha da gelişti). Burada önemli olan, Internet’ e açılmanın, iyi niyetli - kötü niyetli herkese açılmak olduğunu unutmamaktır. Özellikle form denilen, HTML dilinin ziyaretçi bilgisayarın ev sahibi bilgisayara talepten başka şeyler göndermesine imkan veren etiketlerini ve ona bağlı CGI (Common Gateway Interface - Ortak Geçit Arabirimi ) adı verilen ziyaretçinin ev sahibi bilgisayarın programları harekete geçirebildiği buluşma noktasında yer alabilecek programları tasarlarken, daima kötü niyetli kişileri dikkate alarak hareket etmek gerekir.

Web hizmeti sunan kişi sadece başkalarının kendi bilgisayar sisteminde arzu edilmeyen şeyler yapmalarını önlemekle değil, aynı zamanda kendisine tevdi edilen başkalarına ait bilgileri de saklamak ve başkalarından korumakla yükümlüdür. Bu bilgiler, ziyaretçinin adı, elektronik adresi, hatta kredi kartı numarası olabilir.

Web hizmeti sunan kişi olarak, kimin hangi sayfadan sizin sayfanıza atladığını bilmek, kendi sayfanızın reklamını bu sayfalarda daha çok yapmanıza imkan verir. Özellikle elektronik ticarete dayalı veya mesajınızı daha çok kişiye iletmek amacıyla hazırlanan Web alanlarını işletenlerin, sayfalarının varlığını duyurmak için, mümkün olan her yoldan yararlanmaları gerekir. Web Server, size bu kolaylıkları sağlamalıdır. Web Server, kimin hangi tür bilgileri edinmek istediğine ilişkin rapor tutmalıdır. Bu raporu incelemekle, Web alanınızda hiç talep edilmeyen bilgilerden çok talep edilen anlarda daha çok bilgi sunabiliriz.

Web Server programı ile ilgili teknik destek ve problem çözme hizmeti alıp almamak, programın seçiminde belki de en önemli unsur sayıla bilir. Özellikle başlıca işi bilgisayar mühendisliği olmayan bir hizmet sunucu, yazılım donanımla uyum sağlamada karşılaşabileceği güçlükleri ancak yazılımı piyasaya süren firmanın teknik servisinden veya o yazılımla ilgili uzmanlığı olan danışmanlardan sağlayabilir. Piyasada hiç tanınmayan veya Internet’ ten ücretsiz olarak edinilen - dolayısıyla belli bir firmanın malı olmayan – server programları, çoğu zaman gerekli teknik destekten de mahrumdur. Buna karşılık büyük yazılım firmalarının programları, firmanın kendi mühendis ve uzman kadrosu ve buna ek olarak bu programları destek sağlayarak hayatını kazanan kişiler tarafından en ince ayrıntılarına kadar bilinmektir. Bir gece yarısı çöken Server bilgisayarın yeniden çalıştırmamanın bedeli, o programın ilk maliyetinden çok daha yüksek olabilir (1).

## **1.3. WEB TARAYICI (BROWSER) **

Web standart olarak bilgi hizmetlerinin görüntülenmesi ve hazırlanması için birçok değişik platform (Unix, Windows, MacOs,...) üzerinde çalışan programlara izin verir. Bu programlara Web Tarayıcılar (Browser) denir. HTML kodları World Wide Web (Dünya Çapında Kütüphane) için hazırlanmış Web tarayıcılarında görüntülenir. Her bir HTML dokümanı tarayıcılar tarafından görüntülenebilse de tarayıcılardan kaynaklanan çeşitli eksiklik ve özelliklerden ötürü hazırlanan dokümanlar her tarayıcıda aynı görüntülenmez.

Neden değişik tarayıcıların değişik sürümlerine ihtiyacımız var? Bu sorunun cevabı, HTML dilinin Internet’ ın ortak dili olduğu gerçeğine bir ölçüde gölge düşürecektir. Çünkü ortak bir HTML dili bulunmasına rağmen, tarayıcıların ve aynı tarayıcının farklı sürümlerinin HTML kodlarını yorumlayışı farklıdır. HTML, Uluslararası Web Konsorsiyumu adlı kuruluşun çıkarttığı standart sayılan ve 4.01 Sürümüne ulaşmış bir dil konumundadır. Böyle bir standartlaşmaya rağmen, Netscape ve Microsoft firmaları, bilgisayar kullanıcılarını rağbet ettiği tek tarayıcı programını kendi programları olmasını sağlamak üzere giriştikleri rekabet çerçevesinde, programlarını sadece HTML dilini aynı şekilde yorumlayan ve dolayısıyla birbirinden farksız sonuçlar veren programlar olmaktan çıkartmak istediler. Bunun sonucu ise Web tasarımcısının, bazen Netscape’ in anladığı ama IE’ nın anlamadığı, kimi zaman IE’ in becere bildiği, buna karşılık Netscape’ in henüz programına koyamadığı HTML özelliklerinden hangisini kullanacağına karar veremez duruma düşmesi oldu.

HTML dilini kullanarak, ticari amaçlı Web tasarımı yapan kişi, Internet ile bağlantılı bilgisayar kullanıcılarının (Internet kullanıcıların) hepsinin ekranda aynı şekilde gösterilecek sayfalar yapmaya mecburdur. Buna karşılık bir firmanın intranet ortamı için Web tasarımı yapan kişinin, HTML kodlarından sadece kendi firmasının standart olarak benimsediği tarayıcının anlayabileceği özelliklerinden yaralanması mümkündür.

Günümüzde bir çok web tarayıcı programı olmasına rağmen, en çok öne çıkanları Internet Explorer (IE) ve Netscape Navigator (NN)’dır (1).

**1.3.1. En Çok Kullanılan Web Tarayıcıları**

**1.3.1.1. Microsoft Internet Explorer**

Tarayıcı piyasasına diğer tarayıcılardan sonra girmesine rağmen, Microsoft şirketinin Web tarayıcı olan Internet Explorer, piyasa payındaki artış hızı, HTML dilinin tanıdığı özellikleri ve HTML sayfalarına ilave ettiği diğer görsel kabiliyetler bakımından, diğer programları geride bırakmış bulunuyor. IE artık sadece bilgisayar kullanıcısının Internet ile bağlantı kurmasını ve Internet’ ten alacağı HTML sayfalarını ekranda canlandırılmasını sağlamakla kalmıyor, aynı zamanda bilgisayarın disklerinin taranması ve dosya yönetimi gibi işlemleri de yapıyor. Windows işletim sistemiyle beraber de yüklenebilen IE’ nin, daha geriden gelmekle birlikte, Macintosh uyumlu sürümü de bulunmaktadır (1).

**1.3.1.2. Netscape Navigator**

Netscape Communications Corporation şirketinin (NCC) piyasaya sürüldüğü NN, IE’ ın hızlı yükselişine rağmen, kurulduğu bilgisayar sayısı bakımından piyasanın en uygun tarayıcısıdır. NN, sadece Windows ve Macintosh ortamında değil, fakat aynı zaman da UNIX işletim sisteminde de işleye bilmekte ve ayrıca LINUX işletim sistemiyle beraber de bilgisayara kendiliğinden kurulabilmektedir. NCC, yakın zamana kadar, hem tarayıcı hem de Web Server programları alanında Internet’ te öncü konumda idi. Internet’ in bugün sahibi olduğu bir çok özellik, HTTP ve FTP ilklerinin çoğu, bu firmanın tasarımı sonucudur (1).

**1.3.1.3. Diğerleri**

Web tarayıcı piyasanın NCC ve MS firmalarının egemenliklerine almış olmaları sebebi ile, piyasada başka tarayıcı bulunmadığını düşünülse de piyasada, çoğu ücretsiz veya sınayıp da beğenenlerin yazarına az bir ücret ödedikleri paylaşım yazılımı türünden 50’ den fazla tarayıcı programı bulunmaktadır. Bu programların en yaygını, tarayıcı programın ilk mucidi NCSA şirketine ait Mosaic programıdır. Spyglass firmasının Mosaic yazılımını esas alan programı, hala yaygın olarak kullanılmaktadır.

Bir Web tasarımcısının mutlaka aşina olması gereken bir tarayıcı, HTTP, FTP ve HTML gibi Web’ in protokol ve dillerini belirleyen, Evrensel Kaynak Belirleyici (URL) sistemini işleten, yani tüm dünyadaki Web adreslerini sağlayan ve bu listeyi üstlenici firmalar aracılığıyla her gün tüm dünyadaki Internet omurga işletimcilerine ulaştıran uluslar arası kurum olan W3C kurumunun kendi tarayıcı programı olan Amaya yazılımıdır. Bu program, sadece Internet tarayıcı değil, aynı anda HTML sayfaları tasarlamakta ve oluşturmakta da kullanabileceğiniz bir HTML editörüdür. Birden fazla HTML sayfasını açabilen, Internet’ e bağlı iken bir yandan da sayfa tasarımı yapmanıza imkan veren Amaya, HTML dilini olduğu gibi anlayıp, ekranda gösteren tek tarayıcı programıdır. NN ve IE, HTML kodlarına kendi yorumlarını katarken, Amaya, sayfalarınızdaki çalışmalarda gerçek HTML değerlerini ekrana getirecektir. Bu program ücretsiz olarak http://www.w3C.org adresinden indirilebilir (1).

**1.3.2. Yardımcı Programlar ve Ek Birimler**

Internet tarayıcıları, sadece HTML kodları ile yazılmış metinleri okuyup anladıkları günleri çoktan geride bıraktılar. NN ve IE, artık birçok grafik dosyasını okuyup, ekranda resmedebiliyorlar. Bu gelişmeye rağmen, Internet tarayıcının başlıca işi, her gün yeni bir türü ortaya çıkan ses, video ve diğer çoklu ortam dosyalarının, veritabanı veya muhasebe tablolarının hızlı gelişimine ayak uydurup, onları ekranda canlandırmak olmadığı için, tarayıcı programını yazan uzmanlar, bu gibi programların dışardan çalıştırılmasına imkan sağlıyor. Kullanıcı isterse tarayıcısına, Internet’ te adının uzatması, örneğin “.xls” olan bir dosya ile karşılaşınca, bunu ekranda göstermek için Microsoft Excel programını çalıştırmasını bildirebilir. Bu durumda MS Excel, Netscape veya IE’ nin ‘yardımcı programı’ haline gelmiş olur.

Plug - in denilen ek birimler ise tarayıcıya tamamen farklı bir programı açmak yerine, belirli bir tür dosya türünü ekranda canlandırabilme yeteneği kazandıran eklerdir. Tarayıcı program bilgisayara kurulurken bu ek birimler olmaksızın (ya da sadece en yaygın olanları ile) yüklenir. Internet’ te yeni bir dosya türü oluşturmak isteyen, ya da mevcut türlerin Internet servisi sunan bilgisayarlarda (server) müşteri bilgisayara aktarılmasında yeni bir yöntem geliştirenler, bu yeni dosya türünün tarayıcı tarafından bilgisayarda oluşturulabilmesi için bir de “plug - in” oluşturur ve bunu genellikle ücretsiz dağıtır.

Diyelim ki, bir firma, Internet’ te ses naklini çok daha hızlı ve kolay hale getirdiğini düşündüğü yeni bir yöntem geliştirdi. Bu yöntemin Internet hizmeti verenler tarafından benimsenmesi ve yaygın olarak kullanılması tarayıcı programların bu biçimi tanımasını, bu da firmanın yani ses nakil yönteminin gerektirdiği plug - in programcıklarının etkin şekilde dağıtmasına bağlıdır. Kimi zaman bir yöntem o kadar beğenilir ve Internet hizmeti verenler tarafından tutulur ki, plug - in, tarayıcı kullananların satın almak isteyecekleri bir program haline gelir. Çoğu zaman, tarayıcı için gerekli plug - in kullanıcılara ücretsiz ulaştırılırken, yeni yöntemi kullanarak Internet alanında sundukları içeriği daha etkin hale getirmek için gerekli oluşturma programı para ile satılır. Bunun bir örneği Internet’ te gerçek zamanlı ses aktarmakta kullanılan RealAudio ses kayıt ve saklama yöntemidir. Firma, ses dosyalarını bu yöntemle sıkıştırıp hızlı şekilde ulaştırmak isteyenlere kodlama ve bunu Servere yerleştirerek, isteyen tarayıcıya aktaracak programı satarken kendi kullanıcılarına RealAudio dosyalarını okuyarak, bilgisayarın ses kartını ve hoparlörünü kullanarak bu dosyayı sese çevirecek ek birimi ücretsiz dağıtmaktadır.

Web tasarımcısı, özellikle ses, video ve diğer grafik unsurları Server’ dan müşteriye aktarılmasında ne gibi yöntemler olduğunu ve gelişmeleri izlemek zorundadır. HTML sayfanıza bir ses unsuru koymaya karar verdiğiniz zaman NN veya IE kullanan bir kişinin bunu bilgisayarında dinleyip dinleyemeyeceğini de hesaba katmak zorundasınız (1).

## **BÖLÜM 2**

## **WWW (WORLD WİDE WEB)**

## **2.1. WWW ( WORLD WIDE WEB ) NEDİR?**

World Wide Web (Dünya Çapında Kütüphane), protokollere dayanan, standart yollarla Internet üzerinden çok sayıda doküman ve bilgilere ulaşmak için kullanılan Internet hizmetidir.

**2.1.1. WEB Sayfası**

World Wide Web her biri tek bir anda browser tarafından hizmete sunulan milyonlarca Web Sayfasından oluşmuştur. Bir Web sayfası genellikle, tekstler, grafikler, sesler ve hypertext linklerden oluşan tek bir HTML dokümanıdır.

**WEB Sitesi**

Bir Web Sitesi, belirli kişi ya da belirli bir grubun kontrolü altında birden fazla Web sayfasının bir araya getirilmesiyle oluşturulur. Genellikle bir Web sitesi iç içe bilgilerle kuşatılmıştır. Sitenin giriş sayfası bir indeks niteliğindedir. Bu indeks sayfasındaki hypertext linkler kullanılarak diğer sayfalara (sitenin diğer kısımlarına) ya da diğer sitelere geçiş mümkündür (2).

## **2.2. WEB DE NASIL YER ALINIR**

Web de yer almak için iki seçenek vardır. Bunlardan birincisi; başka birine (muhtemelen bir IS Sağlayıcısına ait) Web sunucusundan belirli bir sabit disk alanı kiralamaktır. Türkiye’ deki servis sağlayıcılar bu tür hizmetler veriyorlar. Hatta bazı IS Sağlayıcıları Internet hesabı açtırdığınızda size küçük de olsa ücretsiz bir Web sayfası alanı sağlıyorlar. Ama hazırlayacağınız Web sayfalarını ticari amaçlarla kullanacaksanız, örneğin firmanızın ürünlerini Web sayfalarınızda tanıtmak ve pazarlamak istiyorsanız belirli bir ücret ödemek zorundasınız.

İkinci seçenek, genelde firmalara yöneliktir. Yani, Türk Telekom’ a başvurup bir kiralık hat (leased line) aracılığı ile Web sayfalarınızı kendi Web sunucunuz üzerinden yayınlamak veya Web sunucunuzu bir IS Sağlayıcıya yerleştirip buradan yayın yapmak. Kuşkusuz bu seçenekler içinde bir IS Sağlayıcının sunucusundan - kiraladığınız yerin MB cinsinden büyüklüğüne göre ücret ödeyerek - yer kiralamak en ucuzu. Bunun karşılığında Web sayfalarınıza karşılık gelecek bir Web adresi (URL) ediniyorsunuz. Bu adres IS Sağlayıcınızın ismi ile başlayıp kendi sitenizin ismi ile devam edebileceği gibi (örneğin:** **http://www.iss.com.tr/benimsitem), IS Sağlayıcınızla yaptığınız anlaşmaya göre tamamen kendi verdiğiniz isim de olabilir (örneğin:** **http://www.benimsitem.com.tr).

Yurtdışında hesabı olsun olmasın herkese Web sayfalarını yayınlamak için ücretsiz belirli bir alan açan IS Sağlayıcıları da var. Örneğin Geocities (http://www.geocities.com/homestead/) herkese 3MB’ lık bir Web sayfası alanı açıyor veya Tripod (http://www.tripod.com/homestead/) herkese 2MB’ lık bir Web sayfası alanı açıyor. Internet’ te sörf yaparken kuşkusuz bu tür başka promosyonlarla da karşılaşılabilir. Hazırladığınız sayfaları bir FTP client programı ile (örneğin: ws\_ftp) bu sitelere ‘upload’ edebiliyorsunuz. Yine de bu hizmetin sürekliliği konusunda emin olunamaz (2).

## **2.3. PROFESYONEL WEB TASARIMI**

Web, ticaretin, yayıncılığın ve haberleşmenin en pratik yoludur. Bu sebeple başarılı, düzenli ve şematik bir web sitesi veya sayfası dizayn edebilmek önemli bir konu haline geldi.

Bütün bu düzenli şematik görüntülerin altında yatan neden, insan beyninin algılama ve hatırlama kapasitesidir. Psikologlara göre çoğu insanlar, kısa bir zaman diliminde 4 - 7 farklı yoğunlukta bilgileri hatırlayabiliyorlar fakat zaman uzadıkça konuya hakimiyetleri de azalıyor. Şematik görüntülerin hedefleri ise ana başlıklar altında kısa, öz, anlaşılabilir ve tasarım destekli bilgiler vererek insanların belleklerinde belli bir süre de olsa yer edinebilmektir.

Bir çok web sitesi, insanların araştırabileceği küçük bölümlerde referans bilgiler içerirler. Kullanıcılar (okuyucular) uzun ve bitişik belgeleri nadiren bilgisayar ekranından okurlar. Çoğu insanlar özellikle aradığı belgeleri kısa, anlaşılır, referans bilgilerin bulunduğu sayfalardan aramayı ve aradıklarını bulduktan sonra uzun içerikli bilgileri yazıcıda bastırmayı tercih ederler. Küçük bölümler halinde anlatılmış belgeler, anlaşılabilir organizasyon şeması oluşturmak açısından önemlidir ve ayrıca web sitenizde hypertext bağlantılar kurmaya yardımcı olurlar.

Kısa, şekilsel - organize belgeler bölümleri kullanıcıları sayfaya daha fazla çeker. Çünkü:

Çok az web kullanıcıları, ekranda uzun belgeleri okuyarak zaman kaybederler. Çoğu kullanıcılar uzun belgeleri sabit disklerine kaydederler veya kağıttan okumak amacıyla yazıcıya bastırırlar.

Belgeleri bölümlere ayırmak, onları web bağlantıları ile birbirine bağlamak açısından yaralıdır. Belli konularda ilgili bilgiler elde etmek isteyen kullanıcılar için, bağlantılar, belgelerin ayıklanması ve aradıklarını kolay bulma açısından önemlidir. Fakat belgeler gereğinden fazla bölümlere ayrılmamalıdır. Aksi halde okuyucuların beklentileri boşa çıkartılır. Bölümlerin web üzerinde 1 - 3 sayfa kadar olmaları mantıklıdır. Sadece küçük bir paragraf içeren bağlantılar çoğu koşullarda çirkin görünecektir.

Bilgilerin sunumunda ve organize edilmesinde hazırlanan belirli bir format, şekilsel açıdan önemli olmasının yanı sıra kullanıcıların sitenizdeki geçmiş deneyimini, gelecekteki aramalar ve araştırmalarına uygulamalarında yardımcı olur.

Eğer okuyucu için temel tarama yapısına uygun bir site isteniyorsanız, belgeler;

Uygun bölümlere ayrılmalı,

Önem ve genelliğe bağlı olarak bir hiyerarşi içinde olmalı,

Hiyerarşi bölümler arasındaki ilişkiyi yapılandırmada kullanılmalı,

Sistemin işlevsel ve estetik başarısını analiz etmelidir.

**Şekil-2.1.WEB sitesi sayfa yerleşim taslağı (2).**

Sayfanızda ilk olarak öncelikli bilgileri sunarsanız, en önemliden veya en genel başlıklardan daha ilgili veya daha ayrıntılı bilgilere doğru bir hiyerarşik düzen kurabilirsiniz. Web’ de hiyerarşik organizasyonlar gereklidir. Çünkü çoğu ana sayfa ve bağlantı şemaları hiyerarşik bir düzene sahiptirler. Aşağıdaki sayfada da görüldüğü gibi ana sayfayı alt sayfalar ve içeriksel sayfalar izler (2).

**Şekil-2.2. Ana sayfanın içeriğinin hiyerarşik düzeni (2).**

**2.3.1. Sayfalar Arası İlişkiler******

Mantıklı bir site organizasyonu, kullanıcıların aradıklarını nerede bulabilecekleri hakkında doğru yönlendirmeler yapar. Eğer ilişkiler mantıklı yapılar halinde kurulmazsanız sayfa okuyucunu aklını karıştırmaktan başka işe yaramaz (2).

**Şekil-2.3. Düzensiz bir site örneği (2).**

Yapıyı oluşturduktan sonra istatistikleri ve organizasyon şemasının pratikliği ve ne kadar hızlı ve verimli çalıştığı analiz edilmelidir. Geçerli www site tasarımı geniş olarak yapının dengelenmesi ve menü ilişkileri veya ana sayfa ve ara sayfalar, diğer bağlantılı sayfalar, grafikler ve belgelerin sonucudur. Amaç kullanıcıya doğal gelen menü ve sayfa hiyerarşisi oluşturabilmektir. Birkaç örnek verirsek:

**1- Çok geniş:** Esas menü, birbirleriyle ilgisiz çok yayılmış,tekdüze bir yapı gösteriyor.

**Şekil-2.4. Geniş alana yayılmış site örneği (2).**

**2- Çok derin:** Menü sayfaları gereksizce derinlere doğru uzanıyor, fakat içerik oldukça az. Yani başı ve sonu gelen sayfalar var. Sayfalar hem çok ince hem de çok uzun görünüyor.

**Şekil-2.5. Çok derin alana yayılmış site örneği (2).**

**3- İyi dengelenmiş:******

**Şekil-2.6. Dengeli yapıda bir site örneği (2).******

İyi dengelenmiş hiyerarşik bir ağaç yapısı oluşturmada amaç, okuyucunun sayfa yapısını kolay idrak edebilmesini ve sayfalar arasında kaybolmamasını sağlamaktır. Eğer menülerimiz 4 - 5 bağlantıdan az bağlantı içeriyorsa değerlerini kaybederler.

Web sayfalarının düzenli ve tutarlı bir sistemle hazırlanmasındaki amaç, hedef kitlenin kısa sürede sayfa düzenine adapte olarak aradıkları bilgiye kolayca erişmelerini sağlamaktır.

Web sayfasına iyi bir örnek Şekil - 2.7.’ de verilmiştir. Bu örnekte; sayfanın alt ve üst kısmında görüntü haritaları kullanılmıştır.

Sayfanın hangi siteye ait olduğu, belgelerin içeriği, konu başlıkları gibi temel bilgiler burada sabit bir düzen içinde verilerek aynı zamanda "ileri" "geri" düğmeleri eklenerek bir önceki ve bir sonraki sayfaya geçiş kolaylığı sağlanmıştır.

Sayfanın sol yanında ayrılan bölüm ana sayfaya ve konunun alt başlıklarına bağlantı için kullanılmıştır. Okuyuculara sunulan bilgi bu sınırlandırma içinde, düzgün ve orantılı başlıklar altında metin ve grafik olarak gösterilmiştir. Belgelerin bütün sayfaları bu standart formata uygun halde hazırlanmıştır. Böylece, kullanıcılar ilk sayfayı inceledikten sonra diğer sayfalarda aradıkları bilgilerin nerede olduğunu tahmin edebileceklerdir (2).

**Şekil-2.7. WEB sayfasına iyi bir örnek (2).**

**2.3.2. Bir Sayfa Hazırlanırken Dikkat Edilecekler******

**2.3.2.1. Sayfada Grafik Kullanılırken Dikkat Edilecekler**

Grafiklerin güvenli bir şekilde görüldüğü alan, iki ayrıntıya göre belirlenir:

1. Günümüzde kullanılan en düşük ekran çözünürlüğü.
2. Web sayfalarının yazdırılacağı kağıdın boyutu.

**2.3.2.2. Ekran Boyutu******

Akademik olarak ve iş ortamında en çok kullanılan ekranlar 14 - 16 inch’ lik olanlardır ve bu nispeten küçük olan ekranlar 640X480 nokta ekran çözünürlüğüne sahiptir. Bu ölçüleri aşan web grafiklerini görebilmek için kullanıcılar ekrandaki görüntüyü aşağı ve yana kaydırmak zorunda kalacaklardır.

**2.3.2.3. Sayfanın Yazdırılabilirliliği**

En küçük ekranlarda bile görülebilen grafikler bazen yazdırılma sırasında standard A-4 sayfasını aşmaktadırlar. Özellikle uzun metinler halinde hazırlanan web sayfalarının yazdırılabilirliliğine çok dikkat edilmelidir. Birçok okuyucu ekrandan okumak yerine bu sayfaları yazdırmayı tercih eder ve sayfalar fazla geniş hazırlanmış ise artan kelimeler yazdırılamayacaktır.

Aşağıda verilen değerler, 640X480 nokta ekran çözünürlüğü baz alınarak hesaplanmış, Internet Explorer ve Netscape Navigator gibi sık kullanılan tarayıcılar ve MacOS ve Windows95 işletim sistemlerinde problemsiz olarak görülüp yazdırılabilecek sayfa boyutlarıdır.

Yazdırılabilirlik ===> Maksimum genişlik : 535 piksel
Maksimum yükseklik : 295 piksel

Ekranda Görüntü ===> Maksimum genişlik : 595 piksel
Maksimum yükseklik : 295 piksel

Planlı bir grafik tasarımın amaçlarından birisi de kullanıcıların gözünde, siteye ait her sayfaya bir özellik kazandırmaktır. Siteye ait olan her sayfada bir imza niteliği taşıyan bantlar kullanıcılara farklı başlıklar sunarak istedikleri diğer bağlantı sayfalarına geçiş imkanı verir.

Uzun dokümanlar halinde hazırlanan web sayfalarında konu başlıkları her sayfada verilerek okuyucuya kolaylık sağlanmalıdır. Böylece okuyucular, istedikleri zaman konunun herhangi bir alt başlığına doğrudan geçiş yapabileceklerdir. Ayrıca genel hatlarıyla dokümanın neleri içerdiğini her an görebilecek ve bir kopukluk yaşamadan istedikleri bilgileri alabileceklerdir.

Sayfa sonlarında yine sayfanın hangi siteye ait olduğunu ve siteden genel anlamda ulaşıla bilinecek sayfaları gösteren bir bant bulundurulabilir. Genelde kullanıcılar sayfa sonuna geldiklerinde, sayfanın en başında sunulan bilgileri ve bağlantıları göremezler, dolayısıyla sayfa sonundaki menü kullanıcılar için bir avantaj sağlayacaktır (2).

**2.3.2.4. Doküman Uzunluğu ve Ekran **

Araştırmalara göre uzun dokümanlarda, tarayıcı ekranını aşağıya doğru kaydırmak zorunda kalmak problem yaratmaktadır. Kullanıcılar sayfada aşağı doğru indiklerinde sayfanın üst kısmında verilmiş olan ana başlıkları, diğer sayfalara olan bağlantıları ve konu başlıklarını kaybetmektedir.

Uzun web sayfalarında gezinebilmek için kullanıcı ekranın sağında bulunan kaydırma çubuğunu kullanmak zorunda kalmaktadır. Machintosh ve Windows 3.1 gibi birçok grafik ara yüzünde kaydırma çubuğunun boyutu sabittir ve belgelerin uzunluğu hakkında fazla bilgi vermez. Çok uzun web sayfalarında kaydırma çubuğunun küçük bir hareketi ekranın tüm görünümünü değiştirebilir (2).

** Şekil-2.8. Uzun bir WEB sayfası örneği ve Uzun belgelerdeki kaydıma çubukları (2).**

Ancak uzun web sayfalarının bazı avantajları da vardır. Sayfa tasarımcıları için hazırlaması, kullanıcılar içinde yüklemesi kolaydır. Uzun belgelerde site tasarımcıları bağlantı sayfalarını organize etmek zorunda kalmazlar. Böylece kullanıcılarda her defasında ayrı ayrı dosyaları yüklemek yerine bir kerede uzun belgeleri yüklerler.
Web sayfaları çok uzun olduğunda kullanıcılar bu sayfaları okumak yerine yazdırırlar.

**2.3.2.5. Browser Yazılımlarına Dikkat**

Dünya çapında en çok kullanılan browser yazılımları Microsoft Internet Explorer ve Netscape Communicator yazılımlarıdır. Sitenizi oluştururken mutlaka ve mutlaka her ikisinde de test edin. Mümkünse bu testi sabit diskinizde değil siteniz server bilgisayarına yüklendikten sonra ağ üzerinden yapın. Böylece sayfanın yükleniş hızı hakkında da** **bir fikir elde edersiniz. Yazılımların birbirinden ters düştüğü hususların başında tablolar geliyor. Tabloları oluştururken genişlik elemanlarını % ile değil de piksel olarak verilirse daha sağlam bir sayfa ortaya çıkar. Böylece farklı ekran çözünürlülüklerinde çalışan kullanıcıların sayfayı aynı şekilde görmeleri sağlanmış olur (3).

**2.3.2.6. Sütunlar**

Bir gazete veya dergi satın aldığınızda yazıların belirli sütunlar halinde yerleştirildiğini görürsünüz. Asla ve asla yazılar dümdüz bir sıra halinde yazılmaz. Bunun amacı yazıların daha kolay okunabilir hale getirmek. insan gözü ancak *5 *veya 6 kelimelik sütunları problemsiz olarak takip edebilir. Daha uzun yazları okurken, özellikle bir alt satıra geçerken yazının hakimiyeti kaybedilebilir ve zamanla göz yorulur. Bunun için sayfalarınıza metinler yerleştirirken mümkün olduğunca daha ince sütunlar kullanmaya çalışın. Böylece daha hoş görünümlü bir sayfa elde edersiniz. Aynı zamanda ziyarete gelenler sayfaları daha rahat okuyabilirler (3).

**2.3.2.7. Paragraflar**

Uzun yazıları paragraflara ayırmak, onları çekici hale getirmenin bir yolu. Paragrafsız uzun yazılar, hem görünüm açısından kötü olur hem de okuyucu yazıyı takip etmekte zorlanır. Paragraflar ayrıca değişik konuları birbirinden ayırmak içinde iyi bir yöntemdir (3).

**2.3.2.8. Klişe Görüntüler**

Web üzerindeki binlerce URL artık birbirinin kopyası haline geldi. Aynı zemin desenleri, butonlar, javascriptler vs. her sayfanın birbirine benzemesine sebep oluyor. Öncelikle kendinize özgü* *bir şeyler yapmalısınız. Eğer bir sayfada butonların yerleşimini beğendiyseniz ve bunu kullanmak istiyorsanız en azından butonlar oldukça farklı bir şekilde kendiniz dizayn etmeye çalışın (3).

**2.3.2.9. Çalışma Ortamı**

Bilgisayarınızla çalışırken hangi editörü kullanıyor olursanız olun birkaç yardımcı programa ihtiyaç duyacaksınız. Bu programların kısa yollarını kolay ulaşabileceğiniz yerlerde bulunsun (3).

Ana sayfa scrollbar’ ı bu kadar küçültecek derecede uzun olmamalı

Font rengi sayfa ile uyuşmuyor. Başlık resim olmadığı için antialias problemi var

Zemin deseni kötü seçilmiş Bu sebepten yazılar kolay okunamıyor. Sayfanın ortasına konulan uyarı ise bir çok ziyaretçinin canını sıkacaktır.

Lüzumsuz bir gif animasyonu

640x480 ayarında monitör kullananlar logoyu ortadan kesik görüyorlar

** Şekil-2.9. Kötü hazırlanmış WEB sayfası örneği (2).**

## **BÖLÜM 3**

## **GRAFIK TASARIMI**

## **3.1. WEB SAYFASI TASARIMINDA KULLANILAN YÖNTEMLER**

Bir Web sayfası tasarımında görselliğin ön planda olması istenirse grafik kullanmadan bunu yapabilmek bir hayli zordur. Grafik yönü sağlam sayfalar yapmak için bu tip grafik tasarım programlarının bilinmesi gerekmektedir. HTML kodlarını kullanarak da grafikler yapılabilir. Ancak bunun için sayfalar dolusu kod yazılması gerekmektedir ve sonuçta ortaya çıkacak ürün grafik programları ile on dakikada yapılandan görsellik açısından daha basit olacaktır.

Web sayfamızda grafiklerin yanında animasyonlar da yapmak istersek, Flash gibi animasyon programlarını kullanmalıyız. Bunlar için gerekli layer grafiklerini Fireworks ile hazırlayıp diğer programlarda kullanmak hiçte zor değildir.

Web sayfası hazırlamanın bir çok yolu vardır. Bunlardan bir kısmı zor, profesyonel işi, bir kısmı da kolay yani amatör işidir. Ancak günümüzde gelişen programlar sayesinde web sayfası yapmak hem kolay hem daha görseldir. Web sayfaları HTML kodları üzerine kurulmuştur. Yani sayfada yaptığımız her şeyin bir kodu vardır. Tasarımcı sayfayı tasarlarken yapmak istediği işlemler, koymak istediği resimler için gerekli kodları kullanarak sayfayı oluşturabilir. Bu en zahmetli olanıdır. Çünkü kodları tek tek yazmak hem çok uzun sürer hem de kodları bilmek gereklidir.

Bir diğer yol Java, Visual BASIC veya Delphi türü programlama dillerini sayfa tasarımında kullanmaktır. Bunu yapabilmek için de bu tip programlama dillerini bilmek gereklidir. Bu tip tasarımlar ileri düzey tasarımlardır. Bunlar ile bir sayfa tasarlamak yerine daha çok bir portal tasarımı yapılır. Veri tabanı içeren web siteleri (E – Mail servisleri, chat odaları vb.) bu gruba girmektedir.

Tasarımı en kolay ve görselliği en zengin olan grafik tasarımı yardımı ile yapılan web sayfalarıdır. Bu sayfaların tasarımında Flash, Fireworks, Photoshop gibi programlar kullanılarak sayfaların tasarımları yapılabilir. Ancak yaptığımız bu tasarımların HTML kodlarına dönüştürmek için Dreamweaver veya Frontpage gibi programları kullanmak gerekir. Programlar aracılığı ile sayfanın son şekli oluşturularak Internet’ te yer almaya hazır hale getirilir.

Bunlar gibi birçok tasarım yöntemi ile Web Sayfası tasarımı yapılabilir. Bizim tasarımlar için kullandığımız yol grafik tasarımı yoludur. Bunun için Fireworks programı aracılığı ile grafik tasarımı yapılıp, Dreamweaver programı ile sayfaların düzenlemeleri yapıldı. Bu programların yetersiz kaldığı yerlerde Word ve HTML kodları kullanılarak tasarımlar oluşturuldu.

## **3.2. FIREWORKS**

Fireworks Macromedia firmasının geliştirdiği, grafik tasarımında oldukça pratik çözümler sunan, tasarımcının hayal gücü ile sınırlı işler yapılabilecek bir programdır. Çalışma mantığı olarak piyasada grafik tasarım programları içinde en çok adı duyulan Photoshop programı ile aynıdır. Photoshop ile yapılabilecek işlemlerin tümü Fireworks ile de yapılabilir. Grafik tasarımının yanı sıra bu programlar ile resimler üzerinde oynamalar, kesme işlemleri, ekleme işlemleri, boyama, bozuk resimleri düzeltme vb. işlemler yapılabilir. Kullanım açısından piyasada bulunan grafik programları arasında öğrenilmesi ve kullanımı en kolay olan programdır.

**3.2.1. Fireworks Menüleri ve Kullanımı**

** **Program daha önce de söylediğimiz gibi kullanım açısından diğer programlara oranla daha kolay, yapılabilecek işler ise aynı kalitede ve zenginlikte olacaktır. Bunun için önce programın menülerinden başlayarak daha sonra bir örnek verilerek program tanıtılmaya çalışılacaktır. Örnek olarak web sayfalarında kullanılan işlemler gerçekleştirilecektir. Yani bir web sayfasının grafik tasarımı için ne gerekiyorsa adım adım anlatılacaktır.

**3.2.1.1. Programın çalışma ekranı **

** **Programı çalıştırdığımızda karşımıza Şekil 3.1 deki ekran gelir. Şekilde de görüldüğü gibi Fireworks programının çalışma ekranı menüler, kontrol panelleri, ve araç çubuklarından oluşur. ** ******

**Şekil 3.1. Fireworks programının çalışma ekranı (4).**

**3.2.1.2. Menüler**

**File Menüsü :**

**New: **Yeni dosya açar.

**Open: **Kayıtlı bir dosyayı açar.

**Open Multiple: **Animasyon işlemleri için çoklu resimler açar.

**Scan: **Dijital kameradan veya scannerden resim taramak için kullanılır.

**Save: **Yaptığımız işleri kaydetmemizi sağlar.

**Save As: ** Yaptığımız işleri farklı isimler ile kaydeder.

**Save a Copy: **Dosyayı farklı bir isimle kaydettikten sonra yine eski dosya üzerinde çalışmamızı sağlar.

**Import: **Farklı formatta olan bir dosyayı düzenlemek amacı ile png formatına dönüştürür.

**Export: **png formatındaki dosyanın diğer formatlara dönüştürülmesi için kullanılır.

**Export Special: **Export işlemini dosyayı parçalayarak gerçekleştirir. Böylece dosyanın daha hızlı açılmasını sağlar. Ancak Internet üzerinde yapılanları göremeyiz.

**Export Again: **Hızlı olarak bir önceki ayarlara göre export işlemini yapar.

**Export Wizard: **İşlemi gerçekleştirmek için sihirbaz yardımı sağlar.

**Batch Proses: **Birden çok seçimi bir format veya birden çok formatta export işlemi yapar.

**Run Script: **Kendi hazırladığımız özel komutları çalıştırır.

**Preview in Browser: **Hazırladığımız grafiklerin browser da ön izleme yapmamızı sağlar.

**Print: **Yazdırılmasını sağlar.

**Page Setup: **Sayfanın ayarlarının yapılmasını sağlar.

**Document Properties: **Özel işlemler için dosya özelliklerinin oluşturulup saklanmasını sağlar.

**Preferences: **Programın geçerli olan ayarlarının değiştirilmesi ve kendi ayarlarımızın yapılansına olanak sağlar (4).

**Edit Menüsü :**

**Paste Inside: **Alanları belirlenmiş bir bölümün içine obje yapıştırmamızı sağlar.

**Paste Attributes: **Birçok objenin aynı anda seçilerek çok sayıda yapıştırılması işleminde kullanılır. Cut veya Copy işlemleri mutlaka önce kullanılmış olmalıdır.

**Sellect All: **Tüm objelerin seçilmesini sağlar.

**Deselect: **Seçilmiş öğeleri bırakır.

**Superselect: **Grup işlemler yaptığımızda grupların yanında seçimler yapabilmek için kullanılır.

**Subselect: **Bir önceki komut ile aynı özelliktedir. Bu komutta yapılan seçimler efekt eklemek işlemine ön hazırlık olarak kabul edilir.

**Select Inverse: **Yapılan seçimlerin geri alır.

**Feather: **Seçim yaptığımız bölgenin saydam bir şekilde görünmesini ve başka bir yerde kullanılabilmesini sağlar.

**Select Similar: **Seçim yaptığımız bölgenin dışındaki pikselleri seçer.

**Duplicate: **Objenin bir kopyasını alır ve orijinalinden ayırır.

**Clone: **Objenin kopyasını alır ve üzerine koyar.

**Find & Replace: **Find & Replace panelini açar.

**Crop Selected Image: **Seçilen objenin boyutlarını değiştirir (4).

**View Menüsü :**

**Zoom In: **İstenilen bölgeye yakından bakılır.

**Zoom Out: **Objenin uzaktan görünmesini sağlar.

**Magnification: **Belli bir oranda zoom yapmamızı sağlar.

**Fit Selection: **Seçili bölgenin ekrana göre büyütür veya küçültür.

**Fit All: **Çalışma ekranında olan tüm objelerin görünmesini sağlar.

**Full Display: **Belgenin tüm özellikleri ile görünmesini sağlar.

**Hide Selection: **Seçim yaptığımızda seçilmiş yeri gösteren klavuz çizgilerini görünmez yapar.

**Hide Edges: **Seçili bölgenin çevresindeki programın kendi koyduğu ve seçili olduğunu belirttiği çizgileri kaldırır.

**Hide Panels: **Ekranda görülen kontrol panellerini kaldırır.

**Rules: **Düşey ve yatay olarak ekranda boyutları gösterir.

**Grid: **Ekranı kareler halinde gösterir.

**Grid Options:** Karelerin özelliklerini ayarlamamızı sağlar.

**Guides: **Çizim anında kullanılan kılavuz çizgilerini gösterir veya gizler.

**Slice Guides:** Kesme işleminde kullanılan kılavuz çizgilerinin uzantılarını gösterir veya gizler.

**Guide Options:** Kılavuz çizgilerinin özellikleri ayarlanır.

**Status Bar:** Ne tür işlemler yaptığımızı gösteren, ekranın en altında bulunan status barın gizlenmesini veya görünmesini sağlar (4).

**Insert Menüsü :**

**Hotspot: **Kare, elips gibi objeler eklememizi sağlar.

**Slice: **Başka bir yerden kesilen bir objenin eklenmesini sağlar.

**Behaviors: **Behaviors (işlemler) panelini açmamızı sağlar.

**Image: **Resim gibi bir çok objeyi eklememizi sağlar.

**Empty Image: **Boş bir image oluşturmamızı sağlar.

**Symbol: **Seçili objeyi sembol haline dönüştürür.

**Tween Instances: **Seçili iki obje arasında uygun adımlar ile eklemeler oluşturur.

**Symbol Options:** Sembol oluşturmak için özellikleri ayarlamada kullanılan kullanılır.

**Layer: **Katman oluşturmak için kullanılır.

**Frame: **Animasyonlarda kullanılacak bölümleri oluşturmak için frame ilave edilir. Her bir resim bir hareketi ifade eder (4).

**Modify Menüsü :**

**Stroke: **Oluşturduğumuz objenin kenarlarına hat çizmemizi sağlayan Stroke panelini açar.

**Fill: **Kapalı bir alan içinde dolgu yapmamızı sağlayan Fill panelini açar.

**Effect: **Gölge, kabartama gibi efektler vermemizi sağlayan Effect panelini açar.

**Image Object: **Animasyon işleminde kullanılacak ilk objenin tanımlaması için kullanılır.

**Exit Image Edit: **Animasyonda kullanılacak objeler tanımlandıktan sonra işlemi tamamlamak için seçilir.

**Document:** Bütün dosyanın özeliklerini değiştirmek için kullanılır. Bu özellikler, dosyanın piksel boyutları, arka planın boyutları ve arka planın rengidir.

**Edge: **Oluşturulmuş bir objenin kenarlarını değiştirmek için kullanılır. Kenarları keskin kenar,** **daha yumuşak geçişlere sahip kenar ve belirli bir mesafede saydamlığı olan kenar olarak değiştirebiliriz.

**Free Transform: **Dosyanın veya dosya üzerindeki bir objenin yerini değiştirmek, döndürmek veya boyutlarını değiştirmek için kullanılır. Serbest el ile işlem yapmamıza olanak sunar.

**Transform: **Free Transform komutu ile yaptığımız işlemleri sayısal değerler girerek yapmamızı sağlar.

**Arrange: **Oluşturduğumuz objeleri ön plana almak veya arka plana göndermek için kullanılır.

**Align: **Seçili objenin yatay ve düşey konumunu ayarlamak için kullanılır.

**Join: **Oluşturulmuş iki veya daha çok objenin birleştirilmesi için kullanılır.

**Split: **Birleştirilmiş iki veya daha çok objeyi ayırmak için kullanılır.

**Combine: **İki veya daha çok sayıdaki objeler arasında işlem yapmak için kullanılır. Bu işlemler, birleştirmek, kesişim noktasını almak, kırpmak ve koparmaktır.

**Alter Paths: **Objelerin kenar şekillerini değiştirmek için kullanılır. Bir kareyi daireye veya çokgene çevirebiliriz. Ayrıca objelerin içlerini boşaltarak çerçeveler oluşturabiliriz.

**Merge Images: **Seçili** **bir veya daha fazla objesi tek bir obje haline getirerek üzerinde değişiklik yapılmasına olanak vermez.

**Merge Layers: **Katmanları birleştirerek tek bir katman haline getirir. Kapalı katmanlar varsa açılması gerekir çünkü komut kapalı katmanları ihmal eder. Katmanları birleştirildikten sonra değişiklik yapılmasına imkan vermez.

**Group: **İki veya daha çok objeyi tek bir grup haline getirerek taşımamıza, boyutlarını değiştirmemize, döndürmemize veya efekt eklememize olanak sağlar. İstediğimizde grubu görünmez yapabiliriz. Diğer birleştirme komutlarından farkı objeleri olduğu gibi almasıdır. Diğer komutlarda objelerin görünmez kısımları atılır, burada ise görünmez ancak arka planda durur.

**Mask Group: **Oluşturduğumuz gruba efekt ekler. Bunu iki yolla yapar. Birincisi üst objeden alt olanı çıkartır ve alt objenin normalde görünmeyen kısmını gösterir. İkincisi alt objeyi filitreleyerek üst objenin profilinde ve saydam olarak yeni bir şekil ortaya çıkarır.

**Ungroup: **Grup halindeki objeleri ayırarak eski haline getirir (4).** **

**Text Menüsü :**

**Font: **Yazdığımız yazının fontunu değiştirmemizi sağlar.

**Size: **Yazının yüksekliğini değiştirmemizi sağlar.

**Style: **Yazının stilini seçeriz. Bu stiller koyu yazı stili, italik yazı stili ve altı çizgili yazı stili.

**Align: **Yazdığımız yazının yerini ayarlamak için kullanılır.

**Editor: **Yazının tüm özelliklerini ayarlayabileceğimiz, text editor penceresini açar.

**Attach to Path: **Yazdığımız yazıyı bir çizgi ile ilişkilendirerek yazının çizginin durumuna göre şekil almasını sağlar. Bunun gibi yazıyı bir kare veya daire çevresine yazılmasını sağlayabiliriz.

**Detach from Path: **Bir önceki komut ile yapılan işlemin tersini alır.

**Orientation: **Yazdığımız yazıyı çevirmek veya oluşturulan objenin özel bir bölümüne yerleştirmek için kullanılır. İşlemi yapabilmek için yazının obje ile ilişkilendirilmiş olması gerekir (Attach to Path komutu ile).

**Reverse Direction: **Yazının çizgi eksenine göre ters çevrilmesini sağlar. Bunu yapabilmek için de yazının obje ile ilişkilendirilmiş olması gerekir.

**Convert to Paths: **Yazıyı parçalara ayırarak her harf ile ayrı ayrı işlem yapmamızı sağlar (4). ** **

**Xtras Menüsü :**

**Repeat Xtra: **En son olarak yapılan xtra komutunu tekrar eder.

**Blur: **Blur bir image filtresidir. Resimlerin piksellerini yumuşatarak görüntüyü matlaştırır. Blur, Blur More ve Gaussian Blur olmak üzere üç seçeneği vardır.

**Invert: **Resimlerin renklerini tersine çevirir.

**Other: ***Convert to Alpha**** ***ve*** ****Find Edges**** ***olmak üzere iki seçeneği vardır. İlk seçenek objeyi griye çevirir, ikincisi objenin kenar geçişlerini ön plana çıkarır.

**Sharpen: **Blur komutu ile matlaştırılan objenin netleştirilmesi için kullanılabilir. Normal objelerde keskin pikseller oluşturarak resme keskin netlik katar. Sharpen, Sharpen More ve Unsharp Mask olmak üzere üç seçeneği vardır.

**Photo Optics: **CSI Standartlarına uygun olarak resimler üzerinde işlemler yapmamızı sağlar. Bu işlemler renkleri tersine çevirmek, gri tonlar ile işlem yapmak, yazıları ön plana çıkarmak gibi işlemlerdir (4).

**Window Menüsü : **

**New Window: **Çalışma penceresi ile aynı boyutta yeni bir pencere açar.

**Toolbars: **Araç çubuklarının görünmesini veya gizlenmesini sağlar.

**Toolbox: **Toolbox araçlarının görünmesini veya gizlenmesini sağlar.

**Object: **Object panelinin görünmesini veya gizlenmesini sağlar.

**Stroke: **Stroke panelinin görünmesini veya gizlenmesini sağlar.

**Fill: **Fill panelinin görünmesini veya gizlenmesini sağlar.

**Effect: **Effect panelinin görünmesini veya gizlenmesini sağlar.

**Info: **Info panelinin görünmesini veya gizlenmesini sağlar.

**Tool Options: **Tool Options panelinin görünmesini veya gizlenmesini sağlar.

**Styles: **Styles panelinin görünmesini veya gizlenmesini sağlar.

**Color Mixer: **Color mixer panelinin görünmesini veya gizlenmesini sağlar.

**Swatches: **Swatches panelinin görünmesini veya gizlenmesini sağlar.

**Layers: **Layers panelinin görünmesini veya gizlenmesini sağlar.

**Frames: **Frames panelinin görünmesini veya gizlenmesini sağlar.

**Behaviors: **Behaviors panelinin görünmesini veya gizlenmesini sağlar.

**URL Manager: **URL Manager panelinin görünmesini veya gizlenmesini sağlar.

**Find & Replace: **Find & Replace panelinin görünmesini veya gizlenmesini sağlar.

**Project Log: **Project Log panelinin görünmesini veya gizlenmesini sağlar.

**Cascade: **Çalışma ekranını en büyük objenin boyutlarına göre ayarlar.

**Tile Horizontal: **Çalışma ekranını yatay olarak program ekranına açar.

**Tile Vertical: **Çalışma ekranını düşey olarak program ekranına açar (4).

**3.2.1.3. Kontrol Panelleri**

**Toolbox Paneli:**

Toolbox Paneli 31 adet araç (Tool) içerir. Bu araçlardan bazıları görünür bazıları görünmez. Görünmeyen araçları ortaya çıkarmak için araç kutucuğunun sağ alt köşesine fare imlecini basılı tutmamız gerekir. Tüm araçlar göründükten sonra istediğimizi seçip kullanabiliriz. En son kullanılan araç görünür halde kalır.

Bu araçların ne olduğu ve hangi işlerde kullanıldıkları **Araçlar** başlığı altında ayrıntılı olarak işlenecektir.

**Stroke Paneli :**

Stroke Paneli aracılığı oluşturduğumuz objelerin etrafına veya bağımsız çizgiler çizip onlara efektler ekleyebiliriz. Çizdiğimiz çizgilerin şeklini ayarlayabilmek için *Air Brush* yazan menüden seçimimizi yaparız. Buradan çizgimizin kategorisini seçeriz. Bu kategoriler, çizgimizin görünümünü belirler. *Basic *menüsü çizgimizin adını belirler. Bu menüden yapılacak seçim ile çizgimizin sert veya yumuşak geçişlere sahip olmasını sağlayabiliriz. Bunların dışında bu panelden çizgilerin renklerini ve kalınlıklarını değiştirebiliriz. Aynı zamanda çizgiye özel bir görünüm kazandıran Texture ekleyebiliriz (4).

**Fill Paneli :**

Fill Paneli aracılığı ile oluşturduğumuz kapalı alanlara özel efektlere sahip dolgular yapabiliriz. Kullanmak için kendisi ile birlikte gelen Texture efektlerini kullanabileceğimiz gibi kendimiz de bu tip efektler oluşturabilir veya Internet’ ten download edebiliriz. Bu panelden yapacağımız dolguların kategorisini seçebilir, dolgunun rengini değiştirebilir, saydam görünüşler veya sert geçişlere sahip görünümler ilave edilebiliriz. Ayrıca belirlediğimiz Texture efektinin kontrastını ayarlayabiliriz (4).

**Effect Paneli :**

Effect Paneli çok kapsamlı bir panel olup kullanımı oldukça geniştir. Bu panelden yapacağımız seçimler aracılığı ile oluşturduğumuz objelere birkaç kategoride efekt ilave edebiliriz. Bunlar:

**a) Inner Bevel: **Bu efekt oluşturduğumuz objenin kenarlarından içeriye doğru bizim değiştirebileceğimiz kalınlıkta ve kontrast derecesinde bir hat oluşturur. Ayrıca efektin ışık alma derecesini de ayarlamak bizim elimizdedir.(Şekil 3.13.)

**b) Outer Bevel: **Oluşturduğumuz objenin kenarlarından dışarıya doğru bir hat oluşturur. Inner Bevel efekti için geçerli ayarlar bu efekt için de oluşturulabilir.(Şekil 3.14.)

**c) Drop Shadow: **Objemize gölge eklemek için kullanılır. Eklediğimiz gölgenin objeye mesafesini, kontrastını, ışık alma derecesini ve yumuşaklığını değiştirebiliriz.(Şekil 3.15.)

**d) Emmbos: **Çalıştığımız objeye kabartama efekti eklemek için kullanılır. Bu efektin de diğerleri gibi ışık alma derecesini, kontrastını ve kalınlığını ayarlayabiliriz.(Şekil 3.16.)

**e) Glow: **Glow efekti ile objenin etrafına saydam bir tabaka oluşturabiliriz. Tabakanın kalınlığını, saydamlığını ve rengini istediğimiz gibi değiştirebiliriz.(Şekil 3.17.)

**f) Multiple Effect: **Aynı obje için Inner Bevel, Outer Bevel, Glow ve Drop Shadow efektlerinin kullanılmasına olanak sağlar.(Şekil 3.18.) (4).

** **Şekillerde görünen bu efektleri yazılar dahil bütün objeler için kullanabiliriz. Özellikle web sayfasındaki butonları oluşturmak için kullanılabilirler.

**Info Paneli :**

Info Panelinde objeler ile ilgili bilgiler mevcuttur. Bu bilgiler; Objenin yüksekliği, genişliği, başlangıç noktasının X ve Y koordinatlarına olan mesafesi ve rengindeki R G B değerleri gibi bilgilerdir. Ayrıca imlecin o anda bulunduğu noktanın koordinatlarını da görebiliriz. Program Info Paneli aracılığı ile objenin yüksekliğini ve genişliğini değiştirmemize olanak sağlar. Bunun gibi objenin X ve Y koordinatlarına olan mesafelerini de değiştirebiliriz (4).

**Styles Paneli :**

Styles Paneli, hazır yazı ve arka fon çeşitleri içeren bir kütüphanedir. Bu panelde yer alan elemanlar hazır olarak alınıp kullanılabilir. Program ile birlikte kurulumda 59 adet hazır eleman gelir. Bu stillerin maksimum bir sayısı yoktur. Çünkü kişi istediği kadar stil oluşturup bunları kullanabilir. Program ile gelen stillerin üzerinde de değişiklik yapabilir. Bu da çalışmalara zenginlik ve hız katar. Kullanılmaya stiller istenildiği takdirde silinebilir (4).

**Swatches Paneli :**

Swatches Paneli mevcut tüm ana renklerin görülebileceği bir paneldir. Renkler buradan seçildiği zaman kullanılacağı yerde aktif olur. Böylece başka menülere girmeden doğrudan renklerimizi seçebiliriz (4).

**Color Mixer Paneli :**

Color Mixer Paneli ile Swatches Panelinde olmayan ara renkleri seçebilir ve kullanabiliriz. Bu seçimi yapmak için alt tarafta görülen renk skalasını kullanabileceğimiz gibi R G B değerlerini de girerek renkleri elde edebiliriz. Bu yöntem ile bir çok ara renk elde etmemiz mümkündür (4).

**Layer Paneli :**

Layer Paneli ile çalışmalarımızı kolaylaştırmak için katmanlar oluşturabiliriz. Özellikle çok karmaşık işlerde katmanlama yapmak bize daha sade bir ortamda çalışma imkanı sunar. Çalıştığımız katmanı aktif yaparak diğer katmanları kapatabilir, böylece objenin bir tek bölümüne yoğunlaşabiliriz. Çalıştığımız katman ile işimiz bitince onu kilitleyebilir, yapacağımız diğer çalışmalardan etkilenmesini önleyebiliriz (4).

Yandaki simge layerin şu anda görünür olduğunu ifade eder.

Yeni bir katman eklemek için yanda görülen simgeyi seçmemiz yeterlidir.

İşimize yaramayan veya hatalı olan katmanları ise yanda görülen simge ile silebiliriz.

** Frame Paneli :**

Frame Paneli animasyon işlemleri için kullanılır. Fireworks programı ile Flash animasyonları gibi animasyonlar hazırlanamasa da gif animasyonları hazırlamak için çok uygundur. Her frame önceden hazırlanır. Daha sonra sıra ile frame kareleri çalıştırılarak animasyon oluşturulmuş olur (4).

**3.2.1.4. Araç Çubukları (Toolbars)**

** **Araç çubukları kolaylık olması açısından programlara yerleştirilmiştir. İçerdikleri komutlar bir veya daha çok menüde bulunabilir.

**Main Toolbar: **Her programda bulunan bu araç çubuğunun Fireworks programında görevleri aynıdır. En çok kullanılan komutları içerir. Bu komutlar ve simgelerini Şekil 3.25.’ teki sıra ile açıklamak gerekirse:

** New: **Yeni dosya açar.

** Open: **Kayıtlı olan bir dosyayı açar.

**Save: **Dosyayı kayıt eder.

**Import: **Farklı formatta olan bir dosyayı png formatına dönüştürür.

**Export: **png formatındaki dosyanın diğer formatlara dönüştürür.

**Undo: **En son yapılan işlemi geri alır.

**Redo: **Geri alınan işlemi iptal eder.

** Cut: **Seçili objeyi keser.

**Copy: **Kopyalama işlemi yapar.

**Paste: **Cut veya Copy işlemi ile seçilen objeyi istenilen yere yapıştırır.

**Object: **Object panelini açar veya kapatır.

**Color Mixer: **Color mixer panelini açar veya kapatır.

**Stroke: **Stroke panelini açar veya kapatır.

** Fill: **Fill panelini açar veya kapatır.

**Layer: **Layer panelini açar veya kapatır.

** Help: **Yardım penceresini açar veya kapatır (4).

**Modify Toolbar: **Modify menüsünün altında bulunan ve en çok kullanılan komutları içerir. Bu komutlar ve simgelerini Şekil 3.26.’ daki sıra ile açıklamak gerekirse:** **

** Group: **Seçili objeleri grup haline getirir.

**Ungroup: **Grup haline gelen objeleri ayırır.

** Join:** Oluşturulmuş iki veya daha çok objenin birleştirilmesi için kullanılır.

**Split: **Birleştirilmiş iki veya daha çok objeyi ayırmak için kullanılır.

**Bring to Front: **Seçili objeyi ön plana çıkarır.

**Bring Forward: **Seçili objeyi bir adım öne çıkarır.

** Send to Bacward: **Seçili objeyi bir adım geri gönderir.

** Send to Back: **Seçili objeyi arka plana gönderir.

**Align: **Seçili objenin yatay ve düşey konumunu ayarlamak için kullanılır.

**Rotate 90**°** CCW: **Seçili objeyi saat yönünün tersinde 90° döndürür.

**Rotate 90**°** CW: **Seçili objeyi saat yönünde 90° döndürür.

** Flip Horizontal: **Seçili objeyi yatay konumda döndürür.

** Flip Vertical: **Seçili objeyi düşey konumda döndürür (4).

**View Control Toolbar: **Ekran ayarlarımızı değiştirmek, işlem esnasında zoom yapmak gibi imkanlar sunar. Ayrıca o anda çalıştığımız ekranın boyutları hakkında bize bilgi verir.

**Page Preview:** Çalışma ekranının boyutları hakkında rapor verir (4).

**3.2.1.5. Araçlar**

** **Daha önce toolbox panelinde bahsettiğimiz araçlar (tool) objeleri oluşturmak için kullandığımız araçlardır. Bunlar ile kendimiz yeni objeler oluşturabileceğimiz gibi önceden hazırlanmış olanlar üzerinde de değişiklikler yapabiliriz. Çalışma sırasında en çok ihtiyacını hissettiğimiz elemanlar bunlardır. Bu elemanların neler olduğu ve nerelerde kullanıldığı açıklanacaktır. Açıklamalar alfabetik sıraya göre yapılacaktır.

**Brush: **Serbest elle çizgiler çizmemizi sağlar. Çizilen bu çizgilerde stroke paneli ile değişiklikler yapılabilir.

**Crop: **Almak istediğimiz bir yeri seçip Crop butonuna bastığımızda seçili yerin dışındaki tüm yerleri gizler. Toolbox panelindeki yeri

**Disort: **Çizdiğimiz bir objenin kenarlarından tutup istediğimiz yönde şekline değiştirmemizi sağlar. Toolbox panelindeki yeri

**Ellipse: **Elipsler çizmemizi sağlar. Klavyedeki Alt tuşuna basılı tutmak çizimi merkezden, Shift tuşuna basılı tutmak çizimi kenardan başlatacaktır. Toolbox panelindeki yeri

**Ellipse Marquee: **Marquee araçları çalışma esnasında belirli bölgelere efektler eklemek, seçimler yapmak, kesme veya yapıştırma işlemleri yapmak için kullanılır. İlk elipsimizi oluşturduktan sonra Shift tuşuna basılı tutarak istediğimiz sayıda elips çizerek bunları birbirilerine ekleyerek veya çıkararak değişik şekiller oluşturabiliriz. Bu elipsleri üç tipte oluşturabiliriz.

**Normal: **Bu her zaman kullandığımız, elipsin ölçülerini serbest elle belirlediğimiz yöntemdir.

**Fixed Ratio: **X ve Y yönünde belirli bir orana sahip elipsler oluşturabiliriz.

**Fixed Size:** X ve Y yönünde belli ölçülerde elipsler oluşturabiliriz.

**Eraser / Knife: **Genel olarak silme işlemlerinde kullanılır. Ancak boyutları ve silme renkleri ayarlanabildiği için objelere efekt verme işlemlerinde de kullanılabilir. ** **

**Export Area: **Seçtiğimiz bölgeyi farklı bir resim formatında kaydetmek için kullanılan bir komuttur. Bu komuttu Web sayfalarının grafik tasarımında çok kullanırız. Tasarladığımız grafiklere hareket vermek istersek grafikleri parçalara ayırıp kullanmamız gerekir. Bunun için de bu komutu kullanırız. Ayrıca resim kalitelerini azaltıp dosya boyutunu küçültmek için de bu komuttan yararlanırız. Toolbox panelindeki yeri

**Eyedropper: **Bir resim veya hazır gelen bir obje üzerinde değişiklik yapacağımız zaman objenin hangi renklere sahip olduğunu kestirmemiz zor olacaktır. Bu araç vasıtası ile istediğimiz bir bölgeden renk alarak rengin çeşidini belirleyebiliriz. Böylece saatlerce renk karışımları yaparak rengi tutturmaya uğraşmamış oluruz.

**Freeform: **Çizdiğimiz bir çizgiye form vermek için kullanılır. Bu formları serbest elle verebileceğimiz gibi belli ölçülere sahip S ve O’ lar yardımı ile de form verebiliriz. Toolbox panelindeki yeri

**Hotspot: **Hotspot objeler web sayfalarındaki linklerin verildiği objelerdir. Bu objelere tıkladığımızda web sayfasının başka bir sayfasını açar veya link verildiği sayfayı görüntüler. Bu komut ile dairesel, dörtgen veya çokgen olarak bu objeleri oluşturabiliriz.

**Lasso: **Serbest elle çalıştığımız alandan seçimler yapmamızı sağlar. Bu seçimler tamamen bizim el becerimiz ile ortaya çıkar. Fareyi nasıl yönlendirirsek öyle bir seçim yapmış oluruz. Seçimimizi dairesel olarak çalışıp kapatmazsak program seçimi kendi kapatarak kapalı alan oluşturur. Bunun için seçimimizi iyi belirlememiz gerekir. Toolbox panelindeki yeri

**Line: **İstenilen uzunlukta ve açıda doğrusal çizgiler çizmek için kullanılır. Bu çizgilerin uzunlukları kenarlardan tutularak değiştirilebilir. İstenilen yere taşınabilir. Freeform komutu ile uzatılarak değişik şekiller elde edilebilir.

**Magicwand: **İçinde bir obje olan alanı seçmek için kullanılır. Arka alanı objeden çıkarmak için kullanılabilir. Toolbox panelindeki yeri

**Magnify: **%6’ dan %6400’ e kadar zoom yapmamızı sağlar. Ekranı yakınlaştırmak için simgeye tıklayıp farenin sol tuşuna basmamız gerekir. Her basışımızda ekran belirli bir oranda yaklaşacaktır. Ekranı uzaklaştırmak için ise klavyedeki Alt tuşuna basıp daha sonra farenin sol tuşuna basmamız gerekir. Yine aynı şekilde her basışımızda belirli bir oranda ekran uzaklaşacaktır.

**Paint Bucket:** Oluşturduğumuz kapalı alan objelerin içini istediğimiz renkte boyamak için kullanılır. Rengi seçip objenin içini seçmemiz yeterlidir.

**Pan: **Çalıştığımı ekranı kaydırarak istediğimiz bölgeye gelmek için kullandığımız komuttur.

**Path Scrubber: **Objelerin kenarlarında bulunan çerçeve, çizdi veya süsleme gibi efektleri gölgelendirmek için kullanılır. Efektler arasında yumuşak geçişler yapmak için + veya – simgelerinden birini seçip imleci hat üzerinde gezdirmek yeterlidir. Toolbox panelindeki yeri

**Pen: **Düz veya açılı çizgiler çizmek için kullandığımız bir araçtır. Yatay veya düşey çizgiler çizmek için Shift tuşuna basılı tutup fareyi istediğimiz yöne doğru hareket ettirdiğimizde çizgileri çizmiş oluruz. Aynı yöntemle 45°’ lik çizgiler de çizilebilir. İstediğimiz taktirde çizgileri ovalleştirmemize de izin verir. Bunun için ise işlemi yaparken Alt tuşuna basmak gereklidir.

**Pencil: **Serbest elle çizgiler çizmek için kullanılan bir araçtır. Çizilen çizgilerin Stroke Paneli aracılığı ile renkleri, kalınlıkları ve saydamlıkları değiştirilebilir. Ayrıca çizgiye Texture ilave edilebilir.

**Pointer: **Objeleri taşımak veya yeniden boyutlandırmak için kullanılır. Objeleri taşımak için seçip sürüklememiz yeterlidir. Alt tuşunu basılı tutup objeyi sürüklediğimizde kopyalamış gibi objeden bir tane daha elde etmiş oluruz. Shift tuşunu basılı tutarak grup halindeki objeleri hareket ettirebiliriz. Toolbox panelindeki yeri.

**Polygon: **3’ ten 25’ e kadar noktaya sahip yıldız veya 3 kenarlıdan 25 kenarlıya kadar çokgen çizmemizi sağlar. Toolbox panelindeki yeri

**Rectangle: **İstediğimiz boyutlarda dikdörtgenler çizmemizi sağlar. Dikdörtgenleri köşeleri yuvarlatılmış olarak çizmekte mümkündür. Shift tuşuna basılı tutup merkezi kenardan olan bir dikdörtgen çizebiliriz. Bunun gibi Alt tuşunu basılı tutarak merkezden başlangıç noktası olan bir dikdörtgen çizebiliriz. Toolbox panelindeki yeri

**Redraw Path: **Çizilmiş olan bir çizginin yolunu yeni bir çizgi çizerek değiştirir. Eski çizgi yeni çizginin başlangıç noktasından itibaren kesilip atılır. Toolbox panelindeki yeri ** **

** Reshape Area: **Bu araç ile oluşturduğumuz objelerin kenarlarını istediğimiz şekilde uzatabilir ve değiştirebiliriz. Yeni ve estetik şekiller oluşturmak için bu aracı kullanırız. Bu işlemi iç çapı ve dış çapı birbirinden farklı iki çember aracılığı ile yaparız. Çemberlerin çaplarını ayarlayarak istediğimiz hassasiyette ve yumuşaklıkta objeler elde etmemiz mümkündür. Bu işlemi yazılar üzerinde de uygulamak mümkündür. Ancak önce yazıları Convert to Path komutu ile harflere ayırmak gerekir. Toolbox panelindeki yeri

**Rubber Stamp: **Bir resmin veya hazır olarak alınmış objenin bir bölümünün veya tamamının kopyasını almak için kullanılır. İlk olarak, almak istediğimiz noktayı seçip seçim dairesinin çapını ayarladıktan sonra, çalışma ekranının başka bir noktasına gidip fare ile tıkladığımızda seçim dairesinin içinde görülen kısmın aynısını yapıştırır. Farenin sol tuşuna basılı tutup sürüklediğimizde seçim dairesinin geçtiği yerlerdeki görüntüleri karşı tarafa kopyalar.

**Scale: **Seçtiğimiz objeyi yeniden boyutlandırmak, başka bir yere taşımak veya çevirmek için kullanılan bir komuttur. Yaptığımız bu işlemleri serbest elle yapabileceğimiz gibi değerler girerek de yapabiliriz. Döndürme işleminde objeyi kendi merkezinden döndürebiliriz veya merkezi değiştirip onun etrafında döndürme işlemini yapabiliriz. Toolbox panelindeki yeri

**Select Behind: **Çalışma sırasında oluşturduğumuz katmanlar arasında geçişler yapmak için kullanılır. Bunu gibi sonlandırılmış işlemlerin arka planlarını değiştirmek için de kullanılabilir. Toolbox panelindeki yeri

**Skew: **Çizdiğimiz objelerin kenarlarından tutarak doğrusal olarak uzatmamızı sağlar. Uzatma işlemini önce sadece X ve Y doğrultusunda yapar. Objemizin şekli değiştikten sonra uzatmaya çalıştığımız çizginin doğrultusundan çıkmak mümkün değildir. Çıktığımız zaman oluşan şekli program kabul etmeyecektir. Toolbox panelindeki yeri ** **

**Slice: **Oluşturduğumuz objeleri parçalara ayırmak için kullanılan bir komuttur. Objeleri istediğimiz boyutlarda karelere bölebilir, her kareyi farklı bir resim formatında Export edebiliriz. Web sayfası tasarımında en çok kullandığımız komuttur. İlk önce web sayfasının tamamının grafik tasarımını yaparız. Daha sonra kullanmak istediğimiz kısımları Slice komutu ile kesip parçalara ayırırız. Bu parçaları web sayfasında gerekli yerlere yerleştirdikten sonra sayfamızı oluşturmuş oluruz. ** **

**Subselection: **Tüm seçim işlemlerini yaptığımız araçtır. Bir objeye işlem uygulamadan önce objenin bu araç ile seçilmiş olması gereklidir. Objeleri taşımak için de kullanılabilir. Bunun yanında şekil değiştirme işleminde kullanmakta mümkündür.

**Text: **Yazı yazmak için kullandığımız komuttur. İstediğimiz fontta ve boyutlarda yazılar yazabiliriz. Bunun için Text komutuna bastıktan sonra yazının yazılacağı yere bir dikdörtgen çizeriz. Karşımıza gelen Text Editor penceresinde yazımızı yazıp boyutunu ve fontunu ayarladıktan sonra yazımız yazılmış olur. Yazı fontları olarak program ile birlikte gelen fontları kullanabileceğimiz gibi Internet’ ten güzel fontlar bulup kullanabiliriz (4).

**3.2.2. Web Sayfasının Grafik Tasarımı**

** **Daha önce de bahsettiğimiz gibi Web sayfası tasarımında kullanılan bir çok yol vardır. Bunardan en basit ancak görsellik açısından en zengin olan grafik tasarımı yöntemidir. Bu yöntemde sayfanın görünümü grafiksel olarak, bir program aracılığı ile oluşturulur. Daha sonra oluşturulan objeler parçalara ayrılarak başka bir program aracılığı ile web sayfası haline getirilir.

Grafikleri hazırlamada dikkat edilmesi gereken bazı noktalar vardır. İlk önce hazırlayacağımız sayfanın amacı tespit edilmelidir. Gereksiz banner ve animasyonlarda kaçınılmalıdır. Unutulmamalıdır ki Internet veri alışverişi sitemine göre çalışır. Bu sistem de belirli bir hızda çalışmaktadır (56Kbps). Yaptığımız animasyonlar büyük yer kaplar bu da sayfaların yüklenmesini geciktirir. Renk seçimleri uygun yapılmalıdır. Yazı fontları ve boyutları göze hoş gelecek şekilde seçilmeli, gerekirse efektler ilave edilerek desteklenmelidir. Buton gibi elemanlara hareket verilecekse, sayfaya konulmadan önce mutlaka denenmeli, sorunsuz çalıştığı görüldükten sonra sayfaya konulmalıdır. Kullandığımız resimlerin boyutları fazla büyük olmamalıdır. Bunu gerçekleştirmek için resimlerin kaliteleri ile oynamak mümkündür. Ancak çok düşük kalitedeki bir resim az yer kaplamasına rağmen görüntüsü de o oranda kötüdür. Bu bütün emeğimizi boşa çıkarabilir. Kalitesi düşürmeden farklı resim formatları kullanılarak bunu çözüme kavuşturmak mümkündür. Ancak günümüzde resimlerin kalitesini düşürmeden boyutlarını küçülten programlar da bulunmaktadır. Bunlar gibi daha bir çok dikkat edilmesi gereken noktalar vardır. Bunlar zaman ve tecrübe gerektiren hususlardır.

**3.2.2.1. Artalanın Belirlenmesi**

** **Artalan bir web sayfası için çok önemlidir. Tüm çalışmalarımızı üzerinde taşıyacak olan artalandır. Uyumsuz bir renk kullanımı sayfanın ana tasarımını bozabileceği gibi gözü yorarak sayfanın anlaşılabilirliğini de olumsuz yönde etkileyecektir. Ayrıca arka planda karmaşık şekillerin ve düzensiz kompozisyonların da kullanımı tasarımı etkileyecek diğer bir önemli etkendir.

Fireworks programında artalanı belirlemek için önce 800x600 piksellik yeni bir ekran açarız. 800x600 olmasının sebebi web sayfamızın bu boyutlarda görünecek olmasıdır. Daha büyük olması durumunda yapacağımız çalışmalar küçük piksellere sahip bilgisayarlarda yarım görünecektir. Şu anda standart olarak pek çok bilgisayar bu boyutları kullanmaktadır.

File menüsünün altından New komutunu seçtikten sonra karşımıza Şekil 3.28.’ deki pencere gelir. Buradan istediğimiz boyutları seçip Ok tuşuna basarız.

Yeni pencereyi açtıktan sonra Rectangle aracı ile açılan çerçeve boyutlarında bir dikdörtgen çizeriz. İstediğimiz rengi dolgu rengi olarak belirleyip Paint Bucket aracı ile dikdörtgenimizin içini boyarız. Bunu yaptıktan sonra istersek renk skalasından rengin tonlarında değişiklikler yapabilir, uygun tonu yakalayıncaya kadar deneyebiliriz.

Arka planımıza dolgu efekti eklemek için Fill Panelindeki Texture araçlarını kullanırız. Oluşturduğumuz dikdörtgeni Subselection aracı ile seçip Fill panelindeki Texture araçlarından birisini seçmek yeterlidir. Arka planımız Texture halini alacaktır. Texture efektinin görülmemesi halinde efektin yüzde oranı arttırılarak görünür hale gelmesi sağlanabilir (Şekil 3.29.). Bundan sonra arka plan ile işimiz bitmiştir. Diğer objelerin oluşturulmasına devam ederiz.

**3.2.2.2. Banner Oluşturulması**

** **Banner tasarımı yaparken dikkat edilmesi gereken en önemli nokta bannerın anlatılmak istenen konuyu en kısa ve en sade şekilde ifade etmesidir. Örnek olarak; yüksek faiz veren bir bankanın reklam bannerının tasarımında döviz simgeleri kullanmak amaca uygun olmayacak ve imajın büyüklüğünü de arttıracaktır. Bunun yerine, bankanın logosu ve yüksek faiz verdiğine dair bir açıklama cümlesi ile anlatılmak istenen konu kullanıcıya sorunsuz bir şekilde ulaştırılmış olur. Banner tasarımında da kompozisyona, renk seçimine ve kullanılacak olan yazı tipine dikkat edilmeli, animasyonlu bir banner tasarımı yapılacaksa, yeni çıkan programların “Layered Animation” özelliği kullanılarak animasyonun gereksiz kareleri çıkartılarak hazırlanmalıdır, böylelikle imaj büyüklüğü sabit kalacak ve anlatılmak istenen konu da açıkça işlenecektir.

Yapacağımız sitenin üniversite öğretim görevlisine ait olacağı düşüncesi ile tasarlayacağımız banner da Teknik Eğitim Fakültesi’ nin logosunun kullanılması uygun bulunmuştur. Banner stabil olacaktır, animasyon içermeyecektir.

İki parçalı bir banner tasarlanacaktır. Bir tarafında logo,öbür tarafında üniversitenin ismi yazılı olacaktır. Yeni bir layer oluştururuz. Fakülte logosunu Insert menüsünün altındaki Image komutu ile alırız. Çok sade olmaması için önce Inner Bevel efekti ekleyip kenarları düzeltir ve ışık efekti veririz (Şekil 3.30.). Göze daha hoş görünmesi ve ışık efektini tamamlaması açısından Drop Shadow efekti de ekleriz (Şekil 3.31.).

Logo efektleri verildikten sonra, bir elips çizerek logonun altına yerleştiriyoruz. Tam olarak ortalayabilmek için ok tuşları ile hareket ettiriyoruz. Ayarlarımızı yaptıktan sonra elipse Emboss efekti vererek kabartma bir şekil oluşturuyoruz (Şekil 3.32.). Bannerımızın ilk kısmı tamamlanmış oluyor.

Uygun bir font seçip yazıyı yazıyoruz. Font kadar harf yüksekliğine de dikkat etmek zorundayız. Harflerin büyük olması görüntüyü bozar, küçük olması ise okumayı zorlaştırır.

Yazıya önce Inner Bevel, daha sonra Outer Bevel efektlerini vererek görünüşü zenginleştiriyoruz (Şekil 3.33. ve Şekil 3.34.)

Yazının etrafına köşeleri yuvarlak olan bir dikdörtgen çiziyoruz. Logodaki elipsin efektlerini bu dikdörtgene de uyguluyoruz. Bu bannerımızın bütünlüğünü sağlayarak göze daha hoş görünmesini sağlayacaktır. Bu işlemden sonra logo ve yazıyı web sayfasında kullanılacak haline getirip Export işlemi ile jpg formatında resim olarak bir klasörün içine kaydediyoruz.

**3.2.2.3. Butonların Oluşturulması**

** **Buton tasarımında göz önünde bulundurmamız gereken hususlardan başlıcaları diğer etmenlerde olduğu gibi yine renk uyumu, estetik görünüş, boyut gibi faktörleridir. Butonlar sayfanın genel görünüşünü bozmayacak şekilde yerleştirilmelidir. Renkleri artalanın, yazıların ve animasyonların renkleri ile uyum içinde olmalıdır. Hareketli butonlar kullanıldığı zaman hareket efektinin çalışıp çalışmadığı önceden kontrol edilerek sayfaya butonlar yerleştirilmelidir. Kullanımın rahat olması için butonları uygun büyüklükte yapmak ve uygun yere yerleştirmek şarttır.

Buton tasarımına başlamadan önce, yerini tespit edip buton boyutunu ona göre belirleriz. Bizi kullanacağımız butonlar sol frame alanında yer alacak ve hareketli buton olacaktır. Bu hareketten kastımız fare imleci üzerine geldiğinde buton içeriye doğru bir hareket yapacaktır.

Sayfamızın düzenine göre buton sayısını tespit ettikten sonra butonlarımızı oluşturmaya başlayabiliriz. Köşe radyüsleri 4 olan bir dikdörtgen oluşturuyoruz. Emboss efektini kullanarak kabartama efekti veriyoruz. Böylece banner ve butonlar bütünlük içinde olacaktır. Tespit ettiğimiz sayı kadar oluşturduğumuz, butondan Clone komutu çoğaltıyoruz (Şekil 3.36.). Daha güzel görünmesi için butonların altına bir bar ilave ederek, efektlerini de verdikten sonra butonları üzerine yerleştiriyoruz (Şekil 3.37.). Butonların üzerine yazılarını yazıp, yazılara de Inner Bevel, Outer Bevel ve Drop Shadow efektlerini veriyoruz (Şekil 3.38.). Oluşan objeyi Clone komutu ile çoğaltıyoruz. Hareket efektini verebilmek için butonların taşıdıkları tüm efektleri tersine çeviriyoruz. Yazıların efekte destek olmaları için konumlarını X ve Y de bir veya en fazla iki birim değiştiriyoruz ve kontrastlarını düşürüyoruz (Şekil 3.39.). Butonlar web sayfasında kullanılmaya hazır hale gelmiş durumdadır. İlk oluşturduklarımız butonun ilk hali yani sayfa açıldığında karşımıza gelen halidir. İkinci oluşturulan butonlar ise, fare imlecinin üzerine gelmesi ile oluşan hareket efektini sağlayacak olan butonlardır. Butonları Slice aracı ile kesip web sayfasına Navigation Bar olarak aktardığımızda, hareketli buton menüsünü elde etmiş oluruz (Şekil 3.40.). Navigation Bar oluşturma işlemi Dreamweaver programının bir özeliği olmasından dolayı daha sonra anlatılacaktır.

Slice işlemini uygularken dikkat etmemiz gereken nokta seçim karesinin boyutudur. Butonun ilk ve son halini kesen karenin aynı boyutta olması gerekir. Bu olmadığı zaman hareket efekti düzgün çalışmayacaktır.

Daha önceki anlatımlarımızda hareket efektinin kontrol edilmesi gerektiğini söylemiştik. Bunu şu noktada yapmamız mümkündür. Kestiğimiz butonların ilk ve son hallerini, AcdSee gibi resimlere arka arkaya bakabildiğimiz programlarda açıp, önce ilk halinin sonra ikinci halinin resmine baktığımızda efektin doğru çalışıp çalışmadığı anlaşılabilir.

** **Oluşturulan tüm objeler artık web sayfasında kullanıma hazır hale gelmiştir. Bundan sonra yapılacak işlem sayfayı düzenlemektir. Bunun için Dreamweaver programını kullanırız.

## **BÖLÜM 4******

## **WEB SITESININ OLUŞTURULMASI**

## **4.1. DREAMWEAVER**

Dreamweaver, Macromedia firmasının geliştirdiği web sitesi tasarımı için kullanılan bir programdır. Bu tip programlar bizleri HTML kodları yazma eziyetinden kurtaran, daha kısa zamanda daha fazla iş yapmamızı sağlayan aracılarıdır. Grafik tasarımlarını web sayfasında kullanmak için Dreamweaver gibi bir program kullanırsak, HTML kodları yazarak yaptığımız tasarımlardan çok daha güzel tasarımlar elde etmiş oluruz.

**4.1.1. Dreamweaver Programının Menüleri ve Kullanımı**

** **Bu programda da diğer programlara benzer menüler ve kontrol panelleri vardır. Bu elemanları tanıtarak programın genel çalışma ilkeleri ve bir web sitesinin nasıl oluşturulduğu adım adım anlatılacaktır.

**4.1.1.1. Programın Çalışma Ekranı **

Şekil 4.1.’ de görüldüğü gibi programın çalışma ekranı menüler, kontrol panelleri ve çalışma alanında oluşmaktadır. Çalışma alanı biraz karışık gibi görünmektedir. Bu şekil sadece programın içerdiği bu menüleri gösterir. Çalışma esnasında kullanıcı bu panellerin içinde boğulup kalmaz, hangisini kullanmak istiyorsa onu açıp, kullandıktan sonra kapatma şansı vardır.

**4.1.1.2. Menüler ve Kontrol Panelleri **

**File Menüsü:**

**New:** Yeni, boş bir sayfa açmamızı sağlar.

**New From Template: **Template dosyaları açmamızı sağlar. Önceden oluşturulmuş şablonları açmakta kullanılır.

**Open: **Varolan bir dosyayı açmamızı sağlar.
**Open In Frame: **Frame içeren sayfalarımızda frame alanına bir dosya açmamızı sağlar.

**Close: **Dosyayı kapatmamızı sağlar.

**Save: **Dosyamızı kaydetmemizi sağlar.
**Save As: **Dosyayı** **başka bir isimle içeriğini değiştirmeden kaydedebilmemizi sağlar

**Save As Template: **Kaydettiğimiz dosyayı, Template yani Şablon olarak kaydedip daha sonra kullanmamıza olanak tanır.

**Save Frame Set: **Frame kullandığımızda frame içeren Frame Setini kaydetme olanağı tanır.

**Save Frame Set As: **Frame Setimizi başka bir isimle veya uzantıyla kaydetmemizi sağlar.

**Save All:** Frame alanları ile çalıştığımız zaman, hem Frame alanlarımızı hem de Frame Setimizi aynı anda kaydedebilme seçeneği sunar.
**Revert:** Dosyayı ilk açtığımız haline geri getirir.

**Design Notes: **Dosyamızla çalışırken yaptığımız çalışmalarla ilgili notlar alabilmemizi sağlayan bir board.

**Import: **Bu komut, açılan bir menüdür. Dosyanıza XML, Word HTML ve Table Data dosyalarını dahil edebilirsiniz.

**Export: **Çalışmamızı XML, CSS ve Table Data olarak gönderebilmemizi sağlar.

**Convert: **Çalışmamızı 3.0 Browserlara ayarlı olarak, dönüştürür. Çalışmamız bir çok özelliğini kaybedecektir. Mesela; CSS' ler, Swap yada Rollover Image gibi özellikleri kaybeder. Bunu geçerli dosyamızda yapmaz. Yeni bir dosya yaratarak yapar.

**Preview In Browser: **Bu seçenek de açılır bir menüdür. Belirlediğiniz Browserler bu açılır menüde yer alır. *Edit Browser List*** **seçeneğini tıklarsak, Preferences Penceresi açılır ve bize Browser seçeneklerini belirlememizi sağlar. Açılan pencerede Primary yani birincil olarak belirleyeceğimiz browser, F12** **tuşuna bastığımız zaman görüntülenecek Browser olacaktır.

**Check Links: **Kırık veya External (Harici) Linkleri bulmamızı sağlar. Seçtiğimiz zaman, bir pencere açılır ve HTML kodunu tarayarak, bize kırık linkleri bildirir.

**Check Target Browsers: **Bu seçeneği seçtiğimizde, bir pencere açılır ve bir browser tipi ve sürümü seçmemiz istenir. Seçip *Check*** **butonuna tıkladığımız zaman, açılan bir Browser Penceresinde bulunan hatalar bir rapor halinde sunulur.

**Son Çalışılan Dosyalar: **Altta gördüğümüz dosya isimleri de çalışılan son 4 dosyayı simgeler.

**Exit: **Programdan çıkmamızı sağlar (5).

**Edit Menüsü:**

**Undo: **Son yaptığımız işlemleri geri alabiliriz. Her defasında, işlemimizi bir geriye alırız. Geri alma sayısı Preferences seçeneğinden ayarlanır.
**Redo: **Geri aldığımız işlemleri ileri almamızı sağlar.

**Cut: **Seçili olan imajımızı, Layer veya text, kısacası elimizde olan objelerin tümünü kesmeye yarar.

**Copy: **Seçili olan objelerimizi kopyalamaya olanak tanır. Çoğaltma işlemlerinde kullanılır.
**Paste: **Kopyalayarak veya keserek aldığımız objeleri, seçili yere yapıştırmamızı sağlar.
**Copy Text Only: **Normalde bir text seçilip kopyalandığı zaman, HTML Kodlarıyla birlikte kopyalanır. Kopyalarken bu seçeneği kullanırsak, sadece text olarak kopyalanacak ve kodları dahil etmeyecektir.
**Paste As Text:** Kopyaladığımız yazıları sadece text olarak yani kod olmaksızın yapıştırmamızı sağlar.

**Select All: **Sayfamızdaki bütün objeleri veya bir Layerın içindeki tüm nesne veya objeleri seçebiliriz.

**Select Parent TAG: **İmlecimizin bulunduğu tagı komple seçebiliriz.

**Select Child TAG: **İmlecimizin bulunduğu yerdeki alt tagın içeriğini seçmemizi sağlar.
**Find: **Sayfamız içerisinde kullandığımız bir kelimeyi, bir harfi veya bir tagı bulmamızı sağlar. *Find Next* seçeneği ile, sonrakini, *Find All* seçeneği ile hepsini arattırabiliriz. Find All dediğimiz zaman Find penceresinin altında bir pencere açılır ve bulduklarının üzerine iki kere tıklarsak, yerini saptayabiliriz. Ulaşmak istediğimiz bilgilere kolayca ulaşabiliriz.

**Find Next: **Sayfamızdayken F3 tuşuna basarsak, aradığımız kelimenin veya harfin, bir sonraki bulunduğu yeri seçerek bize gösterir.

**Replace: **Aradığımız veya arayacağımız kelimenin, tagın bulunup belirttiğimiz yeni değerle değiştirilmesini sağlar. Replace All seçeneğiyle hepsini bulur ve yeni verdiğimiz değerle değiştirir.
**Launch** **External Editor: **Preferences ayarlarında hangi editörü harici olarak belirlediysek, çalıştığımız dosyayı son haliyle o editörde açar.

**Preferences: **Dreamweaver programının ayarlarını içerir (5).

**View Menüsü:**

**Head Content:** Seçtiğimizde açılan editör, çalışmamızın, *<HEAD>......</HEAD>*** **tagları arasında yer alan kodları düzenlememizi sağlar. Bunların üzerine tıkladığımız zaman, açılan Properties penceresinden ayarlarımızı yapabiliriz. Böylece HTML kodlarına girmeden HEAD tagı içindeki içeriği düzenleyebiliriz. Mesela kullandığımız bazı Java Script kodlarını, title (Başlık) gibi.

**Invisible Elements: **Bize görünen ama tarayıcılarda görünmeyen elementlerin çalışma sayfasında görünüp, görünmeyeceğini ayarlamamıza olanak tanır.

**Layer Borders: **Layer çizgilerini gizler veya gösterir.** **Kullandığımız katmanların dış çizgilerini kapatır veya açarız.

**Table Borders:** Çalıştığımız dosyada, tabloların kenar çizgilerini gizler veya gösteririz.
**Frame Borders:** Dreamweaver programında Frame alanı olan bir sayfa hazırlarken, programı kapatıp açarsak, Frame mesafelerini ayarladığımız Border araçlarının kaybolduğunu görürüz. Kaybolan Frame kenarlarını buradan açabiliriz.

**Image Maps: **İmajlarda kullandığımız HotSpot yani sıcak noktaların çalışma anında gösterilip, gösterilmeyeceğini belirleriz.

** Ruler: **Bu seçeneğimiz de çalışma alanımızın üst ve sol yanına cetvel açabilmemize olanak tanır. Orijin noktasını yani "0" noktasını sol köşedeki merkezden tutup istediğimiz yere sürükleyebiliriz. Cetvelimizin birimini de değiştirebiliriz. Birimleri; Piksel İnç ve Santimetredir.** **

**Grid: **Sayfamızda hizalama ızgaralarını açabiliriz. Bu ızgaralar bize nesneleri birbirine hizalamamızda yardımcı olur. Ayrıca, *Snap To* yani ‘ızgaraya yapış’ özelliğini açarak, taşıdığımız nesnelerin, ızgaraya yani Grid noktalarına duyarlı hale gelmesini sağlayabiliriz. *Settings* bölümünden, Grid noktalarımızın rengini, çizgi ya da nokta görünümünde mi olacağını, taşıdığımız nesnelere duyarlı olup olmayacağını ve son olarak da ızgaralar arası boşlukların ne kadar olacağını ayarlayabiliriz (Şekil 4.5.).

**Tracing Image: **Belirleyeceğiniz bir imajı rehber olarak kullanmanızı sağlar.

**Plug-Ins (Sayfada Kullanılan Plug-In'ler)**

**Play All: **Bu seçenek kullandığımız Plug-In' leri çalıştırmamızı sağlar.

**Stop All: **Sayfada kullandığımız Plug-In'lerin çalışmasını durdurur. (Test Çalışmasını)
**Status Bar: **Status Bar aracını açıp kapatmamızı sağlar (5).

**Insert Menüsü:**

Bu menüdeki komutlar çok kullanıldığı için komut ile birlikte nasıl kullanıldığı da açıklanacaktır.

**Image Komutu:**

Menü çubuğunda Insert menüsünden Image komutu seçilir. Ekrana gelen Select Image Source iletişim (Şekil 4.7.) kutusunda resmin web’ deki veya bilgisayardaki yeri URL metin kutusuna girilir veya resim dosyasını bulana kadar bilgisayardaki dosyalar ve klasörler arasında dolaşılır. Resim dosyası ikonuna tıklandığında dosya ismi File name metin kutusuna girilir. Select tuşuna tıklayarak, resim sayfaya eklenir.

Dreamweaver programında, HTML programlarının çoğunda olduğu gibi, bir resim seçildiğinde Properties denetçisi resimlere özgü özellikleri gösterir. Bunun için özelliklerini görmek istediğimiz resim seçilir. Properties denetçisi o resmin özelliklerini gösterirken, resmin ufak bir örneğini *Apply* (uygula) düğmesi olarak gösterir. Denetçinin sağlayabileceği tüm resim özelliklerini görmek için, denetçinin sağ alt köşesindeki genişletme okuna tıklanabilir (Şekil 4.8.).

Resim sayfaya yerleştiğinde, ayarlanabilecek pek çok özelliği vardır. Bunların arasında görünüş özellikleri (boyut ve çerçeve), sayfa düzeni özellikleri (hizalama, Vspace ve Hspace) ve sayfa yükleme özellikleri (alt etiketleri ve düşük çözünürlük) vardır. Resimler için bir isim belirlenmesi de mümkündür. Bu isim, ekranda gösterilmez. Ancak doğrudan kod üzerinde çalışma planlanıyorsa yararlı olabilir ve Java Script veya Visual Basic Script kodunda resimleri kullanmak için gereklidir (5).

Dreamweaver programında resimlerin gösterilmesi için varsayılan, resimlerin çerçevesiz gösterilmesidir. Ancak istenirse bir çerçeve eklenebilir. Bunun için; çerçeve eklemek istediğimiz resim seçilir. Properties denetçisinde, border metin kutusuna piksel cinsinden bir değer girilir. Enter tuşuna veya Apply düğmesine tıklandığında resim etrafında bir çerçeve belirir.

Dreamweaver programında bir resmi ilk kez yerleştirdiğimizde, oluşturulduğu sırada sahip olduğu orijinal ölçülerini alır. Sayfanın düzenine uydurmak için bir resmi yeni bir yükseklik ve genişlik atamak için; boyu değiştirilmek istenen resim seçilir. Properties denetçisi resmin ölçülerini W (Width) ve H (Height) metin kutularına piksel cinsinden girilir.

Resimlerin hizalanması için yine properties denetçisinde Align (Hizala) listesine tıklanır. Bir seçenek seçildiğinde, resim hareket eder. Bazı seçenekler sadece başka nesnelerle bir araya geldiklerinde diğerlerine göre farklı görünürler.

**Browser Default; ** hizalaması genellikle baseline dır.

**Baseline; **seçeneği resmin alt tarafını yazını en yakın nesnenin temel çizgisi ile hizalar. Bir yazının temel çizgisi yazının üzerine oturduğu hayali bir çizgidir.

**Bottom; **seçeneği, resmin altını yakındaki en büyük nesnenin yanına hizalar.

**Top; ** seçeneği, resmin üstünü nesnenin üstüne hizalar.

**Middle; ** resmin ortasını yazının temel çizgisi ile hizalar.

**Text top; **resmin üstünü en yakınındaki yazı satırındaki en uzun karakterle hizalar.

**Absolute bottom;** resmin altını en yakınındaki yazı satırında en aşağı inen karaktere göre hizalar.

**Absolute middle; ** resmin ortasını yazını ortası ile hizalar.

**Left ve right; ** seçenekleri resmi sayfa kenarına göre hizalar, resmin sayfa kenarında kalması için yakınındaki yazıyı alt satıra atar.

Boşluk eklemek için properties denetçisinde Vspace ve Hspace metin kutusuna piksel olarak bir değer girilir.

Kullanıcıların resimlerin içeriklerini öğrenebilmesi için alternatif bir yazı sağlanması gerekir. Bunun için alt etiketinin kullanılması gerekir. Bunun için; alt etiketi eklenecek resim seçilir. Properties denetçisinde alt metin kutusuna bir açıklama yazılır.

Resimlerin yüklenmesini yine properties denetçisinde bulunan bir özellik ile daha çabuk hale getirebiliriz. Bunun için; resim editörünü kullanarak daha küçük ve daha hızlı yüklenebilecek bir resim oluşturulur. Kendisi için düşük çözünürlüklü resim oluşturulan resim seçilir. Properties denetçisinde Low Source metin kutusuna resmin konumu girilir ve enter tuşuna tıklanır. Seçim dreamweaver ekranında görülmez. Sayfayı tarayıcıda izlediğimizde bu etki izlenebilir (5).

**Rollover Image:**

Bir image rollover, bir resmin kaynağını başka bir resim dosyası ile değiştirmemizi sağlayan bir Java Script eylemidir. Bu şekilde imleci bir resmin üstüne getirdiğimizde başka bir resim belirir. Rollover image nesnesi, üç olayı gerçekleştiren basit bir davranışı ayarlar: Sayfa yüklenirken resimler önceden yüklenir; kullanıcının imleci belirlenen resmin üzerine geldiğinde farklı bir resim gösterilir; kullanıcının imleci resimden uzaklaştığında tekrar orijinal resim gösterilir. Bu iki resmin aynı boyda olması veya ikinci resmin birinci resmin şekline yakın olması gerekir. Rollover resmini ayarlamak için Insert menüsünden rollover image komutu seçilir. Ekrana gelen Insert Rollover Image iletişim kutusunda ilgili metin kutularına dosya adları yazılarak orijinal resmin ve rollover resminin kaynakları sağlanır (Şekil 4.9.). Resmi başka bir web sayfasına bağlamak için When Clicked, Go To URL metin kutusuna bu URL veya yerel siteden bir sayfa seçilir. Rollover Image objesini denemek için Java Script tanıyabilen bir browser da çalışmak gereklidir.

Preload Rollover Images seçeneği varsayılan durumda seçilidir. Bu buton işaretli olmadığı takdirde ikinci resim talep edildiğinde yüklenmesi için beklemek gerekir.

**Table:**

Bir tablonun eklenmesi için tablonun görünmesi istenen yere imleç konumlandırıldıktan sonra Insert menüsünden Table komutu seçilir. Ekrana gelen Insert Table iletişim kutusunda Rows (satırlar) ve Columns (sütunlar) seçilir (Şekil 4.10.). Tablonun, Width seçeneği ile genişliği seçilir. Tablo oluşturulurken ona bir genişlik atanmış olabilir. Ancak tablonun genişliği istediğimiz zaman ayarlanabilir. Bunun için; tüm tablo seçilerek properties denetçisinden W metin kutusunun sağındaki metin kutusundan pixels veya percent seçilir. W kutusuna genişlik girilir.

Genellikle hücrenin genişliğine sığdırmak üzere, tablo hücrelerindeki yazılar alt satıra atılır. Sözcük kaydırmayı (Wrap) kapattığımız takdirde, hücre yazıya uymak için genişler. Bunun için No Wrap seçeneğini uygulamak istediğimiz satır, sütun veya hücre seçilir. Daha sonra No Wrap seçeneği işaretlenir. Bu seçenek uygulandığında hücrelerin herhangi birinde yazı varsa, bu hücreler içlerindeki yazıya uyacak şekilde genişleyebilir.

Bir tabloyu Dreamweaver programına eklediğimiz zaman, varsayılan durumda bir kenar (border) adı verilen bir piksellik bir çizgi hücreleri ve tablonun kenarlarını çevreler. Ancak bu çevrenin kalınlığını değiştirebiliriz. Bunu ayarlamak için Properties Denetçisinde Border metin kutusuna bir sayı girilir. Bir tabloyu bir sayfa düzeni aracı olarak kullanırken, tablodaki öğelerin arasındaki boşluğu kontrol edebilmek önem kazanır.

Cell Spacing (hücre boşluğu), hücrelerin arasındaki boşluk miktarıdır. Bu, tablo kenarlarına benzer. Ancak tablo ile etrafı arasındaki boşluğu değil, hücreler arası boşluğu belirtir. Eğer sıfıra ayarlanmışsa tablo kenarları sayfa da görünmeyebilir.

Cell Pading (hücre dolgusu) ise, hücrelerin duvarları ve hücrenin içindeki içerik arasındaki boşluk miktarıdır. Bu özellikleri değiştirebilmek için tablo seçilir ve Cellspace ve Cellpading metin kutularına piksel cinsinden değerleri gireriz (5).

**Horizontal Rule: **

Bir horizontal rule, sayfada görünen yatay çizgidir. Bir dokümanın kısımları arasında net bir ayrımı göstermeyi sağlar. Bunu eklemek için Insert menüsünden horizontal rule seçeneği seçilir. Sayfanın genişliği boyunca, kendisinden önce ve sonra birer paragraf boşluğu bulunan bir yatay çizgi belirir. Çizgiyi değiştirmek için yatay çizgi seçilir ve üzerine çift tıklanarak properties denetçisinde horizontal rule özelliklerinin görünmesi sağlanır (5).

**Navigation Bar:**

Bir Dreamweaver Navigation Bar çubuğundaki bir düğme, dörde kadar farklı görünüşe sahip olabilir; Up (ilk), over (imleç düğmenin üzerine geldiğinde), down (kullanıcı düğmeye tıkladığında) ve over while down (kullanıcı düğme basılı iken imleci düğmenin üzerinden çektiğinde). Bir Navigation Bar çubuğu oluşturmak için tek bir resim grubuna ihtiyaç vardır. Ancak çubuktaki her düğmenin her durumu için ayrı bir resim dosyasının oluşturulması gerekir.

Navigation Bar çubuğu eklemek için Insert menüsünden navigation bar seçeneği seçilir. Ekrana gelen iletişim kutusunda (Şekil 4.11.) Up image metin kutusuna kullanmak istenilen resmin dosya adı girilir. Düğmenin diğer durumları için de bir resim dosyası seçilir. Sayfa yüklenirken bu düğmenin basılı olması gerekiyorsa Show “Down Image” Initially onay kutusu işaretlenir. Yüklenirken basılı olacak resmin yanına bir asteriks işareti belirir. When Clicked, Go To URL metin kutusuna, linkin URL’ si yazılır. Başka bir düğme eklemek için + düğmesine tıklanır. Dinamik olarak sunulan resimler kullanılmıyorsa, Preload Image onay kutusu işaretli bırakılır. Böylece sayfa yüklenirken Web tarayıcısı tüm düğme durumları için gereken tüm resimleri alabilir. Aksi halde kullanıcı, imleci bir düğme üzerine getirdiğinde resmin yüklenmesini bekler. Seçimler yapıldığında OK tuşuna tıklayarak iletişim kutusu kapatılır.

** **Butonlarımızı oluştururken Fireworks programında kestiğimi parça resimlerini Navigation Bar iletişim kutusunda tanımladığımız zaman, hareketli butonlarımızı elde etmiş oluruz (5).

**Layers: ******

Layer (katman) çok basit olarak yazı ve resimleri üst üste gelecek şekilde ayarlamak veya bunları birbirinin üzerine yerleştirmek için kullanılır. Sayfaya katman eklemek için Insert menüsünden katman (Layer) komutu seçilir. Bir katman eklendikten sonra properties denetçisinden özellikleri değiştirilebilir.

Katmanları oluştururken kullanılan dört etiket vardır. <div> ve <span> etiketleri marquee layer adı verilen bir katmanı oluşturur. <div> etiketi, mutlak konumlandırmayı kullanır. <div> etiketini bir paragraf kesmesi çevreler. Paragraf kesmeleri olmadan bir iç katman oluşturmak tercih edilirse, bu durumda izafi konumlandırmayı kullanan <span> etiketi kullanılır. Kullanılabilecek diğer etiketler olan <layer> ve <ilayer> Netscape etiketleridir.

Bir katmanın bir sayfadaki konumu, sayfanın sol üst köşesinden, katmanın kendisinin sol üst köşesine olan mesafe ile ölçülür. Properties denetçisinde, L metin kutusuna katmanın sol sayfa kenarından uzaklığı, T metin kutusuna katmanın üst sayfa kenarından uzaklığı girilir.

Bir katmana içerik eklemeden önce veya ekledikten sonra, bir katmanın yüksekliğini ve genişliğini değiştirebiliriz. Properties denetçisinde, W metin kutusuna katmanın genişliğini, H metin kutusuna katmanın yüksekliği girilir.

*Overflow * (taşma), içeriği katmanın sınırlarını aştığında katmanın davranışlarını belirler. Dışarı taşan içeriğin görünür veya gizli olması sağlanabilir. İçeriğin geri kalanına ulaşmayı sağlamak için kaydırma çubukları (scroll) kullanılabilir. Genelde *auto* seçeneği de kaydırma çubuklarını gösterir.

*Clip* (kırpma), katmanın kırpma alanını belirtir. Bu, katmanın içinde, içeriğin göründüğü alandır. Bir katmana 200x200 piksellik bir alan sağladıktan sonra, sadece 100x100 piksellik bir alanın görünmesine izin verilebilir. Bir kırpma alanını, dört ölçüden oluşan dikdörtgen şeklinde bir alan olarak ayarlanabilir.

*Visibility*, öğenin yüklendiğinde görünür olup olmayacağını belirler. Bir öğeyi visible veya hidden olarak bildirebilir veya özelliklerini ebeveyn öğeden miras (inherit) almasını sağlayabiliriz.

*Z- index*, üst üste binen öğelerin yığılma sırasını belirler. Z-index, X ve Y ile bir arada kullanıldığında bir sayfada bir katmanın konumunu üç boyulu olarak belirleyen üçüncü koordinattır. Bu sayı ne kadar büyükse, o öğeye o kadar fazla öncelik sağlanır. Z- index değeri 3 olan bir katman, Z-index değeri 1 ve 2 olan öğelerin üstünde görünür.

Katmanlarla ilgili ne güzel şeylerden biri, bir katmanı başka bir katmanın içine koyabilmek veya üst üste binen iki katman oluşturabilmektir. Bunun için tek yapılması gereken iki katmanı üst üste gelecek şekilde taşımaktır. İlk katman oluşturulur. Mevcut katmanın içine tıklayarak ikinci katman yerleştirilir (5).

**Form:**

Bir HTML formunun nasıl kullanılacağı, form elementinin Action niteliği ile ayarlanır. Action niteliğine genellikle form bilgilerini işleyecek olan bir programın URL’ si atanır. Bu URL de genellikle form sonuçlarını açacak olan bir CGI programcığını gösterir. Verilerin nasıl gönderileceği ise Method niteliği ile belirlenir. Post metodu büyük miktarda veri gönderilmesi gerektiği zamanlarda kullanılır. Form bilgileri URL’ den hemen sonra gönderilir. Get yönteminde çok fazla güvenlik yoktur. Form nesneleri:

**Text field:** İki tiptir. Tek satırlı ve çok satırlı.

**Button:** Formun bir şeyler yapabilmesini sağlar. Gönderme (submit), sıfırlama (reset) gibi...

**Check box:** Tek başına veya iki veya daha çok öğeden oluşan gruplar halinde kullanılır. Onay kutuları kullanıcını evet veya hayır cevaplarını belirtmesini sağlar.

**Radio button:** Her zaman iki veya daha çok öğeden oluşan gruplar halinde kullanılır. bunlar bir dizi seçenek arasında sadece birini seçmemize izin verirler. Radyoda bir düğmeye basıldığında diğer düğmeler dışarı çıkar..

**Listeler/menüler:** Kullanıcının uzun bir seçenek listesinden sayfa üzerinde çok fazla yer kaplamayacak şekilde seçim yapmasını sağlar (5).

** Frames:**

** **Sayfamızın kenarlarında Frame alanları oluşturularak Banner gibi sabit araçların yerleştirilmesi için kullanılır.

Insert menüsündeki diğer komutları gerek Properties Denetçisini gerekse diğer başka araçları kullanarak yapabiliriz. Özellikle Properties Denetçisi bize bu konuda çok fazla destek olacaktır (5).

**Modify Menüsü:**

**Page Properties:** Sayfa özellikleri (page properties), sayfadaki bir tek nesneye değil, tüm bir sayfaya uygulanan ayarları içerir. Görsel özellikler arasında sayfanın başlığı, bir zemin rengi veya resmi, metin ve linklerin renkleri, metin yazarken üst ve solda bırakmak istediğimiz boşluklar vardır. Ayrıca Tracing Image (kopya resim) ile sayfamıza bir resim koyabilir ve bu resmin parlaklık ayarını Image Transparency cetveli ile ayarlayabiliriz. Bu resim sayfamızın arka planında kalır, üzerine yazı veya herhangi bir şey yazabiliriz (Şekil 4.15.) (5).

**Selection Properties:** Document sayfasında, üzerinde bulunduğumuz objenin properties denetçisini (özelliklerini) gösterir. Hiçbir nesne seçili değilse, properties denetçisi metin özelliklerini gösterir (5).

**Quick Tag Editor:** Dreamweaver 3.0 versiyonundan sonra gelen en yenilikçi özelliktir. İmlecimizin yanıp söndüğü yerdeyken aşağıda gördüğünüz Tag editörü açılır ve içerisine dilediğimiz kodu girebiliriz. < ve > işaretlerinin arasına faremizi getirir ve üzerinde aşağı doğru gezdirirseniz, sağ tarafta bir Tag menüsü açılır. Kullanmak istediğimiz Tagı buradan seçebiliriz.

**Make Link:** Bu seçeneğimizi seçili bir öğe varken kullanırsak, karşımıza Browse penceresi gelir ve link vermek istediğimiz adresi seçerek, seçtiğimiz öğeyi link haline getirmiş oluruz. Link rengi, Page Properties te ayarladığımız renge dönüşür.

**Change Link:** Seçili olan öğemizdeki link adresini değiştirmemizi sağlar.

**Remove Link:** Seçili olan öğemizdeki linki kaldırmamızı sağlar.

**Open Linked Page:** Daha önce link vermiş olduğumuz sayfayı Dreamweaver programında açmamızı sağlar.

**Link Target:** Link verdiğimiz objenin, sahip olduğu linki nasıl bir sayfada açması gerektiğini belirlememize olanak tanır. \_blank, \_top gibi...

**Table:** Kullandığımız tablonun ayarlarını yapmamızı sağlar. Açılan pencereden;

**Select Table**: Tabloyu seçer.

**Merge Cells:** Seçilen hücreleri birleştirir.

**Split Cells:** İmlecin içinde bulunduğu hücreyi yatay veya dikey bölmemizi sağlar.

**Insert Row:** İmlecin bulunduğu hücrenin üstüne satır ekler.

**Insert Column:** İmlecin bulunduğu hücrenin soluna sütun ekler.

**Insert Rows or Columns:** İmlecin bulunduğu noktanın üstüne veya altına satır eklememizi sağlar. Veya imlecin bulunduğu noktanın sağına veya soluna sütun eklememizi sağlar.

**Delete Row:** Bir satır siler.

**Delete Column:** Bir sütun siler.

**Increase Row Span:** İmlecin bulunduğu hücrenin satır sayısını arttırır.

**Increase Column Span:** İmlecin bulunduğu hücrenin sütun sayısını arttırır.

**Decrease Row Span:** İmlecin bulunduğu hücrenin satır sayısını azaltır.

**Decrease Column Span:** İmlecin bulunduğu hücrenin sütun sayısını azaltır.

**Clear Cell Heights:** Tablomuzda, yükseklik olarak meydana gelmiş hücre boşluklarını siler.

**Clear Cell Widhts:** Tablomuzda, enine olarak meydana gelmiş hücre boşluklarını siler.

**Converts Widts to Pixels:** Tablomuzun ölçü birimini Piksele çevirir.

**Converts Widts to Percent:** Tablomuzun ölçü birimini %’ ye çevirir.

**Layers And Hotspots:**

**Align Left, Align Right, Align Top, Align Bottom:** Bu seçenekler birden fazla katmanı seçip ortalama ayarı yapmak istediğimiz zaman aktif hale gelir. Mesela, iki tane katmanı seçili hale getirip Align Left komutunu işletirsek ikisi de sol tarafta blok olur.

**Bring To Front:** Bu seçenekte iki tane Image Map ya da Sıcak Nokta ya da başka bir deyişle Hotspot kullandığımız zaman aktif hale gelir. Seçili olan Sıcak Noktayı yanında bulunan veya kesişen sıcak noktalara göre en üst konuma getirir.

**Send To Back:** Seçili olan sıcak noktayı yanında bulunan veya kesişen sıcak noktalara göre en alt konuma getirir.

**Make Same Width:** Bu seçenek iki veya daha fazla katmanı seçili hale getirdiğimiz zaman aktif hale gelir. Katmalarımız seçili halde iken bu komutu uygularsak, seçili olan katmanların genişliği aynı büyüklükte olur.

**Make Same Height:** İki veya daha fazla Layer seçili halde iken bu seçeneği uygularsak, seçili olan katmanlarımızın yüksekliği aynı boyutta olur.

**Frameset:** Bu menüye geldiğimiz zaman bir alt menü açılır. Bu alt menüdeki seçenekler sayfamızı Frame’ lere bölmemizi (Split Frame Left, Split Frame Right...) veya bölünmüşse Frame’ leri kaldırmamızı (Edit No Frames Content) sağlar.

**Layout Mode:** *Convert Tables to Layers*, tablo tabanlı sayfamızı layer tabanlı sayfaya dönüştürür. Yani tablomuzun her bir hücresi bir layer olacak şekilde hücre sayısı kadar layer oluşturur. *Convert Layers to Tables* ise tam tersini, yani layer tabanlı sayfamızdaki bütün Layer’ ları birleştirerek tablo tabanlı sayfaya dönüştürür. Convert Tables to Layers iletişim kutusu, katmanlı yeni sayfamızı oluşturmak ve izlemek için seçenekler sunar. Üst üste binmelere karşı otomatik koruma için *Prevent Layer Overlaps* onay kutusu işaretlenir. Sayfa açıldığında Layers denetçisinin açılmasını sağlamak için Show Layer Palette onay kutusu işaretlenir. Sayfa açıldığında ızgaranın görünmesi için *Show Grid* onay kutusu işaretlenir. *Snap To Grid* işaretli olduğunda sayfanın tüm katmanları ızgaraya kenetlenir.

**Text Menüsü:**

**Indent:** Seçili olan satıra paragraf boşluğu vermek için kullanılır

**Outdent:** Seçili olan satırda paragraf boşluğu varsa onu kaldırmayı sağlar.

**Format:** Bu açılır menüden yazacağımız metinin formatını seçeriz.

Default halde paragraf gelir. Altı başlık boyu veya düzeyi vardır. *Heading 1* en büyüğüdür, *Heading 6* ise genellikle gövde yazısından daha küçüktür*. Preformatted Text* ise başka bir programda biçimlendirdiğiniz ve biçimini korumasını istediğiniz yazıları önceden biçimlendirilmiş metin olarak eklemenize yarar (Şekil 4.20.)

**Align:**Yazımızı hizalamamızı sağlar

**Left:**Yazıyı sola blok yapar.

**Right:** Yazıyı sağa blok yapar.

**Center:** Yazıyı ortalar.

**List: **Sıralı ve sırasız listeler oluşturabiliriz

**Ordered List: **Yazılarımızın başına rakamlar koyabiliriz.

DreamWeaver

Flash

Photoshop gibi

**Definition List: **Liste öğeleri bir atlanarak terim veya tanım olacak şekilde biçimlendirilir.

**Font: **Bu açılır menüden Dreamweaver programında kullanabileceğimiz hazır font kombinasyonlarını seçebiliriz. Tarayıcı, önerilen ilk fontun yüklü olup olmadığını kontrol eder, sonra ikinciyi kontrol eder bu işlem devam eder. Tavsiye edilen fontların hiçbiri yoksa, yazı kullanıcının varsayılan tarayıcı fontuyla gösterilir. Bir font kombinasyonuna istediğimiz sayıda font ekleyebilir hatta kendimiz bir font kombinasyonu tanımlayabiliriz. ** **

**Bir Font Kombinasyonu Tanımlamak: **Font menüsünden Edit Font List’ i seçeriz. Font List iletişim kutusu açılır (Şekil 4.21.)

Önce sağ taraftan eklemek istediğimiz fontları seçerek butonuna tıklıyor ve seçtiğimiz fontları sol tarafa, seçilmiş fontlar penceresine taşıyoruz. Seçme işlemimiz bittikten sonra yukarıda gördüğünüz işaretine tıklayarak Font List' imize alıyoruz. Eğer bu işarete tıklamazsak seçtiğimiz fontlar Font List' imize alınmayacaktır. Yukarı ve Aşağı Ok yön tuşlarıyla, fontları istediğiniz sırayla dizebilirsiniz.

**Style: **Kelime işlemci programınızda veya sayfa hazırlama aracınızda **koyu,** *italik* veya altı çizili gibi stilleri kullanıyor olabilirsiniz. Bu ve diğer stilleri Style listesinden seçip, yazının kısımlarına vurgu veya görsel kontrast kazandırabilirsiniz.

**HTML Styles:** Web ortamında kullanılan bazı standartlar vardır. Bunları listeden seçerek kullanabilirsiniz.

**CSS Styles:** Cascading Style Sheets ile web sayfası şablonlarında, yazı stillerinde, renklerde ve yazının formatında kontrolü daha rahat sağlayabilirsiniz. Çünkü Cascading Style Sheets ile bir sayfada yada tüm sitede kullanacağınız fontu, stili, kontrol boşluklarını vs. açıkça baştan belirtmiş olursunuz.

**Yeni Bir Stil Yaratmak: **CSS Styles seçeneğinden** **Edit Style Sheet’ i seçeriz. Edit Style Sheet iletişim kutusu açılır (Şekil 4.22.)

Bu iletişim kutusundaki **New **seçeneğini tıklarız ve** New Style **iletişim kutusu açılır (Şekil 4.23.). Burada **Name** bölümüne bir isim yazarız. Bu bizim yeni stilimizin ismi olacaktır.

New Style iletişim kutusundaki** OK **seçeneğini tıkladığımızda Style Definition iletişim kutusu açılır. Burada oluşturmak istediğimiz stilin özelliklerini belirleyen birçok seçenek bulunur (Yazı fontu, büyüklüğü, arka plan rengi, kelime aralıkları, girintiler vs.).

Bu seçimleri yapıp OK tuşuna tıkladığımızda artık CSS Styles seçeneğinde görünen ** ***Yeni*** **isimli bir stilimiz var (Şekil 4.24.).

**Size:** Burada metinde kullandığınız fontun büyüklüğünü** **seçebilirsiniz. Yazının mutlak ölçeği en küçük boy olan 1 ile başlar ve maksimum font boyu olan 7’ ye kadar gider.

**Size Increase: **Font boyunu arttırır.

**Size Decrease: **Font boyunu azaltır.

**Color: **Bu seçenekle seçili olan metnin rengini belirleyebilirsiniz.

**Check Spelling: **Yazım denetimi yapmayı sağlayan seçenektir. Yazım denetimine başlandığında Dreamweaver ilk şüpheli kelimeyi bulur; bu *Word Not Found in Dictionary* metin kutusunda görülen kelimedir.

Burada çok sayıda seçeneğiniz vardır. Yazım denetiminin sorguladığı her kelime için bu tercihlerden birini yapmanız gerekir:

Kelime doğru yazılmışsa *Ignore *(dikkate alma) * *seçeneğine tıklayın.

Kelime doğru yazılmışsa ve sayfanızda başka yerlerde de bulunduğunu düşünüyorsanız**, ***Ignore All* (tümünü dikkate alma) seçeneğine tıklayın.

Kelime yanlış yazılmışsa ve doğru yazımı *Suggestions* (öneriler) liste kutusunda görülüyorsa, doğru kelimenin üzerine tıklayın ve sonra *Change* seçeneğine tıklayın.

Kelimenin birden fazla yerde yanlış yazıldığını düşünüyorsanız,** ***Suggestions*** **liste kutusundan doğru kelimenin üzerine tıklayın, sonra *Change All*** **(tümünü değiştir) seçeneğinin üzerine tıklayın.

*Change To* metin kutusuna doğru kelimeyi yazdıktan sonra *Change* seçeneğine tıklayarak kelimeyi elle de düzeltebilirsiniz (5).

**Command Menüsü:**

**Start Recording: **Bu komutu seçip ekrana bir obje veya yazı eklediğimizde objeyi kaydeder.

**Play Recorded Command: **Bir önceki komut ile kaydettiğimiz objeyi veya yazıyı çoğaltmamızı sağlar. ** **

**Edit Command List: **Komutların isimlerini değiştirip kendimizin verdiği isimler ile kullanmamızı sağlar.

**Get More Commands: **Internet’ e bağlanarak yeni komutlar almamızı sağlar.

**Clean Up HTML: **Gereksiz HTML kodlarını temizler.** **

Dreamweaver programının otomatik temizlik işlemlerinin yanında, istediğiniz anda daha hassas kod temizleme işlemleri yapabiliriz.

Commands> Clean Up HTML komutunu seçin. Clean Up HTML iletişim kutusu açılır (Şekil 4.27.)

Programın kaldırmanıza izin verdiği kodlar:

Empty Tags (boş etiketler).

Redundant Nested Tags (yuvarlanmış gereksiz etiketler)

Non-Dreamweaver HTML Comments (Dreamweaver tarafından eklenmemiş açıklamalar)

Specific Tags (belirtilen etiketler)

Kaldırılmasını istediğiniz gereksiz kodların yanındaki kutuyu işaretleyin. Gereksiz font etiketlerinin tümünü bir tek etiket haline getirmek için *Combine Nested <font> Tags When Possible* onay kutusunu işaretleyin. Programın yakaladığı kendi hatalarınızı görmek için, *Show Log On Completion* onay kutusunu işaretleyin.OK tuşuna tıklayın. Dreamweaver sayfanızda seçtiğiniz hataları tarar, kaydın gösterilmesini seçtiyseniz düzelttiği şeylerin listesini gösterir.

**Clean Up Word HTML: **Web sayfalarımızda kullandığımız metinleri düzenlemek için Dreamweaver programını kullanabiliriz. Fakat program HTML kodları mantığına göre çalıştığı için yazıları istediğimiz düzene sokamayız. Satırlar arası boşluğu ayarlamak için bile, kullanmamız gereken bir çok kod vardır. Bu yüzden bir çok kullanıcı metinleri Office programında düzenleyip, web sayfası formatında kaydedip kullanmayı tercih eder. Bu yöntemin de bazı sakıncaları vardır. Yazıları düzenlediğimiz program, dosyayı kaydederken kendine göre bazı kodlar ilave eder. Bu kodları temizlemediğimiz taktirde, oluşturduğumuz dosyayı Office programı kurulu olmayan bir bilgisayarda görmemiz mümkün değildir. Web sayfamızı Internet’ e gönderdiğimizi düşünürsek, milyonlarca bilgisayar arasından böyle bir tanesinin çıkması mümkündür. Dreamweaver programında bu Word kodlarını temizleyerek sayfamızı sorunsuz hale getirir. *Clean Up Word HTML * komutunu seçtiğimizde karşımıza gelen pencereden (Şekil 4.28.) gerekli ayarları yaparak Word kodlarını temizleyebiliriz. Pencerelerdeki seçenekler:

**Remove all Word specific markup:** Word’ e özgü ve standart HTML etiketi olmayan tüm etiketleri kaldırır.

**Clean up CSS:** *Cascading Style Sheets* kullanılarak yapılan değişikleri kaldırır.

**Clean up <font> tags:** Aşırı metin biçimlendirmelerini birleştirir.

**Fix Invalidly Nested Tags:** Standart olmayan bir sırayla yuvarlanmış etiketleri düzeltir.

**Set background color:** Zemin rengini ayarlar.

**Apply Source Formating: **Satır başları, satır sonları ve küçük büyük harf durumları üzerinde değişiklik yapar.

**Show log on completion: **Yapılan değişikleri gösterir.

**Add / Remove Netscape Resize Fix: **Netscape Navigator aracının bazı versiyonları hata içerir. Bu, sayfayı tam ekran yapmamız veya küçültmemiz esnasında sorun oluşturur. Bu komut ile Web sayfamıza bir Java Script kodu ekleyerek sorunu gidermiş oluruz.

**Optimizme Image in Fireworks: **Seçili bir objeyi Fireworks programında düzenlemek için kullanılır.

**Create Web Photo Album: **Web sayfamıza fotoğraf albümü eklememizi sağlar. Fireworks programının 3.0 versiyonu kurulu olmalıdır.

**Formating Table: **Oluşturduğumuz tabloya efektler, yeni özellikler eklemek için kullanılır.

**Sort Table: **Tabloya girdiğimiz yazıları alfabetik veya sayısal olarak sıralamamızı sağlar. Bunun için; tabloyu tıklayarak*, Commands* > *Sort Table* (tabloyu sırala) seçilir. *Sort Table* iletişim kutusu açılır (Şekil 4.29.). *Sort By* (şuna göre sırala) çekme menüsünden, ilk kez kendisine göre sıralama yapılacak sütunu (numarasıyla) seçeriz. *Order* (sıralama) çekme menüsündeki komutlardan *Alphabetically,* alfabetik olarak, *Numerically* sayısal olarak sıralama yapmamızı sağlar. Sonraki çekme menüden *Ascending* A’ dan Z’ ye veya 1’ den 9’ a artan sıralama yapmamızı, *Descending* ise bunun tersi A’ dan Z’ ye veya 1’ den 9’ a azalan bir sıralama yapmamızı sağlar. İlk satırı sıralamaya dahil etmek için, *Sort Includes First Row* onay kutusu işaretlenmelidir. Ham biçimlerin sıralamayla birlikte hareket etmesi için *Keep TR Attributes with Sorted Row* onay kutusunu işaretlenmelidir. OK tuşuna tıklayarak Sort Table iletişim kutusunu kapatıldığında, tablo, belirttiğiniz kriterlere göre sıralanmış olur (5).

** Site Menüsü:**

Dreamweaver programında en çok kullanılan menü Site menüsüdür. Bunun için menüdeki komutları kısaca açıklayıp ayrıntılarını ana başlıklar altında açıklanacaktır.

**Site Files: **Web sitesinin dosyaların görmemizi sağlar.

**Site Map: **Web sitesinin dosyaları arasındaki bağlantıları, linkleri gösterir.

**New Site: **Yeni site oluşturmamızı sağlar.

**Open Site: **Kayıtlı olan siteyi açmamızı sağlar.

**Define Sites: **Tanımlı olan, üzerine çalışabileceğimiz siteleri göstererek, istediğimizi seçmemizi sağlar.

**Get: **Diğer sitelerden dosya almamızı sağlar.

**Check Out: **Diğer sitelere gönderdiğimiz dosyaları kontrol eder.

**Put: **Dış sitelere dosyalar göndermemizi sağlar.

**Check In: **Dış sitelerden aldığımız dosyaları kontrol eder.

**Check Links Sitewide: **Web sitesindeki linkleri kontrol ederek, sorunlu linkleri gösterir.

**Locate in Local Site:** Çalıştığımı sayfanın o andaki yerini, yerel sitede gösterir.

**Locate in Remote Site:** Çalıştığımı sayfanın o andaki yerini, uzak sitede gösterir (5).

**Window Menüsü:**

Bu menü Dreamweaver programındaki bütün panelleri yönetebilmenizi sağlayan menüdür. İçinde tasarım esnasında gerekli olacak bütün paneller yer alır. Kullanıcı istediği paneli buradan açabilir, açık olanları da kapatabilir. Menü beş parçadan oluşmuştur. İlk parça içinde programda iki elimiz diye tanımladığımız *Objects* ve *Properties* panellerini açmak ya da kapamak için kullanabileceğimiz komutlar yer alır. İlgili satırların başında tik işaretinin olması ilgili panellerin o an aktif durumda olduklarını gösterir. Şu halde bunlar programın tasarım ekranından görülmelidir. Launcher panelini açıp kapatan komut da birinci parçada yer alır. İkinci parçada Site menüsü içinde de tanıttığımız siteye ait dosya ve/veya dizinleri gösteren Site Files ve oluşturduğumuz sayfaların ağaç yapısını gösteren Site Map yer alır.

Ayrıca istediğimiz zaman açıp kapayabileceğimiz diğer panel komutları yer alır. Bunlar kullanıcının tercihine göre açılıp kapanabilecek pencerelerdir. Üçüncü parçada *Arrange Floating Palettes* komutunu kullanarak, o an açık olan panelleri ekrana döşeyebilir ya da *Hide Floating Palettes* komutunu kullanarak gizleyebiliriz. En son parçada ise o an açık olan sayfaların adları listelenir. Kullanıcı bu kısmı kullanarak sayfalar arasında dolaşabilir.

Bu paneller çok kullanıldıkları için içerdikleri komutları tanıtmamız gerekmektedir. Bunun için ilk önce Launcher panelinden ve komutlarından bahseidlecektir (Şekil 4.31.).

**Show Site:** Üzerinde çalıştığımız siteye ait tüm dosya ve dizinleri görmek için kullanırız.

**Library:** Çalışmalarda kullanmak için kendi kütüphanemizi oluşturmamızı sağlayan Library penceresini açar (Şekil 4.33.)

**Show HTML Style:** Yeni stiller oluşturabileceğimiz ve bu stilleri sayfalarımıza uygulayabilme imkanı sağlayacak olan HTML Style penceresini açar.

**Show CSS Style:** Sayfalarımızda kullanmak için CSS' ler tanımlayabileceğimiz, bunlar üzerinde istediğimiz işlemleri yapabilmemizi sağlayan CSS Style penceresin açar (Şekil 4.35.).

**Behaviors:** Sayfalarımızı interaktif hale getirebiliriz. Browser ile ilgili sorunları çözebilir, Java Script’ ler ekleyebiliriz v.b.

**Show History:** Tasarım esnasında sürekli tekrar ettiğimiz işlemleri History penceresini (Şekil 4.36.) kullanarak çabuklaştırabilir, bunları tekrar tekrar kullanabiliriz.

**HTML Source:** HTML kodları yazarak, sayfayı düzenlememize yardımcı olan HTML Source penceresini açar (Şekil 4.37.). O an için HTML kodlarının bulunduğu yere gitmek istediğimizde bu pencereyi kullanacağız. İmlecimiz tasarım ekranında nerede duruyorsa oraya gitmemizi ve HTML kodlarını düzenlememizi sağlar (5).

** **Window menüsünden Properties komutunu seçtiğimizde, daha önce tanıttığımız Properties denetçisi açılır. Bu panel ile yaptığımız işlemlerin düzenleyebilir, boyutları ayarlayabilir, linkler verebilir ve daha bir çok işlem yapabiliriz. Kısacası Properties denetçisi tasarımın her aşamasında kullanılabilir (Şekil 4.38.) (5).

** **Window menüsünden Objects komutunu seçtiğimizde karşımızda Common, Character, Forms, Head, Invisibles ve Special olmak üzere altı adet kontrol paneli açar (Şekil 4.39.).

**Common: **Bu paneldeki komutlar ile sayfalarımıza Insert menüsü ile ekleyebileceğimiz objeleri ekleyebiliriz. Image, Table, Navigation Bar gibi.

**Character:** Sayfalarınızda ekstra karakterler eklemek için kullanacağız.

**Forms:** Formlar oluşturmak istediğinizde kullanacağız.

**Head: **Arama motorlarına kayıt olabilmek için sayfalarımıza eklemek durumunda olduğumuz Meta taglarını oluşturabilmek için kullanacağız.

**Special:** Sayfalarımıza anchor, script veya açıklamalar eklemek için kullanabileceğimiz Invisibles, Applet, Plug-In veya ActiveX' ler eklemek için kullanacağız (5).

**4.2. WEB SITESININ OLUŞTURULMASI**

Menüler ve kontrol panellerini tanıttıktan sonra sitenin oluşturulması için gerekli işlemleri anlatacağız. Sitenin sayfaları ve aralarındaki bağlantıları kontrol etmek için gerekli panellere Site menüsünün altındaki komutlar ile ulaşabiliriz.

**4.2.1. Site Penceresi Hakkında**

Dreamweaver programının Site penceresi bir dosya yönetimi aracıdır, aynı zamanda da sitenizi on line hale getirmenize yardımcı olan eksiksiz bir FTP istemcisidir.

Site, penceresinde, bilgisayarınızdaki veya yerel ağınızdaki bir klasörü veya dizini yerel site olarak atarsınız. Bu klasör sitenin kök klasörü haline gelir ve Dreamweaver, resimlerin konumları da dahil olmak üzere izafi bağları kodlamak için onu kullanır. İzafi bağlar, aynı web sitesinin içindeki sayfaları işaret eden verimli kısa yollardır. Dosyaların yerel ve uzak sitelerde yönetimi Site penceresinde gerçekleştirilir.

Site penceresini açmak için menü çubuğundan Window > Site Files komutunu seçip veya F5 tuşuna basarak Site penceresini açabiliriz (Şekil 4.40.). Site penceresini ilk kez gördüğünüzde boş olacaktır. Yerel site üzerinde çalışmaya başlayabilmeniz için, önce bilgisayarınızda bir yerel site kurmanız gerekir.

**4.2.1.1. Yerel Bir Site Kurulması**

** **Yerel bir siteyi, mevcut bir Web sitesinin içeriğine dayanarak kurabilir veya daha önce hiç var olmamış bir yerel site kurabilirsiniz. Seçiminiz bunların hangisi olursa olsun, yerel siteniz için bir kök dizin seçmeniz gerekir.

**4.2.1.2. Yerel Bir Sitenin Kök Dizinin Atamak**

Menü çubuğundan Site > Define Sites veya Site penceresinin Site çekme menüsünden Define Sites komutunu seçebiliriz. Her iki şekilde de Define Sites iletişim kutusu açılır (Şekil 4.41.).

New butonuna tıklayarak Site Definition (site tanımı) iletişim kutusunu açın (Şekil 4.42.). *Local Root Folder* metin kutusuna yerel sitenin kök klasörünün dizin adresinin girin veya klasör ikonuna tıklayın. *Choose Local Folder* (yerel klasörü seç) iletişim kutusu açılır. Mevcut bir klasörü seçebilir veya yeni bir klasör yaratabilirsiniz.

Mevcut bir klasörü seçmek için klasör ikonuna tıklayın, *Open* butonuna tıklayın ve seçiminizi yaptıktan sonra, *Select* butonuna tıklayarak *Choose Local Folder* iletişim kutusunu kapatarak *Site Definition* penceresine geri dönün.

Yeni bir klasör yaratmak için, *New Folder *(yeni klasör) butonuna tıklayın ve yeni klasör için bir isim girin. Oluşturduğumuz klasör ikonuna çift tıklayarak seçin ve *Site Definition* penceresine geri dönün.

*Site Name* iletişim kutusunda bir site ismi girin ve OK butonuna tıklayarak iletişim kutusunu kapatın.

**Cache nedir?**

Dreamweaver, yerel siteleriniz için cache (önbellek) adı verilen bir indeks yaratabilir, bu sayede metin ararken veya değiştirirken daha hızlı araştırmalar yapabilirsiniz. Bu önbellek, yerel bir dosyayı başka bir dosyaya ne zaman bağladığınızı da hatırlar. Bu sayede, bir dosyayı taşıdığınızda ya da ismini değiştirdiğinizde, bir bağı tüm site içinde güncelleyebilirsiniz (5).

**4.2.2. Bağların İdaresi**

Dreamweaver programı sitelerdeki bağları izlemenize, kontrol etmenize ve güncellemenize yardımcı olur.

**4.2.2.1. Bir Yerel Sitedeki Bağları Kontrol Etmek**

Menü çubuğundan Site > Open Side komutu ile site adını seçin. Site penceresi açılır ve seçtiğiniz sitenin içeriğini gösterir. Site penceresinin menü çubuğundan Site > *Check Links Sitewide* (sitede bağları kontrol et) komutunu seçin. *Link Checker* iletişim kutusu açılır (Şekil 4.43.) ve yerel sitenizi taramaya başlar. Sitenizin uzunluğuna bağlı olarak, bu iş birkaç saniye veya daha uzun sürebilir. Tamamlandığında, özette kaç tane dosyanın, bağın kontrol edildiğini, kaç bağın geçersiz olduğunu ve kaç tane harici bağın bulunduğunu göreceksiniz. Link Checker ayrıca boşta kalan (Orphaned) dosyaları da sayar. Bunlar yerel sitenizde bulunan ancak başka hiçbir sayfadan bağ gelmeyen sayfalardır. Boşta kalan dosyaların listesini görmek için *Show* menüsünden *Orphaned Files* komutunu seçin. Bir klasörün içindeki bağları veya birkaç dosyayı da kontrol edebilirsiniz. Site penceresinde kontrol etmek istediğiniz dosya grubunu seçin. Sonra Site penceresinin menü çubuğundan File > *Check Links* komutunu seçin.

Geçersiz bağları düzeltmek için *Link Checker* komutunu bir sayfa, bir sayfa grubu veya bir yerel site üzerinde kullanın. *Link Checker* iletişim kutusunda geçersiz bir bağın URL adresine tıklayın. Bir dosya düğmesi belirir. Eski URL adresi üzerine doğru URL adresini (harici veya izafi) yazın veya dosya düğmesine tıklayarak *Select HTML File* iletişim kutusunu açın. Yerel sitenizden doğru dosyayı seçin ve Select (seç) butona tıklayın. Bu bağ birden fazla yerde geçiyorsa, Dreamweaver geçtiği her yeri düzeltmeyi isteyip istemediğinizi sorar. *Yes *butonuna tıklayarak bu URL adresine gönderen tüm bağları düzeltebilir veya *No* butonuna tıklayarak bir tek bağı değiştirebilirsiniz (5).

**4.2.3. Web Sitelerinin Yönetimi**

Bir sayfayı (veya tüm bir siteyi) herkesin görebilmesi için Web ortamına yüklemeye hazır olduğunuzda, Dreamweaver programından çıkmanız gerekmez. Site penceresi, eksiksiz ve kullanışlı bir FTP istemcisidir. Yani, dosyaların Web ortamına konması veya yüklenmesi için kullanabileceğiniz yerleşik bir araçtır. Dreamweaver programını kullanarak Web ortamından dosya almanız veya göndermeniz de mümkündür.

Yerel sitedeki adresler ve Web sunucunuzun adı da dahil olmak üzere site bilgilerinizi belirledikten sonra, bir uzak sunucuya bağlanabilirsiniz. Uzak sunucu, Web sitenizin yaşayacağı yerdir. Bilgisayarınız ve uzak sunucu arasında dosyalarınızı aktarırken, Dreamweaver sitenin iki versiyonundaki dizin yapısının aynı olmasını sağlar. Dreamweaver, otomatik güncellemeler yapmaz, ancak bu konumlardan birindeki bir dosyayı siler ya da dosya eklerseniz, değişen bağlan otomatik olarak tarayabilir (5).

**4.2.3.1. Uzak Site Bilgilerini Ayarlamak**

Site penceresinin menü çubuğundan veya Document penceresinin menü çubuğundan Site > Define Sites komutunu seçin. *Define Sites* (site tanımla) iletişim kutusu açılır. Ayarlamak istediğiniz yerel siteyi seçin ve Edit butonuna tıklayın. *Site Definition* (site tanımı) iletişim kutusu açılır (Şekil 4.44.). Sol taraftaki *Category* listesinden *Web Server Info* seçeneğine tıklayın. İletişim kutusunun bu paneli öne gelir. Çekme menüden FTP seçeneğini aktif hale getirin. İletişim kutusunda FTP bilgileri görünür.

*FTP Host* metin kutusuna Web sunucunuzun alfanümerik adresini girin (örneğin, ftp.site.com veya www.site.com). *Host Directory* metin kutusuna, sitenin başlangıç kök dizinini girin (örneğin, public\_html veya html/public/personal). *Login* metin kutusuna, ftp veya www hesabınız için kullanıcı adını girin. *Password* metin kutusuna ftp veya www hesabınızın parolasını girin. Kullanıcı adını ve parolayı kaydetmek için, *Save* onay kutusunu işaretleyin. Yerel ve uzak site bilgilerinin her ikisini doldurduğunuzda, OK butonuna tıklayarak Site Definition iletişim kutusunu kapatın, yerel sitenizi gösteren Site penceresine geri döneceksiniz (5).

**4.2.4. Uzak Siteye Bağlanmak ve Bağlantıyı Kesmek**

Mevcut uzak sitelerden birine dosya yüklemek veya ondan dosya indirmek için, önce ona bağlanmanız gerekir.

**4.2.4.1. Uzak Siteye Bağlanmak**

Bir uzak site profili ayarlayın. Site penceresinde Site çekme menüsünden bağlanmak istediğiniz siteyi seçin. *Connect* (bağlan) düğmesine tıklayın. Dreamweaver, uzak Web sunucusuna bağlanmak için ona verdiğiniz adresi ve diğer bilgileri kullanır. Dreamweaver Web sunucusuyla irtibat kurarken, *Connecting to* \[sunucu adı\] başlıklı bir iletişim kutusu açılır. Uzak sunucuya başarıyla bağlandığınızda, Connect (bağlan) düğmesi *Disconnect *(bağlantıyı kes) düğmesine dönüşür ve uzak dosyaların listesi belirir (5).

**4.2.4.2. Uzak Site Bağlantısını Kesmek**

Site penceresinde durum çubuğuna bakarak hiçbir dosya aktarımının yapılmadığından emin olun. Pencerede bir işlem yapılmıyorsa, durum çubuğunda şu yazıyı görürsünüz: *Connected to \[site adı\]*. *Disconnect* düğmesine tıklayın. Durum çubuğunda *Disconnected* yazısı görünür ve *Disconnect* düğmesi tekrar *Connect* düğmesine dönüşür. 30 dakika boyunca hiçbir dosya aktarımı yapmazsanız, Dreamweaver sizin için bağlantıyı keser (5).

**4.2.4.3. Almak ve Koymak**

Artık yerel ve uzak sitelerinizden dosya çekmeye (Get) ve onlara dosya yüklemeye (Put) hazırsınız. Çekeceğiniz dosyalar, uzak sitede yerel sitede henüz var olmayan bir dizinde duruyorsa, o dizin yerel sitede de yaratılır, bunun tersi de olabilir (5).

**4.2.4.4. Uzak Siteden Dosya Çekmek**

Önceki sayfada anlatıldığı şekilde uzak siteye bağlanın. Site penceresinde, çekmek istediğiniz dosya veya dosyaları, klasör veya klasörleri seçin. *Get* butonuna tıklayın. *Dependent Files* (bağımlı dosyalar) iletişim kutusu açılır Yes veya No butonuna tıklayın. Dosyalar alınmaya başlandığında, aktarımın ilerleyişi Site penceresinin durum çubuğunda görünür (5).

**4.2.4.5. Uzak Siteye Dosyaları Yüklemek**

Uzak siteye bağlanın. Site penceresinde, karşıya yüklemek istediğiniz dosyaları veya klasörleri seçin. Put butonuna tıklayın. *Dependent Files* iletişim kutusu açılır. Yes veya No butonuna tıklayın. Dosyalar uzak sunucuya gönderilmeye başlandığında, aktarımın ilerleyişini penceresinin durum çubuğunda görünür (5).

**4.2.5. Senkronizasyon**

Dreamweaver programı bir dizindeki veya tüm sitedeki daha yeni olan dosyaları otomatik olarak seçebilir. Bu sayede, bir aktarım sırasında herhangi bir dosyanın son sürümünün üzerine yazmadığınızdan emin olabilirsiniz (5).

**4.2.5.1. Yeni Dosyaları Seçmek**

Doğru yerel siteyi seçin ve onunla ilişkili uzak siteye bağlanın. Site penceresinin menü çubuğundan, yeni dosyaların hangi panelde seçilmesini istediğinize bağlı olarak, Edit > *Select Newer Local* (yeni yerel dosyaları seç) komutunu veya Edit > *Select Newer Remote* (yeni uzak dosyalan seç) komutunu seçin. Dreamweaver, yerel ve uzak dosyaların tarihlerini karşılaştırır. Karşılaştırma tamamlandığında, diğer sitedekine göre daha yeni olan dosyalar seçilir. Kontrol ettikten sonra, seçilen dosyaları alabilir, karşıya yükleyebilir veya senkronize edebilirsiniz. *Synchronize* (senkronize et) özelliği, daha yeni olan dosyaları seçer ve sonra onları yığın halinde alır veya karşıya yükler. Bu işlemden önce bir yedek almayı düşünebilirsiniz (5).

**4.2.5.2. Dosyaları Senkronize Etmek**

Site penceresinin menü çubuğundan Synchronize komutunu seçin. *Synchronize Files* (dosyaları senkronize et) iletişim kutusu açılır. *Synchronize* çekme menüsünden, tüm siteyi ya da sadece seçiminizi senkronize etmeyi seçin. *Direction *çekme menüsünden *Get* (al), *Put* (karşıya yükle) veya *Both* (ikisi) seçeneklerinden birini seçin. OK butonuna tıklayarak senkronizasyona hazırlanın. Site iletişim kutusu açılır. Dahil edilmesini istemediğiniz dosyaların yanından işareti kaldırın. Hazır olduğunuzda OK butonunu tıklayın. Belirtilen daha yeni olan dosyalar yüklenir veya alınır ve aktarımların ilerleyişi Site penceresinin durum çubuğunda görülür. *Delete remote files not on local drive* (yerel sürücüde olmayan uzak dosyaları sil) onay kutusunu işaretlememenizi şiddetle tavsiye ederim. Aksi halde, dosyaları alırken, yerel sitenizde bulunan ancak uzak sitede bulunmayan dosyalar bilgisayarınızdan silinir. Dosyaları karşıya yüklerken, uzak sitede bulunan ancak yerel sitenizde bulunmayan dosyalar da Web sunucusundan silinir. *Synchronize Files* iletişim kutusunda görünmese de, bu işlem çift yönlü çalışır (5).

**4.2.6. Check In ve Check Out**

Bir site üzerinde çok sayıda kişi çalışıyorsa, kimin hangi dosyayı nereye, ne zaman koyduğunu bilmeniz faydalı olacaktır. Site üzerinde sadece bir veya iki kişi çalışıyorsa, cevabı zaten bilirsiniz.

Bir dosyada Check Out işlemini yapmanız, o dosyayı yeşil bir onay işaretiyle işaretler, o dosyaya sizin kullanıcı adınızı atar ve dosyayı Dreamweaver programının Site penceresinde kilitler. Dreamweaver kullanan diğer ekip üyeleri, kilidi dosyaların (yani başka bir kişi tarafından Check Out uygulanmış dosyaların) üzerine yazamazlar. Ancak başka FTP istemcileri bu dosyaların üstüne yazabilir. Bu, üretim gruplarında kullanılan Unix tabanlı bir araç olan CVS checkout aracı daha basit, kullanıcı tabanlı ve daha az güvenli bir benzeridir.

Diğer insanların Check Out ile işaretlediği dosyalar, Site penceresinde kırmızı bir işaretle görünür ve o kişinin adı *Checked Out By* sütununda görünür (5).

**4.2.6.1. Check In ve Check Out Kullanımını Etkinleştirmek**

Check In ve Check Out özelliklerini kullanabilmek için, sitenin tanımında bu seçeneği etkinleştirmeniz gerekir. Site penceresinin menü çubuğundan Site > Define Sites komutunu seçin. *Define Sites* (site tanımla) iletişim kutusu açılır. Check In ve Check Out seçeneklerini ayarlamak istediğiniz siteyi seçin ve Edit butonuna tıklayın. *Site Definition* (site tanımı) iletişim kutusu açılır (Şekil 4.45.). Sol taraftaki kategori kısmından *Check In/Out kategorisini* seçin. Bu panel iletişim kutusunun ön tarafına gelir. Check In ve Check Out işlemini etkinleştirmek için *Enable* onay kutusuna tıklayın. Document penceresinde açtığınız dokümanların Check Out durumunda görünmesi için, *Check Out Files When Opening* onay kutusunu işaretleyin. Check Out Name metin kutusuna, diğer kullanıcıların Check Out uyguladığınız dosyaların yanında görmesini istediğiniz ismi yazın. Bu, tam adınız veya kullanıcı adınız (e-posta adresiniz) olabilir. OK butonuna tıklayın. Artık uzak sunucudan aldığınız her dosya Check Out durumunda görünür ve sunucuya koyduğunuz her dosya Check In durumunda gösterilir (5).

**4.2.6.2. Bir Uzak Siteye Check Out Uygulamak **

Site penceresinde istediğiniz siteye bağlanın. Check Out butonuna tıklayın. *Dependent Files* (bağımlı dosyalar) iletişim kutusunu cevaplayın. Dosya yerel siteye kopyalanır, ancak açılmaz. Dosyayı görebilmek için yerel siteyi (veya yeni yarattıysanız klasörünü) tazelemeniz gerekebilir.

Dosyalara Check Out uyguladıktan sonra, Site penceresinin menü çubuğundan File > Undo Check Out komutunu (Site>Site Files View>Undo Check Out) seçerek bu işlemi geri alabilirsiniz (5).

**4.2.6.3. Dosyalara Check In Uygulamak**

Site penceresinde istediğiniz siteye bağlanın. Yerel sitede Check In uygulamak istediğiniz dosyalara tıklayarak seçin. Site penceresinden Site > Check In komutunu seçin. Sadece Check In düğmesine de tıklayabilirsiniz. Açılırsa, *Dependent Files* (bağımlı dosyalar) uyarısını ve *Overwrite* (üstüne yazma) uyarılarını cevaplayın. Dosya, yerel sitede bir kilit sembolü ile gösterilir. Uzak sunucudan Check Out durumu ve LCK dosyası kaldırılır, isminiz *Checked Out By* sütunundan kaldırılır. Bir dosyaya Check Out uygulandığında, o dosya seçildiğinde Check Out sütununda bir onay işareti görünür. Bir onay işareti görünmüyorsa, bu sütuna tıklayarak bir dosyaya Check Out uygulayabilirsiniz. Check In uygulanmış dosyaların salt-okunur özelliğini kaldırmak için, Site penceresinin menü çubuğundan File > *Turn Off Read Only* komutunu seçin (5).

**4.2.7. Site Haritasının Kullanılması**

Dreamweaver, dosyaların ilişkilerini görmek için kullanabileceğiniz görsel site haritaları sunar, bunlar sadece dosyaların hangi dizinde olduğunu değil, aynı zamanda neyin nereye bağlı olduğunu da gösterir.

Görsel bir site haritasını kullanmak için, önce ana sayfa olacak dosyayı seçmeniz gerekir. Bu, belirli bir sitenin varsayılan indeks sayfası olabilir. Bir sitenin bir alt bölümüne ait site haritasını göstermeyi de isteyebilirsiniz; bu durumda ana sayfa görünüşünü değiştirerek, o sayfayı site haritasının odak noktası haline getirebilirsiniz (5).

**4.2.7.1. Ana Sayfayı Ayarlamak**

Site penceresinde Site çekme menüsünden Define Sites komutunu seçin. *Define Sites* (site tanımla) iletişim kutusu açılır.

Düzenlemek istediğiniz siteyi seçin ve Edit butonuna tıklayın. *Site Definition* (site tanımı) iletişim kutusu açılır.

Sol taraftaki kategori kısmından, Site Map Layout kategorisine tıklayın. iletişim kutusunun bu paneli öne gelir (Şekil 4.46.). Sitenizin kök dizininde index.html isimli bir dosya varsa, Dreamweaver onun ana sayfa olduğunu varsayar ve *Home Page* metin kutusuna onu girer.

*Home Page* metin kutusuna, ana sayfa olarak atayacağınız dosyanın konumunu girin veya *Browse* düğmesine tıklayarak *Choose Home Page* (ana sayfa seç) iletişim kutusunu açın.

Dosyayı seçin ve Open butonuna tıklayarak *Choose Home Page* iletişim kutusunu kapatın ve *Site Definition* iletişim kutusuna geri dönün.

OK butonuna tıklayarak *Site Definition* iletişim kutusunu kapatın ve Site penceresine geri dönün. Artık site haritasını görebilirsiniz (5).

**4.2.7.2. Site Haritasını Görmek**

Site penceresinde, *Site Map View* (site haritası görünümü) düğmesine tıklayın. Site penceresinde site haritası görünür (Şekil 4.47.).

Pencerenin sağ alt köşesini sürükleyerek pencereyi büyütebilirsiniz; ayrıca, iki bölmenin arasındaki kenarı sürükleyebilirsiniz (5).

**4.2.7.3. Site Haritasının Düzenini Ayarlamak**

Site Definition iletişim kutusunun Site Map Layout panelini açın. *Number of Columns* metin kutusuna bir sayı girerek maksimum sütun sayısını ayarlayın. *Column Width* metin kutusuna bir sayı girerek, piksel cinsinden sütun genişliğini ayarlayın. Sayfa ikonlarının etiketi olarak dosya isimlerini ya da sayfa başlıklarını kullanabilirsiniz. Dosya isimlerini görmek için *File Names* düğmesini seçin. Sayfa başlıklarını görmek için *Page Titles* düğmesini seçin. Normalde gizli olanlar da dahil olmak üzere (LCK dosyaları ve FTP kayıt dosyaları gibi) tüm dosyaları göstermek için *Display Files Marked as Hidden* onay kutusunu işaretleyin. Bir frame ailesindeki tüm dosyalar gibi, tüm bağımlı dosyaları göstermek için *Display Dependent Files* onay kutusunu işaretleyin. OK tuşuna tıklayarak Site Definition iletişim kutusunu kapatın ve Site penceresine dönün (5).

**4.2.7.4. Site Haritasının Bağlarını Çizmek**

Site haritasını izlerken içinden bir sayfayı seçerseniz, sayfanın yanında bağ aracı (Link Tool) ikonu belirir. Bu aracı istediğimiz dosyaya sürükleyip bıraktığımızda, dosyaya link vermiş oluruz (5).

**4.2.7.5. Bağ Aracını Kullanmak**

Bu ikona tıklayıp, site haritası panelindeki veya yerel siteler panelindeki bir sayfaya sürükleyerek bir bağ yaratabilirsiniz. Bağ, ikonu aldığınız sayfada, ikonu bıraktığınız sayfaya giden bir bağ yaratır (Şekil 4.48.).

Bağ ikonunu sürüklerken düz bir çizgi göreceksiniz. Yerel panelindeki bir sayfaya sürüklerseniz, sayfa site haritasında yeni konumunda belirir. Buna ek olarak sayfanın alt tarafında sayfanın başlığına veya medya dosyasına bir bağ belirir (5).

**4.2.7.6. Yeni Bağ Düzenlemek**

Bağ ikonunu sürüklediğiniz sayfaya çift tıklayın. Document penceresinde açılır. Sayfanın alt tarafındaki bağı bulun. Bu bağı istediğiniz herhangi bir yere sürükleyebilir, yazısını düzenleyebilir veya konunu ve bağı mevcut nesnelere kopyalayabilirsiniz (5).

**4.2.8. Tasarım Notlarını Ayarlamak**

Tasarım notları (Design Notes) Dreamweaver Programının 3.0 versiyonu ile gelen, yeni araçlarından biridir ve bir dosyayla ilgili iş akışı bilgilerini kaydetmenize izin verir. Tasarım notlarını kullanarak, dikkat isteyen dosyaları belirtebilir, bir dosyanın üzerinde kimlerin çalıştığını takip edebilir ve hemen her konuda notlar düzenleyebilirisiniz.

Tasarım notlarını kullanabilmek için, önce yerel sitenizde bunların kullanımını etkinleştirmeniz gerekir.

F5 tuşuna basarak Site penceresini açın. Site penceresinin menü çubuğundan Sites > Define Sites komutunu seçin. *Define Sites* iletişim kutusu açılır. Tasarım notlarını etkinleştirmek istediğiniz sitenin adına tıklayın. Edit butonuna tıklayın. *Site Definition* iletişim kutusu açılır. Sol taraftaki *Category* kısmından *Design Notes* kategorisine tıklayın. İletişim kutusunun bu paneli açılır. *Maintain Design Notes* onay kutusu işaretliyse, bir şeye dokunmayın. İşaretsizse, bu onay kutusunu işaretleyerek Tasarım notlarını etkinleştirin. Tasarım notlarını da sunucuya yüklemek isteyebilirsin Tasarım notlarının otomatik olarak yüklenmesini sağlamak için, *Upload Design Notes for Sharing* onay kutusunu işaretleyin. Bir proje üzerinde tek başınıza çalışıyorsanız veya grubunuzdaki herkes Dreamweaver kullanmıyorsa, *Upload Design Notes for Sharing* onay kutusunu boş bırakın; aksi halde sunucu sizin dışınızdaki kimseye faydası olmayan dosyalarla dolar (5).

**4.2.8.1. Tasarım Notlarını Kullanmak**

Tasarım notu, temel olarak başka bir dosya hakkında bilgi içeren gizli bir metin dosyasıdır. Tasarım notlarını sadece Web sayfalarında değil, resimlerde, multimedya dosyalarında, CSS veya HTML style sayfalarında, kütüphane öğelerinde, şablonlarda ve yerel sitenizdeki tüm dosya türleriyle kullanabilirsiniz (5).

**4.2.8.2. Bir Tasarım Notu Yaratmak**

Site penceresinde istediğiniz dosyayı seçin veya çalışma ekranında açın. Sonra, Site veya çalışma ekranının menü çubuğundan File > *Design Notes* komutunu seçin. *Design Notes* iletişim kutusu açılarak dosyanın adını ve sitede konumunu / adresini gösterir (Şekil 4.49). *Status* (durum) çekme menüsü, bir dosyaya şu etiketlerden birini atamanızı sağlar: *Draft* (taslak); *Revision* 1, 2, 3 (revizyon 1, 2, 3); *alpha, beta, final* (son); *needs attention* (dikkat gerektiriyor). Bunlardan birini seçebilir veya menüyü boş bırakabilirsiniz. Tasarım notuna geçerli tarihi eklemek için *Notes* metin kutusundaki dikey kaydırma çubuğunun üstündeki *Date* düğmesine tıklayın. *Notes* metin kutusunda tarih belirir. Notes metin kutusuna ilave notlarınızı yazın. Dosya açıldığında Dreamweaver programının Tasarım notlarını açması için, *Show When File Is Opened* kutusunu işaretleyin. Farklı dosyalarda tutarlı bit tarzda kullanacağınız özel notlar eklemek için *All Info* sekmesine tıklayarak iletişim kutusunun bu paneline geçin (Şekil 4.50.). Bir not eklemek için + düğmesine tıklayın. *Name *(isim) ve *Value* (değer) metin kutularına *Proje* ve *Intranet *veya *Yazar* ve *towers* gibi bilgileri girin. İşiniz bittiğinde, OK tuşuna tıklayarak iletişim kutusunu kapatın ve Tasarım notlarınızı kaydedin (5).

**4.2.8.3. Tasarım Notlarına Erişmek**

Bir Web sayfasına veya başka bir dosyaya ait bir Tasarım notunu açmak, bir tasarım notu yaratmak gibidir. Aynı iletişim kutusunu açarsınız, sonra Tasarım notlarını okur ve düzenlersiniz (5).

**4.2.8.4. Bir Tasarım Notu Açmak**

Site penceresinde Tasarım notlarını okumak istediğiniz dosyayı seçin. Site penceresinin menü çubuğundan File > Design Notes komutunu seçin. Design Notes iletişim kutusu açılır (5).

**4.2.8.5. Tasarım Notlarını Silmek**

Bir dosyayı sildiğinizde, Dreamweaver o dosyayla ilişkili tasarım notlarını otomatik olarak silmez. Geride kalan tasarım notlarını kolayca silebilirsiniz. Site penceresinin menü çubuğundan, Sites > Define Sites komutunu seçin. *Define Sites* iletişim kutusu açılır. Tasarım notlarını silmek istediğiniz sitenin adına tıklayın. *Edit* butonuna tıklayın.

*Site Definition* iletişim kutusu açılır. Sol taraftaki kategori kısmından *Design Notes* kategorisine tıklayın. İletişim kutusunun bu paneli açılır. *Clean Up* düğmesine tıklayın. Bir iletişim kutusu açılarak, bunu yapmayı gerçekten isteyip istemediğinizi sorar. Yes butonuna tıklayın. Dreamweaver, seçiğiniz sitede geride kalan tüm tasarım notlarını siler. *Maintain Design Notes* seçeneğinden işaretli kaldırırsanız, Dreamweaver sitenin tüm tasarım notlarını siler (5).

**SONUÇ VE ÖNERILER: **

Internet alanındaki gelişmeler sonucunda kullanımının yaygınlaşması, kişisel kullanıcılarda bu büyük oluşumda yer alma isteği doğurmuştur.

HTML dilini kullanarak, web siteleri oluşturmak zor ve çok uzun süren bir iştir. Fireworks ve Dreamweaver tarzı programlar, pratik ve daha özgür çözümler sunmamızı sağlayacaktır. Bu sayede yapacağımız işleri kolay ve daha kısa zamanda yapmış olacağız. Ayrıca oluşturacağımız web siteleri görsellik açısından daha zengin olacaktır.

Fakat, anlatılan yararlarına rağmen bu programlar ile yapılan tasarımların bazı dezavantajları vardır. Kullandığımız paket programların yetersiz olduğu noktalar mutlaka çıkacaktır. Bu sebepten HTML dilini öğrenmemiz önümüzü açarak, bize takıldığımız yerlerden kurtulmamıza yardımcı olacaktır. ** **

**KAYNAKLAR:**

**1. ÖCAL, Hakkı, *****Internet Tasarım Rehberi*****, Ankara 1998******

**2. YILDIZ, Murat, *****WEB Tasarımı*****, BYTE Dergisi, Cilt 5, Sayı 1-12******

**3. www.hacettepe.edu.tr.**

**4. Fireworks Programı ve Fireworks Help Dosyaları.**

**5. Dreamweaver Programı ve Dreamweaver Help Dosyaları.**

**ÖZGEÇMİŞ:**

Sinan AYDIN 1978 yılında Bulgaristan’ ın Şumen şehrinde doğdu. 1989 yılında Türkiye’ ye göç ettikten sonra Manisa’ da ikamet etmeye başladı. İlk öğrenimini Murat Germen İlkokulu’ nda ve Cumhuriyet Ortaokulu’ nda tamamladı. Daha sonra Manisa Endüstri Meslek Lisesi Elektronik Bölümüne girmeye hak kazandı. Öğrenimine bir yıl burada devam ettikten sonra İzmir Çınarlı Teknik Lisesi Elektronik Bölümüne geçiş yaptı. 1997 yılında mezun oldu. Aynı yıl Gazi Üniversitesi, Teknik Eğitim Fakültesi, Makine Eğitimi Bölümü, Kalıpçılık Anabilim Dalında öğrenim yapmaya hak kazandı. Halen öğrenimine bu bölümde devam etmektedir.

PAGE

PAGE 1

**Şekil 3.4. View Menüsü (4).**

**Şekil 3.2. File Menüsü (4).**

**Şekil 3.3. Edit Menüsü (4).**

**Şekil 3.5. Insert Menüsü (4).**

**Şekil 3.6. Modify Menüsü (4).**

**Şekil 3.7. Text Menüsü (4).**

**Şekil 3.8. Xtras Menüsü (4).**

**Şekil 3.9. Window Menüsü (4).**

**Şekil 3.10. Toolbox Paneli (4).**

**Şekil 3.11. Stroke Paneli (4).**

**Şekil 3.12. Fill Paneli (4).**

**Şekil 3.13. Inner Bevel Effect Paneli (4)**

**Şekil 3.14. Outer Bevel Effect Paneli (4)**

**Şekil 3.16. Emboss Effect Paneli**

**Şekil 3.15. Drop Shadow Effect Paneli**

**Şekil 3.18. Multiple Effect Paneli**

**Şekil 3.17. Glow Effect Paneli**

**Şekil 3.19. Info Paneli (4).**

**Şekil 3.20. Styles Paneli (4).**

**Şekil 3.21. Swatches Paneli (4).**

**Şekil 3.22. Color Mixer Paneli (4).**

**Şekil 3.23. Layer Paneli (4).**

**Şekil 3.24. Frame Paneli (4).**

**Şekil 3.25. Main Toolbar (4).**

**Print: **Yapılan çalışmanın yazdırılmasını sağlar.

**Şekil 3.26. Modify Toolbar (4).**

**Şekil 3.27. View Control Toolbar (4).**

**Şekil 3.28. Yeni açılan dosyanın boyutlarının belirlenmesi (4).**

**Şekil 3.29. Artalana Texture atanması (4).**

**Şekil 3.30. Inner Bevel efektinin verilmesi (4).**

**Şekil 3.31. Drop Shadow efektinin verilmesi (4).**

**Şekil 3.32. Emboss efektinin verilmesi (4).**

**Şekil 3.33. Yazıya Inner Bevel efektinin verilmesi (4). **

**Şekil 3.34. Yazıya Outer Bevel efektinin verilmesi (4).**

**Şekil 3.35. Bannerın bitmiş hali **

**Şekil 3.36. Butonlara Emboss efektinin verilmesi ve Clone komutu ile çoğaltılması (4). **

**Şekil 3.37. Butonlara Emboss efektinin verilmiş barın üzerine yerleştirilmesi (4). **

**Şekil 3.38. Yazılara efektlerin verilmesi (4). **

**Şekil 3.39. Hareket efekti için butonların ilk ve son durumları (4). **

**Şekil 3.40. Butonların Slice aracı ile kesilmesi (4).**

**Şekil 3.35. Bannerın kullanılmaya hazır şekli (4). **

**Şekil 4.1. Dreamweaver Programının çalışma ekranı (5).**

**Şekil 4.2. File Menüsü (5).**

**Şekil 4.3. Edit Menüsü (5).**

**Şekil 4.4. View Menüsü (5).**

**Şekil 4.5. Grid Settings Paneli (5).**

**Şekil 4.6. Insert Menüsü (5).**

**Şekil 4.7. Select Image Source iletişim kutusu (5).**

**Şekil 4.8. Properties Denetçisi (5).**

**Şekil 4.9. Insert Rollover Image iletişim kutusu (5).**

**Şekil 4.10. Insert Table iletişim kutusu (5).**

**Şekil 4.11. Insert Navigation Bar iletişim kutusu (5).**

**Şekil 4.12. Layer özelliklerini gösteren Properties Denetçisi (5).**

**Şekil 4.13. Form özelliklerini gösteren Properties Denetçisi (5).**

**Şekil 4.14. Modify Menüsü (5). **

**Şekil 4.15. Page Properties iletişim kutusu (5).**

**Şekil 4.16. Quick Tag Editor İletişim Penceresi (5).**

**Şekil 4.17. Convert Tables to Layers İletişim Penceresi (5).**

**Şekil 4.18. Convert Layers to Table İletişim Penceresi (5).**

**Şekil 4.19. Text Menüsü (5).**

**Şekil 4.20. Text Formatları**

**Unordered List****:***** ***Yazılarımızın başına küçük bullet’ lar koyabiliriz.

DreamWeaver

Flash

Photoshop gibi

**Şekil 4.21. Edit Font List Penceresi (5).**

**Şekil 4.22. Edit Style Sheet Penceresi (5).**

**Şekil 4.23. New Style Penceresi (5).**

**Şekil 4.24. CSS stilinde yeni stil oluşturulması (5).**

**Şekil 4.25. Yazım Denetiminin yapılması (5).**

**Şekil 4.26. Command Menüsü (5).**

**Şekil 4.27. Clean Up HTML penceresi (5).**

**Şekil 4.28. Clean Up Word HTML penceresi (5).**

**Şekil 4.29. Sort Table penceresi (5).**

**Şekil 4.30. Site Menüsü (5).**

**Şekil 4.31. Window Menüsü (5).**

**Şekil 4.32. Launcher Paneli (5). **

**Şekil 4.33. Library Penceresi (5). **

**Şekil 4.34. HTML Style Penceresi (5). **

**Şekil 4.35. CSS Style Penceresi (5).**

**Şekil 4.36. History Penceresi (5).**

**Şekil 4.37. HTML Source Penceresi (5).**

**Şekil 4.38. Properties Denetçisi (5).**

**Şekil 4.39. Objects Panelleri (5).**

**Şekil 4.40. Site Penceresi (5).**

**Şekil 4.41. Define Sites Penceresi (5).**

**Şekil 4.42. Sites Definition Penceresi (5).**

**Şekil 4.43. Link Checker Penceresi (5).**

**Şekil 4.44. Site Definition Penceresi (5).**

**Şekil 4.46. Site Map Layout kategorisinin etkinleştirilmesi (5).**

**Şekil 4.45. Site Definition Penceresinde Check In/Out etkinleştirilmesi (5).**

**Şekil 4.47. Site Haritası (5).**

**Şekil 4.48. Bağ Aracını Kullanmak (5).**

**Şekil 4.49. Design Notes penceresinin Basic Info bölümü (5).**

**Şekil 4.50. Design Notes penceresinin All Info bölümü (5).**

**Şekil 4.51. Design Notes özelliklerinin silinmesi (5).**

---
*Kaynak: `INTERNET, WEB SERVER ve WEB TARAYICILARI/O-d-e-v-s-i-t-e-s-i-com-18905.doc` — Speedy Gonzales — 2001*
