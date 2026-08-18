# DNS' In Hiyerarşik Yapisi

**DNS’ in Hiyerarşik Yapısı**

DNS hiyerarşisinde kullanılan Domain isimleri birbirinden nokta ile ayrılarak yapılanırlar. Fully Qualified Domain Name (FQDN) tek olmalı ve Host’un ismini tam olarak ifade etmelidir. Örneğin ; **mx.kabak.net**
Aşağıdaki şekilde örnek bir domain hiyerarşisi gösterilmektedir.

**DNS ve İNTERNET**

İnternette Domain Name Sistem bazı kuruluşlar tarafından kontrol edilmekte ve Register edilmektedir. Aşağıdaki tabloda Bazı isimler belirtilmiştir.

| DNS Domain Name | Organizasyon Tipi |
| --- | --- |
| Com | Ticari Kuruluşlar |
| edu | Üniversiteler |
| Org | Ticari amacı olmayan kuruluşlar |
| Net | İnternet Kuruluşları |
| gov | Hükümet Kuruluşları |
| mil | Askeri kuruluşlar |
| num | Telefon Numaraları |
| arpa | Reserve DNS |
| xx | Iki-harf Ülke Kodu |

**İsim Seçimi Yapmak**
DNS isminizi seçerken internette register ettiğiniz DNS isminizi seçebilirsiniz. (Örneğin : kabak.net ) . Ancak farklı internal ve external isimlerin kullanılması daha iyidir. Bu durumda internal DNS’inide bir forest root ismi, external DNS isminizden farklı olabilir. Örneğin external DNS isminiz kabak.net ise internal isminizi tatlikabak.net olarak yapılandırabilir ve şirket içi departmanlarınızı Active Directory içerisinden farklı Domainlerle (Örneğin : hr.tatlikabak.net gibi) hoş bir hale sokabilirsiniz.
**DNS Server’in yüklenmesi ve ayarlanması**
DNS serverin yüklenebilmesi için öncelikle makinanızın domain içerisinde bir Windows 2000 Server olması gerekmektedir. DNS bir TCP/IP tabanlı uygulamadır. Ancak 2000 de artık Windows NT'den farklı olarak DNS dinamik güncellemeyide beraberinde getirmiş ve aşağıdada belirteceğimiz bir takım yeni uygulamalarla bize daha çok kolaylık sağlamıştır.
**DNS ' in Yüklenmesi**
Eğer işletim sisteminin kuruluşu sırasında DNS' i yüklemediyseniz birazdan bu işlemin ne kadar kolay olduğunu göreceksiniz. Bunun için öncelikle bazı kontroller yapmamız gerekecektir. Sırasıyla şu kontrolleri DNS yükleme işlemine geçmeden önce yapmalısınız ki sisteminize DNS yükleme işlemi sorunsuz ve ayarları önceden konfigüre edilmiş olsun.
**1-** *Start®Settings®Network and Dial up connections®Local Area Connection*(Sağ tıkla)* ®Properties’ *den TCP/IP simgesini seçip *Properties*’i tıklayın. IP adresinin SUBNET ve Default Gateway adreslerinin doğru verildiğinden emin olduktan sonra DNS Server kısmına makinanın kendi IP numarasını girin.
**2- ***Advanced *seçeneğini seçip DNS tabında DNS IP'sinin verildiğinden emin olun.

**3- **Eğer sisteminizde bir DNS server var ise ; Masaüstünde *My computer *simgesini sağ tıklayıp *Properties®Network Identification®Properties®More® *kısmında olan *'Primary DNS suffix of this computer' *seçeneğine mevcut DNS Name adresinizi girin.
**4- **Bu degisikliklerden sonra makinanızın restart etmesi gerekecektir.
Bütün bu ayarlamaları doğru bir şekilde yaptığınızdan emin olduktan sonra artık DNS i yükleyebilirsiniz. Bunun için birden çok seçeneğiniz var, biz burda sadece birini söyleyeyelim.
1- *Start®Programs®AdministrativeTools®ConfigureYour Server®Networking®DNS®Install DNS Service®Set Up DNS*

