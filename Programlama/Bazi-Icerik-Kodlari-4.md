# Bazi İçerik Kodlari

| 17- Image kontrolü |
| --- |

İmage kontrolü, bitmap, icon, metafile, gif ya da jpeg formatındaki resim dosyalarını göstermek için kullanılan kontroldür. PictureBox kontrolü de bu işi yapmakta kullanılır. İkisi arasındaki fark ise şudur: Image kontrolü, picturebox'a göre daha az sistem kaynağı kullanır ve resmi daha hızlı gösterir. Ama picturebox buna karşılık daha fazla property listesine sahiptir. Image kontrolünün en önemli propertisi "Stretch" propertisidir. Bu properti true yapıldığında, resim otomatik olarak image kontrolünün boyutlarına genişletilmektedir. Örneğimizde drag-drop uygulamasının üzerine bir çalışma yapıldı. Bu çalışmada stretch özelliğinin küçük bir zaafının giderilmesine yer verildi. Stretch özellğini true yaptığımızda resim image kontrolünün boyutlarına kadar büyür ama maalesef eni ve boyu aynı oranda büyümez. Yani image kontrolünün eni daha büyükse resmin eni boyuna göre daha fazla uzayacak dolayısıyla görüntü enlemesine uzamış olacaktır. Bu da maalesef şeklin bozulması demektir. Bunu önüne geçmek için yapacağımız şey image kontolünün boyutlarının gösterilecek resmin boyutlarına göre ayarlamak olacaktır. Resmin en/boy oranına aspekt oranı denir. Örneğimizde bu oran kullanılarak resimlerin bozulmaya uğratılmadan görüntülenmesi sağlanmıştır.

| Download |
| --- |
| 16- MS Chart Kontrolü |

Microsoft Chart kontrolü ile verilerin grafik görünümünü gerçekleştirebilirsiniz. En genel grafiksel gösterim biçimlerini kullanmaktadır. Örnek çalışmada, bir dağıtım şirketinin altı aylık kola ve su satış değerleri görülmektedir. Burada "seri" olarak Kola ve Su kullanılırken "veri" olarak da Ocak, Şubat...vs kullanılmıştır. Program içinde bu değerlerin nasıl atandığını görebilirsiniz. Örnek çalışmada komut aralarında yer alan açıklamalardan, seri ve veri adlarının nasıl tanımlandığını ve verilerin nasıl yüklendiğini inceleyebilirsiniz.

| Download |
| --- |
| 15- ListView Kontrolü |

Windows Explorer penceresinde view (görünüm) komutu vardır. Bu menüden, seçeceğimiz bir şıkka göre pencere içeriğini, büyük simgeler, küçük simgeler, liste ya da detaylı olarak görebiliriz. ListView kontrolü bu özelliği uygulamalarımızda kullanmamızı sağlar. Örneğimizde listview kontrolüne yer verilirken bu dört görünüm özelliğinin nasıl kullanıldığını göreceksiniz. En basit kullanımda yapılacak tek şey pencerede görünmesini istediğimiz objelerin Add komutu ile listview tablosuna dahil edilmesidir. Bir de bu öğeler için kullanılacak sembollerin belirtilmesi gerekiyor. Her öğe için ayrı bir sembol atanabileceği gibi, tüm öğelere aynı sembol atanabilir. İkon tanımlamak için projeye bir ImageList dahil edilmelidir. Daha sonra da custom propertisi kullanılarak ImageList, ListView kontrolünün ikon kaynağı olarak tanımlanır. Bu örneğimizde bir veri dosyası içindeki kayıtların listview'da öğe olarak tanımlanmasına yer verilmiştir.

| Download |
| --- |
| 14- Winsock kontrolünün kullanımı |

Winsock kontrolü, ağ ya da internet üzerinden diğer bilgisayarlara erişimi kolaylaştıran güçlü bir arabirim olarak programcıların kullanımına sunulmuştur. Bu kontrol sayesinde bir kaç satırlık bir kodla diğer bilgisayarlar arasında data transferi gerçekleştirilebilir, ağ ya da internet üzerine açılabilirsininiz.

