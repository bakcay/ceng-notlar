# Bazi İçerik Kodlari

| 27- Sürükle-bırak (drag-drop) tekniği |
| --- |

Aslında windows'un en temel, en kullanılan özelliğidir ama nedense bu konuyu anlatmak en sona kaldı. Sürükle-Bırak'la kastedilen, hepinizin de bildiği gibi, mouse ile bir nesneyi tutup (yani nesnenin üzerine mouse ile gelip mouse'un sol tuşuna basmak) taşımak ve sonra da başka bir nesne üzerine bırakmaktır. Burada sürükle (drag) ve bırak (drop) iki temel hareketimizi oluştururken buna bağlı olarak da iki temel olay bulunmaktadır: DragOver ve DragDrop. DragOver olayı, sürükleme sırasında bir nesnenin üzerine gelindiğinde gerçekleşir. DragDrop olayı ise taşınan nesnenin başka bir nesne üzerine bırakılması sonucunda gerçekleşir. Örnek programı inceleyerek bu iki olayın nasıl kullanıldığına dikkat edin.

| Download |
| --- |
| 26- Sayı Yuvarlama |

Bir stok yönetim programı yaptığınızı düşünün ya da bir personel yönetim ve bordro programı üzerine çalıştığınızı varsayın. Diyelim ki stoktaki ürünlerin fiyatını ya da personel ücretlerini yeniden belirleyeceksiniz. Yapılacak işlem çok basittir. Tüm kayıtların birim fiyatları zam miktarı ile çarpılır ve elde edilen sonuç yeni birim fiyatlar olarak kaydedilir. Ama burada bir sorun ortaya çıkar: Örneğin 125,450,000 TL değerindeki bir ürün fiyatına %12 zam yaptınız. Yukarda bahsettiğimiz şekilde yeni fiyatı belirlersek yeni birim fiyat 140,504,000 olacaktır. Bu değer pek uygun bir değer değildir. Aslında 140,500,000 şeklinde bir değer olması daha düzgün olacaktır. İşte burada bahsettiğimiz sayı yuvarlama ile bu sorunu gidermemiz mümkün olacaktır. Örnek programda, belirtilen sıfır miktarına göre sayının nasıl uygun bir değere yuvarlandığı görülmektedir. Sıfır sayısını belirtip yuvarla dediğinizde sayı, ya yukarı ya aşağı ya da orta değere yuvarlanmaktadır. Yalnız bu programın bir kısıtlılığı var: Küçüklü büyüklü tüm sayılar aynı miktarda sıfıra yuvarlanmaktadır. Onun yerine sayının büyüklüğüne göre bir değere yuvarlamak daha profesyonelce olacaktır. Yani 134,535 sayısı ile 134,535,345 sayısı farklı sıfır miktarına yuvarlanmalıdır. Örnek programı revize edip bahsettiğim bu kıstasa göre yuvarlatmayı size bırakıyorum.

| Download |
| --- |
| 25-Dijital gösterge |

7-segment gösterge yöntemi en tanıdık sayısal gösterim biçimidir. Dijital saatlerde ya da çarşı-pazarlarda gördüğünüz saat ve sıcaklık göstergeleri bu yöntemi kullanırlar. Bu gösterim için elbette ki hazır OCX'ler bulunur ama buna gerek kalmadan da istediğimizi yapabiliriz. Bu gösterim biçiminde her bir çizgi bir harfle isimlendirilir. Uygulamamızda da ilgili çizgiler bu harfleri taşıyan segment adlarıyla isimlendirildi. Detaylara inmiyorum. Sırasıyla en üstteki çizginin a-segmenti, sağ üstekinin b-segmenti ...vs olarak isimlendirildiği bu gösterim biçiminde, dijital bir sayının nasıl gösterildiğini inceleyerek anlamayı size bırakıyorum. Bu örneği kullanarak dijital bir saat yapmak da artık size kalmış.

| Download |
| --- |
| 24- DataGrid içinde ComboBox kullanarak veri girişi |

Bir grid içinde ComboBox, CheckBox gibi kontrolleri kullanarak veri girişi yapmak, profesyonel uygulamalarda yer vermemiz gereken yaklaşımlardan biridir. Örnek çalışmamızda bir DBGrid içinde ComboBox kullanımına yer verilmiştir. Örnek veri dosyamızda üç veri alanı bulunan bir tablo yer almaktadır. Bu veri alanlarından ilki adsoyad, diğer ikisi ise doğum yeri ve meslek bilgisidir. Doğum yeri ve meslek bilgisi girişi ComboBox'tan seçim yaparak gereçekleştirilmektedir. Kullanılan teknik şudur: İki adet ComBox projeye ilave edilmiştir. Biri Şehir bilgilerini diğeri de meslek bilgilerini tutmaktadırlar ve Visible propertileri false durumdadır. Doğum Yeri ya da meslek sütununa gelindiğinde ilgili grid hücresinin satır ve sütun adresleri belirleniyor. Sonra da ilgili ComboBox oraya getiriliyor ve Visible propertisi true yapılıyor. Böylece kullanıcı ComboBox'tan seçimini yapıyor. Seçim yapıldığı anda da ComboBox'ın içeriği DBGrid hücresine yazılıyor.

| Download |
| --- |
| 23- DataReport'un ADO DC ile kullanımı |

DataReport veri kaynağının ille de DataEnvironment belirlenmesi gerekmemektedir. Örneğin Aktif data kontrollerini de bu amaç için kullanmak mümkündür. Hatta program içinde veri kaynağını değiştirebilmek, SQL sorgularını veri kaynağı olarak atamak mümkündür. Örnek programımızda da bir ADODC kullanılmış ve bir SQL sorgusuna yer verilmiştir. DataReport için de basit bir tasarım kullanıldı. Tasarım sırasında yapacağınız tek şey, detail kısmındaki metin kutularının "Data Field" propertisine tablodaki alan adlarını vermek olacaktır. Örnek veri kaynağı olarak Biblio.mdb kullanıldı. Çalıştırabilmeniz için bilgisayarınızdaki yolu burada tanımlamanız gerekiyor.

| Download |
| --- |
| 22- Uygulama penceresinin animasyonla kapatılması |

Bu uygulamamız oldukça basit. Özelliği ise uygulamalarınıza bir değişiklik katması. Olan şu: Uygulamanızı kapattığınızda pencere hemen kapanmıyor. Onun yerine pencere, yukarıya doğru panjur gibi açılıyor ve sonrasında kapanıyor. Bu animasyonu gerçekleştirmek için bir timer kontrolü kullanıldı. Timer kontrolu başlangıçta pasif durumda. Kullanıcı kapat tuşuna ya da pencerenin close tuşuna bastığında timer kontrolu aktif hale getiriliyor dolayısıyla animasyon devreye giriyor. Artık, bu basit animasyonu uygulamalarınıza katmak size kalmış durumda.

| Download |
| --- |
| 21- Resimli menü kullanımı (API) |

Office 2000 ile birlikte gelen görsel yeniliklerden biri menü komutlarının yanında o komutla ilgili bir bitmap resim bulunmasıydı. Bu özelliği VB ile yapacağımız uygulamalarda da gerçekleştirebiliriz. Ancak bunu VB ile doğrudan gerçekleştirmemiz mümkün değildir. API, VB'in yetersiz kaldığı bu durumlarda imdadımıza yetişmektedir. Buradaki örneğimizde bu işi mümkün olduğunca basit bir şekilde gerçekleştirdik. Örneğimizin tek kısıtı bitmaplerin 13\*13 piksel boyutunda hazırlanmak zorunda olmasıdır. Windows'un normal boyutundaki komut bitmapleri 16\*15 piksel boyutundadır. Bu resimleri doğrudan kullanırsanız maalesef kırpılacaktır.

Gelelim programa. Dört tane API fonksiyonu kullanıldı:

**GetMenu**: Menünün windows bağlantı değerini (hWind özelliğini) verir.

**GetSubMenu**: Yukardaki fonksiyonla elde edilen bağlantı değerini kullanılarak istenilen menü komutunun kimlik (ID) değerini verir.

**GetSubMenuID**: Yukardaki fonksiyonla elde edilen menü komutu kimlik değerini kullanarak o komuta ait istenilen alt menü komutunun kimlik değerini verir.

**SetMenuItemBitmaps**: İşi yapan komut yani yukardaki fonksiyonlarla elde edilen değerleri kullanarak istenilen alt menü komutunun basılı (pressed) ve basılmamış (unpressed) resimlerini uygular.

Bu komutların deklerasyonu projeye eklenen bir modülde yapıldı. Zaten API kullanımında ilk kural budur. Örneğimizde bir de İmageList kontrolu kullandık. Bu kontrol menülerde kullanacağımız bitmapleri tutmak için kullanılmıştır. Kontrolun properti penceresinde custom'u tıklayarak kullanacağınız bitmapleri yükleyebilirsiniz. Bu işlemi yaptıktan sonra bitmap orijinal dosyalarını, artık uygulamanın yükleme disketine koymaya gerek yoktur.

| Download |
| --- |
| 20- Metin Dosyalarında Bul ve Değiştir işlevi |

Bir metin içinde bir kelime aramak ya da metin içinde yer alan bir kelimeyi başka bir kelime ile değiştirmek profesyonel uygulamalarda yer alan işlevlerdir. Gerçekte, InStr fonksiyonu ile aranılan kelimeyi bulup, Mid fonksiyonu ile bu kelimeyi yeni kelime ile değiştirmek teorik olarak basit bir işlem olarak görülmektedir. Ama uygulamada durum maalesef öyle olmamaktadır. Örnek programda bu işleme yer verilirken yine de gözden kaçan buglar olmuştur. Bazı run-time hatalarını bile gözden kaçırmış olabilirim. Programımız verilen kelimeyi metin dosyası içinde bulup o noktaya imleçi konumlandırabilmektedir. Ayrıca bu kelimenin birini ya da hepsini başka bir kelime ile değiştirmeniz de mümkündür. Ancak bazı eksikler bulunmaktadır. Aranılan karakter dizisi bir kelime mi yoksa bir kelimenin parçası mı? Bu durum her iki şekilde dikkate alınmalıdır. Örneğimizde aranılan karakter dizileri bir kelimenin parçası olarak ele alınmıştır. Dolayısıyla ben "manken" diye bir kelime ararken program bana "mankenler" şeklindeki bir kelimeyi bulabilmektedir. İkinci bir eksiklik ise büyük/küçük harf ayrımı yapıp yapmama durumu ki örnek programımız maalesef yapıyor. Yani "windows" diye bir kelime ararsam eğer, program maalesef "Windows" kelimesini bana göstermiyor. Artık bu eksiklikleri tamamlamak sizin göreviniz. Programcılık kolay değil.

| Download |
| --- |
| 19- Uygulamalara komut satırından parametre geçmek |

Bir Excel dosyasını açmak için Excel'i çalıştırıp dosyayı açmak gerekmez. Dosyayı, sürükle-bırak tekniğiyle Excel uygulamasının üzerine getirerek ya da doğrudan dosya üzerine çift tıklayarak da açabilirsiniz. Çünkü dosyayı tutup Excel uygulamasının üzerine bıraktığınızda ya da dosyaya çift tıkladığınızda Excel programı otomatik olarak çalışır ve dosyanın adı Excel programına bir parametre olarak sunulur. Tüm bunları Windows yapar. Sonrasında ise Excel bu parametreyi bir dosya adı olarak algılar ve açar. Çünkü Excel'i geliştiren programcılar bunu böyle tanımlamışlardır. Siz de uygulamalarınızda böyle bir tanımlama yaparak örneğin bir metin editörü yaptıysanız tüm metin dosyalarını, adlarını parametre olarak kullanarak açıp işleyebilirsiniz.

Bu dersimizde komut satırındaki parametrenin program içinde nasıl kullanıldığı anlatılmaktadır. Uygulamamızın komut satırında yer alan parametreler Command() fonksiyonu ile okunur.

```vbnet
KomutParametresi=Command()
```

Örnek uygulamamızda, komut satırıyla gelen parametrenin bir metin dosyasının adı olduğu kabul edilerek, dosya açılıp içeriği bir metin kutusuna aktarılmaktadır. Örnek uygulamanın komut satırları arasında gerekli açıklamalar yapılmıştır. Uygulamanın EXE haline BenimEditör.EXE adını verdim. Açtığı dosyaların uzantısını da .benim olduğunu varsaydım ve örnek bir metin dosyası da koydum.

Şimdi de bu işlevi devreye sokmak için Windows tarafında neler yapmanız gerektiğini anlatayım: Windows Explorer'ı çalıştırın. Menüden Görünüm-Klasör Seçenekleri'ni çalıştırın. Dosya türleri tabını tıklayın. Yeni tür tuşuna basın. Tür açıklamasına "BenimEditör metin dosyaları" yazın. İlişkilenen uzantıya "benim" yazın. Eylemler kısmında "Yeni" tuşuna basın. Eylem kutusuna "open" yazın. Uygulama adı için de "Gözat" tuşuna basarak örnek uygulamanızın yolunu belirtin. Bu kadar. Şimdi örnek metin dosyası "Deneme.benim" i "BenimEditör.exe" üzerine getirip bırakın. Program otomatik olarak çalışacak ve metin dosyası açılacaktır. Deneme.benim'e çift tıklarsanız bu işlemin yine gerçekleşmesi için BenimEditör.EXE programının Windows'a kaydedilmesi gerekmektedir. Bunun en kolay yolu da uygulamanız için bir setup programı hazırlayıp Windows'a bu şekilde kurmanız gerekmektedir (bakınız: Package & Deployment Wizard'ın kullanımı).

