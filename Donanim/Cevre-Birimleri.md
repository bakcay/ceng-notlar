# Çevre Birimleri

Selçuk Üniversitesi

Mühendislik Mimarlık Fakültesi

Bilgisayar Mühendisliği Bölümü

## VE

## ÇEVREBİRİMLERİ

**Uzm. İbrahim KORANA**

**İÇİNDEKİLER**

**1. İntel 8086/8088 Mikroişlemci **

**1.1 Pin Bağlantıları **

**2. CLOCK GENERATOR (8284A) **

**2.1 Pin Fonksiyonları **

**2.2 8284A'nın çalışması **

***2.2.1 Clock Bölümünün Çalışması ***

***2.2.2 Reset Bölümünün Çalışması ***

**3. BUS HATTINDA BUFFER VE LATCH OLAYI **

**3.1 Bus Hatlarının Demultiplex Edilmesi **

***3.1.1 8088'in Demultiplex Edilmesi ***

***3.1.3 8086'nın Demultiplex Edilmesi ***

**3.2 Sistemin Bufferlanması **

***3.2.1 Tamamen bufferlanmış 8088 ***

***3.2.2 Tamamen bufferlanmış 8086 ***

**3.3 BUS ZAMANLAMASI **

***3.3.1 Bus Hatlarının Çalışmasının Temeli ***

***3.3.2 Genel Olarak Zamanlama İşlemleri ***

***3.3.3 Okuma Zamanlaması ***

**3.4 READY(HAZIR) VE WAIT STATE (BEKLE) DURUMLARI **

***3.4.1 READY Girişi ***

***3.4.2 RDY ve 8284A ***

**3.5 MİNİMUM MODA KARŞILIK MAKSİMUM MOD **

***3.5.1 Minimum Mod İşlemi ***

***3.5.2 8288 Bus Kontroller ***

**4. BELLEK ARABİRİMİ **

**4.1 Bellek Arabirimleri **

***4.1.1 Bellek Pin Bağlantıları ***

**4.2 ROM BELLEK **

**4.3 STATİK RAM ELEMANLARI **

**4.4 DİNAMİK RAM BELLEK **

**4.5 ADRES DEKODE EDİLMESİ **

**4.6 8088 BELLEK ARABİRİMİ **

***4.6.1 Temel 8088 Bellek Arabirim ***

***4.6.2 8088’e EPROM Arabirimi Oluşturması ***

***4.6.3 8088'e RAM Arabirimi Oluşturma ***

***4.6.4 Bellek Hata Dedeksiyonu için Parity: ***

***4.6.5 8086, 80286 ve 80386SX Bellek Arabirimi Oluşturma ***

**4.7 DRAM Kontrol Elemanları **

**5. TEMEL I/O ARABİRİMİ **

**5.1 I/O Komutları **

**5.2 İzole edilmiş ve Memory- Mapped I/O **

***5.2.1 İzole Edilmiş I/O ***

***5.2.2 Memory-mapped I/O ***

**5.3 PC I/O Haritası **

**5.4 TEMEL GİRİŞ/ÇIKIŞ ARABİRİMLERİ **

***5.4.1 Temel Giriş Arabirimi ***

***5.4.2 Temel çıkış Arabirimi ***

**5.5 Handshaking **

**5.6 I/O Port Adresi Dekod Etme **

***5.6.1 8 bit I/O adreslerinin dekod edilmesi ***

***5.6.2 16 bit I/O adreslerinin Dekod edilmesi ***

***5.6.3 8 ve 16 bit I/O portları ***

**5.7 8255 (PPI) **

**5.8 8279 Proğramlanabilen klavya ve display sürücü **

***5.8 1 DISPLAY ***

***5.8. 2 KEYBOARD ***

**5.9 8253/8254 COUNTER **

**1. İntel 8086/8088 Mikroişlemci**

**Bu bölümde 8086 ve 8088 mikroişlemcilerinin her ikisinin de pin fonksiyonlarını anlatacak ve clock üretimi, bus hatlarındaki buffer ve lach işlemleri , zamanlama, bekleme durumları ve minimum moda karşılık maximum mod işlemleri gibi bundan sonra antatılacak donanım konuları hakkında bilgi verilecektir.**

**Mikroişlemciye bağlanacak veya onunla arabirim oluşturacak elemanlarda önce pin fonksiyonlarının ve zamanlamayı anlamak gerekir. dolayısiyle bu kitabın daha sonraki bölümlerinde bulunan bellek ve IO arabirim elemanlarını tam olarak anlamak için bu bölümdeki bilgiler temeldir.**

***1.1 Pin Bağlantıları***

**AD7-AD0 (8088) Adres/Data Bus **

**8088'in hem adres bus hattı hem de data bus hattı olarak kullanılmaktadır. ALE'nin lojik 0 veya lojik 1 olmasına bağlı olarak bellek adresnin veya I/O pot numarasının en düşük değerlikli 8-bitini içerm ektedir. Bu pinler mikroişlemci hold durumunda iken (Bilgisayar hold durumunda iken bazı işlemlerini yerine getiremez.) adres/data bus hattı yüksek empedans gösterir.**

**A15-A8(8088) Adres Bus **

**Bus çevrimi süresince işlem gören bellek adresinin en yüksek değerlikli 8-bitini (bu 8-bite upper denir) gösterir. Mikroişlemci hold durumunda iken bu hatlar yüksek empedans gösterir.**

**AD15-AD7 (8086) Adres/Data Bus **

**Bu hatlar 8086 üzerindeki adres/data bus hattının multiplex edilmiş upperını (yüksek değerlikli 8-biti) içerir. Bu hatlar ALE ucu lojik 1 iken A15-A8 adres bitleri ve lojik 0 iken D15-D8 data bus bitleri ni içerir. Bu pinler mikroişlemci hold durumunda iken yüksek empedans gösterir.**

**A19/S6, A18/S5, A17/S4, A16/S3 Adres/Durum Bus **

**Bu pinler A19-A16 Adres bitlerini ve de S6-S3 durum bitlerini içerir. Bu pinler de mikroişlemci hold durumunda iken yüksek empedans gösterirler. S6 durum biti daima lojik 0 değerinde kalırken, S5 biti IF (İnterrapt Flag biti) 'nin durumunu ve S4 ve S3 ise o andaki bus çevrimi sırasında erişilecek segmenti gösterir. Aşagıdaki Tablo S4 ve S3'ün doğruluk tablosunu temsil etmektedir. Bu iki durum biti dört tane biribirinden ayrı bellek birimini adreslemek içi n kullanılabilir.**

| **S4****** | **S3****** | **Fonksiyon****** |
| --- | --- | --- |
| 0 | 0 | Extra Segment |
| 0 | 1 | Stack Segment |
| 1 | 0 | Code Segment veya Segment Yok |
| 1 | 1 | Data Segment |

**RD Oku **

**RD pini lojik 0 iken data bus sisteme bağlı olan I/O birimlerinden ve bellekten bilgi okur. Bu pin yüksek empedansa mikrişlemci hold durumunda iken girer. **

**6. READY Hazır**

**INTR İnterrupt Talebi **

**INTR donanımın interrupt istekleri için kullanılır. IF lojik 1 iken INTR 1 yapılırsa o sırada yürütülen komutun icrası tamamlandıktan sonra 8086/8088 interrupt isteğini kabul eder ve alındı bildirimini y apar. (INTA aktif yapılır.)**

**TEST Test **

**WAIT komutu tarafından test edilen bir giriş pinidir. Eğer TEST pini Lojik 0 ise WAIT komutu NOP olarak işler. Eğer TEST lojik 1 ise o zaman WAIT komutu TEST komutunun lojik 0 olmasını bekler. Bu pin gen elde 8087 yardımcı sayısal işlemciye bağlanır. **

**NMI Maskelenemeyen İnterrupt Girişi **

**INTR ile benzer olmakla birlikte IF flag bitinin lojik bir seviyesinde olup olmadığına bakmaksızın işlem yapar. NMI aktif yapılırsa bu interrupt girişi vektör 2'yi kullanır. **

**RESET Reset **

**Bu pin 4 clock darbesi boyunca lojik 1 seviyesinde tutulursa mikroişlemcinin kendi kendini resetlemesine sebep olur. 8086/8088 resetlendiği zaman mikroişlemci FFFF0H bellek yerinden itibaren komutların yürütülmesine başlar ve sırada bekleyen interrupt taleplerini IF flag bitini lojik 0 yaparak etkisiz hale getirir. **

**CLK Clock **

**Mikroişlemci için temel zamanlama ögesidir. Clock sinyali görev çevriminin %33'dür. (Clock peryodunun 1/3'ünde high ve 2/3'ünde ise low'dur.)**

**Vcc Güç Kaynağı **

**Vcc girişi **±** %10 toleransla +5V'u sağlar. **

**GND Şase **

**Güç kaynağı için geri dönüş yoludur. Görüldüğü gibi her iki mikroişlemci için GND olarak isimlendirilmiş iki tane pin vardır. **

**MN/MX Minimum/Maximum Mod **

**Mikroişlemci için minimum mod yada maximum modlardan birini seçmek için kullanılır. Minimum mod seçildiyse MN/MX direkt olarak +5V'a bağlanır. **

**BHE/S7 Bus High Enable **

**Bu pin 8086 mikroişlemcisiyle yapılan okuma yada yazma işlemleri sırasında data bus'ın en anlamlı bitlerinin (D15-D8) kullanılmasını sağlar. S7'nin durumu lojik 1'dir. **

**Minimum Mod Pinleri **

**8086/8088 mikroişlemcileri için mimimum mod işlemcileri için MN/MX direkt +5V'a bağlanarak yapılır. Pin +5V'a bir pullup direnciyle bağlanamaz.**

**IO/M(8088), M/IO(8086) Bellek Giriş/Çıkış **

**Hem bellek hem de I/O adreslerinin bulunduğu Mikroişlemci adres bus hattındaki bellek yada I/O'yu gösteren bir pindir. Mikroişlemci hold durumunda iken yüksek empedans göste****rir. **

**WR-Write **

**8086/8088 'nın bellek yada I/O birimleri için data çıkışını gösteren bir strobdur. Bu pin Mikroişlemci hold durumunda iken yüksek empedans durumuna geçer. **

**INTA-Interrupt kabul edildi **

**INTR giriş pininden sorumludur. INTA pini genelde data üzerindeki interrupt isteklerinden sorumlu olan inrerrupt vektöre bir kapı olarak kullanılır.**

**ALE-Adres Latch Enable **

**8086/8088 adres data bus hattının adres bilgileri içerdiğini gösterir. Bu adres bellek yada I/O port numarası olabilir. Mikroişlemci hold durumunda iken bu pinin sinyal vermediğine dikkat edilmelidir. **

**DT/R Data Transmit(gönderme)/Receive(alma) **

**Mikroişlemcinin veriyi aldığını veya verdiğini gösterir. Bu sinyal harici data bus bufferlarını etkin hale getirmek için kullanılır. **

**DEN-Data Bus Enable **

**Harici data bus bufferlarını etkin hale getirmek için kullanılır.**

**HOLD-Hold **

**Direkt belleğe erişme isteğidir. HOLD lojik 1 ise mikroişlemci yazılım yürütme işlemini durdurur ve adres, data ve kontrol bus hatları yüksek empedans durumuna geçerler. Eğer HOLD lojik 0 seviyesinde ise mikroişlemci yazılımını normal olarak yürütür.**

**HLDA-Hold Acknowledge(Hold isteği kabul edildi) **

**8086/8088'in HOLD durumuna geçtiğini gösterir.**

**SS0 (8088) **

**Mikroişlemci max modda çalışırken kullanılan S0'a eşdeğerdir. Bu sinyal IO/M ve DT/R ile birleştirilerek o andaki bus çevriminin yaptığı işlevi decode etmek için kullanılır. **

**Maximum Mod Pinleri**

**Max mod durumunu sona erdirerek dış yardımcı işlemcileri kullanmak için MN/MX pini şaseye bağlanır. **

**S2,S1 ve S0 Durum Bitleri **

**O andaki bus çevriminin işlevini gösterir. Bu sinyaller daha sonra anlatılacak olan 8288 Bus Kontroler tarafından decode edilir. **

**RQ/GT0 ve RQ/GT İstek/Verme **

**Bu pinler DMA ile max mod durumunda haberleşmek için kullanılır. Her ikisi de çift yönlüdür. ve DMA işlemlerinde bilgi okumak yada bilgi vermek için kullanılır**

**LOCK Lock **

**Sistemin çevre birimlerle irtibatını kesen bir çıkıştır. Herhangi bir komuttan önce LOCK kulanılarak aktif hale getirilir. **

**QS1 ve QS0 Kuyruk(dizi) Durumları **

**İç komut dizilerinin durumunu gösterir. Bu pinler nümerik işlemci tarafından erişim için kullanılır. **

**2. CLOCK GENERATOR (8284A)**

**Bu bölümde 8086/8088 mikroişlemci için RESET ve READY sinyallerini üreten 8284A clock generatorünü tanıyacağız. **

**8284A 8086/8088 mikroişlemcilerini tamamlayan elemandır. Clock generatoru olmadan eklenen devrelerin çoğu 8086/8088 temelli sistemlerde clock üretmeye ihtiyaç duyarlar. 8284A şu temel fonksiyon ve sinyalleri sağlar: Clock üretme, reset senkronizasyon, TTl seviyesinde clock çıkış sinyalleri . Aşagıda 8284A'nın pin çıkışlarını göstermektedir.**

**BURAYA 8284A NIN ŞEKLİ YERLEŞTİRİLECEK**

***2.1 Pin Fonksiyonları ***

**8284A 8086/8088 mikroişlemcileri için özel olarak dizayn edilmiş 18 pinli bir entegredir. **

**AEN1 ve AEN2 Adres Enable **

**RDY1 ve RDY2 olarak adlandırılan bus hazır sinyalleri, sırasıyla, bu pinler tarafından sağlanır. RDY1 ve RDY2 girişleriyle bekleme durumlarını sağlayan bu iki pinin kullanımı daha sonraki bölümlerde anl atılmıştır. Bekleme durumları bu iki pin tarafından kontrol edilen 8086/8088 mikroişlemcilerinin READY pini tarafından sağlanır. **

**RDY1 ve RDY2- Bus Hazır **

**8086/8088 temelli sistemlerde AEN1 ve AEN2 pinlerinin bağlantularıyla bekleme durumlarına sebep olan girişleri sağlarlar. **

**ASYNC Hazır Senkronizasyon Seçme **

**RDY1 ve RDY2 girişleri için senkronizasyonun bir yada iki evresinden herbirini seçmekte kullanılan bir giriştir. **

**READY Hazır **

**Bu çıkış pini 8086/8088'in READY giriş pinine bağlanır. Bu sinyal RDY1 ve RDY2 ile sekronize edilir. **

**X1 ve X2-Krisral Girişleri **

**Clock generator ve onun tüm fonksiyonları için zamanlama kaynağı olarak kullanılan harici kristalin bağlantı uçlarıdır.**

**F/C-Frekans/Kristal **

**8284A için clock kaynağını seçer. Eğer bu pin high konumuna getirilirse EFI giriş pinine harici bir clock sağlanır. Eğer lojik 0 ise iç osilator zamanlama sinyalini sağlar.**

**EFI-Harici Frekans Girişi **

**F/C pini lojik 1'e çekildiğinde kullanılır. F/C 1 ise EFI bir zamanlama kaynağıdır.**

**CLK-Clock **

**8086/8088 mikroişlemcilerin ve sistemdeki diğer sinyallerin CLK giriş sinyallerini sağlayan çıkış pinidir. CLK pini kristal veya EFI giriş frekansının 1/3' ne sahip ve 8086/8088'in ihtiyacı olan %33' l ük impuls-peryot oranına sahip bir çıkıştır. **

**PCLK-Çevresel Clock **

**Kristal veya EFI giriş frekansının 1/6 'ı olan ve impuls-peryot oranı %50 olan bir sinyaldir. PCLK çıkışı sistemdeki çevre birimlere clock sinyalini sağlar. **

**OSC-Osilatör Çıkışı **

**Kristal veya EFI ile aynı frekansı sahip olan ve TTl seviyesinde bir sinyaldir. OSC çıkışı çoğullamalı işlemcili sistemlerde bulunan diğer 8284A clock generatorlarının EFI girişlerini sağlarlar. **

**RES Reset Girişi **

**8284A'nın low durumunda aktif olan girişidir. Bu pin çoğunlukla ilk enerji verildiğinde resetlemeyi sağlamak için RC ile bağlanır. **

**RESET-Reset Çıkışı **

**Bu sinyal 8086/8088 'in RESET girişine bağlanır. **

**CSYNC-Clock Senkronizasyon **

**Çoğullamalı işlemcili sistemlerde EFI girişi senkronizasyonu sağlıyorsa bu pin kullanılır. Eğer iç kristal osilatörü kullanılırsa bu pin şaseye bağlanmalıdır. **

**GND-Şase **

**Bu pin şaseye bağlanır.**

**Vcc-Güç Kaynağı Girişi **

**Bu pin toleransı **±** %10 olan +5V'a bağlanır.**

***2.2 8284A'nın çalışması***

**8284A nisbeten anlaşılması kolay bir enteğredir. Aşagıda 8284A Clock generatorunun iç lojik diyagramını vermektedir. **

**8284 ün iç diyagramı yerleştirilecek**

**2.2.1 Clock Bölümünün Çalışması **

**Lojik Diyagramın üst yarısı clock ve reset senkronizasyonunu temsil etmektedir. Diyagramda gösterildiği gibi kristal osilatörün X1 ve X2 adı altında iki girişi vardır. Eğer kristal X1 ve X2 uçlarına bağlıysa, osilatör kristal ile aynı frekansa sahip bir kare dalga sinyal üretir. Kare dalga sinyal bir AND kapısını ve de OSC çıkış sinyalini veren bir invert edici bufferı sürmektedir. OSC sinyali ise diğer 8284A'ların EFI giriş sinyallerini sağlar. AND kapısı kullanarak F/C girişi lojik 0 olduğu zaman kristal frekansı 3'e bölücüye ulaşır. Fakat F/C lojik 1 ise EFI sinyali bölücüye ulaşır. **

**3'e bölücünün çıkışı hazır senkronizasyonu için zamanlama sinyalini, 2'ye bölücünün giriş sinyalini ve mikroişlemciler için CLK sinyali üretir. CLK sinyali clock generatordan çıkmadan önce bufferlanı r. Unutulmamalı ki birinci sayıcının çıkışı ikinciyi besler. Kaskad bağlanmış bu iki sayıcı çevresel clock çıkışı olan PCLK'ya 6'ya bölünmüş sinyal, sağlar. **

**Aşağıda 8284A'nın 8086/8088'e nasıl bağlanacağını gösterir bir şema verilmiştir. Unutulmamalı ki kristal osilator seçileceğinde F/C ve CSYNC topraklanmalıdır. 15MHz'lik bir kristal 8086/8088 mikroişlemcilerine normal bir 5MHz'lik c lock sinyali sağladığı gibi çevre birimlerede 2.5MHz sinyal sağlar.**

***8284A ve 8088 mikroişlemci bağlantısı çizilecek***

**2.2.2 Reset Bölümünün Çalışması **