Bu kontrolün kullandıldığı iki iletişim modu bulunmaktadır: TCP ve UDP. Varsayılan mode TCP modudur. Bu modda iletişim kuran bilgisayarlar arasında önce karşılıklı bir teyid işlemi gerçekleştirilir. Sonrasında da data transferi yapılır. Böylece datanın diğer bilgisayara ulaştığından emin olunur.

Ama örneğin bir sohbet programı yapacaksanız o zaman UDP modunu kullanmanız gerekmektedir. Çünkü böylesi bir uygulamada teyidleşmek anlamsız olmaktadır. Çünkü yapılan sadece bir IP numarasına data göndermektir. Datanın hedefe ulaşıp ulaşmadığı önemli değildir.

Yapacağımız ilk şey doğal olarak, uygulamamıza bir Winsock kontrolü eklemek olmalıdır.

İletişim kuracak olan bilgisayarlardan biri sunucu kodları kullanmak zorundadır. Diğeri ise istemciye yönelik kodları kullanmalıdır. Ancak burada bir yanılgıya düşmemek gerekir. Sunucu bilgisayar sadece veri gönderir, istemci de alır diye bir kural yoktur. Her iki bilgisayar da hem veri gönderir hem alırlar. Kural olarak, bağlantıyı kurmak için makinelerden birinin sunucuya, diğerinin istemciye yönelik kod kullanması gerekir.

İletişim kuracak olan bilgisayarları sunucu ve istemci diye ayırdıktan sonra iletişimde kullanılacak olan portu belirlememiz gerekiyor. Normalde iki bilgisayar arasında fiziksel bir iletişim hattı bulunmaktadır. Ancak bu hat, teorik olarak sonsuz sayıda olmak üzere mantıksal iletişim hatlarına bölünmektedir. Bunlara port denmektedir ve her biri bir numara ile adlanmaktadırlar. Uygulamamızda bir port numarası belirlememiz ve her iki bilgisayarın bu portu kullanmasını sağlamamız gerekmektedir. Örnek olarak 4444 numaralı portu kullanalım.

**Sunucu tarafı******

Sunucu bilgisyar iletişim için ilk adımı başlatmalıdır. Port tanımını yapmalı ve dinleme moduna geçmelidir.

```vbnet
Private Sub Form_Load()
Winsock1.localport = 4444
Winsock1.listen
End Sub
```

İlk komut port tanımını yapmak, ikinci komut ise olası bir istemciden gelecek olan iletişim talebini beklemek içindir. Dinleme modunda bekleyen sunucuya bir iletişim talebi geldiğinde "ConnectionRequest" olayı gerçekleşir. O yüzden bu olay için de bir kod yazmamız gerekir.

```vbnet
Private Sub Winsock1_ConnectionRequest(ByVal requestID As Long)
Winsock1.Close
Winsock1.Accept requestID
End Sub
```

İlk komutla dinleme modundan çıkış gerçekleştirilmektedir. Artık dinleme modundan çıkmamız gerekiyor çünkü iletişim için artık bir istemci bize ulaşmıştır. İkinci komutla gelen talep kabul edilmektedir. Sunucu tarafında olması gereken zorunlu son kod ise istemciden gelen datanın alınması komutudur. İstemcinin bağlantı talebi kabul edildikten sonra istemciden gelecek olana data sunucuya ulaşınca "DataArrival" olayı gerçekleşir. Dolayısıyla datanın alınması ile ilgili komut bu olayla ilgili prosedüre yazılır.

```vbnet
Private Sub Winsock1_DataArrival(ByVal bytesTotal As Long)
Dim bilgi As String
Winsock1.GetData bilgi
MsgBox bilgi
End Sub
```

İkinci komutla, istemciden gelen data alınıp bir değişkene aktarılmaktadır.

Download

**İstemci tarafı******

İstemci bilgisyarın yapması gereken ilk şey, sunucunun, bağlantıya açtığı portu kullanmak olmalıdır. İkinci adım ise bağlantı kuracağı sunucunun IP adresini belirtmek olacaktır. Burada örnek olarak kendi bilgisayarımızla bağlantı kurabiliriz. Dolayısıyla bilgisayarımızın IP adresini bilmemiz gerekiyor. Bunu öğrenmek için windows "Başlat" menüsünden "Çalıştır" komutunu işletip komut satırına "winipcfg" komutunu yazmak olacaktır. Sonuç olarak istemcinin bağlantıya hazırlık komutları şu şekilde olacaktır:

```vbnet
Private Sub Form_Load()
Winsock1.RemotePort = 4444
Winsock1.RemoteHost = "195.87.88.55"
Winsock1.Connect
End Sub
```

İlk komutla, kullanılacak olan portun numarası; ikinci komutla, bağlantı kurulacak olan sunucunun IP adresi tanımlanırken, üçüncü komutla bağlantı talebi devreye sokulmaktadır. Bu komut sayesinde sunucuda "ConnectionRequest" olayı gerçekleşir ve sunucu "Accept" komutuyla istemciden gelen talebi kabul eder. Bu durumda sıra istemcidedir ve yapması gereken datayı göndermek olacaktır.

```vbnet
Private Sub Command1_Click()
Winsock1.SendData bilgi
End Sub
```

İstemci datayı gönderdiğinde sunucuda "DataArrival" olayı gerçekleşecek ve sonrasında gelen datayı alacaktır.

Download

İşte bu kadar. Burada en temel şekliyle bir sunucu ile bir istemci arasında bağlantı kurulmuş ve basit bir veri transferi gerçekleştirilmiştir.

| 13- Multimedia MCI kontrolünün kullanımı |
| --- |

Multimedia MCI kontolu, media kontrol arabirimi (MCI) sayesinde, multimedi dosyalarının çalınması ya da kaydedilmesinde kullanılır. Bu kontrol üzerinde yer alan ilgili komut tuşları ile MIDI, AVI ve WAV dosyaları ile Müzik ve Video CD'lerin kontrolü sağlanır. Bu işi gerçekleştirirken Multimedia MCI kontrolü üzerindeki tuşlar kullanılabileceği gibi, bu tuşların karşılığı olan komutlar da kullanılabilir.

Multimedi MCI kontrolünün kendine özgü propertileri şunlardır:

Command: MCI komutunu işletir. Bu komutlar şunlardır: Open, Close, Play, Pause, Stop, Back, Step, Prev, Next, Seek, Record, Eject, Sound, Save.

DeviceType: Media tipini belirlemekte kullanılır. Medi tipleri şunlardır: WaveAudio, AVIVideo, CDAudio, DAT, DigitalVideo, MMMovie, Overlay, Scanner, Sequencer, VCR, Videodisc ya da Other.

Örnek programımızda bir listeden seçilen Wav dosyaların çalınmasına ve de o dosya üzerine kayıt yapılmasına yer verilmiştir. Bu iş için bir Directory List Box kullanıldı. Bu listeden seçilen wav dosyasını çalmak için MCI kontrolü üzerindeki Play tuşuna basmak yeterli olacaktır. Aynı işin komutla gerçekleştirilmesine de yer verilmiştir. Eğer ekrandaki Çal tuşuna basarsanız seçili dosya tekrar çalacaktır. MCI kontrolü üzerindeki Record tuşuna basarsanız, o anki dosyanın bulunulan konumundan itibaren ses kaydı yapılmaya başlanır. Kaydını aldığınız bu sesin bir dosyada saklanmasını istiyorsanız metin kutusuna dosya adı yazın ve "Kaydet" tuşuna basın.

| Download |
| --- |
| 12- Mask Edit Box'ın kullanımı |

Mask Edit Box kontrolü, maske tanımlama sayesinde, kullanıcıyı sınırlayan veri girişi ve bunun sonucunda da biçimlenmiş veri çıkışı elde etmek için kullanılır. Örneğin telefon numaraları (212) 211 21 82 şeklinde bir formatta tutulur. Mask Edit Box kontrolü sayesinde ilave bir kod kullanmaya gerek kalmadan böylesi bir formatta veri girişi yaparken, yine aynı formatta, bu bilginin veri alanlarına kaydedilmesi sağlanabilmektedir. Veri giriş sınırlamaları "Mask" propertisi ile belirlenirken, kontrolün içeriği "Text" propertisi ile alınır.

Bu kontrolün en çok kullanılan propertileri aşağıda açıklanmıştır:

AutoTab: Tanımlanmış sınırlar içerisinde veri girişi tamamlandığında bir sonraki kontrola geçişi sağlar. (Örnek programda bu özellik kullanıldı).

