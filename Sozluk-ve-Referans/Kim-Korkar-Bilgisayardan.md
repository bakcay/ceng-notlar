# Kim Korkar Bilgisayardan

0 - Kitap Hakkında 1

2

0 - Kitap Hakkında

CAN UĞUR AYFER KİM KORKAR HAİN BİLGİSAYARDAN?

0 - Kitap Hakkında 3

İçindekiler 0. Kİ TAP HAKKINDA 4 1. GENEL TANIMLAR 6 2. Bİ LGİ SAYARLARIN KISA TARİ Hİ 3. PC'Nİ Zİ N KURULMASI 4. MS-DOS İ Ş LETİ M Sİ STEMİ NE Gİ Rİ Ş 5. EN ÇOK KULLANILAN MS-DOS KOMUTLARI 6. Dİ SKET KULLANIMI VE YEDEKLEME / GERİ YÜKLEME

19

23

28

57

81

KOMUTLARI 7. HAYATI KOLAYLAŞ TIRAN KOMUTLAR VE OLANAKLAR 8. MS-DOS EDIT PROGRAMI 100 9. Vİ RÜSLER 107 10. Bİ Lİ NMESİ GEREKMEYEN AMA YARARLI KAVRAM VE

93

111

KOMUTLAR 11. YALNIZCA MS-DOS SÜRÜM 6'DA OLAN ÖZELLİ KLER Ek 1. SIK RASTLANAN MS-DOS HATA MESAJLARI Ek 2. ASCII KOD TABLOSU 122

131

138

4

0 - Kitap Hakkında

Kitap Hakkında...

0

Bilgisayarcılar sayı sayarken sıfırdan başlar!

Bu kitap, bilgisayar dünyasına ilk adımını PC (Personal Computer) tipi bir bilgisayar ile atanlar ve bilgisayar (PC) konusunda Hİ Ç DENEYİ Mİ OLMAYANLAR İ Çİ N yazılmıştır.

Amacım, PC ve MS-DOS İşletim Sistemi ile ilgili herşeyi değil; bir PC’yi kullanabilmek için bilinmesi gereken temel kavramlar ve sık kullanılan komutları anlatmaktır.

Bu kitap bir MS-DOS kullanım kılavuzu ya da komut referans kitabı değildir. Konular ve komutlar alfabetik sırada değil, olabildiğince kolay kavranmalarını sağlayacağına inandığım bir sırada sunulmaktadır.

Kitabı okurken, elinizin altı nda MS-DOS Sürüm 5 veya daha yukarı sı iş letim sistemi ile donatı lmı ş bir kiş isel bilgisayar bulundurmanı zı ve anlatı lan komutları okurken bir yandan da denemenizi öneririm.

Bilgisayar dünyasının standart dili İngilizce’dir. Bu nedenle, kavramlardan sözederken, genellikle yanlarına İngilizce’lerini de ekledim. Böylece bilgisayar ekranında rastlayabileceğiniz birçok İngilizce terim ve sözcüğe yabancılık çekmemenize yardımcı olmayı umuyorum.

Kitabın 10. bölümü dışında, her yerini okumanızı öneririm.

Bu son bölümü, meraklılara bazı teknik ayrıntılar hakkında fikir vermek için hazırladım.

Kitabın hazırlanmasında büyük katkıları olan büyük oğlum Ömer’e, eşim Reyyan’a ve arkadaşım Sina Hakman’a çok çok teşekkür ederim.

0 - Kitap Hakkında 5

KİTAPTA KULLANILAN SEMBOLLER Dikkat edilmesi gereken bir nokta açıklanıyor.

Bu işaretin bulunduğu paragraf ve bölümleri dikkatle okuyunuz.

Yeni bir komut veya kavram anlatılıyor.

Teknik bir ayrıntıdan sözediliyor, ilginizi çekmiyorsa okumadan geçebilirsiniz. Başınız dertte! Teknik destek isteyiniz.

İleride çok gerekli olabilecek veya işinizi kolaylaştırabilecek bir bir püf noktası açıklanıyor.

6

0 - Kitap Hakkında

GENEL TANIMLAR 1Kişisel bilgisayar dünyasında kullanılan terimlerin çoğu İngilizce kökenlidir, fakat buna rağmen İngilizce-Türkçe bir sözlük kullanarak tüm terimlerin karşılığını bulamayabilirsiniz. Bulduklarınız da, bilgisayar dünyasında kullanılan anlamlarında olmayabilir. Örneğin, "byte" sözcüğünü birçok sözlükte bulamazsınız. "Hardware" sözcüğünü bulduğunuzda da, "madeni eşya, tornavida kerpeten gibi el aletleri" gibi bir açıklamayla karşılaşabilirsiniz. Bu nedenle kitabın başında bir TANIMLAR bölümü gerekliydi. Bu bölümü alfabetik sıraya göre hazırlasaydım, bir sözlük gibi olurdu; oysa, birbirine bağlı terimleri ardarda dizerek, kolay okunan ve okundukça birşeyler öğrenilebilen bir bölüm hazırlamaya çalıştım. Bütün İngilizce bilgisayar terimlerinin anlamlarını bilseniz bile bu bölümü bir kez okumanızı öneririm; böylece aynı dili konuş muş oluruz.

Tanı mlar iki bölüm olarak sı ralanmı ş tı r. İ lk bölümdeki tanı mları n bilinmesi, kitabı n okunması nda kolaylı k sağ layacaktı r. İ kinci bölümdeki tanı mlarsa, bilgisayar dünyası nda sı k sı k kullanı lan, ancak bilinmesi gerekmeyen terimler içindir; ilgilenmeyen okurlar bu ikinci bölümü atlayabilirler.