| Download |
| --- |
| 18- En son açılan dosyaların menüde kaydını tutmak |

Word, Excel gibi uygulamalarda dikkatinizi çekmiştir: O güne kadar açtığınız dosyaların menüde bir kaydı tutulmaktadır. En son açtığınız 9 dosyanın adı, menüde komut olarak yer almakta ve bu komutlara tıkladığınızda ilgili dosya açılmaktadır. Bu işlevi siz de uygulamalarınıza koyduğunuzda profesyonel bir çalışma elde etmiş olabileceksiniz.

Yapılan işlem çok basittir. Menü tasarımı sırasında fazladan komutlar yerleştirmek yeterli olmaktadır. Örneğimizde 4 adet dosya komutu işleme koyduk. Bu dosya adları için menüye konulan bu 4 komutla birlikte bir de seperatör kullanıldı. Seperatör ve dosya komutlarının adları, programlamada kolaylık olması için aynı yapıldı ve her birine 0-4 arası bir indis değeri verildi. En son açılan dosyaların sayısı ve adları "PROJECT.INI" isimli bir dosyada tutulmaktadır. Program çalıştırıldığında bu dosya okunmakta ve her dosyanın adı komut başlıklarına yazılmaktadır. Sonrasında da hem seperatör hem de komutlar görünür yapılmaktadır. Eğer en son açılan dosya sayısı 4'ten az hatta 0 ise (ki bu uygulama ilk çalıştırıldığında doğal olarak bu değer 0'dır.) seperatör de dahil olmak üzere dosya komutları görünmez yapılmaktadır.