**DNS Servisinin Konfigürasyonu**
DNS için en önemli konu tabiki bölgelerin(ZONE) oluşturulmasıdır. Biz bu aşamadan itibaren bölge olarak Zone kelimesini kullanacağız. Domaininiz içerisinde herhangi bir Zone oluşturmadıktan sonra DNS kurmanızın bir anlamı olmayacaktır. Zone' lar DNS içerisinde tanımlanan tüm bilgileri tutacaklardır. İki tip Zone oluşturulabilir. **Forward lookup zones **and **Reserve lookup zones . ***Forward lookup zone *IP adresinden DNS ismini elde etmek için, *Reserve lookup zone *ise tersini , yani DNS isminden Ip adresini bulmak için kullanılmaktadır. Burada bizim zorunlu olarak öncelikle *Forward lookup zonu*'u* *oluşturmamız gerekecektir, ancak *reserve lookup zone *mecburi değildir, zaten Windows 2000'de bu özellik default **disable **olarak gelmektedir.

*Şekil 1.1 DNS Servisinin çalıştırılması.*
DNS servisini ilk kez çalıştırdığınız için ilk konfigürasyonu yapmanız gerekmektedir. Bunun için DNS’i çalıştırdıktan sonra server üzerine sağ tıplayıp konfigürasyon menüsüne girmelisiniz.

*Şekil 1.2 DNS Servisinin konfigürasyon menüsü*
Bu aşamada öncelikle DNS serverin ROOT DNS (Domain içindeki ilk DNS) olup olmadığını belirmelisiniz. Eğer ROOT DNS değilse ROOT DNS görevini gören serverin IP numarasını girerek ROOT DNS olarak belirtmelisiniz.

*Şekil 1.3 DNS Serverin konumunun belirtilmesi.*

**Zone Dosyaları ve Delegasyon**

DNS database’i birden fazla Zone’dan oluşabilir. Her bir zone kendi içinde RR kayıtlarını barındırır. Tek bir DNS server bir yada daha fazla Zone’u host edebilir. Her bir Zone kendine has Domain Name ile ilişkilendirilir ve onunla anılır. Zone’un Root Domain Name ile birlikle bütün isimlerini ve bilgilerini barındırır. Her Zone’da ilk kayıt *Start of Authority *(SOA) kaydıdır ve olmalıdır. SOA kaydı *Primary DNS Name Server*’in kimliğini ifade eder. Zone içerisindeki isimler diğer Zone veya Zone’ları delege etmek içinde kullanılabilirler. Delegasyon işlemi ayrı ve uzak bir yerdeki Zone’un yönetilebilmesi için atanan sorumluluktur. Bu şirketinizin içindeki farklı bir organizasyon, departman olabilir. Delege edilen Zone için Zone içerisinde NS kaydı kullanılır ki bu Delege edilen Zone için kullanılacak yetkili DNS name serverdir. Aşağıda bir DNS namespace için delegasyonun neden gerekli oldugunu açıklayabiliriz.
· Bir organizasyon içerisideki Departman yada başka organizasyonların DNS domain name’i yönetmek için.
· Çok büyük networklerde DNS database’inde, isim çözümlemesinin daha kolay ve yüksek performansta yapılabilmesi ve hata toleransı (fault tolerans) sağlayabilmek için birden fazla Name server arasında paylaştırmanız gerekebilir.
NS kayıtları her bir zone için delegasyon işlemini kolayştırmaktadır. Bu kayıtlar hem *forward lookup *, hemde *reserver lookup zone *için geçerlidir. Bu işlem hedef Zone’da delegasyon işlemini yapacak Dns Server için bir NS kaydı oluşturmakla yapılacaktır.
Aşağıdaki şekilde yönetim **kabak.net **tarafından gerçekleştirilmektedir. Domain iki Zone’dan oluşmaktadır , **kabak.net **ve **satış.kabak.net**

**Yeni bir *****Forward Lookup Zone *****oluşturma**

**Şekil 1.4 Yeni Zone oluşturma**