Format: Sınırlamasız ama formatlanmış veri girişi için kullanılır. Örneğin "#,##0" formatını seçerseniz. Bir sayısal değer girişi yaptıktan sonra MaskEditBox, sayıyı binler ayraçlı olarak yeniden düzenler. Kullanılacak olan formatlar önceden tanımlanmış olarak properti penceresinde yer almaktadır.

Mask: Veri giriş maskesini tanımlamakta kullanılır. Örneğin telefon numarası girişi için şöyle bir maske kullanılır. "(999) 999 99 99". Maske tanımlamak için özel karakterler kullanılır. En çok kullanılanları şunlardır:

\# :Sadece rakam girişine izin verilir.

, :Binler ayracı.

: :Saat ayracı.

/ :Tarih ayracı.

& :Kontrol karakterleri dışındaki karakterlerin girişine izin verilir (Ascii 32-126 ve 128-256 arası olanlar).

> :Hemen sonrasındaki pozisyonun harfini büyültür.

< :Hemen sonrasındaki pozisyonun harfini küçültür.

9 :Sadece rakam girişine izin verilir.

? :Sadece harf girişine izin verilir.

Diğer : Bunların dışındaki her türlü sembol (örneğin (,-,),@ gibi karakterler) MaskEdit kutusunda olduğu gibi gösterilirler.

Örnek programda bu karakterler kullanılarak değişik maske kullanımlarına yer verilmiştir. Text propertisi aracılığıyla MaskEdit kutusunun içeriğini ilgili veri alanlarına aktarabilirsiniz. Yine text propertisini kullanarak program içinden MaskEdit kutusunun içeriğini değiştirebilirsiniz ama bu konuda bir şeye dikkat etmeniz gerekiyor. Eğer tanımlı bir maske varsa önce bunu kaldırmalısınız. Aksi taktirde Run-time hata oluşacaktır. Bunu engellemek için text properisini aşağıdaki şekilde değiştirmek gerekir:

```vbnet
Gecici = MaskEdBox1.Mask
MaskEdBox1.Mask = ""
MaskEdBox1.Text=YeniMetin
MaskEdBox1.Mask=Gecici
```

| Download |
| --- |
| DriveList, DirectoryList ve FileList kontrollerinin kullanımı |

CommonDialog kontrolünün save ve open metodları, sistemin dosya yapısına erişmemizi sağlar. Ancak bazen sistem sürücü listesini, klasör ve dosya yapısını, uygulama penceremizde sürekli aktif tutmak isteyebiliriz. Örneğin dosya yönetimi türü bir rutin, uygulamamızın bir parçası olabilir. DriveList, DirectoryList ve FileList kontrolleri, birbirlerine ilişkilendirilerek bizim bu ihtiyacımızı karşılamaktadır. Bu kontroların yaptıkları şudur:

DriveList: Sistem sürücülerini (Floppy, HDD, CDROM) gösterir.

DirectoryList: Klasör yapısını (Belgelerim, Program Files, Windows) gösterir.

FileList: Dosya listesini verir.

Bu kontrolların birbirleriyle ilişkilendirilmeleri de çok basittir. DriveList'ten bir sürücü seçildiği zaman bu değer "Drive" propertisine aktarılır. Bu değeri, DirectoryList kontrolünün "Path" propertisine aktarırsanız, DirectoryList'te seçilen sürücünün klasör yapısı görüntülenecektir. Kullanıcı bu listeden istediği bir klasörü seçtiğinde seçilen klasörün adresi yine "path" propertisinde olacaktır. Bu değeri FileList'in "Path" propertisine aktardığınızda ise FileList'te o klasör içindeki dosyalar görüntülenecektir. Son olarak FileList'ten bir dosya adı seçtiğinizde bu değer FileList'in "FileName" propertisinde olacaktır. Tüm bu zincirin sonunda elde seçilen dosyanın tamyol adı şu olacaktır:

```vbnet
Dir1.Path + "\" + File1.FileName
```

Aşağıdaki örnek programı önce çalıştırın sonra da birkaç satırdan oluşan kod yapısını inceleyiniz.

| Download |
| --- |
| 10- "MsFlexGrid" Kontrolünün kullanımı |

