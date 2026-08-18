# Append - Arama Yolu Ayarlama

**APPEND**

**Arama Yolu Ayarlarma**

AMAÇ : okumak ya da yazmak için bir veri dosyası arandığında , dosyayı sadece çalışan

sürücü ve dizin de arar. Bu araştırma alanını genişletmek için APPEND komutu

kullanılır.

Dizilim : append \[sürücü:\]\\diziadı\[;\[sürücü:\]\[\\dizinadı\]...\]\[/x\[:on::off\]\]\[/path:on:/path:off\] \[/e\]

Bu dizilim veri dosyalarının aranacağı dizinlerin belirlemek için kullanılır.Araştırma birden çok dizinde yapılacaksa ,dizin isimleri”;” işaretiyle birbirinden ayrılır.

append;

Daha önceden ayarlanmış araştırma yollarının tümünü iptal eder

append

Append komutu kullanılarak ayarlanmış araştırma yollarının isimlerini görüntüler.

append komutunun anahtarları:

/x\[:on::off\] Veri dosyalsrını araştırmak için APPEND ,program dosyalarını araştırmak için de path

komutu kullanılır . Eğer veri dosyalarının araştırılacağı dizinde program dosyaları da

varsa , her iki komutuda kullanmak yerine APPEND komutuna “/x”veya “/x:on”

anahtarını eklemek yeterlidir.”/x:off” anahtarı da veri dosyalarının araştırılacağı dizinde

program dosyalarının araştırılmamasını sağlar.

/path:on:/path:off Bir dosyayı diskette aramak için dosyanın aranacağı dizin belirtilmişse

(BOLD.FON yerine C:WİNDOWS\\BOLD.FON şeklinde )araştırmanın sadece bu d

dizinde (örneğimizde windows dizini) sınırlı kalması için “/path : off” anahtarı kullanırız.

“/Path:on anahtarı ya da bu anahtarları hiç kullanmamak araştırmanın tüm belirtilen

dizinlerde yapılmasına neden olur

/e İlave edilen dizinlerin MS\_DOS etrafında depolanmasına neden olur. Bu dizinler SET

komutu ile görüle bilir

Eğer assing komutunu kullanıyorsanız, append komutunu assing komutundan önce kullanmalısınız.

Örnekler:

append c:\\msdos;\\lib ↵

Veya

append c:\\msdos;d:\\lib /x:on ↵

C:disketindeki MSDOS isimli dizinde ve D: disketindeki LIB isimli dizinde var olan veri dosyalarına ve program dosyalarına erişmek için araştırma yolu ayarlanır.daha önceden ayarlanmış araştırma yolu varsa , eskileri iptal edilir ve bu dizinlere araştırma yolu ayarlanır.

append c:\\msdos ;d:\\lib/x:off ↵

Belirtilen dizinlerde sadece veri dosyaları araştırılır

append ↵

Veri dosyalarının araştırılacağı yollar ekranda görüntülenir. Aşağıdaki görüntü karşınıza gelir

APPEND=C:\\MSDOS;:LIB

append; ↵

Öneceden ayarlanmış araştırma yollarının tümü iptal edilir.

**ASSIGN**

**Sürücü Atama**

AMAÇ : Bir sürücüyü tanımlayan harfi başka bir sürücüye atar.

Dizilim : assign \[x\[=\]y\[...\]\]

x şu andaki sürücü adı

y sürücüye verilmek istenilen yeni ad.

Assign komutu bir program tarafından ihtiyaç duyulması haricinde ve özellikle backup, restore, label, join, subst, print, komutlarından birinin kullanılması gerektiği hallerde kullanılmamalıdır. Format ve Diskcopy komutları assign komutunun yaptığı değişiklikleri yok sayar.

Örnekler :

assign a=b ↵

Komutun uygulanmasından sonra A: komutu verildiğinde MS-DOS B sürücüsüne geçer.

assign a=b b=a ↵

Komutunun uygulanmasından sonra A: komutu verildiğinde MS-DOS B sürücüsüne, B: komutu verildiğinde A sürücüsüne geçer. Sürücü işlemlerinin yerleri değişmiştir.

assign ↵

Daha önce yapılmış atamaların tümünü iptal eder.

**ATTRIB**

**Nitelik Verme**

Amaç : Dosya niteliklerini görüntüler veya değiştirir.

Dizilim : attrib \[+r: -r\] \[+a: -a\] \[+s : -s\] \[+h : -h\] \[sürücü\] \\ dizinadı \\ dosya adı \[/s\]

+r sadece okur dosya yapmak için,

-r okunur / yazılır dosya yapmak için,

+a arşiv dosyası yapmak için,

-a dosyanın arşiv niteliğini iptal için,

+s sistem dosyası yapmak için,

-s sistem dosyanın niteliğini iptal için,

+h ismi ekranda görünmeyen dosya yapmak için,

-h görünmeyen dosyayı normal hale getirmek için kullanılır.

/s anahtarı altdizindeki dosyaları da işleme koyar.

Backup, restore, xcopy komutları uygun anahtarlar kullanıldığında sadece arşiv niteliği

olan dosyaları kopyalar.

Örnekler :

attrib \*.\* /s ↵

Bütün dosyaların (altdizindekiler dahil) nitelikleri görüntülenir.

attrib +r \*.com

Uzantısı.com olan dosyalar sadece okunur (silinmez) nitelik kazanır.

attrib –r fiat.txt ↵

Fiat.txt dosyası okunur / yazılır (silinebilir) nitelik kazanır.

attrib +h ozel.not ↵

Ozel.not dosyasının ismi dosya listesinde görülmez.

attrib +a \*.\* ↵

Bütün dosyalar arşiv özelliği kazanır. Yedekleme esnasında bütün dosyalar yedeklenecektir.

**BACKUP**

**Yedekleme**

Amaç : Bir ya da daha fazla dosyayı bir disketten diğerine yedekler.

Dizlim : backup sürücü1:\[\\dizinaltı\]\[dosyaadı\] \[sürücü2:\] \[/s\] \[/m\] \[/f:disketkapasitesi\] \[/d:tarih\]

\[/t:zaman\] \[L:\[\[sürücü:\]\[\\dizinadı\]dosyaadı\]\]

sürücü1 yedeklemek istediğiniz disk sürücüsü

sürücü2 dosyaların yedekleneceği hedef sürücü

Backup komutun anahtarları:

/s Altdizinleri de yedekler

/m Yalnızca en son yedeklemeden sonra sonra değiştirilen dosyaları yedekler

/a Yedeklenecek dosyaları yedekleme diskinde daha önce var olanlara ilave eder.

MS-DOS un 3.2 ya da daha önceki uyarlamasından backup kullanılarak yedekleme

yapılmış dosyalar varsa bu anahtar kabul edilmeyecektir.

/f:disketkapasitesi Hedef disk daha önceden formatlanmadıysa formatlanmasını sağlar.

Disketkapasitesi Olası değerler

160K tek yüzlü, 5.25 inç disk 160, 160K, 160KB

180K tek yüzlü, 5.25 inç disk 180, 180K, 180KB

320K çift yüzlü, 5.25 inç disk 320, 320K, 320KB

360K çift yüzlü, 5.25 inç disk 360, 360K, 360KB

1.2M çift yüzlü, yüksek kapasiteli, 5.25 inç disk 1200, 1200K, 1200KB,

1.2, 1.2M, 1.2MB

720K çift yüzlü, 3.5 inç disk 720, 720K, 720 KB

1.44M çift yüzlü, yüksek kapasiteli, 3.5 inç disk 1440, 1440K, 1440KB,

1.44, 1.44M, 1.44MB

2.88M çift yüzlü, yüksek kapasiteli,3.5 inç disk 2880, 2880K, 2880KB,

2.88, 2.88M, 2.88MB

/d:tarih Verilen tarihten sonra değiştirilen en son dosyaları yedekler.

/t:zaman Verilen zamandan sonra değiştirilen dosyaları yedekler.

/L:dosyaadı Burada verilen isimle dosya açılır. Bu dosyada yedekleme zamanı, yedekleme

tarihi, yedeklenen dosyaların listesi ve yedeklenen dosyaların bulunduğu yedekleme

diskinin numarası vardır. Eğer dosya ismini belirlemezseniz backup komutu disk

üzerindeki ana dizinde backup.log ismiyle bir dosya açıp, yukarıda bahsedilen bilgileri

bu dosyaya yazar.

Örnekler :

Backup c:\\muhasebe\\\*.\*/s a: ↵

Hardiskin muhasebe dizininde ve bu dizin altındaki tüm altdizinlerinde bulunan dosyaların tamamını A sürücüsüne yedekler.

Yedeklenecek dosyaların tamamı bir diskete sığmıyorsa, disket dolduktan sonra MS-DOS sizden ikinci (üçüncü, dördüncü...) disketi A sürücüsüne takmanızı ister.

Yedekleme yapılan diskette önceden var olan dosyalar silinecektir.

Backup c\\muhasebe\\\*.dat a: ↵

Hardiskin muhasebe dizininde bulunan ve uzantısı .dat olan dosyaları A sürücüsüne yedekler.

**BREAK**

**Durdurma**

Amaç : Control-C tuşunu kontrol eder.

Dizilim : Break \[on : off\]

Çalıştırdığınız programa bağlı olarak işlemi durdurmak için Ctrl+C tuşunu kullanabilirsiniz. Komutu break on’a ayarlarsanız MS-DOS, Ctrl+C tuşuna basılıp basılmadığını kontrol etmeye başlar.

Örnek:

Break on ↵

**CHCP**

**Kod Sayfası Değiştirme******

Amaç : En son kod sayfasını değiştirir ya da görüntüler.

Dizilim : chcp \[nnn\]

nnn kod sayfasının değeridir.

Değer kod sayfası

Birleşik Devletler (varsayılan değer)

Çok dilli (birden fazla dilde)

Portekizce

Kanada – Fransızca

iskandinav

Örnekler :

chcp ↵

Aktif kod sayfasını görüntüler.

chcp 850 ↵

Kod sayfasını yeni verilen kod sayfasına değiştirir.

**CHDIR**

**CD**

**Dizin Değiştirme**

Amaç : Bir dizinden başka bir dizine geçmeyi sağlar.

Dizilim : Chdir \[\\dizinadı\]

veya

cd \[\\dizinadı\]

Chdir \[.. \]

veya

cd \[.. \]

Chdir

veya

cd

MS-DOS’un en çok kullanılan komutlarından biridir. CD komutunun kullanımı çok kolaydır fakat, dizin yapısı iyi anlaşılmamışsa bir takım bir takım zorluklarla karşılaşılabilir. Bu durumda dizin konusunu tekrar okumanın yararı olacaktır.

Örnekler :

cd ↵

Çalışılan dizinin adını görünrüler.

cd \\ ↵

Diskin herhangi bir dizin veya altdizindeyken ana dizine geçer.

cd \\ muhasebe ↵

herhangi bir dizinde iken muhasebe adındaki dizine geçer.

cd .. ↵

Çalışılan yer bir altdizin ise, bu altdizinin bulunduğu dizine geçer. Çalışılan yer bir dizin ise, ana dizine geçer.

Muhasebe dizinin altında eski muhasebe isimli bir altdizin olduğunu varsayalım.

cd eskimuh ↵

Eğer muhasebe dizininde iseniz, eskimuh isimli altdizine geçer.

cd \\muhasebe\\eskimuh ↵

Hangi dizinde olursanız oluni muhasebe dizininin altındaki eskimuh altdizinine geçer.

**CHKDSK**

**Çekdisk**

Amaç : istenilen sürücüdeki diski çek eder.

Dizilim : chkdsk \[sürücü:\]\[\\dizinadı\\dosyaadı\]\]/f\]\[/v\]

Chkdsk komutu diskinizin durumunu gösterir. Herbir diskte hata kontrolü için arasıra chkdsk’i çalıştırmalısınız. Eğer chkdsk’i çalıştırdığınız da bir hata bulunursa, chkdsk hata mesajı görüntüler.

Chkdsk komutunun anahtarları :

/f Diskteki hataları tesbit edip temizler.

Ten lost clusters found in 3 chains.

Convert lost chains to files (Y/N) ?

Y yi seçerseniz kayıp bilgiler filennnn.chk isimli (FILE0000.CHK, FILE0001.CHK, FILE0002.CHK,...)dosya(lar) haline gelir. Chkdsk tamamlandığında bu dosya(lar)ın içeriklerinin gerekli olup olmadığını kontrol edip silebilirsiniz . Eğer N yi seçerseniz kayıp kümelerin içindeki bilgiler saklanmaz , fakat hata düzeltilir. /f anahtarı kullanılmazsa chkdsk diskinizde bulduğu hatayı düzeltmez.

/v Her bir dizindeki her bir dosya ismini diski kontrol ederek görüntüler.

Chkdsk subst ya da join komutlarının kullanıldığı sürücülerde çalışmaz.

Örnekler :

chkdsk a: ↵

A sürücüsündeki disketi çek et.

Bu komutu uyguladıktan sonra aşağıdakine benzer bir rapor durumu gelir.

Volume SELSUS created 11-23-1991 1:23a

Volume Serial Number is 236F-14D2

730112 bytes total disk space (disket toplam kapasitesi)

466944 bytes in 14 user files ( dosya sayısı ve toplam uzunluğu)

10240 bytes bad sectors ( bozuk alanların miktarı)

252928 bytes available on disk (Disketteki boş alan)

1024 bytes in each allocation units

713 total allocation units on disk

247 available allocation units on disk

655260 total bytes memory (bilgisayarın toplam hafızası)

514288 bytes free (bilgisayarın boş alanı)

chkdsk c: > cek.rp ↵

Hardiski çek ettikten sonra durum raporunu cek.rp isimli dosyaya yazar.

**CLS**

**Ekran Silme**

Amaç : Ekranı siler

Dizilim : cls

Cls komutu çalışılan diskin ismini belirten harfi ve imleci ekranın sol üst köşesinde bırakarak ekrandaki diğer görüntüleri siler.

Örnek :

cls ↵

**COMMAND**

Amaç : Yeni komut işlemcisi başlatmak.

Dizilim : Command \[sürücü:\]\[\\dizinadı\]\[ünite\]\[/e:nnnn\]\[/p\]\[/c string\]\[/msg\]

Bu komut yeni komut işlemcisini başlatır. Yeni komut işlemcisine başladığınızda siz aynı zamanda yeni komut çeşitlemenizi yaratırsınız. Bu yeni çeşitleme eski eş çeşitlemenin bir kopyasıdır. Her durumda yeni çeşitlemeyi eskisini etkilemeden değiştirebilirsiniz.

Komut işlemcisi hafızaya iki parti halinde yüklenir. Geçici ve kalıcı. Bazı programlar çalıştırıldığında command.com’un geçici hafızası üzerine yazarlar. Bu durumda command işlemlerinin kalıcı bölümü disk üzerinde command.com’u arar ve böylece geçici bölüm yeniden yüklenir. Geçici kısmın hafızaya yeniden yüklenmesine ihtiyaç varsa, sürücü: ve \\ dizinadı komut işlemine command.com’u nerede bulunacağını söyler.

Command komutunun anahtarları :

/e:nnnn nnnn’in 160 dan 32768 bytes arasındaki alanını belirler. MSDOS bu numarayı bir

sonraki bölgesel paragraf sınırına kadar çevreler. Varsayılan değer 160 byte dır.

/p İkinci komut işlemini hafızada saklar ve otomatik olarak önceki komut işlemine dönmez.

/c string Komut işlemine string tarafından belirlenen komutu ya da komutların görevini yerine

getirmesini söyler ve daha sonra otomatik olarak önceki komut işlemine döner.

/msg Hata mesajlarını hafızada tutar.

Örnek :

Command /chkdsk a: ↵

**COMP**

**Dosya Karşılaştırma**

Amaç : Eşit uzunluktaki iki dosyayı karşılaştırıp farklarını listeler.

Dizilim : comp\[sürücü:\]\[\\diziadı\\dosyaadı1\]\[sürücü:\]\[\\dizinadı\\dosyaadı2\]\[/d\]\[/a\]\[/u\]\[/n=sayı\]\[/c\]

Comp komutu bir dosya ya da dosyalar setini \[\\diziadı\\dosyaadı1\], ikinci bir dosya ya da dosyalar seti \[\\dizinadı\\dosyaadı2\] ile karşılaştırır. Bu dosyalar aynı sürücüde ya da farklı sürücülerde olabilir. Ayrıca aynı dizinde ya da farklı dizinlerde de olabilir. Karşılaştırma yapacağınız iki dosya seti farklı sürücülerde olmak şartıyla aynı dizinde ve aynı isimlerde olabilir. Eğer sadece ikinci seçenek için sürücü ismini yazarsanız comp\\dizinadı\\dosyaadı1 ve \\dizinadı\\dosyaadı2 nin aynı olduğunu farzeder.

\\dizinadı\\dosyaadı2 seçeneğini atlarsanız comp bunlar için sizi uyayrır. İki seçenekten biri sadece sürücüden ve dosya ismi olmayan bir dizinadından oluşursa comp dosya ismini \*.\*(bu işaret tüm dosya adlarını içine alır) olarak kabul eder. Eğer karşılaştırmak istediğiniz dosyalar comp’un olduğu diskten başka bir diskte ise comp komutunu seçeneksiz yazın. Comp\\diziadı\\dosyaadı seçeneği için sizi uyardığında sadece doğru diski girip karşılaştırma yapılacak dosya isimlerini yazınız. Comp ilerledikçe dizinadlarını ve karşılaştırma yapılacak dosya isimlerini görüntüler. Eğer comp\\dizinadı\\dosyaadı2 seçeneğine uygun bir dosya bulunmazsa ya da dizin yolu geçersizse bir hata mesajı gelir. Eğer \\dizinadı\\dosyaadı1 seçeneğine hiçbir dosya uymazsa comp her iki dizinadı/dosyaadı seçeneği için sizi uyarır.

Karşılaştırma boyunca birbirine uygun olmayanlar dosyaları gösteren bir mesaj ortaya çıkar.

Bu mesaj dosyalarda birbirine uygun olmayan byteları ve byteların içindekilerini karşılaştırarak gösterir. Bu mesaj aşağıdaki formata sahiptir;

Compare error at OFFSET xxxxxxxx

dosya1 = xx

dosya2 = xx

Bu formatta dosya1 yazılan birinci dosya ismi dosya2 ise yazılan ikinci dosya ismidir. On tane dengi bulunmayan karşılaştırmadan sonra comp karşılaştırmayı duruduru ve şu mesajı görüntüler;

10 mismatches-ending compare

Eğer dosya ölçüleri değişikse comp aşağıdaki mesajı görüntüler :

Files are different size, do you wish to continue (Y/N) .