3 Tip F*orward Lookup Zone *oluşturabiliriz. Bunlar;
**A ) Active Directory Integrated**: Domain içerisindeki tüm Domain Controller makinalar eğer Windows 2000 ise bu kullanılmalıdır. Mixed mode (Domain içerisindeki makinaların sadece Windows 2000 olmaması durumuna verilen isim. Notive Mode bunun tersi olarak Domain içerisindeki tüm makinaların Windows 2000 işletim sistemine sahip olması anlamına gelmektedir. Bu seçim serverlar üzerinde yapılmakta ve default olarak tüm serverlar mixed modda çalışmaktadırlar.) çalışan bir domain içerisinde bu tip bir zone oluşturmuşsanız Unix serverların Microsoft DNS ile uyumlu çalışabilmesini sağlayabilirsiniz. Ayrıca Active Directory Integrated Zone oluşturmak ile domain içerisinde oluşturduğunuz diğer Active Directory Integrated Zone’ larla Dynamic update (Otomatik güncelleme ) yapmasını sağlayabilirsiniz. Böylece DNS için manuel kayıt girmekten kurtulmuş olursunuz.
Öncelikle yeni Zone tipimiz için Active Directory Integrated Zone tipini seçiyoruz. Ancak unutmayınız, bunun için bilgisayarınıza Active Directory kurulu olmalıdır.

**Şekil 1.5 Active Directory Integrated Zone kuruluşu**

Örnek olarak ismi *‘pazarlama.kabak.net’ *olan bir zone oluşturalım.

**Şekil 1.6 Avtive Directory Integrated Zone isminin girilmesi**

**B ) Standart Primary : **Eğer DNS serveriniz kurulu olduğu makina bir Domain Controller değilse (yani sadece server olarak yapılandırılmış ve domaine dahil edilmiş ise) bu seçilmelidir.

**Şekil 1.7 Standart Primary Zone isminin girilmesi**

Bu işlemden sonra wizard size oluşturulacak dosyanın adını soracaktır. Bildiğiniz gibi DNS bilgileri bir text dosyada tutulmaktadır.

**Şekil 1.8 Zone için dosyanın isminin belirtilmesi**

**C ) Standart Secondary :** Eğer DNS ilk olarak bir (Örneğin) Unix serverdan host ediliyorsa (yani clientlerin sorgularına ilk olarak Unix gibi bir server cevap veriyorsa) o zaman Microsoft DNS bu tipte bir zone olarak kurulmalıdır. Bu tip bir zone Standart Primary zone' daki tüm bilginin bir *Read-Only *kopyasını bulunduracak ve client’lara gerekli bilgileri bu dosyadan verecektir. *Secondary Zone *kullanmak aslında oldukça avantajlıdır. Öncelikle sisteminizde birden fazla *Primary Zone *olması client’ların sorgularında network trafiğini artıracak ve karmaşıklığa sebebiyet verecektir. Bu nedenle sisteminizde tek bir Primary DNS olması ve diğer DNS serverların Secondary olmasını tavsiye ederiz. Bununla beraber domain yapınız farklı subnetlere veya Wan ile uzak bağlantılara parçalanıyorsa her bir uç noktaya Secondary DNS kurmanız hem en iyi çözüm olacak hemde replikasyon işlemlerinde network trafiğini düşürerek , eskiden korkunç zaman olan DNS sorgulamalarını çok kısa süreye indirmenizi sağlayacaktır.

*Şekil 1.9 Standart Secondary DNS’in kuruluşu*.
Bu seçimi yaptıktan sonra Zone ismimizi girmemiz gerekiyor.

*Şekil 1.10 Secondary DNS Zone isminin girilmesi*
Bir sonraki aşamada ise master DNS yani Primary DNS serverin IP numarasını vermemiz gerekiyor. İşlemimiz bu aşamada bitecektir. Yeni Zone’umuz create edilmiştir.

*Şekil 1.11 Primary DNS’in IP numarasının girilmesi.*
Bütün oluşturulan zone bilgileri *%SystemRoot%\\System32\\DNS *folderindedir.

---
*Kaynak: `DNS' IN HİYERARŞİK YAPISI/DNS' IN HİYERARŞİK YAPISI.doc` — Marmara — 2004*