MsFlexGrid kontrolü, şablon türü verileri görüntülemek, üzerinde işlem yapmak için kullanılmaktadır. Metin ya da resim içeren tablolar üzerinde esnek bir sıralama, birleştirme ve biçimleme imkanı sunar.

MSFlexGrid hücresine metin, resim ya da her ikisini koyabilirsiniz. Program içinde Row ve Col propertilerine değer vererek ya da doğrudan MSFlixGride tıklayarak ya da yön tuşlarıyla üzerinde hareket ederek aktif hücreyi değiştirebilirsiniz ve Text propertisini kullanarak aktif hücre değerini okuyabilir ya da değiştirebilirsiniz.

Örnek programımızda bazı temel propertilerin kullanımına yer verilmiştir. Program ilk çalıştığında (Form\_Load) Rows ve Cols propertileri ile toplam satır ve sütun sayıları tanımlandı. Sonra da satır ve sütun numaraları tanımlandı. Form üzerinde MSFlexGrid dışında iki tane de TextBox kullanılmıştır. Text1, aktif hücre adresini göstermek Text2 de aktif hücre içeriğini göstermek için kullanılmıştır.

| Download |
| --- |
| 9- "Timer" kontrolünün kullanımı |

Timer kontrolü, önceden belirlenmiş zaman aralıklarında belli bir prosedürü işletmek için kullanılmaktadır. Peryod olarak isimlendirebileceğimiz bu zaman aralığı değeri, milisaniye cinsinden "Interval" propertisi ile tanımlanır. Örnek uygulamamızda basit bir oyun programı oluşturduk. 250 milisaniye aralıklarla top aşağıya doğru kaydırılmaktadır. Her 10 toptan sonra süre 25 ms düşürülmekte dolayısıyla topun düşüş hızı artmaktadır. Bu arada en altta yer alan bar, yön tuşlarıyla sağa sola hareketlendirilerek top yakalanmaya çalışılmaktadır. Yön tuşlarının form üzerinde aktif olması için formun "KeyPreview" propertisi True yapılmalıdır. Böylelikle tüm tuşa basma olayları, form içinde yer alan kontrollerden önce, form tarafından algılanacaktır. Formun "KeyDown" olayı ile yön tuşları sezilmekte ve topu tutan bara, gerekli olan hareket sağlanmaktadır.

| Download |
| --- |
| 8- "ProgressBar" kontrolünün kullanımı |

ProgressBar kontrolü, bir işleminin süresini, bir diktörtgen içine soldan sağa doğru külçeler yığarak gösterir.

Word, Excel gibi uygulamalarda da görmüşsünüzdür, uzun sürebilecek bir hesaplama ya da bir dosyayı kaydederken işlem süresinin bir şekilde kullanıcıya yansıtılması getrekir. İşte progressbar kontrolüyla yapılan budur. Progressbar kontrolünün bu iş için kullanılan temel propertileri "Min", "Max" ve "Value" dur. Min ve max propertilerine progresbarın alabileceği en küçük ve en büyük değerler verilir. Value propertisi ise uygulamanın çalışması sırasında işlemler ilerledikçe sürekli artan değerler alır.

Buradaki örneğimiz, 7- "Treeview" kontrolünün kullanımı konusunun devamı niteliği taşımaktadır. Treeview'ın kullanımı konusunda iki veritabanının tabloları ve bu tablolara ait alan adları okunmuş ve düğüm olarak tanımlanmıştı. Burada bir adım ileri gidildi ve alan değerleri de okundu. Ama veritabanı dosyaları çok büyük olduğu için bu işlem zaman almaktadır. İşte bu zaman alıcı işlemin ilerleyişi ProgressBar kontrolü ile müşteriye yansıtılmıştır. Dosyadaki alan değerleri okunurken bir kısıtlamaya gidilmiş ve okunan kayıt sayısı 750 ile sınırlandırılmıştır. Bu arada bir profesyonelliğe de yer verildi. Yapılan işlemlerle ilgili bir açıklama bir metin kutusu aracılığıyla kullanıcıya gösterilmektedir. Metin kutusunun "MultiLine" propertisi "True" yapılmış ve her işlem ayrı bir satırla metin kutusuna yazılmıştır. Program içinde bir sonraki satıra geçiş Chr(13) ve Chr(10) karakterleriyle sağlanmaktadır. Son olarak "DoEvents" komutundan bahsedeyim. Normalde uygulama, bir komutun işi bitene kadar kullanıcıya tepki vermez. Bu komutun sayesinde, uygulamanın başka olayları da işletmesi sağlanır. Böylece veritabanından kayıtlar okunurken progressbardaki külçelerin dizilişleri de görülebilecektir.