Sergio Aragonez

0 - Kitap Hakkında 7

GENEL TANIMLAR Her terimin altına italik yazıyla İngilizcesi eklenmiştir.

Bilgisayar

Computer Program Program Programlama dili Programming Language Yazılım Software Elektronik tekniklerle üretilmiş olan, yalnızca 4 işlem aritmetik yapabilen ve iki sayıyı karşılaştırabilen bir makinadır. Aslında, insan (ya da herhangi bir canlının) beyniyle karşılaştırılamayacak kadar YAVAŞ ve YETENEKSİZ olan bilgisayarların, günümüzde bu denli yaygınlaşmalarının iki önemli nedeni vardır :

1) Aritmetikte insanlardan daha HIZLI ve HATASIZ olmaları; (Küçük bir kişisel bilgisayar, 5 haneli iki sayıyı, saniyenin 50,000'de birinde rahatlıkla çarpabilir).

2) Belleklerinin son derece güçlü olması. (10 basamaklı, 10,000,000 telefon numarasını hiç unutmadan, gerektiği kadar süre ile unutmadan saklayabilirler).

Bilgisayarların herhangi bir işi yapabilmeleri için, o işi en ince ayrıntısına kadar, tüm kural ve mantışıyla, adım adım tanımlayan komutlar dizisidir.

Bilgisayar programlarını oluşturan komut dizileri, bilgisayar ortamında ikili sayı sisteminde kodlanarak saklanır. Bu sayı sisteminde kodlanmış olan komutlar, sayılar ve veriler şu görünümdedirler .

3A 2E F2 DC 08 0E 3A F0 33 EA 3F D1 A0 ..... vs vs (Onaltılı kod) 1100 0100 1101 1001 0001 0110 1110 1011 ..... vs vs (İkili kod) Bu biçimde kodlanmış olan komutlar dizisine "makina dilinde program" adı verilir. Bir zamanlar programcılar bu dille program geliştirmek zorundaydı ve dolayısıyla bu dilde düşünüp yazmaları gerekiyordu.

Sonradan, geliştirilen, bildiğimiz harf, rakam ve karakterlerden oluşan programlama dilleri geliştirildi. Günümüzde yaygın olarak kullanılan programlama dillerine BASIC, C, C++, FORTRAN, COBOL, PASCAL, LISP, ASSEMBLY örnek olarak gösterilebilir.

Herhangi bir programlama dili kullanılarak yazılmış olan bir programı makina diline çeviren programlara da DERLEYİCİ adı verilir.

Bir bilgisayarın işe yaraması için gereken ve gerekebilecek programların tümüne birlikte verilen isimdir. Bir başka deyişle; yazılım, bir programlar topluluşudur (ya da bütünüdür.)

Genel olarak 3 türlü yazılım vardır :

1) Sistem Yazılımı: Bir bilgisayarın, genel anlamda çalışır durumda olmasını sağlayan programlar grubudur.

Bilgisayarların marka ve modellerine göre önemli ayrılıklar gösterirler.

2) Destek Yazılımı: Çalışır durumda bir bilgisayarda, kullanıcıların bazı temel işleri kolayca yapmalarını sağlayan programlardır; disk/disket/teyp kopyalama programları, herhangi bir metin yazmak için kullanılan editörler, bilgileri yedeklemek için kullanılan programlar gibi.

8

Donanım Hardware İşletim Sistemi Operating System PC Personal Computer

0 - Kitap Hakkında

3) Uygulama Yazılımı : Bilgisayarların asıl kullanım amaçlarına uygun çalışmalarını sağlayan programladır. Muhasebe, Bordro, Bilgisayar Destekli Tasarım, Kelime İşlem, Elektronik Tablolama, Havayolu, Otel Reservasyon ve oyun programları gibi programlardır.

Bilgisayarın elektronik/elektromekanik ve mekanik aksamına verilen genel isimdir. Örneğin, bilgisayarın ekranı, klavyesi, entegre devre ve transistörleri, enerji kabloları, disk/disket sürücüleri, açma-kapama anahtarı, yazıcısı birer donanım unsurudur.

Bir elektronik malzeme yığını olan bilgisayarın, kullanıcısıyla (ya da kullanıcılarıyla) haberleşmesini sağlayan, verilen komutları çözümleyip yerine getirilmesi için gerekli hazırlıkları yapan, bilgisayarın sahip olduğu kaynakların (bellek, manyetik bilgi saklama kapasitesi, zaman) kolay ve verimli kullanılmasını sağlayan sistem ve destek yazılımlarıdır.

Günümüzde yaygın olarak kullanılan işletim sistemlerine örnek olarak, en başta MS-DOS, sonra UNIX (XENIX, HPUX, AIX gibi türevleri), OS/2, VMS, MVS gösterilebilir. Bu kitapta, Microsoft (ABD) firması tarafından, IBM PC serisi ve bunlarla uyumlu olan kişisel bilgisayarlar için geliştirilmiş olan MS-DOS isimli İşletim Sistemi ve kullanılması anlatılmaktadır.

Personal Computer sözcüklerinin baş harfleridir. İlk olarak IBM firmasının bir modeline verdiği isim olarak bilgisayar dünyasında kullanılmaya başlanan bu iki harf, artık bilgisayar dünyasında neredeyse bir sözcük gibi kullanılmaya başlanmıştır. Artık sadece IBM marka ve belirli bir tip bilgisayar için değil; binlerce fabrikada üretilen, oldukça farklı olabilen bilgisayarlara verilen genel bir isim haline gelmiştir. Bir zamanlar IBM markası da bir sözcük gibi kullanılırdı. Benim bir zamanlar çalıştığım bir iş yerinin, dahili telefon rehberinde "Sekreter, mühendis" gibi ünvanların yanısıra "Aybiyemci" diye bir grup personelin de adı yer alırdı. 1980'li yıllarda "Sizin IBM ne marka ?" gibi soruurdu doğrusu..