**8284A'nın reset kısmı çok basittir. Bu kısım Schmitt Trigger buffer ve bir D Tipi Flip-Floptan oluşmaktadır. D tipi Flip-Flop 8086/8088'in RESET girişinin zamanlama ihtiyaçlarının karşılanmasını sağl ar. Bu devre her bir clock darbesinin düşen kenarında mikroişlemciye reset sinyali gönderir. 8086/8088 clock darbesinin yükselen kenarında RESET'i örnekler, ve böylece 8086/8088'in zamanlama ihtiyaçlarını sağlar. **

**Yukarıdaki şemadan yeniden bahsedelim. Unutulmamalı ki RC devresi sisteme ilk enerji verildiğinde RES pinini lojik 0 yapar. Kısa bir süre sonra direnç vasıtasıyla kondansator +5V'a şarj olduğu için R ES girişi lojik 1 değerini alır. Buton mikroişlemcinin resetlenmesine izin verir. Doğru bir reset zamanlaması sistem enerjilendikten sonra RESET girişi 4 clock darbesinden sonra lojik 1 yapılmasını ve en az 50 **μ** s bu seviyede tutulmasını gerektirir. Flip-Flop RESET ucunun 4 clock sonunda 1'e gitmesini ve RC zaman sabiti en az 50**μ** s 1 seviyesinde kalmasını sağlar.**

**3. BUS HATTINDA BUFFER VE LATCH OLAYI**

**8086/8088 mikroişlemcileri bellek yada I/O arabirim elemanlarıyla kullanılmadan önce, multiplex edilmiş olan bus hatları demutiplex edilmelidir. Bu bölümde demultiplex etmek gerekli detaylar ve büyük sistemlerde bus hatlarının nasıl bufferlandığı anlatılacaktır. (Çünkü maximum fanout 10'dur ve 10'dan fazla malzeme olan sistemler bufferlanır.)**

***3.1 Bus Hatlarının Demultiplex Edilmesi***

**8086/8088 üzerinde bulunan adres/data bus hatlarında ihtiyaç duyulan pin sayısını azaltmak için multiplex edilir. Okuma/yazma işlemlerinde adresin aynı ve kararlı olması belek yada I/O için bir gerek liliktir. Eğer bus hatları multiplex edilmiş ise bellek ve I/O'nun yanlış yerden okuma ve yazma işlemlerini yapmasına neden olacak olan adres değişir. **

**Bütün bilgisayar sistemlerinde 3 tane bus hattı vardır. Adres bus bellek adreslerini veya I/O port numarasını kullanarak bellek yada I/O'ya ulaşılmasını sağlar. Data bus sistem için mikroişlemci ve b ellek arasında data transferini sağlar. Kontrol bus ise bellek yada I/O için kontrol sinyallerini sağlar Bu bus hatları bellek ve I/O'ya arabirim oluşturmak için tanımlanmalıdır. **

**3.1.1 8088'in Demultiplex Edilmesi**

**Aşağıdaki şekilde bus hatlarının demultiplex edilmesi için ihtiyaç duyulan 8088 mikroişlemci ve diğer birimleri göstermektedir. Bu durumda, iki tane bağımsız 74LS373 latch AD7-AD0 adres/data bus hatl arını ve multiplex edilmiş olan A19/S6-A16/S3 adres/durum hatlarını demultiplex etmek için kullanılır. **

**Figure 7-5 buraya konulacak**

**ALE ucu lojik 1 olduğu zaman bir tel gibi davranan bu latchlar, girişi çıkışa aktarırlar. Kısa bir süre sonra latchlar ALE ucunun lojik 0 olmasıyla beraber aynı anda girişlerini tutarlar. Bu durum da A7-A0 alttaki latchda ve A19-A16 üstteki latchde tutulur. Bu durum A19-A0 arasındaki adres bus hattının ayrılmasına sebep olur. Bu adres bağlantıları 8088'in 1M Byte'lık adres alanını adreslemesine izin verir. Data bus hattının ayrılması ise her bir 8 bitlik çevresel birimlerle veya bellek birimleriyle bu hattın bağlanmasını sağlar. **

**3.1.3 8086'nın Demultiplex Edilmesi **

**8088'de olduğu gibi 8086'lı sistemlerde ayrılmış adres, data ve kontrol bus hatlarına ihtiyaç duyarlar. Özellikle multipleks edilmiş pinlerin sayısında farklılık vardır. 8088'de sadece AD7-AD0 ve A1 9/S6-A16/S3 multipleks edilmiştir. 8086'da ise multipleks edilmiş pinler, AD15-AD0, A19/S6-A16/S3 ve BHE/S7 'den oluşmaktadır. Bütün bu sinyaller demultiplex edilmelidir.**

**Aşağıdaki şekilde 8086'nın üç Bus hattının demultipleks edilmesi görülmektedir. bu bus hatları; adres(A19-A0 ve BHE), data (D15-D0), kontrol bus (M/IO, RD ve WR) hatlarıdır. 8088 ve 8086 için verilen devreler hemen hemen aynıdır. Fakat 8086 için verilen devrede ilave olarak kullanılan 74LS 373 latchi AD15-AD8 adres/data bus hattını demultipleks etmekte kullanılır. Ayrıca üstteki 74LS373 latchınede 8086'nın 16 bitlik bellek sistemindeki yüksek değerli kli bellek seçimi için BHE/S7 girişi eklenmiştir. Burada bellek ve I/O sistemi 8086'yı 20 bitlik Adres bus (A19-A0), 16 bitlik data bus(D15-D0) ve üç tane kontrol hattı (M/IO,RD ve WR) olan bir aygıt olarak görür. **

**Figure 7-6 daki şekil yerleştirilecek**

***3.2 Sistemin Bufferlanması***

**Eğer herhangi bir bus pinine 10'dan fazla yük uygulanmış ise 8086 veya 8088'den oluşan sistemin tamamı bufferlanmalıdır. Mikrobilgisayar sistemlerinde karşılaşılan yüksek kapasiteli bus sistemlerini sürmekte kullanılan 74LS373 latchları demultipleks edilen pinleri hemen bufferlarlar. Buffer çıkış akımları TTl tipi yüklerin sürülebileceğinden daha fazladır. Çıkış lojik 0 olduğunda 32mA emme akımı, lojik 1 olduğunda ise 5.2mA kaynak akımını sağlamaktad ır. **

**Tamamen bufferlanmış sistemde, sinyal, zamanlama gecikmesi oluşturur. Bellek yada I/O birimleri bus hattının en yüksek hızına yakın bir hızda işlem görmedikçe bu durum herhangi bir güçlük oluşturmaz. **

**3.2.1 Tamamen bufferlanmış 8088 **

**Aşağıdaki şekil tamamen bufferlanmış 8086 mikroişlemciyi göstermektedir. Görüldüğü gibi geride kalan 8 adres pini, A15-A8, 74LS244 8'lik buffer, 8 data bus pini (D7-D0) 74LS245 8 bitlik çift yönlü bu s buffer ve kontrol bus işaretleri IO/M, RD, WR 74LS244 buffer kullanmaktadırlar. Dolayısıyla tamamen bufferlanmış 8088 sistemi iki tane 74LS244, bir 74LS245 ve iki tane 74LS373'e ihtiyaç duyar. 74LS245'in yönü DT/R sinyali ile kontrol edilir. ve bu enteg re etkili yada etkisiz hale getirilir. **

**Figure 7-7 Cizilecek**

**3.2.2 Tamamen bufferlanmış 8086**

**Aşağıdaki şekil tamamen bufferlanmış 8086 mikroişlemcisini gösterir. Adres pinleri 74LS373 adres latchları ile bufferlanır. Data bus ise iki tane 74LS245 8 bit çift yönlü bus buffer tarafından kontro l edilir. Kontrol bus sinyalleri ise IO/M, RD, ve WR 74LS244 bufferı kullanırlar. Tamamı bufferlanmış 8086 sistemi bir tane 74LS244, iki tane 74LS245 ve üç tane 74LS373 kullanır. 8086 8088'e göre 8 tane daha fazla data bus hattı olduğu için ondan bir faz la buffer kullanır. Ayrıca bellek banklarının seçimi için bufferlanan BNE sinyaline sahiptir. **

**Figure 7-8 Cizilecek**

***3.3 BUS ZAMANLAMASI***

**8086 ve 8088 mikroişlemcilerine arabirim oluşturacak bellek yada I/O birimlerini seçmeden önce sistemin bus zamanlama işlemlerini anlamak temeldir. Bu bölüm bus sinyallerinin işlenmesini ve temel oku ma ve yazma zamanlamalarının kavranmasını sağlayacaktır.**

**3.3.1 Bus Hatlarının Çalışmasının Temeli**

**8086/8088'de bulunan üç tane bus hattının yani adres, data ve kontrol buslarının işlevleri tamamiyle diğer mikroişlemcilerdeki gibidir. Eğer data bilgileri belleğe yazılacaksa mikroişlemci adres bus üzerine bellek adresini gönderir, belleğe yazılacak bilgileri data bus üzerine yükler, belleğe yaz komutunu verir ve 8088 için IO/M=0 ve 8086 için M/IO=1 yapar. Aşağıdaki şekil yazma işleminin basitleştirilmiş şeklini görmektesiniz.**

**Figure 7-9 çizilecek**

**Eğer bellekten bilgi okunacaksa mikroişlemci bellek adresini adres bus hattına gönderir, oku komutunu verir ve data bus yoluyla bilgileri alır. Aşağıdaki şekilde basitleştirilmiş okuma bus çevrimi gö rülmektedir.**

**Figure 7-10 çizilecek**

**3.3.2 Genel Olarak Zamanlama İşlemleri**

**8086/8088 bus çevrimi olarak tanımlanan bir zaman diliminde bellek yada I/O'u kullanır. Eğer clock 5MHz'de işlenirse (bu iki işlemci için temel işleme frekansı 5MHz'dir) o zaman bir 8086/8088 bus çe vrimi 800ns'de tamamlanır. Bunun anlamı mikroişlemci kendisi ile bellek yada I/O arasındaki data okuma ve yazma işlemlerini saniyede maximum 1.25 milyon defa yapar. (İç yapısından dolayı 8086/8088 palslarla saniyede 2.5 milyon komutu yürütebilmektedir.) B u mikroişlemcilerin diğer versiyonları yüksek clock frekansından dolayı daha büyük transfer oranına sahiptir. **

**T1. Bus çevriminin birinci peryodu olan T1'de pek çok şey olur. Belleğin adresi ve I/O'nun yeri adres bus ve adres/data bus hatlarıyla gönderilir. Adres/data bus multiplex edilir ve bazen adres bilg isi bazen de data bilgisi içerir. T1 anındaki kontrol sinyalleri de ALE, DT/R, IO/M(8088) veya M/OI (8086)'dir. IO/M veya M/IO sinyalleri adres bus hattının bellek adresini I/O biriminin port numarasını içerip içermediğini gösterir. **

**T2. T2 esnasında, 8086/8088 RD veya WR sinyallerinden birini ve DEN komutunu verir ve yazma sırasında data busta bulunan bilgiyi yazar. Bu evreler bellek yada I/O biriminin okuma yada yazma icrasını n başlamasına neden olur. Sistemde bilgi varsa DEN sinyali data bus bufferlarını açar. Böylece bellek yada I/O yazılmak için bilgi alabilir veya mikroişlemci okuma işlemi için bellek yada I/O'dan bilgiyi alabilir. **

**T3. Bu saat peryodu belleğin dataya erişim zamanını sağlamak için kullanılır. Eğer bus çevrimi okuma bus çevrimi ise data bus T3'ün sonunda örneklenir. **

**T4. T4'te bütün bus sinyalleri aktif değildir ve diğer bus çevrimi için hazırlıktadır. Ayrıca bellek yada I/O'dan okunacak datalar için data bus hatlarının 8086/8088 tarafından örneklendiği zamandır . Sonunda bu noktada WR sinyalinin yükselen kenarında aktif olan bellek yada I/O'a dataları transfer eder ve WR lojik 1 seviyesine döndüğü zaman yazar.**

**3.3.3 Okuma Zamanlaması **

**Aşağıdaki şekil 8088 mikroişlemci için okuma zamanlamasını anlatmaktadır. 8086'nın 16 bit data busa sahip olması dışında 8086 ile okuma zamanlamaları hemen hemen aynıdır. Bu diyagrama küçük bir göza tışla herbir T durumunda tanımlanan temel olayları anlayabilirsiniz. Bellek yada I/O'dan data okunması için geçen süre okuma zamanlaması diyagramının en önemli kısmıdır. Bellek erişim zamanına göre seçilir ve erişim zamanı mikroişlemcinin okuma işlemi için datalara eriştiği sabit bir zaman dilimidir. Sistemin sınırlılıklarına göre bellek seçimi son derece önemlidir. **

**Figure 7-11 Cızılecek**

**Bu arada mikroişlemci zamanlama diyagramı açık şekilde bellek erişim zamanını vermez. Aksine, erişim zamanına ulaşmak için değişik zamanları birleştirmek gerekir. Diyagramdan bellek erişim zamanını b ulmak için öncelikle datanın örneklendiği noktayı belirlemeliyiz. Zaman diyagramı dikkatlice incelenirse T3'ün sonundan data bus'a kadar devam eden çizginin farkına varırsınız. Bellek erişim zamanı adres bellek adres bus hattına yüklendiğinde başlar v e mikroişlemcinin bellek bilgisini örneklediği T3'e kadar devam eder. Bu zaman aralığında yaklaşık olarak 3 tane t durumu geçecektir. Fakat tam değildir. Adres, T1 başladıktan sonra TCLAV zamanına kadar görünmez. (clock 5MHz ise TCLAV 110ns'dir) Bunun an lamı TCLAV zamanı adresin görüldüğü T1 zamanı ve datanın örneklendiği T3 zamanı olarak ayrılan 3 zamanlama durumundan (600ns) çıkartılmalıdır. T3'ten önce oluşan data setup zamanı da (TDVCL ) çıkartılmalıdır. Bus çevriminin bu üç durumundan TDVCL ve TCLAV toplamlarını çıkardığımızda bellek erişim zamanını buluruz. TDVCL 5MHz clock için 30ns olduğundan müsade edilen bellek erişim zamanı sadece 460ns'dir. **

**Sistemlerdeki adres decoder ve bufferladan oluşan zaman gecikmelerinden ötürü tabiki 5MHz de çalışan bir 8086/8088 mikroişlemciyle çalışacak olan bellek devrelerinin dataya erişme zamanı 460ns'den da ha az olmalıdır. En azından 30 veya 40ns'lik bir fark olmalıdır. Böylece bellek hızı 8086/8088 ile düzgün bir şekilde çalışabilmesi için yaklaşık 420ns'den daha yavaş olmalıdır. **

**Bellek işlemlerini etkileyen bir zaman faktörü RD strobunun genişliğidir. Zaman diyagramından RD strobe genişliği TRLRH olarak verilmiştir. Hemen hemen imal edilen 400ns veya daha az erişim zamanın a sahip bütün bellek birimleri için 325ns bu strobe için yeterlidir. **

**Yazma Zamanı**

**Aşagıdaki şekil 8088 mikroişlemci yazma zaman diyagramıdır. 8086'nın da hemen hemen aynı diyagrama sahip olmasından dolayı ayrı diyagram çizilmemiştir. Yazma yada okuma zamanındaki temel farklar çok küçüktür. RD strobunun yerini WR strobu almıştır. Data bellek için bilgi içermekten ziyade bellekten bilgi alır ve bus çevrimi boyunca DT/R lojik 1 olur. Bazı bellek birimleriyle arabirim oluştururken WR'nin lojik 1 olduğu nokta ile data bus hattından da taların uzaklaştırıldığı zaman arasındaki fark tehlikeli olabilmektedir. Bunun sebebi hatırlayacağınız gibi bellek bilgisi WR strobunu takip eden kenarda yazılır. Zaman diyagramına göre 808 8 5MHz Clock frekansında çalıştığı zaman tehlikeli peryot TWHDX 88ns'dir. Tutma zamanı genelde bundan daha azdır ve gerçekte bellek birimleri için 0 ns'dir. WR strobunun genişliği TWLWH yani 430ns'dir. Erişim zamanı 400ns veya daha az olan pek çok bellek birimi için bu oran çok iyidir. **

**Figure 7-13 Cızılecek**

***3.4 READY(HAZIR) VE WAIT STATE (BEKLE) DURUMLARI ***

**Bu bölümün daha önceki kısımlarında belirtildiği gibi READY girişi daha yavaş bellek yada I/O birimleri için bekleme durumlarına neden olur. Bir bekleme durumu (TW) T' ile T^ arasına yerleştirilen ve bus çevrimini uzatan extra clock peryodudur. Bir bekleme durumu meydana geldiyse bellek erişim süresi normalde 5MHz'lik bir clock için 460ns iken bir clock peryodu uzadığı için 660ns olur. **

**3.4.****1**** READY Girişi**

