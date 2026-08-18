# Veri Tabani Ve Bazi Kavramlari

VERİTABANI VE BAZI KAVRAMLAR

Veritabanı Veritabanı Yönetim Sistemi Temel Veritabanı Kavramları Dbase'e Giriş

DOS (Dbase) komutları

Dbase Veri Dosyası Create Use List structure Modify Structure go-skip Zap

Display APPEND BROWSE DELETE LIST EDIT RECALL

FONKSİYONLAR

SUM COUNT AVERAGE COPY SET INDEX SORT

Program Yazımı Örnek programlar Kütük kullanımı örnek programı İndexli kütük program örneği

Veritabanı (Database):

Veritabanı (database) bir sorunu çözmek amacıyla bir araya getirilmiş, birbirleriyle ilişkili verilerin bir topluluğudur. Veri tabanı, belirli bir tarzda organize edilmiş faydalı verilerin bir kolleksiyonudur. Bu verilerin bir araya getirilmesi ve bunların işlenerek anlaşılır bilgi haline dönüştürülmesi bilgi-işlem açısından çok önemlidir.

Çok sayıda bilginin, güvenilir bir şekilde saklanması ve üzerlerinde çeşitli işlemlerin yapılması gerektiğinde, bu bilgileri oluşturan verilerin anlamlı biçimde düzenlenmeleri gerekmektedir. İyi düzenlenmiş bir veri tabanı ile birçok işlev yerine getirilebilir.

Günümüzde, değişik konulara ilişkin bir çok veritabanı oluşturulmuştur. Hastane yönetim sistemine ilişkin veri tabanı örnek olarak verilebilir. Bu veritabanında;

Hasta kayıtları

Personel kayıtları

Malzeme kayıtları

Muhasebe kayıtları

Bilimsel çalışmalar

Büro işlemleri

gibi veriler tutulmaktadır. Bu veriler arasında çeşitli ilişkiler kurularak, bir verinin tekrar veritabanına girmesi önlenmiş, ayrıca veritabanı üzerinde güncelleştirme işlemleri yapılarak veritabanının aktif bir şekilde kullanılması sağlanmıştır.

ÖRNEK : Bir kişisel telefon rehberi bir veritabanı olarak görülebilir.

| Ad Soyad | Şehir Kodu | Telefon No |
| --- | --- | --- |
| Mehmet Türkmen | 322 | 2384153 |
| Uğur Yüksel | 216 | 2761651 |
| Erhan Seçilen | 212 | 4327862 |
| İbrahim Sağlam | 318 | 6115240 |
| Ramazan Tekinarslan | 322 | 7145678 |
| Veli Korkmaz | 322 | 4567890 |
| Ayhan Akgöz | 212 | 1234567 |

Bu telefon rehberi, rasgele düzenlenmiş isimleri ve telefon numaralarını gösterir bir listedir. Bununla beraber, bu liste istenilen tercihe veya forma göre belirli bir sırada organize edilebilir. Örneğin, liste ada veya soyada göre alfabetik sırada, telefon numarasına göre artan bir şekilde sıralanabilir, şehir kodları kendi içinde gruplanabilir. Karışık bir telefon rehberinin, hiçbir yararı olmayacağından bizim için önemli olan, bilgilerin istediğimiz düzende olmasıdır.

Veritabanı Yönetim Sistemi :

Veritabanı yönetim sistemleri büyük iş verilerini organize etmek ve işlemek için kullanılmaktadır. Bu sistemler çok büyük sayıda veri elemanlarını etkili bir şekilde yöneten güçlü bilgisayar programlarıdır. Bu sistemler değişik iş ve konularda insanlara büyük kolaylıklar sağlamaktadır.

Geçmişte, sadece büyük bellek kapasiteli ve yüksek işlem hızlı bilgisayarlarda uygulanan veritabanı yönetim sistemleri maliyet açısından oldukça pahalıydı, bununla beraber kişisel bilgisayarların gelişmesi veritabanı yönetim sisteminin sınırlı bir yatırımla yapılmasına olanak sağlamıştır.

Günümüzde kişisel bilgisayarlar için geliştirilmiş pek çok veritabanı yönetim programları vardır. Bunlardan en çok kullanılanları DBASE, PARADOX, SMART, FOXPRO, ORACLE gibi paket programlardır.

Bu programlarda;

Data entry : Veri girişi

Update : Güncelleştirme

Delete : İptal (silme)

Motify : Değişiklik

Query : Sorgulama

Reporting : Raporlama

işlemleri ve diğer özel işlemlerin yapılması oldukça kolaydır. Veritabanı paket programları, yukarıda sözü geçen işlemleri yapmaya diğer programlama dillerine göre oldukça elverişlidir ve işlemler inter-active (karşılıklı etkileşim) olarak kolayca yapılabilir.

Yaygın kullanımı ve veritabanı yönetim sistemine giriş olması nedeniyle DBASE III PLUS veritabanı programının kullanımını anlatılacaktır. DBASE : Kişisel bilgisayarlar için üretici firma tarafından geliştirilmiş veritabanı yönetim sistemi programlarıdır. Bu tür programlar programcı olmayanlar tarafından da rahatlıkla kullanılabilen kütük düzenleme programlarıdır. Çeşitli uyarlamaları (versiyon) bulunmaktadır. Bu kitapta anlatılacak fonksiyonlar DBASE III PLUS'a ait olacaktır.

Temel Veritabanı Kavramları :

Verilerin birbirlerinden bağımsız bir şekilde bulunmaları kullanıcılar açısından hiçbir önem taşımaz. Bu nedenle veriler gruplandırarak bir dosya (kütük) içerisinde toplanır.

Bir okuldaki öğrencilerin çeşitli bilgileri bulunmaktadır. Her öğrenci için farklı bilgilerin tutulması bilgi-işlem açısından pek önem taşımaz. Bu nedenle her öğrenci için aynı verilerin bulunduğu bir dosya oluşturulması okul yönetimi tarafından tercih edilecektir.

Dosya (File) : Ortak özellikteki bilgilerin yer aldığı kayıtlar topluluğudur.

Kayıt (Record) : Bir dosyayı oluşturan en küçük bilgi gruplarıdır.

Alan (Field) : Bir kayıt içindeki alt sahalardır.

Bir veritabanı oluşturulmasında birçok faktöre dikkat edilmelidir. Bu faktorlerden bazıları;

İlgilenilen sorunun iyice kavranılmış olması,

İlerde değişecek unsurların gözönünde bulundurulması,

Sorgulamayı zenginleştirici ilişkilerin kullanılması,

Disk kapasitesi gibi unsurların gözönünde bulundurulması,

olarak sıralanabilir

Veritabanı oluşturan kişi veya kişilerin o işle ilgili (veritabanını isteyen kişi veya kurum) kişilerle mevcut sistemin nasıl işlediği konusunda, kullanılan belgeler ele alınarak detaylı bir şekilde görüşmeleri ve ilgilenilen sistemi en ince ayrıntısına kadar analiz etmeleri, veritabanı oluşturulduktan sonra neler istenebileceğini esnek bir biçimde belirlemeleri gerekmektedir. İyi bir analiz yapılmadan, mevcut işleyiş anlaşılmadan oluşturulacak veritabanı, kullanımda birçok zorlukların çıkmasına, sistemin tıkanmasına yol açacak, boşyere emek ve zamanın harcanmasına neden olacaktır.

Örneğin bir dosya içinde il, ilçe, mahalle gibi bilgiler bulunacaksa bu bilgileri belirli bir kurala göre kodlamakta oldukça yarar vardır.

İl dosyası

| İl kodu | İl adı |
| --- | --- |
| 01 02 ... | Adana Adıyaman ... |

İlçe dosyası

| İlçe kodu | İlçe adı |
| --- | --- |
| 01001 01002 ... | Ceyhan Kadirli ... |

Mahalle dosyası

| Mahalle kodu | Semt adı |
| --- | --- |
| 01001001 01001002 ... | Mithatpaşa Burhaniye ... |

DBASE III'E GİRİŞ

Dbase III Plus'ın Teknik Özellikleri :

| Maksimum kayıt sayısı :1 milyar dbase kaydı Maksimum byte sayısı :2 milyar byte Bir kaydın büyüklüğü :4 bin byte Kayıt içi alan sayısı :128 alan Bilgi içi byte sayısı :254 byte |
| --- |

Değişkenler :

Program içerisinde çeşitli zamanlarda çeşitli değerler alabilen büyüklüklere denir. Dbase'de 4 tür değişken tanımlaması yapılabilir;

1 - Character : Maksimum uzunluğu 256 byte olan alfasayısal bilgileri saklayan büyüklüklerdir.

2 - Numeric : 15 basamak tamsayı, 9 basamak desimal noktadan oluşan, tamsayı ve reel bilgiler içeren büyüklüklerdir.

3 - Logical : Boolean (doğru-yanlış) tipli 1 karakterden oluşan büyüklüklerdir. (Yes=Y, No=N, True=T, False=F)

4 - Date : Tarih bilgisini saklayan ve sistemin kendisine göre giriş istediği 8 karakterlik büyüklüktür.

Değişken İsimlendirme Kuralları :

Değişkenlerin uzunluğu en fazla 10 karakterdir. Değişkenin ilk karakteri harf olmak zorundadır. İlk harf karakter olmak koşuluyla daha sonraki karakterler harf veya sayı olabilir. Ayrıca alt çizgi ( \_ ) dışındaki karakterler geçerli değildir.

Dbase Operatörleri :

1 - Matematiksel operatörler

| + Artı - Eksi \* Çarpma \*\* Üs alma ( ) Grup işlemleri |
| --- |

2 - Karşılaştırma operatörleri

| < Küçük > Büyük <= Küçük eşit >= Büyük eşit <> veya # Eşit değil |
| --- |

3 - Mantıksal operatörler

| .AND. Ve .OR. Veya .NOT. Değil ( ) Grup işlemleri |
| --- |

4 - String (karakter dizisi) operatörleri

| + Birleştirme $ Karakter grup karşılaştırıcı |
| --- |

Bu operatörlerin kendi aralarındaki öncelik sıraları aşağıda verildiği gibidir.

| 1. + , - 2. \*\* 3. \*, / 4. .NOT. 5. .AND. 6. .OR. |
| --- |

| 1. Matematiksel ve string 2. Karşılaştırma 3. Mantıksal |
| --- |

Dbase'de Kullanılan Fonksiyon Tuşları :

CTRL+W : Yapılan değişikliklerin dosyaya kaydedilmesini sağlar.

Dbase Dosyaları (File) :

Dbase dosyaları geniş kullanım olanaklarına sahiptir. Bir DBASE programında aynı anda; 15 dosya, 10 DBASE dosyası(.DBF), 7 sıralı dosya (.NDX) açmak mümkündür.

Dbase'de çok çeşitli dosyalar oluşturulmakta ve bu dosyaların her biri farklı işlemler için kullanılmaktadır. Bu dosyalar ve amaçları kısaca aşağıda verilmiştir.

| DOSYA | UZANTI | ANLAMI |
| --- | --- | --- |
| Database Format Index Label Report Screen Memory Query Viev Text Output Catalog Dbase Memory Comm&Procedure | .DBF .FMT .NDX .LBL .FRM .SCR .MEM .QRY .VUE .TXT .CAT .DBT .PRG | Database veri dosyası Ekran düzenleme dosyası İndexli (sıralı) kayıt dosyası Etiket amaçlı dosya Yazıcı ve ekran çıktısı dosyası .FMT dosyasına bağlı ekran dosyası Bellek değişkenleri dosyası Koşulların yazıldığı dosyadır .DBF'ler arasında kurulan ilişkilerin yansıtıldığı dosyadır Bilgilerin metin şeklinde saklandığı dosyadır. Bir dosyanın, diğer dosyalarla olan farklılıklarını yansıtan dosyadır. .DBF dosyalarında bellek dosyaları kullanıldığında oluşan dosyadır. Program dosyalarıdır |

DBASE PROGRAMININ ÇALIŞTIRILMASI

Disk ortamında iken Dbase programına girmek için

C\\dbase>dbase (Enter)

komutu kullanılır. Bu program çalışırken CONFIG.DB kütüğünden bir takım komut satırları okunarak belleğe yüklenir. dbase yazıp Enter tuşuna basıldığında ASHTON-TATE Firmasının bir tanıtım menüsü ekrana gelir. Bu menü ENTER ile geçilir. Daha sonra eğer CONFIG.DB (database configuration) kütüğünde tamınlanmış ise, Assist Menü dediğimiz yardımcı menü gelir. Bu menüden (ESC) tuşuna basarak çıkılabilir. Bu durumda dot prompt denilen komut satırına geçilir.

Assist Menü : Ekran dosyası oluşturma, Rapor formu oluşturma, Etiket Formu oluşturma, dosya kopyalama ve silme gibi işlemlerin yapılabildiği etkileşimli bir menüdür. Bu kitapta komut satırı ve program komutlarının nasıl kullanıldığı anlatılacaktır.

Quit (çık) : Dbase'den DOS ortamına dönülür.

Clear (temizle) : Ekran temizlenir.

NOT : Dbase komutlarının veya fonksiyonlarının ilk 4 karakterini kullanmak yeterlidir.

Dbase programı içerisindeyken DOS komutlarının veya hemen çalışabilir programların çalıştırılabilmesi için (EXE, COM, BAT uzantılı)

.run <dos komutu >

veya

.! < dos komutu >

komutları kullanılır.

Komut satırının altında görülen ışıklı satıra STATUS LINE (durum satırı) denir. Eğer Dbase programının çalıştığı ortamda CONFING.DB kütüğü yoksa veya bu kütüğün içerisinde STATUS ON tanımı yapılmışsa Dbase ilk çalıştırıldığında STATUS LINE görülmez. STATUS LINE'ın aktif olması (görülmesi) kullanıcının çalışmasına yardımcı olmasını sağlar.

Komut satırında prompt (nokta) önünde en fazla 254 karakter uzunluğunda komut girişi yapılabilir. Bir önceki girilen komutlar, yukarı ok veya aşağı ok tuşları ile getirilebilir. Komut satırındayken; END tuşu kelimelerin üzerinde sağa doğru atlar, HOME tuşu ise sola doğru kelimelerin üzerinden atlar, CTRL+Y tuşları ise komut satırını tümüyle siler. Komut satırınd yanlış bir komut yazılırsa veya komut olmayan bir ifade yazılırsa