Yeni bir dosya açıldığında, tüm dosya adları bir sıra geriye kaydırılmakta (dördüncü dosya atılmakta) ve son açılan bu dosya ilk sıraya konmaktadır. Bu işlem hem menü hem de PROJECT.INI dosyası için yapılmaktadır. Uygulamamızda dosya açma işlemi hayali olarak yapılmaktadır. Dosyanın adı uygulama başlığına yazılmakta ve bir metin kutusu görünür yapılmaktadır. Dosya kapatıldığında ise form başlığı default değere getirilmekte ve metin kutusu görünmez yapılmaktadır.

| Download |
| --- |
| 17- Menü Editörünün kullanımı ve menü tasarımı |

Uygulamaların vazgeçilmez bir olgusu da menülerdir. Visual Basic'le oluşturacağımız uygulamalar için, menü editörü aracılığıyla kolayca menü tasarlayabiliriz. Menüden Tools-Menu Editor komutunu işlettiğinizde aşağıdaki ekran karşınıza çıkacaktır. Bu pencerede şu an örnek uygulamamızın menü yapısı görülmektedir. Menü tasarımına geçmeden önce menülerle ilgili bir kaç açıklama yapmakta yarar var. Her uygulamada bir menü bar yer alır. Menü bar üzerindeki komutlardan birine tıklayınca onunla ilgili, popup menü dediğimiz bir alt menü açılır. (Çok nadir de olsa, bazen bu menü komutlarının bazılarına popup menü konmayabilir. Örneğin "Çıkış" isimli tek bir komut da bulunabilmektedir.) Bu alt menüde işlemlerimizi yaptığımız komutlar bulunmaktadır. Bu komutlar bazen seperatör denilen çizgilerle bölümlendirilmiş de olmaktadır. Bir sonraki resimde uygulamamızın ana penceresinde menünün açılımında bunu görebilirsiniz. Bunun dışında bazı menü komutlarının silik olduğunu yani kullanım dışı bırakıldığını da görebilirsiniz. Tüm bunlar menü tasarımında bizim de ele alacağımız uygulamalardır.

Şimdi menü editörünün kullanımına gelebiliriz. Caption satırına menü komutunun, menü barda kullanıcıya görülecek olan başlığı yazılır. Name satırına ise menü komutunun programlama sırasında kullanacağımız adı yazılır. Çünkü formlarımızda yer alan her kontrol gibi menü komutlarının da bir adı bulunmaktadır. Bazen birkaç menü komutu için aynı adı kullanma durumu olabilir. Bu durumda her komut için bir sıra numarası kullanırız ve index satırında da bu değer yazılır. Eğer komutlar arasında seperatör (ayraç) kullanmak isterseniz, caption satırına "-" koymanız yeterlidir. Menü editörü penceresinin tam orta yerinde CheckBox'lar bulunmaktadır. İlk üçünün açıklaması şöyle: İlki menü komutuna tik atılıp atılmayacağını belirtmek için kullanılır. Örneğin menüdeki bir komut bilgisayarın sesinin açık olup olmadığını göstermek için kullanılabilir. Bu durumda eğer ses açıksa bu komutta tik işareti bulunur yoksa bu işaret bulunmaz. İkinci ChechBox menü komutumuzun aktif ya da pasif olmasını belirtmek için kullanılır. (Silik komutları hatırlayın). Üçüncüsü de komutumuzun görünür ya da görünmez olmasını sağlamak için kullanılır. Tüm bu checkbox değerleri ve caption değeri program içinde değiştirilebilmektedir. (Örneğimizde göreceksiniz)