| Download |
| --- |
| "Treeview" kontrolünün kullanımı |

Treeview, Node (Düğüm) nesnelerinin hiyerarşik diziliminden oluşan bir kontroldur ve bir metnin başlık ve altbaşlıklarını, diskteki dosya ve klasör yapısını vs.gibi, özellikle hiyerarşik görünümün ihtiyaç duyulduğu tüm işlerde kullanılmaktadır. Buradaki örneğimizde VB ile beraber gelen iki veritabanı dosyası kullanılarak bir veri hiyerarşisi oluşturuldu.

Şimdi, Treeview kontrolünün en önemli komutunu biraz detaylı ele alalım. Treeview penceresinde görüntülenecek olan tüm düğümlerin tanımlanması gerekmektedir. Bu da "Add" komutu ile gerçekleştirilir.

```vbnet
Treeview1.Nodes.Add(relative, relationship, key, text, image, selectedimage)
```

relative: Kendisinden önceki düğümün adı - opsiyonel

relationship: Kendisinden önceki düğümle arasındaki ilişkinin şekli - opsiyonel

0 - (ilk): İlişkide olduğu düğüm seviyesinde ilk sıradaki düğüm

1 - (son): İlişkide olduğu düğüm seviyesinde son sıradaki düğüm

2 - (sonraki): İlişkide olduğu düğümden bir sonraki sırada

3 - (önceki): İlişkide olduğu düğümden bir önceki sırada

4 - (çocuk): İlişkide olduğu düğümün alt seviyesinde

key: Düğüme erişim ya da referans için kullanılacak olan isim - opsiyonel

text: Düğüm üzerinde görülecek olan isim - gerekli

image: Düğüm üzerinde görünmesi istenen resmin ListImage kontrolündaki sıra numarası - opsiyonel

selectedimage: Düğüm seçili iken üzerinde görünmesi istenen resmin ListImage kontrolündeki sıra numarası - opsiyonel

Düğümlere isim verilmesi her ne kadar opsiyonel olsa da, bu, ilk seviye düğümler için geçerlidir. Alt seviye düğümlere doğru ilerlerken maalesef hangi düğümün uzantısı olduğunun bilinmesi gerekmektedir. O yüzden her düğüm için mutlaka "key" yani isim tanımlamakta yarar bulunmaktadır. Örneğimizde düğüm isimleri verilirken, ilk iki seviyenin düğümlerinde, Veriler, Veri1 ve Veri2 isimleri doğrudan tanımlandı. Ancak tablo ve alanlar için düğümler oluşturulurken, bunlardan kaçar tane tanımlanacağı bilinmediği için doğrudan isim verilemedi. Onun yerine "tablo" ve "alan" stringlerinin yanında for-next döngülerinin indis değerleri kullanıldı. Bu arada bir veri dosyası içindeki tablolara ve o tablolar içindeki alan adlarına dinamik olarak nasıl ulaşıldığına da dikkat ediniz.

| Download |
| --- |
| "StatusBar" ve "Shape" kullanımı |

Her profesyonel uygulamada mutlaka durum çubuğuna yer verilmektedir. Uygulama penceresinin alt çizgisini kaplayan bu araç, uygulamanın bir nevi o anki raporunu vermektedir. Durum çubuğunu öncelikle tasarım sırasında şekillendirmek gerekir. Property penceresinde "Custom"u tıkladığımızda karşımıza çıkacak olan bu pencerede durum çubuğunun genel özellikleriyle beraber yazı tipi ve resim özelliklerini tanımlayabilirsiniz. Ancak durum çubuğunun asıl işlevi, üzerindeki her bir durum hücresini kasteden panellerle ortaya çıkar. O yüzden "Panel" penceresini biraz daha geniş ele alalım.

Insert Panel: Yeni panel ekler.

Remove Panel: Varolan paneli siler.