\*\*UNRECOGNIZED COMMAND VERB

DO YOU WANT SOME HELP(Y,N)?

mesajları yöneltilir. Bu mesaja (Y) girilirse yardım menüsü gelir. Yardım normalde F1 tuşuna basılarak veya direk olarak HELP yazılarak çağrılabilir. Yardım programından çıkış ESC tuşudur. Bir önceki menüye dönmek için F10 tuşu kullanılır. . HELP (veya F1) yazıldığında genel yardım menüsü gelir. Eğer sadece belirtilen komutla ilgili yardım isteniyorsa help <komut ismi> komutu yazılır.

? komutu : Önünde belirtilen ifadeyi yorumlar ve ekrana yazar.

Örnekler :

. ? 18+14 32

.? 2^4 16

. "A"+"B" AB

.? 2\*\*4 16

?? Komutu ise önünde belirtilen ifadeyi yorumlar ve sonucu bir önce yazdırılan satıra yazar.

DOS işletim sistemi komutlarına benzeyen bazı Dbase komutları :

.DIR : Belirtilen disk ortamındaki belirtilen kütükleri ekrana listeler. komut içerisinde \* ve ? karakterleri kullanılabilir. Eğer sadece DIR komutu işletilirse .dbf kütüklerini listeler. Listede kütüğün ismi, kütükdeki toplam kayıt sayısı, son olarak update edildiği tarih ve byte olarak büyüklüğü yer alır. Ayrıca disk ortamında geriye kalan kullanılabilir kapasite de belirtilir.

.DIR

.DIR \*.\*

.DIR c:\\temp\\\*.\*

.DIR \*.PRG

.DIR C:\\DOS\\?? K\*.\*

.TYPE : Belirtilen disk ortamındaki bir tek kütüğün içeriğini ekrana ya da yazıcıya listeler.

.TYPE C:\\AUTOEXEC.BAT

.TYPE OGRECI.PRG TO PRINT

.TYPE C:\\DBASE\\A.PRN TO PRINT

.DELETE FILE : Dosya silmek için kullanılır.

.DELE FILE DENE.DBF

.DELE FILE C:\\TEMP\\DENE1.PRG

Eğer silinecek kütük bir veri kütüğü ise bu kütüğün kapalı olması gerekir. Kütük silme işlemi ERASE komutuyla da yapılabilir.

.ERASE STOK.DBF

.ERASE C:\\DBASE\\DENE1.TXT

.COPY FILE <kütük ismi> TO <kütük ismi> : Dosya kopyalamak için kullanılır.

.COPY FILE stok.dbf TO yedstok.dbf

.RENAME <eski dosya ismi> TO <yeni dosya ismi> : Dosya adı değiştirmek için kullanılır. Eğer dosya bir veri kütüğü ise bu kütüğün kapalı olması gerekir.

.RENA dene.dbf TO dene1.dbf

.SET DEFAULT TO \[<Sürücü ismi>\] : Aktif Sürücü Ortamının Değiştirilmesi için kullanılır.

.SET DEFAULT TO A

.SET DEFA TO C:\\stok

Sadece .SET DEFA TO komutu verilirse Dbase programının başlatıldığı orijinal sürücüye dönülür.

.komut satırında iken bir takım matematiksel işlemler yaptırılıp ekrana yazdırabilir. Bunun için ? karakteri kullanılır. Eğer ?? komutu kullanılırsa yazdırılan bilgi bir önce yazdırılan satıra yazdırılır.

Örnekler :

.? 3\*10

30

.? "27"+"8"

278

.A="MEHMET"

.B="ALİ"

.?A+B

MEHMETALİ

.! FORMAT A:

.RUN FORMAT A:

.! EDIT

.RUN EDIT

.Erase Must.dbf

.Erase c:\\aa.prg

.delete file tel.txt

.dele file C:\\db\\hastane.dat

.copy file sınıf.dbf to sınıf1.dbf

.copy fıle ambar.dbf to A:\\

.rena aa1.dbf to AB1.dbf

.rena A:\\ ambar.dbf to ambary1.dbf

Dbase Veri Dosyası (.DBF) :

İşlem yapabilme özelliği taşıyan, üzerlerinde işlem yapılabilen, belirli bir düzene sahip olan her türlü bilgiyi saklayan dosyalara veri dosyaları denir. Bu veriler yan bellek birimlerinde (disk, disket) saklanan bilgilerdir. Dbase, veri dosyaları oluşturmak için diğer programlama dillerinde olduğu gibi uzun programlar yazmayı gerektirmez. Veriler üzerinde doğrudan işlem yapabilme özelliği, hem zaman hem de kullanım kolaylığı sağladığından yaygın kullanım alanına sahiptir.

Dbase Dosyalarının (kütüklerinin) Oluşturulması :

Dbase kütüklerinin uzantısı dbf'dir. Dbase kütükleri ya Assist menüden ya da komut satırından verilecek Create komutuyla oluşturulur. Bir database kütüğünü oluşturmaya başlamadan önce bu kütüğün yapısını, yani kayıtlarda yer alacak alanları, tiplerini ve uzunluklarını belirtmek gerekir.

Kütük yapısı oluşturulurken;

Field Name Type Width Dec

--------------- ---------- ----------------- ----------------------------

Alan ismi Alan tipi Alan uzunluğu ondalık kesrin uzunluğu

bilgileri doldurulur. Bir kütük yapısında en fazla 128 alan belirtilebilir. Alan isimlerinin uzunluğu maksimum 10 karakter olabilir. Alan ismi içerisinde boşluk karakteri veya özel bir karakter yer alamaz, fakat alt çizgi ( \_ ) kullanılabilir. Alan ismi'nin ilk karakteri geçerli bir karakter olmalıdır. Bir kaydın toplam uzunluğu maximum 4000 byte olabilir. Alan tipleri şunlar olabilir:

Charecter : Alfabetik bilgi girme amacını taşır. 1.karakteri alfabetik olmak koşulu ile sayısal karakterler de girilebilir.

Numeric : Sayısal bilgi girme amacını taşır. Alfabetik bilgi girilemez.

Date : Tarih girme amacını taşır. Tarih bilgileri (MM/DD/YYYY) şeklinde veya değiştirilerek (DD/MM/YYYY) şeklinde girilir. Bu form dışındakiler kabul edilmez.

Logical : Mantıksal değerler girme amacı taşır. Yes, No, True, False değerlerinden birisi verilir. Diğerleri kabul edilmez.

Memo : Çok fazla karakterden oluşan metinsel bilgileri depolamada kullanılan alanlardır. memo alan bilgileri .dbt kütüğü içerisinde saklanır. Alfabetik alanlardakine benzer bilgiler olmak üzere kullanılan editöre göre istenilen sayıda karakter bilgi depolanabilir.

Alan tipi tanımlanırken tiplerin ilk harflerini girmek yeterlidir. Alanların tanıtımı bittikten sonra Ctrl+End ve Enter tuşları ile oluşturulan dosya disk'e kaydedilir. Bir alan bilgisini silmek için Ctrl+U tuşlarına basılır. Eğer araya yeni bilgi alanı girilecek ise Ctrl+N tuşlarına basılır. Field Name, Type, Width ve Dec Bölgeleri üzerinde Home ve End tuşlarına basılarak dolaşılabilir. Home bir önceki bölgeye End ise bir sonraki bölgeye geçmeyi sağlar. Alanlar üzerinde ise aşağı ve yukarı ok, Pgup ve Pgdn tuşları ile aşağı yukarı hareket edilebilir.

Dbase Kütüğünü oluşturmak için

.Create kütük-ismi

komutu kullanılır.

Bu komut yazıldığında

| Field Name Type Witdh Dec ......... ........ ......... ...... ......... ........ .......... ....... |
| --- |

bilgilerinin girilmesi istenir. İlgili bilgiler girilip Ctrl+End tuşlarına basılarak kütüğün yapısı disk ortamına kaydedilir. dbf kütüğünün yapısı disk ortamına kaydedilmeden önce, input data records now? (Y\\N) sorusu yöneltilir (şimdi veri girecek misiniz?). Y denilirse kayıt girişi başlatılır. Kayıt girişinde önceki kayıt bilgilerini görmek için PgUp, sonraki kayıt bilgilerini görmek için PgDn tuşları kullanılabilir. Kayıt girişine son vermek için boş kayıt üzerindeyken Esc tuşuna veya en son girilen kayıt üzerindeyken Ctrl+End tuşlarına basılır. Create komutuyla dbase kütüğü oluşturulduğunda kütük aktif hale gelir. Aktif bir kütüğü kapatmak için sadece Use komutu kullanılır.

Kapalı bir dbase kütüğünü aktif hale getirmek için de

.Use <kütük ismi>

komutu kullanılır. Use komutu Dbase dosyalarının aktif veya pasif duruma gelmesini sağlar. Açık olan herhangi bir Dbase kütüğü Close komutu ile kapatılır.

Daha önceden oluşturulan kütüğe veri girmek için

.Append

komutu veya F9 tuşu kullanılır (kütük aktif olmalıdır).

Bu komuttan sonra kütüğün sonuna yeni bir kayıt girişi yapılmak üzere ekrana boş bir kayıt giriş alanı getirilir.

Kütüğün yapısını (structure) görüntülemek için,

.List structure \[to print\]

komutu kullanılır (kütüğün aktif durumda olması gerekir)

Kütüğün yapısını değiştirmek için

.Modify Structure

komutu kullanılır (kütük aktif olmalıdır).

Bu komut kullanıldığında aktif kütüğün kayıt alanları ekrana getirilir. Eğer istenirse bir kayıt alanı eklenip iptal edilebilir. Eğer kütükte veri varsa yapılan işlemlere göre bu veriler yeni yapıya aktarılır veya silinir. Yapılan son değişikleri saklamak için Ctrl+W veya Ctrl+End tuşlarına yapılan değişiklikleri saklamadan çıkmak için Esc veya Ctrl+Q tuşlarına basılır.

Kayıtlarda değişiklik yapmak için

.Edit

komutu veya F10 tuşu kullanılır.

Sadece edit komutu verilirse değişiklik yapmak üzere o anki aktif kayıt bilgileri ekrana getirilir. Kayıtlar üzerinde PgUp, PgDn tuşlarıyla dolaşılır. Alan bilgileri üzerinde değişiklik yaparken Home tuşu alanın başına End tuşu alanın sonuna erişilmesini sağlar. Alan bilgisi boşluklarla birkaç kelimeden oluşuyorsa Home kelime başına End tuşu kelime sonuna gitmeyi sağlar. Ctrl+Y tuşu alan bilgisini, Ctrl+T kelime bilgisini siler.

Kütükteki kayıtlar üzerinde aşağıdaki komutlarla hareket edilir.

.use kütük-ismi

.go n (n. kayda gider)

.go 5 (5. kayıt üzerine gelinir)

.go top (İlk kayda gidilir)

.go bottom (son kaydın üzerine gidilir)

.skip \[n\] (kaydı n kayıt kadar ilerletir veya geriletir)

.use kütük-ismi (1.kayıt üzerindeyiz )

.skip 5 (5 kayit ileriye gidilir)

.skip -3 (3 kayıt geriye gidilir)

.skip (1 kayıt ileri gidilir)

Kütük başı ve kütük sonu için

.BOF() : Begining of the file (kütüğün başı)

.EOF() : End of file (kütüğün sonu)

komutları kullanılır.

.use kütük-ismi

.skip -1

.? BOF()

.T (Evet)

.go bottom

.? EOF()

.T

Aktif olan kaydın kayıt numarasını görmek için

.RECNO()

fonksiyonu kullanılır. Kütük açılır açılmaz aktif kayıt 1.kayıttır.

.use kütük-ismi

. ? recno()

.1

. skıp 5

. ? recno()

6

Komutlarda Kullanılan Çalışma Alanları (Scopes):

ALL : Bütün kayıtlar

NEXT n : Sonraki n kayıt

REST : Geriye kalan kayıtlar

RECORD n : n.kayıt

Çalışma alanları komutlarda hangi kayıtların işleme gireceğini belirler.

Kütükteki kayıtları listelemek için

.List

komutu veya F3 tuşu kullanılır (kütük aktif olmalıdır).

.use kütük-ismi

.list

komutlarıyla ilk kayıttan itibaren tüm bütün kayıtlar ekrana listelenir. Listeleme işlemini kesmek için Esc tuşu kullanılır.

.use kütük-ismi

.list to print

komutlarıyla bütün kayıtlar yazıcıdan listelenir.

Kütüğe girilen kayıtları topluca görmek, istenilen bilgileri değiştirmek ve yeni kayıt eklemek için

. Browse

komutu kullanılır.

Kütükteki tüm kayıtları silmek için

.Zap kütük-ismi

komutu kullanılır. Kayıtların geri alınması söz konusu değildir. Zap komutu işletildiğinde Y/N mesajı iletilir. Y verilirse bütün kayıtlar silinir.

Kütükteki istenilen kayıtları silmek için

.Delete

komutu kullanılır.

Bu komut belirtilen kayıtları kütükten silmek üzere \* karakteriyle işaretler bu komutun arkasından Pack komutu kullanılırsa Delete komutuyla işaretlenmiş kayıtların hepsi fiziksel olarak silinir. Pack komutuyla kayıtlar silindikten sonra kayıtların geri alınması mümkün değildir.

Delete komutuyla silinmek üzere işaretlenen kayıtların \* işaretini kaldırmak için

.Recall

komutu kullanılır.

Aşağıda, komutların çalışma alanları ile birlikte nasıl kullanıldıkları anlatılacaktır. \[ \] işareti seçimlik olduğunu belirtir. < > zorunlu olduğunu belirtir.

DISPLAY \[<kayıt grubu>\] \[<saha-isimleri>\] \[FOR <koşul>\]

WHILE \[<koşul>\] \[OFF\] \[TO PRINT\]

Anlamı :

İstenilen koşula göre istenilen sahaları ekrana listeler.

FOR ve WHILE : Belirli koşula uyacak kayıtları listelemek için kullanılır.

