# Bellek Türleri

## ***Statik ve Dinamik Modüllerin Farkları:***

**SRAM****:** ***Static Random Acces Memory ***olarak adlandırılır. Bu RAM modülünde her bit için iki transistor kullanılır. Burada devreye akım sağladığı müddetçe bilgiler kaybolmaz. İki transistorun kullanılmasının sebebi ise ikinci transistorun birinci transistorun çıkışını kontrol etmesidir. SRAM’ ler 20 nanosaniyelik bir hıza sahiptir. Pipelined Burst SRAM olarak adlandırılan yeni türler ise 4.5 – 8 nanosaniyelik hızlara sahip olmaları ile birlikte 133 Mhz bir frekans hızında çalıştırılıyor. SRAM’ de 3-1-1-1 zamanlaması kullanılır. ***Yani bellekten herhangi bir adrese ulaşmak için geçen zaman 3 olarak gösteriliyor. Adrese ulaştığında adres için de bilgilere ulaşmak için ayrı bir zaman gerekiyor o da 1 olarak gösterilir. *** 66 Mhz’ lik sistemlerde 3-2-2-2 zamanlaması tercih edilir. Neticede SRAM hızlı ve pahalı olmasından dolayı genellikle cache bellek olarak kullanılır.

**DRAM:** Dynamic RAM her bir bit için tek bir transistor kullanır. SRAM’ a göre daha ucuzdur. Bunun nedeni daha az sayıda transistor ile çalışma ve karmaşık bir yapı içermemesidir. Bu bellek modülünde çok basit bir teknik kullanılır. Transistordan akım geçtiğinde bilgi 1 değerini alır. Tersi bir durumda ise bilgi 0 değerini alır. Yalnız bu süre çok kısa olduğu için transistorun sürekli olarak tazelenmesi gerekiyor. SRAM’ e göre kıyaslandığında DRAM yavaş kalıyor. DRAM’ ler genellikle bellek chip’ lerinde kullanılır. Üzerindeki numaralarla bu ürünlerin hızlarını belirliyor. Burada sayının küçük olması belleğin hızlı olması anlamına geliyor. Yalnız dikkat dilmesi gereken bir konu ise aynı sistemde kullanılacak bellek chip’ lerinin aynı hızlara sahip olması. Aksi taktirde sistemde ciddi performans kayıpları meydana gelir.

## ***Ram Modüllerin Çalışma Mantığı:***

İşlemciler işlemlerini bellekler aracılığı ile gerçekleştirirler. Burada belleğin görevini bir not defteri olarak düşünebiliriz. Yani yapılacak işler ilk önce belleğe aktarılır. Sonraki iş ise bilgileri saklamak amacı ile sabit diske kayıt etmek. Bilgisayar kapatıldığında bellekteki bilgilerde otomatik olarak silinecektir. Sabitdiske aktarılan bilgiler bilgisayar kapatıldığında bile bilgi kaybolmayacaktır. Buna karşın sistem, bellekteki bilgilere sabitdiske göre daha hızlı erişebilir.

## ***RAS ve CAS:***

**Bellekteki Bilgilerin Okunması:**

Bellek modüllerinin içinde birden fazla adres yolu bulunur. Bu adres yolları istenilen bilgileri bellek üzerinde aktarırlar. Satırlar RAS (Row Access Signal), sütunlar ise CAS (Column Access Signal) sinyalleri ile uyarılırlar. Bellek, onay sinyalini aldığında istenilen bilgileri satırlar halinde BUS’ a yollar. Bu bilgi yollama işlemi bir STOP sinyali alınıncaya kadar devam eder. Bilgileri BUS’ a yollamanın avantajı tek tek yerine satırlar halinde yollayarak önemli ölçüde zamana kazanmaktır.

## ***Bellek Yuvaları:***

**SIMM: **Single Inline Memory Module, bellek modüllerini bir arada tutmak için kullanılan bir paketleme şekli. İlk SIMM’ ler 30 pin olarak piyasaya sürülmüştür. Daha sonra pin sayısı 72’ ye yükseltilmiştir. Pentium sistemler 32 bit’ te çalıştıkları için SIMM’ lerin ikişerli gruplarda kullanılması gerekiyordu. Bunun en büyük nedeni Pentium sistemlerin 64 bit’lik bir data BUS’ ı kullanmalarıdır. SIMM yuvalarda modüller hafif eğik olarak dururlar.