Text: Panel üzerinde görünecek olan metni tanımlar.

ToolTipText: Mouse'un panel üzerine geldiği anda görünmesi gereken metni tanımlar.

Minimum Width: Pixel olarak panelin genişliğini belirtir.

Style: Panelin işlevini belirler.

Style özelliğiyle "CABS", "INS" ya da "SCRL" tuşlarının durumu durum çubuğunda gösterilmektedir. Eğer style text olarak tanımlanırsa çalışma sırasında bu panel üzerinde kullanıcıya metinsel bildirimler yapılabilir.

Örneğimizde durum çubuğuna 5 tane panel eklenmiştir. Panellerin birincisi mouse'un form üzerindeki pixel konumunu, beşincisi de mouse aracılığıyla taşıdığımız şeklin konumunu verirken diğer paneller de Cabs, ve Ins tuşlarının durumlarını ve sistemin tarihini göstermektedir.

Programın yaptığı işlem şudur: Penceredeki şekli taşımak istediğimizde sol tuşunu basılı tutarak mouse'u hareket ettiriyoruz. Bu sırada mouse'un ve taşınan şeklin pixel konumları durum çubuğunda gösterilmektedir. Sol tuşu bıraktığımız anda da taşıma işlemi sona ermektedir. Kodlamada üç tane form olayı kullanıldı. MouseDown, MouseMove ve MouseUp. Taşıma işlevinin başladığı MouseDown olayı ile sezilmektedir. Bu esnada, mouse'un konum değerlerini veren X ve Y kullanarak mouse'un objemiz üzerinde olup olmadığı denetlenir. Eğer mouse obje üzerinde ise taşıma onayını belirten bayrak değeri yani "TasiBasildi" True yapılır. Taşıma işini gerçekleştiren komutlar ise MouseMove olayında yer almaktadır. Aslında taşıma diye kastettiğimiz şey objenin Top ve Left değerlerini değiştirmektir. Tabi bu işlemi gerçekleştirmeden önce "TasiBasildi" değişkeni denetlenmektedir. Eğer bu bayrak True değerini taşıyorsa taşıma işlemi gerçekleştirilecektir. Bu bayrak MouseUp olayı gerçekleştiğinde False yapılmaktadır

Not: FarkX ve FarkY parametrelerinin ne işe yaradığını ifade etmek zor olduğu için daha doğrusu sizlerin anlayacağı şekilde ifade etmemin zor olacağını düşündüğüm için, bu işi tamamen size bıraktım.. Bu parametreleri devre dışı bırakarak sonucu izleyin bakalım.

| Download |
| --- |
| Common Dialog Kontrolünün Save metodunun kullanımı |

CommonDialog kontrolünün "ShowOpen" metodu ile "Dosya Aç" diyalog penceresi aktive edilir. Bu pencerede kullanıcı, açmak istediği dosyanın sürücüsünü, dizinini ve adını tayin edebilir. Bu örnekte "Flags", "Filter" ve "FilterIndex" özelliklerine değer atamaları yaptıktan sonra ShowOpen metodu ile dosya açma diyalog penceresi ekrana getirildi. Kullanıcı eğer "İptal"a basarsa hiçbir işlem yapılmayacak ama belli bir dosyayı seçtikten sonra "Aç" tuşuna basarsa seçilen dosyanın tam adı "FileName" özelliğine atanacaktır. Bu içerik artık program içinde istenildiği şekilde kullanılabilir.

| Download |
| --- |
| "Text Box" kullanımı |

Bu örnekte, bir TextBox'ta yer alan metnin programatik olarak seçilmesi gösterilmektedir. Bu işleme genelde, yanlış bir veri girişi yapıldığında kullanıcıya düzeltme yapabilme kolaylığı vermek için ihtiyaç duyulmaktadır. Bu işlemi gerçekleştirmek için TextBox'ın SelStart ve SelLength özellikleri kullanılır. Seçilecek metnin başlangıç noktası SelStart ile belirlenir. SelLength ile de seçilecek parçanın uzunluğu tanımlanır.

```vbnet
Text1.Selstart=0
Text1.SelLength=Len(Text1.Text)
```

SelLength'in diğer bir özelliği daha vardır. Programatik olarak metin üzerinde herhangi bir yere konumlanmak için SelStart'a bir değer verilmesi yeterlidir.