Karşılaştırmaya devam edebilirsiniz ya da bitirebilirsiniz. Eğer devam seçeneğini seçerseniz comp daha kısa olan dosyanın sonuna ulaşana kadar karşılaştırmaya devam eder.

Uyumlu bir karşılaştırmadan sonra comp aşağıdaki mesajı görüntüler;

Files compare OK

İki dosya karşılaştırması bittikten sonra comp iki \\dizinadı\\dosyaadı seçeneğine uygun bir sonraki dosya çiftine ilerler bu durum \\dizinadı\\dosyaadı1 seçeneğine uygun başka bir dosya bulunmayana kadar devam eder. Comp bundan sonra aşağıdaki mesajı görüntüler:

Compare more files (Y/N) ?

Bu durumda iki dosya karşılaştırması daha yapılabilir ya da karşılaştırmayı bitirebilirsiniz. Eğer iki dosya daha karşılaştırmak istiyorsanız Y’yi seçiniz. Comp bu durumda iki yeni path seçeneği için sizi uyarır.

Bütün karşılaştırmalar için comp öncelikle her iki dosyanında dosya sonu işareti (ctrl+Z) içinde olup olmadığına bakar. Eğer değilse comp şu mesajı verir:

EOF mark not found.

Comp komutunun anahtarları :

/d Farklı karakterleri ASCII numaralarıyla gösterir.

/a Farklı karakterleri ASCII karakteri olarak (ekranda görüldüğü gibi) gösterir.

/I Farklı karakter(ler) bulunan satırların satır numaralarını gösterir.

/n=sayı Karşılaştırmayı verilen sayı kadar satırda yapar.

/c Karşılaştırma yaparken büyük küçük harf ayrımı yapmaz.

Örnek :

comp c: \***.**prg b: \*. bak ↵

C sürücüsündeki uzantıları .prg olan ve B sürücüsündeki uzantıları .bak veya aynı isimde olan dosyaları karşılaştırır.

**COPY**

**Dosya Kopyalama******

Amaç : Bir veya daha fazla dosyayı başka bir yere kopyalar. Bu komut ayrıca dosyaları

birleştirir.

Dizilim : Dosyaları kopyalamak için :

Copy\[sürücü:\]\\dizinadı\\dosyaadı1\[sürücü:\]\[\\dizinadı\\dosyaadı2\]\[/v\]\[/a\]\[/b\]

Ya da

Copy \[sürücü:\]\\dizinadı\\dosyaadı1\[/v\]\[/a\]\[/b\]\[sürücü:\]\[\\dizinadı\\dosyaadı2\]

Dosyaları eklemek için :

Copy\\dizinadı\\dosyaadı1+\\dizinadı\\dosyaadı2\[...\]\\dizinadı\\dosyaadı

Eğer \\dizinadı\\dosyaadı2’yi belirlemezseniz kopyalama disk üzerindeki en son çalışan dizinde ve sürücüye yaratılır. Bu kopya orijinal (\\dizinadı\\dosyaadı1) ile aynı isme, aynı zaman ve aynı tarihe sahiptir. Eğer orijinal dosya en son çalışılan sürücüde ise ve \\dizinadı\\dosyaadı2’yi belirlemiyorsanız copy komutu durur ve aşağıdaki hata mesajını verir;

File can not be copied on to it self 0 file(s) copied

Kopyalanmak istenen dosya sürücü ve dizinadı verilmemişse çalışılan sürücü ve dizinde aranır bulunamadığında da MS-DOS hata mesajı verir.

File not found – dosyaadı

0 file(s) copied

Copy komutunun anahtarları :

/v Hedef diskte yazılı bölümün tam olarak kayıt edildiğini doğrular. Bu anahtar

kullanıldığında işlem hızı yavaşlar.

/a ASCII dosyalarını kopyalamanıza müsaade eder. Dosya ASCII değilse (dosynın

herhangi bir yerinde dosya sonu işareti varsa) dosyayı eksik kopyalar.

/b Dosyanın tamamını kopyalar (Dosyanın çeşitli yerlerinde bir veya daha fazla dosya

sonu işareti bulunsa da).

Copy komutu anahtarları /a ve /b kaynak kaynak dosya ismi ya da hedef dosya isminin önünde bulunmalarına göre değişik şekilde işlem görürler.

Kaynak dosya ismi önünde kullanılmadıkları zaman:

/a Dosyanın ASCII dosyası gibi kullanılmasını sağlar. İlk dosya sonu işareti hariç

dosyadaki veri kopya edilir. Dosyanın, dosya sonu işaretinden sonra kalanı kopya

edilmez.

/b Dosya sonu işareti dahil dosyanın tamamının kopya edilmesini sağlar.

Hedef dosya ismi önünde kullanıldıkları zaman:

/a Dosyasonu işaretini dosyanın en son karakteri gibi eklemesine sebep olur.

/b Bir dosyasonu karakterini eklemez.

Dosyaları bir araya getiriken geçerli anahtalar daima /a dır.

Örnekler:

Copy fiyat.txt a: ↵

Bulunduğunuz disk ve dizindeki fiyat.txt dosyası, A sürücüsündeki diskete kopyalanır. Eğer A sürücüsünde iseniz, kendi üstüne kopya yapamayacağından hata mesajı verir.

Copy fiyat.txt a:sonfiyat.txt ↵

Fiyat.txt doyası, A sürücüsüne sonfiyat.txt olarak kopyalanacaktır.

Copy fiyat.txt yenifiyat.txt ↵

Bulunduğunuz disk ve dizindeki fiyat.txt doyası aynı yere aynı yenifiyat.txt ismiyle kopyalanır. Dosyayı çiftlemiş olursunuz.

Copy fiyat.txt \\yeniyıl ↵

Fiyat.txt dosyası yeniyıl isimli dizine kopyalanır.

Copy \\eski\\es-fiyat.txt ↵

Eski dizindeki es-fiyat.txt dosyası bulunduğunuz dizne kopyalanır.

Copy a:\*.\* c:\\yeni ↵

A sürücüsüne taktığınız disketteki tüm dosyalar hardiskteki yeni isimli dizine kopyalanacaktır.

Dosya birleştirme :

Copy \*.asm toplam.asm ↵

Uzantısı .asm olan bütün dosyaları toplam.asm olan dosyaya toplar.

Copy prog1.prg+prog2.prg ↵

Prog2.prg dosyası prog1.prg dosyasının sonuna eklenir.

Copy prog1.prg+prog2.prg sonprog.prg ↵

Prog1.prg dosyası ve prog2.prg dosyası, sonprog.prg isimli dosyasına toplanır.

**CTTY**

Amaç : Standart giriş/çıkış (input/output) komutlarını bilgisayırın ekran ve klavyesinden bir

yardımcı üniteye çevirir.

Dizilim : ctty ünite

Örnekler:

ctty aux ↵

Giriş/çıkış (I/O) komutlarını standart üniteden AUX port’a yöneltir.

ctty con ↵

Bilgisayarı eski durumuna döndürür.

**DATE**

**Tarih Gösterme / Değiştirme******

Amaç : Tarihin ayarlanması veya ekrana verilmesi.

Dizilim : date \[mm-dd-yy\]

Date \[ay-gün-yıl\]

Tarihi kendi terminalinizden veya toplu işlem dosyasından değiştirebilirsiniz. Eğer bir autoexec.bat kullanıyorsanız, MS-DOS tarih için ekranda otomatik olarak bir yazı yazmayacaktır, bu durumda o dosyaya bir date komutu ilave etmek isteyebilirsiniz.

Tarih yazarken sadece rakamları kullanınız; kullanabileceğiniz rakamlar şöyledir:

Ay için mm = 1-12

Gün için dd = 1-31

Yıl için yy = 80-79 veya 1980-2079

Tarihi yazarken gün, ay ve yıl rakamlarını (-) tire ya da (/) taksim işaretlerini kullanarak birbirinden ayırabilirsiniz. MS-DOS söz konusu ay ister 28-29 vaya 30, ister 31 gün çeksin, ay ve yıllar doğru olarak değiştirilebilmek üzere programlanmıştır.

Tarihi girdiğiniz veya ekrana verdiğiniz mm-dd-yy formatını değiştirebilmeniz de mümkündür. Config.sys dosyasındaki country komutu tarih formatını dd-mm-yy şeklinde avrupa standart formatına da değiştirebilmenizi sağlar.

Örnekler:

date ↵

Bu komutu verdiğinizde aşağıdaki mesaj gelir:

Current date is weekday mm-dd-yy

Enter new date (mm-dd-yy):\_

Burada weekday haftanın gününü işaret eder (Örnek olarak Salı). Gösterilen tarihi değiştirmek istiyorsanız ENTER tuşuna basınız. Ya da date komutundan sonra belli bir tarihi yazabilirsiniz.

date 3-9-88 ↵

Bu durumda ENTER tuşuna bastıktan sonra Enter new date ifadesi görülmeyecektir.

**DEBUG**

**Hata Bulma******

Amaç : Bir program test ortamı yaratarak hata saptamaya ve temizlemeye yarar.

Dizilim : debug\[dosyaadı\[parametreler\]\]

Veya

Debug

Bu komut ayrı bir bölüm olarak kitapta geniş yer verilerek anlatılmıştır. Tüm debug komutlarını DEBUG ana bulabilirsiniz.

**DEL**

**ERASE**

**Dosya Silme******

Amaç : Belli bazı dosya kayıtlarının silinmesi.

Dizilim : del\[sürücü:\]\\diziadı\\dosyaadı/p

veya

erase\[sürücü:\]\\dizinadı\\dosyaadı/p

Bir dosyanın silinmesi o dosyanın diskte yazılı bulunduğu yerlerin serbest kaldığına dair işaretlenmesidir. Yani dosyalar başlangıçta tam olarak silinmezler. Yeni bir dosya diske yazılacağı zaman ilk olarak silinmiş dosya üzerine yazılır ve silinen dosyanın bilgileri tam olarak silinir.

Eğer bir dosya yanlışlıkla silinmişse başka bir dosya yazma işlemi yaptırmadan undelet komutu ile kurtulunabilir. Daha fazla bilgi için undelete komutuna bakın.

Del komutunun anahtarları :

/p Anahtarı herhangi bir silme olayı gerçekleştirilmezden önce del veya erase’in sizi

uyarmasını sağlar. Eğer bu anahtar seçilirse her dosya ekranda gösterilir veya size

dosya adı hatırlatılır.

delete (Y/N) ?

silinecek Evet mi, Hayır mı ?

Silme işlemini Y tuşu ile onaylar veya N ye basarak iptal edersiniz.

Del komutu size \* ve ? jokerlerini kullanma olanağı verir ve böylece bir defada birden fazla dosya silebilirsiniz. Bu metodla dosya silme işlemi oldukça rahat olmakla beraber tehlikeli de olabilir. Bu yüzden jokerleri dikkatli kullanınız.

Şayet del\*.\* yazarsanız bu mesaj MS-DOS’a çalıştığınız dizindeki tüm dosyaları silmek istediğinizi bildirecektir. Bu durumda MS-DOS ekranda :

Are you sure (Y/N) ?

Eminmisiniz (Evet/Hayır) ?

Sorusunu yazar.

Cevap olarak Y verirseniz, MS-DOS çalıştığınız dizindeki bütün dosyaları silecektir.

Örnekler :

del fiyat.bak ↵

fiayt.bak ismindeki bir tek dosyayı siler.

del fiyat.\* ↵

Adı fiyat ve uzantısı herhangi bir şey olan tüm dosyaları siler.

del \*.bak ↵

Adı herhangi bir şey olan ve uzantısı .bak olan tüm dosyaları siler.

del . ↵

del \*.\* ↵

erase . ↵

erase \*.\* ↵

Bu komutların hepsi de dizindeki tüm dosyaları siler.

del muhasebe ↵

Diskinizde muhasebe isimli bir dosya varsa silinir. Eğer muhasebe isimli bir dizin mevcutsa bu dizin içindeki tüm dosyalar silinecektir. Bu ikinci halde MS-DOS;

All files in directory will be delated !

Are you sure (Y/N) ?

Dizinde bulunan bütün dosyalar silinecektir !

Eminmisiniz (Evet/Hayır) ?

sorusuyla sizden ikinci bir onay isteyecektir.

**DIR**

**Dosya Listesi**

Amaç : Herhangi bir dizindeki dosyaların listesinin yapılması

Dizilim : dır\[sürücü:\]\\dizinadı\\dosyaadı\]\[/p\]\[/w\]\[/a\[\[:\]nitelik\]\]\[/o\[\[:\]sıar\]\]\[/s\]\[/b\]\[/l\]

Tek başına kullanılan dır komutu üzerinde çalıştığınız dizindeki bütün dosya isimlerini ve bu dosyalara ait uzunluk, kayıt tarihi ve kayıt zamanı bilgilerini ekrana veya bir dosyaya listeler. Dır ayrıca sürücnün kodunu ve seri numarasını da listede verir.

Eğer dır komutu ile bir sürücünün adını da dahil ederseniz (“B” gibi) o sürücü içerisindeki disketin çalışılmakta olan dizindeki tüm girdilerin listesi çıkartılır.

Dır komutunun anahtarları:

/p Sayfa modunu seçer, ekran doldurulduğu zaman listeleme işlemi durur. Devam etmek

için bir tuşa basılır.

/w Dosya listesini sadece dosya isimlerini vererek ekrana beş sütun halinde sıralar. Daha

çok dosyayı bir arada görme imkanı verir.

/a\[:\]nitelik Sadece istenilen nitelikteki dosyaları görüntüler. Dosya nitelikleri için ATTRIB komutuna

bakınız.

/o\[:\]sıra Dosyaları görüntülerken alfabetik sıraya, tarih sırasına göre veya uzunluklarına göre

sıraya koyar.

/s Altdizinde bulunan dosyaları da gösterir.

/b Sadece dosya isimlerini gösterir.

/l Dosya isimlerini ekrana küçük harflerle yazarak gösterir.

Örnekler:

dir ↵

dir \*.\* ↵

Çalışılan dizindeki bütün dosyaları sonuna kadar kesintisiz olarak listeler.

dir a: ↵

dir a: . ↵

dir a: \*.\* ↵

A sürücüsünde bulunan disketin içerisindeki dosyaları listeler.

dir fiyat ↵

dir fiyat.\* ↵

dir fiyat.??? ↵

Çalışan dizinde ismi fiyat olan tüm dosyaları listeler.

dir f\* ↵

dir f\*.\* ↵

Çalışılan dizinde ismi f harfi ile başlayan tüm dosyaları listeler.

dir .txt ↵

dir \*.txt ↵

Çalışılan dizinde uzantısı .txt olan tüm dosyaları listeler.

dir ??? ↵

Çalışılan dizinde ismi sadece üç harf olan dosyaları listeler.

dir f?? ↵

Çalışılan dizinde ismi sadece üç harf olan ve ismi f ile başlayan dosyaları listeler.

dir ?f? ↵

Çalışılan dizinde ismi sadece üç harf olan ve ikinci harfi f olan dosyaları listeler.

Bu örneklerle birlikte yukarıda listelenen anahtarlar tak başına ya da bir kaçı bir arada kullanılabilir.

**DISKCOMP**

**Disket Karşılaştırma**

Amaç : Kaynak sürücü içindeki disketin içeriği ile hedef sürücü içindeki disketinin içeriğini

karşılaştırılması.

Dizilim : discomp\[sürücü1:\]\[sürücü2:\]\[/1\]\[/8\]

Sürücü1 kaynak sürücü,

Sürücü2 de hedef sürücü anlamına gelmektedir.

Discomp komutunun anahtarları:

/1 Kulandığınız disket ve sürücüler çift yüzlü olsa bile discomp’un sadece disketinin ilk

yüzünü karşılaştırmasını sağlar.

/8 Disketlerde her iz’de 9 ile 15 sektör olsa bile, discomp’un ilk sekiz sektörü

karşılaştırmasını sağlar.

Eğer sadece bir sürücü belirlemişseniz discomp hedef sürücü olarak o hedef sürücüyü kullanır. Kaynak ve hedef sürücüsü olarak aynı sürücüyü belirlemişseniz discomp bir sürücüyü kullanarak mukayese yapar ve disketleri sırayla sürücüye yerleştirmeniz için size bilgi gönderir.

Şayet bütün işaretler aynı ise discomp şu mesasjı verir:

Compare OK

Karşılatırma sonucu: tamam

Şayet işaretler aynı değil ise discomp:

Comaper error

Karşılaştırma sonucu : Hata var

mesajını verir.

Ayrıca uyumsuzluğun tespit edildiği yüzün numarası (O veya 1) ile işaret numarasını gösterir.

Eğer hedef disketi kaynak sürücünün içindeki disket ile aynı tipte değil ise discomp şu mesajı verir:

Drive types or diskette types not compatible

Sürücü veya disket tipleri uyumlu değil.

Discomp, karşılaştırmayı bitirince sizi şöyle bir mesajla uyaracaktır:

Compare another diskette (Y/N) ?

Başka disket karşılaştırılacakmı (Evet/Hayır) ?

Eğer Y tuşuna basarsanız discomp uygun diketleri sokmanızı ister veya bir sonraki karşılaştırmayı yapar. Şayet N tuşuna basarsanız discomp sona erer.

Bazen iki disketin içeriği aynı olsa bile compare error mesajı gelebilir. Bu durum disketlerdeki bilgilerin yerleşimleri farklı olduğundandır. Böyle bir durumda fc komutunu kullanın.

Discomp network altında assing, join veya subst komutlarının arkasından kullanılmaz. Şayet kullanmaya kalkarsanız hata komutu verecektir.

Örnekler:

discomp a: a: ↵

Bilgisayarınız tek sürücülü ise komutu bu şekilde yazınız. MS-DOS size uygun sırayla disketi yerleştirmeniz için mesaj verecektir.

discomp a: b: ↵

Bilgisayarınız iki sürücülü ise komutu bu şekilde yazıp disketlerinizi her iki sürücüye yerleştiriniz.

**DISCOPY**

**Disket Kopyalama**

Amaç : Kaynak sürücünün içindeki disketi içeriği hedef disketin içindeki formatlı veya

formatsız bir diske kopya eder.

Dizilim : discopy \[sürücü1:\]\[sürücü2:\]\[/1\]\[/v\]

sürücü1 kaynak sürücü

sürücü2 ise hedef sürücüdür.

1 ve 2 nolu sürücüler aynı olabilir. Eğer hedef disket formatlanmamışsa discopy kopyalama işleminden önce disketi formatlar. Bu komutla sadece disket kopyalanır. Hardiski kopyalayamazsınız.

Discopy komutunun anahtarları :

/1 paramatresi bir diskin sadece bir yüzünü kopya edilmesini temin eder.

