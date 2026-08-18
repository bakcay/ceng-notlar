# Router Nasil Çalişir

ROUTER NASIL ÇALIŞIR? (CHIP MART-99 S.200)

Internet-Router başarılı bir şekilde kurulursa ev veya ofisteki tüm bilgisayarlara Internet’in kapısını açıyor. Ama şu anki sisteminizden vazgeçmeden önce iyi bir araştırma yapmanız gerekiyor. Çünkü birçok masraftan kurtulacaksınız ama yenileriyle karşılaşacaksınız, ayrıca ağınızdaki problemlerden de kurtulacaksınız.

500 doların altında fiyatlara satılan routerlar ile yerel ağınızdaki makineleri hiçbirine modem yada ISDN kartı takmadan Internet’e bağlayabiliyorsunuz.çünkü telefon ağına bağlantı işini router yapıyor. Bu akıllı cihazlar teknik olarak ağlar arsındaki bağlantıları gerçekleştiren cihazlar olarak biliniyor. Görevleri local ağdaki herhangi bir makineye yönlenmiş olan veri paketini toplamak. Eğer bağlantı yoksa router servis sağlayıcı seçip arıyor ve isim-şifre girerek Internet’e bağlantıyı sağlıyor. Daha sonrada veri paketlerini taşıması için servis sağlayıcıya veriyor.

ROUTER İLE ÇOKLU AĞ BAĞLANTILARI

Router’ın bağlantı mantığına göre tek bir servis sağlayıcı olma zorunluluğu yok.Aynı şekilde tek bir bağlantı şartı da yok Router verinin ulaşacağı adrese göre seçim yapabilir.”Routing-table” adı verilen bir tabloda tutulan yollara göre ağlardaki grupların istedikleri yerlere nasıl ulaşacakları belirlenmiş.Altenatiflerde yine aynı tablolarda sabit bir şekilde tutuluyor . aynı tablolama mantığında her bilgisayar kendi adına da faydalanıyor.başka bir bilgisayara mı yoksa bir ağ geçidine mi verileri yönlendireceğini bu tablolara bakarak kararlaştırıyor.

En önemli avantaj birden fazla bağlantının aynı anda desteklenmesidir. Bir taraftan Internet’e bağlanılırken diğer taraftan birçok grup ve ağ doğrudan erişilebilir oluyor. Bağlantı noktaları için şifre ve isimlerden oluşan farklı profiller bulunuyor ve tabi ki birde özel ağ adresi. Diğer ağ adresleri ise servis sağlayıcı çıkışını göstermeli. Böylece router hafızasındaki tablo aracılığıyla paketleri nereye göndereceğini kolayca bulabilmelidir. ISDN-router’ların bir özelliği de ISDN bağlantısının her iki kanalını da aynı anda aktif tutabilmeleri. Bir grup Internet’e bağlı iken bir diğer grup da Internet bağlantısı hazırlayabilir.

“Routing-table” adı verilen tablolar aslında birden fazla işlere sahiptir. Alternatif yollar da hazırlayabiliyorlar. Bunun anlamı bir adres bölgesine ulaşmak için birden fazla bağlantı noktasının olduğudur. Bunun avantajı da eğer bir bağlantı koparsa veya çok yüklü ise diğer yolların paketi yerine ulaştırmak için denenecek olmasıdır.

MASKELEME YARDIMA YETİŞİYOR

Bilgisayarı ile servis sağlayıcı üzerinden Internet’e bağlananlar her seferinde farklı bir IP adresi alırlar.Adres,kullanıcıya servis sağlayıcı tarafında adres havuzundan dinamik olarak sağlanır.Router üzerinden Internet’e çıkan birden fazla makine varsa ortaya bir sorun çıkmaktadır:Birçok bilgisayar için sadece bir IP adresinin bulunması.Örneğin bir kullanıcı bir Web sayfasına erişmek isterse Router’ın gelen paketi hangi istasyona yönlendireceği konusunda karar vermesi zorlaşıyor.

Bu sorunun çözümü port adreslerindedir.Tüm IP paketleri sadece gönderenin ve alıcının IP adreslerini değil,her iki tarafın port adreslerini de taşıyor.Hedef portu paketin Server’a hangi görevle geldiğini bildiriyor.Eğer bir www servisi söz konusuysa 80 numaralı,e-mail ise 110 numaralı port kullanılıyor.

Yardımcı port da her zaman gereklidir.Örneğin iki Browser penceresi(aynı Browser) açıksa,aralarında bir fark olmalı ki cevap doğru pencereye gelsin.Tüm Internet uygulamaları her yeni bir bağlantıda bilgisayarın TCP/IP sisteminden henüz kullanımda olmayan yeni bir port ister.Bu yeni portun adresi karşı tarafa da bildirilir.yeni bir bağlantı kurulmasına sebep olur ve kendine ait bir adresi olur.

Router,gönderenin port numarasını yerel ağdan farklı istasyonlardan gönderilen veri paketlerini ayırt etmek için kullanılır.Kural olarak 60.000 numaralı porttan sonrasını kullanıyor ve bir tabloda belirlediği düzene uyuyor.