```vbnet
Text1.Selstart=3 'İmleç TextBox'taki metnin 3.harfine konumlanır
```

TextBox kullanımında yer verilmesi gereken bir incelik bulunmaktadır: Birden çok textbox'ın bulunduğu bir veri giriş ekranında, kullanıcı Enter'a bastıkça imleçin sonraki textbox'a otomatik olarak geçmesi istenir. Aslında bu işlem Tab tuşuyla gerçekleşmekte ama pek kullanışlı olmamaktadır. Bu iş için yapılacak işlem çok basittir: TextBox'ın keydown olayı gerçekleştiğinde basılan tuşun koduna bakılıyor. Bu kod eğer Enter'a aitse, SendKey komutuyla bir "Tab" karakteri gönderiliyor. Böylece programatik olarak Tab tuşuna basıldığı algılanmış oluyor. Enter'a basıldığında ortaya çıkan bip sesinin bastırılması içinse KeyPress olayı kullanılmıştır. Tüm bu işlemlerin işe yaraması için TextBox'ların TabIndex değerleri sıralı olmalıdır. Bu arada bir şeye dikkat etmeniz gerekiyor: Son TextBox'tan sonra "Kaydet" tuşuna geçiliyor ve kullanıcının Enter'a basmasıyla TextBox'ların içindeki değerler gerekli yere kaydedilip TextBox'ların içi boşaltılıyor. Son olarak SetFocus metoduyla imleç tekrar ilk TextBox'a konumlandırılıyor.

| Download |
| --- |
| "Combo Box"ın kullanımı |

Bu örnekte, bir "Combobox'tan seçilen değere bağlı olarak başka bir "ComboBox'taki değerlerin değiştirilmesi yer almaktadır. Çalıştırmadan önce Combo1'in "list" özelliğine 3 örnek ilin -Ankara, İstanbul ve İzmir- eklendiğini görünüz. Örnekte Combo1'in "click" olayı için küçük bir kod yer almaktadır. Bu kodda, seçilen ile ait ilçeler Combo2'ye tanımlanmaktadır. Bunun için de bir dizi tanımı yapılmış ve Form1 "Load" olayı gerçekleştiğinde bu diziye, tasarım sırasında Combo1'e atanmış olan illere ait ilçeler yüklenmektedir.

| Download |
| --- |
| "Check Box" ve "Option" kullanımı |

Bu örnekte, işaretlenen "Option"a bağlı olarak "Check Box"ların kullanıma açılması/kapatılması yer almaktadır. "Option"lar bir firmadaki belirli görevleri gösterirken, "CheckBox"lar da belirli yetki seviyelerini göstermektedir. Bu örnek kullanım, bir "Personel Takip" programında yer alabilir. İlk çalıştırmada, varsayılan görev uzmandır ve ilk üç yetki uzmana atanabilmesi için kullanıma açılmıştır. Kodlamada yapılan işlem ise şudur: Gerçekleşen her bir option olayı için ilgili checkbox'ların enable özelliği true diğerleri false yapılmaktadır. Yalnız ince noktaya dikkat ediniz:: Kodlamayı basitleştirmek için kontrol dizisi kullanılmıştır. Bunu yapabilmek için, deklerasyon bölümünde "Object" tipinde bir dizi tanımlanır ve bu dizinin her bir elemanına "Set" komutuyla ilgili kontrolün ataması yapılır.

| Download |
| --- |
| "Check Box" ve "Frame" kullanımı |

Bu örnekte birden fazla Option grubunun kullanımı yer almaktadır. Normalde Option kontrollerini form'a yerleştirdiğiniz zaman bu tek bir grup oluşturur ve aynı anda yalnızca bir tanesini seçebilirsiniz. Ama option'ları bir "Frame" içine koyarsanız her frame ayrı bir option grubu oluşturur. Programda bir kod yer almamaktadır. Ama her frame'deki varsayılan değeri belirlemek için optionlardan birinin value özelliğini tasarım sırasında true yapmanız gerekmektedir.

| Download |
| --- |

---
*Kaynak: `BAZI İÇERİK KODLARI/KODLAR/Kodlar4.doc` — mine — 2002*