/v Hedef diskette yazılı bölümün tam olarak kayıt edildiğini doğrular. Bu anahtar

kullanıldığında işlem hızı yavaşlar. Kopyalama işleminden sonta discopy size şu mesajı

iletir:

copy another diskette (Y/N) ?

Başka disket kopya edilecek mi (Evet/Hayır) ?

Şayet bu soruya cevap olarak Y basarsanız MS-DOS size kaynak ve hedef disketlerini sokmanız için uyarı gönderir ve önceden belirlediğiniz sürücüler üzerinde müteakip kopyalama işlemini yapar.

Discopy işlemini bitirmek için N’ye basınız.

Discopy yerine copy veya xcopy komutlarını kullanmak daha iyidir.

Örnekler:

discopy a: a ↵

Bilgisayarınız tek sürücü ise komutu bu şekilde yazınız. MS-Dos size uygun sırayla disketi yerleştirmeniz için mesaj verecektir. Eğer bilgisayarın hafızası disket kapasiyesinden küçük ise bu mesajlara uyarak diseketler “copy another diskette (Y/N)?” mesajı gelene takıp çıkarmanız gerekecektir.

discopy a: b: ↵

Bilgisayarınız iki sürücülü ise komutu bu şekilde yazıp kopyalanacak disketi a sürücüsüne boş disketi b sürücüsüne yerleştirn. Bir tuşa bastığınızda kopyalama işlemi başlar.

**DOSKEY**

**Komut Ajandası**

Amaç : Bilgisayar açıldıktan sonra kullanılan her komutu hafızada tutar.

Dizilim:doskey\[/reinstall\]\[/bufsize=büyüklük\]\[/macros\]\[/history\]\[/insert\]\[:/overstrike\]\[macroadı=\[metin\]\]

Veya

doskey

Doskey komutunun anahtarları:

/reinstall Önceden bir doskey programı yüklenmiş bile olsa yeni bir doskey kopyasını yükler.

/bufsize=büyüklük Doskey’in komutları ve makrolaro sakladığı aktif hafızayı belirler. Hazır değer

512 bayt, en düşük verilebilecek değer ise 256 bayt’tır.

/macros Tüm doskey makrolarını listeler. / macros yerine /m kısaltması kullanılabilir.

/history Hafızadaki tüm komutları listeler. /h şeklinde kısaltılabilir.

/insert:/overstrike Yazdığınız yeni komut metninin eskisinin üstüne yazılmasını veya

yazılmamasını sağlar. /overstrike üstüne yazdırır, /insert eski dosyaya ekleme yapar.

Doskey’in hafızaya yüklediği eski komutlara tekrar erişebilmek için aşağıdaki tuşlar kullanılır:

Çağırma tuşları :

Yukarı ok Bir önceki komutu çağırır

Aşağı ok Bir sonraki komutu çağırır

Pg up En eski dos komutunu çağırır

Pg dn En yeni dos komutunu çağırır

Düzeltme tuşları :

Sol ok İmleci bir sola kaydırır

Sağ ok İmleci bir sağa kaydırır

Ctr+sol ok İmleci bir kelime sola kaydırır

Ctr+sağ ok İmleci bir kelime sağa kaydırı

Home Satır başına gelir

End Satır sonuna gelir

ESC Satır siler

F1 Son olarak yazdığınız komutu tekrar çağırır

F2 F2 ye bastıktan sonra yazacağınız bir karakterden itibaren hafızayı tarar ve

bulduklarını ekrana getirir.

F3 Hafızada kalan bilgileri komut satırına ekler

F4 Hafızada baştan başlayarak belirleyeceğiniz bir karaktere kadar olan tüm

karakterleri siler. Önce F4’e basınız sonrada karakteri giriniz.

F5 Ekrandaki aktif komutu hafızaya kopyalar ve komut satırını siler.

F6 O an ki komut satırı sonuna komut sonu karakterini koyar.

F7 Hafızadaki tüm komutları doskey’in vermiş olduğu sıra numaraları ile birlikte

listeler.

Alt+F2 Hafızadaki tüm komutları siler.

F8 Bir komutun daha önce kullanılıp kullanılmadığını arar. Bu tuşa bastıktan sonra da

doskey’in aramasını istediğiniz komutun ilk veya ilk birkaç harfini giriniz. Doskey

bu komutu arayıp ekrana getirecektir.

F9 Girdiğiniz komut numarasına ait komutu ekrana getiri.

Alt+F10 Tüm makro tanımlarını iptal eder.

Insert tuşuna basarak dos komut satırındaki aralara eklemeler yapabilirsiniz. Ancak enter’a bastığınızda doskey insert modundan çıkar. Gerektiğinde tekara insert’e basarak işlem yapabilirsiniz.

Örnek:

doskey ↵

Bu komut verildikten sonra her kullanılan komut hafızada tutulacaktır. Yukarıda listesini verdiğimiz tuşlar yarımıyla bu komutlara tekrar erişip onları kullanabilirsiniz.

devicehigh doskey ↵

Bir önceki örnekle aynı işi yapar. Doskey üst hafızaya yüklenir ve diğer programları çalıştırmak için daha çok yer kalır.

**Makro Yaratma**

Bir makro tanımlarken aşağıdaki karakterleri kullanabilirsiniz:

$G veya $g Çıkışın ekra yerine bir dosyaya yapılmasını sağlar. “>” işareti ile eşdeğer

taşır.

$G$G veya $g$g Çıkışı bir dosyanın sonuna ekler.

$L veya $l Girdinin klavye yerine bir dosyadan okunmasını sağlar.

$B veya $b Makro çıkışını bir komuta gönderir. Komut sırasında kullanılan : işareti ile de

aynı işlemi yapabilirsiniz.

$T veya $t Komut satırında komutları birbirinden ayırmada kullanılır.

$$ $ işareti basar.

$1-$9 Toplu işlem dosyalarındaki %1 işaretinin görevini yapar. Makroyu her

kullanışınızda bu değişkenin yerine dilediğiniz girdiyi yazabilirsiniz.

$\* Komut satırında makro isminden sonra gireceğiniz tüm karakterler yerine $\*

komutunu kullanabilirsiniz.

Örnekler:

Bir formatlama işlemi için şu makroyu girebilirsiniz:

doskey f=format $1↵

Bu makroyu çalıştırmak için

f a: ↵

yazarız.

Bu komut, “FORMAT A:” komutuyla aynı işi görür.

Her gün aynı dosyaları “A:” sürücüsüne yedeklediğimizi varsayalım. Aşağıdaki makro hem komutunuzu kısaltacak hem de dalgınlıkla yanlış komut vermenizi engelleyecektir.

doskey kopya=copy\*.dat a: ↵

Bu makroyu çalıştırmak için

Kopya ↵

yazmamız yeterlidir.

Bu yeni komut uzantısı .DAT olan dosyamızı A: sürücüsündeki diskete kopyalar.

**MS-DOS Komutu ile aynı isimde bir makro yaratmak için:**

Bazen bir dos komutunun hem aynı anahtarlarla kullanmak isteyebiliriz. Bu durumda dos komutuyla aynı ismi taşıyan bir makro yaratmak yararlı olacaktır. MS-DOS komutunu mu yoksa aynı isimli makroyu mu çalıştırmak istediğinizi belirtmek için:

Makroyu çalıştırmak için makro komutunu uyarı komutunun hemen yanına boşluk bırakmadan ayzınız.

Komutu çalıştırmak için komut ismi ile uyarı komutu arasında birkaç boşluk bırakınız.

**DOSSHELL******

Amaç : MS-DOS Shell programını başlatır.

Dizilim : DOSSHELL\[/t:/g\[res\[n\]\]\]\[/b\]

Dosshell komutunun anahtarları:

/t Dos shell’i text modunda çalıştırır.

:res\[n\] Ekran yoğunluğunu ayarlar. “res” yerine -L,M,H- harflerinden birini “n” yerine de 1 veya

2 rakamı yazılır.

/b Dos shell’i siyah beyaz olarak çalıştırır.

/g Dos shell’i grafik modunda çalıştırır.

MS-DOS Shell kullanımı ayrı bir bölüm olarak kitapta kullanılmıştır.

**EDIT**

**Metin Editörü******

Amaç : MS-DOS editörü çalıştırı. MS-DOS editör text dosyaları yaratır ve tekrar düzeltme

olanağı verir.

Dizilim : edit\[sürücü:\]\[dizinadı\]dosyaadı\[/b\]\[/g\]\[/h\]\[/nohi\]

Edit komutunun anahtarları:

/b Ekranın siyah beyaz veya renkli çalışmasını ayaralar.

/g CGA ekranın hızlı çalışmasını sağlar

/h Olabilecek en fazla sayıda satırın görüntülenmesini sağlar

/nohi Yüksek yoğunluklu bir ekranın kullanılmasını sağlar

Edit komutu çalıştırmayı ve kullanılabilecek anahtarları anlatır. Şimdi editin kullanımını daha detaylı olarak görelim.

**MS-DOS Editör’ün Menüleri ve Menüleri Kullanma**

Aşağıda MS-DOS editörün ekranını ve ana menüsünü görmektesiniz.

Ana menü satırına ulaşmak için “alt” tuşuna basmak yeterlidir. Ana menü ve alt menülerin kullanımı aynıdır. Klavyenin sol tarafında bulunan sağ, sol, yukarı ve aşağı ok tuşalrı yardımıyla seçeneklerden bir tanesi patlak konuma getirilir. Enter tuşuna basmakla o menünün yapacağı işlemi başlatmış oluruz. “Esc” tuşu ise menüden çıkıp editör ekranına dönmemizi sağlar.

File EditSearchOptions Help Untitled

Şimdi alt menüleri tek tek görelim:

**File (Dosya) Altmenüsü******

FileEdit SearchOptions

New

|  | Open... |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | Save |  |  |  |  |
|  |  | Save As... |  |  |  |  |
|  |  | Print... |  |  |  |  |
|  |  | Exit... |  |  |  |  |

File altmenüsü diskten okuma – diskte yazdırma işlemlerini dosya yazdırmayı ve program çıkışını içerir.

New Yeni bir dosya açar.

Yeni dosya açılmadan önce bellekte bir dosya varsa bunun diskte kaydedilmesi

hakkında bir uyarı penceresi gelir. “TAB” tuşuna basarak istediğiniz seçerek gelin ve

“ENTER” tuşuna basın.

Yeni dosyanın ismi “UNTITLED” (isimsiz)’dir. Asıl dosya ismi dosya diske yaılırken

verilecektir.

Open... Diskte varolan bir dosyayı açar ve MS-DOS editörün ekranına getirir.

Dosya seçimi için bir diyalog penceresi gelecektir. Bu pencereden açılacak dosya

seçilir. Dosya açma penceresinin aktif bölümleri arasında “TAB” tuşuna basarak değiştirebilirsiniz.

Save Hafızadaki (ekrandaki) dosyayı diskete yazar.

Dosyanın nereye ve hangi isimle yazılacağını soran bir diyalog penceresi gelir. Dosya

imini yazıp “ENTER” tuşuna basınız.

Save As... Hafızadaki dosyayı diske sizin vereceğiniz ikinci bir isimle tekrar yazar.

Print... Hafızadaki dosyayı yazıcıya gönderir.

Karşınıza dosyanın tamamının mı yoksa seçilen kısmının mı yazılacağı soran bir

diyalog penceresi gelir.

Exit MS-DOS editörü terk ederek MS-DOS komut satırına döner.

**Edit Düzeltme Altmenüsü**

FileEditSearchOptions

Cut Shift + Del

|  | Copy |  | Ctrl+Ins |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | Paste |  | Shift+Ins |  |  |
|  |  | Clear |  | Del |  |  |

Edit altmenüsü metnin bir kısmı üzerinde silme, kopyalama ve taşıma işlemlerini gerçekleştirir. Bu menünün işlerlik kazanabilmesi için dosyanın bir kısmının işaretlenmiş olması gerekir.

Metnin bir kısmını işaretleyebilmek için bir parmak “SHIFT” tuşuna basılırken diğer parmak “sağ, sol, yukarı veya aşağı ok” tuşlarına basarak bir kısım alanı parlatır. Böylelikle işlem yapılacak metin seçilmiş olur.

Cut İşaretlenmiş alanı daha sonra kullanmak üzere ara belleğe alır. Bu işlem “Shift ve DEL”

tuşlarına basılarak da yapılabilir.

Copy Ara belleğe alınmış alanı imlacin bulunduğu yere kopyalar. Bu işlem “Ctrl ve ins”

tuşlarına birlikte basılarak da yapılabilir.

Paste Ara belleğe alınmış alanı imlecin bulunduğu yere taşır. Bu işlem “Shift ve ins” tuşlarına

birlikte basılarak da yapılabilir.

Clear İşaretlenmiş alanı siler. Bu işlem “del” tuşuna basılarak da yapılabilir.

**Search (Arama) Altmenüsü******

FileEdit SearchOptions Find...

|  |  | Repeat Last Find | F3 |  |  |
| --- | --- | --- | --- | --- | --- |

Change

Metnin içindeki belli bir kelimeyi aramak ve değiştirmek için bu altmenü kullanılır.

Find... Dosya içinde bir kelimeyi aratmak için kullanılır.

Karşınıza bir diyalog penceresi gelir. Buraya aranacak kelime yazılıp “ENTER” tuşuna basılır.

Repeat Last Find Daha önce aratılıp buldurulan bir kelimeyi dosyanın kalan bölümünde de aranması için bu seçenek seçilir. F3 tuşuna basmak yine aynı işlevi görür.

Change... Aratılan kelimenin aynı zamanda başka bir kelime ile değiştirilmesi istenirse bu seçenek

kullanılır. Karşımıza yeni bir diyalog kutusu gelir. Buraya ilk satıra aranacak kelime

ikinci satıra da bulunan kelimenin yerine konacak kelime yazılır “ENTER tuşuna

basılır.

**Options (Seçenekler) Altmenüsü**

FileEditSearch Options Display...

|  |  |  | Help Path... |  |  |
| --- | --- | --- | --- | --- | --- |

Display... Ekran görüntüsünün ayarlanması bu seçenekle yapılır.

Help path... Buraya Help (Yardım) dosyasının bulunduğu dosya ve dizin adı yazılır.

**MS-DOS Editörde Tuşların Kullanımı**

Aşağıda anlatacağımız tuşlar imleci (cursor) metin üzerinde hareket ettirmek ve sayfa kaydırmak amacıyla kullanılır.

Sol ok ← İmleci bir karakter sola kaydırır.

Sağ ok → İmleci bir karakter sağa kaydırır.

Aşağı ok ↓ İmleci bir satır aşağı kaydırır.

Yukarı ok ↑ İmleci bir satır yukarı kaydırır.

Geri tuşu ← İmleci bir karakter sola silecek kaydırır.

Delete İmlecin üstündeki karakteri siler.

Insret Araya karakter girme modunu açar kapar.

Ctrl+A İmleç bir önceki kelimeye kayar.

Ctrl+F İmleç bir sonraki kelimeye kayar.

Home İmleci satır başına çeker

End İmleci satır sonuna çeker

Page Up Bir önceki sayfayı ekrana getirir.

Page down Bir sonraki sayfayı ekrana getirir.

Ctrl+Page up Sağdaki sayfayı ekrana getirir.

Ctrl+Page down Soldaki sayfayı ekrana getirir.

Ctrl+W Sayfa bir satır aşağı kayar.

Ctrl+Z Sayfa bir satır yukarı kayar.

Ctrl+T İmlecin sağındaki kelimeyi siler.

Ctrl+Y İmlecin bulunduğu satırı siler.

Enter İmlecin sağındaki karakterleri bir alt satıra indirir. Eğer imlecin sağında karakter

yoksa boş satır açar.

Ctrl+N İmlecin sağındaki karakterleri bir alt satıra indirir.

**EDLIN**

**Satır Editörü**

AMAÇ : Eldin,ASCII formatında dosya yaratır ve bu dosyada düzeltme yapma imkanı

sağlar .Edlin aracılığıyla toplu işlem ve config .sys dosyalarını yaratıp, gerektiği

zaman da değişiklik yapabilirsiniz.

Dizilim : **edlin**\[sürücü:\]\[dizinadı\]dosyaadı\[/b\]

Edlin komut anahtarları:

/b Birary doosya(alfabe karakterleri dışındaki karakterleri de içere)açma imkanı verir

Örnek:

Edlin caliştir.bat↵

Diskte bu isimde bir dosya yoksa edlin yeni bir dosya yaratacaktır.

New file(yeni dosya)

\*-(edlin komut uyarısı)

.Eğer böyle bir dosya varsa, bu dosyayı açacaktır.

End of input file(dosya giriş sonu)

\*-(edlin komut uyarısı)

**Edlin konut uyarısından verebileceğiniz komutlar ve komutun yazılış şekli aşağıda**

**listelenmiştir:**

? yardım ?

line satır düzeltme \[satırno\]

a satır ekleme \[n\]a

c dosyayı diske kayderek silme e

i Araya satır yerleştirme \[satırno\]i

l Satırların ekranda listelenmesi \[satırno\]\[,satırno\]L

m Satır aktarma \[satırno,\]\[+\]satırno,satırnom

p Dosyanın bir ekran sayfasını görüntüleme \[satırno\]\[,satırno\]p

q Diske kaydetmeden çıkış q

r Metin yerleştirme \[satırno\]\[,satırno\]\[?\]rtext1 control+ztext2

s Dosya içinde bir karakteri veya kelimeyi arama \[satırno\]\[,satırno\]\[?\]stext

t Başka dosyadan metin aktarma \[satırno\]tdosyaadı

w Satır yazma \[n\]w

**Edlinde kullanılan metin düzeltme tuşları:******

Edlin programında satır numarasını yazarak düzeltme işlemine girdiğimizde, düzeltilecek satır ve onun altında boş bir satır ekrana gelir. Bu boş satırda , aşağıdaki tuşlar yardımıyla düzeltilmiş yeni satırı oluşturabiliriz

F1 Bir üstteki satırın bir karakterini kopyalar. Kopyalama işlemi imlecin hizasında yapılır.

F2 Belli bir karaktere kadar kopyalama sağlar.F2 tuşuna bastıktan sonra bir harftuşuna basarsanız,o harfe kadar olan kısım kopyalanacaktır.

F3 Staırın tamamını kopyalar.

F4 Belli bir karakterden sonrasını kopyalar

F5 Alttaki satırı silip imleci başa çeker,

Ins İmlecin hizasında araya bir karakter veya karakterler yerleştirir.Insert tuşuna bastıktan sonra araya giribilecek karakterleri yazınız

Del İmlecin hizasındaki bir karakterin aşağı taşınmasını engeller.yani karakter silinir.