Pencerenin orta solunda yer alan oklar, seçili olan menü komutunu sol, sağ, yukarı ve aşağı yönlerde kaydırmak için kullanılır. Bu tuşların hemen sağındaki Next, Insert ve Delete komutları ise sırasıyla bir sonraki komuta geçmek, o anki komutun yanına yeni bir komut tanımlamak için boşluk açmak ve o anki komutu silmek için kullanılır. Menü editörünün kullanımı konusunda daha fazla kafa karıştırmamak için şimdilik bu kadarla yetinebiliriz.

Örneğimize gelince, menü bara iki tane komut koydum. İlkini zaten görüyorsunuz. Burada iki tane komut ilk anda pasif durumdadır. Çünkü uygulamamız ilk çalıştığında elimizde açık bir dosya olmayacağı için kapat ve Yazdır komutlarının da kullanılma durumu olmayacaktır. Bu komutlar, Yeni ya da Aç komutlarıyla bir dosya açıldığında program içinde aktif hale getirilmektedir. İşlem komutunda ise açılan popup menüde tek bir komut bulunmaktadır: Kayan Yazı. Bu komutta tik işlevine yer verdik. Bu komut tıklandığında yanına bir tik işareti konmakta ve form üzerindeki etiketin içeriği kayan yazı moduna geçmektedir. Tekrar tıklandığında ise komutun yanındaki tik kaldırılmakta ve kayan yazı modu iptal edilmektedir.

| Download |
| --- |
| 16- Hata denetimi |

Tüm programlama dillerinde kendini hissettiren bir ihtiyaç vardır. Çalışma zamanında, kullanıcının yanlış yönlendirmelerinden kaynaklanabilecek hataların (Run-time hataları) denetim altına alınması. Örneğin belli bir isimle bir dosyayı kaydetmek istediğinizde, eğer o isimde bir dosya ilgili klasörde zaten varsa bir run-time hatası oluşacaktır. Yine örneğin bir integer tipi değişkene bir aritmetik işlem sonucunda, integer tipi değişken sınırlarının dışında kalan bir değer atanmaya kalkışıldığında ya da olmayan bir veri dosyasını açmaya çalıştığınızda, bir pencerenin width propertisine bir şekilde negatif bir değer ataması yapıldığında ya da bir metin kutusuna bir "Null" değer atamaya kalkışıldığında, bahsettiğimiz çalışma zamanı hataları oluşacaktır. Eğer bu hataları öngörüp denetim altına almazsanız projeniz "bug"larla dolu bir çalışma olacaktır. Bu hataların denetim altına alınması ON ERROR komutuyla gerçekleştirilmektedir.

Duruma göre kullanılan üç farklı şekli bulunmaktadır.

`ON ERROR GOTO satıradı` : Hata durumunda programın, satıradı ile isimlendirilmiş olan satırına gidilir.

`ON ERROR RESUME NEXT` : Hata durumunda bir sonraki komut işleme konur.

`ON ERROR GOTO 0` : Hata denetimi pasifleştirilir.

Bu kullanım şekillerinden üçüncüsü hata denetimini iptal etmek için kullanılır. Detaylı bir açıklamaya gerek bulunmamaktadır. İkinci kullanım şekli ise hatanın oluştuğu program satırının gözardı edilmesini sağlamak ve bir sonraki komutu işleme koymak içindir. Bu komut için de detaya inmeye gerek bulunmamaktadır. Geniş şekilde ele alacak olduğum kullanım şekli ilkidir. Bu kullanım şekli ya hatayı gidermek için alternatif bir çözüm üretmekte ya da kullanıcıyı hata konusunda bilgilendirmek için kullanılmalıdır. Aşağıda, kullanıcıyı hata konusunda bilgilendirme yönünde basit bir örnek kullanım şekli yer almaktadır:

```vbnet
Private Sub Command1_Click()
On Error GoTo hata
Open "testdosyasi.txt" For Input As #1
'
'
'Bu kısımda, dosya üzeinde işlem yapan komutlar yer almaktadır.
'
On Error GoTo 0
Exit Sub
hata:
mesaj = MsgBox("Bir hata oluştu" + Chr(13) + "Hata Kodu: " + Str(Err.Number) _
+ Chr(13) + "Hata Adı: " + Err.Description)
On Error GoTo 0
End Sub
```

İlk komutla, hata oluşması durumunda "hata" adındaki satıra gidileceği yorumlayıcıya bildirilmiş oldu. İkinci komutla bir dosya okuma amaçlı olarak açılmak isteniyor. Eğer bahsi geçen dosya bu uygulamanın çalıştığı klasörde varsa sonraki komutlar işleme konacak ve Exit Sub komutuyla prosedür sonlandırılıp bu prosedürün çağrıldığı yere gidilecektir. Ancak eğer bu dosya klasörde yoksa o zaman run-time hata oluşacaktır ve ON ERROR komutuyla, daha önceden belirtilmiş olan satıra yani "hata" isimli satıra gidilecektir. Burada kullanıcıya bir mesaj verilmektedir. Hatanın kodu ve açıklaması. Kullanıcı bu kodu ve açıklamayı alıp program satıcısı ile yani sizle bağlantı kurarak bu hatanın giderilmesini talep edebilecektir. (Hata kodu ve açıklamasının Err nesnesinin Number ve Description propertileriyle elde edildiğine dikkat ediniz)

Kullanıcının hata konusunda bilgilendirilmesini gördük şimdi de hatanın giderilmesine bir örnek verelim.

```vbnet
Private Sub Command1_Click()
On Error GoTo hata
Open "testdosyasi.txt" For Input As #1
On Error GoTo 0
Exit Sub
hata:
Open "testdosyasi.txt" For Output As #1
Open "testdosyasi.txt" For Input As #1
On Error GoTo 0
End Sub
```