Eğer ağdaki iki istasyon aynı Web Server üzerinde geziyorlarsa, Server için bir bilgisayar iki ayrı bağlantı kurmuş gibi görünür. Server dan çıkan paket içindeki port numarasına göre tanıyıp,ait olduğu bilgisayara gönderiliyor.Yani dahili IP adresine doğru istasyona yönlendiriliyor.

IP maskelemenin küçük ağların güvenliği için bir faydası daha var.İşlem her zaman aktif olduğu bilgisayardan aktif duruma getiriliyor.Programlama hatası yüzünden bir uygulama da teorik olarak bir arka kapı(Backdoor:Karşı tarafın bilgisayara sızabileceği hatalı bir yan) bile varsa(örneğin port 4711) , kötü niyetli kullanıcı ancak uygulama daha önceden bir bağlantı kurmuşsa istasyona erişebilir.Pasif bir makine etkilenmez.Tek tehlikeli durum bir truva atının tüm güvenlik kordonunu kırmasıdır.

BAĞLANTI SÜRESİ İLE DOĞRU ORANTILI ÜCRETLER

Eğer router sürekli olarak ağa bağlantı kuruyorsa hata aramak gerekiyor. Ağa kullanıcılarından hiçbiri Internet uygulaması çalıştırmadığı halde, router bunu yapıyorsa kesinlikle bir sorun var demektir. Çünkü Windows 95/98 ağ yapısının aksine, router sürekli olarak ağ bağlantılarını tazelemez. Yerel ağdan herhangi bir IP paketi alırsa ve bunun Internet’e yönlenmiş olduğunu düşünürse router bağlantı kurar.

Yanlış ayarlanmış bir router eğer dikkat edilmez ise telefon ücretlerini yukarıya çekebilir. Birçok router bu gibi durumlar için bir özelliğe sahiptir. Haftalık veya aylık olarak ayarlanabilen belli ücretler söz konusudur. Baştan belirlenen ücret aşılınca router çalışmaz. Tabi ayarlardan ücret hesaplanması açılmış ve kontör ücreti ile kontör süreleri girilmiş olmalıdır.

Eğer router sürekli olarak beklenmedik zamanlarda Internet’e bağlantı kuruyorsa, bunun birçok farklı sebebi olabilir.bunlar basit sebepler olabileceği gibi, çok zararlı sonuçlara da sahip olabilirler. Bunlardan kolayca engellenebilecek olanlar posta uygulamalarıdır. Uygulama her yarım yada saatte bir yeni posta olup olmadığını kontrol ediyor olabilir.

Bir başka sebep de sabit diskte daha önceden kaydedilen HTML dokümanlarının açılması olabilir. Eğer sayfanın içeriğinde yerel olarak kayıtlı olmayan grafikler. Applet’ler veya başka nesneler varsa, Browser Internet’e bağlanıp. Bunları tamamlamaya çalışır. Engellemenin çok kolay. Ama yine aynı kolaylık içinde gözden kaçan bir yolu vardır. Browser’ı “”Off-line” modda çalıştırmak gerekiyor. Bu özellik sadece Browser’larda değil, hemen hemen tüm Internet uygulamalında bulunuyor. Internet2e bir sonraki bağlantıya kadar uygulama Internet’e erişemiyor.

KADEME KADEME HATA ARAMA

Hata arama özellikle istenmeyen bağlantıların protokoller veya görevler tarafından kurulması durumunda zorlaşıyor. Sebep, bağlantının bir programın başlatılması ile ortaya çıkmamasıdır. Bu sorunlar büyük ihtimalle Router yokken, yani ağın dışarıya erişimi yokken varolan sorunlardır.

Bu noktada tek yardımı “trace” adı verilen yöntemler sağlayabilir. Veri trafiğinin çok iyi tabi ki Router’ın tüm hareketleri kaydetmesi olarak özetlenen yöntem, ekrana durum mesajları göndererek çalışıyor. IP paketlerinin alınması PPP bağlantılarının kurulması gibi Router’ın yaptığı çeşitli hareketler gözlemlenebilir.

Ayrıca tarafların IP adresleri, port numaraları gibi bilgilerde ediniliyor. Bu bilgilerden ağdaki hangi makinenin Internet’e bağlanmaya çalıştığı ve ne amaçla bunu istediği anlaşılır. Port numarasından çoğu zaman “gizli” görev tespit ediliyor. Eğer görevin sahibi makine bunu engelleyemiyorsa, zorlamalı metot kullanılabilir. Router ayarlarından sorulan IP adresini ve/veya portu kapatmak mümkündür. Eğer makine aynı bağlantıyı yine gerçekleştirmek isterse, Router bunu engelleyecektir.

Michael TISCHER ve Bruno JENNRICH’TEN çeviren Güçlü AYDOĞAN (guclua@chip.com.tr)

---
*Kaynak: `ROUTER NASIL ÇALIŞIR/ROUTER NASIL ÇALIŞIR.doc` — MURAT ARSLAN — 2004*