**READY girişi T2'nin sonunda ve eğer uygunsa tekrar TW'nin ortasında örneklenir. Eğer READY T2'nin sonunda lojik 0 ise T3 geciktirilir ve ve Tw T2 ile T3 arasında gerçekleşir. Bir sonraki durum TW ve ya T3 ise TW'nin ortasında READY örneklenir. READY T2'nin sonunda lojik 0 için yani 1'den 0'a geçişte ve TW'nin ortasında lojik 1 için yani 0'dan 1'e geçişte test edilir. 8086 ve 8088 için READY girişinin bir dizi zamanlama ihtiyaçları vardır. Aşağıdaki zamanlama diyagramında hold ve setup zamanları sırasında bekleme durumuna sebep olan ready sinyalini göstermektedir. Bu işlem esnasındaki zamanlama şartları Ready senkronizasyon devresi olan 8284A clock generator devresi tarafından karşılanır. READY için 8284A kullanıldığında RDY (8284A'nın girişi)her bir T durumunun sonunda oluşur.**

**Şekil 7-14**

**3.4.2 RDY ve 8284A**

**RDY 8284A clock generatorunun senkronize edilmiş hazır girişidir. Bu giriş için zamanlama diyagramı aşağıdadır. 8086/8088'in READY girişi için zamanlamada farklılık oluşturmasına rağmen 8284A'nın iç yapısı 8086/8088'e sağlanan READY'nin tam olarak senkronizasyonunu garantilemektedir. Aşağıda 8284A'nın içyapısı verilmiştir. Bu devrenin alt yarısı READY senkronizasyon devresidir. En sol tarafta RDY1 ve AEN1 tıpkı RDY2 ve AEN2 gibi AND işlemine tutu lmaktadır. Çıkışlar bir veya iki evrede senkronizasyona giriş oluşturmak için OR işlemine tabi tutulur. Flip-Flop'ların girişinde lojik 1 elde etmek için AND işlemi uygulanan RDY1 ve AEN1'in çıkışı yada RDY2 ve AEN2'nin çıkışı aktif olmalıdır.**

**Şekil 7-15**

**Şekil 7-16**

**AYSNC girişi lojik 1 iken tek evreli senkronizasyonu, lojik 0 iken iki evreli senkronizasyonu seçer. Eğer tek evre seçildiyse RDY sinyalinin clock pulsının bir sonraki düşen kenarına kadar 8086/8088 READY girişine ulaşmasına engel olur. Eğer iki evre seçildiyse clock işaretinin birinci yükselen kenarı RDY sinyalini 1. flip-flopta tutar. Bu ff'un çıkışı 2. Dlip-Flopu sürer. ve bir sonraki clock'un düşen kenarında RDY'i tutar. Aşağıda 8086/8088 mikro işlemciler için kullanılan hemen hemen bütün bekleme durumlarını oluşturacak devreyi göstermektedir. Burada 8 bitlik seri çıkışlı shift register lojik 0 değerinin 8284A'nın RDY1 girişi için bir yada daha fazla clock peryodunda Q**** ç****ıkışlarından birinden kaydırır. Bu devrenin bağlanmasına bağlı olarak değişik sayıda bekleme durumu elde edilir. Shift registerin başlama noktasına dönmesi için nasıl reset edildiğine dikkat edin. RD, WR ve INTA pi nlerinin hepsi lojik 1 ise register çıkışları da high olur. Bu üç sinyal T2 durumuna kadar High seviyede kalır. Böylece T2'nin ilk yükselen kenarına ulaşıldığında shift register kaydırır. Eğer tek bekleme istenildiyse o zaman QB çıkışı OR kapısına bağla nır. Eğer iki bekleme durumu isteniyorsa QC çıkışı bağlanır. Devrenin timing diyağramından da anlaşılabilecegi gibi bu devre daima bekleme durumu üretmez. **

**Şekil 7-17**

**Şekil 7-18**

**Bellek ile sadece bekleme durumuna ihtiyaç gösteren bellek birimleri arasındaki işlemlerde etkindir. Eğer seçilen bellek biriminin sinyali lojik 0 ise bu birim seçilir, o zaman bu devre bekleme duru mu üretecektir. **

***3.5 MİNİMUM MODA KARŞILIK MAKSİMUM MOD***

**8086/8088 mikroişlemcilerinin minimum mod ve maximum mod olmak üzere iki farklı işlem modu vardır. Minimum mod işlemi mod seçme ucu MN/MX +5V'a bağlandığı zaman ve maximum mod ise bu pin şaseye bağla ndığı zaman elde edilir. **

**Her iki mod 8086/8088 mikroişlemci için farklı kontrol yapılarını seçer. Minimum mod tarafından sağlanan işlemler en son Intel 8-bit mikroişlemci olan 8085A ile benzerdir. Oysa maximum mod yeni, tek ve yardımcı işlemcilerin varolduğu sistemlerde kullanılmak için dizayn edilmiştir. **

**3.5.1 Minimum Mod İşlemi **

**Maximum mod minimum moddan bazı kontrol sinyallerin harici olarak üretilmesi bakımından farklıdır. Bu 8288 adında bir bus kontrollerin eklenmesini gerektirir. Maximum mod esnasında bus kontrolu için 8086/8088 üzerinde yeterli pin yoktur. Çünkü yeni pinler ve yeni nitelikler bazılarının yerini almıştır. Maximum mod sadece 8087 aritmetik işlemci gibi harici bir işlemci kullanıldığı zaman tercih edilir. **

**3.5.2 8288 Bus Kontroller**

**Maximum modda işleyen bir 8086/8088 sisteminin, maximum mod yoluyla 8086/8088'den elde edilen sinyalleri sağlamak için 8288 bus kontroller gereklidir. Aşağıdaki şekill 8288 bus kontroller devresinin pin çıkışlarını ve blok diyagramını göstermektedir. Görüldüğü gibi 8288 tarafından yönetilen kontrol sinyalleri I/O ve bellek için farklı sinyaller içerir. (IORC, IOWC-MRDC,MWTC)**

**Şekil 7-21**

**Ayrıca genişletilmiş bellek (AMWC) ve I/O (AIOWC) yazma strobları ve INTA sinyali içerir. Bu sinyaller 8086/8088 mikroişlemcileri minimum moddan maximum moda anahtarlandığı zaman kaybettiği ALE, WR, IO/M, DT/R, DEN, ve INTA sinyallerinin yerini almaktadır. **

**Pin Fonksiyonları**

**Bundan sonraki kısımda 82888 bus kontrollerin pin tanımlamaları anlatılacaktır. **

**S2, S1 ve S0-Durum Bitleri **

**Bunlar 8086/8088!in durum çıkış bitlerine bağlanırlar. Bu üç sinyal sisteme zamanlama sinyali üretmek için decode edilir. **

**CLK-Clock **

**İç zamanlamayı sağlayan giriş pinidir. ve 8284A clock generatorunun CLK çıkış pinine bağlanmalıdır. **

**ALE-Adres Latch Enable **

**Adres/data bus hattını demultiplex etmekte kullanılan çıkış pinidir. **

**DEN Data Bus Enable **

**Sistemde bulunan çift yönlü data bus bufferlarını kontrol etmekte kullanılan bir pindir. **

**DT/R-Data Transmit/Receive **

**Çift yönlü data bus bufferlarını kontrol eden bir sinyal çıkışıdır. **

**AEN-Adres Enable **

**Bellek kontrol sinyallerini etkin hale getiren 8288'in girişidir.**

**CEN- Kontrol Enable **

**8288'in çıkış komutlarını etkin hale getiren giriştir. **

**IOB-I/O Bus Mod **

**I/O bus mod veya sistem bus işlemlerinden birini seçer.**

**AIOWC **

**I/O'a ileri I/O yazma kontrol sinyalini sağlayan kontrol çıkışıdır.**

**IOWC-I/O Yazma **

**I/O'a temel yazma sinyalini sağlamak için kullanılan komuttur. **

**IORC-I/O Oku **

**I/O'a okuma kontrol sinyali sağlamak için kullanılan bir komut çıkışıdır.**

**AMWC- İleri Bellek Yazma **

**Belleğe önceki veya sonraki yaz sinyalini sağlamak için kullanılan komuttur.**

**MWTC- Belleğe Yaz **

**Belleğe okuma kontrol sinyalini sağlayan bir sinyaldir.**

**MRDC-Belleği Oku **

**INTR pinine yapılan interrupt isteklerinin edildiğini bildiren bir çıkıştır.**

**INTA- Interrupt Kabul Edildi **

**IOB şaselenmiş ise interrupt kontrolu için kaskad işlemini seçer ve eğer IOB high seviyesinde ise I/O bus vericileri etkin olur.**

**16. MCE/PDEN- Temel Kaskad/Çevresel Data:**

**4. BELLEK ARABİRİMİ**

**Basit yada karmaşık bütün mikroişlemci temelli sistemlerde bellek vardır. İntel ailesine ait mikroişlemcilerin de diğerlerinden farkı yoktur. Hemen hemen bütün sistemler yalnız okunabilir bellek (ROM ) yada rasgele erişimli bellek yada diğer adıyla yaz/oku bellek(RAM) olmak üzere iki tip belleğe sahiptirler. RAM geçici bilgileri ve yazılım uygulamalarını içerirken ROM daimi sistem bilgilerini ve sistem yazılımını içerir. Bu bölümde Intel ailesinin mi kroişlemcileri ile her iki tip belleğin nasıl arabirim oluşturacağı anlatılır. Değişik adres tiplerini kullanarak 8,16 ve 32 bit data bus ile bellek arabirimini anlatacağız. Bu her türlü mükroişlemcinin bellek sistemi ile arabirim oluşturabilmesine müsasa de eder.**

***4.1 Bellek Arabirimleri***

**Mikroişlemcinin bellek arabirimine başlamadan önce bellek parçalarının çalışmasını tamamen anlamak temeldir. Bu bölümde üç temel tip belleğin işlevini anlatacağız. Bunlar ROM, Static RAM (SRAM) ve Di namik RAM (DRAM)**

**4.1.1 Bellek Pin Bağlantıları**

**Adres girişleri, data çıkışları, giriş/çıkışları, değişik tip giriş seçimleri ve okuma veya yazma işlemini seçmek için en azından 1 tane kontrol girişi bütün bellek cihazları için temel pinlerdir. **

**Adres Bağlantıları : Bellek elemanı içinde bulunan bellek yerini seçen adres girişleri bütün bellek elemanlarında vardır. Bellek elemanı üzerinde bulunan adres pinlerinin sayısı ile tanımlanır . Bugün en genel bellek elemanları 1K ile 4M arasında bellek yerine sahiptirler. 1K'lık bellek elemanının 10 adres pini (A0-A9) vardır. Böylece 10 adres girişi 1024 bellek yerinden herhangi birini seçmenizi gerektirir. Eğer bellek elemanının 11 adres (A0- A10) bağlantısı varsa 2K'lık iç bellek yerine sahip olur. Mesela 4K'lık bellek elemanının 12 adres bağlantısı, 8K'lık elemanın 13 adres bağlantısı vardır. 1M'lık yer içeren bir eleman 20 bit adrese ihtiyaç duyar. 400H bellek sisteminin 1K bytelık bölümün ü temsil eder. Eğer bir bellek elemanı 10000H adresinden başlamak üzere dekode edildiyse ve 1K'lık eleman ise en son bellek yeri 400H'dan bir eksik olan 103FFH adresindedir. Diğer önemli he xadesimal sayı 1000H'dır. Çünkü 1000H 4K'dır.4Kbyte boyutunda ve 14000H adresinden başlayan bir bellek elemanı 1000H'dan 1 eksik olan 14FFFH yerinde sona erer. Üçüncü sayı ise 64K yani 10000h'dır 30000H adresinde başlayıp 3FFFFH adresinde sona eren bir b ellek 64K'lıktır. **

**Data Bağlantıları : Bütün bellek elemanları data çıkış veya giriş/çıkış grubuna sahiptir. Aşağıdaki eleman genel bir giriş/çıkış bağlantı gruplarına sahiptir. Bugün pek çok bellek elemanının ç ift yönlü genel I/O pinleri vardır. **

**Şekil 8-1**

**Data bağlantıları veri saklamak üzere girildiği veya okumak için çıkarıldığı noktalardır. Bu örnek elemanda 8 tane giriş/çıkış pini vardır. Bunun anlamı bu bellek elemanı her bir bellek bölgesindee 8 bitlik bilgiyi depo etmektedir. (bit genişliğindeki bu bellek elemanı çoğunlukla "bytewide" bellek olarak isimlendirilir.) Devrelerin pek çoğu 8 bit genişliğinde olmasına rağmen bütün bellek elemanları 8 bit değildir. Bazı devreler 16 bit, 4 bit ve hat ta 1 bittir. **

**Bellek elemanlarının katalog listeleri genelde CE bellek yerine karşılık gelen bit sayısıyla ifade edilir. Mesela 1K'lık bellek yerine karşılık gelen bit sayısıyla ifade edilir. Mesela 1K'lık bellek yerine sahip ve her bir bellek el emanı genellikle üreticiler tarafından 1Kx8 olarak nitelendirilir. 16Kx1, 16K içerip her birim 1 bitliktir. Bellek elemanları ayrıca toplam kapasitesine göre de sınıflandırılır. Mesela 1Kx8 bit ise 8K veya 64Kx4 ise 256K bellek elemanı olarak adlandırılır . Bu değişiklikler bir üreticiden diğerine değişir. **

**Bağlantıların Seçimi : Her bellek elemanının yada etkin hale getirme işi yapan ucu vardır. Bu tür girişleri çoğunlukla Chip seçme (CS), Chip Enable(CE) veya Select (S) olarak isimlendirilirle r. Ram bellek genelde en az bir CS veya S girişi ROM belleğin ise en az bir CE girişi vardır. Eğer CS, CE veya S girişleri aktif yani lojik 0 ise bellek elemanı okuma yada yazma işlemini yürütür. Eğer aktif değilse yani lojik 1 ise kapalı olduğunu yada e tkin olmadığından okuma yada yazma işlemlerini yapamaz. Eğer birden fazla CS ucu varsa okuma yada yazma için hepsinin aktif olması gerekir. **

**Kontrol Bacakları : Bütün bellek birimlerinin bazı kontrol giriş formları vardır. RAM'ın genelde bir yada iki kontrol girişi varken ROM'un bir kontrol girişi vardır. ROM üzerinde bulunan kontr ol girişi, dataların data çıkış pinlerinden akmasına müsaade eden output enable (OE) veya Gate(G)'dir. Eğer OE ve seçilen girişlerin her ikisi de aktif ise o zaman çıkış etkin olur. Eğer O E aktif değilse çıkış yüksek empedans durumuna girer. OE bellek içinde bulunan 3 durumlu bufferlar tarafından etkin yada etkisiz yapılabilir. Bu uç data okumak için etkin olmalıdır. **

**Bir RAM bellek elemanının ya bir yada iki kontrol ucu vardır. Eğer bir kontrol ucu varsa ki bu R/W olarak adlandırılır. Bu pin okuma yada yazma işlemini sadece eleman CS girişi tarafından seçildiyse yapar. RAM'ın iki kontrol girişi varsa bu girişler WE (veya W) ve OE (veya G) olarak adlandırılır. Burada bellek yazma işlemi için WE ve bellek okuma işlemi için OE aktif olmalıdır. Her iki kontrol girişi de aktif değilse o zaman data ne yazılır ne de ok unur ve data bağlantıları yüksek empedans durumunda olur.**

***4.2 ROM BELLEK***

**Yalnız okunabilir bellek (ROM) kalıcı bir şekilde sistemde sabit kalması gereken ve enerji kesildiğinde değişmeyen data yada programları depolar. Enerji kesildiğinde bile bilginin daima kalması için ROM kalıcı bir şekilde programlanmalıdır. ROM bugün pek çok biçimlerde olmaktadır. ROM olarak adlandırdığımız eleman pek çok özeliği ile birlikte alınır ve fabrikadan fabrikasyon sırasında programlanır. Bir ROM olan EPROM (silinebilir programlanabili r yalnız okunabilir bellek) yazılım değiştirilmek istendiğinde kullanılır. Bir EPROM, EPROM'un tipine bağlı olarak 20 dakika yada daha uzun süre yüksek yoğunluklu ultraviole ışığa maruz bırakılarak silinebilir.**

**PROM bellek elemanları da mevcuttur ama bugün pek kullanılmamaktadır. PROM hafıza hücreleri RAM ve ROM hafıza hücreler gibi matris düzleme yerleştirilirler. Her hücre küçük Nikel-Krom veya silikon ok sidli sigortalardan oluşmuştur. PROM'da bu sigortalar yakılarak programlanırlar. Fakat bir defa programlandılar mı bir daha silinemezler. Bunların yanında daha yeni bir tip olan read-mostly bellek flash bellek olarak adlandırılır. Flash bellek genellikle EEPROM (Elektriki silinebilir- Programlanabilir ROM) EAPROM (Elektriksel Değiştirilebilir ROM) veya NOVROM (Kaybolmayan ROM) olarak da anılırlar. Bu elemanları sistemde elektiksel olarak s ilinebilir. Fakat silmek için normal RAM'dan daha fazla süreye ihtiyaç duyarlar. Flash bellek elemanları bilgisayarda setup bilgilerini depolamak için kullanılır. Bios Bellek için yakın gelecekte EPROM'un yerini alabilir. **

**Bu sistemler flash bellek elemanınında depo edilmiş password içerirler. Aşagıdaki şekilde 2716 EPROM'un genel yapısı verilmiştir. Bu eleman 11 adres girişi ve 8 data çıkışına sahiptir. 2716 2Kx8 bel lek elemanıdır. 27XXX EPROM serisi olup şu tipleri vardır. 2704 (512x8), 2708(1Kx8), 2716 (2Kx8), 2732 (4Kx8), 2764 (8Kx8), 27256 (32Kx8), 27512 (64Kx8) ve 271024 (128Kx8) vb.. Bütün bu elemanlar 8 data pini, bir chip seçme girişi (CE) ve bir output enabl e pini (OE) içerirler.**

**Şekil 8-2**

**Aşagıdaki şekil 2716 EPROM'un zaman diyagramını temsil etmektedir. Datalar sadece hem CE hem de OE pini lojik 0 değerini aldıktan sonra çıkış pinlerinde görünür. Eğer CE ve OE'nin ikisi birden 0 değ ilse data çıkışları yüksek empedans veya kapalı durumunda kalırlar. Ayrıca datanın EPROM'dan okunabilmesi için Vpp'nin lojik 1 değerini alması gerekir. **

**Şekil 8-3**

**Bazı durumlarda SRAM'da Vpp ile WE pini aynı durumda olur. Bu tek bir soketle ya EPROM yada SRAM'ın kullanılmasına müsaade eder. 2716 EPROM ve 6116 SRAM buna bir örnektir. Her ikisi de 2Kx8 elemanla r olup EPROM'un Vpp ve SRAM'ın WE ucu hariç pinleri aynıdır. **

**Zamanlama diyagramı ve bilgi tablosundan sağlanan en önemli bilgi, belleğe okuma işlemini yaptıran bellek erişim zamanıdır. Yukarıdaki timing diyagramının gösterdiği bellek erişim zamanı (**** ****) adresin adres girişlerinde görünmesinden datanın çıkış uçlarında görünmesine kadar ölçülen süredir. Bu CE girişinin low olmasıyla aynı zamanda adres girişle rinin sabit olması esasına dayanır. Ayrıca OE çıkış uçlarının aktif olması için lojik 0 olmalıdır. Bu EPROM'un temel hızı 450ns'dir. Bu tip bellek malzemeleri 8086/8088 mikroişlemcilerle gereği gibi çalışmaları için oldukça uzun erişim zamanlarından ötürü bekleme durumlarına ihtiyaçları vardır. Eğer bekleme durumu istenmiyorsa, EPROM'un daha yüksek versiyonları elde edilebilir. Bugün 100ns gibi küçük erişim zamanına sahip EPROM bellekler mevcuttur.**

***4.3 STATİK RAM ELEMANLARI***

**Statik RAM, üzerindeki bilgileri DC güç uygulanmadığı sürece muhafaza eder. Çünkü güç hariç, dataları yüklemek için özel bir duruma ihtiyaç yoktur. ROM ile RAM arasındaki temel fark RAM normal bir iş lemle yazılırken ROM bilgisayar dışında programlanır ve normal bir şekilde okunur. SRAM geçici bilgileri depo eder ve oku/yaz işlemleri belleğin boyutları nispeten küçük olduğu zaman kullanılır. Bugün küçük bir bellek 1Mbyttan daha azdır. Aşağıdaki şekil 2Kx8 read/write bellek olan 4016 SRAM'ı temsil etmektedir. Bu elemanın 11 adres girişi ve 8 data giriş/çıkış pini vardır. **

**şekil 8-2**

**Bu RAM'ın kontrol girişleri daha önce anlatılanlardan biraz farklıdır. OE pini G, CS pini S ve WE pini W olarak adlandırılmışlardır. Değişik dizayn edilmelerine rağmen kontrol pinlerinin fonksiyonlar ı daha önce anlatılanlarla tamamen aynıdır. Diğer üreticiler bu yaygın SRAM'ı 2016 ve 6116 adlarıyla üretmişlerdir. Aşağıdaki şekil 4016 SRAM'ın zaman diyagramını anlatmaktadır. **

**şekil 8-5**

**En yavaş versiyon olan 4016'da erişim zamanı 250ns'dir ve bekleme durumu olmadan 5MHz'de işleyen 8086 veya 8088 ile bağlantı kurmak için yeterince hızlıdır. Erişim zamanı mikroişlemci ile bellek malz emelerinin tamamını tanımak için kontrol edilmelidir. Aşağıdaki şekil 32Kx8 Static RAM olan 62256'nın pin çıkışlarını temsil etmektedir. Bu eleman 28 bacaklı entegre devre kılıfına sahiptir ve 120ns veya 150ns erişim hızlarındadır. Diğer temel SRAM elema nları 8Kx8 ve 128Kx8 boyutlarındadır. **

**şekil 8-6**

***4.4 DİNAMİK RAM BELLEK ***

**Bugün hemen hemen en büyük SRAM 128x8'dir. Diğer yandan dinamik RAM'lar çok daha büyük boyutlarda mevcuttur. DRAM datayı entegre devre üzerinde 2 veya 4ms tutması dışında temelde SRAM ile aynıdır. 2 veya 4ms sonra DRAM'ın içeriği tamamen yeniden yazılmalıdır. Çünkü lojik 0 veya lojik 1 değerini depo eden kondansatörler deşarj olurlar. Her bir bellek birimindeki çoğu gereksiz şeyleri durmadan bir programla okuyup tekrar yazmak yerine üreticiler 64Kx1' lik DRAM'ı 4ms'lik sürede 256 defa tazeleme işlemi uygulanması için içten yapılandırdılar. Refresh işlemi yazma, okuma ve özel refresh çevrimlerinde meydana gelmektedir. DRAM'ın diğer bir dezavantajı ise üreticilerin adres pinleri multiplex etmiş oldu ğu çok fazla adres pinine ihtiyaç olmasıdır. Aşagıdaki şekil 64Kx4'lık TMS4464 DRAM'ını göstermektedir. **

**Şekil 8-7**

**Unutulmamalı ki 64K'lık bellek yerini adreslemek için gerekli olan 16 adres girişi içermesi gereken 8 adres girişine göndermenin tek yolu iki tane 8 bitlik artışlardır. Bu işlem CAS (Kolon adres stro bu) ve RAS (satır adres srobu) olarak adlandırılan 2 özel pinle yapılır. Önce A0-A7 adres pinlerine yerleştirilen ve satır adres olarak RAS tarafından iç satır (row) latche yerleştirilir. Sonra A8-A15 adres bitleri aynı 8 adrese yerleştirilir ve kolon adr es olarak CAS tarafından iç sütun latchina yüklenir. Bu iç latchlarda tutulan bu 16 bitlik adres 4 bitlik bellek birimlerinden birinin içeriğini adresler. **

**Aşagıdaki şekil TMS4464 DRAM'a ait 8 adres girişindeki satır ve sütun adreslerini strobe etmek için kullanılan multipleksırları göstermektedir. Burada RAS sadece DRAM'da bulunan satır adresi strobe etmekte kullanılmaz. Adres girişlerine uygulanan adresi de değiştirir. Bu multiplexlerin yayılma gecikmesinden dolayı mümkündür. RAS lojik 1 iken B girişleri multiplexlerin Y çıkışlarına bağlanır. Eğer RAS lojik 0 olursa A girişleri Y çıkışlarına gider. Çünkü iç satır adresi latchı kenar teiklemelidir. Girişlerdeki adres kolon adresi değişmeden önce satır adresi alır. SRAM 'daki gibi W pini datayı DRAM'a yazar ve G pini okumak için çıkış pinlerini aktif hale getirir. **

**şekil 8-9**

**Aşağıdaki şekil 41256 DRAM'ını göstermektedir. Bu eleman 70ns kadar küçük bir zamanda data erişimine gerek duyup 256Kx1 olarak düzenlenmiştir. **

**şekil 8-10**

***4.5 ADRES DEKODE EDİLMESİ***

**Bellek veya I/O elemanının mikroişlemciye bağlanabilmesi ve bellek haritasındaki tek bir partisyon yada bölümün belleğin fonksiyonlarını yerine getirebilmesi için mikroişlemciden alınan adresin dekod edilmesi gerekir. Adres dekod edilmeden sadece bir bellek elemanı mikroişlemciye bağlanabilir. Bu bölümde, pek çok bölümde bulunan dekoderler kadar adres dekode etme tekniklerini anlatacağız.**

**Neden Bellek Dekod Edilir?**

**8088 mikroişlemci ile 2716 EPROM karşılaştırıldığında adres uçlarının sayısında farklılık vardır EPROM'un 11 adres ucu ve mikroişlemcinin 20 adres ucu bulunur. EPROM'un sadece 11 adres girişi olduğu için bağlantı nasıl yapılırsa yapılsın ayar bozukluğu olur. Eğer sadece 8088'in 11 adres pini bağlanırsa bağlanmayı umduğu 1Mbyte bellek yerine sadece 2Kbyte'lık belleği görecektir. Dekoder mikroişlemci ile bellek malzemesini uydurmak için kullanılır. **

**Basit NAND Kapılı Dekoder**

**8088'in A10-A0 uçları EPROM'un A10-A0 adres girişlerine bağlanır ve geride kalan A19-A11 adres pinleri NAND kapı decodere bağlanır. Dekoder 8088'in bütünü olan 1Mbytelık adreslerden çok sayıdaki 2K'l ık kısımlarından birini seçer. **

**şekil 8-12**

**Bu devrede tek bir NAND kapısı bellek adresini dekod etmektedir. 8088 adres pinlerinde (A19-A11)'in hepsi lojik 1 ise NAND kapısının çıkışı lojik 1 olur. EPROM'u seçen ve low'da aktif olan CE ucuna NAND kapısının çıkışı bağlanır. Hatırlayacağınız gibi CE değeri lojik 0 iken data EPROM'dan okunacak ki bu sadece OE lojik 0 iken mümkündür. OE pini 8088'in RD sinyali yada diğer mikroişlemcilerin MRDC sinyali (bellek oku kontrol) tarafından kontrol edilir. **

**Eğer NAND kapısı tarafından dekod edilen 20 bit binary adresin en soldaki 9 biti 1 ve en sağdaki 11 biti Don't care olarak alındıysa EPROM'un doğru adresi tanımlanır. Önemsiz bitler (Don't care) önc e 0 yapılarak en düşük değerdeki adresi sonra 1 yapılarak en yüksek değerdeki adresi bulunur. Burada 2K EPROM FF800H-FFFFFH bellek adresleri arasında dekod edilir. Bu belleğin 2 Kilobytelık bölümüdür ve 8086/8088 için başlangıç yeridir. (reset location) H er bir devre kendi NAND dekoderine ihtiyaç duyduğu için bu devre hemen hemen hiç kullanılmaz. Aşırı maliyetinden dolayı buna bir alternatif bulundu.**

**3X8 Dekoder (74LS138)**

**Tek başına olamasa bile birçok mikroişlemci temelli sistemlerde kullanılan temel entegre devrelerden biri 74LS138 3x8 dekoderdir. Aşagıdaki şekilde bu dekoderi ve doğruluk tablosunu gösterilmektedir . **

**şekil 8-13**

**Doğruluk tablosunda görüldüğü gibi çıkışlardan herhangi biri farklı zamanlarda 0'a gider. Çıkışlardan herhangi birinin sıfıra gitmesi için üç enable girişi (G2A, G2B ve G1) aktif olmalıdır. Aktif olmalar ı için ise G2A ve G2B 'nin ikisi de 0 ve G1 high olmalıdır. Bir defa 74LS138 aktif hale getirilirse adres girişleri hangi çıkış piminin 0'a gideceğini seçer. 8 tane EPROM'un CE girişlerinin dekoderin 8 çıkışına bağlandığını düşünün Bu çok büyük bir avanta jdır. Çünkü aynı anda 8 farklı bellek elemanını seçebiliriz. **

**Basit Bir Dekoder Devresi**

**Aşağıdaki şekilde görüldüğü gibi dekoder çıkışları 8 tane farklı 2764 EPROM bellek elemanlarına bağlanmışlardır. **

**şekil 8-14**

**Bu dekoder toplam 64Kbytelık bellek için 8 tane 8Kbytelık bellek bloklarından birini seçer. Bu şekil her bir bellek devresi için bellek dizisini ve bellek devrelerinin genel bağlantısını göstermekted ir. 8088'in bütün adres uçları bu devreye bağlanmaktadır. Ayrıca dekoder çıkışları EPROM'ların CE girişlerine ve 8088'in RD sinyalinde EPROM'ların OE girişlerine bağlanmaktadır. Bu sadece seçilen EPROM'un aktif olmasına ve RD lojik 0 olduğu zamanlarda da ta bus yoluyla mikroişlemciye datayı göndermesine müsaade eder. Bu devrede 3 girişli bir NAND kapısıyla A19-A17 adres bitleri bağlanmıştır. **

**Bu üç girişin üçüde high seviyesinde iken NAND kapısının çıkışı dolayısıyla G2B low'a gider. G1 girişi direkt olarak A16'ya bağlanmıştır. Diğer bir deyişle bu dekoderi aktif hale getirmek için ilk 4 adres bitinin (A19-A16)'nin hepsi high olmalıdır. A,B,C adres girişleri mikroişlemcinin A15-A13 adres pinlerine bağlanmıştır. Bu üç adres girişi hangi çıkış pininin 0'a gideceğini ve 8088'in gösterdiği bellek adresindeki EPROM'u tanımlar.**

**1111 xxxx xxxx xxxx xxxx**

**veya**

**1111 0000 0000 0000 0000 = F0000H**

**ile**

**1111 1111 1111 1111 1111 = FFFFFH**

**Yukarıdaki örnek şeması verilen dekoder için tüm adres dizisinin nasıl tanımlandığını gösterir. Adres dizisi F0000H-FFFFFH arasında yer almıştır. Önce binary bit modeli yazılır. Bu durumda A,B,C adr es girişleri don't care durumundadır. **

**CBA**

**1111 0 0 0 0 xxxx xxxx xxxx**

**veya**

**1111 0000 0000 0000 0000 = F0000H**

**ile**

**1111 0001 1111 1111 1111 = F1FFFH**

**Yukarıdaki örnek dekoderin 0 çıkışının, o pine bağlı EPROM'u seçmek için nasıl 0'a götürdüğünü göstermektedir. Eğer dekoderin 1 nolu çıkışına bağlı olan Eprom gerekliyse, 0 nolu çıkışta izlenen yöntemle tamamen aynı yöntem izlenir. Aradaki tek fark CBA girişleri 000 yerine artık 001 değerini almıştır. **

**Çift 2x4 Dekoder (74LS139)**

**Uygulamaları bulunan diğer bir dekoder ise 74LS139'dur. Aşağıda bu dekoderin doğruluk tablosunu ve pin çıkışlarını göstermektedir. 74LS139 herbirinin ayrı adresi, enable pinleri ve çıkış pinleri bul unan iki tane 2x4 dekoderdir. **

**şekil 8-15**

**PROM Adres Dekoder**

**Bir diğer temel adres dekoder daha çok sayıda giriş bacakları kullanılan bipolar PROM’dur. 74LS138'ın adres bağlantısı için kullanılan 6 bacağı vardır. PROM un ise adres dekode etme işlemi için çok d aha fazla girişi vardır. Mesela adres dekoder olarak kullanılan 82S147(512x8) PROM'un 10 giriş 8 çıkış bacağı vardır. Bu hem maliyeti düşürür hem de kart üstünde boşluk yaratır. Aşağıdaki şekilde PROM ile adres dekod işlemini göstermektedir. PROM 8 tane EPROM bellek elemanını seçmek için binary sistemde programlanması gereken bir bellek elemanıdır. PROM'un kendine ait 512 bitlik iç bellek yerini seçmekte kullanılan 9 adres girişi vardır. PROM’un çıkışlarının yüksek empedansa geçmesi ihtimaline karşın kal an girişler ve G topraklanmalıdır. Aksi halde bir yada daha fazla EPROM sistemdeki gürültü nedeniyle seçilebilir. **

**şekil 8-16**

***4.6 8088 BELLEK ARABİRİMİ***

**Bu bölümde 8 bit data bus hattı olan 8088 16 bit data bus'lı 8086,80286 ve 80386SX ve 32 bit data bus’lı 80386DX ve 80486 için bellek arabirim oluşturma ayrı olarak anlatılmıştır. Bellek adreslemede kullanılan metotlar birbirinden biraz farklı olduğundan bölümlere ayrılmıştır. Donanım mühendisleri yada 16 bit ve 32 bit mikroişlemcilerde arabirim oluşturma bilgisini genişletmek isteyenler bütün bölümü anlamalıdır. **

**Bu bölümde bellek arabirimlerinde hem RAM hem de ROM u inceleyecek hem de parity kontrolünü anlatacağız. Ayrıca bellek sistem düzenleyicileri için gerekli olan hata düzeltme şemalarından bahsedeceği z.**

**4.6.1 Temel 8088 Bellek Arabirim**

**8088 mikroişlemcileri bugün mevcut olan 8 bit devre elemanlarıyla bağlamak için ideal hale getiren 8 bit data bus'ı vardır. Basit bir kontroller de onu ideal yapmaktadır. Bu arada 8088'in bellek ile fonksiyonlarını doğru olarak yerine getirmek ve bellek malzemelerini seçmek için bellek sistemi adresi dekod etmeli ve de bellek sisteminin 8088 tarafından kontrol edilmesi için RD, WR, IO/M kontrol sinyallerinin kullanılması gerekir. Bu bölümde 8088 iç in minimum mod konfigürasyonu kullanılmaktadır ve bellek arabirimi için maximum mod sisteminde esasında aynıdır. Tek fark MRDC sinyalini üretmek için IO/M RD ile birleştirilmiş ve MWTC sinyali için IO/M WR ile birleştirilmiştir. Maximum mod kontrol sinyal leri 8288 bus kontroller vasıtasıyla üretilir. Minimum modda bellek, 8088'i 20 adres biti (A19-A0), 8 data bus biti (AD7-AD0) ve IO/M, RD, WR kontrol sinyallerine sahip bir eleman olarak görür.**

**4.6.2 8088’e EPROM Arabirimi Oluşturması**

**Bu bölümde önceki bölümden farklı olarak bekleme durumlarını ve dekoderini etkin hale getirmek için kullanılan IO/M sinyalini anlatacağız. **

**Dekoder küçük bir farkla bağlanır. Çünkü EPROM'un daha yavaş versiyonu olan bu tip 450 ns'lik bir bellek erişim zamanına sahiptir. Daha önce anlatıldığı gibi 8088 5MHz de işlediği zaman belleğin data ya erişimi için 460 ns'e müsaade eder. Dekodere eklenen zaman gecikmesinden (112ns) dolayı 460 ns içinde işlemlerini yerine getirebilmesi imkansızdır. Bu problemi çözebilsin diye dekoderi etkin yapmak ve bekleme durumu generatorü için bir sinyal üretmek amacıyla NAND kapısı eklemeliyiz. Araya sokulan bekleme durumuyla 8088 EPROM'un dataya erişsimi için 660 ns verecektir. Hatırlanacağı gibi bir extra bekleme durumu erişim zamanına 200 ns ekler. Dekoder yada data bus'a eklenen bufferlarda gecikmeler oluşsa bile 450 ns'lik erişim zamanına sahip bellek malzemeleri için 660ns yeterlidir. Görüldüğü gibi dekoder F8000H yerinden başlayıp 64Kbyte'lik belleğin üst sınır alanı seçilir. Belleğin bu bölümü EPROM'dur. Çünkü FFFF0H 8088'in donanım resetinden sonra komu tları yürütmeye başladığı yerdir. Biz genelde bu FFFF0H yerini "cold-start" yeri olarak tanımlarız. Belleğin bu bölümünde yüklü olan JMP komutu içerir ve bu komut daha sonra devam edecek ol an programın yürütülebilmesi için F8000H adresine atlamasını sağlar.**

**4.6.3 8088'e RAM Arabirimi Oluşturma**

**RAM için arabirim oluşturma EPROM için arabirim oluşturmadan biraz daha kolaydır. Çünkü pek çok RAM bellek malzemesi bekleme durumlarına gerek duymaz. RAM için belleğin en ideal bölgesi interruptlar için bir vektor tablosu içeren alt kısımlardır. Interrupt vektorleri yazılım paketleri tarafından sıkça değiştirilir. Çünkü RAM ile belleğin bu bölümünün kodunu çözmek oldukça önemlidir. Aşağıdaki şekilde 16 tane 62256 32Kx8 SRAM 00000H bellek adresinden başlayarak 8088 ile arabirim oluşturmuşlardır. Bu kart 16 tane RAM bellek malzemesini seçmek için 2 tane ve 1 tane de belleğin uygun bölümleri için diğer dekoderleri seçmekte kullanılır. **

**şekil 8-20**

**16 tane 32K'lik RAM 00000H'tan 7FFFFH'a kadar 512Kbytelık belleği doldurur. Birinci dekoder(U4) diğer iki dekoderi seçer. 00 ile başlayan adres U3 'ü seçer ve 01 U9'u seçer. Görüldüğü gibi daha sonra ki gelişmeler için U4 dekoderinin çıkışında extra pinler kalmaktadır. Bu durum RAM ve ikincil bir dekoder ekleyerek 256Kx8 RAM bloklarıyla toplam 1Mx8'lik bellek oluşturulmasına müsaade eder. Şekilde görüldüğü gibi data bus ve kontrol buslarda oldugu gibi adres girişleri de bufferlanır. Tek bir kart yada tek bir sistem cok sayıda eleman içeriyorsa bufferlama önemlidir. Farzedelim ki bunun gibi 3 farklı kart sisteme bağlansın Her bir kartın bufferlanmamış olması sistemdeki adres, data ve kontrol buslar sis temin doğru olarak çalışmasını önlemek için yeterlidir. Aşırı, yükleme lojik 0 çıkışlarının sistemde müsaade edilen maximum değer olan 0.8 V'un üzerine eklemeler yapılacaksa normal olarak bufferlar kullanılır. Eger bellek büyütülmeyecekse bufferlara ihtiyaç duyulmayabilir. **

**4.6.4 Bellek Hata Dedeksiyonu için Parity:**

**Bugünkü sistemlerde oldukça büyük bellek varolduğundan ve devre maliyetleri düşük olduğu için pek çok bellek üreticisi RAM bellek kartlarından parity kontrolünü de eklemektedirler. Parity kontrolü da talarda bulunan 1'lerin sayısını sayar ve tek sayıda mı çift sayıda mı olduğunu gösterir.**

**Aşağıdaki şekil 74AS280 parity generator/dedektor entegre devresini göstermektedir. Bu elemanın 9 girişi vardır ve girişlerindeki 9 bitlik bilgi için tek veya çift parity üretir. Ayrıca girişlerine b ağlanan 9 bitin paritisini kontrol eder. Aşagıdaki şekil parity üretimi ve dedeksiyonunun yapıldığı 16Kx8 statik RAM sistemini gösterir. 74AS280 4 farklı 4Kx1 parity biti üretir. Burada 8 data bus kanalı parity generatorunun A-H uçlarına bağlamışlardır. I topraklanır. Böylece data bus üzerinde 1'lerin sayısı çift olunca even çıkışı, 1 olan değeri parity RAM'ına yüklenir. Eğer 1'ler tek sayıda görülür ise Parity RAM'ına 0 yüklenir. Burada belleğe yazılan ve parity bitini içeren her bir bytelık data için te k parity yüklenir. Bu durumda kontrol ediciye bütün girişler bağlanır. A-H girişleri Data RAM çıkışlarından ve I girişi Parity RAM bağlanır. Parity tek ise hepsinin doğru olduğu kabulüyle 74AS280'nin even parity çıkışı lojik 0 olur.**

**şekil 8-22**

**Bu pin 8088'in NMI girişi olarak adlandırılan pinine bağlanır. NMI girişi asla kapatılmamalıdır. Eğer lojik 1 yapılırsa programın komut yürütme işi durdurulur ve bellek sistemi tarafından parity hata sının dedekte edildiği özel bir alt programa girer.**

**Parity hata uygulaması zamanlanır. Böylece NMI girişi oluşmadan önce bellekten data okuma son durumunu alır. Bu işlem belleğin bu bölümünden RD çevriminin sonunda parity kontrol bitinin latchlandiği D tipi Flip-Flop tarafından kontrol edilir. Bu yolla generator çıkışı NMI tarafından örneklenmeden önce bellek bilgiyi okumak için yeterli zamana sahip olur ve generator vasıtasıyla geçirir.**

**4.6.5 8086, 80286 ve 80386SX Bellek Arabirimi Oluşturma**

**8086, 80286 ve 80386SX mikroişlemcileri 8088'den 3 şekilde farklıdır: **

**8088 üzerindeki 8 bitlik data bus yerine 16 bit bus'ı vardır. **

**8088'in IO/M pin 8086 üzerinde M/IO'dur. **

**BHE adında (bus high enable) yeni bir kontrol sinyali vardır. A0 adres biti de farklı bir şekilde kullanılır. **

**8086 ve 80286/80386SX arasında ise çok küçük farklılık mevcuttur. 80286/80386SX 8086'daki 20 bit adres bus (A19-A0) 24 bitlik (A23-A0) adres bus içermektedir. 80286 ve 80386SX mikroişlemciler RD ve WR ye rine MRDC ve MWTC kontrol sinyallerini içerirken 8086 M/IO sinyaline sahiptir.**

**16 Bit Bus Kontrol**

**8086, 80286 ve 80386SX'in data bus hattı 8088'in data bus hattının iki katı genişliktedir. Daha geniş data bus genişliği daha önce karşılaşmadığımız bir dizi probleme sebep olmaktadır. 8086, 80286 v e 80386SX datayı herhangi bir 16 bitlik yere veya 8 bitlik yere yazabilmelidir. Bunun anlamı 16 bit data bus her biri 8 bit genişliğinde olan 2 bölüme bölünmelidir. Çünkü mikroişlemci her biri yarıma (8 bit) veya her iki yarıma birden (16 bit) yazabilme lidir. Aşagıdaki şekil belleğin iki bankını gösteriyor. İlk bank (low bank) bütün çift numaralı bellek bölümünü diğer bank (high bank) ise bütün tek numaralı bellek bölümünü gösterir.**

**ŞEKİL **

**8086/80286/80386SX data transferini sağlamak için kullanılan bellek banklarından birini veya ikisini de seçmek için BHE A0 adres biti kullanılır. Bank seçimi iki yolla yapılır.**

**1. Her bir bellek bankına yazımı seçmek için üretilen iki ayrı write(yazma) sinyali **

**Her bir bank için kullanılan ayrı dekoderler **

**Ayrı Bank Dekoderleri**

**Ayrı bank dekoderlerin kullanılması 8086, 80286 ve 80386 için bellek adreslerinin dekod edilmesinde genelde en etkisiz yoldur. Bu metot bazen kullanılır. Aşagıdaki şekil (8-29) 8086 mikroişlemci (20 bit adres) için 64K RAM belleğin seçiminde kullanılan 2 tane 74LS138 dekoderlerini temsil etmektedir. A0 pini G2A'ya bağlamaktadır. Çünkü dekoder bütün uçları aktif oluncaya kadar aktif ol maz. A dekoderi 16 bitlik işlemler için B dekoderi ise 16 bitlik işlemler veya low banktan 8 bitlik işlemler için aktif olur. **

**ŞEKİL**

**Bu iki dekoder ve onların kontrol ettiği 16 tane 64Kbyte RAM 1M 8086 bellek sistemini temsil etmektedir. Yani iki dekoder tüm bellek için kullanılır. Bu şekilden de görüldüğü gibi A0 adres pini bellek ye rine dekodere bağlanmıştır. Ayrıca A1 biti bellek adres girişi olan A0'a ve A2 de A1'e bağlanır. Bunun sebebi 8086'nın A0'ı dekoder A2’ye bağlandığı için belleğe tekrar bağlamak gereksizdir. Eğer A0, A0 adres pinine bağlansaydı her bir bellek bankındaki b ütün bellek birimleri kullanılırdı. Bunun anlamı A0 A0'a bağlansaydı belleğin yarısı kullanılmayacaktı.**

**Ayrılmış Bank Yazma Strobları**

**Uygun bankı seçmek için en etkili yol her bir bellek bankı için ayrı yazma strobu bağlamaktadır. Bu teknik 16 bit genişliğinde bir belleği seçmek için sadece bir dekodere ihtiyaç duyar. Bu maliyeti düşürür ve sistemdeki malzemelerin sayısını azaltır. **

**Aşağıdaki şekil (8-27) bellek için üretilen ayrılmış 8086 write stroblarını göstermektedir. Burada 74LS32 OR kapısı low bank seçimi için (LWR) WR ile A0'ı High bank (HWR) için BHE ile WR sinyaline birleş tirilmektedir. 80286/80386SX için write strobları WR yerine MWTC kullanılarak üretilir. Ayrılmış write strobu kullanan bellek sistemleri hem 8 bit sistemden (8088) hem de ayrılmış bellek bankı kullanan sistemden farklı şekilde yapılanmışlardır. **

**ŞEKİL **

**Ayrılmış yazma strobu kullanan sistemdeki bellek 16 bit genişliğinde bellek olarak dekod edilir. Mesela bir bellek sisteminin 64K bytelık SRAM bellek içereceğini kabul edelim. Bu bellek 32K bytelık b ellek elemanlarına ihtiyaç duyarlar. Böylece 16 bit genişliğinde bellek yapılabilir. Bellek 16 bit genişliğinde olduğundan ve diğer devre banka yazma sinyali ürettiği için A0 adres biti dont care durumuna gelir. **

**Aşağıdaki örnek (8-6) 060000H-06FFFFH bellek birimlerine 16 bit genişliğindeki belleğin 80286 ve 80386 mikroişlemci için nasıl dekod edildiğini gösterir. Bu örnekte dekoder için A0 biti don't care du rumunda olur. A1-A15 her bir bellek elemanının A0-A14 adres pinlerine bağlanır ve dekoder (PAL16L8) her bir bellek elemanı için etkin olur. **

**ŞEKİL**

**Aşağıdaki şekilde (8-28) gösterilen basit devre her iki bellek için dekod işlemini ve üretilen iki ayrı write strobunu göstermektedir. **

**ŞEKİL**

**Aşağıdaki şekil (8-29) 8086 mikroişlemci için EPROM ve RAM bölümlerini içeren küçük bir bellek sistemini göstermektedir. Burada F0000H-FFFFFH yerlerinde bulunan 32Kx16 bitlik belleği oluşturan 4 ta ne 62256 RAM bulunmaktadır. **

**ŞEKİL**

**Bu devre bir yarısıyla EPROM'un yarısını yada diğer yarısıyla RAM'ın herhangi bir yarısını seçmekte kullanan 74LS138 dual 2x4 hatlı dekoder kullanır.**

**Daha önceki gibi 8 bit genişliğinde bir belleği dekod etmektedir. Netice olarak RD strobu tüm EPROM OE girişleri ve bütün RAM'ların G girişlerine bağlanır. **

**8086 sadece 8 bitlik datayı okuduğundan ve geriye kalan diğer 8 bitlik datanın uygulamaları 8086'nın işlemlerinde önemsizdir. LWR ve HWR strobları RAM'ın farklı banklarına bağlanır. Eğer mikroişlemci 16 bit veya 8 bit yazıyorsa burada bir problem oluşur. Eğer 8086 16 bitlik belleğe yazıyorsa heri ki LWR ve HWR low'a gider ve her iki bellek bankı için W pinleri etkin olur. Fakat 8086 8 bit genişliğinde yazıyorsa o zaman sadece bir bellek bankına yaz ar. ****Bellek yazımı için birinci seferde tekrar farklı bir bellek bankı oluşturulur. ****EPROM dekoder sinyali 8086'nın wait state generatoruna gönderilir. Çünkü EPROM genellikle bir wait state'e ihtiyaç duyar. Bu sinyal EPROM'un seçilebilmesi için wait state durumu oluşsun diye EPROM dekoder bölümünü seçmek için kullanılan NAND kapısından gelir. Aşağıdaki şekil (8-30) PAL16L8 dekoder kullanan 80386SX mikroişlemciye bağlı bellek sistemini göstermektedir. **

**ŞEKİL**

**Bu arabirim herbiri 4 tane 64Kx8'lik 2752 yani toplam 256K byte'lık EPROM'dan ve 4 tane 32Kx8'lik 62256 yani toplam 128 Kbyte'lık SRAM'dan oluşur. şekildede görüldüğü gibi PAL ayrıca bellek bankalarını n yazma sinyalleri olan LWR ve HWR'ı üretir. Buradan anlaşıldığı gibi çok sayıda malzemeye ihtiyaç duyulan bellek arabiriminin görevini sadece PAL yerine getirir. PAL SRAM için 000000H-01FFFFH ile EPROM için F00000H-FFFFFFH arasındaki bellek adreslerini d ekod eder. **

**80386DX ve 80486 Bellek Arabirimi**

**8 bit ve 16 bitlik bellek sistemlerindeki gibi mikroişlemci belleği data bus ve bellek bankalarını ayıran kontrol bus sayesinde arabirim olarak görür. 32 bit data bus’a ve bir yada 2 yerine 4 tane be llek bankına sahiptir. Diğer farkı hem 80386DX ve 80486 (hem SX hem de DX) ölçülebilen sayıda adres bitlerinden dolayı birleştirilmiş dekoderler yerine PLL dekoderlere ihtiyaç duyan 32-bit adres bus'a sahiptir.**

**Bellek Bankları**

**Hem 80386DX hem de 80486 için bellek bankaları aşağıdaki şekilde (8-31) gösterilmiştir. **

**ŞEKİL**

**Görüldüğü gibi bu büyük bellek sistemleri her biri 1GByte'a varan 4 tane 8 bitlik bankdan oluşmaktadır. Bank seçimi BE3, BE2, BE1, BE0 banka seçim sinyalleri tarafından yapılmaktadır. Eğer 32 bit transfe r edilecekse bütün banklar seçilir. Eğer 16 bit transfer edilecekse iki bank (genelde BE3 ve BE2 veya BE1 ve BE0) seçilir. Eğer 8 bit transfer edilecekse tek banka seçilir. **

**Tıpkı 8086/80286/80386SX'te olduğu gibi 80386DX ve 80486 her bir bellek bankı için ayrılmış yazma strob sinyallerine ihtiyaç duyarlar. Bu ayrı yazma strobları aşağıda (8-32) gösterildiği gibi basit bir OR kapısıyla yada diğer lojik malzemelerle yapılır. **

**ŞEKİL**

**32 Bit Bellek Arabirimi**

**Daha önceki kısımdan anlaşılacağı gibi 80386SX ve 80486 için bellek arabirimi 4 banka için write strobu üretilmesine ve de 32 bit adresin dekod edilmesine gerek duyarlar. 80386SX ve 80486 için bellek arabirimiyle uyum sağlayabilen 74LS138 gibi bir entegre dekoder yoktur. Ayrıca 32 bit genişliğinde bellek dekod edilirken A0 ve A1 "don't care" durumundadır. Bu bitler mikroişlemci içinde bank seçme sinyalleri üretmek için kullanılır. Ayrıca görüldüğü gi bi A2 adres bus biti bellek pini A0'a bağlanır.**

**aşağıdaki şekil (8-33) 80486 mikroişlemci için 256Kx8 bellek sistemini gösterir. Bu arabirim 32Kx8 SRAM bellek birimi ve 2 tane PAL16L8 elemanı kullanır. İki eleman mikroişlemci üzerinde bulunan adr es hatlarının sayısından dolayı gerek duyulur. Bu sistem SRAM'ın 02000000H-0203FFFFH yerlerinde bulunur.**

**ŞEKİL**

**Bu bölümde bahsedilmemesine rağmen 80386DX ve 80486 mikroişlemcileri bellek erişimi için bekleme durumuna ihtiyaç gösteren çok yüksek clock hızına sahiptir. Arabirim bekleme durumu generatorun ile hı zlı mikroişlemcilerde bulunan diğer elemanlar cache(keş) bellek ve interleaved bellek sistemleridir.**

**Dinamik RAM**

**RAM bellek çoğunlukla büyük olduğu için maliyeti yüksek olan çok sayıda SRAM'a veya çok daha az maliyeti olan sadece birkaç DRAM'a ihtiyaç duyarlar. DRAM bellek daha önce bahsedildiği gibi oldukça ko mplextir. Çünkü adres multipleksine, refresh işlemine ihtiyaç uyarlar. Entegre devre üreticileri adres multiplekser ve refresh işlemi için gereken zamanlama devresini sağlayan bir DRAM Kontrol Devresi sağladılar. **

**DRAM sadece 2-4ms'de data’yı yeniler ve adres girişlerinin multipleks edilmesine ihtiyaç duyarlar. Kısa bir periyot zamanında yüklerini kaybeden iç kondansatörlerde bilgiyi depolamak için DRAM periyo dik olarak tazelenmelidir. DRAM'ın tazelenmesi için bellek bölümünün içerikleri periyodik olarak okunmalı ve yazılmalıdır. Her bir okuma ve yazma otomatik olarak DRAM'ın tamamını tazeler. Tazelenen bitlerin sayısı bellek elemanının boyutuna ve iç yapısına bağlıdır.**

**Refresh çevrimleri okuma yazma yapılarak veya okuma yada yazma yapılmayan özel bir refresh çevrimi ile yapılır. Refresh çevrimi tamamen DRAM'ın içinde olur ve sistemdeki diğer bellek elemanları işler ken gerçekleşir. Bu tip refresh hem hidden refresh, hem transparan refresh, hem de bazen stealing çevrimi olarak adlandırlır. Diğer bellek elemanları fonksiyonlarını yerine getirirken gizli refresh gerçekleşsin diye sadece RAS çevrimi, tazelenecek olan sa tır bitlerini seçmek için DRAM içinde satır adreslerini stob eder. Bu data’ları depolayan iç kondansatörleri tekrar yükler. Bu tip tazeleme gizlidir. Çünkü mikroişlemci belleğin diğer bölümlerini okuyup yazarken meydana gelir. DRAM'ın iç yapısı bir dizi s atır ve sütundan meydana gelir. Bir 256Kx1 DRAM her biri 256 bit içeren 256 kolondan veya her biri 64Kbitlik 4 bölümden oluşan satırlardan meydana gelir.**

**Herhangi bir bellek yeri adreslendiğinde kolon adresi 1024 bitlik kolondan (DRAM'ın her bölümünden biri, iç bellek kelimesi) kolon adresini seçer. Aşağıdaki şekil (8-34/8-35) 256Kx1 DRAM'ın iç yapısı nı ve zamanlama diyagramını temsil etmektedir. **

**ŞEKİL**

**RAS ile yazma veya okuma arasındaki tek temel fark genellikle 7 veya 8 bit binary sayıcı tarafından elde edilen tazeleme adresi kullanılmasıdır. Sayıcının tipi refresh yapılmış olan DRAM'ın tipi tarafınd an belirlenir. Refresh sayıcı her bir refresh çevriminin sonunda arttırılır. Böylece DRAM'ın tipine bağlı olarak bütün satırlar 2 veya 4 ms'de arttırılır.**

**Eğer 4 ms içinde 256 satır tazelenecekse 256Kx1 DRAM'da olduğu gibi tazeleme özelliklerini karşılayabilmesi için en azından her 15.6**μ** s'de refresh çevrimi aktif olmalıdır. Mesela 5MHz'de işleyen 8086/8088 için yazma yada okuma işlemi yapmak 800ns tutar. Her 19 bellek okuma veya yazması için bellek sistemi ya tazeleme çevrimine girmek zorunda kalcak yada bellek datalarını kaydedecektir. Bu yüzden DRAM her 15.6**μ** s'de refresh çevrimi yapmak zorundadır. Dinamik RAM kullanarak bilgileri korumanın küçük bir bedeli olarak bilgisayar zamanının %5'ini kaybetmektedir. **

***4.7 DRAM Kontrol Elemanları***

**Bu bölümde TMS4500A DRAM kontrol elemanı üzerinde duracağız. Bütün DRAM kontrol elemanları gibi TMS4500A adres multiplekser ve bazı tazeleme isteklerinin bulunduğu sistemi içerir. Fakat diğerlerinden farklı olarak refresh esnasındaki işlemi düzenlemek için özel bir yüksek frekans clock sinyaline ihtiyaç duymaz. Unutulmamalı ki TMS4500A iç multiplekser, tazeleme sayıcısı ve refresh işlemini yapmak için gerekli olan zam anlamaya sahiptir.**

**ŞEKİL**

**4500Anın bacak bağlantıları**

**Pin Tanımları: TMS4500A'nın işlemi tam olarak anlamak pinlerin fonksiyonlarının anlatılmasına bağlıdır. **

**RA7-RA0 (Satır Adres Girişleri) **

**Bu pinler mikroişlemcilerin adres bus hatlarına bağlanır. Bunlar çoğunlukla A7 ve A0 adres bus bitleridir. **

**CA7-CA0 (Kolon Adres Girişleri) **

**Bunlarda adres bus hattına bağlanır. Eğer satır girişleri A7-A0,'a bağlanırsa o zaman bu girişler A15-A8'e bağlanır. Bu hatların sırası sistemin işleyişini etkilemez.**

**MA7-MA0 (Bellek Adres Çıkışları) **

**Bunlar direk olark DRAM adres pinleri A7-A0'a bağlanır. **

**ALE( Adres Latch Enable) **

**RA7-RA0, CA7-CA0 ve REN1'e bağlı olan 6 tane adres girişini latchlamak için kullanılır. Bu giriş çevrimi sağlayıp aktif olmak için mikroişlemciden ALE'e bağlanmak zorundadır.**

**CS(Chip Seçme Girişi) **

**ALE'in 1'den 0'a geçişinde lojik 0 ise DRAM kontrol elemanına bağlı olan DRAM'lar için bellek okuma veya yazmasına başlar.**

**REN1(Enable Girişi) **

**Dram kontrol elemanına bağlı olan DRAM banklarından birini seçer. (İki tane RAS çıkışı vardır.) REN1 high olursa RAS1 seçilir veya OLE olursa RAS2 seçilir. **

**ACR (Okuma Erişim Kontrol Girişi) **

**0'dan 1'e geçişte bellek okuma sinyalini bitirir. Bu pin 8086/8088 için minimum mod’da RD kontrol sinyaline veya maximum mod’da MRDC kontrol sinyaline bağlanır.**

**ACW (Yazma Erişim Kontrol Girişi) **

**0'dan 1'e geçişte yazma çevrimini bitirir. WR^ veya MWTC^'ye bağlıdır. **

**CLK (Clock Girişi) **

**Mikroişlemcinin sistem clock girişine bağlıdır. **

**REFREQ (Tazeleme İsteği) **

**Tazeleme çevrimi başlar veya çıkış kullanıldığında devam etmekte olan iç refresh çevrimi gösterir.**

**CAS( Kolon Adres Strobu) **

**Her iki bellek bankası için bütün DRAM belleklerin CAS girişlerine bağlanır.**

**RAS1, RAS2 (Satır Adres Strobları) **

**DRAM'ın RAS girişlerine bağlanır. Refresh işlemi için her iki pin 0'a gider. Fakat normal bir okuma ve yazma esnasında sadece biri low'a gider. REN1 bellek işleyişi esnasında hangi RAS pininin low'a gide ceğini seçer. **

**RDY (Ready Çıkışı) **

**Bir 8086/8088 sistemindeki 8284A clock generatorun RDY girişine bağlanır DRAM kontrol elemanı iç refresh çevrimini de iken RDY aktif olur.**

**TWST (Zamanlama/Bekle Strap Girişi) **

**FS1 ve FS0 girişleri ile birlikte kullanıldığında beklemeler ve/veya temel zamanlama zorunluluklarını seçer. Lojik 1 her bellek erişimi için bir bekleme durumu oluşturur. **

**FS0,FS1(Frekans Seçme Girişleri) **

**Değişik modları ve frekans optionlarını seçer.**

**TMS4500A Çalışması**

**ŞEKİL**

**Yukarıdaki şekil (8-37) minimum mod’da iken 8088 mikroişlemcilerin bus hatlarına bağlanan DRAM kontrol elemanlarının temel bağlantısını göstermektedir. Burada RD ve WR pinleri ACR ve ACW pinlerine ba ğlanmışlardır. CS girişi en çok değerlikli 3 adres bitini dekod eden 4 girişli bir NAND kapısına bağlanmıştır. REN1 A16 adres bus hattına bağlanmıştır ki böylece bellek banklarından birini seçecektir. Eğer A16 high ise RAS1'e bağlı olan bank seçilecek eğ er low ise RAS0'a bağlı bank seçilecektir. Bu örnekte toplam 128Kx8'lik bellek için 64Kx8'lik DRAM'lardan iki bank seçilir. Adres seviyesi 00000H'tan başlar ve 1FFFFH 'a kadar devam eder. **

**Programlama pinleri TWST, FS1 ve FS0 0,1,1 olarak seçilir. Böylece bekleme olmaz, tazeleme her 61 clockta bir olur ve her refresh işlemi için 4 clock geçer. Bu daha önce hesaplanan 15.6****m**** s olan toleransının içinde bir değer olan her 12.2**μ** s'de bir defa refresh sağlanmaktadır. Her 61 clock peryodunda iç clock sinyali üretildiği zaman bir iç refresh isteği oluşur. Diğer 4 clock darbesi ile toplanan asıl bus çevrimi tamamlanana kadar talep geciktirilir. Talep yerine getirildiğinde RDY pini lo jik 0'a gider. Bu durum DRAM kontrol elemanı belleği tazelerken oluşacak bekleme durumlarına neden olur. Tazelenme tamamlandıktan sonra daha sonraki refresh isteğine kadar bus hattı okuma veya yazma yapmak için boşaltılır. **

**Aşağıdaki şekil (8-38) TMS4500A için refresh isteği ve refresh işlevi sırasındaki zamanlama diyagramını gösterir.**

**ŞEKİL**

**DRAM Arabirimi**

**ŞEKİL**

**Yukarıdaki şekil (8-39) 20 bit multipleks edilmiş adresi sağlayan 10 adres pinine sahip bir 1MxSIMM (Tek hat Bellek Modülü) göstermektedir.**

**CAS ve RAS girişleri seçmek (CAS ) ve bellek modülüne adresleri strob etmek için kullanılır. CAS9 9. parity bitini seçer. Bu eleman ayrıca 1Mx8 modülü (42100C8) olarak da mevcut bulunmaktadır. 4210 0C9'un pinleri 9. parity biti için 421000C8 üzerine bağlanmamaktadır ve üzerinde sadece 8 bellek elemanı vardır. **

**Çok daha yeni mikroişlemci temelli bilgisayar sistemlerinde SIMM kullanılmaktadır. Temel boyutları 256Kx9, 1Mx9 ve 4Mx9'tur. Son zamanlarda 16Mx9 SIMM temel yeri almıştır. **

**Aşağıdaki şekil (8-40) 80386DX ve 80486 için dizayn edilmiş 8Mx8 bellek sistemini göstermektedir. Bu sistem CAS ve RAS'ı üreten bir devreyi göstermemektedir. Fakat adres multipleksi göstermektedir. A yrıca görüldüğü gibi bank yazma strobları üretmek ve de bellek adresini dekod etmek için PAL16L8 kullanılmıştır. Buradaki bellek sistemi 00000000H'tan 007FFFFFH'a kadar değişim 8Mbyte'lık belleği sağlamak için dekod edilir.**

**ŞEKİL**

**5. TEMEL I/O ARABİRİMİ**

***5.1 I/O Komutları ***

**Komut seti bilgiyi I/O birimine aktaran (OUT) ayrıca I/O biriminden okuyan (IN) tek tip komut içermektedir. Komutlar (INS ve OUTS komutları 8086/8088 hariç bütün versiyonlarda bulunur.) data dizilerinin bellek ve I/O birimleri arasında transferi için kullanılır. IN ve OUT komutlarından ikisi de datayı I/O birimi mikroişlemci akümülatörleri (AL, AX ve EAX) arasında transfer eder. I/O adresi DX registerinde 16 bit I/O adresi olarak veya opkodu hemen tak ibin byte olarak 8 bit I/O adresi şeklinde depolanır.**

**8 bitlik form komut ile depolandığından genellikle ROM'a depolanır.- Intel bu formu sabitlenmiş adres olarak adlandırır. DX'te bulunan 16 bit I/O adresi registere depolandığı için adres değiştirileb ilir. INS ve OUTS komutlarının her ikisi de DX registerinde bulunan değişken I/O adresi kullanır.**

**Ne zaman data IN ve OUT komutunu kullanarak transfer edilirse I/O adresi çoğunlukla port numarası olarak adlandırılır ve adres bus hattında görülür. Port numarasını bellek adresinin dekod edilmesiyl e aynı yöntemle harici I/O arabirimi dekod eder. 8 bit sabitlenmiş port numarası A15-A8=0000 0000 olacak şekilde A7-A0 adres bus hatlarında görülür. Bu ilk 256 I/O port adresine (00H-FFH) hem sabit hem de değişken I/O komutları fakat 0100H-FFFFH arasınd aki her I/O adresine değişken I/O adresi ile erişilebilir demektir. Pek çok özel görevli sistemde adresin sadece en sağdaki 8 biti dekod edilir. PC'de 16 adres bus biti PC'lerde bulunan çok sayıda I/O için kullanılan 0 0XX-03XXH ile dekod edilir. INS ve OUTS komutları DX registerini kullanarak I/O birimini adresler fakat IN ve OUT gibi datayı akümülatör ve I/O birimi arasında taşımaz. Yerine bu komutlar datayı bellek ve I/O birimi ara sında iletir. Bellek adresi INS komutu için ES:DI tarafında, OUTS komutu için DS:SI tarafında yerleştirilir. Diğer dizi komutları gibi pointerlerin içerikleri özel olarak yönelme durum bayrağı (DF) tarafından azaltılır veya arttırılır. INS ve OUTS'un he r ikisi de I/O ve bellek arasında birden fazla byte yada wordun transfer edilmesine müsaade eder. REP sabiti ile sabitlenebilir. **

***5.2 İzole edilmiş ve Memory- Mapped I/O***

**Birbirinden tamamen farklı iki tane mikroişlemciyle I/O'nun arabirim oluşturma metodu vardır. Bunlar İzole edilmiş I/O ve Memory-mapped I/O 'dur. İzole edilmiş I/O'da IN, INS, OUT, ve OUTS komutl arı datayı mikroişlemci akümülatörü veya bellek ile I/O birimi arasında taşır. Memory-mapped I/O'da ise belleğe başvuran bütün komutlar için transfer yapar. Her iki tip I/O'da kullanılmaktadır. **

**5.2.1 İzole Edilmiş I/O **

**Intel mikroişlemci temelli sistemlerde kullanılan en temel I/O transfer tekniğidir. İzole edilmiş terimi ayrı I/O adres uzayında bulunan bellek sisteminden I/O yerlerinin nasıl izole edildiğini anlatır. Aşağıdaki şekil (9-1) 8088 mikroişlemci için hem izole edilmiş hem de memory-mapped adres uzayını göstermektedir. İzole edilmiş I/O birimi için (bunlar port olarak adlandırılır) bellekten ayrıdırlar. Bunun sonucu olarak kullanıcı I/O birimi için bu boşlu ğun hiçbirini kullanmayarak belleğin tamamı için genişletebilir. İzole edilmiş I/O ‘nun dezavantajı I/O ile mikroişlemci arasındaki data transferi IN, INS, OUT ve OUTS komutları ile yapılmalıdır. I/O uzayı için ayrı kontrol sinyalleri I/O okuma (IORC) ve ya I/O yazma (IOWC) işlemlerinin gösterilmesini sağlamaktadır. Bu sinyaller I/O elemanını seçmekte kullanılan adres bus üzerinde I/O port adresini gösterir. PC’ler izole edilmiş I/O portları çevresel elemanların kontrolünde kullanılır. Kural olarak, 8 bi t port adresi zamanlama ve keyboard arabirimi gibi sistem üzerinde bulunana kartlara erişmek için ve 16 bit port ise video ve disk sürücü sistemlerinde olduğu gibi seri ve paralel portlara erişmek için kullanılır.**

**ŞEKİL**

**5.2.2 Memory-mapped I/O **

**İzole edilmiş I/O’dan farklı olarak memory-mapped I/O IN, INS, OUT ve OUTS komutlarını kullanmaz. Yerine mikroişlemci ile bellek arasında data transferi yapan bütün komutları kullanılır. Memory-mapped I/ O, bellek haritasında bir bellek yeri olarak çalışır. Memory-mapped I/O’nun en temel avantajı bütün bellek transfer komutları I/O birimine ulaşmak için kullanabilmektir. Bu bellek uygulamal arının sayısını azaltmaktadır. (Diğer avantajı ise dekod etme işlemi için gerekli devresel ihtiyaçları azaltan memory-mapped I/O sisteminde IORC ve IOWC’nin fonksiyonu yoktur. )**

***5.3 PC I/O Haritası***

**PC’ler özel fonksiyonlar için I/O haritasının bir bölümünü kullanırlar. Aşağıdaki şekil (9-2) PC için I/O haritasını göstermektedir. 0000H-3FFH arasındaki I/O uzayı normalde bilgisayar sistemi iç in ayrılmıştır. 0400H-FFFFH arasındaki I/O portları genellikle kullanıcı uygulamaları için kullanılır. 80287 aritmetik yardımcı işlemci iletişim için 00F8H-00FDH I/O adresini kullanır. 0000H-00FFH adreslerindeki I/O portlarına sabit port I/O komutları ile erişilir ve 00FH’ın üstündeki portlara değişik I/O port komutlarıyla erişilir. **

**ŞEKİL**

***5.4 TEMEL GİRİŞ/ÇIKIŞ ARABİRİMLERİ***

**Temel giriş birimi üç durumlu buffer düzenidir. Temel çıkış birimi ise data latchlerdir. IN terimi dataların I/O biriminden mikroişlemci birimine ve OUT terimi ise dataların mikroişlemci çıkışınd an I/O birimine taşınmasını sağlar. **

**5.4.1 Temel Giriş Arabirimi**

**Üç durumlu bufferlar aşağıdaki şekilde (9-3’te) gösterilen 8 bit giriş portunu oluşturmakta kullanılır. Görüldüğü gibi harici TTL data buffer girişlerine bağlanmıştır. Bufferların çıkışı data bus hattına bağlanmıştır. Data bağlantıları mikroişlemcinin versiyonuna bağlıdır. Mesela 80486’nın D31-D0 data bus bağlantısı varken 8088’in D7-D0 ‘dır. **

**ŞEKİL**

**Aşağıda şeması verilen (9-39) devre SEL lojik 0 olduğunda data bus’a bağlanan 8’li anahtar içeriğini okumasına izin verir. Mikroişlemci IN komutunu yürüttüğü zaman, I/O port adresi SEL’de lojik 0 üretmek için dekod edilir. 74ALS244’ün çıkış kontrol girişlerinde (1G ve 2G) yer alan 0, data giriş uçlarının (A) data çıkış uçlarına (Y) bağlanmasına neden olur. Eğer 74ALS244 bufferın çıkış kontrol uçlarında 1 olursa devre data bus ile bağlantısını tamamen kes en yüksek empedans moduna geçer. **

**ŞEKİL**

**Temel giriş birimleri bazen aşagıdaki şemada olduğu gibi devreden ayrı bir bölüm olarak görülür. Bazen de programlanabilir. I/O biriminin içinde yapılır. 16 ve 32 bit giriş birimleri değişik mikroişl emci versiyonları ile çalışmak üzere düzenlenebilmektedir. Fakat bu 8 bit data kadar basit bir şekilde olmamaktadır. 16 bitlik data bus ile arabirim oluşturmak için aşağıdaki devre, 16 bit data ile bağlanmak üzere devre 2 tane 74ALS244 içerir. 32 bit data ile arabirim oluşturmak için ise 4 tane kullanılır. **

**şekil 9-3**

**5.4.2 Temel çıkış Arabirimi**

**Temel çıkış arabirim mikroişlemciden dataları alır ve genellikle bazı dış birimler için tutar. Latchler tıpkı giriş devresindeki bufferlarda olduğu gibi I/O birimine doğru gerçekleştirilir. Aşağı daki şekil (9-4) 8 bit LED’in mikroişlemci ile 8 data latch vasıtasıyla nasıl bağlandığını gösterir. Latch, sayıyı data bus’tan alarak mikroişlemci vasıtasıyla depolar. Böylece LED 8 bit binary sayıyı gösterir. Mikroişlemci OUT komutunu yürüttüğünde datal ar 1**μ** s’den çok daha az bir süre data bus’ta kaldığı için latchlere ihtiyaç duyulur. Latch olmadan LED’lerin yanıp sönmesini asla göremeyiz. **

**OUT komutu yürütüldüğü zaman AL, AX veya EAX data bus yoluyla latcha transfer edilir. Buradan 74ALS374 octal latchın D girişleri data bus hattına çıkış datalarını tutmak için bağlıdır ve Q çıkışları ise LED’e bağlanır. **

**Q çıkışları lojik 0 olduğu zaman LED’ler yanar. OUT komutu yürütüldüğü zamanlarda, (SEL sinyali latchı aktif yapar.) data bus’tan latch çıkışlarında dataların tutulması gerçekleşir. Datalar sonraki OUT komutunun yürütülmesine kadar tutulur. **

**---------------------------------------------------------------------------------------------------------------**

***5.5 Handshaking***

**Pekçok I/O birimi bilgileri mikroişlemcilerden çok daha yavaş bir hızla kabul eder veya işletir. Handshake veya tarama (polling) olarak adlandırılan diğer bir I/O kontrol metodu I/O birimi i le mikroişlemciyi senkronize eder. Handshake işlemine ihtiyaç duyan örnek bir devre saniyade 100 karakter (CPS) yazan paralel printerdir. Dolayısıyla mikroişlemci ile printerın hızı eş yapı lmalıdır. Şekil 9-5’de printerde bulunan tipik giriş çıkış bağlantılarını göstermektedir. Burada, data seri data bağlantıları olan D7-D0 vasıtasıyla taşınır. BUSY printerin meşgul olduğunu gösterir STB^ yazma işlemi için printere dataları göndermekte kull anılan bir clock pulsidir.**

**Printer tarafından yazılacak olan ASCII datalar D7-D0 üzerinde bulunurlar ve puls STB^ ucuna uygulanır. Strob sinyali yazılabilmesi için printere dataları gönderir. Printer dataları alır almaz, bilgileri yazmakla meşgul olduğunu gös teren BUSY pininde lojik 1 görülür. Eğer printer meşgul ise, mikroişlemci bekler aksi halde printere diğer ASCII karakterleri gönderir. Printerın interrogating (sorgulama) işlemi handshaking veya polling olarak adlandırılır. Örnek 9-1 printer BUSY bayrağı nı test eder ve eğer meşgul değilse dataları gönderen basit bir işlem dizisini göstermektedir. Eğer sadece BUSY bayrağı Printerin meşgul olmadığını gösteren lojik 0 durumunda ise Print işl em dizisi kodlanılan BL’nin içeriklerini veya ASCII’leri yazar. **

***5.6 I/O Port Adresi Dekod Etme***

**I/O port adresinin dekod edilmesi (memory mapped I/O birimleri için) bellek adres dekod etme işlemi ile son derece benzerdir. Tabiki memory-mapped I/O dekod edilmesi üstünde durmayacağız. Çünkü IORC ^ ve IOWC^ kullanılmadığı için IN ve OUT komutları bellekteki gibi uygulanır. Memory-mapped I/O kullanma kararı bellek sisteminin büyüklüğü ve I/O biriminin sistemdeki yeri ile tanımlanır. Bellek dekod etme ile izole edilmiş I/O dekod etme arasındaki teme l fark dekodere bağlı olan adres pinlerinin sayısıdır. Bellek için A32-A0, A23-A0 veya A19-A0 ve izole edilmiş I/O için A15-A0 dekod ederiz. Bazen I/O birimleri sadece sabit I/O adresi kullanılırsa yalnız A7-A0 dekod edilir. Diğer fark ise IORC^ ve IOWC’ yi okuma veya yazma işlemi için I/O birimlerini aktif yapmak için kullanırız. Mikroişlemcinin daha düşük versiyonlarında I/O birimini aktif yapmak için IO/M^=1 ve RD^veya WR^ kullanılır.**

**5.6.1 8 bit I/O adreslerinin dekod edilmesi**

**Bahsedildiği gibi sabit I/O komutları 0000H-00FFH olarak A15-A0 üzerinde görünen 8 bit I/O port adresini kullanır. Eğer sistem 256’dan daha az I/O birimlerinden oluşuyorsa 8 bit I/O port adresi için sadece A7-A0 adres bağlantılarını dekod ederiz. Lütfen DX registerinde 00H-FFH I/O portlarını adresleyebildiğine dikkat edin. Ayrıca eğer adres 8 bit adres olarak dekod edilirse 16 bit I/O adresi kullanan I/O birimlerine ulaşamayız. Şekil 9-6 F0H-F7H’a ka darki 8 bit I/O portlarını dekod eden 74ALS138 dekoderi göstermektedir. (Burda sistemin bu dekoder için 00H-FFH I/O port kullanacağını varsayıyoruz. Şekil 9-7’de bu dekoderin PAL versiyonunu vermektedir. Bu dekoder bellek adres dekoderi ile aynıdır. (Deko der girişlerine sadce A7-A0 adres bitlerinin bağlanması hariç)**

**Bu dekoder çok daha iyidir. Çünkü entegre devre sayısı 1’e(PAL) indirilmiştir. PAL’in programı örnek 9-2’de gösterilmiştir. **

**5.6.2 16 bit I/O adreslerinin Dekod edilmesi **

**PC sistemlerde dahi 16 bit I/O adresi’de dekod edebiliriz. 8 bit I/O adresi ile 16 bit I/O adres arasındaki temel fark, eklenen adres hatlarının (A15-A8) dekod edilmesidir. Şekil 9-8 3F8H-3FHH I/O P ortlarını dekod etmekte kullanılan 2 tane PAL16L8 içeren bir devreyi göstermektedir. Bunlar seri iletişim portları için PC’lerde kullanılan temel I/O port bölgeleridir. İlk PAL16L8 ilk 8 bit I/O port adresini (A15-A8) dekod eder. Böylece 0300H-03FFH arası ndaki her I/O adresi için ikinci PAL16L8 (U2)etkin yapmakta kullanılan bir sinyal üretir. **

**5.6.3 8 ve 16 bit I/O portları **

**Şimdiye kadar bellek adresi dekod edilmesinden belki de daha kolay olan (çünkü bit sayısı farklı) I/O port adresinin dekod edilmesi anlatıldı. Şimdi de mikroişlemci ile 8 veya 16 bit I/O birimi aras ında dataların nasıl transfer edildiğini anlatacağız 8 bit I/O için datanın transfer edilmesi 8086/80286 veya 80386SX’in I/O bankalarından birinde olur. Bellekte olduğu gibi I/O sistemi de 2 tane 8 bit bellek bankası içerir. Bu 80286 ve 80386SX’teki gib i 16 bit bellek sistemi için ayrı I/O bankasını gösteren devre Şekil 9-9’da ifade edilmiştir. İki I/O bankı mevcut olduğu için her 8 bit I/O yazma işlemi fonksiyonlarını doğru şekilde yapmak için write strobuna ihtiyaç duyar. I/O okuma, ayrı oku strıbuna gerek duymaz. Çünkü bellekteki gibi mikroişlemci sadece bir byte okur. Bu byte diğer byte ile birleştirilmiş veya ayrı tutulmuştur. Okumanın problemlere neden olduğu tek zaman I/O biriminin okuma işlemini doğru bir şekilde yapmadığı zamandır. I/OP birim inin yalnış bankadan okuma yaptığı durumlarda ayrı okuma sinyallerine ihtiyaç duyarız. Şekil 9-10 40H ve 41H 8 bit I/O adresindeki iki farklı8 bit çıkış birimini içeren bir sistemi gösterm ektedir. Çünkü bunlar 8 bitlik birimlerdir. ve iki ayrı I/O yazma sinyali üretiriz. Çünkü farklı I/O banklarında görünürler. Şekil 9-9’da kullanılan PAL16L8 dekoder için program örnek 9-5’te gösterilmektedir.**

**16 bbit genişliğinde I/O birimi seçildiğinde A0 ve BHE^ pinlerinin hiçbir fonksiyonu olmaz Çünkü heriki I/O bbankları birlikte seçilir. 16 bit I/O devreleri nadir olsa da ADC ve DAC bazı video ve di sk bellek arabirimlerinde çok mevcuttur. Şekil 9-11 64H ve 65H 8 bit I/O adreslerine işlemek için bağlanılan 16 bit giriş birimini göstermektedir. PAL16L8’in A0 adres biti ve BHE^ ile bağlantısı yoktur. Çünkü bu sinyaller 16 bit genişliğinde I/O birimleri ne uygulanmamaktadır. PAL16L8’in programı Örnek 9-6’da enable sinyallerinin giriş birimindeki gibi kullanılan 3 durumlu bufferlar (74ALS244) için nasıl üretildiğini göstermektedir. **

***5.7 8255 (PPI)***

**İntel 8085 ve ailesi ve Z80 Mikroişlemcilerin I/O işlemleri için düzenlenmiş olan bir enteğredir. 8255 üzerinde 8 bitlik 3 giriş/çıkış portu bulunur. Bu portlar birbirlerinden bağımsız kullanılabi ldikleri gibi, çalışma moduna göre birbirleriyle bağımlı olarak da çalışabilirler.**

**8255'in çalışabilmesi için 4 adet özel port adresi gereklidir. İlk üç port A, B, C olarak isimlendirilen portlara erişmek için kullanılırken, 4. port enteğrenin çalışma modunu belirleyen kontrol r eğisterine ulaşmak için kullanılır.**

**8255 entegresinin kontrol sözcügü ile belirlenebilen 3 çalışma modu vardır.**

**1 - Mode 0, Temel giriş/çıkış modu,**

**2 - Mode 1, Strobe giriş/çıkış modu,**

**3 - Mode 2, Çift yönlü giriş/çıkış modu.**

**Entegrenin RESET girişine lojik 1 seviyede bir sinyal uygulandığı anda, bütün portlar Mode 0 durumunda, yüksek empedans gösterirler. RESET girişi yeniden lojik 0 seviyeye indikten sonra, bu por tlar normal *****giriş portu *****olarak çalışırlar. **

**8255'in kontrol reğisterinin içeriği aşağıda çıkartılmıştır.**

**Data Hatları Anlamları**

**D7 Mod Flagı**

**0 Pasif**

**1 Aktif**

**D6 D5 Mode Seçimi**

**00 Mode 0**

**01 Mode 1**

**1x Mode 2 **

**D4 A Portu**

**1 Giriş**

**0 Çıkış**

**D3 C Portu (Hıgh 4-7)**

**1 Giriş**

**0 Çıkış**

**D2 Mode Seçimi**

**0 Mode 0**

**1 Mode 1**

**D1 B Portu**

**1 Giriş**

**0 Çıkış**

**D0 C Portu (Low 0-3)**

**1 Giriş**

**0 Çıkış**

**8255 Çalışma modlarının özellikleri aşağıda çıkartılmıştır.**

**Mode 0 : Bu mod ile A, B ve C portları giriş/çıkış işlemleri için kullanılabilir. Çıkışlar Lach edilirler. Girişler lachli değildir. C portu 4 bitlik 2 parça halinde kullanılabilir.**

**Mode 0 çalışma konumunda kullanılabilecek kontrol sözcükleri aşağıda çıkartılmıştır.**

**Mode 1 (Strobe Giriş/Çıkış) : 8255, bu modda giriş/çıkış işlemlerini handshaking veya strobe hatları yardımı ile gerçekleştirir. Enteğre bu mod ile çalışırken 12 bitlik 2 port bulundurur. A portu ve C portunun low (0-3) kısmı bir port, B portu ve C portunun hıgh(4-7) kısmı bir port olarak işlev görür. Her iki portta da giriş/çıkış işlemleri lach'lidir.**

**Handshaking işlemi, her iki portta da C portunun üzerinden gerçekleştirilir. Giriş ve çıkış durumlarında C portunun bitleri farklı anlamlar taşırlar.**

***Mode 1 Giriş : *****8255 Mode 1'de giriş portu olarak çalışırken C portunun bit anlamları aşağıda çıkartılmıştır.**

**C Portu 3. Bit (A) : INTR (İnterrupt)**

**C Portu 4. Bit (A) : ****STB**** (Strobe)**

**C Portu 5. Bit (A) : IBF (Input Buffer Full)**

**C Portu 0. Bit (B) : INTR (İnterrupt)**

**C Portu 2. Bit (B) : ****STB**** (Strobe)**

**C Portu 1. Bit (B) : IBF (Input Buffer Full)**

**Entegreye bilgi gönderen çevre birim A veya B portuna bilgiyi yazdıktan sonra ****STB ****sinyali göndererek verinin hazır olduğun u 8255'e bildirir. PPI bu sinyali aldıktan sonra portun dolu olduğunu bildirme için IBF hattını lojik 1 seviyeye çıkarır. Porttan bilgi okunması durumunda IBF hattı otomatik olarak lojik 0 seviyeye indirilir. Strobe sinyalinin pozitif kenarı, INTR hattını n lojik 1 seviyeye çıkmasını sağlar. Porttan bilginin okunması IBF hattı gibi INTR hattının da lojik 0 seviyeye düşmesini sağlar. **

**C portunun 6 ve 7 numaralı bitleri kontrol biti olarak kullanılmadıklarından giriş/çıkış hattı olarak kullanılabilirler. Bu hatların durumu kontrol sözcügünün 3 nolu biti ile belirlenir.**

***Mode 1 Çıkış : *****8255 Mode 1'de çıkış portu olarak çalışırken C portunun bit anlamları aşağıda çıkartılmıştır.**

**C Portu 3. Bit (A) : INTR (İnterrupt)**

**C Portu 6. Bit (A) : ****ACK**** (Strobe)**

**C Portu 5. Bit (A) : ****OBF ****(Output Buffer Full)**

**C Portu 0. Bit (B) : INTR (İnterrupt)**

**C Portu 2. Bit (B) : ****ACK**** (Strobe)**

**C Portu 1. Bit (B) : ****OBF**** (Output Buffer Full)**

**Mikroişlemciden gelen bilgi porta yazıldıktan sonra, bilginin hazır olduğunu belirtmek için PPI, ****OBF**** hattını lojik 0 seviye ye getirir. Bu sinyal çevre birime verinin hazır olduğunu bildirir. İlgili devre veriyi okuduktan sonra ****ACK**** hattını lojik 0 seviyeye indirerek, PPI'ya bilgiyi okuduğunu bildirir. ****ACK**** hattının pozitif kenarı ****OBF**** hattını otomatik olarak lojik 1 seviyeye çıkartır. ****ACK**** hattının pozitif kenarı aynı zamanda INTR hattının lojik 1 seviyeye çıkmasını da sağlar. ****OBF**** hattının lojik 0 seviyeye düşmesi INTR ha ttının da 0'a düşmesini sağlar.**

**C portunun 4 ve 5 numaralı bitleri kontrol biti olarak kullanılmadıklarından giriş/çıkış hattı olarak kullanılabilirler. Bu hatların durumu kontrol sözcügünün 3 nolu biti ile belirlenir.**

**Mode 2 Çift Yönlü Giriş/Çıkış : Mode 2'de PPI A portunu çift yönlü bir port olarak kullanır. C portu ise A portunun kontrol sözcügü gibi işlem görür. B portu ise tek başına giriş/çıkış olarak kull anılabilir. A portu giriş ve çıkış konumlarında lach'lidir.**

**PPI, Mode 2'de çalışırken C portunun bit anlamları aşağıda çıkartılmıştır.**

**C Portu 7. Bit : ****OBF**** (Output Buffer Full)**

**C Portu 6. Bit : ****ACK**** (Strobe)**

**C Portu 5. Bit : IBF (Input Buffer Full)**

**C Portu 4. Bit :**** STB ****(Strobe)**

**C Portu 3. Bit : INTR (Interrupt)**

**Bitlerin anlamları ve çalışma şekilleri mode 1'de olduğu gibidir. A portu giriş konumunda iken IBF ****STB**** ve INTR hatları kont rol işlevini yaparken çıkış konumunda ****OBF, ACK**** ve INTR hatları kontrol görevini üstlenir.**

**8255 Mode 1 veya Mode 2 konumunda çalışırken C portunun bitlerinin set veya reset edilmesi kontrol reğisterine yazılacak kontrol sözcügü ile gerçekleştirilir. Bit set/reset için kontrol sözcügünün yapısı aşağıda çıkartılmıştır.**

**D7 Bit Set/Reset Flagı**

**0 Aktif**

**D6**

**D5**

**D4 Önemsiz**

**D3**

**D2**

**D1 Hangi bitin set/reset edileceğini gösterir.**

**D1 D2 D3 Seçilen Bit**

**0 0 0 0**

**1 0 0 1**

**0 1 0 2**

**1 1 0 3**

**0 0 1 4**

**1 0 1 5**

**0 1 1 6**

**1 1 1 7**

**D0 Seçilen bitin set veya reset olacağını gösterir.**

**1 Bit Set**

**0 Bit Reset**

***5.8 8279 Proğramlanabilen klavya ve display sürücü***

**8279 proğramlanabilen bir keyboard ve display sürücüsüdür. Entegre 64 tuşlu bir keyboard’u ve 16 adet display’i kontrol edebilir. Kendi iç zamanlama mantığının ve display, keyboard için ram ünite sinin bulunması nedeniyle CPU’yu meşgul etmeden çalışabilir. PC bus üzerine bağlandığında kontrol ve data olmak üzere I/O haritasında 2 adet adres kullanır. **

**5.8 1 DISPLAY**

**Display, entegrenin tarama hatları olan SL 0,1,2,3 ve data hatları olan A0-A3, B0-B3 hatlara tarafından sürülür.**

**SL tarama hatları ortak anot veya ortak katotların sürülmesini sağlar. Bu hatların yapısı proğramlama sırasında kodlanmış ve kodlanmamış olarak belirlenebilir. Eğer hatlar kodlanmış olarak proğramlan mış ise bibr kod çözücü ile kullanılmalıdır. Bu durumda enteğre 16 adet display’i sürebilir. Eğer proğramlama, küdlanmamış modda gerçekleştirilmiş ise bu durumda en çok 4 adet display sürülebilir.**

**5.8. 2 KEYBOARD**

**Keyboard, tarama hatları SL 0,1,2,3 ve RL 0-7 hatları ile CNTRL ve SHIFT hatları tarafından sürülür.**

**SL hatları display’de olduğu gibi 3-8 kod çözücü ile deşifre edilerek kullanılır. Eğer SL hatları kodlanmamış modda proğramlanmış ise SL hatları kod çözücü olmadan kullanılır. Bu durumda keyboard max imum 32 tuştan oluşur.**

**Enteğre içinde display için 16\*8 bitlik bir ram ve keyboard için 64 bitlik bir RAM bulunur. Ayrıca keyboard ve display idaresi için 2 adet register’i bulunur. Bu registerler**

**1 - Komut registeri**

**2 - Fifo statü registeri**

**1 - Komut Reğisteri**

**Genel olarak entegrenin işleyişini belirleyen register’dir. Bu register ile tuş takımının çalışması, tarama frekansının belirlenmesi, keyboard ve display’in okunması, display’in yazılması, gister genin silinmesi ve interrupt kontrolü yapılır. Registerin komutları aşağıdaki gibidir.**

**1- Keyboard ve display durumlarının belirlenmesi.**

**7****6****5****4****3****2****1****0**000DDKKK** **

**Kontrol cümlesindeki DD, display modunu, KKK ise keyboard modunu proğramlar. DD’nin alabileceği değerler:**

| **D****** | **D****** | **ANLAMI****** |
| --- | --- | --- |
| 0 | 0 | 8 Adet 8 Bitlik Soldan Girişli Display |
| 0 | 1 | 16 Adet 8 Bitlik Soldan Girişli Display |
| 1 | 0 | 8 Adet 8 Bitlik Sağdan Girişli Display |
| 1 | 1 | 16 Adet 8 Bitlik Sağdan Girişli Display |

**Sağdan ve soldan girişli display entegrenin ram yapısı ile ilgilidir. **

**Display’e gönderilen bilgiler display ram’ından alınarak displaye yazılır. Display ram’ı 16 adet 8 bitlik bölümlerden oluşur. Eğer display 8 adet olarak seçilmiş ise ram’ın ilk 8 bytı, 16 adet seçilm iş ise tamamı kullanılır.**

**Display 4 bitlik 2 bölüm halinde düzenlenebilir. Bu durumda ram, A ve B data hatları için 4’er bitlik bölümler şeklinde düzenlenir. Display driver ile ilgili örnekler ekte verilmiştir.**

**1.1 Soldan Girişli Display Modu**

**Bu modda displayde yazılacak bilgiler ram’da soldan başlayarak yerleştirilir.(Auto Increment mode için) Eğer ram’da taşma oluşursa yeni gelen bilgiler yine soldan başlayarak yerleştirilirler.**

**OPERASYON****0****1****2****13****14****15**5 Yazıldı**5** 9 Yazıldı**5****9** .**.****.****.****.****.****.**.**.****.****.****.****.****.**4 Yazıldı**5****9****?****?****?****4**3 Yazıldı**3****9****?****?****?****4**12 Yazıldı**3****12****?****?****?****4**** **

**1.2 Sağdan Girişli Display Modu**

**Bu modda kullanılan medod elektronik hesap makinalarında da kullanılır. Ran’a yazılan ilk veri 0. display adresine sağdan girişli olarak yazılır. Bundan sonraki girişler sıra ile fakat ram sola k aydırılarak gerçekleştirilir.(Auto Increment Modda) Ram’da taşma olduğunda en soldaki byte silinir.**

**OPERASYON****1****2****3****14****15****0**5 Yazıldı **5**** **

**OPERASYON****2****3****4****15****0****1**9 Yazıldı **5****9****.**

**.**

**OPERASYON****0****1****3****13****14****15**14 Yazıldı**5****9****?****?****?****14**** **

**OPERASYON****1****2****3****14****15****0**3 Yazıldı**9****?****?****?****14****3**** **

**OPERASYON****2****3****4****15****0****1**121Yazıldı**?****?****?****14****3****121**** **

**1.3 AutoIncrement**

**Gerek display, gerekse FIFO ram’ı okunur veya yazılırken AutoIncrement modu 1 olarak seçilirse her operasyondan sonra ram pointer’i 1 artırılır. Bu mod ile display adres tarifi yapılmaksızın sayı lar soldan veya sağdan girişli olarak yazdırılabilir. Eğer bu mod 0 olarak seçilirse bilgi yazılacak display’in adresinin verilmesi gerekir.**

**AutoIncrement aktif konumda iken ram ile ilgili pointer istenen herhangi bir display’e kaydırılabilir. Soldan girişli display modunda bu durumun etkisi aşağıdaki gibi olur.**

**OPERASYON****0****1****2****3****4****5****6****7**5 Yazıldı**5** 9 Yazıldı**5****9** 10010101 komutu**5****9** 7 Yazıldı**5****9** **7** 12 Yazıldı**5****9****7****12****Sağdan girişli display modunda etki aşağıdaki gibi olur.**

**OPERASYON****1****2****3****4****5****6****7****0**5 Yazıldı **5**** **

**OPERASYON****2****3****4****5****6****7****0****1**9 Yazıldı **5****9**** **

**OPERASYON****2****3****4****5****6****7****0****1**10010101 Komutu **5****9**** **

**OPERASYON****3****4****5****6****7****0****1****2**7 Yazıldı **7** **5****9** ** **

**OPERASYON****4****5****6****7****0****1****2****3**16 Yazıldı **7****16** **5 ****9** ** **

**AutoIncrement biti ile sağdan girişli display modunda başlangıç displayi secilebilir.**

**OPERASYON****0****1****2****3****4****5****6****7**10010101 Komutu ** **

**OPERASYON****1****2****3****4****5****6****7****0**1 Yazıldı **1** ** **

**OPERASYON****2****3****4****5****6****7****0****1**2 Yazıldı **1****2** ** **

**OPERASYON** 8 Yazıldı**4****5****6****7****8****1****2****3**** **

**OPERASYON** 9 Yazıldı**5****6****7****8****9****2****3****4**** **

**8279 keyboard ve display set proğram cümlesinde yer alan KKK değerleri aşağıdaki gibidir.**

| **K****** | **K****** | **K****** | **FONKSİYON****** |
| --- | --- | --- | --- |
| 0 | 0 | 0 | Kodlu taramalı keyboard 2 key lockout mod |
| 0 | 0 | 1 | Kodsuz taramalı keyboard 2 key lockout mod |
| 0 | 1 | 0 | Kodlu taramalı N key rollever mod |
| 0 | 1 | 1 | Kodsuz taramalı N key rollever mod |
| 1 | 0 | 0 | Kodlu taramalı sensör matrix modu |
| 1 | 0 | 1 | Kodsuz taramalı sensör matrix modu |
| 1 | 1 | 0 | Strobe Input, kodlanmamış taramalı display modu |
| 1 | 1 | 1 | Strobe Input, kodlanmış taramalı display modu |

**1.4 2 Key Lockout Çalışma Modu**

**8279, bir tuşa basılmasını yakalayacak şekilde tuş takımı satırlarını tarar. Tuşa basılmasını yakaladıktan sonra gürültü etkisinin geçmesini yaklaşık 5-10ms bekler. Eğer tuş hala basılı görülüyo r ise tuşun adresi Shift ve Cntrl tuşlarının durumu FİFO ram’ına aktarılır. Eğer aynı anda iki tuşa basılmış ise bu çalışma modunda ilk basılan tuş FİFO ram’ına alınır. Diger tuş/tuşlar gözardı edilir.**

**1.5 N Key Rollever Çalışma Modu**

**Bu modda aynı anda veya peşpeşe basılan tuşlar basılma sırasına göre FIFO ram’ına alınır. FIFO ramına alınan karekter sayısı veya fifo’daki karekter sayısı FIFO statü registerine yazılır.**

**1.6 Sensör Matrix Çalışma Modu**

**Bu metod ile çalışma seçildiğinde, 8279’a klavye yerine On veya Off konumlarını alabilen sensörler bağlanır. Enteğre her tarama sonunda sensörlerin durumu FIFO ram’ına aktarılır. FIFO ram’ındaki herhangi bir değişiklik IRQ sinyalinin oluşmasını sağlar.**

**1.7 Strobe Giriş Çalışma Modu**

**8279, bu modda return hatlarının içeriğini, CNTRL/STRB sinyalinin pozitife giden kenarında okur ve FIFO ramına aktarır. FIFO ram’ı boş olmadığı durumda IRQ sinyali üretilir.**

**FIFO ram’ı 8\*8 kapasiteye sahiptir. 2 Key Lockout, N Rollever veya strobe giriş modunda bu ram FIFO metoduna göre çalışır. Her gelen karekter ardışıl adreslere aktarılır. Ran’dan okuma işleminde ise, karekterler bu sıraya göre daha hatlarına yazılır. Bu modlarda FIFO statü registerinde FIFO’daki karekter sayısı ve taşıma ile ilgili hatalar bulunur.**

**2. Tarama Hattı Proğram Cümlesi**

**8279 Display ve keyboard’ın taranması için bir dış osilatöre ihtiyaç duyar. Bu osilatör 2Mhz’lik bir sinyal olmalıdır. Entegre, dış osilatöre bağlı 2 adet iç bölücüye sahiptir. İç bölücülerden bi r tanesi iç çalışma frekansını belirlerken bir tanesi tarama hatlarının frekansını belirler. İkinci bölücü proğramlanabilir niteliğe sahiptir. Bu bölücünün proğramlanması aşağıdaki kontrol cümlesi ile olur.**

**7****6****5****4****3****2****1****0**001PPPPP** **

**Cümledeki PPPPP, bölücünün, bölme sayısını belirler. Bölme dış frekansa göre yapılır. Örneğin:**

**External frekans 2 Mhz ise, bu frekans 20’ye bölünerek 100Hz’lik display/keyboard tarama frekansı elde edilir.**

**Bölme işlemi 2 ile 31 arasında istenen herhangi bir degere ayarlanabilir.**

**3. FIFO Ram’ını Oku**

**FIFO ram’ında kayıtlı bilgileri okuyabilmek için kontrol cümlesi olarak aşağıdaki cümle verilmelidir.**

**7****6****5****4****3****2****1****0**010IXAAA** **

**Cümledeki (I) AutoIncrement okuma işleminden sonra RAM pointerinin artırılıp artırılmayacağını gösterir. Eğer I=0 konumunda ise belirlenen adresteki data okunur.**

**Cümledeki AAA, okunacak ram’ın adresini belirler. Eğer I=1 konumunda ise data bus’a konulacak değer FIFO’ya konan ilk değer olacaktır. **

**Kontrol reğisterine OKU emri yazıldıktan sonra data portundan (A0=0) değer okunabilir.**

**4. Display Ram’ını Oku **

**Display ram’ını okuyabilmek için kontrol cümlesi olarak aşağıdaki cümle verilmelidir.**

**7****6****5****4****3****2****1****0**011IAAAA** **

**Cümledeki AAAA ile okunacak display’in adresi belirlenir. Eğer I (AutoIncrement) flağı 1 konumunda ise ram pointer’i okuma işleminden sonra 1 artırılır.**

**Cümle kontrol portuna yazıldıktan sonra data portundan değer okunabilir.**

**5. Display Ram’ına Yaz**

**CPU, display ram’ına bilgi yazabilmek için 8279 enteğresinin kontrol reğisterine aşağıdaki yapıda bir kontrol cümlesi göndermelidir.**

**7****6****5****4****3****2****1****0**100IAAAA** **

**I flağı 1 ise yazma işleminden sonra display ram pointeri 1 artırılır. Cümledeki AAAA yazılacak display’in adresini gösterir. Kontrol reğisterine yaz cümlesi konduktan sonra data portuna yazılan deger display ram’ına gönderilecektir.**

**6. Display’e Yazmayı Engelleme ve Display Karartma**

**Eğer display 4 bitlik bölümler halinde düzenlenmiş ise A veya B bölümü ile işlem yaparken diğer bölümün operasyonlardan etkilenmemesi için istenilen bölüm yazma ve silme operasyonlarına kapatılab ilir. Komutun yapısı aşağıdaki gibidir.**

**7****6****5****4****3****2****1****0**101XWWBB** **

**Cümledeki WW operasyonlarda kapatılacak bölümün hangisi olduğunu gösterir. Yapısı:**

| **W****** | **W****** | **OPERASYON****** |
| --- | --- | --- |
| 0 | 0 | Kapatma Yok |
| 0 | 1 | A Portu Kapatıldı |
| 1 | 0 | B Portu Kapatıldı |
| 1 | 1 | A ve B Portları Kapatıldı |

**BB bit kombinasyonu A veya B portlarına bağlı display’lerin karartılmasını (boş bırakılmasını) sağlar. Bu komut ile entegrenin BD bacağı aktif duruma gelir.**

| **B****** | **B****** | **OPERASYON****** |
| --- | --- | --- |
| 0 | 0 | Karartma Yok |
| 0 | 1 | A Portu Karartıldı |
| 1 | 0 | B Portu Karartıldı |
| 1 | 1 | A ve B Portları Karartıldı |

**7. Silme (Clear)**

**Komut gösterge ram’ının ve FIFO ram’ın silinmesini sağlar. Komut yapısı**

**7****6****5****4****3****2****1****0**110DDDFA** **

**Kontrol cümlesindeki DDD, display’in silinme şeklini ve silme işlemini kontrol eder. DDD’nin alabileceği değerler.**

| **D****** | **D****** | **D****** | **OPERASYON****** |
| --- | --- | --- | --- |
|  | 0 | x | Bitler 0 yapılarak silinir |
|  | 1 | 0 | Bitler 20h yapılarak silinir |
|  | 1 | 1 | Bitler 1 yapılarak silinir. |
| 1 | x | x | Bit 1 ise silme işlemi yapı-lır. (veya F=1 ise) |

**F (Clear FIFO) fifo ram’ın silinmesini sağlar. F=1 ise interrupt hattı reset olur ve matrix sensör modunda 0 numaralı satır secilir.**

**A (Clear All) Fifo ve gösterge ram’larının silinmesini gerçekleştirir. **

**Clear komutu ile sadece gisterge ram’ı, sadece fifo ram veya her iki ram da belirlenen metoda göre silinebilir. Örneğin:**

**11001110 Sadece fifo’yu siler**

**11011100 Sadece gösterge ram’ını siler**

**11001111 Tüm ram’ları siler.**

**8. End Interrupt/Error Mode Set**

**Sensör matrix modunda, N rollever key veya 2 key lockout modunda çalışırken fifo’da olan bir değişiklik IRQ hattının durum degiştirmesine neden olur. Bu durumda ram’a yazma işlemleri iptal edili r. End Intterrupt komutu ile IRQ hattının ilk şekline gelmesi ve ram yazma işlemlerinin açılması sağlanır. Eğer E biti 1 olarak belirlenirse 8279 error modunda çalışmaya başlar. Komutun yap ısı:**

**7****6****5****4****3****2****1****0**111Exxxx** **

**Fifo sensör ram’ı okunduğunda, 8279 keyboard’dan hangi tuşa basıldığı, aşağıdaki bit yapısı ile belirlenir.**

**7****6****5****4****3****2****1****0**NSLLLCCC** **

**CCC Kolonları**

**LLL Satırları**

**N CNTRL Tuşunu**

**S Shift Tuşunu gösterir.**

**8279’un kontrol cümlesi komutlarının yazılması için düzenlenmiştir. Bu cümle eğer okunur ise gelen bilgi fifo statü sözcüğü olur. Fifo statü sözcügünün yapısı aşağıda çıkartılmıştır.**

**7****6****5****4****3****2****1****0**DEOUFNNN** **

**NNN Fifo’daki karekter sayısını**

**F Fifo dolu**

**U Error Underrun**

**O Error Overrun**

**E Birden fazla tuşa basıldı ise(2 Key Lockout)/ Sensör durumu değişti (Sensör **

**matrix modda)**

**D Display kullanılmıyor.(Boş)**

**Error Overrun : Eğer fifo dolu ise, bir tuşa basıldığında overrun flagı 1 olur. Bu durumda karekterler fifo’da üst üste yazılmaya başlanır.**

**Error Underrun : Fifo boş olduğu durumda, fifo okunmaya çalışılırsa underrun flagı 1 yapılır.**

***5.9 8253/8254 COUNTER***

**İntel 80xxx ailesi ve Z80 Mikroişlemcilerle uyumlu olarak çalışabilen bir sayıcı/bölücü enteğresidir. 8253 üzerinde 16 bitlik 3 adet sayıcı/bölücü bulunur. Bu sayıcı/bölücüler birbirlerinden bağı msız olarak proğramlanabilirler.**

**8253'ün çalışabilmesi için 4 adet port adresi gereklidir. İlk üç port Cnt1, Cnt2, Cnt3 için, dördüncü port(Kontrol Portu) ise, herhangi bir Counterın çalışma modunu proğramlamak için kullanılır. **

**Enteğrenin, Kontrol portuna yazılan kontrol sözcüğü ile belirlenen 6 çalışma modu vardır.**

**1- Mode 0 Yazılımla kesilebilen sayıcı**

**2- Mode 1 Hardware ile tetiklenebilen tek atımlı flip flop**

**3- Mode 2 Oranlı sinyal üretici**

**4- Mode 3 Kare dalga modu**

**5- Mode 4 Yazılım tetiklemeli pals üretici**

**6- Mode 5 Donanım tetiklemeli pals üretici**

**8253'ün kontrol reğisterinin içeriği aşağıda çıkartılmıştır.**

**Data Hatları Anlamları**

**D7 - D6 Counter seçimi**

**00 Counter 0**

**01 Counter 1**

**10 Counter 2**

**11 Okuma komutu**

**D5 - D4 Okuma/Yazma**

**00 Counter Lach komutu**

**01 Okuma ve yazma alt bayttan yapılacak**

**10 Okuma ve yazma üst bayttan yapılacak**

**11 Okuma/yazma önce alt, sonra üst bayttan **

**yapılacak**

**D3 - D2 - D1 Mode seçimi**

**000 Mode 0**

**001 Mode 1**

**x10 Mode 2**

**x11 Mode 3**

**100 Mode 4**

**101 Mode 5**

**D0 Counter tip seçimi**

**0 16 bit binary counter**

**1 BCD counter**

**8253 Proğramlanırken, kontrol cümlesi, kontrol portuna, bölme oranları ve counter start ile ilgili bilgiler counter portuna yazılırlar. Proğramlamada, kontrol cümlesine göre çeşitli yöntemler kull anılabilir. **

**Eğer counter 16 bit olarak proğramlanıyorsa, MSB cümlesi, 8 bit olarak proğramlanıyorsa MSB cümlesi counter'ı start eder. **

**Örnek proğramlama teknikleri:**

**1- **

**Kontrol cümlesi (Counter 0)**

**LSB**

**MSB **

**Kontrol cümlesi (Counter 1)**

**LSB**

**MSB**

**Kontrol cümlesi (Counter 2)**

**LSB**

**MSB**

**2-**

**Kontrol cümlesi (Counter 0)**

**Kontrol cümlesi (Counter 1)**

**Kontrol cümlesi (Counter 2)**

**LSB**

**MSB (Counter 0)**

**LSB**

**MSB (Counter 1)**

**LSB**

**MSB (Counter 2)**

**3 -**

**Kontrol cümlesi (Counter 0)**

**LSB (Counter 0)**

**LSB (Counter 1)**

**LSB (Counter 2) **

**Kontrol cümlesi (Counter 1)**

**Kontrol cümlesi (Counter 2)**

**MSB (Counter 1)**

**MSB (Counter 0)**

**MSB (Counter 2)**

**8253 Çalışma modlarının özellikleri aşağıda çıkartılmıştır.**

**Mode 0 : Bu modda counter, frekans bölücü ve sayıcı gibi çalışır. Counter'ın GATE ayagı sayma işlemi için pozitifte olmalıdır. GATE ayağına gelecek herhangi bir şase palsı sayma işleminin durmasına neden olur. GATE ayağına gelen pozitif pals counter'ın resetlenmesine ve sayma işleminin başlamasına neden olur.**

**Sayma işleminin başlaması ile OUT ayağı şase seviyesine düşer. Counter programlanan sayıya ulaşıncaya kadar şase seviyesinde kalır. Sayma işlemi bittiğinde 1 seviyesine tekrar çıkar. Mode 0'ın çal ışmasıyla ilgili timing diyagramı ekte çıkartılmıştır.**

**Mode 1 : Bu modda counter yeniden tetiklenebilen monostable multivibratör (tek atımlı flip flop) gibi çalışır. Tetikleme işlemi GATE ayağı ile yapılır. GATE normalde 0 seviyesindedir. sayma işlemi nin yapılabilmesi için bu ayağı 1 seviyesinde bir sinyal gelmesi gerekir. Bu sinyali alan counter sayma işlemine başlar. Sayma işleminden önce 1 seviyesinde olan OUT ayağı sayma işlemi ile birlikte 0 seviyesine düşer. Sayma işlemi bittikten sonra tekrar 1 seviyesine yükselir. Mode sayma işlemi için GATE tetiklemesi bekler. Sayma işleminin bittiği clock palsı içinde bir GATE tetiklemesi olursa OUT 1 seviyesine çıkmaksızın yeni sayma işlemi boyunca da 0 seviyesinde kalır.**

**Mode 1'in çalışmasıyla ilgili timing diyagramı ekte çıkartılmıştır.**

**Mode 2 : Mode 2 de counter, belirlenen sayma işlemini yapar. Sayma işleminin sonunda OUT ayağından 0 seviyesinde bir pulslık sinyal üretir. **

**Sayma işlemi için GATE ayagının lojik 1 seviyesinde olması gerekir. Sayma işlemi sırasında bu ayagın 0 seviyesine gitmesi sayma işleminin kilitlenmesine, yeniden 1 seviyesine çıkması, sayıcının re setlenmesine neden olur. Bu mode ile ilgili timing diyagramı ekte çıkartılmıştır. **

**Mode 3 : Mode 3'de counter kare dalga üreteci gibi çalışır. Counter, OUT ayağını programla belirlenen sayma süresinin yarısı kadar bir süre 1 seviyesinde, diğer bölümü için 0 seviyesinde tutar. Bu işlem devamlılık arzeder.**

**Sayıcının çalışabilmesi için GATE ayağının 1 seviyesinde olması gerekir. 0 seviyesi sayıcının resetlenmesine neden olur. Mode ile ilgili timing diyağramı ekte çıkartılmıştır.**

**Mode 4 : Counter bu modda yazılım tetiklemeli pals üreteci olarak çalışır. Program ile belirlenen pals adedi sonunda OUT ayagı 0 seviyesinde bir pals üretir. Out ayağındaki 0 sinyalinin üretilmes i her proğramlamadan sonra 1 kez gerçekleştirilir. Sayıcının GATE ayağı sayma işlemi için 1 konumunda olmalıdır. Mode ile ilgili timing diyagramı ekte çıkartılmıştır.**

**Mode 5 : Counter bu modda donanım tetiklemeli pals üreteci olarak çalışır. Sayıcının GATE ayağı sayma işleminin tetiklenmesi için kullanılır. Tetikleme işlemi 0'a giden bir pals ile yapılır. GAT E ayağından, 0'a giden tetikleme palsını alan sayıcı, programın belirlediği sayma işlemini gerçekleştirir. Sayma işleminin sonunda OUT ayağından 0'a giden bir pals üretir. Yeni pals üretme işleminin yapılabilmesi için GATE ayağından yeni bir tetikleme pa lsının verilmesi gerekir. **

**Entegre programlama işleminden sonra, çalışma moduna göre, yazılım veya donanım ile tetiklendikten sonra sayma işlemini gerçekleştirir. Sayma işlemi sırasında counter ile ilgili portlardan sayma i şleminin durumu izlenebilir. **

**8253 Sayıcı Okuma İşlemi : Entegre içindeki sayıcıların okunabilmesi için 3 metod vardır.**

**1- Direkt sayıcı portundan okuma**

**2- Latch (Latch word) kontrol cümlesi ile dondurarak okuma**

**3- Geri okuma(read-back word) kontrol cümlesi ile dondurarak okuma**

**1- Sayıcıya ait port direkt olarak okunabilir. Sayıcının tam degerinin okunması işlemi, sayıcının 16 bitlik olması nedeniyle, aynı porttan iki ayrı okuma yapılarak gerçekleştirilir. **

**XOR AX,AX ; AX sıfırlandı**

**MOV DX, Base **

**IN AL,DX ; MSB Okundu**

**XCHG AH,AL**

**IN AL,DX ; LSB Okundu**

**XCHG AL,AH ; AX registerinin içeriği Counter 0'ın değeridir**

**2- Sayıcı, kontrol portuna yazılan lacth cümlesi ile dondurulduktan sonra okunabilir. Latch kontrol cümlesinin yapısı aşağıda çıkartılmıştır.**

**D0-D1-D2-D3 : Önemsiz**

**D4-D5 : Daima 0 olmalı**

**D5-D6 : Counter seçimi**

**00 Counter 0**

**01 Counter 1**

**10 Counter 2**

**11 Read-Back command**

**Kontrol portuna yazılan Latch cümlesi belirlenen sayıcının durdurulmasını sağlar. Bu durdurma işlemi, sayıcı portundan yapılacak ilk okuma komutuna kadar geçerlidir. İlk okuma komutundan sonra lat ch cümlesi geçersiz kalır. Kontrol portuna peşpeşe gönderilen Latch cümleleri, arada okuma işlemi olmaksızın geçersizdir. Eğer port 16 bit olarak programlanmış ise Lacth cümlesinden sonra, ilgili porttan iki okuma yapmak gerekir. Aksi halde latch cümlesi geçerli kalır.**

**3- Sayıcının okunmasında kullanılabilecek 3. metod kontrol portuna yazılacak read back cümlesi ile olur. Bu cümle ile sayıcının değeri, OUT ayağının durumu, proğramlama modu ve sayma işleminin yap ılıp yapılmadığı öğrenilebilir. Read-back kontrol cümlesinin yapısı aşağıda çıkartılmıştır. **

**D0 : Sayıcının Tipi**

**0 binary counter**

**1 BCD counter**

**D1-D2-D3 : Sayıcının çalışma modu**

**000 Mode 0**

**001 Mode 1**

**010 Mode 2**

**011 Mode 3**

**100 Mode 4**

**101 Mode 5**

**D4-D5 : Okuma/Yazma**

**00 Counter Lach komutu**

**01 Okuma ve yazma alt bayttan yapılacak**

**10 Okuma ve yazma üst bayttan yapılacak**

**11 Okuma/yazma önce alt, sonra üst bayttan **

**yapılacak**

**D6 : Sayma işleminin yapılıp yapılmadığı**

**1 Sayma işlemi yok**

**0 Sayma işlemi var**

**D7 : OUT ayağının durumu**

**1 Out ayağı 1 durumunda**

**0 Out ayağı 0 durumunda**

---
*Kaynak: `ÇEVRE BİRİMLERİ/ÇEVRE BİRİMLERİ.doc` — Teknik Servis — 2004*