Yine aynı örnek. İlk komutta dosya Input modunda açılıyor. Eğer dosya yoksa hata satırına gelinecek ve burada dosya önce Output modunda açılacak (dolayısıyla dosya klasörde oluşturulacak) sonra da Input modunda açılacak. Sonuç olarak bu prosedürün çalıştırılmasının ardından öyle ya da böyle kullanıcının elinde Input modunda açılmış bir dosya olacaktır.

| Download |
| --- |
| 15- Kayan yazı oluşturmak. |

Timer kontrolu araçılığıyla yanıp sönen metin oluşturma uygulamasındaki taktiğin aynısını kayan yazı oluşturmada da kullanabiliriz. Yapılacak işlem, belli zaman aralıklarında, metnin ilk harfini kesip metnin sonuna eklemek olacaktır. İlk harfi Left fonksiyonu ile alıp geri kalan metni de right fonksiyonu ile ayırırsak bu kesme işlemi gerçekleştirilmiş olacaktır.

| Download |
| --- |
| 14- Uygulama penceresinin başlığına animasyon katmak |

Uygulama penceresi için animasyonlu ikon oluşturmaya benzer şekilde animasyonlu başlık oluşturmamız da mümkün. Yapacağımız tek şey, bir önceki uygulamaya benzer şekilde bir timer kontrolu aracılığıyla belli zaman aralıklarında pencere "Caption" propertisini değiştirmek olacaktır.

| Download |
| --- |
| 13- "Bu ekranı bir daha gösterme" penceresi |

Uygulamaların ana penceresinden önce aşağıdaki gibi bir pencere ile her zaman karşılaşabilirsiniz. Hatta windows'u ilk çalıştırdığınızda bir "Windows Tur" penceresi karşınıza çıkar ve her çalıştırdığınızda bu pencerenin karşınıza çıkmaması için aşağıdada görüldüğü gibi, "Bir daha gösterme" açıklamalı bir CheckBox yer alır. Bu kutuyu işaretlediğinizde bu ekran bir daha karşınıza çıkmaz. Yapılan işlem çok basittir. Bir "PROJECT.INI" dosyası tanımlamamız gerekiyor. Bu dosyada aşağıdaki kutuya verilen cevap yer alacaktır. Bu ekran gelmeden önce bu dosyaya göz atılmakta eğer dosya hiç yok ya da içeriği olumsuz ise uyarı ya da açıklama taşıyan bu pencere ekrana gelmekte aksi taktirde ana pencere doğrudan ekrana gelmektedir.

| Download |
| --- |
| 12- Kontrolların boyutlarının programın çalışması sırasında değiştirilmesi |

Uygulama penceremizin boyutlarını, kenarlarından tutup çekerek büyültüp küçültmemiz, kullandığımız işletim sisteminin sayesinde mümkündür. Uygulamamızın içinde yer alan kontrollar için de, özel bir kod yazarak bunu başarabiliriz. Örnek uygulamamızda dizin penceresini dar tutup, dosya listesini geniş tutmayı ya da bunun tersini yapmayı isteyebiliriz. Her iki pencerenin birleşme noktasında mouse göstergesi sağa-sola yön şekline dönüşmekte ve bu anda sol tuşa basıp mouse sağa-sola kaydırdığımızda her iki kontrolun boyutları değişmektedir. Kolay gibi görünen (belki de zor gibi görünen) bu işlem MouseMOve, MouseDown ve MouseUp olayları ile gerçekleştirilmektedir.

MouseMove olayında mouse'un konumu irdelenmekte ve mouse, boyutlarını değiştireceğimiz iki kontrol öğesinin arasına geldiğinde mouse göstergesi sağa-sola yönlenme şekline dönüştürülmekte, aksi taktirde olağan şekline bürünmektedir. Sağa-sola yönlenme şekline dönüştüğünde yani mouse, boyutları değiştirme bölgesine geldiğinde, MouseDown olayı ile mosue'a basılıp basılmadığı takip edilmekte ve basılmışsa bir değişken (Basılı) True yapılmaktadır. MouseUp olayı ile de mouse'ın bırakıldığı belirlenmekte ve bu değişken (Basılı) False yapılmaktadır. Kontrol boyutlarının değiştirilmesi ise yine MouseMove olayında gerçekleştirilmektedir. MouseMove olayında Basılı isimli mantıksal değişken sorgulanmakta ve eğer bu değişkenin değeri True (yani mouse basılı) ise, her iki kontrol sağa ya da sola doğru, mose'un hareket miktarı kadar genişletilip daraltılmaktadır. Mouse'uın hareket miktarı ise XOnce değeri sayesinde mouse'un bir önceki konum değeri ile son andaki konum değeri arasındaki fark alınarak elde belirlenmektedir..

| Download |
| --- |
| 11- Uygulamalara demo özelliği vermek |

Oluşturduğunuz bir uygulamanın deneme amacıyla bir kullanıcıya vermeniz gerektiğinde, uygulamanın tamamını değil de bir demosunu vermek daha uygun olacaktır. Burada uygulamamızın nasıl demo haline getirildiğini göreceğiz. İki farklı demo örneğine yer verdik. İlkinde 30 adet kullanımdan sonra uygulamayı devre dışı bırakan bir demo ikincisinde ise uygulamanın "Yazdır" komutunu sürekli olarak kullanım dışında tutan bir demo örneği kullandık. Bir şeyi göz önünde bulundurmanızı istiyorum: Burada verdiğimiz demo örneği benim tarzımdır. Siz bu örneklerden yola çıkarak daha güvenli olabilecek bir tarz oluşturabilirsiniz.

Demo uygulamalarının kilit konusu şifrelemedir. Uygulamanız için bir seri numarası belirlemeniz ve bu seri numarasının kırılmaması için de gerekli şifrelemeleri yapmanız gerekmektedir. Şİfrelemenin çok çeşitli yöntemleri vardır. Burada en basit şifreleme tekniği olan X-OR yöntemini kullandık. En basit diyoruz çünkü bu iş için zaten hazır bir komut bulunmakta ve şifreyi deşifre etmek için de yine aynı komutu kullanmak yeterli olmaktadır.