Kısaca PC diye adlandırdığımız sınıftaki kişisel bilgisayarların tek ortak özellikleri INTEL marka merkezi işlem birimine (CPU) sahip olmalarıdır.

1994 yılı itibarıyla, INTEL 8088, 80186, 80286, 80386, 80486 ve Pentium (bazılarına göre 80586) model numaralarıyla anılan M.İ.B modelleri ve bunların eşdeğeri başka marka M.İ.B lerle birçok çeşit kişisel bilgisayar üretildi.

INTEL SERİ Sİ MERKEZİ İ ŞLEM Bİ Rİ MLERİ Nİ N GELİ ŞME SÜRECİ M.İ.B Yıl Max. Bellek (Byte) Komut/Saniy e Transistör Sayısı Intel 4004 1971 640 60,000 2,300 Intel 8080 1974 64,000 290,000 5,000 Intel 8086 1977 1,000,000 333,000 5,500 Intel 8088 1978 1,000,000 333,000 20,000 Intel 80286 1982 16,000,000 2,000,000 134,000 Intel 80386 1985 4,000,000,000 4,000,000 275,000 Intel 80486 1986 4,000,000,000 15,000,000 1,200,000 CPU (M.İ.B) Central Processing Unit RAM (Bellek) Random Access Memory

Disk

Disk

Disket Diskette / Floppy Disk Sistem Disketi System Disk

0 - Kitap Hakkında 9

İngilizce Central Processing Unit (Merkezi İşlem Birimi) sözcüklerinin baş harflerinden oluşan bu kısaltma, her türlü bilgisayarın "beyni" denebilecek, aritmetik ve mantık işlemlerinin yapılmasını sağlayan elektronik devre ya da devrelere verilen genel isimdir. PC lerde kullanılan M.İ.B'ler genellikle INTEL marka 80286, 80386, 80486 gibi kodlarla anılan entegre devrelerdir.

Sayısal bilgisayarların, çalıştıkları sürece programlarını ve kısmen verileri sakladıkları devrelerdir (sayısal olmayan bilgisayarlar da vardır; ama bu tip bilgisayarlar hem artık pek kullanılmadıkları, hem de genel amaçlı olmadıkları için, bu kitabın konusu dışında kalmaktadırlar). Bellek sözcüğü ilk bakışta, bilgilerin uzun dönem saklandıkları devreler ya da parçalarmış gibi düşünülse de, tam tersine, bilgisayarın kapatılması durumunda tamamen sıfırlanan devreler için kullanılan, İngilizce, Random Access Memory sözcüklerinin kısaltılmışıdır. RAM kapasitesi, bilgisayarın saklayabileceği bilgilerin miktarıyla (bilgi saklama kapasitesi) pek ilgili değildir; yalnızca bilgisayarda kullanılabilecek programların büyüklüğünü belirler. RAM kapasiteleri, PC serisi bilgisayarlarda genellikle 640 KByte, 1, 2, 4, 8, 16 MByte gibi ölçülerle ifade edilirler. (Bkz : Byte, bit) Bilgisayarlarda, bilgilerin uzun dönem saklanabilmesi için kullanılan, manyetik kayıt prensipleriyle çalışan birimlerdir. PC dünyasında, 1994 yılında kullanılan disklerde tipik kapasiteler 40, 80, 120, 240 MByte, 1024 ve 2048 MByte olarak sayılabilir. 1980 yılların sonlarında bu kapasiteler 5, 10, 20 MByte dolayındaydı. (1024 MByte = 1 GigaByte.)

Esnek bir yapıya sahip olan disketlerden ayırmak için Hard Disk (sert disk) adıyla da anılırlar.

Çalışma prensibi olarak disklere çok benzeyen, ancak kapasiteleri çok çok daha düşük olan manyetik kayıt ortamlarıdır. Genellikle program ve veri taşıma, aktarma ve yedekleme ortamı olarak kullanılırlar. Tipik kapasiteleri 1.2 - 1.44 MegaByte'dır.

PC dünyasında iki değişik ölçüde disket ve bunlara göre iki değişik disket sürücü kullanılmaktadır; 3.5 inch ve 5.25 inch eninde olanlar. Her bir tipin, üretimlerinde kullanılan manyetik malzemesinin kalitesine bağlı olarak, tek (SD) ve çift yoğunluk (DD) ve yüksek yoğunluk (HD) diye adlandırılan değişik kapasitelerde ikişer tipi kullanılmaktadır. Daha eski yıllarda tek ve çift yüzlü türleri de vardı, fakat artık hep çift yüzlü disketler kulla-nılmaktadır.)

Bir PC'yi açıp (''boot'' edip) asgari özellikleriyle de olsa çalışır duruma getirebilmek için gerekli ve yeterli programlar içeren özel bir şekilde hazırlanmış disketlere verilen isimdir.

10

0 - Kitap Hakkında