**DIMM: **Dual Inline Memory Module’ ler 168 pin’ lik modüllerden oluşur. 64 bit’ lik iletişim sağlayabildikleri için tek başına kullanılabilirler. Günümüzde en yaygın olan bellek modülü 3.3 voltluk DIMM’ lerdir. DDR uyumlu DIMM yuvalarında ise 2.5 volt kullanılır. SDRAM ve DDR RAM yuvalarının aynı pin sayılarında olmalarına rağmen, her birinin kendisine ait yuvasının olduğu unutulmamalıdır. DIMM’ ler yuvalarına dik olarak takılırlar.

**RIMM: **184 pin’ lik RAMBUS sistemlerin en önemli özelliği ise modüllerin seri çalışmasıdır. Burada sinyal bir chip’ ten diğerine iletiliyor. Sinyalin kesilmemesi için bellke yuvalarının dolu olması gerekiyor. Bu yüzden anakartlarla birlikte RAM modülüne benzeyen ama üzerinde chip bulunmayan bir modül veriliyor. Bir kanalda bulunabilen maksimum chip sayısı 32 ile sınırlıdır. RIMM yuvalarına belekler dik olarak takılır.

## ***BELLEK TÜRLERİ***

**ROM:**** **Rom bellek anakart BIOS’ larında yer alırlar. Eskiden BIOS, EPROM’ da (Electrically ProgRAMmable Read Only Memory) yazılırdı. EPROM ile BIOS yazmak o kadar değildir. Onun için özel bir cihaza ihtiyaç duyulurdu. Silme işlemi de mor ışıklarla yapılırdı. BIOS’ u değiştirmek için önce sistemden EPROM’ u çıkarmak gerekir. Mor ışığın altında tutulduğunda bilgi silinir ve özel bir cihazla da EPROM yeniden programlanır. Günümüzde flash bellekler kullanılmaktadır. Flash belleklerde ise silme işlemi elektrik sinyalleri ile yapılır ve programlamak için ekstra bir cihaza ihtiyaç duyulmaz. Örnek olarak BIOS yeni bir sürümü ile değiştirilmek istendiğinde yeni BIOS diskete yüklenir ve özel bir yazılım yardımıyla yenilenir.

**CMOS:** Bir başka RAM türü ise CMOSRAM’ dir. Complementary Metal Oxide Semiconductor olarak adlandırılan bu tür, sistem bilgilerini üzerinde barındırır. Verilerin silinmemesi için anakartta bulunan pilden kendisini besler. Bilgisayarın bazen konfigürasyonunu unutmasının sebebi CMOS’ un pilden beslenmemesinden kaynaklanır. RAM bellke ile yanı özellikte olan bu tür, pil ile entegre bir devrede bulunur. BIOS üzerinde yapılacak bir değişiklik esnasında CMOS devreye girer ve bilgileri kaydeder.

**CACHE :** Bilgisayar teknolojisinin çook hızlı bir şekilde gelişmesi, ayrıca günümüz yazılımlarının daha ayrıntılı ve komplike hale gelmesi, bellek ihtiyacını da önemli ölçüde arttırıyor.bu yüzden daha büyük bloklara daha az zamanda bilginin yazılması gerekiyor. durum bu şekilde olunca cache belleğin önemi ortaya çıkıyor. Pentium öncesi işlemcilerde 8K boyutunda cache bellekler kullanılıyordu. Bu bellkeler işlemcinin sıkça kullanıldığı bilgileri sistemin belleğine gitmeden okuyorlardı. 2. seviye cache bellek yani Level-2-Cache ortaya çıktığında bir önceki örnek Level-1-Cache olarak adlandırıldı. İşlemcilerin gelişmesi ile birlikte bu bellekler de önemli ölçüde artmıştı. P II işlemcilerle birlikte cache belleklerde bir değişime uğradı. Öyle ki günümüzde 256K ile 2048K arasındaki büyüklüklerde cache bellekler bulunuyor. Cache bellekler sistem belleklerinden önce bir yedekleme yaparak sistem performansını arttırıyorlar.

**VRAM:** Video görüntülerini hızlı bir şekilde işlemek ve aktarmak için kullanılan bir bellek türüdür. DRAM’ lerde tek bir giriş/çıkış bulunur. Dolayısıyla iki ayrı birim aynı anda belleğe erişemez. VRAM’ lerde ise iki ayrı giriş/çıkış mevcuttur. Bu sayede görüntü bilgisini oluşturmak için bir devre ve oluşturulan bilgileri monitöre yollamak için farklı bir devre kullanılabilir. DRAM hücrelerinde toplam bilgi akışı bant genişliği bandwich olarak adlandırılır. Yalnız VRAM’ in sahip olduğu çift port, bant genişliğini ikiye katlamak yerine sadece biraz daha arttırıyor. Bant genişliğinin yüksek olması, yalnız yüksek çönürlükteve çok sayıda rengin söz konusu olduğu durumlarda geçerli. Düşük çözünürlüklerde VRAM’ in ekstra bant genişliği çoğu durumlarda kullanılmaz.