İkinci kilit konu şifrelemelerle ilgili verilerin saklanacağı dosyalardır. Uygulamamızda "PROJE.INI" ve "SERIAL.TXT" adlı iki dosya kullandık. İlk dosyada programın şifrelenmiş seri numarası ile o ana kadar ki kullanma sayısı saklanmaktadır ve bu dosya, uygulama kullanıcıya verilmeden önce oluşturulmaktadır. İkinci dosyada ise kullanıcı tarafından program çalıştırıldığında oluşturulmaktadır ve kullanıcının seri numarası açık olarak burada tutulmaktadır.

Öncelikle PROJE.INI dosyasını oluşturmak için bir program yazmamız gerekmektedir. Program bir anahtar kelime ile sizin bu uygulamanız için belirlediğiniz seri numarasını X-OR'lamaktadır. Daha sonra bu değeri hexadecimal forma dönüştürmektedir. Bu değerin arkasına yine hexadecimal formda uygulamanın ilk kullanım değeri olan 01 eklenmektedir. Tüm bu sayısal değerler tek satır halinde PROJE.INI dosyasına yazılmaktadır.

## Download

Şimdi gelelim uygulamaya. Her iki örnekte de Splash ekran taktiği kullanılmıştır. İlk olarak Form değil Sub Main prosedürü içeren bir modül çalışmaktadır. Önce PROJE.INI dosyasından seri numarası ve kullanım sayısı verileri okunmaktadır. Sonra da eğer varsa SERIAL.TXT dosyasından kullanıcının seri numarası okunmaktadır. (Eğer bu dosya yoksa zaten kullanıcı seri numarası değeri diye bir şey olmayacaktır.) Sonra da bu iki değer karşılaştırılmaktadır. Karşılaştırma sonucu iki değer birbirine eşit çıkarsa uygulamamızın ana penceresi Form1 devreye sokulacaktır. Eşitlik durumu olmazsa (ki bu, kullanıcı seri numarası bildirmemiş demektir) uygulamanın kullanım sayısına bakılır ve kullanım sayısı aşılmışsa aşağıdaki ekran kullanıcıya iletilir.

Kullanıcı burada seri numarasını girmek zorundadır. Ya da programı kapatacaktır. Eğer seri numarası girerse bu değer uygulamanın seri numarası ile karşılaştırılır ve doğru değer girildiyse, SERIAL.TXT dosyasına yazılıp uygulama tam sürümüyle kullanıcıya sunulur. Bir daha da bu pencere kullanıcının karşısına çıkmaz. Eğer yanlış değer girildiyse yukardaki ekrana geri döner.

Eğer henüz 30 kullanımlık sınır aşılmadıysa bu sefer şu ekran kullanıcının karşısına çıkar.

Kullanıcı burada Devam tuşuna basarsa kullanım sayısı 1 artırılıp PROJE.INI dosyasına yazılır ve program tam sürüm olarak kullanıcıya açılır. Bu aşamada seri numarası girmek de istenebilir. Bu durumda yukardaki işlemlerin aynısı uygulanır.

## Download

İkinci demo örneğinde ise uygulama sürekli ama kısıtlı olarak kullanıma sunulmaktadır. İlk işlemler yukardaki örnekle aynıdır. Programın ve kullanıcının seri numaralarının karşılaştırılması aşamasında durum değişir. Karşılaştırma sonucunda değerle çakışırsa "Yazdır" komutu aktive edilir. Aksi takdirde şu pencere kullanıcının karşısına çıkar.

Bu aşamada Devam tuşuna basılırsa uygulama sınırlı olarak kullanıma açılır. Tabi seri numarası girmek de istenebilir. Bu durmda yukardaki örnekte yer alan işlemlerin aynısı uygulanır.

| Download |
| --- |
| 10- Timer kontrolu aracılığıyla yanıp sönen etiket oluşturma |

Yine Timer kontrolunu kullanarak Label kontroluna yanıp sönme özelliği verebiliriz. Yapacağımız tek şey belirli aralıklarla etiket metninin rengini, zemin rengi ile kendi rengi arasında sürekli değiştirmek olacaktır.

| Download |
| --- |
| 9- Uygulama penceresi için hareketli ikon oluşturma |

Uygulama pencerenizin ikonunun hareketli olması herhalde ilginç olacaktır. Timer kontrolu aracılığıyla belirli aralıklarla form ikonunu değiştirerek bu isteği gerçekleştirebiliriz. Öncelikle animasyonu oluşturacak ikonları belirlememiz gerekmektedir. Ben örnek olarak ayın, yeniaydan dolunaya kadar olan görüntülerini animasyonda kullandım. LoadPicture komutu ile bu ikonlara ait dosyalar sırayla Form1'in ikon propertisine atanmaktadır. Timer kontrolunun Interval propertisindeki değri değiştirerek hareket hızını ayarlayabilirsiniz.

| Download |
| --- |
| 8- Randomize, Rnd ve rastgele sayı üretme |

İstastiksel amaçlarla ilgili bir uygulama yapacaksanız ya da bir şans oyunu programlamayı düşünüyorsanız rastgele üretilen sayılara ihtiyacınız olacaktır. "Rnd", bu ihtiyaçı karşılayan bir fonksiyondur. Rnd fonksiyonu 0 ile 1 arasında, sıfıra eşit olabilen ama 1'e eşit olmayan 7 ondalık rakamlı bir sayı üretir. Ancak bu sayıyı belli değerlerle çarpıp tamsayı kısmını alırsanız istediğiniz aralıklarda istediğiniz türden sayılar elde edebilirsiniz. Herhangi iki sayı değeri arasında yer alan bir tamsayı üretmenin temel formulü şudur:

```vbnet
Sayi = Int(Rnd*(ÜstSınır-AltSınır+1)) + AltSınır
```

Bu genel formülden yola çıkarak ortaya konmuş, tavla zarı ve yazı/tura atışına kadar varan çeşitli örnekleri aşağıdaki uygulamamızda görebilirsiniz.

## Download

## 7- "MsgBox" fonksiyonunun kullanımı

Bir diyalog penceresi aracılığıyla kullanıcıya bir mesaj gösterir ve kullanıcının bir tuşa basmasından sonra basılan tuşun tamsayı karşılığını verir.