OFF : Kayıt numaralarının görüntülememesini sağlar.

TO PRINT : Listenin yazıcıdan alınmasını sağlar.

kayıt grubu : Listeleme için kaydın hangi grup arasında aranacağını belirler.

saha-isimleri : Hangi sahaların görüntüleceğini belirler.

koşul : Kayıtların uyması gereken koşulu belirler.

Ekran dolduğunda bir tuşa basana kadar beklenir.

APPEND \[BLANK\]

APPEND FROM <dosya-ismi> \[FOR <koşul>\]

\[TYPE dosya-tipi\] /

\[DELIMITED \[WITH BLANK/<delimiter>\]\]

Anlamı :

APPEND : Aktif durumdaki veri dosyasına ekrandan veri girişini sağlar.

APPEND BLANK : Aktif dosyaya boş bir kayıt ekler.

APPEND FROM : <dosya-ismi> adlı dosyanın kayıtlarını aktif durumdaki dosyanın sonuna ilave eder.

TYPE : <dosya-ismi> adlı başka formattaki dosyadan kayıt eklemek için kullanılır.

Başa dosya tipleri aşağıda belirtilmiştir.

SYLK : Microsoft Multipan veya Microsoft Chart

ASCII : Herhangi bir kelime işlemci

WKS, WR1 : Lotus Symphony

DIF : Bazı tablolarda kullanılan tipler (R:base)

SDF : Bazı kelime işlemcilerin kullanığı format (Microsoft Word)

DELIMITED : Bazı kelime işlemcilerin kullandığı format (Wordstar, Microsoft Word)

Not : ASCII dosyaları için saha ayıracı boşluk, kayıt ayıracı satırbaşı kontrol karakteridir. Delimited dosyaları için saha ayıracı "" ve virgüller, kayıt ayıracı bir satırdır. Tablo türünden tüm dosyaların saha ayıracı sütun, kayıt ayıracı satırdır. Dbase dosyasının yapısı ile bu tipten dosyaların saha yapılarının uyumlu olması gerekir.

BROWSE \[FIELDS <saha-isimleri>\] \[LOCK <sayı>\]

\[FREEZE <SAHA>\] \[WITDH <sayı>\]

\[NOAPPEND\] \[NOMENU\]

Anlamı :

Ekranın tamamını kullanarak kayıtların görülmesini, düzeltilmesini ve yani kayıt girişini sağlar.

FIELDS : Hangi sahaların düzeltileceğini belirler.

LOCK : En soldaki ve kayma işlemleri sırasında sabit kalacak alanların sayısını belirler.

WITDH : Karakter sahaların düzeltme genişliğini belirler.

FREEZE : Tek bir sahayı düzletmek için kullanılır.

NOAPPEND : Kayıt girişini önler. NOMENU : Seçim menüsünü kapatır.

DELETE \[<kayıt grubu>\] \[FOR <koşul>\] \[WHILE<koşul>\]

Anlamı :

Aktif durumdaki veri dosyasından silinecek kayıtlara \* işaretini koyar. Bu işlem bir bakıma mantıksal silme işlemidir. FOR ve WHILE belirli koşula uyacak kayıtları silmek için kullanılır. PACK komutu kullanılmadığı sürece bu kayıtlar fiziksel olarak silinmez. \* işaretlerini kaldırmak için RECALL komutu kullanılır. Kaydın silinip silinmediğini öğrenmek için DELETED() komutu kullanılır. \* işareti LIST ve DISPLAY komutlarında görülür.

LIST \[<kayıt grubu>\] \[<saha-isimleri>\] \[FOR <koşul>\]

WHILE \[<koşul>\] \[OFF\] \[TO PRINT\]

Anlamı :

İstenilen koşula göre istenilen sahaları ekrana listeler. Kullanımı DISPLAY komutu ile aynıdır. DISPLAY komutundan farkı ekran dolduğunda herhangi bir mesaj gelmez listeleme devam eder.

EDIT \[RECORD\] <kayıt numarası>

Anlamı :

Aktif olan bir kütükte istenilen bir kaydın veya devamının ekrana getirilip üzerinde değişiklik yapmak amacıyla kullanılır. EDIT RECORD komutu ile sadece o anki aktif kayıt üzerinde işlem yapılır diğer kayıtlara geçilmez.

RECALL \[<kayıt grubu>\] \[FOR <koşul>\] \[WHILE<koşul>\]

Anlamı :

Aktir durumdaki kütükte bulunan mantıksal silme işlemini ortadan kaldırmak için kullanılır. Silinmek üzere konulan \* işaretini kaldırır.

Örnek : Kişisel bir adres, telefon rehberi oluşturunuz. Rehberde bulunacak kayıtlar disk ortamında rehber.dbf kütüğünde yer alsın.

.create rehber (rehber.dbf kütüğü oluşturulur)

| Field NameDec |  |  |  |
| --- | --- | --- | --- |
| NO | Numeric | 6 | 0 |
| AD\_SOYAD | Character | 25 |  |
| DTARIH | Date | 8 |  |
| CINS | Character | 1 |  |
| ADRES | Character | 35 |  |
| SEMT | Character | 15 |  |
| SEHIR | Character | 15 |  |
| TEL | Character | 11 |  |

şeklinde kayıt alanlarını tanımlayınız. Şimdi kayıt girecek misiniz sorusuna evet yanıtını veriniz, 1 kayıt giriniz ve Esc tuşuna basıp kayıt girişinden çıkınız. Aşağıda verilen komutları yazarak sonuçlarını görünüz.

. list stru (kayıt yapısını ekrana getirir)

.append (tekrar kayıt girişine devam ediniz)

. modi stru ( TEL alanının uzunluğunu 12 yapınız, kaydediniz ve çıkınız)

. list stru (kayıt yapısını tekrar görünüz)

. list all (girilen bütün kayıtları listeler)

. display all

. list all no,ad\_soyad (sadece numara ve ad\_soyad bilgileri gelir)

. list all for cins="e" .or. cins="E" (cinsiyeti e ya da E olanların tüm bilgileri gelir)

. list all no, ad\_soyad for cins="e".or.cins="E"

(cinsiyeti e ya da E olanların no,ad\_soyad bilgileri gelir)

. list all ad\_soyad for recno()>2

(record no > 2 olan kayıtların ad\_soyad bilgileri gelir)

. list all off ad\_soyad, dtarih for recno()>3 while no<5

(no< 5 olmak üzere record no > 3 olan kayıtların ad\_soyad, doğum tarihi bilgileri gelir, record no bilgisi görüntülenmez)

. go top (kütüğün başına gidilir)

. edit

(ilk kayıt düzeltme için ekrana getirilir, sonraki kayıtlara geçilip düzeltme yapılabilir)

. edit record 5 (sadece 5.kayıtta düzeltme yapılır)

. go bottom (kütüğün sonuna gidilir)

. ? recno() (record no ekrana getirilir)

. skip -1 (bir kayıt geriye gidilir)

. skip (bir kayıt ileriye gidilir)

. ? eof() (kütük sonu ise .T. bilgisi ekrana gelir)

. append blank (kütüğün sonuna bir kayıt eklemek için giriş ekranı gelir)

. list all ad\_soyad,tel for ad\_soyad="M".or.ad\_soyad="m"

(ad\_soyad alanında ilk harfi m ya da M olan kayıtların ad\_soyad ve tel bilgileri gelir)

. list all for ad\_soyad=upper("m")

. browse (kayıtlarda düzeltme yapmak için girilen kayıtları ekrana getirir)

. browse fields ad\_soyad,dtarih,adres,semt,sehir lock 1

(ad\_soyad bilgisi solda sabit kalır, diğer alanlarda değişiklik yapılabilir)

. browse noappend (yeni kayıt girişi yapılmaz)

. browse noappend, nomenu (yeni kayıt girişi yapılamaz ve menü getirilmez)

. browse noappend, nomenu, width 10

(yukardaki komutla aynı işi yapar sadece karakter sahaların 10 karakterlik bilgisini ekrana getirir)

. browse freeze adres width 10

(tüm alanları ekrana getirir, karakter sahaların uzunluğu 10 karakterdir, sadece adres sahasında değişiklik yapılabilir)

. browse fields ad\_soyad (sadece ad\_soyad bilgisi değişiklik yapmak üzere getirilir)

. browse fields no,ad\_soyad,adres,semt freeze adres

(no, ad\_soyad, adres, semt bilgileri ekrana gelir sadece adres sahasında değişiklik yapılabilir)

. go top (ilk kayda gidilir)

. delete (ilk kayıt silinmek üzere işaretlenir)

. list all (tüm kayıtla listelenir silinmek üzere işaretlenen kayıtlarda \* işareti gösterilir)

. recall all (\* işaretleri kaldırılır)

. go 3 (3.kayda gidilir)

. delete (3.kayıt silinmek üzere işarerlenir)

. pack (3.kayıt fiziksel olarak silinir)

. delete all for ad-soyad="a"

(ad\_soyad alanının ilk karekteri a olan tüm kayıtları silinmek üzere işaretler)

. delete all for recno()>100 .and. cins="e"

(record no > 100 ve cins=e olan tüm kayıtları silmek üzere işaretler)

. delete all (tüm kayıtlar silinmek üzere işaretlenir)

. recall all for ad\_soyad="a"

(belirtilen koşula uyan ve silinmek üzere işaretlenen kayıtların silme işlemi iptal edilir)

. use (aktif kütüğü kapatalım)

. create tel

tel.dbf kütüğünü oluşturalım, kayıt yapısı aşağıdaki gibi olsun, bir kayıt girip çıkalım.

| Field Name | Type | Width | Dec |
| --- | --- | --- | --- |
| NO | Numeric | 6 | 0 |
| AD\_SOYAD | Character | 25 |  |
| TEL | Character | 11 |  |

. use tel (tel.dbf kütüğü aktif hale gelir)

. append from rehber

(rehber.dbf kütüğündeki tüm kayıtlar tel.dbf kütüğüne son kayıttan itibaren eklenir)

. list all

. append from rehber for ad\_soyad="M"

(rehber.dbf kütüğündeki ad\_soyad bilgisinin ilk harfi M olan kayıtlar tel.dbf kütüğünün sonuna eklenir)

DBASE'DE KULLANILAN FONKSİYONLAR

TIME () : Fonksiyonu sistem saatini verir.

.? time ()

DATE() : Fonksiyonu sistem tarihini verir.

.? date()

25/02/1996

CTOD() : Fonksiyonu karakter bilgiyi tarih bilgisine dönüştürmek için kullanılır. Date (Tarih Tipli Değişken) türünden bilgiler ile toplama, çıkarma işlemleri yapılabilir.

.tarih ="01-01-96"

.tarih=CTOD(tarih)

.? DT +20

. 01-21-96

Tarih tipli bilgiler de DTOD () fonksiyonu ile karakter türü bilgilere dönüştürülebilir.

.tarih=DTOD ("12-09-66")

.? tarih

CDOW() : Fonksiyonu belirtilen tarihin gün ismini verir.

.? CDOW(DATE())

.? CDOW(DATE()+1)

DAY() : Fonksiyonu belirtilen tarihin gün değerini verir.

.?DAY (DATE ())

MONTH() : Fonksiyonu belirtilen tarihin ay değerini verir.

.? MONTH (DATE())

YEAR() : Fonksiyonu belirtilen tarihin yıl değerini verir.

.? YEAR (DATE())

CMONT() : Fonksiyonu belirtilen tarihin ay ismini verir.

.? CMONTH (DATE ())

DOW() : Belirtilen tarihteki günün haftanın kaçıncı gün olduğunu verir. Pazar 1.gün kabul edilir.

.? DOW (Date())

Örnek : Hangi günde doğduğumuzu bulalım.

.A=CTOD ("12/09/66")

.GUN=DATE ()-A

.DT=DATE ()-GUN

.? CDOW (DT)

monday (pazartesi)

ASC(X) : X karekterine (veya karakter katarınının ilk karakterinin) karşılılık gelen ASCII değerini verir.

.?asc("N")

78

AT (Y, X) : Y karakter bilgisinin, X karakter bilgisinin içerisindeki pozisyonu verir. Eğer Y, X'in içinde yoksa sonuç 0 dir.

.? at ("a", "bilgisayar")

7

.? AT ("z", "bilgisayar")

0

.? AT ("sayar", "bilgisayar")

6

CHR (sayı) : ASCII kodu ile verilen sayının karakter karşılığını bulur.

.? chr(7) (düdük sesi çıkarır)

.? chr(66)

B

ISALPHA(X) : X karakter bilgisinin ilk harfinin bir harf olup olmadığını bulur. İlk karakter harf ise sonuç .T. olur

.? isalpha("b12sd")

.T.

? isalpha("12jjjj")

.F.

ISLOWER(X) : X karakter bilgisinin küçük harf olup olmadığını kontrol eder. Eğer küçük harf ise bu fonksiyonun sonucu '.T.' olur.

.? islower('M')

.F.

.? ISLOWER('leman')

.T.

ISUPPER(X) : X karakter bilgisinin büyük harf olup olmadığını kontrol eder. Eğer büyük harf ise bu fonksiyonun sonucu '.T.' olur.

.? isupper("deneme")

.F.

? isupper ("L")

.T.

LEFT(X, n) : X karakter bilgisinin soldan n tane karakterini alır.

.? left ("bilgisayar ",5)

bilgi

LEN (X) : X karekter bilgisin uzunluğunu verir.