Monitör (Ekran) PC tipi bilgisayarların ekranları için kullanılan bir başka isimdir. PC dünyasında Hercules (Renksiz), CGA, EGA, PGA, XGA, VGA, SVGA kod isimleriyle anılan birçok çeşit monitör kullanılmıştır. PC'lerde CGA, EGA, VGA gibi özellikler aslında yalnızca EKRAN'ın özellikleri değildir. Görüntü Monitor (Screen) kartıyla ekranı birlikte bir bütün olarak kabul etmek gerekir. Şu yıllarda en yaygın olarak kullanılan tipi SVGA olarak anılandır. Tipik bir SVGA ekranda görüntüler enine 800, yukarıdan aşağı da 600 noktadan oluşmaktadır (biraz daha para harcarsanız 1280 X 1024 nokta çözünürlükte (İngilizce : Resolution) monitör de alabilirsiniz). Her bir noktada 256 değişik renk görüntülenebilir. Özel uygulamalar (grafik sanatlar veya görüntü işleme uygulamalarında) her noktası 32 milyon değişik renk verebilen, hatta özel gözlüklerle 3 boyutlu görüntüleri bile izleyebileceğiniz monitörler vardır.

GÖRÜNTÜ KALİTESİ VE RENK ZENGİNLİĞİ SADECE MONİTÖR TİPİNE BAĞLI DEĞİLDİR; BİLGİSAYARIN İÇİNDE KULLANILAN GÖRÜNTÜ KARTININ ÖZELLİKLERİ DAHA ÖNEMLİDİR. İYİ GÖRÜNTÜ İÇİN BİRBİRİNE UYAN VE BİRBİRİNİ TAMAMLAYAN MONİTÖR VE GÖRÜNTÜ KARTININ KULLANILMASI GEREKİR.

Terminal Klavye PC dünyasında pek kullanılmazlar. Genellikle, çok kullanıcılı, büyük ve orta boy bilgisayarlarda kullanılırlar. Monitörle aralarındaki en önemli ayrım şudur: Monitörlerde görüntü oluşturulmasından, bu görüntünün ekranda kalmasından, program akışı içinde görüntünün değiştirilmesinden bilgisayar sorumludur. Yani, çalışan bir bilgisayarın YALNIZCA monitörünü kapatıp yeniden açarsanız, görüntü tekrar ve aynen geri gelir.

Oysa terminallerde, görüntüden terminal cihazı sorumludur. Bilgisayar, gerektiğinde, yalnızca bir kez, ekrana görüntülenmesi istenen karakteri terminale gönderir ve bu konuyu unutur. Bu nedenle, eğer bir terminali kapatıp açtığınızda, ekrandaki görüntüyü kaybedersiniz.

Keyboard Bu birim için söylenecek birşey yok sanırım.

Fare Mouse Yazıcı Printer Dış görünüşüyle gerçekten fareye benzeyen bu birim, kullanıcıların klavye tutsaklıklarını biraz olsun hafifletmek için tasarlanmıştır. Özellikle grafik uygulamalarda, kalem kullanmaya benzer bir kullanım şekli sağladığı için çok kullanışlıdır. Optik ve mekanik diye sınıflandırılırlar. PC dünyasında genellikle mekanik olanları kullanılır. El hareketlerinizi, altlarında bulunan ve her yöne dönebilen bir top aracılığıyla hissedip, uygulama programına bu hareket bilgisini aktarırlar.

Bilgisayardaki çalışmaların sonuçlarının kağıda aktarılması gerektiğinde devreye giren bu birimler, PC dünyasında matris, lazer ve püskürtmeli olarak 3 ana grupta piyasaya sunulmuşlardır.

Matris tipi olanlar, mekanik olarak, ayrı ayrı kontrol edilen 9 veya 24 iğnenin önce bir mürekkep şeridine, sonrada bu şeritle birlikte kağıda çarpması sonucunda kağıda yazı çıkmasını sağlayan yazıcılardır. Ticari uygulamalarda çok yoğun kullanılırlar. Özellikle birden fazla kopya yazılması gereken uygulamalarda alternatifleri yoktur. Fatura basımı gibi... Renkli veya siyah beyaz çıktı üretebilirler.

Lazer tipi olanlar dış görünüşleri ve çalışma ilkeleri açısından fotokopi makinalarına benzerler. Oldukça yüksek yazı kalitesine sahiptirler ve son derece sessiz çalışırlar. Sıradan modelleri en büyük A4 ölçüsünde kağıt kullanılırlar. Çok pahalı modelleri dışında, hepsi siyah beyaz çıktı üretir. Bit Byte 0 - Kitap Hakkında 11 Püskürtmeli yazıcılar, siyah ya da renkli mikroskopik mürekkep zerrelerini kağıt üzerine püskürterek çalışırlar. Lazer yazıcılar kadar yüksek kaliteli yazmasalar da gerek sessizlikleri, gerekse fiyatları dolayısıyla lazer yazıcılara iyi birer rakiptirler. Birden fazla kopyayı aynı anda yazamazlar, genellikle A4 ölçülerinden daha büyük kağıt kullanamazlar.

İngilizce BInary DigiT sözcüklerinden üretilmiştir. Bilgisayarlarda kodlamada kullanılan en küçük veri elemanıdır (fizikteki atom gibi). Esas olarak, ikili sayı sistemindeki rakamlardır; yani yalnızca 0 (sıfır) veya 1 değerini alabilirler.

(Bu toplamanın yanlış olduğunu farkettiyseniz, bu işi biliyorsunuz demektir) Sayısal kodlamada kullanılan ve anlamlı bilgi içerebilen en küçük veri elemanıdır. Bir BYTE 8 bit'den oluşur. (Fizikteki molekül gibi).

Örneğin A harfini temsil eden Byte, 0100 0001 bitlerinden oluşur. C harfiyse 0100 0011'dir.