Esc Üzerinde çalışılan satırı iptal eder.

Geri tuşu Alt satırdaki son karakteri siler.

**EMM386**

AMAÇ: Emm386, expanded-memory destekleyicisinin 803686 bilgisayarlarda veya daha yüksek mikroişlemcisi bulunan bilgisayarda çalışıp-çalışmamasını sağlar

Dizilim: emm386\[onoff:auto\]\[w=on:w=off\]

Emm386

Emm386 komutunun anahtarları

on:off:auto Eğer “ON” anahtarı kullanılırsa EMM386.EXE ünite sürücüsü aktif hale

getirir,eğer”OFF”a set edilirse EMM386.EXE ünite sürücüsü çalışmaz

eğer”AUOT”ya set edilirse EMM386.EXE ünite sürücüsünü auto moduna getirir.

w=on:w=off Weitek coprocessor destekleyicisini olanaklı veya olanıksız kılar.

EMM386 sürücüsünün durumunu görmek için komutu anahtasız olarak vermek gerekir.

EMM386.EXE ünite sürücüsünü kurma.

Yukarıda açıkladığımız komutların işleyebilmesi için CONFİG:SYS dosyasına:

DEVICE=C:\\DOS\\EMM386.EXE

Satırının eklenmiş olması gerekir

EMM386.EXE ünite sürücüsünü ve emm386 komutunu kullanmak için bilgisayarınızın 80386 veya daha yüksek işletim sistemine sahip olması gerekir.Eğer emm386 komutu 80386 veya daha yüksek microişlemciye sahip olmayam bir bilgisayarda kullanmaya çalışırsanız MS\_DOS aşağıdaki mesaj görüntülenir

EMM386 drive not installed.

**EXE2BIN**

Amaç : exe (executable) dosyalarını bınary formatlarına çevirir.

DİZİLİM : exe2bin\[sürücü:\]\\dizinadı\\dosyaadı1\[sürücü:\]\\dizinadı\\dosyaadı2\\dizinadı\\dosyaadı1

girdi dosyası

\\dizinadı\\dosyaadı2 ise çıktı dosyasıdır

Bu komut.exe (executable) dosyalarını binary formatlarına çevirir. Eğer dizinadı1 için bir genişletme istiyorsanız, .exe komutuna giremez. Girdi dosyası bir .bin dosya formatına dönüşür, ve veri dosyasına (\\dizinadı\\dosyaadı2)yerleştirilir.

Şayet bir sürücü adı seçmezseniz , exe2bin girdi dosya ismini kullancaktır. Yani netice olarak veri dosya isminde eğer bir dosya ismi genişletme seçmezsen,z exe2bin yeni dosyaya .bin genişletmesini verecektir.

Exe2bin komutunu kullanırken bazı kısıtklamalar da vardır:girdi dosyası linker tarafından üretilen geçerli .exe formatında olmalıdır;dosyanın kalıcı veya gerçek kod ve data kısmı 64K byte’tan daha az olmalıdır; ve herhangi bir STACK segmenti bulunmamalıdır.

Başlangıç CS:IP exe dosyasında ister belirtilsin ister belirtilmesin exe2bin ile iki çeşit dönüşüm yapmak mümkündür (CS:IP=Code Segment : Instuction Pointer).

.exe dosyasında şayet CS:IP belirlenmemişse, exe2bin , açık bir binary dönüşümü istediğinizi sanacaktır.Şayet segment fixup’ları gerekiyorsa, exe2bin komutu sizi fixup değeri konusunda uyaracaktır. Bu değer programın yüklenmiş olduğu tam segmenttir. Neticede ortaya çıkan program ancak aplikasyonunuda belirttiğiniz tam hafıza adresinde yüklendiği zaman çalışacaktır. Komut işlem birimi programı yükleyemez.** **

Şayet CS:IP0000:100H ise exe2bin bu dosyanın bir .com dosyası gibi çalışacağını varsayacaktır,bu .com dosyasında ORG toplayıcı ifadesi tarafından 100H de düzenlenmiş talimat pointer’ı vardır.(dosyanın ilk 100H byte’ı silinir). .com dosyasına segment yerleştirmenin mümkün olması gerektiğinden burada herhangi bir fixup a yer yoktur yani Microsoft Macro Assembler el kitabında açıklanan giriş şartlarını ele almalıdırlar.Düşüm tamamlanınca veri dosyasını bir .com genişletme ile yeniden adlandırabilirsiniz. Böylece komut işlem birimi MS\_DOS diskinizde verilen .com programları çalıştıracaktır.

**EXIT**

**Çıkış**

Amaç : Command.com programını çıkartarak, (eğer varsa) bir önceki seviyeye geri dönüş

yapar.

Dizilim : exit

Şayet MS-DOS command programını yeni bir komut işleyiciyi çalıştırmak için kullanırsanız, exit komutunu da eski komut işleyiciye geri dönmek için kullanabilirsiniz. Aynı şekilde, bir aplikasyon programını işletirken, MS-DOS komut işleyicisini çıkartabilir, ve programınıza geri dönebilirsiniz.

Örnek :

exit ↵

**EXPAND**

Amaç : Sıkıştırılmış bir MS-DOS 5.00 dosyasını çözer.

Dizilim : expand\[sürücü:\]\\dizinadı\\dosyaadı1\[sürücü:\]\\dizinadı\\dosyaadı2

Ms-DOS programları daha az yer tutması için, orijinal disketlere sıkıştırılmış olarak kopyalanmıştır. Sıkıştırılmış dosyalar çalıştırılamayacağı için, bunları çözmek gereklidir.

Install programı ile MS-DOS’u kurarken, program dosyaları otomatik olarak çözülürler. Dosyaları tek tek çözüp kullanmak isterseniz veya bir dosya kazara diskten silindiğinde EXPAND komutunu kullanarak, orijinal MS-DOS disketinden programı çözmek gerekir.

Bir dosyanın sıkıştırılmış olduğunu dosya uzantısına bakarak anlayabilirsiniz. Sıkıştırılmış dosya isminin uzantısı “\_” karakteri ile biter. Bu dosyalardan bir kaçını aşağıda görüyorsunuz:

Sıkıştırılmış dosya Çözülmüş dosya

DOSSHELL.CO\_ DOSSHELL.COM

EDLIN.EX\_ EDLIN.EXE

KEYBOARD.SY\_ KEYBOARD.SYS

EGAMONO.GR\_ EGAMONO.GRB

MONO\_IN\_ MONO.INI

VGA.VI\_ VGA.VID

QBASIC.HL\_ QBASIC.HLP

GORILLA.BA\_ GORILLA.BAS

Şimdi bu dosyaların nasıl çözüleceğini örnekleyelim.

Örnekler:

expand a:\\dosshell.co\_ c:\\dos\\dosshell.com

expand a:\\keyboard.sy\_ c:\\dos\\keyboard.sys

expand a:\\gorilla.ba\_ c:\\dos\\gorilla.bas

**FASTOPEN**

Amaç : Sık sık kullanılan dosya ve dosya listelerini açmak için gereken zamanı azaltır.

Dizilim : fastopen\[sürücü:\[=n\]\[.....\]\]/x

veya

fastopen\[sürücü:\[=(n,m)\]\[....\]\]/x

veya

fastopen\[sürücü:\[=(\[n\],m)\]\[....\]\]/x

n, fastopen’in çalışacağı dosya sayısını belirtir. 10 ile 999 arasındadır.

m, belirlenen sürücüdeki dosyalar için dosya genişletme girdilerinin sayısıdır. Eğer

çıkarılırsa, bu özellik sağlanamaz. 1 ile 999 arasında değişir.

Fastopen, hızlı giriş yapmak için bir disk üzerindeki dosya ve dosya listesinin durumunu izler.Karmaşık bir dosya yapısı içerisine giriş yapmak zaman alıcı olabilir. Birkaç dosya kullanan aplikasyonlarla işlem görüyorsanız (database aplikasyonu gibi) dosyaları açmak ve kapamak için geçen zaman bilgisayarınızın performansı dikkate değer bir ölçüde düşecektir. Bir dosya veya dizinin her açılışında, fastopen bunun adını be konumunu kaydeder. Fastopen ayrıca, dosyanın o sürücü üzerindekifiziki konumunun bir haritasını da çıkartır. Bundan sonra, fastopenin kayıt etmiş olduğu bir dosya veya dizin adı yeniden açılacak olursa, giriş süresi oldukça daha az olacaktır. Fastopen, sadece hard disklerle çalışır, network üzerinde çalışmaz. Bir fastopen’i bir defada azami dört hard disk ile kullanabilirsiniz. Her bir hard disk için, fastopen, n dosya ve dizinleri inceleyecektir, burada n, 10 da+ 999’a kadar değişebilir. Bu değer verilmezse 10 kabul edilir.

/x parametresi, cache’in (LIM 4.0) genişletilmiş hafıza içerisinde olduğunu gösterir. Bu

parametre ile aynı iyi neticeyi almak için, select komutunun varsayılan değerini

kullanınız.

Fastopen komutunu sadece bir kez çağırabilirsiniz. Şayet fastopen ayarını değiştirmek isterseniz, yeniden ayarladıktan sonra makineyi kapatıp açınız.

Fastopen izlediği her dosya (n) için yaklaşık 48 byte’lık ve her dosya genişletme girdisi için (m) 16 byte’lık hafıza gerektiri.

Örnek:

Fastopen c:=100 ↵

Yukarıdaki komutu verdiğinizde MS-DOS 100 adete kadar dosyanın konumunu izler.

**FC**

**Dosya Karşılaştırma******

Amaç : İki dosya veya iki dosya setini karşılaştırarak farkları ekranda gösterir.

Dizilim : ASCII karşılaştırmaları için:

Fc\[/a\]\[/c\]\[/L\]\[/Lb*n*\]\[/n\]\[/t\]\[/w\]\[/*nnn*\]\[sürücü\]\\dizinadı\\dosyaadı1\[sürücü:\]\\dizinadı

\\dosyaadı2

Binary karşılaştırmaları için:

fc\[/b\]\[/*nnn*\]\[sürücü:\]\\dizinadı\\dosyaadı1\[sürücü:\]\\dizinadı\\dosyaadı2

\\dizinadı\\dosyaadı1 karşılaştırmak istediğiniz birinci dosya,

\\dizinadı\\dosyaadı2 karşılaştırmak istediğiniz ikinci dosyadır.

Fc komutunun anahtarları

/a Bir ASCII karşılaştırmasının verisini kısaltır. Farklılık gösteren tüm satırları ekranda

göstermek yerine fc sadece her farklılık setinin başladığı ve bittiği satırları gösterir.

/b Her iki dosya arasında binary karşılaştırmasını zorlar. Fc, iki dosyayı herhangi bir

uyumsuzluk tespit ettiğindebunu eşitlemek, yani aralarında uygunluğu temin etmeye

çalışmaksızın byte-byte karşılaştırmasını yapar. Bu uyumsuzluklar şu şekilde yazılır:

xxxxxxxx: yy zz

Burada, xxxxxxxx byte çiftlerin dosyasının başlangıcındanalınan ilgili adreslerdir.

Adresler 00000000’de başlar; yy ve zz sıara ile \\dizinadı\\dosyaadı1 ile

\\dizinadı\\dosyaadı2 deki uyumsuzluk gösteren byte’lardır. /b parametresi .exe, .com,

.sys, .obj, .lib veya .bin dosyalarını karşılaştırırken kullanılır.

/c Denkleştirme işleminin harflerinin durumlarına önem vermemesini sağlar. Bundan

sonra fc, dosyalardaki tüm farfleri büyükharf karakteri olarak ele alır.

/L ASCII modundaki dosyaları karşılaştırır. Bu parametre, .exe, .com, .sys, .obj, .lib veya

.bin uzantısına sahip olmayan dosyaları larşılaştırırken kullanılır.

/Lb Dahili satır buffer’ini n satırlarına yerleştirir. Dahili buffer’in varsayılan uzunluğu 100

satırdır. Bundan daha fazla ardıl, farklılıklar arzeden satıra sahip olan dosyalarda bu

karşılaştırma yapılmayacaktır.

/n Bir ASCII karşılaştırması üzerinde satır numaralarını gösterir.

/t Tabları ve boşlukları genişletmez. Başka bir değer vermezseniz, her tab 8 boş karakter olarak tanımlanır.

/w Karşılaştırma esnasında fc’nin boş karaktere (tablar ve boşluklar) basmasını sağlar. Şayet bir satır, herhangi bir sırada bir sürü tab ve boşluklar ihtiva etmiyorsa, bu karakterler tek bir boş karakter gibi kabul edilir. Dikkat ediniz, fc boş karaktere baskı yapmakla beraber, boş karakteri görmemekte değildir. Buna iki istisna, boş karakterlerin bir satırda başlangıcı ve bitişidir, ki bunlar da önemsenmez.

/*nnn* fc nin dosyalar arasında bir farklılık bulunmasından sonra eşitlenmesi gereken satırların sayısını belirtir. Dosyalarda eşlenen satırların sayısı bu rakamdan daha fazla ise fc eşlenen satırları farklılıklar olarak ekranda gösterir.

**Fc farklılıkları nasıl rapor eder ?******

Fc, iki dosya arasındaki farklılıklarıi önce dosya adını ekranda vererek, sonra dosyalar arasında farklılıkları gösteren satırları ve sonra da her iki dosyada eşlenen ilk satırı verir.

Dosyalar arasındaki eşlenecek satırların sayısı için varsayılan değer 2 dir. Şayet bu değeri değiştirmek istiyorsanız, satır sayısını /nnn ile belirtiniz.

Örnekler

fc /a fiyat.txt yenifiat.txt ↵

fc /b mg.exe mp.exe ↵

**FDISK**

**Hard Diski Hazırlama**

Amaç : Bir hard diskin MS-DOS’ta kullanmak üzere düzenlenmesi

Dizilim . fdisk

Hard diskler, bölme adı verilen 1 veya 4 ayrı kısma ayrılabilirler. Bölmeler de hard diski bireysel alanlara ayırırlar ve her bir bölme değişik birer işletim sistemi içerebilirler.

Hard diskinizi MS-DOS işletim sistemi için hazırlamak için, DOS bölmesi adı altında bir bölme yaratmalısınız. Fdisk programı yardımıyla DOS bölmesi yaratılabilir. Eğer aşağıdakilerden herhangi birini gerçekleştirmek istiyorsanız, fdisk’i kullanmalısınız:

Başlangıç DOS bölmesi yaratmak

Genişletilmiş DOS bölmesi yaratmak

Lojik DOS sürücüsü yaratmak

Aktif bölme belirlemek

Bir DOS bölmesini ya da lojik sürücüyü silmek

Bölme hakkında bilgi almak

Bilgisayar üzerinde başka bir hard diskin konfigürasyonunu tekrar etmek ya da değiştirmek.

Fdisk hard diskte var olan tüm dosyaların silinmesine yol açar.

**Fdisk’i Çalıştırmak******

Üzerine fdisk.exe bulunan disketi A sürücüsüne takıp, bilgisayarınızı çalıştırın. Fdisk yazıp enter tuşuna basın. Fdisk ana menüsü karşınıza gelecektir (bir hard disk varsa 5. seçenek görüntülenmez):

Disk Options

Current fixed disk drive: 1

Choose one of the following:

Create DOS Partition or Logical DOS drive

Set Active Partition

Delete DOS Partition or Logical DOS drive

Display Partition Data

Sellect Next Fixed Disk Drive

Enter choice: \[1\]

Press ESC to return to DOS

Fdisk’ten çıkmak için veya alt menüden ana menüye dönmek için Esc tuşuna basınız.

**Create DOS Partition or Logical DOS drive**

**Dos Bölmesi Yaratmak**

Eğer ana menünün ilk seçeneğini tercih ettiyseniz ve hard diskiniz tamamiyle bölmelere ayrılmışsa, fdisk aşağıdaki menüyü ekrana getirir. Eğer hiçbir genişletilmiş bölme yoksa, üçüncü seçenek görüntüye gelmez:

Create DOS Partition

Current fixed disk drive: 1

Create Primary DOS Partition

Create Extended DOS Partition

Create Logical DOS Drive(s) in the Extended DOS Partition

Enter choice \[1\]

Press Esc to return to Fdisk Options

**Create Primary DOS Partition**

**Başlangıç DOS Bölmesi Yarat******

Genişletilmiş MS-DOS bölmeleri yaratmadan önce, ilk olarak bir başlangıç DOS bölmesi yaratmanız gereklidir. Birçok durumda, tüm diskiniz için sadece bir MS-DOS bölmesine ihtiyaç duyacaksınız.

Başlangıç DOS bölmesi yaratmak için, tercih edeceğiniz seçeneği gösteren bölümde zaten 1 bulunduğu için sadece ENTER’a basın.

Bir sonraki menü başlangıç DOS bölmesi yaratma işlemi içindir:

Create Primary DOS Partition

Current fixed disk drive: 1

Do you wish to use the maximum size for a DOS partition and make the DOS partition active (Y/N)..............? \[Y\]

Press Esc to return to Fdisk Options

Tüm hard diskinizi MS-DOS için kullanmak istiyorsanız, fdisk programını bir kereye mahsus olmak üzere başlangıç MS-DOS bölmesi yaratmak için kullanacaksınız. Eğer ki tüm hard diskinizi (2 gigabyte’a kadar) MS-DOS için kullanacaksanız, görüntülenen tercih olan Y’yi (Evet anlamında) seçmek için ENTER’a basın.

Fdisk daha sonra aşağıdaki mesajı görüntüler:

System will now restart

Insert DOS diskette in drive A:

Press any key when ready.....

MS-DOS disketinizi A sürücüsüne takın ve MS-DOS’u tekarar çalıştırın.

Şimdi MS-DOS bölmenizi yaratmış bulunuyorsunuz, MS-DOS‘un kullanılabilmesi için bundan sonraki adım hard diski formatlamak olacaktır. Bunu format/s komutuyla gerçekleştirebilirsiniz. Format Komutunu okuyunuz.

Fdisk, subst veya join komutlarından sonra kullanılmaya çalışılırsa çalışmaz.

**FIND**

**Veri Arama******

Amaç : Bir dosyada veya dosyalarda belli bir grup karakteri aramak.

Dizilim : find\[/v\]\[/c\]\[/n\]\[/i\]”string”\[\[sürücü:\]\[\\dizinadı\\dosyaadı\]...\]

String aramak istediğiniz bir grup karakterdir.

Find, istenen dosyaları aradıktan sonra içerisinde istediğiniz karakterlerin bulunduğu satırları ekranda gösterir.

Eğer \\dizinadı\\dosyaadı’nı çıkartırsanız, find bu durumda bir filtre gibi davranacak, MS-DOS standart girdisinden okuyacak ve aranan karakterleri ihtiva eden satırları gösterecektir.

Find komutunun anahtarları:

/v Aranan karakterleri ihtiva etmeyen tüm satırları gösterir.

/c Dosyaların her birinde, bir uyum ihtiva eden satırların sayısını gösterir.

/n Her satırın önüne o satırın dosyadaki satır numarasını getirir.

/i Arama yaparken büyük harf ve küçük harf ayrımı yapmaz.

Örnek:

find “perakende fiyatı” fiyat.txt ↵

Fiyat.txt dosyasındaki perakende fiyatı yazan satırları gösterir.

**FORMAT**

Amaç : İstenen sürücü içerisindeki diski/disketi MS-DOS dosyalarını kabul edecek şekilde

düzenler.

Dizilim : format sürücü:\[/v\[:disketetiketi\]\]\[/q\]\[/u\]\[/f:disketkapasitesi\]\[/b:/s\]

veya

format sürücü:\[/v\[:disketetiketi\]\]\[/q\]\[/u\]\[/t:izler\]\[/n:sektörler\]\[/b:/s\]

veya

format sürücü:\[/v\[:disketetiketi\]\]\[/q\]\[/u\]\[/1\]\[/4\]\[/b:/s\]

veya

format sürücü:\[/q\]\[/u\]\[/1\]\[/4\]\[/8\]\[/b:/s\]

Yeni alınan bir disket/diskin kullanılabilmesi için formatlanması gerekir. Eski disketleri formatlarken disk üzerinde daha önceden bulunan bilgilerin silineceği unutulmamalıdır.

Format komutunun anahtarları:

/1 Floppy diskin tek yüzünü formatlar.

/4 Yüksek kapasiteli bir disk sürücüsü içindeki 5.25 inç, 360K, çift yüzlü bir disketi

formatlar

/8 Her iz’de 8 sektör formatlar

/b Diske, MS-DOS 5.0 işletim sistemini kopya edebilmek için geniş bir boşluk bırakarak

formatlar.

/f:disketkapasitesi Diketin formata göre büyüklüğünü belirler. Bu büyüklük şunlardan biri olabilir:

Disk tipi Büyüklük

160K tek yüzlü, 5.25 inç disk 160, 160K, 160KB

180K tek yüzlü, 5.25 inç disk 180, 180K, 180KB

320K çift yüzlü, 5.25 inç disk 320, 320K, 320KB

360K çift yüzlü, 5.25 inç disk 360, 360K, 360KB

1.2M çift yüzlü, yüksek kapasiteli, 5.25 inç disk 1200, 1200K, 1200KB,

1.2, 1.2M, 1.2MB

720K çift yüzlü, 3.5 inç disk 720, 720K, 720 KB

1.44M çift yüzlü, yüksek kapasiteli, 3.5 inç disk 1440, 1440K, 1440KB,

1.44, 1.44M, 1.44MB

2.88M çift yüzlü, yüksek kapasiteli,3.5 inç disk 2880, 2880K, 2880KB,

2.88, 2.88M, 2.88MB

/n:sektörler Her izdeki sektör sayısını belirler. Bu anahtar 3.5 inçlik bir diski belirlenen iz

sayısına kadar formatlar. 720kbyte diskler için bu değer 9 dur. (/n:9).

/q Çabuk format. Formatlama işlemini hızlandırır.

/s Varsayılan sürücüden, yeni formatlanan diske işletim sistemi dosyalarını kopya eder.

Eğer işletim sistemi çalışılan sürücüde değilse, format sizi uyararak çalışılan sürücüye

bir sistem diski koymanızı ister.

/t:izler Disk üzerinde iz sayısını belirler. Bu anahtar, 3.5 lik bir floppy diski belirlenen iz

sayısına kadar formatlar. 720Kbyte ve 1.44 megabyte diskler için bu değer 80 olmalıdır.

(/t:80).

/u Diskteki bilgilerin tamamı silinir. Unformat komutuyla diski kurtarmak mümkün değildir.

Unformat komutuna bakınız.

/v:disketetiketi Kullanılacak disk etiketini (herhangi bir isim verilebilir) belirler. Bu etiket diski

diğerlerinden ayırır ve 11 karakter uzunluğunda olabilir.

/n ve /t anahtarları /f anahtarı ile kullanılamaz.

Format komutu assign, join veya subst komutlarının kullanıldığı sürücülerle kullanmamalısınız, ayrı ayrıca sürücüleri de bir network üzerinden formatlayamazsınız.

**Bir Hard Diskin Formatlanması******

Hard diskiniz daha önceden formatlanmışsa ya da (yeni diskler için) fdisk komutu ile bölümlenmiş ise formatlama işlemine geçebilirsiniz.

Bir hard diski formatlarken, MS-DOS sizi, tüm bilgilerin silineceği konusunda uyarır.

*WARNING ALL DATA ON NON\_REMOVABLE DISK DRIVE X: WILL BE LOST*

*Proceed with Format (Y/N) ?*

DİKKAT, TÜM DATA HARD DİSK’TE SÜRÜCÜ X: KAYBOLACAK (Bilgiler silinecek)

Formata devam mı (Evet/Hayır) ?

Şayet hard diskinizi formatlamak istiyorsanız Y yazıp, ENTER tuşuna basınız. Hard diskinizi formatlamak istemiyorsanız, N yazıp ENTER tuşuna basınız.

Formatlama işlemi tamamlanınca, format, ekrana bir mesaj verir, bu mesajda toplam disk boşluğu, kusurlu olarak belirlenmiş herhangi bir yer, işletim sistemi tarafından kullanılmış topla yer (/s anahtarını kullandığınız zaman) ve dosyalarınız için kalan yer bildirilmektedir.

**Disket Formatlama******

format a:/s ↵

A sürücüsü içerisindeki bir disketi formatlamak için işletim sistemini buna kopya etmek için bu komut verilir.

format a: ↵

format a:/v ↵

A sürücüsü içerisindeki bir disketi, bilgi disketi olarak kullanmak için formatlamak isterseniz bu komutlardan birini yaznız.

format a:/4 ↵

format a:/4/v ↵

format a:/f360 ↵

Eğer disketiniz 360 Kb. Ve disket sürücünüz 1.2 Mb. İse komutu yukarıdaki gibi giriniz.

format a:/n:9/t:80 ↵

format a:/f:720 ↵

Eğer disketiniz 720 Kb. Ve disket sürücünüz 1.44 Mb ise komutu yukarıdaki gibi veriniz..

\*\*\* 360 Kb.’lik disketi 1.2 Mb.’a veya 720 Kb.’lik disketi 1.44 Mb.’a formatlamaya çalışmamalısınız. Formatlanmış gibi görünse de; o diskete kaydelilen bilgiler kolayca kaybolur.

**GRAFTABL**

Amaç : Harici karakter setinin grafik ekranda kullanılmasını sağlar.

Dizilim : graftabl\[xxx\]

veya

garftabl/status

xxx bir kod sayfası tanımlama numarasıdır.

Geçerli Kod sayfaları şunları içerir (xxx):

Değer kod sayfası

437 Birleşik Devletler (varsayılan değer)

Çok dilli (Latin I)

852 Slav (Latin II)

860 Portekizce

863 Kanada – Fransızca

İskandinav

/status\] Aktif karakter setini ekrana verir.

**GRAPHICS**

Amaç : Renkli veya grafik monitör adaptörü kullanılırken, bilgiyazara grafik ekranındaki görüntüyü yazdırmanızı sağlar.

Dizilim : graphics\[type\]\[\[sürücü:\]\[dizinadı\]\[dosyaadı\]\[/r\]\[/b\]\[/lcd\]\[/printbox:std:/printbox:lscd\]

Graphics komutu EGA ve VGA görüntü adaptörlerinin garfik görüntü modlarını

destekler.

Graphics komutunun anahtarları:

type Bilgiyazarın özelliklerini belirtir.

/p Renkli olarak zemini çizer

/r Printer üzerinde siyah veya beyaz yazar (Ekranda görüldüğü gibi). Varsayım, siyahı

beyaz ve beyazı da siyah gibi yazmak içindir.

/lcd CGA görüntü oranını kullanmak yerine LCD görüntü oranını kullanarak şekil çizer. Bu,

/printbox ifadesinin birinci operant (bilgisayarda kullanılan bilgi) ile eş olmalıdır.

/printbox:std:/printbox:lcd Yazıcı boyutunu seçer.

Ekrandaki printer’da yazmak için shift ve print screen tuşlarına aynı anda basmalısınız. Şayet bilgisayar 320x200 renkli modta ise ve printer’in tipi color1 veya graphics ise graphics ekrandakile dört gri tona kadar printer’a yazdıracaktır.

**HELP**

**Yardım******

Amaç : MS-DOS 5.0 versiyonu komutları hakkında online bilgi sağlar .

Dizilim : help\[komutadı\]

Komutadı Bilgi almak istediğiniz komutun adıdır. Eğer komut adı belirlemezseniz help komutu MS-DOS 5.0 versiyonundaki tüm komutları kısa açıklamaları ile birlikte listeler.

Komutlar için online yardım almanın iki yolu vardır. Komutun adını help komutu satırında belirleyebilirsiniz veya komutunun adı yazarak /? Tuşunu komutun yanına koyunuz.

Örnek:

Ağaıdaki komutlardan herhangi birini “dir” komutu hakkında bilgi almak için kullanabilirsiniz.

help dir

dir/?

**JOIN**

Amaç : Bir disk sürücüsünü belli bir dizin adına birleştirir.

Dizilim : join\[sürücü:sürücü:dizinadı\]

Veya

join sürücü:/d

Bir sürücüde bulunan boş bir dizini (dizin yoksa yeni bir dizin açılır) join komutu ile başka bir sürücüye bağlayabilrsiniz. Bu durumda bağladığınız dizini geçmek için komut verdiğinizde ikinci sürücüye geçersiniz. İkinci sürücünün adını yazdığınızda ise hata mesajı gelir.

Backup, chkdsk, diskcomp, diskcopy, fdisk, format, label, recover, restore ve sys komutları join kullanılan sürücüde kullanılamaz.

Örnekler:

Join a: c: \\yeni ↵

Bu komutu verdiğinizde hard diskte yeni adlı bir dizin varsa A sürücü ile birleşektir. Hard diskte böyle bir dizilim yoksa bu isimde bir dizin açılır.

İşlemi gerçekleştirdikten sonra cd\\yeni komutu verirseniz ekranda yeni dizine geçmiş gibi mesaj gelmesine rağmen A sürücüsünün ışığının yandığını görürsünüz. Gerçekte A sürücüsüne geçtiğiniz A: komutu verdiğinzde ise hata mesajı gelir.

join a: /d ↵

Bir önceki örnekte verilen komutun yaptığı işlemi iptal eder.

**KEYB**

**Klavye Değiştirme**

Amaç : Bir klavye programı yükler. Klavyede normalde bulunmayan karakterleri

kullanabilirsiniz.

Dizilim : \[*xx*\[,\[*yyy*\],\[sürücü:\[dizinadı\]dosyaadı\]\]\]\[/id:*nnn*\]

*xx* iki harfli ülke kodu,

*yyy* karakter setini belirleyen kod sayfası

*dosyaadı* klavye düzenleme dosyasının adıdır. Şayet belirtilmemişse kullanılan

dosyayı keyboard.sys dir.

/ID:*nnn* ise kullanılan klavyeyi belirtir.

xx Ülke yyy Kod Sayfası

be Belçika 120 437,850

cf Kanada – Fransız 058 863,850

df Danimarka 159 865,850

fr/120 Fransa 189/120 437,850

gr Almanya 129 437,850

it/142 İtalya 141/142 437,850

la Latin Amerika 171 437,850

nl Hollanda 143 437,850

no Norveç 155 865,850

po Portekiz 153 860,850

sf İsviçre, Fransız 150 437,850

sg İsviçre, Alman 000 437,850

sp İspanya 172 437,850

su Finlandiya 153 437,850

sv İsveç 153 437,850

uk/168 İngiltere 166/168 437,850

us Birleşik Amerika 103 437,850

Şayet herhangi bir seçenek kullanmadan kyb yazarsanız MS-DOS size aşağıda verdiğimize benzer bir mesaj vererek o andaki klavye kodunu, bununla ilgili kod sayfasını ve ekranınızın kullandığı kod sayfasını gösterir.

Current keyboard kod: uk kode page 437

Current cont kod page: 437

Klavye kodu : uk kodsayfası : 437

Ekran kod sayfası : 437

İstediğiniz zaman ctrl+alt+F1’e basarak keyb programının aktivitesini sonlandırabilirsiniz. Tekrar, ctrl+alt+F2’ye basmak suretiyle değiştirdiğiniz klavyeye dönebilirsiniz.

Keyb komutunu MS-DOS komutu satırında girebilir veya config.sys dosyasına, install komutuyla birlikte yazabilirsiniz.

\*\*\* IBM bilgisayarlarla birlikte verilen MS-DOS programları içinde türkçe klavye kullanmamıza izin veren kod sayfası dosyaları vardır. Bunların ismi “keyboarf.sys” (klavye) ve “keyboarq.sys” (türkçe q klavye) dir. Bu dosyaların birini “TR” anahtarları ile birlikte kullanabilirsiniz.

Örnek:

keyb tr,,\\dos\\keyboarf.sys ↵

Bir türkçe kullanıcıs için bu komutu yazınız.

**LABEL**

**Disk Etiketi******

Amaç : Bir disk üzerinde etiket yaratır, değiştirir veya bu etiketi siler.

Dizilim : label \[sürücü:\]\[disketiketi\]

Etiket, bir disk için seçebileceğiniz bir isimdir. Label, 11 karaktere kadar yeni bir etiket yazar.

MS-DOS, bir diskin etiketini size dizin listesinin başında göstererek hangi diski kullandığınızı açıklar.

Bir seri numarası varsa, label size bu sekiz karakterli numarayı da ekranda gösterir:

Volume serial Number in drive x is nnnn-nnnn

X sürücüsü içindeki seri numarası nnnn-nnnn’dir.

Şayet herhangi bir etiket seçmezseniz, label sizi şöyle bir mesajla uyaracaktır :

Volume in drive x is xxxxxxxxxxx

Volume serial Number is xxxx-xxxx

Volume label (11 characters, ENTER for none)?

X sürücüsü içindeki etiket xxxxxxxxxxx’dir.

Disk seri numarası xxxx-xxxx’dir

Disk etiketi (11 karakter, hiçbiri için ENTER)?

Disk etiketinin adlandırılması:

Bir etikette yan yana 11 karakter olabilir ve burada boşluklar da bulunabilir, ancak herhangi bir tab bulunamaz.

İstediğiniz ismi yazın ve ENTER tuşuna basınız. Şayet etiketi silmek istiyorsanız ENTER tuşuna basın. Label size şu mesajı gönderecektir:

Delete current volume label (Y/N)?

Mevcut disk etiketi silinecek mi (Evet/Hayır)?

Evet anlamında Y tuşuna basarsanız label disk üzerindeki disk etiketini silecektir. Aksi taktirde etiket aynı şekliyle kalır.

Label, subst veya join komutlarıyla ilgili sürücüler üzerinde çalışmaz.

Bir disk etiketinde aşağıdaki karakterlerden herhangi birini kullanmalıyız:

&()\*+,./:;?>=<\[\\\]^:

Örnek:

label a:YENIDISK ↵

**LINK******

Amaç : Obje haline getirilmiş dosyaları makine kodu formatına çevirerek icra edilebilir

program dosyaları (.EXE uzantılı dosyalar) haline getirir.

Dizilim : link

veya

link objedosya\[,\[exedosyaadı\]\[,\[mapdosyaadı\]\[,\[kütüphanedosya\]\]\]\]\[anahtar\]\[,\]

veya

link@dosya adı

Microsoft 8086 obje birleştiricisi yani bu bölümde sık sık tekrarlayacağımız ismiyle link programı microft macro assembler (MASM) veya herhangi bir yüksek seviyeye dil derleyicisi (c, pascal, clipper derleyicileri gibi) tarafından obje haline getirilmiş dosyaları makine kodu formatına çevirerek icra edilebilir program dosyaları (.exe uzantılı dosyalar) haline getirir.

Link orijinal kaynak dosyalarındaki komutları göz önüne alarak program kod ve verisini birleştirerek program dosyası yaratır. Program çalıştırıldığında bir birine yapıştırılmış segmentlerin oluşturduğu bu icra imajı direkt olarak belleğe kopyalanır. Program dosyasına kopylanan segmentlerin sırası, bunların belleğe aktarımındaki sırayı belirler.

Link’i kullanmak için bir veya birden fazla obje dosyasının yaratılmış olması ve bunların eğer ihtiyaç duyulmakta ise yine herhangi bir kütüphane veya dağarcık dosyası ile birlikte link programının bilgisi olarak belirtilmesi gerekmektedir. Obje dosyası kullanıcının yazmış olduğu sembolik programın bir derleyici tarafından kullanılan bilgisayar donanımının anlayabileceği komut formatına çevrilmiş obje kodunu içeren dosyadır. Kütüphane veya dağarcık dosyaları ise standart program modülleri içeren ve yazılımcının bu modülleri her defasında tekrar yazması yerine istendiğinde bu modülleri başka programlar bünyesinde kullanımı için oluşturulmuş bir nevi hazır obje kodu depolarıdır. Link’in özetle yaptığı ise obje dosyaları içindeki kod ve verinin birleştirilip dış referansların çözümlenmesi için kütüphane dosyalarının araştırılıp elde edilen icra komutları kümesinin bir dosya içine toplanmasıdır. MS-DOS bundan sonra bu dosya içindeki bilgilerden yararlanarak yazdığınız ve link ettiğiniz programınızı uygun bir adresten başlayarak belleğe yükleyecektir.

**Link’in Kullanımı:**

1. Link

Komut satırında link yazıp enter tuşuna bastığınızda aşağıdaki sorular size yöneltilir.

Object modules \[.obj\]:

Birden fazla obje dosya ismi belirtilirken her birinin arasına + koyun, obje dosyaları bir komut satırına sığmıyorsa alt satıra geçmeden önce son karakter olarak + bulunması gerekmektedir.

Rangfile \[dosyaadı.exe\]:

Bu soruda dosya adı ile belirtilen yerde ilk girdiğimiz obje modülünün ismi yer alır. Değiştirmek için yeni bir isim girebilir veya sadece entr’a basarak bu isim seçimini onaylayabilirsiniz.

Listfile \[nul.map\]:

Eğer istiyorsanız bu yolla .exe’nizin bir icra haritasını çıkartabilirsiniz. Harita veya liste dosyası yaratmak için her hangi bir isim girin aksi taktirde hiçbir şey yazmadan bu bölümü pas geçin.

Libraries \[.lip\]:

Burada da dosya isimlerinin verilmesi obje dosyalarının verilmesiyle aynı mantığa dayanır. Birden fazla kütüphane dosyası + ile bir birinden ayrılır. Eğer kütüphane dosyasına gerek duyulmuyorsa hiçbir şey yazmadan enter’la karşılığı pas geçilir. Bundan sonra link .exe dosyasını yaratacaktır.

Dosya ismi girişlerinin hiç birinde uzantı kullanmaya gerek yoktur. Eğer gireceğiniz dosya ismi başka bir dik sürücü veya başka bir dizin içinde ise dosyanın bulunduğu dizin adını belirtmelisiniz. En az bir obje modülü ismi vermek kaydıyla sorunların herhangi birinde noktalı virgül (;) ile karşılık verilmesi halinde link diğer soruları sormadan .exe’yi yaratır.

Örnek:

Link ↵

Object Modules \[.OBJ\]: krt1+krt2+krt3 ↵

Run File \[KRT1.EXE\]: Kartotext ↵

List File \[NUL.MAP\]: ↵

Libraries\[.LIB\]: c:\\lib\\clipper ↵

2. link objedosya(ları)\[,\[exedosyaadı\]\[,\[mapdosyaadı\]\[,\[kütüphanedosya(ları)\]\]\]\]\[anahtar(lar)\]\[,\]

objedosyaları Bir birine bağlayacağınız birden fazla olması halinde boşlulka bir birinden ayrılmış

olan dosya isimleri gurubudur.

exedosyaadı .EXE dosyasına (program dosyası) vereceğiniz isim için ayrılan yerdir.

mapdosyaadı Harita dosyanıza vereceğiniz isim için ayrılan yerdir. /map veya / linenumbers

anahtarlarının kullanımı halinde harita dosyası için bir isim girilmemiş olsa bile

Link bir harita dosyası yaratır.

kütüphanedosyaları Gerek duyulan, birden fazla olması halinde boşlukla biribirinden ayrılmış olan

kütüphane isimleri grubudur.

anahtar(lar) Link’in operasyonunu kontrol için sunulan seçeneklerdir. Bunları komut satırının

herhangi bir yerinde kullanabilirsiniz.

Obje dosyalarından sonra noktalı virgül kullanımı halinde .exe dosyanız ilk obje dosyasının ismini alır ve haritada dosyası yaratılmaz. Bu durumda kütüphane dosyasının ismi obje dosyası içinde belirtilmemişse veya kütüphane dosyası bulunamamışsa Link işleme ara verip kütüphane dosyasını sorar.

3. **Link@dosyaadı** dosya adı dosya isimlerini içeren bir dosyadır.

Link’e girilecek dosya isimlerini listesini içeren bir ASCII dosya yaratıp link komut satırında bu dosya ismini vererek her fırsatta uzun uzadıya komut satırından bilgi girişi külfetinden kurtulabilirsiniz. Link’in giriş bilgilerini istenilen dosyadan alması için dosya adının önüne (“@”) işaretinin konulması gereklidir. Eğer bu dosya başka bir sürücü veya dizinde ise dizin adını belirtmelisiniz. Bu dosyanın içeriği şöyle olmalıdır:

objedosyaları

\[exedosyaadı\]

\[mapdosyaadı\]

\[kütüphanedosyaları\]

Köşeli parantez içindekilerin bu dosya içinde yer alması isteğe bağlıdır. Bir satıra sığamayacak kadar dosya ismi belirtiyorsanız bir sonraki satıra geçmeden önce + karakterini son karakter olarak yazmayı ihmal etmeyiniz. Obje dosyalarından sonra noktalı virgülün kullanımı (”;”) bir önceki dosya ismi girişi ve metodundaki sonucu doğuracaktır. Yani .exe’nin ismi ilk obje dosyasının ismi olurken harita dosyası yaratılmayacaktır.

Örnek:

toplam.lnk dosyasını aşağıdaki gibi kullanırız:

link@toplam.lnk ↵

Object Modules \[.OBJ\]: KRT1 +

Object Modules \[.OBJ\]: KRT2 +

Object Modules \[.OBJ\]: KRT3

Run File \[KRT1.EXE\]: KART

Map File \[NUL.MAP\]:

Libraries \[.LIB\]: C:\\LIB\\CLIPPER

Link programının anahtarları:

/help veya /he

Link tarafından geçerli kabul edilen anahtarların listesini verir. Bu anahtar kullanılırken komut satırında dosya ismi belirtilmemelidir.

/pause veya /p

Bu anahtar link’in .exe’yi yaratmadan önce ara verip size çalıştığınız sürücüdeki disketleri değiştirme olanağı vermesini sağlar. Program dosyası yaratılmadan hemen önce aşağıdaki mesaj verilir

About the generate .exe file

Change dikette in drive x: and press <ENTER>

Bu mesajdan sonra x: sürücüsündeki disketi değiştirip, ENTER tuşuna basın. Oluşturulan .EXE dosyası bu yeni diskete yazılır ve işlem sonunda ilk disketin sürücüye tekrar takılması istenir.

Please replace original diskette in drive x: and press <ENTER>

/exepack veya /e

Bu anahtar, oluşturulacak icra dosyasını, birbiri ardına tekrarlanan 0 baytları yok ederek, minimum boya indirger. Aynı zamanda, icra dosyasının yükleme-zamanı tablosunu optimum şekilde düzenleyerek, ilerde maksimum hızda programın belleğe yüklenmesini sağlar. Bu anahtar her zaman için disk yüzeyinden tasarruf etmeyebilir, bazen dosyaların boyu daha büyük olabilir. Diskten tasarruf edilebilmesi için üretilen dosyada uzun uzadıya birbiri ardına tekrar edilen baytların olması öngörülmektedir.

/map veya /m

Bu anahtar ise, oluşturulacak harita dosyasına program içindeki tüm tüzel sembollerin bir listesinin dahil edilmesini sağlar.

/linenumbers veya /li

Bu anahtar, harita dosyasına kaynak program kodundaki her satırın başlangıç adreslerini kopyalar. Bu adresler aslında kaynak program komutundaki her satırın ilk makine komutu adresleridir.

/noignorecase veya /noi

Bu anahtar, sembol isimlerinde büyük/küçük harf ayrımını yapar.

/nodefaultlibrarysearch veya /nod

Bu anahtarla, daha önce obje modüllerin içine dahil edilmiş olan kütüphane isimlerine ait bilgileri görmemezlikten gelebilir, Link!i sadece komut satırında belirtilen dizinlerde kütüphane aramaya yöneltebilirsiniz.

/stack:boy veya /st:boy

Bu anahtarla, boy parametresiyle verilen sayıda bayt kadar program için yığın yaratabilirsiniz. Program esnasında bir alt program, fonksiyon veya prosedürden bir diğerine dallanırken, dönüş adresi ve dallanılan programın kullanacağı değişkenler bayt uzunlukları kadar yığına basılır ve alt program işlemi için muhafaza edilmiş olur. Bunu göz önüne alarak programınızın ihtiyacını karşılayacak şekilde yığın büyüklüğünü belirleyebilirsiniz. Boy için verilen değer onluk, sekizlik veya onlatılık düzende verilebilir.

Örnekler

Link dosya /stack:512..: ↵ yığın boyu 512 bayt.

Link dosya /stack:0xFF..: ↵ yığın boyu 255 bayt (FFh).

Link dosya /st:30...: ↵ yığın boyu 24 bayt (8’lik düzende gösterim).

/cparmaxalloc:sayı veya /c:sayı

Bu anahtarla programın belleğe yüklenirken gerek duyulacak olan 16 baytlık maksimim paragraf sayısını belirleyebilirsiniz. DOS bu sayı ile belirtilen bellek alanını programın yüklenmesi için tahsis eder. Link normal olarak maksimum paragraf sayısı olarak 65535’i belirler eğer bellekte bu büyüklükte bir alan yoksa bulunabildiği en uzun kesintisiz bellek bloğunu yükleme işlemi olarak kullanır. Bu alanı kontrol ederek bellekte diğer programlara da yer açabilirsiniz.

Örnekler:

Link dosya /c:15...: ↵ 15 paragraf tahsis edilir.

Link dosya /cparmaxalloc:0xff...: ↵ 255 paragraf tahsis edilir (FFh).

Link dosya /c:030..: ↵ 24 paragraf tahsis edilir (8’lik düzende gösterim).

/high veya /h

Bu anahtar programın başlangıç adresini kullanılmayan bellek alanındaki en yüksek adres olarak belirler. Aksi halde Link başlangıç adresi olarak en alçak adresi belirleyecektir.

/dsallocate veya /d

Bu anahtar, programın DGROUP’u (veri grubu) içindeki ilk baytı en yüksek ofsete koyar, yani normalde DGROUP’un ilk baytı data segmentinin ilk ofsetinden başlarken veri baytları segmentin sonundan başa doğru gider.

/overlayinterrupt veya /s:sayı

Bu anahtar, overlay yükleme modülünün kesme numarasını sayı olarak belirler. Normalde bu anahtar kullanılmaksızın bu değer 3Fh’dır. Bu anahtar, overlay kullanımını sağlayan derleyiciler tarafından yaratılmış obje modülleri ile kullanılmalıdır.

/segments:sayı veya /se:sayı

Link’in program başına ayıracağı bölüm sayısı 128’dir. Eğer programınız bu sayıdan fazlasını kullanıyorsa bu anahtarla üst bölüm sayısı sınırını belirleyebilirsiniz. Bu sayıyı yine onluk, onaltılık ve sekizlik düzende gösterebilirsiniz.

/dosseg veya /do

Bu anahtarla, Link icra programı içindeki tüm bölümleri MS-DOS segment-sıralamasına göre düzenler. Bu sözü edilen sıralama şöyledir:

- CODE sınıfındaki tüm segmentler veya bölümleri icra programının en başına yerleştirir.

- DGROUP’a ait olmayanlar CODE’dan sonra yer alır.

- Dosya sonuna DGROUP üyeleri yerleştirilir.

**LOADFIX******

Amaç : 64 Kb’tan büyük programların çalışmasını sağlar.

Dizilim : loadfix\[sürücü:\]\[dizinadı\]dosyaadı

\[sürücü:\]\[dizinadı\]dosyaadı çalıştırılacak programın bulunduğu yer ve program

dosyasının adıdır.

Örnek:

“MUHASEBE.EXE” isimli bir programımız olduğunu varsayalım.

Programı çalıştırmak için aşağıdaki komutu yazalım:

Muhasebe ↵

Programımız çalışırsa sorun yok. Eğer çalışmazsa ve “Packed file corrupt” diye bir mesajla karşılaşırsak komutu aşağıdaki şekilde vermemiz gerekir:

loadfixmuhasebe ↵

**LOADHIGH**

**LH**

Amaç : Bir programı üst hafızaya (upper memory) yüklemek için kullanılır. Böylece diğer

programları çalıştırmak için daha fazla yer kalır.

Dizilim : lh\[sürücü:\]\[dizinadı\]dosyaadı\[parametreler\]

veya

loadhigh\[sürücü:\]\[dizinadı\]dosyaadı\[parametreler\]

Parametreler yüklenen program için gerekli anahtar bilgileri içerir.

Bu komutu kullanabilmemiz için üst hafızayı yönetecek bir programı önceden yüklemiş olmanız gerekmektedir. MS-DOS bu işlem için EMM386.EXE komutu kullanır. Ayrıca EMM386.EXE’yi kurmadan önce HIMEM.SYS sistemini kurmuş ve CONFIG.SYS dosyasını buna göre değiştirmiş olmanız gerekmektedir.

LOADHIGH komutu genellikle klavye düzenleyici, ekrana font yükleyen programlar, doskye, hesap makinesi programlarımı gibi memoryde sürekli yer işgal eden programları üst hafızaya yüklemek için kullanılır. Diğer uygulama programlarını üst hafızaya yüklemeye çalışmamalıdır.

Örnek:

lh doskey ↵

**MEM**

**Hafıza Gösterme******

Amaç : Kullanılan ve geriye kalan boş hafızayı ekranda gösterir. Yerleştirme yapılan

bölgelerin, serbest bölgelerin ve yüklenen programların listesini yapar.

Dizilim : mem\[/program\]

veya

mem\[/debug\]

veya

mem\[/classify\]

/program Hafızaya yüklenen programları ekranda gösterir.

/debug Programları, dahili sürücüleri ve diğer program bilgilerini verir.

/classify Yüklenen programların hafızadaki durumları hakkında bilgi verir.

Örnek:

mem /program ↵

Veri aşağıdaki dökümün benzeri olacaktır.

Adres İsim Uzunluk Tip

Address Name Size Type

000000 000400 Interput Vector

000400 000100 ROM Communication Area

000500 000200 DOS Communication Area

000700 I0 000030 System Data

001330 MSDOS 0013D0 System Data

002700 I0 0075F0 System Data

HIMEM 000470 DEVICE=

SMARTDRV 005F40 DEVICE=

0005D0 FILES=

000100 FCBS=

000200 BUFFERS=

000100 LASTDRIVE=

000740 STACKS=

009D00 MSDOS 000040 System Program

009D50 COMMAND 000940 Program

00A6A0 MSDOS 000040 -- Free --

00A6F0 COMMAND 000100 Environment

00A800 MSDOS 000090 -- Free --

00CCE0 DOSKEY 001020 Program

0101C0 MEM 0000E0 Environment

0102B0 MEM 0176F0 Program

0279B0 MSDOS 077A40 -- Free --

655360 bytes total conventional memory

652288 bytes available to MS-DOS

586048 largest executable program size

1310720 bytes total contigous exended memory

bytes available contiguous extended memory

196608 bytes available XMS memory

**MIRROR**

Amaç :Bir veya birden fazla disk bilgisini daha sonra unformat ve undelete komutlarının kullanabilmesi için kaydeder. Unformat komutu formatlanmış bir disketi undelete komutu ise del komutu ile silinmiş dosyaları kurtarmak için kullanılırlar

Dizilim ** mirror**\[sürücü:\[...\]\]\[/1\]\[/tsürücü\[-girişler\]\[...\]\]

**Mirror\[/u\]**

** Mirror\[partn\]**

O anki disket bilgilerini yazdırmak için sadece mirror komutu yeterlidir.

Mirror komutunun anahtarları:

/1 Disk hakkındaki en son bilgileri kullanır

/tsürücüsü\[-girişler\] Undelete komutu tarafından kullanılmak üzere belirtilen disk hakkındaki bilgileri kaydeder.Girişler bölümüne istenirse 1’den 999’a kadar bir sayı girilerek disk bilgileri dosyanın büyüklüğü sınırlandırılabilir.

Bir drğer verilmemesi halinde disk tipine göre aşağıdaki değerler hazır olarak kabul edilir.

Disk büyüklüğü Girişler Dosya büyüklüğü

360 K 25 5 K

720 K 50 9 K

1,2 MB 75 14 K

1,44 MB 75 14 K

20 MB 101 18 K

32 MB 202 36 K

>32 MB 303 55 K

/u /t anahtarının işlevini iptal eder.

/partn Harddiskin dosya bilgilerini diskete yazar

Örnek

Mirror a: ↵

Diskette kayıtlı dosyalar hakkındaki kurtarma bilgileri “MİRROR.FIL”isimli dosyaya yazılır.

**MKDIR**

**MD**

**Dizin Yaratma**

Amaç :Yeni bir dizin yaratır.

Dizilim :mkdir\[sürücü:\]dizinadı

Veya

Md\[sürücü:\]dizinadı

Mkdir sayesinde çok seyiyeli bir dizin yapısı kurabilirsiniz

Örnekler:

Md\\musteri ↵

Ana dizini altında musteri adlı bir dizin yaratır

Md\\musteri\\borclu ↵

Musteri dizini altında borclu adlı bir dizin yaratır

Cd\\musteri\\borclu ↵

Sonra

Md bocrlu ↵

Musteri dizinine geçtikten sonra md komutunu kuldandığımızda yine musteri dizini altında borclu adlı bir dizin yaratır.

**MODE**

**Mode değiştirme**

Amaç :mode komutu birkaç farklı amaç için kullanılır.

Tüm ünitelerin veya tek bir ünitenin durumunu ekranda göstermek için.

Paralel porta bağlı bir bilgiyazarı (PRN,LPT1,LPT2 veya LPT3) her satırda 80 veya 132 karakter, her inçte 6 veya 8 satır yada her ikisini birden yazacak şekilde düzenler. Başka bir görüntü seçmek için veya kullandığımız görüntü düzenini değiştirmek için kullanılır.görüntü düzeninin değiştirilmesi derken , 40 sütun ile 80 sütun arasında bir görüntü seçilmesi siyah- beyaz ya da renkli bir görüntü seçilmesi görülen satır sayısının değiştirilmesi görüntünün bir ekrana veya bunların herhangi bir kombinasyonuna odaklanmasını anlıyoruz .klavyenin yazma hızının ayarlar.

Kod sayfa dönüştürme için kullanılan üniteleri hazırlar.

Bilgiyazar verisin parelel bir porttan seri portlardan birine gönderir böylece seri port sistemin geçerli bilgiyazar portu haline getirir.

Mode komutunun bu kullanımlardan her biri için ayrı bir dizilimi olduğundan aşağıdaki bölümde bunları tek tek açıklıyoruz.

Notlar:

Klavyenin veya görüntü modunun ayarlanması gibi bazı fonksiyonlar ancak ansi.sys sürücüsünün config.sys dosyasına yerleştirilmesi durumunda işletilebilir.

Mode komutu ile yaptığınız değişikliklerin sürekli olarak aktif olmasını istiyorsak bilgisayarı her açışta tekrar aynı işlemleri yapmamak için autoexec.bat dosyası içine yerleştirmekte fayda vardır.

**Ünitelerin durumu******

Amaç :Ünitelerin durumunu ekranda gösterir.

Dizilim mode\[ünite\]\[/status\]

veya

** **mode

Mode komutunun kendisini yazmakla ekranda sisteminize takılı olan tüm üniteleri görebilirsiniz

/status anhtarı sadece paralel bilgiyazarın durmlarını isterken kullanılır

Örnek:

Mode con ↵

**Bilgiyazarın düzenlenmesi******

Amaç :paralel bilgiyazar portuna (LPT1,LPT2 veya LPT3)bağlı bilgiyazarların özelliklerini ayarlar

Dizilim :mode LPTn\[:\]\[c\]\[,\[l\]\[,r\]\]

Veya

Mode LPTn(cols=c)(line=l)(retry=r\]

Paralel bilgiyazar modları için PRN veya LPT1’i değişimli olarak kullanabilirsiniz. Mode komutu ile paralel bir bilgiyazar için parametreleri tespit etmek için şu seçenekleri kullanabilirsiniz.

n Bilgiyazar numarasını belirler:1,2 veya 3

c Her saturda olacak karakterleri belirler:80 veya 132

l Dikey yerleştirme ve her inçteki satırları belirler:6 veya 8

r Zaman dolma hataları olduğu zaman yapılacak retry hareketini belirler.Bu seçenek mode programının bir kısmının hafızada kalmasına tol açar.Şayet mode komutunu bir network üzerinde kullanıyorsanız sürekli retry için r seçeneğini kullanmayınız.

Muhtemel değerler şöyledir:

E Meşgul bir portun durum kontrolünden hatayı verir

B Meşgul bir portun durum kontrolünden meşgul verir

R Meşgul bir portun durum kontrolünden hazır verir

NONE Herhangi bir retry hareketinin yapılmadığını gösterir

Mode komutu kullanılmadığı durumda kabul edilen değerler :bilgiyazar portu LPT1, her satırda 80 karakter ve her inçte 6 satır’dır.

Örnekler:

mode lpt2: 132, 8 ↵

mode lpt2: ,8 ↵

**Seri port’un Düzenlenmesi**

Amaç :Seri haberleşme port’unun düzenlenmesini kontrol eder.

Dizilim :mode COMm\]:\]b,\[,p\[,d\[,s\[,r\]\]\]\]

veya

modeCOMmbaud=b\[data=d\]\[stop=s\]\[parity=p\]\[retry=r\]

Seri port parametrelerini ayarlamak için mode komutu ile aşağıdaki seçenekleri kullanabilirsiniz:

m Asenkron haberleşme (COM) port numarasını belirler.

b İletim hızının ilk iki digitini belirler:110,150,300,600,1200,2400,4800,9600, veya 19,200

p Eşleelerin belirler:N(hiç) , O(anlamsız) , E(az) , M(işaret) , S(yer).Varsayılan değer E dir

d Data bitlerinin sayısını belirler.5,6,7 veya 8.

s Durma bitlerinin sayısını belirler:1,1.5 veya 2. Şayet baud oranı 110 ise kabul edilen değer 2’dir aksi taktirde kabul edilen değer 1’dir

r Ne tür bir retry hareketinin alınacağını belirler. Şayet mode komutunu bir network üzerinde kullanıyorsanız devamlı retry için r seçeneğini kullanmayınız.

Seçenekler şunlardır:

E E Meşgul bir portun durum kontrolünden hatayı verir

B Meşgul bir portun durum kontrolünden meşgul verir

R Meşgul bir portun durum kontrolünden hazır verir

NONE Herhangi bir retry hareketinin allınmadığını belirtir

**Görüntü modunun ayarlanması**

Amaç : Aktiv video adaptörünü ve onun görüntü şeklini seçerek kullandığınız ekranı düzenler.

Dizilim : mode display, n

veya

mode\[display\],shift\[,test\]

veya

mode con\[:\]\[cols=c\]\[lines=\]

Parametreleri görüntü için ayarlarken mode komutu ile şu seçenekleri kullanabilirsiniz.

display Şu değerlerden birini belirler : 40, 80, BW40, BW80, CO40, CO80 veya MONO.

40 ve 80 rakamları her satırdaki karakter sayısını belirler.

BW ve CO ise renkli grafik monitörün adaptörünü belirtir, BW siyah\_beyaz ve CO ise

renklidir.

MONO ise her satırda 80 karakter genişliğe sahip devamlı bir görüntüsü olan

monokrom bir görüntü adaptörünü belirtir.

shift Renkli bir Grafik Adaptör /CGA) görüntünün sağa ya da sola çevrilmesini belirtir.

Burada geçerli değerler, sol için L ve sağ için R dir.

n Görüntü üzerinde satırların sayısını belirler. Muhtemel değerler 25, 43 ve 50 dir. Tüm

adaptörler bütün bu hacimleri desteklemez.

c Her satırdaki karakterlerin sayısını belirler. Muhtemel değerler 40 veya 80 dir.

test Görüntüyü sıraya dizmenizi sağlar. Ayrıca ekranın doğru bir şekilde sıraya dizilip

dizilmediğini de bildirir.

**Klavye Modunun Ayarlanması******

Amaç : Klavye yazım hızını düzenler.

Dizilim : mode con\[:\]\[rate=r delay=d\]

Yazım hızını düzenlemek için, hem hızı hem de gecikmeyi aynı anda seçmelisiniz.

r Yazım ara zamanını belirler. Muhtemel değerler 1 ile 32 arasındadır.

d Kendi kendine tekrar başlangıç gecikme zamanını belirler. Muhtemel değerler 1 ile 4 tür

(etkin değerler .25, .50, .75 ve 1 saniyedir).

**Ekran Kod Sayfalarının Ayaralanması******

Amaç : Kod sayfalarını konsolunuz veya paralel bilgiyazarlar için yerleştirir ve ekrana verir.

Dizilim : mode ünite codepage prepare=((yyy)\[sürücü:\]\[dizinadı\]dosyaadı)

mode ünite codepageselect=yyy

mode ünite codepage refresh

mode ünite codepage\[/stasus\]

ünite Kod sayfasını parametrelerken bunu destekleyecek üniteyi belirler. Geçerli ünite isimleri

CON, LPT1, LPT2 ve LPT3 tür.

yyy Bir kod sayfasını belirler. Geçerleri kod sayfaları 437, 850, 860, 863 ve 865’tir.

dosyaadı MS-DOS’un belirlenen ünite için bir kod sayfası hazırlamakta kullanıldığı kod sayfası

bilgi (CPI) dosyasının adını tanımlar.

mode ünite codepage komutu ile kullanabileceğiniz 4 kelime vardır. Bunların her biri mode komutunun farklı bir işlem yapmasını sağlar. Aşağıda bu kelimelerin her biri hakkında açıklamalar bulacaksınız:

prepare MS-DOS’a ait belli bir ünite için kod sayfaları hazırlanmasını söyler. O üniteyle bunu

kullanmazdan önce söz konusu ünite için bir kod sayfası hazırlamalısınız.

select Belli bir ünite ile hangi kod sayfasını kullanmak istediğinizi belirler. Seçimi yapmazdan

önce bir kod sayfası hazırlamalısınız.

refresh Bir ünite için hazırlanan kod sayfaları her hangi bir fiziksel veya diğer hatlardan dolayı kaybolacak olursa bu kelime hazırlanan kod sayfalarını eski haline döndürür.

/statüs Bir ünite için hazırlanan ve / veya seçilen mevcut kod sayfalarını ekrana verir. Dikkat

ediniz, aşağıdaki komutların ikisi de aynı neticeleri vermektedir:

mode con codepage

mode con codepage/statüs

**Dolaylı Yazdırma******

Amaç : Veriyi paralel porttan seri haberleşme portuna düzelterek gönderir.

Dizilim : modeLPTn\[:\]=COMn\[:\]

**MORE******

**Akan Görüntüyü Durdurmak******

Amaç : Ekranda gösterilen verinin bir ekrana sığmaması durumunda her 24 satırda bir

görüntüyü durdurup bir tuşa basılmasını bekler.

Dizilim : more<kaynak

veya

kaynak:more

Kaynak bir dosya veya komuttur.

More uzun dosyaların izlenmesinde yaygın bir şekilde kullanılır. Örneğin kaynak olarak dil komutunu sort komutunu veya bir dosya ismini kullanabilirsiniz. More komutu bunun ardından duracak ve ekranın dibinde –more—mesajını verecektir.

Başka bir bilgi ekranını görüntülemek için her hangi bir tuşa basınız. Sonra tüm bilgiyi okuyana kadar tuşa basmaya devam ediniz. Girdi bilgisini ekranda görülene kadar tut.

**NLSFUNC******

Amaç : Ülkeye özgü bilgileri yükler.

Dizilim : nlsfunc\[sürücü:\]\[dizinadı\]dosyaadı

dosyaadı, ülkeye özgü bilgileri içeren dosyayı belirtir.

Nlsfunc komutu genişletilmiş ülkeye özgü bilgilerin ve kod sayfa anahtarlarının kullanımını sağlar.

Dosya isminin kabul edilen değeri config.sys dosyasındaki country komutu ile belirlenir. Şayet config.sys dosyanızda country komutu bulunmuyorsa MS-DOS ülkeye özgü bilgiler için ana dizininizin içinde ki country.sys dosyasını kullanır.

nlsfun.exe’yi tespit etmek için config.sys dosyasındaki install komutunu kullanabilirsiniz.

**PATH**

**Arama Yolu Ayarları******

Amaç : Komut arama yolunu ayarlar.

Dizilim : path\[sürücü:\]\[dizinadı\]\[;\[sürücü:\]\[dizinadı\]...\]

veya

path;

Bir komut arama yolunun maksimum uzunluğu 127 karakterdir. Yol komutu MS-DOS’a programların hangi dizinlerden aranması gerektiğini söyler. .com, .exe, veya .bat uzantılı dosyaları üzerinde çalıştığınız dizini aradıktan sonra yol ayarlanmış dizinlerde arar.

Örnek:

path c:\\dos; c:\\dbase ↵

MS-DOS programlarını dos dizinine bir database programını da dbase dizinine kopyaladığınızı varsayalım. Yukarıdaki komutu verdiğinizde veya autoexec.bat dosyasını iave ettiğinizde hangi dizin veya alt dizinde olursanız olun bu programlar çalışacaktır.

**PRINT**

**Yazdırma******

Amaç : Bir metin dosyasını bilgiyazdırdan almak.

Dizilim : print\[/d:ünite\]\[/b:hacim\]\[/u:değer1\]\[/m:değer2\]\[/s:değer3\]\[/q:dosyasayısı\]\[/t\]\[süzürü:\]\[\\dizinadı\\dosyaadı\]\[/c\]\[/p\]

Print komutunu ancak bilgiyazarın seri veya paralel portlarından birinde bağlı bilgiyazar veya plotter (çizici) gibi bir ünite bağlı olması durumunda kullanabilirsiniz.

Print komutunun anahtarları:

/d:ünite: Yazdırma ünitesinin adını belirler. Şayet /d seçerseniz, bu ilk parametre olmalıdır.

Varsayılan ünite PRN’dir. Paralel portlar için diğer muhtemel yazdırma ünitelerin isimleri şöyledir: LPT1, LPT2 ve LPT3. COMX, seri bir portu gösterir, burada x, 1’den 4’e kadar bir sayıdır.

/b:hacim Dahili buffer’in byte olarak hacmini belirler. Print komutunu hızlandırmak için /b değerini

arttırmalısınız. /b’nin minimum 512 ve değer verilmediği zaman kabul edilen değeri ise 1634’tür.

/u:değer1 Print komutunun bilgiyazarı bekleyeceği saat tiklerinin sayısını belirler. Eğer belirlenen

zaman dahilinde bilgiyazar müsait değil ise, iş görülmeyecektir. değer1 için geçerli değerler 1’den 255’e kadardır. Değer verilmediğinde 1 kabul edilir.

/m:değer2 Bilgiyazarın bir karakteri vurmak için gereken saat tiklerinin sayısını belirtir. değer2 için

geçerli değerler 1’den 255’e kadar değişmektedir. Değer verilmediğinde 2 kabul edilir.

/s:değer3 Print komutunda MS-DOS programcısı tarafından kullanılan zaman aralığıdır. Geçerli

değerler 1’den 255’e kadardır. Değer verilmediğinde 8 kabul edilir.

/q:dosyasayısı Yazma sırasına dosyaların sayısını belirler. /q anahtarı için minimim değer 4 olup

makximum değer 32 kabul edilir ve değer verilmezse 10 kabul edilir. Dosya sayısını değiştirmek için her hangi bir dosya ismi belirtmeksizin print komutunu girmelisiniz.

/t Yazılmayı bekleyen tüm dosyaları siler.

/c İptal komutunu çalıştırarak önceki dosya adını ve yazma sırasında bundan sonraki tüm

dosya adlarını siler. /c anahtarından evvel bir dosya adı belirlemeniz şarttır.

/p Yazma modunu açarak, yazma sırasına önceki dosya adını ve takip eden dosya

adlarını ilave eder. /p anahtarından önce bir dosya adı belirlemeniz şarttır.

Her hangi bir seçenek verilmeksizin kullanıldığında print komutu yazma sırasında bulunanların bu sıraya hiçbir şekilde etki etmeksizin ekranda gösterir.

/d, /b, /u, /m, /s ve /q anahtarları MS-DOS’u çalıştırdıktan sonra sadece print komutunu ilk kez devreye sokarken kullanılabilir.

Örnek:

print fiyat.txt /c ↵

**PROMPT**

**Komut Uyarısı******

Amaç : MS-DOS komut uyarısını değiştirir.

Dizilim : prompt \[\[text\]\[$karakter\]...\]

Bu komut MS-DOS sistemini prompt’unu değiştirmenizi sağlar. Eğer prompt komutunu kullanırken yeni bir değer girmezseniz prompt çalışan sürücünün adını ihtiva eden değere ayarlanmış olur.

Özel prompt’lar ortaya çıkarmak için prompt komutuyla aşağıdaki karakterleri kullanabilirsiniz:

Şu promptları almak için Şu karakterleri yazınız

= karakteri $q

$ karakteri $$

içinde bulunduğunuz zaman $t

O günkü tarik $d

Üzerinde çalıştığınız sürücü dizini $p

Uyarlama numarası $v

Varsayılan sürücü $n

< karakteri $g

< karakteri $1

¦ karakteri $b

ENTER – LINEFEED $ -

ASCII kod X’1B’ (escape) $e

Geri alan (backspace)(prompt satırına yazılmış bir

Karakteri silmek için) $h

Örnek:

prompt $P$G ↵

Bilgisayar normalde komut uyarısını c> veya a> şeklinde verir. Ayrıca o anda çalışan dizinin adını göstermez.

Yukarıdaki komutu kalvyeden yazdığınızda ve autoexec.bat dosyasını ilave ettiğinizde bu uyarı c:\\> şekline dönüşür. Muhasebe isimli dizine geçtiğinizde c:\\MUHASEBE> şeklinde görülür.

**QBASIC**

Amaç : MS-DOS Qbasic programını çalıştırır. Qbasic program yazmayı ve bunları uygulana-

bilir makine kodlarına dönüştürmeyi sağlar.

Dizilim : qbasic\[/b\]\[/editor\]\[/g\]\[/h\]\[/mbf\]\[/nohi\]\[/run\]\[sürücü:\]\[dizinadı\]\[dosyaadı\]

Qbasic komutunun anahtarları:

/b Renkli monitöre sahipseniz qbasic’i siyah-beyaz gösterir.

/editor MS-DOS editörü çalıştırır.

/g CGA monitörun en hızlı bir şekilde güncelleşmesini sağlar

/h Ekranınızdaki görülebilecek maksimum satır sayısını gösterir.

/mbf Yapı fonksiyonları (MKS$, MKD$, CVS ve CVD) MKSMBR$, MKDMBFS, CVSMBF ve

CVDMBF’ye dönüştürür.

/nohi High-intencity video ile desteklenmeyen bir monitörü kullanmanıza olanak verir. Bu tuşu

COMPAQ laptop bilgisayarlarla kullanmayınız.

/run Belirlenen basic programı görüntülenmeden önce çalıştırır. Dosya ismini belirtmelisiniz.

**RECOVER**

**Bozuk Dosyaları Kurtarma******

Amaç : Disk üzerindeki bir veya birkaç sektörün bozulması veya hatalı olması halinde dosya

veya dosyalardaki okunabilir bilgileri kurtarır.

Dizilim : recover\[sürücü:\]\[dizinadı\]dosyaadı

veya

recover sürücü

Şayet chkdsk komutunuz disk üzerinde bir sektörün bozuk olduğunu haber verirse recover komutu diskteki her dosyayı veya sadece bozuk sektöre sahip olan dosyayı düzeltmek için kullanabilirsiniz.

Bozuk bir sektör bulunduğu zaman bu sektördeki bilgi, bozuk olmayan başka bir yere aktarılır.

Ana dizin sadece sınırlı sayıda girdi tutabileceği için alınan bazı dosyalar kaybolabilir. Eğer bir diskteki tüm dosyaların geri alınması gerekiyorsa dosyaları tek tek alınız. Dosyaları alt dizine almaya veya bütün diski bir anda kurtarmaya kalmayınız.

Bir alt dizini recover komut satırında belirtilmesi alt dizinin dosyaların saklandığı orijinal alt dizinlerin yerini ana dizine alınmasına sebep olur. Recover komutu network üzerinde çalışmaz. Subst veya join komutlarında kullanılan sürücüler üzerinde çalışmaz. Recover komutu backup veya restore komutlarıyla çalışmaz.

Örnekler:

recover fiyat.txt ↵

Fiyat.txt dosyanız bozuk alanlar içeriyorsa bu komutu yazın. Dosya içindeki kurtarılabilecek bilgileri file0001.rec dosyası içinde ana dizine yazılmış olarak bulacaksınız.

recover c: ↵

Hard diskin tamamını tarayıp kurtarılacak bilgileri kurtarır. Eğer hatalı dosya miktarı çoksa ve diskteki boş alan azsa dosyaları bir önceki örnekte gibi tek tek kurtarmanız iyidir.

**REN**

**RENAME**

**Dosya İsmi Değiştirme******

Amaç : Bir dosyanın ismini değiştirir.

Dizilim : rename\[sürücü:\]\[dizinadı\]dosyaadı1dosyaadı2

veya

ren\[sürücü:\]\[dizinadı\]dosyaadı1dosyaadı2

dosyaadı1, dosyanın eski ismi

dosyaadı2, dosyanın yeni ismini belirtir

dosyaadı1 ile verilen dosyayı ren komutu diskte varsa dosyaadı2 ile değiştirecektir. Her iki dosya adı seçeneğinde joker kullanabilirsiniz, fakat bu jokerleri dosyaadı2 de kullanırsanız ren benzer karakterlerin pozisyonlarını değiştirmeyecektir.

Örnekler:

ren fiyat.txt eski-fi.txt ↵

fiyat.txt dosyası eski-fi.txt adını alır.

ren \*.txt \*.pub ↵

uzantısı .txt ile biten bütün dosyaların uzantıları .pub olur.

**REPLACE**

**Dosya Yenileme******

Amaç : Aynı isimdeki dosyaları bir disk veya dizinden diğerine kopyalar.

Dizilim : replace\[sürücü:\]\\dizinadı\\dosyaadı\[sürücü:\]\[\\dizinadı2\\dosyaadı2\]\[/a\]\[/p\]\[/r\]\[/s\]\[/w\]\[/u\]

\\dizinadı\\dosyaadı, kaynak dizinadı ve dosya adıdır.

\\dizinadı\\dosyaadı, ise hedef dizinadı ve dosya adıdır.

Hedef dizindeki doyaları aynı ismi almış olan kaynak dizindeki dosylarla üzerine kopyalar. /a anahtarını belirlediğiniz zaman replace kaynak dizindeki dosyaları hedef dizindeki dosyalara ekler.

Replace komutunun anahtarları:

/a Hedef dizindeki mevcut dosyaların yerlerine yenilerini koymak yerine hedef dizine yeni

dosyalar ilave eder. Bu anahtarı /s veya /u anahatarları ile kullanamazsınız.

/p Hedef dosyayı değiştirmeden veya bir kaynak dosya eklemeden önce size aşağıdaki

gibi bir mesaj göndererek uyarıda bulunur.

Replace filename ?(Y/N)

Dosya değiştirilecek mi (Evet/Hayır) ?

/r Normal dosyaların yanında silinemez, dosyaları da değiştirir.

/s Benzer dosyaları yerleştirme işlemini yaparken hedef dosyanın tüm alt dizinlerini

araştırır. Bu anahtar /a anahtarı ile zıttır. Replace kaynak dizindeki alt dizinleri asla araştırmaz.

/u Kaynak dizinde bulunan dosyalarda daha eski olan hedef dizin dosyalarını değiştirir. Bu

anahtar kaynak dosyanın kayıt, zaman/tarihin hedef dosyadakilerle karşılaştırır ve

yalnızca yenilenmesi gereken dosyaları yerleştirir.

/w Kaynak dosyaları araştırmaya başlamadan önce bir disk sürmenizi bekler. Şayet bu

anahtarı belirtmezseniz yerleştirme ve dosyaların eklenmesi işlemi hemen başlar.

Örnek:

replace a:fiyat.txt c:\\muhasebe ↵

a: sürücüsündeki fiyat.txt dosyasını muhasebe dizininde bulunan fiyat.txt dosyası üzerine kopyalar.

**RESTORE**

**Yedeklenmiş Dosyaları Geri Kopyalama******

Amaç : Backup programı kullanılarak yedeklenmiş dosyaları hard diske geri kopyalar.

Dizilim : restore sürücü1:\[sürücü2:\]\[\\dizinadı\\dosyaadı\]\[/s\]\[/p\]\[/b:tarih\]\[/a:tarih\]\[/e:zaman\]

\[/ı:zaman\]\[/m\]\[/n\]

Restore komutu benzer veya benzer olmayan tipteki disklerden dosyaları

kopyalayabilir.

Restore komutunun anahtarları:

/s Alt dizinleri de geri kopyalar.

/p En son backup işleminden beri değişmeye uğramış olan veya sadece okuma amaçlı

olan dosya spesifikasyonu ile uyumlu durumdaki dosyaları geri kopyalamak için izin

verir.

/b:tarih Tarihten önce veya tarihte değiştirilmiş olan dosyaları geri kopyalar.

/a:tarih Tarih veya tarihte veya tarihten sonra değiştirilmiş olan dosyaları geri kopyalar.

/e:zaman Zamanda veya zamandan önce değiştirilmiş olan dosyaları geri kopyalar.

/ı:zaman Zamanda veya zamandan sonra değiştirilmiş dosyaları değiştirir.

/m En son backup’tan sonraki değiştirilmiş dosyaları geri kopyalar.

/n Hedef dosyada olmayan dosyaları geri kopyalar.

**RMDIR**

**RD**

**Dizin Adı Silme******

Amaç : Bir dizinin adını diskten siler.

Dizilim : rmdir\[sürücü:\]dizinadı

veya

rd\[sürücü\]dizinadı

İçinde dosya veya alt dizin bulunmayan dizinlerin adını siler. Dizin içinde sadece “.” ve “..” karakterleri varsa içinde dosya yok demektir. Buna rağmen bazı dizinleri silmek istediğinizde dizini silemezsiniz. Bu durumda ya dizinin yapısında bir bozukluk vardır ya da dizinde gizli dosya bulunmaktadır. Gizli dosyaları açığa çıkarıp sildikten sonra dizini silebilirsiniz. Bir dizinin içindeyken o dizinin adını diskten silemezsiniz. Önce cd.. komutu ile dizini terk etmeniz gerekir.

Örnekler:

Diskten müşteri isimli dizini çıkartmak istediğinizde sırayla şu işlemleri yapın:

cd müşteri ↵

del \*.\* ↵

cd.. ↵

rd müşteri ↵

**SET**

Amaç : Programlarda daha sonra kullanılmak üzere hafıza bir karakter dizisi yerleştirir.

Dizilim : set\[değişken=\[string\]

MS-DOS bir set komutu aldığı zaman verilen karakter dizisini ve parametresinin hafızanın bir bölümüne yerleştirir. Bu karakter dizisi MS-DOS için anlamsızdır. Fakat daha sonradan bir program tarafından kullanılacaktır.

Örnek :

set lib=c:\\lib ↵

Kullandığınız derleyicinin program kütüphanesine erişebilmek için böyle bir komuta ihtiyacınız olabilir.

**SETVER**

**Uyarlama Tablosu******

Amaç : MS-DOS 5.0 altında çalışmayan yada bozuk olan programları çalıştırır.

Dizilim : setver\[sürücü:dizinadı\]\[dosyaadın.nn\]

setver\[sürücü:dizinadı\]\[dosyaadı\[/delete\[/quite\]\]

dosyaadı Uyarlama yapılacak program dosyasının adıdır.

n.nn çalışalack programın çalışacağı MS-DOS uyarlama numarasıdır.

Setver komutunun anahtarları:

/delete Belirlenen program dosyası için versiyon tablosu girişini iptal eder. Bu tuş /d olarak

kullanılabilir.

/qiute Versiyon tablosunun iptal edilmesi sırasında görülen mesajları gizler.

Setver farklı MS-DOS uyarlamalarında çalışan programlar için bir program ismi listesi ve programın hangi MS-DOS uygulamasında çalışacağını belirten uyarlama listesi tutar. Bu listeye program ismi ekleme ve çıkarma yukarda anlatılmıştır. Öncelikle setver’in aktivite gösterebilmesi için config.sys dosyasına aşağıdaki satırı ekleyip bilgisayarı yeniden çalıştırmalıyız.

device=c:\\dos\\setver.exe ↵

Daha sonra setver’in uyarlama tablosuna program ismini ve uyarlama numarasını eklemeliyiz.

**SHARE******

Amaç : Dosya paylaşımını ve kilitlenmesini tespit eder.

Dizilim : share\[/f:space\]\[/l:locks\]

Share normalde işlemler arasında paylaşılacak dosyaların bulunduğu ve network çevresinde kullanılır. Şayet share tespit edilirse bir aplikasyonun tüm okuma ve yazma istekleri açılmış olan dosyadaki dosya paylaşım koduna doğruluğu tespit edilir.

Şayet bir okuma veya yazma işleminin ortasında disk değiştirilse share yeni konulan diskin sürücüde daha önce bulunan disk olup olmadığını belirlemek için disk etiketine bakar. Eğer disk etiketi aynı değil ise MS-DOS geçersiz disk hatası mesajı gönderir, ve öndeki diskin sürücüye konulmasını ister. Önceki disk sürüldüğü taktirde share okuma ve yazma işleminin başarıyla tamamlanmasını sağlar.

Share komutunun anahtarları:

/f:space Dosya paylaşım bilgilerinin kayıt edilmesi için kullanılacak olan MS-DOS hafıza bölümü

için byte’lar halinde dosya boşluğu tahsis eder.

/f anahtarı için değer verilmezse 2048 kabul edilir. Şuna dikkat etmek gerekir ki

\\dizindı\\dosyaadı için ortalama 20 byte ayrılır. Her açık dosyanın 11 byte ilavesi ile birlikte bütün dosya adı genişliği için yeterli boşluk gerektirir.

/l:locks Kullanacağınız kilit sayısını belirler. /l anahtarı içinb değer verilmediğinde değer 20

kabul edilir.

Örnek:

Share ↵

**SORT**

**Sıralama**

Amaç : Girdiyi okur, bilgiyi sıralar ve daha sonra sıralanmış bilgiyi ekrana, bir dosyaya veya

başka bir araca yazar.

Dizilim : \[kaynak\]¦sort\[/r\]\[/+n\]

veya

sort\[/r\]\[/+n\]<kaynak

Sort komutu belli bir sütundaki karaktere bir dosyayı alfabetik sıra ile dizmenize imkan tanıyan bir filtre programıdır. Sort programı, ASCII kod tablosundaki sıraya göre sıralama yapar.

Sort komutunun anahtarları:

/r Sıralama olayını ters çevirir; yani z’den a’ya ve 9’dan 0’a doğru dizer.

/+n Dosyayı bu n satırındaki karaktere göre dizer. Eğer bu değişkeni belirlemezseniz sort komutu dosyayı ilk satırdaki karaktere göre tanzim eder.

Bir kaynak belirlemediğiniz sürece sort filtre rolü oynar ve girdileri MS-DOS standart girdisinden kabul eder.

Sort büyük harf ve küçük harf arasında ayrım yapmaz.

ASCII kod 127 üzerindeki karakterler country.sys dosyasından bulunan bilgiye ya da config.sys dosyasındaki country komutu ile tanımlanan kod sayfasına bağlı olarak tanzim eder.

Örnekler:

sort<adres.adr ↵

Bu komut adres dosyamızı alfabetik sıaraya koyup ekranda görüntüler.

dir¦sort/+4 ↵

Dosya listesindeki ilk 4 karakterlerini dikkate alarak sıralar ve ekranda gösterir.

**SUBST**

Amaç : Bir sürücü harfi ile dizin arasında bağlantı kurar.

Dizilim : subst\[sürücü:sürücü:dizinadı\]

veya

subst sürücü:/d

Bir sürücü harfi ile dizin arasında bağlantı kurmanızı sağlar. Bu sürücü harfi daha sonra bir virtual sürücüyü temsil eder. Çünkü sürücü harfini asıl fiziksel sürücüyü temsil ediyor gibi kullanabilirsiniz.

MS-DOS virtuel sürücüyü kullanan bir komut bulduğu zaman dizin adı ile sürücü harfinin yerini değiştirir ve yeni sürücü harfinin fiziksel sürücüye aitmiş gibi davranır.

Subst komutunu seçeneksiz yazarsanız MS-DOS devredeki virtuel sürücülerin isimlerini gösterir.

Virtüel sürücüyü devraden çıkarmak için /d anahtarını kullanın.

Şu komutlar subst komutunda veya join komutunda kullanılmış sürücüler üzerinde kullanılmaz: backup, format, chkdsk, label, diskcomp, recover, diskcopy, restore, fdisk, sys.

Örnek:

z: c:\\yeni ↵

Bu komutu uyguladıktan sonra yeni dizinine tıpkı sürücü değiştirir gibi z: komutunu vererek geçebilirsiniz. Aynı zamanda bu dizinine cd\\yeni komutu ile de geçebilirsiniz.

z: c:\\yeni/d ↵

Bir önceki komutla yapılan değişikliği iptal eder.

**SYS**

**Sistem Dosyalarını Yerleştirme******

Amaç : MS-DOS sistem dosyalarını disk sürücüsünden hard diske transfer eder.

Dizilim : sys\[sürücü:\]\[dizinadı\]sürücü

Sys komutu bir dikstteki sitem dosyalarınızı yeni bilgilerle güncelleştirir. Sys komutundan sonra bir sürücü harfi yazmalısınız. Transfer edilen dosyalar şunlardır: IO.SYS, MSDOS.SYS ve COMMAND.COM.

Sys komutu, subst ve join komutu ile çalışan sürücüler üzerinde çalışmaz. Sys bir network altında çalışmaz.

Örnek:

sys a: c: ↵

**TIME**

**Zaman Gösterme / Değiştirme******

Amaç : Sistem tarafından bilinen zamanı görmenize ya da sistem zamanını değiştirmenize

imkan tanır.

Dizilim : time\[saat:dakika\[:saniye\[salise\]\]\]\[a§p\]

MS-DOS 24 saatlik dilimler halinde zamanı takip eder ve bir dosyayı değiştirdiğimizde vay yeni bir doya açtığımızda bunlar dizine geçmek için zaman bilgisini kullanır. Time komutu tek başına kullanıldığında o anki zamanı gösterir ve zamanı değiştirme imkanı verir. Öğleden önce için a, öğleden sonra için de p anahtarını kullanınız.

Current time is hh:mm:ss:cc

Saat şu anda saat:dakika:saniye:salise

Enter new time

Yeni bir zaman giriniz

Şayet zamanı değiştirmek istemezseniz ENTER tuşuna basınız. Şayet zamanı değiştirmek isterseniz 24 saatlik birim içinde yeni değerler giriniz. Eğer geçerli bir zaman girmezseniz MS-DOS aşağıdaki mesajı verir ve geçerli bir zaman girmenizi bekler:

Invalid time

Geçersiz zaman

Enter nwe time

Yeni zaman giriniz

**TREE**

**Dizin Listesi******

Amaç : Sürücüdeki dizin ve alt dizinleri her birinin adlarını şemamatik olarak ekranda gösterir.

Dizilim : tree\[\\dizinadı\\dosyaadı\[/f\]\[/a\]

Dizin isimlerinin bulunması

Tree komutu her dizinin bütün dizin adının listesini verir. Eğer tek bir sürücü ismi belirtirseniz bu sürücüdeki ana dizinden başlayarak bütün tree yapısı ekranda gösterirlir. Belli bir dizini belirlerseniz, o dizinden başlamak üzere tree yapısı ekranda gösterilir.

Tree komutunun anahtarları:

/f Her dizindeki dosyaların isimlerini ekranda gösterir.

/a Kod sayfalarında mevcut olan grafik karakterlerin tree tarafından kullanılmasını sağlar.

Örnek:

tree/f ↵

**TYPE**

**Dosya İçeriğini Gösterme******

Amaç : Bir metin dosyasının içeriğini ekranda gösterir.

Dizilim : type\[sürücü:\]dosyaadı

Metin dosyasını değiştirmeden incelemek için typr komutu kullanılır.

Örnek:

type fiyat.txt ↵

Dosya ekrandan akarak geçer ve son sayfada durur.

type fiyat.txt¦more ↵

Dosya ekrana sayfa sayfa gelir. Her tuşa bastıkça bir sayfa atlar.

**UNDELETE**

**Dosya Kurtarma******

Amaça : Del komutu ile silinen dosyaları geri çağırmak için kullanılır.

Dizilim : undelete\[\[sürücü:\]\[dizinadı\]dosyaadı\[/list§all\]\[/dos§/dt\]

Undelet komutunun anahtarları:

/list Sadece kurtarılabilecek dosyaları listeler ancak kurtarma işlemi yapmaz.

/all Sizden onay beklemeden mümkün olan tüm dosyaları kurtarır.

/dt MS-DOS’un silinmiş olarak gösterdiği dosyaları kurtarır. Mirror dosyası kullanmaz.

/dt Mirror komutuyla kaydedilmiş dosyaları kurtarır.

Örnek:

undelete c:\\dos\\\*.\*/list ↵

Dos dizinindeki silinmiş tüm dosyaları ekranda gösterir. Eğer silinmiş dosya varsa kurtarmak için aşağıdaki komutu kullanabilirsiniz.

undelete c:\\dos\\\*.\*/all ↵

Dos dizinindeki silinmiş tüm dosyaları onay beklemeden kurtarır.

**UNFORMAT**

**Disk(et) Kurtarma******

Amaç : Format komutuyla silinmiş bir diski kurtarmak için kullanılır.

Dizilim : unformat sürücü:\[/j\]

unformat sürücü:\[/u\]\[/ı\]\[test\]\[/p\]

unformat\[/partn\]\[/ı\]

Unformat komutunun anahtarları:

/j Komut satırında tek başına kullanılır ve mirro programında elde edilen bilgilerle disk

durumunun doğruluğu kontrol eder. Diski kurtarma işlemini yapmaz.

/u Mirror dosyasını kullanmadan diski kurtarır. Disk tam olarak eski haline döndürülemez.

Ancak mirror programı ile disk bilgilerini kaydetmediyseniz bu anahtarı kullanınız.

/ı Diskteki tüm dosyaları listeler.

test Bilgilerin tekrar nasıl kurtarılacağını ve nasıl düzenleneceğini gösterir.

/p Ekrana gelen mesajları yazıcıdan yazdırır.

/partn Mirror komutu /partn anahtarı kullanılarak disk bilgileri PARTNSAW.FIL dosyasına

yazdırılmışsa bu anahtar kullanılarak diskteki bilgeler kullanılabilir.

Örnek:

unformat a:/u ↵

Mirro dosyası kullanmadan diskteki eski bilgileri kurtarmaya çaılışır.

**VER**

**MS-DOS Uyarlama Numarası******

Amaç : MS-DOS uyarlama numarasını gösterir.

Dizilim : ver

Kullandığınız MS-DOS uyarlamasının ne olduğunu öğrenmek isterseniz ver komutunu yazınız. Uyarlama numarası ekranda görülecektir.

Örnek:

ver ↵

MS-DOS 5.00

**VERIFY**

**Bozuk Dosya Kontrolü******

Amaç : Bir diske yazarken verify anahtarını anahtarını açar veya kapar.

Dizilim : verify\[on\]

veya

verify\[off\]

Dosyalarınızın diske doğru yazılıp yazılmadığını kontrol etmek için bu komutu kullanabilirsiniz.

Bu komut copy komutundaki /v ile anahtarı ile aynı işi görür.

Örnek:

verify on ↵

**VOL**

**Disk Etiketini Gösterme******

Amaç : Eğer varsa disk etiketini ve seri numarasını ekranda gösterir.

Dizilim : vol\[sürücü:\]

Bu komut belirli bir sürücüdeki disk etiketini ekranda gösterir. Eğer sürücüyü belirtmezseniz MS-DOS çalışan sürücüdeki disk etiketini gösterir.

Örnek:

vol c: ↵

## **2001 – 2002 2. DÖNEM**

## **DÖNEM ÖDEVİ**

## Adı : Enis Naci

## Soyadı : Doğan

## Sınıf : 9/O

## No : 3462

## Öğretmen Adı : Gönül Bedir

## Branş : Bilgisayar

## Dönem Ödevi Konusu : MS-DOS İşletim Sistemi Komutları

## İşlem Yapılması ve Tarihçesi

## Okulun Adı : Kadriye Moroğlu

---
*Kaynak: `APPEND - Arama Yolu Ayarlama/APPEND - Arama Yolu Ayarlama.doc` — Batuhan — 2004*