.? LEN ("bilgisayar)

10

LOWER(X) : X karakter bilgisini küçük harfe dönüştürür.

.? lower("BİLGİSAYAR")

bilgisayar

.use <kütük-ismi> replace <alan-ismi> with upper(<alan-ismi>)

komutu, kütükteki bütün alan-ismi verilerini büyük harfe dönüştürür.

LTRIM (X) : X karakter bilgisinin başındaki boşlukları atar.

.? ltrim(" dede ")

dede

REPLICATE (X, n) : X karekter bilgisinden n tane üretir.

.? REPL ("\*",10)

\*\*\*\*\*\*\*\*\*\*

RIGHT (X, n) : X karakter bilgisinin sağından n tane karakterini alır

.? right ("bilgisayar",5)

sayar

RTRIM(X) : X karakter bilgisinin sonundaki boşlukları atar.

.? rtrim ("bilgisayar uygulamaları ")

bilgisayar uygulamaları

.ad=" Mehmet"

.soyad="Şahin "

.? rtrim(soyad)+" " ltrim(ad)

Şahin Mehmet

SPACE(n) : n tane boşluk karakteri üretir.

.L= "nn"+space(4)+"mm"

.? len(L)

6

.? L

nn mm

STUFF(X,n,m,Y) : X ile verilen karakter bilginin, n.konumundan itibaren m adet Y karakter bilgisini X e taşır.

.adı=stuff ("çarşı",1,1,"M")

.? adı

Marşı

SUBSTR (X,m,n) : X karakter bilgisinin m. konumundan n tane karakteri alır.

.? substr ("bilgisayar", 1,3)

bil

TRIM (X) : X karakter bilgisindeki gerekiz tüm boşlukları atar.

.ad=" Mehmet"

.soyad="Şahin "

.? trim(ad)+" "trim(soyad)

Mehmet Şahin

UPPER(X) : X karekter bilgisini büyük harfe dönüştürür.

.M="bilgisayar"

.? UPPER (M)

BİLGİSAYAR

ABS (n) : n sayının mutlak değerini alır.

.? abs (-3)

3

EXP(n) : Verilen n sayısına göre e^n değerini hesaplar

. ? exp(1)

2.718

INT(n) : n sayısının tam kısmını alır.

.? int (235.45)

235

LOG(n) : n sayısının logaritmasını alır.

.? log(10)

1

MAX(n,m) : n ve m ile verilen sayılardan hangisinin büyük olduğunu bulur.

.? max(4,8)

8

MIN(n,m) : n ve m ile verilen sayılardan hangisinin küçük olduğunu bulur.

.?min(4,8)

4

MOD(n,m) : n sayısının m sayısına bölümünden kalanı bulur.

.? mod(2,5)

2

. ? mod(14,13)

1

ROUND(n,m) : n ile verilen sayıyı m adet kesire yuvarlar.

.? round(3.3333333333333,4)

3.3333

SQRT(n) : n ile verilen pozitif sayının karakökünü alır.

.? sqrt(4)

2

STR (N, I, J) : Sayısal bilgiyi karaktere çevirir. I : tamsayı uzunluğunu, J : kesir uzunluğunu belirtir. I ve J belirtilmesse karakter bilginin uzunluğu 10 dur.

.L=6

.e=STR (L)

.? LEN (e)

10

.e=STR(L,1)

.? LEN (e)

1

VAL (X) : X karakter bilgisini sayısal bilgiye dönüştürür. Eğer X karekter bilgisinde hiç sayısal değer yoksa sonuç 0 olur.

.? val ("bilgisayar")

0

.L= "12"

.M="8"

.? val (K+B)

128

TYPE () : Fonsiyonu belirtilen değişkenin tip karakterini verir.

.B="123"

.? type ("B")

C (Karakter)

.A=8

.? type("A")

N (Numeric)

OS() : Sistemde çalışan Dos işletim sisteminin versiyonunu verir.

.? OS()

MS-DOS VERSION 5.0

ISCOLOR() : Monitör'ün renkli olup olmadığını test eder. Renkli ise bu fonksiyonun sonucu .T. olur.

GETENV() : Çevre tanımlarına ilişkin değerleri gösterir.

.? getenv('prompt')

$p$g

.? getenv ('path')

path= C:\\;C:\\dos;C:\\dbase

GETENV('COMSPEC') : Sistem açılırken command.com programın nereden çalıştığını gösterir.

DBF() : Aktif veri dosyasının ismini verir.

.? dbf()

rehber.dbf

LUPDATE() : Aktif olan dosyanın son kullanım tarihini verir.

RECCOUNT() : Aktif kütükteki kayıt sayısını verir.

DELETED() : Kayıtın silinmek üzere işaretlenip işaretlenmediğini verir. İşaretlenmiş ise .T. olur.

FILE () : Belirtilen ortamdaki belirtilen isimli kütüğün var olup olmadığını test eder. Eğer kütük varsa bu fonksiyonun sonucu .T. dır. Bu fonksiyon gizli ve sistem nitelikli kütüklerin de var olup olmadığını test eder.

. ? File (DBASE.EXE)

.T.

.? FILE (c:\\MSDOS.SYS)

.F.

F2 ....F10 Fonksiyon tuşlarına komut atanması

Set fonction 2..10 to "komut"

F2 ASSIST

F3 LIST

F4 DIR

F5 DISPLAY STRUCTURE

F6 DISPLAY STATUS

F7 DISPLAY MEMORY

F8 DISPLAY

F9 APPEND

F10 EDIT

.Set fonction 8 to "BROWSE"

Bu atama dbase ortamında çalışırken geçerlidir.

Aşağıdaki kütük yapısını dikkate alarak aşağıda verilecek komutları gözden geçirelim.

Kütük adı : SINIF.DBF

FIELD NAME TYPE WIDTH DEC

NO N 5 0

ISIM C 30

VIZE N 3 0

FINAL N 3 0

CINS C 1

YAS N 2 0

YIL D 8

SUM komutu : DBASE kütüğündeki istenilen nümerik alanların toplamının alınmasını sağlar.

Komutun genel kullanımı :

SUM \[<Çalışma alanı>\]\[<alan-listesi>\]

ALL

REST

NEXT n

\[FOR <Koşul>\]

\[WHILE <Koşul>\]

\[TO <degişken>\]

Sadece SUM komutu kullanılırsa kütükteki bütün nümerik alanların toplamı alınır ve sonuç ekrana yazılır.

ÖRNEK :

.USE SINIF

.SUM VIZE

.125

Vize toplamları bulunur.

ÖRNEK :

.SUM VIZE TO TOPLAM

.? TOPLAM

.125

Vize toplamları TOPLAM değişkenine atarılır.

ÖRNEK :

.SUM VIZE FOR CINS="K" TO TOPLAM

.? TOPLAM

.75

Kız öğrencilerin vize toplamları TOPLAM değişkenine atarılır.

ÖRNEK : Geriye kalan kayıtlardaki VIZE alanları toplamı.

.SUM REST VIZE

.75

ÖRNEK :

.Sum VIZE for Year(YIL)=1996.AND.CINS="E" TO TOPLAM

1996 yılında erkek öğrencilerin VIZE toplamı TOPLAM değişkenine aktarılır.

COUNT komutu : Belirtilen koşula uyan kayıtların sayısının bulunmasını sağlar.

Komutun genel kullanımı

COUNT \[<Çalışma alanı>\]\[<alan-listesi>\]

ALL

REST

NEXT n

\[FOR <Koşul>\]

\[WHILE <Koşul>\] \[TO <değişken>\]

ÖRNEK :

.USE SINIF

.COUNT FOR CINS="E"

Erkek öğrencilerin sayısını verir.

ÖRNEK :

.COUNT FOR VIZE=90.AND.CINS="K" TO SONUC

.? SONUC

Vizesi 90 olan kız öğrencilerin sayısını verir.

ÖRNEK :

.COUNT FOR (VIZE+FINAL)/2 >=60

VIZE ve FINAL ortlaması 60 dan büyük olan öğrencilerin sayısını verir.

AVERAGE komutu : Sayısal alanların avarajının (ortalamasının) alınmasını sağlar.

Komutun genel kullanımı

AVERAGE \[<Çalışma alanı>\]\[<alan-listesi>\]

ALL

REST

NEXT n

\[FOR <Koşul>\]

\[WHILE <Koşul>\]

\[TO <degişken>\]

Sadece average komutu verilirse bütün numerik alanların ayrı-ayrı ortalaması alınır ve ekrana yazılır.

ÖRNEKLER :

1) .USE SINIF

.AVER VIZE FINAL

Vize ve final ortalmaları bulunur.

2) .AVER FINAL VIZE TO FORT,VORT

Tüm öğrencilerin FINAL VE VIZE ortalamaları bulunur ve FORT, VORT değişkenlerine aktarılır.

3) .AVER FINAL FOR CINS="K"

Kız öğrencilerin FINAL ortalamaları bulunur.

4) .AVER YAS FOR CINS="E"

Erkek öğrencilerin YAS ortalamaları bulunur.

NOT : SUM, AVERAGE, COUNT komutları aktif kütüğün başından itibaren tüm kayıtları işleme alır.

KÜTÜK YAPISINI VE İSTENİLEN ALANLARI BELİRTİLEN BİR KÜTÜGÜN İÇERİSİNE KOPYALAMA :

COPY TO < yeni kütük ismi > \[<çalışma alanı >\]

\[fields <alan listesi>\]

\[for <koşul>\] \[while <koşul >\]

<type > \[<kütük tipi\]

Eğer copy to komutunda type belirtilmezse oluşan yeni kütügün uzantısı DBF olur. Kütük tipi olarak şunlar belirtilebilir

SDF : System data file (TXT uzantılı ASC file)

WKS : Lotus file formatı

DIF : Visicak

SYLK : Multiplan

ÖRNEK :

Aktif Database kütüğünün yapısını bütünüyle veya istenilen alanlarını başka kütük isminde Copy'lemek.

.USE SINIF

.COPY STRUCTURE TO SINIF1

.USE SINIF1

.LIST STRU

SINIF.DBF ile SINIF1.DBF kütüklerinin yapıları aynı

Bütün yapıyı değil de istediğimiz alanların yapısını copy'leyelim.

.USE SINIF

.COPY stru to SINIF1 fields ISIM,CINS,YAS

.USE SINIF1

.list stru

ÖRNEK :

SINIF.DBF kütüğündeki bütün kayıtları SINIF.TXT kütügü içerisine transfer edelim daha sonra bu kütügü type ederek içeriğini görüntüleyelim.

. use sınıf

.copy to sınıf1 type sdf

.type sın.txt

ÖRNEK :

Erkek ögrencilerin isim, vize, final bilgilerini ERK.DBF kütüğüne transfer edelim.

.use sınıf

.copy to erk fields isim,vize,final for cins="e".or.cins="E"

.use eb

.list

ÖRNEK : Tüm öğrencilerin isim, vize, final bilgilerini ERK.wks kütüğüne transfer edelim.

.use sınıf

.copy to sınıf2 fields isim,vize,final all type wks

Bu komutu uyguladıktan sonra Lotus programına girerek sınıf2.wks dosyasının içeriğini görünüz.

ÖRNEK : Aşağıda kayıt yapısı verilen personel.dbf kütüğünü oluşturun.

FIELD NAME TYPE WIDTH

SICIL N 5

ISIM C 30

BIRIMKOD N 2

SEMDKOD N 2

KAN C 5

UNVAN C 20

STATU N 1 ------ 0:Memur

GIZLI M 10 1:sözleşmeli

İBTAR D 5 2:işçi

ÖRNEKLER :

1- 5 kayıt giriniz

2- kütük yapısını ekrana listeleyiniz

3- kan gurubu ORH+ olan personellerin isim ve semt kod bilgilerini listeleyiniz

4- kütük yapısına tel C 20 alanını ekleyiniz

5- kütükte kaç sözleşmeli personel var bulunuz

6- İşe başlama tarihi 01.01.96'den önce olanların, isim, birim kod, ünvanı ve işe başlama tarihi listeleyiniz.

7- Birimi 02 olan personellerin isim ve gizli bilgilerini listeleyiniz

CEVAPLAR :

Create personel

1-Append

2-List structure

3-List isim, semdkod for kan="ORH+"

4-Modi stru

5-Count FOR STATU=1

6-List isim, birimkod, ünvan FOR ibtar<ctod("01/01/91")

7-List isim, gizli for bırımkod=02

BAZI ÖNEMLİ SET KOMUTLARI

SET ALTERNATE komutu :

SET ALTERNATE TO \[<dosya>\]

SET ALTERNATE ON/OFF

SET ALTERNATE TO LIST1 : Ekrana gelen çıktıları LIST1 isimli bir text dosyasına kaydeder. SET ALTERNATE ON komutu, bilgileri belirtilen dosyaya kayıt etmeye başlar. SET ALTERNATE OFF komutu, kayıt etme işini durdurur ve belirtilen text dosyasını açık durumda bırakır. SET ALTERNATE TO komutuyla açık durumdaki text dosyaları kapatılır.

Not : Bu komut yardımıyla bir DBASE dosyası bir text dosyasına çevrilir ve herhangi bir bilgisayar programlama dili ile kullanılabilir. Ayrıca bu dosyaya bir ediör ile ulaşılabilir.

SET DATE komutu :

SET DATE AMERICAN /ANSI / BRITISH / FRENCH / GERMAN / ITALIAN

SET DATE aşağıdaki formatları içerebilir.

AMERICAN : AA/GG/YY

ANSI : YY.AA.GG

BRITISH : GG/AA/YY

RENCH : GG/AA/YY

GERMAN : GG.AA.YY

ITALIAN : GG-AA-YY

SET DECIMALS komutu :

SET DECIMALS TO <sayısal değer>

Sayısal değerlerde ondalık hane sayısını belirler.

SET DEFAULT komutu :

SET DEFAULT TO <sürücü ismi>

Dbase işlemlerinin yapıldığı sürüyü belirler. Dbase için aktif sürücüyü seçer.

SET FILTER komutu :

SET FILTER TO \[<koşul>\] / \[FILE <dosya adı>\]

Aktif dosyadaki sadece belirtilen koşula uyan kayıtların kullanılmasını sağlar. Yalnızca verilen koşulu sağlayan kyıtlar elekten geçirilir. Filtre seçildikten sonra, verilen koşulu sağlayan ilk kayda gitmek için GO TOP komutu kullanılır. SET FILTER TO komutu aktif filtreyi kapatır.

ÖRNEK : Aşağıda verilen komutları deneyerek filtreleme işlemini görünüz.

.USE SINIF

.LIST

.SET FILTER TO VIZE > 60

.GO TOP

.LIST

.SET FILTER TO

.LIST

SET MEMOWIDTH komutu :

SET MEMOWIDTH <sayı>

Memo türünden sahalarıngörüntüleme genişliklerini verilen sayı kadar değiştirir. Normal değer 50 dir.

SET PATH komutu :

SET PATH TO \[<directory listesi>\]