Bellek, disk, teyp gibi birimlerin kapasitesi Byte ile ölçülür. Bu kapasiteler genellikle 1000 ve milyon düzeylerinde olduğundan Kilo ve Mega gibi ön eklerle kullanılır. (1 kilometre = 1000 metre, gibi; ancak bir farkla ki, bilgisayar dünyasında "kilo" 1000 değil, 1024 misli anlamındadır : 1024 = 210 = 2x2x2x2x2x2x2x2x2x2 ) 1 KByte = 1024 Byte 1 MByte = 1024 X 1024 Byte 1 GByte = 1024 X 1024 X 1024 Byte KiloByte MegaByte GigaByte

12

Virus Reset Boot veya Boot Etmek MHz (Megahertz)

0 - Kitap Hakkında

Baş belası programlar! İşini çok iyi bilen ve bunu kanıtlamak için başkalarına zarar vermekten kaçınmayan bilgisayar programcıların yazdığı programlardır. Bu programların ortak özellikleri, virüslü programın çalıştırılması durumunda, virüslü olmayan programlara da bulaşabilmeleri, bu yolla hızla yayılmaları ve programı yazanın uygun gördüğü bir koşul ortaya çıkınca, bilgisayarın diskinde kayıtlı bilgilere zarar vermeleridir. Bu şart, ayın on üçünün Cuma gününe rastlaması, günün tarihinin virüs programını yazan kişinin doğum gününe eşit olması, virüs bulaştığından bu yana bilgisayarın 100. kez açılması gibi herhangi bir koşul olabilir.

Bilgisayarınıza virüs bulaşması için, dışarıdan virüslü bir program yüklemiş olmanız ve bu programı bir şekilde çalıştırmış olmanız gerekmektedir.

VİRÜSLER, BİLGİSAYARIN DONANIMINA ZARAR VEREMEZLER; ANCAK SİSTEM YAZILIMINI BOZARAK YA DA SİLEREK BİLGİSAYARI ÇALIŞMAZ DURUMA GETİREBİLİRLER.

Bir bilgisayar çalışırken kilitlenirse (kullanıcı hatası, donanım arızası, program hatası veya virütik enfeksiyon (!) nedeniyle sistem kilitlenmesi olabilir); bilgisayarı kapatıp yeniden açmanız gerekebilir. PC tipi bilgisayarların hemen hemen hepsinde, kapatıp açmaya gerek kalmaması için RESET düğmesi bulunur. Bu düğmeye bastığınızda, sanki bilgisayarın elektriğini kesmiş ve tekrar açmış gibi olursunuz. (Kapatıp açmaktan çok daha sağlıklı bir yöntem olduğuna inanın).

İnsanın, botlarının bağcıklarından tutarak kendisini havaya kaldırması anlamına gelen "bootstrap" kelimesinden türemiştir. Elbette çok anlamlı değil ama belleğinde hiçbir program olmayan, yeni açılmış bir bilgisayarın işletim sistemini diskten kendi belleğine yüklemesini ve ayağa kalkmasını, bir bakıma kendi bağcıklarından çekerek kendini havaya kaldıran bir insana benzetmek oldukça hoş !