```vbnet
MsgBox(Mesaj,Tuşlar,Başlık,Yardım Dosyası,Konu Numarası)
```

Mesaj: Diyalog penceresinde kullanıcıya iletilecek olan mesaj metni - Gerekli

Tuşlar: Kullanılacak tuşlar ya da ikon tipini gösteren sayıların toplamı - Opsiyonel

Başlık: Diyalog epenceresinin başlık barında yer alması istenilen metin - Opsiyonel

Yardım Dosyası: Tuşlarda Help tuşuna da yer verilmişse kullanılacak olan yardım dosyasının adı - Opsiyonel

Konu Numarası: Help tuşuna basılması durumunda, ekrana gelecek olan metnin konui numarası -Opsiyonel

En çok kullanılan tuş numaralarına örnek verecek olursak:

Tuş Numarası TuşAdı Görüntülenen tuşlar

0 VbOKOnly OK

1 VbOKCancel OK, Cancel

3 VbYesNoCancel Yes, No, Cancel

4 VbYesNo Yes, No

16 VbCritical Kritik mesaj ikonu

48 VbExclamation Uyarı mesajı ikonu

Örnek kullanımlar:

```vbnet
mesaj = MsgBox("Ad Soyad alanını boş geçmeyiniz.", vbOKOnly)
mesaj = MsgBox("Programdan çıkmak istediğinizden emin misiniz?", 20, "Önemli soru")
'4 ve 16'nın toplamı kullanıldı
```

Şimdi de, kullanıcını bu tuşlardan hangisine bastığını belirlemeye geldik. Aşağıda bazı tuşların numara karşılıkları listelenmiştir.

Tuş Adı Numarası

OK 1

Cancel 2

Yes 6

No 7

Yukarıdaki ikinci örneğin sonucunun, program için kullanımı şu şekilde olacaktır:

```vbnet
If mesaj = 6 Then Unload Me
```

## 6- Splash ekran kullanımı

Profesyonel uygulamalarda dikkatinizi çekmiştir. Uygulamayı çalıştırdığınız zaman bir ön pencere açılır ve uygulamaya ait tüm run-time dosyalar yüklenirken ve ön işlemler yapılırken bu pencere ekranda kalır. Sonra da asıl uygulama penceresi ekrana gelir. İşte bu ön pencereye "Splash Ekran" denir. Siz de uygulamalarınıza profesyonellik katmak için splash ekran kullanabilirsiniz. Splash ekran kullanımı aşağıdaki adımlardan oluşmaktadır:

Projeye bir modül eklenir. (Project-Add Module)

Modülde "Main" isimli bir prosedür tanımlanır.

Splash ekran olarak kullanılacak form aktive edilir.

Ön işlemlerle ilgili komutlar devreye sokulur (örneğimizde sistem fontları bir ComboBoxa yüklendi)

Splash ekran UnLoad edilir.

Menüden Project-Properties çalıştırılarak, ekrana gelen pencerede Startup Object olarak Sub Main seçilir.

Örneğimizdeki splash ekran aşağıdaki gibi hazırlanmıştır. Burada bir progressbara da yer verilmiştir. (Bkz. 8- "ProgressBar" kontrolunun kullanımı ) Splask ekran görünürken arka planda da sisteme ait fontlar ana ekrandaki comboboxa yüklenmekte ve bu işlem progressbar aracılığıyla monitör edilmektedir.

Sub Main de önce Form1 (ana ekran) Load edilmiştir. Çünkü arka planda bu formdaki kontrolları kullanabilmemiz gerekmektedir. Sonra da Form2 (splash ekran) show edilmektedir. Sonrasında progressbar için gerekli atamalar yapılmakta ve sisteme ait fontlar ana ekrandaki Combo1'e yüklenmektedir. İşlemin sonunda Form2 unload edilmekte ve ana ekran (Form1) show edilmektedir.

| Download |
| --- |
| 5- TextBox'ta konumlanılan satır numarasının belirlenmesi |

Multiline özelliği true yapılmış olan bir metin kutusuna çok satırlı metin girişi yapabilirsiniz. Ve bu veri girişi sırasında kaçıncı satırda olduğunuzu bilmek isteyebilirsiniz. Bunun çözümünde şu özelliği kullanacağız: Her satırın sonunda görünmeyen iki karakter bulunmaktadır: Satır sonu (Ascii=13) ve satır yedirme (Ascii=10). Mid fonksiyonuyla, bulunulan noktaya kadar olan bu karakter çifti sayılmaktadır. Çıkan değer imleçin kaçıncı satırda olduğunu bize verecektir. Peki imleçin konumu nasıl belirleniyor? Tabii ki SelStart propertisi ile.

Bu programa ilave bir özelliği de siz kazandırabilirsiniz: Kullanıcı, örneğin 106. satıra gitmek isteyebilir. Bunu çözmek size düşüyor.

| Download |
| --- |
| 4- String veritipleriyle işlemler |

Word kullandığınız için mutlaka görmüşsünüzdür: "Biçim" menüsünde "BÜYÜK/küçük harf değiştir" diye bir komut vardır. Buradaki örnek uygulamamızda, string veriler üzerinde neleri nasıl yapabileceğimizi göstermek için Microsoft Ofis'in bu özelliğini taklit ettik. Program kaynak kodunda yer alan açıklama satırlarından, bir sonraki komutla ne yapılmak istendiği belirtilmiştir. Burada belirtmek istediğim bir kaç noktadan biri şudur. UCase ve LCase fonksiyonları ı,i,I, ve İ harflerinde maalesef türkçeye uygun sonuç vermiyor. O yüzden biz kendi özel dönüştürme fonksiyonlarımızı tanımladık. Diğer nokta da şu: Ofis'te yer alan "bÜYÜK/kÜÇÜK dÖNÜŞTÜR" komutuna yer vermedik. Yani metin içinde yer alan tüm küçük harflerin büyüğe, büyük harflerin de küçüğe dönüştürme işini size bıraktık.

| Download |
| --- |
| Sayıların yazıya dönüştürülmesi |