Bulunulan directory'de aranılan dosyalar bulunamaz ise verilen directory listesindeki directory'lere bakılır.

ÖRNEK:

.SET PATH TO C:\\DBASE\\KUTUKLER;C:\\DATA;C:\\

İlkönce bulunulan directory sonra C:\\DBASE\\KUTUKLER directorysine daha sonra C:\\DATA directory'sine daha sonrada ana directory'ye bakılır.

BAZI SET ON/OFF KOMUTLARI

SET <DURUM> PARAMETRE (ON VEYA OFF) : ON komutun aktif hale getirilmesini OFF kaldırılmasını sağlar.

SET BELL ON : Ekran zilini aktif hale getirir.

SET CARRY ON : Son kayıttan bir sonraki kayda bilgi getirir.

SET CENTURY ON : Tarih görüntülemede yıl bölümünü 4 hane olarak getirir.

SET DELETED ON : Silinmek üzere işaretlenen kayıtları işlemlerde dikkate almaz.

SET EXACT ON : Karaktersel saha karşılaştırmalarında eşitlik durumu için iki sahanın da aynı olmasını zorunlu kılar. Set Exact normalde OFF'dur.Yani kesin eşitlik aramaz. Set Exact ON yapılırsa karakter bilgilerin karşılıklı karakterleri birbirine eşit olmalıdır.

SET HEADING ON : LIST ve DISPLAY işlemleri sırasında saha başlıklarını görüntüler.

SET HELP ON : Bir hata yapıldığında yardım istiyor musunuz? sorusunu sorar.

SET MENUS ON : Tüm ekran komutlarının icrası sırasında, yardım menülerini ekrana getirir.

SET SAFETY ON : Mevcut bir dosya oluşturulmak istendiğinde, bu dosyanın var olduğu kullanıcıya hatırlatılır.

SET SCOREBOARD ON : Durum satırını görüntüler. (en üst satır veya en alt satır). Capslock, insert, numlock gibi tuşların ekranda aktif olup olmadığını gösterir.

SET STATUS ON : Durum satırını görüntüler.

SET TALK ON : komutların sonuçlarını ekrana görüntüler.

KÜTÜKLERİN SEÇİLEN ANAHTARA GÖRE İNDEXLENMESİ

INDEX komutu :

INDEX ON <anahtar ifade> TO <indekx dosya adı> \[UNIQUE\]

Indexleme : Aktif durumdaki veri dosyasından bir indeks dosyası oluşturur. İndeks kullanımı ile sahalar alfabetik, kronolejik ve sayısal olarak sıralanabilirler. Kütüğün içeresindeki kayıtlara daha kolay erişilmesi sağlanır. Indexleme kayıtlara kolay erişilmesini sağlayan bir anahtar kütügün oluşturulması işlemidir. Logic ve memo alanları üzerine index kurulamaz. Kütüğün indexlenmesi işlemi sona erince .NDX uzantılı index anahtar değerlerini tutan bir kütük oluşturulur.

ÖRNEK :

Personel kütüğünü isim alanına göre PISIM.NDX kütügü üzerine indexleyelim.

.INDEX ON ISIM TO PISIM

Index anahtarı farklı tiplerden alanaların birleşiminden oluşacaksa bu alanları hepsi karakter tipli bilgiye dönüştürülmelidir ve alanlar arasına "+" karakteri konulmalıdır (karakter bilgilerin birleştirilmesi işlemi).

Indexleme işinden sonra hem DBF hem de NDX kütügü aktiftir

Bir DBF kütüğü başına aynı anda 7 açık index kütügü bulundurulabilir.

Index kütüğü aktifken yeni kayıt girişleri yapılırsa bu kayıtlar anahtara göre bulunmaları gereken pozisyona yerleşirler.

Index kütükleri aktifken yapılan bir günceleştirme işlemi bütün NDX kütüklerine yansıtılır.

REINDEX komutu açık olan bütün index kütüklerinde yeniden indexleme işlemini başlatır.

Index kütüklerini kapatmak için CLOSE INDEX komutu verilmelidir eğer DBF kütüğü kapatılırsa buna bağlı diğer index kütükler de otomatik olarak kapatılır.

İNDEXLİ KÜTÜKLERİN AKTİF HALE GETİRİLMESİ

PERSONEL.DBF

PISIM.NDX

.USE PERSONEL INDEX PISIM

Eğer birden fazla indexed file aktif hale getirilecekse

.use <dbf> \[index\] \[index file 1\] \[index file 2\] \[..7\]

INDEXED KÜTÜKLERİN AKTİF HALE GETİRİLMESİNİN

DİGER BİR YOLU

.USE PERSONEL

.set index to pisim

vaya genel olarak

.set index to <index 1> < index 2> ....

Index kütükleri aktif hale getirme komutlarından sonra MASTER index (birinci index ) kütük ilk belirtilen index kütüktür. Master index kütügünü değiştirmek için SET ORDER TO n (N=1 .. 7 ) komutu kullanılır.

Hangi index kütüğün isminin ne olduğunu öğrenmek istersek NDX(n) fonksiyonunu kullanabiliriz.

.? NDX(1)

.C:\\dbase\\pisim.ndx

ÖRNEK :

.use personel

.index on birimkod to birim (birim.NDX oluşur)

. set ındex to pisim, birim

master index pisim.NDX

. set order to 2

master index birim.NDX olur.

UNIQUE INDEX OLUŞTURMA

.Index on < anahtar > to <index> unique

Bu indexten sonra aynı değerli index anahtar kayıtlarından yalnız ilk kayıtlar alınır.

Unigue index kurma işlemini set komutuyla da sağlayabiliriz.

.Set Unique OFF/ON

Normalde Unique off durumundadır.

Anahtar bilgisi sadece tarih tipli bir bilgi ise bu tarihin karaktere dönüştürülmesi gerekmez fakat tarih ve isim alanlarına göre index kurulacaksa tarih karaktere dönüştürülmelidir.

ÖRNEK

.Use Personel

.Index on Str(Year(IBTAR),4)+str(month(IBTAR),2)+str(Day(IBTAR,2))+ISIM

TO IBISIM.NDX

01/01/91 --> Daha büyüktür. 91 01 01

12/31/80

80 31 12

KÜTÜKLERİN İSTENİLEN ALANLARI GÖRE SORT (sıralama) EDİLMESİ

En fazla 10 alana göre sort işlemi yapılabilir. Sort işleminin sonucunda oluşturulan yeni tütüğün uzantısı DBF'dir. Logic ve Memo alanlarında sort işlemi yapılamaz. Sort işlemi Azalan veya Artan şekilde yapılabilir. Sort işleminin sonunda kayıtların orjinal kayıt numaraları korunmaz. Yani kayıt numaraları 1,2,3,... şeklinde devam eder. (İndexed kütüklerde index işleminden sonra kayıtların orjinal numaraları korunur.) Sort işlemini küçük, büyük harf gözetmeksizin yapabiliriz.

SORT komutu :

SORT TO <yeni dosya adı> ON <alan -1>

\[/A\] \[/D\] \[/C\], \[<Alan -2>\] \[/A\] \[/D\] \[/C\]

.....

\[FOR <koşul>\]

\[WHILE <koşul>\]

\[çalışma alanı\]

Anahtar alanlarının arasına virgül karekteri konur. Alan bilgilerinde tip dönüşümüne gerek yoktur. Alan isminden sonra istenirse A,D,C seçenekleri belirtilebilir.

A: Ascending (artan sort)

D: Descending (azalan sort)

C: Büyük, küçük harf gözetmeden sort

ÖRNEKLER:

1) SINIF kütügünü ISIM alanına göre Z den A ya SINIF4.DBF kütügü üzerine sort edelim.

.Use sınıf

.sort to sınıf4 on ısım /D

.use sınıf4

.list

2) SINIF kütügünü NO alanına ONO.DBF kütügü üzerine sort edelim (küçükten büyüğe doğru)

.use sınıf

.Sort to ONO on stok no /A

.Use ono

.list

3) Sınıf kütügünü cinsiyet ve isim alanına güre CI.DBF kütügü üzerine sort edelim. Fakat isimlerde küçük, büyük harf gözetimi yapılmasın

.use sınıf

.sort to CI on cıns, isim /c

.use CI

.list

4) İsmi A ile başlayanları cınsıyet ve isim alanlarına göre AAD.DBF kütügü üzerine sort edelim.

.use sınıf

.sort to aad on cıns, ısım /A for ısım="A"

.USE Aad

.LIST

DBASE Programlama Dilinde Program Yazımı

Dbase komutları .prg (program) kütükleri aracılığıyla da çalıştırılabilir. Şimdiye kadar kullanılan komutlar, fonksiyonlar program kütükleri içerisinde de kullanılabilirler ve .prg kütüklerinin içine aynı şekilde yazılırlar. Bunlara ek olarak Dbase veri üzerinde daha fazla kontrolü sağlayan ve yalnızca .prg kütükleri içinde kullanılan komutlara sahiptir. Program kütüklerinin kullanım nedenlerinden en önemlisi zamandan kazanç sağlanmasıdır. Bir kere yazılan bir program istenilen anda sadece Do program-adı komutuyla çalıştırılabilir ve aynı komutların tekrar yazılmasına gerek kalmaz. Dbase, diğer programlama dillerinin sağladığı programlama komutlarına benzer komutlara sahiptir. Dbase programlarının uzantısı PRG'dir. Dbase programları herhangi bir editör yardımıyla oluşturulabilir. Dbase paketinin kendi edötürü 5 KB'lik bir yazım alanına sahiptir. Bu durumda kendi editöründe büyük programlar yazılamaz. Bir Dbase programı do <prg ismi> komutu ile çalıştırılır. Program yazarken küçük büyük harf farkı gözetilmez. Açıklama satırı belirtmek için satırın başına bir \* karekteri konulması yeterlidir. Uzun yazılan komutları bir sonraki satırdan devam etmek için satırın sonuna , karakteri konulmalıdır. Açıklama belirtmek için NOTE ...... açıklama komutu kullanılır. Programı saklamak için Ctrl-W tusları kullanılır.

.Prompt'unda (nokta iletisi) iken program yazım editörüne Modify command <prg ismi> kısaca modi com <prg ismi> komutu yazılarak girilir.

Programlama komutları : Bu komutlar şunlardır;

DO WHILE .... ENDDO

IF ..... ELSE ...... ENDIF

DO CASE ..... ENDCASE

ON komutu

Sayılan komutların ortak yanı, verilen bir koşulun sağlanması üzerine bazı komutların çalıştırılmasıdır.

Do while <koşul> Enddo komutu: verilen koşul sağlandığı sürece DO-ENDDO arasında yazılan komutları tekrar tekrar çalıştırır. Bu tekrarlanma işlemi döngü verilen koşul sağlanmadığı an durur. Komutun genel formu aşağıdaki gibidir.

Do while < koşul >

< komutlar > \[EXIT\] \[LOOP\] \[RETURN\]

Enddo

Do while deyiminin önündeki koşul doğruysa Do while / Enddo arasındaki deyimler işletilir. Koşul yanlış duruma düştüğünde işleyiş Enddo deyiminden sonraki deyimden devam eder. Do While / Enddo döngüsünden isteğe bağlı olarak Exit deyimi ile çıkılabilir. Exit programın çalışmasını durdurmaz. Do while / End do döngüsü içerisinde döngüyü başa döndürmek için Loop komutu kullanılır. İç-içe Do While / Enddo döngüleri kullanılabilir. Fakat döngüler birbirlerini kesmeyecek şekilde kapatılmalıdır. Return komutu programı çağrıldığı yere geri döndürür.

Sonsuz döngü yapısı

Do while .T.

< deyimler > ENDDO

Sonsuz bir döngü yapısıdır. Bu döngüden döngü dışına Exit deyimiyle çıkılabilir. Programı sona erdirmek için Return veya Cancel deyimleri kullanılabilir. Return Programı çağrıldığı yere gere döndürür. CANCEL ise nokta iletisine döndürür. Bütün dosyalar kapatılır.

Örnek : USE OGRENCI

DO WHILE .NOT.EOF()

? OGR\_NO, OGR\_AD\_SOYAD, OGR\_BOLUM

SKIP

ENDDO

Örnek : X=0

DO WHILE .T.

X=X+1

? X

IF X=10

EXIT

ENDIF

ENDDO

? "Sonuç=", X

RETURN

Örnek : USE OGRENCI INDEX OGRISIM

DO WHILE .T.

CLEAR

@ 10,10 SAY "ARANAN KİŞİNİN İSMİ=" GET ISIM

READ

IF ISIM=" "

EXIT

ENDIF

ISIM=TRIM(ISIM)

FIND &ISIM

IF.NOT.FOUND()

@ 20,2 SAY "ARANAN BULUNAMADI"

LOOP

ELSE

@ 14, 2 SAY "ARANAN BULUNDU"

? ISIM, SOYAD, BOLUM

ENDIF

ENDDO

Örnek : IF INKEY()=13

CLEAR

CLEAR ALL

CLOSE ALL

CANCEL

ENDIF

CLEAR komutunun genel formu aşağıdaki şekildedir;

CLEAR \[ALL/GETS/MEMORYTYPEAHEAD\]

Bu komut ekranı siler. CLEAR ALL komutu bütün açık veri dosyalarını kapatır, bütün hafıza değişkenlerini boşaltır. CLEAR GETS, @ ... GET komutunda READ ile okunan değişkenleri boşaltır. CLEAR MEMORY, bütün hafıza değişkenlerini boşaltır. CLEAR TYPEAHEAD, klavye buffer'ını boşaltır.

CLOSE ALL komutu : Açık durumda bulunan bütün dosyaları kapatır.

INKEY() komutu: Klavyeden basılan tuşun ASCII karakter kodunu klavye buffer'ına aktarır.

Örnek : USE MUSTERI

LOCATE FOR MUSNO="5555"

DO WHILE FOUND()

? MUSNO, VERGINO, BORCU

CONTINUE

ENDDO

LOCATE komutunun genel formu aşağıdaki gibidir.

LOCATE \[<kayıt seçimi>\] \[FOR <koşul>\] \[WHILE <koşul>\]