Her bilgisayarın içinde bir kristal vardır (saat devresi de denir). Bu kristal saniyede milyonlarca kez titrer. (33 Mhz'lik bir bilgisayarda saniyede 33,000,000 kez). Bu titreyen kristalin oluşturduğu sinyalleri, bir bakıma, davulla kürekçilere tempo veren bir forsa başına benzetebiliriz. Aynı tempoya göre kürek çekilmeyen bir kalyondaki kargaşayı düşünebiliyor musunuz? Bilgisayarın içinde de, aynı forsalar gibi belirli bir tempo ve eş zamanlı olarak çalışması gereken parçalar vardır.

Bir M.İ.B içinde aritmetik ve mantık işlemleri, tipik olarak 3-16 saat sinyalinde (davul vuruşu) içinde tamamlanmak zorundadır ve tamamlanır da (bir arıza yoksa). Dolayısıyla saat sinyalini (davul temposunu) ne kadar sıklaştırırsanız, bilgisayar o kadar hızlı çalışır. Elbette ki, teknik nedenlerle, saat hızı için bir üst sınır olacaktır.

Genellikle, saat hızının, bilgisayarın hızını belirleyen tek unsur olduğu düşünülür. BU NE YAZIKKİ YANLIŞTIR: Bilgisayarların hızı (performansı) saat devresinin hızıyla ÖLÇÜLMEZ.

Nedenini anlamak için şöyle bir hesap yapalım:

Diyelim ki, A marka M.İ.B ile üretilmiş olan bir bilgisayar iki tamsayıyı 10 saat sinyalinde (10 davul sesinde) çarpabiliyor ve bu bilgisayarın saati de 40 MHz hızında çalışıyor. Basitleştirilmiş ve hatalı bir düşünceyle, bu bilgisayarın saniyede 4,000,000 çarpma yapacağını hesaplayabiliriz.

(Düşüncemiz hatalı, çünkü bu günkü teknolojiyle bir saniyede 8,000,000 adet sayıyı, çarpılmak üzere bilgisayara aktaramayız).

Editör İmleç

0 - Kitap Hakkında 13

B marka M.İ.B ile üretilmiş bir bilgisayarsa, aynı çarpma işlemini 2 saat sinyali içinde tamamlayabiliyor olsun ve bu bilgisayar da 20 MHz saat frekansıyla çalıştırılsın. Yukarıdaki mantık gereği, bu ikinci bilgisayar saniyede 10,000,000 çarpma yapabilecektir. Yani, saat hızı iki misli yavaş olmasına karşın, ikinci bilgisayar birinciden 2.5 kez daha hızlıdır.

İşte, 33 MHz bir 80486 bilgisayarın, 33 MHz bir 80386 bilgisayardan hatırı sayılır bir oranla daha hızlı olmasının nedeni budur.

Farklı M.İ.B'lere sahip iki bilgisayarın hızlarını, saat frekanslarına bakarak karşılaştırmak KESİNLİKLE YANLIŞTIR.

Bilgisayar hızları MIPS, MFLOPS gibi birimlerle ölçülür. (Bu terimlerin tanımlarını izleyen sayfalarda bulabilirsiniz), Editor Bilgisayarlarda, estetik özelliği olmayan metinler hazırlamak için kullanılan programlardır. Genellikle program yazarken kullanılırlar.

(Kelime işlemciler ortada yokken bu programları kullanarak, olabildiğince estetik yazılar yazmaya çalışırdık, o başka).

MS-DOS ortamında tipik örnekleri EDIT, EDLIN, NORTON EDITOR isimli programlardır.

Cursor Klavyeden basacağınız bir karakterin, ekranın neresine yerleştirileceğini belirten, genellikle yanıp sönen bir eksi işaretine benzeyen özel karakterdir.

14

ARİTMETİK İŞLEMCİ Arithmetic Co-Processor ROM (Salt Oku Bellek) Read Only Memory

0 - Kitap Hakkında

Tanımların ikinci bölümü....

İlginizi çekmiyorsa, ''Bilgisayarın Kısa Tarihçesi'' isimli bölüme kadar olan kısımları okumadan atlayabilirsiniz.

Belki inanmayacaksınız ama, PC'lerde kullanılan Intel serisi Merkezi İşlem birimleri ondalıklı aritmetik işlemlerini doğrudan doğruya yapamazlar.

(Ondalıklı Aritmetik = "kayan noktalı aritmetik", İngilizcesi : Floating point arithmetic). Ondalıklı sayıları birer tamsayı gibi değerlendirip işlemi yaparlar ve ondalık noktasının yerini sonradan kararlaştırırlar. Daha doğrusu bütün bu işlemler, kullanılan programlama dilinin standart kütüphanesinde bulunan programlar tarafından yapılır. Tamsayı aritmetik işlemlerini birkaç mikrosaniyede (1 mikrosaniye = bir saniyenin milyonda biri) yapabilen merkezi işlem birimleri, ondalıklı sayılar üzerinde ancak milisaniyeler düzeyinde sürelerde yapabilmektedir. (1 milisaniye = 1 saniyenin binde biri). Toplam bir kaç bin işlem için (örneğin bir firmanın bilançosunun hesaplanması) bu süre farkları pek önemli olmayabilir; ancak mühendislik hesaplarında, çizim programlarında milyonlarca ondalıklı çarpma/bölme gerekmektedir. Bu nedenle işlemleri 10 kez bile hızlandırmak büyük bir başarı olacaktır. (Düşünün, 1 saatte tamamlanan bir program artık 5 dakikada tamamlanacak...)

Yüksek sayıda ondalıklı aritmetik gerektiren uygulamalar için Intel firmasının geliştirmiş olduğu yardımcı mikro işlemci ailesi 80287, 80387 gibi 7'yle biten model numaralarıyla anılmaktadır. 80486DX serisi hariç, PC lerde standart olarak Aritmetik İşlemci bulunmaz; gerektiği durumlarda sonrada takılır.

Bilgisayarı nı za Aritmetik İ ş lemci taktı rmanı z bilgisayarı nı zı hı zlandı rmaz! Yalnızca, bu yardımcı işlemcinin varlığını hissedebilen ve özelliklerinden yararlanabilen programların çalışması hızlanır. Bu yetenekte (daha doğrusu gereksinimde) olan program sayısı oldukça azdır. En başta gelen örnekleri AutoCAD teknik çizim programı, SAP4 statik hesap programı, LOTUS elektronik tablolama programıdır.

Intel 80486DX ailesinden merkezi işlem birimine sahip kişisel bilgisayarlarda aritmetik işlemci MİB'nin içine standart olarak yerleştirilmiş durumdadır.

Enerji kesintilerinden bile etkilenmeyen bellek devreleridir. Bu devrelere hiç bir zaman değişmeyecek olan program ve veriler kaydedilir. PC'lerde BIOS isimli sistem programları ROM tipi bellek devrelerine kaydedilmiştir.

Bu tip bellek devrelerine kayıt yapmak ya da kayıtlı bilgileri değiştirmek için özel cihazlar gerekmektedir. Tipik kapasiteleri 128 KiloByte'dır.

0 - Kitap Hakkında 15

ANA Bellek Main Memory YAN Bellek Secondary Storage KAŞE Bellek Cache Memory CD-ROM Magneto Optik

Disk

Çizici Plotter Tarayıcı Scanner Daha önce RAM olarak tanımladığım bellek tipidir. Çalışmakta olan programların ve bu programların kullandığı verilerin YALNIZCA gerekli olanların GEÇİCİ olarak saklandığı bellektir. Kullanılan programın çalışması tamamlandığında veya bilgisayar kapatıldığında ana bellekteki tüm kayıtlar kaybolur. Bir bilgisayarın ANA BELLEÐİNİN kapasitesi bilgi saklama kapasitesi değildir, çalıştırabileceği programların büyüklüğüyle ilgili kapasitesidir. Tipik RAM büyüklükleri 640 KiloByte, 1, 2, 4, 8, ve 16 MegaByte'dır.

Bilgisayarlarda, bilgileri kalıcı olarak saklamak için kullanılan bellektir. Günümüz teknolojisinde genellikle manyetik prensiplerle kayıt yapılan bu bellek tipine örnek olarak disk, disket, teyp, CD-ROM ve Magneto Optik diskler gösterilebilir.

Bilgisayarların çalışma hızlarını arttırmak için kullanılan özel bir bellek devresidir. Özel ve çok hızlı bellek devrelerinden üretilmiş olan bir ana bellek parçasıdır. Bilgisayarın program veya bilgi saklama kapasitesi ile bir ilgisi yoktur. Sadece 80386 ve daha yukarı modell bilgisayarlarda olabilirler. Tipik kapasiteleri 64 - 256 KByte'dır.

Müzik kaydında kullanılan Compact Disklerin bilgisayar dünyasında kullanılanlarıdır. Bu disklere yapılan sayısal kayıtlar hem çok uzun ömürlü olmakta hemde dağıtım açısından çok ucuza mal olmaktadır. CD-ROM sözcüğündeki ROM hecesi, Read Only Memory, yani ylnızca okunabilir bellek (salt-oku bellek) anlamındadır. Bir başka deyişle, bu ortamlara kayıt yapamazsınız (şimdilik elbette); ancak daha önce, fabrikasında yapılmış kaydı istediğiniz kadar okuyabilirsiniz. Tipik CD-ROM kapasiteleri 600,000,000 byte dolayında olduğundan hızla kitap yayıncılığında hızla yaygınlaşmaya başlamıştır. Bugün pek çok ansiklopedi CD-ROM üzerinde satın alınabilmektedir.

PC dünyasında, CD-ROM okuyabilen sürücüler, aynı zamanda müzik CD'lerini de okuyabilmekte, bu sayede PC'ler müzik seti görevini de üstlenebilmektedir. (Bu iş için bir de ses kartı gerekmektedir; bir masraf kapısı daha...)

Manyetik ve optik kayıt teknolojilerini birleştirerek üretilen, üzerine kullanıcı tarafından kayıt yapılabilen disklerdir. Henüz oldukça pahalı bir teknoloji olmasına rağmen, kayıt güvenlikleri çok yüksek olduğu için, değerli bilgilerin uzun süre saklanmasını gerektiren uygulamalarda yaygın olarak kullanılmaktadırlar. Tipik kapasiteleri 600 - 900 MegaByte'dır.

Genellikle renkli ve büyük ölçüdeki resimleri (A0, A1 gibi) kağıda aktarmak için kullanılırlar. Kalemli ve elektrostatik tipleri vardır.

Genellikle mühendislik bürolarınca proje çizim işlerinde kullanılırlar.

Resim ve fotoğrafların bilgisayar ortamına aktarılmasını sağlayan cihazlardır.

16

MODEM JOYSTICK MIPS MFLOPS Arabirim (Interface) RS-232 ve RS-422 Centronics 0 - Kitap Hakkında Birbirlerine uzak ( 500m - kıtalararası) bilgisayarları veya bilgisayarla terminallerin bağlantısını telefon hatlarıyla yapabilmek için kullanılan cihazlardır. Hattın her iki ucuna da yerleştirilen bu cihazlar bilgisayar veri kodlarını ses sinyallerine dönüştürüp, telefon hattıyla öbür bilgisayara ulaştırılmalarını sağlar ve öbür uçta tekrar ses sinyallerinden bilgisayar kodlarına dönüştürür. MOdulatör-DEModülatör kelimelerinden sentetik olarak üretilmiş bir sözcüktür. Telefon hattı üzerinden bilgi transfer hızları BAUD birimiyle ölçülür (saniyede gönderilen ya da alınan bit sayısı). Tipik transfer hızları 2400, 4800, 9600 ve 14400 Baud'dur.

Genellikle oyun programlarında, ekranda hareket eden nesneleri kontrol etmekte kullanılan bir çevre birimidir.

İngilizce Million Instructions Per Second sözcüklerinin baş harfleridir.

Bilgisayarın bir saniyede yerine getirebildiği makina komutlarının ortalama bir ölçüsüdür.

İngilizce Million FLOating Point Operations Per Second sözcüklerinin kısaltılmışıdır. Bilgisayarın bir saniyede yapabildiği ondalıklı aritmetik sayısının ortalama bir ölçüsüdür.

Bilgisayarın ana biriminin yan birimlerle (yazıcı, disk, teyp, modem, terminal gibi) bağlantısını sağlayan elektronik aksamlara verilen genel isimdir. Seri, Paralel ve Analog olmak üzere üç ana sınıfta tasarlanırlar. Seri arabirimler ucuz buna karşılık yavaş olurlar, paralel arabirimlerse tam tersi. Seri arabirimle yapılan bağlantılar 50-100 metreye kadar uzanabilir fakat paralel ve analog arabirimle yapılan bağlantılarda 4-5 metreden daha uzun kablo kullanılmamalıdır. Seri arabirimlere örnek olarak RS-232, RS-422, Klavye arabirimi gösterilebilir.

Centronics, SCSI, IDE gibi arabirimler, paralel arabirimlere, Composite ve VGA ise analog arabirimlere örnektir.

Genellikle yazıcı, modem ve terminal bağlantılarında kullanılan seri sınıfından arabirimlerdir. Karşılıklı bağlanan bilgisayar ve yan birim 300, 1200, 2400, 9600, 14400 karakter/saniye (Baud) gibi transfer hızlarıyla haberleşirler. Bu arabirimlerde kullanılan kablo uzunlukları tipik olarak 75 metreyle (RS232 için) sınırlıdır. RS-422 de bu sınır 500 metre dolaylarına çıkar. Haberleşen birimler eşit transfer hızına ayarlanmalıdır. Yazıcı bağlantılarında kullanılan paralel arabirimlerdir. Bilgi transfer hızları, karşılıklı olarak cihazların bilgi gönderme ve gönderilen bilgiyi işleme hızına bağlıdır.

SCSI IDE veya Embedded Kelime İşlemci Word Processor Elektronik Tablolama Spread Sheet

Bilgisayar

Destekli Tasarım Computer Aided Design

Bilgisayar

Destekli Üretim Comp.Aided Manufacturing Windows Veri Tabanı Database Derleyici Compiler Turbo 0 - Kitap Hakkında 17 Orta ve büyük boy bilgisayarlarda kullanılan disk, teyp, tarayıcı, CD-ROM sürücülerinin bağlanmasında kullanılan arabirimdir. Kapasitelerin ve hız gereksinimlerinin hızla arttığı PC dünyasında da yaygın olarak kullanılmaya başlanmıştır.

Şimdilik yalnızca PC dünyasında kullanılmakta olan ucuz ve makul hızda bir disk arabirimidir.

Sayfa üzerindeki yerleşimleri de dikkate alarak metin düzenleme işinde kullanılan programlara verilen genel addır. Örneğin, bu kitabın tamamı bir kelime işlemciyle yazılmış ve baskıya hazırlanmıştır.

MS-DOS ortamındaki tipik örnekleri MoonStar (Türkiye'de geliştirilmiştir), WordStar, WordPerfect, Word, Word for Windows, Professional Write gibi programlardır.

Program yazmaksızın hesap yapmak için kullanılan programlardır. En geniş uygulama alanı bankacılık, finans, maliyet hesabı, muhasebe gibi iş uygulamalarıdır.

MS-DOS ortamında tipik örnekleri Lotus 123, SuperCalc, Excel, QuattroPro gibi programlardır.

Mühendislik ve mimarlık alanlarında kullanılan, teknik çizim ve simülasyon çalışmalarını kolaylaştıran programlara verilen genel addır.

Tipik örnekleri AutoCAD, MicroCAD, MicroStation gibi programlardır.

Bilgisayar ekranında tasarımı tamamlanan bir ürünün kendisini veya modelini, gene bilgisayar kontrolundaki robot veya numerik kontrollu tezgahlarla üretmek için kullanılan program ve sistemlerdir.

Microsoft firmasının PC dünyasına, MS-DOS'dan sonra en önemli armağanlarındandır. Her türlü işlemin grafik olarak yürütüldüğü ve bir bilgisayarın, sınırlı da olsa, bir anda birden fazla iş yapabilmesine olanak sağlayan bir altyapı programıdır.

Zaman içinde biriken büyük hacımlı bilgi kayıtlarını düzenlemekte ve bunlar arasında belirli özelliğe sahip olanlarını bulup çıkarmakta kullanılan program paketlerine verilen genel isimdir. Tipik örneklerin başında dBase gelmektedir. Neredeyse programlama dili özelliklerine sahip olacak kadar gelişmiş olan veri tabanı uygulama programları, PC kullanımının yaygınlaşmasını sağlamış olan önemli uygulamalardır.

Herhangi bir programla diliyle (FORTRAN, BASIC, COBOL, PASCAL gibi) yazılmış programları makina diline çeviren destek programlarıdır.

Genellikle her PC'nin ön panelinde Turbo etiketli bir düğme bulunur. Bu düğmeye her basışınızda bilgisayarın hızı bir artacak bir azalacaktır.

Genellikle oyun programlarında, güçlü PC'lerin hızını düşürerek oyunu kolaylaştırmak için kullanılır. (Yoksa kim niye bilgisayarının yavaş çalışmasını istesin ki ?)

18

0 - Kitap Hakkında

Multimedya Multimedia Debug / Bug ASCII Veri, ses ve video bilgilerinin bilgisayar ortamında birlikte kullanılmasıdır. Multimedya sayesinde PC ortamında sesli ansiklopediler, etkileşimli (interactive) tanıtım ve eğitim programları günlük hayatımıza girmiştir.

Bilgisayar programcıları arasında oldukça sık kullanılan terimlerdir. Tam karşılıkları BÖCEK ve BÖCEKTEN ARINDIRMA'dır. Bir programın umulmadık noktalarında hatalar varsa ve program zaman zaman yanlış çalışıyorsa, o programda BUG (Böcek) bulunduğuna ilişkin cümleler kullanılır. Bu hataların bulunarak düzeltilmesi sürecine DEBUG adı verilir. Bu deyimin bilgisayar terminolojisine girmesinin hikayesiyse oldukça ilginçtir :

MARK II elektromekanik bilgisayarı için 1950 li yıllarda program geliştiren Grace Hopper isimli ünlü kadın programcı, hatalı çalışan programındaki problemi bir türlü bulamamaktaydı. Uzun aramalar sonucunda, bilgisayarın röleleri arasında sıkışmış kalmış bir böcek ölüsünün bütün sorunların kaynağı olduğu anlaşılmıştı.

Kişisel bilgisayarlarda kullanılan standart bir kodlama sisteminin adıdır.

Harf, noktalama işaretleri ve rakamların bilgisayarın bellek ve diğer çevre birimleri üzerinde saklanırken kullanılacak, ikili sayı sistemindeki kodlanmış durumlarını belirler. ASCII kodlama tablosunun tamamını Ek-2 de bulabilirsiniz.

Karakter ASCII Kodu Karakter ASCII Kodu

0 00110000 1 00110001 2 00110010 3 00110011 4 00110100 ... ...... A 01000001

B 01000010 C 01000011 D 01000100 E 01000101 ... ......

---
*Kaynak: `KİM KORKAR BİLGİSAYARDAN/Kim korkar hain bilgisayardan.pdf`*