**WRAM :** Windows RAM bellekleri, VRAM belleklerinin daha gelişmiş bir çeşididir. WRAM lere eklenen ek bellekler aracılığı ile bazı özel görüntü fonksiyonlarının daha hızlı gerçekleştirilmesi sağlanır. Bu devreler özellikle animasyon işlerinde yüksek performans sağlar. Diğer işlerde belirgin bir üstünlük göstermez. WRAM bellekler Matrox görüntü kartlarının bazı modüllerinde bulunuyorlar.

**SGRAM :** Synchronous Graphics RAM, SDRAM’ in grafik tabanlı işler için geliştirilmiş halidir. SGRAM, verileri tek tek yerine blok halinde alıyor ve işliyor. Bu sayede okuma ve yazma performansı önemli ölçüde artıyor. Dolayısıyla grafik kartının performansı da doğru orantıda etkileniyor.

**SDRAM :** Synchronous DRAM adını taşıyan bu bellek türü, sistem frekansı ile senkronik bir şekilde çalışıyor. İşlemcinin sahip olduğu sistem, saat frekansı ile belleğin çalışma frekansının birbiri ile eşit çalışması için ayarlanmıştır. Bu sayede belleğe giden komutlarda bir hızlanma ve sistem performansında bir artış gözlenir. SDRAM bellekleri günümüzde en yaygın olarak kullanılan modüllerdir. Bu modüller 3 türden oluşur;

PC66

PC100

PC133

Buradaki sayılar bellek modüllerinin çalışma frekansını belirler. Örneğin PC66 FSB hızı 66 MHz olan sistemler için tasarlanmış bir bellek türüdür. PC133’ ler PC100’ lerin yerini almaya başladılar. Bunun en önemli nedeni iki model arasında fiyat farkının olmaması ve PC133’ lerin daha düşük FSB’ li sistemlerde çalışabilmesidir.

**DDR-RAM :** Double Data Rate olarak adlandırılan bu bellek türü bazı çevreler tarafından SDRAM II olarak adlandırılır. Bu bellek türü ilk olarak Nvidia’ nın Geforce chip’ li ekran kartlarında ortaya çıkmıştır. DDR-RAM, SDRAM’ in geliştirilmiş versiyonu olarak tanımlanır. Bu bellek türünde çalışma frekansı çok daha yüksektir. Örneğin ekran kartlarının sahip olduğu 150 MHz çalışma frekansı bu bellek türü kullanıldığında 300 MHz’ ye çıkar. Piyasada bu türe ait iki türü vardır. Bunlardan 100 MHz hızında çalışan PC200 diğeri 133 MHz hızında çalışan PC266’ dır.

**RAMBUS :** RDRAM, Concurrent ve Direct RDRAM olmak üzere 3 değişik üründen oluşmaktadır. DDR SDRAM modüllerinde olduğu gibi RDRAM’ de düşen ve yükselen frekans değerlerini veri iletişimi için kullanır. Burada 8 bit’ lik bant genişliği sayesinde 400 MHz’ lik bir çalışma frekansı elde eder. DDR-SDRAM ve SDRAM bellek modülleri buna karşın 64 bitlik bir bant genişliğine sahiptir.

Concurrent RAMBUS, RDRAM modüllerinin daha gelişmiş bir türüdür. Bu modülde küçük ver bloklarının hızlı bir şekilde iletilmesi için bir protokol yer alır. Concurrent RAMBUS 600 MHz’ lik bir çalışma frekansı ile 600 Mb’ lik bir veri transferi gerçekleştirebiliyor. Direct RAMBUS teknolojisi diğerlerine göre daha yüksek bir transfer oranına sahiptir. Direct RAM’ ler diğer modüller gibi aynı sinyal tipine sahip olmasına karşın 16 bit’ lik bir RAMBUS kanalı ile 800 MHz’ lik bir frekansla çalışır. Bu durumda tek bir Direct RAM saniyede 1.6 Gbyte’ lik bir orana ulaşır. Uyumlu bir anakartta 4 adet yuva olduğu düşünülürse maksimum bat genişliği 6.4 Gbyte/saniyeye ulaşır.

## **- PAGE 1-**

---
*Kaynak: `BELLEK TÜRLERİ/BELLEK TURLERI.doc` — Ahmett — 2004*