Bordro ya da muhasebe ile ilgili bir uygulamada ihtiyaç duyacağımız rutinlerden biridir sayıları metne dönüştürmek. Bu iş için download sitelerinde mutlaka bir rutine rastlamışsınızdır. Aşağıdaki uygulama bunlara ilave olarak, programcılık mantığınızı geliştirmek açısından farklı bir yaklaşımla bu konuya değinmektedir.

Doğal olarak, deklerasyon bölümünde bazı değişkenler tanımlanmış Form\_Load prosedürüyle de onlara program içinde kullanacağımız değerler atanmıştır. Programda bir de fonksiyon tanımlandı. Ucrakam isimli bu fonksiyon kendisine string olarak gelen üç rakamlı bir sayıyı metine dönüştürüyor. Programımızda metne dönüştürülecek olan sayı üç rakamlı dilimlere bölünerek bu fonksiyona gönderiliyor. Her parçanın sonuna da dilimin adı yani bin, milyon, milyar ...vs yerleştiriliyor. Programın yapısını anlayabilmeniz için şu küçük açıklamayı da yapayım. Metne dönüştürülecek olan sayı önce string forma alınıyor. Sonra For..Next döngüsü içinde Left fonksiyonu ile bu stringin son üç karakteri alınıp ucrakam fonksiyonuna gönderiliyor. Right fonksiyonu ile de son üç karakter atılıp kalan karakterlerle işleme devam ediliyor. Bu prgramla katrilyondan daha fazlası tanımlanmamıştır. Ama binler dizinini ve for..next döngüsünü 5 yerine 6 ya da daha fazla yaparak programın kapasitesini artırabilirsiniz.

| Download |
| --- |
| Uygulamaların kontrollu olarak kapatılması |

Oluşturulan dataların ya da dosyalar üzerinde yapılan değişikliklerin, uygulamanın kapatılması sırasında kullanıcının unutkanlığı yüzünden kaybolmaması için, güvenlik altına alınması gerekmektedir. Bu da uygulamalarımızda her zaman yer verdiğimiz "kapat" komutuna özel bir rutin yerleştirerek sağlanabilir. Ancak kullanıcı, uygulama penceresinin sağ üst köşesinde yer alan ve pencerenin kendisine ait olan "Close" tuşuna da basabilir. İşte bunun da bir şekilde de denetim altına alınması gerekmektedir. Aşağıdaki örnek programda "Unload" işlemi üç şekilde denetim altına alınmaktadır. Pencereye konmuş olan bir Command butonu, menüye yerleştirilmiş bir "Çıkış" komutu ve formun kendisine ait olan "Close" komutu bu örnek uygulamada kombine olarak denetim altına alınmıştır. Command1'in click programının hepiniz için anlaşılır olduğunu sanıyorum. Size "unload" olayının denetimini anlatayım. "Unload" olayı, form kapatıldığında gerçekleşir. Bu da uygulamada yer alan bir unload komutu ile ya da formun kapat tuşuna basılması ile gerçekleşir.

```vbnet
Private Sub Form_Unload(Cancel As Integer)
```

Burada yer alan cancel parametresine uygulama içerisinde bir değer atayarak uygulamanın geleceği belirlenebilir. 0 değeri atanırsa form kapanır, sıfırdan farklı bir değer atanırsa formun kapatılmasına izin verilmez. Örnek uygulamamızda kullanıcının, Msgbox aracılığıyla kendisine sorulan soruya verdiği cevaba bağlı olarak cancel parametresine değer atanmaktadır. Kullanıcı, değişikliklerin kaydedilmesi sorusuna evet derse ilgili değişiklikler işleme konur ve cancel=0 yapılarak form kapatılır. Hayır derse değişiklikler dikkate alınmaz ve yine cancel=0 yapılır. Eğer kullanıcı iptal tuşuna basarsa cancel=1 yapılarak formun kapatılmasına izin verilmez ve formda kalınan yere geri dönülür. Burada muhtemelen "cikisizni" parametresi dikkatinizi çekmiştir. Bu parametre mükerrer denetim yapmamak için kullanılmıştır. Çünkü menüden yapılan kapatma işlemi ile yapılan denetimlerden sonra unload komutu ile pencere kapatılıyor ve bu da maalesef unload olayını tetikliyor. Bunun sonucunda da ilgili denetim programı tekrar çalıştırılıyor. Bu programda "cikisizni" değerine bakılıyor ve eğer değer true ise denetim yapılmış olduğu için mükerrerlik gerçekleşmiyor.

| Download |
| --- |
| "Context Sensitive - Metin Duyarlı" menü kullanımı |

Bu örnekte, bir kontrol üzerinde sağ klik yapıldığında bir popup menünün devreye sokulması anlatılmaktadır. Bu iş için "popupmenu" komutu kullanılmaktadır.

```vbnet
PopupMenu sag1 'sag1: Örneğimizdeki popup menünün adı.
```

Tasarım sırasında menü editörü ile ilgili popup menü tanımlanır ve visible özelliği false yapılır. Program sırasında ilgili kontrolün MouseUp olayı için küçük bir kod yazılması yeterlidir. Eğer sağ klik yapılmışsa PopupMenu komutuyla popup aktive edilir.

```vbnet
Private Sub DBGrid1_MouseUp(Button As Integer, Shift As Integer, X As Single, Y As Single)
If Button = 2 Then 'Mouseun sağ tuşuna basılmış
PopupMenu sag1
End If
End Sub
```

Geriye popup menümüzün herbir komutu için ilgili kodların yazılması kalmaktadır. Bu örneğimizde VisualBasic'le beraber gelen Biblio.mdb dosyasının verileri kullanılarak DBGrid kontrolüne yer verilmiştir. Programı çalıştırmadan önce, data1 kontrolünün DatabaseName özelliğine kendi bilgisayarınızdaki Biblio.mdb dosyasını tam adresi ile yazın, RecordSource özelliğine de Autors yazın. Visible özelliğini de false yaptıktan sonra, DBGrid kontrolünün DataSource özelliğine data1 yazın. Biblio.mdb dosyasının orijinalliğini bozmamak için popup menüde yer alan "Yeni" ve "Sil" komutları işlevsel olarak kullanılmamışlardır.

| Download |
| --- |

---
*Kaynak: `BAZI İÇERİK KODLARI/KODLAR/Kodlar5.doc` — mine — 2002*