Aktif veri dosyasında verilen koşulları sağlayan ilk kayıt için arama yapar. CONTINUE komutu sözkonusu koşula uyan bir sonraki kayıt için arama yapar. Eğer böyle bir kayıt bulunduysa FOUND() fonksiyonu .T. aksi durumda .F. değerini verir.

Örnek : USE MUSTERI

LOCATE ALL FOR "MEHMET" $ ISIM

Bu komut musteri.dbf kütüğünde ISIM alanı içerisinde "MEHMET" olan tüm kayıtları arar. MEHMETALİ, MEHMET EMİN, MEHMETOĞLU,... gibi. Bu komut

LIST ISIM, MUSNO ALL FOR "MEHMET" $ ISIM

DISPLAY ISIM,MUSNO ALL FOR "MEHMET" $ ISIM

biçiminde de kullanılabilir.

DO CASE / ENDCASE komutu: Bu yapı bir çok if-endif kullanılmasına alternatif bir yapıdır. Her do case endcase ile bitirilmelidir.

do case

case I=1

"deyimler"

case I=2

"deyimler"

case I=3

"deyimler"

otherwise

end case

Örnek: Ekrandan bir yas giriniz. Yas 100 ise program sona ersin, yaş 0 ile 3 arasında ise bebeksin, 3-7 çocuksun, 7-17 gençsin, 17-30 yolun yarısı mesajlarını versin

Set talk off

do while.t.

Store 0 to YAS

clear

@ 1,1 say "YAŞINIZ ="get YAS Pict "ggg"

read

if YAS=100

clear

return

endif

do case

case Yas <=3

@ 2,1 say "... Bebeksin...."

case Yas <=7

@ 3,2 say "...Çocuksun.."

case Yas <=17

@ 2,0 say "..Gençsin.."

case Yas <=30

@ 2,0 say "...Yolun yarısı"

otherwise

@ 2,0 say "bir sozum yok"

end case

@ 20,0 say "xxxxx.bir tuşsa basınız xxxxx"

wait " "

enddo

Do case / Endcase arasından mümkün olan koşulların irdelenmesi case ile yapılır. Diğer herhangi bir durum otherwise ile denetlenir.

STORE komutunun genel formu;

STORE <değer> TO <değişkenler listesi>

Bu komut hafıza değişkenlerini tanımlar ve başlangıç olarak bir değer verir.

STORE 0 to TOPLAM, SAYAC

STORE CTOD("01/01/99") TO TARIH

WAIT komutunun genel formu;

WAIT \[<karaktersel ifade>\] \[TO <karaktersel hafıza değişkeni>\]

Dbase'in çalışmasını herhangi bir tuşa basılıncaya kadar durdurur. \[<karaktersel ifade>\], herhangi bir karaktersel ifadedir. Bu seçenek kullanılmazsa

Press any key to continue

mesajı gelir. Hafıza değişkeni, kullanıcının gireceği değeri içerir.

Örnek : WAIT "Devam mı? (E/H)" TO CEV

IF UPPER(CEV)="H"

RETURN

ENDIF

IF-ELSE-ENDIF komutunun genel formu;

IF <koşul>

<komutlar>

\[ELSE

<komutlar>\]

ENDIF

Komutların belirli koşullar sağlandığında çalışmasını sağlar. Eğer koşul doğru ise (.T.) ilk kısımdaki komutlar çalışır. Eğer koşul yanlış ise (.F.) ve ELSE seçeneği kullanılmışsa ikinci kısımdaki komutlar çalıştırılır. Aksi durumda program akışı ENDIF den sonra devam eder.

Örnek: Ekrandan abone nosu, isim, tüketim miktarı, abone türü giriliyor. Abone türü 1 ise konut, 2 ise sanayi anlaşılacaktır. Tüketim miktarı ise m3-ton su değeridir. Program Abone numarası boş geçildiğinde sona erecektir. Konutlardan ilk 30 m3 için 30 TL, fazlası için 400 TL sanayi için ilk 20 m3 için 400 TL fazlası için 500 TL alınacaktır. Buna göre her abonenin ödeyeceği bedeli ve sonuçta toplam abonelerden ne kadar para alınacağını ekrana yazdırınız.

Set talk off

topucr = 0

do while .t.

store 0 to ano, atur, tuk

store space(30) to isim

clear

@ 2,2 say "abaone no:" get ano

read

if ano = 0

exit

endif

@ 4,2 say "isim :" get isim

@ 5,2 say "tuketim:" get tuk

@ 6,2 say " turu :" get atur range 1,2

read

if atur=1

if tuk <= 30

b= tuk \* 300

else

b= 900 +(tuk-30)\*500

endif

else

if tuk <= 20

b=tuk \* 400

else

b=8000+(tuk-20)\* 500

endif

endif

?? chr(7)

@ 20,1 say "bedel :"+ str(b)

topucr=topucr+b

@ 22,1 say "bir tus "

wait " "

enddo

clear

@ 1,1 say "toplam ucret :"+str(topucr)

Çabuk IF fonksiyonu;

<Degişken >= IIF(<mantiksal ifade>,<deger-1 >, <değer-2>

Eger mantıksal ifade doğru ise değişkene değer-1 atanir. Mantıksal ifade yanlış ise değer-2 atanir.

Örnek : Aşağıdaki program parçası aynı işi yapar

a) if sec=1

satir =18

else

satir=36

endif

b) Satir =IIF(sec=1,18,36)

GET - READ - SAY - KOMUTLARI

@... GET komutu verilen koordinatlarla ekrandan değer almak için kullanılır. Genel formu;

@ <sat>, <sut> GET <değişken> \[PICTURE <format>\]

\[RANGE <altlimit>, <üstlimit>\]

değişken sahayı sat ve sut ile verilen koordinatlarda gösterir ve READ komutuyla bu koordinatlardan sahanın değerini alır.

Sat: satır (0-24) arası, Sut :sütun (0-79) arası.

PICTURE :Görünüm biçimi

RANGE : Girilebilecek enküçük ve enbüyük değerler. (Sayısal ve tarih alanları için kullanılır.

Ekrandan alınan değerler dbase tarafından geçici bir sahada depolanır. Bu değerleri ancak READ komutu verilirse elde edilir.

Örnek : @ 20, 40 GET SECIM PICT "!"

21.satır, 41.sütunda SECIM sahasının içeriğini gösterir. Daha önceden SECIM sahası tanımlanmamışsa hata verir. (SECIM=" " yazılmalıdır)

@ 20, 40 GET SECIM PICT "!"

READ

21.satır, 41.sütunda SECIM sahasının içeriğini gösterir ve bu sahanın yeni değerini ekrandan almamızı sağlar.

Örnek : sayı=0

@ 19,45 get sayı pict "99999" range 0,49999

0 ile 49999 arasındaki sayılar dışındaki sayıların girişine izin verilmez.

Get-Read komutu yapısı:

Ekran ortamından değişkenler içerisine bilgi okumasını sağlar. Önce bilgi girilecek değişkenlerin get edilmesi gerekir, arkasından Read deyimiyle değer girişine başlanır. Normalde bir READ Deyimi 128 tane get edilmiş değişkenin içerisine bilgi girilmesini sağlar.

@ ... SAY komutu:

Ekrana sabit veya değişkenlerin değerlerini yazdırır. Hem get hemde say komutlarında ekran koordinatları sat, sut ifadesiyle belirtilir. İlk değer satırı ikinci değer sutünu ifade eder. Genel formu;

@ <sat>, <sut> \[SAY <değişken / karakter bilgi> \[PICTURE <format>\]\]

Sahayı sat ve sut ile verilen koordinatlarla görüntüle. PICTURE, görünüm şekli. SAY yazılmazsa verilen koordinatlardan itibaren ekranı siler.

secim="E"

@ 20, 40 say SECIM PICT "!"

21.satır, 41.sütunda SECIM sahasının içeriğini gösterir.

Örnek : use STOK

clear

@ 1,1 TO 23,78 DOUBLE

@ 2,2 SAY "STOK NO =" GET S\_NO RANGE 1,1000

@ 3,2 SAY "STOK ADI = " GET S\_AD

READ

Örnek : Değişkenler içerisine değer okuma (Get-Read)

. modi comm oku.prg ( PROGRAM yazım editörüne girmek için)

isim= Space (30)

adres = Space (40)

yas = 0

Clear

@ 2, 2 say "İsim Giriniz :" get isim

@ 4, 2 say "Adres giriniz:" get adres

@ 6, 2 say "Yaşınız :" get yas

read

Clear

? isim

? adres

? yas

Ctrl-W (programı saklamak için)

do oku (programın çalıştırılması için)

Alıştırma : Ekrandan öğrencinin numarasını, ismini vize1, vize2 ve final notlarını okuyunuz. Daha sonra öğrencinin geçme notunu hesaplayıp ekrana yazdırınız. Öğrenci nosu boş geçildiğinde program sona ersin.

Örnek Program : Ekrandan Personel ismi, netmaaşı, ekgeliri ve verdiği fatura miktarını giriniz. Buna göre personelin alacağı vergi iadesini hesaplayınız. Program, isim boş girildiğinde son bulsun.

Set talk off

clear

@ 0,0 say "KDV İadesi Hesabı"

@ 1,0 to 24,79

do while.t.

store 0 to net, VFM,EK

isim = space(30)

@ 3,2 say "Personel ismi :" get isim pict "@!"

read

if isim=space(30)

clear

return

endif

@ 5,2 say "Net Ucreti:" get net pict "@z 9,999,999"

@ 6,2 say " Ek geliri :" grt ek pict "@z 9,999,999"

@ 7,2 "verdigi fatura:" get VFM pict "@ 99,999,999"

read

if VFM>=Net+ek

esas =net+ek

else

esas=VFM

endif

do case

case esas<=60.000

Iade=Esas\*20

case esas<=120.000

Iade= 12.000+(Esas-60.000)\*12

case Esas <=200.000

Iade= 19.200+(Esas-200.000)\*.005

otherwise

Iade=27.200+(Esas-200.000)\*.005

end case

?? chr(7)

@ 20,2 Say " İade="+transform (Iade "9.999.999)+"TL"

@ 22,2 Say "\*Bir tuşa basınız!"

wait " "

@ 2,1 clear to 23,78

enddo

PICTURE SEMBOLLERİ

Değişkenlere okunan değerlerin hangi formatlarda okunacağını gösterir. Bu semboller 9, #, A, L, Y, N, X, !, $, \*, . , , dır. Bu semboller SAY ve GET komutları ile birlikte kullanılır. Bu semboller tırnak içinde ve değer uzunluğunda verilmelidir.

9 : Sayısal değer ve başında +, - kabul eder

\# : Sayısal değer, +, - space (boşluk) kabul eder

A : Alfabetik karakterleri kabul eder

L : Sadece mantıksal değerleri kabul eder ( Y, N, T, F)

Y : Mantıksal değerlerden sadece Y ve N kabul eder

N : Harf, sayısal +, - kabul eder

X : Herşey girilebilir

! : Girilen karakteri büyük harfe çevirir

$ : Sayısal değerlerin başına $ işareti koyar

\* : Sayısal değerlerin başındaki boş yere \* karakterleri koyar

. : Bulunduğu yere . işareti koyar

, : Bulunduğu yere , işareti koyar

SAYI =123.456

@ 10,10 SAY TOPLAM PICT "9999.9"

işleminin sonucunda TOPLAM=123.4 olur.

Not : @ komutu PICTURE nin yanısıra FUNCTION kullanabilir. Bu fonksiyonlar ve anlamları aşağıda verilmiştir.

C: Pozitif sayılardan sonra CR (credit) koy

X: Negatif sayılardan sonra DB (debi) koy

(: Negatif sayıları paranteze al

B : Sayısal bilgiyi ekrana yazarken sola yanaştır

Z: Seğer sıfır ise araya space (boşluk) koy

D: (date için) Amerikan sistemi yazar

E: (date için) Avrupa sistemi yazar

A: Picture deki işlemi yapar

! : Picture deki işlemi yapar

Örnek : sayi = 1987

@ 1, 10 get sayı function "B"

S <n> : Get sahaları için saha sınırlaması yapar

acıklama=space(30)

@ 10 ,10 get acıklama function "S15"

Acıklama değişkeni 30 byte buyuklugundedir. Ancak yukardaki komut verildiğinde ekranda 15 karakterlik yer açılır. Ve 15 karakterlik yer dolduktan sonra yazı sola kayar ve ekrandan tasarruf sağlanır.

TEXT - ENDTEXT komutu : Bu deyim ile ENDTEXT cümlesi arasında yazılanların tamamı ekrana yazılır Amaç açıklayıcı bilgilerin ekrana yansıtılmasıdır.

TEXT

açıklayıcı bilgiler

ENDTEXT

ON ERROR <komutlar>

ON ESCAPE <komutlar>

ON ERROR RETURN : Hata oluştuğunda çağrıldığın yere don.

ON ERROR QUIT : Hata olduğunda DOS a dön

ON ERROR DO <PRG ADI> Hata olduğunda programı çalıştır

ON ESCAPE ( kullanmak için set escape on olmalıdır)

örnek : on escape @ 23,1 say "lütfen escape tuşuna basmayınız"

ACCEPT komutu nun genel formu;

ACCEPT \[<karaktersel ifade>\] TO <karaktersel-hafıza değişkeni>

Klavye ile girilen değeri <karaktersel-hafıza değişkeni> nin içinde saklar. <karaktersel- ifade> seçeneği kullanılırsa, saklama işleminden önce dbase onu ekranda görüntüler.

ACCEPT "İSİM GİRİNİZ=" TO ISIM

ACCEPT "SECİM =" TO SECIM

gibi.

INPUT komutu nun genel formu;

INPUT \[<karaktersel ifade>\] TO <SAYISAL-hafıza değişkeni>

Klavye ile girilen değeri <SAYISAL-hafıza değişkeni> nin içinde saklar. <karaktersel- ifade> seçeneği kullanılırsa, saklama işleminden önce dbase onu ekranda görüntüler.

INPUT "TOPLAM GİRİNİZ=" TO ISIM

INPUT "SECİMİNİZ =" TO SECIM

gibi.

Accept ile kararter tipli değerler, input ile sayısal tipli değerler okunur.

İNDEXLİ KÜTÜKLERDE ERİŞİM İÇİN NOTLAR

FIND komutu:

FIND <karaktersel ifade>

İndexli bir dosyada anahtar sahaya göre kayıtların çok hızlı bir şekilde aranmasını sağlar. FIND, karaktersel ifadeyi içeren ilk kayda konumlanır. Karaktersel ifadenin tırnak (" ") içinde verilmesine gerek yoktur. Karaktersel ifade tırnak arasına alınmayabilir. Bundan dolayı anahtar sahayı değişken olarak kullanabilmek için & kullanılır.

Örnek: USE TELEFON INDEX ISIM

FIND AHMET

Örnek : USE TELEFON INDEX ISIM

CLEAR

SAHA=SPACE(30)

@ 10,10 SAY "ARANAN ISIM=",SAHA

READ

SAHA=TRIM(SAHA)

FIND "&SAHA"

SEEK komutu :

SEEK <anahtar ifade>

İndexli veri dosyasında anahtar saha için verilen <anahtar-ifade> ile hızlı aramaya imkan sağlar.

Örnek : USE TELEFON

SEEK "ÖZBEK"

? RECNO()

IF EOF()

? "BULUNAMADI"

ENDIF

ARA=SPACE(20)

ACCEPT "ARANAN SOYADI GİRİNİZ" TO ARA

ARA = TRIM(ARA)

SEEK ARA

? RECNO()

IF EOF()

? "BULUNAMADI"

ENDIF

Not : (FIND ve SEEK): Bu komutlar indexli kütüklerde hızlı erişmeyi sağlar. Erişim index anahtarı üzerinden gerçekleşmelidir. Karakter indexli kayıtlara erişim için FIND komutu sayısal indexli kayıtlara erişmek için SEEK komutu kullanılır. Aslında her iki komutla da bu iki türden kayıtlara erişmek mümkündür.

Örnek : USE OGRENCI

INDEX ON OGRISIM TO ISIMDNX

a) FIND "A"

ismi A ile başlayan kayda erişilir. Eğer set exact on durumunda olsaydı ALİ isimli kayıt bulunamazdı.

b) Erişimde değişken kullanılmak istenirse

B="ALİ"

FIND &B

komutu yazılır. & karakteri macro karakteridir. Yani bir değerin içeriğini temsil eder. Bu komut FIND ALİ ile eşdeğerdir.

Aynı arama işlemi SEEK komutuyla da yapılabilir

SEEK "ALİ"

Örnek (macro kullanımı):

.ISIM ="LEVENT"

? "ÖZBEK &ISIM"

komutu yazılırsa sonuç ÖZBEK LEVENT olur.

Örnek :

.use ogrenci

. index on osym to osymndx

SEEK 500 ( osym puanı 500 olan kayda erişilir)

veya

.puan=500

.seek puan

FIND komutuyla erişmek için

.puan=500

.puan=ltrim(str(puan))

.find &puan

komutları kullanılır.

SELECT komutu;

SELECT <çalışma alanı>

Aktif veri dosyasını açmak veya seçmek için çalışma alanı seçilir. Çekmece seçimi. 10 çalışma alanı verdır, her birinin kayıt işaretleyicisi birbirinden bağımsızdır.

Örnek: SELECT 1

USE MUSTERI

SELE 2

USE STOK

Örnek :

SELE 1

USE MUSTERI INDEX MUSIND

SELE 2

USE FATURA INDEX FATNO,TARIH,MUSNO

SELE 3

USE STOK

INDEX STKIND

REPLACE komutunun genel yapısı:

Replace \[ <kayıt seçimi>\] <saha> WITH <değer>,

\[, <saha2> WITH <değer2> ...\] \[FOR <koşul>\]

\[WHILE <koşul>\]

Aktif dosyada belirlenen sahaların içeriklerini değiştirir. FOR/WHILE koşul cümleleri kullanılmadığı durumda yalnızca o andaki kayıt etkilenir.

Örnekler :

.Use Emlak

.Replace all isim with lower(isim) (dosyadaki bütün isimler küçük harfe dönüşür)

.Use Personel

.Replace All maas with maas+2500000 (Bütün maaşlara 2500000 eklenir)

.Use Sinif

. Repl all Final with 0 For vize<40

. repleca toplam with 100\*sayi, acıklama with " \*\*\*\*\*\* "

DBASE Programlarının Debug edilmesi, Adım-adım çalıştırılması

Set echo on/off

Eğer set echo on yapılırsa çalışan satırlar ekrana sergilenir. Set step on yapılırsa çalışan satır adım-adım sergilenir, space bar tuşuna basınca program adım adım çalışır. S tusuna basılırsa Suspend edilir (biran durdurulur). Tekrar program devam ettirilmek isteniyorsa nokta iletisinden RESUME komutu verilmelidir. Bu işlemlerin amacı karmaşık programlarda hata yakalamayı kolaylaştırmaktır.

ÖRNEK PROGRAMLAR

PROGRAM ADI :K1

clear

store 1 to i

sayi=0

@ 10,10 say "sayiyi giriniz:" get sayi

read

if sayi=0

clear

cancel

endif

clear

@ 1,5 say "sayi karesi"

do while i<=sayi

? i, i\*i

i=i+1

enddo

PROGRAM ADI : K2

clear

@ 1,1 say "1 den 100 e kadar tek sayilarin toplami"

T=0

I=1

do while I<100

T=T+I

I=I+2

enddo

? "Toplam=", T

PROGRAM ADI: K3

clear

set talk off

set date british

do while .t.

t=ctod(' / / ')

@ 10,1 say "dogum tarihi:" get t

read

g=day(t)

a=month(t)

y=year(t)

if g=0.or.a=0.or. y=0

clear

cancel

endif

gun=date()-t

@ 12, 10 say "gecen gun:"+str(gun)

@ 13,10 say "gun:"+str(g)

@ 14,10 say "ay :"+str(a)

@ 15,10 say "yil:"+str(y)

wait " "

enddo

PROGRAM ADI :K4

clear

@ 1,1 say "ekrana kutu çizmek için"

wait " "

@ 1,1 to 10,60

wait " "

clear

@ 1,1 say "ekrana cizgi cizer"

@ 2,10 to 2,50

wait " "

clear

@ 1, 1 say "ekrana duzey cizgi cizer"

@ 2,10 to 20,10

wait " "

@ 2,10 clear to 20,10

wait "bir tusa bas "

@ 2,10 clear

PROGRAM ADI :K5

clear

do while .t.

store 0 to sayi

@ 1,1 say "sayiyi giriniz:" get sayi

read

if sayi > 10

clear

return

else

if sayi=0

return

endif

endif

do case

case sayi=0

@ 2,10 say "sifir"

case sayi=1

@ 2,10 say "bir"

case sayi=2

@ 2,10 say "iki"

otherwise

?? chr(7)

@ 10,10 say "diger degerler"

endcase

wait " "

enddo

PROGRAM ADI :K6

clear

set escape on

i=1

fakt=1

do while .t.

sayi=0

clear

@ 1,1 say "sayi :" get sayi

read

if sayi=0

return

endif

do while i<=sayi

fakt=fakt\*i

i=i+1

enddo

@ 3,1 say str(sayi)+" faktoryel :"+str(fakt)

wait " "

enddo

KÜTÜK KULLANIMI İLE İLGİLİ PROGRAMLAR

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Aşağıdaki program 4 alt programdan oluşmaktadır. (Öğrenci bilgileri ile ilgili)

Kütük adı : ders.dbf

Kayıt yapısı aşağıdaki gibidir.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Field Field Name Type Width Dec

1 KAYIT\_NO Numeric 5 N

2 ISIM Character 30 N

3 TEL Character 15 N

4 ADR Character 40 N

5 ADR1 Character 20 N

6 BOLUM Numeric 2 N

7 GIRIS Numeric 4 N

8 YDIL Numeric 1 N

9 MOKUL Character 30 N

10 OSYM Numeric 3 N

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------DERS PRG (Menü programı)

set echo off

set talk off

set bell off

set scoreboard off

set stat off

set escape off

set deleted off

set talk off

DO WHILE .T.

CLEAR

@ 0,32 SAY "OGRENCI ANA MENUSU"

@ 1,0 SAY REPL ("-",80)

SEC=0

@ 3,0 TO 10,35

@ 4,1 SAY "1.ÖĞRENCİ BİLGİ GİRİŞİ"

@ 5,1 SAY "2.ÖĞRENCİ DEĞİŞİKLİĞİ"

@ 6,1 SAY "3.ÖĞRENCİ İPTALİ"

@ 7,1 SAY "4.ÖĞRENCİ LİSTELEME"

@ 8,1 SAY "5.ÇIKIŞ"

@ 0,60 SAY "Tarih="

@ 0,70 say DATE()

@ 23,0 SAY REPL("-",80)

@ 11,0 SAY "SEÇİMİNİZ="

@ 11,11 GET SEC PICT "9"

READ

DO CASE

CASE SEC=1

DO OGIR

CASE SEC=2

DO ODEG1

CASE SEC=3

DO OIPT

CASE SEC=4

DO OLIST

CASE SEC=5

CLEAR

RETURN

ENDCASE

ENDDO

-------- OGIR.PRG (Giriş bilgilerinin yapıldığı program)

USE DERS

CLEAR

@ 0,0 SAY "ÖĞRENCİ BİLGİ GİRİŞİ"

@ 1,0 SAY REPL("-",80)

@ 3,0 TO 20,79

DO WHILE .T.

WKAYIT\_NO=0

WISIM=SPACE(30)

WTEL=SPACE(15)

WADR=SPACE(40)

WADR1=SPACE(20)

WBOLUM=0

WGIRIS=0

WYDIL=0

WMOKUL=SPACE(30)

WOSYM=0

@ 5,2 SAY "ÖĞRENCİ KAYIT NO:" GET WKAYIT\_NO PICT "99999"

READ

IF WKAYIT\_NO=0

USE

RETURN

ENDIF

LOCATE FOR KAYIT\_NO=WKAYIT\_NO

IF .NOT.EOF()

?? CHR(7)

@ 23,2 SAY "BU ÖĞRENCİ GİRİLMİŞ"

WAIT " "

@ 23,2 SAY SPACE(40)

LOOP

ENDIF

@ 7,2 SAY "ÖĞRENCİ ADI =" GET WISIM

@ 9,2 SAY "TELEFON =" GET WTEL

@10,2 SAY "ADRES =" GET WADR

@11,2 SAY "SEMPT/ŞEHİR =" GET WADR1

@13,2 SAY "BÖLÜM =" GET WBOLUM PICT "99"

@ 11, 45 TO 16,79 DOUBLE

@ 12, 55 SAY "BÖLÜM KODLARI"

@ 13, 47 SAY "1-MAT. 2-İST. 3-FİZ."

@ 14, 47 SAY "4-BİY. 5-FMÜH. 6-KİM."

@ 15, 47 SAY "7-KMÜH. 8-JMÜH. 9-AST. 10-E.MÜH."

@14,2 SAY "GİRİŞ YILI =" GET WGIRIS PICT "9999"

@15,2 SAY "YABANCI DİLİ=" GET WYDIL PICT "9"

@ 17,50 TO 19,75 DOUBLE

@ 18,52 SAY "1-İNG. 2-ALM. 3-FRANS."

@16,2 SAY "MEZ.OLD.OKUL=" GET WMOKUL

@17,2 SAY "OSYM PUANI =" GET WOSYM PICT "999"

READ

IF WISIM = SPACE(30)

LOOP

ENDIF

APPEND BLANK

REPLACE KAYIT\_NO WITH WKAYIT\_NO

REPLACE ISIM WITH WISIM

REPLACE TEL WITH WTEL

REPLACE ADR WITH WADR

REPLACE ADR1 WITH WADR1

REPLACE BOLUM WITH WBOLUM

REPLACE GIRIS WITH WGIRIS

REPLACE YDIL WITH WYDIL

REPLACE MOKUL WITH WMOKUL

REPLACE OSYM WITH WOSYM

ENDDO

-----ODEG1.PRG (Değişiklik işlemlerini yapan program)

USE DERS

CLEAR

@ 0,0 SAY "ÖĞRENCİ BİLGİ DEĞİŞİKLİĞİ"

@ 1,0 SAY REPL("-",80)

@ 3,0 TO 20,79

DO WHILE .T.

WKAYIT\_NO=0

WISIM=SPACE(30)

WTEL=SPACE(15)

WADR=SPACE(40)

WADR1=SPACE(20)

WBOLUM=0

WGIRIS=0

WYDIL=0

WMOKUL=SPACE(30)

WOSYM=0

@ 5,2 SAY "ÖĞRENCİ KAYIT NO:" GET WKAYIT\_NO PICT "99999"

READ

IF WKAYIT\_NO=0

USE

RETURN

ENDIF

LOCATE FOR KAYIT\_NO=WKAYIT\_NO

IF EOF()

?? CHR(7)

@ 23,2 SAY "BU ÖĞRENCİ KAYDI BULUNAMADI"

WAIT " "

@ 23,2 SAY SPACE(40)

LOOP

ENDIF

STORE ISIM TO WISIM

STORE TEL TO WTEL

STORE ADR TO WADR

STORE ADR1 TO WADR1

STORE BOLUM TO WBOLUM

STORE GIRIS TO WGIRIS

STORE YDIL TO WYDIL

STORE MOKUL TO WMOKUL

STORE OSYM TO WOSYM

@ 7,2 SAY "ÖªRENCÿ ADI =" GET WISIM

@ 9,2 SAY "TELEFON =" GET WTEL

@10,2 SAY "ADRES =" GET WADR

@11,2 SAY "SEMPT/ŞEHİR =" GET WADR1

@13,2 SAY "BÖLÜM =" GET WBOLUM PICT "99"

@ 11, 45 TO 16,79 DOUBLE

@ 12, 55 SAY "BÖLÜM KODLARI"

@ 13,47 SAY "1-MAT. 2-İST. 3-FİZ."

@ 14,47 SAY "4-BİY. 5-FMÜH. 6-KİM."

@ 15,47 SAY "7-KMÜH. 8-JMÜH. 9-AST. 10-E.MÜH."

@14,2 SAY "GİRİŞ YILI =" GET WGIRIS PICT "9999"

@15,2 SAY "YABANCI DİLİ=" GET WYDIL PICT "9"

@ 17,50 TO 19,75 DOUBLE

@ 18,52 SAY "1-İNG. 2-ALM. 3-FRANS."

@16,2 SAY "MEZ.OLD.OKUL=" GET WMOKUL

@17,2 SAY "OSYM PUANI =" GET WOSYM PICT "999"

READ

IF WISIM = SPACE(30)

LOOP

ENDIF

REPLACE KAYIT\_NO WITH WKAYIT\_NO

REPLACE ISIM WITH WISIM

REPLACE TEL WITH WTEL

REPLACE ADR WITH WADR

REPLACE ADR1 WITH WADR1

REPLACE BOLUM WITH WBOLUM

REPLACE GIRIS WITH WGIRIS

REPLACE YDIL WITH WYDIL

REPLACE MOKUL WITH WMOKUL

REPLACE OSYM WITH WOSYM

ENDDO

----------OLIST.PRG (Listeleme işlemlerini yapan program)

USE DERS

DO WHILE .T.

GO TOP

CLEAR

@ 0,0 SAY "ÖĞRENCİ LİSTE MENÜSÜ"

@ 1,0 SAY REPL("-",80)

@ 3,0 TO 7,31

@ 4,2 SAY "1.BÖLÜME GÖRE LİSTELEME"

@ 5,2 SAY "2.YABANCI DİLE GÖRE LİSTELEME"

@ 6,2 SAY "3.ANA MENÜ"

@ 8,2 SAY "SEÇİM : "

SEC=0

TUS=0

@ 8,10 GET SEC PICT "9"

READ

DO CASE

CASE SEC=3

USE

RETURN

CASE SEC=1

DO WHILE .T.

GO TOP

STORE 0 TO WBOLUM

CLEAR

@ 0,0 SAY "ÖĞRENCİ BÖLÜME GÖRE LİSTE"

@ 1,0 SAY REPL("-",80)

@ 3,0 SAY "BÖLÜM = " GET WBOLUM PICT "99"

READ

IF WBOLUM=0

EXIT

ENDIF

SAY=0

LOCATE FOR BOLUM=WBOLUM

CLEAR

DO CASE

CASE WBOLUM=1

@ 0,60 SAY "MATEMATİK"

CASE WBOLUM=2

@ 0,60 SAY "İSTATİSTİK"

CASE WBOLUM=3

@ 0,60 SAY "FİZİK"

CASE WBOLUM=4

@ 0,60 SAY "BİYOLOJİ"

CASE WBOLUM=5

@ 0,60 SAY "FİZİK MÜHENDİSLİĞİ"

CASE WBOLUM=6

@ 0,60 SAY "KİMYA"

CASE WBOLUM=7

@ 0,60 SAY "KİMYA MÜHENDİSLİĞİ"

CASE WBOLUM=8

@ 0,60 SAY "JEOLOJİ MÜHENDİSLİĞİ"

CASE WBOLUM=9

@ 0,60 SAY "ASTRONOMİ"

CASE WBOLUM=10

@ 0,60 SAY "ELEKTRONİK MÜH."

ENDCASE

@ 1,0 SAY "NO "+"ISIM"+SPACE(30)+"TEL"

@ 2,0 SAY REPL("-",80)

DO WHILE .NOT.EOF()

? STR(KAYIT\_NO,5)+" "+ISIM+" "+TEL

? REPL("-",80)

SAY=SAY+1

IF SAY=10

SAY=0

TUS=0

DO WHILE TUS=0

TUS=INKEY()

ENDDO

CLEAR

ENDIF

IF TUS=27

EXIT

ENDIF

CONT

ENDDO

GO TOP

@ 23,0 SAY "BİR TUŞA BASINIZ"

TUS=0

DO WHILE TUS=0

TUS=INKEY()

ENDDO

ENDDO

CASE SEC=2

DO WHILE .T.

GO TOP

STORE 0 TO WDIL

CLEAR

@ 0,0 SAY "ÖĞRENCİ YABANCI DİLE GÖRE LİSTE"

@ 1,0 SAY REPL("-",80)

@ 3,0 SAY "BÖLÜM = " GET WDIL PICT "9"

READ

IF WDIL=0

EXIT

ENDIF

SAY=0

LOCATE FOR YDIL=WDIL

CLEAR

DO CASE

CASE WDIL=1

@ 0,60 SAY "İNGİLİZCE"

CASE WDIL=2

@ 0,60 SAY "ALMANCA"

CASE WDIL=3

@ 0,60 SAY "FRANSIZCA"

ENDCASE

@ 1,0 SAY "NO "+"ISIM"+SPACE(30)+"TEL"

@ 2,0 SAY REPL("-",80)

DO WHILE .NOT.EOF()

? STR(KAYIT\_NO,5)+" "+ISIM+" "+TEL

? REPL("-",80)

SAY=SAY+1

IF SAY=10

SAY=0

TUS=0

DO WHILE TUS=0

TUS=INKEY()

ENDDO

CLEAR

ENDIF

IF TUS=27

EXIT

ENDIF

CONT

ENDDO

GO TOP

@ 23,0 SAY "BİR TŞA BASINIZ"

TUS=0

DO WHILE TUS=0

TUS=INKEY()

ENDDO

ENDDO

ENDCASE

ENDDO

-------OIPT.PRG (Öğrenci bilgilerini silme işlemleri)

USE DERS

CLEAR

@ 0,0 SAY "ÖĞRENCİ BİLGİ SİLME"

@ 1,0 SAY REPL("-",80)

@ 3,0 TO 20,79

DO WHILE .T.

WKAYIT\_NO=0

@ 5,2 SAY "ÖĞRENCİ KAYIT NO:" GET WKAYIT\_NO PICT "99999"

READ

IF WKAYIT\_NO=0

USE

RETURN

ENDIF

LOCATE FOR KAYIT\_NO=WKAYIT\_NO

IF EOF()

?? CHR(7)

@ 23,2 SAY "BU ÖĞRENCİ KAYDI BULUNAMADI"

WAIT " "

@ 23,2 SAY SPACE(40)

LOOP

ENDIF

@ 7,2 SAY "ÖĞRENCİ ADI ="+ISIM

@ 9,2 SAY "TELEFON ="+TEL

@10,2 SAY "ADRES ="+ADR

@11,2 SAY "SEMPT/ŞEHİR ="+ADR1

@13,2 SAY "BÖLÜM ="+STR(BOLUM,2)

@ 11, 45 TO 16,79

@ 12, 55 SAY "BÖLÜM KODLARI"

@ 13,47 SAY "1-MAT. 2-İST. 3-FİZ."

@ 14,47 SAY "4-BİY. 5-FMÜH. 6-KİM."

@ 15,47 SAY "7-KMÜH. 8-JMÜH. 9-AST. 10-E.MÜH."

@14,2 SAY "GİRİŞ YILI ="+STR(GIRIS,4)

@15,2 SAY "YABANCI DİLİ="+STR(YDIL,1)

@ 17,50 TO 19,75 DOUBLE

@ 18,52 SAY "1-İNG. 2-ALM. 3-FRANS."

@16,2 SAY "MEZ.OLD.OKUL="+MOKUL

@17,2 SAY "OSYM PUANI ="+STR(OSYM,4)

?? CHR(7)

SOR=" "

@19,2 SAY "KAYDI SİLECEK MİSİNİZ (E/H)=" GET SOR

READ

IF SOR = "E"

DELETE

PACK

ENDIF

S1=SPACE(77)

@ 19,2 SAY S1

I=6

DO WHILE I<20

@ I,2 SAY S1

I=I+1

ENDDO

ENDDO

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

İndexli 2 kütüğün kullanıldığı program örneği

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

1.kütüğün adı : SUBE1.DBF

Kütük yapısı

SUBE\_KODU N 4

SUBE\_ADI C 20

S\_MUDUR C 20

S\_IL C 10

S\_NOT C 15

2. kütüğün adı : SUBE2.DBF

Kütük yapısı

SUBE\_KODU N 4

TARIH D 8

A1 N 9

A2 N 9

A3 N 9

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

----- SUBEMENU.PRG

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

set echo off

set talk off

set bell off

set scoreboard off

set stat off

set escape off

set deleted off

set talk off

DO WHILE .T.

CLEAR

@ 0,32 SAY "ŞUBE İŞLEMLERİ ANA MENÜSÜ"

@ 1,0 SAY REPL ("-",80)

SEC=0

@ 3,0 TO 10,35

@ 4,1 SAY "1.ŞUBE İSİM BİLGİ GİRİŞİ˜"

@ 5,1 SAY "2.ŞUBE HESAP GİRİŞİ"

@ 8,1 SAY "5.ÇIKIŞ"

@ 0,60 SAY "Tarih="

@ 0,70 say DATE()

@ 23,0 SAY REPL("-",80)

@ 11,0 SAY "SEÇİMİNİZ="

@ 11,11 GET SEC PICT "9"

READ

DO CASE

CASE SEC=1

DO SUB1

CASE SEC=2

DO SUB3

CASE SEC=5

CLEAR

RETURN

ENDCASE

ENDDO

------SUB1.prg (Şube isim bilgi giriş/değişiklik işlemleri)

CLEAR ALL

SET TALK OFF

SET ECHO OFF

SET SAFETY OFF

SET STAT OFF

SET SCOREBOARD OFF

SET DELIMITER TO "\[\]"

SET DELIMITER ON

SET COLOR TO W/ ,W/

DO WHILE .T.

CLEAR

BUL = 0

WSUBE\_ADI=SPACE(20)

USE SUBE1 INDEX SUBE1

@ 0,0 TO 20,70

@ 1,1 SAY "ŞUBE GİRİŞ İŞLEMLERİ"

@ 4,10 SAY "ŞUBE KODU ="

@ 6,10 SAY "ŞUBE ADI ="

@ 8,20 SAY "MÜDÜR ADI ="

@ 10,20 SAY "İL ="

@ 12,20 SAY "NOT ="

@ 7,5 TO 13,65

WSUBE\_KODU =0

@ 4,24 GET WSUBE\_KODU PICT "9999"

READ

IF WSUBE\_KODU = 0

RETURN

ENDIF

SEEK WSUBE\_KODU

IF FOUND()

WSUBE\_ADI=SUBE\_ADI

WS\_MUDUR=S\_MUDUR

WS\_IL=S\_IL

WS\_NOT=S\_NOT

@ 6,34 SAY WSUBE\_ADI

@ 8,34 SAY WS\_MUDUR

@ 10,34 SAY WS\_IL

@ 12,34 SAY WS\_NOT

STORE 1 TO BUL

ENDIF

@ 6,24 GET WSUBE\_ADI

@ 8,34 GET WS\_MUDUR

@ 10,34 GET WS\_IL

@ 12,34 GET WS\_NOT

READ

IF BUL=0

APPEND BLANK

ENDIF

REPLACE SUBE\_KODU WITH WSUBE\_KODU

REPLACE SUBE\_ADI WITH WSUBE\_ADI

REPLACE S\_MUDUR WITH WS\_MUDUR

REPLACE S\_IL WITH WS\_IL

REPLACE S\_NOT WITH WS\_NOT

WS\_MUDUR=SPACE(20)

WS\_IL=SPACE(10)

WS\_NOT=SPACE(10)

ENDDO

RETURN

------SUB3.prg (Şube hesap bilgi giriş/değişiklik işlemleri)

CLOSE ALL

CLEAR ALL

SET TALK OFF

SET ECHO OFF

SET SAFETY OFF

SET STAT OFF

SET SCOREBOARD OFF

SET DELIMITER TO "\[\]"

SET DELIMITER ON

SET COLOR TO W/ ,W/

DO WHILE .T.

SELECT 1

USE SUBE1 INDEX SUBE1

SELECT 2

USE SUBE2 INDEX SUBE2

CLEAR

WTARIH = CTOD(" / / ")

WSUBE\_KODU=0

WA1=0

WA2=0

WA3=0

BUL = 0

CLEAR

@ 0,0 TO 20,70

@ 1,1 SAY "HESAP GIRIS İŞLEMLERİ"

@ 4,10 SAY "SUBE KODU ="

@ 6,10 SAY "SUBE ADI ="

@ 8,20 SAY "MUDUR ADI ="

@ 10,20 SAY "IL ="

@ 12,20 SAY "NOT ="

@ 7,5 TO 13,65

@ 13,10 TO 20,60

@ 16,20 SAY "A1 HESABI :"

@ 17,20 SAY "A2 HESABI :"

@ 18,20 SAY "A3 HESABI :"

@ 4,24 GET WSUBE\_KODU PICT "9999"

READ

IF WSUBE\_KODU = 0

RETURN

ENDIF

SELECT 1

SEEK WSUBE\_KODU

IF FOUND()

@ 6,34 SAY SUBE\_ADI

@ 8,34 SAY S\_MUDUR

@ 10,34 SAY S\_IL

@ 12,34 SAY S\_NOT

@ 14,20 SAY "TARIH ="

@ 14,30 GET WTARIH

READ

SELECT 2

SEEK STR(WSUBE\_KODU)+DTOC(WTARIH)

IF FOUND()

@ 21,1 SAY "KAYIT VAR"

WA1=A1

WA2=A2

WA3=A3

@ 16,32 SAY WA1

@ 17,32 SAY WA2

@ 18,32 SAY WA3

STORE 1 TO BUL

ENDIF

@ 16,32 GET WA1 PICT "999999999"

@ 17,32 GET WA2 PICT "999999999"

@ 18,32 GET WA3 PICT "999999999"

READ

IF BUL=0

APPEND BLANK

ENDIF

REPLACE SUBE\_KODU WITH WSUBE\_KODU

REPLACE TARIH WITH WTARIH

REPLACE A1 WITH WA1

REPLACE A2 WITH WA2

REPLACE A3 WITH WA3

ELSE

CLEAR

@ 22,10

WAIT " BU SUBE\_KODU BULUNAMADI İLK DOSYAYA GIRINIZ"

LOOP

ENDIF

ENDDO

RETURN

---
*Kaynak: `VERİ TABANI VE BAZI KAVRAMLARI/VERİ TABANI VE BAZI KAVRAMLARI.doc` — serkan — 2004*
